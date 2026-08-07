# ARCHITECTURAL_BRIEF: substrate
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_rust/substrate` |
| **Timestamp** | `2026-08-07T04:08:16.526824+00:00` |
| **Scan Duration** | `7.54s` |
| **Git Branch** | `master` |
| **Git Commit** | `033d4e86cc7eff0066cd376b9375f815761d653c` |
| **Git Remote** | `https://github.com/paritytech/substrate.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1551 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 2683 |
| Analyzed Artifacts (Scanned) | 1756 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 927 |
| Total LOC | 331025 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 65.4% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8698 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2178 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1104 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 19 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 1528 | 325805 | 87.0% |
| MARKDOWN | 185 | 0 | 10.5% |
| SHELL | 12 | 492 | 0.7% |
| JSON | 8 | 2957 | 0.5% |
| YAML | 7 | 1260 | 0.4% |
| PROTO | 5 | 128 | 0.3% |
| DOCKERFILE | 3 | 73 | 0.2% |
| HTML | 3 | 220 | 0.2% |
| PLAINTEXT | 2 | 0 | 0.1% |
| NIX | 1 | 20 | 0.1% |
| PYTHON | 1 | 27 | 0.1% |
| JAVASCRIPT | 1 | 43 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `3.993`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 573 | 32.6% |
| file_cluster_8 | 503 | 28.6% |
| file_cluster_13 | 262 | 14.9% |
| file_cluster_0 | 145 | 8.3% |
| file_cluster_4 | 46 | 2.6% |
| file_cluster_17 | 19 | 1.1% |
| file_cluster_7 | 14 | 0.8% |
| file_cluster_11 | 3 | 0.2% |
| file_cluster_12 | 2 | 0.1% |
| file_cluster_6 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 187 | 10.6% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 927*

**Composition by Extension & Reason:**
- `.rs`: 277x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 3927 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1461 LOC)
- `.toml`: 272x Unsupported Format (.toml), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Unsupported Extension: '.toml')
- `.stderr`: 208x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 17x Excluded (Unsupported Extension: '.stderr')
- `.wat`: 48x Excluded (Unsupported Extension: '.wat'), 1x Excluded (Embedded Hex Payload: 4488 hex tokens in 2294 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Unsupported Format (.undeterminable), 1x Excluded (Unsupported Extension: '.dockerignore')
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 2813 LOC)
- `.wasm`: 4x Excluded (Unsupported Extension: '.wasm'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dat`: 4x Excluded (Binary Format Detected)
- `.zndsl`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.zndsl')
- `.yaml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.adoc`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 10.6 | 5.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 25.0 | 22.2 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 48.7 | 46.7 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.4 | 2.3 | 0.0 |
| API Exposure | 0.0 | 9.6 | 3.4 | 3.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.6 | 12.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 97.6 | 2.4 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 95.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 19.5 | 11.9 | 11.9 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/ci/common/lib.sh` (Hits: 32)
- `client/offchain/src/api/http.rs` (Hits: 24)
- `scripts/ci/gitlab/publish_draft_release.sh` (Hits: 19)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **benchmarks.rs** (`frame/bags-list/src/benchmarks.rs`) — 18 inbound connections
2. **log.rs** (`frame/staking/reward-curve/src/log.rs`) — 14 inbound connections
3. **mem.rs** (`primitives/database/src/mem.rs`) — 10 inbound connections
4. **unhashed.rs** (`frame/support/src/storage/unhashed.rs`) — 7 inbound connections
5. **ready.rs** (`client/transaction-pool/src/graph/ready.rs`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`frame/support/src/lib.rs`) — 190 outbound dependencies
2. **traits.rs** (`frame/support/src/traits.rs`) — 177 outbound dependencies
3. **lib.rs** (`bin/node/runtime/src/lib.rs`) — 151 outbound dependencies
4. **lib.rs** (`client/network/sync/src/lib.rs`) — 120 outbound dependencies
5. **client.rs** (`client/service/src/client/client.rs`) — 120 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `on_block_data` (@ `client/network/sync/src/lib.rs`) -> Impact: **656.0** | LOC: 1853
- `on_block_justification` (@ `client/network/sync/src/lib.rs`) -> Impact: **582.6** | LOC: 1859
- `try_commit_operation` (@ `client/db/src/lib.rs`) -> Impact: **358.0** | LOC: 1757
- `on_blocks_processed` (@ `client/network/sync/src/lib.rs`) -> Impact: **305.8** | LOC: 1120
- `execute_and_import_block` (@ `client/service/src/client/client.rs`) -> Impact: **268.0** | LOC: 248
- `import` (@ `utils/fork-tree/src/lib.rs`) -> Impact: **191.1** | LOC: 276
  * *Intent:* /// Rebalance the tree. /// /// For each tree level sort child nodes by max branch depth (decreasing). /// /// Most operations in the tree are perform...
- `bond` (@ `frame/staking/src/pallet/mod.rs`) -> Impact: **188.4** | LOC: 682
  * *Intent:* /// The maximum number of `unlocking` chunks a [`StakingLedger`] can /// have. Effectively determines how many unique eras a staker may be /// unbondi...
- `on_connection_handler_event` (@ `client/network/src/protocol/notifications/behaviour.rs`) -> Impact: **185.6** | LOC: 528
- `benchmarks` (@ `frame/support/procedural/src/benchmark.rs`) -> Impact: **177.2** | LOC: 593
  * *Intent:* /// Parses and expands a `#[benchmarks]` or `#[instance_benchmarks]` invocation
- `transfer_and_die` (@ `frame/assets/src/functions.rs`) -> Impact: **172.4** | LOC: 394
  * *Intent:* /// of the debit. /// /// - `amount`: The amount desired to be debited. The actual amount returned for debit may be /// less (in the case of `best_eff...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `client/network/sync/src` | 11 | 4015.84 | 12.5% | 21.03% |
| `client/consensus/grandpa/src` | 13 | 3041.54 | 14.35% | 50.2% |
| `client/db/src` | 10 | 2923.2 | 17.29% | 49.84% |
| `primitives/state-machine/src` | 11 | 2766.68 | 14.99% | 64.89% |
| `client/rpc-spec-v2/src/chain_head` | 9 | 2527.88 | 17.66% | 34.48% |
| `frame/contracts/src` | 10 | 2322.68 | 8.23% | 76.56% |
| `client/network/src` | 17 | 2157.04 | 8.64% | 49.31% |
| `primitives/core/src` | 15 | 2091.64 | 11.92% | 77.09% |
| `frame/support/procedural/src/pallet/parse` | 17 | 2079.4 | 11.87% | 17.48% |
| `primitives/arithmetic/src` | 7 | 1869.62 | 7.24% | 76.65% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `bin/node-template/node/build.rs` -> **100.0%** Exposure
- `bin/node-template/pallets/template/src/weights.rs` -> **100.0%** Exposure
- `bin/node/cli/bin/main.rs` -> **100.0%** Exposure
- `bin/node/cli/src/benchmarking.rs` -> **100.0%** Exposure
- `bin/utils/subkey/src/main.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/node/bench/src/generator.rs` -> **100.0%** Exposure
- `client/chain-spec/src/lib.rs` -> **100.0%** Exposure
- `client/consensus/common/src/import_queue/basic_queue.rs` -> **100.0%** Exposure
- `client/consensus/common/src/import_queue/buffered_link.rs` -> **100.0%** Exposure
- `client/consensus/common/src/import_queue/mock.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `primitives/arithmetic/src/per_things.rs` -> **36** Orphaned Functions | **48** Duplicates
- `frame/support/src/traits/misc.rs` -> **38** Orphaned Functions | **41** Duplicates
- `primitives/core/src/crypto.rs` -> **13** Orphaned Functions | **65** Duplicates
- `frame/staking/src/tests.rs` -> **73** Orphaned Functions | **0** Duplicates
- `primitives/runtime/src/traits.rs` -> **0** Orphaned Functions | **69** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`client/tracing/src/logging/stderr_writer.rs`** -> AI Confidence: **99.48%**
2. **`frame/balances/src/tests/fungible_tests.rs`** -> AI Confidence: **99.48%**
3. **`frame/conviction-voting/src/tests.rs`** -> AI Confidence: **99.48%**
4. **`frame/salary/src/tests.rs`** -> AI Confidence: **99.48%**
5. **`client/consensus/beefy/src/metrics.rs`** -> AI Confidence: **99.39%**
6. **`client/network/src/service/metrics.rs`** -> AI Confidence: **99.39%**
7. **`frame/bags-list/src/tests.rs`** -> AI Confidence: **99.39%**
8. **`frame/assets/src/tests.rs`** -> AI Confidence: **99.35%**
9. **`bin/node-template/node/src/command.rs`** -> AI Confidence: **99.31%**
10. **`bin/utils/chain-spec-builder/src/lib.rs`** -> AI Confidence: **99.31%**
11. **`client/cli/src/commands/run_cmd.rs`** -> AI Confidence: **99.31%**
12. **`client/cli/src/config.rs`** -> AI Confidence: **99.31%**
13. **`client/consensus/common/src/metrics.rs`** -> AI Confidence: **99.31%**
14. **`client/db/src/parity_db.rs`** -> AI Confidence: **99.31%**
15. **`client/network/sync/src/state.rs`** -> AI Confidence: **99.31%**
16. **`client/proposer-metrics/src/lib.rs`** -> AI Confidence: **99.31%**
17. **`client/rpc-servers/src/middleware.rs`** -> AI Confidence: **99.31%**
18. **`client/storage-monitor/src/lib.rs`** -> AI Confidence: **99.31%**
19. **`client/tracing/src/logging/directives.rs`** -> AI Confidence: **99.31%**
20. **`client/tracing/src/logging/event_format.rs`** -> AI Confidence: **99.31%**
21. **`frame/alliance/src/tests.rs`** -> AI Confidence: **99.31%**
22. **`frame/asset-rate/src/tests.rs`** -> AI Confidence: **99.31%**
23. **`frame/assets/src/functions.rs`** -> AI Confidence: **99.31%**
24. **`frame/balances/src/lib.rs`** -> AI Confidence: **99.31%**
25. **`frame/contracts/src/wasm/runtime.rs`** -> AI Confidence: **99.31%**
26. **`frame/elections-phragmen/src/lib.rs`** -> AI Confidence: **99.31%**
27. **`frame/fast-unstake/src/tests.rs`** -> AI Confidence: **99.31%**
28. **`frame/nfts/src/impl_nonfungibles.rs`** -> AI Confidence: **99.31%**
29. **`frame/nis/src/tests.rs`** -> AI Confidence: **99.31%**
30. **`frame/proxy/src/lib.rs`** -> AI Confidence: **99.31%**
31. **`frame/safe-mode/src/tests.rs`** -> AI Confidence: **99.31%**
32. **`frame/society/src/tests.rs`** -> AI Confidence: **99.31%**
33. **`frame/support/procedural/src/construct_runtime/parse.rs`** -> AI Confidence: **99.31%**
34. **`frame/support/procedural/src/storage_alias.rs`** -> AI Confidence: **99.31%**
35. **`frame/support/src/storage/transactional.rs`** -> AI Confidence: **99.31%**
36. **`frame/tx-pause/src/tests.rs`** -> AI Confidence: **99.31%**
37. **`frame/uniques/src/lib.rs`** -> AI Confidence: **99.31%**
38. **`primitives/arithmetic/fuzzer/src/per_thing_from_rational.rs`** -> AI Confidence: **99.31%**
39. **`primitives/arithmetic/src/rational.rs`** -> AI Confidence: **99.31%**
40. **`primitives/blockchain/src/header_metadata.rs`** -> AI Confidence: **99.31%**
41. **`primitives/metadata-ir/src/v14.rs`** -> AI Confidence: **99.31%**
42. **`bin/node-template/scripts/init.sh`** -> AI Confidence: **99.29%**
43. **`scripts/ci/github/generate_changelog.sh`** -> AI Confidence: **99.29%**
44. **`scripts/run_all_benchmarks.sh`** -> AI Confidence: **99.29%**
45. **`scripts/ci/gitlab/check-each-crate.py`** -> AI Confidence: **99.29%**
46. **`bin/node/cli/src/command.rs`** -> AI Confidence: **99.24%**
47. **`bin/node/rpc/src/lib.rs`** -> AI Confidence: **99.24%**
48. **`bin/utils/subkey/src/lib.rs`** -> AI Confidence: **99.24%**
49. **`client/authority-discovery/src/worker.rs`** -> AI Confidence: **99.24%**
50. **`client/cli/src/commands/purge_chain_cmd.rs`** -> AI Confidence: **99.24%**
51. **`client/cli/src/commands/utils.rs`** -> AI Confidence: **99.24%**
52. **`client/cli/src/commands/verify.rs`** -> AI Confidence: **99.24%**
53. **`client/cli/src/params/keystore_params.rs`** -> AI Confidence: **99.24%**
54. **`client/consensus/common/src/longest_chain.rs`** -> AI Confidence: **99.24%**
55. **`client/consensus/pow/src/lib.rs`** -> AI Confidence: **99.24%**
56. **`client/db/src/bench.rs`** -> AI Confidence: **99.24%**
57. **`client/network/src/service/out_events.rs`** -> AI Confidence: **99.24%**
58. **`client/network/statement/src/lib.rs`** -> AI Confidence: **99.24%**
59. **`client/network/sync/src/block_request_handler.rs`** -> AI Confidence: **99.24%**
60. **`client/network/sync/src/engine.rs`** -> AI Confidence: **99.24%**
61. **`client/network/sync/src/warp.rs`** -> AI Confidence: **99.24%**
62. **`client/rpc/src/statement/mod.rs`** -> AI Confidence: **99.24%**
63. **`client/service/src/client/client.rs`** -> AI Confidence: **99.24%**
64. **`client/state-db/src/lib.rs`** -> AI Confidence: **99.24%**
65. **`client/transaction-pool/src/tests.rs`** -> AI Confidence: **99.24%**
66. **`frame/asset-conversion/src/lib.rs`** -> AI Confidence: **99.24%**
67. **`frame/assets/src/impl_fungibles.rs`** -> AI Confidence: **99.24%**
68. **`frame/assets/src/lib.rs`** -> AI Confidence: **99.24%**
69. **`frame/babe/src/equivocation.rs`** -> AI Confidence: **99.24%**
70. **`frame/balances/src/impl_currency.rs`** -> AI Confidence: **99.24%**
71. **`frame/balances/src/tests/currency_tests.rs`** -> AI Confidence: **99.24%**
72. **`frame/beefy/src/equivocation.rs`** -> AI Confidence: **99.24%**
73. **`frame/contracts/primitives/src/lib.rs`** -> AI Confidence: **99.24%**
74. **`frame/conviction-voting/src/types.rs`** -> AI Confidence: **99.24%**
75. **`frame/democracy/src/lib.rs`** -> AI Confidence: **99.24%**
76. **`frame/democracy/src/types.rs`** -> AI Confidence: **99.24%**
77. **`frame/fast-unstake/src/migrations.rs`** -> AI Confidence: **99.24%**
78. **`frame/grandpa/src/equivocation.rs`** -> AI Confidence: **99.24%**
79. **`frame/merkle-mountain-range/src/lib.rs`** -> AI Confidence: **99.24%**
80. **`frame/message-queue/src/tests.rs`** -> AI Confidence: **99.24%**
81. **`frame/node-authorization/src/lib.rs`** -> AI Confidence: **99.24%**
82. **`frame/ranked-collective/src/lib.rs`** -> AI Confidence: **99.24%**
83. **`frame/safe-mode/src/lib.rs`** -> AI Confidence: **99.24%**
84. **`frame/scored-pool/src/lib.rs`** -> AI Confidence: **99.24%**
85. **`frame/session/src/tests.rs`** -> AI Confidence: **99.24%**
86. **`frame/staking/reward-curve/src/lib.rs`** -> AI Confidence: **99.24%**
87. **`frame/staking/src/pallet/mod.rs`** -> AI Confidence: **99.24%**
88. **`frame/support/src/storage/child.rs`** -> AI Confidence: **99.24%**
89. **`frame/support/src/storage/types/counted_map.rs`** -> AI Confidence: **99.24%**
90. **`frame/support/src/traits/preimages.rs`** -> AI Confidence: **99.24%**
91. **`frame/support/src/traits/tokens/fungible/hold.rs`** -> AI Confidence: **99.24%**
92. **`frame/support/src/traits/tokens/fungibles/hold.rs`** -> AI Confidence: **99.24%**
93. **`primitives/blockchain/src/backend.rs`** -> AI Confidence: **99.24%**
94. **`primitives/metadata-ir/src/v15.rs`** -> AI Confidence: **99.24%**
95. **`primitives/npos-elections/src/phragmen.rs`** -> AI Confidence: **99.24%**
96. **`primitives/runtime/src/generic/checked_extrinsic.rs`** -> AI Confidence: **99.24%**
97. **`primitives/runtime/src/generic/digest.rs`** -> AI Confidence: **99.24%**
98. **`primitives/trie/src/trie_stream.rs`** -> AI Confidence: **99.24%**
99. **`utils/fork-tree/src/lib.rs`** -> AI Confidence: **99.24%**
100. **`utils/frame/benchmarking-cli/src/machine/mod.rs`** -> AI Confidence: **99.24%**
101. **`utils/frame/benchmarking-cli/src/pallet/command.rs`** -> AI Confidence: **99.24%**
102. **`client/cli/src/params/import_params.rs`** -> AI Confidence: **99.23%**
103. **`frame/balances/src/impl_fungible.rs`** -> AI Confidence: **99.23%**
104. **`frame/paged-list/fuzzer/src/paged_list.rs`** -> AI Confidence: **99.23%**
105. **`frame/support/src/traits/tokens/fungibles/imbalance.rs`** -> AI Confidence: **99.23%**
106. **`frame/transaction-storage/src/tests.rs`** -> AI Confidence: **99.23%**
107. **`frame/uniques/src/impl_nonfungibles.rs`** -> AI Confidence: **99.23%**
108. **`primitives/blockchain/src/error.rs`** -> AI Confidence: **99.23%**
109. **`primitives/database/src/kvdb.rs`** -> AI Confidence: **99.23%**
110. **`primitives/trie/src/trie_codec.rs`** -> AI Confidence: **99.23%**
111. **`bin/node-template/node/src/service.rs`** -> AI Confidence: **99.18%**
112. **`bin/node/cli/tests/export_import_flow.rs`** -> AI Confidence: **99.18%**
113. **`bin/node/runtime/src/impls.rs`** -> AI Confidence: **99.18%**
114. **`bin/node/testing/src/keyring.rs`** -> AI Confidence: **99.18%**
115. **`client/api/src/client.rs`** -> AI Confidence: **99.18%**
116. **`client/basic-authorship/src/basic_authorship.rs`** -> AI Confidence: **99.18%**
117. **`client/chain-spec/derive/src/impls.rs`** -> AI Confidence: **99.18%**
118. **`client/chain-spec/src/chain_spec.rs`** -> AI Confidence: **99.18%**
119. **`client/chain-spec/src/extension.rs`** -> AI Confidence: **99.18%**
120. **`client/chain-spec/src/lib.rs`** -> AI Confidence: **99.18%**
121. **`client/cli/src/commands/build_spec_cmd.rs`** -> AI Confidence: **99.18%**
122. **`client/cli/src/commands/check_block_cmd.rs`** -> AI Confidence: **99.18%**
123. **`client/cli/src/commands/generate.rs`** -> AI Confidence: **99.18%**
124. **`client/cli/src/commands/import_blocks_cmd.rs`** -> AI Confidence: **99.18%**
125. **`client/cli/src/commands/inspect_node_key.rs`** -> AI Confidence: **99.18%**
126. **`client/cli/src/commands/revert_cmd.rs`** -> AI Confidence: **99.18%**
127. **`client/cli/src/params/mod.rs`** -> AI Confidence: **99.18%**
128. **`client/cli/src/runner.rs`** -> AI Confidence: **99.18%**
129. **`client/consensus/babe/src/aux_schema.rs`** -> AI Confidence: **99.18%**
130. **`client/consensus/beefy/src/justification.rs`** -> AI Confidence: **99.18%**
131. **`client/consensus/beefy/src/lib.rs`** -> AI Confidence: **99.18%**
132. **`client/consensus/beefy/src/worker.rs`** -> AI Confidence: **99.18%**
133. **`client/consensus/common/src/block_import.rs`** -> AI Confidence: **99.18%**
134. **`client/consensus/common/src/import_queue.rs`** -> AI Confidence: **99.18%**
135. **`client/consensus/common/src/shared_data.rs`** -> AI Confidence: **99.18%**
136. **`client/consensus/epochs/src/lib.rs`** -> AI Confidence: **99.18%**
137. **`client/consensus/grandpa/src/communication/mod.rs`** -> AI Confidence: **99.18%**
138. **`client/consensus/grandpa/src/finality_proof.rs`** -> AI Confidence: **99.18%**
139. **`client/consensus/grandpa/src/lib.rs`** -> AI Confidence: **99.18%**
140. **`client/consensus/grandpa/src/until_imported.rs`** -> AI Confidence: **99.18%**
141. **`client/consensus/grandpa/src/warp_proof.rs`** -> AI Confidence: **99.18%**
142. **`client/consensus/manual-seal/src/error.rs`** -> AI Confidence: **99.18%**
143. **`client/consensus/manual-seal/src/rpc.rs`** -> AI Confidence: **99.18%**
144. **`client/consensus/pow/src/worker.rs`** -> AI Confidence: **99.18%**
145. **`client/consensus/slots/src/slots.rs`** -> AI Confidence: **99.18%**
146. **`client/db/src/lib.rs`** -> AI Confidence: **99.18%**
147. **`client/executor/benches/bench.rs`** -> AI Confidence: **99.18%**
148. **`client/executor/src/executor.rs`** -> AI Confidence: **99.18%**
149. **`client/executor/src/wasm_runtime.rs`** -> AI Confidence: **99.18%**
150. **`client/executor/wasmtime/src/imports.rs`** -> AI Confidence: **99.18%**
151. **`client/informant/src/display.rs`** -> AI Confidence: **99.18%**
152. **`client/informant/src/lib.rs`** -> AI Confidence: **99.18%**
153. **`client/merkle-mountain-range/rpc/src/lib.rs`** -> AI Confidence: **99.18%**
154. **`client/merkle-mountain-range/src/offchain_mmr.rs`** -> AI Confidence: **99.18%**
155. **`client/network/bitswap/src/lib.rs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `24456` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `client/consensus/common/src/import_queue/mock.rs` (RUST) -> Cumulative Risk: **590.57**
- **Archetype:** `file_cluster_4` (Distance: 13.747 IQR)
- **Magnitude:** 34.78 | **LOC:** 47 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `import_justifications` (Impact: 6.3)

### 2. `test-utils/cli/src/lib.rs` (RUST) -> Cumulative Risk: **586.03**
- **Archetype:** `file_cluster_4` (Distance: 18.237 IQR)
- **Magnitude:** 172.64 | **LOC:** 359 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (93.798%), Tech Debt (89.5777%)
- **Heaviest Functions:** `extract_info_from_output` (Impact: 12.0), `wait_n_finalized_blocks` (Impact: 9.6), `block_hash` (Impact: 7.8)

### 3. `client/transaction-pool/src/graph/watcher.rs` (RUST) -> Cumulative Risk: **580.51**
- **Archetype:** `file_cluster_16` (Distance: 12.089 IQR)
- **Magnitude:** 71.18 | **LOC:** 135 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (98.8622%), State Flux (98.3479%)
- **Heaviest Functions:** `is_done` (Impact: 3.6), `finalized` (Impact: 2.2), `invalid` (Impact: 2.2)

### 4. `client/consensus/beefy/src/tests.rs` (RUST) -> Cumulative Risk: **542.71**
- **Archetype:** `file_cluster_4` (Distance: 12.555 IQR)
- **Magnitude:** 560.5 | **LOC:** 1436 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Cognitive Load (93.6251%), State Flux (89.9582%)
- **Heaviest Functions:** `beefy_reports_equivocations` (Impact: 15.9), `generate_blocks_and_sync` (Impact: 9.9), `finalize_block_and_wait_for_beefy` (Impact: 8.6)

### 5. `scripts/ci/gitlab/publish_draft_release.sh` (SHELL) -> Cumulative Risk: **537.8**
- **Archetype:** `file_cluster_12` (Distance: 12.222 IQR)
- **Magnitude:** 3.65 | **LOC:** 55 | **CtrlFlow:** 69.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.7268%), Tech Debt (99.6406%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 7.3), `__global_context__` (Impact: 3.8), `Anonymous_Block_[Truncated]` (Impact: 3.6)

### 6. `client/consensus/babe/src/tests.rs` (RUST) -> Cumulative Risk: **528.39**
- **Archetype:** `file_cluster_4` (Distance: 12.043 IQR)
- **Magnitude:** 551.78 | **LOC:** 1351 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (94.2625%), Cognitive Load (93.6081%)
- **Heaviest Functions:** `run_one_test` (Impact: 19.4), `claim_vrf_check` (Impact: 18.8), `propose_and_import_block` (Impact: 10.7)

### 7. `bin/node/bench/src/construct.rs` (RUST) -> Cumulative Risk: **525.38**
- **Archetype:** `file_cluster_16` (Distance: 12.061 IQR)
- **Magnitude:** 104.08 | **LOC:** 305 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.7483%), Concurrency (89.8138%), Verification (80.0%)
- **Heaviest Functions:** `path` (Impact: 8.1), `run` (Impact: 7.9), `setup` (Impact: 4.8)

### 8. `utils/frame/rpc/support/src/lib.rs` (RUST) -> Cumulative Risk: **523.49**
- **Archetype:** `file_cluster_4` (Distance: 26.432 IQR)
- **Magnitude:** 35.02 | **LOC:** 185 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Dead Code (97.6238%), Tech Debt (91.5138%)
- **Heaviest Functions:** `get` (Impact: 5.2), `double_map` (Impact: 2.3), `value` (Impact: 2.1)

### 9. `bin/node/bench/src/trie.rs` (RUST) -> Cumulative Risk: **523.37**
- **Archetype:** `file_cluster_13` (Distance: 11.845 IQR)
- **Magnitude:** 187.3 | **LOC:** 371 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9863%), Tech Debt (98.9202%), Safety Score (78.0883%)
- **Heaviest Functions:** `run` (Impact: 13.1), `setup` (Impact: 12.1), `run` (Impact: 12.0)

### 10. `scripts/ci/github/generate_changelog.sh` (SHELL) -> Cumulative Risk: **523.16**
- **Archetype:** `file_cluster_8` (Distance: 12.302 IQR)
- **Magnitude:** 11.09 | **LOC:** 86 | **CtrlFlow:** 89.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9991%), Safety Score (99.2026%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 27.8), `Anonymous_Block` (Impact: 14.2), `Anonymous_Block` (Impact: 5.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `client/network/sync/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.185 IQR)
- **Top Global Matches:** file_cluster_16: 14.185, file_cluster_13: 14.192, file_cluster_17: 14.215
- **Magnitude:** 2500.34 | **LOC:** 4192 | **CtrlFlow:** 36.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.4808%), Tech Debt (27.222%)
**Top Internal Functions/Classes:**
  * `on_block_data` (Impact: 656.0)
  * `on_block_justification` (Impact: 582.6)
  * `on_blocks_processed` (Impact: 305.8)
  * `block_requests` (Impact: 56.3)
  * `validate_blocks` (Impact: 47.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 460`, `args: 114`, `func_start: 52`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 224`, `dead_code: 7`, `fragile_debt: 4`, `orphaned_logic: 15`
* *Architecture:* `api: 25`, `concurrency: 7`, `import: 26`
* *Defense:* `safety: 364`, `doc: 218`, `test: 32`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StreamExt, WarpSyncPhase, crate::
	blocks::BlockCollection, warp::EncodedProof, stream::FuturesUnordered, Header, pin::Pin, sp_runtime::
	traits::
		Block...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/db/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.063 IQR)
- **Top Global Matches:** file_cluster_16: 14.063, file_cluster_0: 14.093, file_cluster_8: 14.108
- **Magnitude:** 1853.64 | **LOC:** 4411 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.638%), Tech Debt (82.9215%)
**Top Internal Functions/Classes:**
  * `try_commit_operation` (Impact: 358.0)
  * `revert` (Impact: 69.6)
  * `revert_finalized_blocks` (Impact: 41.0)
  * `prune_blocks` (Impact: 36.0)
  * `set_head_with_transaction` (Impact: 35.1)
    * *Intent:* /// Handle setting head within a transaction. `route_to` should be the last /// block that existed i...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 303`, `structural_boundaries: 802`, `args: 201`, `func_start: 145`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 373`, `state_mutation: 402`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 16`, `orphaned_logic: 47`
* *Architecture:* `api: 56`, `import: 32`
* *Defense:* `safety: 661`, `doc: 101`, `test: 225`, `sync_locks: 25`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sp_runtime::
	generic::BlockId, utils::OpenDbError, Header, DatabaseType, sp_blockchain::
	Backend, NumberFor, LeafSet, StorageCollection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/rpc-spec-v2/src/chain_head/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.917 IQR)
- **Top Global Matches:** file_cluster_4: 11.917, file_cluster_8: 12.451, file_cluster_16: 12.681
- **Magnitude:** 1772.48 | **LOC:** 2568 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.8496%), Tech Debt (20.3981%)
**Top Internal Functions/Classes:**
  * `check_continue_operation` (Impact: 46.0)
  * `get_storage_multi_query_iter` (Impact: 42.3)
  * `get_storage_hash` (Impact: 36.4)
  * `get_storage_value` (Impact: 36.4)
  * `call_runtime` (Impact: 23.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 751`, `args: 24`, `func_start: 24`
* *Risk/State:* `safety_bypasses: 178`, `state_mutation: 269`, `orphaned_logic: 19`
* *Architecture:* `concurrency: 1099`, `import: 17`
* *Defense:* `safety: 89`, `test: 62`, `immutability_locks: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Backend, sp_consensus::BlockOrigin, GenesisInit, codec::Decode, CODE, testing::TaskExecutor, EmptyServerParams, sp_api::BlockT...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/service/src/client/client.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.616 IQR)
- **Top Global Matches:** file_cluster_16: 13.616, file_cluster_8: 13.844, file_cluster_13: 13.941
- **Magnitude:** 1188.1 | **LOC:** 2136 | **CtrlFlow:** 44.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.516%), Tech Debt (99.4073%)
**Top Internal Functions/Classes:**
  * `execute_and_import_block` (Impact: 268.0)
  * `storage_collection` (Impact: 91.3)
  * `apply_finality_with_block_hash` (Impact: 61.2)
  * `lock_import_and_run` (Impact: 38.8)
  * `new` (Impact: 36.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 327`, `args: 148`, `func_start: 93`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 117`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 37`
* *Architecture:* `api: 46`, `concurrency: 91`, `import: 25`
* *Defense:* `safety: 358`, `doc: 70`, `test: 3`, `sync_locks: 25`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sp_runtime::
	generic::BlockId, StorageProof, StreamExt, client::
		BadBlocks, sc_client_api::
	backend::
		self, BlockBackend, Header, SpawnNamed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/network/src/protocol/notifications/behaviour.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.544 IQR)
- **Top Global Matches:** file_cluster_8: 12.544, file_cluster_0: 12.69, file_cluster_7: 12.887
- **Magnitude:** 1066.6 | **LOC:** 4568 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.8692%), Tech Debt (12.1759%)
**Top Internal Functions/Classes:**
  * `on_connection_handler_event` (Impact: 185.6)
  * `peerset_report_connect` (Impact: 60.3)
  * `poll` (Impact: 43.0)
  * `reschedule_disabled_pending_enable_when_` (Impact: 28.3)
  * `connection_closed_sink_replaced` (Impact: 23.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 576`, `args: 105`, `func_start: 67`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `high_risk_execution: 1`, `state_mutation: 201`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 60`, `concurrency: 74`, `import: 16`
* *Defense:* `safety: 317`, `doc: 180`, `test: 277`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` NotifsHandlerOut, libp2p::
	core::ConnectedPoint, THandler, protocol_controller::self, rand::distributions::Distribution, DialError, PollParameters, Multiaddr...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frame/contracts/src/exec.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.698 IQR)
- **Top Global Matches:** file_cluster_16: 13.698, file_cluster_13: 13.978, file_cluster_8: 13.979
- **Magnitude:** 805.22 | **LOC:** 3885 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0872%), Tech Debt (69.8957%)
**Top Internal Functions/Classes:**
  * `pop_frame` (Impact: 158.1)
  * `run` (Impact: 48.2)
  * `new_frame` (Impact: 42.4)
    * *Intent:* /// Create and run a new call stack by calling into `dest`. /// /// # Note /// /// `debug_message` s...
  * `call` (Impact: 20.2)
  * `push_frame` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 365`, `args: 169`, `func_start: 123`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 162`, `dead_code: 2`, `duplicate_logic: 13`, `orphaned_logic: 17`
* *Architecture:* `api: 21`, `import: 21`
* *Defense:* `safety: 175`, `doc: 306`, `test: 42`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` CodeHash, sp_io::crypto::secp256k1_ecdsa_recover_compressed, weights::Weight, TransactionOutcome, std::
		cell::RefCell, rc::Rc, smallvec::Array, hashing::blake2_256...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `primitives/state-machine/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.52 IQR)
- **Top Global Matches:** file_cluster_0: 13.52, file_cluster_16: 13.532, file_cluster_8: 13.619
- **Magnitude:** 749.46 | **LOC:** 1965 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.7859%), Tech Debt (31.2799%)
**Top Internal Functions/Classes:**
  * `prove_range_read_with_child_with_size_on` (Impact: 72.2)
    * *Intent:* /// Generate range storage read proof, with child tries /// content. /// See `prove_range_read_with_...
  * `read_range_proof_check_with_child_on_pro` (Impact: 59.4)
    * *Intent:* /// Check storage range proof on pre-created proving backend. /// /// See `read_range_proof_check_wi...
  * `update_last_key` (Impact: 36.7)
    * *Intent:* /// Update last keys accessed from this state.
  * `child_read_compact_stress_test` (Impact: 28.8)
  * `prove_range_read_with_size_on_trie_backe` (Impact: 25.9)
    * *Intent:* /// Generate range storage read proof on an existing trie backend.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 133`, `structural_boundaries: 487`, `args: 89`, `func_start: 55`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 210`, `orphaned_logic: 29`
* *Architecture:* `api: 49`, `import: 28`
* *Defense:* `safety: 322`, `doc: 91`, `test: 84`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` crate::
		basic::BasicExternalities, StorageProof, sp_externalities::Extensions, KeySpacedDBMut, CodeExecutor, TrieBackendStorage, OverlayedChanges, trie_backend::create_proof_check_backend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utils/fork-tree/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 14.366 IQR)
- **Top Global Matches:** file_cluster_17: 14.366, file_cluster_0: 14.413, file_cluster_11: 14.657
- **Magnitude:** 704.72 | **LOC:** 1610 | **CtrlFlow:** 39.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.9927%), Tech Debt (72.9408%)
**Top Internal Functions/Classes:**
  * `import` (Impact: 191.1)
    * *Intent:* /// Rebalance the tree. /// /// For each tree level sort child nodes by max branch depth (decreasing...
  * `next` (Impact: 119.3)
  * `finalizes_any_with_descendent_if` (Impact: 67.1)
  * `finalize_with_ancestors` (Impact: 50.1)
  * `drain_filter` (Impact: 18.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 183`, `args: 86`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 115`, `dead_code: 8`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `api: 14`, `import: 5`
* *Defense:* `safety: 136`, `doc: 107`, `test: 84`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std::sync::atomic::AtomicUsize, Encode, node_implementation::Node, codec::Decode, super::Error, Ordering, crate::FilterAction, std::cmp::Reverse...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frame/support/procedural/src/pallet/parse/helper.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.529 IQR)
- **Top Global Matches:** file_cluster_11: 15.529, file_cluster_0: 15.627, file_cluster_16: 15.636
- **Magnitude:** 671.92 | **LOC:** 613 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.0728%), Tech Debt (99.9851%)
**Top Internal Functions/Classes:**
  * `check_type_def_optional_gen` (Impact: 55.6)
    * *Intent:* /// Check the syntax: /// * either `` (no generics /// * or `T` /// * or `T: Config` /// * or `T, I ...
  * `check_type_def_gen` (Impact: 53.3)
    * *Intent:* /// Check the syntax: /// * or `T` /// * or `T: Config` /// * or `T, I = ()` /// * or `T: Config<I>,...
  * `parse` (Impact: 50.3)
  * `parse` (Impact: 48.1)
  * `check_type_value_gen` (Impact: 32.5)
    * *Intent:* /// Check the syntax: /// * either `` (no generics) /// * or `T: Config` /// * or `T: Config<I>, I: ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 140`, `args: 44`, `func_start: 29`, `class_start: 13`
* *Risk/State:* `state_mutation: 85`, `dead_code: 9`, `duplicate_logic: 16`, `orphaned_logic: 11`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 122`, `doc: 70`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quote::ToTokens, syn::spanned::Spanned
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `utils/frame/remote-externalities/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.058 IQR)
- **Top Global Matches:** file_cluster_4: 13.058, file_cluster_16: 13.148, file_cluster_0: 13.165
- **Magnitude:** 661.84 | **LOC:** 1430 | **CtrlFlow:** 31.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.5797%), Tech Debt (69.8889%)
**Top Internal Functions/Classes:**
  * `rpc_get_pairs_paged` (Impact: 29.1)
  * `get_storage_data_dynamic_batch_size` (Impact: 25.8)
    * *Intent:* /// /// Returns a `Result` with a vector of `Option<StorageData>`, where each element corresponds to...
  * `init` (Impact: 23.6)
    * *Intent:* // Build an HttpClient from a URI.
  * `pre_build` (Impact: 21.8)
  * `load_child_remote` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 246`, `args: 97`, `func_start: 53`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 81`, `dead_code: 7`, `duplicate_logic: 11`, `orphaned_logic: 11`
* *Architecture:* `io: 9`, `api: 34`, `concurrency: 168`, `import: 19`
* *Defense:* `safety: 117`, `doc: 122`, `test: 27`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StateApi, DEFAULT_CHILD_STORAGE_KEY_PREFIX, fs, ExtrinsicWrapper, std::
	cmp::max, codec::Compact, PathBuf, hexdisplay::HexDisplay...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frame/contracts/src/wasm/runtime.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.367 IQR)
- **Top Global Matches:** file_cluster_0: 14.367, file_cluster_16: 14.422, file_cluster_13: 14.495
- **Magnitude:** 655.78 | **LOC:** 2857 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.1706%), Tech Debt (99.5593%)
**Top Internal Functions/Classes:**
  * `call` (Impact: 86.1)
  * `instantiate` (Impact: 66.7)
  * `write_sandbox_output` (Impact: 25.4)
    * *Intent:* /// length of the buffer located at `out_ptr`. If that buffer is large enough the actual /// `buf.le...
  * `take_storage` (Impact: 24.0)
    * *Intent:* /// Retrieve and remove the value under the given key from storage. /// /// # Parameters /// /// - `...
  * `sr25519_verify` (Impact: 21.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 163`, `args: 69`, `func_start: 56`, `class_start: 12`
* *Risk/State:* `state_mutation: 62`, `dead_code: 7`, `planned_debt: 5`, `duplicate_logic: 22`
* *Architecture:* `api: 27`, `import: 15`
* *Defense:* `safety: 150`, `doc: 998`, `test: 2`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CodeHash, self::RuntimeCosts::*, weights::Weight, GetDispatchInfo, codec::Decode, SENTINEL, sp_runtime::
	traits::Bounded, wasmi::core::HostError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/babe/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.265 IQR)
- **Top Global Matches:** file_cluster_16: 13.265, file_cluster_0: 13.422, file_cluster_13: 13.477
- **Magnitude:** 643.72 | **LOC:** 1940 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.718%), Tech Debt (77.3758%)
**Top Internal Functions/Classes:**
  * `verify` (Impact: 92.2)
  * `revert` (Impact: 39.4)
  * `check_and_report_equivocation` (Impact: 35.5)
  * `find_pre_digest` (Impact: 18.9)
  * `check_inherents` (Impact: 17.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 224`, `args: 77`, `func_start: 45`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 53`, `dead_code: 5`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 16`
* *Architecture:* `api: 60`, `concurrency: 110`, `import: 28`
* *Defense:* `safety: 144`, `doc: 191`, `test: 1`, `sync_locks: 5`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BabeConfiguration, aux_schema::load_block_weight, InherentDataProviderExt, Header, SlotInfo, pin::Pin, StateAction, sp_blockchain::
	Backend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/network/test/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 13.286 IQR)
- **Top Global Matches:** file_cluster_16: 13.286, file_cluster_4: 13.298, file_cluster_13: 13.48
- **Magnitude:** 629.28 | **LOC:** 1209 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.8645%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `add_full_peer_with_config` (Impact: 37.0)
  * `generate_blocks_at` (Impact: 22.6)
  * `is_in_sync` (Impact: 15.1)
    * *Intent:* /// Polls the testnet until all peers are connected to each other. ///
  * `generate_tx_blocks_at` (Impact: 11.2)
    * *Intent:* /// Push blocks to the peer (simplified: with or without a TX) starting from
  * `is_idle` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 229`, `args: 89`, `func_start: 76`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 89`, `duplicate_logic: 23`, `orphaned_logic: 19`
* *Architecture:* `api: 60`, `concurrency: 209`, `import: 20`
* *Defense:* `safety: 118`, `doc: 81`, `test: 4`, `sync_locks: 9`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sc_network_light::light_client_requests::handler::LightClientRequestHandler, BlockBackend, sc_block_builder::BlockBuilder, Header, BlockchainEvents, pin::Pin, VerificationResult, sp_blockchain::
	Backend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/network/src/protocol/notifications/handler.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.186 IQR)
- **Top Global Matches:** file_cluster_4: 13.186, file_cluster_8: 13.437, file_cluster_16: 13.532
- **Magnitude:** 618.94 | **LOC:** 1614 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.2387%), Tech Debt (37.102%)
**Top Internal Functions/Classes:**
  * `poll` (Impact: 66.0)
    * *Intent:* // If a substream already exists, silently drop the new one. // Note that we drop the substream, whi...
  * `on_behaviour_event` (Impact: 16.7)
    * *Intent:* // Cloning the `mpsc::Sender` guarantees the allocation of an extra spot in the
  * `on_connection_event` (Impact: 16.4)
  * `open_rejected_if_substream_already_open` (Impact: 9.6)
  * `open_rejected_if_substream_is_opening` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 265`, `args: 42`, `func_start: 24`, `class_start: 7`
* *Risk/State:* `state_mutation: 158`, `orphaned_logic: 17`
* *Architecture:* `io: 5`, `api: 10`, `concurrency: 243`
* *Defense:* `safety: 89`, `doc: 184`, `test: 54`, `sync_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` libp2p::
	core::ConnectedPoint, NotificationsOut, KeepAlive, io::Error, IoSliceMut, parking_lot::Mutex, unsigned_varint::codec::UviBytes, ConnectionHandler...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frame/staking/src/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.565 IQR)
- **Top Global Matches:** file_cluster_8: 10.565, file_cluster_16: 11.037, file_cluster_0: 11.068
- **Magnitude:** 606.86 | **LOC:** 6127 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8027%), Tech Debt (51.6921%)
**Top Internal Functions/Classes:**
  * `invulnerables_are_not_slashed` (Impact: 54.2)
    * *Intent:* // // * Should test
  * `test_payout_stakers` (Impact: 21.5)
  * `chill_other_works` (Impact: 12.4)
    * *Intent:* // no slash yet.
  * `rewards_should_work` (Impact: 12.3)
  * `test_max_nominator_rewarded_per_validato` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 222`, `args: 169`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 86`, `state_mutation: 27`, `dead_code: 7`, `orphaned_logic: 73`
* *Architecture:* `import: 16`
* *Defense:* `safety: 66`, `doc: 1`, `test: 579`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` super::ConfigOp, frame_support::
	assert_noop, assert_ok, Get, GetDispatchInfo, Percent, substrate_test_utils::assert_eq_uvec, Support...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/grandpa/src/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.054 IQR)
- **Top Global Matches:** file_cluster_4: 12.054, file_cluster_8: 12.166, file_cluster_13: 12.227
- **Magnitude:** 595.64 | **LOC:** 2166 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.8333%), Tech Debt (40.1817%)
**Top Internal Functions/Classes:**
  * `voter_persists_its_votes` (Impact: 68.4)
  * `transition_3_voters_twice_1_full_observe` (Impact: 21.7)
  * `run_to_completion_with` (Impact: 14.4)
    * *Intent:* // run the voters to completion. provide a closure to be invoked after // the voters are spawned but...
  * `finalize_3_voters_1_full_observer` (Impact: 12.1)
  * `sync_justifications_on_change_blocks` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 409`, `args: 88`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 107`, `dead_code: 4`, `duplicate_logic: 2`, `orphaned_logic: 23`
* *Architecture:* `api: 3`, `concurrency: 162`, `import: 30`
* *Defense:* `safety: 141`, `doc: 4`, `test: 54`, `sync_locks: 70`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` futures_timer::Delay, sp_consensus::BlockOrigin, sp_keyring::Ed25519Keyring, BoxJustificationImport, parking_lot::Mutex, FullPeerConfig, assert_matches::assert_matches, PeersClient...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `bin/node/runtime/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 10.58 IQR)
- **Top Global Matches:** file_cluster_16: 10.58, file_cluster_8: 10.614, file_cluster_13: 10.91
- **Magnitude:** 579.12 | **LOC:** 2789 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2878%), Tech Debt (85.7828%)
**Top Internal Functions/Classes:**
  * `dispatch_benchmark` (Impact: 19.0)
  * `on_unbalanceds` (Impact: 17.6)
  * `create_transaction` (Impact: 9.1)
  * `track_for` (Impact: 8.5)
  * `is_superset` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 1011`, `args: 104`, `func_start: 90`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 17`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 38`
* *Architecture:* `api: 248`, `import: 63`
* *Defense:* `safety: 75`, `doc: 62`, `test: 8`, `immutability_locks: 191`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` EnsureSigned, tokens::nonfungibles_v2::Inspect, super::Runtime, BlockWeights, ConstU16, ConstU32, EnsureRootWithSuccess, EqualPrivilegeOnly...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/slots/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.041 IQR)
- **Top Global Matches:** file_cluster_8: 12.041, file_cluster_4: 12.069, file_cluster_16: 12.089
- **Magnitude:** 564.94 | **LOC:** 1244 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.2642%), Tech Debt (95.8936%)
**Top Internal Functions/Classes:**
  * `on_slot` (Impact: 74.1)
    * *Intent:* /// Called when a new slot is triggered. /// /// Returns a future that resolves to a [`SlotResult`] ...
  * `on_slot` (Impact: 40.1)
    * *Intent:* /// Implements [`SlotWorker::on_slot`].
  * `proposing_remaining_duration` (Impact: 34.3)
    * *Intent:* /// Calculate the remaining duration for block proposal taking into account whether any slots have /...
  * `should_backoff` (Impact: 21.5)
  * `propose` (Impact: 19.2)
    * *Intent:* /// Propose a block by `Proposer`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 217`, `args: 66`, `func_start: 49`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 10`, `orphaned_logic: 12`
* *Architecture:* `api: 25`, `concurrency: 135`, `import: 20`
* *Defense:* `safety: 77`, `doc: 107`, `test: 34`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` TryFutureExt, futures_timer::Delay, futures::future::Either, sp_runtime::traits::Zero, CONSENSUS_INFO, CONSENSUS_WARN, slots::Slots, sp_arithmetic::traits::BaseArithmetic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/statement-store/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.568 IQR)
- **Top Global Matches:** file_cluster_8: 13.568, file_cluster_16: 13.659, file_cluster_0: 13.697
- **Magnitude:** 563.76 | **LOC:** 1297 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.7415%), Tech Debt (59.9687%)
**Top Internal Functions/Classes:**
  * `insert` (Impact: 56.3)
  * `make_expired` (Impact: 28.2)
  * `iterate_with` (Impact: 26.5)
  * `submit` (Impact: 26.3)
  * `new` (Impact: 24.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 248`, `args: 82`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 111`, `dead_code: 1`, `duplicate_logic: 8`, `orphaned_logic: 10`
* *Architecture:* `api: 6`, `concurrency: 36`, `import: 6`
* *Defense:* `safety: 238`, `doc: 52`, `test: 49`, `sync_locks: 2`, `immutability_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AccountId, DecryptionKey, traits::SpawnNamed, ValidateStatement, hexdisplay::HexDisplay, SignatureVerificationResult, sp_core::Pair, SubmitResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/beefy/src/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.555 IQR)
- **Top Global Matches:** file_cluster_4: 12.555, file_cluster_17: 12.96, file_cluster_0: 12.971
- **Magnitude:** 560.5 | **LOC:** 1436 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.6251%), Tech Debt (84.1131%)
**Top Internal Functions/Classes:**
  * `beefy_reports_equivocations` (Impact: 15.9)
  * `generate_blocks_and_sync` (Impact: 9.9)
    * *Intent:* /// Builds the blocks and returns the vector of built block hashes. /// Returned vector contains the...
  * `finalize_block_and_wait_for_beefy` (Impact: 8.6)
  * `initialize_beefy` (Impact: 7.2)
    * *Intent:* // Spawns beefy voters. Returns a future to spawn on the runtime.
  * `streams_empty_after_future` (Impact: 6.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 385`, `args: 67`, `func_start: 45`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 1`, `state_mutation: 95`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `api: 23`, `concurrency: 262`, `import: 20`
* *Defense:* `safety: 130`, `doc: 4`, `test: 60`, `sync_locks: 48`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StreamExt, sc_utils::notification::NotificationReceiver, VoteMessage, stream::FuturesUnordered, tokio::time::Duration, beefy_block_import_and_links, BlockchainEvents, sp_keystore::testing::MemoryKeystore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/grandpa/src/environment.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.691 IQR)
- **Top Global Matches:** file_cluster_16: 12.691, file_cluster_8: 12.902, file_cluster_13: 13.02
- **Magnitude:** 557.76 | **LOC:** 1545 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.3566%), Tech Debt (36.0552%)
**Top Internal Functions/Classes:**
  * `concluded` (Impact: 123.5)
  * `finalize_block` (Impact: 82.5)
  * `report_equivocation` (Impact: 28.6)
  * `precommitted` (Impact: 21.4)
  * `prevoted` (Impact: 18.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 177`, `args: 65`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 26`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 61`, `concurrency: 21`, `import: 18`
* *Defense:* `safety: 191`, `doc: 77`, `sync_locks: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Backend, futures_timer::Delay, Syncing, ClientForGrandpa, CONSENSUS_INFO, PrimaryPropose, crate::
	authorities::AuthoritySet, voter...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `client/consensus/beefy/src/worker.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.286 IQR)
- **Top Global Matches:** file_cluster_13: 13.286, file_cluster_16: 13.317, file_cluster_0: 13.35
- **Magnitude:** 552.36 | **LOC:** 1649 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0203%), Tech Debt (11.9842%)
**Top Internal Functions/Classes:**
  * `process_new_state` (Impact: 94.1)
  * `do_vote` (Impact: 35.6)
  * `report_equivocation` (Impact: 30.7)
  * `triage_incoming_justif` (Impact: 21.6)
  * `finalize` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 290`, `args: 64`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 81`, `dead_code: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 51`, `concurrency: 17`, `import: 25`
* *Defense:* `safety: 174`, `doc: 79`, `test: 85`, `sync_locks: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` StreamExt, peers::PeerReport, VoteMessage, Header, crate::
	communication::
		gossip::proofs_topic, known_payloads::MMR_ROOT_ID, fmt::Debug, NumberFor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/consensus/babe/src/tests.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.043 IQR)
- **Top Global Matches:** file_cluster_4: 12.043, file_cluster_17: 12.406, file_cluster_0: 12.447
- **Magnitude:** 551.78 | **LOC:** 1351 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.6081%), Tech Debt (43.1637%)
**Top Internal Functions/Classes:**
  * `run_one_test` (Impact: 19.4)
  * `claim_vrf_check` (Impact: 18.8)
  * `propose_and_import_block` (Impact: 10.7)
    * *Intent:* // Propose and import a new BABE block on top of the given parent.
  * `revert_prunes_epoch_changes_and_removes_` (Impact: 9.5)
  * `verify_slots_are_strictly_increasing` (Impact: 6.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 323`, `args: 77`, `func_start: 31`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 113`, `dead_code: 5`, `orphaned_logic: 19`
* *Architecture:* `api: 4`, `concurrency: 268`, `import: 23`
* *Defense:* `safety: 73`, `doc: 4`, `test: 52`, `sync_locks: 11`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sc_network_test::Block, NoNetwork, AuthorityId, BoxJustificationImport, authorship::claim_slot, EpochIdentifierPosition, BlockBuilderProvider, sc_block_builder::BlockBuilder...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `client/network/test/src/sync.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.137 IQR)
- **Top Global Matches:** file_cluster_4: 11.137, file_cluster_0: 11.575, file_cluster_8: 11.641
- **Magnitude:** 532.38 | **LOC:** 1326 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.3072%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `wait_until_deferred_block_announce_valid` (Impact: 44.6)
  * `sync_cycle_from_offline_to_syncing_to_of` (Impact: 21.9)
  * `block_announce_data_is_propagated` (Impact: 20.5)
  * `syncs_state` (Impact: 17.6)
    * *Intent:* #[tokio::test(flavor = "multi_thread", worker_threads = 2)]
  * `can_sync_small_non_best_forks` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 169`, `args: 47`, `func_start: 24`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 50`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 21`, `concurrency: 222`, `import: 9`
* *Defense:* `safety: 51`, `doc: 13`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` sp_runtime::Justifications, futures::Future, sp_core::storage::well_known_keys::HEAP_PAGES, sp_runtime::codec::Encode, substrate_test_runtime_client::BlockBuilderExt, BlockOrigin, super::*, substrate_test_runtime::Header...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `frame/asset-conversion/src/lib.rs` (RUST | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.144 IQR)
- **Top Global Matches:** file_cluster_16: 12.144, file_cluster_8: 12.378, file_cluster_0: 12.455
- **Magnitude:** 526.36 | **LOC:** 1311 | **CtrlFlow:** 46.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.2736%), Tech Debt (18.28%)
**Top Internal Functions/Classes:**
  * `add_liquidity` (Impact: 87.6)
  * `remove_liquidity` (Impact: 51.6)
  * `do_swap` (Impact: 39.9)
  * `get_amount_in` (Impact: 28.7)
  * `do_swap_exact_tokens_for_tokens` (Impact: 21.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 166`, `args: 47`, `func_start: 32`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 15`, `dead_code: 2`, `duplicate_logic: 2`, `orphaned_logic: 3`
* *Architecture:* `api: 32`, `import: 14`
* *Defense:* `safety: 75`, `doc: 228`, `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.547
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Preserve, types::*, tokens::
				Fortitude::Polite, Preservation::Expendable, MaybeDisplay, sp_arithmetic::traits::Unsigned, PalletId, Ensure...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `primitives/runtime/src/lib.rs` (RUST) | Magnitude: 288.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 479, doc: 185, structural_boundaries: 161, generics: 92
- `utils/frame/benchmarking-cli/src/machine/mod.rs` (RUST) | Magnitude: 101.56 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 122, structural_boundaries: 36, doc: 35, branch: 30
- `frame/indices/src/tests.rs` (RUST) | Magnitude: 34.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 63, safety: 34, test: 23, args: 16
- `frame/support/procedural/src/pallet/expand/doc_only.rs` (RUST) | Magnitude: 19.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 50, doc: 28, structural_boundaries: 19, api: 5
- `client/cli/src/arg_enums.rs` (RUST) | Magnitude: 46.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 119, doc: 57, decorators: 29, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `primitives/runtime-interface/src/pass_by.rs` (RUST) | Magnitude: 87.22 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 206, indent_tabs: 92, structural_boundaries: 68, generics: 59
- `frame/support/src/dispatch_context.rs` (RUST) | Magnitude: 78.96 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 95, indent_tabs: 85, state_mutation: 37, structural_boundaries: 36
- `frame/support/procedural/src/pallet/parse/helper.rs` (RUST) | Magnitude: 671.92 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 393, branch: 140, structural_boundaries: 140, safety: 122

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/ci/gitlab/publish_draft_release.sh` (SHELL) | Magnitude: 3.65 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 21, io: 19, safety_bypasses: 11, indent_spaces: 11
- `scripts/ci/common/lib.sh` (SHELL) | Magnitude: 12.0 | Delta: **0.306 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 58, indent_spaces: 55, branch: 37, io: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `client/consensus/manual-seal/src/consensus/timestamp.rs` (RUST) | Magnitude: 67.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 87, structural_boundaries: 30, generics: 26, safety: 18
- `primitives/authority-discovery/src/lib.rs` (RUST) | Magnitude: 26.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 7, indent_tabs: 6, api: 4
- `client/network/src/error.rs` (RUST) | Magnitude: 5.48 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 20, doc: 15, structural_boundaries: 7, decorators: 5
- `client/consensus/grandpa/src/finality_proof.rs` (RUST) | Magnitude: 175.84 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 390, structural_boundaries: 112, doc: 58, generics: 50
- `client/network/sync/src/engine.rs` (RUST) | Magnitude: 243.46 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 557, structural_boundaries: 98, safety: 86, doc: 86

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `bin/node/rpc/src/lib.rs` (RUST) | Magnitude: 19.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 72, doc: 32, structural_boundaries: 18, branch: 13
- `frame/identity/src/lib.rs` (RUST) | Magnitude: 38.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 301, indent_tabs: 99, generics: 28, structural_boundaries: 23
- `frame/im-online/src/benchmarking.rs` (RUST) | Magnitude: 21.94 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 43, structural_boundaries: 17, branch: 10, generics: 9
- `client/network/transactions/src/lib.rs` (RUST) | Magnitude: 200.0 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 325, structural_boundaries: 80, doc: 53, safety: 45
- `primitives/state-machine/src/error.rs` (RUST) | Magnitude: 21.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 9, indent_tabs: 8, decorators: 7, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `frame/contracts/proc-macro/src/lib.rs` (RUST) | Magnitude: 313.08 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 508, structural_boundaries: 162, doc: 153, branch: 89
- `client/rpc/src/state/state_full.rs` (RUST) | Magnitude: 251.18 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 519, safety: 156, generics: 118, structural_boundaries: 109
- `primitives/core/hashing/proc-macro/src/impls.rs` (RUST) | Magnitude: 77.0 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 61, structural_boundaries: 21, safety: 16, branch: 13
- `frame/support/procedural/src/pallet/parse/type_value.rs` (RUST) | Magnitude: 63.3 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 79, structural_boundaries: 32, safety: 17, branch: 15
- `scripts/ci/docker/subkey.Dockerfile` (DOCKERFILE) | Magnitude: 50.36 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 7, args: 3, func_start: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `frame/system/src/extensions/check_non_zero_sender.rs` (RUST) | Magnitude: 52.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 60, concurrency: 26, structural_boundaries: 24, generics: 16
- `client/cli/src/signals.rs` (RUST) | Magnitude: 45.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 44, structural_boundaries: 17, concurrency: 14, doc: 12
- `client/rpc-spec-v2/src/transaction/transaction.rs` (RUST) | Magnitude: 78.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 112, concurrency: 39, structural_boundaries: 35, safety: 29
- `client/consensus/common/src/import_queue.rs` (RUST) | Magnitude: 221.96 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 180, concurrency: 90, structural_boundaries: 64, doc: 63
- `client/rpc/src/system/tests.rs` (RUST) | Magnitude: 166.72 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 295, structural_boundaries: 91, concurrency: 49, test: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `frame/benchmarking/src/v1.rs` (RUST) | Magnitude: 38.6 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 396, indent_tabs: 100, dead_code: 48, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `primitives/genesis-builder/src/lib.rs` (RUST) | Magnitude: 23.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 25, indent_tabs: 4, safety: 3, structural_boundaries: 2
- `primitives/core/hashing/proc-macro/src/lib.rs` (RUST) | Magnitude: 26.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 67, macros: 9, args: 8, func_start: 8
- `frame/elections-phragmen/src/migrations/mod.rs` (RUST) | Magnitude: 16.08 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, api: 4, encapsulation: 4
- `frame/democracy/src/migrations/mod.rs` (RUST) | Magnitude: 13.04 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 3, structural_boundaries: 2, api: 2, encapsulation: 2
- `primitives/api/proc-macro/src/common.rs` (RUST) | Magnitude: 19.64 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 13, api: 6, immutability_locks: 6, encapsulation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `primitives/runtime-interface/proc-macro/src/runtime_interface/bare_function_interface.rs` (RUST) | Magnitude: 114.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 158, structural_boundaries: 47, branch: 27, doc: 23
- `bin/node/testing/src/bench.rs` (RUST) | Magnitude: 166.32 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 395, structural_boundaries: 101, doc: 68, safety: 44
- `primitives/runtime/src/generic/era.rs` (RUST) | Magnitude: 6.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 27, indent_tabs: 8, structural_boundaries: 5, api: 4
- `frame/support/procedural/src/construct_runtime/expand/call.rs` (RUST) | Magnitude: 111.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 170, structural_boundaries: 48, branch: 16, args: 14
- `client/consensus/grandpa/src/aux_schema.rs` (RUST) | Magnitude: 219.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 549, structural_boundaries: 126, generics: 90, safety: 84

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `frame/staking/reward-curve/src/log.rs` -> **Severity: 202.388** (Blast Radius: 6.139 * Doc Risk: 32.9676%)
- `primitives/rpc/src/tracing.rs` -> **Severity: 192.924** (Blast Radius: 1.941 * Doc Risk: 99.394%)
- `primitives/database/src/mem.rs` -> **Severity: 165.728** (Blast Radius: 5.194 * Doc Risk: 31.9075%)
- `frame/contracts/src/migration/v11.rs` -> **Severity: 96.664** (Blast Radius: 1.554 * Doc Risk: 62.2036%)
- `test-utils/runtime/src/substrate_test_pallet.rs` -> **Severity: 85.106** (Blast Radius: 1.012 * Doc Risk: 84.0972%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
