# ARCHITECTURAL_BRIEF: libwww-perl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/libwww-perl` |
| **Timestamp** | `2026-08-03T19:29:51.591735+00:00` |
| **Scan Duration** | `0.29s` |
| **Git Branch** | `master` |
| **Git Commit** | `7420d1bfff7cd5369ca24e87c37edf97b2cbb0c1` |
| **Git Remote** | `https://github.com/libwww-perl/libwww-perl.git` |
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
| Total Artifacts | 100 |
| Analyzed Artifacts (Scanned) | 58 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 42 |
| Total LOC | 3925 |
| Volatility Index | 0.017 |
| % Scanned of codebase = | 58.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 52 | 3906 | 89.7% |
| MARKDOWN | 3 | 0 | 5.2% |
| PLAINTEXT | 1 | 0 | 1.7% |
| YAML | 1 | 16 | 1.7% |
| SHELL | 1 | 3 | 1.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 4`
> **Architectural Drift Z-Score:** `9.535`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 41 | 70.7% |
| file_cluster_13 | 10 | 17.2% |
| file_cluster_8 | 2 | 3.4% |
| file_cluster_17 | 1 | 1.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 6.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 42*

**Composition by Extension & Reason:**
- `.pm`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1050 LOC)
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 17 LOC)
- `.ssl`: 1x Excluded (Unsupported Extension: '.SSL')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.pl_dist`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.t`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 5.0 | 98.3 | 72.2 | 93.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 91.4 | 50.4 | 45.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.8 | 2.0 | 0.0 |
| API Exposure | 0.0 | 1.1 | 0.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 92.3 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 52.6 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.0 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 28.9 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 65.5 | 78.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 11.5 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 24.1 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lwptut.pod` (Hits: 25)
- `t/base/ua.t` (Hits: 22)
- `lwpcook.pod` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **simple.t** (`t/base/simple.t`) — 1 inbound connections
2. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
3. **README.md** (`README.md`) — 0 inbound connections
4. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections
5. **Changes** (`Changes`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lwp-request** (`bin/lwp-request`) — 20 outbound dependencies
2. **lwptut.pod** (`lwptut.pod`) — 17 outbound dependencies
3. **lwp-download** (`bin/lwp-download`) — 14 outbound dependencies
4. **http.t** (`t/local/http.t`) — 14 outbound dependencies
5. **lwpcook.pod** (`lwpcook.pod`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_test` (@ `t/local/http.t`) -> Impact: **563.5** | LOC: 431
- `daemonize` (@ `t/local/http.t`) -> Impact: **395.4** | LOC: 218
- `daemonize` (@ `t/robot/ua-get.t`) -> Impact: **80.2** | LOC: 46
- `daemonize` (@ `t/robot/ua.t`) -> Impact: **80.2** | LOC: 46
- `_test` (@ `t/robot/ua-get.t`) -> Impact: **73.5** | LOC: 60
- `_test` (@ `t/robot/ua.t`) -> Impact: **58.3** | LOC: 56
- `request` (@ `t/local/protosub.t`) -> Impact: **43.2** | LOC: 15
- `get_basic_credentials` (@ `bin/lwp-request`) -> Impact: **37.1** | LOC: 23
- `new` (@ `bin/lwp-request`) -> Impact: **21.2** | LOC: 5
- `ua` (@ `t/base/ua_handlers.t`) -> Impact: **20.5** | LOC: 10

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `new` (@ `bin/lwp-request`) -> **O(2^N) [Recursive]**
- `request` (@ `t/local/protosub.t`) -> **O(2^N) [Recursive]**
- `new` (@ `t/local/protosub.t`) -> **O(2^N) [Recursive]**
- `data` (@ `xt/author/misc/get-callback`) -> **O(2^N) [Recursive]**
- `daemonize` (@ `t/local/http.t`) -> **O(N^5)**
- `daemonize` (@ `t/robot/ua-get.t`) -> **O(N^4)**
- `daemonize` (@ `t/robot/ua.t`) -> **O(N^4)**
- `get_basic_credentials` (@ `bin/lwp-request`) -> **O(N^3)**
- `ua` (@ `t/base/ua_handlers.t`) -> **O(N^3)**
- `_test` (@ `t/local/http.t`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `_test` (@ `t/local/http.t`) -> DB Complexity: **82**
- `daemonize` (@ `t/local/http.t`) -> DB Complexity: **31**
- `daemonize` (@ `t/robot/ua-get.t`) -> DB Complexity: **13**
- `daemonize` (@ `t/robot/ua.t`) -> DB Complexity: **13**
- `_test` (@ `t/robot/ua.t`) -> DB Complexity: **11**
- `get_basic_credentials` (@ `bin/lwp-request`) -> DB Complexity: **9**
- `slurp` (@ `t/local/get.t`) -> DB Complexity: **8**
- `usage` (@ `bin/lwp-dump`) -> DB Complexity: **7**
- `_test` (@ `t/robot/ua-get.t`) -> DB Complexity: **7**
- `out` (@ `xt/author/net/cgi-bin/nph-slowdata`) -> DB Complexity: **6**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bin` | 4 | 3445.2 | 54.37% | 3.07% |
| `t/local` | 8 | 1618.2 | 94.09% | 28.99% |
| `__monolith__` | 8 | 464.12 | 26.52% | 4.94% |
| `t/robot` | 2 | 463.68 | 94.2% | 0.0% |
| `t/base` | 7 | 397.68 | 77.94% | 0.0% |
| `xt/author/live/jigsaw` | 9 | 299.4 | 74.13% | 21.99% |
| `xt/author/net` | 6 | 243.76 | 94.53% | 0.0% |
| `xt/author/misc` | 3 | 122.34 | 65.24% | 0.0% |
| `t` | 2 | 68.38 | 80.95% | 0.0% |
| `xt/author/net/cgi-bin` | 3 | 51.7 | 60.54% | 33.33% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/local/httpsub.t` -> **100.0%** Exposure
- `xt/author/net/cgi-bin/moved` -> **100.0%** Exposure
- `xt/author/live/jigsaw/auth-d.t` -> **99.8499%** Exposure
- `t/local/download_to_fh.t` -> **99.1491%** Exposure
- `xt/author/live/jigsaw/auth-b.t` -> **98.0708%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/lwp-download` -> **100.0%** Exposure
- `bin/lwp-dump` -> **100.0%** Exposure
- `bin/lwp-mirror` -> **100.0%** Exposure
- `lwpcook.pod` -> **100.0%** Exposure
- `t/10-attrs.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/local/httpsub.t` -> **8** Orphaned Functions | **2** Duplicates
- `t/local/http.t` -> **0** Orphaned Functions | **4** Duplicates
- `bin/lwp-request` -> **1** Orphaned Functions | **0** Duplicates
- `xt/author/live/jigsaw/auth-b.t` -> **1** Orphaned Functions | **0** Duplicates
- `xt/author/live/jigsaw/auth-d.t` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`xt/author/net/cgi-bin/moved`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `bin/lwp-request` -> **100.0%** Exposure
- `t/base/ua.t` -> **100.0%** Exposure
- `t/local/http.t` -> **100.0%** Exposure
- `t/robot/ua-get.t` -> **100.0%** Exposure
- `t/robot/ua.t` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bin/lwp-request` -> **100.0%** Exposure
- `t/local/http.t` -> **100.0%** Exposure
- `t/robot/ua-get.t` -> **100.0%** Exposure
- `t/robot/ua.t` -> **100.0%** Exposure
- `talk-to-ourself` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `t/local/http.t` -> **100.0%** Exposure
- `t/local/httpsub.t` -> **100.0%** Exposure
- `t/robot/ua.t` -> **99.7683%** Exposure
- `t/local/protosub.t` -> **99.6335%** Exposure
- `bin/lwp-request` -> **99.4384%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `354` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/robot/ua.t` (PERL) -> Cumulative Risk: **772.48**
- **Archetype:** `file_cluster_0` (Distance: 12.537 IQR)
- **Magnitude:** 230.22 | **LOC:** 146 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `daemonize` (Impact: 80.2), `_test` (Impact: 58.3), `url` (Impact: 2.2)

### 2. `t/robot/ua-get.t` (PERL) -> Cumulative Risk: **762.61**
- **Archetype:** `file_cluster_0` (Distance: 12.281 IQR)
- **Magnitude:** 233.46 | **LOC:** 149 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `daemonize` (Impact: 80.2), `_test` (Impact: 73.5), `url` (Impact: 2.2)

### 3. `t/local/http.t` (PERL) -> Cumulative Risk: **726.12**
- **Archetype:** `file_cluster_0` (Distance: 12.658 IQR)
- **Magnitude:** 1318.54 | **LOC:** 749 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `_test` (Impact: 563.5), `daemonize` (Impact: 395.4), `get_basic_credentials` (Impact: 13.8)

### 4. `bin/lwp-request` (PERL) -> Cumulative Risk: **694.71**
- **Archetype:** `file_cluster_0` (Distance: 12.258 IQR)
- **Magnitude:** 219.04 | **LOC:** 566 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%), State Flux (99.9987%)
- **Heaviest Functions:** `get_basic_credentials` (Impact: 37.1), `new` (Impact: 21.2), `show` (Impact: 10.3)

### 5. `xt/author/net/cgi-bin/nph-slowdata` (PERL) -> Cumulative Risk: **662.36**
- **Archetype:** `file_cluster_13` (Distance: 12.192 IQR)
- **Magnitude:** 13.98 | **LOC:** 28 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `out` (Impact: 4.6)

### 6. `xt/author/net/http-post.t` (PERL) -> Cumulative Risk: **653.08**
- **Archetype:** `file_cluster_0` (Distance: 13.484 IQR)
- **Magnitude:** 42.54 | **LOC:** 39 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.977%)

### 7. `xt/author/net/cgi-bin/slowread` (PERL) -> Cumulative Risk: **647.73**
- **Archetype:** `file_cluster_13` (Distance: 12.764 IQR)
- **Magnitude:** 36.46 | **LOC:** 34 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)

### 8. `xt/author/net/http-get.t` (PERL) -> Cumulative Risk: **642.79**
- **Archetype:** `file_cluster_0` (Distance: 13.252 IQR)
- **Magnitude:** 36.5 | **LOC:** 37 | **CtrlFlow:** 65.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.8844%)

### 9. `xt/author/net/moved.t` (PERL) -> Cumulative Risk: **638.38**
- **Archetype:** `file_cluster_0` (Distance: 12.947 IQR)
- **Magnitude:** 33.48 | **LOC:** 34 | **CtrlFlow:** 65.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Logic Bomb (99.8666%)

### 10. `xt/author/net/mirror.t` (PERL) -> Cumulative Risk: **636.8**
- **Archetype:** `file_cluster_0` (Distance: 12.927 IQR)
- **Magnitude:** 33.46 | **LOC:** 34 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Injection Surface (100.0%), Cognitive Load (94.6321%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/lwp-download` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.708 IQR)
- **Top Global Matches:** file_cluster_13: 12.708, file_cluster_0: 12.757, file_cluster_8: 12.935
- **Magnitude:** 3123.9 | **LOC:** 336 | **CtrlFlow:** 63.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (77.2798%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 64`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 189`, `dead_code: 1`
* *Architecture:* `io: 10`, `import: 14`
* *Defense:* `safety: 2`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode::Locale, URI, LWP::MediaTypes, Fcntl, File::Spec, strict, warnings, HTTP::Date...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/http.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.658 IQR)
- **Top Global Matches:** file_cluster_0: 12.658, file_cluster_13: 13.156, file_cluster_8: 13.179
- **Magnitude:** 1318.54 | **LOC:** 749 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (98.3428%), Tech Debt (32.7407%)
**Top Internal Functions/Classes:**
  * `_test` (Impact: 563.5 | O(N^3) | DB: 82)
  * `daemonize` (Impact: 395.4 | O(N^5) | DB: 31)
  * `get_basic_credentials` (Impact: 13.8 | O(N^3))
  * `get_basic_credentials` (Impact: 13.8 | O(N^3))
  * `get_basic_credentials` (Impact: 13.8 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 138`, `args: 21`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 298`, `duplicate_logic: 4`
* *Architecture:* `io: 14`, `api: 4`, `import: 16`
* *Defense:* `safety: 2`, `test: 94`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Daemon, URI, Config, point, utf8, strict, HTTP::Request, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua-get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.281 IQR)
- **Top Global Matches:** file_cluster_0: 12.281, file_cluster_13: 12.589, file_cluster_11: 12.829
- **Magnitude:** 233.46 | **LOC:** 149 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (94.1654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` (Impact: 80.2 | O(N^4) | DB: 13)
  * `_test` (Impact: 73.5 | O(N^2) | DB: 7)
  * `url` (Impact: 2.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 37`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 75`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Daemon, URI, Config, utf8, strict, warnings, LWP::RobotUA, FindBin...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.537 IQR)
- **Top Global Matches:** file_cluster_0: 12.537, file_cluster_13: 12.774, file_cluster_11: 13.034
- **Magnitude:** 230.22 | **LOC:** 146 | **CtrlFlow:** 64.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (94.2332%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` (Impact: 80.2 | O(N^4) | DB: 13)
  * `_test` (Impact: 58.3 | O(N^2) | DB: 11)
  * `url` (Impact: 2.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 41`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 87`
* *Architecture:* `io: 3`, `import: 10`
* *Defense:* `safety: 2`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Daemon, URI, Config, utf8, strict, HTTP::Request, warnings, LWP::RobotUA...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwptut.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.688 IQR)
- **Top Global Matches:** file_cluster_0: 12.688, file_cluster_13: 12.79, file_cluster_8: 12.982
- **Magnitude:** 219.38 | **LOC:** 821 | **CtrlFlow:** 81.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (44.1899%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 352`, `structural_boundaries: 79`
* *Risk/State:* `state_mutation: 194`
* *Architecture:* `io: 25`, `import: 31`
* *Defense:* `safety: 8`, `doc: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request::Common, LWP::Simple, for, URI, LWP::ConnCache, it, the, proxies...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-request` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.258 IQR)
- **Top Global Matches:** file_cluster_0: 12.258, file_cluster_13: 12.291, file_cluster_8: 12.661
- **Magnitude:** 219.04 | **LOC:** 566 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (46.8712%), Tech Debt (12.273%)
**Top Internal Functions/Classes:**
  * `get_basic_credentials` (Impact: 37.1 | O(N^3) | DB: 9)
  * `new` (Impact: 21.2 | O(2^N) | DB: 4)
  * `show` (Impact: 10.3 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 69`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 141`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 1`, `import: 23`
* *Defense:* `safety: 6`, `doc: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` for, this, effect, warnings, HTTP::Date, HTTP::Status, method, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.729 IQR)
- **Top Global Matches:** file_cluster_0: 12.729, file_cluster_13: 13.194, file_cluster_8: 13.295
- **Magnitude:** 138.2 | **LOC:** 207 | **CtrlFlow:** 82.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.3309%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 33`, `args: 1`
* *Risk/State:* `state_mutation: 120`
* *Architecture:* `io: 22`, `import: 6`
* *Defense:* `safety: 2`, `test: 54`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` undef, strict, HTTP::Request, warnings, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwpcook.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.056 IQR)
- **Top Global Matches:** file_cluster_0: 12.056, file_cluster_13: 12.22, file_cluster_17: 12.669
- **Magnitude:** 112.1 | **LOC:** 311 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (57.7847%), Tech Debt (39.4884%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 38`, `args: 1`
* *Risk/State:* `state_mutation: 93`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `import: 27`
* *Defense:* `safety: 2`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTP::Request::Common, LWP::Simple, proxies, the, this, HTTP::CookieJar::LWP, simple, SSL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/protosub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.364 IQR)
- **Top Global Matches:** file_cluster_0: 16.364, file_cluster_13: 16.749, file_cluster_11: 16.908
- **Magnitude:** 86.3 | **LOC:** 58 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (92.4142%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 43.2 | O(2^N) | DB: 3)
  * `new` (Impact: 17.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 17`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Request, warnings, LWP::Protocol, parent, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/cache-timeouts.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.253 IQR)
- **Top Global Matches:** file_cluster_0: 12.253, file_cluster_13: 12.42, file_cluster_17: 12.83
- **Magnitude:** 70.38 | **LOC:** 94 | **CtrlFlow:** 72.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.6321%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 19`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 54`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net, LWP::ConnCache, strict, HTTP::Request, warnings, FindBin, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/ua_handlers.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.603 IQR)
- **Top Global Matches:** file_cluster_0: 12.603, file_cluster_13: 12.621, file_cluster_11: 12.879
- **Magnitude:** 66.64 | **LOC:** 66 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (91.3004%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ua` (Impact: 20.5 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 19`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Response, strict, HTTP::Request, warnings, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/default_content_type.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.16 IQR)
- **Top Global Matches:** file_cluster_0: 12.16, file_cluster_13: 12.511, file_cluster_11: 12.65
- **Magnitude:** 65.08 | **LOC:** 141 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (89.9557%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 26`
* *Risk/State:* `state_mutation: 48`, `dead_code: 1`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` the, strict, HTTP::Request, warnings, default, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/httpsub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.02 IQR)
- **Top Global Matches:** file_cluster_0: 12.02, file_cluster_13: 12.201, file_cluster_8: 12.626
- **Magnitude:** 60.06 | **LOC:** 93 | **CtrlFlow:** 50.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (92.7435%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 2.3 | O(N^2) | DB: 2)
  * `format_request` (Impact: 2.3 | O(N^2) | DB: 2)
  * `syswrite` (Impact: 2.3 | O(N^2) | DB: 5)
  * `read_response_headers` (Impact: 2.3 | O(N^2) | DB: 2)
  * `read_entity_body` (Impact: 2.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 36`, `args: 10`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 31`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 3`, `api: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Request, warnings, LWP::Protocol, parent, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-dump` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.798 IQR)
- **Top Global Matches:** file_cluster_13: 12.798, file_cluster_0: 12.935, file_cluster_8: 13.228
- **Magnitude:** 59.36 | **LOC:** 114 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (45.2601%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 3.8 | O(N^1) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 12`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 6`, `import: 8`
* *Defense:* `safety: 3`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode::Locale, strict, warnings, Getopt::Long, content, LWP::UserAgent, Encode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/proxy.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.519 IQR)
- **Top Global Matches:** file_cluster_0: 11.519, file_cluster_13: 11.666, file_cluster_8: 11.862
- **Magnitude:** 55.44 | **LOC:** 85 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (90.702%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 35`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 8`, `import: 5`
* *Defense:* `safety: 2`, `test: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, errors, Test::Fatal, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/chunk.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.446 IQR)
- **Top Global Matches:** file_cluster_17: 14.446, file_cluster_0: 14.509, file_cluster_13: 14.565
- **Magnitude:** 51.48 | **LOC:** 35 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (94.4451%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 12`, `args: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Request, warnings, Test::RequiresInternet, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.36 | **LOC:** 2468 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/misc/get-callback` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.784 IQR)
- **Top Global Matches:** file_cluster_13: 13.784, file_cluster_0: 13.823, file_cluster_8: 14.199
- **Magnitude:** 46.78 | **LOC:** 30 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (94.4451%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `data` (Impact: 16.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 10`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-mirror` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.11 IQR)
- **Top Global Matches:** file_cluster_13: 12.11, file_cluster_0: 12.211, file_cluster_8: 12.496
- **Magnitude:** 42.9 | **LOC:** 104 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (48.0796%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 2.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 17`, `args: 2`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 39`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode::Locale, LWP::Simple, strict, warnings, Getopt::Long, basename, LWP, Encode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `talk-to-ourself` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.751 IQR)
- **Top Global Matches:** file_cluster_0: 12.751, file_cluster_13: 12.969, file_cluster_11: 13.329
- **Magnitude:** 42.78 | **LOC:** 51 | **CtrlFlow:** 76.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (95.3719%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 12`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 27`
* *Architecture:* `io: 13`, `import: 4`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IO::Socket, strict, warnings, IO::Select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/10-attrs.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.291 IQR)
- **Top Global Matches:** file_cluster_0: 13.291, file_cluster_13: 13.561, file_cluster_17: 13.744
- **Magnitude:** 42.64 | **LOC:** 48 | **CtrlFlow:** 47.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.2453%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 38`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` realm, strict, warnings, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/redirect-post.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.179 IQR)
- **Top Global Matches:** file_cluster_0: 13.179, file_cluster_13: 13.201, file_cluster_11: 13.831
- **Magnitude:** 42.56 | **LOC:** 44 | **CtrlFlow:** 56.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.7864%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Request, warnings, JSON::PP, Test::RequiresInternet, LWP::UserAgent, Encode, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/http-post.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.484 IQR)
- **Top Global Matches:** file_cluster_0: 13.484, file_cluster_13: 13.574, file_cluster_11: 14.133
- **Magnitude:** 42.54 | **LOC:** 39 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (93.9388%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 18`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `io: 2`, `import: 7`
* *Defense:* `safety: 2`, `test: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` net, strict, HTTP::Request, warnings, FindBin, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/misc/dbmrobot` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.478 IQR)
- **Top Global Matches:** file_cluster_0: 14.478, file_cluster_13: 14.543, file_cluster_11: 15.077
- **Magnitude:** 39.32 | **LOC:** 23 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (96.2673%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 12`, `args: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, LWP::RobotUA, WWW::RobotRules::AnyDBM_File, URI::URL
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/auth-b.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.559 IQR)
- **Top Global Matches:** file_cluster_0: 13.559, file_cluster_13: 13.775, file_cluster_11: 14.242
- **Magnitude:** 38.7 | **LOC:** 48 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (92.9%), Tech Debt (98.0708%)
**Top Internal Functions/Classes:**
  * `get_basic_credentials` (Impact: 7.0 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 15`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 7`
* *Defense:* `safety: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, HTTP::Request, warnings, parent, Test::RequiresInternet, LWP::UserAgent, Test::More
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/base/protocols.t` (PERL) | Magnitude: 21.32 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 10, structural_boundaries: 8, test: 7, state_mutation: 6
- `t/base/protocols/nntp.t` (PERL) | Magnitude: 20.68 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 12, structural_boundaries: 7, state_mutation: 6, decorators: 5
- `t/base/ua_handlers.t` (PERL) | Magnitude: 66.64 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 45, indent_spaces: 36, branch: 30, structural_boundaries: 19
- `xt/author/live/jigsaw/redirect-post.t` (PERL) | Magnitude: 42.56 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 27, branch: 22, structural_boundaries: 17, decorators: 11
- `t/local/autoload.t` (PERL) | Magnitude: 27.38 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 16, state_mutation: 12, structural_boundaries: 10, decorators: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/local/autoload-get.t` (PERL) | Magnitude: 24.34 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 12, state_mutation: 9, structural_boundaries: 8, decorators: 5
- `xt/author/misc/get-callback` (PERL) | Magnitude: 46.78 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, branch: 14, indent_spaces: 11, structural_boundaries: 10
- `bin/lwp-download` (PERL) | Magnitude: 3123.9 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 190, state_mutation: 189, branch: 113, structural_boundaries: 64
- `t/base/simple.t` (PERL) | Magnitude: 13.64 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 6, structural_boundaries: 4, import: 4, test: 3
- `bin/lwp-mirror` (PERL) | Magnitude: 42.9 | Delta: **0.101 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 39, branch: 32, indent_spaces: 19, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `xt/author/live/jigsaw/chunk.t` (PERL) | Magnitude: 51.48 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 36, branch: 23, structural_boundaries: 12, decorators: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bin/lwp-download` -> **copilot-swe-agent[bot]** (100.0% isolated ownership) | Magnitude: 3123.9
- `t/base/default_content_type.t` -> **copilot-swe-agent[bot]** (100.0% isolated ownership) | Magnitude: 65.08
- `t/base/proxy.t` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 55.44

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/leak/no_leak.t` -> **Severity: 1699.2** (Blast Radius: 16.992 * Doc Risk: 100.0%)
- `xt/author/live/jigsaw/auth-b.t` -> **Severity: 1699.2** (Blast Radius: 16.992 * Doc Risk: 100.0%)
- `t/base/protocols.t` -> **Severity: 1675.302** (Blast Radius: 16.992 * Doc Risk: 98.5936%)
- `xt/author/misc/dbmrobot` -> **Severity: 1675.302** (Blast Radius: 16.992 * Doc Risk: 98.5936%)
- `xt/author/live/jigsaw/auth-d.t` -> **Severity: 1654.006** (Blast Radius: 16.992 * Doc Risk: 97.3403%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
