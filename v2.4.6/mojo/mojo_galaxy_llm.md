# ARCHITECTURAL_BRIEF: mojo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/mojo` |
| **Timestamp** | `2026-08-03T19:29:54.872693+00:00` |
| **Scan Duration** | `1.32s` |
| **Git Branch** | `main` |
| **Git Commit** | `19fc4f19a0d83204a458ae4a19d192b7eaf4ba81` |
| **Git Remote** | `https://github.com/mojolicious/mojo.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Total Artifacts | 405 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 90 |
| Total LOC | 52647 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 77.8% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7604 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2008 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 280 | 52539 | 88.9% |
| PLAINTEXT | 22 | 12 | 7.0% |
| JSON | 6 | 30 | 1.9% |
| YAML | 4 | 13 | 1.3% |
| MARKDOWN | 1 | 0 | 0.3% |
| MAKEFILE | 1 | 52 | 0.3% |
| HTML | 1 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.673`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 151 | 47.9% |
| file_cluster_8 | 45 | 14.3% |
| file_cluster_13 | 42 | 13.3% |
| file_cluster_4 | 41 | 13.0% |
| Unknown | 12 | 3.8% |
| file_cluster_17 | 10 | 3.2% |
| file_cluster_2 | 3 | 1.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 90*

**Composition by Extension & Reason:**
- `.ep`: 11x Excluded (Unsupported Extension: '.ep'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.epl`: 8x Excluded (Unsupported Extension: '.epl'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 8x Excluded (Explicitly Denied Extension: '.png')
- `.conf`: 6x Excluded (Unsupported Extension: '.conf'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 11 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.css`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mt`: 2x Excluded (Unsupported Extension: '.mt'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')
- `.map`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 100.0 | 50.3 | 47.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 46.0 | 43.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 13.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 21.6 | 0.6 | 0.0 |
| API Exposure | 0.0 | 10.7 | 0.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 24.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 79.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 89.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.6 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 79.2 | 1.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 34.1 | 23.1 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 13.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Mojo/UserAgent.pm` (Hits: 84)
- `lib/Mojo/DOM/CSS.pm` (Hits: 57)
- `lib/Test/Mojo.pm` (Hits: 43)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **content.t** (`t/mojo/content.t`) — 10 inbound connections
2. **Mojolicious.pm** (`lib/Mojolicious.pm`) — 7 inbound connections
3. **Config.pm** (`lib/Mojolicious/Plugin/Config.pm`) — 6 inbound connections
4. **URL.pm** (`lib/Mojo/URL.pm`) — 3 inbound connections
5. **path.t** (`t/mojo/path.t`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Util.pm** (`lib/Mojo/Util.pm`) — 31 outbound dependencies
2. **dom.t** (`t/mojo/dom.t`) — 26 outbound dependencies
3. **request.t** (`t/mojo/request.t`) — 26 outbound dependencies
4. **response.t** (`t/mojo/response.t`) — 26 outbound dependencies
5. **commands.t** (`t/mojolicious/commands.t`) — 23 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `download` (@ `lib/Mojo/UserAgent/Transactor.pm`) -> Impact: **2104.6** | LOC: 572
- `new` (@ `lib/Test/Mojo.pm`) -> Impact: **1764.9** | LOC: 1103
- `start_app` (@ `lib/Mojolicious/Commands.pm`) -> Impact: **1596.1** | LOC: 244
- `register` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> Impact: **1515.6** | LOC: 902
- `attr` (@ `lib/Mojo/Base.pm`) -> Impact: **1403.8** | LOC: 357
- `run` (@ `lib/Mojolicious/Command/get.pm`) -> Impact: **1259.6** | LOC: 215
- `client` (@ `lib/Mojo/IOLoop.pm`) -> Impact: **1251.4** | LOC: 506
- `clone` (@ `lib/Mojo/URL.pm`) -> Impact: **1055.0** | LOC: 510
- `BUILD_DYNAMIC` (@ `lib/Mojolicious/Controller.pm`) -> Impact: **1001.5** | LOC: 949
- `AWAIT_GET` (@ `lib/Mojo/Promise.pm`) -> Impact: **977.0** | LOC: 533

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `run` (@ `lib/Mojolicious/Command/eval.pm`) -> **O(2^N) [Recursive]**
- `run` (@ `lib/Mojolicious/Command/get.pm`) -> **O(2^N) [Recursive]**
- `_walk` (@ `lib/Mojolicious/Command/routes.pm`) -> **O(2^N) [Recursive]**
- `start_app` (@ `lib/Mojolicious/Commands.pm`) -> **O(2^N) [Recursive]**
- `attr` (@ `lib/Mojo/Base.pm`) -> **O(2^N) [Recursive]**
- `client` (@ `lib/Mojo/IOLoop.pm`) -> **O(2^N) [Recursive]**
- `AWAIT_GET` (@ `lib/Mojo/Promise.pm`) -> **O(2^N) [Recursive]**
- `process` (@ `lib/Mojo/Template.pm`) -> **O(2^N) [Recursive]**
- `download` (@ `lib/Mojo/UserAgent/Transactor.pm`) -> **O(2^N) [Recursive]**
- `register` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `new` (@ `lib/Test/Mojo.pm`) -> DB Complexity: **394**
- `BUILD_DYNAMIC` (@ `lib/Mojolicious/Controller.pm`) -> DB Complexity: **255**
- `BUILD_DYNAMIC` (@ `lib/Mojolicious/Routes/Route.pm`) -> DB Complexity: **221**
- `download` (@ `lib/Mojo/UserAgent/Transactor.pm`) -> DB Complexity: **198**
- `register` (@ `lib/Mojolicious/Plugin/DefaultHelpers.pm`) -> DB Complexity: **198**
- `is_finished` (@ `lib/Mojo/Headers.pm`) -> DB Complexity: **184**
- `download` (@ `lib/Mojo/File.pm`) -> DB Complexity: **181**
- `client` (@ `lib/Mojo/IOLoop.pm`) -> DB Complexity: **154**
- `BUILD_DYNAMIC` (@ `lib/Mojolicious.pm`) -> DB Complexity: **144**
- `cookies` (@ `lib/Mojo/Message/Request.pm`) -> DB Complexity: **129**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `lib/Mojo` | 35 | 55329.86 | 48.64% | 18.2% |
| `t/mojo/certs` | 10 | 50000.0 | 0.0% | 0.0% |
| `t/mojo` | 63 | 24731.94 | 83.5% | 8.37% |
| `lib/Mojo/IOLoop/resources` | 2 | 10000.0 | 0.0% | 0.0% |
| `lib/Mojo/UserAgent` | 4 | 9438.44 | 48.9% | 0.0% |
| `lib/Mojolicious/Routes` | 3 | 8325.58 | 44.56% | 4.13% |
| `lib/Mojolicious` | 12 | 8189.96 | 44.17% | 18.64% |
| `lib/Mojo/DOM` | 2 | 6587.69 | 49.08% | 0.0% |
| `t/mojolicious` | 54 | 4762.26 | 50.69% | 0.94% |
| `lib/Mojo/Server` | 6 | 4266.67 | 47.36% | 19.64% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `lib/Mojo/Asset.pm` -> **100.0%** Exposure
- `lib/Mojo/Cookie.pm` -> **100.0%** Exposure
- `lib/Mojo/Reactor.pm` -> **100.0%** Exposure
- `lib/Mojo/Transaction.pm` -> **100.0%** Exposure
- `lib/Mojolicious/Plugin.pm` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `lib/Mojo/Asset.pm` -> **100.0%** Exposure
- `lib/Mojo/Asset/File.pm` -> **100.0%** Exposure
- `lib/Mojo/Asset/Memory.pm` -> **100.0%** Exposure
- `lib/Mojo/Base.pm` -> **100.0%** Exposure
- `lib/Mojo/ByteStream.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Mojo/Reactor.pm` -> **0** Orphaned Functions | **24** Duplicates
- `lib/Mojo/Asset.pm` -> **0** Orphaned Functions | **16** Duplicates
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` -> **14** Orphaned Functions | **0** Duplicates
- `lib/Mojo/Transaction.pm` -> **0** Orphaned Functions | **8** Duplicates
- `lib/Mojolicious/Lite.pm` -> **0** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`lib/Mojolicious/Command/Author/generate/makefile.pm`** -> AI Confidence: **99.06%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `t/mojo/request.t` -> **100.0%** Exposure
- `t/mojo/websocket_proxy_tls.t` -> **0.0022%** Exposure
- `examples/microhttpd.pl` -> **0.0001%** Exposure
### Exploit Generation Surface
- `lib/Mojo/Base.pm` -> **100.0%** Exposure
- `lib/Mojo/Content.pm` -> **100.0%** Exposure
- `lib/Mojo/DOM.pm` -> **100.0%** Exposure
- `lib/Mojo/Headers.pm` -> **100.0%** Exposure
- `lib/Mojo/IOLoop.pm` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `lib/Mojo/IOLoop.pm` -> **100.0%** Exposure
- `lib/Mojo/Server.pm` -> **100.0%** Exposure
- `lib/Mojo/Server/Prefork.pm` -> **100.0%** Exposure
- `lib/Mojo/URL.pm` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `lib/Mojo/Base.pm` -> **100.0%** Exposure
- `lib/Mojo/IOLoop.pm` -> **100.0%** Exposure
- `lib/Mojo/IOLoop/Client.pm` -> **100.0%** Exposure
- `lib/Mojo/Promise.pm` -> **100.0%** Exposure
- `lib/Mojo/Template.pm` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1755` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `lib/Mojo/IOLoop.pm` (PERL) -> Cumulative Risk: **856.28**
- **Archetype:** `file_cluster_4` (Distance: 14.508 IQR)
- **Magnitude:** 1893.86 | **LOC:** 552 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `client` (Impact: 1251.4), `acceptor` (Impact: 6.4)

### 2. `t/mojo/lib/Mojo/TestConnectProxy.pm` (PERL) -> Cumulative Risk: **844.27**
- **Archetype:** `file_cluster_4` (Distance: 11.968 IQR)
- **Magnitude:** 332.48 | **LOC:** 85 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `proxy` (Impact: 245.3)

### 3. `lib/Mojolicious/Command/eval.pm` (PERL) -> Cumulative Risk: **826.01**
- **Archetype:** `file_cluster_4` (Distance: 13.652 IQR)
- **Magnitude:** 663.84 | **LOC:** 100 | **CtrlFlow:** 78.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 598.6)

### 4. `lib/Mojolicious/Command/routes.pm` (PERL) -> Cumulative Risk: **810.84**
- **Archetype:** `file_cluster_0` (Distance: 13.689 IQR)
- **Magnitude:** 958.12 | **LOC:** 122 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_walk` (Impact: 866.0), `run` (Impact: 5.6)

### 5. `lib/Mojolicious/Command/get.pm` (PERL) -> Cumulative Risk: **800.41**
- **Archetype:** `file_cluster_0` (Distance: 13.664 IQR)
- **Magnitude:** 1408.84 | **LOC:** 232 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `run` (Impact: 1259.6)

### 6. `lib/Mojo/Base.pm` (PERL) -> Cumulative Risk: **755.7**
- **Archetype:** `file_cluster_13` (Distance: 13.675 IQR)
- **Magnitude:** 1547.32 | **LOC:** 382 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `attr` (Impact: 1403.8), `DESTROY` (Impact: 1.1)

### 7. `lib/Mojo/UserAgent/Transactor.pm` (PERL) -> Cumulative Risk: **745.77**
- **Archetype:** `file_cluster_0` (Distance: 14.023 IQR)
- **Magnitude:** 2524.46 | **LOC:** 595 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `download` (Impact: 2104.6), `add_generator` (Impact: 1.1)

### 8. `lib/Mojo/Server.pm` (PERL) -> Cumulative Risk: **738.79**
- **Archetype:** `file_cluster_0` (Distance: 13.879 IQR)
- **Magnitude:** 170.02 | **LOC:** 204 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.7576%)
- **Heaviest Functions:** `build_app` (Impact: 36.3), `new` (Impact: 8.7), `run` (Impact: 2.4)

### 9. `lib/Mojo/Util.pm` (PERL) -> Cumulative Risk: **720.58**
- **Archetype:** `file_cluster_0` (Distance: 14.685 IQR)
- **Magnitude:** 1689.42 | **LOC:** 1064 | **CtrlFlow:** 62.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9772%)
- **Heaviest Functions:** `unindent` (Impact: 513.7), `class_to_file` (Impact: 447.1), `camelize` (Impact: 6.1)

### 10. `lib/Mojo/Server/Prefork.pm` (PERL) -> Cumulative Risk: **673.0**
- **Archetype:** `file_cluster_0` (Distance: 13.919 IQR)
- **Magnitude:** 315.24 | **LOC:** 416 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Concurrency (99.5361%)
- **Heaviest Functions:** `_manage` (Impact: 36.0), `_wait` (Impact: 19.3), `ensure_pid_file` (Impact: 12.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `lib/Mojo/DOM.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.967 IQR)
- **Top Global Matches:** file_cluster_17: 12.967, file_cluster_0: 13.115, file_cluster_8: 13.191
- **Magnitude:** 21101.6 | **LOC:** 1109 | **CtrlFlow:** 54.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (76.9261%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 200`, `args: 74`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 341`
* *Architecture:* `io: 11`, `import: 9`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` it, Mojo::Base, Mojo::Collection, Storable, Mojo::DOM, value, parent, Mojo::DOM::HTML...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Content.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.987 IQR)
- **Top Global Matches:** file_cluster_0: 13.987, file_cluster_13: 14.092, file_cluster_8: 14.124
- **Magnitude:** 14254.1 | **LOC:** 608 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.3149%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 125`, `args: 42`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 289`
* *Architecture:* `io: 9`, `import: 7`
* *Defense:* `safety: 4`, `doc: 45`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.382
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004246
  * `Imports (Out-Degree: 0):` Mojo::Base, Compress::Raw::Zlib, Mojo::SSE, Mojo::Headers, Scalar::Util, Carp, leading
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/mojo/util.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.787 IQR)
- **Top Global Matches:** file_cluster_0: 10.787, file_cluster_8: 10.849, file_cluster_13: 11.255
- **Magnitude:** 8692.12 | **LOC:** 691 | **CtrlFlow:** 83.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (43.7731%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 415`, `structural_boundaries: 81`, `args: 3`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `import: 15`
* *Defense:* `safety: 3`, `doc: 2`, `test: 100`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Mojo::DeprecationTest, Mojo::Base, warning, o, Mojo::File, Mojo::Util, result, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojolicious/Routes/Pattern.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.025 IQR)
- **Top Global Matches:** file_cluster_0: 14.025, file_cluster_8: 14.256, file_cluster_13: 14.266
- **Magnitude:** 6506.86 | **LOC:** 371 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.4871%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 175`, `structural_boundaries: 86`, `args: 11`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 292`
* *Architecture:* `import: 3`
* *Defense:* `safety: 1`, `doc: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojolicious::Routes::Pattern, Carp, Mojo::Base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/UserAgent/CookieJar.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.545 IQR)
- **Top Global Matches:** file_cluster_0: 13.545, file_cluster_13: 13.772, file_cluster_8: 13.866
- **Magnitude:** 6469.14 | **LOC:** 319 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.5403%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 76`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 198`
* *Architecture:* `io: 9`, `import: 6`
* *Defense:* `doc: 20`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Cookie::Request, Mojo::Path, Mojo::Base, Mojo::File, Scalar::Util, Mojo::UserAgent::CookieJar
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/DOM/HTML.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.413 IQR)
- **Top Global Matches:** file_cluster_0: 13.413, file_cluster_13: 13.502, file_cluster_17: 13.621
- **Magnitude:** 5641.17 | **LOC:** 377 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.8931%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 77`, `args: 7`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 178`
* *Architecture:* `io: 6`, `api: 2`, `import: 6`
* *Defense:* `doc: 15`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, warnings, Mojo::Util, Mojo::DOM::HTML, Exporter, more, Scalar::Util
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/IOLoop/resources/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/IOLoop/resources/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/bad.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/bad.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/ca.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/ca.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/client.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/client.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/domain.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/domain.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/certs/server.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Server/Morbo.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.43 IQR)
- **Top Global Matches:** file_cluster_0: 13.43, file_cluster_4: 13.528, file_cluster_13: 13.78
- **Magnitude:** 3045.37 | **LOC:** 156 | **CtrlFlow:** 82.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (49.5869%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 27`, `args: 4`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 69`
* *Architecture:* `io: 5`, `concurrency: 18`, `import: 6`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::Loader, Mojo::Server::Daemon, Mojo::Server::Morbo, POSIX, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Test/Mojo.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.434 IQR)
- **Top Global Matches:** file_cluster_0: 14.434, file_cluster_4: 14.499, file_cluster_13: 14.536
- **Magnitude:** 2872.38 | **LOC:** 1354 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 394
- **Risk Profile:** Cognitive Load (24.93%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 1764.9 | O(2^N) | DB: 394)
  * `finished_ok` (Impact: 15.9 | O(N^1) | DB: 1)
  * `json_has` (Impact: 12.2 | O(N^1) | DB: 1)
  * `json_hasnt` (Impact: 12.2 | O(N^1) | DB: 1)
  * `finish_ok` (Impact: 7.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 224`, `args: 111`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `state_mutation: 812`, `planned_debt: 1`
* *Architecture:* `io: 43`, `concurrency: 80`, `import: 30`
* *Defense:* `safety: 1`, `doc: 86`, `test: 13`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, similar, Mojo::Server, Test::Mojo, element, Mojo::JSON, Mojo::Util, match...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/UserAgent/Transactor.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.023 IQR)
- **Top Global Matches:** file_cluster_0: 14.023, file_cluster_13: 14.228, file_cluster_11: 14.411
- **Magnitude:** 2524.46 | **LOC:** 595 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 198
- **Risk Profile:** Cognitive Load (55.5862%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `download` (Impact: 2104.6 | O(2^N) | DB: 198)
  * `add_generator` (Impact: 1.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 189`, `args: 21`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 404`
* *Architecture:* `io: 21`, `concurrency: 7`, `import: 15`
* *Defense:* `safety: 1`, `doc: 25`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Asset::Memory, query, Mojo::WebSocket, Mojo::Base, Mojo::Content::MultiPart, Mojo::File, Mojo::JSON, Mojo::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.212 IQR)
- **Top Global Matches:** file_cluster_0: 14.212, file_cluster_13: 14.503, file_cluster_11: 14.558
- **Magnitude:** 2191.74 | **LOC:** 2178 | **CtrlFlow:** 83.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (88.18%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1093`, `structural_boundaries: 220`, `args: 24`
* *Risk/State:* `state_mutation: 2135`
* *Architecture:* `io: 18`, `import: 90`
* *Defense:* `safety: 17`, `test: 96`, `cleanup: 60`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` multipart, Mojo::Base, headers, Mojo::Content::MultiPart, content, Mojo::Util, Mojo::Content::Single, Mojo::URL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojolicious/Plugin/DefaultHelpers.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.413 IQR)
- **Top Global Matches:** file_cluster_0: 14.413, file_cluster_13: 14.513, file_cluster_4: 14.539
- **Magnitude:** 1957.4 | **LOC:** 917 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 198
- **Risk Profile:** Cognitive Load (47.8825%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `register` (Impact: 1515.6 | O(2^N) | DB: 198)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 159`, `args: 48`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 384`
* *Architecture:* `io: 20`, `concurrency: 47`, `import: 16`
* *Defense:* `safety: 7`, `doc: 58`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::Collection, Time::HiRes, Mojo::Exception, Mojo::Util, L, Mojo::IOLoop, Mojo::Asset::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/IOLoop.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.508 IQR)
- **Top Global Matches:** file_cluster_4: 14.508, file_cluster_0: 14.872, file_cluster_11: 15.174
- **Magnitude:** 1893.86 | **LOC:** 552 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 154
- **Risk Profile:** Cognitive Load (49.9999%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `client` (Impact: 1251.4 | O(2^N) | DB: 154)
  * `acceptor` (Impact: 6.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 327`, `structural_boundaries: 113`, `args: 49`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 295`
* *Architecture:* `io: 19`, `concurrency: 334`, `import: 12`
* *Defense:* `safety: 5`, `doc: 34`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::IOLoop::Server, Mojo::IOLoop::Client, Mojo::Base, Mojo::Reactor::Poll, constant, Scalar::Util, Mojo::IOLoop::Stream, Mojo::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojolicious/Commands.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.621 IQR)
- **Top Global Matches:** file_cluster_0: 12.621, file_cluster_13: 13.045, file_cluster_8: 13.154
- **Magnitude:** 1821.9 | **LOC:** 326 | **CtrlFlow:** 83.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (45.0595%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `start_app` (Impact: 1596.1 | O(2^N) | DB: 23)
  * `run` (Impact: 118.5 | O(2^N) | DB: 17)
  * `detect` (Impact: 4.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 43`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 99`
* *Architecture:* `io: 2`, `import: 4`
* *Defense:* `safety: 1`, `doc: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Loader, Mojo::Server, Mojo::Util, Mojo::Base
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/mojo/prefork.t` (PERL) | Magnitude: 125.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 90, branch: 66, structural_boundaries: 32
- `lib/Mojolicious/Renderer.pm` (PERL) | Magnitude: 583.86 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 316, branch: 223, indent_spaces: 185, structural_boundaries: 157
- `t/mojolicious/lib/MojoliciousTest/Plugin/UPPERCASETestPlugin.pm` (PERL) | Magnitude: 2.14 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 8, decorators: 4, structural_boundaries: 3, indent_spaces: 2
- `lib/Mojolicious/Controller.pm` (PERL) | Magnitude: 1554.36 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 529, indent_spaces: 401, branch: 345, structural_boundaries: 235
- `t/mojolicious/rebased_lite_app.t` (PERL) | Magnitude: 40.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 56, state_mutation: 20, indent_spaces: 14, decorators: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/mojolicious/lib/MojoliciousTest2/Foo.pm` (PERL) | Magnitude: 3.86 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 6, structural_boundaries: 4, decorators: 3, indent_spaces: 3
- `t/mojolicious/external/myapp.pl` (PERL) | Magnitude: 0.07 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_spaces: 27, structural_boundaries: 13, closures: 12
- `t/mojolicious/lib/MojoliciousTest3/Bar.pm` (PERL) | Magnitude: 3.74 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 6, structural_boundaries: 3, decorators: 3, state_mutation: 2
- `lib/Mojo/BaseUtil.pm` (PERL) | Magnitude: 63.66 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 37, structural_boundaries: 13, decorators: 13, state_mutation: 9
- `t/mojolicious/lib/MojoliciousTest/Baz.pm` (PERL) | Magnitude: 2.58 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 6, decorators: 3, structural_boundaries: 2, ssr_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/mojo/file.t` (PERL) | Magnitude: 122.58 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 257, state_mutation: 101, structural_boundaries: 67, test: 56
- `t/mojo/collection.t` (PERL) | Magnitude: 68.38 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 125, test: 78, state_mutation: 50, closures: 45
- `t/mojolicious/log_lite_app.t` (PERL) | Magnitude: 44.02 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, state_mutation: 27, branch: 20, structural_boundaries: 14
- `t/mojolicious/lib/PluginWithTemplate.pm` (PERL) | Magnitude: 4.22 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 4, structural_boundaries: 3, indent_spaces: 3, args: 2
- `examples/proxy.pl` (PERL) | Magnitude: 26.24 | Delta: **0.134 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 10, indent_spaces: 8, structural_boundaries: 5, encapsulation: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `t/mojolicious/external/lib/MyApp.pm` (PERL) | Magnitude: 0.02 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, state_mutation: 12, structural_boundaries: 8, encapsulation: 6
- `t/mojo/template.t` (PERL) | Magnitude: 748.56 | Delta: **0.081 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 726, branch: 288, ui_framework: 224, decorators: 142
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` (PERL) | Magnitude: 96.82 | Delta: **0.201 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 45, indent_spaces: 38, args: 22, structural_boundaries: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/mojo/daemon.t` (PERL) | Magnitude: 261.78 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 250, branch: 230, state_mutation: 178, structural_boundaries: 90
- `examples/microhttpd.pl` (PERL) | Magnitude: 23.52 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 17, indent_spaces: 13, sec_reflection_metaprogramming: 10, structural_boundaries: 8
- `t/mojo/morbo.t` (PERL) | Magnitude: 158.4 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 156, state_mutation: 91, indent_spaces: 83, decorators: 59
- `lib/Mojolicious/Command/eval.pm` (PERL) | Magnitude: 663.84 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 60, state_mutation: 51, indent_spaces: 29, decorators: 21
- `lib/Mojo/UserAgent/Server.pm` (PERL) | Magnitude: 165.14 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 108, state_mutation: 60, decorators: 38, indent_spaces: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/mojolicious/lite_app.t` (PERL) | Magnitude: 491.7 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 443, state_mutation: 362, branch: 193, structural_boundaries: 127
- `examples/login/t/login.t` (PERL) | Magnitude: 18.44 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 8, structural_boundaries: 4, decorators: 4
- `t/mojo/base_util.t` (PERL) | Magnitude: 2.82 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 56, indent_spaces: 30, decorators: 23, closures: 7
- `t/mojolicious/websocket_lite_app.t` (PERL) | Magnitude: 167.1 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 124, branch: 70, closures: 64
- `t/mojolicious/embedded_app.t` (PERL) | Magnitude: 39.64 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, state_mutation: 21, test: 19, closures: 19

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/mojo/util.t` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 8692.12
- `lib/Mojo/UserAgent/CookieJar.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 6469.14
- `lib/Mojo/IOLoop.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 1893.86
- `lib/Mojo/Util.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 1689.42
- `lib/Mojolicious/Controller.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 1554.36

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/mojo/response.t` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 100.0%)
- `t/mojo/exception.t` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Mojolicious.pm` -> **Severity: 1.083** (Embedded: 0.0223 * Error Risk: 48.5718%)
- `lib/Mojo/URL.pm` -> **Severity: 0.901** (Embedded: 0.0096 * Error Risk: 94.2988%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 0.823** (Embedded: 0.0191 * Error Risk: 43.0454%)
- `t/mojo/content.t` -> **Severity: 0.738** (Embedded: 0.0321 * Error Risk: 22.973%)
- `lib/Mojo/Reactor/EV.pm` -> **Severity: 0.446** (Embedded: 0.0064 * Error Risk: 70.0612%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/mojo/content.t` -> **Severity: 591.367** (Blast Radius: 22.307 * Doc Risk: 26.5104%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 423.617** (Blast Radius: 16.319 * Doc Risk: 25.9585%)
- `t/mojo/base.t` -> **Severity: 341.509** (Blast Radius: 5.32 * Doc Risk: 64.1935%)
- `lib/Mojolicious.pm` -> **Severity: 328.213** (Blast Radius: 18.356 * Doc Risk: 17.8804%)
- `lib/Mojo/BaseUtil.pm` -> **Severity: 287.409** (Blast Radius: 2.875 * Doc Risk: 99.9685%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
