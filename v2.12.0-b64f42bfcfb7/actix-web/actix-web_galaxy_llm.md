# ARCHITECTURAL_BRIEF: actix-web
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/actix/actix-web.git` |
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
- **Scope:** 390 analyzed artifact(s), 59657 LOC.
- **Load-bearing artifact:** `actix-http/src/lib.rs` -- 108 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `actix-http/src/header/mod.rs` -- pulls in 122 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `actix-web/src/introspection.rs` at magnitude 586.3 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 390 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 52 |
| Total LOC | 59657 |
| Volatility Index | 0.013 |
| % Scanned of codebase = | 88.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4302 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1239 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 43.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1762 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 312 | 59078 | 80.0% |
| MARKDOWN | 34 | 0 | 8.7% |
| PLAINTEXT | 28 | 0 | 7.2% |
| YAML | 11 | 383 | 2.8% |
| SHELL | 4 | 196 | 1.0% |
| JAVASCRIPT | 1 | 0 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 390 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Generic / Templated Code Files 22%, State Mutators Files 18%, Large Core Modules (3) 12%, Declarative / Non-Code 10%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 328 | 84.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 62 | 15.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 52*

**Composition by Extension & Reason:**
- `.toml`: 12x Unsupported Format (.toml), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.toml')
- `.stderr`: 13x Excluded (Unsupported Extension: '.stderr')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.png`: 3x Excluded (Explicitly Denied Extension: '.png')
- `.binary`: 3x Excluded (Unsupported Extension: '.binary')
- `.dot`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.br`: 2x Excluded (Unsupported Extension: '.br')
- `.gz`: 2x Excluded (Explicitly Denied Extension: '.gz')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')
- `.xz`: 1x Excluded (Explicitly Denied Extension: '.xz')
- `.zst`: 1x Excluded (Unsupported Extension: '.zst')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.9 | 11.8 | 8.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.1 | 36.9 | 48.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.4 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 79.6 | 28.3 | 31.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 45.5 | 36.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.5 | 0.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.7 | 73.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 289 | 84 | 3 | `actix-web/src/rmap.rs` |
| cleanup | 61 | 23 | 0 | `awc/src/client/pool.rs` |
| guards | 1322 | 203 | 11 | `actix-web/src/server.rs` |
| danger | 2369 | 194 | 16 | `actix-http/tests/test_server.rs` |
| concurrency | 3553 | 194 | 25 | `actix-files/src/lib.rs` |
| connectivity | 3997 | 278 | 28 | `actix-web/src/service.rs` |
| io | 132 | 41 | 1 | `scripts/bump` |
| crypto | 0 | 0 | 0 | - |
| ipc | 9 | 4 | 0 | `actix-web/tests/test_httpserver.rs` |
| time | 23 | 15 | 0 | `actix-http/tests/test_h2_timer.rs` |
| serialization | 12 | 8 | 0 | `actix-web/src/types/json.rs` |
| regex | 33 | 8 | 0 | `scripts/bump` |
| events | 147 | 64 | 1 | `actix-http/src/h1/dispatcher.rs` |
| tests | 3380 | 181 | 27 | `actix-router/src/resource.rs` |
| docs | 11085 | 241 | 83 | `actix-router/src/resource.rs` |
| debt | 231 | 80 | 2 | `scripts/bump` |
| mutation | 8854 | 263 | 73 | `actix-files/src/lib.rs` |
| dead_code | 455 | 96 | 2 | `actix-files/src/lib.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
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

1. **lib.rs** (`actix-http/src/lib.rs`) — 108 inbound connections
2. **mod.rs** (`actix-http/src/header/mod.rs`) — 89 inbound connections
3. **error.rs** (`actix-http/src/error.rs`) — 78 inbound connections
4. **app.rs** (`actix-web/src/app.rs`) — 74 inbound connections
5. **response.rs** (`actix-web/src/response/response.rs`) — 73 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`actix-http/src/header/mod.rs`) — 122 outbound dependencies
2. **connector.rs** (`awc/src/client/connector.rs`) — 71 outbound dependencies
3. **mod.rs** (`actix-web/src/http/header/mod.rs`) — 61 outbound dependencies
4. **service.rs** (`actix-http/src/h2/service.rs`) — 53 outbound dependencies
5. **resource.rs** (`actix-web/src/resource.rs`) — 53 outbound dependencies

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
| `actix-web/src` | 23 | 4022.72 | 14.96% | 7.66% |
| `actix-http/src/h1` | 14 | 2266.8 | 18.56% | 13.41% |
| `actix-http/src` | 14 | 1222.04 | 10.05% | 9.38% |
| `actix-files/src` | 10 | 1193.44 | 18.0% | 9.37% |
| `actix-web/src/http/header` | 27 | 1112.14 | 3.14% | 11.87% |
| `actix-web/src/middleware` | 11 | 1062.68 | 14.25% | 18.61% |
| `awc/src/client` | 8 | 1036.76 | 19.65% | 18.13% |
| `actix-router/src` | 10 | 1033.48 | 7.92% | 25.0% |
| `actix-web/src/types` | 10 | 975.74 | 18.85% | 14.96% |
| `awc/src` | 10 | 929.34 | 7.14% | 6.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `actix-http/src/header/into_value.rs` -> **100.0%** Exposure
- `actix-web/src/error/response_error.rs` -> **100.0%** Exposure
- `actix-http/src/header/as_name.rs` -> **99.9996%** Exposure
- `actix-web/src/http/header/macros.rs` -> **99.9985%** Exposure
- `actix-router/src/resource_path.rs` -> **99.9447%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/bump` -> **100.0%** Exposure
- `scripts/unreleased` -> **100.0%** Exposure
- `actix-http/src/notify_on_drop.rs` -> **99.8341%** Exposure
- `actix-http/src/responses/head.rs` -> **99.6642%** Exposure
- `actix-web/src/server.rs` -> **99.5647%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `actix-files/src/lib.rs` -> **47** Orphaned Functions | **0** Duplicates
- `actix-web/tests/test_server.rs` -> **31** Orphaned Functions | **0** Duplicates
- `actix-http/tests/test_server.rs` -> **29** Orphaned Functions | **0** Duplicates
- `awc/tests/test_client.rs` -> **25** Orphaned Functions | **0** Duplicates
- `actix-http/tests/test_rustls.rs` -> **19** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `5091` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `actix-web/src/introspection.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.811)
- **Top Global Matches:** file_cluster_0: 8.811, file_cluster_5: 8.85, file_cluster_12: 8.974
- **Magnitude:** 586.3 | **LOC:** 1338 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.825; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (55.2%), Guard Balance (formerly Safety Score) (53.7%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
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
* *Structure:* `branch: 120`, `structural_boundaries: 232`, `args: 89`, `func_start: 53`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 54`
* *Architecture:* `api: 63`, `import: 5`
* *Defense:* `safety: 20`, `doc: 75`, `test: 39`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.825
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.112811
  * `Imports (Out-Degree: 3):` crate::dev::ResourceDef, crate::guard::Guard, crate::guard::GuardDetail, crate::http::Method, self::*, serde::Serialize, std::collections::BTreeMap, std::collections::BTreeSet...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `actix-web/src/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.595)
- **Top Global Matches:** file_cluster_5: 6.595, file_cluster_12: 8.12, file_cluster_0: 9.481
- **Magnitude:** 572.64 | **LOC:** 1305 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **36**; blast radius 2.111; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.7%), Guard Balance (formerly Safety Score) (54.7%)
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
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 66`
* *Architecture:* `api: 43`, `concurrency: 13`, `import: 14`
* *Defense:* `safety: 45`, `doc: 330`, `sync_locks: 21`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.111
  * `Choke Point (Betweenness):` 0.001232 | `Ripple Effect (Closeness):` 0.117728
  * `Imports (Out-Degree: 9):` actix_http::Extensions, actix_http::HttpService, actix_http::KeepAlive, actix_http::Protocol, actix_http::Request, actix_http::Response, actix_http::TlsAcceptorConfig, actix_http::body::MessageBody...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `actix-http/src/h1/dispatcher.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.015)
- **Top Global Matches:** file_cluster_6: 8.015, file_cluster_4: 9.659, file_cluster_0: 16.472
- **Magnitude:** 520.7 | **LOC:** 1319 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **48**; blast radius 1.302; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.9%), Concurrency Surface (formerly Concurrency) (28.7%)
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
* *Structure:* `branch: 149`, `structural_boundaries: 210`, `args: 29`, `func_start: 21`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 1`, `state_mutation: 50`, `planned_debt: 3`
* *Architecture:* `api: 13`, `concurrency: 8`, `import: 13`
* *Defense:* `safety: 21`, `doc: 19`, `test: 6`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.302
  * `Choke Point (Betweenness):` 0.000163 | `Ripple Effect (Closeness):` 0.184101
  * `Imports (Out-Degree: 16):` actix_codec::Framed, actix_codec::FramedParts, actix_rt::time::sleep_until, actix_service::Service, bitflags::bitflags, bytes::Buf, bytes::BytesMut, crate::Error...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `actix-http/src/h1/decoder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.904)
- **Top Global Matches:** file_cluster_5: 7.904, file_cluster_12: 9.768, file_cluster_7: 10.068
- **Magnitude:** 421.0 | **LOC:** 1186 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **26**; blast radius 2.087; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.8%), Connectivity (formerly Api Exposure) (56.2%), Mutation Surface (formerly State Flux) (50.6%), Concurrency Surface (formerly Concurrency) (17.0%)
- **Documentation Coverage:** 92.9204% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_headers` **(Many-Argument Workhorses)** (Impact: 85.2)
  * `decode` **(Compute Cores)** (Impact: 28.2)
  * `decode` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `decode` **(Compute Cores)** (Impact: 26.4)
  * `record` **(Stateful Encapsulated Methods)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 339`, `args: 68`, `func_start: 65`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 7`, `state_mutation: 25`
* *Architecture:* `api: 59`, `concurrency: 5`, `import: 9`
* *Defense:* `safety: 10`, `doc: 27`, `test: 110`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.087
  * `Choke Point (Betweenness):` 0.00034 | `Ripple Effect (Closeness):` 0.185604
  * `Imports (Out-Degree: 8):` actix_codec::Decoder, bytes::Bytes, bytes::BytesMut, crate::ConnectionType, crate::HttpMessage, crate::Request, crate::ResponseHead, crate::error::ParseError...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `actix-router/src/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.324)
- **Top Global Matches:** file_cluster_5: 7.324, file_cluster_12: 7.645, file_cluster_0: 9.764
- **Magnitude:** 413.26 | **LOC:** 1781 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **18**; blast radius 7.724; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (69.3%), Connectivity (formerly Api Exposure) (62.1%), Guard Balance (formerly Safety Score) (39.2%), Complexity Load (formerly Cognitive Load) (8.6%)
- **Documentation Coverage:** 64.8148% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse` **(Many-Argument Workhorses)** (Impact: 37.5)
    * *Intent:* /// Parse `pattern` using `is_prefix` and `force_dynamic` flags. /// /// Parameters: /// - `is_prefi...
  * `capture_match_info_fn` **(Many-Argument Workhorses)** (Impact: 33.8)
    * *Intent:* /// /// let resource = ResourceDef::prefix("/user/{id}"); /// /// // path matches; segment values ar...
  * `static_match` **(Compute Cores)** (Impact: 12.7)
    * *Intent:* /// Returns true if `prefix` acts as a proper prefix (i.e., separated by a slash) in `path`.
  * `pattern_iter` **(Generic / Templated Code)** (Impact: 12.3)
    * *Intent:* /// /// # Examples /// ``` /// # use actix_router::ResourceDef; /// let mut resource = ResourceDef::...
  * `parse_param` **(Compute Cores)** (Impact: 11.2)
    * *Intent:* /// Parses a dynamic segment definition from a pattern. /// /// The returned tuple includes: /// - t...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 319`, `args: 69`, `func_start: 59`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 5`, `state_mutation: 33`
* *Architecture:* `api: 48`, `import: 5`
* *Defense:* `safety: 9`, `doc: 541`, `test: 275`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.724
  * `Choke Point (Betweenness):` 0.001946 | `Ripple Effect (Closeness):` 0.18955
  * `Imports (Out-Degree: 4):` crate::IntoPatterns, crate::Path, crate::Patterns, crate::Resource, crate::ResourcePath, crate::path::PathItem, crate::regex_set::Regex, crate::regex_set::RegexSet...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `actix-web/src/scope.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_5: 6.43, file_cluster_12: 8.729, file_cluster_7: 9.66
- **Magnitude:** 405.46 | **LOC:** 1257 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **53**; blast radius 1.247; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (65.1%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (34.2%)
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
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 26`, `planned_debt: 1`
* *Architecture:* `api: 44`, `concurrency: 135`, `import: 12`
* *Defense:* `safety: 5`, `doc: 174`, `test: 62`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.247
  * `Choke Point (Betweenness):` 0.000423 | `Ripple Effect (Closeness):` 0.147871
  * `Imports (Out-Degree: 24):` actix_http::Extensions, actix_http::body::MessageBody, actix_router::ResourceDef, actix_router::Router, actix_service::IntoServiceFactory, actix_service::Service, actix_service::ServiceFactory, actix_service::ServiceFactoryExt...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `actix-multipart/src/form/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.67)
- **Top Global Matches:** file_cluster_5: 7.67, file_cluster_0: 7.936, file_cluster_12: 9.712
- **Magnitude:** 381.32 | **LOC:** 926 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **42**; blast radius 4.321; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (87.2%), Guard Balance (formerly Safety Score) (50.3%), Complexity Load (formerly Cognitive Load) (35.3%)
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
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 15`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 14`
* *Architecture:* `api: 25`, `concurrency: 86`, `import: 16`
* *Defense:* `safety: 11`, `doc: 67`, `test: 35`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.321
  * `Choke Point (Betweenness):` 0.006779 | `Ripple Effect (Closeness):` 0.03599
  * `Imports (Out-Degree: 24):` bytes, json, tempfile, text, actix_http::encoding::Decoder, actix_multipart_derive::MultipartForm, actix_multipart_rfc7578::client::multipart, actix_test::TestServer...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `actix-multipart/src/multipart.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.653)
- **Top Global Matches:** file_cluster_5: 9.653, file_cluster_12: 10.512, file_cluster_4: 10.571
- **Magnitude:** 377.4 | **LOC:** 884 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **39**; blast radius 1.399; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (97.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (66.2%), Guard Balance (formerly Safety Score) (62.6%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.399
  * `Choke Point (Betweenness):` 0.001492 | `Ripple Effect (Closeness):` 0.024764
  * `Imports (Out-Degree: 15):` actix_http::h1, actix_web::FromRequest, actix_web::HttpRequest, actix_web::dev, actix_web::error::ParseError, actix_web::error::PayloadError, actix_web::http::header, actix_web::http::header::ContentDisposition...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `actix-web/src/request.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.749)
- **Top Global Matches:** file_cluster_5: 6.749, file_cluster_12: 8.433, file_cluster_0: 10.179
- **Magnitude:** 356.8 | **LOC:** 1249 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **50** in-repo importer(s); it depends on **49**; blast radius 7.605; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (93.2%), Connectivity (formerly Api Exposure) (59.6%), Guard Balance (formerly Safety Score) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.3%)
- **Documentation Coverage:** 56.7164% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Compute Cores)** (Impact: 20.7)
  * `cookies` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* /// Load request cookies. /// /// Any cookie that cannot be parsed is omitted from the result. /// T...
  * `cookie` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* /// Return request cookie.
  * `test_data` **(Annotated & Test Methods)** (Impact: 6.6)
  * `drop` **(Defensive Guards)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 1 instances
* *Concurrency (weighted view):* 51
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 232`, `args: 93`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 23`, `duplicate_logic: 2`
* *Architecture:* `api: 74`, `concurrency: 46`, `import: 12`
* *Defense:* `safety: 8`, `doc: 221`, `test: 84`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.605
  * `Choke Point (Betweenness):` 0.022987 | `Ripple Effect (Closeness):` 0.214051
  * `Imports (Out-Degree: 26):` actix_http::Message, actix_http::RequestHead, actix_http::header::COOKIE, actix_router::Path, actix_router::Url, actix_utils::future::Ready, actix_utils::future::ok, bytes::Bytes...
  * `Imported By (In-Degree: 50):` (Excluded from Brief to save tokens)

### `actix-http/src/service.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.812)
- **Top Global Matches:** file_cluster_5: 6.812, file_cluster_0: 8.788, file_cluster_12: 9.949
- **Magnitude:** 348.62 | **LOC:** 1130 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **31** in-repo importer(s); it depends on **51**; blast radius 5.754; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Guard Balance (formerly Safety Score) (54.5%), Connectivity (formerly Api Exposure) (52.0%), Mutation Surface (formerly State Flux) (47.3%)
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
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 7`, `state_mutation: 45`
* *Architecture:* `io: 4`, `api: 37`, `concurrency: 53`, `import: 27`
* *Defense:* `safety: 19`, `doc: 64`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.754
  * `Choke Point (Betweenness):` 0.002484 | `Ripple Effect (Closeness):` 0.253685
  * `Imports (Out-Degree: 9):` actix_codec::AsyncRead, actix_codec::AsyncWrite, actix_codec::Framed, actix_rt::net::TcpStream, actix_service::IntoServiceFactory, actix_service::Service, actix_service::ServiceFactory, actix_service::ServiceFactoryExt...
  * `Imported By (In-Degree: 31):` (Excluded from Brief to save tokens)

### `actix-files/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.396)
- **Top Global Matches:** file_cluster_7: 7.396, file_cluster_5: 9.043, file_cluster_14: 9.988
- **Magnitude:** 340.6 | **LOC:** 1104 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **51**; blast radius 1.04; role: Pure Consumer (Orchestrator)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.04
  * `Choke Point (Betweenness):` 0.000313 | `Ripple Effect (Closeness):` 0.009254
  * `Imports (Out-Degree: 25):` chunked, directory, encoding, error, files, named, path_buf, range...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `actix-web/src/service.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.295)
- **Top Global Matches:** file_cluster_5: 7.295, file_cluster_0: 8.841, file_cluster_12: 9.418
- **Magnitude:** 334.36 | **LOC:** 926 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **53**; blast radius 13.238; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.1%), Connectivity (formerly Api Exposure) (79.1%), Guard Balance (formerly Safety Score) (49.7%), Mutation Surface (formerly State Flux) (18.0%)
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
* *Structure:* `branch: 37`, `structural_boundaries: 170`, `args: 102`, `func_start: 85`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 9`, `planned_debt: 2`
* *Architecture:* `api: 79`, `concurrency: 36`, `import: 10`
* *Defense:* `safety: 4`, `doc: 123`, `test: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.238
  * `Choke Point (Betweenness):` 0.015843 | `Ripple Effect (Closeness):` 0.182198
  * `Imports (Out-Degree: 31):` actix_http::BoxedPayloadStream, actix_http::Extensions, actix_http::HttpMessage, actix_http::Method, actix_http::Payload, actix_http::RequestHead, actix_http::Response, actix_http::ResponseHead...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `awc/src/client/connector.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.374)
- **Top Global Matches:** file_cluster_0: 7.374, file_cluster_5: 9.753, file_cluster_15: 9.941
- **Magnitude:** 325.9 | **LOC:** 1154 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **71**; blast radius 1.57; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.6%), Guard Balance (formerly Safety Score) (51.5%)
- **Documentation Coverage:** 37.6812% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finish` **(Compute Cores)** (Impact: 41.8)
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
* *Structure:* `branch: 67`, `structural_boundaries: 212`, `args: 68`, `func_start: 48`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 25`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 31`, `concurrency: 34`, `import: 34`
* *Defense:* `safety: 5`, `doc: 110`, `test: 3`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.57
  * `Choke Point (Betweenness):` 0.000514 | `Ripple Effect (Closeness):` 0.056874
  * `Imports (Out-Degree: 10):` actix_http::HttpService, actix_http::Protocol, actix_http::Request, actix_http::Response, actix_http::Version, actix_http_test::test_server, actix_rt::net::ActixStream, actix_rt::net::TcpStream...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `actix-http/tests/test_server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_7: 7.912, file_cluster_5: 8.906, file_cluster_14: 10.116
- **Magnitude:** 317.34 | **LOC:** 1024 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **39**; blast radius 0.791; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.2%), Complexity Load (formerly Cognitive Load) (20.0%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `h2_flow_control_window_sizes` **(I/O & Config Routines)** (Impact: 10.2)
  * `content_length_truncated` **(Annotated & Test Methods)** (Impact: 8.7)
  * `chunked_payload` **(Callbacks & Closures)** (Impact: 8.0)
  * `slow_request_408` **(Annotated & Test Methods)** (Impact: 7.8)
  * `not_modified_spec_h1` **(Annotated & Test Methods)** (Impact: 7.0)
    * *Intent:* /// Tests compliance with 304 Not Modified spec in RFC 7232 §4.1. /// https://datatracker.ietf.org/d...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 5
* *Concurrency (weighted view):* 157
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 433`, `args: 97`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 100`, `high_risk_execution: 6`, `state_mutation: 7`, `planned_debt: 3`, `fragile_debt: 1`, `unreferenced_by_name: 29`
* *Architecture:* `concurrency: 152`, `import: 13`
* *Defense:* `safety: 3`, `doc: 2`, `test: 76`, `immutability_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` actix_http::Error, actix_http::HttpService, actix_http::KeepAlive, actix_http::Request, actix_http::Response, actix_http::StatusCode, actix_http::Version, actix_http::body...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-http/src/h1/encoder.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.366)
- **Top Global Matches:** file_cluster_12: 7.366, file_cluster_5: 8.399, file_cluster_0: 8.828
- **Magnitude:** 307.28 | **LOC:** 688 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 1.093; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.6%), Concurrency Surface (formerly Concurrency) (50.1%)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 35`
* *Architecture:* `api: 18`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 8`, `doc: 19`, `test: 25`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.093
  * `Choke Point (Betweenness):` 0.000345 | `Ripple Effect (Closeness):` 0.184475
  * `Imports (Out-Degree: 9):` bytes::BufMut, bytes::Bytes, bytes::BytesMut, crate::ConnectionType, crate::RequestHead, crate::RequestHeadType, crate::Response, crate::ServiceConfig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `actix-http/src/header/map.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.935)
- **Top Global Matches:** file_cluster_5: 6.935, file_cluster_12: 9.105, file_cluster_0: 9.277
- **Magnitude:** 305.92 | **LOC:** 1206 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **15**; blast radius 10.569; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (55.9%), Guard Balance (formerly Safety Score) (46.0%), Debt Markers (formerly Tech Debt) (39.3%)
- **Documentation Coverage:** 50.5263% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 77`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 41`, `import: 9`
* *Defense:* `safety: 11`, `doc: 458`, `test: 88`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.569
  * `Choke Point (Betweenness):` 0.000454 | `Ripple Effect (Closeness):` 0.302913
  * `Imports (Out-Degree: 1):` foldhash::HashMap, foldhash::HashMapExt, http::header, http::header::HeaderName, http::header::HeaderValue, self::*, smallvec::SmallVec, smallvec::smallvec...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `actix-web/src/middleware/logger.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.174)
- **Top Global Matches:** file_cluster_5: 6.174, file_cluster_12: 7.983, file_cluster_0: 9.211
- **Magnitude:** 302.56 | **LOC:** 1031 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **40**; blast radius 1.201; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (57.6%), Guard Balance (formerly Safety Score) (53.3%), Connectivity (formerly Api Exposure) (52.1%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `render_request` **(Many-Argument Workhorses)** (Impact: 24.9)
  * `new` **(Compute Cores)** (Impact: 16.7)
    * *Intent:* /// Create a `Format` from a format string. /// /// Returns `None` if the format string syntax is in...
  * `poll` **(Defensive Guards)** (Impact: 12.7)
  * `call` **(Compute Cores)** (Impact: 10.4)
  * `render` **(Many-Argument Workhorses)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 251`, `args: 52`, `func_start: 34`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 4`, `state_mutation: 19`
* *Architecture:* `api: 26`, `concurrency: 23`, `import: 15`
* *Defense:* `safety: 16`, `doc: 132`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.201
  * `Choke Point (Betweenness):` 0.00047 | `Ripple Effect (Closeness):` 0.120351
  * `Imports (Out-Degree: 10):` actix_service::IntoService, actix_service::Service, actix_service::Transform, actix_utils::future::Ready, actix_utils::future::ok, actix_utils::future::ready, bytes::Bytes, crate::Error...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `actix-web/tests/test_server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.989)
- **Top Global Matches:** file_cluster_5: 7.989, file_cluster_7: 8.125, file_cluster_12: 9.672
- **Magnitude:** 293.62 | **LOC:** 909 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.791; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (79.2%), Complexity Load (formerly Cognitive Load) (23.1%), Dead Code Surface (formerly Dead Code) (9.1%)
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
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 5`, `dead_code: 7`, `unreferenced_by_name: 31`
* *Architecture:* `io: 1`, `concurrency: 139`, `import: 13`
* *Defense:* `test: 71`, `sync_locks: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` utils, actix_web::App, actix_web::Error, actix_web::HttpResponse, actix_web::cookie::Cookie, actix_web::http, actix_web::http::StatusCode, actix_web::http::header...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-web/src/http/header/content_disposition.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.827)
- **Top Global Matches:** file_cluster_5: 6.827, file_cluster_12: 9.093, file_cluster_7: 9.945
- **Magnitude:** 290.88 | **LOC:** 1013 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **16**; blast radius 1.752; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (79.1%), Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (54.7%), Complexity Load (formerly Cognitive Load) (9.7%)
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
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 37`, `dead_code: 1`
* *Architecture:* `api: 45`, `import: 8`
* *Defense:* `safety: 4`, `doc: 194`, `test: 61`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.752
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.14716
  * `Imports (Out-Degree: 2):` crate::http::header, crate::http::header::Charset, crate::http::header::ExtendedValue, crate::http::header::HeaderValue, once_cell::sync::Lazy, regex::Regex, regex_lite::Regex, self::ContentDisposition...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `awc/src/middleware/redirect.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.396)
- **Top Global Matches:** file_cluster_5: 7.396, file_cluster_12: 8.796, file_cluster_7: 9.064
- **Magnitude:** 285.78 | **LOC:** 681 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 1.723; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.9%), Connectivity (formerly Api Exposure) (54.0%)
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
* *Risk/State:* `safety_bypasses: 41`, `high_risk_execution: 1`, `state_mutation: 15`
* *Architecture:* `api: 17`, `concurrency: 49`, `import: 11`
* *Defense:* `safety: 3`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.723
  * `Choke Point (Betweenness):` 0.019298 | `Ripple Effect (Closeness):` 0.037583
  * `Imports (Out-Degree: 15):` actix_http::Method, actix_http::RequestHead, actix_http::RequestHeadType, actix_http::StatusCode, actix_http::Uri, actix_http::header, actix_service::Service, actix_web::App...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `actix-web-actors/src/ws.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.414)
- **Top Global Matches:** file_cluster_5: 7.414, file_cluster_0: 8.598, file_cluster_12: 9.365
- **Magnitude:** 279.44 | **LOC:** 1053 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **50**; blast radius 1.149; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.8%), Concurrency Surface (formerly Concurrency) (63.6%), Guard Balance (formerly Safety Score) (49.2%)
- **Documentation Coverage:** 34.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handshake_with_protocols` **(Defensive Guards)** (Impact: 33.4)
    * *Intent:* /// Prepare WebSocket handshake response. /// /// This function returns handshake `HttpResponse`, re...
  * `poll_next` **(Compute Cores)** (Impact: 23.0)
  * `poll_next` **(Defensive Guards)** (Impact: 22.0)
  * `test_handshake` **(I/O & Config Routines)** (Impact: 9.0)
  * `start_with_protocols` **(Generic / Templated Code)** (Impact: 5.3)
    * *Intent:* /// Do WebSocket handshake and start ws actor. /// /// `protocols` is a sequence of known protocols.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 170`, `args: 48`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 11`
* *Architecture:* `api: 35`, `concurrency: 25`, `import: 13`
* *Defense:* `safety: 12`, `doc: 198`, `test: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.149
  * `Choke Point (Betweenness):` 0.0009 | `Ripple Effect (Closeness):` 0.005141
  * `Imports (Out-Degree: 12):` actix::Actor, actix::ActorContext, actix::ActorState, actix::Addr, actix::AsyncContext, actix::Handler, actix::Message, actix::SpawnHandle...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `actix-web/src/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.081)
- **Top Global Matches:** file_cluster_0: 7.081, file_cluster_5: 8.738, file_cluster_12: 9.195
- **Magnitude:** 275.8 | **LOC:** 926 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **53**; blast radius 1.833; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Connectivity (formerly Api Exposure) (58.0%), Guard Balance (formerly Safety Score) (48.2%), Mutation Surface (formerly State Flux) (48.0%)
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
* *Structure:* `branch: 31`, `structural_boundaries: 194`, `args: 55`, `func_start: 30`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `planned_debt: 3`
* *Architecture:* `api: 28`, `concurrency: 67`, `import: 15`
* *Defense:* `safety: 6`, `doc: 188`, `test: 28`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.833
  * `Choke Point (Betweenness):` 0.000902 | `Ripple Effect (Closeness):` 0.155114
  * `Imports (Out-Degree: 25):` actix_http::Extensions, actix_http::body::MessageBody, actix_router::IntoPatterns, actix_router::Patterns, actix_rt::time::sleep, actix_service::IntoServiceFactory, actix_service::Service, actix_service::ServiceFactory...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `awc/tests/test_client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.771)
- **Top Global Matches:** file_cluster_7: 7.771, file_cluster_5: 9.218, file_cluster_12: 9.733
- **Magnitude:** 267.58 | **LOC:** 841 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 0.791; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (20.2%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` utils, actix_http::HttpService, actix_http::StatusCode, actix_http_test::test_server, actix_service::ServiceFactoryExt, actix_service::fn_service, actix_service::map_config, actix_utils::future::ok...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `actix-files/src/named.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.004)
- **Top Global Matches:** file_cluster_0: 8.004, file_cluster_15: 8.802, file_cluster_13: 8.841
- **Magnitude:** 249.36 | **LOC:** 739 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **44**; blast radius 1.406; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (48.3%), Guard Balance (formerly Safety Score) (46.1%), Concurrency Surface (formerly Concurrency) (35.5%)
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
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 11`
* *Architecture:* `io: 6`, `api: 40`, `concurrency: 9`, `import: 13`
* *Defense:* `safety: 13`, `doc: 132`, `test: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.406
  * `Choke Point (Betweenness):` 0.001198 | `Ripple Effect (Closeness):` 0.017352
  * `Imports (Out-Degree: 18):` actix_web::Error, actix_web::HttpMessage, actix_web::HttpRequest, actix_web::HttpResponse, actix_web::Responder, actix_web::body, actix_web::body::BoxBody, actix_web::body::SizedStream...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `actix-http/tests/test_rustls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.447)
- **Top Global Matches:** file_cluster_5: 7.447, file_cluster_7: 7.973, file_cluster_12: 9.243
- **Magnitude:** 235.82 | **LOC:** 695 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **51**; blast radius 0.791; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (73.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.6%), Complexity Load (formerly Cognitive Load) (23.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` actix_http::Error, actix_http::HttpService, actix_http::Method, actix_http::Request, actix_http::Response, actix_http::StatusCode, actix_http::TlsAcceptorConfig, actix_http::Version...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `actix-web/src/introspection.rs` (RUST) | Magnitude: 586.3 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 975, structural_boundaries: 232, branch: 120, core_var_decl: 106
- `actix-http/src/lib.rs` (RUST) | Magnitude: 18.64 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 34, doc: 29, indent_spaces: 26, api: 15
- `actix-web/src/types/payload.rs` (RUST) | Magnitude: 214.88 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 384, structural_boundaries: 176, doc: 131, core_var_decl: 69
- `actix-http/src/h1/dispatcher_tests.rs` (RUST) | Magnitude: 207.04 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 935, structural_boundaries: 243, core_var_decl: 127, design_snake_case: 113

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `actix-web/benches/server.rs` (RUST) | Magnitude: 12.68 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 16, core_var_decl: 9, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `actix-web/src/test/mod.rs` (RUST) | Magnitude: 10.4 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 34, indent_spaces: 25, structural_boundaries: 17, import: 8
- `actix-http/src/ws/proto.rs` (RUST) | Magnitude: 52.28 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 217, doc: 54, test: 45, core_var_decl: 37
- `actix-files/src/encoding.rs` (RUST) | Magnitude: 15.24 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 9, doc: 9, branch: 6
- `actix-http/examples/actix-web.rs` (RUST) | Magnitude: 8.5 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 7, args: 4, import: 4
- `actix-files/src/error.rs` (RUST) | Magnitude: 5.84 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 19, doc: 10, decorators: 10, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `actix-web-codegen/tests/trybuild/route-custom-method.rs` (RUST) | Magnitude: 13.06 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 16, core_var_decl: 11, design_snake_case: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/labeler.yml` (YAML) | Magnitude: 15.26 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 2, import: 2, immutability_locks: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `actix-http/src/body/mod.rs` (RUST) | Magnitude: 17.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, doc: 3, api: 2
- `actix-web/src/types/mod.rs` (RUST) | Magnitude: 16.4 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 9, api: 1, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `actix-http/src/ws/frame.rs` (RUST) | Magnitude: 187.44 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 330, structural_boundaries: 134, core_var_decl: 61, design_snake_case: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `actix-test/src/lib.rs` (RUST) | Magnitude: 231.22 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 493, structural_boundaries: 162, doc: 126, args: 92
- `actix-web/src/error/response_error.rs` (RUST) | Magnitude: 35.8 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 34, generics: 23, branch: 20
- `actix-http/src/date.rs` (RUST) | Magnitude: 30.44 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 53, structural_boundaries: 27, core_var_decl: 10, design_snake_case: 10
- `actix-web/tests/utils.rs` (RUST) | Magnitude: 27.26 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 49, safety_bypasses: 14, api: 12
- `awc/tests/utils.rs` (RUST) | Magnitude: 27.26 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 49, safety_bypasses: 14, api: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `actix-web/src/introspection.rs` -> **Guillermo Céspedes Tabárez** (100.0% isolated ownership) | Magnitude: 586.3
- `actix-multipart/src/form/mod.rs` -> **fasilmveloor** (100.0% isolated ownership) | Magnitude: 381.32
- `actix-http/src/service.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 348.62
- `actix-web/src/service.rs` -> **Yuki Okushi** (100.0% isolated ownership) | Magnitude: 334.36
- `actix-http/src/h1/encoder.rs` -> **Ali Mirghasemi** (100.0% isolated ownership) | Magnitude: 307.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `actix-web/src/app.rs` -> **Severity: 1.9** (Bridge: 0.028 * Flux: 67.7893%)
- `awc/src/builder.rs` -> **Severity: 1.028** (Bridge: 0.0121 * Flux: 85.0424%)
- `awc/src/middleware/redirect.rs` -> **Severity: 0.605** (Bridge: 0.0193 * Flux: 31.3646%)
- `actix-web/src/dev.rs` -> **Severity: 0.572** (Bridge: 0.0062 * Flux: 91.6827%)
- `actix-web/src/request.rs` -> **Severity: 0.546** (Bridge: 0.023 * Flux: 23.7318%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `actix-http/src/responses/response.rs` -> **Severity: 20.251** (Embedded: 0.3202 * Error Risk: 63.237%)
- `actix-http/src/body/utils.rs` -> **Severity: 19.524** (Embedded: 0.2468 * Error Risk: 79.1071%)
- `actix-http/src/error.rs` -> **Severity: 18.009** (Embedded: 0.3645 * Error Risk: 49.4057%)
- `actix-http/src/responses/head.rs` -> **Severity: 16.533** (Embedded: 0.2816 * Error Risk: 58.7185%)
- `actix-http/src/body/boxed.rs` -> **Severity: 15.965** (Embedded: 0.3093 * Error Risk: 51.6096%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `actix-http/src/error.rs` -> **Severity: 3929.8** (Blast Radius: 39.298 * Doc Risk: 100.0%)
- `actix-http/src/body/message_body.rs` -> **Severity: 2719.24** (Blast Radius: 28.605 * Doc Risk: 95.0617%)
- `actix-http/src/body/boxed.rs` -> **Severity: 2373.811** (Blast Radius: 33.629 * Doc Risk: 70.5882%)
- `actix-http/src/header/as_name.rs` -> **Severity: 1192.1** (Blast Radius: 11.921 * Doc Risk: 100.0%)
- `actix-http/src/body/utils.rs` -> **Severity: 1006.143** (Blast Radius: 14.086 * Doc Risk: 71.4286%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 21089 call pairs -- scoped 13.7%, unique 0.0%, ambiguous 11.9%, external 74.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 21060 | 13.7% | 0.0% | 11.9% | 74.4% |
| shell | 29 | 3.4% | 0.0% | 0.0% | 96.6% |

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
