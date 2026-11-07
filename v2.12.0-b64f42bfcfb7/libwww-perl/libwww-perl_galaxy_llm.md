# ARCHITECTURAL_BRIEF: libwww-perl
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/libwww-perl/libwww-perl.git` |
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
- **Scope:** 87 analyzed artifact(s), 8990 LOC.
- **Load-bearing artifact:** `lib/LWP/UserAgent.pm` -- 40 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `lib/LWP/UserAgent.pm` -- pulls in 22 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `lib/LWP/UserAgent.pm` at magnitude 5881.44 (structural weight, not risk).
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
| Total Artifacts | 100 |
| Analyzed Artifacts (Scanned) | 87 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 13 |
| Total LOC | 8990 |
| Volatility Index | 0.034 |
| % Scanned of codebase = | 87.0% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.341 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5511 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.8298 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 77 | 8764 | 88.5% |
| YAML | 4 | 218 | 4.6% |
| MARKDOWN | 3 | 0 | 3.4% |
| SHELL | 2 | 8 | 2.3% |
| PLAINTEXT | 1 | 0 | 1.1% |

## 4.1 SOURCE ENCODINGS
All 87 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 46%, Data / Markup / Trivial 14%, Many-Argument Workhorses Files 14%, Parameter Forwarders Files 10%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 83 | 95.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 4.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 13*

**Composition by Extension & Reason:**
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.pm`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (Static Asset Blob without Intent: 1050 LOC)
- `.ssl`: 1x Excluded (Unsupported Extension: '.SSL')
- `.ini`: 1x Excluded (Unsupported Extension: '.ini')
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.pl_dist`: 1x Excluded (Unsupported Extension: '.pl_dist')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.8 | 29.3 | 15.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 70.8 | 37.0 | 49.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.9 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 11.6 | 2.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 53.1 | 50.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 52.6 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.8 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 16.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.4 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 211 | 36 | 4 | `lib/LWP/UserAgent.pm` |
| cleanup | 31 | 16 | 1 | `lib/LWP/UserAgent.pm` |
| guards | 204 | 75 | 2 | `lib/LWP/UserAgent.pm` |
| danger | 205 | 33 | 9 | `lib/LWP/UserAgent.pm` |
| concurrency | 8 | 5 | 0 | `lib/LWP/RobotUA.pm` |
| connectivity | 188 | 38 | 7 | `lib/LWP/UserAgent.pm` |
| io | 424 | 66 | 10 | `lib/LWP/UserAgent.pm` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 4 | 0 | `bin/lwp-request` |
| time | 48 | 18 | 2 | `lib/LWP/UserAgent.pm` |
| serialization | 0 | 0 | 0 | - |
| regex | 244 | 39 | 6 | `lib/LWP/UserAgent.pm` |
| events | 16 | 6 | 0 | `lib/LWP/UserAgent.pm` |
| tests | 367 | 40 | 9 | `t/local/http.t` |
| docs | 27 | 17 | 1 | `.github/workflows/dzil-build-and-test.yml` |
| debt | 191 | 35 | 6 | `t/local/http.t` |
| mutation | 907 | 72 | 30 | `lib/LWP/UserAgent.pm` |
| dead_code | 36 | 24 | 1 | `t/local/httpsub.t` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 19 | 9 | 0 | `bin/lwp-download` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `lib/LWP/UserAgent.pm` (Hits: 88)
- `lib/LWP/Protocol/http.pm` (Hits: 35)
- `lwptut.pod` (Hits: 25)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **UserAgent.pm** (`lib/LWP/UserAgent.pm`) — 40 inbound connections
2. **LWP.pm** (`lib/LWP.pm`) — 4 inbound connections
3. **Simple.pm** (`lib/LWP/Simple.pm`) — 4 inbound connections
4. **Protocol.pm** (`lib/LWP/Protocol.pm`) — 3 inbound connections
5. **RobotUA.pm** (`lib/LWP/RobotUA.pm`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **UserAgent.pm** (`lib/LWP/UserAgent.pm`) — 22 outbound dependencies
2. **lwp-request** (`bin/lwp-request`) — 16 outbound dependencies
3. **http.t** (`t/local/http.t`) — 13 outbound dependencies
4. **lwp-download** (`bin/lwp-download`) — 12 outbound dependencies
5. **ua.t** (`t/robot/ua.t`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/UserAgent.pm`) -> Impact: **4699.8** | LOC: 1646
- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/Protocol/http.pm`) -> Impact: **474.6** | LOC: 373
- `daemonize` **(Many-Argument Workhorses)** (@ `t/local/http.t`) -> Impact: **371.5** | LOC: 213
- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/Protocol/ftp.pm`) -> Impact: **230.4** | LOC: 322
- `_test` **(Annotated & Test Methods)** (@ `t/local/http.t`) -> Impact: **177.6** | LOC: 431
- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/Protocol/mailto.pm`) -> Impact: **127.5** | LOC: 150
- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/Protocol/nntp.pm`) -> Impact: **109.8** | LOC: 133
- `new` **(Many-Argument Workhorses)** (@ `lib/LWP/UserAgent.pm`) -> Impact: **94.7** | LOC: 127
- `request` **(Many-Argument Workhorses)** (@ `lib/LWP/Protocol/gopher.pm`) -> Impact: **90.8** | LOC: 123
- `authenticate` **(Many-Argument Workhorses)** (@ `lib/LWP/Authen/Ntlm.pm`) -> Impact: **76.0** | LOC: 80

*Function archetypes referenced above:*
  * **Annotated & Test Methods**: n/a
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `lib/LWP` | 8 | 6514.62 | 40.95% | 15.73% |
| `lib/LWP/Protocol` | 10 | 1792.44 | 49.33% | 34.56% |
| `t/local` | 8 | 895.04 | 25.9% | 17.22% |
| `__monolith__` | 9 | 314.4 | 17.88% | 2.89% |
| `lib/LWP/Authen` | 3 | 298.9 | 55.55% | 19.36% |
| `bin` | 4 | 277.88 | 38.72% | 2.36% |
| `t/base` | 7 | 226.68 | 39.19% | 0.0% |
| `t/robot` | 2 | 218.28 | 66.96% | 0.0% |
| `xt/author/live/jigsaw` | 9 | 156.4 | 16.99% | 8.39% |
| `xt/author/net` | 7 | 131.28 | 16.46% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/local/httpsub.t` -> **99.9788%** Exposure
- `lib/LWP/Protocol/file.pm` -> **74.4868%** Exposure
- `lib/LWP/Protocol.pm` -> **49.7407%** Exposure
- `lib/LWP/Protocol/gopher.pm` -> **47.985%** Exposure
- `lib/LWP/Protocol/data.pm` -> **37.7541%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `lib/LWP/Authen/Digest.pm` -> **100.0%** Exposure
- `t/base/ua.t` -> **100.0%** Exposure
- `lib/LWP/Protocol/http.pm` -> **99.9999%** Exposure
- `lib/LWP/Protocol/nntp.pm` -> **99.9992%** Exposure
- `lwpcook.pod` -> **99.997%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/local/httpsub.t` -> **8** Orphaned Functions | **0** Duplicates
- `lib/LWP/Protocol/http.pm` -> **2** Orphaned Functions | **0** Duplicates
- `bin/lwp-request` -> **1** Orphaned Functions | **0** Duplicates
- `lib/LWP/Authen/Basic.pm` -> **1** Orphaned Functions | **0** Duplicates
- `lib/LWP/Authen/Digest.pm` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `449` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `lib/LWP/UserAgent.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.709)
- **Top Global Matches:** file_cluster_6: 7.709, file_cluster_4: 8.474, file_cluster_15: 15.736
- **Magnitude:** 5881.44 | **LOC:** 2257 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **40** in-repo importer(s); it depends on **22**; blast radius 254.626; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (81.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 4699.8)
  * `new` **(Many-Argument Workhorses)** (Impact: 94.7)
  * `send_request` **(Many-Argument Workhorses)** (Impact: 58.5)
  * `_process_colonic_headers` **(Defensive Guards)** (Impact: 52.5)
  * `mirror` **(Many-Argument Workhorses)** (Impact: 43.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 131 instances
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 550`, `structural_boundaries: 631`, `args: 75`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 132`, `planned_debt: 2`, `fragile_debt: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 88`, `api: 48`, `import: 70`
* *Defense:* `safety: 44`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 254.626
  * `Choke Point (Betweenness):` 0.023666 | `Ripple Effect (Closeness):` 0.47093
  * `Imports (Out-Degree: 4):` Carp, Encode, Encode::Locale, File::Copy, File::Temp, HTML::HeadParser, HTTP::Config, HTTP::Date...
  * `Imported By (In-Degree: 40):` (Excluded from Brief to save tokens)

### `t/local/http.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.274)
- **Top Global Matches:** file_cluster_8: 9.274, file_cluster_6: 14.45, file_cluster_4: 22.241
- **Magnitude:** 740.68 | **LOC:** 749 | **CtrlFlow:** 38.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (82.7%), Guard Balance (formerly Safety Score) (55.3%), Connectivity (formerly Api Exposure) (7.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 371.5)
  * `_test` **(Annotated & Test Methods)** (Impact: 177.6)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
  * `get_basic_credentials` **(Parameter Forwarders)** (Impact: 7.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 11
* *State Mutation (weighted view):* 143
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 164`, `args: 21`, `func_start: 7`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 53`
* *Architecture:* `io: 11`, `api: 10`, `import: 16`
* *Defense:* `safety: 2`, `test: 94`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, FindBin, HTTP::Cookies, HTTP::Daemon, HTTP::Request, LWP::UserAgent, Test::Fatal, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol/http.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.195)
- **Top Global Matches:** file_cluster_4: 7.195, file_cluster_6: 10.938, file_cluster_15: 12.055
- **Magnitude:** 735.2 | **LOC:** 522 | **CtrlFlow:** 44.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (97.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 474.6)
  * `_new_socket` **(Many-Argument Workhorses)** (Impact: 31.1)
  * `_fixup_header` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `hlist_remove` **(Compute Cores)** (Impact: 7.3)
  * `_get_sock_info` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 55 instances
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 166
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 121`, `args: 9`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `state_mutation: 56`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 35`, `api: 8`, `import: 11`
* *Defense:* `safety: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Response, HTTP::Status, Net::HTTP, URI::Escape, bytes, content, parent, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol/ftp.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.274)
- **Top Global Matches:** file_cluster_4: 7.274, file_cluster_6: 7.429, file_cluster_15: 14.022
- **Magnitude:** 401.72 | **LOC:** 556 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 230.4)
  * `_connect` **(Many-Argument Workhorses)** (Impact: 42.1)
  * `new` **(Compute Cores)** (Impact: 9.3)
  * `home` **(Parameter Forwarders)** (Impact: 3.9)
  * `http_server` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 121`, `args: 9`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 32`, `dead_code: 1`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 5`, `api: 9`, `import: 10`
* *Defense:* `safety: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, File::Listing, HTTP::Negotiate, HTTP::Response, HTTP::Status, LWP::MediaTypes, parent, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.734)
- **Top Global Matches:** file_cluster_4: 7.734, file_cluster_6: 8.169, file_cluster_15: 14.296
- **Magnitude:** 187.42 | **LOC:** 327 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 64.464; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `collect` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `implementor` **(Compute Cores)** (Impact: 21.2)
  * `collect_once` **(Callbacks & Closures)** (Impact: 4.5)
  * `request` **(Defensive Guards)** (Impact: 2.9)
  * `new` **(Type Conversions)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 96`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `fragile_debt: 4`
* *Architecture:* `io: 3`, `api: 10`, `import: 12`
* *Defense:* `safety: 8`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 64.464
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.261752
  * `Imports (Out-Degree: 0):` Carp, HTTP::Response, HTTP::Status, Scalar::Util, Try::Tiny, parent, strict
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `lib/LWP/ConnCache.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.201)
- **Top Global Matches:** file_cluster_15: 6.201, file_cluster_10: 7.975, file_cluster_16: 8.183
- **Magnitude:** 178.66 | **LOC:** 351 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 62.086; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `enforce_limits` **(Compute Cores)** (Impact: 25.4)
  * `drop` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `withdraw` **(Compute Cores)** (Impact: 10.6)
  * `new` **(Compute Cores)** (Impact: 9.4)
  * `get_connections` **(Compute Cores)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 91`, `args: 16`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* `io: 4`, `api: 11`, `import: 6`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.086
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.258996
  * `Imports (Out-Degree: 0):` Carp, strict
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `lib/LWP/Protocol/gopher.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.159)
- **Top Global Matches:** file_cluster_8: 8.159, file_cluster_6: 18.324, file_cluster_3: 19.959
- **Magnitude:** 172.9 | **LOC:** 214 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.2%), Complexity Load (formerly Cognitive Load) (58.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 90.8)
  * `gopher2url` **(Compute Cores)** (Impact: 23.3)
  * `menu2html` **(Compute Cores)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 53`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 14`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 20`, `api: 4`, `import: 6`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Response, HTTP::Status, IO::Select, IO::Socket, parent, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol/mailto.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.537)
- **Top Global Matches:** file_cluster_1: 4.537, file_cluster_3: 48.132, file_cluster_8: 70.003
- **Magnitude:** 171.68 | **LOC:** 185 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%), Complexity Load (formerly Cognitive Load) (57.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 127.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 44`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 7`
* *Defense:* `safety: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, HTTP::Request, HTTP::Response, HTTP::Status, Mail::Internet, parent, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol/nntp.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.791)
- **Top Global Matches:** file_cluster_1: 4.791, file_cluster_3: 48.159, file_cluster_8: 70.02
- **Magnitude:** 149.84 | **LOC:** 151 | **CtrlFlow:** 37.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (63.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 109.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 44`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* `io: 1`, `api: 2`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTTP::Response, HTTP::Status, Net::NNTP, parent, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-request` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_9: 6.526, file_cluster_15: 10.392, file_cluster_16: 10.855
- **Magnitude:** 149.64 | **LOC:** 566 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (61.6%), Complexity Load (formerly Cognitive Load) (54.7%), Debt Markers (formerly Tech Debt) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_basic_credentials` **(Compute Cores)** (Impact: 19.1)
  * `show` **(Compute Cores)** (Impact: 12.5)
  * `usage` **(I/O & Config Routines)** (Impact: 10.4)
  * `new` **(Interface Declarations)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 31`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 5`, `import: 23`
* *Defense:* `safety: 6`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Encode, Encode::Locale, Getopt::Long, HTML::FormatPS, HTML::FormatText, HTML::Parse, HTTP::Date, HTTP::Status...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/RobotUA.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.022)
- **Top Global Matches:** file_cluster_15: 6.022, file_cluster_9: 8.249, file_cluster_16: 8.31
- **Magnitude:** 148.34 | **LOC:** 313 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 19.871; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (54.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simple_request` **(Many-Argument Workhorses)** (Impact: 27.7)
  * `new` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* # # Additional attributes in addition to those found in LWP::UserAgent: # # $self->{'delay'} Require...
  * `host_wait` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* *host_count = \&no_visits; # backwards compatibility with LWP-5.02
  * `as_string` **(Type Conversions)** (Impact: 7.6)
  * `no_visits` **(Parameter Forwarders)** (Impact: 3.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 83`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `unreferenced_by_name: 1`
* *Architecture:* `io: 9`, `api: 10`, `import: 10`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.871
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.034884
  * `Imports (Out-Degree: 0):` Carp, HTTP::Date, HTTP::Request, HTTP::Response, HTTP::Status, WWW::RobotRules, parent, strict
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `t/robot/ua-get.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 16.753)
- **Top Global Matches:** file_cluster_3: 16.753, file_cluster_1: 34.299, file_cluster_8: 37.325
- **Magnitude:** 117.26 | **LOC:** 149 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (71.9%), Guard Balance (formerly Safety Score) (63.2%), Connectivity (formerly Api Exposure) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `_test` **(Annotated & Test Methods)** (Impact: 36.0)
  * `url` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 45`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 2`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, FindBin, HTTP::Daemon, LWP::RobotUA, Test::More, URI, strict, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/lwp-download` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.392)
- **Top Global Matches:** file_cluster_15: 7.392, file_cluster_2: 7.917, file_cluster_10: 8.515
- **Magnitude:** 107.98 | **LOC:** 336 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (67.7%), Complexity Load (formerly Cognitive Load) (65.8%), Connectivity (formerly Api Exposure) (4.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fduration` **(Type Conversions)** (Impact: 6.6)
  * `fbytes` **(Type Conversions)** (Impact: 6.3)
  * `show` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 69`, `args: 5`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 27`
* *Architecture:* `io: 9`, `api: 3`, `import: 14`
* *Defense:* `safety: 2`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Encode, Encode::Locale, Fcntl, File::Spec, Getopt::Long, HTTP::Date, LWP::MediaTypes, LWP::UserAgent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Authen/Ntlm.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.737)
- **Top Global Matches:** file_cluster_1: 4.737, file_cluster_3: 48.15, file_cluster_8: 70.013
- **Magnitude:** 106.5 | **LOC:** 184 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `authenticate` **(Many-Argument Workhorses)** (Impact: 76.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 37`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `io: 6`, `api: 1`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Authen::NTLM, MIME::Base64, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwptut.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.117)
- **Top Global Matches:** file_cluster_2: 5.117, file_cluster_13: 5.689, file_cluster_17: 6.517
- **Magnitude:** 105.42 | **LOC:** 821 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.7%), Guard Balance (formerly Safety Score) (55.9%), Complexity Load (formerly Cognitive Load) (46.6%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 89`, `class_start: 1`
* *Risk/State:* `state_mutation: 28`
* *Architecture:* `io: 25`, `import: 31`
* *Defense:* `safety: 8`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/robot/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 16.55)
- **Top Global Matches:** file_cluster_3: 16.55, file_cluster_1: 34.2, file_cluster_8: 37.229
- **Magnitude:** 101.02 | **LOC:** 146 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (64.0%), Complexity Load (formerly Cognitive Load) (62.1%), Connectivity (formerly Api Exposure) (4.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `daemonize` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `_test` **(Annotated & Test Methods)** (Impact: 19.8)
  * `url` **(Interface Declarations)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 48`, `args: 3`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 11`
* *Architecture:* `io: 2`, `api: 2`, `import: 10`
* *Defense:* `safety: 2`, `test: 11`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Config, FindBin, HTTP::Daemon, HTTP::Request, LWP::RobotUA, Test::More, URI, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/base/ua.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.503)
- **Top Global Matches:** file_cluster_13: 7.503, file_cluster_10: 8.003, file_cluster_2: 8.075
- **Magnitude:** 98.2 | **LOC:** 207 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 5.597; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.1%), Guard Balance (formerly Safety Score) (56.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 35`, `args: 1`
* *Risk/State:* `state_mutation: 40`
* *Architecture:* `io: 22`, `import: 6`
* *Defense:* `safety: 2`, `test: 54`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` HTTP::Request, LWP::UserAgent, Test::More, strict, undef, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.533)
- **Top Global Matches:** file_cluster_2: 3.533, file_cluster_13: 5.223, file_cluster_17: 5.399
- **Magnitude:** 96.96 | **LOC:** 670 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **1**; blast radius 71.601; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Guard Balance (formerly Safety Score) (57.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (29.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 41`, `class_start: 1`
* *Risk/State:* `state_mutation: 31`, `planned_debt: 4`
* *Architecture:* `io: 17`, `import: 7`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 71.601
  * `Choke Point (Betweenness):` 0.001368 | `Ripple Effect (Closeness):` 0.267574
  * `Imports (Out-Degree: 1):` LWP::UserAgent
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `lib/LWP/Authen/Basic.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.989)
- **Top Global Matches:** file_cluster_8: 8.989, file_cluster_6: 10.384, file_cluster_4: 18.092
- **Magnitude:** 96.52 | **LOC:** 87 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `authenticate` **(Many-Argument Workhorses)** (Impact: 65.0)
  * `auth_header` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `add_path` **(Parameter Forwarders)** (Impact: 2.0)
  * `_reauth_requested` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 40`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Encode, MIME::Base64, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Authen/Digest.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.857)
- **Top Global Matches:** file_cluster_3: 6.857, file_cluster_8: 20.631, file_cluster_6: 33.492
- **Magnitude:** 95.88 | **LOC:** 81 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.2%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `auth_header` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `_reauth_requested` **(Many-Argument Workhorses)** (Impact: 7.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 29`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 3`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Digest::MD5, parent, strict
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Protocol/file.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.198)
- **Top Global Matches:** file_cluster_1: 5.198, file_cluster_3: 48.19, file_cluster_8: 70.036
- **Magnitude:** 89.8 | **LOC:** 148 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (74.5%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `request` **(Many-Argument Workhorses)** (Impact: 67.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 51`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 6`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 10`, `api: 2`, `import: 9`
* *Defense:* `safety: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HTML::Entities, HTTP::Date, HTTP::Request, HTTP::Response, HTTP::Status, LWP::MediaTypes, URI::Escape, parent...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lwpcook.pod` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.699)
- **Top Global Matches:** file_cluster_2: 5.699, file_cluster_13: 5.826, file_cluster_17: 6.952
- **Magnitude:** 85.12 | **LOC:** 311 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (77.0%), Guard Balance (formerly Safety Score) (63.3%), Debt Markers (formerly Tech Debt) (26.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 41`, `args: 1`
* *Risk/State:* `state_mutation: 22`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 21`, `import: 27`
* *Defense:* `safety: 2`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Debug.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.755)
- **Top Global Matches:** file_cluster_11: 6.755, file_cluster_15: 7.234, file_cluster_10: 7.949
- **Magnitude:** 53.56 | **LOC:** 113 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.597; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (59.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Complexity Load (formerly Cognitive Load) (44.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `level` **(I/O & Config Routines)** (Impact: 6.8)
  * `import` **(Compute Cores)** (Impact: 6.5)
  * `_log` **(Compute Cores)** (Impact: 4.6)
  * `trace` **(Interface Declarations)** (Impact: 2.0)
  * `debug` **(Interface Declarations)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 33`, `args: 4`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 7`, `import: 7`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Exporter
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Centroid distance: N/A)
- **Magnitude:** 49.36 | **LOC:** 2468 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 5.597
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/LWP/Simple.pm` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.368)
- **Top Global Matches:** file_cluster_15: 5.368, file_cluster_10: 6.831, file_cluster_13: 7.518
- **Magnitude:** 44.72 | **LOC:** 271 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **5**; blast radius 19.871; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.0%), Mutation Surface (formerly State Flux) (41.1%), Complexity Load (formerly Cognitive Load) (14.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getprint` **(Callbacks & Closures)** (Impact: 7.8)
  * `head` **(Compute Cores)** (Impact: 5.1)
  * `get` **(Parameter Forwarders)** (Impact: 3.1)
  * `getstore` **(Parameter Forwarders)** (Impact: 2.1)
  * `mirror` **(Parameter Forwarders)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 60`, `args: 12`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 9`, `api: 9`, `import: 11`
* *Defense:* `safety: 1`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.871
  * `Choke Point (Betweenness):` 0.001642 | `Ripple Effect (Closeness):` 0.046512
  * `Imports (Out-Degree: 1):` Exporter, HTTP::Date, HTTP::Status, LWP::UserAgent, strict
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `t/local/httpsub.t` (PERL) | Magnitude: 33.56 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 47, api: 13, func_start: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `lib/LWP/Protocol/loopback.pm` (PERL) | Magnitude: 8.34 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 8, import: 3, api: 2

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `lib/LWP/UserAgent.pm` -> Churn: **100.0%** | Cog Load: 80.9811% | Debt: 12.7254%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `lib/LWP/Protocol/http.pm` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 735.2
- `lib/LWP/Protocol/ftp.pm` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 401.72
- `lib/LWP/Protocol.pm` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 187.42
- `lib/LWP/ConnCache.pm` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 178.66
- `lib/LWP/Protocol/gopher.pm` -> **Olaf Alders** (100.0% isolated ownership) | Magnitude: 172.9

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `lib/LWP/UserAgent.pm` -> **Severity: 2.364** (Bridge: 0.0237 * Flux: 99.898%)
- `lib/LWP.pm` -> **Severity: 0.135** (Bridge: 0.0014 * Flux: 98.3981%)
- `lib/LWP/Simple.pm` -> **Severity: 0.068** (Bridge: 0.0016 * Flux: 41.1157%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `lib/LWP/UserAgent.pm` -> **Severity: 27.736** (Embedded: 0.4709 * Error Risk: 58.8967%)
- `lib/LWP/Protocol.pm` -> **Severity: 15.939** (Embedded: 0.2618 * Error Risk: 60.8953%)
- `lib/LWP/ConnCache.pm` -> **Severity: 15.378** (Embedded: 0.259 * Error Risk: 59.3749%)
- `lib/LWP.pm` -> **Severity: 15.331** (Embedded: 0.2676 * Error Risk: 57.2979%)
- `lib/LWP/Simple.pm` -> **Severity: 2.41** (Embedded: 0.0465 * Error Risk: 51.8048%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `lib/LWP/UserAgent.pm` -> **Severity: 25462.6** (Blast Radius: 254.626 * Doc Risk: 100.0%)
- `lib/LWP/Protocol.pm` -> **Severity: 6446.4** (Blast Radius: 64.464 * Doc Risk: 100.0%)
- `lib/LWP/ConnCache.pm` -> **Severity: 6208.6** (Blast Radius: 62.086 * Doc Risk: 100.0%)
- `lib/LWP/Protocol/nogo.pm` -> **Severity: 5970.7** (Blast Radius: 59.707 * Doc Risk: 100.0%)
- `lib/LWP/RobotUA.pm` -> **Severity: 1987.1** (Blast Radius: 19.871 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 1053 call pairs -- scoped 6.5%, unique 0.0%, ambiguous 4.1%, external 89.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| perl | 1052 | 6.5% | 0.0% | 4.1% | 89.4% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

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
