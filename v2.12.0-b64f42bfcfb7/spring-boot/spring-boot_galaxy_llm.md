# ARCHITECTURAL_BRIEF: spring-boot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spring-projects/spring-boot` |
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
- **Scope:** 9361 analyzed artifact(s), 510598 LOC.
- **Load-bearing artifact:** `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -- 411 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` -- pulls in 151 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `build-plugin/spring-boot-maven-plugin/src/dockerTest/projects/build-image-bindings/bindings/ca-certificates/test.crt` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 11449 |
| Analyzed Artifacts (Scanned) | 9361 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2088 |
| Total LOC | 510598 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 81.8% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6973 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0297 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1514 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 689 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 7752 | 472534 | 82.8% |
| GROOVY | 690 | 18086 | 7.4% |
| XML | 255 | 0 | 2.7% |
| PLAINTEXT | 233 | 39 | 2.5% |
| JSON | 195 | 13166 | 2.1% |
| YAML | 110 | 2301 | 1.2% |
| HTML | 49 | 1280 | 0.5% |
| SQLITE | 23 | 331 | 0.2% |
| KOTLIN | 18 | 1133 | 0.2% |
| MARKDOWN | 12 | 0 | 0.1% |
| PROTO | 8 | 107 | 0.1% |
| SHELL | 6 | 318 | 0.1% |
| RUBY | 3 | 210 | 0.0% |
| CSS | 3 | 9 | 0.0% |
| BATCH | 2 | 102 | 0.0% |
| DOCKERFILE | 1 | 9 | 0.0% |
| JAVASCRIPT | 1 | 973 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 9323 |
| unknown | unknown | 36 |
| cp1252 | cp1252-fallback | 1 |
| latin-1 | latin-1-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 26%, Data / Markup / Trivial 25%, Encapsulated Accessors Files 18%, State Mutators Files 7%, Large Core Modules (3) 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 9116 | 97.4% |
| Unknown | 36 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 206 | 2.2% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2088*

**Composition by Extension & Reason:**
- `.java`: 747x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kt`: 390x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adoc`: 213x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.imports`: 177x Unsupported Format (.imports)
- `.factories`: 88x Unsupported Format (.factories)
- `.json`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 4615 LOC), 2x Excluded (Embedded Array/Matrix Payload: 2025 commas in 599 LOC)
- `.xml`: 62x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 55x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 40x Unsupported Format (.undeterminable), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.configurator)
- `.crt`: 46x Unsupported Format (.crt)
- `.jar`: 13x Excluded (Explicitly Denied Extension: '.jar')
- `.tar`: 10x Excluded (Explicitly Denied Extension: '.tar')
- `.pem`: 9x Unsupported Format (.pem)
- `.pom`: 8x Unsupported Format (.pom)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.6 | 30.5 | 44.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.3 | 8.4 | 1.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 11.3 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 51.8 | 66.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1767 | 805 | 0 | `module/spring-boot-jetty/src/test/java/org/springframework/boot/jetty/servlet/JettyServletWebServerFactoryTests.java` |
| cleanup | 553 | 316 | 0 | `core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleApplicationContextInitializerTests.java` |
| guards | 37786 | 4920 | 11 | `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` |
| danger | 19350 | 3305 | 6 | `core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackLoggingSystemTests.java` |
| concurrency | 4585 | 1203 | 2 | `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` |
| connectivity | 26912 | 5009 | 7 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| io | 7384 | 1049 | 2 | `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 192 | 39 | 0 | `module/spring-boot-amqp/src/test/java/org/springframework/boot/amqp/autoconfigure/RabbitAutoConfigurationTests.java` |
| time | 2763 | 545 | 0 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| serialization | 387 | 92 | 0 | `module/spring-boot-jackson2/src/test/java/org/springframework/boot/jackson2/autoconfigure/Jackson2AutoConfigurationTests.java` |
| regex | 354 | 123 | 0 | `module/spring-boot-security/src/test/java/org/springframework/boot/security/autoconfigure/actuate/web/reactive/EndpointRequestTests.java` |
| events | 1714 | 470 | 0 | `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` |
| tests | 52504 | 2693 | 15 | `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` |
| docs | 15907 | 6869 | 3 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| debt | 1354 | 436 | 0 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| mutation | 69453 | 5660 | 19 | `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` |
| dead_code | 25535 | 4661 | 7 | `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` |
| credential | 155 | 27 | 0 | `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/ssl/PemFileWriter.java` |
| threat | 5 | 2 | 0 | `loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/ZipStringTests.java` |
| ml_ai | 134 | 61 | 0 | `module/spring-boot-jackson/src/test/java/org/springframework/boot/jackson/ObjectValueDeserializerTests.java` |
| ui | 187 | 45 | 0 | `core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SpringBootJoranConfigurator.java` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.3333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java` (Hits: 96)
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/JarIntegrationTests.java` (Hits: 84)
- `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/AbstractBootArchiveIntegrationTests.java` (Hits: 66)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AutoConfigurations.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java`) — 411 inbound connections
2. **ConditionalOnClass.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnClass.java`) — 376 inbound connections
3. **ApplicationContextRunner.java** (`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/runner/ApplicationContextRunner.java`) — 367 inbound connections
4. **AutoConfiguration.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfiguration.java`) — 359 inbound connections
5. **ConditionalOnMissingBean.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBean.java`) — 356 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AbstractServletWebServerFactoryTests.java** (`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java`) — 151 outbound dependencies
2. **WebMvcAutoConfigurationTests.java** (`module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfigurationTests.java`) — 146 outbound dependencies
3. **SpringApplicationTests.java** (`core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java`) — 124 outbound dependencies
4. **WebFluxAutoConfigurationTests.java** (`module/spring-boot-webflux/src/test/java/org/springframework/boot/webflux/autoconfigure/WebFluxAutoConfigurationTests.java`) — 121 outbound dependencies
5. **WebMvcAutoConfiguration.java** (`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfiguration.java`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `loadWhenBindingClasspathPatternToResourceArrayShouldBindMultipleValues` **(C Struct Operations)** (@ `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java`) -> Impact: **106.7** | LOC: 2074
- `SslBundleSource` **(Stateful Encapsulated Methods)** (@ `core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/SslBundleSource.java`) -> Impact: **44.4** | LOC: 104
  * *Intent:* /** * {@link SslBundle} source created from annotations. Used as a cache key and as a * {@link SslBundle} factory. * * @param ssl the {@link Ssl @Ssl}...
- `MemberPath` **(Stateful Encapsulated Methods)** (@ `core/spring-boot/src/main/java/org/springframework/boot/json/JsonWriter.java`) -> Impact: **37.1** | LOC: 102
  * *Intent:* /** * A path used to identify a specific JSON member. Paths can be represented as strings * in form {@code "my.json[1].item"} where elements are separ...
- `compare` **(Many-Argument Workhorses)** (@ `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/ZipString.java`) -> Impact: **36.9** | LOC: 50
- `LiveReload` **(Defensive Guards)** (@ `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js`) -> Impact: **36.0** | LOC: 69
- `ZipCentralDirectoryFileHeaderRecord` **(Many-Argument Workhorses)** (@ `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/ZipCentralDirectoryFileHeaderRecord.java`) -> Impact: **32.6** | LOC: 158
  * *Intent:* * @param lastModFileDate the last modified file date * @param crc32 the CRC32 checksum * @param compressedSize the size of the entry when compressed *...
- `dashIgnoringElementEquals` **(Stateful Encapsulated Methods)** (@ `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyName.java`) -> Impact: **29.9** | LOC: 39
- `ServiceConfig` **(Many-Argument Workhorses)** (@ `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`) -> Impact: **29.7** | LOC: 371
  * *Intent:* * protocol definition. For advanced or experimental service configurations, use the * {@link GrpcClientDefaultServiceConfigCustomizer} to directly add...
- `process` **(Defensive Guards)** (@ `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js`) -> Impact: **29.1** | LOC: 44
- `customize` **(Compute Cores)** (@ `build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/Image.java`) -> Impact: **28.6** | LOC: 62

*Function archetypes referenced above:*
  * **C Struct Operations**: operates on C structs and pointers (data-structure logic)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose` | 6 | 20030.92 | 0.0% | 0.0% |
| `smoke-test/spring-boot-smoke-test-data-cassandra/src/dockerTest/resources/ssl` | 4 | 15017.46 | 0.0% | 2.74% |
| `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl` | 3 | 15000.0 | 0.0% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive` | 3 | 15000.0 | 0.0% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/servlet` | 3 | 15000.0 | 0.0% | 0.0% |
| `smoke-test/spring-boot-smoke-test-kafka/src/dockerTest/resources/ssl` | 3 | 15000.0 | 0.0% | 0.0% |
| `module/spring-boot-elasticsearch/src/dockerTest/resources/org/springframework/boot/elasticsearch/docker/compose` | 4 | 10030.9 | 1.41% | 0.0% |
| `module/spring-boot-mongodb/src/dockerTest/resources/org/springframework/boot/mongodb/docker/compose` | 4 | 10030.24 | 0.0% | 0.0% |
| `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose` | 4 | 10028.02 | 0.0% | 0.0% |
| `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp` | 2 | 10000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `configuration-metadata/spring-boot-configuration-metadata/src/main/java/org/springframework/boot/configurationmetadata/ConfigurationMetadataSource.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/context/MessageSourceProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/info/ProjectInfoProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/JksSslBundleProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/PemSslBundleProperties.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` -> **100.0%** Exposure
- `gradlew` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/env/ConfigTreePropertySource.java` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/env/DefaultPropertiesPropertySource.java` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/env/OriginTrackedPropertiesLoader.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` -> **197** Orphaned Functions | **0** Duplicates
- `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` -> **115** Orphaned Functions | **53** Duplicates
- `module/spring-boot-pulsar/src/main/java/org/springframework/boot/pulsar/autoconfigure/PulsarProperties.java` -> **111** Orphaned Functions | **29** Duplicates
- `module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitProperties.java` -> **106** Orphaned Functions | **28** Duplicates
- `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` -> **119** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/ssl/PemFileWriter.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/SslPropertiesBundleRegistrarTests.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/BundleContentPropertyTests.java` -> **99.9998%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemContentTests.java` -> **99.9998%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemSslStoreBundleTests.java` -> **99.9994%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70977` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `build-plugin/spring-boot-maven-plugin/src/dockerTest/projects/build-image-bindings/bindings/ca-certificates/test.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/alt/test-hello-alt-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/default/test-hello-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/alt/test-hello-alt-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/default/test-hello-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/client-keystore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/client-truststore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/server-keystore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/server-truststore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-elasticsearch/src/dockerTest/resources/org/springframework/boot/elasticsearch/docker/compose/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-elasticsearch/src/dockerTest/resources/org/springframework/boot/elasticsearch/docker/compose/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl/test-ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl/test-client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl/test-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-mongodb/src/dockerTest/resources/org/springframework/boot/mongodb/docker/compose/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-mongodb/src/dockerTest/resources/org/springframework/boot/mongodb/docker/compose/mongo.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive/test-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive/test.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive/test.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/servlet/test-key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/servlet/test.jks` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/condition/scan/ScanFactoryBean.java` (JAVA) | Magnitude: 8.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 15, structural_boundaries: 10, args: 4, func_start: 4
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/EnableConfigurationProperties.java` (JAVA) | Magnitude: 16.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 10, import: 7, decorators: 4, doc: 3
- `core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/ExcludeFilterApplicationContextInitializer.java` (JAVA) | Magnitude: 2.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 5, import: 3, args: 1
- `core/spring-boot/src/test/java/org/springframework/boot/logging/CorrelationIdFormatterTests.java` (JAVA) | Magnitude: 28.6 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 77, structural_boundaries: 27, test: 23, args: 20
- `module/spring-boot-rsocket/src/main/java/org/springframework/boot/rsocket/autoconfigure/RSocketMessagingAutoConfiguration.java` (JAVA) | Magnitude: 27.74 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 52, structural_boundaries: 37, import: 15, decorators: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `core/spring-boot/src/test/java/org/springframework/boot/convert/LenientBooleanToEnumConverterFactoryTests.java` (JAVA) | Magnitude: 3.88 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 16, test: 4, import: 4
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/JarIntegrationTests.java` (JAVA) | Magnitude: 88.88 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 445, structural_boundaries: 114, test: 105, io: 84
- `module/spring-boot-micrometer-tracing-brave/src/test/java/org/springframework/boot/micrometer/tracing/brave/autoconfigure/PrometheusExemplarsAutoConfigurationTests.java` (JAVA) | Magnitude: 25.52 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 116, structural_boundaries: 73, args: 29, import: 27
- `starter/spring-boot-starter-test-classic/build.gradle` (GROOVY) | Magnitude: 16.22 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 4, dependency_injection: 2, args: 1, state_mutation: 1
- `build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-compileClasspathDoesNotIncludeDevelopmentOnlyDependencies.gradle` (GROOVY) | Magnitude: 16.32 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 6, closures: 2, dependency_injection: 2, state_mutation: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/DevToolsProperties.java` (JAVA) | Magnitude: 79.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 44, api: 27, args: 24
- `configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationsample/simple/AutowiredProperties.java` (JAVA) | Magnitude: 10.6 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 5, api: 4, args: 3
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/DataBlock.java` (JAVA) | Magnitude: 21.66 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 15, indent_tabs: 15, branch: 5, doc: 5
- `module/spring-boot-micrometer-tracing-opentelemetry/src/test/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/otlp/OtlpTracingAutoConfigurationIntegrationTests.java` (JAVA) | Magnitude: 34.6 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 131, structural_boundaries: 90, import: 36, test: 25
- `smoke-test/spring-boot-smoke-test-integration/src/main/java/smoketest/integration/ServiceProperties.java` (JAVA) | Magnitude: 18.84 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 13, io: 7, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/reactive/AbstractClientHttpConnectorBuilderTests.java` (JAVA) | Magnitude: 70.74 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 158, structural_boundaries: 83, import: 36, core_var_decl: 35
- `module/spring-boot-jetty/src/test/java/org/springframework/boot/jetty/autoconfigure/AutoConfigureWebServerJettyServletTests.java` (JAVA) | Magnitude: 7.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_tabs: 20, import: 17, decorators: 7
- `module/spring-boot-tomcat/src/test/java/org/springframework/boot/tomcat/autoconfigure/AutoConfigureWebServerTomcatServletTests.java` (JAVA) | Magnitude: 7.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, indent_tabs: 20, import: 17, decorators: 7
- `module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SkipSslVerificationHttpRequestFactoryTests.java` (JAVA) | Magnitude: 14.48 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 35, structural_boundaries: 33, import: 16, core_var_decl: 7
- `module/spring-boot-data-couchbase-test/src/dockerTest/java/org/springframework/boot/data/couchbase/test/autoconfigure/ExampleDocument.java` (JAVA) | Magnitude: 12.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 11, api: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/error/ErrorAttributes.java` (JAVA) | Magnitude: 6.6 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 11, import: 7, indent_tabs: 5, doc: 4
- `smoke-test/spring-boot-smoke-test-web-secure-custom/src/main/java/smoketest/web/secure/custom/SampleWebSecureCustomApplication.java` (JAVA) | Magnitude: 12.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 21, structural_boundaries: 19, import: 10, args: 6
- `smoke-test/spring-boot-smoke-test-tomcat-multi-connectors/src/test/java/smoketest/tomcat/multiconnector/SampleTomcatTwoConnectorsApplicationTests.java` (JAVA) | Magnitude: 19.92 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 50, structural_boundaries: 32, import: 20, test: 11
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/AotTests.java` (JAVA) | Magnitude: 42.8 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 175, structural_boundaries: 59, io: 50, test: 43
- `module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/RemoteUrlPropertyExtractorTests.java` (JAVA) | Magnitude: 12.14 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 24, args: 12, test: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `core/spring-boot/src/main/java/org/springframework/boot/convert/PeriodToStringConverter.java` (JAVA) | Magnitude: 21.4 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 23, import: 9, safety_bypasses: 7
- `test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/ssl/MockPkcs11SecurityProvider.java` (JAVA) | Magnitude: 3.4 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 6, safety_bypasses: 2, api: 2
- `core/spring-boot/src/main/java/org/springframework/boot/ssl/jks/JksSslStoreBundle.java` (JAVA) | Magnitude: 47.94 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 84, structural_boundaries: 33, safety_bypasses: 21, args: 15
- `module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/servlet/view/MustacheView.java` (JAVA) | Magnitude: 30.04 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 35, import: 16, safety_bypasses: 13
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemSslStoreTests.java` (JAVA) | Magnitude: 7.96 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 21, test: 14, safety_bypasses: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `smoke-test/spring-boot-smoke-test-tomcat/src/main/java/smoketest/tomcat/util/RandomStringUtil.java` (JAVA) | Magnitude: 5.04 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 7, args: 2, func_start: 2
- `core/spring-boot/src/test/java/org/springframework/boot/system/MockApplicationPid.java` (JAVA) | Magnitude: 4.86 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 5, structural_boundaries: 4, args: 2, func_start: 2
- `test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/classpath/resources/Resources.java` (JAVA) | Magnitude: 65.44 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 123, structural_boundaries: 44, io: 25, import: 21
- `build-plugin/spring-boot-gradle-plugin/src/test/resources/com/example/bootrun/jvmargs/BootRunJvmArgsApplication.java` (JAVA) | Magnitude: 10.44 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 4, api: 3, args: 2
- `build-plugin/spring-boot-gradle-plugin/src/test/resources/com/example/boottestrun/jvmargs/BootTestRunJvmArgsApplication.java` (JAVA) | Magnitude: 10.44 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 4, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/audit/listener/AuditListener.java` (JAVA) | Magnitude: 12.18 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 12, structural_boundaries: 9, import: 4, api: 3
- `smoke-test/spring-boot-smoke-test-jetty/src/main/java/smoketest/jetty/util/StringUtil.java` (JAVA) | Magnitude: 5.32 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, args: 2, func_start: 2
- `core/spring-boot-testcontainers/src/testFixtures/java/org/springframework/boot/testcontainers/service/connection/ContainerConnectionDetailsFactoryHints.java` (JAVA) | Magnitude: 5.04 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 7, args: 2, func_start: 2
- `cli/spring-boot-cli/src/intTest/java/org/springframework/boot/cli/infrastructure/CommandLineInvoker.java` (JAVA) | Magnitude: 95.76 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 129, structural_boundaries: 69, io: 28, import: 21
- `build-plugin/spring-boot-gradle-plugin/src/test/resources/com/example/bootjar/main/CustomMainClass.java` (JAVA) | Magnitude: 5.86 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 5, structural_boundaries: 4, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/shell/ShellExitException.java` (JAVA) | Magnitude: 3.26 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 4, api: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `build-plugin/spring-boot-gradle-plugin/build.gradle` (GROOVY) | Magnitude: 31.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 107, state_mutation: 24, core_var_decl: 19, design_camel_case: 11
- `smoke-test/spring-boot-smoke-test-grpc-server-servlet/build.gradle` (GROOVY) | Magnitude: 20.88 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 28, core_var_decl: 7, state_mutation: 5, dependency_injection: 4
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/ref/Cleaner.java` (JAVA) | Magnitude: 4.92 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, api: 2, indent_tabs: 2
- `module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/reactive/AbstractReactiveWebServerFactory.java` (JAVA) | Magnitude: 5.9 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 5, api: 3, args: 2
- `smoke-test/spring-boot-smoke-test-web-method-security/src/main/webapp/templates/home.html` (HTML) | Magnitude: 15.22 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_tabs: 3, doc: 1, ui_framework: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/metadata/OracleUcpDataSourcePoolMetadata.java` (JAVA) | Magnitude: 19.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 38, structural_boundaries: 16, api: 8, args: 7
- `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/ApplicationPluginActionIntegrationTests.java` (JAVA) | Magnitude: 46.98 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 152, structural_boundaries: 67, test: 44, core_var_decl: 34
- `module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/servlet/ServletWebServerConfiguration.java` (JAVA) | Magnitude: 31.2 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 47, indent_tabs: 47, import: 27, decorators: 9
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/NestedJarFile.java` (JAVA) | Magnitude: 366.98 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 585, structural_boundaries: 175, args: 91, func_start: 78
- `loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/AssertFileChannelDataBlocksClosedExtension.java` (JAVA) | Magnitude: 34.02 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 44, structural_boundaries: 33, import: 14, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `module/spring-boot-jpa-test/src/test/java/org/springframework/boot/jpa/test/autoconfigure/TestEntityManagerTests.java` (JAVA) | Magnitude: 38.9 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 161, structural_boundaries: 64, test: 50, decorators: 27
- `core/spring-boot/src/main/java/org/springframework/boot/system/ApplicationPid.java` (JAVA) | Magnitude: 41.68 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 76, structural_boundaries: 32, args: 12, func_start: 12
- `module/spring-boot-jpa/src/test/java/org/springframework/boot/jpa/EntityManagerFactoryBuilderTests.java` (JAVA) | Magnitude: 21.92 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 87, structural_boundaries: 38, core_var_decl: 22, args: 20
- `core/spring-boot/src/main/java/org/springframework/boot/system/SystemProperties.java` (JAVA) | Magnitude: 12.92 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 5, safety_bypasses: 4, branch: 3
- `core/spring-boot/src/test/java/org/springframework/boot/logging/log4j2/Log4j2LoggingSystemPropertiesTests.java` (JAVA) | Magnitude: 25.68 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 49, structural_boundaries: 24, state_mutation: 12, import: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 787.96
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnBeanCondition.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 401.12
- `integration-test/spring-boot-actuator-integration-tests/src/test/java/org/springframework/boot/actuate/endpoint/web/annotation/AbstractWebEndpointIntegrationTests.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 337.78
- `module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfigurationTests.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 337.22
- `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/TomcatServerProperties.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 323.22

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` -> **Severity: 0.196** (Bridge: 0.0021 * Flux: 94.8167%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java` -> **Severity: 0.129** (Bridge: 0.0017 * Flux: 73.9017%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesBean.java` -> **Severity: 0.058** (Bridge: 0.0007 * Flux: 77.6161%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesBinder.java` -> **Severity: 0.038** (Bridge: 0.0004 * Flux: 84.0181%)
- `configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/PropertyDescriptorResolver.java` -> **Severity: 0.033** (Bridge: 0.0009 * Flux: 36.0907%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertySources.java` -> **Severity: 4.993** (Embedded: 0.0624 * Error Risk: 80.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Bindable.java` -> **Severity: 4.547** (Embedded: 0.0568 * Error Risk: 80.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java` -> **Severity: 4.529** (Embedded: 0.0566 * Error Risk: 80.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/origin/Origin.java` -> **Severity: 4.371** (Embedded: 0.0546 * Error Risk: 80.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationProperty.java` -> **Severity: 4.338** (Embedded: 0.0542 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/spring-boot/src/test/java/org/springframework/boot/context/annotation/ConfigurationsTests.java` -> **Severity: 546.821** (Blast Radius: 5.772 * Doc Risk: 94.7368%)
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -> **Severity: 410.5** (Blast Radius: 4.105 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/ssl/DefaultSslManagerBundle.java` -> **Severity: 329.0** (Blast Radius: 3.29 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/TypeExcludeFilter.java` -> **Severity: 326.3** (Blast Radius: 3.263 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/annotation/ImportCandidates.java` -> **Severity: 325.0** (Blast Radius: 5.2 * Doc Risk: 62.5%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 355 literal sites + 8 sites through wrappers = 363
- **`panics_and_aborts`:** 1518 literal sites + 104 sites through wrappers = 1622

- `resolve` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `core/spring-boot/src/main/java/org/springframework/boot/logging/logback/DefaultLogbackConfiguration.java`
- `pushAndPrint` (function, debug_prints, primitive): 7 call sites in 1 files -- `core/spring-boot-test/src/test/java/org/springframework/boot/test/system/OutputCaptureTests.java`
- `withJarFile` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/AbstractArchiveIntegrationTests.java`
- `projectPath` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests.java`
- `createObjectName` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `core/spring-boot/src/test/java/org/springframework/boot/admin/SpringApplicationAdminMXBeanRegistrarTests.java`
- `fail` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/JarEntriesStream.java`
- `getJarPathFileStore` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/nio/file/NestedFileStore.java`
- `createInstance` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `cli/spring-boot-cli/src/test/java/org/springframework/boot/cli/command/init/InitializrServiceMetadataTests.java`
- `hasGatewayUrl` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `module/spring-boot-micrometer-metrics/src/test/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/prometheus/PrometheusMetricsExportAutoConfigurationTests.java`
- `is` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/bind/JavaBeanBinderTests.java`
- `RefreshFailure` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `module/spring-boot-web-server/src/test/java/org/springframework/boot/web/server/reactive/context/ReactiveWebServerApplicationContextTests.java`
- `RefreshFailure` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `module/spring-boot-web-server/src/test/java/org/springframework/boot/web/server/servlet/context/ServletWebServerApplicationContextTests.java`
*(+48 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 195723 call pairs -- scoped 27.4%, unique 1.8%, ambiguous 35.6%, external 35.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 194084 | 27.6% | 1.8% | 35.8% | 34.8% |
| groovy | 705 | 7.5% | 0.0% | 7.2% | 85.2% |
| kotlin | 462 | 16.7% | 5.2% | 42.6% | 35.5% |
| javascript | 179 | 4.5% | 0.0% | 0.0% | 95.5% |
| html | 134 | 22.4% | 0.0% | 0.0% | 77.6% |
| ruby | 104 | 5.8% | 0.0% | 0.0% | 94.2% |
| shell | 55 | 10.9% | 0.0% | 0.0% | 89.1% |

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
