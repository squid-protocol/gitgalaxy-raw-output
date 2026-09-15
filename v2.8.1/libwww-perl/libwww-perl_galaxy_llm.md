# ARCHITECTURAL_BRIEF: libwww-perl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/libwww-perl/libwww-perl.git` |
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
| Total Artifacts | 100 |
| Analyzed Artifacts (Scanned) | 60 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 40 |
| Total LOC | 3961 |
| Volatility Index | 0.017 |
| % Scanned of codebase = | 60.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 0 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 53 | 3937 | 88.3% |
| MARKDOWN | 3 | 0 | 5.0% |
| SHELL | 2 | 8 | 3.3% |
| PLAINTEXT | 1 | 0 | 1.7% |
| YAML | 1 | 16 | 1.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z -1.16; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 58%, Data / Markup / Trivial 13%, Large Core Modules 8%, Interface Declarations Files 5%, Compute Cores Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 56 | 93.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 6.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 40*

**Composition by Extension & Reason:**
- `.pm`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1050 LOC)
- `.pl`: 1x Excluded (Machine-Generated Source Code Signature: 17 LOC)
- `.ssl`: 1x Excluded (Unsupported Extension: '.SSL')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.pl_dist`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 88.1 | 23.6 | 12.3 | 6.4 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.9 | 41.2 | 55.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.4 | 1.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 41.2 | 2.0 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 44.8 | 35.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 52.6 | 1.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.4 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 33.3 | 0.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 26.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 97 | 23 | 3 | `t/10-attrs.t` |
| cleanup | 17 | 10 | 1 | `t/local/http.t` |
| guards | 121 | 53 | 2 | `lwptut.pod` |
| danger | 131 | 23 | 9 | `bin/lwp-download` |
| concurrency | 5 | 4 | 0 | `xt/author/net/cgi-bin/slowread` |
| connectivity | 49 | 16 | 2 | `t/local/httpsub.t` |
| io | 211 | 50 | 8 | `lwptut.pod` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `bin/lwp-request` |
| time | 23 | 10 | 1 | `bin/lwp-request` |
| serialization | 0 | 0 | 0 | - |
| regex | 132 | 23 | 6 | `t/local/http.t` |
| events | 4 | 2 | 0 | `lwptut.pod` |
| tests | 367 | 40 | 10 | `t/local/http.t` |
| docs | 46 | 6 | 0 | `lwptut.pod` |
| debt | 138 | 21 | 6 | `t/local/http.t` |
| mutation | 429 | 48 | 16 | `t/local/http.t` |
| dead_code | 20 | 9 | 1 | `t/local/httpsub.t` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 2 | 0 | `bin/lwp-download` |
| ml_ai | 13 | 6 | 0 | `bin/lwp-download` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

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

- `daemonize` **(Many-Argument Workhorses)** (@ `t/local/http.t`) -> Impact: **371.5** | LOC: 213
- `_test` **(Tests & Verification)** (@ `t/local/http.t`) -> Impact: **177.6** | LOC: 431
- `daemonize` **(Many-Argument Workhorses)** (@ `t/robot/ua-get.t`) -> Impact: **41.5** | LOC: 46
- `daemonize` **(Many-Argument Workhorses)** (@ `t/robot/ua.t`) -> Impact: **41.5** | LOC: 46
- `_test` **(Tests & Verification)** (@ `t/robot/ua-get.t`) -> Impact: **36.0** | LOC: 60
- `request` **(Many-Argument Workhorses)** (@ `t/local/protosub.t`) -> Impact: **21.9** | LOC: 15
- `_test` **(Tests & Verification)** (@ `t/robot/ua.t`) -> Impact: **19.8** | LOC: 56
- `get_basic_credentials` **(Compute Cores)** (@ `bin/lwp-request`) -> Impact: **19.1** | LOC: 23
- `show` **(Compute Cores)** (@ `bin/lwp-request`) -> Impact: **12.5** | LOC: 8
- `usage` **(I/O & Config Routines)** (@ `bin/lwp-request`) -> Impact: **10.4** | LOC: 29

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Tests & Verification**: assertion-heavy test or verification function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t/local` | 8 | 895.04 | 25.9% | 21.64% |
| `__monolith__` | 8 | 299.18 | 13.5% | 4.2% |
| `bin` | 4 | 277.88 | 37.58% | 2.76% |
| `t/base` | 7 | 226.68 | 39.19% | 0.0% |
| `t/robot` | 2 | 218.28 | 66.96% | 0.0% |
| `xt/author/live/jigsaw` | 9 | 156.4 | 16.99% | 16.25% |
| `xt/author/net` | 7 | 131.28 | 16.46% | 0.0% |
| `xt/author/misc` | 3 | 49.84 | 15.45% | 0.0% |
| `t` | 2 | 40.38 | 33.17% | 0.0% |
| `xt/author/net/cgi-bin` | 4 | 31.8 | 7.45% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/local/httpsub.t` -> **99.9924%** Exposure
- `t/local/download_to_fh.t` -> **73.1059%** Exposure
- `xt/author/live/jigsaw/auth-b.t` -> **73.1059%** Exposure
- `xt/author/live/jigsaw/auth-d.t` -> **73.1059%** Exposure
- `lwpcook.pod` -> **33.6348%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/base/ua.t` -> **100.0%** Exposure
- `lwpcook.pod` -> **99.997%** Exposure
- `bin/lwp-download` -> **99.9919%** Exposure
- `t/robot/ua.t` -> **99.9689%** Exposure
- `xt/author/live/jigsaw/auth-b.t` -> **99.9665%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/local/httpsub.t` -> **8** Orphaned Functions | **0** Duplicates
- `bin/lwp-request` -> **1** Orphaned Functions | **0** Duplicates
- `xt/author/live/jigsaw/auth-b.t` -> **1** Orphaned Functions | **0** Duplicates
- `xt/author/live/jigsaw/auth-d.t` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `361` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `xt/author/live/jigsaw/auth-b.t` (PERL) -> Cumulative Risk: **499.82**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.44)
- **Magnitude:** 18.2 | **LOC:** 48 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9665%), Tech Debt (73.1059%)
- **Heaviest Functions:** `get_basic_credentials` (Defensive Guards, Impact: 2.5)

### 2. `t/local/http.t` (PERL) -> Cumulative Risk: **496.43**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z +1.56)
- **Magnitude:** 740.68 | **LOC:** 749 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8671%), Cognitive Load (82.6995%)
- **Heaviest Functions:** `daemonize` (Many-Argument Workhorses, Impact: 371.5), `_test` (Tests & Verification, Impact: 177.6), `get_basic_credentials` (Parameter Forwarders, Impact: 7.1)

### 3. `bin/lwp-download` (PERL) -> Cumulative Risk: **470.24**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.97)
- **Magnitude:** 107.98 | **LOC:** 336 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9919%), Safety Score (91.2365%)
- **Heaviest Functions:** `fduration` (Compute Cores, Impact: 6.6), `fbytes` (Type Conversions, Impact: 6.3), `show` (Compute Cores, Impact: 5.6)

### 4. `t/robot/ua-get.t` (PERL) -> Cumulative Risk: **464.71**
- **Archetype:** `file_cluster_16` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.49)
- **Magnitude:** 117.26 | **LOC:** 149 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9634%), Safety Score (88.4987%)
- **Heaviest Functions:** `daemonize` (Many-Argument Workhorses, Impact: 41.5), `_test` (Tests & Verification, Impact: 36.0), `url` (Interface Declarations, Impact: 2.2)

### 5. `bin/lwp-request` (PERL) -> Cumulative Risk: **462.85**
- **Archetype:** `file_cluster_3` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.88)
- **Magnitude:** 149.64 | **LOC:** 566 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8366%), Safety Score (81.8181%)
- **Heaviest Functions:** `get_basic_credentials` (Compute Cores, Impact: 19.1), `show` (Compute Cores, Impact: 12.5), `usage` (I/O & Config Routines, Impact: 10.4)

### 6. `t/robot/ua.t` (PERL) -> Cumulative Risk: **455.75**
- **Archetype:** `file_cluster_16` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.46)
- **Magnitude:** 101.02 | **LOC:** 146 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9689%), Safety Score (89.3145%)
- **Heaviest Functions:** `daemonize` (Many-Argument Workhorses, Impact: 41.5), `_test` (Tests & Verification, Impact: 19.8), `url` (Interface Declarations, Impact: 2.2)

### 7. `xt/author/misc/get-callback` (PERL) -> Cumulative Risk: **405.56**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.10)
- **Magnitude:** 16.28 | **LOC:** 30 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1837%), Safety Score (71.9676%)
- **Heaviest Functions:** `data` (Compute Cores, Impact: 5.8)

### 8. `bin/lwp-mirror` (PERL) -> Cumulative Risk: **405.22**
- **Archetype:** `file_cluster_1` (Distance: N/A IQR)
- **Composition Archetype:** `I/O & Config Routines Files` (z +1.64)
- **Magnitude:** 13.9 | **LOC:** 104 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (91.6827%), Safety Score (84.457%)
- **Heaviest Functions:** `usage` (I/O & Config Routines, Impact: 2.4)

### 9. `t/local/httpsub.t` (PERL) -> Cumulative Risk: **397.93**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +0.19)
- **Magnitude:** 33.56 | **LOC:** 93 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9924%), Safety Score (54.2904%)
- **Heaviest Functions:** `new` (Type Conversions, Impact: 1.6), `format_request` (Interface Declarations, Impact: 1.6), `syswrite` (Interface Declarations, Impact: 1.6)

### 10. `t/base/ua_handlers.t` (PERL) -> Cumulative Risk: **390.42**
- **Archetype:** `file_cluster_9` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.60)
- **Magnitude:** 13.64 | **LOC:** 66 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.0464%), Safety Score (57.094%)
- **Heaviest Functions:** `ua` (Callbacks & Closures, Impact: 2.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `t/local/http.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 740.68 | **LOC:** 749 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.6995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 371.5)
  * `_test` **(Tests & Verification)** (Impact: 177.6)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 11
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 164`, `args: 21`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 53`
* *Architecture:* `io: 11`, `api: 10`, `import: 16`
* *Defense:* `safety: 2`, `test: 94`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Config, FindBin, HTTP::Cookies, HTTP::Daemon, HTTP::Request, LWP::UserAgent, Test::Fatal, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-request` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 149.64 | **LOC:** 566 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.6861%), Tech Debt (11.0533%)
**Top Internal Functions/Classes:**
  * `get_basic_credentials` **(Compute Cores)** (Impact: 19.1)
  * `show` **(Compute Cores)** (Impact: 12.5)
  * `usage` **(I/O & Config Routines)** (Impact: 10.4)
  * `new` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 31 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 31`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 5`, `import: 23`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, Encode::Locale, Getopt::Long, HTML::FormatPS, HTML::FormatText, HTML::Parse, HTTP::Date, HTTP::Status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua-get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 117.26 | **LOC:** 149 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8594%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `_test` **(Tests & Verification)** (Impact: 36.0)
  * `url` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 45`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Config, FindBin, HTTP::Daemon, LWP::RobotUA, Test::More, URI, strict, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-download` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 107.98 | **LOC:** 336 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.7829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fduration` **(Compute Cores)** (Impact: 6.6)
  * `fbytes` **(Type Conversions)** (Impact: 6.3)
  * `show` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 69`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 27`, `dead_code: 1`
* *Architecture:* `io: 9`, `api: 3`, `import: 14`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, Encode::Locale, Fcntl, File::Spec, Getopt::Long, HTTP, HTTP::Date, LWP::MediaTypes...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwptut.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 105.42 | **LOC:** 821 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.2123%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 89`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `io: 25`, `import: 31`
* *Defense:* `safety: 8`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::CookieJar::LWP, HTTP::Request::Common, LWP, LWP::ConnCache, LWP::RobotUA, LWP::Simple, LWP::UserAgent, URI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 101.02 | **LOC:** 146 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.0592%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `_test` **(Tests & Verification)** (Impact: 19.8)
  * `url` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 48`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 2`, `import: 10`
* *Defense:* `safety: 2`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Config, FindBin, HTTP::Daemon, HTTP::Request, LWP::RobotUA, Test::More, URI, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 98.2 | **LOC:** 207 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 35`, `args: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `io: 22`, `import: 6`
* *Defense:* `safety: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::UserAgent, Test::More, strict, undef, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwpcook.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 85.12 | **LOC:** 311 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.4737%), Tech Debt (33.6348%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 41`, `args: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `import: 27`
* *Defense:* `safety: 2`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTP::CookieJar::LWP, HTTP::Request::Common, LWP::Simple, LWP::UserAgent, SSL, proxies, se, simple...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 49.36 | **LOC:** 2468 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/cache-timeouts.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 37.38 | **LOC:** 94 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 19`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 7`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FindBin, HTTP::Request, LWP::ConnCache, LWP::UserAgent, Test::More, net, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/httpsub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 33.56 | **LOC:** 93 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6854%), Tech Debt (99.9924%)
**Top Internal Functions/Classes:**
  * `new` **(Type Conversions)** (Impact: 1.6)
  * `format_request` **(Interface Declarations)** (Impact: 1.6)
  * `syswrite` **(Interface Declarations)** (Impact: 1.6)
  * `read_response_headers` **(Interface Declarations)** (Impact: 1.6)
  * `read_entity_body` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 47`, `args: 10`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2`, `unreferenced_by_name: 8`
* *Architecture:* `io: 3`, `api: 13`, `import: 9`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::Protocol, LWP::UserAgent, Test::More, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/proxy.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 32.44 | **LOC:** 85 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (67.3096%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 39`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 8`, `import: 6`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, Test::Fatal, Test::More, errors, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/default_content_type.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 31.08 | **LOC:** 141 | **CtrlFlow:** 49.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (50.9614%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 29`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::UserAgent, Test::More, default, strict, the, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/protosub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 29.5 | **LOC:** 58 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1851%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `new` **(Annotated Framework Methods)** (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 19`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `dead_code: 2`
* *Architecture:* `io: 2`, `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::Protocol, LWP::UserAgent, Test::More, parent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/cookie_jar.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 27.64 | **LOC:** 43 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.8646%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 7`
* *Risk/State:* `state_mutation: 4`
* *Architecture:* `io: 7`, `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::Fatal, Test::More, cookie, cookie_jar, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/10-attrs.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 24.64 | **LOC:** 48 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.8259%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 38`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, Test::More, realm, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/chunk.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 24.48 | **LOC:** 35 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.1535%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::UserAgent, Test::More, Test::RequiresInternet, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/cgi-bin/slowread` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 24.46 | **LOC:** 34 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.8667%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 9`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 3`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/proxy_request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 22.36 | **LOC:** 85 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.5015%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 5`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* `io: 2`, `import: 4`
* *Defense:* `safety: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/download_to_fh.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 21.62 | **LOC:** 42 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.3647%), Tech Debt (73.1059%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 2`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, LWP::Simple, LWP::UserAgent, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/redirect-post.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 21.56 | **LOC:** 44 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1871%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, HTTP::Request, JSON::PP, LWP::UserAgent, Test::More, Test::RequiresInternet, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 20.36 | **LOC:** 1018 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `talk-to-ourself` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 18.78 | **LOC:** 51 | **CtrlFlow:** 64.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.2852%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 1
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 12`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 1`
* *Architecture:* `io: 10`, `import: 4`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IO::Select, IO::Socket, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/te.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 18.62 | **LOC:** 40 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.1871%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 13`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Request, LWP::UserAgent, Test::More, Test::RequiresInternet, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/md5-get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 18.54 | **LOC:** 33 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.1851%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.434
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Digest::MD5, LWP::UserAgent, Test::More, Test::RequiresInternet, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `bin/lwp-download` -> **Severity: 1643.4** (Blast Radius: 16.434 * Doc Risk: 100.0%)
- `bin/lwp-dump` -> **Severity: 1643.4** (Blast Radius: 16.434 * Doc Risk: 100.0%)
- `bin/lwp-mirror` -> **Severity: 1643.4** (Blast Radius: 16.434 * Doc Risk: 100.0%)
- `bin/lwp-request` -> **Severity: 1643.4** (Blast Radius: 16.434 * Doc Risk: 100.0%)
- `t/base/ua_handlers.t` -> **Severity: 1643.4** (Blast Radius: 16.434 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
