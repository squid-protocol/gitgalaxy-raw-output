# ARCHITECTURAL_BRIEF: yii2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/yiisoft/yii2.git` |
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
- **Scope:** 1048 analyzed artifact(s), 124898 LOC.
- **Load-bearing artifact:** `framework/Yii.php` -- 246 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/framework/db/ActiveRecordTest.php` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `framework/helpers/BaseHtml.php` at magnitude 1643.58 (structural weight, not risk).
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
| Total Artifacts | 2426 |
| Analyzed Artifacts (Scanned) | 1048 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1378 |
| Total LOC | 124898 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 43.2% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4861 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1102 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4377 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 72 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 955 | 115302 | 91.1% |
| YAML | 21 | 1025 | 2.0% |
| MARKDOWN | 16 | 0 | 1.5% |
| POSTGRESQL | 16 | 692 | 1.5% |
| JAVASCRIPT | 11 | 5461 | 1.0% |
| DB2_SQL | 7 | 1652 | 0.7% |
| SQLITE | 6 | 112 | 0.6% |
| PLAINTEXT | 4 | 0 | 0.4% |
| XML | 3 | 0 | 0.3% |
| HTML | 3 | 375 | 0.3% |
| JSON | 2 | 220 | 0.2% |
| DOCKERFILE | 1 | 7 | 0.1% |
| BATCH | 1 | 6 | 0.1% |
| CSS | 1 | 0 | 0.1% |
| SHELL | 1 | 46 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1048 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 17%, Interface Declarations Files 17%, Large Core Modules (3) 14%, Parameter Forwarders Files 12%, Declarative / Non-Code 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1028 | 98.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 1.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1378*

**Composition by Extension & Reason:**
- `.md`: 850x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3209 LOC)
- `.png`: 261x Excluded (Explicitly Denied Extension: '.png')
- `.graphml`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.php`: 53x Excluded (Machine-Generated Source Code Signature: 149 LOC), 35x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 431 LOC)
- `.json`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Unsupported Format (.undeterminable)
- `.xml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sql`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 4x Excluded (Unsupported Extension: '.neon')
- `.vsd`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xlsx`: 3x Excluded (Explicitly Denied Extension: '.xlsx')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 2x Excluded (Unsupported Extension: '.dist')
- `.bat`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 61.6 | 11.4 | 3.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.4 | 45.2 | 51.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.8 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 65.8 | 5.7 | 5.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 31.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 33.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 23.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4206 | 484 | 11 | `tests/framework/db/sqlite/SqlTokenizerTest.php` |
| cleanup | 506 | 119 | 1 | `tests/data/oci.sql` |
| guards | 5867 | 632 | 15 | `tests/data/mssql.sql` |
| danger | 2398 | 374 | 4 | `tests/framework/db/mssql/QueryBuilderTest.php` |
| concurrency | 130 | 27 | 0 | `framework/db/BaseActiveRecord.php` |
| connectivity | 7845 | 850 | 21 | `tests/framework/helpers/HtmlTest.php` |
| io | 568 | 123 | 1 | `tests/js/data/yii.html` |
| crypto | 0 | 0 | 0 | - |
| ipc | 44 | 24 | 0 | `framework/i18n/Formatter.php` |
| time | 272 | 59 | 0 | `tests/framework/i18n/FormatterDateTest.php` |
| serialization | 104 | 41 | 0 | `tests/framework/rest/SerializerTest.php` |
| regex | 291 | 92 | 0 | `framework/assets/yii.validation.js` |
| events | 252 | 23 | 0 | `tests/framework/base/EventTest.php` |
| tests | 8135 | 265 | 18 | `tests/framework/db/ActiveRecordTest.php` |
| docs | 8410 | 973 | 20 | `tests/framework/ar/ActiveRecordTestTrait.php` |
| debt | 700 | 162 | 1 | `tests/framework/validators/DateValidatorTest.php` |
| mutation | 23110 | 800 | 68 | `framework/helpers/BaseHtml.php` |
| dead_code | 5104 | 730 | 13 | `tests/framework/helpers/HtmlTest.php` |
| credential | 9 | 5 | 0 | `.github/workflows/ci-mssql.yml` |
| threat | 21 | 10 | 0 | `tests/framework/web/RequestTest.php` |
| ml_ai | 67 | 15 | 0 | `tests/framework/db/mysql/connection/DeadLockTest.php` |
| ui | 997 | 123 | 1 | `tests/framework/db/CommandTest.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/js/data/yii.html` (Hits: 71)
- `tests/framework/web/MultipartFormDataParserTest.php` (Hits: 40)
- `tests/framework/db/SchemaTest.php` (Hits: 23)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Yii.php** (`framework/Yii.php`) — 246 inbound connections
2. **TestCase.php** (`tests/TestCase.php`) — 172 inbound connections
3. **InvalidConfigException.php** (`framework/base/InvalidConfigException.php`) — 121 inbound connections
4. **Component.php** (`framework/base/Component.php`) — 54 inbound connections
5. **InvalidArgumentException.php** (`framework/base/InvalidArgumentException.php`) — 54 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ActiveRecordTest.php** (`tests/framework/db/ActiveRecordTest.php`) — 36 outbound dependencies
2. **ContainerTest.php** (`tests/framework/di/ContainerTest.php`) — 31 outbound dependencies
3. **QueryBuilderTest.php** (`tests/framework/db/QueryBuilderTest.php`) — 22 outbound dependencies
4. **DbManagerTestCase.php** (`tests/framework/rbac/DbManagerTestCase.php`) — 17 outbound dependencies
5. **Schema.php** (`framework/db/oci/Schema.php`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseToken` **(Many-Argument Workhorses)** (@ `framework/i18n/MessageFormatter.php`) -> Impact: **97.0** | LOC: 100
  * *Intent:* /** * Parses a token. * @param array $token the token to parse * @param array $args arguments to replace * @param string $locale the locale * @return ...
- `saveMessagesToDb` **(Many-Argument Workhorses)** (@ `framework/console/controllers/MessageController.php`) -> Impact: **94.7** | LOC: 141
  * *Intent:* /** * Saves messages to database. * * @param array $messages * @param Connection $db * @param string $sourceMessageTable * @param string $messageTable...
- `saveMessagesToPO` **(Many-Argument Workhorses)** (@ `framework/console/controllers/MessageController.php`) -> Impact: **77.7** | LOC: 84
  * *Intent:* /** * Writes messages into PO file. * * @param array $messages * @param string $dirName name of the directory to write to * @param bool $overwrite if ...
- `createUrl` **(Many-Argument Workhorses)** (@ `framework/web/UrlRule.php`) -> Impact: **74.2** | LOC: 85
  * *Intent:* /** * Creates a URL according to the given route and parameters. * @param UrlManager $manager the URL manager * @param string $route the route. It sho...
- `resolveCallableDependencies` **(Defensive Guards)** (@ `framework/di/Container.php`) -> Impact: **71.7** | LOC: 83
  * *Intent:* /** * Resolve dependencies for a function. * * This method can be used to implement similar functionality as provided by [[invoke()]] in other * compo...
- `saveMessagesCategoryToPHP` **(Many-Argument Workhorses)** (@ `framework/console/controllers/MessageController.php`) -> Impact: **71.3** | LOC: 69
  * *Intent:* /** * Writes category messages into PHP file. * * @param array $messages * @param string $fileName name of the file to write to * @param bool $overwri...
- `handleAction` **(Many-Argument Workhorses)** (@ `framework/assets/yii.js`) -> Impact: **69.0** | LOC: 132
  * *Intent:* * echo Html::a('submit', ['site/foobar'], [ * 'data' => [ * 'method' => 'post', * 'params' => [ * 'name1' => 'value1', * 'name2' => 'value2', * ], * ]...
- `extractMessagesFromTokens` **(Many-Argument Workhorses)** (@ `framework/console/controllers/MessageController.php`) -> Impact: **67.0** | LOC: 101
  * *Intent:* /** * Extracts messages from a parsed PHP tokens list. * @param array $tokens tokens to be processed. * @param array $translatorTokens translator toke...
- `unlink` **(Many-Argument Workhorses)** (@ `framework/db/BaseActiveRecord.php`) -> Impact: **66.3** | LOC: 87
  * *Intent:* * The model with the foreign key of the relationship will be deleted if `$delete` is `true`. * Otherwise, the foreign key will be set `null` and the m...
- `validate` **(Defensive Guards)** (@ `framework/assets/yii.activeForm.js`) -> Impact: **64.4** | LOC: 129
  * *Intent:* // validate all applicable inputs in the form

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `framework/db` | 47 | 8080.23 | 17.26% | 42.45% |
| `framework/web` | 59 | 6913.11 | 17.33% | 52.16% |
| `framework/helpers` | 31 | 5864.48 | 14.34% | 32.07% |
| `framework/base` | 50 | 3927.7 | 15.01% | 43.75% |
| `tests/framework/db` | 22 | 3717.86 | 10.28% | 0.0% |
| `framework/console/controllers` | 8 | 3250.76 | 35.21% | 41.22% |
| `framework/validators` | 24 | 2891.66 | 30.63% | 62.29% |
| `tests/framework/web` | 29 | 2783.66 | 7.32% | 0.0% |
| `framework/i18n` | 12 | 2695.56 | 22.74% | 40.91% |
| `tests/framework/validators` | 20 | 2626.38 | 9.57% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `framework/caching/ApcCache.php` -> **100.0%** Exposure
- `framework/caching/WinCache.php` -> **100.0%** Exposure
- `framework/db/Migration.php` -> **99.9998%** Exposure
- `framework/db/DataReader.php` -> **99.9997%** Exposure
- `framework/web/SessionHandler.php` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `framework/base/ActionFilter.php` -> **100.0%** Exposure
- `framework/base/ArrayableTrait.php` -> **100.0%** Exposure
- `framework/base/Controller.php` -> **100.0%** Exposure
- `framework/base/DynamicModel.php` -> **100.0%** Exposure
- `framework/base/ErrorException.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/framework/helpers/HtmlTest.php` -> **108** Orphaned Functions | **0** Duplicates
- `tests/framework/db/ActiveRecordTest.php` -> **83** Orphaned Functions | **2** Duplicates
- `tests/framework/helpers/ArrayHelperTest.php` -> **67** Orphaned Functions | **0** Duplicates
- `tests/framework/base/SecurityTest.php` -> **64** Orphaned Functions | **0** Duplicates
- `tests/framework/db/CommandTest.php` -> **51** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `.github/workflows/ci-mssql.yml` -> **100.0%** Exposure
- `tests/data/config-docker.php` -> **99.9571%** Exposure
- `tests/data/config.php` -> **99.9571%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2785` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `framework/helpers/BaseHtml.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.672)
- **Top Global Matches:** file_cluster_4: 6.672, file_cluster_15: 7.186, file_cluster_16: 8.178
- **Magnitude:** 1643.58 | **LOC:** 2412 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderSelectOptions` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* * @param array $items the option data items. The array keys are option values, and the array values ...
  * `checkboxList` **(Many-Argument Workhorses)** (Impact: 38.5)
    * *Intent:* * corresponding to a single item in $items. The signature of this callback must be: * * ``` * functi...
  * `renderTagAttributes` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* * the array will be "expanded" and a list of ARIA/data attributes will be rendered. For example, * `...
  * `radioList` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* * corresponding to a single item in $items. The signature of this callback must be: * * ``` * functi...
  * `beginForm` **(Many-Argument Workhorses)** (Impact: 28.2)
    * *Intent:* * be simulated using "post", and a hidden input will be added which contains the actual method type....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 914
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 210`, `args: 74`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 358`, `unreferenced_by_name: 35`
* *Architecture:* `io: 5`, `api: 71`, `import: 6`
* *Defense:* `safety: 73`, `doc: 81`, `immutability_locks: 1`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Yii, yii\base\InvalidArgumentException, yii\base\Model, yii\db\ActiveRecordInterface, yii\validators\StringValidator, yii\web\Request
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/i18n/Formatter.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 4.706)
- **Top Global Matches:** file_cluster_6: 4.706, file_cluster_4: 10.409, file_cluster_8: 14.035
- **Magnitude:** 1455.26 | **LOC:** 2198 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **16**; blast radius 1.156; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.5%), Debt Markers (formerly Tech Debt) (52.1%), Complexity Load (formerly Cognitive Load) (29.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatDateTimeValue` **(Many-Argument Workhorses)** (Impact: 54.1)
    * *Intent:* /** * @param int|string|DateTime|DateTimeInterface|null $value the value to be formatted. The follow...
  * `asDecimalStringFallback` **(Many-Argument Workhorses)** (Impact: 51.9)
    * *Intent:* /** * Fallback for formatting value as a decimal number. * * Property [[decimalSeparator]] will be u...
  * `formatNumber` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* /** * Given the value in bytes formats number part of the human readable form. * * @param string|int...
  * `asShortSize` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* * This is the short form of [[asSize]]. * * If [[sizeFormatBase]] is 1024, [binary prefixes](https:/...
  * `asSize` **(Many-Argument Workhorses)** (Impact: 42.2)
    * *Intent:* * Formats the value in bytes as a size in human readable form, for example `12 kilobytes`. * * If [[...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 227 instances
* *State Mutation (weighted view):* 709
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 248`, `args: 46`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 255`, `unreferenced_by_name: 28`
* *Architecture:* `api: 57`, `import: 16`
* *Defense:* `safety: 28`, `doc: 79`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.156
  * `Choke Point (Betweenness):` 0.000136 | `Ripple Effect (Closeness):` 0.008071
  * `Imports (Out-Degree: 11):` Closure, DateInterval, DateTime, DateTimeInterface, DateTimeZone, IntlDateFormatter, NumberFormatter, Yii...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `framework/db/BaseActiveRecord.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.574)
- **Top Global Matches:** file_cluster_4: 6.574, file_cluster_15: 7.556, file_cluster_16: 8.352
- **Magnitude:** 1087.18 | **LOC:** 1860 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 1.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.1%), Guard Balance (formerly Safety Score) (68.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unlink` **(Many-Argument Workhorses)** (Impact: 66.3)
    * *Intent:* * The model with the foreign key of the relationship will be deleted if `$delete` is `true`. * Other...
  * `link` **(Many-Argument Workhorses)** (Impact: 57.9)
    * *Intent:* * and **without** events/behaviors. * * If the relationship involves a junction table, a new row wil...
  * `unlinkAll` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* * Destroys the relationship in current model. * * The model with the foreign key of the relationship...
  * `updateInternal` **(Stateful Encapsulated Methods)** (Impact: 16.0)
    * *Intent:* /** * @see update() * @param array|null $attributes attributes to update * @return int|false the num...
  * `getDirtyAttributes` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /** * Returns the attribute values that have been modified since they are loaded or saved most recen...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 156 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 491
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 208`, `args: 70`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 179`, `planned_debt: 3`, `unreferenced_by_name: 30`
* *Architecture:* `api: 70`, `import: 10`
* *Defense:* `safety: 61`, `doc: 105`, `sync_locks: 16`, `immutability_locks: 9`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.811
  * `Choke Point (Betweenness):` 0.000293 | `Ripple Effect (Closeness):` 0.012165
  * `Imports (Out-Degree: 12):` Yii, yii\base\InvalidArgumentException, yii\base\InvalidCallException, yii\base\InvalidConfigException, yii\base\InvalidParamException, yii\base\Model, yii\base\ModelEvent, yii\base\NotSupportedException...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `framework/web/Request.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.494)
- **Top Global Matches:** file_cluster_12: 7.494, file_cluster_15: 7.55, file_cluster_16: 7.727
- **Magnitude:** 1060.06 | **LOC:** 2041 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.4%), Guard Balance (formerly Safety Score) (71.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseAcceptHeader` **(Compute Cores)** (Impact: 30.2)
    * *Intent:* * $accepts = $request->parseAcceptHeader($header); * print_r($accepts); * // displays: * // [ * // '...
  * `loadCookies` **(I/O & Config Routines)** (Impact: 18.1)
    * *Intent:* /** * Converts `$_COOKIE` into an array of [[Cookie]]. * @return array the cookies obtained from req...
  * `getUserIpFromIpHeader` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* /** * Return user IP's from IP header. * * @param string $ips comma separated IP list * @return stri...
  * `getHostInfo` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* * You may explicitly specify it by setting the [[setHostInfo()|hostInfo]] property. * * > Warning: D...
  * `getScriptUrl` **(Defensive Guards)** (Impact: 14.1)
    * *Intent:* /** * Returns the relative URL of the entry script. * The implementation of this method referenced Z...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 174 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 244`, `args: 89`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 200`, `planned_debt: 5`, `fragile_debt: 4`, `unreferenced_by_name: 40`
* *Architecture:* `io: 16`, `api: 86`, `import: 3`
* *Defense:* `safety: 42`, `doc: 109`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Yii, yii\base\InvalidConfigException, yii\validators\IpValidator
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/QueryBuilder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.445)
- **Top Global Matches:** file_cluster_15: 5.445, file_cluster_16: 6.363, file_cluster_11: 7.922
- **Magnitude:** 986.92 | **LOC:** 1794 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 0.935; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (95.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.7%), Guard Balance (formerly Safety Score) (69.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildSelect` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* /** * @param array $columns * @param array $params the binding parameters to be populated * @param b...
  * `batchInsert` **(Many-Argument Workhorses)** (Impact: 33.7)
    * *Intent:* * ['Linda', 25], * ]); * ``` * * Note that the values in each row must match the corresponding colum...
  * `build` **(Defensive Guards)** (Impact: 19.6)
    * *Intent:* /** * Generates a SELECT SQL statement from a [[Query]] object. * * @param Query $query the [[Query]...
  * `prepareInsertValues` **(Stateful Encapsulated Methods)** (Impact: 19.4)
    * *Intent:* /** * Prepares a `VALUES` part for an `INSERT` SQL statement. * * @param string $table the table tha...
  * `prepareInsertSelectSubQuery` **(Stateful Encapsulated Methods)** (Impact: 17.1)
    * *Intent:* /** * Prepare select-subquery and field names for INSERT INTO ... SELECT SQL statement. * * @param Q...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 136 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 216`, `args: 80`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `state_mutation: 177`, `unreferenced_by_name: 45`
* *Architecture:* `api: 70`, `import: 5`
* *Defense:* `safety: 51`, `doc: 88`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.935
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.005731
  * `Imports (Out-Degree: 5):` yii\base\InvalidArgumentException, yii\base\NotSupportedException, yii\db\conditions\ConditionInterface, yii\db\conditions\HashCondition, yii\helpers\StringHelper
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `framework/console/controllers/MessageController.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.177)
- **Top Global Matches:** file_cluster_6: 8.177, file_cluster_8: 8.814, file_cluster_4: 16.434
- **Magnitude:** 883.24 | **LOC:** 1028 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.57; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.1%)
- **Documentation Coverage:** 4.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `saveMessagesToDb` **(Many-Argument Workhorses)** (Impact: 94.7)
    * *Intent:* /** * Saves messages to database. * * @param array $messages * @param Connection $db * @param string...
  * `saveMessagesToPO` **(Many-Argument Workhorses)** (Impact: 77.7)
    * *Intent:* /** * Writes messages into PO file. * * @param array $messages * @param string $dirName name of the ...
  * `saveMessagesCategoryToPHP` **(Many-Argument Workhorses)** (Impact: 71.3)
    * *Intent:* /** * Writes category messages into PHP file. * * @param array $messages * @param string $fileName n...
  * `extractMessagesFromTokens` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* /** * Extracts messages from a parsed PHP tokens list. * @param array $tokens tokens to be processed...
  * `initConfig` **(Defensive Guards)** (Impact: 21.5)
    * *Intent:* /** * @param string $configFile * @throws Exception If configuration file does not exists. * @since ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 129 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 418
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 106`, `args: 17`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 160`, `planned_debt: 6`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `api: 24`, `import: 14`
* *Defense:* `safety: 30`, `doc: 41`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.57
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.000955
  * `Imports (Out-Degree: 9):` $configFile, $fileName, Yii, yii\console\Application, yii\console\Controller, yii\console\Exception, yii\console\ExitCode, yii\db\Connection...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseFileHelper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.56)
- **Top Global Matches:** file_cluster_4: 7.56, file_cluster_6: 8.127, file_cluster_9: 13.374
- **Magnitude:** 861.6 | **LOC:** 1032 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.7%), Complexity Load (formerly Cognitive Load) (42.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `changeOwnership` **(Many-Argument Workhorses)** (Impact: 58.9)
    * *Intent:* * @param string|array|int|null $ownership the user and/or group ownership for the file or directory....
  * `copyDirectory` **(Defensive Guards)** (Impact: 52.8)
    * *Intent:* * - recursive: boolean, whether the files under the subdirectories should also be copied. Defaults t...
  * `normalizePath` **(Defensive Guards)** (Impact: 32.7)
    * *Intent:* * The normalization does the following work: * * - Convert all directory separators into `DIRECTORY_...
  * `matchPathname` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /** * Compares a path part against a pattern with optional wildcards. * * Based on match_pathname() ...
  * `lastExcludeMatchingFromList` **(Stateful Encapsulated Methods)** (Impact: 27.4)
    * *Intent:* /** * Scan the given exclude list in reverse to see whether pathname * should be ignored. The first ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 126 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 120`, `args: 28`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 133`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 10`
* *Defense:* `safety: 50`, `doc: 31`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` $aliasesFile, $extensionsFile, $magicFile, Yii, yii\base\ErrorException, yii\base\Exception, yii\base\InvalidArgumentException, yii\base\InvalidConfigException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/framework/db/ActiveRecordTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.874)
- **Top Global Matches:** file_cluster_12: 7.874, file_cluster_11: 9.141, file_cluster_15: 9.385
- **Magnitude:** 843.42 | **LOC:** 2320 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **36**; blast radius 0.599; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.7%), Complexity Load (formerly Cognitive Load) (16.2%), Connectivity (formerly Api Exposure) (11.6%), Dead Code Surface (formerly Dead Code) (4.9%)
- **Documentation Coverage:** 58.2888% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testJoinWithAlias` **(Compute Cores)** (Impact: 58.6)
    * *Intent:* /** * Tests the alias syntax for joinWith: 'alias' => 'relation'. * @dataProvider aliasMethodProvide...
  * `testPopulateWithoutPk` **(I/O & Config Routines)** (Impact: 13.3)
  * `testAmbiguousColumnIndexBy` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* /** * Ensure no ambiguous column error occurs on indexBy with JOIN. * * @see https://github.com/yiis...
  * `testJoinWith` **(I/O & Config Routines)** (Impact: 10.0)
  * `testLoadRelations` **(I/O & Config Routines)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 53 instances
* *Memory Alloc (weighted view):* 23
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 250`, `args: 131`, `func_start: 94`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 4`, `state_mutation: 337`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 83`
* *Architecture:* `api: 93`, `import: 36`
* *Defense:* `safety: 6`, `doc: 72`, `test: 383`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.599
  * `Choke Point (Betweenness):` 8.4e-05 | `Ripple Effect (Closeness):` 0.00191
  * `Imports (Out-Degree: 31):` ActiveRecordTestTrait, Yii, yii\base\InvalidArgumentException, yii\base\InvalidConfigException, yii\db\ActiveQuery, yii\db\ActiveRecordInterface, yii\db\Query, yii\helpers\ArrayHelper...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseConsole.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.314)
- **Top Global Matches:** file_cluster_4: 7.314, file_cluster_12: 7.603, file_cluster_15: 7.869
- **Magnitude:** 764.46 | **LOC:** 1208 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.711; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.7%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (47.6%)
- **Documentation Coverage:** 0.9524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ansiToHtml` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * Converts an ANSI formatted string to HTML. * * Note: xTerm 256 bit colors are currently not su...
  * `ansiColorizedSubstr` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* /** * Returns the portion with ANSI color codes of string specified by the start and length paramete...
  * `getScreenSize` **(Type Conversions)** (Impact: 28.1)
    * *Intent:* /** * Returns terminal screen size. * * Usage: * * ``` * list($width, $height) = ConsoleHelper::getS...
  * `updateProgress` **(Many-Argument Workhorses)** (Impact: 23.8)
    * *Intent:* /** * Updates a progress bar that has been started by [[startProgress()]]. * * @param int $done the ...
  * `prompt` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* * Prompts the user for input and validates it. * * @param string $text prompt string * @param array ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 111 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 369
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 122`, `args: 57`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 147`, `planned_debt: 2`, `unreferenced_by_name: 33`
* *Architecture:* `io: 2`, `api: 78`, `import: 3`
* *Defense:* `safety: 11`, `doc: 56`, `immutability_locks: 28`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.711
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.000955
  * `Imports (Out-Degree: 2):` Yii, yii\base\Model, yii\console\Markdown
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/helpers/BaseArrayHelper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.435)
- **Top Global Matches:** file_cluster_4: 7.435, file_cluster_6: 9.895, file_cluster_9: 10.886
- **Magnitude:** 727.6 | **LOC:** 1104 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toArray` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* * The result of `ArrayHelper::toArray($post, $properties)` could be like the following: * * ``` * [ ...
  * `filter` **(Compute Cores)** (Impact: 37.4)
    * *Intent:* * // [ * // 'B' => ['D' => 2], * // ] * ``` * * @param array $array Source array * @param iterable $...
  * `getValue` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* * $street = \yii\helpers\ArrayHelper::getValue($users, 'address.street'); * // using an array of key...
  * `merge` **(Defensive Guards)** (Impact: 22.1)
    * *Intent:* * Merges two or more arrays into one recursively. * If each array has an element with the same strin...
  * `multisort` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* * @param array $array the array to be sorted. The array will be modified after calling this method. ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 111`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 119`, `dead_code: 4`, `planned_debt: 7`, `unreferenced_by_name: 15`
* *Architecture:* `api: 21`, `import: 5`
* *Defense:* `safety: 22`, `doc: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ArrayAccess, Traversable, Yii, yii\base\Arrayable, yii\base\InvalidArgumentException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Query.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.158)
- **Top Global Matches:** file_cluster_15: 5.158, file_cluster_16: 7.021, file_cluster_11: 7.393
- **Magnitude:** 671.16 | **LOC:** 1403 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **51** in-repo importer(s); it depends on **6**; blast radius 7.972; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.3%), Guard Balance (formerly Safety Score) (72.0%), Complexity Load (formerly Cognitive Load) (34.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `column` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* /** * Executes the query and returns the first column of the result. * @param Connection|null $db th...
  * `normalizeSelect` **(Stateful Encapsulated Methods)** (Impact: 20.1)
    * *Intent:* /** * Normalizes the SELECT columns passed to [[select()]] or [[addSelect()]]. * * @param string|arr...
  * `cleanUpTableNames` **(Stateful Encapsulated Methods)** (Impact: 18.6)
    * *Intent:* /** * Clean up table names and aliases * Both aliases and names are enclosed into {{ and }}. * @para...
  * `getUniqueColumns` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* /** * Returns unique column names excluding duplicates. * Columns to be removed: * - if column defin...
  * `queryScalar` **(Defensive Guards)** (Impact: 14.7)
    * *Intent:* /** * Queries a scalar value by setting [[select]] first. * Restores the value of select to make thi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 337
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 142`, `args: 51`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `state_mutation: 143`, `dead_code: 1`, `unreferenced_by_name: 26`
* *Architecture:* `api: 56`, `import: 7`
* *Defense:* `safety: 24`, `doc: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.972
  * `Choke Point (Betweenness):` 0.000597 | `Ripple Effect (Closeness):` 0.055711
  * `Imports (Out-Degree: 6):` QueryTrait, Yii, yii\base\Component, yii\base\InvalidArgumentException, yii\base\InvalidConfigException, yii\helpers\ArrayHelper
  * `Imported By (In-Degree: 51):` (Excluded from Brief to save tokens)

### `tests/framework/helpers/HtmlTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.667)
- **Top Global Matches:** file_cluster_11: 6.667, file_cluster_15: 7.348, file_cluster_16: 8.194
- **Magnitude:** 620.96 | **LOC:** 2351 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (51.7%), Complexity Load (formerly Cognitive Load) (18.2%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 68.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testNonStrictBooleanDropDownList` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* /** * @dataProvider providerForNonStrictBooleanDropDownList */
  * `testStrictBooleanDropDownList` **(Many-Argument Workhorses)** (Impact: 9.8)
    * *Intent:* /** * @dataProvider providerForStrictBooleanDropDownList */
  * `testCheckboxList` **(I/O & Config Routines)** (Impact: 6.4)
  * `setActivePlaceholder` **(Stateful Encapsulated Methods)** (Impact: 6.3)
    * *Intent:* /** * @param Model $model * @param string $attribute * @param array $options */
  * `testRadioList` **(I/O & Config Routines)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 323`, `args: 125`, `func_start: 112`, `class_start: 3`
* *Risk/State:* `state_mutation: 212`, `dead_code: 2`, `unreferenced_by_name: 108`
* *Architecture:* `io: 3`, `api: 107`, `import: 10`
* *Defense:* `safety: 3`, `doc: 37`, `test: 170`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` ArrayObject, Closure, Yii, yii\base\DynamicModel, yii\base\InvalidArgumentException, yii\base\Model, yii\db\ArrayExpression, yii\helpers\Html...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/ActiveRelationTrait.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.934)
- **Top Global Matches:** file_cluster_6: 5.934, file_cluster_8: 11.738, file_cluster_4: 13.08
- **Magnitude:** 609.64 | **LOC:** 639 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.603; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (41.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `populateRelation` **(Many-Argument Workhorses)** (Impact: 64.1)
    * *Intent:* /** * Finds the related records and populates them into the primary models. * @param string $name th...
  * `populateInverseRelation` **(Many-Argument Workhorses)** (Impact: 58.7)
    * *Intent:* /** * @param ActiveRecordInterface[]|array<array-key, array<string, mixed>> $primaryModels primary m...
  * `buildBuckets` **(Many-Argument Workhorses)** (Impact: 36.8)
    * *Intent:* /** * @param array $models * @param array $link * @param array|null $viaModels * @param self<ActiveR...
  * `filterByModels` **(Defensive Guards)** (Impact: 31.2)
    * *Intent:* /** * @param array $models */
  * `prefixKeyColumns` **(Stateful Encapsulated Methods)** (Impact: 16.8)
    * *Intent:* /** * @param array $attributes the attributes to prefix * @return array */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 106 instances
* *State Mutation (weighted view):* 320
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 68`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 108`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 42`, `doc: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.603
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.012094
  * `Imports (Out-Degree: 2):` yii\base\InvalidArgumentException, yii\base\InvalidConfigException
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/db/ActiveQuery.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.991)
- **Top Global Matches:** file_cluster_4: 4.991, file_cluster_6: 9.966, file_cluster_15: 10.932
- **Magnitude:** 604.8 | **LOC:** 867 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **3**; blast radius 5.193; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.7%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 2.439% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `joinWithRelation` **(Many-Argument Workhorses)** (Impact: 41.3)
    * *Intent:* /** * Joins a parent query with a child query. * The current query object will be modified according...
  * `prepare` **(Defensive Guards)** (Impact: 31.8)
    * *Intent:* /** * {@inheritdoc} */
  * `joinWithRelations` **(Many-Argument Workhorses)** (Impact: 24.2)
    * *Intent:* /** * Modifies the current query by adding join fragments based on the given relations. * @param Act...
  * `removeDuplicatedModels` **(Defensive Guards)** (Impact: 23.5)
    * *Intent:* /** * Removes duplicated models by checking their primary key values. * This method is mainly called...
  * `buildJoinWith` **(I/O & Config Routines)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 109 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 76`, `args: 24`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 118`, `unreferenced_by_name: 9`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 35`, `doc: 36`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.193
  * `Choke Point (Betweenness):` 0.000212 | `Ripple Effect (Closeness):` 0.018453
  * `Imports (Out-Degree: 4):` ActiveQueryTrait, ActiveRelationTrait, yii\base\InvalidConfigException
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `framework/console/Controller.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.051)
- **Top Global Matches:** file_cluster_4: 7.051, file_cluster_6: 8.449, file_cluster_15: 13.365
- **Magnitude:** 584.28 | **LOC:** 809 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (90.1%), Debt Markers (formerly Tech Debt) (81.9%), Guard Balance (formerly Safety Score) (78.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindActionParams` **(Defensive Guards)** (Impact: 48.7)
    * *Intent:* /** * Binds the parameters to the action. * This method is invoked by [[Action]] when it begins to r...
  * `runAction` **(Defensive Guards)** (Impact: 41.6)
    * *Intent:* /** * Runs an action with the specified action ID and parameters. * If the action ID is empty, the m...
  * `getActionArgsHelp` **(Defensive Guards)** (Impact: 32.5)
    * *Intent:* * - required: bool, whether this argument is required * - type: string|null, the PHP type(s) of this...
  * `getActionOptionsHelp` **(Defensive Guards)** (Impact: 19.4)
    * *Intent:* * * - type: string, the PHP type of this argument. * - default: string, the default value of this ar...
  * `parseDocCommentTags` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* /** * Parses the comment block into tags. * @param \ReflectionClass<object>|\ReflectionProperty|\Ref...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 110 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 92`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 116`, `unreferenced_by_name: 16`
* *Architecture:* `io: 1`, `api: 27`, `import: 8`
* *Defense:* `safety: 30`, `doc: 35`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Yii, yii\base\Action, yii\base\Controller, yii\base\InlineAction, yii\base\InvalidRouteException, yii\base\Module, yii\helpers\Console, yii\helpers\Inflector
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/AssetController.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.525)
- **Top Global Matches:** file_cluster_4: 6.525, file_cluster_6: 10.35, file_cluster_12: 11.408
- **Magnitude:** 582.38 | **LOC:** 847 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.552; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (71.1%), Complexity Load (formerly Cognitive Load) (36.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `adjustCssUrl` **(Many-Argument Workhorses)** (Impact: 45.5)
    * *Intent:* /** * Adjusts CSS content allowing URL references pointing to the original resources. * @param strin...
  * `loadTargets` **(Defensive Guards)** (Impact: 32.2)
    * *Intent:* /** * Creates full list of output asset bundles. * @param array $targets output asset bundles config...
  * `buildTarget` **(Stateful Encapsulated Methods)** (Impact: 25.9)
    * *Intent:* /** * Builds output asset bundle. * @param \yii\web\AssetBundle $target output asset bundle * @param...
  * `adjustDependency` **(Stateful Encapsulated Methods)** (Impact: 17.6)
    * *Intent:* /** * Adjust dependencies between asset bundles in the way source bundles begin to depend on output ...
  * `saveTargets` **(Stateful Encapsulated Methods)** (Impact: 14.3)
    * *Intent:* /** * Saves new asset bundles configuration. * @param \yii\web\AssetBundle[] $targets list of asset ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 94 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 304
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 111`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 2`, `state_mutation: 116`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 44`, `doc: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.552
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000955
  * `Imports (Out-Degree: 6):` $configFile, Yii, yii\console\Application, yii\console\Controller, yii\console\Exception, yii\console\ExitCode, yii\helpers\Console, yii\helpers\FileHelper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `framework/web/Response.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.805)
- **Top Global Matches:** file_cluster_4: 6.805, file_cluster_12: 8.39, file_cluster_16: 10.04
- **Magnitude:** 582.32 | **LOC:** 1158 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (91.7%), Guard Balance (formerly Safety Score) (71.2%), Complexity Load (formerly Cognitive Load) (34.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `redirect` **(Many-Argument Workhorses)** (Impact: 29.9)
    * *Intent:* * * Any relative URL that starts with a single forward slash "/" will be converted * into an absolut...
  * `sendStreamAsFile` **(Defensive Guards)** (Impact: 21.8)
    * *Intent:* * @param string $attachmentName the file name shown to the user. * @param array $options additional ...
  * `sendContent` **(I/O & Config Routines)** (Impact: 18.8)
    * *Intent:* /** * Sends the response content to the client. */
  * `sendCookies` **(Defensive Guards)** (Impact: 18.3)
    * *Intent:* /** * Sends the cookies to the client. */
  * `prepare` **(Stateful Encapsulated Methods)** (Impact: 16.1)
    * *Intent:* /** * Prepares for sending the response. * The default implementation will convert [[data]] into [[c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 292
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 101`, `args: 34`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 114`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 17`
* *Architecture:* `io: 7`, `api: 45`, `import: 8`
* *Defense:* `safety: 20`, `doc: 53`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Yii, yii\base\InvalidArgumentException, yii\base\InvalidConfigException, yii\base\InvalidRouteException, yii\helpers\FileHelper, yii\helpers\Inflector, yii\helpers\StringHelper, yii\helpers\Url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/console/controllers/BaseMigrateController.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.873)
- **Top Global Matches:** file_cluster_4: 5.873, file_cluster_16: 10.272, file_cluster_9: 10.919
- **Magnitude:** 581.86 | **LOC:** 1020 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 0.578; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.8%), Guard Balance (formerly Safety Score) (70.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `actionUp` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* * Upgrades the application by applying new migrations. * * For example, * * ``` * yii migrate # appl...
  * `actionRedo` **(Compute Cores)** (Impact: 22.2)
    * *Intent:* * them again. For example, * * ``` * yii migrate/redo # redo the last applied migration * yii migrat...
  * `actionMark` **(Compute Cores)** (Impact: 20.7)
    * *Intent:* * ``` * yii migrate/mark 101129_185401 # using timestamp * yii migrate/mark m101129_185401_create_us...
  * `actionDown` **(Compute Cores)** (Impact: 20.6)
    * *Intent:* * For example, * * ``` * yii migrate/down # revert the last migration * yii migrate/down 3 # revert ...
  * `getNewMigrations` **(I/O & Config Routines)** (Impact: 19.4)
    * *Intent:* /** * Returns the migrations that are not applied. * @return array list of new migrations */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 96 instances
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 141`, `args: 30`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 104`, `planned_debt: 1`, `unreferenced_by_name: 9`
* *Architecture:* `io: 1`, `api: 19`, `import: 15`
* *Defense:* `safety: 24`, `doc: 40`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.578
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.001273
  * `Imports (Out-Degree: 10):` $file, Yii, yii\base\Action, yii\base\BaseObject, yii\base\InvalidConfigException, yii\base\NotSupportedException, yii\console\Application, yii\console\Controller...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/framework/db/CommandTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.613)
- **Top Global Matches:** file_cluster_12: 6.613, file_cluster_7: 9.237, file_cluster_15: 9.468
- **Magnitude:** 579.7 | **LOC:** 1680 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.2%), Complexity Load (formerly Cognitive Load) (21.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.8%), Connectivity (formerly Api Exposure) (10.3%)
- **Documentation Coverage:** 73.5849% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testBindParamValue` **(I/O & Config Routines)** (Impact: 20.6)
  * `testInsertExpression` **(I/O & Config Routines)** (Impact: 13.8)
  * `upsertProvider` **(I/O & Config Routines)** (Impact: 8.5)
  * `testAddDropForeignKey` **(Many-Argument Workhorses)** (Impact: 6.5)
    * *Intent:* /** * @dataProvider addForeignKeyProvider * * @param string $name * @param string $tableName * @para...
  * `testAutoRefreshTableSchema` **(I/O & Config Routines)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 58 instances
* *Api Near Db Sink:* 10 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 117`, `args: 58`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 8`, `state_mutation: 203`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 51`
* *Architecture:* `io: 15`, `api: 52`, `import: 15`
* *Defense:* `safety: 25`, `doc: 16`, `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` ArrayObject, PDO, Throwable, testBatchInsertWithYield.php', yii\base\InvalidArgumentException, yii\caching\ArrayCache, yii\db\Connection, yii\db\DataReader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/rbac/DbManager.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.631)
- **Top Global Matches:** file_cluster_12: 6.631, file_cluster_16: 6.918, file_cluster_15: 7.291
- **Magnitude:** 562.4 | **LOC:** 1138 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 1.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.4%), Guard Balance (formerly Safety Score) (64.1%), Complexity Load (formerly Cognitive Load) (29.8%)
- **Documentation Coverage:** 9.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkAccessFromCache` **(Stateful Encapsulated Methods)** (Impact: 21.5)
    * *Intent:* /** * Performs access check for the specified user based on the data loaded from cache. * This metho...
  * `checkAccessRecursive` **(Stateful Encapsulated Methods)** (Impact: 19.3)
    * *Intent:* /** * Performs access check for the specified user. * This method is internally called by [[checkAcc...
  * `loadFromCache` **(Defensive Guards)** (Impact: 13.0)
  * `checkAccess` **(Type Conversions)** (Impact: 11.0)
    * *Intent:* /** * {@inheritdoc} */
  * `getRolesByUser` **(Compute Cores)** (Impact: 10.1)
    * *Intent:* /** * {@inheritdoc} * The roles returned by this method include the roles assigned via [[$defaultRol...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 76 instances
* *Api Near Db Sink:* 5 instances
* *Memory Alloc (weighted view):* 27
* *State Mutation (weighted view):* 249
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 184`, `args: 50`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 97`, `unreferenced_by_name: 29`
* *Architecture:* `api: 35`, `import: 8`
* *Defense:* `safety: 22`, `doc: 63`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.414
  * `Choke Point (Betweenness):` 9.8e-05 | `Ripple Effect (Closeness):` 0.006686
  * `Imports (Out-Degree: 9):` Yii, yii\base\InvalidArgumentException, yii\base\InvalidCallException, yii\caching\CacheInterface, yii\db\Connection, yii\db\Expression, yii\db\Query, yii\di\Instance
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `framework/db/mssql/Schema.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.218)
- **Top Global Matches:** file_cluster_16: 6.218, file_cluster_4: 7.217, file_cluster_15: 7.404
- **Magnitude:** 548.7 | **LOC:** 832 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (83.6%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (43.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadTableConstraints` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* /** * Loads multiple types of constraints and returns the specified ones. * @param string $tableName...
  * `loadColumnSchema` **(Stateful Encapsulated Methods)** (Impact: 29.8)
    * *Intent:* /** * Loads the column information into a [[ColumnSchema]] object. * @param array $info column infor...
  * `findColumns` **(Defensive Guards)** (Impact: 17.5)
    * *Intent:* /** * Collects the metadata of table columns. * @param TableSchema $table the table metadata * @retu...
  * `insert` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /** * Retrieving inserted data from a primary key request of type uniqueidentifier (for SQL Server 2...
  * `resolveTableNames` **(Stateful Encapsulated Methods)** (Impact: 11.7)
    * *Intent:* /** * Resolves the table name and schema name (if any). * @param TableSchema $table the table metada...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 102 instances
* *Api Near Db Sink:* 3 instances
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 94`, `args: 29`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 137`, `unreferenced_by_name: 19`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 12`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` ConstraintFinderTrait, ViewFinderTrait, Yii, yii\db\CheckConstraint, yii\db\Constraint, yii\db\ConstraintFinderInterface, yii\db\ConstraintFinderTrait, yii\db\DefaultValueConstraint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Connection.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.032)
- **Top Global Matches:** file_cluster_15: 6.032, file_cluster_16: 6.934, file_cluster_11: 7.024
- **Magnitude:** 546.24 | **LOC:** 1289 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **6**; blast radius 5.379; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (80.5%), Guard Balance (formerly Safety Score) (66.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `openFromPoolSequentially` **(Defensive Guards)** (Impact: 25.7)
    * *Intent:* * connection attempts to unavailable servers saves time when the connection attempts fail due to tim...
  * `getQueryCacheInfo` **(Compute Cores)** (Impact: 20.5)
    * *Intent:* /** * Returns the current query cache information. * This method is used internally by [[Command]]. ...
  * `createPdoInstance` **(I/O & Config Routines)** (Impact: 14.6)
    * *Intent:* /** * Creates the PDO instance. * This method is called by [[open]] to establish a DB connection. * ...
  * `open` **(Defensive Guards)** (Impact: 11.2)
    * *Intent:* /** * Establishes a DB connection. * It does nothing if a DB connection has already been established...
  * `initConnection` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* /** * Initializes the DB connection. * This method is invoked right after the DB connection is estab...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 79 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 284
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 104`, `args: 36`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 126`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `io: 12`, `api: 64`, `import: 6`
* *Defense:* `safety: 47`, `doc: 84`, `immutability_locks: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.379
  * `Choke Point (Betweenness):` 0.000507 | `Ripple Effect (Closeness):` 0.049674
  * `Imports (Out-Degree: 7):` PDO, Yii, yii\base\Component, yii\base\InvalidConfigException, yii\base\NotSupportedException, yii\caching\CacheInterface
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `framework/di/Container.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.165)
- **Top Global Matches:** file_cluster_4: 6.165, file_cluster_6: 9.366, file_cluster_16: 12.451
- **Magnitude:** 545.28 | **LOC:** 833 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 1.196; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.1%), Debt Markers (formerly Tech Debt) (62.4%), Complexity Load (formerly Cognitive Load) (42.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveCallableDependencies` **(Defensive Guards)** (Impact: 71.7)
    * *Intent:* /** * Resolve dependencies for a function. * * This method can be used to implement similar function...
  * `getDependencies` **(Defensive Guards)** (Impact: 30.4)
    * *Intent:* /** * Returns the dependencies of the specified class. * * @template T of object * * @param class-st...
  * `build` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* /** * Creates an instance of the specified class. * This method will resolve dependencies of the spe...
  * `get` **(Many-Argument Workhorses)** (Impact: 24.1)
    * *Intent:* * * @param string|class-string<T>|Instance $class the class Instance, name, or an alias name (e.g. `...
  * `normalizeDefinition` **(Stateful Encapsulated Methods)** (Impact: 22.2)
    * *Intent:* /** * Normalizes the class definition. * @param string $class class name * @param string|array|calla...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 85 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 96`, `args: 20`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `planned_debt: 1`, `unreferenced_by_name: 7`
* *Architecture:* `api: 12`, `import: 8`
* *Defense:* `safety: 35`, `doc: 31`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.196
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.006792
  * `Imports (Out-Degree: 6):` ReflectionClass, ReflectionException, ReflectionNamedType, ReflectionParameter, Yii, yii\base\Component, yii\base\InvalidConfigException, yii\helpers\ArrayHelper
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `framework/db/mssql/QueryBuilder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.509)
- **Top Global Matches:** file_cluster_12: 8.509, file_cluster_7: 8.895, file_cluster_5: 9.995
- **Magnitude:** 532.82 | **LOC:** 692 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.499; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (88.2%), Guard Balance (formerly Safety Score) (82.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert` **(Many-Argument Workhorses)** (Impact: 34.4)
    * *Intent:* /** * {@inheritdoc} * Added OUTPUT construction for getting inserted data (for SQL Server 2005 or la...
  * `upsert` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* /** * {@inheritdoc} * @see https://docs.microsoft.com/en-us/sql/t-sql/statements/merge-transact-sql ...
  * `alterColumn` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* /** * Builds a SQL statement for changing the definition of a column. * @param string $table the tab...
  * `normalizeTableRowData` **(Stateful Encapsulated Methods)** (Impact: 14.8)
    * *Intent:* /** * Normalizes data to be saved into the table, performing extra preparations and type converting,...
  * `oldBuildOrderByAndLimit` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* /** * Builds the ORDER BY/LIMIT/OFFSET clauses for SQL SERVER 2005 to 2008. * @param string $sql the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 88 instances
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 87`, `args: 30`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 107`, `unreferenced_by_name: 19`
* *Architecture:* `api: 19`, `import: 5`
* *Defense:* `safety: 10`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.499
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` yii\base\InvalidArgumentException, yii\base\NotSupportedException, yii\db\Expression, yii\db\Query, yii\db\TableSchema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `framework/db/Command.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.013)
- **Top Global Matches:** file_cluster_15: 6.013, file_cluster_16: 6.371, file_cluster_11: 6.971
- **Magnitude:** 528.36 | **LOC:** 1348 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.641; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Guard Balance (formerly Safety Score) (65.5%), Complexity Load (formerly Cognitive Load) (44.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `queryInternal` **(Stateful Encapsulated Methods)** (Impact: 18.0)
    * *Intent:* /** * Performs the actual DB query of a SQL statement. * @param string $method method of PDOStatemen...
  * `getRawSql` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Returns the raw SQL by inserting parameter values into the corresponding placeholders in [[sql...
  * `internalExecute` **(Stateful Encapsulated Methods)** (Impact: 15.4)
    * *Intent:* /** * Executes a prepared statement. * * It's a wrapper around [[\PDOStatement::execute()]] to suppo...
  * `prepare` **(Defensive Guards)** (Impact: 14.4)
    * *Intent:* /** * Prepares the SQL statement to be executed. * For complex SQL statement that is to be executed ...
  * `bindValues` **(Defensive Guards)** (Impact: 14.2)
    * *Intent:* /** * Binds a list of values to the corresponding parameters. * This is similar to [[bindValue()]] e...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 145`, `args: 64`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 130`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 40`
* *Architecture:* `io: 2`, `api: 57`, `import: 3`
* *Defense:* `safety: 29`, `doc: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.641
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000955
  * `Imports (Out-Degree: 4):` Yii, yii\base\Component, yii\base\NotSupportedException
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/framework/data/ActiveDataFilterTest.php` (PHP) | Magnitude: 27.26 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 190, structural_boundaries: 19, state_mutation: 11, args: 6
- `tests/data/base/Singer.php` (PHP) | Magnitude: 0.01 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, api: 6, args: 3
- `tests/framework/filters/auth/BasicAuthTest.php` (PHP) | Magnitude: 53.02 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 76, structural_boundaries: 27, state_mutation: 25, globals: 14
- `tests/js/tests/yii.activeForm.test.js` (JAVASCRIPT) | Magnitude: 66.72 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 47, core_var_decl: 40, args: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/framework/web/RequestTest.php` (PHP) | Magnitude: 447.76 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1123, state_mutation: 173, structural_boundaries: 138, test: 122
- `framework/captcha/CaptchaValidator.php` (PHP) | Magnitude: 63.46 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 19, state_mutation: 14, doc: 12
- `tests/framework/db/ColumnSchemaBuilderTest.php` (PHP) | Magnitude: 26.2 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 15, doc: 5, args: 4
- `framework/web/CompositeUrlRule.php` (PHP) | Magnitude: 66.96 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 21, branch: 12, doc: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `framework/web/DbSession.php` (PHP) | Magnitude: 120.1 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 38, branch: 22, state_mutation: 22
- `tests/framework/db/pgsql/ActiveRecordTest.php` (PHP) | Magnitude: 91.12 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 257, structural_boundaries: 73, memory_alloc: 34, state_mutation: 29
- `tests/framework/grid/RadiobuttonColumnTest.php` (PHP) | Magnitude: 26.36 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 33, state_mutation: 10, args: 9
- `framework/web/Request.php` (PHP) | Magnitude: 1060.06 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 955, structural_boundaries: 244, branch: 229, state_mutation: 200
- `tests/framework/grid/CheckboxColumnTest.php` (PHP) | Magnitude: 26.96 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 75, structural_boundaries: 39, memory_alloc: 14, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/framework/base/DynamicModelTest.php` (PHP) | Magnitude: 39.18 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 91, test: 28, state_mutation: 19, structural_boundaries: 17
- `framework/web/SessionHandler.php` (PHP) | Magnitude: 20.34 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 17, doc: 9, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `framework/i18n/migrations/schema-pgsql.sql` (SQLITE) | Magnitude: 0.85 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: safety: 6, indent_spaces: 6, safety_bypasses: 4, state_mutation: 4
- `tests/framework/db/mssql/QueryBuilderTest.php` (PHP) | Magnitude: 225.04 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 697, safety_bypasses: 141, state_mutation: 117, structural_boundaries: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `framework/web/CookieCollection.php` (PHP) | Magnitude: 104.68 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 42, doc: 20, api: 17
- `framework/validators/UrlValidator.php` (PHP) | Magnitude: 98.8 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 23, branch: 19, state_mutation: 17
- `framework/db/mysql/QueryBuilder.php` (PHP) | Magnitude: 305.12 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 255, structural_boundaries: 65, state_mutation: 55, branch: 46
- `framework/db/oci/conditions/InConditionBuilder.php` (PHP) | Magnitude: 56.46 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 13, structural_boundaries: 12, branch: 6
- `framework/console/UnknownCommandException.php` (PHP) | Magnitude: 68.4 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 20, state_mutation: 18, doc: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `framework/behaviors/AttributesBehavior.php` (PHP) | Magnitude: 47.88 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 22, branch: 12, doc: 9
- `framework/behaviors/OptimisticLockBehavior.php` (PHP) | Magnitude: 70.5 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 22, state_mutation: 15, sync_locks: 14
- `framework/db/pgsql/QueryBuilder.php` (PHP) | Magnitude: 490.2 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 329, state_mutation: 103, structural_boundaries: 72, branch: 67
- `framework/validators/TrimValidator.php` (PHP) | Magnitude: 41.98 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 12, doc: 9, branch: 8
- `tests/framework/filters/AccessRuleTest.php` (PHP) | Magnitude: 283.0 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 464, state_mutation: 203, structural_boundaries: 73, test: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `framework/console/ExitCode.php` (PHP) | Magnitude: 23.9 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 40, doc: 21, api: 19, immutability_locks: 17
- `framework/web/Cookie.php` (PHP) | Magnitude: 20.6 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, doc: 14, api: 12, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/framework/db/sqlite/SqlTokenizerTest.php` (PHP) | Magnitude: 88.86 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1077, structural_boundaries: 182, memory_alloc: 169, high_risk_execution: 7
- `tests/framework/base/StaticInstanceTraitTest.php` (PHP) | Magnitude: 4.96 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, test: 5, import: 3
- `framework/filters/auth/AuthInterface.php` (PHP) | Magnitude: 29.76 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, doc: 5, import: 5, args: 3
- `tests/framework/web/UrlNormalizerTest.php` (PHP) | Magnitude: 50.44 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 105, state_mutation: 35, structural_boundaries: 28, test: 26
- `framework/base/ExitException.php` (PHP) | Magnitude: 24.5 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 5, structural_boundaries: 4, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `framework/widgets/ActiveField.php` (PHP) | Magnitude: 523.38 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 407, state_mutation: 122, structural_boundaries: 85, branch: 83

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `framework/i18n/GettextMoFile.php` (PHP) | Magnitude: 188.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 130, state_mutation: 42, structural_boundaries: 30, branch: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `framework/db/mssql/DBLibPDO.php` (PHP) | Magnitude: 11.58 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 8, doc: 4, branch: 3
- `tests/framework/console/controllers/BaseMessageControllerTest.php` (PHP) | Magnitude: 272.94 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 503, state_mutation: 164, structural_boundaries: 65, args: 34
- `tests/framework/test/ArrayFixtureTest.php` (PHP) | Magnitude: 13.32 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 11, args: 4, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `framework/validators/ImageValidator.php` (PHP) | Magnitude: 112.78 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 101, branch: 22, structural_boundaries: 21, state_mutation: 19
- `framework/web/migrations/m160313_153426_session_init.php` (PHP) | Magnitude: 25.0 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 25, branch: 7, structural_boundaries: 5, state_mutation: 4
- `framework/web/AssetBundle.php` (PHP) | Magnitude: 128.18 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 80, state_mutation: 30, branch: 21, structural_boundaries: 16
- `framework/db/oci/ColumnSchemaBuilder.php` (PHP) | Magnitude: 20.48 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, branch: 7, doc: 4
- `framework/db/sqlite/ColumnSchemaBuilder.php` (PHP) | Magnitude: 20.48 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, branch: 7, doc: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `framework/BaseYii.php` -> Churn: **100.0%** | Cog Load: 45.6138% | Debt: 98.2742%
- `framework/console/Controller.php` -> Churn: **90.09%** | Cog Load: 47.4512% | Debt: 81.9065%
- `framework/web/Controller.php` -> Churn: **81.03%** | Cog Load: 47.2755% | Debt: 76.9183%
- `framework/base/Application.php` -> Churn: **75.97%** | Cog Load: 32.4028% | Debt: 94.3514%
- `framework/base/Controller.php` -> Churn: **71.77%** | Cog Load: 46.769% | Debt: 97.577%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `framework/i18n/Formatter.php` -> **Alexander Makarov** (100.0% isolated ownership) | Magnitude: 1455.26
- `framework/helpers/BaseFileHelper.php` -> **Alexander Makarov** (100.0% isolated ownership) | Magnitude: 861.6
- `framework/helpers/BaseConsole.php` -> **Alexander Makarov** (100.0% isolated ownership) | Magnitude: 764.46
- `framework/helpers/BaseArrayHelper.php` -> **Maksim Spirkov** (100.0% isolated ownership) | Magnitude: 727.6
- `framework/db/ActiveRelationTrait.php` -> **Maksim Spirkov** (100.0% isolated ownership) | Magnitude: 609.64

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `framework/base/Component.php` -> **Severity: 0.139** (Bridge: 0.0014 * Flux: 99.9998%)
- `framework/base/Model.php` -> **Severity: 0.112** (Bridge: 0.0011 * Flux: 100.0%)
- `framework/db/Query.php` -> **Severity: 0.06** (Bridge: 0.0006 * Flux: 100.0%)
- `framework/base/BaseObject.php` -> **Severity: 0.057** (Bridge: 0.0006 * Flux: 99.995%)
- `framework/db/Connection.php` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `framework/Yii.php` -> **Severity: 16.823** (Embedded: 0.3289 * Error Risk: 51.1427%)
- `tests/TestCase.php` -> **Severity: 11.828** (Embedded: 0.1652 * Error Risk: 71.5976%)
- `framework/base/Component.php` -> **Severity: 8.732** (Embedded: 0.1423 * Error Risk: 61.3505%)
- `framework/base/Event.php` -> **Severity: 7.21** (Embedded: 0.1065 * Error Risk: 67.6878%)
- `framework/base/BaseObject.php` -> **Severity: 6.774** (Embedded: 0.1135 * Error Risk: 59.6725%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/framework/caching/CacheTestCase.php` -> **Severity: 579.613** (Blast Radius: 7.206 * Doc Risk: 80.4348%)
- `tests/framework/i18n/IntlTestHelper.php` -> **Severity: 534.857** (Blast Radius: 7.488 * Doc Risk: 71.4286%)
- `tests/data/validators/models/FakedValidationModel.php` -> **Severity: 186.627** (Blast Radius: 2.281 * Doc Risk: 81.8182%)
- `tests/framework/web/session/AbstractDbSessionTest.php` -> **Severity: 146.963** (Blast Radius: 1.984 * Doc Risk: 74.0741%)
- `tests/TestCase.php` -> **Severity: 141.092** (Blast Radius: 31.04 * Doc Risk: 4.5455%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24933 call pairs -- scoped 34.9%, unique 0.9%, ambiguous 26.8%, external 37.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 24374 | 35.4% | 0.9% | 27.4% | 36.3% |
| javascript | 496 | 13.1% | 0.0% | 0.4% | 86.5% |
| db2_sql | 54 | 0.0% | 0.0% | 0.0% | 100.0% |
| postgresql | 7 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
