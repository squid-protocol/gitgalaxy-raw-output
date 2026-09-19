# ARCHITECTURAL_BRIEF: spring-boot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spring-projects/spring-boot` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 8861 analyzed artifact(s), 491051 LOC.
- **Load-bearing artifact:** `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -- 408 in-repo importer(s) depend on it. Changes here propagate furthest.
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
| Total Artifacts | 11421 |
| Analyzed Artifacts (Scanned) | 8861 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2560 |
| Total LOC | 491051 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.6% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6677 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0796 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3753 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 423 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 7713 | 468394 | 87.0% |
| PLAINTEXT | 260 | 66 | 2.9% |
| XML | 252 | 0 | 2.8% |
| GROOVY | 235 | 3881 | 2.7% |
| JSON | 195 | 13166 | 2.2% |
| YAML | 84 | 1173 | 0.9% |
| HTML | 49 | 1280 | 0.6% |
| SQLITE | 23 | 331 | 0.3% |
| KOTLIN | 18 | 1133 | 0.2% |
| MARKDOWN | 9 | 0 | 0.1% |
| PROTO | 8 | 107 | 0.1% |
| SHELL | 4 | 159 | 0.0% |
| BATCH | 3 | 160 | 0.0% |
| RUBY | 3 | 210 | 0.0% |
| CSS | 3 | 9 | 0.0% |
| DOCKERFILE | 1 | 9 | 0.0% |
| JAVASCRIPT | 1 | 973 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.135`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.13; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 26%, Declarative / Non-Code 22%, Encapsulated Accessors Files 18%, State Mutators Files 7%, Large Core Modules (3) 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8592 | 97.0% |
| Unknown | 63 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 203 | 2.3% |
| Static: Minified & Vendor Opaque Mass | 3 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2560*

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 31.3 | 29.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 93.3 | 8.9 | 1.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 12.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 13.6 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.0 | 1.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 76.3 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.2 | 71.4 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1744 | 796 | 0 | `module/spring-boot-jetty/src/test/java/org/springframework/boot/jetty/servlet/JettyServletWebServerFactoryTests.java` |
| cleanup | 541 | 312 | 0 | `core/spring-boot-testcontainers/src/test/java/org/springframework/boot/testcontainers/lifecycle/TestcontainersLifecycleApplicationContextInitializerTests.java` |
| guards | 37420 | 4868 | 11 | `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` |
| danger | 19148 | 3274 | 6 | `core/spring-boot/src/test/java/org/springframework/boot/logging/logback/LogbackLoggingSystemTests.java` |
| concurrency | 4539 | 1186 | 2 | `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` |
| connectivity | 26788 | 4975 | 7 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| io | 7049 | 1014 | 2 | `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 189 | 38 | 0 | `module/spring-boot-amqp/src/test/java/org/springframework/boot/amqp/autoconfigure/RabbitAutoConfigurationTests.java` |
| time | 2763 | 545 | 0 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| serialization | 387 | 92 | 0 | `module/spring-boot-jackson2/src/test/java/org/springframework/boot/jackson2/autoconfigure/Jackson2AutoConfigurationTests.java` |
| regex | 160 | 95 | 0 | `module/spring-boot-devtools/src/main/resources/org/springframework/boot/devtools/livereload/livereload.js` |
| events | 1706 | 466 | 0 | `core/spring-boot/src/test/java/org/springframework/boot/SpringApplicationTests.java` |
| tests | 51894 | 2673 | 16 | `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` |
| docs | 15721 | 6811 | 3 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| debt | 1303 | 419 | 0 | `module/spring-boot-kafka/src/main/java/org/springframework/boot/kafka/autoconfigure/KafkaProperties.java` |
| mutation | 66078 | 5165 | 19 | `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` |
| dead_code | 25344 | 4631 | 7 | `core/spring-boot-test/src/test/java/org/springframework/boot/test/json/JsonContentAssertTests.java` |
| credential | 154 | 26 | 0 | `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/ssl/PemFileWriter.java` |
| threat | 1166 | 436 | 0 | `module/spring-boot-kotlinx-serialization-json/src/test/kotlin/org/springframework/boot/kotlinx/serialization/json/autoconfigure/KotlinxSerializationJsonAutoConfigurationTests.kt` |
| ml_ai | 126 | 58 | 0 | `module/spring-boot-jackson/src/test/java/org/springframework/boot/jackson/ObjectValueDeserializerTests.java` |
| ui | 187 | 45 | 0 | `core/spring-boot/src/main/java/org/springframework/boot/logging/logback/SpringBootJoranConfigurator.java` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `core/spring-boot-autoconfigure/src/test/java/org/springframework/boot/autoconfigure/ssl/FileWatcherTests.java` (Hits: 96)
- `build-plugin/spring-boot-maven-plugin/src/intTest/java/org/springframework/boot/maven/JarIntegrationTests.java` (Hits: 84)
- `build-plugin/spring-boot-gradle-plugin/src/test/java/org/springframework/boot/gradle/tasks/bundling/AbstractBootArchiveTests.java` (Hits: 64)

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

- `getAuthHeaderWhenAuthForDockerDomain` **(Annotated & Test Methods)** (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> Impact: **131.5** | LOC: 367
- `loadWhenBindingClasspathPatternToResourceArrayShouldBindMultipleValues` **(C Struct Operations)** (@ `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java`) -> Impact: **125.7** | LOC: 2074
- `getAuthHeaderWhenAuthForLegacyDockerDomain` **(Annotated & Test Methods)** (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> Impact: **115.7** | LOC: 334
- `testMultiBaseDn` **(Compute Cores)** (@ `module/spring-boot-ldap/src/test/java/org/springframework/boot/ldap/autoconfigure/embedded/EmbeddedLdapAutoConfigurationTests.java`) -> Impact: **112.3** | LOC: 126
- `getAuthHeaderWhenAuthForCustomDomainWithLegacyFormat` **(Stateful Encapsulated Methods)** (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> Impact: **100.8** | LOC: 290
- `withWsdlBeans` **(Compute Cores)** (@ `module/spring-boot-webservices/src/test/java/org/springframework/boot/webservices/autoconfigure/WebServicesAutoConfigurationTests.java`) -> Impact: **93.8** | LOC: 65
- `getAuthHeaderWhenUsingHelperFromCredsStore` **(Stateful Encapsulated Methods)** (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> Impact: **87.4** | LOC: 248
- `getAuthHeaderWhenUsingHelperFromCredsStoreAndUseEmailFromAuth` **(Stateful Encapsulated Methods)** (@ `buildpack/spring-boot-buildpack-platform/src/test/java/org/springframework/boot/buildpack/platform/docker/configuration/DockerRegistryConfigAuthenticationTests.java`) -> Impact: **68.9** | LOC: 218
- `databaseJdbcUrlLookups` **(Compute Cores)** (@ `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DatabaseDriverTests.java`) -> Impact: **66.8** | LOC: 36
- `SslBundleSource` **(Stateful Encapsulated Methods)** (@ `core/spring-boot-testcontainers/src/main/java/org/springframework/boot/testcontainers/service/connection/SslBundleSource.java`) -> Impact: **61.5** | LOC: 104
  * *Intent:* /** * {@link SslBundle} source created from annotations. Used as a cache key and as a * {@link SslBundle} factory. * * @param ssl the {@link Ssl @Ssl}...

*Function archetypes referenced above:*
  * **Annotated & Test Methods**: n/a
  * **C Struct Operations**: operates on C structs and pointers (data-structure logic)
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `module/spring-boot-mail/src/dockerTest/resources/org/springframework/boot/mail/autoconfigure/ssl` | 6 | 30000.0 | 0.0% | 0.0% |
| `module/spring-boot-elasticsearch/src/dockerTest/resources/org/springframework/boot/elasticsearch/docker/compose` | 7 | 25030.9 | 0.8% | 0.0% |
| `module/spring-boot-data-redis/src/dockerTest/resources/org/springframework/boot/data/redis/docker/compose` | 7 | 25028.02 | 0.0% | 0.0% |
| `module/spring-boot-amqp/src/dockerTest/resources/org/springframework/boot/amqp` | 5 | 25000.0 | 0.0% | 0.0% |
| `module/spring-boot-cassandra/src/dockerTest/resources/org/springframework/boot/cassandra/docker/compose` | 6 | 20030.92 | 0.0% | 0.0% |
| `module/spring-boot-mongodb/src/dockerTest/resources/org/springframework/boot/mongodb/docker/compose` | 6 | 20030.24 | 0.0% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/reactive` | 4 | 20000.0 | 0.0% | 0.0% |
| `module/spring-boot-web-server/src/testFixtures/resources/org/springframework/boot/web/server/servlet` | 4 | 20000.0 | 0.0% | 0.0% |
| `smoke-test/spring-boot-smoke-test-data-cassandra/src/dockerTest/resources/ssl` | 4 | 15017.46 | 0.0% | 2.74% |
| `smoke-test/spring-boot-smoke-test-kafka/src/dockerTest/resources/ssl` | 3 | 15000.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `configuration-metadata/spring-boot-configuration-metadata/src/main/java/org/springframework/boot/configurationmetadata/ConfigurationMetadataSource.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/context/MessageSourceProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/info/ProjectInfoProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/JksSslBundleProperties.java` -> **100.0%** Exposure
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/ssl/PemSslBundleProperties.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `cli/spring-boot-cli/src/main/executablecontent/bin/spring` -> **100.0%** Exposure
- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/command/init/InitCommand.java` -> **100.0%** Exposure
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/jar/ZipInflaterInputStream.java` -> **100.0%** Exposure
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/launch/SystemPropertyUtils.java` -> **100.0%** Exposure
- `loader/spring-boot-loader/src/main/java/org/springframework/boot/loader/net/util/UrlDecoder.java` -> **100.0%** Exposure
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
- **Binary Anomalies (X-Ray):** `17` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `70425` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `build-plugin/spring-boot-maven-plugin/src/dockerTest/projects/build-image-bindings/bindings/ca-certificates/test.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
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

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `module/spring-boot-web-server/src/testFixtures/java/org/springframework/boot/web/server/servlet/AbstractServletWebServerFactoryTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 1001.26
- `core/spring-boot/src/test/java/org/springframework/boot/context/config/ConfigDataEnvironmentPostProcessorIntegrationTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 694.48
- `core/spring-boot/src/test/java/org/springframework/boot/context/properties/ConfigurationPropertiesTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 636.94
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/condition/OnBeanCondition.java` -> **Andy Wilkinson** (100.0% isolated ownership) | Magnitude: 457.42
- `module/spring-boot-jdbc/src/test/java/org/springframework/boot/jdbc/DataSourceBuilderTests.java` -> **Moritz Halbritter** (100.0% isolated ownership) | Magnitude: 450.4

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 98.1645%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 77.0969%)
- `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/autoconfigure/servlet/TomcatServletWebServerAutoConfiguration.java` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 84.1282%)
- `module/spring-boot-tomcat/src/main/java/org/springframework/boot/tomcat/servlet/TomcatServletWebServerFactory.java` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.4231%)
- `core/spring-boot-test/src/main/java/org/springframework/boot/test/context/SpringBootTest.java` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 9.756%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/util/Log.java` -> **Severity: 5.963** (Embedded: 0.0795 * Error Risk: 74.9724%)
- `core/spring-boot/src/main/java/org/springframework/boot/SpringApplication.java` -> **Severity: 3.708** (Embedded: 0.043 * Error Risk: 86.1412%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/properties/bind/Binder.java` -> **Severity: 3.627** (Embedded: 0.0382 * Error Risk: 94.8262%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/annotation/ImportCandidates.java` -> **Severity: 3.433** (Embedded: 0.0474 * Error Risk: 72.4063%)
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -> **Severity: 3.377** (Embedded: 0.046 * Error Risk: 73.33%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `cli/spring-boot-cli/src/main/java/org/springframework/boot/cli/util/Log.java` -> **Severity: 999.6** (Blast Radius: 12.495 * Doc Risk: 80.0%)
- `core/spring-boot-autoconfigure/src/main/java/org/springframework/boot/autoconfigure/AutoConfigurations.java` -> **Severity: 487.3** (Blast Radius: 4.873 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/annotation/ImportCandidates.java` -> **Severity: 417.188** (Blast Radius: 6.675 * Doc Risk: 62.5%)
- `core/spring-boot/src/main/java/org/springframework/boot/context/TypeExcludeFilter.java` -> **Severity: 329.0** (Blast Radius: 3.29 * Doc Risk: 100.0%)
- `core/spring-boot/src/main/java/org/springframework/boot/ssl/SslBundle.java` -> **Severity: 264.31** (Blast Radius: 4.552 * Doc Risk: 58.0645%)

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
