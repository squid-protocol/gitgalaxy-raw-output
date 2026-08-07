# ARCHITECTURAL_BRIEF: spring-boot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/spring-boot` |
| **Timestamp** | `2026-08-07T05:38:02.903575+00:00` |
| **Scan Duration** | `21.84s` |
| **Git Branch** | `main` |
| **Git Commit** | `5cecd3922fce651f13d16a85d8a29efaa7f44cfd` |
| **Git Remote** | `https://github.com/spring-projects/spring-boot` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 8009 malicious artifacts.

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
> **Architectural Drift Z-Score:** `6.099`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 5590 | 63.1% |
| file_cluster_8 | 2580 | 29.1% |
| file_cluster_0 | 258 | 2.9% |
| file_cluster_16 | 100 | 1.1% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 8.4 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 28.4 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.8 | 0.0 | 0.0 |
| API Exposure | 0.0 | 13.3 | 2.7 | 1.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 13.6 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 80.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 8.0 | 1.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 76.0 | 3.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
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

- `ServiceConfig` (@ `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`) -> Impact: **347.2** | LOC: 281
- `customize` (@ `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizer.java`) -> Impact: **257.7** | LOC: 75
  * *Intent:* /** * Customization for Tomcat-specific features common to both Servlet and Reactive servers. * * @author Brian Clozel * @author Yulin Qin * @author S...
- `configure` (@ `module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java`) -> Impact: **217.1** | LOC: 48
  * *Intent:* /** * Creates a new configurer that will use the given {@code resourceLoader} and * {@code properties}.
- `MethodConfig` (@ `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`) -> Impact: **199.4** | LOC: 85
  * *Intent:* /** * 'weighted round robin' load balancing. * * @param blackoutPeriod must report load metrics continuously for at least this * long before the endpo...
- `configureContainer` (@ `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/ConcurrentKafkaListenerContainerFactoryConfigurer.java`) -> Impact: **191.6** | LOC: 30
- `customize` (@ `module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/servlet/ServletWebServerFactoryCustomizer.java`) -> Impact: **160.4** | LOC: 24
- `defaultPartHttpMessageReaderCustomizer` (@ `module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/ReactiveMultipartAutoConfiguration.java`) -> Impact: **148.8** | LOC: 37
- `customize` (@ `module/spring-boot-kotlinx-serialization-json/src/main/java/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonAutoConfiguration.java`) -> Impact: **145.5** | LOC: 20
- `customize` (@ `module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/JettyWebServerFactoryCustomizer.java`) -> Impact: **143.6** | LOC: 31
  * *Intent:* /** * Customization for Jetty-specific features common for both Servlet and Reactive servers. * * @author Brian Clozel * @author Phillip Webb * @autho...
- `databaseJdbcUrlLookups` (@ `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverTests.java`) -> Impact: **131.8** | LOC: 36

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
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java` -> **125** Orphaned Functions | **173** Duplicates
- `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` -> **136** Orphaned Functions | **61** Duplicates
- `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` -> **109** Orphaned Functions | **53** Duplicates
- `module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfigurationTests.java` -> **110** Orphaned Functions | **14** Duplicates
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/bind/JavaBeanBinderTests.java` -> **63** Orphaned Functions | **59** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`core/spring-boot/src/test/java/org/springframework/boot/cloud/CloudFoundryVcapEnvironmentPostProcessorTests.java`** -> AI Confidence: **99.48%**
2. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java`** -> AI Confidence: **99.48%**
3. **`module/spring-boot-pulsar/src/main/java/org/springframework/boot/pulsar/autoconfigure/PulsarPropertiesMapper.java`** -> AI Confidence: **99.48%**
4. **`module/spring-boot-security-oauth2-authorization-server/src/main/java/org/springframework/boot/security/oauth2/server/authorization/autoconfigure/servlet/OAuth2AuthorizationServerPropertiesMapper.java`** -> AI Confidence: **99.48%**
5. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/servlet/ServletWebServerFactoryCustomizer.java`** -> AI Confidence: **99.48%**
6. **`core/spring-boot/src/test/java/org/springframework/boot/logging/StandardStackTracePrinterTests.java`** -> AI Confidence: **99.39%**
7. **`module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/ConcurrentKafkaListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.39%**
8. **`module/spring-boot-ldap/src/test/java/org/springframework/boot/ldap/autoconfigure/embedded/EmbeddedLdapAutoConfigurationTests.java`** -> AI Confidence: **99.39%**
9. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/ReactiveMultipartAutoConfiguration.java`** -> AI Confidence: **99.39%**
10. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/PropertiesGrpcChannelBuilderCustomizer.java`** -> AI Confidence: **99.35%**
11. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java`** -> AI Confidence: **99.35%**
12. **`module/spring-boot-security-oauth2-client/src/main/java/org/springframework/boot/security/oauth2/client/autoconfigure/OAuth2ClientPropertiesMapper.java`** -> AI Confidence: **99.35%**
13. **`module/spring-boot-kotlinx-serialization-json/src/test/java/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonPropertiesTests.java`** -> AI Confidence: **99.34%**
14. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverTests.java`** -> AI Confidence: **99.32%**
15. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/DockerSpecTests.java`** -> AI Confidence: **99.31%**
16. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthentication.java`** -> AI Confidence: **99.31%**
17. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`** -> AI Confidence: **99.31%**
18. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/ResolvedDockerHostTests.java`** -> AI Confidence: **99.31%**
19. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/type/ImageReferenceTests.java`** -> AI Confidence: **99.31%**
20. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/CommandRunner.java`** -> AI Confidence: **99.31%**
21. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/core/HintCommand.java`** -> AI Confidence: **99.31%**
22. **`configuration-metadata/spring-boot-configuration-metadata-changelog-generator/src/main/java/org/springframework/boot/configurationmetadata/changelog/ChangelogWriter.java`** -> AI Confidence: **99.31%**
23. **`configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/metadata/JsonMarshallerTests.java`** -> AI Confidence: **99.31%**
24. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/logging/ConditionEvaluationReportMessage.java`** -> AI Confidence: **99.31%**
25. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/service/connection/ConnectionDetailsFactories.java`** -> AI Confidence: **99.31%**
26. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/assertj/ApplicationContextAssert.java`** -> AI Confidence: **99.31%**
27. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/FileHint.java`** -> AI Confidence: **99.31%**
28. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/BindableRuntimeHintsRegistrar.java`** -> AI Confidence: **99.31%**
29. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/DefaultBindConstructorProvider.java`** -> AI Confidence: **99.31%**
30. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/JavaBeanBinder.java`** -> AI Confidence: **99.31%**
31. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/SpringIterableConfigurationPropertySource.java`** -> AI Confidence: **99.31%**
32. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DurationStyle.java`** -> AI Confidence: **99.31%**
33. **`core/spring-boot/src/main/java/org/springframework/boot/convert/PeriodStyle.java`** -> AI Confidence: **99.31%**
34. **`core/spring-boot/src/main/java/org/springframework/boot/json/JsonValueWriter.java`** -> AI Confidence: **99.31%**
35. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ElasticCommonSchemaStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
36. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/GraylogExtendedLogFormatStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
37. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/LogstashStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
38. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/ElasticCommonSchemaStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
39. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/GraylogExtendedLogFormatStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
40. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogstashStructuredLogFormatter.java`** -> AI Confidence: **99.31%**
41. **`core/spring-boot/src/main/java/org/springframework/boot/retry/RetryPolicySettings.java`** -> AI Confidence: **99.31%**
42. **`core/spring-boot/src/main/java/org/springframework/boot/system/ApplicationHome.java`** -> AI Confidence: **99.31%**
43. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/PropertyMapperTests.java`** -> AI Confidence: **99.31%**
44. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/source/FilteredIterableConfigurationPropertiesSourceTests.java`** -> AI Confidence: **99.31%**
45. **`core/spring-boot/src/test/java/org/springframework/boot/json/JsonWriterTests.java`** -> AI Confidence: **99.31%**
46. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/net/protocol/jar/JarUrlClassLoader.java`** -> AI Confidence: **99.31%**
47. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/ZipString.java`** -> AI Confidence: **99.31%**
48. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/web/CorsEndpointProperties.java`** -> AI Confidence: **99.31%**
49. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/ProducibleOperationArgumentResolver.java`** -> AI Confidence: **99.31%**
50. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/SanitizingFunction.java`** -> AI Confidence: **99.31%**
51. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitTemplateConfigurer.java`** -> AI Confidence: **99.31%**
52. **`module/spring-boot-amqp/src/test/java/org/springframework/boot/amqp/autoconfigure/RabbitPropertiesTests.java`** -> AI Confidence: **99.31%**
53. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/TokenValidatorTests.java`** -> AI Confidence: **99.31%**
54. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/TokenValidatorTests.java`** -> AI Confidence: **99.31%**
55. **`module/spring-boot-graphql/src/main/java/org/springframework/boot/graphql/autoconfigure/GraphQlCorsProperties.java`** -> AI Confidence: **99.31%**
56. **`module/spring-boot-groovy-templates/src/main/java/org/springframework/boot/groovy/template/autoconfigure/GroovyTemplateAutoConfiguration.java`** -> AI Confidence: **99.31%**
57. **`module/spring-boot-grpc-client/src/test/java/org/springframework/boot/grpc/client/autoconfigure/GrpcClientPropertiesTests.java`** -> AI Confidence: **99.31%**
58. **`module/spring-boot-grpc-client/src/test/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfigTests.java`** -> AI Confidence: **99.31%**
59. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/PropertiesServerBuilderCustomizer.java`** -> AI Confidence: **99.31%**
60. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/health/SimpleStatusAggregator.java`** -> AI Confidence: **99.31%**
61. **`module/spring-boot-gson/src/main/java/org/springframework/boot/gson/autoconfigure/GsonAutoConfiguration.java`** -> AI Confidence: **99.31%**
62. **`module/spring-boot-hazelcast/src/test/java/org/springframework/boot/hazelcast/autoconfigure/HazelcastAutoConfigurationTests.java`** -> AI Confidence: **99.31%**
63. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/SimpleHttpCodeStatusMapper.java`** -> AI Confidence: **99.31%**
64. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/SimpleStatusAggregator.java`** -> AI Confidence: **99.31%**
65. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JdkHttpClientBuilder.java`** -> AI Confidence: **99.31%**
66. **`module/spring-boot-http-converter/src/main/java/org/springframework/boot/http/converter/autoconfigure/HttpMessageConverters.java`** -> AI Confidence: **99.31%**
67. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/autoconfigure/SpringBeanHandlerInstantiator.java`** -> AI Confidence: **99.31%**
68. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/DataSourceBuilder.java`** -> AI Confidence: **99.31%**
69. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/EmbeddedDatabaseConnection.java`** -> AI Confidence: **99.31%**
70. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/JettyWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
71. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/AbstractJmsListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.31%**
72. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/DefaultJmsListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.31%**
73. **`module/spring-boot-jms/src/main/java/org/springframework/boot/jms/autoconfigure/JmsClientConfigurations.java`** -> AI Confidence: **99.31%**
74. **`module/spring-boot-jpa/src/main/java/org/springframework/boot/jpa/EntityManagerFactoryBuilder.java`** -> AI Confidence: **99.31%**
75. **`module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/PropertiesKafkaConnectionDetails.java`** -> AI Confidence: **99.31%**
76. **`module/spring-boot-kotlinx-serialization-json/src/main/java/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonAutoConfiguration.java`** -> AI Confidence: **99.31%**
77. **`module/spring-boot-mail/src/dockerTest/java/org/springframework/boot/mail/autoconfigure/MailSenderAutoConfigurationIntegrationTests.java`** -> AI Confidence: **99.31%**
78. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/otlp/OtlpMetricsPropertiesConfigAdapter.java`** -> AI Confidence: **99.31%**
79. **`module/spring-boot-micrometer-metrics/src/testFixtures/java/org/springframework/boot/actuate/autoconfigure/metrics/export/properties/AbstractPropertiesConfigAdapterTests.java`** -> AI Confidence: **99.31%**
80. **`module/spring-boot-micrometer-observation/src/main/java/org/springframework/boot/micrometer/observation/autoconfigure/ObservationHandlerGroups.java`** -> AI Confidence: **99.31%**
81. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/autoconfigure/MustacheReactiveWebConfiguration.java`** -> AI Confidence: **99.31%**
82. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/ConnectionFactoryBuilder.java`** -> AI Confidence: **99.31%**
83. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/metrics/ConnectionPoolMetrics.java`** -> AI Confidence: **99.31%**
84. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/autoconfigure/service/PropertiesRestClientHttpServiceGroupConfigurer.java`** -> AI Confidence: **99.31%**
85. **`module/spring-boot-restdocs/src/main/java/org/springframework/boot/restdocs/test/autoconfigure/RestDocsMockMvcBuilderCustomizer.java`** -> AI Confidence: **99.31%**
86. **`module/spring-boot-security-saml2/src/main/java/org/springframework/boot/security/saml2/autoconfigure/Saml2RelyingPartyRegistrationConfiguration.java`** -> AI Confidence: **99.31%**
87. **`module/spring-boot-session-data-redis/src/main/java/org/springframework/boot/session/data/redis/autoconfigure/SessionDataRedisAutoConfiguration.java`** -> AI Confidence: **99.31%**
88. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/autoconfigure/SessionAutoConfiguration.java`** -> AI Confidence: **99.31%**
89. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/TomcatEmbeddedWebappClassLoader.java`** -> AI Confidence: **99.31%**
90. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
91. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/autoconfigure/reactive/ReactiveWebServerFactoryCustomizer.java`** -> AI Confidence: **99.31%**
92. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/DocumentRoot.java`** -> AI Confidence: **99.31%**
93. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/ServletContextInitializers.java`** -> AI Confidence: **99.31%**
94. **`module/spring-boot-webclient/src/main/java/org/springframework/boot/webclient/autoconfigure/service/PropertiesWebClientHttpServiceGroupConfigurer.java`** -> AI Confidence: **99.31%**
95. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WebSessionIdResolverAutoConfiguration.java`** -> AI Confidence: **99.31%**
96. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/ManagementErrorEndpoint.java`** -> AI Confidence: **99.31%**
97. **`cli/spring-boot-cli/src/main/executablecontent/bin/spring`** -> AI Confidence: **99.29%**
98. **`smoke-test/spring-boot-smoke-test-traditional/src/main/webapp/WEB-INF/views/home.jsp`** -> AI Confidence: **99.29%**
99. **`smoke-test/spring-boot-smoke-test-web-jsp/src/main/webapp/WEB-INF/jsp/error.jsp`** -> AI Confidence: **99.29%**
100. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithApplicationDirectory.gradle`** -> AI Confidence: **99.29%**
101. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithNetworkModeNone.gradle`** -> AI Confidence: **99.29%**
102. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests-buildsImageWithTrustBuilder.gradle`** -> AI Confidence: **99.29%**
103. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/resources/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests.gradle`** -> AI Confidence: **99.29%**
104. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/DependencyManagementPluginActionIntegrationTests.gradle`** -> AI Confidence: **99.29%**
105. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksCanOverrideDefaultParametersCompilerFlag.gradle`** -> AI Confidence: **99.29%**
106. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseParametersAndAdditionalCompilerFlags.gradle`** -> AI Confidence: **99.29%**
107. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseParametersCompilerFlagByDefault.gradle`** -> AI Confidence: **99.29%**
108. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests-javaCompileTasksUseUtf8Encoding.gradle`** -> AI Confidence: **99.29%**
109. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests-compileAotTestJavaHasTransitiveRuntimeDependenciesOnItsClasspathWhenUsingKotlin.gradle`** -> AI Confidence: **99.29%**
110. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/OnlyDependencyManagementIntegrationTests.gradle`** -> AI Confidence: **99.29%**
111. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotDoesNotHaveDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
112. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasLibraryResourcesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
113. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasTestAndDevelopmentOnlyDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
114. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/SpringBootAotPluginIntegrationTests-processTestAotHasTransitiveRuntimeDependenciesOnItsClasspath.gradle`** -> AI Confidence: **99.29%**
115. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/plugin/WarPluginActionIntegrationTests.gradle`** -> AI Confidence: **99.29%**
116. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-multiModuleCustomLayers.gradle`** -> AI Confidence: **99.29%**
117. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-multiModuleImplicitLayers.gradle`** -> AI Confidence: **99.29%**
118. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootJarIntegrationTests-reproducibleArchive.gradle`** -> AI Confidence: **99.29%**
119. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-multiModuleCustomLayers.gradle`** -> AI Confidence: **99.29%**
120. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-multiModuleImplicitLayers.gradle`** -> AI Confidence: **99.29%**
121. **`build-plugin/spring-boot-gradle-plugin/src/test/resources/org/springframework/boot/gradle/tasks/bundling/BootWarIntegrationTests-reproducibleArchive.gradle`** -> AI Confidence: **99.29%**
122. **`settings.gradle`** -> AI Confidence: **99.29%**
123. **`system-test/spring-boot-image-system-tests/src/systemTest/resources/org/springframework/boot/image/paketo/settings.gradle`** -> AI Confidence: **99.29%**
124. **`integration-test/spring-boot-loader-integration-tests/src/dockerTest/resources/conf/oracle-jdk-17/Dockerfile`** -> AI Confidence: **99.29%**
125. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImageTests.java`** -> AI Confidence: **99.24%**
126. **`build-plugin/spring-boot-maven-plugin/src/dockerTest/java/org/springframework/boot/maven/BuildImageTests.java`** -> AI Confidence: **99.24%**
127. **`build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/RunIntegrationTests.java`** -> AI Confidence: **99.24%**
128. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractRunMojo.java`** -> AI Confidence: **99.24%**
129. **`build-plugin/spring-boot-maven-plugin/src/test/java/org/springframework/boot/maven/DockerTests.java`** -> AI Confidence: **99.24%**
130. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerConfigurationMetadataTests.java`** -> AI Confidence: **99.24%**
131. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitCommand.java`** -> AI Confidence: **99.24%**
132. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ProjectGenerator.java`** -> AI Confidence: **99.24%**
133. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/ServiceCapabilitiesReportGenerator.java`** -> AI Confidence: **99.24%**
134. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/shell/CommandCompleter.java`** -> AI Confidence: **99.24%**
135. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AbstractDependsOnBeanFactoryPostProcessor.java`** -> AI Confidence: **99.24%**
136. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ImportAutoConfigurationImportSelector.java`** -> AI Confidence: **99.24%**
137. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBean.java`** -> AI Confidence: **99.24%**
138. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnBeanCondition.java`** -> AI Confidence: **99.24%**
139. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/CertificateMatcher.java`** -> AI Confidence: **99.24%**
140. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/FileWatcher.java`** -> AI Confidence: **99.24%**
141. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerCli.java`** -> AI Confidence: **99.24%**
142. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/lifecycle/DockerComposeLifecycleManager.java`** -> AI Confidence: **99.24%**
143. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/lifecycle/ServiceReadinessChecks.java`** -> AI Confidence: **99.24%**
144. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerHostTests.java`** -> AI Confidence: **99.24%**
145. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationReport.java`** -> AI Confidence: **99.24%**
146. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/AnnotationsPropertySource.java`** -> AI Confidence: **99.24%**
147. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/SpringBootTestContextBootstrapper.java`** -> AI Confidence: **99.24%**
148. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/FilterAnnotations.java`** -> AI Confidence: **99.24%**
149. **`core/spring-boot-test/src/test/java/org/springframework/boot/test/http/server/LocalTestWebServerTests.java`** -> AI Confidence: **99.24%**
150. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersStartup.java`** -> AI Confidence: **99.24%**
151. **`core/spring-boot/src/main/java/org/springframework/boot/DefaultApplicationContextFactory.java`** -> AI Confidence: **99.24%**
152. **`core/spring-boot/src/main/java/org/springframework/boot/EnvironmentConverter.java`** -> AI Confidence: **99.24%**
153. **`core/spring-boot/src/main/java/org/springframework/boot/StartupInfoLogger.java`** -> AI Confidence: **99.24%**
154. **`core/spring-boot/src/main/java/org/springframework/boot/cloud/CloudFoundryVcapEnvironmentPostProcessor.java`** -> AI Confidence: **99.24%**
155. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironment.java`** -> AI Confidence: **99.24%**
156. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentContributorPlaceholdersResolver.java`** -> AI Confidence: **99.24%**
157. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataLocationBindHandler.java`** -> AI Confidence: **99.24%**
158. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/InactiveConfigDataAccessException.java`** -> AI Confidence: **99.24%**
159. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/LocationResourceLoader.java`** -> AI Confidence: **99.24%**
160. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesBean.java`** -> AI Confidence: **99.24%**
161. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/PropertyMapper.java`** -> AI Confidence: **99.24%**
162. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/IndexedElementsBinder.java`** -> AI Confidence: **99.24%**
163. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/MapBinder.java`** -> AI Confidence: **99.24%**
164. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/validation/ValidationBindHandler.java`** -> AI Confidence: **99.24%**
165. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyName.java`** -> AI Confidence: **99.24%**
166. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/SpringConfigurationPropertySource.java`** -> AI Confidence: **99.24%**
167. **`core/spring-boot/src/main/java/org/springframework/boot/convert/ApplicationConversionService.java`** -> AI Confidence: **99.24%**
168. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BeanCurrentlyInCreationFailureAnalyzer.java`** -> AI Confidence: **99.24%**
169. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BindFailureAnalyzer.java`** -> AI Confidence: **99.24%**
170. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/NoSuchMethodFailureAnalyzer.java`** -> AI Confidence: **99.24%**
171. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzer.java`** -> AI Confidence: **99.24%**
172. **`core/spring-boot/src/main/java/org/springframework/boot/info/SslInfo.java`** -> AI Confidence: **99.24%**
173. **`core/spring-boot/src/main/java/org/springframework/boot/json/JsonWriter.java`** -> AI Confidence: **99.24%**
174. **`core/spring-boot/src/main/java/org/springframework/boot/logging/CorrelationIdFormatter.java`** -> AI Confidence: **99.24%**
175. **`core/spring-boot/src/main/java/org/springframework/boot/logging/LoggingSystemProperties.java`** -> AI Confidence: **99.24%**
176. **`core/spring-boot/src/main/java/org/springframework/boot/logging/StandardStackTracePrinter.java`** -> AI Confidence: **99.24%**
177. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/DefaultLogbackConfiguration.java`** -> AI Confidence: **99.24%**
178. **`core/spring-boot/src/main/java/org/springframework/boot/logging/structured/StructuredLoggingJsonProperties.java`** -> AI Confidence: **99.24%**
179. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/jks/JksSslStoreBundle.java`** -> AI Confidence: **99.24%**
180. **`core/spring-boot/src/main/java/org/springframework/boot/util/Instantiator.java`** -> AI Confidence: **99.24%**
181. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/FilterRegistration.java`** -> AI Confidence: **99.24%**
182. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/ServletRegistration.java`** -> AI Confidence: **99.24%**
183. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessorIntegrationTests.java`** -> AI Confidence: **99.24%**
184. **`core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/LoadedPemSslStoreTests.java`** -> AI Confidence: **99.24%**
185. **`core/spring-boot/src/test/java/org/springframework/boot/support/SpringApplicationJsonEnvironmentPostProcessorTests.java`** -> AI Confidence: **99.24%**
186. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/NestedJarFileResources.java`** -> AI Confidence: **99.24%**
187. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/SecurityInfo.java`** -> AI Confidence: **99.24%**
188. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/LaunchedClassLoader.java`** -> AI Confidence: **99.24%**
189. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/PropertiesLauncher.java`** -> AI Confidence: **99.24%**
190. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/web/PathMappedEndpoints.java`** -> AI Confidence: **99.24%**
191. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/management/PlainTextThreadDumpFormatter.java`** -> AI Confidence: **99.24%**
192. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/AbstractRabbitListenerContainerFactoryConfigurer.java`** -> AI Confidence: **99.24%**
193. **`module/spring-boot-cassandra/src/main/java/org/springframework/boot/cassandra/autoconfigure/CassandraAutoConfiguration.java`** -> AI Confidence: **99.24%**
194. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityService.java`** -> AI Confidence: **99.24%**
195. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/DataRedisAutoConfigurationJedisTests.java`** -> AI Confidence: **99.24%**
196. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/DataRedisAutoConfigurationTests.java`** -> AI Confidence: **99.24%**
197. **`module/spring-boot-data-redis/src/test/java/org/springframework/boot/data/redis/autoconfigure/PropertiesRedisConnectionDetailsTests.java`** -> AI Confidence: **99.24%**
198. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathChangedEvent.java`** -> AI Confidence: **99.24%**
199. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/filewatch/FileSystemWatcher.java`** -> AI Confidence: **99.24%**
200. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/RemoteUrlPropertyExtractorTests.java`** -> AI Confidence: **99.24%**
201. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/GrpcChannelBuilderCustomizers.java`** -> AI Confidence: **99.24%**
202. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/GrpcServerBuilderCustomizers.java`** -> AI Confidence: **99.24%**
203. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/HealthEndpointSupport.java`** -> AI Confidence: **99.24%**
204. **`module/spring-boot-health/src/test/java/org/springframework/boot/health/actuate/endpoint/SystemHealthDescriptorTests.java`** -> AI Confidence: **99.24%**
205. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JettyHttpClientBuilder.java`** -> AI Confidence: **99.24%**
206. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReactorHttpClientBuilder.java`** -> AI Confidence: **99.24%**
207. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonComponentModule.java`** -> AI Confidence: **99.24%**
208. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonComponentModule.java`** -> AI Confidence: **99.24%**
209. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DataSourceBuilderTests.java`** -> AI Confidence: **99.24%**
210. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/TomcatDataSourceConfigurationTests.java`** -> AI Confidence: **99.24%**
211. **`module/spring-boot-micrometer-observation/src/main/java/org/springframework/boot/micrometer/observation/autoconfigure/ObservationRegistryConfigurer.java`** -> AI Confidence: **99.24%**
212. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/CompositeTextMapPropagator.java`** -> AI Confidence: **99.24%**
213. **`module/spring-boot-micrometer-tracing/src/main/java/org/springframework/boot/micrometer/tracing/autoconfigure/TracingAndMeterObservationHandlerGroup.java`** -> AI Confidence: **99.24%**
214. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/autoconfigure/ConnectionFactoryConfigurations.java`** -> AI Confidence: **99.24%**
215. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/EmbeddedDatabaseConnectionTests.java`** -> AI Confidence: **99.24%**
216. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/autoconfigure/R2dbcAutoConfigurationTests.java`** -> AI Confidence: **99.24%**
217. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/autoconfigure/R2dbcAutoConfigurationWithoutConnectionPoolTests.java`** -> AI Confidence: **99.24%**
218. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/NettyWebServer.java`** -> AI Confidence: **99.24%**
219. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/GracefulShutdown.java`** -> AI Confidence: **99.24%**
220. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/SslConnectorCustomizer.java`** -> AI Confidence: **99.24%**
221. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/StaticResourceJars.java`** -> AI Confidence: **99.24%**
222. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/error/DefaultErrorWebExceptionHandler.java`** -> AI Confidence: **99.24%**
223. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/error/BasicErrorController.java`** -> AI Confidence: **99.24%**
224. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/AbstractManagementPortAndPathSampleActuatorApplicationTests.java`** -> AI Confidence: **99.24%**
225. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/MavenBuildOutputTimestamp.java`** -> AI Confidence: **99.23%**
226. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/metadata/ConfigurationMetadata.java`** -> AI Confidence: **99.23%**
227. **`configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/test/ItemMetadataAssert.java`** -> AI Confidence: **99.23%**
228. **`core/spring-boot/src/main/java/org/springframework/boot/availability/ApplicationAvailabilityBean.java`** -> AI Confidence: **99.23%**
229. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/PropertySourcesPlaceholdersResolver.java`** -> AI Confidence: **99.23%**
230. **`core/spring-boot/src/main/java/org/springframework/boot/json/BasicJsonParser.java`** -> AI Confidence: **99.23%**
231. **`module/spring-boot-actuator-autoconfigure/src/testFixtures/java/org/springframework/boot/actuate/autoconfigure/integrationtest/AbstractHealthEndpointAdditionalPathIntegrationTests.java`** -> AI Confidence: **99.23%**
232. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/DefaultRepositoryTagsProvider.java`** -> AI Confidence: **99.23%**
233. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/NettyAddress.java`** -> AI Confidence: **99.23%**
234. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/health/SimpleServingStatusMapper.java`** -> AI Confidence: **99.23%**
235. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/influx/InfluxPropertiesConfigAdapter.java`** -> AI Confidence: **99.23%**
236. **`module/spring-boot-restclient-test/src/main/java/org/springframework/boot/restclient/test/autoconfigure/RestClientTypeExcludeFilter.java`** -> AI Confidence: **99.23%**
237. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/HttpClientSettingsPropertyMapper.java`** -> AI Confidence: **99.22%**
238. **`module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/CachingConnectionFactoryConfigurer.java`** -> AI Confidence: **99.2%**
239. **`build-plugin/spring-boot-antlib/src/main/java/org/springframework/boot/ant/FindMainClass.java`** -> AI Confidence: **99.18%**
240. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/dsl/SpringBootExtension.java`** -> AI Confidence: **99.18%**
241. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/ApplicationPluginAction.java`** -> AI Confidence: **99.18%**
242. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/JavaPluginAction.java`** -> AI Confidence: **99.18%**
243. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/ResolveMainClassName.java`** -> AI Confidence: **99.18%**
244. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/SpringBootAotPlugin.java`** -> AI Confidence: **99.18%**
245. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/SpringBootPlugin.java`** -> AI Confidence: **99.18%**
246. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/aot/ProcessTestAot.java`** -> AI Confidence: **99.18%**
247. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoProperties.java`** -> AI Confidence: **99.18%**
248. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImage.java`** -> AI Confidence: **99.18%**
249. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootWar.java`** -> AI Confidence: **99.18%**
250. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/ResolvedDependencies.java`** -> AI Confidence: **99.18%**
251. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/util/VersionExtractor.java`** -> AI Confidence: **99.18%**
252. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/TaskConfigurationAvoidanceTests.java`** -> AI Confidence: **99.18%**
253. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/dsl/BuildInfoDslIntegrationTests.java`** -> AI Confidence: **99.18%**
254. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/junit/GradleCompatibilityExtension.java`** -> AI Confidence: **99.18%**
255. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/ApplicationPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
256. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/CyclonedxPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
257. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/KotlinPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
258. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/WarPluginActionIntegrationTests.java`** -> AI Confidence: **99.18%**
259. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/PomCondition.java`** -> AI Confidence: **99.18%**
260. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractDependencyFilterMojo.java`** -> AI Confidence: **99.18%**
261. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractPackagerMojo.java`** -> AI Confidence: **99.18%**
262. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/BuildInfoMojo.java`** -> AI Confidence: **99.18%**
263. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/CommandLineBuilder.java`** -> AI Confidence: **99.18%**
264. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/DependencyFilter.java`** -> AI Confidence: **99.18%**
265. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/JarTypeFilter.java`** -> AI Confidence: **99.18%**
266. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/ProcessTestAotMojo.java`** -> AI Confidence: **99.18%**
267. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/VersionExtractor.java`** -> AI Confidence: **99.18%**
268. **`build-plugin/spring-boot-maven-plugin/src/test/java/org/springframework/boot/maven/ImageTests.java`** -> AI Confidence: **99.18%**
269. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerConfigurationMetadata.java`** -> AI Confidence: **99.18%**
270. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ssl/SslContextFactory.java`** -> AI Confidence: **99.18%**
271. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/transport/DockerEngineException.java`** -> AI Confidence: **99.18%**
272. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/ImageArchive.java`** -> AI Confidence: **99.18%**
273. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/ImageConfig.java`** -> AI Confidence: **99.18%**
274. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/FilePermissions.java`** -> AI Confidence: **99.18%**
275. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/InspectedContent.java`** -> AI Confidence: **99.18%**
276. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/io/ZipFileTarArchive.java`** -> AI Confidence: **99.18%**
277. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/json/JsonStream.java`** -> AI Confidence: **99.18%**
278. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/json/MappedObject.java`** -> AI Confidence: **99.18%**
279. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/DockerApiTests.java`** -> AI Confidence: **99.18%**
280. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/transport/RemoteHttpClientTransportTests.java`** -> AI Confidence: **99.18%**
281. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/type/ImageTests.java`** -> AI Confidence: **99.18%**
282. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/encodepassword/EncodePasswordCommand.java`** -> AI Confidence: **99.18%**
283. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitializrService.java`** -> AI Confidence: **99.18%**
284. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/options/OptionHandler.java`** -> AI Confidence: **99.18%**
285. **`configuration-metadata/spring-boot-configuration-metadata/src/test/java/org/springframework/boot/configurationmetadata/ConfigurationMetadataRepositoryJsonBuilderTests.java`** -> AI Confidence: **99.18%**
286. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/MetadataCollectors.java`** -> AI Confidence: **99.18%**
287. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/MetadataStore.java`** -> AI Confidence: **99.18%**
288. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/fieldvalues/javac/JavaCompilerFieldValuesParser.java`** -> AI Confidence: **99.18%**
289. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfiguration.java`** -> AI Confidence: **99.18%**
290. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationPackage.java`** -> AI Confidence: **99.18%**
291. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationReplacements.java`** -> AI Confidence: **99.18%**
292. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigureAfter.java`** -> AI Confidence: **99.18%**
293. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigureBefore.java`** -> AI Confidence: **99.18%**
294. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/SpringBootApplication.java`** -> AI Confidence: **99.18%**
295. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnSingleCandidate.java`** -> AI Confidence: **99.18%**
296. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/FilteringSpringBootCondition.java`** -> AI Confidence: **99.18%**
297. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnResourceCondition.java`** -> AI Confidence: **99.18%**
298. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ResourceCondition.java`** -> AI Confidence: **99.18%**
299. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/context/MessageSourceAutoConfiguration.java`** -> AI Confidence: **99.18%**
300. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/logging/ConditionEvaluationReportLoggingListener.java`** -> AI Confidence: **99.18%**
301. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/BundleContentProperty.java`** -> AI Confidence: **99.18%**
302. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/task/ScheduledBeanLazyInitializationExcludeFilter.java`** -> AI Confidence: **99.18%**
303. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/template/TemplateAvailabilityProviders.java`** -> AI Confidence: **99.18%**
304. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/web/WebProperties.java`** -> AI Confidence: **99.18%**
305. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/context/ConfigurationPropertiesAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
306. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/context/PropertyPlaceholderAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
307. **`core/spring-boot-autoconfigure/src/testFixtures/java/org/springframework/boot/autoconfigure/jndi/TestableInitialContextFactory.java`** -> AI Confidence: **99.18%**
308. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DefaultDockerCompose.java`** -> AI Confidence: **99.18%**
309. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerCliCommand.java`** -> AI Confidence: **99.18%**
310. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/ProcessRunner.java`** -> AI Confidence: **99.18%**
311. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/service/connection/ConnectionNamePredicate.java`** -> AI Confidence: **99.18%**
312. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/service/connection/DockerComposeServiceConnectionsApplicationListener.java`** -> AI Confidence: **99.18%**
313. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerCliCommandTests.java`** -> AI Confidence: **99.18%**
314. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/core/DockerCliInspectResponseTests.java`** -> AI Confidence: **99.18%**
315. **`core/spring-boot-docker-compose/src/test/java/org/springframework/boot/docker/compose/lifecycle/TcpConnectServiceReadinessCheckTests.java`** -> AI Confidence: **99.18%**
316. **`core/spring-boot-docker-compose/src/testFixtures/java/org/springframework/boot/docker/compose/service/connection/test/DockerComposeTestExtension.java`** -> AI Confidence: **99.18%**
317. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationListener.java`** -> AI Confidence: **99.18%**
318. **`core/spring-boot-test-autoconfigure/src/main/java/org/springframework/boot/test/autoconfigure/TestSliceTestContextBootstrapper.java`** -> AI Confidence: **99.18%**
319. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/ImportsContextCustomizer.java`** -> AI Confidence: **99.18%**
320. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/TypeExcludeFiltersContextCustomizerFactory.java`** -> AI Confidence: **99.18%**
321. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/runner/AbstractApplicationContextRunner.java`** -> AI Confidence: **99.18%**
322. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/http/server/LocalTestWebServer.java`** -> AI Confidence: **99.18%**
323. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/json/JacksonTester.java`** -> AI Confidence: **99.18%**
324. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/json/JsonContentAssert.java`** -> AI Confidence: **99.18%**
325. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/system/OutputCapture.java`** -> AI Confidence: **99.18%**
326. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/system/OutputCaptureRule.java`** -> AI Confidence: **99.18%**
327. **`core/spring-boot-test/src/test/java/org/springframework/boot/test/web/htmlunit/UriBuilderFactoryWebClientTests.java`** -> AI Confidence: **99.18%**
328. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleBeanFactoryPostProcessor.java`** -> AI Confidence: **99.18%**
329. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnection.java`** -> AI Confidence: **99.18%**
330. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnectionContextCustomizerFactory.java`** -> AI Confidence: **99.18%**
331. **`core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersStartupTests.java`** -> AI Confidence: **99.18%**
332. **`core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/service/connection/ContainerConnectionSourceTests.java`** -> AI Confidence: **99.18%**
333. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationShutdownHook.java`** -> AI Confidence: **99.18%**
334. **`core/spring-boot/src/main/java/org/springframework/boot/builder/SpringApplicationBuilder.java`** -> AI Confidence: **99.18%**
335. **`core/spring-boot/src/main/java/org/springframework/boot/context/ConfigurationWarningsApplicationContextInitializer.java`** -> AI Confidence: **99.18%**
336. **`core/spring-boot/src/main/java/org/springframework/boot/context/annotation/ImportCandidates.java`** -> AI Confidence: **99.18%**
337. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessor.java`** -> AI Confidence: **99.18%**
338. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataProperties.java`** -> AI Confidence: **99.18%**
339. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigTreeConfigDataLocationResolver.java`** -> AI Confidence: **99.18%**
340. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/InvalidConfigDataPropertyException.java`** -> AI Confidence: **99.18%**
341. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/Profiles.java`** -> AI Confidence: **99.18%**
342. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/StandardConfigDataLoader.java`** -> AI Confidence: **99.18%**
343. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesCharSequenceToObjectConverter.java`** -> AI Confidence: **99.18%**
344. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesJsr303Validator.java`** -> AI Confidence: **99.18%**
345. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesScan.java`** -> AI Confidence: **99.18%**
346. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationPropertiesScanRegistrar.java`** -> AI Confidence: **99.18%**
347. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/ArrayBinder.java`** -> AI Confidence: **99.18%**
348. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/BindConverter.java`** -> AI Confidence: **99.18%**
349. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Bindable.java`** -> AI Confidence: **99.18%**
350. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java`** -> AI Confidence: **99.18%**
351. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/CollectionBinder.java`** -> AI Confidence: **99.18%**
352. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyNameAliases.java`** -> AI Confidence: **99.18%**
353. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/MutuallyExclusiveConfigurationPropertiesException.java`** -> AI Confidence: **99.18%**
354. **`core/spring-boot/src/main/java/org/springframework/boot/convert/CollectionToDelimitedStringConverter.java`** -> AI Confidence: **99.18%**
355. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DelimitedStringToArrayConverter.java`** -> AI Confidence: **99.18%**
356. **`core/spring-boot/src/main/java/org/springframework/boot/convert/DurationToStringConverter.java`** -> AI Confidence: **99.18%**
357. **`core/spring-boot/src/main/java/org/springframework/boot/convert/PeriodToStringConverter.java`** -> AI Confidence: **99.18%**
358. **`core/spring-boot/src/main/java/org/springframework/boot/convert/StringToDurationConverter.java`** -> AI Confidence: **99.18%**
359. **`core/spring-boot/src/main/java/org/springframework/boot/convert/StringToPeriodConverter.java`** -> AI Confidence: **99.18%**
360. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/AbstractInjectionFailureAnalyzer.java`** -> AI Confidence: **99.18%**
361. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/BindValidationFailureAnalyzer.java`** -> AI Confidence: **99.18%**
362. **`core/spring-boot/src/main/java/org/springframework/boot/diagnostics/analyzer/MutuallyExclusiveConfigurationPropertiesFailureAnalyzer.java`** -> AI Confidence: **99.18%**
363. **`core/spring-boot/src/main/java/org/springframework/boot/io/ApplicationResourceLoader.java`** -> AI Confidence: **99.18%**
364. **`core/spring-boot/src/main/java/org/springframework/boot/json/WritableJson.java`** -> AI Confidence: **99.18%**
365. **`core/spring-boot/src/main/java/org/springframework/boot/logging/DeferredLogs.java`** -> AI Confidence: **99.18%**
366. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/ColorConverter.java`** -> AI Confidence: **99.18%**
367. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/Log4j2LoggingSystemProperties.java`** -> AI Confidence: **99.18%**
368. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/SpringBootTriggeringPolicy.java`** -> AI Confidence: **99.18%**
369. **`core/spring-boot/src/main/java/org/springframework/boot/logging/log4j2/StructuredLogLayout.java`** -> AI Confidence: **99.18%**
370. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogbackConfigurator.java`** -> AI Confidence: **99.18%**
371. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/LogbackLoggingSystem.java`** -> AI Confidence: **99.18%**
372. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SpringProfileModelHandler.java`** -> AI Confidence: **99.18%**
373. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/StructuredLogEncoder.java`** -> AI Confidence: **99.18%**
374. **`core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SystemStatusListener.java`** -> AI Confidence: **99.18%**
375. **`core/spring-boot/src/main/java/org/springframework/boot/logging/structured/GraylogExtendedLogFormatProperties.java`** -> AI Confidence: **99.18%**
376. **`core/spring-boot/src/main/java/org/springframework/boot/origin/Origin.java`** -> AI Confidence: **99.18%**
377. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/SslOptions.java`** -> AI Confidence: **99.18%**
378. **`core/spring-boot/src/main/java/org/springframework/boot/ssl/pem/PemContent.java`** -> AI Confidence: **99.18%**
379. **`core/spring-boot/src/main/java/org/springframework/boot/support/EnvironmentPostProcessorApplicationListener.java`** -> AI Confidence: **99.18%**
380. **`core/spring-boot/src/main/java/org/springframework/boot/validation/MessageInterpolatorFactory.java`** -> AI Confidence: **99.18%**
381. **`core/spring-boot/src/main/java/org/springframework/boot/web/context/servlet/WebApplicationContextInitializer.java`** -> AI Confidence: **99.18%**
382. **`core/spring-boot/src/main/java/org/springframework/boot/web/error/Error.java`** -> AI Confidence: **99.18%**
383. **`core/spring-boot/src/main/java/org/springframework/boot/web/error/ErrorAttributeOptions.java`** -> AI Confidence: **99.18%**
384. **`core/spring-boot/src/main/java/org/springframework/boot/web/servlet/AbstractFilterRegistrationBean.java`** -> AI Confidence: **99.18%**
385. **`core/spring-boot/src/test/java/org/springframework/boot/ResourceBannerTests.java`** -> AI Confidence: **99.18%**
386. **`core/spring-boot/src/test/java/org/springframework/boot/context/annotation/ConfigurationsTests.java`** -> AI Confidence: **99.18%**
387. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigTreeConfigDataLocationResolverTests.java`** -> AI Confidence: **99.18%**
388. **`core/spring-boot/src/test/java/org/springframework/boot/context/config/StandardConfigDataLoaderTests.java`** -> AI Confidence: **99.18%**
389. **`core/spring-boot/src/test/java/org/springframework/boot/context/metrics/buffering/BufferingApplicationStartupTests.java`** -> AI Confidence: **99.18%**
390. **`core/spring-boot/src/test/java/org/springframework/boot/context/properties/bind/DefaultBindConstructorProviderTests.java`** -> AI Confidence: **99.18%**
391. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/BindFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
392. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/InvalidConfigurationPropertyNameFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
393. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/MissingParameterNamesFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
394. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoSuchMethodFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
395. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
396. **`core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/UnboundConfigurationPropertyFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
397. **`core/spring-boot/src/test/java/org/springframework/boot/info/SslInfoTests.java`** -> AI Confidence: **99.18%**
398. **`core/spring-boot/src/test/java/org/springframework/boot/logging/log4j2/Log4J2LoggingSystemTests.java`** -> AI Confidence: **99.18%**
399. **`core/spring-boot/src/test/java/org/springframework/boot/logging/log4j2/SpringEnvironmentLookupTests.java`** -> AI Confidence: **99.18%**
400. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackLoggingSystemTests.java`** -> AI Confidence: **99.18%**
401. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackRuntimeHintsTests.java`** -> AI Confidence: **99.18%**
402. **`core/spring-boot/src/test/java/org/springframework/boot/logging/logback/SpringBootJoranConfiguratorTests.java`** -> AI Confidence: **99.18%**
403. **`integration-test/spring-boot-actuator-integration-tests/src/test/java/org/springframework/boot/actuate/audit/AuditEventsEndpointWebIntegrationTests.java`** -> AI Confidence: **99.18%**
404. **`integration-test/spring-boot-actuator-integration-tests/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/JmxEndpointAccessIntegrationTests.java`** -> AI Confidence: **99.18%**
405. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/AbstractApplicationLauncher.java`** -> AI Confidence: **99.18%**
406. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/BootRunApplicationLauncher.java`** -> AI Confidence: **99.18%**
407. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/ExplodedApplicationLauncher.java`** -> AI Confidence: **99.18%**
408. **`integration-test/spring-boot-server-integration-tests/src/intTest/java/org/springframework/boot/context/embedded/IdeApplicationLauncher.java`** -> AI Confidence: **99.18%**
409. **`loader/spring-boot-jarmode-tools/src/main/java/org/springframework/boot/jarmode/tools/Command.java`** -> AI Confidence: **99.18%**
410. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/AbstractJarModeTests.java`** -> AI Confidence: **99.18%**
411. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/ExtractCommandTests.java`** -> AI Confidence: **99.18%**
412. **`loader/spring-boot-jarmode-tools/src/test/java/org/springframework/boot/jarmode/tools/ExtractLayersCommandTests.java`** -> AI Confidence: **99.18%**
413. **`loader/spring-boot-loader-tools/src/main/java/org/springframework/boot/loader/tools/BuildPropertiesWriter.java`** -> AI Confidence: **99.18%**
414. **`loader/spring-boot-loader-tools/src/main/java/org/springframework/boot/loader/tools/layer/CustomLayers.java`** -> AI Confidence: **99.18%**
415. **`loader/spring-boot-loader-tools/src/test/java/org/springframework/boot/loader/tools/layer/IncludeExcludeContentSelectorTests.java`** -> AI Confidence: **99.18%**
416. **`loader/spring-boot-loader-tools/src/test/java/org/springframework/boot/loader/tools/layer/LibraryContentFilterTests.java`** -> AI Confidence: **99.18%**
417. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/Archive.java`** -> AI Confidence: **99.18%**
418. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/ExplodedArchive.java`** -> AI Confidence: **99.18%**
419. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/nio/file/NestedByteChannel.java`** -> AI Confidence: **99.18%**
420. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/nio/file/NestedPath.java`** -> AI Confidence: **99.18%**
421. **`loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/zip/FileDataBlock.java`** -> AI Confidence: **99.18%**
422. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/jar/MetaInfVersionsInfoTests.java`** -> AI Confidence: **99.18%**
423. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/jar/SecurityInfoTests.java`** -> AI Confidence: **99.18%**
424. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/launch/ExplodedArchiveTests.java`** -> AI Confidence: **99.18%**
425. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/launch/JarFileArchiveTests.java`** -> AI Confidence: **99.18%**
426. **`loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/ZipContentTests.java`** -> AI Confidence: **99.18%**
427. **`module/spring-boot-activemq/src/main/java/org/springframework/boot/activemq/testcontainers/ActiveMQContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
428. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/condition/ConditionsReportEndpoint.java`** -> AI Confidence: **99.18%**
429. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/EndpointAutoConfiguration.java`** -> AI Confidence: **99.18%**
430. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/condition/ConditionalOnAvailableEndpoint.java`** -> AI Confidence: **99.18%**
431. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/condition/OnAvailableEndpointCondition.java`** -> AI Confidence: **99.18%**
432. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/expose/IncludeExcludeEndpointFilter.java`** -> AI Confidence: **99.18%**
433. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/DefaultEndpointObjectNameFactory.java`** -> AI Confidence: **99.18%**
434. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/web/server/ManagementContextConfigurationImportSelector.java`** -> AI Confidence: **99.18%**
435. **`module/spring-boot-actuator-autoconfigure/src/main/java/org/springframework/boot/actuate/autoconfigure/web/server/ManagementWebServerFactoryCustomizer.java`** -> AI Confidence: **99.18%**
436. **`module/spring-boot-actuator-autoconfigure/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/PropertiesEndpointAccessResolverTests.java`** -> AI Confidence: **99.18%**
437. **`module/spring-boot-actuator-autoconfigure/src/test/java/org/springframework/boot/actuate/autoconfigure/endpoint/jmx/DefaultEndpointObjectNameFactoryTests.java`** -> AI Confidence: **99.18%**
438. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/beans/BeansEndpoint.java`** -> AI Confidence: **99.18%**
439. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/ShutdownEndpoint.java`** -> AI Confidence: **99.18%**
440. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/Jackson2BeanSerializer.java`** -> AI Confidence: **99.18%**
441. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/context/properties/JacksonBeanSerializer.java`** -> AI Confidence: **99.18%**
442. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/DiscoveredOperationMethod.java`** -> AI Confidence: **99.18%**
443. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/DiscoveredOperationsFactory.java`** -> AI Confidence: **99.18%**
444. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/EndpointExtension.java`** -> AI Confidence: **99.18%**
445. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/invoker/cache/CachingOperationInvoker.java`** -> AI Confidence: **99.18%**
446. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/EndpointMBean.java`** -> AI Confidence: **99.18%**
447. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/Jackson2JmxOperationResponseMapper.java`** -> AI Confidence: **99.18%**
448. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/JacksonJmxOperationResponseMapper.java`** -> AI Confidence: **99.18%**
449. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/MBeanInfoFactory.java`** -> AI Confidence: **99.18%**
450. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/jmx/annotation/DiscoveredJmxOperation.java`** -> AI Confidence: **99.18%**
451. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/info/InfoPropertiesInfoContributor.java`** -> AI Confidence: **99.18%**
452. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/management/HeapDumpWebEndpoint.java`** -> AI Confidence: **99.18%**
453. **`module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/sbom/SbomEndpointWebExtension.java`** -> AI Confidence: **99.18%**
454. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/context/properties/ConfigurationPropertiesReportEndpointFilteringTests.java`** -> AI Confidence: **99.18%**
455. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/endpoint/SanitizingFunctionTests.java`** -> AI Confidence: **99.18%**
456. **`module/spring-boot-actuator/src/test/java/org/springframework/boot/actuate/sbom/SbomEndpointWebExtensionTests.java`** -> AI Confidence: **99.18%**
457. **`module/spring-boot-actuator/src/testFixtures/java/org/springframework/boot/actuate/endpoint/web/test/WebEndpointTestInvocationContextProvider.java`** -> AI Confidence: **99.18%**
458. **`module/spring-boot-artemis/src/main/java/org/springframework/boot/artemis/autoconfigure/ArtemisXAConnectionFactoryConfiguration.java`** -> AI Confidence: **99.18%**
459. **`module/spring-boot-batch-data-mongodb/src/main/java/org/springframework/boot/batch/mongodb/autoconfigure/BatchMongoSchemaInitializer.java`** -> AI Confidence: **99.18%**
460. **`module/spring-boot-batch-data-mongodb/src/test/java/org/springframework/boot/batch/mongodb/autoconfigure/BatchMongoSchemaInitializerTests.java`** -> AI Confidence: **99.18%**
461. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/actuate/endpoint/CachesEndpoint.java`** -> AI Confidence: **99.18%**
462. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/autoconfigure/CaffeineCacheConfiguration.java`** -> AI Confidence: **99.18%**
463. **`module/spring-boot-cache/src/main/java/org/springframework/boot/cache/metrics/CacheMetricsRegistrar.java`** -> AI Confidence: **99.18%**
464. **`module/spring-boot-cache/src/test/java/org/springframework/boot/cache/autoconfigure/EhCache3CacheAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
465. **`module/spring-boot-cassandra/src/main/java/org/springframework/boot/cassandra/health/CassandraDriverHealthIndicator.java`** -> AI Confidence: **99.18%**
466. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/SecurityInterceptor.java`** -> AI Confidence: **99.18%**
467. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityInterceptor.java`** -> AI Confidence: **99.18%**
468. **`module/spring-boot-cloudfoundry/src/main/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/TokenValidator.java`** -> AI Confidence: **99.18%**
469. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/reactive/SecurityServiceTests.java`** -> AI Confidence: **99.18%**
470. **`module/spring-boot-cloudfoundry/src/test/java/org/springframework/boot/cloudfoundry/autoconfigure/actuate/endpoint/servlet/SecurityServiceTests.java`** -> AI Confidence: **99.18%**
471. **`module/spring-boot-data-cassandra-test/src/main/java/org/springframework/boot/data/cassandra/test/autoconfigure/DataCassandraTest.java`** -> AI Confidence: **99.18%**
472. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/MetricsRepositoryMethodInvocationListener.java`** -> AI Confidence: **99.18%**
473. **`module/spring-boot-data-commons/src/main/java/org/springframework/boot/data/metrics/TimedAnnotations.java`** -> AI Confidence: **99.18%**
474. **`module/spring-boot-data-couchbase-test/src/main/java/org/springframework/boot/data/couchbase/test/autoconfigure/DataCouchbaseTest.java`** -> AI Confidence: **99.18%**
475. **`module/spring-boot-data-elasticsearch-test/src/main/java/org/springframework/boot/data/elasticsearch/test/autoconfigure/DataElasticsearchTest.java`** -> AI Confidence: **99.18%**
476. **`module/spring-boot-data-elasticsearch/src/test/java/org/springframework/boot/data/elasticsearch/health/DataElasticsearchReactiveHealthIndicatorTests.java`** -> AI Confidence: **99.18%**
477. **`module/spring-boot-data-jpa-test/src/main/java/org/springframework/boot/data/jpa/test/autoconfigure/DataJpaTest.java`** -> AI Confidence: **99.18%**
478. **`module/spring-boot-data-ldap-test/src/main/java/org/springframework/boot/data/ldap/test/autoconfigure/DataLdapTest.java`** -> AI Confidence: **99.18%**
479. **`module/spring-boot-data-mongodb-test/src/main/java/org/springframework/boot/data/mongodb/test/autoconfigure/DataMongoTest.java`** -> AI Confidence: **99.18%**
480. **`module/spring-boot-data-mongodb/src/main/java/org/springframework/boot/data/mongodb/autoconfigure/DataMongoConfiguration.java`** -> AI Confidence: **99.18%**
481. **`module/spring-boot-data-r2dbc-test/src/main/java/org/springframework/boot/data/r2dbc/test/autoconfigure/DataR2dbcTest.java`** -> AI Confidence: **99.18%**
482. **`module/spring-boot-data-redis-test/src/main/java/org/springframework/boot/data/redis/test/autoconfigure/DataRedisTest.java`** -> AI Confidence: **99.18%**
483. **`module/spring-boot-data-redis/src/main/java/org/springframework/boot/data/redis/health/DataRedisHealthIndicator.java`** -> AI Confidence: **99.18%**
484. **`module/spring-boot-data-redis/src/main/java/org/springframework/boot/data/redis/testcontainers/RedisContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
485. **`module/spring-boot-devtools/src/intTest/java/org/springframework/boot/devtools/tests/RemoteApplicationLauncher.java`** -> AI Confidence: **99.18%**
486. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/ConditionEvaluationDeltaLoggingListener.java`** -> AI Confidence: **99.18%**
487. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/autoconfigure/RemoteDevtoolsSecurityConfiguration.java`** -> AI Confidence: **99.18%**
488. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathDirectories.java`** -> AI Confidence: **99.18%**
489. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/classpath/ClassPathFileChangeListener.java`** -> AI Confidence: **99.18%**
490. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/remote/client/ClassPathChangeUploader.java`** -> AI Confidence: **99.18%**
491. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/remote/client/DelayedLiveReloadTrigger.java`** -> AI Confidence: **99.18%**
492. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/restart/ClassLoaderFilesResourcePatternResolver.java`** -> AI Confidence: **99.18%**
493. **`module/spring-boot-devtools/src/main/java/org/springframework/boot/devtools/restart/OnInitializedRestarterCondition.java`** -> AI Confidence: **99.18%**
494. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/livereload/ConnectionOutputStreamTests.java`** -> AI Confidence: **99.18%**
495. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/livereload/LiveReloadServerTests.java`** -> AI Confidence: **99.18%**
496. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/restart/server/DefaultSourceDirectoryUrlFilterTests.java`** -> AI Confidence: **99.18%**
497. **`module/spring-boot-devtools/src/test/java/org/springframework/boot/devtools/test/MockClientHttpRequestFactory.java`** -> AI Confidence: **99.18%**
498. **`module/spring-boot-elasticsearch/src/main/java/org/springframework/boot/elasticsearch/autoconfigure/Rest5ClientBuilderCustomizer.java`** -> AI Confidence: **99.18%**
499. **`module/spring-boot-elasticsearch/src/test/java/org/springframework/boot/elasticsearch/autoconfigure/ElasticsearchRestClientAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
500. **`module/spring-boot-flyway/src/main/java/org/springframework/boot/flyway/autoconfigure/FlywayAutoConfiguration.java`** -> AI Confidence: **99.18%**
501. **`module/spring-boot-freemarker/src/main/java/org/springframework/boot/freemarker/autoconfigure/FreeMarkerAutoConfiguration.java`** -> AI Confidence: **99.18%**
502. **`module/spring-boot-graphql-test/src/main/java/org/springframework/boot/graphql/test/autoconfigure/GraphQlTypeExcludeFilter.java`** -> AI Confidence: **99.18%**
503. **`module/spring-boot-graphql/src/main/java/org/springframework/boot/graphql/autoconfigure/DefaultGraphQlSchemaCondition.java`** -> AI Confidence: **99.18%**
504. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlQueryByExampleAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
505. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlQuerydslAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
506. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlReactiveQueryByExampleAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
507. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/data/GraphQlReactiveQuerydslAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
508. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/security/GraphQlWebFluxSecurityAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
509. **`module/spring-boot-graphql/src/test/java/org/springframework/boot/graphql/autoconfigure/security/GraphQlWebMvcSecurityAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
510. **`module/spring-boot-groovy-templates/src/test/java/org/springframework/boot/groovy/template/autoconfigure/GroovyTemplateAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
511. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/GrpcClientCodecConfiguration.java`** -> AI Confidence: **99.18%**
512. **`module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/PropertiesChannelCredentialsProvider.java`** -> AI Confidence: **99.18%**
513. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/ServerCredentials.java`** -> AI Confidence: **99.18%**
514. **`module/spring-boot-grpc-server/src/main/java/org/springframework/boot/grpc/server/autoconfigure/health/AutoConfiguredHealthCheckedGrpcComponents.java`** -> AI Confidence: **99.18%**
515. **`module/spring-boot-gson/src/test/java/org/springframework/boot/gson/autoconfigure/GsonAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
516. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/autoconfigure/HazelcastServerConfiguration.java`** -> AI Confidence: **99.18%**
517. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/autoconfigure/PropertiesHazelcastConnectionDetails.java`** -> AI Confidence: **99.18%**
518. **`module/spring-boot-hazelcast/src/main/java/org/springframework/boot/hazelcast/testcontainers/HazelcastContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
519. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/actuate/endpoint/CompositeHealthDescriptor.java`** -> AI Confidence: **99.18%**
520. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/application/AvailabilityStateHealthIndicator.java`** -> AI Confidence: **99.18%**
521. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/application/DiskSpaceHealthIndicator.java`** -> AI Confidence: **99.18%**
522. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/autoconfigure/actuate/endpoint/AvailabilityProbesHealthEndpointGroups.java`** -> AI Confidence: **99.18%**
523. **`module/spring-boot-health/src/main/java/org/springframework/boot/health/registry/AbstractRegistry.java`** -> AI Confidence: **99.18%**
524. **`module/spring-boot-hibernate/src/main/java/org/springframework/boot/hibernate/autoconfigure/HibernateProperties.java`** -> AI Confidence: **99.18%**
525. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/JettyClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
526. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReactorClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
527. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/ReflectiveComponentsClientHttpRequestFactoryBuilder.java`** -> AI Confidence: **99.18%**
528. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/imperative/ImperativeHttpClientAutoConfiguration.java`** -> AI Confidence: **99.18%**
529. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/autoconfigure/reactive/ReactiveHttpClientAutoConfiguration.java`** -> AI Confidence: **99.18%**
530. **`module/spring-boot-http-client/src/main/java/org/springframework/boot/http/client/reactive/ClientHttpConnectorBuilder.java`** -> AI Confidence: **99.18%**
531. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/AbstractClientHttpRequestFactoryBuilderTests.java`** -> AI Confidence: **99.18%**
532. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/autoconfigure/service/HttpServiceClientPropertiesTests.java`** -> AI Confidence: **99.18%**
533. **`module/spring-boot-http-client/src/test/java/org/springframework/boot/http/client/reactive/AbstractClientHttpConnectorBuilderTests.java`** -> AI Confidence: **99.18%**
534. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonComponent.java`** -> AI Confidence: **99.18%**
535. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/JacksonMixinModuleEntriesBeanRegistrationAotProcessor.java`** -> AI Confidence: **99.18%**
536. **`module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/ObjectValueDeserializer.java`** -> AI Confidence: **99.18%**
537. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonComponent.java`** -> AI Confidence: **99.18%**
538. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonMixinModuleEntriesBeanRegistrationAotProcessor.java`** -> AI Confidence: **99.18%**
539. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/JsonObjectDeserializer.java`** -> AI Confidence: **99.18%**
540. **`module/spring-boot-jackson2/src/main/java/org/springframework/boot/jackson2/autoconfigure/Jackson2AutoConfiguration.java`** -> AI Confidence: **99.18%**
541. **`module/spring-boot-jdbc/src/dockerTest/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
542. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/DatabaseDriver.java`** -> AI Confidence: **99.18%**
543. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/autoconfigure/DataSourceProperties.java`** -> AI Confidence: **99.18%**
544. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/autoconfigure/health/DataSourceHealthContributorAutoConfiguration.java`** -> AI Confidence: **99.18%**
545. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
546. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/health/DataSourceHealthIndicator.java`** -> AI Confidence: **99.18%**
547. **`module/spring-boot-jdbc/src/main/java/org/springframework/boot/jdbc/init/DataSourceScriptDatabaseInitializer.java`** -> AI Confidence: **99.18%**
548. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverClassNameTests.java`** -> AI Confidence: **99.18%**
549. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/JdbcTemplateAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
550. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/XADataSourceAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
551. **`module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/docker/compose/PostgresJdbcDockerComposeConnectionDetailsFactoryConnectionDetailsTests.java`** -> AI Confidence: **99.18%**
552. **`module/spring-boot-jersey/src/main/java/org/springframework/boot/jersey/actuate/endpoint/web/JerseyEndpointResourceFactory.java`** -> AI Confidence: **99.18%**
553. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/JettyWebServer.java`** -> AI Confidence: **99.18%**
554. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/SslServerCustomizer.java`** -> AI Confidence: **99.18%**
555. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/JettyVirtualThreadsWebServerFactoryCustomizer.java`** -> AI Confidence: **99.18%**
556. **`module/spring-boot-jetty/src/main/java/org/springframework/boot/jetty/autoconfigure/actuate/web/server/JettyAccessLogCustomizer.java`** -> AI Confidence: **99.18%**
557. **`module/spring-boot-jooq/src/main/java/org/springframework/boot/jooq/autoconfigure/DefaultExceptionTranslatorExecuteListener.java`** -> AI Confidence: **99.18%**
558. **`module/spring-boot-jooq/src/main/java/org/springframework/boot/jooq/autoconfigure/SqlDialectLookup.java`** -> AI Confidence: **99.18%**
559. **`module/spring-boot-jooq/src/test/java/org/springframework/boot/jooq/autoconfigure/JooqPropertiesTests.java`** -> AI Confidence: **99.18%**
560. **`module/spring-boot-jpa/src/main/java/org/springframework/boot/jpa/JpaDatabaseInitializerDetector.java`** -> AI Confidence: **99.18%**
561. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/KafkaAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
562. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/KafkaPropertiesTests.java`** -> AI Confidence: **99.18%**
563. **`module/spring-boot-kafka/src/test/java/org/springframework/boot/kafka/autoconfigure/metrics/KafkaMetricsAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
564. **`module/spring-boot-liquibase/src/main/java/org/springframework/boot/liquibase/actuate/endpoint/LiquibaseEndpoint.java`** -> AI Confidence: **99.18%**
565. **`module/spring-boot-liquibase/src/test/java/org/springframework/boot/liquibase/LiquibaseChangelogMissingFailureAnalyzerTests.java`** -> AI Confidence: **99.18%**
566. **`module/spring-boot-mail/src/main/java/org/springframework/boot/mail/autoconfigure/MailSenderPropertiesConfiguration.java`** -> AI Confidence: **99.18%**
567. **`module/spring-boot-micrometer-metrics/src/dockerTest/java/org/springframework/boot/micrometer/metrics/testcontainers/otlp/OpenTelemetryMetricsContainerConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
568. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/prometheus/PrometheusScrapeEndpoint.java`** -> AI Confidence: **99.18%**
569. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/ssl/SslMeterBinder.java`** -> AI Confidence: **99.18%**
570. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/startup/StartupTimeMetricsListener.java`** -> AI Confidence: **99.18%**
571. **`module/spring-boot-micrometer-tracing-opentelemetry/src/dockerTest/java/org/springframework/boot/micrometer/tracing/opentelemetry/testcontainers/otlp/OpenTelemetryTracingContainerConnectionDetailsFactoryIntegrationTests.java`** -> AI Confidence: **99.18%**
572. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/OpenTelemetryEventPublisherBeansApplicationListener.java`** -> AI Confidence: **99.18%**
573. **`module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/testcontainers/otlp/GrafanaOpenTelemetryTracingContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
574. **`module/spring-boot-micrometer-tracing/src/main/java/org/springframework/boot/micrometer/tracing/autoconfigure/prometheus/PrometheusExemplarsAutoConfiguration.java`** -> AI Confidence: **99.18%**
575. **`module/spring-boot-micrometer-tracing/src/test/java/org/springframework/boot/micrometer/tracing/autoconfigure/TracingAndMeterObservationHandlerGroupTests.java`** -> AI Confidence: **99.18%**
576. **`module/spring-boot-mongodb/src/main/java/org/springframework/boot/mongodb/autoconfigure/MongoClientFactorySupport.java`** -> AI Confidence: **99.18%**
577. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/reactive/view/MustacheView.java`** -> AI Confidence: **99.18%**
578. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/reactive/view/MustacheViewResolver.java`** -> AI Confidence: **99.18%**
579. **`module/spring-boot-mustache/src/main/java/org/springframework/boot/mustache/servlet/view/MustacheViewResolver.java`** -> AI Confidence: **99.18%**
580. **`module/spring-boot-mustache/src/test/java/org/springframework/boot/mustache/autoconfigure/MustacheAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
581. **`module/spring-boot-neo4j/src/dockerTest/java/org/springframework/boot/neo4j/autoconfigure/Neo4jAutoConfigurationIntegrationTests.java`** -> AI Confidence: **99.18%**
582. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/autoconfigure/Neo4jAutoConfiguration.java`** -> AI Confidence: **99.18%**
583. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/health/Neo4jReactiveHealthIndicator.java`** -> AI Confidence: **99.18%**
584. **`module/spring-boot-neo4j/src/main/java/org/springframework/boot/neo4j/testcontainers/DeprecatedNeo4jContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
585. **`module/spring-boot-opentelemetry/src/dockerTest/java/org/springframework/boot/opentelemetry/testcontainers/OtelCollectorOltpLoggingContainerConnectionDetailsFactoryTests.java`** -> AI Confidence: **99.18%**
586. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/autoconfigure/OpenTelemetrySdkAutoConfiguration.java`** -> AI Confidence: **99.18%**
587. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/autoconfigure/logging/otlp/OtlpLoggingConfigurations.java`** -> AI Confidence: **99.18%**
588. **`module/spring-boot-opentelemetry/src/main/java/org/springframework/boot/opentelemetry/testcontainers/GrafanaOtlpLoggingContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.18%**
589. **`module/spring-boot-opentelemetry/src/test/java/org/springframework/boot/opentelemetry/autoconfigure/OpenTelemetryResourceAttributesTests.java`** -> AI Confidence: **99.18%**
590. **`module/spring-boot-opentelemetry/src/test/java/org/springframework/boot/opentelemetry/autoconfigure/logging/otlp/OtlpLoggingAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
591. **`module/spring-boot-persistence/src/main/java/org/springframework/boot/persistence/autoconfigure/EntityScanPackages.java`** -> AI Confidence: **99.18%**
592. **`module/spring-boot-pulsar/src/test/java/org/springframework/boot/pulsar/autoconfigure/Customizers.java`** -> AI Confidence: **99.18%**
593. **`module/spring-boot-r2dbc/src/main/java/org/springframework/boot/r2dbc/OptionsCapableConnectionFactory.java`** -> AI Confidence: **99.18%**
594. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/init/R2dbcScriptDatabaseInitializerTests.java`** -> AI Confidence: **99.18%**
595. **`module/spring-boot-r2dbc/src/test/java/org/springframework/boot/r2dbc/metrics/ConnectionPoolMetricsTests.java`** -> AI Confidence: **99.18%**
596. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/CompressionCustomizer.java`** -> AI Confidence: **99.18%**
597. **`module/spring-boot-reactor-netty/src/main/java/org/springframework/boot/reactor/netty/SslServerCustomizer.java`** -> AI Confidence: **99.18%**
598. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/RestTemplateBuilder.java`** -> AI Confidence: **99.18%**
599. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/RestTemplateBuilderClientHttpRequestInitializer.java`** -> AI Confidence: **99.18%**
600. **`module/spring-boot-restclient/src/main/java/org/springframework/boot/restclient/autoconfigure/RestClientBuilderConfigurer.java`** -> AI Confidence: **99.18%**
601. **`module/spring-boot-restclient/src/test/java/org/springframework/boot/restclient/RestClientWithRestTemplateTests.java`** -> AI Confidence: **99.18%**
602. **`module/spring-boot-restdocs/src/main/java/org/springframework/boot/restdocs/test/autoconfigure/AutoConfigureRestDocs.java`** -> AI Confidence: **99.18%**
603. **`module/spring-boot-resttestclient/src/main/java/org/springframework/boot/resttestclient/TestRestTemplate.java`** -> AI Confidence: **99.18%**
604. **`module/spring-boot-resttestclient/src/main/java/org/springframework/boot/resttestclient/autoconfigure/TestRestTemplateTestAutoConfiguration.java`** -> AI Confidence: **99.18%**
605. **`module/spring-boot-rsocket/src/main/java/org/springframework/boot/rsocket/autoconfigure/RSocketServerAutoConfiguration.java`** -> AI Confidence: **99.18%**
606. **`module/spring-boot-rsocket/src/main/java/org/springframework/boot/rsocket/netty/NettyRSocketServerFactory.java`** -> AI Confidence: **99.18%**
607. **`module/spring-boot-rsocket/src/test/java/org/springframework/boot/rsocket/netty/NettyRSocketServerFactoryTests.java`** -> AI Confidence: **99.18%**
608. **`module/spring-boot-security-oauth2-authorization-server/src/main/java/org/springframework/boot/security/oauth2/server/authorization/autoconfigure/servlet/RegisteredClientsConfiguredCondition.java`** -> AI Confidence: **99.18%**
609. **`module/spring-boot-security-oauth2-resource-server/src/test/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/OAuth2ResourceServerAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
610. **`module/spring-boot-security-oauth2-resource-server/src/test/java/org/springframework/boot/security/oauth2/server/resource/autoconfigure/reactive/ReactiveOAuth2ResourceServerAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
611. **`module/spring-boot-security/src/main/java/org/springframework/boot/security/web/reactive/ApplicationContextServerWebExchangeMatcher.java`** -> AI Confidence: **99.18%**
612. **`module/spring-boot-security/src/main/java/org/springframework/boot/security/web/servlet/ApplicationContextRequestMatcher.java`** -> AI Confidence: **99.18%**
613. **`module/spring-boot-servlet/src/main/java/org/springframework/boot/servlet/actuate/web/exchanges/HttpExchangesFilter.java`** -> AI Confidence: **99.18%**
614. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/actuate/endpoint/ReactiveSessionsEndpoint.java`** -> AI Confidence: **99.18%**
615. **`module/spring-boot-session/src/main/java/org/springframework/boot/session/actuate/endpoint/SessionsEndpoint.java`** -> AI Confidence: **99.18%**
616. **`module/spring-boot-sql/src/main/java/org/springframework/boot/sql/init/AbstractScriptDatabaseInitializer.java`** -> AI Confidence: **99.18%**
617. **`module/spring-boot-sql/src/main/java/org/springframework/boot/sql/init/dependency/DatabaseInitializationDependencyConfigurer.java`** -> AI Confidence: **99.18%**
618. **`module/spring-boot-thymeleaf/src/main/java/org/springframework/boot/thymeleaf/autoconfigure/TemplateEngineConfigurations.java`** -> AI Confidence: **99.18%**
619. **`module/spring-boot-thymeleaf/src/main/java/org/springframework/boot/thymeleaf/autoconfigure/ThymeleafAutoConfiguration.java`** -> AI Confidence: **99.18%**
620. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/TomcatWebServerFactory.java`** -> AI Confidence: **99.18%**
621. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/actuate/web/server/TomcatAccessLogCustomizer.java`** -> AI Confidence: **99.18%**
622. **`module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/metrics/TomcatMetricsBinder.java`** -> AI Confidence: **99.18%**
623. **`module/spring-boot-tomcat/src/test/java/org/springframework/boot/tomcat/autoconfigure/TomcatWebServerFactoryCustomizerTests.java`** -> AI Confidence: **99.18%**
624. **`module/spring-boot-transaction/src/main/java/org/springframework/boot/transaction/jta/autoconfigure/JndiJtaConfiguration.java`** -> AI Confidence: **99.18%**
625. **`module/spring-boot-validation/src/main/java/org/springframework/boot/validation/autoconfigure/PrimaryDefaultValidatorPostProcessor.java`** -> AI Confidence: **99.18%**
626. **`module/spring-boot-validation/src/main/java/org/springframework/boot/validation/autoconfigure/ValidatorAdapter.java`** -> AI Confidence: **99.18%**
627. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/context/SpringBootTestRandomPortContextCustomizer.java`** -> AI Confidence: **99.18%**
628. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/reactive/context/ReactiveWebServerApplicationContextLocalTestWebServerProvider.java`** -> AI Confidence: **99.18%**
629. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/CookieSameSiteSupplier.java`** -> AI Confidence: **99.18%**
630. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentHandler.java`** -> AI Confidence: **99.18%**
631. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentRegisteringPostProcessor.java`** -> AI Confidence: **99.18%**
632. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentScan.java`** -> AI Confidence: **99.18%**
633. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletComponentScanRegistrar.java`** -> AI Confidence: **99.18%**
634. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletWebServerApplicationContext.java`** -> AI Confidence: **99.18%**
635. **`module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/servlet/context/ServletWebServerApplicationContextLocalTestWebServerProvider.java`** -> AI Confidence: **99.18%**
636. **`module/spring-boot-web-server/src/test/java/org/springframework/boot/web/server/WebServerSslBundleTests.java`** -> AI Confidence: **99.18%**
637. **`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/reactive/AbstractReactiveWebServerFactoryTests.java`** -> AI Confidence: **99.18%**
638. **`module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/MockServletWebServerFactory.java`** -> AI Confidence: **99.18%**
639. **`module/spring-boot-webflux-test/src/main/java/org/springframework/boot/webflux/test/autoconfigure/WebFluxTest.java`** -> AI Confidence: **99.18%**
640. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/WebFluxWebApplicationTypeDeducer.java`** -> AI Confidence: **99.18%**
641. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/AbstractWebFluxEndpointHandlerMapping.java`** -> AI Confidence: **99.18%**
642. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/AdditionalHealthEndpointPathsWebFluxHandlerMapping.java`** -> AI Confidence: **99.18%**
643. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/endpoint/web/ControllerEndpointHandlerMapping.java`** -> AI Confidence: **99.18%**
644. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/exchanges/RecordableServerHttpRequest.java`** -> AI Confidence: **99.18%**
645. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/exchanges/RecordableServerHttpResponse.java`** -> AI Confidence: **99.18%**
646. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/ResourceChainResourceHandlerRegistrationCustomizer.java`** -> AI Confidence: **99.18%**
647. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WebFluxAutoConfiguration.java`** -> AI Confidence: **99.18%**
648. **`module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/autoconfigure/WelcomePageRouterFunctionFactory.java`** -> AI Confidence: **99.18%**
649. **`module/spring-boot-webmvc-test/src/main/java/org/springframework/boot/webmvc/test/autoconfigure/SpringBootMockMvcBuilderCustomizer.java`** -> AI Confidence: **99.18%**
650. **`module/spring-boot-webmvc-test/src/main/java/org/springframework/boot/webmvc/test/autoconfigure/WebMvcTypeExcludeFilter.java`** -> AI Confidence: **99.18%**
651. **`module/spring-boot-webmvc-test/src/test/java/org/springframework/boot/webmvc/test/autoconfigure/mockmvc/WebMvcTestHtmlUnitWebClientIntegrationTests.java`** -> AI Confidence: **99.18%**
652. **`module/spring-boot-webmvc-test/src/test/java/org/springframework/boot/webmvc/test/autoconfigure/mockmvc/WebMvcTestHtmlUnitWebDriverIntegrationTests.java`** -> AI Confidence: **99.18%**
653. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/WebMvcWebApplicationTypeDeducer.java`** -> AI Confidence: **99.18%**
654. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/actuate/web/mappings/RequestMappingConditionsDescription.java`** -> AI Confidence: **99.18%**
655. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/JspTemplateAvailabilityProvider.java`** -> AI Confidence: **99.18%**
656. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/WebMvcAutoConfiguration.java`** -> AI Confidence: **99.18%**
657. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/CompositeHandlerExceptionResolver.java`** -> AI Confidence: **99.18%**
658. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/CompositeHandlerMapping.java`** -> AI Confidence: **99.18%**
659. **`module/spring-boot-webmvc/src/main/java/org/springframework/boot/webmvc/error/DefaultErrorAttributes.java`** -> AI Confidence: **99.18%**
660. **`module/spring-boot-webmvc/src/test/java/org/springframework/boot/webmvc/autoconfigure/actuate/web/WebMvcEndpointCorsIntegrationTests.java`** -> AI Confidence: **99.18%**
661. **`module/spring-boot-webservices-test/src/test/java/org/springframework/boot/webservices/test/autoconfigure/client/WebServiceClientIntegrationTests.java`** -> AI Confidence: **99.18%**
662. **`module/spring-boot-webservices/src/main/java/org/springframework/boot/webservices/client/WebServiceTemplateBuilder.java`** -> AI Confidence: **99.18%**
663. **`module/spring-boot-webservices/src/test/java/org/springframework/boot/webservices/autoconfigure/WebServicesAutoConfigurationTests.java`** -> AI Confidence: **99.18%**
664. **`smoke-test/spring-boot-smoke-test-actuator-custom-security/src/test/java/smoketest/actuator/customsecurity/ManagementServerWithCustomServletPathSampleActuatorTests.java`** -> AI Confidence: **99.18%**
665. **`smoke-test/spring-boot-smoke-test-actuator-ui/src/test/java/smoketest/actuator/ui/SampleActuatorUiApplicationPortTests.java`** -> AI Confidence: **99.18%**
666. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/ManagementAddressActuatorApplicationTests.java`** -> AI Confidence: **99.18%**
667. **`smoke-test/spring-boot-smoke-test-actuator/src/test/java/smoketest/actuator/ManagementPortSampleActuatorApplicationTests.java`** -> AI Confidence: **99.18%**
668. **`smoke-test/spring-boot-smoke-test-grpc-server-netty-shaded/src/dockerTest/java/smoketest/grpcservernettyshaded/SampleGrpcServerNettyShadedApplicationTests.java`** -> AI Confidence: **99.18%**
669. **`smoke-test/spring-boot-smoke-test-grpc-server-netty-shaded/src/main/java/smoketest/grpcservernettyshaded/HelloWorldService.java`** -> AI Confidence: **99.18%**
670. **`smoke-test/spring-boot-smoke-test-grpc-server-oauth/src/test/java/smoketest/grpcserveroauth/SampleGrpcServerOAuthApplicationTests.java`** -> AI Confidence: **99.18%**
671. **`smoke-test/spring-boot-smoke-test-grpc-server-servlet/src/main/java/smoketest/grpcserverservlet/HelloWorldService.java`** -> AI Confidence: **99.18%**
672. **`smoke-test/spring-boot-smoke-test-grpc-server/src/dockerTest/java/smoketest/grpcserver/SampleGrpcServerApplicationTests.java`** -> AI Confidence: **99.18%**
673. **`smoke-test/spring-boot-smoke-test-grpc-server/src/main/java/smoketest/grpcserver/HelloWorldService.java`** -> AI Confidence: **99.18%**
674. **`smoke-test/spring-boot-smoke-test-hateoas/src/test/java/smoketest/hateoas/SampleHateoasApplicationTests.java`** -> AI Confidence: **99.18%**
675. **`smoke-test/spring-boot-smoke-test-oauth2-authorization-server/src/test/java/smoketest/oauth2/server/SampleOAuth2AuthorizationServerApplicationTests.java`** -> AI Confidence: **99.18%**
676. **`smoke-test/spring-boot-smoke-test-property-validation/src/test/java/smoketest/propertyvalidation/SamplePropertyValidationApplicationTests.java`** -> AI Confidence: **99.18%**
677. **`smoke-test/spring-boot-smoke-test-secure-jersey/src/test/java/smoketest/secure/jersey/ManagementPortAndPathJerseyApplicationTests.java`** -> AI Confidence: **99.18%**
678. **`smoke-test/spring-boot-smoke-test-secure-jersey/src/test/java/smoketest/secure/jersey/ManagementPortCustomApplicationPathJerseyTests.java`** -> AI Confidence: **99.18%**
679. **`smoke-test/spring-boot-smoke-test-secure-webflux/src/test/java/smoketest/secure/webflux/ManagementPortSampleSecureWebFluxTests.java`** -> AI Confidence: **99.18%**
680. **`smoke-test/spring-boot-smoke-test-structured-logging-log4j2/src/test/java/smoketest/structuredlogging/log4j2/SampleLog4j2StructuredLoggingApplicationTests.java`** -> AI Confidence: **99.18%**
681. **`smoke-test/spring-boot-smoke-test-test/src/main/java/smoketest/test/service/RemoteVehicleDetailsService.java`** -> AI Confidence: **99.18%**
682. **`smoke-test/spring-boot-smoke-test-webservices/src/main/java/smoketest/webservices/endpoint/HolidayEndpoint.java`** -> AI Confidence: **99.18%**
683. **`smoke-test/spring-boot-smoke-test-webservices/src/test/java/smoketest/webservices/SampleWsApplicationTests.java`** -> AI Confidence: **99.18%**
684. **`smoke-test/spring-boot-smoke-test-websocket-jetty/src/test/java/smoketest/websocket/jetty/SampleWebSocketsApplicationTests.java`** -> AI Confidence: **99.18%**
685. **`smoke-test/spring-boot-smoke-test-websocket-tomcat/src/test/java/smoketest/websocket/tomcat/SampleWebSocketsApplicationTests.java`** -> AI Confidence: **99.18%**
686. **`system-test/spring-boot-image-system-tests/src/systemTest/java/org/springframework/boot/image/assertions/ContainerConfigAssert.java`** -> AI Confidence: **99.18%**
687. **`system-test/spring-boot-image-system-tests/src/systemTest/java/org/springframework/boot/image/assertions/ImageAssert.java`** -> AI Confidence: **99.18%**
688. **`test-support/spring-boot-docker-test-support/src/main/java/org/springframework/boot/testsupport/container/TestImage.java`** -> AI Confidence: **99.18%**
689. **`test-support/spring-boot-gradle-test-support/src/main/java/org/springframework/boot/testsupport/gradle/testkit/GradleBuild.java`** -> AI Confidence: **99.18%**
690. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/FileUtils.java`** -> AI Confidence: **99.18%**
691. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/classpath/resources/ResourcesClassLoader.java`** -> AI Confidence: **99.18%**
692. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/classpath/resources/ResourcesExtension.java`** -> AI Confidence: **99.18%**
693. **`test-support/spring-boot-test-support/src/main/java/org/springframework/boot/testsupport/system/OutputCapture.java`** -> AI Confidence: **99.18%**
694. **`buildpack/spring-boot-buildpack-platform/src/test/resources/org/springframework/boot/buildpack/platform/docker/configuration/docker-credential-test.sh`** -> AI Confidence: **99.17%**
695. **`module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/atlas/AtlasPropertiesConfigAdapter.java`** -> AI Confidence: **99.17%**
696. **`smoke-test/spring-boot-smoke-test-jetty-jsp/src/main/webapp/WEB-INF/jsp/welcome.jsp`** -> AI Confidence: **99.17%**
697. **`smoke-test/spring-boot-smoke-test-tomcat-jsp/src/main/webapp/WEB-INF/jsp/welcome.jsp`** -> AI Confidence: **99.17%**
698. **`smoke-test/spring-boot-smoke-test-web-jsp/src/main/webapp/WEB-INF/jsp/welcome.jsp`** -> AI Confidence: **99.17%**
699. **`build-plugin/spring-boot-gradle-plugin/src/dockerTest/java/org/springframework/boot/gradle/tasks/bundling/BootBuildImageIntegrationTests.java`** -> AI Confidence: **99.16%**
700. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/plugin/ProtobufPluginAction.java`** -> AI Confidence: **99.16%**
701. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootArchiveSupport.java`** -> AI Confidence: **99.16%**
702. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootJar.java`** -> AI Confidence: **99.16%**
703. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/BootZipCopyAction.java`** -> AI Confidence: **99.16%**
704. **`build-plugin/spring-boot-gradle-plugin/src/main/java/org/springframework/boot/gradle/tasks/bundling/DockerSpec.java`** -> AI Confidence: **99.16%**
705. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/plugin/JavaPluginActionIntegrationTests.java`** -> AI Confidence: **99.16%**
706. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/buildinfo/BuildInfoIntegrationTests.java`** -> AI Confidence: **99.16%**
707. **`build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/AbstractBootArchiveIntegrationTests.java`** -> AI Confidence: **99.16%**
708. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/AbstractAotMojo.java`** -> AI Confidence: **99.16%**
709. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/ArtifactsLibraries.java`** -> AI Confidence: **99.16%**
710. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/BuildImageMojo.java`** -> AI Confidence: **99.16%**
711. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/ClassPath.java`** -> AI Confidence: **99.16%**
712. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/CustomLayersProvider.java`** -> AI Confidence: **99.16%**
713. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/Image.java`** -> AI Confidence: **99.16%**
714. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/JavaProcessExecutor.java`** -> AI Confidence: **99.16%**
715. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/RepackageMojo.java`** -> AI Confidence: **99.16%**
716. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/SpringApplicationAdminClient.java`** -> AI Confidence: **99.16%**
717. **`build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/StartMojo.java`** -> AI Confidence: **99.16%**
718. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/DockerApi.java`** -> AI Confidence: **99.16%**
719. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ExportedImageTar.java`** -> AI Confidence: **99.16%**
720. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/configuration/CredentialHelper.java`** -> AI Confidence: **99.16%**
721. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ssl/KeyStoreFactory.java`** -> AI Confidence: **99.16%**
722. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ssl/PemCertificateParser.java`** -> AI Confidence: **99.16%**
723. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/ssl/PemPrivateKeyParser.java`** -> AI Confidence: **99.16%**
724. **`buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/Image.java`** -> AI Confidence: **99.16%**
725. **`buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/transport/DockerEngineExceptionTests.java`** -> AI Confidence: **99.16%**
726. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/core/HelpCommand.java`** -> AI Confidence: **99.16%**
727. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitializrServiceMetadata.java`** -> AI Confidence: **99.16%**
728. **`cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/shell/Shell.java`** -> AI Confidence: **99.16%**
729. **`cli/spring-boot-cli/src/test/java/org/springframework/boot/cli/command/init/ProjectGenerationRequestTests.java`** -> AI Confidence: **99.16%**
730. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/ConfigurationMetadataAnnotationProcessor.java`** -> AI Confidence: **99.16%**
731. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/ConfigurationPropertiesSourceResolver.java`** -> AI Confidence: **99.16%**
732. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/MetadataGenerationEnvironment.java`** -> AI Confidence: **99.16%**
733. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/ParameterPropertyDescriptor.java`** -> AI Confidence: **99.16%**
734. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/PropertyDescriptorResolver.java`** -> AI Confidence: **99.16%**
735. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/TypeElementMembers.java`** -> AI Confidence: **99.16%**
736. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/TypeUtils.java`** -> AI Confidence: **99.16%**
737. **`configuration-metadata/spring-boot-configuration-processor/src/main/java/org/springframework/boot/configurationprocessor/metadata/JsonMarshaller.java`** -> AI Confidence: **99.16%**
738. **`configuration-metadata/spring-boot-configuration-processor/src/test/java/org/springframework/boot/configurationprocessor/TestProject.java`** -> AI Confidence: **99.16%**
739. **`core/spring-boot-autoconfigure-processor/src/main/java/org/springframework/boot/autoconfigureprocessor/AutoConfigureAnnotationProcessor.java`** -> AI Confidence: **99.16%**
740. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationImportSelector.java`** -> AI Confidence: **99.16%**
741. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationMetadataLoader.java`** -> AI Confidence: **99.16%**
742. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationPackages.java`** -> AI Confidence: **99.16%**
743. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurationSorter.java`** -> AI Confidence: **99.16%**
744. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java`** -> AI Confidence: **99.16%**
745. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/AbstractNestedCondition.java`** -> AI Confidence: **99.16%**
746. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionMessage.java`** -> AI Confidence: **99.16%**
747. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/ConditionalOnBean.java`** -> AI Confidence: **99.16%**
748. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnClassCondition.java`** -> AI Confidence: **99.16%**
749. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnPropertyCondition.java`** -> AI Confidence: **99.16%**
750. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnWebApplicationCondition.java`** -> AI Confidence: **99.16%**
751. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/preinitialize/BackgroundPreinitializingApplicationListener.java`** -> AI Confidence: **99.16%**
752. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/SslPropertiesBundleRegistrar.java`** -> AI Confidence: **99.16%**
753. **`core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/web/format/WebConversionService.java`** -> AI Confidence: **99.16%**
754. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/CertificateMatchingTestSource.java`** -> AI Confidence: **99.16%**
755. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/PropertiesSslBundleTests.java`** -> AI Confidence: **99.16%**
756. **`core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/SslPropertiesBundleRegistrarTests.java`** -> AI Confidence: **99.16%**
757. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DefaultConnectionPorts.java`** -> AI Confidence: **99.16%**
758. **`core/spring-boot-docker-compose/src/main/java/org/springframework/boot/docker/compose/core/DockerComposeFile.java`** -> AI Confidence: **99.16%**
759. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationReporter.java`** -> AI Confidence: **99.16%**
760. **`core/spring-boot-properties-migrator/src/main/java/org/springframework/boot/context/properties/migrator/PropertyMigration.java`** -> AI Confidence: **99.16%**
761. **`core/spring-boot-properties-migrator/src/test/java/org/springframework/boot/context/properties/migrator/PropertiesMigrationReporterTests.java`** -> AI Confidence: **99.16%**
762. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/AnnotatedClassFinder.java`** -> AI Confidence: **99.16%**
763. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/FilteredClassLoader.java`** -> AI Confidence: **99.16%**
764. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/PropertyMappingContextCustomizer.java`** -> AI Confidence: **99.16%**
765. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/SpringBootContextLoader.java`** -> AI Confidence: **99.16%**
766. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/assertj/ApplicationContextAssertProvider.java`** -> AI Confidence: **99.16%**
767. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/assertj/AssertProviderApplicationContextInvocationHandler.java`** -> AI Confidence: **99.16%**
768. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/AnnotationCustomizableTypeExcludeFilter.java`** -> AI Confidence: **99.16%**
769. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/TypeExcludeFiltersContextCustomizer.java`** -> AI Confidence: **99.16%**
770. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/context/filter/annotation/TypeIncludes.java`** -> AI Confidence: **99.16%**
771. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/json/JsonLoader.java`** -> AI Confidence: **99.16%**
772. **`core/spring-boot-test/src/main/java/org/springframework/boot/test/util/TestPropertyValues.java`** -> AI Confidence: **99.16%**
773. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/context/ContainerFieldsImporter.java`** -> AI Confidence: **99.16%**
774. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleBeanPostProcessor.java`** -> AI Confidence: **99.16%**
775. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ConnectionDetailsRegistrar.java`** -> AI Confidence: **99.16%**
776. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ContainerConnectionDetailsFactory.java`** -> AI Confidence: **99.16%**
777. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ContainerConnectionSource.java`** -> AI Confidence: **99.16%**
778. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnectionAutoConfigurationRegistrar.java`** -> AI Confidence: **99.16%**
779. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/ServiceConnectionContextCustomizer.java`** -> AI Confidence: **99.16%**
780. **`core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/SslBundleSource.java`** -> AI Confidence: **99.16%**
781. **`core/spring-boot/src/main/java/org/springframework/boot/BeanDefinitionLoader.java`** -> AI Confidence: **99.16%**
782. **`core/spring-boot/src/main/java/org/springframework/boot/LazyInitializationBeanFactoryPostProcessor.java`** -> AI Confidence: **99.16%**
783. **`core/spring-boot/src/main/java/org/springframework/boot/ResourceBanner.java`** -> AI Confidence: **99.16%**
784. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java`** -> AI Confidence: **99.16%**
785. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationAotProcessor.java`** -> AI Confidence: **99.16%**
786. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationBannerPrinter.java`** -> AI Confidence: **99.16%**
787. **`core/spring-boot/src/main/java/org/springframework/boot/SpringApplicationRunListeners.java`** -> AI Confidence: **99.16%**
788. **`core/spring-boot/src/main/java/org/springframework/boot/bootstrap/DefaultBootstrapContext.java`** -> AI Confidence: **99.16%**
789. **`core/spring-boot/src/main/java/org/springframework/boot/context/annotation/Configurations.java`** -> AI Confidence: **99.16%**
790. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentContributor.java`** -> AI Confidence: **99.16%**
791. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataEnvironmentContributors.java`** -> AI Confidence: **99.16%**
792. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataImporter.java`** -> AI Confidence: **99.16%**
793. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataLoaders.java`** -> AI Confidence: **99.16%**
794. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataLocationResolvers.java`** -> AI Confidence: **99.16%**
795. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ConfigDataLocationRuntimeHints.java`** -> AI Confidence: **99.16%**
796. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/ProfilesValidator.java`** -> AI Confidence: **99.16%**
797. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/StandardConfigDataLocationResolver.java`** -> AI Confidence: **99.16%**
798. **`core/spring-boot/src/main/java/org/springframework/boot/context/config/StandardConfigDataResource.java`** -> AI Confidence: **99.16%**
799. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/BindMethodAttribute.java`** -> AI Confidence: **99.16%**
800. **`core/spring-boot/src/main/java/org/springframework/boot/context/properties/ConfigurationProperties.java`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/ssl/PemFileWriter.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/SslPropertiesBundleRegistrarTests.java` -> **100.0%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemContentTests.java` -> **99.9998%** Exposure
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/BundleContentPropertyTests.java` -> **99.4119%** Exposure
- `core/spring-boot/src/test/java/org/springframework/boot/ssl/pem/PemSslStoreBundleTests.java` -> **98.9215%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70425` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `core/spring-boot-testcontainers/src/dockerTest/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleOrderWithScopeIntegrationTests.java` (JAVA) -> Cumulative Risk: **757.44**
- **Archetype:** `file_cluster_4` (Distance: 10.845 IQR)
- **Magnitude:** 129.72 | **LOC:** 204 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.504%)
- **Heaviest Functions:** `remove` (Impact: 7.9), `destroy` (Impact: 5.5), `synchronized` (Impact: 4.6)

### 2. `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` (JAVA) -> Cumulative Risk: **666.41**
- **Archetype:** `file_cluster_13` (Distance: 12.338 IQR)
- **Magnitude:** 1308.76 | **LOC:** 1924 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.8528%), Concurrency (99.5026%)
- **Heaviest Functions:** `getSsl` (Impact: 21.2), `whenARequestIsActiveAfterGracefulShutdow` (Impact: 19.1), `addTestTxtFile` (Impact: 12.9)

### 3. `smoke-test/spring-boot-smoke-test-web-thymeleaf/src/main/java/smoketest/web/thymeleaf/InMemoryMessageRepository.java` (JAVA) -> Cumulative Risk: **662.91**
- **Archetype:** `file_cluster_4` (Distance: 11.274 IQR)
- **Magnitude:** 44.02 | **LOC:** 58 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.99%)
- **Heaviest Functions:** `save` (Impact: 5.4), `deleteMessage` (Impact: 2.6), `findAll` (Impact: 2.4)

### 4. `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/reactive/AbstractReactiveWebServerFactoryTests.java` (JAVA) -> Cumulative Risk: **655.67**
- **Archetype:** `file_cluster_4` (Distance: 12.131 IQR)
- **Magnitude:** 688.26 | **LOC:** 823 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.7958%), Cognitive Load (96.3435%)
- **Heaviest Functions:** `tearDown` (Impact: 12.8), `givenAnInflightRequestWhenTheServerIsSto` (Impact: 11.7), `sslWithValidAlias` (Impact: 10.4)

### 5. `smoke-test/spring-boot-smoke-test-web-groovy-templates/src/main/java/smoketest/groovytemplates/InMemoryMessageRepository.java` (JAVA) -> Cumulative Risk: **647.93**
- **Archetype:** `file_cluster_4` (Distance: 11.195 IQR)
- **Magnitude:** 39.34 | **LOC:** 53 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9921%)
- **Heaviest Functions:** `save` (Impact: 5.4), `findAll` (Impact: 2.4)

### 6. `cli/spring-boot-cli/src/main/executablecontent/bin/spring` (SHELL) -> Cumulative Risk: **645.89**
- **Archetype:** `file_cluster_12` (Distance: 14.852 IQR)
- **Magnitude:** 173.74 | **LOC:** 119 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 32.5), `Anonymous_Block` (Impact: 14.9), `__global_context__` (Impact: 8.1)

### 7. `module/spring-boot-micrometer-tracing-opentelemetry/src/main/java/org/springframework/boot/micrometer/tracing/opentelemetry/autoconfigure/OpenTelemetryEventPublisherBeansApplicationListener.java` (JAVA) -> Cumulative Risk: **639.7**
- **Archetype:** `file_cluster_13` (Distance: 10.72 IQR)
- **Magnitude:** 142.2 | **LOC:** 203 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9992%), Tech Debt (99.9988%), State Flux (80.9406%)
- **Heaviest Functions:** `onApplicationEvent` (Impact: 18.2), `getStorageDelegate` (Impact: 14.9), `synchronized` (Impact: 6.6)

### 8. `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/TomcatWebServerFactory.java` (JAVA) -> Cumulative Risk: **608.32**
- **Archetype:** `file_cluster_13` (Distance: 11.785 IQR)
- **Magnitude:** 328.04 | **LOC:** 504 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.5982%), State Flux (99.4995%)
- **Heaviest Functions:** `customizeConnector` (Impact: 21.4), `createTomcat` (Impact: 19.1), `setProtocolHandlerCustomizers` (Impact: 8.7)

### 9. `module/spring-boot-web-server/src/main/java/org/springframework/boot/web/server/MimeMappings.java` (JAVA) -> Cumulative Risk: **599.77**
- **Archetype:** `file_cluster_13` (Distance: 11.859 IQR)
- **Magnitude:** 210.7 | **LOC:** 407 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9997%), State Flux (99.7289%), Concurrency (95.4896%)
- **Heaviest Functions:** `equals` (Impact: 10.4), `equals` (Impact: 10.4), `load` (Impact: 10.1)

### 10. `core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleBeanPostProcessor.java` (JAVA) -> Cumulative Risk: **597.91**
- **Archetype:** `file_cluster_4` (Distance: 11.156 IQR)
- **Magnitude:** 135.88 | **LOC:** 200 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9955%), Verification (80.0%)
- **Heaviest Functions:** `start` (Impact: 16.0), `postProcessAfterInitialization` (Impact: 11.2), `initializeContainers` (Impact: 8.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `build-plugin/spring-boot-maven-plugin/src/dockerTest/projects/build-image-bindings/bindings/ca-certificates/test.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/condition/ConditionalOnJavaTests.java` (JAVA) | Magnitude: 40.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 45, decorators: 21, func_start: 19
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/condition/ConditionalOnMissingBeanTests.java` (JAVA) | Magnitude: 357.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 856, structural_boundaries: 421, decorators: 188, args: 172
- `module/spring-boot-cache/src/test/java/org/springframework/boot/cache/autoconfigure/CacheAutoConfigurationTests.java` (JAVA) | Magnitude: 186.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 889, structural_boundaries: 370, test: 160, args: 159
- `build-plugin/spring-boot-maven-plugin/src/main/java/org/springframework/boot/maven/FilterableDependency.java` (JAVA) | Magnitude: 43.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 36, structural_boundaries: 12, state_mutation: 12, func_start: 10
- `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/autoconfigure/TestJdbcConnectionDetails.java` (JAVA) | Magnitude: 24.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 10, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `core/spring-boot/src/main/java/org/springframework/boot/bootstrap/BootstrapContextClosedEvent.java` (JAVA) | Magnitude: 11.42 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 7, doc: 7, api: 5
- `core/spring-boot/src/main/java/org/springframework/boot/ExitCodeEvent.java` (JAVA) | Magnitude: 7.24 | Delta: **0.307 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 8, doc: 7, structural_boundaries: 5, func_start: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js` (JAVASCRIPT) | Magnitude: 1142.46 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 914, state_mutation: 635, branch: 225, structural_boundaries: 178

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` (SHELL) | Magnitude: 173.74 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 75, branch: 74, indent_tabs: 63, reflection_metaprogramming: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `module/spring-boot-pulsar/src/test/java/org/springframework/boot/pulsar/autoconfigure/Customizers.java` (JAVA) | Magnitude: 19.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 33, doc: 18, structural_boundaries: 17, generics: 15
- `module/spring-boot-webflux/src/main/java/org/springframework/boot/webflux/actuate/web/mappings/RequestMappingConditionsDescription.java` (JAVA) | Magnitude: 70.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 85, structural_boundaries: 29, args: 19, api: 14
- `module/spring-boot-elasticsearch/src/test/java/org/springframework/boot/elasticsearch/autoconfigure/ElasticsearchRestClientAutoConfigurationTests.java` (JAVA) | Magnitude: 219.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 333, structural_boundaries: 139, test: 86, args: 81
- `module/spring-boot-h2console/src/main/java/org/springframework/boot/h2console/autoconfigure/H2ConsoleAutoConfiguration.java` (JAVA) | Magnitude: 81.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 37, concurrency: 24, import: 20
- `module/spring-boot-micrometer-metrics/src/test/java/org/springframework/boot/micrometer/metrics/autoconfigure/export/simple/SimpleMetricsExportAutoConfigurationTests.java` (JAVA) | Magnitude: 22.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 58, structural_boundaries: 45, args: 14, decorators: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `module/spring-boot-amqp/src/main/java/org/springframework/boot/amqp/autoconfigure/RabbitConnectionFactoryBeanConfigurer.java` (JAVA) | Magnitude: 321.42 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 96, indent_tabs: 81, args: 54, closures: 47
- `module/spring-boot-data-rest/src/main/java/org/springframework/boot/data/rest/autoconfigure/DataRestProperties.java` (JAVA) | Magnitude: 183.58 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 99, branch: 48, args: 38, structural_boundaries: 33
- `module/spring-boot-grpc-client/src/main/java/org/springframework/boot/grpc/client/autoconfigure/ServiceConfig.java` (JAVA) | Magnitude: 1177.76 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 213, branch: 148, args: 101, closures: 81

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `core/spring-boot-test/src/main/java/org/springframework/boot/test/context/FilteredClassLoader.java` (JAVA) | Magnitude: 124.18 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 128, structural_boundaries: 50, branch: 32, generics: 24
- `module/spring-boot-micrometer-metrics/src/main/java/org/springframework/boot/micrometer/metrics/actuate/endpoint/MetricsEndpoint.java` (JAVA) | Magnitude: 138.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 166, structural_boundaries: 66, generics: 44, args: 42
- `module/spring-boot-actuator/src/main/java/org/springframework/boot/actuate/endpoint/annotation/EndpointDiscoverer.java` (JAVA) | Magnitude: 283.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 352, structural_boundaries: 123, generics: 78, branch: 73
- `smoke-test/spring-boot-smoke-test-data-r2dbc-flyway/src/main/java/smoketest/data/r2dbc/CityRepository.java` (JAVA) | Magnitude: 20.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 2, generics: 2, import: 2
- `smoke-test/spring-boot-smoke-test-data-r2dbc-liquibase/src/main/java/smoketest/data/r2dbc/CityRepository.java` (JAVA) | Magnitude: 20.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, concurrency: 2, generics: 2, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleBeanPostProcessor.java` (JAVA) | Magnitude: 135.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 114, structural_boundaries: 57, concurrency: 36, branch: 26
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/net/protocol/jar/UrlJarFiles.java` (JAVA) | Magnitude: 110.0 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 91, doc: 39, structural_boundaries: 36, state_mutation: 23
- `core/spring-boot-testcontainers/src/dockerTest/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleOrderWithScopeIntegrationTests.java` (JAVA) | Magnitude: 129.72 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 103, structural_boundaries: 73, concurrency: 42, import: 31
- `module/spring-boot-health/src/test/java/org/springframework/boot/health/contributor/MapCompositeTests.java` (JAVA) | Magnitude: 82.66 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 94, structural_boundaries: 31, test: 27, args: 26
- `loader/spring-boot-loader/src/test/java/org/springframework/boot/loader/zip/DataBlockTests.java` (JAVA) | Magnitude: 38.92 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 34, indent_tabs: 29, concurrency: 18, import: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/CredentialTests.java` (JAVA) | Magnitude: 11.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 19, test: 15, branch: 9
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/logging/ConditionEvaluationReportLogger.java` (JAVA) | Magnitude: 36.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 14, branch: 10, func_start: 6
- `module/spring-boot-web-server/src/test/java/org/springframework/boot/web/server/reactive/context/AnnotationConfigReactiveWebServerApplicationContextTests.java` (JAVA) | Magnitude: 54.8 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 61, func_start: 20, decorators: 17
- `smoke-test/spring-boot-smoke-test-jersey/src/main/java/smoketest/jersey/JerseyConfig.java` (JAVA) | Magnitude: 5.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, indent_tabs: 4, func_start: 3, api: 3
- `smoke-test/spring-boot-smoke-test-secure-jersey/src/main/java/smoketest/secure/jersey/JerseyConfig.java` (JAVA) | Magnitude: 5.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
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

- `module/spring-boot-jackson/src/main/java/org/springframework/boot/jackson/autoconfigure/JacksonAutoConfiguration.java` -> Churn: **56.32%** | Cog Load: 17.4481% | Debt: 99.6935%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1308.76
- `core/spring-boot/src/test/java/org/springframework/boot/diagnostics/analyzer/NoUniqueBeanDefinitionFailureAnalyzerTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1199.01
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1119.72
- `core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessorIntegrationTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 660.88
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationPropertyName.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 601.26

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

- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/util/Log.java` -> **Severity: 862.637** (Blast Radius: 12.495 * Doc Risk: 69.0386%)
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -> **Severity: 333.253** (Blast Radius: 4.873 * Doc Risk: 68.3876%)
- `buildpack/spring-boot-buildpack-platform/src/main/java/org/springframework/boot/buildpack/platform/docker/type/Manifest.java` -> **Severity: 260.665** (Blast Radius: 2.729 * Doc Risk: 95.5166%)
- `module/spring-boot-health/src/main/java/org/springframework/boot/health/contributor/Status.java` -> **Severity: 229.1** (Blast Radius: 2.291 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/source/ConfigurationProperty.java` -> **Severity: 207.0** (Blast Radius: 2.07 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
