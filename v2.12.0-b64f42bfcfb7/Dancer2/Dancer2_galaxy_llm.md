# ARCHITECTURAL_BRIEF: Dancer2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/PerlDancer/Dancer2.git` |
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
- **Scope:** 356 analyzed artifact(s), 29043 LOC.
- **Load-bearing artifact:** `lib/Dancer2.pm` -- 160 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/Dancer2/Core/App.pm` -- pulls in 26 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/Dancer2/Manual.pod` at magnitude 19101.96 (structural weight, not risk).
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
| Total Artifacts | 438 |
| Analyzed Artifacts (Scanned) | 356 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 82 |
| Total LOC | 29043 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 81.3% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.566 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4238 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.93 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 17 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 304 | 28413 | 85.4% |
| YAML | 27 | 282 | 7.6% |
| HTML | 7 | 84 | 2.0% |
| PLAINTEXT | 5 | 0 | 1.4% |
| MARKDOWN | 5 | 0 | 1.4% |
| CSS | 4 | 239 | 1.1% |
| SQLITE | 2 | 14 | 0.6% |
| DOCKERFILE | 1 | 6 | 0.3% |
| JSON | 1 | 5 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 356 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 52%, Data / Markup / Trivial 19%, Parameter Forwarders Files 10%, Large Core Modules (3) 6%, Interface Declarations Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 346 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 10 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 82*

**Composition by Extension & Reason:**
- `.tt`: 25x Excluded (Unsupported Extension: '.tt')
- `.t`: 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.psgi`: 2x Excluded (Unsupported Extension: '.psgi')
- `.fcgi`: 2x Excluded (Unsupported Extension: '.fcgi')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.db`: 2x Excluded (Unsupported Extension: '.db')
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 2x Excluded (Unsupported Extension: '.rc')
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')
- `.foo`: 1x Excluded (Unsupported Extension: '.foo')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 63.7 | 7.6 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 18.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 99.6 | 6.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 59.7 | 4.7 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 33.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.4 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 62.3 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 98.5 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 97.9 | 0.3 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 297 | 75 | 2 | `t/types.t` |
| cleanup | 20 | 12 | 0 | `lib/Dancer2/Core/Role/SessionFactory/File.pm` |
| guards | 837 | 263 | 4 | `lib/Dancer2/Core/App.pm` |
| danger | 259 | 75 | 2 | `lib/Dancer2/Plugin.pm` |
| concurrency | 12 | 5 | 0 | `lib/Dancer2/Manual.pod` |
| connectivity | 3376 | 304 | 17 | `lib/Dancer2/Manual.pod` |
| io | 171 | 34 | 0 | `lib/Dancer2/Core/Request.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 7 | 0 | `lib/Dancer2/Manual.pod` |
| time | 60 | 21 | 0 | `lib/Dancer2/Core/Role/Logger.pm` |
| serialization | 5 | 4 | 0 | `lib/Dancer2/Core/DSL.pm` |
| regex | 515 | 116 | 4 | `lib/Dancer2/Plugin.pm` |
| events | 53 | 27 | 0 | `lib/Dancer2/Manual/Tutorial.pod` |
| tests | 1440 | 180 | 11 | `t/dsl/parameters.t` |
| docs | 99 | 73 | 1 | `.github/workflows/ci.yml` |
| debt | 145 | 46 | 1 | `lib/Dancer2/CLI/Gen.pm` |
| mutation | 3758 | 247 | 26 | `lib/Dancer2/Core/App.pm` |
| dead_code | 93 | 48 | 1 | `lib/Dancer2/Core/Request.pm` |
| credential | 3 | 3 | 0 | `lib/Dancer2/Manual/Tutorial.pod` |
| threat | 1 | 1 | 0 | `tools/perf.pl` |
| ml_ai | 138 | 34 | 0 | `lib/Dancer2/Core/App.pm` |
| ui | 425 | 28 | 0 | `lib/Dancer2/Manual/Tutorial.pod` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/Dancer2/Core/Request.pm` (Hits: 23)
- `lib/Dancer2/Manual/Config.pod` (Hits: 20)
- `lib/Dancer2/Manual/Tutorial.pod` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Dancer2.pm** (`lib/Dancer2.pm`) — 160 inbound connections
2. **Types.pm** (`lib/Dancer2/Core/Types.pm`) — 42 inbound connections
3. **Plugin.pm** (`lib/Dancer2/Plugin.pm`) — 29 inbound connections
4. **Core.pm** (`lib/Dancer2/Core.pm`) — 12 inbound connections
5. **Factory.pm** (`lib/Dancer2/Core/Factory.pm`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **App.pm** (`lib/Dancer2/Core/App.pm`) — 26 outbound dependencies
2. **Request.pm** (`lib/Dancer2/Core/Request.pm`) — 18 outbound dependencies
3. **Test.pm** (`lib/Dancer2/Test.pm`) — 18 outbound dependencies
4. **error.t** (`t/error.t`) — 17 outbound dependencies
5. **Response.pm** (`lib/Dancer2/Core/Response.pm`) — 14 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `send_file` **(Many-Argument Workhorses)** (@ `lib/Dancer2/Core/App.pm`) -> Impact: **66.5** | LOC: 129
- `run_test` **(I/O & Config Routines)** (@ `t/request.t`) -> Impact: **61.1** | LOC: 242
- `_copy_templates` **(Many-Argument Workhorses)** (@ `lib/Dancer2/CLI/Gen.pm`) -> Impact: **58.3** | LOC: 48
- `uri_for_route` **(Many-Argument Workhorses)** (@ `lib/Dancer2/Core/App.pm`) -> Impact: **51.8** | LOC: 56
- `dispatch` **(Many-Argument Workhorses)** (@ `lib/Dancer2/Core/App.pm`) -> Impact: **49.7** | LOC: 154
- `match` **(Compute Cores)** (@ `lib/Dancer2/Core/Route.pm`) -> Impact: **46.8** | LOC: 70
- `_build_regexp_from_string` **(Compute Cores)** (@ `lib/Dancer2/Core/Route.pm`) -> Impact: **46.1** | LOC: 55
- `all_tests` **(I/O & Config Routines)** (@ `t/cookie.t`) -> Impact: **46.1** | LOC: 182
- `_build_request_from_env` **(Many-Argument Workhorses)** (@ `lib/Dancer2/Test.pm`) -> Impact: **44.6** | LOC: 93
- `_exporter_app` **(Many-Argument Workhorses)** (@ `lib/Dancer2/Plugin.pm`) -> Impact: **43.8** | LOC: 135
  * *Intent:* # plugin has been called within a D2 app. Modify # the app and export keywords

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/Dancer2` | 10 | 20160.18 | 18.67% | 16.76% |
| `lib/Dancer2/Manual` | 10 | 5716.34 | 16.93% | 4.43% |
| `lib/Dancer2/Core` | 16 | 2549.66 | 24.06% | 17.55% |
| `t` | 84 | 1847.52 | 7.68% | 1.72% |
| `lib/Dancer2/Core/Role` | 13 | 622.4 | 16.29% | 35.58% |
| `t/dsl` | 24 | 520.12 | 6.5% | 3.12% |
| `t/issues` | 19 | 298.64 | 4.44% | 3.24% |
| `lib/Dancer2/CLI` | 2 | 267.8 | 17.02% | 4.87% |
| `t/lib` | 12 | 213.46 | 1.78% | 0.0% |
| `t/plugin2` | 13 | 173.88 | 5.79% | 5.23% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `lib/Dancer2/CLI.pm` -> **99.593%** Exposure
- `lib/Dancer2/Session/Simple.pm` -> **99.593%** Exposure
- `t/lib/Dancer2/Session/SimpleNoChangeId.pm` -> **99.593%** Exposure
- `.github/workflows/ci.yml` -> **95.8936%** Exposure
- `lib/Dancer2/Core/Role/SessionFactory/File.pm` -> **90.242%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/Dancer2/Core/Route.pm` -> **99.9914%** Exposure
- `t/forward_test_tcp.t` -> **99.9868%** Exposure
- `t/lib/Dancer2/Plugin/DefineKeywords.pm` -> **99.9665%** Exposure
- `lib/Dancer2/Serializer/JSON.pm` -> **99.9465%** Exposure
- `lib/Dancer2/Core/Role/Template.pm` -> **99.9351%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `lib/Dancer2/Core/Request.pm` -> **6** Orphaned Functions | **0** Duplicates
- `lib/Dancer2/Core/Role/SessionFactory/File.pm` -> **6** Orphaned Functions | **0** Duplicates
- `lib/Dancer2/CLI.pm` -> **4** Orphaned Functions | **0** Duplicates
- `lib/Dancer2/Core/DSL.pm` -> **4** Orphaned Functions | **0** Duplicates
- `lib/Dancer2/Session/Simple.pm` -> **4** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `t/error.t` -> **97.8667%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1763` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/Dancer2/Manual.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.585)
- **Top Global Matches:** file_cluster_10: 5.585, file_cluster_13: 6.016, file_cluster_2: 6.299
- **Magnitude:** 19101.96 | **LOC:** 2586 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.0%), Concurrency Surface (formerly Concurrency) (14.0%), Complexity Load (formerly Cognitive Load) (13.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 378`, `args: 17`, `func_start: 4`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 7`, `planned_debt: 4`
* *Architecture:* `io: 17`, `api: 82`, `concurrency: 4`, `import: 58`
* *Defense:* `safety: 3`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Manual/Cookbook.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 6.111)
- **Top Global Matches:** file_cluster_13: 6.111, file_cluster_10: 6.165, file_cluster_2: 6.501
- **Magnitude:** 3291.6 | **LOC:** 1012 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (62.3%), Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (27.1%), Complexity Load (formerly Cognitive Load) (19.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 183`, `args: 1`, `func_start: 2`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `planned_debt: 1`
* *Architecture:* `io: 12`, `api: 29`, `import: 55`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Manual/Extending.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.191)
- **Top Global Matches:** file_cluster_13: 5.191, file_cluster_2: 5.623, file_cluster_10: 6.094
- **Magnitude:** 2092.6 | **LOC:** 442 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (53.6%), Debt Markers (formerly Tech Debt) (19.1%), Mutation Surface (formerly State Flux) (17.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 96`, `args: 18`, `func_start: 19`, `class_start: 9`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 4`, `planned_debt: 6`
* *Architecture:* `api: 21`, `import: 16`
* *Defense:* `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/App.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.073)
- **Top Global Matches:** file_cluster_4: 6.073, file_cluster_15: 8.908, file_cluster_12: 10.258
- **Magnitude:** 843.22 | **LOC:** 2135 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 85.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **26**; blast radius 49.332; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (98.5%), Mutation Surface (formerly State Flux) (95.8%), Connectivity (formerly Api Exposure) (56.9%), Guard Balance (formerly Safety Score) (54.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `send_file` **(Many-Argument Workhorses)** (Impact: 66.5)
  * `uri_for_route` **(Many-Argument Workhorses)** (Impact: 51.8)
  * `dispatch` **(Many-Argument Workhorses)** (Impact: 49.7)
  * `send_as` **(Many-Argument Workhorses)** (Impact: 38.4)
  * `to_app` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* # DISPATCHER
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 62 instances
* *Memory Alloc (weighted view):* 14
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 583`, `args: 128`, `func_start: 63`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 81`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 45`, `import: 31`
* *Defense:* `safety: 44`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 49.332
  * `Choke Point (Betweenness):` 0.018549 | `Ripple Effect (Closeness):` 0.245102
  * `Imports (Out-Degree: 10):` Carp, Dancer2::ConfigReader, Dancer2::Core, Dancer2::Core::Cookie, Dancer2::Core::Error, Dancer2::Core::Factory, Dancer2::Core::HTTP, Dancer2::Core::Hook...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Core/Request.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.212)
- **Top Global Matches:** file_cluster_15: 6.212, file_cluster_11: 7.219, file_cluster_12: 7.545
- **Magnitude:** 480.54 | **LOC:** 1225 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **18**; blast radius 12.35; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.0%), Debt Markers (formerly Tech Debt) (52.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `params` **(Defensive Guards)** (Impact: 23.6)
  * `_parse_get_params` **(Compute Cores)** (Impact: 23.3)
  * `uri_for` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `deserialize` **(Compute Cores)** (Impact: 15.7)
  * `_decode` **(Compute Cores)** (Impact: 15.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 369`, `args: 45`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 52`, `fragile_debt: 5`, `unreferenced_by_name: 6`
* *Architecture:* `io: 23`, `api: 54`, `import: 26`
* *Defense:* `safety: 13`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.35
  * `Choke Point (Betweenness):` 0.001599 | `Ripple Effect (Closeness):` 0.174508
  * `Imports (Out-Degree: 3):` CGI::Deurl::XS, Carp, Dancer2::Core::Cookie, Dancer2::Core::Request::Upload, Dancer2::Core::Types, Encode, HTTP::XSCookies, Hash::MultiValue...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Test.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.158)
- **Top Global Matches:** file_cluster_4: 7.158, file_cluster_15: 11.003, file_cluster_13: 11.427
- **Magnitude:** 440.98 | **LOC:** 956 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.0%), Complexity Load (formerly Cognitive Load) (41.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_request_from_env` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `route_pod_coverage` **(Compute Cores)** (Impact: 33.6)
  * `response_headers_include` **(Compute Cores)** (Impact: 16.9)
  * `dancer_response` **(Type Conversions)** (Impact: 11.6)
    * *Intent:* # can be called with the ($method, $path, $option) triplet, # or can be fed a request object directl...
  * `response_status_is` **(Compute Cores)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 243`, `args: 18`, `func_start: 27`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 44`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 31`, `import: 44`
* *Defense:* `safety: 5`, `doc: 1`, `test: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.000141 | `Ripple Effect (Closeness):` 0.005634
  * `Imports (Out-Degree: 4):` Carp, Dancer2, Dancer2::Core::Dispatcher, Dancer2::Core::MIME, Dancer2::Core::Request, Data::Dumper, File::Copy, File::Temp...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Plugin.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.459)
- **Top Global Matches:** file_cluster_12: 7.459, file_cluster_4: 9.866, file_cluster_15: 10.225
- **Magnitude:** 376.82 | **LOC:** 1104 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **10**; blast radius 31.411; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Complexity Load (formerly Cognitive Load) (58.6%), Guard Balance (formerly Safety Score) (57.1%), Debt Markers (formerly Tech Debt) (50.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_exporter_app` **(Many-Argument Workhorses)** (Impact: 43.8)
    * *Intent:* # plugin has been called within a D2 app. Modify # the app and export keywords
  * `_exporter_plugin` **(Defensive Guards)** (Impact: 32.6)
    * *Intent:* # turns the caller namespace into # a D2P2 class, with exported keywords
  * `_p2_has_from_config` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `_exported_plugin_keywords` **(Type Conversions)** (Impact: 16.2)
    * *Intent:* # define the exported 'plugin_keywords'
  * `PluginKeyword` **(Many-Argument Workhorses)** (Impact: 15.4)
    * *Intent:* ### ATTRIBUTE HANDLER STUFF ########################################
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 329`, `args: 34`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 41`, `planned_debt: 2`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 40`, `import: 48`
* *Defense:* `safety: 26`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 31.411
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.084557
  * `Imports (Out-Degree: 0):` Attribute::Handlers, Carp, List::Util, Module::Runtime, Moo, Ref::Util, Scalar::Util, fully...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Core/DSL.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.661)
- **Top Global Matches:** file_cluster_15: 5.661, file_cluster_11: 6.531, file_cluster_13: 8.146
- **Magnitude:** 295.96 | **LOC:** 549 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 1.737; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (54.4%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `session` **(Many-Argument Workhorses)** (Impact: 13.4)
  * `_normalize_route` **(Compute Cores)** (Impact: 11.8)
  * `content` **(Defensive Guards)** (Impact: 9.8)
  * `_add_postponed_plugin_hooks` **(Defensive Guards)** (Impact: 7.9)
  * `any` **(Compute Cores)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 152`, `args: 66`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `unreferenced_by_name: 4`
* *Architecture:* `api: 83`, `import: 12`
* *Defense:* `safety: 11`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.737
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.002817
  * `Imports (Out-Degree: 4):` Carp, Dancer2::Core::Hook, Dancer2::Core::Response::Delayed, Module::Runtime, Moo, Path::Tiny, Ref::Util, content...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `lib/Dancer2/CLI/Gen.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.034)
- **Top Global Matches:** file_cluster_6: 7.034, file_cluster_4: 11.475, file_cluster_8: 15.211
- **Magnitude:** 265.02 | **LOC:** 459 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.4%), Complexity Load (formerly Cognitive Load) (34.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_copy_templates` **(Many-Argument Workhorses)** (Impact: 58.3)
  * `_how_to_run` **(Compute Cores)** (Impact: 40.4)
  * `_check_git` **(Compute Cores)** (Impact: 19.5)
  * `BUILD` **(Compute Cores)** (Impact: 18.4)
    * *Intent:* # Last chance to validate args before we attempt to do something with them
  * `_build_file_list` **(Compute Cores)** (Impact: 16.8)
    * *Intent:* # skel creation routines
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 101`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 7`, `api: 2`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CLI::Osprey, Dancer2::Template::Tiny, File::Which, HTTP::Tiny, IPC::Open3, JSON::MaybeXS, Module::Runtime, Moo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/Route.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.737)
- **Top Global Matches:** file_cluster_8: 6.737, file_cluster_6: 17.459, file_cluster_3: 19.771
- **Magnitude:** 215.76 | **LOC:** 351 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 5.581; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.7%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `match` **(Compute Cores)** (Impact: 46.8)
  * `_build_regexp_from_string` **(Compute Cores)** (Impact: 46.1)
  * `BUILDARGS` **(Defensive Guards)** (Impact: 17.5)
    * *Intent:* # private subs
  * `_check_options` **(Defensive Guards)** (Impact: 11.1)
  * `execute` **(Many-Argument Workhorses)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 75`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.581
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.165885
  * `Imports (Out-Degree: 1):` Carp, Dancer2::Core::Types, List::Util, Module::Runtime, Moo, Ref::Util, Scalar::Util, Type::Registry
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Core/Error.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.845)
- **Top Global Matches:** file_cluster_15: 6.845, file_cluster_12: 8.143, file_cluster_9: 8.173
- **Magnitude:** 212.52 | **LOC:** 638 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 6.307; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `backtrace` **(Compute Cores)** (Impact: 23.4)
  * `_build_content` **(Compute Cores)** (Impact: 21.6)
  * `environment` **(Compute Cores)** (Impact: 13.6)
  * `default_error_page` **(Compute Cores)** (Impact: 13.2)
  * `dumper` **(Compute Cores)** (Impact: 11.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 173`, `args: 21`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 16`
* *Defense:* `safety: 16`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.307
  * `Choke Point (Betweenness):` 0.00175 | `Ripple Effect (Closeness):` 0.167479
  * `Imports (Out-Degree: 4):` Carp, Clone, Dancer2::Core::HTTP, Dancer2::Core::MIME, Dancer2::Core::Types, Data::Dumper, Module::Runtime, Moo...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Manual/Tutorial.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.976)
- **Top Global Matches:** file_cluster_13: 5.976, file_cluster_10: 6.167, file_cluster_2: 6.204
- **Magnitude:** 143.2 | **LOC:** 2548 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.0%), Complexity Load (formerly Cognitive Load) (17.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (16.8%), Mutation Surface (formerly State Flux) (15.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 570`, `structural_boundaries: 369`, `class_start: 4`
* *Risk/State:* `state_mutation: 11`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 19`, `api: 58`, `import: 67`
* *Defense:* `safety: 28`, `doc: 1`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/Role/Template.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.687)
- **Top Global Matches:** file_cluster_15: 5.687, file_cluster_11: 7.095, file_cluster_10: 7.838
- **Magnitude:** 138.1 | **LOC:** 360 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 4.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.7%), Guard Balance (formerly Safety Score) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `apply_layout` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `process` **(Many-Argument Workhorses)** (Impact: 12.4)
  * `_prepare_tokens_options` **(Compute Cores)** (Impact: 8.0)
  * `layout_pathname` **(Compute Cores)** (Impact: 5.6)
  * `apply_renderer` **(Parameter Forwarders)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 74`, `args: 21`, `func_start: 14`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`, `planned_debt: 2`, `fragile_debt: 2`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `safety: 10`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.5
  * `Choke Point (Betweenness):` 0.000203 | `Ripple Effect (Closeness):` 0.019718
  * `Imports (Out-Degree: 2):` Carp, Dancer2::Core::Types, Moo::Role, Path::Tiny, Ref::Util, Scalar::Util
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `lib/Dancer2/ConfigReader.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.065)
- **Top Global Matches:** file_cluster_4: 8.065, file_cluster_6: 8.313, file_cluster_15: 14.123
- **Magnitude:** 133.8 | **LOC:** 518 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 7.308; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (72.3%), Guard Balance (formerly Safety Score) (51.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_warn_unknown_engine_config_keys` **(Compute Cores)** (Impact: 31.5)
  * `_build_config` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* # The config builder
  * `_strict_config_keys` **(Compute Cores)** (Impact: 19.1)
  * `_build_config_readers` **(Compute Cores)** (Impact: 7.8)
  * `_normalize_engine_name` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 87`, `structural_boundaries: 106`, `args: 10`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 1`, `import: 15`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.308
  * `Choke Point (Betweenness):` 0.002899 | `Ripple Effect (Closeness):` 0.169655
  * `Imports (Out-Degree: 5):` Carp, Config::Any, Dancer2::ConfigUtils, Dancer2::Core, Dancer2::Core::Factory, Dancer2::Core::Types, Hash::Merge::Simple, Module::Runtime...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Core/Role/Logger.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.426)
- **Top Global Matches:** file_cluster_4: 7.426, file_cluster_15: 10.845, file_cluster_11: 11.659
- **Magnitude:** 120.08 | **LOC:** 331 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (71.6%), Guard Balance (formerly Safety Score) (49.1%), Mutation Surface (formerly State Flux) (21.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `map_chars_to_subs` **(Compute Cores)** (Impact: 41.3)
  * `format_message` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `_serialize` **(Type Conversions)** (Impact: 7.6)
  * `_should` **(Parameter Forwarders)** (Impact: 2.0)
  * `core` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 88`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 9`, `import: 7`
* *Defense:* `safety: 5`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Dancer2::Core::Types, Data::Dumper, Encode, Moo::Role, POSIX
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/Role/SessionFactory.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.137)
- **Top Global Matches:** file_cluster_15: 6.137, file_cluster_11: 7.02, file_cluster_10: 8.005
- **Magnitude:** 112.14 | **LOC:** 497 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.3%), Mutation Surface (formerly State Flux) (68.1%), Guard Balance (formerly Safety Score) (46.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cookie` **(Defensive Guards)** (Impact: 11.7)
  * `retrieve` **(Defensive Guards)** (Impact: 10.0)
  * `change_id` **(Defensive Guards)** (Impact: 7.7)
    * *Intent:* # XXX eventually we could perhaps require '_change_id'?
  * `generate_id` **(Compute Cores)** (Impact: 7.2)
    * *Intent:* # prepend epoch seconds so session ID is roughly monotonic
  * `create` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 105`, `args: 10`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `state_mutation: 9`, `planned_debt: 1`, `fragile_debt: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 12`, `import: 12`
* *Defense:* `safety: 25`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Carp, Dancer2::Core::Session, Dancer2::Core::Types, Digest::SHA, List::Util, MIME::Base64, Module::Runtime, Moo::Role...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/Response.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.331)
- **Top Global Matches:** file_cluster_15: 5.331, file_cluster_10: 6.929, file_cluster_16: 7.832
- **Magnitude:** 109.22 | **LOC:** 426 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 6.907; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.9%), Guard Balance (formerly Safety Score) (48.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_content` **(Compute Cores)** (Impact: 24.5)
  * `to_psgi` **(Compute Cores)** (Impact: 8.4)
  * `headers_to_array` **(Parameter Forwarders)** (Impact: 7.4)
  * `content_type` **(Parameter Forwarders)** (Impact: 5.8)
    * *Intent:* # sugar for accessing the content_type header, with mimetype care
  * `redirect` **(Parameter Forwarders)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 114`, `args: 27`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 2`
* *Architecture:* `api: 13`, `import: 20`
* *Defense:* `safety: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.907
  * `Choke Point (Betweenness):` 0.00033 | `Ripple Effect (Closeness):` 0.128887
  * `Imports (Out-Degree: 4):` Carp, Dancer2, Dancer2::Core::HTTP, Dancer2::Core::MIME, Dancer2::Core::Types, Encode, HTTP::Headers::Fast, Moo...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Serializer/JSON.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.088)
- **Top Global Matches:** file_cluster_15: 5.088, file_cluster_11: 6.396, file_cluster_10: 7.812
- **Magnitude:** 100.88 | **LOC:** 217 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **6**; blast radius 2.6; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serialize` **(Compute Cores)** (Impact: 12.8)
    * *Intent:* # class definition
  * `_ensure_characters` **(Type Conversions)** (Impact: 10.6)
  * `_ensure_scalar` **(Compute Cores)** (Impact: 8.5)
  * `_invalid_utf8` **(Compute Cores)** (Impact: 5.8)
  * `deserialize` **(Parameter Forwarders)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 28`, `structural_boundaries: 59`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 7`, `import: 6`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.6
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.008451
  * `Imports (Out-Degree: 0):` Encode, JSON::MaybeXS, Moo, Ref::Util, Scalar::Util, Unicode::UTF8
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.528)
- **Top Global Matches:** file_cluster_1: 6.528, file_cluster_3: 48.353, file_cluster_8: 70.144
- **Magnitude:** 99.78 | **LOC:** 274 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (27.9%), Connectivity (formerly Api Exposure) (14.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_test` **(I/O & Config Routines)** (Impact: 61.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 39`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 15`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 2`, `test: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Dancer2::Core::App, Dancer2::Core::Request, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/Core/Runner.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.415)
- **Top Global Matches:** file_cluster_15: 6.415, file_cluster_10: 8.258, file_cluster_16: 8.441
- **Magnitude:** 96.5 | **LOC:** 249 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 45.931; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.8%), Debt Markers (formerly Tech Debt) (32.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `psgi_app` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `_build_config` **(Compute Cores)** (Impact: 13.7)
  * `print_banner` **(Compute Cores)** (Impact: 8.2)
  * `BUILD` **(Compute Cores)** (Impact: 6.4)
  * `_build_server` **(Compute Cores)** (Impact: 3.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 56`, `args: 14`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 11`, `unreferenced_by_name: 3`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 45.931
  * `Choke Point (Betweenness):` 0.004544 | `Ripple Effect (Closeness):` 0.232684
  * `Imports (Out-Degree: 4):` Carp, Dancer2::Core::Dispatcher, Dancer2::Core::MIME, Dancer2::Core::Types, Module::Runtime, Moo, Plack::Builder, Ref::Util...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/Dancer2/Core/Time.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.022)
- **Top Global Matches:** file_cluster_6: 8.022, file_cluster_8: 13.095, file_cluster_4: 13.836
- **Magnitude:** 87.22 | **LOC:** 177 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **1**; blast radius 7.22; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.4%), Complexity Load (formerly Cognitive Load) (40.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_parse_duration` **(Compute Cores)** (Impact: 41.6)
    * *Intent:* #>>> # This code is taken from Time::Duration::Parse, except if it isn't # understood it just passes...
  * `_build_gmt_string` **(Compute Cores)** (Impact: 6.5)
  * `_build_epoch` **(Compute Cores)** (Impact: 4.5)
  * `BUILDARGS` **(Parameter Forwarders)** (Impact: 3.9)
  * `_build_seconds` **(Parameter Forwarders)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 34`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 8`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 1`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.22
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.134977
  * `Imports (Out-Degree: 0):` Moo
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/Dancer2.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.514)
- **Top Global Matches:** file_cluster_6: 7.514, file_cluster_8: 12.902, file_cluster_4: 13.498
- **Magnitude:** 80.98 | **LOC:** 434 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **160** in-repo importer(s); it depends on **8**; blast radius 156.535; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (61.6%), Connectivity (formerly Api Exposure) (59.0%), Guard Balance (formerly Safety Score) (53.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import` **(Compute Cores)** (Impact: 34.8)
  * `_set_import_method_to_caller` **(Parameter Forwarders)** (Impact: 5.0)
  * `VERSION` **(Compute Cores)** (Impact: 2.9)
  * `psgi_app` **(Parameter Forwarders)** (Impact: 1.5)
  * `runner` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 46`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 8`
* *Architecture:* `api: 5`, `import: 13`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 156.535
  * `Choke Point (Betweenness):` 0.026059 | `Ripple Effect (Closeness):` 0.431962
  * `Imports (Out-Degree: 3):` Dancer2::Core, Dancer2::Core::App, Dancer2::Core::Runner, Import::Into, List::Util, Module::Runtime, strict, warnings
  * `Imported By (In-Degree: 160):` (Excluded from Brief to save tokens)

### `t/dsl/uri_for_route.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.891)
- **Top Global Matches:** file_cluster_9: 6.891, file_cluster_16: 12.782, file_cluster_10: 12.809
- **Magnitude:** 80.5 | **LOC:** 247 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (51.4%), Complexity Load (formerly Cognitive Load) (30.8%), Connectivity (formerly Api Exposure) (6.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_app` **(Many-Argument Workhorses)** (Impact: 29.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 45`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `api: 5`, `import: 8`
* *Defense:* `safety: 6`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Dancer2, HTTP::Request::Common, JSON::MaybeXS, Plack::Builder, Plack::Test, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/request_upload.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.59)
- **Top Global Matches:** file_cluster_3: 9.59, file_cluster_8: 21.571, file_cluster_6: 33.98
- **Magnitude:** 65.64 | **LOC:** 210 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.6%), Guard Balance (formerly Safety Score) (54.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.1%), Complexity Load (formerly Cognitive Load) (22.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_test` **(I/O & Config Routines)** (Impact: 39.4)
  * `test_path` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 43`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 2`, `import: 13`
* *Defense:* `safety: 3`, `test: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Carp, Dancer2::Core::Request, Encode, File::Temp, Path::Tiny, Test::Fatal, Test::More, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/Dancer2/ConfigReader/Config/Any.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.082)
- **Top Global Matches:** file_cluster_8: 9.082, file_cluster_6: 10.726, file_cluster_4: 18.489
- **Magnitude:** 63.18 | **LOC:** 236 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 3.273; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (73.6%), Guard Balance (formerly Safety Score) (48.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.7%), Complexity Load (formerly Cognitive Load) (13.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_build_config_files_path` **(Compute Cores)** (Impact: 30.5)
  * `_load_config_file` **(Defensive Guards)** (Impact: 11.2)
  * `read_config` **(Parameter Forwarders)** (Impact: 3.4)
  * `_build_config_files` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 64`, `args: 6`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 1`, `import: 12`
* *Defense:* `safety: 9`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.273
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.130865
  * `Imports (Out-Degree: 3):` Carp, Config::Any, Dancer2::Core, Dancer2::Core::Factory, Dancer2::Core::Types, Hash::Merge::Simple, Module::Runtime, Moo...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `lib/Dancer2/Logger/File.pm` (PERL) | Magnitude: 24.92 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 36, core_var_decl: 35, design_snake_case: 35
- `lib/Dancer2/Serializer/YAML.pm` (PERL) | Magnitude: 8.74 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 20, indent_spaces: 8, closures: 5, import: 5
- `t/roles/hook.t` (PERL) | Magnitude: 10.3 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 20, closures: 6, import: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `lib/Dancer2/Manual/Cookbook.pod` (PERL) | Magnitude: 3291.6 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 363, branch: 203, structural_boundaries: 183, decorators: 66

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `t/issues/gh-634.t` (PERL) | Magnitude: 4.74 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 27, core_var_decl: 17, design_snake_case: 15
- `lib/Dancer2/Core/Role/HasLocation.pm` (PERL) | Magnitude: 27.94 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 23, core_var_decl: 14, design_snake_case: 14
- `tools/perf.pl` (PERL) | Magnitude: 0.03 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 32, branch: 17, core_var_decl: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `t/plugin2/no-config.t` (PERL) | Magnitude: 15.48 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, core_var_decl: 7, design_snake_case: 7
- `t/shared_engines.t` (PERL) | Magnitude: 16.78 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 19, import: 9, test: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tools/cookie_perf.pl` (PERL) | Magnitude: 0.06 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 123, core_var_decl: 41, design_snake_case: 41, structural_boundaries: 39

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/Dancer2/Manual.pod` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 19101.96
- `lib/Dancer2/Manual/Cookbook.pod` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 3291.6
- `lib/Dancer2/Manual/Extending.pod` -> **Jason A. Crome** (100.0% isolated ownership) | Magnitude: 2092.6
- `lib/Dancer2/Core/App.pm` -> **Sawyer X** (85.0% isolated ownership) | Magnitude: 843.22
- `lib/Dancer2/Core/Request.pm` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 480.54

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/Dancer2/Core/App.pm` -> **Severity: 1.778** (Bridge: 0.0185 * Flux: 95.8385%)
- `lib/Dancer2.pm` -> **Severity: 1.606** (Bridge: 0.0261 * Flux: 61.639%)
- `lib/Dancer2/Core/Runner.pm` -> **Severity: 0.433** (Bridge: 0.0045 * Flux: 95.3103%)
- `lib/Dancer2/ConfigReader.pm` -> **Severity: 0.21** (Bridge: 0.0029 * Flux: 72.2726%)
- `lib/Dancer2/Core/Error.pm` -> **Severity: 0.172** (Bridge: 0.0018 * Flux: 98.1435%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/Dancer2.pm` -> **Severity: 23.048** (Embedded: 0.432 * Error Risk: 53.3565%)
- `lib/Dancer2/Core/App.pm` -> **Severity: 13.28** (Embedded: 0.2451 * Error Risk: 54.1808%)
- `lib/Dancer2/Core.pm` -> **Severity: 13.155** (Embedded: 0.2669 * Error Risk: 49.2858%)
- `lib/Dancer2/Core/Runner.pm` -> **Severity: 12.063** (Embedded: 0.2327 * Error Risk: 51.8413%)
- `lib/Dancer2/Core/Request.pm` -> **Severity: 9.78** (Embedded: 0.1745 * Error Risk: 56.0431%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/Dancer2.pm` -> **Severity: 15653.5** (Blast Radius: 156.535 * Doc Risk: 100.0%)
- `lib/Dancer2/Core.pm` -> **Severity: 6216.4** (Blast Radius: 62.164 * Doc Risk: 100.0%)
- `lib/Dancer2/Core/App.pm` -> **Severity: 4933.2** (Blast Radius: 49.332 * Doc Risk: 100.0%)
- `lib/Dancer2/Core/Runner.pm` -> **Severity: 4593.1** (Blast Radius: 45.931 * Doc Risk: 100.0%)
- `lib/Dancer2/Plugin.pm` -> **Severity: 3141.1** (Blast Radius: 31.411 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2437 call pairs -- scoped 3.8%, unique 0.0%, ambiguous 9.9%, external 86.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 2437 | 3.8% | 0.0% | 9.9% | 86.3% |

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
