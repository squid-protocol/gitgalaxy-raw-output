# ARCHITECTURAL_BRIEF: guzzle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_php/guzzle` |
| **Timestamp** | `2026-08-07T03:53:09.884590+00:00` |
| **Scan Duration** | `0.24s` |
| **Git Branch** | `7.10` |
| **Git Commit** | `fb92d95f80a9da51bf8f2a5b26d8e8ea3b6d99ed` |
| **Git Remote** | `https://github.com/guzzle/guzzle.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 49 malicious artifacts.

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
| Error & Exception Exposure | 0.0 | 95.3 | 50.6 | 66.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 43.6 | 30.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.1 | 2.5 | 80.0 |
| API Exposure | 0.0 | 11.7 | 3.8 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 56.6 | 99.9 | 0.0 |
| Commented Logic Exposure | 0.0 | 9.1 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 13.3 | 100.0 | 84.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.5 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 7.8 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 86.7 | 16.2 | 11.9 | 11.9 |
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

- `format` (@ `src/MessageFormatter.php`) -> Impact: **123.8** | LOC: 115
  * *Intent:* * The following variable substitutions are supported: * * - {request}: Full HTTP request message * - {response}: Full HTTP response message * - {ts}: ...
- `GuzzleServer` (@ `tests/server.js`) -> Impact: **106.9** | LOC: 198
  * *Intent:* /** * Guzzle node.js test server to return queued responses to HTTP requests and * expose a RESTful API for enqueueing responses and retrieving the re...
- `controlRequest` (@ `tests/server.js`) -> Impact: **67.8** | LOC: 76
- `createStream` (@ `src/Handler/StreamHandler.php`) -> Impact: **40.7** | LOC: 87
  * *Intent:* /** * @return resource */
- `__invoke` (@ `src/Handler/StreamHandler.php`) -> Impact: **37.5** | LOC: 57
  * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $options Request transfer options. */
- `fromString` (@ `src/Cookie/SetCookie.php`) -> Impact: **36.3** | LOC: 46
- `__invoke` (@ `src/Handler/MockHandler.php`) -> Impact: **34.5** | LOC: 66
  * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. *
- `createResponse` (@ `src/Handler/StreamHandler.php`) -> Impact: **31.5** | LOC: 49
  * *Intent:* /** * @param resource $stream */
- `setCookie` (@ `src/Cookie/CookieJar.php`) -> Impact: **28.1** | LOC: 42
- `create` (@ `src/Exception/RequestException.php`) -> Impact: **27.0** | LOC: 50

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 18 | 1411.48 | 23.35% | 55.73% |
| `src/Handler` | 9 | 1303.64 | 32.64% | 71.67% |
| `src/Cookie` | 5 | 565.79 | 29.55% | 55.61% |
| `tests` | 6 | 454.1 | 18.53% | 0.0% |
| `__monolith__` | 7 | 265.92 | 3.58% | 0.0% |
| `src/Exception` | 9 | 244.5 | 12.98% | 32.98% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `181` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Cookie/CookieJar.php` (PHP) -> Cumulative Risk: **579.91**
- **Archetype:** `file_cluster_8` (Distance: 12.193 IQR)
- **Magnitude:** 220.4 | **LOC:** 308 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (89.6228%), Tech Debt (85.6401%)
- **Heaviest Functions:** `setCookie` (Impact: 28.1), `clear` (Impact: 23.6), `withCookieHeader` (Impact: 19.1)

### 2. `src/Middleware.php` (PHP) -> Cumulative Risk: **570.27**
- **Archetype:** `file_cluster_13` (Distance: 12.508 IQR)
- **Magnitude:** 106.38 | **LOC:** 269 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), State Flux (99.9425%), Tech Debt (84.8229%)
- **Heaviest Functions:** `httpErrors` (Impact: 10.8), `tap` (Impact: 9.5), `log` (Impact: 9.3)

### 3. `src/Handler/CurlMultiHandler.php` (PHP) -> Cumulative Risk: **544.48**
- **Archetype:** `file_cluster_13` (Distance: 12.899 IQR)
- **Magnitude:** 163.06 | **LOC:** 288 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.7148%), Safety Score (80.4067%)
- **Heaviest Functions:** `__construct` (Impact: 15.6), `tick` (Impact: 13.9), `processMessages` (Impact: 9.8)

### 4. `src/Pool.php` (PHP) -> Cumulative Risk: **532.25**
- **Archetype:** `file_cluster_4` (Distance: 13.808 IQR)
- **Magnitude:** 87.78 | **LOC:** 126 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.987%), Safety Score (86.4127%)
- **Heaviest Functions:** `__construct` (Impact: 17.4), `cmpCallback` (Impact: 6.7), `batch` (Impact: 2.5)

### 5. `src/Exception/RequestException.php` (PHP) -> Cumulative Risk: **526.68**
- **Archetype:** `file_cluster_13` (Distance: 13.658 IQR)
- **Magnitude:** 127.36 | **LOC:** 151 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.2508%), Safety Score (90.5794%)
- **Heaviest Functions:** `create` (Impact: 27.0), `__construct` (Impact: 10.5), `wrapException` (Impact: 3.7)

### 6. `src/HandlerStack.php` (PHP) -> Cumulative Risk: **524.65**
- **Archetype:** `file_cluster_8` (Distance: 13.463 IQR)
- **Magnitude:** 205.16 | **LOC:** 276 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.9053%), Safety Score (94.5347%)
- **Heaviest Functions:** `splice` (Impact: 14.4), `__toString` (Impact: 8.1), `create` (Impact: 7.8)

### 7. `src/Utils.php` (PHP) -> Cumulative Risk: **514.69**
- **Archetype:** `file_cluster_13` (Distance: 12.547 IQR)
- **Magnitude:** 132.5 | **LOC:** 385 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (98.9883%), Verification (80.0%)
- **Heaviest Functions:** `chooseHandler` (Impact: 20.3), `defaultCaBundle` (Impact: 12.5), `isHostInNoProxy` (Impact: 9.6)

### 8. `src/RedirectMiddleware.php` (PHP) -> Cumulative Risk: **513.26**
- **Archetype:** `file_cluster_13` (Distance: 12.134 IQR)
- **Magnitude:** 133.48 | **LOC:** 229 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9992%), Verification (80.0%), Safety Score (73.8142%)
- **Heaviest Functions:** `modifyRequest` (Impact: 26.4), `checkRedirect` (Impact: 16.0), `__invoke` (Impact: 11.7)

### 9. `src/Handler/CurlFactory.php` (PHP) -> Cumulative Risk: **499.44**
- **Archetype:** `file_cluster_13` (Distance: 12.724 IQR)
- **Magnitude:** 378.42 | **LOC:** 742 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Verification (80.0%), Safety Score (79.968%)
- **Heaviest Functions:** `createHeaderFn` (Impact: 26.4), `applyBody` (Impact: 23.4), `retryFailedRewind` (Impact: 21.8)

### 10. `src/Handler/MockHandler.php` (PHP) -> Cumulative Risk: **498.75**
- **Archetype:** `file_cluster_13` (Distance: 14.002 IQR)
- **Magnitude:** 166.48 | **LOC:** 213 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (92.6815%), Verification (80.0%)
- **Heaviest Functions:** `__invoke` (Impact: 34.5), `append` (Impact: 12.8), `__construct` (Impact: 10.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Handler/StreamHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.228 IQR)
- **Top Global Matches:** file_cluster_13: 13.228, file_cluster_8: 13.413, file_cluster_11: 13.55
- **Magnitude:** 440.1 | **LOC:** 635 | **CtrlFlow:** 54.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (38.655%), Tech Debt (15.7563%)
**Top Internal Functions/Classes:**
  * `createStream` (Impact: 40.7)
    * *Intent:* /** * @return resource */
  * `__invoke` (Impact: 37.5)
    * *Intent:* /** * Sends an HTTP request. * * @param RequestInterface $request Request to send. * @param array $o...
  * `createResponse` (Impact: 31.5)
    * *Intent:* /** * @param resource $stream */
  * `parse_proxy` (Impact: 23.9)
    * *Intent:* /** * Parses the given proxy URL to make it compatible with the format PHP's stream context expects....
  * `add_proxy` (Impact: 21.6)
    * *Intent:* /** * @param mixed $value as passed via Request transfer options. */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 87`, `args: 19`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 173`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 15`, `api: 1`, `import: 13`
* *Defense:* `safety: 47`, `doc: 24`, `test: 3`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.852
  * `Choke Point (Betweenness):` 0.009434 | `Ripple Effect (Closeness):` 0.071118
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\TransferStats, GuzzleHttp\Utils, GuzzleHttp\Promise, Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface, 'close'...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/CurlFactory.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.724 IQR)
- **Top Global Matches:** file_cluster_13: 12.724, file_cluster_8: 12.813, file_cluster_0: 13.092
- **Magnitude:** 378.42 | **LOC:** 742 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (44.4045%), Tech Debt (48.1477%)
**Top Internal Functions/Classes:**
  * `createHeaderFn` (Impact: 26.4)
  * `applyBody` (Impact: 23.4)
  * `retryFailedRewind` (Impact: 21.8)
  * `createRejection` (Impact: 20.4)
  * `create` (Impact: 17.4)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 70`, `args: 19`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 161`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 7`, `import: 10`
* *Defense:* `safety: 22`, `doc: 17`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Exception\ConnectException, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\TransferStats, 1882 for more details.
                    $conf[\CURLOPT_HTTPHEADER][] = "$name, GuzzleHttp\Utils, GuzzleHttp\Promise, Psr\Http\Message\UriInterface, GuzzleHttp\Exception\RequestException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/server.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.799 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 4.42 IQR)
- **Top Global Matches:** file_cluster_8: 11.799, file_cluster_13: 11.887, file_cluster_11: 12.082
- **Magnitude:** 308.96 | **LOC:** 262 | **CtrlFlow:** 69.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GuzzleServer` (Impact: 106.9)
    * *Intent:* /** * Guzzle node.js test server to return queued responses to HTTP requests and * expose a RESTful ...
  * `controlRequest` (Impact: 67.8)
  * `loadAuthentifier` (Impact: 25.9)
    * *Intent:* * > Host: 127.0.0.1:8126 * > * > [{'status': 200, 'reason': 'OK', 'headers': {}, 'body': '' }] * * -...
  * `receivedRequest` (Impact: 14.8)
  * `firewallRequest` (Impact: 12.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 25`, `args: 13`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 60`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 5`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 4`, `doc: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` http-auth, url, http, crypto
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/MessageFormatter.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.189 IQR)
- **Top Global Matches:** file_cluster_13: 13.189, file_cluster_8: 13.218, file_cluster_7: 13.413
- **Magnitude:** 249.4 | **LOC:** 200 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8764%), Tech Debt (35.9641%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 123.8)
    * *Intent:* * The following variable substitutions are supported: * * - {request}: Full HTTP request message * -...
  * `__construct` (Impact: 7.5)
    * *Intent:* /** * Formats log messages using variable substitutions for requests, responses, * and other transac...
  * `headers` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 16`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 106`, `orphaned_logic: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 3`, `doc: 14`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\MessageInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/CookieJar.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.193 IQR)
- **Top Global Matches:** file_cluster_8: 12.193, file_cluster_13: 12.333, file_cluster_7: 12.397
- **Magnitude:** 220.4 | **LOC:** 308 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.1185%), Tech Debt (85.6401%)
**Top Internal Functions/Classes:**
  * `setCookie` (Impact: 28.1)
  * `clear` (Impact: 23.6)
  * `withCookieHeader` (Impact: 19.1)
  * `getCookiePathFromRequest` (Impact: 12.9)
  * `getCookieByName` (Impact: 10.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 53`, `args: 16`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 84`, `orphaned_logic: 7`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 1`, `doc: 19`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/HandlerStack.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.463 IQR)
- **Top Global Matches:** file_cluster_8: 13.463, file_cluster_13: 13.471, file_cluster_7: 13.545
- **Magnitude:** 205.16 | **LOC:** 276 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.2074%), Tech Debt (96.9053%)
**Top Internal Functions/Classes:**
  * `splice` (Impact: 14.4)
  * `__toString` (Impact: 8.1)
  * `create` (Impact: 7.8)
  * `resolve` (Impact: 7.8)
    * *Intent:* /** * Unshift a middleware to the bottom of the stack.
  * `remove` (Impact: 7.7)
    * *Intent:* /** * Set the HTTP handler that actually returns a promise. * * @param callable(RequestInterface, ar...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 39`, `args: 16`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `state_mutation: 109`, `orphaned_logic: 8`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `doc: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.327
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/MockHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.002 IQR)
- **Top Global Matches:** file_cluster_13: 14.002, file_cluster_8: 14.41, file_cluster_11: 14.446
- **Magnitude:** 166.48 | **LOC:** 213 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.3113%), Tech Debt (92.6815%)
**Top Internal Functions/Classes:**
  * `__invoke` (Impact: 34.5)
    * *Intent:* /** * Creates a new MockHandler that uses the default handler stack list of * middlewares. *
  * `append` (Impact: 12.8)
  * `__construct` (Impact: 10.5)
    * *Intent:* /** * @var callable|null */
  * `invokeStats` (Impact: 9.5)
  * `createWithMiddleware` (Impact: 8.2)
    * *Intent:* /** * @var array
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 40`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 71`, `orphaned_logic: 6`
* *Architecture:* `io: 2`, `api: 8`, `import: 9`
* *Defense:* `safety: 18`, `doc: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\TransferStats, GuzzleHttp\HandlerStack, GuzzleHttp\Utils, GuzzleHttp\Promise, Psr\Http\Message\ResponseInterface, d for BC
            $this->append(...array_values($queue), GuzzleHttp\Exception\RequestException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Handler/CurlMultiHandler.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.899 IQR)
- **Top Global Matches:** file_cluster_13: 12.899, file_cluster_8: 13.221, file_cluster_11: 13.309
- **Magnitude:** 163.06 | **LOC:** 288 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.6801%), Tech Debt (96.7148%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 15.6)
  * `tick` (Impact: 13.9)
  * `processMessages` (Impact: 9.8)
  * `execute` (Impact: 9.3)
  * `__get` (Impact: 8.0)
    * *Intent:* /** @var resource|\CurlMultiHandle */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 36`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 67`, `dead_code: 1`, `fragile_debt: 1`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 6`, `doc: 27`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.852
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071118
  * `Imports (Out-Degree: 1):` GuzzleHttp\Promise\Promise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Utils, GuzzleHttp\Promise, Closure, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Cookie/CookieJarInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.419 IQR)
- **Top Global Matches:** file_cluster_13: 14.419, file_cluster_7: 14.929, file_cluster_8: 14.959
- **Magnitude:** 154.05 | **LOC:** 81 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 6`, `import: 2`
* *Defense:* `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.014
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018868
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/RedirectMiddleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.134 IQR)
- **Top Global Matches:** file_cluster_13: 12.134, file_cluster_8: 12.311, file_cluster_7: 12.572
- **Magnitude:** 133.48 | **LOC:** 229 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.7572%), Tech Debt (30.5308%)
**Top Internal Functions/Classes:**
  * `modifyRequest` (Impact: 26.4)
  * `checkRedirect` (Impact: 16.0)
  * `__invoke` (Impact: 11.7)
  * `guardMax` (Impact: 6.5)
  * `redirectUri` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 35`, `args: 9`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 53`, `orphaned_logic: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 8`, `doc: 13`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Exception\BadResponseException, Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface, GuzzleHttp\Exception\TooManyRedirectsException, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Utils.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.547 IQR)
- **Top Global Matches:** file_cluster_13: 12.547, file_cluster_8: 12.858, file_cluster_7: 13.008
- **Magnitude:** 132.5 | **LOC:** 385 | **CtrlFlow:** 39.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.8781%), Tech Debt (98.9883%)
**Top Internal Functions/Classes:**
  * `chooseHandler` (Impact: 20.3)
    * *Intent:* /** * Returns a debug stream based on the provided variable.
  * `defaultCaBundle` (Impact: 12.5)
  * `isHostInNoProxy` (Impact: 9.6)
  * `describeType` (Impact: 9.5)
    * *Intent:* /**
  * `debugResource` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 44`, `args: 13`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 8`, `import: 6`
* *Defense:* `safety: 3`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 77.72
  * `Choke Point (Betweenness):` 0.022134 | `Ripple Effect (Closeness):` 0.132075
  * `Imports (Out-Degree: 5):` GuzzleHttp\Handler\CurlHandler, GuzzleHttp\Handler\StreamHandler, s cURL, GuzzleHttp\Handler\CurlMultiHandler, GuzzleHttp\Handler\Proxy, or a custom HTTP handler.', Psr\Http\Message\UriInterface, GuzzleHttp\Exception\InvalidArgumentException...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.037 IQR)
- **Top Global Matches:** file_cluster_8: 8.037, file_cluster_7: 8.916, file_cluster_1: 9.165
- **Magnitude:** 130.36 | **LOC:** 86 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
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

### `src/Exception/RequestException.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.658 IQR)
- **Top Global Matches:** file_cluster_13: 13.658, file_cluster_8: 13.987, file_cluster_7: 14.116
- **Magnitude:** 127.36 | **LOC:** 151 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.2055%), Tech Debt (99.2508%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 27.0)
  * `__construct` (Impact: 10.5)
    * *Intent:* /** * @var ResponseInterface|null
  * `wrapException` (Impact: 3.7)
    * *Intent:* // Set the code of the exception if the response is set and not future.
  * `getResponse` (Impact: 3.7)
  * `getRequest` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 27`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 68`, `orphaned_logic: 6`
* *Architecture:* `api: 7`, `import: 5`
* *Defense:* `safety: 6`, `doc: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.881
  * `Choke Point (Betweenness):` 0.006531 | `Ripple Effect (Closeness):` 0.084906
  * `Imports (Out-Degree: 2):` GuzzleHttp\BodySummarizerInterface, GuzzleHttp\BodySummarizer, Psr\Http\Client\RequestExceptionInterface, Psr\Http\Message\ResponseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Middleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.508 IQR)
- **Top Global Matches:** file_cluster_13: 12.508, file_cluster_8: 12.663, file_cluster_7: 12.878
- **Magnitude:** 106.38 | **LOC:** 269 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.1954%), Tech Debt (84.8229%)
**Top Internal Functions/Classes:**
  * `httpErrors` (Impact: 10.8)
  * `tap` (Impact: 9.5)
  * `log` (Impact: 9.3)
    * *Intent:* /** * Middleware that invokes a callback before and after sending a request. * * The provided listen...
  * `history` (Impact: 6.8)
  * `cookies` (Impact: 6.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 104`, `args: 33`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 38`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 8`, `doc: 30`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Cookie\CookieJarInterface, Psr\Log\LoggerInterface, GuzzleHttp\Promise, Psr\Http\Message\ResponseInterface, GuzzleHttp\Exception\RequestException, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Cookie/SetCookie.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.044 IQR)
- **Top Global Matches:** file_cluster_8: 13.044, file_cluster_17: 13.153, file_cluster_7: 13.298
- **Magnitude:** 102.66 | **LOC:** 493 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.0605%), Tech Debt (58.4411%)
**Top Internal Functions/Classes:**
  * `fromString` (Impact: 36.3)
  * `__construct` (Impact: 26.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`, `orphaned_logic: 2`
* *Architecture:* `api: 2`
* *Defense:* `safety: 12`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` an equal sign.
        if (!isset($pieces[0]) || \strpos($pieces[0], "
        return \substr($requestPath, 
    public function matchesPath(string $requestPath): bool
    
        $cookiePath = $this->getPath(, ', '=') === false) 
            return new self($data, \strlen($cookiePath)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ClientInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 99.07%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.639 IQR)
- **Top Global Matches:** file_cluster_13: 14.639, file_cluster_7: 15.403, file_cluster_8: 15.413
- **Magnitude:** 96.8 | **LOC:** 85 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.5529%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 6`, `import: 5`
* *Defense:* `safety: 1`, `doc: 22`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` a "handler"
     * (if utilized by the concrete client), GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Exception\GuzzleException, default request options of the client, Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface, 
    public function getConfig(?string $option = null, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Pool.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.808 IQR)
- **Top Global Matches:** file_cluster_4: 13.808, file_cluster_13: 13.824, file_cluster_8: 14.227
- **Magnitude:** 87.78 | **LOC:** 126 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.6287%), Tech Debt (80.3174%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 17.4)
    * *Intent:* /** * Sends an iterator of requests concurrently using a capped pool size. * * The pool will read fr...
  * `cmpCallback` (Impact: 6.7)
  * `batch` (Impact: 2.5)
  * `promise` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 27`, `args: 7`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 43`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 5`
* *Defense:* `safety: 4`, `doc: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise\EachPromise, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Promise\PromisorInterface, GuzzleHttp\Promise, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/TestLogger.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.578 IQR)
- **Top Global Matches:** file_cluster_8: 11.578, file_cluster_13: 11.859, file_cluster_11: 12.043
- **Magnitude:** 68.66 | **LOC:** 100 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.2694%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `hasRecord` (Impact: 9.5)
  * `hasRecordThatPasses` (Impact: 7.6)
  * `__call` (Impact: 7.6)
  * `log` (Impact: 2.5)
  * `hasRecordThatContains` (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 33`, `args: 11`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 22`, `orphaned_logic: 6`
* *Architecture:* `api: 10`, `import: 1`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Log\AbstractLogger
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/MessageFormatterInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.38 IQR)
- **Top Global Matches:** file_cluster_13: 14.38, file_cluster_8: 15.077, file_cluster_11: 15.199
- **Magnitude:** 67.73 | **LOC:** 19 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 5`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ClientTrait.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.655 IQR)
- **Top Global Matches:** file_cluster_13: 12.655, file_cluster_8: 12.897, file_cluster_7: 12.93
- **Magnitude:** 61.98 | **LOC:** 242 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.4699%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 1.9)
    * *Intent:* /** * Create and send an HTTP request.
  * `head` (Impact: 1.9)
    * *Intent:* /** * Create and send an HTTP request. * * Use an absolute path to override the base path of the cli...
  * `put` (Impact: 1.9)
  * `post` (Impact: 1.9)
    * *Intent:* /** * Create and send an HTTP GET request. * * Use an absolute path to override the base path of the...
  * `patch` (Impact: 1.9)
    * *Intent:* /** * Create and send an HTTP GET request. * * Use an absolute path to override the base path of the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* `api: 24`, `import: 4`
* *Defense:* `safety: 1`, `doc: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.028302
  * `Imports (Out-Degree: 1):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface, GuzzleHttp\Promise\PromiseInterface, GuzzleHttp\Exception\GuzzleException
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/TransferStats.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.92%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.64 IQR)
- **Top Global Matches:** file_cluster_13: 12.64, file_cluster_8: 12.813, file_cluster_7: 12.89
- **Magnitude:** 60.26 | **LOC:** 134 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5115%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 8.0)
    * *Intent:* /** * @var float|null */
  * `getHandlerStat` (Impact: 4.2)
    * *Intent:* /** * Gets handler specific error data.
  * `getResponse` (Impact: 3.7)
  * `getTransferTime` (Impact: 3.7)
  * `getRequest` (Impact: 1.9)
    * *Intent:* /** * @param RequestInterface $request Request that was sent.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 22`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 9`
* *Architecture:* `api: 9`, `import: 3`
* *Defense:* `safety: 1`, `doc: 28`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.508
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071032
  * `Imports (Out-Degree: 0):` Psr\Http\Message\ResponseInterface, Psr\Http\Message\UriInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Cookie/FileCookieJar.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.478 IQR)
- **Top Global Matches:** file_cluster_13: 12.478, file_cluster_8: 12.495, file_cluster_7: 12.59
- **Magnitude:** 56.64 | **LOC:** 102 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.9866%), Tech Debt (59.4986%)
**Top Internal Functions/Classes:**
  * `load` (Impact: 14.9)
    * *Intent:* /** * Saves the cookies to a file.
  * `save` (Impact: 8.8)
  * `__construct` (Impact: 4.0)
  * `__destruct` (Impact: 1.9)
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

### `src/RetryMiddleware.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.64 IQR)
- **Top Global Matches:** file_cluster_13: 11.64, file_cluster_8: 11.756, file_cluster_7: 11.973
- **Magnitude:** 50.74 | **LOC:** 120 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.2494%), Tech Debt (77.4054%)
**Top Internal Functions/Classes:**
  * `__construct` (Impact: 6.3)
  * `doRetry` (Impact: 4.3)
  * `__invoke` (Impact: 4.2)
    * *Intent:* /** * @param callable $decider Function that accepts the number of retries, * a request, [response],...
  * `onFulfilled` (Impact: 4.2)
    * *Intent:* /** * Default exponential backoff delay function.
  * `onRejected` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 26`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `orphaned_logic: 2`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 1`, `doc: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GuzzleHttp\Promise, GuzzleHttp\Promise\PromiseInterface, Psr\Http\Message\ResponseInterface, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/BodySummarizerInterface.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.549 IQR)
- **Top Global Matches:** file_cluster_8: 8.549, file_cluster_13: 8.715, file_cluster_7: 9.055
- **Magnitude:** 47.07 | **LOC:** 14 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 4`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.915
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.067385
  * `Imports (Out-Degree: 0):` Psr\Http\Message\MessageInterface
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Handler/EasyHandle.php` (PHP | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.107 IQR)
- **Top Global Matches:** file_cluster_13: 13.107, file_cluster_8: 13.614, file_cluster_7: 13.687
- **Magnitude:** 45.58 | **LOC:** 113 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.3401%), Tech Debt (93.0993%)
**Top Internal Functions/Classes:**
  * `createResponse` (Impact: 11.9)
  * `__get` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 11`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`, `orphaned_logic: 2`
* *Architecture:* `api: 11`, `import: 5`
* *Defense:* `safety: 3`, `doc: 25`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 12.641
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` GuzzleHttp\Utils, Psr\Http\Message\ResponseInterface, Psr\Http\Message\StreamInterface, GuzzleHttp\Psr7\Response, Psr\Http\Message\RequestInterface
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Dockerfile` (DOCKERFILE) | Magnitude: 44.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 3, import: 3, structural_boundaries: 2, class_start: 2
- `src/Cookie/FileCookieJar.php` (PHP) | Magnitude: 56.64 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, state_mutation: 22, doc: 18, structural_boundaries: 15
- `src/MessageFormatter.php` (PHP) | Magnitude: 249.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 122, state_mutation: 106, branch: 62, structural_boundaries: 16
- `src/Handler/CurlFactory.php` (PHP) | Magnitude: 378.42 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 356, state_mutation: 161, branch: 84, structural_boundaries: 70
- `src/Handler/Proxy.php` (PHP) | Magnitude: 10.0 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 12, doc: 9, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Pool.php` (PHP) | Magnitude: 87.78 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 43, structural_boundaries: 27, doc: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/HandlerStack.php` (PHP) | Magnitude: 205.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 135, state_mutation: 109, doc: 43, structural_boundaries: 39
- `tests/Server.php` (PHP) | Magnitude: 18.64 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 8, import: 4, doc: 3
- `src/RequestOptions.php` (PHP) | Magnitude: 39.58 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 25, immutability_locks: 25, api: 24, indent_spaces: 24
- `src/Handler/CurlFactoryInterface.php` (PHP) | Magnitude: 40.8 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, doc: 5, args: 2, func_start: 2
- `tests/server.js` (JAVASCRIPT) | Magnitude: 308.96 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, state_mutation: 60, branch: 57, structural_boundaries: 25

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Middleware.php` -> Churn: **100.0%** | Cog Load: 18.1954% | Debt: 84.8229%
- `src/Cookie/CookieJar.php` -> Churn: **63.09%** | Cog Load: 38.1185% | Debt: 85.6401%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Handler/CurlFactory.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 378.42
- `src/Cookie/CookieJar.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 220.4
- `src/Handler/CurlMultiHandler.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 163.06
- `src/RedirectMiddleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 133.48
- `src/Middleware.php` -> **Graham Campbell** (100.0% isolated ownership) | Magnitude: 106.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Utils.php` -> **Severity: 2.213** (Bridge: 0.0221 * Flux: 99.9999%)
- `src/Handler/StreamHandler.php` -> **Severity: 0.943** (Bridge: 0.0094 * Flux: 99.9999%)
- `src/Exception/RequestException.php` -> **Severity: 0.653** (Bridge: 0.0065 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Utils.php` -> **Severity: 10.503** (Embedded: 0.1321 * Error Risk: 79.5248%)
- `src/Exception/RequestException.php` -> **Severity: 7.691** (Embedded: 0.0849 * Error Risk: 90.5794%)
- `src/Handler/CurlMultiHandler.php` -> **Severity: 5.718** (Embedded: 0.0711 * Error Risk: 80.4067%)
- `src/Handler/CurlHandler.php` -> **Severity: 5.677** (Embedded: 0.0805 * Error Risk: 70.5181%)
- `src/BodySummarizer.php` -> **Severity: 5.508** (Embedded: 0.0674 * Error Risk: 81.7332%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/RequestOptions.php` -> **Severity: 3002.807** (Blast Radius: 34.618 * Doc Risk: 86.7412%)
- `src/BodySummarizer.php` -> **Severity: 1307.482** (Blast Radius: 24.915 * Doc Risk: 52.4777%)
- `src/Utils.php` -> **Severity: 926.446** (Blast Radius: 77.72 * Doc Risk: 11.9203%)
- `src/Exception/BadResponseException.php` -> **Severity: 915.54** (Blast Radius: 18.014 * Doc Risk: 50.8238%)
- `src/Exception/GuzzleException.php` -> **Severity: 725.531** (Blast Radius: 46.915 * Doc Risk: 15.4648%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
