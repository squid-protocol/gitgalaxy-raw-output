# ARCHITECTURAL_BRIEF: ack3
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/beyondgrep/ack3.git` |
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
- **Scope:** 199 analyzed artifact(s), 13778 LOC.
- **Load-bearing artifact:** `t/Util.pm` -- 68 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `ack` -- pulls in 23 dependencies, the widest assembly point in the scan.
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
| Analyzed Artifacts (Scanned) | 199 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 98 |
| Total LOC | 13778 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5039 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5349 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4179 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 126 | 12391 | 63.3% |
| YAML | 21 | 1038 | 10.6% |
| PLAINTEXT | 16 | 0 | 8.0% |
| MARKDOWN | 12 | 0 | 6.0% |
| HTML | 5 | 142 | 2.5% |
| PYTHON | 4 | 87 | 2.0% |
| SHELL | 3 | 15 | 1.5% |
| CSHARP | 3 | 8 | 1.5% |
| RUBY | 2 | 64 | 1.0% |
| FORTRAN | 2 | 22 | 1.0% |
| DOCKERFILE | 1 | 5 | 0.5% |
| MAKEFILE | 1 | 1 | 0.5% |
| CSS | 1 | 1 | 0.5% |
| JAVASCRIPT | 1 | 2 | 0.5% |
| LUA | 1 | 2 | 0.5% |

## 4.1 SOURCE ENCODINGS
All 199 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 37%, Declarative / Non-Code 35%, Large Core Modules (3) 8%, Parameter Forwarders Files 7%, Large Core Modules 4%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 171 | 85.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 28 | 14.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 98*

**Composition by Extension & Reason:**
- `no_extension`: 28x Unsupported Format (.undeterminable), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 114 LOC)
- `.0`: 10x Excluded (Unsupported Extension: '.0')
- `.xxx`: 8x Excluded (Unsupported Extension: '.xxx')
- `.yaml`: 1x Zero-Density Threshold (LOC: 74, Signals: 0), 1x Zero-Density Threshold (LOC: 82, Signals: 0), 1x Zero-Density Threshold (LOC: 98, Signals: 0)
- `.1`: 1x Excluded (Machine-Generated Source Code Signature: 5566 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5800 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5914 LOC)
- `.2`: 1x Excluded (Machine-Generated Source Code Signature: 5616 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5851 LOC), 1x Excluded (Machine-Generated Source Code Signature: 6290 LOC)
- `.3`: 1x Excluded (Machine-Generated Source Code Signature: 5619 LOC), 1x Excluded (Machine-Generated Source Code Signature: 5849 LOC)
- `.min`: 2x Excluded (Unsupported Extension: '.min')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.96`: 1x Excluded (Unsupported Extension: '.96')
- `.22`: 1x Excluded (Unsupported Extension: '.22')
- `.24`: 1x Excluded (Unsupported Extension: '.24')
- `.master`: 1x Excluded (Unsupported Extension: '.master')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.pl`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2131 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.0 | 19.7 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 79.6 | 31.4 | 48.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.7 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 179 | 40 | 2 | `t/Util.pm` |
| cleanup | 64 | 12 | 0 | `t/Util.pm` |
| guards | 286 | 129 | 2 | `t/run_yaml_test.py` |
| danger | 300 | 74 | 3 | `t/Util.pm` |
| concurrency | 20 | 4 | 0 | `t/Util.pm` |
| connectivity | 254 | 52 | 4 | `t/Util.pm` |
| io | 130 | 24 | 1 | `ack` |
| crypto | 0 | 0 | 0 | - |
| ipc | 25 | 8 | 0 | `t/Util.pm` |
| time | 18 | 8 | 0 | `t/highlighting.t` |
| serialization | 2 | 2 | 0 | `t/swamp/crystallography-weenies.f` |
| regex | 368 | 56 | 3 | `lib/App/Ack.pm` |
| events | 10 | 6 | 0 | `t/run_yaml_test.py` |
| tests | 429 | 90 | 7 | `t/ack-color.t` |
| docs | 181 | 55 | 3 | `t/ack-g.yaml` |
| debt | 250 | 46 | 3 | `ack` |
| mutation | 2001 | 136 | 21 | `lib/App/Ack/ConfigLoader.pm` |
| dead_code | 81 | 26 | 1 | `t/swamp/Makefile` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `t/file-permission.t` |
| ml_ai | 23 | 8 | 0 | `dev/Cookbook.pm` |
| ui | 38 | 1 | 0 | `dev/generate-completion-scripts.pl` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.6667**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `ack` (Hits: 55)
- `t/Util.pm` (Hits: 31)
- `lib/App/Ack/File.pm` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Util.pm** (`t/Util.pm`) — 68 inbound connections
2. **Ack.pm** (`lib/App/Ack.pm`) — 12 inbound connections
3. **ConfigLoader.pm** (`lib/App/Ack/ConfigLoader.pm`) — 5 inbound connections
4. **Filter.pm** (`lib/App/Ack/Filter.pm`) — 5 inbound connections
5. **FilterTest.pm** (`t/FilterTest.pm`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ack** (`ack`) — 23 outbound dependencies
2. **Util.pm** (`t/Util.pm`) — 18 outbound dependencies
3. **timings.pl** (`dev/timings.pl`) — 12 outbound dependencies
4. **ConfigLoader.pm** (`lib/App/Ack/ConfigLoader.pm`) — 12 outbound dependencies
5. **00-load.t** (`t/00-load.t`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `windows_slashify` **(Many-Argument Workhorses)** (@ `t/Util.pm`) -> Impact: **367.3** | LOC: 411
- `options_clean` **(I/O & Config Routines)** (@ `lib/App/Ack/ConfigDefault.pm`) -> Impact: **277.9** | LOC: 517
- `_options_block` **(I/O & Config Routines)** (@ `lib/App/Ack/ConfigDefault.pm`) -> Impact: **276.5** | LOC: 510
- `ackbar` **(Compute Cores)** (@ `lib/App/Ack.pm`) -> Impact: **176.1** | LOC: 101
- `get_arg_spec` **(Many-Argument Workhorses)** (@ `lib/App/Ack/ConfigLoader.pm`) -> Impact: **112.8** | LOC: 146
- `print_line_with_options` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **96.7** | LOC: 122
- `show_help` **(I/O & Config Routines)** (@ `lib/App/Ack.pm`) -> Impact: **72.5** | LOC: 171
- `pmif_context` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **68.5** | LOC: 74
- `build_regex` **(Compute Cores)** (@ `lib/App/Ack.pm`) -> Impact: **68.4** | LOC: 87
  * *Intent:* # Returns a regex object based on a string and command-line options. # Dies when the regex $str is undefined (i.e. not given on command line).
- `pmif_normal` **(Many-Argument Workhorses)** (@ `ack`) -> Impact: **65.8** | LOC: 63

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 94 | 3762.72 | 24.21% | 5.02% |
| `lib/App/Ack` | 6 | 1554.56 | 29.11% | 14.34% |
| `__monolith__` | 13 | 1363.88 | 7.56% | 2.71% |
| `lib/App` | 1 | 644.76 | 79.06% | 14.79% |
| `dev` | 17 | 633.94 | 26.16% | 6.68% |
| `t/swamp` | 31 | 300.25 | 1.64% | 4.87% |
| `lib/App/Ack/Filter` | 12 | 212.94 | 7.5% | 92.81% |
| `xt` | 4 | 154.04 | 38.61% | 0.0% |
| `t/range` | 5 | 65.38 | 0.0% | 16.35% |
| `t/swamp/blib` | 2 | 28.32 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/App/Ack/Filter/FirstLineMatch.pm` -> **99.9999%** Exposure
- `lib/App/Ack/Filter/Match.pm` -> **99.9999%** Exposure
- `t/filetypes.t` -> **99.9988%** Exposure
- `lib/App/Ack/Filter/Collection.pm` -> **99.593%** Exposure
- `lib/App/Ack/Filter/Extension.pm` -> **99.593%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `dev/crank-mutex` -> **100.0%** Exposure
- `t/ack-group.t` -> **100.0%** Exposure
- `t/ack-n.t` -> **100.0%** Exposure
- `t/ack-pager.t` -> **100.0%** Exposure
- `t/ack-passthru.t` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/App/Ack.pm` -> **5** Orphaned Functions | **0** Duplicates
- `lib/App/Ack/Filter/Collection.pm` -> **4** Orphaned Functions | **0** Duplicates
- `lib/App/Ack/Filter/Extension.pm` -> **4** Orphaned Functions | **0** Duplicates
- `lib/App/Ack/Filter/ExtensionGroup.pm` -> **4** Orphaned Functions | **0** Duplicates
- `lib/App/Ack/Filter/FirstLineMatch.pm` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `7` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `687` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `ack` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 7.977)
- **Top Global Matches:** file_cluster_3: 7.977, file_cluster_8: 18.047, file_cluster_6: 30.844
- **Magnitude:** 1276.16 | **LOC:** 2545 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.5%), Guard Balance (formerly Safety Score) (68.2%)
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
* *Defense:* `safety: 4`, `doc: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` App::Ack, App::Ack::ConfigLoader, App::Ack::File, App::Ack::Files, App::Ack::Filter, App::Ack::Filter::Collection, App::Ack::Filter::Default, App::Ack::Filter::Extension...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/Util.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.068)
- **Top Global Matches:** file_cluster_4: 8.068, file_cluster_15: 8.072, file_cluster_12: 9.256
- **Magnitude:** 1078.72 | **LOC:** 1380 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **68** in-repo importer(s); it depends on **18**; blast radius 190.266; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.7%), Concurrency Surface (formerly Concurrency) (92.7%), Test Surface (formerly Verification) (80.0%)
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 7`, `state_mutation: 71`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 31`, `api: 51`, `concurrency: 13`, `import: 21`
* *Defense:* `safety: 3`, `doc: 3`, `test: 18`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 190.266
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.331653
  * `Imports (Out-Degree: 0):` Carp, Cwd, File::Next, File::Spec, File::Temp, IO::Pty, List::Util, Scalar::Util...
  * `Imported By (In-Degree: 68):` (Excluded from Brief to save tokens)

### `lib/App/Ack/ConfigLoader.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.482)
- **Top Global Matches:** file_cluster_6: 6.482, file_cluster_4: 9.628, file_cluster_9: 16.299
- **Magnitude:** 742.6 | **LOC:** 1198 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 11.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 96.1538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_arg_spec` **(Many-Argument Workhorses)** (Impact: 112.8)
  * `_options_used` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* # Processes the command line option and returns a hash of the options that were # used on the comman...
  * `_process_other` **(Many-Argument Workhorses)** (Impact: 42.9)
  * `_generate_ignore_dir` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `_explode_sources` **(Many-Argument Workhorses)** (Impact: 29.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 257`, `args: 42`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 111`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 4`, `api: 6`, `import: 13`
* *Defense:* `safety: 2`, `doc: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.811
  * `Choke Point (Betweenness):` 0.000876 | `Ripple Effect (Closeness):` 0.024272
  * `Imports (Out-Degree: 7):` App::Ack, App::Ack::ConfigDefault, App::Ack::ConfigFinder, App::Ack::Filter, App::Ack::Filter::Collection, App::Ack::Filter::Default, App::Ack::Filter::IsPath, File::Spec...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `lib/App/Ack.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.411)
- **Top Global Matches:** file_cluster_6: 8.411, file_cluster_4: 10.677, file_cluster_8: 17.314
- **Magnitude:** 644.76 | **LOC:** 899 | **CtrlFlow:** 49.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **5**; blast radius 40.477; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 57.4468% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ackbar` **(Compute Cores)** (Impact: 176.1)
  * `show_help` **(I/O & Config Routines)** (Impact: 72.5)
  * `build_regex` **(Compute Cores)** (Impact: 68.4)
    * *Intent:* # Returns a regex object based on a string and command-line options. # Dies when the regex $str is u...
  * `is_lowercase` **(Compute Cores)** (Impact: 25.0)
  * `build_all_regexes` **(Compute Cores)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 172
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 331`, `structural_boundaries: 152`, `args: 13`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 64`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 22`, `import: 12`
* *Defense:* `safety: 5`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 40.477
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.074581
  * `Imports (Out-Degree: 0):` Config, File::Basename, Pod::Usage, strict, warnings
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `lib/App/Ack/ConfigDefault.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 18.053)
- **Top Global Matches:** file_cluster_3: 18.053, file_cluster_1: 34.894, file_cluster_8: 37.958
- **Magnitude:** 563.92 | **LOC:** 541 | **CtrlFlow:** 148.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 7.242; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.7%), Complexity Load (formerly Cognitive Load) (28.0%), Debt Markers (formerly Tech Debt) (20.9%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `options_clean` **(I/O & Config Routines)** (Impact: 277.9)
  * `_options_block` **(I/O & Config Routines)** (Impact: 276.5)
  * `options` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 11`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.242
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.023898
  * `Imports (Out-Degree: 1):` App::Ack, strict, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dev/timings.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.007)
- **Top Global Matches:** file_cluster_9: 7.007, file_cluster_15: 7.593, file_cluster_16: 9.021
- **Magnitude:** 201.02 | **LOC:** 408 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.8%), Guard Balance (formerly Safety Score) (69.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Next, File::Spec, Getopt::Long, JSON, List::Util, Term::ANSIColor, Time::HiRes, Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/Cookbook.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.941)
- **Top Global Matches:** file_cluster_2: 5.941, file_cluster_13: 6.321, file_cluster_17: 7.091
- **Magnitude:** 140.04 | **LOC:** 589 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.6%), Guard Balance (formerly Safety Score) (68.3%), Debt Markers (formerly Tech Debt) (16.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 48`, `args: 2`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 46`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `import: 19`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-output-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.876)
- **Top Global Matches:** file_cluster_13: 4.876, file_cluster_2: 5.245, file_cluster_17: 6.46
- **Magnitude:** 134.5 | **LOC:** 450 | **CtrlFlow:** 35.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (76.6%), Guard Balance (formerly Safety Score) (66.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Term::ANSIColor, Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/run_yaml_test.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.336)
- **Top Global Matches:** file_cluster_9: 7.336, file_cluster_15: 10.941, file_cluster_16: 12.037
- **Magnitude:** 127.88 | **LOC:** 122 | **CtrlFlow:** 53.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.4; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (68.7%), Complexity Load (formerly Cognitive Load) (44.0%), Debt Markers (formerly Tech Debt) (22.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_case` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* """ Runs an individual case from the YAML. """
  * `massage_case` **(Defensive Guards)** (Impact: 19.1)
    * *Intent:* """ Takes the raw case from the YAML and sets defaults. """
  * `test_all_yaml_files` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* """ Walk all the YAML files and run their tests. """
  * `expected_lines` **(Compute Cores)** (Impact: 8.9)
    * *Intent:* """ Gets the lines expected from the case, adjusting on the settings. """
  * `show_diff` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* """ Shows the diffs between two sets of strings """
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 22`, `args: 5`, `func_start: 5`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 19`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 5`, `import: 7`
* *Defense:* `safety: 7`, `doc: 5`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` difflib, glob, logging, os, subprocess, sys, yaml
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Ack/File.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.584)
- **Top Global Matches:** file_cluster_15: 6.584, file_cluster_11: 8.163, file_cluster_16: 8.533
- **Magnitude:** 118.24 | **LOC:** 232 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 9.472; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%), Connectivity (formerly Api Exposure) (48.1%)
- **Documentation Coverage:** 10.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `may_be_present` **(Compute Cores)** (Impact: 22.8)
  * `firstliney` **(Compute Cores)** (Impact: 17.1)
  * `reset` **(Compute Cores)** (Impact: 9.1)
  * `close` **(Compute Cores)** (Impact: 7.7)
  * `open` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 11 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 50`, `args: 10`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`
* *Architecture:* `io: 7`, `api: 9`, `import: 4`
* *Defense:* `safety: 2`, `doc: 8`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.472
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.023898
  * `Imports (Out-Degree: 1):` App::Ack, File::Spec, strict, warnings
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/ack-pager.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.224)
- **Top Global Matches:** file_cluster_13: 5.224, file_cluster_2: 6.249, file_cluster_17: 7.383
- **Magnitude:** 117.92 | **LOC:** 248 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.7%), Guard Balance (formerly Safety Score) (71.8%), Debt Markers (formerly Tech Debt) (9.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-type.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.112)
- **Top Global Matches:** file_cluster_13: 5.112, file_cluster_2: 5.425, file_cluster_17: 6.661
- **Magnitude:** 107.22 | **LOC:** 154 | **CtrlFlow:** 43.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.9%), Guard Balance (formerly Safety Score) (79.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, lines, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xt/man.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.415)
- **Top Global Matches:** file_cluster_8: 9.415, file_cluster_6: 10.747, file_cluster_4: 18.329
- **Magnitude:** 91.38 | **LOC:** 132 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (67.7%), Connectivity (formerly Api Exposure) (5.7%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Data::Dumper, Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-underline.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.032)
- **Top Global Matches:** file_cluster_10: 5.032, file_cluster_13: 5.483, file_cluster_2: 6.1
- **Magnitude:** 84.24 | **LOC:** 156 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (75.8%), Guard Balance (formerly Safety Score) (72.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-passthru.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.747)
- **Top Global Matches:** file_cluster_10: 6.747, file_cluster_15: 7.042, file_cluster_13: 7.182
- **Magnitude:** 71.58 | **LOC:** 188 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (73.2%), Guard Balance (formerly Safety Score) (67.2%), Connectivity (formerly Api Exposure) (2.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/interactive.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.611)
- **Top Global Matches:** file_cluster_13: 4.611, file_cluster_2: 5.267, file_cluster_17: 6.522
- **Magnitude:** 68.1 | **LOC:** 138 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (79.1%), Guard Balance (formerly Safety Score) (65.8%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Term::ANSIColor, Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/App/Ack/ConfigFinder.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.615)
- **Top Global Matches:** file_cluster_9: 7.615, file_cluster_15: 8.757, file_cluster_16: 9.423
- **Magnitude:** 65.48 | **LOC:** 148 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 6.279; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (69.6%), Complexity Load (formerly Cognitive Load) (47.5%), Debt Markers (formerly Tech Debt) (27.2%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_remove_redundancies` **(Compute Cores)** (Impact: 12.2)
  * `find_config_files` **(I/O & Config Routines)** (Impact: 12.0)
  * `_check_for_ackrc` **(I/O & Config Routines)** (Impact: 5.6)
  * `new` **(Type Conversions)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 32`, `args: 2`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 10`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 6`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.279
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.019822
  * `Imports (Out-Degree: 1):` App::Ack, Cwd, File::Spec, if, strict, warnings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/config-loader.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.218)
- **Top Global Matches:** file_cluster_2: 6.218, file_cluster_10: 6.94, file_cluster_15: 7.289
- **Magnitude:** 65.44 | **LOC:** 298 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (21.1%), Connectivity (formerly Api Exposure) (2.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App::Ack::ConfigLoader, App::Ack::Filter::Default, Test::More, Util, argument, lib, strict, targets...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-group.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.182)
- **Top Global Matches:** file_cluster_13: 5.182, file_cluster_2: 5.88, file_cluster_17: 6.975
- **Magnitude:** 64.72 | **LOC:** 110 | **CtrlFlow:** 43.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.8%), Guard Balance (formerly Safety Score) (72.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, break, heading, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/ack-color.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.873)
- **Top Global Matches:** file_cluster_10: 4.873, file_cluster_13: 5.347, file_cluster_2: 5.365
- **Magnitude:** 61.58 | **LOC:** 185 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (63.1%), Guard Balance (formerly Safety Score) (58.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/range.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.132)
- **Top Global Matches:** file_cluster_11: 6.132, file_cluster_10: 6.849, file_cluster_13: 7.193
- **Magnitude:** 55.0 | **LOC:** 281 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (95.5%), Guard Balance (formerly Safety Score) (58.2%), Complexity Load (formerly Cognitive Load) (48.3%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, end, lib, range, start, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile.PL` (PERL | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 8.513)
- **Top Global Matches:** file_cluster_3: 8.513, file_cluster_8: 21.192, file_cluster_6: 33.795
- **Magnitude:** 54.08 | **LOC:** 177 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 3.4; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Guard Balance (formerly Safety Score) (55.0%), Debt Markers (formerly Tech Debt) (25.7%), Complexity Load (formerly Cognitive Load) (22.8%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExtUtils::MakeMaker, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/find-minimum-dep-versions.pl` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.939)
- **Top Global Matches:** file_cluster_15: 5.939, file_cluster_2: 6.356, file_cluster_17: 7.229
- **Magnitude:** 53.54 | **LOC:** 161 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.4; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.5%), Complexity Load (formerly Cognitive Load) (41.7%), Connectivity (formerly Api Exposure) (4.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_releases` **(Compute Cores)** (Impact: 8.1)
  * `bisect` **(Compute Cores)** (Impact: 8.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 41`, `args: 3`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 11`
* *Architecture:* `api: 2`, `import: 8`
* *Defense:* `safety: 2`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Capture::Tiny, File::Spec, File::Temp, MetaCPAN::API, feature, strict, suitable, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/invalid-ackrc.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_10: 6.321, file_cluster_13: 6.856, file_cluster_2: 7.315
- **Magnitude:** 53.2 | **LOC:** 88 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (69.0%), Guard Balance (formerly Safety Score) (65.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` File::Temp, List::Util, Test::More, Util, lib, output, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/highlighting.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.384)
- **Top Global Matches:** file_cluster_15: 6.384, file_cluster_13: 7.215, file_cluster_2: 7.309
- **Magnitude:** 49.4 | **LOC:** 221 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 3.4; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.5%), Guard Balance (formerly Safety Score) (62.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Test::More, Util, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `t/forbidden-options.t` (PERL) | Magnitude: 27.74 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 38, import: 7, branch: 6
- `t/ack-w.t` (PERL) | Magnitude: 17.0 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 29, branch: 23, test: 10
- `dev/record-options` (PERL) | Magnitude: 18.46 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, indent_spaces: 6, import: 5, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `t/swamp/foo_test.py` (PYTHON) | Magnitude: 3.16 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1
- `t/swamp/test_foo.py` (PYTHON) | Magnitude: 3.16 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 2, indent_spaces: 2, args: 1, func_start: 1
- `t/ack-help.t` (PERL) | Magnitude: 32.92 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 23, branch: 10, state_mutation: 6
- `lib/App/Ack/Filter/Extension.pm` (PERL) | Magnitude: 19.1 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 24, indent_spaces: 16, api: 6, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/ack-type-del.t` (PERL) | Magnitude: 36.68 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, branch: 7, state_mutation: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `t/noenv.t` (PERL) | Magnitude: 21.12 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 30, core_var_decl: 12, design_snake_case: 12
- `t/file-permission.t` (PERL) | Magnitude: 21.86 | Delta: **0.159** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 28, test: 11, branch: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `t/Util.pm` (PERL) | Magnitude: 1078.72 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 835, structural_boundaries: 369, branch: 194, state_mutation: 71

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/App/Ack/ConfigLoader.pm` -> **Severity: 0.088** (Bridge: 0.0009 * Flux: 99.9923%)
- `t/FilterTest.pm` -> **Severity: 0.016** (Bridge: 0.0003 * Flux: 50.0%)
- `lib/App/Ack/File.pm` -> **Severity: 0.011** (Bridge: 0.0001 * Flux: 99.8138%)
- `lib/App/Ack/Filter.pm` -> **Severity: 0.004** (Bridge: 0.0003 * Flux: 13.0108%)
- `lib/App/Ack/ConfigFinder.pm` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.994%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/Util.pm` -> **Severity: 20.512** (Embedded: 0.3317 * Error Risk: 61.8473%)
- `lib/App/Ack.pm` -> **Severity: 4.743** (Embedded: 0.0746 * Error Risk: 63.5887%)
- `lib/App/Ack/ConfigLoader.pm` -> **Severity: 1.608** (Embedded: 0.0243 * Error Risk: 66.2667%)
- `lib/App/Ack/Filter.pm` -> **Severity: 1.486** (Embedded: 0.0324 * Error Risk: 45.9092%)
- `lib/App/Ack/File.pm` -> **Severity: 1.384** (Embedded: 0.0239 * Error Risk: 57.8984%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/Util.pm` -> **Severity: 17939.363** (Blast Radius: 190.266 * Doc Risk: 94.2857%)
- `lib/App/Ack.pm` -> **Severity: 2325.274** (Blast Radius: 40.477 * Doc Risk: 57.4468%)
- `lib/App/Ack/ConfigLoader.pm` -> **Severity: 1135.673** (Blast Radius: 11.811 * Doc Risk: 96.1538%)
- `t/FilterTest.pm` -> **Severity: 1014.3** (Blast Radius: 10.143 * Doc Risk: 100.0%)
- `lib/App/Ack/Filter/Inverse.pm` -> **Severity: 832.4** (Blast Radius: 8.324 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 205 literal sites + 2 sites through wrappers = 207
- **`panics_and_aborts`:** 186 literal sites + 7 sites through wrappers = 193

- `_pic_decode` (function, debug_prints, primitive): 2 call sites in 1 files -- `lib/App/Ack.pm`
- `_pic_decode` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `lib/App/Ack.pm`
- `getcwd_clean` (function, panics_and_aborts, primitive): 2 call sites in 2 files -- `t/Util.pm`
- `untaint` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `t/Util.pm`
- `touch_ackrc` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `t/Util.pm`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 938 call pairs -- scoped 23.3%, unique 0.0%, ambiguous 0.7%, external 75.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 872 | 24.5% | 0.0% | 0.8% | 74.7% |
| ruby | 32 | 3.1% | 0.0% | 0.0% | 96.9% |
| python | 29 | 13.8% | 0.0% | 0.0% | 86.2% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |

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
