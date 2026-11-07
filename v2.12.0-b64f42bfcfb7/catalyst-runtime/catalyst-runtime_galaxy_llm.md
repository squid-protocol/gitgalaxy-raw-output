# ARCHITECTURAL_BRIEF: catalyst-runtime
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/perl-catalyst/catalyst-runtime.git` |
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
- **Scope:** 485 analyzed artifact(s), 30992 LOC.
- **Load-bearing artifact:** `lib/Catalyst/Test.pm` -- 130 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/Catalyst.pm` -- pulls in 57 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Catalyst/UTF8.pod` at magnitude 7912.91 (structural weight, not risk).
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
| Total Artifacts | 493 |
| Analyzed Artifacts (Scanned) | 485 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 30992 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 98.4% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.523 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3816 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8751 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 29 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 472 | 30839 | 97.3% |
| PLAINTEXT | 11 | 0 | 2.3% |
| M4 | 1 | 27 | 0.2% |
| JSON | 1 | 126 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 485 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 44%, Compute Cores Files 12%, Parameter Forwarders Files 11%, Data / Markup / Trivial 11%, Interface Declarations Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 474 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.rc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mkdn`: 1x Excluded (Unsupported Extension: '.mkdn')
- `.pod`: 1x Excluded (Saturation: Line 18 exceeds 500 chars)
- `.include`: 1x Excluded (Unsupported Extension: '.include')
- `.gif`: 1x Excluded (Explicitly Denied Extension: '.gif')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.6 | 11.4 | 7.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 79.3 | 21.3 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.6 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 1.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 23.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 32.4 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 509 | 117 | 3 | `lib/Catalyst.pm` |
| cleanup | 61 | 30 | 0 | `lib/Catalyst/Response.pm` |
| guards | 915 | 369 | 3 | `lib/Catalyst.pm` |
| danger | 343 | 123 | 2 | `lib/Catalyst.pm` |
| concurrency | 44 | 14 | 0 | `t/live_fork.t` |
| connectivity | 1837 | 321 | 8 | `lib/Catalyst.pm` |
| io | 155 | 37 | 0 | `lib/Catalyst.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 37 | 12 | 0 | `t/live_fork.t` |
| time | 51 | 14 | 0 | `lib/Catalyst/Stats.pm` |
| serialization | 0 | 0 | 0 | - |
| regex | 528 | 109 | 3 | `lib/Catalyst.pm` |
| events | 226 | 35 | 0 | `lib/Catalyst.pm` |
| tests | 2148 | 219 | 11 | `t/aggregate/live_component_controller_action_chained.t` |
| docs | 257 | 60 | 1 | `lib/Catalyst.pm` |
| debt | 297 | 80 | 1 | `lib/Catalyst.pm` |
| mutation | 2506 | 312 | 10 | `lib/Catalyst.pm` |
| dead_code | 416 | 176 | 3 | `t/lib/TestApp/Controller/Root.pm` |
| credential | 0 | 0 | 0 | - |
| threat | 4 | 1 | 0 | `t/unicode_plugin_live.t` |
| ml_ai | 337 | 47 | 0 | `lib/Catalyst.pm` |
| ui | 16 | 9 | 0 | `lib/Catalyst.pm` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Catalyst.pm` (Hits: 33)
- `lib/Catalyst/UTF8.pod` (Hits: 19)
- `lib/Catalyst/Request.pm` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Test.pm** (`lib/Catalyst/Test.pm`) — 130 inbound connections
2. **Moose.pm** (`t/lib/TestApp/Controller/Moose.pm`) — 101 inbound connections
3. **Catalyst.pm** (`lib/Catalyst.pm`) — 86 inbound connections
4. **Utils.pm** (`lib/Catalyst/Utils.pm`) — 25 inbound connections
5. **Request.pm** (`lib/Catalyst/Request.pm`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **Catalyst.pm** (`lib/Catalyst.pm`) — 57 outbound dependencies
2. **arg_constraints.t** (`t/arg_constraints.t`) — 18 outbound dependencies
3. **Dispatcher.pm** (`lib/Catalyst/Dispatcher.pm`) — 17 outbound dependencies
4. **Utils.pm** (`lib/Catalyst/Utils.pm`) — 16 outbound dependencies
5. **utf_incoming.t** (`t/utf_incoming.t`) — 16 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_tests` **(Many-Argument Workhorses)** (@ `t/aggregate/live_component_controller_action_chained.t`) -> Impact: **279.4** | LOC: 1147
- `uri_for` **(Many-Argument Workhorses)** (@ `lib/Catalyst.pm`) -> Impact: **117.2** | LOC: 145
- `setup` **(Many-Argument Workhorses)** (@ `lib/Catalyst.pm`) -> Impact: **100.4** | LOC: 173
- `list` **(Compute Cores)** (@ `lib/Catalyst/DispatchType/Chained.pm`) -> Impact: **90.0** | LOC: 103
- `recurse_match` **(Many-Argument Workhorses)** (@ `lib/Catalyst/DispatchType/Chained.pm`) -> Impact: **83.5** | LOC: 104
- `run_tests` **(I/O & Config Routines)** (@ `t/aggregate/live_component_controller_action_visit.t`) -> Impact: **62.0** | LOC: 259
- `resolve_type_constraint` **(Compute Cores)** (@ `lib/Catalyst/Action.pm`) -> Impact: **58.2** | LOC: 56
- `run_tests` **(I/O & Config Routines)** (@ `t/aggregate/live_component_controller_action_go.t`) -> Impact: **57.1** | LOC: 242
- `prepare_path` **(Compute Cores)** (@ `lib/Catalyst/Engine.pm`) -> Impact: **56.4** | LOC: 55
- `execute` **(Many-Argument Workhorses)** (@ `lib/Catalyst.pm`) -> Impact: **47.0** | LOC: 59

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Catalyst` | 28 | 19091.12 | 19.62% | 16.88% |
| `t/aggregate` | 119 | 2632.98 | 13.1% | 5.63% |
| `t` | 87 | 2370.46 | 16.74% | 16.39% |
| `lib` | 1 | 1827.64 | 32.65% | 10.49% |
| `t/lib/TestApp/Controller/Action` | 22 | 1128.8 | 11.53% | 64.35% |
| `t/lib` | 44 | 573.0 | 3.11% | 15.8% |
| `lib/Catalyst/DispatchType` | 4 | 558.38 | 21.63% | 16.24% |
| `t/lib/TestApp/Controller` | 17 | 503.26 | 13.51% | 60.75% |
| `lib/Catalyst/ActionRole` | 4 | 418.47 | 12.57% | 0.0% |
| `t/lib/TestApp/Controller/Action/Chained` | 9 | 209.06 | 18.73% | 65.74% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/lib/TestApp/Controller/Action/Inheritance.pm` -> **100.0%** Exposure
- `t/lib/TestApp/Controller/HTTPMethods.pm` -> **100.0%** Exposure
- `t/lib/TestApp/Controller/Root.pm` -> **100.0%** Exposure
- `t/lib/TestContentNegotiation/Controller/Root.pm` -> **100.0%** Exposure
- `t/unit_core_methodattributes_method_metaclass_on_subclasses.t` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/aggregate/live_component_controller_args.t` -> **100.0%** Exposure
- `t/lib/TestApp/Controller/Fork.pm` -> **100.0%** Exposure
- `t/lib/TestApp/View/Dump.pm` -> **100.0%** Exposure
- `t/aggregate/live_engine_request_uri.t` -> **99.9914%** Exposure
- `Makefile.PL` -> **99.9809%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/lib/TestApp/Controller/Root.pm` -> **19** Orphaned Functions | **0** Duplicates
- `t/lib/TestApp/Controller/HTTPMethods.pm` -> **16** Orphaned Functions | **0** Duplicates
- `t/lib/TestApp/Controller/Action/Go.pm` -> **12** Orphaned Functions | **0** Duplicates
- `t/lib/TestApp/Controller/Action/Inheritance.pm` -> **0** Orphaned Functions | **12** Duplicates
- `t/lib/TestApp/Controller/Action/Visit.pm` -> **12** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `2312` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Catalyst/UTF8.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.875)
- **Top Global Matches:** file_cluster_13: 4.875, file_cluster_2: 5.081, file_cluster_17: 6.114
- **Magnitude:** 7912.91 | **LOC:** 654 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.4%), Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (19.1%), Debt Markers (formerly Tech Debt) (17.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 138`, `args: 17`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `state_mutation: 2`, `fragile_debt: 3`
* *Architecture:* `io: 19`, `api: 19`, `import: 41`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Upgrading.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 4.755)
- **Top Global Matches:** file_cluster_13: 4.755, file_cluster_2: 4.819, file_cluster_10: 5.661
- **Magnitude:** 3309.77 | **LOC:** 984 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.9%), Complexity Load (formerly Cognitive Load) (14.6%), Concurrency Surface (formerly Concurrency) (14.5%), Debt Markers (formerly Tech Debt) (12.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 209`, `args: 2`, `func_start: 10`, `class_start: 16`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `io: 9`, `api: 23`, `concurrency: 2`, `import: 78`
* *Defense:* `safety: 8`, `doc: 1`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/RouteMatching.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.417)
- **Top Global Matches:** file_cluster_13: 5.417, file_cluster_2: 6.82, file_cluster_0: 7.116
- **Magnitude:** 3183.12 | **LOC:** 394 | **CtrlFlow:** 34.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (15.9%), Connectivity (formerly Api Exposure) (12.2%), Debt Markers (formerly Tech Debt) (9.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 116`, `args: 9`, `func_start: 37`, `class_start: 11`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 37`, `import: 43`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.267)
- **Top Global Matches:** file_cluster_4: 6.267, file_cluster_15: 9.973, file_cluster_16: 11.305
- **Magnitude:** 1827.64 | **LOC:** 5088 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **86** in-repo importer(s); it depends on **57**; blast radius 65.028; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (87.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 22.4066% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uri_for` **(Many-Argument Workhorses)** (Impact: 117.2)
  * `setup` **(Many-Argument Workhorses)** (Impact: 100.4)
  * `execute` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `view` **(Compute Cores)** (Impact: 46.3)
  * `model` **(Compute Cores)** (Impact: 44.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 124 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1016`, `structural_boundaries: 1315`, `args: 151`, `func_start: 136`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 132`, `planned_debt: 1`, `fragile_debt: 8`
* *Architecture:* `io: 33`, `api: 121`, `import: 127`
* *Defense:* `safety: 49`, `doc: 96`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.028
  * `Choke Point (Betweenness):` 0.012983 | `Ripple Effect (Closeness):` 0.210405
  * `Imports (Out-Degree: 14):` Carp, Catalyst::Controller, Catalyst::Devel, Catalyst::EngineLoader, Catalyst::Exception, Catalyst::Exception::Detach, Catalyst::Exception::Go, Catalyst::Log...
  * `Imported By (In-Degree: 86):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Delta.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.935)
- **Top Global Matches:** file_cluster_2: 3.935, file_cluster_13: 5.374, file_cluster_17: 5.491
- **Magnitude:** 1086.0 | **LOC:** 553 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Debt Markers (formerly Tech Debt) (28.9%), Complexity Load (formerly Cognitive Load) (11.0%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 66`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `high_risk_execution: 1`, `fragile_debt: 4`
* *Architecture:* `io: 4`, `api: 1`, `import: 32`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Dispatcher.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.853)
- **Top Global Matches:** file_cluster_15: 6.853, file_cluster_9: 8.021, file_cluster_16: 8.545
- **Magnitude:** 517.4 | **LOC:** 817 | **CtrlFlow:** 27.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (38.6%)
- **Documentation Coverage:** 27.907% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_display_action_tables` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `_command2action` **(Many-Argument Workhorses)** (Impact: 28.9)
    * *Intent:* # $self->_command2action( $c, $command [, \@arguments ] ) # $self->_command2action( $c, $command [, ...
  * `register` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `_do_visit` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `prepare_action` **(Compute Cores)** (Impact: 26.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 251`, `args: 33`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 49`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `api: 15`, `import: 22`
* *Defense:* `safety: 3`, `doc: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` Catalyst::Action, Catalyst::ActionContainer, Catalyst::DispatchType::Default, Catalyst::DispatchType::Index, Catalyst::Exception, Catalyst::Utils, Chained, Class::Load...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Engine.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.78)
- **Top Global Matches:** file_cluster_6: 5.78, file_cluster_4: 10.132, file_cluster_8: 15.08
- **Magnitude:** 496.96 | **LOC:** 858 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **13**; blast radius 2.122; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%), Debt Markers (formerly Tech Debt) (44.9%)
- **Documentation Coverage:** 10.4167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prepare_path` **(Compute Cores)** (Impact: 56.4)
  * `finalize_body` **(Many-Argument Workhorses)** (Impact: 45.3)
  * `prepare_query_parameters` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `prepare_uploads` **(Compute Cores)** (Impact: 30.1)
  * `finalize_error` **(Many-Argument Workhorses)** (Impact: 29.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 169`, `args: 29`, `func_start: 24`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 51`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 22`, `import: 15`
* *Defense:* `safety: 1`, `doc: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.122
  * `Choke Point (Betweenness):` 8.5e-05 | `Ripple Effect (Closeness):` 0.004132
  * `Imports (Out-Degree: 2):` CGI::Simple::Cookie, Catalyst::EngineLoader, Data::Dump, Encode, Errno, HTML::Entities, HTTP::Headers, Hash::MultiValue...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Controller.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.385)
- **Top Global Matches:** file_cluster_15: 6.385, file_cluster_11: 7.948, file_cluster_16: 8.495
- **Magnitude:** 476.1 | **LOC:** 1089 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 4.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.2%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_attrs` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `register_action_methods` **(Compute Cores)** (Impact: 32.0)
  * `_parse_Chained_attr` **(Many-Argument Workhorses)** (Impact: 28.1)
  * `_parse_attr` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `_parse_attr_key_value` **(Compute Cores)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 255`, `structural_boundaries: 323`, `args: 47`, `func_start: 73`, `class_start: 8`
* *Risk/State:* `state_mutation: 32`, `fragile_debt: 3`
* *Architecture:* `api: 61`, `import: 35`
* *Defense:* `safety: 12`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.882
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.145842
  * `Imports (Out-Degree: 3):` Catalyst::Exception, Catalyst::Utils, Class::Load, Class::MOP, List::Util, Moose, Moose::Util, MooseX::MethodAttributes...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Request.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.994)
- **Top Global Matches:** file_cluster_6: 5.994, file_cluster_4: 12.446, file_cluster_8: 12.595
- **Magnitude:** 429.88 | **LOC:** 1169 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **15**; blast radius 10.828; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.1%), Guard Balance (formerly Safety Score) (55.3%)
- **Documentation Coverage:** 75.5102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mangle_params` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `prepare_body_parameters` **(Compute Cores)** (Impact: 37.4)
  * `upload` **(Compute Cores)** (Impact: 33.3)
  * `prepare_body` **(Compute Cores)** (Impact: 29.0)
  * `param` **(Compute Cores)** (Impact: 24.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 245`, `structural_boundaries: 247`, `args: 35`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `state_mutation: 33`, `planned_debt: 1`, `fragile_debt: 10`, `unreferenced_by_name: 1`
* *Architecture:* `io: 13`, `api: 24`, `concurrency: 2`, `import: 20`
* *Defense:* `safety: 4`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.828
  * `Choke Point (Betweenness):` 0.001505 | `Ripple Effect (Closeness):` 0.155878
  * `Imports (Out-Degree: 4):` Carp, Catalyst::Exception, Catalyst::Request::PartData, HTTP::Body, HTTP::Headers, Hash::MultiValue, Moose, Scalar::Util...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Utils.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.554)
- **Top Global Matches:** file_cluster_4: 7.554, file_cluster_15: 8.554, file_cluster_9: 9.287
- **Magnitude:** 416.32 | **LOC:** 743 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **16**; blast radius 63.892; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Complexity Load (formerly Cognitive Load) (31.4%)
- **Documentation Coverage:** 4.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inject_component` **(Defensive Guards)** (Impact: 43.5)
  * `ensure_class_loaded` **(Defensive Guards)** (Impact: 26.0)
  * `term_width` **(Compute Cores)** (Impact: 23.4)
  * `build_middleware` **(Compute Cores)** (Impact: 23.2)
  * `home` **(Compute Cores)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 125
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 263`, `args: 30`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`, `fragile_debt: 1`
* *Architecture:* `api: 29`, `import: 28`
* *Defense:* `safety: 16`, `doc: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 63.892
  * `Choke Point (Betweenness):` 0.002051 | `Ripple Effect (Closeness):` 0.241966
  * `Imports (Out-Degree: 3):` Carp, Catalyst::Exception, Class::Load, Cwd, Devel::InnerPackage, File::Spec, HTTP::Request, Moose::Util...
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `lib/Catalyst/DispatchType/Chained.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.08)
- **Top Global Matches:** file_cluster_6: 8.08, file_cluster_8: 10.147, file_cluster_4: 15.683
- **Magnitude:** 414.56 | **LOC:** 806 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.6%), Connectivity (formerly Api Exposure) (52.6%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `list` **(Compute Cores)** (Impact: 90.0)
  * `recurse_match` **(Many-Argument Workhorses)** (Impact: 83.5)
  * `register` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `uri_for_action` **(Compute Cores)** (Impact: 27.8)
  * `match` **(Many-Argument Workhorses)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 161`, `args: 16`, `func_start: 23`, `class_start: 3`
* *Risk/State:* `state_mutation: 39`
* *Architecture:* `io: 5`, `api: 21`, `import: 18`
* *Defense:* `safety: 3`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Catalyst::ActionChain, Catalyst::Utils, Encode, Moose, Scalar::Util, Text::SimpleTable, URI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/lib/TestApp/Controller/Action/Chained.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 9.558)
- **Top Global Matches:** file_cluster_13: 9.558, file_cluster_15: 11.036, file_cluster_16: 11.853
- **Magnitude:** 378.2 | **LOC:** 257 | **CtrlFlow:** 141.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 0.999; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (29.6%), Debt Markers (formerly Tech Debt) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foo` **(Compute Cores)** (Impact: 14.2)
    * *Intent:* # # TODO # # # Simple parent/child action test #
  * `end` **(Parameter Forwarders)** (Impact: 5.5)
  * `chain_fw_a` **(Annotated & Test Methods)** (Impact: 4.2)
    * *Intent:* # # the ParentChain controller chains to this action by # # # This is just for a test that a loose e...
  * `chain_dt_a` **(Annotated & Test Methods)** (Impact: 4.2)
    * *Intent:* # # Detaching out of the middle of a chain. #
  * `chain_error_a` **(Annotated & Test Methods)** (Impact: 4.2)
    * *Intent:* # # Error in the middle of a chain #
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 103`, `args: 5`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 92`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.999
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002066
  * `Imports (Out-Degree: 0):` HTML::Entities, base, strict, warnings
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Catalyst/ActionRole/Scheme.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.535)
- **Top Global Matches:** file_cluster_10: 4.535, file_cluster_13: 4.715, file_cluster_2: 4.771
- **Magnitude:** 324.89 | **LOC:** 96 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.933; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (8.3%), Connectivity (formerly Api Exposure) (6.1%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 23`, `args: 4`, `func_start: 2`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `io: 3`, `api: 3`, `import: 3`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Moose::Role
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/aggregate/live_component_controller_action_chained.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.703)
- **Top Global Matches:** file_cluster_1: 5.703, file_cluster_3: 48.262, file_cluster_8: 70.094
- **Magnitude:** 308.6 | **LOC:** 1176 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (39.9%), Debt Markers (formerly Tech Debt) (14.7%), Mutation Surface (formerly State Flux) (14.1%), Complexity Load (formerly Cognitive Load) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_tests` **(Many-Argument Workhorses)** (Impact: 279.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 183`, `args: 1`, `func_start: 1`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 6`, `fragile_debt: 2`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 4`, `test: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Args, Benchmark, Catalyst::Test, FindBin, Test::More, URI, URI::QueryParam, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Action.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.814)
- **Top Global Matches:** file_cluster_4: 6.814, file_cluster_6: 9.037, file_cluster_9: 13.157
- **Magnitude:** 276.1 | **LOC:** 627 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 1.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.0%), Connectivity (formerly Api Exposure) (46.6%), Mutation Surface (formerly State Flux) (21.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolve_type_constraint` **(Compute Cores)** (Impact: 58.2)
  * `_build_number_of_args_constraints` **(Compute Cores)** (Impact: 30.8)
  * `match_args` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `_build_number_of_capture_constraints` **(Compute Cores)** (Impact: 23.2)
  * `match_captures_constraints` **(Compute Cores)** (Impact: 19.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 174`, `args: 19`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 4`, `dead_code: 2`
* *Architecture:* `api: 13`, `import: 10`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.417
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.004132
  * `Imports (Out-Degree: 2):` CaptureArgs, Moose, Moose::Util::TypeConstraints, Scalar::Util, Type::Registry, namespace::clean, overload, warnings
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `t/arg_constraints.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.639)
- **Top Global Matches:** file_cluster_13: 6.639, file_cluster_15: 7.596, file_cluster_0: 8.144
- **Magnitude:** 219.22 | **LOC:** 597 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.6%), Mutation Surface (formerly State Flux) (40.0%), Debt Markers (formerly Tech Debt) (28.6%), Complexity Load (formerly Cognitive Load) (15.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `user` **(Type Conversions)** (Impact: 8.2)
  * `user_object` **(Compute Cores)** (Impact: 8.2)
    * *Intent:* # Tests using this are current skipped pending coercion rethink
  * `default` **(Type Conversions)** (Impact: 8.2)
  * `tuple` **(Generic / Templated Code)** (Impact: 4.7)
  * `slurpy_tuple` **(Generic / Templated Code)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 175`, `args: 17`, `func_start: 46`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 47`, `import: 33`
* *Defense:* `safety: 27`, `doc: 1`, `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Catalyst, Catalyst::Test, HTTP::Request::Common, Moose, Moose::Role, MooseX::MethodAttributes, MooseX::MethodAttributes::Role, MyApp::Types...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Response.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.812)
- **Top Global Matches:** file_cluster_15: 5.812, file_cluster_11: 7.353, file_cluster_10: 7.561
- **Magnitude:** 154.92 | **LOC:** 742 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 4.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (38.7%), Concurrency Surface (formerly Concurrency) (27.6%)
- **Documentation Coverage:** 76.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_psgi_response` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `encodable_response` **(Compute Cores)** (Impact: 20.0)
  * `redirect` **(Compute Cores)** (Impact: 10.8)
  * `write` **(Compute Cores)** (Impact: 7.8)
  * `unencoded_write` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 147`, `args: 23`, `func_start: 17`, `class_start: 3`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 1`
* *Architecture:* `io: 10`, `api: 16`, `concurrency: 2`, `import: 18`
* *Defense:* `safety: 5`, `doc: 4`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.882
  * `Choke Point (Betweenness):` 0.000971 | `Ripple Effect (Closeness):` 0.145842
  * `Imports (Out-Degree: 3):` Catalyst::Response::Writer, Catalyst::Utils, HTTP::Headers, Moose, Moose::Util::TypeConstraints, Scalar::Util, namespace::clean
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Test.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 7.113)
- **Top Global Matches:** file_cluster_9: 7.113, file_cluster_10: 8.632, file_cluster_15: 8.881
- **Magnitude:** 154.54 | **LOC:** 476 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **130** in-repo importer(s); it depends on **14**; blast radius 73.915; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%), Complexity Load (formerly Cognitive Load) (26.4%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_remote_request` **(Compute Cores)** (Impact: 24.0)
  * `_local_request` **(Compute Cores)** (Impact: 17.6)
  * `import` **(Compute Cores)** (Impact: 16.7)
  * `_customize_request` **(Compute Cores)** (Impact: 12.8)
  * `_build_ctx_request_export` **(Many-Argument Workhorses)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 180`, `args: 22`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `fragile_debt: 2`
* *Architecture:* `io: 2`, `api: 1`, `import: 33`
* *Defense:* `safety: 6`, `doc: 2`, `test: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 73.915
  * `Choke Point (Betweenness):` 0.006817 | `Ripple Effect (Closeness):` 0.268657
  * `Imports (Out-Degree: 3):` Carp, Catalyst::Exception, Catalyst::Test, Catalyst::Utils, Class::Load, HTML::HeadParser, LWP::UserAgent, Moose::Util...
  * `Imported By (In-Degree: 130):` (Excluded from Brief to save tokens)

### `lib/Catalyst/Exception/Interface.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.314)
- **Top Global Matches:** file_cluster_2: 4.314, file_cluster_10: 4.787, file_cluster_17: 5.129
- **Magnitude:** 146.08 | **LOC:** 75 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.933; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (8.6%), Connectivity (formerly Api Exposure) (6.4%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 13`, `args: 2`, `func_start: 3`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Moose::Role, namespace::clean, overload
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/utf_incoming.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.113)
- **Top Global Matches:** file_cluster_15: 6.113, file_cluster_13: 6.246, file_cluster_2: 7.866
- **Magnitude:** 138.12 | **LOC:** 567 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.9%), Mutation Surface (formerly State Flux) (10.7%), Connectivity (formerly Api Exposure) (10.3%), Complexity Load (formerly Cognitive Load) (7.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stream_body_fh2` **(Compute Cores)** (Impact: 9.1)
    * *Intent:* # If you pull the file contents into a var, NOW you need to specify the # IO encoding on the FH. Ult...
  * `stream_body_fh` **(Compute Cores)** (Impact: 7.3)
    * *Intent:* # Stream a file with utf8 chars directly, you don't need to decode
  * `argend` **(Type Conversions)** (Impact: 4.8)
  * `file_upload` **(Parameter Forwarders)** (Impact: 4.4)
  * `file_upload_utf8_param` **(Parameter Forwarders)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 141`, `args: 23`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`
* *Architecture:* `io: 2`, `api: 25`, `import: 17`
* *Defense:* `safety: 3`, `test: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Catalyst, Catalyst::Test, Compress::Zlib, Data::Dumper, Encode, File::Spec, HTTP::Message::PSGI, HTTP::Request::Common...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Stats.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.582)
- **Top Global Matches:** file_cluster_4: 7.582, file_cluster_6: 8.153, file_cluster_15: 13.487
- **Magnitude:** 131.92 | **LOC:** 383 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.8%), Complexity Load (formerly Cognitive Load) (56.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `report` **(Compute Cores)** (Impact: 32.9)
  * `profile` **(Compute Cores)** (Impact: 20.9)
  * `addChild` **(Parameter Forwarders)** (Impact: 3.5)
  * `setNodeValue` **(Parameter Forwarders)** (Impact: 3.4)
  * `_get_uid` **(Parameter Forwarders)** (Impact: 2.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 60`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 8`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Catalyst::Utils, Moose, Text::SimpleTable, Time::HiRes, Tree::Simple, Tree::Simple::Visitor::FindByUID, namespace::clean
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Catalyst/Script/Server.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.872)
- **Top Global Matches:** file_cluster_9: 5.872, file_cluster_15: 9.339, file_cluster_16: 9.845
- **Magnitude:** 128.24 | **LOC:** 345 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.726; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.7%), Concurrency Surface (formerly Concurrency) (71.4%), Debt Markers (formerly Tech Debt) (61.7%), Guard Balance (formerly Safety Score) (55.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 19.4)
  * `_plack_loader_args` **(Compute Cores)** (Impact: 18.2)
  * `_restarter_args` **(Compute Cores)** (Impact: 13.5)
  * `BUILD` **(Compute Cores)** (Impact: 10.6)
  * `_plack_engine_name` **(Compute Cores)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 46`, `args: 10`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 14`, `fragile_debt: 1`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `api: 3`, `concurrency: 6`, `import: 8`
* *Defense:* `safety: 13`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.726
  * `Choke Point (Betweenness):` 7.7e-05 | `Ripple Effect (Closeness):` 0.002066
  * `Imports (Out-Degree: 3):` Catalyst, Catalyst::Restarter, Catalyst::Utils, Class::Load, Moose, Moose::Util::TypeConstraints, namespace::clean
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Catalyst/ActionChain.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.88)
- **Top Global Matches:** file_cluster_15: 5.88, file_cluster_16: 7.823, file_cluster_9: 8.176
- **Magnitude:** 123.46 | **LOC:** 242 | **CtrlFlow:** 37.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 1.091; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next` **(Compute Cores)** (Impact: 16.3)
  * `match_captures_constraints` **(Compute Cores)** (Impact: 12.6)
  * `_dispatch_chain_actions` **(Compute Cores)** (Impact: 11.2)
  * `_dispatch_chain_action` **(Compute Cores)** (Impact: 9.3)
  * `_abort_needed` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 80`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 3`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.091
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002066
  * `Imports (Out-Degree: 1):` Moose
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/lib/TestApp/Controller/Action/Visit.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.256)
- **Top Global Matches:** file_cluster_13: 7.256, file_cluster_15: 7.67, file_cluster_11: 9.205
- **Magnitude:** 122.78 | **LOC:** 105 | **CtrlFlow:** 36.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 1.197; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.6%), Mutation Surface (formerly State Flux) (26.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visit_chained` **(Compute Cores)** (Impact: 15.0)
  * `visit_die` **(Defensive Guards)** (Impact: 8.2)
  * `view` **(Defensive Guards)** (Impact: 8.2)
  * `model` **(Defensive Guards)** (Impact: 8.2)
  * `args` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 40`, `args: 18`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 19`, `import: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.197
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002066
  * `Imports (Out-Degree: 0):` base, strict
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `t/psgi_utils.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.641)
- **Top Global Matches:** file_cluster_15: 6.641, file_cluster_13: 6.893, file_cluster_11: 7.534
- **Magnitude:** 115.04 | **LOC:** 442 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.6%), Mutation Surface (formerly State Flux) (15.1%), Debt Markers (formerly Tech Debt) (12.6%), Connectivity (formerly Api Exposure) (10.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_env` **(Compute Cores)** (Impact: 9.3)
  * `filehandle` **(Compute Cores)** (Impact: 8.3)
  * `mounted` **(Type Conversions)** (Impact: 6.3)
  * `streaming_body` **(Callbacks & Closures)** (Impact: 4.5)
  * `streaming_body_with_charset` **(Callbacks & Closures)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 121`, `args: 19`, `func_start: 19`, `class_start: 4`
* *Risk/State:* `state_mutation: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `api: 21`, `import: 13`
* *Defense:* `safety: 2`, `test: 35`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Catalyst, Catalyst::Test, Catalyst::Utils, Encode, Plack::Request, Test::More, base, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `t/query_constraints.t` (PERL) | Magnitude: 44.3 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 51, branch: 41, bitwise_ops: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `t/unit_stats.t` (PERL) | Magnitude: 45.32 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 95, structural_boundaries: 29, state_mutation: 28, test: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `t/configured_comps.t` (PERL) | Magnitude: 39.9 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 44, import: 13, branch: 10
- `t/lib/TestAppPathBug.pm` (PERL) | Magnitude: 8.2 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 15, import: 8, safety: 6, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `t/aggregate/live_engine_request_env.t` (PERL) | Magnitude: 20.68 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 13, import: 9, indent_spaces: 8, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `t/lib/TestApp/Controller/Engine/Request/Uploads.pm` (PERL) | Magnitude: 7.86 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, branch: 2, api: 2
- `lib/Catalyst/Upgrading.pod` (PERL) | Magnitude: 3309.77 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 209, branch: 168, indent_spaces: 151, import: 78
- `t/body_fh.t` (PERL) | Magnitude: 23.8 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 71, structural_boundaries: 49, test: 12, args: 8
- `t/aggregate/unit_utils_request.t` (PERL) | Magnitude: 15.44 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, branch: 10, structural_boundaries: 8, test: 5
- `t/lib/TestApp/Controller/Keyword.pm` (PERL) | Magnitude: 9.38 | Delta: **0.112** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 6, branch: 3, indent_spaces: 3, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `t/lib/TestAppOneView/Controller/Root.pm` (PERL) | Magnitude: 15.92 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 13, indent_spaces: 10, api: 4, branch: 3
- `xt/author/http-server.t` (PERL) | Magnitude: 40.74 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: structural_boundaries: 36, indent_spaces: 32, branch: 17, import: 14
- `t/lib/TestApp/Action/TestMyAction.pm` (PERL) | Magnitude: 7.18 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, args: 3, import: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/lib/TestPluginWithConstructor.pm` (PERL) | Magnitude: 3.84 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 12, import: 5, safety: 4, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `t/aggregate/unit_load_catalyst_test.t` (PERL) | Magnitude: 7.74 | Delta: **0.099** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 49, test: 24, branch: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `t/aggregate/unit_core_script_help.t` (PERL) | Magnitude: 6.02 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 15, indent_spaces: 11, import: 8, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `lib/Catalyst/Component.pm` (PERL) | Magnitude: 85.08 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 93, indent_spaces: 89, branch: 58, import: 18
- `lib/Catalyst/EngineLoader.pm` (PERL) | Magnitude: 44.62 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 78, branch: 29, structural_boundaries: 23, core_var_decl: 17

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Catalyst.pm` -> **Severity: 1.134** (Bridge: 0.013 * Flux: 87.3712%)
- `lib/Catalyst/Test.pm` -> **Severity: 0.655** (Bridge: 0.0068 * Flux: 96.0459%)
- `lib/Catalyst/Utils.pm` -> **Severity: 0.205** (Bridge: 0.0021 * Flux: 99.9437%)
- `lib/Catalyst/Request.pm` -> **Severity: 0.138** (Bridge: 0.0015 * Flux: 91.8779%)
- `lib/Catalyst/Log.pm` -> **Severity: 0.098** (Bridge: 0.001 * Flux: 97.3193%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Catalyst/Utils.pm` -> **Severity: 14.184** (Embedded: 0.242 * Error Risk: 58.6203%)
- `lib/Catalyst/Test.pm` -> **Severity: 14.163** (Embedded: 0.2687 * Error Risk: 52.7166%)
- `lib/Catalyst.pm` -> **Severity: 11.338** (Embedded: 0.2104 * Error Risk: 53.8878%)
- `t/lib/TestApp/Controller/Engine/Request/URI.pm` -> **Severity: 9.93** (Embedded: 0.1898 * Error Risk: 52.3239%)
- `lib/Catalyst/Request.pm` -> **Severity: 8.619** (Embedded: 0.1559 * Error Risk: 55.2956%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/lib/TestApp/Controller/Moose.pm` -> **Severity: 13164.2** (Blast Radius: 131.642 * Doc Risk: 100.0%)
- `lib/Catalyst/Test.pm` -> **Severity: 6570.223** (Blast Radius: 73.915 * Doc Risk: 88.8889%)
- `t/lib/TestAppClassExceptionSimpleTest.pm` -> **Severity: 4915.0** (Blast Radius: 49.15 * Doc Risk: 100.0%)
- `t/lib/TestApp/Controller/Engine/Request/URI.pm` -> **Severity: 2651.5** (Blast Radius: 26.515 * Doc Risk: 100.0%)
- `lib/Catalyst.pm` -> **Severity: 1457.056** (Blast Radius: 65.028 * Doc Risk: 22.4066%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 5425 call pairs -- scoped 2.8%, unique 0.0%, ambiguous 6.9%, external 90.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 5425 | 2.8% | 0.0% | 6.9% | 90.3% |

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
