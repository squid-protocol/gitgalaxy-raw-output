# ARCHITECTURAL_BRIEF: monolog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/monolog` |
| **Timestamp** | `2026-08-03T19:32:52.935977+00:00` |
| **Scan Duration** | `0.52s` |
| **Git Branch** | `main` |
| **Git Commit** | `68b974809baff3f071893de61447212e9e688ee7` |
| **Git Remote** | `https://github.com/Seldaek/monolog.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 124 malicious artifacts.

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
| Total Artifacts | 248 |
| Analyzed Artifacts (Scanned) | 135 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 113 |
| Total LOC | 7258 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 54.4% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2723 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3559 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1092 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 124 | 7175 | 91.9% |
| MARKDOWN | 9 | 0 | 6.7% |
| YAML | 1 | 1 | 0.7% |
| JSON | 1 | 82 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.892`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 100 | 74.1% |
| file_cluster_8 | 24 | 17.8% |
| file_cluster_0 | 1 | 0.7% |
| file_cluster_9 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 6.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 113*

**Composition by Extension & Reason:**
- `.php`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 2x Excluded (Unsupported Extension: '.neon')
- `.dist`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 1x Excluded (Explicitly Denied Extension: '.jpg')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 87.6 | 25.0 | 29.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.2 | 22.1 | 15.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 49.5 | 53.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 34.4 | 2.9 | 80.0 |
| API Exposure | 0.0 | 12.1 | 3.4 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 98.8 | 0.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 79.1 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 93.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.0 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 59.2 | 70.6 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 79.4 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 41.2 | 2.1 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Monolog/Handler/SyslogUdp/UdpSocket.php` (Hits: 15)
- `src/Monolog/Handler/FirePHPHandler.php` (Hits: 9)
- `src/Monolog/Handler/SyslogUdpHandler.php` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **LogRecord.php** (`src/Monolog/LogRecord.php`) — 97 inbound connections
2. **Level.php** (`src/Monolog/Level.php`) — 62 inbound connections
3. **FormatterInterface.php** (`src/Monolog/Formatter/FormatterInterface.php`) — 38 inbound connections
4. **Utils.php** (`src/Monolog/Utils.php`) — 27 inbound connections
5. **Logger.php** (`src/Monolog/Logger.php`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **SlackHandler.php** (`src/Monolog/Handler/SlackHandler.php`) — 24 outbound dependencies
2. **PushoverHandler.php** (`src/Monolog/Handler/PushoverHandler.php`) — 20 outbound dependencies
3. **SlackWebhookHandler.php** (`src/Monolog/Handler/SlackWebhookHandler.php`) — 18 outbound dependencies
4. **PHPConsoleHandler.php** (`src/Monolog/Handler/PHPConsoleHandler.php`) — 17 outbound dependencies
5. **SlackRecord.php** (`src/Monolog/Handler/Slack/SlackRecord.php`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `addRecord` (@ `src/Monolog/Logger.php`) -> Impact: **223.1** | LOC: 80
- `handleSignal` (@ `src/Monolog/SignalHandler.php`) -> Impact: **220.2** | LOC: 39
- `normalize` (@ `src/Monolog/Formatter/JsonFormatter.php`) -> Impact: **158.7** | LOC: 57
- `format` (@ `src/Monolog/Formatter/LineFormatter.php`) -> Impact: **152.7** | LOC: 53
- `write` (@ `src/Monolog/Handler/NewRelicHandler.php`) -> Impact: **149.3** | LOC: 46
  * *Intent:* /** * @inheritDoc */
- `getSlackData` (@ `src/Monolog/Handler/Slack/SlackRecord.php`) -> Impact: **143.8** | LOC: 75
- `__invoke` (@ `src/Monolog/Processor/PsrLogMessageProcessor.php`) -> Impact: **134.1** | LOC: 42
- `initConnector` (@ `src/Monolog/Handler/PHPConsoleHandler.php`) -> Impact: **119.1** | LOC: 54
  * *Intent:* * ipMasks: string[], * enableEvalListener: bool, * dumperDetectCallbacks: bool, * dumperLevelLimit: int, * dumperItemsCountLimit: int, * dumperItemSiz...
- `format` (@ `src/Monolog/Formatter/GelfMessageFormatter.php`) -> Impact: **113.2** | LOC: 65
- `__construct` (@ `src/Monolog/Handler/LogmaticHandler.php`) -> Impact: **98.7** | LOC: 35
  * *Intent:* /** * @author Julien Breux <julien.breux@gmail.com> */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `normalize` (@ `src/Monolog/Formatter/JsonFormatter.php`) -> **O(2^N) [Recursive]**
- `handleSignal` (@ `src/Monolog/SignalHandler.php`) -> **O(2^N) [Recursive]**
- `normalizeRecord` (@ `src/Monolog/Formatter/JsonFormatter.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * @inheritDoc */
- `format` (@ `src/Monolog/Formatter/LineFormatter.php`) -> **O(2^N) [Recursive]**
- `formatArray` (@ `src/Monolog/Formatter/MongoDBFormatter.php`) -> **O(2^N) [Recursive]**
- `handleBatch` (@ `src/Monolog/Handler/AmqpHandler.php`) -> **O(2^N) [Recursive]**
- `__construct` (@ `src/Monolog/Handler/CubeHandler.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Logs to Cube. * * @link https://github.com/square/cube/wiki * @author Wan Chen <kami@kamisama.me>
- `__construct` (@ `src/Monolog/Handler/ElasticaHandler.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Elastic Search handler
- `__construct` (@ `src/Monolog/Handler/ElasticsearchHandler.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Elasticsearch handler * * @link https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html *
- `handleBatch` (@ `src/Monolog/Handler/FallbackGroupHandler.php`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `getSocket` (@ `src/Monolog/Handler/SyslogUdp/UdpSocket.php`) -> DB Complexity: **25**
- `buildHeader` (@ `src/Monolog/Handler/FlowdockHandler.php`) -> DB Complexity: **23**
- `buildHeader` (@ `src/Monolog/Handler/PushoverHandler.php`) -> DB Complexity: **23**
- `buildHeader` (@ `src/Monolog/Handler/SlackHandler.php`) -> DB Complexity: **23**
- `write` (@ `src/Monolog/Handler/FirePHPHandler.php`) -> DB Complexity: **22**
  * *Intent:* /**
- `__construct` (@ `src/Monolog/Handler/PushoverHandler.php`) -> DB Complexity: **21**
- `writeToSocket` (@ `src/Monolog/Handler/SocketHandler.php`) -> DB Complexity: **17**
- `addRecord` (@ `src/Monolog/Logger.php`) -> DB Complexity: **17**
- `format` (@ `src/Monolog/Formatter/GelfMessageFormatter.php`) -> DB Complexity: **16**
- `format` (@ `src/Monolog/Formatter/HtmlFormatter.php`) -> DB Complexity: **15**
  * *Intent:* /** * Creates an HTML table row *

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Monolog/Handler` | 67 | 7317.1 | 24.43% | 62.05% |
| `src/Monolog/Formatter` | 19 | 2212.76 | 25.34% | 6.89% |
| `src/Monolog` | 10 | 2126.82 | 30.8% | 19.85% |
| `src/Monolog/Processor` | 15 | 662.66 | 33.25% | 91.02% |
| `src/Monolog/Handler/Slack` | 1 | 492.26 | 35.56% | 0.0% |
| `src/Monolog/Handler/SyslogUdp` | 1 | 73.96 | 87.6% | 0.0% |
| `__monolith__` | 6 | 66.2 | 1.67% | 0.0% |
| `src/Monolog/Handler/FingersCrossed` | 3 | 61.34 | 7.54% | 33.33% |
| `src/Monolog/Handler/Curl` | 1 | 57.84 | 36.55% | 89.91% |
| `src/Monolog/Attribute` | 2 | 40.96 | 5.0% | 99.99% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/Monolog/Handler/NoopHandler.php` -> **100.0%** Exposure
- `src/Monolog/Handler/AbstractHandler.php` -> **99.9998%** Exposure
- `src/Monolog/Handler/NullHandler.php` -> **99.9998%** Exposure
- `src/Monolog/Processor/HostnameProcessor.php` -> **99.9998%** Exposure
- `src/Monolog/Attribute/WithMonologChannel.php` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `phpstan-ignore-by-php-version.neon.php` -> **100.0%** Exposure
- `src/Monolog/Attribute/AsMonologProcessor.php` -> **100.0%** Exposure
- `src/Monolog/ErrorHandler.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/ChromePHPFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FluentdFormatter.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Monolog/Handler/SocketHandler.php` -> **12** Orphaned Functions | **0** Duplicates
- `src/Monolog/Handler/TestHandler.php` -> **9** Orphaned Functions | **0** Duplicates
- `src/Monolog/Handler/AbstractHandler.php` -> **6** Orphaned Functions | **0** Duplicates
- `src/Monolog/Handler/LogglyHandler.php` -> **5** Orphaned Functions | **0** Duplicates
- `src/Monolog/Handler/MailHandler.php` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Monolog/Formatter/LineFormatter.php`** -> AI Confidence: **99.31%**
2. **`src/Monolog/Handler/DeduplicationHandler.php`** -> AI Confidence: **99.31%**
3. **`src/Monolog/Handler/NewRelicHandler.php`** -> AI Confidence: **99.31%**
4. **`src/Monolog/Handler/PHPConsoleHandler.php`** -> AI Confidence: **99.31%**
5. **`src/Monolog/Handler/Slack/SlackRecord.php`** -> AI Confidence: **99.31%**
6. **`src/Monolog/Handler/ChromePHPHandler.php`** -> AI Confidence: **99.23%**
7. **`src/Monolog/Handler/ElasticsearchHandler.php`** -> AI Confidence: **99.18%**
8. **`src/Monolog/Handler/FilterHandler.php`** -> AI Confidence: **99.18%**
9. **`src/Monolog/Handler/PsrHandler.php`** -> AI Confidence: **99.18%**
10. **`src/Monolog/Formatter/JsonFormatter.php`** -> AI Confidence: **99.16%**
11. **`src/Monolog/Handler/FirePHPHandler.php`** -> AI Confidence: **99.16%**
12. **`src/Monolog/Handler/PushoverHandler.php`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/Monolog/ErrorHandler.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FlowdockFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FluentdFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/GelfMessageFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/HtmlFormatter.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/Monolog/Handler/DeduplicationHandler.php` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/Monolog/ErrorHandler.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/ChromePHPFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FlowdockFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/FluentdFormatter.php` -> **100.0%** Exposure
- `src/Monolog/Formatter/GelfMessageFormatter.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `527` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Monolog/Handler/DeduplicationHandler.php` (PHP) -> Cumulative Risk: **845.65**
- **Archetype:** `file_cluster_13` (Distance: 12.684 IQR)
- **Magnitude:** 291.44 | **LOC:** 184 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `flush` (Impact: 86.8), `collectLogs` (Impact: 45.2), `isDuplicate` (Impact: 36.0)

### 2. `src/Monolog/Handler/RotatingFileHandler.php` (PHP) -> Cumulative Risk: **774.44**
- **Archetype:** `file_cluster_13` (Distance: 12.521 IQR)
- **Magnitude:** 309.4 | **LOC:** 235 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `rotate` (Impact: 63.3), `write` (Impact: 41.0), `setDateFormat` (Impact: 30.6)

### 3. `src/Monolog/Processor/PsrLogMessageProcessor.php` (PHP) -> Cumulative Risk: **771.81**
- **Archetype:** `file_cluster_13` (Distance: 12.031 IQR)
- **Magnitude:** 167.82 | **LOC:** 88 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `__invoke` (Impact: 134.1), `__construct` (Impact: 5.4)

### 4. `src/Monolog/Formatter/LineFormatter.php` (PHP) -> Cumulative Risk: **757.34**
- **Archetype:** `file_cluster_13` (Distance: 13.796 IQR)
- **Magnitude:** 642.1 | **LOC:** 318 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `format` (Impact: 152.7), `formatException` (Impact: 61.7), `stacktracesParser` (Impact: 49.1)

### 5. `src/Monolog/Logger.php` (PHP) -> Cumulative Risk: **749.26**
- **Archetype:** `file_cluster_13` (Distance: 13.656 IQR)
- **Magnitude:** 702.08 | **LOC:** 752 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9992%)
- **Heaviest Functions:** `addRecord` (Impact: 223.1), `reset` (Impact: 44.0), `toMonologLevel` (Impact: 43.6)

### 6. `src/Monolog/Handler/SocketHandler.php` (PHP) -> Cumulative Risk: **748.29**
- **Archetype:** `file_cluster_8` (Distance: 12.246 IQR)
- **Magnitude:** 448.28 | **LOC:** 437 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9992%)
- **Heaviest Functions:** `writeToSocket` (Impact: 61.4), `__construct` (Impact: 61.2), `streamSetChunkSize` (Impact: 21.4)

### 7. `src/Monolog/SignalHandler.php` (PHP) -> Cumulative Risk: **738.99**
- **Archetype:** `file_cluster_13` (Distance: 13.464 IQR)
- **Magnitude:** 309.3 | **LOC:** 114 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleSignal` (Impact: 220.2), `registerSignalHandler` (Impact: 35.5), `__construct` (Impact: 3.2)

### 8. `src/Monolog/Registry.php` (PHP) -> Cumulative Risk: **737.02**
- **Archetype:** `file_cluster_13` (Distance: 13.976 IQR)
- **Magnitude:** 85.66 | **LOC:** 134 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9999%), Tech Debt (99.9871%)
- **Heaviest Functions:** `addLogger` (Impact: 20.5), `removeLogger` (Impact: 17.8), `getInstance` (Impact: 8.4)

### 9. `src/Monolog/Handler/AmqpHandler.php` (PHP) -> Cumulative Risk: **729.05**
- **Archetype:** `file_cluster_13` (Distance: 12.448 IQR)
- **Magnitude:** 210.34 | **LOC:** 171 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `handleBatch` (Impact: 61.5), `__construct` (Impact: 45.3), `write` (Impact: 26.6)

### 10. `src/Monolog/Handler/LogglyHandler.php` (PHP) -> Cumulative Risk: **724.59**
- **Archetype:** `file_cluster_13` (Distance: 11.998 IQR)
- **Magnitude:** 124.42 | **LOC:** 157 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `setTag` (Impact: 20.5), `__construct` (Impact: 16.5), `addTag` (Impact: 12.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Monolog/Logger.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.656 IQR)
- **Top Global Matches:** file_cluster_13: 13.656, file_cluster_8: 13.934, file_cluster_7: 13.986
- **Magnitude:** 702.08 | **LOC:** 752 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (46.0828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addRecord` (Impact: 223.1 | O(N^6) | DB: 17)
  * `reset` (Impact: 44.0 | O(2^N))
  * `toMonologLevel` (Impact: 43.6 | O(N^5) | DB: 5)
    * *Intent:* /** * Control the use of microsecond resolution timestamps in the 'datetime' * member of new records...
  * `isHandling` (Impact: 30.9 | O(2^N) | DB: 1)
    * *Intent:* /** * Adds a log record. * * @param int $level The logging level (a Monolog or RFC 5424 level) * @pa...
  * `log` (Impact: 25.8 | O(N^4) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 110`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`
* *Architecture:* `api: 65`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 23`, `doc: 107`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.876
  * `Choke Point (Betweenness):` 0.001403 | `Ripple Effect (Closeness):` 0.097015
  * `Imports (Out-Degree: 2):` Throwable, Monolog\Handler\HandlerInterface, 
    public function useMicrosecondTimestamps(bool $micro): self
    
        $this->microsecondTimestamps = $micro, DateTimeZone, Stringable, d by the engine, Psr\Log\InvalidArgumentException, Psr\Log\LogLevel...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/LineFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.796 IQR)
- **Top Global Matches:** file_cluster_13: 13.796, file_cluster_8: 13.95, file_cluster_17: 14.075
- **Magnitude:** 642.1 | **LOC:** 318 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (36.6963%), Tech Debt (31.1593%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 152.7 | O(2^N) | DB: 12)
  * `formatException` (Impact: 61.7 | O(N^5) | DB: 9)
  * `stacktracesParser` (Impact: 49.1 | O(2^N) | DB: 4)
  * `replaceNewlines` (Impact: 36.9 | O(N^5) | DB: 2)
  * `__construct` (Impact: 29.8 | O(2^N) | DB: 9)
    * *Intent:* /** * Formats incoming records into a one-line string * * This is especially useful for logging to f...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 50`, `args: 17`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 182`, `fragile_debt: 2`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 10`, `doc: 24`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.443
  * `Choke Point (Betweenness):` 0.000505 | `Ripple Effect (Closeness):` 0.075249
  * `Imports (Out-Degree: 2):` ?Closure $parser = null): self
    
        $this->includeStacktraces = $include, Stacktraces(bool $include = true, Monolog\LogRecord, Stacktraces) 
            $str .= $this->stacktracesParser($e, Stacktraces, Stacktraces($includeStacktraces, Monolog\Utils, Closure...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/Slack/SlackRecord.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.168 IQR)
- **Top Global Matches:** file_cluster_13: 13.168, file_cluster_8: 13.275, file_cluster_7: 13.366
- **Magnitude:** 492.26 | **LOC:** 382 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (35.5619%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSlackData` (Impact: 143.8 | O(N^6) | DB: 6)
  * `removeExcludedFields` (Impact: 43.0 | O(N^5) | DB: 8)
  * `__construct` (Impact: 31.2 | O(N^3) | DB: 9)
    * *Intent:* /** * User icon e.g. 'ghost', 'http://example.com/user.png'
  * `includeContextAndExtra` (Impact: 20.1 | O(2^N) | DB: 3)
    * *Intent:* /** * Channel used by the bot when posting
  * `setUserIcon` (Impact: 15.2 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 134`
* *Architecture:* `api: 18`, `import: 5`
* *Defense:* `safety: 2`, `doc: 46`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.462
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 5):` FormatterInterface|null $formatter = null
    ) 
        $this
            ->setChannel($channel)
            ->setUsername($username)
            ->useAttachment($useAttachment)
            ->setUserIcon($userIcon)
            ->useShortAttachment($useShortAttachment)
            ->includeContextAndExtra($includeContextAndExtra)
            ->excludeFields($excludeFields)
            ->setFormatter($formatter, ContextAndExtra = false, array $excludeFields = [], 
    public function getSlackData(LogRecord $record): array
    
        $dataArray = [], 'context'], Monolog\LogRecord, Monolog\Formatter\NormalizerFormatter, ContextAndExtra) 
            $this->normalizerFormatter = new NormalizerFormatter(...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/SocketHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.246 IQR)
- **Top Global Matches:** file_cluster_8: 12.246, file_cluster_7: 12.402, file_cluster_13: 12.479
- **Magnitude:** 448.28 | **LOC:** 437 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (42.6131%), Tech Debt (91.8434%)
**Top Internal Functions/Classes:**
  * `writeToSocket` (Impact: 61.4 | O(N^4) | DB: 17)
  * `__construct` (Impact: 61.2 | O(2^N) | DB: 13)
  * `streamSetChunkSize` (Impact: 21.4 | O(2^N))
  * `writingIsTimedOut` (Impact: 21.2 | O(N^3) | DB: 2)
    * *Intent:* /** * Wrapper to allow mocking * * @return mixed[]|bool */
  * `fwrite` (Impact: 16.4 | O(2^N) | DB: 9)
    * *Intent:* /** * Get current in-transfer timeout */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 76`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 89`, `orphaned_logic: 12`
* *Architecture:* `io: 6`, `api: 15`, `import: 2`
* *Defense:* `safety: 1`, `doc: 46`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Utils.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.822 IQR)
- **Top Global Matches:** file_cluster_8: 12.822, file_cluster_7: 13.043, file_cluster_13: 13.127
- **Magnitude:** 390.8 | **LOC:** 258 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (40.003%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expandIniShorthandBytes` (Impact: 70.7 | O(N^4) | DB: 4)
  * `detectAndCleanUtf8` (Impact: 37.6 | O(N^6) | DB: 4)
  * `handleJsonError` (Impact: 33.3 | O(N^3) | DB: 6)
  * `substr` (Impact: 32.4 | O(2^N) | DB: 1)
  * `jsonEncode` (Impact: 31.1 | O(N^4) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 38`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 91`
* *Architecture:* `api: 12`
* *Defense:* `safety: 3`, `doc: 19`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.218284
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/PHPConsoleHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.43 IQR)
- **Top Global Matches:** file_cluster_13: 12.43, file_cluster_8: 12.598, file_cluster_7: 12.868
- **Magnitude:** 369.86 | **LOC:** 304 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (35.187%), Tech Debt (50.7022%)
**Top Internal Functions/Classes:**
  * `initConnector` (Impact: 119.1 | O(N^4) | DB: 10)
    * *Intent:* * ipMasks: string[], * enableEvalListener: bool, * dumperDetectCallbacks: bool, * dumperLevelLimit: ...
  * `getRecordTags` (Impact: 57.0 | O(N^6) | DB: 6)
  * `__construct` (Impact: 27.3 | O(2^N) | DB: 6)
    * *Intent:* * 4. Example (result will looks like http://i.hizliresim.com/vg3Pz4.png) * * $logger = new \Monolog\...
  * `handle` (Impact: 24.4 | O(2^N))
  * `handleErrorRecord` (Impact: 20.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 10`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` php-console#troubleshooting-with-_session-handler-overridden-in-some-frameworks)
    ], Monolog\Formatter\LineFormatter, Monolog\LogRecord,  int Maximum length of any string or dumped array item
        'dumperDumpSizeLimit' => 500000, PhpConsole\Connector,  int Maximum approximate size of dumped vars result formatted in JSON
        'detectDumpTraceAndSource' => false, Monolog\Utils, Monolog\Level...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/JsonFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.151 IQR)
- **Top Global Matches:** file_cluster_13: 13.151, file_cluster_17: 13.335, file_cluster_0: 13.521
- **Magnitude:** 369.42 | **LOC:** 235 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (44.6826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 158.7 | O(2^N) | DB: 5)
  * `normalizeRecord` (Impact: 91.0 | O(2^N) | DB: 1)
    * *Intent:* /** * @inheritDoc */
  * `normalizeException` (Impact: 14.3 | O(2^N) | DB: 2)
  * `formatBatch` (Impact: 12.3 | O(N^3) | DB: 1)
    * *Intent:* /** * The batch mode option configures the formatting style for * multiple records. By default, mult...
  * `includeStacktraces` (Impact: 7.6 | O(2^N) | DB: 2)
    * *Intent:* /** * True if newlines are appended to every formatted record */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 45`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 12`, `doc: 19`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.809
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 1):` Throwable, Stacktraces = false)
    
        $this->batchMode = $batchMode, Stacktraces) 
            unset($data['trace'], Monolog\LogRecord, int $depth = 0): array
    
        $data = parent::normalizeException($e, Stacktraces = false, Stacktraces = $includeStacktraces, Stacktraces` property.
     *
     * @return array<array-key...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/ErrorHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.124 IQR)
- **Top Global Matches:** file_cluster_8: 13.124, file_cluster_13: 13.176, file_cluster_7: 13.322
- **Magnitude:** 324.4 | **LOC:** 280 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `handleFatalError` (Impact: 42.8 | O(N^5) | DB: 4)
  * `handleError` (Impact: 41.5 | O(N^3) | DB: 7)
  * `handleException` (Impact: 36.3 | O(N^4) | DB: 3)
  * `registerExceptionHandler` (Impact: 22.5 | O(N^4) | DB: 6)
    * *Intent:* /** * Registers a new ErrorHandler for a given Logger * * By default it will handle errors, exceptio...
  * `register` (Impact: 18.7 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 38`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 10`, `doc: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Closure, Psr\Log\LogLevel, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/RotatingFileHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.521 IQR)
- **Top Global Matches:** file_cluster_13: 12.521, file_cluster_8: 12.804, file_cluster_9: 12.904
- **Magnitude:** 309.4 | **LOC:** 235 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (35.5806%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rotate` (Impact: 63.3 | O(N^6) | DB: 9)
  * `write` (Impact: 41.0 | O(2^N) | DB: 2)
    * *Intent:* /** * @inheritDoc
  * `setDateFormat` (Impact: 30.6 | O(N^4) | DB: 1)
  * `__construct` (Impact: 19.5 | O(2^N) | DB: 12)
    * *Intent:* /** * Stores logs to files that are rotated every day and a limited number of files are kept. * * Th...
  * `close` (Impact: 14.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 37`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 80`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` InvalidArgumentException, Monolog\LogRecord, DateTimeZone, Monolog\Utils, Monolog\Level
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/SignalHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.464 IQR)
- **Top Global Matches:** file_cluster_13: 13.464, file_cluster_8: 13.761, file_cluster_7: 13.9
- **Magnitude:** 309.3 | **LOC:** 114 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (41.9927%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `handleSignal` (Impact: 220.2 | O(2^N) | DB: 8)
  * `registerSignalHandler` (Impact: 35.5 | O(N^3) | DB: 6)
  * `__construct` (Impact: 3.2 | O(N^2) | DB: 1)
    * *Intent:* /** * Monolog POSIX signal handler * * @author Robert Gust-Bardon <robert@gust-bardon.org> */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 14`, `args: 9`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 5`, `doc: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Log\LogLevel, Psr\Log\LoggerInterface, ReflectionExtension
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/TelegramBotHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.472 IQR)
- **Top Global Matches:** file_cluster_13: 12.472, file_cluster_8: 12.578, file_cluster_7: 12.696
- **Magnitude:** 305.9 | **LOC:** 302 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (33.0378%), Tech Debt (30.2941%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 80.9 | O(2^N) | DB: 10)
    * *Intent:* /** * The maximum number of characters allowed in a message according to the Telegram api documentat...
  * `handleBatch` (Impact: 31.0 | O(N^4) | DB: 2)
  * `sendCurl` (Impact: 21.6 | O(N^3) | DB: 7)
    * *Intent:* /** * True - split a message longer than MAX_MESSAGE_LENGTH into parts and send in multiple messages...
  * `send` (Impact: 20.6 | O(N^4) | DB: 2)
  * `setParseMode` (Impact: 15.2 | O(N^3) | DB: 2)
    * *Intent:* /** * Sends the message silently. Users will receive a notification with no sound.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 37`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `orphaned_logic: 2`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `doc: 35`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` RuntimeException, Monolog\Utils, Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/GelfMessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.732 IQR)
- **Top Global Matches:** file_cluster_13: 13.732, file_cluster_8: 14.057, file_cluster_7: 14.202
- **Magnitude:** 298.9 | **LOC:** 153 | **CtrlFlow:** 62.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (40.6275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 113.2 | O(N^4) | DB: 16)
  * `__construct` (Impact: 81.2 | O(2^N) | DB: 9)
    * *Intent:* /**
  * `getGraylog2Priority` (Impact: 8.7 | O(N^3) | DB: 8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 19`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.943
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 3):` Monolog\LogRecord, Gelf\Message, Monolog\Utils, Monolog\Level, d to use Monolog\'s GelfMessageFormatter'
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/DeduplicationHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.684 IQR)
- **Top Global Matches:** file_cluster_13: 12.684, file_cluster_8: 12.807, file_cluster_7: 13.005
- **Magnitude:** 291.44 | **LOC:** 184 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (44.9998%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flush` (Impact: 86.8 | O(N^6) | DB: 13)
  * `collectLogs` (Impact: 45.2 | O(N^4) | DB: 11)
    * *Intent:* /**
  * `isDuplicate` (Impact: 36.0 | O(N^4) | DB: 9)
  * `__construct` (Impact: 22.4 | O(2^N) | DB: 8)
    * *Intent:* /** * @param HandlerInterface $handler Handler.
  * `buildDeduplicationStoreEntry` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 8`, `state_mutation: 93`
* *Architecture:* `io: 3`, `api: 2`, `import: 4`
* *Defense:* `doc: 11`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` s the BufferHandler functionality and will buffer
 * all messages until the end of the request or flush() is called.
 *
 * This works by storing all log records' messages above $deduplicationLevel
 * to the file specified by $deduplicationStore. When further logs come in at the end of the
 * request (or when flush() is called), all those above $deduplicationLevel are checked
 * against the existing stored logs. If they match and the timestamps in the stored log is
 * not older than $time seconds, the new log record is discarded. If no log record is new, Monolog\LogRecord, 
class DeduplicationHandler extends BufferHandler

    protected string $deduplicationStore, Monolog\Level, Psr\Log\LogLevel, the
 * whole data set is discarded.
 *
 * This is mainly useful in combination with Mail handlers or things like Slack or HipChat handlers
 * that send messages to people...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SlackHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.231 IQR)
- **Top Global Matches:** file_cluster_13: 12.231, file_cluster_8: 12.379, file_cluster_7: 12.502
- **Magnitude:** 266.88 | **LOC:** 268 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (42.4109%), Tech Debt (62.7179%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 98.2 | O(2^N) | DB: 15)
    * *Intent:* /** * Sends notifications through Slack API *
  * `prepareContentData` (Impact: 16.6 | O(N^3) | DB: 1)
  * `finalizeWrite` (Impact: 7.3 | O(N^3) | DB: 4)
    * *Intent:* /** * @return string[] */
  * `setFormatter` (Impact: 6.3 | O(2^N))
  * `setChannel` (Impact: 6.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 45`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` float $timeout = 0.0, Monolog\LogRecord, bool $bubble = true, ?int $chunkSize = null
    ) 
        if (!\extension_loaded('openssl')) 
            throw new MissingExtensionException('The OpenSSL PHP extension is required to use the SlackHandler', float $writingTimeout = 10.0, bool $persistent = false, ContextAndExtra Whether the attachment should include context and extra data
     * @param  string[]                  $excludeFields          Dot separated list of fields to exclude from slack message. E.g. ['context.field1', ContextAndExtra(bool $includeContextAndExtra): self
    
        $this->slackRecord->includeContextAndExtra($includeContextAndExtra...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PushoverHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.993 IQR)
- **Top Global Matches:** file_cluster_13: 12.993, file_cluster_8: 13.088, file_cluster_7: 13.269
- **Magnitude:** 256.92 | **LOC:** 247 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (41.6927%), Tech Debt (49.5567%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 97.8 | O(2^N) | DB: 21)
  * `buildContent` (Impact: 26.0 | O(N^3) | DB: 8)
  * `write` (Impact: 16.6 | O(2^N) | DB: 2)
  * `useFormattedMessage` (Impact: 6.3 | O(2^N) | DB: 1)
  * `buildHeader` (Impact: 3.5 | O(N^2) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 24`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 4`, `import: 5`
* *Defense:* `safety: 2`, `doc: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` int $retry = 30, float $timeout = 0.0, ?string $title = null, Monolog\LogRecord, int|string|Level $level = Level::Critical, bool $bubble = true, float $writingTimeout = 10.0, bool $persistent = false...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/NewRelicHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.202 IQR)
- **Top Global Matches:** file_cluster_13: 12.202, file_cluster_8: 12.378, file_cluster_7: 12.609
- **Magnitude:** 234.46 | **LOC:** 181 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.4155%), Tech Debt (51.2752%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 149.3 | O(N^6) | DB: 6)
    * *Intent:* /** * @inheritDoc */
  * `setNewRelicParameter` (Impact: 14.3 | O(N^3))
    * *Intent:* /** * Returns the appname where this log should be sent. Each log can override the default appname, ...
  * `getAppName` (Impact: 12.4 | O(N^3))
  * `getTransactionName` (Impact: 12.4 | O(N^3))
  * `__construct` (Impact: 8.1 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 31`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 7`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` 
        protected string|null $transactionName = null
    ) 
        parent::__construct($level, Monolog\LogRecord, bool $bubble = true, 
    public function __construct(
        int|string|Level $level = Level::Error, Monolog\Formatter\NormalizerFormatter, $bubble, d to use the NewRelicHandler', Monolog\Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/FilterHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.832 IQR)
- **Top Global Matches:** file_cluster_13: 12.832, file_cluster_17: 13.186, file_cluster_8: 13.198
- **Magnitude:** 214.58 | **LOC:** 203 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (32.2427%), Tech Debt (42.3843%)
**Top Internal Functions/Classes:**
  * `handleBatch` (Impact: 40.6 | O(2^N) | DB: 1)
    * *Intent:* /** * @param int|string|Level|LogLevel::*|array<int|string|Level|LogLevel::*> $minLevelOrList A list...
  * `handle` (Impact: 24.7 | O(2^N) | DB: 1)
  * `getHandler` (Impact: 19.0 | O(N^4) | DB: 3)
  * `setAcceptedLevels` (Impact: 18.1 | O(N^3) | DB: 7)
    * *Intent:* /** * Minimum level for logs that are passed to handler *
  * `setFormatter` (Impact: 16.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 38`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `orphaned_logic: 2`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 6`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Monolog\ResettableInterface, ProcessableHandlerTrait, Monolog\LogRecord, Monolog\Level, Psr\Log\LogLevel, Monolog\Formatter\FormatterInterface, Closure, Monolog\Logger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/ElasticsearchHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.134 IQR)
- **Top Global Matches:** file_cluster_13: 12.134, file_cluster_8: 12.54, file_cluster_7: 12.748
- **Magnitude:** 211.76 | **LOC:** 239 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (14.821%), Tech Debt (78.8108%)
**Top Internal Functions/Classes:**
  * `bulkSend` (Impact: 50.6 | O(N^6) | DB: 2)
  * `__construct` (Impact: 45.8 | O(2^N) | DB: 7)
    * *Intent:* /** * Elasticsearch handler * * @link https://www.elastic.co/guide/en/elasticsearch/client/php-api/c...
  * `createExceptionFromError` (Impact: 32.7 | O(2^N) | DB: 1)
    * *Intent:* /** * @inheritDoc
  * `createExceptionFromResponses` (Impact: 26.9 | O(N^4))
    * *Intent:* /** * Getter options
  * `setFormatter` (Impact: 16.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 51`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 12`
* *Defense:* `safety: 12`, `doc: 23`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Throwable, InvalidArgumentException, Monolog\LogRecord, RuntimeException, Elastic\Elasticsearch\Exception\InvalidArgumentException, Monolog\Level, Elasticsearch\Client, Elastic\Elasticsearch\Client...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/AmqpHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.448 IQR)
- **Top Global Matches:** file_cluster_13: 12.448, file_cluster_8: 12.766, file_cluster_7: 12.995
- **Magnitude:** 210.34 | **LOC:** 171 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (32.6869%), Tech Debt (84.6266%)
**Top Internal Functions/Classes:**
  * `handleBatch` (Impact: 61.5 | O(2^N) | DB: 5)
  * `__construct` (Impact: 45.3 | O(2^N) | DB: 5)
  * `write` (Impact: 26.6 | O(N^4) | DB: 7)
  * `createAmqpMessage` (Impact: 8.6 | O(N^3) | DB: 2)
  * `setExtraAttributes` (Impact: 3.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 5`, `doc: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Monolog\LogRecord, Gelf\Message, Monolog\Level, PhpAmqpLib\Channel\AMQPChannel, Monolog\Formatter\JsonFormatter, Monolog\Formatter\FormatterInterface, PhpAmqpLib\Message\AMQPMessage, AMQPExchange
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/GroupHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.077 IQR)
- **Top Global Matches:** file_cluster_13: 11.077, file_cluster_8: 11.225, file_cluster_7: 11.521
- **Magnitude:** 203.16 | **LOC:** 131 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.676%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `handleBatch` (Impact: 40.7 | O(2^N) | DB: 2)
  * `isHandling` (Impact: 30.5 | O(2^N))
    * *Intent:* /** * @param HandlerInterface[] $handlers Array of Handlers. * @param bool $bubble Whether the messa...
  * `setFormatter` (Impact: 30.5 | O(2^N))
  * `reset` (Impact: 26.5 | O(2^N))
  * `handle` (Impact: 24.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 31`, `args: 8`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `orphaned_logic: 1`
* *Architecture:* `api: 7`, `import: 4`
* *Defense:* `safety: 3`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Monolog\ResettableInterface, Monolog\Formatter\FormatterInterface, ProcessableHandlerTrait, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Processor/PsrLogMessageProcessor.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.031 IQR)
- **Top Global Matches:** file_cluster_13: 12.031, file_cluster_8: 12.195, file_cluster_0: 12.444
- **Magnitude:** 167.82 | **LOC:** 88 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (42.8334%), Tech Debt (78.3788%)
**Top Internal Functions/Classes:**
  * `__invoke` (Impact: 134.1 | O(N^5) | DB: 4)
  * `__construct` (Impact: 5.4 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 5`, `doc: 5`, `test: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Utils, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/CubeHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.028 IQR)
- **Top Global Matches:** file_cluster_13: 12.028, file_cluster_8: 12.192, file_cluster_7: 12.437
- **Magnitude:** 162.44 | **LOC:** 168 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (34.7493%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 41.0 | O(2^N) | DB: 7)
    * *Intent:* /** * Logs to Cube. * * @link https://github.com/square/cube/wiki * @author Wan Chen <kami@kamisama....
  * `write` (Impact: 21.1 | O(N^3) | DB: 4)
  * `connectUdp` (Impact: 14.7 | O(N^3) | DB: 8)
  * `writeHttp` (Impact: 12.9 | O(N^3))
  * `writeUdp` (Impact: 12.6 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` d to use udp URLs with the CubeHandler', Monolog\LogRecord, Monolog\Utils, Monolog\Level, d to use http URLs with the CubeHandler'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/HtmlFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.167 IQR)
- **Top Global Matches:** file_cluster_13: 13.167, file_cluster_8: 13.286, file_cluster_7: 13.437
- **Magnitude:** 160.18 | **LOC:** 143 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (32.9431%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 26.4 | O(N^4) | DB: 15)
    * *Intent:* /** * Creates an HTML table row *
  * `__construct` (Impact: 14.9 | O(2^N) | DB: 1)
    * *Intent:* /** * Translates Monolog log levels to html color priorities. */
  * `convertToString` (Impact: 10.9 | O(N^3) | DB: 1)
  * `getLevelColor` (Impact: 8.7 | O(N^3) | DB: 8)
  * `addRow` (Impact: 8.4 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.231
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 3):` Monolog\Utils, Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/WhatFailureGroupHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.635 IQR)
- **Top Global Matches:** file_cluster_13: 12.635, file_cluster_17: 12.756, file_cluster_8: 12.844
- **Magnitude:** 159.7 | **LOC:** 81 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (24.167%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `handleBatch` (Impact: 60.9 | O(2^N) | DB: 2)
  * `handle` (Impact: 50.8 | O(2^N) | DB: 1)
  * `close` (Impact: 35.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 16`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 10`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Throwable, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/ProcessHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.076 IQR)
- **Top Global Matches:** file_cluster_13: 13.076, file_cluster_8: 13.132, file_cluster_7: 13.301
- **Magnitude:** 157.82 | **LOC:** 192 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (36.2264%), Tech Debt (56.15%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 39.9 | O(2^N) | DB: 9)
    * *Intent:* /** * Holds the process to receive data on its STDIN. *
  * `handleStartupErrors` (Impact: 22.4 | O(N^4) | DB: 2)
    * *Intent:* /** * Writes the record down to the log of the implementing handler *
  * `close` (Impact: 13.5 | O(N^4) | DB: 1)
  * `write` (Impact: 12.6 | O(N^3) | DB: 1)
    * *Intent:* /** * @var array<int, list<string>>
  * `ensureProcessIsStarted` (Impact: 7.3 | O(N^3))
    * *Intent:* /** * @param string $command Command for the process to start. Absolute paths are recommended, * esp...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 24`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 42`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 2`, `import: 2`
* *Defense:* `safety: 5`, `doc: 24`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, Monolog\LogRecord
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Monolog/Attribute/AsMonologProcessor.php` (PHP) | Magnitude: 34.36 | Delta: **0.465 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 7, doc: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Monolog/Handler/OverflowHandler.php` (PHP) | Magnitude: 33.22 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, branch: 3, doc: 3
- `tests/Monolog/Handler/ExceptionTestHandler.php` (PHP) | Magnitude: 3.42 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 4, safety: 2, import: 2
- `src/Monolog/Formatter/LogmaticFormatter.php` (PHP) | Magnitude: 44.02 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, state_mutation: 7, doc: 6
- `src/Monolog/Handler/Curl/Util.php` (PHP) | Magnitude: 57.84 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 24, structural_boundaries: 8, branch: 6
- `src/Monolog/Formatter/ElasticsearchFormatter.php` (PHP) | Magnitude: 30.58 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, doc: 14, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Monolog/LogRecord.php` (PHP) | Magnitude: 124.32 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 33, structural_boundaries: 27, api: 21
- `src/Monolog/ErrorHandler.php` (PHP) | Magnitude: 324.4 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 103, structural_boundaries: 38, branch: 35
- `src/Monolog/Formatter/SyslogFormatter.php` (PHP) | Magnitude: 28.94 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, encapsulation: 8, state_mutation: 5
- `src/Monolog/Handler/MissingExtensionException.php` (PHP) | Magnitude: 12.6 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, class_start: 1, safety: 1
- `src/Monolog/Handler/HandlerWrapper.php` (PHP) | Magnitude: 115.3 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 31, args: 10, func_start: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Monolog/JsonSerializableDateTimeImmutable.php` (PHP) | Magnitude: 31.36 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, state_mutation: 6, api: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Monolog/Formatter/LineFormatter.php` -> **angeljqv** (100.0% isolated ownership) | Magnitude: 642.1
- `src/Monolog/Formatter/JsonFormatter.php` -> **Adrien SIMON** (100.0% isolated ownership) | Magnitude: 369.42
- `src/Monolog/Handler/TelegramBotHandler.php` -> **Dawid Nowak** (100.0% isolated ownership) | Magnitude: 305.9
- `src/Monolog/Formatter/GelfMessageFormatter.php` -> **Tobias Lorenz** (100.0% isolated ownership) | Magnitude: 298.9
- `src/Monolog/Handler/DeduplicationHandler.php` -> **Denis** (100.0% isolated ownership) | Magnitude: 291.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Monolog/Logger.php` -> **Severity: 0.14** (Bridge: 0.0014 * Flux: 99.9992%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 0.051** (Bridge: 0.0005 * Flux: 100.0%)
- `src/Monolog/Handler/ProcessableHandlerTrait.php` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 98.7711%)
- `src/Monolog/Handler/Slack/SlackRecord.php` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)
- `src/Monolog/Handler/FormattableHandlerTrait.php` -> **Severity: 0.017** (Bridge: 0.0002 * Flux: 99.7655%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Monolog/Level.php` -> **Severity: 16.307** (Embedded: 0.4631 * Error Risk: 35.2097%)
- `src/Monolog/Utils.php` -> **Severity: 12.945** (Embedded: 0.2183 * Error Risk: 59.305%)
- `src/Monolog/LogRecord.php` -> **Severity: 11.491** (Embedded: 0.7256 * Error Risk: 15.8358%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 6.034** (Embedded: 0.0752 * Error Risk: 80.1845%)
- `src/Monolog/Logger.php` -> **Severity: 1.335** (Embedded: 0.097 * Error Risk: 13.7593%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Monolog/LogRecord.php` -> **Severity: 23080.4** (Blast Radius: 230.804 * Doc Risk: 100.0%)
- `src/Monolog/Level.php` -> **Severity: 7040.411** (Blast Radius: 73.797 * Doc Risk: 95.4024%)
- `src/Monolog/Utils.php` -> **Severity: 4221.552** (Blast Radius: 42.217 * Doc Risk: 99.9965%)
- `src/Monolog/Logger.php` -> **Severity: 1684.365** (Blast Radius: 16.876 * Doc Risk: 99.8083%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 1444.3** (Blast Radius: 14.443 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
