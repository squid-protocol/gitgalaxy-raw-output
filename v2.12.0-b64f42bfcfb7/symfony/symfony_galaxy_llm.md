# ARCHITECTURAL_BRIEF: symfony
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/symfony/symfony.git` |
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
- **Scope:** 12999 analyzed artifact(s), 1664426 LOC.
- **Load-bearing artifact:** `src/Symfony/Component/HttpFoundation/Request.php` -- 505 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` -- pulls in 208 dependencies, the widest assembly point in the scan.
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
| Total Artifacts | 14067 |
| Analyzed Artifacts (Scanned) | 12999 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1068 |
| Total LOC | 1664426 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.4% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7846 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0978 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.4646 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 663 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 10351 | 1623092 | 79.6% |
| YAML | 795 | 12539 | 6.1% |
| MARKDOWN | 640 | 0 | 4.9% |
| JSON | 398 | 15090 | 3.1% |
| XML | 368 | 0 | 2.8% |
| PLAINTEXT | 300 | 0 | 2.3% |
| HTML | 101 | 10740 | 0.8% |
| CSS | 19 | 2113 | 0.1% |
| JAVASCRIPT | 15 | 595 | 0.1% |
| SHELL | 6 | 191 | 0.0% |
| CSV | 3 | 6 | 0.0% |
| MAKEFILE | 2 | 39 | 0.0% |
| TYPESCRIPT | 1 | 21 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 3 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 12996 |
| cp1252 | cp1252-fallback | 2 |
| latin-1 | latin-1-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 29%, Declarative / Non-Code 20%, Interface Declarations Files 17%, Encapsulated Accessors Files 8%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 12059 | 92.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 940 | 7.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1068*

**Composition by Extension & Reason:**
- `no_extension`: 388x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 207x Unsupported Format (.undeterminable), 5x Excluded (Binary Format Detected)
- `.xlf`: 139x Unsupported Format (.xlf)
- `.phpt`: 82x Unsupported Format (.phpt)
- `.php`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Saturation: Line 8 exceeds 500 chars), 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.yml`: 7x Excluded: Neighborhood Micro-Mass Limit Exceeded, 2x Zero-Density Threshold (LOC: 60, Signals: 0), 1x Zero-Density Threshold (LOC: 68, Signals: 0)
- `.gif`: 15x Excluded (Explicitly Denied Extension: '.gif')
- `.expected`: 15x Unsupported Format (.expected)
- `.ini`: 10x Unsupported Format (.ini), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.res`: 11x Excluded (Binary Format Detected)
- `.dot`: 9x Unsupported Format (.dot)
- `.crt`: 9x Unsupported Format (.crt)
- `.po`: 8x Unsupported Format (.po)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.puml`: 7x Unsupported Format (.puml)
- `.dat`: 5x Unsupported Format (.dat), 1x Excluded (Binary Format Detected)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.4 | 29.3 | 45.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.2 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.8 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 72.9 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 38.8 | 0.7 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.7 | 6.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 49587 | 4906 | 9 | `src/Symfony/Component/HttpKernel/Tests/Controller/ArgumentResolver/RequestPayloadValueResolverTest.php` |
| cleanup | 977 | 423 | 0 | `src/Symfony/Component/Dotenv/Tests/DotenvTest.php` |
| guards | 43343 | 6066 | 9 | `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` |
| danger | 14811 | 2628 | 2 | `src/Symfony/Bridge/Twig/Tests/Extension/AbstractBootstrap3LayoutTestCase.php` |
| concurrency | 9060 | 1058 | 0 | `src/Symfony/Component/Filesystem/Tests/PathTest.php` |
| connectivity | 55095 | 7445 | 9 | `src/Symfony/Bridge/Twig/Resources/views/Form/form_div_layout.html.twig` |
| io | 2534 | 619 | 0 | `src/Symfony/Component/Mime/Tests/Header/ParameterizedHeaderTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 320 | 88 | 0 | `src/Symfony/Component/HttpClient/Response/AsyncResponse.php` |
| time | 2052 | 526 | 0 | `src/Symfony/Component/Serializer/Tests/Normalizer/DateTimeNormalizerTest.php` |
| serialization | 1372 | 562 | 0 | `src/Symfony/Component/Serializer/Tests/SerializerTest.php` |
| regex | 1049 | 432 | 0 | `src/Symfony/Component/String/AbstractUnicodeString.php` |
| events | 1874 | 633 | 0 | `src/Symfony/Component/Console/Tests/ApplicationTest.php` |
| tests | 34512 | 2341 | 6 | `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` |
| docs | 14024 | 5151 | 3 | `src/Symfony/Component/HttpFoundation/Request.php` |
| debt | 3982 | 788 | 0 | `src/Symfony/Component/Emoji/Resources/data/emoji-nl.php` |
| mutation | 104844 | 6361 | 21 | `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` |
| dead_code | 22393 | 2986 | 5 | `src/Symfony/Component/OptionsResolver/Tests/OptionsResolverTest.php` |
| credential | 112 | 66 | 0 | `src/Symfony/Component/HttpFoundation/Tests/UriSignerTest.php` |
| threat | 331347 | 355 | 0 | `src/Symfony/Component/Emoji/Resources/data/emoji-fa.php` |
| ml_ai | 1307 | 148 | 0 | `src/Symfony/Component/Emoji/Resources/data/emoji-pcm.php` |
| ui | 2004 | 361 | 0 | `src/Symfony/Bridge/Twig/Tests/Extension/TranslationExtensionTest.php` |

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

1. **Request.php** (`src/Symfony/Component/HttpFoundation/Request.php`) — 505 inbound connections
2. **ContainerBuilder.php** (`src/Symfony/Component/DependencyInjection/ContainerBuilder.php`) — 423 inbound connections
3. **Response.php** (`src/Symfony/Component/HttpFoundation/Response.php`) — 286 inbound connections
4. **HttpClientInterface.php** (`src/Symfony/Contracts/HttpClient/HttpClientInterface.php`) — 283 inbound connections
5. **ContainerInterface.php** (`src/Symfony/Component/DependencyInjection/ContainerInterface.php`) — 265 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **FrameworkExtension.php** (`src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) — 208 outbound dependencies
2. **ObjectMapperTest.php** (`src/Symfony/Component/ObjectMapper/Tests/ObjectMapperTest.php`) — 115 outbound dependencies
3. **FrameworkExtensionTestCase.php** (`src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php`) — 108 outbound dependencies
4. **PhpDumperTest.php** (`src/Symfony/Component/DependencyInjection/Tests/Dumper/PhpDumperTest.php`) — 106 outbound dependencies
5. **FrameworkBundle.php** (`src/Symfony/Bundle/FrameworkBundle/FrameworkBundle.php`) — 81 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseDefinition` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/DependencyInjection/Loader/ContentLoaderTrait.php`) -> Impact: **409.7** | LOC: 416
  * *Intent:* /** * @throws InvalidArgumentException When tags are invalid */
- `createConnection` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Cache/Traits/RedisTrait.php`) -> Impact: **319.7** | LOC: 435
  * *Intent:* /** * Creates a Redis connection using a DSN configuration. * * Example DSN: * - redis://localhost * - redis://example.com:1234 * - redis://secret@exa...
- `checkAnnotations` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/ErrorHandler/DebugClassLoader.php`) -> Impact: **308.2** | LOC: 310
- `validateAndDenormalize` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php`) -> Impact: **285.4** | LOC: 258
  * *Intent:* /** * Validates the submitted data and denormalizes it. * * @throws NotNormalizableValueException * @throws ExtraAttributesException * @throws Missing...
- `doParse` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Yaml/Parser.php`) -> Impact: **280.3** | LOC: 409
- `getEnv` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/DependencyInjection/EnvVarProcessor.php`) -> Impact: **249.6** | LOC: 311
- `__construct` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Validator/Constraints/File.php`) -> Impact: **237.2** | LOC: 67
  * *Intent:* * @param string|null $disallowEmptyMessage Enable empty upload validation with this message in case of error * @param string|null $uploadIniSizeErrorM...
- `load` **(Many-Argument Workhorses)** (@ `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php`) -> Impact: **233.8** | LOC: 554
  * *Intent:* /** * Responds to the app.config configuration parameter. * * @throws LogicException */
- `request` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/HttpClient/CurlHttpClient.php`) -> Impact: **204.1** | LOC: 242
  * *Intent:* /** * @see HttpClientInterface::OPTIONS_DEFAULTS for available options */
- `doGenerate` **(Many-Argument Workhorses)** (@ `src/Symfony/Component/Routing/Generator/UrlGenerator.php`) -> Impact: **194.7** | LOC: 162
  * *Intent:* /** * @throws MissingMandatoryParametersException When some parameters are missing that are mandatory for the route * @throws InvalidParameterExceptio...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Symfony/Component/Emoji/Resources/data` | 174 | 14335.5 | 0.0% | 1.23% |
| `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector` | 23 | 14334.94 | 10.49% | 1.75% |
| `src/Symfony/Component/Validator/Constraints` | 153 | 11192.75 | 30.7% | 0.63% |
| `src/Symfony/Component/Intl/Resources/data/currencies` | 368 | 7864.08 | 0.0% | 0.02% |
| `src/Symfony/Component/DependencyInjection/Compiler` | 57 | 6327.44 | 51.94% | 4.57% |
| `src/Symfony/Component/Cache/Traits` | 18 | 6165.66 | 34.78% | 10.91% |
| `src/Symfony/Bundle/SecurityBundle/Resources/views/Collector` | 2 | 5792.95 | 5.97% | 4.84% |
| `src/Symfony/Component/HttpClient` | 24 | 5631.8 | 46.78% | 3.93% |
| `src/Symfony/Component/HttpFoundation` | 29 | 5543.52 | 32.79% | 3.45% |
| `src/Symfony/Component/Validator/Tests/Constraints` | 156 | 5455.0 | 6.21% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Symfony/Component/Console/Output/CombinedOutput.php` -> **100.0%** Exposure
- `src/Symfony/Component/Notifier/Bridge/Novu/NovuSubscriberRecipient.php` -> **100.0%** Exposure
- `src/Symfony/Component/OptionsResolver/OptionConfigurator.php` -> **100.0%** Exposure
- `src/Symfony/Component/VarDumper/Caster/DOMCaster.php` -> **100.0%** Exposure
- `src/Symfony/Component/VarDumper/Caster/DoctrineCaster.php` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/build-packages.php` -> **100.0%** Exposure
- `.github/get-modified-packages.php` -> **100.0%** Exposure
- `.github/sync-translations.php` -> **100.0%** Exposure
- `link` -> **100.0%** Exposure
- `src/Symfony/Bridge/Doctrine/ArgumentResolver/Console/EntityValueResolver.php` -> **100.0%** Exposure
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
- `src/Symfony/Component/Form/Tests/Extension/PasswordHasher/Type/PasswordTypePasswordHasherExtensionTest.php` -> **99.9961%** Exposure
- `src/Symfony/Bundle/SecurityBundle/Tests/DependencyInjection/Fixtures/php/container1.php` -> **99.9958%** Exposure
- `src/Symfony/Component/Mailer/Tests/EventListener/DkimSignedMessageListenerTest.php` -> **99.9767%** Exposure
- `src/Symfony/Component/Mailer/Bridge/Mailgun/Tests/Webhook/Fixtures/accepted.json` -> **99.9735%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36865` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Symfony/Bundle/SecurityBundle/Resources/views/Collector/security.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.079)
- **Top Global Matches:** file_cluster_7: 7.079, file_cluster_12: 7.298, file_cluster_13: 8.926
- **Magnitude:** 5782.43 | **LOC:** 610 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.6%), Complexity Load (formerly Cognitive Load) (11.9%), Debt Markers (formerly Tech Debt) (9.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 87`, `args: 31`, `func_start: 1`, `class_start: 60`
* *Risk/State:* `safety_bypasses: 16`, `planned_debt: 3`
* *Architecture:* `io: 9`, `api: 2`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/request.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.897)
- **Top Global Matches:** file_cluster_13: 5.897, file_cluster_2: 6.9, file_cluster_17: 7.711
- **Magnitude:** 5067.97 | **LOC:** 444 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.2%), Complexity Load (formerly Cognitive Load) (11.2%), Test Surface (formerly Verification) (2.3%), Connectivity (formerly Api Exposure) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 134`, `args: 37`, `func_start: 1`, `class_start: 8`
* *Risk/State:* None
* *Architecture:* `io: 13`, `api: 1`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/DependencyInjection/Dumper/PhpDumper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.61)
- **Top Global Matches:** file_cluster_8: 6.61, file_cluster_6: 11.738, file_cluster_4: 20.335
- **Magnitude:** 3246.78 | **LOC:** 2439 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 54.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **34**; blast radius 0.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Complexity Load (formerly Cognitive Load) (82.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.0%)
- **Documentation Coverage:** 83.6066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dumpValue` **(Defensive Guards)** (Impact: 115.4)
    * *Intent:* /** * @throws RuntimeException */
  * `addNewInstance` **(Many-Argument Workhorses)** (Impact: 105.5)
  * `addService` **(Many-Argument Workhorses)** (Impact: 102.3)
  * `dump` **(Many-Argument Workhorses)** (Impact: 98.7)
    * *Intent:* /** * Dumps the service container as a PHP class. * * Available options: * * * class: The class name...
  * `collectCircularReferences` **(Many-Argument Workhorses)** (Impact: 77.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 578 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 1790
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 730`, `structural_boundaries: 401`, `args: 60`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 634`
* *Architecture:* `api: 7`, `concurrency: 2`, `import: 47`
* *Defense:* `safety: 129`, `doc: 21`, `immutability_locks: 6`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.003264
  * `Imports (Out-Degree: 32):` Composer\Autoload\ClassLoader, Symfony\Component\Config\Resource\FileResource, Symfony\Component\DependencyInjection\Argument\AbstractArgument, Symfony\Component\DependencyInjection\Argument\ArgumentInterface, Symfony\Component\DependencyInjection\Argument\IteratorArgument, Symfony\Component\DependencyInjection\Argument\LazyClosure, Symfony\Component\DependencyInjection\Argument\ServiceClosureArgument, Symfony\Component\DependencyInjection\Argument\ServiceLocator...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.381)
- **Top Global Matches:** file_cluster_8: 8.381, file_cluster_6: 10.787, file_cluster_4: 18.872
- **Magnitude:** 2553.78 | **LOC:** 3589 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 28.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **208**; blast radius 0.049; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.5%), Complexity Load (formerly Cognitive Load) (67.2%), Guard Balance (formerly Safety Score) (61.5%)
- **Documentation Coverage:** 80.5195% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load` **(Many-Argument Workhorses)** (Impact: 233.8)
    * *Intent:* /** * Responds to the app.config configuration parameter. * * @throws LogicException */
  * `registerMessengerConfiguration` **(Many-Argument Workhorses)** (Impact: 171.0)
  * `registerTranslatorConfiguration` **(Many-Argument Workhorses)** (Impact: 102.9)
  * `registerNotifierConfiguration` **(Many-Argument Workhorses)** (Impact: 84.9)
  * `registerWorkflowConfiguration` **(Many-Argument Workhorses)** (Impact: 84.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 21 instances
* *Amplified Cascading Flux:* 273 instances
* *Memory Alloc (weighted view):* 195
* *State Mutation (weighted view):* 880
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 656`, `structural_boundaries: 704`, `args: 78`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `state_mutation: 334`
* *Architecture:* `api: 2`, `import: 249`
* *Defense:* `safety: 98`, `doc: 4`, `sync_locks: 67`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.000617
  * `Imports (Out-Degree: 191):` Composer\InstalledVersions, Doctrine\ORM\Mapping\Embeddable, Doctrine\ORM\Mapping\Entity, Doctrine\ORM\Mapping\MappedSuperclass, Http\Client\HttpAsyncClient, Http\Client\HttpClient, PHPStan\PhpDocParser\Parser\PhpDocParser, PhpParser\Parser...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/config.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.923)
- **Top Global Matches:** file_cluster_13: 5.923, file_cluster_2: 6.987, file_cluster_17: 7.809
- **Magnitude:** 2478.02 | **LOC:** 325 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (18.9%), Complexity Load (formerly Cognitive Load) (5.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (4.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 85`, `args: 27`, `func_start: 1`, `class_start: 12`
* *Risk/State:* `fragile_debt: 2`
* *Architecture:* `io: 16`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/serializer.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.728)
- **Top Global Matches:** file_cluster_12: 7.728, file_cluster_13: 7.894, file_cluster_7: 8.589
- **Magnitude:** 2192.23 | **LOC:** 375 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (7.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.8%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 84`, `args: 34`, `func_start: 1`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 6`
* *Architecture:* `io: 15`, `api: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/ErrorHandler/DebugClassLoader.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.184)
- **Top Global Matches:** file_cluster_8: 10.184, file_cluster_3: 15.558, file_cluster_6: 22.035
- **Magnitude:** 1893.12 | **LOC:** 1407 | **CtrlFlow:** 46.0% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **15**; blast radius 0.306; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.5%), Complexity Load (formerly Cognitive Load) (65.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.8%)
- **Documentation Coverage:** 28.0488% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkAnnotations` **(Many-Argument Workhorses)** (Impact: 308.2)
  * `setReturnType` **(Many-Argument Workhorses)** (Impact: 151.8)
  * `patchMethod` **(Many-Argument Workhorses)** (Impact: 80.8)
    * *Intent:* /** * Utility method to add @return annotations to the Symfony code-base where it triggers self-depr...
  * `parsePhpDoc` **(Compute Cores)** (Impact: 73.4)
    * *Intent:* /** * @param \ReflectionClass|\ReflectionMethod|\ReflectionProperty $reflector */
  * `fixReturnStatements` **(Many-Argument Workhorses)** (Impact: 46.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 310 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 950
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 467`, `structural_boundaries: 192`, `args: 22`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 330`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `io: 4`, `api: 9`, `import: 18`
* *Defense:* `safety: 103`, `doc: 27`, `test: 3`, `immutability_locks: 15`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.306
  * `Choke Point (Betweenness):` 0.000435 | `Ripple Effect (Closeness):` 0.028116
  * `Imports (Out-Degree: 4):` $file, Composer\InstalledVersions, Doctrine\Common\Persistence\Proxy, Doctrine\Persistence\Proxy, Mockery\MockInterface, PHPUnit\Framework\MockObject\Matcher\StatelessInvocation, PHPUnit\Framework\MockObject\MockObject, PHPUnit\Framework\MockObject\Stub...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpFoundation/Request.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.913)
- **Top Global Matches:** file_cluster_4: 5.913, file_cluster_12: 9.626, file_cluster_15: 9.941
- **Magnitude:** 1732.38 | **LOC:** 2274 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **505** in-repo importer(s); it depends on **6**; blast radius 6.457; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.0%), Guard Balance (formerly Safety Score) (76.7%), Complexity Load (formerly Cognitive Load) (46.6%)
- **Documentation Coverage:** 3.4682% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create` **(Many-Argument Workhorses)** (Impact: 147.7)
    * *Intent:* * * The information contained in the URI always take precedence * over the other information (server...
  * `getTrustedValues` **(Many-Argument Workhorses)** (Impact: 46.1)
    * *Intent:* /** * This method is rather heavy because it splits and merges headers, and it's called by many othe...
  * `duplicate` **(Many-Argument Workhorses)** (Impact: 44.5)
    * *Intent:* /** * Clones a request and overrides some of its parameters. * * @param array|null $query The GET pa...
  * `getFormat` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* * Gets the format associated with the mime type. * * Resolution order: * 1) Exact match on the full ...
  * `prepareBaseUrl` **(I/O & Config Routines)** (Impact: 25.1)
    * *Intent:* /** * Prepares the base URL. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 274 instances
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 889
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 300`, `args: 95`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 341`
* *Architecture:* `io: 25`, `api: 103`, `import: 6`
* *Defense:* `safety: 71`, `doc: 106`, `immutability_locks: 22`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.457
  * `Choke Point (Betweenness):` 0.000425 | `Ripple Effect (Closeness):` 0.036211
  * `Imports (Out-Degree: 13):` Symfony\Component\HttpFoundation\Exception\BadRequestException, Symfony\Component\HttpFoundation\Exception\ConflictingHeadersException, Symfony\Component\HttpFoundation\Exception\JsonException, Symfony\Component\HttpFoundation\Exception\SessionNotFoundException, Symfony\Component\HttpFoundation\Exception\SuspiciousOperationException, Symfony\Component\HttpFoundation\Session\SessionInterface
  * `Imported By (In-Degree: 505):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Validator/Constraints/Video.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.027)
- **Top Global Matches:** file_cluster_2: 6.027, file_cluster_17: 6.338, file_cluster_15: 6.933
- **Magnitude:** 1651.0 | **LOC:** 253 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Connectivity (formerly Api Exposure) (84.0%), Complexity Load (formerly Cognitive Load) (83.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 3):` Symfony\Component\Process\ExecutableFinder, Symfony\Component\Process\Process, Symfony\Component\Validator\Exception\LogicException
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Yaml/Parser.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.849)
- **Top Global Matches:** file_cluster_6: 6.849, file_cluster_8: 11.683, file_cluster_4: 13.861
- **Magnitude:** 1601.62 | **LOC:** 1280 | **CtrlFlow:** 40.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **2**; blast radius 0.171; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.1%), Guard Balance (formerly Safety Score) (82.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.0%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doParse` **(Many-Argument Workhorses)** (Impact: 280.3)
  * `parseValue` **(Many-Argument Workhorses)** (Impact: 91.5)
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
* *Structure:* `branch: 371`, `structural_boundaries: 149`, `args: 29`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 307`
* *Architecture:* `io: 1`, `api: 7`, `import: 3`
* *Defense:* `safety: 57`, `doc: 12`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.171
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.018198
  * `Imports (Out-Degree: 3):` Symfony\Component\Yaml\Exception\ParseException, Symfony\Component\Yaml\Tag\TaggedValue
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.152)
- **Top Global Matches:** file_cluster_4: 6.152, file_cluster_6: 10.557, file_cluster_15: 11.595
- **Magnitude:** 1544.12 | **LOC:** 1837 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **423** in-repo importer(s); it depends on **40**; blast radius 6.449; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (77.4%), Guard Balance (formerly Safety Score) (65.1%), Complexity Load (formerly Cognitive Load) (48.1%)
- **Documentation Coverage:** 7.7922% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createService` **(Many-Argument Workhorses)** (Impact: 182.1)
    * *Intent:* /** * Creates a service for a service definition. * * @throws RuntimeException When the factory defi...
  * `doResolveServices` **(Defensive Guards)** (Impact: 57.2)
  * `resolveEnvPlaceholders` **(Many-Argument Workhorses)** (Impact: 50.9)
    * *Intent:* /** * Resolves env parameter placeholders in a string or an array. * * @param string|true|null $form...
  * `addResource` **(Defensive Guards)** (Impact: 44.7)
    * *Intent:* /** * @return $this */
  * `doGet` **(Many-Argument Workhorses)** (Impact: 41.0)
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
* *Structure:* `branch: 363`, `structural_boundaries: 340`, `args: 84`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 228`
* *Architecture:* `api: 68`, `concurrency: 1`, `import: 41`
* *Defense:* `safety: 119`, `doc: 81`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.449
  * `Choke Point (Betweenness):` 0.001731 | `Ripple Effect (Closeness):` 0.030231
  * `Imports (Out-Degree: 39):` $parameterBag->resolveValue($definition->getFile(), Composer\Autoload\ClassLoader, Composer\InstalledVersions, Symfony\Component\Config\Resource\ClassExistenceResource, Symfony\Component\Config\Resource\ComposerResource, Symfony\Component\Config\Resource\DirectoryResource, Symfony\Component\Config\Resource\FileExistenceResource, Symfony\Component\Config\Resource\FileResource...
  * `Imported By (In-Degree: 423):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Validator/Constraints/Image.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.524)
- **Top Global Matches:** file_cluster_2: 5.524, file_cluster_17: 6.073, file_cluster_15: 6.792
- **Magnitude:** 1409.77 | **LOC:** 243 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 0.063; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.3%), Connectivity (formerly Api Exposure) (84.8%), Complexity Load (formerly Cognitive Load) (80.5%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000807
  * `Imports (Out-Degree: 1):` Symfony\Component\Validator\Exception\InvalidArgumentException
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/JsonPath/JsonCrawler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.753)
- **Top Global Matches:** file_cluster_6: 7.753, file_cluster_8: 9.813, file_cluster_4: 15.66
- **Magnitude:** 1384.24 | **LOC:** 1174 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **11**; blast radius 0.186; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.7%), Guard Balance (formerly Safety Score) (77.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.9%)
- **Documentation Coverage:** 45.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateBracket` **(Many-Argument Workhorses)** (Impact: 189.6)
  * `evaluateFunction` **(Defensive Guards)** (Impact: 77.8)
  * `compareEquality` **(Stateful Encapsulated Methods)** (Impact: 49.1)
  * `evaluateScalar` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `evaluateFilterExpression` **(Many-Argument Workhorses)** (Impact: 45.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 214 instances
* *State Mutation (weighted view):* 647
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 363`, `structural_boundaries: 216`, `args: 32`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 219`, `dead_code: 2`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 57`, `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.186
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000886
  * `Imports (Out-Degree: 13):` Psr\Container\ContainerInterface, Symfony\Component\JsonPath\Exception\InvalidArgumentException, Symfony\Component\JsonPath\Exception\InvalidJsonPathException, Symfony\Component\JsonPath\Exception\InvalidJsonStringInputException, Symfony\Component\JsonPath\Exception\JsonCrawlerException, Symfony\Component\JsonPath\Tokenizer\JsonPathToken, Symfony\Component\JsonPath\Tokenizer\JsonPathTokenizer, Symfony\Component\JsonPath\Tokenizer\TokenType...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Serializer/Normalizer/AbstractObjectNormalizer.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.137)
- **Top Global Matches:** file_cluster_6: 8.137, file_cluster_8: 11.546, file_cluster_4: 15.172
- **Magnitude:** 1346.12 | **LOC:** 975 | **CtrlFlow:** 44.3% | **Authorship Centralization:** 36.4%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **34**; blast radius 0.187; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.6%), Complexity Load (formerly Cognitive Load) (63.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.5%)
- **Documentation Coverage:** 44.8276% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateAndDenormalize` **(Many-Argument Workhorses)** (Impact: 285.4)
    * *Intent:* /** * Validates the submitted data and denormalizes it. * * @throws NotNormalizableValueException * ...
  * `denormalize` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `normalize` **(Defensive Guards)** (Impact: 69.9)
  * `denormalizeParameter` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* /** * @internal */
  * `updateData` **(Stateful Encapsulated Methods)** (Impact: 46.2)
    * *Intent:* /** * Sets an attribute and apply the name converter if necessary. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 537
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 145`, `args: 23`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 193`
* *Architecture:* `api: 15`, `import: 34`
* *Defense:* `safety: 129`, `doc: 23`, `immutability_locks: 10`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.187
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.002319
  * `Imports (Out-Degree: 35):` Symfony\Component\PropertyAccess\Exception\InvalidArgumentException, Symfony\Component\PropertyAccess\Exception\InvalidTypeException, Symfony\Component\PropertyAccess\Exception\NoSuchIndexException, Symfony\Component\PropertyAccess\Exception\NoSuchPropertyException, Symfony\Component\PropertyAccess\Exception\UninitializedPropertyException, Symfony\Component\PropertyAccess\PropertyAccess, Symfony\Component\PropertyInfo\PropertyTypeExtractorInterface, Symfony\Component\Serializer\Encoder\CsvEncoder...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Serializer/Tests/Normalizer/AbstractObjectNormalizerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.84)
- **Top Global Matches:** file_cluster_11: 6.84, file_cluster_15: 7.011, file_cluster_16: 7.322
- **Magnitude:** 1339.6 | **LOC:** 2125 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 11.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **54**; blast radius 0.041; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (46.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.7%)
- **Documentation Coverage:** 94.702% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `denormalize` **(Defensive Guards)** (Impact: 11.7)
  * `testDenormalizeNullCoalescingValues` **(Annotated & Test Methods)** (Impact: 7.8)
  * `testDenormalizeWithNestedDiscriminatorMap` **(Interface Declarations)** (Impact: 7.7)
  * `setAttributeValue` **(Stateful Encapsulated Methods)** (Impact: 7.6)
  * `setAttributeValue` **(Stateful Encapsulated Methods)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 108 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 680`, `args: 167`, `func_start: 166`, `class_start: 46`
* *Risk/State:* `state_mutation: 355`, `duplicate_logic: 41`, `unreferenced_by_name: 77`
* *Architecture:* `api: 202`, `concurrency: 6`, `import: 54`
* *Defense:* `safety: 17`, `doc: 31`, `test: 86`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 53):` PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\TestCase, Symfony\Component\PropertyAccess\PropertyAccess, Symfony\Component\PropertyAccess\PropertyPath, Symfony\Component\PropertyInfo\Extractor\PhpDocExtractor, Symfony\Component\PropertyInfo\Extractor\PhpStanExtractor, Symfony\Component\PropertyInfo\Extractor\ReflectionExtractor, Symfony\Component\PropertyInfo\PropertyInfoExtractor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/HttpClient/HttpClientTrait.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.671)
- **Top Global Matches:** file_cluster_8: 11.671, file_cluster_3: 13.881, file_cluster_6: 23.859
- **Magnitude:** 1295.82 | **LOC:** 866 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **5**; blast radius 0.22; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (73.6%), Concurrency Surface (formerly Concurrency) (63.1%)
- **Documentation Coverage:** 10.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareRequest` **(Many-Argument Workhorses)** (Impact: 156.9)
    * *Intent:* /** * Validates and normalizes method, URL and options, and merges them with defaults. * * @throws I...
  * `normalizeBody` **(Many-Argument Workhorses)** (Impact: 126.4)
    * *Intent:* /** * @param array|string|resource|\Traversable|\Closure $body * * @return string|resource|\Closure ...
  * `mergeDefaultOptions` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* /** * @throws InvalidArgumentException When an invalid option is found */
  * `parseUrl` **(Defensive Guards)** (Impact: 77.7)
    * *Intent:* /** * Parses a URL and fixes its encoding if needed. * * @throws InvalidArgumentException When an in...
  * `resolveUrl` **(Many-Argument Workhorses)** (Impact: 67.2)
    * *Intent:* /** * Resolves a URL against a base URI. * * @see https://tools.ietf.org/html/rfc3986#section-5.2.2 ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 195 instances
* *Concurrency (weighted view):* 18
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 593
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 126`, `args: 23`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 203`
* *Architecture:* `io: 7`, `api: 4`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 105`, `doc: 12`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.22
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.011051
  * `Imports (Out-Degree: 5):` Symfony\Component\HttpClient\Exception\InvalidArgumentException, Symfony\Component\HttpClient\Exception\TransportException, Symfony\Component\HttpClient\Response\StreamWrapper, Symfony\Component\HttpClient\Response\StreamableInterface, Symfony\Component\Mime\MimeTypes
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Console/Application.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.131)
- **Top Global Matches:** file_cluster_4: 7.131, file_cluster_6: 8.068, file_cluster_12: 13.996
- **Magnitude:** 1276.4 | **LOC:** 1422 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 18.2%
- **Blast Radius:** changing it is visible to **62** in-repo importer(s); it depends on **46**; blast radius 0.833; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.1%), Connectivity (formerly Api Exposure) (52.5%), Complexity Load (formerly Cognitive Load) (52.2%)
- **Documentation Coverage:** 12.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 59.9)
    * *Intent:* /** * Runs the current application. * * @return int 0 if everything went fine, or an error code * * ...
  * `doRenderThrowable` **(Defensive Guards)** (Impact: 59.0)
  * `doRunCommand` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* /** * Runs the current command. * * If an event dispatcher has been attached to the application, * e...
  * `find` **(Compute Cores)** (Impact: 45.3)
    * *Intent:* /** * Finds a command by name or alias. * * Contrary to get, this command tries to find the best * m...
  * `doRun` **(Defensive Guards)** (Impact: 39.7)
    * *Intent:* /** * Runs the current application. * * @return int 0 if everything went fine, or an error code */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 213 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 47
* *State Mutation (weighted view):* 660
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 258`, `args: 69`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 234`
* *Architecture:* `api: 43`, `import: 46`
* *Defense:* `safety: 80`, `doc: 43`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.833
  * `Choke Point (Betweenness):` 0.001111 | `Ripple Effect (Closeness):` 0.016535
  * `Imports (Out-Degree: 46):` Psr\Container\ContainerInterface, Symfony\Component\Console\ArgumentResolver\ArgumentResolverInterface, Symfony\Component\Console\CommandLoader\CommandLoaderInterface, Symfony\Component\Console\Command\Command, Symfony\Component\Console\Command\CompleteCommand, Symfony\Component\Console\Command\DumpCompletionCommand, Symfony\Component\Console\Command\HelpCommand, Symfony\Component\Console\Command\LazyCommand...
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.383)
- **Top Global Matches:** file_cluster_11: 7.383, file_cluster_12: 8.185, file_cluster_16: 8.525
- **Magnitude:** 1256.98 | **LOC:** 3160 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 30.4%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **108**; blast radius 0.465; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.7%), Complexity Load (formerly Cognitive Load) (52.7%), Guard Balance (formerly Safety Score) (49.4%)
- **Documentation Coverage:** 99.458% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContainerFromFile` **(Stateful Encapsulated Methods)** (Impact: 18.4)
  * `assertCachePoolServiceDefinitionIsCreated` **(Stateful Encapsulated Methods)** (Impact: 12.7)
  * `testWorkflows` **(I/O & Config Routines)** (Impact: 10.9)
  * `testSerializerMapping` **(Defensive Guards)** (Impact: 8.5)
  * `assertTransition` **(Stateful Encapsulated Methods)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 600
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 480`, `args: 200`, `func_start: 187`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 474`
* *Architecture:* `api: 176`, `concurrency: 2`, `import: 109`
* *Defense:* `safety: 27`, `doc: 4`, `test: 610`, `sync_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.465
  * `Choke Point (Betweenness):` 0.000134 | `Ripple Effect (Closeness):` 0.000999
  * `Imports (Out-Degree: 100):` PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group, PHPUnit\Framework\Attributes\IgnoreDeprecations, PHPUnit\Framework\Attributes\RequiresMethod, Psr\Cache\CacheItemPoolInterface, Psr\Log\LogLevel, Symfony\Bundle\FrameworkBundle\DependencyInjection\FrameworkExtension, Symfony\Bundle\FrameworkBundle\FrameworkBundle...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RelayProxy.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.91)
- **Top Global Matches:** file_cluster_15: 10.91, file_cluster_11: 11.4, file_cluster_16: 12.112
- **Magnitude:** 1239.06 | **LOC:** 1755 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 0.059; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.4%), Mutation Surface (formerly State Flux) (81.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.059
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000154
  * `Imports (Out-Degree: 4):` RedisProxyTrait 
        resetLazyObject, Relay20Trait, Relay21Trait, Symfony\Component\Cache\Traits\Relay\Relay20Trait, Symfony\Component\Cache\Traits\Relay\Relay21Trait, Symfony\Component\VarExporter\LazyObjectInterface, Symfony\Contracts\Service\ResetInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/http_client.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_13: 6.134, file_cluster_2: 6.801, file_cluster_17: 7.638
- **Magnitude:** 1204.04 | **LOC:** 175 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.7%), Complexity Load (formerly Cognitive Load) (10.2%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 30`, `args: 12`, `func_start: 1`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`
* *Architecture:* `io: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Console/Tests/ApplicationTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.773)
- **Top Global Matches:** file_cluster_11: 8.773, file_cluster_15: 9.212, file_cluster_10: 9.327
- **Magnitude:** 1191.22 | **LOC:** 3250 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **73**; blast radius 0.041; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (52.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.8%), Complexity Load (formerly Cognitive Load) (40.7%)
- **Documentation Coverage:** 98.2051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runRestoresSttyTest` **(Many-Argument Workhorses)** (Impact: 18.4)
  * `execute` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `testAlarmSubscriberCalledAfterSignalSubscriberAndInheritsExitCode` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `execute` **(Stateful Encapsulated Methods)** (Impact: 5.8)
  * `createSignalableApplication` **(Stateful Encapsulated Methods)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 343
* *State Mutation (weighted view):* 513
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 959`, `args: 273`, `func_start: 201`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 463`, `dead_code: 2`, `duplicate_logic: 12`, `unreferenced_by_name: 153`
* *Architecture:* `io: 2`, `api: 197`, `concurrency: 3`, `import: 75`
* *Defense:* `safety: 76`, `doc: 5`, `test: 224`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 67):` PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\Group, PHPUnit\Framework\Attributes\RequiresPhpExtension, PHPUnit\Framework\Attributes\TestWith, PHPUnit\Framework\TestCase, Psr\Container\ContainerInterface, SignalableInvokableCommandTrait, Symfony\Component\Console\Application...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/messenger.html.twig` (HTML | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.6)
- **Top Global Matches:** file_cluster_12: 7.6, file_cluster_13: 8.078, file_cluster_7: 8.181
- **Magnitude:** 1138.26 | **LOC:** 220 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.3%), Complexity Load (formerly Cognitive Load) (8.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.8%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 32`, `args: 16`, `func_start: 1`, `class_start: 40`
* *Risk/State:* `safety_bypasses: 4`
* *Architecture:* `io: 2`, `api: 4`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Symfony/Component/Yaml/Inline.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.742)
- **Top Global Matches:** file_cluster_8: 7.742, file_cluster_3: 18.317, file_cluster_6: 18.924
- **Magnitude:** 1128.22 | **LOC:** 881 | **CtrlFlow:** 42.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 0.135; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (66.9%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (17.0%)
- **Documentation Coverage:** 15.2174% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evaluateScalar` **(Many-Argument Workhorses)** (Impact: 152.8)
    * *Intent:* /** * Evaluates scalars and replaces magic values. * * @throws ParseException when object parsing su...
  * `parseMapping` **(Many-Argument Workhorses)** (Impact: 141.1)
    * *Intent:* /** * Parses a YAML mapping. * * @throws ParseException When malformed inline YAML string is parsed ...
  * `dump` **(Many-Argument Workhorses)** (Impact: 88.6)
    * *Intent:* /** * Dumps a given PHP variable to a YAML string. * * @param mixed $value The PHP variable to conve...
  * `parseSequence` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* /** * Parses a YAML sequence. * * @throws ParseException When malformed inline YAML string is parsed...
  * `parseScalar` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* /** * Parses a YAML scalar. * * @throws ParseException When malformed inline YAML string is parsed *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 153 instances
* *State Mutation (weighted view):* 468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 157`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 162`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 31`, `doc: 13`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.135
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.015668
  * `Imports (Out-Degree: 6):` Symfony\Component\Yaml\Exception\DumpException, Symfony\Component\Yaml\Exception\ParseException, Symfony\Component\Yaml\Tag\TaggedValue
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/Cache/Traits/RedisTrait.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.124)
- **Top Global Matches:** file_cluster_8: 7.124, file_cluster_6: 14.889, file_cluster_3: 23.27
- **Magnitude:** 1087.28 | **LOC:** 827 | **CtrlFlow:** 42.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 0.24; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (93.7%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (70.4%), Concurrency Surface (formerly Concurrency) (49.1%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createConnection` **(Many-Argument Workhorses)** (Impact: 319.7)
    * *Intent:* /** * Creates a Redis connection using a DSN configuration. * * Example DSN: * - redis://localhost *...
  * `doClear` **(Defensive Guards)** (Impact: 67.2)
  * `pipeline` **(Defensive Guards)** (Impact: 56.8)
  * `doFetch` **(Stateful Encapsulated Methods)** (Impact: 18.6)
  * `doDelete` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 171 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 523
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 146`, `args: 21`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 3`, `state_mutation: 181`
* *Architecture:* `api: 6`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 117`, `doc: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.24
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001252
  * `Imports (Out-Degree: 6):` Predis\Command\Redis\UNLINK, Predis\Connection\Aggregate\ClusterInterface, Predis\Connection\Aggregate\RedisCluster, Predis\Connection\Aggregate\ReplicationInterface, Predis\Connection\Cluster\ClusterInterface, Predis\Connection\Cluster\RedisCluster, Predis\Connection\Replication\ReplicationInterface, Predis\Response\ErrorInterface...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Symfony/Component/HttpFoundation/Tests/RequestTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.137)
- **Top Global Matches:** file_cluster_11: 7.137, file_cluster_15: 7.902, file_cluster_13: 7.924
- **Magnitude:** 1038.0 | **LOC:** 3011 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.041; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (53.4%), Guard Balance (formerly Safety Score) (48.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testHostValidity` **(Many-Argument Workhorses)** (Impact: 12.1)
  * `getRequestInstanceForClientIpsForwardedTests` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `getRequestInstanceForClientIpTests` **(Stateful Encapsulated Methods)** (Impact: 10.8)
  * `testPreferredLanguageWithLocales` **(Annotated & Test Methods)** (Impact: 8.4)
  * `providePreferredFormatRfc9110` **(I/O & Config Routines)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 25 instances
* *Concurrency (weighted view):* 125
* *Memory Alloc (weighted view):* 101
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 416`, `args: 146`, `func_start: 143`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 331`, `unreferenced_by_name: 110`
* *Architecture:* `io: 21`, `api: 139`, `concurrency: 80`, `import: 13`
* *Defense:* `safety: 19`, `test: 452`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` PHPUnit\Framework\Attributes\DataProvider, PHPUnit\Framework\Attributes\RequiresPhpExtension, PHPUnit\Framework\Attributes\TestWith, PHPUnit\Framework\TestCase, Symfony\Component\HttpFoundation\Exception\BadRequestException, Symfony\Component\HttpFoundation\Exception\ConflictingHeadersException, Symfony\Component\HttpFoundation\Exception\JsonException, Symfony\Component\HttpFoundation\Exception\SuspiciousOperationException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/Symfony/Component/Validator/Tests/Constraints/Fixtures/WhenTestWithClosure.php` (PHP) | Magnitude: 0.02 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 9, import: 4, memory_alloc: 3
- `src/Symfony/Component/Security/Http/Tests/Firewall/SwitchUserListenerTest.php` (PHP) | Magnitude: 130.26 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 114, state_mutation: 67, memory_alloc: 65
- `src/Symfony/Component/DependencyInjection/Tests/Exception/AutowiringFailedExceptionTest.php` (PHP) | Magnitude: 10.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, test: 8, state_mutation: 4
- `src/Symfony/Component/Console/Tests/Fixtures/application_sttyhelper.php` (PHP) | Magnitude: 0.02 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 18, import: 8, memory_alloc: 6
- `src/Symfony/Component/HttpKernel/Tests/EventListener/CacheAttributeListenerTest.php` (PHP) | Magnitude: 236.56 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 465, structural_boundaries: 164, state_mutation: 83, memory_alloc: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Symfony/Bundle/FrameworkBundle/Tests/Functional/SchedulerTest.php` (PHP) | Magnitude: 55.16 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 42, state_mutation: 25, test: 20
- `src/Symfony/Component/DependencyInjection/Tests/Fixtures/php/services_subscriber.php` (PHP) | Magnitude: 0.03 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 30, state_mutation: 9, args: 8
- `src/Symfony/Component/CssSelector/Tests/Parser/Shortcut/ElementParserTest.php` (PHP) | Magnitude: 9.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 11, test: 5, import: 4
- `src/Symfony/Component/Asset/Tests/VersionStrategy/JsonManifestVersionStrategyTest.php` (PHP) | Magnitude: 60.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 45, args: 15, func_start: 14
- `src/Symfony/Component/HttpKernel/Tests/EventListener/DisallowRobotsIndexingListenerTest.php` (PHP) | Magnitude: 17.1 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 19, indent_spaces: 17, import: 8, test: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Symfony/Component/JsonStreamer/Tests/JsonStreamReaderTest.php` (PHP) | Magnitude: 82.04 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 191, structural_boundaries: 78, args: 34, test: 31
- `src/Symfony/Component/HttpKernel/Event/ControllerEvent.php` (PHP) | Magnitude: 139.76 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 94, branch: 37, structural_boundaries: 33, state_mutation: 18
- `src/Symfony/Component/VarDumper/Dumper/HtmlDumper.php` (PHP) | Magnitude: 794.48 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 819, state_mutation: 205, branch: 148, structural_boundaries: 113
- `src/Symfony/Component/Config/Tests/ConfigCacheTest.php` (PHP) | Magnitude: 40.46 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 72, structural_boundaries: 32, state_mutation: 14, memory_alloc: 10
- `src/Symfony/Component/Config/Tests/Definition/ArrayShapeGeneratorTest.php` (PHP) | Magnitude: 104.74 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 104, memory_alloc: 46, concurrency: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Symfony/Component/Serializer/Tests/Context/Normalizer/FormErrorNormalizerContextBuilderTest.php` (PHP) | Magnitude: 11.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, test: 5, import: 4
- `src/Symfony/Component/Serializer/Tests/Context/Normalizer/ProblemNormalizerContextBuilderTest.php` (PHP) | Magnitude: 11.64 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, test: 5, import: 4
- `src/Symfony/Component/HttpFoundation/Tests/RequestMatcher/HostRequestMatcherTest.php` (PHP) | Magnitude: 8.28 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 11, test: 6, import: 4
- `src/Symfony/Component/Security/Http/Tests/Authenticator/FormLoginAuthenticatorTest.php` (PHP) | Magnitude: 100.8 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 190, structural_boundaries: 88, memory_alloc: 34, state_mutation: 28
- `src/Symfony/Bundle/FrameworkBundle/Tests/Fixtures/JsonPath/UppercaseFunction.php` (PHP) | Magnitude: 0.01 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, branch: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/Symfony/Component/Notifier/Bridge/SmsBiuras/Tests/SmsBiurasTransportFactoryTest.php` (PHP) | Magnitude: 23.5 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 26, safety_bypasses: 9, concurrency: 9
- `src/Symfony/Component/Notifier/Bridge/LightSms/Tests/LightSmsTransportFactoryTest.php` (PHP) | Magnitude: 18.9 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 21, safety_bypasses: 7, concurrency: 7
- `src/Symfony/Component/Security/Http/Tests/Authenticator/X509AuthenticatorTest.php` (PHP) | Magnitude: 76.84 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 53, safety_bypasses: 24, state_mutation: 19
- `src/Symfony/Component/Notifier/Bridge/Sipgate/Tests/SipgateTransportFactoryTest.php` (PHP) | Magnitude: 18.9 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 21, safety_bypasses: 7, concurrency: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Symfony/Component/Security/Http/Authenticator/AbstractPreAuthenticatedAuthenticator.php` (PHP) | Magnitude: 59.54 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 40, branch: 15, import: 13
- `src/Symfony/Component/VarExporter/Internal/Reference.php` (PHP) | Magnitude: 8.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 6, api: 4, structural_boundaries: 3, safety: 2
- `src/Symfony/Component/Console/ArgumentResolver/ValueResolver/TraceableValueResolver.php` (PHP) | Magnitude: 13.9 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 9, import: 3, args: 2
- `src/Symfony/Component/AssetMapper/ImportMap/ImportMapEntries.php` (PHP) | Magnitude: 26.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 15, args: 6, func_start: 6
- `src/Symfony/Component/RateLimiter/Exception/ReserveNotSupportedException.php` (PHP) | Magnitude: 11.38 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 4, indent_spaces: 4, safety: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Symfony/Component/JsonStreamer/ValueTransformer/StringToDateTimeValueTransformer.php` (PHP) | Magnitude: 37.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 21, state_mutation: 7, branch: 6
- `src/Symfony/Component/HttpFoundation/Test/Constraint/ResponseIsUnprocessable.php` (PHP) | Magnitude: 15.52 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, args: 5, func_start: 5
- `src/Symfony/Bridge/Monolog/Command/ServerLogCommand.php` (PHP) | Magnitude: 88.3 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 38, branch: 19, import: 16
- `src/Symfony/Component/HttpFoundation/Test/Constraint/ResponseIsRedirected.php` (PHP) | Magnitude: 15.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, args: 5, func_start: 5
- `src/Symfony/Component/HttpFoundation/Test/Constraint/ResponseIsSuccessful.php` (PHP) | Magnitude: 15.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 14, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Symfony/Component/Console/Input/InputInterface.php` (PHP) | Magnitude: 115.42 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 20, doc: 17, args: 16, func_start: 16
- `src/Symfony/Component/HttpClient/Response/StreamableInterface.php` (PHP) | Magnitude: 21.34 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, safety: 4, import: 4, doc: 2
- `src/Symfony/Bundle/FrameworkBundle/Resources/config/services.php` (PHP) | Magnitude: 17.6 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 37, import: 26, ssr_boundaries: 8
- `src/Symfony/Bundle/SecurityBundle/Resources/config/password_hasher.php` (PHP) | Magnitude: 15.74 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, import: 9, args: 1
- `src/Symfony/Bundle/FrameworkBundle/Resources/config/type_info.php` (PHP) | Magnitude: 15.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 10, import: 7, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Symfony/Component/Mime/Encoder/Base64Encoder.php` (PHP) | Magnitude: 37.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 8, structural_boundaries: 5, branch: 4
- `src/Symfony/Bundle/TwigBundle/Resources/config/twig.php` (PHP) | Magnitude: 18.04 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 54, import: 42, dependency_injection: 3
- `src/Symfony/Component/Serializer/SerializerInterface.php` (PHP) | Magnitude: 26.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, safety: 3, doc: 3, import: 3
- `src/Symfony/Component/DependencyInjection/ParameterBag/ContainerBagInterface.php` (PHP) | Magnitude: 32.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 9, doc: 5, args: 4, func_start: 4
- `src/Symfony/Component/Cache/Tests/Adapter/PredisReplicationAdapterTest.php` (PHP) | Magnitude: 28.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, state_mutation: 8, structural_boundaries: 7, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Symfony/Bundle/FrameworkBundle/Console/Descriptor/Descriptor.php` (PHP) | Magnitude: 422.08 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 284, structural_boundaries: 102, branch: 84, state_mutation: 80
- `src/Symfony/Component/Form/Extension/Core/Type/DateType.php` (PHP) | Magnitude: 288.9 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 292, structural_boundaries: 75, state_mutation: 63, branch: 56

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/Symfony/Component/HttpFoundation/IpUtils.php` (PHP) | Magnitude: 217.12 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 161, branch: 44, state_mutation: 40, structural_boundaries: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Symfony/Component/HttpKernel/Tests/CacheClearer/ChainCacheClearerTest.php` (PHP) | Magnitude: 10.42 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, test: 4, args: 3
- `src/Symfony/Component/Notifier/Bridge/FreeMobile/Tests/FreeMobileTransportFactoryTest.php` (PHP) | Magnitude: 22.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 25, safety_bypasses: 8, concurrency: 8
- `src/Symfony/Component/Notifier/Bridge/Sinch/Tests/SinchTransportFactoryTest.php` (PHP) | Magnitude: 22.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 25, safety_bypasses: 8, concurrency: 8
- `src/Symfony/Component/Notifier/Bridge/Twilio/Tests/TwilioTransportFactoryTest.php` (PHP) | Magnitude: 22.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 25, safety_bypasses: 8, concurrency: 8
- `src/Symfony/Component/Notifier/Bridge/Vonage/Tests/VonageTransportFactoryTest.php` (PHP) | Magnitude: 22.22 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 25, safety_bypasses: 8, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Symfony/Component/Console/Input/StringInput.php` (PHP) | Magnitude: 66.52 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 40, state_mutation: 14, branch: 11, structural_boundaries: 8
- `src/Symfony/Bridge/PhpUnit/Extension/EnableClockMockSubscriber.php` (PHP) | Magnitude: 18.04 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 14, import: 7, branch: 6
- `src/Symfony/Component/Notifier/Bridge/Ntfy/NtfyTransportFactory.php` (PHP) | Magnitude: 39.74 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, state_mutation: 8, branch: 7
- `src/Symfony/Component/Mailer/Bridge/Postmark/Transport/PostmarkTransportFactory.php` (PHP) | Magnitude: 39.7 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 14, state_mutation: 8, branch: 7
- `src/Symfony/Component/Messenger/Middleware/DecodeFailedMessageMiddleware.php` (PHP) | Magnitude: 36.58 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, safety: 9, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Symfony/Component/HttpKernel/Kernel.php` -> Churn: **100.0%** | Cog Load: 70.0094% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/DependencyInjection/FrameworkExtension.php` -> Churn: **88.49%** | Cog Load: 67.1999% | Debt: 0.0%
- `src/Symfony/Bundle/FrameworkBundle/Tests/DependencyInjection/FrameworkExtensionTestCase.php` -> Churn: **71.73%** | Cog Load: 52.7406% | Debt: 0.0%
- `src/Symfony/Component/ObjectMapper/ObjectMapper.php` -> Churn: **62.58%** | Cog Load: 69.9313% | Debt: 0.0%
- `src/Symfony/Component/ObjectMapper/Tests/ObjectMapperTest.php` -> Churn: **52.54%** | Cog Load: 94.2245% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/config.html.twig` -> **Antoine M** (100.0% isolated ownership) | Magnitude: 2478.02
- `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/serializer.html.twig` -> **Javier Eguiluz** (100.0% isolated ownership) | Magnitude: 2192.23
- `src/Symfony/Component/Yaml/Parser.php` -> **Younes ENNAJI** (100.0% isolated ownership) | Magnitude: 1601.62
- `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` -> **Dariusz Ruminski** (100.0% isolated ownership) | Magnitude: 1544.12
- `src/Symfony/Bundle/WebProfilerBundle/Resources/views/Collector/messenger.html.twig` -> **Javier Eguiluz** (100.0% isolated ownership) | Magnitude: 1138.26

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Symfony/Component/DependencyInjection/ContainerBuilder.php` -> **Severity: 0.173** (Bridge: 0.0017 * Flux: 100.0%)
- `src/Symfony/Component/Console/Application.php` -> **Severity: 0.111** (Bridge: 0.0011 * Flux: 100.0%)
- `src/Symfony/Component/DependencyInjection/Compiler/PassConfig.php` -> **Severity: 0.107** (Bridge: 0.0011 * Flux: 100.0%)
- `src/Symfony/Component/DependencyInjection/Loader/Configurator/ContainerConfigurator.php` -> **Severity: 0.093** (Bridge: 0.0009 * Flux: 100.0%)
- `src/Symfony/Component/Console/Command/Command.php` -> **Severity: 0.075** (Bridge: 0.0008 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Symfony/Component/DependencyInjection/Exception/ParameterNotFoundException.php` -> **Severity: 3.111** (Embedded: 0.0414 * Error Risk: 75.2093%)
- `src/Symfony/Component/DependencyInjection/Exception/ServiceNotFoundException.php` -> **Severity: 2.803** (Embedded: 0.0414 * Error Risk: 67.6371%)
- `src/Symfony/Component/VarDumper/Cloner/Stub.php` -> **Severity: 2.78** (Embedded: 0.0368 * Error Risk: 75.6102%)
- `src/Symfony/Component/HttpFoundation/Request.php` -> **Severity: 2.777** (Embedded: 0.0362 * Error Risk: 76.6945%)
- `src/Symfony/Contracts/Deprecation/function.php` -> **Severity: 2.753** (Embedded: 0.0533 * Error Risk: 51.6779%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Symfony/Component/Validator/Exception/InvalidOptionsException.php` -> **Severity: 267.9** (Blast Radius: 2.679 * Doc Risk: 100.0%)
- `src/Symfony/Component/Notifier/Transport/Dsn.php` -> **Severity: 262.6** (Blast Radius: 2.626 * Doc Risk: 100.0%)
- `src/Symfony/Component/ErrorHandler/Tests/HeaderMock.php` -> **Severity: 199.4** (Blast Radius: 1.994 * Doc Risk: 100.0%)
- `src/Symfony/Component/RemoteEvent/Event/Mailer/MailerDeliveryEvent.php` -> **Severity: 199.0** (Blast Radius: 1.99 * Doc Risk: 100.0%)
- `src/Symfony/Component/DependencyInjection/Exception/ParameterNotFoundException.php` -> **Severity: 158.67** (Blast Radius: 1.763 * Doc Risk: 90.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2351 literal sites + 8 sites through wrappers = 2359
- **`panics_and_aborts`:** 6414 literal sites + 4 sites through wrappers = 6418

- `bailout` (function, debug_prints, primitive): 3 call sites in 1 files -- `src/Symfony/Component/Intl/Resources/bin/common.php`
- `bailout` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `src/Symfony/Component/Intl/Resources/bin/common.php`
- `textColorRed` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/Symfony/Component/Translation/Resources/bin/translation-status.php`
- `getController` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/Symfony/Component/HttpKernel/Tests/Controller/TraceableControllerResolverTest.php`
- `printTitle` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/Symfony/Component/Translation/Resources/bin/translation-status.php`
- `textColorGreen` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/Symfony/Component/Translation/Resources/bin/translation-status.php`
- `textColorNormal` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/Symfony/Component/Translation/Resources/bin/translation-status.php`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 194572 call pairs -- scoped 44.9%, unique 0.9%, ambiguous 21.9%, external 32.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 194104 | 44.9% | 0.9% | 21.9% | 32.3% |
| html | 280 | 10.4% | 0.0% | 0.0% | 89.6% |
| javascript | 157 | 38.9% | 0.0% | 3.2% | 58.0% |
| shell | 31 | 0.0% | 0.0% | 0.0% | 100.0% |

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
