# ARCHITECTURAL_BRIEF: Rex
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/RexOps/Rex.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 469 analyzed artifact(s), 42567 LOC.
- **Load-bearing artifact:** `lib/Rex/Logger.pm` -- 130 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/Rex.pm` -- pulls in 36 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Rex/Config.pm` at magnitude 877.92 (structural weight, not risk).
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
| Total Artifacts | 515 |
| Analyzed Artifacts (Scanned) | 469 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 46 |
| Total LOC | 42567 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 91.1% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4554 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1915 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.0451 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 46 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 437 | 41866 | 93.2% |
| YAML | 11 | 459 | 2.3% |
| PLAINTEXT | 10 | 0 | 2.1% |
| MARKDOWN | 3 | 0 | 0.6% |
| SHELL | 3 | 218 | 0.6% |
| ELIXIR | 2 | 13 | 0.4% |
| XML | 2 | 0 | 0.4% |
| JAVASCRIPT | 1 | 11 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 469 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Compute Cores Files 20%, Declarative / Non-Code 18%, Large Core Modules (3) 17%, Type Conversions Files 14%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 456 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 13 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 46*

**Composition by Extension & Reason:**
- `no_extension`: 11x Unsupported Format (.undeterminable), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2047 LOC)
- `.out1`: 3x Excluded (Unsupported Extension: '.out1')
- `.out2`: 3x Excluded (Unsupported Extension: '.out2')
- `.ini`: 2x Excluded (Unsupported Extension: '.ini')
- `.out3`: 2x Excluded (Unsupported Extension: '.out3')
- `.rex`: 2x Excluded (Unsupported Extension: '.rex')
- `.stderr`: 2x Excluded (Unsupported Extension: '.stderr')
- `.stdout`: 2x Excluded (Unsupported Extension: '.stdout')
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.ppd`: 1x Excluded (Unsupported Extension: '.ppd')
- `.args`: 1x Excluded (Unsupported Extension: '.args')
- `.tpl`: 1x Excluded (Unsupported Extension: '.tpl')
- `.t`: 1x Excluded (Machine-Generated Source Code Signature: 62 LOC)
- `.ex2`: 1x Excluded (Unsupported Extension: '.ex2')
- `.out4`: 1x Excluded (Unsupported Extension: '.out4')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 98.6 | 27.6 | 15.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.7 | 39.1 | 50.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.6 | 26.6 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.2 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 99.0 | 7.2 | 5.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 55.3 | 69.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 82.9 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 986 | 266 | 5 | `lib/Rex/Config.pm` |
| cleanup | 135 | 67 | 1 | `lib/Rex/Commands/File.pm` |
| guards | 1061 | 436 | 3 | `lib/Rex/Commands/File.pm` |
| danger | 941 | 212 | 5 | `bin/rexify` |
| concurrency | 88 | 35 | 0 | `lib/Rex/CLI.pm` |
| connectivity | 1969 | 357 | 9 | `lib/Rex/Config.pm` |
| io | 556 | 116 | 2 | `misc/create_pod.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 106 | 37 | 0 | `bin/rexify` |
| time | 80 | 32 | 0 | `lib/Rex/Output/JUnit.pm` |
| serialization | 4 | 4 | 0 | `bin/rexify` |
| regex | 1470 | 176 | 9 | `t/file.t` |
| events | 41 | 21 | 0 | `lib/Rex/Interface/Connection/OpenSSH.pm` |
| tests | 1199 | 101 | 5 | `t/cron.t` |
| docs | 521 | 78 | 2 | `lib/Rex/Config.pm` |
| debt | 567 | 107 | 3 | `bin/rexify` |
| mutation | 6914 | 381 | 42 | `lib/Rex/Commands/File.pm` |
| dead_code | 823 | 276 | 5 | `lib/Rex/Interface/Fs/Base.pm` |
| credential | 56 | 4 | 0 | `lib/Rex.pm` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 76 | 21 | 0 | `lib/Rex/Resource/firewall/Provider/ufw.pm` |
| ui | 480 | 22 | 0 | `lib/Rex/Virtualization/LibVirt/create.pm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `misc/create_pod.sh` (Hits: 195)
- `share/rex-tab-completion.zsh` (Hits: 30)
- `share/rex-tab-completion.bash` (Hits: 24)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Logger.pm** (`lib/Rex/Logger.pm`) — 130 inbound connections
2. **Run.pm** (`lib/Rex/Helper/Run.pm`) — 120 inbound connections
3. **Config.pm** (`lib/Rex/Config.pm`) — 82 inbound connections
4. **Commands.pm** (`lib/Rex/Commands.pm`) — 77 inbound connections
5. **Exporter.pm** (`lib/Rex/Exporter.pm`) — 58 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Rex.pm** (`lib/Rex.pm`) — 36 outbound dependencies
2. **CLI.pm** (`lib/Rex/CLI.pm`) — 27 outbound dependencies
3. **rexify** (`bin/rexify`) — 25 outbound dependencies
4. **File.pm** (`lib/Rex/Commands/File.pm`) — 24 outbound dependencies
5. **Task.pm** (`lib/Rex/Task.pm`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `import` **(Many-Argument Workhorses)** (@ `lib/Rex.pm`) -> Impact: **188.6** | LOC: 411
- `sync` **(Many-Argument Workhorses)** (@ `lib/Rex/Commands/Rsync.pm`) -> Impact: **184.3** | LOC: 270
- `run` **(Many-Argument Workhorses)** (@ `lib/Rex/Commands/Run.pm`) -> Impact: **172.3** | LOC: 181
  * *Intent:* # so that it is possible to get for example the output of an apt-get update # that is called through >> install "foo" <<
- `augeas` **(Many-Argument Workhorses)** (@ `lib/Rex/Commands/Augeas.pm`) -> Impact: **164.6** | LOC: 313
- `__run__` **(Many-Argument Workhorses)** (@ `lib/Rex/CLI.pm`) -> Impact: **163.6** | LOC: 327
- `file` **(Many-Argument Workhorses)** (@ `lib/Rex/Commands/File.pm`) -> Impact: **161.8** | LOC: 361
- `install` **(Many-Argument Workhorses)** (@ `lib/Rex/Commands/Pkg.pm`) -> Impact: **125.5** | LOC: 207
- `_parse` **(Many-Argument Workhorses)** (@ `lib/Rex/Template/NG.pm`) -> Impact: **124.5** | LOC: 170
- `create_user` **(Many-Argument Workhorses)** (@ `lib/Rex/User/Linux.pm`) -> Impact: **121.9** | LOC: 198
- `is_installed` **(Many-Argument Workhorses)** (@ `lib/Rex/Pkg/Gentoo.pm`) -> Impact: **105.2** | LOC: 105

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Rex/Commands` | 34 | 5231.56 | 28.81% | 1.0% |
| `lib/Rex` | 34 | 4358.4 | 39.27% | 46.35% |
| `t` | 81 | 1864.8 | 16.64% | 0.74% |
| `lib/Rex/Pkg` | 16 | 1298.32 | 45.04% | 74.5% |
| `lib/Rex/User` | 7 | 1219.58 | 50.47% | 52.5% |
| `lib/Rex/Virtualization/LibVirt` | 18 | 934.8 | 27.11% | 35.58% |
| `lib/Rex/Hardware/Network` | 6 | 906.56 | 41.51% | 47.46% |
| `lib/Rex/Helper` | 13 | 893.1 | 47.84% | 26.97% |
| `lib/Rex/Interface/Fs` | 6 | 876.5 | 29.95% | 64.95% |
| `lib/Rex/Cloud` | 4 | 720.76 | 28.96% | 69.89% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/Rex/Cloud/Base.pm` -> **100.0%** Exposure
- `lib/Rex/Interface/Connection/Base.pm` -> **100.0%** Exposure
- `lib/Rex/Interface/Connection/Fake.pm` -> **100.0%** Exposure
- `lib/Rex/Helper/File/Stat.pm` -> **99.9999%** Exposure
- `lib/Rex/Helper/File/Stat/Unix.pm` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/Rex/Commands/Augeas.pm` -> **100.0%** Exposure
- `lib/Rex/Fork/Manager.pm` -> **100.0%** Exposure
- `lib/Rex/Hardware/Network/Linux.pm` -> **100.0%** Exposure
- `lib/Rex/Hardware/Network/Solaris.pm` -> **100.0%** Exposure
- `lib/Rex/Hardware/VirtInfo.pm` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Rex/Interface/Fs/Base.pm` -> **21** Orphaned Functions | **0** Duplicates
- `lib/Rex/Cloud/Base.pm` -> **20** Orphaned Functions | **0** Duplicates
- `lib/Rex/Interface/Connection/Base.pm` -> **20** Orphaned Functions | **0** Duplicates
- `lib/Rex/Interface/Fs/HTTP.pm` -> **19** Orphaned Functions | **0** Duplicates
- `lib/Rex/Group/Entry/Server.pm` -> **18** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `lib/Rex.pm` -> **100.0%** Exposure
- `lib/Rex/Commands/User.pm` -> **99.9906%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2848` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Rex/Config.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.513)
- **Top Global Matches:** file_cluster_15: 5.513, file_cluster_11: 6.513, file_cluster_16: 8.023
- **Magnitude:** 877.92 | **LOC:** 1940 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **82** in-repo importer(s); it depends on **9**; blast radius 104.293; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.1%), Complexity Load (formerly Cognitive Load) (19.6%)
- **Documentation Coverage:** 56.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_template_function` **(Many-Argument Workhorses)** (Impact: 45.1)
  * `_parse_ssh_config` **(Compute Cores)** (Impact: 25.9)
  * `set` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `_register_set_handlers` **(Compute Cores)** (Impact: 15.6)
  * `get_tmp_dir` **(I/O & Config Routines)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 61 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 557`, `args: 141`, `func_start: 132`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 112`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `io: 22`, `api: 128`, `import: 30`
* *Defense:* `safety: 8`, `doc: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 104.293
  * `Choke Point (Betweenness):` 0.025555 | `Ripple Effect (Closeness):` 0.400992
  * `Imports (Out-Degree: 7):` Data::Dumper, Rex::Helper::File::Spec, Rex::Logger, Rex::Require, Rex::Template, Symbol, YAML, v5...
  * `Imported By (In-Degree: 82):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.679)
- **Top Global Matches:** file_cluster_4: 6.679, file_cluster_15: 8.79, file_cluster_11: 9.677
- **Magnitude:** 852.7 | **LOC:** 1970 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **17**; blast radius 25.239; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.5%), Complexity Load (formerly Cognitive Load) (36.4%)
- **Documentation Coverage:** 23.2558% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `task` **(Many-Argument Workhorses)** (Impact: 60.9)
  * `needs` **(Compute Cores)** (Impact: 43.4)
  * `evaluate_hostname` **(Compute Cores)** (Impact: 43.3)
    * *Intent:* ######### private functions
  * `auth` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `case` **(Compute Cores)** (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 308`, `structural_boundaries: 365`, `args: 42`, `func_start: 69`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 87`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 63`, `import: 32`
* *Defense:* `safety: 4`, `doc: 51`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 25.239
  * `Choke Point (Betweenness):` 0.033812 | `Ripple Effect (Closeness):` 0.328714
  * `Imports (Out-Degree: 12):` Carp, Rex, Rex::Config, Rex::Exporter, Rex::Helper::Misc, Rex::Logger, Rex::Profiler, Rex::Report...
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands/File.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.284)
- **Top Global Matches:** file_cluster_6: 7.284, file_cluster_8: 12.088, file_cluster_4: 14.059
- **Magnitude:** 749.96 | **LOC:** 1412 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **24**; blast radius 11.873; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.4%), Complexity Load (formerly Cognitive Load) (55.5%)
- **Documentation Coverage:** 7.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `file` **(Many-Argument Workhorses)** (Impact: 161.8)
  * `template` **(Many-Argument Workhorses)** (Impact: 59.1)
  * `extract` **(Compute Cores)** (Impact: 43.3)
  * `delete_lines_matching` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `_append_or_update` **(Many-Argument Workhorses)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 216`, `args: 16`, `func_start: 15`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 107`
* *Architecture:* `io: 14`, `api: 16`, `import: 34`
* *Defense:* `safety: 13`, `doc: 14`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.873
  * `Choke Point (Betweenness):` 0.012017 | `Ripple Effect (Closeness):` 0.265462
  * `Imports (Out-Degree: 14):` Carp, Data::Dumper, Fcntl, File::Basename, Rex::CMDB, Rex::Commands::MD5, Rex::Commands::Upload, Rex::Config...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `lib/Rex.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_4: 7.67, file_cluster_15: 7.809, file_cluster_11: 8.777
- **Magnitude:** 558.48 | **LOC:** 1170 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **36**; blast radius 57.954; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (80.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 74.4681% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import` **(Many-Argument Workhorses)** (Impact: 188.6)
  * `search_module_path` **(Compute Cores)** (Impact: 26.6)
  * `deprecated` **(Compute Cores)** (Impact: 11.1)
  * `connect` **(I/O & Config Routines)** (Impact: 9.8)
  * `add_libstruct_to_inc` **(Compute Cores)** (Impact: 8.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 68 instances
* *Amplified Leaks:* 1 instances
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 173`, `args: 10`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 73`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 24`, `concurrency: 1`, `import: 51`
* *Defense:* `safety: 3`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.954
  * `Choke Point (Betweenness):` 0.077657 | `Ripple Effect (Closeness):` 0.300857
  * `Imports (Out-Degree: 31):` Cwd, Data::Dumper, File::Basename, File::Spec, Rex::CMDB, Rex::Commands, Rex::Commands::Cron, Rex::Commands::Download...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `lib/Rex/Task.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.216)
- **Top Global Matches:** file_cluster_15: 6.216, file_cluster_4: 7.091, file_cluster_16: 8.36
- **Magnitude:** 529.04 | **LOC:** 1090 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **21**; blast radius 1.551; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (30.5%)
- **Documentation Coverage:** 3.9604% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 57.1)
  * `connect` **(Many-Argument Workhorses)** (Impact: 47.5)
  * `server` **(Compute Cores)** (Impact: 20.9)
  * `run_hook` **(Many-Argument Workhorses)** (Impact: 18.9)
  * `get_connection_type` **(Compute Cores)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 49 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 245`, `args: 54`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 65`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 13`, `api: 50`, `import: 25`
* *Defense:* `safety: 10`, `doc: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.551
  * `Choke Point (Betweenness):` 0.002507 | `Ripple Effect (Closeness):` 0.144706
  * `Imports (Out-Degree: 15):` Carp, Data::Dumper, Rex::Args, Rex::Commands, Rex::Group::Entry::Server, Rex::Hardware, Rex::Helper::Path, Rex::Helper::Run...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands/Fs.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.285)
- **Top Global Matches:** file_cluster_4: 6.285, file_cluster_15: 8.736, file_cluster_11: 9.914
- **Magnitude:** 524.26 | **LOC:** 1211 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **16**; blast radius 11.983; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.7%), Complexity Load (formerly Cognitive Load) (37.9%)
- **Documentation Coverage:** 3.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mount` **(Many-Argument Workhorses)** (Impact: 90.0)
  * `mkdir` **(Compute Cores)** (Impact: 47.4)
  * `rename` **(Compute Cores)** (Impact: 28.1)
  * `umount` **(Compute Cores)** (Impact: 21.2)
  * `cp` **(Compute Cores)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 227`, `args: 24`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 12`, `state_mutation: 66`
* *Architecture:* `io: 6`, `api: 32`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 3`, `doc: 30`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.983
  * `Choke Point (Betweenness):` 0.008318 | `Ripple Effect (Closeness):` 0.268948
  * `Imports (Out-Degree: 11):` Data::Dumper, Fcntl, File::Basename, Rex::Commands, Rex::Commands::MD5, Rex::Exporter, Rex::Helper::File::Spec, Rex::Helper::Path...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `lib/Rex/CLI.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.748)
- **Top Global Matches:** file_cluster_6: 6.748, file_cluster_4: 10.024, file_cluster_8: 16.179
- **Magnitude:** 472.42 | **LOC:** 850 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **27**; blast radius 2.145; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `__run__` **(Many-Argument Workhorses)** (Impact: 163.6)
  * `load_rexfile` **(Compute Cores)** (Impact: 34.3)
  * `exit_rex` **(Compute Cores)** (Impact: 24.1)
  * `__help__` **(I/O & Config Routines)** (Impact: 21.7)
  * `summarize` **(Compute Cores)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 11
* *State Mutation (weighted view):* 119
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 179`, `args: 12`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 16`, `state_mutation: 41`, `unreferenced_by_name: 4`
* *Architecture:* `io: 6`, `api: 8`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 7`, `sync_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.145
  * `Choke Point (Betweenness):` 0.001545 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 8):` Cwd, Data::Dumper, English, File::Basename, FindBin, List::Util, Rex, Rex::Args...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `bin/rexify` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.421)
- **Top Global Matches:** file_cluster_6: 7.421, file_cluster_8: 12.33, file_cluster_4: 13.959
- **Magnitude:** 418.0 | **LOC:** 1402 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%), Complexity Load (formerly Cognitive Load) (35.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_deps` **(Compute Cores)** (Impact: 54.3)
  * `download_recipe` **(Compute Cores)** (Impact: 28.4)
  * `install_perl_module` **(Compute Cores)** (Impact: 20.7)
  * `get` **(Compute Cores)** (Impact: 19.6)
  * `print_found` **(Compute Cores)** (Impact: 16.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 72 instances
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 228`, `structural_boundaries: 181`, `args: 13`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 52`, `state_mutation: 74`, `dead_code: 1`, `fragile_debt: 1`
* *Architecture:* `io: 11`, `api: 10`, `import: 33`
* *Defense:* `safety: 5`, `doc: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Carp, Cwd, Data::Dumper, File::Basename, File::Spec, HTTP::Request, HTTP::Request::Common, JSON::MaybeXS...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Rex/Template/NG.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.812)
- **Top Global Matches:** file_cluster_8: 6.812, file_cluster_6: 17.132, file_cluster_3: 20.193
- **Magnitude:** 416.6 | **LOC:** 407 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 13.453; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.9%), Guard Balance (formerly Safety Score) (78.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse` **(Many-Argument Workhorses)** (Impact: 124.5)
  * `parse` **(Many-Argument Workhorses)** (Impact: 73.1)
  * `_replace_var` **(Compute Cores)** (Impact: 5.7)
  * `__out` **(Compute Cores)** (Impact: 5.4)
  * `new` **(Type Conversions)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 64 instances
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 72`, `args: 8`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 67`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.453
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.263293
  * `Imports (Out-Degree: 0):` v5, warnings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Rex/User/Linux.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.492)
- **Top Global Matches:** file_cluster_4: 6.492, file_cluster_9: 10.278, file_cluster_15: 10.871
- **Magnitude:** 406.86 | **LOC:** 514 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **16**; blast radius 0.838; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.0%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_user` **(Many-Argument Workhorses)** (Impact: 121.9)
  * `create_group` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `user_groups` **(Compute Cores)** (Impact: 15.7)
  * `rm_user` **(Compute Cores)** (Impact: 15.2)
  * `unlock_password` **(Compute Cores)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 112`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 44`, `unreferenced_by_name: 8`
* *Architecture:* `io: 6`, `api: 14`, `import: 16`
* *Defense:* `safety: 4`, `sync_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.838
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.008903
  * `Imports (Out-Degree: 12):` JSON::MaybeXS, Rex::Commands, Rex::Commands::Fs, Rex::Commands::MD5, Rex::Helper::Encode, Rex::Helper::Path, Rex::Helper::Run, Rex::Interface::Exec...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands/Pkg.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.668)
- **Top Global Matches:** file_cluster_6: 6.668, file_cluster_8: 11.991, file_cluster_4: 13.447
- **Magnitude:** 379.32 | **LOC:** 808 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 2.206; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (31.1%)
- **Documentation Coverage:** 10.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `install` **(Many-Argument Workhorses)** (Impact: 125.5)
  * `pkg` **(Compute Cores)** (Impact: 49.4)
  * `repository` **(Many-Argument Workhorses)** (Impact: 32.0)
  * `remove` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `update` **(Compute Cores)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 104
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 219`, `args: 13`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `io: 8`, `api: 13`, `import: 30`
* *Defense:* `safety: 10`, `doc: 10`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.206
  * `Choke Point (Betweenness):` 0.002623 | `Ripple Effect (Closeness):` 0.21542
  * `Imports (Out-Degree: 13):` Data::Dumper, Rex::Commands, Rex::Commands::File, Rex::Commands::Fs, Rex::Commands::Gather, Rex::Commands::MD5, Rex::Commands::Upload, Rex::Config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/Hardware/Network/Linux.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 10.52)
- **Top Global Matches:** file_cluster_3: 10.52, file_cluster_8: 15.76, file_cluster_6: 28.241
- **Magnitude:** 365.6 | **LOC:** 422 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 1.665; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `netstat` **(I/O & Config Routines)** (Impact: 43.2)
  * `_parse_ip` **(Compute Cores)** (Impact: 42.4)
  * `_parse_ifconfig` **(Compute Cores)** (Impact: 33.5)
  * `default_gateway` **(Compute Cores)** (Impact: 29.2)
  * `get_network_configuration` **(I/O & Config Routines)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 58 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 92`, `args: 4`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 59`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 6`, `import: 7`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.665
  * `Choke Point (Betweenness):` 0.001217 | `Ripple Effect (Closeness):` 0.00641
  * `Imports (Out-Degree: 4):` Data::Dumper, Rex::Commands::Run, Rex::Helper::Array, Rex::Helper::Run, Rex::Logger, v5, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/Rex/Virtualization/LibVirt/create.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 23.718)
- **Top Global Matches:** file_cluster_3: 23.718, file_cluster_1: 25.367, file_cluster_8: 45.299
- **Magnitude:** 355.52 | **LOC:** 622 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.748; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (57.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_set_defaults` **(Many-Argument Workhorses)** (Impact: 65.1)
  * `execute` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `_set_storage_defaults` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `_set_network_defaults` **(Compute Cores)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 57`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 1`, `import: 15`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.748
  * `Choke Point (Betweenness):` 0.000186 | `Ripple Effect (Closeness):` 0.002137
  * `Imports (Out-Degree: 12):` Data::Dumper, Rex::Commands::File, Rex::Commands::Fs, Rex::Commands::Gather, Rex::Commands::Run, Rex::File::Parser::Data, Rex::Hardware, Rex::Helper::Path...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/Resource/firewall/Provider/ufw.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.963)
- **Top Global Matches:** file_cluster_8: 6.963, file_cluster_6: 11.803, file_cluster_4: 20.163
- **Magnitude:** 342.22 | **LOC:** 303 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_ufw_rule` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `_generate_rule_array` **(Compute Cores)** (Impact: 31.8)
  * `_ufw_logging` **(Compute Cores)** (Impact: 31.1)
  * `_ufw_disable_enable` **(Compute Cores)** (Impact: 18.4)
  * `_ufw_exec` **(Compute Cores)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 148
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 82`, `args: 14`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 50`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Data::Dumper, Rex::Commands::Run, Rex::Helper::Run, base, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Rex/Commands/Augeas.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.302)
- **Top Global Matches:** file_cluster_3: 6.302, file_cluster_8: 20.905, file_cluster_6: 33.858
- **Magnitude:** 341.46 | **LOC:** 425 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.5%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `augeas` **(Many-Argument Workhorses)** (Impact: 164.6)
  * `_run_augtool` **(Compute Cores)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 109`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`
* *Architecture:* `io: 1`, `api: 4`, `import: 13`
* *Defense:* `safety: 2`, `doc: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.879
  * `Choke Point (Betweenness):` 0.000187 | `Ripple Effect (Closeness):` 0.002137
  * `Imports (Out-Degree: 10):` Exporter, Module::Load::Conditional, Rex::Commands, Rex::Commands::File, Rex::Commands::Fs, Rex::Commands::Run, Rex::Helper::Path, Rex::Helper::Run...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/TaskList/Base.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_4: 6.997, file_cluster_15: 8.019, file_cluster_16: 9.667
- **Magnitude:** 326.46 | **LOC:** 444 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.691; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Debt Markers (formerly Tech Debt) (82.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_task` **(Many-Argument Workhorses)** (Impact: 104.9)
  * `modify` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `build_child_coderef` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `get_thread_count` **(Compute Cores)** (Impact: 14.7)
  * `run` **(Many-Argument Workhorses)** (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 130`, `args: 24`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 24`, `unreferenced_by_name: 14`
* *Architecture:* `api: 20`, `concurrency: 6`, `import: 13`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.691
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.002137
  * `Imports (Out-Degree: 8):` Data::Dumper, POSIX, Rex::Config, Rex::Fork::Manager, Rex::Group, Rex::Interface::Executor, Rex::Logger, Rex::Report...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands/Iptables.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.934)
- **Top Global Matches:** file_cluster_4: 5.934, file_cluster_15: 9.721, file_cluster_9: 9.857
- **Magnitude:** 321.92 | **LOC:** 656 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.879; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%), Complexity Load (formerly Cognitive Load) (33.4%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_open_or_close_port` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `iptables` **(Compute Cores)** (Impact: 24.6)
  * `_iptables_list` **(Compute Cores)** (Impact: 23.0)
  * `redirect_port` **(Compute Cores)** (Impact: 20.1)
  * `_rule_exists` **(Compute Cores)** (Impact: 17.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 151`, `args: 14`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 37`, `dead_code: 1`
* *Architecture:* `api: 12`, `import: 14`
* *Defense:* `safety: 2`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.879
  * `Choke Point (Betweenness):` 0.00018 | `Ripple Effect (Closeness):` 0.002137
  * `Imports (Out-Degree: 7):` Data::Dumper, Rex::Commands::Fs, Rex::Commands::Gather, Rex::Commands::Run, Rex::Commands::Sysctl, Rex::Exporter, Rex::Helper::Run, Rex::Logger...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/Commands/Rsync.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.554)
- **Top Global Matches:** file_cluster_1: 5.554, file_cluster_3: 48.226, file_cluster_8: 70.064
- **Magnitude:** 290.3 | **LOC:** 382 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.791; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.1%), Complexity Load (formerly Cognitive Load) (55.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sync` **(Many-Argument Workhorses)** (Impact: 184.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 66`, `args: 7`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`
* *Architecture:* `api: 4`, `import: 16`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.002137
  * `Imports (Out-Degree: 10):` Net::OpenSSH::ShellQuoter, Rex::Commands, Rex::Commands::Sync, Rex::Exporter, Rex::Helper::IP, Rex::Helper::Path, Rex::Helper::Run, Rex::Interface::Shell...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Rex/Cloud/Amazon.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.099)
- **Top Global Matches:** file_cluster_15: 7.099, file_cluster_4: 7.185, file_cluster_12: 8.972
- **Magnitude:** 278.96 | **LOC:** 541 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (60.0%), Guard Balance (formerly Safety Score) (56.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_instance` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `_request` **(Defensive Guards)** (Impact: 19.8)
  * `_sign` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `_make_instance_map` **(Compute Cores)** (Impact: 17.7)
  * `list_instances` **(Type Conversions)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 142`, `args: 23`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `dead_code: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 2`, `api: 20`, `import: 15`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AWS::Signature4, Carp, Data::Dumper, Digest::HMAC_SHA1, HTTP::Request::Common, LWP::UserAgent, Rex::Cloud::Base, Rex::Logger...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Rex/Commands/Sync.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.645)
- **Top Global Matches:** file_cluster_6: 7.645, file_cluster_8: 12.071, file_cluster_4: 14.474
- **Magnitude:** 272.86 | **LOC:** 414 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 2.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.5%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sync_up` **(Many-Argument Workhorses)** (Impact: 89.1)
  * `sync_down` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `_get_local_files` **(Compute Cores)** (Impact: 18.7)
  * `_get_remote_files` **(Compute Cores)** (Impact: 18.6)
  * `_diff_files` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 98
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 82`, `args: 7`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 34`, `dead_code: 6`
* *Architecture:* `api: 5`, `import: 19`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.273
  * `Choke Point (Betweenness):` 0.002027 | `Ripple Effect (Closeness):` 0.215944
  * `Imports (Out-Degree: 8):` Data::Dumper, File::Basename, JSON::MaybeXS, Rex::Commands, Rex::Commands::Download, Rex::Commands::File, Rex::Commands::Fs, Rex::Commands::MD5...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Rex/Hardware/Network/Solaris.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 12.271)
- **Top Global Matches:** file_cluster_8: 12.271, file_cluster_3: 14.166, file_cluster_6: 24.229
- **Magnitude:** 268.94 | **LOC:** 322 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.8%), Guard Balance (formerly Safety Score) (73.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `netstat` **(I/O & Config Routines)** (Impact: 54.8)
  * `default_gateway` **(Compute Cores)** (Impact: 29.2)
  * `get_network_configuration` **(Compute Cores)** (Impact: 15.2)
  * `route` **(I/O & Config Routines)** (Impact: 12.1)
  * `get_network_devices` **(Interface Declarations)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 60`, `args: 1`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Rex::Helper::Array, Rex::Helper::Run, Rex::Logger, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Rex/Commands/Run.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.589)
- **Top Global Matches:** file_cluster_8: 6.589, file_cluster_6: 17.376, file_cluster_3: 19.761
- **Magnitude:** 260.1 | **LOC:** 497 | **CtrlFlow:** 35.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **37** in-repo importer(s); it depends on **17**; blast radius 10.764; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (41.2%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 172.3)
    * *Intent:* # so that it is possible to get for example the output of an apt-get update # that is called through...
  * `sudo` **(Compute Cores)** (Impact: 13.2)
  * `can_run` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 20 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 73`, `args: 7`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 4`, `state_mutation: 20`
* *Architecture:* `io: 7`, `api: 6`, `import: 22`
* *Defense:* `safety: 4`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.764
  * `Choke Point (Betweenness):` 0.010017 | `Ripple Effect (Closeness):` 0.261808
  * `Imports (Out-Degree: 9):` Data::Dumper, English, Expect, Net::OpenSSH::ShellQuoter, Rex, Rex::Config, Rex::Exporter, Rex::Helper::Run...
  * `Imported By (In-Degree: 37):` (Excluded from Brief to save tokens)

### `lib/Rex/Group/Entry/Server.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 4.932)
- **Top Global Matches:** file_cluster_15: 4.932, file_cluster_16: 7.7, file_cluster_11: 7.979
- **Magnitude:** 257.02 | **LOC:** 387 | **CtrlFlow:** 22.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **13**; blast radius 1.749; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (97.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_auth_type` **(Defensive Guards)** (Impact: 21.4)
  * `new` **(Compute Cores)** (Impact: 19.9)
  * `get_public_key` **(Compute Cores)** (Impact: 15.3)
  * `get_private_key` **(Compute Cores)** (Impact: 15.3)
  * `merge_auth` **(Compute Cores)** (Impact: 13.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 131`, `args: 31`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`, `unreferenced_by_name: 18`
* *Architecture:* `api: 27`, `import: 13`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.749
  * `Choke Point (Betweenness):` 0.000789 | `Ripple Effect (Closeness):` 0.124653
  * `Imports (Out-Degree: 4):` Data::Dumper, List::Util, Rex::Config, Rex::Helper::System, Rex::Interface::Exec, Rex::Logger, Sort::Naturally, Symbol...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Rex/Resource/firewall/Provider/iptables.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.788)
- **Top Global Matches:** file_cluster_3: 6.788, file_cluster_8: 20.55, file_cluster_6: 33.398
- **Magnitude:** 246.54 | **LOC:** 174 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.0%), Guard Balance (formerly Safety Score) (83.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `absent` **(Compute Cores)** (Impact: 48.3)
  * `present` **(Compute Cores)** (Impact: 48.2)
  * `_version` **(Compute Cores)** (Impact: 4.9)
  * `new` **(Type Conversions)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 34`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 45`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Data::Dumper, Rex::Commands::Iptables, Rex::Helper::Run, base, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Rex/Pkg/Gentoo.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.056)
- **Top Global Matches:** file_cluster_6: 6.056, file_cluster_4: 10.72, file_cluster_8: 14.917
- **Magnitude:** 244.7 | **LOC:** 235 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.617; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_installed` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `get_installed` **(Compute Cores)** (Impact: 22.9)
  * `add_repository` **(Compute Cores)** (Impact: 18.8)
  * `rm_repository` **(Compute Cores)** (Impact: 5.7)
  * `new` **(Type Conversions)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 75
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 75`, `structural_boundaries: 58`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 37`, `unreferenced_by_name: 5`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.617
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Rex::Commands::File, Rex::Commands::Run, Rex::Helper::Run, Rex::Pkg::Base, base, v5, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `lib/Rex/Shared/Var/Array.pm` (PERL) | Magnitude: 59.58 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 77, explicit_casts: 35, args: 23
- `t/symlinks.t` (PERL) | Magnitude: 6.38 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 25, test: 25, import: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `t/logger.t` (PERL) | Magnitude: 2.74 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 22, test: 9, bitwise_ops: 8
- `.github/workflows/build_and_test.yml` (YAML) | Magnitude: 50.0 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 260, args: 33, func_start: 30, import: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `t/db.t` (PERL) | Magnitude: 19.64 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 31, test: 15, core_var_decl: 13
- `t/ini.t` (PERL) | Magnitude: 20.64 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 74, test: 35, globals: 29, comprehensions: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `bin/rex` (PERL) | Magnitude: 22.42 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: branch: 33, structural_boundaries: 14, indent_spaces: 14, decorators: 11
- `lib/Rex/Virtualization/Docker.pm` (PERL) | Magnitude: 6.08 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 16, design_snake_case: 16, structural_boundaries: 14, indent_spaces: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/Rex/PkgConf/Base.pm` (PERL) | Magnitude: 4.54 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 5, safety: 2, import: 2
- `lib/Rex/Inventory/DMIDecode/Bios.pm` (PERL) | Magnitude: 5.62 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 5, import: 4, safety: 2
- `lib/Rex/Cron/Linux.pm` (PERL) | Magnitude: 5.58 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 5, import: 4, safety: 2
- `lib/Rex/Pkg/Ubuntu.pm` (PERL) | Magnitude: 5.58 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 5, import: 4, safety: 2
- `lib/Rex/Service/ALT/systemd.pm` (PERL) | Magnitude: 5.58 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 5, import: 4, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `lib/Rex/Inventory/DMIDecode/BaseBoard.pm` (PERL) | Magnitude: 5.64 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 6, import: 4, safety: 2
- `lib/Rex/Service/OpenBSD.pm` (PERL) | Magnitude: 9.3 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 12, core_var_decl: 8, design_snake_case: 8
- `lib/Rex/Inventory/SMBios/Bios.pm` (PERL) | Magnitude: 5.68 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 7, import: 4, safety: 2
- `t/cron.ex` (ELIXIR) | Magnitude: 1.66 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: core_var_decl: 4, design_upper_case: 4, closures: 1
- `lib/Rex/Inventory/DMIDecode/SystemInformation.pm` (PERL) | Magnitude: 5.72 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 9, import: 4, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `lib/Rex.pm` (PERL) | Magnitude: 558.48 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 600, branch: 191, structural_boundaries: 173, state_mutation: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `lib/Rex/Cloud.pm` (PERL) | Magnitude: 19.46 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 26, indent_spaces: 21, import: 7, dependency_injection: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/build_and_test.yml` -> Churn: **100.0%** | Cog Load: 6.3295% | Debt: 99.9943%

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Rex.pm` -> **Severity: 7.762** (Bridge: 0.0777 * Flux: 99.954%)
- `lib/Rex/Helper/Run.pm` -> **Severity: 3.498** (Bridge: 0.035 * Flux: 100.0%)
- `lib/Rex/Commands.pm` -> **Severity: 3.362** (Bridge: 0.0338 * Flux: 99.4424%)
- `lib/Rex/Config.pm` -> **Severity: 2.53** (Bridge: 0.0256 * Flux: 98.9848%)
- `lib/Rex/Helper/Path.pm` -> **Severity: 2.193** (Bridge: 0.0219 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Rex/Logger.pm` -> **Severity: 24.828** (Embedded: 0.4071 * Error Risk: 60.9831%)
- `lib/Rex/Config.pm` -> **Severity: 23.3** (Embedded: 0.401 * Error Risk: 58.1057%)
- `lib/Rex/Template/NG.pm` -> **Severity: 20.677** (Embedded: 0.2633 * Error Risk: 78.5338%)
- `lib/Rex/Helper/Run.pm` -> **Severity: 19.674** (Embedded: 0.2824 * Error Risk: 69.6802%)
- `lib/Rex/Commands.pm` -> **Severity: 19.573** (Embedded: 0.3287 * Error Risk: 59.5445%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Rex/Logger.pm` -> **Severity: 7775.0** (Blast Radius: 77.75 * Doc Risk: 100.0%)
- `lib/Rex/Config.pm` -> **Severity: 5936.681** (Blast Radius: 104.293 * Doc Risk: 56.9231%)
- `lib/Rex/Exporter.pm` -> **Severity: 5910.4** (Blast Radius: 59.104 * Doc Risk: 100.0%)
- `lib/Rex.pm` -> **Severity: 4315.724** (Blast Radius: 57.954 * Doc Risk: 74.4681%)
- `lib/Rex/Helper/Run.pm` -> **Severity: 3223.6** (Blast Radius: 32.236 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 600 literal sites + 6 sites through wrappers = 606

- `chgrp` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lib/Rex/Commands/Fs.pm`
- `chmod` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lib/Rex/Commands/Fs.pm`
- `chown` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lib/Rex/Commands/Fs.pm`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6081 call pairs -- scoped 24.3%, unique 0.0%, ambiguous 4.3%, external 71.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 6057 | 24.4% | 0.0% | 4.3% | 71.3% |
| shell | 24 | 4.2% | 0.0% | 0.0% | 95.8% |

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
