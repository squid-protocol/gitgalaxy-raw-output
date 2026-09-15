# ARCHITECTURAL_BRIEF: vyre
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/santhsecurity/vyre` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 4674 |
| Analyzed Artifacts (Scanned) | 4128 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 546 |
| Total LOC | 753480 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.3% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8753 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3472 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.012 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 56 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 3685 | 722346 | 89.3% |
| MARKDOWN | 217 | 0 | 5.3% |
| SHELL | 118 | 5983 | 2.9% |
| C | 56 | 19144 | 1.4% |
| JSON | 24 | 4729 | 0.6% |
| PLAINTEXT | 18 | 10 | 0.4% |
| PYTHON | 6 | 753 | 0.1% |
| GO | 4 | 515 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +1.48; from the repo's file-archetype mix)
> **File Composition:** Tests & Verification Files 34%, Large Core Modules 19%, Data / Markup / Trivial 13%, State Mutators Files 7%, Declarative / Non-Code 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3893 | 94.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 234 | 5.7% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 546*

**Composition by Extension & Reason:**
- `.md`: 189x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2191 LOC), 1x Excluded (Machine-Generated Source Code Signature: 145 LOC)
- `.json`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4672 LOC)
- `.toml`: 41x Unsupported Format (.toml), 19x Excluded (Unsupported Extension: '.toml'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 28x Excluded (Unsupported Extension: '.stderr')
- `no_extension`: 18x Excluded (Unsupported Extension: '.proptest-regressions'), 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wgsl`: 10x Unsupported Format (.wgsl)
- `.lock`: 7x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.tmpl`: 3x Excluded (Unsupported Extension: '.tmpl')
- `.c`: 1x Excluded (Machine-Generated Source Code Signature: 138 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1522 LOC)
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.tsv`: 1x Excluded (Static Asset Blob without Intent: 1835 LOC)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.9 | 3.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 35.7 | 43.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 21.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 7.4 | 2.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 1.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 88.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 41.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 56.1 | 56.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 36162 | 2853 | 21 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/expr.c` |
| cleanup | 219 | 83 | 0 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/confdata.c` |
| guards | 16774 | 2351 | 10 | `xtask/src/vyre_weir_release_gate.rs` |
| danger | 14113 | 1816 | 10 | `vyre-driver-cuda/tests/resident_dispatch_contracts.rs` |
| concurrency | 2600 | 595 | 2 | `vyre-libs/tests/fixtures/go/pipeline.go` |
| connectivity | 22676 | 2412 | 16 | `vyre-driver-cuda/src/egraph_kernel_plan.rs` |
| io | 3279 | 379 | 0 | `scripts/bench_index.sh` |
| crypto | 1 | 1 | 0 | `benches/competition/scripts/check_corpora.py` |
| ipc | 90 | 58 | 0 | `tools/divergence-gate.py` |
| time | 218 | 137 | 0 | `conform/vyre-conform-runner/src/main.rs` |
| serialization | 214 | 83 | 0 | `vyre-lower/src/descriptor.rs` |
| regex | 288 | 87 | 0 | `scripts/check_capability_negotiation.sh` |
| events | 398 | 125 | 0 | `vyre-driver-cuda/src/backend/resident_dispatch.rs` |
| tests | 47205 | 2365 | 33 | `vyre-driver-cuda/tests/egraph_device_image_upload.rs` |
| docs | 60991 | 2923 | 45 | `vyre-driver/src/backend/vyre_backend.rs` |
| debt | 3119 | 491 | 1 | `vyre-frontend-c/tests/r2_corpus_measurement.rs` |
| mutation | 102846 | 3288 | 63 | `xtask/src/vyre_weir_release_gate.rs` |
| dead_code | 17511 | 2939 | 11 | `vyre-driver-wgpu/src/backend_impl.rs` |
| credential | 19 | 8 | 0 | `vyre-libs/src/scan/test_fixtures.rs` |
| threat | 256 | 102 | 0 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/asn1_compiler.c` |
| ml_ai | 4514 | 485 | 1 | `vyre-self-substrate/src/math/scientific_kernel_pipeline.rs` |
| ui | 58 | 10 | 0 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/gconf.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/bench_index.sh` (Hits: 126)
- `scripts/check_no_string_wgsl.sh` (Hits: 73)
- `scripts/check_repo_hygiene.sh` (Hits: 62)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cargo_runner.sh** (`scripts/lib/cargo_runner.sh`) — 30 inbound connections
2. **slot.rs** (`vyre-runtime/src/megakernel/protocol/slot.rs`) — 18 inbound connections
3. **transfer_accounting.rs** (`vyre-driver/src/transfer_accounting.rs`) — 15 inbound connections
4. **debug.rs** (`vyre-runtime/src/megakernel/protocol/debug.rs`) — 9 inbound connections
5. **opcode.rs** (`vyre-runtime/src/megakernel/protocol/opcode.rs`) — 7 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`vyre-driver-cuda/src/lib.rs`) — 197 outbound dependencies
2. **mod.rs** (`vyre-runtime/src/megakernel/mod.rs`) — 166 outbound dependencies
3. **mod.rs** (`vyre-libs/src/parsing/c/parse/vast/mod.rs`) — 150 outbound dependencies
4. **lib.rs** (`vyre-driver/src/lib.rs`) — 135 outbound dependencies
5. **lib.rs** (`vyre-foundation/src/lib.rs`) — 133 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `fill_upload_resident_many_repeated_sequence_read_ranges_borrowed_into` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **396.9** | LOC: 475
- `simplify_binop` **(Many-Argument Workhorses)** (@ `vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`) -> Impact: **368.9** | LOC: 617
  * *Intent:* /// Algebraic identity simplifications for binary operators. /// These rewrites are always valid and don't require literal operands - /// they fire wh...
- `reference_typed_kind` **(Compute Cores)** (@ `vyre-libs/src/parsing/c/parse/vast/ref_typedef/typed_kind.rs`) -> Impact: **348.4** | LOC: 351
- `flush_active_macro_segment_inner` **(Many-Argument Workhorses)** (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_expansion/flush.rs`) -> Impact: **343.0** | LOC: 574
- `emit_op` **(Many-Argument Workhorses)** (@ `vyre-emit-ptx/src/emitter.rs`) -> Impact: **321.5** | LOC: 470
- `dispatch_resident_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **313.5** | LOC: 432
- `run_semantic_requirement_checks` **(Many-Argument Workhorses)** (@ `xtask/src/vyre_weir_release_gate.rs`) -> Impact: **300.6** | LOC: 1091
- `dispatch_borrowed_async_with_ptx_concrete` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/host_dispatch.rs`) -> Impact: **265.9** | LOC: 339
- `record_macro_token_provenance` **(Many-Argument Workhorses)** (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/token_provenance/macro_record.rs`) -> Impact: **246.8** | LOC: 256
  * *Intent:* /// Records provenance for a segment after GPU macro materialization.
- `record_cuda_graph_borrowed` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/cuda_graph.rs`) -> Impact: **221.7** | LOC: 409
  * *Intent:* /// Record one full Program dispatch into a CUDA graph using borrowed /// sample inputs. /// /// # Errors /// /// Returns [`BackendError`] when device...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `xtask/src` | 56 | 18417.68 | 14.62% | 10.49% |
| `vyre-primitives/src/graph` | 36 | 8899.08 | 6.56% | 34.57% |
| `vyre-driver/src` | 58 | 8563.46 | 6.37% | 50.9% |
| `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig` | 13 | 8447.18 | 76.23% | 0.0% |
| `vyre-driver-cuda/src/backend` | 25 | 6433.16 | 8.53% | 41.84% |
| `vyre-driver-cuda/src` | 33 | 6149.8 | 4.9% | 50.33% |
| `vyre-driver-wgpu/tests` | 166 | 5540.1 | 2.32% | 0.0% |
| `vyre-frontend-c/tests/corpus/r2_kernel_scripts` | 11 | 5400.7 | 26.2% | 0.0% |
| `vyre-primitives/src/math` | 43 | 5379.28 | 8.32% | 55.6% |
| `vyre-driver-wgpu/tests/__split` | 137 | 4959.48 | 3.15% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `conform/vyre-conform-generate/src/minimizer.rs` -> **100.0%** Exposure
- `vyre-emit-naga/src/program/mod_tests.rs` -> **100.0%** Exposure
- `vyre-foundation/src/ir_inner/model/program/stats/methods.rs` -> **100.0%** Exposure
- `vyre-self-substrate/src/graph/adaptive_traverse/resident.rs` -> **100.0%** Exposure
- `vyre-spec/src/extension.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/check_no_raw_unwrap.py` -> **100.0%** Exposure
- `scripts/check_no_under_reserve.py` -> **100.0%** Exposure
- `scripts/check_self_consumer_coverage.py` -> **100.0%** Exposure
- `tools/divergence-gate.py` -> **100.0%** Exposure
- `vyre-driver-wgpu/tests/common/c_fixture.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `vyre-driver-wgpu/src/backend_impl.rs` -> **53** Orphaned Functions | **0** Duplicates
- `vyre-driver/src/backend/registry/grid_sync_split.rs` -> **40** Orphaned Functions | **10** Duplicates
- `vyre-libs/tests/gpu_if_expression_roundtrip.rs` -> **47** Orphaned Functions | **0** Duplicates
- `vyre-primitives/tests/__split/adversarial_graph_reachability_fixpoint_chunk1.rs` -> **45** Orphaned Functions | **0** Duplicates
- `vyre-lower/src/descriptor.rs` -> **43** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `vyre-libs/src/scan/test_fixtures.rs` -> **100.0%** Exposure
- `vyre-libs/tests/cache_key_collision.rs` -> **99.9995%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28970` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `vyre-emit-ptx/src/emitter/results.rs` (RUST) -> Cumulative Risk: **722.21**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.11)
- **Magnitude:** 54.48 | **LOC:** 82 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Tech Debt (98.603%)
- **Heaviest Functions:** `bind_consecutive_results` (Many-Argument Workhorses, Impact: 11.1), `alloc_literal` (Compute Cores, Impact: 8.0), `finish_with_return` (Interface Declarations, Impact: 4.9)

### 2. `scripts/prove-release-shards.sh` (SHELL) -> Cumulative Risk: **721.37**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.74)
- **Magnitude:** 16.61 | **LOC:** 127 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Defensive Guards, Impact: 24.3), `__global_context__` (I/O & Config Routines, Impact: 3.1), `Anonymous_Block` (I/O & Config Routines, Impact: 2.6)

### 3. `vyre-bench/src/cases/cpu_baselines.rs` (RUST) -> Cumulative Risk: **717.1**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.32)
- **Magnitude:** 131.8 | **LOC:** 282 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), Safety Score (82.2391%)
- **Heaviest Functions:** `elementwise_add_f32_bytes_into` (Many-Argument Workhorses, Impact: 12.1), `matmul_f32_bytes` (Many-Argument Workhorses, Impact: 11.2), `attention_proxy_f32_bytes` (Many-Argument Workhorses, Impact: 10.9)

### 4. `scripts/check_trait_freeze.sh` (SHELL) -> Cumulative Risk: **710.45**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.82)
- **Magnitude:** 9.76 | **LOC:** 110 | **CtrlFlow:** 23.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `extract_block` (Compute Cores, Impact: 14.9), `Anonymous_Block` (I/O & Config Routines, Impact: 11.9), `__global_context__` (I/O & Config Routines, Impact: 8.0)

### 5. `scripts/check_repo_split_readiness.sh` (SHELL) -> Cumulative Risk: **710.07**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.74)
- **Magnitude:** 12.85 | **LOC:** 165 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (I/O & Config Routines, Impact: 18.6), `__global_context__` (I/O & Config Routines, Impact: 7.8), `check_publish_field` (Compute Cores, Impact: 5.8)

### 6. `scripts/check_public_api_snapshot.sh` (SHELL) -> Cumulative Risk: **707.67**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z -0.34)
- **Magnitude:** 7.08 | **LOC:** 81 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Anonymous_Block` (I/O & Config Routines, Impact: 8.6), `__global_context__` (I/O & Config Routines, Impact: 6.0), `Anonymous_Block` (Interface Declarations, Impact: 2.1)

### 7. `xtask/src/source_similar.rs` (RUST) -> Cumulative Risk: **699.81**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.22)
- **Magnitude:** 664.28 | **LOC:** 1168 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (97.3545%), Churn (95.42%)
- **Heaviest Functions:** `normalize_tokens` (Compute Cores, Impact: 60.8), `has_control_flow_keyword` (Compute Cores, Impact: 28.9), `collect_rust_files_recursive` (Many-Argument Workhorses, Impact: 28.4)

### 8. `scripts/check_gpu_test_loudness.sh` (SHELL) -> Cumulative Risk: **690.43**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Parameter Forwarders Files` (z -0.64)
- **Magnitude:** 4.78 | **LOC:** 87 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), State Flux (99.9971%)
- **Heaviest Functions:** `Anonymous_Block` (I/O & Config Routines, Impact: 7.8), `__global_context__` (I/O & Config Routines, Impact: 7.3), `has_loud_abort` (Parameter Forwarders, Impact: 4.1)

### 9. `scripts/check_unsafe_budget.sh` (SHELL) -> Cumulative Risk: **685.52**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z -0.34)
- **Magnitude:** 3.58 | **LOC:** 73 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Stability (100.0%), Documentation (100.0%), State Flux (99.9254%)
- **Heaviest Functions:** `is_whitelisted` (Interface Declarations, Impact: 4.7), `Anonymous_Block` (I/O & Config Routines, Impact: 4.5), `__global_context__` (I/O & Config Routines, Impact: 4.0)

### 10. `vyre-foundation/src/transform/inline/expand/impl_calleeexpander/composition.rs` (RUST) -> Cumulative Risk: **684.0**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z -0.80)
- **Magnitude:** 239.04 | **LOC:** 277 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Stability (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `push_atomic` (Many-Argument Workhorses, Impact: 23.4), `rename_expr_vars` (Defensive Guards, Impact: 22.2), `enter_expr_frame` (Many-Argument Workhorses, Impact: 13.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `xtask/src/release_completion_audit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3609.02 | **LOC:** 6411 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.3603%), Tech Debt (8.1602%)
**Top Internal Functions/Classes:**
  * `inspect_json_evidence` **(Many-Argument Workhorses)** (Impact: 153.7)
  * `inspect_pass_family_benchmark_manifest_semantics` **(Many-Argument Workhorses)** (Impact: 96.3)
  * `inspect_backend_suite_semantics` **(Many-Argument Workhorses)** (Impact: 95.2)
  * `inspect_release_workload_matrix_semantics` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `inspect_weir_matrix_semantics` **(Many-Argument Workhorses)** (Impact: 81.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 396 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 902`, `structural_boundaries: 497`, `args: 334`, `func_start: 87`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 466`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 304`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000242
  * `Imports (Out-Degree: 0):` PathBuf, Read, Serialize, serde::Deserialize, std::collections::BTreeSet, std::fs, std::io::self, std::path::Path
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xtask/src/vyre_weir_release_gate.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2780.2 | **LOC:** 6940 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.1984%), Tech Debt (8.3893%)
**Top Internal Functions/Classes:**
  * `run_semantic_requirement_checks` **(Many-Argument Workhorses)** (Impact: 300.6)
  * `check_backend_suite_report` **(Many-Argument Workhorses)** (Impact: 149.4)
  * `check_workload_matrix_artifact_coverage` **(Many-Argument Workhorses)** (Impact: 97.7)
  * `check_parser_contract_evidence` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `check_single_benchmark_report` **(Many-Argument Workhorses)** (Impact: 64.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 328 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 887`, `structural_boundaries: 554`, `args: 280`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 449`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 340`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PathBuf, Read, serde::Deserialize, std::collections::BTreeSet, std::fs, std::io::self, std::path::Path
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/backend/resident_dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1487.46 | **LOC:** 2201 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (22.0073%), Tech Debt (15.0348%)
**Top Internal Functions/Classes:**
  * `fill_upload_resident_many_repeated_sequence_read_ranges_borrowed_into` **(Many-Argument Workhorses)** (Impact: 396.9)
  * `dispatch_resident_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (Impact: 313.5)
  * `dispatch_resident_batch_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (Impact: 207.4)
  * `dispatch_resident_via_borrowed_into` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `dispatch_resident_timed` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /// Dispatch with CUDA-resident buffers and return ordered output readbacks.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 394`, `structural_boundaries: 488`, `args: 70`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 50`, `dead_code: 2`, `unreferenced_by_name: 16`
* *Architecture:* `api: 20`, `import: 26`
* *Defense:* `safety: 23`, `doc: 4`, `test: 35`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingPlan, CudaOutputReadback, CudaResidentDispatch, CudaResidentDispatchStep, DispatchConfig, FxHashSet, HostTransferAllocations, PendingDispatch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/asn1_compiler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1420.22 | **LOC:** 1612 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.009%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse_type` **(Many-Argument Workhorses)** (Impact: 174.5)
    * *Intent:* /* * Parse one type definition statement */
  * `render_element` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* /* * Render an element. */
  * `tokenise` **(Many-Argument Workhorses)** (Impact: 79.5)
    * *Intent:* /* * Tokenise an ASN.1 grammar */
  * `main` **(Compute Cores)** (Impact: 43.5)
    * *Intent:* /* * */
  * `dump_element` **(Compute Cores)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Rce:* 12 instances
* *Amplified Cascading Flux:* 259 instances
* *High Risk Execution (weighted view):* 35
* *Memory Alloc (weighted view):* 6
* *Sec Tainted Injection (weighted view):* 12
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 171`, `args: 118`, `func_start: 17`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 41`, `state_mutation: 268`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 9`, `import: 11`
* *Defense:* `safety: 7`, `immutability_locks: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, fcntl.h, asn1_ber_bytecode.h, stdarg.h, stdbool.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/egraph_kernel_plan.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1311.88 | **LOC:** 2930 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (6.207%), Tech Debt (13.9224%)
**Top Internal Functions/Classes:**
  * `run_egraph_structural_canonicalization_fixed_point_with_readback` **(Many-Argument Workhorses)** (Impact: 101.6)
    * *Intent:* /// Iterate CUDA-resident structural canonicalization with explicit control /// over the final host ...
  * `plan_cuda_egraph_signature_buckets_from_column` **(Many-Argument Workhorses)** (Impact: 74.9)
  * `plan_cuda_egraph_union_compaction` **(Many-Argument Workhorses)** (Impact: 66.7)
    * *Intent:* /// Generate the concrete PTX kernel that compares packed e-graph rows inside /// one signature buck...
  * `run_egraph_canonical_rewrite_kernel_inner` **(Many-Argument Workhorses)** (Impact: 59.2)
  * `run_egraph_structural_equivalence_kernel_inner` **(Many-Argument Workhorses)** (Impact: 53.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 459`, `args: 141`, `func_start: 64`, `class_start: 30`
* *Risk/State:* `state_mutation: 49`, `dead_code: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 199`, `import: 15`
* *Defense:* `safety: 54`, `doc: 434`, `test: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CudaEGraphDeviceKernelView, CudaResidentBuffer, CudaStorageReserveFailure, EGraphSignatureRefreshKernelArgs, GpuEGraphDeviceImage, args::EGraphCanonicalRewriteKernelArgs, crate::CudaResidentEGraphDeviceImage, crate::backend::CudaBackend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/symbol.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1276.64 | **LOC:** 1349 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.5996%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `sym_calc_value` **(Compute Cores)** (Impact: 58.6)
  * `sym_string_valid` **(Compute Cores)** (Impact: 48.9)
  * `sym_set_string_value` **(Compute Cores)** (Impact: 40.5)
  * `sym_get_string_default` **(Compute Cores)** (Impact: 38.9)
    * *Intent:* /* * Find the default value associated to a symbol. * For tristate symbol handle the modules=n case ...
  * `sym_string_within_range` **(Compute Cores)** (Impact: 38.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 194 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 336`, `args: 41`, `func_start: 41`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 197`, `dead_code: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 28`, `import: 9`
* *Defense:* `doc: 3`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, hash.h, internal.h, lkc.h, regex.h, stdlib.h, string.h, types.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/expr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1247.5 | **LOC:** 1181 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.7374%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expr_join_and` **(Compute Cores)** (Impact: 148.4)
  * `expr_join_or` **(Compute Cores)** (Impact: 89.8)
    * *Intent:* /* * e1 || e2 -> ? */
  * `expr_transform` **(Compute Cores)** (Impact: 73.8)
    * *Intent:* * !(A<=B) -> A>B * !(A>=B) -> A<B * !(A<B) -> A>=B * !(A>B) -> A<=B * !(A || B) -> !A && !B * !(A &&...
  * `expr_print` **(Many-Argument Workhorses)** (Impact: 73.5)
  * `expr_trans_compare` **(Compute Cores)** (Impact: 65.2)
    * *Intent:* /* * Inserts explicit comparisons of type 'type' to symbol 'sym' into the * expression 'e'. * * Exam...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 432`, `structural_boundaries: 282`, `args: 60`, `func_start: 31`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 119`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 3`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, errno.h, hash.h, internal.h, lkc.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/unifdef.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 1160.0 | **LOC:** 1226 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.61%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `skipcomment` **(Compute Cores)** (Impact: 91.7)
    * *Intent:* /* * Skip over comments, strings, and character literals and stop at the * next character position t...
  * `main` **(Compute Cores)** (Impact: 87.5)
    * *Intent:* #define endsym(c) (!isalnum((unsigned char)c) && c != '_') /* * The main program. */
  * `eval_unary` **(Many-Argument Workhorses)** (Impact: 70.2)
    * *Intent:* /* * Function for evaluating the innermost parts of expressions, * viz. !expr (expr) number defined(...
  * `parseline` **(Compute Cores)** (Impact: 54.1)
    * *Intent:* /* * Parse a line and determine its type. We keep the preprocessor line * parser state between calls...
  * `addsym` **(Many-Argument Workhorses)** (Impact: 23.6)
    * *Intent:* /* * Add a symbol to the symbol table. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 195 instances
* *High Risk Execution (weighted view):* 8
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 587
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 253`, `args: 98`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 9`, `state_mutation: 197`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 11`
* *Defense:* `safety: 6`, `immutability_locks: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, err.h, errno.h, stdarg.h, stdbool.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/nconf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 967.14 | **LOC:** 1558 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.046%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `selected_conf` **(Compute Cores)** (Impact: 120.4)
  * `build_conf` **(Compute Cores)** (Impact: 83.5)
  * `conf_choice` **(Compute Cores)** (Impact: 71.0)
  * `do_match` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* /* Return 0 means I have handled the key. In such a case, ans should hold the * item to center, or -...
  * `main` **(Compute Cores)** (Impact: 26.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 130 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 411
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 252`, `args: 68`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `state_mutation: 151`, `dead_code: 6`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, list.h, lkc.h, mnconf-common.h, nconf.h, stdlib.h, string.h, strings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/release_benchmarks.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 943.86 | **LOC:** 2236 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.5398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `inspect_backend_suite_artifact` **(Many-Argument Workhorses)** (Impact: 105.4)
  * `inspect_optimization_benchmark_artifact` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `run` **(Compute Cores)** (Impact: 58.8)
  * `write_cpu_100x_proof` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `benchmark_artifact_is_reusable` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 93 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 301
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 243`, `structural_boundaries: 362`, `args: 143`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 19`, `state_mutation: 115`
* *Architecture:* `io: 10`, `api: 1`, `import: 6`
* *Defense:* `safety: 49`, `doc: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` PathBuf, Serialize, Value, serde::Deserialize, serde_json::json, std::fs, std::io::Read, std::path::Path...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-primitives/src/graph/exploded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 909.18 | **LOC:** 2317 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.2735%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `try_build_cpu_reference_into` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* /// Fallible CPU-reference CSR builder into caller-owned output and scratch. /// /// Validation happ...
  * `ifds_program_cache_key_from_program` **(Defensive Guards)** (Impact: 52.1)
    * *Intent:* /// Recover the exploded IFDS program cache key baked into a generated CSR /// builder [`Program`]. ...
  * `build_ifds_csr_program` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /// Build a GPU Program that emits the exploded-supergraph CSR. /// /// This is a deterministic sing...
  * `validate_ifds_csr_inputs` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* /// Validate the full IFDS CSR dispatch contract from caller-owned rule slices. /// /// Returns the ...
  * `validate_ifds_csr_layout` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /// Validate dimensions/counts and return the exact dispatch buffer layout.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 43 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 283`, `args: 92`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 63`
* *Architecture:* `api: 137`, `import: 9`
* *Defense:* `safety: 24`, `doc: 254`, `test: 116`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.237
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000242
  * `Imports (Out-Degree: 0):` BufferDecl, DataType, Expr, Node, Program, std::sync::Arc, super::*, vyre_foundation::ir::BinOp...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xtask/src/c_parser_bench.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 899.78 | **LOC:** 1933 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9725%), Tech Debt (12.9716%)
**Top Internal Functions/Classes:**
  * `is_release_evidence_valid` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `run_inner` **(Compute Cores)** (Impact: 84.0)
  * `parse_args` **(Compute Cores)** (Impact: 65.3)
  * `inspect_vyrecob2_sections` **(Defensive Guards)** (Impact: 42.4)
  * `run_vyre_parser_file_range` **(Many-Argument Workhorses)** (Impact: 38.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 278`, `args: 104`, `func_start: 54`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 74`, `unreferenced_by_name: 11`
* *Architecture:* `io: 1`, `api: 1`, `import: 13`
* *Defense:* `safety: 26`, `doc: 1`, `test: 33`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` BenchOrder, CParseSummary, CliMacroAction, Ordering, PathBuf, SourceFile, SyntaxParseSummary, VYRECOB2_MAGIC...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/sorttable.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 898.68 | **LOC:** 1415 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.6131%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `do_sort` **(Many-Argument Workhorses)** (Impact: 87.6)
    * *Intent:* #endif
  * `do_file` **(Compute Cores)** (Impact: 66.4)
  * `fill_relocs` **(Many-Argument Workhorses)** (Impact: 27.3)
    * *Intent:* /* Fill the array with the content of the relocs */
  * `sort_mcount_loc` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* /* Sort the addresses stored between __start_mcount_loc to __stop_mcount_loc in vmlinux */
  * `replace_relocs` **(Many-Argument Workhorses)** (Impact: 22.0)
    * *Intent:* /* Put the sorted vals back into the relocation elements */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 143 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 432
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 230`, `args: 80`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 146`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 4`, `import: 16`
* *Defense:* `safety: 9`, `immutability_locks: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` orc_types.h, elf.h, errno.h, fcntl.h, getopt.h, pthread.h, stdbool.h, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/confdata.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 875.3 | **LOC:** 1144 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.4527%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `conf_read_simple` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `conf_set_sym_val` **(Many-Argument Workhorses)** (Impact: 52.3)
  * `conf_write` **(Compute Cores)** (Impact: 46.7)
  * `print_symbol_for_c` **(Compute Cores)** (Impact: 28.0)
  * `conf_touch_deps` **(Compute Cores)** (Impact: 27.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 128 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 208`, `args: 43`, `func_start: 35`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 135`, `dead_code: 3`, `unreferenced_by_name: 8`
* *Architecture:* `io: 14`, `api: 14`, `import: 17`
* *Defense:* `safety: 15`, `immutability_locks: 43`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, errno.h, fcntl.h, internal.h, limits.h, lkc.h, stdarg.h, stdbool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `conform/vyre-conform-runner/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 868.9 | **LOC:** 1952 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (19.4052%), Tech Debt (7.9834%)
**Top Internal Functions/Classes:**
  * `merge_certificates` **(Compute Cores)** (Impact: 62.1)
  * `read_and_verify_shard` **(Compute Cores)** (Impact: 53.0)
  * `compare_backend_against_reference` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `prove` **(Compute Cores)** (Impact: 32.3)
  * `prepare_reference_cases` **(Many-Argument Workhorses)** (Impact: 29.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 50 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 289`, `structural_boundaries: 401`, `args: 147`, `func_start: 47`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 62`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `concurrency: 8`, `import: 22`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, BufferParity, Signer, SigningKey, Verifier, VerifyingKey, ed25519_dalek::Signature, rand_core::RngCore...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-lower/src/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 837.68 | **LOC:** 1928 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1894%), Tech Debt (25.6963%)
**Top Internal Functions/Classes:**
  * `lower_node` **(Many-Argument Workhorses)** (Impact: 131.1)
  * `lower_expr` **(Many-Argument Workhorses)** (Impact: 80.6)
  * `walk` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `lower_child_node` **(Many-Argument Workhorses)** (Impact: 29.3)
  * `collect_carrier_names` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /// 1. Appears on the left of an `Assign` somewhere inside the body /// (including nested If/Block/R...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 276`, `args: 107`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 4`, `state_mutation: 83`, `dead_code: 1`, `duplicate_logic: 3`, `unreferenced_by_name: 16`
* *Architecture:* `api: 5`, `import: 24`
* *Defense:* `safety: 17`, `doc: 70`, `test: 62`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BindingSlot, BindingVisibility, BufferAccess, BufferDecl, DataType, Dispatch, Expr, FxHashSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-bench/src/cases/release_workloads.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 836.3 | **LOC:** 2595 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.1777%), Tech Debt (19.3782%)
**Top Internal Functions/Classes:**
  * `release_benchmark_csr_forward_baseline` **(Many-Argument Workhorses)** (Impact: 34.3)
  * `callgraph_witness_digest` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `run` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `run` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `run_string_bitmap_scatter` **(Many-Argument Workhorses)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 254`, `args: 127`, `func_start: 110`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 73`, `duplicate_logic: 8`, `unreferenced_by_name: 6`
* *Architecture:* `api: 20`, `import: 4`
* *Defense:* `safety: 2`, `doc: 21`, `test: 4`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BenchContext, BenchError, BenchId, BenchLayer, BenchMetadata, BenchRequirements, BenchRun, BufferDecl...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/conf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 768.68 | **LOC:** 870 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (87.5405%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 155.9)
  * `conf_set_all_new_symbols` **(Compute Cores)** (Impact: 53.2)
  * `conf_sym` **(Compute Cores)** (Impact: 48.6)
  * `conf_choice` **(Compute Cores)** (Impact: 46.7)
  * `conf` **(Compute Cores)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 100 instances
* *State Mutation (weighted view):* 309
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 143`, `args: 21`, `func_start: 15`, `class_start: 19`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 109`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, errno.h, getopt.h, internal.h, limits.h, lkc.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/gconf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 757.0 | **LOC:** 1336 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (83.6513%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `set_node` **(Many-Argument Workhorses)** (Impact: 62.9)
  * `on_treeview2_button_press_event` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /* User click: update choice (full) or goes down (single) */
  * `change_sym_value` **(Compute Cores)** (Impact: 29.3)
    * *Intent:* /* Change the value of a symbol and update the tree */
  * `main` **(Compute Cores)** (Impact: 26.8)
    * *Intent:* /* Main */
  * `on_treeview2_key_press_event` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /* Key pressed: update choice */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 85 instances
* *State Mutation (weighted view):* 315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 126`, `args: 126`, `func_start: 54`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 145`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gtk.h, images.h, lkc.h, stdio.h, stdlib.h, string.h, strings.h, time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 749.64 | **LOC:** 865 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.7306%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_menu_finalize` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `sym_check_prop` **(Compute Cores)** (Impact: 51.1)
  * `get_prompt_str` **(C Struct Operations)** (Impact: 32.9)
  * `menu_dump` **(Compute Cores)** (Impact: 28.5)
    * *Intent:* /** * menu_dump - dump all menu entries in a tree-like format */
  * `get_symbol_str` **(C Struct Operations)** (Impact: 22.6)
    * *Intent:* /* * head is optional and may be NULL */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 183`, `args: 35`, `func_start: 33`, `class_start: 40`
* *Risk/State:* `state_mutation: 130`, `unreferenced_by_name: 19`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `doc: 4`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ctype.h, internal.h, list.h, lkc.h, stdarg.h, stdlib.h, string.h, xalloc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/lego_audit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 730.86 | **LOC:** 1352 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.2783%), Tech Debt (8.9072%)
**Top Internal Functions/Classes:**
  * `check_1_no_reinvention` **(Compute Cores)** (Impact: 42.9)
    * *Intent:* /// Check 1: flag pairs of ops with near-identical fingerprints whose /// Region chains don't indica...
  * `check_10_operand_shape_duplicate` **(Compute Cores)** (Impact: 35.3)
  * `check_4_cross_dialect_reachthrough` **(Compute Cores)** (Impact: 34.4)
    * *Intent:* /// path reaching into `vyre_libs::<other_dialect>::...` or /// `crate::<other_dialect>::...` across...
  * `walk` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `check_9_name_stem_collision` **(Compute Cores)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 170`, `args: 55`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 118`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `io: 5`, `api: 13`, `import: 6`
* *Defense:* `safety: 13`, `doc: 87`, `test: 7`, `sync_locks: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BTreeSet, HashMap, Node, Program, Read, std::collections::BTreeMap, std::io::self, std::process...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/nconf.gui.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 668.48 | **LOC:** 653 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.7995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `dialog_inputbox` **(Many-Argument Workhorses)** (Impact: 120.3)
  * `show_scroll_win_ext` **(Many-Argument Workhorses)** (Impact: 111.4)
    * *Intent:* /* layman's scrollable window... */
  * `btn_dialog` **(Many-Argument Workhorses)** (Impact: 64.3)
    * *Intent:* /* get the message, and buttons. * each button must be a char* * return the selected button * * this...
  * `get_line` **(Compute Cores)** (Impact: 9.3)
  * `get_line_no` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 53`, `args: 24`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 118`, `unreferenced_by_name: 4`
* *Architecture:* `api: 12`, `import: 3`
* *Defense:* `safety: 4`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` lkc.h, nconf.h, xalloc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/source_similar.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 664.28 | **LOC:** 1168 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (26.2959%), Tech Debt (21.3116%)
**Top Internal Functions/Classes:**
  * `normalize_tokens` **(Compute Cores)** (Impact: 60.8)
  * `has_control_flow_keyword` **(Compute Cores)** (Impact: 28.9)
  * `collect_rust_files_recursive` **(Many-Argument Workhorses)** (Impact: 28.4)
  * `parse_args` **(Compute Cores)** (Impact: 23.7)
  * `source_shape` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 57 instances
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 227`, `args: 130`, `func_start: 45`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 8`, `state_mutation: 61`, `unreferenced_by_name: 13`
* *Architecture:* `io: 1`, `api: 44`, `concurrency: 2`, `import: 12`
* *Defense:* `safety: 4`, `doc: 7`, `test: 46`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` HashSet, PathBuf, alpha::alpha, beta::beta, delta::delta, gamma::gamma, std::collections::HashMap, std::fs...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/segments.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 656.62 | **LOC:** 780 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.3331%), Tech Debt (19.4602%)
**Top Internal Functions/Classes:**
  * `function_argument_prescan_macros` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `macro_use_statement_ranges` **(Compute Cores)** (Impact: 55.9)
  * `has_live_macro_for_segment_excluding` **(Defensive Guards)** (Impact: 49.0)
  * `classified_segment` **(Defensive Guards)** (Impact: 46.7)
  * `live_macro_defs_for_segment` **(Defensive Guards)** (Impact: 42.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 166`, `args: 71`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 71`, `unreferenced_by_name: 8`
* *Architecture:* `api: 9`, `import: 19`
* *Defense:* `safety: 28`, `test: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ClassifiedTokens, FxHashSet, MacroDef, TOK_LPAREN, TOK_RBRACE, TOK_RPAREN, TOK_SEMICOLON, crate::parsing::c::lex::tokens::
    TOK_IDENTIFIER...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/gendwarfksyms/dwarf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 648.66 | **LOC:** 1184 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.2095%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolve_fqns` **(Many-Argument Workhorses)** (Impact: 35.5)
  * `process_exported_symbols` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `___process_structure_type` **(Compute Cores)** (Impact: 25.1)
  * `process_type` **(Many-Argument Workhorses)** (Impact: 20.5)
  * `check_union_member_kabi_status` **(Many-Argument Workhorses)** (Impact: 18.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 64 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 224`, `args: 65`, `func_start: 53`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 71`, `unreferenced_by_name: 11`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 3`, `immutability_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.234
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` assert.h, gendwarfksyms.h, inttypes.h, stdarg.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `vyre-lints/src/lib.rs` -> Churn: **69.9%** | Cog Load: 29.4801% | Debt: 99.9991%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `vyre-driver-cuda/src/backend/resident_dispatch.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1487.46
- `vyre-driver-cuda/src/egraph_kernel_plan.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1311.88
- `vyre-primitives/src/graph/exploded.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 909.18
- `conform/vyre-conform-runner/src/main.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 868.9
- `vyre-bench/src/cases/release_workloads.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 836.3

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `scripts/lib/cargo_runner.sh` -> **Severity: 0.523** (Embedded: 0.0073 * Error Risk: 71.9676%)
- `vyre-driver/src/transfer_accounting.rs` -> **Severity: 0.172** (Embedded: 0.0036 * Error Risk: 47.2413%)
- `vyre-runtime/src/megakernel/protocol/opcode.rs` -> **Severity: 0.077** (Embedded: 0.0017 * Error Risk: 45.3468%)
- `vyre-driver-wgpu/tests/c11_build_vast_nodes.rs` -> **Severity: 0.058** (Embedded: 0.0012 * Error Risk: 48.236%)
- `vyre-foundation/src/serial/wire/framing/put_u8.rs` -> **Severity: 0.055** (Embedded: 0.0012 * Error Risk: 45.2996%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `scripts/lib/cargo_runner.sh` -> **Severity: 620.4** (Blast Radius: 6.204 * Doc Risk: 100.0%)
- `vyre-driver/src/transfer_accounting.rs` -> **Severity: 90.652** (Blast Radius: 2.921 * Doc Risk: 31.0345%)
- `vyre-frontend-c/tests/parse_syntax_bytes.rs` -> **Severity: 73.2** (Blast Radius: 0.732 * Doc Risk: 100.0%)
- `vyre-libs/src/parsing/c/preprocess/expr_parser/precedence.rs` -> **Severity: 63.2** (Blast Radius: 0.632 * Doc Risk: 100.0%)
- `vyre-driver-wgpu/tests/c11_build_vast_nodes.rs` -> **Severity: 61.45** (Blast Radius: 1.229 * Doc Risk: 50.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
