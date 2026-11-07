# ARCHITECTURAL_BRIEF: mach
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/hexops/mach.git` |
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
- **Scope:** 133 analyzed artifact(s), 58356 LOC.
- **Load-bearing artifact:** `src/sysgpu/sysgpu/main.zig` -- 46 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/sysgpu/sysgpu/main.zig` -- pulls in 28 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/sysgpu/shader/AstGen.zig` at magnitude 1923.08 (structural weight, not risk).
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
| Total Artifacts | 185 |
| Analyzed Artifacts (Scanned) | 133 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 52 |
| Total LOC | 58356 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 71.9% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6242 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2605 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 62.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.1161 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 125 | 58340 | 94.0% |
| MARKDOWN | 3 | 0 | 2.3% |
| PLAINTEXT | 2 | 0 | 1.5% |
| C | 2 | 12 | 1.5% |
| SHELL | 1 | 4 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 133 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Large Core Modules (2) 23%, State Mutators Files 19%, Data / Markup / Trivial 8%, Many-Argument Workhorses Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 128 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 52*

**Composition by Extension & Reason:**
- `.wgsl`: 31x Unsupported Format (.wgsl), 4x Excluded (Unsupported Extension: '.wgsl')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 7424 LOC)
- `.manifest`: 1x Unsupported Format (.manifest)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 79.4 | 11.1 | 6.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.0 | 37.9 | 48.1 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.1 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 55.5 | 59.3 | 100.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 7.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 74.7 | 93.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 2960 | 76 | 45 | `src/sysgpu/opengl/proc.zig` |
| cleanup | 633 | 53 | 10 | `src/sysgpu/vulkan.zig` |
| guards | 6621 | 96 | 136 | `src/sysgpu/shader/AstGen.zig` |
| danger | 4039 | 90 | 48 | `src/sysgpu/opengl/proc.zig` |
| concurrency | 121 | 16 | 2 | `src/graph.zig` |
| connectivity | 4425 | 124 | 64 | `src/win32.zig` |
| io | 92 | 17 | 1 | `src/sysaudio/alsa.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 53 | 5 | 0 | `src/sysaudio/alsa.zig` |
| time | 6 | 4 | 0 | `src/sysaudio/alsa.zig` |
| serialization | 1 | 1 | 0 | `src/sysgpu/tools/gen_spirv_spec.zig` |
| regex | 0 | 0 | 0 | - |
| events | 35 | 17 | 1 | `src/sysaudio/tests/sine.zig` |
| tests | 295 | 26 | 3 | `src/math/vec.zig` |
| docs | 1433 | 56 | 28 | `src/sysgpu/shader/Ast.zig` |
| debt | 454 | 61 | 12 | `src/sysgpu/d3d12.zig` |
| mutation | 13607 | 122 | 221 | `src/win32.zig` |
| dead_code | 168 | 30 | 2 | `src/sysgpu/shader/test.zig` |
| credential | 3 | 1 | 0 | `build.zig.zon` |
| threat | 1 | 1 | 0 | `src/gfx/font/main.zig` |
| ml_ai | 850 | 68 | 17 | `src/sysgpu/shader/AstGen.zig` |
| ui | 381 | 37 | 14 | `examples/hardware-check/App.zig` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/sysaudio/alsa.zig` (Hits: 25)
- `src/core/linux/Wayland.zig` (Hits: 16)
- `src/core/linux/X11.zig` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **main.zig** (`src/sysgpu/sysgpu/main.zig`) — 46 inbound connections
2. **main.zig** (`src/main.zig`) — 26 inbound connections
3. **interface.zig** (`src/sysgpu/sysgpu/interface.zig`) — 25 inbound connections
4. **bind_group.zig** (`src/sysgpu/sysgpu/bind_group.zig`) — 12 inbound connections
5. **main.zig** (`src/sysaudio/main.zig`) — 9 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/sysgpu/sysgpu/main.zig`) — 28 outbound dependencies
2. **device.zig** (`src/sysgpu/sysgpu/device.zig`) — 20 outbound dependencies
3. **main.zig** (`src/main.zig`) — 15 outbound dependencies
4. **Wayland.zig** (`src/core/linux/Wayland.zig`) — 14 outbound dependencies
5. **X11.zig** (`src/core/linux/X11.zig`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `renderOpcodes` **(Many-Argument Workhorses)** (@ `src/sysgpu/tools/gen_spirv_spec.zig`) -> Impact: **189.2** | LOC: 430
- `genCall` **(Many-Argument Workhorses)** (@ `src/sysgpu/shader/AstGen.zig`) -> Impact: **187.6** | LOC: 552
- `renderOperandKind` **(Defensive Guards)** (@ `src/sysgpu/tools/gen_spirv_spec.zig`) -> Impact: **177.2** | LOC: 496
- `peek` **(Compute Cores)** (@ `src/sysgpu/shader/Tokenizer.zig`) -> Impact: **96.5** | LOC: 374
- `Printer` **(Defensive Guards)** (@ `src/sysgpu/shader/print_air.zig`) -> Impact: **94.8** | LOC: 511
- `addFunction` **(Many-Argument Workhorses)** (@ `src/sysgpu/utils.zig`) -> Impact: **89.4** | LOC: 179
- `wndProc` **(Many-Argument Workhorses)** (@ `src/core/Windows.zig`) -> Impact: **88.8** | LOC: 256
- `execute` **(Defensive Guards)** (@ `src/sysgpu/opengl.zig`) -> Impact: **87.3** | LOC: 332
  * *Intent:* // Internal
- `Objects` **(Many-Argument Workhorses)** (@ `src/module.zig`) -> Impact: **84.6** | LOC: 444
- `emitBinaryAir` **(Many-Argument Workhorses)** (@ `src/sysgpu/shader/codegen/spirv.zig`) -> Impact: **78.3** | LOC: 166

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/sysgpu` | 10 | 6360.46 | 14.83% | 5.7% |
| `src/sysgpu/shader` | 11 | 3964.86 | 12.38% | 5.39% |
| `src` | 11 | 3205.18 | 14.07% | 19.49% |
| `src/sysgpu/sysgpu` | 28 | 2741.14 | 4.03% | 0.29% |
| `src/sysgpu/shader/codegen` | 4 | 2416.58 | 9.85% | 16.74% |
| `src/sysaudio` | 11 | 2357.58 | 14.74% | 5.26% |
| `src/math` | 6 | 1392.6 | 7.94% | 8.85% |
| `src/sysgpu/opengl` | 3 | 1029.02 | 31.26% | 0.0% |
| `src/core/linux` | 3 | 666.64 | 35.07% | 10.22% |
| `src/core` | 4 | 619.22 | 9.53% | 8.06% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/testing.zig` -> **100.0%** Exposure
- `src/gfx/font/native/Font.zig` -> **99.708%** Exposure
- `src/gfx/font/main.zig` -> **97.7023%** Exposure
- `src/sysaudio/pipewire/sysaudio.c` -> **81.7574%** Exposure
- `src/gfx/Text.zig` -> **72.9284%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/sysgpu/opengl/proc.zig` -> **100.0%** Exposure
- `src/sysgpu/shader/Tokenizer.zig` -> **100.0%** Exposure
- `src/time/Frequency.zig` -> **100.0%** Exposure
- `src/math/collision.zig` -> **99.9475%** Exposure
- `src/sysgpu/gpu_allocator.zig` -> **99.9315%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/math/vec.zig` -> **0** Orphaned Functions | **8** Duplicates
- `src/testing.zig` -> **0** Orphaned Functions | **5** Duplicates
- `src/gfx/font/native/Font.zig` -> **4** Orphaned Functions | **0** Duplicates
- `build.zig` -> **2** Orphaned Functions | **0** Duplicates
- `src/win32.zig` -> **0** Orphaned Functions | **2** Duplicates

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
- **Unknown Dependencies:** `496` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/sysgpu/shader/AstGen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.517)
- **Top Global Matches:** file_cluster_4: 7.517, file_cluster_12: 11.0, file_cluster_15: 12.22
- **Magnitude:** 1923.08 | **LOC:** 4569 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 5.084; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (70.1%), Guard Balance (formerly Safety Score) (40.8%), Connectivity (formerly Api Exposure) (18.7%), Complexity Load (formerly Cognitive Load) (13.9%)
- **Documentation Coverage:** 97.9592% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genCall` **(Many-Argument Workhorses)** (Impact: 187.6)
  * `genFn` **(Many-Argument Workhorses)** (Impact: 77.4)
  * `genBinary` **(Many-Argument Workhorses)** (Impact: 73.0)
  * `genBitcast` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `genTextureSampleBuiltin` **(Many-Argument Workhorses)** (Impact: 60.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 542`, `structural_boundaries: 536`, `args: 96`, `func_start: 96`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 124`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `api: 3`, `import: 6`
* *Defense:* `safety: 645`, `doc: 3`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.084
  * `Choke Point (Betweenness):` 0.000135 | `Ripple Effect (Closeness):` 0.153093
  * `Imports (Out-Degree: 4):` Air.zig, Ast.zig, ErrorList.zig, Token.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/d3d12.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.314)
- **Top Global Matches:** file_cluster_12: 8.314, file_cluster_7: 8.992, file_cluster_5: 10.032
- **Magnitude:** 1617.7 | **LOC:** 4160 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 5.232; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (85.0%), Connectivity (formerly Api Exposure) (72.5%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (20.2%)
- **Documentation Coverage:** 91.075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 57.5)
  * `init` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `init` **(Defensive Guards)** (Impact: 40.7)
  * `init` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `init` **(Many-Argument Workhorses)** (Impact: 30.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 96 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 334`, `args: 171`, `func_start: 171`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 229`, `high_risk_execution: 7`, `state_mutation: 167`, `dead_code: 1`, `planned_debt: 29`
* *Architecture:* `api: 201`, `import: 9`
* *Defense:* `safety: 307`, `doc: 4`, `cleanup: 94`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.232
  * `Choke Point (Betweenness):` 0.016571 | `Ripple Effect (Closeness):` 0.196103
  * `Imports (Out-Degree: 8):` builtin, c.zig, conv.zig, gpu_allocator.zig, limits.zig, shader.zig, std, main.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/win32.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.842)
- **Top Global Matches:** file_cluster_12: 8.842, file_cluster_7: 10.047, file_cluster_5: 10.226
- **Magnitude:** 1509.76 | **LOC:** 4254 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 5.849; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%), Debt Markers (formerly Tech Debt) (14.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loword` **(Type Conversions)** (Impact: 9.0)
  * `pxFromPt` **(Generic / Templated Code)** (Impact: 6.3)
  * `ptFromPx` **(Generic / Templated Code)** (Impact: 6.3)
  * `hiword` **(Type Conversions)** (Impact: 6.2)
  * `hexVal` **(Type Conversions)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 171`, `args: 403`, `func_start: 181`, `class_start: 159`
* *Risk/State:* `safety_bypasses: 154`, `high_risk_execution: 1`, `state_mutation: 1`, `dead_code: 4`, `planned_debt: 27`, `duplicate_logic: 2`
* *Architecture:* `io: 2`, `api: 1028`, `import: 135`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.849
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.123737
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sysgpu/sysgpu/interface.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 13.742)
- **Top Global Matches:** file_cluster_7: 13.742, file_cluster_12: 14.304, file_cluster_5: 14.556
- **Magnitude:** 1341.88 | **LOC:** 2696 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **4**; blast radius 62.765; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (8.1%)
- **Documentation Coverage:** 99.0751% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Export` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* /// Exports C ABI function declarations for the given sysgpu.Interface implementation.
  * `assertDecl` **(Generic / Templated Code)** (Impact: 6.2)
  * `renderPassEncoderSetViewport` **(Many-Argument Workhorses)** (Impact: 3.3)
  * `bufferMapAsync` **(Parameter Forwarders)** (Impact: 3.1)
  * `commandEncoderCopyBufferToBuffer` **(Parameter Forwarders)** (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 276`, `args: 646`, `func_start: 432`
* *Risk/State:* `safety_bypasses: 216`, `planned_debt: 3`
* *Architecture:* `api: 433`, `import: 4`
* *Defense:* `doc: 7`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.765
  * `Choke Point (Betweenness):` 0.189943 | `Ripple Effect (Closeness):` 0.243933
  * `Imports (Out-Degree: 2):` main.zig, builtin, main.zig, root
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `src/sysgpu/vulkan.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.708)
- **Top Global Matches:** file_cluster_12: 7.708, file_cluster_7: 8.787, file_cluster_5: 10.076
- **Magnitude:** 1336.92 | **LOC:** 3622 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 8.771; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.2%), Mutation Surface (formerly State Flux) (77.8%), Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (17.6%)
- **Documentation Coverage:** 91.075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 44.7)
  * `findBestAllocator` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `init` **(Defensive Guards)** (Impact: 35.5)
  * `init` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `init` **(Type Conversions)** (Impact: 25.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 44 instances
* *Amplified Cascading Flux:* 70 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 18
* *State Mutation (weighted view):* 276
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 244`, `structural_boundaries: 239`, `args: 150`, `func_start: 150`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 162`, `high_risk_execution: 8`, `state_mutation: 136`, `planned_debt: 13`
* *Architecture:* `api: 170`, `import: 10`
* *Defense:* `safety: 360`, `doc: 1`, `test: 1`, `sync_locks: 6`, `cleanup: 96`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.771
  * `Choke Point (Betweenness):` 0.13466 | `Ripple Effect (Closeness):` 0.199361
  * `Imports (Out-Degree: 8):` main.zig, builtin, limits.zig, shader.zig, std, main.zig, utils.zig, vulkan...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sysgpu/opengl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.695)
- **Top Global Matches:** file_cluster_12: 8.695, file_cluster_7: 9.788, file_cluster_5: 10.661
- **Magnitude:** 1056.14 | **LOC:** 2635 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 5.232; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (78.8%), Connectivity (formerly Api Exposure) (71.8%), Guard Balance (formerly Safety Score) (59.0%), Complexity Load (formerly Cognitive Load) (20.4%)
- **Documentation Coverage:** 91.075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execute` **(Defensive Guards)** (Impact: 87.3)
    * *Intent:* // Internal
  * `init` **(Many-Argument Workhorses)** (Impact: 57.2)
  * `applyState` **(Many-Argument Workhorses)** (Impact: 35.9)
  * `init` **(Defensive Guards)** (Impact: 17.7)
  * `messageCallback` **(Many-Argument Workhorses)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 23 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 236`, `args: 126`, `func_start: 126`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 127`, `high_risk_execution: 4`, `state_mutation: 115`, `planned_debt: 14`
* *Architecture:* `api: 143`, `import: 9`
* *Defense:* `safety: 201`, `test: 1`, `cleanup: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.232
  * `Choke Point (Betweenness):` 0.016455 | `Ripple Effect (Closeness):` 0.196103
  * `Imports (Out-Degree: 8):` builtin, limits.zig, c.zig, conv.zig, proc.zig, shader.zig, std, main.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/metal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.803)
- **Top Global Matches:** file_cluster_12: 7.803, file_cluster_7: 9.461, file_cluster_5: 10.301
- **Magnitude:** 1035.42 | **LOC:** 2236 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 5.232; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (74.1%), Mutation Surface (formerly State Flux) (74.0%), Guard Balance (formerly Safety Score) (49.3%), Complexity Load (formerly Cognitive Load) (20.1%)
- **Documentation Coverage:** 91.075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 61.5)
  * `setBindGroup` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `init` **(Many-Argument Workhorses)** (Impact: 25.4)
  * `init` **(Defensive Guards)** (Impact: 24.5)
  * `buildBindings` **(Defensive Guards)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 38 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 22
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 194`, `args: 133`, `func_start: 133`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 81`, `high_risk_execution: 6`, `state_mutation: 80`, `planned_debt: 22`
* *Architecture:* `api: 150`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 212`, `test: 1`, `cleanup: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.232
  * `Choke Point (Betweenness):` 0.006335 | `Ripple Effect (Closeness):` 0.196103
  * `Imports (Out-Degree: 6):` limits.zig, conv.zig, objc, shader.zig, std, main.zig, utils.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/codegen/spirv.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.447)
- **Top Global Matches:** file_cluster_12: 8.447, file_cluster_4: 8.774, file_cluster_5: 9.657
- **Magnitude:** 936.6 | **LOC:** 2826 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (32.7%), Connectivity (formerly Api Exposure) (23.1%), Mutation Surface (formerly State Flux) (17.8%), Debt Markers (formerly Tech Debt) (10.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitBinaryAir` **(Many-Argument Workhorses)** (Impact: 78.3)
  * `emitFn` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `emitVarProto` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `emitFnVars` **(Defensive Guards)** (Impact: 28.5)
  * `emitBinaryIntrinsic` **(Defensive Guards)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 199`, `args: 68`, `func_start: 68`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 62`, `high_risk_execution: 5`, `state_mutation: 29`, `dead_code: 2`, `planned_debt: 20`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 578`, `doc: 8`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.417
  * `Choke Point (Betweenness):` 0.005552 | `Ripple Effect (Closeness):` 0.145758
  * `Imports (Out-Degree: 3):` Air.zig, CodeGen.zig, Section.zig, spec.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/opengl/proc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 16.882)
- **Top Global Matches:** file_cluster_14: 16.882, file_cluster_7: 19.082, file_cluster_5: 20.36
- **Magnitude:** 872.96 | **LOC:** 1461 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.4; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loadVersion` **(Type Conversions)** (Impact: 51.5)
  * `removeOptional` **(Generic / Templated Code)** (Impact: 4.5)
  * `load` **(Type Conversions)** (Impact: 1.7)
  * `getProcAddress` **(Parameter Forwarders)** (Impact: 1.6)
  * `load` **(Type Conversions)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 56 instances
* *State Mutation (weighted view):* 774
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 3`, `args: 7`, `func_start: 7`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 662`, `state_mutation: 662`
* *Architecture:* `api: 8`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.002622 | `Ripple Effect (Closeness):` 0.153081
  * `Imports (Out-Degree: 2):` main.zig, c.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/Parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.464)
- **Top Global Matches:** file_cluster_4: 7.464, file_cluster_12: 7.96, file_cluster_15: 8.543
- **Magnitude:** 794.24 | **LOC:** 2055 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 4.43; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (66.5%), Guard Balance (formerly Safety Score) (28.1%), Connectivity (formerly Api Exposure) (17.6%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `attribute` **(Defensive Guards)** (Impact: 30.8)
  * `statement` **(Defensive Guards)** (Impact: 29.9)
  * `switchStatement` **(Defensive Guards)** (Impact: 27.3)
  * `typeSpecifierWithoutIdent` **(Defensive Guards)** (Impact: 21.8)
  * `parameterizeTemplates` **(Compute Cores)** (Impact: 18.9)
    * *Intent:* // Based on https://gpuweb.github.io/gpuweb/wgsl/#template-lists-sec
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 144
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 270`, `args: 74`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 54`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 542`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.43
  * `Choke Point (Betweenness):` 0.00113 | `Ripple Effect (Closeness):` 0.191288
  * `Imports (Out-Degree: 4):` Ast.zig, ErrorList.zig, Token.zig, std, wgsl.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sysgpu/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 12.225)
- **Top Global Matches:** file_cluster_14: 12.225, file_cluster_7: 12.687, file_cluster_5: 14.431
- **Magnitude:** 732.08 | **LOC:** 1381 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 31.898; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (14.6%)
- **Documentation Coverage:** 91.075% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deviceCreateShaderModule` **(Defensive Guards)** (Impact: 26.5)
  * `instanceRequestAdapter` **(Type Conversions)** (Impact: 5.1)
  * `createInstance` **(Type Conversions)** (Impact: 4.6)
  * `adapterCreateDevice` **(Type Conversions)** (Impact: 3.9)
  * `commandEncoderFinish` **(Type Conversions)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 55 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 118
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 39`, `args: 218`, `func_start: 218`
* *Risk/State:* `safety_bypasses: 248`, `high_risk_execution: 173`, `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `api: 222`, `import: 11`
* *Defense:* `safety: 73`, `test: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 31.898
  * `Choke Point (Betweenness):` 0.321346 | `Ripple Effect (Closeness):` 0.272762
  * `Imports (Out-Degree: 8):` build-options, builtin, d3d12.zig, metal.zig, opengl.zig, shader.zig, test.zig, std...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/module.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.277)
- **Top Global Matches:** file_cluster_5: 8.277, file_cluster_12: 9.54, file_cluster_7: 10.856
- **Magnitude:** 557.2 | **LOC:** 1021 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 5.226; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.6%), Mutation Surface (formerly State Flux) (59.3%), Guard Balance (formerly Safety Score) (55.0%)
- **Documentation Coverage:** 50.8197% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Objects` **(Many-Argument Workhorses)** (Impact: 84.6)
  * `Modules` **(Defensive Guards)** (Impact: 47.0)
  * `run` **(Defensive Guards)** (Impact: 25.9)
  * `Module` **(Defensive Guards)** (Impact: 24.4)
  * `ModuleTuple` **(Defensive Guards)** (Impact: 19.5)
    * *Intent:* /// Type-returning variant of merge()
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 7
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 86`, `args: 56`, `func_start: 55`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 33`, `high_risk_execution: 4`, `state_mutation: 18`, `dead_code: 1`, `planned_debt: 22`
* *Architecture:* `api: 64`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 47`, `doc: 136`, `test: 3`, `sync_locks: 5`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.226
  * `Choke Point (Betweenness):` 0.005147 | `Ripple Effect (Closeness):` 0.167152
  * `Imports (Out-Degree: 3):` StringTable.zig, graph.zig, main.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/codegen/msl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.822)
- **Top Global Matches:** file_cluster_15: 7.822, file_cluster_12: 7.851, file_cluster_16: 8.857
- **Magnitude:** 536.4 | **LOC:** 1221 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (21.2%), Debt Markers (formerly Tech Debt) (18.7%), Guard Balance (formerly Safety Score) (15.8%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitFn` **(Defensive Guards)** (Impact: 46.3)
  * `gen` **(Many-Argument Workhorses)** (Impact: 40.1)
  * `emitTextureType` **(Defensive Guards)** (Impact: 21.7)
  * `emitCall` **(Defensive Guards)** (Impact: 16.9)
  * `emitUnaryIntrinsic` **(Defensive Guards)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 9 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 34`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 11`, `planned_debt: 22`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 480`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.145758
  * `Imports (Out-Degree: 2):` Air.zig, CodeGen.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/codegen/hlsl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.405)
- **Top Global Matches:** file_cluster_4: 8.405, file_cluster_15: 9.074, file_cluster_0: 9.263
- **Magnitude:** 534.78 | **LOC:** 1190 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (19.5%), Mutation Surface (formerly State Flux) (19.0%), Guard Balance (formerly Safety Score) (16.4%), Connectivity (formerly Api Exposure) (11.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitFn` **(Defensive Guards)** (Impact: 50.0)
  * `emitGlobalVar` **(Defensive Guards)** (Impact: 39.6)
  * `emitStruct` **(Defensive Guards)** (Impact: 35.4)
  * `structMemberLessThan` **(Defensive Guards)** (Impact: 23.1)
  * `fnParamLessThan` **(Defensive Guards)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 46`, `args: 67`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 7`, `state_mutation: 10`, `planned_debt: 22`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 438`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.145758
  * `Imports (Out-Degree: 2):` Air.zig, CodeGen.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysaudio/wasapi.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 10.495)
- **Top Global Matches:** file_cluster_7: 10.495, file_cluster_14: 10.89, file_cluster_12: 11.855
- **Magnitude:** 499.88 | **LOC:** 1044 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.776; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.7%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `refresh` **(Defensive Guards)** (Impact: 63.4)
  * `createAudioClient` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `init` **(Defensive Guards)** (Impact: 24.7)
  * `getDefaultAudioEndpoint` **(Defensive Guards)** (Impact: 20.7)
  * `writeThread` **(Type Conversions)** (Impact: 18.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 10 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *Concurrency (weighted view):* 16
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 94
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 322`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 150`, `state_mutation: 34`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 25`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 41`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 0.000661 | `Ripple Effect (Closeness):` 0.119299
  * `Imports (Out-Degree: 4):` win32.zig, backends.zig, main.zig, std, util.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/codegen/glsl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.151)
- **Top Global Matches:** file_cluster_15: 8.151, file_cluster_12: 8.227, file_cluster_0: 8.565
- **Magnitude:** 408.8 | **LOC:** 904 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (17.9%), Guard Balance (formerly Safety Score) (15.9%), Mutation Surface (formerly State Flux) (15.8%), Connectivity (formerly Api Exposure) (11.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `emitFn` **(Defensive Guards)** (Impact: 40.1)
  * `gen` **(Many-Argument Workhorses)** (Impact: 40.0)
  * `emitGlobalVar` **(Defensive Guards)** (Impact: 23.1)
  * `emitReturn` **(Defensive Guards)** (Impact: 13.1)
  * `emitStruct` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 23`, `args: 59`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 5`, `state_mutation: 6`, `planned_debt: 15`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 342`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.417
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.145758
  * `Imports (Out-Degree: 2):` Air.zig, CodeGen.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/linux/Wayland.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.525)
- **Top Global Matches:** file_cluster_7: 8.525, file_cluster_12: 8.594, file_cluster_5: 10.101
- **Magnitude:** 408.22 | **LOC:** 993 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **14**; blast radius 3.101; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.2%), Guard Balance (formerly Safety Score) (66.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `registryHandleGlobal` **(Many-Argument Workhorses)** (Impact: 57.7)
  * `initWindow` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `seatHandleCapabilities` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `keyboardHandleKeymap` **(Many-Argument Workhorses)** (Impact: 17.6)
  * `keyboardHandleKey` **(Many-Argument Workhorses)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 109
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 53`, `args: 38`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 58`, `high_risk_execution: 8`, `state_mutation: 45`, `planned_debt: 15`
* *Architecture:* `io: 16`, `api: 19`, `import: 15`
* *Defense:* `safety: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.101
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.113651
  * `Imports (Out-Degree: 3):` Core.zig, main.zig, Linux.zig, input-event-codes.h, std, wayland-client-protocol.h, wayland-idle-inhibit-unstable-v1-client-protocol.h, wayland-pointer-constraints-unstable-v1-client-protocol.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/math/vec.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.243)
- **Top Global Matches:** file_cluster_15: 7.243, file_cluster_0: 8.708, file_cluster_16: 9.219
- **Magnitude:** 395.6 | **LOC:** 1175 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 8.411; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (94.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (41.4%), Guard Balance (formerly Safety Score) (34.0%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VecShared` **(Many-Argument Workhorses)** (Impact: 45.9)
  * `Vec3` **(Compute Cores)** (Impact: 10.4)
  * `Vec4` **(Generic / Templated Code)** (Impact: 8.2)
  * `maxScalar` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* // Returns the largest scalar of two vectors
  * `minScalar` **(Defensive Guards)** (Impact: 7.5)
    * *Intent:* // Returns the smallest scalar of two vectors
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 59`, `args: 54`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 6`, `duplicate_logic: 8`
* *Architecture:* `api: 154`, `import: 4`
* *Defense:* `safety: 118`, `doc: 66`, `test: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.411
  * `Choke Point (Betweenness):` 0.001504 | `Ripple Effect (Closeness):` 0.137317
  * `Imports (Out-Degree: 3):` main.zig, mat.zig, quat.zig, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/sysgpu/d3d12/conv.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.276)
- **Top Global Matches:** file_cluster_12: 6.276, file_cluster_7: 7.572, file_cluster_5: 8.277
- **Magnitude:** 389.54 | **LOC:** 738 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.4; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.3%), Guard Balance (formerly Safety Score) (61.7%)
- **Documentation Coverage:** 88.678% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dxgiFormatForTextureView` **(Compute Cores)** (Impact: 15.2)
  * `d3d12RasterizerDesc` **(Defensive Guards)** (Impact: 13.7)
  * `d3d12DescriptorRangeType` **(Generic / Templated Code)** (Impact: 12.3)
  * `d3d12ResourceFlagsForTexture` **(Compute Cores)** (Impact: 11.3)
  * `d3d12SrvDimension` **(Compute Cores)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 75`, `args: 45`, `func_start: 45`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 34`, `planned_debt: 1`
* *Architecture:* `api: 44`, `import: 3`
* *Defense:* `safety: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.153472
  * `Imports (Out-Degree: 3):` main.zig, utils.zig, c.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/Tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.65)
- **Top Global Matches:** file_cluster_8: 6.65, file_cluster_6: 17.069, file_cluster_3: 20.13
- **Magnitude:** 358.82 | **LOC:** 438 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 4.43; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (63.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `peek` **(Compute Cores)** (Impact: 96.5)
  * `init` **(Compute Cores)** (Impact: 4.5)
  * `next` **(Parameter Forwarders)** (Impact: 1.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 64`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `dead_code: 8`, `planned_debt: 2`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.43
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.194133
  * `Imports (Out-Degree: 1):` Token.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sysaudio/alsa.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_12: 7.625, file_cluster_7: 9.652, file_cluster_4: 10.157
- **Magnitude:** 356.48 | **LOC:** 838 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 6.911; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (58.1%), Mutation Surface (formerly State Flux) (51.3%), Guard Balance (formerly Safety Score) (51.0%), Concurrency Surface (formerly Concurrency) (50.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createStream` **(Many-Argument Workhorses)** (Impact: 41.3)
  * `refresh` **(Defensive Guards)** (Impact: 41.2)
  * `deviceEventsLoop` **(Defensive Guards)** (Impact: 23.0)
  * `toAlsaFormat` **(Compute Cores)** (Impact: 14.6)
  * `init` **(Defensive Guards)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 19
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 148`, `args: 86`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 17`
* *Architecture:* `io: 25`, `api: 30`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 57`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.911
  * `Choke Point (Betweenness):` 0.019716 | `Ripple Effect (Closeness):` 0.120256
  * `Imports (Out-Degree: 4):` main.zig, asoundlib.h, backends.zig, builtin, main.zig, std, util.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/math/collision.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.843)
- **Top Global Matches:** file_cluster_4: 6.843, file_cluster_12: 9.245, file_cluster_15: 9.687
- **Magnitude:** 351.96 | **LOC:** 825 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 2.945; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (53.2%), Guard Balance (formerly Safety Score) (44.5%)
- **Documentation Coverage:** 29.4118% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `polygonPolygonContact` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* /// Compute a Contact report between polygon_a and polygon_b if they are colliding.
  * `collisionRect` **(Compute Cores)** (Impact: 18.3)
    * *Intent:* /// Get collision rectangle for two rectangles collision.
  * `circlePolygonContact` **(Many-Argument Workhorses)** (Impact: 15.7)
    * *Intent:* /// Compute a Contact report between a Circle and a polygon.
  * `collidesLine` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* /// Returns true if a point is within the Line's threshold.
  * `collidesRect` **(Compute Cores)** (Impact: 13.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 49 instances
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 54`, `args: 17`, `func_start: 17`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 57`, `dead_code: 6`, `planned_debt: 6`
* *Architecture:* `api: 22`, `import: 3`
* *Defense:* `safety: 112`, `doc: 42`, `test: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.945
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.135152
  * `Imports (Out-Degree: 2):` testing.zig, main.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/Air.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.958)
- **Top Global Matches:** file_cluster_12: 6.958, file_cluster_5: 8.947, file_cluster_15: 9.288
- **Magnitude:** 332.88 | **LOC:** 1045 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **5**; blast radius 15.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (95.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.9%), Mutation Surface (formerly State Flux) (11.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveConstExpr` **(Defensive Guards)** (Impact: 55.8)
  * `findFunction` **(Defensive Guards)** (Impact: 9.4)
  * `typeSize` **(Defensive Guards)** (Impact: 9.3)
  * `resolveInt` **(Defensive Guards)** (Impact: 9.3)
  * `mul` **(Compute Cores)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 89`, `args: 36`, `func_start: 36`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 5`
* *Architecture:* `api: 92`, `import: 5`
* *Defense:* `safety: 41`, `doc: 3`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.251
  * `Choke Point (Betweenness):` 0.009874 | `Ripple Effect (Closeness):` 0.19186
  * `Imports (Out-Degree: 4):` Ast.zig, AstGen.zig, ErrorList.zig, std, wgsl.zig
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/sysaudio/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.586)
- **Top Global Matches:** file_cluster_12: 6.586, file_cluster_7: 8.337, file_cluster_5: 8.76
- **Magnitude:** 307.36 | **LOC:** 511 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **5**; blast radius 25.574; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (44.8%), Complexity Load (formerly Cognitive Load) (13.1%), Debt Markers (formerly Tech Debt) (10.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertTo` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `convertFrom` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `init` **(Defensive Guards)** (Impact: 15.4)
  * `preferredFormat` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* // TODO: don't call this in backends. let the user use it
  * `sampleRate` **(Defensive Guards)** (Impact: 10.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 50`, `args: 38`, `func_start: 35`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `planned_debt: 3`
* *Architecture:* `api: 66`, `import: 5`
* *Defense:* `safety: 47`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.574
  * `Choke Point (Betweenness):` 0.051527 | `Ripple Effect (Closeness):` 0.178064
  * `Imports (Out-Degree: 3):` backends.zig, builtin, conv.zig, std, util.zig
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/sysaudio/coreaudio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.515)
- **Top Global Matches:** file_cluster_12: 7.515, file_cluster_4: 9.395, file_cluster_7: 9.706
- **Magnitude:** 300.36 | **LOC:** 770 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.776; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (57.1%), Guard Balance (formerly Safety Score) (54.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `refresh` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `createRecorder` **(Many-Argument Workhorses)** (Impact: 40.4)
  * `createPlayer` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `captureCallback` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `createStreamDesc` **(Type Conversions)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 63
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 93`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 25`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 1`, `api: 27`, `import: 9`
* *Defense:* `safety: 37`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.776
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.119299
  * `Imports (Out-Degree: 3):` AudioUnit.h, CoreAudio.h, backends.zig, builtin, main.zig, objc, std, util.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/sysaudio/tests/sine.zig` (ZIG) | Magnitude: 27.34 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 23, design_snake_case: 22, safety: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/sysgpu/sysgpu/bind_group_layout.zig` (ZIG) | Magnitude: 39.5 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 102, core_var_decl: 24, design_pascal_case: 21, api: 12
- `src/sysgpu/shader/codegen/msl.zig` (ZIG) | Magnitude: 536.4 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 905, safety: 480, branch: 165, core_var_decl: 73
- `src/sysgpu/shader/codegen/glsl.zig` (ZIG) | Magnitude: 408.8 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 634, safety: 342, branch: 127, pointers: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/custom-renderer/Renderer.zig` (ZIG) | Magnitude: 31.26 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 112, core_var_decl: 35, design_snake_case: 32, structural_boundaries: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/core/linux/Wayland.zig` (ZIG) | Magnitude: 408.22 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 739, core_var_decl: 176, design_short_vars: 100, design_snake_case: 82
- `src/sysaudio/jack.zig` (ZIG) | Magnitude: 195.68 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 322, pointers: 81, args: 55, structural_boundaries: 53
- `src/StringTable.zig` (ZIG) | Magnitude: 33.64 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 48, core_var_decl: 19, safety: 17, doc: 14
- `src/sysaudio/tests/record.zig` (ZIG) | Magnitude: 14.62 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 56, core_var_decl: 15, design_snake_case: 12, structural_boundaries: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/gfx/font/native/Font.zig` -> Churn: **60.21%** | Cog Load: 27.9821% | Debt: 99.708%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sysgpu/vulkan.zig` -> **Shail Patel** (100.0% isolated ownership) | Magnitude: 1336.92
- `src/module.zig` -> **OliveThePuffin** (100.0% isolated ownership) | Magnitude: 557.2
- `build.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 190.78
- `src/gfx/Text.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 185.18
- `src/Audio.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 165.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sysgpu/vulkan.zig` -> **Severity: 10.477** (Bridge: 0.1347 * Flux: 77.8064%)
- `src/sysgpu/main.zig` -> **Severity: 4.685** (Bridge: 0.3213 * Flux: 14.5808%)
- `src/sysgpu/sysgpu/main.zig` -> **Severity: 1.843** (Bridge: 0.1955 * Flux: 9.4286%)
- `src/Core.zig` -> **Severity: 1.425** (Bridge: 0.0346 * Flux: 41.1999%)
- `src/sysgpu/d3d12.zig` -> **Severity: 1.408** (Bridge: 0.0166 * Flux: 84.9716%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sysgpu/main.zig` -> **Severity: 25.54** (Embedded: 0.2728 * Error Risk: 93.6346%)
- `src/sysgpu/sysgpu/interface.zig` -> **Severity: 19.515** (Embedded: 0.2439 * Error Risk: 80.0%)
- `src/sysgpu/sysgpu/main.zig` -> **Severity: 16.951** (Embedded: 0.3226 * Error Risk: 52.5426%)
- `src/sysgpu/sysgpu/buffer.zig` -> **Severity: 16.902** (Embedded: 0.229 * Error Risk: 73.7956%)
- `src/sysgpu/opengl/proc.zig` -> **Severity: 15.005** (Embedded: 0.1531 * Error Risk: 98.0178%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sysgpu/sysgpu/interface.zig` -> **Severity: 6218.449** (Blast Radius: 62.765 * Doc Risk: 99.0751%)
- `src/sysgpu/sysgpu/main.zig` -> **Severity: 5243.48** (Blast Radius: 122.348 * Doc Risk: 42.8571%)
- `src/main.zig` -> **Severity: 4774.7** (Blast Radius: 47.747 * Doc Risk: 100.0%)
- `src/sysgpu/main.zig` -> **Severity: 2905.11** (Blast Radius: 31.898 * Doc Risk: 91.075%)
- `src/sysaudio/main.zig` -> **Severity: 2557.4** (Blast Radius: 25.574 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9897 call pairs -- scoped 13.8%, unique 0.0%, ambiguous 11.1%, external 75.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 9893 | 13.8% | 0.0% | 11.1% | 75.1% |
| c | 2 | 0.0% | 0.0% | 0.0% | 100.0% |
| shell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
