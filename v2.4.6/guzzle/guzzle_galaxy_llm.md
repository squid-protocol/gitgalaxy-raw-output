# ARCHITECTURAL_BRIEF: guzzle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/guzzle` |
| **Timestamp** | `2026-08-03T19:31:11.803183+00:00` |
| **Scan Duration** | `0.34s` |
| **Git Branch** | `7.10` |
| **Git Commit** | `fb92d95f80a9da51bf8f2a5b26d8e8ea3b6d99ed` |
| **Git Remote** | `https://github.com/guzzle/guzzle.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 49 malicious artifacts.

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
| Total Artifacts | 114 |
| Analyzed Artifacts (Scanned) | 54 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 60 |
| Total LOC | 3423 |
| Volatility Index | 0.019 |
| % Scanned of codebase = | 47.4% |
| Dominant Lang | PHP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5662 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1934 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4359 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PHP | 46 | 3027 | 85.2% |
| MARKDOWN | 3 | 0 | 5.6% |
| JSON | 2 | 137 | 3.7% |
| DOCKERFILE | 1 | 8 | 1.9% |
| MAKEFILE | 1 | 68 | 1.9% |
| JAVASCRIPT | 1 | 183 | 1.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.563`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 26 | 48.1% |
| file_cluster_8 | 24 | 44.4% |
| file_cluster_4 | 1 | 1.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 60*

**Composition by Extension & Reason:**
- `.php`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rst`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dist`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.neon`: 1x Excluded (Unsupported Extension: '.neon')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 47.6 | 21.9 | 22.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 19.5 | 13.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.5 | 30.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.2 | 2.6 | 80.0 |
| API Exposure | 0.0 | 11.7 | 3.8 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.6 | 99.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.1 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 84.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.5 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 44.3 | 33.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 54.6 | 98.7 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 40.8 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Handler/StreamHandler.php` (Hits: 15)
- `tests/server.js` (Hits: 5)
- `src/Handler/HeaderProcessor.php` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Utils.php** (`src/Utils.php`) — 7 inbound connections
2. **RequestException.php** (`src/Exception/RequestException.php`) — 4 inbound connections
3. **GuzzleException.php** (`src/Exception/GuzzleException.php`) — 3 inbound connections
4. **TransferStats.php** (`src/TransferStats.php`) — 3 inbound connections
5. **ConnectException.php** (`src/Exception/ConnectException.php`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Client.php** (`src/Client.php`) — 18 outbound dependencies
2. **StreamHandler.php** (`src/Handler/StreamHandler.php`) — 14 outbound dependencies
3. **RequestOptions.php** (`src/RequestOptions.php`) — 13 outbound dependencies
4. **CurlFactory.php** (`src/Handler/CurlFactory.php`) — 11 outbound dependencies
5. **MockHandler.php** (`src/Handler/MockHandler.php`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `format` (@ `src/MessageFormatter.php`) -> Impact: **418.8** | LOC: 115
  * *Intent:* * The following variable substitutions are supported: * * - {request}: Full HTTP request message * - {response}: Full HTTP response message * - {ts}: ...
- `GuzzleServer` (@ `tests/server.js`) -> Impact: **203.9** | LOC: 198
  * *Intent:* /** * Guzzle node.js test server to return queued responses to HTTP requests and * expose a RESTful API for enqueueing responses and retrieving the re...
- `setCookie` (@ `src/Cookie/CookieJar.php`) -> Impact: **132.1** | LOC: 42
- `fromString` (@ `src/Cookie/SetCookie.php`) -> Impact: **121.3** | LOC: 46
- `createStream` (@ `src/Handler/StreamHandler.php`) -> Impact: **113.5** | LOC: 87
  * *Intent:* /** * @return resource */
- `__invoke` (@ `src/Handler/MockHandler.php`) -> Impact: **112.4** | LOC: 66
  * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. *
- `__invoke` (@ `src/Handler/StreamHandler.php`) -> Impact: **106.8** | LOC: 57
  * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $options Request transfer options. */
- `modifyRequest` (@ `src/RedirectMiddleware.php`) -> Impact: **98.4** | LOC: 48
- `createResponse` (@ `src/Handler/StreamHandler.php`) -> Impact: **89.7** | LOC: 49
  * *Intent:* /** * @param resource $stream */
- `createHeaderFn` (@ `src/Handler/CurlFactory.php`) -> Impact: **86.4** | LOC: 48

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `log` (@ `src/Middleware.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Middleware that invokes a callback before and after sending a request. * * The provided listener cannot modify or alter the response. It simply ...
- `history` (@ `src/Middleware.php`) -> **O(2^N) [Recursive]**
- `cookies` (@ `src/Middleware.php`) -> **O(2^N) [Recursive]**
- `setCookie` (@ `src/Cookie/CookieJar.php`) -> **O(2^N) [Recursive]**
- `load` (@ `src/Cookie/FileCookieJar.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Saves the cookies to a file.
- `save` (@ `src/Cookie/FileCookieJar.php`) -> **O(2^N) [Recursive]**
- `supportsHttp2` (@ `src/Handler/CurlFactory.php`) -> **O(2^N) [Recursive]**
- `supportsTls13` (@ `src/Handler/CurlFactory.php`) -> **O(2^N) [Recursive]**
- `remove` (@ `src/HandlerStack.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Set the HTTP handler that actually returns a promise. * * @param callable(RequestInterface, array): PromiseInterface $handler Accepts a request ...
- `toArray` (@ `src/Cookie/CookieJar.php`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Evaluate if this cookie should be persisted to storage * that survives between requests. * * @param SetCookie $cookie Being evaluated. * @param ...

### Highest Data Gravity (Database Complexity)
- `GuzzleServer` (@ `tests/server.js`) -> DB Complexity: **40**
  * *Intent:* /** * Guzzle node.js test server to return queued responses to HTTP requests and * expose a RESTful API for enqueueing responses and retrieving the re...
- `format` (@ `src/MessageFormatter.php`) -> DB Complexity: **29**
  * *Intent:* * The following variable substitutions are supported: * * - {request}: Full HTTP request message * - {response}: Full HTTP response message * - {ts}: ...
- `createStream` (@ `src/Handler/StreamHandler.php`) -> DB Complexity: **21**
  * *Intent:* /** * @return resource */
- `getDefaultContext` (@ `src/Handler/StreamHandler.php`) -> DB Complexity: **20**
- `create` (@ `src/Exception/RequestException.php`) -> DB Complexity: **17**
- `parseHeaders` (@ `src/Handler/HeaderProcessor.php`) -> DB Complexity: **16**
- `__invoke` (@ `src/Handler/MockHandler.php`) -> DB Complexity: **16**
  * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. *
- `add_proxy` (@ `src/Handler/StreamHandler.php`) -> DB Complexity: **16**
  * *Intent:* /** * @param mixed $value as passed via Request transfer options. */
- `__invoke` (@ `src/Handler/StreamHandler.php`) -> DB Complexity: **13**
  * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $options Request transfer options. */
- `checkDecode` (@ `src/Handler/StreamHandler.php`) -> DB Complexity: **11**
  * *Intent:* /** * @param resource $stream */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Handler` | 9 | 2364.34 | 33.7% | 71.35% |
| `src` | 18 | 2293.28 | 23.35% | 55.73% |
| `src/Cookie` | 5 | 1064.69 | 29.55% | 55.61% |
| `tests` | 6 | 536.0 | 17.25% | 0.0% |
| `src/Exception` | 9 | 331.7 | 12.98% | 32.98% |
| `__monolith__` | 7 | 265.92 | 3.58% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/functions.php` -> **100.0%** Exposure
- `src/TransferStats.php` -> **99.9999%** Exposure
- `src/BodySummarizer.php` -> **99.9995%** Exposure
- `src/PrepareBodyMiddleware.php` -> **99.9995%** Exposure
- `src/Handler/Proxy.php` -> **99.9955%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/BodySummarizer.php` -> **100.0%** Exposure
- `src/ClientInterface.php` -> **100.0%** Exposure
- `src/Cookie/CookieJar.php` -> **100.0%** Exposure
- `src/Cookie/CookieJarInterface.php` -> **100.0%** Exposure
- `src/Cookie/FileCookieJar.php` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/functions.php` -> **10** Orphaned Functions | **0** Duplicates
- `src/TransferStats.php` -> **9** Orphaned Functions | **0** Duplicates
- `src/HandlerStack.php` -> **8** Orphaned Functions | **0** Duplicates
- `src/Utils.php` -> **8** Orphaned Functions | **0** Duplicates
- `src/Cookie/CookieJar.php` -> **7** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/MessageFormatter.php`** -> AI Confidence: **99.32%**
2. **`src/Handler/CurlFactory.php`** -> AI Confidence: **99.31%**
3. **`src/Handler/MockHandler.php`** -> AI Confidence: **99.31%**
4. **`src/Handler/StreamHandler.php`** -> AI Confidence: **99.31%**
5. **`Makefile`** -> AI Confidence: **99.29%**
6. **`src/functions_include.php`** -> AI Confidence: **99.29%**
7. **`tests/bootstrap-phpstan.php`** -> AI Confidence: **99.29%**
8. **`src/Utils.php`** -> AI Confidence: **99.24%**
9. **`src/Cookie/SetCookie.php`** -> AI Confidence: **99.22%**
10. **`src/RequestOptions.php`** -> AI Confidence: **99.16%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/Cookie/CookieJar.php` -> **100.0%** Exposure
- `src/Cookie/SetCookie.php` -> **100.0%** Exposure
- `src/Exception/RequestException.php` -> **100.0%** Exposure
- `src/Handler/CurlFactory.php` -> **100.0%** Exposure
- `src/Handler/CurlMultiHandler.php` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `tests/Server.php` -> **100.0%** Exposure
- `src/Handler/StreamHandler.php` -> **54.0011%** Exposure
### Algorithmic DoS Exposure
- `src/ClientTrait.php` -> **100.0%** Exposure
- `src/Cookie/CookieJar.php` -> **100.0%** Exposure
- `src/Cookie/FileCookieJar.php` -> **100.0%** Exposure
- `src/Cookie/SessionCookieJar.php` -> **100.0%** Exposure
- `src/Cookie/SetCookie.php` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `181` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Cookie/CookieJar.php` (PHP) -> Cumulative Risk: **820.54**
- **Archetype:** `file_cluster_8` (Distance: 12.193 IQR)
- **Magnitude:** 485.3 | **LOC:** 308 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `setCookie` (Impact: 132.1), `clear` (Impact: 78.6), `withCookieHeader` (Impact: 55.1)

### 2. `src/Middleware.php` (PHP) -> Cumulative Risk: **801.53**
- **Archetype:** `file_cluster_13` (Distance: 12.517 IQR)
- **Magnitude:** 271.68 | **LOC:** 269 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `log` (Impact: 57.4), `history` (Impact: 38.0), `cookies` (Impact: 37.5)

### 3. `src/Pool.php` (PHP) -> Cumulative Risk: **794.73**
- **Archetype:** `file_cluster_4` (Distance: 13.808 IQR)
- **Magnitude:** 133.28 | **LOC:** 126 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `__construct` (Impact: 49.4), `cmpCallback` (Impact: 15.7), `promise` (Impact: 5.4)

### 4. `src/HandlerStack.php` (PHP) -> Cumulative Risk: **784.97**
- **Archetype:** `file_cluster_8` (Distance: 13.463 IQR)
- **Magnitude:** 303.16 | **LOC:** 276 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `remove` (Impact: 35.4), `splice` (Impact: 34.5), `resolve` (Impact: 18.2)

### 5. `src/Handler/CurlMultiHandler.php` (PHP) -> Cumulative Risk: **774.15**
- **Archetype:** `file_cluster_13` (Distance: 12.9 IQR)
- **Magnitude:** 264.66 | **LOC:** 288 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `tick` (Impact: 44.2), `__construct` (Impact: 30.3), `processMessages` (Impact: 22.8)

### 6. `src/Exception/RequestException.php` (PHP) -> Cumulative Risk: **757.95**
- **Archetype:** `file_cluster_13` (Distance: 13.653 IQR)
- **Magnitude:** 189.76 | **LOC:** 151 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `create` (Impact: 63.7), `__construct` (Impact: 30.1), `wrapException` (Impact: 5.4)

### 7. `src/RedirectMiddleware.php` (PHP) -> Cumulative Risk: **731.54**
- **Archetype:** `file_cluster_13` (Distance: 12.177 IQR)
- **Magnitude:** 258.08 | **LOC:** 229 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `modifyRequest` (Impact: 98.4), `checkRedirect` (Impact: 37.0), `__invoke` (Impact: 27.3)

### 8. `src/Handler/CurlFactory.php` (PHP) -> Cumulative Risk: **729.52**
- **Archetype:** `file_cluster_13` (Distance: 12.724 IQR)
- **Magnitude:** 720.22 | **LOC:** 742 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `createHeaderFn` (Impact: 86.4), `applyBody` (Impact: 78.5), `createRejection` (Impact: 55.0)

### 9. `src/Utils.php` (PHP) -> Cumulative Risk: **722.22**
- **Archetype:** `file_cluster_13` (Distance: 12.547 IQR)
- **Magnitude:** 220.2 | **LOC:** 385 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `chooseHandler` (Impact: 48.8), `defaultCaBundle` (Impact: 28.1), `isHostInNoProxy` (Impact: 22.6)

### 10. `src/Handler/MockHandler.php` (PHP) -> Cumulative Risk: **713.03**
- **Archetype:** `file_cluster_13` (Distance: 14.002 IQR)
- **Magnitude:** 292.58 | **LOC:** 213 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `__invoke` (Impact: 112.4), `append` (Impact: 31.0), `__construct` (Impact: 20.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Handler/StreamHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.232 IQR)
- **Top Global Matches:** file_cluster_13: 13.232, file_cluster_8: 13.416, file_cluster_11: 13.553
- **Magnitude:** 858.9 | **LOC:** 635 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (38.655%), Tech Debt (12.8783%)
**Top Internal Functions/Classes:**
  * `createStream` (Impact: 113.5 | O(N^5) | DB: 21)
    * *Intent:* /** * @return resource */
  * `__invoke` (Impact: 106.8 | O(N^5) | DB: 13)
    * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $o...
  * `createResponse` (Impact: 89.7 | O(N^5) | DB: 6)
    * *Intent:* /** * @param resource $stream */
  * `parse_proxy` (Impact: 68.0 | O(N^5) | DB: 4)
    * *Intent:* /** * Parses the given proxy URL to make it compatible with the format PHP's stream context expects....
  * `add_proxy` (Impact: 61.8 | O(N^5) | DB: 16)
    * *Intent:* /** * @param mixed $value as passed via Request transfer options. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 87`, `args: 20`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 173`, `dead_code: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 15`, `api: 1`, `import: 13`
* *Defense:* `safety: 47`, `doc: 24`, `test: 3`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.852
  * `Choke Point (Betweenness):` 0.009434 | `Ripple Effect (Closeness):` 0.071118
  * `Imports (Out-Degree: 4):` GuzzleHttp\Promise, Psr\Http\Message\StreamInterface, GuzzleHttp\Utils, GuzzleHttp\Promise\FulfilledPromise, Psr\Http\Message\ResponseInterface, GuzzleHttp\Psr7, Psr\Http\Message\UriInterface, GuzzleHttp\Exception\ConnectException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/CurlFactory.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.724 IQR)
- **Top Global Matches:** file_cluster_13: 12.724, file_cluster_8: 12.813, file_cluster_0: 13.092
- **Magnitude:** 720.22 | **LOC:** 742 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (44.4045%), Tech Debt (48.1477%)
**Top Internal Functions/Classes:**
  * `createHeaderFn` (Impact: 86.4 | O(N^6) | DB: 10)
  * `applyBody` (Impact: 78.5 | O(N^6) | DB: 3)
  * `createRejection` (Impact: 55.0 | O(N^5) | DB: 7)
  * `retryFailedRewind` (Impact: 51.8 | O(N^4) | DB: 2)
  * `create` (Impact: 40.8 | O(N^4) | DB: 8)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 70`, `args: 19`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 161`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 22`, `doc: 17`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Promise, Psr\Http\Message\UriInterface, GuzzleHttp\Utils, GuzzleHttp\Promise\FulfilledPromise, GuzzleHttp\Psr7\LazyOpenStream, GuzzleHttp\Exception\ConnectException, 1882 for more details.
                    $conf[\CURLOPT_HTTPHEADER][] = "$name, GuzzleHttp\Exception\RequestException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/MessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.189 IQR)
- **Top Global Matches:** file_cluster_13: 13.189, file_cluster_8: 13.218, file_cluster_7: 13.413
- **Magnitude:** 552.0 | **LOC:** 200 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (43.8764%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 418.8 | O(N^6) | DB: 29)
    * *Intent:* * The following variable substitutions are supported: * * - {request}: Full HTTP request message * -...
  * `__construct` (Impact: 11.2 | O(N^2) | DB: 2)
    * *Intent:* /** * Formats log messages using variable substitutions for requests, responses, * and other transac...
  * `headers` (Impact: 8.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 16`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 106`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 3`, `doc: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\MessageInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/CookieJar.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.193 IQR)
- **Top Global Matches:** file_cluster_8: 12.193, file_cluster_13: 12.333, file_cluster_7: 12.397
- **Magnitude:** 485.3 | **LOC:** 308 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (38.1185%), Tech Debt (85.6401%)
**Top Internal Functions/Classes:**
  * `setCookie` (Impact: 132.1 | O(2^N) | DB: 3)
  * `clear` (Impact: 78.6 | O(N^6) | DB: 7)
  * `withCookieHeader` (Impact: 55.1 | O(N^5) | DB: 6)
  * `getCookieByName` (Impact: 25.5 | O(N^4))
  * `getCookiePathFromRequest` (Impact: 24.9 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 53`, `args: 16`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 84`, `orphaned_logic: 7`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 1`, `doc: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/HandlerStack.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.463 IQR)
- **Top Global Matches:** file_cluster_8: 13.463, file_cluster_13: 13.471, file_cluster_7: 13.545
- **Magnitude:** 303.16 | **LOC:** 276 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (35.2074%), Tech Debt (96.9053%)
**Top Internal Functions/Classes:**
  * `remove` (Impact: 35.4 | O(2^N) | DB: 3)
    * *Intent:* /** * Set the HTTP handler that actually returns a promise. * * @param callable(RequestInterface, ar...
  * `splice` (Impact: 34.5 | O(N^4) | DB: 10)
  * `resolve` (Impact: 18.2 | O(N^4) | DB: 4)
    * *Intent:* /** * Unshift a middleware to the bottom of the stack.
  * `debugCallable` (Impact: 18.1 | O(N^4))
  * `findByName` (Impact: 15.5 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 39`, `args: 16`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 109`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/MockHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.002 IQR)
- **Top Global Matches:** file_cluster_13: 14.002, file_cluster_8: 14.41, file_cluster_11: 14.446
- **Magnitude:** 292.58 | **LOC:** 213 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (39.3113%), Tech Debt (92.6815%)
**Top Internal Functions/Classes:**
  * `__invoke` (Impact: 112.4 | O(N^6) | DB: 16)
    * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. *
  * `append` (Impact: 31.0 | O(N^4))
  * `__construct` (Impact: 20.5 | O(N^3) | DB: 5)
    * *Intent:* /** * @var callable|null */
  * `invokeStats` (Impact: 18.5 | O(N^3) | DB: 4)
  * `createWithMiddleware` (Impact: 12.2 | O(N^2) | DB: 3)
    * *Intent:* /** * @var array
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 40`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 71`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 8`, `import: 9`
* *Defense:* `safety: 18`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Promise, Psr\Http\Message\StreamInterface, GuzzleHttp\Utils, Psr\Http\Message\ResponseInterface, GuzzleHttp\TransferStats, GuzzleHttp\Exception\RequestException, Psr\Http\Message\RequestInterface, d for BC
            $this->append(...array_values($queue)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Middleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.517 IQR)
- **Top Global Matches:** file_cluster_13: 12.517, file_cluster_8: 12.672, file_cluster_7: 12.887
- **Magnitude:** 271.68 | **LOC:** 269 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (18.1954%), Tech Debt (84.8229%)
**Top Internal Functions/Classes:**
  * `log` (Impact: 57.4 | O(2^N) | DB: 5)
    * *Intent:* /** * Middleware that invokes a callback before and after sending a request. * * The provided listen...
  * `history` (Impact: 38.0 | O(2^N) | DB: 5)
  * `cookies` (Impact: 37.5 | O(2^N) | DB: 2)
  * `httpErrors` (Impact: 35.3 | O(N^6) | DB: 2)
  * `tap` (Impact: 26.8 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 106`, `args: 34`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 8`, `doc: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` GuzzleHttp\Promise, Psr\Log\LoggerInterface, Psr\Http\Message\ResponseInterface, GuzzleHttp\Cookie\CookieJarInterface, GuzzleHttp\Exception\RequestException, Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.809 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.142 IQR)
- **Top Global Matches:** file_cluster_8: 11.809, file_cluster_13: 11.911, file_cluster_11: 12.1
- **Magnitude:** 268.56 | **LOC:** 262 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (29.5858%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GuzzleServer` (Impact: 203.9 | O(N^3) | DB: 40)
    * *Intent:* /** * Guzzle node.js test server to return queued responses to HTTP requests and * expose a RESTful ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 25`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 60`
* *Architecture:* `io: 5`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 4`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http, url, http-auth, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Handler/CurlMultiHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.9 IQR)
- **Top Global Matches:** file_cluster_13: 12.9, file_cluster_8: 13.222, file_cluster_11: 13.31
- **Magnitude:** 264.66 | **LOC:** 288 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (38.6801%), Tech Debt (96.7148%)
**Top Internal Functions/Classes:**
  * `tick` (Impact: 44.2 | O(N^6) | DB: 2)
  * `__construct` (Impact: 30.3 | O(N^3) | DB: 7)
  * `processMessages` (Impact: 22.8 | O(N^4) | DB: 4)
  * `execute` (Impact: 22.3 | O(N^4) | DB: 1)
  * `__get` (Impact: 14.9 | O(N^3) | DB: 3)
    * *Intent:* /** @var resource|\CurlMultiHandle */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 36`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 67`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 6`, `doc: 27`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.852
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071118
  * `Imports (Out-Degree: 1):` GuzzleHttp\Promise, GuzzleHttp\Promise\Promise, GuzzleHttp\Utils, Closure, Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/RedirectMiddleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.177 IQR)
- **Top Global Matches:** file_cluster_13: 12.177, file_cluster_8: 12.353, file_cluster_7: 12.614
- **Magnitude:** 258.08 | **LOC:** 229 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (33.7572%), Tech Debt (30.5308%)
**Top Internal Functions/Classes:**
  * `modifyRequest` (Impact: 98.4 | O(2^N) | DB: 10)
  * `checkRedirect` (Impact: 37.0 | O(N^4) | DB: 2)
  * `__invoke` (Impact: 27.3 | O(N^4) | DB: 1)
  * `guardMax` (Impact: 12.6 | O(N^3) | DB: 3)
  * `redirectUri` (Impact: 8.8 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 35`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 53`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 8`, `doc: 13`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Psr\Http\Message\UriInterface, Psr\Http\Message\ResponseInterface, GuzzleHttp\Exception\TooManyRedirectsException, GuzzleHttp\Exception\BadResponseException, Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Utils.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_13: 12.547, file_cluster_8: 12.858, file_cluster_7: 13.008
- **Magnitude:** 220.2 | **LOC:** 385 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (36.8781%), Tech Debt (98.9883%)
**Top Internal Functions/Classes:**
  * `chooseHandler` (Impact: 48.8 | O(N^4) | DB: 11)
    * *Intent:* /** * Returns a debug stream based on the provided variable.
  * `defaultCaBundle` (Impact: 28.1 | O(N^4) | DB: 7)
  * `isHostInNoProxy` (Impact: 22.6 | O(N^4) | DB: 1)
  * `describeType` (Impact: 22.5 | O(N^4) | DB: 1)
    * *Intent:* /**
  * `debugResource` (Impact: 14.0 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 44`, `args: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 8`, `import: 6`
* *Defense:* `safety: 3`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 77.72
  * `Choke Point (Betweenness):` 0.022134 | `Ripple Effect (Closeness):` 0.132075
  * `Imports (Out-Degree: 5):` Psr\Http\Message\UriInterface, the allow_url_fopen ini setting, GuzzleHttp\Exception\InvalidArgumentException, GuzzleHttp\Handler\StreamHandler, or a custom HTTP handler.', GuzzleHttp\Handler\CurlMultiHandler, GuzzleHttp\Handler\CurlHandler, s cURL...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Cookie/SetCookie.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.044 IQR)
- **Top Global Matches:** file_cluster_8: 13.044, file_cluster_17: 13.153, file_cluster_7: 13.298
- **Magnitude:** 212.16 | **LOC:** 493 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (39.0605%), Tech Debt (58.4411%)
**Top Internal Functions/Classes:**
  * `fromString` (Impact: 121.3 | O(N^6) | DB: 9)
  * `__construct` (Impact: 51.1 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`, `orphaned_logic: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 12`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` '=') === false) 
            return new self($data, "
        return \substr($requestPath, an equal sign.
        if (!isset($pieces[0]) || \strpos($pieces[0], ', 
    public function matchesPath(string $requestPath): bool
    
        $cookiePath = $this->getPath(, \strlen($cookiePath)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Exception/RequestException.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.653 IQR)
- **Top Global Matches:** file_cluster_13: 13.653, file_cluster_8: 13.984, file_cluster_7: 14.114
- **Magnitude:** 189.76 | **LOC:** 151 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (34.2055%), Tech Debt (99.2508%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 63.7 | O(N^4) | DB: 17)
  * `__construct` (Impact: 30.1 | O(2^N) | DB: 7)
    * *Intent:* /** * @var ResponseInterface|null
  * `wrapException` (Impact: 5.4 | O(N^2))
    * *Intent:* // Set the code of the exception if the response is set and not future.
  * `getResponse` (Impact: 5.4 | O(N^2))
  * `getRequest` (Impact: 2.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 29`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 68`, `orphaned_logic: 6`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 6`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.881
  * `Choke Point (Betweenness):` 0.006531 | `Ripple Effect (Closeness):` 0.084906
  * `Imports (Out-Degree: 2):` Psr\Http\Client\RequestExceptionInterface, Psr\Http\Message\ResponseInterface, GuzzleHttp\BodySummarizerInterface, GuzzleHttp\BodySummarizer, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Cookie/FileCookieJar.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.478 IQR)
- **Top Global Matches:** file_cluster_13: 12.478, file_cluster_8: 12.495, file_cluster_7: 12.59
- **Magnitude:** 156.04 | **LOC:** 102 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (39.9866%), Tech Debt (59.4986%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 71.0 | O(2^N) | DB: 6)
    * *Intent:* /** * Saves the cookies to a file.
  * `save` (Impact: 40.8 | O(2^N) | DB: 5)
  * `__construct` (Impact: 14.4 | O(2^N) | DB: 3)
  * `__destruct` (Impact: 2.8 | O(N^2))
    * *Intent:* /** * Create a new FileCookieJar object * * @param string $cookieFile File to store the cookie data ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 15`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 4`, `import: 1`
* *Defense:* `safety: 1`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GuzzleHttp\Utils
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/CookieJarInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.419 IQR)
- **Top Global Matches:** file_cluster_13: 14.419, file_cluster_7: 14.929, file_cluster_8: 14.959
- **Magnitude:** 154.05 | **LOC:** 81 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Pool.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.808 IQR)
- **Top Global Matches:** file_cluster_4: 13.808, file_cluster_13: 13.824, file_cluster_8: 14.227
- **Magnitude:** 133.28 | **LOC:** 126 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (47.6287%), Tech Debt (80.3174%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 49.4 | O(N^5) | DB: 9)
    * *Intent:* /** * Sends an iterator of requests concurrently using a capped pool size. * * The pool will read fr...
  * `cmpCallback` (Impact: 15.7 | O(N^4) | DB: 5)
  * `promise` (Impact: 5.4 | O(2^N))
  * `batch` (Impact: 3.5 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 27`, `args: 7`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 5`
* *Defense:* `safety: 4`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise, GuzzleHttp\Promise\PromisorInterface, GuzzleHttp\Promise\EachPromise, Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.037 IQR)
- **Top Global Matches:** file_cluster_8: 8.037, file_cluster_7: 8.916, file_cluster_1: 9.165
- **Magnitude:** 130.36 | **LOC:** 86 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (15.061%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 2`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 2`
* *Defense:* `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/TestLogger.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.569 IQR)
- **Top Global Matches:** file_cluster_8: 11.569, file_cluster_13: 11.849, file_cluster_11: 12.035
- **Magnitude:** 109.76 | **LOC:** 100 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (24.2694%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasRecord` (Impact: 22.5 | O(N^4) | DB: 1)
  * `hasRecordThatPasses` (Impact: 18.0 | O(N^4) | DB: 1)
  * `__call` (Impact: 18.0 | O(N^4) | DB: 2)
  * `log` (Impact: 4.5 | O(N^3) | DB: 2)
  * `hasRecordThatContains` (Impact: 3.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 34`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Log\AbstractLogger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ClientInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.639 IQR)
- **Top Global Matches:** file_cluster_13: 14.639, file_cluster_7: 15.403, file_cluster_8: 15.413
- **Magnitude:** 96.8 | **LOC:** 85 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 1`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` 
    public function getConfig(?string $option = null, Psr\Http\Message\UriInterface, Psr\Http\Message\ResponseInterface, default request options of the client, a "handler"
     * (if utilized by the concrete client), Psr\Http\Message\RequestInterface, GuzzleHttp\Exception\GuzzleException, GuzzleHttp\Promise\PromiseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/Helpers.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.977 IQR)
- **Top Global Matches:** file_cluster_8: 11.977, file_cluster_17: 12.438, file_cluster_0: 12.446
- **Magnitude:** 78.92 | **LOC:** 40 | **CtrlFlow:** 61.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `readObjectAttribute` (Impact: 68.3 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 7`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `orphaned_logic: 1`
* *Architecture:* `api: 1`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TransferStats.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.64 IQR)
- **Top Global Matches:** file_cluster_13: 12.64, file_cluster_8: 12.813, file_cluster_7: 12.89
- **Magnitude:** 73.86 | **LOC:** 134 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (30.5115%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 11.7 | O(N^2) | DB: 9)
    * *Intent:* /** * @var float|null */
  * `getHandlerStat` (Impact: 6.2 | O(N^2))
    * *Intent:* /** * Gets handler specific error data.
  * `getResponse` (Impact: 5.4 | O(N^2))
  * `getTransferTime` (Impact: 5.4 | O(N^2))
  * `getRequest` (Impact: 2.8 | O(N^2))
    * *Intent:* /** * @param RequestInterface $request Request that was sent.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 9`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 1`, `doc: 28`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.508
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071032
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\UriInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/ClientTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.655 IQR)
- **Top Global Matches:** file_cluster_13: 12.655, file_cluster_8: 12.897, file_cluster_7: 12.93
- **Magnitude:** 72.78 | **LOC:** 242 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.4699%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 2.8 | O(N^2) | DB: 1)
    * *Intent:* /** * Create and send an HTTP request.
  * `head` (Impact: 2.8 | O(N^2) | DB: 1)
    * *Intent:* /** * Create and send an HTTP request. * * Use an absolute path to override the base path of the cli...
  * `put` (Impact: 2.8 | O(N^2) | DB: 1)
  * `post` (Impact: 2.8 | O(N^2) | DB: 1)
    * *Intent:* /** * Create and send an HTTP GET request. * * Use an absolute path to override the base path of the...
  * `patch` (Impact: 2.8 | O(N^2) | DB: 1)
    * *Intent:* /** * Create and send an HTTP GET request. * * Use an absolute path to override the base path of the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 24`, `import: 4`
* *Defense:* `safety: 1`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 1):` Psr\Http\Message\UriInterface, GuzzleHttp\Exception\GuzzleException, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/RetryMiddleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.665 IQR)
- **Top Global Matches:** file_cluster_13: 11.665, file_cluster_8: 11.78, file_cluster_7: 11.996
- **Magnitude:** 72.34 | **LOC:** 120 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (29.2494%), Tech Debt (77.4054%)
**Top Internal Functions/Classes:**
  * `__invoke` (Impact: 9.4 | O(N^4) | DB: 1)
    * *Intent:* /** * @param callable $decider Function that accepts the number of retries, * a request, [response],...
  * `onFulfilled` (Impact: 9.4 | O(N^4))
    * *Intent:* /** * Default exponential backoff delay function.
  * `onRejected` (Impact: 9.4 | O(N^4))
  * `__construct` (Impact: 9.3 | O(N^2) | DB: 4)
  * `doRetry` (Impact: 6.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 26`, `args: 9`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise, Psr\Http\Message\RequestInterface, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Handler/EasyHandle.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.107 IQR)
- **Top Global Matches:** file_cluster_13: 13.107, file_cluster_8: 13.614, file_cluster_7: 13.687
- **Magnitude:** 68.08 | **LOC:** 113 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (37.3401%), Tech Debt (93.0993%)
**Top Internal Functions/Classes:**
  * `createResponse` (Impact: 32.7 | O(N^5) | DB: 3)
  * `__get` (Impact: 5.4 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `orphaned_logic: 2`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 3`, `doc: 25`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Psr\Http\Message\StreamInterface, GuzzleHttp\Utils, Psr\Http\Message\ResponseInterface, GuzzleHttp\Psr7\Response, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/MessageFormatterInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.38 IQR)
- **Top Global Matches:** file_cluster_13: 14.38, file_cluster_8: 15.077, file_cluster_11: 15.199
- **Magnitude:** 67.73 | **LOC:** 19 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Http\Message\RequestInterface, Psr\Http\Message\ResponseInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Dockerfile` (DOCKERFILE) | Magnitude: 44.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 3, import: 3, structural_boundaries: 2, class_start: 2
- `src/Cookie/FileCookieJar.php` (PHP) | Magnitude: 156.04 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 22, doc: 18, structural_boundaries: 15
- `src/MessageFormatter.php` (PHP) | Magnitude: 552.0 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 106, branch: 62, structural_boundaries: 16
- `src/Handler/CurlFactory.php` (PHP) | Magnitude: 720.22 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 356, state_mutation: 161, branch: 84, structural_boundaries: 70
- `src/RetryMiddleware.php` (PHP) | Magnitude: 72.34 | Delta: **0.115 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 26, state_mutation: 21, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Pool.php` (PHP) | Magnitude: 133.28 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 43, structural_boundaries: 27, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/HandlerStack.php` (PHP) | Magnitude: 303.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 109, doc: 43, structural_boundaries: 39
- `tests/Server.php` (PHP) | Magnitude: 18.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, import: 4, doc: 3
- `src/RequestOptions.php` (PHP) | Magnitude: 39.58 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 25, immutability_locks: 25, api: 24, indent_spaces: 24
- `src/Handler/CurlFactoryInterface.php` (PHP) | Magnitude: 40.8 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, args: 2, func_start: 2
- `tests/server.js` (JAVASCRIPT) | Magnitude: 268.56 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 60, branch: 57, structural_boundaries: 25

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Middleware.php` -> Churn: **100.0%** | Cog Load: 18.1954% | Debt: 84.8229%
- `src/Cookie/CookieJar.php` -> Churn: **63.09%** | Cog Load: 38.1185% | Debt: 85.6401%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Handler/CurlFactory.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 720.22
- `src/Cookie/CookieJar.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 485.3
- `src/Middleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 271.68
- `src/Handler/CurlMultiHandler.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 264.66
- `src/RedirectMiddleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 258.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Utils.php` -> **Severity: 2.213** (Bridge: 0.0221 * Flux: 99.9999%)
- `src/Handler/StreamHandler.php` -> **Severity: 0.943** (Bridge: 0.0094 * Flux: 99.9999%)
- `src/Exception/RequestException.php` -> **Severity: 0.653** (Bridge: 0.0065 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Exception/RequestException.php` -> **Severity: 4.801** (Embedded: 0.0849 * Error Risk: 56.5456%)
- `src/Utils.php` -> **Severity: 3.387** (Embedded: 0.1321 * Error Risk: 25.6437%)
- `src/Handler/StreamHandler.php` -> **Severity: 3.305** (Embedded: 0.0711 * Error Risk: 46.4706%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 1.988** (Embedded: 0.0711 * Error Risk: 27.9594%)
- `src/BodySummarizer.php` -> **Severity: 1.846** (Embedded: 0.0674 * Error Risk: 27.3966%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Utils.php` -> **Severity: 5699.464** (Blast Radius: 77.72 * Doc Risk: 73.3333%)
- `src/RequestOptions.php` -> **Severity: 3425.707** (Blast Radius: 34.618 * Doc Risk: 98.9574%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 2585.2** (Blast Radius: 25.852 * Doc Risk: 100.0%)
- `src/BodySummarizer.php` -> **Severity: 2491.495** (Blast Radius: 24.915 * Doc Risk: 99.9998%)
- `src/Exception/RequestException.php` -> **Severity: 2372.742** (Blast Radius: 28.881 * Doc Risk: 82.1558%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
