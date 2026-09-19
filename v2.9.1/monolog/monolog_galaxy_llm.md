# ARCHITECTURAL_BRIEF: monolog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Seldaek/monolog.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 227 analyzed artifact(s), 17095 LOC.
- **Load-bearing artifact:** `src/Monolog/Level.php` -- 126 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Monolog/Handler/SlackHandler.php` -- pulls in 24 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `tests/Monolog/LoggerTest.php` at magnitude 322.14 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 227 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 17095 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 91.5% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.364 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2894 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4215 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 216 | 17012 | 95.2% |
| MARKDOWN | 9 | 0 | 4.0% |
| YAML | 1 | 1 | 0.4% |
| JSON | 1 | 82 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.406`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.41; from the repo's file-archetype mix)
> **File Composition:** Interface Declarations Files 27%, Encapsulated Accessors Files 15%, Large Core Modules (3) 12%, Parameter Forwarders Files 11%, Large Core Modules (2) 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 218 | 96.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 2x Excluded (Unsupported Extension: '.neon')
- `.dist`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.php`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.8 | 14.5 | 7.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 66.5 | 68.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.7 | 0.3 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.9 | 5.6 | 5.6 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 98.8 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 30.8 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.0 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.2 | 13.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 865 | 153 | 10 | `tests/Monolog/LoggerTest.php` |
| cleanup | 68 | 45 | 1 | `tests/Monolog/Formatter/NormalizerFormatterTest.php` |
| guards | 1104 | 158 | 13 | `src/Monolog/Logger.php` |
| danger | 210 | 79 | 2 | `tests/Monolog/Handler/NativeMailerHandlerTest.php` |
| concurrency | 22 | 8 | 0 | `tests/Monolog/Processor/ClosureContextProcessorTest.php` |
| connectivity | 1134 | 208 | 10 | `tests/Monolog/LoggerTest.php` |
| io | 182 | 36 | 3 | `src/Monolog/Handler/SyslogUdp/UdpSocket.php` |
| crypto | 0 | 0 | 0 | - |
| ipc | 41 | 18 | 0 | `src/Monolog/Handler/DeduplicationHandler.php` |
| time | 123 | 29 | 1 | `tests/Monolog/Handler/RotatingFileHandlerTest.php` |
| serialization | 62 | 22 | 0 | `tests/Monolog/Formatter/LogstashFormatterTest.php` |
| regex | 32 | 15 | 0 | `src/Monolog/Formatter/LineFormatter.php` |
| events | 17 | 6 | 0 | `tests/Monolog/Handler/AbstractProcessingHandlerTest.php` |
| tests | 920 | 91 | 11 | `tests/Monolog/LoggerTest.php` |
| docs | 1090 | 197 | 11 | `src/Monolog/Logger.php` |
| debt | 36 | 17 | 0 | `tests/Monolog/LoggerTest.php` |
| mutation | 3236 | 200 | 32 | `tests/Monolog/LoggerTest.php` |
| dead_code | 866 | 175 | 8 | `tests/Monolog/LoggerTest.php` |
| credential | 2 | 2 | 0 | `src/Monolog/Handler/ChromePHPHandler.php` |
| threat | 49 | 36 | 1 | `tests/Monolog/Formatter/NormalizerFormatterTest.php` |
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
2. **LogRecord.php** (`src/Monolog/LogRecord.php`) — 105 inbound connections
3. **FormatterInterface.php** (`src/Monolog/Formatter/FormatterInterface.php`) — 38 inbound connections
4. **Utils.php** (`src/Monolog/Utils.php`) — 27 inbound connections
5. **LineFormatter.php** (`src/Monolog/Formatter/LineFormatter.php`) — 20 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **SlackHandler.php** (`src/Monolog/Handler/SlackHandler.php`) — 24 outbound dependencies
2. **PushoverHandler.php** (`src/Monolog/Handler/PushoverHandler.php`) — 20 outbound dependencies
3. **SlackWebhookHandler.php** (`src/Monolog/Handler/SlackWebhookHandler.php`) — 18 outbound dependencies
4. **PHPConsoleHandler.php** (`src/Monolog/Handler/PHPConsoleHandler.php`) — 17 outbound dependencies
5. **SignalHandlerTest.php** (`tests/Monolog/SignalHandlerTest.php`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addRecord` **(Many-Argument Workhorses)** (@ `src/Monolog/Logger.php`) -> Impact: **53.2** | LOC: 80
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
| `src/Monolog/Handler` | 67 | 4057.26 | 21.83% | 77.57% |
| `tests/Monolog/Handler` | 54 | 2209.44 | 5.86% | 0.0% |
| `src/Monolog/Formatter` | 19 | 1416.8 | 23.74% | 19.85% |
| `src/Monolog` | 10 | 1015.98 | 23.99% | 17.45% |
| `tests/Monolog/Formatter` | 17 | 966.08 | 7.09% | 0.0% |
| `tests/Monolog` | 6 | 656.14 | 7.99% | 0.0% |
| `src/Monolog/Processor` | 15 | 428.52 | 19.39% | 65.75% |
| `src/Monolog/Handler/Slack` | 1 | 267.36 | 33.97% | 0.0% |
| `tests/Monolog/Processor` | 13 | 234.48 | 1.44% | 0.0% |
| `tests/Monolog/Handler/Slack` | 1 | 157.7 | 29.2% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Monolog/Handler/HandlerWrapper.php` -> **100.0%** Exposure
- `src/Monolog/Handler/AbstractHandler.php` -> **99.9972%** Exposure
- `src/Monolog/Handler/MailHandler.php` -> **99.9797%** Exposure
- `src/Monolog/Registry.php` -> **99.9797%** Exposure
- `src/Monolog/Handler/ElasticaHandler.php` -> **99.9659%** Exposure
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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `809` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `tests/Monolog/LoggerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 322.14 | **LOC:** 920 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.4%), Concurrency Surface (formerly Concurrency) (42.0%), Complexity Load (formerly Cognitive Load) (14.7%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 38.6139% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testUseMicrosecondTimestamps` **(Defensive Guards)** (Impact: 4.8)
    * *Intent:* /** * @covers Logger::useMicrosecondTimestamps * @covers Logger::addRecord */
  * `testReset` **(I/O & Config Routines)** (Impact: 4.6)
  * `testTimezoneIsRespectedInUTC` **(Interface Declarations)** (Impact: 3.9)
    * *Intent:* /** * @covers Logger::setTimezone * @covers JsonSerializableDateTimeImmutable::__construct */
  * `testTimezoneIsRespectedInOtherTimezone` **(I/O & Config Routines)** (Impact: 3.9)
    * *Intent:* /** * @covers Logger::setTimezone * @covers JsonSerializableDateTimeImmutable::__construct */
  * `testConvertRFC5424ToMonologLevelInAddRecordAndLog` **(I/O & Config Routines)** (Impact: 3.3)
    * *Intent:* /** * @covers Monolog\Logger::addRecord * @covers Monolog\Logger::log */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 146
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 176`, `args: 63`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 124`, `duplicate_logic: 6`, `unreferenced_by_name: 38`
* *Architecture:* `api: 49`, `concurrency: 4`, `import: 5`
* *Defense:* `safety: 5`, `doc: 30`, `test: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` 'Y-m-d\TH:i:sP'], 'assertNotSame', Monolog\Handler\HandlerInterface, Monolog\Handler\TestHandler, Monolog\Processor\WebProcessor, Monolog\Test\MonologTestCase, PHPUnit\Framework\Attributes\DataProvider, ]...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Logger.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 316.28 | **LOC:** 752 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **13**; blast radius 16.178; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.2%), Connectivity (formerly Api Exposure) (69.9%), Complexity Load (formerly Cognitive Load) (44.1%)
- **Documentation Coverage:** 5.9701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addRecord` **(Many-Argument Workhorses)** (Impact: 53.2)
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
* *Structure:* `branch: 45`, `structural_boundaries: 104`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 56`
* *Architecture:* `api: 42`, `concurrency: 2`, `import: 14`
* *Defense:* `safety: 23`, `doc: 48`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.178
  * `Choke Point (Betweenness):` 0.001298 | `Ripple Effect (Closeness):` 0.094482
  * `Imports (Out-Degree: 2):` Closure, DateTimeZone, Fiber, Monolog\Handler\HandlerInterface, Monolog\Processor\ProcessorInterface, Psr\Log\InvalidArgumentException, Psr\Log\LogLevel, Psr\Log\LoggerInterface...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/LineFormatter.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 297.1 | **LOC:** 318 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **10**; blast radius 16.491; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.4%), Complexity Load (formerly Cognitive Load) (36.1%), Connectivity (formerly Api Exposure) (33.0%)
- **Documentation Coverage:** 29.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Compute Cores)** (Impact: 23.9)
    * *Intent:* /** * @inheritDoc */
  * `formatException` **(Stateful Encapsulated Methods)** (Impact: 15.8)
  * `__construct` **(Many-Argument Workhorses)** (Impact: 10.2)
    * *Intent:* /** * @param string|null $format The format of the message * @param string|null $dateFormat The form...
  * `stacktracesParser` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `replaceNewlines` **(Stateful Encapsulated Methods)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 173
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 48`, `args: 17`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 61`, `fragile_debt: 2`
* *Architecture:* `api: 12`, `import: 5`
* *Defense:* `safety: 10`, `doc: 11`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.491
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.088697
  * `Imports (Out-Degree: 2):` ?Closure $parser = null): self
    
        $this->includeStacktraces = $include, Closure, Monolog\LogRecord, Monolog\Utils, Stacktraces, Stacktraces = false)
    
        $this->format = $format === null ? static::SIMPLE_FORMAT : $format, Stacktraces($includeStacktraces, Stacktraces(bool $include = true...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/Slack/SlackRecord.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 267.36 | **LOC:** 382 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 4.351; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Connectivity (formerly Api Exposure) (36.0%), Complexity Load (formerly Cognitive Load) (34.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.351
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.017699
  * `Imports (Out-Degree: 5):` 'context'], ContextAndExtra = false, ContextAndExtra(bool $includeContextAndExtra = false): self
    
        $this->includeContextAndExtra = $includeContextAndExtra, ContextAndExtra) 
                foreach (['extra', ContextAndExtra) 
            $this->normalizerFormatter = new NormalizerFormatter(, FormatterInterface|null $formatter = null
    ) 
        $this
            ->setChannel($channel)
            ->setUsername($username)
            ->useAttachment($useAttachment)
            ->setUserIcon($userIcon)
            ->useShortAttachment($useShortAttachment)
            ->includeContextAndExtra($includeContextAndExtra)
            ->excludeFields($excludeFields)
            ->setFormatter($formatter, Monolog\Formatter\FormatterInterface, Monolog\Formatter\NormalizerFormatter...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/NormalizerFormatter.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 260.06 | **LOC:** 373 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 5.673; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Complexity Load (formerly Cognitive Load) (45.7%), Connectivity (formerly Api Exposure) (41.1%)
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
* *Risk/State:* `state_mutation: 47`, `dead_code: 1`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 18`, `doc: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.673
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.031606
  * `Imports (Out-Degree: 3):` 
    public function getMaxTraceLength(): ?int
    
        return $this->maxTraceLength, Monolog\JsonSerializableDateTimeImmutable, Monolog\LogRecord, Monolog\Utils, Throwable
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `tests/Monolog/Formatter/NormalizerFormatterTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 221.78 | **LOC:** 591 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (24.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.3%), Connectivity (formerly Api Exposure) (10.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Monolog\Level, s the soap extension'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SocketHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 208.48 | **LOC:** 437 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.3%), Guard Balance (formerly Safety Score) (88.2%), Complexity Load (formerly Cognitive Load) (40.5%)
- **Documentation Coverage:** 19.1489% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeToSocket` **(Stateful Encapsulated Methods)** (Impact: 18.4)
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
* *Structure:* `branch: 36`, `structural_boundaries: 76`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 38`, `unreferenced_by_name: 13`
* *Architecture:* `io: 6`, `api: 15`, `import: 2`
* *Defense:* `safety: 1`, `doc: 25`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/StreamHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 206.26 | **LOC:** 281 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.929; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.5%), Complexity Load (formerly Cognitive Load) (35.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.7%)
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
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 41`, `args: 14`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 40`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 3`
* *Defense:* `safety: 4`, `doc: 12`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.929
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.004425
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/ErrorHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 191.6 | **LOC:** 280 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.767; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (33.8%), Connectivity (formerly Api Exposure) (10.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.767
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004425
  * `Imports (Out-Degree: 0):` Closure, Psr\Log\LogLevel, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Utils.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 190.2 | **LOC:** 258 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); blast radius 30.238; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.1%), Connectivity (formerly Api Exposure) (48.5%), Complexity Load (formerly Cognitive Load) (45.8%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expandIniShorthandBytes` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* /** * Converts a string with a valid 'memory_limit' format, to bytes. * * @param string|false $val *...
  * `handleJsonError` **(Many-Argument Workhorses)** (Impact: 17.3)
    * *Intent:* /** * Handle a json_encode failure. * * If the failure is due to invalid string encoding, try to cle...
  * `jsonEncode` **(Compute Cores)** (Impact: 13.1)
    * *Intent:* /** * Return the JSON representation of a value * * @param mixed $data * @param int $encodeFlags fla...
  * `detectAndCleanUtf8` **(Stateful Encapsulated Methods)** (Impact: 9.7)
    * *Intent:* * Detect invalid UTF-8 string characters and convert to valid UTF-8. * * Valid UTF-8 input will be l...
  * `canonicalizePath` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* /** * Makes sure if a relative path is passed in it is turned into an absolute path * * @param strin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 33`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 29`
* *Architecture:* `api: 7`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.238
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.157349
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/BrowserConsoleHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 161.46 | **LOC:** 301 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Debt Markers (formerly Tech Debt) (49.0%), Complexity Load (formerly Cognitive Load) (32.7%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleCustomStyles` **(Stateful Encapsulated Methods)** (Impact: 11.7)
  * `generateScript` **(Stateful Encapsulated Methods)** (Impact: 8.1)
  * `dump` **(Stateful Encapsulated Methods)** (Impact: 7.8)
    * *Intent:* /** * @param mixed[] $dict * @return mixed[] */
  * `getResponseFormatFromContentType` **(Stateful Encapsulated Methods)** (Impact: 6.4)
    * *Intent:* /** * @return string One of 'js', 'html' or 'unknown' * @phpstan-return self::FORMAT_* */
  * `send` **(I/O & Config Routines)** (Impact: 5.8)
    * *Intent:* /** * Convert records to javascript console commands and send it to the browser. * This method is au...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 59`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 4`
* *Architecture:* `io: 3`, `api: 4`, `import: 7`
* *Defense:* `safety: 1`, `doc: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Monolog\Formatter\FormatterInterface, Monolog\Formatter\LineFormatter, Monolog\Level, Monolog\LogRecord, Monolog\Utils, 
class BrowserConsoleHandler extends AbstractProcessingHandler

    protected static bool $initialized = false, headers_list, stripos
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/Formatter/JsonFormatterTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 160.48 | **LOC:** 399 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (75.3%), Complexity Load (formerly Cognitive Load) (20.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.6%), Connectivity (formerly Api Exposure) (8.3%)
- **Documentation Coverage:** 74.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatException` **(Stateful Encapsulated Methods)** (Impact: 5.8)
    * *Intent:* /** * @param \Exception|\Throwable $exception */
  * `testDefFormatWithPreviousException` **(Interface Declarations)** (Impact: 2.5)
  * `testFormatWithPrettyPrint` **(I/O & Config Routines)** (Impact: 2.4)
    * *Intent:* /** * @covers Monolog\Formatter\JsonFormatter::format */
  * `formatRecordWithExceptionInContext` **(Stateful Encapsulated Methods)** (Impact: 2.3)
  * `assertContextContainsFormattedException` **(Encapsulated Accessors)** (Impact: 2.1)
    * *Intent:* /** * @internal param string $exception */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 91`, `args: 29`, `func_start: 27`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 69`, `unreferenced_by_name: 20`
* *Architecture:* `api: 24`, `import: 5`
* *Defense:* `safety: 3`, `doc: 8`, `test: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Exception, JsonSerializable, Monolog\Level, Monolog\LogRecord, Monolog\Test\MonologTestCase
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/Handler/Slack/SlackRecordTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 157.7 | **LOC:** 380 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.9%), Complexity Load (formerly Cognitive Load) (29.2%), Connectivity (formerly Api Exposure) (10.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Monolog\Level, PHPUnit\Framework\Attributes\CoversClass, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PushoverHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 157.32 | **LOC:** 247 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.7%), Debt Markers (formerly Tech Debt) (80.2%), Complexity Load (formerly Cognitive Load) (40.9%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` $users, ?float $connectionTimeout = null, api.pushover.net:443' : 'api.pushover.net:80', ?string $title = null, Monolog\Level, Monolog\LogRecord, Monolog\Logger, Monolog\Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/SignalHandlerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 155.54 | **LOC:** 293 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (88.6%), Guard Balance (formerly Safety Score) (85.9%), Complexity Load (formerly Cognitive Load) (25.1%), Connectivity (formerly Api Exposure) (6.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` $callPrevious, $desiredAsync, $expected)
    
        $this->setSignalHandler($signo, $expectedAfter)
    
        $this->setSignalHandler(SIGURG, $expectedBefore, Monolog\Handler\StreamHandler, Monolog\Handler\TestHandler, Monolog\Test\MonologTestCase...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/TelegramBotHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 152.6 | **LOC:** 302 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Debt Markers (formerly Tech Debt) (45.8%), Complexity Load (formerly Cognitive Load) (32.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Utils, RuntimeException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PHPConsoleHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 150.46 | **LOC:** 304 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.3%), Debt Markers (formerly Tech Debt) (76.0%), Complexity Load (formerly Cognitive Load) (36.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` php-console#troubleshooting-with-_session-handler-overridden-in-some-frameworks)
    ],  bool Autodetect and append trace data to debug
        'dataStorage' => null,  bool Convert callback items in dumper vars to (callback SomeClass::someMethod) strings
        'dumperLevelLimit' => 5,  int Maximum approximate size of dumped vars result formatted in JSON
        'detectDumpTraceAndSource' => false,  int Maximum dumped var same level array items or object properties number
        'dumperItemSizeLimit' => 5000,  int Maximum dumped vars array or object nested dump level
        'dumperItemsCountLimit' => 100,  int Maximum length of any string or dumped array item
        'dumperDumpSizeLimit' => 500000, Monolog\Formatter\FormatterInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/Formatter/LineFormatterTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 139.86 | **LOC:** 352 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (20.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.6%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testMaxLevelNameLength` **(Parameter Forwarders)** (Impact: 4.5)
  * `testDefFormatWithPreviousException` **(Interface Declarations)** (Impact: 3.8)
  * `testDefFormatWithSoapFaultException` **(I/O & Config Routines)** (Impact: 3.5)
  * `testDefFormatWithExceptionAndStacktraceParserCustom` **(Callbacks & Closures)** (Impact: 2.8)
  * `providerMaxLevelNameLength` **(I/O & Config Routines)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 75`, `args: 26`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 51`, `dead_code: 1`, `unreferenced_by_name: 22`
* *Architecture:* `io: 1`, `api: 24`, `import: 4`
* *Defense:* `doc: 1`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` 'TestSuite.php') === false) 
                return $line, Monolog\Level, Monolog\Test\MonologTestCase, PHPUnit\Framework\Attributes\DataProvider, RuntimeException, Stacktraces(, Stacktraces(true, function ($line) 
            if (strpos($line...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/Handler/StreamHandlerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 139.62 | **LOC:** 381 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.3%), Complexity Load (formerly Cognitive Load) (12.3%), Connectivity (formerly Api Exposure) (10.5%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testPreventOOMError` **(Defensive Guards)** (Impact: 6.4)
  * `testWriteErrorDuringWriteRetriesWithClose` **(I/O & Config Routines)** (Impact: 5.3)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::__construct * @covers Monolog\Handler\StreamHandler::wr...
  * `testWriteErrorDuringWriteRetriesButThrowsIfStillFails` **(I/O & Config Routines)** (Impact: 4.2)
  * `testWriteNonExistingAndNotCreatablePath` **(Defensive Guards)** (Impact: 4.0)
  * `testWriteInvalidResource` **(I/O & Config Routines)** (Impact: 3.0)
    * *Intent:* /** * @covers Monolog\Handler\StreamHandler::__construct * @covers Monolog\Handler\StreamHandler::wr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 53`, `args: 24`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 43`, `unreferenced_by_name: 19`
* *Architecture:* `io: 6`, `api: 22`, `import: 3`
* *Defense:* `safety: 8`, `doc: 15`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Monolog\Level, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/RotatingFileHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 136.6 | **LOC:** 235 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Debt Markers (formerly Tech Debt) (44.0%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rotate` **(I/O & Config Routines)** (Impact: 12.7)
    * *Intent:* /** * Rotates the files. */
  * `setDateFormat` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `write` **(Stateful Encapsulated Methods)** (Impact: 8.0)
    * *Intent:* /** * @inheritDoc */
  * `__construct` **(Many-Argument Workhorses)** (Impact: 6.8)
    * *Intent:* /** * @param int $maxFiles The maximal amount of files to keep (0 means unlimited) * @param int|null...
  * `setFilenameFormat` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* /** * @return $this */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 37`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` DateTimeZone, InvalidArgumentException, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SlackHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 135.28 | **LOC:** 268 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.0%), Guard Balance (formerly Safety Score) (90.2%), Complexity Load (formerly Cognitive Load) (42.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` $excludeFields, $level = Level::Critical, 
    public function __construct(
        string $token, ?float $connectionTimeout = null, ?int $chunkSize = null
    ) 
        if (!\extension_loaded('openssl')) 
            throw new MissingExtensionException('The OpenSSL PHP extension is required to use the SlackHandler', ?string $iconEmoji = null, ?string $username = null, ContextAndExtra...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/FingersCrossedHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 134.7 | **LOC:** 243 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (96.3%), Guard Balance (formerly Safety Score) (92.9%), Complexity Load (formerly Cognitive Load) (31.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` Closure, Monolog\Formatter\FormatterInterface, Monolog\Handler\FingersCrossed\ActivationStrategyInterface, Monolog\Handler\FingersCrossed\ErrorLevelActivationStrategy, Monolog\Level, Monolog\LogRecord, Monolog\Logger, Monolog\ResettableInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/DeduplicationHandler.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 134.28 | **LOC:** 184 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.282; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.2%), Debt Markers (formerly Tech Debt) (47.6%), Complexity Load (formerly Cognitive Load) (46.3%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isDuplicate` **(Stateful Encapsulated Methods)** (Impact: 15.2)
    * *Intent:* /** * If there is a store entry older than e.g. a day, this method should set `$this->gc` to `true` ...
  * `flush` **(I/O & Config Routines)** (Impact: 13.9)
  * `collectLogs` **(I/O & Config Routines)** (Impact: 11.8)
  * `__construct` **(Many-Argument Workhorses)** (Impact: 7.7)
    * *Intent:* /** * @param HandlerInterface $handler Handler. * @param string|null $deduplicationStore The file/pa...
  * `buildDeduplicationStoreEntry` **(Encapsulated Accessors)** (Impact: 1.6)
    * *Intent:* /** * @return string The given record serialized as a single line of text */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`, `unreferenced_by_name: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 4`
* *Defense:* `doc: 4`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Logger, Psr\Log\LogLevel, all those above $deduplicationLevel are checked
 * against the existing stored logs. If they match and the timestamps in the stored log is
 * not older than $time seconds, s the BufferHandler functionality and will buffer
 * all messages until the end of the request or flush() is called.
 *
 * This works by storing all log records' messages above $deduplicationLevel
 * to the file specified by $deduplicationStore. When further logs come in at the end of the
 * request (or when flush() is called), the
 * whole data set is discarded.
 *
 * This is mainly useful in combination with Mail handlers or things like Slack or HipChat handlers
 * that send messages to people, the new log record is discarded. If no log record is new...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Monolog/Handler/RotatingFileHandlerTest.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 133.36 | **LOC:** 344 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.282; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.2%), Complexity Load (formerly Cognitive Load) (11.3%), Connectivity (formerly Api Exposure) (7.2%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.282
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` InvalidArgumentException, PHPUnit\Framework\Attributes\DataProvider
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/GelfMessageFormatter.php` (PHP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 128.5 | **LOC:** 153 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 3.737; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.3%), Complexity Load (formerly Cognitive Load) (39.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (11.6%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.737
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.00885
  * `Imports (Out-Degree: 3):` Gelf\Message, Monolog\Level, Monolog\LogRecord, Monolog\Utils, d to use Monolog\'s GelfMessageFormatter'
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Monolog/Formatter/LineFormatter.php` -> **angeljqv** (100.0% isolated ownership) | Magnitude: 297.1
- `src/Monolog/Formatter/NormalizerFormatter.php` -> **Tom Molloy** (100.0% isolated ownership) | Magnitude: 260.06
- `tests/Monolog/Formatter/NormalizerFormatterTest.php` -> **Tom Molloy** (100.0% isolated ownership) | Magnitude: 221.78
- `tests/Monolog/Formatter/JsonFormatterTest.php` -> **Adrien SIMON** (100.0% isolated ownership) | Magnitude: 160.48
- `src/Monolog/Handler/TelegramBotHandler.php` -> **Dawid Nowak** (100.0% isolated ownership) | Magnitude: 152.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Monolog/Logger.php` -> **Severity: 0.13** (Bridge: 0.0013 * Flux: 99.9976%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Monolog/Handler/TestHandler.php` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.9757%)
- `src/Monolog/Formatter/NormalizerFormatter.php` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 100.0%)
- `src/Monolog/Handler/Slack/SlackRecord.php` -> **Severity: 0.024** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Monolog/LogRecord.php` -> **Severity: 30.687** (Embedded: 0.4954 * Error Risk: 61.943%)
- `src/Monolog/Utils.php` -> **Severity: 15.121** (Embedded: 0.1573 * Error Risk: 96.1011%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 8.729** (Embedded: 0.0887 * Error Risk: 98.4141%)
- `src/Monolog/Logger.php` -> **Severity: 7.013** (Embedded: 0.0945 * Error Risk: 74.2237%)
- `src/Monolog/JsonSerializableDateTimeImmutable.php` -> **Severity: 4.327** (Embedded: 0.0619 * Error Risk: 69.8465%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Monolog/LogRecord.php` -> **Severity: 13635.517** (Blast Radius: 159.081 * Doc Risk: 85.7143%)
- `src/Monolog/Level.php` -> **Severity: 3431.45** (Blast Radius: 137.258 * Doc Risk: 25.0%)
- `src/Monolog/Utils.php` -> **Severity: 1133.925** (Blast Radius: 30.238 * Doc Risk: 37.5%)
- `src/Monolog/Test/MonologTestCase.php` -> **Severity: 705.56** (Blast Radius: 17.639 * Doc Risk: 40.0%)
- `src/Monolog/JsonSerializableDateTimeImmutable.php` -> **Severity: 607.0** (Blast Radius: 9.105 * Doc Risk: 66.6667%)

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
