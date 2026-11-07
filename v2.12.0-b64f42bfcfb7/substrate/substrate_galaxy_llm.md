# ARCHITECTURAL_BRIEF: substrate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/paritytech/substrate.git` |
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
- **Scope:** 2040 analyzed artifact(s), 410326 LOC.
- **Load-bearing artifact:** `primitives/runtime/src/traits.rs` -- 645 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `frame/support/src/lib.rs` -- pulls in 203 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `client/network/sync/src/lib.rs` at magnitude 1592.6 (structural weight, not risk).
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
| Total Artifacts | 2683 |
| Analyzed Artifacts (Scanned) | 2040 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 643 |
| Total LOC | 410326 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 76.0% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4807 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1593 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 47.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3511 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 62 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1790 | 403775 | 87.7% |
| MARKDOWN | 186 | 0 | 9.1% |
| YAML | 23 | 1930 | 1.1% |
| JSON | 14 | 3601 | 0.7% |
| SHELL | 12 | 515 | 0.6% |
| PROTO | 5 | 142 | 0.2% |
| DOCKERFILE | 3 | 73 | 0.1% |
| HTML | 3 | 220 | 0.1% |
| PLAINTEXT | 2 | 0 | 0.1% |
| PYTHON | 1 | 27 | 0.0% |
| JAVASCRIPT | 1 | 43 | 0.0% |

## 4.1 SOURCE ENCODINGS
All 2040 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 28%, Generic / Templated Code Files 26%, Data / Markup / Trivial 16%, Large Core Modules (3) 11%, Declarative / Non-Code 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1848 | 90.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 188 | 9.2% |
| Static: Minified & Vendor Opaque Mass | 4 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 643*

**Composition by Extension & Reason:**
- `.toml`: 268x Unsupported Format (.toml), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 6x Excluded (Unsupported Extension: '.toml')
- `.stderr`: 225x Excluded (Unsupported Extension: '.stderr')
- `.wat`: 49x Excluded (Unsupported Extension: '.wat'), 1x Excluded (Embedded Hex Payload: 4488 hex tokens in 2294 LOC)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Binary Format Detected), 3x Unsupported Format (.undeterminable)
- `.rs`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3927 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1461 LOC)
- `.md`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wasm`: 5x Excluded (Unsupported Extension: '.wasm')
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 4x Excluded (Binary Format Detected)
- `.zndsl`: 4x Excluded (Unsupported Extension: '.zndsl')
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.adoc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ejs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hbs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 6.3 | 4.8 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.8 | 29.2 | 44.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 39.9 | 42.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 64.6 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 56.6 | 62.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3692 | 577 | 5 | `frame/contracts/src/benchmarking/mod.rs` |
| cleanup | 182 | 75 | 0 | `frame/collective/src/tests.rs` |
| guards | 8437 | 995 | 11 | `frame/contracts/src/wasm/mod.rs` |
| danger | 10336 | 784 | 11 | `client/db/src/lib.rs` |
| concurrency | 5025 | 365 | 4 | `client/rpc-spec-v2/src/chain_head/tests.rs` |
| connectivity | 24149 | 1644 | 33 | `bin/node/runtime/src/lib.rs` |
| io | 335 | 84 | 0 | `scripts/ci/common/lib.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 74 | 39 | 0 | `client/authority-discovery/src/worker/tests.rs` |
| time | 128 | 61 | 0 | `client/network/src/protocol/notifications/behaviour.rs` |
| serialization | 162 | 35 | 0 | `client/rpc-spec-v2/src/chain_head/event.rs` |
| regex | 28 | 14 | 0 | `scripts/ci/common/lib.sh` |
| events | 2027 | 334 | 2 | `client/network/src/protocol/notifications/behaviour.rs` |
| tests | 21575 | 795 | 23 | `frame/staking/src/tests.rs` |
| docs | 67695 | 1417 | 91 | `frame/support/src/lib.rs` |
| debt | 1300 | 367 | 2 | `frame/support/src/storage/mod.rs` |
| mutation | 51483 | 1371 | 71 | `bin/node/runtime/src/lib.rs` |
| dead_code | 925 | 385 | 1 | `frame/contracts/src/wasm/mod.rs` |
| credential | 84 | 8 | 0 | `scripts/ci/common/lib.sh` |
| threat | 5 | 4 | 0 | `utils/frame/remote-externalities/src/lib.rs` |
| ml_ai | 280 | 59 | 0 | `frame/benchmarking/src/analysis.rs` |
| ui | 4 | 1 | 0 | `scripts/ci/gitlab/check_runtime.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/ci/common/lib.sh` (Hits: 42)
- `client/offchain/src/api/http.rs` (Hits: 40)
- `scripts/ci/gitlab/check_runtime.sh` (Hits: 21)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **traits.rs** (`primitives/runtime/src/traits.rs`) — 645 inbound connections
2. **lib.rs** (`primitives/std/src/lib.rs`) — 580 inbound connections
3. **lib.rs** (`frame/support/src/lib.rs`) — 463 inbound connections
4. **lib.rs** (`primitives/runtime/src/lib.rs`) — 338 inbound connections
5. **lib.rs** (`frame/system/src/lib.rs`) — 269 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`frame/support/src/lib.rs`) — 203 outbound dependencies
2. **traits.rs** (`frame/support/src/traits.rs`) — 196 outbound dependencies
3. **lib.rs** (`bin/node/runtime/src/lib.rs`) — 154 outbound dependencies
4. **lib.rs** (`client/network/sync/src/lib.rs`) — 131 outbound dependencies
5. **client.rs** (`client/service/src/client/client.rs`) — 122 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `execute_and_import_block` **(Many-Argument Workhorses)** (@ `client/service/src/client/client.rs`) -> Impact: **251.9** | LOC: 248
- `on_connection_handler_event` **(Many-Argument Workhorses)** (@ `client/network/src/protocol/notifications/behaviour.rs`) -> Impact: **171.7** | LOC: 528
- `try_commit_operation` **(Many-Argument Workhorses)** (@ `client/db/src/lib.rs`) -> Impact: **134.0** | LOC: 325
- `on_swarm_event` **(Many-Argument Workhorses)** (@ `client/network/src/protocol/notifications/behaviour.rs`) -> Impact: **118.4** | LOC: 429
- `parse` **(Compute Cores)** (@ `frame/support/procedural/src/storage_alias.rs`) -> Impact: **116.2** | LOC: 90
- `handle_swarm_event` **(Many-Argument Workhorses)** (@ `client/network/src/service.rs`) -> Impact: **114.8** | LOC: 426
  * *Intent:* /// Process the next event coming from `Swarm`.
- `run` **(Many-Argument Workhorses)** (@ `utils/frame/benchmarking-cli/src/pallet/command.rs`) -> Impact: **109.9** | LOC: 362
  * *Intent:* /// Runs the command and benchmarks the chain.
- `reduce_all` **(Compute Cores)** (@ `primitives/npos-elections/src/reduce.rs`) -> Impact: **107.2** | LOC: 333
  * *Intent:* /// Reduce redundant edges from the edge weight graph, with all possible length. /// /// To get the best performance, this should be called after `red...
- `on_block_data` **(Many-Argument Workhorses)** (@ `client/network/sync/src/lib.rs`) -> Impact: **102.3** | LOC: 257
- `try_from` **(Many-Argument Workhorses)** (@ `frame/support/procedural/src/pallet/parse/call.rs`) -> Impact: **102.3** | LOC: 185

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `client/consensus/grandpa/src` | 13 | 3073.14 | 8.32% | 3.59% |
| `client/network/sync/src` | 11 | 3051.16 | 10.27% | 4.24% |
| `client/network/src` | 17 | 2798.9 | 7.0% | 6.76% |
| `frame/contracts/src` | 10 | 2585.46 | 6.45% | 2.82% |
| `client/db/src` | 10 | 2561.38 | 13.77% | 4.99% |
| `primitives/state-machine/src` | 11 | 2339.46 | 6.08% | 12.2% |
| `frame/support/procedural/src/pallet/parse` | 17 | 2217.14 | 8.74% | 3.6% |
| `frame/staking/src` | 9 | 1875.24 | 6.4% | 0.93% |
| `primitives/arithmetic/src` | 7 | 1873.06 | 7.24% | 4.05% |
| `frame/nomination-pools/src` | 4 | 1854.94 | 5.93% | 8.9% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `client/rpc-api/src/system/mod.rs` -> **100.0%** Exposure
- `frame/benchmarking/src/weights.rs` -> **100.0%** Exposure
- `frame/election-provider-support/src/weights.rs` -> **100.0%** Exposure
- `frame/society/src/weights.rs` -> **100.0%** Exposure
- `frame/support/src/traits/schedule.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `utils/build-script-utils/src/git.rs` -> **100.0%** Exposure
- `utils/fork-tree/src/lib.rs` -> **100.0%** Exposure
- `utils/frame/benchmarking-cli/src/extrinsic/bench.rs` -> **100.0%** Exposure
- `utils/frame/benchmarking-cli/src/shared/record.rs` -> **100.0%** Exposure
- `utils/frame/benchmarking-cli/src/storage/read.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `frame/contracts/src/wasm/mod.rs` -> **58** Orphaned Functions | **0** Duplicates
- `frame/support/src/storage/mod.rs` -> **14** Orphaned Functions | **33** Duplicates
- `frame/society/src/weights.rs` -> **0** Orphaned Functions | **40** Duplicates
- `primitives/api/test/tests/decl_and_impl.rs` -> **10** Orphaned Functions | **25** Duplicates
- `client/service/test/src/client/mod.rs` -> **30** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `scripts/ci/common/lib.sh` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24855` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `client/network/sync/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.557)
- **Top Global Matches:** file_cluster_4: 8.557, file_cluster_5: 10.707, file_cluster_12: 10.769
- **Magnitude:** 1592.6 | **LOC:** 4192 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **131**; blast radius 0.219; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (69.9%), Connectivity (formerly Api Exposure) (55.0%), Guard Balance (formerly Safety Score) (53.7%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_block_data` **(Many-Argument Workhorses)** (Impact: 102.3)
  * `on_blocks_processed` **(Many-Argument Workhorses)** (Impact: 51.9)
    * *Intent:* /// A batch of blocks have been processed, with or without errors. /// /// Call this when a batch of...
  * `block_response_into_blocks` **(Many-Argument Workhorses)** (Impact: 47.2)
  * `block_requests` **(Compute Cores)** (Impact: 38.8)
  * `finish_block_announce_validation` **(Many-Argument Workhorses)** (Impact: 38.6)
    * *Intent:* /// This will finish processing of the block announcement.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 13 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 406`, `structural_boundaries: 664`, `args: 199`, `func_start: 94`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 84`, `high_risk_execution: 2`, `state_mutation: 121`, `fragile_debt: 4`
* *Architecture:* `api: 59`, `concurrency: 22`, `import: 29`
* *Defense:* `safety: 97`, `doc: 218`, `test: 54`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 0.002367 | `Ripple Effect (Closeness):` 0.085762
  * `Imports (Out-Degree: 38):` block_request_handler, blocks, engine, extra_requests, mock, schema, service, state...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `client/db/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.658)
- **Top Global Matches:** file_cluster_5: 8.658, file_cluster_7: 11.274, file_cluster_12: 11.429
- **Magnitude:** 1493.32 | **LOC:** 4411 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **106**; blast radius 1.224; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Mutation Surface (formerly State Flux) (62.6%), Connectivity (formerly Api Exposure) (61.8%), Complexity Load (formerly Cognitive Load) (12.0%)
- **Documentation Coverage:** 89.0411% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_commit_operation` **(Many-Argument Workhorses)** (Impact: 134.0)
  * `revert` **(Many-Argument Workhorses)** (Impact: 63.0)
  * `prune_blocks` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `set_head_with_transaction` **(Many-Argument Workhorses)** (Impact: 32.3)
    * *Intent:* /// Handle setting head within a transaction. `route_to` should be the last /// block that existed i...
  * `append_justification` **(Many-Argument Workhorses)** (Impact: 28.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 72 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 269
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 353`, `structural_boundaries: 883`, `args: 212`, `func_start: 151`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 382`, `high_risk_execution: 2`, `state_mutation: 125`, `planned_debt: 4`
* *Architecture:* `api: 111`, `import: 32`
* *Defense:* `safety: 55`, `doc: 101`, `test: 233`, `sync_locks: 24`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.224
  * `Choke Point (Betweenness):` 0.008622 | `Ripple Effect (Closeness):` 0.143746
  * `Imports (Out-Degree: 33):` bench, children, offchain, parity_db, pinned_blocks_cache, record_stats_state, stats, upgrade...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `client/network/src/protocol/notifications/behaviour.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.837)
- **Top Global Matches:** file_cluster_4: 8.837, file_cluster_12: 9.091, file_cluster_13: 9.112
- **Magnitude:** 1227.46 | **LOC:** 4568 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **60**; blast radius 0.305; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.1%), Concurrency Surface (formerly Concurrency) (55.6%), Mutation Surface (formerly State Flux) (49.3%), Guard Balance (formerly Safety Score) (46.9%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_connection_handler_event` **(Many-Argument Workhorses)** (Impact: 171.7)
  * `on_swarm_event` **(Many-Argument Workhorses)** (Impact: 118.4)
  * `poll` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `disconnect_peer_inner` **(Many-Argument Workhorses)** (Impact: 29.6)
    * *Intent:* /// Inner implementation of `disconnect_peer`.
  * `peerset_report_connect` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /// Function that is called when the peerset wants us to connect to a peer.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 30 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 58 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 220
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 675`, `args: 141`, `func_start: 81`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 31`, `state_mutation: 104`, `fragile_debt: 2`
* *Architecture:* `api: 77`, `concurrency: 32`, `import: 16`
* *Defense:* `safety: 92`, `doc: 180`, `test: 298`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.305
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.088732
  * `Imports (Out-Degree: 6):` bytes::BytesMut, crate::mock::MockPeerStore, crate::protocol::notifications::handler, crate::protocol::notifications::handler::NotificationsSink, crate::protocol::notifications::handler::NotifsHandler, crate::protocol::notifications::handler::NotifsHandlerIn, crate::protocol::notifications::handler::NotifsHandlerOut, crate::protocol::notifications::handler::tests::*...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `client/service/src/client/client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.973)
- **Top Global Matches:** file_cluster_0: 7.973, file_cluster_4: 10.392, file_cluster_15: 11.216
- **Magnitude:** 1069.98 | **LOC:** 2136 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **122**; blast radius 0.438; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.0%), Mutation Surface (formerly State Flux) (52.4%), Guard Balance (formerly Safety Score) (50.9%)
- **Documentation Coverage:** 68.3099% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute_and_import_block` **(Many-Argument Workhorses)** (Impact: 251.9)
  * `storage_collection` **(Many-Argument Workhorses)** (Impact: 83.8)
  * `apply_finality_with_block_hash` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `lock_import_and_run` **(Defensive Guards)** (Impact: 35.4)
  * `new` **(Many-Argument Workhorses)** (Impact: 35.4)
    * *Intent:* /// Creates new Substrate Client with given blockchain and code executor.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 323`, `args: 150`, `func_start: 95`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 46`, `planned_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 54`, `concurrency: 46`, `import: 22`
* *Defense:* `safety: 36`, `doc: 70`, `test: 3`, `sync_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.438
  * `Choke Point (Betweenness):` 0.004713 | `Ripple Effect (Closeness):` 0.139949
  * `Imports (Out-Degree: 36):` futures::FutureExt, futures::StreamExt, log::error, log::info, log::trace, log::warn, parking_lot::Mutex, parking_lot::RwLock...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `frame/contracts/src/wasm/runtime.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.56)
- **Top Global Matches:** file_cluster_0: 7.56, file_cluster_15: 8.994, file_cluster_13: 9.808
- **Magnitude:** 923.28 | **LOC:** 2857 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **50**; blast radius 0.472; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.0%), Guard Balance (formerly Safety Score) (42.9%), Mutation Surface (formerly State Flux) (8.8%)
- **Documentation Coverage:** 14.9123% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `call` **(Many-Argument Workhorses)** (Impact: 81.8)
  * `instantiate` **(Many-Argument Workhorses)** (Impact: 64.7)
  * `write_sandbox_output` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /// length of the buffer located at `out_ptr`. If that buffer is large enough the actual /// `buf.le...
  * `deposit_event` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* /// Deposit a contract event with the data buffer and optional list of topics. There is a limit /// ...
  * `take_storage` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* /// Retrieve and remove the value under the given key from storage. /// /// # Parameters /// /// - `...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 207`, `args: 110`, `func_start: 96`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 3`, `planned_debt: 5`
* *Architecture:* `api: 28`, `import: 17`
* *Defense:* `safety: 24`, `doc: 998`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.472
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.00613
  * `Imports (Out-Degree: 16):` ReturnCode::*, TrapReason::*, bitflags::bitflags, codec::Decode, codec::DecodeLimit, codec::Encode, codec::MaxEncodedLen, crate::BalanceOf...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `frame/nomination-pools/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.281)
- **Top Global Matches:** file_cluster_0: 6.281, file_cluster_5: 10.167, file_cluster_13: 10.657
- **Magnitude:** 894.98 | **LOC:** 3294 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **45**; blast radius 0.651; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.9%), Guard Balance (formerly Safety Score) (43.4%), Mutation Surface (formerly State Flux) (38.7%)
- **Documentation Coverage:** 22.5352% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withdraw_unbonded` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /// /// # Conditions for a permissionless dispatch /// /// * The pool is in destroy mode and the tar...
  * `unbond` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* /// /// * The caller is not the depositor. /// * The caller is the depositor, the pool is destroying...
  * `ok_to_unbond_with` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `do_try_state` **(Generic / Templated Code)** (Impact: 23.8)
    * *Intent:* /// /// Then, considering unbonding members: /// /// for each pool: /// * sum of the balance that's ...
  * `do_bond_extra` **(Many-Argument Workhorses)** (Impact: 22.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 318`, `args: 142`, `func_start: 105`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 37`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 109`, `import: 15`
* *Defense:* `safety: 72`, `doc: 974`, `test: 9`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.651
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.005968
  * `Imports (Out-Degree: 19):` migration, mock, tests, weights, codec::Codec, frame_support::DefaultNoBound, frame_support::PalletError, frame_support::defensive...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `frame/contracts/src/exec.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.388)
- **Top Global Matches:** file_cluster_5: 7.388, file_cluster_12: 9.75, file_cluster_0: 10.623
- **Magnitude:** 851.8 | **LOC:** 3885 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **96**; blast radius 0.459; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.1%), Guard Balance (formerly Safety Score) (50.6%), Mutation Surface (formerly State Flux) (13.6%), Complexity Load (formerly Cognitive Load) (3.8%)
- **Documentation Coverage:** 65.9292% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* /// Run the current (top) frame. /// /// This can be either a call or an instantiate.
  * `new_frame` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* /// Construct a new frame. /// /// This does not take `self` because when constructing the first fra...
  * `pop_frame` **(Defensive Guards)** (Impact: 26.5)
    * *Intent:* /// Remove the current (top) frame from the stack. /// /// This is called after running the current ...
  * `call` **(Many-Argument Workhorses)** (Impact: 19.2)
  * `push_frame` **(Many-Argument Workhorses)** (Impact: 11.6)
    * *Intent:* /// Create a subsequent nested frame.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 44
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 775`, `args: 310`, `func_start: 176`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 105`, `high_risk_execution: 2`, `state_mutation: 18`
* *Architecture:* `api: 67`, `import: 24`
* *Defense:* `safety: 26`, `doc: 306`, `test: 162`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.459
  * `Choke Point (Betweenness):` 0.000349 | `Ripple Effect (Closeness):` 0.00786
  * `Imports (Out-Degree: 32):` assert_matches::assert_matches, codec::Decode, codec::Encode, crate::BalanceOf, crate::CodeHash, crate::CodeInfo, crate::CodeInfoOf, crate::Config...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `frame/staking/src/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.195)
- **Top Global Matches:** file_cluster_5: 8.195, file_cluster_12: 8.963, file_cluster_7: 10.084
- **Magnitude:** 778.8 | **LOC:** 6127 | **CtrlFlow:** 3.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.184; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (45.8%), Mutation Surface (formerly State Flux) (12.7%), Complexity Load (formerly Cognitive Load) (5.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_payout_stakers` **(I/O & Config Routines)** (Impact: 15.7)
  * `chill_other_works` **(I/O & Config Routines)** (Impact: 9.5)
  * `proportional_ledger_slash_works` **(I/O & Config Routines)** (Impact: 9.5)
  * `payout_stakers_handles_weight_refund` **(I/O & Config Routines)** (Impact: 9.3)
  * `nominating_and_rewards_should_work` **(I/O & Config Routines)** (Impact: 9.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 345`, `args: 286`, `func_start: 123`
* *Risk/State:* `safety_bypasses: 148`, `state_mutation: 45`
* *Architecture:* `api: 123`, `import: 21`
* *Defense:* `safety: 1`, `doc: 1`, `test: 867`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.008784
  * `Imports (Out-Degree: 20):` frame_election_provider_support::ElectionDataProvider, frame_election_provider_support::ElectionProvider, frame_election_provider_support::SortedListProvider, frame_election_provider_support::Support, frame_election_provider_support::bounds::DataProviderBounds, frame_election_provider_support::bounds::ElectionBoundsBuilder, frame_support::assert_noop, frame_support::assert_ok...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/consensus/grandpa/src/communication/gossip.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.714)
- **Top Global Matches:** file_cluster_0: 7.714, file_cluster_12: 8.814, file_cluster_5: 9.045
- **Magnitude:** 757.58 | **LOC:** 2651 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **56**; blast radius 0.253; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.2%), Guard Balance (formerly Safety Score) (50.2%), Connectivity (formerly Api Exposure) (39.8%)
- **Documentation Coverage:** 76.9912% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `reshuffle` **(Compute Cores)** (Impact: 31.9)
  * `handle_catch_up_request` **(Many-Argument Workhorses)** (Impact: 26.8)
  * `message_allowed` **(Defensive Guards)** (Impact: 25.0)
  * `update_peer_state` **(Many-Argument Workhorses)** (Impact: 20.2)
    * *Intent:* // returns a reference to the new view, if the peer is known.
  * `validate_catch_up_message` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Cascading Flux:* 40 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 413`, `args: 139`, `func_start: 83`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 9`, `state_mutation: 61`
* *Architecture:* `api: 57`, `import: 25`
* *Defense:* `safety: 33`, `doc: 203`, `test: 102`, `sync_locks: 3`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.253
  * `Choke Point (Betweenness):` 6.6e-05 | `Ripple Effect (Closeness):` 0.003633
  * `Imports (Out-Degree: 19):` Misbehavior::*, ahash::AHashMap, ahash::AHashSet, crate::CatchUp, crate::CompactCommit, crate::LOG_TARGET, crate::SignedMessage, crate::authorities::AuthoritySet...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `frame/contracts/src/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.798)
- **Top Global Matches:** file_cluster_5: 6.798, file_cluster_12: 9.062, file_cluster_7: 9.595
- **Magnitude:** 757.54 | **LOC:** 5894 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **102**; blast radius 0.302; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (55.2%), Mutation Surface (formerly State Flux) (9.3%), Debt Markers (formerly Tech Debt) (8.7%)
- **Documentation Coverage:** 98.6607% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `call` **(Generic / Templated Code)** (Impact: 14.1)
  * `lazy_removal_partial_remove_works` **(I/O & Config Routines)** (Impact: 12.6)
  * `lazy_removal_does_not_use_all_weight` **(I/O & Config Routines)** (Impact: 10.0)
  * `add_remove_delegate_dependency_works` **(I/O & Config Routines)** (Impact: 9.7)
  * `native_dependency_deposit_works` **(I/O & Config Routines)** (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 678`, `args: 238`, `func_start: 123`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 246`, `high_risk_execution: 4`, `state_mutation: 21`, `duplicate_logic: 3`
* *Architecture:* `api: 123`, `import: 21`
* *Defense:* `safety: 4`, `doc: 7`, `test: 227`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.302
  * `Choke Point (Betweenness):` 0.000184 | `Ripple Effect (Closeness):` 0.007298
  * `Imports (Out-Degree: 32):` pallet_dummy, test_debug, assert_matches::assert_matches, codec::Decode, codec::Encode, codec::MaxEncodedLen, crate, crate::BalanceOf...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `utils/fork-tree/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 12.07)
- **Top Global Matches:** file_cluster_4: 12.07, file_cluster_5: 12.946, file_cluster_6: 13.16
- **Magnitude:** 732.54 | **LOC:** 1610 | **CtrlFlow:** 17.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 0.324; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.8%), Connectivity (formerly Api Exposure) (59.7%)
- **Documentation Coverage:** 60.241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finalize_with_descendent_if` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* /// Finalize a root in the tree by either finalizing the node itself or a /// node's descendent that...
  * `prune` **(Many-Argument Workhorses)** (Impact: 47.5)
    * *Intent:* /// Prune the tree, removing all non-canonical nodes. /// /// We find the node in the tree that is t...
  * `find_node_index_where` **(Many-Argument Workhorses)** (Impact: 47.1)
    * *Intent:* /// Same as [`find_node_where`](ForkTree::find_node_where), but returns indices. /// /// The returne...
  * `finalize_with_ancestors` **(Many-Argument Workhorses)** (Impact: 46.0)
    * *Intent:* /// Finalize a node in the tree and all its ancestors. The given function /// `is_descendent_of` sho...
  * `finalize` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /// Finalize a node in the tree. This method will make sure that the node /// being finalized is eit...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 191
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 291`, `args: 124`, `func_start: 45`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 62`, `high_risk_execution: 1`, `state_mutation: 69`
* *Architecture:* `api: 47`, `import: 7`
* *Defense:* `safety: 14`, `doc: 107`, `test: 115`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.324
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.069111
  * `Imports (Out-Degree: 0):` codec::Decode, codec::Encode, crate::FilterAction, node_implementation::Node, self::*, self::Error, self::FinalizationResult, self::ForkTree...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `client/rpc-spec-v2/src/chain_head/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 14.977)
- **Top Global Matches:** file_cluster_6: 14.977, file_cluster_4: 15.871, file_cluster_5: 16.126
- **Magnitude:** 705.38 | **LOC:** 2568 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.179; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_continue_operation` **(I/O & Config Routines)** (Impact: 29.9)
  * `get_storage_multi_query_iter` **(I/O & Config Routines)** (Impact: 26.9)
  * `get_storage_hash` **(I/O & Config Routines)** (Impact: 23.9)
  * `get_storage_value` **(I/O & Config Routines)** (Impact: 23.9)
  * `call_runtime` **(I/O & Config Routines)** (Impact: 15.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 331
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 965`, `args: 29`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 252`, `high_risk_execution: 26`, `state_mutation: 6`
* *Architecture:* `api: 24`, `concurrency: 301`, `import: 17`
* *Defense:* `test: 85`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.001414
  * `Imports (Out-Degree: 16):` assert_matches::assert_matches, codec::Decode, codec::Encode, crate::chain_head::event::MethodResponse, crate::chain_head::event::StorageQuery, crate::chain_head::event::StorageQueryType, crate::chain_head::event::StorageResultType, crate::chain_head::test_utils::ChainHeadMockClient...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `frame/elections-phragmen/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.593)
- **Top Global Matches:** file_cluster_0: 7.593, file_cluster_13: 9.31, file_cluster_10: 9.84
- **Magnitude:** 677.16 | **LOC:** 3328 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **53**; blast radius 0.455; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (67.6%), Guard Balance (formerly Safety Score) (41.8%), Mutation Surface (formerly State Flux) (18.0%), Debt Markers (formerly Tech Debt) (9.2%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_phragmen` **(I/O & Config Routines)** (Impact: 24.5)
    * *Intent:* /// Run the phragmen election with all required side processes and state updates, if election /// su...
  * `remove_and_replace_member` **(Many-Argument Workhorses)** (Impact: 21.0)
    * *Intent:* /// Returns: /// /// - `Ok(true)` if the member was removed and a replacement was found. /// - `Ok(f...
  * `renounce_candidacy` **(Generic / Templated Code)** (Impact: 17.8)
    * *Intent:* /// origin is removed as a runner-up. /// - `origin` is a current member. In this case, the deposit ...
  * `remove_member` **(Many-Argument Workhorses)** (Impact: 16.9)
    * *Intent:* /// /// If a runner-up is available, then the best runner-up will be removed and replaces the /// ou...
  * `vote` **(Generic / Templated Code)** (Impact: 10.9)
    * *Intent:* /// /// The `votes` should: /// - not be empty. /// - be less than the number of possible candidates...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 58
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 245`, `args: 302`, `func_start: 134`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 36`, `duplicate_logic: 2`
* *Architecture:* `api: 132`, `import: 21`
* *Defense:* `safety: 12`, `doc: 310`, `test: 385`, `sync_locks: 3`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.455
  * `Choke Point (Betweenness):` 0.000358 | `Ripple Effect (Closeness):` 0.002522
  * `Imports (Out-Degree: 25):` benchmarking, migrations, weights, codec::Decode, codec::Encode, crate, frame_support::assert_noop, frame_support::assert_ok...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `client/consensus/babe/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.949)
- **Top Global Matches:** file_cluster_0: 7.949, file_cluster_5: 10.391, file_cluster_4: 10.518
- **Magnitude:** 648.06 | **LOC:** 1940 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **108**; blast radius 0.359; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.7%), Guard Balance (formerly Safety Score) (49.1%)
- **Documentation Coverage:** 58.1081% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import_block` **(Many-Argument Workhorses)** (Impact: 84.8)
  * `verify` **(Many-Argument Workhorses)** (Impact: 37.4)
  * `revert` **(Generic / Templated Code)** (Impact: 33.6)
    * *Intent:* /// Reverts protocol aux data to at most the last finalized block. /// In particular, epoch-changes ...
  * `check_and_report_equivocation` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `check_inherents` **(Many-Argument Workhorses)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 11 instances
* *Concurrency (weighted view):* 104
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 294`, `args: 107`, `func_start: 49`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 25`, `fragile_debt: 1`
* *Architecture:* `api: 73`, `concurrency: 84`, `import: 27`
* *Defense:* `safety: 29`, `doc: 191`, `test: 1`, `sync_locks: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.359
  * `Choke Point (Betweenness):` 0.000572 | `Ripple Effect (Closeness):` 0.006086
  * `Imports (Out-Degree: 40):` authorship, aux_schema, migration, tests, verification, aux_schema::load_block_weight, codec::Decode, codec::Encode...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `frame/nomination-pools/src/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.38)
- **Top Global Matches:** file_cluster_5: 7.38, file_cluster_7: 9.147, file_cluster_12: 9.349
- **Magnitude:** 636.9 | **LOC:** 6730 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.184; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (59.5%), Mutation Surface (formerly State Flux) (10.7%), Complexity Load (formerly Cognitive Load) (5.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_reward_payout_works_with_a_pool_of_3` **(I/O & Config Routines)** (Impact: 11.2)
  * `withdraw_unbonded_works_against_slashed_no_era_sub_pool` **(I/O & Config Routines)** (Impact: 7.5)
  * `maybe_merge_pools_works` **(Annotated & Test Methods)** (Impact: 6.5)
  * `do_reward_payout_works_with_a_pool_of_1` **(Annotated & Test Methods)** (Impact: 5.6)
  * `join_max_member_limits_are_respected` **(I/O & Config Routines)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 277`, `args: 220`, `func_start: 111`
* *Risk/State:* `safety_bypasses: 298`, `state_mutation: 27`
* *Architecture:* `api: 104`, `import: 27`
* *Defense:* `test: 841`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.004429
  * `Imports (Out-Degree: 8):` crate::Event, crate::mock::*, frame_support::assert_err, frame_support::assert_noop, frame_support::assert_ok, frame_support::assert_storage_noop, pallet_balances::Event, self::*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/network/test/src/sync.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.422)
- **Top Global Matches:** file_cluster_5: 7.422, file_cluster_7: 7.62, file_cluster_12: 8.785
- **Magnitude:** 633.24 | **LOC:** 1326 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.173; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (69.4%), Connectivity (formerly Api Exposure) (62.6%), Complexity Load (formerly Cognitive Load) (34.5%)
- **Documentation Coverage:** 87.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sync_cycle_from_offline_to_syncing_to_offline` **(I/O & Config Routines)** (Impact: 13.8)
  * `block_announce_data_is_propagated` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* /// Ensures that when we receive a block announcement with some data attached, that we propagate ///...
  * `syncs_state` **(I/O & Config Routines)** (Impact: 11.7)
  * `can_sync_small_non_best_forks` **(Annotated & Test Methods)** (Impact: 9.2)
  * `can_sync_explicit_forks` **(Annotated & Test Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 296
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 279`, `args: 81`, `func_start: 46`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 40`, `planned_debt: 1`
* *Architecture:* `api: 39`, `concurrency: 146`, `import: 9`
* *Defense:* `doc: 13`, `test: 107`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.173
  * `Choke Point (Betweenness):` 9.4e-05 | `Ripple Effect (Closeness):` 0.007909
  * `Imports (Out-Degree: 9):` futures::Future, sp_consensus::BlockOrigin, sp_consensus::block_validation::Validation, sp_core::storage::well_known_keys::HEAP_PAGES, sp_runtime::Justifications, sp_runtime::codec::Encode, sp_runtime::traits::Hash, substrate_test_runtime::Header...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `primitives/runtime/src/traits.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.074)
- **Top Global Matches:** file_cluster_0: 8.074, file_cluster_5: 11.023, file_cluster_13: 11.413
- **Magnitude:** 619.94 | **LOC:** 2457 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **645** in-repo importer(s); it depends on **98**; blast radius 30.458; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.7%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (68.0%), Guard Balance (formerly Safety Score) (47.0%)
- **Documentation Coverage:** 49.6% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `read` **(Defensive Guards)** (Impact: 18.6)
  * `post_dispatch` **(Many-Argument Workhorses)** (Impact: 10.6)
  * `try_from_sub_account` **(Callbacks & Closures)** (Impact: 7.8)
  * `try_into_sub_account` **(Generic / Templated Code)** (Impact: 5.8)
    * *Intent:* // Same as `into_sub_account_truncating`, but returns `None` if any bytes would be truncated.
  * `get_raw` **(Compute Cores)** (Impact: 5.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 426`, `args: 245`, `func_start: 213`, `class_start: 67`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 2`, `state_mutation: 6`, `planned_debt: 4`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 122`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 9`, `doc: 501`, `test: 36`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.458
  * `Choke Point (Betweenness):` 0.029201 | `Ripple Effect (Closeness):` 0.378616
  * `Imports (Out-Degree: 16):` codec::Codec, codec::Decode, codec::Encode, codec::EncodeLike, codec::FullCodec, codec::MaxEncodedLen, crate::DispatchResult, crate::codec::Decode...
  * `Imported By (In-Degree: 645):` (Excluded from Brief to save tokens)

### `primitives/state-machine/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.264)
- **Top Global Matches:** file_cluster_5: 7.264, file_cluster_12: 9.17, file_cluster_0: 10.803
- **Magnitude:** 617.72 | **LOC:** 1965 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **92**; blast radius 0.932; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.2%), Mutation Surface (formerly State Flux) (55.7%), Guard Balance (formerly Safety Score) (55.5%)
- **Documentation Coverage:** 50.495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `prove_range_read_with_child_with_size_on_trie_backend` **(Many-Argument Workhorses)** (Impact: 65.2)
    * *Intent:* /// Generate range storage read proof, with child tries /// content. /// See `prove_range_read_with_...
  * `read_range_proof_check_with_child_on_proving_backend` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* /// Check storage range proof on pre-created proving backend. /// /// See `read_range_proof_check_wi...
  * `update_last_key` **(Many-Argument Workhorses)** (Impact: 33.1)
    * *Intent:* /// Update last keys accessed from this state.
  * `prove_range_read_with_size_on_trie_backend` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /// Generate range storage read proof on an existing trie backend.
  * `child_read_compact_stress_test` **(Type Conversions)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 486`, `args: 89`, `func_start: 55`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 2`, `state_mutation: 56`
* *Architecture:* `api: 70`, `import: 27`
* *Defense:* `safety: 16`, `doc: 91`, `test: 84`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.932
  * `Choke Point (Betweenness):` 0.004393 | `Ripple Effect (Closeness):` 0.177847
  * `Imports (Out-Degree: 21):` backend, basic, error, ext, in_memory_backend, overlayed_changes, read_only, stats...
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `frame/staking/src/pallet/impls.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.878)
- **Top Global Matches:** file_cluster_0: 6.878, file_cluster_5: 9.047, file_cluster_12: 9.95
- **Magnitude:** 596.92 | **LOC:** 1886 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **71**; blast radius 0.207; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.1%), Connectivity (formerly Api Exposure) (62.7%), Guard Balance (formerly Safety Score) (48.7%)
- **Documentation Coverage:** 64.557% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `on_offence` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `get_npos_voters` **(Compute Cores)** (Impact: 35.2)
    * *Intent:* /// Get all of the voters that are eligible for the npos election. /// /// `maybe_max_len` can impos...
  * `do_payout_stakers` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `try_trigger_new_era` **(Stateful Encapsulated Methods)** (Impact: 16.6)
    * *Intent:* /// Potentially plan a new era. /// /// Get election result from `T::ElectionProvider`. /// In case ...
  * `new_session` **(Defensive Guards)** (Impact: 16.0)
    * *Intent:* /// Plan a new session potentially trigger a new era.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 65
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 247`, `args: 181`, `func_start: 105`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 4`, `state_mutation: 27`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 12`
* *Architecture:* `api: 55`, `import: 12`
* *Defense:* `safety: 53`, `doc: 132`, `test: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.207
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.008828
  * `Imports (Out-Degree: 27):` crate::ActiveEraInfo, crate::BalanceOf, crate::EraPayout, crate::Exposure, crate::ExposureOf, crate::Forcing, crate::IndividualExposure, crate::MaxNominationsOf...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `bin/node/runtime/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_0: 6.997, file_cluster_15: 10.177, file_cluster_13: 10.286
- **Magnitude:** 577.98 | **LOC:** 2789 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **154**; blast radius 0.829; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (88.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.7%), Debt Markers (formerly Tech Debt) (13.7%)
- **Documentation Coverage:** 95.7317% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch_benchmark` **(Generic / Templated Code)** (Impact: 11.7)
  * `create_transaction` **(Generic / Templated Code)** (Impact: 8.5)
  * `track_for` **(Defensive Guards)** (Impact: 6.2)
  * `is_superset` **(State Mutators)** (Impact: 5.6)
  * `on_unbalanceds` **(Generic / Templated Code)** (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 1040`, `args: 106`, `func_start: 92`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 319`, `import: 63`
* *Defense:* `safety: 11`, `doc: 62`, `test: 8`, `immutability_locks: 186`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.829
  * `Choke Point (Betweenness):` 0.002465 | `Ripple Effect (Closeness):` 0.009015
  * `Imports (Out-Degree: 76):` assets_api, constants, impls, voter_bags, baseline::Pallet, codec::Decode, codec::Encode, codec::MaxEncodedLen...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `frame/asset-conversion/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.483)
- **Top Global Matches:** file_cluster_4: 8.483, file_cluster_0: 11.73, file_cluster_6: 11.92
- **Magnitude:** 564.8 | **LOC:** 1311 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **47**; blast radius 0.288; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (47.4%), Guard Balance (formerly Safety Score) (46.4%), Mutation Surface (formerly State Flux) (24.5%)
- **Documentation Coverage:** 12.069% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add_liquidity` **(Many-Argument Workhorses)** (Impact: 83.4)
    * *Intent:* /// Provide liquidity into the pool of `asset1` and `asset2`. /// NOTE: an optimal amount of asset1 ...
  * `remove_liquidity` **(Many-Argument Workhorses)** (Impact: 48.9)
    * *Intent:* /// Allows you to remove liquidity by providing the `lp_token_burn` tokens that will be /// burned i...
  * `create_pool` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /// Creates an empty liquidity pool and an associated new `lp_token` asset /// (the id of which is r...
  * `do_swap` **(Many-Argument Workhorses)** (Impact: 37.1)
    * *Intent:* /// Swap assets along a `path`, depositing in `send_to`.
  * `get_amount_in` **(Defensive Guards)** (Impact: 25.9)
    * *Intent:* /// Calculates amount in. /// /// Given an output amount of an asset and pair reserves, returns a re...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 188`, `args: 49`, `func_start: 34`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 37`, `import: 14`
* *Defense:* `safety: 31`, `doc: 228`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` 0.000229 | `Ripple Effect (Closeness):` 0.005785
  * `Imports (Out-Degree: 19):` benchmarking, mock, tests, types, weights, codec::Codec, frame_support::BoundedBTreeSet, frame_support::PalletId...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `frame/society/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 5.802)
- **Top Global Matches:** file_cluster_0: 5.802, file_cluster_5: 9.976, file_cluster_13: 10.676
- **Magnitude:** 556.22 | **LOC:** 2036 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **39**; blast radius 0.278; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.6%), Guard Balance (formerly Safety Score) (44.3%), Mutation Surface (formerly State Flux) (37.7%)
- **Documentation Coverage:** 17.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `judge_suspended_member` **(Generic / Templated Code)** (Impact: 15.4)
    * *Intent:* /// Allow suspension judgement origin to make judgement on a suspended member. /// /// If a suspende...
  * `vote` **(Generic / Templated Code)** (Impact: 15.2)
    * *Intent:* /// As a member, vote on a candidate. /// /// The dispatch origin for this call must be _Signed_ and...
  * `reward_bidder` **(Many-Argument Workhorses)** (Impact: 15.2)
    * *Intent:* /// Pay an accepted candidate their bid value.
  * `rotate_challenge` **(Generic / Templated Code)** (Impact: 15.1)
    * *Intent:* /// End the current challenge period and start a new one.
  * `remove_member` **(Generic / Templated Code)** (Impact: 14.9)
    * *Intent:* /// Remove a member from the members list and return the candidacy. /// /// If the member was vouchi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 319`, `args: 87`, `func_start: 61`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 20`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 87`, `import: 10`
* *Defense:* `safety: 39`, `doc: 597`, `test: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.278
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.001962
  * `Imports (Out-Degree: 23):` benchmarking, migrations, mock, tests, weights, frame_support::PalletId, frame_support::impl_ensure_origin_with_arg_ignoring_arg, frame_support::pallet_prelude::*...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `frame/assets/src/functions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.389)
- **Top Global Matches:** file_cluster_4: 9.389, file_cluster_0: 10.531, file_cluster_9: 11.743
- **Magnitude:** 550.9 | **LOC:** 1017 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.184; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (44.6%), Connectivity (formerly Api Exposure) (33.8%)
- **Documentation Coverage:** 6.5574% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `transfer_and_die` **(Many-Argument Workhorses)** (Impact: 47.0)
    * *Intent:* /// Same as `do_transfer` but it does not execute the `FrozenBalance::died` hook and /// instead ret...
  * `can_decrease` **(Many-Argument Workhorses)** (Impact: 38.2)
    * *Intent:* /// Return the consequence of a withdraw.
  * `decrease_balance` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /// Reduces asset `id` balance of `target` by `amount`. Flags `f` can be given to alter whether /// ...
  * `can_increase` **(Stateful Encapsulated Methods)** (Impact: 30.8)
    * *Intent:* /// Returns `true` when the balance of `account` can be increased by `amount`. /// /// - `id`: The i...
  * `do_transfer_approved` **(Many-Argument Workhorses)** (Impact: 26.7)
    * *Intent:* /// Reduces the asset `id` balance of `owner` by some `amount` and increases the balance of /// `des...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 152`, `args: 56`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 31`, `import: 7`
* *Defense:* `safety: 60`, `doc: 122`, `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.184
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002337
  * `Imports (Out-Degree: 4):` AssetStatus::*, DeadConsequence::*, ExistenceReason::*, WithdrawConsequence::*, frame_support::BoundedVec, frame_support::defensive, frame_support::traits::Get, super::*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `client/consensus/grandpa/src/environment.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.609)
- **Top Global Matches:** file_cluster_0: 8.609, file_cluster_5: 9.476, file_cluster_4: 9.608
- **Magnitude:** 531.0 | **LOC:** 1545 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **71**; blast radius 0.262; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.7%), Connectivity (formerly Api Exposure) (42.7%), Concurrency Surface (formerly Concurrency) (27.9%)
- **Documentation Coverage:** 38.5542% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finalize_block` **(Many-Argument Workhorses)** (Impact: 76.0)
    * *Intent:* /// Finalize the given block and apply any authority set changes. If an /// authority set change is ...
  * `best_chain_containing` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `report_equivocation` **(Many-Argument Workhorses)** (Impact: 23.7)
    * *Intent:* /// Report the given equivocation to the GRANDPA runtime module. This method /// generates a session...
  * `concluded` **(Many-Argument Workhorses)** (Impact: 19.9)
  * `precommitted` **(Many-Argument Workhorses)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 6 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 23
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 214`, `args: 79`, `func_start: 47`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 1`, `state_mutation: 18`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 64`, `concurrency: 13`, `import: 19`
* *Defense:* `safety: 27`, `doc: 77`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.005449
  * `Imports (Out-Degree: 20):` crate::ClientForGrandpa, crate::CommandOrError, crate::Commit, crate::Config, crate::Error, crate::LOG_TARGET, crate::NewAuthoritySet, crate::Precommit...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `client/statement-store/src/lib.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.553)
- **Top Global Matches:** file_cluster_5: 7.553, file_cluster_12: 7.78, file_cluster_0: 8.904
- **Magnitude:** 528.08 | **LOC:** 1297 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **43**; blast radius 0.174; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.0%), Connectivity (formerly Api Exposure) (44.8%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `insert` **(Many-Argument Workhorses)** (Impact: 53.0)
  * `make_expired` **(Defensive Guards)** (Impact: 28.2)
  * `submit` **(Many-Argument Workhorses)** (Impact: 26.3)
    * *Intent:* /// Submit a statement to the store. Validates the statement and returns validation result.
  * `new` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* /// Create a new instance. /// `path` will be used to open a statement database or create a new one ...
  * `validate_statement` **(Compute Cores)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 32 instances
* *Concurrency (weighted view):* 21
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 268`, `args: 85`, `func_start: 48`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 4`, `state_mutation: 46`
* *Architecture:* `api: 21`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 39`, `doc: 52`, `test: 49`, `sync_locks: 3`, `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.174
  * `Choke Point (Betweenness):` 1.2e-05 | `Ripple Effect (Closeness):` 0.002091
  * `Imports (Out-Degree: 14):` metrics, crate::Store, crate::tests::account, metrics::MetricsLink, parking_lot::RwLock, prometheus_endpoint::Registry, sc_keystore::Keystore, sc_keystore::LocalKeystore...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `primitives/arithmetic/src/fixed_point.rs` (RUST) | Magnitude: 519.18 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 1538, structural_boundaries: 370, test: 333, core_var_decl: 330
- `frame/asset-rate/src/benchmarking.rs` (RUST) | Magnitude: 13.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 17, generics: 9, import: 9
- `frame/support/procedural/src/construct_runtime/expand/outer_enums.rs` (RUST) | Magnitude: 92.44 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 174, structural_boundaries: 48, doc: 34, core_var_decl: 30
- `client/transaction-pool/src/enactment_state.rs` (RUST) | Magnitude: 176.94 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 482, structural_boundaries: 157, core_var_decl: 89, design_snake_case: 88
- `client/rpc-api/src/author/error.rs` (RUST) | Magnitude: 13.94 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 109, doc: 26, core_var_decl: 15, design_snake_case: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `frame/whitelist/src/mock.rs` (RUST) | Magnitude: 5.98 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 63, structural_boundaries: 62, core_var_decl: 51, design_pascal_case: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `frame/staking/reward-curve/src/log.rs` (RUST) | Magnitude: 57.38 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 67, structural_boundaries: 33, core_var_decl: 29, design_snake_case: 26
- `frame/support/procedural/src/pallet/expand/mod.rs` (RUST) | Magnitude: 18.5 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 67, indent_tabs: 62, core_var_decl: 22, design_snake_case: 22
- `frame/support/src/traits/hooks.rs` (RUST) | Magnitude: 135.08 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 254, doc: 231, structural_boundaries: 63, args: 46
- `frame/system/src/limits.rs` (RUST) | Magnitude: 107.44 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 207, doc: 151, structural_boundaries: 40, api: 29
- `bin/node/cli/tests/websocket_server.rs` (RUST) | Magnitude: 126.1 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 146, doc: 60, structural_boundaries: 51, core_var_decl: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `frame/vesting/src/weights.rs` (RUST) | Magnitude: 57.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 161, indent_tabs: 120, args: 24, func_start: 24
- `primitives/rpc/src/tracing.rs` (RUST) | Magnitude: 38.9 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 31, api: 23, indent_tabs: 19, decorators: 12
- `primitives/runtime-interface/src/lib.rs` (RUST) | Magnitude: 29.78 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 395, structural_boundaries: 18, decorators: 15, api: 14
- `frame/safe-mode/src/tests.rs` (RUST) | Magnitude: 106.6 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 433, test: 60, args: 49, generics: 33
- `frame/nis/src/weights.rs` (RUST) | Magnitude: 50.82 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 161, indent_tabs: 123, args: 33, func_start: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `client/executor/src/integration_tests/linux.rs` (RUST) | Magnitude: 10.66 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 16, safety_bypasses: 10, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `client/executor/runtime-test/src/lib.rs` (RUST) | Magnitude: 137.2 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 251, structural_boundaries: 56, args: 45, func_start: 43
- `bin/node/testing/src/genesis.rs` (RUST) | Magnitude: 12.82 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 77, structural_boundaries: 6, args: 5, doc: 4
- `client/consensus/beefy/src/communication/mod.rs` (RUST) | Magnitude: 39.42 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 33, core_var_decl: 28, api: 21
- `client/network/statement/src/lib.rs` (RUST) | Magnitude: 201.88 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 342, structural_boundaries: 80, branch: 49, doc: 46
- `utils/frame/benchmarking-cli/build.rs` (RUST) | Magnitude: 4.58 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 6, doc: 4, structural_boundaries: 3, branch: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `.github/workflows/burnin-label-notification.yml` (YAML) | Magnitude: 17.44 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 4, args: 4, branch: 2
- `frame/support/src/traits/tokens/fungibles/mod.rs` (RUST) | Magnitude: 26.4 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 15, api: 11, import: 6, indent_tabs: 3
- `frame/support/src/traits/tokens.rs` (RUST) | Magnitude: 27.34 | Delta: **0.156** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, api: 12, import: 3, indent_tabs: 3
- `frame/nfts/src/features/mod.rs` (RUST) | Magnitude: 26.22 | Delta: **0.188** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 11, api: 11, sync_locks: 1
- `client/cli/src/commands/mod.rs` (RUST) | Magnitude: 17.56 | Delta: **0.202** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 21, indent_tabs: 6, api: 2, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `bin/utils/chain-spec-builder/build.rs` (RUST) | Magnitude: 2.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, branch: 1, args: 1
- `client/consensus/slots/build.rs` (RUST) | Magnitude: 2.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, branch: 1, args: 1
- `client/executor/wasmtime/build.rs` (RUST) | Magnitude: 2.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, branch: 1, args: 1
- `test-utils/cli/build.rs` (RUST) | Magnitude: 2.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 3, structural_boundaries: 2, branch: 1, args: 1
- `client/rpc-spec-v2/src/transaction/error.rs` (RUST) | Magnitude: 9.76 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 65, structural_boundaries: 7, doc: 6, decorators: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `frame/society/src/mock.rs` (RUST) | Magnitude: 100.0 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 202, structural_boundaries: 90, core_var_decl: 69, design_pascal_case: 52
- `bin/node/inspect/src/lib.rs` (RUST) | Magnitude: 123.48 | Delta: **0.192** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 182, structural_boundaries: 75, generics: 55, branch: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `frame/support/src/storage/generator/value.rs` (RUST) | Magnitude: 54.18 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 33, generics: 30, args: 24
- `frame/beefy/src/mock.rs` (RUST) | Magnitude: 46.42 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 206, structural_boundaries: 142, core_var_decl: 113, design_pascal_case: 105
- `frame/offences/benchmarking/src/lib.rs` (RUST) | Magnitude: 82.72 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 317, generics: 107, structural_boundaries: 99, core_var_decl: 60
- `client/rpc-api/src/system/helpers.rs` (RUST) | Magnitude: 34.66 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 67, doc: 25, api: 23, structural_boundaries: 12
- `utils/frame/benchmarking-cli/src/shared/weight_params.rs` (RUST) | Magnitude: 17.7 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 37, structural_boundaries: 19, doc: 15, api: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `frame/support/procedural/src/construct_runtime/parse.rs` (RUST) | Magnitude: 411.6 | Delta: **0.15** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 513, branch: 183, structural_boundaries: 149, doc: 79
- `primitives/npos-elections/src/mock.rs` (RUST) | Magnitude: 237.36 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 271, structural_boundaries: 97, generics: 50, branch: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `frame/offences/src/tests.rs` (RUST) | Magnitude: 40.72 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 129, test: 32, structural_boundaries: 23, args: 22
- `client/executor/wasmtime/src/tests.rs` (RUST) | Magnitude: 96.68 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 329, structural_boundaries: 65, core_var_decl: 48, design_snake_case: 45
- `bin/node/cli/tests/temp_base_path_works.rs` (RUST) | Magnitude: 9.3 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 14, concurrency: 5, core_var_decl: 4
- `bin/node/cli/tests/version.rs` (RUST) | Magnitude: 6.8 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 14, structural_boundaries: 10, test: 8, core_var_decl: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `test-utils/client/src/lib.rs` -> **Severity: 2.138** (Bridge: 0.0761 * Flux: 28.1037%)
- `primitives/runtime/src/lib.rs` -> **Severity: 1.918** (Bridge: 0.0986 * Flux: 19.4453%)
- `frame/broker/src/mock.rs` -> **Severity: 0.978** (Bridge: 0.0113 * Flux: 86.2187%)
- `frame/support/src/lib.rs` -> **Severity: 0.814** (Bridge: 0.0586 * Flux: 13.897%)
- `primitives/state-machine/src/ext.rs` -> **Severity: 0.765** (Bridge: 0.0116 * Flux: 66.1172%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `primitives/core/src/hash.rs` -> **Severity: 21.427** (Embedded: 0.2678 * Error Risk: 80.0%)
- `primitives/std/src/lib.rs` -> **Severity: 19.754** (Embedded: 0.4043 * Error Risk: 48.861%)
- `primitives/runtime/src/traits.rs` -> **Severity: 17.784** (Embedded: 0.3786 * Error Risk: 46.972%)
- `primitives/state-machine/src/trie_backend.rs` -> **Severity: 17.761** (Embedded: 0.222 * Error Risk: 80.0%)
- `primitives/runtime/src/runtime_logger.rs` -> **Severity: 17.456** (Embedded: 0.2182 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `primitives/runtime/src/traits.rs` -> **Severity: 1510.717** (Blast Radius: 30.458 * Doc Risk: 49.6%)
- `primitives/arithmetic/src/traits.rs` -> **Severity: 1455.024** (Blast Radius: 33.38 * Doc Risk: 43.5897%)
- `primitives/runtime/src/lib.rs` -> **Severity: 1224.09** (Blast Radius: 19.113 * Doc Risk: 64.0449%)
- `frame/support/src/lib.rs` -> **Severity: 1012.288** (Blast Radius: 23.138 * Doc Risk: 43.75%)
- `primitives/core/src/crypto.rs` -> **Severity: 898.785** (Blast Radius: 18.397 * Doc Risk: 48.855%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 348 literal sites + 2 sites through wrappers = 350
- **`panics_and_aborts`:** 383 literal sites + 9 sites through wrappers = 392

- `invalid_version` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `frame/contracts/src/migration.rs`
- `generate_rerun_if_changed_instructions` (function, debug_prints, primitive): 2 call sites in 1 files -- `utils/wasm-builder/src/builder.rs`
- `parse_cargo_toml` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `scripts/ci/node-template-release/src/main.rs`
- `write_cargo_toml` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `scripts/ci/node-template-release/src/main.rs`
- `duration_now` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `client/consensus/slots/src/slots.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 121465 call pairs -- scoped 19.1%, unique 0.0%, ambiguous 31.9%, external 49.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 121367 | 19.1% | 0.0% | 32.0% | 49.0% |
| shell | 68 | 11.8% | 10.3% | 0.0% | 77.9% |
| javascript | 16 | 0.0% | 0.0% | 0.0% | 100.0% |
| python | 14 | 0.0% | 0.0% | 0.0% | 100.0% |

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
