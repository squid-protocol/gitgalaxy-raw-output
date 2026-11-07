# ARCHITECTURAL_BRIEF: laravel_core
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/laravel/framework.git` |
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
- **Scope:** 3075 analyzed artifact(s), 335515 LOC.
- **Load-bearing artifact:** `src/Illuminate/Database/Eloquent/Model.php` -- 274 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Illuminate/Foundation/Providers/ArtisanServiceProvider.php` -- pulls in 114 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/Foundation/fixtures/.env` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 3275 |
| Analyzed Artifacts (Scanned) | 3075 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 200 |
| Total LOC | 335515 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 93.9% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5474 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1459 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 7.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1719 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 221 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 2928 | 329175 | 95.2% |
| MARKDOWN | 46 | 0 | 1.5% |
| JSON | 46 | 4596 | 1.5% |
| YAML | 40 | 1202 | 1.3% |
| SHELL | 4 | 174 | 0.1% |
| PLAINTEXT | 3 | 1 | 0.1% |
| JAVASCRIPT | 3 | 102 | 0.1% |
| CSS | 2 | 265 | 0.1% |
| XML | 2 | 0 | 0.1% |
| SQLITE | 1 | 0 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 3074 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 17%, Data / Markup / Trivial 16%, Parameter Forwarders Files 16%, Encapsulated Accessors Files 12%, Large Core Modules (3) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3026 | 98.4% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 48 | 1.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 200*

**Composition by Extension & Reason:**
- `.stub`: 87x Unsupported Format (.stub)
- `no_extension`: 35x Unsupported Format (.undeterminable), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.php`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 9 exceeds 500 chars), 1x Excluded (Saturation: Line 10 exceeds 500 chars)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Statistical Anomaly (Z-Score: -12971.15 < -4.55), 1x Statistical Anomaly (Z-Score: -25499.39 < -4.55)
- `.png`: 7x Excluded (Explicitly Denied Extension: '.png')
- `.dist`: 2x Unsupported Format (.dist), 1x Excluded (Unsupported Extension: '.dist')
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sqlite`: 1x Excluded (Unsupported Extension: '.sqlite')
- `.gz`: 1x Excluded (Explicitly Denied Extension: '.gz')
- `.pdf`: 1x Excluded (Explicitly Denied Extension: '.pdf')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 75.5 | 8.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.3 | 39.8 | 50.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 5.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.9 | 8.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.2 | 11.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 38.9 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.7 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 35.5 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16941 | 1460 | 12 | `tests/Validation/ValidationValidatorTest.php` |
| cleanup | 349 | 150 | 0 | `tests/Events/EventsDispatcherTest.php` |
| guards | 16501 | 1765 | 14 | `tests/Testing/Fluent/AssertTest.php` |
| danger | 5071 | 757 | 3 | `tests/Database/DatabaseEloquentIntegrationTest.php` |
| concurrency | 1229 | 176 | 0 | `tests/Integration/Cache/PhpRedisCacheLockTest.php` |
| connectivity | 28202 | 2507 | 20 | `tests/Database/DatabaseQueryBuilderTest.php` |
| io | 690 | 155 | 0 | `tests/Filesystem/FilesystemTest.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 114 | 27 | 0 | `src/Illuminate/Collections/LazyCollection.php` |
| time | 260 | 65 | 0 | `tests/Validation/ValidationValidatorTest.php` |
| serialization | 957 | 233 | 0 | `tests/Integration/Queue/ModelSerializationTest.php` |
| regex | 254 | 108 | 0 | `src/Illuminate/Support/Str.php` |
| events | 1790 | 246 | 0 | `tests/Events/EventsDispatcherTest.php` |
| tests | 31346 | 1018 | 21 | `tests/Validation/ValidationValidatorTest.php` |
| docs | 17671 | 1741 | 14 | `src/Illuminate/Support/Facades/Redis.php` |
| debt | 1781 | 302 | 0 | `src/Illuminate/Foundation/Console/StubPublishCommand.php` |
| mutation | 48776 | 2246 | 34 | `tests/Validation/ValidationValidatorTest.php` |
| dead_code | 14147 | 1231 | 10 | `tests/Database/DatabaseQueryBuilderTest.php` |
| credential | 114 | 15 | 0 | `src/Illuminate/Foundation/resources/exceptions/renderer/package-lock.json` |
| threat | 116 | 35 | 0 | `tests/Http/Middleware/TrimStringsTest.php` |
| ml_ai | 246 | 62 | 0 | `tests/Support/SupportConditionableTest.php` |
| ui | 1001 | 257 | 0 | `tests/Integration/View/BladeTest.php` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/Filesystem/FilesystemTest.php` (Hits: 61)
- `tests/Http/Middleware/TrustProxiesTest.php` (Hits: 51)
- `tests/Http/HttpClientTest.php` (Hits: 49)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Model.php** (`src/Illuminate/Database/Eloquent/Model.php`) — 274 inbound connections
2. **helpers.php** (`src/Illuminate/Support/helpers.php`) — 254 inbound connections
3. **Str.php** (`src/Illuminate/Support/Str.php`) — 243 inbound connections
4. **helpers.php** (`src/Illuminate/Foundation/helpers.php`) — 213 inbound connections
5. **Arr.php** (`src/Illuminate/Collections/Arr.php`) — 182 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ArtisanServiceProvider.php** (`src/Illuminate/Foundation/Providers/ArtisanServiceProvider.php`) — 114 outbound dependencies
2. **DatabaseEloquentModelTest.php** (`tests/Database/DatabaseEloquentModelTest.php`) — 66 outbound dependencies
3. **rector.php** (`rector.php`) — 55 outbound dependencies
4. **HttpClientTest.php** (`tests/Http/HttpClientTest.php`) — 53 outbound dependencies
5. **Handler.php** (`src/Illuminate/Foundation/Exceptions/Handler.php`) — 51 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getPluralIndex` **(Compute Cores)** (@ `src/Illuminate/Translation/MessageSelector.php`) -> Impact: **597.1** | LOC: 302
  * *Intent:* /** * Get the index to use for pluralization. * * The plural rules are derived from code of the Zend Framework (2010-09-25), which * is subject to the...
- `buildRoutingCallback` **(Many-Argument Workhorses)** (@ `src/Illuminate/Foundation/Configuration/ApplicationBuilder.php`) -> Impact: **72.6** | LOC: 77
  * *Intent:* /** * Create the routing callback for the application. * * @param array|string|null $web * @param array|string|null $api * @param string|null $pages *...
- `formatParameters` **(Many-Argument Workhorses)** (@ `src/Illuminate/Routing/RouteUrlGenerator.php`) -> Impact: **67.0** | LOC: 127
  * *Intent:* /** * Format the array of route parameters. * * @param \Illuminate\Routing\Route $route * @param mixed $parameters * @return array */
- `withRouting` **(Many-Argument Workhorses)** (@ `src/Illuminate/Foundation/Configuration/ApplicationBuilder.php`) -> Impact: **64.9** | LOC: 34
  * *Intent:* /** * Register the routing services for the application. * * @param \Closure|null $using * @param array|string|null $web * @param array|string|null $a...
- `update` **(Compute Cores)** (@ `src/Illuminate/Database/Schema/BlueprintState.php`) -> Impact: **61.2** | LOC: 93
  * *Intent:* /** * Update the blueprint's state. * * @param \Illuminate\Support\Fluent $command * @return void */
- `queueNotification` **(Defensive Guards)** (@ `src/Illuminate/Notifications/NotificationSender.php`) -> Impact: **57.5** | LOC: 77
  * *Intent:* /** * Queue the given notification instances. * * @param mixed $notifiables * @param \Illuminate\Notifications\Notification $notification * @return vo...
- `castAttribute` **(Many-Argument Workhorses)** (@ `src/Illuminate/Database/Eloquent/Concerns/HasAttributes.php`) -> Impact: **51.7** | LOC: 64
  * *Intent:* /** * Cast an attribute to a native PHP type. * * @param string $key * @param mixed $value * @return mixed */
- `__construct` **(Many-Argument Workhorses)** (@ `src/Illuminate/Database/Eloquent/Factories/Factory.php`) -> Impact: **50.9** | LOC: 24
  * *Intent:* /** * Create a new factory instance. * * @param int|null $count * @param \Illuminate\Support\Collection|null $states * @param \Illuminate\Support\Coll...
- `send` **(Defensive Guards)** (@ `src/Illuminate/Http/Client/PendingRequest.php`) -> Impact: **50.0** | LOC: 81
  * *Intent:* /** * Send the request to the given URL. * * @param string $method * @param string $url * @param array $options * @return \Illuminate\Http\Client\Resp...
- `data_set` **(Many-Argument Workhorses)** (@ `src/Illuminate/Collections/helpers.php`) -> Impact: **49.5** | LOC: 50
  * *Intent:* /** * Set an item on an array or object using dot notation. * * @param mixed $target * @param string|array $key * @param mixed $value * @param bool $o...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/Database` | 128 | 19299.66 | 5.81% | 0.0% |
| `tests/Support` | 53 | 8210.64 | 4.01% | 0.0% |
| `tests/Integration/Database` | 100 | 6358.62 | 3.78% | 0.0% |
| `tests/Validation` | 37 | 5837.32 | 4.4% | 0.0% |
| `src/Illuminate/Collections` | 11 | 5344.25 | 19.4% | 43.28% |
| `src/Illuminate/Support` | 41 | 5087.44 | 26.14% | 5.2% |
| `tests/Foundation/fixtures` | 13 | 5000.15 | 0.41% | 0.0% |
| `src/Illuminate/Routing` | 38 | 4255.38 | 22.86% | 17.33% |
| `src/Illuminate/Foundation/Console` | 68 | 3420.62 | 15.34% | 36.03% |
| `src/Illuminate/Database/Eloquent` | 24 | 3409.54 | 14.44% | 6.5% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Illuminate/Foundation/Console/StubPublishCommand.php` -> **100.0%** Exposure
- `src/Illuminate/Database/Schema/ForeignKeyDefinition.php` -> **99.9999%** Exposure
- `src/Illuminate/Cache/RedisLock.php` -> **99.999%** Exposure
- `src/Illuminate/Database/DatabaseTransactionRecord.php` -> **99.999%** Exposure
- `src/Illuminate/Process/InvokedProcess.php` -> **99.9989%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/Illuminate/Auth/Passwords/PasswordBroker.php` -> **100.0%** Exposure
- `src/Illuminate/Auth/TokenGuard.php` -> **100.0%** Exposure
- `src/Illuminate/Bus/Batchable.php` -> **100.0%** Exposure
- `src/Illuminate/Bus/DebounceLock.php` -> **100.0%** Exposure
- `src/Illuminate/Bus/Dispatcher.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/Database/DatabaseQueryBuilderTest.php` -> **452** Orphaned Functions | **2** Duplicates
- `tests/Support/SupportCollectionTest.php` -> **391** Orphaned Functions | **0** Duplicates
- `tests/Validation/ValidationValidatorTest.php` -> **288** Orphaned Functions | **33** Duplicates
- `tests/Database/DatabaseEloquentModelTest.php` -> **261** Orphaned Functions | **8** Duplicates
- `tests/Http/HttpClientTest.php` -> **255** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/Integration/Database/EloquentModelEncryptedDirtyTest.php` -> **100.0%** Exposure
- `tests/Integration/Foundation/CloudTest.php` -> **99.9993%** Exposure
- `tests/Support/ConfigurationUrlParserTest.php` -> **99.4941%** Exposure
- `tests/Broadcasting/PusherBroadcasterTest.php` -> **87.0113%** Exposure
- `tests/Queue/QueueSqsJobTest.php` -> **74.9953%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `13534` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/Foundation/fixtures/.env` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Validation/ValidationValidatorTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 11.203)
- **Top Global Matches:** file_cluster_11: 11.203, file_cluster_15: 11.491, file_cluster_12: 11.721
- **Magnitude:** 3692.06 | **LOC:** 10299 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 26.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.183; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.6%), Guard Balance (formerly Safety Score) (52.6%), Complexity Load (formerly Cognitive Load) (29.5%), Connectivity (formerly Api Exposure) (12.1%)
- **Documentation Coverage:** 99.7085% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testCustomValidationObject` **(I/O & Config Routines)** (Impact: 25.2)
  * `testValidateDecimal` **(I/O & Config Routines)** (Impact: 10.2)
  * `testItemAwareSometimesAddingRules` **(Callbacks & Closures)** (Impact: 10.0)
  * `testCapitalizedDisplayableValuesAreReplaced` **(I/O & Config Routines)** (Impact: 8.5)
  * `testValidateImageDimensions` **(I/O & Config Routines)** (Impact: 7.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 1655
* *State Mutation (weighted view):* 2315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 2298`, `args: 420`, `func_start: 344`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 2301`, `dead_code: 9`, `fragile_debt: 1`, `duplicate_logic: 33`, `unreferenced_by_name: 288`
* *Architecture:* `api: 347`, `import: 41`
* *Defense:* `safety: 10`, `doc: 1`, `test: 1948`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.183
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.000324
  * `Imports (Out-Degree: 26):` Countable, DateTime, DateTimeImmutable, Egulias\EmailValidator\Validation\NoRFCWarningsValidation, Illuminate\Container\Container, Illuminate\Contracts\Auth\Authenticatable, Illuminate\Contracts\Auth\Guard, Illuminate\Contracts\Hashing\Hasher...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Database/DatabaseQueryBuilderTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.859)
- **Top Global Matches:** file_cluster_10: 6.859, file_cluster_11: 7.191, file_cluster_2: 8.517
- **Magnitude:** 2788.12 | **LOC:** 7703 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 12.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **36**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.9%), Guard Balance (formerly Safety Score) (59.2%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 99.8911% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testDeleteWithJoinMethod` **(I/O & Config Routines)** (Impact: 4.6)
  * `testWhereBetweens` **(I/O & Config Routines)** (Impact: 4.3)
  * `testAggregateFunctions` **(Callbacks & Closures)** (Impact: 4.0)
  * `testWhereExists` **(Callbacks & Closures)** (Impact: 3.8)
  * `testCursorPaginateWithUnionMultipleWheresMultipleOrders` **(Callbacks & Closures)** (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1318`, `args: 692`, `func_start: 464`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 140`, `state_mutation: 1397`, `duplicate_logic: 2`, `unreferenced_by_name: 452`
* *Architecture:* `api: 454`, `import: 37`
* *Defense:* `safety: 13`, `doc: 1`, `test: 1361`, `sync_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` BadMethodCallException, Closure, DateInterval, DatePeriod, DateTime, Enums.php, Illuminate\Contracts\Database\Query\ConditionExpression, Illuminate\Database\Connection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Illuminate/Database/Query/Builder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.67)
- **Top Global Matches:** file_cluster_15: 6.67, file_cluster_16: 7.532, file_cluster_12: 8.356
- **Magnitude:** 2432.46 | **LOC:** 4951 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 13.3%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **35**; blast radius 2.464; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `where` **(Many-Argument Workhorses)** (Impact: 45.2)
    * *Intent:* /** * Add a basic "where" clause to the query. * * @param \Closure|string|array|\Illuminate\Contract...
  * `upsert` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* /** * Insert new records or update the existing ones. * * @param non-empty-string|non-empty-array<in...
  * `insertOrIgnoreReturning` **(Defensive Guards)** (Impact: 19.8)
    * *Intent:* /** * Insert new records into the database and returning specified columns with optional ignoring sp...
  * `having` **(Many-Argument Workhorses)** (Impact: 17.8)
    * *Intent:* /** * Add a "having" clause to the query. * * @param \Illuminate\Contracts\Database\Query\Expression...
  * `addSelect` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* /** * Add a new select column to the query. * * @param mixed $column * @return $this */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 284 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1029
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 296`, `structural_boundaries: 717`, `args: 280`, `func_start: 259`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 461`
* *Architecture:* `api: 259`, `concurrency: 1`, `import: 31`
* *Defense:* `safety: 103`, `doc: 289`, `sync_locks: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.464
  * `Choke Point (Betweenness):` 0.006467 | `Ripple Effect (Closeness):` 0.149439
  * `Imports (Out-Degree: 28):` BackedEnum, BuildsQueries, BuildsWhereDateClauses, Closure, DatePeriod, DateTimeInterface, ExplainsQueries, ForwardsCalls...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `tests/Support/SupportCollectionTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.351)
- **Top Global Matches:** file_cluster_12: 9.351, file_cluster_13: 9.612, file_cluster_10: 9.708
- **Magnitude:** 2331.68 | **LOC:** 6400 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.4%), Complexity Load (formerly Cognitive Load) (15.5%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 99.7576% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testWhere` **(I/O & Config Routines)** (Impact: 7.4)
  * `testSortByMany` **(I/O & Config Routines)** (Impact: 4.9)
  * `testContains` **(Annotated & Test Methods)** (Impact: 4.3)
  * `testDoesntContain` **(Annotated & Test Methods)** (Impact: 4.3)
  * `testNewInstanceIsUsedByCollectionMethods` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *Memory Alloc (weighted view):* 146
* *State Mutation (weighted view):* 942
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 1519`, `args: 621`, `func_start: 412`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 924`, `unreferenced_by_name: 391`
* *Architecture:* `api: 416`, `import: 32`
* *Defense:* `safety: 71`, `doc: 1`, `test: 1053`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ArrayAccess, ArrayIterator, ArrayObject, CachingIterator, Common.php, Enums.php, Exception, Illuminate\Contracts\Support\Arrayable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Database/DatabaseEloquentModelTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 7.404)
- **Top Global Matches:** file_cluster_11: 7.404, file_cluster_12: 7.925, file_cluster_15: 8.261
- **Magnitude:** 1908.88 | **LOC:** 4789 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 46.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **66**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (53.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.8%), Complexity Load (formerly Cognitive Load) (25.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set` **(Defensive Guards)** (Impact: 7.1)
  * `__construct` **(Compute Cores)** (Impact: 5.4)
  * `castUsing` **(Defensive Guards)** (Impact: 5.3)
  * `testRelationsWithVariedConnections` **(I/O & Config Routines)** (Impact: 5.0)
  * `set` **(Parameter Forwarders)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 37 instances
* *Memory Alloc (weighted view):* 250
* *State Mutation (weighted view):* 948
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 886`, `args: 342`, `func_start: 322`, `class_start: 69`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 874`, `dead_code: 72`, `planned_debt: 11`, `duplicate_logic: 8`, `unreferenced_by_name: 261`
* *Architecture:* `api: 332`, `import: 69`
* *Defense:* `safety: 60`, `test: 617`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` DateTime, DateTimeImmutable, DateTimeInterface, EloquentTraitBootingCallbackTestStub, Enums.php, Exception, FooBarTrait, Foo\Bar\EloquentModelNamespacedStub...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Illuminate/Collections/Enumerable.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.351)
- **Top Global Matches:** file_cluster_2: 5.351, file_cluster_17: 5.551, file_cluster_11: 5.713
- **Magnitude:** 1829.99 | **LOC:** 1362 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 0.291; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (75.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 134
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 158`, `args: 148`, `func_start: 148`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`
* *Architecture:* `api: 148`, `import: 7`
* *Defense:* `safety: 1`, `doc: 149`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.291
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.123158
  * `Imports (Out-Degree: 2):` CachingIterator, Countable, Illuminate\Contracts\Support\Arrayable, Illuminate\Contracts\Support\Jsonable, IteratorAggregate, JsonSerializable, Traversable
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Illuminate/Validation/Concerns/ValidatesAttributes.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.608)
- **Top Global Matches:** file_cluster_15: 6.608, file_cluster_12: 6.717, file_cluster_16: 6.979
- **Magnitude:** 1365.32 | **LOC:** 2957 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 17.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **27**; blast radius 0.177; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.0%), Connectivity (formerly Api Exposure) (53.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `failsBasicDimensionChecks` **(Stateful Encapsulated Methods)** (Impact: 24.4)
    * *Intent:* /** * Test if the given width and height fail any conditions. * * @param array<string,string> $param...
  * `validateGt` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /** * Validate that an attribute is greater than another attribute. * * @param string $attribute * @...
  * `validateGte` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /** * Validate that an attribute is greater than or equal another attribute. * * @param string $attr...
  * `validateLt` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* /** * Validate that an attribute is less than another attribute. * * @param string $attribute * @par...
  * `validateLte` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* /** * Validate that an attribute is less than or equal another attribute. * * @param string $attribu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 500`, `args: 154`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 100`
* *Architecture:* `api: 117`, `import: 27`
* *Defense:* `safety: 113`, `doc: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.177
  * `Choke Point (Betweenness):` 0.000616 | `Ripple Effect (Closeness):` 0.056766
  * `Imports (Out-Degree: 14):` Brick\Math\BigDecimal, Brick\Math\BigNumber, Brick\Math\Exception\MathException, DateTime, DateTimeInterface, DateTimeZone, Egulias\EmailValidator\EmailValidator, Egulias\EmailValidator\Validation\DNSCheckValidation...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Database/DatabaseEloquentBuilderTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 8.073)
- **Top Global Matches:** file_cluster_11: 8.073, file_cluster_10: 8.488, file_cluster_15: 9.046
- **Magnitude:** 1363.44 | **LOC:** 3282 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 37.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Guard Balance (formerly Safety Score) (58.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.2%), Complexity Load (formerly Cognitive Load) (28.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testEagerLoadParsingSetsProperRelationships` **(I/O & Config Routines)** (Impact: 3.7)
  * `testWhereBelongsTo` **(I/O & Config Routines)** (Impact: 3.6)
  * `testPassthruArrayElementsMustAllBeLowercase` **(Interface Declarations)** (Impact: 3.2)
  * `testIncrementEachCallsToBaseWithUpdatedAt` **(Callbacks & Closures)** (Impact: 3.1)
  * `testDecrementEachCallsToBaseWithUpdatedAt` **(Callbacks & Closures)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 6 instances
* *Memory Alloc (weighted view):* 275
* *State Mutation (weighted view):* 699
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 759`, `args: 311`, `func_start: 232`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 6`, `state_mutation: 687`, `duplicate_logic: 6`, `unreferenced_by_name: 209`
* *Architecture:* `io: 2`, `api: 227`, `import: 23`
* *Defense:* `safety: 3`, `test: 338`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` BadMethodCallException, Closure, Illuminate\Database\Connection, Illuminate\Database\ConnectionInterface, Illuminate\Database\ConnectionResolverInterface, Illuminate\Database\Eloquent\Builder, Illuminate\Database\Eloquent\Collection, Illuminate\Database\Eloquent\Model...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Http/HttpClientTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.301)
- **Top Global Matches:** file_cluster_10: 7.301, file_cluster_11: 8.322, file_cluster_15: 8.92
- **Magnitude:** 1358.18 | **LOC:** 4906 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 21.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.5%), Guard Balance (formerly Safety Score) (47.8%), Connectivity (formerly Api Exposure) (12.8%), Complexity Load (formerly Cognitive Load) (8.3%)
- **Documentation Coverage:** 99.8092% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testHeaderValuesAreSerialized` **(I/O & Config Routines)** (Impact: 12.6)
  * `testCanAssertAgainstOrderOfHttpRequestsWithCallablesAndHeadersFailsCorrectly` **(I/O & Config Routines)** (Impact: 10.9)
  * `testCanAssertAgainstOrderOfHttpRequestsWithCallablesAndHeaders` **(I/O & Config Routines)** (Impact: 10.8)
  * `testCanSendMultipartDataWithFileAndArrayValues` **(I/O & Config Routines)** (Impact: 10.2)
  * `testMultipartHeaderValuesAreSerialized` **(I/O & Config Routines)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 808`, `args: 472`, `func_start: 264`, `class_start: 4`
* *Risk/State:* `state_mutation: 385`, `unreferenced_by_name: 255`
* *Architecture:* `io: 49`, `api: 261`, `import: 53`
* *Defense:* `safety: 112`, `doc: 2`, `test: 339`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` Exception, GuzzleHttp\Client, GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\Middleware, GuzzleHttp\Promise\Create, GuzzleHttp\Promise\PromiseInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Illuminate/Collections/LazyCollection.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.445)
- **Top Global Matches:** file_cluster_12: 7.445, file_cluster_15: 8.39, file_cluster_10: 8.742
- **Magnitude:** 1283.14 | **LOC:** 1977 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 15.8%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **15**; blast radius 0.941; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `chunk` **(Compute Cores)** (Impact: 19.2)
    * *Intent:* /** * Chunk the collection into chunks of the given size. * * @param int $size * @param bool $preser...
  * `select` **(Defensive Guards)** (Impact: 18.4)
    * *Intent:* /** * Select specific values from the items within the collection. * * @param \Illuminate\Support\En...
  * `sliding` **(Compute Cores)** (Impact: 15.7)
    * *Intent:* /** * Create chunks representing a "sliding window" view of the items in the collection. * * @param ...
  * `only` **(Defensive Guards)** (Impact: 15.5)
    * *Intent:* /** * Get the items with the specified keys. * * @param \Illuminate\Support\Enumerable<array-key, TK...
  * `pluck` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* /** * Get the values of a given key. * * @param string|array<array-key, string> $value * @param stri...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 144 instances
* *High Risk Execution (weighted view):* 36
* *Concurrency (weighted view):* 158
* *Memory Alloc (weighted view):* 60
* *State Mutation (weighted view):* 463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 488`, `args: 155`, `func_start: 109`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 37`, `state_mutation: 175`, `unreferenced_by_name: 85`
* *Architecture:* `api: 102`, `concurrency: 48`, `import: 14`
* *Defense:* `safety: 35`, `doc: 118`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.941
  * `Choke Point (Betweenness):` 0.000275 | `Ripple Effect (Closeness):` 0.140557
  * `Imports (Out-Degree: 7):` ArrayIterator, Closure, DateInterval, DateTimeImmutable, DateTimeInterface, EnumeratesValues, Generator, Illuminate\Contracts\Support\CanBeEscapedWhenCastToString...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/Illuminate/Support/Str.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.029)
- **Top Global Matches:** file_cluster_15: 6.029, file_cluster_11: 7.905, file_cluster_16: 8.168
- **Magnitude:** 1244.58 | **LOC:** 2177 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 14.3%
- **Blast Radius:** changing it is visible to **243** in-repo importer(s); it depends on **18**; blast radius 18.84; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is` **(Many-Argument Workhorses)** (Impact: 19.8)
    * *Intent:* /** * Determine if a given string matches a given pattern. * * @param string|iterable<string> $patte...
  * `apa` **(Compute Cores)** (Impact: 19.1)
    * *Intent:* /** * Convert the given string to APA-style title case. * * See: https://apastyle.apa.org/style-gram...
  * `contains` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /** * Determine if a given string contains a given substring. * * @param string $haystack * @param s...
  * `isUuid` **(Defensive Guards)** (Impact: 13.8)
    * *Intent:* /** * Determine if a given value is a valid UUID. * * @param mixed $value * @param int<0, 8>|'nil'|'...
  * `password` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /** * Generate a random, secure password. * * @param int $length * @param bool $letters * @param boo...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 167 instances
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 349`, `args: 132`, `func_start: 110`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 241`
* *Architecture:* `api: 109`, `import: 18`
* *Defense:* `safety: 43`, `doc: 117`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.84
  * `Choke Point (Betweenness):` 0.019575 | `Ripple Effect (Closeness):` 0.256777
  * `Imports (Out-Degree: 4):` Closure, Illuminate\Support\Traits\Macroable, League\CommonMark\Environment\Environment, League\CommonMark\Extension\GithubFlavoredMarkdownExtension, League\CommonMark\Extension\InlinesOnly\InlinesOnlyExtension, League\CommonMark\GithubFlavoredMarkdownConverter, League\CommonMark\MarkdownConverter, Macroable...
  * `Imported By (In-Degree: 243):` (Excluded from Brief to save tokens)

### `src/Illuminate/Database/Eloquent/Concerns/HasAttributes.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.442)
- **Top Global Matches:** file_cluster_16: 6.442, file_cluster_15: 7.311, file_cluster_4: 8.309
- **Magnitude:** 1167.6 | **LOC:** 2590 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 7.1%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **45**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `castAttribute` **(Many-Argument Workhorses)** (Impact: 51.7)
    * *Intent:* /** * Cast an attribute to a native PHP type. * * @param string $key * @param mixed $value * @return...
  * `addCastAttributesToArray` **(Defensive Guards)** (Impact: 35.3)
    * *Intent:* /** * Add the casted attributes to the attributes array. * * @param array<string, mixed> $attributes...
  * `originalIsEquivalent` **(Defensive Guards)** (Impact: 34.9)
    * *Intent:* /** * Determine if the new and old values for a given key are equivalent. * * @param string $key * @...
  * `setAttribute` **(Defensive Guards)** (Impact: 26.9)
    * *Intent:* /** * Set a given attribute on the model. * * @param string $key * @param mixed $value * @return mix...
  * `transformModelValue` **(Stateful Encapsulated Methods)** (Impact: 19.1)
    * *Intent:* /** * Transform a raw model value using mutators, casts, etc. * * @param string $key * @param mixed ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 121 instances
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 275`, `structural_boundaries: 434`, `args: 136`, `func_start: 125`, `class_start: 1`
* *Risk/State:* `state_mutation: 169`, `planned_debt: 2`
* *Architecture:* `api: 60`, `import: 46`
* *Defense:* `safety: 67`, `doc: 143`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.003915 | `Ripple Effect (Closeness):` 0.164944
  * `Imports (Out-Degree: 32):` BackedEnum, Brick\Math\BigDecimal, Brick\Math\Exception\MathException, Brick\Math\RoundingMode, Carbon\CarbonImmutable, Carbon\CarbonInterface, DateTimeImmutable, DateTimeInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Illuminate/Database/Eloquent/Builder.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.242)
- **Top Global Matches:** file_cluster_15: 6.242, file_cluster_16: 6.658, file_cluster_11: 7.532
- **Magnitude:** 1143.4 | **LOC:** 2372 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 15.4%
- **Blast Radius:** changing it is visible to **48** in-repo importer(s); it depends on **21**; blast radius 1.703; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (79.0%), Guard Balance (formerly Safety Score) (64.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepareNestedWithRelationships` **(Stateful Encapsulated Methods)** (Impact: 19.6)
    * *Intent:* /** * Prepare nested with relationships. * * @param array $relations * @param string $prefix * @retu...
  * `__call` **(Compute Cores)** (Impact: 13.9)
    * *Intent:* /** * Dynamically handle calls into the query instance. * * @param string $method * @param array $pa...
  * `paginate` **(Many-Argument Workhorses)** (Impact: 13.1)
    * *Intent:* /** * Paginate the given query. * * @param int|null|\Closure $perPage * @param array|string $columns...
  * `addUpdatedAtColumn` **(Stateful Encapsulated Methods)** (Impact: 13.1)
    * *Intent:* /** * Add the "updated at" column to an array of values. * * @param array $values * @return array */...
  * `whereKey` **(Defensive Guards)** (Impact: 12.4)
    * *Intent:* /** * Add a where clause on the primary key to the query. * * @param mixed $id * @return $this */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 147 instances
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 374`, `args: 147`, `func_start: 121`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 215`
* *Architecture:* `api: 102`, `import: 22`
* *Defense:* `safety: 70`, `doc: 136`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.703
  * `Choke Point (Betweenness):` 0.00325 | `Ripple Effect (Closeness):` 0.153942
  * `Imports (Out-Degree: 19):` BadMethodCallException, Closure, Exception, Illuminate\Contracts\Database\Eloquent\Builder, Illuminate\Contracts\Database\Query\Expression, Illuminate\Contracts\Support\Arrayable, Illuminate\Database\Concerns\BuildsQueries, Illuminate\Database\Eloquent\Concerns\QueriesRelationships...
  * `Imported By (In-Degree: 48):` (Excluded from Brief to save tokens)

### `src/Illuminate/Collections/Collection.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.818)
- **Top Global Matches:** file_cluster_15: 5.818, file_cluster_12: 7.086, file_cluster_11: 7.436
- **Magnitude:** 1128.18 | **LOC:** 2006 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 0.552; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sortByMany` **(Many-Argument Workhorses)** (Impact: 30.3)
    * *Intent:* /** * Sort the collection using multiple comparisons. * * @param array<array-key, (callable(TValue, ...
  * `groupBy` **(Defensive Guards)** (Impact: 21.3)
    * *Intent:* /** * {@inheritDoc} */
  * `implode` **(Defensive Guards)** (Impact: 14.6)
    * *Intent:* /** * Concatenate values of a given key as a string. * * @param (callable(TValue, TKey): mixed)|stri...
  * `sortBy` **(Many-Argument Workhorses)** (Impact: 13.6)
    * *Intent:* /** * Sort the collection using the given callback. * * @param array<array-key, (callable(TValue, TV...
  * `split` **(Compute Cores)** (Impact: 10.2)
    * *Intent:* /** * Split a collection into a certain number of groups. * * @param int $numberOfGroups * @return (...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 538
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 321`, `args: 128`, `func_start: 115`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 200`, `unreferenced_by_name: 82`
* *Architecture:* `api: 112`, `import: 11`
* *Defense:* `safety: 34`, `doc: 118`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.552
  * `Choke Point (Betweenness):` 0.001902 | `Ripple Effect (Closeness):` 0.135839
  * `Imports (Out-Degree: 10):` ArrayAccess, ArrayIterator, EnumeratesValues, Illuminate\Contracts\Support\CanBeEscapedWhenCastToString, Illuminate\Support\Traits\EnumeratesValues, Illuminate\Support\Traits\Macroable, Illuminate\Support\Traits\TransformsToResourceCollection, InvalidArgumentException...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Illuminate/Database/Eloquent/Model.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.768)
- **Top Global Matches:** file_cluster_15: 6.768, file_cluster_16: 6.946, file_cluster_11: 7.535
- **Magnitude:** 1114.64 | **LOC:** 2896 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 11.1%
- **Blast Radius:** changing it is visible to **274** in-repo importer(s); it depends on **47**; blast radius 16.815; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Connectivity (formerly Api Exposure) (83.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (60.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `incrementOrDecrementEach` **(Stateful Encapsulated Methods)** (Impact: 19.9)
    * *Intent:* /** * Run the incrementEach or decrementEach method on the model. * * @param array<string, float|int...
  * `initializeModelAttributes` **(Defensive Guards)** (Impact: 19.6)
    * *Intent:* /** * Initialize the model attributes from class attributes. * * @return void */
  * `resolveClassAttribute` **(Stateful Encapsulated Methods)** (Impact: 19.4)
    * *Intent:* /** * Resolve a class attribute value from the model. * * @template TAttribute of object * * @param ...
  * `fill` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Fill the model with an array of attributes. * * @param array<string, mixed> $attributes * @ret...
  * `incrementOrDecrement` **(Stateful Encapsulated Methods)** (Impact: 14.8)
    * *Intent:* /** * Run the increment or decrement method on the model. * * @param string $column * @param float|i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 102 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 428`, `args: 182`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `state_mutation: 202`
* *Architecture:* `api: 134`, `import: 38`
* *Defense:* `safety: 54`, `doc: 199`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.815
  * `Choke Point (Betweenness):` 0.025193 | `Ripple Effect (Closeness):` 0.225891
  * `Imports (Out-Degree: 39):` ArrayAccess, Closure, Concerns\GuardsAttributes, Concerns\HasAttributes, Concerns\HasEvents, Concerns\HasGlobalScopes, Concerns\HasRelationships, Concerns\HasTimestamps...
  * `Imported By (In-Degree: 274):` (Excluded from Brief to save tokens)

### `tests/Testing/TestResponseTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.134)
- **Top Global Matches:** file_cluster_11: 6.134, file_cluster_10: 7.16, file_cluster_15: 7.877
- **Magnitude:** 1046.12 | **LOC:** 3368 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **32**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.0%), Connectivity (formerly Api Exposure) (13.1%), Concurrency Surface (formerly Concurrency) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAssertExactJsonStructure` **(I/O & Config Routines)** (Impact: 4.0)
  * `testAssertSessionOnlyValidationErrorsUsingAssertOnlyInvalid` **(I/O & Config Routines)** (Impact: 2.8)
  * `testResponseCanBeReturnedAsCollection` **(I/O & Config Routines)** (Impact: 2.8)
  * `testAssertStreamedAndAssertNotStreamed` **(I/O & Config Routines)** (Impact: 2.6)
  * `testAssertJsonPath` **(I/O & Config Routines)** (Impact: 2.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 400
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 673`, `args: 260`, `func_start: 219`, `class_start: 8`
* *Risk/State:* `state_mutation: 396`, `unreferenced_by_name: 213`
* *Architecture:* `io: 9`, `api: 218`, `concurrency: 3`, `import: 32`
* *Defense:* `safety: 64`, `test: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 25):` Exception, Illuminate\Container\Container, Illuminate\Contracts\View\View, Illuminate\Cookie\CookieValuePrefix, Illuminate\Database\Eloquent\Collection, Illuminate\Database\Eloquent\Model, Illuminate\Encryption\Encrypter, Illuminate\Filesystem\Filesystem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Illuminate/Http/Client/PendingRequest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.127)
- **Top Global Matches:** file_cluster_16: 7.127, file_cluster_15: 7.269, file_cluster_11: 8.412
- **Magnitude:** 978.54 | **LOC:** 2136 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **33**; blast radius 0.161; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.5%), Guard Balance (formerly Safety Score) (58.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send` **(Defensive Guards)** (Impact: 50.0)
    * *Intent:* /** * Send the request to the given URL. * * @param string $method * @param string $url * @param arr...
  * `handlePromiseResponse` **(Many-Argument Workhorses)** (Impact: 41.4)
    * *Intent:* /** * Handle the response of an asynchronous request. * * @param \Illuminate\Http\Client\Response|\T...
  * `parseRequestData` **(Stateful Encapsulated Methods)** (Impact: 27.5)
    * *Intent:* /** * Get the request data as an array so that we can attach it to the request for convenient assert...
  * `normalizeRequestOptions` **(Stateful Encapsulated Methods)** (Impact: 21.6)
    * *Intent:* /** * Normalize the given request options. * * @param array $options * @return array */
  * `pool` **(Defensive Guards)** (Impact: 21.3)
    * *Intent:* /** * Send a pool of asynchronous requests concurrently. * * @param (callable(\Illuminate\Http\Clien...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 98 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 360`, `args: 132`, `func_start: 100`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 171`, `planned_debt: 6`
* *Architecture:* `io: 5`, `api: 72`, `concurrency: 1`, `import: 32`
* *Defense:* `safety: 85`, `doc: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 7.2e-05 | `Ripple Effect (Closeness):` 0.005957
  * `Imports (Out-Degree: 20):` Closure, Conditionable, Exception, GuzzleHttp\Client, GuzzleHttp\Cookie\CookieJar, GuzzleHttp\Exception\ConnectException, GuzzleHttp\Exception\RequestException, GuzzleHttp\Exception\TransferException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/Database/DatabaseEloquentIntegrationTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.198)
- **Top Global Matches:** file_cluster_7: 8.198, file_cluster_12: 9.876, file_cluster_5: 10.316
- **Magnitude:** 978.1 | **LOC:** 3092 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.3%), Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.6%), Complexity Load (formerly Cognitive Load) (14.9%)
- **Documentation Coverage:** 98.1763% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createSchema` **(Callbacks & Closures)** (Impact: 8.4)
  * `testPaginatedModelCollectionRetrievalUsingCallablePerPage` **(Callbacks & Closures)** (Impact: 8.2)
  * `testBasicModelRetrieval` **(I/O & Config Routines)** (Impact: 6.5)
    * *Intent:* /** * Tests... */
  * `testChunksWithLimitsAndOffsets` **(I/O & Config Routines)** (Impact: 5.5)
  * `testChunkByIdWithLimitsAndOffsets` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 434
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 444`, `args: 252`, `func_start: 168`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 284`, `state_mutation: 386`, `duplicate_logic: 2`, `unreferenced_by_name: 138`
* *Architecture:* `api: 167`, `import: 29`
* *Defense:* `safety: 19`, `doc: 7`, `test: 360`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` DateTimeInterface, Exception, HasUuids, Illuminate\Database\Capsule\Manager, Illuminate\Database\Eloquent\Builder, Illuminate\Database\Eloquent\Collection, Illuminate\Database\Eloquent\Concerns\HasUuids, Illuminate\Database\Eloquent\Model...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Routing/RoutingRouteTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.779)
- **Top Global Matches:** file_cluster_12: 7.779, file_cluster_10: 8.287, file_cluster_11: 9.344
- **Magnitude:** 961.54 | **LOC:** 2763 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 0.128; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.6%), Complexity Load (formerly Cognitive Load) (17.8%), Connectivity (formerly Api Exposure) (12.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testBasicDispatchingOfRoutes` **(Callbacks & Closures)** (Impact: 7.5)
  * `testWherePatternsProperlyFilter` **(Callbacks & Closures)** (Impact: 5.5)
  * `testMatchesMethodAgainstRequests` **(Callbacks & Closures)** (Impact: 5.0)
  * `withModels` **(Parameter Forwarders)** (Impact: 4.7)
  * `getRouter` **(Stateful Encapsulated Methods)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 13 instances
* *Memory Alloc (weighted view):* 128
* *State Mutation (weighted view):* 444
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 781`, `args: 352`, `func_start: 162`, `class_start: 35`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 418`, `duplicate_logic: 18`, `unreferenced_by_name: 110`
* *Architecture:* `api: 164`, `import: 44`
* *Defense:* `safety: 15`, `doc: 2`, `test: 313`, `immutability_locks: 3`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` Attribute, Closure, DateTime, Enums.php, Exception, Illuminate\Auth\Middleware\Authenticate, Illuminate\Auth\Middleware\Authorize, Illuminate\Config\Repository...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Illuminate/Testing/TestResponse.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.831)
- **Top Global Matches:** file_cluster_15: 5.831, file_cluster_12: 7.203, file_cluster_11: 7.539
- **Magnitude:** 945.98 | **LOC:** 2083 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 15.4%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 0.172; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.5%), Guard Balance (formerly Safety Score) (55.1%), Complexity Load (formerly Cognitive Load) (14.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertInvalid` **(Many-Argument Workhorses)** (Impact: 24.4)
    * *Intent:* /** * Assert that the response has the given validation errors. * * @param string|array|null $errors...
  * `assertJsonValidationErrors` **(Compute Cores)** (Impact: 21.2)
    * *Intent:* /** * Assert that the response has the given JSON validation errors. * * @param string|array $errors...
  * `assertValid` **(Many-Argument Workhorses)** (Impact: 17.7)
    * *Intent:* /** * Assert that the given keys do not have validation errors. * * @param string|array|null $keys *...
  * `assertSessionHasInput` **(Defensive Guards)** (Impact: 15.2)
    * *Intent:* /** * Assert that the session has a given value in the flashed input array. * * @param string|array ...
  * `assertDownload` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* /** * Assert that the response offers a file download. * * @param string|null $filename * @return $t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 105 instances
* *State Mutation (weighted view):* 362
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 294`, `args: 109`, `func_start: 102`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 152`
* *Architecture:* `io: 6`, `api: 101`, `import: 27`
* *Defense:* `safety: 54`, `doc: 107`, `test: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.172
  * `Choke Point (Betweenness):` 4.6e-05 | `Ripple Effect (Closeness):` 0.001135
  * `Imports (Out-Degree: 24):` ArrayAccess, Closure, Concerns\AssertsStatusCodes, Conditionable, Dumpable, Illuminate\Contracts\Support\MessageBag, Illuminate\Contracts\View\View, Illuminate\Cookie\CookieValuePrefix...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Illuminate/Container/Container.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.254)
- **Top Global Matches:** file_cluster_16: 6.254, file_cluster_15: 6.723, file_cluster_12: 7.94
- **Magnitude:** 912.2 | **LOC:** 1857 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **171** in-repo importer(s); it depends on **20**; blast radius 5.918; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.5%), Connectivity (formerly Api Exposure) (54.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve` **(Many-Argument Workhorses)** (Impact: 27.2)
    * *Intent:* /** * Resolve the given type from the container. * * @template TClass of object * * @param string|cl...
  * `getConcreteBindingFromAttributes` **(Stateful Encapsulated Methods)** (Impact: 18.1)
    * *Intent:* /** * Get the concrete binding for an abstract from the Bind attribute. * * @param string $abstract ...
  * `resolveClass` **(Stateful Encapsulated Methods)** (Impact: 15.5)
    * *Intent:* /** * Resolve a class based dependency from the container. * * @return mixed * * @throws \Illuminate...
  * `resolveDependencies` **(Stateful Encapsulated Methods)** (Impact: 14.6)
    * *Intent:* /** * Resolve all of the dependencies from the ReflectionParameters. * * @param \ReflectionParameter...
  * `bind` **(Many-Argument Workhorses)** (Impact: 13.8)
    * *Intent:* /** * Register a binding with the container. * * @param \Closure|string $abstract * @param \Closure|...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 239`, `args: 94`, `func_start: 87`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 173`
* *Architecture:* `api: 57`, `concurrency: 1`, `import: 20`
* *Defense:* `safety: 72`, `doc: 112`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.918
  * `Choke Point (Betweenness):` 0.003808 | `Ripple Effect (Closeness):` 0.176467
  * `Imports (Out-Degree: 13):` ArrayAccess, Closure, Exception, Illuminate\Container\Attributes\Bind, Illuminate\Container\Attributes\Scoped, Illuminate\Container\Attributes\Singleton, Illuminate\Contracts\Container\BindingResolutionException, Illuminate\Contracts\Container\CircularDependencyException...
  * `Imported By (In-Degree: 171):` (Excluded from Brief to save tokens)

### `src/Illuminate/Collections/Arr.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.725)
- **Top Global Matches:** file_cluster_15: 5.725, file_cluster_16: 7.867, file_cluster_12: 8.163
- **Magnitude:** 805.56 | **LOC:** 1319 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 13.3%
- **Blast Radius:** changing it is visible to **182** in-repo importer(s); it depends on **13**; blast radius 30.111; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `random` **(Defensive Guards)** (Impact: 25.8)
    * *Intent:* /** * Get one or a specified number of random values from an array. * * @param array $array * @param...
  * `get` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* /** * Get an item from an array using "dot" notation. * * @param \ArrayAccess|array $array * @param ...
  * `forget` **(Many-Argument Workhorses)** (Impact: 19.1)
    * *Intent:* /** * Remove one or many array items from a given array using "dot" notation. * * @param array $arra...
  * `has` **(Compute Cores)** (Impact: 18.6)
    * *Intent:* /** * Check if an item or items exist in an array using "dot" notation. * * @param \ArrayAccess|arra...
  * `pluck` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /** * Pluck an array of values from an array. * * @param iterable $array * @param string|array|int|C...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 103 instances
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 217`, `args: 68`, `func_start: 60`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 122`, `unreferenced_by_name: 40`
* *Architecture:* `api: 59`, `import: 13`
* *Defense:* `safety: 42`, `doc: 60`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.111
  * `Choke Point (Betweenness):` 0.005439 | `Ripple Effect (Closeness):` 0.243709
  * `Imports (Out-Degree: 7):` ArgumentCountError, ArrayAccess, Closure, Illuminate\Contracts\Support\Arrayable, Illuminate\Contracts\Support\Jsonable, Illuminate\Support\Traits\Macroable, InvalidArgumentException, JsonSerializable...
  * `Imported By (In-Degree: 182):` (Excluded from Brief to save tokens)

### `src/Illuminate/Database/Schema/Blueprint.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.935)
- **Top Global Matches:** file_cluster_15: 6.935, file_cluster_16: 7.864, file_cluster_11: 7.985
- **Magnitude:** 803.8 | **LOC:** 2007 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 12.5%
- **Blast Radius:** changing it is visible to **152** in-repo importer(s); it depends on **13**; blast radius 4.066; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addFluentIndexes` **(I/O & Config Routines)** (Impact: 21.6)
    * *Intent:* /** * Add the index commands fluently specified on columns. * * @return void */
  * `foreignIdFor` **(Defensive Guards)** (Impact: 9.9)
    * *Intent:* /** * Create a foreign ID column for the given model. * * @param \Illuminate\Database\Eloquent\Model...
  * `toSql` **(I/O & Config Routines)** (Impact: 9.6)
    * *Intent:* /** * Get the raw SQL statements for the blueprint. * * @return array */
  * `addAlterCommands` **(I/O & Config Routines)** (Impact: 8.7)
    * *Intent:* /** * Add the alter commands if whenever needed. * * @return void */
  * `morphs` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* /** * Add the proper columns for a polymorphic table. * * @param string $name * @param string|null $...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 288
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 300`, `args: 144`, `func_start: 136`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 154`
* *Architecture:* `api: 130`, `import: 13`
* *Defense:* `safety: 24`, `doc: 147`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.066
  * `Choke Point (Betweenness):` 0.004588 | `Ripple Effect (Closeness):` 0.092815
  * `Imports (Out-Degree: 15):` Closure, Illuminate\Database\Connection, Illuminate\Database\Eloquent\Concerns\HasUlids, Illuminate\Database\Query\Expression, Illuminate\Database\Schema\Grammars\Grammar, Illuminate\Database\Schema\Grammars\MariaDbGrammar, Illuminate\Database\Schema\Grammars\MySqlGrammar, Illuminate\Database\Schema\Grammars\SQLiteGrammar...
  * `Imported By (In-Degree: 152):` (Excluded from Brief to save tokens)

### `src/Illuminate/Database/Eloquent/Relations/BelongsToMany.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.266)
- **Top Global Matches:** file_cluster_15: 6.266, file_cluster_16: 6.911, file_cluster_11: 6.986
- **Magnitude:** 785.58 | **LOC:** 1714 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 7.1%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **18**; blast radius 1.042; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.3%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findOr` **(Defensive Guards)** (Impact: 15.1)
    * *Intent:* /** * Find a related model by its primary key or call a callback. * * @template TValue * * @param mi...
  * `withTimestamps` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /** * Specify that the pivot table has creation and update timestamps. * * @param string|null|false ...
  * `match` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* /** @inheritDoc */
  * `buildDictionary` **(Stateful Encapsulated Methods)** (Impact: 9.7)
    * *Intent:* /** * Build model dictionary keyed by the relation's foreign key. * * @param \Illuminate\Database\El...
  * `firstOrCreate` **(Defensive Guards)** (Impact: 9.7)
    * *Intent:* /** * Get the first record matching the attributes. If the record is not found, create it. * * @para...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 273`, `args: 114`, `func_start: 95`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 85`, `import: 17`
* *Defense:* `safety: 44`, `doc: 112`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.042
  * `Choke Point (Betweenness):` 0.001519 | `Ripple Effect (Closeness):` 0.172624
  * `Imports (Out-Degree: 15):` Closure, Illuminate\Contracts\Support\Arrayable, Illuminate\Database\Eloquent\Builder, Illuminate\Database\Eloquent\Collection, Illuminate\Database\Eloquent\Model, Illuminate\Database\Eloquent\ModelNotFoundException, Illuminate\Database\Eloquent\Relations\Concerns\AsPivot, Illuminate\Database\Eloquent\Relations\Concerns\InteractsWithDictionary...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/Integration/Routing/FluentRoutingTest.php` (PHP) | Magnitude: 18.08 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 17, test: 11, args: 6
- `tests/Integration/Queue/RateLimitedWithRedisTest.php` (PHP) | Magnitude: 73.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 145, structural_boundaries: 76, state_mutation: 25, args: 22
- `src/Illuminate/Support/Facades/Queue.php` (PHP) | Magnitude: 29.56 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 18, args: 8, doc: 7
- `tests/Database/DatabaseEloquentFactoryTest.php` (PHP) | Magnitude: 423.72 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 1048, structural_boundaries: 282, args: 145, state_mutation: 145
- `src/Illuminate/Pipeline/PipelineServiceProvider.php` (PHP) | Magnitude: 5.26 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, args: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/Cache/RateLimiterTest.php` (PHP) | Magnitude: 28.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 23, state_mutation: 11, import: 8
- `src/Illuminate/Auth/AuthManager.php` (PHP) | Magnitude: 119.72 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 134, structural_boundaries: 59, doc: 24, state_mutation: 23
- `tests/Integration/Database/Postgres/FulltextTest.php` (PHP) | Magnitude: 18.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 18, args: 8, func_start: 7
- `tests/Integration/Queue/CustomPayloadTest.php` (PHP) | Magnitude: 18.58 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 28, import: 8, args: 7
- `src/Illuminate/Foundation/Bus/PendingDispatch.php` (PHP) | Magnitude: 77.64 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 56, doc: 20, args: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Illuminate/Queue/CallQueuedHandler.php` (PHP) | Magnitude: 195.48 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 220, structural_boundaries: 78, branch: 54, safety: 24
- `src/Illuminate/View/Compilers/ComponentTagCompiler.php` (PHP) | Magnitude: 386.18 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 479, structural_boundaries: 132, state_mutation: 92, bitwise_ops: 66
- `tests/Testing/Console/RouteListCommandTest.php` (PHP) | Magnitude: 53.94 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 169, structural_boundaries: 51, args: 34, closures: 21
- `tests/Integration/Database/DatabaseEloquentModelCustomCastingTest.php` (PHP) | Magnitude: 322.68 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 472, structural_boundaries: 195, state_mutation: 74, test: 60
- `tests/Database/DatabaseEloquentHasManyThroughIntegrationTest.php` (PHP) | Magnitude: 196.52 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 539, structural_boundaries: 124, args: 74, state_mutation: 60

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Illuminate/Routing/Attributes/Controllers/Middleware.php` (PHP) | Magnitude: 16.58 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, api: 4, bitwise_ops: 3
- `src/Illuminate/Container/Attributes/Bind.php` (PHP) | Magnitude: 18.52 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, state_mutation: 5, import: 4
- `tests/Mail/MailManagerTest.php` (PHP) | Magnitude: 50.76 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 145, test: 29, structural_boundaries: 20, decorators: 19
- `tests/Database/DatabaseEloquentBuilderCreateOrFirstTest.php` (PHP) | Magnitude: 148.68 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 569, test: 84, structural_boundaries: 83, state_mutation: 59
- `tests/Integration/Http/Resources/JsonApi/Fixtures/PostFactory.php` (PHP) | Magnitude: 0.01 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/Notifications/NotificationMailMessageTest.php` (PHP) | Magnitude: 151.92 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 367, structural_boundaries: 109, safety_bypasses: 72, test: 63
- `tests/View/Blade/BladePushTest.php` (PHP) | Magnitude: 39.14 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 49, safety_bypasses: 18, state_mutation: 16, structural_boundaries: 12
- `tests/View/Blade/BladeComponentFirstTest.php` (PHP) | Magnitude: 2.4 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 4, safety_bypasses: 2, test: 2
- `tests/View/Blade/BladeExpressionTest.php` (PHP) | Magnitude: 4.8 | Delta: **0.175** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 10, debug_prints: 6, structural_boundaries: 5, test: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Illuminate/Queue/Console/PauseCommand.php` (PHP) | Magnitude: 7.1 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 13, import: 6, doc: 3
- `src/Illuminate/Console/Scheduling/Schedule.php` (PHP) | Magnitude: 241.22 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 243, structural_boundaries: 94, state_mutation: 46, branch: 38
- `tests/Validation/ValidationUniqueRuleTest.php` (PHP) | Magnitude: 76.72 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 177, structural_boundaries: 72, state_mutation: 43, test: 36
- `types/Database/Eloquent/Model.php` (PHP) | Magnitude: 10.44 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 37, import: 10, args: 9
- `src/Illuminate/Queue/Connectors/FailoverConnector.php` (PHP) | Magnitude: 6.22 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, import: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Illuminate/Support/Facades/Auth.php` (PHP) | Magnitude: 9.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, doc: 3, import: 3
- `src/Illuminate/Foundation/Validation/ValidatesRequests.php` (PHP) | Magnitude: 40.02 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 14, state_mutation: 9, branch: 5
- `src/Illuminate/Filesystem/FilesystemManager.php` (PHP) | Magnitude: 259.98 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 212, structural_boundaries: 102, state_mutation: 48, branch: 42
- `src/Illuminate/Auth/Access/HandlesAuthorization.php` (PHP) | Magnitude: 20.32 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 10, state_mutation: 8, args: 4
- `src/Illuminate/Database/Eloquent/Relations/MorphPivot.php` (PHP) | Magnitude: 52.78 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 32, args: 11, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Illuminate/Foundation/Auth/User.php` (PHP) | Magnitude: 15.34 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 16, import: 9, indent_spaces: 4, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Illuminate/Process/Exceptions/ProcessFailedException.php` (PHP) | Magnitude: 19.06 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, state_mutation: 4, branch: 3
- `src/Illuminate/Contracts/Validation/InvokableRule.php` (PHP) | Magnitude: 18.78 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 2, args: 1, func_start: 1
- `src/Illuminate/Http/Middleware/CheckResponseForModifications.php` (PHP) | Magnitude: 8.3 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 6, ssr_boundaries: 3, import: 2
- `tests/Integration/Database/QueryingWithEnumsTest.php` (PHP) | Magnitude: 13.2 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 11, test: 6, state_mutation: 5
- `src/Illuminate/Http/Resources/MergeValue.php` (PHP) | Magnitude: 9.92 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, core_var_decl: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Illuminate/Console/Scheduling/ScheduleRunCommand.php` (PHP) | Magnitude: 140.8 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 159, structural_boundaries: 46, branch: 40, state_mutation: 22
- `src/Illuminate/Notifications/NotificationSender.php` (PHP) | Magnitude: 209.94 | Delta: **0.11** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 155, structural_boundaries: 55, branch: 52, state_mutation: 33
- `src/Illuminate/Database/Eloquent/Concerns/QueriesRelationships.php` (PHP) | Magnitude: 710.1 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 500, structural_boundaries: 194, state_mutation: 124, branch: 98

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/Support/ConfigurationUrlParserTest.php` (PHP) | Magnitude: 19.16 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 425, safety_bypasses: 15, structural_boundaries: 13, test: 8
- `tests/View/Blade/BladeLangTest.php` (PHP) | Magnitude: 6.82 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 5, args: 4, safety_bypasses: 3
- `tests/Mail/MailLogTransportTest.php` (PHP) | Magnitude: 34.04 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 28, state_mutation: 14, import: 9
- `tests/Events/EventsSubscriberTest.php` (PHP) | Magnitude: 32.0 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, structural_boundaries: 23, state_mutation: 10, api: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Illuminate/Http/Resources/CollectsResources.php` (PHP) | Magnitude: 69.46 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 25, branch: 16, state_mutation: 13

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Illuminate/Collections/LazyCollection.php` -> Churn: **71.5%** | Cog Load: 46.3231% | Debt: 99.5632%
- `.github/workflows/tests.yml` -> Churn: **66.18%** | Cog Load: 5.1429% | Debt: 77.4054%
- `src/Illuminate/Collections/Arr.php` -> Churn: **66.18%** | Cog Load: 35.7785% | Debt: 97.8524%
- `.github/workflows/redis.yml` -> Churn: **61.22%** | Cog Load: 0.0% | Debt: 85.4893%
- `.github/workflows/databases.yml` -> Churn: **57.23%** | Cog Load: 0.0% | Debt: 99.9447%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `tests/Database/DatabaseEloquentIntegrationTest.php` -> **Lucas Michot** (100.0% isolated ownership) | Magnitude: 978.1
- `tests/Database/DatabaseMariaDbSchemaGrammarTest.php` -> **Lucas Michot** (100.0% isolated ownership) | Magnitude: 666.38
- `src/Illuminate/Foundation/Application.php` -> **taylorotwell** (89.2% isolated ownership) | Magnitude: 552.76
- `tests/Database/DatabaseSQLiteSchemaGrammarTest.php` -> **Lucas Michot** (100.0% isolated ownership) | Magnitude: 463.84
- `tests/Foundation/FoundationViteTest.php` -> **Karim Mahmoud Hassan** (100.0% isolated ownership) | Magnitude: 443.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Illuminate/Foundation/helpers.php` -> **Severity: 2.929** (Bridge: 0.0293 * Flux: 100.0%)
- `src/Illuminate/Database/Eloquent/Model.php` -> **Severity: 2.141** (Bridge: 0.0252 * Flux: 84.9975%)
- `src/Illuminate/Support/Str.php` -> **Severity: 1.957** (Bridge: 0.0196 * Flux: 100.0%)
- `src/Illuminate/Support/Stringable.php` -> **Severity: 1.904** (Bridge: 0.0191 * Flux: 99.4903%)
- `src/Illuminate/Support/helpers.php` -> **Severity: 1.785** (Bridge: 0.0178 * Flux: 99.9997%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Illuminate/Support/Str.php` -> **Severity: 18.289** (Embedded: 0.2568 * Error Risk: 71.2259%)
- `src/Illuminate/Collections/Arr.php` -> **Severity: 16.391** (Embedded: 0.2437 * Error Risk: 67.2553%)
- `src/Illuminate/Collections/helpers.php` -> **Severity: 15.124** (Embedded: 0.2414 * Error Risk: 62.6625%)
- `src/Illuminate/Support/helpers.php` -> **Severity: 15.123** (Embedded: 0.2583 * Error Risk: 58.5396%)
- `src/Illuminate/Foundation/Exceptions/Renderer/Exception.php` -> **Severity: 14.21** (Embedded: 0.2311 * Error Risk: 61.4953%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tests/Database/DatabaseEloquentRelationshipsTest.php` -> **Severity: 337.9** (Blast Radius: 3.379 * Doc Risk: 100.0%)
- `src/Illuminate/Support/helpers.php` -> **Severity: 300.909** (Blast Radius: 21.991 * Doc Risk: 13.6833%)
- `tests/Integration/Database/DatabaseTestCase.php` -> **Severity: 84.35** (Blast Radius: 1.687 * Doc Risk: 50.0%)
- `tests/Integration/Database/EloquentTransactionWithAfterCommitTests.php` -> **Severity: 34.7** (Blast Radius: 0.347 * Doc Risk: 100.0%)
- `tests/Integration/Database/EloquentPivotWithoutTimestampTest.fixtures.php` -> **Severity: 23.8** (Blast Radius: 0.238 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 1107 literal sites + 66 sites through wrappers = 1173

- `fail` (function, panics_and_aborts, primitive): 66 call sites in 1 files -- `tests/Integration/Routing/PrecognitionTest.php`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 114835 call pairs -- scoped 37.4%, unique 2.0%, ambiguous 31.4%, external 29.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 114807 | 37.4% | 2.0% | 31.4% | 29.2% |
| shell | 16 | 12.5% | 0.0% | 0.0% | 87.5% |
| javascript | 12 | 0.0% | 0.0% | 0.0% | 100.0% |

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
