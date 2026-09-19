# ARCHITECTURAL_BRIEF: symfony
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/symfony/symfony.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 12963 analyzed artifact(s), 1652085 LOC.
- **Load-bearing artifact:** `src/Symfony/Component/HttpFoundation/Request.php` -- 504 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Symfony/Component/Intl/Tests/ResourceBundleTestCase.php` -- pulls in 712 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Symfony/Bundle/SecurityBundle/Resources/views/Collector/security.html.twig` at magnitude 5782.43 (structural weight, not risk).
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
| Total Artifacts | 14058 |
| Analyzed Artifacts (Scanned) | 12963 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1095 |
| Total LOC | 1652085 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.2% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7849 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0976 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0292 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 693 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 10332 | 1611840 | 79.7% |
| YAML | 782 | 11476 | 6.0% |
| MARKDOWN | 639 | 0 | 4.9% |
| JSON | 396 | 15064 | 3.1% |
| XML | 367 | 0 | 2.8% |
| PLAINTEXT | 300 | 0 | 2.3% |
| HTML | 101 | 10740 | 0.8% |
| CSS | 19 | 2113 | 0.1% |
| JAVASCRIPT | 15 | 595 | 0.1% |
| SHELL | 6 | 191 | 0.0% |
| CSV | 3 | 6 | 0.0% |
| MAKEFILE | 2 | 39 | 0.0% |
| TYPESCRIPT | 1 | 21 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.161`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.16; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 29%, Declarative / Non-Code 20%, Interface Declarations Files 17%, Encapsulated Accessors Files 8%, Parameter Forwarders Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12024 | 92.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 939 | 7.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1095*

**Composition by Extension & Reason:**
- `no_extension`: 389x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Unsupported Format (.undeterminable), 5x Excluded (Binary Format Detected)
- `.xlf`: 139x Unsupported Format (.xlf)
- `.php`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 8 exceeds 500 chars), 2x Excluded (Binary Format Detected)
- `.phpt`: 82x Unsupported Format (.phpt)
- `.yml`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Zero-Density Threshold (LOC: 60, Signals: 0)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 36.0 | 44.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.9 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.3 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 38.8 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.7 | 6.1 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 49389 | 4895 | 9 | `src/Symfony/Component/HttpKernel/Tests/Controller/ArgumentResolver/RequestPayloadValueResolverTest.php` |
| cleanup | 971 | 420 | 0 | `src/Symfony/Component/Dotenv/Tests/DotenvTest.php` |
| guards | 42946 | 6040 | 9 | `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` |
| danger | 14713 | 2608 | 2 | `src/Symfony/Bridge/Twig/Tests/Extension/AbstractBootstrap3LayoutTestCase.php` |
| concurrency | 8921 | 1046 | 0 | `src/Symfony/Component/Filesystem/Tests/PathTest.php` |
| connectivity | 54811 | 7425 | 9 | `src/Symfony/Bridge/Twig/Resources/views/Form/form_div_layout.html.twig` |
| io | 2460 | 607 | 0 | `src/Symfony/Component/Mime/Tests/Header/ParameterizedHeaderTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 311 | 85 | 0 | `src/Symfony/Component/HttpClient/Response/AsyncResponse.php` |
| time | 2027 | 524 | 0 | `src/Symfony/Component/Serializer/Tests/Normalizer/DateTimeNormalizerTest.php` |
| serialization | 1344 | 557 | 0 | `src/Symfony/Component/Serializer/Tests/SerializerTest.php` |
| regex | 999 | 423 | 0 | `src/Symfony/Component/JsonPath/JsonCrawler.php` |
| events | 1845 | 626 | 0 | `src/Symfony/Component/Console/Tests/ApplicationTest.php` |
| tests | 34004 | 2336 | 6 | `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` |
| docs | 13900 | 5127 | 3 | `src/Symfony/Component/HttpFoundation/Request.php` |
| debt | 3860 | 773 | 0 | `src/Symfony/Component/Emoji/Resources/data/emoji-nl.php` |
| mutation | 103600 | 6337 | 20 | `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` |
| dead_code | 22436 | 3082 | 5 | `src/Symfony/Component/OptionsResolver/Tests/OptionsResolverTest.php` |
| credential | 95 | 53 | 0 | `src/Symfony/Component/HttpFoundation/Tests/UriSignerTest.php` |
| threat | 2030 | 744 | 0 | `src/Symfony/Component/PropertyInfo/Extractor/ReflectionExtractor.php` |
| ml_ai | 1307 | 148 | 0 | `src/Symfony/Component/Emoji/Resources/data/emoji-pcm.php` |
| ui | 1965 | 358 | 0 | `src/Symfony/Bridge/Twig/Tests/Extension/TranslationExtensionTest.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Symfony/Component/Mime/Tests/Header/ParameterizedHeaderTest.php` (Hits: 74)
- `src/Symfony/Component/HttpFoundation/Session/Storage/Handler/PdoSessionHandler.php` (Hits: 66)
- `src/Symfony/Component/Mime/Tests/Header/UnstructuredHeaderTest.php` (Hits: 48)

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

- `parseDefinition` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`) -> Impact: **499.7** | LOC: 416
  * *Intent:* /** * @throws InvalidArgumentException When tags are invalid */
- `createConnection` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Cache/Traits/RedisTrait.php`) -> Impact: **337.0** | LOC: 435
  * *Intent:* /** * Creates a Redis connection using a DSN configuration. * * Example DSN: * - redis://localhost * - redis://example.com:1234 * - redis://secret@exa...
- `doParse` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Yaml/Parser.php`) -> Impact: **313.2** | LOC: 409
- `checkAnnotations` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> Impact: **311.7** | LOC: 310
- `validateAndDenormalize` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php`) -> Impact: **298.6** | LOC: 258
  * *Intent:* /** * Validates the submitted data and denormalizes it. * * @throws NotNormalizableValueException * @throws ExtraAttributesException * @throws Missing...
- `getEnv` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`) -> Impact: **259.6** | LOC: 311
- `load` **(Many-Argument Workhorses)** (@ `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) -> Impact: **242.5** | LOC: 554
  * *Intent:* /** * Responds to the app.config configuration parameter. * * @throws LogicException */
- `__construct` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Validator/Constraints/File.php`) -> Impact: **237.2** | LOC: 67
  * *Intent:* * @param string|null $disallowEmptyMessage Enable empty upload validation with this message in case of error * @param string|null $uploadIniSizeErrorM...
- `doGenerate` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Routing/Generator/UrlGenerator.php`) -> Impact: **229.5** | LOC: 162
  * *Intent:* /** * @throws MissingMandatoryParametersException When some parameters are missing that are mandatory for the route * @throws InvalidParameterExceptio...
- `evaluateBracket` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/JsonPath/JsonCrawler.php`) -> Impact: **220.8** | LOC: 293

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector` | 23 | 14338.64 | 10.53% | 1.85% |
| `src/Symfony/Component/Emoji/Resources/data` | 174 | 14335.5 | 1.03% | 1.24% |
| `src/Symfony/Component/Validator/Constraints` | 152 | 11242.79 | 31.18% | 0.9% |
| `src/Symfony/Component/Intl/Resources/data/currencies` | 368 | 7864.08 | 0.04% | 0.02% |
| `src/Symfony/Component/DependencyInjection/Compiler` | 57 | 6467.74 | 52.64% | 6.62% |
| `src/Symfony/Component/Cache/Traits` | 18 | 6194.86 | 34.83% | 11.03% |
| `src/Symfony/Bundle/SecurityBundle/Resources/views/Collector` | 2 | 5792.95 | 5.97% | 4.84% |
| `src/Symfony/Component/HttpClient` | 24 | 5711.2 | 46.93% | 3.98% |
| `src/Symfony/Component/HttpFoundation` | 29 | 5627.92 | 33.1% | 4.69% |
| `src/Symfony/Component/Validator/Tests/Constraints` | 156 | 5542.2 | 7.02% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Symfony/Component/Console/Output/CombinedOutput.php` -> **100.0%** Exposure
- `src/Symfony/Component/Form/Extension/DataCollector/Proxy/ResolvedTypeDataCollectorProxy.php` -> **100.0%** Exposure
- `src/Symfony/Component/Notifier/Bridge/Expo/ExpoOptions.php` -> **100.0%** Exposure
- `src/Symfony/Component/Notifier/Bridge/Novu/NovuSubscriberRecipient.php` -> **100.0%** Exposure
- `src/Symfony/Component/OptionsResolver/OptionConfigurator.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `link` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/EntityValueResolver.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/Attribute/MapEntity.php` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/DataCollector/DoctrineDataCollector.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Symfony/Component/OptionsResolver/Tests/OptionsResolverTest.php` -> **211** Orphaned Functions | **0** Duplicates
- `src/Symfony/Component/Console/Tests/ApplicationTest.php` -> **153** Orphaned Functions | **12** Duplicates
- `src/Symfony/Bridge/Twig/Tests/Extension/AbstractLayoutTestCase.php` -> **151** Orphaned Functions | **0** Duplicates
- `src/Symfony/Component/Serializer/Tests/Normalizer/ObjectNormalizerTest.php` -> **114** Orphaned Functions | **33** Duplicates
- `src/Symfony/Component/DependencyInjection/Tests/ContainerBuilderTest.php` -> **134** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/Symfony/Component/Mailer/Bridge/Sendgrid/Tests/Webhook/SendgridSignedRequestParserTest.php` -> **100.0%** Exposure
- `src/Symfony/Component/Mailer/Tests/EventListener/DkimSignedMessageListenerTest.php` -> **99.9795%** Exposure
- `src/Symfony/Component/Security/Core/Tests/Authentication/Token/AbstractTokenTest.php` -> **98.9215%** Exposure
- `src/Symfony/Component/Mime/Tests/Crypto/DkimSignerTest.php` -> **93.201%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `172` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `42928` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Symfony/Bundle/SecurityBundle/Resources/views/Collector/security.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 5782.43 | **LOC:** 610 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.6%), Complexity Load (formerly Cognitive Load) (11.9%), Debt Markers (formerly Tech Debt) (9.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 87`, `args: 31`, `func_start: 1`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 16`, `planned_debt: 3`
* *Architecture:* `io: 9`, `api: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/request.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 5067.97 | **LOC:** 444 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.7%), Complexity Load (formerly Cognitive Load) (11.2%), Test Surface (formerly Verification) (2.3%), Connectivity (formerly Api Exposure) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 134`, `args: 37`, `func_start: 1`, `class_start: 8`
* *Risk/State:* None
* *Architecture:* `io: 13`, `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 3315.96 | **LOC:** 2439 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **52**; blast radius 0.063; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (83.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.9%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dumpValue` **(Defensive Guards)** (Impact: 129.3)
  * `addNewInstance` **(Many-Argument Workhorses)** (Impact: 114.4)
  * `addService` **(Many-Argument Workhorses)** (Impact: 110.3)
  * `dump` **(Compute Cores)** (Impact: 102.9)
    * *Intent:* /** * Dumps the service container as a PHP class. * * Available options: * * * class: The class name...
  * `collectCircularReferences` **(Many-Argument Workhorses)** (Impact: 77.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 581 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1796
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 775`, `structural_boundaries: 401`, `args: 60`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 634`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 129`, `doc: 21`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.003105
  * `Imports (Out-Degree: 37):` $autoloadFile, $this->containerDir.\DIRECTORY_SEPARATOR.$file, ) \n", = false, = true, Composer\Autoload\ClassLoader, Symfony\Component\Config\Resource\FileResource, Symfony\Component\DependencyInjection\Argument\AbstractArgument...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2596.78 | **LOC:** 3589 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 31.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **252**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.4%), Guard Balance (formerly Safety Score) (80.4%), Complexity Load (formerly Cognitive Load) (68.0%)
- **Documentation Coverage:** 80.5195% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 242.5)
    * *Intent:* /** * Responds to the app.config configuration parameter. * * @throws LogicException */
  * `registerMessengerConfiguration` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `registerTranslatorConfiguration` **(Many-Argument Workhorses)** (Impact: 107.8)
  * `registerNotifierConfiguration` **(Many-Argument Workhorses)** (Impact: 84.9)
  * `registerWorkflowConfiguration` **(Many-Argument Workhorses)** (Impact: 84.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 21 instances
* *Amplified Cascading Flux:* 274 instances
* *Memory Alloc (weighted view):* 195
* *State Mutation (weighted view):* 882
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 676`, `structural_boundaries: 704`, `args: 78`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `state_mutation: 334`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 249`
* *Defense:* `safety: 98`, `doc: 4`, `sync_locks: 67`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.000619
  * `Imports (Out-Degree: 190):` $config['form']) || $this->readConfigEnabled('validation', $config['translator']) || $this->readConfigEnabled('form', $config['translator'])) 
                throw new LogicException('Translation support cannot be enabled, $config['validation'])) 
            if (!class_exists(Translator::class) && $this->readConfigEnabled('translator', $container, $name), Composer\InstalledVersions, Doctrine\ORM\Mapping\Embeddable...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/config.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 2478.02 | **LOC:** 325 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (18.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.5%), Complexity Load (formerly Cognitive Load) (5.8%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 85`, `args: 27`, `func_start: 1`, `class_start: 12`
* *Risk/State:* `fragile_debt: 2`
* *Architecture:* `io: 16`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/serializer.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2192.23 | **LOC:** 375 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.2%), Complexity Load (formerly Cognitive Load) (7.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.4%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 84`, `args: 34`, `func_start: 1`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 15`, `api: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/ErrorHandler/DebugClassLoader.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1946.12 | **LOC:** 1407 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **26**; blast radius 0.335; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.9%), Complexity Load (formerly Cognitive Load) (66.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.5%)
- **Documentation Coverage:** 29.2683% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkAnnotations` **(Many-Argument Workhorses)** (Impact: 311.7)
  * `setReturnType` **(Many-Argument Workhorses)** (Impact: 159.8)
  * `parsePhpDoc` **(Compute Cores)** (Impact: 98.8)
  * `patchMethod` **(Many-Argument Workhorses)** (Impact: 82.8)
    * *Intent:* /** * Utility method to add @return annotations to the Symfony code-base where it triggers self-depr...
  * `fixReturnStatements` **(Compute Cores)** (Impact: 58.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 311 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 952
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 498`, `structural_boundaries: 192`, `args: 22`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 330`, `dead_code: 1`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 9`, `import: 18`
* *Defense:* `safety: 103`, `doc: 27`, `test: 3`, `immutability_locks: 15`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.335
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.022382
  * `Imports (Out-Degree: 3):` $className, $file, $file) 
                    return, $method->name, $parameterName, $parameterType ? $parameterType.' ' : '', ?string $parent): array
    
        $ownInterfaces = class_implements($class, Composer\InstalledVersions...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpFoundation/Request.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1764.88 | **LOC:** 2274 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **504** in-repo importer(s); it depends on **11**; blast radius 6.818; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Connectivity (formerly Api Exposure) (82.0%), Complexity Load (formerly Cognitive Load) (46.9%)
- **Documentation Coverage:** 3.4682% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 159.0)
    * *Intent:* * * The information contained in the URI always take precedence * over the other information (server...
  * `getTrustedValues` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* /** * This method is rather heavy because it splits and merges headers, and it's called by many othe...
  * `duplicate` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* /** * Clones a request and overrides some of its parameters. * * @param array|null $query The GET pa...
  * `getFormat` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* * Gets the format associated with the mime type. * * Resolution order: * 1) Exact match on the full ...
  * `prepareBaseUrl` **(I/O & Config Routines)** (Impact: 26.1)
    * *Intent:* /** * Prepares the base URL. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 276 instances
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 300`, `args: 95`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 341`, `dead_code: 2`
* *Architecture:* `io: 25`, `api: 103`, `import: 6`
* *Defense:* `safety: 71`, `doc: 106`, `immutability_locks: 22`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.818
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.033508
  * `Imports (Out-Degree: 6):` Symfony\Component\HttpFoundation\Exception\BadRequestException, Symfony\Component\HttpFoundation\Exception\ConflictingHeadersException, Symfony\Component\HttpFoundation\Exception\JsonException, Symfony\Component\HttpFoundation\Exception\SessionNotFoundException, Symfony\Component\HttpFoundation\Exception\SuspiciousOperationException, Symfony\Component\HttpFoundation\Session\SessionInterface, an html-form with method "POST" can be altered
     * and used to send a "PUT" or "DELETE" request via the _method request parameter.
     * If these methods are not protected against CSRF, d.
     * If the HTTP method parameter override is enabled...
  * `Imported By (In-Degree: 504):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Validator/Constraints/Video.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1651.0 | **LOC:** 253 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **28**; blast radius 0.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Connectivity (formerly Api Exposure) (84.0%), Complexity Load (formerly Cognitive Load) (83.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 94 instances
* *State Mutation (weighted view):* 299
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 111`
* *Architecture:* `api: 48`, `import: 6`
* *Defense:* `safety: 31`, `doc: 2`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 3):` Symfony\Component\Process\ExecutableFinder, Symfony\Component\Process\Process, Symfony\Component\Validator\Exception\LogicException, ], process".', d to use the Video constraint.', self::CORRUPTED_VIDEO_ERROR => 'CORRUPTED_VIDEO_ERROR', self::EMPTY_ERROR => 'EMPTY_ERROR'...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Yaml/Parser.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1647.42 | **LOC:** 1280 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **2**; blast radius 0.156; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.1%), Complexity Load (formerly Cognitive Load) (84.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.0%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doParse` **(Many-Argument Workhorses)** (Impact: 313.2)
  * `parseValue` **(Many-Argument Workhorses)** (Impact: 99.5)
    * *Intent:* /** * Parses a YAML value. * * @param string $value A YAML value * @param int $flags A bit field of ...
  * `getNextEmbedBlock` **(Many-Argument Workhorses)** (Impact: 77.5)
    * *Intent:* /** * Returns the next embed block of YAML. * * @param int|null $indentation The indent level at whi...
  * `parseBlockScalar` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /** * Parses a block scalar. * * @param string $style The style indicator that was used to begin thi...
  * `lexInlineStructure` **(Many-Argument Workhorses)** (Impact: 52.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 267 instances
* *Memory Alloc (weighted view):* 49
* *State Mutation (weighted view):* 841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 149`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 307`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 7`, `import: 3`
* *Defense:* `safety: 57`, `doc: 12`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.156
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.004772
  * `Imports (Out-Degree: 2):` Symfony\Component\Yaml\Exception\ParseException, Symfony\Component\Yaml\Tag\TaggedValue
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1553.92 | **LOC:** 1837 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **423** in-repo importer(s); it depends on **41**; blast radius 6.703; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Connectivity (formerly Api Exposure) (77.4%), Complexity Load (formerly Cognitive Load) (48.1%)
- **Documentation Coverage:** 7.7922% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createService` **(Many-Argument Workhorses)** (Impact: 184.5)
    * *Intent:* /** * Creates a service for a service definition. * * @throws RuntimeException When the factory defi...
  * `doResolveServices` **(Defensive Guards)** (Impact: 59.2)
  * `resolveEnvPlaceholders` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* /** * Resolves env parameter placeholders in a string or an array. * * @param string|true|null $form...
  * `addResource` **(Defensive Guards)** (Impact: 44.7)
    * *Intent:* /** * @return $this */
  * `merge` **(Defensive Guards)** (Impact: 41.8)
    * *Intent:* * the parameters passed to the container constructor to have precedence * over the loaded ones. * * ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 189 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 44
* *State Mutation (weighted view):* 606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 368`, `structural_boundaries: 340`, `args: 84`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 228`
* *Architecture:* `api: 68`, `concurrency: 1`, `import: 41`
* *Defense:* `safety: 119`, `doc: 81`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.703
  * `Choke Point (Betweenness):` 0.000412 | `Ripple Effect (Closeness):` 0.022004
  * `Imports (Out-Degree: 37):` Composer\Autoload\ClassLoader, Composer\InstalledVersions, Symfony\Component\Config\Resource\ClassExistenceResource, Symfony\Component\Config\Resource\ComposerResource, Symfony\Component\Config\Resource\DirectoryResource, Symfony\Component\Config\Resource\FileExistenceResource, Symfony\Component\Config\Resource\FileResource, Symfony\Component\Config\Resource\GlobResource...
  * `Imported By (In-Degree: 423):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/JsonPath/JsonCrawler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1448.04 | **LOC:** 1174 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **15**; blast radius 0.157; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.5%), Complexity Load (formerly Cognitive Load) (82.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.2%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateBracket` **(Many-Argument Workhorses)** (Impact: 220.8)
  * `evaluateFunction` **(Defensive Guards)** (Impact: 81.8)
  * `compareEquality` **(Stateful Encapsulated Methods)** (Impact: 49.1)
  * `evaluateFilterExpression` **(Many-Argument Workhorses)** (Impact: 46.9)
  * `evaluateScalar` **(Many-Argument Workhorses)** (Impact: 45.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 647
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 216`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 219`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 57`, `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.157
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00077
  * `Imports (Out-Degree: 11):` $expectedArgCount), $name, Psr\Container\ContainerInterface, Symfony\Component\JsonPath\Exception\InvalidArgumentException, Symfony\Component\JsonPath\Exception\InvalidJsonPathException, Symfony\Component\JsonPath\Exception\InvalidJsonStringInputException, Symfony\Component\JsonPath\Exception\JsonCrawlerException, Symfony\Component\JsonPath\Tokenizer\JsonPathToken...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Validator/Constraints/Image.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1409.77 | **LOC:** 243 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 0.065; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.8%), Connectivity (formerly Api Exposure) (84.8%), Complexity Load (formerly Cognitive Load) (80.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 6`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 105`
* *Architecture:* `api: 41`, `import: 1`
* *Defense:* `safety: 18`, `doc: 2`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000308
  * `Imports (Out-Degree: 1):` Symfony\Component\Validator\Exception\InvalidArgumentException, ], self::CORRUPTED_IMAGE_ERROR => 'CORRUPTED_IMAGE_ERROR', self::EMPTY_ERROR => 'EMPTY_ERROR', self::FILENAME_TOO_LONG => 'FILENAME_TOO_LONG', self::INVALID_MIME_TYPE_ERROR => 'INVALID_MIME_TYPE_ERROR', self::LANDSCAPE_NOT_ALLOWED_ERROR => 'LANDSCAPE_NOT_ALLOWED_ERROR', self::NOT_READABLE_ERROR => 'NOT_READABLE_ERROR'...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1385.18 | **LOC:** 3160 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 31.2%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **123**; blast radius 0.479; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (74.5%), Complexity Load (formerly Cognitive Load) (63.6%), Guard Balance (formerly Safety Score) (52.6%)
- **Documentation Coverage:** 99.458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertCachePoolServiceDefinitionIsCreated` **(Stateful Encapsulated Methods)** (Impact: 19.4)
  * `createContainerFromFile` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `testWorkflows` **(I/O & Config Routines)** (Impact: 12.9)
  * `testMessengerTransports` **(I/O & Config Routines)** (Impact: 12.9)
  * `testTranslator` **(I/O & Config Routines)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 670
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 480`, `args: 200`, `func_start: 187`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 474`
* *Architecture:* `api: 176`, `concurrency: 2`, `import: 109`
* *Defense:* `safety: 27`, `doc: 4`, `test: 610`, `sync_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.479
  * `Choke Point (Betweenness):` 9.7e-05 | `Ripple Effect (Closeness):` 0.001001
  * `Imports (Out-Degree: 100):` $container->getParameter('.serializer.named_serializers'), 'crawl')]
    public function testJsonPathEnabled()
    
        $container = $this->createContainerFromClosure(static function (ContainerBuilder $container) 
            $container->loadFromExtension('framework', 'crawl')]
    public function testJsonPathFunctionAttributeAutoconfiguration()
    
        $container = $this->createContainerFromClosure(static function (ContainerBuilder $container) 
            $container->loadFromExtension('framework', 'default_context' => ['enable_max_depth' => false]]], 'include_built_in_encoders' => true, PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group, PHPUnit\Framework\Attributes\IgnoreDeprecations...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1376.02 | **LOC:** 975 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 0.199; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.8%), Complexity Load (formerly Cognitive Load) (63.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.4%)
- **Documentation Coverage:** 44.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateAndDenormalize` **(Many-Argument Workhorses)** (Impact: 298.6)
    * *Intent:* /** * Validates the submitted data and denormalizes it. * * @throws NotNormalizableValueException * ...
  * `denormalize` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `normalize` **(Defensive Guards)** (Impact: 69.9)
  * `denormalizeParameter` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* /** * @internal */
  * `updateData` **(Stateful Encapsulated Methods)** (Impact: 46.2)
    * *Intent:* /** * Sets an attribute and apply the name converter if necessary. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 174 instances
* *State Mutation (weighted view):* 541
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 145`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 193`, `dead_code: 1`
* *Architecture:* `api: 15`, `import: 34`
* *Defense:* `safety: 129`, `doc: 23`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.199
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.002325
  * `Imports (Out-Degree: 34):` Symfony\Component\PropertyAccess\Exception\InvalidArgumentException, Symfony\Component\PropertyAccess\Exception\InvalidTypeException, Symfony\Component\PropertyAccess\Exception\NoSuchIndexException, Symfony\Component\PropertyAccess\Exception\NoSuchPropertyException, Symfony\Component\PropertyAccess\Exception\UninitializedPropertyException, Symfony\Component\PropertyAccess\PropertyAccess, Symfony\Component\PropertyInfo\PropertyTypeExtractorInterface, Symfony\Component\Serializer\Encoder\CsvEncoder...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Tests/ApplicationTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1375.92 | **LOC:** 3250 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 31.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **105**; blast radius 0.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (54.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.2%)
- **Documentation Coverage:** 98.209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testRun` **(I/O & Config Routines)** (Impact: 35.0)
  * `runRestoresSttyTest` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `testFindAlternativeCommands` **(Defensive Guards)** (Impact: 12.6)
  * `testFindAlternativeNamespace` **(Defensive Guards)** (Impact: 11.7)
  * `testFindAlternativeExceptionMessageMultiple` **(Defensive Guards)** (Impact: 10.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 55 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 343
* *State Mutation (weighted view):* 573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 959`, `args: 273`, `func_start: 201`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 463`, `dead_code: 2`, `duplicate_logic: 12`, `unreferenced_by_name: 153`
* *Architecture:* `io: 2`, `api: 197`, `concurrency: 3`, `import: 75`
* *Defense:* `safety: 76`, `doc: 5`, `test: 224`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` $command->getHelp()), '', 'Pre-condition: Original handler for SIGUSR1 must be SIG_DFL.', console %command.name%', 'q', D)], InputOption::VALUE_NONE)], PHPUnit\Framework\Attributes\DataProvider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Serializer/Tests/Normalizer/AbstractObjectNormalizerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1347.4 | **LOC:** 2125 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 11.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **54**; blast radius 0.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Complexity Load (formerly Cognitive Load) (46.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.2%)
- **Documentation Coverage:** 94.702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDenormalizeNullCoalescingValues` **(Annotated & Test Methods)** (Impact: 11.8)
  * `denormalize` **(Defensive Guards)** (Impact: 11.7)
  * `testDenormalizeWithDiscriminatorMapHandlesInvalidTypeValue` **(Compute Cores)** (Impact: 9.0)
  * `testDenormalizeWithNestedDiscriminatorMap` **(Interface Declarations)** (Impact: 7.7)
  * `setAttributeValue` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 680`, `args: 167`, `func_start: 166`, `class_start: 46`
* *Risk/State:* `state_mutation: 355`, `dead_code: 2`, `duplicate_logic: 41`, `unreferenced_by_name: 77`
* *Architecture:* `api: 202`, `concurrency: 6`, `import: 54`
* *Defense:* `safety: 17`, `doc: 31`, `test: 86`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 52):` PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\TestCase, Symfony\Component\PropertyAccess\PropertyAccess, Symfony\Component\PropertyAccess\PropertyPath, Symfony\Component\PropertyInfo\Extractor\PhpDocExtractor, Symfony\Component\PropertyInfo\Extractor\PhpStanExtractor, Symfony\Component\PropertyInfo\Extractor\ReflectionExtractor, Symfony\Component\PropertyInfo\PropertyInfoExtractor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/HttpClient/HttpClientTrait.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1334.52 | **LOC:** 866 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **7**; blast radius 0.194; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.6%), Complexity Load (formerly Cognitive Load) (73.9%), Concurrency Surface (formerly Concurrency) (63.1%)
- **Documentation Coverage:** 10.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareRequest` **(Many-Argument Workhorses)** (Impact: 156.9)
    * *Intent:* /** * Validates and normalizes method, URL and options, and merges them with defaults. * * @throws I...
  * `normalizeBody` **(Many-Argument Workhorses)** (Impact: 133.3)
    * *Intent:* /** * @param array|string|resource|\Traversable|\Closure $body * * @return string|resource|\Closure ...
  * `parseUrl` **(Defensive Guards)** (Impact: 85.7)
    * *Intent:* /** * Parses a URL and fixes its encoding if needed. * * @throws InvalidArgumentException When an in...
  * `mergeDefaultOptions` **(Many-Argument Workhorses)** (Impact: 82.5)
    * *Intent:* /** * @throws InvalidArgumentException When an invalid option is found */
  * `resolveUrl` **(Many-Argument Workhorses)** (Impact: 73.2)
    * *Intent:* /** * Resolves a URL against a base URI. * * @see https://tools.ietf.org/html/rfc3986#section-5.2.2 ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 197 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 328`, `structural_boundaries: 126`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 203`, `dead_code: 1`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 105`, `doc: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.194
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.007959
  * `Imports (Out-Degree: 5):` $host), Symfony\Component\HttpClient\Exception\InvalidArgumentException, Symfony\Component\HttpClient\Exception\TransportException, Symfony\Component\HttpClient\Response\StreamWrapper, Symfony\Component\HttpClient\Response\StreamableInterface, Symfony\Component\Mime\MimeTypes, polyfill-intl-idn".'
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Application.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1299.0 | **LOC:** 1422 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 15.4%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **74**; blast radius 0.988; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Connectivity (formerly Api Exposure) (52.5%), Complexity Load (formerly Cognitive Load) (52.5%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doRenderThrowable` **(Defensive Guards)** (Impact: 67.6)
  * `run` **(Defensive Guards)** (Impact: 59.9)
    * *Intent:* /** * Runs the current application. * * @return int 0 if everything went fine, or an error code * * ...
  * `doRunCommand` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* /** * Runs the current command. * * If an event dispatcher has been attached to the application, * e...
  * `find` **(Compute Cores)** (Impact: 48.2)
    * *Intent:* /** * Finds a command by name or alias. * * Contrary to get, this command tries to find the best * m...
  * `doRun` **(Defensive Guards)** (Impact: 41.5)
    * *Intent:* /** * Runs the current application. * * @return int 0 if everything went fine, or an error code */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 213 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 47
* *State Mutation (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 258`, `args: 69`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 234`, `dead_code: 3`
* *Architecture:* `api: 43`, `import: 46`
* *Defense:* `safety: 80`, `doc: 43`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.988
  * `Choke Point (Betweenness):` 0.00051 | `Ripple Effect (Closeness):` 0.016653
  * `Imports (Out-Degree: 45):` '', '-V', '-h', '-n', '-q', '-v|vv|vvv', info> command'), 'Display this application version')...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayProxy.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1239.06 | **LOC:** 1755 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.4%), Mutation Surface (formerly State Flux) (81.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connect` **(Parameter Forwarders)** (Impact: 3.2)
  * `migrate` **(Parameter Forwarders)** (Impact: 3.2)
  * `pconnect` **(Parameter Forwarders)** (Impact: 3.2)
  * `xautoclaim` **(Parameter Forwarders)** (Impact: 3.0)
  * `xpending` **(Parameter Forwarders)** (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 699`, `args: 344`, `func_start: 344`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 192`
* *Architecture:* `api: 344`, `import: 7`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 4):` RedisProxyTrait 
        resetLazyObject, Relay20Trait, Relay21Trait, Symfony\Component\Cache\Traits\Relay\Relay20Trait, Symfony\Component\Cache\Traits\Relay\Relay21Trait, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Contracts\Service\ResetInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/http_client.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 1204.04 | **LOC:** 175 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Complexity Load (formerly Cognitive Load) (10.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 30`, `args: 12`, `func_start: 1`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Yaml/Inline.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1163.42 | **LOC:** 881 | **CtrlFlow:** 45.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Complexity Load (formerly Cognitive Load) (68.0%), Connectivity (formerly Api Exposure) (15.5%)
- **Documentation Coverage:** 17.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateScalar` **(Many-Argument Workhorses)** (Impact: 177.4)
    * *Intent:* /** * Evaluates scalars and replaces magic values. * * @throws ParseException when object parsing su...
  * `parseMapping` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* /** * Parses a YAML mapping. * * @throws ParseException When malformed inline YAML string is parsed ...
  * `dump` **(Many-Argument Workhorses)** (Impact: 88.6)
    * *Intent:* /** * Dumps a given PHP variable to a YAML string. * * @param mixed $value The PHP variable to conve...
  * `parseSequence` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* /** * Parses a YAML sequence. * * @throws ParseException When malformed inline YAML string is parsed...
  * `parseScalar` **(Many-Argument Workhorses)** (Impact: 59.0)
    * *Intent:* /** * Parses a YAML scalar. * * @throws ParseException When malformed inline YAML string is parsed *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 154 instances
* *State Mutation (weighted view):* 470
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 157`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`, `dead_code: 1`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 31`, `doc: 13`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000231
  * `Imports (Out-Degree: 3):` Symfony\Component\Yaml\Exception\DumpException, Symfony\Component\Yaml\Exception\ParseException, Symfony\Component\Yaml\Tag\TaggedValue, sDoubleQuoting($value):
            case Yaml::DUMP_FORCE_DOUBLE_QUOTES_ON_VALUES & $flags:
                return Escaper::escapeWithDoubleQuotes($value, sSingleQuoting($value):
                $singleQuoted = Escaper::escapeWithSingleQuotes($value
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1141.14 | **LOC:** 936 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.043; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseDefinition` **(Many-Argument Workhorses)** (Impact: 499.7)
    * *Intent:* /** * @throws InvalidArgumentException When tags are invalid */
  * `resolveServices` **(Many-Argument Workhorses)** (Impact: 96.8)
  * `parseCallable` **(Stateful Encapsulated Methods)** (Impact: 42.2)
    * *Intent:* /** * @throws InvalidArgumentException When errors occur */
  * `parseDefaults` **(Defensive Guards)** (Impact: 39.5)
    * *Intent:* /** * @throws InvalidArgumentException */
  * `parseDefinitions` **(Defensive Guards)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 15 instances
* *Amplified Cascading Flux:* 114 instances
* *Memory Alloc (weighted view):* 64
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 179`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`
* *Architecture:* `api: 1`, `import: 19`
* *Defense:* `safety: 118`, `doc: 4`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Symfony\Component\DependencyInjection\Alias, Symfony\Component\DependencyInjection\Argument\AbstractArgument, Symfony\Component\DependencyInjection\Argument\BoundArgument, Symfony\Component\DependencyInjection\Argument\IteratorArgument, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\DependencyInjection\Argument\ServiceLocatorArgument, Symfony\Component\DependencyInjection\Argument\TaggedIteratorArgument, Symfony\Component\DependencyInjection\ChildDefinition...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/messenger.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1138.26 | **LOC:** 220 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (8.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.4%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 32`, `args: 16`, `func_start: 1`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Cache/Traits/RedisTrait.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1111.38 | **LOC:** 827 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (93.6%), Mutation Surface (formerly State Flux) (85.0%), Concurrency Surface (formerly Concurrency) (49.1%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createConnection` **(Many-Argument Workhorses)** (Impact: 337.0)
    * *Intent:* /** * Creates a Redis connection using a DSN configuration. * * Example DSN: * - redis://localhost *...
  * `doClear` **(Defensive Guards)** (Impact: 70.0)
  * `pipeline` **(Defensive Guards)** (Impact: 56.8)
  * `doFetch` **(Stateful Encapsulated Methods)** (Impact: 18.6)
  * `doDelete` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 173 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 146`, `args: 21`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 181`
* *Architecture:* `api: 6`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 117`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.249
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001255
  * `Imports (Out-Degree: 4):` "ext-redis >= 6.1", "ext-relay".', Predis\Command\Redis\UNLINK, Predis\Connection\Aggregate\ClusterInterface, Predis\Connection\Aggregate\RedisCluster, Predis\Connection\Aggregate\ReplicationInterface, Predis\Connection\Cluster\ClusterInterface, Predis\Connection\Cluster\RedisCluster...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Symfony/Component/HttpKernel/Kernel.php` -> Churn: **100.0%** | Cog Load: 70.7039% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` -> Churn: **89.4%** | Cog Load: 68.0405% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` -> Churn: **74.53%** | Cog Load: 63.6331% | Debt: 0.0%
- `src/Symfony/Component/ObjectMapper/ObjectMapper.php` -> Churn: **62.76%** | Cog Load: 70.4074% | Debt: 0.0%
- `src/Symfony/Component/DependencyInjection/Loader/PhpFileLoader.php` -> Churn: **59.01%** | Cog Load: 78.5625% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/serializer.html.twig` -> **Javier Eguiluz** (100.0% isolated ownership) | Magnitude: 2192.23
- `src/Symfony/Component/Yaml/Parser.php` -> **Younes ENNAJI** (100.0% isolated ownership) | Magnitude: 1647.42
- `src/Symfony/Component/Cache/Traits/RelayProxy.php` -> **Christian Flothmann** (83.3% isolated ownership) | Magnitude: 1239.06
- `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/messenger.html.twig` -> **Javier Eguiluz** (100.0% isolated ownership) | Magnitude: 1138.26
- `src/Symfony/Component/Console/Helper/Table.php` -> **Pascal CESCON - Amoifr** (100.0% isolated ownership) | Magnitude: 1031.68

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Symfony/Component/Console/Application.php` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 100.0%)
- `src/Symfony/Component/Console/Command/Command.php` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 100.0%)
- `src/Symfony/Component/ErrorHandler/ErrorHandler.php` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `src/Symfony/Bundle/FrameworkBundle/FrameworkBundle.php` -> **Severity: 0.02** (Bridge: 0.0003 * Flux: 65.9755%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Symfony/Component/DependencyInjection/Exception/ParameterNotFoundException.php` -> **Severity: 3.657** (Embedded: 0.0376 * Error Risk: 97.2474%)
- `src/Symfony/Component/DependencyInjection/Exception/ServiceNotFoundException.php` -> **Severity: 3.509** (Embedded: 0.0378 * Error Risk: 92.7861%)
- `src/Symfony/Component/HttpFoundation/Request.php` -> **Severity: 3.263** (Embedded: 0.0335 * Error Risk: 97.3696%)
- `src/Symfony/Component/VarDumper/Cloner/Stub.php` -> **Severity: 2.742** (Embedded: 0.0281 * Error Risk: 97.6732%)
- `src/Symfony/Component/Validator/Constraint.php` -> **Severity: 2.688** (Embedded: 0.0331 * Error Risk: 81.1227%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Symfony/Component/Notifier/Transport/Dsn.php` -> **Severity: 321.1** (Blast Radius: 3.211 * Doc Risk: 100.0%)
- `src/Symfony/Component/Validator/Exception/InvalidOptionsException.php` -> **Severity: 261.3** (Blast Radius: 2.613 * Doc Risk: 100.0%)
- `src/Symfony/Component/RemoteEvent/Event/Mailer/MailerDeliveryEvent.php` -> **Severity: 204.9** (Blast Radius: 2.049 * Doc Risk: 100.0%)
- `src/Symfony/Component/DependencyInjection/Exception/ParameterNotFoundException.php` -> **Severity: 167.49** (Blast Radius: 1.861 * Doc Risk: 90.0%)
- `src/Symfony/Component/Form/Exception/TransformationFailedException.php` -> **Severity: 140.025** (Blast Radius: 1.867 * Doc Risk: 75.0%)

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
