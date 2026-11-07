# ARCHITECTURAL_BRIEF: monolog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Seldaek/monolog.git` |
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
- **Scope:** 236 analyzed artifact(s), 17363 LOC.
- **Load-bearing artifact:** `src/Monolog/Level.php` -- 126 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Monolog/Handler/ElasticsearchHandler.php` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/Monolog/LoggerTest.php` at magnitude 318.74 (structural weight, not risk).
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
| Total Artifacts | 248 |
| Analyzed Artifacts (Scanned) | 236 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 12 |
| Total LOC | 17363 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 95.2% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3828 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1681 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.5109 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 24 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 216 | 17012 | 91.5% |
| MARKDOWN | 13 | 0 | 5.5% |
| YAML | 6 | 269 | 2.5% |
| JSON | 1 | 82 | 0.4% |

## 4.1 SOURCE ENCODINGS
All 236 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 26%, Encapsulated Accessors Files 15%, Data / Markup / Trivial 11%, Large Core Modules (3) 11%, Parameter Forwarders Files 11%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 223 | 94.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 5.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 12*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 2x Excluded (Unsupported Extension: '.neon')
- `.dist`: 2x Excluded (Unsupported Extension: '.dist')
- `.php`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.8 | 14.1 | 7.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 82.2 | 51.8 | 54.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 29.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.6 | 0.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.5 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 1.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 6.0 | 0.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.8 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.9 | 16.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.9 | 0.9 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 865 | 153 | 10 | `tests/Monolog/LoggerTest.php` |
| cleanup | 68 | 45 | 1 | `tests/Monolog/Formatter/NormalizerFormatterTest.php` |
| guards | 1123 | 161 | 13 | `src/Monolog/Logger.php` |
| danger | 219 | 81 | 3 | `tests/Monolog/Handler/NativeMailerHandlerTest.php` |
| concurrency | 26 | 11 | 0 | `tests/Monolog/Processor/ClosureContextProcessorTest.php` |
| connectivity | 1134 | 208 | 10 | `tests/Monolog/LoggerTest.php` |
| io | 184 | 37 | 3 | `src/Monolog/Handler/SyslogUdp/UdpSocket.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 41 | 18 | 0 | `src/Monolog/Handler/DeduplicationHandler.php` |
| time | 123 | 29 | 1 | `tests/Monolog/Handler/RotatingFileHandlerTest.php` |
| serialization | 62 | 22 | 0 | `tests/Monolog/Formatter/LogstashFormatterTest.php` |
| regex | 32 | 15 | 0 | `src/Monolog/Formatter/LineFormatter.php` |
| events | 19 | 8 | 0 | `tests/Monolog/Handler/AbstractProcessingHandlerTest.php` |
| tests | 920 | 91 | 11 | `tests/Monolog/LoggerTest.php` |
| docs | 1098 | 200 | 11 | `src/Monolog/Logger.php` |
| debt | 43 | 19 | 0 | `tests/Monolog/LoggerTest.php` |
| mutation | 3245 | 203 | 32 | `tests/Monolog/LoggerTest.php` |
| dead_code | 860 | 172 | 8 | `tests/Monolog/LoggerTest.php` |
| credential | 4 | 3 | 0 | `tests/Monolog/Handler/SlackWebhookHandlerTest.php` |
| threat | 7 | 4 | 0 | `tests/Monolog/Handler/ChromePHPHandlerTest.php` |
| ml_ai | 154 | 35 | 1 | `tests/Monolog/Handler/RotatingFileHandlerTest.php` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Monolog/Handler/SyslogUdp/UdpSocket.php` (Hits: 15)
- `tests/Monolog/Handler/SocketHandlerTest.php` (Hits: 12)
- `tests/Monolog/Handler/UdpSocketTest.php` (Hits: 12)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Level.php** (`src/Monolog/Level.php`) — 126 inbound connections
2. **LogRecord.php** (`src/Monolog/LogRecord.php`) — 106 inbound connections
3. **FormatterInterface.php** (`src/Monolog/Formatter/FormatterInterface.php`) — 38 inbound connections
4. **Utils.php** (`src/Monolog/Utils.php`) — 29 inbound connections
5. **LineFormatter.php** (`src/Monolog/Formatter/LineFormatter.php`) — 21 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ElasticsearchHandler.php** (`src/Monolog/Handler/ElasticsearchHandler.php`) — 12 outbound dependencies
2. **Logger.php** (`src/Monolog/Logger.php`) — 11 outbound dependencies
3. **PHPConsoleHandlerTest.php** (`tests/Monolog/Handler/PHPConsoleHandlerTest.php`) — 11 outbound dependencies
4. **FingersCrossedHandler.php** (`src/Monolog/Handler/FingersCrossedHandler.php`) — 10 outbound dependencies
5. **ElasticsearchHandlerTest.php** (`tests/Monolog/Handler/ElasticsearchHandlerTest.php`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addRecord` **(Many-Argument Workhorses)** (@ `src/Monolog/Logger.php`) -> Impact: **51.0** | LOC: 80
  * *Intent:* /** * Adds a log record. * * @param int $level The logging level (a Monolog or RFC 5424 level) * @param string $message The log message * @param mixed...
- `normalize` **(Many-Argument Workhorses)** (@ `src/Monolog/Formatter/NormalizerFormatter.php`) -> Impact: **38.3** | LOC: 74
  * *Intent:* /** * @return null|scalar|array<mixed[]|scalar|null> */
- `handleSignal` **(Defensive Guards)** (@ `src/Monolog/SignalHandler.php`) -> Impact: **38.3** | LOC: 39
  * *Intent:* /** * @param mixed $siginfo */
- `format` **(Compute Cores)** (@ `src/Monolog/Formatter/GelfMessageFormatter.php`) -> Impact: **34.4** | LOC: 65
  * *Intent:* /** * @inheritDoc */
- `write` **(Defensive Guards)** (@ `src/Monolog/Handler/NewRelicHandler.php`) -> Impact: **32.0** | LOC: 46
  * *Intent:* /** * @inheritDoc */
- `getSlackData` **(Compute Cores)** (@ `src/Monolog/Handler/Slack/SlackRecord.php`) -> Impact: **32.0** | LOC: 75
  * *Intent:* /** * Returns required data in format that Slack * is expecting. * * @phpstan-return mixed[] */
- `__invoke` **(Defensive Guards)** (@ `src/Monolog/Processor/PsrLogMessageProcessor.php`) -> Impact: **30.4** | LOC: 42
  * *Intent:* /** * @inheritDoc */
- `initConnector` **(Compute Cores)** (@ `src/Monolog/Handler/PHPConsoleHandler.php`) -> Impact: **29.6** | LOC: 54
- `normalizeException` **(Defensive Guards)** (@ `src/Monolog/Formatter/NormalizerFormatter.php`) -> Impact: **28.8** | LOC: 57
  * *Intent:* /** * @return array<array-key, string|int|array<string|int|array<string>>> */
- `__construct` **(Many-Argument Workhorses)** (@ `src/Monolog/Handler/SlackHandler.php`) -> Impact: **26.2** | LOC: 44
  * *Intent:* /** * @param string $token Slack API token * @param string $channel Slack channel (encoded ID or name) * @param string|null $username Name of a bot * ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Monolog/Handler` | 67 | 4009.96 | 21.66% | 74.83% |
| `tests/Monolog/Handler` | 54 | 2210.64 | 5.86% | 0.0% |
| `src/Monolog/Formatter` | 19 | 1411.1 | 23.68% | 17.08% |
| `src/Monolog` | 10 | 1005.28 | 23.8% | 15.88% |
| `tests/Monolog/Formatter` | 17 | 949.18 | 6.75% | 0.0% |
| `tests/Monolog` | 6 | 651.64 | 7.27% | 0.0% |
| `src/Monolog/Processor` | 15 | 426.52 | 19.27% | 54.49% |
| `src/Monolog/Handler/Slack` | 1 | 267.36 | 33.97% | 0.0% |
| `tests/Monolog/Processor` | 13 | 226.48 | 0.57% | 0.0% |
| `tests/Monolog/Handler/Slack` | 1 | 157.7 | 29.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Monolog/Handler/HandlerWrapper.php` -> **100.0%** Exposure
- `src/Monolog/Handler/AbstractHandler.php` -> **99.9925%** Exposure
- `src/Monolog/Handler/MailHandler.php` -> **99.9447%** Exposure
- `src/Monolog/Registry.php` -> **99.9447%** Exposure
- `src/Monolog/Handler/ElasticaHandler.php` -> **99.9237%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/Monolog/ErrorHandler.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/ChromePHPFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FlowdockFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FluentdFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/GelfMessageFormatter.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/Monolog/LoggerTest.php` -> **38** Orphaned Functions | **6** Duplicates
- `tests/Monolog/Formatter/NormalizerFormatterTest.php` -> **27** Orphaned Functions | **0** Duplicates
- `tests/Monolog/Formatter/LineFormatterTest.php` -> **22** Orphaned Functions | **0** Duplicates
- `tests/Monolog/Handler/SocketHandlerTest.php` -> **21** Orphaned Functions | **0** Duplicates
- `tests/Monolog/Formatter/JsonFormatterTest.php` -> **20** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/Monolog/Handler/RollbarHandlerTest.php` -> **99.9176%** Exposure
- `tests/Monolog/Handler/SlackWebhookHandlerTest.php` -> **95.8312%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `629` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/Monolog/LoggerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.691)
- **Top Global Matches:** file_cluster_11: 6.691, file_cluster_10: 7.139, file_cluster_15: 7.521
- **Magnitude:** 318.74 | **LOC:** 920 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.9%), Concurrency Surface (formerly Concurrency) (42.0%), Complexity Load (formerly Cognitive Load) (14.5%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 38.6139% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUseMicrosecondTimestamps` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** * @covers Logger::useMicrosecondTimestamps * @covers Logger::addRecord */
  * `testReset` **(I/O & Config Routines)** (Impact: 4.6)
  * `testConvertRFC5424ToMonologLevelInAddRecordAndLog` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* /** * @covers Monolog\Logger::addRecord * @covers Monolog\Logger::log */
  * `testLogCycleDetectionWithFibersWithoutCycle` **(Callbacks & Closures)** (Impact: 3.2)
  * `testTimezoneIsRespectedInUTC` **(Interface Declarations)** (Impact: 2.9)
    * *Intent:* /** * @covers Logger::setTimezone * @covers JsonSerializableDateTimeImmutable::__construct */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 176`, `args: 63`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 124`, `duplicate_logic: 6`, `unreferenced_by_name: 38`
* *Architecture:* `api: 49`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 5`, `doc: 30`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Monolog\Handler\HandlerInterface, Monolog\Handler\TestHandler, Monolog\Processor\WebProcessor, Monolog\Test\MonologTestCase, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Logger.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.66)
- **Top Global Matches:** file_cluster_15: 6.66, file_cluster_11: 7.753, file_cluster_16: 8.253
- **Magnitude:** 314.08 | **LOC:** 752 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **11**; blast radius 18.719; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (69.9%), Guard Balance (formerly Safety Score) (58.2%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 5.9701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addRecord` **(Many-Argument Workhorses)** (Impact: 51.0)
    * *Intent:* /** * Adds a log record. * * @param int $level The logging level (a Monolog or RFC 5424 level) * @pa...
  * `toMonologLevel` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* /** * Converts PSR-3 levels to Monolog ones if necessary * * @param int|string|Level|LogLevel::* $le...
  * `log` **(Defensive Guards)** (Impact: 10.8)
    * *Intent:* /** * Adds a log record at an arbitrary level. * * This method allows for compatibility with common ...
  * `reset` **(Defensive Guards)** (Impact: 5.7)
    * *Intent:* /** * Ends a log cycle and resets all handlers and processors to their initial state. * * Resetting ...
  * `isHandling` **(Compute Cores)** (Impact: 5.1)
    * *Intent:* /** * Checks whether the Logger has a handler that listens on the given level * * @phpstan-param val...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 7
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 104`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `api: 42`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 23`, `doc: 48`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.719
  * `Choke Point (Betweenness):` 0.002247 | `Ripple Effect (Closeness):` 0.12682
  * `Imports (Out-Degree: 4):` Closure, DateTimeZone, Fiber, Monolog\Handler\HandlerInterface, Monolog\Processor\ProcessorInterface, Psr\Log\InvalidArgumentException, Psr\Log\LogLevel, Psr\Log\LoggerInterface...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/LineFormatter.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.722)
- **Top Global Matches:** file_cluster_16: 5.722, file_cluster_15: 5.993, file_cluster_11: 8.558
- **Magnitude:** 292.8 | **LOC:** 318 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **3**; blast radius 14.223; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.3%), Complexity Load (formerly Cognitive Load) (35.5%), Connectivity (formerly Api Exposure) (33.0%)
- **Documentation Coverage:** 29.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Compute Cores)** (Impact: 21.0)
    * *Intent:* /** * @inheritDoc */
  * `formatException` **(Stateful Encapsulated Methods)** (Impact: 15.8)
  * `__construct` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* /** * @param string|null $format The format of the message * @param string|null $dateFormat The form...
  * `stacktracesParser` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `replaceNewlines` **(Stateful Encapsulated Methods)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 48`, `args: 17`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `fragile_debt: 2`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.223
  * `Choke Point (Betweenness):` 0.000462 | `Ripple Effect (Closeness):` 0.094004
  * `Imports (Out-Degree: 2):` Closure, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/Slack/SlackRecord.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.513)
- **Top Global Matches:** file_cluster_4: 5.513, file_cluster_15: 8.264, file_cluster_16: 8.875
- **Magnitude:** 267.36 | **LOC:** 382 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 4.488; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (36.0%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSlackData` **(Compute Cores)** (Impact: 32.0)
    * *Intent:* /** * Returns required data in format that Slack * is expecting. * * @phpstan-return mixed[] */
  * `__construct` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* /** * @param string[] $excludeFields */
  * `removeExcludedFields` **(Stateful Encapsulated Methods)** (Impact: 10.9)
    * *Intent:* /** * Get a copy of record with fields excluded according to $this->excludeFields * * @return mixed[...
  * `stringify` **(Compute Cores)** (Impact: 4.8)
    * *Intent:* /** * Stringifies an array of key/value pairs to be used in attachment fields * * @param mixed[] $fi...
  * `setUserIcon` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * @return $this */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `api: 16`, `import: 5`
* *Defense:* `safety: 2`, `doc: 25`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.488
  * `Choke Point (Betweenness):` 0.000294 | `Ripple Effect (Closeness):` 0.021277
  * `Imports (Out-Degree: 5):` Monolog\Formatter\FormatterInterface, Monolog\Formatter\NormalizerFormatter, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/NormalizerFormatter.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.627)
- **Top Global Matches:** file_cluster_4: 6.627, file_cluster_15: 7.16, file_cluster_16: 7.631
- **Magnitude:** 260.06 | **LOC:** 373 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **4**; blast radius 6.137; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.3%), Complexity Load (formerly Cognitive Load) (45.7%), Connectivity (formerly Api Exposure) (41.1%)
- **Documentation Coverage:** 8.1081% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalize` **(Many-Argument Workhorses)** (Impact: 38.3)
    * *Intent:* /** * @return null|scalar|array<mixed[]|scalar|null> */
  * `normalizeException` **(Defensive Guards)** (Impact: 28.8)
    * *Intent:* /** * @return array<array-key, string|int|array<string|int|array<string>>> */
  * `setJsonPrettyPrint` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * Enables `json_encode` pretty print. * * @return $this */
  * `formatDate` **(Stateful Encapsulated Methods)** (Impact: 4.7)
  * `__construct` **(Compute Cores)** (Impact: 4.4)
    * *Intent:* /** * @param string|null $dateFormat The format of the timestamp: one supported by DateTime::format ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 66`, `args: 21`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 18`, `doc: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.137
  * `Choke Point (Betweenness):` 0.000439 | `Ripple Effect (Closeness):` 0.04352
  * `Imports (Out-Degree: 3):` Monolog\JsonSerializableDateTimeImmutable, Monolog\LogRecord, Monolog\Utils, Throwable
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `tests/Monolog/Formatter/NormalizerFormatterTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.505)
- **Top Global Matches:** file_cluster_11: 5.505, file_cluster_15: 6.937, file_cluster_16: 7.347
- **Magnitude:** 221.78 | **LOC:** 591 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.3%), Complexity Load (formerly Cognitive Load) (24.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.3%), Connectivity (formerly Api Exposure) (10.2%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFormatSoapFaultException` **(I/O & Config Routines)** (Impact: 4.3)
  * `testIgnoresRecursiveObjectReferences` **(I/O & Config Routines)** (Impact: 3.4)
    * *Intent:* /** * Test issue #137 */
  * `testExceptionTraceWithArgs` **(Defensive Guards)** (Impact: 3.4)
  * `testToJsonIgnoresInvalidTypes` **(I/O & Config Routines)** (Impact: 3.2)
  * `testFormat` **(I/O & Config Routines)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 6 instances
* *Memory Alloc (weighted view):* 28
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 119`, `args: 38`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `unreferenced_by_name: 27`
* *Architecture:* `io: 4`, `api: 34`, `import: 1`
* *Defense:* `safety: 10`, `doc: 2`, `test: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SocketHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.786)
- **Top Global Matches:** file_cluster_12: 6.786, file_cluster_16: 6.968, file_cluster_11: 7.847
- **Magnitude:** 207.08 | **LOC:** 437 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 2.894; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.2%), Guard Balance (formerly Safety Score) (65.5%), Complexity Load (formerly Cognitive Load) (40.3%)
- **Documentation Coverage:** 19.1489% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeToSocket` **(Stateful Encapsulated Methods)** (Impact: 17.0)
  * `__construct` **(Many-Argument Workhorses)** (Impact: 16.2)
    * *Intent:* /** * @param string $connectionString Socket connection string * @param bool $persistent Flag to ena...
  * `writingIsTimedOut` **(Stateful Encapsulated Methods)** (Impact: 8.3)
  * `createSocketResource` **(Stateful Encapsulated Methods)** (Impact: 4.6)
  * `streamSetChunkSize` **(Stateful Encapsulated Methods)** (Impact: 3.6)
    * *Intent:* /** * Wrapper to allow mocking * * @see http://php.net/manual/en/function.stream-set-chunk-size.php ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 76`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 38`, `unreferenced_by_name: 13`
* *Architecture:* `io: 6`, `api: 15`, `import: 2`
* *Defense:* `safety: 1`, `doc: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.894
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 2):` Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/StreamHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.604)
- **Top Global Matches:** file_cluster_16: 6.604, file_cluster_12: 6.746, file_cluster_11: 8.177
- **Magnitude:** 202.46 | **LOC:** 281 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 3.24; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (35.5%), Connectivity (formerly Api Exposure) (11.3%)
- **Documentation Coverage:** 30.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 25.4)
    * *Intent:* /** * @param resource|string $stream If a missing path can't be created, an UnexpectedValueException...
  * `write` **(Defensive Guards)** (Impact: 21.8)
    * *Intent:* /** * @inheritDoc */
  * `createDir` **(Stateful Encapsulated Methods)** (Impact: 10.9)
  * `getDirFromStream` **(Stateful Encapsulated Methods)** (Impact: 6.3)
  * `getInodeFromUrl` **(Stateful Encapsulated Methods)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 41`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`
* *Architecture:* `io: 4`, `api: 7`, `import: 3`
* *Defense:* `safety: 4`, `doc: 12`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.24
  * `Choke Point (Betweenness):` 6.5e-05 | `Ripple Effect (Closeness):` 0.008511
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/ErrorHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.555)
- **Top Global Matches:** file_cluster_16: 5.555, file_cluster_15: 7.045, file_cluster_2: 8.808
- **Magnitude:** 191.6 | **LOC:** 280 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 2.952; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.4%), Complexity Load (formerly Cognitive Load) (33.8%), Connectivity (formerly Api Exposure) (10.7%)
- **Documentation Coverage:** 17.6471% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleError` **(Stateful Encapsulated Methods)** (Impact: 21.4)
  * `handleException` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `register` **(Many-Argument Workhorses)** (Impact: 9.7)
    * *Intent:* /** * Registers a new ErrorHandler for a given Logger * * By default it will handle errors, exceptio...
  * `registerErrorHandler` **(Many-Argument Workhorses)** (Impact: 9.6)
    * *Intent:* /** * @param array<int, LogLevel::*> $levelMap an array of E_* constant to LogLevel::* constant mapp...
  * `registerExceptionHandler` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /** * @param array<class-string, LogLevel::*> $levelMap an array of class name to LogLevel::* consta...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 33`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 45`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 10`, `doc: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.952
  * `Choke Point (Betweenness):` 2.7e-05 | `Ripple Effect (Closeness):` 0.008511
  * `Imports (Out-Degree: 1):` Closure, Psr\Log\LogLevel, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/Utils.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 8.057)
- **Top Global Matches:** file_cluster_9: 8.057, file_cluster_12: 8.254, file_cluster_16: 9.976
- **Magnitude:** 181.7 | **LOC:** 258 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); blast radius 31.778; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Connectivity (formerly Api Exposure) (48.5%), Complexity Load (formerly Cognitive Load) (44.0%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleJsonError` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /** * Handle a json_encode failure. * * If the failure is due to invalid string encoding, try to cle...
  * `jsonEncode` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** * Return the JSON representation of a value * * @param mixed $data * @param int $encodeFlags fla...
  * `expandIniShorthandBytes` **(Type Conversions)** (Impact: 12.8)
    * *Intent:* /** * Converts a string with a valid 'memory_limit' format, to bytes. * * @param string|false $val *...
  * `detectAndCleanUtf8` **(Stateful Encapsulated Methods)** (Impact: 9.7)
    * *Intent:* * Detect invalid UTF-8 string characters and convert to valid UTF-8. * * Valid UTF-8 input will be l...
  * `canonicalizePath` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Makes sure if a relative path is passed in it is turned into an absolute path * * @param strin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 33`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`
* *Architecture:* `api: 7`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.778
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.192021
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `tests/Monolog/Handler/Slack/SlackRecordTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.104)
- **Top Global Matches:** file_cluster_11: 6.104, file_cluster_13: 7.549, file_cluster_10: 7.706
- **Magnitude:** 157.7 | **LOC:** 380 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (29.2%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testExcludeExtraAndContextFields` **(I/O & Config Routines)** (Impact: 4.5)
  * `testTextEqualsFormatterOutput` **(Callbacks & Closures)** (Impact: 2.5)
  * `testAddsShortAttachmentWithContextAndExtra` **(I/O & Config Routines)** (Impact: 2.5)
  * `testAddsLongAttachmentWithContextAndExtra` **(I/O & Config Routines)** (Impact: 2.5)
  * `testStringify` **(Annotated & Test Methods)** (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 58`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 88`, `unreferenced_by_name: 20`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 1`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, PHPUnit\Framework\Attributes\CoversClass, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PushoverHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.374)
- **Top Global Matches:** file_cluster_16: 5.374, file_cluster_15: 6.647, file_cluster_11: 8.461
- **Magnitude:** 157.32 | **LOC:** 247 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.8%), Debt Markers (formerly Tech Debt) (74.0%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 25.9)
    * *Intent:* * send the same notification to the user. * @param int $expire The expire parameter specifies how ma...
  * `buildContent` **(Stateful Encapsulated Methods)** (Impact: 10.5)
  * `write` **(Stateful Encapsulated Methods)** (Impact: 3.4)
  * `buildHeader` **(Encapsulated Accessors)** (Impact: 1.9)
  * `generateDataStream` **(Encapsulated Accessors)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 24`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `unreferenced_by_name: 5`
* *Architecture:* `io: 6`, `api: 4`, `import: 5`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Monolog\Level, Monolog\LogRecord, Monolog\Logger, Monolog\Utils, Psr\Log\LogLevel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/SignalHandlerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.879)
- **Top Global Matches:** file_cluster_11: 6.879, file_cluster_15: 7.555, file_cluster_13: 7.601
- **Magnitude:** 155.54 | **LOC:** 293 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.6%), Guard Balance (formerly Safety Score) (63.8%), Complexity Load (formerly Cognitive Load) (25.1%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 58.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testRegisterSyscallRestartingSignalHandler` **(Compute Cores)** (Impact: 10.4)
    * *Intent:* /** * @depends testRegisterDefaultPreviousSignalHandler * @requires function pcntl_fork * @requires ...
  * `tearDown` **(I/O & Config Routines)** (Impact: 6.0)
  * `setSignalHandler` **(Stateful Encapsulated Methods)** (Impact: 5.6)
  * `testRegisterDefaultPreviousSignalHandler` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /** * @depends testRegisterSignalHandler * @requires function pcntl_fork * @requires function pcntl_...
  * `testRegisterCallablePreviousSignalHandler` **(Annotated & Test Methods)** (Impact: 5.1)
    * *Intent:* /** * @depends testRegisterSignalHandler * @requires function pcntl_signal_get_handler */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 48`, `args: 17`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 37`, `unreferenced_by_name: 8`
* *Architecture:* `io: 2`, `api: 11`, `concurrency: 2`, `import: 5`
* *Defense:* `doc: 6`, `test: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Monolog\Handler\StreamHandler, Monolog\Handler\TestHandler, Monolog\Test\MonologTestCase, PHPUnit\Framework\Attributes\DataProvider, Psr\Log\LogLevel
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/BrowserConsoleHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.215)
- **Top Global Matches:** file_cluster_16: 5.215, file_cluster_11: 6.634, file_cluster_15: 7.598
- **Magnitude:** 152.66 | **LOC:** 301 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.894; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.9%), Debt Markers (formerly Tech Debt) (42.2%), Complexity Load (formerly Cognitive Load) (31.4%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleCustomStyles` **(Stateful Encapsulated Methods)** (Impact: 8.3)
  * `dump` **(Stateful Encapsulated Methods)** (Impact: 7.8)
    * *Intent:* /** * @param mixed[] $dict * @return mixed[] */
  * `getResponseFormatFromContentType` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* /** * @return string One of 'js', 'html' or 'unknown' * @phpstan-return self::FORMAT_* */
  * `generateScript` **(Stateful Encapsulated Methods)** (Impact: 6.1)
  * `send` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* /** * Convert records to javascript console commands and send it to the browser. * This method is au...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 59`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 4`, `import: 7`
* *Defense:* `safety: 1`, `doc: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.894
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 5):` Monolog\Formatter\FormatterInterface, Monolog\Formatter\LineFormatter, Monolog\Level, Monolog\LogRecord, Monolog\Utils, headers_list, stripos
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/TelegramBotHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.355)
- **Top Global Matches:** file_cluster_16: 5.355, file_cluster_15: 5.623, file_cluster_11: 8.196
- **Magnitude:** 152.6 | **LOC:** 302 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.894; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.6%), Debt Markers (formerly Tech Debt) (37.8%), Complexity Load (formerly Cognitive Load) (32.1%)
- **Documentation Coverage:** 5.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 21.2)
    * *Intent:* /** * @param string $apiKey Telegram bot access token provided by BotFather * @param string $channel...
  * `handleBatch` **(Compute Cores)** (Impact: 9.5)
    * *Intent:* /** * @inheritDoc */
  * `sendCurl` **(Stateful Encapsulated Methods)** (Impact: 8.7)
  * `send` **(Stateful Encapsulated Methods)** (Impact: 6.3)
    * *Intent:* /** * Send request to @link https://api.telegram.org/bot on SendMessage action. */
  * `setParseMode` **(Compute Cores)** (Impact: 4.7)
    * *Intent:* /** * @return $this */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 37`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `doc: 22`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.894
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 5):` Monolog\Level, Monolog\LogRecord, Monolog\Utils, RuntimeException
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Monolog/Formatter/JsonFormatterTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.62)
- **Top Global Matches:** file_cluster_11: 6.62, file_cluster_16: 7.489, file_cluster_10: 8.162
- **Magnitude:** 151.58 | **LOC:** 399 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.4%), Complexity Load (formerly Cognitive Load) (17.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.8%), Connectivity (formerly Api Exposure) (8.3%)
- **Documentation Coverage:** 74.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatException` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* /** * @param \Exception|\Throwable $exception */
  * `testFormatWithPrettyPrint` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* /** * @covers Monolog\Formatter\JsonFormatter::format */
  * `formatRecordWithExceptionInContext` **(Stateful Encapsulated Methods)** (Impact: 2.3)
  * `assertContextContainsFormattedException` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* /** * @internal param string $exception */
  * `testFormatObjects` **(Encapsulated Accessors)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 91`, `args: 29`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`, `unreferenced_by_name: 20`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Exception, JsonSerializable, Monolog\Level, Monolog\LogRecord, Monolog\Test\MonologTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PHPConsoleHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.954)
- **Top Global Matches:** file_cluster_4: 5.954, file_cluster_16: 9.737, file_cluster_15: 10.979
- **Magnitude:** 150.46 | **LOC:** 304 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 2.376; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (70.5%), Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (36.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initConnector` **(Compute Cores)** (Impact: 29.6)
  * `getRecordTags` **(Stateful Encapsulated Methods)** (Impact: 12.4)
    * *Intent:* /** * @return array{string, mixed[]} */
  * `handleErrorRecord` **(Stateful Encapsulated Methods)** (Impact: 7.7)
  * `write` **(Stateful Encapsulated Methods)** (Impact: 7.6)
    * *Intent:* /** * Writes the record down to the log of the implementing handler */
  * `__construct` **(Many-Argument Workhorses)** (Impact: 7.2)
    * *Intent:* /** * @param array<string, mixed> $options See \Monolog\Handler\PHPConsoleHandler::$options for more...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`, `unreferenced_by_name: 6`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 10`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.376
  * `Choke Point (Betweenness):` 5.5e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 6):` Monolog\Formatter\FormatterInterface, Monolog\Formatter\LineFormatter, Monolog\Level, Monolog\LogRecord, Monolog\Utils, PhpConsole\Connector, PhpConsole\Handler, PhpConsole\Helper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Monolog/Handler/StreamHandlerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.385)
- **Top Global Matches:** file_cluster_12: 6.385, file_cluster_11: 8.196, file_cluster_7: 9.004
- **Magnitude:** 139.12 | **LOC:** 381 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (58.1%), Complexity Load (formerly Cognitive Load) (12.2%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 31.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testPreventOOMError` **(Defensive Guards)** (Impact: 6.4)
  * `testWriteErrorDuringWriteRetriesWithClose` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::write */
  * `testWriteNonExistingAndNotCreatablePath` **(Defensive Guards)** (Impact: 4.0)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::__construct * @covers Monolog\Handler\StreamHandler::wr...
  * `testWriteInvalidResource` **(I/O & Config Routines)** (Impact: 3.5)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::__construct * @covers Monolog\Handler\StreamHandler::wr...
  * `testWriteErrorDuringWriteRetriesButThrowsIfStillFails` **(I/O & Config Routines)** (Impact: 3.2)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::write */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 53`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 43`, `unreferenced_by_name: 19`
* *Architecture:* `io: 6`, `api: 22`, `import: 3`
* *Defense:* `safety: 8`, `doc: 15`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SlackHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.288)
- **Top Global Matches:** file_cluster_16: 6.288, file_cluster_15: 6.602, file_cluster_11: 6.84
- **Magnitude:** 135.28 | **LOC:** 268 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.2%), Guard Balance (formerly Safety Score) (66.7%), Complexity Load (formerly Cognitive Load) (42.1%)
- **Documentation Coverage:** 26.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* /** * @param string $token Slack API token * @param string $channel Slack channel (encoded ID or nam...
  * `prepareContentData` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* /** * @return string[] */
  * `finalizeWrite` **(Encapsulated Accessors)** (Impact: 2.4)
    * *Intent:* /** * Finalizes the request by reading some bytes and then closing the socket * * If we do not read ...
  * `buildHeader` **(Encapsulated Accessors)** (Impact: 1.9)
    * *Intent:* /** * Builds the header of the API Call */
  * `setFormatter` **(Parameter Forwarders)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 45`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`, `unreferenced_by_name: 9`
* *Architecture:* `io: 7`, `api: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Monolog\Formatter\FormatterInterface, Monolog\Handler\Slack\SlackRecord, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/FingersCrossedHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.058)
- **Top Global Matches:** file_cluster_15: 6.058, file_cluster_11: 6.755, file_cluster_16: 7.179
- **Magnitude:** 134.7 | **LOC:** 243 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **10**; blast radius 2.549; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.7%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (31.8%)
- **Documentation Coverage:** 9.5238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__construct` **(Many-Argument Workhorses)** (Impact: 11.6)
    * *Intent:* /** * @phpstan-param (Closure(LogRecord|null, HandlerInterface): HandlerInterface)|HandlerInterface ...
  * `handle` **(Compute Cores)** (Impact: 10.9)
    * *Intent:* /** * @inheritDoc */
  * `getHandler` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** * Return the nested handler * * If the handler was provided as a factory, this will trigger the ...
  * `flushBuffer` **(Stateful Encapsulated Methods)** (Impact: 3.8)
    * *Intent:* /** * Resets the state of the handler. Stops forwarding records to the wrapped handler. */
  * `activate` **(Interface Declarations)** (Impact: 3.5)
    * *Intent:* /** * Manually activate this logger regardless of the activation strategy */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 40`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`, `unreferenced_by_name: 7`
* *Architecture:* `api: 10`, `import: 10`
* *Defense:* `safety: 6`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.549
  * `Choke Point (Betweenness):` 0.000156 | `Ripple Effect (Closeness):` 0.008511
  * `Imports (Out-Degree: 8):` Closure, Monolog\Formatter\FormatterInterface, Monolog\Handler\FingersCrossed\ActivationStrategyInterface, Monolog\Handler\FingersCrossed\ErrorLevelActivationStrategy, Monolog\Level, Monolog\LogRecord, Monolog\Logger, Monolog\ResettableInterface...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/Monolog/Handler/RotatingFileHandlerTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.944)
- **Top Global Matches:** file_cluster_10: 7.944, file_cluster_16: 8.003, file_cluster_11: 8.027
- **Magnitude:** 133.36 | **LOC:** 344 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (55.6%), Complexity Load (formerly Cognitive Load) (11.3%), Connectivity (formerly Api Exposure) (7.2%)
- **Documentation Coverage:** 93.5484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rrmdir` **(Stateful Encapsulated Methods)** (Impact: 9.5)
  * `testRotation` **(Many-Argument Workhorses)** (Impact: 5.4)
  * `testRotationWithFolderByDate` **(Many-Argument Workhorses)** (Impact: 5.4)
  * `tearDown` **(I/O & Config Routines)** (Impact: 4.9)
  * `assertErrorWasTriggered` **(Stateful Encapsulated Methods)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 57`, `args: 24`, `func_start: 17`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`, `unreferenced_by_name: 9`
* *Architecture:* `io: 5`, `api: 14`, `import: 2`
* *Defense:* `safety: 1`, `doc: 1`, `test: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/DeduplicationHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.697)
- **Top Global Matches:** file_cluster_9: 7.697, file_cluster_16: 8.344, file_cluster_15: 10.071
- **Magnitude:** 133.28 | **LOC:** 184 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.463; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.2%), Complexity Load (formerly Cognitive Load) (45.9%), Debt Markers (formerly Tech Debt) (36.0%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isDuplicate` **(Stateful Encapsulated Methods)** (Impact: 15.2)
    * *Intent:* /** * If there is a store entry older than e.g. a day, this method should set `$this->gc` to `true` ...
  * `flush` **(I/O & Config Routines)** (Impact: 13.9)
  * `collectLogs` **(I/O & Config Routines)** (Impact: 10.8)
  * `__construct` **(Many-Argument Workhorses)** (Impact: 7.7)
    * *Intent:* /** * @param HandlerInterface $handler Handler. * @param string|null $deduplicationStore The file/pa...
  * `buildDeduplicationStoreEntry` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * @return string The given record serialized as a single line of text */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 4`
* *Defense:* `doc: 4`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.463
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Logger, Psr\Log\LogLevel
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/Monolog/Formatter/LineFormatterTest.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 5.785)
- **Top Global Matches:** file_cluster_11: 5.785, file_cluster_10: 7.214, file_cluster_15: 7.333
- **Magnitude:** 131.86 | **LOC:** 352 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.9%), Complexity Load (formerly Cognitive Load) (17.7%), Connectivity (formerly Api Exposure) (11.0%), Dead Code Surface (formerly Dead Code) (6.0%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMaxLevelNameLength` **(Parameter Forwarders)** (Impact: 4.5)
  * `testDefFormatWithSoapFaultException` **(I/O & Config Routines)** (Impact: 3.5)
  * `testDefFormatWithExceptionAndStacktraceParserCustom` **(Callbacks & Closures)** (Impact: 2.8)
  * `providerMaxLevelNameLength` **(I/O & Config Routines)** (Impact: 2.1)
  * `testBatchFormat` **(I/O & Config Routines)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 75`, `args: 26`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 51`, `dead_code: 1`, `unreferenced_by_name: 22`
* *Architecture:* `io: 1`, `api: 24`, `import: 4`
* *Defense:* `doc: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\Test\MonologTestCase, PHPUnit\Framework\Attributes\DataProvider, RuntimeException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/RotatingFileHandler.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.455)
- **Top Global Matches:** file_cluster_16: 5.455, file_cluster_15: 7.006, file_cluster_11: 7.029
- **Magnitude:** 130.9 | **LOC:** 235 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.758; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (66.9%), Debt Markers (formerly Tech Debt) (36.3%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rotate` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* /** * Rotates the files. */
  * `write` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* /** * @inheritDoc */
  * `__construct` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * @param int $maxFiles The maximal amount of files to keep (0 means unlimited) * @param int|null...
  * `setFilenameFormat` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* /** * @return $this */
  * `getGlobPattern` **(Stateful Encapsulated Methods)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 37`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.758
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.004255
  * `Imports (Out-Degree: 4):` DateTimeZone, InvalidArgumentException, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/GelfMessageFormatter.php` (PHP | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.988)
- **Top Global Matches:** file_cluster_8: 6.988, file_cluster_6: 17.465, file_cluster_3: 19.948
- **Magnitude:** 128.5 | **LOC:** 153 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 3.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.5%), Complexity Load (formerly Cognitive Load) (39.6%), Connectivity (formerly Api Exposure) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Compute Cores)** (Impact: 34.4)
    * *Intent:* /** * @inheritDoc */
  * `__construct` **(Compute Cores)** (Impact: 20.8)
    * *Intent:* /** * @throws \RuntimeException */
  * `getGraylog2Priority` **(Stateful Encapsulated Methods)** (Impact: 3.5)
    * *Intent:* /** * Translates Monolog log levels to Graylog2 log priorities. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 18`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 4`, `doc: 10`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.592
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.012766
  * `Imports (Out-Degree: 3):` Gelf\Message, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/Monolog/Handler/RotatingFileHandlerTest.php` (PHP) | Magnitude: 133.36 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 271, structural_boundaries: 57, state_mutation: 36, time_date_logic: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Monolog/Handler/PsrHandler.php` (PHP) | Magnitude: 31.18 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 18, state_mutation: 9, doc: 6
- `tests/Monolog/Handler/ElasticsearchHandlerTest.php` (PHP) | Magnitude: 109.94 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 48, state_mutation: 30, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Monolog/Handler/AmqpHandler.php` (PHP) | Magnitude: 91.34 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 30, state_mutation: 18, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Monolog/Handler/TestHandler.php` (PHP) | Magnitude: 77.74 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 36, args: 14, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/Monolog/Formatter/SyslogFormatterTest.php` (PHP) | Magnitude: 39.44 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 73, structural_boundaries: 19, scientific: 10, memory_alloc: 8
- `src/Monolog/Registry.php` (PHP) | Magnitude: 55.26 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 16, branch: 9, state_mutation: 8
- `src/Monolog/Handler/ProcessableHandlerTrait.php` (PHP) | Magnitude: 21.42 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 16, branch: 4, args: 4
- `src/Monolog/Handler/FallbackGroupHandler.php` (PHP) | Magnitude: 29.26 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 14, branch: 7, safety: 7
- `src/Monolog/Formatter/LogglyFormatter.php` (PHP) | Magnitude: 10.14 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 8, state_mutation: 4, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/Monolog/Handler/BrowserConsoleHandlerTest.php` (PHP) | Magnitude: 35.5 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 22, state_mutation: 14, args: 8
- `tests/Monolog/Handler/CouchDBHandlerTest.php` (PHP) | Magnitude: 4.92 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, safety: 2, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/Monolog/Handler/DeduplicationHandlerTest.php` (PHP) | Magnitude: 36.6 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 89, structural_boundaries: 26, test: 22, state_mutation: 17
- `tests/Monolog/Handler/NullHandlerTest.php` (PHP) | Magnitude: 11.4 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, test: 6, state_mutation: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/continuous-integration.yml` -> Churn: **100.0%** | Cog Load: 4.6668% | Debt: 51.932%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Monolog/Formatter/NormalizerFormatter.php` -> **Tom Molloy** (100.0% isolated ownership) | Magnitude: 260.06
- `tests/Monolog/Formatter/NormalizerFormatterTest.php` -> **Tom Molloy** (100.0% isolated ownership) | Magnitude: 221.78
- `tests/Monolog/Formatter/JsonFormatterTest.php` -> **Adrien SIMON** (100.0% isolated ownership) | Magnitude: 151.58
- `src/Monolog/Handler/DeduplicationHandler.php` -> **Denis** (100.0% isolated ownership) | Magnitude: 133.28
- `src/Monolog/Handler/RotatingFileHandler.php` -> **omniError** (100.0% isolated ownership) | Magnitude: 130.9

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Monolog/Logger.php` -> **Severity: 0.225** (Bridge: 0.0022 * Flux: 99.9976%)
- `src/Monolog/Handler/TestHandler.php` -> **Severity: 0.068** (Bridge: 0.0007 * Flux: 99.9757%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Monolog/Formatter/NormalizerFormatter.php` -> **Severity: 0.044** (Bridge: 0.0004 * Flux: 100.0%)
- `src/Monolog/Handler/Slack/SlackRecord.php` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Monolog/LogRecord.php` -> **Severity: 28.881** (Embedded: 0.5546 * Error Risk: 52.078%)
- `src/Monolog/Utils.php` -> **Severity: 14.117** (Embedded: 0.192 * Error Risk: 73.5202%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 7.45** (Embedded: 0.094 * Error Risk: 79.2563%)
- `src/Monolog/Logger.php` -> **Severity: 7.378** (Embedded: 0.1268 * Error Risk: 58.1746%)
- `src/Monolog/JsonSerializableDateTimeImmutable.php` -> **Severity: 6.645** (Embedded: 0.1227 * Error Risk: 54.1334%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Monolog/LogRecord.php` -> **Severity: 14400.517** (Blast Radius: 168.006 * Doc Risk: 85.7143%)
- `src/Monolog/Level.php` -> **Severity: 2383.1** (Blast Radius: 95.324 * Doc Risk: 25.0%)
- `src/Monolog/Utils.php` -> **Severity: 1191.675** (Blast Radius: 31.778 * Doc Risk: 37.5%)
- `src/Monolog/JsonSerializableDateTimeImmutable.php` -> **Severity: 706.0** (Blast Radius: 10.59 * Doc Risk: 66.6667%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 421.422** (Blast Radius: 14.223 * Doc Risk: 29.6296%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5345 call pairs -- scoped 15.2%, unique 10.5%, ambiguous 21.2%, external 53.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| php | 5345 | 15.2% | 10.5% | 21.2% | 53.1% |

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
