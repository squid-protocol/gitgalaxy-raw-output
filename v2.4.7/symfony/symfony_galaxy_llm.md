# ARCHITECTURAL_BRIEF: symfony
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/symfony` |
| **Timestamp** | `2026-08-07T03:55:19.294485+00:00` |
| **Scan Duration** | `41.94s` |
| **Git Branch** | `8.1` |
| **Git Commit** | `d75aa6cb9200149510699b90cb57e6e9be1408f9` |
| **Git Remote** | `https://github.com/symfony/symfony.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 10543 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.354`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 7178 | 55.3% |
| file_cluster_13 | 4267 | 32.9% |
| file_cluster_4 | 218 | 1.7% |
| file_cluster_9 | 187 | 1.4% |
| file_cluster_0 | 116 | 0.9% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 22.6 | 9.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 35.1 | 41.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.3 | 4.0 | 3.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.3 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.3 | 0.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 85.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 38.8 | 1.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 18.5 | 4.0 | 0.0 |
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

- `__construct` (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> Impact: **1008.8** | LOC: 1136
  * *Intent:* /** * Autoloader checking if the class is really defined in the file found. * * The ClassLoader will wrap all registered autoloaders * and will throw ...
- `checkAnnotations` (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> Impact: **744.5** | LOC: 929
- `parseDefinition` (@ `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`) -> Impact: **499.7** | LOC: 416
- `createConnection` (@ `src/Symfony/Component/Cache/Traits/RedisTrait.php`) -> Impact: **357.8** | LOC: 435
- `doParse` (@ `src/Symfony/Component/Yaml/Parser.php`) -> Impact: **334.0** | LOC: 409
  * *Intent:* /** * Parses a YAML string to a PHP value. * * @param string $value A YAML string * @param int-mask-of<Yaml::PARSE_*> $flags A bit field of Yaml::PARS...
- `getEnv` (@ `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`) -> Impact: **273.6** | LOC: 311
- `load` (@ `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) -> Impact: **242.5** | LOC: 554
- `__construct` (@ `src/Symfony/Component/Validator/Constraints/File.php`) -> Impact: **241.5** | LOC: 67
  * *Intent:* /** * @param positive-int|string|null $maxSize The max size of the underlying file
- `evaluateBracket` (@ `src/Symfony/Component/JsonPath/JsonCrawler.php`) -> Impact: **220.8** | LOC: 293
- `stop` (@ `src/Symfony/Component/Process/Process.php`) -> Impact: **205.6** | LOC: 474

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Symfony/Component/Emoji/Resources/data` | 174 | 14335.5 | 5.28% | 1.24% |
| `src/Symfony/Component/Validator/Constraints` | 152 | 11783.67 | 36.97% | 0.49% |
| `src/Symfony/Component/Intl/Resources/data/currencies` | 368 | 7864.08 | 5.35% | 0.02% |
| `src/Symfony/Component/DependencyInjection/Compiler` | 57 | 6736.88 | 60.08% | 12.44% |
| `src/Symfony/Component/Validator/Tests/Constraints` | 156 | 6563.6 | 16.03% | 0.0% |
| `src/Symfony/Component/Cache/Traits` | 18 | 6366.38 | 37.67% | 11.04% |
| `src/Symfony/Component/VarDumper/Dumper` | 6 | 5816.15 | 38.71% | 1.8% |
| `src/Symfony/Component/HttpFoundation` | 29 | 5538.34 | 31.82% | 4.16% |
| `src/Symfony/Component/Cache/Adapter` | 24 | 5320.8 | 60.66% | 3.01% |
| `src/Symfony/Component/DependencyInjection/Dumper` | 7 | 5076.24 | 60.6% | 14.29% |

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
- `src/Symfony/Component/Serializer/Tests/Normalizer/AbstractObjectNormalizerTest.php` -> **64** Orphaned Functions | **94** Duplicates
- `src/Symfony/Bridge/Twig/Tests/Extension/AbstractLayoutTestCase.php` -> **148** Orphaned Functions | **2** Duplicates
- `src/Symfony/Component/DependencyInjection/Tests/ContainerBuilderTest.php` -> **131** Orphaned Functions | **4** Duplicates
- `src/Symfony/Component/Form/Tests/Extension/Core/Type/ChoiceTypeTest.php` -> **115** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Symfony/Bridge/PhpUnit/bin/simple-phpunit.php`** -> AI Confidence: **99.48%**
2. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/full.php`** -> AI Confidence: **99.48%**
3. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/container1.php`** -> AI Confidence: **99.48%**
4. **`src/Symfony/Component/ErrorHandler/Resources/views/exception_full.html.php`** -> AI Confidence: **99.48%**
5. **`src/Symfony/Component/Routing/Attribute/Route.php`** -> AI Confidence: **99.48%**
6. **`src/Symfony/Component/Routing/Matcher/Dumper/CompiledUrlMatcherTrait.php`** -> AI Confidence: **99.48%**
7. **`src/Symfony/Component/Validator/Constraints/Image.php`** -> AI Confidence: **99.48%**
8. **`src/Symfony/Component/Validator/Constraints/Video.php`** -> AI Confidence: **99.48%**
9. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveBindingsPass.php`** -> AI Confidence: **99.39%**
10. **`src/Symfony/Component/Dotenv/Dotenv.php`** -> AI Confidence: **99.39%**
11. **`src/Symfony/Component/ErrorHandler/DebugClassLoader.php`** -> AI Confidence: **99.39%**
12. **`src/Symfony/Component/HttpClient/Response/NativeResponse.php`** -> AI Confidence: **99.39%**
13. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php`** -> AI Confidence: **99.39%**
14. **`src/Symfony/Component/JsonPath/Tokenizer/JsonPathTokenizer.php`** -> AI Confidence: **99.39%**
15. **`src/Symfony/Component/Messenger/Bridge/Redis/Transport/Connection.php`** -> AI Confidence: **99.39%**
16. **`src/Symfony/Component/Routing/Matcher/TraceableUrlMatcher.php`** -> AI Confidence: **99.39%**
17. **`src/Symfony/Component/Routing/RouteCompiler.php`** -> AI Confidence: **99.39%**
18. **`src/Symfony/Component/Validator/Constraints/Choice.php`** -> AI Confidence: **99.39%**
19. **`src/Symfony/Component/Cache/Adapter/PdoAdapter.php`** -> AI Confidence: **99.35%**
20. **`src/Symfony/Bundle/FrameworkBundle/Controller/RedirectController.php`** -> AI Confidence: **99.34%**
21. **`src/Symfony/Component/Routing/Loader/ContentLoaderTrait.php`** -> AI Confidence: **99.34%**
22. **`src/Symfony/Component/Validator/Constraints/ImageValidator.php`** -> AI Confidence: **99.34%**
23. **`src/Symfony/Component/HttpClient/HttpClientTrait.php`** -> AI Confidence: **99.33%**
24. **`src/Symfony/Component/ErrorHandler/Resources/views/trace.html.php`** -> AI Confidence: **99.32%**
25. **`src/Symfony/Component/VarDumper/Dumper/CliDumper.php`** -> AI Confidence: **99.32%**
26. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php`** -> AI Confidence: **99.31%**
27. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php`** -> AI Confidence: **99.31%**
28. **`src/Symfony/Bridge/Doctrine/PropertyInfo/DoctrineExtractor.php`** -> AI Confidence: **99.31%**
29. **`src/Symfony/Bridge/Doctrine/Validator/DoctrineLoader.php`** -> AI Confidence: **99.31%**
30. **`src/Symfony/Bridge/Monolog/Formatter/ConsoleFormatter.php`** -> AI Confidence: **99.31%**
31. **`src/Symfony/Bridge/PhpUnit/DeprecationErrorHandler.php`** -> AI Confidence: **99.31%**
32. **`src/Symfony/Bridge/PhpUnit/DeprecationErrorHandler/Deprecation.php`** -> AI Confidence: **99.31%**
33. **`src/Symfony/Bridge/PhpUnit/Legacy/SymfonyTestsListenerTrait.php`** -> AI Confidence: **99.31%**
34. **`src/Symfony/Bridge/PsrHttpMessage/Factory/PsrHttpFactory.php`** -> AI Confidence: **99.31%**
35. **`src/Symfony/Bridge/Twig/Command/DebugCommand.php`** -> AI Confidence: **99.31%**
36. **`src/Symfony/Bridge/Twig/Node/TransNode.php`** -> AI Confidence: **99.31%**
37. **`src/Symfony/Bridge/Twig/NodeVisitor/TranslationNodeVisitor.php`** -> AI Confidence: **99.31%**
38. **`src/Symfony/Bundle/FrameworkBundle/Command/AbstractConfigCommand.php`** -> AI Confidence: **99.31%**
39. **`src/Symfony/Bundle/FrameworkBundle/Command/AssetsInstallCommand.php`** -> AI Confidence: **99.31%**
40. **`src/Symfony/Bundle/FrameworkBundle/Command/CacheClearCommand.php`** -> AI Confidence: **99.31%**
41. **`src/Symfony/Bundle/FrameworkBundle/Command/ContainerDebugCommand.php`** -> AI Confidence: **99.31%**
42. **`src/Symfony/Bundle/FrameworkBundle/Command/DebugAutowiringCommand.php`** -> AI Confidence: **99.31%**
43. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsSetCommand.php`** -> AI Confidence: **99.31%**
44. **`src/Symfony/Bundle/FrameworkBundle/Command/TranslationExtractCommand.php`** -> AI Confidence: **99.31%**
45. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/Descriptor.php`** -> AI Confidence: **99.31%**
46. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/JsonDescriptor.php`** -> AI Confidence: **99.31%**
47. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/MarkdownDescriptor.php`** -> AI Confidence: **99.31%**
48. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
49. **`src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/XmlDescriptor.php`** -> AI Confidence: **99.31%**
50. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Compiler/PhpConfigReferenceDumpPass.php`** -> AI Confidence: **99.31%**
51. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Configuration.php`** -> AI Confidence: **99.31%**
52. **`src/Symfony/Bundle/FrameworkBundle/Secrets/SodiumVault.php`** -> AI Confidence: **99.31%**
53. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/authenticator_manager.php`** -> AI Confidence: **99.31%**
54. **`src/Symfony/Bundle/TwigBundle/DependencyInjection/Compiler/ExtensionPass.php`** -> AI Confidence: **99.31%**
55. **`src/Symfony/Bundle/TwigBundle/DependencyInjection/TwigExtension.php`** -> AI Confidence: **99.31%**
56. **`src/Symfony/Bundle/WebProfilerBundle/Controller/ProfilerController.php`** -> AI Confidence: **99.31%**
57. **`src/Symfony/Bundle/WebProfilerBundle/EventListener/WebDebugToolbarListener.php`** -> AI Confidence: **99.31%**
58. **`src/Symfony/Component/Asset/VersionStrategy/JsonManifestVersionStrategy.php`** -> AI Confidence: **99.31%**
59. **`src/Symfony/Component/AssetMapper/Command/DebugAssetMapperCommand.php`** -> AI Confidence: **99.31%**
60. **`src/Symfony/Component/AssetMapper/Command/ImportMapAuditCommand.php`** -> AI Confidence: **99.31%**
61. **`src/Symfony/Component/AssetMapper/Compiler/JavaScriptImportPathCompiler.php`** -> AI Confidence: **99.31%**
62. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapConfigReader.php`** -> AI Confidence: **99.31%**
63. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapGenerator.php`** -> AI Confidence: **99.31%**
64. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapManager.php`** -> AI Confidence: **99.31%**
65. **`src/Symfony/Component/AssetMapper/ImportMap/ImportMapRenderer.php`** -> AI Confidence: **99.31%**
66. **`src/Symfony/Component/AssetMapper/ImportMap/Resolver/JsDelivrEsmResolver.php`** -> AI Confidence: **99.31%**
67. **`src/Symfony/Component/Cache/Adapter/AbstractAdapter.php`** -> AI Confidence: **99.31%**
68. **`src/Symfony/Component/Cache/Adapter/AbstractTagAwareAdapter.php`** -> AI Confidence: **99.31%**
69. **`src/Symfony/Component/Cache/Adapter/CouchbaseCollectionAdapter.php`** -> AI Confidence: **99.31%**
70. **`src/Symfony/Component/Cache/Adapter/DoctrineDbalAdapter.php`** -> AI Confidence: **99.31%**
71. **`src/Symfony/Component/Cache/Adapter/PhpArrayAdapter.php`** -> AI Confidence: **99.31%**
72. **`src/Symfony/Component/Cache/Adapter/RedisTagAwareAdapter.php`** -> AI Confidence: **99.31%**
73. **`src/Symfony/Component/Cache/Adapter/TagAwareAdapter.php`** -> AI Confidence: **99.31%**
74. **`src/Symfony/Component/Cache/DependencyInjection/CachePoolPass.php`** -> AI Confidence: **99.31%**
75. **`src/Symfony/Component/Cache/Psr16Cache.php`** -> AI Confidence: **99.31%**
76. **`src/Symfony/Component/Cache/Tests/Traits/RedisProxiesTest.php`** -> AI Confidence: **99.31%**
77. **`src/Symfony/Component/Config/Definition/Dumper/XmlReferenceDumper.php`** -> AI Confidence: **99.31%**
78. **`src/Symfony/Component/Config/Definition/Dumper/YamlReferenceDumper.php`** -> AI Confidence: **99.31%**
79. **`src/Symfony/Component/Config/Resource/ClassExistenceResource.php`** -> AI Confidence: **99.31%**
80. **`src/Symfony/Component/Console/Application.php`** -> AI Confidence: **99.31%**
81. **`src/Symfony/Component/Console/Attribute/Argument.php`** -> AI Confidence: **99.31%**
82. **`src/Symfony/Component/Console/Attribute/Ask.php`** -> AI Confidence: **99.31%**
83. **`src/Symfony/Component/Console/Attribute/AskChoice.php`** -> AI Confidence: **99.31%**
84. **`src/Symfony/Component/Console/Command/CompleteCommand.php`** -> AI Confidence: **99.31%**
85. **`src/Symfony/Component/Console/Command/InvokableCommand.php`** -> AI Confidence: **99.31%**
86. **`src/Symfony/Component/Console/Completion/CompletionInput.php`** -> AI Confidence: **99.31%**
87. **`src/Symfony/Component/Console/DependencyInjection/AddConsoleCommandPass.php`** -> AI Confidence: **99.31%**
88. **`src/Symfony/Component/Console/DependencyInjection/RegisterCommandArgumentLocatorsPass.php`** -> AI Confidence: **99.31%**
89. **`src/Symfony/Component/Console/Descriptor/MarkdownDescriptor.php`** -> AI Confidence: **99.31%**
90. **`src/Symfony/Component/Console/Descriptor/ReStructuredTextDescriptor.php`** -> AI Confidence: **99.31%**
91. **`src/Symfony/Component/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
92. **`src/Symfony/Component/Console/Helper/FileInputHelper.php`** -> AI Confidence: **99.31%**
93. **`src/Symfony/Component/Console/Helper/QuestionHelper.php`** -> AI Confidence: **99.31%**
94. **`src/Symfony/Component/Console/Helper/Table.php`** -> AI Confidence: **99.31%**
95. **`src/Symfony/Component/Console/Input/InputDefinition.php`** -> AI Confidence: **99.31%**
96. **`src/Symfony/Component/Console/Input/InputOption.php`** -> AI Confidence: **99.31%**
97. **`src/Symfony/Component/DependencyInjection/Attribute/Autowire.php`** -> AI Confidence: **99.31%**
98. **`src/Symfony/Component/DependencyInjection/Attribute/AutowireLocator.php`** -> AI Confidence: **99.31%**
99. **`src/Symfony/Component/DependencyInjection/Compiler/AbstractRecursivePass.php`** -> AI Confidence: **99.31%**
100. **`src/Symfony/Component/DependencyInjection/Compiler/AnalyzeServiceReferencesPass.php`** -> AI Confidence: **99.31%**
101. **`src/Symfony/Component/DependencyInjection/Compiler/AutowirePass.php`** -> AI Confidence: **99.31%**
102. **`src/Symfony/Component/DependencyInjection/Compiler/AutowireRequiredMethodsPass.php`** -> AI Confidence: **99.31%**
103. **`src/Symfony/Component/DependencyInjection/Compiler/AutowireRequiredPropertiesPass.php`** -> AI Confidence: **99.31%**
104. **`src/Symfony/Component/DependencyInjection/Compiler/CheckTypeDeclarationsPass.php`** -> AI Confidence: **99.31%**
105. **`src/Symfony/Component/DependencyInjection/Compiler/RegisterServiceSubscribersPass.php`** -> AI Confidence: **99.31%**
106. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveAutowireInlineAttributesPass.php`** -> AI Confidence: **99.31%**
107. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveDecoratorStackPass.php`** -> AI Confidence: **99.31%**
108. **`src/Symfony/Component/DependencyInjection/Compiler/ResolveInvalidReferencesPass.php`** -> AI Confidence: **99.31%**
109. **`src/Symfony/Component/DependencyInjection/Compiler/ValidateEnvPlaceholdersPass.php`** -> AI Confidence: **99.31%**
110. **`src/Symfony/Component/DependencyInjection/Container.php`** -> AI Confidence: **99.31%**
111. **`src/Symfony/Component/DependencyInjection/ContainerBuilder.php`** -> AI Confidence: **99.31%**
112. **`src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php`** -> AI Confidence: **99.31%**
113. **`src/Symfony/Component/DependencyInjection/Dumper/XmlDumper.php`** -> AI Confidence: **99.31%**
114. **`src/Symfony/Component/DependencyInjection/Dumper/YamlDumper.php`** -> AI Confidence: **99.31%**
115. **`src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`** -> AI Confidence: **99.31%**
116. **`src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`** -> AI Confidence: **99.31%**
117. **`src/Symfony/Component/DependencyInjection/Loader/FileLoader.php`** -> AI Confidence: **99.31%**
118. **`src/Symfony/Component/DependencyInjection/Loader/PhpFileLoader.php`** -> AI Confidence: **99.31%**
119. **`src/Symfony/Component/DependencyInjection/ServiceLocator.php`** -> AI Confidence: **99.31%**
120. **`src/Symfony/Component/Dotenv/Command/DebugCommand.php`** -> AI Confidence: **99.31%**
121. **`src/Symfony/Component/ErrorHandler/ErrorEnhancer/ClassNotFoundErrorEnhancer.php`** -> AI Confidence: **99.31%**
122. **`src/Symfony/Component/ErrorHandler/ErrorHandler.php`** -> AI Confidence: **99.31%**
123. **`src/Symfony/Component/EventDispatcher/DependencyInjection/RegisterListenersPass.php`** -> AI Confidence: **99.31%**
124. **`src/Symfony/Component/Filesystem/Filesystem.php`** -> AI Confidence: **99.31%**
125. **`src/Symfony/Component/Form/ChoiceList/Factory/DefaultChoiceListFactory.php`** -> AI Confidence: **99.31%**
126. **`src/Symfony/Component/Form/Console/Descriptor/JsonDescriptor.php`** -> AI Confidence: **99.31%**
127. **`src/Symfony/Component/Form/Console/Descriptor/TextDescriptor.php`** -> AI Confidence: **99.31%**
128. **`src/Symfony/Component/Form/Extension/Core/Type/BaseType.php`** -> AI Confidence: **99.31%**
129. **`src/Symfony/Component/Form/Extension/Core/Type/DateIntervalType.php`** -> AI Confidence: **99.31%**
130. **`src/Symfony/Component/Form/Extension/Core/Type/FileType.php`** -> AI Confidence: **99.31%**
131. **`src/Symfony/Component/Form/Extension/Validator/Constraints/FormValidator.php`** -> AI Confidence: **99.31%**
132. **`src/Symfony/Component/Form/Extension/Validator/ViolationMapper/ViolationMapper.php`** -> AI Confidence: **99.31%**
133. **`src/Symfony/Component/HtmlSanitizer/Visitor/DomVisitor.php`** -> AI Confidence: **99.31%**
134. **`src/Symfony/Component/HttpClient/CachingHttpClient.php`** -> AI Confidence: **99.31%**
135. **`src/Symfony/Component/HttpClient/CurlHttpClient.php`** -> AI Confidence: **99.31%**
136. **`src/Symfony/Component/HttpClient/DataCollector/HttpClientDataCollector.php`** -> AI Confidence: **99.31%**
137. **`src/Symfony/Component/HttpClient/EventSourceHttpClient.php`** -> AI Confidence: **99.31%**
138. **`src/Symfony/Component/HttpClient/GuzzleHttpHandler.php`** -> AI Confidence: **99.31%**
139. **`src/Symfony/Component/HttpClient/Internal/HttplugWaitLoop.php`** -> AI Confidence: **99.31%**
140. **`src/Symfony/Component/HttpClient/NativeHttpClient.php`** -> AI Confidence: **99.31%**
141. **`src/Symfony/Component/HttpClient/NoPrivateNetworkHttpClient.php`** -> AI Confidence: **99.31%**
142. **`src/Symfony/Component/HttpClient/Response/AmpResponse.php`** -> AI Confidence: **99.31%**
143. **`src/Symfony/Component/HttpClient/Response/AsyncResponse.php`** -> AI Confidence: **99.31%**
144. **`src/Symfony/Component/HttpClient/Response/CurlResponse.php`** -> AI Confidence: **99.31%**
145. **`src/Symfony/Component/HttpClient/Response/MockResponse.php`** -> AI Confidence: **99.31%**
146. **`src/Symfony/Component/HttpClient/Response/TraceableResponse.php`** -> AI Confidence: **99.31%**
147. **`src/Symfony/Component/HttpClient/RetryableHttpClient.php`** -> AI Confidence: **99.31%**
148. **`src/Symfony/Component/HttpFoundation/Request.php`** -> AI Confidence: **99.31%**
149. **`src/Symfony/Component/HttpFoundation/Response.php`** -> AI Confidence: **99.31%**
150. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/SessionHandlerFactory.php`** -> AI Confidence: **99.31%**
151. **`src/Symfony/Component/HttpFoundation/Tests/UriSignerTest.php`** -> AI Confidence: **99.31%**
152. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/RequestPayloadValueResolver.php`** -> AI Confidence: **99.31%**
153. **`src/Symfony/Component/HttpKernel/DataCollector/DumpDataCollector.php`** -> AI Confidence: **99.31%**
154. **`src/Symfony/Component/HttpKernel/DataCollector/EventDataCollector.php`** -> AI Confidence: **99.31%**
155. **`src/Symfony/Component/HttpKernel/DataCollector/LoggerDataCollector.php`** -> AI Confidence: **99.31%**
156. **`src/Symfony/Component/HttpKernel/DependencyInjection/RegisterControllerArgumentLocatorsPass.php`** -> AI Confidence: **99.31%**
157. **`src/Symfony/Component/HttpKernel/EventListener/AbstractSessionListener.php`** -> AI Confidence: **99.31%**
158. **`src/Symfony/Component/HttpKernel/EventListener/DebugHandlersListener.php`** -> AI Confidence: **99.31%**
159. **`src/Symfony/Component/HttpKernel/EventListener/DumpListener.php`** -> AI Confidence: **99.31%**
160. **`src/Symfony/Component/HttpKernel/EventListener/ProfilerListener.php`** -> AI Confidence: **99.31%**
161. **`src/Symfony/Component/HttpKernel/Kernel.php`** -> AI Confidence: **99.31%**
162. **`src/Symfony/Component/Intl/Data/Generator/TimezoneDataGenerator.php`** -> AI Confidence: **99.31%**
163. **`src/Symfony/Component/Intl/Resources/bin/update-data.php`** -> AI Confidence: **99.31%**
164. **`src/Symfony/Component/Intl/Util/IntlTestHelper.php`** -> AI Confidence: **99.31%**
165. **`src/Symfony/Component/JsonPath/JsonCrawler.php`** -> AI Confidence: **99.31%**
166. **`src/Symfony/Component/JsonStreamer/Write/PhpGenerator.php`** -> AI Confidence: **99.31%**
167. **`src/Symfony/Component/Lock/Bridge/DynamoDb/Store/DynamoDbStore.php`** -> AI Confidence: **99.31%**
168. **`src/Symfony/Component/Lock/Lock.php`** -> AI Confidence: **99.31%**
169. **`src/Symfony/Component/Lock/Store/CombinedStore.php`** -> AI Confidence: **99.31%**
170. **`src/Symfony/Component/Lock/Store/PostgreSqlStore.php`** -> AI Confidence: **99.31%**
171. **`src/Symfony/Component/Lock/Store/RedisStore.php`** -> AI Confidence: **99.31%**
172. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesApiAsyncAwsTransport.php`** -> AI Confidence: **99.31%**
173. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesHttpAsyncAwsTransport.php`** -> AI Confidence: **99.31%**
174. **`src/Symfony/Component/Mailer/Bridge/Amazon/Transport/SesSmtpTransport.php`** -> AI Confidence: **99.31%**
175. **`src/Symfony/Component/Mailer/Bridge/Mailchimp/Transport/MandrillApiTransport.php`** -> AI Confidence: **99.31%**
176. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Transport/MailgunApiTransport.php`** -> AI Confidence: **99.31%**
177. **`src/Symfony/Component/Mailer/Bridge/Mailjet/Transport/MailjetApiTransport.php`** -> AI Confidence: **99.31%**
178. **`src/Symfony/Component/Messenger/Bridge/AmazonSqs/Transport/Connection.php`** -> AI Confidence: **99.31%**
179. **`src/Symfony/Component/Messenger/Bridge/Amqp/Transport/AmqpReceiver.php`** -> AI Confidence: **99.31%**
180. **`src/Symfony/Component/Messenger/Bridge/Amqp/Transport/AmqpSender.php`** -> AI Confidence: **99.31%**
181. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/Connection.php`** -> AI Confidence: **99.31%**
182. **`src/Symfony/Component/Messenger/Bridge/Redis/Transport/RedisReceiver.php`** -> AI Confidence: **99.31%**
183. **`src/Symfony/Component/Messenger/Command/ConsumeMessagesCommand.php`** -> AI Confidence: **99.31%**
184. **`src/Symfony/Component/Messenger/Command/FailedMessagesRemoveCommand.php`** -> AI Confidence: **99.31%**
185. **`src/Symfony/Component/Messenger/Command/FailedMessagesRetryCommand.php`** -> AI Confidence: **99.31%**
186. **`src/Symfony/Component/Messenger/Command/FailedMessagesShowCommand.php`** -> AI Confidence: **99.31%**
187. **`src/Symfony/Component/Messenger/DependencyInjection/MessengerPass.php`** -> AI Confidence: **99.31%**
188. **`src/Symfony/Component/Messenger/Transport/TransportFactory.php`** -> AI Confidence: **99.31%**
189. **`src/Symfony/Component/Messenger/Worker.php`** -> AI Confidence: **99.31%**
190. **`src/Symfony/Component/Notifier/Bridge/Bluesky/BlueskyTransport.php`** -> AI Confidence: **99.31%**
191. **`src/Symfony/Component/Notifier/Bridge/ClickSend/ClickSendTransport.php`** -> AI Confidence: **99.31%**
192. **`src/Symfony/Component/Notifier/Bridge/ContactEveryone/ContactEveryoneTransport.php`** -> AI Confidence: **99.31%**
193. **`src/Symfony/Component/Notifier/Bridge/Engagespot/EngagespotTransport.php`** -> AI Confidence: **99.31%**
194. **`src/Symfony/Component/Notifier/Bridge/GoogleChat/GoogleChatTransport.php`** -> AI Confidence: **99.31%**
195. **`src/Symfony/Component/Notifier/Bridge/OneSignal/OneSignalTransport.php`** -> AI Confidence: **99.31%**
196. **`src/Symfony/Component/Notifier/Bridge/Slack/SlackTransport.php`** -> AI Confidence: **99.31%**
197. **`src/Symfony/Component/Notifier/Bridge/SmsFactor/SmsFactorTransport.php`** -> AI Confidence: **99.31%**
198. **`src/Symfony/Component/Notifier/Bridge/Telegram/TelegramTransport.php`** -> AI Confidence: **99.31%**
199. **`src/Symfony/Component/Notifier/Bridge/Twitter/TwitterTransport.php`** -> AI Confidence: **99.31%**
200. **`src/Symfony/Component/Notifier/Channel/EmailChannel.php`** -> AI Confidence: **99.31%**
201. **`src/Symfony/Component/ObjectMapper/ObjectMapper.php`** -> AI Confidence: **99.31%**
202. **`src/Symfony/Component/Process/Process.php`** -> AI Confidence: **99.31%**
203. **`src/Symfony/Component/PropertyAccess/PropertyAccessor.php`** -> AI Confidence: **99.31%**
204. **`src/Symfony/Component/PropertyInfo/Extractor/PhpDocExtractor.php`** -> AI Confidence: **99.31%**
205. **`src/Symfony/Component/PropertyInfo/Extractor/PhpStanExtractor.php`** -> AI Confidence: **99.31%**
206. **`src/Symfony/Component/PropertyInfo/Extractor/ReflectionExtractor.php`** -> AI Confidence: **99.31%**
207. **`src/Symfony/Component/PropertyInfo/Util/PhpDocTypeHelper.php`** -> AI Confidence: **99.31%**
208. **`src/Symfony/Component/Routing/Generator/CompiledUrlGenerator.php`** -> AI Confidence: **99.31%**
209. **`src/Symfony/Component/Routing/Matcher/UrlMatcher.php`** -> AI Confidence: **99.31%**
210. **`src/Symfony/Component/Routing/Tests/RouteCompilerTest.php`** -> AI Confidence: **99.31%**
211. **`src/Symfony/Component/Runtime/GenericRuntime.php`** -> AI Confidence: **99.31%**
212. **`src/Symfony/Component/Runtime/SymfonyRuntime.php`** -> AI Confidence: **99.31%**
213. **`src/Symfony/Component/Scheduler/DependencyInjection/AddScheduleMessengerPass.php`** -> AI Confidence: **99.31%**
214. **`src/Symfony/Component/Security/Core/Authorization/AccessDecisionManager.php`** -> AI Confidence: **99.31%**
215. **`src/Symfony/Component/Security/Csrf/SameOriginCsrfTokenManager.php`** -> AI Confidence: **99.31%**
216. **`src/Symfony/Component/Security/Http/Firewall/ContextListener.php`** -> AI Confidence: **99.31%**
217. **`src/Symfony/Component/Security/Http/HttpUtils.php`** -> AI Confidence: **99.31%**
218. **`src/Symfony/Component/Semaphore/Semaphore.php`** -> AI Confidence: **99.31%**
219. **`src/Symfony/Component/Semaphore/Store/RedisStore.php`** -> AI Confidence: **99.31%**
220. **`src/Symfony/Component/Serializer/DependencyInjection/SerializerPass.php`** -> AI Confidence: **99.31%**
221. **`src/Symfony/Component/Serializer/Encoder/XmlEncoder.php`** -> AI Confidence: **99.31%**
222. **`src/Symfony/Component/Serializer/Mapping/Loader/AttributeLoader.php`** -> AI Confidence: **99.31%**
223. **`src/Symfony/Component/Serializer/Mapping/Loader/XmlFileLoader.php`** -> AI Confidence: **99.31%**
224. **`src/Symfony/Component/Serializer/Mapping/Loader/YamlFileLoader.php`** -> AI Confidence: **99.31%**
225. **`src/Symfony/Component/Serializer/Normalizer/AbstractNormalizer.php`** -> AI Confidence: **99.31%**
226. **`src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php`** -> AI Confidence: **99.31%**
227. **`src/Symfony/Component/Serializer/Normalizer/ArrayDenormalizer.php`** -> AI Confidence: **99.31%**
228. **`src/Symfony/Component/Serializer/Normalizer/DataUriNormalizer.php`** -> AI Confidence: **99.31%**
229. **`src/Symfony/Component/Serializer/Normalizer/ObjectNormalizer.php`** -> AI Confidence: **99.31%**
230. **`src/Symfony/Component/Serializer/Normalizer/ProblemNormalizer.php`** -> AI Confidence: **99.31%**
231. **`src/Symfony/Component/Serializer/Serializer.php`** -> AI Confidence: **99.31%**
232. **`src/Symfony/Component/String/Slugger/AsciiSlugger.php`** -> AI Confidence: **99.31%**
233. **`src/Symfony/Component/Translation/Loader/XliffFileLoader.php`** -> AI Confidence: **99.31%**
234. **`src/Symfony/Component/Translation/Resources/bin/translation-status.php`** -> AI Confidence: **99.31%**
235. **`src/Symfony/Component/Validator/Constraints/AbstractComparison.php`** -> AI Confidence: **99.31%**
236. **`src/Symfony/Component/Validator/Constraints/AtLeastOneOf.php`** -> AI Confidence: **99.31%**
237. **`src/Symfony/Component/Validator/Constraints/Bic.php`** -> AI Confidence: **99.31%**
238. **`src/Symfony/Component/Validator/Constraints/EmailValidator.php`** -> AI Confidence: **99.31%**
239. **`src/Symfony/Component/Validator/Constraints/FileValidator.php`** -> AI Confidence: **99.31%**
240. **`src/Symfony/Component/Validator/Constraints/Hostname.php`** -> AI Confidence: **99.31%**
241. **`src/Symfony/Component/Validator/Constraints/Issn.php`** -> AI Confidence: **99.31%**
242. **`src/Symfony/Component/Validator/Constraints/PasswordStrength.php`** -> AI Confidence: **99.31%**
243. **`src/Symfony/Component/Validator/Constraints/Range.php`** -> AI Confidence: **99.31%**
244. **`src/Symfony/Component/Validator/Constraints/RangeValidator.php`** -> AI Confidence: **99.31%**
245. **`src/Symfony/Component/Validator/Constraints/UlidValidator.php`** -> AI Confidence: **99.31%**
246. **`src/Symfony/Component/Validator/Constraints/Url.php`** -> AI Confidence: **99.31%**
247. **`src/Symfony/Component/Validator/Constraints/WordCount.php`** -> AI Confidence: **99.31%**
248. **`src/Symfony/Component/Validator/Mapping/Factory/LazyLoadingMetadataFactory.php`** -> AI Confidence: **99.31%**
249. **`src/Symfony/Component/Validator/Mapping/Loader/PropertyInfoLoader.php`** -> AI Confidence: **99.31%**
250. **`src/Symfony/Component/Validator/Validator/RecursiveContextualValidator.php`** -> AI Confidence: **99.31%**
251. **`src/Symfony/Component/Workflow/Dumper/GraphvizDumper.php`** -> AI Confidence: **99.31%**
252. **`phpunit`** -> AI Confidence: **99.29%**
253. **`src/Symfony/Bridge/PhpUnit/Tests/DeprecationErrorHandler/deprecation/deprecation.php`** -> AI Confidence: **99.29%**
254. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/asset_mapper_without_assets.php`** -> AI Confidence: **99.29%**
255. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets.php`** -> AI Confidence: **99.29%**
256. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets_disabled.php`** -> AI Confidence: **99.29%**
257. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/assets_version_strategy_as_service.php`** -> AI Confidence: **99.29%**
258. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache.php`** -> AI Confidence: **99.29%**
259. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache_app_redis_tag_aware.php`** -> AI Confidence: **99.29%**
260. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/cache_app_redis_tag_aware_pool.php`** -> AI Confidence: **99.29%**
261. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/csrf.php`** -> AI Confidence: **99.29%**
262. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/csrf_needs_session.php`** -> AI Confidence: **99.29%**
263. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/default_config.php`** -> AI Confidence: **99.29%**
264. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/esi_and_ssi_without_fragments.php`** -> AI Confidence: **99.29%**
265. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/esi_disabled.php`** -> AI Confidence: **99.29%**
266. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_csrf_disabled.php`** -> AI Confidence: **99.29%**
267. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_csrf_field_attr.php`** -> AI Confidence: **99.29%**
268. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_default_csrf.php`** -> AI Confidence: **99.29%**
269. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/form_no_csrf.php`** -> AI Confidence: **99.29%**
270. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/fragments_and_hinclude.php`** -> AI Confidence: **99.29%**
271. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/html_sanitizer_default_allowed_link_and_media_hosts.php`** -> AI Confidence: **99.29%**
272. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/html_sanitizer_default_config.php`** -> AI Confidence: **99.29%**
273. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_caching.php`** -> AI Confidence: **99.29%**
274. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_default_options.php`** -> AI Confidence: **99.29%**
275. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_full_default_options.php`** -> AI Confidence: **99.29%**
276. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_mock.php`** -> AI Confidence: **99.29%**
277. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_mock_response_factory.php`** -> AI Confidence: **99.29%**
278. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_override_default_options.php`** -> AI Confidence: **99.29%**
279. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_rate_limiter.php`** -> AI Confidence: **99.29%**
280. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_retry.php`** -> AI Confidence: **99.29%**
281. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_scoped_without_query_option.php`** -> AI Confidence: **99.29%**
282. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/http_client_xml_key.php`** -> AI Confidence: **99.29%**
283. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/json_streamer.php`** -> AI Confidence: **99.29%**
284. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock.php`** -> AI Confidence: **99.29%**
285. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock_named.php`** -> AI Confidence: **99.29%**
286. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock_service.php`** -> AI Confidence: **99.29%**
287. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/lock_service_and_env.php`** -> AI Confidence: **99.29%**
288. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer.php`** -> AI Confidence: **99.29%**
289. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer_with_disabled_message_bus.php`** -> AI Confidence: **99.29%**
290. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/mailer_with_specific_message_bus.php`** -> AI Confidence: **99.29%**
291. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_bus_name_stamp.php`** -> AI Confidence: **99.29%**
292. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_disabled.php`** -> AI Confidence: **99.29%**
293. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_middleware_factory_erroneous_format.php`** -> AI Confidence: **99.29%**
294. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_buses_with_deduplicate_middleware.php`** -> AI Confidence: **99.29%**
295. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_buses_without_deduplicate_middleware.php`** -> AI Confidence: **99.29%**
296. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_failure_transports.php`** -> AI Confidence: **99.29%**
297. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_multiple_failure_transports_global.php`** -> AI Confidence: **99.29%**
298. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_routing_invalid_wildcard.php`** -> AI Confidence: **99.29%**
299. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_transport.php`** -> AI Confidence: **99.29%**
300. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/messenger_transports.php`** -> AI Confidence: **99.29%**
301. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier.php`** -> AI Confidence: **99.29%**
302. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_with_disabled_message_bus.php`** -> AI Confidence: **99.29%**
303. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_with_specific_message_bus.php`** -> AI Confidence: **99.29%**
304. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_mailer.php`** -> AI Confidence: **99.29%**
305. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_messenger.php`** -> AI Confidence: **99.29%**
306. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/notifier_without_transports.php`** -> AI Confidence: **99.29%**
307. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_disabled.php`** -> AI Confidence: **99.29%**
308. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_enabled.php`** -> AI Confidence: **99.29%**
309. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_log_level.php`** -> AI Confidence: **99.29%**
310. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/php_errors_log_levels.php`** -> AI Confidence: **99.29%**
311. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/profiler.php`** -> AI Confidence: **99.29%**
312. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_accessor.php`** -> AI Confidence: **99.29%**
313. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_info.php`** -> AI Confidence: **99.29%**
314. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/property_info_without_constructor_extractor.php`** -> AI Confidence: **99.29%**
315. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/request.php`** -> AI Confidence: **99.29%**
316. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/router_enabled_locales_env.php`** -> AI Confidence: **99.29%**
317. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore.php`** -> AI Confidence: **99.29%**
318. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_lock.php`** -> AI Confidence: **99.29%**
319. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_lock_named.php`** -> AI Confidence: **99.29%**
320. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_named.php`** -> AI Confidence: **99.29%**
321. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/semaphore_service.php`** -> AI Confidence: **99.29%**
322. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_disabled.php`** -> AI Confidence: **99.29%**
323. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_enabled.php`** -> AI Confidence: **99.29%**
324. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_mapping.php`** -> AI Confidence: **99.29%**
325. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_mapping_without_attributes.php`** -> AI Confidence: **99.29%**
326. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/serializer_without_translator.php`** -> AI Confidence: **99.29%**
327. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/session.php`** -> AI Confidence: **99.29%**
328. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/session_cookie_secure_auto.php`** -> AI Confidence: **99.29%**
329. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/ssi_disabled.php`** -> AI Confidence: **99.29%**
330. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_cache_dir_disabled.php`** -> AI Confidence: **99.29%**
331. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_fallbacks.php`** -> AI Confidence: **99.29%**
332. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_globals.php`** -> AI Confidence: **99.29%**
333. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_providers.php`** -> AI Confidence: **99.29%**
334. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/translator_without_globals.php`** -> AI Confidence: **99.29%**
335. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/trusted_proxies_private_ranges.php`** -> AI Confidence: **99.29%**
336. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/type_info.php`** -> AI Confidence: **99.29%**
337. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_attributes.php`** -> AI Confidence: **99.29%**
338. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_auto_mapping.php`** -> AI Confidence: **99.29%**
339. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_email_validation_mode.php`** -> AI Confidence: **99.29%**
340. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_mapping.php`** -> AI Confidence: **99.29%**
341. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_multiple_static_methods.php`** -> AI Confidence: **99.29%**
342. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_no_static_method.php`** -> AI Confidence: **99.29%**
343. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/validation_translation_domain.php`** -> AI Confidence: **99.29%**
344. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/web_link.php`** -> AI Confidence: **99.29%**
345. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/webhook.php`** -> AI Confidence: **99.29%**
346. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/webhook_without_serializer.php`** -> AI Confidence: **99.29%**
347. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/workflow_without_support_and_support_strategy.php`** -> AI Confidence: **99.29%**
348. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/Fixtures/php/workflows_enabled.php`** -> AI Confidence: **99.29%**
349. **`src/Symfony/Bundle/FrameworkBundle/Tests/Fixtures/Resources/views/translation.html.php`** -> AI Confidence: **99.29%**
350. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_customized_config.php`** -> AI Confidence: **99.29%**
351. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_default_strategy.php`** -> AI Confidence: **99.29%**
352. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_service.php`** -> AI Confidence: **99.29%**
353. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_service_and_strategy.php`** -> AI Confidence: **99.29%**
354. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_decision_manager_strategy_service.php`** -> AI Confidence: **99.29%**
355. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc.php`** -> AI Confidence: **99.29%**
356. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_encryption.php`** -> AI Confidence: **99.29%**
357. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_user_info_discovery.php`** -> AI Confidence: **99.29%**
358. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/access_token_oidc_user_info_multiple_discovery.php`** -> AI Confidence: **99.29%**
359. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/argon2i_hasher.php`** -> AI Confidence: **99.29%**
360. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/bcrypt_hasher.php`** -> AI Confidence: **99.29%**
361. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_patterns.php`** -> AI Confidence: **99.29%**
362. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_provider.php`** -> AI Confidence: **99.29%**
363. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/firewall_undefined_provider.php`** -> AI Confidence: **99.29%**
364. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/listener_provider.php`** -> AI Confidence: **99.29%**
365. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/listener_undefined_provider.php`** -> AI Confidence: **99.29%**
366. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/logout_clear_site_data.php`** -> AI Confidence: **99.29%**
367. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/merge.php`** -> AI Confidence: **99.29%**
368. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/merge_import.php`** -> AI Confidence: **99.29%**
369. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/migrating_hasher.php`** -> AI Confidence: **99.29%**
370. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/no_custom_user_checker.php`** -> AI Confidence: **99.29%**
371. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/remember_me_options.php`** -> AI Confidence: **99.29%**
372. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/sodium_hasher.php`** -> AI Confidence: **99.29%**
373. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/customTemplateEscapingGuesser.php`** -> AI Confidence: **99.29%**
374. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/empty.php`** -> AI Confidence: **99.29%**
375. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/extra.php`** -> AI Confidence: **99.29%**
376. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/formats.php`** -> AI Confidence: **99.29%**
377. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/full.php`** -> AI Confidence: **99.29%**
378. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/mailer.php`** -> AI Confidence: **99.29%**
379. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/no-cache.php`** -> AI Confidence: **99.29%**
380. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/path-cache.php`** -> AI Confidence: **99.29%**
381. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/Fixtures/php/prod-cache.php`** -> AI Confidence: **99.29%**
382. **`src/Symfony/Bundle/WebProfilerBundle/Tests/Fixtures/hello_world.php`** -> AI Confidence: **99.29%**
383. **`src/Symfony/Component/Cache/Traits/RedisTrait.php`** -> AI Confidence: **99.29%**
384. **`src/Symfony/Component/Console/Helper/OutputWrapper.php`** -> AI Confidence: **99.29%**
385. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/config/legacy_internal_scope.php`** -> AI Confidence: **99.29%**
386. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/directory/simple.php`** -> AI Confidence: **99.29%**
387. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services2.php`** -> AI Confidence: **99.29%**
388. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/simple.php`** -> AI Confidence: **99.29%**
389. **`src/Symfony/Component/Emoji/Resources/data/emoji-cs.php`** -> AI Confidence: **99.29%**
390. **`src/Symfony/Component/Emoji/Resources/data/emoji-da.php`** -> AI Confidence: **99.29%**
391. **`src/Symfony/Component/Emoji/Resources/data/emoji-hi_latn.php`** -> AI Confidence: **99.29%**
392. **`src/Symfony/Component/Emoji/Resources/data/emoji-kl.php`** -> AI Confidence: **99.29%**
393. **`src/Symfony/Component/Emoji/Resources/data/emoji-lij.php`** -> AI Confidence: **99.29%**
394. **`src/Symfony/Component/Emoji/Resources/data/emoji-no.php`** -> AI Confidence: **99.29%**
395. **`src/Symfony/Component/Emoji/Resources/data/emoji-pl.php`** -> AI Confidence: **99.29%**
396. **`src/Symfony/Component/Emoji/Resources/data/emoji-pt.php`** -> AI Confidence: **99.29%**
397. **`src/Symfony/Component/ErrorHandler/Resources/views/logs.html.php`** -> AI Confidence: **99.29%**
398. **`src/Symfony/Component/ErrorHandler/Tests/Fixtures/ClassAlias.php`** -> AI Confidence: **99.29%**
399. **`src/Symfony/Component/ExpressionLanguage/Lexer.php`** -> AI Confidence: **99.29%**
400. **`src/Symfony/Component/ExpressionLanguage/Resources/bin/generate_operator_regex.php`** -> AI Confidence: **99.29%**
401. **`src/Symfony/Component/Filesystem/Tests/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
402. **`src/Symfony/Component/Finder/Glob.php`** -> AI Confidence: **99.29%**
403. **`src/Symfony/Component/HttpClient/Tests/Fixtures/response-functional/index.php`** -> AI Confidence: **99.29%**
404. **`src/Symfony/Component/Intl/Resources/data/currencies/pt.php`** -> AI Confidence: **99.29%**
405. **`src/Symfony/Component/Intl/Resources/data/currencies/pt_PT.php`** -> AI Confidence: **99.29%**
406. **`src/Symfony/Component/Intl/Resources/data/languages/gl.php`** -> AI Confidence: **99.29%**
407. **`src/Symfony/Component/Intl/Resources/data/languages/pt.php`** -> AI Confidence: **99.29%**
408. **`src/Symfony/Component/Intl/Resources/data/languages/pt_PT.php`** -> AI Confidence: **99.29%**
409. **`src/Symfony/Component/Intl/Resources/data/locales/gl.php`** -> AI Confidence: **99.29%**
410. **`src/Symfony/Component/Intl/Resources/data/locales/pt.php`** -> AI Confidence: **99.29%**
411. **`src/Symfony/Component/Intl/Resources/data/locales/pt_PT.php`** -> AI Confidence: **99.29%**
412. **`src/Symfony/Component/Intl/Resources/data/regions/gl.php`** -> AI Confidence: **99.29%**
413. **`src/Symfony/Component/Intl/Resources/data/regions/pt.php`** -> AI Confidence: **99.29%**
414. **`src/Symfony/Component/Intl/Resources/data/regions/pt_PT.php`** -> AI Confidence: **99.29%**
415. **`src/Symfony/Component/Intl/Resources/data/timezones/gl.php`** -> AI Confidence: **99.29%**
416. **`src/Symfony/Component/Intl/Resources/data/timezones/nn.php`** -> AI Confidence: **99.29%**
417. **`src/Symfony/Component/Intl/Resources/data/timezones/no.php`** -> AI Confidence: **99.29%**
418. **`src/Symfony/Component/Intl/Resources/data/timezones/pt.php`** -> AI Confidence: **99.29%**
419. **`src/Symfony/Component/Intl/Resources/data/timezones/pt_PT.php`** -> AI Confidence: **99.29%**
420. **`src/Symfony/Component/Mailer/Tests/Transport/Fixtures/fake-failing-sendmail.php`** -> AI Confidence: **99.29%**
421. **`src/Symfony/Component/Mailer/Tests/Transport/Fixtures/fake-sendmail.php`** -> AI Confidence: **99.29%**
422. **`src/Symfony/Component/Mime/Tests/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
423. **`src/Symfony/Component/Notifier/Bridge/Primotexto/PrimotextoErrorCode.php`** -> AI Confidence: **99.29%**
424. **`src/Symfony/Component/Process/Tests/Fixtures/memory.php`** -> AI Confidence: **99.29%**
425. **`src/Symfony/Component/Process/Tests/NonStopableProcess.php`** -> AI Confidence: **99.29%**
426. **`src/Symfony/Component/Process/Tests/PipeStdinInStdoutStdErrStreamSelect.php`** -> AI Confidence: **99.29%**
427. **`src/Symfony/Component/Process/Tests/ThreeSecondProcess.php`** -> AI Confidence: **99.29%**
428. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher1.php`** -> AI Confidence: **99.29%**
429. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher11.php`** -> AI Confidence: **99.29%**
430. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher12.php`** -> AI Confidence: **99.29%**
431. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher13.php`** -> AI Confidence: **99.29%**
432. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher2.php`** -> AI Confidence: **99.29%**
433. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher6.php`** -> AI Confidence: **99.29%**
434. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher7.php`** -> AI Confidence: **99.29%**
435. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher8.php`** -> AI Confidence: **99.29%**
436. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-7.3/translation.html.php`** -> AI Confidence: **99.29%**
437. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translatable-short-fqn.html.php`** -> AI Confidence: **99.29%**
438. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translatable-short.html.php`** -> AI Confidence: **99.29%**
439. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor-ast/translation.html.php`** -> AI Confidence: **99.29%**
440. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor/translatable-short.html.php`** -> AI Confidence: **99.29%**
441. **`src/Symfony/Component/Translation/Tests/Fixtures/extractor/translation.html.php`** -> AI Confidence: **99.29%**
442. **`src/Symfony/Component/VarDumper/Cloner/VarCloner.php`** -> AI Confidence: **99.29%**
443. **`src/Symfony/Contracts/Deprecation/function.php`** -> AI Confidence: **99.29%**
444. **`src/Symfony/Contracts/HttpClient/Test/Fixtures/web/index.php`** -> AI Confidence: **99.29%**
445. **`src/Symfony/Component/Console/Resources/completion.bash`** -> AI Confidence: **99.29%**
446. **`src/Symfony/Component/Console/Resources/completion.fish`** -> AI Confidence: **99.29%**
447. **`src/Symfony/Component/Console/Resources/completion.zsh`** -> AI Confidence: **99.29%**
448. **`src/Symfony/Component/Translation/Tests/Fixtures/resources.ts`** -> AI Confidence: **99.29%**
449. **`src/Symfony/Component/HttpClient/Response/TransportResponseTrait.php`** -> AI Confidence: **99.28%**
450. **`src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolverTrait.php`** -> AI Confidence: **99.25%**
451. **`src/Symfony/Component/Cache/Traits/AbstractAdapterTrait.php`** -> AI Confidence: **99.25%**
452. **`src/Symfony/Component/Cache/Traits/ContractsTrait.php`** -> AI Confidence: **99.25%**
453. **`src/Symfony/Component/Lock/Store/DatabaseTableTrait.php`** -> AI Confidence: **99.25%**
454. **`src/Symfony/Bridge/Doctrine/DependencyInjection/CompilerPass/RegisterEventListenersAndSubscribersPass.php`** -> AI Confidence: **99.24%**
455. **`src/Symfony/Bridge/Doctrine/Validator/Constraints/UniqueEntityValidator.php`** -> AI Confidence: **99.24%**
456. **`src/Symfony/Bridge/Twig/Command/LintCommand.php`** -> AI Confidence: **99.24%**
457. **`src/Symfony/Bridge/Twig/EventListener/TemplateAttributeListener.php`** -> AI Confidence: **99.24%**
458. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolClearCommand.php`** -> AI Confidence: **99.24%**
459. **`src/Symfony/Bundle/FrameworkBundle/Command/ConfigDumpReferenceCommand.php`** -> AI Confidence: **99.24%**
460. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsListCommand.php`** -> AI Confidence: **99.24%**
461. **`src/Symfony/Bundle/FrameworkBundle/Command/TranslationDebugCommand.php`** -> AI Confidence: **99.24%**
462. **`src/Symfony/Bundle/FrameworkBundle/Console/Application.php`** -> AI Confidence: **99.24%**
463. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`** -> AI Confidence: **99.24%**
464. **`src/Symfony/Bundle/FrameworkBundle/EventListener/ConsoleProfilerListener.php`** -> AI Confidence: **99.24%**
465. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ApiAttributesTest.php`** -> AI Confidence: **99.24%**
466. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/CachePoolsTest.php`** -> AI Confidence: **99.24%**
467. **`src/Symfony/Bundle/SecurityBundle/DataCollector/SecurityDataCollector.php`** -> AI Confidence: **99.24%**
468. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/SecurityExtension.php`** -> AI Confidence: **99.24%**
469. **`src/Symfony/Component/Asset/Tests/UrlPackageTest.php`** -> AI Confidence: **99.24%**
470. **`src/Symfony/Component/BrowserKit/AbstractBrowser.php`** -> AI Confidence: **99.24%**
471. **`src/Symfony/Component/BrowserKit/HttpBrowser.php`** -> AI Confidence: **99.24%**
472. **`src/Symfony/Component/Cache/Adapter/ChainAdapter.php`** -> AI Confidence: **99.24%**
473. **`src/Symfony/Component/Console/ArgumentResolver/ArgumentResolver.php`** -> AI Confidence: **99.24%**
474. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/MapInputValueResolver.php`** -> AI Confidence: **99.24%**
475. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/UidValueResolver.php`** -> AI Confidence: **99.24%**
476. **`src/Symfony/Component/Console/Command/Command.php`** -> AI Confidence: **99.24%**
477. **`src/Symfony/Component/Console/Command/DumpCompletionCommand.php`** -> AI Confidence: **99.24%**
478. **`src/Symfony/Component/Console/Input/InputArgument.php`** -> AI Confidence: **99.24%**
479. **`src/Symfony/Component/Console/Style/SymfonyStyle.php`** -> AI Confidence: **99.24%**
480. **`src/Symfony/Component/Console/Tester/CommandTester.php`** -> AI Confidence: **99.24%**
481. **`src/Symfony/Component/DependencyInjection/Compiler/MergeExtensionConfigurationPass.php`** -> AI Confidence: **99.24%**
482. **`src/Symfony/Component/DependencyInjection/Compiler/ServiceLocatorTagPass.php`** -> AI Confidence: **99.24%**
483. **`src/Symfony/Component/DependencyInjection/Dumper/GraphvizDumper.php`** -> AI Confidence: **99.24%**
484. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/AbstractConfigurator.php`** -> AI Confidence: **99.24%**
485. **`src/Symfony/Component/Dotenv/Command/DotenvDumpCommand.php`** -> AI Confidence: **99.24%**
486. **`src/Symfony/Component/Form/Command/DebugCommand.php`** -> AI Confidence: **99.24%**
487. **`src/Symfony/Component/Form/Extension/Core/Type/DateTimeType.php`** -> AI Confidence: **99.24%**
488. **`src/Symfony/Component/Form/Extension/Core/Type/DateType.php`** -> AI Confidence: **99.24%**
489. **`src/Symfony/Component/Form/Extension/Core/Type/MoneyType.php`** -> AI Confidence: **99.24%**
490. **`src/Symfony/Component/Form/Extension/Core/Type/TimeType.php`** -> AI Confidence: **99.24%**
491. **`src/Symfony/Component/Form/Extension/Csrf/Type/FormTypeCsrfExtension.php`** -> AI Confidence: **99.24%**
492. **`src/Symfony/Component/Form/Extension/HttpFoundation/HttpFoundationRequestHandler.php`** -> AI Confidence: **99.24%**
493. **`src/Symfony/Component/HttpClient/AmpHttpClient.php`** -> AI Confidence: **99.24%**
494. **`src/Symfony/Component/HttpClient/Internal/AmpClientState.php`** -> AI Confidence: **99.24%**
495. **`src/Symfony/Component/HttpFoundation/File/UploadedFile.php`** -> AI Confidence: **99.24%**
496. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver.php`** -> AI Confidence: **99.24%**
497. **`src/Symfony/Component/HttpKernel/EventListener/CacheAttributeListener.php`** -> AI Confidence: **99.24%**
498. **`src/Symfony/Component/HttpKernel/EventListener/ErrorListener.php`** -> AI Confidence: **99.24%**
499. **`src/Symfony/Component/HttpKernel/EventListener/RouterListener.php`** -> AI Confidence: **99.24%**
500. **`src/Symfony/Component/HttpKernel/Fragment/HIncludeFragmentRenderer.php`** -> AI Confidence: **99.24%**
501. **`src/Symfony/Component/HttpKernel/HttpKernel.php`** -> AI Confidence: **99.24%**
502. **`src/Symfony/Component/Intl/Currencies.php`** -> AI Confidence: **99.24%**
503. **`src/Symfony/Component/JsonStreamer/Read/PhpGenerator.php`** -> AI Confidence: **99.24%**
504. **`src/Symfony/Component/JsonStreamer/StreamerDumper.php`** -> AI Confidence: **99.24%**
505. **`src/Symfony/Component/Ldap/Adapter/ExtLdap/Connection.php`** -> AI Confidence: **99.24%**
506. **`src/Symfony/Component/Ldap/Security/CheckLdapCredentialsListener.php`** -> AI Confidence: **99.24%**
507. **`src/Symfony/Component/Ldap/Security/LdapUserProvider.php`** -> AI Confidence: **99.24%**
508. **`src/Symfony/Component/Lock/Store/DoctrineDbalPostgreSqlStore.php`** -> AI Confidence: **99.24%**
509. **`src/Symfony/Component/Lock/Store/StoreFactory.php`** -> AI Confidence: **99.24%**
510. **`src/Symfony/Component/Lock/Tests/Store/BlockingStoreTestTrait.php`** -> AI Confidence: **99.24%**
511. **`src/Symfony/Component/Mailer/Bridge/AhaSend/Transport/AhaSendApiTransport.php`** -> AI Confidence: **99.24%**
512. **`src/Symfony/Component/Mailer/Bridge/Brevo/Transport/BrevoApiTransport.php`** -> AI Confidence: **99.24%**
513. **`src/Symfony/Component/Mailer/Bridge/Infobip/Transport/InfobipApiTransport.php`** -> AI Confidence: **99.24%**
514. **`src/Symfony/Component/Mailer/Bridge/MailPace/Transport/MailPaceApiTransport.php`** -> AI Confidence: **99.24%**
515. **`src/Symfony/Component/Mailer/Bridge/MailerSend/Transport/MailerSendApiTransport.php`** -> AI Confidence: **99.24%**
516. **`src/Symfony/Component/Mailer/Bridge/Mailtrap/Transport/MailtrapApiTransport.php`** -> AI Confidence: **99.24%**
517. **`src/Symfony/Component/Mailer/Bridge/Postmark/Transport/PostmarkApiTransport.php`** -> AI Confidence: **99.24%**
518. **`src/Symfony/Component/Mailer/Bridge/Resend/Transport/ResendApiTransport.php`** -> AI Confidence: **99.24%**
519. **`src/Symfony/Component/Mailer/Bridge/Scaleway/Transport/ScalewayApiTransport.php`** -> AI Confidence: **99.24%**
520. **`src/Symfony/Component/Mailer/Transport/AbstractHttpTransport.php`** -> AI Confidence: **99.24%**
521. **`src/Symfony/Component/Mailer/Transport/SendmailTransport.php`** -> AI Confidence: **99.24%**
522. **`src/Symfony/Component/Mailer/Transport/Smtp/EsmtpTransport.php`** -> AI Confidence: **99.24%**
523. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Tests/Transport/ConnectionTest.php`** -> AI Confidence: **99.24%**
524. **`src/Symfony/Component/Messenger/Command/AbstractFailedMessagesCommand.php`** -> AI Confidence: **99.24%**
525. **`src/Symfony/Component/Messenger/EventListener/SendFailedMessageForRetryListener.php`** -> AI Confidence: **99.24%**
526. **`src/Symfony/Component/Messenger/Middleware/DecodeFailedMessageMiddleware.php`** -> AI Confidence: **99.24%**
527. **`src/Symfony/Component/Messenger/Middleware/HandleMessageMiddleware.php`** -> AI Confidence: **99.24%**
528. **`src/Symfony/Component/Notifier/Bridge/AmazonSns/AmazonSnsTransport.php`** -> AI Confidence: **99.24%**
529. **`src/Symfony/Component/Notifier/Bridge/Bandwidth/BandwidthTransport.php`** -> AI Confidence: **99.24%**
530. **`src/Symfony/Component/Notifier/Bridge/Brevo/BrevoTransport.php`** -> AI Confidence: **99.24%**
531. **`src/Symfony/Component/Notifier/Bridge/Esendex/EsendexTransport.php`** -> AI Confidence: **99.24%**
532. **`src/Symfony/Component/Notifier/Bridge/Expo/ExpoTransport.php`** -> AI Confidence: **99.24%**
533. **`src/Symfony/Component/Notifier/Bridge/FakeChat/Tests/FakeChatTransportFactoryTest.php`** -> AI Confidence: **99.24%**
534. **`src/Symfony/Component/Notifier/Bridge/FakeSms/Tests/FakeSmsTransportFactoryTest.php`** -> AI Confidence: **99.24%**
535. **`src/Symfony/Component/Notifier/Bridge/Firebase/FirebaseTransport.php`** -> AI Confidence: **99.24%**
536. **`src/Symfony/Component/Notifier/Bridge/Isendpro/IsendproTransport.php`** -> AI Confidence: **99.24%**
537. **`src/Symfony/Component/Notifier/Bridge/Lox24/Webhook/Lox24RequestParser.php`** -> AI Confidence: **99.24%**
538. **`src/Symfony/Component/Notifier/Bridge/Mattermost/MattermostTransport.php`** -> AI Confidence: **99.24%**
539. **`src/Symfony/Component/Notifier/Bridge/MessageBird/MessageBirdTransport.php`** -> AI Confidence: **99.24%**
540. **`src/Symfony/Component/Notifier/Bridge/MessageMedia/MessageMediaTransport.php`** -> AI Confidence: **99.24%**
541. **`src/Symfony/Component/Notifier/Bridge/Ntfy/NtfyTransport.php`** -> AI Confidence: **99.24%**
542. **`src/Symfony/Component/Notifier/Bridge/Plivo/PlivoTransport.php`** -> AI Confidence: **99.24%**
543. **`src/Symfony/Component/Notifier/Bridge/Primotexto/PrimotextoTransport.php`** -> AI Confidence: **99.24%**
544. **`src/Symfony/Component/Notifier/Bridge/Redlink/RedlinkTransport.php`** -> AI Confidence: **99.24%**
545. **`src/Symfony/Component/Notifier/Bridge/RingCentral/RingCentralTransport.php`** -> AI Confidence: **99.24%**
546. **`src/Symfony/Component/Notifier/Bridge/SmsBiuras/SmsBiurasTransport.php`** -> AI Confidence: **99.24%**
547. **`src/Symfony/Component/Notifier/Bridge/Smsbox/SmsboxTransport.php`** -> AI Confidence: **99.24%**
548. **`src/Symfony/Component/Notifier/Bridge/Smsmode/SmsmodeTransport.php`** -> AI Confidence: **99.24%**
549. **`src/Symfony/Component/Notifier/Bridge/Telnyx/TelnyxTransport.php`** -> AI Confidence: **99.24%**
550. **`src/Symfony/Component/Notifier/Bridge/Termii/TermiiTransport.php`** -> AI Confidence: **99.24%**
551. **`src/Symfony/Component/Notifier/Bridge/Twilio/TwilioTransport.php`** -> AI Confidence: **99.24%**
552. **`src/Symfony/Component/Notifier/Bridge/Zendesk/ZendeskTransport.php`** -> AI Confidence: **99.24%**
553. **`src/Symfony/Component/OptionsResolver/OptionsResolver.php`** -> AI Confidence: **99.24%**
554. **`src/Symfony/Component/RateLimiter/Policy/SlidingWindowLimiter.php`** -> AI Confidence: **99.24%**
555. **`src/Symfony/Component/RateLimiter/Policy/TokenBucketLimiter.php`** -> AI Confidence: **99.24%**
556. **`src/Symfony/Component/Routing/Loader/AttributeClassLoader.php`** -> AI Confidence: **99.24%**
557. **`src/Symfony/Component/Routing/Matcher/Dumper/CompiledUrlMatcherDumper.php`** -> AI Confidence: **99.24%**
558. **`src/Symfony/Component/Routing/RouteCollection.php`** -> AI Confidence: **99.24%**
559. **`src/Symfony/Component/Runtime/Internal/ComposerPlugin.php`** -> AI Confidence: **99.24%**
560. **`src/Symfony/Component/Scheduler/Scheduler.php`** -> AI Confidence: **99.24%**
561. **`src/Symfony/Component/Security/Http/AccessToken/OAuth2/Oauth2TokenHandler.php`** -> AI Confidence: **99.24%**
562. **`src/Symfony/Component/Security/Http/Authentication/AuthenticatorManager.php`** -> AI Confidence: **99.24%**
563. **`src/Symfony/Component/Security/Http/Authentication/DefaultAuthenticationFailureHandler.php`** -> AI Confidence: **99.24%**
564. **`src/Symfony/Component/Security/Http/EventListener/IsGrantedAttributeListener.php`** -> AI Confidence: **99.24%**
565. **`src/Symfony/Component/Security/Http/Firewall/ExceptionListener.php`** -> AI Confidence: **99.24%**
566. **`src/Symfony/Component/Semaphore/Store/LockStore.php`** -> AI Confidence: **99.24%**
567. **`src/Symfony/Component/Serializer/Normalizer/MimeMessageNormalizer.php`** -> AI Confidence: **99.24%**
568. **`src/Symfony/Component/Translation/Bridge/Phrase/PhraseProvider.php`** -> AI Confidence: **99.24%**
569. **`src/Symfony/Component/Translation/Command/XliffLintCommand.php`** -> AI Confidence: **99.24%**
570. **`src/Symfony/Component/Translation/Translator.php`** -> AI Confidence: **99.24%**
571. **`src/Symfony/Component/TypeInfo/TypeContext/TypeContextFactory.php`** -> AI Confidence: **99.24%**
572. **`src/Symfony/Component/TypeInfo/TypeFactoryTrait.php`** -> AI Confidence: **99.24%**
573. **`src/Symfony/Component/TypeInfo/TypeResolver/PhpDocAwareReflectionTypeResolver.php`** -> AI Confidence: **99.24%**
574. **`src/Symfony/Component/TypeInfo/TypeResolver/StringTypeResolver.php`** -> AI Confidence: **99.24%**
575. **`src/Symfony/Component/Uid/Command/GenerateUuidCommand.php`** -> AI Confidence: **99.24%**
576. **`src/Symfony/Component/Validator/Constraints/AbstractComparisonValidator.php`** -> AI Confidence: **99.24%**
577. **`src/Symfony/Component/Validator/Constraints/BicValidator.php`** -> AI Confidence: **99.24%**
578. **`src/Symfony/Component/Validator/Constraints/Expression.php`** -> AI Confidence: **99.24%**
579. **`src/Symfony/Component/Workflow/EventListener/GuardListener.php`** -> AI Confidence: **99.24%**
580. **`src/Symfony/Component/Workflow/Workflow.php`** -> AI Confidence: **99.24%**
581. **`src/Symfony/Component/Yaml/Command/LintCommand.php`** -> AI Confidence: **99.24%**
582. **`src/Symfony/Contracts/HttpClient/Test/HttpClientTestCase.php`** -> AI Confidence: **99.24%**
583. **`src/Symfony/Bridge/Monolog/Handler/MailerHandler.php`** -> AI Confidence: **99.23%**
584. **`src/Symfony/Bridge/PhpUnit/Legacy/CommandForV9.php`** -> AI Confidence: **99.23%**
585. **`src/Symfony/Bridge/Twig/Validator/Constraints/TwigValidator.php`** -> AI Confidence: **99.23%**
586. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsDecryptToLocalCommand.php`** -> AI Confidence: **99.23%**
587. **`src/Symfony/Bundle/FrameworkBundle/HttpCache/HttpCache.php`** -> AI Confidence: **99.23%**
588. **`src/Symfony/Bundle/FrameworkBundle/Test/HttpClientAssertionsTrait.php`** -> AI Confidence: **99.23%**
589. **`src/Symfony/Component/AssetMapper/AssetMapperDevServerSubscriber.php`** -> AI Confidence: **99.23%**
590. **`src/Symfony/Component/Cache/Adapter/TraceableAdapter.php`** -> AI Confidence: **99.23%**
591. **`src/Symfony/Component/Config/Definition/Builder/ArrayNodeDefinition.php`** -> AI Confidence: **99.23%**
592. **`src/Symfony/Component/Config/Exception/LoaderLoadException.php`** -> AI Confidence: **99.23%**
593. **`src/Symfony/Component/Console/Tester/ConsoleAssertionsTrait.php`** -> AI Confidence: **99.23%**
594. **`src/Symfony/Component/DependencyInjection/Loader/YamlFileLoader.php`** -> AI Confidence: **99.23%**
595. **`src/Symfony/Component/ErrorHandler/Resources/views/exception.html.php`** -> AI Confidence: **99.23%**
596. **`src/Symfony/Component/Form/ChoiceList/Factory/PropertyAccessDecorator.php`** -> AI Confidence: **99.23%**
597. **`src/Symfony/Component/Form/Extension/Csrf/EventListener/CsrfValidationListener.php`** -> AI Confidence: **99.23%**
598. **`src/Symfony/Component/Form/Flow/FormFlow.php`** -> AI Confidence: **99.23%**
599. **`src/Symfony/Component/HttpFoundation/UriSigner.php`** -> AI Confidence: **99.23%**
600. **`src/Symfony/Component/HttpKernel/EventListener/ControllerAttributesListener.php`** -> AI Confidence: **99.23%**
601. **`src/Symfony/Component/HttpKernel/Profiler/Profiler.php`** -> AI Confidence: **99.23%**
602. **`src/Symfony/Component/JsonStreamer/Mapping/Read/AttributePropertyMetadataLoader.php`** -> AI Confidence: **99.23%**
603. **`src/Symfony/Component/JsonStreamer/Mapping/Write/AttributePropertyMetadataLoader.php`** -> AI Confidence: **99.23%**
604. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Transport/SendgridSmtpTransport.php`** -> AI Confidence: **99.23%**
605. **`src/Symfony/Component/Mailer/EventListener/MessageListener.php`** -> AI Confidence: **99.23%**
606. **`src/Symfony/Component/Notifier/Bridge/AllMySms/AllMySmsTransport.php`** -> AI Confidence: **99.23%**
607. **`src/Symfony/Component/Notifier/Bridge/KazInfoTeh/KazInfoTehTransport.php`** -> AI Confidence: **99.23%**
608. **`src/Symfony/Component/Notifier/Bridge/Mobyt/MobytTransport.php`** -> AI Confidence: **99.23%**
609. **`src/Symfony/Component/Notifier/Bridge/RocketChat/RocketChatTransport.php`** -> AI Confidence: **99.23%**
610. **`src/Symfony/Component/Notifier/Bridge/Sweego/SweegoTransport.php`** -> AI Confidence: **99.23%**
611. **`src/Symfony/Component/Security/Core/Authorization/Voter/ExpressionVoter.php`** -> AI Confidence: **99.23%**
612. **`src/Symfony/Component/Security/Http/Authentication/DefaultAuthenticationSuccessHandler.php`** -> AI Confidence: **99.23%**
613. **`src/Symfony/Component/Semaphore/Store/StoreFactory.php`** -> AI Confidence: **99.23%**
614. **`src/Symfony/Component/Translation/Bridge/Loco/LocoProvider.php`** -> AI Confidence: **99.23%**
615. **`src/Symfony/Component/Validator/Constraints/ExpressionSyntaxValidator.php`** -> AI Confidence: **99.23%**
616. **`src/Symfony/Component/VarExporter/ProxyHelper.php`** -> AI Confidence: **99.23%**
617. **`src/Symfony/Component/Cache/LockRegistry.php`** -> AI Confidence: **99.2%**
618. **`src/Symfony/Component/DomCrawler/Tests/UriResolverTest.php`** -> AI Confidence: **99.2%**
619. **`src/Symfony/Component/ErrorHandler/Resources/views/traces.html.php`** -> AI Confidence: **99.2%**
620. **`src/Symfony/Component/Validator/Constraints/Length.php`** -> AI Confidence: **99.2%**
621. **`src/Symfony/Bridge/Doctrine/Form/Type/DoctrineType.php`** -> AI Confidence: **99.18%**
622. **`src/Symfony/Bridge/Doctrine/Form/Type/EntityType.php`** -> AI Confidence: **99.18%**
623. **`src/Symfony/Bridge/Doctrine/Security/RememberMe/DoctrineTokenProvider.php`** -> AI Confidence: **99.18%**
624. **`src/Symfony/Bridge/Doctrine/Tests/Form/Type/EntityTypePerformanceTest.php`** -> AI Confidence: **99.18%**
625. **`src/Symfony/Bridge/Monolog/Processor/ConsoleCommandProcessor.php`** -> AI Confidence: **99.18%**
626. **`src/Symfony/Bridge/Monolog/Processor/RouteProcessor.php`** -> AI Confidence: **99.18%**
627. **`src/Symfony/Bridge/Monolog/Tests/Handler/ServerLogHandlerTest.php`** -> AI Confidence: **99.18%**
628. **`src/Symfony/Bridge/PhpUnit/SymfonyExtension.php`** -> AI Confidence: **99.18%**
629. **`src/Symfony/Bridge/PhpUnit/Tests/Fixtures/symfonyextension/tests/bootstrap.php`** -> AI Confidence: **99.18%**
630. **`src/Symfony/Bridge/Twig/Tests/Command/DebugCommandTest.php`** -> AI Confidence: **99.18%**
631. **`src/Symfony/Bridge/Twig/Tests/Command/LintCommandTest.php`** -> AI Confidence: **99.18%**
632. **`src/Symfony/Bridge/Twig/Translation/TwigExtractor.php`** -> AI Confidence: **99.18%**
633. **`src/Symfony/Bundle/DebugBundle/DependencyInjection/DebugExtension.php`** -> AI Confidence: **99.18%**
634. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolDeleteCommand.php`** -> AI Confidence: **99.18%**
635. **`src/Symfony/Bundle/FrameworkBundle/Test/TestContainer.php`** -> AI Confidence: **99.18%**
636. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php`** -> AI Confidence: **99.18%**
637. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/CachePoolClearCommandTest.php`** -> AI Confidence: **99.18%**
638. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ConfigDebugCommandTest.php`** -> AI Confidence: **99.18%**
639. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/ConfigDumpReferenceCommandTest.php`** -> AI Confidence: **99.18%**
640. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/AddSecurityVotersPass.php`** -> AI Confidence: **99.18%**
641. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/RegisterCsrfFeaturesPass.php`** -> AI Confidence: **99.18%**
642. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/SortFirewallListenersPass.php`** -> AI Confidence: **99.18%**
643. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/AccessToken/OidcTokenHandlerFactory.php`** -> AI Confidence: **99.18%**
644. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/Factory/LoginLinkFactory.php`** -> AI Confidence: **99.18%**
645. **`src/Symfony/Bundle/SecurityBundle/EventListener/FirewallListener.php`** -> AI Confidence: **99.18%**
646. **`src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/CompleteConfigurationTestCase.php`** -> AI Confidence: **99.18%**
647. **`src/Symfony/Bundle/SecurityBundle/Tests/Functional/Bundle/CsrfFormLoginBundle/Form/UserLoginType.php`** -> AI Confidence: **99.18%**
648. **`src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/TwigExtensionTest.php`** -> AI Confidence: **99.18%**
649. **`src/Symfony/Bundle/WebProfilerBundle/DependencyInjection/WebProfilerExtension.php`** -> AI Confidence: **99.18%**
650. **`src/Symfony/Bundle/WebProfilerBundle/Tests/DependencyInjection/WebProfilerExtensionTest.php`** -> AI Confidence: **99.18%**
651. **`src/Symfony/Bundle/WebProfilerBundle/Twig/WebProfilerExtension.php`** -> AI Confidence: **99.18%**
652. **`src/Symfony/Component/AssetMapper/Command/AssetMapperCompileCommand.php`** -> AI Confidence: **99.18%**
653. **`src/Symfony/Component/AssetMapper/Command/ImportMapInstallCommand.php`** -> AI Confidence: **99.18%**
654. **`src/Symfony/Component/BrowserKit/Tests/TestHttpClient.php`** -> AI Confidence: **99.18%**
655. **`src/Symfony/Component/Cache/Tests/Adapter/AdapterTestCase.php`** -> AI Confidence: **99.18%**
656. **`src/Symfony/Component/Cache/Tests/Adapter/PdoAdapterTest.php`** -> AI Confidence: **99.18%**
657. **`src/Symfony/Component/Cache/Tests/Adapter/RedisAdapterTest.php`** -> AI Confidence: **99.18%**
658. **`src/Symfony/Component/Cache/Tests/Adapter/RelayAdapterTest.php`** -> AI Confidence: **99.18%**
659. **`src/Symfony/Component/Cache/Tests/Adapter/RelayClusterAdapterTest.php`** -> AI Confidence: **99.18%**
660. **`src/Symfony/Component/Cache/Tests/Marshaller/DefaultMarshallerTest.php`** -> AI Confidence: **99.18%**
661. **`src/Symfony/Component/Config/Definition/Builder/NodeDefinition.php`** -> AI Confidence: **99.18%**
662. **`src/Symfony/Component/Config/Tests/Definition/ScalarNodeTest.php`** -> AI Confidence: **99.18%**
663. **`src/Symfony/Component/Console/Command/TraceableCommand.php`** -> AI Confidence: **99.18%**
664. **`src/Symfony/Component/Console/DataCollector/CommandDataCollector.php`** -> AI Confidence: **99.18%**
665. **`src/Symfony/Component/Console/DependencyInjection/ConsoleArgumentValueResolverPass.php`** -> AI Confidence: **99.18%**
666. **`src/Symfony/Component/Console/Messenger/RunCommandMessageHandler.php`** -> AI Confidence: **99.18%**
667. **`src/Symfony/Component/Console/Tests/ApplicationTest.php`** -> AI Confidence: **99.18%**
668. **`src/Symfony/Component/Console/Tests/Command/HelpCommandTest.php`** -> AI Confidence: **99.18%**
669. **`src/Symfony/Component/Console/Tests/Input/ArrayInputTest.php`** -> AI Confidence: **99.18%**
670. **`src/Symfony/Component/Console/Tests/Input/InputArgumentTest.php`** -> AI Confidence: **99.18%**
671. **`src/Symfony/Component/Console/Tests/Input/InputOptionTest.php`** -> AI Confidence: **99.18%**
672. **`src/Symfony/Component/Console/Tests/Input/InputTest.php`** -> AI Confidence: **99.18%**
673. **`src/Symfony/Component/CssSelector/Parser/Handler/StringHandler.php`** -> AI Confidence: **99.18%**
674. **`src/Symfony/Component/DependencyInjection/Extension/Extension.php`** -> AI Confidence: **99.18%**
675. **`src/Symfony/Component/DependencyInjection/Kernel/AbstractBundle.php`** -> AI Confidence: **99.18%**
676. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/ServicesConfigurator.php`** -> AI Confidence: **99.18%**
677. **`src/Symfony/Component/DependencyInjection/Tests/ContainerTest.php`** -> AI Confidence: **99.18%**
678. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/custom_container_class_constructor_without_arguments.php`** -> AI Confidence: **99.18%**
679. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/custom_container_class_with_optional_constructor_arguments.php`** -> AI Confidence: **99.18%**
680. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services12.php`** -> AI Confidence: **99.18%**
681. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services8.php`** -> AI Confidence: **99.18%**
682. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_almost_circular_private.php`** -> AI Confidence: **99.18%**
683. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_array_params.php`** -> AI Confidence: **99.18%**
684. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_deprecated_parameters.php`** -> AI Confidence: **99.18%**
685. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_env_in_id.php`** -> AI Confidence: **99.18%**
686. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_uninitialized_ref.php`** -> AI Confidence: **99.18%**
687. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_unsupported_characters.php`** -> AI Confidence: **99.18%**
688. **`src/Symfony/Component/DomCrawler/Tests/CrawlerTest.php`** -> AI Confidence: **99.18%**
689. **`src/Symfony/Component/Emoji/Tests/EmojiTransliteratorTest.php`** -> AI Confidence: **99.18%**
690. **`src/Symfony/Component/ExpressionLanguage/Tests/ExpressionLanguageTest.php`** -> AI Confidence: **99.18%**
691. **`src/Symfony/Component/Filesystem/Tests/FilesystemTest.php`** -> AI Confidence: **99.18%**
692. **`src/Symfony/Component/Finder/Tests/FinderTest.php`** -> AI Confidence: **99.18%**
693. **`src/Symfony/Component/Form/Extension/Core/Type/ChoiceType.php`** -> AI Confidence: **99.18%**
694. **`src/Symfony/Component/Form/Extension/Core/Type/LanguageType.php`** -> AI Confidence: **99.18%**
695. **`src/Symfony/Component/Form/Extension/Core/Type/NumberType.php`** -> AI Confidence: **99.18%**
696. **`src/Symfony/Component/Form/Extension/HtmlSanitizer/Type/TextTypeHtmlSanitizerExtension.php`** -> AI Confidence: **99.18%**
697. **`src/Symfony/Component/Form/Extension/Validator/Type/FormTypeValidatorExtension.php`** -> AI Confidence: **99.18%**
698. **`src/Symfony/Component/Form/Extension/Validator/ValidatorExtension.php`** -> AI Confidence: **99.18%**
699. **`src/Symfony/Component/Form/Extension/Validator/ValidatorTypeGuesser.php`** -> AI Confidence: **99.18%**
700. **`src/Symfony/Component/Form/Flow/FormFlowBuilder.php`** -> AI Confidence: **99.18%**
701. **`src/Symfony/Component/Form/Flow/Type/FormFlowType.php`** -> AI Confidence: **99.18%**
702. **`src/Symfony/Component/Form/FormConfigBuilder.php`** -> AI Confidence: **99.18%**
703. **`src/Symfony/Component/Form/Tests/CompoundFormPerformanceTest.php`** -> AI Confidence: **99.18%**
704. **`src/Symfony/Component/Form/Tests/Extension/Core/Type/TimezoneTypeTest.php`** -> AI Confidence: **99.18%**
705. **`src/Symfony/Component/HttpClient/Tests/AsyncDecoratorTraitTest.php`** -> AI Confidence: **99.18%**
706. **`src/Symfony/Component/HttpClient/Tests/Response/MockResponseTest.php`** -> AI Confidence: **99.18%**
707. **`src/Symfony/Component/HttpFoundation/Session/Session.php`** -> AI Confidence: **99.18%**
708. **`src/Symfony/Component/HttpFoundation/Tests/Session/Storage/Handler/MemcachedSessionHandlerTest.php`** -> AI Confidence: **99.18%**
709. **`src/Symfony/Component/HttpKernel/EventListener/IsSignatureValidAttributeListener.php`** -> AI Confidence: **99.18%**
710. **`src/Symfony/Component/HttpKernel/EventListener/SerializeControllerResultAttributeListener.php`** -> AI Confidence: **99.18%**
711. **`src/Symfony/Component/HttpKernel/HttpCache/Ssi.php`** -> AI Confidence: **99.18%**
712. **`src/Symfony/Component/HttpKernel/HttpClientKernel.php`** -> AI Confidence: **99.18%**
713. **`src/Symfony/Component/HttpKernel/Tests/Controller/ControllerResolverTest.php`** -> AI Confidence: **99.18%**
714. **`src/Symfony/Component/HttpKernel/Tests/EventListener/DebugHandlersListenerTest.php`** -> AI Confidence: **99.18%**
715. **`src/Symfony/Component/HttpKernel/Tests/EventListener/DisallowRobotsIndexingListenerTest.php`** -> AI Confidence: **99.18%**
716. **`src/Symfony/Component/HttpKernel/Tests/Fragment/HIncludeFragmentRendererTest.php`** -> AI Confidence: **99.18%**
717. **`src/Symfony/Component/HttpKernel/Tests/Fragment/InlineFragmentRendererTest.php`** -> AI Confidence: **99.18%**
718. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/HttpCacheTest.php`** -> AI Confidence: **99.18%**
719. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/TestHttpKernel.php`** -> AI Confidence: **99.18%**
720. **`src/Symfony/Component/JsonPath/Tests/JsonCrawlerTest.php`** -> AI Confidence: **99.18%**
721. **`src/Symfony/Component/JsonStreamer/Mapping/GenericTypePropertyMetadataLoader.php`** -> AI Confidence: **99.18%**
722. **`src/Symfony/Component/Ldap/Tests/Adapter/ExtLdap/AdapterTest.php`** -> AI Confidence: **99.18%**
723. **`src/Symfony/Component/Lock/Store/MongoDbStore.php`** -> AI Confidence: **99.18%**
724. **`src/Symfony/Component/Lock/Tests/Store/AbstractRedisStoreTestCase.php`** -> AI Confidence: **99.18%**
725. **`src/Symfony/Component/Lock/Tests/Store/FlockStoreTest.php`** -> AI Confidence: **99.18%**
726. **`src/Symfony/Component/Lock/Tests/Store/PostgreSqlStoreTest.php`** -> AI Confidence: **99.18%**
727. **`src/Symfony/Component/Lock/Tests/Store/StoreFactoryTest.php`** -> AI Confidence: **99.18%**
728. **`src/Symfony/Component/Mailer/Bridge/Brevo/Webhook/BrevoRequestParser.php`** -> AI Confidence: **99.18%**
729. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Webhook/MailgunRequestParser.php`** -> AI Confidence: **99.18%**
730. **`src/Symfony/Component/Mailer/Bridge/Mailomat/Webhook/MailomatRequestParser.php`** -> AI Confidence: **99.18%**
731. **`src/Symfony/Component/Mailer/Bridge/Postmark/Webhook/PostmarkRequestParser.php`** -> AI Confidence: **99.18%**
732. **`src/Symfony/Component/Mailer/Bridge/Sweego/Tests/Transport/SweegoTransportFactoryTest.php`** -> AI Confidence: **99.18%**
733. **`src/Symfony/Component/Mailer/Tests/Transport/NativeTransportFactoryTest.php`** -> AI Confidence: **99.18%**
734. **`src/Symfony/Component/Mailer/Tests/Transport/Smtp/EsmtpTransportTest.php`** -> AI Confidence: **99.18%**
735. **`src/Symfony/Component/Messenger/Bridge/AmazonSqs/Transport/AmazonSqsTransport.php`** -> AI Confidence: **99.18%**
736. **`src/Symfony/Component/Messenger/Bridge/Amqp/Tests/Transport/AmqpTransportTest.php`** -> AI Confidence: **99.18%**
737. **`src/Symfony/Component/Messenger/Bridge/Amqp/Tests/Transport/ConnectionTest.php`** -> AI Confidence: **99.18%**
738. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Tests/Transport/DoctrinePostgreSqlFilterIntegrationTest.php`** -> AI Confidence: **99.18%**
739. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Tests/Transport/DoctrineTransportFactoryTest.php`** -> AI Confidence: **99.18%**
740. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineSender.php`** -> AI Confidence: **99.18%**
741. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineTransportFactory.php`** -> AI Confidence: **99.18%**
742. **`src/Symfony/Component/Messenger/Bridge/Redis/Tests/Transport/ConnectionTest.php`** -> AI Confidence: **99.18%**
743. **`src/Symfony/Component/Messenger/Bridge/Redis/Tests/Transport/RedisTransportFactoryTest.php`** -> AI Confidence: **99.18%**
744. **`src/Symfony/Component/Messenger/EventListener/SendFailedMessageToFailureTransportListener.php`** -> AI Confidence: **99.18%**
745. **`src/Symfony/Component/Notifier/Bridge/Bluesky/BlueskyTransportFactory.php`** -> AI Confidence: **99.18%**
746. **`src/Symfony/Component/Notifier/Bridge/Chatwork/Tests/ChatworkTransportFactoryTest.php`** -> AI Confidence: **99.18%**
747. **`src/Symfony/Component/Notifier/Bridge/FakeChat/FakeChatLoggerTransport.php`** -> AI Confidence: **99.18%**
748. **`src/Symfony/Component/Notifier/Bridge/FakeSms/FakeSmsEmailTransport.php`** -> AI Confidence: **99.18%**
749. **`src/Symfony/Component/Notifier/Bridge/GoIp/Tests/GoIpTransportFactoryTest.php`** -> AI Confidence: **99.18%**
750. **`src/Symfony/Component/Notifier/Bridge/KazInfoTeh/Tests/KazInfoTehTransportTest.php`** -> AI Confidence: **99.18%**
751. **`src/Symfony/Component/Notifier/Bridge/LineBot/Tests/LineBotTransportFactoryTest.php`** -> AI Confidence: **99.18%**
752. **`src/Symfony/Component/Notifier/Bridge/LineNotify/LineNotifyTransport.php`** -> AI Confidence: **99.18%**
753. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureTransportFactory.php`** -> AI Confidence: **99.18%**
754. **`src/Symfony/Component/Notifier/Bridge/MicrosoftTeams/MicrosoftTeamsOptions.php`** -> AI Confidence: **99.18%**
755. **`src/Symfony/Component/Notifier/Bridge/Octopush/OctopushTransport.php`** -> AI Confidence: **99.18%**
756. **`src/Symfony/Component/Notifier/Bridge/Sinch/SinchTransport.php`** -> AI Confidence: **99.18%**
757. **`src/Symfony/Component/Notifier/Bridge/Smsbox/SmsboxOptions.php`** -> AI Confidence: **99.18%**
758. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Webhook/SmsboxRequestParser.php`** -> AI Confidence: **99.18%**
759. **`src/Symfony/Component/Notifier/Bridge/Sweego/Webhook/SweegoRequestParser.php`** -> AI Confidence: **99.18%**
760. **`src/Symfony/Component/Notifier/Transport.php`** -> AI Confidence: **99.18%**
761. **`src/Symfony/Component/PasswordHasher/Tests/Command/UserPasswordHashCommandTest.php`** -> AI Confidence: **99.18%**
762. **`src/Symfony/Component/PropertyInfo/Tests/Fixtures/DummyExtractor.php`** -> AI Confidence: **99.18%**
763. **`src/Symfony/Component/Routing/Tests/RouteTest.php`** -> AI Confidence: **99.18%**
764. **`src/Symfony/Component/Scheduler/EventListener/DispatchSchedulerEventListener.php`** -> AI Confidence: **99.18%**
765. **`src/Symfony/Component/Scheduler/Tests/EventListener/DispatchSchedulerEventListenerTest.php`** -> AI Confidence: **99.18%**
766. **`src/Symfony/Component/Security/Core/Tests/Authorization/Voter/VoterTest.php`** -> AI Confidence: **99.18%**
767. **`src/Symfony/Component/Security/Http/Authenticator/LoginLinkAuthenticator.php`** -> AI Confidence: **99.18%**
768. **`src/Symfony/Component/Security/Http/Controller/SecurityTokenValueResolver.php`** -> AI Confidence: **99.18%**
769. **`src/Symfony/Component/Security/Http/EntryPoint/AuthenticationEntryPointInterface.php`** -> AI Confidence: **99.18%**
770. **`src/Symfony/Component/Security/Http/Event/LoginFailureEvent.php`** -> AI Confidence: **99.18%**
771. **`src/Symfony/Component/Security/Http/EventListener/RememberMeListener.php`** -> AI Confidence: **99.18%**
772. **`src/Symfony/Component/Security/Http/Firewall/LogoutListener.php`** -> AI Confidence: **99.18%**
773. **`src/Symfony/Component/Security/Http/Tests/LoginLink/LoginLinkHandlerTest.php`** -> AI Confidence: **99.18%**
774. **`src/Symfony/Component/Semaphore/Tests/Store/StoreFactoryTest.php`** -> AI Confidence: **99.18%**
775. **`src/Symfony/Component/Serializer/Command/DebugCommand.php`** -> AI Confidence: **99.18%**
776. **`src/Symfony/Component/Serializer/Context/Normalizer/UnwrappingDenormalizerContextBuilder.php`** -> AI Confidence: **99.18%**
777. **`src/Symfony/Component/Translation/Bridge/Loco/LocoProviderFactory.php`** -> AI Confidence: **99.18%**
778. **`src/Symfony/Component/Translation/Bridge/Loco/Tests/LocoProviderFactoryTest.php`** -> AI Confidence: **99.18%**
779. **`src/Symfony/Component/Translation/Tests/Command/XliffLintCommandTest.php`** -> AI Confidence: **99.18%**
780. **`src/Symfony/Component/TypeInfo/TypeResolver/TypeResolver.php`** -> AI Confidence: **99.18%**
781. **`src/Symfony/Component/Uid/Command/GenerateUlidCommand.php`** -> AI Confidence: **99.18%**
782. **`src/Symfony/Component/Uid/Command/InspectUuidCommand.php`** -> AI Confidence: **99.18%**
783. **`src/Symfony/Component/Validator/Context/ExecutionContext.php`** -> AI Confidence: **99.18%**
784. **`src/Symfony/Component/Validator/Test/CompoundConstraintTestCase.php`** -> AI Confidence: **99.18%**
785. **`src/Symfony/Component/Validator/Test/ConstraintValidatorTestCase.php`** -> AI Confidence: **99.18%**
786. **`src/Symfony/Component/Validator/Tests/Constraints/UrlValidatorTest.php`** -> AI Confidence: **99.18%**
787. **`src/Symfony/Component/Validator/Tests/Constraints/XmlValidatorTest.php`** -> AI Confidence: **99.18%**
788. **`src/Symfony/Component/Validator/ValidatorBuilder.php`** -> AI Confidence: **99.18%**
789. **`src/Symfony/Component/VarDumper/Tests/Caster/RedisCasterTest.php`** -> AI Confidence: **99.18%**
790. **`src/Symfony/Component/VarDumper/Tests/Dumper/ServerDumperTest.php`** -> AI Confidence: **99.18%**
791. **`src/Symfony/Component/Yaml/Escaper.php`** -> AI Confidence: **99.18%**
792. **`src/Symfony/Component/Yaml/Tests/Command/LintCommandTest.php`** -> AI Confidence: **99.18%**
793. **`src/Symfony/Bundle/FrameworkBundle/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
794. **`src/Symfony/Component/Console/Command/LockableTrait.php`** -> AI Confidence: **99.17%**
795. **`src/Symfony/Component/CssSelector/Parser/Parser.php`** -> AI Confidence: **99.17%**
796. **`src/Symfony/Component/DependencyInjection/Attribute/Autoconfigure.php`** -> AI Confidence: **99.17%**
797. **`src/Symfony/Component/DependencyInjection/Kernel/KernelTrait.php`** -> AI Confidence: **99.17%**
798. **`src/Symfony/Component/Emoji/Resources/data/emoji-bs.php`** -> AI Confidence: **99.17%**
799. **`src/Symfony/Component/Emoji/Resources/data/emoji-gd.php`** -> AI Confidence: **99.17%**
800. **`src/Symfony/Component/Emoji/Resources/data/emoji-gl.php`** -> AI Confidence: **99.17%**
801. **`src/Symfony/Component/Emoji/Resources/data/emoji-nn.php`** -> AI Confidence: **99.17%**
802. **`src/Symfony/Component/Emoji/Resources/data/emoji-pt_pt.php`** -> AI Confidence: **99.17%**
803. **`src/Symfony/Component/Emoji/Resources/data/emoji-sk.php`** -> AI Confidence: **99.17%**
804. **`src/Symfony/Component/ErrorHandler/Resources/views/error.html.php`** -> AI Confidence: **99.17%**
805. **`src/Symfony/Component/ExpressionLanguage/SyntaxError.php`** -> AI Confidence: **99.17%**
806. **`src/Symfony/Component/Finder/Comparator/NumberComparator.php`** -> AI Confidence: **99.17%**
807. **`src/Symfony/Component/Finder/Gitignore.php`** -> AI Confidence: **99.17%**
808. **`src/Symfony/Component/Form/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
809. **`src/Symfony/Component/HttpClient/Caching/Freshness.php`** -> AI Confidence: **99.17%**
810. **`src/Symfony/Component/HttpFoundation/ServerBag.php`** -> AI Confidence: **99.17%**
811. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/NativeFileSessionHandler.php`** -> AI Confidence: **99.17%**
812. **`src/Symfony/Component/HttpKernel/Profiler/FileProfilerStorage.php`** -> AI Confidence: **99.17%**
813. **`src/Symfony/Component/HttpKernel/Tests/Fixtures/Suit.php`** -> AI Confidence: **99.17%**
814. **`src/Symfony/Component/JsonStreamer/Read/Splitter.php`** -> AI Confidence: **99.17%**
815. **`src/Symfony/Component/JsonStreamer/Tests/Fixtures/Model/DummyWithRepeatedOtherDummy.php`** -> AI Confidence: **99.17%**
816. **`src/Symfony/Component/Mime/CharacterStream.php`** -> AI Confidence: **99.17%**
817. **`src/Symfony/Component/Mime/Resources/bin/update_mime_types.php`** -> AI Confidence: **99.17%**
818. **`src/Symfony/Component/Notifier/Bridge/Lox24/VoiceLanguage.php`** -> AI Confidence: **99.17%**
819. **`src/Symfony/Component/Notifier/Bridge/Pushy/Enum/InterruptionLevel.php`** -> AI Confidence: **99.17%**
820. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Enum/Encoding.php`** -> AI Confidence: **99.17%**
821. **`src/Symfony/Component/Notifier/Bridge/Smsbox/Enum/Strategy.php`** -> AI Confidence: **99.17%**
822. **`src/Symfony/Component/Routing/Matcher/Dumper/StaticPrefixCollection.php`** -> AI Confidence: **99.17%**
823. **`src/Symfony/Component/Routing/Requirement/Requirement.php`** -> AI Confidence: **99.17%**
824. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestIntBackedEnum.php`** -> AI Confidence: **99.17%**
825. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestStringBackedEnum.php`** -> AI Confidence: **99.17%**
826. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestStringBackedEnum2.php`** -> AI Confidence: **99.17%**
827. **`src/Symfony/Component/Routing/Tests/Fixtures/Enum/TestUnitEnum.php`** -> AI Confidence: **99.17%**
828. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher5.php`** -> AI Confidence: **99.17%**
829. **`src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher9.php`** -> AI Confidence: **99.17%**
830. **`src/Symfony/Component/Security/Core/Dumper/MermaidDirection.php`** -> AI Confidence: **99.17%**
831. **`src/Symfony/Component/Translation/Loader/PoFileLoader.php`** -> AI Confidence: **99.17%**
832. **`src/Symfony/Component/Uid/UuidV7.php`** -> AI Confidence: **99.17%**
833. **`src/Symfony/Component/Validator/Constraints/Count.php`** -> AI Confidence: **99.17%**
834. **`src/Symfony/Component/Validator/Constraints/File.php`** -> AI Confidence: **99.17%**
835. **`src/Symfony/Component/Validator/Constraints/Isbn.php`** -> AI Confidence: **99.17%**
836. **`src/Symfony/Component/VarDumper/Caster/Caster.php`** -> AI Confidence: **99.17%**
837. **`src/Symfony/Component/VarDumper/Caster/CutStub.php`** -> AI Confidence: **99.17%**
838. **`src/Symfony/Component/VarDumper/Tests/Fixtures/BackedEnumFixture.php`** -> AI Confidence: **99.17%**
839. **`src/Symfony/Component/VarDumper/Tests/Fixtures/UnitEnumFixture.php`** -> AI Confidence: **99.17%**
840. **`src/Symfony/Component/WebLink/HttpHeaderParser.php`** -> AI Confidence: **99.17%**
841. **`src/Symfony/Component/Yaml/Dumper.php`** -> AI Confidence: **99.17%**
842. **`src/Symfony/Component/Yaml/Parser.php`** -> AI Confidence: **99.17%**
843. **`src/Symfony/Component/Intl/Tests/Data/Bundle/Reader/Fixtures/build.sh`** -> AI Confidence: **99.17%**
844. **`src/Symfony/Bridge/Doctrine/Form/DoctrineOrmTypeGuesser.php`** -> AI Confidence: **99.16%**
845. **`src/Symfony/Bridge/Doctrine/SchemaListener/AbstractSchemaListener.php`** -> AI Confidence: **99.16%**
846. **`src/Symfony/Bridge/Doctrine/Security/User/EntityUserProvider.php`** -> AI Confidence: **99.16%**
847. **`src/Symfony/Bridge/Doctrine/Tests/DataCollector/DoctrineDataCollectorTest.php`** -> AI Confidence: **99.16%**
848. **`src/Symfony/Bridge/Monolog/Command/ServerLogCommand.php`** -> AI Confidence: **99.16%**
849. **`src/Symfony/Bridge/Monolog/Handler/ConsoleHandler.php`** -> AI Confidence: **99.16%**
850. **`src/Symfony/Bridge/Monolog/Handler/ElasticsearchLogstashHandler.php`** -> AI Confidence: **99.16%**
851. **`src/Symfony/Bridge/Twig/Extension/FormExtension.php`** -> AI Confidence: **99.16%**
852. **`src/Symfony/Bridge/Twig/Extension/SecurityExtension.php`** -> AI Confidence: **99.16%**
853. **`src/Symfony/Bridge/Twig/Extension/TranslationExtension.php`** -> AI Confidence: **99.16%**
854. **`src/Symfony/Bridge/Twig/NodeVisitor/TranslationDefaultDomainNodeVisitor.php`** -> AI Confidence: **99.16%**
855. **`src/Symfony/Bridge/Twig/Tests/Extension/AbstractDivLayoutTestCase.php`** -> AI Confidence: **99.16%**
856. **`src/Symfony/Bundle/FrameworkBundle/CacheWarmer/ValidatorCacheWarmer.php`** -> AI Confidence: **99.16%**
857. **`src/Symfony/Bundle/FrameworkBundle/Command/CachePoolInvalidateTagsCommand.php`** -> AI Confidence: **99.16%**
858. **`src/Symfony/Bundle/FrameworkBundle/Command/ConfigDebugCommand.php`** -> AI Confidence: **99.16%**
859. **`src/Symfony/Bundle/FrameworkBundle/Command/ContainerLintCommand.php`** -> AI Confidence: **99.16%**
860. **`src/Symfony/Bundle/FrameworkBundle/Command/EventDispatcherDebugCommand.php`** -> AI Confidence: **99.16%**
861. **`src/Symfony/Bundle/FrameworkBundle/Command/RouterDebugCommand.php`** -> AI Confidence: **99.16%**
862. **`src/Symfony/Bundle/FrameworkBundle/Command/RouterMatchCommand.php`** -> AI Confidence: **99.16%**
863. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsRemoveCommand.php`** -> AI Confidence: **99.16%**
864. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsRevealCommand.php`** -> AI Confidence: **99.16%**
865. **`src/Symfony/Bundle/FrameworkBundle/Controller/AbstractController.php`** -> AI Confidence: **99.16%**
866. **`src/Symfony/Bundle/FrameworkBundle/Controller/ControllerHelper.php`** -> AI Confidence: **99.16%**
867. **`src/Symfony/Bundle/FrameworkBundle/KernelBrowser.php`** -> AI Confidence: **99.16%**
868. **`src/Symfony/Bundle/FrameworkBundle/Routing/Router.php`** -> AI Confidence: **99.16%**
869. **`src/Symfony/Bundle/FrameworkBundle/Test/KernelTestCase.php`** -> AI Confidence: **99.16%**
870. **`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/ConfigurationTest.php`** -> AI Confidence: **99.16%**
871. **`src/Symfony/Bundle/SecurityBundle/Command/DebugFirewallCommand.php`** -> AI Confidence: **99.16%**
872. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Compiler/RegisterGlobalSecurityEventListenersPass.php`** -> AI Confidence: **99.16%**
873. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/MainConfiguration.php`** -> AI Confidence: **99.16%**
874. **`src/Symfony/Bundle/SecurityBundle/DependencyInjection/Security/Factory/RememberMeFactory.php`** -> AI Confidence: **99.16%**
875. **`src/Symfony/Bundle/SecurityBundle/Security.php`** -> AI Confidence: **99.16%**
876. **`src/Symfony/Bundle/SecurityBundle/Security/LazyFirewallContext.php`** -> AI Confidence: **99.16%**
877. **`src/Symfony/Bundle/WebProfilerBundle/Controller/RouterController.php`** -> AI Confidence: **99.16%**
878. **`src/Symfony/Component/AssetMapper/Command/ImportMapOutdatedCommand.php`** -> AI Confidence: **99.16%**
879. **`src/Symfony/Component/AssetMapper/Command/ImportMapRequireCommand.php`** -> AI Confidence: **99.16%**
880. **`src/Symfony/Component/Cache/Adapter/ArrayAdapter.php`** -> AI Confidence: **99.16%**
881. **`src/Symfony/Component/Cache/Adapter/ProxyAdapter.php`** -> AI Confidence: **99.16%**
882. **`src/Symfony/Component/Cache/Tests/Adapter/MemcachedAdapterTest.php`** -> AI Confidence: **99.16%**
883. **`src/Symfony/Component/Cache/Tests/Traits/RedisTraitTest.php`** -> AI Confidence: **99.16%**
884. **`src/Symfony/Component/Config/Definition/Loader/DefinitionFileLoader.php`** -> AI Confidence: **99.16%**
885. **`src/Symfony/Component/Console/Tests/Fixtures/InvokableWithInteractiveAttributesTestCommand.php`** -> AI Confidence: **99.16%**
886. **`src/Symfony/Component/DependencyInjection/Compiler/PriorityTaggedServiceTrait.php`** -> AI Confidence: **99.16%**
887. **`src/Symfony/Component/DependencyInjection/Loader/Configurator/ContainerConfigurator.php`** -> AI Confidence: **99.16%**
888. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services19.php`** -> AI Confidence: **99.16%**
889. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services26.php`** -> AI Confidence: **99.16%**
890. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_rot13_env.php`** -> AI Confidence: **99.16%**
891. **`src/Symfony/Component/DomCrawler/Tests/FormTest.php`** -> AI Confidence: **99.16%**
892. **`src/Symfony/Component/ErrorHandler/Command/ErrorDumpCommand.php`** -> AI Confidence: **99.16%**
893. **`src/Symfony/Component/ErrorHandler/Tests/ErrorHandlerTest.php`** -> AI Confidence: **99.16%**
894. **`src/Symfony/Component/Finder/Finder.php`** -> AI Confidence: **99.16%**
895. **`src/Symfony/Component/Form/Console/Descriptor/Descriptor.php`** -> AI Confidence: **99.16%**
896. **`src/Symfony/Component/Form/Extension/Core/DataAccessor/PropertyPathAccessor.php`** -> AI Confidence: **99.16%**
897. **`src/Symfony/Component/Form/Extension/Core/Type/CollectionType.php`** -> AI Confidence: **99.16%**
898. **`src/Symfony/Component/Form/Extension/Core/Type/CurrencyType.php`** -> AI Confidence: **99.16%**
899. **`src/Symfony/Component/Form/Extension/Core/Type/FormType.php`** -> AI Confidence: **99.16%**
900. **`src/Symfony/Component/Form/Extension/Core/Type/TimezoneType.php`** -> AI Confidence: **99.16%**
901. **`src/Symfony/Component/Form/Extension/Core/Type/WeekType.php`** -> AI Confidence: **99.16%**
902. **`src/Symfony/Component/Form/Extension/DataCollector/FormDataCollector.php`** -> AI Confidence: **99.16%**
903. **`src/Symfony/Component/Form/Form.php`** -> AI Confidence: **99.16%**
904. **`src/Symfony/Component/HtmlSanitizer/Reference/W3CReference.php`** -> AI Confidence: **99.16%**
905. **`src/Symfony/Component/HttpClient/HttplugClient.php`** -> AI Confidence: **99.16%**
906. **`src/Symfony/Component/HttpClient/Internal/AmpListener.php`** -> AI Confidence: **99.16%**
907. **`src/Symfony/Component/HttpClient/Psr18Client.php`** -> AI Confidence: **99.16%**
908. **`src/Symfony/Component/HttpClient/Tests/HttpClientTestCase.php`** -> AI Confidence: **99.16%**
909. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/VariadicValueResolver.php`** -> AI Confidence: **99.16%**
910. **`src/Symfony/Component/HttpKernel/DataCollector/RequestDataCollector.php`** -> AI Confidence: **99.16%**
911. **`src/Symfony/Component/HttpKernel/DependencyInjection/ControllerArgumentValueResolverPass.php`** -> AI Confidence: **99.16%**
912. **`src/Symfony/Component/HttpKernel/HttpCache/Esi.php`** -> AI Confidence: **99.16%**
913. **`src/Symfony/Component/HttpKernel/HttpCache/HttpCache.php`** -> AI Confidence: **99.16%**
914. **`src/Symfony/Component/HttpKernel/HttpKernelBrowser.php`** -> AI Confidence: **99.16%**
915. **`src/Symfony/Component/Intl/Tests/CountriesWithUserAssignedTest.php`** -> AI Confidence: **99.16%**
916. **`src/Symfony/Component/JsonStreamer/Read/StreamReaderGenerator.php`** -> AI Confidence: **99.16%**
917. **`src/Symfony/Component/JsonStreamer/Write/StreamWriterGenerator.php`** -> AI Confidence: **99.16%**
918. **`src/Symfony/Component/Lock/Tests/Store/MongoDbStoreTest.php`** -> AI Confidence: **99.16%**
919. **`src/Symfony/Component/Mailer/Bridge/AhaSend/Webhook/AhaSendRequestParser.php`** -> AI Confidence: **99.16%**
920. **`src/Symfony/Component/Mailer/Bridge/Azure/Transport/AzureApiTransport.php`** -> AI Confidence: **99.16%**
921. **`src/Symfony/Component/Mailer/Bridge/Mailchimp/Transport/MandrillHttpTransport.php`** -> AI Confidence: **99.16%**
922. **`src/Symfony/Component/Mailer/Bridge/MailerSend/Webhook/MailerSendRequestParser.php`** -> AI Confidence: **99.16%**
923. **`src/Symfony/Component/Mailer/Bridge/Mailgun/Transport/MailgunHttpTransport.php`** -> AI Confidence: **99.16%**
924. **`src/Symfony/Component/Mailer/Bridge/Mailomat/Transport/MailomatApiTransport.php`** -> AI Confidence: **99.16%**
925. **`src/Symfony/Component/Mailer/Bridge/MicrosoftGraph/Transport/MicrosoftGraphApiTransport.php`** -> AI Confidence: **99.16%**
926. **`src/Symfony/Component/Mailer/Bridge/Postal/Transport/PostalApiTransport.php`** -> AI Confidence: **99.16%**
927. **`src/Symfony/Component/Mailer/Bridge/Resend/Webhook/ResendRequestParser.php`** -> AI Confidence: **99.16%**
928. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Transport/SendgridApiTransport.php`** -> AI Confidence: **99.16%**
929. **`src/Symfony/Component/Mailer/Bridge/Sendgrid/Webhook/SendgridRequestParser.php`** -> AI Confidence: **99.16%**
930. **`src/Symfony/Component/Mailer/Bridge/Sweego/Transport/SweegoApiTransport.php`** -> AI Confidence: **99.16%**
931. **`src/Symfony/Component/Mailer/Bridge/Sweego/Webhook/SweegoRequestParser.php`** -> AI Confidence: **99.16%**
932. **`src/Symfony/Component/Mailer/Transport.php`** -> AI Confidence: **99.16%**
933. **`src/Symfony/Component/Mailer/Transport/AbstractTransport.php`** -> AI Confidence: **99.16%**
934. **`src/Symfony/Component/Mailer/Transport/Smtp/SmtpTransport.php`** -> AI Confidence: **99.16%**
935. **`src/Symfony/Component/Messenger/Bridge/Beanstalkd/Transport/BeanstalkdReceiver.php`** -> AI Confidence: **99.16%**
936. **`src/Symfony/Component/Messenger/Bridge/Beanstalkd/Transport/Connection.php`** -> AI Confidence: **99.16%**
937. **`src/Symfony/Component/Messenger/Bridge/Doctrine/Transport/DoctrineReceiver.php`** -> AI Confidence: **99.16%**
938. **`src/Symfony/Component/Messenger/Bridge/Redis/Tests/Transport/RedisExtIntegrationTest.php`** -> AI Confidence: **99.16%**
939. **`src/Symfony/Component/Messenger/Command/SetupTransportsCommand.php`** -> AI Confidence: **99.16%**
940. **`src/Symfony/Component/Messenger/Command/StatsCommand.php`** -> AI Confidence: **99.16%**
941. **`src/Symfony/Component/Messenger/Transport/Serialization/Serializer.php`** -> AI Confidence: **99.16%**
942. **`src/Symfony/Component/Mime/Address.php`** -> AI Confidence: **99.16%**
943. **`src/Symfony/Component/Mime/Tests/Encoder/QpEncoderTest.php`** -> AI Confidence: **99.16%**
944. **`src/Symfony/Component/Notifier/Bridge/FreeMobile/FreeMobileTransport.php`** -> AI Confidence: **99.16%**
945. **`src/Symfony/Component/Notifier/Bridge/GoIp/GoIpTransport.php`** -> AI Confidence: **99.16%**
946. **`src/Symfony/Component/Notifier/Bridge/LinkedIn/LinkedInTransport.php`** -> AI Confidence: **99.16%**
947. **`src/Symfony/Component/Notifier/Bridge/Lox24/Lox24Transport.php`** -> AI Confidence: **99.16%**
948. **`src/Symfony/Component/Notifier/Bridge/Mastodon/MastodonTransport.php`** -> AI Confidence: **99.16%**
949. **`src/Symfony/Component/Notifier/Bridge/Matrix/MatrixTransport.php`** -> AI Confidence: **99.16%**
950. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureOptions.php`** -> AI Confidence: **99.16%**
951. **`src/Symfony/Component/Notifier/Bridge/Mercure/MercureTransport.php`** -> AI Confidence: **99.16%**
952. **`src/Symfony/Component/Notifier/Bridge/Pushy/PushyTransport.php`** -> AI Confidence: **99.16%**
953. **`src/Symfony/Component/Notifier/Bridge/SmsSluzba/SmsSluzbaTransport.php`** -> AI Confidence: **99.16%**
954. **`src/Symfony/Component/Notifier/Bridge/Smsc/SmscTransport.php`** -> AI Confidence: **99.16%**
955. **`src/Symfony/Component/Notifier/Bridge/SpotHit/SpotHitTransport.php`** -> AI Confidence: **99.16%**
956. **`src/Symfony/Component/Notifier/Bridge/Yunpian/YunpianTransport.php`** -> AI Confidence: **99.16%**
957. **`src/Symfony/Component/Notifier/Bridge/Zulip/ZulipTransport.php`** -> AI Confidence: **99.16%**
958. **`src/Symfony/Component/Notifier/Tests/Transport/DsnTest.php`** -> AI Confidence: **99.16%**
959. **`src/Symfony/Component/Notifier/Transport/AbstractTransport.php`** -> AI Confidence: **99.16%**
960. **`src/Symfony/Component/PasswordHasher/Command/UserPasswordHashCommand.php`** -> AI Confidence: **99.16%**
961. **`src/Symfony/Component/Process/Tests/ProcessTest.php`** -> AI Confidence: **99.16%**
962. **`src/Symfony/Component/Routing/Generator/UrlGenerator.php`** -> AI Confidence: **99.16%**
963. **`src/Symfony/Component/Routing/Route.php`** -> AI Confidence: **99.16%**
964. **`src/Symfony/Component/Routing/Router.php`** -> AI Confidence: **99.16%**
965. **`src/Symfony/Component/Security/Http/AccessToken/Oidc/OidcTokenHandler.php`** -> AI Confidence: **99.16%**
966. **`src/Symfony/Component/Security/Http/Authenticator/AbstractPreAuthenticatedAuthenticator.php`** -> AI Confidence: **99.16%**
967. **`src/Symfony/Component/Security/Http/Authenticator/AccessTokenAuthenticator.php`** -> AI Confidence: **99.16%**
968. **`src/Symfony/Component/Security/Http/Authenticator/FormLoginAuthenticator.php`** -> AI Confidence: **99.16%**
969. **`src/Symfony/Component/Security/Http/Authenticator/JsonLoginAuthenticator.php`** -> AI Confidence: **99.16%**
970. **`src/Symfony/Component/Security/Http/Authenticator/RememberMeAuthenticator.php`** -> AI Confidence: **99.16%**
971. **`src/Symfony/Component/Security/Http/Command/OidcTokenGenerateCommand.php`** -> AI Confidence: **99.16%**
972. **`src/Symfony/Component/Security/Http/EventListener/LoginThrottlingListener.php`** -> AI Confidence: **99.16%**
973. **`src/Symfony/Component/Security/Http/Firewall/AccessListener.php`** -> AI Confidence: **99.16%**
974. **`src/Symfony/Component/Security/Http/Firewall/SwitchUserListener.php`** -> AI Confidence: **99.16%**
975. **`src/Symfony/Component/Security/Http/LoginLink/LoginLinkHandler.php`** -> AI Confidence: **99.16%**
976. **`src/Symfony/Component/Security/Http/RememberMe/SignatureRememberMeHandler.php`** -> AI Confidence: **99.16%**
977. **`src/Symfony/Component/Serializer/Tests/Encoder/XmlEncoderTest.php`** -> AI Confidence: **99.16%**
978. **`src/Symfony/Component/Translation/Bridge/Phrase/PhraseProviderFactory.php`** -> AI Confidence: **99.16%**
979. **`src/Symfony/Component/Translation/Bridge/Phrase/Tests/PhraseProviderFactoryTest.php`** -> AI Confidence: **99.16%**
980. **`src/Symfony/Component/Translation/Command/TranslationLintCommand.php`** -> AI Confidence: **99.16%**
981. **`src/Symfony/Component/Translation/Command/TranslationPullCommand.php`** -> AI Confidence: **99.16%**
982. **`src/Symfony/Component/Translation/Command/TranslationPushCommand.php`** -> AI Confidence: **99.16%**
983. **`src/Symfony/Component/Translation/Tests/Extractor/PhpAstExtractorTest.php`** -> AI Confidence: **99.16%**
984. **`src/Symfony/Component/Translation/Tests/Provider/DsnTest.php`** -> AI Confidence: **99.16%**
985. **`src/Symfony/Component/Validator/Command/DebugCommand.php`** -> AI Confidence: **99.16%**
986. **`src/Symfony/Component/Validator/Constraints/IbanValidator.php`** -> AI Confidence: **99.16%**
987. **`src/Symfony/Component/Validator/Tests/Fixtures/ConstraintWithRequiredArgument.php`** -> AI Confidence: **99.16%**
988. **`src/Symfony/Component/Validator/Tests/Util/PropertyPathTest.php`** -> AI Confidence: **99.16%**
989. **`src/Symfony/Component/VarDumper/Resources/bin/var-dump-server`** -> AI Confidence: **99.16%**
990. **`src/Symfony/Component/VarDumper/VarDumper.php`** -> AI Confidence: **99.16%**
991. **`src/Symfony/Component/Workflow/Command/WorkflowDumpCommand.php`** -> AI Confidence: **99.16%**
992. **`src/Symfony/Bridge/Doctrine/DataCollector/DoctrineDataCollector.php`** -> AI Confidence: **99.15%**
993. **`src/Symfony/Bridge/Doctrine/Types/AbstractUidType.php`** -> AI Confidence: **99.15%**
994. **`src/Symfony/Bridge/Monolog/Processor/DebugProcessor.php`** -> AI Confidence: **99.15%**
995. **`src/Symfony/Bridge/PhpUnit/CoverageListener.php`** -> AI Confidence: **99.15%**
996. **`src/Symfony/Bridge/PhpUnit/Extension/EnableClockMockSubscriber.php`** -> AI Confidence: **99.15%**
997. **`src/Symfony/Bridge/PhpUnit/Extension/RegisterClockMockSubscriber.php`** -> AI Confidence: **99.15%**
998. **`src/Symfony/Bridge/PhpUnit/Extension/RegisterDnsMockSubscriber.php`** -> AI Confidence: **99.15%**
999. **`src/Symfony/Bridge/PsrHttpMessage/Factory/HttpFoundationFactory.php`** -> AI Confidence: **99.15%**
1000. **`src/Symfony/Bridge/Twig/AppVariable.php`** -> AI Confidence: **99.15%**
1001. **`src/Symfony/Bridge/Twig/DataCollector/TwigDataCollector.php`** -> AI Confidence: **99.15%**
1002. **`src/Symfony/Bridge/Twig/Extension/DumpExtension.php`** -> AI Confidence: **99.15%**
1003. **`src/Symfony/Bridge/Twig/Mime/BodyRenderer.php`** -> AI Confidence: **99.15%**
1004. **`src/Symfony/Bridge/Twig/Mime/NotificationEmail.php`** -> AI Confidence: **99.15%**
1005. **`src/Symfony/Bridge/Twig/Tests/Extension/HttpFoundationExtensionTest.php`** -> AI Confidence: **99.15%**
1006. **`src/Symfony/Bridge/Twig/TokenParser/TransTokenParser.php`** -> AI Confidence: **99.15%**
1007. **`src/Symfony/Bridge/Twig/UndefinedCallableHandler.php`** -> AI Confidence: **99.15%**
1008. **`src/Symfony/Bundle/FrameworkBundle/CacheWarmer/SerializerCacheWarmer.php`** -> AI Confidence: **99.15%**
1009. **`src/Symfony/Bundle/FrameworkBundle/Command/AboutCommand.php`** -> AI Confidence: **99.15%**
1010. **`src/Symfony/Bundle/FrameworkBundle/Command/CacheWarmupCommand.php`** -> AI Confidence: **99.15%**
1011. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsEncryptFromLocalCommand.php`** -> AI Confidence: **99.15%**
1012. **`src/Symfony/Bundle/FrameworkBundle/Command/SecretsGenerateKeysCommand.php`** -> AI Confidence: **99.15%**
1013. **`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/Compiler/ContainerBuilderDebugDumpPass.php`** -> AI Confidence: **99.15%**
1014. **`src/Symfony/Bundle/FrameworkBundle/EventListener/SuggestMissingPackageSubscriber.php`** -> AI Confidence: **99.15%**
1015. **`src/Symfony/Bundle/FrameworkBundle/Tests/Controller/RedirectControllerTest.php`** -> AI Confidence: **99.15%**
1016. **`src/Symfony/Bundle/FrameworkBundle/Tests/Functional/JsonStreamerTest.php`** -> AI Confidence: **99.15%**
1017. **`src/Symfony/Bundle/FrameworkBundle/Translation/Translator.php`** -> AI Confidence: **99.15%**
1018. **`src/Symfony/Component/AssetMapper/Command/VersionProblemCommandTrait.php`** -> AI Confidence: **99.15%**
1019. **`src/Symfony/Component/BrowserKit/Tests/AbstractBrowserTest.php`** -> AI Confidence: **99.15%**
1020. **`src/Symfony/Component/Cache/DependencyInjection/CacheCollectorPass.php`** -> AI Confidence: **99.15%**
1021. **`src/Symfony/Component/Cache/Tests/Adapter/RedisClusterAdapterTest.php`** -> AI Confidence: **99.15%**
1022. **`src/Symfony/Component/Config/Definition/BaseNode.php`** -> AI Confidence: **99.15%**
1023. **`src/Symfony/Component/Console/ArgumentResolver/ValueResolver/VariadicValueResolver.php`** -> AI Confidence: **99.15%**
1024. **`src/Symfony/Component/Console/Tests/Fixtures/InvokableWithInputTestCommand.php`** -> AI Confidence: **99.15%**
1025. **`src/Symfony/Component/Console/Tests/Helper/ProcessHelperTest.php`** -> AI Confidence: **99.15%**
1026. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_base64_env.php`** -> AI Confidence: **99.15%**
1027. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_csv_env.php`** -> AI Confidence: **99.15%**
1028. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_default_env.php`** -> AI Confidence: **99.15%**
1029. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_json_env.php`** -> AI Confidence: **99.15%**
1030. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_nonempty_parameters.php`** -> AI Confidence: **99.15%**
1031. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_query_string_env.php`** -> AI Confidence: **99.15%**
1032. **`src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_url_env.php`** -> AI Confidence: **99.15%**
1033. **`src/Symfony/Component/DependencyInjection/Tests/ParameterBag/ParameterBagTest.php`** -> AI Confidence: **99.15%**
1034. **`src/Symfony/Component/ErrorHandler/Exception/FlattenException.php`** -> AI Confidence: **99.15%**
1035. **`src/Symfony/Component/ErrorHandler/Tests/ErrorEnhancer/ClassNotFoundErrorEnhancerTest.php`** -> AI Confidence: **99.15%**
1036. **`src/Symfony/Component/Form/DependencyInjection/FormPass.php`** -> AI Confidence: **99.15%**
1037. **`src/Symfony/Component/Form/Extension/Core/Type/ColorType.php`** -> AI Confidence: **99.15%**
1038. **`src/Symfony/Component/Form/Extension/DependencyInjection/DependencyInjectionExtension.php`** -> AI Confidence: **99.15%**
1039. **`src/Symfony/Component/Form/Extension/PasswordHasher/EventListener/PasswordHasherListener.php`** -> AI Confidence: **99.15%**
1040. **`src/Symfony/Component/Form/FormFactory.php`** -> AI Confidence: **99.15%**
1041. **`src/Symfony/Component/Form/ResolvedFormType.php`** -> AI Confidence: **99.15%**
1042. **`src/Symfony/Component/Form/Tests/Extension/Core/Type/IntegerTypeTest.php`** -> AI Confidence: **99.15%**
1043. **`src/Symfony/Component/HttpClient/Internal/AmpBody.php`** -> AI Confidence: **99.15%**
1044. **`src/Symfony/Component/HttpClient/TraceableHttpClient.php`** -> AI Confidence: **99.15%**
1045. **`src/Symfony/Component/HttpFoundation/Session/Storage/Handler/MongoDbSessionHandler.php`** -> AI Confidence: **99.15%**
1046. **`src/Symfony/Component/HttpFoundation/Tests/UrlHelperTest.php`** -> AI Confidence: **99.15%**
1047. **`src/Symfony/Component/HttpKernel/Controller/ArgumentResolver/RequestValueResolver.php`** -> AI Confidence: **99.15%**
1048. **`src/Symfony/Component/HttpKernel/Controller/ContainerControllerResolver.php`** -> AI Confidence: **99.15%**
1049. **`src/Symfony/Component/HttpKernel/DataCollector/ConfigDataCollector.php`** -> AI Confidence: **99.15%**
1050. **`src/Symfony/Component/HttpKernel/DependencyInjection/ResettableServicePass.php`** -> AI Confidence: **99.15%**
1051. **`src/Symfony/Component/HttpKernel/EventListener/LocaleListener.php`** -> AI Confidence: **99.15%**
1052. **`src/Symfony/Component/HttpKernel/Fragment/FragmentHandler.php`** -> AI Confidence: **99.15%**
1053. **`src/Symfony/Component/HttpKernel/Fragment/InlineFragmentRenderer.php`** -> AI Confidence: **99.15%**
1054. **`src/Symfony/Component/HttpKernel/Tests/HttpCache/HttpCacheTestCase.php`** -> AI Confidence: **99.15%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `src/Symfony/Component/Mailer/Bridge/Sendgrid/Tests/Webhook/SendgridSignedRequestParserTest.php` -> **100.0%** Exposure
- `src/Symfony/Component/Mailer/Tests/EventListener/DkimSignedMessageListenerTest.php` -> **99.9795%** Exposure
- `src/Symfony/Component/Security/Core/Tests/Authentication/Token/AbstractTokenTest.php` -> **98.9215%** Exposure
- `src/Symfony/Component/Mime/Tests/Crypto/DkimSignerTest.php` -> **93.201%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `182` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `42752` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Symfony/Component/HttpClient/Internal/AmpListener.php` (PHP) -> Cumulative Risk: **762.32**
- **Archetype:** `file_cluster_13` (Distance: 12.292 IQR)
- **Magnitude:** 185.84 | **LOC:** 230 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9955%)
- **Heaviest Functions:** `requestHeaderStart` (Impact: 33.9), `requestStart` (Impact: 8.6), `connectionAcquired` (Impact: 4.5)

### 2. `src/Symfony/Component/HttpClient/Internal/AmpClientState.php` (PHP) -> Cumulative Risk: **646.04**
- **Archetype:** `file_cluster_4` (Distance: 13.136 IQR)
- **Magnitude:** 232.68 | **LOC:** 205 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (94.2254%)
- **Heaviest Functions:** `request` (Impact: 41.7), `getClient` (Impact: 36.9), `connect` (Impact: 10.3)

### 3. `src/Symfony/Component/VarDumper/Server/DumpServer.php` (PHP) -> Cumulative Risk: **643.19**
- **Archetype:** `file_cluster_4` (Distance: 12.683 IQR)
- **Magnitude:** 104.48 | **LOC:** 110 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (86.2123%)
- **Heaviest Functions:** `listen` (Impact: 27.4), `getMessages` (Impact: 11.5), `__construct` (Impact: 6.5)

### 4. `src/Symfony/Component/Messenger/Middleware/StackMiddleware.php` (PHP) -> Cumulative Risk: **642.53**
- **Archetype:** `file_cluster_4` (Distance: 12.503 IQR)
- **Magnitude:** 73.0 | **LOC:** 91 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `__construct` (Impact: 13.1), `next` (Impact: 10.9), `next` (Impact: 4.0)

### 5. `src/Symfony/Component/HttpClient/Internal/AmpBody.php` (PHP) -> Cumulative Risk: **641.73**
- **Archetype:** `file_cluster_13` (Distance: 12.542 IQR)
- **Magnitude:** 154.28 | **LOC:** 151 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (95.2704%)
- **Heaviest Functions:** `__construct` (Impact: 14.8), `read` (Impact: 12.9), `rewind` (Impact: 10.9)

### 6. `src/Symfony/Component/HttpClient/Response/AmpResponse.php` (PHP) -> Cumulative Risk: **639.7**
- **Archetype:** `file_cluster_13` (Distance: 13.721 IQR)
- **Magnitude:** 548.06 | **LOC:** 467 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (84.5759%)
- **Heaviest Functions:** `followRedirects` (Impact: 84.3), `getPushedResponse` (Impact: 77.0), `generateResponse` (Impact: 55.2)

### 7. `src/Symfony/Component/HttpFoundation/ServerEvent.php` (PHP) -> Cumulative Risk: **634.14**
- **Archetype:** `file_cluster_4` (Distance: 12.1 IQR)
- **Magnitude:** 135.94 | **LOC:** 146 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `getIterator` (Impact: 17.0), `__construct` (Impact: 13.6), `setRetry` (Impact: 4.3)

### 8. `src/Symfony/Component/CssSelector/XPath/Extension/NodeExtension.php` (PHP) -> Cumulative Risk: **633.64**
- **Archetype:** `file_cluster_8` (Distance: 11.713 IQR)
- **Magnitude:** 181.04 | **LOC:** 230 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (89.8779%)
- **Heaviest Functions:** `translateElement` (Impact: 17.4), `translateAttribute` (Impact: 11.6), `setFlag` (Impact: 9.3)

### 9. `src/Symfony/Component/HttpClient/Internal/AmpResolver.php` (PHP) -> Cumulative Risk: **624.69**
- **Archetype:** `file_cluster_4` (Distance: 13.075 IQR)
- **Magnitude:** 81.24 | **LOC:** 65 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.603%)
- **Heaviest Functions:** `resolve` (Impact: 18.8), `query` (Impact: 14.8), `__construct` (Impact: 1.9)

### 10. `src/Symfony/Component/Emoji/Resources/bin/build.php` (PHP) -> Cumulative Risk: **619.84**
- **Archetype:** `file_cluster_4` (Distance: 13.236 IQR)
- **Magnitude:** 305.58 | **LOC:** 263 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (96.6576%), Cognitive Load (87.9145%)
- **Heaviest Functions:** `buildRules` (Impact: 31.1), `saveRules` (Impact: 23.3), `getEmojisCodePoints` (Impact: 18.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Symfony/Component/VarDumper/Dumper/HtmlDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.878 IQR)
- **Top Global Matches:** file_cluster_8: 13.878, file_cluster_13: 14.053, file_cluster_0: 14.169
- **Magnitude:** 4540.68 | **LOC:** 979 | **CtrlFlow:** 64.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.9013%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 54`, `args: 17`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 260`
* *Architecture:* `io: 2`, `api: 14`, `import: 2`
* *Defense:* `safety: 25`, `doc: 8`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Symfony\Component\VarDumper\Cloner\Cursor, Symfony\Component\VarDumper\Cloner\Data
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.07 IQR)
- **Top Global Matches:** file_cluster_13: 15.07, file_cluster_8: 15.187, file_cluster_11: 15.281
- **Magnitude:** 3550.72 | **LOC:** 2439 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.7839%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dump` (Impact: 180.0)
  * `dumpValue` (Impact: 132.8)
  * `addNewInstance` (Impact: 114.4)
  * `addService` (Impact: 110.3)
  * `isTrivialInstance` (Impact: 70.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 780`, `structural_boundaries: 404`, `args: 60`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1747`
* *Architecture:* `api: 12`, `concurrency: 12`, `import: 48`
* *Defense:* `safety: 128`, `doc: 30`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` Symfony\Component\DependencyInjection\Compiler\AnalyzeServiceReferencesPass, = true, Symfony\Component\DependencyInjection\Definition, $preloadedFiles', Container$hash.legacy', Composer\Autoload\ClassLoader, Symfony\Component\DependencyInjection\Argument\ServiceLocator, $autoloadFile...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/ErrorHandler/DebugClassLoader.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.73 IQR)
- **Top Global Matches:** file_cluster_13: 14.73, file_cluster_11: 14.845, file_cluster_8: 14.871
- **Magnitude:** 3267.02 | **LOC:** 1407 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (71.4934%), Tech Debt (10.6974%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 1008.8)
    * *Intent:* /** * Autoloader checking if the class is really defined in the file found. * * The ClassLoader will...
  * `checkAnnotations` (Impact: 744.5)
  * `setReturnType` (Impact: 162.4)
  * `parsePhpDoc` (Impact: 137.5)
  * `patchMethod` (Impact: 82.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 477`, `structural_boundaries: 199`, `args: 20`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 760`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 10`, `import: 19`
* *Defense:* `safety: 92`, `doc: 30`, `test: 17`, `immutability_locks: 8`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.335
  * `Choke Point (Betweenness):` 0.000254 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Composer\InstalledVersions, Mockery\MockInterface, $parameterName, Psr\Log\LogLevel, ?string $parent): array
    
        $ownInterfaces = class_implements($class, not defining it is deprecated.', PHPUnit\Framework\MockObject\Stub, Prophecy\Prophecy\ProphecySubjectInterface...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Tests/Helper/ProgressBarTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.85 IQR)
- **Top Global Matches:** file_cluster_8: 13.85, file_cluster_13: 14.074, file_cluster_4: 14.192
- **Magnitude:** 2118.44 | **LOC:** 1396 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (87.0649%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testParallelBars` (Impact: 8.1)
  * `testOverwriteWithSectionOutputWithNewlin` (Impact: 6.5)
  * `testAnsiColorsAndEmojis` (Impact: 6.4)
  * `testOverwritWithNewlinesInMessage` (Impact: 6.2)
  * `testNonDecoratedOutput` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 196`, `args: 76`, `func_start: 72`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 1809`, `duplicate_logic: 2`, `orphaned_logic: 67`
* *Architecture:* `io: 1`, `api: 68`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 8`, `doc: 1`, `test: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` PHPUnit\Framework\Attributes\DataProvider, Symfony\Component\Console\Helper\ProgressBar, Symfony\Component\Console\Formatter\OutputFormatter, PHPUnit\Framework\Attributes\Group, Symfony\Component\Console\Output\StreamOutput, Symfony\Component\Console\Output\ConsoleSectionOutput, PHPUnit\Framework\TestCase, Symfony\Component\Console\Exception\LogicException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.226 IQR)
- **Top Global Matches:** file_cluster_13: 13.226, file_cluster_8: 13.253, file_cluster_0: 13.618
- **Magnitude:** 1751.08 | **LOC:** 3160 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 34.1%
- **Risk Profile:** Cognitive Load (61.1852%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMessengerTransports` (Impact: 19.5)
  * `assertCachePoolServiceDefinitionIsCreate` (Impact: 19.4)
  * `createContainerFromFile` (Impact: 18.4)
  * `testWorkflows` (Impact: 18.0)
  * `testTranslator` (Impact: 17.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 480`, `args: 200`, `func_start: 187`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 647`, `duplicate_logic: 2`
* *Architecture:* `api: 348`, `concurrency: 2`, `import: 109`
* *Defense:* `safety: 27`, `doc: 5`, `test: 616`, `sync_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.479
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 100):` Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\HttpKernel\Exception\NotFoundHttpException, Psr\Cache\CacheItemPoolInterface, Symfony\Component\Workflow\Metadata\InMemoryMetadataStore, Symfony\Component\Translation\TranslatableMessage, Psr\Log\LogLevel, Symfony\Component\Messenger\Middleware\DecodeFailedMessageMiddleware, Symfony\Component\Messenger\Middleware\DeduplicateMiddleware...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Yaml/Parser.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.174 IQR)
- **Top Global Matches:** file_cluster_8: 14.174, file_cluster_13: 14.33, file_cluster_7: 14.436
- **Magnitude:** 1689.42 | **LOC:** 1280 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.6231%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doParse` (Impact: 334.0)
    * *Intent:* /** * Parses a YAML string to a PHP value. * * @param string $value A YAML string * @param int-mask-...
  * `parseValue` (Impact: 103.5)
  * `getNextEmbedBlock` (Impact: 77.5)
  * `parseBlockScalar` (Impact: 67.2)
  * `lexInlineQuotedString` (Impact: 59.5)
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

### `src/Symfony/Component/Validator/Constraints/Video.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 15.993 IQR)
- **Top Global Matches:** file_cluster_13: 15.993, file_cluster_2: 16.157, file_cluster_17: 16.179
- **Magnitude:** 1686.14 | **LOC:** 253 | **CtrlFlow:** 86.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (47.0328%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 320`
* *Architecture:* `api: 48`, `import: 6`
* *Defense:* `safety: 31`, `doc: 28`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` self::CORRUPTED_VIDEO_ERROR => 'CORRUPTED_VIDEO_ERROR', self::TOO_MANY_PIXEL_ERROR => 'TOO_MANY_PIXEL_ERROR', self::TOO_WIDE_ERROR => 'TOO_WIDE_ERROR', self::TOO_NARROW_ERROR => 'TOO_NARROW_ERROR', Symfony\Component\Validator\Exception\LogicException, self::RATIO_TOO_SMALL_ERROR => 'RATIO_TOO_SMALL_ERROR', self::RATIO_TOO_BIG_ERROR => 'RATIO_TOO_BIG_ERROR', self::INVALID_MIME_TYPE_ERROR => 'INVALID_MIME_TYPE_ERROR'...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/JsonPath/JsonCrawler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.055 IQR)
- **Top Global Matches:** file_cluster_8: 14.055, file_cluster_13: 14.076, file_cluster_17: 14.241
- **Magnitude:** 1563.44 | **LOC:** 1174 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (81.7997%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `evaluateBracket` (Impact: 220.8)
  * `evaluateFunction` (Impact: 85.8)
  * `evaluateFilterExpression` (Impact: 50.4)
  * `compareEquality` (Impact: 49.1)
  * `evaluateScalar` (Impact: 45.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 216`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 653`, `dead_code: 2`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 57`, `doc: 6`, `test: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` Symfony\Component\JsonPath\Tokenizer\TokenType, Symfony\Component\JsonPath\Tokenizer\JsonPathToken, $expectedArgCount), json-streamer".', s exactly %d argument(s).', Symfony\Component\JsonPath\Tokenizer\JsonPathTokenizer, Symfony\Component\JsonPath\Exception\InvalidJsonPathException, Psr\Container\ContainerInterface...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Serializer/Tests/Normalizer/AbstractObjectNormalizerTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.87 IQR)
- **Top Global Matches:** file_cluster_13: 12.87, file_cluster_0: 13.025, file_cluster_8: 13.032
- **Magnitude:** 1527.1 | **LOC:** 2125 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (44.9061%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDenormalizeNullCoalescingValues` (Impact: 19.1)
    * *Intent:* #[SerializedPath('[data][foo]')]
  * `testDenormalizeWithNestedDiscriminatorMa` (Impact: 12.0)
  * `denormalize` (Impact: 11.7)
    * *Intent:* /** * @param DenormalizerInterface[] $normalizers */
  * `testNormalizeBasedOnAllowedAttributes` (Impact: 10.4)
  * `testDenormalizeXmlScalar` (Impact: 10.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 680`, `args: 167`, `func_start: 166`, `class_start: 46`
* *Risk/State:* `state_mutation: 625`, `dead_code: 2`, `duplicate_logic: 94`, `orphaned_logic: 64`
* *Architecture:* `api: 202`, `concurrency: 11`, `import: 54`
* *Defense:* `safety: 17`, `doc: 60`, `test: 123`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` Symfony\Component\Serializer\Normalizer\ArrayDenormalizer, Symfony\Component\Serializer\Tests\Fixtures\DummyString, Symfony\Component\Serializer\Exception\NotNormalizableValueException, Symfony\Component\Serializer\Normalizer\PropertyNormalizer, Symfony\Component\Serializer\SerializerInterface, Symfony\Component\Serializer\Normalizer\BackedEnumNormalizer, Symfony\Component\Serializer\Mapping\ClassDiscriminatorFromClassMetadata, Symfony\Component\Serializer\Tests\Fixtures\DummyWithObjectOrNull...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Console/Application.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.632 IQR)
- **Top Global Matches:** file_cluster_13: 14.632, file_cluster_11: 14.958, file_cluster_17: 14.969
- **Magnitude:** 1459.7 | **LOC:** 1422 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 14.3%
- **Risk Profile:** Cognitive Load (47.2973%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `doRunCommand` (Impact: 70.1)
  * `doRenderThrowable` (Impact: 67.6)
  * `find` (Impact: 65.8)
  * `run` (Impact: 65.1)
  * `doRun` (Impact: 51.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 258`, `args: 69`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 663`, `dead_code: 3`
* *Architecture:* `api: 61`, `import: 46`
* *Defense:* `safety: 80`, `doc: 58`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 45):` InputOption::VALUE_NONE, new InputOption('--help', Symfony\Component\Console\Formatter\OutputFormatter, 'Do not ask any interactive question'), '-h', Symfony\Component\Console\Command\CompleteCommand, 'Display this application version'), Symfony\Component\Console\Exception\NamespaceNotFoundException...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Validator/Constraints/Image.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_2` (Drift: 15.588 IQR)
- **Top Global Matches:** file_cluster_2: 15.588, file_cluster_13: 15.69, file_cluster_17: 15.704
- **Magnitude:** 1444.91 | **LOC:** 243 | **CtrlFlow:** 92.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (45.6603%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 290`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `safety: 18`, `doc: 27`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` self::TOO_MANY_PIXEL_ERROR => 'TOO_MANY_PIXEL_ERROR', self::TOO_WIDE_ERROR => 'TOO_WIDE_ERROR', self::TOO_NARROW_ERROR => 'TOO_NARROW_ERROR', self::RATIO_TOO_SMALL_ERROR => 'RATIO_TOO_SMALL_ERROR', self::RATIO_TOO_BIG_ERROR => 'RATIO_TOO_BIG_ERROR', self::INVALID_MIME_TYPE_ERROR => 'INVALID_MIME_TYPE_ERROR', self::EMPTY_ERROR => 'EMPTY_ERROR', self::SIZE_NOT_DETECTED_ERROR => 'SIZE_NOT_DETECTED_ERROR'...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.662 IQR)
- **Top Global Matches:** file_cluster_8: 10.662, file_cluster_7: 11.267, file_cluster_13: 11.349
- **Magnitude:** 1293.06 | **LOC:** 1755 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 83.3%
- **Risk Profile:** Cognitive Load (23.4884%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLastError` (Impact: 3.7)
  * `connect` (Impact: 3.2)
  * `migrate` (Impact: 3.2)
  * `pconnect` (Impact: 3.2)
  * `xautoclaim` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 699`, `args: 344`, `func_start: 344`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 196`
* *Architecture:* `api: 345`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Symfony\Component\Cache\Traits\Relay\Relay21Trait, Relay21Trait, Symfony\Contracts\Service\ResetInterface, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Component\Cache\Traits\Relay\Relay20Trait, Relay20Trait, RedisProxyTrait 
        resetLazyObject
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Tests/Dumper/PhpDumperTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.747 IQR)
- **Top Global Matches:** file_cluster_13: 12.747, file_cluster_8: 12.927, file_cluster_0: 13.092
- **Magnitude:** 1287.7 | **LOC:** 2612 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (70.1311%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getStripCommentsCodes` (Impact: 30.3)
  * `testLazyArgumentProvideGenerator` (Impact: 16.0)
  * `testAddService` (Impact: 13.1)
  * `testNonSharedLazyAsFiles` (Impact: 10.7)
  * `testCircularDynamicEnv` (Impact: 9.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 725`, `args: 126`, `func_start: 126`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 600`, `duplicate_logic: 12`, `orphaned_logic: 108`
* *Architecture:* `io: 1`, `api: 148`, `concurrency: 2`, `import: 116`
* *Defense:* `safety: 20`, `doc: 13`, `test: 110`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\DependencyInjection\Argument\ServiceLocator, container10.php', autowire_closure.php', Symfony\Component\DependencyInjection\Tests\Compiler\SingleMethodInterface, container_uninitialized_ref.php', services_query_string_env.php', container_env_in_id.php'...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/HttpFoundation/Request.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.178 IQR)
- **Top Global Matches:** file_cluster_13: 14.178, file_cluster_8: 14.272, file_cluster_17: 14.278
- **Magnitude:** 1272.0 | **LOC:** 2274 | **CtrlFlow:** 57.8% | **Authorship Centralization:** 34.8%
- **Risk Profile:** Cognitive Load (47.1392%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 159.0)
  * `duplicate` (Impact: 44.5)
  * `getFormat` (Impact: 38.9)
  * `getRelativeUriForPath` (Impact: 33.8)
  * `getHost` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 237`, `args: 71`, `func_start: 70`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 602`, `dead_code: 2`
* *Architecture:* `io: 23`, `api: 91`, `import: 10`
* *Defense:* `safety: 61`, `doc: 106`, `test: 3`, `immutability_locks: 7`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.82
  * `Choke Point (Betweenness):` 7.8e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` 
    private function getBaseUrlReal(): string
    
        return $this->baseUrl ??= $this->prepareBaseUrl(, 
    public function getBaseUrl(): string
    
        $trustedPrefix = '', Symfony\Component\HttpFoundation\Exception\SuspiciousOperationException, Symfony\Component\HttpFoundation\Session\SessionInterface, 
    public static function enableHttpMethodParameterOverride(): void
    
        self::$httpMethodParameterOverride = true, Symfony\Component\HttpFoundation\Exception\JsonException, Symfony\Component\HttpFoundation\Exception\BadRequestException, Symfony\Component\HttpFoundation\Exception\SessionNotFoundException...
  * `Imported By (In-Degree: 504):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpClient/HttpClientTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.929 IQR)
- **Top Global Matches:** file_cluster_4: 14.929, file_cluster_13: 14.951, file_cluster_11: 14.989
- **Magnitude:** 1259.92 | **LOC:** 866 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (61.8054%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `prepareRequest` (Impact: 156.9)
    * *Intent:* /** * Provides the common logic from writing HttpClientInterface implementations. * * All private me...
  * `normalizeBody` (Impact: 133.3)
  * `parseUrl` (Impact: 97.6)
  * `mergeDefaultOptions` (Impact: 88.5)
  * `resolveUrl` (Impact: 73.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 126`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 473`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 5`, `concurrency: 18`, `import: 6`
* *Defense:* `safety: 105`, `doc: 24`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.194
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Symfony\Component\HttpClient\Exception\TransportException, Symfony\Component\HttpClient\Exception\InvalidArgumentException, Symfony\Component\Mime\MimeTypes, $host), polyfill-intl-idn".', Symfony\Component\HttpClient\Response\StreamWrapper, Symfony\Component\HttpClient\Response\StreamableInterface
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.137 IQR)
- **Top Global Matches:** file_cluster_13: 14.137, file_cluster_8: 14.278, file_cluster_11: 14.424
- **Magnitude:** 1205.84 | **LOC:** 936 | **CtrlFlow:** 63.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (85.3529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseDefinition` (Impact: 499.7)
  * `resolveServices` (Impact: 96.8)
  * `parseCallable` (Impact: 42.2)
  * `parseDefaults` (Impact: 39.5)
  * `parseDefinitions` (Impact: 23.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 179`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 380`
* *Architecture:* `api: 25`, `import: 19`
* *Defense:* `safety: 118`, `doc: 7`, `test: 1`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\DependencyInjection\Exception\LogicException, Symfony\Component\DependencyInjection\Definition, expression-language".', Symfony\Component\DependencyInjection\Alias, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\ContainerBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.318 IQR)
- **Top Global Matches:** file_cluster_13: 13.318, file_cluster_8: 13.688, file_cluster_11: 13.975
- **Magnitude:** 1157.98 | **LOC:** 3589 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 35.3%
- **Risk Profile:** Cognitive Load (76.4498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 242.5)
  * `registerWorkflowConfiguration` (Impact: 84.0)
  * `registerHtmlSanitizerConfiguration` (Impact: 44.4)
  * `registerProfilerConfiguration` (Impact: 37.9)
  * `registerSessionConfiguration` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 478`, `args: 45`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 391`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 235`
* *Defense:* `safety: 51`, `doc: 4`, `test: 16`, `sync_locks: 28`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 190):` Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\ObjectMapper\ObjectMapperInterface, Composer\InstalledVersions, Symfony\Component\Console\EventListener\ValidateQuestionInputListener, Symfony\Component\Lock\LockFactory, Symfony\Contracts\Cache\CallbackInterface, Http\Client\HttpClient, Symfony\Contracts\Translation\LocaleAwareInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Process/Tests/ProcessTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.068 IQR)
- **Top Global Matches:** file_cluster_8: 13.068, file_cluster_0: 13.173, file_cluster_13: 13.251
- **Magnitude:** 1082.24 | **LOC:** 1775 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (61.13%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getProcess` (Impact: 17.7)
  * `testNonBlockingNorClearingIteratorOutput` (Impact: 10.4)
  * `getProcessForCode` (Impact: 10.0)
  * `pipesCodeProvider` (Impact: 9.8)
  * `testIdleTimeoutNotExceededWhenOutputIsSe` (Impact: 9.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 219`, `args: 145`, `func_start: 123`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 412`, `duplicate_logic: 2`, `orphaned_logic: 112`
* *Architecture:* `io: 26`, `api: 120`, `concurrency: 28`, `import: 15`
* *Defense:* `safety: 33`, `doc: 1`, `test: 142`, `sync_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` d.', PHPUnit\Framework\Attributes\RequiresPhpExtension, Symfony\Component\Process\InputStream, SignalListener.php'], PHPUnit\Framework\Attributes\Group, sPhpExtension('pcntl')]
    public function testStopWithTimeoutIsActuallyWorking()
    
        $p = $this->getProcess([self::$phpBin, Symfony\Component\Process\Exception\RuntimeException, Symfony\Component\Process\Exception\ProcessSignaledException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/DependencyInjection/Compiler/AutowirePass.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.244 IQR)
- **Top Global Matches:** file_cluster_13: 14.244, file_cluster_0: 14.425, file_cluster_11: 14.437
- **Magnitude:** 1040.76 | **LOC:** 771 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (81.2461%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `autowireMethod` (Impact: 167.3)
  * `getCombinedAlias` (Impact: 57.7)
  * `autowireCalls` (Impact: 54.9)
  * `doProcessValue` (Impact: 45.1)
  * `set` (Impact: 35.5)
    * *Intent:* /** * Populates the list of available types for a given definition. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 146`, `args: 21`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 488`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 17`
* *Defense:* `safety: 51`, `doc: 10`, `test: 3`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Symfony\Component\DependencyInjection\Exception\RuntimeException, Symfony\Component\DependencyInjection\Exception\AutowiringFailedException, Symfony\Component\DependencyInjection\Attribute\AutowireInline, Symfony\Component\DependencyInjection\Definition, Symfony\Component\DependencyInjection\Exception\ParameterNotFoundException, Symfony\Component\DependencyInjection\ContainerBuilder, Symfony\Component\Config\Resource\ClassExistenceResource, Symfony\Component\DependencyInjection\Reference...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.359 IQR)
- **Top Global Matches:** file_cluster_13: 14.359, file_cluster_8: 14.775, file_cluster_11: 14.79
- **Magnitude:** 1018.8 | **LOC:** 1837 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (48.0937%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createService` (Impact: 184.5)
  * `doResolveServices` (Impact: 59.2)
  * `resolveEnvPlaceholders` (Impact: 50.9)
  * `willBeAvailable` (Impact: 27.5)
  * `inVendors` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 218`, `args: 49`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 372`
* *Architecture:* `api: 56`, `concurrency: 6`, `import: 41`
* *Defense:* `safety: 63`, `doc: 100`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.706
  * `Choke Point (Betweenness):` 0.000799 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 37):` Composer\InstalledVersions, Symfony\Component\DependencyInjection\Exception\ServiceCircularReferenceException, Symfony\Component\Config\Resource\ClassExistenceResource, Composer\Autoload\ClassLoader, Symfony\Component\DependencyInjection\Argument\ServiceLocator, Symfony\Component\DependencyInjection\Compiler\Compiler, Symfony\Component\DependencyInjection\Compiler\CompilerPassInterface, Symfony\Component\DependencyInjection\ParameterBag\EnvPlaceholderParameterBag...
  * `Imported By (In-Degree: 423):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Process/Process.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.108 IQR)
- **Top Global Matches:** file_cluster_13: 14.108, file_cluster_8: 14.333, file_cluster_7: 14.364
- **Magnitude:** 1018.8 | **LOC:** 1727 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 41.7%
- **Risk Profile:** Cognitive Load (47.1274%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stop` (Impact: 205.6)
  * `start` (Impact: 57.1)
  * `buildShellCommandline` (Impact: 38.7)
    * *Intent:* /** * Returns an iterator to the output of the process, with the output type as keys (Process::OUT/E...
  * `waitUntil` (Impact: 25.7)
    * *Intent:* * This is identical to run() except that an exception is thrown if the process * exits with a non-ze...
  * `__construct` (Impact: 23.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 141`, `args: 50`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 4`, `state_mutation: 356`, `dead_code: 1`
* *Architecture:* `io: 3`, `api: 58`, `import: 10`
* *Defense:* `safety: 22`, `doc: 116`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.649
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Symfony\Component\Process\Exception\ProcessFailedException, writable.', ProcessIsStarted(__FUNCTION__, Symfony\Component\Process\Exception\ProcessStartFailedException, ProcessIsTerminated(__FUNCTION__, Symfony\Component\Process\Pipes\UnixPipes, Symfony\Component\Process\Exception\InvalidArgumentException, Symfony\Component\Process\Pipes\WindowsPipes...
  * `Imported By (In-Degree: 41):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RedisProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.738 IQR)
- **Top Global Matches:** file_cluster_8: 10.738, file_cluster_7: 11.332, file_cluster_13: 11.4
- **Magnitude:** 987.94 | **LOC:** 1298 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (30.8318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLastError` (Impact: 3.7)
  * `getPersistentID` (Impact: 3.7)
  * `migrate` (Impact: 3.2)
  * `connect` (Impact: 3.0)
  * `open` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 515`, `args: 253`, `func_start: 253`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 175`
* *Architecture:* `api: 253`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Symfony\Component\VarExporter\LazyObjectInterface, Redis63ProxyTrait, Symfony\Contracts\Service\ResetInterface, Redis62ProxyTrait, RedisProxyTrait 
        resetLazyObject
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayClusterProxy.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.579 IQR)
- **Top Global Matches:** file_cluster_8: 10.579, file_cluster_7: 11.186, file_cluster_13: 11.251
- **Magnitude:** 983.26 | **LOC:** 1355 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (21.3471%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getLastError` (Impact: 3.7)
  * `__construct` (Impact: 3.0)
    * *Intent:* /** * @internal
  * `xautoclaim` (Impact: 3.0)
  * `xpending` (Impact: 3.0)
  * `georadius` (Impact: 2.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 539`, `args: 264`, `func_start: 264`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 140`
* *Architecture:* `api: 265`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Symfony\Component\Cache\Traits\Relay\RelayCluster20Trait, Symfony\Component\Cache\Traits\Relay\RelayCluster21Trait, RelayCluster21Trait, Symfony\Contracts\Service\ResetInterface, Symfony\Component\VarExporter\LazyObjectInterface, RelayCluster20Trait, RedisProxyTrait 
        resetLazyObject
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Bridge/Doctrine/Tests/Form/Type/EntityTypeTest.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.905 IQR)
- **Top Global Matches:** file_cluster_8: 11.905, file_cluster_13: 12.111, file_cluster_7: 12.406
- **Magnitude:** 979.32 | **LOC:** 1993 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (36.6401%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setUp` (Impact: 15.9)
  * `testLoaderCaching` (Impact: 9.7)
  * `testLoaderCachingWithParameters` (Impact: 9.7)
  * `testOverrideChoicesValuesWithCallable` (Impact: 8.4)
  * `testWithSameLoaderAndDifferentChoiceValu` (Impact: 8.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 426`, `args: 113`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `state_mutation: 405`, `duplicate_logic: 18`, `orphaned_logic: 74`
* *Architecture:* `api: 94`, `import: 36`
* *Defense:* `safety: 11`, `test: 177`, `sync_locks: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` Doctrine\ORM\EntityRepository, Symfony\Bridge\Doctrine\Types\UuidType, 'choice_label' => 'name', ])
            ->createView(, Symfony\Bridge\Doctrine\Tests\Fixtures\SingleAssociationToIntIdEntity, Symfony\Component\Form\ChoiceList\LazyChoiceList, Symfony\Bridge\Doctrine\Form\Type\EntityType, Symfony\Component\Form\Exception\RuntimeException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bridge/Twig/Tests/Extension/AbstractLayoutTestCase.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.395 IQR)
- **Top Global Matches:** file_cluster_8: 11.395, file_cluster_7: 11.943, file_cluster_13: 12.046
- **Magnitude:** 978.76 | **LOC:** 2830 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (19.1242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testSingleChoiceExpandedWithPlaceholder` (Impact: 8.2)
  * `testSingleChoiceExpandedWithPlaceholderW` (Impact: 8.2)
  * `testMultipleChoiceExpandedWithoutTransla` (Impact: 8.2)
  * `testMultipleChoiceExpandedAttributes` (Impact: 8.2)
  * `testMultipleChoiceExpanded` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 242`, `args: 154`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 733`, `state_mutation: 287`, `planned_debt: 2`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 148`
* *Architecture:* `api: 150`, `import: 13`
* *Defense:* `safety: 6`, `doc: 3`, `test: 16`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` d.', 'choice_translation_domain' => false, 'expanded' => false,  has *no* empty value, option)=2]
', 'placeholder' => 'Test&Me', 'maxlength' => 10, d' => true...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Symfony/Component/Serializer/Attribute/Context.php` (PHP) | Magnitude: 35.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, state_mutation: 13, structural_boundaries: 8, doc: 7
- `src/Symfony/Component/Routing/Tests/Fixtures/Psr4Controllers/SubNamespace/EvenDeeperNamespace/MyOtherController.php` (PHP) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 10, ssr_boundaries: 8, api: 7
- `src/Symfony/Component/DependencyInjection/Tests/Compiler/PriorityTaggedServiceTraitTest.php` (PHP) | Magnitude: 255.42 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 448, structural_boundaries: 203, memory_alloc: 120, state_mutation: 112
- `src/Symfony/Component/Serializer/Attribute/DiscriminatorMap.php` (PHP) | Magnitude: 22.74 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 7, branch: 6, safety: 6
- `src/Symfony/Component/Console/Tests/ArgumentResolver/ValueResolver/MapInputValueResolverTest.php` (PHP) | Magnitude: 156.98 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 209, structural_boundaries: 141, memory_alloc: 86, state_mutation: 84

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/Symfony/Component/EventDispatcher/EventSubscriberInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: ownership: 4, structural_boundaries: 3, doc: 3, branch: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Symfony/Component/VarExporter/ProxyHelper.php` (PHP) | Magnitude: 707.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 319, state_mutation: 318, branch: 188, structural_boundaries: 63
- `src/Symfony/Component/VarDumper/Caster/SymfonyCaster.php` (PHP) | Magnitude: 93.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, state_mutation: 37, structural_boundaries: 26, planned_debt: 17
- `src/Symfony/Component/Serializer/Normalizer/DenormalizableInterface.php` (PHP) | Magnitude: 52.55 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 6, doc: 6, bitwise_ops: 4, structural_boundaries: 3
- `src/Symfony/Component/Serializer/Normalizer/NormalizableInterface.php` (PHP) | Magnitude: 52.55 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: state_mutation: 6, bitwise_ops: 6, doc: 5, structural_boundaries: 3
- `src/Symfony/Component/VarDumper/Caster/ArgsStub.php` (PHP) | Magnitude: 78.0 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 36, branch: 19, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Symfony/Component/Console/Resources/completion.zsh` (SHELL) | Magnitude: 82.72 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 48, indent_spaces: 38, branch: 28, reflection_metaprogramming: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Symfony/Component/Config/Definition/VariableNode.php` (PHP) | Magnitude: 75.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 23, state_mutation: 22, api: 14
- `src/Symfony/Component/Console/Tests/Command/CommandTest.php` (PHP) | Magnitude: 264.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 378, structural_boundaries: 190, state_mutation: 92, test: 80
- `src/Symfony/Component/HttpKernel/Tests/Controller/ArgumentResolver/BackedEnumValueResolverTest.php` (PHP) | Magnitude: 55.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 38, state_mutation: 14, args: 9
- `src/Symfony/Component/VarExporter/Tests/ProxyHelperTest.php` (PHP) | Magnitude: 147.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 79, state_mutation: 42, args: 28
- `src/Symfony/Component/Mailer/Tests/Transport/Smtp/Stream/SocketStreamTest.php` (PHP) | Magnitude: 9.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 10, test: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Symfony/Component/Config/Definition/Builder/ExprBuilder.php` (PHP) | Magnitude: 178.5 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 119, state_mutation: 64, structural_boundaries: 42, api: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Symfony/Component/Intl/Data/Util/LocaleScanner.php` (PHP) | Magnitude: 50.04 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, state_mutation: 26, structural_boundaries: 11, branch: 6
- `src/Symfony/Component/Validator/Constraints/DateTimeValidator.php` (PHP) | Magnitude: 34.4 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, branch: 13, structural_boundaries: 12, ui_framework: 8
- `src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher2.php` (PHP) | Magnitude: 0.08 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 101, state_mutation: 60, bitwise_ops: 58, branch: 26
- `src/Symfony/Component/Routing/Tests/Fixtures/dumper/compiled_url_matcher1.php` (PHP) | Magnitude: 0.08 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 60, bitwise_ops: 58, branch: 26
- `src/Symfony/Component/Config/Definition/EnumNode.php` (PHP) | Magnitude: 153.26 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 107, structural_boundaries: 42, branch: 41, state_mutation: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Symfony/Component/Security/Core/Exception/UserNotFoundException.php` (PHP) | Magnitude: 33.54 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, api: 10, state_mutation: 7
- `src/Symfony/Component/Validator/Constraints/ImageValidator.php` (PHP) | Magnitude: 227.86 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 212, branch: 85, state_mutation: 54, structural_boundaries: 37
- `src/Symfony/Component/ErrorHandler/Resources/views/exception.html.php` (PHP) | Magnitude: 41.12 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, branch: 96, structural_boundaries: 33, state_mutation: 24
- `src/Symfony/Component/Validator/Tests/Constraints/LengthValidatorTest.php` (PHP) | Magnitude: 115.5 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 305, structural_boundaries: 62, ui_framework: 48, args: 26
- `src/Symfony/Component/HtmlSanitizer/Visitor/Node/DocumentNode.php` (PHP) | Magnitude: 24.24 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 9, state_mutation: 9, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Symfony/Component/HttpClient/Internal/AmpClientState.php` (PHP) | Magnitude: 232.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 93, structural_boundaries: 45, branch: 34
- `src/Symfony/Component/Workflow/Tests/Dumper/MermaidDumperTest.php` (PHP) | Magnitude: 111.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, state_mutation: 51, structural_boundaries: 34, concurrency: 26
- `src/Symfony/Component/Console/Helper/TreeNode.php` (PHP) | Magnitude: 81.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 27, state_mutation: 27, branch: 13
- `src/Symfony/Bundle/FrameworkBundle/Tests/Command/CachePruneCommandTest.php` (PHP) | Magnitude: 58.8 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 45, concurrency: 20, args: 13
- `src/Symfony/Bridge/Twig/Tests/Command/DebugCommandTest.php` (PHP) | Magnitude: 181.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 160, state_mutation: 88, structural_boundaries: 50, concurrency: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/Symfony/Component/Security/Core/User/UserInterface.php` (PHP) | Magnitude: 40.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, planned_debt: 3, args: 2
- `src/Symfony/Component/VarDumper/Caster/OpenSSLCaster.php` (PHP) | Magnitude: 31.26 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 19, state_mutation: 14, planned_debt: 8
- `src/Symfony/Component/VarDumper/Cloner/Cursor.php` (PHP) | Magnitude: 51.52 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 21, indent_spaces: 21, state_mutation: 15, planned_debt: 4
- `src/Symfony/Component/VarDumper/Caster/SplCaster.php` (PHP) | Magnitude: 115.92 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 34, structural_boundaries: 30, branch: 23
- `src/Symfony/Component/VarDumper/Caster/StubCaster.php` (PHP) | Magnitude: 37.74 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, planned_debt: 12, indent_spaces: 12, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Symfony/Component/PropertyInfo/Tests/Fixtures/PseudoTypesDummy.php` (PHP) | Magnitude: 0.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 51, api: 27, indent_spaces: 27, structural_boundaries: 2
- `src/Symfony/Component/PropertyInfo/Tests/Fixtures/Dummy.php` (PHP) | Magnitude: 0.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 83, indent_spaces: 82, api: 60, structural_boundaries: 20
- `src/Symfony/Component/Console/Style/StyleInterface.php` (PHP) | Magnitude: 263.9 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 21, structural_boundaries: 20, args: 18, func_start: 18
- `src/Symfony/Component/Form/FormBuilderInterface.php` (PHP) | Magnitude: 138.38 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, state_mutation: 12, structural_boundaries: 10, args: 7
- `src/Symfony/Component/PropertyAccess/PropertyAccessorInterface.php` (PHP) | Magnitude: 56.4 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, bitwise_ops: 9, structural_boundaries: 6, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Symfony/Bundle/TwigBundle/Tests/DependencyInjection/ConfigurationTest.php` (PHP) | Magnitude: 26.08 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 18, state_mutation: 12, memory_alloc: 8
- `src/Symfony/Component/DependencyInjection/Exception/ParameterCircularReferenceException.php` (PHP) | Magnitude: 14.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, branch: 3, api: 3
- `src/Symfony/Component/Dotenv/Exception/FormatException.php` (PHP) | Magnitude: 16.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 7, state_mutation: 6, api: 3
- `src/Symfony/Component/HttpFoundation/Test/Constraint/ResponseHeaderSame.php` (PHP) | Magnitude: 14.38 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, api: 5, args: 4
- `src/Symfony/Component/Messenger/Bridge/Amqp/Transport/Connection.php` (PHP) | Magnitude: 547.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 431, state_mutation: 194, branch: 127, structural_boundaries: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Symfony/Component/Notifier/Exception/TransportExceptionInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, func_start: 1
- `src/Symfony/Component/Translation/Exception/ProviderExceptionInterface.php` (PHP) | Magnitude: 32.4 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, args: 1, func_start: 1
- `src/Symfony/Component/PropertyAccess/PropertyPathBuilder.php` (PHP) | Magnitude: 231.54 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 120, branch: 30, structural_boundaries: 27
- `src/Symfony/Component/Form/RequestHandlerInterface.php` (PHP) | Magnitude: 43.28 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, state_mutation: 3, doc: 3, args: 2
- `src/Symfony/Component/Config/Loader/LoaderInterface.php` (PHP) | Magnitude: 104.12 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 6, state_mutation: 6, args: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Symfony/Component/HttpKernel/Kernel.php` -> Churn: **100.0%** | Cog Load: 73.5772% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` -> Churn: **91.45%** | Cog Load: 76.4498% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` -> Churn: **77.94%** | Cog Load: 61.1852% | Debt: 0.0%
- `src/Symfony/Component/ObjectMapper/ObjectMapper.php` -> Churn: **64.45%** | Cog Load: 58.5493% | Debt: 0.0%
- `src/Symfony/Component/DependencyInjection/Loader/PhpFileLoader.php` -> Churn: **57.73%** | Cog Load: 83.2962% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Symfony/Component/VarDumper/Dumper/HtmlDumper.php` -> **Dariusz Ruminski** (100.0% isolated ownership) | Magnitude: 4540.68
- `src/Symfony/Component/Yaml/Parser.php` -> **Younes ENNAJI** (100.0% isolated ownership) | Magnitude: 1689.42
- `src/Symfony/Component/Validator/Constraints/Video.php` -> **symfonyaml** (100.0% isolated ownership) | Magnitude: 1686.14
- `src/Symfony/Component/Cache/Traits/RelayProxy.php` -> **Christian Flothmann** (83.3% isolated ownership) | Magnitude: 1293.06
- `src/Symfony/Component/Cache/Traits/RedisProxy.php` -> **Christian Flothmann** (100.0% isolated ownership) | Magnitude: 987.94

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

- `src/Symfony/Component/HttpFoundation/Response.php` -> **Severity: 429.3** (Blast Radius: 4.293 * Doc Risk: 100.0%)
- `src/Symfony/Component/Notifier/Transport/Dsn.php` -> **Severity: 320.981** (Blast Radius: 3.213 * Doc Risk: 99.9008%)
- `src/Symfony/Component/VarDumper/Cloner/Stub.php` -> **Severity: 266.3** (Blast Radius: 2.663 * Doc Risk: 100.0%)
- `src/Symfony/Component/Console/Output/OutputInterface.php` -> **Severity: 239.895** (Blast Radius: 2.399 * Doc Risk: 99.9978%)
- `src/Symfony/Component/Validator/Exception/InvalidOptionsException.php` -> **Severity: 228.276** (Blast Radius: 2.614 * Doc Risk: 87.3281%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
