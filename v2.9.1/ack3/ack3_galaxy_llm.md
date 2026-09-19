# ARCHITECTURAL_BRIEF: ack3
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/beyondgrep/ack3.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 172 analyzed artifact(s), 10618 LOC.
- **Load-bearing artifact:** `t/Util.pm` -- 67 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ack` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `ack` at magnitude 1276.16 (structural weight, not risk).
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
| Total Artifacts | 297 |
| Analyzed Artifacts (Scanned) | 172 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 125 |
| Total LOC | 10618 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 57.9% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2332 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6273 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.061 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 103 | 9387 | 59.9% |
| YAML | 20 | 947 | 11.6% |
| PLAINTEXT | 15 | 0 | 8.7% |
| MARKDOWN | 12 | 0 | 7.0% |
| HTML | 5 | 142 | 2.9% |
| SHELL | 3 | 15 | 1.7% |
| CSHARP | 3 | 8 | 1.7% |
| RUBY | 2 | 64 | 1.2% |
| C | 2 | 21 | 1.2% |
| FORTRAN | 2 | 22 | 1.2% |
| DOCKERFILE | 1 | 5 | 0.6% |
| MAKEFILE | 1 | 1 | 0.6% |
| CSS | 1 | 1 | 0.6% |
| JAVASCRIPT | 1 | 2 | 0.6% |
| PYTHON | 1 | 3 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `5.612`
> **Composition Archetype:** `Small Flat Repo (2)` (z +5.61; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 40%, Declarative / Non-Code 38%, Parameter Forwarders Files 5%, Large Core Modules (3) 5%, Large Core Modules 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 145 | 84.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 15.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 125*

**Composition by Extension & Reason:**
- `no_extension`: 27x Unsupported Format (.undeterminable), 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 114 LOC)
- `.pm`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.0`: 10x Excluded (Unsupported Extension: '.0')
- `.xxx`: 8x Excluded (Unsupported Extension: '.xxx')
- `.yaml`: 1x Zero-Density Threshold (LOC: 74, Signals: 0), 1x Zero-Density Threshold (LOC: 82, Signals: 0), 1x Zero-Density Threshold (LOC: 98, Signals: 0)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.0 | 19.7 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.7 | 38.8 | 53.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 2.4 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.8 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 118 | 21 | 1 | `t/Util.pm` |
| cleanup | 56 | 10 | 0 | `t/Util.pm` |
| guards | 228 | 104 | 2 | `t/filter.t` |
| danger | 240 | 67 | 3 | `t/Util.pm` |
| concurrency | 20 | 4 | 0 | `t/Util.pm` |
| connectivity | 126 | 29 | 1 | `t/Util.pm` |
| io | 113 | 18 | 1 | `ack` |
| crypto | 0 | 0 | 0 | - |
| ipc | 18 | 6 | 0 | `t/Util.pm` |
| time | 18 | 8 | 0 | `t/highlighting.t` |
| serialization | 2 | 2 | 0 | `t/swamp/crystallography-weenies.f` |
| regex | 209 | 46 | 3 | `ack` |
| events | 4 | 4 | 0 | `ack` |
| tests | 421 | 85 | 7 | `t/ack-color.t` |
| docs | 213 | 34 | 2 | `ack` |
| debt | 182 | 35 | 2 | `ack` |
| mutation | 1379 | 111 | 20 | `ack` |
| dead_code | 29 | 10 | 0 | `t/swamp/Makefile` |
| credential | 0 | 0 | 0 | - |
| threat | 48 | 16 | 0 | `t/highlighting.t` |
| ml_ai | 21 | 6 | 0 | `dev/Cookbook.pm` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ack` (Hits: 55)
- `t/Util.pm` (Hits: 31)
- `t/process-substitution.t` (Hits: 4)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Util.pm** (`t/Util.pm`) — 67 inbound connections
2. **FilterTest.pm** (`t/FilterTest.pm`) — 5 inbound connections
3. **CODE_OF_CONDUCT.md** (`CODE_OF_CONDUCT.md`) — 1 inbound connections
4. **CONTRIBUTING.md** (`CONTRIBUTING.md`) — 1 inbound connections
5. **DESIGN.md** (`DESIGN.md`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ack** (`ack`) — 47 outbound dependencies
2. **Util.pm** (`t/Util.pm`) — 19 outbound dependencies
3. **Cookbook.pm** (`dev/Cookbook.pm`) — 13 outbound dependencies
4. **timings.pl** (`dev/timings.pl`) — 13 outbound dependencies
5. **00-load.t** (`t/00-load.t`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `windows_slashify` **(Many-Argument Workhorses)** (@ `t/Util.pm`) -> Impact: **367.3** | LOC: 411
- `print_line_with_options` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **96.7** | LOC: 122
- `pmif_context` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **68.5** | LOC: 74
- `pmif_normal` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **65.8** | LOC: 63
- `_compile_file_filter` **(Compute Cores)** (@ `ack`) -> Impact: **64.5** | LOC: 113
- `pmif_passthru` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **60.8** | LOC: 53
- `run_cmd` **(Compute Cores)** (@ `t/Util.pm`) -> Impact: **58.6** | LOC: 125
  * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus writes its STDERR to $catcherr_file). # # Sets $a...
- `count_matches_in_file` **(Compute Cores)** (@ `ack`) -> Impact: **53.3** | LOC: 62
- `pmif_opt_v` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **49.3** | LOC: 47
- `file_loop_normal` **(Compute Cores)** (@ `ack`) -> Impact: **30.3** | LOC: 41

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 92 | 3619.56 | 24.19% | 6.15% |
| `__monolith__` | 13 | 1363.88 | 5.37% | 3.63% |
| `dev` | 15 | 559.46 | 23.07% | 2.0% |
| `t/swamp` | 28 | 281.87 | 1.81% | 7.44% |
| `xt` | 4 | 154.04 | 38.61% | 0.0% |
| `t/range` | 5 | 65.38 | 0.0% | 19.05% |
| `t/swamp/blib` | 2 | 28.32 | 0.0% | 0.0% |
| `t/text` | 9 | 26.12 | 0.0% | 0.0% |
| `dev/docker` | 3 | 17.46 | 1.71% | 0.0% |
| `t/swamp/swamp` | 1 | 1.0 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/filetypes.t` -> **99.9996%** Exposure
- `t/range.t` -> **96.9887%** Exposure
- `t/range/rangefile.pm` -> **95.2574%** Exposure
- `t/filter.t` -> **73.1059%** Exposure
- `t/swamp/crystallography-weenies.f` -> **73.1059%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `dev/crank-mutex` -> **100.0%** Exposure
- `t/ack-group.t` -> **100.0%** Exposure
- `t/ack-n.t` -> **100.0%** Exposure
- `t/ack-pager.t` -> **100.0%** Exposure
- `t/ack-passthru.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/range.t` -> **0** Orphaned Functions | **4** Duplicates
- `Makefile.PL` -> **2** Orphaned Functions | **0** Duplicates
- `t/range/rangefile.pm` -> **2** Orphaned Functions | **0** Duplicates
- `t/filter.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/swamp/crystallography-weenies.f` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `633` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ack` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 1276.16 | **LOC:** 2545 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **47**; blast radius 7.535; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (46.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print_line_with_options` **(Many-Argument Workhorses)** (Impact: 96.7)
  * `pmif_context` **(Many-Argument Workhorses)** (Impact: 68.5)
  * `pmif_normal` **(Many-Argument Workhorses)** (Impact: 65.8)
  * `_compile_file_filter` **(Compute Cores)** (Impact: 64.5)
  * `pmif_passthru` **(Many-Argument Workhorses)** (Impact: 60.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 196 instances
* *Memory Alloc (weighted view):* 12
* *State Mutation (weighted view):* 618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 649`, `structural_boundaries: 330`, `args: 28`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 9`, `state_mutation: 226`, `fragile_debt: 3`
* *Architecture:* `io: 55`, `api: 17`, `import: 54`
* *Defense:* `safety: 4`, `doc: 70`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.535
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005618
  * `Imports (Out-Degree: 0):` App::Ack, App::Ack::ConfigLoader, App::Ack::File, App::Ack::Files, App::Ack::Filter, App::Ack::Filter::Collection, App::Ack::Filter::Default, App::Ack::Filter::Extension...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1078.72 | **LOC:** 1380 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **67** in-repo importer(s); it depends on **19**; blast radius 250.741; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Concurrency Surface (formerly Concurrency) (92.7%), Guard Balance (formerly Safety Score) (81.5%)
- **Documentation Coverage:** 94.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `windows_slashify` **(Many-Argument Workhorses)** (Impact: 367.3)
  * `run_cmd` **(Compute Cores)** (Impact: 58.6)
    * *Intent:* # Run the given command, assuming that the command was created with # build_ack_invocation (and thus...
  * `run_piped` **(Many-Argument Workhorses)** (Impact: 22.9)
  * `build_ack_invocation` **(Compute Cores)** (Impact: 19.1)
  * `make_unreadable` **(Compute Cores)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 67 instances
* *Concurrency (weighted view):* 58
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 369`, `args: 67`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 7`, `state_mutation: 71`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 31`, `api: 51`, `concurrency: 13`, `import: 21`
* *Defense:* `safety: 3`, `doc: 3`, `test: 18`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 250.741
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.378229
  * `Imports (Out-Degree: 0):` Carp, Cwd, File::Next, File::Spec, File::Temp, IO::Pty, List::Util, Scalar::Util...
  * `Imported By (In-Degree: 67):` (Excluded from Brief to save tokens)

### `dev/timings.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 201.02 | **LOC:** 408 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `time_ack` **(Many-Argument Workhorses)** (Impact: 23.1)
  * `grab_versions` **(Compute Cores)** (Impact: 17.4)
  * `color` **(I/O & Config Routines)** (Impact: 9.1)
  * `create_format` **(Compute Cores)** (Impact: 6.6)
  * `counts_valid` **(Compute Cores)** (Impact: 5.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *Concurrency (weighted view):* 12
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 101`, `args: 5`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 39`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 6`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Next, File::Spec, Getopt::Long, JSON, List::Util, Term::ANSIColor, Time::HiRes, Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/Cookbook.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 140.04 | **LOC:** 589 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.2%), Complexity Load (formerly Cognitive Load) (42.5%), Debt Markers (formerly Tech Debt) (19.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 48`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 46`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 1`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` C, LWP::Simple, a, ack, args, changes, guarantee, longer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 134.5 | **LOC:** 450 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.1%), Complexity Load (formerly Cognitive Load) (76.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 34 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 113
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 115`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 45`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Term::ANSIColor, Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-pager.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 117.92 | **LOC:** 248 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.1%), Complexity Load (formerly Cognitive Load) (86.7%), Debt Markers (formerly Tech Debt) (13.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 92`, `structural_boundaries: 38`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 33`, `planned_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-type.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 107.22 | **LOC:** 154 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.7%), Complexity Load (formerly Cognitive Load) (84.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 46`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, lines, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/man.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 91.38 | **LOC:** 132 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.6%), Complexity Load (formerly Cognitive Load) (79.1%), Connectivity (formerly Api Exposure) (5.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_populate_man_options` **(I/O & Config Routines)** (Impact: 29.6)
  * `strip_special_chars` **(Compute Cores)** (Impact: 7.5)
  * `check_for_option_in_man_output` **(Compute Cores)** (Impact: 5.1)
  * `get_man_options` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 35`, `args: 2`, `func_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 16`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Data::Dumper, Test::More, Util, critic, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-underline.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 84.24 | **LOC:** 156 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.8%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 34`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 23`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, law, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-passthru.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 71.58 | **LOC:** 188 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.5%), Complexity Load (formerly Cognitive Load) (73.2%), Connectivity (formerly Api Exposure) (2.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `color_match` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 48`, `args: 2`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 26`
* *Architecture:* `io: 1`, `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/interactive.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 68.1 | **LOC:** 138 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.5%), Complexity Load (formerly Cognitive Load) (79.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 30`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 19`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Term::ANSIColor, Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/config-loader.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 65.44 | **LOC:** 298 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (78.7%), Complexity Load (formerly Cognitive Load) (21.1%), Connectivity (formerly Api Exposure) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_loader` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 65`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 24`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 2`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App::Ack::ConfigLoader, App::Ack::Filter::Default, Test::More, Util, argument, lib, strict, targets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-group.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 64.72 | **LOC:** 110 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.0%), Complexity Load (formerly Cognitive Load) (84.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 23`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 16`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, break, heading, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 61.58 | **LOC:** 185 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (78.4%), Complexity Load (formerly Cognitive Load) (63.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 58`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 16`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/range.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 55.0 | **LOC:** 281 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (97.0%), Guard Balance (formerly Safety Score) (76.3%), Complexity Load (formerly Cognitive Load) (48.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foo` **(Interface Declarations)** (Impact: 1.1)
  * `bar` **(Interface Declarations)** (Impact: 1.1)
  * `foo` **(Interface Declarations)** (Impact: 1.1)
  * `bar` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 68`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 27`, `duplicate_logic: 4`
* *Architecture:* `api: 4`, `import: 13`
* *Defense:* `safety: 4`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, end, lib, range, start, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 54.08 | **LOC:** 177 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.073; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Guard Balance (formerly Safety Score) (69.6%), Debt Markers (formerly Tech Debt) (37.2%), Complexity Load (formerly Cognitive Load) (22.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MY::postamble` **(I/O & Config Routines)** (Impact: 27.2)
  * `MY::test` **(Interface Declarations)** (Impact: 1.1)
    * *Intent:* # Suppress EU::MM test rule.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 13`, `func_start: 2`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExtUtils::MakeMaker, need, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/invalid-ackrc.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 53.2 | **LOC:** 88 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (91.1%), Complexity Load (formerly Cognitive Load) (69.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 22`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 13`
* *Architecture:* `import: 8`
* *Defense:* `safety: 2`, `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Temp, List::Util, Test::More, Util, lib, output, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/highlighting.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 49.4 | **LOC:** 221 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (84.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_check_it` **(Parameter Forwarders)** (Impact: 4.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 37`, `args: 2`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 14`
* *Architecture:* `import: 6`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, law, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/boolean.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 46.88 | **LOC:** 255 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Guard Balance (formerly Safety Score) (74.5%), Debt Markers (formerly Tech Debt) (51.8%), Complexity Load (formerly Cognitive Load) (17.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_movies_are` **(Compute Cores)** (Impact: 7.6)
  * `_argjoin` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 25`, `args: 4`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 27`, `fragile_debt: 3`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/linecount-fork` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 42.74 | **LOC:** 46 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 4.073; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Complexity Load (formerly Cognitive Load) (97.0%), Guard Balance (formerly Safety Score) (83.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 15`, `args: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`
* *Architecture:* `io: 3`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` File::Next, IO::Handle, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/mutex-options.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 42.5 | **LOC:** 225 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.3%), Guard Balance (formerly Safety Score) (58.2%), Debt Markers (formerly Tech Debt) (22.3%), Complexity Load (formerly Cognitive Load) (15.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `are_mutually_exclusive` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* # Do this without system().
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 34`, `args: 3`, `func_start: 1`
* *Risk/State:* `state_mutation: 8`, `fragile_debt: 1`
* *Architecture:* `api: 1`, `import: 5`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 40.68 | **LOC:** 121 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Complexity Load (formerly Cognitive Load) (78.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 8`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-x.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 40.52 | **LOC:** 107 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Complexity Load (formerly Cognitive Load) (82.1%), Dead Code Surface (formerly Dead Code) (10.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 30`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 8`, `dead_code: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, black, lib, living, strict, warning, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/crank-mutex` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 39.62 | **LOC:** 68 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 4.073; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.2%), Complexity Load (formerly Cognitive Load) (58.8%), Connectivity (formerly Api Exposure) (3.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_combinations` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 35
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 20`, `func_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 25`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Data::Dumper, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-n.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 37.86 | **LOC:** 60 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.073; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.6%), Guard Balance (formerly Safety Score) (92.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 9`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 18`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.073
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `t/FilterTest.pm` -> **Severity: 0.008** (Bridge: 0.0002 * Flux: 50.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/Util.pm` -> **Severity: 30.836** (Embedded: 0.3782 * Error Risk: 81.5273%)
- `t/FilterTest.pm` -> **Severity: 1.344** (Embedded: 0.0281 * Error Risk: 47.8585%)
- `ack` -> **Severity: 0.509** (Embedded: 0.0056 * Error Risk: 90.5323%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/Util.pm` -> **Severity: 23641.291** (Blast Radius: 250.741 * Doc Risk: 94.2857%)
- `t/FilterTest.pm` -> **Severity: 2138.3** (Blast Radius: 21.383 * Doc Risk: 100.0%)
- `t/ack-help.t` -> **Severity: 407.3** (Blast Radius: 4.073 * Doc Risk: 100.0%)
- `t/ack-ignore-dir.t` -> **Severity: 407.3** (Blast Radius: 4.073 * Doc Risk: 100.0%)
- `t/ack-match.t` -> **Severity: 407.3** (Blast Radius: 4.073 * Doc Risk: 100.0%)

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
