# ARCHITECTURAL_BRIEF: spring-boot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/spring-boot` |
| **Timestamp** | `2026-08-03T21:37:35.825869+00:00` |
| **Scan Duration** | `22.62s` |
| **Git Branch** | `main` |
| **Git Commit** | `5cecd3922fce651f13d16a85d8a29efaa7f44cfd` |
| **Git Remote** | `https://github.com/spring-projects/spring-boot` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8009 malicious artifacts.

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
| Total Artifacts | 11421 |
| Analyzed Artifacts (Scanned) | 8862 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2559 |
| Total LOC | 482768 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.6% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0797 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 423 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 7713 | 460052 | 87.0% |
| PLAINTEXT | 262 | 66 | 3.0% |
| XML | 252 | 0 | 2.8% |
| GROOVY | 235 | 3881 | 2.7% |
| JSON | 195 | 13166 | 2.2% |
| YAML | 85 | 1225 | 1.0% |
| HTML | 49 | 1288 | 0.6% |
| SQLITE | 23 | 331 | 0.3% |
| KOTLIN | 18 | 1133 | 0.2% |
| PROTO | 8 | 107 | 0.1% |
| MARKDOWN | 7 | 0 | 0.1% |
| SHELL | 4 | 156 | 0.0% |
| BATCH | 3 | 162 | 0.0% |
| RUBY | 3 | 210 | 0.0% |
| CSS | 3 | 9 | 0.0% |
| DOCKERFILE | 1 | 9 | 0.0% |
| JAVASCRIPT | 1 | 973 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.104`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 5595 | 63.1% |
| file_cluster_8 | 2581 | 29.1% |
| file_cluster_0 | 253 | 2.9% |
| file_cluster_16 | 99 | 1.1% |
| Unknown | 63 | 0.7% |
| file_cluster_4 | 52 | 0.6% |
| file_cluster_9 | 6 | 0.1% |
| file_cluster_15 | 3 | 0.0% |
| file_cluster_1 | 2 | 0.0% |
| file_cluster_12 | 1 | 0.0% |
| file_cluster_11 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 203 | 2.3% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2559*

**Composition by Extension & Reason:**
- `.java`: 785x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 94 exceeds 500 chars)
- `.gradle`: 510x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kt`: 390x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adoc`: 213x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.imports`: 177x Unsupported Format (.imports)
- `.factories`: 88x Unsupported Format (.factories)
- `.json`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Massive Static Asset Blob: 4615 LOC), 2x Excluded (Embedded Array/Matrix Payload: 2025 commas in 599 LOC)
- `.xml`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.kts`: 53x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 42x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.configurator)
- `.yml`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 13x Excluded (Explicitly Denied Extension: '.jar')
- `.tar`: 10x Excluded (Explicitly Denied Extension: '.tar')
- `.pom`: 8x Unsupported Format (.pom)
- `.properties`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 8.7 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 27.6 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.6 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.3 | 2.8 | 1.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 13.6 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 80.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.0 | 1.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 76.0 | 3.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 16.6 | 2.4 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `smoke-test/spring-boot-smoke-test-data-jpa/src/main/resources/import.sql` (Hits: 111)
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java` (Hits: 96)
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/JarIntegrationTests.java` (Hits: 84)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **AutoConfigurations.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java`) — 408 inbound connections
2. **ConditionalOnClass.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnClass.java`) — 376 inbound connections
3. **ApplicationContextRunner.java** (`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/runner/ApplicationContextRunner.java`) — 365 inbound connections
4. **AutoConfiguration.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfiguration.java`) — 358 inbound connections
5. **ConditionalOnMissingBean.java** (`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBean.java`) — 355 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AbstractServletWebServerFactoryTests.java** (`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java`) — 151 outbound dependencies
2. **WebMvcAutoConfigurationTests.java** (`module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfigurationTests.java`) — 146 outbound dependencies
3. **SpringApplicationTests.java** (`core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java`) — 124 outbound dependencies
4. **WebFluxAutoConfigurationTests.java** (`module/spring-boot-webflux/src/test/java/org/springframework/boot/webflux/autoconfigure/WebFluxAutoConfigurationTests.java`) — 121 outbound dependencies
5. **WebMvcAutoConfiguration.java** (`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfiguration.java`) — 118 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ServiceConfig` (@ `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`) -> Impact: **680.4** | LOC: 281
- `StructuredLoggingJsonProperties` (@ `core/spring-boot/src/main/java/org/springframework/boot/logging/structured/StructuredLoggingJsonProperties.java`) -> Impact: **226.7** | LOC: 107
- `customize` (@ `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizer.java`) -> Impact: **218.3** | LOC: 73
  * *Intent:* * Customization for Tomcat-specific features common to both Servlet and Reactive servers. * * @author Brian Clozel * @author Yulin Qin * @author Steph...
- `configure` (@ `module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java`) -> Impact: **217.1** | LOC: 48
  * *Intent:* /** * Creates a new configurer that will use the given {@code resourceLoader} and * {@code properties}.
- `apply` (@ `core/spring-boot/src/main/java/org/springframework/boot/context/properties/PropertyMapper.java`) -> Impact: **206.6** | LOC: 196
- `configureContainer` (@ `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/ConcurrentKafkaListenerContainerFactoryConfigurer.java`) -> Impact: **191.6** | LOC: 30
- `addBean` (@ `core/spring-boot/src/main/java/org/springframework/boot/convert/ApplicationConversionService.java`) -> Impact: **157.6** | LOC: 31
  * *Intent:* /** * Add converters to support delimited strings. * @param registry the registry of converters to add to (must also be castable to * ConversionServic...
- `jsonMembers` (@ `core/spring-boot/src/main/java/org/springframework/boot/logging/logback/ElasticCommonSchemaStructuredLogFormatter.java`) -> Impact: **153.6** | LOC: 34
- `build` (@ `module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JdkHttpClientBuilder.java`) -> Impact: **152.5** | LOC: 13
- `jsonMembers` (@ `core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ElasticCommonSchemaStructuredLogFormatter.java`) -> Impact: **149.0** | LOC: 29

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `collectImportedStylesheets` (@ `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js`) -> **O(2^N) [Recursive]**
- `reloadStylesheetImages` (@ `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js`) -> **O(2^N) [Recursive]**
- `reload` (@ `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js`) -> **O(2^N) [Recursive]**
- `execute` (@ `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/MavenBuild.java`) -> **O(2^N) [Recursive]**
- `assertThat` (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> **O(2^N) [Recursive]**
- `addToClasses` (@ `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationSorter.java`) -> **O(2^N) [Recursive]**
- `run` (@ `core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationAotProcessor.java`) -> **O(2^N) [Recursive]**
- `serializationTypes` (@ `core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SpringBootJoranConfigurator.java`) -> **O(2^N) [Recursive]**
- `serializeAsField` (@ `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/Jackson2BeanSerializer.java`) -> **O(2^N) [Recursive]**
- `serializeAsProperty` (@ `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/JacksonBeanSerializer.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `INSERT_Statement_[Unterminated]` (@ `smoke-test/spring-boot-smoke-test-data-jpa/src/main/resources/import.sql`) -> DB Complexity: **333**
  * *Intent:* -- -- Sample dataset containing a number of Hotels in various Cities across the world. The reviews are entirely fictional :) -- -- ===================...
- `pluginClasspath` (@ `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/testkit/PluginClasspathGradleBuild.java`) -> DB Complexity: **194**
- `INSERT_Statement_[Unterminated]` (@ `smoke-test/spring-boot-smoke-test-data-rest/src/main/resources/import.sql`) -> DB Complexity: **138**
  * *Intent:* -- -- Sample dataset containing a number of Hotels in various Cities across the world. -- -- =========================================================...
- `execute` (@ `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/MavenBuild.java`) -> DB Complexity: **68**
- `generateProject` (@ `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ProjectGenerator.java`) -> DB Complexity: **48**
- `INSERT_Statement_[Unterminated]` (@ `smoke-test/spring-boot-smoke-test-hibernate/src/main/resources/import.sql`) -> DB Complexity: **45**
- `addContent` (@ `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/AbstractBootArchiveTests.java`) -> DB Complexity: **42**
- `shouldFollowRelativePathSymlinks` (@ `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java`) -> DB Complexity: **39**
- `writeBuildpackContent` (@ `build-plugin/spring-boot-gradle-plugin/src/dockerTest/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests.java`) -> DB Complexity: **36**
- `additionalMetadataIsLocatedInGradle3Buil` (@ `configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/MetadataStoreTests.java`) -> DB Complexity: **33**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl` | 6 | 30000.0 | 0.0% | 0.0% |
| `module/spring-boot-elasticsearch/src/dockerTest/resources/org/springframework/boot/elasticsearch/docker/compose` | 7 | 25030.9 | 2.15% | 0.0% |
| `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose` | 7 | 25028.02 | 2.51% | 0.0% |
| `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp` | 5 | 25000.0 | 0.0% | 0.0% |
| `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose` | 6 | 20030.92 | 2.34% | 0.0% |
| `module/spring-boot-mongodb/src/dockerTest/resources/org/springframework/boot/mongodb/docker/compose` | 6 | 20030.24 | 2.53% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive` | 4 | 20000.0 | 0.0% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/servlet` | 4 | 20000.0 | 0.0% | 0.0% |
| `smoke-test/spring-boot-smoke-test-data-cassandra/src/dockerTest/resources/ssl` | 4 | 15017.46 | 0.0% | 6.35% |
| `smoke-test/spring-boot-smoke-test-kafka/src/dockerTest/resources/ssl` | 3 | 15000.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `build-plugin/spring-boot-maven-plugin/src/intTest/projects/run-toolchains/jdkHome/bin/java` -> **100.0%** Exposure
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` -> **100.0%** Exposure
- `build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/DefaultTimeZoneOffset.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/LayeredSpec.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-maven-plugin/src/intTest/projects/jar-custom-layout/layout/src/main/java/smoketest/layout/SampleLayoutFactory.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/scripts/reclaim-docker-diskspace.sh` -> **100.0%** Exposure
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` -> **100.0%** Exposure
- `cli/spring-boot-cli/src/test/java/org/springframework/boot/cli/util/MockLog.java` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ElasticCommonSchemaStructuredLogFormatter.java` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/LogstashStructuredLogFormatter.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java` -> **113** Orphaned Functions | **102** Duplicates
- `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` -> **136** Orphaned Functions | **61** Duplicates
- `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` -> **108** Orphaned Functions | **41** Duplicates
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/bind/JavaBeanBinderTests.java` -> **63** Orphaned Functions | **59** Duplicates
- `module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfigurationTests.java` -> **106** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`core/spring-boot/src/test/java/org/springframework/boot/cloud/CloudFoundryVcapEnvironmentPostProcessorTests.java`** -> AI Confidence: **99.48%**
2. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java`** -> AI Confidence: **99.48%**
3. **`module/spring-boot-pulsar/src/main/java/org/springframework/boot/pulsar/autoconfigure/PulsarPropertiesMapper.java`** -> AI Confidence: **99.48%**
4. **`module/spring-boot-security-oauth2-authorization-server/src/main/java/org/springframework/boot/security/oauth2/server/authorization/autoconfigure/servlet/OAuth2AuthorizationServerPropertiesMapper.java`** -> AI Confidence: **99.48%**
5. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/servlet/ServletWebServerFactoryCustomizer.java`** -> AI Confidence: **99.48%**
6. **`core/spring-boot/src/test/kotlin/org/springframework/boot/SpringApplicationExtensionsTests.kt`** -> AI Confidence: **99.48%**
7. **`module/spring-boot-kotlinx-serialization-json/src/test/kotlin/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonAutoConfigurationTests.kt`** -> AI Confidence: **99.48%**
8. **`core/spring-boot/src/test/java/org/springframework/boot/logging/StandardStackTracePrinterTests.java`** -> AI Confidence: **99.39%**
9. **`module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/ConcurrentKafkaListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.39%**
10. **`module/spring-boot-ldap/src/test/java/org/springframework/boot/ldap/autoconfigure/embedded/EmbeddedLdapAutoConfigurationTests.java`** -> AI Confidence: **99.39%**
11. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/ReactiveMultipartAutoConfiguration.java`** -> AI Confidence: **99.39%**
12. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/PropertiesGrpcChannelBuilderCustomizer.java`** -> AI Confidence: **99.35%**
13. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`** -> AI Confidence: **99.35%**
14. **`module/spring-boot-security-oauth2-client/src/main/java/org/springframework/boot/security/oauth2/client/autoconfigure/OAuth2ClientPropertiesMapper.java`** -> AI Confidence: **99.35%**
15. **`module/spring-boot-kotlinx-serialization-json/src/test/java/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonPropertiesTests.java`** -> AI Confidence: **99.34%**
16. **`core/spring-boot-test/src/test/kotlin/org/springframework/boot/test/context/SpringBootContextLoaderKotlinTests.kt`** -> AI Confidence: **99.34%**
17. **`core/spring-boot/src/main/kotlin/org/springframework/boot/SpringApplicationExtensions.kt`** -> AI Confidence: **99.34%**
18. **`core/spring-boot/src/test/kotlin/org/springframework/boot/context/properties/bind/KotlinConstructorParametersBinderTests.kt`** -> AI Confidence: **99.34%**
19. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverTests.java`** -> AI Confidence: **99.32%**
20. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/DockerSpecTests.java`** -> AI Confidence: **99.31%**
21. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthentication.java`** -> AI Confidence: **99.31%**
22. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`** -> AI Confidence: **99.31%**
23. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/ResolvedDockerHostTests.java`** -> AI Confidence: **99.31%**
24. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/type/ImageReferenceTests.java`** -> AI Confidence: **99.31%**
25. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/CommandRunner.java`** -> AI Confidence: **99.31%**
26. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/core/HintCommand.java`** -> AI Confidence: **99.31%**
27. **`configuration-metadata/spring-boot-configuration-metadata-changelog-generator/src/main/java/org/springframework/boot/configurationmetadata/changelog/ChangelogWriter.java`** -> AI Confidence: **99.31%**
28. **`configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/metadata/JsonMarshallerTests.java`** -> AI Confidence: **99.31%**
29. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/logging/ConditionEvaluationReportMessage.java`** -> AI Confidence: **99.31%**
30. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/service/connection/ConnectionDetailsFactories.java`** -> AI Confidence: **99.31%**
31. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/assertj/ApplicationContextAssert.java`** -> AI Confidence: **99.31%**
32. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/FileHint.java`** -> AI Confidence: **99.31%**
33. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/BindableRuntimeHintsRegistrar.java`** -> AI Confidence: **99.31%**
34. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/DefaultBindConstructorProvider.java`** -> AI Confidence: **99.31%**
35. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/JavaBeanBinder.java`** -> AI Confidence: **99.31%**
36. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/SpringIterableConfigurationPropertySource.java`** -> AI Confidence: **99.31%**
37. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DurationStyle.java`** -> AI Confidence: **99.31%**
38. **`core/spring-boot/src/main/java/org/springframework/boot/convert/PeriodStyle.java`** -> AI Confidence: **99.31%**
39. **`core/spring-boot/src/main/java/org/springframework/boot/json/JsonValueWriter.java`** -> AI Confidence: **99.31%**
40. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ElasticCommonSchemaStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
41. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/GraylogExtendedLogFormatStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
42. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/LogstashStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
43. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/ElasticCommonSchemaStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
44. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/GraylogExtendedLogFormatStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
45. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogstashStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
46. **`core/spring-boot/src/main/java/org/springframework/boot/retry/RetryPolicySettings.java`** -> AI Confidence: **99.31%**
47. **`core/spring-boot/src/main/java/org/springframework/boot/system/ApplicationHome.java`** -> AI Confidence: **99.31%**
48. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/PropertyMapperTests.java`** -> AI Confidence: **99.31%**
49. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/source/FilteredIterableConfigurationPropertiesSourceTests.java`** -> AI Confidence: **99.31%**
50. **`core/spring-boot/src/test/java/org/springframework/boot/json/JsonWriterTests.java`** -> AI Confidence: **99.31%**
51. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/net/protocol/jar/JarUrlClassLoader.java`** -> AI Confidence: **99.31%**
52. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/ZipString.java`** -> AI Confidence: **99.31%**
53. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/web/CorsEndpointProperties.java`** -> AI Confidence: **99.31%**
54. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/ProducibleOperationArgumentResolver.java`** -> AI Confidence: **99.31%**
55. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/SanitizingFunction.java`** -> AI Confidence: **99.31%**
56. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitTemplateConfigurer.java`** -> AI Confidence: **99.31%**
57. **`module/spring-boot-amqp/src/test/java/org/springframework/boot/amqp/autoconfigure/RabbitPropertiesTests.java`** -> AI Confidence: **99.31%**
58. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/TokenValidatorTests.java`** -> AI Confidence: **99.31%**
59. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/TokenValidatorTests.java`** -> AI Confidence: **99.31%**
60. **`module/spring-boot-graphql/src/main/java/org/springframework/boot/graphql/autoconfigure/GraphQlCorsProperties.java`** -> AI Confidence: **99.31%**
61. **`module/spring-boot-groovy-templates/src/main/java/org/springframework/boot/groovy/template/autoconfigure/GroovyTemplateAutoConfiguration.java`** -> AI Confidence: **99.31%**
62. **`module/spring-boot-grpc-client/src/test/java/org/springframework/boot/grpc/client/autoconfigure/GrpcClientPropertiesTests.java`** -> AI Confidence: **99.31%**
63. **`module/spring-boot-grpc-client/src/test/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfigTests.java`** -> AI Confidence: **99.31%**
64. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/PropertiesServerBuilderCustomizer.java`** -> AI Confidence: **99.31%**
65. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/health/SimpleStatusAggregator.java`** -> AI Confidence: **99.31%**
66. **`module/spring-boot-gson/src/main/java/org/springframework/boot/gson/autoconfigure/GsonAutoConfiguration.java`** -> AI Confidence: **99.31%**
67. **`module/spring-boot-hazelcast/src/test/java/org/springframework/boot/hazelcast/autoconfigure/HazelcastAutoConfigurationTests.java`** -> AI Confidence: **99.31%**
68. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/SimpleHttpCodeStatusMapper.java`** -> AI Confidence: **99.31%**
69. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/SimpleStatusAggregator.java`** -> AI Confidence: **99.31%**
70. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JdkHttpClientBuilder.java`** -> AI Confidence: **99.31%**
71. **`module/spring-boot-http-converter/src/main/java/org/springframework/boot/http/converter/autoconfigure/HttpMessageConverters.java`** -> AI Confidence: **99.31%**
72. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/autoconfigure/SpringBeanHandlerInstantiator.java`** -> AI Confidence: **99.31%**
73. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/DataSourceBuilder.java`** -> AI Confidence: **99.31%**
74. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/EmbeddedDatabaseConnection.java`** -> AI Confidence: **99.31%**
75. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/JettyWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
76. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/AbstractJmsListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.31%**
77. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/DefaultJmsListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.31%**
78. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/JmsClientConfigurations.java`** -> AI Confidence: **99.31%**
79. **`module/spring-boot-jpa/src/main/java/org/springframework/boot/jpa/EntityManagerFactoryBuilder.java`** -> AI Confidence: **99.31%**
80. **`module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/PropertiesKafkaConnectionDetails.java`** -> AI Confidence: **99.31%**
81. **`module/spring-boot-kotlinx-serialization-json/src/main/java/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonAutoConfiguration.java`** -> AI Confidence: **99.31%**
82. **`module/spring-boot-mail/src/dockerTest/java/org/springframework/boot/mail/autoconfigure/MailSenderAutoConfigurationIntegrationTests.java`** -> AI Confidence: **99.31%**
83. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/otlp/OtlpMetricsPropertiesConfigAdapter.java`** -> AI Confidence: **99.31%**
84. **`module/spring-boot-micrometer-metrics/src/testFixtures/java/org/springframework/boot/actuate/autoconfigure/metrics/export/properties/AbstractPropertiesConfigAdapterTests.java`** -> AI Confidence: **99.31%**
85. **`module/spring-boot-micrometer-observation/src/main/java/org/springframework/boot/micrometer/observation/autoconfigure/ObservationHandlerGroups.java`** -> AI Confidence: **99.31%**
86. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/autoconfigure/MustacheReactiveWebConfiguration.java`** -> AI Confidence: **99.31%**
87. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/ConnectionFactoryBuilder.java`** -> AI Confidence: **99.31%**
88. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/metrics/ConnectionPoolMetrics.java`** -> AI Confidence: **99.31%**
89. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/autoconfigure/service/PropertiesRestClientHttpServiceGroupConfigurer.java`** -> AI Confidence: **99.31%**
90. **`module/spring-boot-restdocs/src/main/java/org/springframework/boot/restdocs/test/autoconfigure/RestDocsMockMvcBuilderCustomizer.java`** -> AI Confidence: **99.31%**
91. **`module/spring-boot-security-saml2/src/main/java/org/springframework/boot/security/saml2/autoconfigure/Saml2RelyingPartyRegistrationConfiguration.java`** -> AI Confidence: **99.31%**
92. **`module/spring-boot-session-data-redis/src/main/java/org/springframework/boot/session/data/redis/autoconfigure/SessionDataRedisAutoConfiguration.java`** -> AI Confidence: **99.31%**
93. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/autoconfigure/SessionAutoConfiguration.java`** -> AI Confidence: **99.31%**
94. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/TomcatEmbeddedWebappClassLoader.java`** -> AI Confidence: **99.31%**
95. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
96. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/reactive/ReactiveWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
97. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/DocumentRoot.java`** -> AI Confidence: **99.31%**
98. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/ServletContextInitializers.java`** -> AI Confidence: **99.31%**
99. **`module/spring-boot-webclient/src/main/java/org/springframework/boot/webclient/autoconfigure/service/PropertiesWebClientHttpServiceGroupConfigurer.java`** -> AI Confidence: **99.31%**
100. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WebSessionIdResolverAutoConfiguration.java`** -> AI Confidence: **99.31%**
101. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/ManagementErrorEndpoint.java`** -> AI Confidence: **99.31%**
102. **`smoke-test/spring-boot-smoke-test-traditional/src/main/webapp/WEB-INF/views/home.jsp`** -> AI Confidence: **99.29%**
103. **`smoke-test/spring-boot-smoke-test-web-jsp/src/main/webapp/WEB-INF/jsp/error.jsp`** -> AI Confidence: **99.29%**
104. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageOnLinuxArmWithImagePlatformLinuxArm.gradle`** -> AI Confidence: **99.29%**
105. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithApplicationDirectory.gradle`** -> AI Confidence: **99.29%**
106. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBindCaches.gradle`** -> AI Confidence: **99.29%**
107. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBinding.gradle`** -> AI Confidence: **99.29%**
108. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBuildpackFromBuilder.gradle`** -> AI Confidence: **99.29%**
109. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBuildpackFromDirectory.gradle`** -> AI Confidence: **99.29%**
110. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBuildpackFromTarGzip.gradle`** -> AI Confidence: **99.29%**
111. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithBuildpacksFromImages.gradle`** -> AI Confidence: **99.29%**
112. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithCreatedDate.gradle`** -> AI Confidence: **99.29%**
113. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithCurrentCreatedDate.gradle`** -> AI Confidence: **99.29%**
114. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithCustomBuilderAndRunImage.gradle`** -> AI Confidence: **99.29%**
115. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithCustomName.gradle`** -> AI Confidence: **99.29%**
116. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithEmptySecurityOptions.gradle`** -> AI Confidence: **99.29%**
117. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithNetworkModeNone.gradle`** -> AI Confidence: **99.29%**
118. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithTag.gradle`** -> AI Confidence: **99.29%**
119. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithTrustBuilder.gradle`** -> AI Confidence: **99.29%**
120. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithVolumeCaches.gradle`** -> AI Confidence: **99.29%**
121. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithWarPackagingAndJarConfiguration.gradle`** -> AI Confidence: **99.29%**
122. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWhenBuildingOnLinuxAmdWithImagePlatformLinuxArm.gradle`** -> AI Confidence: **99.29%**
123. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWhenCachesAreConfiguredTwice.gradle`** -> AI Confidence: **99.29%**
124. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWithBuilderError.gradle`** -> AI Confidence: **99.29%**
125. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWithBuildpackNotInBuilder.gradle`** -> AI Confidence: **99.29%**
126. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWithIncompatiblePlatform.gradle`** -> AI Confidence: **99.29%**
127. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWithInvalidCreatedDate.gradle`** -> AI Confidence: **99.29%**
128. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-failsWithInvalidTag.gradle`** -> AI Confidence: **99.29%**
129. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests.gradle`** -> AI Confidence: **99.29%**
130. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageRegistryIntegrationTests.gradle`** -> AI Confidence: **99.29%**
131. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/dsl/BuildInfoDslIntegrationTests-additionalProperties.gradle`** -> AI Confidence: **99.29%**
132. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/CyclonedxPluginActionIntegrationTests-sbomIsIncludedInUberJar.gradle`** -> AI Confidence: **99.29%**
133. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/CyclonedxPluginActionIntegrationTests-sbomIsIncludedInUberWar.gradle`** -> AI Confidence: **99.29%**
134. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/DependencyManagementPluginActionIntegrationTests-helpfulErrorWhenVersionlessDependencyFailsToResolve.gradle`** -> AI Confidence: **99.29%**
135. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/DependencyManagementPluginActionIntegrationTests.gradle`** -> AI Confidence: **99.29%**
136. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-additionalMetadataLocationsConfiguredWhenProcessorIsPresent.gradle`** -> AI Confidence: **99.29%**
137. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-additionalMetadataLocationsNotConfiguredWhenProcessorIsAbsent.gradle`** -> AI Confidence: **99.29%**
138. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-compileClasspathDoesNotIncludeDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
139. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-compileClasspathDoesNotIncludeTestAndDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
140. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksCanOverrideDefaultParametersCompilerFlag.gradle`** -> AI Confidence: **99.29%**
141. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseParametersAndAdditionalCompilerFlags.gradle`** -> AI Confidence: **99.29%**
142. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseParametersCompilerFlagByDefault.gradle`** -> AI Confidence: **99.29%**
143. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseUtf8Encoding.gradle`** -> AI Confidence: **99.29%**
144. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-runtimeClasspathIncludesDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
145. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-runtimeClasspathIncludesTestAndDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
146. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-testCompileClasspathDoesNotIncludeDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
147. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-testCompileClasspathIncludesTestAndDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
148. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-testRuntimeClasspathDoesNotIncludeDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
149. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-testRuntimeClasspathIncludesTestAndDevelopmentOnlyDependencies.gradle`** -> AI Confidence: **99.29%**
150. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests-compileAotJavaHasTransitiveRuntimeDependenciesOnItsClasspathWhenUsingKotlin.gradle`** -> AI Confidence: **99.29%**
151. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests-compileAotTestJavaHasTransitiveRuntimeDependenciesOnItsClasspathWhenUsingKotlin.gradle`** -> AI Confidence: **99.29%**
152. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests-taskConfigurationIsAvoided.gradle`** -> AI Confidence: **99.29%**
153. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-applyingNativeImagePluginAppliesAotPlugin.gradle`** -> AI Confidence: **99.29%**
154. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-classesGeneratedDuringAotProcessingAreOnTheNativeImageClasspath.gradle`** -> AI Confidence: **99.29%**
155. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-classesGeneratedDuringAotTestProcessingAreOnTheTestNativeImageClasspath.gradle`** -> AI Confidence: **99.29%**
156. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-developmentOnlyDependenciesDoNotAppearInNativeImageClasspath.gradle`** -> AI Confidence: **99.29%**
157. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-nativeEntryIsAddedToManifest.gradle`** -> AI Confidence: **99.29%**
158. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-reachabilityMetadataConfigurationFilesAreCopiedToJar.gradle`** -> AI Confidence: **99.29%**
159. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-reachabilityMetadataConfigurationFilesFromFileRepositoryAreCopiedToJar.gradle`** -> AI Confidence: **99.29%**
160. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/NativeImagePluginActionIntegrationTests-testAndDevelopmentOnlyDependenciesDoNotAppearInNativeImageClasspath.gradle`** -> AI Confidence: **99.29%**
161. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/OnlyDependencyManagementIntegrationTests.gradle`** -> AI Confidence: **99.29%**
162. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/ProtobufPluginActionIntegrationTests-usesVersionOfGrpcPluginDependencyWhenSpecified.gradle`** -> AI Confidence: **99.29%**
163. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/ProtobufPluginActionIntegrationTests-usesVersionOfProtocDependencyWhenSpecified.gradle`** -> AI Confidence: **99.29%**
164. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/ProtobufPluginActionIntegrationTests.gradle`** -> AI Confidence: **99.29%**
165. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processAotDoesNotHaveDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
166. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processAotDoesNotHaveTestAndDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
167. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processAotHasLibraryResourcesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
168. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processAotHasTransitiveRuntimeDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
169. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotDoesNotHaveDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
170. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasLibraryResourcesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
171. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasTestAndDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
172. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasTransitiveRuntimeDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
173. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootPluginIntegrationTests-unresolvedDependenciesAreAnalyzedWhenDependencyResolutionFails.gradle`** -> AI Confidence: **99.29%**
174. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/WarPluginActionIntegrationTests.gradle`** -> AI Confidence: **99.29%**
175. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoIntegrationTests-basicExecution.gradle`** -> AI Confidence: **99.29%**
176. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoIntegrationTests-notUpToDateWhenExecutedTwiceWithFixedTimeAndChangedGradlePropertiesProjectVersion.gradle`** -> AI Confidence: **99.29%**
177. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoIntegrationTests-notUpToDateWhenExecutedTwiceWithFixedTimeAndChangedProjectVersion.gradle`** -> AI Confidence: **99.29%**
178. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-customLayers.gradle`** -> AI Confidence: **99.29%**
179. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-developmentOnlyDependenciesAreNotIncludedInTheArchive.gradle`** -> AI Confidence: **99.29%**
180. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-developmentOnlyDependenciesAreNotIncludedInTheArchiveByDefault.gradle`** -> AI Confidence: **99.29%**
181. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-developmentOnlyDependenciesCanBeIncludedInTheArchive.gradle`** -> AI Confidence: **99.29%**
182. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-duplicatesAreHandledGracefully.gradle`** -> AI Confidence: **99.29%**
183. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-explodedApplicationClasspath.gradle`** -> AI Confidence: **99.29%**
184. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-implicitLayers.gradle`** -> AI Confidence: **99.29%**
185. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-jarTypeFilteringIsApplied.gradle`** -> AI Confidence: **99.29%**
186. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-layersWithCustomSourceSet.gradle`** -> AI Confidence: **99.29%**
187. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-multiModuleCustomLayers.gradle`** -> AI Confidence: **99.29%**
188. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-multiModuleImplicitLayers.gradle`** -> AI Confidence: **99.29%**
189. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-packagedApplicationClasspath.gradle`** -> AI Confidence: **99.29%**
190. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-reproducibleArchive.gradle`** -> AI Confidence: **99.29%**
191. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-signed.gradle`** -> AI Confidence: **99.29%**
192. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-testAndDevelopmentOnlyDependenciesAreNotIncludedInTheArchiveByDefault.gradle`** -> AI Confidence: **99.29%**
193. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-testAndDevelopmentOnlyDependenciesCanBeIncludedInTheArchive.gradle`** -> AI Confidence: **99.29%**
194. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-versionMismatchBetweenTransitiveDevelopmentOnlyImplementationDependenciesDoesNotRemoveDependencyFromTheArchive.gradle`** -> AI Confidence: **99.29%**
195. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-customLayers.gradle`** -> AI Confidence: **99.29%**
196. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-developmentOnlyDependenciesAreNotIncludedInTheArchiveByDefault.gradle`** -> AI Confidence: **99.29%**
197. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-developmentOnlyDependenciesCanBeIncludedInTheArchive.gradle`** -> AI Confidence: **99.29%**
198. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-duplicatesAreHandledGracefully.gradle`** -> AI Confidence: **99.29%**
199. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-implicitLayers.gradle`** -> AI Confidence: **99.29%**
200. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-jarTypeFilteringIsApplied.gradle`** -> AI Confidence: **99.29%**
201. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-layersWithCustomSourceSet.gradle`** -> AI Confidence: **99.29%**
202. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-multiModuleCustomLayers.gradle`** -> AI Confidence: **99.29%**
203. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-multiModuleImplicitLayers.gradle`** -> AI Confidence: **99.29%**
204. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-reproducibleArchive.gradle`** -> AI Confidence: **99.29%**
205. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-signed.gradle`** -> AI Confidence: **99.29%**
206. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-testAndDevelopmentOnlyDependenciesAreNotIncludedInTheArchiveByDefault.gradle`** -> AI Confidence: **99.29%**
207. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-testAndDevelopmentOnlyDependenciesCanBeIncludedInTheArchive.gradle`** -> AI Confidence: **99.29%**
208. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-versionMismatchBetweenTransitiveDevelopmentOnlyImplementationDependenciesDoesNotRemoveDependencyFromTheArchive.gradle`** -> AI Confidence: **99.29%**
209. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/MavenIntegrationTests-bootJarCanBeUploaded.gradle`** -> AI Confidence: **99.29%**
210. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/MavenIntegrationTests-bootWarCanBeUploaded.gradle`** -> AI Confidence: **99.29%**
211. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootRunIntegrationTests-developmentOnlyDependenciesAreOnTheClasspath.gradle`** -> AI Confidence: **99.29%**
212. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootRunIntegrationTests-jarTypeFilteringIsAppliedToTheClasspath.gradle`** -> AI Confidence: **99.29%**
213. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootRunIntegrationTests-testAndDevelopmentOnlyDependenciesAreOnTheClasspath.gradle`** -> AI Confidence: **99.29%**
214. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootTestRunIntegrationTests-developmentOnlyDependenciesAreNotOnTheClasspath.gradle`** -> AI Confidence: **99.29%**
215. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootTestRunIntegrationTests-jarTypeFilteringIsAppliedToTheClasspath.gradle`** -> AI Confidence: **99.29%**
216. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/run/BootTestRunIntegrationTests-testAndDevelopmentOnlyDependenciesAreOnTheClasspath.gradle`** -> AI Confidence: **99.29%**
217. **`buildSrc/settings.gradle`** -> AI Confidence: **99.29%**
218. **`cli/spring-boot-cli/src/test/resources/grab-samples/duplicateDependencyManagementBom.groovy`** -> AI Confidence: **99.29%**
219. **`cli/spring-boot-cli/src/test/resources/scripts/options.groovy`** -> AI Confidence: **99.29%**
220. **`gradle/plugins/settings.gradle`** -> AI Confidence: **99.29%**
221. **`settings.gradle`** -> AI Confidence: **99.29%**
222. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-bootDistZipJarApp.gradle`** -> AI Confidence: **99.29%**
223. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-classDataSharingApp.gradle`** -> AI Confidence: **99.29%**
224. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-executableWarApp.gradle`** -> AI Confidence: **99.29%**
225. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-nativeApp.gradle`** -> AI Confidence: **99.29%**
226. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-plainDistZipJarApp.gradle`** -> AI Confidence: **99.29%**
227. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests-plainWarApp.gradle`** -> AI Confidence: **99.29%**
228. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/PaketoBuilderTests.gradle`** -> AI Confidence: **99.29%**
229. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/settings.gradle`** -> AI Confidence: **99.29%**
230. **`core/spring-boot/src/test/kotlin/org/springframework/boot/context/properties/bind/KotlinBindableRuntimeHintsRegistrarTests.kt`** -> AI Confidence: **99.29%**
231. **`core/spring-boot/src/test/kotlin/org/springframework/boot/context/properties/bind/KotlinDefaultBindConstructorProviderTests.kt`** -> AI Confidence: **99.29%**
232. **`smoke-test/spring-boot-smoke-test-webflux-coroutines/src/main/kotlin/smoketest/coroutines/CoroutinesController.kt`** -> AI Confidence: **99.29%**
233. **`integration-test/spring-boot-loader-integration-tests/src/dockerTest/resources/conf/oracle-jdk-17/Dockerfile`** -> AI Confidence: **99.29%**
234. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImageTests.java`** -> AI Confidence: **99.24%**
235. **`build-plugin/spring-boot-maven-plugin/src/dockerTest/java/org/springframework/boot/maven/BuildImageTests.java`** -> AI Confidence: **99.24%**
236. **`build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/RunIntegrationTests.java`** -> AI Confidence: **99.24%**
237. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractRunMojo.java`** -> AI Confidence: **99.24%**
238. **`build-plugin/spring-boot-maven-plugin/src/test/java/org/springframework/boot/maven/DockerTests.java`** -> AI Confidence: **99.24%**
239. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerConfigurationMetadataTests.java`** -> AI Confidence: **99.24%**
240. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitCommand.java`** -> AI Confidence: **99.24%**
241. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ProjectGenerator.java`** -> AI Confidence: **99.24%**
242. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ServiceCapabilitiesReportGenerator.java`** -> AI Confidence: **99.24%**
243. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/shell/CommandCompleter.java`** -> AI Confidence: **99.24%**
244. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AbstractDependsOnBeanFactoryPostProcessor.java`** -> AI Confidence: **99.24%**
245. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ImportAutoConfigurationImportSelector.java`** -> AI Confidence: **99.24%**
246. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBean.java`** -> AI Confidence: **99.24%**
247. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnBeanCondition.java`** -> AI Confidence: **99.24%**
248. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/CertificateMatcher.java`** -> AI Confidence: **99.24%**
249. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/FileWatcher.java`** -> AI Confidence: **99.24%**
250. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerCli.java`** -> AI Confidence: **99.24%**
251. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/lifecycle/DockerComposeLifecycleManager.java`** -> AI Confidence: **99.24%**
252. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/lifecycle/ServiceReadinessChecks.java`** -> AI Confidence: **99.24%**
253. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerHostTests.java`** -> AI Confidence: **99.24%**
254. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationReport.java`** -> AI Confidence: **99.24%**
255. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/AnnotationsPropertySource.java`** -> AI Confidence: **99.24%**
256. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/SpringBootTestContextBootstrapper.java`** -> AI Confidence: **99.24%**
257. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/FilterAnnotations.java`** -> AI Confidence: **99.24%**
258. **`core/spring-boot-test/src/test/java/org/springframework/boot/test/http/server/LocalTestWebServerTests.java`** -> AI Confidence: **99.24%**
259. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersStartup.java`** -> AI Confidence: **99.24%**
260. **`core/spring-boot/src/main/java/org/springframework/boot/DefaultApplicationContextFactory.java`** -> AI Confidence: **99.24%**
261. **`core/spring-boot/src/main/java/org/springframework/boot/EnvironmentConverter.java`** -> AI Confidence: **99.24%**
262. **`core/spring-boot/src/main/java/org/springframework/boot/StartupInfoLogger.java`** -> AI Confidence: **99.24%**
263. **`core/spring-boot/src/main/java/org/springframework/boot/cloud/CloudFoundryVcapEnvironmentPostProcessor.java`** -> AI Confidence: **99.24%**
264. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironment.java`** -> AI Confidence: **99.24%**
265. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentContributorPlaceholdersResolver.java`** -> AI Confidence: **99.24%**
266. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataLocationBindHandler.java`** -> AI Confidence: **99.24%**
267. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/InactiveConfigDataAccessException.java`** -> AI Confidence: **99.24%**
268. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/LocationResourceLoader.java`** -> AI Confidence: **99.24%**
269. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesBean.java`** -> AI Confidence: **99.24%**
270. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/PropertyMapper.java`** -> AI Confidence: **99.24%**
271. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/IndexedElementsBinder.java`** -> AI Confidence: **99.24%**
272. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/MapBinder.java`** -> AI Confidence: **99.24%**
273. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/validation/ValidationBindHandler.java`** -> AI Confidence: **99.24%**
274. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyName.java`** -> AI Confidence: **99.24%**
275. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/SpringConfigurationPropertySource.java`** -> AI Confidence: **99.24%**
276. **`core/spring-boot/src/main/java/org/springframework/boot/convert/ApplicationConversionService.java`** -> AI Confidence: **99.24%**
277. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BeanCurrentlyInCreationFailureAnalyzer.java`** -> AI Confidence: **99.24%**
278. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BindFailureAnalyzer.java`** -> AI Confidence: **99.24%**
279. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/NoSuchMethodFailureAnalyzer.java`** -> AI Confidence: **99.24%**
280. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzer.java`** -> AI Confidence: **99.24%**
281. **`core/spring-boot/src/main/java/org/springframework/boot/info/SslInfo.java`** -> AI Confidence: **99.24%**
282. **`core/spring-boot/src/main/java/org/springframework/boot/json/JsonWriter.java`** -> AI Confidence: **99.24%**
283. **`core/spring-boot/src/main/java/org/springframework/boot/logging/CorrelationIdFormatter.java`** -> AI Confidence: **99.24%**
284. **`core/spring-boot/src/main/java/org/springframework/boot/logging/LoggingSystemProperties.java`** -> AI Confidence: **99.24%**
285. **`core/spring-boot/src/main/java/org/springframework/boot/logging/StandardStackTracePrinter.java`** -> AI Confidence: **99.24%**
286. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/DefaultLogbackConfiguration.java`** -> AI Confidence: **99.24%**
287. **`core/spring-boot/src/main/java/org/springframework/boot/logging/structured/StructuredLoggingJsonProperties.java`** -> AI Confidence: **99.24%**
288. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/jks/JksSslStoreBundle.java`** -> AI Confidence: **99.24%**
289. **`core/spring-boot/src/main/java/org/springframework/boot/util/Instantiator.java`** -> AI Confidence: **99.24%**
290. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/FilterRegistration.java`** -> AI Confidence: **99.24%**
291. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/ServletRegistration.java`** -> AI Confidence: **99.24%**
292. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessorIntegrationTests.java`** -> AI Confidence: **99.24%**
293. **`core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/LoadedPemSslStoreTests.java`** -> AI Confidence: **99.24%**
294. **`core/spring-boot/src/test/java/org/springframework/boot/support/SpringApplicationJsonEnvironmentPostProcessorTests.java`** -> AI Confidence: **99.24%**
295. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/NestedJarFileResources.java`** -> AI Confidence: **99.24%**
296. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/SecurityInfo.java`** -> AI Confidence: **99.24%**
297. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/LaunchedClassLoader.java`** -> AI Confidence: **99.24%**
298. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/PropertiesLauncher.java`** -> AI Confidence: **99.24%**
299. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/web/PathMappedEndpoints.java`** -> AI Confidence: **99.24%**
300. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/management/PlainTextThreadDumpFormatter.java`** -> AI Confidence: **99.24%**
301. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/AbstractRabbitListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.24%**
302. **`module/spring-boot-cassandra/src/main/java/org/springframework/boot/cassandra/autoconfigure/CassandraAutoConfiguration.java`** -> AI Confidence: **99.24%**
303. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityService.java`** -> AI Confidence: **99.24%**
304. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/DataRedisAutoConfigurationJedisTests.java`** -> AI Confidence: **99.24%**
305. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/DataRedisAutoConfigurationTests.java`** -> AI Confidence: **99.24%**
306. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/PropertiesRedisConnectionDetailsTests.java`** -> AI Confidence: **99.24%**
307. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathChangedEvent.java`** -> AI Confidence: **99.24%**
308. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/filewatch/FileSystemWatcher.java`** -> AI Confidence: **99.24%**
309. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/RemoteUrlPropertyExtractorTests.java`** -> AI Confidence: **99.24%**
310. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/GrpcChannelBuilderCustomizers.java`** -> AI Confidence: **99.24%**
311. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/GrpcServerBuilderCustomizers.java`** -> AI Confidence: **99.24%**
312. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/HealthEndpointSupport.java`** -> AI Confidence: **99.24%**
313. **`module/spring-boot-health/src/test/java/org/springframework/boot/health/actuate/endpoint/SystemHealthDescriptorTests.java`** -> AI Confidence: **99.24%**
314. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JettyHttpClientBuilder.java`** -> AI Confidence: **99.24%**
315. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReactorHttpClientBuilder.java`** -> AI Confidence: **99.24%**
316. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonComponentModule.java`** -> AI Confidence: **99.24%**
317. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonComponentModule.java`** -> AI Confidence: **99.24%**
318. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DataSourceBuilderTests.java`** -> AI Confidence: **99.24%**
319. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/TomcatDataSourceConfigurationTests.java`** -> AI Confidence: **99.24%**
320. **`module/spring-boot-micrometer-observation/src/main/java/org/springframework/boot/micrometer/observation/autoconfigure/ObservationRegistryConfigurer.java`** -> AI Confidence: **99.24%**
321. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/CompositeTextMapPropagator.java`** -> AI Confidence: **99.24%**
322. **`module/spring-boot-micrometer-tracing/src/main/java/org/springframework/boot/micrometer/tracing/autoconfigure/TracingAndMeterObservationHandlerGroup.java`** -> AI Confidence: **99.24%**
323. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/autoconfigure/ConnectionFactoryConfigurations.java`** -> AI Confidence: **99.24%**
324. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/EmbeddedDatabaseConnectionTests.java`** -> AI Confidence: **99.24%**
325. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/autoconfigure/R2dbcAutoConfigurationTests.java`** -> AI Confidence: **99.24%**
326. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/autoconfigure/R2dbcAutoConfigurationWithoutConnectionPoolTests.java`** -> AI Confidence: **99.24%**
327. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/NettyWebServer.java`** -> AI Confidence: **99.24%**
328. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/GracefulShutdown.java`** -> AI Confidence: **99.24%**
329. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/SslConnectorCustomizer.java`** -> AI Confidence: **99.24%**
330. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/StaticResourceJars.java`** -> AI Confidence: **99.24%**
331. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/error/DefaultErrorWebExceptionHandler.java`** -> AI Confidence: **99.24%**
332. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/error/BasicErrorController.java`** -> AI Confidence: **99.24%**
333. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/AbstractManagementPortAndPathSampleActuatorApplicationTests.java`** -> AI Confidence: **99.24%**
334. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/MavenBuildOutputTimestamp.java`** -> AI Confidence: **99.23%**
335. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/metadata/ConfigurationMetadata.java`** -> AI Confidence: **99.23%**
336. **`configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/test/ItemMetadataAssert.java`** -> AI Confidence: **99.23%**
337. **`core/spring-boot/src/main/java/org/springframework/boot/availability/ApplicationAvailabilityBean.java`** -> AI Confidence: **99.23%**
338. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/PropertySourcesPlaceholdersResolver.java`** -> AI Confidence: **99.23%**
339. **`core/spring-boot/src/main/java/org/springframework/boot/json/BasicJsonParser.java`** -> AI Confidence: **99.23%**
340. **`module/spring-boot-actuator-autoconfigure/src/testFixtures/java/org/springframework/boot/actuate/autoconfigure/integrationtest/AbstractHealthEndpointAdditionalPathIntegrationTests.java`** -> AI Confidence: **99.23%**
341. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/DefaultRepositoryTagsProvider.java`** -> AI Confidence: **99.23%**
342. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/NettyAddress.java`** -> AI Confidence: **99.23%**
343. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/health/SimpleServingStatusMapper.java`** -> AI Confidence: **99.23%**
344. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/influx/InfluxPropertiesConfigAdapter.java`** -> AI Confidence: **99.23%**
345. **`module/spring-boot-restclient-test/src/main/java/org/springframework/boot/restclient/test/autoconfigure/RestClientTypeExcludeFilter.java`** -> AI Confidence: **99.23%**
346. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/HttpClientSettingsPropertyMapper.java`** -> AI Confidence: **99.22%**
347. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/CachingConnectionFactoryConfigurer.java`** -> AI Confidence: **99.2%**
348. **`build-plugin/spring-boot-antlib/src/main/java/org/springframework/boot/ant/FindMainClass.java`** -> AI Confidence: **99.18%**
349. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/dsl/SpringBootExtension.java`** -> AI Confidence: **99.18%**
350. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/ApplicationPluginAction.java`** -> AI Confidence: **99.18%**
351. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/JavaPluginAction.java`** -> AI Confidence: **99.18%**
352. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/ResolveMainClassName.java`** -> AI Confidence: **99.18%**
353. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/SpringBootAotPlugin.java`** -> AI Confidence: **99.18%**
354. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/SpringBootPlugin.java`** -> AI Confidence: **99.18%**
355. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/aot/ProcessTestAot.java`** -> AI Confidence: **99.18%**
356. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoProperties.java`** -> AI Confidence: **99.18%**
357. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImage.java`** -> AI Confidence: **99.18%**
358. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootWar.java`** -> AI Confidence: **99.18%**
359. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/ResolvedDependencies.java`** -> AI Confidence: **99.18%**
360. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/util/VersionExtractor.java`** -> AI Confidence: **99.18%**
361. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/TaskConfigurationAvoidanceTests.java`** -> AI Confidence: **99.18%**
362. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/dsl/BuildInfoDslIntegrationTests.java`** -> AI Confidence: **99.18%**
363. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/junit/GradleCompatibilityExtension.java`** -> AI Confidence: **99.18%**
364. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/ApplicationPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
365. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/CyclonedxPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
366. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
367. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/WarPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
368. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/PomCondition.java`** -> AI Confidence: **99.18%**
369. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractDependencyFilterMojo.java`** -> AI Confidence: **99.18%**
370. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractPackagerMojo.java`** -> AI Confidence: **99.18%**
371. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/BuildInfoMojo.java`** -> AI Confidence: **99.18%**
372. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/CommandLineBuilder.java`** -> AI Confidence: **99.18%**
373. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/DependencyFilter.java`** -> AI Confidence: **99.18%**
374. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/JarTypeFilter.java`** -> AI Confidence: **99.18%**
375. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/ProcessTestAotMojo.java`** -> AI Confidence: **99.18%**
376. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/VersionExtractor.java`** -> AI Confidence: **99.18%**
377. **`build-plugin/spring-boot-maven-plugin/src/test/java/org/springframework/boot/maven/ImageTests.java`** -> AI Confidence: **99.18%**
378. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerConfigurationMetadata.java`** -> AI Confidence: **99.18%**
379. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ssl/SslContextFactory.java`** -> AI Confidence: **99.18%**
380. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/transport/DockerEngineException.java`** -> AI Confidence: **99.18%**
381. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/ImageArchive.java`** -> AI Confidence: **99.18%**
382. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/ImageConfig.java`** -> AI Confidence: **99.18%**
383. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/FilePermissions.java`** -> AI Confidence: **99.18%**
384. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/InspectedContent.java`** -> AI Confidence: **99.18%**
385. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/ZipFileTarArchive.java`** -> AI Confidence: **99.18%**
386. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/json/JsonStream.java`** -> AI Confidence: **99.18%**
387. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/json/MappedObject.java`** -> AI Confidence: **99.18%**
388. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/DockerApiTests.java`** -> AI Confidence: **99.18%**
389. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/transport/RemoteHttpClientTransportTests.java`** -> AI Confidence: **99.18%**
390. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/type/ImageTests.java`** -> AI Confidence: **99.18%**
391. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/encodepassword/EncodePasswordCommand.java`** -> AI Confidence: **99.18%**
392. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitializrService.java`** -> AI Confidence: **99.18%**
393. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/options/OptionHandler.java`** -> AI Confidence: **99.18%**
394. **`configuration-metadata/spring-boot-configuration-metadata/src/test/java/org/springframework/boot/configurationmetadata/ConfigurationMetadataRepositoryJsonBuilderTests.java`** -> AI Confidence: **99.18%**
395. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/MetadataCollectors.java`** -> AI Confidence: **99.18%**
396. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/MetadataStore.java`** -> AI Confidence: **99.18%**
397. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/fieldvalues/javac/JavaCompilerFieldValuesParser.java`** -> AI Confidence: **99.18%**
398. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfiguration.java`** -> AI Confidence: **99.18%**
399. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationPackage.java`** -> AI Confidence: **99.18%**
400. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationReplacements.java`** -> AI Confidence: **99.18%**
401. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigureAfter.java`** -> AI Confidence: **99.18%**
402. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigureBefore.java`** -> AI Confidence: **99.18%**
403. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/SpringBootApplication.java`** -> AI Confidence: **99.18%**
404. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnSingleCandidate.java`** -> AI Confidence: **99.18%**
405. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/FilteringSpringBootCondition.java`** -> AI Confidence: **99.18%**
406. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnResourceCondition.java`** -> AI Confidence: **99.18%**
407. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ResourceCondition.java`** -> AI Confidence: **99.18%**
408. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/context/MessageSourceAutoConfiguration.java`** -> AI Confidence: **99.18%**
409. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/logging/ConditionEvaluationReportLoggingListener.java`** -> AI Confidence: **99.18%**
410. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/BundleContentProperty.java`** -> AI Confidence: **99.18%**
411. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/task/ScheduledBeanLazyInitializationExcludeFilter.java`** -> AI Confidence: **99.18%**
412. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/template/TemplateAvailabilityProviders.java`** -> AI Confidence: **99.18%**
413. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/web/WebProperties.java`** -> AI Confidence: **99.18%**
414. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/context/ConfigurationPropertiesAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
415. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/context/PropertyPlaceholderAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
416. **`core/spring-boot-autoconfigure/src/testFixtures/java/org/springframework/boot/autoconfigure/jndi/TestableInitialContextFactory.java`** -> AI Confidence: **99.18%**
417. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DefaultDockerCompose.java`** -> AI Confidence: **99.18%**
418. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerCliCommand.java`** -> AI Confidence: **99.18%**
419. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/ProcessRunner.java`** -> AI Confidence: **99.18%**
420. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/service/connection/ConnectionNamePredicate.java`** -> AI Confidence: **99.18%**
421. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/service/connection/DockerComposeServiceConnectionsApplicationListener.java`** -> AI Confidence: **99.18%**
422. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerCliCommandTests.java`** -> AI Confidence: **99.18%**
423. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerCliInspectResponseTests.java`** -> AI Confidence: **99.18%**
424. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/lifecycle/TcpConnectServiceReadinessCheckTests.java`** -> AI Confidence: **99.18%**
425. **`core/spring-boot-docker-compose/src/testFixtures/java/org/springframework/boot/docker/compose/service/connection/test/DockerComposeTestExtension.java`** -> AI Confidence: **99.18%**
426. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationListener.java`** -> AI Confidence: **99.18%**
427. **`core/spring-boot-test-autoconfigure/src/main/java/org/springframework/boot/test/autoconfigure/TestSliceTestContextBootstrapper.java`** -> AI Confidence: **99.18%**
428. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/ImportsContextCustomizer.java`** -> AI Confidence: **99.18%**
429. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/TypeExcludeFiltersContextCustomizerFactory.java`** -> AI Confidence: **99.18%**
430. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/runner/AbstractApplicationContextRunner.java`** -> AI Confidence: **99.18%**
431. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/http/server/LocalTestWebServer.java`** -> AI Confidence: **99.18%**
432. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/json/JacksonTester.java`** -> AI Confidence: **99.18%**
433. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/json/JsonContentAssert.java`** -> AI Confidence: **99.18%**
434. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/system/OutputCapture.java`** -> AI Confidence: **99.18%**
435. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/system/OutputCaptureRule.java`** -> AI Confidence: **99.18%**
436. **`core/spring-boot-test/src/test/java/org/springframework/boot/test/web/htmlunit/UriBuilderFactoryWebClientTests.java`** -> AI Confidence: **99.18%**
437. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleBeanFactoryPostProcessor.java`** -> AI Confidence: **99.18%**
438. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnection.java`** -> AI Confidence: **99.18%**
439. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnectionContextCustomizerFactory.java`** -> AI Confidence: **99.18%**
440. **`core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersStartupTests.java`** -> AI Confidence: **99.18%**
441. **`core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/service/connection/ContainerConnectionSourceTests.java`** -> AI Confidence: **99.18%**
442. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationShutdownHook.java`** -> AI Confidence: **99.18%**
443. **`core/spring-boot/src/main/java/org/springframework/boot/builder/SpringApplicationBuilder.java`** -> AI Confidence: **99.18%**
444. **`core/spring-boot/src/main/java/org/springframework/boot/context/ConfigurationWarningsApplicationContextInitializer.java`** -> AI Confidence: **99.18%**
445. **`core/spring-boot/src/main/java/org/springframework/boot/context/annotation/ImportCandidates.java`** -> AI Confidence: **99.18%**
446. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessor.java`** -> AI Confidence: **99.18%**
447. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataProperties.java`** -> AI Confidence: **99.18%**
448. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigTreeConfigDataLocationResolver.java`** -> AI Confidence: **99.18%**
449. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/InvalidConfigDataPropertyException.java`** -> AI Confidence: **99.18%**
450. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/Profiles.java`** -> AI Confidence: **99.18%**
451. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/StandardConfigDataLoader.java`** -> AI Confidence: **99.18%**
452. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesCharSequenceToObjectConverter.java`** -> AI Confidence: **99.18%**
453. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesJsr303Validator.java`** -> AI Confidence: **99.18%**
454. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesScan.java`** -> AI Confidence: **99.18%**
455. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesScanRegistrar.java`** -> AI Confidence: **99.18%**
456. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/ArrayBinder.java`** -> AI Confidence: **99.18%**
457. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/BindConverter.java`** -> AI Confidence: **99.18%**
458. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Bindable.java`** -> AI Confidence: **99.18%**
459. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java`** -> AI Confidence: **99.18%**
460. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/CollectionBinder.java`** -> AI Confidence: **99.18%**
461. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyNameAliases.java`** -> AI Confidence: **99.18%**
462. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/MutuallyExclusiveConfigurationPropertiesException.java`** -> AI Confidence: **99.18%**
463. **`core/spring-boot/src/main/java/org/springframework/boot/convert/CollectionToDelimitedStringConverter.java`** -> AI Confidence: **99.18%**
464. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DelimitedStringToArrayConverter.java`** -> AI Confidence: **99.18%**
465. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DurationToStringConverter.java`** -> AI Confidence: **99.18%**
466. **`core/spring-boot/src/main/java/org/springframework/boot/convert/PeriodToStringConverter.java`** -> AI Confidence: **99.18%**
467. **`core/spring-boot/src/main/java/org/springframework/boot/convert/StringToDurationConverter.java`** -> AI Confidence: **99.18%**
468. **`core/spring-boot/src/main/java/org/springframework/boot/convert/StringToPeriodConverter.java`** -> AI Confidence: **99.18%**
469. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/AbstractInjectionFailureAnalyzer.java`** -> AI Confidence: **99.18%**
470. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BindValidationFailureAnalyzer.java`** -> AI Confidence: **99.18%**
471. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/MutuallyExclusiveConfigurationPropertiesFailureAnalyzer.java`** -> AI Confidence: **99.18%**
472. **`core/spring-boot/src/main/java/org/springframework/boot/io/ApplicationResourceLoader.java`** -> AI Confidence: **99.18%**
473. **`core/spring-boot/src/main/java/org/springframework/boot/json/WritableJson.java`** -> AI Confidence: **99.18%**
474. **`core/spring-boot/src/main/java/org/springframework/boot/logging/DeferredLogs.java`** -> AI Confidence: **99.18%**
475. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ColorConverter.java`** -> AI Confidence: **99.18%**
476. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/Log4j2LoggingSystemProperties.java`** -> AI Confidence: **99.18%**
477. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/SpringBootTriggeringPolicy.java`** -> AI Confidence: **99.18%**
478. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/StructuredLogLayout.java`** -> AI Confidence: **99.18%**
479. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogbackConfigurator.java`** -> AI Confidence: **99.18%**
480. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogbackLoggingSystem.java`** -> AI Confidence: **99.18%**
481. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SpringProfileModelHandler.java`** -> AI Confidence: **99.18%**
482. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/StructuredLogEncoder.java`** -> AI Confidence: **99.18%**
483. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SystemStatusListener.java`** -> AI Confidence: **99.18%**
484. **`core/spring-boot/src/main/java/org/springframework/boot/logging/structured/GraylogExtendedLogFormatProperties.java`** -> AI Confidence: **99.18%**
485. **`core/spring-boot/src/main/java/org/springframework/boot/origin/Origin.java`** -> AI Confidence: **99.18%**
486. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/SslOptions.java`** -> AI Confidence: **99.18%**
487. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/pem/PemContent.java`** -> AI Confidence: **99.18%**
488. **`core/spring-boot/src/main/java/org/springframework/boot/support/EnvironmentPostProcessorApplicationListener.java`** -> AI Confidence: **99.18%**
489. **`core/spring-boot/src/main/java/org/springframework/boot/validation/MessageInterpolatorFactory.java`** -> AI Confidence: **99.18%**
490. **`core/spring-boot/src/main/java/org/springframework/boot/web/context/servlet/WebApplicationContextInitializer.java`** -> AI Confidence: **99.18%**
491. **`core/spring-boot/src/main/java/org/springframework/boot/web/error/Error.java`** -> AI Confidence: **99.18%**
492. **`core/spring-boot/src/main/java/org/springframework/boot/web/error/ErrorAttributeOptions.java`** -> AI Confidence: **99.18%**
493. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/AbstractFilterRegistrationBean.java`** -> AI Confidence: **99.18%**
494. **`core/spring-boot/src/test/java/org/springframework/boot/ResourceBannerTests.java`** -> AI Confidence: **99.18%**
495. **`core/spring-boot/src/test/java/org/springframework/boot/context/annotation/ConfigurationsTests.java`** -> AI Confidence: **99.18%**
496. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigTreeConfigDataLocationResolverTests.java`** -> AI Confidence: **99.18%**
497. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/StandardConfigDataLoaderTests.java`** -> AI Confidence: **99.18%**
498. **`core/spring-boot/src/test/java/org/springframework/boot/context/metrics/buffering/BufferingApplicationStartupTests.java`** -> AI Confidence: **99.18%**
499. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/bind/DefaultBindConstructorProviderTests.java`** -> AI Confidence: **99.18%**
500. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/BindFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
501. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/InvalidConfigurationPropertyNameFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
502. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/MissingParameterNamesFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
503. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoSuchMethodFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
504. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
505. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/UnboundConfigurationPropertyFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
506. **`core/spring-boot/src/test/java/org/springframework/boot/info/SslInfoTests.java`** -> AI Confidence: **99.18%**
507. **`core/spring-boot/src/test/java/org/springframework/boot/logging/log4j2/Log4J2LoggingSystemTests.java`** -> AI Confidence: **99.18%**
508. **`core/spring-boot/src/test/java/org/springframework/boot/logging/log4j2/SpringEnvironmentLookupTests.java`** -> AI Confidence: **99.18%**
509. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackLoggingSystemTests.java`** -> AI Confidence: **99.18%**
510. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackRuntimeHintsTests.java`** -> AI Confidence: **99.18%**
511. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/SpringBootJoranConfiguratorTests.java`** -> AI Confidence: **99.18%**
512. **`integration-test/spring-boot-actuator-integration-tests/src/test/java/org/springframework/boot/actuate/audit/AuditEventsEndpointWebIntegrationTests.java`** -> AI Confidence: **99.18%**
513. **`integration-test/spring-boot-actuator-integration-tests/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/JmxEndpointAccessIntegrationTests.java`** -> AI Confidence: **99.18%**
514. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/AbstractApplicationLauncher.java`** -> AI Confidence: **99.18%**
515. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/BootRunApplicationLauncher.java`** -> AI Confidence: **99.18%**
516. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/ExplodedApplicationLauncher.java`** -> AI Confidence: **99.18%**
517. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/IdeApplicationLauncher.java`** -> AI Confidence: **99.18%**
518. **`loader/spring-boot-jarmode-tools/src/main/java/org/springframework/boot/jarmode/tools/Command.java`** -> AI Confidence: **99.18%**
519. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/AbstractJarModeTests.java`** -> AI Confidence: **99.18%**
520. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/ExtractCommandTests.java`** -> AI Confidence: **99.18%**
521. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/ExtractLayersCommandTests.java`** -> AI Confidence: **99.18%**
522. **`loader/spring-boot-loader-tools/src/main/java/org/springframework/boot/loader/tools/BuildPropertiesWriter.java`** -> AI Confidence: **99.18%**
523. **`loader/spring-boot-loader-tools/src/main/java/org/springframework/boot/loader/tools/layer/CustomLayers.java`** -> AI Confidence: **99.18%**
524. **`loader/spring-boot-loader-tools/src/test/java/org/springframework/boot/loader/tools/layer/IncludeExcludeContentSelectorTests.java`** -> AI Confidence: **99.18%**
525. **`loader/spring-boot-loader-tools/src/test/java/org/springframework/boot/loader/tools/layer/LibraryContentFilterTests.java`** -> AI Confidence: **99.18%**
526. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/Archive.java`** -> AI Confidence: **99.18%**
527. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/ExplodedArchive.java`** -> AI Confidence: **99.18%**
528. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/nio/file/NestedByteChannel.java`** -> AI Confidence: **99.18%**
529. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/nio/file/NestedPath.java`** -> AI Confidence: **99.18%**
530. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/FileDataBlock.java`** -> AI Confidence: **99.18%**
531. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/jar/MetaInfVersionsInfoTests.java`** -> AI Confidence: **99.18%**
532. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/jar/SecurityInfoTests.java`** -> AI Confidence: **99.18%**
533. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/launch/ExplodedArchiveTests.java`** -> AI Confidence: **99.18%**
534. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/launch/JarFileArchiveTests.java`** -> AI Confidence: **99.18%**
535. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/ZipContentTests.java`** -> AI Confidence: **99.18%**
536. **`module/spring-boot-activemq/src/main/java/org/springframework/boot/activemq/testcontainers/ActiveMQContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
537. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/condition/ConditionsReportEndpoint.java`** -> AI Confidence: **99.18%**
538. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/EndpointAutoConfiguration.java`** -> AI Confidence: **99.18%**
539. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/condition/ConditionalOnAvailableEndpoint.java`** -> AI Confidence: **99.18%**
540. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/condition/OnAvailableEndpointCondition.java`** -> AI Confidence: **99.18%**
541. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/expose/IncludeExcludeEndpointFilter.java`** -> AI Confidence: **99.18%**
542. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/DefaultEndpointObjectNameFactory.java`** -> AI Confidence: **99.18%**
543. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/web/server/ManagementContextConfigurationImportSelector.java`** -> AI Confidence: **99.18%**
544. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/web/server/ManagementWebServerFactoryCustomizer.java`** -> AI Confidence: **99.18%**
545. **`module/spring-boot-actuator-autoconfigure/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/PropertiesEndpointAccessResolverTests.java`** -> AI Confidence: **99.18%**
546. **`module/spring-boot-actuator-autoconfigure/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/DefaultEndpointObjectNameFactoryTests.java`** -> AI Confidence: **99.18%**
547. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/beans/BeansEndpoint.java`** -> AI Confidence: **99.18%**
548. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/ShutdownEndpoint.java`** -> AI Confidence: **99.18%**
549. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/Jackson2BeanSerializer.java`** -> AI Confidence: **99.18%**
550. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/JacksonBeanSerializer.java`** -> AI Confidence: **99.18%**
551. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/DiscoveredOperationMethod.java`** -> AI Confidence: **99.18%**
552. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/DiscoveredOperationsFactory.java`** -> AI Confidence: **99.18%**
553. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/EndpointExtension.java`** -> AI Confidence: **99.18%**
554. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/invoker/cache/CachingOperationInvoker.java`** -> AI Confidence: **99.18%**
555. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/EndpointMBean.java`** -> AI Confidence: **99.18%**
556. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/Jackson2JmxOperationResponseMapper.java`** -> AI Confidence: **99.18%**
557. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/JacksonJmxOperationResponseMapper.java`** -> AI Confidence: **99.18%**
558. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/MBeanInfoFactory.java`** -> AI Confidence: **99.18%**
559. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/annotation/DiscoveredJmxOperation.java`** -> AI Confidence: **99.18%**
560. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/info/InfoPropertiesInfoContributor.java`** -> AI Confidence: **99.18%**
561. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/management/HeapDumpWebEndpoint.java`** -> AI Confidence: **99.18%**
562. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/sbom/SbomEndpointWebExtension.java`** -> AI Confidence: **99.18%**
563. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/context/properties/ConfigurationPropertiesReportEndpointFilteringTests.java`** -> AI Confidence: **99.18%**
564. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/endpoint/SanitizingFunctionTests.java`** -> AI Confidence: **99.18%**
565. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/sbom/SbomEndpointWebExtensionTests.java`** -> AI Confidence: **99.18%**
566. **`module/spring-boot-actuator/src/testFixtures/java/org/springframework/boot/actuate/endpoint/web/test/WebEndpointTestInvocationContextProvider.java`** -> AI Confidence: **99.18%**
567. **`module/spring-boot-artemis/src/main/java/org/springframework/boot/artemis/autoconfigure/ArtemisXAConnectionFactoryConfiguration.java`** -> AI Confidence: **99.18%**
568. **`module/spring-boot-batch-data-mongodb/src/main/java/org/springframework/boot/batch/mongodb/autoconfigure/BatchMongoSchemaInitializer.java`** -> AI Confidence: **99.18%**
569. **`module/spring-boot-batch-data-mongodb/src/test/java/org/springframework/boot/batch/mongodb/autoconfigure/BatchMongoSchemaInitializerTests.java`** -> AI Confidence: **99.18%**
570. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/actuate/endpoint/CachesEndpoint.java`** -> AI Confidence: **99.18%**
571. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/autoconfigure/CaffeineCacheConfiguration.java`** -> AI Confidence: **99.18%**
572. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/metrics/CacheMetricsRegistrar.java`** -> AI Confidence: **99.18%**
573. **`module/spring-boot-cache/src/test/java/org/springframework/boot/cache/autoconfigure/EhCache3CacheAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
574. **`module/spring-boot-cassandra/src/main/java/org/springframework/boot/cassandra/health/CassandraDriverHealthIndicator.java`** -> AI Confidence: **99.18%**
575. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/SecurityInterceptor.java`** -> AI Confidence: **99.18%**
576. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityInterceptor.java`** -> AI Confidence: **99.18%**
577. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/TokenValidator.java`** -> AI Confidence: **99.18%**
578. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/SecurityServiceTests.java`** -> AI Confidence: **99.18%**
579. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityServiceTests.java`** -> AI Confidence: **99.18%**
580. **`module/spring-boot-data-cassandra-test/src/main/java/org/springframework/boot/data/cassandra/test/autoconfigure/DataCassandraTest.java`** -> AI Confidence: **99.18%**
581. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/MetricsRepositoryMethodInvocationListener.java`** -> AI Confidence: **99.18%**
582. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/TimedAnnotations.java`** -> AI Confidence: **99.18%**
583. **`module/spring-boot-data-couchbase-test/src/main/java/org/springframework/boot/data/couchbase/test/autoconfigure/DataCouchbaseTest.java`** -> AI Confidence: **99.18%**
584. **`module/spring-boot-data-elasticsearch-test/src/main/java/org/springframework/boot/data/elasticsearch/test/autoconfigure/DataElasticsearchTest.java`** -> AI Confidence: **99.18%**
585. **`module/spring-boot-data-elasticsearch/src/test/java/org/springframework/boot/data/elasticsearch/health/DataElasticsearchReactiveHealthIndicatorTests.java`** -> AI Confidence: **99.18%**
586. **`module/spring-boot-data-jpa-test/src/main/java/org/springframework/boot/data/jpa/test/autoconfigure/DataJpaTest.java`** -> AI Confidence: **99.18%**
587. **`module/spring-boot-data-ldap-test/src/main/java/org/springframework/boot/data/ldap/test/autoconfigure/DataLdapTest.java`** -> AI Confidence: **99.18%**
588. **`module/spring-boot-data-mongodb-test/src/main/java/org/springframework/boot/data/mongodb/test/autoconfigure/DataMongoTest.java`** -> AI Confidence: **99.18%**
589. **`module/spring-boot-data-mongodb/src/main/java/org/springframework/boot/data/mongodb/autoconfigure/DataMongoConfiguration.java`** -> AI Confidence: **99.18%**
590. **`module/spring-boot-data-r2dbc-test/src/main/java/org/springframework/boot/data/r2dbc/test/autoconfigure/DataR2dbcTest.java`** -> AI Confidence: **99.18%**
591. **`module/spring-boot-data-redis-test/src/main/java/org/springframework/boot/data/redis/test/autoconfigure/DataRedisTest.java`** -> AI Confidence: **99.18%**
592. **`module/spring-boot-data-redis/src/main/java/org/springframework/boot/data/redis/health/DataRedisHealthIndicator.java`** -> AI Confidence: **99.18%**
593. **`module/spring-boot-data-redis/src/main/java/org/springframework/boot/data/redis/testcontainers/RedisContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
594. **`module/spring-boot-devtools/src/intTest/java/org/springframework/boot/devtools/tests/RemoteApplicationLauncher.java`** -> AI Confidence: **99.18%**
595. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/ConditionEvaluationDeltaLoggingListener.java`** -> AI Confidence: **99.18%**
596. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/RemoteDevtoolsSecurityConfiguration.java`** -> AI Confidence: **99.18%**
597. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathDirectories.java`** -> AI Confidence: **99.18%**
598. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathFileChangeListener.java`** -> AI Confidence: **99.18%**
599. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/remote/client/ClassPathChangeUploader.java`** -> AI Confidence: **99.18%**
600. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/remote/client/DelayedLiveReloadTrigger.java`** -> AI Confidence: **99.18%**
601. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/restart/ClassLoaderFilesResourcePatternResolver.java`** -> AI Confidence: **99.18%**
602. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/restart/OnInitializedRestarterCondition.java`** -> AI Confidence: **99.18%**
603. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/livereload/ConnectionOutputStreamTests.java`** -> AI Confidence: **99.18%**
604. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/livereload/LiveReloadServerTests.java`** -> AI Confidence: **99.18%**
605. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/restart/server/DefaultSourceDirectoryUrlFilterTests.java`** -> AI Confidence: **99.18%**
606. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/test/MockClientHttpRequestFactory.java`** -> AI Confidence: **99.18%**
607. **`module/spring-boot-elasticsearch/src/main/java/org/springframework/boot/elasticsearch/autoconfigure/Rest5ClientBuilderCustomizer.java`** -> AI Confidence: **99.18%**
608. **`module/spring-boot-elasticsearch/src/test/java/org/springframework/boot/elasticsearch/autoconfigure/ElasticsearchRestClientAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
609. **`module/spring-boot-flyway/src/main/java/org/springframework/boot/flyway/autoconfigure/FlywayAutoConfiguration.java`** -> AI Confidence: **99.18%**
610. **`module/spring-boot-freemarker/src/main/java/org/springframework/boot/freemarker/autoconfigure/FreeMarkerAutoConfiguration.java`** -> AI Confidence: **99.18%**
611. **`module/spring-boot-graphql-test/src/main/java/org/springframework/boot/graphql/test/autoconfigure/GraphQlTypeExcludeFilter.java`** -> AI Confidence: **99.18%**
612. **`module/spring-boot-graphql/src/main/java/org/springframework/boot/graphql/autoconfigure/DefaultGraphQlSchemaCondition.java`** -> AI Confidence: **99.18%**
613. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlQueryByExampleAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
614. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlQuerydslAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
615. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlReactiveQueryByExampleAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
616. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlReactiveQuerydslAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
617. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/security/GraphQlWebFluxSecurityAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
618. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/security/GraphQlWebMvcSecurityAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
619. **`module/spring-boot-groovy-templates/src/test/java/org/springframework/boot/groovy/template/autoconfigure/GroovyTemplateAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
620. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/GrpcClientCodecConfiguration.java`** -> AI Confidence: **99.18%**
621. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/PropertiesChannelCredentialsProvider.java`** -> AI Confidence: **99.18%**
622. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/ServerCredentials.java`** -> AI Confidence: **99.18%**
623. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/health/AutoConfiguredHealthCheckedGrpcComponents.java`** -> AI Confidence: **99.18%**
624. **`module/spring-boot-gson/src/test/java/org/springframework/boot/gson/autoconfigure/GsonAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
625. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/autoconfigure/HazelcastServerConfiguration.java`** -> AI Confidence: **99.18%**
626. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/autoconfigure/PropertiesHazelcastConnectionDetails.java`** -> AI Confidence: **99.18%**
627. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/testcontainers/HazelcastContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
628. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/CompositeHealthDescriptor.java`** -> AI Confidence: **99.18%**
629. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/application/AvailabilityStateHealthIndicator.java`** -> AI Confidence: **99.18%**
630. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/application/DiskSpaceHealthIndicator.java`** -> AI Confidence: **99.18%**
631. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/autoconfigure/actuate/endpoint/AvailabilityProbesHealthEndpointGroups.java`** -> AI Confidence: **99.18%**
632. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/registry/AbstractRegistry.java`** -> AI Confidence: **99.18%**
633. **`module/spring-boot-hibernate/src/main/java/org/springframework/boot/hibernate/autoconfigure/HibernateProperties.java`** -> AI Confidence: **99.18%**
634. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JettyClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
635. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReactorClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
636. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReflectiveComponentsClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
637. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/imperative/ImperativeHttpClientAutoConfiguration.java`** -> AI Confidence: **99.18%**
638. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/reactive/ReactiveHttpClientAutoConfiguration.java`** -> AI Confidence: **99.18%**
639. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/reactive/ClientHttpConnectorBuilder.java`** -> AI Confidence: **99.18%**
640. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/AbstractClientHttpRequestFactoryBuilderTests.java`** -> AI Confidence: **99.18%**
641. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/autoconfigure/service/HttpServiceClientPropertiesTests.java`** -> AI Confidence: **99.18%**
642. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/reactive/AbstractClientHttpConnectorBuilderTests.java`** -> AI Confidence: **99.18%**
643. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonComponent.java`** -> AI Confidence: **99.18%**
644. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonMixinModuleEntriesBeanRegistrationAotProcessor.java`** -> AI Confidence: **99.18%**
645. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/ObjectValueDeserializer.java`** -> AI Confidence: **99.18%**
646. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonComponent.java`** -> AI Confidence: **99.18%**
647. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonMixinModuleEntriesBeanRegistrationAotProcessor.java`** -> AI Confidence: **99.18%**
648. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonObjectDeserializer.java`** -> AI Confidence: **99.18%**
649. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/autoconfigure/Jackson2AutoConfiguration.java`** -> AI Confidence: **99.18%**
650. **`module/spring-boot-jdbc/src/dockerTest/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
651. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/DatabaseDriver.java`** -> AI Confidence: **99.18%**
652. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/autoconfigure/DataSourceProperties.java`** -> AI Confidence: **99.18%**
653. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/autoconfigure/health/DataSourceHealthContributorAutoConfiguration.java`** -> AI Confidence: **99.18%**
654. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
655. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/health/DataSourceHealthIndicator.java`** -> AI Confidence: **99.18%**
656. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/init/DataSourceScriptDatabaseInitializer.java`** -> AI Confidence: **99.18%**
657. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverClassNameTests.java`** -> AI Confidence: **99.18%**
658. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/JdbcTemplateAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
659. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/XADataSourceAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
660. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactoryConnectionDetailsTests.java`** -> AI Confidence: **99.18%**
661. **`module/spring-boot-jersey/src/main/java/org/springframework/boot/jersey/actuate/endpoint/web/JerseyEndpointResourceFactory.java`** -> AI Confidence: **99.18%**
662. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/JettyWebServer.java`** -> AI Confidence: **99.18%**
663. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/SslServerCustomizer.java`** -> AI Confidence: **99.18%**
664. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/JettyVirtualThreadsWebServerFactoryCustomizer.java`** -> AI Confidence: **99.18%**
665. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/actuate/web/server/JettyAccessLogCustomizer.java`** -> AI Confidence: **99.18%**
666. **`module/spring-boot-jooq/src/main/java/org/springframework/boot/jooq/autoconfigure/DefaultExceptionTranslatorExecuteListener.java`** -> AI Confidence: **99.18%**
667. **`module/spring-boot-jooq/src/main/java/org/springframework/boot/jooq/autoconfigure/SqlDialectLookup.java`** -> AI Confidence: **99.18%**
668. **`module/spring-boot-jooq/src/test/java/org/springframework/boot/jooq/autoconfigure/JooqPropertiesTests.java`** -> AI Confidence: **99.18%**
669. **`module/spring-boot-jpa/src/main/java/org/springframework/boot/jpa/JpaDatabaseInitializerDetector.java`** -> AI Confidence: **99.18%**
670. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/KafkaAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
671. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/KafkaPropertiesTests.java`** -> AI Confidence: **99.18%**
672. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/metrics/KafkaMetricsAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
673. **`module/spring-boot-liquibase/src/main/java/org/springframework/boot/liquibase/actuate/endpoint/LiquibaseEndpoint.java`** -> AI Confidence: **99.18%**
674. **`module/spring-boot-liquibase/src/test/java/org/springframework/boot/liquibase/LiquibaseChangelogMissingFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
675. **`module/spring-boot-mail/src/main/java/org/springframework/boot/mail/autoconfigure/MailSenderPropertiesConfiguration.java`** -> AI Confidence: **99.18%**
676. **`module/spring-boot-micrometer-metrics/src/dockerTest/java/org/springframework/boot/micrometer/metrics/testcontainers/otlp/OpenTelemetryMetricsContainerConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
677. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/prometheus/PrometheusScrapeEndpoint.java`** -> AI Confidence: **99.18%**
678. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/ssl/SslMeterBinder.java`** -> AI Confidence: **99.18%**
679. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/startup/StartupTimeMetricsListener.java`** -> AI Confidence: **99.18%**
680. **`module/spring-boot-micrometer-tracing-opentelemetry/src/dockerTest/java/org/springframework/boot/micrometer/tracing/opentelemetry/testcontainers/otlp/OpenTelemetryTracingContainerConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
681. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/OpenTelemetryEventPublisherBeansApplicationListener.java`** -> AI Confidence: **99.18%**
682. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/testcontainers/otlp/GrafanaOpenTelemetryTracingContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
683. **`module/spring-boot-micrometer-tracing/src/main/java/org/springframework/boot/micrometer/tracing/autoconfigure/prometheus/PrometheusExemplarsAutoConfiguration.java`** -> AI Confidence: **99.18%**
684. **`module/spring-boot-micrometer-tracing/src/test/java/org/springframework/boot/micrometer/tracing/autoconfigure/TracingAndMeterObservationHandlerGroupTests.java`** -> AI Confidence: **99.18%**
685. **`module/spring-boot-mongodb/src/main/java/org/springframework/boot/mongodb/autoconfigure/MongoClientFactorySupport.java`** -> AI Confidence: **99.18%**
686. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/reactive/view/MustacheView.java`** -> AI Confidence: **99.18%**
687. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/reactive/view/MustacheViewResolver.java`** -> AI Confidence: **99.18%**
688. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/servlet/view/MustacheViewResolver.java`** -> AI Confidence: **99.18%**
689. **`module/spring-boot-mustache/src/test/java/org/springframework/boot/mustache/autoconfigure/MustacheAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
690. **`module/spring-boot-neo4j/src/dockerTest/java/org/springframework/boot/neo4j/autoconfigure/Neo4jAutoConfigurationIntegrationTests.java`** -> AI Confidence: **99.18%**
691. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/autoconfigure/Neo4jAutoConfiguration.java`** -> AI Confidence: **99.18%**
692. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/health/Neo4jReactiveHealthIndicator.java`** -> AI Confidence: **99.18%**
693. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/testcontainers/DeprecatedNeo4jContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
694. **`module/spring-boot-opentelemetry/src/dockerTest/java/org/springframework/boot/opentelemetry/testcontainers/OtelCollectorOltpLoggingContainerConnectionDetailsFactoryTests.java`** -> AI Confidence: **99.18%**
695. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/autoconfigure/OpenTelemetrySdkAutoConfiguration.java`** -> AI Confidence: **99.18%**
696. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/autoconfigure/logging/otlp/OtlpLoggingConfigurations.java`** -> AI Confidence: **99.18%**
697. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/testcontainers/GrafanaOtlpLoggingContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
698. **`module/spring-boot-opentelemetry/src/test/java/org/springframework/boot/opentelemetry/autoconfigure/OpenTelemetryResourceAttributesTests.java`** -> AI Confidence: **99.18%**
699. **`module/spring-boot-opentelemetry/src/test/java/org/springframework/boot/opentelemetry/autoconfigure/logging/otlp/OtlpLoggingAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
700. **`module/spring-boot-persistence/src/main/java/org/springframework/boot/persistence/autoconfigure/EntityScanPackages.java`** -> AI Confidence: **99.18%**
701. **`module/spring-boot-pulsar/src/test/java/org/springframework/boot/pulsar/autoconfigure/Customizers.java`** -> AI Confidence: **99.18%**
702. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/OptionsCapableConnectionFactory.java`** -> AI Confidence: **99.18%**
703. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/init/R2dbcScriptDatabaseInitializerTests.java`** -> AI Confidence: **99.18%**
704. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/metrics/ConnectionPoolMetricsTests.java`** -> AI Confidence: **99.18%**
705. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/CompressionCustomizer.java`** -> AI Confidence: **99.18%**
706. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/SslServerCustomizer.java`** -> AI Confidence: **99.18%**
707. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/RestTemplateBuilder.java`** -> AI Confidence: **99.18%**
708. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/RestTemplateBuilderClientHttpRequestInitializer.java`** -> AI Confidence: **99.18%**
709. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/autoconfigure/RestClientBuilderConfigurer.java`** -> AI Confidence: **99.18%**
710. **`module/spring-boot-restclient/src/test/java/org/springframework/boot/restclient/RestClientWithRestTemplateTests.java`** -> AI Confidence: **99.18%**
711. **`module/spring-boot-restdocs/src/main/java/org/springframework/boot/restdocs/test/autoconfigure/AutoConfigureRestDocs.java`** -> AI Confidence: **99.18%**
712. **`module/spring-boot-resttestclient/src/main/java/org/springframework/boot/resttestclient/TestRestTemplate.java`** -> AI Confidence: **99.18%**
713. **`module/spring-boot-resttestclient/src/main/java/org/springframework/boot/resttestclient/autoconfigure/TestRestTemplateTestAutoConfiguration.java`** -> AI Confidence: **99.18%**
714. **`module/spring-boot-rsocket/src/main/java/org/springframework/boot/rsocket/autoconfigure/RSocketServerAutoConfiguration.java`** -> AI Confidence: **99.18%**
715. **`module/spring-boot-rsocket/src/main/java/org/springframework/boot/rsocket/netty/NettyRSocketServerFactory.java`** -> AI Confidence: **99.18%**
716. **`module/spring-boot-rsocket/src/test/java/org/springframework/boot/rsocket/netty/NettyRSocketServerFactoryTests.java`** -> AI Confidence: **99.18%**
717. **`module/spring-boot-security-oauth2-authorization-server/src/main/java/org/springframework/boot/security/oauth2/server/authorization/autoconfigure/servlet/RegisteredClientsConfiguredCondition.java`** -> AI Confidence: **99.18%**
718. **`module/spring-boot-security-oauth2-resource-server/src/test/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/OAuth2ResourceServerAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
719. **`module/spring-boot-security-oauth2-resource-server/src/test/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/reactive/ReactiveOAuth2ResourceServerAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
720. **`module/spring-boot-security/src/main/java/org/springframework/boot/security/web/reactive/ApplicationContextServerWebExchangeMatcher.java`** -> AI Confidence: **99.18%**
721. **`module/spring-boot-security/src/main/java/org/springframework/boot/security/web/servlet/ApplicationContextRequestMatcher.java`** -> AI Confidence: **99.18%**
722. **`module/spring-boot-servlet/src/main/java/org/springframework/boot/servlet/actuate/web/exchanges/HttpExchangesFilter.java`** -> AI Confidence: **99.18%**
723. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/actuate/endpoint/ReactiveSessionsEndpoint.java`** -> AI Confidence: **99.18%**
724. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/actuate/endpoint/SessionsEndpoint.java`** -> AI Confidence: **99.18%**
725. **`module/spring-boot-sql/src/main/java/org/springframework/boot/sql/init/AbstractScriptDatabaseInitializer.java`** -> AI Confidence: **99.18%**
726. **`module/spring-boot-sql/src/main/java/org/springframework/boot/sql/init/dependency/DatabaseInitializationDependencyConfigurer.java`** -> AI Confidence: **99.18%**
727. **`module/spring-boot-thymeleaf/src/main/java/org/springframework/boot/thymeleaf/autoconfigure/TemplateEngineConfigurations.java`** -> AI Confidence: **99.18%**
728. **`module/spring-boot-thymeleaf/src/main/java/org/springframework/boot/thymeleaf/autoconfigure/ThymeleafAutoConfiguration.java`** -> AI Confidence: **99.18%**
729. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/TomcatWebServerFactory.java`** -> AI Confidence: **99.18%**
730. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/actuate/web/server/TomcatAccessLogCustomizer.java`** -> AI Confidence: **99.18%**
731. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/metrics/TomcatMetricsBinder.java`** -> AI Confidence: **99.18%**
732. **`module/spring-boot-tomcat/src/test/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizerTests.java`** -> AI Confidence: **99.18%**
733. **`module/spring-boot-transaction/src/main/java/org/springframework/boot/transaction/jta/autoconfigure/JndiJtaConfiguration.java`** -> AI Confidence: **99.18%**
734. **`module/spring-boot-validation/src/main/java/org/springframework/boot/validation/autoconfigure/PrimaryDefaultValidatorPostProcessor.java`** -> AI Confidence: **99.18%**
735. **`module/spring-boot-validation/src/main/java/org/springframework/boot/validation/autoconfigure/ValidatorAdapter.java`** -> AI Confidence: **99.18%**
736. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/context/SpringBootTestRandomPortContextCustomizer.java`** -> AI Confidence: **99.18%**
737. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/reactive/context/ReactiveWebServerApplicationContextLocalTestWebServerProvider.java`** -> AI Confidence: **99.18%**
738. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/CookieSameSiteSupplier.java`** -> AI Confidence: **99.18%**
739. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentHandler.java`** -> AI Confidence: **99.18%**
740. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentRegisteringPostProcessor.java`** -> AI Confidence: **99.18%**
741. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentScan.java`** -> AI Confidence: **99.18%**
742. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentScanRegistrar.java`** -> AI Confidence: **99.18%**
743. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletWebServerApplicationContext.java`** -> AI Confidence: **99.18%**
744. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletWebServerApplicationContextLocalTestWebServerProvider.java`** -> AI Confidence: **99.18%**
745. **`module/spring-boot-web-server/src/test/java/org/springframework/boot/web/server/WebServerSslBundleTests.java`** -> AI Confidence: **99.18%**
746. **`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/reactive/AbstractReactiveWebServerFactoryTests.java`** -> AI Confidence: **99.18%**
747. **`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/MockServletWebServerFactory.java`** -> AI Confidence: **99.18%**
748. **`module/spring-boot-webflux-test/src/main/java/org/springframework/boot/webflux/test/autoconfigure/WebFluxTest.java`** -> AI Confidence: **99.18%**
749. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/WebFluxWebApplicationTypeDeducer.java`** -> AI Confidence: **99.18%**
750. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/AbstractWebFluxEndpointHandlerMapping.java`** -> AI Confidence: **99.18%**
751. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/AdditionalHealthEndpointPathsWebFluxHandlerMapping.java`** -> AI Confidence: **99.18%**
752. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/ControllerEndpointHandlerMapping.java`** -> AI Confidence: **99.18%**
753. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/exchanges/RecordableServerHttpRequest.java`** -> AI Confidence: **99.18%**
754. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/exchanges/RecordableServerHttpResponse.java`** -> AI Confidence: **99.18%**
755. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/ResourceChainResourceHandlerRegistrationCustomizer.java`** -> AI Confidence: **99.18%**
756. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WebFluxAutoConfiguration.java`** -> AI Confidence: **99.18%**
757. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WelcomePageRouterFunctionFactory.java`** -> AI Confidence: **99.18%**
758. **`module/spring-boot-webmvc-test/src/main/java/org/springframework/boot/webmvc/test/autoconfigure/SpringBootMockMvcBuilderCustomizer.java`** -> AI Confidence: **99.18%**
759. **`module/spring-boot-webmvc-test/src/main/java/org/springframework/boot/webmvc/test/autoconfigure/WebMvcTypeExcludeFilter.java`** -> AI Confidence: **99.18%**
760. **`module/spring-boot-webmvc-test/src/test/java/org/springframework/boot/webmvc/test/autoconfigure/mockmvc/WebMvcTestHtmlUnitWebClientIntegrationTests.java`** -> AI Confidence: **99.18%**
761. **`module/spring-boot-webmvc-test/src/test/java/org/springframework/boot/webmvc/test/autoconfigure/mockmvc/WebMvcTestHtmlUnitWebDriverIntegrationTests.java`** -> AI Confidence: **99.18%**
762. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/WebMvcWebApplicationTypeDeducer.java`** -> AI Confidence: **99.18%**
763. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/actuate/web/mappings/RequestMappingConditionsDescription.java`** -> AI Confidence: **99.18%**
764. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/JspTemplateAvailabilityProvider.java`** -> AI Confidence: **99.18%**
765. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfiguration.java`** -> AI Confidence: **99.18%**
766. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/CompositeHandlerExceptionResolver.java`** -> AI Confidence: **99.18%**
767. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/CompositeHandlerMapping.java`** -> AI Confidence: **99.18%**
768. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/error/DefaultErrorAttributes.java`** -> AI Confidence: **99.18%**
769. **`module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/WebMvcEndpointCorsIntegrationTests.java`** -> AI Confidence: **99.18%**
770. **`module/spring-boot-webservices-test/src/test/java/org/springframework/boot/webservices/test/autoconfigure/client/WebServiceClientIntegrationTests.java`** -> AI Confidence: **99.18%**
771. **`module/spring-boot-webservices/src/main/java/org/springframework/boot/webservices/client/WebServiceTemplateBuilder.java`** -> AI Confidence: **99.18%**
772. **`module/spring-boot-webservices/src/test/java/org/springframework/boot/webservices/autoconfigure/WebServicesAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
773. **`smoke-test/spring-boot-smoke-test-actuator-custom-security/src/test/java/smoketest/actuator/customsecurity/ManagementServerWithCustomServletPathSampleActuatorTests.java`** -> AI Confidence: **99.18%**
774. **`smoke-test/spring-boot-smoke-test-actuator-ui/src/test/java/smoketest/actuator/ui/SampleActuatorUiApplicationPortTests.java`** -> AI Confidence: **99.18%**
775. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/ManagementAddressActuatorApplicationTests.java`** -> AI Confidence: **99.18%**
776. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/ManagementPortSampleActuatorApplicationTests.java`** -> AI Confidence: **99.18%**
777. **`smoke-test/spring-boot-smoke-test-grpc-server-netty-shaded/src/dockerTest/java/smoketest/grpcservernettyshaded/SampleGrpcServerNettyShadedApplicationTests.java`** -> AI Confidence: **99.18%**
778. **`smoke-test/spring-boot-smoke-test-grpc-server-netty-shaded/src/main/java/smoketest/grpcservernettyshaded/HelloWorldService.java`** -> AI Confidence: **99.18%**
779. **`smoke-test/spring-boot-smoke-test-grpc-server-oauth/src/test/java/smoketest/grpcserveroauth/SampleGrpcServerOAuthApplicationTests.java`** -> AI Confidence: **99.18%**
780. **`smoke-test/spring-boot-smoke-test-grpc-server-servlet/src/main/java/smoketest/grpcserverservlet/HelloWorldService.java`** -> AI Confidence: **99.18%**
781. **`smoke-test/spring-boot-smoke-test-grpc-server/src/dockerTest/java/smoketest/grpcserver/SampleGrpcServerApplicationTests.java`** -> AI Confidence: **99.18%**
782. **`smoke-test/spring-boot-smoke-test-grpc-server/src/main/java/smoketest/grpcserver/HelloWorldService.java`** -> AI Confidence: **99.18%**
783. **`smoke-test/spring-boot-smoke-test-hateoas/src/test/java/smoketest/hateoas/SampleHateoasApplicationTests.java`** -> AI Confidence: **99.18%**
784. **`smoke-test/spring-boot-smoke-test-oauth2-authorization-server/src/test/java/smoketest/oauth2/server/SampleOAuth2AuthorizationServerApplicationTests.java`** -> AI Confidence: **99.18%**
785. **`smoke-test/spring-boot-smoke-test-property-validation/src/test/java/smoketest/propertyvalidation/SamplePropertyValidationApplicationTests.java`** -> AI Confidence: **99.18%**
786. **`smoke-test/spring-boot-smoke-test-secure-jersey/src/test/java/smoketest/secure/jersey/ManagementPortAndPathJerseyApplicationTests.java`** -> AI Confidence: **99.18%**
787. **`smoke-test/spring-boot-smoke-test-secure-jersey/src/test/java/smoketest/secure/jersey/ManagementPortCustomApplicationPathJerseyTests.java`** -> AI Confidence: **99.18%**
788. **`smoke-test/spring-boot-smoke-test-secure-webflux/src/test/java/smoketest/secure/webflux/ManagementPortSampleSecureWebFluxTests.java`** -> AI Confidence: **99.18%**
789. **`smoke-test/spring-boot-smoke-test-structured-logging-log4j2/src/test/java/smoketest/structuredlogging/log4j2/SampleLog4j2StructuredLoggingApplicationTests.java`** -> AI Confidence: **99.18%**
790. **`smoke-test/spring-boot-smoke-test-test/src/main/java/smoketest/test/service/RemoteVehicleDetailsService.java`** -> AI Confidence: **99.18%**
791. **`smoke-test/spring-boot-smoke-test-webservices/src/main/java/smoketest/webservices/endpoint/HolidayEndpoint.java`** -> AI Confidence: **99.18%**
792. **`smoke-test/spring-boot-smoke-test-webservices/src/test/java/smoketest/webservices/SampleWsApplicationTests.java`** -> AI Confidence: **99.18%**
793. **`smoke-test/spring-boot-smoke-test-websocket-jetty/src/test/java/smoketest/websocket/jetty/SampleWebSocketsApplicationTests.java`** -> AI Confidence: **99.18%**
794. **`smoke-test/spring-boot-smoke-test-websocket-tomcat/src/test/java/smoketest/websocket/tomcat/SampleWebSocketsApplicationTests.java`** -> AI Confidence: **99.18%**
795. **`system-test/spring-boot-image-system-tests/src/systemTest/java/org/springframework/boot/image/assertions/ContainerConfigAssert.java`** -> AI Confidence: **99.18%**
796. **`system-test/spring-boot-image-system-tests/src/systemTest/java/org/springframework/boot/image/assertions/ImageAssert.java`** -> AI Confidence: **99.18%**
797. **`test-support/spring-boot-docker-test-support/src/main/java/org/springframework/boot/testsupport/container/TestImage.java`** -> AI Confidence: **99.18%**
798. **`test-support/spring-boot-gradle-test-support/src/main/java/org/springframework/boot/testsupport/gradle/testkit/GradleBuild.java`** -> AI Confidence: **99.18%**
799. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/FileUtils.java`** -> AI Confidence: **99.18%**
800. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/classpath/resources/ResourcesClassLoader.java`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `cli/spring-boot-cli/src/json-shade/java/org/springframework/boot/cli/json/JSONTokener.java` -> **100.0%** Exposure
- `configuration-metadata/spring-boot-configuration-metadata/src/json-shade/java/org/springframework/boot/configurationmetadata/json/JSONTokener.java` -> **100.0%** Exposure
- `configuration-metadata/spring-boot-configuration-processor/src/json-shade/java/org/springframework/boot/configurationprocessor/json/JSONTokener.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnBeanCondition.java` -> **100.0%** Exposure
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesBean.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/CacheSpec.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/LayeredSpec.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/AotTests.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/BuildInfoIntegrationTests.java` -> **100.0%** Exposure
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/MavenBuild.java` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/ssl/PemFileWriter.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/SslPropertiesBundleRegistrarTests.java` -> **100.0%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemContentTests.java` -> **99.9998%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/BundleContentPropertyTests.java` -> **99.4119%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemSslStoreBundleTests.java` -> **98.9215%** Exposure
### Algorithmic DoS Exposure
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/MavenBuild.java` -> **100.0%** Exposure
- `module/spring-boot-restclient-test/src/main/java/org/springframework/boot/restclient/test/autoconfigure/MockRestServiceServerAutoConfiguration.java` -> **100.0%** Exposure
- `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js` -> **100.0%** Exposure
- `module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/DevToolsDataSourceAutoConfiguration.java` -> **99.9998%** Exposure
- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ProjectGenerator.java` -> **99.9773%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70425` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js` (JAVASCRIPT) -> Cumulative Risk: **777.35**
- **Archetype:** `file_cluster_11` (Distance: 13.598 IQR)
- **Magnitude:** 1578.96 | **LOC:** 1056 | **CtrlFlow:** 55.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `collectImportedStylesheets` (Impact: 141.4), `reloadStylesheetImages` (Impact: 105.3), `reload` (Impact: 77.6)

### 2. `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` (JAVA) -> Cumulative Risk: **764.92**
- **Archetype:** `file_cluster_13` (Distance: 12.474 IQR)
- **Magnitude:** 1224.16 | **LOC:** 1924 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `getSsl` (Impact: 21.2), `whenARequestIsActiveAfterGracefulShutdow` (Impact: 16.7), `tearDown` (Impact: 11.2)

### 3. `core/spring-boot-testcontainers/src/dockerTest/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleOrderWithScopeIntegrationTests.java` (JAVA) -> Cumulative Risk: **743.73**
- **Archetype:** `file_cluster_4` (Distance: 10.889 IQR)
- **Magnitude:** 127.42 | **LOC:** 204 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (99.7617%)
- **Heaviest Functions:** `remove` (Impact: 13.9), `destroy` (Impact: 5.5), `afterAll` (Impact: 4.7)

### 4. `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/MavenBuild.java` (JAVA) -> Cumulative Risk: **727.93**
- **Archetype:** `file_cluster_13` (Distance: 11.051 IQR)
- **Magnitude:** 153.12 | **LOC:** 223 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), Tech Debt (99.6221%)
- **Heaviest Functions:** `execute` (Impact: 76.4), `createTempDirectory` (Impact: 12.4), `project` (Impact: 4.2)

### 5. `smoke-test/spring-boot-smoke-test-web-thymeleaf/src/main/java/smoketest/web/thymeleaf/InMemoryMessageRepository.java` (JAVA) -> Cumulative Risk: **685.32**
- **Archetype:** `file_cluster_4` (Distance: 11.246 IQR)
- **Magnitude:** 43.02 | **LOC:** 58 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.99%)
- **Heaviest Functions:** `save` (Impact: 4.9), `deleteMessage` (Impact: 2.4), `findAll` (Impact: 2.1)

### 6. `smoke-test/spring-boot-smoke-test-web-groovy-templates/src/main/java/smoketest/groovytemplates/InMemoryMessageRepository.java` (JAVA) -> Cumulative Risk: **678.26**
- **Archetype:** `file_cluster_4` (Distance: 11.167 IQR)
- **Magnitude:** 38.54 | **LOC:** 53 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9921%)
- **Heaviest Functions:** `save` (Impact: 4.9), `findAll` (Impact: 2.1)

### 7. `cli/spring-boot-cli/src/main/executablecontent/bin/spring` (SHELL) -> Cumulative Risk: **648.13**
- **Archetype:** `file_cluster_12` (Distance: 14.829 IQR)
- **Magnitude:** 157.74 | **LOC:** 119 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 28.6), `Anonymous_Block` (Impact: 10.9), `__global_context__` (Impact: 8.1)

### 8. `module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/OpenTelemetryEventPublisherBeansApplicationListener.java` (JAVA) -> Cumulative Risk: **642.59**
- **Archetype:** `file_cluster_13` (Distance: 10.791 IQR)
- **Magnitude:** 148.0 | **LOC:** 203 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (97.4762%), State Flux (80.9406%)
- **Heaviest Functions:** `getStorageDelegate` (Impact: 21.9), `onApplicationEvent` (Impact: 16.7), `addWrapper` (Impact: 12.2)

### 9. `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/reactive/AbstractReactiveWebServerFactoryTests.java` (JAVA) -> Cumulative Risk: **635.29**
- **Archetype:** `file_cluster_4` (Distance: 12.195 IQR)
- **Magnitude:** 659.86 | **LOC:** 823 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7958%), Cognitive Load (96.3435%)
- **Heaviest Functions:** `tearDown` (Impact: 11.2), `doWithRetry` (Impact: 10.4), `givenAnInflightRequestWhenTheServerIsSto` (Impact: 10.3)

### 10. `core/spring-boot/src/main/java/org/springframework/boot/convert/ApplicationConversionService.java` (JAVA) -> Cumulative Risk: **611.6**
- **Archetype:** `file_cluster_13` (Distance: 11.081 IQR)
- **Magnitude:** 519.04 | **LOC:** 597 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), Tech Debt (99.9986%)
- **Heaviest Functions:** `addBean` (Impact: 157.6), `parse` (Impact: 22.9), `addFormatterForFieldType` (Impact: 16.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `build-plugin/spring-boot-maven-plugin/src/dockerTest/projects/build-image-bindings/bindings/ca-certificates/test.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-client-app/src/main/resources/ca/test-ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/alt/test-hello-alt-server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/alt/test-hello-alt-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/ca/test-ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/default/test-hello-server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-reactive-app/src/main/resources/default/test-hello-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/alt/test-hello-alt-server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/alt/test-hello-alt-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/ca/test-ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/default/test-hello-server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `integration-test/spring-boot-sni-integration-tests/spring-boot-sni-servlet-app/src/main/resources/default/test-hello-server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/client-keystore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/client-truststore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/server-keystore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose/server-truststore.p12` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `module/spring-boot-cache/src/test/java/org/springframework/boot/cache/autoconfigure/CacheAutoConfigurationTests.java` (JAVA) | Magnitude: 168.66 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 889, structural_boundaries: 370, func_start: 172, args: 162
- `module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/filewatch/ChangedFileTests.java` (JAVA) | Magnitude: 18.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 44, structural_boundaries: 30, io: 15, func_start: 12
- `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/TestJdbcConnectionDetails.java` (JAVA) | Magnitude: 26.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 10, func_start: 7, args: 5
- `build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImage.java` (JAVA) | Magnitude: 192.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 280, structural_boundaries: 91, doc: 66, decorators: 56
- `loader/spring-boot-loader-tools/src/test/java/org/springframework/boot/loader/tools/RepackagerTests.java` (JAVA) | Magnitude: 0.11 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 208, structural_boundaries: 117, func_start: 59, test: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `core/spring-boot/src/main/java/org/springframework/boot/bootstrap/BootstrapContextClosedEvent.java` (JAVA) | Magnitude: 11.42 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 7, doc: 7, api: 5
- `core/spring-boot/src/main/java/org/springframework/boot/ExitCodeEvent.java` (JAVA) | Magnitude: 7.24 | Delta: **0.307 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, doc: 7, structural_boundaries: 5, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js` (JAVASCRIPT) | Magnitude: 1578.96 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 914, state_mutation: 633, branch: 225, structural_boundaries: 178

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` (SHELL) | Magnitude: 157.74 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 75, indent_tabs: 63, branch: 58, reflection_metaprogramming: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `core/spring-boot-test/src/main/java/org/springframework/boot/test/context/FilteredClassLoader.java` (JAVA) | Magnitude: 139.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 128, structural_boundaries: 50, branch: 32, func_start: 26
- `module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/mappings/RequestMappingConditionsDescription.java` (JAVA) | Magnitude: 70.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 85, structural_boundaries: 29, args: 19, api: 14
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/condition/ConditionalOnJavaTests.java` (JAVA) | Magnitude: 47.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 45, func_start: 26, decorators: 21
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/task/TaskSchedulingAutoConfigurationTests.java` (JAVA) | Magnitude: 102.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 261, structural_boundaries: 164, func_start: 67, args: 60
- `test-support/spring-boot-test-support/src/test/java/org/springframework/boot/testsupport/classpath/resources/WithPackageResourcesTests.java` (JAVA) | Magnitude: 4.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 17, indent_tabs: 16, func_start: 8, test: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java` (JAVA) | Magnitude: 256.82 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 96, indent_tabs: 81, args: 54, closures: 47
- `module/spring-boot-data-rest/src/main/java/org/springframework/boot/data/rest/autoconfigure/DataRestProperties.java` (JAVA) | Magnitude: 183.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 99, branch: 48, args: 38, structural_boundaries: 33
- `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java` (JAVA) | Magnitude: 720.06 | Delta: **0.175 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 213, branch: 148, args: 101, closures: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/spring-boot/src/test/kotlin/org/springframework/boot/kotlinsample/TestKotlinApplication.kt` (KOTLIN) | Magnitude: 3.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 2, import: 2, args: 1, func_start: 1
- `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/EndpointDiscoverer.java` (JAVA) | Magnitude: 282.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 352, structural_boundaries: 123, generics: 78, branch: 73
- `module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/actuate/endpoint/MetricsEndpoint.java` (JAVA) | Magnitude: 160.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 166, structural_boundaries: 66, generics: 44, args: 43
- `smoke-test/spring-boot-smoke-test-data-r2dbc-flyway/src/main/java/smoketest/data/r2dbc/CityRepository.java` (JAVA) | Magnitude: 20.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 2, generics: 2, import: 2
- `smoke-test/spring-boot-smoke-test-data-r2dbc-liquibase/src/main/java/smoketest/data/r2dbc/CityRepository.java` (JAVA) | Magnitude: 20.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 2, generics: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `module/spring-boot-h2console/src/main/java/org/springframework/boot/h2console/autoconfigure/H2ConsoleAutoConfiguration.java` (JAVA) | Magnitude: 82.7 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 37, concurrency: 24, import: 20
- `core/spring-boot-testcontainers/src/dockerTest/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleOrderWithScopeIntegrationTests.java` (JAVA) | Magnitude: 127.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 103, structural_boundaries: 73, concurrency: 42, import: 31
- `module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/endpoint/invoker/cache/CachingOperationInvokerTests.java` (JAVA) | Magnitude: 167.12 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 249, structural_boundaries: 142, func_start: 80, concurrency: 56
- `module/spring-boot-health/src/test/java/org/springframework/boot/health/contributor/MapCompositeTests.java` (JAVA) | Magnitude: 83.16 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 94, func_start: 36, structural_boundaries: 31, args: 29
- `loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/DataBlockTests.java` (JAVA) | Magnitude: 37.82 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 34, indent_tabs: 29, concurrency: 18, import: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/validation/BindValidationException.java` (JAVA) | Magnitude: 13.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 8, doc: 6, args: 4
- `module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/endpoint/InvocationContextTests.java` (JAVA) | Magnitude: 10.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 29, structural_boundaries: 21, func_start: 10, test: 10
- `module/spring-boot-cassandra/src/main/java/org/springframework/boot/cassandra/autoconfigure/CassandraProperties.java` (JAVA) | Magnitude: 150.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 177, structural_boundaries: 63, api: 50, func_start: 33
- `module/spring-boot-data-r2dbc/src/test/java/org/springframework/boot/data/r2dbc/autoconfigure/DataR2dbcRepositoriesAutoConfigurationTests.java` (JAVA) | Magnitude: 30.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 81, structural_boundaries: 66, import: 24, args: 18
- `smoke-test/spring-boot-smoke-test-jersey/src/main/java/smoketest/jersey/JerseyConfig.java` (JAVA) | Magnitude: 5.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 4, func_start: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerProcessStartException.java` (JAVA) | Magnitude: 3.02 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, ownership: 3, indent_tabs: 3, func_start: 2
- `core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerNotRunningException.java` (JAVA) | Magnitude: 7.22 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 4, doc: 4, func_start: 3
- `core/spring-boot/src/main/javaTemplates/org/springframework/boot/SpringBootVersion.java` (JAVA) | Magnitude: 7.36 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 5, doc: 4, ownership: 4, structural_boundaries: 3
- `core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerOutputParseException.java` (JAVA) | Magnitude: 4.72 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, ownership: 3, indent_tabs: 3, func_start: 2
- `core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerCliComposeVersionResponse.java` (JAVA) | Magnitude: 2.16 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: ownership: 3, structural_boundaries: 2, doc: 2, args: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/autoconfigure/JacksonAutoConfiguration.java` -> Churn: **56.32%** | Cog Load: 17.684% | Debt: 99.6935%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1224.16
- `core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzerTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1199.01
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 826.42
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyName.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 694.26
- `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DataSourceBuilderTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 580.1

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 83.664%)
- `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/DiscoveredOperationMethod.java` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 74.6165%)
- `core/spring-boot-test/src/main/java/org/springframework/boot/test/context/SpringBootTestContextBootstrapper.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 67.8473%)
- `module/spring-boot-ldap/src/main/java/org/springframework/boot/ldap/autoconfigure/LdapAutoConfiguration.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 68.0896%)
- `module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfiguration.java` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 36.0601%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/util/Log.java` -> **Severity: 1159.265** (Blast Radius: 12.495 * Doc Risk: 92.7783%)
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -> **Severity: 426.662** (Blast Radius: 4.873 * Doc Risk: 87.5563%)
- `buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/Manifest.java` -> **Severity: 272.9** (Blast Radius: 2.729 * Doc Risk: 100.0%)
- `module/spring-boot-health/src/main/java/org/springframework/boot/health/contributor/Status.java` -> **Severity: 229.1** (Blast Radius: 2.291 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationProperty.java` -> **Severity: 207.0** (Blast Radius: 2.07 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
