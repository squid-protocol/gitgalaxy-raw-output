# ARCHITECTURAL_BRIEF: solana
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/solana-labs/solana.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1606 analyzed artifact(s), 475298 LOC.
- **Load-bearing artifact:** `sdk/program/src/system_program.rs` -- 67 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `rpc/src/rpc.rs` -- pulls in 239 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `storage-bigtable/src/pki-goog-roots.pem` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 2192 |
| Analyzed Artifacts (Scanned) | 1606 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 586 |
| Total LOC | 475298 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 73.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7293 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1911 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0909 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 61 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1168 | 452363 | 72.7% |
| SHELL | 225 | 15993 | 14.0% |
| C | 115 | 4280 | 7.2% |
| YAML | 46 | 917 | 2.9% |
| MARKDOWN | 25 | 0 | 1.6% |
| PYTHON | 6 | 349 | 0.4% |
| MAKEFILE | 4 | 542 | 0.2% |
| JAVASCRIPT | 4 | 285 | 0.2% |
| PROTO | 4 | 279 | 0.2% |
| PLAINTEXT | 3 | 1 | 0.2% |
| DOCKERFILE | 2 | 126 | 0.1% |
| JSON | 2 | 142 | 0.1% |
| CPP | 2 | 21 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `3.267`
> **Composition Archetype:** `Flat Modular Platform` (z +3.27; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 20%, Declarative / Non-Code 16%, State Mutators Files 14%, Data / Markup / Trivial 12%, Generic / Templated Code Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1578 | 98.3% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 27 | 1.7% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 586*

**Composition by Extension & Reason:**
- `.toml`: 169x Unsupported Format (.toml), 3x Excluded (Unsupported Extension: '.toml'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 129x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 6 LOC)
- `no_extension`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.undeterminable)
- `.png`: 30x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ttf`: 20x Excluded (Explicitly Denied Extension: '.ttf')
- `.woff`: 20x Excluded (Explicitly Denied Extension: '.woff')
- `.woff2`: 20x Excluded (Explicitly Denied Extension: '.woff2')
- `.so`: 16x Excluded (Explicitly Denied Extension: '.so')
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bob`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 13852 LOC)
- `.css`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.3 | 10.2 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 47.0 | 54.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.2 | 10.1 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.2 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 13.7 | 6.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.9 | 12.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.8 | 2.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.7 | 82.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 18924 | 1072 | 30 | `accounts-db/src/accounts_db.rs` |
| cleanup | 476 | 161 | 0 | `programs/system/src/system_instruction.rs` |
| guards | 8670 | 1018 | 14 | `accounts-db/src/accounts_db.rs` |
| danger | 20513 | 949 | 29 | `ledger/src/blockstore.rs` |
| concurrency | 4920 | 431 | 7 | `rpc-client/src/nonblocking/rpc_client.rs` |
| connectivity | 15905 | 1141 | 25 | `runtime/src/bank.rs` |
| io | 3653 | 326 | 5 | `net/net.sh` |
| crypto | 0 | 0 | 0 | - |
| ipc | 215 | 72 | 0 | `net/net.sh` |
| time | 137 | 75 | 0 | `system-test/testnet-automation.sh` |
| serialization | 323 | 94 | 0 | `rpc/src/rpc.rs` |
| regex | 262 | 82 | 0 | `scripts/patch-crates.sh` |
| events | 3005 | 307 | 4 | `local-cluster/tests/local_cluster.rs` |
| tests | 19711 | 693 | 29 | `runtime/src/bank/tests.rs` |
| docs | 29844 | 842 | 24 | `rpc-client/src/nonblocking/rpc_client.rs` |
| debt | 2574 | 426 | 4 | `validator/src/main.rs` |
| mutation | 70380 | 1280 | 104 | `accounts-db/src/accounts_db.rs` |
| dead_code | 6878 | 873 | 10 | `rpc-client/src/rpc_client.rs` |
| credential | 134 | 24 | 0 | `net/scripts/solana-user-authorized_keys.sh` |
| threat | 555 | 217 | 1 | `sdk/bpf/c/bpf.mk` |
| ml_ai | 813 | 183 | 1 | `cli-output/src/cli_output.rs` |
| ui | 30 | 10 | 0 | `net/azure.sh` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.2**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `net/net.sh` (Hits: 170)
- `net/azure.sh` (Hits: 162)
- `net/colo.sh` (Hits: 162)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **system_program.rs** (`sdk/program/src/system_program.rs`) — 67 inbound connections
2. **system_transaction.rs** (`sdk/src/system_transaction.rs`) — 53 inbound connections
3. **thread.rs** (`perf/src/thread.rs`) — 18 inbound connections
4. **feature_set.rs** (`sdk/src/feature_set.rs`) — 17 inbound connections
5. **rust-version.sh** (`ci/rust-version.sh`) — 16 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **rpc.rs** (`rpc/src/rpc.rs`) — 239 outbound dependencies
2. **bank.rs** (`runtime/src/bank.rs`) — 234 outbound dependencies
3. **tests.rs** (`runtime/src/bank/tests.rs`) — 179 outbound dependencies
4. **validator.rs** (`core/src/validator.rs`) — 170 outbound dependencies
5. **accounts_db.rs** (`accounts-db/src/accounts_db.rs`) — 168 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `process_loader_upgradeable_instruction` **(Compute Cores)** (@ `programs/bpf_loader/src/lib.rs`) -> Impact: **355.5** | LOC: 830
- `new` **(Many-Argument Workhorses)** (@ `core/src/validator.rs`) -> Impact: **348.1** | LOC: 963
- `usage` **(Many-Argument Workhorses)** (@ `net/net.sh`) -> Impact: **233.2** | LOC: 784
- `new` **(Many-Argument Workhorses)** (@ `core/src/replay_stage.rs`) -> Impact: **197.1** | LOC: 679
- `run_accounts_bench` **(Many-Argument Workhorses)** (@ `accounts-cluster-bench/src/main.rs`) -> Impact: **190.7** | LOC: 297
- `process_instruction` **(Many-Argument Workhorses)** (@ `programs/sbf/rust/invoke/src/processor.rs`) -> Impact: **188.0** | LOC: 1280
- `process_catchup` **(Many-Argument Workhorses)** (@ `cli/src/cluster_query.rs`) -> Impact: **183.2** | LOC: 213
- `process_program_deploy` **(Many-Argument Workhorses)** (@ `cli/src/program.rs`) -> Impact: **181.6** | LOC: 190
  * *Intent:* /// Deploy program using upgradeable loader. It also can process program upgrades
- `main` **(I/O & Config Routines)** (@ `validator/src/main.rs`) -> Impact: **172.2** | LOC: 1183
- `run_transactions_dos` **(Many-Argument Workhorses)** (@ `transaction-dos/src/main.rs`) -> Impact: **158.3** | LOC: 287
  * *Intent:* /// creates large transactions that all touch the same set of accounts, /// so they can't be parallelized ///

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `accounts-db/src` | 39 | 12411.12 | 11.55% | 46.47% |
| `core/src` | 41 | 8196.24 | 9.03% | 35.02% |
| `cli/src` | 20 | 7867.96 | 8.83% | 10.52% |
| `ledger/src` | 31 | 7730.28 | 8.16% | 32.24% |
| `runtime/src` | 34 | 7272.9 | 5.7% | 29.43% |
| `storage-bigtable/src` | 6 | 6092.48 | 13.6% | 14.86% |
| `gossip/src` | 26 | 5209.78 | 9.0% | 24.78% |
| `rpc/src` | 16 | 4624.12 | 8.48% | 22.17% |
| `core/src/repair` | 16 | 4054.1 | 8.25% | 24.84% |
| `net` | 10 | 3895.4 | 57.58% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `bench-tps/src/bench_tps_client.rs` -> **100.0%** Exposure
- `core/src/banking_stage/scheduler_messages.rs` -> **100.0%** Exposure
- `frozen-abi/src/abi_digester.rs` -> **100.0%** Exposure
- `ledger/src/shred/traits.rs` -> **100.0%** Exposure
- `local-cluster/src/cluster.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.buildkite/scripts/common.sh` -> **100.0%** Exposure
- `ci/channel-info.sh` -> **100.0%** Exposure
- `ci/check-crates.sh` -> **100.0%** Exposure
- `ci/common/limit-threads.sh` -> **100.0%** Exposure
- `ci/run-local.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `runtime/src/bank/tests.rs` -> **241** Orphaned Functions | **0** Duplicates
- `accounts-db/src/accounts_db.rs` -> **187** Orphaned Functions | **12** Duplicates
- `rpc-client/src/rpc_client.rs` -> **123** Orphaned Functions | **2** Duplicates
- `core/src/consensus.rs` -> **82** Orphaned Functions | **0** Duplicates
- `rpc-client/src/nonblocking/rpc_client.rs` -> **75** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `net/scripts/solana-user-authorized_keys.sh` -> **100.0%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `21897` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `storage-bigtable/src/pki-goog-roots.pem` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `accounts-db/src/accounts_db.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 4858.2 | **LOC:** 17766 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **168**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (64.3%), Guard Balance (formerly Safety Score) (59.4%), Debt Markers (formerly Tech Debt) (45.3%), Connectivity (formerly Api Exposure) (9.7%)
- **Documentation Coverage:** 73.628% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clean_accounts` **(Many-Argument Workhorses)** (Impact: 85.6)
    * *Intent:* // Purge zero lamport accounts and older rooted account states as garbage // collection // Only remo...
  * `generate_index` **(Many-Argument Workhorses)** (Impact: 66.6)
  * `scan_account_storage_no_bank` **(Many-Argument Workhorses)** (Impact: 64.9)
    * *Intent:* /// Scan through all the account storage in parallel. /// Returns a Vec of opened files. /// Each fi...
  * `retry_to_get_account_accessor` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `calc_delete_dependencies` **(Many-Argument Workhorses)** (Impact: 50.4)
    * *Intent:* /// increment store_counts to non-zero for all stores that can not be deleted. /// a store cannot be...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 208 instances
* *High Risk Execution (weighted view):* 10
* *Concurrency (weighted view):* 47
* *State Mutation (weighted view):* 1078
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 827`, `structural_boundaries: 3068`, `args: 855`, `func_start: 520`, `class_start: 55`
* *Risk/State:* `safety_bypasses: 292`, `high_risk_execution: 14`, `state_mutation: 662`, `dead_code: 37`, `fragile_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 187`
* *Architecture:* `io: 3`, `api: 289`, `concurrency: 42`, `import: 4`
* *Defense:* `safety: 127`, `doc: 504`, `test: 779`, `sync_locks: 72`, `immutability_locks: 37`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ACCOUNTS_INDEX_CONFIG_FOR_BENCHMARKS, ACCOUNTS_INDEX_CONFIG_FOR_TESTING, ALIGN_BOUNDARY_OFFSET, APPEND_VEC_MMAPPED_FILES_OPEN, Account, AccountMapEntry, AccountSecondaryIndexes, AccountSecondaryIndexesIncludeExclude...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ledger/src/blockstore.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 3230.56 | **LOC:** 10744 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **158**; blast radius 0.538; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.3%), Guard Balance (formerly Safety Score) (79.2%), Mutation Surface (formerly State Flux) (47.6%), Debt Markers (formerly Tech Debt) (7.7%)
- **Documentation Coverage:** 81.6701% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_insert_shreds` **(Many-Argument Workhorses)** (Impact: 105.0)
    * *Intent:* /// boolean indicates whether the corresponding shred is repaired or not. /// - `leader_schedule`: t...
  * `get_confirmed_signatures_for_address2` **(Many-Argument Workhorses)** (Impact: 88.2)
  * `check_insert_coding_shred` **(Many-Argument Workhorses)** (Impact: 71.8)
  * `test_get_confirmed_signatures_for_address2` **(I/O & Config Routines)** (Impact: 66.5)
  * `check_insert_data_shred` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* /// the dirty copy of the index meta. It will later be written to /// `cf::SlotMeta` in insert_shred...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 132 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 501
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 725`, `structural_boundaries: 1858`, `args: 467`, `func_start: 283`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 777`, `high_risk_execution: 13`, `state_mutation: 237`, `dead_code: 13`, `planned_debt: 2`
* *Architecture:* `api: 236`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 110`, `doc: 364`, `test: 652`, `sync_locks: 29`, `immutability_locks: 9`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, AtomicU64, BLOCKSTORE_DIRECTORY_ROCKS_FIFO, BLOCKSTORE_DIRECTORY_ROCKS_LEVEL, BTreeSet, BlockstoreOptions, Column, ColumnIndexDeprecation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/src/bank.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2718.96 | **LOC:** 8004 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **234**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.3%), Guard Balance (formerly Safety Score) (59.8%), Mutation Surface (formerly State Flux) (46.4%)
- **Documentation Coverage:** 58.7762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_and_execute_transactions` **(Many-Argument Workhorses)** (Impact: 76.2)
  * `eq` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `_new_from_parent` **(Many-Argument Workhorses)** (Impact: 41.1)
  * `collect_rent_from_accounts` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* /// Collect rent from `accounts` /// /// This fn is called inside a parallel loop from `collect_rent...
  * `calculate_stake_vote_rewards` **(Many-Argument Workhorses)** (Impact: 34.7)
    * *Intent:* /// Calculates epoch rewards for stake/vote accounts /// Returns vote rewards, stake rewards, and th...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 77 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 365
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 414`, `structural_boundaries: 957`, `args: 529`, `func_start: 374`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 116`, `high_risk_execution: 5`, `state_mutation: 211`, `dead_code: 22`, `planned_debt: 6`
* *Architecture:* `api: 413`, `concurrency: 21`, `import: 10`
* *Defense:* `safety: 89`, `doc: 462`, `test: 42`, `sync_locks: 63`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ACCOUNTS_DB_CONFIG_FOR_TESTING, Account, AccountSharedData, AccountStorageEntry, Accounts, AccountsDb, AccountsDbConfig, AccountsHash...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpc/src/rpc.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2450.22 | **LOC:** 9280 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **239**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.9%), Debt Markers (formerly Tech Debt) (22.2%), Mutation Surface (formerly State Flux) (16.4%)
- **Documentation Coverage:** 97.6879% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get_signatures_for_address` **(Many-Argument Workhorses)** (Impact: 64.4)
  * `simulate_transaction` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `get_block` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `get_blocks` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `get_stake_activation` **(Many-Argument Workhorses)** (Impact: 40.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 163
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 516`, `structural_boundaries: 1694`, `args: 453`, `func_start: 309`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 352`, `high_risk_execution: 5`, `state_mutation: 85`, `planned_debt: 9`, `fragile_debt: 1`, `unreferenced_by_name: 63`
* *Architecture:* `api: 90`, `concurrency: 53`, `import: 14`
* *Defense:* `safety: 159`, `doc: 15`, `test: 285`, `sync_locks: 34`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` *, ACCOUNTTYPE_ACCOUNT, AccountSecondaryIndexes, AddressLoader, Arc, AtomicU64, BlockCommitmentCache, BlockEncodingOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/replay_stage.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2272.1 | **LOC:** 8755 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **162**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.0%), Mutation Surface (formerly State Flux) (29.3%), Debt Markers (formerly Tech Debt) (19.5%)
- **Documentation Coverage:** 97.6378% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 197.1)
  * `process_replay_results` **(Many-Argument Workhorses)** (Impact: 120.5)
  * `dump_then_repair_correct_slots` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `select_vote_and_reset_forks` **(Many-Argument Workhorses)** (Impact: 68.6)
    * *Intent:* /// Given a `heaviest_bank` and a `heaviest_bank_on_same_voted_fork`, return /// a bank to vote on, ...
  * `maybe_start_leader` **(Many-Argument Workhorses)** (Impact: 59.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 52 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 1695`, `args: 254`, `func_start: 117`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 466`, `high_risk_execution: 11`, `state_mutation: 183`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 48`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 99`, `doc: 17`, `test: 325`, `sync_locks: 45`, `immutability_locks: 9`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Arc, AtomicU64, Bank, BankNotificationSenderConfig, BlockhashStatus, BlockstoreError, BlockstoreProcessorError, Builder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/src/bank/tests.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2184.64 | **LOC:** 13795 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **179**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (65.6%), Guard Balance (formerly Safety Score) (57.7%), Mutation Surface (formerly State Flux) (36.0%), Concurrency Surface (formerly Concurrency) (12.1%)
- **Documentation Coverage:** 90.4762% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_store_scan_consistency` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `test_bpf_loader_upgradeable_deploy_with_max_len` **(I/O & Config Routines)** (Impact: 38.1)
  * `test_fuzz_instructions` **(I/O & Config Routines)** (Impact: 36.9)
  * `test_bank_update_sysvar_account` **(I/O & Config Routines)** (Impact: 22.8)
  * `test_rent_complex` **(I/O & Config Routines)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 15
* *Memory Alloc (weighted view):* 189
* *State Mutation (weighted view):* 539
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 387`, `structural_boundaries: 2624`, `args: 454`, `func_start: 292`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 494`, `high_risk_execution: 5`, `state_mutation: 357`, `dead_code: 4`, `planned_debt: 4`, `unreferenced_by_name: 241`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 10`, `import: 8`
* *Defense:* `safety: 28`, `doc: 71`, `test: 1354`, `sync_locks: 8`, `immutability_locks: 21`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` *, Account, AccountSecondaryIndexes, AccountSharedData, Arc, AtomicU64, BlockTimestamp, CompiledInstruction...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/src/stake.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1641.9 | **LOC:** 5052 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **96**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%), Connectivity (formerly Api Exposure) (65.7%), Mutation Surface (formerly State Flux) (15.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_split_stake` **(Many-Argument Workhorses)** (Impact: 140.3)
  * `process_delegate_stake` **(Many-Argument Workhorses)** (Impact: 135.7)
  * `process_deactivate_stake_account` **(Many-Argument Workhorses)** (Impact: 119.2)
  * `process_stake_authorize` **(Many-Argument Workhorses)** (Impact: 115.2)
  * `process_create_stake_account` **(Many-Argument Workhorses)** (Impact: 112.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 89
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 608`, `args: 66`, `func_start: 37`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 201`, `state_mutation: 31`, `dead_code: 1`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 46`, `test: 57`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` App, Arg, ArgConstant, ArgGroup, ArgMatches, COMPUTE_UNIT_PRICE_ARG, CliBalance, CliCommand...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli-output/src/cli_output.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1610.74 | **LOC:** 3407 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **76**; blast radius 0.538; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.8%), Connectivity (formerly Api Exposure) (14.4%), Mutation Surface (formerly State Flux) (12.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fmt` **(Many-Argument Workhorses)** (Impact: 83.5)
  * `fmt` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `show_votes_and_credits` **(Many-Argument Workhorses)** (Impact: 54.8)
  * `fmt` **(Many-Argument Workhorses)** (Impact: 51.4)
  * `fmt` **(Compute Cores)** (Impact: 41.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 40
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 630`, `structural_boundaries: 490`, `args: 154`, `func_start: 109`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 1`, `state_mutation: 16`, `duplicate_logic: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 347`, `import: 3`
* *Defense:* `safety: 64`, `test: 31`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arg, BuildBalanceMessageConfig, Emoji, EncodedTransaction, Engine, HashMap, LandedVote, Lockup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `rpc-client/src/nonblocking/rpc_client.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1561.88 | **LOC:** 5459 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **84**; blast radius 0.538; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Test Surface (formerly Verification) (80.0%), Dead Code Surface (formerly Dead Code) (71.5%), Debt Markers (formerly Tech Debt) (68.6%)
- **Documentation Coverage:** 36.7491% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `confirm_transaction_with_spinner` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `send_and_confirm_transaction` **(Compute Cores)** (Impact: 30.3)
    * *Intent:* /// # system_transaction, /// # }; /// # futures::executor::block_on(async { /// # let rpc_client = ...
  * `send_transaction_with_config` **(Many-Argument Workhorses)** (Impact: 29.5)
    * *Intent:* /// let latest_blockhash = rpc_client.get_latest_blockhash().await?; /// let tx = system_transaction...
  * `get_recent_blockhash_with_commitment` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `get_token_account_with_commitment` **(Many-Argument Workhorses)** (Impact: 22.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 25 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 473
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 425`, `args: 208`, `func_start: 153`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `dead_code: 214`, `unreferenced_by_name: 75`
* *Architecture:* `api: 148`, `concurrency: 348`, `import: 13`
* *Defense:* `safety: 32`, `doc: 2970`, `test: 1`, `sync_locks: 3`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` *, CommitmentLevel, DEFAULT_MS_PER_SLOT, EncodedConfirmedTransactionWithStatusMeta, Engine, ErrorKind, FeeRateGovernor, Instant...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `cli/src/program.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1464.08 | **LOC:** 3720 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **101**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.0%), Connectivity (formerly Api Exposure) (42.1%), Mutation Surface (formerly State Flux) (17.0%)
- **Documentation Coverage:** 95.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_program_deploy` **(Many-Argument Workhorses)** (Impact: 181.6)
    * *Intent:* /// Deploy program using upgradeable loader. It also can process program upgrades
  * `parse_program_subcommand` **(Many-Argument Workhorses)** (Impact: 124.6)
  * `do_process_program_write_and_deploy` **(Many-Argument Workhorses)** (Impact: 116.8)
  * `process_show` **(Many-Argument Workhorses)** (Impact: 100.8)
  * `send_deploy_messages` **(Many-Argument Workhorses)** (Impact: 81.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 74
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 495`, `args: 64`, `func_start: 37`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 124`, `high_risk_execution: 1`, `state_mutation: 30`, `dead_code: 3`
* *Architecture:* `io: 8`, `api: 14`, `import: 7`
* *Defense:* `safety: 76`, `doc: 2`, `test: 40`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AppSettings, Arg, ArgMatches, CliCommand, CliCommandInfo, CliConfig, CliError, CliProgram...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gossip/src/cluster_info.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1454.58 | **LOC:** 4739 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **140**; blast radius 0.538; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Debt Markers (formerly Tech Debt) (49.8%), Mutation Surface (formerly State Flux) (34.2%)
- **Documentation Coverage:** 87.156% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_packets` **(Many-Argument Workhorses)** (Impact: 49.3)
  * `filter_on_shred_version` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* // Filters out values from nodes with different shred-version.
  * `gossip` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* /// randomly pick a node and ask them for updates asynchronously
  * `handle_pull_requests` **(Many-Argument Workhorses)** (Impact: 34.8)
    * *Intent:* // Pull requests take an incoming bloom filter of contained entries from a node // and tries to send...
  * `handle_batch_push_messages` **(Many-Argument Workhorses)** (Impact: 31.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 321`, `structural_boundaries: 1102`, `args: 294`, `func_start: 159`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 202`, `high_risk_execution: 13`, `state_mutation: 87`, `dead_code: 1`, `planned_debt: 10`, `unreferenced_by_name: 65`
* *Architecture:* `io: 2`, `api: 92`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 42`, `doc: 65`, `test: 213`, `sync_locks: 30`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Arc, Builder, CRDS_GOSSIP_PULL_CRDS_TIMEOUT_MS, ContactInfo, Counter, CrdsData, CrdsTimeouts, CrdsValue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `accounts-db/src/accounts_index.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1273.86 | **LOC:** 4222 | **CtrlFlow:** 5.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **55**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (66.1%), Mutation Surface (formerly State Flux) (62.7%), Guard Balance (formerly Safety Score) (58.0%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 72.4696% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_checked_scan_accounts` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `test_new_entry_code_paths_helper` **(Many-Argument Workhorses)** (Impact: 32.9)
  * `latest_slot` **(Stateful Encapsulated Methods)** (Impact: 31.0)
    * *Intent:* // Given a SlotSlice `L`, a list of ancestors and a maximum slot, find the latest element // in `L`,...
  * `scan` **(Many-Argument Workhorses)** (Impact: 22.5)
    * *Intent:* /// - callback fn to run for each pubkey in the accounts index /// - avoid_callback_result. If it is...
  * `update_spl_token_secondary_indexes` **(Many-Argument Workhorses)** (Impact: 22.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 64 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 684`, `args: 241`, `func_start: 169`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 87`, `high_risk_execution: 15`, `state_mutation: 127`, `dead_code: 10`, `planned_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 62`
* *Architecture:* `api: 155`, `concurrency: 16`, `import: 2`
* *Defense:* `safety: 29`, `doc: 121`, `test: 289`, `sync_locks: 23`, `immutability_locks: 9`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Arc, AtomicAge, AtomicU64, AtomicUsize, Bound::Excluded, BucketMapHolder, GenericTokenAccount, HashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `programs/bpf_loader/src/syscalls/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1178.0 | **LOC:** 4128 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **148**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.8%), Debt Markers (formerly Tech Debt) (31.6%), Mutation Surface (formerly State Flux) (13.9%)
- **Documentation Coverage:** 84.0426% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `rust` **(Many-Argument Workhorses)** (Impact: 122.8)
  * `create_program_runtime_environment_v1` **(Many-Argument Workhorses)** (Impact: 100.0)
  * `rust` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `rust` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `rust` **(Many-Argument Workhorses)** (Impact: 34.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 816`, `args: 100`, `func_start: 90`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 149`, `high_risk_execution: 2`, `state_mutation: 52`, `duplicate_logic: 15`, `unreferenced_by_name: 26`
* *Architecture:* `api: 12`, `import: 16`
* *Defense:* `safety: 15`, `doc: 27`, `test: 119`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` ALT_BN128_ADDITION_OUTPUT_LEN, ALT_BN128_G1_COMPRESS, ALT_BN128_G1_DECOMPRESS, ALT_BN128_G2_COMPRESS, ALT_BN128_G2_DECOMPRESS, ALT_BN128_MUL, ALT_BN128_MULTIPLICATION_OUTPUT_LEN, ALT_BN128_PAIRING...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `ledger/src/blockstore_processor.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1150.88 | **LOC:** 4770 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **127**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.4%), Mutation Surface (formerly State Flux) (38.2%), Debt Markers (formerly Tech Debt) (31.7%), Connectivity (formerly Api Exposure) (10.0%)
- **Documentation Coverage:** 88.7755% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `load_frozen_forks` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* /// Starting with the root slot corresponding to `start_slot_meta`, iteratively /// find and process...
  * `confirm_slot_entries` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `process_entries` **(Many-Argument Workhorses)** (Impact: 50.5)
  * `process_blockstore_from_root` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* /// Process blockstore from a known root bank
  * `rebatch_and_execute_batches` **(Many-Argument Workhorses)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 811`, `args: 150`, `func_start: 85`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 146`, `high_risk_execution: 4`, `state_mutation: 103`, `dead_code: 5`, `planned_debt: 1`, `unreferenced_by_name: 45`
* *Architecture:* `api: 71`, `concurrency: 5`, `import: 3`
* *Defense:* `safety: 30`, `doc: 46`, `test: 208`, `sync_locks: 17`, `immutability_locks: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` AccountsDbConfig, Arc, BlockstoreOptions, Entry, EntryNotifierSender, EntrySlice, EntryType, EntryVerificationStatus...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `streamer/src/nonblocking/quic.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1092.94 | **LOC:** 2033 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.538; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (85.7%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.5075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setup_connection` **(Many-Argument Workhorses)** (Impact: 58.4)
  * `handle_connection` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `handle_chunk` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* // Return true if the server should drop the stream
  * `packet_batch_sender` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `run_server` **(Many-Argument Workhorses)** (Impact: 23.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 42 instances
* *Amplified Cascading Flux:* 50 instances
* *Concurrency (weighted view):* 330
* *Memory Alloc (weighted view):* 24
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 143`, `structural_boundaries: 416`, `args: 80`, `func_start: 56`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 93`, `dead_code: 4`, `unreferenced_by_name: 20`
* *Architecture:* `io: 3`, `api: 20`, `concurrency: 120`, `import: 6`
* *Defense:* `safety: 35`, `doc: 1`, `test: 78`, `sync_locks: 22`, `immutability_locks: 14`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` IdleTimeout, MAX_UNSTAKED_CONNECTIONS, QUIC_MAX_TIMEOUT, Receiver, TransportConfig, assert_matches::assert_matches, async_channel::unbounded, crate::
            nonblocking::quic::compute_max_allowed_uni_streams...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `programs/stake/src/stake_state.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1072.1 | **LOC:** 2886 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **41**; blast radius 0.653; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Connectivity (formerly Api Exposure) (51.7%), Mutation Surface (formerly State Flux) (25.0%)
- **Documentation Coverage:** 95.1456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `split` **(Many-Argument Workhorses)** (Impact: 112.3)
  * `withdraw` **(Many-Argument Workhorses)** (Impact: 111.4)
  * `redelegate` **(Many-Argument Workhorses)** (Impact: 73.7)
  * `merge` **(Many-Argument Workhorses)** (Impact: 63.2)
  * `deactivate_delinquent` **(Many-Argument Workhorses)** (Impact: 50.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 80
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 252`, `structural_boundaries: 387`, `args: 75`, `func_start: 59`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 55`, `high_risk_execution: 1`, `state_mutation: 44`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 46`, `import: 4`
* *Defense:* `safety: 9`, `doc: 42`, `test: 113`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.653
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000623
  * `Imports (Out-Degree: 0):` AccountSharedData, Epoch, FeatureSet, IndexOfAccount, InstructionContext, InstructionError, ReadableAccount, StakeError...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cli/src/cluster_query.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1030.48 | **LOC:** 2407 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **102**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Mutation Surface (formerly State Flux) (55.6%), Debt Markers (formerly Tech Debt) (39.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process_catchup` **(Many-Argument Workhorses)** (Impact: 183.2)
  * `process_ping` **(Many-Argument Workhorses)** (Impact: 90.8)
  * `process_show_block_production` **(Many-Argument Workhorses)** (Impact: 82.6)
  * `process_show_stakes` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `process_show_validators` **(Many-Argument Workhorses)** (Impact: 46.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 145
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 369`, `args: 88`, `func_start: 53`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 2`, `unreferenced_by_name: 46`
* *Architecture:* `api: 54`, `concurrency: 1`, `import: 3`
* *Defense:* `safety: 36`, `test: 15`, `sync_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` *, App, AppSettings, Arc, Arg, ArgMatches, BLOCKHASH_ARG, COMPUTE_UNIT_PRICE_ARG...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/consensus.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1023.7 | **LOC:** 3604 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **78**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (86.2%), Guard Balance (formerly Safety Score) (60.6%), Mutation Surface (formerly State Flux) (43.8%), Concurrency Surface (formerly Concurrency) (15.8%)
- **Documentation Coverage:** 94.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `make_check_switch_threshold_decision` **(Many-Argument Workhorses)** (Impact: 138.5)
  * `adjust_lockouts_with_slot_history` **(Many-Argument Workhorses)** (Impact: 52.0)
  * `collect_vote_lockouts` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `adjust_lockouts_after_replay` **(Many-Argument Workhorses)** (Impact: 26.1)
    * *Intent:* // The tower root can be older/newer if the validator booted from a newer/older snapshot, so // towe...
  * `check_vote_stake_threshold` **(Many-Argument Workhorses)** (Impact: 24.9)
    * *Intent:* /// Checks a single vote threshold for `slot`
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 576`, `args: 182`, `func_start: 130`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 116`, `high_risk_execution: 5`, `state_mutation: 105`, `dead_code: 7`, `planned_debt: 3`, `unreferenced_by_name: 82`
* *Architecture:* `io: 2`, `api: 70`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 33`, `doc: 11`, `test: 252`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AccountSharedData, BlockTimestamp, Deref, HashSet, LandedVote, Lockout, MAX_LOCKOUT_HISTORY, OpenOptions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `local-cluster/tests/local_cluster.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1012.26 | **LOC:** 5699 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **123**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.3%), Dead Code Surface (formerly Dead Code) (5.0%), Complexity Load (formerly Cognitive Load) (4.7%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_test_optimistic_confirmation_violation_with_or_without_tower` **(Compute Cores)** (Impact: 53.5)
    * *Intent:* // // The fork choice rule weights look like: // // S0 -> S1 -> S2 (ABC) // | // -> S4 (C) -> S5 // ...
  * `test_incremental_snapshot_download_with_crossing_full_snapshot_interval_at_startup` **(I/O & Config Routines)** (Impact: 51.6)
    * *Intent:* /// snapshot while processing the blockstore so that once the background services start up, there //...
  * `test_duplicate_shreds_switch_failure` **(I/O & Config Routines)** (Impact: 47.2)
    * *Intent:* // We want to simulate the following: // /--- 1 --- 3 (duplicate block) // 0 // \--- 2 // // 1. > DU...
  * `setup_transfer_scan_threads` **(Many-Argument Workhorses)** (Impact: 44.9)
  * `test_boot_from_local_state` **(I/O & Config Routines)** (Impact: 37.6)
    * *Intent:* /// Test fastboot to ensure a node can boot from local state and still produce correct snapshots ///...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 37 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 306`, `structural_boundaries: 1030`, `args: 151`, `func_start: 66`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 229`, `high_risk_execution: 7`, `state_mutation: 101`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 51`
* *Architecture:* `io: 7`, `concurrency: 8`, `import: 1`
* *Defense:* `safety: 39`, `doc: 27`, `test: 127`, `sync_locks: 19`, `immutability_locks: 4`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Arc, AtomicUsize, BlockVerificationMethod, Blockstore, BroadcastStageType, Builder, ClusterPartition, ClusterValidatorInfo...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/validator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 962.32 | **LOC:** 2883 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **170**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (63.9%), Guard Balance (formerly Safety Score) (62.3%), Mutation Surface (formerly State Flux) (20.4%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `new` **(Many-Argument Workhorses)** (Impact: 348.1)
  * `load_blockstore` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `wait_for_supermajority` **(Many-Argument Workhorses)** (Impact: 41.0)
    * *Intent:* // Return if the validator waited on other nodes to start. In this case // it should not wait for on...
  * `get_stake_percent_in_gossip` **(Many-Argument Workhorses)** (Impact: 34.7)
    * *Intent:* // Get the activated stake percentage (based on the provided bank) that is visible in gossip
  * `join` **(Defensive Guards)** (Impact: 29.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 19 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 33
* *State Mutation (weighted view):* 70
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 360`, `args: 92`, `func_start: 40`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 32`, `dead_code: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 95`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 50`, `doc: 9`, `test: 37`, `sync_locks: 36`, `immutability_locks: 7`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AbsRequestSender, AccountsBackgroundService, AccountsDbConfig, Arc, AtomicU64, BankingTracer, BlockstoreError, BlockstoreRecoveryMode...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/src/consensus/heaviest_subtree_fork_choice.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 961.96 | **LOC:** 4619 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **37**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (64.8%), Debt Markers (formerly Tech Debt) (40.2%), Mutation Surface (formerly State Flux) (37.3%), Complexity Load (formerly Cognitive Load) (9.5%)
- **Documentation Coverage:** 89.2617% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `generate_update_operations` **(Many-Argument Workhorses)** (Impact: 41.7)
  * `propagate_new_leaf` **(Many-Argument Workhorses)** (Impact: 28.1)
    * *Intent:* /// To be called when `slot_hash_key` has been added to `self.fork_infos`, before any /// aggregate ...
  * `aggregate_slot` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `test_mark_valid_then_descendant_invalid` **(I/O & Config Routines)** (Impact: 22.3)
  * `purge_prune` **(Defensive Guards)** (Impact: 17.6)
    * *Intent:* /// Purges all slots < `new_root` and prunes subtrees with slots > `new_root` not descending from `n...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 170
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 200`, `structural_boundaries: 598`, `args: 181`, `func_start: 119`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 201`, `high_risk_execution: 6`, `state_mutation: 88`, `dead_code: 7`, `planned_debt: 1`, `unreferenced_by_name: 50`
* *Architecture:* `api: 34`, `import: 3`
* *Defense:* `safety: 26`, `doc: 26`, `test: 378`, `sync_locks: 3`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BTreeMap, BTreeSet, HashMap, HashSet, RwLock, Slot, Tower, TreeWalk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `programs/stake/src/stake_instruction.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 956.04 | **LOC:** 7916 | **CtrlFlow:** 2.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **86**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.9%), Mutation Surface (formerly State Flux) (19.2%), Debt Markers (formerly Tech Debt) (13.6%)
- **Documentation Coverage:** 83.871% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_redelegate` **(I/O & Config Routines)** (Impact: 54.6)
  * `process_instruction_as_one_arg` **(Many-Argument Workhorses)** (Impact: 40.5)
  * `test_merge_active_stake` **(Compute Cores)** (Impact: 35.1)
  * `test_split_require_rent_exempt_destination` **(Many-Argument Workhorses)** (Impact: 30.4)
  * `test_deactivate_delinquent` **(I/O & Config Routines)** (Impact: 20.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 5
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 891`, `args: 79`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 285`, `high_risk_execution: 13`, `state_mutation: 149`, `dead_code: 4`, `unreferenced_by_name: 47`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 21`, `doc: 53`, `test: 111`, `immutability_locks: 1`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` AccountSharedData, AuthorizeCheckedWithSeedArgs, AuthorizeWithSeedArgs, Authorized, Delegation, Epoch, Instruction, InstructionContext...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `runtime/src/snapshot_utils.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 928.92 | **LOC:** 3215 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **67**; blast radius 3.119; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.8%), Mutation Surface (formerly State Flux) (14.2%)
- **Documentation Coverage:** 46.3855% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `archive_snapshot_package` **(Many-Argument Workhorses)** (Impact: 98.2)
    * *Intent:* /// Make a snapshot archive out of the snapshot package
  * `rebuild_storages_from_snapshot_dir` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* /// Performs the common tasks when deserializing a snapshot /// /// Handles reading the snapshot fil...
  * `purge_old_snapshot_archives` **(Many-Argument Workhorses)** (Impact: 27.0)
  * `verify_snapshot_archive` **(Many-Argument Workhorses)** (Impact: 21.8)
  * `clean_orphaned_account_snapshot_dirs` **(Compute Cores)** (Impact: 21.6)
    * *Intent:* /// The account snapshot directories under <account_path>/snapshot/<slot> contain account files hard...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 526`, `args: 200`, `func_start: 97`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 120`, `state_mutation: 27`, `dead_code: 5`
* *Architecture:* `io: 29`, `api: 113`, `concurrency: 1`, `import: 5`
* *Defense:* `safety: 24`, `doc: 141`, `test: 85`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.119
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005799
  * `Imports (Out-Degree: 0):` ACCOUNTS_RUN_DIR, ACCOUNTS_SNAPSHOT_DIR, Archive, ArchiveSnapshotPackageError, AtomicAppendVecId, BufWriter, Error, HashSet...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `programs/bpf_loader/src/syscalls/cpi.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 914.38 | **LOC:** 2943 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **35**; blast radius 0.538; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%), Mutation Surface (formerly State Flux) (23.5%), Debt Markers (formerly Tech Debt) (14.0%)
- **Documentation Coverage:** 92.1569% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `update_caller_account` **(Many-Argument Workhorses)** (Impact: 118.3)
    * *Intent:* // Update the given account after executing CPI. // // caller_account and callee_account describe to...
  * `translate_and_update_accounts` **(Many-Argument Workhorses)** (Impact: 75.8)
    * *Intent:* // Finish translating accounts, build CallerAccount values and update callee // accounts in preparat...
  * `cpi_common` **(Many-Argument Workhorses)** (Impact: 64.6)
    * *Intent:* /// Call process instruction, common to both Rust and C
  * `update_callee_account` **(Many-Argument Workhorses)** (Impact: 56.3)
    * *Intent:* // Update the given account before executing CPI. // // caller_account and callee_account describe t...
  * `from_account_info` **(Many-Argument Workhorses)** (Impact: 55.7)
    * *Intent:* // Create a CallerAccount given an AccountInfo.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 473`, `args: 80`, `func_start: 51`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 38`, `dead_code: 2`, `duplicate_logic: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 1`, `import: 2`
* *Defense:* `safety: 18`, `doc: 13`, `test: 63`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.538
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AccountSharedData, MAX_CPI_INSTRUCTION_ACCOUNTS, MAX_CPI_INSTRUCTION_DATA_LEN, MemoryState, ReadableAccount, RefCell, assert_matches::assert_matches, clock::Epoch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `ci/rust-version.sh` -> **Severity: 0.965** (Embedded: 0.01 * Error Risk: 96.806%)
- `perf/src/thread.rs` -> **Severity: 0.799** (Embedded: 0.0112 * Error Risk: 71.2371%)
- `scripts/read-cargo-variable.sh` -> **Severity: 0.753** (Embedded: 0.0091 * Error Risk: 82.388%)
- `sdk/src/feature_set.rs` -> **Severity: 0.58** (Embedded: 0.0118 * Error Risk: 49.1338%)
- `sdk/program/src/bpf_loader_upgradeable.rs` -> **Severity: 0.472** (Embedded: 0.0087 * Error Risk: 54.1239%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/read-cargo-variable.sh` -> **Severity: 712.6** (Blast Radius: 7.126 * Doc Risk: 100.0%)
- `ledger/src/shred/merkle.rs` -> **Severity: 440.7** (Blast Radius: 4.407 * Doc Risk: 100.0%)
- `sdk/src/feature_set.rs` -> **Severity: 372.11** (Blast Radius: 6.011 * Doc Risk: 61.9048%)
- `perf/src/thread.rs` -> **Severity: 310.04** (Blast Radius: 7.751 * Doc Risk: 40.0%)
- `sdk/program/src/serde_varint.rs` -> **Severity: 277.8** (Blast Radius: 2.778 * Doc Risk: 100.0%)

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
