# ARCHITECTURAL_BRIEF: tigerbeetle
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/tigerbeetle/tigerbeetle` |
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
- **Scope:** 440 analyzed artifact(s), 148381 LOC.
- **Load-bearing artifact:** `src/stdx/stdx.zig` -- 140 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/unit_tests.zig` -- pulls in 74 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/vsr/replica.zig` at magnitude 6500.6 (structural weight, not risk).
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
| Total Artifacts | 564 |
| Analyzed Artifacts (Scanned) | 440 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 124 |
| Total LOC | 148381 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 78.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5073 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2038 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0273 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 234 | 116273 | 53.2% |
| JAVA | 57 | 9131 | 13.0% |
| MARKDOWN | 36 | 0 | 8.2% |
| CSHARP | 18 | 4204 | 4.1% |
| RUST | 13 | 4323 | 3.0% |
| PYTHON | 12 | 3407 | 2.7% |
| GO | 12 | 3637 | 2.7% |
| PLAINTEXT | 9 | 0 | 2.0% |
| JAVASCRIPT | 8 | 1920 | 1.8% |
| XML | 7 | 0 | 1.6% |
| JSON | 6 | 222 | 1.4% |
| LUA | 5 | 78 | 1.1% |
| HTML | 5 | 390 | 1.1% |
| TYPESCRIPT | 4 | 1812 | 0.9% |
| SHELL | 3 | 200 | 0.7% |
| YAML | 3 | 280 | 0.7% |
| CPP | 3 | 951 | 0.7% |
| CSS | 3 | 1217 | 0.7% |
| C | 1 | 291 | 0.2% |
| POWERSHELL | 1 | 45 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 440 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Large Core Modules (2) 24%, Data / Markup / Trivial 17%, Declarative / Non-Code 9%, Parameter Forwarders Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 395 | 89.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 45 | 10.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 124*

**Composition by Extension & Reason:**
- `.md`: 70x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.csproj`: 6x Unsupported Format (.csproj)
- `.toml`: 6x Unsupported Format (.toml)
- `.mod`: 5x Unsupported Format (.mod)
- `.zig`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1705 LOC)
- `.webp`: 3x Excluded (Explicitly Denied Extension: '.webp')
- `.html`: 2x Excluded (Saturation: Line 92 exceeds 500 chars)
- `.sln`: 1x Unsupported Format (.sln)
- `.cs`: 1x Excluded (Machine-Generated Source Code Signature: 1369 LOC)
- `.props`: 1x Unsupported Format (.props)
- `.sum`: 1x Unsupported Format (.sum)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.test`: 1x Unsupported Format (.test)
- `.typed`: 1x Unsupported Format (.typed)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.8 | 8.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.5 | 40.5 | 48.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 17.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 29.8 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.8 | 21.7 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 10.7 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 12.1 | 2.9 | 0.5 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 15.8 | 7.8 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 69.0 | 85.2 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2569 | 230 | 17 | `src/testing/cluster.zig` |
| cleanup | 1512 | 188 | 12 | `src/testing/cluster.zig` |
| guards | 12224 | 328 | 70 | `src/vsr/replica_test.zig` |
| danger | 4077 | 291 | 24 | `src/io/windows.zig` |
| concurrency | 966 | 84 | 4 | `src/clients/node/src/test.ts` |
| connectivity | 5441 | 328 | 30 | `src/vsr/message_header.zig` |
| io | 741 | 102 | 4 | `.github/ci/test_aof.sh` |
| crypto | 1 | 1 | 0 | `src/clients/node/src/index.ts` |
| ipc | 153 | 43 | 0 | `src/stdx/unshare.zig` |
| time | 101 | 43 | 0 | `src/devhub/devhub.js` |
| serialization | 9 | 7 | 0 | `src/cdc/runner.zig` |
| regex | 66 | 25 | 0 | `src/docs_website/assets/js/search.js` |
| events | 159 | 86 | 1 | `src/docs_website/src/html/404.html` |
| tests | 3645 | 141 | 12 | `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` |
| docs | 9531 | 237 | 50 | `src/vsr/replica.zig` |
| debt | 645 | 135 | 4 | `src/cdc/amqp/spec_parser.py` |
| mutation | 30280 | 367 | 173 | `src/vsr/replica.zig` |
| dead_code | 669 | 110 | 2 | `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` |
| credential | 93 | 3 | 0 | `src/stdx/testing/low_level_hash_vectors.zig` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 731 | 134 | 5 | `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` |
| ui | 105 | 6 | 0 | `src/docs_website/assets/style/style.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5228**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/ci/test_aof.sh` (Hits: 61)
- `src/multiversion.zig` (Hits: 60)
- `src/tigerbeetle/inspect.zig` (Hits: 32)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **stdx.zig** (`src/stdx/stdx.zig`) — 140 inbound connections
2. **vsr.zig** (`src/vsr.zig`) — 90 inbound connections
3. **constants.zig** (`src/constants.zig`) — 78 inbound connections
4. **fuzz.zig** (`src/testing/fuzz.zig`) — 27 inbound connections
5. **client_readmes.zig** (`src/scripts/client_readmes.zig`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **unit_tests.zig** (`src/unit_tests.zig`) — 74 outbound dependencies
2. **vsr.zig** (`src/vsr.zig`) — 49 outbound dependencies
3. **IntegrationTest.java** (`src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java`) — 25 outbound dependencies
4. **Main.java** (`src/testing/vortex/java_driver/src/main/java/Main.java`) — 24 outbound dependencies
5. **fuzz_tests.zig** (`src/fuzz_tests.zig`) — 22 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ReplicaType` **(Many-Argument Workhorses)** (@ `src/vsr/replica.zig`) -> Impact: **2828.0** | LOC: 11301
- `StateMachineType` **(Many-Argument Workhorses)** (@ `src/state_machine.zig`) -> Impact: **772.9** | LOC: 4511
- `JournalType` **(Many-Argument Workhorses)** (@ `src/vsr/journal.zig`) -> Impact: **385.7** | LOC: 2067
- `GrooveType` **(Many-Argument Workhorses)** (@ `src/lsm/groove.zig`) -> Impact: **379.4** | LOC: 1349
  * *Intent:* /// A Groove is a collection of LSM trees auto generated for fields on a struct type /// as well as custom derived fields from said struct type.
- `CompactionType` **(Many-Argument Workhorses)** (@ `src/lsm/compaction.zig`) -> Impact: **356.2** | LOC: 1720
- `WorkloadType` **(Many-Argument Workhorses)** (@ `src/state_machine/workload.zig`) -> Impact: **289.3** | LOC: 1827
- `doTestClient` **(Many-Argument Workhorses)** (@ `src/clients/go/tb_client_test.go`) -> Impact: **261.3** | LOC: 1442
- `GridType` **(Many-Argument Workhorses)** (@ `src/vsr/grid.zig`) -> Impact: **256.1** | LOC: 1558
  * *Intent:* /// The Grid provides access to on-disk blocks (blobs of `block_size` bytes). /// Each block is identified by an "address" (`u64`, beginning at 1). //...
- `SegmentedArrayBaseType` **(Many-Argument Workhorses)** (@ `src/lsm/segmented_array.zig`) -> Impact: **252.0** | LOC: 912
- `MessageBusType` **(Many-Argument Workhorses)** (@ `src/message_bus.zig`) -> Impact: **215.6** | LOC: 1201

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/vsr` | 29 | 14113.64 | 11.15% | 5.91% |
| `src/lsm` | 39 | 10835.36 | 10.05% | 9.83% |
| `src` | 38 | 9790.44 | 12.88% | 6.42% |
| `src/clients/java/src/test/java/com/tigerbeetle` | 16 | 2556.56 | 29.44% | 0.0% |
| `src/testing` | 15 | 2045.82 | 5.41% | 0.0% |
| `src/io` | 5 | 2005.9 | 10.48% | 5.59% |
| `src/stdx` | 16 | 1997.74 | 12.22% | 2.54% |
| `src/clients/go` | 10 | 1821.16 | 21.38% | 21.75% |
| `src/clients/java/src/main/java/com/tigerbeetle` | 35 | 1753.64 | 12.66% | 43.97% |
| `src/tigerbeetle` | 7 | 1737.38 | 11.77% | 4.57% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/clients/java/src/main/java/com/tigerbeetle/AccountFilter.java` -> **100.0%** Exposure
- `src/clients/java/src/main/java/com/tigerbeetle/QueryFilter.java` -> **100.0%** Exposure
- `src/clients/java/src/main/java/com/tigerbeetle/QueryFilterBatch.java` -> **100.0%** Exposure
- `src/clients/java/src/main/java/com/tigerbeetle/AsyncRequest.java` -> **99.9994%** Exposure
- `src/clients/java/src/main/java/com/tigerbeetle/AccountFilterBatch.java` -> **99.9992%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `zig/download.sh` -> **100.0%** Exposure
- `src/cdc/amqp/spec_parser.py` -> **100.0%** Exposure
- `src/clients/python/src/tigerbeetle/lib.py` -> **100.0%** Exposure
- `src/clients/java/samples/two-phase-many/src/main/java/Main.java` -> **100.0%** Exposure
- `src/clients/java/samples/two-phase/src/main/java/Main.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` -> **50** Orphaned Functions | **0** Duplicates
- `src/clients/dotnet/TigerBeetle.Tests/IntegrationTests.cs` -> **44** Orphaned Functions | **0** Duplicates
- `src/clients/java/src/test/java/com/tigerbeetle/TransferTest.java` -> **42** Orphaned Functions | **0** Duplicates
- `src/clients/java/src/test/java/com/tigerbeetle/AccountTest.java` -> **32** Orphaned Functions | **0** Duplicates
- `src/clients/java/src/test/java/com/tigerbeetle/BatchTest.java` -> **32** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1371` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/vsr/replica.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.744)
- **Top Global Matches:** file_cluster_4: 9.744, file_cluster_12: 12.294, file_cluster_15: 12.614
- **Magnitude:** 6500.6 | **LOC:** 12356 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 34.6%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **15**; blast radius 1.658; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (61.5%), Guard Balance (formerly Safety Score) (51.2%)
- **Documentation Coverage:** 66.9903% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ReplicaType` **(Many-Argument Workhorses)** (Impact: 2828.0)
  * `open` **(Many-Argument Workhorses)** (Impact: 109.2)
    * *Intent:* /// Initializes and opens the provided replica using the options.
  * `init` **(Many-Argument Workhorses)** (Impact: 60.8)
    * *Intent:* /// NOTE: self.superblock must be initialized and opened prior to this call.
  * `on_prepare` **(Many-Argument Workhorses)** (Impact: 51.2)
    * *Intent:* /// /// This does not impact latency, since with Flexible Paxos we need only one remote /// prepare_...
  * `execute_op` **(Many-Argument Workhorses)** (Impact: 50.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 148 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 644
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1110`, `structural_boundaries: 682`, `args: 270`, `func_start: 269`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 92`, `high_risk_execution: 10`, `state_mutation: 348`, `planned_debt: 16`, `fragile_debt: 9`
* *Architecture:* `api: 24`, `import: 21`
* *Defense:* `safety: 279`, `doc: 845`, `test: 1`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.658
  * `Choke Point (Betweenness):` 0.003069 | `Ripple Effect (Closeness):` 0.140722
  * `Imports (Out-Degree: 14):` constants.zig, forest_table_iterator.zig, message_buffer.zig, message_pool.zig, multiversion.zig, static_allocator.zig, marks.zig, storage.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/state_machine.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.115)
- **Top Global Matches:** file_cluster_4: 8.115, file_cluster_12: 10.434, file_cluster_15: 11.942
- **Magnitude:** 2338.96 | **LOC:** 5030 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 46.2%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 1.915; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.4%), Connectivity (formerly Api Exposure) (62.1%), Guard Balance (formerly Safety Score) (53.1%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `StateMachineType` **(Many-Argument Workhorses)** (Impact: 772.9)
  * `create_transfer` **(Many-Argument Workhorses)** (Impact: 116.4)
  * `post_or_void_pending_transfer` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `execute_create` **(Many-Argument Workhorses)** (Impact: 89.0)
  * `post_or_void_pending_transfer_exists` **(Many-Argument Workhorses)** (Impact: 58.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 47 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 339`, `args: 132`, `func_start: 127`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 118`, `dead_code: 1`, `planned_debt: 15`
* *Architecture:* `api: 41`, `import: 18`
* *Defense:* `safety: 84`, `doc: 73`, `test: 8`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.915
  * `Choke Point (Betweenness):` 0.007272 | `Ripple Effect (Closeness):` 0.143235
  * `Imports (Out-Degree: 16):` constants.zig, direction.zig, forest.zig, groove.zig, scan_buffer.zig, scan_lookup.zig, scan_range.zig, scan_tree.zig...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/vsr/journal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.347)
- **Top Global Matches:** file_cluster_4: 8.347, file_cluster_12: 8.375, file_cluster_15: 10.53
- **Magnitude:** 1189.1 | **LOC:** 2587 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.499; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (56.9%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 52.0408% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JournalType` **(Many-Argument Workhorses)** (Impact: 385.7)
  * `find_latest_headers_break_between` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /// A break is a missing header or a header not connected to the next header by hash chain. /// On f...
  * `recovery_case` **(Many-Argument Workhorses)** (Impact: 48.4)
  * `torn_prepares` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /// The goal of this function is to identify all prepares that were torn while being /// appended to...
  * `read_prepare_with_op_and_checksum_callback` **(Compute Cores)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 38 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 165
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 144`, `args: 70`, `func_start: 66`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 89`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 38`, `import: 5`
* *Defense:* `safety: 50`, `doc: 368`, `test: 2`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.499
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.139672
  * `Imports (Out-Degree: 5):` constants.zig, message_pool.zig, vsr.zig, std, stdx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.621)
- **Top Global Matches:** file_cluster_12: 7.621, file_cluster_5: 8.663, file_cluster_7: 9.42
- **Magnitude:** 1176.42 | **LOC:** 2680 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.704; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (89.8%), Concurrency Surface (formerly Concurrency) (76.2%), Guard Balance (formerly Safety Score) (54.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.2%)
- **Documentation Coverage:** 86.5546% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAccountTransfers` **(I/O & Config Routines)** (Impact: 32.4)
  * `testQueryTransfers` **(I/O & Config Routines)** (Impact: 17.5)
  * `testQueryAccounts` **(I/O & Config Routines)** (Impact: 16.6)
  * `createSuccess` **(Defensive Guards)** (Impact: 9.5)
  * `testCloseWithConcurrentTasks` **(I/O & Config Routines)** (Impact: 9.4)
    * *Intent:* /** * This test asserts that client.close() will wait for all ongoing request to complete And new * ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 106 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 83
* *State Mutation (weighted view):* 711
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 649`, `args: 69`, `func_start: 65`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 73`, `high_risk_execution: 2`, `state_mutation: 499`, `unreferenced_by_name: 50`
* *Architecture:* `io: 2`, `api: 60`, `concurrency: 28`, `import: 25`
* *Defense:* `safety: 69`, `doc: 9`, `test: 615`, `sync_locks: 1`, `immutability_locks: 314`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` java.io.BufferedReader, java.io.File, java.io.IOException, java.io.InputStreamReader, java.lang.ProcessBuilder.Redirect, java.math.BigInteger, java.util.UUID, java.util.concurrent.CompletableFuture...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lsm/compaction.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.623)
- **Top Global Matches:** file_cluster_4: 7.623, file_cluster_6: 10.367, file_cluster_12: 12.281
- **Magnitude:** 1060.72 | **LOC:** 2083 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 57.1%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 1.329; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%)
- **Documentation Coverage:** 82.4324% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CompactionType` **(Many-Argument Workhorses)** (Impact: 356.2)
  * `compaction_dispatch` **(Many-Argument Workhorses)** (Impact: 66.5)
    * *Intent:* // // The job of compaction_dispatch is to kick off all the jobs. There are several additional // co...
  * `half_bar_commence` **(Many-Argument Workhorses)** (Impact: 36.5)
    * *Intent:* /// Plan the work for the bar: /// - check if compaction is needed at all (if the level_a is full), ...
  * `half_bar_complete` **(I/O & Config Routines)** (Impact: 34.6)
    * *Intent:* /// Apply the changes that have been accumulated in memory to the manifest and remove any /// tables...
  * `merge_advance_position` **(I/O & Config Routines)** (Impact: 29.2)
    * *Intent:* // merge_callback advances just position.values. Here, we implement the carry-flag logic, // advanci...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 49 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 75`, `args: 51`, `func_start: 49`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 121`, `planned_debt: 4`
* *Architecture:* `api: 25`, `import: 13`
* *Defense:* `safety: 44`, `doc: 161`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.329
  * `Choke Point (Betweenness):` 0.000306 | `Ripple Effect (Closeness):` 0.107977
  * `Imports (Out-Degree: 8):` constants.zig, stack.zig, trace.zig, vsr.zig, grid.zig, manifest.zig, schema.zig, std...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/state_machine/workload.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.741)
- **Top Global Matches:** file_cluster_4: 7.741, file_cluster_15: 7.784, file_cluster_12: 8.213
- **Magnitude:** 1019.2 | **LOC:** 2192 | **CtrlFlow:** 7.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.806; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%), Connectivity (formerly Api Exposure) (38.0%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WorkloadType` **(Many-Argument Workhorses)** (Impact: 289.3)
  * `on_query` **(Many-Argument Workhorses)** (Impact: 39.0)
  * `on_get_account_transfers` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `build_transfer` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* /// The transfer built is guaranteed to match the TransferPlan's outcome. /// The transfer built is ...
  * `on_create_transfers_sparse` **(Many-Argument Workhorses)** (Impact: 27.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 40 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 192
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 100`, `args: 39`, `func_start: 39`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 112`
* *Architecture:* `api: 10`, `import: 9`
* *Defense:* `safety: 37`, `doc: 66`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.806
  * `Choke Point (Betweenness):` 0.000817 | `Ripple Effect (Closeness):` 0.102647
  * `Imports (Out-Degree: 9):` constants.zig, timestamp_range.zig, fuzz.zig, id.zig, tigerbeetle.zig, vsr.zig, auditor.zig, std...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/clients/dotnet/TigerBeetle.Tests/IntegrationTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 7.731)
- **Top Global Matches:** file_cluster_10: 7.731, file_cluster_13: 7.878, file_cluster_12: 7.88
- **Magnitude:** 922.14 | **LOC:** 2379 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.704; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.8%), Mutation Surface (formerly State Flux) (99.4%), Complexity Load (formerly Cognitive Load) (73.1%), Guard Balance (formerly Safety Score) (45.9%)
- **Documentation Coverage:** 89.5652% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestGetAccountTransfers` **(I/O & Config Routines)** (Impact: 30.1)
  * `ConcurrencyTest` **(Compute Cores)** (Impact: 21.7)
  * `TestQueryTransfers` **(I/O & Config Routines)** (Impact: 18.5)
  * `TestQueryAccounts` **(I/O & Config Routines)** (Impact: 18.0)
  * `ConcurrentLinkedChainTest` **(Callbacks & Closures)** (Impact: 13.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 81 instances
* *Concurrency (weighted view):* 205
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 364`, `args: 132`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 210`, `unreferenced_by_name: 44`
* *Architecture:* `io: 2`, `api: 55`, `concurrency: 90`, `import: 7`
* *Defense:* `safety: 21`, `doc: 11`, `test: 528`, `immutability_locks: 14`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.VisualStudio.TestTools.UnitTesting, System, System.Diagnostics, System.IO, System.Linq, System.Threading, System.Threading.Tasks
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lsm/groove.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.202)
- **Top Global Matches:** file_cluster_12: 8.202, file_cluster_5: 9.501, file_cluster_4: 9.582
- **Magnitude:** 882.42 | **LOC:** 1496 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 1.756; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.1%), Guard Balance (formerly Safety Score) (50.8%), Mutation Surface (formerly State Flux) (46.6%)
- **Documentation Coverage:** 53.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GrooveType` **(Many-Argument Workhorses)** (Impact: 379.4)
    * *Intent:* /// A Groove is a collection of LSM trees auto generated for fields on a struct type /// as well as ...
  * `init` **(Many-Argument Workhorses)** (Impact: 45.7)
  * `HelperType` **(Defensive Guards)** (Impact: 26.1)
  * `lookup_object_callback` **(Defensive Guards)** (Impact: 23.1)
  * `prefetch_from_memory_by_timestamp` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* /// This function attempts to prefetch a value for the timestamp from the ObjectTree's /// table blo...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 62
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 75`, `args: 58`, `func_start: 57`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 32`, `high_risk_execution: 1`, `state_mutation: 32`, `planned_debt: 2`
* *Architecture:* `api: 40`, `import: 16`
* *Defense:* `safety: 60`, `doc: 97`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.756
  * `Choke Point (Betweenness):` 0.006121 | `Ripple Effect (Closeness):` 0.141788
  * `Imports (Out-Degree: 12):` constants.zig, grid.zig, builtin, cache_map.zig, composite_key.zig, manifest_log.zig, node_pool.zig, scan_builder.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lsm/segmented_array.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.345)
- **Top Global Matches:** file_cluster_4: 8.345, file_cluster_12: 9.123, file_cluster_5: 10.691
- **Magnitude:** 839.18 | **LOC:** 1501 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 1.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (65.4%), Connectivity (formerly Api Exposure) (61.9%), Guard Balance (formerly Safety Score) (49.6%)
- **Documentation Coverage:** 70.5128% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SegmentedArrayBaseType` **(Many-Argument Workhorses)** (Impact: 252.0)
  * `FuzzContextType` **(Many-Argument Workhorses)** (Impact: 117.2)
    * *Intent:* /// In order to avoid making internal details of segmented array public, the fuzzing code is defined...
  * `verify` **(Defensive Guards)** (Impact: 26.4)
  * `run_fuzz` **(Many-Argument Workhorses)** (Impact: 22.2)
  * `remove_elements_batch` **(Many-Argument Workhorses)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 21 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 85
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 85`, `args: 49`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 43`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 27`, `import: 10`
* *Defense:* `safety: 97`, `doc: 36`, `test: 2`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.288
  * `Choke Point (Betweenness):` 0.000718 | `Ripple Effect (Closeness):` 0.071254
  * `Imports (Out-Degree: 7):` direction.zig, binary_search.zig, composite_key.zig, manifest.zig, node_pool.zig, std, stdx, table.zig
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/vsr/message_header.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.278)
- **Top Global Matches:** file_cluster_4: 6.278, file_cluster_15: 8.855, file_cluster_9: 10.106
- **Magnitude:** 784.3 | **LOC:** 1778 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 80.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **5**; blast radius 4.234; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (29.4%)
- **Documentation Coverage:** 87.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `invalid_header` **(Compute Cores)** (Impact: 64.0)
  * `invalid_header` **(Compute Cores)** (Impact: 51.3)
  * `invalid_header` **(Compute Cores)** (Impact: 40.3)
  * `invalid_header` **(Compute Cores)** (Impact: 22.4)
  * `format_header_field` **(Many-Argument Workhorses)** (Impact: 22.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 257`, `args: 52`, `func_start: 52`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`, `planned_debt: 4`
* *Architecture:* `api: 271`, `import: 5`
* *Defense:* `safety: 23`, `doc: 128`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.234
  * `Choke Point (Betweenness):` 0.000311 | `Ripple Effect (Closeness):` 0.14854
  * `Imports (Out-Degree: 4):` constants.zig, schema.zig, vsr.zig, std, stdx
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/lsm/manifest_level.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.93)
- **Top Global Matches:** file_cluster_4: 5.93, file_cluster_12: 9.977, file_cluster_15: 10.8
- **Magnitude:** 763.32 | **LOC:** 1295 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 1.121; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (67.5%), Connectivity (formerly Api Exposure) (60.0%), Guard Balance (formerly Safety Score) (47.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.0%)
- **Documentation Coverage:** 59.322% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ManifestLevelType` **(Many-Argument Workhorses)** (Impact: 180.8)
  * `TestContextType` **(Many-Argument Workhorses)** (Impact: 136.7)
  * `verify_snapshot` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `delete_tables` **(Defensive Guards)** (Impact: 26.8)
  * `next_table` **(Many-Argument Workhorses)** (Impact: 22.8)
    * *Intent:* /// Returns the next table in the range, after `key_exclusive` if provided. /// /// * The table retu...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 76
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 109`, `args: 40`, `func_start: 40`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 34`, `planned_debt: 2`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 81`, `doc: 71`, `test: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 0.000773 | `Ripple Effect (Closeness):` 0.086249
  * `Imports (Out-Degree: 9):` constants.zig, direction.zig, binary_search.zig, manifest.zig, node_pool.zig, segmented_array.zig, std, stdx...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/clients/java/src/jni.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.685)
- **Top Global Matches:** file_cluster_15: 6.685, file_cluster_2: 8.273, file_cluster_16: 8.468
- **Magnitude:** 743.96 | **LOC:** 3239 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); blast radius 2.225; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.0%), Mutation Surface (formerly State Flux) (8.5%)
- **Documentation Coverage:** 1.6484% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `JNIInterfaceType` **(Type Conversions)** (Impact: 6.0)
    * *Intent:* /// Invokes a function at the offset of the vtable, allowing to utilize the function pointer /// wit...
  * `to_jvalue` **(Generic / Templated Code)** (Impact: 4.9)
  * `JniFnType` **(Generic / Templated Code)** (Impact: 4.8)
  * `define_class` **(Many-Argument Workhorses)** (Impact: 3.1)
    * *Intent:* /// https://docs.oracle.com/en/java/javase/17/docs/specs/jni/functions.html#defineclass.
  * `call_nonvirtual_object_method` **(Many-Argument Workhorses)** (Impact: 3.1)
    * *Intent:* /// https://docs.oracle.com/en/java/javase/17/docs/specs/jni/functions.html#callnonvirtualtypemethod...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 123`, `args: 180`, `func_start: 180`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`
* *Architecture:* `api: 221`
* *Defense:* `doc: 549`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.225
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006834
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vsr/grid.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.546)
- **Top Global Matches:** file_cluster_12: 7.546, file_cluster_15: 7.962, file_cluster_4: 8.606
- **Magnitude:** 739.54 | **LOC:** 1597 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **11**; blast radius 4.846; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.3%), Guard Balance (formerly Safety Score) (47.4%)
- **Documentation Coverage:** 56.1644% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GridType` **(Many-Argument Workhorses)** (Impact: 256.1)
    * *Intent:* /// The Grid provides access to on-disk blocks (blobs of `block_size` bytes). /// Each block is iden...
  * `read_block_resolve` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `read_block_from_cache` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /// Fetch the block synchronously from the write queues or grid cache, if possible. /// The returned...
  * `read_block_tick_callback` **(Defensive Guards)** (Impact: 22.2)
  * `writing` **(Defensive Guards)** (Impact: 19.3)
    * *Intent:* /// If the address is being written to by a non-repair, return `.create`. /// If the address is bein...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 10 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 56
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 98`, `args: 56`, `func_start: 49`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 36`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 36`, `import: 15`
* *Defense:* `safety: 67`, `doc: 112`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.846
  * `Choke Point (Betweenness):` 0.007605 | `Ripple Effect (Closeness):` 0.15341
  * `Imports (Out-Degree: 9):` constants.zig, schema.zig, set_associative_cache.zig, queue.zig, storage.zig, vsr.zig, free_set.zig, grid_blocks_missing.zig...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/clients/node/src/test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.71)
- **Top Global Matches:** file_cluster_10: 4.71, file_cluster_2: 6.574, file_cluster_15: 7.424
- **Magnitude:** 728.02 | **LOC:** 1544 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.704; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.8%), Complexity Load (formerly Cognitive Load) (94.8%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Callbacks & Closures)** (Impact: 2.9)
  * `test` **(Callbacks & Closures)** (Impact: 1.9)
  * `skip` **(Callbacks & Closures)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 70 instances
* *Amplified Cascading Flux:* 41 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 513
* *State Mutation (weighted view):* 182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 233`, `args: 36`, `func_start: 27`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 100`, `planned_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `concurrency: 163`, `import: 2`
* *Defense:* `safety: 10`, `test: 25`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` , assert
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/clients/go/tb_client_test.go` (GO | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.445)
- **Top Global Matches:** file_cluster_4: 8.445, file_cluster_6: 8.602, file_cluster_15: 14.883
- **Magnitude:** 714.38 | **LOC:** 1654 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.704; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (48.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.6%), Complexity Load (formerly Cognitive Load) (38.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `doTestClient` **(Many-Argument Workhorses)** (Impact: 261.3)
  * `WithClient` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `doTestImportedFlag` **(Many-Argument Workhorses)** (Impact: 16.6)
  * `BenchmarkNop` **(Defensive Guards)** (Impact: 4.7)
  * `assertCreateAccountsOK` **(Parameter Forwarders)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 113 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 31`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 129`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `concurrency: 2`, `import: 1`
* *Defense:* `safety: 88`, `doc: 55`, `test: 205`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` bytes, fmt, assert, big, rand, os, exec, runtime...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vopr.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.133)
- **Top Global Matches:** file_cluster_6: 6.133, file_cluster_4: 8.709, file_cluster_12: 16.337
- **Magnitude:** 699.66 | **LOC:** 1786 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.704; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (89.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.8%)
- **Documentation Coverage:** 64.5833% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `core_missing_prepare` **(Many-Argument Workhorses)** (Impact: 86.3)
    * *Intent:* // Returns an op for a prepare which can't be repaired by the core due to storage faults. // // If a...
  * `main` **(I/O & Config Routines)** (Impact: 53.8)
  * `core_missing_blocks` **(Many-Argument Workhorses)** (Impact: 37.9)
    * *Intent:* /// Check whether the cluster is stuck because the entire core is missing the same block[s].
  * `pending` **(Defensive Guards)** (Impact: 30.0)
  * `tick_requests` **(Compute Cores)** (Impact: 26.7)
    * *Intent:* /// Maybe send a request from one of the cluster's clients.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 149`, `args: 34`, `func_start: 34`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 4`, `state_mutation: 70`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 18`, `import: 23`
* *Defense:* `safety: 76`, `doc: 47`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` fuzz.zig, builtin, config.zig, constants.zig, schema.zig, message_pool.zig, state_machine.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/multiversion.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.69)
- **Top Global Matches:** file_cluster_4: 7.69, file_cluster_12: 8.779, file_cluster_15: 10.66
- **Magnitude:** 679.74 | **LOC:** 2195 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **7**; blast radius 2.644; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.7%), Mutation Surface (formerly State Flux) (59.2%), Guard Balance (formerly Safety Score) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.2%)
- **Documentation Coverage:** 75.8929% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_elf` **(Compute Cores)** (Impact: 53.1)
    * *Intent:* /// Parse an untrusted, unverified, and potentially corrupt ELF file. This parsing happens before //...
  * `init` **(Many-Argument Workhorses)** (Impact: 42.6)
  * `verify` **(Defensive Guards)** (Impact: 32.2)
  * `target_update` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `verify` **(Defensive Guards)** (Impact: 24.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 111
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 202`, `args: 69`, `func_start: 66`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 12`, `state_mutation: 69`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `io: 60`, `api: 54`, `import: 7`
* *Defense:* `safety: 152`, `doc: 78`, `test: 3`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.644
  * `Choke Point (Betweenness):` 0.003337 | `Ripple Effect (Closeness):` 0.143969
  * `Imports (Out-Degree: 7):` vsr.zig, builtin, constants.zig, io.zig, std, stdx, checksum.zig
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/tigerbeetle/inspect.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.729)
- **Top Global Matches:** file_cluster_4: 7.729, file_cluster_12: 9.225, file_cluster_9: 9.818
- **Magnitude:** 671.04 | **LOC:** 1659 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.958; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (54.5%), Guard Balance (formerly Safety Score) (37.1%), Connectivity (formerly Api Exposure) (21.3%), Complexity Load (formerly Cognitive Load) (18.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect_tables` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `run_inspect` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `print_struct` **(Defensive Guards)** (Impact: 35.3)
  * `print_block` **(Defensive Guards)** (Impact: 28.9)
  * `inspect_replies_slot` **(Defensive Guards)** (Impact: 24.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 20 instances
* *Amplified Cascading Flux:* 25 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 132`, `args: 39`, `func_start: 39`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 42`, `planned_debt: 1`
* *Architecture:* `io: 32`, `api: 3`, `import: 6`
* *Defense:* `safety: 270`, `doc: 9`, `cleanup: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.958
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.005177
  * `Imports (Out-Degree: 7):` cli.zig, inspect_integrity.zig, main.zig, std, vsr
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/message_bus.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.471)
- **Top Global Matches:** file_cluster_4: 8.471, file_cluster_12: 8.909, file_cluster_5: 11.124
- **Magnitude:** 663.02 | **LOC:** 1220 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.08; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.7%), Guard Balance (formerly Safety Score) (52.3%), Connectivity (formerly Api Exposure) (48.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.1%)
- **Documentation Coverage:** 72.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MessageBusType` **(Many-Argument Workhorses)** (Impact: 215.6)
  * `recv_update_peer` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `init` **(Many-Argument Workhorses)** (Impact: 24.0)
    * *Intent:* /// Initialize the MessageBus for the given configuration and replica/client process.
  * `deinit` **(Defensive Guards)** (Impact: 17.6)
  * `recv_callback` **(Many-Argument Workhorses)** (Impact: 16.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 25 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 62`, `args: 38`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 51`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 14`, `import: 7`
* *Defense:* `safety: 65`, `doc: 73`, `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.08
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.142147
  * `Imports (Out-Degree: 6):` message_buffer.zig, queue.zig, constants.zig, message_pool.zig, std, stdx, vsr.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/io/windows.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.455)
- **Top Global Matches:** file_cluster_5: 8.455, file_cluster_7: 8.578, file_cluster_12: 8.83
- **Magnitude:** 647.54 | **LOC:** 1610 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%), Connectivity (formerly Api Exposure) (67.1%), Mutation Surface (formerly State Flux) (43.9%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connect` **(Many-Argument Workhorses)** (Impact: 38.5)
  * `accept` **(Many-Argument Workhorses)** (Impact: 32.1)
  * `open_data_file` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /// Opens or creates a journal file: /// - For reading and writing. /// - For Direct I/O (required o...
  * `windows_open_file` **(Many-Argument Workhorses)** (Impact: 28.3)
    * *Intent:* // Vendor std.os.windows.OpenFile so we can set file attributes. Add it as a parameter after // `opt...
  * `flush` **(Defensive Guards)** (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 190`, `args: 59`, `func_start: 57`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 116`, `high_risk_execution: 4`, `state_mutation: 37`, `dead_code: 1`, `planned_debt: 5`
* *Architecture:* `io: 19`, `api: 57`, `import: 8`
* *Defense:* `safety: 73`, `doc: 17`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.061
  * `Choke Point (Betweenness):` 0.000388 | `Ripple Effect (Closeness):` 0.10777
  * `Imports (Out-Degree: 6):` constants.zig, io.zig, queue.zig, time.zig, common.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/io/linux.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.759)
- **Top Global Matches:** file_cluster_12: 7.759, file_cluster_7: 9.633, file_cluster_5: 9.75
- **Magnitude:** 598.66 | **LOC:** 1892 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 2.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.8%), Guard Balance (formerly Safety Score) (51.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.8%), Mutation Surface (formerly State Flux) (35.2%)
- **Documentation Coverage:** 69.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `open_data_file` **(Many-Argument Workhorses)** (Impact: 125.7)
    * *Intent:* /// Opens or creates a journal file: /// - For reading and writing. /// - For Direct I/O (if possibl...
  * `complete` **(Many-Argument Workhorses)** (Impact: 83.2)
  * `flush_completions` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `flush` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `flush_submissions` **(Defensive Guards)** (Impact: 10.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 151`, `args: 50`, `func_start: 48`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 9`, `state_mutation: 37`, `planned_debt: 3`
* *Architecture:* `io: 19`, `api: 59`, `import: 9`
* *Defense:* `safety: 98`, `doc: 56`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.061
  * `Choke Point (Betweenness):` 0.001413 | `Ripple Effect (Closeness):` 0.10777
  * `Imports (Out-Degree: 7):` constants.zig, io.zig, list.zig, queue.zig, superblock.zig, common.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/testing/cluster.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.171)
- **Top Global Matches:** file_cluster_4: 9.171, file_cluster_6: 11.655, file_cluster_12: 12.314
- **Magnitude:** 569.72 | **LOC:** 1199 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 1.58; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (63.0%), Guard Balance (formerly Safety Score) (47.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.8%), Complexity Load (formerly Cognitive Load) (5.9%)
- **Documentation Coverage:** 72.093% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ClusterType` **(Many-Argument Workhorses)** (Impact: 182.9)
  * `init` **(Many-Argument Workhorses)** (Impact: 59.1)
  * `log_replica` **(Many-Argument Workhorses)** (Impact: 50.1)
  * `tick` **(Defensive Guards)** (Impact: 25.5)
  * `deinit` **(I/O & Config Routines)** (Impact: 21.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 54 instances
* *Amplified Cascading Flux:* 18 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 87`, `args: 32`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 2`, `state_mutation: 47`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 32`, `import: 20`
* *Defense:* `safety: 108`, `doc: 34`, `cleanup: 81`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.58
  * `Choke Point (Betweenness):` 0.006611 | `Ripple Effect (Closeness):` 0.14002
  * `Imports (Out-Degree: 18):` aof.zig, constants.zig, message_pool.zig, vsr.zig, replica_format.zig, grid_checker.zig, journal_checker.zig, manifest_checker.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.268)
- **Top Global Matches:** file_cluster_15: 6.268, file_cluster_12: 7.992, file_cluster_16: 8.103
- **Magnitude:** 566.84 | **LOC:** 2294 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 46.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.704; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (78.4%), Guard Balance (formerly Safety Score) (48.9%), Mutation Surface (formerly State Flux) (23.8%)
- **Documentation Coverage:** 44.1176% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build_ci` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* /// This is what is called by CI infrastructure, but you can also use it locally. In particular, ///...
  * `fetch_release` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `build_test_jni` **(Many-Argument Workhorses)** (Impact: 29.6)
  * `build_tigerbeetle` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `build_test` **(Many-Argument Workhorses)** (Impact: 22.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 12 instances
* *High Risk Execution (weighted view):* 5
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 80`, `args: 54`, `func_start: 54`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 14`, `state_mutation: 37`, `planned_debt: 4`
* *Architecture:* `io: 9`, `api: 10`, `import: 2`
* *Defense:* `safety: 81`, `doc: 26`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/scripts/cfo.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.716)
- **Top Global Matches:** file_cluster_4: 5.716, file_cluster_6: 9.811, file_cluster_15: 11.602
- **Magnitude:** 565.38 | **LOC:** 1865 | **CtrlFlow:** 10.5% | **Authorship Centralization:** 83.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.787; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.1%), Mutation Surface (formerly State Flux) (49.3%), Guard Balance (formerly Safety Score) (43.7%), Connectivity (formerly Api Exposure) (38.8%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_fuzzers` **(Many-Argument Workhorses)** (Impact: 104.1)
  * `run_fuzzers_prepare_tasks` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `upload_results` **(Many-Argument Workhorses)** (Impact: 46.6)
  * `merge` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* // Merges two sets of seeds keeping the more interesting one. A direct way to write this would // be...
  * `run_fuzzers_start_fuzzer` **(Defensive Guards)** (Impact: 27.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 27 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 100`, `args: 32`, `func_start: 32`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 1`, `state_mutation: 37`, `planned_debt: 3`
* *Architecture:* `io: 9`, `api: 10`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 155`, `doc: 65`, `test: 2`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.787
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.004556
  * `Imports (Out-Degree: 3):` shell.zig, builtin, std, stdx
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/clients/python/tests/test_basic.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.997)
- **Top Global Matches:** file_cluster_12: 6.997, file_cluster_7: 8.921, file_cluster_4: 9.861
- **Magnitude:** 530.5 | **LOC:** 1447 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.704; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.6%), Guard Balance (formerly Safety Score) (41.8%), Complexity Load (formerly Cognitive Load) (26.9%), Connectivity (formerly Api Exposure) (9.0%)
- **Documentation Coverage:** 92.1569% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `test_get_account_transfers` **(Defensive Guards)** (Impact: 37.7)
  * `test_query_transfers` **(Defensive Guards)** (Impact: 34.4)
  * `test_query_accounts` **(Defensive Guards)** (Impact: 27.8)
  * `test_uint128` **(Defensive Guards)** (Impact: 9.2)
  * `test_import_accounts_and_transfers` **(Defensive Guards)** (Impact: 5.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 334`, `args: 25`, `func_start: 25`
* *Risk/State:* `safety_bypasses: 35`, `high_risk_execution: 2`, `state_mutation: 185`, `unreferenced_by_name: 24`
* *Architecture:* `io: 3`, `api: 25`, `import: 8`
* *Defense:* `safety: 300`, `doc: 2`, `test: 27`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.704
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` dataclasses, json, os, pytest, subprocess, sys, tigerbeetle, time
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/scripts.zig` (ZIG) | Magnitude: 14.84 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, safety: 18, core_var_decl: 16, design_snake_case: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/clients/dotnet/TigerBeetle.Tests/IntegrationTests.cs` (CSHARP) | Magnitude: 922.14 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1912, core_var_decl: 719, test: 528, design_pascal_case: 371

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/clients/java/src/main/java/com/tigerbeetle/AccountFilter.java` (JAVA) | Magnitude: 103.38 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 35, args: 31, func_start: 31
- `src/clients/java/src/main/java/com/tigerbeetle/QueryFilterBatch.java` (JAVA) | Magnitude: 66.18 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 100, structural_boundaries: 38, args: 25, func_start: 25
- `src/clients/java/src/main/java/com/tigerbeetle/QueryFilter.java` (JAVA) | Magnitude: 83.46 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 80, structural_boundaries: 28, args: 24, func_start: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/stdx/testing/snaptest.zig` (ZIG) | Magnitude: 110.72 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 179, doc: 98, core_var_decl: 41, structural_boundaries: 39
- `src/time.zig` (ZIG) | Magnitude: 56.26 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 125, core_var_decl: 40, design_snake_case: 34, structural_boundaries: 23
- `src/clients/java/src/test/java/com/tigerbeetle/AccountFilterTest.java` (JAVA) | Magnitude: 89.28 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 87, test: 58, core_var_decl: 30
- `src/tigerbeetle/benchmark_driver.zig` (ZIG) | Magnitude: 81.0 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 157, safety: 35, core_var_decl: 32, design_snake_case: 26
- `src/vsr/fault_detector.zig` (ZIG) | Magnitude: 70.7 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 135, doc: 42, core_var_decl: 37, design_snake_case: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/clients/java/src/main/java/com/tigerbeetle/RequestException.java` (JAVA) | Magnitude: 26.46 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 30, branch: 14, structural_boundaries: 14, api: 5
- `src/clients/java/src/main/java/com/tigerbeetle/InitializationException.java` (JAVA) | Magnitude: 24.32 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, branch: 12, structural_boundaries: 12, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/clients/python/ci.zig` (ZIG) | Magnitude: 26.04 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 89, safety: 33, core_var_decl: 18, design_snake_case: 16
- `src/clients/java/src/main/java/com/tigerbeetle/AccountFilterBatch.java` (JAVA) | Magnitude: 74.34 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 40, args: 28, func_start: 28
- `src/config.zig` (ZIG) | Magnitude: 35.22 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 194, core_var_decl: 79, design_snake_case: 66, doc: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/clients/rust/src/conversions.rs` (RUST) | Magnitude: 40.72 | Delta: **0.116** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 270, core_var_decl: 145, design_pascal_case: 108, design_long_vars: 76

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/vsr/journal.zig` (ZIG) | Magnitude: 1189.1 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 1621, doc: 368, branch: 207, core_var_decl: 206
- `src/state_machine/workload.zig` (ZIG) | Magnitude: 1019.2 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1792, core_var_decl: 213, design_snake_case: 176, branch: 142
- `src/vsr/grid_scrubber.zig` (ZIG) | Magnitude: 377.08 | Delta: **0.139** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 500, core_var_decl: 87, doc: 64, design_snake_case: 64
- `src/clients/go/tb_client_test.go` (GO) | Magnitude: 714.38 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 1383, test: 205, state_mutation: 129, branch: 127

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/clients/rust/src/time_based_id.rs` (RUST) | Magnitude: 76.08 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 187, structural_boundaries: 70, core_var_decl: 46, design_snake_case: 44
- `src/clients/dotnet/TigerBeetle/NativeClient.cs` (CSHARP) | Magnitude: 46.04 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 27, core_var_decl: 15, generics: 13
- `src/io/windows.zig` (ZIG) | Magnitude: 647.54 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1298, structural_boundaries: 190, core_var_decl: 147, safety_bypasses: 116

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/lsm/k_way_merge.zig` (ZIG) | Magnitude: 429.72 | Delta: **0.132** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 586, core_var_decl: 107, design_snake_case: 80, branch: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/clients/python/src/tigerbeetle/__init__.py` (PYTHON) | Magnitude: 17.68 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 6, import: 3, safety_bypasses: 1
- `src/cdc/amqp/types.zig` (ZIG) | Magnitude: 74.28 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 184, doc: 105, core_var_decl: 42, design_pascal_case: 24
- `src/clients/java/src/main/java/com/tigerbeetle/Request.java` (JAVA) | Magnitude: 148.26 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 38, branch: 30, state_mutation: 26
- `src/vsr/checksum_benchmark.zig` (ZIG) | Magnitude: 21.58 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 19, core_var_decl: 16, design_snake_case: 12, globals: 8
- `src/clients/node/node.zig` (ZIG) | Magnitude: 147.3 | Delta: **0.137** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 383, structural_boundaries: 77, core_var_decl: 70, safety: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/unit_tests.zig` (ZIG) | Magnitude: 33.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 277, core_var_decl: 116, import: 79, design_short_vars: 73
- `src/clients/node/src/benchmark.ts` (TYPESCRIPT) | Magnitude: 73.42 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 126, core_var_decl: 32, structural_boundaries: 15, design_snake_case: 15
- `src/cdc/amqp/spec_parser.py` (PYTHON) | Magnitude: 294.28 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 263, debug_prints: 99, core_var_decl: 84, design_snake_case: 70

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` -> Churn: **54.18%** | Cog Load: 89.8437% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/clients/java/src/test/java/com/tigerbeetle/IntegrationTest.java` -> **batiati** (100.0% isolated ownership) | Magnitude: 1176.42
- `src/state_machine/workload.zig` -> **batiati** (100.0% isolated ownership) | Magnitude: 1019.2
- `src/clients/dotnet/TigerBeetle.Tests/IntegrationTests.cs` -> **batiati** (100.0% isolated ownership) | Magnitude: 922.14
- `src/clients/node/src/test.ts` -> **batiati** (100.0% isolated ownership) | Magnitude: 728.02
- `src/clients/go/tb_client_test.go` -> **batiati** (100.0% isolated ownership) | Magnitude: 714.38

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/vsr.zig` -> **Severity: 2.301** (Bridge: 0.0882 * Flux: 26.0769%)
- `src/stdx/stdx.zig` -> **Severity: 1.317** (Bridge: 0.0193 * Flux: 68.3444%)
- `src/state_machine.zig` -> **Severity: 0.297** (Bridge: 0.0073 * Flux: 40.9051%)
- `src/vsr/grid.zig` -> **Severity: 0.297** (Bridge: 0.0076 * Flux: 39.0055%)
- `src/lsm/groove.zig` -> **Severity: 0.285** (Bridge: 0.0061 * Flux: 46.5747%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/stdx/stdx.zig` -> **Severity: 15.201** (Embedded: 0.3626 * Error Risk: 41.9165%)
- `src/stdx/radix.zig` -> **Severity: 12.224** (Embedded: 0.2128 * Error Risk: 57.451%)
- `src/stdx/prng.zig` -> **Severity: 11.701** (Embedded: 0.2192 * Error Risk: 53.3706%)
- `src/stdx/mlock.zig` -> **Severity: 11.675** (Embedded: 0.2128 * Error Risk: 54.8709%)
- `src/counting_allocator.zig` -> **Severity: 11.233** (Embedded: 0.1404 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/stdx/stdx.zig` -> **Severity: 8968.605** (Blast Radius: 175.855 * Doc Risk: 51.0%)
- `src/vsr.zig` -> **Severity: 3352.114** (Blast Radius: 44.435 * Doc Risk: 75.4386%)
- `src/stdx/time_units.zig` -> **Severity: 1523.4** (Blast Radius: 17.773 * Doc Risk: 85.7143%)
- `src/clients/java/src/main/java/com/tigerbeetle/AssertionError.java` -> **Severity: 1357.9** (Blast Radius: 13.579 * Doc Risk: 100.0%)
- `src/scripts/client_readmes.zig` -> **Severity: 1202.1** (Blast Radius: 12.021 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 943 literal sites + 6 sites through wrappers = 949

- `tidy_line_length` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/tidy.zig`
- `bytes` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/stdx/stdx.zig`
- `realtime_unix` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/time.zig`
- `url2slug` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/docs_website/src/docs.zig`
- `write_callback` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/io/test.zig`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 26418 call pairs -- scoped 30.5%, unique 0.4%, ambiguous 17.8%, external 51.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 20039 | 27.4% | 0.0% | 19.0% | 53.7% |
| java | 3595 | 54.9% | 2.1% | 19.4% | 23.6% |
| rust | 871 | 16.4% | 0.0% | 0.1% | 83.5% |
| csharp | 639 | 31.1% | 0.6% | 15.6% | 52.6% |
| python | 427 | 21.3% | 0.0% | 14.3% | 64.4% |
| go | 371 | 24.0% | 6.2% | 9.2% | 60.6% |
| javascript | 258 | 16.7% | 0.0% | 1.9% | 81.4% |
| html | 81 | 18.5% | 0.0% | 0.0% | 81.5% |
| typescript | 46 | 19.6% | 0.0% | 4.3% | 76.1% |
| c | 42 | 9.5% | 0.0% | 0.0% | 90.5% |

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
