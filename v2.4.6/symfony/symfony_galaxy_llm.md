# ARCHITECTURAL_BRIEF: symfony
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/symfony` |
| **Timestamp** | `2026-08-03T19:33:41.766670+00:00` |
| **Scan Duration** | `44.21s` |
| **Git Branch** | `8.1` |
| **Git Commit** | `d75aa6cb9200149510699b90cb57e6e9be1408f9` |
| **Git Remote** | `https://github.com/symfony/symfony.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10543 malicious artifacts.

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
| Total Artifacts | 14058 |
| Analyzed Artifacts (Scanned) | 12982 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1076 |
| Total LOC | 1629638 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.3% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0978 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 688 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 10519 | 1588444 | 81.0% |
| YAML | 795 | 12547 | 6.1% |
| MARKDOWN | 639 | 0 | 4.9% |
| JSON | 396 | 15064 | 3.1% |
| PLAINTEXT | 300 | 0 | 2.3% |
| XML | 186 | 0 | 1.4% |
| HTML | 102 | 10831 | 0.8% |
| CSS | 18 | 2112 | 0.1% |
| JAVASCRIPT | 15 | 394 | 0.1% |
| SHELL | 6 | 180 | 0.0% |
| CSV | 3 | 6 | 0.0% |
| MAKEFILE | 2 | 39 | 0.0% |
| TYPESCRIPT | 1 | 21 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.346`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7153 | 55.1% |
| file_cluster_13 | 4284 | 33.0% |
| file_cluster_4 | 222 | 1.7% |
| file_cluster_9 | 187 | 1.4% |
| file_cluster_0 | 120 | 0.9% |
| file_cluster_11 | 22 | 0.2% |
| file_cluster_17 | 20 | 0.2% |
| file_cluster_2 | 18 | 0.1% |
| file_cluster_6 | 9 | 0.1% |
| file_cluster_7 | 5 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_1 | 1 | 0.0% |
| file_cluster_12 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 939 | 7.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1076*

**Composition by Extension & Reason:**
- `no_extension`: 389x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Unsupported Format (.undeterminable), 5x Excluded (Binary Format Detected)
- `.xlf`: 139x Unsupported Format (.xlf)
- `.phpt`: 82x Unsupported Format (.phpt)
- `.php`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 8 exceeds 500 chars), 2x Excluded (Binary Format Detected)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.gif`: 15x Excluded (Explicitly Denied Extension: '.gif')
- `.expected`: 15x Unsupported Format (.expected)
- `.ini`: 10x Unsupported Format (.ini), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.res`: 11x Excluded (Binary Format Detected)
- `.dot`: 9x Unsupported Format (.dot)
- `.po`: 8x Unsupported Format (.po)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.puml`: 7x Unsupported Format (.puml)
- `.dat`: 5x Unsupported Format (.dat), 1x Excluded (Binary Format Detected)
- `.mp4`: 6x Excluded (Explicitly Denied Extension: '.mp4')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 22.7 | 9.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 11.8 | 4.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.3 | 4.0 | 3.8 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.3 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 38.8 | 1.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 28.7 | 4.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 45.5 | 10.7 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 4.9 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 23.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Symfony/Component/Mime/Tests/Header/ParameterizedHeaderTest.php` (Hits: 74)
- `src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php` (Hits: 54)
- `src/Symfony/Component/Dotenv/Tests/DotenvTest.php` (Hits: 45)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Request.php** (`src/Symfony/Component/HttpFoundation/Request.php`) — 504 inbound connections
2. **ContainerBuilder.php** (`src/Symfony/Component/DependencyInjection/ContainerBuilder.php`) — 423 inbound connections
3. **Response.php** (`src/Symfony/Component/HttpFoundation/Response.php`) — 284 inbound connections
4. **HttpClientInterface.php** (`src/Symfony/Contracts/HttpClient/HttpClientInterface.php`) — 282 inbound connections
5. **ContainerInterface.php** (`src/Symfony/Component/DependencyInjection/ContainerInterface.php`) — 261 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ResourceBundleTestCase.php** (`src/Symfony/Component/Intl/Tests/ResourceBundleTestCase.php`) — 712 outbound dependencies
2. **FrameworkExtension.php** (`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) — 252 outbound dependencies
3. **InlineTest.php** (`src/Symfony/Component/Yaml/Tests/InlineTest.php`) — 156 outbound dependencies
4. **IbanValidator.php** (`src/Symfony/Component/Validator/Constraints/IbanValidator.php`) — 135 outbound dependencies
5. **ArgvInputTest.php** (`src/Symfony/Component/Console/Tests/Input/ArgvInputTest.php`) — 125 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `__construct` (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> Impact: **6720.8** | LOC: 1136
  * *Intent:* /** * Autoloader checking if the class is really defined in the file found. * * The ClassLoader will wrap all registered autoloaders * and will throw ...
- `parseDefinition` (@ `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`) -> Impact: **3373.0** | LOC: 416
- `getEnv` (@ `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`) -> Impact: **2017.5** | LOC: 311
- `load` (@ `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) -> Impact: **1531.1** | LOC: 554
- `evaluateBracket` (@ `src/Symfony/Component/JsonPath/JsonCrawler.php`) -> Impact: **1457.4** | LOC: 293
- `createConnection` (@ `src/Symfony/Component/Cache/Traits/RedisTrait.php`) -> Impact: **1197.8** | LOC: 435
- `doParse` (@ `src/Symfony/Component/Yaml/Parser.php`) -> Impact: **1117.7** | LOC: 409
  * *Intent:* /** * Parses a YAML string to a PHP value. * * @param string $value A YAML string * @param int-mask-of<Yaml::PARSE_*> $flags A bit field of Yaml::PARS...
- `stop` (@ `src/Symfony/Component/Process/Process.php`) -> Impact: **1114.9** | LOC: 474
- `createService` (@ `src/Symfony/Component/DependencyInjection/ContainerBuilder.php`) -> Impact: **1066.3** | LOC: 163
- `doDump` (@ `src/Symfony/Component/Yaml/Dumper.php`) -> Impact: **1015.3** | LOC: 74

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `getConcatValueFromNode` (@ `src/Symfony/Bridge/Twig/NodeVisitor/TranslationNodeVisitor.php`) -> **O(2^N) [Recursive]**
- `setUp` (@ `src/Symfony/Bridge/Twig/Tests/Extension/FormExtensionFieldHelpersTest.php`) -> **O(2^N) [Recursive]**
- `registerCommands` (@ `src/Symfony/Bundle/FrameworkBundle/Console/Application.php`) -> **O(2^N) [Recursive]**
- `load` (@ `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) -> **O(2^N) [Recursive]**
- `load` (@ `src/Symfony/Bundle/TwigBundle/DependencyInjection/TwigExtension.php`) -> **O(2^N) [Recursive]**
- `compute` (@ `src/Symfony/Component/Cache/LockRegistry.php`) -> **O(2^N) [Recursive]**
- `marshall` (@ `src/Symfony/Component/Cache/Marshaller/TagAwareMarshaller.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * A marshaller optimized for data structures generated by AbstractTagAwareAdapter. *
- `writeNode` (@ `src/Symfony/Component/Config/Definition/Dumper/YamlReferenceDumper.php`) -> **O(2^N) [Recursive]**
- `loadFiles` (@ `src/Symfony/Component/Config/Resource/ReflectionClassResource.php`) -> **O(2^N) [Recursive]**
- `convertDomElementToArray` (@ `src/Symfony/Component/Config/Util/XmlUtils.php`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `__construct` (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> DB Complexity: **260**
  * *Intent:* /** * Autoloader checking if the class is really defined in the file found. * * The ClassLoader will wrap all registered autoloaders * and will throw ...
- `provideSorting` (@ `src/Symfony/Component/Scheduler/Tests/Command/DebugCommandTest.php`) -> DB Complexity: **186**
  * *Intent:* ;
- `provideCurlRequests` (@ `src/Symfony/Component/HttpClient/Tests/DataCollector/HttpClientDataCollectorTest.php`) -> DB Complexity: **142**
- `testExecuteWithSchedule` (@ `src/Symfony/Component/Scheduler/Tests/Command/DebugCommandTest.php`) -> DB Complexity: **118**
- `testParallelBars` (@ `src/Symfony/Component/Console/Tests/Helper/ProgressBarTest.php`) -> DB Complexity: **103**
- `doClone` (@ `src/Symfony/Component/VarDumper/Cloner/VarCloner.php`) -> DB Complexity: **97**
  * *Intent:* /* * This file is part of the Symfony package. * * (c) Fabien Potencier <fabien@symfony.com> * * For the full copyright and license information, pleas...
- `testOverwriteMultipleProgressBarsWithSec` (@ `src/Symfony/Component/Console/Tests/Helper/ProgressBarTest.php`) -> DB Complexity: **84**
- `setUpBeforeClass` (@ `src/Symfony/Component/Notifier/Tests/Exception/UnsupportedSchemeExceptionTest.php`) -> DB Complexity: **81**
- `stop` (@ `src/Symfony/Component/Process/Process.php`) -> DB Complexity: **78**
- `doSave` (@ `src/Symfony/Component/Cache/Adapter/PdoAdapter.php`) -> DB Complexity: **76**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Symfony/Component/Validator/Constraints` | 152 | 22660.67 | 37.04% | 0.49% |
| `src/Symfony/Component/DependencyInjection/Compiler` | 57 | 17728.28 | 60.14% | 10.74% |
| `src/Symfony/Component/Emoji/Resources/data` | 174 | 14335.5 | 5.28% | 1.24% |
| `src/Symfony/Component/Cache/Traits` | 18 | 12536.88 | 38.69% | 11.04% |
| `src/Symfony/Component/DependencyInjection/Dumper` | 7 | 11963.54 | 60.8% | 14.29% |
| `src/Symfony/Component/Cache/Adapter` | 24 | 10745.3 | 60.73% | 3.01% |
| `src/Symfony/Component/HttpFoundation` | 29 | 9909.94 | 31.5% | 4.16% |
| `src/Symfony/Component/HttpClient` | 24 | 9325.26 | 44.69% | 4.12% |
| `src/Symfony/Component/ErrorHandler` | 9 | 9042.2 | 23.72% | 1.19% |
| `src/Symfony/Component/Validator/Tests/Constraints` | 156 | 8453.9 | 16.03% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/Symfony/Bridge/Doctrine/DataCollector/ObjectParameter.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/Security/User/UserLoaderInterface.php` -> **100.0%** Exposure
- `src/Symfony/Component/Config/Loader/GlobFileLoader.php` -> **100.0%** Exposure
- `src/Symfony/Component/Console/Helper/TableRows.php` -> **100.0%** Exposure
- `src/Symfony/Component/CssSelector/Node/RelationNode.php` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `link` -> **100.0%** Exposure
- `phpunit` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/Attribute/MapEntity.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Symfony/Component/OptionsResolver/Tests/OptionsResolverTest.php` -> **162** Orphaned Functions | **4** Duplicates
- `src/Symfony/Bridge/Twig/Tests/Extension/AbstractLayoutTestCase.php` -> **148** Orphaned Functions | **2** Duplicates
- `src/Symfony/Component/Form/Tests/Extension/Core/Type/ChoiceTypeTest.php` -> **115** Orphaned Functions | **17** Duplicates
- `src/Symfony/Component/DependencyInjection/Tests/ContainerBuilderTest.php` -> **127** Orphaned Functions | **4** Duplicates
- `src/Symfony/Bridge/Twig/Tests/Extension/AbstractBootstrap3LayoutTestCase.php` -> **127** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Symfony/Bridge/PhpUnit/bin/simple-phpunit.php`** -> AI Confidence: **99.48%**
2. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/full.php`** -> AI Confidence: **99.48%**
3. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/container1.php`** -> AI Confidence: **99.48%**
4. **`src/Symfony/Component/Routing/Attribute/Route.php`** -> AI Confidence: **99.48%**
5. **`src/Symfony/Component/Routing/Matcher/Dumper/CompiledUrlMatcherTrait.php`** -> AI Confidence: **99.48%**
6. **`src/Symfony/Component/Validator/Constraints/Image.php`** -> AI Confidence: **99.48%**
7. **`src/Symfony/Component/Validator/Constraints/Video.php`** -> AI Confidence: **99.48%**
8. **`src/Symfony/Component/Config/Definition/Dumper/YamlReferenceDumper.php`** -> AI Confidence: **99.39%**
9. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveBindingsPass.php`** -> AI Confidence: **99.39%**
10. **`src/Symfony/Component/Dotenv/Dotenv.php`** -> AI Confidence: **99.39%**
11. **`src/Symfony/Component/ErrorHandler/Resources/views/exception_full.html.php`** -> AI Confidence: **99.39%**
12. **`src/Symfony/Component/HttpClient/Response/NativeResponse.php`** -> AI Confidence: **99.39%**
13. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php`** -> AI Confidence: **99.39%**
14. **`src/Symfony/Component/JsonPath/Tokenizer/JsonPathTokenizer.php`** -> AI Confidence: **99.39%**
15. **`src/Symfony/Component/Routing/Matcher/TraceableUrlMatcher.php`** -> AI Confidence: **99.39%**
16. **`src/Symfony/Component/Routing/RouteCompiler.php`** -> AI Confidence: **99.39%**
17. **`src/Symfony/Component/Validator/Constraints/Choice.php`** -> AI Confidence: **99.39%**
18. **`src/Symfony/Bundle/FrameworkBundle/Controller/RedirectController.php`** -> AI Confidence: **99.34%**
19. **`src/Symfony/Component/Messenger/Bridge/Redis/Transport/Connection.php`** -> AI Confidence: **99.34%**
20. **`src/Symfony/Component/Routing/Loader/ContentLoaderTrait.php`** -> AI Confidence: **99.34%**
21. **`src/Symfony/Component/HttpClient/HttpClientTrait.php`** -> AI Confidence: **99.33%**
22. **`src/Symfony/Component/ErrorHandler/Resources/views/trace.html.php`** -> AI Confidence: **99.32%**
23. **`src/Symfony/Component/VarDumper/Dumper/CliDumper.php`** -> AI Confidence: **99.32%**
24. **`src/Symfony/Bridge/Doctrine/Validator/DoctrineLoader.php`** -> AI Confidence: **99.31%**
25. **`src/Symfony/Bridge/Monolog/Formatter/ConsoleFormatter.php`** -> AI Confidence: **99.31%**
26. **`src/Symfony/Bridge/PhpUnit/DeprecationErrorHandler.php`** -> AI Confidence: **99.31%**
27. **`src/Symfony/Bridge/PhpUnit/Legacy/SymfonyTestsListenerTrait.php`** -> AI Confidence: **99.31%**
28. **`src/Symfony/Bridge/PsrHttpMessage/Factory/PsrHttpFactory.php`** -> AI Confidence: **99.31%**
29. **`src/Symfony/Bridge/Twig/Command/DebugCommand.php`** -> AI Confidence: **99.31%**
30. **`src/Symfony/Bridge/Twig/Node/TransNode.php`** -> AI Confidence: **99.31%**
31. **`src/Symfony/Bridge/Twig/NodeVisitor/TranslationNodeVisitor.php`** -> AI Confidence: **99.31%**
32. **`src/Symfony/Bundle/FrameworkBundle/Command/AbstractConfigCommand.php`** -> AI Confidence: **99.31%**
33. **`src/Symfony/Bundle/FrameworkBundle/Command/AssetsInstallCommand.php`** -> AI Confidence: **99.31%**
34. **`src/Symfony/Bundle/FrameworkBundle/Command/CacheClearCommand.php`** -> AI Confidence: **99.31%**
35. **`src/Symfony/Bundle/FrameworkBundle/Command/ContainerDebugCommand.php`** -> AI Confidence: **99.31%**
36. **`src/Symfony/Bundle/FrameworkBundle/Command/DebugAutowiringCommand.php`** -> AI Confidence: **99.31%**
37. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsSetCommand.php`** -> AI Confidence: **99.31%**
38. **`src/Symfony/Bundle/FrameworkBundle/Command/TranslationExtractCommand.php`** -> AI Confidence: **99.31%**
39. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/JsonDescriptor.php`** -> AI Confidence: **99.31%**
40. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/MarkdownDescriptor.php`** -> AI Confidence: **99.31%**
41. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
42. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/XmlDescriptor.php`** -> AI Confidence: **99.31%**
43. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Compiler/PhpConfigReferenceDumpPass.php`** -> AI Confidence: **99.31%**
44. **`src/Symfony/Bundle/FrameworkBundle/Secrets/SodiumVault.php`** -> AI Confidence: **99.31%**
45. **`src/Symfony/Bundle/TwigBundle/DependencyInjection/Compiler/ExtensionPass.php`** -> AI Confidence: **99.31%**
46. **`src/Symfony/Bundle/WebProfilerBundle/Controller/ProfilerController.php`** -> AI Confidence: **99.31%**
47. **`src/Symfony/Bundle/WebProfilerBundle/EventListener/WebDebugToolbarListener.php`** -> AI Confidence: **99.31%**
48. **`src/Symfony/Component/Asset/VersionStrategy/JsonManifestVersionStrategy.php`** -> AI Confidence: **99.31%**
49. **`src/Symfony/Component/AssetMapper/Command/DebugAssetMapperCommand.php`** -> AI Confidence: **99.31%**
50. **`src/Symfony/Component/AssetMapper/Command/ImportMapAuditCommand.php`** -> AI Confidence: **99.31%**
51. **`src/Symfony/Component/AssetMapper/Compiler/JavaScriptImportPathCompiler.php`** -> AI Confidence: **99.31%**
52. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapGenerator.php`** -> AI Confidence: **99.31%**
53. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapManager.php`** -> AI Confidence: **99.31%**
54. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapRenderer.php`** -> AI Confidence: **99.31%**
55. **`src/Symfony/Component/AssetMapper/ImportMap/Resolver/JsDelivrEsmResolver.php`** -> AI Confidence: **99.31%**
56. **`src/Symfony/Component/Cache/Adapter/AbstractTagAwareAdapter.php`** -> AI Confidence: **99.31%**
57. **`src/Symfony/Component/Cache/Adapter/CouchbaseCollectionAdapter.php`** -> AI Confidence: **99.31%**
58. **`src/Symfony/Component/Cache/Adapter/DoctrineDbalAdapter.php`** -> AI Confidence: **99.31%**
59. **`src/Symfony/Component/Cache/Adapter/PdoAdapter.php`** -> AI Confidence: **99.31%**
60. **`src/Symfony/Component/Cache/Adapter/PhpArrayAdapter.php`** -> AI Confidence: **99.31%**
61. **`src/Symfony/Component/Cache/Adapter/RedisTagAwareAdapter.php`** -> AI Confidence: **99.31%**
62. **`src/Symfony/Component/Cache/DependencyInjection/CachePoolPass.php`** -> AI Confidence: **99.31%**
63. **`src/Symfony/Component/Cache/Psr16Cache.php`** -> AI Confidence: **99.31%**
64. **`src/Symfony/Component/Cache/Tests/Traits/RedisProxiesTest.php`** -> AI Confidence: **99.31%**
65. **`src/Symfony/Component/Config/Definition/Dumper/XmlReferenceDumper.php`** -> AI Confidence: **99.31%**
66. **`src/Symfony/Component/Config/Resource/ClassExistenceResource.php`** -> AI Confidence: **99.31%**
67. **`src/Symfony/Component/Console/Application.php`** -> AI Confidence: **99.31%**
68. **`src/Symfony/Component/Console/Attribute/Argument.php`** -> AI Confidence: **99.31%**
69. **`src/Symfony/Component/Console/Attribute/Ask.php`** -> AI Confidence: **99.31%**
70. **`src/Symfony/Component/Console/Attribute/AskChoice.php`** -> AI Confidence: **99.31%**
71. **`src/Symfony/Component/Console/Completion/CompletionInput.php`** -> AI Confidence: **99.31%**
72. **`src/Symfony/Component/Console/DependencyInjection/AddConsoleCommandPass.php`** -> AI Confidence: **99.31%**
73. **`src/Symfony/Component/Console/DependencyInjection/RegisterCommandArgumentLocatorsPass.php`** -> AI Confidence: **99.31%**
74. **`src/Symfony/Component/Console/Descriptor/MarkdownDescriptor.php`** -> AI Confidence: **99.31%**
75. **`src/Symfony/Component/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
76. **`src/Symfony/Component/Console/Helper/FileInputHelper.php`** -> AI Confidence: **99.31%**
77. **`src/Symfony/Component/Console/Helper/QuestionHelper.php`** -> AI Confidence: **99.31%**
78. **`src/Symfony/Component/Console/Helper/Table.php`** -> AI Confidence: **99.31%**
79. **`src/Symfony/Component/Console/Input/InputArgument.php`** -> AI Confidence: **99.31%**
80. **`src/Symfony/Component/Console/Input/InputDefinition.php`** -> AI Confidence: **99.31%**
81. **`src/Symfony/Component/Console/Input/InputOption.php`** -> AI Confidence: **99.31%**
82. **`src/Symfony/Component/DependencyInjection/Attribute/Autowire.php`** -> AI Confidence: **99.31%**
83. **`src/Symfony/Component/DependencyInjection/Attribute/AutowireLocator.php`** -> AI Confidence: **99.31%**
84. **`src/Symfony/Component/DependencyInjection/Compiler/AnalyzeServiceReferencesPass.php`** -> AI Confidence: **99.31%**
85. **`src/Symfony/Component/DependencyInjection/Compiler/AutowirePass.php`** -> AI Confidence: **99.31%**
86. **`src/Symfony/Component/DependencyInjection/Compiler/AutowireRequiredMethodsPass.php`** -> AI Confidence: **99.31%**
87. **`src/Symfony/Component/DependencyInjection/Compiler/CheckTypeDeclarationsPass.php`** -> AI Confidence: **99.31%**
88. **`src/Symfony/Component/DependencyInjection/Compiler/RegisterServiceSubscribersPass.php`** -> AI Confidence: **99.31%**
89. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveAutowireInlineAttributesPass.php`** -> AI Confidence: **99.31%**
90. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveDecoratorStackPass.php`** -> AI Confidence: **99.31%**
91. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveInvalidReferencesPass.php`** -> AI Confidence: **99.31%**
92. **`src/Symfony/Component/DependencyInjection/Compiler/ValidateEnvPlaceholdersPass.php`** -> AI Confidence: **99.31%**
93. **`src/Symfony/Component/DependencyInjection/Container.php`** -> AI Confidence: **99.31%**
94. **`src/Symfony/Component/DependencyInjection/ContainerBuilder.php`** -> AI Confidence: **99.31%**
95. **`src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php`** -> AI Confidence: **99.31%**
96. **`src/Symfony/Component/DependencyInjection/Dumper/XmlDumper.php`** -> AI Confidence: **99.31%**
97. **`src/Symfony/Component/DependencyInjection/Dumper/YamlDumper.php`** -> AI Confidence: **99.31%**
98. **`src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`** -> AI Confidence: **99.31%**
99. **`src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`** -> AI Confidence: **99.31%**
100. **`src/Symfony/Component/DependencyInjection/Loader/FileLoader.php`** -> AI Confidence: **99.31%**
101. **`src/Symfony/Component/DependencyInjection/Loader/PhpFileLoader.php`** -> AI Confidence: **99.31%**
102. **`src/Symfony/Component/Dotenv/Command/DebugCommand.php`** -> AI Confidence: **99.31%**
103. **`src/Symfony/Component/ErrorHandler/DebugClassLoader.php`** -> AI Confidence: **99.31%**
104. **`src/Symfony/Component/ErrorHandler/ErrorHandler.php`** -> AI Confidence: **99.31%**
105. **`src/Symfony/Component/EventDispatcher/DependencyInjection/RegisterListenersPass.php`** -> AI Confidence: **99.31%**
106. **`src/Symfony/Component/Filesystem/Filesystem.php`** -> AI Confidence: **99.31%**
107. **`src/Symfony/Component/Form/ChoiceList/Factory/DefaultChoiceListFactory.php`** -> AI Confidence: **99.31%**
108. **`src/Symfony/Component/Form/Console/Descriptor/JsonDescriptor.php`** -> AI Confidence: **99.31%**
109. **`src/Symfony/Component/Form/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
110. **`src/Symfony/Component/Form/Extension/Core/Type/BaseType.php`** -> AI Confidence: **99.31%**
111. **`src/Symfony/Component/Form/Extension/Core/Type/DateIntervalType.php`** -> AI Confidence: **99.31%**
112. **`src/Symfony/Component/Form/Extension/Core/Type/FileType.php`** -> AI Confidence: **99.31%**
113. **`src/Symfony/Component/Form/Extension/Validator/Constraints/FormValidator.php`** -> AI Confidence: **99.31%**
114. **`src/Symfony/Component/Form/Extension/Validator/ViolationMapper/ViolationMapper.php`** -> AI Confidence: **99.31%**
115. **`src/Symfony/Component/HtmlSanitizer/Visitor/DomVisitor.php`** -> AI Confidence: **99.31%**
116. **`src/Symfony/Component/HttpClient/CachingHttpClient.php`** -> AI Confidence: **99.31%**
117. **`src/Symfony/Component/HttpClient/CurlHttpClient.php`** -> AI Confidence: **99.31%**
118. **`src/Symfony/Component/HttpClient/DataCollector/HttpClientDataCollector.php`** -> AI Confidence: **99.31%**
119. **`src/Symfony/Component/HttpClient/EventSourceHttpClient.php`** -> AI Confidence: **99.31%**
120. **`src/Symfony/Component/HttpClient/GuzzleHttpHandler.php`** -> AI Confidence: **99.31%**
121. **`src/Symfony/Component/HttpClient/Internal/HttplugWaitLoop.php`** -> AI Confidence: **99.31%**
122. **`src/Symfony/Component/HttpClient/NativeHttpClient.php`** -> AI Confidence: **99.31%**
123. **`src/Symfony/Component/HttpClient/NoPrivateNetworkHttpClient.php`** -> AI Confidence: **99.31%**
124. **`src/Symfony/Component/HttpClient/Response/AmpResponse.php`** -> AI Confidence: **99.31%**
125. **`src/Symfony/Component/HttpClient/Response/AsyncResponse.php`** -> AI Confidence: **99.31%**
126. **`src/Symfony/Component/HttpClient/Response/CurlResponse.php`** -> AI Confidence: **99.31%**
127. **`src/Symfony/Component/HttpClient/Response/MockResponse.php`** -> AI Confidence: **99.31%**
128. **`src/Symfony/Component/HttpClient/Response/TraceableResponse.php`** -> AI Confidence: **99.31%**
129. **`src/Symfony/Component/HttpFoundation/Request.php`** -> AI Confidence: **99.31%**
130. **`src/Symfony/Component/HttpFoundation/Response.php`** -> AI Confidence: **99.31%**
131. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/SessionHandlerFactory.php`** -> AI Confidence: **99.31%**
132. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/RequestPayloadValueResolver.php`** -> AI Confidence: **99.31%**
133. **`src/Symfony/Component/HttpKernel/DataCollector/DumpDataCollector.php`** -> AI Confidence: **99.31%**
134. **`src/Symfony/Component/HttpKernel/DataCollector/EventDataCollector.php`** -> AI Confidence: **99.31%**
135. **`src/Symfony/Component/HttpKernel/DataCollector/LoggerDataCollector.php`** -> AI Confidence: **99.31%**
136. **`src/Symfony/Component/HttpKernel/DependencyInjection/RegisterControllerArgumentLocatorsPass.php`** -> AI Confidence: **99.31%**
137. **`src/Symfony/Component/HttpKernel/EventListener/AbstractSessionListener.php`** -> AI Confidence: **99.31%**
138. **`src/Symfony/Component/HttpKernel/EventListener/CacheAttributeListener.php`** -> AI Confidence: **99.31%**
139. **`src/Symfony/Component/HttpKernel/EventListener/DebugHandlersListener.php`** -> AI Confidence: **99.31%**
140. **`src/Symfony/Component/HttpKernel/EventListener/ProfilerListener.php`** -> AI Confidence: **99.31%**
141. **`src/Symfony/Component/HttpKernel/EventListener/RouterListener.php`** -> AI Confidence: **99.31%**
142. **`src/Symfony/Component/HttpKernel/Kernel.php`** -> AI Confidence: **99.31%**
143. **`src/Symfony/Component/Intl/Data/Generator/TimezoneDataGenerator.php`** -> AI Confidence: **99.31%**
144. **`src/Symfony/Component/Intl/Resources/bin/update-data.php`** -> AI Confidence: **99.31%**
145. **`src/Symfony/Component/Intl/Util/IntlTestHelper.php`** -> AI Confidence: **99.31%**
146. **`src/Symfony/Component/JsonPath/JsonCrawler.php`** -> AI Confidence: **99.31%**
147. **`src/Symfony/Component/Lock/Bridge/DynamoDb/Store/DynamoDbStore.php`** -> AI Confidence: **99.31%**
148. **`src/Symfony/Component/Lock/Lock.php`** -> AI Confidence: **99.31%**
149. **`src/Symfony/Component/Lock/Store/CombinedStore.php`** -> AI Confidence: **99.31%**
150. **`src/Symfony/Component/Lock/Store/PostgreSqlStore.php`** -> AI Confidence: **99.31%**
151. **`src/Symfony/Component/Lock/Store/RedisStore.php`** -> AI Confidence: **99.31%**
152. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesApiAsyncAwsTransport.php`** -> AI Confidence: **99.31%**
153. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesHttpAsyncAwsTransport.php`** -> AI Confidence: **99.31%**
154. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesSmtpTransport.php`** -> AI Confidence: **99.31%**
155. **`src/Symfony/Component/Mailer/Bridge/Mailchimp/Transport/MandrillApiTransport.php`** -> AI Confidence: **99.31%**
156. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Transport/MailgunApiTransport.php`** -> AI Confidence: **99.31%**
157. **`src/Symfony/Component/Mailer/Bridge/Mailjet/Transport/MailjetApiTransport.php`** -> AI Confidence: **99.31%**
158. **`src/Symfony/Component/Messenger/Bridge/AmazonSqs/Transport/Connection.php`** -> AI Confidence: **99.31%**
159. **`src/Symfony/Component/Messenger/Bridge/Amqp/Transport/AmqpReceiver.php`** -> AI Confidence: **99.31%**
160. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/Connection.php`** -> AI Confidence: **99.31%**
161. **`src/Symfony/Component/Messenger/Bridge/Redis/Transport/RedisReceiver.php`** -> AI Confidence: **99.31%**
162. **`src/Symfony/Component/Messenger/Command/ConsumeMessagesCommand.php`** -> AI Confidence: **99.31%**
163. **`src/Symfony/Component/Messenger/Command/FailedMessagesRemoveCommand.php`** -> AI Confidence: **99.31%**
164. **`src/Symfony/Component/Messenger/Command/FailedMessagesShowCommand.php`** -> AI Confidence: **99.31%**
165. **`src/Symfony/Component/Messenger/DependencyInjection/MessengerPass.php`** -> AI Confidence: **99.31%**
166. **`src/Symfony/Component/Messenger/Transport/TransportFactory.php`** -> AI Confidence: **99.31%**
167. **`src/Symfony/Component/Messenger/Worker.php`** -> AI Confidence: **99.31%**
168. **`src/Symfony/Component/Notifier/Bridge/Bluesky/BlueskyTransport.php`** -> AI Confidence: **99.31%**
169. **`src/Symfony/Component/Notifier/Bridge/ClickSend/ClickSendTransport.php`** -> AI Confidence: **99.31%**
170. **`src/Symfony/Component/Notifier/Bridge/Engagespot/EngagespotTransport.php`** -> AI Confidence: **99.31%**
171. **`src/Symfony/Component/Notifier/Bridge/Slack/SlackTransport.php`** -> AI Confidence: **99.31%**
172. **`src/Symfony/Component/Notifier/Bridge/Telegram/TelegramTransport.php`** -> AI Confidence: **99.31%**
173. **`src/Symfony/Component/Notifier/Bridge/Twitter/TwitterTransport.php`** -> AI Confidence: **99.31%**
174. **`src/Symfony/Component/Notifier/Channel/EmailChannel.php`** -> AI Confidence: **99.31%**
175. **`src/Symfony/Component/ObjectMapper/ObjectMapper.php`** -> AI Confidence: **99.31%**
176. **`src/Symfony/Component/Process/Process.php`** -> AI Confidence: **99.31%**
177. **`src/Symfony/Component/PropertyAccess/PropertyAccessor.php`** -> AI Confidence: **99.31%**
178. **`src/Symfony/Component/PropertyInfo/Extractor/PhpStanExtractor.php`** -> AI Confidence: **99.31%**
179. **`src/Symfony/Component/PropertyInfo/Extractor/ReflectionExtractor.php`** -> AI Confidence: **99.31%**
180. **`src/Symfony/Component/Routing/Generator/CompiledUrlGenerator.php`** -> AI Confidence: **99.31%**
181. **`src/Symfony/Component/Routing/Matcher/UrlMatcher.php`** -> AI Confidence: **99.31%**
182. **`src/Symfony/Component/Routing/Tests/RouteCompilerTest.php`** -> AI Confidence: **99.31%**
183. **`src/Symfony/Component/Runtime/GenericRuntime.php`** -> AI Confidence: **99.31%**
184. **`src/Symfony/Component/Runtime/SymfonyRuntime.php`** -> AI Confidence: **99.31%**
185. **`src/Symfony/Component/Security/Core/Authorization/AccessDecisionManager.php`** -> AI Confidence: **99.31%**
186. **`src/Symfony/Component/Security/Csrf/SameOriginCsrfTokenManager.php`** -> AI Confidence: **99.31%**
187. **`src/Symfony/Component/Security/Http/Firewall/ContextListener.php`** -> AI Confidence: **99.31%**
188. **`src/Symfony/Component/Security/Http/HttpUtils.php`** -> AI Confidence: **99.31%**
189. **`src/Symfony/Component/Semaphore/Semaphore.php`** -> AI Confidence: **99.31%**
190. **`src/Symfony/Component/Semaphore/Store/RedisStore.php`** -> AI Confidence: **99.31%**
191. **`src/Symfony/Component/Serializer/Encoder/XmlEncoder.php`** -> AI Confidence: **99.31%**
192. **`src/Symfony/Component/Serializer/Mapping/Loader/AttributeLoader.php`** -> AI Confidence: **99.31%**
193. **`src/Symfony/Component/Serializer/Mapping/Loader/YamlFileLoader.php`** -> AI Confidence: **99.31%**
194. **`src/Symfony/Component/Serializer/Normalizer/AbstractNormalizer.php`** -> AI Confidence: **99.31%**
195. **`src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php`** -> AI Confidence: **99.31%**
196. **`src/Symfony/Component/Serializer/Normalizer/ArrayDenormalizer.php`** -> AI Confidence: **99.31%**
197. **`src/Symfony/Component/Serializer/Normalizer/ProblemNormalizer.php`** -> AI Confidence: **99.31%**
198. **`src/Symfony/Component/Serializer/Serializer.php`** -> AI Confidence: **99.31%**
199. **`src/Symfony/Component/String/Slugger/AsciiSlugger.php`** -> AI Confidence: **99.31%**
200. **`src/Symfony/Component/Translation/Command/XliffLintCommand.php`** -> AI Confidence: **99.31%**
201. **`src/Symfony/Component/Translation/Loader/XliffFileLoader.php`** -> AI Confidence: **99.31%**
202. **`src/Symfony/Component/Translation/Resources/bin/translation-status.php`** -> AI Confidence: **99.31%**
203. **`src/Symfony/Component/Validator/Constraints/AtLeastOneOf.php`** -> AI Confidence: **99.31%**
204. **`src/Symfony/Component/Validator/Constraints/Bic.php`** -> AI Confidence: **99.31%**
205. **`src/Symfony/Component/Validator/Constraints/EmailValidator.php`** -> AI Confidence: **99.31%**
206. **`src/Symfony/Component/Validator/Constraints/FileValidator.php`** -> AI Confidence: **99.31%**
207. **`src/Symfony/Component/Validator/Constraints/Hostname.php`** -> AI Confidence: **99.31%**
208. **`src/Symfony/Component/Validator/Constraints/ImageValidator.php`** -> AI Confidence: **99.31%**
209. **`src/Symfony/Component/Validator/Constraints/Issn.php`** -> AI Confidence: **99.31%**
210. **`src/Symfony/Component/Validator/Constraints/Range.php`** -> AI Confidence: **99.31%**
211. **`src/Symfony/Component/Validator/Constraints/RangeValidator.php`** -> AI Confidence: **99.31%**
212. **`src/Symfony/Component/Validator/Constraints/UlidValidator.php`** -> AI Confidence: **99.31%**
213. **`src/Symfony/Component/Validator/Constraints/Url.php`** -> AI Confidence: **99.31%**
214. **`src/Symfony/Component/Validator/Constraints/WordCount.php`** -> AI Confidence: **99.31%**
215. **`src/Symfony/Component/Validator/Mapping/Loader/PropertyInfoLoader.php`** -> AI Confidence: **99.31%**
216. **`src/Symfony/Component/Validator/Validator/RecursiveContextualValidator.php`** -> AI Confidence: **99.31%**
217. **`src/Symfony/Component/Workflow/Dumper/GraphvizDumper.php`** -> AI Confidence: **99.31%**
218. **`src/Symfony/Component/Yaml/Command/LintCommand.php`** -> AI Confidence: **99.31%**
219. **`phpunit`** -> AI Confidence: **99.29%**
220. **`src/Symfony/Bridge/PhpUnit/Tests/DeprecationErrorHandler/deprecation/deprecation.php`** -> AI Confidence: **99.29%**
221. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/asset_mapper_without_assets.php`** -> AI Confidence: **99.29%**
222. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets.php`** -> AI Confidence: **99.29%**
223. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets_disabled.php`** -> AI Confidence: **99.29%**
224. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets_version_strategy_as_service.php`** -> AI Confidence: **99.29%**
225. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache.php`** -> AI Confidence: **99.29%**
226. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache_app_redis_tag_aware.php`** -> AI Confidence: **99.29%**
227. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache_app_redis_tag_aware_pool.php`** -> AI Confidence: **99.29%**
228. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/csrf.php`** -> AI Confidence: **99.29%**
229. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/csrf_needs_session.php`** -> AI Confidence: **99.29%**
230. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/default_config.php`** -> AI Confidence: **99.29%**
231. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/esi_and_ssi_without_fragments.php`** -> AI Confidence: **99.29%**
232. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/esi_disabled.php`** -> AI Confidence: **99.29%**
233. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_csrf_disabled.php`** -> AI Confidence: **99.29%**
234. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_csrf_field_attr.php`** -> AI Confidence: **99.29%**
235. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_default_csrf.php`** -> AI Confidence: **99.29%**
236. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_no_csrf.php`** -> AI Confidence: **99.29%**
237. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/fragments_and_hinclude.php`** -> AI Confidence: **99.29%**
238. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/html_sanitizer_default_allowed_link_and_media_hosts.php`** -> AI Confidence: **99.29%**
239. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/html_sanitizer_default_config.php`** -> AI Confidence: **99.29%**
240. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_caching.php`** -> AI Confidence: **99.29%**
241. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_default_options.php`** -> AI Confidence: **99.29%**
242. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_full_default_options.php`** -> AI Confidence: **99.29%**
243. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_mock.php`** -> AI Confidence: **99.29%**
244. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_mock_response_factory.php`** -> AI Confidence: **99.29%**
245. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_override_default_options.php`** -> AI Confidence: **99.29%**
246. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_rate_limiter.php`** -> AI Confidence: **99.29%**
247. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_retry.php`** -> AI Confidence: **99.29%**
248. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_scoped_without_query_option.php`** -> AI Confidence: **99.29%**
249. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_xml_key.php`** -> AI Confidence: **99.29%**
250. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/json_streamer.php`** -> AI Confidence: **99.29%**
251. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock.php`** -> AI Confidence: **99.29%**
252. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock_named.php`** -> AI Confidence: **99.29%**
253. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock_service_and_env.php`** -> AI Confidence: **99.29%**
254. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer.php`** -> AI Confidence: **99.29%**
255. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer_with_disabled_message_bus.php`** -> AI Confidence: **99.29%**
256. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer_with_specific_message_bus.php`** -> AI Confidence: **99.29%**
257. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_bus_name_stamp.php`** -> AI Confidence: **99.29%**
258. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_disabled.php`** -> AI Confidence: **99.29%**
259. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_middleware_factory_erroneous_format.php`** -> AI Confidence: **99.29%**
260. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_buses_with_deduplicate_middleware.php`** -> AI Confidence: **99.29%**
261. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_buses_without_deduplicate_middleware.php`** -> AI Confidence: **99.29%**
262. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_failure_transports.php`** -> AI Confidence: **99.29%**
263. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_failure_transports_global.php`** -> AI Confidence: **99.29%**
264. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_routing_invalid_wildcard.php`** -> AI Confidence: **99.29%**
265. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_transport.php`** -> AI Confidence: **99.29%**
266. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_transports.php`** -> AI Confidence: **99.29%**
267. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier.php`** -> AI Confidence: **99.29%**
268. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_with_disabled_message_bus.php`** -> AI Confidence: **99.29%**
269. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_with_specific_message_bus.php`** -> AI Confidence: **99.29%**
270. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_mailer.php`** -> AI Confidence: **99.29%**
271. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_messenger.php`** -> AI Confidence: **99.29%**
272. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_transports.php`** -> AI Confidence: **99.29%**
273. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_disabled.php`** -> AI Confidence: **99.29%**
274. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_enabled.php`** -> AI Confidence: **99.29%**
275. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_log_level.php`** -> AI Confidence: **99.29%**
276. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_log_levels.php`** -> AI Confidence: **99.29%**
277. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/profiler.php`** -> AI Confidence: **99.29%**
278. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_accessor.php`** -> AI Confidence: **99.29%**
279. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_info.php`** -> AI Confidence: **99.29%**
280. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_info_without_constructor_extractor.php`** -> AI Confidence: **99.29%**
281. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/request.php`** -> AI Confidence: **99.29%**
282. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/router_enabled_locales_env.php`** -> AI Confidence: **99.29%**
283. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore.php`** -> AI Confidence: **99.29%**
284. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_lock.php`** -> AI Confidence: **99.29%**
285. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_lock_named.php`** -> AI Confidence: **99.29%**
286. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_named.php`** -> AI Confidence: **99.29%**
287. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_disabled.php`** -> AI Confidence: **99.29%**
288. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_enabled.php`** -> AI Confidence: **99.29%**
289. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_mapping.php`** -> AI Confidence: **99.29%**
290. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_mapping_without_attributes.php`** -> AI Confidence: **99.29%**
291. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_without_translator.php`** -> AI Confidence: **99.29%**
292. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/session.php`** -> AI Confidence: **99.29%**
293. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/session_cookie_secure_auto.php`** -> AI Confidence: **99.29%**
294. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/ssi_disabled.php`** -> AI Confidence: **99.29%**
295. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_cache_dir_disabled.php`** -> AI Confidence: **99.29%**
296. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_fallbacks.php`** -> AI Confidence: **99.29%**
297. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_globals.php`** -> AI Confidence: **99.29%**
298. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_providers.php`** -> AI Confidence: **99.29%**
299. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_without_globals.php`** -> AI Confidence: **99.29%**
300. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/trusted_proxies_private_ranges.php`** -> AI Confidence: **99.29%**
301. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/type_info.php`** -> AI Confidence: **99.29%**
302. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_attributes.php`** -> AI Confidence: **99.29%**
303. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_auto_mapping.php`** -> AI Confidence: **99.29%**
304. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_email_validation_mode.php`** -> AI Confidence: **99.29%**
305. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_mapping.php`** -> AI Confidence: **99.29%**
306. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_multiple_static_methods.php`** -> AI Confidence: **99.29%**
307. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_no_static_method.php`** -> AI Confidence: **99.29%**
308. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_translation_domain.php`** -> AI Confidence: **99.29%**
309. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/web_link.php`** -> AI Confidence: **99.29%**
310. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/webhook.php`** -> AI Confidence: **99.29%**
311. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/webhook_without_serializer.php`** -> AI Confidence: **99.29%**
312. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/workflow_without_support_and_support_strategy.php`** -> AI Confidence: **99.29%**
313. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/workflows_enabled.php`** -> AI Confidence: **99.29%**
314. **`src/Symfony/Bundle/FrameworkBundle/Tests/Fixtures/Resources/views/translation.html.php`** -> AI Confidence: **99.29%**
315. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_customized_config.php`** -> AI Confidence: **99.29%**
316. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_default_strategy.php`** -> AI Confidence: **99.29%**
317. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_service.php`** -> AI Confidence: **99.29%**
318. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_service_and_strategy.php`** -> AI Confidence: **99.29%**
319. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_strategy_service.php`** -> AI Confidence: **99.29%**
320. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc.php`** -> AI Confidence: **99.29%**
321. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_encryption.php`** -> AI Confidence: **99.29%**
322. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_user_info_discovery.php`** -> AI Confidence: **99.29%**
323. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_user_info_multiple_discovery.php`** -> AI Confidence: **99.29%**
324. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/argon2i_hasher.php`** -> AI Confidence: **99.29%**
325. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/bcrypt_hasher.php`** -> AI Confidence: **99.29%**
326. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_patterns.php`** -> AI Confidence: **99.29%**
327. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_provider.php`** -> AI Confidence: **99.29%**
328. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_undefined_provider.php`** -> AI Confidence: **99.29%**
329. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/listener_provider.php`** -> AI Confidence: **99.29%**
330. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/listener_undefined_provider.php`** -> AI Confidence: **99.29%**
331. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/logout_clear_site_data.php`** -> AI Confidence: **99.29%**
332. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/merge.php`** -> AI Confidence: **99.29%**
333. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/merge_import.php`** -> AI Confidence: **99.29%**
334. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/migrating_hasher.php`** -> AI Confidence: **99.29%**
335. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/no_custom_user_checker.php`** -> AI Confidence: **99.29%**
336. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/remember_me_options.php`** -> AI Confidence: **99.29%**
337. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/sodium_hasher.php`** -> AI Confidence: **99.29%**
338. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/customTemplateEscapingGuesser.php`** -> AI Confidence: **99.29%**
339. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/empty.php`** -> AI Confidence: **99.29%**
340. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/extra.php`** -> AI Confidence: **99.29%**
341. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/formats.php`** -> AI Confidence: **99.29%**
342. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/full.php`** -> AI Confidence: **99.29%**
343. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/mailer.php`** -> AI Confidence: **99.29%**
344. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/no-cache.php`** -> AI Confidence: **99.29%**
345. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/path-cache.php`** -> AI Confidence: **99.29%**
346. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/prod-cache.php`** -> AI Confidence: **99.29%**
347. **`src/Symfony/Bundle/WebProfilerBundle/Tests/Fixtures/hello_world.php`** -> AI Confidence: **99.29%**
348. **`src/Symfony/Component/Console/Helper/OutputWrapper.php`** -> AI Confidence: **99.29%**
349. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/config/legacy_internal_scope.php`** -> AI Confidence: **99.29%**
350. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/directory/simple.php`** -> AI Confidence: **99.29%**
351. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services2.php`** -> AI Confidence: **99.29%**
352. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/simple.php`** -> AI Confidence: **99.29%**
353. **`src/Symfony/Component/Emoji/Resources/data/emoji-cs.php`** -> AI Confidence: **99.29%**
354. **`src/Symfony/Component/Emoji/Resources/data/emoji-da.php`** -> AI Confidence: **99.29%**
355. **`src/Symfony/Component/Emoji/Resources/data/emoji-hi_latn.php`** -> AI Confidence: **99.29%**
356. **`src/Symfony/Component/Emoji/Resources/data/emoji-kl.php`** -> AI Confidence: **99.29%**
357. **`src/Symfony/Component/Emoji/Resources/data/emoji-lij.php`** -> AI Confidence: **99.29%**
358. **`src/Symfony/Component/Emoji/Resources/data/emoji-no.php`** -> AI Confidence: **99.29%**
359. **`src/Symfony/Component/Emoji/Resources/data/emoji-pl.php`** -> AI Confidence: **99.29%**
360. **`src/Symfony/Component/Emoji/Resources/data/emoji-pt.php`** -> AI Confidence: **99.29%**
361. **`src/Symfony/Component/ErrorHandler/Resources/views/logs.html.php`** -> AI Confidence: **99.29%**
362. **`src/Symfony/Component/ErrorHandler/Tests/Fixtures/ClassAlias.php`** -> AI Confidence: **99.29%**
363. **`src/Symfony/Component/ExpressionLanguage/Lexer.php`** -> AI Confidence: **99.29%**
364. **`src/Symfony/Component/ExpressionLanguage/Resources/bin/generate_operator_regex.php`** -> AI Confidence: **99.29%**
365. **`src/Symfony/Component/Filesystem/Tests/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
366. **`src/Symfony/Component/Finder/Glob.php`** -> AI Confidence: **99.29%**
367. **`src/Symfony/Component/HttpClient/Tests/Fixtures/response-functional/index.php`** -> AI Confidence: **99.29%**
368. **`src/Symfony/Component/Intl/Resources/data/currencies/pt.php`** -> AI Confidence: **99.29%**
369. **`src/Symfony/Component/Intl/Resources/data/currencies/pt_PT.php`** -> AI Confidence: **99.29%**
370. **`src/Symfony/Component/Intl/Resources/data/languages/gl.php`** -> AI Confidence: **99.29%**
371. **`src/Symfony/Component/Intl/Resources/data/languages/pt.php`** -> AI Confidence: **99.29%**
372. **`src/Symfony/Component/Intl/Resources/data/languages/pt_PT.php`** -> AI Confidence: **99.29%**
373. **`src/Symfony/Component/Intl/Resources/data/locales/gl.php`** -> AI Confidence: **99.29%**
374. **`src/Symfony/Component/Intl/Resources/data/locales/pt.php`** -> AI Confidence: **99.29%**
375. **`src/Symfony/Component/Intl/Resources/data/locales/pt_PT.php`** -> AI Confidence: **99.29%**
376. **`src/Symfony/Component/Intl/Resources/data/regions/gl.php`** -> AI Confidence: **99.29%**
377. **`src/Symfony/Component/Intl/Resources/data/regions/pt.php`** -> AI Confidence: **99.29%**
378. **`src/Symfony/Component/Intl/Resources/data/regions/pt_PT.php`** -> AI Confidence: **99.29%**
379. **`src/Symfony/Component/Intl/Resources/data/timezones/gl.php`** -> AI Confidence: **99.29%**
380. **`src/Symfony/Component/Intl/Resources/data/timezones/nn.php`** -> AI Confidence: **99.29%**
381. **`src/Symfony/Component/Intl/Resources/data/timezones/no.php`** -> AI Confidence: **99.29%**
382. **`src/Symfony/Component/Intl/Resources/data/timezones/pt.php`** -> AI Confidence: **99.29%**
383. **`src/Symfony/Component/Intl/Resources/data/timezones/pt_PT.php`** -> AI Confidence: **99.29%**
384. **`src/Symfony/Component/Mailer/Tests/Transport/Fixtures/fake-failing-sendmail.php`** -> AI Confidence: **99.29%**
385. **`src/Symfony/Component/Mailer/Tests/Transport/Fixtures/fake-sendmail.php`** -> AI Confidence: **99.29%**
386. **`src/Symfony/Component/Mime/Tests/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
387. **`src/Symfony/Component/Notifier/Bridge/Primotexto/PrimotextoErrorCode.php`** -> AI Confidence: **99.29%**
388. **`src/Symfony/Component/Process/Tests/Fixtures/memory.php`** -> AI Confidence: **99.29%**
389. **`src/Symfony/Component/Process/Tests/NonStopableProcess.php`** -> AI Confidence: **99.29%**
390. **`src/Symfony/Component/Process/Tests/PipeStdinInStdoutStdErrStreamSelect.php`** -> AI Confidence: **99.29%**
391. **`src/Symfony/Component/Process/Tests/ThreeSecondProcess.php`** -> AI Confidence: **99.29%**
392. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher1.php`** -> AI Confidence: **99.29%**
393. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher11.php`** -> AI Confidence: **99.29%**
394. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher12.php`** -> AI Confidence: **99.29%**
395. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher13.php`** -> AI Confidence: **99.29%**
396. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher2.php`** -> AI Confidence: **99.29%**
397. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher6.php`** -> AI Confidence: **99.29%**
398. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher7.php`** -> AI Confidence: **99.29%**
399. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher8.php`** -> AI Confidence: **99.29%**
400. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-7.3/translation.html.php`** -> AI Confidence: **99.29%**
401. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translatable-short-fqn.html.php`** -> AI Confidence: **99.29%**
402. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translatable-short.html.php`** -> AI Confidence: **99.29%**
403. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translation.html.php`** -> AI Confidence: **99.29%**
404. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor/translatable-short.html.php`** -> AI Confidence: **99.29%**
405. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor/translation.html.php`** -> AI Confidence: **99.29%**
406. **`src/Symfony/Contracts/Deprecation/function.php`** -> AI Confidence: **99.29%**
407. **`src/Symfony/Contracts/HttpClient/Test/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
408. **`src/Symfony/Component/Console/Resources/completion.bash`** -> AI Confidence: **99.29%**
409. **`src/Symfony/Component/Console/Resources/completion.fish`** -> AI Confidence: **99.29%**
410. **`src/Symfony/Component/Console/Resources/completion.zsh`** -> AI Confidence: **99.29%**
411. **`src/Symfony/Component/Translation/Tests/Fixtures/resources.ts`** -> AI Confidence: **99.29%**
412. **`src/Symfony/Component/HttpClient/Response/TransportResponseTrait.php`** -> AI Confidence: **99.28%**
413. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolverTrait.php`** -> AI Confidence: **99.25%**
414. **`src/Symfony/Component/Cache/Traits/ContractsTrait.php`** -> AI Confidence: **99.25%**
415. **`src/Symfony/Component/Cache/Traits/RedisTrait.php`** -> AI Confidence: **99.25%**
416. **`src/Symfony/Component/Lock/Store/DatabaseTableTrait.php`** -> AI Confidence: **99.25%**
417. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php`** -> AI Confidence: **99.24%**
418. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php`** -> AI Confidence: **99.24%**
419. **`src/Symfony/Bridge/Doctrine/DependencyInjection/CompilerPass/RegisterEventListenersAndSubscribersPass.php`** -> AI Confidence: **99.24%**
420. **`src/Symfony/Bridge/Doctrine/PropertyInfo/DoctrineExtractor.php`** -> AI Confidence: **99.24%**
421. **`src/Symfony/Bridge/Monolog/Handler/MailerHandler.php`** -> AI Confidence: **99.24%**
422. **`src/Symfony/Bridge/PhpUnit/DeprecationErrorHandler/Deprecation.php`** -> AI Confidence: **99.24%**
423. **`src/Symfony/Bridge/PhpUnit/Legacy/CommandForV9.php`** -> AI Confidence: **99.24%**
424. **`src/Symfony/Bridge/Twig/Command/LintCommand.php`** -> AI Confidence: **99.24%**
425. **`src/Symfony/Bridge/Twig/EventListener/TemplateAttributeListener.php`** -> AI Confidence: **99.24%**
426. **`src/Symfony/Bridge/Twig/Validator/Constraints/TwigValidator.php`** -> AI Confidence: **99.24%**
427. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolClearCommand.php`** -> AI Confidence: **99.24%**
428. **`src/Symfony/Bundle/FrameworkBundle/Command/ConfigDumpReferenceCommand.php`** -> AI Confidence: **99.24%**
429. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsListCommand.php`** -> AI Confidence: **99.24%**
430. **`src/Symfony/Bundle/FrameworkBundle/Command/TranslationDebugCommand.php`** -> AI Confidence: **99.24%**
431. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/Descriptor.php`** -> AI Confidence: **99.24%**
432. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Configuration.php`** -> AI Confidence: **99.24%**
433. **`src/Symfony/Bundle/FrameworkBundle/EventListener/ConsoleProfilerListener.php`** -> AI Confidence: **99.24%**
434. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ApiAttributesTest.php`** -> AI Confidence: **99.24%**
435. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/SecurityExtension.php`** -> AI Confidence: **99.24%**
436. **`src/Symfony/Bundle/TwigBundle/DependencyInjection/TwigExtension.php`** -> AI Confidence: **99.24%**
437. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapConfigReader.php`** -> AI Confidence: **99.24%**
438. **`src/Symfony/Component/BrowserKit/AbstractBrowser.php`** -> AI Confidence: **99.24%**
439. **`src/Symfony/Component/BrowserKit/HttpBrowser.php`** -> AI Confidence: **99.24%**
440. **`src/Symfony/Component/Cache/Adapter/AbstractAdapter.php`** -> AI Confidence: **99.24%**
441. **`src/Symfony/Component/Cache/Adapter/ChainAdapter.php`** -> AI Confidence: **99.24%**
442. **`src/Symfony/Component/Cache/Adapter/TagAwareAdapter.php`** -> AI Confidence: **99.24%**
443. **`src/Symfony/Component/Console/ArgumentResolver/ArgumentResolver.php`** -> AI Confidence: **99.24%**
444. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/MapInputValueResolver.php`** -> AI Confidence: **99.24%**
445. **`src/Symfony/Component/Console/Command/Command.php`** -> AI Confidence: **99.24%**
446. **`src/Symfony/Component/Console/Command/CompleteCommand.php`** -> AI Confidence: **99.24%**
447. **`src/Symfony/Component/Console/Command/DumpCompletionCommand.php`** -> AI Confidence: **99.24%**
448. **`src/Symfony/Component/Console/Command/InvokableCommand.php`** -> AI Confidence: **99.24%**
449. **`src/Symfony/Component/Console/Descriptor/ReStructuredTextDescriptor.php`** -> AI Confidence: **99.24%**
450. **`src/Symfony/Component/Console/Style/SymfonyStyle.php`** -> AI Confidence: **99.24%**
451. **`src/Symfony/Component/Console/Tester/CommandTester.php`** -> AI Confidence: **99.24%**
452. **`src/Symfony/Component/DependencyInjection/Compiler/AbstractRecursivePass.php`** -> AI Confidence: **99.24%**
453. **`src/Symfony/Component/DependencyInjection/Compiler/AutowireRequiredPropertiesPass.php`** -> AI Confidence: **99.24%**
454. **`src/Symfony/Component/DependencyInjection/Compiler/MergeExtensionConfigurationPass.php`** -> AI Confidence: **99.24%**
455. **`src/Symfony/Component/DependencyInjection/Compiler/ServiceLocatorTagPass.php`** -> AI Confidence: **99.24%**
456. **`src/Symfony/Component/DependencyInjection/Dumper/GraphvizDumper.php`** -> AI Confidence: **99.24%**
457. **`src/Symfony/Component/DependencyInjection/Loader/YamlFileLoader.php`** -> AI Confidence: **99.24%**
458. **`src/Symfony/Component/DependencyInjection/ServiceLocator.php`** -> AI Confidence: **99.24%**
459. **`src/Symfony/Component/Dotenv/Command/DotenvDumpCommand.php`** -> AI Confidence: **99.24%**
460. **`src/Symfony/Component/Form/Extension/Core/Type/DateTimeType.php`** -> AI Confidence: **99.24%**
461. **`src/Symfony/Component/Form/Extension/Core/Type/DateType.php`** -> AI Confidence: **99.24%**
462. **`src/Symfony/Component/Form/Extension/Core/Type/MoneyType.php`** -> AI Confidence: **99.24%**
463. **`src/Symfony/Component/Form/Extension/Core/Type/TimeType.php`** -> AI Confidence: **99.24%**
464. **`src/Symfony/Component/Form/Extension/HttpFoundation/HttpFoundationRequestHandler.php`** -> AI Confidence: **99.24%**
465. **`src/Symfony/Component/HttpClient/AmpHttpClient.php`** -> AI Confidence: **99.24%**
466. **`src/Symfony/Component/HttpClient/Internal/AmpClientState.php`** -> AI Confidence: **99.24%**
467. **`src/Symfony/Component/HttpClient/RetryableHttpClient.php`** -> AI Confidence: **99.24%**
468. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver.php`** -> AI Confidence: **99.24%**
469. **`src/Symfony/Component/HttpKernel/Fragment/HIncludeFragmentRenderer.php`** -> AI Confidence: **99.24%**
470. **`src/Symfony/Component/HttpKernel/HttpKernel.php`** -> AI Confidence: **99.24%**
471. **`src/Symfony/Component/Intl/Currencies.php`** -> AI Confidence: **99.24%**
472. **`src/Symfony/Component/JsonStreamer/Mapping/Write/AttributePropertyMetadataLoader.php`** -> AI Confidence: **99.24%**
473. **`src/Symfony/Component/JsonStreamer/Read/PhpGenerator.php`** -> AI Confidence: **99.24%**
474. **`src/Symfony/Component/JsonStreamer/StreamerDumper.php`** -> AI Confidence: **99.24%**
475. **`src/Symfony/Component/JsonStreamer/Write/PhpGenerator.php`** -> AI Confidence: **99.24%**
476. **`src/Symfony/Component/Ldap/Adapter/ExtLdap/Connection.php`** -> AI Confidence: **99.24%**
477. **`src/Symfony/Component/Lock/Store/DoctrineDbalPostgreSqlStore.php`** -> AI Confidence: **99.24%**
478. **`src/Symfony/Component/Lock/Store/StoreFactory.php`** -> AI Confidence: **99.24%**
479. **`src/Symfony/Component/Lock/Tests/Store/BlockingStoreTestTrait.php`** -> AI Confidence: **99.24%**
480. **`src/Symfony/Component/Mailer/Bridge/AhaSend/Transport/AhaSendApiTransport.php`** -> AI Confidence: **99.24%**
481. **`src/Symfony/Component/Mailer/Bridge/Brevo/Transport/BrevoApiTransport.php`** -> AI Confidence: **99.24%**
482. **`src/Symfony/Component/Mailer/Bridge/Infobip/Transport/InfobipApiTransport.php`** -> AI Confidence: **99.24%**
483. **`src/Symfony/Component/Mailer/Bridge/MailPace/Transport/MailPaceApiTransport.php`** -> AI Confidence: **99.24%**
484. **`src/Symfony/Component/Mailer/Bridge/MailerSend/Transport/MailerSendApiTransport.php`** -> AI Confidence: **99.24%**
485. **`src/Symfony/Component/Mailer/Bridge/Mailtrap/Transport/MailtrapApiTransport.php`** -> AI Confidence: **99.24%**
486. **`src/Symfony/Component/Mailer/Bridge/Postmark/Transport/PostmarkApiTransport.php`** -> AI Confidence: **99.24%**
487. **`src/Symfony/Component/Mailer/Bridge/Resend/Transport/ResendApiTransport.php`** -> AI Confidence: **99.24%**
488. **`src/Symfony/Component/Mailer/Bridge/Scaleway/Transport/ScalewayApiTransport.php`** -> AI Confidence: **99.24%**
489. **`src/Symfony/Component/Mailer/Transport/SendmailTransport.php`** -> AI Confidence: **99.24%**
490. **`src/Symfony/Component/Mailer/Transport/Smtp/EsmtpTransport.php`** -> AI Confidence: **99.24%**
491. **`src/Symfony/Component/Messenger/Command/FailedMessagesRetryCommand.php`** -> AI Confidence: **99.24%**
492. **`src/Symfony/Component/Messenger/EventListener/SendFailedMessageForRetryListener.php`** -> AI Confidence: **99.24%**
493. **`src/Symfony/Component/Messenger/Middleware/HandleMessageMiddleware.php`** -> AI Confidence: **99.24%**
494. **`src/Symfony/Component/Notifier/Bridge/AmazonSns/AmazonSnsTransport.php`** -> AI Confidence: **99.24%**
495. **`src/Symfony/Component/Notifier/Bridge/Bandwidth/BandwidthTransport.php`** -> AI Confidence: **99.24%**
496. **`src/Symfony/Component/Notifier/Bridge/ContactEveryone/ContactEveryoneTransport.php`** -> AI Confidence: **99.24%**
497. **`src/Symfony/Component/Notifier/Bridge/Esendex/EsendexTransport.php`** -> AI Confidence: **99.24%**
498. **`src/Symfony/Component/Notifier/Bridge/Expo/ExpoTransport.php`** -> AI Confidence: **99.24%**
499. **`src/Symfony/Component/Notifier/Bridge/Firebase/FirebaseTransport.php`** -> AI Confidence: **99.24%**
500. **`src/Symfony/Component/Notifier/Bridge/GoogleChat/GoogleChatTransport.php`** -> AI Confidence: **99.24%**
501. **`src/Symfony/Component/Notifier/Bridge/Isendpro/IsendproTransport.php`** -> AI Confidence: **99.24%**
502. **`src/Symfony/Component/Notifier/Bridge/Lox24/Lox24Transport.php`** -> AI Confidence: **99.24%**
503. **`src/Symfony/Component/Notifier/Bridge/Lox24/Webhook/Lox24RequestParser.php`** -> AI Confidence: **99.24%**
504. **`src/Symfony/Component/Notifier/Bridge/Mattermost/MattermostTransport.php`** -> AI Confidence: **99.24%**
505. **`src/Symfony/Component/Notifier/Bridge/MessageMedia/MessageMediaTransport.php`** -> AI Confidence: **99.24%**
506. **`src/Symfony/Component/Notifier/Bridge/Ntfy/NtfyTransport.php`** -> AI Confidence: **99.24%**
507. **`src/Symfony/Component/Notifier/Bridge/OneSignal/OneSignalTransport.php`** -> AI Confidence: **99.24%**
508. **`src/Symfony/Component/Notifier/Bridge/Plivo/PlivoTransport.php`** -> AI Confidence: **99.24%**
509. **`src/Symfony/Component/Notifier/Bridge/Primotexto/PrimotextoTransport.php`** -> AI Confidence: **99.24%**
510. **`src/Symfony/Component/Notifier/Bridge/RingCentral/RingCentralTransport.php`** -> AI Confidence: **99.24%**
511. **`src/Symfony/Component/Notifier/Bridge/Smsbox/SmsboxTransport.php`** -> AI Confidence: **99.24%**
512. **`src/Symfony/Component/Notifier/Bridge/Smsmode/SmsmodeTransport.php`** -> AI Confidence: **99.24%**
513. **`src/Symfony/Component/Notifier/Bridge/Sweego/SweegoTransport.php`** -> AI Confidence: **99.24%**
514. **`src/Symfony/Component/Notifier/Bridge/Telnyx/TelnyxTransport.php`** -> AI Confidence: **99.24%**
515. **`src/Symfony/Component/Notifier/Bridge/Termii/TermiiTransport.php`** -> AI Confidence: **99.24%**
516. **`src/Symfony/Component/Notifier/Bridge/Twilio/TwilioTransport.php`** -> AI Confidence: **99.24%**
517. **`src/Symfony/Component/Notifier/Bridge/Zendesk/ZendeskTransport.php`** -> AI Confidence: **99.24%**
518. **`src/Symfony/Component/OptionsResolver/OptionsResolver.php`** -> AI Confidence: **99.24%**
519. **`src/Symfony/Component/PropertyInfo/Extractor/PhpDocExtractor.php`** -> AI Confidence: **99.24%**
520. **`src/Symfony/Component/PropertyInfo/Util/PhpDocTypeHelper.php`** -> AI Confidence: **99.24%**
521. **`src/Symfony/Component/RateLimiter/Policy/SlidingWindowLimiter.php`** -> AI Confidence: **99.24%**
522. **`src/Symfony/Component/RateLimiter/Policy/TokenBucketLimiter.php`** -> AI Confidence: **99.24%**
523. **`src/Symfony/Component/Routing/Loader/AttributeClassLoader.php`** -> AI Confidence: **99.24%**
524. **`src/Symfony/Component/Routing/Matcher/Dumper/CompiledUrlMatcherDumper.php`** -> AI Confidence: **99.24%**
525. **`src/Symfony/Component/Routing/RouteCollection.php`** -> AI Confidence: **99.24%**
526. **`src/Symfony/Component/Runtime/Internal/ComposerPlugin.php`** -> AI Confidence: **99.24%**
527. **`src/Symfony/Component/Scheduler/DependencyInjection/AddScheduleMessengerPass.php`** -> AI Confidence: **99.24%**
528. **`src/Symfony/Component/Security/Http/AccessToken/OAuth2/Oauth2TokenHandler.php`** -> AI Confidence: **99.24%**
529. **`src/Symfony/Component/Security/Http/Authentication/AuthenticatorManager.php`** -> AI Confidence: **99.24%**
530. **`src/Symfony/Component/Security/Http/Authentication/DefaultAuthenticationFailureHandler.php`** -> AI Confidence: **99.24%**
531. **`src/Symfony/Component/Security/Http/Firewall/ExceptionListener.php`** -> AI Confidence: **99.24%**
532. **`src/Symfony/Component/Semaphore/Store/LockStore.php`** -> AI Confidence: **99.24%**
533. **`src/Symfony/Component/Semaphore/Store/StoreFactory.php`** -> AI Confidence: **99.24%**
534. **`src/Symfony/Component/Serializer/DependencyInjection/SerializerPass.php`** -> AI Confidence: **99.24%**
535. **`src/Symfony/Component/Serializer/Normalizer/ObjectNormalizer.php`** -> AI Confidence: **99.24%**
536. **`src/Symfony/Component/Translation/Bridge/Phrase/PhraseProvider.php`** -> AI Confidence: **99.24%**
537. **`src/Symfony/Component/Translation/Translator.php`** -> AI Confidence: **99.24%**
538. **`src/Symfony/Component/TypeInfo/TypeContext/TypeContextFactory.php`** -> AI Confidence: **99.24%**
539. **`src/Symfony/Component/TypeInfo/TypeFactoryTrait.php`** -> AI Confidence: **99.24%**
540. **`src/Symfony/Component/TypeInfo/TypeResolver/PhpDocAwareReflectionTypeResolver.php`** -> AI Confidence: **99.24%**
541. **`src/Symfony/Component/TypeInfo/TypeResolver/StringTypeResolver.php`** -> AI Confidence: **99.24%**
542. **`src/Symfony/Component/Validator/Constraints/AbstractComparison.php`** -> AI Confidence: **99.24%**
543. **`src/Symfony/Component/Validator/Constraints/AbstractComparisonValidator.php`** -> AI Confidence: **99.24%**
544. **`src/Symfony/Component/Validator/Constraints/BicValidator.php`** -> AI Confidence: **99.24%**
545. **`src/Symfony/Component/Validator/Constraints/ExpressionSyntaxValidator.php`** -> AI Confidence: **99.24%**
546. **`src/Symfony/Component/Workflow/EventListener/GuardListener.php`** -> AI Confidence: **99.24%**
547. **`src/Symfony/Component/Workflow/Workflow.php`** -> AI Confidence: **99.24%**
548. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsDecryptToLocalCommand.php`** -> AI Confidence: **99.23%**
549. **`src/Symfony/Bundle/FrameworkBundle/HttpCache/HttpCache.php`** -> AI Confidence: **99.23%**
550. **`src/Symfony/Bundle/FrameworkBundle/Test/HttpClientAssertionsTrait.php`** -> AI Confidence: **99.23%**
551. **`src/Symfony/Component/AssetMapper/AssetMapperDevServerSubscriber.php`** -> AI Confidence: **99.23%**
552. **`src/Symfony/Component/Cache/Adapter/TraceableAdapter.php`** -> AI Confidence: **99.23%**
553. **`src/Symfony/Component/Config/Definition/Builder/ArrayNodeDefinition.php`** -> AI Confidence: **99.23%**
554. **`src/Symfony/Component/Config/Exception/LoaderLoadException.php`** -> AI Confidence: **99.23%**
555. **`src/Symfony/Component/Console/Tester/ConsoleAssertionsTrait.php`** -> AI Confidence: **99.23%**
556. **`src/Symfony/Component/CssSelector/Parser/Handler/StringHandler.php`** -> AI Confidence: **99.23%**
557. **`src/Symfony/Component/ErrorHandler/ErrorEnhancer/ClassNotFoundErrorEnhancer.php`** -> AI Confidence: **99.23%**
558. **`src/Symfony/Component/ErrorHandler/Resources/views/exception.html.php`** -> AI Confidence: **99.23%**
559. **`src/Symfony/Component/Form/ChoiceList/Factory/PropertyAccessDecorator.php`** -> AI Confidence: **99.23%**
560. **`src/Symfony/Component/Form/Extension/Csrf/EventListener/CsrfValidationListener.php`** -> AI Confidence: **99.23%**
561. **`src/Symfony/Component/Form/Flow/FormFlow.php`** -> AI Confidence: **99.23%**
562. **`src/Symfony/Component/HttpFoundation/Tests/UriSignerTest.php`** -> AI Confidence: **99.23%**
563. **`src/Symfony/Component/HttpFoundation/UriSigner.php`** -> AI Confidence: **99.23%**
564. **`src/Symfony/Component/HttpKernel/EventListener/DumpListener.php`** -> AI Confidence: **99.23%**
565. **`src/Symfony/Component/HttpKernel/Profiler/Profiler.php`** -> AI Confidence: **99.23%**
566. **`src/Symfony/Component/JsonStreamer/Mapping/Read/AttributePropertyMetadataLoader.php`** -> AI Confidence: **99.23%**
567. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Transport/SendgridSmtpTransport.php`** -> AI Confidence: **99.23%**
568. **`src/Symfony/Component/Mailer/EventListener/MessageListener.php`** -> AI Confidence: **99.23%**
569. **`src/Symfony/Component/Messenger/Bridge/Amqp/Transport/AmqpSender.php`** -> AI Confidence: **99.23%**
570. **`src/Symfony/Component/Notifier/Bridge/AllMySms/AllMySmsTransport.php`** -> AI Confidence: **99.23%**
571. **`src/Symfony/Component/Notifier/Bridge/KazInfoTeh/KazInfoTehTransport.php`** -> AI Confidence: **99.23%**
572. **`src/Symfony/Component/Notifier/Bridge/Mobyt/MobytTransport.php`** -> AI Confidence: **99.23%**
573. **`src/Symfony/Component/Notifier/Bridge/RocketChat/RocketChatTransport.php`** -> AI Confidence: **99.23%**
574. **`src/Symfony/Component/Notifier/Bridge/SmsFactor/SmsFactorTransport.php`** -> AI Confidence: **99.23%**
575. **`src/Symfony/Component/Security/Core/Authorization/Voter/ExpressionVoter.php`** -> AI Confidence: **99.23%**
576. **`src/Symfony/Component/Security/Http/Authentication/DefaultAuthenticationSuccessHandler.php`** -> AI Confidence: **99.23%**
577. **`src/Symfony/Component/Serializer/Mapping/Loader/XmlFileLoader.php`** -> AI Confidence: **99.23%**
578. **`src/Symfony/Component/Serializer/Normalizer/DataUriNormalizer.php`** -> AI Confidence: **99.23%**
579. **`src/Symfony/Component/Translation/Bridge/Loco/LocoProvider.php`** -> AI Confidence: **99.23%**
580. **`src/Symfony/Component/Validator/Constraints/PasswordStrength.php`** -> AI Confidence: **99.23%**
581. **`src/Symfony/Component/Cache/LockRegistry.php`** -> AI Confidence: **99.2%**
582. **`src/Symfony/Component/DomCrawler/Tests/UriResolverTest.php`** -> AI Confidence: **99.2%**
583. **`src/Symfony/Component/Validator/Constraints/Length.php`** -> AI Confidence: **99.2%**
584. **`src/Symfony/Bridge/Doctrine/Form/DoctrineOrmTypeGuesser.php`** -> AI Confidence: **99.18%**
585. **`src/Symfony/Bridge/Doctrine/Form/Type/DoctrineType.php`** -> AI Confidence: **99.18%**
586. **`src/Symfony/Bridge/Doctrine/Security/RememberMe/DoctrineTokenProvider.php`** -> AI Confidence: **99.18%**
587. **`src/Symfony/Bridge/Doctrine/Tests/Form/Type/EntityTypePerformanceTest.php`** -> AI Confidence: **99.18%**
588. **`src/Symfony/Bridge/Monolog/Processor/ConsoleCommandProcessor.php`** -> AI Confidence: **99.18%**
589. **`src/Symfony/Bridge/Monolog/Processor/RouteProcessor.php`** -> AI Confidence: **99.18%**
590. **`src/Symfony/Bridge/PhpUnit/CoverageListener.php`** -> AI Confidence: **99.18%**
591. **`src/Symfony/Bridge/PhpUnit/Tests/Fixtures/symfonyextension/tests/bootstrap.php`** -> AI Confidence: **99.18%**
592. **`src/Symfony/Bridge/Twig/Extension/TranslationExtension.php`** -> AI Confidence: **99.18%**
593. **`src/Symfony/Bridge/Twig/Tests/Command/LintCommandTest.php`** -> AI Confidence: **99.18%**
594. **`src/Symfony/Bridge/Twig/Translation/TwigExtractor.php`** -> AI Confidence: **99.18%**
595. **`src/Symfony/Bundle/DebugBundle/DependencyInjection/DebugExtension.php`** -> AI Confidence: **99.18%**
596. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolDeleteCommand.php`** -> AI Confidence: **99.18%**
597. **`src/Symfony/Bundle/FrameworkBundle/Command/ContainerLintCommand.php`** -> AI Confidence: **99.18%**
598. **`src/Symfony/Bundle/FrameworkBundle/Test/KernelTestCase.php`** -> AI Confidence: **99.18%**
599. **`src/Symfony/Bundle/FrameworkBundle/Test/TestContainer.php`** -> AI Confidence: **99.18%**
600. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/CachePoolClearCommandTest.php`** -> AI Confidence: **99.18%**
601. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ConfigDebugCommandTest.php`** -> AI Confidence: **99.18%**
602. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ConfigDumpReferenceCommandTest.php`** -> AI Confidence: **99.18%**
603. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/JsonStreamerTest.php`** -> AI Confidence: **99.18%**
604. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/RegisterCsrfFeaturesPass.php`** -> AI Confidence: **99.18%**
605. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/SortFirewallListenersPass.php`** -> AI Confidence: **99.18%**
606. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/AccessToken/OidcTokenHandlerFactory.php`** -> AI Confidence: **99.18%**
607. **`src/Symfony/Bundle/SecurityBundle/EventListener/FirewallListener.php`** -> AI Confidence: **99.18%**
608. **`src/Symfony/Bundle/SecurityBundle/Tests/Functional/Bundle/CsrfFormLoginBundle/Form/UserLoginType.php`** -> AI Confidence: **99.18%**
609. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/TwigExtensionTest.php`** -> AI Confidence: **99.18%**
610. **`src/Symfony/Bundle/WebProfilerBundle/DependencyInjection/WebProfilerExtension.php`** -> AI Confidence: **99.18%**
611. **`src/Symfony/Bundle/WebProfilerBundle/Twig/WebProfilerExtension.php`** -> AI Confidence: **99.18%**
612. **`src/Symfony/Component/Asset/Tests/PackagesTest.php`** -> AI Confidence: **99.18%**
613. **`src/Symfony/Component/AssetMapper/Command/AssetMapperCompileCommand.php`** -> AI Confidence: **99.18%**
614. **`src/Symfony/Component/AssetMapper/Command/ImportMapInstallCommand.php`** -> AI Confidence: **99.18%**
615. **`src/Symfony/Component/BrowserKit/Tests/AbstractBrowserTest.php`** -> AI Confidence: **99.18%**
616. **`src/Symfony/Component/BrowserKit/Tests/TestHttpClient.php`** -> AI Confidence: **99.18%**
617. **`src/Symfony/Component/Cache/Adapter/ProxyAdapter.php`** -> AI Confidence: **99.18%**
618. **`src/Symfony/Component/Cache/Tests/Adapter/AdapterTestCase.php`** -> AI Confidence: **99.18%**
619. **`src/Symfony/Component/Cache/Tests/Adapter/RedisAdapterTest.php`** -> AI Confidence: **99.18%**
620. **`src/Symfony/Component/Cache/Tests/Adapter/RelayClusterAdapterTest.php`** -> AI Confidence: **99.18%**
621. **`src/Symfony/Component/Cache/Tests/Marshaller/DefaultMarshallerTest.php`** -> AI Confidence: **99.18%**
622. **`src/Symfony/Component/Console/Command/LazyCommand.php`** -> AI Confidence: **99.18%**
623. **`src/Symfony/Component/Console/DataCollector/CommandDataCollector.php`** -> AI Confidence: **99.18%**
624. **`src/Symfony/Component/Console/DependencyInjection/ConsoleArgumentValueResolverPass.php`** -> AI Confidence: **99.18%**
625. **`src/Symfony/Component/Console/Messenger/RunCommandMessageHandler.php`** -> AI Confidence: **99.18%**
626. **`src/Symfony/Component/Console/Tests/Command/HelpCommandTest.php`** -> AI Confidence: **99.18%**
627. **`src/Symfony/Component/Console/Tests/Input/ArrayInputTest.php`** -> AI Confidence: **99.18%**
628. **`src/Symfony/Component/Console/Tests/Input/InputOptionTest.php`** -> AI Confidence: **99.18%**
629. **`src/Symfony/Component/DependencyInjection/Kernel/AbstractBundle.php`** -> AI Confidence: **99.18%**
630. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/ContainerConfigurator.php`** -> AI Confidence: **99.18%**
631. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/ServicesConfigurator.php`** -> AI Confidence: **99.18%**
632. **`src/Symfony/Component/DependencyInjection/Tests/ContainerTest.php`** -> AI Confidence: **99.18%**
633. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/custom_container_class_constructor_without_arguments.php`** -> AI Confidence: **99.18%**
634. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/custom_container_class_with_optional_constructor_arguments.php`** -> AI Confidence: **99.18%**
635. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services12.php`** -> AI Confidence: **99.18%**
636. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services8.php`** -> AI Confidence: **99.18%**
637. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_almost_circular_private.php`** -> AI Confidence: **99.18%**
638. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_array_params.php`** -> AI Confidence: **99.18%**
639. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_deprecated_parameters.php`** -> AI Confidence: **99.18%**
640. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_env_in_id.php`** -> AI Confidence: **99.18%**
641. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_uninitialized_ref.php`** -> AI Confidence: **99.18%**
642. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_unsupported_characters.php`** -> AI Confidence: **99.18%**
643. **`src/Symfony/Component/DomCrawler/Tests/CrawlerTest.php`** -> AI Confidence: **99.18%**
644. **`src/Symfony/Component/Emoji/Tests/EmojiTransliteratorTest.php`** -> AI Confidence: **99.18%**
645. **`src/Symfony/Component/ErrorHandler/Tests/ErrorHandlerTest.php`** -> AI Confidence: **99.18%**
646. **`src/Symfony/Component/ExpressionLanguage/Tests/ExpressionLanguageTest.php`** -> AI Confidence: **99.18%**
647. **`src/Symfony/Component/Finder/Tests/FinderTest.php`** -> AI Confidence: **99.18%**
648. **`src/Symfony/Component/Form/Extension/Core/Type/ChoiceType.php`** -> AI Confidence: **99.18%**
649. **`src/Symfony/Component/Form/Extension/Core/Type/LanguageType.php`** -> AI Confidence: **99.18%**
650. **`src/Symfony/Component/Form/Extension/Core/Type/NumberType.php`** -> AI Confidence: **99.18%**
651. **`src/Symfony/Component/Form/Extension/HtmlSanitizer/Type/TextTypeHtmlSanitizerExtension.php`** -> AI Confidence: **99.18%**
652. **`src/Symfony/Component/Form/Extension/Validator/ValidatorExtension.php`** -> AI Confidence: **99.18%**
653. **`src/Symfony/Component/Form/Extension/Validator/ValidatorTypeGuesser.php`** -> AI Confidence: **99.18%**
654. **`src/Symfony/Component/Form/Flow/FormFlowBuilder.php`** -> AI Confidence: **99.18%**
655. **`src/Symfony/Component/Form/Flow/Type/ButtonFlowType.php`** -> AI Confidence: **99.18%**
656. **`src/Symfony/Component/Form/FormConfigBuilder.php`** -> AI Confidence: **99.18%**
657. **`src/Symfony/Component/Form/Tests/CompoundFormPerformanceTest.php`** -> AI Confidence: **99.18%**
658. **`src/Symfony/Component/Form/Tests/Extension/Core/Type/TimezoneTypeTest.php`** -> AI Confidence: **99.18%**
659. **`src/Symfony/Component/HttpClient/Tests/AsyncDecoratorTraitTest.php`** -> AI Confidence: **99.18%**
660. **`src/Symfony/Component/HttpClient/Tests/HttpClientTestCase.php`** -> AI Confidence: **99.18%**
661. **`src/Symfony/Component/HttpFoundation/Session/Session.php`** -> AI Confidence: **99.18%**
662. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/RequestValueResolver.php`** -> AI Confidence: **99.18%**
663. **`src/Symfony/Component/HttpKernel/Controller/ContainerControllerResolver.php`** -> AI Confidence: **99.18%**
664. **`src/Symfony/Component/HttpKernel/DependencyInjection/ControllerArgumentValueResolverPass.php`** -> AI Confidence: **99.18%**
665. **`src/Symfony/Component/HttpKernel/HttpCache/Ssi.php`** -> AI Confidence: **99.18%**
666. **`src/Symfony/Component/HttpKernel/Tests/EventListener/DebugHandlersListenerTest.php`** -> AI Confidence: **99.18%**
667. **`src/Symfony/Component/HttpKernel/Tests/Fragment/HIncludeFragmentRendererTest.php`** -> AI Confidence: **99.18%**
668. **`src/Symfony/Component/HttpKernel/Tests/Fragment/InlineFragmentRendererTest.php`** -> AI Confidence: **99.18%**
669. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/HttpCacheTest.php`** -> AI Confidence: **99.18%**
670. **`src/Symfony/Component/Intl/Tests/CountriesWithUserAssignedTest.php`** -> AI Confidence: **99.18%**
671. **`src/Symfony/Component/JsonPath/Tests/JsonCrawlerTest.php`** -> AI Confidence: **99.18%**
672. **`src/Symfony/Component/JsonStreamer/DependencyInjection/TransformerPass.php`** -> AI Confidence: **99.18%**
673. **`src/Symfony/Component/JsonStreamer/Mapping/GenericTypePropertyMetadataLoader.php`** -> AI Confidence: **99.18%**
674. **`src/Symfony/Component/Lock/Store/MongoDbStore.php`** -> AI Confidence: **99.18%**
675. **`src/Symfony/Component/Lock/Tests/Store/AbstractRedisStoreTestCase.php`** -> AI Confidence: **99.18%**
676. **`src/Symfony/Component/Lock/Tests/Store/FlockStoreTest.php`** -> AI Confidence: **99.18%**
677. **`src/Symfony/Component/Lock/Tests/Store/MongoDbStoreTest.php`** -> AI Confidence: **99.18%**
678. **`src/Symfony/Component/Lock/Tests/Store/PostgreSqlStoreTest.php`** -> AI Confidence: **99.18%**
679. **`src/Symfony/Component/Mailer/Bridge/Brevo/Webhook/BrevoRequestParser.php`** -> AI Confidence: **99.18%**
680. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Webhook/MailgunRequestParser.php`** -> AI Confidence: **99.18%**
681. **`src/Symfony/Component/Mailer/Bridge/Mailomat/Webhook/MailomatRequestParser.php`** -> AI Confidence: **99.18%**
682. **`src/Symfony/Component/Mailer/Bridge/Postmark/Webhook/PostmarkRequestParser.php`** -> AI Confidence: **99.18%**
683. **`src/Symfony/Component/Mailer/Bridge/Sweego/Tests/Transport/SweegoTransportFactoryTest.php`** -> AI Confidence: **99.18%**
684. **`src/Symfony/Component/Mailer/Tests/Transport/NativeTransportFactoryTest.php`** -> AI Confidence: **99.18%**
685. **`src/Symfony/Component/Mailer/Transport.php`** -> AI Confidence: **99.18%**
686. **`src/Symfony/Component/Messenger/Bridge/AmazonSqs/Transport/AmazonSqsTransport.php`** -> AI Confidence: **99.18%**
687. **`src/Symfony/Component/Messenger/Bridge/Beanstalkd/Transport/BeanstalkdReceiver.php`** -> AI Confidence: **99.18%**
688. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Tests/Transport/DoctrinePostgreSqlFilterIntegrationTest.php`** -> AI Confidence: **99.18%**
689. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineSender.php`** -> AI Confidence: **99.18%**
690. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineTransportFactory.php`** -> AI Confidence: **99.18%**
691. **`src/Symfony/Component/Messenger/Bridge/Redis/Tests/Transport/RedisExtIntegrationTest.php`** -> AI Confidence: **99.18%**
692. **`src/Symfony/Component/Messenger/Bridge/Redis/Tests/Transport/RedisTransportFactoryTest.php`** -> AI Confidence: **99.18%**
693. **`src/Symfony/Component/Messenger/EventListener/SendFailedMessageToFailureTransportListener.php`** -> AI Confidence: **99.18%**
694. **`src/Symfony/Component/Messenger/Transport/Serialization/Serializer.php`** -> AI Confidence: **99.18%**
695. **`src/Symfony/Component/Notifier/Bridge/Bluesky/BlueskyTransportFactory.php`** -> AI Confidence: **99.18%**
696. **`src/Symfony/Component/Notifier/Bridge/Chatwork/Tests/ChatworkTransportFactoryTest.php`** -> AI Confidence: **99.18%**
697. **`src/Symfony/Component/Notifier/Bridge/FakeChat/FakeChatLoggerTransport.php`** -> AI Confidence: **99.18%**
698. **`src/Symfony/Component/Notifier/Bridge/FakeSms/FakeSmsEmailTransport.php`** -> AI Confidence: **99.18%**
699. **`src/Symfony/Component/Notifier/Bridge/GoIp/Tests/GoIpTransportFactoryTest.php`** -> AI Confidence: **99.18%**
700. **`src/Symfony/Component/Notifier/Bridge/KazInfoTeh/Tests/KazInfoTehTransportTest.php`** -> AI Confidence: **99.18%**
701. **`src/Symfony/Component/Notifier/Bridge/LineBot/Tests/LineBotTransportFactoryTest.php`** -> AI Confidence: **99.18%**
702. **`src/Symfony/Component/Notifier/Bridge/LineNotify/LineNotifyTransport.php`** -> AI Confidence: **99.18%**
703. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureTransportFactory.php`** -> AI Confidence: **99.18%**
704. **`src/Symfony/Component/Notifier/Bridge/MicrosoftTeams/MicrosoftTeamsOptions.php`** -> AI Confidence: **99.18%**
705. **`src/Symfony/Component/Notifier/Bridge/Octopush/OctopushTransport.php`** -> AI Confidence: **99.18%**
706. **`src/Symfony/Component/Notifier/Bridge/Sinch/SinchTransport.php`** -> AI Confidence: **99.18%**
707. **`src/Symfony/Component/Notifier/Bridge/Smsbox/SmsboxOptions.php`** -> AI Confidence: **99.18%**
708. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Webhook/SmsboxRequestParser.php`** -> AI Confidence: **99.18%**
709. **`src/Symfony/Component/Notifier/Bridge/Smsc/SmscTransport.php`** -> AI Confidence: **99.18%**
710. **`src/Symfony/Component/Notifier/Bridge/Sweego/Webhook/SweegoRequestParser.php`** -> AI Confidence: **99.18%**
711. **`src/Symfony/Component/Notifier/Bridge/Yunpian/YunpianTransport.php`** -> AI Confidence: **99.18%**
712. **`src/Symfony/Component/PasswordHasher/Tests/Command/UserPasswordHashCommandTest.php`** -> AI Confidence: **99.18%**
713. **`src/Symfony/Component/PropertyInfo/Tests/Fixtures/DummyExtractor.php`** -> AI Confidence: **99.18%**
714. **`src/Symfony/Component/Routing/Tests/RouteTest.php`** -> AI Confidence: **99.18%**
715. **`src/Symfony/Component/Security/Core/Tests/Authorization/Voter/VoterTest.php`** -> AI Confidence: **99.18%**
716. **`src/Symfony/Component/Security/Http/Authenticator/LoginLinkAuthenticator.php`** -> AI Confidence: **99.18%**
717. **`src/Symfony/Component/Security/Http/Controller/SecurityTokenValueResolver.php`** -> AI Confidence: **99.18%**
718. **`src/Symfony/Component/Security/Http/EntryPoint/AuthenticationEntryPointInterface.php`** -> AI Confidence: **99.18%**
719. **`src/Symfony/Component/Security/Http/Event/LoginFailureEvent.php`** -> AI Confidence: **99.18%**
720. **`src/Symfony/Component/Security/Http/EventListener/CheckCredentialsListener.php`** -> AI Confidence: **99.18%**
721. **`src/Symfony/Component/Security/Http/EventListener/LoginThrottlingListener.php`** -> AI Confidence: **99.18%**
722. **`src/Symfony/Component/Security/Http/EventListener/RememberMeListener.php`** -> AI Confidence: **99.18%**
723. **`src/Symfony/Component/Security/Http/Firewall/LogoutListener.php`** -> AI Confidence: **99.18%**
724. **`src/Symfony/Component/Security/Http/Tests/LoginLink/LoginLinkHandlerTest.php`** -> AI Confidence: **99.18%**
725. **`src/Symfony/Component/Serializer/Command/DebugCommand.php`** -> AI Confidence: **99.18%**
726. **`src/Symfony/Component/Serializer/Context/Normalizer/UnwrappingDenormalizerContextBuilder.php`** -> AI Confidence: **99.18%**
727. **`src/Symfony/Component/Translation/Bridge/Loco/LocoProviderFactory.php`** -> AI Confidence: **99.18%**
728. **`src/Symfony/Component/Translation/Bridge/Loco/Tests/LocoProviderFactoryTest.php`** -> AI Confidence: **99.18%**
729. **`src/Symfony/Component/Translation/Tests/Command/XliffLintCommandTest.php`** -> AI Confidence: **99.18%**
730. **`src/Symfony/Component/Uid/Command/GenerateUlidCommand.php`** -> AI Confidence: **99.18%**
731. **`src/Symfony/Component/Uid/Command/InspectUuidCommand.php`** -> AI Confidence: **99.18%**
732. **`src/Symfony/Component/Validator/Command/DebugCommand.php`** -> AI Confidence: **99.18%**
733. **`src/Symfony/Component/Validator/Context/ExecutionContext.php`** -> AI Confidence: **99.18%**
734. **`src/Symfony/Component/Validator/Test/CompoundConstraintTestCase.php`** -> AI Confidence: **99.18%**
735. **`src/Symfony/Component/Validator/Tests/Constraints/UrlValidatorTest.php`** -> AI Confidence: **99.18%**
736. **`src/Symfony/Component/Validator/Tests/Constraints/XmlValidatorTest.php`** -> AI Confidence: **99.18%**
737. **`src/Symfony/Component/Validator/ValidatorBuilder.php`** -> AI Confidence: **99.18%**
738. **`src/Symfony/Component/Yaml/Escaper.php`** -> AI Confidence: **99.18%**
739. **`src/Symfony/Component/Yaml/Tests/Command/LintCommandTest.php`** -> AI Confidence: **99.18%**
740. **`src/Symfony/Bundle/FrameworkBundle/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
741. **`src/Symfony/Component/Cache/Traits/AbstractAdapterTrait.php`** -> AI Confidence: **99.17%**
742. **`src/Symfony/Component/Console/Input/StringInput.php`** -> AI Confidence: **99.17%**
743. **`src/Symfony/Component/DependencyInjection/Attribute/Autoconfigure.php`** -> AI Confidence: **99.17%**
744. **`src/Symfony/Component/DependencyInjection/Kernel/KernelTrait.php`** -> AI Confidence: **99.17%**
745. **`src/Symfony/Component/Emoji/Resources/data/emoji-bs.php`** -> AI Confidence: **99.17%**
746. **`src/Symfony/Component/Emoji/Resources/data/emoji-gd.php`** -> AI Confidence: **99.17%**
747. **`src/Symfony/Component/Emoji/Resources/data/emoji-gl.php`** -> AI Confidence: **99.17%**
748. **`src/Symfony/Component/Emoji/Resources/data/emoji-nn.php`** -> AI Confidence: **99.17%**
749. **`src/Symfony/Component/Emoji/Resources/data/emoji-pt_pt.php`** -> AI Confidence: **99.17%**
750. **`src/Symfony/Component/Emoji/Resources/data/emoji-sk.php`** -> AI Confidence: **99.17%**
751. **`src/Symfony/Component/ErrorHandler/Resources/views/error.html.php`** -> AI Confidence: **99.17%**
752. **`src/Symfony/Component/ExpressionLanguage/SyntaxError.php`** -> AI Confidence: **99.17%**
753. **`src/Symfony/Component/Finder/Comparator/NumberComparator.php`** -> AI Confidence: **99.17%**
754. **`src/Symfony/Component/Finder/Gitignore.php`** -> AI Confidence: **99.17%**
755. **`src/Symfony/Component/Form/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
756. **`src/Symfony/Component/HttpClient/Caching/Freshness.php`** -> AI Confidence: **99.17%**
757. **`src/Symfony/Component/HttpFoundation/ServerBag.php`** -> AI Confidence: **99.17%**
758. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/NativeFileSessionHandler.php`** -> AI Confidence: **99.17%**
759. **`src/Symfony/Component/HttpKernel/Profiler/FileProfilerStorage.php`** -> AI Confidence: **99.17%**
760. **`src/Symfony/Component/HttpKernel/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
761. **`src/Symfony/Component/JsonStreamer/Read/Splitter.php`** -> AI Confidence: **99.17%**
762. **`src/Symfony/Component/JsonStreamer/Tests/Fixtures/Model/DummyWithRepeatedOtherDummy.php`** -> AI Confidence: **99.17%**
763. **`src/Symfony/Component/Mime/CharacterStream.php`** -> AI Confidence: **99.17%**
764. **`src/Symfony/Component/Notifier/Bridge/Lox24/VoiceLanguage.php`** -> AI Confidence: **99.17%**
765. **`src/Symfony/Component/Notifier/Bridge/Pushy/Enum/InterruptionLevel.php`** -> AI Confidence: **99.17%**
766. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Enum/Encoding.php`** -> AI Confidence: **99.17%**
767. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Enum/Strategy.php`** -> AI Confidence: **99.17%**
768. **`src/Symfony/Component/Process/ExecutableFinder.php`** -> AI Confidence: **99.17%**
769. **`src/Symfony/Component/Routing/Matcher/Dumper/StaticPrefixCollection.php`** -> AI Confidence: **99.17%**
770. **`src/Symfony/Component/Routing/Requirement/Requirement.php`** -> AI Confidence: **99.17%**
771. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestIntBackedEnum.php`** -> AI Confidence: **99.17%**
772. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestStringBackedEnum.php`** -> AI Confidence: **99.17%**
773. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestStringBackedEnum2.php`** -> AI Confidence: **99.17%**
774. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestUnitEnum.php`** -> AI Confidence: **99.17%**
775. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher5.php`** -> AI Confidence: **99.17%**
776. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher9.php`** -> AI Confidence: **99.17%**
777. **`src/Symfony/Component/Security/Core/Dumper/MermaidDirection.php`** -> AI Confidence: **99.17%**
778. **`src/Symfony/Component/Translation/Loader/PoFileLoader.php`** -> AI Confidence: **99.17%**
779. **`src/Symfony/Component/Uid/UuidV7.php`** -> AI Confidence: **99.17%**
780. **`src/Symfony/Component/Validator/Constraints/Count.php`** -> AI Confidence: **99.17%**
781. **`src/Symfony/Component/Validator/Constraints/File.php`** -> AI Confidence: **99.17%**
782. **`src/Symfony/Component/Validator/Constraints/Isbn.php`** -> AI Confidence: **99.17%**
783. **`src/Symfony/Component/VarDumper/Cloner/VarCloner.php`** -> AI Confidence: **99.17%**
784. **`src/Symfony/Component/VarDumper/Tests/Fixtures/BackedEnumFixture.php`** -> AI Confidence: **99.17%**
785. **`src/Symfony/Component/VarDumper/Tests/Fixtures/UnitEnumFixture.php`** -> AI Confidence: **99.17%**
786. **`src/Symfony/Component/WebLink/HttpHeaderParser.php`** -> AI Confidence: **99.17%**
787. **`src/Symfony/Component/Yaml/Dumper.php`** -> AI Confidence: **99.17%**
788. **`src/Symfony/Component/Yaml/Parser.php`** -> AI Confidence: **99.17%**
789. **`src/Symfony/Bridge/Doctrine/SchemaListener/AbstractSchemaListener.php`** -> AI Confidence: **99.16%**
790. **`src/Symfony/Bridge/Doctrine/Security/User/EntityUserProvider.php`** -> AI Confidence: **99.16%**
791. **`src/Symfony/Bridge/Doctrine/Tests/DataCollector/DoctrineDataCollectorTest.php`** -> AI Confidence: **99.16%**
792. **`src/Symfony/Bridge/Monolog/Command/ServerLogCommand.php`** -> AI Confidence: **99.16%**
793. **`src/Symfony/Bridge/Monolog/Handler/ConsoleHandler.php`** -> AI Confidence: **99.16%**
794. **`src/Symfony/Bridge/Monolog/Handler/ElasticsearchLogstashHandler.php`** -> AI Confidence: **99.16%**
795. **`src/Symfony/Bridge/Twig/Extension/FormExtension.php`** -> AI Confidence: **99.16%**
796. **`src/Symfony/Bridge/Twig/Extension/SecurityExtension.php`** -> AI Confidence: **99.16%**
797. **`src/Symfony/Bridge/Twig/NodeVisitor/TranslationDefaultDomainNodeVisitor.php`** -> AI Confidence: **99.16%**
798. **`src/Symfony/Bridge/Twig/Tests/Extension/AbstractDivLayoutTestCase.php`** -> AI Confidence: **99.16%**
799. **`src/Symfony/Bundle/FrameworkBundle/CacheWarmer/ValidatorCacheWarmer.php`** -> AI Confidence: **99.16%**
800. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolInvalidateTagsCommand.php`** -> AI Confidence: **99.16%**
801. **`src/Symfony/Bundle/FrameworkBundle/Command/ConfigDebugCommand.php`** -> AI Confidence: **99.16%**
802. **`src/Symfony/Bundle/FrameworkBundle/Command/EventDispatcherDebugCommand.php`** -> AI Confidence: **99.16%**
803. **`src/Symfony/Bundle/FrameworkBundle/Command/RouterDebugCommand.php`** -> AI Confidence: **99.16%**
804. **`src/Symfony/Bundle/FrameworkBundle/Command/RouterMatchCommand.php`** -> AI Confidence: **99.16%**
805. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsRemoveCommand.php`** -> AI Confidence: **99.16%**
806. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsRevealCommand.php`** -> AI Confidence: **99.16%**
807. **`src/Symfony/Bundle/FrameworkBundle/Console/Application.php`** -> AI Confidence: **99.16%**
808. **`src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php`** -> AI Confidence: **99.16%**
809. **`src/Symfony/Bundle/FrameworkBundle/Controller/ControllerHelper.php`** -> AI Confidence: **99.16%**
810. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`** -> AI Confidence: **99.16%**
811. **`src/Symfony/Bundle/FrameworkBundle/EventListener/SuggestMissingPackageSubscriber.php`** -> AI Confidence: **99.16%**
812. **`src/Symfony/Bundle/FrameworkBundle/KernelBrowser.php`** -> AI Confidence: **99.16%**
813. **`src/Symfony/Bundle/FrameworkBundle/Routing/Router.php`** -> AI Confidence: **99.16%**
814. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/ConfigurationTest.php`** -> AI Confidence: **99.16%**
815. **`src/Symfony/Bundle/SecurityBundle/Command/DebugFirewallCommand.php`** -> AI Confidence: **99.16%**
816. **`src/Symfony/Bundle/SecurityBundle/DataCollector/SecurityDataCollector.php`** -> AI Confidence: **99.16%**
817. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/RegisterGlobalSecurityEventListenersPass.php`** -> AI Confidence: **99.16%**
818. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/MainConfiguration.php`** -> AI Confidence: **99.16%**
819. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/Factory/LoginLinkFactory.php`** -> AI Confidence: **99.16%**
820. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/Factory/RememberMeFactory.php`** -> AI Confidence: **99.16%**
821. **`src/Symfony/Bundle/SecurityBundle/Security.php`** -> AI Confidence: **99.16%**
822. **`src/Symfony/Bundle/SecurityBundle/Security/LazyFirewallContext.php`** -> AI Confidence: **99.16%**
823. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/authenticator_manager.php`** -> AI Confidence: **99.16%**
824. **`src/Symfony/Bundle/WebProfilerBundle/Controller/RouterController.php`** -> AI Confidence: **99.16%**
825. **`src/Symfony/Component/AssetMapper/Command/ImportMapOutdatedCommand.php`** -> AI Confidence: **99.16%**
826. **`src/Symfony/Component/AssetMapper/Command/ImportMapRequireCommand.php`** -> AI Confidence: **99.16%**
827. **`src/Symfony/Component/Cache/Adapter/ArrayAdapter.php`** -> AI Confidence: **99.16%**
828. **`src/Symfony/Component/Cache/Tests/Adapter/MemcachedAdapterTest.php`** -> AI Confidence: **99.16%**
829. **`src/Symfony/Component/Cache/Tests/Traits/RedisTraitTest.php`** -> AI Confidence: **99.16%**
830. **`src/Symfony/Component/Config/Definition/Loader/DefinitionFileLoader.php`** -> AI Confidence: **99.16%**
831. **`src/Symfony/Component/Console/Command/TraceableCommand.php`** -> AI Confidence: **99.16%**
832. **`src/Symfony/Component/Console/Tests/Fixtures/InvokableWithInteractiveAttributesTestCommand.php`** -> AI Confidence: **99.16%**
833. **`src/Symfony/Component/Console/Tests/Input/InputArgumentTest.php`** -> AI Confidence: **99.16%**
834. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services19.php`** -> AI Confidence: **99.16%**
835. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services26.php`** -> AI Confidence: **99.16%**
836. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_rot13_env.php`** -> AI Confidence: **99.16%**
837. **`src/Symfony/Component/DomCrawler/Tests/FormTest.php`** -> AI Confidence: **99.16%**
838. **`src/Symfony/Component/ErrorHandler/Command/ErrorDumpCommand.php`** -> AI Confidence: **99.16%**
839. **`src/Symfony/Component/Finder/Finder.php`** -> AI Confidence: **99.16%**
840. **`src/Symfony/Component/Form/Command/DebugCommand.php`** -> AI Confidence: **99.16%**
841. **`src/Symfony/Component/Form/Console/Descriptor/Descriptor.php`** -> AI Confidence: **99.16%**
842. **`src/Symfony/Component/Form/Extension/Core/DataAccessor/PropertyPathAccessor.php`** -> AI Confidence: **99.16%**
843. **`src/Symfony/Component/Form/Extension/Core/Type/CollectionType.php`** -> AI Confidence: **99.16%**
844. **`src/Symfony/Component/Form/Extension/Core/Type/CurrencyType.php`** -> AI Confidence: **99.16%**
845. **`src/Symfony/Component/Form/Extension/Core/Type/FormType.php`** -> AI Confidence: **99.16%**
846. **`src/Symfony/Component/Form/Extension/Core/Type/TimezoneType.php`** -> AI Confidence: **99.16%**
847. **`src/Symfony/Component/Form/Extension/Core/Type/WeekType.php`** -> AI Confidence: **99.16%**
848. **`src/Symfony/Component/Form/Extension/Csrf/Type/FormTypeCsrfExtension.php`** -> AI Confidence: **99.16%**
849. **`src/Symfony/Component/Form/Extension/DataCollector/FormDataCollector.php`** -> AI Confidence: **99.16%**
850. **`src/Symfony/Component/Form/Flow/Type/FormFlowType.php`** -> AI Confidence: **99.16%**
851. **`src/Symfony/Component/Form/Form.php`** -> AI Confidence: **99.16%**
852. **`src/Symfony/Component/Form/FormFactory.php`** -> AI Confidence: **99.16%**
853. **`src/Symfony/Component/Form/Tests/Extension/Core/Type/IntegerTypeTest.php`** -> AI Confidence: **99.16%**
854. **`src/Symfony/Component/HtmlSanitizer/Reference/W3CReference.php`** -> AI Confidence: **99.16%**
855. **`src/Symfony/Component/HttpClient/HttplugClient.php`** -> AI Confidence: **99.16%**
856. **`src/Symfony/Component/HttpClient/Internal/AmpListener.php`** -> AI Confidence: **99.16%**
857. **`src/Symfony/Component/HttpClient/Psr18Client.php`** -> AI Confidence: **99.16%**
858. **`src/Symfony/Component/HttpFoundation/File/UploadedFile.php`** -> AI Confidence: **99.16%**
859. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/VariadicValueResolver.php`** -> AI Confidence: **99.16%**
860. **`src/Symfony/Component/HttpKernel/DataCollector/RequestDataCollector.php`** -> AI Confidence: **99.16%**
861. **`src/Symfony/Component/HttpKernel/EventListener/ErrorListener.php`** -> AI Confidence: **99.16%**
862. **`src/Symfony/Component/HttpKernel/HttpCache/Esi.php`** -> AI Confidence: **99.16%**
863. **`src/Symfony/Component/HttpKernel/HttpCache/HttpCache.php`** -> AI Confidence: **99.16%**
864. **`src/Symfony/Component/HttpKernel/HttpClientKernel.php`** -> AI Confidence: **99.16%**
865. **`src/Symfony/Component/HttpKernel/HttpKernelBrowser.php`** -> AI Confidence: **99.16%**
866. **`src/Symfony/Component/JsonStreamer/Read/StreamReaderGenerator.php`** -> AI Confidence: **99.16%**
867. **`src/Symfony/Component/JsonStreamer/Write/StreamWriterGenerator.php`** -> AI Confidence: **99.16%**
868. **`src/Symfony/Component/Ldap/Security/CheckLdapCredentialsListener.php`** -> AI Confidence: **99.16%**
869. **`src/Symfony/Component/Ldap/Security/LdapUserProvider.php`** -> AI Confidence: **99.16%**
870. **`src/Symfony/Component/Mailer/Bridge/AhaSend/Webhook/AhaSendRequestParser.php`** -> AI Confidence: **99.16%**
871. **`src/Symfony/Component/Mailer/Bridge/Azure/Transport/AzureApiTransport.php`** -> AI Confidence: **99.16%**
872. **`src/Symfony/Component/Mailer/Bridge/Mailchimp/Transport/MandrillHttpTransport.php`** -> AI Confidence: **99.16%**
873. **`src/Symfony/Component/Mailer/Bridge/MailerSend/Webhook/MailerSendRequestParser.php`** -> AI Confidence: **99.16%**
874. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Transport/MailgunHttpTransport.php`** -> AI Confidence: **99.16%**
875. **`src/Symfony/Component/Mailer/Bridge/Mailomat/Transport/MailomatApiTransport.php`** -> AI Confidence: **99.16%**
876. **`src/Symfony/Component/Mailer/Bridge/MicrosoftGraph/Transport/MicrosoftGraphApiTransport.php`** -> AI Confidence: **99.16%**
877. **`src/Symfony/Component/Mailer/Bridge/Postal/Transport/PostalApiTransport.php`** -> AI Confidence: **99.16%**
878. **`src/Symfony/Component/Mailer/Bridge/Resend/Webhook/ResendRequestParser.php`** -> AI Confidence: **99.16%**
879. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Transport/SendgridApiTransport.php`** -> AI Confidence: **99.16%**
880. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Webhook/SendgridRequestParser.php`** -> AI Confidence: **99.16%**
881. **`src/Symfony/Component/Mailer/Bridge/Sweego/Transport/SweegoApiTransport.php`** -> AI Confidence: **99.16%**
882. **`src/Symfony/Component/Mailer/Bridge/Sweego/Webhook/SweegoRequestParser.php`** -> AI Confidence: **99.16%**
883. **`src/Symfony/Component/Mailer/Transport/AbstractTransport.php`** -> AI Confidence: **99.16%**
884. **`src/Symfony/Component/Mailer/Transport/Smtp/SmtpTransport.php`** -> AI Confidence: **99.16%**
885. **`src/Symfony/Component/Messenger/Bridge/Beanstalkd/Transport/Connection.php`** -> AI Confidence: **99.16%**
886. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Tests/Transport/ConnectionTest.php`** -> AI Confidence: **99.16%**
887. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineReceiver.php`** -> AI Confidence: **99.16%**
888. **`src/Symfony/Component/Messenger/Command/AbstractFailedMessagesCommand.php`** -> AI Confidence: **99.16%**
889. **`src/Symfony/Component/Messenger/Command/SetupTransportsCommand.php`** -> AI Confidence: **99.16%**
890. **`src/Symfony/Component/Messenger/Command/StatsCommand.php`** -> AI Confidence: **99.16%**
891. **`src/Symfony/Component/Mime/Address.php`** -> AI Confidence: **99.16%**
892. **`src/Symfony/Component/Mime/Tests/Encoder/QpEncoderTest.php`** -> AI Confidence: **99.16%**
893. **`src/Symfony/Component/Notifier/Bridge/FakeChat/FakeChatTransportFactory.php`** -> AI Confidence: **99.16%**
894. **`src/Symfony/Component/Notifier/Bridge/FakeChat/Tests/FakeChatTransportFactoryTest.php`** -> AI Confidence: **99.16%**
895. **`src/Symfony/Component/Notifier/Bridge/FakeSms/FakeSmsTransportFactory.php`** -> AI Confidence: **99.16%**
896. **`src/Symfony/Component/Notifier/Bridge/FakeSms/Tests/FakeSmsTransportFactoryTest.php`** -> AI Confidence: **99.16%**
897. **`src/Symfony/Component/Notifier/Bridge/FreeMobile/FreeMobileTransport.php`** -> AI Confidence: **99.16%**
898. **`src/Symfony/Component/Notifier/Bridge/GoIp/GoIpTransport.php`** -> AI Confidence: **99.16%**
899. **`src/Symfony/Component/Notifier/Bridge/Iqsms/IqsmsTransport.php`** -> AI Confidence: **99.16%**
900. **`src/Symfony/Component/Notifier/Bridge/JoliNotif/JoliNotifTransport.php`** -> AI Confidence: **99.16%**
901. **`src/Symfony/Component/Notifier/Bridge/LinkedIn/LinkedInTransport.php`** -> AI Confidence: **99.16%**
902. **`src/Symfony/Component/Notifier/Bridge/Mastodon/MastodonTransport.php`** -> AI Confidence: **99.16%**
903. **`src/Symfony/Component/Notifier/Bridge/Matrix/MatrixTransport.php`** -> AI Confidence: **99.16%**
904. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureOptions.php`** -> AI Confidence: **99.16%**
905. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureTransport.php`** -> AI Confidence: **99.16%**
906. **`src/Symfony/Component/Notifier/Bridge/Pushy/PushyTransport.php`** -> AI Confidence: **99.16%**
907. **`src/Symfony/Component/Notifier/Bridge/SmsBiuras/SmsBiurasTransport.php`** -> AI Confidence: **99.16%**
908. **`src/Symfony/Component/Notifier/Bridge/SmsSluzba/SmsSluzbaTransport.php`** -> AI Confidence: **99.16%**
909. **`src/Symfony/Component/Notifier/Bridge/SpotHit/SpotHitTransport.php`** -> AI Confidence: **99.16%**
910. **`src/Symfony/Component/Notifier/Bridge/Zulip/ZulipTransport.php`** -> AI Confidence: **99.16%**
911. **`src/Symfony/Component/Notifier/Tests/Transport/DsnTest.php`** -> AI Confidence: **99.16%**
912. **`src/Symfony/Component/Notifier/Transport/AbstractTransport.php`** -> AI Confidence: **99.16%**
913. **`src/Symfony/Component/PasswordHasher/Command/UserPasswordHashCommand.php`** -> AI Confidence: **99.16%**
914. **`src/Symfony/Component/Process/Tests/ProcessTest.php`** -> AI Confidence: **99.16%**
915. **`src/Symfony/Component/Routing/Generator/UrlGenerator.php`** -> AI Confidence: **99.16%**
916. **`src/Symfony/Component/Routing/Loader/PhpFileLoader.php`** -> AI Confidence: **99.16%**
917. **`src/Symfony/Component/Routing/Route.php`** -> AI Confidence: **99.16%**
918. **`src/Symfony/Component/Routing/Router.php`** -> AI Confidence: **99.16%**
919. **`src/Symfony/Component/Routing/Tests/Matcher/UrlMatcherTest.php`** -> AI Confidence: **99.16%**
920. **`src/Symfony/Component/Security/Http/AccessToken/Oidc/OidcTokenHandler.php`** -> AI Confidence: **99.16%**
921. **`src/Symfony/Component/Security/Http/Authenticator/AbstractPreAuthenticatedAuthenticator.php`** -> AI Confidence: **99.16%**
922. **`src/Symfony/Component/Security/Http/Authenticator/AccessTokenAuthenticator.php`** -> AI Confidence: **99.16%**
923. **`src/Symfony/Component/Security/Http/Authenticator/FormLoginAuthenticator.php`** -> AI Confidence: **99.16%**
924. **`src/Symfony/Component/Security/Http/Authenticator/JsonLoginAuthenticator.php`** -> AI Confidence: **99.16%**
925. **`src/Symfony/Component/Security/Http/Authenticator/RememberMeAuthenticator.php`** -> AI Confidence: **99.16%**
926. **`src/Symfony/Component/Security/Http/Command/OidcTokenGenerateCommand.php`** -> AI Confidence: **99.16%**
927. **`src/Symfony/Component/Security/Http/EventListener/IsGrantedAttributeListener.php`** -> AI Confidence: **99.16%**
928. **`src/Symfony/Component/Security/Http/Firewall/AccessListener.php`** -> AI Confidence: **99.16%**
929. **`src/Symfony/Component/Security/Http/Firewall/SwitchUserListener.php`** -> AI Confidence: **99.16%**
930. **`src/Symfony/Component/Security/Http/LoginLink/LoginLinkHandler.php`** -> AI Confidence: **99.16%**
931. **`src/Symfony/Component/Security/Http/RememberMe/SignatureRememberMeHandler.php`** -> AI Confidence: **99.16%**
932. **`src/Symfony/Component/Serializer/Tests/Encoder/XmlEncoderTest.php`** -> AI Confidence: **99.16%**
933. **`src/Symfony/Component/Translation/Bridge/Phrase/PhraseProviderFactory.php`** -> AI Confidence: **99.16%**
934. **`src/Symfony/Component/Translation/Bridge/Phrase/Tests/PhraseProviderFactoryTest.php`** -> AI Confidence: **99.16%**
935. **`src/Symfony/Component/Translation/Command/TranslationLintCommand.php`** -> AI Confidence: **99.16%**
936. **`src/Symfony/Component/Translation/Command/TranslationPullCommand.php`** -> AI Confidence: **99.16%**
937. **`src/Symfony/Component/Translation/Command/TranslationPushCommand.php`** -> AI Confidence: **99.16%**
938. **`src/Symfony/Component/Translation/Tests/Extractor/PhpAstExtractorTest.php`** -> AI Confidence: **99.16%**
939. **`src/Symfony/Component/Translation/Tests/Provider/DsnTest.php`** -> AI Confidence: **99.16%**
940. **`src/Symfony/Component/Uid/Command/GenerateUuidCommand.php`** -> AI Confidence: **99.16%**
941. **`src/Symfony/Component/Validator/Constraints/IbanValidator.php`** -> AI Confidence: **99.16%**
942. **`src/Symfony/Component/Validator/Tests/Fixtures/ConstraintWithRequiredArgument.php`** -> AI Confidence: **99.16%**
943. **`src/Symfony/Component/Validator/Tests/Util/PropertyPathTest.php`** -> AI Confidence: **99.16%**
944. **`src/Symfony/Component/VarDumper/Resources/bin/var-dump-server`** -> AI Confidence: **99.16%**
945. **`src/Symfony/Component/VarDumper/VarDumper.php`** -> AI Confidence: **99.16%**
946. **`src/Symfony/Component/Workflow/Command/WorkflowDumpCommand.php`** -> AI Confidence: **99.16%**
947. **`src/Symfony/Contracts/HttpClient/Test/HttpClientTestCase.php`** -> AI Confidence: **99.16%**
948. **`src/Symfony/Bridge/Doctrine/DataCollector/DoctrineDataCollector.php`** -> AI Confidence: **99.15%**
949. **`src/Symfony/Bridge/Doctrine/Types/AbstractUidType.php`** -> AI Confidence: **99.15%**
950. **`src/Symfony/Bridge/Doctrine/Validator/Constraints/UniqueEntityValidator.php`** -> AI Confidence: **99.15%**
951. **`src/Symfony/Bridge/Monolog/Processor/DebugProcessor.php`** -> AI Confidence: **99.15%**
952. **`src/Symfony/Bridge/PhpUnit/Extension/EnableClockMockSubscriber.php`** -> AI Confidence: **99.15%**
953. **`src/Symfony/Bridge/PhpUnit/Extension/RegisterClockMockSubscriber.php`** -> AI Confidence: **99.15%**
954. **`src/Symfony/Bridge/PhpUnit/Extension/RegisterDnsMockSubscriber.php`** -> AI Confidence: **99.15%**
955. **`src/Symfony/Bridge/PsrHttpMessage/Factory/HttpFoundationFactory.php`** -> AI Confidence: **99.15%**
956. **`src/Symfony/Bridge/Twig/AppVariable.php`** -> AI Confidence: **99.15%**
957. **`src/Symfony/Bridge/Twig/DataCollector/TwigDataCollector.php`** -> AI Confidence: **99.15%**
958. **`src/Symfony/Bridge/Twig/Extension/DumpExtension.php`** -> AI Confidence: **99.15%**
959. **`src/Symfony/Bridge/Twig/Mime/BodyRenderer.php`** -> AI Confidence: **99.15%**
960. **`src/Symfony/Bridge/Twig/Mime/NotificationEmail.php`** -> AI Confidence: **99.15%**
961. **`src/Symfony/Bridge/Twig/Tests/Extension/HttpFoundationExtensionTest.php`** -> AI Confidence: **99.15%**
962. **`src/Symfony/Bridge/Twig/TokenParser/TransTokenParser.php`** -> AI Confidence: **99.15%**
963. **`src/Symfony/Bridge/Twig/UndefinedCallableHandler.php`** -> AI Confidence: **99.15%**
964. **`src/Symfony/Bundle/FrameworkBundle/CacheWarmer/SerializerCacheWarmer.php`** -> AI Confidence: **99.15%**
965. **`src/Symfony/Bundle/FrameworkBundle/Command/AboutCommand.php`** -> AI Confidence: **99.15%**
966. **`src/Symfony/Bundle/FrameworkBundle/Command/CacheWarmupCommand.php`** -> AI Confidence: **99.15%**
967. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsEncryptFromLocalCommand.php`** -> AI Confidence: **99.15%**
968. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsGenerateKeysCommand.php`** -> AI Confidence: **99.15%**
969. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Compiler/ContainerBuilderDebugDumpPass.php`** -> AI Confidence: **99.15%**
970. **`src/Symfony/Bundle/FrameworkBundle/Tests/Controller/RedirectControllerTest.php`** -> AI Confidence: **99.15%**
971. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/CachePoolsTest.php`** -> AI Confidence: **99.15%**
972. **`src/Symfony/Bundle/FrameworkBundle/Translation/Translator.php`** -> AI Confidence: **99.15%**
973. **`src/Symfony/Component/Asset/Tests/UrlPackageTest.php`** -> AI Confidence: **99.15%**
974. **`src/Symfony/Component/AssetMapper/Command/VersionProblemCommandTrait.php`** -> AI Confidence: **99.15%**
975. **`src/Symfony/Component/Cache/DependencyInjection/CacheCollectorPass.php`** -> AI Confidence: **99.15%**
976. **`src/Symfony/Component/Cache/Tests/Adapter/RedisClusterAdapterTest.php`** -> AI Confidence: **99.15%**
977. **`src/Symfony/Component/Config/Definition/BaseNode.php`** -> AI Confidence: **99.15%**
978. **`src/Symfony/Component/Config/Definition/Builder/NodeDefinition.php`** -> AI Confidence: **99.15%**
979. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/UidValueResolver.php`** -> AI Confidence: **99.15%**
980. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/VariadicValueResolver.php`** -> AI Confidence: **99.15%**
981. **`src/Symfony/Component/Console/Tests/Fixtures/InvokableWithInputTestCommand.php`** -> AI Confidence: **99.15%**
982. **`src/Symfony/Component/Console/Tests/Helper/ProcessHelperTest.php`** -> AI Confidence: **99.15%**
983. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/AbstractConfigurator.php`** -> AI Confidence: **99.15%**
984. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_base64_env.php`** -> AI Confidence: **99.15%**
985. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_csv_env.php`** -> AI Confidence: **99.15%**
986. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_default_env.php`** -> AI Confidence: **99.15%**
987. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_json_env.php`** -> AI Confidence: **99.15%**
988. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_nonempty_parameters.php`** -> AI Confidence: **99.15%**
989. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_query_string_env.php`** -> AI Confidence: **99.15%**
990. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_url_env.php`** -> AI Confidence: **99.15%**
991. **`src/Symfony/Component/DependencyInjection/Tests/ParameterBag/ParameterBagTest.php`** -> AI Confidence: **99.15%**
992. **`src/Symfony/Component/ErrorHandler/Exception/FlattenException.php`** -> AI Confidence: **99.15%**
993. **`src/Symfony/Component/ErrorHandler/Tests/ErrorEnhancer/ClassNotFoundErrorEnhancerTest.php`** -> AI Confidence: **99.15%**
994. **`src/Symfony/Component/Form/DependencyInjection/FormPass.php`** -> AI Confidence: **99.15%**
995. **`src/Symfony/Component/Form/Extension/Core/Type/ColorType.php`** -> AI Confidence: **99.15%**
996. **`src/Symfony/Component/Form/Extension/DependencyInjection/DependencyInjectionExtension.php`** -> AI Confidence: **99.15%**
997. **`src/Symfony/Component/Form/Extension/PasswordHasher/EventListener/PasswordHasherListener.php`** -> AI Confidence: **99.15%**
998. **`src/Symfony/Component/Form/ResolvedFormType.php`** -> AI Confidence: **99.15%**
999. **`src/Symfony/Component/HttpClient/Internal/AmpBody.php`** -> AI Confidence: **99.15%**
1000. **`src/Symfony/Component/HttpClient/TraceableHttpClient.php`** -> AI Confidence: **99.15%**
1001. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MongoDbSessionHandler.php`** -> AI Confidence: **99.15%**
1002. **`src/Symfony/Component/HttpFoundation/Tests/UrlHelperTest.php`** -> AI Confidence: **99.15%**
1003. **`src/Symfony/Component/HttpKernel/DataCollector/ConfigDataCollector.php`** -> AI Confidence: **99.15%**
1004. **`src/Symfony/Component/HttpKernel/DependencyInjection/ResettableServicePass.php`** -> AI Confidence: **99.15%**
1005. **`src/Symfony/Component/HttpKernel/EventListener/ControllerAttributesListener.php`** -> AI Confidence: **99.15%**
1006. **`src/Symfony/Component/HttpKernel/EventListener/LocaleListener.php`** -> AI Confidence: **99.15%**
1007. **`src/Symfony/Component/HttpKernel/Fragment/FragmentHandler.php`** -> AI Confidence: **99.15%**
1008. **`src/Symfony/Component/HttpKernel/Fragment/InlineFragmentRenderer.php`** -> AI Confidence: **99.15%**
1009. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/HttpCacheTestCase.php`** -> AI Confidence: **99.15%**
1010. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/TestHttpKernel.php`** -> AI Confidence: **99.15%**
1011. **`src/Symfony/Component/Intl/Data/Generator/LocaleDataGenerator.php`** -> AI Confidence: **99.15%**
1012. **`src/Symfony/Component/Intl/Tests/CountriesTest.php`** -> AI Confidence: **99.15%**
1013. **`src/Symfony/Component/JsonPath/Tests/Functions/CustomFunctionTest.php`** -> AI Confidence: **99.15%**
1014. **`src/Symfony/Component/JsonStreamer/CacheWarmer/StreamerCacheWarmer.php`** -> AI Confidence: **99.15%**
1015. **`src/Symfony/Component/Lock/Store/PdoStore.php`** -> AI Confidence: **99.15%**
1016. **`src/Symfony/Component/Lock/Store/ZookeeperStore.php`** -> AI Confidence: **99.15%**
1017. **`src/Symfony/Component/Mailer/Bridge/AhaSend/Transport/AhaSendSmtpTransport.php`** -> AI Confidence: **99.15%**
1018. **`src/Symfony/Component/Mailer/Bridge/MailPace/Transport/MailPaceSmtpTransport.php`** -> AI Confidence: **99.15%**
1019. **`src/Symfony/Component/Mailer/Bridge/Mailchimp/Webhook/MailchimpRequestParser.php`** -> AI Confidence: **99.15%**
1020. **`src/Symfony/Component/Mailer/Bridge/Mailtrap/Transport/MailtrapSmtpTransport.php`** -> AI Confidence: **99.15%**
1021. **`src/Symfony/Component/Mailer/Bridge/MicrosoftGraph/Transport/MicrosoftGraphTransportFactory.php`** -> AI Confidence: **99.15%**
1022. **`src/Symfony/Component/Mailer/Bridge/Postmark/Transport/PostmarkSmtpTransport.php`** -> AI Confidence: **99.15%**
1023. **`src/Symfony/Component/Mailer/Mailer.php`** -> AI Confidence: **99.15%**
1024. **`src/Symfony/Component/Mailer/Transport/AbstractHttpTransport.php`** -> AI Confidence: **99.15%**
1025. **`src/Symfony/Component/Mailer/Transport/RoundRobinTransport.php`** -> AI Confidence: **99.15%**
1026. **`src/Symfony/Component/Messenger/Bridge/AmazonSqs/Transport/AmazonSqsReceiver.php`** -> AI Confidence: **99.15%**
1027. **`src/Symfony/Component/Messenger/Bridge/Doctrine/EventListener/PostgreSqlNotifyOnIdleListener.php`** -> AI Confidence: **99.15%**
1028. **`src/Symfony/Component/Messenger/Command/DebugCommand.php`** -> AI Confidence: **99.15%**
1029. **`src/Symfony/Component/Messenger/Middleware/DecodeFailedMessageMiddleware.php`** -> AI Confidence: **99.15%**
1030. **`src/Symfony/Component/Messenger/Transport/InMemory/InMemoryTransport.php`** -> AI Confidence: **99.15%**
1031. **`src/Symfony/Component/Mime/Email.php`** -> AI Confidence: **99.15%**
1032. **`src/Symfony/Component/Notifier/Bridge/Brevo/BrevoTransport.php`** -> AI Confidence: **99.15%**
1033. **`src/Symfony/Component/Notifier/Bridge/Chatwork/ChatworkTransport.php`** -> AI Confidence: **99.15%**
1034. **`src/Symfony/Component/Notifier/Bridge/Clickatell/ClickatellTransport.php`** -> AI Confidence: **99.15%**
1035. **`src/Symfony/Component/Notifier/Bridge/Discord/DiscordBotTransport.php`** -> AI Confidence: **99.15%**
1036. **`src/Symfony/Component/Notifier/Bridge/Discord/DiscordTransport.php`** -> AI Confidence: **99.15%**
1037. **`src/Symfony/Component/Notifier/Bridge/FakeChat/FakeChatEmailTransport.php`** -> AI Confidence: **99.15%**
1038. **`src/Symfony/Component/Notifier/Bridge/FortySixElks/FortySixElksTransport.php`** -> AI Confidence: **99.15%**
1039. **`src/Symfony/Component/Notifier/Bridge/GatewayApi/GatewayApiTransport.php`** -> AI Confidence: **99.15%**
1040. **`src/Symfony/Component/Notifier/Bridge/Infobip/InfobipTransport.php`** -> AI Confidence: **99.15%**
1041. **`src/Symfony/Component/Notifier/Bridge/LightSms/LightSmsTransport.php`** -> AI Confidence: **99.15%**
1042. **`src/Symfony/Component/Notifier/Bridge/LineBot/LineBotTransport.php`** -> AI Confidence: **99.15%**
1043. **`src/Symfony/Component/Notifier/Bridge/Lox24/Tests/Lox24TransportFactoryTest.php`** -> AI Confidence: **99.15%**
1044. **`src/Symfony/Component/Notifier/Bridge/Mailjet/MailjetTransport.php`** -> AI Confidence: **99.15%**
1045. **`src/Symfony/Component/Notifier/Bridge/MessageBird/MessageBirdTransport.php`** -> AI Confidence: **99.15%**
1046. **`src/Symfony/Component/Notifier/Bridge/MicrosoftTeams/MicrosoftTeamsTransport.php`** -> AI Confidence: **99.15%**
1047. **`src/Symfony/Component/Notifier/Bridge/Novu/NovuTransport.php`** -> AI Confidence: **99.15%**
1048. **`src/Symfony/Component/Notifier/Bridge/OrangeSms/OrangeSmsTransport.php`** -> AI Confidence: **99.15%**
1049. **`src/Symfony/Component/Notifier/Bridge/OvhCloud/OvhCloudTransport.php`** -> AI Confidence: **99.15%**
1050. **`src/Symfony/Component/Notifier/Bridge/PagerDuty/PagerDutyTransport.php`** -> AI Confidence: **99.15%**
1051. **`src/Symfony/Component/Notifier/Bridge/Pushover/PushoverTransport.php`** -> AI Confidence: **99.15%**
1052. **`src/Symfony/Component/Notifier/Bridge/Redlink/RedlinkTransport.php`** -> AI Confidence: **99.15%**
1053. **`src/Symfony/Component/Notifier/Bridge/Sendberry/SendberryTransport.php`** -> AI Confidence: **99.15%**
1054. **`src/Symfony/Component/Notifier/Bridge/Sevenio/SevenIoTransport.php`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/Symfony/Component/Intl/Resources/data/timezones/km.php` -> **4.8584%** Exposure
- `src/Symfony/Component/Intl/Resources/data/timezones/lo.php` -> **2.3793%** Exposure
- `src/Symfony/Component/HtmlSanitizer/Tests/TextSanitizer/UrlSanitizerTest.php` -> **0.0532%** Exposure
- `src/Symfony/Component/Emoji/Resources/data/emoji-fa.php` -> **0.033%** Exposure
- `src/Symfony/Component/Emoji/Resources/data/emoji-lo.php` -> **0.0051%** Exposure
### Exploit Generation Surface
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ContainerAwareEventManager.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/DataCollector/DoctrineDataCollector.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/DependencyInjection/CompilerPass/RegisterEventListenersAndSubscribersPass.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/Symfony/Bridge/Doctrine/Attribute/MapEntity.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/PhpUnit/bin/simple-phpunit.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Twig/Tests/Command/DebugCommandTest.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Twig/Tests/Command/LintCommandTest.php` -> **100.0%** Exposure
- `src/Symfony/Bundle/FrameworkBundle/Routing/Router.php` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `src/Symfony/Component/Mailer/Bridge/Sendgrid/Tests/Webhook/SendgridSignedRequestParserTest.php` -> **100.0%** Exposure
- `src/Symfony/Component/Mailer/Tests/EventListener/DkimSignedMessageListenerTest.php` -> **99.9795%** Exposure
- `src/Symfony/Component/Security/Core/Tests/Authentication/Token/AbstractTokenTest.php` -> **98.9215%** Exposure
- `src/Symfony/Component/Mime/Tests/Crypto/DkimSignerTest.php` -> **93.201%** Exposure
### Algorithmic DoS Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolverTrait.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/Attribute/MapEntity.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/CacheWarmer/ProxyCacheWarmer.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `182` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `42752` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Symfony/Component/HttpClient/Internal/AmpResolver.php` (PHP) -> Cumulative Risk: **1013.32**
- **Archetype:** `file_cluster_4` (Distance: 13.075 IQR)
- **Magnitude:** 150.14 | **LOC:** 65 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolve` (Impact: 72.8), `query` (Impact: 28.8), `__construct` (Impact: 2.8)

### 2. `src/Symfony/Component/HttpClient/Internal/AmpListener.php` (PHP) -> Cumulative Risk: **907.27**
- **Archetype:** `file_cluster_13` (Distance: 12.292 IQR)
- **Magnitude:** 281.94 | **LOC:** 230 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `requestHeaderStart` (Impact: 96.2), `requestStart` (Impact: 20.6), `connectionAcquired` (Impact: 8.6)

### 3. `src/Symfony/Component/Emoji/Resources/bin/build.php` (PHP) -> Cumulative Risk: **901.66**
- **Archetype:** `file_cluster_4` (Distance: 13.236 IQR)
- **Magnitude:** 483.98 | **LOC:** 263 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `buildRules` (Impact: 87.2), `saveRules` (Impact: 67.3), `getEmojisCodePoints` (Impact: 44.6)

### 4. `src/Symfony/Component/HttpClient/Response/AsyncResponse.php` (PHP) -> Cumulative Risk: **868.43**
- **Archetype:** `file_cluster_13` (Distance: 13.353 IQR)
- **Magnitude:** 944.56 | **LOC:** 504 | **CtrlFlow:** 55.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `stream` (Impact: 381.4), `__construct` (Impact: 156.6), `getInfo` (Impact: 98.8)

### 5. `src/Symfony/Component/Runtime/Internal/ComposerPlugin.php` (PHP) -> Cumulative Risk: **859.98**
- **Archetype:** `file_cluster_13` (Distance: 12.605 IQR)
- **Magnitude:** 165.36 | **LOC:** 123 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `updateAutoloadFile` (Impact: 80.8), `getSubscribedEvents` (Impact: 7.4), `activate` (Impact: 2.9)

### 6. `src/Symfony/Component/HttpClient/Internal/AmpClientState.php` (PHP) -> Cumulative Risk: **849.79**
- **Archetype:** `file_cluster_13` (Distance: 13.145 IQR)
- **Magnitude:** 476.68 | **LOC:** 205 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `request` (Impact: 240.1), `getClient` (Impact: 87.9), `__construct` (Impact: 15.1)

### 7. `src/Symfony/Component/JsonStreamer/Read/PhpGenerator.php` (PHP) -> Cumulative Risk: **841.91**
- **Archetype:** `file_cluster_13` (Distance: 14.025 IQR)
- **Magnitude:** 1184.46 | **LOC:** 376 | **CtrlFlow:** 39.9% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `generateProviders` (Impact: 694.0), `canBeDecodedWithJsonDecode` (Impact: 95.2), `generateCompositeNodeItemCondition` (Impact: 72.2)

### 8. `src/Symfony/Component/VarDumper/Server/DumpServer.php` (PHP) -> Cumulative Risk: **831.32**
- **Archetype:** `file_cluster_4` (Distance: 12.668 IQR)
- **Magnitude:** 181.68 | **LOC:** 110 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `listen` (Impact: 66.5), `getMessages` (Impact: 32.3), `start` (Impact: 14.2)

### 9. `src/Symfony/Component/VarDumper/Caster/ReflectionCaster.php` (PHP) -> Cumulative Risk: **827.22**
- **Archetype:** `file_cluster_11` (Distance: 12.942 IQR)
- **Magnitude:** 932.3 | **LOC:** 444 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `castFunctionAbstract` (Impact: 171.9), `getSignature` (Impact: 170.6), `castParameter` (Impact: 109.3)

### 10. `src/Symfony/Bundle/FrameworkBundle/Command/AbstractConfigCommand.php` (PHP) -> Cumulative Risk: **826.76**
- **Archetype:** `file_cluster_13` (Distance: 12.966 IQR)
- **Magnitude:** 335.16 | **LOC:** 190 | **CtrlFlow:** 51.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `findExtension` (Impact: 123.2), `listNonBundleExtensions` (Impact: 46.9), `listBundles` (Impact: 25.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.027 IQR)
- **Top Global Matches:** file_cluster_13: 15.027, file_cluster_8: 15.152, file_cluster_11: 15.239
- **Magnitude:** 7838.22 | **LOC:** 2439 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 74
- **Risk Profile:** Cognitive Load (81.9046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dumpValue` (Impact: 929.5 | O(2^N) | DB: 45)
  * `dump` (Impact: 602.5 | O(N^6) | DB: 74)
  * `collectCircularReferences` (Impact: 465.9 | O(2^N) | DB: 25)
  * `addService` (Impact: 376.2 | O(N^6) | DB: 62)
  * `addNewInstance` (Impact: 333.6 | O(N^5) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 785`, `structural_boundaries: 558`, `args: 60`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1747`
* *Architecture:* `api: 12`, `concurrency: 12`, `import: 48`
* *Defense:* `safety: 128`, `doc: 30`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` \$this->containerDir.\\DIRECTORY_SEPARATOR.'removed-ids.php'", Composer\Autoload\ClassLoader, = true, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\ContainerInterface, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, '.\$class.'.php', Symfony\Component\DependencyInjection\Exception\EnvParameterException...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/ErrorHandler/DebugClassLoader.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.683 IQR)
- **Top Global Matches:** file_cluster_13: 14.683, file_cluster_11: 14.798, file_cluster_8: 14.83
- **Magnitude:** 7506.32 | **LOC:** 1407 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 260
- **Risk Profile:** Cognitive Load (66.0524%), Tech Debt (10.6974%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 6720.8 | O(2^N) | DB: 260)
    * *Intent:* /** * Autoloader checking if the class is really defined in the file found. * * The ClassLoader will...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 369`, `args: 20`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 760`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 19`
* *Defense:* `safety: 92`, `doc: 30`, `test: 17`, `immutability_locks: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.335
  * `Choke Point (Betweenness):` 0.000254 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` $parameterName, Prophecy\Prophecy\ProphecySubjectInterface, ?string $parent): array
    
        $ownInterfaces = class_implements($class, $file, Psr\Log\LogLevel, ProxyManager\Proxy\ProxyInterface, not defining it is deprecated.', Composer\InstalledVersions...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.128 IQR)
- **Top Global Matches:** file_cluster_13: 14.128, file_cluster_8: 14.271, file_cluster_11: 14.415
- **Magnitude:** 4982.84 | **LOC:** 936 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (85.4244%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseDefinition` (Impact: 3373.0 | O(2^N) | DB: 64)
  * `resolveServices` (Impact: 636.8 | O(2^N) | DB: 36)
  * `parseDefaults` (Impact: 136.5 | O(N^6) | DB: 9)
  * `parseCallable` (Impact: 122.7 | O(N^5))
  * `parseDefinitions` (Impact: 67.8 | O(N^5) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 194`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 380`
* *Architecture:* `api: 25`, `import: 19`
* *Defense:* `safety: 118`, `doc: 7`, `test: 1`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Symfony\Component\DependencyInjection\Reference, Symfony\Component\DependencyInjection\Exception\LogicException, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\Yaml\Tag\TaggedValue, Symfony\Component\VarExporter\DeepCloner, Symfony\Component\DependencyInjection\ContainerBuilder, Symfony\Component\DependencyInjection\Definition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/VarDumper/Dumper/HtmlDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.866 IQR)
- **Top Global Matches:** file_cluster_8: 13.866, file_cluster_13: 14.039, file_cluster_0: 14.154
- **Magnitude:** 4540.68 | **LOC:** 979 | **CtrlFlow:** 60.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (66.9013%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 62`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 260`
* *Architecture:* `io: 2`, `api: 14`, `import: 2`
* *Defense:* `safety: 25`, `doc: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Symfony\Component\VarDumper\Cloner\Cursor, Symfony\Component\VarDumper\Cloner\Data
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/JsonPath/JsonCrawler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.054 IQR)
- **Top Global Matches:** file_cluster_8: 14.054, file_cluster_13: 14.076, file_cluster_17: 14.24
- **Magnitude:** 4251.24 | **LOC:** 1174 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (81.7997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `evaluateBracket` (Impact: 1457.4 | O(2^N) | DB: 59)
  * `evaluateFilterExpression` (Impact: 284.2 | O(2^N) | DB: 13)
  * `evaluate` (Impact: 269.4 | O(2^N) | DB: 15)
    * *Intent:* /** * @param resource|string $raw * @param ContainerInterface|ServiceProviderInterface<callable(mixe...
  * `evaluateFunction` (Impact: 208.8 | O(N^4) | DB: 12)
  * `validateFilterExpression` (Impact: 194.8 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 217`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 653`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 57`, `doc: 6`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` s exactly %d argument(s).', json-streamer".', Symfony\Component\JsonPath\Tokenizer\JsonPathToken, Symfony\Component\JsonPath\Exception\InvalidJsonPathException, $name, Symfony\Component\JsonPath\Tokenizer\TokenType, Symfony\Component\JsonStreamer\Exception\UnexpectedValueException, $expectedArgCount)...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Yaml/Parser.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.174 IQR)
- **Top Global Matches:** file_cluster_8: 14.174, file_cluster_13: 14.33, file_cluster_7: 14.436
- **Magnitude:** 3500.82 | **LOC:** 1280 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 74
- **Risk Profile:** Cognitive Load (71.6231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doParse` (Impact: 1117.7 | O(N^6) | DB: 74)
    * *Intent:* /** * Parses a YAML string to a PHP value. * * @param string $value A YAML string * @param int-mask-...
  * `parseValue` (Impact: 348.5 | O(N^6) | DB: 23)
  * `getNextEmbedBlock` (Impact: 259.4 | O(N^6) | DB: 21)
  * `lexInlineQuotedString` (Impact: 200.3 | O(N^6) | DB: 25)
  * `parseBlockScalar` (Impact: 191.2 | O(N^5) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 149`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 782`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 8`, `import: 3`
* *Defense:* `safety: 57`, `doc: 29`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.156
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Symfony\Component\Yaml\Tag\TaggedValue, Symfony\Component\Yaml\Exception\ParseException
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.228 IQR)
- **Top Global Matches:** file_cluster_13: 13.228, file_cluster_8: 13.609, file_cluster_11: 13.89
- **Magnitude:** 3209.68 | **LOC:** 3589 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (76.4498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 1531.1 | O(2^N) | DB: 13)
  * `registerWorkflowConfiguration` (Impact: 268.9 | O(N^6) | DB: 30)
  * `registerHtmlSanitizerConfiguration` (Impact: 124.3 | O(N^5) | DB: 9)
  * `registerSessionConfiguration` (Impact: 98.5 | O(N^5) | DB: 2)
  * `registerRouterConfiguration` (Impact: 89.1 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 720`, `args: 45`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 391`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 235`
* *Defense:* `safety: 51`, `doc: 4`, `test: 16`, `sync_locks: 28`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 190):` serializer-pack".', Symfony\Component\Translation\LocaleSwitcher, Symfony\Component\Config\FileLocator, Symfony\Component\ObjectMapper\Attribute\Map, Symfony\Component\Config\Loader\LoaderInterface, semaphore".', Symfony\Component\RateLimiter\CompoundRateLimiterFactory, asset".'...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.34 IQR)
- **Top Global Matches:** file_cluster_13: 14.34, file_cluster_8: 14.758, file_cluster_11: 14.772
- **Magnitude:** 2985.8 | **LOC:** 1837 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (48.0937%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createService` (Impact: 1066.3 | O(2^N) | DB: 40)
  * `doResolveServices` (Impact: 395.2 | O(2^N) | DB: 19)
  * `resolveEnvPlaceholders` (Impact: 338.9 | O(2^N) | DB: 17)
  * `getEnv` (Impact: 81.4 | O(2^N) | DB: 5)
    * *Intent:* /** * Deprecates a service container parameter. *
  * `willBeAvailable` (Impact: 66.5 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 245`, `args: 49`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 372`
* *Architecture:* `api: 56`, `concurrency: 6`, `import: 41`
* *Defense:* `safety: 63`, `doc: 100`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.706
  * `Choke Point (Betweenness):` 0.000799 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` Symfony\Component\ExpressionLanguage\ExpressionFunctionProviderInterface, Composer\Autoload\ClassLoader, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\Compiler\CompilerPassInterface, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\Config\Resource\GlobResource, Symfony\Component\DependencyInjection\Argument\ServiceLocator, Symfony\Component\DependencyInjection\Compiler\ResolveEnvPlaceholdersPass...
  * `Imported By (In-Degree: 423):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpClient/HttpClientTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.922 IQR)
- **Top Global Matches:** file_cluster_4: 14.922, file_cluster_13: 14.946, file_cluster_11: 14.984
- **Magnitude:** 2703.52 | **LOC:** 866 | **CtrlFlow:** 71.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 64
- **Risk Profile:** Cognitive Load (61.8054%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepareRequest` (Impact: 530.5 | O(N^6) | DB: 16)
    * *Intent:* /** * Provides the common logic from writing HttpClientInterface implementations. * * All private me...
  * `normalizeBody` (Impact: 445.1 | O(N^6) | DB: 64)
  * `mergeDefaultOptions` (Impact: 256.4 | O(N^5) | DB: 18)
  * `resolveUrl` (Impact: 248.2 | O(N^6) | DB: 4)
  * `parseUrl` (Impact: 238.4 | O(N^4) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 132`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 473`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 5`, `concurrency: 18`, `import: 6`
* *Defense:* `safety: 105`, `doc: 24`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Symfony\Component\HttpClient\Response\StreamableInterface, Symfony\Component\HttpClient\Exception\TransportException, polyfill-intl-idn".', Symfony\Component\Mime\MimeTypes, Symfony\Component\HttpClient\Exception\InvalidArgumentException, $host), Symfony\Component\HttpClient\Response\StreamWrapper
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Application.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.62 IQR)
- **Top Global Matches:** file_cluster_13: 14.62, file_cluster_11: 14.946, file_cluster_17: 14.954
- **Magnitude:** 2686.1 | **LOC:** 1422 | **CtrlFlow:** 52.3% | **Authorship Centralization:** 14.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (47.2973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doRunCommand` (Impact: 230.1 | O(N^6) | DB: 21)
  * `doRenderThrowable` (Impact: 195.8 | O(N^5) | DB: 26)
  * `run` (Impact: 186.4 | O(N^5) | DB: 17)
  * `find` (Impact: 185.8 | O(N^5) | DB: 31)
  * `doRun` (Impact: 168.8 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 280`, `args: 69`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 663`, `dead_code: 3`
* *Architecture:* `api: 61`, `import: 46`
* *Defense:* `safety: 80`, `doc: 58`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` '', Symfony\Component\Console\Style\SymfonyStyle, Symfony\Component\Console\CommandLoader\CommandLoaderInterface, Symfony\Component\Console\Input\InputAwareInterface, Symfony\Component\Console\Helper\FormatterHelper, Symfony\Component\Console\Event\ConsoleSignalEvent, Symfony\Component\Console\Helper\ProcessHelper, Symfony\Component\Console\Output\ConsoleOutputInterface...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/SecurityBundle/DependencyInjection/SecurityExtension.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.045 IQR)
- **Top Global Matches:** file_cluster_13: 13.045, file_cluster_8: 13.336, file_cluster_17: 13.453
- **Magnitude:** 2256.38 | **LOC:** 1125 | **CtrlFlow:** 41.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (73.1806%), Tech Debt (8.4486%)
**Top Internal Functions/Classes:**
  * `createHasher` (Impact: 365.0 | O(2^N) | DB: 2)
  * `createFirewall` (Impact: 335.2 | O(N^5) | DB: 37)
    * *Intent:* ;
  * `load` (Impact: 223.2 | O(2^N) | DB: 4)
    * *Intent:* /** @var AuthenticatorFactoryInterface[] */
  * `createRequestMatcher` (Impact: 198.9 | O(N^5) | DB: 16)
  * `createAuthenticationListeners` (Impact: 151.2 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 314`, `args: 30`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 359`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 7`, `import: 55`
* *Defense:* `safety: 54`, `doc: 10`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.078
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 49):` Symfony\Component\Security\Core\Authorization\Strategy\AffirmativeStrategy, Symfony\Component\HttpFoundation\RequestMatcher\PortRequestMatcher, Symfony\Component\Config\FileLocator, Symfony\Component\PasswordHasher\Hasher\NativePasswordHasher, Symfony\Component\HttpFoundation\RequestMatcher\MethodRequestMatcher, Symfony\Component\Security\Http\Event\CheckPassportEvent, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\HttpFoundation\RequestMatcher\PathRequestMatcher...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Tests/Helper/ProgressBarTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.855 IQR)
- **Top Global Matches:** file_cluster_8: 13.855, file_cluster_13: 14.078, file_cluster_4: 14.195
- **Magnitude:** 2253.74 | **LOC:** 1396 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^4) | **DB Complexity:** 103
- **Risk Profile:** Cognitive Load (87.0649%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testParallelBars` (Impact: 15.9 | O(N^4) | DB: 103)
  * `testOverwriteWithSectionOutputWithNewlin` (Impact: 11.7 | O(N^3) | DB: 4)
  * `testAnsiColorsAndEmojis` (Impact: 11.6 | O(N^4) | DB: 9)
  * `testOverwritWithNewlinesInMessage` (Impact: 11.4 | O(N^3) | DB: 2)
  * `testNonDecoratedOutput` (Impact: 8.3 | O(N^3) | DB: 75)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 200`, `args: 76`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1809`, `duplicate_logic: 2`, `orphaned_logic: 67`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 8`, `doc: 1`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` PHPUnit\Framework\TestCase, PHPUnit\Framework\Attributes\Group, Symfony\Component\Console\Output\ConsoleSectionOutput, Symfony\Component\Console\Output\StreamOutput, Symfony\Component\Console\Exception\LogicException, Symfony\Component\Console\Helper\ProgressBar, PHPUnit\Framework\Attributes\DataProvider, Symfony\Component\Console\Helper\Helper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.148 IQR)
- **Top Global Matches:** file_cluster_13: 13.148, file_cluster_8: 13.182, file_cluster_0: 13.542
- **Magnitude:** 2239.58 | **LOC:** 3160 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 34.9%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (61.2742%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assertCachePoolServiceDefinitionIsCreate` (Impact: 37.3 | O(N^3) | DB: 5)
  * `testWorkflows` (Impact: 36.2 | O(N^4) | DB: 18)
  * `createContainerFromFile` (Impact: 35.5 | O(N^3) | DB: 8)
  * `testMessengerTransports` (Impact: 35.1 | O(N^3) | DB: 18)
  * `testHtmlSanitizerDefaultConfig` (Impact: 32.5 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 646`, `args: 200`, `func_start: 187`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 647`, `duplicate_logic: 2`
* *Architecture:* `api: 348`, `concurrency: 2`, `import: 109`
* *Defense:* `safety: 27`, `doc: 5`, `test: 616`, `sync_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.479
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 100):` Symfony\Component\Translation\LocaleSwitcher, Symfony\Component\JsonPath\FunctionReturnType, mentDefinition = $requirements['_locale'], Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\HtmlSanitizer\HtmlSanitizerInterface, Symfony\Component\HttpClient\ThrottlingHttpClient, Symfony\Component\Messenger\Bridge\AmazonSqs\Transport\AmazonSqsTransportFactory, Symfony\Component\HttpFoundation\IpUtils...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RedisTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.585 IQR)
- **Top Global Matches:** file_cluster_13: 14.585, file_cluster_4: 14.627, file_cluster_8: 14.734
- **Magnitude:** 2232.12 | **LOC:** 827 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (95.061%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createConnection` (Impact: 1197.8 | O(N^6) | DB: 75)
  * `doClear` (Impact: 326.9 | O(N^6) | DB: 33)
  * `doDelete` (Impact: 79.7 | O(N^5) | DB: 4)
  * `doFetch` (Impact: 73.6 | O(N^5) | DB: 5)
  * `doSave` (Impact: 48.0 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 177`, `args: 17`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 376`
* *Architecture:* `api: 7`, `concurrency: 24`, `import: 18`
* *Defense:* `safety: 103`, `doc: 4`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Predis\Response\ErrorInterface, Relay\Cluster, Relay\Relay, "ext-relay".', Predis\Connection\Aggregate\ClusterInterface, Predis\Connection\Cluster\RedisCluster, Predis\Connection\Replication\ReplicationInterface, Predis\Connection\Aggregate\ReplicationInterface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/VarDumper/Dumper/CliDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.844 IQR)
- **Top Global Matches:** file_cluster_8: 13.844, file_cluster_13: 13.974, file_cluster_11: 14.026
- **Magnitude:** 2230.22 | **LOC:** 668 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (64.7088%), Tech Debt (10.8263%)
**Top Internal Functions/Classes:**
  * `style` (Impact: 568.2 | O(2^N) | DB: 30)
  * `dumpKey` (Impact: 263.1 | O(N^6) | DB: 16)
  * `dumpString` (Impact: 254.8 | O(N^6) | DB: 17)
  * `dumpScalar` (Impact: 153.0 | O(N^5) | DB: 19)
  * `supportsColors` (Impact: 123.1 | O(N^6) | DB: 22)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 64`, `args: 20`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 405`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 21`, `import: 3`
* *Defense:* `safety: 35`, `doc: 19`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.564
  * `Choke Point (Betweenness):` 6.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Symfony\Component\VarDumper\Cloner\Cursor, Symfony\Component\VarDumper\Cloner\Stub, Symfony\Component\ErrorHandler\ErrorRenderer\FileLinkFormatter
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Compiler/AutowirePass.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.232 IQR)
- **Top Global Matches:** file_cluster_13: 14.232, file_cluster_0: 14.412, file_cluster_11: 14.424
- **Magnitude:** 2224.56 | **LOC:** 771 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (81.2461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `autowireMethod` (Impact: 562.3 | O(N^6) | DB: 47)
  * `getCombinedAlias` (Impact: 281.7 | O(2^N) | DB: 13)
  * `autowireCalls` (Impact: 183.5 | O(N^6) | DB: 16)
  * `doProcessValue` (Impact: 128.2 | O(N^5) | DB: 17)
  * `getAutowiredReference` (Impact: 117.3 | O(N^6) | DB: 11)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 162`, `args: 21`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 488`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 17`
* *Defense:* `safety: 51`, `doc: 10`, `test: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Symfony\Component\DependencyInjection\Reference, Symfony\Component\DependencyInjection\Attribute\AutowireInline, Symfony\Component\DependencyInjection\Exception\RuntimeException, Symfony\Component\DependencyInjection\TypedReference, Symfony\Component\DependencyInjection\ContainerBuilder, Symfony\Component\DependencyInjection\Definition, Symfony\Component\DependencyInjection\Attribute\Autowire, Symfony\Component\DependencyInjection\Attribute\Target...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.297 IQR)
- **Top Global Matches:** file_cluster_13: 13.297, file_cluster_8: 13.421, file_cluster_11: 13.583
- **Magnitude:** 2199.38 | **LOC:** 389 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 50
- **Risk Profile:** Cognitive Load (78.3578%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getEnv` (Impact: 2017.5 | O(2^N) | DB: 50)
  * `__construct` (Impact: 9.3 | O(N^2) | DB: 3)
    * *Intent:* /** * @author Nicolas Grekas <p@tchwork.com> */
  * `getProvidedTypes` (Impact: 8.2 | O(N^3))
  * `reset` (Impact: 7.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 82`, `args: 5`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 145`
* *Architecture:* `io: 1`, `api: 6`, `import: 7`
* *Defense:* `safety: 30`, `doc: 7`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Symfony\Component\DependencyInjection\Exception\EnvNotFoundException, === $prefix) 
            if (!\is_scalar($file = $getEnv($name))) 
                throw new RuntimeException(\sprintf(, $file, Symfony\Contracts\Service\ResetInterface, =>, Symfony\Component\DependencyInjection\Exception\RuntimeException, Symfony\Component\DependencyInjection\Exception\ParameterCircularReferenceException
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Filesystem/Filesystem.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.552 IQR)
- **Top Global Matches:** file_cluster_8: 13.552, file_cluster_13: 13.624, file_cluster_7: 13.695
- **Magnitude:** 2094.36 | **LOC:** 779 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (41.7686%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doRemove` (Impact: 293.2 | O(2^N) | DB: 8)
  * `copy` (Impact: 182.3 | O(2^N) | DB: 14)
  * `mirror` (Impact: 170.7 | O(N^5) | DB: 15)
    * *Intent:* /** * Resolves links in paths. * * With $canonicalize = false (default) * - if $path does not exist ...
  * `makePathRelative` (Impact: 138.8 | O(N^5) | DB: 17)
  * `tempnam` (Impact: 133.8 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 112`, `args: 32`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 238`
* *Architecture:* `io: 6`, `api: 24`, `import: 3`
* *Defense:* `safety: 18`, `doc: 60`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.928
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` d privilege is not held by the client\'. Do you have the required Administrator-rights?', 0, Symfony\Component\Filesystem\Exception\InvalidArgumentException, $target, Symfony\Component\Filesystem\Exception\FileNotFoundException, $linkType), Symfony\Component\Filesystem\Exception\IOException, null
  * `Imported By (In-Degree: 88):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.955 IQR)
- **Top Global Matches:** file_cluster_8: 10.955, file_cluster_7: 11.541, file_cluster_13: 11.6
- **Magnitude:** 2092.06 | **LOC:** 1755 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 83.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (29.0175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hscan` (Impact: 13.6 | O(2^N) | DB: 3)
  * `scan` (Impact: 13.6 | O(2^N) | DB: 4)
  * `getLastError` (Impact: 10.6 | O(2^N))
  * `connect` (Impact: 9.2 | O(2^N) | DB: 7)
  * `migrate` (Impact: 9.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 703`, `args: 345`, `func_start: 344`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 222`
* *Architecture:* `api: 345`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` RedisProxyTrait 
        resetLazyObject, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Component\Cache\Traits\Relay\Relay21Trait, Symfony\Contracts\Service\ResetInterface, Symfony\Component\Cache\Traits\Relay\Relay20Trait, Relay21Trait, Relay20Trait
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Dumper/XmlDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.455 IQR)
- **Top Global Matches:** file_cluster_4: 13.455, file_cluster_13: 13.932, file_cluster_8: 14.051
- **Magnitude:** 2076.9 | **LOC:** 444 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (99.5317%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `convertParameters` (Impact: 719.5 | O(2^N) | DB: 41)
  * `addService` (Impact: 686.4 | O(2^N) | DB: 31)
  * `addTagRecursiveAttributes` (Impact: 72.7 | O(2^N) | DB: 2)
  * `addMethodCalls` (Impact: 42.8 | O(N^5) | DB: 1)
  * `escape` (Impact: 40.6 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 108`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 281`
* *Architecture:* `api: 4`, `concurrency: 127`, `import: 13`
* *Defense:* `safety: 27`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Symfony\Component\DependencyInjection\Reference, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\DependencyInjection\Definition, Symfony\Component\DependencyInjection\ContainerInterface, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\DependencyInjection\Parameter, Symfony\Component\DependencyInjection\Argument\ArgumentInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpFoundation/Request.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.181 IQR)
- **Top Global Matches:** file_cluster_13: 14.181, file_cluster_8: 14.277, file_cluster_17: 14.281
- **Magnitude:** 1988.3 | **LOC:** 2274 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 41
- **Risk Profile:** Cognitive Load (47.1912%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 464.5 | O(N^5) | DB: 25)
  * `getFormat` (Impact: 93.4 | O(N^4) | DB: 12)
  * `duplicate` (Impact: 86.8 | O(N^3) | DB: 17)
  * `getRelativeUriForPath` (Impact: 81.8 | O(N^4) | DB: 12)
  * `getHost` (Impact: 75.1 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 245`, `args: 71`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 602`, `dead_code: 2`
* *Architecture:* `io: 23`, `api: 91`, `import: 10`
* *Defense:* `safety: 61`, `doc: 106`, `test: 3`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.82
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` d.
     * If the HTTP method parameter override is enabled, an html-form with method "POST" can be altered
     * and used to send a "PUT" or "DELETE" request via the _method request parameter.
     * If these methods are not protected against CSRF, Symfony\Component\HttpFoundation\Session\SessionInterface, 
    public function getBaseUrl(): string
    
        $trustedPrefix = '', Symfony\Component\HttpFoundation\Exception\SuspiciousOperationException, Symfony\Component\HttpFoundation\Exception\ConflictingHeadersException, Symfony\Component\HttpFoundation\Exception\JsonException, 
    private function getBaseUrlReal(): string
    
        return $this->baseUrl ??= $this->prepareBaseUrl(...
  * `Imported By (In-Degree: 504):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayClusterProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.013 IQR)
- **Top Global Matches:** file_cluster_8: 11.013, file_cluster_7: 11.592, file_cluster_13: 11.621
- **Magnitude:** 1976.46 | **LOC:** 1355 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (29.7001%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `scan` (Impact: 14.9 | O(2^N) | DB: 4)
  * `hscan` (Impact: 13.6 | O(2^N) | DB: 3)
  * `sscan` (Impact: 13.6 | O(2^N) | DB: 3)
  * `fullscan` (Impact: 12.2 | O(2^N) | DB: 3)
  * `getLastError` (Impact: 10.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 542`, `args: 264`, `func_start: 264`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 172`
* *Architecture:* `api: 265`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` RedisProxyTrait 
        resetLazyObject, RelayCluster20Trait, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Component\Cache\Traits\Relay\RelayCluster21Trait, Symfony\Contracts\Service\ResetInterface, RelayCluster21Trait, Symfony\Component\Cache\Traits\Relay\RelayCluster20Trait
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/JsonPath/Tokenizer/JsonPathTokenizer.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.462 IQR)
- **Top Global Matches:** file_cluster_8: 13.462, file_cluster_13: 13.667, file_cluster_7: 13.819
- **Magnitude:** 1971.84 | **LOC:** 633 | **CtrlFlow:** 73.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (87.3913%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tokenize` (Impact: 620.9 | O(N^6) | DB: 57)
  * `parseFunctionCalls` (Impact: 327.1 | O(2^N) | DB: 21)
  * `validateUnicodeEscape` (Impact: 171.2 | O(N^6) | DB: 17)
  * `validateFilterExpression` (Impact: 143.0 | O(N^5) | DB: 9)
  * `extractParenthesizedExpression` (Impact: 101.1 | O(N^5) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 227`, `structural_boundaries: 84`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 375`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 12`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.071
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` s exactly %d argument(s).', $functionName, Symfony\Component\JsonPath\Exception\InvalidJsonPathException, s a query argument, not a literal.', $expectedArgCount), $functionName), Symfony\Component\JsonPath\JsonPath...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RedisProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.739 IQR)
- **Top Global Matches:** file_cluster_8: 10.739, file_cluster_7: 11.333, file_cluster_13: 11.401
- **Magnitude:** 1964.44 | **LOC:** 1298 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (33.4716%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLastError` (Impact: 10.6 | O(2^N))
  * `getPersistentID` (Impact: 10.6 | O(2^N))
  * `migrate` (Impact: 9.2 | O(2^N) | DB: 3)
  * `connect` (Impact: 8.7 | O(2^N) | DB: 6)
  * `open` (Impact: 8.7 | O(2^N) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 519`, `args: 254`, `func_start: 253`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 175`
* *Architecture:* `api: 253`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` RedisProxyTrait 
        resetLazyObject, Redis62ProxyTrait, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Contracts\Service\ResetInterface, Redis63ProxyTrait
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.188 IQR)
- **Top Global Matches:** file_cluster_13: 15.188, file_cluster_11: 15.616, file_cluster_0: 15.727
- **Magnitude:** 1958.4 | **LOC:** 975 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 30.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (48.369%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `denormalize` (Impact: 898.5 | O(2^N) | DB: 30)
  * `normalize` (Impact: 423.9 | O(2^N) | DB: 22)
  * `__construct` (Impact: 148.2 | O(2^N) | DB: 8)
  * `validateAndDenormalize` (Impact: 101.8 | O(N^4) | DB: 11)
  * `getAttributes` (Impact: 46.5 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 94`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 259`, `dead_code: 1`
* *Architecture:* `api: 16`, `import: 34`
* *Defense:* `safety: 65`, `doc: 22`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.2
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 34):` Symfony\Component\Serializer\Encoder\XmlEncoder, Symfony\Component\TypeInfo\Type\BuiltinType, Symfony\Component\Serializer\Mapping\ClassDiscriminatorResolverInterface, Symfony\Component\Serializer\NameConverter\NameConverterInterface, Symfony\Component\PropertyAccess\Exception\InvalidTypeException, Symfony\Component\Serializer\Mapping\Factory\ClassMetadataFactoryInterface, Symfony\Component\Serializer\Mapping\AttributeMetadata, Symfony\Component\PropertyAccess\Exception\InvalidArgumentException...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Symfony/Component/Serializer/Attribute/Context.php` (PHP) | Magnitude: 57.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, state_mutation: 13, structural_boundaries: 10, doc: 7
- `src/Symfony/Component/Routing/Tests/Fixtures/Psr4Controllers/SubNamespace/EvenDeeperNamespace/MyOtherController.php` (PHP) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, ssr_boundaries: 8, api: 7
- `src/Symfony/Bridge/Doctrine/Tests/PropertyInfo/Fixtures/DoctrineRelation.php` (PHP) | Magnitude: 0.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, decorators: 13, structural_boundaries: 12, encapsulation: 8
- `src/Symfony/Component/Console/Tests/ArgumentResolver/ValueResolver/MapInputValueResolverTest.php` (PHP) | Magnitude: 169.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 209, structural_boundaries: 149, memory_alloc: 86, state_mutation: 84
- `src/Symfony/Component/HttpFoundation/Tests/Session/Storage/Proxy/AbstractProxyTest.php` (PHP) | Magnitude: 33.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 24, test: 16, decorators: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/Symfony/Component/EventDispatcher/EventSubscriberInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: ownership: 4, structural_boundaries: 3, doc: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Symfony/Component/VarDumper/Caster/SymfonyCaster.php` (PHP) | Magnitude: 150.64 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 37, structural_boundaries: 30, planned_debt: 17
- `src/Symfony/Component/Serializer/Normalizer/DenormalizableInterface.php` (PHP) | Magnitude: 52.55 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 6, doc: 6, bitwise_ops: 4, structural_boundaries: 3
- `src/Symfony/Component/VarDumper/Caster/ArgsStub.php` (PHP) | Magnitude: 207.3 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 36, structural_boundaries: 28, branch: 19
- `src/Symfony/Component/VarExporter/ProxyHelper.php` (PHP) | Magnitude: 1659.96 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 319, state_mutation: 318, branch: 194, structural_boundaries: 156
- `src/Symfony/Component/Serializer/Normalizer/NormalizableInterface.php` (PHP) | Magnitude: 52.55 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 6, bitwise_ops: 6, doc: 5, structural_boundaries: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Symfony/Component/Console/Resources/completion.zsh` (SHELL) | Magnitude: 88.82 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 45, indent_spaces: 38, branch: 18, reflection_metaprogramming: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Symfony/Component/Config/Definition/VariableNode.php` (PHP) | Magnitude: 107.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 23, state_mutation: 22, api: 14
- `src/Symfony/Component/Console/Tests/Command/CommandTest.php` (PHP) | Magnitude: 325.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 378, structural_boundaries: 195, state_mutation: 92, test: 80
- `src/Symfony/Component/Serializer/Normalizer/GetSetMethodNormalizer.php` (PHP) | Magnitude: 585.72 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 124, state_mutation: 93, structural_boundaries: 58, branch: 56
- `src/Symfony/Component/Uid/Uuid.php` (PHP) | Magnitude: 321.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 147, state_mutation: 97, structural_boundaries: 70, branch: 43
- `src/Symfony/Bridge/PsrHttpMessage/Tests/Functional/ControllerTest.php` (PHP) | Magnitude: 21.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, state_mutation: 6, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Symfony/Component/Config/Definition/Builder/ExprBuilder.php` (PHP) | Magnitude: 235.3 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 64, structural_boundaries: 42, api: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Symfony/Component/Intl/Data/Util/LocaleScanner.php` (PHP) | Magnitude: 70.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 26, structural_boundaries: 11, branch: 6
- `src/Symfony/Component/Validator/Constraints/DateTimeValidator.php` (PHP) | Magnitude: 79.4 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, branch: 13, structural_boundaries: 13, ui_framework: 8
- `src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher2.php` (PHP) | Magnitude: 0.08 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, state_mutation: 60, bitwise_ops: 58, branch: 26
- `src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher1.php` (PHP) | Magnitude: 0.08 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 60, bitwise_ops: 58, branch: 26
- `src/Symfony/Component/Config/Definition/EnumNode.php` (PHP) | Magnitude: 469.46 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 47, branch: 41, state_mutation: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Symfony/Component/Security/Core/Exception/UserNotFoundException.php` (PHP) | Magnitude: 49.54 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, api: 10, state_mutation: 7
- `src/Symfony/Component/Validator/Constraints/ImageValidator.php` (PHP) | Magnitude: 806.06 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, branch: 85, state_mutation: 54, structural_boundaries: 41
- `src/Symfony/Component/ErrorHandler/Resources/views/exception.html.php` (PHP) | Magnitude: 41.12 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, branch: 96, structural_boundaries: 38, state_mutation: 24
- `src/Symfony/Component/Validator/Tests/Constraints/LengthValidatorTest.php` (PHP) | Magnitude: 146.3 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 305, structural_boundaries: 63, ui_framework: 48, args: 26
- `src/Symfony/Component/ErrorHandler/Resources/views/traces.html.php` (PHP) | Magnitude: 43.14 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 66, indent_spaces: 55, structural_boundaries: 29, state_mutation: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Symfony/Component/Clock/Tests/DatePointTest.php` (PHP) | Magnitude: 60.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 46, test: 16, concurrency: 12
- `src/Symfony/Component/DependencyInjection/Tests/Loader/Configurator/EnvConfiguratorTest.php` (PHP) | Magnitude: 19.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 27, indent_spaces: 15, concurrency: 7, memory_alloc: 7
- `src/Symfony/Component/HttpClient/Internal/AmpClientState.php` (PHP) | Magnitude: 476.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 93, structural_boundaries: 45, branch: 34
- `src/Symfony/Component/HttpKernel/Tests/EventListener/ProfilerListenerTest.php` (PHP) | Magnitude: 68.92 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 44, state_mutation: 26, concurrency: 19
- `src/Symfony/Component/Workflow/Tests/Dumper/MermaidDumperTest.php` (PHP) | Magnitude: 118.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 51, structural_boundaries: 34, concurrency: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/Symfony/Component/Security/Core/User/UserInterface.php` (PHP) | Magnitude: 40.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, planned_debt: 3, args: 2
- `src/Symfony/Component/VarDumper/Caster/OpenSSLCaster.php` (PHP) | Magnitude: 43.36 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, state_mutation: 14, planned_debt: 8
- `src/Symfony/Component/VarDumper/Caster/StubCaster.php` (PHP) | Magnitude: 51.14 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, planned_debt: 12, indent_spaces: 12, structural_boundaries: 8
- `src/Symfony/Component/VarDumper/Cloner/Cursor.php` (PHP) | Magnitude: 51.52 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 21, indent_spaces: 21, state_mutation: 15, planned_debt: 4
- `src/Symfony/Component/VarDumper/Caster/SplCaster.php` (PHP) | Magnitude: 211.12 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 34, structural_boundaries: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Symfony/Component/PropertyInfo/Tests/Fixtures/PseudoTypesDummy.php` (PHP) | Magnitude: 0.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 51, api: 27, indent_spaces: 27, structural_boundaries: 2
- `src/Symfony/Component/PropertyInfo/Tests/Fixtures/Dummy.php` (PHP) | Magnitude: 0.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 83, indent_spaces: 82, api: 60, structural_boundaries: 20
- `src/Symfony/Component/Console/Style/StyleInterface.php` (PHP) | Magnitude: 400.67 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 22, doc: 21, structural_boundaries: 20, args: 18
- `src/Symfony/Component/Form/FormBuilderInterface.php` (PHP) | Magnitude: 138.38 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, state_mutation: 12, structural_boundaries: 10, args: 7
- `src/Symfony/Component/PropertyAccess/PropertyAccessorInterface.php` (PHP) | Magnitude: 56.4 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, bitwise_ops: 9, structural_boundaries: 6, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/ConfigurationTest.php` (PHP) | Magnitude: 32.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, state_mutation: 12, memory_alloc: 8
- `src/Symfony/Component/DependencyInjection/Exception/ParameterCircularReferenceException.php` (PHP) | Magnitude: 27.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, branch: 3, api: 3
- `src/Symfony/Component/Dotenv/Exception/FormatException.php` (PHP) | Magnitude: 27.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, state_mutation: 6, api: 3
- `src/Symfony/Component/Form/Extension/Core/DataTransformer/DatePointToDateTimeTransformer.php` (PHP) | Magnitude: 37.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 15, branch: 7, api: 4
- `src/Symfony/Component/HttpFoundation/Test/Constraint/ResponseHeaderSame.php` (PHP) | Magnitude: 18.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, api: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Symfony/Component/Notifier/Exception/TransportExceptionInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, func_start: 1
- `src/Symfony/Component/Translation/Exception/ProviderExceptionInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, func_start: 1
- `src/Symfony/Component/PropertyAccess/PropertyPathBuilder.php` (PHP) | Magnitude: 318.04 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 120, branch: 30, structural_boundaries: 27
- `src/Symfony/Component/Form/RequestHandlerInterface.php` (PHP) | Magnitude: 43.28 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 3, doc: 3, args: 2
- `src/Symfony/Component/Config/Loader/LoaderInterface.php` (PHP) | Magnitude: 104.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 6, state_mutation: 6, args: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Symfony/Component/HttpKernel/Kernel.php` -> Churn: **100.0%** | Cog Load: 90.1546% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` -> Churn: **92.16%** | Cog Load: 76.4498% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` -> Churn: **78.91%** | Cog Load: 61.2742% | Debt: 0.0%
- `src/Symfony/Component/ObjectMapper/ObjectMapper.php` -> Churn: **64.45%** | Cog Load: 59.057% | Debt: 0.0%
- `src/Symfony/Component/HttpKernel/Tests/KernelTest.php` -> Churn: **60.27%** | Cog Load: 60.3212% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Symfony/Component/VarDumper/Dumper/HtmlDumper.php` -> **Dariusz Ruminski** (100.0% isolated ownership) | Magnitude: 4540.68
- `src/Symfony/Component/Yaml/Parser.php` -> **Younes ENNAJI** (100.0% isolated ownership) | Magnitude: 3500.82
- `src/Symfony/Component/VarDumper/Dumper/CliDumper.php` -> **Dariusz Ruminski** (100.0% isolated ownership) | Magnitude: 2230.22
- `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php` -> **Younes ENNAJI** (100.0% isolated ownership) | Magnitude: 2199.38
- `src/Symfony/Component/Cache/Traits/RelayProxy.php` -> **Christian Flothmann** (83.3% isolated ownership) | Magnitude: 2092.06

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Symfony/Component/Console/Application.php` -> **Severity: 0.09** (Bridge: 0.0009 * Flux: 100.0%)
- `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` -> **Severity: 0.08** (Bridge: 0.0008 * Flux: 100.0%)
- `src/Symfony/Component/Console/Command/Command.php` -> **Severity: 0.053** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Symfony/Component/ErrorHandler/ErrorHandler.php` -> **Severity: 0.045** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Symfony/Component/DependencyInjection/Argument/LazyClosure.php` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` -> **Severity: 670.6** (Blast Radius: 6.706 * Doc Risk: 100.0%)
- `src/Symfony/Component/HttpFoundation/Request.php` -> **Severity: 636.74** (Blast Radius: 6.82 * Doc Risk: 93.3637%)
- `src/Symfony/Component/Validator/Constraint.php` -> **Severity: 601.7** (Blast Radius: 6.017 * Doc Risk: 100.0%)
- `src/Symfony/Component/HttpFoundation/Response.php` -> **Severity: 429.3** (Blast Radius: 4.293 * Doc Risk: 100.0%)
- `src/Symfony/Component/Notifier/Transport/Dsn.php` -> **Severity: 321.3** (Blast Radius: 3.213 * Doc Risk: 99.9999%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
