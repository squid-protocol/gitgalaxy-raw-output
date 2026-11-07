# ARCHITECTURAL_BRIEF: cakephp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/cakephp/cakephp.git` |
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
- **Scope:** 1652 analyzed artifact(s), 223420 LOC.
- **Load-bearing artifact:** `src/TestSuite/TestCase.php` -- 363 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/TestCase/ORM/TableTest.php` -- pulls in 59 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/test_app/config/key.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 1840 |
| Analyzed Artifacts (Scanned) | 1652 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 188 |
| Total LOC | 223420 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 89.8% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5528 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1578 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.217 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 81 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 1562 | 218046 | 94.6% |
| JSON | 19 | 818 | 1.2% |
| PLAINTEXT | 18 | 2 | 1.1% |
| MARKDOWN | 17 | 0 | 1.0% |
| YAML | 11 | 484 | 0.7% |
| JAVASCRIPT | 8 | 4 | 0.5% |
| CSS | 7 | 636 | 0.4% |
| XML | 6 | 0 | 0.4% |
| MAKEFILE | 1 | 131 | 0.1% |
| PYTHON | 1 | 3254 | 0.1% |
| SHELL | 1 | 34 | 0.1% |
| HTML | 1 | 11 | 0.1% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 1649 |
| unknown | unknown | 2 |
| utf-8 | bom | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 19%, Interface Declarations Files 17%, Declarative / Non-Code 16%, Parameter Forwarders Files 13%, Large Core Modules (3) 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1617 | 97.9% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 33 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 188*

**Composition by Extension & Reason:**
- `.po`: 49x Excluded (Unsupported Extension: '.po')
- `.php`: 46x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 4 exceeds 500 chars)
- `.mo`: 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 13x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 5x Unsupported Format (.dist), 2x Excluded (Unsupported Extension: '.dist')
- `.ini`: 5x Excluded (Unsupported Extension: '.ini')
- `.gif`: 4x Excluded (Explicitly Denied Extension: '.gif')
- `.jpg`: 3x Excluded (Explicitly Denied Extension: '.jpg'), 1x Excluded (Explicitly Denied Extension: '.JPG')
- `.neon`: 3x Excluded (Unsupported Extension: '.neon')
- `.swf`: 2x Excluded (Unsupported Extension: '.swf')
- `.pdf`: 2x Excluded (Explicitly Denied Extension: '.pdf')
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 72.8 | 9.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.6 | 40.8 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 1.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 74.4 | 6.9 | 4.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.6 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.5 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10259 | 743 | 14 | `tests/TestCase/Database/Query/SelectQueryTest.php` |
| cleanup | 604 | 203 | 1 | `src/View/Helper/FormHelper.php` |
| guards | 8251 | 971 | 12 | `contrib/git-filter-repo` |
| danger | 2185 | 400 | 2 | `tests/TestCase/Mailer/MessageTest.php` |
| concurrency | 85 | 33 | 0 | `src/Cache/Engine/FileEngine.php` |
| connectivity | 13063 | 1218 | 19 | `tests/TestCase/ORM/TableTest.php` |
| io | 855 | 162 | 0 | `tests/TestCase/Mailer/Transport/SmtpTransportTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 275 | 42 | 0 | `contrib/git-filter-repo` |
| time | 1188 | 90 | 0 | `tests/TestCase/Validation/ValidationTest.php` |
| serialization | 371 | 81 | 0 | `tests/TestCase/View/JsonViewTest.php` |
| regex | 231 | 80 | 0 | `contrib/git-filter-repo` |
| events | 315 | 56 | 0 | `contrib/git-filter-repo` |
| tests | 15234 | 404 | 19 | `tests/TestCase/Validation/ValidationTest.php` |
| docs | 16955 | 1367 | 24 | `tests/TestCase/ORM/TableTest.php` |
| debt | 636 | 184 | 1 | `tests/TestCase/Datasource/ModelAwareTraitTest.php` |
| mutation | 42421 | 1190 | 59 | `contrib/git-filter-repo` |
| dead_code | 9893 | 927 | 15 | `tests/TestCase/ORM/TableTest.php` |
| credential | 77 | 11 | 0 | `tests/TestCase/Utility/TextTest.php` |
| threat | 43 | 18 | 0 | `src/Http/Middleware/CsrfProtectionMiddleware.php` |
| ml_ai | 356 | 54 | 0 | `tests/TestCase/Database/Query/SelectQueryTest.php` |
| ui | 1010 | 170 | 1 | `src/View/Helper/FormHelper.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/TestCase/Mailer/Transport/SmtpTransportTest.php` (Hits: 127)
- `contrib/git-filter-repo` (Hits: 126)
- `src/TestSuite/IntegrationTestTrait.php` (Hits: 20)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **TestCase.php** (`src/TestSuite/TestCase.php`) — 363 inbound connections
2. **InvalidArgumentException.php** (`src/Cache/Exception/InvalidArgumentException.php`) — 191 inbound connections
3. **CakeException.php** (`src/Core/Exception/CakeException.php`) — 169 inbound connections
4. **Configure.php** (`src/Core/Configure.php`) — 107 inbound connections
5. **Table.php** (`src/ORM/Table.php`) — 87 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TableTest.php** (`tests/TestCase/ORM/TableTest.php`) — 59 outbound dependencies
2. **ExceptionsTest.php** (`tests/TestCase/ExceptionsTest.php`) — 58 outbound dependencies
3. **IntegrationTestTrait.php** (`src/TestSuite/IntegrationTestTrait.php`) — 57 outbound dependencies
4. **Table.php** (`src/ORM/Table.php`) — 47 outbound dependencies
5. **WebExceptionRendererTest.php** (`tests/TestCase/Error/Renderer/WebExceptionRendererTest.php`) — 45 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_compute_metadata` **(Many-Argument Workhorses)** (@ `contrib/git-filter-repo`) -> Impact: **129.6** | LOC: 192
  * *Intent:* # # First, handle commit_renames # old_commit_renames = dict() if not self._already_ran: commit_renames = {old: new for old, new in self._commit_renam...
- `calculate` **(Compute Cores)** (@ `src/I18n/PluralRules.php`) -> Impact: **120.4** | LOC: 53
  * *Intent:* /** * Returns the plural form number for the passed locale corresponding * to the countable provided in $n. * * @param string $locale The locale to ge...
- `create_arg_parser` **(I/O & Config Routines)** (@ `contrib/git-filter-repo`) -> Impact: **107.3** | LOC: 427
  * *Intent:* # Include usage in the summary, so we can put the description first summary = _('''Rewrite (or analyze) repository history git-filter-repo destructive...
- `_tweak_commit` **(Many-Argument Workhorses)** (@ `contrib/git-filter-repo`) -> Impact: **106.3** | LOC: 207
- `match` **(Defensive Guards)** (@ `src/Routing/Route/Route.php`) -> Impact: **98.9** | LOC: 142
  * *Intent:* /** * Check if a URL array matches this route instance. * * If the URL matches the route parameters and settings, then * return a generated string URL...
- `sanity_check` **(Many-Argument Workhorses)** (@ `contrib/git-filter-repo`) -> Impact: **98.1** | LOC: 122
- `columnDefinitionSql` **(Defensive Guards)** (@ `src/Database/Schema/MysqlSchemaDialect.php`) -> Impact: **92.9** | LOC: 217
  * *Intent:* /** * Create a SQL snippet for a column based on the array shape * that `describeColumns()` creates. * * @param array $column The column metadata * @r...
- `_convertColumn` **(Many-Argument Workhorses)** (@ `src/Database/Schema/SqlserverSchemaDialect.php`) -> Impact: **90.3** | LOC: 107
  * *Intent:* /** * Convert a column definition to the abstract types. * * The returned type will be a type that * Cake\Database\TypeFactory can handle. * * @param ...
- `assertHtml` **(Many-Argument Workhorses)** (@ `src/TestSuite/TestCase.php`) -> Impact: **87.6** | LOC: 152
  * *Intent:* * [ * ['input' => ['name', 'id' => 'preg:/FieldName\d+/']], * 'preg:/My\s+field/' * ] * ``` * * Important: This function is very forgiving about white...
- `_filter_files` **(Compute Cores)** (@ `contrib/git-filter-repo`) -> Impact: **86.7** | LOC: 105

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/test_app/config` | 16 | 10169.2 | 0.0% | 0.0% |
| `tests/TestCase/ORM` | 23 | 5154.46 | 2.91% | 0.0% |
| `src/Database/Schema` | 17 | 4980.43 | 24.28% | 74.19% |
| `src/ORM` | 23 | 4761.66 | 20.81% | 38.31% |
| `tests/TestCase/View/Helper` | 9 | 4483.58 | 11.58% | 0.0% |
| `src/View/Helper` | 10 | 4460.48 | 35.8% | 58.02% |
| `src/Validation` | 10 | 4117.52 | 19.66% | 45.15% |
| `src/Utility` | 12 | 3564.14 | 24.69% | 24.97% |
| `src/Http` | 26 | 3532.2 | 22.33% | 53.92% |
| `src/Database` | 24 | 2872.89 | 17.56% | 43.55% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Cache/Engine/NullEngine.php` -> **100.0%** Exposure
- `src/Database/Schema/UniqueKey.php` -> **100.0%** Exposure
- `src/I18n/Package.php` -> **100.0%** Exposure
- `src/View/Form/NullContext.php` -> **100.0%** Exposure
- `src/Console/TestSuite/StubConsoleOutput.php` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `contrib/validate-deprecation-aliases.php` -> **100.0%** Exposure
- `contrib/validate-split-packages-phpstan.php` -> **100.0%** Exposure
- `contrib/validate-split-packages.php` -> **100.0%** Exposure
- `src/Collection/CollectionInterface.php` -> **100.0%** Exposure
- `src/Collection/CollectionTrait.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/TestCase/ORM/TableTest.php` -> **263** Orphaned Functions | **0** Duplicates
- `tests/TestCase/View/Helper/FormHelperTest.php` -> **234** Orphaned Functions | **0** Duplicates
- `tests/TestCase/Database/Query/SelectQueryTest.php` -> **145** Orphaned Functions | **0** Duplicates
- `tests/TestCase/Validation/ValidatorTest.php` -> **142** Orphaned Functions | **0** Duplicates
- `tests/TestCase/Collection/CollectionTest.php` -> **137** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/Fixture/AuthUsersFixture.php` -> **100.0%** Exposure
- `tests/Fixture/UsersFixture.php` -> **100.0%** Exposure
- `tests/TestCase/Http/Client/Auth/OauthTest.php` -> **99.9991%** Exposure
- `tests/TestCase/ORM/TableTest.php` -> **72.7757%** Exposure
- `tests/TestCase/Utility/HashTest.php` -> **60.2917%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6764` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/test_app/config/key.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_app/config/key_with_passphrase.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Validation/Validator.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.036)
- **Top Global Matches:** file_cluster_15: 6.036, file_cluster_16: 7.586, file_cluster_4: 8.038
- **Magnitude:** 2491.34 | **LOC:** 3252 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **10**; blast radius 0.931; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.8%), Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (36.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* /** * Validates and returns an array of failed fields and their error messages. * * @param array<str...
  * `isEmpty` **(Stateful Encapsulated Methods)** (Impact: 35.2)
    * *Intent:* /** * Returns true if the field is empty in the passed data array * * @param mixed $data Value to ch...
  * `_processRules` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /** * Iterates over each rule in the validation set and collects the errors resulting * from executi...
  * `creditCard` **(Many-Argument Workhorses)** (Impact: 24.5)
    * *Intent:* /** * Add a credit card rule to a field. * * @param string $field The field you want to apply the ru...
  * `addNestedMany` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* * * This method assumes that the sub-document has a 1:N relationship with the parent. * * The provid...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 422 instances
* *State Mutation (weighted view):* 1297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 280`, `args: 112`, `func_start: 105`, `class_start: 1`
* *Risk/State:* `state_mutation: 453`, `unreferenced_by_name: 75`
* *Architecture:* `api: 109`, `import: 10`
* *Defense:* `safety: 27`, `doc: 128`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 0.000232 | `Ripple Effect (Closeness):` 0.006922
  * `Imports (Out-Degree: 3):` ArrayAccess, ArrayIterator, BackedEnum, Cake\I18n\__d, Closure, Countable, InvalidArgumentException, IteratorAggregate...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `tests/TestCase/View/Helper/FormHelperTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.803)
- **Top Global Matches:** file_cluster_11: 8.803, file_cluster_15: 9.407, file_cluster_2: 9.506
- **Magnitude:** 2156.4 | **LOC:** 9567 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (17.4%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 2.1142% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testControlCustomization` **(I/O & Config Routines)** (Impact: 13.0)
    * *Intent:* /** * testControlCustomization method * * Tests the input method and passing custom options. */
  * `testErrorMessageDisplay` **(I/O & Config Routines)** (Impact: 9.5)
    * *Intent:* /** * testErrorMessageDisplay method * * Test error message display. */
  * `testControlSelectType` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* /** * testControlSelectType method * * Test form->control() with select type inputs. */
  * `testSelectMultipleCheckboxes` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /** * testSelectMultipleCheckboxes method * * Test generation of multi select elements in checkbox f...
  * `testControlMaxLengthEntityContext` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /** * testControlMaxLengthEntityContext method * * Test control() with maxlength attribute in Entity...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 1187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 774`, `args: 244`, `func_start: 237`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 1171`, `planned_debt: 16`, `unreferenced_by_name: 234`
* *Architecture:* `io: 2`, `api: 235`, `import: 43`
* *Defense:* `safety: 39`, `doc: 239`, `test: 93`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 33):` ArrayObject, Cake\Chronos\ChronosTime, Cake\Collection\Collection, Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\Database\Type\EnumType, Cake\Form\Form, Cake\Form\FormProtector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/TestCase/ORM/TableTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.422)
- **Top Global Matches:** file_cluster_11: 6.422, file_cluster_15: 7.577, file_cluster_2: 7.96
- **Magnitude:** 1974.52 | **LOC:** 6661 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **59**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (72.8%), Guard Balance (formerly Safety Score) (53.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.2%), Connectivity (formerly Api Exposure) (12.4%)
- **Documentation Coverage:** 7.037% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setUp` **(I/O & Config Routines)** (Impact: 7.0)
  * `testCallbackArgumentTypes` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* /** * Tests that the callbacks receive the expected types of arguments. */
  * `testSaveManyResultSet` **(I/O & Config Routines)** (Impact: 5.1)
    * *Intent:* /** * Test saveMany() with ResultSet instance */
  * `testSetSchemaLongIdentifiers` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* /** * Tests schema method with long identifiers */
  * `testSaveManyFailedWithException` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* /** * Test saveMany() with failed save due to an exception */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 28 instances
* *Api Near Db Sink:* 1 instances
* *Memory Alloc (weighted view):* 264
* *State Mutation (weighted view):* 1045
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 792`, `args: 359`, `func_start: 271`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 989`, `dead_code: 1`, `unreferenced_by_name: 263`
* *Architecture:* `api: 269`, `import: 59`
* *Defense:* `safety: 31`, `doc: 276`, `test: 620`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` ArrayObject, AssertionError, BadMethodCallException, Cake\Collection\Collection, Cake\Core\Exception\CakeException, Cake\Database\Connection, Cake\Database\Driver\Sqlserver, Cake\Database\Exception\DatabaseException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/View/Helper/FormHelper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.881)
- **Top Global Matches:** file_cluster_4: 5.881, file_cluster_16: 9.551, file_cluster_15: 9.606
- **Magnitude:** 1912.32 | **LOC:** 2750 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 0.317; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.1%), Complexity Load (formerly Cognitive Load) (36.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `control` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* * option you will also need to modify the default `checkboxWrapper` template to include the * `{{inp...
  * `create` **(Many-Argument Workhorses)** (Impact: 52.5)
    * *Intent:* * the templates you want to load, or an array of templates to use. * - `context` Additional options ...
  * `postLink` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* * HTTP/1.1 DELETE request. Defaults to 'post'. * - `confirm` - Confirm message to show. Form executi...
  * `_initInputField` **(Defensive Guards)** (Impact: 36.0)
    * *Intent:* * - `disabled` - mixed - Either a boolean indicating disabled state, or the string in * a numericall...
  * `error` **(Many-Argument Workhorses)** (Impact: 30.8)
    * *Intent:* * Uses the `error`, `errorList` and `errorItem` templates. The `errorList` and * `errorItem` templat...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 347 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 1134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 299`, `structural_boundaries: 212`, `args: 69`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `state_mutation: 440`, `planned_debt: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 45`, `import: 24`
* *Defense:* `safety: 89`, `doc: 82`, `immutability_locks: 1`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.317
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.002423
  * `Imports (Out-Degree: 17):` BackedEnum, Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\Core\deprecationWarning, Cake\Core\h, Cake\Database\TypeFactory, Cake\Database\Type\EnumLabelInterface, Cake\Database\Type\EnumType...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/ORM/Table.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.92)
- **Top Global Matches:** file_cluster_4: 6.92, file_cluster_15: 7.094, file_cluster_16: 7.755
- **Magnitude:** 1430.92 | **LOC:** 3325 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **87** in-repo importer(s); it depends on **47**; blast radius 13.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.6%), Guard Balance (formerly Safety Score) (69.7%), Debt Markers (formerly Tech Debt) (62.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invokeFinder` **(Many-Argument Workhorses)** (Impact: 60.5)
    * *Intent:* /** * @internal * @template TSubject of \Cake\Datasource\EntityInterface|array * @param \Closure $ca...
  * `_processSave` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /** * Performs the actual saving of an entity based on the passed options. * * @param \Cake\Datasour...
  * `get` **(Many-Argument Workhorses)** (Impact: 33.0)
    * *Intent:* * @param mixed $primaryKey primary key value to find * @param array|string $finder The finder to use...
  * `_saveMany` **(Many-Argument Workhorses)** (Impact: 31.8)
    * *Intent:* /** * @template TSavedEntity of \Cake\Datasource\EntityInterface * @param iterable<TSavedEntity> $en...
  * `_insert` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* /** * Auxiliary function to handle the insert of an entity's data in the table * * @param \Cake\Data...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 211 instances
* *Api Near Db Sink:* 1 instances
* *Memory Alloc (weighted view):* 35
* *State Mutation (weighted view):* 697
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 356`, `args: 105`, `func_start: 92`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 275`, `unreferenced_by_name: 41`
* *Architecture:* `api: 80`, `import: 47`
* *Defense:* `safety: 56`, `doc: 128`, `immutability_locks: 5`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.417
  * `Choke Point (Betweenness):` 0.013694 | `Ripple Effect (Closeness):` 0.165611
  * `Imports (Out-Degree: 33):` ArrayObject, BadMethodCallException, Cake\Collection\CollectionInterface, Cake\Core\App, Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\Core\deprecationWarning, Cake\Core\namespaceSplit...
  * `Imported By (In-Degree: 87):` (Excluded from Brief to save tokens)

### `tests/TestCase/Database/Query/SelectQueryTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_11: 7.729, file_cluster_10: 8.035, file_cluster_15: 8.679
- **Magnitude:** 1412.66 | **LOC:** 4456 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Guard Balance (formerly Safety Score) (57.7%), Complexity Load (formerly Cognitive Load) (14.6%), Connectivity (formerly Api Exposure) (11.5%)
- **Documentation Coverage:** 13.4948% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testIdentifierCollation` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * Tests setting identifier collation. */
  * `testStringExpression` **(Defensive Guards)** (Impact: 10.7)
    * *Intent:* /** * Tests creating StringExpression. */
  * `testSelectWhereOperatorMethods` **(Callbacks & Closures)** (Impact: 9.8)
    * *Intent:* /** * Tests using where conditions with operator methods */
  * `testSQLFunctions` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* /** * Tests that functions are correctly transformed and their parameters are bound */
  * `testDecorateResults` **(Callbacks & Closures)** (Impact: 7.5)
    * *Intent:* /** * Tests stacking decorators for results and resetting the list of decorators */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *Api Near Db Sink:* 5 instances
* *State Mutation (weighted view):* 829
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 698`, `args: 216`, `func_start: 145`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 715`, `unreferenced_by_name: 145`
* *Architecture:* `api: 146`, `import: 31`
* *Defense:* `safety: 19`, `doc: 131`, `test: 255`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` ArrayIterator, Cake\Collection\collection, Cake\Database\Connection, Cake\Database\DriverFeatureEnum, Cake\Database\Driver\Mysql, Cake\Database\Driver\Postgres, Cake\Database\Driver\Sqlite, Cake\Database\Driver\Sqlserver...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Validation/Validation.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.677)
- **Top Global Matches:** file_cluster_15: 6.677, file_cluster_12: 7.521, file_cluster_16: 7.596
- **Magnitude:** 1266.0 | **LOC:** 1977 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **15**; blast radius 0.838; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (81.8%), Guard Balance (formerly Safety Score) (71.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `creditCard` **(Many-Argument Workhorses)** (Impact: 39.0)
    * *Intent:* /** * Validation of credit card numbers. * Returns true if $check is in the proper credit card forma...
  * `datetime` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* * Time is validated as 24hr (HH:MM[:SS][.FFFFFF]) or am/pm ([H]H:MM[a|p]m) * * Seconds and fractiona...
  * `checkEnum` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /** * @param mixed $check * @param class-string $enumClassName * @param array<string, mixed> $option...
  * `decimal` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* * Be aware that the currently set locale is being used to determine * the decimal and thousands sepa...
  * `multiple` **(Many-Argument Workhorses)** (Impact: 27.7)
    * *Intent:* /** * Validates a multiple select. Comparison is case sensitive by default. * * Valid Options * * - ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 264`, `args: 70`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 225`, `unreferenced_by_name: 41`
* *Architecture:* `api: 70`, `import: 15`
* *Defense:* `safety: 43`, `doc: 83`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.838
  * `Choke Point (Betweenness):` 0.00022 | `Ripple Effect (Closeness):` 0.008456
  * `Imports (Out-Degree: 4):` BackedEnum, Cake\Chronos\ChronosDate, Cake\Chronos\ChronosTime, Cake\Core\Exception\CakeException, Cake\I18n\DateTime, Cake\Utility\Text, Countable, DateTimeInterface...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Utility/Hash.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.225)
- **Top Global Matches:** file_cluster_6: 7.225, file_cluster_8: 12.438, file_cluster_4: 14.007
- **Magnitude:** 1228.0 | **LOC:** 1286 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **10**; blast radius 11.105; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Debt Markers (formerly Tech Debt) (41.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_matches` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* /** * Checks whether $data matches the attribute patterns * * @param \ArrayAccess<array-key, mixed>|...
  * `combine` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* /** * Creates an associative array using `$keyPath` as the path to build its keys, and optionally * ...
  * `sort` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* * ``` * Hash::sort($data, 'some.attribute', 'asc', ['type' => 'regular', 'ignoreCase' => true]); * `...
  * `get` **(Defensive Guards)** (Impact: 39.5)
    * *Intent:* * Get a single value specified by $path out of $data. * Does not support the full dot notation featu...
  * `extract` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* * - `1.User.name` Get the name of the user at index 1. * - `{n}.User.name` Get the name of every use...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 201 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 135`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 212`, `unreferenced_by_name: 16`
* *Architecture:* `api: 23`, `import: 12`
* *Defense:* `safety: 36`, `doc: 39`, `immutability_locks: 7`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.105
  * `Choke Point (Betweenness):` 0.001614 | `Ripple Effect (Closeness):` 0.187901
  * `Imports (Out-Degree: 3):` ArrayAccess, Cake\Core\Exception\CakeException, InvalidArgumentException, SORT_ASC, SORT_DESC, SORT_LOCALE_STRING, SORT_NATURAL, SORT_NUMERIC...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/Mailer/Message.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.272)
- **Top Global Matches:** file_cluster_4: 6.272, file_cluster_15: 7.885, file_cluster_16: 8.76
- **Magnitude:** 1217.72 | **LOC:** 1947 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.6%), Guard Balance (formerly Safety Score) (77.9%), Complexity Load (formerly Cognitive Load) (45.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* /** * Wrap the message to follow the RFC 2822 - 2.1.1 * * @param string|null $message Message to wra...
  * `getHeaders` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* * ### Includes: * * - `from` * - `replyTo` * - `readReceipt` * - `returnPath` * - `to` * - `cc` * - ...
  * `setAttachments` **(Defensive Guards)** (Impact: 28.1)
    * *Intent:* * ] * ]); * ``` * * The `contentId` key allows you to specify an inline attachment. In your email te...
  * `generateMessage` **(I/O & Config Routines)** (Impact: 21.4)
    * *Intent:* /** * Generate full message. * * @return array<string> */
  * `addAttachment` **(Many-Argument Workhorses)** (Impact: 15.6)
    * *Intent:* /** * Add attachment. * * @param \Psr\Http\Message\UploadedFileInterface|string $path Path to the fi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 201 instances
* *State Mutation (weighted view):* 684
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 216`, `args: 82`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 282`, `unreferenced_by_name: 50`
* *Architecture:* `io: 4`, `api: 71`, `import: 23`
* *Defense:* `safety: 27`, `doc: 116`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Cake\Core\Configure, Cake\Core\env, Cake\Http\Client\FormDataPart, Cake\Utility\Hash, Cake\Utility\Security, Cake\Utility\Text, Closure, InvalidArgumentException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/TestCase/Validation/ValidatorTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.139)
- **Top Global Matches:** file_cluster_11: 7.139, file_cluster_15: 8.293, file_cluster_10: 8.754
- **Magnitude:** 1159.66 | **LOC:** 3215 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (15.6%), Connectivity (formerly Api Exposure) (12.2%)
- **Documentation Coverage:** 4.1096% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertProxyMethod` **(Stateful Encapsulated Methods)** (Impact: 16.1)
    * *Intent:* /** * Tests that a rule in the Validator class exists and was configured as expected. * * @param Val...
  * `assertValidationMessage` **(Stateful Encapsulated Methods)** (Impact: 12.7)
    * *Intent:* /** * Assert for the data validation message for a given field's rule for a I18n-enabled & a I18n-di...
  * `testNestedManyValidationWithParentContextAndIndex` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /** * Test that nested many validators receive parent context and index information */
  * `testNestedValidationWithParentContext` **(I/O & Config Routines)** (Impact: 4.3)
    * *Intent:* /** * Test that nested validators receive parent context information */
  * `testMethodsWithExtraArguments` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* /** * Tests that it is possible to pass extra arguments to the validation function * and it still ge...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 12 instances
* *Memory Alloc (weighted view):* 177
* *State Mutation (weighted view):* 664
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 381`, `args: 156`, `func_start: 147`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 640`, `unreferenced_by_name: 142`
* *Architecture:* `api: 147`, `import: 16`
* *Defense:* `safety: 18`, `doc: 143`, `test: 224`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Cake\TestSuite\TestCase, Cake\Validation\Validation, Cake\Validation\ValidationRule, Cake\Validation\ValidationSet, Cake\Validation\Validator, InvalidArgumentException, Laminas\Diactoros\UploadedFile, TestApp\Model\Enum\ArticleStatus...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Utility/Text.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.019)
- **Top Global Matches:** file_cluster_4: 6.019, file_cluster_6: 7.928, file_cluster_9: 13.158
- **Magnitude:** 1133.68 | **LOC:** 1194 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **6**; blast radius 6.642; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.1%), Debt Markers (formerly Tech Debt) (45.6%), Complexity Load (formerly Cognitive Load) (35.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_substr` **(Many-Argument Workhorses)** (Impact: 57.6)
    * *Intent:* /** * Return part of a string. * * ### Options: * * - `html` If true, HTML entities will be handled ...
  * `tokenize` **(Many-Argument Workhorses)** (Impact: 50.5)
    * *Intent:* /** * Tokenizes a string using $separator, ignoring any instance of $separator that appears between ...
  * `truncate` **(Many-Argument Workhorses)** (Impact: 48.6)
    * *Intent:* * * ### Options: * * - `ellipsis` Will be used as ending and appended to the trimmed string * - `exa...
  * `_wordWrap` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* /** * Unicode aware version of wordwrap as helper method. * * @param string $text The text to format...
  * `insert` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* * - before: The character or string in front of the name of the variable placeholder (Defaults to `:...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 705
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 103`, `args: 30`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 255`, `unreferenced_by_name: 16`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 11`, `doc: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.642
  * `Choke Point (Betweenness):` 0.001809 | `Ripple Effect (Closeness):` 0.148814
  * `Imports (Out-Degree: 3):` Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\I18n\__d, Closure, InvalidArgumentException, Transliterator
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `tests/TestCase/ORM/Query/SelectQueryTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.869)
- **Top Global Matches:** file_cluster_10: 6.869, file_cluster_11: 7.117, file_cluster_2: 8.06
- **Magnitude:** 1080.9 | **LOC:** 4176 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **34**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%), Connectivity (formerly Api Exposure) (11.4%), Complexity Load (formerly Cognitive Load) (8.5%)
- **Documentation Coverage:** 5.1471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testWith` **(I/O & Config Routines)** (Impact: 6.3)
    * *Intent:* /** * Tests ORM query using with CTE. */
  * `testFormatResultsBelongsToMany` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* /** * Tests that belongsToMany associations are also correctly hydrated */
  * `testBelongsToManyEagerLoadingNoHydration` **(I/O & Config Routines)** (Impact: 5.9)
    * *Intent:* /** * Tests that BelongsToMany associations are correctly eager loaded. * Also that the query object...
  * `testFormatDeepDistantAssociationRecords` **(Callbacks & Closures)** (Impact: 4.5)
    * *Intent:* /** * Tests that formatters cna be applied to deep associations that are fetched using * additional ...
  * `testFilteringByBelongsToManyNoHydration` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* /** * Tests that BelongsToMany associations are correctly eager loaded. * Also that the query object...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 490`, `args: 246`, `func_start: 136`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 533`, `unreferenced_by_name: 133`
* *Architecture:* `api: 135`, `import: 34`
* *Defense:* `safety: 7`, `doc: 134`, `test: 216`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` AssertionError, Cake\Cache\CacheEngine, Cake\Cache\Engine\FileEngine, Cake\Database\Connection, Cake\Database\DriverFeatureEnum, Cake\Database\Driver\Mysql, Cake\Database\Driver\Sqlite, Cake\Database\Exception\DatabaseException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/View/Helper/PaginatorHelper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.888)
- **Top Global Matches:** file_cluster_4: 5.888, file_cluster_16: 9.197, file_cluster_15: 9.277
- **Magnitude:** 953.08 | **LOC:** 1322 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.277; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.1%), Complexity Load (formerly Cognitive Load) (36.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sort` **(Many-Argument Workhorses)** (Impact: 60.1)
    * *Intent:* * * - `escape` Whether you want the contents html entity encoded, defaults to true. * - `direction` ...
  * `generateUrlParams` **(Defensive Guards)** (Impact: 37.9)
    * *Intent:* /** * Merges passed URL options with current pagination state to generate a pagination URL. * * @par...
  * `limitControl` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* /** * Dropdown select for pagination limit. * This will generate a wrapping form. * * Options: * - `...
  * `_toggledLink` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* /** * Generate an active/inactive link for next/prev methods. * * @param string|false $text The enab...
  * `prepareLimitOptions` **(Stateful Encapsulated Methods)** (Impact: 17.6)
    * *Intent:* /** * Prepare and filter limit options for limitControl. * * Handles generating limits from steps, a...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 166 instances
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 114`, `args: 35`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 216`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 14`
* *Defense:* `safety: 36`, `doc: 39`, `sync_locks: 5`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.277
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000606
  * `Imports (Out-Degree: 10):` Cake\Core\Exception\CakeException, Cake\Core\h, Cake\Datasource\Paging\PaginatedInterface, Cake\Datasource\Paging\SortField, Cake\I18n\__, Cake\Utility\Hash, Cake\Utility\Inflector, Cake\View\Helper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/TestCase/Routing/RouterTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.254)
- **Top Global Matches:** file_cluster_11: 7.254, file_cluster_15: 8.196, file_cluster_2: 8.339
- **Magnitude:** 947.0 | **LOC:** 3571 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.3%), Complexity Load (formerly Cognitive Load) (11.3%), Connectivity (formerly Api Exposure) (9.7%)
- **Documentation Coverage:** 11.0092% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUrlGenerationWithPrefix` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /** * Test URL generation with an admin prefix */
  * `testUrlNormalization` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* /** * testUrlNormalization method */
  * `match` **(Parameter Forwarders)** (Impact: 3.7)
  * `testReverseRouteKeyAndPassDuplicateValues` **(I/O & Config Routines)** (Impact: 3.5)
  * `testUrlGenerationBasic` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* /** * test generation of basic urls. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 52
* *State Mutation (weighted view):* 562
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 230`, `args: 138`, `func_start: 111`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 558`, `planned_debt: 1`, `unreferenced_by_name: 105`
* *Architecture:* `api: 107`, `import: 18`
* *Defense:* `safety: 13`, `doc: 102`, `test: 288`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\Http\ServerRequest, Cake\Http\ServerRequestFactory, Cake\Routing\Exception\DuplicateNamedRouteException, Cake\Routing\Exception\MissingRouteException, Cake\Routing\RouteBuilder, Cake\Routing\RouteCollection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ORM/Association/BelongsToMany.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.686)
- **Top Global Matches:** file_cluster_12: 6.686, file_cluster_4: 8.02, file_cluster_16: 8.416
- **Magnitude:** 941.74 | **LOC:** 1551 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **14**; blast radius 0.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.6%), Guard Balance (formerly Safety Score) (77.0%), Complexity Load (formerly Cognitive Load) (33.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_diffLinks` **(Many-Argument Workhorses)** (Impact: 55.4)
    * *Intent:* /** * Helper method used to delete the difference between the links passed in * `$existing` and `$jo...
  * `_saveTarget` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /** * Persists each of the entities into the target table and creates links between * the parent ent...
  * `unlink` **(Many-Argument Workhorses)** (Impact: 22.1)
    * *Intent:* * ``` * * `$article->get('tags')` will contain only `[$tag4]` after deleting in the database * * @pa...
  * `_saveLinks` **(Many-Argument Workhorses)** (Impact: 20.6)
    * *Intent:* /** * Creates links between the source entity and each of the passed target entities * * @param \Cak...
  * `replaceLinks` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* * $articles->getAssociation('tags')->replaceLinks($article, $tags); * ``` * * `$article->get('tags')...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 157 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 544
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 166`, `args: 47`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 230`, `unreferenced_by_name: 13`
* *Architecture:* `api: 27`, `import: 14`
* *Defense:* `safety: 35`, `doc: 77`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.749
  * `Choke Point (Betweenness):` 0.00053 | `Ripple Effect (Closeness):` 0.112938
  * `Imports (Out-Degree: 11):` Cake\Core\App, Cake\Database\ExpressionInterface, Cake\Database\Expression\IdentifierExpression, Cake\Database\Expression\QueryExpression, Cake\Datasource\EntityInterface, Cake\ORM\Association, Cake\ORM\Association\Loader\SelectWithPivotLoader, Cake\ORM\Query\SelectQuery...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/TestSuite/IntegrationTestTrait.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.431)
- **Top Global Matches:** file_cluster_15: 6.431, file_cluster_16: 6.976, file_cluster_11: 8.057
- **Magnitude:** 916.54 | **LOC:** 1685 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **57**; blast radius 0.355; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.2%), Connectivity (formerly Api Exposure) (45.8%), Complexity Load (formerly Cognitive Load) (42.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_buildRequest` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* /** * Creates a request object with the configured options and parameters. * * @param string $url Th...
  * `_addTokens` **(Many-Argument Workhorses)** (Impact: 26.4)
    * *Intent:* /** * Add the CSRF and FormProtectionComponent tokens if necessary. * * @param string $url The URL t...
  * `assertRedirectBack` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* /** * Assert whether the response is redirecting back to the previous location. * * @param int|null ...
  * `assertRedirectBackToReferer` **(Defensive Guards)** (Impact: 13.4)
    * *Intent:* /** * Assert whether the response is redirecting back to the referer. * * @param int|null $code Spec...
  * `_castToString` **(Stateful Encapsulated Methods)** (Impact: 12.4)
    * *Intent:* /** * Recursively casts all data to string as that is how data would be POSTed in * the real world *...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 141 instances
* *Memory Alloc (weighted view):* 59
* *State Mutation (weighted view):* 516
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 228`, `args: 81`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 234`, `planned_debt: 1`
* *Architecture:* `io: 20`, `api: 63`, `import: 57`
* *Defense:* `safety: 51`, `doc: 97`, `test: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.355
  * `Choke Point (Betweenness):` 6.4e-05 | `Ripple Effect (Closeness):` 0.001211
  * `Imports (Out-Degree: 51):` Cake\Controller\Controller, Cake\Core\Configure, Cake\Core\HttpApplicationInterface, Cake\Core\PluginApplicationInterface, Cake\Core\TestSuite\ContainerStubTrait, Cake\Database\Exception\DatabaseException, Cake\Error\Renderer\WebExceptionRenderer, Cake\Event\EventInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/TestCase/Collection/CollectionTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.798)
- **Top Global Matches:** file_cluster_12: 7.798, file_cluster_11: 8.283, file_cluster_10: 8.518
- **Magnitude:** 913.36 | **LOC:** 2826 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.8%), Connectivity (formerly Api Exposure) (12.5%), Concurrency Surface (formerly Concurrency) (12.3%), Complexity Load (formerly Cognitive Load) (10.1%)
- **Documentation Coverage:** 7.5658% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testCartesianProduct` **(I/O & Config Routines)** (Impact: 7.2)
    * *Intent:* /** * Tests cartesianProduct */
  * `testNestObjects` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* /** * Tests the nest method with more than one level */
  * `testNestObjectsAlternateNestingKey` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* /** * Tests the nest method with more than one level */
  * `testSample` **(Annotated & Test Methods)** (Impact: 3.3)
    * *Intent:* /** * Tests sample */
  * `testCombine` **(Callbacks & Closures)** (Impact: 3.3)
    * *Intent:* /** * Tests the combine method */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 556`, `args: 201`, `func_start: 152`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 431`, `unreferenced_by_name: 137`
* *Architecture:* `api: 150`, `concurrency: 1`, `import: 25`
* *Defense:* `safety: 5`, `doc: 143`, `test: 192`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` ArrayIterator, ArrayObject, Cake\Collection\Collection, Cake\Collection\Iterator\BufferedIterator, Cake\Collection\Iterator\ExtractIterator, Cake\Collection\Iterator\InsertIterator, Cake\Collection\Iterator\ReplaceIterator, Cake\Collection\collection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/TestCase/ORM/MarshallerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.218)
- **Top Global Matches:** file_cluster_11: 8.218, file_cluster_2: 8.867, file_cluster_15: 8.916
- **Magnitude:** 898.7 | **LOC:** 3666 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.257; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Connectivity (formerly Api Exposure) (10.4%), Complexity Load (formerly Cognitive Load) (8.3%)
- **Documentation Coverage:** 3.3493% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMergeBelongsToManyJoinData` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* /** * Test merging the _joinData entity for belongstomany associations. */
  * `testBeforeMarshalEventOnAssociations` **(I/O & Config Routines)** (Impact: 4.8)
    * *Intent:* /** * Test Model.beforeMarshal event on associated tables. */
  * `testMergeMultipleAssociations` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* /** * Tests merging one to many associations */
  * `testAfterMarshalEventOnPatchEntity` **(I/O & Config Routines)** (Impact: 4.5)
    * *Intent:* /** * Test Model.afterMarshal event on patchEntity. * when $options['fields'] is set and is empty */
  * `testBelongsToManyAddingNewExisting` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* /** * Test belongsToMany association with mixed data and _joinData */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 189
* *State Mutation (weighted view):* 481
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 358`, `args: 118`, `func_start: 106`, `class_start: 1`
* *Risk/State:* `state_mutation: 475`, `unreferenced_by_name: 105`
* *Architecture:* `api: 103`, `import: 14`
* *Defense:* `safety: 3`, `doc: 110`, `test: 336`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.257
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` Cake\Database\Expression\IdentifierExpression, Cake\Event\EventInterface, Cake\I18n\DateTime, Cake\ORM\Association, Cake\ORM\Entity, Cake\ORM\Marshaller, Cake\TestSuite\TestCase, Cake\Validation\Validator...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/View/View.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.026)
- **Top Global Matches:** file_cluster_15: 6.026, file_cluster_16: 6.607, file_cluster_11: 7.029
- **Magnitude:** 846.36 | **LOC:** 1715 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **26**; blast radius 1.963; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (89.2%), Guard Balance (formerly Safety Score) (73.0%), Complexity Load (formerly Cognitive Load) (44.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 31.0)
    * *Intent:* /** * Constructor * * @param \Cake\Http\ServerRequest|null $request Request instance. * @param \Cake...
  * `_getTemplateFileName` **(Stateful Encapsulated Methods)** (Impact: 29.2)
    * *Intent:* /** * Returns filename of given action's template file as a string. * CamelCased action names will b...
  * `_paths` **(Stateful Encapsulated Methods)** (Impact: 23.3)
    * *Intent:* /** * Return all possible paths to find view files in order * * @param string|null $plugin Optional ...
  * `extend` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** * Provides template or element extension/inheritance. Templates can extends a * parent template ...
  * `render` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* * * If View::$autoLayout is set to `false`, the template will be returned bare. * * Template and lay...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 134 instances
* *State Mutation (weighted view):* 445
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 203`, `args: 66`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 177`, `unreferenced_by_name: 34`
* *Architecture:* `api: 56`, `concurrency: 2`, `import: 29`
* *Defense:* `safety: 25`, `doc: 104`, `immutability_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.963
  * `Choke Point (Betweenness):` 0.000539 | `Ripple Effect (Closeness):` 0.024837
  * `Imports (Out-Degree: 15):` Cake\Cache\Cache, Cake\Core\App, Cake\Core\Exception\CakeException, Cake\Core\InstanceConfigTrait, Cake\Core\Plugin, Cake\Core\pluginSplit, Cake\Event\EventDispatcherInterface, Cake\Event\EventDispatcherTrait...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/View/Helper/HtmlHelper.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.991)
- **Top Global Matches:** file_cluster_4: 5.991, file_cluster_6: 10.837, file_cluster_9: 10.838
- **Magnitude:** 838.56 | **LOC:** 1204 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 0.357; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.0%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `meta` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* * * ### Options * * - `block` - Set to true to append output to view block "meta" or provide * custo...
  * `media` **(Many-Argument Workhorses)** (Impact: 31.3)
    * *Intent:* * ### Options * * - `tag` Type of media element to generate, either "audio" or "video". * If tag is ...
  * `tableCells` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /** * Returns a formatted string of table rows (TR's with TD's in them). * * @param array|string $da...
  * `css` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* * - `rel` Defaults to 'stylesheet'. If equal to 'import' the stylesheet will be imported. * - `fullB...
  * `link` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* * * - `escape` Set to false to disable escaping of title and attributes. * - `escapeTitle` Set to fa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 498
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 92`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 182`, `unreferenced_by_name: 8`
* *Architecture:* `api: 22`, `import: 6`
* *Defense:* `safety: 32`, `doc: 32`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.357
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.003028
  * `Imports (Out-Degree: 3):` Cake\Core\Configure, Cake\Core\h, Cake\Http\MimeType, Cake\View\Helper, Cake\View\StringTemplateTrait, StringTemplateTrait
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Database/Schema/MysqlSchemaDialect.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.501)
- **Top Global Matches:** file_cluster_4: 5.501, file_cluster_15: 9.056, file_cluster_16: 9.303
- **Magnitude:** 829.84 | **LOC:** 1077 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.504; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (85.2%), Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (70.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `columnDefinitionSql` **(Defensive Guards)** (Impact: 92.9)
    * *Intent:* /** * Create a SQL snippet for a column based on the array shape * that `describeColumns()` creates....
  * `_convertColumn` **(Compute Cores)** (Impact: 57.1)
    * *Intent:* /** * Convert a MySQL column type into an abstract type. * * The returned type will be a type that C...
  * `convertIndexDescription` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* /** * @inheritDoc */
  * `describeIndexes` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* /** * @inheritDoc */
  * `describeColumns` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* * - type : the abstract type of the column. * - length : the length of the column. * - default : the...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 142 instances
* *Api Near Db Sink:* 3 instances
* *State Mutation (weighted view):* 456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 102`, `args: 30`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 172`, `planned_debt: 2`, `unreferenced_by_name: 21`
* *Architecture:* `api: 23`, `import: 4`
* *Defense:* `safety: 53`, `doc: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.504
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.087009
  * `Imports (Out-Degree: 3):` Cake\Database\DriverFeatureEnum, Cake\Database\Driver\Mysql, Cake\Database\Exception\DatabaseException, PDOException
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Collection/CollectionTrait.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.13)
- **Top Global Matches:** file_cluster_15: 6.13, file_cluster_12: 6.79, file_cluster_11: 7.595
- **Magnitude:** 818.8 | **LOC:** 1244 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **28**; blast radius 1.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Connectivity (formerly Api Exposure) (74.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cartesianProduct` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* /** * {@inheritDoc} * * @param callable|null $operation A callable that allows you to customize the ...
  * `combine` **(Many-Argument Workhorses)** (Impact: 21.4)
    * *Intent:* /** * {@inheritDoc} * * @return \Cake\Collection\CollectionInterface<mixed, mixed> */
  * `nest` **(Many-Argument Workhorses)** (Impact: 18.3)
    * *Intent:* /** * {@inheritDoc} * * @return \Cake\Collection\CollectionInterface<TKey, TValue> */
  * `takeLast` **(Compute Cores)** (Impact: 16.1)
    * *Intent:* /** * {@inheritDoc} * * @return \Cake\Collection\CollectionInterface<TKey, TValue> */
  * `groupBy` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* * ['id' => 3, 'name' => 'baz', 'parent_id' => 10], * ], * 11 => [ * ['id' => 2, 'name' => 'bar', 'pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 135 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 259`, `args: 77`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 171`
* *Architecture:* `api: 56`, `concurrency: 3`, `import: 28`
* *Defense:* `safety: 19`, `doc: 69`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.494
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.003524
  * `Imports (Out-Degree: 15):` AppendIterator, ArrayIterator, BackedEnum, Cake\Collection\Iterator\BufferedIterator, Cake\Collection\Iterator\ExtractIterator, Cake\Collection\Iterator\FilterIterator, Cake\Collection\Iterator\InsertIterator, Cake\Collection\Iterator\MapReduce...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Http/ServerRequest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.781)
- **Top Global Matches:** file_cluster_15: 5.781, file_cluster_11: 6.85, file_cluster_16: 7.109
- **Magnitude:** 818.2 | **LOC:** 1840 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **64** in-repo importer(s); it depends on **16**; blast radius 3.33; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.7%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (33.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_setConfig` **(Defensive Guards)** (Impact: 19.8)
    * *Intent:* /** * Process the config/settings data into properties. * * @param array<string, mixed> $config The ...
  * `_is` **(Stateful Encapsulated Methods)** (Impact: 18.5)
    * *Intent:* /** * Worker for the public is() function * * @param string $type The type of request you want to ch...
  * `referer` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Returns the referer that referred this request. * * @param bool $local Attempt to return a loc...
  * `is` **(Defensive Guards)** (Impact: 13.2)
    * *Intent:* /** * Check whether a Request is a certain type. * * Uses the built-in detection rules as well as ad...
  * `clientIp` **(I/O & Config Routines)** (Impact: 11.4)
    * *Intent:* /** * Get the IP the client is using, or says they are using. * * @return string The client IP. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 114 instances
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 258`, `args: 74`, `func_start: 74`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 172`, `unreferenced_by_name: 54`
* *Architecture:* `io: 8`, `api: 66`, `import: 16`
* *Defense:* `safety: 32`, `doc: 97`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.33
  * `Choke Point (Betweenness):` 0.003483 | `Ripple Effect (Closeness):` 0.109942
  * `Imports (Out-Degree: 10):` BadMethodCallException, Cake\Core\Configure, Cake\Core\Exception\CakeException, Cake\Core\deprecationWarning, Cake\Core\env, Cake\Http\Cookie\CookieCollection, Cake\Http\Exception\MethodNotAllowedException, Cake\Utility\Hash...
  * `Imported By (In-Degree: 64):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/TestCase/Cache/Engine/CacheEngineTest.php` (PHP) | Magnitude: 8.14 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 14, test: 5, import: 4
- `tests/TestCase/Command/PluginListCommandTest.php` (PHP) | Magnitude: 48.04 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 21, state_mutation: 15, bitwise_ops: 14
- `tests/TestCase/Http/ServerRequestFactoryTest.php` (PHP) | Magnitude: 219.28 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1162, test: 127, state_mutation: 93, structural_boundaries: 56
- `src/TestSuite/Constraint/EventFired.php` (PHP) | Magnitude: 17.16 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 13, doc: 6, args: 3
- `tests/TestCase/Datasource/Paging/PaginatorTestTrait.php` (PHP) | Magnitude: 354.2 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 957, state_mutation: 193, structural_boundaries: 81, test: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/TestCase/Database/Expression/QueryExpressionTest.php` (PHP) | Magnitude: 93.1 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 80, memory_alloc: 50, state_mutation: 46
- `tests/TestCase/Utility/FilesystemTest.php` (PHP) | Magnitude: 27.96 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 14, state_mutation: 12, test: 10
- `src/Core/StaticConfigTrait.php` (PHP) | Magnitude: 132.7 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 33, branch: 28, state_mutation: 22
- `src/ORM/Rule/IsUnique.php` (PHP) | Magnitude: 51.52 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 13, state_mutation: 13, doc: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Http/TestSuite/HttpClientTrait.php` (PHP) | Magnitude: 31.36 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 15, state_mutation: 9, doc: 9
- `src/ORM/Attribute/CollectionOf.php` (PHP) | Magnitude: 3.84 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 4, doc: 3, api: 2
- `tests/TestCase/Http/SessionTest.php` (PHP) | Magnitude: 191.28 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 458, structural_boundaries: 98, test: 85, state_mutation: 73
- `tests/TestCase/I18n/PluralRulesTest.php` (PHP) | Magnitude: 8.9 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 10, test: 5, doc: 4
- `tests/TestCase/Utility/InflectorTest.php` (PHP) | Magnitude: 69.18 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 415, test: 99, structural_boundaries: 29, doc: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Core/BasePlugin.php` (PHP) | Magnitude: 132.5 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 50, doc: 30, state_mutation: 26
- `src/Database/Expression/CommonTableExpression.php` (PHP) | Magnitude: 108.8 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 39, state_mutation: 24, doc: 20
- `src/TestSuite/Constraint/Email/MailSentWith.php` (PHP) | Magnitude: 37.88 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 13, branch: 9, doc: 6
- `src/Database/Driver.php` (PHP) | Magnitude: 409.5 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 482, structural_boundaries: 182, doc: 76, branch: 69
- `src/Command/CacheClearGroupCommand.php` (PHP) | Magnitude: 39.08 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 21, branch: 9, doc: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/TestCase/Database/QueryTests/TupleComparisonQueryTest.php` (PHP) | Magnitude: 63.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 38, state_mutation: 20, memory_alloc: 13
- `src/ORM/BehaviorRegistry.php` (PHP) | Magnitude: 142.12 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 51, state_mutation: 30, doc: 21
- `src/Database/Expression/TupleComparison.php` (PHP) | Magnitude: 146.28 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 119, structural_boundaries: 35, branch: 30, state_mutation: 28
- `tests/TestCase/ORM/Behavior/CounterCacheBehaviorTest.php` (PHP) | Magnitude: 161.9 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 475, state_mutation: 84, test: 69, structural_boundaries: 59
- `src/View/Widget/BasicWidget.php` (PHP) | Magnitude: 108.64 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 21, branch: 20, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/TestCase/View/Helper/BreadcrumbsHelperTest.php` (PHP) | Magnitude: 122.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 602, structural_boundaries: 100, state_mutation: 40, ui_framework: 25
- `src/View/Widget/TextareaWidget.php` (PHP) | Magnitude: 16.68 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, doc: 4, branch: 3
- `tests/test_app/TestApp/Model/Entity/NonExtending.php` (PHP) | Magnitude: 14.78 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 8, branch: 4, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Console/ConsoleOptionParser.php` (PHP) | Magnitude: 507.78 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 439, state_mutation: 103, structural_boundaries: 91, branch: 86

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `templates/element/exception_stack_trace_nav.php` (PHP) | Magnitude: 24.74 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, branch: 10, core_var_decl: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/test_app/TestApp/Controller/UnionDependenciesController.php` (PHP) | Magnitude: 44.24 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 13, state_mutation: 7, branch: 6
- `src/View/XmlView.php` (PHP) | Magnitude: 63.24 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 52, branch: 14, structural_boundaries: 14, state_mutation: 14
- `src/Database/Query/UpdateQuery.php` (PHP) | Magnitude: 63.26 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 18, state_mutation: 14, doc: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/ORM/Table.php` -> Churn: **82.57%** | Cog Load: 44.521% | Debt: 62.2803%
- `src/Database/Schema/MysqlSchemaDialect.php` -> Churn: **66.94%** | Cog Load: 52.2895% | Debt: 85.1587%
- `src/Http/Response.php` -> Churn: **61.61%** | Cog Load: 31.9884% | Debt: 95.1204%
- `src/ORM/Behavior/TranslateBehavior.php` -> Churn: **60.48%** | Cog Load: 29.511% | Debt: 95.5022%
- `Makefile` -> Churn: **56.16%** | Cog Load: 12.3907% | Debt: 88.8959%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/TestCase/Collection/CollectionTest.php` -> **mscherer** (100.0% isolated ownership) | Magnitude: 913.36
- `tests/TestCase/View/Helper/HtmlHelperTest.php` -> **scribblemaniac** (100.0% isolated ownership) | Magnitude: 750.36
- `tests/TestCase/View/ViewTest.php` -> **Mark Scherer** (100.0% isolated ownership) | Magnitude: 627.7
- `src/Error/Debugger.php` -> **Mark Scherer** (100.0% isolated ownership) | Magnitude: 585.88
- `src/Routing/RouteBuilder.php` -> **ADmad** (100.0% isolated ownership) | Magnitude: 531.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/TestSuite/TestCase.php` -> **Severity: 2.266** (Bridge: 0.0227 * Flux: 100.0%)
- `src/ORM/Table.php` -> **Severity: 1.369** (Bridge: 0.0137 * Flux: 100.0%)
- `src/Datasource/ConnectionManager.php` -> **Severity: 0.925** (Bridge: 0.0093 * Flux: 100.0%)
- `src/Core/Configure.php` -> **Severity: 0.613** (Bridge: 0.0061 * Flux: 100.0%)
- `src/Cache/Cache.php` -> **Severity: 0.578** (Bridge: 0.0068 * Flux: 84.9999%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Core/Exception/CakeException.php` -> **Severity: 17.633** (Embedded: 0.2994 * Error Risk: 58.904%)
- `src/TestSuite/TestCase.php` -> **Severity: 16.161** (Embedded: 0.2199 * Error Risk: 73.5047%)
- `src/Utility/Hash.php` -> **Severity: 15.516** (Embedded: 0.1879 * Error Risk: 82.5748%)
- `src/Core/Configure.php` -> **Severity: 14.056** (Embedded: 0.2112 * Error Risk: 66.5397%)
- `src/Utility/Text.php` -> **Severity: 12.957** (Embedded: 0.1488 * Error Risk: 87.0672%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/test_app/TestApp/Http/TestRequestHandler.php` -> **Severity: 64.1** (Blast Radius: 0.641 * Doc Risk: 100.0%)
- `tests/TestCase/Cache/Engine/EngineEventsTrait.php` -> **Severity: 54.4** (Blast Radius: 0.544 * Doc Risk: 100.0%)
- `tests/test_app/TestApp/Database/ColumnSchemaAwareTypeValueObject.php` -> **Severity: 39.5** (Blast Radius: 0.395 * Doc Risk: 100.0%)
- `tests/test_app/TestApp/Command/DemoCommand.php` -> **Severity: 38.6** (Blast Radius: 0.386 * Doc Risk: 100.0%)
- `tests/test_app/TestApp/Datasource/FakeConnection.php` -> **Severity: 37.164** (Blast Radius: 0.511 * Doc Risk: 72.7273%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 59275 call pairs -- scoped 39.6%, unique 0.3%, ambiguous 26.7%, external 33.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 58326 | 39.8% | 0.3% | 27.0% | 32.9% |
| python | 948 | 23.5% | 0.0% | 7.7% | 68.8% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
