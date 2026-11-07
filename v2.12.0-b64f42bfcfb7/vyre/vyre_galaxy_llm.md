# ARCHITECTURAL_BRIEF: vyre
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/santhsecurity/vyre` |
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
- **Scope:** 4171 analyzed artifact(s), 756053 LOC.
- **Load-bearing artifact:** `vyre-foundation/src/lib.rs` -- 1319 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `vyre-driver-cuda/src/lib.rs` -- pulls in 230 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `xtask/src/release_completion_audit.rs` at magnitude 3542.62 (structural weight, not risk).
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
| Total Artifacts | 4674 |
| Analyzed Artifacts (Scanned) | 4171 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 503 |
| Total LOC | 756053 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 89.2% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6959 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1608 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2639 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 217 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 3685 | 722346 | 88.3% |
| MARKDOWN | 224 | 0 | 5.4% |
| SHELL | 118 | 5860 | 2.8% |
| C | 58 | 20369 | 1.4% |
| YAML | 33 | 1471 | 0.8% |
| JSON | 24 | 4729 | 0.6% |
| PLAINTEXT | 19 | 10 | 0.5% |
| PYTHON | 6 | 753 | 0.1% |
| GO | 4 | 515 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 4171 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 19%, Data / Markup / Trivial 14%, Large Core Modules (3) 14%, State Mutators Files 14%, Many-Argument Workhorses Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3928 | 94.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 242 | 5.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 503*

**Composition by Extension & Reason:**
- `.md`: 183x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2191 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3983 LOC)
- `.json`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4672 LOC)
- `.toml`: 41x Unsupported Format (.toml), 19x Excluded (Unsupported Extension: '.toml'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rs`: 30x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stderr`: 28x Excluded (Unsupported Extension: '.stderr')
- `no_extension`: 18x Excluded (Unsupported Extension: '.proptest-regressions'), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wgsl`: 10x Unsupported Format (.wgsl)
- `.lock`: 7x Excluded (Unsupported Extension: '.lock'), 1x Unsupported Format (.lock)
- `.tmpl`: 3x Excluded (Unsupported Extension: '.tmpl')
- `.cff`: 1x Excluded (Unsupported Extension: '.cff')
- `.tsv`: 1x Excluded (Static Asset Blob without Intent: 1835 LOC)
- `.svg`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Zero-Density Threshold (LOC: 233, Signals: 0)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.7 | 3.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.0 | 34.6 | 47.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.1 | 11.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 20.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 90.4 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 100.0 | 41.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.8 | 64.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 12161 | 1676 | 9 | `vyre-driver-cuda/tests/int4_quantized_gpu_parity.rs` |
| cleanup | 229 | 86 | 0 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/confdata.c` |
| guards | 16892 | 2367 | 10 | `xtask/src/vyre_weir_release_gate.rs` |
| danger | 14167 | 1821 | 10 | `vyre-driver-cuda/tests/resident_dispatch_contracts.rs` |
| concurrency | 2608 | 604 | 1 | `vyre-libs/tests/fixtures/go/pipeline.go` |
| connectivity | 28957 | 2601 | 20 | `vyre-driver-cuda/src/egraph_kernel_plan.rs` |
| io | 3328 | 381 | 0 | `scripts/check_ownership_boundaries.sh` |
| crypto | 1 | 1 | 0 | `benches/competition/scripts/check_corpora.py` |
| ipc | 90 | 58 | 0 | `tools/divergence-gate.py` |
| time | 218 | 137 | 0 | `conform/vyre-conform-runner/src/main.rs` |
| serialization | 214 | 83 | 0 | `vyre-lower/src/descriptor.rs` |
| regex | 299 | 88 | 0 | `scripts/check_capability_negotiation.sh` |
| events | 413 | 133 | 0 | `vyre-driver-cuda/src/backend/resident_dispatch.rs` |
| tests | 47211 | 2370 | 32 | `vyre-driver-cuda/tests/egraph_device_image_upload.rs` |
| docs | 61053 | 2955 | 44 | `vyre-driver/src/backend/vyre_backend.rs` |
| debt | 3212 | 499 | 1 | `vyre-frontend-c/tests/r2_corpus_measurement.rs` |
| mutation | 103063 | 3305 | 63 | `xtask/src/vyre_weir_release_gate.rs` |
| dead_code | 8366 | 1379 | 7 | `vyre-libs/tests/gpu_if_expression_roundtrip.rs` |
| credential | 20 | 8 | 0 | `vyre-libs/src/scan/test_fixtures.rs` |
| threat | 23 | 11 | 0 | `vyre-libs/src/decode/base64.rs` |
| ml_ai | 4514 | 485 | 1 | `vyre-self-substrate/src/math/scientific_kernel_pipeline.rs` |
| ui | 41 | 9 | 0 | `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/gconf.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.25**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/check_ownership_boundaries.sh` (Hits: 170)
- `scripts/check_no_string_wgsl.sh` (Hits: 73)
- `scripts/check_repo_hygiene.sh` (Hits: 62)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lib.rs** (`vyre-foundation/src/lib.rs`) — 1319 inbound connections
2. **value.rs** (`vyre-reference/src/value.rs`) — 226 inbound connections
3. **mod.rs** (`vyre-macros/tests/support/mod.rs`) — 215 inbound connections
4. **tokens.rs** (`vyre-libs/src/parsing/c/lex/tokens.rs`) — 185 inbound connections
5. **descriptor.rs** (`vyre-lower/src/descriptor.rs`) — 147 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`vyre-driver-cuda/src/lib.rs`) — 230 outbound dependencies
2. **lib.rs** (`vyre-driver/src/lib.rs`) — 197 outbound dependencies
3. **mod.rs** (`vyre-runtime/src/megakernel/mod.rs`) — 190 outbound dependencies
4. **mod.rs** (`vyre-libs/src/parsing/c/parse/vast/mod.rs`) — 161 outbound dependencies
5. **pipeline.rs** (`vyre-frontend-c/src/pipeline.rs`) — 160 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run_semantic_requirement_checks` **(Many-Argument Workhorses)** (@ `xtask/src/vyre_weir_release_gate.rs`) -> Impact: **1004.0** | LOC: 3360
- `fill_upload_resident_many_repeated_sequence_read_ranges_borrowed_into` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **377.9** | LOC: 475
- `simplify_binop` **(Many-Argument Workhorses)** (@ `vyre-foundation/src/optimizer/passes/algebraic/const_fold/binop_identities.rs`) -> Impact: **368.9** | LOC: 617
  * *Intent:* /// Algebraic identity simplifications for binary operators. /// These rewrites are always valid and don't require literal operands - /// they fire wh...
- `reference_typed_kind` **(Many-Argument Workhorses)** (@ `vyre-libs/src/parsing/c/parse/vast/ref_typedef/typed_kind.rs`) -> Impact: **348.4** | LOC: 351
- `flush_active_macro_segment_inner` **(Many-Argument Workhorses)** (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/macro_expansion/flush.rs`) -> Impact: **343.0** | LOC: 574
- `emit_op` **(Many-Argument Workhorses)** (@ `vyre-emit-ptx/src/emitter.rs`) -> Impact: **321.5** | LOC: 470
- `dispatch_resident_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/resident_dispatch.rs`) -> Impact: **310.1** | LOC: 432
- `dispatch_borrowed_async_with_ptx_concrete` **(Many-Argument Workhorses)** (@ `vyre-driver-cuda/src/backend/host_dispatch.rs`) -> Impact: **254.5** | LOC: 339
- `record_macro_token_provenance` **(Many-Argument Workhorses)** (@ `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/token_provenance/macro_record.rs`) -> Impact: **246.8** | LOC: 256
  * *Intent:* /// Records provenance for a segment after GPU macro materialization.
- `dialog_menu` **(Many-Argument Workhorses)** (@ `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/lxdialog/menubox.c`) -> Impact: **216.2** | LOC: 254
  * *Intent:* /* * Display a menu for choosing among a number of options */

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `xtask/src` | 56 | 18816.98 | 14.82% | 2.8% |
| `vyre-primitives/src/graph` | 36 | 8981.28 | 6.45% | 1.73% |
| `vyre-driver/src` | 58 | 8818.26 | 6.35% | 1.11% |
| `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig` | 13 | 8295.38 | 73.53% | 0.0% |
| `vyre-driver-cuda/src/backend` | 25 | 6296.76 | 8.08% | 3.28% |
| `vyre-driver-cuda/src` | 33 | 6059.6 | 4.37% | 5.56% |
| `vyre-primitives/src/math` | 43 | 5637.88 | 8.25% | 0.0% |
| `vyre-frontend-c/tests/corpus/r2_kernel_scripts` | 11 | 5362.5 | 25.8% | 0.0% |
| `vyre-driver-wgpu/tests` | 166 | 5160.4 | 2.08% | 0.0% |
| `vyre-driver-wgpu/tests/__split` | 137 | 4311.68 | 2.35% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `vyre-emit-naga/src/program/mod_tests.rs` -> **100.0%** Exposure
- `vyre-self-substrate/src/graph/adaptive_traverse/resident.rs` -> **100.0%** Exposure
- `vyre-lints/src/lib.rs` -> **99.9991%** Exposure
- `.github/workflows/conform.yml` -> **99.9984%** Exposure
- `vyre-spec/src/extension.rs` -> **99.9885%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/check_no_raw_unwrap.py` -> **100.0%** Exposure
- `scripts/check_no_under_reserve.py` -> **100.0%** Exposure
- `scripts/check_self_consumer_coverage.py` -> **100.0%** Exposure
- `tools/divergence-gate.py` -> **100.0%** Exposure
- `vyre-driver-wgpu/tests/common/c_fixture.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `vyre-libs/tests/gpu_if_expression_roundtrip.rs` -> **47** Orphaned Functions | **0** Duplicates
- `vyre-primitives/tests/__split/adversarial_graph_reachability_fixpoint_chunk1.rs` -> **45** Orphaned Functions | **0** Duplicates
- `vyre-lower/src/rewrites/descriptor_const_fold/mod.rs` -> **42** Orphaned Functions | **0** Duplicates
- `vyre-primitives/tests/__split/adversarial_boolean_packing_four_russians_readiness_chunk1.rs` -> **41** Orphaned Functions | **0** Duplicates
- `vyre-libs/tests/gpu_char_constant_scan_roundtrip.rs` -> **39** Orphaned Functions | **0** Duplicates

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
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `28851` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `xtask/src/release_completion_audit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.064)
- **Top Global Matches:** file_cluster_6: 7.064, file_cluster_8: 11.357, file_cluster_4: 14.219
- **Magnitude:** 3542.62 | **LOC:** 6411 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 0.08; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Complexity Load (formerly Cognitive Load) (29.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect_json_evidence` **(Many-Argument Workhorses)** (Impact: 153.7)
  * `inspect_backend_suite_semantics` **(Many-Argument Workhorses)** (Impact: 95.2)
  * `inspect_pass_family_benchmark_manifest_semantics` **(Many-Argument Workhorses)** (Impact: 91.8)
  * `inspect_release_workload_matrix_semantics` **(Many-Argument Workhorses)** (Impact: 88.4)
  * `inspect_weir_matrix_semantics` **(Many-Argument Workhorses)** (Impact: 79.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Amplified Cascading Flux:* 394 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 1254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 864`, `structural_boundaries: 497`, `args: 334`, `func_start: 87`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 466`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 304`, `doc: 1`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000432
  * `Imports (Out-Degree: 0):` serde::Deserialize, serde::Serialize, std::collections::BTreeSet, std::fs, std::io, std::io::Read, std::path::Path, std::path::PathBuf
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `xtask/src/vyre_weir_release_gate.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.251)
- **Top Global Matches:** file_cluster_6: 7.251, file_cluster_8: 11.53, file_cluster_4: 14.236
- **Magnitude:** 3450.9 | **LOC:** 6940 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.08; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.2%), Complexity Load (formerly Cognitive Load) (36.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run_semantic_requirement_checks` **(Many-Argument Workhorses)** (Impact: 1004.0)
  * `check_backend_suite_report` **(Many-Argument Workhorses)** (Impact: 147.2)
  * `check_workload_matrix_artifact_coverage` **(Many-Argument Workhorses)** (Impact: 95.5)
  * `check_parser_contract_evidence` **(Many-Argument Workhorses)** (Impact: 70.7)
  * `check_single_benchmark_report` **(Many-Argument Workhorses)** (Impact: 61.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 325 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 1099
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 861`, `structural_boundaries: 554`, `args: 280`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 449`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 3`, `import: 7`
* *Defense:* `safety: 340`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000432
  * `Imports (Out-Degree: 0):` serde::Deserialize, std::collections::BTreeSet, std::fs, std::io, std::io::Read, std::path::Path, std::path::PathBuf
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-driver-cuda/src/backend/resident_dispatch.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.142)
- **Top Global Matches:** file_cluster_4: 6.142, file_cluster_6: 9.3, file_cluster_16: 12.545
- **Magnitude:** 1470.26 | **LOC:** 2201 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **43**; blast radius 0.079; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (53.1%), Guard Balance (formerly Safety Score) (51.8%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fill_upload_resident_many_repeated_sequence_read_ranges_borrowed_into` **(Many-Argument Workhorses)** (Impact: 377.9)
  * `dispatch_resident_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (Impact: 310.1)
  * `dispatch_resident_batch_async_concrete_with_ptx_key` **(Many-Argument Workhorses)** (Impact: 207.4)
  * `dispatch_resident_via_borrowed_into` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `dispatch_resident_timed` **(Many-Argument Workhorses)** (Impact: 34.0)
    * *Intent:* /// Dispatch with CUDA-resident buffers and return ordered output readbacks.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 132
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 384`, `structural_boundaries: 488`, `args: 70`, `func_start: 40`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 50`
* *Architecture:* `api: 29`, `import: 26`
* *Defense:* `safety: 23`, `doc: 4`, `test: 35`, `immutability_locks: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.004434
  * `Imports (Out-Degree: 18):` crate::backend::resident::CudaResidentBuffer, rustc_hash::FxHashMap, rustc_hash::FxHashSet, self::borrow_resident_sequence_output_slots, self::prepare_resident_sequence_fills, self::stage_resident_fill_payload, smallvec::SmallVec, std::ffi::c_void...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/asn1_compiler.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.467)
- **Top Global Matches:** file_cluster_8: 6.467, file_cluster_6: 13.738, file_cluster_4: 22.349
- **Magnitude:** 1414.12 | **LOC:** 1612 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (82.3%), Complexity Load (formerly Cognitive Load) (38.8%), Dead Code Surface (formerly Dead Code) (5.9%), Connectivity (formerly Api Exposure) (1.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_type` **(Many-Argument Workhorses)** (Impact: 174.5)
    * *Intent:* /* * Parse one type definition statement */
  * `render_element` **(Many-Argument Workhorses)** (Impact: 142.7)
    * *Intent:* /* * Render an element. */
  * `tokenise` **(Many-Argument Workhorses)** (Impact: 77.8)
    * *Intent:* /* * Tokenise an ASN.1 grammar */
  * `main` **(Many-Argument Workhorses)** (Impact: 43.5)
    * *Intent:* /* * */
  * `dump_element` **(Stateful Encapsulated Methods)** (Impact: 34.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 259 instances
* *High Risk Execution (weighted view):* 35
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 786
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 171`, `args: 118`, `func_start: 17`, `class_start: 43`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 41`, `state_mutation: 268`, `dead_code: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 9`, `import: 11`
* *Defense:* `safety: 7`, `immutability_locks: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` ctype.h, fcntl.h, asn1_ber_bytecode.h, stdarg.h, stdbool.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-driver-cuda/src/egraph_kernel_plan.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.53)
- **Top Global Matches:** file_cluster_4: 7.53, file_cluster_6: 7.96, file_cluster_15: 14.597
- **Magnitude:** 1308.48 | **LOC:** 2930 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **35**; blast radius 0.454; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.6%), Guard Balance (formerly Safety Score) (48.8%)
- **Documentation Coverage:** 24.5098% of unit weight undocumented
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
* *Structure:* `branch: 333`, `structural_boundaries: 459`, `args: 141`, `func_start: 64`, `class_start: 30`
* *Risk/State:* `state_mutation: 49`, `duplicate_logic: 2`
* *Architecture:* `api: 200`, `import: 15`
* *Defense:* `safety: 54`, `doc: 434`, `test: 1`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.454
  * `Choke Point (Betweenness):` 7.4e-05 | `Ripple Effect (Closeness):` 0.006724
  * `Imports (Out-Degree: 13):` args, ptx, tests, args::EGraphCanonicalRewriteKernelArgs, args::EGraphSignatureRefreshKernelArgs, crate::CudaResidentEGraphDeviceImage, crate::backend::CudaBackend, crate::backend::CudaResidentBuffer...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/symbol.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.372)
- **Top Global Matches:** file_cluster_6: 7.372, file_cluster_8: 10.373, file_cluster_4: 14.975
- **Magnitude:** 1268.04 | **LOC:** 1349 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **9**; blast radius 0.319; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.2%), Guard Balance (formerly Safety Score) (75.1%), Connectivity (formerly Api Exposure) (5.8%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
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
* *Structure:* `branch: 341`, `structural_boundaries: 336`, `args: 41`, `func_start: 41`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 197`, `unreferenced_by_name: 10`
* *Architecture:* `api: 28`, `import: 9`
* *Defense:* `doc: 3`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.319
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001678
  * `Imports (Out-Degree: 3):` ctype.h, hash.h, internal.h, lkc.h, regex.h, stdlib.h, string.h, types.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/expr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.032)
- **Top Global Matches:** file_cluster_8: 6.032, file_cluster_6: 15.978, file_cluster_3: 21.035
- **Magnitude:** 1225.9 | **LOC:** 1181 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (92.0%), Guard Balance (formerly Safety Score) (68.5%), Connectivity (formerly Api Exposure) (29.8%), Dead Code Surface (formerly Dead Code) (5.1%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expr_join_and` **(Compute Cores)** (Impact: 144.9)
  * `expr_join_or` **(Compute Cores)** (Impact: 86.3)
    * *Intent:* /* * e1 || e2 -> ? */
  * `expr_print` **(Many-Argument Workhorses)** (Impact: 69.0)
  * `expr_transform` **(Compute Cores)** (Impact: 68.2)
    * *Intent:* * !(A<=B) -> A>B * !(A>=B) -> A<B * !(A<B) -> A>=B * !(A>B) -> A<=B * !(A || B) -> !A && !B * !(A &&...
  * `expr_trans_compare` **(Compute Cores)** (Impact: 65.2)
    * *Intent:* /* * Inserts explicit comparisons of type 'type' to symbol 'sym' into the * expression 'e'. * * Exam...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 118 instances
* *State Mutation (weighted view):* 355
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 282`, `args: 60`, `func_start: 31`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 119`, `dead_code: 1`
* *Architecture:* `api: 21`, `import: 9`
* *Defense:* `doc: 3`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.251
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001068
  * `Imports (Out-Degree: 2):` ctype.h, errno.h, hash.h, internal.h, lkc.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/unifdef.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.677)
- **Top Global Matches:** file_cluster_4: 6.677, file_cluster_16: 7.873, file_cluster_15: 10.255
- **Magnitude:** 1150.2 | **LOC:** 1226 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **11**; blast radius 0.452; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (78.9%), Complexity Load (formerly Cognitive Load) (47.5%), Connectivity (formerly Api Exposure) (0.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `skipcomment` **(Compute Cores)** (Impact: 91.7)
    * *Intent:* /* * Skip over comments, strings, and character literals and stop at the * next character position t...
  * `main` **(Many-Argument Workhorses)** (Impact: 85.8)
    * *Intent:* #define endsym(c) (!isalnum((unsigned char)c) && c != '_') /* * The main program. */
  * `eval_unary` **(Many-Argument Workhorses)** (Impact: 70.2)
    * *Intent:* /* * Function for evaluating the innermost parts of expressions, * viz. !expr (expr) number defined(...
  * `parseline` **(I/O & Config Routines)** (Impact: 52.1)
    * *Intent:* /* * Parse a line and determine its type. We keep the preprocessor line * parser state between calls...
  * `addsym` **(Stateful Encapsulated Methods)** (Impact: 23.6)
    * *Intent:* /* * Add a symbol to the symbol table. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 194 instances
* *High Risk Execution (weighted view):* 8
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 271`, `structural_boundaries: 253`, `args: 98`, `func_start: 65`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 9`, `state_mutation: 197`, `fragile_debt: 6`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 7`, `import: 11`
* *Defense:* `safety: 6`, `immutability_locks: 59`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001678
  * `Imports (Out-Degree: 0):` ctype.h, err.h, errno.h, stdarg.h, stdbool.h, stdio.h, stdlib.h, string.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/nconf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.722)
- **Top Global Matches:** file_cluster_4: 5.722, file_cluster_6: 8.762, file_cluster_16: 11.39
- **Magnitude:** 931.34 | **LOC:** 1558 | **CtrlFlow:** 19.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.8%), Guard Balance (formerly Safety Score) (63.3%), Connectivity (formerly Api Exposure) (1.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selected_conf` **(Many-Argument Workhorses)** (Impact: 118.7)
  * `build_conf` **(Compute Cores)** (Impact: 83.5)
  * `conf_choice` **(Compute Cores)** (Impact: 68.1)
  * `do_match` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* /* Return 0 means I have handled the key. In such a case, ans should hold the * item to center, or -...
  * `main` **(Many-Argument Workhorses)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 118 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 262`, `structural_boundaries: 252`, `args: 68`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `state_mutation: 151`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `safety: 5`, `immutability_locks: 17`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ctype.h, list.h, lkc.h, mnconf-common.h, nconf.h, stdlib.h, string.h, strings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/release_benchmarks.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.693)
- **Top Global Matches:** file_cluster_4: 7.693, file_cluster_6: 7.828, file_cluster_9: 14.774
- **Magnitude:** 909.76 | **LOC:** 2236 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.08; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inspect_backend_suite_artifact` **(Many-Argument Workhorses)** (Impact: 101.4)
  * `inspect_optimization_benchmark_artifact` **(Many-Argument Workhorses)** (Impact: 70.2)
  * `run` **(Compute Cores)** (Impact: 58.8)
  * `write_cpu_100x_proof` **(Many-Argument Workhorses)** (Impact: 54.9)
  * `benchmark_artifact_is_reusable` **(Many-Argument Workhorses)** (Impact: 37.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Amplified Cascading Flux:* 91 instances
* *High Risk Execution (weighted view):* 9
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 362`, `args: 143`, `func_start: 32`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 19`, `state_mutation: 115`
* *Architecture:* `io: 10`, `api: 1`, `import: 6`
* *Defense:* `safety: 49`, `doc: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000432
  * `Imports (Out-Degree: 0):` serde::Deserialize, serde::Serialize, serde_json::Value, serde_json::json, std::fs, std::io::Read, std::path::Path, std::path::PathBuf...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/sorttable.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.971)
- **Top Global Matches:** file_cluster_4: 8.971, file_cluster_12: 9.728, file_cluster_7: 11.028
- **Magnitude:** 898.68 | **LOC:** 1415 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **16**; blast radius 0.176; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (72.2%), Complexity Load (formerly Cognitive Load) (46.6%), Concurrency Surface (formerly Concurrency) (15.1%), Connectivity (formerly Api Exposure) (0.5%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_sort` **(Many-Argument Workhorses)** (Impact: 87.6)
    * *Intent:* #endif
  * `do_file` **(Many-Argument Workhorses)** (Impact: 66.4)
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
* *Structure:* `branch: 165`, `structural_boundaries: 230`, `args: 80`, `func_start: 49`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 146`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 4`, `import: 16`
* *Defense:* `safety: 9`, `immutability_locks: 55`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00048
  * `Imports (Out-Degree: 3):` orc_types.h, elf.h, errno.h, fcntl.h, getopt.h, pthread.h, stdbool.h, stdio.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `vyre-primitives/src/graph/exploded.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.551)
- **Top Global Matches:** file_cluster_4: 7.551, file_cluster_12: 8.4, file_cluster_15: 8.87
- **Magnitude:** 895.78 | **LOC:** 2317 | **CtrlFlow:** 9.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **13**; blast radius 0.385; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (99.4%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.6%), Mutation Surface (formerly State Flux) (57.7%)
- **Documentation Coverage:** 36.3636% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `try_build_cpu_reference_into` **(Many-Argument Workhorses)** (Impact: 166.7)
    * *Intent:* /// Fallible CPU-reference CSR builder into caller-owned output and scratch. /// /// Validation happ...
  * `build_ifds_csr_program` **(Many-Argument Workhorses)** (Impact: 42.5)
    * *Intent:* /// Build a GPU Program that emits the exploded-supergraph CSR. /// /// This is a deterministic sing...
  * `ifds_program_cache_key_from_program` **(Defensive Guards)** (Impact: 42.2)
    * *Intent:* /// Recover the exploded IFDS program cache key baked into a generated CSR /// builder [`Program`]. ...
  * `validate_ifds_csr_inputs` **(Many-Argument Workhorses)** (Impact: 39.5)
    * *Intent:* /// Validate the full IFDS CSR dispatch contract from caller-owned rule slices. /// /// Returns the ...
  * `validate_ifds_csr_layout` **(Many-Argument Workhorses)** (Impact: 37.4)
    * *Intent:* /// Validate dimensions/counts and return the exact dispatch buffer layout.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 42 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 283`, `args: 92`, `func_start: 47`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 1`, `state_mutation: 63`
* *Architecture:* `api: 137`, `import: 9`
* *Defense:* `safety: 24`, `doc: 254`, `test: 116`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.385
  * `Choke Point (Betweenness):` 7.9e-05 | `Ripple Effect (Closeness):` 0.002517
  * `Imports (Out-Degree: 4):` tests, self::*, std::sync::Arc, vyre_foundation::ir::BinOp, vyre_foundation::ir::BufferAccess, vyre_foundation::ir::BufferDecl, vyre_foundation::ir::DataType, vyre_foundation::ir::Expr...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `xtask/src/c_parser_bench.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.449)
- **Top Global Matches:** file_cluster_4: 6.449, file_cluster_6: 10.534, file_cluster_15: 11.965
- **Magnitude:** 887.78 | **LOC:** 1933 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.6%), Connectivity (formerly Api Exposure) (35.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `is_release_evidence_valid` **(Many-Argument Workhorses)** (Impact: 137.8)
  * `run_inner` **(Compute Cores)** (Impact: 79.7)
  * `parse_args` **(Compute Cores)** (Impact: 61.1)
  * `inspect_vyrecob2_sections` **(Type Conversions)** (Impact: 42.4)
  * `run_vyre_parser_file_range` **(Many-Argument Workhorses)** (Impact: 36.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 278`, `args: 104`, `func_start: 54`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 74`
* *Architecture:* `io: 1`, `api: 12`, `import: 13`
* *Defense:* `safety: 26`, `doc: 1`, `test: 33`, `sync_locks: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.000432
  * `Imports (Out-Degree: 8):` self::BenchOrder, self::SourceFile, self::is_release_evidence_valid, self::parse_args, self::parser_bench_source_text, self::repro_command, serde::Serialize, std::fs...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/confdata.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.0)
- **Top Global Matches:** file_cluster_4: 6.0, file_cluster_6: 7.87, file_cluster_16: 12.974
- **Magnitude:** 870.8 | **LOC:** 1144 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **17**; blast radius 0.219; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.3%), Guard Balance (formerly Safety Score) (70.1%), Connectivity (formerly Api Exposure) (2.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `conf_read_simple` **(Many-Argument Workhorses)** (Impact: 72.5)
  * `conf_set_sym_val` **(Many-Argument Workhorses)** (Impact: 47.8)
  * `conf_write` **(Compute Cores)** (Impact: 46.7)
  * `print_symbol_for_c` **(Stateful Encapsulated Methods)** (Impact: 28.0)
  * `conf_touch_deps` **(I/O & Config Routines)** (Impact: 27.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 128 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 391
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 208`, `args: 43`, `func_start: 35`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 135`, `unreferenced_by_name: 8`
* *Architecture:* `io: 14`, `api: 14`, `import: 17`
* *Defense:* `safety: 15`, `immutability_locks: 43`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001305
  * `Imports (Out-Degree: 4):` ctype.h, errno.h, fcntl.h, internal.h, limits.h, lkc.h, stdarg.h, stdbool.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `conform/vyre-conform-runner/src/main.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.91)
- **Top Global Matches:** file_cluster_4: 6.91, file_cluster_6: 11.192, file_cluster_0: 11.855
- **Magnitude:** 835.3 | **LOC:** 1952 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (75.9%), Guard Balance (formerly Safety Score) (51.7%)
- **Documentation Coverage:** 97.8723% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `merge_certificates` **(Compute Cores)** (Impact: 59.3)
  * `read_and_verify_shard` **(Compute Cores)** (Impact: 53.0)
  * `prove` **(Compute Cores)** (Impact: 32.3)
  * `dispatch_pairs` **(Compute Cores)** (Impact: 27.5)
  * `compare_backend_against_reference` **(Many-Argument Workhorses)** (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 50 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 38
* *State Mutation (weighted view):* 162
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 270`, `structural_boundaries: 401`, `args: 147`, `func_start: 47`, `class_start: 15`
* *Risk/State:* `high_risk_execution: 8`, `state_mutation: 62`, `unreferenced_by_name: 1`
* *Architecture:* `io: 3`, `concurrency: 8`, `import: 22`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` ed25519_dalek::Signature, ed25519_dalek::Signer, ed25519_dalek::SigningKey, ed25519_dalek::Verifier, ed25519_dalek::VerifyingKey, rand_core::RngCore, serde::Serialize, std::collections::BTreeMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-bench/src/cases/release_workloads.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.362)
- **Top Global Matches:** file_cluster_15: 7.362, file_cluster_0: 7.56, file_cluster_16: 8.669
- **Magnitude:** 831.6 | **LOC:** 2595 | **CtrlFlow:** 7.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.112; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (55.9%), Guard Balance (formerly Safety Score) (53.5%)
- **Documentation Coverage:** 89.7436% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `release_benchmark_csr_forward_baseline` **(Many-Argument Workhorses)** (Impact: 31.7)
  * `callgraph_witness_digest` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `run` **(Many-Argument Workhorses)** (Impact: 26.7)
  * `run` **(Many-Argument Workhorses)** (Impact: 16.1)
  * `run_string_bitmap_scatter` **(Many-Argument Workhorses)** (Impact: 15.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 181
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 254`, `args: 127`, `func_start: 110`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 73`, `duplicate_logic: 8`
* *Architecture:* `api: 21`, `import: 4`
* *Defense:* `safety: 2`, `doc: 21`, `test: 4`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.112
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.000539
  * `Imports (Out-Degree: 5):` crate::api::case::BenchCase, crate::api::case::BenchContext, crate::api::case::BenchError, crate::api::case::BenchId, crate::api::case::BenchLayer, crate::api::case::BenchMetadata, crate::api::case::BenchRequirements, crate::api::case::BenchRun...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `vyre-lower/src/lower.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.2)
- **Top Global Matches:** file_cluster_12: 7.2, file_cluster_4: 9.033, file_cluster_5: 9.222
- **Magnitude:** 823.98 | **LOC:** 1928 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **31**; blast radius 0.179; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.2%), Connectivity (formerly Api Exposure) (49.8%)
- **Documentation Coverage:** 80.2469% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lower_node` **(Many-Argument Workhorses)** (Impact: 128.8)
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
* *Structure:* `branch: 170`, `structural_boundaries: 276`, `args: 107`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 36`, `high_risk_execution: 4`, `state_mutation: 83`, `dead_code: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 21`, `import: 24`
* *Defense:* `safety: 17`, `doc: 70`, `test: 62`, `sync_locks: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.179
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.011059
  * `Imports (Out-Degree: 5):` scope, crate::descriptor::BindingLayout, crate::descriptor::BindingSlot, crate::descriptor::BindingVisibility, crate::descriptor::Dispatch, crate::descriptor::KernelBody, crate::descriptor::KernelDescriptor, crate::descriptor::KernelOp...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/mod/file2alias.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.887)
- **Top Global Matches:** file_cluster_12: 6.887, file_cluster_7: 8.346, file_cluster_16: 8.497
- **Magnitude:** 756.06 | **LOC:** 1522 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (76.5%), Guard Balance (formerly Safety Score) (68.2%), Connectivity (formerly Api Exposure) (0.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `do_usb_entry` **(Many-Argument Workhorses)** (Impact: 37.2)
    * *Intent:* /* USB is special because the bcdDevice can be matched against a numeric range */ /* Looks like "usb...
  * `do_usb_entry_multi` **(Many-Argument Workhorses)** (Impact: 27.4)
  * `handle_moddevtable` **(Many-Argument Workhorses)** (Impact: 24.8)
    * *Intent:* /* Create MODULE_ALIAS() statements. * At this time, we cannot write the actual output C source yet,...
  * `do_pci_entry` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /* Looks like: pci:vNdNsvNsdNbcNscNiN or <prefix>_pci:vNdNsvNsdNbcNscNiN. */
  * `do_input_entry` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* /* input:b0v0p0e0-eXkXrXaXmXlXsXfXwX where X is comma-separated %02X. */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 104 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 317
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 299`, `args: 68`, `func_start: 66`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 109`, `unreferenced_by_name: 1`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` mod_devicetable.h, ctype.h, devicetable-offsets.h, inttypes.h, list.h, modpost.h, stdarg.h, stdbool.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/gconf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.231)
- **Top Global Matches:** file_cluster_4: 6.231, file_cluster_16: 7.009, file_cluster_15: 9.614
- **Magnitude:** 747.5 | **LOC:** 1336 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (82.7%), Guard Balance (formerly Safety Score) (64.7%), Dead Code Surface (formerly Dead Code) (5.1%), Connectivity (formerly Api Exposure) (0.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `set_node` **(Many-Argument Workhorses)** (Impact: 62.9)
  * `on_treeview2_button_press_event` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /* User click: update choice (full) or goes down (single) */
  * `change_sym_value` **(C Struct Operations)** (Impact: 29.3)
    * *Intent:* /* Change the value of a symbol and update the tree */
  * `main` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* /* Main */
  * `on_treeview2_key_press_event` **(C Struct Operations)** (Impact: 23.9)
    * *Intent:* /* Key pressed: update choice */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 311
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 126`, `args: 126`, `func_start: 54`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 145`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 2`, `import: 9`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` gtk.h, images.h, lkc.h, stdio.h, stdlib.h, string.h, strings.h, time.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.993)
- **Top Global Matches:** file_cluster_4: 4.993, file_cluster_6: 9.99, file_cluster_16: 10.74
- **Magnitude:** 738.84 | **LOC:** 865 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **8**; blast radius 0.175; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (77.2%), Guard Balance (formerly Safety Score) (75.9%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 85.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_menu_finalize` **(Many-Argument Workhorses)** (Impact: 64.2)
  * `sym_check_prop` **(Compute Cores)** (Impact: 45.5)
  * `get_prompt_str` **(Many-Argument Workhorses)** (Impact: 30.9)
  * `menu_dump` **(I/O & Config Routines)** (Impact: 27.5)
    * *Intent:* /** * menu_dump - dump all menu entries in a tree-like format */
  * `get_symbol_str` **(C Struct Operations)** (Impact: 22.6)
    * *Intent:* /* * head is optional and may be NULL */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 183`, `args: 35`, `func_start: 33`, `class_start: 40`
* *Risk/State:* `state_mutation: 130`, `unreferenced_by_name: 19`
* *Architecture:* `api: 23`, `import: 8`
* *Defense:* `doc: 4`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001175
  * `Imports (Out-Degree: 4):` ctype.h, internal.h, list.h, lkc.h, stdarg.h, stdlib.h, string.h, xalloc.h
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/conf.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.795)
- **Top Global Matches:** file_cluster_8: 6.795, file_cluster_6: 17.262, file_cluster_3: 20.003
- **Magnitude:** 724.68 | **LOC:** 870 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.077; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (86.1%), Guard Balance (formerly Safety Score) (72.4%), Dead Code Surface (formerly Dead Code) (5.2%), Connectivity (formerly Api Exposure) (0.4%)
- **Documentation Coverage:** 94.7368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 152.5)
  * `conf_set_all_new_symbols` **(Compute Cores)** (Impact: 53.2)
  * `conf_sym` **(Compute Cores)** (Impact: 45.7)
  * `conf_choice` **(Compute Cores)** (Impact: 42.4)
  * `conf` **(Compute Cores)** (Impact: 31.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 89 instances
* *State Mutation (weighted view):* 287
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 143`, `args: 21`, `func_start: 15`, `class_start: 19`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 109`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `import: 12`
* *Defense:* `doc: 1`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` ctype.h, errno.h, getopt.h, internal.h, limits.h, lkc.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `xtask/src/lego_audit.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.974)
- **Top Global Matches:** file_cluster_4: 5.974, file_cluster_6: 10.862, file_cluster_9: 11.237
- **Magnitude:** 720.96 | **LOC:** 1352 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.149; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (23.5%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `check_1_no_reinvention` **(Compute Cores)** (Impact: 42.9)
    * *Intent:* /// Check 1: flag pairs of ops with near-identical fingerprints whose /// Region chains don't indica...
  * `check_10_operand_shape_duplicate` **(Compute Cores)** (Impact: 35.3)
  * `check_4_cross_dialect_reachthrough` **(I/O & Config Routines)** (Impact: 32.4)
    * *Intent:* /// path reaching into `vyre_libs::<other_dialect>::...` or /// `crate::<other_dialect>::...` across...
  * `walk` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `check_9_name_stem_collision` **(Compute Cores)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 170`, `args: 55`, `func_start: 37`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 118`
* *Architecture:* `io: 5`, `api: 15`, `import: 6`
* *Defense:* `safety: 13`, `doc: 87`, `test: 7`, `sync_locks: 3`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.149
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.000639
  * `Imports (Out-Degree: 1):` self::*, std::collections::BTreeMap, std::collections::BTreeSet, std::collections::HashMap, std::io, std::io::Read, std::process, syn::spanned::Spanned...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `vyre-driver-wgpu/src/backend_impl.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.979)
- **Top Global Matches:** file_cluster_0: 6.979, file_cluster_15: 7.598, file_cluster_16: 7.831
- **Magnitude:** 673.86 | **LOC:** 1354 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.124; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (100.0%), Mutation Surface (formerly State Flux) (89.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.3%)
- **Documentation Coverage:** 71.8121% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dispatch_with_device_buffers` **(Many-Argument Workhorses)** (Impact: 39.7)
  * `dispatch_borrowed_batch_into` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /// Dispatch a borrowed batch and write each job's outputs into caller-owned per-job output buffers.
  * `dispatch_borrowed_batch` **(Compute Cores)** (Impact: 23.4)
    * *Intent:* /// Dispatch a batch of borrowed `(Program, inputs, config)` triples.
  * `record_borrowed_batch_job` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `dispatch_borrowed_into` **(Many-Argument Workhorses)** (Impact: 18.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 141
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 175`, `args: 106`, `func_start: 82`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 51`
* *Architecture:* `api: 67`, `import: 9`
* *Defense:* `safety: 15`, `doc: 29`, `test: 13`, `sync_locks: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.124
  * `Choke Point (Betweenness):` 3.2e-05 | `Ripple Effect (Closeness):` 0.022243
  * `Imports (Out-Degree: 5):` crate::AdapterRecoveryTarget, crate::DispatchArena, crate::WgpuBackend, crate::staging_reserve::reserve_backend_vec, crate::staging_reserve::reserve_smallvec, crate::staging_reserve::reserve_vec, self::borrowed_slices_from_owned_inputs, self::empty_batch_result_slots...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/nconf.gui.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.607)
- **Top Global Matches:** file_cluster_8: 6.607, file_cluster_6: 11.299, file_cluster_4: 19.731
- **Magnitude:** 668.48 | **LOC:** 653 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.088; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (78.8%), Guard Balance (formerly Safety Score) (74.8%), Connectivity (formerly Api Exposure) (6.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00024
  * `Imports (Out-Degree: 0):` lkc.h, nconf.h, xalloc.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/segments.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.877)
- **Top Global Matches:** file_cluster_8: 7.877, file_cluster_6: 10.848, file_cluster_4: 19.083
- **Magnitude:** 655.62 | **LOC:** 780 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 0.26; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (58.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `function_argument_prescan_macros` **(Many-Argument Workhorses)** (Impact: 78.8)
  * `macro_use_statement_ranges` **(Many-Argument Workhorses)** (Impact: 55.9)
  * `has_live_macro_for_segment_excluding` **(Defensive Guards)** (Impact: 49.0)
  * `live_macro_defs_for_segment` **(Defensive Guards)** (Impact: 42.0)
  * `classified_segment` **(Defensive Guards)** (Impact: 40.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 166`, `args: 71`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 71`
* *Architecture:* `api: 14`, `import: 19`
* *Defense:* `safety: 28`, `test: 14`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.26
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.009244
  * `Imports (Out-Degree: 5):` crate::parsing::c::lex::tokens::TOK_IDENTIFIER, crate::parsing::c::lex::tokens::TOK_LPAREN, crate::parsing::c::lex::tokens::TOK_RBRACE, crate::parsing::c::lex::tokens::TOK_RPAREN, crate::parsing::c::lex::tokens::TOK_SEMICOLON, rustc_hash::FxHashMap, rustc_hash::FxHashSet, self::*...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `vyre-libs/tests/c_preprocess_gpu_buffer_allocation_contract.rs` (RUST) | Magnitude: 13.24 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 8, api: 8, encapsulation: 8
- `vyre-foundation/src/optimizer/passes/memory/read_only_load_hoist.rs` (RUST) | Magnitude: 145.96 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 398, structural_boundaries: 72, doc: 70, core_var_decl: 50
- `vyre-libs/src/parsing/c/preprocess/expansion/objlike.rs` (RUST) | Magnitude: 5.78 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 6, import: 2, core_var_decl: 2
- `vyre-runtime/src/pipeline_cache/in_memory.rs` (RUST) | Magnitude: 143.08 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 329, structural_boundaries: 75, args: 49, core_var_decl: 42
- `vyre-driver-wgpu/src/config.rs` (RUST) | Magnitude: 13.02 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, api: 10, structural_boundaries: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `vyre-libs/src/compiler/stack_layout.rs` (RUST) | Magnitude: 4.8 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 7, args: 7, doc: 5
- `vyre-reference/tests/dual_reference_parity.rs` (RUST) | Magnitude: 29.26 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, args: 20, branch: 15, structural_boundaries: 15
- `vyre-libs/src/nn/optim/muon_update.rs` (RUST) | Magnitude: 5.12 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, doc: 10, args: 5, branch: 3
- `vyre-libs/src/nn/backward/qk_gain_backward.rs` (RUST) | Magnitude: 7.06 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 10, core_var_decl: 8, design_snake_case: 8
- `vyre-libs/tests/c_preprocess_live_conditional_cache_contract.rs` (RUST) | Magnitude: 8.86 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 6, test: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `vyre-driver-wgpu/tests/__split/c_ast_linux_gnu_declarations_preprocessor_contracts_part1.rs` (RUST) | Magnitude: 12.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 17, test: 15, core_var_decl: 9
- `vyre-lower/tests/dataflow_loop_rewrites.rs` (RUST) | Magnitude: 26.12 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 297, structural_boundaries: 13, args: 11, func_start: 9
- `vyre-driver-wgpu/tests/c_ast_string_init_e2e.rs` (RUST) | Magnitude: 42.76 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 238, structural_boundaries: 29, test: 26, core_var_decl: 20
- `vyre-libs/src/parsing/python/lex.rs` (RUST) | Magnitude: 83.54 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 540, core_var_decl: 39, design_snake_case: 39, doc: 33
- `vyre-frontend-c/src/megakernel_workspace/nodes.rs` (RUST) | Magnitude: 45.78 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 297, doc: 20, structural_boundaries: 14, core_var_decl: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `vyre-core/tests/cross_crate_perf_contracts.rs` (RUST) | Magnitude: 16.42 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 11, test: 10, core_var_decl: 7
- `vyre-reference/src/dialect_dispatch.rs` (RUST) | Magnitude: 70.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 188, structural_boundaries: 44, doc: 38, test: 22
- `vyre-driver/tests/backend_launch_validation.rs` (RUST) | Magnitude: 36.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 34, core_var_decl: 23, design_snake_case: 23
- `vyre-spec/tests/generated_surface_matrix.rs` (RUST) | Magnitude: 71.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 232, structural_boundaries: 36, test: 34, core_var_decl: 28
- `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/driver/active_segments.rs` (RUST) | Magnitude: 24.4 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 24, test: 5, core_var_decl: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `conform/vyre-conform-enforce/tests/module_surface_truth.rs` (RUST) | Magnitude: 35.3 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 45, args: 15, core_var_decl: 13
- `vyre-primitives/src/math/info_geometry.rs` (RUST) | Magnitude: 136.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 280, structural_boundaries: 69, core_var_decl: 55, design_snake_case: 54
- `vyre-self-substrate/src/optimizer/canonicalize_via_encoded.rs` (RUST) | Magnitude: 83.96 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 354, structural_boundaries: 85, core_var_decl: 42, design_snake_case: 41
- `vyre-foundation/tests/consumer_boundary.rs` (RUST) | Magnitude: 27.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 15, core_var_decl: 9, design_snake_case: 9
- `vyre-libs/tests/consumer_boundary.rs` (RUST) | Magnitude: 27.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 15, core_var_decl: 9, design_snake_case: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `scripts/check_tier_config.sh` (SHELL) | Magnitude: 7.02 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 52, io: 21, branch: 17
- `scripts/check_audit_status_tags.sh` (SHELL) | Magnitude: 3.71 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 34, indent_spaces: 20, io: 16, debug_prints: 8
- `scripts/docs.sh` (SHELL) | Magnitude: 9.29 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 67, indent_spaces: 61, branch: 31, io: 24
- `scripts/vyre_smoke.sh` (SHELL) | Magnitude: 3.34 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 24, io: 23, indent_spaces: 19, debug_prints: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `vyre-libs/src/compiler/types_layout.rs` (RUST) | Magnitude: 21.3 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 109, doc: 15, core_var_decl: 10, design_snake_case: 9
- `vyre-reference/src/execution/call.rs` (RUST) | Magnitude: 86.6 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 124, structural_boundaries: 38, branch: 24, core_var_decl: 19
- `xtask/src/catalog.rs` (RUST) | Magnitude: 119.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 213, structural_boundaries: 43, branch: 33, core_var_decl: 31
- `vyre-frontend-c/src/pipeline/buffers/diagnostics.rs` (RUST) | Magnitude: 12.4 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, branch: 3, import: 3
- `vyre-primitives/tests/sweep_graph_csr_bidirectional_oracle_matrix.rs` (RUST) | Magnitude: 89.4 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 110, structural_boundaries: 51, core_var_decl: 32, design_snake_case: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `xtask/src/quick_cache/nibble.rs` (RUST) | Magnitude: 2.82 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 7, explicit_casts: 2, args: 1, func_start: 1
- `vyre-driver-cuda/src/codegen/descriptor_gate.rs` (RUST) | Magnitude: 81.7 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 196, structural_boundaries: 41, core_var_decl: 32, design_snake_case: 32
- `vyre-frontend-c/tests/corpus/r2_kernel_scripts/gendwarfksyms/die.c` (C) | Magnitude: 107.1 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 81, pointers: 71, structural_boundaries: 48, state_mutation: 24
- `vyre-driver-cuda/src/instrumentation.rs` (RUST) | Magnitude: 40.72 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 51, globals: 38, args: 18, func_start: 14
- `vyre-frontend-c/src/pipeline/compile_unit/preproc_mask.rs` (RUST) | Magnitude: 55.96 | Delta: **0.053** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 29, branch: 12, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `vyre-libs/src/math/linalg/matmul_tiled/mod.rs` (RUST) | Magnitude: 15.68 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 22, structural_boundaries: 9, api: 1, import: 1
- `vyre-bench/src/api/mod.rs` (RUST) | Magnitude: 28.26 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13, api: 13, import: 6
- `vyre-libs/src/parsing/c/parse/mod.rs` (RUST) | Magnitude: 20.16 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, doc: 7, api: 6
- `vyre-libs/src/contracts.rs` (RUST) | Magnitude: 17.26 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, doc: 3, api: 2, globals: 2
- `vyre-self-substrate/src/hardware/mod.rs` (RUST) | Magnitude: 20.64 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, encapsulation: 3, doc: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `vyre-frontend-c/src/pipeline/semantic_graph_stage.rs` (RUST) | Magnitude: 30.54 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 74, api: 14, structural_boundaries: 8, generics: 3
- `vyre-libs/src/parsing/c/preprocess/gpu_pipeline/include_events.rs` (RUST) | Magnitude: 34.56 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, api: 19, indent_spaces: 19, structural_boundaries: 3
- `vyre-libs/src/nn/backward/skip_gate_backward.rs` (RUST) | Magnitude: 9.82 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 13, core_var_decl: 11, design_snake_case: 11
- `vyre-foundation/src/vast.rs` (RUST) | Magnitude: 21.26 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 13, api: 6, import: 6, doc: 5
- `vyre-libs/src/nn/optim/mod.rs` (RUST) | Magnitude: 26.22 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 11, api: 11, import: 5, doc: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `vyre-self-substrate/src/optimizer/expr_arena.rs` (RUST) | Magnitude: 224.24 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 598, structural_boundaries: 103, core_var_decl: 88, design_snake_case: 79
- `vyre-self-substrate/src/math/sinkhorn_dispatch_clustering.rs` (RUST) | Magnitude: 271.82 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 803, structural_boundaries: 127, core_var_decl: 75, design_snake_case: 75
- `vyre-foundation/src/optimizer/passes/cleanup/empty_block_collapse.rs` (RUST) | Magnitude: 127.98 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 253, structural_boundaries: 61, core_var_decl: 47, design_snake_case: 45
- `vyre-libs/tests/gpu_ifdef_value_roundtrip.rs` (RUST) | Magnitude: 142.1 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 199, structural_boundaries: 96, core_var_decl: 58, design_snake_case: 58
- `xtask/src/release_benchmarks.rs` (RUST) | Magnitude: 909.76 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 2068, structural_boundaries: 362, branch: 226, core_var_decl: 198

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `vyre-libs/src/nn/linear/inner/tests/tiled.rs` (RUST) | Magnitude: 29.06 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 165, structural_boundaries: 40, core_var_decl: 33, design_snake_case: 33
- `vyre-self-substrate/src/graph/resident_handles.rs` (RUST) | Magnitude: 44.48 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 19, branch: 9, core_var_decl: 7
- `vyre-libs/tests/matching_post_process_contracts.rs` (RUST) | Magnitude: 25.54 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 29, test: 25, core_var_decl: 25
- `vyre-self-substrate/src/graph/csr_forward_or_changed/tests.rs` (RUST) | Magnitude: 116.12 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 509, structural_boundaries: 122, test: 78, core_var_decl: 61
- `vyre-self-substrate/src/scheduling/spectral_schedule.rs` (RUST) | Magnitude: 131.8 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 313, structural_boundaries: 93, doc: 56, core_var_decl: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vyre-driver-wgpu/src/parity_probe.rs` (RUST) | Magnitude: 124.14 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 314, structural_boundaries: 82, core_var_decl: 51, design_snake_case: 50
- `vyre-frontend-c/tests/r2_corpus_measurement.rs` (RUST) | Magnitude: 292.42 | Delta: **0.095** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 715, structural_boundaries: 228, core_var_decl: 136, design_snake_case: 119
- `vyre-frontend-c/src/pipeline/backend_select/resident_dispatch.rs` (RUST) | Magnitude: 205.44 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 320, structural_boundaries: 66, branch: 56, core_var_decl: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `vyre-frontend-c/src/megakernel_workspace/tests.rs` (RUST) | Magnitude: 99.98 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 207, test: 55, structural_boundaries: 42, core_var_decl: 38
- `vyre-driver-wgpu/tests/sinkhorn_iterate_contract.rs` (RUST) | Magnitude: 3.58 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 9, core_var_decl: 5, design_snake_case: 5
- `vyre-emit-ptx/tests/adversarial_emit_program_matrix.rs` (RUST) | Magnitude: 42.24 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 160, test: 30, structural_boundaries: 18, branch: 15
- `vyre-debug/tests/descriptor_dump_tests.rs` (RUST) | Magnitude: 19.5 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 20, core_var_decl: 15, design_snake_case: 15
- `vyre-driver-cuda/tests/cooperative_launch_contracts.rs` (RUST) | Magnitude: 42.12 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 170, structural_boundaries: 43, core_var_decl: 27, design_snake_case: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `vyre-frontend-c/tests/clang_declaration_oracle.rs` (RUST) | Magnitude: 9.82 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 10, branch: 6, test: 6
- `vyre-primitives/tests/adversarial_text_utf8_validate.rs` (RUST) | Magnitude: 52.92 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, branch: 21, structural_boundaries: 16, args: 14
- `vyre-foundation/src/optimizer/passes/fusion_cse/fusion_tests.rs` (RUST) | Magnitude: 99.54 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 347, structural_boundaries: 40, branch: 30, core_var_decl: 30
- `vyre-emit-ptx/src/emitter/names.rs` (RUST) | Magnitude: 18.46 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 43, branch: 6, args: 3, doc: 3
- `vyre-libs/src/parsing/c/mod.rs` (RUST) | Magnitude: 128.92 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 126, branch: 38, structural_boundaries: 38, args: 28

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `vyre-lints/src/lib.rs` -> Churn: **69.9%** | Cog Load: 29.4801% | Debt: 99.9991%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `vyre-driver-cuda/src/backend/resident_dispatch.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1470.26
- `vyre-driver-cuda/src/egraph_kernel_plan.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 1308.48
- `vyre-primitives/src/graph/exploded.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 895.78
- `conform/vyre-conform-runner/src/main.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 835.3
- `vyre-bench/src/cases/release_workloads.rs` -> **Mukund Thiru** (100.0% isolated ownership) | Magnitude: 831.6

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `vyre-foundation/src/lib.rs` -> **Severity: 0.548** (Bridge: 0.0512 * Flux: 10.6956%)
- `vyre-foundation/src/optimizer.rs` -> **Severity: 0.411** (Bridge: 0.0169 * Flux: 24.2901%)
- `vyre-driver/src/backend.rs` -> **Severity: 0.273** (Bridge: 0.0046 * Flux: 58.8707%)
- `vyre-foundation/src/optimizer/passes/algebraic/const_fold/mod.rs` -> **Severity: 0.14** (Bridge: 0.0018 * Flux: 76.6695%)
- `vyre-driver-cuda/src/backend/dispatch.rs` -> **Severity: 0.114** (Bridge: 0.0019 * Flux: 59.9372%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `vyre-foundation/src/lib.rs` -> **Severity: 16.805** (Embedded: 0.3616 * Error Risk: 46.4693%)
- `vyre-foundation/src/validate/validate.rs` -> **Severity: 13.705** (Embedded: 0.2302 * Error Risk: 59.5416%)
- `vyre-foundation/src/optimizer/diff_compile.rs` -> **Severity: 13.101** (Embedded: 0.1701 * Error Risk: 77.0297%)
- `vyre-foundation/src/ir_inner/model/program/stats.rs` -> **Severity: 12.84** (Embedded: 0.2298 * Error Risk: 55.8747%)
- `vyre-foundation/src/allocation.rs` -> **Severity: 12.395** (Embedded: 0.2301 * Error Risk: 53.8613%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `vyre-foundation/src/ir_inner/model/program/stats.rs` -> **Severity: 1561.65** (Blast Radius: 20.822 * Doc Risk: 75.0%)
- `vyre-macros/tests/support/mod.rs` -> **Severity: 903.8** (Blast Radius: 9.038 * Doc Risk: 100.0%)
- `vyre-foundation/src/ir_inner/model/program/core.rs` -> **Severity: 676.8** (Blast Radius: 10.152 * Doc Risk: 66.6667%)
- `vyre-lower/src/descriptor.rs` -> **Severity: 583.353** (Blast Radius: 8.44 * Doc Risk: 69.1176%)
- `vyre-foundation/src/dispatch/extern_registry.rs` -> **Severity: 353.483** (Blast Radius: 6.03 * Doc Risk: 58.6207%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2594 literal sites + 87 sites through wrappers = 2681
- **`memory_alloc`:** 4192 literal sites + 58 sites through wrappers = 4250
- **`panics_and_aborts`:** 2165 literal sites + 396 sites through wrappers = 2561

- `pack_i4x8_cpu` (function, panics_and_aborts, primitive): 43 call sites in 3 files -- `vyre-primitives/src/math/quantized/cpu.rs`
- `kernel_offset_usize_or_panic` (function, panics_and_aborts, primitive): 16 call sites in 1 files -- `vyre-runtime/src/uring/ring.rs`
- `finalize` (function, debug_prints, primitive): 15 call sites in 1 files -- `vyre-libs/tests/fixtures/go/pipeline.go`
- `build_chd` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `vyre-libs/src/intern/perfect_hash.rs`
- `flushStats` (function, debug_prints, primitive): 13 call sites in 1 files -- `vyre-libs/tests/fixtures/go/worker_pool.go`
- `logCall` (function, debug_prints, primitive): 12 call sites in 1 files -- `vyre-libs/tests/fixtures/go/storage.go`
- `str_free` (function, memory_alloc, primitive): 12 call sites in 5 files -- `vyre-frontend-c/tests/corpus/r2_kernel_scripts/kconfig/util.c`
- `count_u64` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `vyre-frontend-c/src/api/security_index/common.rs`
- `detect_cross_arm_redundancy` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `vyre-runtime/src/megakernel/planner/whole_megakernel_opt.rs`
- `usize_from_u32` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `vyre-primitives/src/bitset/four_russians.rs`
- `gaussian_rdp_step_cpu` (function, panics_and_aborts, primitive): 8 call sites in 2 files -- `vyre-primitives/src/math/dp_accountant.rs`
- `hot_path_test_guard` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `vyre-driver-wgpu/tests/dispatch_hot_path.rs`
*(+120 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 204973 call pairs -- scoped 18.0%, unique 0.2%, ambiguous 15.8%, external 66.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 200461 | 17.9% | 0.0% | 16.1% | 66.0% |
| c | 3490 | 24.7% | 12.0% | 0.6% | 62.7% |
| shell | 629 | 15.7% | 0.0% | 0.0% | 84.3% |
| python | 246 | 16.7% | 0.0% | 0.0% | 83.3% |
| go | 147 | 78.9% | 0.0% | 0.0% | 21.1% |

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
