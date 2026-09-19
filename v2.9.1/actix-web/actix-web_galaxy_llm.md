# ARCHITECTURAL_BRIEF: actix-web
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/actix/actix-web.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 376 analyzed artifact(s), 59274 LOC.
- **Load-bearing artifact:** `actix-web/src/web.rs` -- 56 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `actix-http/src/header/mod.rs` -- pulls in 88 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `actix-web/src/introspection.rs` at magnitude 578.3 (structural weight, not risk).
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
| Total Artifacts | 442 |
| Analyzed Artifacts (Scanned) | 376 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 66 |
| Total LOC | 59274 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 85.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4823 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3151 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.4412 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 312 | 59078 | 83.0% |
| MARKDOWN | 31 | 0 | 8.2% |
| PLAINTEXT | 28 | 0 | 7.4% |
| SHELL | 4 | 196 | 1.1% |
| JAVASCRIPT | 1 | 0 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Mid Flat Project`
> **Architectural Drift Z-Score:** `1.522`
> **Composition Archetype:** `Mid Flat Project` (z +1.52; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 23%, Data / Markup / Trivial 21%, State Mutators Files 18%, Large Core Modules (3) 12%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 317 | 84.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 59 | 15.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 66*

**Composition by Extension & Reason:**
- `.toml`: 12x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 13x Excluded (Unsupported Extension: '.stderr')
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 23 LOC)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.binary`: 3x Excluded (Unsupported Extension: '.binary')
- `.dot`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.br`: 2x Excluded (Unsupported Extension: '.br')
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.xz`: 1x Excluded (Explicitly Denied Extension: '.xz')
- `.zst`: 1x Excluded (Unsupported Extension: '.zst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.9 | 12.2 | 8.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 38.9 | 46.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.9 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.0 | 6.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 46.6 | 47.9 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.9 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 59.8 | 4.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.0 | 71.4 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2962 | 265 | 24 | `actix-web/src/service.rs` |
| cleanup | 61 | 23 | 0 | `awc/src/client/pool.rs` |
| guards | 1274 | 196 | 11 | `actix-web/src/server.rs` |
| danger | 2369 | 194 | 16 | `actix-http/tests/test_server.rs` |
| concurrency | 3548 | 189 | 26 | `actix-files/src/lib.rs` |
| connectivity | 3598 | 271 | 26 | `actix-web/src/service.rs` |
| io | 132 | 41 | 1 | `scripts/bump` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 4 | 0 | `actix-web/tests/test_httpserver.rs` |
| time | 23 | 15 | 0 | `actix-http/tests/test_h2_timer.rs` |
| serialization | 12 | 8 | 0 | `actix-web/src/types/json.rs` |
| regex | 33 | 8 | 0 | `scripts/bump` |
| events | 145 | 63 | 1 | `actix-http/src/h1/dispatcher.rs` |
| tests | 3379 | 180 | 28 | `actix-router/src/resource.rs` |
| docs | 11072 | 234 | 84 | `actix-router/src/resource.rs` |
| debt | 226 | 77 | 2 | `scripts/bump` |
| mutation | 8850 | 259 | 75 | `actix-files/src/lib.rs` |
| dead_code | 1713 | 234 | 15 | `actix-http/src/header/map.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 191 | 65 | 2 | `awc/src/client/connection.rs` |
| ml_ai | 16 | 7 | 0 | `actix-http/src/header/shared/quality.rs` |
| ui | 2 | 1 | 0 | `scripts/unreleased` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0625**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/bump` (Hits: 45)
- `scripts/unreleased` (Hits: 10)
- `actix-files/src/named.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **web.rs** (`actix-web/src/web.rs`) — 56 inbound connections
2. **guard.rs** (`actix-files/tests/guard.rs`) — 10 inbound connections
3. **read_body.rs** (`awc/src/responses/read_body.rs`) — 10 inbound connections
4. **header.rs** (`actix-web/src/types/header.rs`) — 6 inbound connections
5. **dev.rs** (`actix-web/src/dev.rs`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`actix-http/src/header/mod.rs`) — 88 outbound dependencies
2. **connector.rs** (`awc/src/client/connector.rs`) — 67 outbound dependencies
3. **resource.rs** (`actix-web/src/resource.rs`) — 61 outbound dependencies
4. **app.rs** (`actix-web/src/app.rs`) — 59 outbound dependencies
5. **scope.rs** (`actix-web/src/scope.rs`) — 58 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `set_headers` **(Many-Argument Workhorses)** (@ `actix-http/src/h1/decoder.rs`) -> Impact: **85.2** | LOC: 139
- `encode_headers` **(Many-Argument Workhorses)** (@ `actix-http/src/h1/encoder.rs`) -> Impact: **74.9** | LOC: 175
- `poll` **(Many-Argument Workhorses)** (@ `actix-multipart/src/multipart.rs`) -> Impact: **74.8** | LOC: 135
- `poll` **(Many-Argument Workhorses)** (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **73.4** | LOC: 187
- `into_response` **(Many-Argument Workhorses)** (@ `actix-files/src/named.rs`) -> Impact: **71.7** | LOC: 153
  * *Intent:* /// Creates an `HttpResponse` with file as a streaming body.
- `poll_response` **(Many-Argument Workhorses)** (@ `actix-http/src/h1/dispatcher.rs`) -> Impact: **71.0** | LOC: 208
- `start_with` **(Many-Argument Workhorses)** (@ `actix-test/src/lib.rs`) -> Impact: **68.3** | LOC: 362
  * *Intent:* /// } /// /// #[actix_web::test] /// async fn test_example() { /// let srv = actix_test::start_with(actix_test::config().h1(), || /// App::new().servi...
- `send_request` **(Many-Argument Workhorses)** (@ `awc/src/client/h1proto.rs`) -> Impact: **59.0** | LOC: 140
- `read_stream` **(Many-Argument Workhorses)** (@ `actix-multipart/src/field.rs`) -> Impact: **57.3** | LOC: 73
  * *Intent:* /// Reads content chunk of body part with unknown length. /// /// The `Content-Length` header for body part is not necessary.
- `connect` **(Defensive Guards)** (@ `awc/src/ws.rs`) -> Impact: **56.6** | LOC: 171
  * *Intent:* /// Complete request construction and connect to a WebSocket server.

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `actix-web/src` | 23 | 3980.92 | 15.57% | 30.05% |
| `actix-http/src/h1` | 14 | 2208.0 | 18.57% | 35.83% |
| `actix-http/src` | 14 | 1209.04 | 10.08% | 30.95% |
| `actix-files/src` | 10 | 1184.44 | 18.0% | 27.59% |
| `actix-web/src/http/header` | 27 | 1106.24 | 3.14% | 18.36% |
| `actix-web/src/middleware` | 11 | 1051.28 | 14.4% | 43.06% |
| `awc/src/client` | 8 | 1028.16 | 19.75% | 32.49% |
| `actix-router/src` | 10 | 1022.08 | 7.94% | 38.89% |
| `actix-web/src/types` | 10 | 953.74 | 18.85% | 31.1% |
| `awc/src` | 10 | 928.14 | 7.15% | 25.2% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `actix-http/src/header/into_value.rs` -> **100.0%** Exposure
- `actix-web/src/error/response_error.rs` -> **100.0%** Exposure
- `actix-http/src/header/as_name.rs` -> **99.9996%** Exposure
- `actix-web/src/http/header/macros.rs` -> **99.9985%** Exposure
- `actix-router/src/resource_path.rs` -> **99.9925%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/bump` -> **100.0%** Exposure
- `scripts/unreleased` -> **100.0%** Exposure
- `actix-http/src/notify_on_drop.rs` -> **99.8341%** Exposure
- `actix-http/src/responses/head.rs` -> **99.6642%** Exposure
- `actix-web/src/server.rs` -> **99.5647%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `actix-files/src/lib.rs` -> **47** Orphaned Functions | **0** Duplicates
- `actix-http/src/h1/decoder.rs` -> **39** Orphaned Functions | **0** Duplicates
- `actix-web/tests/test_server.rs` -> **31** Orphaned Functions | **0** Duplicates
- `actix-http/tests/test_server.rs` -> **29** Orphaned Functions | **0** Duplicates
- `actix-http/src/body/message_body.rs` -> **14** Orphaned Functions | **13** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5403` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `actix-web/src/introspection.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 578.3 | **LOC:** 1338 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.0%), Debt Markers (formerly Tech Debt) (22.8%)
- **Documentation Coverage:** 82.0896% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `has_conflicting_methods` **(Many-Argument Workhorses)** (Impact: 44.0)
  * `shadowed_route_context` **(Compute Cores)** (Impact: 28.7)
  * `shadowed_scope_context` **(Compute Cores)** (Impact: 22.3)
  * `merge_guard_detail_reports` **(Defensive Guards)** (Impact: 20.9)
  * `guard_possible_methods` **(Defensive Guards)** (Impact: 19.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 42 instances
* *State Mutation (weighted view):* 138
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 232`, `args: 89`, `func_start: 53`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 54`, `dead_code: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 54`, `import: 5`
* *Defense:* `safety: 20`, `doc: 75`, `test: 39`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, GuardDetail, crate::
    dev::ResourceDef, fmt::Write, guard::Guard, http::Method, serde::Serialize, std::
    collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 572.64 | **LOC:** 1305 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **42**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.9%), Connectivity (formerly Api Exposure) (62.9%)
- **Documentation Coverage:** 5.4945% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `listen_openssl_inner` **(Defensive Guards)** (Impact: 21.3)
  * `listen_rustls_0_20_inner` **(Defensive Guards)** (Impact: 21.1)
  * `listen_rustls_0_21_inner` **(Defensive Guards)** (Impact: 21.1)
  * `listen_rustls_0_22_inner` **(Defensive Guards)** (Impact: 21.1)
  * `listen_rustls_0_23_inner` **(Defensive Guards)** (Impact: 21.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 214`, `args: 100`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 66`, `dead_code: 6`
* *Architecture:* `api: 43`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 45`, `doc: 330`, `sync_locks: 21`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App, Error, Extensions, HttpResponse, HttpServer, HttpService, IntoServiceFactory, KeepAlive...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/dispatcher.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 522.4 | **LOC:** 1319 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.5%)
- **Documentation Coverage:** 73.0769% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `poll_response` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `poll_request` **(Many-Argument Workhorses)** (Impact: 49.0)
    * *Intent:* /// Process one incoming request. /// /// Returns true if any meaningful work was done.
  * `read_available` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /// Returns true when I/O stream can be disconnected after write to it. /// /// It covers these cond...
  * `handle_request` **(Many-Argument Workhorses)** (Impact: 20.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 210`, `args: 29`, `func_start: 21`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 50`, `dead_code: 7`, `planned_debt: 3`
* *Architecture:* `api: 13`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 21`, `doc: 19`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AsyncWrite, BoxBody, BytesMut, Encoder, Error, Extensions, FramedParts, HttpMessage...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-router/src/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 420.06 | **LOC:** 1781 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.1%), Mutation Surface (formerly State Flux) (69.3%), Dead Code Surface (formerly Dead Code) (53.0%), Guard Balance (formerly Safety Score) (21.2%)
- **Documentation Coverage:** 64.8148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `capture_match_info_fn` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /// /// let resource = ResourceDef::prefix("/user/{id}"); /// /// // path matches; segment values ar...
  * `parse` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* /// Parse `pattern` using `is_prefix` and `force_dynamic` flags. /// /// Parameters: /// - `is_prefi...
  * `parse_param` **(Compute Cores)** (Impact: 14.0)
    * *Intent:* /// Parses a dynamic segment definition from a pattern. /// /// The returned tuple includes: /// - t...
  * `static_match` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* /// Returns true if `prefix` acts as a proper prefix (i.e., separated by a slash) in `path`.
  * `pattern_iter` **(Generic / Templated Code)** (Impact: 12.3)
    * *Intent:* /// /// # Examples /// ``` /// # use actix_router::ResourceDef; /// let mut resource = ResourceDef::...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 319`, `args: 69`, `func_start: 59`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 5`, `state_mutation: 33`, `dead_code: 54`
* *Architecture:* `api: 48`, `import: 5`
* *Defense:* `safety: 9`, `doc: 541`, `test: 275`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cow, Hash, Hasher, IntoPatterns, Patterns, Regex, RegexSet, Resource...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/scope.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 405.46 | **LOC:** 1257 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **58**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (65.1%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (34.2%)
- **Documentation Coverage:** 77.0115% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `register` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `new_service` **(Callbacks & Closures)** (Impact: 6.9)
  * `call` **(Defensive Guards)** (Impact: 6.2)
  * `can_be_returned_from_fn` **(Annotated & Test Methods)** (Impact: 5.7)
  * `configure` **(Generic / Templated Code)** (Impact: 4.5)
    * *Intent:* /// cfg.service(web::resource("/test") /// .route(web::get().to(|| HttpResponse::Ok())) /// .route(w...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 170
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 338`, `args: 86`, `func_start: 47`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 26`, `dead_code: 17`, `planned_debt: 1`
* *Architecture:* `api: 44`, `concurrency: 135`, `import: 12`
* *Defense:* `safety: 5`, `doc: 174`, `test: 62`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` App, BoxedHttpService, BoxedHttpServiceFactory, Error, Extensions, HeaderValue, HttpMessage, HttpRequest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/decoder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 383.5 | **LOC:** 1186 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (83.9%), Guard Balance (formerly Safety Score) (75.2%), Mutation Surface (formerly State Flux) (50.6%), Concurrency Surface (formerly Concurrency) (17.0%)
- **Documentation Coverage:** 89.1892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_headers` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `decode` **(Compute Cores)** (Impact: 29.7)
  * `decode` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `decode` **(Compute Cores)** (Impact: 26.4)
  * `record` **(Stateful Encapsulated Methods)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 339`, `args: 68`, `func_start: 65`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 7`, `state_mutation: 25`, `dead_code: 1`, `unreferenced_by_name: 39`
* *Architecture:* `api: 20`, `concurrency: 5`, `import: 9`
* *Defense:* `safety: 10`, `doc: 27`, `test: 110`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BytesMut, ConnectionType, HeaderName, HeaderValue, HttpMessage, Method, Request, ResponseHead...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/form/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 381.32 | **LOC:** 926 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **40**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (87.2%), Guard Balance (formerly Safety Score) (50.8%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 70.1754% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_request` **(Compute Cores)** (Impact: 20.3)
  * `try_consume_limits` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* /// This function should be called within a [`FieldReader`] when reading each chunk of a field /// t...
  * `handle_field` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `handle_field` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `handle_field` **(Generic / Templated Code)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 126
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 260`, `args: 73`, `func_start: 50`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 25`, `concurrency: 86`, `import: 16`
* *Defense:* `safety: 11`, `doc: 67`, `test: 35`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App, ClientResponse, DerefMut, Error, Field, FieldReader, FromRequest, Future...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-multipart/src/multipart.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 377.4 | **LOC:** 884 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Mutation Surface (formerly State Flux) (66.2%)
- **Documentation Coverage:** 72.3404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Many-Argument Workhorses)** (Impact: 74.8)
  * `skip_until_boundary` **(Compute Cores)** (Impact: 33.2)
  * `read_boundary` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* /// /// Reads "in-between" and "final" boundaries. E.g. for boundary = "foo": /// /// ```plain /// -...
  * `read_field_headers` **(Compute Cores)** (Impact: 15.8)
  * `poll_next` **(Defensive Guards)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 6
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 218`, `args: 44`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 21`, `state_mutation: 29`, `planned_debt: 4`
* *Architecture:* `api: 20`, `concurrency: 51`, `import: 14`
* *Defense:* `safety: 20`, `doc: 37`, `test: 21`, `immutability_locks: 4`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BytesMut, ContentDisposition, DispositionType, Field, FromRequest, HeaderMap, HeaderName, HeaderValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/request.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 362.8 | **LOC:** 1249 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.2%), Connectivity (formerly Api Exposure) (84.7%), Guard Balance (formerly Safety Score) (43.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.0%)
- **Documentation Coverage:** 56.7164% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Compute Cores)** (Impact: 20.7)
  * `cookies` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* /// Load request cookies. /// /// Any cookie that cannot be parsed is omitted from the result. /// T...
  * `check_full_url` **(Annotated & Test Methods)** (Impact: 8.1)
  * `cookie` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /// Return request cookie.
  * `test_data` **(Annotated & Test Methods)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 232`, `args: 93`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 23`, `dead_code: 20`, `duplicate_logic: 2`
* *Architecture:* `api: 74`, `concurrency: 46`, `import: 12`
* *Defense:* `safety: 8`, `doc: 221`, `test: 84`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App, Error, FromRequest, Hash, HttpMessage, HttpRequest, HttpResponse, Method...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/service.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 348.62 | **LOC:** 1130 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **47**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.2%), Connectivity (formerly Api Exposure) (62.9%)
- **Documentation Coverage:** 28.8136% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rustls_with_config` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /// Create Rustls v0.20 based service with custom TLS acceptor configuration.
  * `rustls_021_with_config` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /// Create Rustls v0.21 based service with custom TLS acceptor configuration.
  * `rustls_0_22_with_config` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /// Create Rustls v0.22 based service with custom TLS acceptor configuration.
  * `rustls_0_23_with_config` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /// Create Rustls v0.23 based service with custom TLS acceptor configuration.
  * `openssl_with_config` **(Defensive Guards)** (Impact: 16.1)
    * *Intent:* /// Create OpenSSL based service with custom TLS acceptor configuration.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 2
* *Concurrency (weighted view):* 78
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 196`, `args: 50`, `func_start: 28`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 45`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 37`, `concurrency: 53`, `import: 27`
* *Defense:* `safety: 19`, `doc: 64`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Acceptor, AsyncWrite, ConnectCallback, Framed, IntoServiceFactory, MessageBody, OnConnectData, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-files/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 340.6 | **LOC:** 1104 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 80.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **44**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (93.7%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (58.4%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_named_file_empty_range_headers` **(Annotated & Test Methods)** (Impact: 3.9)
  * `test_named_file_content_length_headers` **(Annotated & Test Methods)** (Impact: 3.9)
  * `test_redirect_to_slash_directory` **(Annotated & Test Methods)** (Impact: 3.8)
  * `test_named_file_content_encoding_gzip` **(Annotated & Test Methods)** (Impact: 3.4)
  * `test_named_file_content_range_headers` **(Annotated & Test Methods)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Concurrency (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 425`, `args: 61`, `func_start: 49`
* *Risk/State:* `safety_bypasses: 104`, `state_mutation: 14`, `unreferenced_by_name: 47`
* *Architecture:* `io: 4`, `api: 2`, `concurrency: 172`, `import: 10`
* *Defense:* `doc: 17`, `test: 110`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App, BoxServiceFactory, Bytes, ContentDisposition, DirectoryRenderer, DispositionParam, HttpResponse, Method...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/service.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 336.36 | **LOC:** 926 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **57**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.7%), Concurrency Surface (formerly Concurrency) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 33.9744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Compute Cores)** (Impact: 16.6)
  * `register` **(Defensive Guards)** (Impact: 13.1)
  * `test_services_vec` **(Annotated & Test Methods)** (Impact: 6.8)
  * `test_services_macro` **(Annotated & Test Methods)** (Impact: 4.8)
  * `app_data` **(Generic / Templated Code)** (Impact: 4.7)
    * *Intent:* /// Counterpart to [`HttpRequest::app_data`].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 170`, `args: 102`, `func_start: 85`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 9`, `dead_code: 8`, `planned_debt: 2`
* *Architecture:* `api: 79`, `concurrency: 36`, `import: 10`
* *Defense:* `safety: 4`, `doc: 123`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App, AppService, BoxServiceFactory, BoxedPayloadStream, EitherBody, Error, Extensions, FromRequest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/client/connector.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 327.3 | **LOC:** 1154 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **67**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.1%), Guard Balance (formerly Safety Score) (54.5%)
- **Documentation Coverage:** 37.6812% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finish` **(Compute Cores)** (Impact: 43.2)
    * *Intent:* /// Finish configuration process and create connector service. /// /// The `Connector` builder alway...
  * `poll` **(Generic / Templated Code)** (Impact: 9.8)
  * `resolver` **(Generic / Templated Code)** (Impact: 7.6)
  * `poll_ready` **(Generic / Templated Code)** (Impact: 7.3)
  * `build_tls` **(Compute Cores)** (Impact: 6.6)
    * *Intent:* /// Build TLS connector with Rustls v0.23, based on supplied ALPN protocols. /// /// Note that if ot...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 212`, `args: 68`, `func_start: 48`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 25`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 31`, `concurrency: 34`, `import: 34`
* *Defense:* `safety: 5`, `doc: 110`, `test: 3`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BytesMut, Connect, ConnectInfo, Connection, ConnectionIo, Connector, Poll, Ready...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/tests/test_server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 325.34 | **LOC:** 1024 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (86.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.8%), Complexity Load (formerly Cognitive Load) (20.5%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `h2_flow_control_window_sizes` **(I/O & Config Routines)** (Impact: 11.2)
  * `content_length_truncated` **(Annotated & Test Methods)** (Impact: 9.7)
  * `expect_continue_h1` **(Callbacks & Closures)** (Impact: 8.6)
  * `expect_continue` **(Annotated & Test Methods)** (Impact: 8.5)
  * `chunked_payload` **(Callbacks & Closures)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 157
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 433`, `args: 97`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 6`, `state_mutation: 7`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `concurrency: 152`, `import: 13`
* *Defense:* `safety: 3`, `doc: 2`, `test: 76`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AsyncWriteExt, BodyStream, BoxBody, Error, FutureExt, HeaderValue, HttpService, Instant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/middleware/logger.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 315.56 | **LOC:** 1031 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **45**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.1%), Guard Balance (formerly Safety Score) (59.9%), Concurrency Surface (formerly Concurrency) (57.6%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_request` **(Many-Argument Workhorses)** (Impact: 26.9)
  * `new` **(Compute Cores)** (Impact: 18.2)
    * *Intent:* /// Create a `Format` from a format string. /// /// Returns `None` if the format string syntax is in...
  * `poll` **(Defensive Guards)** (Impact: 12.7)
  * `new_transform` **(Defensive Guards)** (Impact: 11.5)
  * `custom_request_replace` **(Generic / Templated Code)** (Impact: 11.3)
    * *Intent:* /// Register a function that receives a ServiceRequest and returns a String for use in the /// log l...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 90`, `structural_boundaries: 251`, `args: 52`, `func_start: 34`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 4`, `state_mutation: 19`, `dead_code: 4`
* *Architecture:* `api: 26`, `concurrency: 23`, `import: 15`
* *Defense:* `safety: 16`, `doc: 132`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App, Display, Error, HttpResponse, Level, MessageBody, OffsetDateTime, Poll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/encoder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 307.28 | **LOC:** 688 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.7%), Connectivity (formerly Api Exposure) (55.6%)
- **Documentation Coverage:** 72.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_headers` **(Many-Argument Workhorses)** (Impact: 74.9)
  * `encode` **(Many-Argument Workhorses)** (Impact: 26.9)
    * *Intent:* /// Encode message.
  * `encode` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* /// Encode message. Return `EOF` state of encoder
  * `write_camel_case` **(Defensive Guards)** (Impact: 11.5)
    * *Intent:* /// # Safety /// Callers must ensure that the given `len` matches the given `value` length and that ...
  * `encode_eof` **(Compute Cores)** (Impact: 9.7)
    * *Intent:* /// Encode eof. Return `EOF` state of encoder
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 133`, `args: 42`, `func_start: 36`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 35`, `dead_code: 1`
* *Architecture:* `api: 18`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 8`, `doc: 19`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BytesMut, CONNECTION, CONTENT_LENGTH, CONTENT_TYPE, ConnectionType, DATE, HeaderMap, HeaderName...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/header/map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 293.92 | **LOC:** 1206 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Debt Markers (formerly Tech Debt) (96.9%), Dead Code Surface (formerly Dead Code) (62.8%), Guard Balance (formerly Safety Score) (38.1%)
- **Documentation Coverage:** 43.3735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next` **(Defensive Guards)** (Impact: 8.1)
  * `next` **(Defensive Guards)** (Impact: 6.8)
  * `next` **(Defensive Guards)** (Impact: 6.7)
  * `get_value` **(Generic / Templated Code)** (Impact: 5.5)
  * `get_mut` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* /// # use actix_http::header::{self, HeaderMap, HeaderValue}; /// let mut map = HeaderMap::new(); //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 188`, `args: 72`, `func_start: 62`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 77`, `dead_code: 42`, `planned_debt: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 15`
* *Architecture:* `api: 29`, `import: 9`
* *Defense:* `safety: 11`, `doc: 458`, `test: 88`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashMapExt, HeaderMap, HeaderValue, SmallVec, actix_http::header::HeaderMap, actix_http::header::self, collections::hash_map, foldhash::HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/tests/test_server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 293.62 | **LOC:** 909 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (23.1%), Dead Code Surface (formerly Dead Code) (8.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_server_cookies` **(Annotated & Test Methods)** (Impact: 9.8)
  * `test_data_drop` **(Annotated & Test Methods)** (Impact: 6.4)
    * *Intent:* // allow deprecated App::data
  * `poll_next` **(Generic / Templated Code)** (Impact: 5.8)
  * `body_gzip_large` **(Annotated & Test Methods)** (Impact: 4.5)
    * *Intent:* // .request(actix_web::http::Method::GET, srv.url("/raw")) // .no_decompress() // .append_header((AC...
  * `test_body_gzip_large_random` **(Annotated & Test Methods)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Concurrency (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 314`, `args: 94`, `func_start: 36`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 5`, `dead_code: 6`, `unreferenced_by_name: 31`
* *Architecture:* `io: 1`, `concurrency: 139`, `import: 13`
* *Defense:* `test: 71`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App, Arc, Error, HttpResponse, NormalizePath, Ordering, Poll, SampleString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/http/header/content_disposition.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 290.88 | **LOC:** 1013 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (79.1%), Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (60.9%), Dead Code Surface (formerly Dead Code) (15.2%)
- **Documentation Coverage:** 48.8636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_raw` **(Compute Cores)** (Impact: 45.4)
    * *Intent:* /// Parse a raw Content-Disposition header value.
  * `from` **(Compute Cores)** (Impact: 10.4)
  * `fmt` **(Many-Argument Workhorses)** (Impact: 8.3)
  * `as_unknown` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* /// Returns the value of the unrecognized regular parameter if it is /// [`Unknown`](DispositionPara...
  * `as_unknown_ext` **(Generic / Templated Code)** (Impact: 5.7)
    * *Intent:* /// Returns the value of the unrecognized extended parameter if it is /// [`Unknown`](DispositionPar...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 155`, `args: 56`, `func_start: 48`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 37`, `dead_code: 10`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 4`, `doc: 194`, `test: 61`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DispositionParam, DispositionType, ExtendedValue, Header, HeaderValue, TryIntoHeaderValue, Write, Writer...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/src/middleware/redirect.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 285.78 | **LOC:** 681 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **31**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.3%), Connectivity (formerly Api Exposure) (50.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Many-Argument Workhorses)** (Impact: 31.0)
  * `build_next_uri` **(Compute Cores)** (Impact: 15.9)
  * `test_redirect_cross_origin_headers` **(I/O & Config Routines)** (Impact: 14.2)
  * `test` **(Compute Cores)** (Impact: 9.1)
  * `call` **(Compute Cores)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 148`, `args: 57`, `func_start: 29`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 15`, `dead_code: 1`
* *Architecture:* `api: 17`, `concurrency: 49`, `import: 11`
* *Defense:* `safety: 3`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` App, ClientBuilder, ClientResponse, ConnectResponse, Error, HttpRequest, HttpResponse, Method...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web-actors/src/ws.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 283.74 | **LOC:** 1053 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **56**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.9%), Concurrency Surface (formerly Concurrency) (63.6%), Guard Balance (formerly Safety Score) (48.0%)
- **Documentation Coverage:** 34.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handshake_with_protocols` **(Defensive Guards)** (Impact: 33.4)
    * *Intent:* /// Prepare WebSocket handshake response. /// /// This function returns handshake `HttpResponse`, re...
  * `poll_next` **(Compute Cores)** (Impact: 23.0)
  * `poll_next` **(Defensive Guards)** (Impact: 22.0)
  * `test_handshake` **(I/O & Config Routines)** (Impact: 9.0)
  * `start_with_protocols` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* /// Do WebSocket handshake and start ws actor. /// /// `protocols` is a sequence of known protocols.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 170`, `args: 48`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 11`
* *Architecture:* `api: 35`, `concurrency: 25`, `import: 13`
* *Defense:* `safety: 12`, `doc: 198`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Actor, ActorContext, ActorState, Addr, App, AsyncContext, BytesMut, CloseReason...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 275.8 | **LOC:** 926 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **61**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (67.4%), Mutation Surface (formerly State Flux) (48.0%), Guard Balance (formerly Safety Score) (44.6%)
- **Documentation Coverage:** 62.2642% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `register` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `can_be_returned_from_fn` **(Annotated & Test Methods)** (Impact: 6.6)
  * `new_service` **(Generic / Templated Code)** (Impact: 6.0)
  * `new` **(Defensive Guards)** (Impact: 5.6)
    * *Intent:* /// Constructs new resource that matches a `path` pattern.
  * `call` **(Compute Cores)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 7 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 194`, `args: 55`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `dead_code: 19`, `planned_debt: 3`
* *Architecture:* `api: 28`, `concurrency: 67`, `import: 15`
* *Defense:* `safety: 6`, `doc: 188`, `test: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` App, AppService, BoxedHttpServiceFactory, Error, FromRequest, Guard, HttpMessage, HttpRequest...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `awc/tests/test_client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 267.58 | **LOC:** 841 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (83.7%), Complexity Load (formerly Cognitive Load) (20.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `client_cookie_handling` **(Callbacks & Closures)** (Impact: 10.1)
  * `response_timeout` **(I/O & Config Routines)** (Impact: 9.6)
  * `connection_wait_queue` **(Annotated & Test Methods)** (Impact: 5.3)
  * `connection_wait_queue_force_close` **(Annotated & Test Methods)** (Impact: 5.3)
  * `client_basic_auth` **(Annotated & Test Methods)** (Impact: 5.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 279`, `args: 92`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 5`, `state_mutation: 6`, `unreferenced_by_name: 25`
* *Architecture:* `io: 5`, `concurrency: 118`, `import: 14`
* *Defense:* `safety: 2`, `test: 61`, `sync_locks: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` App, Arc, Error, ErrorKind, HttpRequest, HttpResponse, Ipv4Addr, Ordering...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-files/src/named.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 249.36 | **LOC:** 739 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **49**; blast radius 3.814; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.7%), Guard Balance (formerly Safety Score) (38.6%)
- **Documentation Coverage:** 25.4237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `into_response` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* /// Creates an `HttpResponse` with file as a streaming body.
  * `get_content_type_and_disposition` **(Stateful Encapsulated Methods)** (Impact: 12.3)
  * `none_match` **(Defensive Guards)** (Impact: 9.6)
    * *Intent:* /// Returns true if `req` doesn't have an `If-None-Match` header matching `req`.
  * `etag` **(Stateful Encapsulated Methods)** (Impact: 9.5)
    * *Intent:* /// Creates an `ETag` in a format is similar to Apache's.
  * `any_match` **(Defensive Guards)** (Impact: 9.5)
    * *Intent:* /// Returns true if `req` has no `If-Match` header or one which matches `etag`.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 124`, `args: 32`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`, `dead_code: 16`
* *Architecture:* `io: 6`, `api: 40`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 13`, `doc: 132`, `test: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.814
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002667
  * `Imports (Out-Degree: 0):` AppService, BoxBody, Charset, ContentDisposition, ContentEncoding, DerefMut, DispositionParam, DispositionType...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `actix-http/tests/test_rustls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 235.82 | **LOC:** 695 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **48**; blast radius 2.062; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (75.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.5%), Complexity Load (formerly Cognitive Load) (23.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `h2_content_length` **(Annotated & Test Methods)** (Impact: 8.2)
  * `load_body` **(Generic / Templated Code)** (Impact: 6.7)
  * `h2_headers` **(Annotated & Test Methods)** (Impact: 5.1)
  * `h2_body1` **(Annotated & Test Methods)** (Impact: 4.0)
  * `h2_response_http_error_handling` **(Annotated & Test Methods)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 119
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 245`, `args: 77`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 50`, `state_mutation: 7`, `unreferenced_by_name: 19`
* *Architecture:* `api: 1`, `concurrency: 104`, `import: 15`
* *Defense:* `safety: 1`, `test: 49`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BoxBody, BytesMut, Connector, Error, HeaderName, HeaderValue, HttpService, Method...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `actix-web/src/introspection.rs` -> **Guillermo Céspedes Tabárez** (100.0% isolated ownership) | Magnitude: 578.3
- `actix-multipart/src/form/mod.rs` -> **fasilmveloor** (100.0% isolated ownership) | Magnitude: 381.32
- `actix-http/src/service.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 348.62
- `actix-web/src/service.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 336.36
- `actix-http/src/h1/encoder.rs` -> **Ali Mirghasemi** (100.0% isolated ownership) | Magnitude: 307.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `actix-web/src/types/header.rs` -> **Severity: 0.745** (Embedded: 0.016 * Error Risk: 46.5814%)
- `actix-web/src/dev.rs` -> **Severity: 0.628** (Embedded: 0.0107 * Error Risk: 58.904%)
- `actix-http/src/body/boxed.rs` -> **Severity: 0.439** (Embedded: 0.008 * Error Risk: 54.8155%)
- `actix-web/examples/introspection.rs` -> **Severity: 0.3** (Embedded: 0.0053 * Error Risk: 56.2177%)
- `actix-http/src/notify_on_drop.rs` -> **Severity: 0.223** (Embedded: 0.0027 * Error Risk: 83.5974%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `actix-files/tests/guard.rs` -> **Severity: 9364.9** (Blast Radius: 93.649 * Doc Risk: 100.0%)
- `awc/src/responses/read_body.rs` -> **Severity: 1038.6** (Blast Radius: 10.386 * Doc Risk: 100.0%)
- `actix-web/src/types/header.rs` -> **Severity: 1006.16** (Blast Radius: 12.577 * Doc Risk: 80.0%)
- `actix-web/src/dev.rs` -> **Severity: 498.3** (Blast Radius: 4.983 * Doc Risk: 100.0%)
- `actix-web/examples/introspection.rs` -> **Severity: 369.025** (Blast Radius: 3.814 * Doc Risk: 96.7555%)

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
