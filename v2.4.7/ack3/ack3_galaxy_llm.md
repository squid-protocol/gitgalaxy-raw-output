# ARCHITECTURAL_BRIEF: ack3
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_perl/ack3` |
| **Timestamp** | `2026-08-07T03:51:39.069531+00:00` |
| **Scan Duration** | `0.48s` |
| **Git Branch** | `dev` |
| **Git Commit** | `1c9cfd3508dd1109815d85e64c55656b00454289` |
| **Git Remote** | `https://github.com/beyondgrep/ack3.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 16 malicious artifacts.

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
| Total Artifacts | 297 |
| Analyzed Artifacts (Scanned) | 175 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 122 |
| Total LOC | 11211 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 58.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0294 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9701 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 99 | 9329 | 56.6% |
| YAML | 27 | 1602 | 15.4% |
| PLAINTEXT | 15 | 0 | 8.6% |
| MARKDOWN | 12 | 0 | 6.9% |
| HTML | 5 | 142 | 2.9% |
| SHELL | 3 | 15 | 1.7% |
| CSHARP | 3 | 8 | 1.7% |
| RUBY | 2 | 64 | 1.1% |
| C | 2 | 17 | 1.1% |
| FORTRAN | 2 | 22 | 1.1% |
| DOCKERFILE | 1 | 5 | 0.6% |
| MAKEFILE | 1 | 1 | 0.6% |
| CSS | 1 | 1 | 0.6% |
| JAVASCRIPT | 1 | 2 | 0.6% |
| PYTHON | 1 | 3 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.842`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 59 | 33.7% |
| file_cluster_13 | 49 | 28.0% |
| file_cluster_0 | 31 | 17.7% |
| file_cluster_17 | 6 | 3.4% |
| file_cluster_4 | 2 | 1.1% |
| file_cluster_9 | 1 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 15.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 122*

**Composition by Extension & Reason:**
- `no_extension`: 27x Unsupported Format (.undeterminable), 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 114 LOC)
- `.pm`: 21x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 10x Excluded (Unsupported Extension: '.0')
- `.xxx`: 8x Excluded (Unsupported Extension: '.xxx')
- `.1`: 1x Excluded (Machine-Generated Source Code Signature: 5566 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5800 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5914 LOC)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2131 LOC)
- `.2`: 1x Excluded (Machine-Generated Source Code Signature: 5616 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5851 LOC), 1x Excluded (Machine-Generated Source Code Signature: 6290 LOC)
- `.py`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.3`: 1x Excluded (Machine-Generated Source Code Signature: 5619 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5849 LOC)
- `.min`: 2x Excluded (Unsupported Extension: '.min')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.96`: 1x Excluded (Unsupported Extension: '.96')
- `.22`: 1x Excluded (Unsupported Extension: '.22')
- `.24`: 1x Excluded (Unsupported Extension: '.24')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 39.2 | 23.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 53.2 | 79.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 2.5 | 0.3 | 0.0 |
| API Exposure | 0.0 | 8.0 | 0.2 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 58.8 | 99.9 | 100.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 86.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 92.8 | 32.8 | 29.4 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/Util.pm` (Hits: 64)
- `ack` (Hits: 58)
- `dev/linecount-fork` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Util.pm** (`t/Util.pm`) — 66 inbound connections
2. **ack** (`ack`) — 1 inbound connections
3. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 0 inbound connections
4. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
5. **DESIGN.md** (`DESIGN.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ack** (`ack`) — 47 outbound dependencies
2. **Util.pm** (`t/Util.pm`) — 19 outbound dependencies
3. **Cookbook.pm** (`dev/Cookbook.pm`) — 13 outbound dependencies
4. **timings.pl** (`dev/timings.pl`) — 13 outbound dependencies
5. **00-load.t** (`t/00-load.t`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `lists_match` (@ `t/Util.pm`) -> Impact: **174.3** | LOC: 743
  * *Intent:* # Use this one if order is important.
- `run_cmd` (@ `t/Util.pm`) -> Impact: **104.1** | LOC: 125
  * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus writes its STDERR to $catcherr_file). # # Sets $a...
- `_populate_man_options` (@ `xt/man.t`) -> Impact: **29.6** | LOC: 71
- `MY::postamble` (@ `Makefile.PL`) -> Impact: **27.2** | LOC: 104
- `time_ack` (@ `dev/timings.pl`) -> Impact: **23.1** | LOC: 61
- `_where` (@ `dev/generate-rgb-codes.pl`) -> Impact: **22.9** | LOC: 118
- `run_piped` (@ `t/Util.pm`) -> Impact: **19.4** | LOC: 77
- `_do_parent` (@ `t/Util.pm`) -> Impact: **15.2** | LOC: 44
- `build_ack_invocation` (@ `t/Util.pm`) -> Impact: **14.2** | LOC: 43
- `strip_special_chars` (@ `xt/man.t`) -> Impact: **13.6** | LOC: 8

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 13 | 38631.72 | 8.03% | 19.7% |
| `t` | 98 | 7078.4 | 45.67% | 7.34% |
| `dev` | 15 | 838.56 | 51.76% | 3.17% |
| `xt` | 4 | 298.14 | 63.21% | 0.0% |
| `t/swamp` | 27 | 274.81 | 4.25% | 14.33% |
| `t/range` | 5 | 66.38 | 12.99% | 0.0% |
| `dev/docker` | 3 | 27.06 | 5.0% | 33.33% |
| `t/text` | 9 | 26.12 | 0.0% | 0.0% |
| `t/swamp/swamp` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `t/ack-k.yaml` -> **100.0%** Exposure
- `dev/docker/docker-entrypoint.sh` -> **100.0%** Exposure
- `stack` -> **100.0%** Exposure
- `tack` -> **100.0%** Exposure
- `t/swamp/crystallography-weenies.f` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `ack` -> **100.0%** Exposure
- `dev/Cookbook.pm` -> **100.0%** Exposure
- `dev/crank-mutex` -> **100.0%** Exposure
- `dev/generate-rgb-codes.pl` -> **100.0%** Exposure
- `dev/issues-scrub.pl` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/range.t` -> **0** Orphaned Functions | **4** Duplicates
- `Makefile.PL` -> **2** Orphaned Functions | **0** Duplicates
- `t/swamp/Rakefile` -> **2** Orphaned Functions | **0** Duplicates
- `t/ack-ignore-dir.t` -> **1** Orphaned Functions | **0** Duplicates
- `dev/docker/docker-entrypoint.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`dev/docker/docker-entrypoint.sh`** -> AI Confidence: **99.29%**
2. **`t/swamp/sample.rake`** -> AI Confidence: **99.29%**
3. **`t/swamp/Rakefile`** -> AI Confidence: **98.96%**
4. **`dev/docker/Dockerfile`** -> AI Confidence: **98.84%**
5. **`stack`** -> AI Confidence: **98.84%**
6. **`tack`** -> AI Confidence: **98.84%**
7. **`t/swamp/Makefile`** -> AI Confidence: **98.84%**
8. **`t/swamp/Sample.ascx`** -> AI Confidence: **98.84%**
9. **`t/swamp/Sample.asmx`** -> AI Confidence: **98.84%**
10. **`t/swamp/service.svc`** -> AI Confidence: **98.84%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `614` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `t/Util.pm` (PERL) -> Cumulative Risk: **706.3**
- **Archetype:** `file_cluster_0` (Distance: 13.229 IQR)
- **Magnitude:** 1175.72 | **LOC:** 1380 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Concurrency (98.4013%)
- **Heaviest Functions:** `lists_match` (Impact: 174.3), `run_cmd` (Impact: 104.1), `run_piped` (Impact: 19.4)

### 2. `dev/timings.pl` (PERL) -> Cumulative Risk: **559.47**
- **Archetype:** `file_cluster_17` (Distance: 12.378 IQR)
- **Magnitude:** 271.82 | **LOC:** 408 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.947%), Verification (80.0%)
- **Heaviest Functions:** `time_ack` (Impact: 23.1), `grab_versions` (Impact: 12.8), `counts_valid` (Impact: 9.8)

### 3. `t/process-substitution.t` (PERL) -> Cumulative Risk: **536.08**
- **Archetype:** `file_cluster_4` (Distance: 11.995 IQR)
- **Magnitude:** 51.84 | **LOC:** 58 | **CtrlFlow:** 42.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9997%), Cognitive Load (99.0684%)

### 4. `dev/linecount-fork` (PERL) -> Cumulative Risk: **511.34**
- **Archetype:** `file_cluster_4` (Distance: 13.041 IQR)
- **Magnitude:** 63.74 | **LOC:** 46 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.9286%)

### 5. `xt/man.t` (PERL) -> Cumulative Risk: **484.54**
- **Archetype:** `file_cluster_13` (Distance: 12.88 IQR)
- **Magnitude:** 160.48 | **LOC:** 132 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.9881%), Cognitive Load (82.2788%)
- **Heaviest Functions:** `_populate_man_options` (Impact: 29.6), `strip_special_chars` (Impact: 13.6), `check_for_option_in_man_output` (Impact: 5.1)

### 6. `t/ack-ignore-file.t` (PERL) -> Cumulative Risk: **484.26**
- **Archetype:** `file_cluster_17` (Distance: 11.649 IQR)
- **Magnitude:** 50.34 | **LOC:** 86 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (90.3304%), Tech Debt (83.2643%)

### 7. `t/range.t` (PERL) -> Cumulative Risk: **483.2**
- **Archetype:** `file_cluster_13` (Distance: 12.722 IQR)
- **Magnitude:** 139.0 | **LOC:** 281 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.7023%), Safety Score (95.3845%)
- **Heaviest Functions:** `foo` (Impact: 1.1), `bar` (Impact: 1.1), `foo` (Impact: 1.1)

### 8. `t/filetypes.t` (PERL) -> Cumulative Risk: **474.06**
- **Archetype:** `file_cluster_13` (Distance: 10.575 IQR)
- **Magnitude:** 31.0 | **LOC:** 93 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (99.998%), Safety Score (82.5846%)
- **Heaviest Functions:** `is_filetype` (Impact: 5.6), `filetypes` (Impact: 3.1)

### 9. `dev/generate-rgb-codes.pl` (PERL) -> Cumulative Risk: **459.09**
- **Archetype:** `file_cluster_0` (Distance: 19.895 IQR)
- **Magnitude:** 81.08 | **LOC:** 150 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.238%), Dead Code (91.6827%)
- **Heaviest Functions:** `_where` (Impact: 22.9), `_five_to_1` (Impact: 1.6)

### 10. `t/ack-dump.t` (PERL) -> Cumulative Risk: **443.29**
- **Archetype:** `file_cluster_13` (Distance: 13.565 IQR)
- **Magnitude:** 39.44 | **LOC:** 36 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (97.8422%), Cognitive Load (86.0348%)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `ack` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.27 IQR)
- **Top Global Matches:** file_cluster_0: 14.27, file_cluster_13: 14.493, file_cluster_8: 14.582
- **Magnitude:** 38515.0 | **LOC:** 2545 | **CtrlFlow:** 66.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.541%), Tech Debt (10.1462%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 646`, `structural_boundaries: 329`, `args: 30`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 12`, `state_mutation: 1554`, `fragile_debt: 3`
* *Architecture:* `io: 58`, `import: 54`
* *Defense:* `safety: 4`, `doc: 161`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.976
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005747
  * `Imports (Out-Degree: 0):` FILE, F, C, matter, returns, file, files, Win32::Console::ANSI...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.229 IQR)
- **Top Global Matches:** file_cluster_0: 13.229, file_cluster_4: 13.275, file_cluster_13: 13.497
- **Magnitude:** 1175.72 | **LOC:** 1380 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.8656%), Tech Debt (13.9159%)
**Top Internal Functions/Classes:**
  * `lists_match` (Impact: 174.3)
    * *Intent:* # Use this one if order is important.
  * `run_cmd` (Impact: 104.1)
    * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus...
  * `run_piped` (Impact: 19.4)
  * `_do_parent` (Impact: 15.2)
  * `build_ack_invocation` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 369`, `args: 59`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 8`, `state_mutation: 682`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 64`, `api: 2`, `concurrency: 73`, `import: 21`
* *Defense:* `safety: 3`, `doc: 6`, `test: 19`, `cleanup: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 246.184
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.37931
  * `Imports (Out-Degree: 0):` YAML::PP, Cwd, Test::More, Win32, Carp, IO::Pty, List::Util, Scalar::Util...
  * `Imported By (In-Degree: 66):` (Excluded from Brief to save tokens)

### `t/ack-output-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.263 IQR)
- **Top Global Matches:** file_cluster_0: 13.263, file_cluster_8: 13.491, file_cluster_13: 13.624
- **Magnitude:** 467.5 | **LOC:** 450 | **CtrlFlow:** 49.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.2238%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 115`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 446`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings, Term::ANSIColor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config-loader.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.671 IQR)
- **Top Global Matches:** file_cluster_8: 11.671, file_cluster_0: 11.712, file_cluster_13: 11.77
- **Magnitude:** 452.74 | **LOC:** 298 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.2763%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 64`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 133`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `test: 8`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, targets, lib, argument, Test::More, warnings, App::Ack::ConfigLoader...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mutex-options.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.443 IQR)
- **Top Global Matches:** file_cluster_8: 13.443, file_cluster_13: 13.554, file_cluster_0: 13.661
- **Magnitude:** 314.4 | **LOC:** 225 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.9318%), Tech Debt (27.4438%)
**Top Internal Functions/Classes:**
  * `are_mutually_exclusive` (Impact: 11.8)
    * *Intent:* # Do this without system().
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 34`, `args: 2`, `func_start: 1`
* *Risk/State:* `state_mutation: 299`, `fragile_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/timings.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.378 IQR)
- **Top Global Matches:** file_cluster_17: 12.378, file_cluster_8: 12.383, file_cluster_13: 12.391
- **Magnitude:** 271.82 | **LOC:** 408 | **CtrlFlow:** 41.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.6662%), Tech Debt (17.9738%)
**Top Internal Functions/Classes:**
  * `time_ack` (Impact: 23.1)
  * `grab_versions` (Impact: 12.8)
  * `counts_valid` (Impact: 9.8)
  * `color` (Impact: 9.1)
  * `create_format` (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 101`, `args: 4`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 190`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 6`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 2`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Spec, Time::HiRes, Util, Getopt::Long, List::Util, autodie, strict, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-pager.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.965 IQR)
- **Top Global Matches:** file_cluster_0: 12.965, file_cluster_8: 13.484, file_cluster_13: 13.539
- **Magnitude:** 255.92 | **LOC:** 248 | **CtrlFlow:** 70.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.8638%), Tech Debt (16.6986%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 38`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 237`, `planned_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-type.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.649 IQR)
- **Top Global Matches:** file_cluster_0: 13.649, file_cluster_13: 13.705, file_cluster_8: 13.863
- **Magnitude:** 222.22 | **LOC:** 154 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.1009%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 205`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, lines, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/Cookbook.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.334 IQR)
- **Top Global Matches:** file_cluster_13: 13.334, file_cluster_0: 13.348, file_cluster_17: 13.393
- **Magnitude:** 192.04 | **LOC:** 589 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.3317%), Tech Debt (29.5988%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 48`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 5`, `state_mutation: 170`, `planned_debt: 3`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 1`, `doc: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` LWP::Simple, two, guarantee, neither, args, C, changes, a...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.084 IQR)
- **Top Global Matches:** file_cluster_13: 13.084, file_cluster_8: 13.1, file_cluster_0: 13.105
- **Magnitude:** 189.58 | **LOC:** 185 | **CtrlFlow:** 31.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.337%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 58`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 172`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/context.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.938 IQR)
- **Top Global Matches:** file_cluster_13: 12.938, file_cluster_0: 13.016, file_cluster_8: 13.043
- **Magnitude:** 182.66 | **LOC:** 180 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8204%), Tech Debt (39.357%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 45`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 165`, `fragile_debt: 1`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` separator, Amendment, black, Util, law, strict, token, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/man.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.88 IQR)
- **Top Global Matches:** file_cluster_13: 12.88, file_cluster_0: 12.898, file_cluster_8: 13.031
- **Magnitude:** 160.48 | **LOC:** 132 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.2788%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_populate_man_options` (Impact: 29.6)
  * `strip_special_chars` (Impact: 13.6)
  * `check_for_option_in_man_output` (Impact: 5.1)
  * `get_man_options` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 35`, `args: 2`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 108`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Data::Dumper, critic, Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-underline.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.756 IQR)
- **Top Global Matches:** file_cluster_0: 13.756, file_cluster_13: 13.827, file_cluster_8: 13.975
- **Magnitude:** 160.24 | **LOC:** 156 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.9419%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 34`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 143`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, law, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/highlighting.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.791 IQR)
- **Top Global Matches:** file_cluster_17: 12.791, file_cluster_0: 12.907, file_cluster_8: 12.961
- **Magnitude:** 153.7 | **LOC:** 221 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (97.9668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_check_it` (Impact: 3.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 37`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 147`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, law, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-passthru.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.537 IQR)
- **Top Global Matches:** file_cluster_8: 12.537, file_cluster_0: 12.544, file_cluster_13: 12.554
- **Magnitude:** 142.68 | **LOC:** 188 | **CtrlFlow:** 42.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.9708%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `color_match` (Impact: 4.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 48`, `args: 1`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 135`
* *Architecture:* `io: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-ignore-dir.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.142 IQR)
- **Top Global Matches:** file_cluster_8: 12.142, file_cluster_0: 12.172, file_cluster_13: 12.284
- **Magnitude:** 141.52 | **LOC:** 231 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.9971%), Tech Debt (22.1507%)
**Top Internal Functions/Classes:**
  * `set_up_assertion_that_these_options_will` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 18`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 129`, `orphaned_logic: 1`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Spec, Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/range.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.722 IQR)
- **Top Global Matches:** file_cluster_13: 12.722, file_cluster_0: 12.775, file_cluster_17: 12.839
- **Magnitude:** 139.0 | **LOC:** 281 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6454%), Tech Debt (97.7023%)
**Top Internal Functions/Classes:**
  * `foo` (Impact: 1.1)
  * `bar` (Impact: 1.1)
  * `foo` (Impact: 1.1)
  * `bar` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 67`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 131`, `duplicate_logic: 4`
* *Architecture:* `import: 13`
* *Defense:* `safety: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, end, strict, start, lib, Test::More, warnings, range
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/interactive.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.786 IQR)
- **Top Global Matches:** file_cluster_0: 12.786, file_cluster_13: 12.964, file_cluster_8: 13.045
- **Magnitude:** 136.1 | **LOC:** 138 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.1099%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`
* *Risk/State:* `state_mutation: 119`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings, Term::ANSIColor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-group.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.045 IQR)
- **Top Global Matches:** file_cluster_0: 13.045, file_cluster_13: 13.209, file_cluster_17: 13.433
- **Magnitude:** 127.72 | **LOC:** 110 | **CtrlFlow:** 61.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.5827%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 23`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 111`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, break, strict, lib, Test::More, heading, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.05 IQR)
- **Top Global Matches:** file_cluster_0: 13.05, file_cluster_13: 13.353, file_cluster_17: 13.493
- **Magnitude:** 125.68 | **LOC:** 121 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (90.3619%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 109`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/longopts.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.194 IQR)
- **Top Global Matches:** file_cluster_13: 12.194, file_cluster_8: 12.272, file_cluster_0: 12.76
- **Magnitude:** 119.6 | **LOC:** 162 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.0821%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 44`
* *Risk/State:* `state_mutation: 102`
* *Architecture:* `import: 10`
* *Defense:* `safety: 5`, `doc: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` snorgledork, Util, strict, upper, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/invalid-ackrc.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.582 IQR)
- **Top Global Matches:** file_cluster_17: 13.582, file_cluster_13: 13.624, file_cluster_0: 13.701
- **Magnitude:** 104.2 | **LOC:** 88 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6454%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 22`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 88`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Temp, Util, output, List::Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-print0.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.894 IQR)
- **Top Global Matches:** file_cluster_17: 12.894, file_cluster_13: 12.96, file_cluster_8: 13.193
- **Magnitude:** 99.2 | **LOC:** 80 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.9974%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 26`
* *Risk/State:* `state_mutation: 83`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` null, Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.359 IQR)
- **Top Global Matches:** file_cluster_0: 11.359, file_cluster_8: 11.683, file_cluster_17: 11.745
- **Magnitude:** 83.08 | **LOC:** 177 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.8146%), Tech Debt (45.9621%)
**Top Internal Functions/Classes:**
  * `MY::postamble` (Impact: 27.2)
  * `MY::test` (Impact: 1.1)
    * *Intent:* # Suppress EU::MM test rule.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 13`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `state_mutation: 52`, `orphaned_logic: 2`
* *Architecture:* `import: 3`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExtUtils::MakeMaker, need, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-type-del.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.103 IQR)
- **Top Global Matches:** file_cluster_13: 14.103, file_cluster_0: 14.302, file_cluster_8: 14.459
- **Magnitude:** 81.68 | **LOC:** 48 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.4044%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `args: 3`
* *Risk/State:* `state_mutation: 66`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.311
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Util, strict, lib, Test::More, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/command-line-files.t` (PERL) | Magnitude: 54.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 39, indent_spaces: 23, branch: 20, structural_boundaries: 19
- `dev/linecount` (PERL) | Magnitude: 37.38 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 22, structural_boundaries: 12, indent_spaces: 8, encapsulation: 6
- `t/00-load.t` (PERL) | Magnitude: 56.96 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 41, structural_boundaries: 26, decorators: 23, indent_spaces: 23
- `t/Util.pm` (PERL) | Magnitude: 1175.72 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 835, state_mutation: 682, structural_boundaries: 369, branch: 194
- `dev/display-option-coverage.pl` (PERL) | Magnitude: 24.72 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 9, structural_boundaries: 8, branch: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/ack-w.t` (PERL) | Magnitude: 54.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, state_mutation: 49, structural_boundaries: 29, branch: 23
- `dev/Cookbook.pm` (PERL) | Magnitude: 192.04 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 191, state_mutation: 170, bitwise_ops: 157, indent_spaces: 108
- `t/ack-color.t` (PERL) | Magnitude: 189.58 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 172, indent_spaces: 91, structural_boundaries: 58, encapsulation: 47
- `xt/man.t` (PERL) | Magnitude: 160.48 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 108, indent_spaces: 81, structural_boundaries: 35, branch: 33
- `t/ack-match.t` (PERL) | Magnitude: 26.38 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 22, structural_boundaries: 21, indent_spaces: 21, encapsulation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dev/timings.pl` (PERL) | Magnitude: 271.82 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 190, structural_boundaries: 101, branch: 72
- `t/ack-ignore-file.t` (PERL) | Magnitude: 50.34 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, state_mutation: 34, branch: 19, structural_boundaries: 13
- `t/invalid-ackrc.t` (PERL) | Magnitude: 104.2 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 88, indent_spaces: 36, structural_boundaries: 22, test: 16
- `t/ack-print0.t` (PERL) | Magnitude: 99.2 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 83, indent_spaces: 43, structural_boundaries: 26, encapsulation: 21
- `t/highlighting.t` (PERL) | Magnitude: 153.7 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 147, indent_spaces: 61, structural_boundaries: 37, branch: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/process-substitution.t` (PERL) | Magnitude: 51.84 | Delta: **0.328 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 24, indent_spaces: 17, concurrency: 12, structural_boundaries: 11
- `dev/linecount-fork` (PERL) | Magnitude: 63.74 | Delta: **0.414 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 30, indent_spaces: 23, concurrency: 18, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `t/ack-passthru.t` (PERL) | Magnitude: 142.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 135, indent_spaces: 56, structural_boundaries: 48, branch: 35
- `t/ext-filter.t` (PERL) | Magnitude: 15.44 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 6, import: 6, decorators: 4
- `t/ack-ignore-dir.t` (PERL) | Magnitude: 141.52 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 131, state_mutation: 129, branch: 40, structural_boundaries: 18
- `t/config-loader.t` (PERL) | Magnitude: 452.74 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 196, state_mutation: 133, structural_boundaries: 64, cleanup: 32
- `t/firstlinematch-filter.t` (PERL) | Magnitude: 15.48 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, import: 6, decorators: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `t/swamp/Makefile` (MAKEFILE) | Magnitude: 10.52 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 10

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `t/Util.pm` -> Churn: **100.0%** | Cog Load: 93.8656% | Debt: 13.9159%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/Util.pm` -> **Dmitri Vereshchagin** (100.0% isolated ownership) | Magnitude: 1175.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/Util.pm` -> **Severity: 36.576** (Embedded: 0.3793 * Error Risk: 96.4272%)
- `ack` -> **Severity: 0.565** (Embedded: 0.0057 * Error Risk: 98.284%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/Util.pm` -> **Severity: 4560.903** (Blast Radius: 246.184 * Doc Risk: 18.5264%)
- `t/needs-line-scan.t` -> **Severity: 290.224** (Blast Radius: 4.311 * Doc Risk: 67.3218%)
- `t/ack-version.t` -> **Severity: 289.432** (Blast Radius: 4.311 * Doc Risk: 67.1381%)
- `t/bad-ackrc-opt.t` -> **Severity: 289.432** (Blast Radius: 4.311 * Doc Risk: 67.1381%)
- `t/match-filter.t` -> **Severity: 289.432** (Blast Radius: 4.311 * Doc Risk: 67.1381%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
