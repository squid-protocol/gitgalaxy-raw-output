# ARCHITECTURAL_BRIEF: Rex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/Rex` |
| **Timestamp** | `2026-08-07T03:51:36.903114+00:00` |
| **Scan Duration** | `0.32s` |
| **Git Branch** | `master` |
| **Git Commit** | `3159b71860d2f75850c75965462f0d7cd791dd57` |
| **Git Remote** | `https://github.com/RexOps/Rex.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 3 malicious artifacts.

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
| Total Artifacts | 515 |
| Analyzed Artifacts (Scanned) | 108 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 407 |
| Total LOC | 6845 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 21.0% |
| Dominant Lang | PERL |

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
| PERL | 90 | 6601 | 83.3% |
| PLAINTEXT | 7 | 0 | 6.5% |
| YAML | 5 | 36 | 4.6% |
| SHELL | 3 | 208 | 2.8% |
| MARKDOWN | 2 | 0 | 1.9% |
| XML | 1 | 0 | 0.9% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.715`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_0 | 44 | 40.7% |
| file_cluster_13 | 34 | 31.5% |
| file_cluster_8 | 18 | 16.7% |
| file_cluster_4 | 2 | 1.9% |
| file_cluster_17 | 1 | 0.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 8.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 407*

**Composition by Extension & Reason:**
- `.pm`: 347x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 11x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2047 LOC)
- `.yml`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out1`: 3x Excluded (Unsupported Extension: '.out1')
- `.out2`: 3x Excluded (Unsupported Extension: '.out2')
- `.out`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ex`: 2x Excluded (Unsupported Extension: '.ex')
- `.out3`: 2x Excluded (Unsupported Extension: '.out3')
- `.rex`: 2x Excluded (Unsupported Extension: '.rex')
- `.stderr`: 2x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 45.7 | 46.0 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.6 | 67.6 | 72.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 1.1 | 0.0 | 0.0 |
| API Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 86.9 | 100.0 | 100.0 |
| Commented Logic Exposure | 0.0 | 6.0 | 0.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.8 | 68.5 | 39.5 | 39.8 | 51.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `misc/create_pod.sh` (Hits: 166)
- `share/rex-tab-completion.zsh` (Hits: 28)
- `share/rex-tab-completion.bash` (Hits: 22)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
2. **README.md** (`README.md`) — 0 inbound connections
3. **rex** (`bin/rex`) — 0 inbound connections
4. **rexify** (`bin/rexify`) — 0 inbound connections
5. **check_supported_OS.pl** (`misc/check_supported_OS.pl`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rexify** (`bin/rexify`) — 29 outbound dependencies
2. **file.t** (`t/file.t`) — 15 outbound dependencies
3. **load_rexfile.t** (`t/load_rexfile.t`) — 14 outbound dependencies
4. **git.t** (`t/scm/git.t`) — 14 outbound dependencies
5. **rsync.t** (`t/rsync.t`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `upload_rexfile` (@ `bin/rexify`) -> Impact: **114.0** | LOC: 222
  * *Intent:* # upload rexfile to rex-jobcontrol (the complete directory)
- `Anonymous_Block` (@ `share/rex-tab-completion.bash`) -> Impact: **37.7** | LOC: 46
- `_hostgroups_[Truncated]` (@ `share/rex-tab-completion.zsh`) -> Impact: **18.4** | LOC: 68
- `Anonymous_Block` (@ `misc/create_pod.sh`) -> Impact: **17.6** | LOC: 98
- `get_image_format` (@ `t/issue/948.t`) -> Impact: **12.5** | LOC: 71
- `Rex::Helper::Run::i_run` (@ `t/issue/948.t`) -> Impact: **9.0** | LOC: 45
- `expected_params` (@ `t/file_hooks.t`) -> Impact: **8.2** | LOC: 22
- `test_summary` (@ `t/summary.t`) -> Impact: **6.6** | LOC: 32
- `create_tasks` (@ `t/summary.t`) -> Impact: **6.2** | LOC: 25
- `Anonymous_Block_[Truncated]` (@ `share/rex-tab-completion.bash`) -> Impact: **5.7** | LOC: 13

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `t` | 75 | 3142.21 | 47.99% | 1.58% |
| `bin` | 2 | 570.58 | 42.99% | 4.76% |
| `t/issue` | 8 | 234.42 | 42.4% | 12.5% |
| `share` | 2 | 126.66 | 72.12% | 96.46% |
| `misc` | 3 | 122.56 | 44.44% | 14.59% |
| `t/scm` | 1 | 83.46 | 29.84% | 0.0% |
| `xt/author` | 2 | 47.86 | 72.22% | 0.0% |
| `t/cmdb/default` | 2 | 29.42 | 5.0% | 0.0% |
| `t/cmdb` | 2 | 25.76 | 5.0% | 0.0% |
| `t/commands` | 1 | 20.6 | 9.11% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/issue/948.t` -> **99.9981%** Exposure
- `share/rex-tab-completion.bash` -> **98.97%** Exposure
- `share/rex-tab-completion.zsh` -> **93.9456%** Exposure
- `t/augeas.t` -> **87.3855%** Exposure
- `misc/create_pod.sh` -> **43.7823%** Exposure
### Highest State Flux (Mutation/Volatility)
- `misc/sanitize_pod.pl` -> **100.0%** Exposure
- `t/0.31.t` -> **100.0%** Exposure
- `t/augeas.t` -> **100.0%** Exposure
- `t/can_run.t` -> **100.0%** Exposure
- `t/case.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/issue/948.t` -> **4** Orphaned Functions | **0** Duplicates
- `share/rex-tab-completion.bash` -> **2** Orphaned Functions | **0** Duplicates
- `share/rex-tab-completion.zsh` -> **2** Orphaned Functions | **0** Duplicates
- `misc/create_pod.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`share/rex-tab-completion.bash`** -> AI Confidence: **99.17%**
2. **`share/rex-tab-completion.zsh`** -> AI Confidence: **99.06%**
3. **`misc/create_pod.sh`** -> AI Confidence: **98.83%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `651` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `share/rex-tab-completion.bash` (SHELL) -> Cumulative Risk: **631.78**
- **Archetype:** `file_cluster_4` (Distance: 12.426 IQR)
- **Magnitude:** 93.62 | **LOC:** 67 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.8653%), Safety Score (99.6282%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 37.7), `Anonymous_Block_[Truncated]` (Impact: 5.7), `__global_context__` (Impact: 1.3)

### 2. `t/shared.t` (PERL) -> Cumulative Risk: **515.34**
- **Archetype:** `file_cluster_4` (Distance: 12.667 IQR)
- **Magnitude:** 65.18 | **LOC:** 87 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9946%), Cognitive Load (96.7385%)

### 3. `t/summary.t` (PERL) -> Cumulative Risk: **489.72**
- **Archetype:** `file_cluster_0` (Distance: 11.337 IQR)
- **Magnitude:** 53.5 | **LOC:** 115 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Concurrency (94.0679%), Cognitive Load (85.0836%)
- **Heaviest Functions:** `test_summary` (Impact: 6.6), `create_tasks` (Impact: 6.2)

### 4. `misc/create_pod.sh` (SHELL) -> Cumulative Risk: **476.54**
- **Archetype:** `file_cluster_8` (Distance: 9.315 IQR)
- **Magnitude:** 38.1 | **LOC:** 120 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (95.6893%), Safety Score (93.7027%), Concurrency (72.3122%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.6), `__global_context__` (Impact: 1.5)

### 5. `t/augeas.t` (PERL) -> Cumulative Risk: **469.56**
- **Archetype:** `file_cluster_0` (Distance: 11.692 IQR)
- **Magnitude:** 47.24 | **LOC:** 103 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (87.3855%), Safety Score (84.8537%)

### 6. `bin/rexify` (PERL) -> Cumulative Risk: **467.45**
- **Archetype:** `file_cluster_0` (Distance: 12.494 IQR)
- **Magnitude:** 533.16 | **LOC:** 1402 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9995%), Safety Score (96.202%), Verification (80.0%)
- **Heaviest Functions:** `upload_rexfile` (Impact: 114.0), `download_recipe_local_tar_gz` (Impact: 5.1)

### 7. `share/rex-tab-completion.zsh` (SHELL) -> Cumulative Risk: **466.76**
- **Archetype:** `file_cluster_8` (Distance: 9.381 IQR)
- **Magnitude:** 33.04 | **LOC:** 77 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6467%), Safety Score (97.8301%), Tech Debt (93.9456%)
- **Heaviest Functions:** `_hostgroups_[Truncated]` (Impact: 18.4), `__global_context__` (Impact: 1.4)

### 8. `t/issue/948.t` (PERL) -> Cumulative Risk: **465.45**
- **Archetype:** `file_cluster_0` (Distance: 11.501 IQR)
- **Magnitude:** 52.8 | **LOC:** 96 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Tech Debt (99.9981%), Safety Score (80.3766%)
- **Heaviest Functions:** `get_image_format` (Impact: 12.5), `Rex::Helper::Run::i_run` (Impact: 9.0), `Rex::Commands::File::file` (Impact: 2.4)

### 9. `xt/author/critic-progressive.t` (PERL) -> Cumulative Risk: **441.34**
- **Archetype:** `file_cluster_0` (Distance: 12.294 IQR)
- **Magnitude:** 26.36 | **LOC:** 29 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (88.2172%), Cognitive Load (85.5422%)

### 10. `t/path.t` (PERL) -> Cumulative Risk: **441.15**
- **Archetype:** `file_cluster_0` (Distance: 13.363 IQR)
- **Magnitude:** 25.32 | **LOC:** 25 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (88.0797%), Safety Score (84.5535%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `bin/rexify` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.494 IQR)
- **Top Global Matches:** file_cluster_0: 12.494, file_cluster_13: 13.271, file_cluster_11: 13.361
- **Magnitude:** 533.16 | **LOC:** 1402 | **CtrlFlow:** 55.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.7555%), Tech Debt (9.5291%)
**Top Internal Functions/Classes:**
  * `upload_rexfile` (Impact: 114.0)
    * *Intent:* # upload rexfile to rex-jobcontrol (the complete directory)
  * `download_recipe_local_tar_gz` (Impact: 5.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 181`, `args: 11`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 51`, `state_mutation: 392`, `dead_code: 4`, `fragile_debt: 1`
* *Architecture:* `io: 18`, `import: 33`
* *Defense:* `safety: 5`, `doc: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Spec, HTTP::Request::Common, Rex::Commands::Box, Rex::Helper::URI, Rex, URI::QueryParam, Rex::Helper::Misc, multi...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/load_rexfile.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.315 IQR)
- **Top Global Matches:** file_cluster_0: 12.315, file_cluster_13: 12.479, file_cluster_17: 12.925
- **Magnitude:** 247.11 | **LOC:** 100 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.3876%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 32`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 41`
* *Architecture:* `io: 4`, `import: 13`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` delete, File::Temp, autodie, File::Spec, Sub::Override, English, Rex::CLI, Test::Output...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/write_utf8_files.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.605 IQR)
- **Top Global Matches:** file_cluster_13: 11.605, file_cluster_0: 11.787, file_cluster_8: 12.169
- **Magnitude:** 214.12 | **LOC:** 100 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9168%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 37`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`
* *Architecture:* `io: 2`, `import: 19`
* *Defense:* `safety: 3`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::LibMagic, File::Temp, command, utf8, Test::More, v5, Test::Warnings, Rex::Interface::File...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/rsync.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.746 IQR)
- **Top Global Matches:** file_cluster_13: 10.746, file_cluster_0: 10.81, file_cluster_8: 11.136
- **Magnitude:** 181.22 | **LOC:** 108 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.4497%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 30`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 27`
* *Architecture:* `io: 2`, `import: 13`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, autodie, Rex::Commands::Rsync, Rex::Task, Test::Deep, File::Find, Test::More, v5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.342 IQR)
- **Top Global Matches:** file_cluster_8: 11.342, file_cluster_0: 11.425, file_cluster_13: 11.46
- **Magnitude:** 113.06 | **LOC:** 393 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.743%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 45`
* *Risk/State:* `state_mutation: 92`
* *Architecture:* `import: 19`
* *Defense:* `safety: 2`, `test: 67`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Commands::Fs, extra, File::Spec, Rex::Commands::Gather, longer, Test::More, change...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/db.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.005 IQR)
- **Top Global Matches:** file_cluster_13: 10.005, file_cluster_0: 10.025, file_cluster_8: 10.204
- **Magnitude:** 95.04 | **LOC:** 121 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.1301%), Tech Debt (31.3391%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 31`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `io: 1`, `import: 11`
* *Defense:* `safety: 2`, `test: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` data, DBI, TCP, Test::More, v5, Test::Warnings, Data::Dumper, Test::mysqld...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `share/rex-tab-completion.bash` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.426 IQR)
- **Top Global Matches:** file_cluster_4: 12.426, file_cluster_8: 12.67, file_cluster_12: 12.797
- **Magnitude:** 93.62 | **LOC:** 67 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.8653%), Tech Debt (98.97%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 37.7)
  * `Anonymous_Block_[Truncated]` (Impact: 5.7)
  * `__global_context__` (Impact: 1.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 8`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 42`, `orphaned_logic: 2`
* *Architecture:* `io: 22`, `concurrency: 6`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cron.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.184 IQR)
- **Top Global Matches:** file_cluster_8: 11.184, file_cluster_17: 11.631, file_cluster_0: 11.882
- **Magnitude:** 86.86 | **LOC:** 539 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4321%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 25`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `import: 5`
* *Defense:* `safety: 4`, `test: 287`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Cron::Base, Test::More, v5, Test::Warnings, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/scm/git.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.06 IQR)
- **Top Global Matches:** file_cluster_8: 10.06, file_cluster_13: 10.303, file_cluster_0: 10.349
- **Magnitude:** 83.46 | **LOC:** 353 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.8419%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `git_last_commit_message_ok` (Impact: 5.2)
  * `prepare_test_repo` (Impact: 3.1)
  * `init_test` (Impact: 2.9)
  * `git_repo_ok` (Impact: 2.2)
  * `configure_git_user` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 75`, `args: 5`, `func_start: 8`
* *Risk/State:* `state_mutation: 61`
* *Architecture:* `import: 13`
* *Defense:* `safety: 2`, `test: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, File::Temp, Test::Exception, File::Spec, Rex::Commands::SCM, English, Rex::Helper::Run, critic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/0.31.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.333 IQR)
- **Top Global Matches:** file_cluster_0: 12.333, file_cluster_8: 12.344, file_cluster_13: 12.355
- **Magnitude:** 72.46 | **LOC:** 156 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.4796%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 26`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 55`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::More, v5, Test::Warnings, Rex, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `misc/sanitize_pod.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.395 IQR)
- **Top Global Matches:** file_cluster_13: 13.395, file_cluster_8: 13.491, file_cluster_17: 13.763
- **Magnitude:** 69.78 | **LOC:** 51 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.3241%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 11`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* `io: 4`, `import: 2`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` warnings, v5
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/file_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.551 IQR)
- **Top Global Matches:** file_cluster_13: 11.551, file_cluster_0: 11.626, file_cluster_8: 11.685
- **Magnitude:** 67.3 | **LOC:** 141 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (84.9838%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expected_params` (Impact: 8.2)
  * `before_hook` (Impact: 2.6)
  * `after_change_hook` (Impact: 2.5)
  * `after_hook` (Impact: 2.5)
  * `before_change_hook` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 45`, `args: 5`, `func_start: 5`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Temp, Rex::Hook, Test::Deep, Test::Output, Test::More, v5, Test::Warnings, warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/helper_path.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.043 IQR)
- **Top Global Matches:** file_cluster_0: 13.043, file_cluster_13: 13.494, file_cluster_8: 13.949
- **Magnitude:** 66.86 | **LOC:** 60 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.7122%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Helper::Path, Test::More, v5, Cwd, Test::Warnings, warnings, File::Basename
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/shared.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.667 IQR)
- **Top Global Matches:** file_cluster_4: 12.667, file_cluster_0: 12.772, file_cluster_13: 12.816
- **Magnitude:** 65.18 | **LOC:** 87 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (96.7385%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`
* *Architecture:* `concurrency: 12`, `import: 7`
* *Defense:* `safety: 2`, `test: 18`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Test::Deep, Test::More, v5, Rex::Shared::Var, Test::Warnings, Time::HiRes, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks_in_rexfile_tasks_in_pkg.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.305 IQR)
- **Top Global Matches:** file_cluster_0: 13.305, file_cluster_13: 13.507, file_cluster_11: 13.688
- **Magnitude:** 60.86 | **LOC:** 58 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8235%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, File::Temp, Test::More, v5, t::tasks::alien, Rex::Shared::Var, Test::Warnings, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dmi.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.547 IQR)
- **Top Global Matches:** file_cluster_0: 10.547, file_cluster_8: 10.595, file_cluster_13: 10.836
- **Magnitude:** 59.34 | **LOC:** 196 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.4268%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 41`
* *Architecture:* `import: 5`
* *Defense:* `safety: 5`, `test: 29`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Inventory::DMIDecode, Test::More, v5, Test::Warnings, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template_ng.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.063 IQR)
- **Top Global Matches:** file_cluster_13: 11.063, file_cluster_0: 11.084, file_cluster_8: 11.184
- **Magnitude:** 59.22 | **LOC:** 149 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.9128%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 19`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, spaces, Rex::Config, Test::More, v5, Test::Warnings, warnings, Rex::Template::NG
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cmdb.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.978 IQR)
- **Top Global Matches:** file_cluster_13: 10.978, file_cluster_0: 11.006, file_cluster_8: 11.1
- **Magnitude:** 58.2 | **LOC:** 135 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.0321%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 34`
* *Risk/State:* `state_mutation: 41`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 10`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, File::Spec, Test::Deep, Test::More, v5, Rex::CMDB, Cwd, Test::Warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cmdb_path.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.28 IQR)
- **Top Global Matches:** file_cluster_0: 11.28, file_cluster_13: 11.472, file_cluster_8: 11.708
- **Magnitude:** 56.12 | **LOC:** 121 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (62.5943%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_host_filename` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 51`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 51`
* *Architecture:* `import: 10`
* *Defense:* `safety: 2`, `test: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, File::Spec, Test::Deep, Test::More, v5, Rex::CMDB, Cwd, Test::Warnings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/summary.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.337 IQR)
- **Top Global Matches:** file_cluster_0: 11.337, file_cluster_13: 11.43, file_cluster_4: 11.649
- **Magnitude:** 53.5 | **LOC:** 115 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (85.0836%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_summary` (Impact: 6.6)
  * `create_tasks` (Impact: 6.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 40`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 33`
* *Architecture:* `concurrency: 6`, `import: 12`
* *Defense:* `safety: 2`, `test: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Module::Load::Conditional, if, English, Test::Deep, Rex::Config, Test::More, v5...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issue/948.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.501 IQR)
- **Top Global Matches:** file_cluster_0: 11.501, file_cluster_13: 11.672, file_cluster_8: 12.091
- **Magnitude:** 52.8 | **LOC:** 96 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.3934%), Tech Debt (99.9981%)
**Top Internal Functions/Classes:**
  * `get_image_format` (Impact: 12.5)
  * `Rex::Helper::Run::i_run` (Impact: 9.0)
  * `Rex::Commands::File::file` (Impact: 2.4)
    * *Intent:* # TODO implement mocking
  * `Rex::Commands::Fs::unlink` (Impact: 2.4)
  * `Rex::Commands::Run::can_run` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 31`, `args: 2`, `func_start: 5`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 24`, `planned_debt: 2`, `orphaned_logic: 4`
* *Architecture:* `import: 12`
* *Defense:* `safety: 4`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands::Fs, Rex::Helper::Run, Rex::Virtualization, Test::More, v5, Test::Warnings, Data::Dumper, Rex::Commands::Run...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/task.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.523 IQR)
- **Top Global Matches:** file_cluster_8: 10.523, file_cluster_0: 10.54, file_cluster_13: 10.581
- **Magnitude:** 52.2 | **LOC:** 199 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.8645%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 39`, `args: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 34`
* *Architecture:* `io: 2`, `import: 11`
* *Defense:* `safety: 2`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, connection, more, Rex::Task, Test::More, v5, Test::Warnings, not...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.781 IQR)
- **Top Global Matches:** file_cluster_13: 10.781, file_cluster_0: 10.847, file_cluster_8: 10.921
- **Magnitude:** 51.04 | **LOC:** 139 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.5098%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 22`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Config, Test::More, Rex::Template, v5, Test::Warnings, warnings, Symbol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/auth.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.628 IQR)
- **Top Global Matches:** file_cluster_8: 10.628, file_cluster_0: 10.815, file_cluster_13: 10.865
- **Magnitude:** 50.92 | **LOC:** 181 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.5405%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 23`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 33`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Commands, Rex::Group, Test::More, v5, Test::Warnings, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/network_linux.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.428 IQR)
- **Top Global Matches:** file_cluster_0: 13.428, file_cluster_13: 13.978, file_cluster_8: 14.208
- **Magnitude:** 49.48 | **LOC:** 93 | **CtrlFlow:** 75.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.6385%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 17`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `import: 6`
* *Defense:* `safety: 9`, `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 9.259
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Rex::Helper::Hash, Test::More, v5, Test::Warnings, Rex::Hardware::Network::Linux, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/0.31.t` (PERL) | Magnitude: 72.46 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 55, test: 54, pointers: 46, indent_spaces: 44
- `t/config-ssh.t` (PERL) | Magnitude: 22.4 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: pointers: 28, test: 22, structural_boundaries: 16, indent_spaces: 11
- `t/hooks_in_rexfile.t` (PERL) | Magnitude: 36.82 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, state_mutation: 21, decorators: 11, closures: 9
- `t/url_encode.t` (PERL) | Magnitude: 18.26 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, decorators: 7, import: 5, state_mutation: 3
- `t/before_all_tasks.t` (PERL) | Magnitude: 25.5 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 14, decorators: 13, state_mutation: 10, import: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/issue/949.t` (PERL) | Magnitude: 20.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 10, decorators: 8, import: 7
- `t/hooks.t` (PERL) | Magnitude: 36.8 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 21, structural_boundaries: 20, decorators: 10, closures: 9
- `t/issue/934.t` (PERL) | Magnitude: 23.58 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 16, decorators: 14, import: 11, state_mutation: 8
- `t/interface_fs_local.t` (PERL) | Magnitude: 18.38 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 12, test: 8, decorators: 6, import: 5
- `t/commands_file_template.t` (PERL) | Magnitude: 23.8 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, state_mutation: 8, decorators: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/ini.t` (PERL) | Magnitude: 29.64 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, test: 35, globals: 28, comprehensions: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/shared.t` (PERL) | Magnitude: 65.18 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 37, indent_spaces: 26, test: 18, structural_boundaries: 13
- `share/rex-tab-completion.bash` (SHELL) | Magnitude: 93.62 | Delta: **0.244 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 42, indent_spaces: 39, branch: 28, io: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/task.t` (PERL) | Magnitude: 52.2 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 39, test: 36, state_mutation: 34
- `t/hardware/memory.t` (PERL) | Magnitude: 20.08 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 9, decorators: 9, import: 6
- `t/file.t` (PERL) | Magnitude: 113.06 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 92, test: 67, regex_execution: 66
- `t/auth.t` (PERL) | Magnitude: 50.92 | Delta: **0.187 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 54, pointers: 42, test: 37, state_mutation: 33
- `t/helper_hash.t` (PERL) | Magnitude: 17.84 | Delta: **0.193 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 8, test: 7, pointers: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/os_dependencies.t` -> **Severity: 634.428** (Blast Radius: 9.259 * Doc Risk: 68.5201%)
- `t/path.t` -> **Severity: 634.428** (Blast Radius: 9.259 * Doc Risk: 68.5201%)
- `t/virtualization.t` -> **Severity: 634.428** (Blast Radius: 9.259 * Doc Risk: 68.5201%)
- `t/base_virt.t` -> **Severity: 621.632** (Blast Radius: 9.259 * Doc Risk: 67.1381%)
- `t/proc.t` -> **Severity: 619.23** (Blast Radius: 9.259 * Doc Risk: 66.8787%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
