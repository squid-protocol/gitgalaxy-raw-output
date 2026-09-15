# ARCHITECTURAL_BRIEF: mojo
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/mojolicious/mojo.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 405 |
| Analyzed Artifacts (Scanned) | 315 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 90 |
| Total LOC | 53237 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 77.8% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7604 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1172 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.098 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 14 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 280 | 53128 | 88.9% |
| PLAINTEXT | 22 | 12 | 7.0% |
| JSON | 6 | 30 | 1.9% |
| YAML | 4 | 14 | 1.3% |
| MARKDOWN | 1 | 0 | 0.3% |
| MAKEFILE | 1 | 52 | 0.3% |
| HTML | 1 | 1 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.284`
> **Composition Archetype:** `Small Flat Repo` (z -0.60; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 31%, Large Core Modules 23%, Data / Markup / Trivial 20%, Interface Declarations Files 9%, Compute Cores Files 6%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 292 | 92.7% |
| Unknown | 12 | 3.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 90*

**Composition by Extension & Reason:**
- `.ep`: 12x Excluded (Unsupported Extension: '.ep'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pod`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.epl`: 9x Excluded (Unsupported Extension: '.epl')
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 32.3 | 16.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 97.7 | 51.2 | 60.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.7 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 62.8 | 6.1 | 3.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 19.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.5 | 61.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 59.6 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 79.2 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 54.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1458 | 155 | 11 | `t/mojo/dom.t` |
| cleanup | 275 | 62 | 2 | `t/mojo/ioloop.t` |
| guards | 544 | 110 | 5 | `t/mojo/promise.t` |
| danger | 420 | 103 | 5 | `t/mojo/template.t` |
| concurrency | 1128 | 89 | 11 | `t/mojo/promise.t` |
| connectivity | 2074 | 215 | 16 | `t/mojolicious/lite_app.t` |
| io | 864 | 104 | 9 | `lib/Mojo/UserAgent.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 41 | 30 | 0 | `lib/Mojo/IOLoop/Subprocess.pm` |
| time | 221 | 69 | 3 | `t/mojo/log.t` |
| serialization | 3 | 3 | 0 | `lib/Mojo/IOLoop/Subprocess.pm` |
| regex | 1420 | 142 | 11 | `t/mojolicious/app.t` |
| events | 1253 | 110 | 13 | `t/mojo/eventemitter.t` |
| tests | 3218 | 116 | 28 | `t/mojo/dom.t` |
| docs | 253 | 120 | 1 | `lib/Test/Mojo.pm` |
| debt | 566 | 95 | 5 | `lib/Mojo/UserAgent.pm` |
| mutation | 6704 | 232 | 56 | `t/mojo/dom.t` |
| dead_code | 115 | 59 | 1 | `t/mojolicious/lib/MojoliciousTest/Foo.pm` |
| credential | 8 | 2 | 0 | `t/mojo/request.t` |
| threat | 134 | 103 | 1 | `lib/Mojo/URL.pm` |
| ml_ai | 539 | 62 | 2 | `t/mojo/log.t` |
| ui | 1566 | 99 | 6 | `t/mojo/template.t` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Mojo/UserAgent.pm` (Hits: 75)
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

- `_siblings` **(Many-Argument Workhorses)** (@ `lib/Mojo/DOM.pm`) -> Impact: **421.8** | LOC: 807
- `parse` **(Compute Cores)** (@ `lib/Mojo/Template.pm`) -> Impact: **128.6** | LOC: 112
- `attr` **(Many-Argument Workhorses)** (@ `lib/Mojo/Base.pm`) -> Impact: **89.2** | LOC: 69
- `_compile` **(Compute Cores)** (@ `lib/Mojo/DOM/CSS.pm`) -> Impact: **89.2** | LOC: 58
- `_pc` **(Many-Argument Workhorses)** (@ `lib/Mojo/DOM/CSS.pm`) -> Impact: **88.6** | LOC: 57
- `run` **(Many-Argument Workhorses)** (@ `lib/Mojolicious/Command/get.pm`) -> Impact: **72.8** | LOC: 70
- `parse` **(Compute Cores)** (@ `lib/Mojo/DOM/HTML.pm`) -> Impact: **68.7** | LOC: 73
- `proxy` **(Many-Argument Workhorses)** (@ `t/mojo/lib/Mojo/TestConnectProxy.pm`) -> Impact: **65.8** | LOC: 76
  * *Intent:* # CONNECT proxy server for testing
- `build_frame` **(Many-Argument Workhorses)** (@ `lib/Mojo/WebSocket.pm`) -> Impact: **64.2** | LOC: 39
- `_listen` **(Many-Argument Workhorses)** (@ `lib/Mojo/Server/Daemon.pm`) -> Impact: **63.7** | LOC: 49

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t/mojo/certs` | 10 | 50000.0 | 0.0% | 0.0% |
| `lib/Mojo/IOLoop/resources` | 2 | 10000.0 | 0.0% | 0.0% |
| `t/mojo` | 63 | 7683.28 | 45.5% | 4.05% |
| `lib/Mojo` | 35 | 7275.98 | 54.34% | 6.62% |
| `lib/Mojolicious` | 12 | 1894.92 | 44.79% | 3.22% |
| `t/mojolicious` | 54 | 1844.6 | 10.46% | 0.79% |
| `lib/Test` | 1 | 1073.88 | 26.71% | 0.0% |
| `lib/Mojolicious/Plugin` | 9 | 913.66 | 27.81% | 13.21% |
| `lib/Mojo/DOM` | 2 | 830.66 | 76.31% | 0.0% |
| `lib/Mojo/Server` | 6 | 823.98 | 56.57% | 17.35% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` -> **100.0%** Exposure
- `t/mojo/date.t` -> **99.177%** Exposure
- `t/mojolicious/lib/MojoliciousTest/Controller/Foo/Bar.pm` -> **95.2574%** Exposure
- `t/mojolicious/lib/MojoliciousTest/Exceptional.pm` -> **95.2574%** Exposure
- `lib/Mojolicious/Command/Author/generate/makefile.pm` -> **94.2049%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/Mojo/Content.pm` -> **100.0%** Exposure
- `lib/Mojo/Content/MultiPart.pm` -> **100.0%** Exposure
- `lib/Mojo/Cookie/Response.pm` -> **100.0%** Exposure
- `lib/Mojo/Headers.pm` -> **100.0%** Exposure
- `lib/Mojo/Parameters.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/mojolicious/lib/MojoliciousTest/Foo.pm` -> **16** Orphaned Functions | **0** Duplicates
- `lib/Mojo/Promise.pm` -> **12** Orphaned Functions | **0** Duplicates
- `lib/Mojolicious/Plugin/DefaultHelpers.pm` -> **12** Orphaned Functions | **0** Duplicates
- `lib/Mojolicious/Plugin/TagHelpers.pm` -> **8** Orphaned Functions | **0** Duplicates
- `lib/Mojo/Util.pm` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1755` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/mojo/lib/Mojo/TestConnectProxy.pm` (PERL) -> Cumulative Risk: **735.27**
- **Archetype:** `file_cluster_7` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.39)
- **Magnitude:** 147.98 | **LOC:** 85 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `proxy` (Many-Argument Workhorses, Impact: 65.8)

### 2. `lib/Mojo/Promise.pm` (PERL) -> Cumulative Risk: **724.24**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.09)
- **Magnitude:** 402.18 | **LOC:** 551 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.7869%)
- **Heaviest Functions:** `_all` (Many-Argument Workhorses, Impact: 22.6), `_settle` (Defensive Guards, Impact: 18.9), `map` (Callbacks & Closures, Impact: 14.9)

### 3. `lib/Mojo/IOLoop/TLS.pm` (PERL) -> Cumulative Risk: **685.69**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.35)
- **Magnitude:** 127.48 | **LOC:** 200 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.954%)
- **Heaviest Functions:** `_expand` (Compute Cores, Impact: 23.6), `_tls` (Compute Cores, Impact: 14.6), `negotiate` (Callbacks & Closures, Impact: 9.0)

### 4. `lib/Mojo/IOLoop/Server.pm` (PERL) -> Cumulative Risk: **685.05**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.53)
- **Magnitude:** 194.78 | **LOC:** 295 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9996%), State Flux (99.9989%)
- **Heaviest Functions:** `listen` (Compute Cores, Impact: 57.8), `_accept` (Callbacks & Closures, Impact: 11.0), `DESTROY` (Compute Cores, Impact: 10.1)

### 5. `lib/Mojo/Server/Daemon.pm` (PERL) -> Cumulative Risk: **673.37**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.52)
- **Magnitude:** 322.24 | **LOC:** 528 | **CtrlFlow:** 48.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9963%), Concurrency (99.4897%)
- **Heaviest Functions:** `_listen` (Many-Argument Workhorses, Impact: 63.7), `_build_tx` (Many-Argument Workhorses, Impact: 28.9), `_write` (Compute Cores, Impact: 21.5)

### 6. `lib/Mojo/UserAgent/Server.pm` (PERL) -> Cumulative Risk: **666.57**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.57)
- **Magnitude:** 114.74 | **LOC:** 128 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9998%)
- **Heaviest Functions:** `_url` (Compute Cores, Impact: 39.1), `app` (Compute Cores, Impact: 11.0), `nb_url` (Interface Declarations, Impact: 1.5)

### 7. `lib/Mojo/IOLoop/Client.pm` (PERL) -> Cumulative Risk: **661.13**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +2.07)
- **Magnitude:** 195.86 | **LOC:** 350 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8818%), State Flux (99.866%)
- **Heaviest Functions:** `connect` (Compute Cores, Impact: 29.2), `_connect` (Compute Cores, Impact: 25.7), `_try_socks` (Compute Cores, Impact: 11.1)

### 8. `lib/Mojo/IOLoop.pm` (PERL) -> Cumulative Risk: **659.16**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.27)
- **Magnitude:** 285.26 | **LOC:** 552 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (97.3549%)
- **Heaviest Functions:** `_remove` (Compute Cores, Impact: 18.1), `_stream` (Many-Argument Workhorses, Impact: 14.0), `server` (Compute Cores, Impact: 8.3)

### 9. `lib/Mojo/IOLoop/Stream.pm` (PERL) -> Cumulative Risk: **658.02**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.55)
- **Magnitude:** 172.42 | **LOC:** 328 | **CtrlFlow:** 30.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.8756%), State Flux (99.5298%)
- **Heaviest Functions:** `_read` (Compute Cores, Impact: 13.4), `timeout` (Compute Cores, Impact: 11.3), `_write` (Compute Cores, Impact: 10.7)

### 10. `lib/Mojo/Util.pm` (PERL) -> Cumulative Risk: **652.93**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.12)
- **Magnitude:** 618.52 | **LOC:** 1064 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%), Safety Score (88.7333%)
- **Heaviest Functions:** `punycode_encode` (Compute Cores, Impact: 32.0), `network_contains` (Compute Cores, Impact: 27.0), `_entity` (Compute Cores, Impact: 24.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `lib/Mojo/IOLoop/resources/server.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `lib/Test/Mojo.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1073.88 | **LOC:** 1354 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.7123%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_message` **(Compute Cores)** (Impact: 25.4)
  * `new` **(Defensive Guards)** (Impact: 18.5)
  * `_request_ok` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `json_is` **(Many-Argument Workhorses)** (Impact: 11.6)
  * `json_message_is` **(Many-Argument Workhorses)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 169 instances
* *Concurrency (weighted view):* 60
* *State Mutation (weighted view):* 555
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 349`, `args: 111`, `func_start: 84`, `class_start: 1`
* *Risk/State:* `state_mutation: 217`, `planned_debt: 1`
* *Architecture:* `io: 43`, `api: 72`, `concurrency: 15`, `import: 30`
* *Defense:* `safety: 1`, `doc: 33`, `test: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::File, Mojo::IOLoop, Mojo::JSON, Mojo::JSON::Pointer, Mojo::Server, Mojo::UserAgent, Mojo::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/DOM.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 915.3 | **LOC:** 1109 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.6186%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_siblings` **(Many-Argument Workhorses)** (Impact: 421.8)
  * `val` **(Compute Cores)** (Impact: 26.4)
  * `_text` **(Compute Cores)** (Impact: 20.9)
  * `_wrap` **(Compute Cores)** (Impact: 19.2)
  * `namespace` **(Compute Cores)** (Impact: 16.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 327`, `args: 48`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `state_mutation: 65`
* *Architecture:* `api: 43`, `import: 15`
* *Defense:* `safety: 2`, `doc: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::Collection, Mojo::DOM, Mojo::DOM::CSS, Mojo::DOM::HTML, Scalar::Util, Storable, it...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/promise.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 802.98 | **LOC:** 558 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 102 instances
* *Amplified Cascading Flux:* 18 instances
* *Concurrency (weighted view):* 647
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 320`, `args: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 95`
* *Architecture:* `concurrency: 137`, `import: 12`
* *Defense:* `safety: 36`, `test: 111`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::IOLoop, Scalar::Util, Test::More, more, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/dom.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 671.16 | **LOC:** 3104 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.1866%), Tech Debt (10.7199%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 173 instances
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 605`, `structural_boundaries: 637`, `args: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 251`, `fragile_debt: 7`
* *Architecture:* `io: 9`, `import: 174`
* *Defense:* `safety: 2`, `test: 266`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Mojo::Base, Mojo::DOM, Mojo::DOM::HTML, Test::More, attribute, attributes, changes, children...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 618.52 | **LOC:** 1064 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.7984%), Tech Debt (16.5654%)
**Top Internal Functions/Classes:**
  * `punycode_encode` **(Compute Cores)** (Impact: 32.0)
    * *Intent:* # Direct translation of RFC 3492
  * `network_contains` **(Compute Cores)** (Impact: 27.0)
  * `_entity` **(Compute Cores)** (Impact: 24.8)
  * `_header` **(Compute Cores)** (Impact: 22.1)
  * `punycode_decode` **(Compute Cores)** (Impact: 21.3)
    * *Intent:* # Direct translation of RFC 3492
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 338`, `args: 42`, `func_start: 47`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 85`, `unreferenced_by_name: 5`
* *Architecture:* `io: 5`, `api: 39`, `import: 35`
* *Defense:* `safety: 12`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Crypt::AuthEnc::ChaCha20Poly1305, Crypt::KeyDerivation, Crypt::Misc, Crypt::PRNG, CryptX, Data::Dumper, Digest::MD5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/DOM/CSS.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 565.12 | **LOC:** 759 | **CtrlFlow:** 84.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_compile` **(Compute Cores)** (Impact: 89.2)
  * `_pc` **(Many-Argument Workhorses)** (Impact: 88.6)
  * `_equation` **(Compute Cores)** (Impact: 34.7)
  * `_value` **(Compute Cores)** (Impact: 33.1)
  * `_selector` **(Compute Cores)** (Impact: 32.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 265`, `args: 20`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `io: 57`, `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Mojo::Base, Mojo::DOM::CSS, Mojo::Util, children, constant, namespace, the
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/UserAgent.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 496.22 | **LOC:** 997 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.2181%), Tech Debt (9.6286%)
**Top Internal Functions/Classes:**
  * `_connect` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `_connection` **(Compute Cores)** (Impact: 41.5)
  * `_start` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `_dequeue` **(Compute Cores)** (Impact: 25.4)
  * `_finish` **(Compute Cores)** (Impact: 25.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 57
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 322`, `structural_boundaries: 328`, `args: 74`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `unreferenced_by_name: 1`
* *Architecture:* `io: 75`, `api: 7`, `concurrency: 42`, `import: 14`
* *Defense:* `safety: 10`, `doc: 20`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Mojo::Base, Mojo::IOLoop, Mojo::Promise, Mojo::UserAgent, Mojo::UserAgent::CookieJar, Mojo::UserAgent::Proxy, Mojo::UserAgent::Server, Mojo::UserAgent::Transactor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/ioloop.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 485.36 | **LOC:** 394 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9992%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 62 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 400
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 171`, `args: 28`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `io: 2`, `concurrency: 90`, `import: 17`
* *Defense:* `safety: 2`, `test: 28`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IO::Socket::IP, Mojo::Base, Mojo::IOLoop, Mojo::IOLoop::Client, Mojo::IOLoop::Server, Mojo::IOLoop::Stream, Mojo::Promise, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 444.54 | **LOC:** 673 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.084%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 128.6)
  * `_compile` **(Compute Cores)** (Impact: 49.6)
  * `process` **(Defensive Guards)** (Impact: 11.5)
  * `_wrap` **(Many-Argument Workhorses)** (Impact: 11.0)
  * `_trim` **(Compute Cores)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 208
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 138`, `args: 19`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 80`
* *Architecture:* `io: 2`, `api: 4`, `import: 15`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Mojo::Base, Mojo::ByteStream, Mojo::Exception, Mojo::File, Mojo::Template, Mojo::Util, Time::Piece...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Content.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 436.38 | **LOC:** 608 | **CtrlFlow:** 39.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.4467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` **(Compute Cores)** (Impact: 39.7)
  * `_parse_chunked` **(Compute Cores)** (Impact: 29.8)
  * `_decompress` **(Compute Cores)** (Impact: 14.8)
  * `generate_body_chunk` **(Compute Cores)** (Impact: 14.4)
  * `write_chunk` **(Compute Cores)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 188`, `args: 42`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `state_mutation: 68`
* *Architecture:* `io: 7`, `api: 28`, `import: 7`
* *Defense:* `safety: 4`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.382
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004246
  * `Imports (Out-Degree: 0):` Carp, Compress::Raw::Zlib, Mojo::Base, Mojo::Headers, Mojo::SSE, Scalar::Util, leading
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Mojolicious/Controller.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 419.06 | **LOC:** 968 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.4842%), Tech Debt (9.9312%)
**Top Internal Functions/Classes:**
  * `render` **(Compute Cores)** (Impact: 27.5)
  * `url_for` **(Compute Cores)** (Impact: 24.4)
  * `rendered` **(Compute Cores)** (Impact: 22.2)
  * `every_signed_cookie` **(Compute Cores)** (Impact: 18.6)
  * `send` **(Defensive Guards)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 306`, `args: 57`, `func_start: 30`, `class_start: 2`
* *Risk/State:* `state_mutation: 57`, `unreferenced_by_name: 1`
* *Architecture:* `io: 11`, `api: 30`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 9`, `doc: 13`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carp, Digest::SHA, L, Mojo::Base, Mojo::ByteStream, Mojo::DynamicMethods, Mojo::JSON, Mojo::URL...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mojo/user_agent.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 413.84 | **LOC:** 743 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7076%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 39 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 236
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 140
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 180`, `args: 38`
* *Risk/State:* `state_mutation: 106`
* *Architecture:* `io: 32`, `api: 10`, `concurrency: 41`, `import: 43`
* *Defense:* `safety: 4`, `test: 25`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Mojo::Base, Mojo::IOLoop, Mojo::Message::Request, Mojo::Promise, Mojo::Server::Daemon, Mojo::UserAgent, Mojo::UserAgent::Server, Mojo::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Mojo/Promise.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 402.18 | **LOC:** 551 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.0907%), Tech Debt (70.352%)
**Top Internal Functions/Classes:**
  * `_all` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `_settle` **(Defensive Guards)** (Impact: 18.9)
  * `map` **(Callbacks & Closures)** (Impact: 14.9)
  * `_finally` **(Defensive Guards)** (Impact: 12.0)
  * `AWAIT_GET` **(Defensive Guards)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 115
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 229`, `args: 46`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `state_mutation: 33`, `unreferenced_by_name: 12`
* *Architecture:* `io: 4`, `api: 29`, `concurrency: 50`, `import: 8`
* *Defense:* `safety: 21`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.875
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Mojo::Base, Mojo::Exception, Mojo::IOLoop, Mojo::Promise, Mojo::UserAgent, Scalar::Util, constant
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/Mojo/Util.pm` -> Churn: **79.25%** | Cog Load: 77.7984% | Debt: 16.5654%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/Mojo/Util.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 618.52
- `lib/Mojolicious/Controller.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 419.06
- `t/mojo/ioloop_tls.t` -> **Alexander Karelas** (100.0% isolated ownership) | Magnitude: 316.94
- `lib/Mojo/IOLoop.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 285.26
- `lib/Mojo/Base.pm` -> **Sebastian Riedel** (100.0% isolated ownership) | Magnitude: 254.42

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/mojo/response.t` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 83.7746%)
- `t/mojo/exception.t` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.9626%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/mojo/content.t` -> **Severity: 1.579** (Embedded: 0.0321 * Error Risk: 49.18%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 1.556** (Embedded: 0.0191 * Error Risk: 81.4527%)
- `lib/Mojolicious.pm` -> **Severity: 1.45** (Embedded: 0.0223 * Error Risk: 65.0625%)
- `lib/Mojo/URL.pm` -> **Severity: 0.842** (Embedded: 0.0096 * Error Risk: 88.1761%)
- `t/mojo/path.t` -> **Severity: 0.52** (Embedded: 0.0096 * Error Risk: 54.4483%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Mojolicious.pm` -> **Severity: 1835.6** (Blast Radius: 18.356 * Doc Risk: 100.0%)
- `lib/Mojolicious/Plugin/Config.pm` -> **Severity: 1631.9** (Blast Radius: 16.319 * Doc Risk: 100.0%)
- `lib/Mojo/Reactor/EV.pm` -> **Severity: 776.4** (Blast Radius: 7.764 * Doc Risk: 100.0%)
- `t/mojo/exception.t` -> **Severity: 776.4** (Blast Radius: 7.764 * Doc Risk: 100.0%)
- `lib/Mojo/URL.pm` -> **Severity: 694.9** (Blast Radius: 6.949 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
