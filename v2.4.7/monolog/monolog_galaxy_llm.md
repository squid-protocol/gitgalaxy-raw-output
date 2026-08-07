# ARCHITECTURAL_BRIEF: monolog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/monolog` |
| **Timestamp** | `2026-08-07T03:54:33.443993+00:00` |
| **Scan Duration** | `0.48s` |
| **Git Branch** | `main` |
| **Git Commit** | `68b974809baff3f071893de61447212e9e688ee7` |
| **Git Remote** | `https://github.com/Seldaek/monolog.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 124 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 87.6 | 24.7 | 28.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 61.2 | 71.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 50.0 | 59.2 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.4 | 2.5 | 80.0 |
| API Exposure | 0.0 | 12.1 | 3.4 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 43.0 | 0.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 79.1 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 30.8 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 93.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.0 | 0.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 99.6 | 21.7 | 12.7 | 11.9 |
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

- `addRecord` (@ `src/Monolog/Logger.php`) -> Impact: **66.6** | LOC: 80
- `initConnector` (@ `src/Monolog/Handler/PHPConsoleHandler.php`) -> Impact: **49.2** | LOC: 54
  * *Intent:* * ipMasks: string[], * enableEvalListener: bool, * dumperDetectCallbacks: bool, * dumperLevelLimit: int, * dumperItemsCountLimit: int, * dumperItemSiz...
- `format` (@ `src/Monolog/Formatter/GelfMessageFormatter.php`) -> Impact: **47.2** | LOC: 65
- `__invoke` (@ `src/Monolog/Processor/PsrLogMessageProcessor.php`) -> Impact: **46.1** | LOC: 42
- `write` (@ `src/Monolog/Handler/NewRelicHandler.php`) -> Impact: **44.3** | LOC: 46
  * *Intent:* /** * @inheritDoc */
- `getSlackData` (@ `src/Monolog/Handler/Slack/SlackRecord.php`) -> Impact: **43.8** | LOC: 75
- `handleSignal` (@ `src/Monolog/SignalHandler.php`) -> Impact: **38.3** | LOC: 39
- `format` (@ `src/Monolog/Formatter/LineFormatter.php`) -> Impact: **32.6** | LOC: 53
- `normalize` (@ `src/Monolog/Formatter/JsonFormatter.php`) -> Impact: **28.8** | LOC: 57
- `flush` (@ `src/Monolog/Handler/DeduplicationHandler.php`) -> Impact: **26.2** | LOC: 39

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Monolog/Handler` | 67 | 4020.4 | 24.25% | 62.91% |
| `src/Monolog` | 10 | 1235.22 | 30.73% | 19.85% |
| `src/Monolog/Formatter` | 19 | 1217.86 | 25.34% | 6.89% |
| `src/Monolog/Processor` | 15 | 414.26 | 31.76% | 91.02% |
| `src/Monolog/Handler/Slack` | 1 | 288.06 | 34.58% | 0.0% |
| `__monolith__` | 6 | 66.2 | 1.67% | 0.0% |
| `src/Monolog/Handler/SyslogUdp` | 1 | 59.96 | 87.6% | 0.0% |
| `src/Monolog/Handler/FingersCrossed` | 3 | 54.54 | 7.54% | 33.33% |
| `src/Monolog/Handler/Curl` | 1 | 37.04 | 36.55% | 89.91% |
| `src/Monolog/Attribute` | 2 | 33.96 | 5.0% | 99.99% |

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
6. **`src/Monolog/Formatter/JsonFormatter.php`** -> AI Confidence: **99.24%**
7. **`src/Monolog/Handler/ChromePHPHandler.php`** -> AI Confidence: **99.23%**
8. **`src/Monolog/Handler/FilterHandler.php`** -> AI Confidence: **99.18%**
9. **`src/Monolog/Handler/PsrHandler.php`** -> AI Confidence: **99.18%**
10. **`src/Monolog/Handler/ElasticsearchHandler.php`** -> AI Confidence: **99.16%**
11. **`src/Monolog/Handler/FirePHPHandler.php`** -> AI Confidence: **99.16%**
12. **`src/Monolog/Handler/PushoverHandler.php`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `527` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Monolog/Handler/RotatingFileHandler.php` (PHP) -> Cumulative Risk: **536.09**
- **Archetype:** `file_cluster_13` (Distance: 12.521 IQR)
- **Magnitude:** 168.0 | **LOC:** 235 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (88.7799%)
- **Heaviest Functions:** `rotate` (Impact: 20.0), `setDateFormat` (Impact: 12.6), `write` (Impact: 10.9)

### 2. `src/Monolog/Formatter/LineFormatter.php` (PHP) -> Cumulative Risk: **519.64**
- **Archetype:** `file_cluster_13` (Distance: 13.804 IQR)
- **Magnitude:** 341.4 | **LOC:** 318 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.9218%), Verification (80.0%)
- **Heaviest Functions:** `format` (Impact: 32.6), `formatException` (Impact: 21.7), `stacktracesParser` (Impact: 13.1)

### 3. `src/Monolog/Logger.php` (PHP) -> Cumulative Risk: **514.5**
- **Archetype:** `file_cluster_13` (Distance: 13.665 IQR)
- **Magnitude:** 386.88 | **LOC:** 752 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Verification (80.0%), Documentation (69.2923%)
- **Heaviest Functions:** `addRecord` (Impact: 66.6), `toMonologLevel` (Impact: 15.7), `log` (Impact: 10.8)

### 4. `src/Monolog/Handler/SocketHandler.php` (PHP) -> Cumulative Risk: **512.03**
- **Archetype:** `file_cluster_8` (Distance: 12.246 IQR)
- **Magnitude:** 253.38 | **LOC:** 437 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Tech Debt (91.8434%), Safety Score (83.1753%)
- **Heaviest Functions:** `writeToSocket` (Impact: 25.4), `__construct` (Impact: 16.2), `writingIsTimedOut` (Impact: 11.2)

### 5. `src/Monolog/SignalHandler.php` (PHP) -> Cumulative Risk: **496.41**
- **Archetype:** `file_cluster_13` (Distance: 13.464 IQR)
- **Magnitude:** 109.3 | **LOC:** 114 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.5037%), Verification (80.0%)
- **Heaviest Functions:** `handleSignal` (Impact: 38.3), `registerSignalHandler` (Impact: 18.4), `__construct` (Impact: 2.2)

### 6. `src/Monolog/Handler/SlackHandler.php` (PHP) -> Cumulative Risk: **482.44**
- **Archetype:** `file_cluster_13` (Distance: 12.231 IQR)
- **Magnitude:** 142.38 | **LOC:** 268 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Verification (80.0%), Safety Score (79.8877%)
- **Heaviest Functions:** `__construct` (Impact: 26.2), `prepareContentData` (Impact: 8.6), `finalizeWrite` (Impact: 3.9)

### 7. `src/Monolog/Processor/LoadAverageProcessor.php` (PHP) -> Cumulative Risk: **475.83**
- **Archetype:** `file_cluster_13` (Distance: 10.962 IQR)
- **Magnitude:** 24.58 | **LOC:** 67 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.2255%), State Flux (97.3464%), Safety Score (89.4416%)
- **Heaviest Functions:** `__invoke` (Impact: 6.7), `__construct` (Impact: 5.2)

### 8. `src/Monolog/Handler/PushoverHandler.php` (PHP) -> Cumulative Risk: **475.68**
- **Archetype:** `file_cluster_13` (Distance: 12.993 IQR)
- **Magnitude:** 152.92 | **LOC:** 247 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (91.2821%), Verification (80.0%)
- **Heaviest Functions:** `__construct` (Impact: 25.9), `buildContent` (Impact: 14.0), `write` (Impact: 4.5)

### 9. `src/Monolog/Handler/TelegramBotHandler.php` (PHP) -> Cumulative Risk: **474.05**
- **Archetype:** `file_cluster_13` (Distance: 12.472 IQR)
- **Magnitude:** 170.0 | **LOC:** 302 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (85.8364%), Verification (80.0%)
- **Heaviest Functions:** `__construct` (Impact: 21.2), `handleBatch` (Impact: 13.0), `sendCurl` (Impact: 11.7)

### 10. `src/Monolog/Handler/StreamHandler.php` (PHP) -> Cumulative Risk: **467.71**
- **Archetype:** `file_cluster_13` (Distance: 12.463 IQR)
- **Magnitude:** 89.6 | **LOC:** 281 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (89.7216%), Safety Score (89.4592%)
- **Heaviest Functions:** `createDir` (Impact: 15.1), `getInodeFromUrl` (Impact: 9.2), `getDirFromStream` (Impact: 8.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Monolog/Logger.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.665 IQR)
- **Top Global Matches:** file_cluster_13: 13.665, file_cluster_8: 13.942, file_cluster_7: 13.993
- **Magnitude:** 386.88 | **LOC:** 752 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.0828%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addRecord` (Impact: 66.6)
  * `toMonologLevel` (Impact: 15.7)
    * *Intent:* /** * Control the use of microsecond resolution timestamps in the 'datetime' * member of new records...
  * `log` (Impact: 10.8)
  * `reset` (Impact: 9.4)
  * `isHandling` (Impact: 6.8)
    * *Intent:* /** * Adds a log record. * * @param int $level The logging level (a Monolog or RFC 5424 level) * @pa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 104`, `args: 34`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `state_mutation: 122`
* *Architecture:* `api: 65`, `concurrency: 7`, `import: 14`
* *Defense:* `safety: 23`, `doc: 107`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.876
  * `Choke Point (Betweenness):` 0.001403 | `Ripple Effect (Closeness):` 0.097015
  * `Imports (Out-Degree: 2):` Psr\Log\InvalidArgumentException, WeakMap, d by the engine, Fiber, Monolog\Processor\ProcessorInterface, 
    public function useMicrosecondTimestamps(bool $micro): self
    
        $this->microsecondTimestamps = $micro, Throwable, DateTimeZone...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/LineFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.804 IQR)
- **Top Global Matches:** file_cluster_13: 13.804, file_cluster_8: 13.957, file_cluster_17: 14.084
- **Magnitude:** 341.4 | **LOC:** 318 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.6963%), Tech Debt (31.1593%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 32.6)
  * `formatException` (Impact: 21.7)
  * `stacktracesParser` (Impact: 13.1)
  * `replaceNewlines` (Impact: 12.8)
  * `__construct` (Impact: 10.2)
    * *Intent:* /** * Formats incoming records into a one-line string * * This is especially useful for logging to f...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 48`, `args: 17`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 182`, `fragile_debt: 2`
* *Architecture:* `api: 15`, `import: 5`
* *Defense:* `safety: 10`, `doc: 24`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.443
  * `Choke Point (Betweenness):` 0.000505 | `Ripple Effect (Closeness):` 0.075249
  * `Imports (Out-Degree: 2):` Stacktraces) 
            $str .= $this->stacktracesParser($e, Stacktraces) 
            $this->allowInlineLineBreaks = true, Monolog\LogRecord, Monolog\Utils, Stacktraces($includeStacktraces, ?Closure $parser = null): self
    
        $this->includeStacktraces = $include, Stacktraces(bool $include = true, Closure...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/Slack/SlackRecord.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.168 IQR)
- **Top Global Matches:** file_cluster_13: 13.168, file_cluster_8: 13.275, file_cluster_7: 13.366
- **Magnitude:** 288.06 | **LOC:** 382 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getSlackData` (Impact: 43.8)
  * `__construct` (Impact: 16.2)
    * *Intent:* /** * User icon e.g. 'ghost', 'http://example.com/user.png'
  * `removeExcludedFields` (Impact: 15.1)
  * `setUserIcon` (Impact: 7.8)
  * `stringify` (Impact: 6.6)
    * *Intent:* // Add all extra fields as individual fields in attachment
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 43`, `args: 15`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 134`
* *Architecture:* `api: 18`, `import: 5`
* *Defense:* `safety: 2`, `doc: 46`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.462
  * `Choke Point (Betweenness):` 0.000224 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 5):` ContextAndExtra) 
                foreach (['extra', 'context'], array $excludeFields = [], Monolog\Level, Monolog\Formatter\FormatterInterface, Monolog\LogRecord, FormatterInterface|null $formatter = null
    ) 
        $this
            ->setChannel($channel)
            ->setUsername($username)
            ->useAttachment($useAttachment)
            ->setUserIcon($userIcon)
            ->useShortAttachment($useShortAttachment)
            ->includeContextAndExtra($includeContextAndExtra)
            ->excludeFields($excludeFields)
            ->setFormatter($formatter, Monolog\Utils...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/SocketHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.246 IQR)
- **Top Global Matches:** file_cluster_8: 12.246, file_cluster_7: 12.402, file_cluster_13: 12.479
- **Magnitude:** 253.38 | **LOC:** 437 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9136%), Tech Debt (91.8434%)
**Top Internal Functions/Classes:**
  * `writeToSocket` (Impact: 25.4)
  * `__construct` (Impact: 16.2)
  * `writingIsTimedOut` (Impact: 11.2)
    * *Intent:* /** * Wrapper to allow mocking * * @return mixed[]|bool */
  * `createSocketResource` (Impact: 7.5)
  * `streamSetChunkSize` (Impact: 5.8)
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
- **Global Archetype:** `file_cluster_8` (Drift: 12.818 IQR)
- **Top Global Matches:** file_cluster_8: 12.818, file_cluster_7: 13.042, file_cluster_13: 13.131
- **Magnitude:** 218.9 | **LOC:** 258 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expandIniShorthandBytes` (Impact: 24.0)
  * `handleJsonError` (Impact: 17.3)
  * `canonicalizePath` (Impact: 13.1)
  * `jsonEncode` (Impact: 13.1)
  * `getRecordMessageForException` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 33`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 91`
* *Architecture:* `api: 12`
* *Defense:* `safety: 3`, `doc: 19`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 42.217
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.218284
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/Monolog/ErrorHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.139 IQR)
- **Top Global Matches:** file_cluster_8: 13.139, file_cluster_13: 13.194, file_cluster_7: 13.335
- **Magnitude:** 211.9 | **LOC:** 280 | **CtrlFlow:** 51.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.4987%), Tech Debt (24.0736%)
**Top Internal Functions/Classes:**
  * `handleError` (Impact: 21.4)
  * `handleException` (Impact: 15.3)
  * `handleFatalError` (Impact: 15.1)
  * `register` (Impact: 9.7)
  * `registerErrorHandler` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 33`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 103`, `orphaned_logic: 2`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 10`, `doc: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Log\LogLevel, Closure, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PHPConsoleHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.43 IQR)
- **Top Global Matches:** file_cluster_13: 12.43, file_cluster_8: 12.598, file_cluster_7: 12.868
- **Magnitude:** 190.46 | **LOC:** 304 | **CtrlFlow:** 51.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.187%), Tech Debt (50.7022%)
**Top Internal Functions/Classes:**
  * `initConnector` (Impact: 49.2)
    * *Intent:* * ipMasks: string[], * enableEvalListener: bool, * dumperDetectCallbacks: bool, * dumperLevelLimit: ...
  * `getRecordTags` (Impact: 17.1)
  * `handleErrorRecord` (Impact: 10.6)
  * `write` (Impact: 10.5)
  * `__construct` (Impact: 7.2)
    * *Intent:* * 4. Example (result will looks like http://i.hizliresim.com/vg3Pz4.png) * * $logger = new \Monolog\...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 10`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):`  bool Autodetect and append trace data to debug
        'dataStorage' => null, PhpConsole\Helper,  int Maximum dumped vars array or object nested dump level
        'dumperItemsCountLimit' => 100,  int Maximum length of any string or dumped array item
        'dumperDumpSizeLimit' => 500000, PhpConsole\Handler, PhpConsole\Storage, Monolog\Formatter\FormatterInterface, Monolog\Level...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/TelegramBotHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.472 IQR)
- **Top Global Matches:** file_cluster_13: 12.472, file_cluster_8: 12.578, file_cluster_7: 12.696
- **Magnitude:** 170.0 | **LOC:** 302 | **CtrlFlow:** 38.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.0378%), Tech Debt (30.2941%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 21.2)
    * *Intent:* /** * The maximum number of characters allowed in a message according to the Telegram api documentat...
  * `handleBatch` (Impact: 13.0)
  * `sendCurl` (Impact: 11.7)
    * *Intent:* /** * True - split a message longer than MAX_MESSAGE_LENGTH into parts and send in multiple messages...
  * `send` (Impact: 8.6)
  * `setParseMode` (Impact: 7.8)
    * *Intent:* /** * Sends the message silently. Users will receive a notification with no sound.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 37`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `orphaned_logic: 2`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `doc: 35`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` RuntimeException, Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/GelfMessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.735 IQR)
- **Top Global Matches:** file_cluster_13: 13.735, file_cluster_8: 14.059, file_cluster_7: 14.204
- **Magnitude:** 168.5 | **LOC:** 153 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.6275%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 47.2)
  * `__construct` (Impact: 20.8)
    * *Intent:* /**
  * `getGraylog2Priority` (Impact: 4.7)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 18`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 91`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 4`, `doc: 17`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.943
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, d to use Monolog\'s GelfMessageFormatter', Monolog\Utils, Gelf\Message
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/DeduplicationHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.684 IQR)
- **Top Global Matches:** file_cluster_13: 12.684, file_cluster_8: 12.807, file_cluster_7: 13.005
- **Magnitude:** 168.34 | **LOC:** 184 | **CtrlFlow:** 56.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2339%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `flush` (Impact: 26.2)
  * `collectLogs` (Impact: 19.2)
    * *Intent:* /**
  * `isDuplicate` (Impact: 15.2)
  * `__construct` (Impact: 7.7)
    * *Intent:* /** * @param HandlerInterface $handler Handler.
  * `buildDeduplicationStoreEntry` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 8`, `state_mutation: 93`
* *Architecture:* `io: 3`, `api: 2`, `import: 4`
* *Defense:* `doc: 11`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` 
class DeduplicationHandler extends BufferHandler

    protected string $deduplicationStore, Monolog\Logger, Monolog\Level, Monolog\LogRecord, Psr\Log\LogLevel, s the BufferHandler functionality and will buffer
 * all messages until the end of the request or flush() is called.
 *
 * This works by storing all log records' messages above $deduplicationLevel
 * to the file specified by $deduplicationStore. When further logs come in at the end of the
 * request (or when flush() is called), the new log record is discarded. If no log record is new, all those above $deduplicationLevel are checked
 * against the existing stored logs. If they match and the timestamps in the stored log is
 * not older than $time seconds...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/RotatingFileHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.521 IQR)
- **Top Global Matches:** file_cluster_13: 12.521, file_cluster_8: 12.804, file_cluster_9: 12.904
- **Magnitude:** 168.0 | **LOC:** 235 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (34.2214%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `rotate` (Impact: 20.0)
  * `setDateFormat` (Impact: 12.6)
  * `write` (Impact: 10.9)
    * *Intent:* /** * @inheritDoc
  * `__construct` (Impact: 6.8)
    * *Intent:* /** * Stores logs to files that are rotated every day and a limited number of files are kept. * * Th...
  * `getGlobPattern` (Impact: 6.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 37`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 80`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 4`, `doc: 11`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Monolog\Level, DateTimeZone, Monolog\LogRecord, Monolog\Utils, InvalidArgumentException
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/PushoverHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.993 IQR)
- **Top Global Matches:** file_cluster_13: 12.993, file_cluster_8: 13.088, file_cluster_7: 13.269
- **Magnitude:** 152.92 | **LOC:** 247 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6927%), Tech Debt (49.5567%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 25.9)
  * `buildContent` (Impact: 14.0)
  * `write` (Impact: 4.5)
  * `buildHeader` (Impact: 2.5)
  * `generateDataStream` (Impact: 2.3)
    * *Intent:* * the pushover.net app owner. OpenSSL is required for this option. * @param int $retry The retry par...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 24`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`, `orphaned_logic: 3`
* *Architecture:* `io: 6`, `api: 4`, `import: 5`
* *Defense:* `safety: 2`, `doc: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` bool $persistent = false, Monolog\LogRecord, int|string|Level $highPriorityLevel = Level::Critical, float $timeout = 0.0, int|string|Level $emergencyLevel = Level::Emergency, 
    public function __construct(
        string $token, Monolog\Logger, int $expire = 25200...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SlackHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.231 IQR)
- **Top Global Matches:** file_cluster_13: 12.231, file_cluster_8: 12.379, file_cluster_7: 12.502
- **Magnitude:** 142.38 | **LOC:** 268 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.4109%), Tech Debt (62.7179%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 26.2)
    * *Intent:* /** * Sends notifications through Slack API *
  * `prepareContentData` (Impact: 8.6)
  * `finalizeWrite` (Impact: 3.9)
    * *Intent:* /** * @return string[] */
  * `buildHeader` (Impact: 2.5)
  * `setFormatter` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 45`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 12`, `import: 6`
* *Defense:* `safety: 1`, `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bool $persistent = false, array $excludeFields = [], Monolog\LogRecord, float $timeout = 0.0, bool $useAttachment = true, 
    public function __construct(
        string $token, $excludeFields, Monolog\Handler\Slack\SlackRecord...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Formatter/JsonFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.159 IQR)
- **Top Global Matches:** file_cluster_13: 13.159, file_cluster_17: 13.345, file_cluster_0: 13.529
- **Magnitude:** 136.02 | **LOC:** 235 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.6826%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `normalize` (Impact: 28.8)
  * `normalizeRecord` (Impact: 19.1)
    * *Intent:* /** * @inheritDoc */
  * `formatBatch` (Impact: 6.3)
    * *Intent:* /** * The batch mode option configures the formatting style for * multiple records. By default, mult...
  * `format` (Impact: 4.3)
  * `normalizeException` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 42`, `args: 13`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 12`, `doc: 19`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.809
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014925
  * `Imports (Out-Degree: 1):` Stacktraces = false, Stacktraces` property.
     *
     * @return array<array-key, Throwable, Stacktraces = $includeStacktraces, Stacktraces = false)
    
        $this->batchMode = $batchMode, Monolog\LogRecord, 
    protected function normalizeException(Throwable $e, Stringable...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Monolog/Formatter/HtmlFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.167 IQR)
- **Top Global Matches:** file_cluster_13: 13.167, file_cluster_8: 13.286, file_cluster_7: 13.437
- **Magnitude:** 117.38 | **LOC:** 143 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9431%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 11.3)
    * *Intent:* /** * Creates an HTML table row *
  * `convertToString` (Impact: 5.7)
  * `__construct` (Impact: 5.1)
    * *Intent:* /** * Translates Monolog log levels to html color priorities. */
  * `getLevelColor` (Impact: 4.7)
  * `addRow` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 26`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 74`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.231
  * `Choke Point (Betweenness):` 0.000112 | `Ripple Effect (Closeness):` 0.007463
  * `Imports (Out-Degree: 3):` Monolog\Level, Monolog\LogRecord, Monolog\Utils
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Monolog/SignalHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.464 IQR)
- **Top Global Matches:** file_cluster_13: 13.464, file_cluster_8: 13.761, file_cluster_7: 13.9
- **Magnitude:** 109.3 | **LOC:** 114 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.9927%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `handleSignal` (Impact: 38.3)
  * `registerSignalHandler` (Impact: 18.4)
  * `__construct` (Impact: 2.2)
    * *Intent:* /** * Monolog POSIX signal handler * * @author Robert Gust-Bardon <robert@gust-bardon.org> */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 14`, `args: 9`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 5`, `doc: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ReflectionExtension, Psr\Log\LogLevel, Psr\Log\LoggerInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/FilterHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.832 IQR)
- **Top Global Matches:** file_cluster_13: 12.832, file_cluster_17: 13.186, file_cluster_8: 13.198
- **Magnitude:** 108.98 | **LOC:** 203 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.2427%), Tech Debt (42.3843%)
**Top Internal Functions/Classes:**
  * `setAcceptedLevels` (Impact: 9.5)
    * *Intent:* /** * Minimum level for logs that are passed to handler *
  * `handleBatch` (Impact: 8.7)
    * *Intent:* /** * @param int|string|Level|LogLevel::*|array<int|string|Level|LogLevel::*> $minLevelOrList A list...
  * `getHandler` (Impact: 7.9)
  * `handle` (Impact: 6.7)
  * `setFormatter` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 38`, `args: 12`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `orphaned_logic: 2`
* *Architecture:* `api: 10`, `import: 8`
* *Defense:* `safety: 6`, `doc: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Monolog\Logger, Monolog\Level, Monolog\Formatter\FormatterInterface, Monolog\LogRecord, Psr\Log\LogLevel, Monolog\ResettableInterface, ProcessableHandlerTrait, Closure
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/AmqpHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.448 IQR)
- **Top Global Matches:** file_cluster_13: 12.448, file_cluster_8: 12.766, file_cluster_7: 12.995
- **Magnitude:** 105.84 | **LOC:** 171 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.6869%), Tech Debt (84.6266%)
**Top Internal Functions/Classes:**
  * `handleBatch` (Impact: 13.4)
  * `__construct` (Impact: 11.7)
  * `write` (Impact: 11.6)
  * `createAmqpMessage` (Impact: 4.6)
  * `setExtraAttributes` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 30`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 50`, `orphaned_logic: 4`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 5`, `doc: 14`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Monolog\Level, Monolog\Formatter\FormatterInterface, PhpAmqpLib\Channel\AMQPChannel, Monolog\LogRecord, AMQPExchange, Monolog\Formatter\JsonFormatter, Gelf\Message, PhpAmqpLib\Message\AMQPMessage
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/NewRelicHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.202 IQR)
- **Top Global Matches:** file_cluster_13: 12.202, file_cluster_8: 12.378, file_cluster_7: 12.609
- **Magnitude:** 101.76 | **LOC:** 181 | **CtrlFlow:** 47.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.4155%), Tech Debt (51.2752%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 44.3)
    * *Intent:* /** * @inheritDoc */
  * `setNewRelicParameter` (Impact: 7.3)
    * *Intent:* /** * Returns the appname where this log should be sent. Each log can override the default appname, ...
  * `getAppName` (Impact: 6.4)
  * `getTransactionName` (Impact: 6.4)
  * `__construct` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 31`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 23`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 7`, `doc: 16`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bool $bubble = true, 
        protected bool $explodeArrays = false, **
         * Some context and extra data is passed into the handler, $bubble, d to use the NewRelicHandler', 
    public function __construct(
        int|string|Level $level = Level::Error, Monolog\Level, Monolog\Formatter\FormatterInterface...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/SyslogUdpHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.679 IQR)
- **Top Global Matches:** file_cluster_13: 12.679, file_cluster_8: 13.029, file_cluster_7: 13.156
- **Magnitude:** 98.02 | **LOC:** 155 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.2594%), Tech Debt (31.9556%)
**Top Internal Functions/Classes:**
  * `makeCommonSyslogHeader` (Impact: 8.6)
  * `splitMessageIntoLines` (Impact: 7.7)
  * `__construct` (Impact: 6.3)
    * *Intent:* /** @var array<self::RFC*, string> */
  * `write` (Impact: 4.5)
    * *Intent:* /** * @param string $host Either IP/hostname or a path to a unix socket (port must be 0 then) * @par...
  * `setSocket` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 25`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 62`, `orphaned_logic: 1`
* *Architecture:* `io: 9`, `api: 3`, `import: 6`
* *Defense:* `doc: 19`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` d to use the SyslogUdpHandler', Monolog\Level, Monolog\LogRecord, Monolog\Handler\SyslogUdp\UdpSocket, Monolog\Utils, DateTimeInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/NativeMailerHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.883 IQR)
- **Top Global Matches:** file_cluster_13: 12.883, file_cluster_8: 13.026, file_cluster_7: 13.103
- **Magnitude:** 97.26 | **LOC:** 180 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.2109%), Tech Debt (94.8908%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 13.2)
    * *Intent:* /** * @param string|string[] $to The receiver of the mail * @param string $subject The subject of th...
  * `addHeader` (Impact: 9.2)
    * *Intent:* /** * Optional parameters for the message * @var string[]
  * `setContentType` (Impact: 6.5)
    * *Intent:* /** * Add parameters to the message * * @param string|string[] $parameters Custom added parameters
  * `setEncoding` (Impact: 6.5)
    * *Intent:* /** * @inheritDoc */
  * `getContentType` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 40`, `orphaned_logic: 4`
* *Architecture:* `io: 6`, `api: 7`, `import: 2`
* *Defense:* `safety: 1`, `doc: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Monolog\Level, Monolog\Formatter\LineFormatter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/CubeHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.028 IQR)
- **Top Global Matches:** file_cluster_13: 12.028, file_cluster_8: 12.192, file_cluster_7: 12.437
- **Magnitude:** 96.44 | **LOC:** 168 | **CtrlFlow:** 44.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.7493%), Tech Debt (26.3198%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 11.2)
  * `__construct` (Impact: 9.1)
    * *Intent:* /** * Logs to Cube. * * @link https://github.com/square/cube/wiki * @author Wan Chen <kami@kamisama....
  * `connectUdp` (Impact: 7.7)
  * `writeHttp` (Impact: 6.9)
  * `writeUdp` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 46`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `doc: 13`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` d to use udp URLs with the CubeHandler', Monolog\Level, Monolog\LogRecord, Monolog\Utils, d to use http URLs with the CubeHandler'
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Level.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.233 IQR)
- **Top Global Matches:** file_cluster_8: 12.233, file_cluster_7: 12.411, file_cluster_13: 12.487
- **Magnitude:** 93.84 | **LOC:** 210 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.148%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromName` (Impact: 4.7)
    * *Intent:* /** * Detailed debug information */
  * `getName` (Impact: 4.1)
    * *Intent:* /** * Action must be taken immediately *
  * `toPsrLogLevel` (Impact: 4.1)
  * `toRFC5424Level` (Impact: 4.1)
    * *Intent:* /** * @param value-of<self::VALUES> $value
  * `fromValue` (Impact: 2.2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 20`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`
* *Architecture:* `api: 18`, `import: 1`
* *Defense:* `doc: 20`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.797
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.463139
  * `Imports (Out-Degree: 0):` 
    case Debug = 100, isHigherThan methods are
 * not enough, Psr\Log\LogLevel, s(Level $level): bool
    
        return $this->value <= $level->value
  * `Imported By (In-Degree: 62):` (Excluded from Brief to save tokens)

### `src/Monolog/Handler/ChromePHPHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.935 IQR)
- **Top Global Matches:** file_cluster_13: 11.935, file_cluster_8: 12.249, file_cluster_7: 12.441
- **Magnitude:** 93.64 | **LOC:** 187 | **CtrlFlow:** 42.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.5676%), Tech Debt (71.7354%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 15.7)
  * `handleBatch` (Impact: 13.2)
  * `sendHeader` (Impact: 5.5)
  * `write` (Impact: 4.5)
  * `headersAccepted` (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 29`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `orphaned_logic: 3`
* *Architecture:* `io: 4`, `api: 2`, `import: 7`
* *Defense:* `safety: 2`, `doc: 13`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.076
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` Monolog\Formatter\ChromePHPFormatter, WebRequestRecognizerTrait, Monolog\Formatter\FormatterInterface, Monolog\Level, Monolog\LogRecord, Monolog\Utils, Monolog\JsonSerializableDateTimeImmutable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Monolog/Handler/ProcessHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.076 IQR)
- **Top Global Matches:** file_cluster_13: 13.076, file_cluster_8: 13.132, file_cluster_7: 13.301
- **Magnitude:** 91.92 | **LOC:** 192 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.929%), Tech Debt (56.15%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 10.5)
    * *Intent:* /** * Holds the process to receive data on its STDIN. *
  * `handleStartupErrors` (Impact: 9.4)
    * *Intent:* /** * Writes the record down to the log of the implementing handler *
  * `write` (Impact: 6.5)
    * *Intent:* /** * @var array<int, list<string>>
  * `close` (Impact: 5.7)
  * `ensureProcessIsStarted` (Impact: 3.9)
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
- `src/Monolog/Attribute/AsMonologProcessor.php` (PHP) | Magnitude: 28.76 | Delta: **0.465 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 7, doc: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Monolog/Handler/OverflowHandler.php` (PHP) | Magnitude: 10.82 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 11, branch: 3, doc: 3
- `tests/Monolog/Handler/ExceptionTestHandler.php` (PHP) | Magnitude: 2.42 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 4, safety: 2, import: 2
- `src/Monolog/Formatter/LogmaticFormatter.php` (PHP) | Magnitude: 24.02 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, state_mutation: 7, doc: 6
- `src/Monolog/Handler/Curl/Util.php` (PHP) | Magnitude: 37.04 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 24, structural_boundaries: 8, branch: 6
- `src/Monolog/Formatter/ElasticsearchFormatter.php` (PHP) | Magnitude: 20.28 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, doc: 14, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Monolog/LogRecord.php` (PHP) | Magnitude: 91.62 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 33, structural_boundaries: 27, api: 21
- `src/Monolog/ErrorHandler.php` (PHP) | Magnitude: 211.9 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 177, state_mutation: 103, branch: 35, structural_boundaries: 33
- `src/Monolog/Formatter/SyslogFormatter.php` (PHP) | Magnitude: 17.64 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 13, encapsulation: 8, state_mutation: 5
- `src/Monolog/Handler/MissingExtensionException.php` (PHP) | Magnitude: 12.6 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 4, branch: 1, class_start: 1, safety: 1
- `src/Monolog/Handler/AbstractSyslogHandler.php` (PHP) | Magnitude: 33.98 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 14, state_mutation: 14, doc: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Monolog/JsonSerializableDateTimeImmutable.php` (PHP) | Magnitude: 20.16 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, state_mutation: 6, api: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Monolog/Formatter/LineFormatter.php` -> **angeljqv** (100.0% isolated ownership) | Magnitude: 341.4
- `src/Monolog/Handler/TelegramBotHandler.php` -> **Dawid Nowak** (100.0% isolated ownership) | Magnitude: 170.0
- `src/Monolog/Formatter/GelfMessageFormatter.php` -> **Tobias Lorenz** (100.0% isolated ownership) | Magnitude: 168.5
- `src/Monolog/Handler/DeduplicationHandler.php` -> **Denis** (100.0% isolated ownership) | Magnitude: 168.34
- `src/Monolog/Formatter/JsonFormatter.php` -> **Adrien SIMON** (100.0% isolated ownership) | Magnitude: 136.02

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

- `src/Monolog/LogRecord.php` -> **Severity: 49.755** (Embedded: 0.7256 * Error Risk: 68.568%)
- `src/Monolog/Level.php` -> **Severity: 39.462** (Embedded: 0.4631 * Error Risk: 85.2056%)
- `src/Monolog/Utils.php` -> **Severity: 20.109** (Embedded: 0.2183 * Error Risk: 92.1213%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 7.218** (Embedded: 0.0752 * Error Risk: 95.9218%)
- `src/Monolog/Logger.php` -> **Severity: 6.332** (Embedded: 0.097 * Error Risk: 65.2643%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Monolog/LogRecord.php` -> **Severity: 22988.955** (Blast Radius: 230.804 * Doc Risk: 99.6038%)
- `src/Monolog/Level.php` -> **Severity: 5183.531** (Blast Radius: 73.797 * Doc Risk: 70.2404%)
- `src/Monolog/Logger.php` -> **Severity: 1169.377** (Blast Radius: 16.876 * Doc Risk: 69.2923%)
- `src/Monolog/Utils.php` -> **Severity: 1097.473** (Blast Radius: 42.217 * Doc Risk: 25.996%)
- `src/Monolog/Formatter/LineFormatter.php` -> **Severity: 672.52** (Blast Radius: 14.443 * Doc Risk: 46.5637%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
