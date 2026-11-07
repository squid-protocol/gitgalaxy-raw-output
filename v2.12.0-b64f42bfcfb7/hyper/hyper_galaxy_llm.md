# ARCHITECTURAL_BRIEF: hyper
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hyperium/hyper.git` |
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
- **Scope:** 109 analyzed artifact(s), 24806 LOC.
- **Load-bearing artifact:** `src/lib.rs` -- 27 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `tests/server.rs` -- pulls in 68 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/proto/h1/role.rs` at magnitude 1209.16 (structural weight, not risk).
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
| Total Artifacts | 130 |
| Analyzed Artifacts (Scanned) | 109 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 21 |
| Total LOC | 24806 |
| Volatility Index | 0.046 |
| % Scanned of codebase = | 83.8% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4416 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2555 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 33.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.095 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 92 | 23822 | 84.4% |
| MARKDOWN | 7 | 0 | 6.4% |
| YAML | 5 | 380 | 4.6% |
| C | 2 | 538 | 1.8% |
| MAKEFILE | 1 | 15 | 0.9% |
| SHELL | 1 | 41 | 0.9% |
| HTML | 1 | 10 | 0.9% |

## 4.1 SOURCE ENCODINGS
All 109 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Generic / Templated Code Files 24%, Data / Markup / Trivial 21%, Large Core Modules (3) 17%, Encapsulated Accessors Files 10%, State Mutators Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 102 | 93.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 6.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 21*

**Composition by Extension & Reason:**
- `.md`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.toml`: 2x Excluded (Unsupported Extension: '.toml'), 1x Unsupported Format (.toml)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 545 LOC)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 83.9 | 20.0 | 13.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 33.1 | 48.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 14.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.0 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 67.7 | 24.8 | 19.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 47.7 | 49.6 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.1 | 50.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 119 | 34 | 2 | `src/proto/h1/decode.rs` |
| cleanup | 60 | 17 | 2 | `tests/server.rs` |
| guards | 875 | 75 | 22 | `src/proto/h1/role.rs` |
| danger | 1194 | 51 | 14 | `tests/server.rs` |
| concurrency | 1547 | 64 | 25 | `tests/server.rs` |
| connectivity | 1120 | 88 | 30 | `tests/server.rs` |
| io | 445 | 42 | 12 | `tests/server.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 23 | 10 | 0 | `tests/server.rs` |
| time | 16 | 14 | 1 | `src/proto/h1/dispatch.rs` |
| serialization | 2 | 1 | 0 | `examples/web_api.rs` |
| regex | 0 | 0 | 0 | - |
| events | 264 | 27 | 10 | `src/proto/h1/conn.rs` |
| tests | 808 | 36 | 13 | `tests/server.rs` |
| docs | 2683 | 64 | 82 | `src/client/conn/http1.rs` |
| debt | 197 | 53 | 4 | `capi/examples/upload.c` |
| mutation | 3041 | 80 | 54 | `tests/server.rs` |
| dead_code | 77 | 17 | 1 | `benches/end_to_end.rs` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 8 | 2 | 0 | `src/proto/h2/ping.rs` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.875**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/server.rs` (Hits: 63)
- `tests/client.rs` (Hits: 60)
- `benches/support/tokiort.rs` (Hits: 26)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`src/lib.rs`) — 27 inbound connections
2. **mod.rs** (`src/body/mod.rs`) — 22 inbound connections
3. **util.rs** (`src/service/util.rs`) — 20 inbound connections
4. **mod.rs** (`benches/support/mod.rs`) — 19 inbound connections
5. **io.rs** (`src/rt/io.rs`) — 17 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **server.rs** (`tests/server.rs`) — 68 outbound dependencies
2. **client.rs** (`tests/client.rs`) — 64 outbound dependencies
3. **client.rs** (`src/proto/h2/client.rs`) — 47 outbound dependencies
4. **conn.rs** (`src/proto/h1/conn.rs`) — 38 outbound dependencies
5. **role.rs** (`src/proto/h1/role.rs`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `encode_headers` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **178.6** | LOC: 344
- `parse` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **73.6** | LOC: 225
- `poll_write` **(Many-Argument Workhorses)** (@ `src/proto/h1/dispatch.rs`) -> Impact: **72.2** | LOC: 94
- `parse` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **65.6** | LOC: 169
- `main` **(Many-Argument Workhorses)** (@ `capi/examples/upload.c`) -> Impact: **60.2** | LOC: 234
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `main` **(Many-Argument Workhorses)** (@ `capi/examples/client.c`) -> Impact: **53.4** | LOC: 202
  * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
- `poll` **(Many-Argument Workhorses)** (@ `src/proto/h2/client.rs`) -> Impact: **50.9** | LOC: 118
- `set_length` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **48.2** | LOC: 132
- `poll_read` **(Many-Argument Workhorses)** (@ `src/proto/h1/dispatch.rs`) -> Impact: **41.9** | LOC: 75
- `encode` **(Many-Argument Workhorses)** (@ `src/proto/h1/role.rs`) -> Impact: **41.4** | LOC: 101

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/proto/h1` | 7 | 3270.82 | 21.77% | 21.28% |
| `tests` | 3 | 1558.32 | 11.54% | 0.0% |
| `src/proto/h2` | 5 | 862.94 | 18.33% | 14.23% |
| `examples` | 18 | 725.38 | 46.77% | 0.0% |
| `src/ffi` | 8 | 597.12 | 9.45% | 11.02% |
| `src/client/conn` | 3 | 481.6 | 21.69% | 38.52% |
| `src` | 7 | 432.0 | 4.16% | 22.74% |
| `tests/support` | 3 | 343.08 | 20.9% | 0.0% |
| `capi/examples` | 3 | 325.46 | 21.5% | 0.0% |
| `src/server/conn` | 3 | 317.54 | 24.8% | 3.3% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/service/service.rs` -> **100.0%** Exposure
- `src/proto/h1/mod.rs` -> **99.9961%** Exposure
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **99.9608%** Exposure
- `benches/end_to_end.rs` -> **99.4252%** Exposure
- `src/client/conn/http2.rs` -> **98.7807%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/common/buf.rs` -> **100.0%** Exposure
- `capi/gen_header.sh` -> **99.9994%** Exposure
- `src/server/conn/http2.rs` -> **99.5958%** Exposure
- `src/proto/h2/ping.rs` -> **98.1937%** Exposure
- `src/ext/mod.rs` -> **97.2279%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `benches/end_to_end.rs` -> **19** Orphaned Functions | **0** Duplicates
- `src/client/conn/http2.rs` -> **0** Orphaned Functions | **7** Duplicates
- `src/ext/mod.rs` -> **7** Orphaned Functions | **0** Duplicates
- `src/proto/h1/mod.rs` -> **7** Orphaned Functions | **0** Duplicates
- `src/proto/h2/mod.rs` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `1252` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/proto/h1/role.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.23)
- **Top Global Matches:** file_cluster_4: 8.23, file_cluster_12: 9.076, file_cluster_5: 9.773
- **Magnitude:** 1209.16 | **LOC:** 3174 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **38**; blast radius 9.791; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.8%), Guard Balance (formerly Safety Score) (54.5%)
- **Documentation Coverage:** 97.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_headers` **(Many-Argument Workhorses)** (Impact: 178.6)
  * `parse` **(Many-Argument Workhorses)** (Impact: 73.6)
  * `parse` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `set_length` **(Many-Argument Workhorses)** (Impact: 48.2)
  * `encode` **(Many-Argument Workhorses)** (Impact: 41.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 81 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 654`, `args: 103`, `func_start: 86`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 5`, `state_mutation: 132`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 42`, `import: 41`
* *Defense:* `safety: 49`, `doc: 7`, `test: 123`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.791
  * `Choke Point (Betweenness):` 0.009884 | `Ripple Effect (Closeness):` 0.136124
  * `Imports (Out-Degree: 9):` bytes::Bytes, bytes::BytesMut, crate::body::DecodedLength, crate::common::date, crate::error::Kind, crate::error::Parse, crate::ext::HeaderCaseMap, crate::ext::OriginalHeaderOrder...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.226)
- **Top Global Matches:** file_cluster_5: 8.226, file_cluster_7: 9.167, file_cluster_14: 10.212
- **Magnitude:** 966.98 | **LOC:** 3601 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **68**; blast radius 3.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.1%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_test` **(Compute Cores)** (Impact: 15.6)
  * `h2_connect_multiplex` **(I/O & Config Routines)** (Impact: 13.4)
  * `serve` **(Compute Cores)** (Impact: 12.4)
  * `call` **(Defensive Guards)** (Impact: 11.8)
  * `read_until` **(Generic / Templated Code)** (Impact: 11.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 352
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 1200`, `args: 210`, `func_start: 144`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 417`, `high_risk_execution: 8`, `state_mutation: 22`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `io: 63`, `api: 93`, `concurrency: 322`, `import: 42`
* *Defense:* `safety: 7`, `doc: 2`, `test: 239`, `sync_locks: 14`, `immutability_locks: 9`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` support, bytes::Bytes, futures_channel::oneshot, futures_util::StreamExt, futures_util::TryStreamExt, futures_util::future, futures_util::future::Either, futures_util::future::FutureExt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.764)
- **Top Global Matches:** file_cluster_5: 7.764, file_cluster_7: 8.48, file_cluster_12: 9.823
- **Magnitude:** 570.04 | **LOC:** 2930 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **64**; blast radius 3.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Guard Balance (formerly Safety Score) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%), Connectivity (formerly Api Exposure) (55.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_try_send_request` **(I/O & Config Routines)** (Impact: 12.1)
  * `http2_detect_conn_eof` **(I/O & Config Routines)** (Impact: 7.0)
  * `connect_method` **(Annotated & Test Methods)** (Impact: 6.5)
  * `upgrade` **(Annotated & Test Methods)** (Impact: 6.2)
  * `drain_til_eof` **(Generic / Templated Code)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 9
* *Concurrency (weighted view):* 288
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 751`, `args: 132`, `func_start: 51`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 250`, `high_risk_execution: 11`, `state_mutation: 19`
* *Architecture:* `io: 60`, `api: 27`, `concurrency: 263`, `import: 51`
* *Defense:* `safety: 9`, `doc: 2`, `test: 94`, `sync_locks: 1`, `immutability_locks: 4`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` support, bytes::Buf, bytes::Bytes, futures_channel::mpsc, futures_channel::oneshot, futures_util::future, futures_util::future::FutureExt, futures_util::future::TryFuture...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/proto/h1/decode.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.376)
- **Top Global Matches:** file_cluster_5: 6.376, file_cluster_12: 8.515, file_cluster_7: 10.093
- **Magnitude:** 569.64 | **LOC:** 1255 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 6.714; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (82.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `decode` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `read_body` **(Many-Argument Workhorses)** (Impact: 17.4)
  * `test_read_chunk_size` **(Annotated & Test Methods)** (Impact: 14.8)
    * *Intent:* */
  * `read_async` **(Many-Argument Workhorses)** (Impact: 13.7)
    * *Intent:* // perform an async read using a custom buffer size and causing a blocking // read at the specified ...
  * `decode_trailers` **(Compute Cores)** (Impact: 10.7)
    * *Intent:* // TODO: disallow Transfer-Encoding, Content-Length, Trailer, etc in trailers ??
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 142
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 403`, `args: 56`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 1`, `state_mutation: 47`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 24`, `concurrency: 82`, `import: 19`
* *Defense:* `safety: 7`, `doc: 28`, `test: 62`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.714
  * `Choke Point (Betweenness):` 0.000241 | `Ripple Effect (Closeness):` 0.134903
  * `Imports (Out-Degree: 5):` bytes::BufMut, bytes::Bytes, bytes::BytesMut, crate::rt::Read, crate::rt::ReadBuf, futures_core::ready, http::HeaderMap, http::HeaderName...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/proto/h1/conn.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.343)
- **Top Global Matches:** file_cluster_16: 7.343, file_cluster_0: 7.578, file_cluster_15: 8.161
- **Magnitude:** 559.7 | **LOC:** 1532 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **38**; blast radius 9.649; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.7%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 98.4127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_read_head` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `poll_read_body` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `maybe_notify` **(Compute Cores)** (Impact: 17.9)
  * `write_trailers` **(Stateful Encapsulated Methods)** (Impact: 16.8)
  * `require_empty_read` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* // This will check to make sure the io object read is empty. // // This should only be called for Cl...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 22 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 207`, `args: 82`, `func_start: 77`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 6`, `state_mutation: 63`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 46`, `concurrency: 1`, `import: 23`
* *Defense:* `safety: 18`, `doc: 26`, `test: 20`, `immutability_locks: 1`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.649
  * `Choke Point (Betweenness):` 0.009714 | `Ripple Effect (Closeness):` 0.173892
  * `Imports (Out-Degree: 11):` bytes::Buf, bytes::Bytes, crate::body::DecodedLength, crate::common::io::Compat, crate::common::time::Time, crate::headers, crate::proto::BodyLength, crate::proto::MessageHead...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/proto/h1/dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.574)
- **Top Global Matches:** file_cluster_4: 8.574, file_cluster_0: 9.811, file_cluster_5: 10.061
- **Magnitude:** 366.1 | **LOC:** 809 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **31**; blast radius 9.214; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (61.1%), Guard Balance (formerly Safety Score) (51.7%), Mutation Surface (formerly State Flux) (41.6%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_write` **(Many-Argument Workhorses)** (Impact: 72.2)
  * `poll_read` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `poll_inner` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `recv_msg` **(Defensive Guards)** (Impact: 19.4)
  * `poll_read_head` **(Many-Argument Workhorses)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 202`, `args: 46`, `func_start: 35`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 6`, `state_mutation: 14`, `fragile_debt: 1`
* *Architecture:* `api: 15`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 17`, `doc: 7`, `test: 13`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.214
  * `Choke Point (Betweenness):` 0.020544 | `Ripple Effect (Closeness):` 0.172893
  * `Imports (Out-Degree: 12):` bytes::Buf, bytes::Bytes, crate::body::Body, crate::body::DecodedLength, crate::body::Incoming, crate::client::dispatch::TrySendError, crate::common::io::Compat, crate::common::task...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/proto/h1/io.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.143)
- **Top Global Matches:** file_cluster_0: 7.143, file_cluster_16: 9.032, file_cluster_13: 9.151
- **Magnitude:** 352.28 | **LOC:** 968 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **24**; blast radius 11.396; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.0%), Guard Balance (formerly Safety Score) (50.4%), Connectivity (formerly Api Exposure) (40.7%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_flush` **(Stateful Encapsulated Methods)** (Impact: 24.3)
  * `parse` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `record` **(Compute Cores)** (Impact: 15.5)
  * `poll_flush_flattened` **(Compute Cores)** (Impact: 13.0)
    * *Intent:* /// Specialized version of `flush` when strategy is Flatten. /// /// Since all buffered bytes are fl...
  * `buffer` **(Stateful Encapsulated Methods)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 181`, `args: 64`, `func_start: 61`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 30`, `dead_code: 13`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 39`, `concurrency: 8`, `import: 15`
* *Defense:* `safety: 2`, `doc: 25`, `test: 51`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.396
  * `Choke Point (Betweenness):` 0.003243 | `Ripple Effect (Closeness):` 0.136742
  * `Imports (Out-Degree: 4):` bytes::Buf, bytes::BufMut, bytes::Bytes, bytes::BytesMut, crate::common::buf::BufList, crate::common::io::Compat, crate::proto::h1::ClientTransaction, crate::rt::Read...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/client/conn/http2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.375)
- **Top Global Matches:** file_cluster_5: 7.375, file_cluster_0: 8.54, file_cluster_12: 10.185
- **Magnitude:** 291.22 | **LOC:** 712 | **CtrlFlow:** 4.9% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 5.842; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 33.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_send_request` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `send_request` **(Generic / Templated Code)** (Impact: 6.3)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `poll_ready` **(Generic / Templated Code)** (Impact: 5.5)
    * *Intent:* /// Polls to determine whether this sender can be used yet for a request. /// /// If the associated ...
  * `poll` **(Generic / Templated Code)** (Impact: 5.5)
  * `handshake` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* /// Constructs a connection with the configured options and IO. /// See [`client::conn`](crate::clie...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 82
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 152`, `args: 48`, `func_start: 47`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 20`, `fragile_debt: 2`, `duplicate_logic: 7`
* *Architecture:* `api: 39`, `concurrency: 72`, `import: 18`
* *Defense:* `safety: 3`, `doc: 187`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.842
  * `Choke Point (Betweenness):` 0.00205 | `Ripple Effect (Closeness):` 0.117056
  * `Imports (Out-Degree: 8):` crate::body::Body, crate::body::Incoming, crate::common::time::Time, crate::proto, crate::rt::Read, crate::rt::Timer, crate::rt::Write, crate::rt::bounds::Http2ClientConnExec...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/proto/h2/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.363)
- **Top Global Matches:** file_cluster_0: 9.363, file_cluster_5: 9.736, file_cluster_4: 10.259
- **Magnitude:** 247.58 | **LOC:** 792 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **47**; blast radius 9.752; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Concurrency Surface (formerly Concurrency) (93.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%)
- **Documentation Coverage:** 93.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Many-Argument Workhorses)** (Impact: 50.9)
  * `poll` **(Generic / Templated Code)** (Impact: 13.0)
  * `poll_pipe` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `handshake` **(Many-Argument Workhorses)** (Impact: 12.6)
  * `new_builder` **(Defensive Guards)** (Impact: 9.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 181`, `args: 25`, `func_start: 19`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `concurrency: 40`, `import: 24`
* *Defense:* `safety: 14`, `doc: 5`, `immutability_locks: 6`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 9.752
  * `Choke Point (Betweenness):` 0.017035 | `Ripple Effect (Closeness):` 0.155069
  * `Imports (Out-Degree: 15):` bytes::Bytes, crate::Request, crate::Response, crate::body::Body, crate::body::Incoming, crate::client::dispatch::Callback, crate::client::dispatch::SendWhen, crate::client::dispatch::TrySendError...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/support/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.04)
- **Top Global Matches:** file_cluster_6: 11.04, file_cluster_4: 14.002, file_cluster_8: 17.871
- **Magnitude:** 237.38 | **LOC:** 594 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **29**; blast radius 7.847; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (61.1%), Complexity Load (formerly Cognitive Load) (42.2%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `async_test` **(Compute Cores)** (Impact: 32.0)
  * `naive_proxy` **(Compute Cores)** (Impact: 20.4)
  * `__run_test` **(Parameter Forwarders)** (Impact: 1.6)
  * `default` **(State Mutators)** (Impact: 1.4)
  * `default` **(State Mutators)** (Impact: 1.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 114
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 152`, `args: 15`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 5`, `state_mutation: 11`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 59`, `import: 13`
* *Defense:* `safety: 5`, `test: 14`, `sync_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.847
  * `Choke Point (Betweenness):` 0.00592 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 6):` tokiort, trailers, bytes::Bytes, futures_util::FutureExt, futures_util::StreamExt, futures_util::TryFutureExt, futures_util::TryStreamExt, futures_util::future...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/proto/h2/ping.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.415)
- **Top Global Matches:** file_cluster_5: 7.415, file_cluster_12: 7.517, file_cluster_0: 8.829
- **Magnitude:** 225.38 | **LOC:** 515 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 14.134; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.3%), Connectivity (formerly Api Exposure) (28.0%)
- **Documentation Coverage:** 91.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Defensive Guards)** (Impact: 18.5)
  * `calculate` **(Many-Argument Workhorses)** (Impact: 18.1)
  * `record_data` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `maybe_ping` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `maybe_schedule` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 115`, `args: 26`, `func_start: 23`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 22`, `fragile_debt: 2`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 11`, `doc: 44`, `test: 1`, `sync_locks: 8`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.134
  * `Choke Point (Betweenness):` 0.001356 | `Ripple Effect (Closeness):` 0.20202
  * `Imports (Out-Degree: 2):` crate::common::time::Time, crate::rt::Sleep, h2::Ping, h2::PingPong, std::fmt, std::future::Future, std::pin::Pin, std::sync::Arc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ffi/http_types.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.556)
- **Top Global Matches:** file_cluster_15: 6.556, file_cluster_16: 7.334, file_cluster_12: 7.344
- **Magnitude:** 212.8 | **LOC:** 707 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **23**; blast radius 7.753; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (71.5%), Connectivity (formerly Api Exposure) (49.7%), Guard Balance (formerly Safety Score) (49.0%)
- **Documentation Coverage:** 34.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hyper_headers_foreach` **(Many-Argument Workhorses)** (Impact: 30.9)
    * *Intent:* /// Iterates the headers passing each name and value pair to the callback. /// /// The `userdata` po...
  * `hyper_request_set_uri_parts` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /// Set the URI of the request with separate scheme, authority, and /// path/query strings. /// /// ...
  * `raw_name_value` **(Many-Argument Workhorses)** (Impact: 7.7)
  * `hyper_headers_set` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /// Sets the header with the provided name to the provided value. /// /// This overwrites any previo...
  * `hyper_headers_add` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* /// Adds the provided value to the list of the provided name. /// /// If there were already existing...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 165`, `args: 32`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 25`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 30`, `import: 14`
* *Defense:* `safety: 9`, `doc: 159`, `test: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.753
  * `Choke Point (Betweenness):` 0.019508 | `Ripple Effect (Closeness):` 0.146748
  * `Imports (Out-Degree: 8):` bytes::Bytes, crate::HeaderMap, crate::Method, crate::Request, crate::Response, crate::Uri, crate::body::Incoming, crate::ext::HeaderCaseMap...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/proto/h1/encode.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.975)
- **Top Global Matches:** file_cluster_5: 6.975, file_cluster_12: 8.244, file_cluster_0: 9.331
- **Magnitude:** 184.76 | **LOC:** 673 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **31**; blast radius 8.78; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.5%), Mutation Surface (formerly State Flux) (36.1%), Connectivity (formerly Api Exposure) (34.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encode_trailers` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `encode` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `encode_and_end` **(Stateful Encapsulated Methods)** (Impact: 8.2)
  * `advance` **(Parameter Forwarders)** (Impact: 4.0)
  * `chunks_vectored` **(Generic / Templated Code)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 159`, `args: 43`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 19`
* *Architecture:* `io: 2`, `api: 25`, `import: 15`
* *Defense:* `safety: 1`, `doc: 9`, `test: 33`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.78
  * `Choke Point (Betweenness):` 0.000284 | `Ripple Effect (Closeness):` 0.136124
  * `Imports (Out-Degree: 2):` bytes::Buf, bytes::BufMut, bytes::Bytes, bytes::buf::Chain, bytes::buf::Take, http::HeaderMap, http::HeaderName, http::HeaderValue...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/error.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.24)
- **Top Global Matches:** file_cluster_0: 7.24, file_cluster_13: 7.604, file_cluster_16: 8.635
- **Magnitude:** 182.52 | **LOC:** 703 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 22.08; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.1%), Connectivity (formerly Api Exposure) (44.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.9%)
- **Documentation Coverage:** 77.2277% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `find_source` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `description` **(Annotated & Test Methods)** (Impact: 4.8)
  * `new_h2` **(Stateful Encapsulated Methods)** (Impact: 4.6)
  * `fmt` **(Defensive Guards)** (Impact: 3.9)
  * `from` **(State Mutators)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 50`, `args: 62`, `func_start: 59`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `io: 3`, `api: 53`, `concurrency: 4`, `import: 4`
* *Defense:* `safety: 4`, `doc: 75`, `test: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 22.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.229031
  * `Imports (Out-Degree: 0):` self::*, std::error::Error, std::fmt, std::mem
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/client/dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.257)
- **Top Global Matches:** file_cluster_5: 6.257, file_cluster_12: 9.887, file_cluster_7: 10.892
- **Magnitude:** 179.6 | **LOC:** 528 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **18**; blast radius 11.476; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.3%), Guard Balance (formerly Safety Score) (57.3%)
- **Documentation Coverage:** 87.8788% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `giver_queue_throughput` **(Generic / Templated Code)** (Impact: 8.2)
  * `poll` **(Generic / Templated Code)** (Impact: 6.8)
  * `drop` **(Defensive Guards)** (Impact: 6.5)
  * `can_send` **(Compute Cores)** (Impact: 6.3)
  * `try_send` **(Encapsulated Accessors)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 162`, `args: 50`, `func_start: 36`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 3`, `state_mutation: 1`, `fragile_debt: 1`
* *Architecture:* `api: 40`, `concurrency: 21`, `import: 12`
* *Defense:* `safety: 3`, `doc: 36`, `test: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.476
  * `Choke Point (Betweenness):` 0.021999 | `Ripple Effect (Closeness):` 0.182323
  * `Imports (Out-Degree: 3):` crate::Request, crate::Response, crate::body::Incoming, crate::proto::h2::client::ResponseFutMap, http::Request, http::Response, http_body::Body, pin_project_lite::pin_project...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/body/incoming.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.456)
- **Top Global Matches:** file_cluster_5: 7.456, file_cluster_12: 7.902, file_cluster_0: 9.451
- **Magnitude:** 177.78 | **LOC:** 633 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **25**; blast radius 29.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (78.0%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (35.9%), Mutation Surface (formerly State Flux) (14.9%)
- **Documentation Coverage:** 83.6364% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_frame` **(Compute Cores)** (Impact: 18.5)
  * `h2` **(Stateful Encapsulated Methods)** (Impact: 7.0)
  * `size_hint` **(Annotated & Test Methods)** (Impact: 6.8)
  * `new_channel` **(Stateful Encapsulated Methods)** (Impact: 6.4)
  * `as_ffi_mut` **(Stateful Encapsulated Methods)** (Impact: 4.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 136`, `args: 37`, `func_start: 32`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 6`, `state_mutation: 5`
* *Architecture:* `api: 24`, `concurrency: 21`, `import: 18`
* *Defense:* `safety: 5`, `doc: 46`, `test: 31`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.592
  * `Choke Point (Betweenness):` 0.010694 | `Ripple Effect (Closeness):` 0.270853
  * `Imports (Out-Degree: 4):` bytes::Bytes, crate::common::watch, crate::proto::h2::ping, futures_channel::mpsc, futures_channel::oneshot, futures_core::Stream, futures_core::ready, futures_core::stream::FusedStream...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/proto/h2/server.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.227)
- **Top Global Matches:** file_cluster_0: 8.227, file_cluster_9: 9.376, file_cluster_16: 10.271
- **Magnitude:** 174.88 | **LOC:** 551 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **37**; blast radius 7.314; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (80.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.1%), Connectivity (formerly Api Exposure) (29.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_server` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `poll2` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `new` **(Many-Argument Workhorses)** (Impact: 17.3)
  * `poll` **(Compute Cores)** (Impact: 17.3)
  * `poll_ping` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 135`, `args: 13`, `func_start: 9`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`
* *Architecture:* `api: 18`, `concurrency: 22`, `import: 25`
* *Defense:* `safety: 13`, `test: 2`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.314
  * `Choke Point (Betweenness):` 0.013259 | `Ripple Effect (Closeness):` 0.149668
  * `Imports (Out-Degree: 15):` bytes::Bytes, crate::Response, crate::body::Body, crate::body::Incoming, crate::common::date, crate::common::io::Compat, crate::common::time::Time, crate::ext::Protocol...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/client/conn/http1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.239)
- **Top Global Matches:** file_cluster_0: 7.239, file_cluster_5: 8.309, file_cluster_12: 9.873
- **Magnitude:** 174.78 | **LOC:** 612 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 5.842; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.4%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handshake` **(Defensive Guards)** (Impact: 21.8)
    * *Intent:* /// Constructs a connection with the configured options and IO. /// See [`client::conn`](crate::clie...
  * `try_send_request` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /// Sends a `Request` on the associated connection. /// /// Returns a future that if successful, yie...
  * `send_request` **(Generic / Templated Code)** (Impact: 6.2)
    * *Intent:* /// Returns a future that if successful, yields the `Response`. /// /// `req` must have a `Host` hea...
  * `poll` **(Generic / Templated Code)** (Impact: 5.8)
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 111`, `args: 30`, `func_start: 28`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 2`, `state_mutation: 10`, `fragile_debt: 2`
* *Architecture:* `api: 32`, `concurrency: 38`, `import: 15`
* *Defense:* `safety: 4`, `doc: 214`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.842
  * `Choke Point (Betweenness):` 0.001423 | `Ripple Effect (Closeness):` 0.117056
  * `Imports (Out-Degree: 6):` bytes::Bytes, crate::body::Body, crate::body::Incoming, crate::proto, crate::rt::Read, crate::rt::Write, crate::upgrade::Upgraded, futures_core::ready...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `capi/examples/upload.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.686)
- **Top Global Matches:** file_cluster_4: 8.686, file_cluster_6: 8.964, file_cluster_12: 14.524
- **Magnitude:** 171.56 | **LOC:** 401 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.988; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.9%), Complexity Load (formerly Cognitive Load) (29.4%), Connectivity (formerly Api Exposure) (2.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 60.2)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` **(C Struct Operations)** (Impact: 12.2)
  * `read_cb` **(C Struct Operations)** (Impact: 9.9)
  * `write_cb` **(C Struct Operations)** (Impact: 9.9)
  * `poll_req_upload` **(C Struct Operations)** (Impact: 7.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 16 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 62`, `args: 11`, `func_start: 8`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 21`, `unreferenced_by_name: 1`
* *Architecture:* `io: 6`, `api: 4`, `import: 12`
* *Defense:* `safety: 11`, `immutability_locks: 10`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, errno.h, fcntl.h, hyper.h, netdb.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/conn/http1.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.822)
- **Top Global Matches:** file_cluster_0: 6.822, file_cluster_5: 8.575, file_cluster_12: 9.553
- **Magnitude:** 170.32 | **LOC:** 560 | **CtrlFlow:** 6.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **20**; blast radius 16.757; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.0%), Guard Balance (formerly Safety Score) (44.7%)
- **Documentation Coverage:** 10.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `serve_connection` **(Many-Argument Workhorses)** (Impact: 26.5)
    * *Intent:* /// # I: Read + Write + Unpin + Send + 'static, /// # S: Service<hyper::Request<Incoming>, Response=...
  * `poll` **(Generic / Templated Code)** (Impact: 7.7)
  * `poll` **(Generic / Templated Code)** (Impact: 6.1)
  * `without_shutdown` **(Generic / Templated Code)** (Impact: 3.2)
    * *Intent:* /// Prevent shutdown of the underlying IO object at the end of service the request, /// instead run ...
  * `graceful_shutdown` **(Defensive Guards)** (Impact: 3.2)
    * *Intent:* /// Start a graceful shutdown process for this connection. /// /// This `Connection` should continue...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 97`, `args: 27`, `func_start: 25`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 11`
* *Architecture:* `api: 30`, `concurrency: 29`, `import: 15`
* *Defense:* `safety: 6`, `doc: 208`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.757
  * `Choke Point (Betweenness):` 0.021238 | `Ripple Effect (Closeness):` 0.136124
  * `Imports (Out-Degree: 8):` bytes::Bytes, crate::body::Body, crate::body::Incoming, crate::common::time::Dur, crate::common::time::Time, crate::proto, crate::rt::Read, crate::rt::Timer...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/ffi/task.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_5: 7.729, file_cluster_0: 8.91, file_cluster_12: 8.924
- **Magnitude:** 160.42 | **LOC:** 550 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 13.986; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (89.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.8%), Guard Balance (formerly Safety Score) (47.1%)
- **Documentation Coverage:** 50.9434% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll_next` **(Compute Cores)** (Impact: 11.6)
  * `hyper_task_value` **(Defensive Guards)** (Impact: 7.8)
    * *Intent:* /// Takes the output value of this task. /// /// This must only be called once polling the task on a...
  * `drain_queue` **(Compute Cores)** (Impact: 4.9)
    * *Intent:* /// drain_queue locks both self.spawn_queue and self.driver, so it requires /// that neither of them...
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
  * `hyper_task_set_userdata` **(Parameter Forwarders)** (Impact: 3.8)
    * *Intent:* /// Set a user data pointer to be associated with this task. /// /// This value will be passed to ta...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 92`, `args: 31`, `func_start: 31`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 6`
* *Architecture:* `api: 30`, `concurrency: 26`, `import: 9`
* *Defense:* `safety: 5`, `doc: 188`, `sync_locks: 10`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.986
  * `Choke Point (Betweenness):` 0.000216 | `Ripple Effect (Closeness):` 0.148927
  * `Imports (Out-Degree: 2):` futures_util::stream::FuturesUnordered, futures_util::stream::Stream, std::ffi::c_int, std::ffi::c_void, std::future::Future, std::pin::Pin, std::ptr, std::sync::Arc...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `benches/end_to_end.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.049)
- **Top Global Matches:** file_cluster_5: 7.049, file_cluster_12: 8.595, file_cluster_0: 10.128
- **Magnitude:** 151.14 | **LOC:** 452 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 3.988; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.4%), Concurrency Surface (formerly Concurrency) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bench` **(Many-Argument Workhorses)** (Impact: 38.8)
  * `spawn_server` **(Defensive Guards)** (Impact: 12.8)
  * `request_chunks` **(Generic / Templated Code)** (Impact: 2.3)
  * `http2_parallel_x10_req_10mb` **(Generic / Templated Code)** (Impact: 2.0)
  * `http2_parallel_x10_req_10kb_100_chunks_adaptive_window` **(Generic / Templated Code)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 130`, `args: 39`, `func_start: 31`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 11`, `planned_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `io: 16`, `concurrency: 25`, `import: 11`
* *Defense:* `safety: 6`, `test: 6`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` support, futures_util::SinkExt, futures_util::future::join_all, http_body_util::BodyExt, http_body_util::Full, hyper::Method, hyper::Request, hyper::Response...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `capi/examples/client.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.106)
- **Top Global Matches:** file_cluster_6: 8.106, file_cluster_4: 9.71, file_cluster_16: 16.123
- **Magnitude:** 149.1 | **LOC:** 344 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 3.988; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.4%), Complexity Load (formerly Cognitive Load) (35.1%), Connectivity (formerly Api Exposure) (1.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 53.4)
    * *Intent:* #define STR_ARG(XX) (uint8_t *)XX, strlen(XX)
  * `connect_to` **(C Struct Operations)** (Impact: 12.2)
  * `read_cb` **(C Struct Operations)** (Impact: 9.9)
  * `write_cb` **(C Struct Operations)** (Impact: 9.9)
  * `free_conn_data` **(Stateful Encapsulated Methods)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 14 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 47`, `args: 10`, `func_start: 7`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 18`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 3`, `import: 12`
* *Defense:* `safety: 13`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.988
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, errno.h, fcntl.h, hyper.h, netdb.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/single_threaded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.084)
- **Top Global Matches:** file_cluster_5: 8.084, file_cluster_7: 9.584, file_cluster_14: 10.279
- **Magnitude:** 136.84 | **LOC:** 384 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **23**; blast radius 4.23; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (39.8%), Complexity Load (formerly Cognitive Load) (34.8%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `http1_client` **(Defensive Guards)** (Impact: 16.9)
  * `http2_client` **(Defensive Guards)** (Impact: 16.9)
  * `main` **(I/O & Config Routines)** (Impact: 8.3)
  * `http2_server` **(I/O & Config Routines)** (Impact: 7.2)
  * `http1_server` **(I/O & Config Routines)** (Impact: 6.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 171`, `args: 20`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 38`
* *Architecture:* `io: 24`, `api: 7`, `concurrency: 52`, `import: 17`
* *Defense:* `safety: 10`, `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.23
  * `Choke Point (Betweenness):` 0.000827 | `Ripple Effect (Closeness):` 0.009259
  * `Imports (Out-Degree: 6):` mod.rs, http_body_util::BodyExt, hyper::Error, hyper::Request, hyper::Response, hyper::body::Body, hyper::body::Bytes, hyper::body::Frame...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/server/conn/http2.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.974)
- **Top Global Matches:** file_cluster_0: 5.974, file_cluster_15: 10.496, file_cluster_13: 10.723
- **Magnitude:** 133.14 | **LOC:** 313 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **20**; blast radius 9.565; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Connectivity (formerly Api Exposure) (64.6%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 10.5263% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `poll` **(Generic / Templated Code)** (Impact: 4.0)
  * `adaptive_window` **(Parameter Forwarders)** (Impact: 4.0)
    * *Intent:* /// Sets whether to use an adaptive flow control. /// /// Enabling this will override the limits set...
  * `initial_stream_window_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the [`SETTINGS_INITIAL_WINDOW_SIZE`][spec] option for HTTP2 /// stream-level flow control. ...
  * `initial_connection_window_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the max connection-level flow control for HTTP2. /// /// Passing `None` will do nothing. //...
  * `max_frame_size` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /// Sets the maximum frame size to use for HTTP2. /// /// Passing `None` will do nothing. /// /// If...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 29
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 75`, `args: 19`, `func_start: 19`, `class_start: 2`
* *Risk/State:* `state_mutation: 18`, `planned_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 3`, `doc: 108`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.565
  * `Choke Point (Betweenness):` 0.010364 | `Ripple Effect (Closeness):` 0.119378
  * `Imports (Out-Degree: 8):` crate::body::Body, crate::body::Incoming, crate::common::time::Time, crate::proto, crate::rt::Read, crate::rt::Timer, crate::rt::Write, crate::rt::bounds::Http2ServerConnExec...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/trace.rs` (RUST) | Magnitude: 17.28 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 87, decorators: 13, reflection_metaprogramming: 11, macros: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/proto/h2/ping.rs` (RUST) | Magnitude: 225.38 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 314, structural_boundaries: 115, branch: 49, doc: 44

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/client/conn/http2.rs` -> Churn: **100.0%** | Cog Load: 41.7635% | Debt: 98.7807%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/proto/h1/decode.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 569.64
- `src/proto/h2/ping.rs` -> **Ariel Ben-Yehuda** (100.0% isolated ownership) | Magnitude: 225.38
- `src/ffi/http_types.rs` -> **Dhruva D** (100.0% isolated ownership) | Magnitude: 212.8
- `src/proto/h1/encode.rs` -> **HueCodes** (100.0% isolated ownership) | Magnitude: 184.76
- `src/body/incoming.rs` -> **Sean McArthur** (100.0% isolated ownership) | Magnitude: 177.78

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/ffi/http_types.rs` -> **Severity: 1.395** (Bridge: 0.0195 * Flux: 71.4869%)
- `src/server/conn/http2.rs` -> **Severity: 1.032** (Bridge: 0.0104 * Flux: 99.5958%)
- `src/proto/h2/mod.rs` -> **Severity: 0.961** (Bridge: 0.0172 * Flux: 55.7028%)
- `src/proto/h1/role.rs` -> **Severity: 0.872** (Bridge: 0.0099 * Flux: 88.2259%)
- `src/proto/h1/conn.rs` -> **Severity: 0.862** (Bridge: 0.0097 * Flux: 88.7028%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/common/time.rs` -> **Severity: 15.35** (Embedded: 0.2326 * Error Risk: 65.9822%)
- `src/body/incoming.rs` -> **Severity: 14.52** (Embedded: 0.2709 * Error Risk: 53.6086%)
- `src/rt/io.rs` -> **Severity: 12.701** (Embedded: 0.2825 * Error Risk: 44.9614%)
- `src/upgrade.rs` -> **Severity: 11.989** (Embedded: 0.236 * Error Risk: 50.8069%)
- `src/proto/h2/ping.rs` -> **Severity: 11.372** (Embedded: 0.202 * Error Risk: 56.2904%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/body/mod.rs` -> **Severity: 3126.4** (Blast Radius: 31.264 * Doc Risk: 100.0%)
- `src/body/incoming.rs` -> **Severity: 2474.968** (Blast Radius: 29.592 * Doc Risk: 83.6364%)
- `src/rt/io.rs` -> **Severity: 2392.494** (Blast Radius: 44.432 * Doc Risk: 53.8462%)
- `src/proto/h1/mod.rs` -> **Severity: 1980.3** (Blast Radius: 19.803 * Doc Risk: 100.0%)
- `src/proto/mod.rs` -> **Severity: 1754.6** (Blast Radius: 17.546 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 43 literal sites + 2 sites through wrappers = 45

- `free_conn_data` (function, memory_alloc, primitive): 1 call sites in 1 files -- `capi/examples/client.c`
- `free_conn_data` (function, memory_alloc, primitive): 1 call sites in 1 files -- `capi/examples/upload.c`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 7209 call pairs -- scoped 17.1%, unique 0.0%, ambiguous 9.9%, external 72.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 7055 | 17.4% | 0.0% | 10.1% | 72.4% |
| c | 144 | 2.8% | 0.0% | 0.0% | 97.2% |
| shell | 10 | 10.0% | 0.0% | 0.0% | 90.0% |

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
