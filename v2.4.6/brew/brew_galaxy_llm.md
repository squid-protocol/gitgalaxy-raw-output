# ARCHITECTURAL_BRIEF: brew
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/brew` |
| **Timestamp** | `2026-08-03T19:24:48.835149+00:00` |
| **Scan Duration** | `1.34s` |
| **Git Branch** | `main` |
| **Git Commit** | `ff29aa966b3127a32e5637bde7d5c0195186d6d4` |
| **Git Remote** | `https://github.com/Homebrew/brew` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 124 malicious artifacts.

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
| Total Artifacts | 2828 |
| Analyzed Artifacts (Scanned) | 136 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2692 |
| Total LOC | 13917 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 4.8% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6544 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1923 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1429 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 89 | 10301 | 65.4% |
| RUST | 19 | 2333 | 14.0% |
| SHELL | 12 | 1077 | 8.8% |
| MARKDOWN | 7 | 0 | 5.1% |
| PLAINTEXT | 4 | 1 | 2.9% |
| SWIFT | 3 | 127 | 2.2% |
| DOCKERFILE | 1 | 78 | 0.7% |
| XML | 1 | 0 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.939`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 94 | 69.1% |
| file_cluster_13 | 17 | 12.5% |
| file_cluster_12 | 7 | 5.1% |
| file_cluster_11 | 2 | 1.5% |
| file_cluster_0 | 2 | 1.5% |
| Unknown | 1 | 0.7% |
| file_cluster_17 | 1 | 0.7% |
| file_cluster_4 | 1 | 0.7% |
| file_cluster_16 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 7.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2692*

**Composition by Extension & Reason:**
- `.rb`: 1785x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rbi`: 301x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 184x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3531 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2680 LOC)
- `.pc`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gz`: 32x Excluded (Explicitly Denied Extension: '.gz')
- `.sh`: 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 12x Excluded (Explicitly Denied Extension: '.zip')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.erb`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.diff`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tbz`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 26.0 | 15.7 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 18.3 | 4.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 28.7 | 2.3 | 80.0 |
| API Exposure | 0.0 | 10.2 | 2.1 | 1.5 | 0.0 |
| Concurrency Exposure | 0.0 | 99.8 | 2.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 41.6 | 23.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 22.9 | 0.4 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.8 | 1.0 | 0.1 | 0.0 |
| Volatility Exposure | 0.0 | 80.7 | 16.7 | 9.6 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 31.6 | 17.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.5 | 2.8 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 28.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Library/Homebrew/utils/shfmt.sh` (Hits: 38)
- `bin/brew` (Hits: 32)
- `Library/Homebrew/utils/helpers.sh` (Hits: 31)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **output.rb** (`Library/Homebrew/utils/output.rb`) — 14 inbound connections
2. **curl.rb** (`Library/Homebrew/utils/curl.rb`) — 8 inbound connections
3. **github.rb** (`Library/Homebrew/utils/github.rb`) — 3 inbound connections
4. **actions.rb** (`Library/Homebrew/utils/github/actions.rb`) — 3 inbound connections
5. **api.rb** (`Library/Homebrew/utils/github/api.rb`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **fetch.rs** (`Library/Homebrew/rust/brew-rs/src/commands/fetch.rs`) — 55 outbound dependencies
2. **install.rs** (`Library/Homebrew/rust/brew-rs/src/commands/install.rs`) — 20 outbound dependencies
3. **list.rs** (`Library/Homebrew/rust/brew-rs/src/commands/list.rs`) — 19 outbound dependencies
4. **homebrew.rs** (`Library/Homebrew/rust/brew-rs/src/homebrew.rs`) — 18 outbound dependencies
5. **analytics.rb** (`Library/Homebrew/utils/analytics.rb`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Utils` (@ `Library/Homebrew/utils/analytics.rb`) -> Impact: **2153.2** | LOC: 505
  * *Intent:* # Helper module for fetching and reporting analytics data. module Analytics INFLUX_BUCKET = "analytics" INFLUX_TOKEN = "iVdsgJ_OjvTYGAA79gOfWlA_fX0QCu...
- `Utils_[Truncated]` (@ `Library/Homebrew/utils/curl.rb`) -> Impact: **1676.3** | LOC: 767
  * *Intent:* # Helper function for interacting with `curl`. module Curl include SystemCommand::Mixin extend SystemCommand::Mixin include Utils::Output::Mixin exten...
- `GitHub_[Truncated]` (@ `Library/Homebrew/utils/github.rb`) -> Impact: **1560.8** | LOC: 1026
  * *Intent:* # A module that interfaces with GitHub, code like PAT scopes, credential handling and API errors. # # @api internal
- `PyPI_[Truncated]` (@ `Library/Homebrew/utils/pypi.rb`) -> Impact: **1363.2** | LOC: 525
  * *Intent:* # Helper functions for updating PyPI resources.
- `Anonymous_Block_[Truncated]` (@ `Library/Homebrew/test/utils/curl_spec.rb`) -> Impact: **1223.5** | LOC: 827
- `Utils` (@ `Library/Homebrew/utils/output.rb`) -> Impact: **1105.5** | LOC: 286
  * *Intent:* # typed: strict # frozen_string_literal: true
- `Utils_[Truncated]` (@ `Library/Homebrew/utils/bottles.rb`) -> Impact: **841.3** | LOC: 390
  * *Intent:* # Helper functions for bottles. # # @api internal module Bottles class << self # Gets the tag for the running OS. # # @api internal sig { params(tag: ...
- `GitHub_[Truncated]` (@ `Library/Homebrew/utils/github/api.rb`) -> Impact: **829.6** | LOC: 470
- `Utils` (@ `Library/Homebrew/utils/git.rb`) -> Impact: **446.3** | LOC: 197
  * *Intent:* # Helper functions for querying Git information. # # @see GitRepository module Git extend SystemCommand::Mixin sig { returns(T::Boolean) } def self.av...
- `Anonymous_Block` (@ `Library/Homebrew/utils/shfmt.sh`) -> Impact: **430.2** | LOC: 374
  * *Intent:* # HOMEBREW_PREFIX is set by extend/ENV/super.rb # shellcheck disable=SC2154

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Utils` (@ `Library/Homebrew/utils/analytics.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Helper module for fetching and reporting analytics data. module Analytics INFLUX_BUCKET = "analytics" INFLUX_TOKEN = "iVdsgJ_OjvTYGAA79gOfWlA_fX0QCu...
- `Utils` (@ `Library/Homebrew/utils/gzip.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Helper functions for creating gzip files. module Gzip extend ::Utils::Output::Mixin # Apple's gzip also uses zlib so use the same buffer size here. ...
- `Utils` (@ `Library/Homebrew/utils/svn.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Helper functions for querying SVN information. module Svn class << self include SystemCommand::Mixin include Utils::Output::Mixin sig { returns(T::B...
- `Utils` (@ `Library/Homebrew/utils/tar.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Helper functions for interacting with tar files. module Tar class << self include SystemCommand::Mixin include Utils::Output::Mixin TAR_FILE_EXTENSI...
- `Utils` (@ `Library/Homebrew/utils/output.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # typed: strict # frozen_string_literal: true
- `run` (@ `Library/Homebrew/rust/brew-rs/src/commands/list.rs`) -> **O(2^N) [Recursive]**
- `width` (@ `Library/Homebrew/rust/brew-rs/src/utils/tty.rs`) -> **O(2^N) [Recursive]**
- `Utils` (@ `Library/Homebrew/utils/backtrace.rb`) -> **O(2^N) [Recursive]**
- `Utils` (@ `Library/Homebrew/utils/git.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # Helper functions for querying Git information. # # @see GitRepository module Git extend SystemCommand::Mixin sig { returns(T::Boolean) } def self.av...
- `Utils` (@ `Library/Homebrew/utils/path.rb`) -> **O(2^N) [Recursive]**
  * *Intent:* # typed: strict # frozen_string_literal: true

### Highest Data Gravity (Database Complexity)
- `Anonymous_Block` (@ `Library/Homebrew/utils/shfmt.sh`) -> DB Complexity: **122**
  * *Intent:* # HOMEBREW_PREFIX is set by extend/ENV/super.rb # shellcheck disable=SC2154
- `symlink_target_directory_[Truncated]` (@ `bin/brew`) -> DB Complexity: **104**
- `PyPI_[Truncated]` (@ `Library/Homebrew/utils/pypi.rb`) -> DB Complexity: **59**
  * *Intent:* # Helper functions for updating PyPI resources.
- `Utils_[Truncated]` (@ `Library/Homebrew/utils/curl.rb`) -> DB Complexity: **55**
  * *Intent:* # Helper function for interacting with `curl`. module Curl include SystemCommand::Mixin extend SystemCommand::Mixin include Utils::Output::Mixin exten...
- `GitHub_[Truncated]` (@ `Library/Homebrew/utils/github.rb`) -> DB Complexity: **48**
  * *Intent:* # A module that interfaces with GitHub, code like PAT scopes, credential handling and API errors. # # @api internal
- `opoo` (@ `Library/Homebrew/utils/helpers.sh`) -> DB Complexity: **42**
- `lock_[Truncated]` (@ `Library/Homebrew/utils/lock.sh`) -> DB Complexity: **37**
  * *Intent:* # Create a lock using `flock(2)`. A command name with arguments is required as # first argument. The lock will be automatically unlocked when the shel...
- `setup-ruby-path` (@ `Library/Homebrew/utils/ruby.sh`) -> DB Complexity: **37**
  * *Intent:* # HOMEBREW_LINUX is set by brew.sh # shellcheck disable=SC2154
- `Anonymous_Block` (@ `Library/Homebrew/test/utils/git_spec.rb`) -> DB Complexity: **34**
- `Anonymous_Block` (@ `Library/Homebrew/test/utils/inreplace_spec.rb`) -> DB Complexity: **31**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `Library/Homebrew/utils` | 49 | 15151.96 | 28.04% | 20.98% |
| `Library/Homebrew/api` | 1 | 5000.0 | 0.0% | 0.0% |
| `Library/Homebrew/test/utils` | 30 | 2744.72 | 22.74% | 0.0% |
| `Library/Homebrew/rust/brew-rs/src/commands` | 10 | 2497.62 | 11.19% | 17.09% |
| `Library/Homebrew/utils/github` | 3 | 1109.64 | 21.49% | 33.33% |
| `bin` | 1 | 406.86 | 92.43% | 98.4% |
| `Library/Homebrew/rust/brew-rs/src` | 6 | 293.16 | 8.36% | 43.31% |
| `Library/Homebrew/rust/brew-rs/src/utils` | 3 | 247.28 | 7.22% | 20.99% |
| `Library/Homebrew/test/utils/ast` | 2 | 227.08 | 28.75% | 0.0% |
| `Library/Homebrew/extend/os/mac/utils` | 2 | 130.1 | 9.76% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `Library/Homebrew/cask/utils/rmdir.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/bash/brew-sh-prompt-bashrc.bash` -> **100.0%** Exposure
- `Library/Homebrew/utils/zsh/brew-sh-prompt-zshrc.zsh` -> **100.0%** Exposure
- `package/scripts/postinstall` -> **100.0%** Exposure
- `package/scripts/preinstall` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `Library/Homebrew/cask/utils/quarantine.swift` -> **100.0%** Exposure
- `Library/Homebrew/cask/utils/trash.swift` -> **100.0%** Exposure
- `Library/Homebrew/cask/utils/rmdir.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/analytics.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/ruby.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> **14** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/test/utils/ast/formula_ast_spec.rb` -> **1** Orphaned Functions | **10** Duplicates
- `Library/Homebrew/utils/gems.rb` -> **7** Orphaned Functions | **2** Duplicates
- `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` -> **9** Orphaned Functions | **0** Duplicates
- `bin/brew` -> **2** Orphaned Functions | **5** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`Library/Homebrew/utils/github.rb`** -> AI Confidence: **99.39%**
2. **`Library/Homebrew/utils/curl.rb`** -> AI Confidence: **99.34%**
3. **`Library/Homebrew/utils/pypi.rb`** -> AI Confidence: **99.34%**
4. **`Library/Homebrew/utils/fork.rb`** -> AI Confidence: **99.32%**
5. **`Library/Homebrew/utils/analytics.rb`** -> AI Confidence: **99.31%**
6. **`Library/Homebrew/utils/github/api.rb`** -> AI Confidence: **99.31%**
7. **`Library/Homebrew/rust/brew-rs/src/commands/fetch.rs`** -> AI Confidence: **99.31%**
8. **`Library/Homebrew/rust/brew-rs/src/commands/install.rs`** -> AI Confidence: **99.31%**
9. **`Dockerfile`** -> AI Confidence: **99.29%**
10. **`Library/Homebrew/cask/utils/rmdir.sh`** -> AI Confidence: **99.29%**
11. **`Library/Homebrew/utils/helpers.sh`** -> AI Confidence: **99.29%**
12. **`Library/Homebrew/utils/wrapper.sh`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `Library/Homebrew/utils/lock.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/shfmt.sh` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/analytics_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/ast/formula_ast_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/autoremove_spec.rb` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `Library/Homebrew/test/utils/curl_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/git_repository_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/git_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/inreplace_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/utils/attestation.rb` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `Library/Homebrew/utils/ruby.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/shfmt.sh` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/analytics_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/git_spec.rb` -> **100.0%** Exposure
- `Library/Homebrew/test/utils/string_inreplace_extension_spec.rb` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `343` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `Library/Homebrew/utils/gems.rb` (RUBY) -> Cumulative Risk: **831.22**
- **Archetype:** `file_cluster_8` (Distance: 11.283 IQR)
- **Magnitude:** 330.94 | **LOC:** 334 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `self.odie_if_defined` (Impact: 117.4), `self.install_bundler_gems!` (Impact: 82.8), `Anonymous_Block` (Impact: 31.9)

### 2. `Library/Homebrew/utils/shfmt.sh` (SHELL) -> Cumulative Risk: **824.16**
- **Archetype:** `file_cluster_11` (Distance: 16.269 IQR)
- **Magnitude:** 611.52 | **LOC:** 453 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 430.2), `Anonymous_Block_[Truncated]` (Impact: 27.6), `Anonymous_Block` (Impact: 14.8)

### 3. `Library/Homebrew/utils/attestation.rb` (RUBY) -> Cumulative Risk: **749.83**
- **Archetype:** `file_cluster_13` (Distance: 11.563 IQR)
- **Magnitude:** 68.18 | **LOC:** 74 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Utils_[Truncated]` (Impact: 51.8), `__global_context__` (Impact: 1.4)

### 4. `Library/Homebrew/utils/ruby.sh` (SHELL) -> Cumulative Risk: **723.5**
- **Archetype:** `file_cluster_4` (Distance: 14.047 IQR)
- **Magnitude:** 233.0 | **LOC:** 205 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (97.6645%)
- **Heaviest Functions:** `setup-ruby-path` (Impact: 91.5), `need_vendored_ruby` (Impact: 10.6), `can_use_ruby_from_path` (Impact: 10.4)

### 5. `Library/Homebrew/rust/brew-rs/src/homebrew.rs` (RUST) -> Cumulative Risk: **672.18**
- **Archetype:** `file_cluster_13` (Distance: 11.16 IQR)
- **Magnitude:** 163.04 | **LOC:** 217 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.4472%)
- **Heaviest Functions:** `list_directories` (Impact: 31.1), `print_sections` (Impact: 21.9), `env_bool` (Impact: 18.9)

### 6. `Library/Homebrew/utils/lock.sh` (SHELL) -> Cumulative Risk: **650.88**
- **Archetype:** `file_cluster_12` (Distance: 11.87 IQR)
- **Magnitude:** 71.78 | **LOC:** 76 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (99.9994%), Cognitive Load (93.3332%)
- **Heaviest Functions:** `lock_[Truncated]` (Impact: 65.7)

### 7. `Library/Homebrew/utils/fork.rb` (RUBY) -> Cumulative Risk: **649.36**
- **Archetype:** `file_cluster_8` (Distance: 9.082 IQR)
- **Magnitude:** 220.26 | **LOC:** 127 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Utils` (Impact: 212.1), `__global_context__` (Impact: 1.3)

### 8. `Library/Homebrew/utils/wrapper.sh` (SHELL) -> Cumulative Risk: **643.08**
- **Archetype:** `file_cluster_13` (Distance: 12.903 IQR)
- **Magnitude:** 150.26 | **LOC:** 83 | **CtrlFlow:** 81.0% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (95.7035%), Cognitive Load (94.1004%)
- **Heaviest Functions:** `odie-with-wrapper-message` (Impact: 136.7), `__global_context__` (Impact: 2.4)

### 9. `Library/Homebrew/utils/spdx.rb` (RUBY) -> Cumulative Risk: **635.62**
- **Archetype:** `file_cluster_8` (Distance: 10.461 IQR)
- **Magnitude:** 449.88 | **LOC:** 272 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Verification (80.0%)
- **Heaviest Functions:** `SPDX` (Impact: 258.7), `Anonymous_Block` (Impact: 94.8), `licenses_forbid_installation?` (Impact: 45.1)

### 10. `Library/Homebrew/utils/curl.rb` (RUBY) -> Cumulative Risk: **634.71**
- **Archetype:** `file_cluster_8` (Distance: 12.666 IQR)
- **Magnitude:** 1811.68 | **LOC:** 776 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Utils_[Truncated]` (Impact: 1676.3), `__global_context__` (Impact: 1.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `Library/Homebrew/api/homebrew-1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/analytics.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.928 IQR)
- **Top Global Matches:** file_cluster_8: 9.928, file_cluster_13: 10.314, file_cluster_7: 10.351
- **Magnitude:** 2174.6 | **LOC:** 516 | **CtrlFlow:** 67.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (12.8516%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils` (Impact: 2153.2 | O(2^N) | DB: 8)
    * *Intent:* # Helper module for fetching and reporting analytics data. module Analytics INFLUX_BUCKET = "analyti...
  * `__global_context__` (Impact: 1.5 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "context" require "erb" require "settings" require "cachable" ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 72`, `args: 27`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 11`
* *Architecture:* `io: 1`, `api: 1`, `import: 10`
* *Defense:* `safety: 7`, `doc: 26`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` curl, Utils::Output::Mixin, settings, api, OS, cachable, output, Cachable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/curl.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.666 IQR)
- **Top Global Matches:** file_cluster_8: 12.666, file_cluster_11: 12.721, file_cluster_13: 12.803
- **Magnitude:** 1811.68 | **LOC:** 776 | **CtrlFlow:** 78.2% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (32.1937%), Tech Debt (14.5368%)
**Top Internal Functions/Classes:**
  * `Utils_[Truncated]` (Impact: 1676.3 | O(N^6) | DB: 55)
    * *Intent:* # Helper function for interacting with `curl`. module Curl include SystemCommand::Mixin extend Syste...
  * `__global_context__` (Impact: 1.4 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "open3" require "utils/timer" require "system_command" module ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 233`, `structural_boundaries: 65`, `args: 31`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 120`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 3`, `import: 3`
* *Defense:* `safety: 32`, `doc: 37`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.218
  * `Choke Point (Betweenness):` 0.000663 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` Utils::Output::Mixin, open3, T::Helpers, timer, system_command, SystemCommand::Mixin
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/github.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.794 IQR)
- **Top Global Matches:** file_cluster_8: 11.794, file_cluster_17: 12.04, file_cluster_13: 12.057
- **Magnitude:** 1661.08 | **LOC:** 1040 | **CtrlFlow:** 72.5% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(N^6) | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (20.1024%), Tech Debt (8.4703%)
**Top Internal Functions/Classes:**
  * `GitHub_[Truncated]` (Impact: 1560.8 | O(N^6) | DB: 48)
    * *Intent:* # A module that interfaces with GitHub, code like PAT scopes, credential handling and API errors. # ...
  * `__global_context__` (Impact: 1.6 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "uri" require "utils/github/actions" require "utils/github/api...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 94`, `args: 91`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 80`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 2`, `import: 9`
* *Defense:* `safety: 34`, `doc: 29`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.339
  * `Choke Point (Betweenness):` 0.001548 | `Ripple Effect (Closeness):` 0.023704
  * `Imports (Out-Degree: 5):` curl, Utils::Output::Mixin, actions, popen, api, uri, output, system_command...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.044 IQR)
- **Top Global Matches:** file_cluster_0: 13.044, file_cluster_8: 13.113, file_cluster_13: 13.157
- **Magnitude:** 1562.38 | **LOC:** 1329 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (23.4832%), Tech Debt (14.933%)
**Top Internal Functions/Classes:**
  * `fetch_bottle` (Impact: 187.3 | O(N^5) | DB: 1)
  * `start` (Impact: 95.8 | O(N^6) | DB: 8)
  * `resolve_bottle` (Impact: 83.0 | O(N^4) | DB: 1)
  * `download_http_url` (Impact: 82.3 | O(N^5) | DB: 9)
  * `load_formula_json` (Impact: 81.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 235`, `args: 125`, `func_start: 66`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 127`, `orphaned_logic: 9`
* *Architecture:* `io: 9`, `api: 50`, `concurrency: 12`, `import: 28`
* *Defense:* `safety: 170`, `test: 50`, `sync_locks: 18`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` format_progress_message, should_send_github_packages_auth_for_host, std::collections::HashMap, std::sync::Arc, reqwest::header::AUTHORIZATION, ExitCode, HeaderMap, rayon::prelude::*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/pypi.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.406 IQR)
- **Top Global Matches:** file_cluster_8: 11.406, file_cluster_13: 11.641, file_cluster_11: 11.744
- **Magnitude:** 1416.08 | **LOC:** 534 | **CtrlFlow:** 79.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (25.5591%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `PyPI_[Truncated]` (Impact: 1363.2 | O(N^6) | DB: 59)
    * *Intent:* # Helper functions for updating PyPI resources.
  * `__global_context__` (Impact: 1.4 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "utils/inreplace" require "utils/output" require "utils/ast" #...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 49`, `args: 31`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`
* *Architecture:* `io: 13`, `api: 3`, `import: 6`
* *Defense:* `safety: 25`, `doc: 19`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.000221 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` Utils::Output::Mixin, formula, inreplace, output, ast
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/test/utils/curl_spec.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.152 IQR)
- **Top Global Matches:** file_cluster_8: 9.152, file_cluster_7: 9.896, file_cluster_15: 9.9
- **Magnitude:** 1245.64 | **LOC:** 832 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (61.0477%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 1223.5 | O(N^6) | DB: 8)
  * `__global_context__` (Impact: 1.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 47`, `args: 1`
* *Risk/State:* `high_risk_execution: 74`, `state_mutation: 7`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `import: 1`
* *Defense:* `safety: 1`, `test: 215`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` curl, Utils::Curl, a_string_starting_with, Context
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/output.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.345 IQR)
- **Top Global Matches:** file_cluster_8: 10.345, file_cluster_13: 10.536, file_cluster_7: 10.665
- **Magnitude:** 1121.9 | **LOC:** 290 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (19.2633%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils` (Impact: 1105.5 | O(2^N) | DB: 4)
    * *Intent:* # typed: strict # frozen_string_literal: true
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 43`, `args: 22`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `import: 7`
* *Defense:* `safety: 5`, `doc: 23`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 83.563
  * `Choke Point (Betweenness):` 0.001382 | `Ripple Effect (Closeness):` 0.136054
  * `Imports (Out-Degree: 1):` tap, T::Helpers, actions, Mixin, formatter
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/github/api.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.889 IQR)
- **Top Global Matches:** file_cluster_8: 11.889, file_cluster_13: 12.005, file_cluster_16: 12.113
- **Magnitude:** 871.66 | **LOC:** 477 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (12.2506%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GitHub_[Truncated]` (Impact: 829.6 | O(N^6) | DB: 15)
  * `__global_context__` (Impact: 1.3 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "system_command" require "utils/output" module GitHub sig { pa...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 58`, `args: 15`, `func_start: 18`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 31`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `safety: 39`, `doc: 21`, `test: 13`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.63
  * `Choke Point (Betweenness):` 0.001106 | `Ripple Effect (Closeness):` 0.033862
  * `Imports (Out-Degree: 4):` curl, shell, Utils::Output::Mixin, uid, formatter, output, system_command, SystemCommand::Mixin...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/bottles.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.708 IQR)
- **Top Global Matches:** file_cluster_8: 10.708, file_cluster_7: 11.022, file_cluster_13: 11.174
- **Magnitude:** 870.84 | **LOC:** 396 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (15.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils_[Truncated]` (Impact: 841.3 | O(N^6) | DB: 18)
    * *Intent:* # Helper functions for bottles. # # @api internal module Bottles class << self # Gets the tag for th...
  * `__global_context__` (Impact: 1.2 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "tab" module Utils # Helper functions for bottles. # # @api in...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 73`, `args: 26`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 20`
* *Architecture:* `io: 2`, `api: 2`, `import: 2`
* *Defense:* `safety: 12`, `doc: 45`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tab, bottles
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/shfmt.sh` (SHELL | Tier 0 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.269 IQR)
- **Top Global Matches:** file_cluster_11: 16.269, file_cluster_4: 16.272, file_cluster_17: 16.345
- **Magnitude:** 611.52 | **LOC:** 453 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 122
- **Risk Profile:** Cognitive Load (97.3867%), Tech Debt (93.0745%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 430.2 | O(N^2) | DB: 122)
    * *Intent:* # HOMEBREW_PREFIX is set by extend/ENV/super.rb # shellcheck disable=SC2154
  * `Anonymous_Block_[Truncated]` (Impact: 27.6 | O(N^1) | DB: 7)
  * `Anonymous_Block` (Impact: 14.8 | O(N^1) | DB: 6)
  * `Anonymous_Block` (Impact: 6.2 | O(N^1) | DB: 3)
  * `__global_context__` (Impact: 2.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 74`, `args: 25`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 102`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 3`, `orphaned_logic: 2`
* *Architecture:* `io: 38`, `concurrency: 18`
* *Defense:* `safety: 108`, `doc: 4`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/git.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.497 IQR)
- **Top Global Matches:** file_cluster_8: 10.497, file_cluster_7: 10.792, file_cluster_13: 10.848
- **Magnitude:** 463.54 | **LOC:** 203 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (19.1758%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils` (Impact: 446.3 | O(2^N) | DB: 4)
    * *Intent:* # Helper functions for querying Git information. # # @see GitRepository module Git extend SystemComm...
  * `__global_context__` (Impact: 1.2 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "system_command" module Utils # Helper functions for querying ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 31`, `args: 9`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 12`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 5`, `doc: 17`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 0):` system_command, formula, SystemCommand::Mixin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/shared_audits.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.694 IQR)
- **Top Global Matches:** file_cluster_8: 11.694, file_cluster_16: 11.77, file_cluster_13: 11.941
- **Magnitude:** 461.4 | **LOC:** 371 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^3) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (17.797%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `self.bitbucket` (Impact: 123.0 | O(N^3) | DB: 6)
  * `SharedAudits` (Impact: 87.4 | O(N^1) | DB: 14)
    * *Intent:* # Auditing functions for rules common to both casks and formulae.
  * `__global_context__` (Impact: 81.0 | O(N^3))
    * *Intent:* # frozen_string_literal: true require "utils/curl" require "utils/github/api" # Auditing functions f...
  * `Anonymous_Block` (Impact: 41.9 | O(N^2) | DB: 2)
  * `self.gitlab` (Impact: 37.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 71`, `args: 22`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 15`
* *Architecture:* `io: 1`, `api: 10`, `import: 2`
* *Defense:* `safety: 44`, `doc: 22`, `test: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.679
  * `Choke Point (Betweenness):` 0.000276 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` curl, api
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/spdx.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.461 IQR)
- **Top Global Matches:** file_cluster_8: 10.461, file_cluster_16: 10.636, file_cluster_13: 10.825
- **Magnitude:** 449.88 | **LOC:** 272 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (18.3086%), Tech Debt (47.5456%)
**Top Internal Functions/Classes:**
  * `SPDX` (Impact: 258.7 | O(N^6) | DB: 9)
    * *Intent:* # Helper module for updating SPDX license data.
  * `Anonymous_Block` (Impact: 94.8 | O(N^2) | DB: 1)
  * `licenses_forbid_installation?` (Impact: 45.1 | O(N^2))
  * `forbidden_licenses_include?` (Impact: 16.3 | O(N^1))
  * `Anonymous_Block` (Impact: 4.8 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 31`, `args: 21`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 18`, `duplicate_logic: 2`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 8`, `doc: 13`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` curl, github
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/ast.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.875 IQR)
- **Top Global Matches:** file_cluster_8: 9.875, file_cluster_7: 10.233, file_cluster_13: 10.289
- **Magnitude:** 430.0 | **LOC:** 241 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (10.3853%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils_[Truncated]` (Impact: 417.9 | O(N^6) | DB: 19)
    * *Intent:* # Helper functions for editing Ruby files. module AST Node = RuboCop::AST::Node SendNode = RuboCop::...
  * `__global_context__` (Impact: 1.3 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "ast_constants" require "rubocop-ast" module Utils # Helper fu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 31`, `args: 20`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 3`, `import: 2`
* *Defense:* `safety: 4`, `doc: 19`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ast_constants, rubocop-ast, AST, Forwardable
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/rust/brew-rs/src/commands/install.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.072 IQR)
- **Top Global Matches:** file_cluster_8: 11.072, file_cluster_13: 11.35, file_cluster_11: 11.537
- **Magnitude:** 417.76 | **LOC:** 298 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (17.8664%), Tech Debt (24.6642%)
**Top Internal Functions/Classes:**
  * `pour_bottle` (Impact: 141.9 | O(N^5))
  * `basic_install_delegate_reason` (Impact: 108.9 | O(N^4))
  * `run` (Impact: 58.6 | O(N^3) | DB: 2)
  * `cleanup_failed_pour` (Impact: 28.6 | O(N^3))
  * `remove_install_metadata` (Impact: 25.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 49`, `args: 26`, `func_start: 9`
* *Risk/State:* `state_mutation: 6`, `planned_debt: 7`
* *Architecture:* `io: 1`, `api: 1`, `import: 10`
* *Defense:* `safety: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FormulaJson, ExitCode, crate::delegate, std::path::Path, anyhow::Context, crate::commands::fetch::self, anyhow, crate::BrewResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/brew` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_12` (Drift: 14.801 IQR)
- **Top Global Matches:** file_cluster_12: 14.801, file_cluster_11: 14.854, file_cluster_8: 14.914
- **Magnitude:** 406.86 | **LOC:** 333 | **CtrlFlow:** 83.1% | **Authorship Centralization:** 41.7%
- **Algorithmic:** O(N) | **DB Complexity:** 104
- **Risk Profile:** Cognitive Load (92.4345%), Tech Debt (98.3978%)
**Top Internal Functions/Classes:**
  * `symlink_target_directory_[Truncated]` (Impact: 267.6 | O(N^1) | DB: 104)
  * `Anonymous_Block` (Impact: 6.2 | O(N^1) | DB: 3)
    * *Intent:* # Fail fast with concise messages when PWD has issues
  * `Anonymous_Block` (Impact: 6.2 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 6.2 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 6.2 | O(N^1) | DB: 3)
    * *Intent:* # Fail fast with concise message when HOME is unset
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 202`, `structural_boundaries: 41`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 97`, `duplicate_logic: 5`, `orphaned_logic: 2`
* *Architecture:* `io: 32`, `api: 4`
* *Defense:* `safety: 79`, `doc: 3`, `test: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/rust/brew-rs/src/commands/list.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.471 IQR)
- **Top Global Matches:** file_cluster_13: 11.471, file_cluster_8: 11.645, file_cluster_0: 11.723
- **Magnitude:** 366.26 | **LOC:** 217 | **CtrlFlow:** 38.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (23.9636%), Tech Debt (42.2088%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 242.8 | O(2^N) | DB: 2)
  * `current_keg_path` (Impact: 46.0 | O(N^4))
  * `list_formula_paths` (Impact: 18.9 | O(N^2))
  * `list_cask_paths` (Impact: 8.2 | O(N^2))
  * `new_in` (Impact: 6.7 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 58`, `args: 15`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 10`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 1`, `import: 15`
* *Defense:* `safety: 28`, `test: 7`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` list_formula_paths, list_cask_paths, crate::delegate, std::path::Path, std::io, Ordering, crate::BrewResult, PathBuf...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/gems.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.283 IQR)
- **Top Global Matches:** file_cluster_8: 11.283, file_cluster_13: 11.561, file_cluster_17: 11.7
- **Magnitude:** 330.94 | **LOC:** 334 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (38.3024%), Tech Debt (92.8291%)
**Top Internal Functions/Classes:**
  * `self.odie_if_defined` (Impact: 117.4 | O(N^4) | DB: 16)
  * `self.install_bundler_gems!` (Impact: 82.8 | O(N^4) | DB: 12)
  * `Anonymous_Block` (Impact: 31.9 | O(N^3) | DB: 3)
  * `__global_context__` (Impact: 16.2 | O(N^3))
    * *Intent:* # frozen_string_literal: true # Never `require` anything in this file (except English). It needs to ...
  * `self.write_user_gem_groups` (Impact: 14.9 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 31`, `args: 14`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 31`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 13`, `import: 5`
* *Defense:* `safety: 21`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` fileutils, bundler, rubygems, package, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/svn.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.016 IQR)
- **Top Global Matches:** file_cluster_13: 11.016, file_cluster_8: 11.118, file_cluster_7: 11.439
- **Magnitude:** 245.04 | **LOC:** 57 | **CtrlFlow:** 52.9% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (39.3418%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils` (Impact: 232.9 | O(2^N) | DB: 3)
    * *Intent:* # Helper functions for querying SVN information. module Svn class << self include SystemCommand::Mix...
  * `__global_context__` (Impact: 1.3 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "system_command" require "utils/output" module Utils # Helper ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 16`, `args: 1`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 1`, `doc: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 1):` system_command, Utils::Output::Mixin, output, SystemCommand::Mixin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/ruby.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.047 IQR)
- **Top Global Matches:** file_cluster_4: 14.047, file_cluster_12: 14.048, file_cluster_11: 14.223
- **Magnitude:** 233.0 | **LOC:** 205 | **CtrlFlow:** 76.3% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (76.5467%), Tech Debt (70.8291%)
**Top Internal Functions/Classes:**
  * `setup-ruby-path` (Impact: 91.5 | O(N^2) | DB: 37)
    * *Intent:* # HOMEBREW_LINUX is set by brew.sh # shellcheck disable=SC2154
  * `need_vendored_ruby` (Impact: 10.6 | O(N^1))
    * *Intent:* # HOMEBREW_FORCE_VENDOR_RUBY is from the user environment # shellcheck disable=SC2154
  * `can_use_ruby_from_path` (Impact: 10.4 | O(N^1) | DB: 6)
  * `find_ruby` (Impact: 10.1 | O(N^1) | DB: 14)
    * *Intent:* # HOMEBREW_PATH is set by global.rb # shellcheck disable=SC2154
  * `ensure-bundle-dependencies` (Impact: 9.7 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 33`, `args: 2`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 54`, `dead_code: 1`, `orphaned_logic: 4`
* *Architecture:* `io: 18`, `api: 6`, `concurrency: 12`, `import: 1`
* *Defense:* `safety: 37`, `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` helpers.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/fork.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.082 IQR)
- **Top Global Matches:** file_cluster_8: 9.082, file_cluster_13: 9.366, file_cluster_7: 9.663
- **Magnitude:** 220.26 | **LOC:** 127 | **CtrlFlow:** 80.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (19.3095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Utils` (Impact: 212.1 | O(N^6) | DB: 11)
  * `__global_context__` (Impact: 1.3 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "fcntl" require "utils/socket" module Utils sig { params(child...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 8`, `args: 3`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`
* *Architecture:* `io: 2`, `api: 2`, `import: 3`
* *Defense:* `safety: 4`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 0):` socket, fcntl, exception
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/test/utils/ast/formula_ast_spec.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.863 IQR)
- **Top Global Matches:** file_cluster_8: 10.863, file_cluster_15: 11.299, file_cluster_7: 11.515
- **Magnitude:** 214.08 | **LOC:** 509 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (43.8301%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__global_context__` (Impact: 49.0 | O(N^3))
  * `Anonymous_Block` (Impact: 11.8 | O(N^3) | DB: 2)
  * `Anonymous_Block` (Impact: 10.1 | O(N^3) | DB: 3)
  * `Anonymous_Block` (Impact: 9.5 | O(N^3) | DB: 2)
  * `Anonymous_Block` (Impact: 9.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 32`, `class_start: 31`
* *Risk/State:* `high_risk_execution: 18`, `state_mutation: 76`, `duplicate_logic: 10`, `orphaned_logic: 1`
* *Architecture:* `import: 1`
* *Defense:* `test: 92`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/test/utils/git_spec.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.66 IQR)
- **Top Global Matches:** file_cluster_8: 8.66, file_cluster_15: 9.245, file_cluster_7: 9.477
- **Magnitude:** 208.02 | **LOC:** 228 | **CtrlFlow:** 96.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (29.1355%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 199.0 | O(N^6) | DB: 34)
  * `__global_context__` (Impact: 1.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 1`, `args: 1`
* *Risk/State:* `high_risk_execution: 11`, `state_mutation: 4`, `orphaned_logic: 1`
* *Architecture:* `io: 10`, `import: 1`
* *Defense:* `safety: 1`, `test: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` git
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/cpan.rb` (RUBY | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.365 IQR)
- **Top Global Matches:** file_cluster_8: 10.365, file_cluster_13: 10.703, file_cluster_7: 10.805
- **Magnitude:** 205.66 | **LOC:** 198 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (19.3642%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CPAN` (Impact: 179.2 | O(N^3) | DB: 15)
    * *Intent:* # Helper functions for updating CPAN resources.
  * `__global_context__` (Impact: 1.4 | O(N^1))
    * *Intent:* # frozen_string_literal: true require "utils/inreplace" require "utils/output" # Helper functions fo...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 24`, `args: 7`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `io: 2`, `api: 3`, `import: 2`
* *Defense:* `safety: 5`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.67
  * `Choke Point (Betweenness):` 0.000221 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` inreplace, Utils::Output::Mixin, output
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` (RUST) | Magnitude: 1562.38 | Delta: **0.069 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1008, structural_boundaries: 235, branch: 212, safety: 170
- `Library/Homebrew/rust/brew-rs/src/utils/tty.rs` (RUST) | Magnitude: 177.3 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, structural_boundaries: 38, branch: 21, api: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `Library/Homebrew/utils/shfmt.sh` (SHELL) | Magnitude: 611.52 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 271, branch: 237, reflection_metaprogramming: 125, safety: 108
- `package/scripts/preinstall` (SHELL) | Magnitude: 28.5 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 18, structural_boundaries: 9, io: 6, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `Library/Homebrew/utils/zsh/brew-sh-prompt-zshrc.zsh` (SHELL) | Magnitude: 10.76 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 5, structural_boundaries: 4, globals: 4, reflection_metaprogramming: 4
- `bin/brew` (SHELL) | Magnitude: 406.86 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 202, indent_spaces: 125, state_mutation: 97, safety: 79
- `Library/Homebrew/cask/utils/rmdir.sh` (SHELL) | Magnitude: 46.16 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 31, indent_spaces: 25, reflection_metaprogramming: 12, safety: 10
- `Library/Homebrew/utils/bash/brew-sh-prompt-bashrc.bash` (SHELL) | Magnitude: 9.74 | Delta: **0.061 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 5, globals: 4, reflection_metaprogramming: 4, structural_boundaries: 3
- `package/scripts/postinstall` (SHELL) | Magnitude: 82.1 | Delta: **0.224 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 44, branch: 38, reflection_metaprogramming: 31, indent_spaces: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `Library/Homebrew/utils/wrapper.sh` (SHELL) | Magnitude: 150.26 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 47, indent_spaces: 46, reflection_metaprogramming: 21, safety: 17
- `Library/Homebrew/rust/brew-rs/src/lib.rs` (RUST) | Magnitude: 4.86 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, safety: 2, generics: 2, import: 2
- `Library/Homebrew/utils/tar.rb` (RUBY) | Magnitude: 191.0 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 15, branch: 14, func_start: 4
- `Library/Homebrew/utils/svn.rb` (RUBY) | Magnitude: 245.04 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, branch: 18, structural_boundaries: 16, state_mutation: 9
- `Library/Homebrew/rust/brew-rs/src/commands/search.rs` (RUST) | Magnitude: 111.44 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 74, structural_boundaries: 35, branch: 14, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `Library/Homebrew/utils/autoremove.rb` (RUBY) | Magnitude: 75.68 | Delta: **0.185 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 52, branch: 17, args: 10, generics: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `Library/Homebrew/utils/helpers.sh` (SHELL) | Magnitude: 110.34 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 58, branch: 54, io: 31, safety: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `Library/Homebrew/utils/ruby.sh` (SHELL) | Magnitude: 233.0 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 128, branch: 106, reflection_metaprogramming: 61, state_mutation: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `Library/Homebrew/utils/github/actions.rb` (RUBY) | Magnitude: 181.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, state_mutation: 51, branch: 34, structural_boundaries: 21
- `Library/Homebrew/rust/brew-rs/src/app.rs` (RUST) | Magnitude: 25.56 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 8, import: 6, safety: 4
- `Library/Homebrew/utils/string_inreplace_extension.rb` (RUBY) | Magnitude: 63.44 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 24, test: 16, doc: 13
- `Library/Homebrew/cask/utils/trash.swift` (SWIFT) | Magnitude: 33.48 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 11, branch: 7, structural_boundaries: 5
- `Library/Homebrew/utils/curl.rb` (RUBY) | Magnitude: 1811.68 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 544, branch: 233, state_mutation: 120, structural_boundaries: 65

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/brew` -> Churn: **80.71%** | Cog Load: 92.4345% | Debt: 98.3978%
- `Library/Homebrew/utils/wrapper.sh` -> Churn: **65.43%** | Cog Load: 94.1004% | Debt: 95.7035%
- `Library/Homebrew/rust/brew-rs/src/utils/tty.rs` -> Churn: **56.38%** | Cog Load: 15.6859% | Debt: 62.9554%
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> Churn: **50.64%** | Cog Load: 16.0322% | Debt: 99.4472%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Library/Homebrew/utils/shfmt.sh` -> **John E** (100.0% isolated ownership) | Magnitude: 611.52
- `Library/Homebrew/rust/brew-rs/src/commands/install.rs` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 417.76
- `Library/Homebrew/rust/brew-rs/src/commands/list.rs` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 366.26
- `Library/Homebrew/utils/fork.rb` -> **Douglas Eichelberger** (100.0% isolated ownership) | Magnitude: 220.26
- `Library/Homebrew/utils/link.rb` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 199.96

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Library/Homebrew/utils/github.rb` -> **Severity: 0.147** (Bridge: 0.0015 * Flux: 94.9799%)
- `Library/Homebrew/utils/github/api.rb` -> **Severity: 0.071** (Bridge: 0.0011 * Flux: 64.5306%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 0.066** (Bridge: 0.0007 * Flux: 100.0%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 0.065** (Bridge: 0.0014 * Flux: 46.957%)
- `Library/Homebrew/utils/inreplace.rb` -> **Severity: 0.039** (Bridge: 0.0004 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Library/Homebrew/utils/github/actions.rb` -> **Severity: 1.752** (Embedded: 0.0998 * Error Risk: 17.5536%)
- `Library/Homebrew/utils/github/api.rb` -> **Severity: 1.714** (Embedded: 0.0339 * Error Risk: 50.6186%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 1.178** (Embedded: 0.1361 * Error Risk: 8.6551%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 0.832** (Embedded: 0.0667 * Error Risk: 12.4824%)
- `Library/Homebrew/utils/spdx.rb` -> **Severity: 0.368** (Embedded: 0.0074 * Error Risk: 49.6507%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Library/Homebrew/utils/timer.rb` -> **Severity: 3095.4** (Blast Radius: 30.954 * Doc Risk: 100.0%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 1245.122** (Blast Radius: 83.563 * Doc Risk: 14.9004%)
- `Library/Homebrew/rust/brew-rs/src/delegate.rs` -> **Severity: 1205.6** (Blast Radius: 12.056 * Doc Risk: 100.0%)
- `Library/Homebrew/extend/os/mac/utils/socket.rb` -> **Severity: 1205.529** (Blast Radius: 12.056 * Doc Risk: 99.9941%)
- `Library/Homebrew/utils/backtrace.rb` -> **Severity: 1112.7** (Blast Radius: 11.127 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
