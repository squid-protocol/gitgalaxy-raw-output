# ARCHITECTURAL_BRIEF: brew
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Homebrew/brew` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 136 analyzed artifact(s), 13947 LOC.
- **Load-bearing artifact:** `Library/Homebrew/utils/output.rb` -- 14 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` -- pulls in 55 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `Library/Homebrew/api/homebrew-1.pem` at magnitude 5000.0 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2828 |
| Analyzed Artifacts (Scanned) | 136 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2692 |
| Total LOC | 13947 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 4.8% |
| Dominant Lang | RUBY |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6879 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.1873 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8036 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 21 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUBY | 89 | 10325 | 65.4% |
| RUST | 19 | 2330 | 14.0% |
| SHELL | 12 | 1086 | 8.8% |
| MARKDOWN | 7 | 0 | 5.1% |
| PLAINTEXT | 4 | 1 | 2.9% |
| SWIFT | 3 | 127 | 2.2% |
| DOCKERFILE | 1 | 78 | 0.7% |
| XML | 1 | 0 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `2.863`
> **Composition Archetype:** `Small Flat Repo (2)` (z +2.86; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Data / Markup / Trivial 21%, Large Core Modules (3) 18%, Large Core Modules (2) 10%, Compute Cores Files 5%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 125 | 91.9% |
| Unknown | 1 | 0.7% |

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 94.9 | 21.0 | 13.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 50.8 | 63.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 71.7 | 11.7 | 3.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 96.6 | 2.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 57.3 | 86.1 | 100.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 22.9 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.6 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 75.6 | 14.7 | 6.5 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 28.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 184 | 30 | 2 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| cleanup | 22 | 9 | 0 | `bin/brew` |
| guards | 620 | 61 | 11 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| danger | 575 | 71 | 11 | `Library/Homebrew/test/utils/curl_spec.rb` |
| concurrency | 40 | 9 | 0 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| connectivity | 323 | 68 | 6 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| io | 342 | 53 | 7 | `Library/Homebrew/utils/shfmt.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `Library/Homebrew/utils/helpers.sh` |
| time | 18 | 9 | 0 | `Library/Homebrew/utils/shared_audits.rb` |
| serialization | 26 | 9 | 0 | `Library/Homebrew/utils/shared_audits.rb` |
| regex | 110 | 29 | 3 | `Library/Homebrew/utils/shfmt.sh` |
| events | 12 | 6 | 0 | `Library/Homebrew/utils/shfmt.sh` |
| tests | 1715 | 69 | 42 | `Library/Homebrew/test/utils/curl_spec.rb` |
| docs | 466 | 50 | 13 | `Library/Homebrew/utils/bottles.rb` |
| debt | 191 | 46 | 5 | `Library/Homebrew/test/utils/pypi_spec.rb` |
| mutation | 2968 | 92 | 64 | `Library/Homebrew/utils/github.rb` |
| dead_code | 106 | 32 | 3 | `Library/Homebrew/rust/brew-rs/src/homebrew.rs` |
| credential | 3 | 3 | 0 | `Library/Homebrew/utils/ruby.sh` |
| threat | 27 | 15 | 1 | `bin/brew` |
| ml_ai | 12 | 4 | 0 | `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` |
| ui | 16 | 2 | 0 | `Library/Homebrew/utils/helpers.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `Library/Homebrew/utils/shfmt.sh` (Hits: 39)
- `Library/Homebrew/utils/helpers.sh` (Hits: 34)
- `bin/brew` (Hits: 32)

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

- `update_python_resources!` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/pypi.rb`) -> Impact: **259.8** | LOC: 292
- `curl_check_http_content` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/curl.rb`) -> Impact: **147.6** | LOC: 131
- `Anonymous_Block` **(Unclassified)** (@ `Library/Homebrew/test/utils/curl_spec.rb`) -> Impact: **130.4** | LOC: 827
- `update_perl_resources!` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/cpan.rb`) -> Impact: **61.5** | LOC: 104
- `fetch_bottle` **(Many-Argument Workhorses)** (@ `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs`) -> Impact: **59.5** | LOC: 71
- `create_bump_pr` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/github.rb`) -> Impact: **59.3** | LOC: 112
  * *Intent:* # --write-only without --commit means don't take any git actions at all. return if args.write_only? && !args.commit? tap = info[:tap] remote = info[:r...
- `Anonymous_Block` **(Defensive Guards)** (@ `Library/Homebrew/test/utils/backtrace_spec.rb`) -> Impact: **58.0** | LOC: 86
- `odeprecated` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/output.rb`) -> Impact: **56.8** | LOC: 78
- `install_bundler_gems!` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/gems.rb`) -> Impact: **54.4** | LOC: 128
- `table_output` **(Many-Argument Workhorses)** (@ `Library/Homebrew/utils/analytics.rb`) -> Impact: **45.9** | LOC: 86

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Unclassified**: no dominant structural signature (too small or ambiguous)

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `Library/Homebrew/utils` | 49 | 6226.86 | 30.57% | 12.53% |
| `Library/Homebrew/api` | 1 | 5000.0 | 0.0% | 0.0% |
| `Library/Homebrew/test/utils` | 30 | 1014.78 | 15.5% | 0.0% |
| `Library/Homebrew/rust/brew-rs/src/commands` | 10 | 978.96 | 6.78% | 38.04% |
| `Library/Homebrew/utils/github` | 3 | 415.94 | 27.59% | 33.33% |
| `bin` | 1 | 217.86 | 70.27% | 0.0% |
| `Library/Homebrew/rust/brew-rs/src` | 6 | 136.16 | 5.53% | 67.88% |
| `Library/Homebrew/rust/brew-rs/src/utils` | 3 | 109.78 | 10.36% | 60.45% |
| `Library/Homebrew/test/utils/bottles` | 3 | 76.48 | 33.47% | 0.0% |
| `package/scripts` | 2 | 71.3 | 43.56% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `Library/Homebrew/utils/helpers.sh` -> **99.9975%** Exposure
- `Library/Homebrew/utils/github/artifacts.rb` -> **99.9925%** Exposure
- `Library/Homebrew/utils/link.rb` -> **99.6272%** Exposure
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> **99.4472%** Exposure
- `Library/Homebrew/rust/brew-rs/src/matcher.rs` -> **97.4762%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `Library/Homebrew/cask/utils/trash.swift` -> **100.0%** Exposure
- `Library/Homebrew/cask/utils/rmdir.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/analytics.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/ruby.sh` -> **100.0%** Exposure
- `Library/Homebrew/utils/shfmt.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> **14** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/utils/helpers.sh` -> **10** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` -> **9** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/rust/brew-rs/src/utils/tty.rs` -> **7** Orphaned Functions | **0** Duplicates
- `Library/Homebrew/utils/link.rb` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `345` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `Library/Homebrew/api/homebrew-1.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/github.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 862.98 | **LOC:** 1040 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 16.119; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.5%)
- **Documentation Coverage:** 48.6842% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_bump_pr` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* # --write-only without --commit means don't take any git actions at all. return if args.write_only? ...
  * `check_for_duplicate_pull_requests` **(Many-Argument Workhorses)** (Impact: 34.9)
  * `fetch_pull_requests` **(Many-Argument Workhorses)** (Impact: 23.0)
  * `repo_commits_for_user` **(Many-Argument Workhorses)** (Impact: 20.8)
  * `organisation_repositories` **(Many-Argument Workhorses)** (Impact: 19.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 109 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 389
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 98`, `args: 39`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 5`, `state_mutation: 171`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 6`, `api: 28`, `import: 9`
* *Defense:* `safety: 34`, `doc: 29`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.119
  * `Choke Point (Betweenness):` 0.001548 | `Ripple Effect (Closeness):` 0.023704
  * `Imports (Out-Degree: 5):` SystemCommand::Mixin, Utils::Output::Mixin, system_command, uri, curl, actions, api, output...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/curl.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 728.06 | **LOC:** 776 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **6**; blast radius 25.866; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `curl_check_http_content` **(Many-Argument Workhorses)** (Impact: 147.6)
  * `curl_http_content_headers_and_checksum` **(Many-Argument Workhorses)** (Impact: 43.9)
  * `curl_with_workarounds` **(Many-Argument Workhorses)** (Impact: 35.6)
  * `curl_headers` **(Defensive Guards)** (Impact: 30.2)
  * `curl_download` **(Defensive Guards)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 119 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 364
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 71`, `args: 15`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 6`, `state_mutation: 126`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 6`, `import: 4`
* *Defense:* `safety: 32`, `doc: 37`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.866
  * `Choke Point (Betweenness):` 0.000663 | `Ripple Effect (Closeness):` 0.066667
  * `Imports (Out-Degree: 1):` SystemCommand::Mixin, T::Helpers, Utils::Output::Mixin, open3, system_command, timer
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `Library/Homebrew/rust/brew-rs/src/commands/fetch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 667.62 | **LOC:** 1329 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.9%), Mutation Surface (formerly State Flux) (49.7%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fetch_bottle` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `load_formula_json` **(Stateful Encapsulated Methods)** (Impact: 35.3)
  * `resolve_bottle` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `download_http_url` **(Many-Argument Workhorses)** (Impact: 26.1)
  * `download_formula_json` **(Compute Cores)** (Impact: 24.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 235`, `args: 132`, `func_start: 66`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 31`, `unreferenced_by_name: 9`
* *Architecture:* `io: 9`, `api: 50`, `concurrency: 2`, `import: 28`
* *Defense:* `safety: 27`, `test: 50`, `sync_locks: 18`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExitCode, File, HashSet, HeaderMap, HeaderValue, Instant, IsTerminal, Mutex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/pypi.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 597.88 | **LOC:** 534 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 8.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (54.8%)
- **Documentation Coverage:** 13.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_python_resources!` **(Many-Argument Workhorses)** (Impact: 259.8)
  * `pypi_info` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `basic_metadata` **(I/O & Config Routines)** (Impact: 17.7)
  * `resource_blocks_from_formula` **(Compute Cores)** (Impact: 16.5)
  * `update_pypi_url` **(Defensive Guards)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 69 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 50`, `args: 10`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 81`
* *Architecture:* `io: 16`, `api: 5`, `import: 6`
* *Defense:* `safety: 25`, `doc: 19`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.554
  * `Choke Point (Betweenness):` 0.000221 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` Utils::Output::Mixin, formula, ast, inreplace, output
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/analytics.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 381.42 | **LOC:** 516 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.624; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (42.0%)
- **Documentation Coverage:** 2.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `table_output` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `output_analytics` **(Compute Cores)** (Impact: 18.5)
  * `output_github_packages_downloads` **(Compute Cores)** (Impact: 17.4)
  * `report_command_run` **(Compute Cores)** (Impact: 12.7)
  * `report_package_event` **(Many-Argument Workhorses)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 77`, `args: 15`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 82`
* *Architecture:* `io: 1`, `api: 9`, `import: 10`
* *Defense:* `safety: 7`, `doc: 26`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Cachable, Context, OS, Utils::Output::Mixin, api, cachable, context, erb...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/shared_audits.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 379.9 | **LOC:** 371 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 6.589; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.1%), Connectivity (formerly Api Exposure) (46.1%), Complexity Load (formerly Cognitive Load) (41.3%)
- **Documentation Coverage:** 18.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bitbucket` **(Defensive Guards)** (Impact: 31.9)
  * `github` **(Defensive Guards)** (Impact: 19.2)
  * `forgejo` **(Defensive Guards)** (Impact: 19.2)
  * `gitlab` **(Defensive Guards)** (Impact: 17.1)
  * `gitlab_release` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 77`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 7`, `state_mutation: 53`
* *Architecture:* `io: 1`, `api: 10`, `import: 2`
* *Defense:* `safety: 54`, `doc: 22`, `test: 14`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.589
  * `Choke Point (Betweenness):` 0.000276 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` curl, api
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/shfmt.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 322.12 | **LOC:** 453 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.7%), Concurrency Surface (formerly Concurrency) (88.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `wrap_then_do` **(Compute Cores)** (Impact: 31.9)
    * *Intent:* # Wrap `then` and `do` to a separated line # before: after: # if [[ ... ]]; then if [[ ... ]] # then...
  * `format` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* # Return codes: # 0: success, good styles # 1: file system permission errors # 2: shfmt failed # 3: ...
  * `no_forbidden_pattern` **(Many-Argument Workhorses)** (Impact: 17.1)
    * *Intent:* ### ### Custom shell script styling ### # Check for specific patterns and prompt messages if detecte...
  * `align_multiline_if_condition` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* # Align multiline if condition (indent with 3 spaces or 6 spaces (start with "-")) # before: after: ...
  * `no_multiline_for_statements` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* # Check pattern: # for var in ... \ # ...; do # # Use the following instead (keep for statements onl...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 133
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 234`, `args: 27`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 45`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `io: 39`, `concurrency: 3`
* *Defense:* `safety: 5`, `doc: 4`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/github/api.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 281.46 | **LOC:** 477 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 11.474; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.9%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_rest` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `raise_error` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `credentials_error_message` **(Compute Cores)** (Impact: 15.1)
  * `open_graphql` **(Many-Argument Workhorses)** (Impact: 9.5)
  * `paginate_rest` **(Many-Argument Workhorses)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 65`, `args: 4`, `func_start: 18`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 52`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 39`, `doc: 21`, `test: 12`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.474
  * `Choke Point (Betweenness):` 0.001106 | `Ripple Effect (Closeness):` 0.033862
  * `Imports (Out-Degree: 4):` SystemCommand::Mixin, Utils::Output::Mixin, system_command, tempfile, curl, formatter, output, shell...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/bottles.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 260.46 | **LOC:** 396 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (43.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_formula_names` **(Defensive Guards)** (Impact: 15.1)
  * `load_tab` **(Defensive Guards)** (Impact: 13.9)
  * `tag` **(Defensive Guards)** (Impact: 9.1)
  * `add` **(Compute Cores)** (Impact: 8.2)
  * `from_symbol` **(Defensive Guards)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 75`, `args: 21`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 20`, `state_mutation: 41`
* *Architecture:* `io: 2`, `api: 13`, `import: 2`
* *Defense:* `safety: 13`, `doc: 45`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bottles, tab
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/output.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 231.0 | **LOC:** 290 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **5**; blast radius 82.439; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `odeprecated` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `odebug` **(Compute Cores)** (Impact: 12.6)
  * `oh1_title` **(Compute Cores)** (Impact: 10.9)
  * `ohai_title` **(Compute Cores)** (Impact: 7.6)
  * `pretty_duration` **(Compute Cores)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 43`, `args: 13`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 27`
* *Architecture:* `api: 13`, `import: 7`
* *Defense:* `safety: 5`, `doc: 23`, `test: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 82.439
  * `Choke Point (Betweenness):` 0.001382 | `Ripple Effect (Closeness):` 0.136054
  * `Imports (Out-Degree: 1):` Mixin, T::Helpers, tap, formatter, actions
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/gems.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 224.04 | **LOC:** 334 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.9%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install_bundler_gems!` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `install_gem!` **(Many-Argument Workhorses)** (Impact: 15.3)
  * `setup_gem_environment!` **(Compute Cores)** (Impact: 10.2)
  * `write_user_gem_groups` **(Defensive Guards)** (Impact: 6.7)
  * `odie_if_defined` **(Compute Cores)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 33`, `args: 5`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 43`, `unreferenced_by_name: 3`
* *Architecture:* `io: 14`, `import: 5`
* *Defense:* `safety: 21`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` bundler, fileutils, rubygems, package, tempfile
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/brew` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 217.86 | **LOC:** 333 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.6%), Complexity Load (formerly Cognitive Load) (70.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `export_homebrew_env_file` **(Compute Cores)** (Impact: 9.6)
    * *Intent:* # Load Homebrew's variable configuration files from disk.
  * `symlink_target_directory` **(Compute Cores)** (Impact: 9.4)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 9.1)
    * *Intent:* # don't filter the environment for `brew bundle (exec|env|sh)`
  * `__global_context__` **(I/O & Config Routines)** (Impact: 6.3)
  * `Anonymous_Block` **(Defensive Guards)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 180`, `args: 10`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 36`
* *Architecture:* `io: 32`, `api: 4`
* *Defense:* `safety: 20`, `doc: 3`, `test: 5`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/spdx.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 208.18 | **LOC:** 272 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 8.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Complexity Load (formerly Cognitive Load) (39.2%), Connectivity (formerly Api Exposure) (32.7%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `license_expression_to_string` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `string_to_license_expression` **(Compute Cores)** (Impact: 18.8)
  * `licenses_forbid_installation?` **(Compute Cores)** (Impact: 18.2)
  * `forbidden_licenses_include?` **(Compute Cores)** (Impact: 11.1)
  * `parse_license_expression` **(Generic / Templated Code)** (Impact: 9.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 32`, `args: 9`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 34`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 8`, `doc: 13`, `test: 6`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.554
  * `Choke Point (Betweenness):` 0.000498 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` curl, github
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/test/utils/curl_spec.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 205.56 | **LOC:** 832 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.624; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (97.7%), Mutation Surface (formerly State Flux) (84.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.1%), Complexity Load (formerly Cognitive Load) (13.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 130.4)
  * `__global_context__` **(Unclassified)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 74
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 60`, `args: 1`
* *Risk/State:* `high_risk_execution: 79`, `state_mutation: 54`, `planned_debt: 1`
* *Architecture:* `io: 2`, `import: 1`
* *Defense:* `safety: 1`, `test: 207`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Context, Utils::Curl, a_string_starting_with, curl
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/ast.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 186.4 | **LOC:** 241 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (40.2%)
- **Documentation Coverage:** 5.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_stanza` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `stanza_text` **(Compute Cores)** (Impact: 16.4)
  * `call_node_match?` **(Compute Cores)** (Impact: 10.6)
  * `remove_stanza` **(Compute Cores)** (Impact: 10.2)
  * `formula_component_before_target?` **(Callbacks & Closures)** (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 31`, `args: 7`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 31`, `dead_code: 1`
* *Architecture:* `io: 5`, `api: 6`, `import: 2`
* *Defense:* `safety: 4`, `doc: 19`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AST, Forwardable, ast_constants, rubocop-ast
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/cpan.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 156.86 | **LOC:** 198 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.1%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_perl_resources!` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `install` **(I/O & Config Routines)** (Impact: 6.9)
  * `latest_cpan_info` **(I/O & Config Routines)** (Impact: 6.1)
  * `extract_version_from_url` **(Encapsulated Accessors)** (Impact: 2.4)
  * `initialize` **(Defensive Guards)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 25`, `args: 1`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `io: 5`, `api: 4`, `import: 2`
* *Defense:* `safety: 5`, `doc: 8`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.554
  * `Choke Point (Betweenness):` 0.000221 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 2):` Utils::Output::Mixin, inreplace, output
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/formatter.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 145.0 | **LOC:** 220 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.6%)
- **Documentation Coverage:** 3.2258% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `columns` **(Many-Argument Workhorses)** (Impact: 19.4)
  * `format_help_text` **(Compute Cores)** (Impact: 9.1)
  * `prefix` **(Many-Argument Workhorses)** (Impact: 4.5)
  * `number_readable` **(I/O & Config Routines)** (Impact: 4.5)
  * `truncate` **(Compute Cores)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 22`, `args: 5`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 26`
* *Architecture:* `api: 13`, `import: 1`
* *Defense:* `safety: 9`, `doc: 27`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` tty
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/rust/brew-rs/src/commands/install.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 139.76 | **LOC:** 298 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (46.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.1%), Debt Markers (formerly Tech Debt) (24.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pour_bottle` **(Compute Cores)** (Impact: 36.4)
  * `basic_install_delegate_reason` **(Compute Cores)** (Impact: 33.6)
  * `run` **(Compute Cores)** (Impact: 22.4)
  * `cleanup_failed_pour` **(Defensive Guards)** (Impact: 14.7)
  * `display_bottle_basename` **(Defensive Guards)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *High Risk Execution (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 49`, `args: 32`, `func_start: 9`
* *Risk/State:* `high_risk_execution: 2`, `planned_debt: 7`
* *Architecture:* `io: 1`, `api: 1`, `import: 10`
* *Defense:* `safety: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BottleFetch, ExitCode, FormulaJson, PathBuf, Resolution, ResolvedBottle, Stdio, UNIX_EPOCH...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/git.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 131.64 | **LOC:** 203 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.554; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (49.3%)
- **Documentation Coverage:** 8.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_name_email!` **(Defensive Guards)** (Impact: 14.9)
  * `last_revision_commit_of_files` **(Many-Argument Workhorses)** (Impact: 7.0)
  * `last_revision_commit_of_file` **(Compute Cores)** (Impact: 6.5)
  * `version` **(Defensive Guards)** (Impact: 5.3)
  * `ensure_installed!` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 33`, `args: 1`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 5`, `doc: 17`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.554
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 0):` SystemCommand::Mixin, formula, system_command
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/ruby.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 124.9 | **LOC:** 205 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 6.589; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (96.6%), Guard Balance (formerly Safety Score) (89.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup-ruby-path` **(I/O & Config Routines)** (Impact: 24.5)
    * *Intent:* # HOMEBREW_LINUX is set by brew.sh # shellcheck disable=SC2154
  * `need_vendored_ruby` **(Interface Declarations)** (Impact: 5.5)
    * *Intent:* # HOMEBREW_FORCE_VENDOR_RUBY is from the user environment # shellcheck disable=SC2154
  * `can_use_ruby_from_path` **(Interface Declarations)** (Impact: 4.4)
  * `find_ruby` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* # HOMEBREW_PATH is set by global.rb # shellcheck disable=SC2154
  * `ensure-bundle-dependencies` **(I/O & Config Routines)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 101`, `args: 2`, `func_start: 9`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 23`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 18`, `api: 6`, `concurrency: 2`, `import: 1`
* *Defense:* `doc: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.589
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007407
  * `Imports (Out-Degree: 1):` helpers.sh
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/shell.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 119.06 | **LOC:** 187 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 10.992; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (45.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_variable_in_profile` **(Compute Cores)** (Impact: 9.4)
  * `profile` **(I/O & Config Routines)** (Impact: 9.0)
  * `export_value` **(Many-Argument Workhorses)** (Impact: 8.8)
  * `prepend_path_in_profile` **(Compute Cores)** (Impact: 6.4)
  * `shell_with_prompt` **(Many-Argument Workhorses)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 22`, `args: 1`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`
* *Architecture:* `io: 11`, `api: 6`
* *Defense:* `safety: 5`, `doc: 11`, `test: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.992
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.030864
  * `Imports (Out-Degree: 0):` T::Helpers
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `Library/Homebrew/utils/github/actions.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 111.68 | **LOC:** 136 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 81.367; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.9%), Connectivity (formerly Api Exposure) (41.8%), Complexity Load (formerly Cognitive Load) (38.1%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialize` **(Defensive Guards)** (Impact: 18.7)
  * `to_s` **(I/O & Config Routines)** (Impact: 8.2)
  * `format_multiline_string` **(Compute Cores)** (Impact: 6.0)
    * *Intent:* # Format multiline strings for environment files # See https://docs.github.com/en/actions/using-work...
  * `puts_annotation_if_env_set!` **(Defensive Guards)** (Impact: 5.0)
    * *Intent:* # Don't print annotations during tests, too messy to handle these. return false if ENV.fetch("HOMEBR...
  * `relevant?` **(I/O & Config Routines)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 21`, `args: 5`, `func_start: 8`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 21`
* *Architecture:* `io: 1`, `api: 4`, `import: 2`
* *Defense:* `safety: 11`, `doc: 9`, `test: 7`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 81.367
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.099805
  * `Imports (Out-Degree: 0):` securerandom, tty
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `Library/Homebrew/rust/brew-rs/src/commands/list.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 99.66 | **LOC:** 217 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 4.624; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.1%), Debt Markers (formerly Tech Debt) (55.8%), Mutation Surface (formerly State Flux) (42.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 31.1)
  * `current_keg_path` **(Compute Cores)** (Impact: 19.1)
  * `list_formula_paths` **(Defensive Guards)** (Impact: 12.8)
  * `list_cask_paths` **(Generic / Templated Code)** (Impact: 5.6)
  * `list_paths` **(Generic / Templated Code)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 58`, `args: 14`, `func_start: 12`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 4`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `api: 1`, `import: 15`
* *Defense:* `safety: 2`, `test: 7`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Ordering, PathBuf, UNIX_EPOCH, crate::BrewResult, crate::delegate, crate::homebrew, current_keg_path, list_cask_paths...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Library/Homebrew/utils/inreplace.rb` (RUBY | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 83.76 | **LOC:** 112 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 15.824; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.6%), Complexity Load (formerly Cognitive Load) (36.5%), Connectivity (formerly Api Exposure) (29.7%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inreplace` **(Many-Argument Workhorses)** (Impact: 28.0)
  * `inreplace_pairs` **(Many-Argument Workhorses)** (Impact: 7.5)
  * `initialize` **(Callbacks & Closures)** (Impact: 1.7)
  * `__global_context__` **(I/O & Config Routines)** (Impact: 1.2)
    * *Intent:* # frozen_string_literal: true require "utils/string_inreplace_extension" module Utils # Helper funct...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 9`, `args: 3`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 16`
* *Architecture:* `io: 2`, `api: 2`, `import: 1`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.824
  * `Choke Point (Betweenness):` 0.000387 | `Ripple Effect (Closeness):` 0.026455
  * `Imports (Out-Degree: 1):` string_inreplace_extension
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `bin/brew` -> Churn: **75.63%** | Cog Load: 70.2694% | Debt: 0.0%
- `Library/Homebrew/rust/brew-rs/src/utils/tty.rs` -> Churn: **58.85%** | Cog Load: 10.2474% | Debt: 85.0995%
- `Library/Homebrew/utils/wrapper.sh` -> Churn: **52.86%** | Cog Load: 55.8305% | Debt: 62.6502%
- `Library/Homebrew/rust/brew-rs/src/homebrew.rs` -> Churn: **52.86%** | Cog Load: 10.3844% | Debt: 99.4472%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `Library/Homebrew/utils/analytics.rb` -> **Douglas Eichelberger** (100.0% isolated ownership) | Magnitude: 381.42
- `Library/Homebrew/utils/shfmt.sh` -> **John E** (100.0% isolated ownership) | Magnitude: 322.12
- `Library/Homebrew/utils/spdx.rb` -> **Rylan Polster** (100.0% isolated ownership) | Magnitude: 208.18
- `Library/Homebrew/test/utils/curl_spec.rb` -> **Sam Ford** (100.0% isolated ownership) | Magnitude: 205.56
- `Library/Homebrew/rust/brew-rs/src/commands/install.rs` -> **Mike McQuaid** (100.0% isolated ownership) | Magnitude: 139.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `Library/Homebrew/utils/github.rb` -> **Severity: 0.155** (Bridge: 0.0015 * Flux: 100.0%)
- `Library/Homebrew/utils/output.rb` -> **Severity: 0.138** (Bridge: 0.0014 * Flux: 100.0%)
- `Library/Homebrew/utils/github/api.rb` -> **Severity: 0.111** (Bridge: 0.0011 * Flux: 100.0%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 0.066** (Bridge: 0.0007 * Flux: 100.0%)
- `Library/Homebrew/utils/spdx.rb` -> **Severity: 0.05** (Bridge: 0.0005 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `Library/Homebrew/utils/output.rb` -> **Severity: 12.377** (Embedded: 0.1361 * Error Risk: 90.9702%)
- `Library/Homebrew/utils/github/actions.rb` -> **Severity: 8.47** (Embedded: 0.0998 * Error Risk: 84.8691%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 6.517** (Embedded: 0.0667 * Error Risk: 97.7564%)
- `Library/Homebrew/utils/timer.rb` -> **Severity: 3.087** (Embedded: 0.0484 * Error Risk: 63.7774%)
- `Library/Homebrew/utils/github/api.rb` -> **Severity: 2.81** (Embedded: 0.0339 * Error Risk: 82.9953%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `Library/Homebrew/utils/github/actions.rb` -> **Severity: 2712.231** (Blast Radius: 81.367 * Doc Risk: 33.3333%)
- `Library/Homebrew/utils/curl.rb` -> **Severity: 1293.3** (Blast Radius: 25.866 * Doc Risk: 50.0%)
- `Library/Homebrew/rust/brew-rs/src/delegate.rs` -> **Severity: 1189.4** (Blast Radius: 11.894 * Doc Risk: 100.0%)
- `Library/Homebrew/utils/popen.rb` -> **Severity: 1129.4** (Blast Radius: 11.294 * Doc Risk: 100.0%)
- `Library/Homebrew/utils/helpers.sh` -> **Severity: 1015.75** (Blast Radius: 12.189 * Doc Risk: 83.3333%)

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
