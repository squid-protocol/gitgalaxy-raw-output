# ARCHITECTURAL_BRIEF: libwww-perl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/libwww-perl` |
| **Timestamp** | `2026-08-07T03:51:55.568563+00:00` |
| **Scan Duration** | `0.23s` |
| **Git Branch** | `master` |
| **Git Commit** | `7420d1bfff7cd5369ca24e87c37edf97b2cbb0c1` |
| **Git Remote** | `https://github.com/libwww-perl/libwww-perl.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1 malicious artifacts.

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
| Cognitive Load Exposure | 5.0 | 96.2 | 65.1 | 82.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.0 | 83.3 | 86.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 2.5 | 1.3 | 2.0 | 0.0 |
| API Exposure | 0.0 | 1.1 | 0.1 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 92.2 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 52.6 | 1.9 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 94.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.0 | 0.1 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 28.9 | 1.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 95.0 | 44.2 | 49.0 | 11.9 |
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

- `_test` (@ `t/local/http.t`) -> Impact: **176.6** | LOC: 431
- `daemonize` (@ `t/local/http.t`) -> Impact: **125.2** | LOC: 218
- `_test` (@ `t/robot/ua-get.t`) -> Impact: **36.0** | LOC: 60
- `daemonize` (@ `t/robot/ua-get.t`) -> Impact: **30.0** | LOC: 46
- `daemonize` (@ `t/robot/ua.t`) -> Impact: **30.0** | LOC: 46
- `_test` (@ `t/robot/ua.t`) -> Impact: **19.8** | LOC: 56
- `get_basic_credentials` (@ `bin/lwp-request`) -> Impact: **19.1** | LOC: 23
- `request` (@ `t/local/protosub.t`) -> Impact: **12.1** | LOC: 15
- `show` (@ `bin/lwp-request`) -> Impact: **10.3** | LOC: 8
- `get_basic_credentials` (@ `t/local/http.t`) -> Impact: **7.1** | LOC: 7

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `bin` | 4 | 2862.31 | 48.2% | 3.07% |
| `t/local` | 8 | 875.2 | 84.58% | 28.99% |
| `__monolith__` | 8 | 462.12 | 25.86% | 4.94% |
| `t/base` | 7 | 307.68 | 66.46% | 0.0% |
| `xt/author/live/jigsaw` | 9 | 292.8 | 68.58% | 21.99% |
| `t/robot` | 2 | 287.28 | 85.49% | 0.0% |
| `xt/author/net` | 6 | 231.76 | 84.24% | 0.0% |
| `xt/author/misc` | 3 | 105.94 | 59.97% | 0.0% |
| `t` | 2 | 56.38 | 70.61% | 0.0% |
| `xt/author/net/cgi-bin` | 3 | 50.3 | 57.35% | 33.33% |

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `354` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `xt/author/live/jigsaw/auth-b.t` (PERL) -> Cumulative Risk: **582.26**
- **Archetype:** `file_cluster_0` (Distance: 13.467 IQR)
- **Magnitude:** 36.4 | **LOC:** 48 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.0708%), Documentation (94.9621%)
- **Heaviest Functions:** `get_basic_credentials` (Impact: 4.7)

### 2. `xt/author/live/jigsaw/auth-d.t` (PERL) -> Cumulative Risk: **551.57**
- **Archetype:** `file_cluster_0` (Distance: 13.676 IQR)
- **Magnitude:** 24.2 | **LOC:** 37 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8499%), Cognitive Load (87.2138%)
- **Heaviest Functions:** `get_basic_credentials` (Impact: 4.7)

### 3. `t/local/httpsub.t` (PERL) -> Cumulative Risk: **517.14**
- **Archetype:** `file_cluster_0` (Distance: 11.788 IQR)
- **Magnitude:** 52.56 | **LOC:** 93 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (85.2156%)
- **Heaviest Functions:** `new` (Impact: 1.6), `format_request` (Impact: 1.6), `syswrite` (Impact: 1.6)

### 4. `t/local/download_to_fh.t` (PERL) -> Cumulative Risk: **515.35**
- **Archetype:** `file_cluster_0` (Distance: 11.698 IQR)
- **Magnitude:** 31.62 | **LOC:** 42 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.1491%), Safety Score (86.6526%)

### 5. `t/local/protosub.t` (PERL) -> Cumulative Risk: **482.23**
- **Archetype:** `file_cluster_0` (Distance: 16.293 IQR)
- **Magnitude:** 41.0 | **LOC:** 58 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (88.0797%), Safety Score (86.1762%)
- **Heaviest Functions:** `request` (Impact: 12.1), `new` (Impact: 3.1)

### 6. `t/leak/no_leak.t` (PERL) -> Cumulative Risk: **466.23**
- **Archetype:** `file_cluster_0` (Distance: 11.959 IQR)
- **Magnitude:** 21.36 | **LOC:** 27 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Documentation (94.3304%), Cognitive Load (84.1131%)

### 7. `xt/author/misc/dbmrobot` (PERL) -> Cumulative Risk: **451.7**
- **Archetype:** `file_cluster_0` (Distance: 13.908 IQR)
- **Magnitude:** 33.32 | **LOC:** 23 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (95.6893%), Cognitive Load (85.1953%)

### 8. `xt/author/live/jigsaw/chunk.t` (PERL) -> Cumulative Risk: **446.77**
- **Archetype:** `file_cluster_17` (Distance: 14.378 IQR)
- **Magnitude:** 51.48 | **LOC:** 35 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.6402%), Cognitive Load (91.16%)

### 9. `xt/author/misc/get-callback` (PERL) -> Cumulative Risk: **446.73**
- **Archetype:** `file_cluster_13` (Distance: 13.741 IQR)
- **Magnitude:** 36.38 | **LOC:** 30 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.7327%), Cognitive Load (89.7216%)
- **Heaviest Functions:** `data` (Impact: 5.9)

### 10. `t/base/proxy.t` (PERL) -> Cumulative Risk: **444.46**
- **Archetype:** `file_cluster_0` (Distance: 11.182 IQR)
- **Magnitude:** 49.44 | **LOC:** 85 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (88.6508%), Safety Score (85.209%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/lwp-download` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.652 IQR)
- **Top Global Matches:** file_cluster_13: 12.652, file_cluster_0: 12.701, file_cluster_8: 12.875
- **Magnitude:** 2583.01 | **LOC:** 336 | **CtrlFlow:** 56.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.6819%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 69`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 187`, `dead_code: 1`
* *Architecture:* `io: 10`, `import: 14`
* *Defense:* `safety: 2`, `doc: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, Fcntl, acceptable, HTTP::Date, File::Spec, LWP::UserAgent, Encode, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/http.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.474 IQR)
- **Top Global Matches:** file_cluster_0: 12.474, file_cluster_13: 12.98, file_cluster_8: 12.982
- **Magnitude:** 632.34 | **LOC:** 749 | **CtrlFlow:** 59.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.1962%), Tech Debt (32.7407%)
**Top Internal Functions/Classes:**
  * `_test` (Impact: 176.6)
  * `daemonize` (Impact: 125.2)
  * `get_basic_credentials` (Impact: 7.1)
  * `get_basic_credentials` (Impact: 7.1)
  * `get_basic_credentials` (Impact: 7.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 164`, `args: 21`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 288`, `duplicate_logic: 4`
* *Architecture:* `io: 14`, `api: 4`, `import: 16`
* *Defense:* `safety: 2`, `test: 94`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, point, strict, parent, FindBin, HTTP::Request, HTTP::Daemon, LWP::UserAgent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwptut.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.633 IQR)
- **Top Global Matches:** file_cluster_0: 12.633, file_cluster_13: 12.732, file_cluster_8: 12.918
- **Magnitude:** 219.38 | **LOC:** 821 | **CtrlFlow:** 71.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2351%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 87`, `class_start: 1`
* *Risk/State:* `state_mutation: 194`
* *Architecture:* `io: 25`, `import: 31`
* *Defense:* `safety: 8`, `doc: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP, strict, LWP::RobotUA, HTTP::Request::Common, HTTP::CookieJar::LWP, proxies, an, the...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-request` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.162 IQR)
- **Top Global Matches:** file_cluster_0: 12.162, file_cluster_13: 12.195, file_cluster_8: 12.569
- **Magnitude:** 179.04 | **LOC:** 566 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4117%), Tech Debt (12.273%)
**Top Internal Functions/Classes:**
  * `get_basic_credentials` (Impact: 19.1)
  * `show` (Impact: 10.3)
  * `new` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 99`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 139`, `dead_code: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 6`, `api: 1`, `import: 23`
* *Defense:* `safety: 6`, `doc: 32`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Date, HTML::FormatText, warnings, HTML::Parse, HTML::FormatPS, method, for, Getopt::Long...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua-get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.215 IQR)
- **Top Global Matches:** file_cluster_0: 12.215, file_cluster_13: 12.526, file_cluster_11: 12.785
- **Magnitude:** 145.76 | **LOC:** 149 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.4039%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_test` (Impact: 36.0)
  * `daemonize` (Impact: 30.0)
  * `url` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 45`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 75`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, FindBin, utf8, HTTP::Daemon, warnings, URI, LWP::RobotUA...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.431 IQR)
- **Top Global Matches:** file_cluster_0: 12.431, file_cluster_13: 12.674, file_cluster_11: 12.967
- **Magnitude:** 141.52 | **LOC:** 146 | **CtrlFlow:** 47.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `daemonize` (Impact: 30.0)
  * `_test` (Impact: 19.8)
  * `url` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 48`, `args: 4`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 87`
* *Architecture:* `io: 3`, `import: 10`
* *Defense:* `safety: 2`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, FindBin, HTTP::Request, HTTP::Daemon, utf8, warnings, URI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwpcook.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.958 IQR)
- **Top Global Matches:** file_cluster_0: 11.958, file_cluster_13: 12.12, file_cluster_17: 12.577
- **Magnitude:** 110.1 | **LOC:** 311 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.3416%), Tech Debt (39.4884%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 41`, `args: 1`
* *Risk/State:* `state_mutation: 91`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `import: 27`
* *Defense:* `safety: 2`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTP::Request::Common, simple, proxies, HTTP::CookieJar::LWP, the, se, that, LWP::UserAgent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.166 IQR)
- **Top Global Matches:** file_cluster_0: 12.166, file_cluster_13: 12.65, file_cluster_8: 12.707
- **Magnitude:** 104.2 | **LOC:** 207 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.3309%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 35`, `args: 1`
* *Risk/State:* `state_mutation: 86`
* *Architecture:* `io: 22`, `import: 6`
* *Defense:* `safety: 2`, `test: 54`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, HTTP::Request, LWP::UserAgent, warnings, undef
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/cache-timeouts.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.136 IQR)
- **Top Global Matches:** file_cluster_0: 12.136, file_cluster_13: 12.301, file_cluster_17: 12.72
- **Magnitude:** 68.38 | **LOC:** 94 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.4722%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 19`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 52`
* *Architecture:* `io: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, FindBin, HTTP::Request, LWP::UserAgent, warnings, net, LWP::ConnCache
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/default_content_type.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.01 IQR)
- **Top Global Matches:** file_cluster_0: 12.01, file_cluster_13: 12.364, file_cluster_11: 12.519
- **Magnitude:** 61.08 | **LOC:** 141 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.6028%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 29`
* *Risk/State:* `state_mutation: 44`, `dead_code: 1`
* *Architecture:* `io: 2`, `import: 5`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, the, HTTP::Request, LWP::UserAgent, warnings, default
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-dump` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.653 IQR)
- **Top Global Matches:** file_cluster_13: 12.653, file_cluster_0: 12.793, file_cluster_8: 13.079
- **Magnitude:** 57.36 | **LOC:** 114 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.5696%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 3.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 52`
* *Architecture:* `io: 6`, `import: 8`
* *Defense:* `safety: 3`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, content, LWP::UserAgent, Encode, warnings, Encode::Locale, Getopt::Long
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/httpsub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.788 IQR)
- **Top Global Matches:** file_cluster_0: 11.788, file_cluster_13: 11.96, file_cluster_8: 12.36
- **Magnitude:** 52.56 | **LOC:** 93 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.7381%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 1.6)
  * `format_request` (Impact: 1.6)
  * `syswrite` (Impact: 1.6)
  * `read_response_headers` (Impact: 1.6)
  * `read_entity_body` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 47`, `args: 10`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 31`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `io: 3`, `api: 3`, `import: 9`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, parent, LWP::Protocol, HTTP::Request, LWP::UserAgent, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/chunk.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.378 IQR)
- **Top Global Matches:** file_cluster_17: 14.378, file_cluster_0: 14.442, file_cluster_13: 14.494
- **Magnitude:** 51.48 | **LOC:** 35 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.16%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 12`, `args: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `io: 2`, `import: 6`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, Test::RequiresInternet, HTTP::Request, LWP::UserAgent, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/proxy.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.182 IQR)
- **Top Global Matches:** file_cluster_0: 11.182, file_cluster_13: 11.331, file_cluster_8: 11.498
- **Magnitude:** 49.44 | **LOC:** 85 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.6508%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 38`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 8`, `import: 5`
* *Defense:* `safety: 2`, `test: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, errors, strict, LWP::UserAgent, warnings, Test::Fatal
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-mirror` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.052 IQR)
- **Top Global Matches:** file_cluster_13: 12.052, file_cluster_0: 12.155, file_cluster_8: 12.429
- **Magnitude:** 42.9 | **LOC:** 104 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.1524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `usage` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 18`, `args: 2`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 39`
* *Architecture:* `io: 1`, `import: 7`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP, strict, basename, Encode, warnings, Encode::Locale, Getopt::Long, LWP::Simple
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `talk-to-ourself` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.716 IQR)
- **Top Global Matches:** file_cluster_0: 12.716, file_cluster_13: 12.932, file_cluster_11: 13.317
- **Magnitude:** 42.78 | **LOC:** 51 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.5036%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 12`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 27`
* *Architecture:* `io: 13`, `import: 4`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings, IO::Socket, IO::Select
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/protosub.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 16.293 IQR)
- **Top Global Matches:** file_cluster_0: 16.293, file_cluster_13: 16.677, file_cluster_11: 16.884
- **Magnitude:** 41.0 | **LOC:** 58 | **CtrlFlow:** 44.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.0797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `request` (Impact: 12.1)
  * `new` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 19`, `args: 4`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `dead_code: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 8`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, parent, LWP::Protocol, HTTP::Request, LWP::UserAgent, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/redirect-post.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.924 IQR)
- **Top Global Matches:** file_cluster_0: 12.924, file_cluster_13: 12.937, file_cluster_8: 13.58
- **Magnitude:** 40.56 | **LOC:** 44 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.3421%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, Test::RequiresInternet, HTTP::Request, LWP::UserAgent, Encode, warnings, JSON::PP
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/http-post.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.093 IQR)
- **Top Global Matches:** file_cluster_0: 13.093, file_cluster_13: 13.176, file_cluster_8: 13.812
- **Magnitude:** 38.54 | **LOC:** 39 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6119%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 19`
* *Risk/State:* `state_mutation: 23`
* *Architecture:* `io: 2`, `import: 7`
* *Defense:* `safety: 2`, `test: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, FindBin, HTTP::Request, LWP::UserAgent, warnings, net
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/local/get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.181 IQR)
- **Top Global Matches:** file_cluster_0: 12.181, file_cluster_13: 12.322, file_cluster_8: 12.591
- **Magnitude:** 37.32 | **LOC:** 82 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.4197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `slurp` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 20`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 8`, `import: 5`
* *Defense:* `safety: 2`, `test: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, warnings, File::Temp, LWP::Simple
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/net/cgi-bin/slowread` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.764 IQR)
- **Top Global Matches:** file_cluster_13: 12.764, file_cluster_8: 12.94, file_cluster_17: 13.243
- **Magnitude:** 36.46 | **LOC:** 34 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.7101%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 9`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/live/jigsaw/auth-b.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.467 IQR)
- **Top Global Matches:** file_cluster_0: 13.467, file_cluster_13: 13.679, file_cluster_11: 14.213
- **Magnitude:** 36.4 | **LOC:** 48 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.1591%), Tech Debt (98.0708%)
**Top Internal Functions/Classes:**
  * `get_basic_credentials` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 16`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 7`
* *Defense:* `safety: 4`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, strict, Test::RequiresInternet, parent, HTTP::Request, LWP::UserAgent, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/misc/get-callback` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.741 IQR)
- **Top Global Matches:** file_cluster_13: 13.741, file_cluster_0: 13.782, file_cluster_8: 14.146
- **Magnitude:** 36.38 | **LOC:** 30 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.7216%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `data` (Impact: 5.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 11`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 30`
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/author/misc/get-file` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 20.109 IQR)
- **Top Global Matches:** file_cluster_0: 20.109, file_cluster_13: 20.341, file_cluster_17: 20.456
- **Magnitude:** 36.24 | **LOC:** 24 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* `state_mutation: 21`, `dead_code: 1`
* *Architecture:* `io: 2`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 16.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` LWP::UserAgent, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/base/protocols.t` (PERL) | Magnitude: 19.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, test: 7, state_mutation: 4, decorators: 4
- `t/base/protocols/nntp.t` (PERL) | Magnitude: 20.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 7, state_mutation: 6, decorators: 5, import: 5
- `xt/author/live/jigsaw/redirect-post.t` (PERL) | Magnitude: 40.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 25, structural_boundaries: 17, decorators: 11, test: 9
- `t/local/autoload.t` (PERL) | Magnitude: 27.38 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, structural_boundaries: 10, decorators: 7, import: 6
- `t/base/ua_handlers.t` (PERL) | Magnitude: 34.64 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 31, structural_boundaries: 28, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/local/autoload-get.t` (PERL) | Magnitude: 24.34 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 9, structural_boundaries: 8, decorators: 5, import: 5
- `xt/author/misc/get-callback` (PERL) | Magnitude: 36.38 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, structural_boundaries: 11, indent_spaces: 11, branch: 8
- `bin/lwp-download` (PERL) | Magnitude: 2583.01 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 190, state_mutation: 187, branch: 91, structural_boundaries: 69
- `bin/lwp-mirror` (PERL) | Magnitude: 42.9 | Delta: **0.103 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 39, branch: 20, indent_spaces: 19, structural_boundaries: 18
- `xt/author/net/cgi-bin/nph-slowdata` (PERL) | Magnitude: 12.58 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 9, indent_spaces: 7, structural_boundaries: 6, branch: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `xt/author/live/jigsaw/chunk.t` (PERL) | Magnitude: 51.48 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 36, structural_boundaries: 12, decorators: 10, branch: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `bin/lwp-download` -> **copilot-swe-agent[bot]** (100.0% isolated ownership) | Magnitude: 2583.01
- `t/base/default_content_type.t` -> **copilot-swe-agent[bot]** (100.0% isolated ownership) | Magnitude: 61.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `xt/author/live/jigsaw/auth-b.t` -> **Severity: 1613.596** (Blast Radius: 16.992 * Doc Risk: 94.9621%)
- `t/leak/no_leak.t` -> **Severity: 1602.862** (Blast Radius: 16.992 * Doc Risk: 94.3304%)
- `xt/author/live/jigsaw/auth-d.t` -> **Severity: 1278.369** (Blast Radius: 16.992 * Doc Risk: 75.2336%)
- `t/base/simple.t` -> **Severity: 1241.118** (Blast Radius: 31.436 * Doc Risk: 39.4808%)
- `t/base/protocols.t` -> **Severity: 1164.294** (Blast Radius: 16.992 * Doc Risk: 68.5201%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
