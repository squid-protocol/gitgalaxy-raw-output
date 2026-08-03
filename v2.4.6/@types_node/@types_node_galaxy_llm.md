# ARCHITECTURAL_BRIEF: @types_node
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/npm_top_200/@types_node` |
| **Timestamp** | `2026-08-03T21:10:46.199027+00:00` |
| **Scan Duration** | `0.63s` |
| **Git Branch** | `N/A` |
| **Git Commit** | `N/A` |
| **Git Remote** | `N/A` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 78 malicious artifacts.

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
| Total Artifacts | 88 |
| Analyzed Artifacts (Scanned) | 80 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 7196 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 90.9% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 78 | 7196 | 97.5% |
| MARKDOWN | 1 | 0 | 1.2% |
| PLAINTEXT | 1 | 0 | 1.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.332`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 30 | 37.5% |
| file_cluster_16 | 25 | 31.2% |
| file_cluster_13 | 14 | 17.5% |
| file_cluster_2 | 6 | 7.5% |
| file_cluster_6 | 1 | 1.2% |
| file_cluster_1 | 1 | 1.2% |
| file_cluster_0 | 1 | 1.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `.ts`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4066 LOC), 1x Excluded (Machine-Generated Source Code Signature: 151 LOC)
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 76.8 | 16.3 | 5.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.0 | 22.3 | 12.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 42.8 | 24.3 | 0.0 |
| Testing Exposure | 0.2 | 80.0 | 12.1 | 2.3 | 80.0 |
| API Exposure | 0.0 | 9.6 | 3.2 | 2.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 25.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 23.1 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.5 | 100.0 | 100.0 |
| Instability Exposure | 50.0 | 50.0 | 50.0 | 50.0 | 50.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 97.9 | 20.8 | 11.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 20.0 | 1.9 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 18.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 91.7 | 1.2 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `node/https.d.ts` (Hits: 47)
- `node/process.d.ts` (Hits: 35)
- `node/cluster.d.ts` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **README.md** (`node/README.md`) — 0 inbound connections
2. **assert.d.ts** (`node/assert.d.ts`) — 0 inbound connections
3. **strict.d.ts** (`node/assert/strict.d.ts`) — 0 inbound connections
4. **async_hooks.d.ts** (`node/async_hooks.d.ts`) — 0 inbound connections
5. **buffer.buffer.d.ts** (`node/buffer.buffer.d.ts`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **process.d.ts** (`node/process.d.ts`) — 111 outbound dependencies
2. **worker_threads.d.ts** (`node/worker_threads.d.ts`) — 13 outbound dependencies
3. **child_process.d.ts** (`node/child_process.d.ts`) — 10 outbound dependencies
4. **stream.d.ts** (`node/stream.d.ts`) — 10 outbound dependencies
5. **promises.d.ts** (`node/fs/promises.d.ts`) — 9 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `assert` (@ `node/assert.d.ts`) -> Impact: **300.8** | LOC: 127
  * *Intent:* /** * The `node:assert` module provides a set of assertion functions for verifying * invariants. * @see [source](https://github.com/nodejs/node/blob/v...
- `oncreate` (@ `node/http.d.ts`) -> Impact: **145.1** | LOC: 131
- `removeListener` (@ `node/http2.d.ts`) -> Impact: **144.8** | LOC: 124
- `isWritable` (@ `node/stream.d.ts`) -> Impact: **93.6** | LOC: 34
  * *Intent:* * } * } * * const wordsStream = Readable.from(['text passed through', 'composed stream']).compose(splitToWords); * const words = await wordsStream.toA...
- `callback` (@ `node/tls.d.ts`) -> Impact: **85.4** | LOC: 45
  * *Intent:* /** * The name property is available only when type is 'ECDH'.
- `triggerAsyncId` (@ `node/async_hooks.d.ts`) -> Impact: **43.0** | LOC: 29
  * *Intent:* /** * We strongly discourage the use of the `async_hooks` API. * Other APIs that can cover most of its use cases include: * * * [`AsyncLocalStorage`](...
- `callback` (@ `node/readline.d.ts`) -> Impact: **37.8** | LOC: 29
- `removeEventListener` (@ `node/web-globals/events.d.ts`) -> Impact: **33.2** | LOC: 37
- `exit` (@ `node/process.d.ts`) -> Impact: **32.3** | LOC: 11
- `duplexPair` (@ `node/stream.d.ts`) -> Impact: **30.4** | LOC: 8
  * *Intent:* /** * The `readable.setEncoding()` method sets the character encoding for * data read from the `Readable` stream. *

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `exit` (@ `node/process.d.ts`) -> **O(2^N) [Recursive]**
- `assert` (@ `node/assert.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * The `node:assert` module provides a set of assertion functions for verifying * invariants. * @see [source](https://github.com/nodejs/node/blob/v...
- `error` (@ `node/diagnostics_channel.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Register a message handler to subscribe to this channel. This message handler
- `strict` (@ `node/assert/strict.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* * ```js * import { strict as assert } from 'node:assert'; * ``` * * ```js * import assert from 'node:assert/strict'; * ``` * * Example error diff: * *...
- `triggerAsyncId` (@ `node/async_hooks.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * We strongly discourage the use of the `async_hooks` API. * Other APIs that can cover most of its use cases include: * * * [`AsyncLocalStorage`](...
- `removeListener` (@ `node/http2.d.ts`) -> **O(2^N) [Recursive]**
- `callback` (@ `node/tls.d.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * The name property is available only when type is 'ECDH'.
- `inspect` (@ `node/util.d.ts`) -> **O(2^N) [Recursive]**
- `abort` (@ `node/web-globals/abortcontroller.d.ts`) -> **O(2^N) [Recursive]**
- `readFile` (@ `node/fs/promises.d.ts`) -> **O(N^5)**
  * *Intent:* * * If the `FileHandle` points to a character device that only supports blocking * reads (such as keyboard or sound card), read operations do not fini...

### Highest Data Gravity (Database Complexity)
- `getName` (@ `node/https.d.ts`) -> DB Complexity: **15**
  * *Intent:* /** * An `Agent` object for HTTPS similar to `http.Agent`. See {@link request} for more information. * * Like `http.Agent`, the `createConnection(opti...
- `removeListener` (@ `node/https.d.ts`) -> DB Complexity: **15**
- `get` (@ `node/https.d.ts`) -> DB Complexity: **13**
  * *Intent:* /** * ```js * // curl -k https://localhost:8000/ * import https from 'node:https'; * import fs from 'node:fs';
- `setItem` (@ `node/web-globals/storage.d.ts`) -> DB Complexity: **9**
- `setGlobalProxyFromEnv` (@ `node/http.d.ts`) -> DB Complexity: **7**
  * *Intent:* /** * Returns an array containing the unique names of the current outgoing headers. * All names are lowercase. * @since v7.7.0
- `wrap` (@ `node/module.d.ts`) -> DB Complexity: **7**
  * *Intent:* /** * If you want to resolve `specifier` relative to a
- `execFileSync` (@ `node/child_process.d.ts`) -> DB Complexity: **6**
  * *Intent:* * import { spawn } from 'node:child_process'; * import { once } from 'node:events'; * const ls = spawn('ls', ['-lh', '/usr']); * * ls.stdout.on('data'...
- `globSync` (@ `node/fs.d.ts`) -> DB Complexity: **6**
  * *Intent:* * size: 527n, * blksize: 4096n, * blocks: 8n, * atimeMs: 1318289051000n, * mtimeMs: 1318289051000n, * ctimeMs: 1318289051000n, * birthtimeMs: 13182890...
- `glob` (@ `node/fs/promises.d.ts`) -> DB Complexity: **6**
  * *Intent:* /** * Forces all currently queued I/O operations associated with the file to the * operating system's synchronized I/O completion state. Refer to the ...
- `callback` (@ `node/tls.d.ts`) -> DB Complexity: **4**
  * *Intent:* /** * The name property is available only when type is 'ECDH'.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `node` | 45 | 249.97 | 7.46% | 49.22% |
| `node/ts5.7/compatibility` | 1 | 164.31 | 23.02% | 0.0% |
| `node/ts5.6/compatibility` | 1 | 157.8 | 23.5% | 0.0% |
| `node/web-globals` | 16 | 58.1 | 46.63% | 24.79% |
| `node/stream` | 3 | 18.99 | 27.69% | 71.28% |
| `node/fs` | 1 | 8.83 | 8.89% | 100.0% |
| `node/ts5.6` | 3 | 8.19 | 3.01% | 0.0% |
| `node/dns` | 1 | 3.31 | 8.41% | 23.75% |
| `node/path` | 2 | 3.24 | 5.0% | 0.0% |
| `node/timers` | 1 | 2.67 | 5.0% | 99.05% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `node/web-globals/timers.d.ts` -> **99.9999%** Exposure
- `node/fs/promises.d.ts` -> **99.9965%** Exposure
- `node/console.d.ts` -> **99.9447%** Exposure
- `node/stream/consumers.d.ts` -> **99.708%** Exposure
- `node/inspector/promises.d.ts` -> **99.4472%** Exposure
### Highest State Flux (Mutation/Volatility)
- `node/web-globals/encoding.d.ts` -> **100.0%** Exposure
- `node/web-globals/fetch.d.ts` -> **100.0%** Exposure
- `node/web-globals/messaging.d.ts` -> **100.0%** Exposure
- `node/web-globals/performance.d.ts` -> **100.0%** Exposure
- `node/web-globals/storage.d.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `node/stream.d.ts` -> **5** Orphaned Functions | **4** Duplicates
- `node/stream/web.d.ts` -> **4** Orphaned Functions | **5** Duplicates
- `node/module.d.ts` -> **8** Orphaned Functions | **0** Duplicates
- `node/fs/promises.d.ts` -> **1** Orphaned Functions | **6** Duplicates
- `node/http.d.ts` -> **3** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`node/child_process.d.ts`** -> AI Confidence: **99.31%**
2. **`node/fs/promises.d.ts`** -> AI Confidence: **99.31%**
3. **`node/http.d.ts`** -> AI Confidence: **99.31%**
4. **`node/cluster.d.ts`** -> AI Confidence: **99.23%**
5. **`node/vm.d.ts`** -> AI Confidence: **99.23%**
6. **`node/http2.d.ts`** -> AI Confidence: **99.18%**
7. **`node/stream.d.ts`** -> AI Confidence: **99.18%**
8. **`node/v8.d.ts`** -> AI Confidence: **99.18%**
9. **`node/worker_threads.d.ts`** -> AI Confidence: **99.16%**
10. **`node/dgram.d.ts`** -> AI Confidence: **99.13%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `node/assert.d.ts` -> **100.0%** Exposure
- `node/fs/promises.d.ts` -> **100.0%** Exposure
- `node/http.d.ts` -> **100.0%** Exposure
- `node/module.d.ts` -> **100.0%** Exposure
- `node/process.d.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `node/dns.d.ts` -> **100.0%** Exposure
- `node/dns/promises.d.ts` -> **37.6669%** Exposure
- `node/url.d.ts` -> **0.0004%** Exposure
### Hardcoded Payload Artifacts
- `node/tls.d.ts` -> **91.7239%** Exposure
### Algorithmic DoS Exposure
- `node/fs/promises.d.ts` -> **100.0%** Exposure
- `node/https.d.ts` -> **100.0%** Exposure
- `node/module.d.ts` -> **100.0%** Exposure
- `node/web-globals/storage.d.ts` -> **99.9213%** Exposure
- `node/child_process.d.ts` -> **99.8356%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `344` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `node/stream/web.d.ts` (TYPESCRIPT) -> Cumulative Risk: **769.82**
- **Archetype:** `file_cluster_16` (Distance: 12.69 IQR)
- **Magnitude:** 15.6 | **LOC:** 297 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (99.9992%), Tech Debt (95.5821%)
- **Heaviest Functions:** `values` (Impact: 24.8), `cancel` (Impact: 8.0), `getWriter` (Impact: 6.7)

### 2. `node/fs/promises.d.ts` (TYPESCRIPT) -> Cumulative Risk: **652.73**
- **Archetype:** `file_cluster_8` (Distance: 10.437 IQR)
- **Magnitude:** 8.83 | **LOC:** 1330 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `write` (Impact: 13.8), `opendir` (Impact: 10.6), `readFile` (Impact: 10.3)

### 3. `node/web-globals/crypto.d.ts` (TYPESCRIPT) -> Cumulative Risk: **649.38**
- **Archetype:** `file_cluster_16` (Distance: 11.023 IQR)
- **Magnitude:** 1.66 | **LOC:** 40 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.994%), Documentation (97.9286%), Logic Bomb (90.5737%)
- **Heaviest Functions:** `supports` (Impact: 4.9)

### 4. `node/module.d.ts` (TYPESCRIPT) -> Cumulative Risk: **642.72**
- **Archetype:** `file_cluster_16` (Distance: 11.38 IQR)
- **Magnitude:** 14.22 | **LOC:** 758 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (97.4164%)
- **Heaviest Functions:** `wrap` (Impact: 18.6), `isBuiltin` (Impact: 16.4), `registerHooks` (Impact: 16.4)

### 5. `node/util.d.ts` (TYPESCRIPT) -> Cumulative Risk: **603.51**
- **Archetype:** `file_cluster_16` (Distance: 11.02 IQR)
- **Magnitude:** 11.96 | **LOC:** 1688 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (99.9989%), Algorithmic Dos (99.8238%), Verification (80.0%)
- **Heaviest Functions:** `parseArgs` (Impact: 22.7), `decode` (Impact: 13.3), `inspect` (Impact: 10.8)

### 6. `node/web-globals/storage.d.ts` (TYPESCRIPT) -> Cumulative Risk: **594.86**
- **Archetype:** `file_cluster_16` (Distance: 13.535 IQR)
- **Magnitude:** 1.63 | **LOC:** 25 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9213%), Tech Debt (92.4142%)
- **Heaviest Functions:** `setItem` (Impact: 5.9)

### 7. `node/dns.d.ts` (TYPESCRIPT) -> Cumulative Risk: **570.21**
- **Archetype:** `file_cluster_8` (Distance: 11.72 IQR)
- **Magnitude:** 4.63 | **LOC:** 923 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.9999%), Tech Debt (91.0235%)
- **Heaviest Functions:** `setDefaultResultOrder` (Impact: 18.7), `setLocalAddress` (Impact: 8.1), `callback` (Impact: 6.3)

### 8. `node/web-globals/messaging.d.ts` (TYPESCRIPT) -> Cumulative Risk: **563.45**
- **Archetype:** `file_cluster_16` (Distance: 12.515 IQR)
- **Magnitude:** 1.39 | **LOC:** 24 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.7148%), Safety Score (80.0%)
- **Heaviest Functions:** `structuredClone` (Impact: 3.6)

### 9. `node/web-globals/fetch.d.ts` (TYPESCRIPT) -> Cumulative Risk: **544.92**
- **Archetype:** `file_cluster_16` (Distance: 11.867 IQR)
- **Magnitude:** 3.63 | **LOC:** 70 | **CtrlFlow:** 23.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (80.0%), Cognitive Load (76.8217%)
- **Heaviest Functions:** `fetch` (Impact: 6.3)

### 10. `node/tls.d.ts` (TYPESCRIPT) -> Cumulative Risk: **539.74**
- **Archetype:** `file_cluster_13` (Distance: 12.639 IQR)
- **Magnitude:** 11.09 | **LOC:** 1204 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Secrets Risk (91.7239%), Verification (80.0%)
- **Heaviest Functions:** `callback` (Impact: 85.4), `disableRenegotiation` (Impact: 17.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.046 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.796 IQR)
- **Top Global Matches:** file_cluster_2: 12.046, file_cluster_8: 12.114, file_cluster_16: 12.138
- **Magnitude:** 164.31 | **LOC:** 73 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.0191%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 21`, `args: 37`, `func_start: 44`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/ts5.6/compatibility/float16array.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.747 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 4.515 IQR)
- **Top Global Matches:** file_cluster_8: 11.747, file_cluster_16: 11.976, file_cluster_17: 12.16
- **Magnitude:** 157.8 | **LOC:** 72 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (23.4984%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 21`, `args: 34`, `func_start: 42`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`
* *Architecture:* None
* *Defense:* `safety: 8`, `doc: 1`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/assert.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.744 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.727 IQR)
- **Top Global Matches:** file_cluster_8: 14.744, file_cluster_16: 14.767, file_cluster_4: 14.777
- **Magnitude:** 32.09 | **LOC:** 956 | **CtrlFlow:** 50.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.3222%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `assert` (Impact: 300.8 | O(2^N) | DB: 1)
    * *Intent:* /** * The `node:assert` module provides a set of assertion functions for verifying * invariants. * @...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 32`, `args: 28`, `func_start: 27`, `class_start: 5`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `concurrency: 12`, `import: 2`
* *Defense:* `safety: 62`, `doc: 39`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:assert, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.554 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.479 IQR)
- **Top Global Matches:** file_cluster_16: 12.554, file_cluster_2: 12.997, file_cluster_13: 13.054
- **Magnitude:** 23.0 | **LOC:** 1794 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.0756%), Tech Debt (94.0183%)
**Top Internal Functions/Classes:**
  * `isWritable` (Impact: 93.6 | O(N^4) | DB: 1)
    * *Intent:* * } * } * * const wordsStream = Readable.from(['text passed through', 'composed stream']).compose(sp...
  * `duplexPair` (Impact: 30.4 | O(N^4))
    * *Intent:* /** * The `readable.setEncoding()` method sets the character encoding for * data read from the `Read...
  * `removeListener` (Impact: 24.8 | O(N^3))
    * *Intent:* /** * Is `true` after `'close'` has been emitted. * @since v18.0.0
  * `_write` (Impact: 18.3 | O(N^5))
    * *Intent:* /** * A utility method for creating a `Readable` from a web `ReadableStream`. * @since v17.0.0 */
  * `setDefaultHighWaterMark` (Impact: 14.2 | O(N^3))
    * *Intent:* /** * The `readable.pause()` method will cause a stream in flowing mode to stop
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 253`, `args: 122`, `func_start: 128`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 3`, `planned_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 5`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 92`, `doc: 86`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web, promises, node:stream, node:http, node:string_decoder, node:fs, node:events, node:zlib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.057 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.18 IQR)
- **Top Global Matches:** file_cluster_16: 13.057, file_cluster_2: 13.204, file_cluster_8: 13.206
- **Magnitude:** 22.55 | **LOC:** 2189 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (10.1351%), Tech Debt (32.3386%)
**Top Internal Functions/Classes:**
  * `oncreate` (Impact: 145.1 | O(N^3) | DB: 3)
  * `removeListener` (Impact: 25.6 | O(N^3))
  * `removeListener` (Impact: 18.7 | O(N^2))
    * *Intent:* /** * Reference to the underlying socket. Usually, users will not want to access * this property. * ...
  * `getName` (Impact: 5.5 | O(N^2))
    * *Intent:* /** * Append a single header value to the header object. * * If the value is an array, this is equiv...
  * `setGlobalProxyFromEnv` (Impact: 4.8 | O(N^1) | DB: 7)
    * *Intent:* /** * Returns an array containing the unique names of the current outgoing headers. * All names are ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 200`, `args: 145`, `func_start: 172`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 3`, `duplicate_logic: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 9`, `api: 4`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 115`, `doc: 140`, `immutability_locks: 17`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` undici-types, node:url, node:stream, node:http, node:events, node:buffer, node:net, node:dns
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/http2.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.459 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.704 IQR)
- **Top Global Matches:** file_cluster_16: 12.459, file_cluster_8: 12.487, file_cluster_13: 12.592
- **Magnitude:** 19.05 | **LOC:** 2481 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (3.4839%), Tech Debt (16.2344%)
**Top Internal Functions/Classes:**
  * `removeListener` (Impact: 144.8 | O(2^N) | DB: 3)
  * `connect` (Impact: 14.4 | O(N^2) | DB: 3)
  * `removeListener` (Impact: 5.6 | O(N^2) | DB: 1)
    * *Intent:* /** * Provides miscellaneous information about the current state of the `Http2Stream`. * * A current...
  * `callback` (Impact: 5.1 | O(N^2))
    * *Intent:* * * Initiates a response. When the `options.waitForTrailers` option is set, the `'wantTrailers'` eve...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 172`, `args: 118`, `func_start: 138`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 3`, `duplicate_logic: 2`
* *Architecture:* `io: 7`, `api: 2`, `concurrency: 4`, `import: 10`
* *Defense:* `safety: 104`, `doc: 103`, `immutability_locks: 253`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:url, node:stream, node:http, node:tls, node:fs, node:events, node:buffer, node:net...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/stream/web.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.69 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.758 IQR)
- **Top Global Matches:** file_cluster_16: 12.69, file_cluster_4: 12.799, file_cluster_8: 12.989
- **Magnitude:** 15.6 | **LOC:** 297 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (72.3434%), Tech Debt (95.5821%)
**Top Internal Functions/Classes:**
  * `values` (Impact: 24.8 | O(N^3) | DB: 1)
  * `cancel` (Impact: 8.0 | O(N^2))
  * `getWriter` (Impact: 6.7 | O(N^2) | DB: 1)
  * `error` (Impact: 5.5 | O(N^2) | DB: 1)
  * `error` (Impact: 5.5 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 92`, `args: 47`, `func_start: 33`, `class_start: 45`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 31`, `duplicate_logic: 5`, `orphaned_logic: 4`
* *Architecture:* `api: 1`, `concurrency: 48`, `import: 2`
* *Defense:* `safety: 45`, `immutability_locks: 28`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util, web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/module.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.38 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.071 IQR)
- **Top Global Matches:** file_cluster_16: 11.38, file_cluster_2: 11.399, file_cluster_8: 11.477
- **Magnitude:** 14.22 | **LOC:** 758 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (6.0886%), Tech Debt (97.4164%)
**Top Internal Functions/Classes:**
  * `wrap` (Impact: 18.6 | O(N^4) | DB: 7)
    * *Intent:* /** * If you want to resolve `specifier` relative to a
  * `isBuiltin` (Impact: 16.4 | O(N^3))
    * *Intent:* /** * @since v12.2.0 * @param path Filename to be used to construct the require * function. Must be ...
  * `registerHooks` (Impact: 16.4 | O(N^3))
    * *Intent:* /** * Node.js fails to enable the compile cache. This can be caused by the lack of * permission to u...
  * `register` (Impact: 14.2 | O(N^3))
    * *Intent:* /**
  * `findSourceMap` (Impact: 12.3 | O(N^3) | DB: 3)
    * *Intent:* /** * ```text * /path/to/project * ├ packages/ * ├ bar/ * ├ bar.js
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 83`, `args: 28`, `func_start: 23`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 6`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `io: 2`, `api: 3`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 8`, `doc: 82`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:module, node:assert, node:url, node:fs
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/blob.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.371 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.27 IQR)
- **Top Global Matches:** file_cluster_16: 11.371, file_cluster_13: 11.762, file_cluster_8: 11.998
- **Magnitude:** 13.66 | **LOC:** 24 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (69.4938%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 23`, `args: 2`, `func_start: 2`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/util.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.02 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.775 IQR)
- **Top Global Matches:** file_cluster_16: 11.02, file_cluster_8: 11.409, file_cluster_13: 11.475
- **Magnitude:** 11.96 | **LOC:** 1688 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (6.659%), Tech Debt (70.9934%)
**Top Internal Functions/Classes:**
  * `parseArgs` (Impact: 22.7 | O(N^2))
    * *Intent:* /** * If `true`, `Proxy` inspection includes the target and handler objects. * @default false
  * `decode` (Impact: 13.3 | O(N^2) | DB: 1)
    * *Intent:* /** * The `util.format()` method returns a formatted string using the first argument * as a `printf`...
  * `inspect` (Impact: 10.8 | O(2^N) | DB: 4)
  * `styleText` (Impact: 7.1 | O(N^2))
    * *Intent:* /** * If `true`, the output is styled with ANSI color codes. Colors are customizable.
  * `values` (Impact: 4.6 | O(N^2))
    * *Intent:* * // [-1, '!'], * // ] * // Comparing arrays * const actualArray = ['1', '2', '3']; * const expected...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 121`, `args: 17`, `func_start: 13`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `api: 35`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 17`, `doc: 34`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:util, node:fs, node:events, types, node:assert, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/tls.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.639 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.627 IQR)
- **Top Global Matches:** file_cluster_13: 12.639, file_cluster_8: 12.657, file_cluster_16: 12.754
- **Magnitude:** 11.09 | **LOC:** 1204 | **CtrlFlow:** 50.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (8.6088%), Tech Debt (43.0999%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 85.4 | O(2^N) | DB: 4)
    * *Intent:* /** * The name property is available only when type is 'ECDH'.
  * `disableRenegotiation` (Impact: 17.8 | O(N^2))
    * *Intent:* /** * The issuer certificate object. * For self-signed certificates, this may be a circular referenc...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 46`, `args: 30`, `func_start: 25`, `class_start: 13`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 15`, `doc: 86`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:tls, node:crypto, node:fs, node:buffer, node:net, stream
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/net.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.897 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 5.965 IQR)
- **Top Global Matches:** file_cluster_8: 13.897, file_cluster_16: 13.911, file_cluster_13: 13.938
- **Magnitude:** 9.03 | **LOC:** 953 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.8724%), Tech Debt (78.8108%)
**Top Internal Functions/Classes:**
  * `removeListener` (Impact: 26.7 | O(N^2) | DB: 3)
    * *Intent:* /** * Pauses the reading of data. That is, `'data'` events will not be emitted. * Useful to throttle...
  * `callback` (Impact: 24.1 | O(N^2))
  * `isIPv6` (Impact: 15.6 | O(N^2))
  * `callback` (Impact: 6.3 | O(N^2))
    * *Intent:* /** * > Stability: 2 - Stable * * The `node:net` module provides an asynchronous network API for cre...
  * `toJSON` (Impact: 4.5 | O(N^2))
    * *Intent:* /** * Opposite of `unref()`, calling `ref()` on a previously `unref`ed socket will _not_ let the pro...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 109`, `args: 86`, `func_start: 88`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 13`, `duplicate_logic: 2`, `orphaned_logic: 4`
* *Architecture:* `io: 7`, `api: 1`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 66`, `doc: 107`, `immutability_locks: 23`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:stream, node:events, node:buffer, node:net, node:dns
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/fs/promises.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.437 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.469 IQR)
- **Top Global Matches:** file_cluster_8: 10.437, file_cluster_13: 10.65, file_cluster_16: 10.659
- **Magnitude:** 8.83 | **LOC:** 1330 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (8.89%), Tech Debt (99.9965%)
**Top Internal Functions/Classes:**
  * `write` (Impact: 13.8 | O(N^3))
    * *Intent:* /** * Modifies the permissions on the file. See [`chmod(2)`](http://man7.org/linux/man-pages/man2/ch...
  * `opendir` (Impact: 10.6 | O(N^2) | DB: 3)
    * *Intent:* * const stream = fd.createReadStream(); * setTimeout(() => { * stream.close(); // This may not close...
  * `readFile` (Impact: 10.3 | O(N^4) | DB: 3)
    * *Intent:* /** * Unlike the 16 KiB default `highWaterMark` for a `stream.Readable`, the stream * returned by th...
  * `write` (Impact: 10.2 | O(N^3))
    * *Intent:* /** * Changes the ownership of the file. A wrapper for [`chown(2)`](http://man7.org/linux/man-pages/...
  * `readFile` (Impact: 9.4 | O(N^5) | DB: 3)
    * *Intent:* * * If the `FileHandle` points to a character device that only supports blocking * reads (such as ke...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 31`, `args: 20`, `func_start: 22`, `class_start: 11`
* *Risk/State:* `planned_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 1`
* *Architecture:* `io: 8`, `api: 1`, `concurrency: 12`, `import: 7`
* *Defense:* `safety: 5`, `doc: 43`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web, node:stream, node:fs, node:events, promises, node:os, node:path, node:buffer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/buffer.buffer.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.387 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.772 IQR)
- **Top Global Matches:** file_cluster_2: 11.387, file_cluster_16: 11.551, file_cluster_8: 12.155
- **Magnitude:** 7.38 | **LOC:** 467 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 9`, `args: 4`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/diagnostics_channel.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.2 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.37 IQR)
- **Top Global Matches:** file_cluster_2: 13.2, file_cluster_16: 13.309, file_cluster_13: 13.613
- **Magnitude:** 6.91 | **LOC:** 577 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.7464%), Tech Debt (19.0407%)
**Top Internal Functions/Classes:**
  * `tracingChannel` (Impact: 21.1 | O(N^3))
    * *Intent:* /** * The `node:diagnostics_channel` module provides an API to create named channels * to report arb...
  * `fn` (Impact: 14.5 | O(N^3))
    * *Intent:* /** * Creates a `TracingChannel` wrapper for the given `TracingChannel Channels`. If a name is given...
  * `end` (Impact: 7.8 | O(N^4))
  * `asyncStart` (Impact: 7.8 | O(N^4))
    * *Intent:* /** * This is the primary entry-point for anyone wanting to publish to a named * channel. It produce...
  * `asyncEnd` (Impact: 7.8 | O(N^4))
    * *Intent:* /** * This is the primary entry-point for anyone wanting to publish to a named * channel. It produce...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 23`, `func_start: 26`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `orphaned_logic: 1`
* *Architecture:* `api: 1`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 26`, `doc: 63`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:diagnostics_channel, node:async_hooks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/streams.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.496 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.523 IQR)
- **Top Global Matches:** file_cluster_16: 11.496, file_cluster_8: 12.168, file_cluster_11: 12.328
- **Magnitude:** 6.89 | **LOC:** 116 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (69.1574%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 109`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 51`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` web
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/worker_threads.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.349 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.202 IQR)
- **Top Global Matches:** file_cluster_13: 13.349, file_cluster_2: 13.573, file_cluster_16: 13.574
- **Magnitude:** 6.01 | **LOC:** 718 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (14.015%), Tech Debt (18.1115%)
**Top Internal Functions/Classes:**
  * `removeEventListener` (Impact: 9.4 | O(N^3) | DB: 1)
    * *Intent:* * * The `import { isMainThread } from 'node:worker_threads'` variable is set to `false`. * * The `im...
  * `postMessageToThread` (Impact: 8.3 | O(N^2))
  * `removeListener` (Impact: 5.5 | O(N^2) | DB: 1)
    * *Intent:* /**
  * `startHeapProfile` (Impact: 2.4 | O(N^2))
  * `request` (Impact: 2.0 | O(N^2))
    * *Intent:* * a built-in pair of `MessagePort` s that are already associated with each * other when the `Worker`...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 80`, `args: 61`, `func_start: 64`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 10`, `planned_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 16`, `import: 10`
* *Defense:* `safety: 49`, `doc: 39`, `sync_locks: 3`, `immutability_locks: 15`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:v8, node:vm, some-js-parsing-library, web, node:url, undici-types, node:stream, promises...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/readline.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.377 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.884 IQR)
- **Top Global Matches:** file_cluster_13: 12.377, file_cluster_8: 12.472, file_cluster_7: 12.629
- **Magnitude:** 5.7 | **LOC:** 543 | **CtrlFlow:** 52.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.749%), Tech Debt (97.5313%)
**Top Internal Functions/Classes:**
  * `callback` (Impact: 37.8 | O(N^2))
  * `emitKeypressEvents` (Impact: 5.5 | O(N^2))
    * *Intent:* /** * The current input data being processed by node. * * This can be used when collecting input fro...
  * `moveCursor` (Impact: 4.7 | O(N^1))
    * *Intent:* * being emitted. Once the `line` event has been emitted, this property will * be an empty string. * ...
  * `getCursorPos` (Impact: 2.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 29`, `args: 17`, `func_start: 16`, `class_start: 6`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 11`, `doc: 41`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises, node:fs, node:events, node:readline, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/process.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.224 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.299 IQR)
- **Top Global Matches:** file_cluster_13: 12.224, file_cluster_8: 12.796, file_cluster_16: 12.946
- **Magnitude:** 5.6 | **LOC:** 2176 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.6365%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `exit` (Impact: 32.3 | O(2^N))
  * `removeListener` (Impact: 4.0 | O(N^3))
    * *Intent:* /** * @deprecated Global listener types will be removed in a future version. * Callbacks passed dire...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 203`, `args: 58`, `func_start: 51`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 1`
* *Architecture:* `io: 35`, `api: 3`, `concurrency: 9`, `import: 116`
* *Defense:* `safety: 47`, `doc: 81`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` domain, node:https, crypto, node:trace_events, strict, promises, consumers, tty...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/cluster.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.304 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 7.384 IQR)
- **Top Global Matches:** file_cluster_13: 13.304, file_cluster_4: 13.349, file_cluster_11: 13.587
- **Magnitude:** 5.59 | **LOC:** 487 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (34.604%), Tech Debt (95.6769%)
**Top Internal Functions/Classes:**
  * `isConnected` (Impact: 17.9 | O(N^3))
    * *Intent:* * const numCPUs = availableParallelism(); * * if (cluster.isPrimary) { * console.log(`Primary ${proc...
  * `setupPrimary` (Impact: 14.7 | O(N^3) | DB: 1)
    * *Intent:* /** * All workers are created using [`child_process.fork()`](https://nodejs.org/docs/latest-v25.x/ap...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 21`, `args: 13`, `func_start: 12`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 3`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 10`, `api: 2`, `concurrency: 17`, `import: 3`
* *Defense:* `safety: 9`, `doc: 30`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:child_process, node:http, node:events, node:cluster, node:os, node:net, node:process
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/sqlite.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.272 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.472 IQR)
- **Top Global Matches:** file_cluster_8: 12.272, file_cluster_16: 12.401, file_cluster_7: 12.471
- **Magnitude:** 5.53 | **LOC:** 1066 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (4.1348%), Tech Debt (82.9793%)
**Top Internal Functions/Classes:**
  * `step` (Impact: 19.0 | O(N^2))
    * *Intent:* /** * If `true`, the database is opened by the constructor. When * this value is `false`, the databa...
  * `setReadBigInts` (Impact: 13.7 | O(N^2))
    * *Intent:* /** * The function to call for each row in the aggregation. The * function receives the current stat...
  * `backup` (Impact: 8.9 | O(N^2) | DB: 3)
    * *Intent:* /** * If `true`, integer fields are read as `BigInt`s.
  * `applyChangeset` (Impact: 5.9 | O(N^2))
    * *Intent:* /** * If `true`, unknown named parameters are ignored when binding. * If `false`, an exception is th...
  * `clear` (Impact: 2.8 | O(N^2) | DB: 3)
    * *Intent:* /** * A function that determines how to handle conflicts. The function receives one argument, * whic...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 35`, `args: 46`, `func_start: 40`, `class_start: 14`
* *Risk/State:* `planned_debt: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 7`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 20`, `doc: 152`, `immutability_locks: 51`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sqlite, node:fs, node:sqlite
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/ts5.6/buffer.buffer.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.82%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.148 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.115 IQR)
- **Top Global Matches:** file_cluster_8: 11.148, file_cluster_2: 11.151, file_cluster_7: 11.327
- **Magnitude:** 5.47 | **LOC:** 463 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 4`, `args: 5`, `func_start: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:buffer
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/url.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.086 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.713 IQR)
- **Top Global Matches:** file_cluster_8: 11.086, file_cluster_13: 11.227, file_cluster_16: 11.357
- **Magnitude:** 5.36 | **LOC:** 542 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (13.0114%), Tech Debt (57.3759%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 15.9 | O(N^2) | DB: 1)
    * *Intent:* /** * The `url.format()` method returns a formatted URL string derived from `urlObject`. *
  * `toJSON` (Impact: 9.0 | O(N^2) | DB: 1)
    * *Intent:* * } * ``` * * The example above assumes well-formed headers are forwarded from a reverse * proxy to ...
  * `format` (Impact: 8.3 | O(N^2))
  * `values` (Impact: 4.5 | O(N^2) | DB: 1)
    * *Intent:* * query: { * page: 1, * format: 'json', * }, * }); * * // => 'https://example.com/some/path?page=1&#...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 30`, `args: 23`, `func_start: 19`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 12`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 1`, `import: 4`
* *Defense:* `safety: 8`, `doc: 9`, `test: 1`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:querystring, node:http, node:buffer, node:url
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/web-globals/events.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.331 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.486 IQR)
- **Top Global Matches:** file_cluster_16: 11.331, file_cluster_8: 11.65, file_cluster_11: 11.874
- **Magnitude:** 5.3 | **LOC:** 107 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (33.6587%), Tech Debt (69.7059%)
**Top Internal Functions/Classes:**
  * `removeEventListener` (Impact: 33.2 | O(N^3) | DB: 3)
  * `stopPropagation` (Impact: 6.1 | O(N^1))
  * `handleEvent` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 54`, `args: 11`, `func_start: 9`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 9`, `orphaned_logic: 3`
* *Architecture:* `api: 1`
* *Defense:* `safety: 8`, `immutability_locks: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `node/events.d.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.311 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 6.288 IQR)
- **Top Global Matches:** file_cluster_16: 13.311, file_cluster_2: 13.709, file_cluster_13: 13.734
- **Magnitude:** 4.98 | **LOC:** 1048 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.8806%), Tech Debt (84.8817%)
**Top Internal Functions/Classes:**
  * `setMaxListeners` (Impact: 18.8 | O(N^3))
    * *Intent:* /** * The `Symbol.for('nodejs.rejection')` method is called in case a * promise rejection happens wh...
  * `emitDestroy` (Impact: 12.8 | O(N^3))
    * *Intent:* * ```js * import { EventEmitter } from 'node:events'; * const myEmitter = new EventEmitter(); * * //...
  * `setMaxListeners` (Impact: 3.8 | O(N^3))
    * *Intent:* /** * The `EventEmitter` class is defined and exposed by the `node:events` module: * * ```js * impor...
  * `constructor` (Impact: 3.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 113`, `args: 49`, `func_start: 56`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 3`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 34`, `doc: 56`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 12.5
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` node:process, node:async_hooks, node:assert, node:events
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `node/timers.d.ts` (TYPESCRIPT) | Magnitude: 3.02 | Delta: **0.17 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 27, doc: 23, time_date_logic: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `node/domain.d.ts` (TYPESCRIPT) | Magnitude: 0.33 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 12, indent_spaces: 10, structural_boundaries: 9, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `node/tls.d.ts` (TYPESCRIPT) | Magnitude: 11.09 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, doc: 86, branch: 47, structural_boundaries: 46
- `node/cluster.d.ts` (TYPESCRIPT) | Magnitude: 5.59 | Delta: **0.045 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 63, ipc_rpc_bridges: 31, doc: 30, structural_boundaries: 21
- `node/path/posix.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, io: 8, indent_spaces: 4, api: 2
- `node/path/win32.d.ts` (TYPESCRIPT) | Magnitude: 1.62 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, io: 8, indent_spaces: 4, api: 2
- `node/readline.d.ts` (TYPESCRIPT) | Magnitude: 5.7 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 79, doc: 41, branch: 32, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `node/vm.d.ts` (TYPESCRIPT) | Magnitude: 0.6 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, doc: 36, structural_boundaries: 18, branch: 15
- `node/module.d.ts` (TYPESCRIPT) | Magnitude: 14.22 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 204, structural_boundaries: 83, doc: 82, branch: 36
- `node/http2.d.ts` (TYPESCRIPT) | Magnitude: 19.05 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 576, immutability_locks: 253, structural_boundaries: 172, func_start: 138
- `node/buffer.d.ts` (TYPESCRIPT) | Magnitude: 4.43 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 64, indent_spaces: 64, args: 35, func_start: 33
- `node/util/types.d.ts` (TYPESCRIPT) | Magnitude: 0.85 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: safety: 87, indent_spaces: 50, doc: 44, args: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `node/web-globals/timers.d.ts` (TYPESCRIPT) | Magnitude: 2.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 19, func_start: 10, generics: 10
- `node/ts5.7/compatibility/float16array.d.ts` (TYPESCRIPT) | Magnitude: 164.31 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 64, func_start: 44, args: 37, branch: 25
- `node/diagnostics_channel.d.ts` (TYPESCRIPT) | Magnitude: 6.91 | Delta: **0.109 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 91, doc: 63, structural_boundaries: 31, generics: 27
- `node/globals.typedarray.d.ts` (TYPESCRIPT) | Magnitude: 1.67 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 33, doc: 32, ui_framework: 31, generics: 31
- `node/https.d.ts` (TYPESCRIPT) | Magnitude: 2.16 | Delta: **0.112 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 73, io: 47, generics: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `node/compatibility/iterators.d.ts` (TYPESCRIPT) | Magnitude: 1.47 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: generics: 11, structural_boundaries: 10, indent_spaces: 5, class_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `node/ts5.6/buffer.buffer.d.ts` (TYPESCRIPT) | Magnitude: 5.47 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 17, indent_spaces: 9, args: 5, structural_boundaries: 4
- `node/net.d.ts` (TYPESCRIPT) | Magnitude: 9.03 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 109, branch: 108, doc: 107
- `node/assert.d.ts` (TYPESCRIPT) | Magnitude: 32.09 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: sec_high_risk_execution: 161, indent_spaces: 99, safety: 62, doc: 39
- `node/dns/promises.d.ts` (TYPESCRIPT) | Magnitude: 3.31 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 71, sec_io: 27, immutability_locks: 24, args: 10
- `node/dgram.d.ts` (TYPESCRIPT) | Magnitude: 1.69 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 110, doc: 43, branch: 40, structural_boundaries: 38

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `node/web-globals/crypto.d.ts` -> **Severity: 1224.108** (Blast Radius: 12.5 * Doc Risk: 97.9286%)
- `node/web-globals/abortcontroller.d.ts` -> **Severity: 1151.102** (Blast Radius: 12.5 * Doc Risk: 92.0882%)
- `node/web-globals/timers.d.ts` -> **Severity: 943.084** (Blast Radius: 12.5 * Doc Risk: 75.4467%)
- `node/web-globals/events.d.ts` -> **Severity: 844.319** (Blast Radius: 12.5 * Doc Risk: 67.5455%)
- `node/web-globals/blob.d.ts` -> **Severity: 778.074** (Blast Radius: 12.5 * Doc Risk: 62.2459%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
