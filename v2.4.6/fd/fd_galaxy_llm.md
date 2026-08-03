# ARCHITECTURAL_BRIEF: fd
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/fd` |
| **Timestamp** | `2026-08-03T19:44:10.895752+00:00` |
| **Scan Duration** | `0.37s` |
| **Git Branch** | `master` |
| **Git Commit** | `866ba9bfd52b0a0fef537afee285d0c0703aa48e` |
| **Git Remote** | `https://github.com/sharkdp/fd.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 26 malicious artifacts.

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
| Total Artifacts | 54 |
| Analyzed Artifacts (Scanned) | 37 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 5457 |
| Volatility Index | 0.108 |
| % Scanned of codebase = | 68.5% |
| Dominant Lang | RUST |

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
| RUST | 22 | 5270 | 59.5% |
| MARKDOWN | 6 | 0 | 16.2% |
| PLAINTEXT | 3 | 0 | 8.1% |
| SHELL | 3 | 157 | 8.1% |
| XML | 2 | 1 | 5.4% |
| MAKEFILE | 1 | 29 | 2.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.526`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 11 | 29.7% |
| file_cluster_13 | 11 | 29.7% |
| file_cluster_0 | 2 | 5.4% |
| file_cluster_12 | 1 | 2.7% |
| file_cluster_16 | 1 | 2.7% |
| file_cluster_17 | 1 | 2.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 24.3% |
| Static: Minified & Vendor Opaque Mass | 1 | 2.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.toml`: 2x Excluded (Unsupported Extension: '.toml'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.toml)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yaml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.rs`: 1x Excluded (Saturation: Line 57 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 12.9 | 7.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 81.2 | 25.6 | 23.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 44.6 | 37.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 40.6 | 41.2 | 80.0 |
| API Exposure | 0.0 | 7.4 | 3.0 | 3.0 | 0.0 |
| Concurrency Exposure | 0.0 | 15.7 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.1 | 8.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 12.1 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 87.9 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.6 | 1.9 | 0.5 | 0.0 |
| Volatility Exposure | 0.0 | 96.4 | 16.3 | 8.6 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 55.8 | 66.6 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 55.0 | 72.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 7.7 | 0.3 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 96.6 | 3.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/create-deb.sh` (Hits: 25)
- `tests/tests.rs` (Hits: 16)
- `tests/testenv/mod.rs` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **job.rs** (`src/exec/job.rs`) — 1 inbound connections
2. **CHANGELOG.md** (`CHANGELOG.md`) — 0 inbound connections
3. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 0 inbound connections
4. **README.md** (`README.md`) — 0 inbound connections
5. **SECURITY.md** (`SECURITY.md`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **walk.rs** (`src/walk.rs`) — 39 outbound dependencies
2. **cli.rs** (`src/cli.rs`) — 22 outbound dependencies
3. **mod.rs** (`src/exec/mod.rs`) — 19 outbound dependencies
4. **tests.rs** (`tests/tests.rs`) — 19 outbound dependencies
5. **mod.rs** (`src/fmt/mod.rs`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `get_absolute_root_path` (@ `tests/tests.rs`) -> Impact: **405.5** | LOC: 2028
- `should_ignore` (@ `src/filetypes.rs`) -> Impact: **141.4** | LOC: 22
- `poll` (@ `src/walk.rs`) -> Impact: **137.0** | LOC: 80
- `absolute_path` (@ `src/filesystem.rs`) -> Impact: **106.7** | LOC: 133
- `parse_opt` (@ `src/filter/size.rs`) -> Impact: **77.7** | LOC: 34
- `build_walker` (@ `src/walk.rs`) -> Impact: **75.6** | LOC: 58
- `from_string` (@ `src/filter/owner.rs`) -> Impact: **73.6** | LOC: 32
  * *Intent:* /// Parses an owner constraint /// Returns an error if the string is invalid /// Returns Ok(None) when string is acceptable but a noop (such as "" or ...
- `print_entry_colorized` (@ `src/output.rs`) -> Impact: **69.9** | LOC: 50
  * *Intent:* // TODO: this function is performance critical and can probably be optimized
- `from_str` (@ `src/filter/time.rs`) -> Impact: **67.0** | LOC: 19
- `parse` (@ `src/fmt/mod.rs`) -> Impact: **65.5** | LOC: 50

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `exit` (@ `src/exit_codes.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Exit the process with the appropriate code.
- `gen_completions` (@ `src/cli.rs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// The directory where the filesystem search is rooted (optional). If /// omitted, search the current working directory. #[arg(action = ArgAction::Ap...
- `new` (@ `src/exec/mod.rs`) -> **O(2^N) [Recursive]**
- `fmt` (@ `src/hyperlink.rs`) -> **O(2^N) [Recursive]**
- `send` (@ `src/walk.rs`) -> **O(2^N) [Recursive]**
- `recv` (@ `src/walk.rs`) -> **O(2^N) [Recursive]**
- `get_absolute_root_path` (@ `tests/tests.rs`) -> **O(2^N) [Recursive]**
- `max_results` (@ `src/cli.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `src/exec/command.rs`) -> **O(2^N) [Recursive]**
- `new` (@ `src/exec/mod.rs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_absolute_root_path` (@ `tests/tests.rs`) -> DB Complexity: **35**
- `create_working_directory` (@ `tests/testenv/mod.rs`) -> DB Complexity: **9**
  * *Intent:* /// Create the working directory and the test files.
- `execute_commands` (@ `src/exec/command.rs`) -> DB Complexity: **5**
  * *Intent:* /// Executes a command.
- `poll` (@ `src/walk.rs`) -> DB Complexity: **5**
- `parse` (@ `src/fmt/mod.rs`) -> DB Complexity: **4**
- `create_broken_symlink` (@ `tests/testenv/mod.rs`) -> DB Complexity: **4**
  * *Intent:* /// Create a broken symlink at the given path in the temp_dir.
- `create_config_directory_with_global_igno` (@ `tests/testenv/mod.rs`) -> DB Complexity: **4**
- `Anonymous_Block` (@ `scripts/version-bump.sh`) -> DB Complexity: **3**
- `execute_batch` (@ `src/exec/mod.rs`) -> DB Complexity: **3**
- `new` (@ `src/exec/mod.rs`) -> DB Complexity: **3**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 11 | 1548.62 | 10.1% | 57.07% |
| `src/exec` | 3 | 497.0 | 16.09% | 32.59% |
| `tests` | 1 | 469.52 | 1.96% | 0.0% |
| `src/filter` | 4 | 377.92 | 7.93% | 38.29% |
| `tests/testenv` | 1 | 273.52 | 4.86% | 0.0% |
| `src/fmt` | 2 | 242.72 | 11.21% | 67.19% |
| `__monolith__` | 7 | 57.44 | 0.9% | 0.0% |
| `doc` | 6 | 43.42 | 5.15% | 16.06% |
| `scripts` | 2 | 7.75 | 52.5% | 70.34% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `scripts/version-bump.sh` -> **100.0%** Exposure
- `src/error.rs` -> **100.0%** Exposure
- `src/hyperlink.rs` -> **99.9998%** Exposure
- `src/output.rs` -> **99.8368%** Exposure
- `src/fmt/input.rs` -> **99.0462%** Exposure
### Highest State Flux (Mutation/Volatility)
- `scripts/version-bump.sh` -> **100.0%** Exposure
- `scripts/create-deb.sh` -> **99.999%** Exposure
- `src/exec/command.rs` -> **99.6631%** Exposure
- `src/output.rs` -> **98.9979%** Exposure
- `doc/screencast.sh` -> **98.2941%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/exec/mod.rs` -> **7** Orphaned Functions | **3** Duplicates
- `tests/testenv/mod.rs` -> **10** Orphaned Functions | **0** Duplicates
- `src/walk.rs` -> **3** Orphaned Functions | **3** Duplicates
- `src/hyperlink.rs` -> **1** Orphaned Functions | **4** Duplicates
- `src/cli.rs` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/filetypes.rs`** -> AI Confidence: **99.32%**
2. **`src/cli.rs`** -> AI Confidence: **99.31%**
3. **`src/filter/owner.rs`** -> AI Confidence: **99.31%**
4. **`src/fmt/input.rs`** -> AI Confidence: **99.31%**
5. **`doc/screencast.sh`** -> AI Confidence: **99.29%**
6. **`src/filesystem.rs`** -> AI Confidence: **99.24%**
7. **`src/output.rs`** -> AI Confidence: **99.24%**
8. **`tests/testenv/mod.rs`** -> AI Confidence: **99.24%**
9. **`src/hyperlink.rs`** -> AI Confidence: **99.23%**
10. **`scripts/create-deb.sh`** -> AI Confidence: **99.17%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/cli.rs` -> **20.0%** Exposure
- `src/exec/command.rs` -> **20.0%** Exposure
- `src/exec/mod.rs` -> **20.0%** Exposure
- `src/filter/time.rs` -> **20.0%** Exposure
- `src/fmt/mod.rs` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `src/exec/mod.rs` -> **96.6424%** Exposure
### Algorithmic DoS Exposure
- `src/exec/command.rs` -> **100.0%** Exposure
- `src/exec/mod.rs` -> **100.0%** Exposure
- `src/filesystem.rs` -> **100.0%** Exposure
- `src/fmt/mod.rs` -> **100.0%** Exposure
- `src/walk.rs` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `233` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/exec/mod.rs` (RUST) -> Cumulative Risk: **742.04**
- **Archetype:** `file_cluster_13` (Distance: 12.568 IQR)
- **Magnitude:** 300.92 | **LOC:** 474 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (97.7622%)
- **Heaviest Functions:** `execute_batch` (Impact: 56.3), `new_batch` (Impact: 43.1), `new` (Impact: 31.7)

### 2. `src/walk.rs` (RUST) -> Cumulative Risk: **687.58**
- **Archetype:** `file_cluster_13` (Distance: 13.077 IQR)
- **Magnitude:** 511.04 | **LOC:** 739 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 36.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Churn (96.36%)
- **Heaviest Functions:** `poll` (Impact: 137.0), `build_walker` (Impact: 75.6), `spawn_senders` (Impact: 64.0)

### 3. `src/hyperlink.rs` (RUST) -> Cumulative Risk: **598.32**
- **Archetype:** `file_cluster_0` (Distance: 11.45 IQR)
- **Magnitude:** 96.52 | **LOC:** 88 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9998%), Algorithmic Dos (99.9995%)
- **Heaviest Functions:** `fmt` (Impact: 28.1), `fmt` (Impact: 26.3), `encode` (Impact: 11.3)

### 4. `src/fmt/mod.rs` (RUST) -> Cumulative Risk: **595.06**
- **Archetype:** `file_cluster_13` (Distance: 11.2 IQR)
- **Magnitude:** 206.12 | **LOC:** 282 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (89.5647%)
- **Heaviest Functions:** `parse` (Impact: 65.5), `fmt` (Impact: 56.0), `generate` (Impact: 29.5)

### 5. `src/exec/command.rs` (RUST) -> Cumulative Risk: **587.6**
- **Archetype:** `file_cluster_13` (Distance: 11.705 IQR)
- **Magnitude:** 132.78 | **LOC:** 116 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), State Flux (99.6631%)
- **Heaviest Functions:** `execute_commands` (Impact: 55.7), `write` (Impact: 18.7), `handle_cmd_error` (Impact: 18.1)

### 6. `src/output.rs` (RUST) -> Cumulative Risk: **586.89**
- **Archetype:** `file_cluster_13` (Distance: 12.272 IQR)
- **Magnitude:** 198.26 | **LOC:** 176 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9878%), Tech Debt (99.8368%), State Flux (98.9979%)
- **Heaviest Functions:** `print_entry_colorized` (Impact: 69.9), `print_entry` (Impact: 46.4), `print_trailing_slash` (Impact: 19.3)

### 7. `src/filter/time.rs` (RUST) -> Cumulative Risk: **526.61**
- **Archetype:** `file_cluster_8` (Distance: 10.419 IQR)
- **Magnitude:** 123.74 | **LOC:** 203 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9136%), Tech Debt (82.775%)
- **Heaviest Functions:** `from_str` (Impact: 67.0), `is_time_filter_applicable` (Impact: 8.8), `applies_to` (Impact: 7.2)

### 8. `src/exec/job.rs` (RUST) -> Cumulative Risk: **523.31**
- **Archetype:** `file_cluster_13` (Distance: 10.044 IQR)
- **Magnitude:** 63.3 | **LOC:** 65 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (99.9542%), Verification (80.0%)
- **Heaviest Functions:** `job` (Impact: 35.2), `batch` (Impact: 21.1)

### 9. `src/exit_codes.rs` (RUST) -> Cumulative Risk: **508.38**
- **Archetype:** `file_cluster_8` (Distance: 8.342 IQR)
- **Magnitude:** 64.32 | **LOC:** 95 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (87.3091%), Verification (80.0%)
- **Heaviest Functions:** `exit` (Impact: 31.8), `from` (Impact: 8.4), `merge_exitcodes` (Impact: 8.2)

### 10. `src/filesystem.rs` (RUST) -> Cumulative Risk: **505.05**
- **Archetype:** `file_cluster_13` (Distance: 11.004 IQR)
- **Magnitude:** 134.74 | **LOC:** 157 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Verification (80.0%)
- **Heaviest Functions:** `absolute_path` (Impact: 106.7), `path_absolute_form` (Impact: 6.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/walk.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.077 IQR)
- **Top Global Matches:** file_cluster_13: 13.077, file_cluster_16: 13.388, file_cluster_0: 13.405
- **Magnitude:** 511.04 | **LOC:** 739 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 36.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (12.5172%), Tech Debt (57.9953%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 137.0 | O(N^6) | DB: 5)
  * `build_walker` (Impact: 75.6 | O(N^6) | DB: 1)
  * `spawn_senders` (Impact: 64.0 | O(N^5) | DB: 2)
  * `receive` (Impact: 44.1 | O(N^6) | DB: 1)
  * `send` (Impact: 35.7 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 100`, `args: 30`, `func_start: 21`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 50`, `duplicate_logic: 3`, `orphaned_logic: 3`
* *Architecture:* `io: 1`, `api: 2`, `concurrency: 7`, `import: 24`
* *Defense:* `safety: 60`, `doc: 43`, `test: 9`, `sync_locks: 7`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::mem, anyhow, RecvTimeoutError, std::sync::Arc, std::ffi::OsStr, crate::config::Config, ignore::WalkBuilder, SendError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.967 IQR)
- **Top Global Matches:** file_cluster_8: 8.967, file_cluster_7: 9.611, file_cluster_0: 9.762
- **Magnitude:** 469.52 | **LOC:** 2761 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (1.9598%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get_absolute_root_path` (Impact: 405.5 | O(2^N) | DB: 35)
  * `test_ignore_contain` (Impact: 4.7 | O(N^3))
  * `test_ignore_contain_precedence_over_dept` (Impact: 4.3 | O(N^3))
  * `test_ignore_contain_precedence_over_root` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 223`, `args: 107`, `func_start: 99`
* *Risk/State:* `safety_bypasses: 47`, `high_risk_execution: 1`, `state_mutation: 7`, `planned_debt: 6`, `orphaned_logic: 3`
* *Architecture:* `io: 16`, `import: 18`
* *Defense:* `safety: 6`, `doc: 63`, `test: 100`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` regex::escape, std::ffi::OsStr, crate::testenv::TestEnv, Uid, nix::unistd::Gid, std::io::Write, test_case::test_case, std::os::unix::ffi::OsStrExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exec/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.568 IQR)
- **Top Global Matches:** file_cluster_13: 12.568, file_cluster_0: 12.68, file_cluster_16: 12.695
- **Magnitude:** 300.92 | **LOC:** 474 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (11.4281%), Tech Debt (97.7622%)
**Top Internal Functions/Classes:**
  * `execute_batch` (Impact: 56.3 | O(N^6) | DB: 3)
  * `new_batch` (Impact: 43.1 | O(N^6))
  * `new` (Impact: 31.7 | O(N^4) | DB: 3)
  * `finish` (Impact: 30.6 | O(N^4) | DB: 1)
  * `push` (Impact: 28.9 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 55`, `args: 18`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 31`, `duplicate_logic: 3`, `orphaned_logic: 7`
* *Architecture:* `io: 1`, `api: 8`, `import: 12`
* *Defense:* `safety: 37`, `doc: 12`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` crate::fmt::FormatTemplate, crate::exit_codes::ExitCode, std::process::Stdio, crate::exec::command::OutputBuffer, std::iter, argmax::Command, Token, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/testenv/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.616 IQR)
- **Top Global Matches:** file_cluster_13: 11.616, file_cluster_0: 11.64, file_cluster_8: 11.681
- **Magnitude:** 273.52 | **LOC:** 345 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (4.8633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `create_working_directory` (Impact: 53.8 | O(N^3) | DB: 9)
    * *Intent:* /// Create the working directory and the test files.
  * `create_broken_symlink` (Impact: 25.9 | O(N^4) | DB: 4)
    * *Intent:* /// Create a broken symlink at the given path in the temp_dir.
  * `assert_error_subdirectory` (Impact: 23.2 | O(N^5))
    * *Intent:* /// Assert that calling *fd* in the specified path under the root working directory, /// and with th...
  * `normalize_output` (Impact: 21.0 | O(N^4) | DB: 2)
    * *Intent:* /// Normalize the output for comparison.
  * `run_command` (Impact: 12.8 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 49`, `args: 28`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 15`, `orphaned_logic: 10`
* *Architecture:* `io: 7`, `api: 16`, `import: 8`
* *Defense:* `safety: 21`, `doc: 27`, `test: 1`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tempfile::TempDir, std::io::self, std::fs, std::os::windows, Write, PathBuf, std::process, std::os::unix...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.04 IQR)
- **Top Global Matches:** file_cluster_0: 12.04, file_cluster_16: 12.327, file_cluster_8: 12.328
- **Magnitude:** 214.42 | **LOC:** 949 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.9464%), Tech Debt (16.1009%)
**Top Internal Functions/Classes:**
  * `search_paths` (Impact: 49.8 | O(N^6))
    * *Intent:* /// Limit the search to a single result and quit immediately. /// This is an alias for '--max-result...
  * `gen_completions` (Impact: 26.5 | O(2^N))
    * *Intent:* /// The directory where the filesystem search is rooted (optional). If /// omitted, search the curre...
  * `normalize_path` (Impact: 17.8 | O(N^3))
  * `ensure_current_directory_exists` (Impact: 16.4 | O(N^3))
  * `max_results` (Impact: 14.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 26`, `args: 21`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 3`, `orphaned_logic: 4`
* *Architecture:* `api: 46`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 36`, `doc: 226`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` clap::
    Arg, ValueEnum, std::num::NonZeroUsize, value_parser, crate::error::print_error, normpath::PathExt, Command, ArgAction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fmt/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.2 IQR)
- **Top Global Matches:** file_cluster_13: 11.2, file_cluster_8: 11.358, file_cluster_0: 11.448
- **Magnitude:** 206.12 | **LOC:** 282 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (8.5525%), Tech Debt (35.3368%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 65.5 | O(N^6) | DB: 4)
  * `fmt` (Impact: 56.0 | O(2^N) | DB: 1)
  * `generate` (Impact: 29.5 | O(N^6) | DB: 1)
    * *Intent:* /// Generate a result string from this template. If path_separator is Some, then it will replace ///...
  * `token_from_pattern_id` (Impact: 6.5 | O(N^2))
  * `all_placeholders` (Impact: 5.7 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 49`, `args: 10`, `func_start: 9`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 25`, `orphaned_logic: 4`
* *Architecture:* `api: 5`, `import: 12`
* *Defense:* `safety: 15`, `doc: 15`, `test: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Path, dirname, std::ffi::OsStr, remove_extension, super::*, aho_corasick::AhoCorasick, std::borrow::Cow, Token::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/output.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.272 IQR)
- **Top Global Matches:** file_cluster_13: 12.272, file_cluster_11: 12.358, file_cluster_0: 12.406
- **Magnitude:** 198.26 | **LOC:** 176 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (33.0418%), Tech Debt (99.8368%)
**Top Internal Functions/Classes:**
  * `print_entry_colorized` (Impact: 69.9 | O(N^4) | DB: 3)
    * *Intent:* // TODO: this function is performance critical and can probably be optimized
  * `print_entry` (Impact: 46.4 | O(N^2) | DB: 2)
    * *Intent:* // TODO: this function is performance critical and can probably be optimized
  * `print_trailing_slash` (Impact: 19.3 | O(N^4) | DB: 1)
    * *Intent:* // Display a trailing slash if the path is a directory and the config option is enabled. // If the p...
  * `print_entry_uncolorized` (Impact: 17.6 | O(N^2) | DB: 1)
  * `print_entry_uncolorized_base` (Impact: 7.4 | O(N^1) | DB: 2)
    * *Intent:* // TODO: this function is performance critical and can probably be optimized
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 39`, `args: 10`, `func_start: 8`
* *Risk/State:* `state_mutation: 25`, `planned_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 1`, `api: 1`, `import: 8`
* *Defense:* `safety: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Style, std::io::self, crate::config::Config, std::os::unix::ffi::OsStrExt, std::borrow::Cow, crate::fmt::FormatTemplate, LsColors, Write...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filetypes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.123 IQR)
- **Top Global Matches:** file_cluster_8: 9.123, file_cluster_13: 9.242, file_cluster_0: 9.633
- **Magnitude:** 153.18 | **LOC:** 44 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.9982%), Tech Debt (51.602%)
**Top Internal Functions/Classes:**
  * `should_ignore` (Impact: 141.4 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 7`, `args: 16`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `orphaned_logic: 1`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::dir_entry, crate::filesystem, faccess::PathExt
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filesystem.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.004 IQR)
- **Top Global Matches:** file_cluster_13: 11.004, file_cluster_0: 11.043, file_cluster_8: 11.283
- **Magnitude:** 134.74 | **LOC:** 157 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.3819%), Tech Debt (14.9005%)
**Top Internal Functions/Classes:**
  * `absolute_path` (Impact: 106.7 | O(N^4) | DB: 1)
  * `path_absolute_form` (Impact: 6.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 26`, `args: 20`, `func_start: 17`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 16`, `import: 13`
* *Defense:* `safety: 14`, `doc: 6`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::os::unix::fs::FileTypeExt, std::ffi::OsStr, std::os::unix::ffi::OsStrExt, std::io, std::borrow::Cow, std::fs, super::strip_current_dir, normpath::PathExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exec/command.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.705 IQR)
- **Top Global Matches:** file_cluster_13: 11.705, file_cluster_8: 11.871, file_cluster_16: 12.196
- **Magnitude:** 132.78 | **LOC:** 116 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (31.0889%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `execute_commands` (Impact: 55.7 | O(N^5) | DB: 5)
    * *Intent:* /// Executes a command.
  * `write` (Impact: 18.7 | O(N^3) | DB: 2)
  * `handle_cmd_error` (Impact: 18.1 | O(N^4))
  * `new` (Impact: 8.3 | O(2^N))
  * `push` (Impact: 6.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 26`, `args: 6`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 2`, `api: 5`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 13`, `doc: 1`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::io, crate::error::print_error, crate::exit_codes::ExitCode, argmax::Command, std::io::Write
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filter/owner.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.036 IQR)
- **Top Global Matches:** file_cluster_13: 12.036, file_cluster_8: 12.091, file_cluster_0: 12.108
- **Magnitude:** 128.96 | **LOC:** 141 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.7408%), Tech Debt (30.8939%)
**Top Internal Functions/Classes:**
  * `from_string` (Impact: 73.6 | O(N^5) | DB: 1)
    * *Intent:* /// Parses an owner constraint /// Returns an error if the string is invalid /// Returns Ok(None) wh...
  * `parse` (Impact: 22.6 | O(N^4))
  * `filter_ignore` (Impact: 10.7 | O(N^3))
    * *Intent:* /// If self is a no-op (ignore both uid and gid) then return `None`, otherwise wrap in a `Some`
  * `check` (Impact: 7.3 | O(N^3))
  * `matches` (Impact: 5.4 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 23`, `args: 12`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 4`, `import: 6`
* *Defense:* `safety: 36`, `doc: 4`, `test: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` nix::unistd::Group, super::Check::*, anyhow, std::os::unix::fs::MetadataExt, std::fs, User, anyhow::Result, super::OwnerFilter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filter/time.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.419 IQR)
- **Top Global Matches:** file_cluster_8: 10.419, file_cluster_0: 10.583, file_cluster_16: 10.68
- **Magnitude:** 123.74 | **LOC:** 203 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.8551%), Tech Debt (82.775%)
**Top Internal Functions/Classes:**
  * `from_str` (Impact: 67.0 | O(N^5))
  * `is_time_filter_applicable` (Impact: 8.8 | O(N^3) | DB: 2)
  * `applies_to` (Impact: 7.2 | O(N^3))
  * `new` (Impact: 4.2 | O(N^3))
  * `drop` (Impact: 4.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 30`, `args: 15`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 4`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 20`, `doc: 2`, `test: 27`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` civil::DateTime, SystemTime, std::time::Duration, Timestamp, super::*, jiff::Span, tz::TimeZone, Zoned...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/regex_helper.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 11.458 IQR)
- **Top Global Matches:** file_cluster_17: 11.458, file_cluster_8: 11.471, file_cluster_13: 11.526
- **Magnitude:** 112.34 | **LOC:** 106 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.6772%), Tech Debt (76.1067%)
**Top Internal Functions/Classes:**
  * `hir_matches_strings_with_leading_dot` (Impact: 49.5 | O(N^5) | DB: 1)
    * *Intent:* /// See above.
  * `hir_has_uppercase_char` (Impact: 41.1 | O(2^N))
    * *Intent:* /// Determine if a regex expression contains a literal uppercase character.
  * `pattern_has_uppercase_char` (Impact: 3.4 | O(N^2) | DB: 1)
    * *Intent:* /// Determine if a regex pattern contains a literal uppercase character.
  * `pattern_matches_strings_with_leading_dot` (Impact: 3.4 | O(N^2) | DB: 1)
    * *Intent:* /// Determine if a regex pattern only matches strings starting with a literal dot (hidden files)
  * `pattern_has_uppercase_char_simple` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 14`, `args: 16`, `func_start: 7`
* *Risk/State:* `state_mutation: 5`, `orphaned_logic: 3`
* *Architecture:* `api: 2`, `import: 4`
* *Defense:* `safety: 10`, `doc: 4`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` regex_syntax::hir::*, regex_syntax::ParserBuilder, regex_syntax::hir::Hir
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filter/size.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.797 IQR)
- **Top Global Matches:** file_cluster_8: 8.797, file_cluster_0: 9.33, file_cluster_16: 9.453
- **Magnitude:** 108.06 | **LOC:** 220 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.1154%), Tech Debt (39.4733%)
**Top Internal Functions/Classes:**
  * `parse_opt` (Impact: 77.7 | O(N^3))
  * `from_string` (Impact: 8.2 | O(N^3))
  * `is_within` (Impact: 7.3 | O(N^3))
  * `is_within_less_than` (Impact: 2.0 | O(N^1))
  * `is_within_less_than_equal` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 22`, `args: 12`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `orphaned_logic: 4`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `safety: 11`, `doc: 1`, `test: 13`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` super::*, anyhow::anyhow, std::sync::OnceLock, regex::Regex
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/hyperlink.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.45 IQR)
- **Top Global Matches:** file_cluster_0: 11.45, file_cluster_13: 11.491, file_cluster_16: 11.652
- **Magnitude:** 96.52 | **LOC:** 88 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (16.9166%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `fmt` (Impact: 28.1 | O(2^N) | DB: 1)
  * `fmt` (Impact: 26.3 | O(2^N) | DB: 1)
  * `encode` (Impact: 11.3 | O(N^3) | DB: 1)
  * `host` (Impact: 9.4 | O(N^4))
  * `new` (Impact: 6.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 15`, `args: 13`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 4`, `orphaned_logic: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 8`, `test: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Write, std::sync::OnceLock, crate::filesystem::absolute_path, std::fmt::self, std::path::Path, super::*, PathBuf, Formatter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exit_codes.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.342 IQR)
- **Top Global Matches:** file_cluster_8: 8.342, file_cluster_0: 8.778, file_cluster_16: 8.938
- **Magnitude:** 64.32 | **LOC:** 95 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.6115%), Tech Debt (76.9183%)
**Top Internal Functions/Classes:**
  * `exit` (Impact: 31.8 | O(2^N))
    * *Intent:* /// Exit the process with the appropriate code.
  * `from` (Impact: 8.4 | O(N^3))
  * `merge_exitcodes` (Impact: 8.2 | O(N^2))
  * `general_error_if_at_least_one_error` (Impact: 3.7 | O(N^2))
  * `success_if_no_error` (Impact: 3.0 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 10`, `args: 7`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 1`, `doc: 1`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` signal, Signal, std::process, super::*, raise, nix::sys::signal::SigHandler
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/exec/job.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.93%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.044 IQR)
- **Top Global Matches:** file_cluster_13: 10.044, file_cluster_8: 10.247, file_cluster_16: 10.352
- **Magnitude:** 63.3 | **LOC:** 65 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^5) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (5.7533%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `job` (Impact: 35.2 | O(N^5) | DB: 1)
    * *Intent:* /// An event loop that listens for inputs from the `rx` receiver. Each received input will /// gener...
  * `batch` (Impact: 21.1 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 4`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 48.877
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 0):` crate::config::Config, crate::error::print_error, merge_exitcodes, crate::walk::WorkerResult, crate::exit_codes::ExitCode, super::CommandSet
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/config.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.206 IQR)
- **Top Global Matches:** file_cluster_13: 14.206, file_cluster_16: 14.245, file_cluster_0: 14.364
- **Magnitude:** 41.78 | **LOC:** 144 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (34.3407%)
**Top Internal Functions/Classes:**
  * `is_printing` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 38`, `import: 8`
* *Defense:* `safety: 14`, `doc: 50`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` regex::bytes::RegexSet, crate::filetypes::FileTypes, crate::filter::SizeFilter, sync::Arc, crate::fmt::FormatTemplate, crate::filter::OwnerFilter, TimeFilter, lscolors::LsColors...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fmt/input.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.505 IQR)
- **Top Global Matches:** file_cluster_8: 8.505, file_cluster_13: 8.924, file_cluster_7: 9.123
- **Magnitude:** 36.6 | **LOC:** 88 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (13.8669%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `dirname` (Impact: 20.6 | O(N^4))
    * *Intent:* /// Removes the basename from the path.
  * `correct` (Impact: 3.1 | O(N^2))
  * `remove_extension` (Impact: 2.4 | O(N^1))
    * *Intent:* /// Removes the extension from the path
  * `basename` (Impact: 2.1 | O(N^1))
    * *Intent:* /// Removes the parent component of the path
  * `dirname_root` (Impact: 2.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 11`, `args: 8`, `func_start: 6`
* *Risk/State:* `duplicate_logic: 2`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 3`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::ffi::OsStr, std::path::MAIN_SEPARATOR_STR, crate::filesystem::strip_current_dir, std::path::Path, super::*, PathBuf, OsString
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/dir_entry.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.382 IQR)
- **Top Global Matches:** file_cluster_8: 6.382, file_cluster_13: 7.45, file_cluster_7: 7.469
- **Magnitude:** 18.56 | **LOC:** 156 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 9`, `class_start: 9`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Style, Metadata, std::fs::FileType, std::cell::OnceCell, lscolors::Colorable, crate::config::Config, LsColors, crate::filesystem::strip_current_dir...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `doc/screencast.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.422 IQR)
- **Top Global Matches:** file_cluster_8: 10.422, file_cluster_7: 11.151, file_cluster_0: 11.375
- **Magnitude:** 17.98 | **LOC:** 65 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (25.8979%), Tech Debt (96.3358%)
**Top Internal Functions/Classes:**
  * `type` (Impact: 7.5 | O(2^N) | DB: 1)
  * `enter` (Impact: 2.2 | O(N^1) | DB: 2)
  * `__global_context__` (Impact: 1.5 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `args: 1`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 6`, `orphaned_logic: 1`
* *Architecture:* None
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 6.084 IQR)
- **Top Global Matches:** file_cluster_8: 6.084, file_cluster_7: 7.338, file_cluster_1: 7.547
- **Magnitude:** 17.58 | **LOC:** 38 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (6.3189%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `func_start: 6`
* *Risk/State:* None
* *Architecture:* `io: 5`, `api: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/filter/mod.rs` (RUST | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_13` (Drift: 7.056 IQR)
- **Top Global Matches:** file_cluster_13: 7.056, file_cluster_8: 7.295, file_cluster_0: 7.503
- **Magnitude:** 17.16 | **LOC:** 12 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` self::time::TimeFilter, self::owner::OwnerFilter, self::size::SizeFilter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 17.1 | **LOC:** 855 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `README.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 15.72 | **LOC:** 786 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 26.42
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/hyperlink.rs` (RUST) | Magnitude: 96.52 | Delta: **0.041 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 15, args: 13, branch: 11
- `src/cli.rs` (RUST) | Magnitude: 214.42 | Delta: **0.287 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 430, doc: 226, decorators: 67, api: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/create-deb.sh` (SHELL) | Magnitude: 6.38 | Delta: **0.232 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 51, indent_spaces: 47, state_mutation: 36, io: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/testenv/mod.rs` (RUST) | Magnitude: 273.52 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 222, structural_boundaries: 49, branch: 32, args: 28
- `src/config.rs` (RUST) | Magnitude: 41.78 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 50, indent_spaces: 41, api: 38, encapsulation: 38
- `src/filesystem.rs` (RUST) | Magnitude: 134.74 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 26, branch: 20, args: 20
- `src/filter/owner.rs` (RUST) | Magnitude: 128.96 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 102, safety: 36, structural_boundaries: 23, branch: 22
- `src/output.rs` (RUST) | Magnitude: 198.26 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 39, branch: 32, state_mutation: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/error.rs` (RUST) | Magnitude: 3.46 | Delta: **0.424 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: generics: 2, structural_boundaries: 1, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/regex_helper.rs` (RUST) | Magnitude: 112.34 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, args: 16, structural_boundaries: 14, test: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/filetypes.rs` (RUST) | Magnitude: 153.18 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, branch: 26, args: 16, api: 11
- `scripts/version-bump.sh` (SHELL) | Magnitude: 1.37 | Delta: **0.149 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 6, regex_execution: 5, branch: 4, serialization_parsing: 4
- `src/filter/time.rs` (RUST) | Magnitude: 123.74 | Delta: **0.164 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 153, structural_boundaries: 30, test: 27, safety_bypasses: 26
- `src/fmt/input.rs` (RUST) | Magnitude: 36.6 | Delta: **0.419 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, branch: 18, structural_boundaries: 11, args: 8
- `src/exit_codes.rs` (RUST) | Magnitude: 64.32 | Delta: **0.436 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 66, test: 12, structural_boundaries: 10, args: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/walk.rs` -> Churn: **96.36%** | Cog Load: 12.5172% | Debt: 57.9953%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/exec/mod.rs` -> **Thayne McCombs** (100.0% isolated ownership) | Magnitude: 300.92
- `tests/testenv/mod.rs` -> **Andreas Stergiopoulos** (100.0% isolated ownership) | Magnitude: 273.52
- `src/fmt/mod.rs` -> **Thayne McCombs** (100.0% isolated ownership) | Magnitude: 206.12
- `src/output.rs` -> **Thayne McCombs** (100.0% isolated ownership) | Magnitude: 198.26
- `src/exec/command.rs` -> **Thayne McCombs** (100.0% isolated ownership) | Magnitude: 132.78

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/exec/job.rs` -> **Severity: 1.062** (Embedded: 0.0278 * Error Risk: 38.2252%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/exec/job.rs` -> **Severity: 4887.7** (Blast Radius: 48.877 * Doc Risk: 100.0%)
- `src/config.rs` -> **Severity: 2642.0** (Blast Radius: 26.42 * Doc Risk: 100.0%)
- `src/exec/command.rs` -> **Severity: 2642.0** (Blast Radius: 26.42 * Doc Risk: 100.0%)
- `src/exec/mod.rs` -> **Severity: 2642.0** (Blast Radius: 26.42 * Doc Risk: 100.0%)
- `src/exit_codes.rs` -> **Severity: 2642.0** (Blast Radius: 26.42 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
