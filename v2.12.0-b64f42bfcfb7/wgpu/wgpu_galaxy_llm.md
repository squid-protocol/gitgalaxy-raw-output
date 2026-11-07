# ARCHITECTURAL_BRIEF: wgpu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gfx-rs/wgpu.git` |
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
- **Scope:** 894 analyzed artifact(s), 265620 LOC.
- **Load-bearing artifact:** `naga/src/ir/mod.rs` -- 102 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `wgpu/src/backend/webgpu/webgpu_sys/mod.rs` -- pulls in 256 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `naga/src/back/msl/writer.rs` at magnitude 5411.92 (structural weight, not risk).
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
| Total Artifacts | 2230 |
| Analyzed Artifacts (Scanned) | 894 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1336 |
| Total LOC | 265620 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 40.1% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7444 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.312 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 46.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.7877 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 32 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 760 | 261517 | 85.0% |
| MARKDOWN | 56 | 0 | 6.3% |
| GLSL | 54 | 1510 | 6.0% |
| YAML | 15 | 1287 | 1.7% |
| JAVASCRIPT | 4 | 1005 | 0.4% |
| HTML | 2 | 184 | 0.2% |
| PLAINTEXT | 1 | 0 | 0.1% |
| SHELL | 1 | 21 | 0.1% |
| JSON | 1 | 96 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 894 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 19%, Large Core Modules (3) 19%, Generic / Templated Code Files 15%, State Mutators Files 15%, Data / Markup / Trivial 12%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 837 | 93.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 57 | 6.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1336*

**Composition by Extension & Reason:**
- `.wgsl`: 201x Excluded (Unsupported Extension: '.wgsl'), 162x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 55x Unsupported Format (.wgsl)
- `.toml`: 170x Excluded (Unsupported Extension: '.toml'), 30x Unsupported Format (.toml), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.spvasm`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Unsupported Extension: '.spvasm')
- `.ron`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Unsupported Extension: '.ron')
- `.metal`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.metal'), 1x Unsupported Format (.metal)
- `.glsl`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hlsl`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.hlsl')
- `.png`: 40x Excluded (Explicitly Denied Extension: '.png')
- `.apache`: 13x Excluded (Unsupported Extension: '.APACHE')
- `.mit`: 13x Excluded (Unsupported Extension: '.MIT')
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ktx2`: 3x Excluded (Binary Format Detected), 1x Excluded (Monolithic Amalgamation: 185587 LOC exceeds the 150000 LOC backstop)
- `.slang`: 4x Excluded (Unsupported Extension: '.slang')
- `.bin`: 4x Excluded (Unsupported Extension: '.bin')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.6 | 5.6 | 3.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.9 | 31.5 | 49.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.9 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 95.3 | 31.3 | 26.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 15.4 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.7 | 0.9 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 73.2 | 11.5 | 4.3 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 54.1 | 53.8 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3179 | 409 | 9 | `wgpu-hal/src/gles/queue.rs` |
| cleanup | 191 | 73 | 0 | `tests/tests/wgpu-gpu/render_pass_ownership.rs` |
| guards | 6130 | 515 | 17 | `naga/src/back/hlsl/writer.rs` |
| danger | 3639 | 370 | 10 | `wgpu-types/src/texture/format.rs` |
| concurrency | 2109 | 286 | 8 | `wgpu-core/src/device/resource.rs` |
| connectivity | 10664 | 736 | 32 | `wgpu-hal/src/lib.rs` |
| io | 84 | 38 | 0 | `cts_runner/src/main.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 7 | 0 | `tests/tests/wgpu-gpu/passthrough/mod.rs` |
| time | 13 | 12 | 0 | `benches/src/iter.rs` |
| serialization | 152 | 5 | 0 | `wgpu-types/src/texture/format.rs` |
| regex | 2 | 2 | 0 | `xtask/src/changelog.rs` |
| events | 640 | 124 | 2 | `wgpu-hal/src/gles/egl.rs` |
| tests | 1759 | 257 | 4 | `wgpu-types/src/texture/format.rs` |
| docs | 32575 | 585 | 90 | `naga/src/ir/mod.rs` |
| debt | 976 | 252 | 3 | `wgpu/src/backend/webgpu.rs` |
| mutation | 30662 | 767 | 75 | `naga/src/back/msl/writer.rs` |
| dead_code | 903 | 147 | 2 | `wgpu-hal/src/lib.rs` |
| credential | 6 | 6 | 0 | `.github/actions/install-mesa/action.yml` |
| threat | 3 | 2 | 0 | `wgpu/src/util/spirv.rs` |
| ml_ai | 1272 | 209 | 3 | `naga/src/proc/constant_evaluator.rs` |
| ui | 12 | 3 | 0 | `examples/features/web-static/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4105**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cts_runner/src/main.rs` (Hits: 6)
- `tests/tests/wgpu-gpu/passthrough/mod.rs` (Hits: 6)
- `wgpu-core/src/device/trace/record.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **mod.rs** (`naga/src/ir/mod.rs`) — 102 inbound connections
2. **config.rs** (`tests/src/config.rs`) — 102 inbound connections
3. **params.rs** (`tests/src/params.rs`) — 99 inbound connections
4. **lib.rs** (`wgpu-macros/src/lib.rs`) — 98 inbound connections
5. **mod.rs** (`wgpu/src/backend/webgpu/webgpu_sys/mod.rs`) — 96 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **mod.rs** (`wgpu/src/backend/webgpu/webgpu_sys/mod.rs`) — 256 outbound dependencies
2. **lib.rs** (`wgpu/src/lib.rs`) — 151 outbound dependencies
3. **mod.rs** (`wgpu-core/src/command/mod.rs`) — 134 outbound dependencies
4. **resource.rs** (`wgpu-core/src/device/resource.rs`) — 113 outbound dependencies
5. **render.rs** (`wgpu-core/src/command/render.rs`) — 104 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `next_block` **(Many-Argument Workhorses)** (@ `naga/src/front/spv/next_block.rs`) -> Impact: **1330.2** | LOC: 3083
  * *Intent:* /// Add the next SPIR-V block's contents to `block_ctx`. /// /// Except for the function's entry block, `block_id` should be the label of /// a block ...
- `write_expr` **(Many-Argument Workhorses)** (@ `naga/src/back/hlsl/writer.rs`) -> Impact: **1133.9** | LOC: 1436
  * *Intent:* /// Helper method to write expressions /// /// # Notes /// Doesn't add any newlines or leading/trailing spaces
- `call_builtin` **(Many-Argument Workhorses)** (@ `naga/src/front/wgsl/lower/mod.rs`) -> Impact: **780.6** | LOC: 853
  * *Intent:* /// Generate Naga IR for a call to a WGSL builtin function.
- `write_functions` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **773.8** | LOC: 1317
- `put_expression` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **752.0** | LOC: 998
  * *Intent:* /// Emit code for the expression `expr_handle`. /// /// The `is_scoped` argument is true if the surrounding operators have the /// precedence of the c...
- `write_stmt` **(Many-Argument Workhorses)** (@ `naga/src/back/hlsl/writer.rs`) -> Impact: **732.3** | LOC: 830
  * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
- `put_block` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **637.9** | LOC: 683
- `write_stmt` **(Many-Argument Workhorses)** (@ `naga/src/back/wgsl/writer.rs`) -> Impact: **542.0** | LOC: 503
  * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
- `validate_expression` **(Many-Argument Workhorses)** (@ `naga/src/valid/expression.rs`) -> Impact: **523.5** | LOC: 1049
- `lower_inner` **(Many-Argument Workhorses)** (@ `naga/src/front/glsl/context.rs`) -> Impact: **436.9** | LOC: 851
  * *Intent:* /// Internal implementation of [`lower`](Self::lower)

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `naga/src/back/hlsl` | 8 | 7255.02 | 16.27% | 7.58% |
| `naga/src/back/msl` | 4 | 5687.0 | 6.85% | 12.02% |
| `wgpu-core/src/command` | 20 | 5185.9 | 5.9% | 7.7% |
| `naga/src/back/spv` | 13 | 4940.28 | 11.25% | 20.25% |
| `wgpu-hal/src/vulkan` | 9 | 4725.92 | 18.37% | 12.76% |
| `naga/src/front/spv` | 7 | 4439.94 | 14.14% | 5.04% |
| `wgpu/src/backend/webgpu/webgpu_sys` | 128 | 4371.04 | 0.47% | 0.0% |
| `wgpu-core/src/device` | 8 | 4157.86 | 8.09% | 15.78% |
| `naga/src/front/glsl` | 13 | 3947.3 | 8.57% | 9.86% |
| `wgpu-hal/src/dx12` | 15 | 3818.46 | 13.64% | 8.8% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `naga/src/back/spv/reclaimable.rs` -> **100.0%** Exposure
- `naga/src/proc/overloads/mod.rs` -> **100.0%** Exposure
- `wgpu-core/src/lock/vanilla.rs` -> **100.0%** Exposure
- `wgpu-hal/src/vulkan/swapchain/mod.rs` -> **100.0%** Exposure
- `wgpu/src/dispatch.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `wgpu/src/util/device.rs` -> **100.0%** Exposure
- `wgpu-hal/src/dx12/view.rs` -> **99.9998%** Exposure
- `wgpu-hal/src/vulkan/conv.rs` -> **99.997%** Exposure
- `naga/src/back/dot/mod.rs` -> **99.9939%** Exposure
- `wgpu-core/src/track/range.rs` -> **99.9924%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wgpu-hal/src/lib.rs` -> **125** Orphaned Functions | **0** Duplicates
- `wgpu/src/backend/webgpu.rs` -> **0** Orphaned Functions | **66** Duplicates
- `wgpu-hal/src/noop/mod.rs` -> **60** Orphaned Functions | **0** Duplicates
- `wgpu/src/dispatch.rs` -> **0** Orphaned Functions | **60** Duplicates
- `wgpu-hal/src/dx12/mod.rs` -> **30** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `7954` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `naga/src/back/msl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.26)
- **Top Global Matches:** file_cluster_8: 8.26, file_cluster_6: 8.929, file_cluster_4: 17.214
- **Magnitude:** 5411.92 | **LOC:** 8257 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 17.6%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **48**; blast radius 0.431; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.2%), Guard Balance (formerly Safety Score) (51.9%), Connectivity (formerly Api Exposure) (27.1%)
- **Documentation Coverage:** 61.6822% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_functions` **(Many-Argument Workhorses)** (Impact: 773.8)
  * `put_expression` **(Many-Argument Workhorses)** (Impact: 752.0)
    * *Intent:* /// Emit code for the expression `expr_handle`. /// /// The `is_scoped` argument is true if the surr...
  * `put_block` **(Many-Argument Workhorses)** (Impact: 637.9)
  * `write_unpacking_function` **(Many-Argument Workhorses)** (Impact: 256.5)
  * `write_wrapped_image_sample` **(Many-Argument Workhorses)** (Impact: 147.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 77 instances
* *High Risk Execution (weighted view):* 25
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1911`, `structural_boundaries: 996`, `args: 148`, `func_start: 103`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 36`, `state_mutation: 100`, `dead_code: 1`, `planned_debt: 10`, `fragile_debt: 4`
* *Architecture:* `api: 27`, `import: 19`
* *Defense:* `safety: 106`, `doc: 364`, `test: 9`, `sync_locks: 13`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.431
  * `Choke Point (Betweenness):` 7.9e-05 | `Ripple Effect (Closeness):` 0.066008
  * `Imports (Out-Degree: 14):` alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec, alloc::vec::Vec, back::msl::VertexFormat, back::msl::VertexFormat::*, core::cmp::Ordering...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/back/hlsl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.759)
- **Top Global Matches:** file_cluster_8: 7.759, file_cluster_6: 9.745, file_cluster_4: 18.219
- **Magnitude:** 3929.96 | **LOC:** 5021 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **44**; blast radius 0.777; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.9%), Connectivity (formerly Api Exposure) (34.1%)
- **Documentation Coverage:** 49.2063% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_expr` **(Many-Argument Workhorses)** (Impact: 1133.9)
    * *Intent:* /// Helper method to write expressions /// /// # Notes /// Doesn't add any newlines or leading/trail...
  * `write_stmt` **(Many-Argument Workhorses)** (Impact: 732.3)
    * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
  * `write_function` **(Many-Argument Workhorses)** (Impact: 309.1)
    * *Intent:* /// Helper method used to write functions /// # Notes /// Ends in a newline
  * `write` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `write_switch` **(Many-Argument Workhorses)** (Impact: 134.1)
    * *Intent:* /// Helper method used to write switches
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 22
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1395`, `structural_boundaries: 625`, `args: 98`, `func_start: 48`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 28`, `state_mutation: 65`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `api: 59`, `import: 14`
* *Defense:* `safety: 138`, `doc: 96`, `test: 2`, `sync_locks: 31`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.777
  * `Choke Point (Betweenness):` 0.000167 | `Ripple Effect (Closeness):` 0.068507
  * `Imports (Out-Degree: 12):` alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec::Vec, back::continue_forward::ExitControlFlow, core::fmt, core::fmt::Write, core::mem...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `naga/src/front/wgsl/lower/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.939)
- **Top Global Matches:** file_cluster_4: 8.939, file_cluster_6: 9.187, file_cluster_0: 15.282
- **Magnitude:** 2678.38 | **LOC:** 4879 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 34.5%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **39**; blast radius 0.805; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (81.3%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.2%), Guard Balance (formerly Safety Score) (53.4%)
- **Documentation Coverage:** 75.5319% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `call_builtin` **(Many-Argument Workhorses)** (Impact: 780.6)
    * *Intent:* /// Generate Naga IR for a call to a WGSL builtin function.
  * `statement` **(Many-Argument Workhorses)** (Impact: 191.8)
  * `texture_sample_helper` **(Many-Argument Workhorses)** (Impact: 108.4)
  * `expression_for_reference` **(Many-Argument Workhorses)** (Impact: 88.7)
  * `function` **(Many-Argument Workhorses)** (Impact: 81.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 110 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 743`, `structural_boundaries: 1148`, `args: 161`, `func_start: 86`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 11`, `state_mutation: 160`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 16`, `import: 20`
* *Defense:* `safety: 71`, `doc: 321`, `test: 2`, `sync_locks: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.805
  * `Choke Point (Betweenness):` 0.005725 | `Ripple Effect (Closeness):` 0.082503
  * `Imports (Out-Degree: 21):` construction, conversion, template_list, ExpressionContextType, SubgroupGather, alloc::borrow::ToOwned, alloc::boxed::Box, alloc::format...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `wgpu-core/src/device/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.33)
- **Top Global Matches:** file_cluster_6: 8.33, file_cluster_8: 9.77, file_cluster_4: 16.062
- **Magnitude:** 2136.3 | **LOC:** 5265 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 40.5%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **113**; blast radius 2.004; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%), Guard Balance (formerly Safety Score) (51.3%), Connectivity (formerly Api Exposure) (42.3%)
- **Documentation Coverage:** 76.5766% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_render_pipeline` **(Many-Argument Workhorses)** (Impact: 324.5)
  * `create_texture_view` **(Many-Argument Workhorses)** (Impact: 133.2)
  * `create_texture` **(Many-Argument Workhorses)** (Impact: 121.5)
  * `configure_surface` **(Many-Argument Workhorses)** (Impact: 95.5)
  * `create_bind_group_layout_internal` **(Many-Argument Workhorses)** (Impact: 85.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 65 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 29
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 708`, `structural_boundaries: 782`, `args: 174`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 8`, `state_mutation: 82`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `api: 87`, `concurrency: 6`, `import: 33`
* *Defense:* `safety: 74`, `doc: 182`, `test: 4`, `sync_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.004
  * `Choke Point (Betweenness):` 0.002061 | `Ripple Effect (Closeness):` 0.065348
  * `Imports (Out-Degree: 28):` alloc::borrow::Cow, alloc::boxed::Box, alloc::string::String, alloc::string::ToString, alloc::sync::Arc, alloc::sync::Weak, alloc::vec::Vec, arrayvec::ArrayVec...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `naga/src/front/spv/next_block.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.32)
- **Top Global Matches:** file_cluster_8: 8.32, file_cluster_6: 17.828, file_cluster_3: 20.697
- **Magnitude:** 1730.68 | **LOC:** 3129 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **24**; blast radius 0.414; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (24.6%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next_block` **(Many-Argument Workhorses)** (Impact: 1330.2)
    * *Intent:* /// Add the next SPIR-V block's contents to `block_ctx`. /// /// Except for the function's entry blo...
  * `make_index_literal` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `merger` **(Parameter Forwarders)** (Impact: 4.1)
    * *Intent:* // Extend `body` with the correct form for a branch to `target`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 71 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 588`, `structural_boundaries: 688`, `args: 59`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 6`, `state_mutation: 192`, `planned_debt: 6`, `fragile_debt: 4`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 32`, `doc: 8`, `test: 3`, `sync_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.071885
  * `Imports (Out-Degree: 6):` alloc::format, alloc::vec, alloc::vec::Vec, crate::Handle, crate::MathFunction, crate::SwizzleComponent, crate::front::spv::BlockContext, crate::front::spv::Body...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/back/spv/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 4.858)
- **Top Global Matches:** file_cluster_4: 4.858, file_cluster_6: 9.851, file_cluster_16: 10.921
- **Magnitude:** 1723.6 | **LOC:** 3849 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 29.4%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **58**; blast radius 0.62; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.9%)
- **Documentation Coverage:** 74.6032% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_function` **(Many-Argument Workhorses)** (Impact: 245.6)
  * `write_logical_layout` **(Many-Argument Workhorses)** (Impact: 136.2)
  * `map_binding` **(Many-Argument Workhorses)** (Impact: 105.7)
  * `write_global_variable` **(Many-Argument Workhorses)** (Impact: 66.6)
  * `write_std140_compat_type_declaration` **(Many-Argument Workhorses)** (Impact: 62.2)
    * *Intent:* /// type declaration, if one is required. /// * Two-row matrix members will have each of their colum...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 15
* *State Mutation (weighted view):* 356
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 685`, `args: 130`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 17`, `state_mutation: 188`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 55`, `import: 17`
* *Defense:* `safety: 73`, `doc: 162`, `test: 4`, `sync_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.62
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.06901
  * `Imports (Out-Degree: 13):` alloc::format, alloc::string::String, alloc::vec, alloc::vec::Vec, arrayvec::ArrayVec, core::mem::take, crate::BuiltIn, crate::ScalarKind...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wgpu-core/src/command/render.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.702)
- **Top Global Matches:** file_cluster_4: 6.702, file_cluster_15: 10.372, file_cluster_0: 10.449
- **Magnitude:** 1699.64 | **LOC:** 3865 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **104**; blast radius 1.38; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.3%), Guard Balance (formerly Safety Score) (51.4%)
- **Documentation Coverage:** 93.8931% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `start` **(Many-Argument Workhorses)** (Impact: 386.2)
  * `encode_render_pass` **(Many-Argument Workhorses)** (Impact: 136.4)
  * `fill_arc_desc` **(Many-Argument Workhorses)** (Impact: 85.3)
  * `command_encoder_begin_render_pass` **(Many-Argument Workhorses)** (Impact: 84.5)
    * *Intent:* /// Creates a render pass. /// /// If creation fails, an invalid pass is returned. Attempting to rec...
  * `multi_draw_indirect` **(Many-Argument Workhorses)** (Impact: 80.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 506`, `args: 142`, `func_start: 92`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 83`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 86`, `import: 11`
* *Defense:* `safety: 38`, `doc: 90`, `test: 1`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.38
  * `Choke Point (Betweenness):` 0.001282 | `Ripple Effect (Closeness):` 0.064877
  * `Imports (Out-Degree: 25):` EncoderStateError, alloc::borrow::Cow, alloc::sync::Arc, alloc::vec::Vec, arrayvec::ArrayVec, core::convert::Infallible, core::fmt, core::num::NonZeroU32...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `naga/src/front/spv/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.85)
- **Top Global Matches:** file_cluster_4: 6.85, file_cluster_6: 8.914, file_cluster_12: 12.905
- **Magnitude:** 1686.24 | **LOC:** 3275 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **30**; blast radius 1.484; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.9%)
- **Documentation Coverage:** 85.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parse_global_variable` **(Many-Argument Workhorses)** (Impact: 74.8)
  * `parse` **(Compute Cores)** (Impact: 60.0)
  * `next_decoration` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `parse_type_image` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `parse_expr_binary_op_sign_adjusted` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* /// A more complicated version of the binary op, /// where we force the operand to have the same typ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 100 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 475`, `structural_boundaries: 688`, `args: 95`, `func_start: 76`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 5`, `state_mutation: 172`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 14`, `import: 13`
* *Defense:* `safety: 57`, `doc: 241`, `test: 3`, `sync_locks: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.484
  * `Choke Point (Betweenness):` 0.003953 | `Ripple Effect (Closeness):` 0.084499
  * `Imports (Out-Degree: 12):` convert, error, function, image, next_block, null, alloc::borrow::ToOwned, alloc::string::String...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `naga/src/back/wgsl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.147)
- **Top Global Matches:** file_cluster_8: 6.147, file_cluster_6: 11.689, file_cluster_4: 20.321
- **Magnitude:** 1682.02 | **LOC:** 2170 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 31.2%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **31**; blast radius 0.59; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.1%), Guard Balance (formerly Safety Score) (52.0%), Mutation Surface (formerly State Flux) (44.1%)
- **Documentation Coverage:** 64.8649% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_stmt` **(Many-Argument Workhorses)** (Impact: 542.0)
    * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
  * `write_expr_plain_form` **(Many-Argument Workhorses)** (Impact: 435.1)
    * *Intent:* /// Write the 'plain form' of `expr`. /// /// An expression's 'plain form' is the most general rendi...
  * `write_possibly_const_expression` **(Many-Argument Workhorses)** (Impact: 87.5)
  * `write` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `write_function` **(Many-Argument Workhorses)** (Impact: 73.8)
    * *Intent:* /// Helper method used to write /// [functions](https://gpuweb.github.io/gpuweb/wgsl/#functions) ///...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 7
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 599`, `structural_boundaries: 224`, `args: 59`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 8`, `state_mutation: 39`, `planned_debt: 5`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 46`, `doc: 117`, `sync_locks: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.59
  * `Choke Point (Betweenness):` 8.7e-05 | `Ripple Effect (Closeness):` 0.066008
  * `Imports (Out-Degree: 12):` alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec, alloc::vec::Vec, core::fmt::Write, crate::DerivativeAxis, crate::DerivativeControl...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/proc/constant_evaluator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.731)
- **Top Global Matches:** file_cluster_4: 8.731, file_cluster_12: 9.575, file_cluster_5: 10.002
- **Magnitude:** 1639.58 | **LOC:** 4774 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 35.3%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **43**; blast radius 0.791; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.8%), Connectivity (formerly Api Exposure) (43.3%)
- **Documentation Coverage:** 65.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `math` **(Many-Argument Workhorses)** (Impact: 281.3)
  * `binary_op` **(Many-Argument Workhorses)** (Impact: 181.0)
  * `cast` **(Many-Argument Workhorses)** (Impact: 83.3)
    * *Intent:* /// Convert the scalar components of `expr` to `target`. /// /// Treat `span` as the location of the...
  * `try_eval_and_append_impl` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `select` **(Many-Argument Workhorses)** (Impact: 44.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 43 instances
* *State Mutation (weighted view):* 193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 506`, `structural_boundaries: 758`, `args: 246`, `func_start: 99`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 17`, `state_mutation: 107`, `planned_debt: 3`
* *Architecture:* `api: 24`, `import: 18`
* *Defense:* `safety: 40`, `doc: 230`, `test: 55`, `sync_locks: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.791
  * `Choke Point (Betweenness):` 0.000567 | `Ripple Effect (Closeness):` 0.108185
  * `Imports (Out-Degree: 9):` Literal, alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec, alloc::vec::Vec, arrayvec::ArrayVec, core::iter...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `naga/src/back/hlsl/help.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 11.172)
- **Top Global Matches:** file_cluster_8: 11.172, file_cluster_3: 12.699, file_cluster_6: 23.84
- **Magnitude:** 1612.58 | **LOC:** 2333 | **CtrlFlow:** 32.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **24**; blast radius 0.523; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Mutation Surface (formerly State Flux) (45.0%), Connectivity (formerly Api Exposure) (31.1%)
- **Documentation Coverage:** 95.2381% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_wrapped_constructor_function` **(Many-Argument Workhorses)** (Impact: 117.4)
  * `write_wrapped_image_query_function` **(Many-Argument Workhorses)** (Impact: 114.8)
  * `write_wrapped_image_sample_function` **(Many-Argument Workhorses)** (Impact: 111.3)
  * `write_wrapped_math_functions` **(Many-Argument Workhorses)** (Impact: 106.7)
  * `write_wrapped_binary_ops` **(Many-Argument Workhorses)** (Impact: 103.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 23
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 268`, `args: 46`, `func_start: 37`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 26`, `state_mutation: 40`, `planned_debt: 3`
* *Architecture:* `api: 68`, `import: 14`
* *Defense:* `safety: 24`, `doc: 73`, `test: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.523
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.068474
  * `Imports (Out-Degree: 6):` alloc::format, core::fmt::Write, crate::ImageDimension, crate::ImageQuery, crate::ScalarKind, crate::arena::Handle, crate::back::COMPONENTS, crate::back::INDENT...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/vulkan/adapter.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.147)
- **Top Global Matches:** file_cluster_6: 7.147, file_cluster_8: 11.974, file_cluster_4: 13.823
- **Magnitude:** 1514.08 | **LOC:** 3366 | **CtrlFlow:** 12.6% | **Authorship Centralization:** 18.4%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.503; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (71.2%), Guard Balance (formerly Safety Score) (56.6%)
- **Documentation Coverage:** 70.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `from_extensions_and_requested_features` **(Many-Argument Workhorses)** (Impact: 187.4)
    * *Intent:* /// `private_caps`: /// /// - The given `enabled_extensions` set must include all the extensions ///...
  * `device_from_raw` **(Many-Argument Workhorses)** (Impact: 187.0)
    * *Intent:* /// # Safety /// /// - `raw_device` must be created from this adapter. /// - `raw_device` must be cr...
  * `to_wgpu` **(Many-Argument Workhorses)** (Impact: 111.6)
    * *Intent:* /// Compute the wgpu [`Features`] and [`DownlevelFlags`] supported by a physical device. /// /// Giv...
  * `inspect` **(Many-Argument Workhorses)** (Impact: 110.4)
  * `get_required_extensions` **(Many-Argument Workhorses)** (Impact: 80.1)
    * *Intent:* /// Map `requested_features` to the list of Vulkan extension strings required to create the logical ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 146 instances
* *State Mutation (weighted view):* 483
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 393`, `args: 140`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 191`, `dead_code: 7`, `planned_debt: 9`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* `safety: 69`, `doc: 196`, `test: 2`, `sync_locks: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.503
  * `Choke Point (Betweenness):` 0.001497 | `Ripple Effect (Closeness):` 0.068196
  * `Imports (Out-Degree: 4):` alloc::borrow::ToOwned, alloc::boxed::Box, alloc::collections::BTreeMap, alloc::sync::Arc, alloc::vec::Vec, ash::ext, ash::google, ash::khr...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/front/wgsl/parse/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.504)
- **Top Global Matches:** file_cluster_6: 9.504, file_cluster_4: 12.764, file_cluster_8: 17.095
- **Magnitude:** 1362.78 | **LOC:** 2409 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 61.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **35**; blast radius 0.618; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (73.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.2%), Guard Balance (formerly Safety Score) (58.5%)
- **Documentation Coverage:** 75.4717% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `global_decl` **(Many-Argument Workhorses)** (Impact: 233.8)
  * `statement` **(Many-Argument Workhorses)** (Impact: 164.7)
  * `parse` **(Many-Argument Workhorses)** (Impact: 77.5)
  * `function_decl` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `variable_or_value_or_func_call_or_variable_updating_statement` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* /// Parses variable_or_value_statement, func_call_statement and variable_updating_statement. /// ///...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 534`, `args: 87`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 2`, `state_mutation: 74`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 19`, `doc: 90`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.618
  * `Choke Point (Betweenness):` 0.003672 | `Ripple Effect (Closeness):` 0.082371
  * `Imports (Out-Degree: 15):` ast, conv, directive, lexer, number, alloc::boxed::Box, alloc::vec::Vec, crate::Arena...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/back/spv/block.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.382)
- **Top Global Matches:** file_cluster_6: 5.382, file_cluster_8: 11.402, file_cluster_4: 12.934
- **Magnitude:** 1310.06 | **LOC:** 4232 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **29**; blast radius 0.665; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (70.3%), Guard Balance (formerly Safety Score) (57.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.0%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cache_expression_value` **(Many-Argument Workhorses)** (Impact: 290.6)
    * *Intent:* /// Cache an expression for a value.
  * `write_block` **(Many-Argument Workhorses)** (Impact: 224.2)
    * *Intent:* /// Use `label_id` as the label for the SPIR-V entry point block. /// /// If control reaches the end...
  * `write_as_expression` **(Many-Argument Workhorses)** (Impact: 76.8)
    * *Intent:* /// Helper which focuses on generating the `As` expressions and the various conversions /// that nee...
  * `write_access_chain` **(Many-Argument Workhorses)** (Impact: 58.4)
    * *Intent:* /// Build an `OpAccessChain` instruction. /// /// Emit any needed bounds-checking expressions to `bl...
  * `write_checked_load` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 43
* *State Mutation (weighted view):* 283
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 601`, `args: 55`, `func_start: 25`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 44`, `state_mutation: 189`, `dead_code: 10`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 41`, `doc: 212`, `test: 1`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.665
  * `Choke Point (Betweenness):` 0.000158 | `Ripple Effect (Closeness):` 0.069078
  * `Imports (Out-Degree: 7):` alloc::vec::Vec, arrayvec::ArrayVec, crate::DerivativeAxis, crate::DerivativeControl, crate::MathFunction, crate::RelationalFunction, crate::ScalarKind, crate::Statement...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `naga/src/front/glsl/builtins.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 5.531)
- **Top Global Matches:** file_cluster_3: 5.531, file_cluster_8: 20.226, file_cluster_6: 33.225
- **Magnitude:** 1155.9 | **LOC:** 2376 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **32**; blast radius 0.452; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.0%), Connectivity (formerly Api Exposure) (28.5%)
- **Documentation Coverage:** 27.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `inject_standard_builtins` **(Many-Argument Workhorses)** (Impact: 195.2)
    * *Intent:* /// Injects the builtins into declaration that don't need any special variations
  * `call` **(Many-Argument Workhorses)** (Impact: 192.7)
    * *Intent:* /// Adds the necessary expressions and statements to the passed body and /// finally returns the fin...
  * `inject_builtin` **(Many-Argument Workhorses)** (Impact: 180.1)
    * *Intent:* /// Inject builtins into the declaration /// /// This is done to not add a large startup cost and no...
  * `inject_common_builtin` **(Many-Argument Workhorses)** (Impact: 109.7)
    * *Intent:* /// Injects the builtins into declaration that can used either float or doubles
  * `inject_double_builtin` **(Many-Argument Workhorses)** (Impact: 62.5)
    * *Intent:* /// Injects the builtins into declaration that need doubles
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 57 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 280`, `args: 55`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 23`, `state_mutation: 97`, `dead_code: 12`, `planned_debt: 3`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 34`, `doc: 37`, `test: 2`, `sync_locks: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.452
  * `Choke Point (Betweenness):` 0.00028 | `Ripple Effect (Closeness):` 0.071685
  * `Imports (Out-Degree: 7):` alloc::vec, alloc::vec::Vec, crate::BinaryOperator, crate::DerivativeAxis, crate::DerivativeControl, crate::Expression, crate::Handle, crate::ImageClass...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wgpu/src/backend/webgpu.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.718)
- **Top Global Matches:** file_cluster_12: 7.718, file_cluster_15: 8.522, file_cluster_0: 8.924
- **Magnitude:** 1109.62 | **LOC:** 4059 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 24.1%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **59**; blast radius 2.378; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.8%)
- **Documentation Coverage:** 96.9325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `begin_render_pass` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `create_render_pipeline` **(Defensive Guards)** (Impact: 21.1)
  * `create_bind_group_layout` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `create_shader_module` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `request_adapter` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 42
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 241`, `structural_boundaries: 590`, `args: 277`, `func_start: 235`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 49`, `state_mutation: 12`, `dead_code: 1`, `planned_debt: 11`, `duplicate_logic: 66`
* *Architecture:* `api: 141`, `concurrency: 12`, `import: 35`
* *Defense:* `safety: 75`, `doc: 81`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.378
  * `Choke Point (Betweenness):` 0.03393 | `Ripple Effect (Closeness):` 0.052989
  * `Imports (Out-Degree: 21):` defined_non_null_js_value, ext_bindings, webgpu_sys, alloc::boxed::Box, alloc::format, alloc::rc::Rc, alloc::string::String, alloc::string::ToString...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wgpu/src/backend/wgpu_core.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.888)
- **Top Global Matches:** file_cluster_0: 7.888, file_cluster_15: 8.661, file_cluster_12: 9.832
- **Magnitude:** 1108.9 | **LOC:** 4037 | **CtrlFlow:** 6.0% | **Authorship Centralization:** 20.8%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **56**; blast radius 2.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (62.6%), Guard Balance (formerly Safety Score) (48.1%)
- **Documentation Coverage:** 97.205% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_bind_group` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `pop_error_scope` **(Defensive Guards)** (Impact: 19.3)
  * `handle_error_or_return_handler` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* /// Deliver the error to /// /// * the innermost error scope, if any, or /// * the uncaptured error ...
  * `handle_error_inner` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `print_tree` **(Defensive Guards)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 590`, `args: 290`, `func_start: 212`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `api: 164`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 106`, `doc: 23`, `test: 1`, `sync_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.03
  * `Choke Point (Betweenness):` 0.000376 | `Ripple Effect (Closeness):` 0.052989
  * `Imports (Out-Degree: 4):` thread_id, alloc::borrow::Cow, alloc::borrow::Cow::Borrowed, alloc::boxed::Box, alloc::format, alloc::string::String, alloc::string::ToString, alloc::sync::Arc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/vulkan/device.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.362)
- **Top Global Matches:** file_cluster_4: 7.362, file_cluster_12: 8.053, file_cluster_15: 8.627
- **Magnitude:** 1060.76 | **LOC:** 2827 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 0.426; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (73.8%), Guard Balance (formerly Safety Score) (54.3%)
- **Documentation Coverage:** 91.8519% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_render_pipeline` **(Many-Argument Workhorses)** (Impact: 68.2)
  * `compile_stage` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `create_bind_group_layout` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `error_if_would_oom_on_resource_allocation` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `make_render_pass` **(Many-Argument Workhorses)** (Impact: 30.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 70 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 244
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 481`, `args: 115`, `func_start: 77`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 6`, `state_mutation: 104`, `planned_debt: 3`
* *Architecture:* `api: 58`, `import: 9`
* *Defense:* `safety: 60`, `doc: 48`, `sync_locks: 20`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.068154
  * `Imports (Out-Degree: 3):` alloc::borrow::ToOwned, alloc::collections::BTreeMap, alloc::ffi::CString, alloc::sync::Arc, alloc::vec::Vec, arrayvec::ArrayVec, ash::ext, ash::vk...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/dx12/device.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.344)
- **Top Global Matches:** file_cluster_4: 6.344, file_cluster_6: 8.357, file_cluster_12: 13.051
- **Magnitude:** 958.38 | **LOC:** 2655 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 26.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **37**; blast radius 0.48; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.8%), Connectivity (formerly Api Exposure) (72.5%), Guard Balance (formerly Safety Score) (54.2%)
- **Documentation Coverage:** 99.0291% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `create_pipeline_layout` **(Many-Argument Workhorses)** (Impact: 121.0)
  * `create_render_pipeline` **(Many-Argument Workhorses)** (Impact: 74.7)
  * `new` **(Many-Argument Workhorses)** (Impact: 67.3)
  * `create_bind_group` **(Many-Argument Workhorses)** (Impact: 52.8)
  * `load_shader` **(Many-Argument Workhorses)** (Impact: 52.6)
    * *Intent:* /// When generating the vertex shader, the fragment stage must be passed if it exists! /// Otherwise...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 350`, `args: 74`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 3`, `state_mutation: 97`, `planned_debt: 6`, `fragile_debt: 1`
* *Architecture:* `api: 50`, `import: 12`
* *Defense:* `safety: 47`, `doc: 3`, `test: 6`, `sync_locks: 15`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.48
  * `Choke Point (Betweenness):` 0.001945 | `Ripple Effect (Closeness):` 0.069136
  * `Imports (Out-Degree: 12):` alloc::borrow::Cow, alloc::borrow::ToOwned, alloc::string::String, alloc::string::ToString, alloc::sync::Arc, alloc::vec::Vec, arrayvec::ArrayVec, bytemuck::TransparentWrapper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/front/glsl/functions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.402)
- **Top Global Matches:** file_cluster_8: 10.402, file_cluster_3: 14.914, file_cluster_6: 22.522
- **Magnitude:** 920.06 | **LOC:** 1624 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.371; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (14.8%)
- **Documentation Coverage:** 52.9412% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `function_call` **(Many-Argument Workhorses)** (Impact: 173.3)
  * `constructor_single` **(Many-Argument Workhorses)** (Impact: 95.6)
  * `process_lhs_argument` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* /// Processes a function call argument that appears in place of an output /// parameter.
  * `matrix_one_arg` **(Many-Argument Workhorses)** (Impact: 79.3)
  * `constructor_many` **(Many-Argument Workhorses)** (Impact: 46.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 246`, `args: 33`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 86`, `planned_debt: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 21`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.371
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.071436
  * `Imports (Out-Degree: 10):` ScalarKind::*, alloc::format, alloc::string::String, alloc::string::ToString, alloc::vec, alloc::vec::Vec, core::cmp::Ordering, core::iter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `wgpu-core/src/device/global.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.966)
- **Top Global Matches:** file_cluster_0: 7.966, file_cluster_15: 8.198, file_cluster_4: 9.036
- **Magnitude:** 832.68 | **LOC:** 2127 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **57**; blast radius 0.513; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.9%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 73.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `device_create_general_render_pipeline` **(Many-Argument Workhorses)** (Impact: 77.2)
  * `device_create_bind_group` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `device_create_compute_pipeline` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `resolve_entry` **(Many-Argument Workhorses)** (Impact: 33.8)
  * `device_create_pipeline_layout` **(Many-Argument Workhorses)** (Impact: 23.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 21 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 184`, `structural_boundaries: 453`, `args: 98`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 27`, `planned_debt: 2`
* *Architecture:* `api: 68`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 61`, `doc: 106`, `test: 1`, `sync_locks: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.513
  * `Choke Point (Betweenness):` 6e-05 | `Ripple Effect (Closeness):` 0.062718
  * `Imports (Out-Degree: 17):` alloc::borrow::Cow, alloc::boxed::Box, alloc::string::String, alloc::sync::Arc, alloc::vec::Vec, core::ptr::NonNull, core::sync::atomic::Ordering, crate::Label...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/front/glsl/context.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.089)
- **Top Global Matches:** file_cluster_0: 8.089, file_cluster_4: 8.625, file_cluster_15: 8.993
- **Magnitude:** 807.04 | **LOC:** 1550 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **37**; blast radius 0.593; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (60.6%), Mutation Surface (formerly State Flux) (60.4%), Guard Balance (formerly Safety Score) (51.9%)
- **Documentation Coverage:** 54.902% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lower_inner` **(Many-Argument Workhorses)** (Impact: 436.9)
    * *Intent:* /// Internal implementation of [`lower`](Self::lower)
  * `add_function_arg` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /// Add function argument to current scope
  * `add_global` **(Many-Argument Workhorses)** (Impact: 23.8)
  * `binary_implicit_conversion` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `lower_store` **(Many-Argument Workhorses)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 241`, `args: 54`, `func_start: 28`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 42`, `dead_code: 4`
* *Architecture:* `api: 41`, `import: 4`
* *Defense:* `safety: 23`, `doc: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.593
  * `Choke Point (Betweenness):` 0.000762 | `Ripple Effect (Closeness):` 0.071784
  * `Imports (Out-Degree: 11):` alloc::format, alloc::string::String, alloc::vec::Vec, core::ops::Index, crate::AddressSpace, crate::Arena, crate::BinaryOperator, crate::Block...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/gles/command.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.964)
- **Top Global Matches:** file_cluster_15: 7.964, file_cluster_4: 8.271, file_cluster_12: 8.345
- **Magnitude:** 784.42 | **LOC:** 1310 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.447; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.6%), Guard Balance (formerly Safety Score) (65.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `begin_render_pass` **(Many-Argument Workhorses)** (Impact: 70.7)
    * *Intent:* // render
  * `set_render_pipeline` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `rebind_vertex_data` **(Compute Cores)** (Impact: 28.9)
  * `set_bind_group` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `transition_textures` **(Generic / Templated Code)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 84 instances
* *High Risk Execution (weighted view):* 12
* *State Mutation (weighted view):* 312
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 189`, `args: 73`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 13`, `state_mutation: 144`, `planned_debt: 2`
* *Architecture:* `api: 49`, `import: 5`
* *Defense:* `safety: 16`, `test: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.447
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.068196
  * `Imports (Out-Degree: 3):` alloc::string::String, arrayvec::ArrayVec, core::mem, core::ops::Range, crate::CommandEncoder, super::Command, super::conv
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `naga/src/valid/function.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.403)
- **Top Global Matches:** file_cluster_6: 7.403, file_cluster_4: 12.144, file_cluster_8: 14.712
- **Magnitude:** 765.24 | **LOC:** 1933 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **22**; blast radius 0.94; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.9%), Mutation Surface (formerly State Flux) (39.7%), Connectivity (formerly Api Exposure) (26.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validate_block_impl` **(Many-Argument Workhorses)** (Impact: 321.4)
  * `validate_atomic` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `validate_function` **(Many-Argument Workhorses)** (Impact: 60.0)
  * `validate_call` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `validate_subgroup_gather` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 230`, `structural_boundaries: 295`, `args: 65`, `func_start: 17`, `class_start: 8`
* *Risk/State:* `state_mutation: 35`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 29`, `doc: 3`, `sync_locks: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.94
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.104829
  * `Imports (Out-Degree: 10):` alloc::format, alloc::string::String, crate::AddressSpace, crate::CollectiveOperation, crate::Expression, crate::ScalarKind, crate::Statement, crate::SubgroupOperation...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/metal/command.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.677)
- **Top Global Matches:** file_cluster_12: 7.677, file_cluster_5: 8.458, file_cluster_4: 10.123
- **Magnitude:** 759.48 | **LOC:** 1919 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 16.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **47**; blast radius 0.555; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.2%), Guard Balance (formerly Safety Score) (56.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (54.7%)
- **Documentation Coverage:** 99.1597% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `begin_render_pass` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* // render
  * `update_bind_group_state` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* /// Updates the bindings for a single shader stage, called in `set_bind_group`.
  * `set_render_pipeline` **(Many-Argument Workhorses)** (Impact: 37.1)
  * `set_immediates` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `set_bind_group` **(Many-Argument Workhorses)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 308`, `args: 88`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `high_risk_execution: 11`, `state_mutation: 49`, `planned_debt: 4`, `fragile_debt: 1`
* *Architecture:* `api: 51`, `import: 9`
* *Defense:* `safety: 65`, `doc: 5`, `test: 16`, `sync_locks: 4`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.555
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.068112
  * `Imports (Out-Degree: 5):` alloc::borrow::Cow, alloc::borrow::ToOwned, alloc::sync::Arc, alloc::vec::Vec, core::ops::Range, core::ptr::NonNull, core::sync::atomic, crate::CommandEncoder...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `wgpu-core/src/command/render_command.rs` (RUST) | Magnitude: 19.02 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 88, doc: 35, structural_boundaries: 7, decorators: 5
- `wgpu-core/src/command/allocator.rs` (RUST) | Magnitude: 16.4 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 24, doc: 17, structural_boundaries: 9, sync_locks: 6
- `deno_webgpu/buffer.rs` (RUST) | Magnitude: 133.06 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 52, decorators: 36, api: 24
- `tests/tests/wgpu-gpu/shader/mod.rs` (RUST) | Magnitude: 92.1 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 264, structural_boundaries: 49, doc: 37, core_var_decl: 26
- `wgpu-core/src/limits.rs` (RUST) | Magnitude: 74.96 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 368, structural_boundaries: 90, doc: 68, core_var_decl: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/tests/wgpu-gpu/resource_error.rs` (RUST) | Magnitude: 4.94 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 60, args: 13, branch: 9, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/tests/wgpu-validation/api/experimental.rs` (RUST) | Magnitude: 13.16 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 9, core_var_decl: 9, design_snake_case: 9
- `wgpu-core/src/command/bind.rs` (RUST) | Magnitude: 228.08 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 437, structural_boundaries: 69, branch: 50, args: 33
- `tests/tests/wgpu-dependency/main.rs` (RUST) | Magnitude: 70.12 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 232, args: 23, decorators: 22, func_start: 21
- `examples/standalone/02_hello_window/src/main.rs` (RUST) | Magnitude: 35.18 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 36, core_var_decl: 18, design_snake_case: 17
- `tests/tests/wgpu-gpu/oob_indexing.rs` (RUST) | Magnitude: 64.04 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 388, structural_boundaries: 49, core_var_decl: 39, design_snake_case: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `deno_webgpu/device.rs` (RUST) | Magnitude: 222.6 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 854, structural_boundaries: 129, decorators: 84, args: 57
- `examples/features/src/lib.rs` (RUST) | Magnitude: 42.26 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 45, structural_boundaries: 38, api: 36, decorators: 6
- `wgpu-core/src/command/draw.rs` (RUST) | Magnitude: 15.54 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 123, decorators: 37, structural_boundaries: 13, generics: 9
- `wgpu-hal/src/auxil/mod.rs` (RUST) | Magnitude: 91.14 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 147, structural_boundaries: 45, api: 33, core_var_decl: 26
- `wgpu-types/src/assertions.rs` (RUST) | Magnitude: 15.84 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 18, indent_spaces: 18, decorators: 12, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `wgpu-hal/src/gles/conv.rs` (RUST) | Magnitude: 89.78 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 371, branch: 19, structural_boundaries: 16, args: 16
- `wgpu-core/src/timestamp_normalization/mod.rs` (RUST) | Magnitude: 95.22 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 306, structural_boundaries: 61, doc: 42, core_var_decl: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `naga/src/back/spv/layout.rs` (RUST) | Magnitude: 97.38 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 61, state_mutation: 32, core_var_decl: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `wgpu/src/backend/webgpu/webgpu_sys/mod.rs` (RUST) | Magnitude: 147.12 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 255, import: 128, api: 127, doc: 3
- `tests/tests/wgpu-validation/api/mod.rs` (RUST) | Magnitude: 15.26 | Delta: **0.188** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/tests/wgpu-gpu/queue_transfer.rs` (RUST) | Magnitude: 6.64 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 9, core_var_decl: 9, args: 6
- `tests/tests/wgpu-gpu/texture_view_creation.rs` (RUST) | Magnitude: 9.04 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 13, core_var_decl: 9, args: 8
- `tests/tests/wgpu-gpu/oom.rs` (RUST) | Magnitude: 74.2 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, structural_boundaries: 53, core_var_decl: 33, design_snake_case: 19
- `naga/src/front/type_gen.rs` (RUST) | Magnitude: 114.62 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 547, structural_boundaries: 52, doc: 42, state_mutation: 35
- `tests/tests/wgpu-gpu/bind_group_layout_dedup.rs` (RUST) | Magnitude: 45.86 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 390, structural_boundaries: 72, core_var_decl: 61, design_snake_case: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `wgpu-info/src/human.rs` (RUST) | Magnitude: 293.62 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 266, branch: 121, doc: 76, structural_boundaries: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/tests/wgpu-gpu/subgroup_operations/mod.rs` (RUST) | Magnitude: 6.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 26, core_var_decl: 17, design_snake_case: 16
- `examples/features/src/hello_windows/mod.rs` (RUST) | Magnitude: 69.88 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 48, core_var_decl: 19, design_snake_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `wgpu-core/src/command/transfer.rs` (RUST) | Magnitude: 546.28 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1161, structural_boundaries: 181, branch: 161, core_var_decl: 91

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `examples/standalone/01_hello_compute/src/main.rs` (RUST) | Magnitude: 17.68 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 25, core_var_decl: 17, design_snake_case: 17

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `wgpu-hal/src/metal/mod.rs` -> Churn: **65.49%** | Cog Load: 8.8071% | Debt: 57.8%
- `.github/workflows/ci.yml` -> Churn: **64.1%** | Cog Load: 4.6922% | Debt: 70.2941%
- `wgpu/src/backend/webgpu.rs` -> Churn: **57.75%** | Cog Load: 5.9928% | Debt: 99.2531%
- `wgpu-hal/src/noop/mod.rs` -> Churn: **52.64%** | Cog Load: 5.948% | Debt: 99.9997%
- `wgpu-hal/src/lib.rs` -> Churn: **51.39%** | Cog Load: 2.947% | Debt: 99.9985%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `naga/src/front/glsl/builtins.rs` -> **Connor Fitzgerald** (100.0% isolated ownership) | Magnitude: 1155.9
- `naga/src/back/hlsl/ray.rs` -> **Vecvec** (100.0% isolated ownership) | Magnitude: 730.32
- `wgpu-hal/src/vulkan/conv.rs` -> **Connor Fitzgerald** (100.0% isolated ownership) | Magnitude: 698.74
- `naga/src/back/spv/ray/query.rs` -> **Vecvec** (100.0% isolated ownership) | Magnitude: 413.22
- `naga/src/front/glsl/parser/declarations.rs` -> **06wj** (100.0% isolated ownership) | Magnitude: 407.46

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `naga/src/front/mod.rs` -> **Severity: 1.816** (Bridge: 0.0195 * Flux: 93.2678%)
- `naga/src/front/glsl/mod.rs` -> **Severity: 0.774** (Bridge: 0.0088 * Flux: 87.6926%)
- `wgpu-core/src/lib.rs` -> **Severity: 0.683** (Bridge: 0.0336 * Flux: 20.3635%)
- `wgpu/src/api/instance.rs` -> **Severity: 0.629** (Bridge: 0.0067 * Flux: 93.8426%)
- `wgpu/src/api/tlas.rs` -> **Severity: 0.497** (Bridge: 0.0052 * Flux: 95.4978%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `naga/src/arena/unique_arena.rs` -> **Severity: 7.982** (Embedded: 0.1471 * Error Risk: 54.2677%)
- `naga/src/arena/handle.rs` -> **Severity: 7.755** (Embedded: 0.156 * Error Risk: 49.717%)
- `naga/src/arena/range.rs` -> **Severity: 7.579** (Embedded: 0.1434 * Error Risk: 52.8657%)
- `naga/src/arena/mod.rs` -> **Severity: 7.424** (Embedded: 0.1479 * Error Risk: 50.1946%)
- `naga/src/error.rs` -> **Severity: 7.133** (Embedded: 0.133 * Error Risk: 53.6252%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `naga/src/ir/mod.rs` -> **Severity: 2449.9** (Blast Radius: 24.499 * Doc Risk: 100.0%)
- `naga/src/arena/handle.rs` -> **Severity: 1633.45** (Blast Radius: 23.335 * Doc Risk: 70.0%)
- `wgpu/src/api/mod.rs` -> **Severity: 1588.065** (Blast Radius: 47.642 * Doc Risk: 33.3333%)
- `wgpu/src/dispatch.rs` -> **Severity: 884.066** (Blast Radius: 9.281 * Doc Risk: 95.2555%)
- `wgpu-core/src/resource.rs` -> **Severity: 861.368** (Blast Radius: 11.126 * Doc Risk: 77.4194%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 223 literal sites + 2 sites through wrappers = 225
- **`panics_and_aborts`:** 221 literal sites + 8 sites through wrappers = 229

- `get_unexpected_err` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `wgpu-hal/src/vulkan/mod.rs`
- `handle_unexpected` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `wgpu-hal/src/vulkan/device.rs`
- `exit_with_help` (function, debug_prints, primitive): 2 call sites in 1 files -- `wgpu-info/src/cli.rs`
- `default_error_handler` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `wgpu/src/backend/wgpu_core.rs`
- `get_lost_err` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `wgpu-hal/src/vulkan/mod.rs`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 41855 call pairs -- scoped 14.2%, unique 0.0%, ambiguous 18.9%, external 66.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| rust | 41746 | 14.2% | 0.0% | 19.0% | 66.8% |
| javascript | 101 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 5 | 0.0% | 0.0% | 0.0% | 100.0% |
| html | 3 | 0.0% | 0.0% | 0.0% | 100.0% |

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
