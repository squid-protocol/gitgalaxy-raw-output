# ARCHITECTURAL_BRIEF: wgpu
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gfx-rs/wgpu.git` |
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
| Total Artifacts | 2230 |
| Analyzed Artifacts (Scanned) | 880 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1350 |
| Total LOC | 268917 |
| Volatility Index | 0.014 |
| % Scanned of codebase = | 39.5% |
| Dominant Lang | RUST |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.8686 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4274 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.0685 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| RUST | 761 | 266084 | 86.5% |
| GLSL | 54 | 1510 | 6.1% |
| MARKDOWN | 51 | 0 | 5.8% |
| JAVASCRIPT | 4 | 1005 | 0.5% |
| BINARY_THREAT | 4 | 4 | 0.5% |
| HTML | 2 | 184 | 0.2% |
| YAML | 1 | 13 | 0.1% |
| PLAINTEXT | 1 | 0 | 0.1% |
| SHELL | 1 | 21 | 0.1% |
| JSON | 1 | 96 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Flat Modular Platform` (z +0.06; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 25%, Annotated Framework Methods Files 17%, Declarative / Non-Code 11%, Data / Markup / Trivial 11%, State Mutators Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 824 | 93.6% |
| Unknown | 4 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 52 | 5.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1350*

**Composition by Extension & Reason:**
- `.wgsl`: 201x Excluded (Unsupported Extension: '.wgsl'), 162x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 54x Unsupported Format (.wgsl)
- `.toml`: 170x Excluded (Unsupported Extension: '.toml'), 30x Unsupported Format (.toml), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.spvasm`: 121x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 32x Excluded (Unsupported Extension: '.spvasm')
- `.ron`: 128x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Unsupported Extension: '.ron')
- `.metal`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.metal'), 1x Unsupported Format (.metal)
- `.glsl`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hlsl`: 89x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.hlsl')
- `.png`: 40x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 14x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 5504 LOC)
- `.apache`: 13x Excluded (Unsupported Extension: '.APACHE')
- `.mit`: 13x Excluded (Unsupported Extension: '.MIT')
- `no_extension`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ktx2`: 4x Excluded (Binary Format Detected)
- `.slang`: 4x Excluded (Unsupported Extension: '.slang')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 64.6 | 5.7 | 3.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 33.6 | 49.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 26.8 | 3.9 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 20.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 97.2 | 14.4 | 6.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.7 | 1.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 89.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.7 | 1.1 | 0.1 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 15.8 | 5.6 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 53.7 | 52.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10254 | 626 | 29 | `wgpu-hal/src/gles/queue.rs` |
| cleanup | 190 | 72 | 0 | `tests/tests/wgpu-gpu/render_pass_ownership.rs` |
| guards | 6200 | 516 | 17 | `naga/src/back/hlsl/writer.rs` |
| danger | 3686 | 369 | 10 | `wgpu-types/src/texture/format.rs` |
| concurrency | 2116 | 280 | 8 | `wgpu-core/src/device/resource.rs` |
| connectivity | 10074 | 710 | 30 | `wgpu-hal/src/lib.rs` |
| io | 71 | 32 | 0 | `cts_runner/src/main.rs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 12 | 7 | 0 | `tests/tests/wgpu-gpu/passthrough/mod.rs` |
| time | 13 | 12 | 0 | `benches/src/iter.rs` |
| serialization | 152 | 5 | 0 | `wgpu-types/src/texture/format.rs` |
| regex | 2 | 2 | 0 | `xtask/src/changelog.rs` |
| events | 640 | 124 | 2 | `wgpu-hal/src/gles/egl.rs` |
| tests | 1928 | 258 | 4 | `naga/tests/naga/wgsl_errors.rs` |
| docs | 32595 | 573 | 91 | `naga/src/ir/mod.rs` |
| debt | 953 | 246 | 3 | `wgpu/src/backend/webgpu.rs` |
| mutation | 30903 | 756 | 77 | `naga/src/back/msl/writer.rs` |
| dead_code | 3455 | 556 | 9 | `naga/tests/naga/wgsl_errors.rs` |
| credential | 4 | 4 | 0 | `naga/src/back/msl/writer.rs` |
| threat | 267 | 82 | 0 | `deno_webgpu/01_webgpu.js` |
| ml_ai | 1499 | 210 | 4 | `naga/tests/naga/wgsl_errors.rs` |
| ui | 12 | 3 | 0 | `examples/features/web-static/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.4914**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `cts_runner/src/main.rs` (Hits: 6)
- `tests/tests/wgpu-gpu/passthrough/mod.rs` (Hits: 6)
- `wgpu-core/src/device/trace/record.rs` (Hits: 6)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **iter.rs** (`benches/src/iter.rs`) — 14 inbound connections
2. **format.rs** (`wgpu-types/src/texture/format.rs`) — 12 inbound connections
3. **id.rs** (`wgpu-core/src/id.rs`) — 8 inbound connections
4. **ir.rs** (`naga/fuzz/fuzz_targets/ir.rs`) — 7 inbound connections
5. **fs.rs** (`naga/xtask/src/fs.rs`) — 3 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **lib.rs** (`wgpu/src/lib.rs`) — 140 outbound dependencies
2. **mod.rs** (`wgpu/src/backend/webgpu/webgpu_sys/mod.rs`) — 129 outbound dependencies
3. **resource.rs** (`wgpu-core/src/device/resource.rs`) — 117 outbound dependencies
4. **mod.rs** (`wgpu-core/src/command/mod.rs`) — 115 outbound dependencies
5. **render.rs** (`wgpu-core/src/command/render.rs`) — 103 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `write_expr` **(Many-Argument Workhorses)** (@ `naga/src/back/hlsl/writer.rs`) -> Impact: **852.9** | LOC: 1137
  * *Intent:* /// Helper method to write expressions /// /// # Notes /// Doesn't add any newlines or leading/trailing spaces
- `call_builtin` **(Many-Argument Workhorses)** (@ `naga/src/front/wgsl/lower/mod.rs`) -> Impact: **780.6** | LOC: 853
  * *Intent:* /// Generate Naga IR for a call to a WGSL builtin function.
- `put_expression` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **761.0** | LOC: 998
  * *Intent:* /// Emit code for the expression `expr_handle`. /// /// The `is_scoped` argument is true if the surrounding operators have the /// precedence of the c...
- `write_stmt` **(Many-Argument Workhorses)** (@ `naga/src/back/hlsl/writer.rs`) -> Impact: **756.8** | LOC: 830
  * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
- `write_functions` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **729.6** | LOC: 1217
- `put_block` **(Many-Argument Workhorses)** (@ `naga/src/back/msl/writer.rs`) -> Impact: **658.0** | LOC: 683
- `write_stmt` **(Many-Argument Workhorses)** (@ `naga/src/back/wgsl/writer.rs`) -> Impact: **559.1** | LOC: 503
  * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
- `validate_expression` **(Many-Argument Workhorses)** (@ `naga/src/valid/expression.rs`) -> Impact: **526.5** | LOC: 1049
- `next_block` **(Many-Argument Workhorses)** (@ `naga/src/front/spv/next_block.rs`) -> Impact: **472.6** | LOC: 1132
  * *Intent:* /// Add the next SPIR-V block's contents to `block_ctx`. /// /// Except for the function's entry block, `block_id` should be the label of /// a block ...
- `lower_inner` **(Many-Argument Workhorses)** (@ `naga/src/front/glsl/context.rs`) -> Impact: **436.9** | LOC: 851
  * *Intent:* /// Internal implementation of [`lower`](Self::lower)

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `naga/src/back/hlsl` | 8 | 7160.12 | 17.17% | 15.55% |
| `naga/src/back/msl` | 4 | 5742.0 | 7.06% | 12.02% |
| `wgpu-core/src/command` | 20 | 5189.2 | 6.07% | 27.96% |
| `naga/src/back/spv` | 13 | 4879.38 | 11.26% | 40.0% |
| `wgpu-hal/src/vulkan` | 9 | 4738.62 | 18.46% | 24.4% |
| `wgpu/src/backend/webgpu/webgpu_sys` | 128 | 4349.04 | 1.21% | 52.73% |
| `wgpu-core/src/device` | 8 | 4169.66 | 7.81% | 54.21% |
| `naga/src/front/glsl` | 13 | 3978.1 | 9.24% | 28.16% |
| `wgpu-hal/src/dx12` | 15 | 3839.46 | 13.72% | 19.98% |
| `naga/src/valid` | 8 | 3719.6 | 9.5% | 14.92% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `naga/src/arena/handle_set.rs` -> **100.0%** Exposure
- `naga/src/back/spv/reclaimable.rs` -> **100.0%** Exposure
- `naga/src/proc/overloads/mod.rs` -> **100.0%** Exposure
- `wgpu-core/src/lock/vanilla.rs` -> **100.0%** Exposure
- `wgpu-hal/src/vulkan/swapchain/mod.rs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `wgpu/src/util/device.rs` -> **100.0%** Exposure
- `wgpu-hal/src/dx12/view.rs` -> **99.9998%** Exposure
- `wgpu-hal/src/vulkan/conv.rs` -> **99.997%** Exposure
- `naga/src/back/dot/mod.rs` -> **99.9939%** Exposure
- `wgpu-core/src/track/range.rs` -> **99.9924%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `wgpu/src/backend/webgpu.rs` -> **88** Orphaned Functions | **66** Duplicates
- `naga/tests/naga/wgsl_errors.rs` -> **149** Orphaned Functions | **0** Duplicates
- `wgpu-hal/src/lib.rs` -> **125** Orphaned Functions | **0** Duplicates
- `naga/src/back/spv/instructions.rs` -> **94** Orphaned Functions | **0** Duplicates
- `wgpu-core/src/device/global.rs` -> **68** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `7929` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `wgpu-hal/src/gles/command.rs` (RUST) -> Cumulative Risk: **680.02**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.16)
- **Magnitude:** 784.42 | **LOC:** 1310 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9716%), Safety Score (87.7971%)
- **Heaviest Functions:** `begin_render_pass` (Many-Argument Workhorses, Impact: 70.7), `set_render_pipeline` (Many-Argument Workhorses, Impact: 47.1), `rebind_vertex_data` (Compute Cores, Impact: 28.9)

### 2. `deno_webgpu/buffer.rs` (RUST) -> Cumulative Risk: **629.89**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Annotated Framework Methods Files` (z +0.26)
- **Magnitude:** 133.06 | **LOC:** 279 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (98.6928%), State Flux (84.849%), Api Exposure (80.0948%)
- **Heaviest Functions:** `map_async` (Compute Cores, Impact: 23.2), `get_mapped_range` (Many-Argument Workhorses, Impact: 13.7), `unmap` (Annotated Framework Methods, Impact: 6.0)

### 3. `wgpu/src/dispatch.rs` (RUST) -> Cumulative Risk: **609.77**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.41)
- **Magnitude:** 539.68 | **LOC:** 986 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (95.2555%), Api Exposure (83.0758%)
- **Heaviest Functions:** `deref` (Annotated Framework Methods, Impact: 3.5), `deref` (Annotated Framework Methods, Impact: 3.5), `deref_mut` (Annotated Framework Methods, Impact: 3.5)

### 4. `wgpu-hal/src/vulkan/conv.rs` (RUST) -> Cumulative Risk: **605.19**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.61)
- **Magnitude:** 698.74 | **LOC:** 1038 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.997%), Safety Score (89.7996%)
- **Heaviest Functions:** `map_texture_format` (Many-Argument Workhorses, Impact: 31.9), `map_buffer_usage_to_barrier` (Compute Cores, Impact: 21.7), `map_texture_usage_to_barrier` (Compute Cores, Impact: 20.1)

### 5. `wgpu-hal/src/dx12/device.rs` (RUST) -> Cumulative Risk: **595.15**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.45)
- **Magnitude:** 965.28 | **LOC:** 2655 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 25.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.0291%), Verification (80.0%), Api Exposure (75.6676%)
- **Heaviest Functions:** `create_pipeline_layout` (Many-Argument Workhorses, Impact: 121.0), `create_render_pipeline` (Many-Argument Workhorses, Impact: 74.7), `new` (Many-Argument Workhorses, Impact: 67.3)

### 6. `wgpu-hal/src/vulkan/adapter.rs` (RUST) -> Cumulative Risk: **593.81**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.33)
- **Magnitude:** 1517.58 | **LOC:** 3366 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 17.5%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.2286%), Churn (93.53%), Verification (80.0%)
- **Heaviest Functions:** `from_extensions_and_requested_features` (Many-Argument Workhorses, Impact: 187.4), `device_from_raw` (Many-Argument Workhorses, Impact: 187.0), `to_wgpu` (Many-Argument Workhorses, Impact: 111.6)

### 7. `naga/src/back/hlsl/ray.rs` (RUST) -> Cumulative Risk: **591.94**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 814.92 | **LOC:** 565 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.626%), Safety Score (80.4959%)
- **Heaviest Functions:** `write_initialize_function` (Many-Argument Workhorses, Impact: 247.2), `write_generate_intersection` (Many-Argument Workhorses, Impact: 96.0), `write_candidate_intersection_function` (Compute Cores, Impact: 79.5)

### 8. `wgpu-hal/src/metal/device.rs` (RUST) -> Cumulative Risk: **586.25**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +0.84)
- **Magnitude:** 733.78 | **LOC:** 2003 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 22.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Api Exposure (80.7795%), Verification (80.0%)
- **Heaviest Functions:** `create_render_pipeline` (Many-Argument Workhorses, Impact: 107.4), `load_shader` (Many-Argument Workhorses, Impact: 81.8), `create_pipeline_layout` (Many-Argument Workhorses, Impact: 44.8)

### 9. `wgpu-hal/src/dx12/command.rs` (RUST) -> Cumulative Risk: **578.24**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.48)
- **Magnitude:** 710.5 | **LOC:** 1860 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 37.5%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (83.6879%), Verification (80.0%)
- **Heaviest Functions:** `begin_render_pass` (Many-Argument Workhorses, Impact: 47.5), `transition_textures` (Many-Argument Workhorses, Impact: 36.1), `set_bind_group` (Many-Argument Workhorses, Impact: 28.0)

### 10. `wgpu-hal/src/vulkan/device.rs` (RUST) -> Cumulative Risk: **576.43**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.21)
- **Magnitude:** 1060.76 | **LOC:** 2827 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 23.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (91.8519%), State Flux (83.8207%), Verification (80.0%)
- **Heaviest Functions:** `create_render_pipeline` (Many-Argument Workhorses, Impact: 68.2), `compile_stage` (Many-Argument Workhorses, Impact: 57.0), `create_bind_group_layout` (Many-Argument Workhorses, Impact: 35.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `naga/src/back/msl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 5464.92 | **LOC:** 8257 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 16.7%
- **Risk Profile:** Cognitive Load (12.9125%), Tech Debt (8.7706%)
**Top Internal Functions/Classes:**
  * `put_expression` **(Many-Argument Workhorses)** (Impact: 761.0)
    * *Intent:* /// Emit code for the expression `expr_handle`. /// /// The `is_scoped` argument is true if the surr...
  * `write_functions` **(Many-Argument Workhorses)** (Impact: 729.6)
  * `put_block` **(Many-Argument Workhorses)** (Impact: 658.0)
  * `write_unpacking_function` **(Many-Argument Workhorses)** (Impact: 256.5)
  * `write_wrapped_image_sample` **(Many-Argument Workhorses)** (Impact: 161.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Amplified Cascading Flux:* 77 instances
* *High Risk Execution (weighted view):* 25
* *State Mutation (weighted view):* 254
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1951`, `structural_boundaries: 996`, `args: 148`, `func_start: 103`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 36`, `state_mutation: 100`, `dead_code: 27`, `planned_debt: 10`, `fragile_debt: 4`
* *Architecture:* `api: 27`, `import: 19`
* *Defense:* `safety: 106`, `doc: 364`, `test: 9`, `sync_locks: 13`, `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Baked, BoundsCheck, Error, ExternalTextureNameKey, FastHashMap, FastHashSet, Formatter, HandleSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/hlsl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3701.96 | **LOC:** 5021 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (24.7414%), Tech Debt (8.9217%)
**Top Internal Functions/Classes:**
  * `write_expr` **(Many-Argument Workhorses)** (Impact: 852.9)
    * *Intent:* /// Helper method to write expressions /// /// # Notes /// Doesn't add any newlines or leading/trail...
  * `write_stmt` **(Many-Argument Workhorses)** (Impact: 756.8)
    * *Intent:* /// Helper method used to write statements /// /// # Notes /// Always adds a newline
  * `write_function` **(Many-Argument Workhorses)** (Impact: 311.9)
    * *Intent:* /// Helper method used to write functions /// # Notes /// Ends in a newline
  * `write` **(Many-Argument Workhorses)** (Impact: 175.9)
  * `write_switch` **(Many-Argument Workhorses)** (Impact: 150.0)
    * *Intent:* /// Helper method used to write switches
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 48 instances
* *High Risk Execution (weighted view):* 22
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1417`, `structural_boundaries: 625`, `args: 98`, `func_start: 48`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 28`, `state_mutation: 65`, `dead_code: 11`, `planned_debt: 6`, `fragile_debt: 3`
* *Architecture:* `api: 59`, `import: 14`
* *Defense:* `safety: 138`, `doc: 96`, `test: 2`, `sync_locks: 31`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BackendResult, Baked, DerivativeControl, Error, ExternalTextureNameKey, FragmentEntryPoint, Handle, Module...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/wgsl/lower/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2680.88 | **LOC:** 4879 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (16.7001%), Tech Debt (10.7432%)
**Top Internal Functions/Classes:**
  * `call_builtin` **(Many-Argument Workhorses)** (Impact: 780.6)
    * *Intent:* /// Generate Naga IR for a call to a WGSL builtin function.
  * `statement` **(Many-Argument Workhorses)** (Impact: 194.3)
  * `texture_sample_helper` **(Many-Argument Workhorses)** (Impact: 108.4)
  * `expression_for_reference` **(Many-Argument Workhorses)** (Impact: 88.7)
  * `function` **(Many-Argument Workhorses)** (Impact: 81.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 110 instances
* *High Risk Execution (weighted view):* 10
* *State Mutation (weighted view):* 380
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 744`, `structural_boundaries: 1148`, `args: 161`, `func_start: 86`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 11`, `state_mutation: 160`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 9`
* *Architecture:* `api: 16`, `import: 20`
* *Defense:* `safety: 71`, `doc: 321`, `test: 2`, `sync_locks: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ExpectedToken, ExpressionContextType, FastHashMap, FastIndexMap, Handle, InvalidAssignmentType, Span, SubgroupGather...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/device/resource.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2140.7 | **LOC:** 5265 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 48.1%
- **Risk Profile:** Cognitive Load (10.1879%), Tech Debt (8.7075%)
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
* *Structure:* `branch: 710`, `structural_boundaries: 782`, `args: 174`, `func_start: 65`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 8`, `state_mutation: 82`, `dead_code: 10`, `planned_debt: 7`, `fragile_debt: 2`
* *Architecture:* `api: 87`, `concurrency: 6`, `import: 33`
* *Defense:* `safety: 74`, `doc: 182`, `test: 4`, `sync_locks: 46`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AttachmentData, BindGroup, BindGroupLateBufferBindingInfo, BindGroupLayout, BindGroupLayoutEntryError, Buffer, BufferInitTrackerAction, ColorStateError...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/spv/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1730.5 | **LOC:** 3849 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (12.7182%), Tech Debt (8.261%)
**Top Internal Functions/Classes:**
  * `write_function` **(Many-Argument Workhorses)** (Impact: 248.3)
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
* *Structure:* `branch: 406`, `structural_boundaries: 685`, `args: 130`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 17`, `state_mutation: 188`, `dead_code: 6`, `planned_debt: 3`, `fragile_debt: 1`
* *Architecture:* `api: 55`, `import: 17`
* *Defense:* `safety: 73`, `doc: 162`, `test: 4`, `sync_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BITS_PER_BYTE, BindingDecorations, BindingInfo, Block, BlockContext, CachedConstant, CachedExpressions, CooperativeType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/command/render.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1699.64 | **LOC:** 3865 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 45.0%
- **Risk Profile:** Cognitive Load (10.2418%), Tech Debt (32.7077%)
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
* *Structure:* `branch: 363`, `structural_boundaries: 506`, `args: 142`, `func_start: 92`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 2`, `state_mutation: 83`, `planned_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 33`
* *Architecture:* `api: 86`, `import: 11`
* *Defense:* `safety: 38`, `doc: 90`, `test: 1`, `sync_locks: 2`, `immutability_locks: 1`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ArcCommand, ArcPassTimestampWrites, BasePass, BindGroupStateChange, BufferAddress, BufferSize, BufferUsages, Color...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/wgsl/writer.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1699.12 | **LOC:** 2170 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 35.3%
- **Risk Profile:** Cognitive Load (19.1679%), Tech Debt (8.6335%)
**Top Internal Functions/Classes:**
  * `write_stmt` **(Many-Argument Workhorses)** (Impact: 559.1)
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
* *Structure:* `branch: 606`, `structural_boundaries: 224`, `args: 59`, `func_start: 29`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 8`, `state_mutation: 39`, `dead_code: 2`, `planned_debt: 5`
* *Architecture:* `api: 10`, `import: 15`
* *Defense:* `safety: 46`, `doc: 117`, `sync_locks: 12`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Baked, DerivativeControl, Handle, Module, NameKey, ShaderStage, Statement, ToString...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/spv/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1694.24 | **LOC:** 3275 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (12.1783%), Tech Debt (16.989%)
**Top Internal Functions/Classes:**
  * `parse_global_variable` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `parse` **(Compute Cores)** (Impact: 60.0)
  * `next_decoration` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `parse_type_image` **(Many-Argument Workhorses)** (Impact: 56.8)
  * `parse_expr_binary_op_sign_adjusted` **(Many-Argument Workhorses)** (Impact: 42.7)
    * *Intent:* /// A more complicated version of the binary op, /// where we force the operand to have the same typ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 101 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 374
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 478`, `structural_boundaries: 688`, `args: 95`, `func_start: 76`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 42`, `high_risk_execution: 5`, `state_mutation: 172`, `dead_code: 4`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 12`
* *Architecture:* `api: 14`, `import: 13`
* *Defense:* `safety: 57`, `doc: 241`, `test: 3`, `sync_locks: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FastHashMap, FastHashSet, FastIndexMap, Handle, Layouter, UniqueArena, alloc::borrow::ToOwned, alloc::vec...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/hlsl/help.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1640.98 | **LOC:** 2333 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.0805%), Tech Debt (12.3036%)
**Top Internal Functions/Classes:**
  * `write_wrapped_image_query_function` **(Many-Argument Workhorses)** (Impact: 119.7)
  * `write_wrapped_image_sample_function` **(Many-Argument Workhorses)** (Impact: 119.3)
  * `write_wrapped_constructor_function` **(Many-Argument Workhorses)** (Impact: 117.4)
  * `write_wrapped_math_functions` **(Many-Argument Workhorses)** (Impact: 106.7)
  * `write_wrapped_binary_ops` **(Many-Argument Workhorses)** (Impact: 103.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 35 instances
* *High Risk Execution (weighted view):* 23
* *State Mutation (weighted view):* 110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 608`, `structural_boundaries: 268`, `args: 46`, `func_start: 37`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 26`, `state_mutation: 40`, `dead_code: 3`, `planned_debt: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 68`, `import: 14`
* *Defense:* `safety: 24`, `doc: 73`, `test: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BackendResult, DIV_FUNCTION, EXTRACT_BITS_FUNCTION, F2I32_FUNCTION, F2I64_FUNCTION, F2U32_FUNCTION, F2U64_FUNCTION, IMAGE_LOAD_EXTERNAL_FUNCTION...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/proc/constant_evaluator.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1633.58 | **LOC:** 4774 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 35.3%
- **Risk Profile:** Cognitive Load (7.4028%), Tech Debt (12.1973%)
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
* *Structure:* `branch: 516`, `structural_boundaries: 758`, `args: 246`, `func_start: 99`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 66`, `high_risk_execution: 17`, `state_mutation: 107`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 13`
* *Architecture:* `api: 18`, `import: 18`
* *Defense:* `safety: 40`, `doc: 230`, `test: 55`, `sync_locks: 3`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ArraySize, BinaryOperator, Constant, ConstantEvaluator, Expression, ExpressionKindTracker, FastHashMap, FromPrimitive...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-hal/src/vulkan/adapter.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1517.58 | **LOC:** 3366 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 17.5%
- **Risk Profile:** Cognitive Load (22.1819%), Tech Debt (8.8633%)
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
* *Structure:* `branch: 337`, `structural_boundaries: 393`, `args: 140`, `func_start: 39`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 191`, `dead_code: 8`, `planned_debt: 9`
* *Architecture:* `api: 23`, `import: 10`
* *Defense:* `safety: 69`, `doc: 196`, `test: 2`, `sync_locks: 7`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AllocationSizes, Features, alloc::borrow::ToOwned, ash::ext, boxed::Box, collections::BTreeMap, core::ffi::CStr, crate::TextureFormatCapabilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/wgsl/parse/mod.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1388.78 | **LOC:** 2409 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 61.9%
- **Risk Profile:** Cognitive Load (18.1048%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `global_decl` **(Many-Argument Workhorses)** (Impact: 235.8)
  * `statement` **(Many-Argument Workhorses)** (Impact: 186.7)
  * `parse` **(Many-Argument Workhorses)** (Impact: 77.5)
  * `function_decl` **(Many-Argument Workhorses)** (Impact: 55.3)
  * `variable_or_value_or_func_call_or_variable_updating_statement` **(Many-Argument Workhorses)** (Impact: 54.4)
    * *Intent:* /// Parses variable_or_value_statement, func_call_statement and variable_updating_statement. /// ///...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 176
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 445`, `structural_boundaries: 534`, `args: 87`, `func_start: 49`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 71`, `high_risk_execution: 2`, `state_mutation: 74`
* *Architecture:* `api: 13`, `import: 13`
* *Defense:* `safety: 19`, `doc: 90`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DiagnosticFilter, DiagnosticFilterMap, DiagnosticFilterNode, EnableExtensions, Error, ExpectedToken, FastHashSet, FastIndexSet...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/spv/block.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1238.76 | **LOC:** 4232 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (8.1621%), Tech Debt (8.6653%)
**Top Internal Functions/Classes:**
  * `write_block` **(Many-Argument Workhorses)** (Impact: 224.2)
    * *Intent:* /// Use `label_id` as the label for the SPIR-V entry point block. /// /// If control reaches the end...
  * `cache_expression_value` **(Many-Argument Workhorses)** (Impact: 219.3)
    * *Intent:* /// Cache an expression for a value.
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
* *Structure:* `branch: 303`, `structural_boundaries: 601`, `args: 55`, `func_start: 25`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 44`, `state_mutation: 189`, `dead_code: 11`, `planned_debt: 4`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 41`, `doc: 212`, `test: 1`, `sync_locks: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Block, BlockContext, DerivativeControl, Dimension, Error, IdGenerator, Instruction, LocalType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/glsl/builtins.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1154.9 | **LOC:** 2376 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (15.282%), Tech Debt (9.6319%)
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
* *Risk/State:* `high_risk_execution: 23`, `state_mutation: 97`, `planned_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 3`
* *Defense:* `safety: 34`, `doc: 37`, `test: 2`, `sync_locks: 5`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DerivativeAxis, DerivativeControl, Error, ErrorKind, Expression, Frontend, FunctionDeclaration, FunctionKind...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu/src/backend/wgpu_core.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1115.9 | **LOC:** 4037 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (5.9783%), Tech Debt (9.7604%)
**Top Internal Functions/Classes:**
  * `create_bind_group` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `pop_error_scope` **(Defensive Guards)** (Impact: 21.0)
  * `handle_error_or_return_handler` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* /// Deliver the error to /// /// * the innermost error scope, if any, or /// * the uncaptured error ...
  * `handle_error_inner` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `create_mesh_pipeline` **(Many-Argument Workhorses)** (Impact: 11.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 221`, `structural_boundaries: 590`, `args: 290`, `func_start: 212`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 8`, `state_mutation: 15`, `duplicate_logic: 4`
* *Architecture:* `api: 164`, `concurrency: 2`, `import: 16`
* *Defense:* `safety: 106`, `doc: 23`, `test: 1`, `sync_locks: 20`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.787
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.003413
  * `Imports (Out-Degree: 1):` BindingResource, Blas, BlasCompactCallback, Borrowed, BufferBinding, BufferDescriptor, BufferMappedRangeInterface, CompilationInfo...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `wgpu-hal/src/vulkan/device.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1060.76 | **LOC:** 2827 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 23.1%
- **Risk Profile:** Cognitive Load (16.3966%), Tech Debt (8.0352%)
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
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 6`, `state_mutation: 104`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 58`, `import: 9`
* *Defense:* `safety: 60`, `doc: 48`, `sync_locks: 20`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MaybeUninit, RawTlasInstance, alloc::borrow::ToOwned, arrayvec::ArrayVec, ash::ext, collections::BTreeMap, core::
    ffi::CStr, crate::TlasInstance...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu/src/backend/webgpu.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1055.22 | **LOC:** 4059 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 22.6%
- **Risk Profile:** Cognitive Load (6.1483%), Tech Debt (99.9834%)
**Top Internal Functions/Classes:**
  * `begin_render_pass` **(Defensive Guards)** (Impact: 29.9)
  * `create_render_pipeline` **(Defensive Guards)** (Impact: 21.1)
  * `create_bind_group_layout` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `create_shader_module` **(Many-Argument Workhorses)** (Impact: 16.9)
  * `create_bind_group` **(Many-Argument Workhorses)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 42
* *Memory Alloc (weighted view):* 7
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 590`, `args: 277`, `func_start: 235`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 49`, `state_mutation: 12`, `dead_code: 3`, `planned_debt: 11`, `duplicate_logic: 66`, `unreferenced_by_name: 88`
* *Architecture:* `api: 53`, `concurrency: 12`, `import: 35`
* *Defense:* `safety: 75`, `doc: 81`, `sync_locks: 1`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Blas, BlasCompactCallback, JsCast, OnceCell, Poll, RefCell, SurfaceTargetUnsafe, Tlas...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/tests/naga/wgsl_errors.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 965.44 | **LOC:** 5255 | **CtrlFlow:** 6.8% | **Authorship Centralization:** 35.5%
- **Risk Profile:** Cognitive Load (3.3259%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `bad_for_initializer` **(Compute Cores)** (Impact: 189.4)
  * `too_many_unclosed_loops` **(Compute Cores)** (Impact: 138.7)
  * `invalid_functions` **(I/O & Config Routines)** (Impact: 16.8)
  * `subgroup_capability` **(I/O & Config Routines)** (Impact: 16.0)
  * `reserved_keyword` **(I/O & Config Routines)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 383`, `args: 389`, `func_start: 313`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 19`, `state_mutation: 28`, `dead_code: 6`, `planned_debt: 2`, `unreferenced_by_name: 149`
* *Architecture:* `concurrency: 4`, `import: 3`
* *Defense:* `doc: 63`, `test: 169`, `sync_locks: 10`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Capabilities, ImplementedEnableExtension, ValidationError, VaryingError, front::wgsl::EnableExtension, naga::
    compact::KeepUnused, naga::valid::TypeError, valid::self
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-hal/src/dx12/device.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 965.28 | **LOC:** 2655 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (18.741%), Tech Debt (9.0841%)
**Top Internal Functions/Classes:**
  * `create_pipeline_layout` **(Many-Argument Workhorses)** (Impact: 121.0)
  * `create_render_pipeline` **(Many-Argument Workhorses)** (Impact: 74.7)
  * `new` **(Many-Argument Workhorses)** (Impact: 67.3)
  * `load_shader` **(Many-Argument Workhorses)** (Impact: 55.0)
    * *Intent:* /// When generating the vertex shader, the fragment stage must be passed if it exists! /// Otherwise...
  * `create_bind_group` **(Many-Argument Workhorses)** (Impact: 52.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 229`, `structural_boundaries: 350`, `args: 74`, `func_start: 53`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 3`, `state_mutation: 97`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 1`
* *Architecture:* `api: 50`, `import: 12`
* *Defense:* `safety: 47`, `doc: 3`, `test: 6`, `sync_locks: 15`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` AccelerationStructureEntries, D3D12Lib, DCompLib, Direct3D12::D3D12_RESOURCE_FLAG_RAYTRACING_ACCELERATION_STRUCTURE
            Flags: Direct3D12::D3D12_RESOURCE_FLAG_ALLOW_UNORDERED_ACCESS, Dxgi, DynamicStorageBufferOffsets, Event, Graphics::Direct3D12...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/glsl/functions.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 922.86 | **LOC:** 1624 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (14.834%), Tech Debt (12.9677%)
**Top Internal Functions/Classes:**
  * `function_call` **(Many-Argument Workhorses)** (Impact: 176.1)
  * `constructor_single` **(Many-Argument Workhorses)** (Impact: 95.6)
  * `process_lhs_argument` **(Many-Argument Workhorses)** (Impact: 80.5)
    * *Intent:* /// Processes a function call argument that appears in place of an output /// parameter.
  * `matrix_one_arg` **(Many-Argument Workhorses)** (Impact: 79.3)
  * `constructor_many` **(Many-Argument Workhorses)** (Impact: 46.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 219`, `structural_boundaries: 246`, `args: 33`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 86`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 21`, `doc: 58`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AddressSpace, Block, EntryPoint, ErrorKind, ExprPos, Expression, Frontend, Function...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/spv/next_block.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 873.08 | **LOC:** 3129 | **CtrlFlow:** 21.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (23.4438%), Tech Debt (12.4515%)
**Top Internal Functions/Classes:**
  * `next_block` **(Many-Argument Workhorses)** (Impact: 472.6)
    * *Intent:* /// Add the next SPIR-V block's contents to `block_ctx`. /// /// Except for the function's entry blo...
  * `make_index_literal` **(Many-Argument Workhorses)** (Impact: 6.8)
  * `merger` **(Compute Cores)** (Impact: 4.1)
    * *Intent:* // Extend `body` with the correct form for a branch to `target`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 71 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 334
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 588`, `structural_boundaries: 688`, `args: 59`, `func_start: 3`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `high_risk_execution: 6`, `state_mutation: 192`, `dead_code: 1`, `planned_debt: 6`, `fragile_debt: 4`, `unreferenced_by_name: 1`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 32`, `doc: 8`, `test: 3`, `sync_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` BlockContext, Body, BodyFragment, Constant, Error, Frontend, LookupExpression, LookupHelper...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `wgpu-core/src/device/global.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 835.08 | **LOC:** 2127 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 56.0%
- **Risk Profile:** Cognitive Load (4.968%), Tech Debt (97.7192%)
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
* *Structure:* `branch: 185`, `structural_boundaries: 453`, `args: 98`, `func_start: 72`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 27`, `planned_debt: 2`, `unreferenced_by_name: 68`
* *Architecture:* `api: 68`, `concurrency: 2`, `import: 9`
* *Defense:* `safety: 61`, `doc: 106`, `test: 1`, `sync_locks: 40`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Adapter, AdapterId, BindGroupEntry, BindingResource, BufferAccessError, BufferAccessResult, BufferBinding, BufferMapOperation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/back/hlsl/ray.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 814.92 | **LOC:** 565 | **CtrlFlow:** 48.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.4444%), Tech Debt (55.2092%)
**Top Internal Functions/Classes:**
  * `write_initialize_function` **(Many-Argument Workhorses)** (Impact: 247.2)
  * `write_generate_intersection` **(Many-Argument Workhorses)** (Impact: 96.0)
  * `write_candidate_intersection_function` **(Compute Cores)** (Impact: 79.5)
  * `write_committed_intersection_function` **(Compute Cores)** (Impact: 73.9)
  * `write_proceed` **(Many-Argument Workhorses)** (Impact: 65.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 35 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 38`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 35`, `fragile_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 8`, `import: 4`
* *Defense:* `safety: 1`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Baked, Handle, Level, ToString, TypeInner, alloc::
    format, core::fmt::Write, crate::
    back::hlsl::BackendResult...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/front/glsl/context.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 807.04 | **LOC:** 1550 | **CtrlFlow:** 17.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (13.0194%), Tech Debt (0.0%)
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
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 42`, `dead_code: 3`
* *Architecture:* `api: 41`, `import: 4`
* *Defense:* `safety: 23`, `doc: 75`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AddressSpace, Arena, BinaryOperator, Block, ErrorKind, Expression, FastHashMap, Frontend...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `naga/src/valid/function.rs` (RUST | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 784.44 | **LOC:** 1933 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (16.6175%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `validate_block_impl` **(Many-Argument Workhorses)** (Impact: 340.6)
  * `validate_atomic` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `validate_function` **(Many-Argument Workhorses)** (Impact: 60.0)
  * `validate_call` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `validate_subgroup_gather` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 295`, `args: 65`, `func_start: 17`, `class_start: 8`
* *Risk/State:* `state_mutation: 35`, `dead_code: 2`
* *Architecture:* `api: 6`, `import: 12`
* *Defense:* `safety: 29`, `doc: 3`, `sync_locks: 27`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.067
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ExpressionError, FunctionInfo, HandleSet, MapErrWithSpan, ModuleInfo, Statement, TypeInner, UniformityRequirements...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `wgpu-hal/src/metal/mod.rs` -> Churn: **85.67%** | Cog Load: 8.853% | Debt: 57.8%
- `wgpu-core/src/device/global.rs` -> Churn: **82.06%** | Cog Load: 4.968% | Debt: 97.7192%
- `wgpu/src/backend/webgpu.rs` -> Churn: **76.39%** | Cog Load: 6.1483% | Debt: 99.9834%
- `wgpu-hal/src/noop/mod.rs` -> Churn: **69.6%** | Cog Load: 5.948% | Debt: 99.9997%
- `wgpu-hal/src/lib.rs` -> Churn: **68.07%** | Cog Load: 2.992% | Debt: 99.9985%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `naga/src/front/glsl/builtins.rs` -> **Connor Fitzgerald** (100.0% isolated ownership) | Magnitude: 1154.9
- `naga/src/back/hlsl/ray.rs` -> **Vecvec** (100.0% isolated ownership) | Magnitude: 814.92
- `wgpu-hal/src/vulkan/conv.rs` -> **Connor Fitzgerald** (100.0% isolated ownership) | Magnitude: 698.74
- `naga/src/back/spv/ray/query.rs` -> **Vecvec** (100.0% isolated ownership) | Magnitude: 414.92
- `naga/src/front/glsl/parser/declarations.rs` -> **06wj** (100.0% isolated ownership) | Magnitude: 407.46

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `wgpu-types/src/texture/format.rs` -> **Severity: 0.915** (Embedded: 0.0142 * Error Risk: 64.316%)
- `benches/src/iter.rs` -> **Severity: 0.912** (Embedded: 0.0159 * Error Risk: 57.2305%)
- `wgpu-core/src/id.rs` -> **Severity: 0.559** (Embedded: 0.0095 * Error Risk: 58.9764%)
- `wgpu/src/backend/wgpu_core.rs` -> **Severity: 0.151** (Embedded: 0.0034 * Error Risk: 44.3209%)
- `wgpu-hal/src/dx12/shader_compilation.rs` -> **Severity: 0.136** (Embedded: 0.0023 * Error Risk: 59.655%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `benches/src/iter.rs` -> **Severity: 1376.1** (Blast Radius: 13.761 * Doc Risk: 100.0%)
- `naga/fuzz/fuzz_targets/ir.rs` -> **Severity: 741.4** (Blast Radius: 7.414 * Doc Risk: 100.0%)
- `wgpu-core/src/id.rs` -> **Severity: 604.506** (Blast Radius: 9.863 * Doc Risk: 61.2903%)
- `naga/xtask/src/fs.rs` -> **Severity: 378.7** (Blast Radius: 3.787 * Doc Risk: 100.0%)
- `wgpu/src/backend/wgpu_core.rs` -> **Severity: 368.115** (Blast Radius: 3.787 * Doc Risk: 97.205%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
