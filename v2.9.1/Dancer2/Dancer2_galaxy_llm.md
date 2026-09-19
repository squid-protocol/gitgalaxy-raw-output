# ARCHITECTURAL_BRIEF: Dancer2
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/PerlDancer/Dancer2.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 226 analyzed artifact(s), 10832 LOC.
- **Load-bearing artifact:** `t/dsl/content.t` -- 3 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `t/error.t` -- pulls in 17 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `t/request.t` at magnitude 99.78 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 226 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 212 |
| Total LOC | 10832 |
| Volatility Index | 0.004 |
| % Scanned of codebase = | 51.6% |
| Dominant Lang | PERL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.375 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.0 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| PERL | 179 | 10384 | 79.2% |
| YAML | 23 | 100 | 10.2% |
| HTML | 7 | 84 | 3.1% |
| MARKDOWN | 5 | 0 | 2.2% |
| PLAINTEXT | 4 | 0 | 1.8% |
| CSS | 4 | 239 | 1.8% |
| SQLITE | 2 | 14 | 0.9% |
| DOCKERFILE | 1 | 6 | 0.4% |
| JSON | 1 | 5 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo`
> **Architectural Drift Z-Score:** `4.988`
> **Composition Archetype:** `Small Flat Repo` (z +4.99; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 65%, Data / Markup / Trivial 22%, Interface Declarations Files 4%, Parameter Forwarders Files 4%, Large Core Modules 2%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 217 | 96.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9 | 4.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 212*

**Composition by Extension & Reason:**
- `.pm`: 111x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tt`: 25x Excluded (Unsupported Extension: '.tt')
- `.t`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.pod`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.psgi`: 2x Excluded (Unsupported Extension: '.psgi')
- `.fcgi`: 2x Excluded (Unsupported Extension: '.fcgi')
- `.ico`: 2x Excluded (Explicitly Denied Extension: '.ico')
- `.jpg`: 2x Excluded (Explicitly Denied Extension: '.jpg')
- `.db`: 1x Excluded (Unsupported Extension: '.db'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pl`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 2x Excluded (Unsupported Extension: '.rc')
- `.ini`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.skip`: 1x Excluded (Unsupported Extension: '.SKIP')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 45.0 | 5.3 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 78.0 | 16.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 92.4 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 2.3 | 0.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 63.9 | 4.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 33.0 | 0.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 14.6 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.4 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 40.1 | 3.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 97.9 | 0.5 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 178 | 40 | 1 | `t/types.t` |
| cleanup | 3 | 3 | 0 | `t/file_utils.t` |
| guards | 380 | 172 | 3 | `t/dsl/uri_for_route.t` |
| danger | 59 | 27 | 1 | `share/skel/default/public/css/style.css` |
| concurrency | 3 | 1 | 0 | `t/dsl/delayed.t` |
| connectivity | 1173 | 178 | 10 | `t/error.t` |
| io | 26 | 12 | 0 | `t/request_upload.t` |
| crypto | 0 | 0 | 0 | - |
| ipc | 3 | 2 | 0 | `share/docker/Dockerfile` |
| time | 5 | 5 | 0 | `t/cookie.t` |
| serialization | 1 | 1 | 0 | `t/deserialize.t` |
| regex | 227 | 74 | 3 | `t/types.t` |
| events | 15 | 11 | 0 | `t/error.t` |
| tests | 1336 | 167 | 13 | `t/dsl/parameters.t` |
| docs | 12 | 10 | 0 | `share/skel/default/bin/+app.psgi` |
| debt | 30 | 16 | 0 | `t/dsl/delayed.t` |
| mutation | 1299 | 158 | 15 | `t/app.t` |
| dead_code | 16 | 14 | 0 | `t/roles/hook.t` |
| credential | 2 | 2 | 0 | `t/error.t` |
| threat | 35 | 27 | 1 | `t/types.t` |
| ml_ai | 26 | 12 | 0 | `t/issues/gh-634.t` |
| ui | 45 | 11 | 0 | `t/template.t` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `t/request_upload.t` (Hits: 5)
- `share/skel/default/public/404.html` (Hits: 3)
- `share/skel/default/public/500.html` (Hits: 3)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **content.t** (`t/dsl/content.t`) — 3 inbound connections
2. **TestPlugin.pm** (`t/issues/gh-1449/TestPlugin.pm`) — 1 inbound connections
3. **AUTHORS** (`AUTHORS`) — 0 inbound connections
4. **Changes** (`Changes`) — 0 inbound connections
5. **file.txt** (`t/public/file.txt`) — 0 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **error.t** (`t/error.t`) — 17 outbound dependencies
2. **plugin_syntax.t** (`t/plugin_syntax.t`) — 14 outbound dependencies
3. **hooks.t** (`t/hooks.t`) — 13 outbound dependencies
4. **serializer_mutable_custom.t** (`t/serializer_mutable_custom.t`) — 12 outbound dependencies
5. **perf.pl** (`tools/perf.pl`) — 12 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_test` **(I/O & Config Routines)** (@ `t/request.t`) -> Impact: **61.1** | LOC: 242
- `all_tests` **(I/O & Config Routines)** (@ `t/cookie.t`) -> Impact: **46.1** | LOC: 182
- `run_test` **(I/O & Config Routines)** (@ `t/request_upload.t`) -> Impact: **39.4** | LOC: 168
- `test_app` **(Many-Argument Workhorses)** (@ `t/dsl/uri_for_route.t`) -> Impact: **29.7** | LOC: 109
- `dancer_bake` **(Compute Cores)** (@ `tools/cookie_perf.pl`) -> Impact: **10.6** | LOC: 14
- `plack_crush` **(Compute Cores)** (@ `tools/cookie_perf.pl`) -> Impact: **9.1** | LOC: 12
- `check_app` **(Compute Cores)** (@ `tools/perf.pl`) -> Impact: **5.8** | LOC: 12
- `write_file` **(Compute Cores)** (@ `t/file_utils.t`) -> Impact: **5.6** | LOC: 8
- `throw` **(Type Conversions)** (@ `t/error.t`) -> Impact: **5.5** | LOC: 7
- `_normalize` **(Compute Cores)** (@ `t/plugin_syntax.t`) -> Impact: **4.7** | LOC: 10

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `t` | 83 | 1825.5 | 7.57% | 2.64% |
| `t/dsl` | 24 | 520.12 | 6.5% | 5.34% |
| `t/issues` | 19 | 298.64 | 4.44% | 6.26% |
| `t/plugin2` | 13 | 173.88 | 5.79% | 5.62% |
| `t/scope_problems` | 5 | 80.12 | 2.21% | 0.0% |
| `__monolith__` | 7 | 59.94 | 0.0% | 0.0% |
| `share/skel/tutorial/t` | 4 | 58.84 | 2.75% | 0.0% |
| `share/skel/default/public` | 3 | 52.92 | 3.09% | 0.0% |
| `share/skel/tutorial/public` | 3 | 52.92 | 3.09% | 0.0% |
| `t/config/environments` | 4 | 47.8 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `t/roles/hook.t` -> **92.4142%** Exposure
- `t/dsl/extend.t` -> **73.1059%** Exposure
- `t/issues/gh-797.t` -> **73.1059%** Exposure
- `t/plugin2/no-app-munging.t` -> **73.1059%** Exposure
- `t/session_bad_client_cookie.t` -> **67.5966%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `t/forward_test_tcp.t` -> **99.9868%** Exposure
- `t/dsl/uri_for_route.t` -> **99.8409%** Exposure
- `tools/plugins_auto_tests/get_modules_list.pl` -> **99.1837%** Exposure
- `t/hooks.t` -> **97.6326%** Exposure
- `tools/cookie_perf.pl` -> **97.6216%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `t/roles/hook.t` -> **2** Orphaned Functions | **0** Duplicates
- `t/session_bad_client_cookie.t` -> **2** Orphaned Functions | **0** Duplicates
- `t/config_reader.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/extend.t` -> **1** Orphaned Functions | **0** Duplicates
- `t/dsl/send_as.t` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1255` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `t/request.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 99.78 | **LOC:** 274 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Guard Balance (formerly Safety Score) (57.6%), Complexity Load (formerly Cognitive Load) (27.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (8.6%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::Core::App, Dancer2::Core::Request, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/uri_for_route.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 80.5 | **LOC:** 247 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (58.5%), Complexity Load (formerly Cognitive Load) (30.8%), Connectivity (formerly Api Exposure) (6.5%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, JSON::MaybeXS, Plack::Builder, Plack::Test, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/request_upload.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 65.64 | **LOC:** 210 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.6%), Guard Balance (formerly Safety Score) (67.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.6%), Complexity Load (formerly Cognitive Load) (22.7%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Dancer2::Core::Request, Encode, File::Temp, Path::Tiny, Test::Fatal, Test::More, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 61.46 | **LOC:** 352 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 4.359; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.6%), Guard Balance (formerly Safety Score) (54.2%), Connectivity (formerly Api Exposure) (52.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `my_after` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 113`, `args: 8`, `func_start: 1`, `class_start: 9`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 14`, `import: 21`
* *Defense:* `safety: 3`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Capture::Tiny, Dancer2, HTTP::Request::Common, JSON::MaybeXS, Path::Tiny, Plack::Test, Ref::Util, Sub::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/cookie.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 51.56 | **LOC:** 211 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.8%), Connectivity (formerly Api Exposure) (14.7%), Complexity Load (formerly Cognitive Load) (12.4%), Mutation Surface (formerly State Flux) (10.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `all_tests` **(I/O & Config Routines)** (Impact: 46.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 31`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`
* *Architecture:* `api: 1`, `import: 10`
* *Defense:* `safety: 2`, `test: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2::Core::Cookie, Dancer2::Core::Request, Test::Fatal, Test::More, cookie, domain, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Changes` (PLAINTEXT | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 42.0 | **LOC:** 2100 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/forward_test_tcp.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 41.2 | **LOC:** 81 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.9%), Complexity Load (formerly Cognitive Load) (45.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 17
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 21`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Plack::Test, Ref::Util, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/multiapp_template_hooks.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 38.98 | **LOC:** 206 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Guard Balance (formerly Safety Score) (52.7%), Complexity Load (formerly Cognitive Load) (14.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 43`, `args: 6`, `class_start: 2`
* *Risk/State:* `state_mutation: 10`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 2`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Path::Tiny, Plack::Test, Test::More, hooks, routes, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/template.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 37.24 | **LOC:** 221 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.9%), Guard Balance (formerly Safety Score) (47.5%), Mutation Surface (formerly State Flux) (39.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 59`, `args: 5`, `class_start: 4`
* *Risk/State:* `state_mutation: 8`
* *Architecture:* `api: 11`, `import: 13`
* *Defense:* `safety: 3`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Dancer2::Core::Hook, HTTP::Request::Common, Path::Tiny, Plack::Test, Template, Test::More, lib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dispatcher.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 33.98 | **LOC:** 247 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.9%), Guard Balance (formerly Safety Score) (56.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%), Complexity Load (formerly Cognitive Load) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 56`, `args: 5`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `import: 11`
* *Defense:* `safety: 3`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Carp, Dancer2, Dancer2::Core::App, Dancer2::Core::Dispatcher, Dancer2::Core::Hook, Dancer2::Core::Response, Dancer2::Core::Route, Ref::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_lifecycle.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 31.36 | **LOC:** 228 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (32.4%), Guard Balance (formerly Safety Score) (31.7%), Complexity Load (formerly Cognitive Load) (7.8%), Connectivity (formerly Api Exposure) (7.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 67`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `safety: 2`, `test: 33`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Cookies, HTTP::Request::Common, Plack::Test, Test::More, lib, new, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/parameters.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 30.62 | **LOC:** 393 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (7.7%), Complexity Load (formerly Cognitive Load) (5.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 73`, `class_start: 7`
* *Risk/State:* None
* *Architecture:* `api: 9`, `import: 14`
* *Defense:* `safety: 2`, `test: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Encode, HTTP::Request::Common, Plack::Test, Test::More, critic, strict, utf8...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/delayed.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 30.22 | **LOC:** 189 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (33.0%), Debt Markers (formerly Tech Debt) (31.2%), Guard Balance (formerly Safety Score) (28.3%), Mutation Surface (formerly State Flux) (13.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 58`, `args: 2`, `class_start: 6`
* *Risk/State:* `state_mutation: 2`, `planned_debt: 4`
* *Architecture:* `api: 7`, `concurrency: 3`, `import: 13`
* *Defense:* `safety: 3`, `test: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AnyEvent, Dancer2, HTTP::Request::Common, Plack::Test, Test::More, critic, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issues/gh-1564.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 29.92 | **LOC:** 114 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (52.5%), Guard Balance (formerly Safety Score) (41.0%), Complexity Load (formerly Cognitive Load) (11.1%), Connectivity (formerly Api Exposure) (8.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 42`, `args: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `safety: 2`, `test: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Plack::Builder, Plack::Test, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/serializer_mutable.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 29.82 | **LOC:** 118 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Guard Balance (formerly Safety Score) (52.7%), Complexity Load (formerly Cognitive Load) (23.2%), Connectivity (formerly Api Exposure) (4.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 29`, `class_start: 1`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* `api: 2`, `import: 12`
* *Defense:* `safety: 2`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Dancer2::Serializer::Mutable, Encode, HTTP::Request::Common, JSON::MaybeXS, Plack::Test, Ref::Util, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks_no_change_id.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 28.0 | **LOC:** 196 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.5%), Mutation Surface (formerly State Flux) (31.0%), Complexity Load (formerly Cognitive Load) (7.6%), Connectivity (formerly Api Exposure) (6.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 62`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 8`
* *Defense:* `safety: 2`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Cookies, HTTP::Request::Common, Plack::Test, Test::More, lib, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_hooks.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 27.98 | **LOC:** 191 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.5%), Mutation Surface (formerly State Flux) (31.2%), Complexity Load (formerly Cognitive Load) (7.7%), Connectivity (formerly Api Exposure) (6.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 61`, `args: 3`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 4`, `import: 7`
* *Defense:* `safety: 2`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Cookies, HTTP::Request::Common, Plack::Test, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 27.64 | **LOC:** 173 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%), Connectivity (formerly Api Exposure) (9.3%), Complexity Load (formerly Cognitive Load) (6.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (1.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 28`, `args: 1`
* *Risk/State:* None
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 2`, `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Plack::Test, Ref::Util, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/dsl/send_file.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 27.52 | **LOC:** 161 | **CtrlFlow:** 1.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.1%), Connectivity (formerly Api Exposure) (9.4%), Complexity Load (formerly Cognitive Load) (5.0%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 57`, `args: 1`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `io: 1`, `api: 10`, `import: 14`
* *Defense:* `safety: 2`, `test: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Encode, HTTP::Request::Common, Path::Tiny, Plack::Test, Ref::Util, Test::More, streaming...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/error.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 26.66 | **LOC:** 320 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Credential Material (formerly Secrets Risk) (97.9%), Guard Balance (formerly Safety Score) (30.5%), Mutation Surface (formerly State Flux) (14.9%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `throw` **(Type Conversions)** (Impact: 5.5)
  * `MyApp::Censor::censor` **(Interface Declarations)** (Impact: 1.1)
  * `new` **(Type Conversions)** (Impact: 1.1)
  * `as_str` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 106`, `args: 4`, `func_start: 4`, `class_start: 6`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 9`, `import: 21`
* *Defense:* `safety: 5`, `test: 36`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Dancer2::Core::App, Dancer2::Core::Error, Dancer2::Core::Request, Dancer2::Core::Response, HTTP::Request::Common, JSON::MaybeXS, List::Util...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_forward.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25.92 | **LOC:** 196 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (8.3%), Complexity Load (formerly Cognitive Load) (7.5%), Dead Code Surface (formerly Dead Code) (7.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 52`, `class_start: 3`
* *Risk/State:* `dead_code: 1`
* *Architecture:* `api: 8`, `import: 9`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Cookies, HTTP::Request::Common, Plack::Test, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/session_engines.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25.8 | **LOC:** 117 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (45.9%), Mutation Surface (formerly State Flux) (45.6%), Complexity Load (formerly Cognitive Load) (14.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 44`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 2`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Cookies, HTTP::Request::Common, Path::Tiny, Plack::Test, Test::More, YAML, strict...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/deserialize.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25.3 | **LOC:** 229 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (19.3%), Complexity Load (formerly Cognitive Load) (7.5%), Connectivity (formerly Api Exposure) (5.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 66`, `args: 6`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `safety: 2`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, Dancer2::Logger::Capture, Encode, HTTP::Request::Common, JSON::MaybeXS, Module::Runtime, Plack::Test, Test::More...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/redirect.t` (PERL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25.18 | **LOC:** 141 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (8.9%), Complexity Load (formerly Cognitive Load) (6.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 33`, `args: 2`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 8`, `import: 8`
* *Defense:* `safety: 2`, `test: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Plack::Test, Ref::Util, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `t/issues/gh-1712/gh-1712.t` (PERL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 25.04 | **LOC:** 71 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 4.359; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.2%), Guard Balance (formerly Safety Score) (60.3%), Complexity Load (formerly Cognitive Load) (16.6%), Connectivity (formerly Api Exposure) (6.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 22`, `args: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 3`, `import: 7`
* *Defense:* `safety: 2`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.359
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Dancer2, HTTP::Request::Common, Plack::Test, Ref::Util, Test::More, strict, warnings
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `t/request.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 99.78
- `t/request_upload.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 65.64
- `t/cookie.t` -> **Sawyer X** (100.0% isolated ownership) | Magnitude: 51.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `t/dsl/content.t` -> **Severity: 0.667** (Embedded: 0.0133 * Error Risk: 50.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `t/issues/gh-1449/TestPlugin.pm` -> **Severity: 806.5** (Blast Radius: 8.065 * Doc Risk: 100.0%)
- `t/auto_page.t` -> **Severity: 435.9** (Blast Radius: 4.359 * Doc Risk: 100.0%)
- `t/config_reader.t` -> **Severity: 435.9** (Blast Radius: 4.359 * Doc Risk: 100.0%)
- `t/cookie.t` -> **Severity: 435.9** (Blast Radius: 4.359 * Doc Risk: 100.0%)
- `t/dsl/extend.t` -> **Severity: 435.9** (Blast Radius: 4.359 * Doc Risk: 100.0%)

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
