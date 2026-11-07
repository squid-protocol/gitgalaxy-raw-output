# ARCHITECTURAL_BRIEF: sokol-zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/floooh/sokol-zig.git` |
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
- **Scope:** 79 analyzed artifact(s), 60738 LOC.
- **Load-bearing artifact:** `src/sokol/sokol.zig` -- 21 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/sokol/c/sokol_app.h` -- pulls in 46 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/sokol/c/sokol_gfx.h` at magnitude 17286.52 (structural weight, not risk).
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
| Total Artifacts | 96 |
| Analyzed Artifacts (Scanned) | 79 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 60738 |
| Volatility Index | 0.025 |
| % Scanned of codebase = | 82.3% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5144 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5447 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7436 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 37 | 7968 | 46.8% |
| C | 25 | 52234 | 31.6% |
| GLSL | 13 | 464 | 16.5% |
| MARKDOWN | 2 | 0 | 2.5% |
| YAML | 1 | 20 | 1.3% |
| HTML | 1 | 52 | 1.3% |

## 4.1 SOURCE ENCODINGS
All 79 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 23%, Large Core Modules 23%, Data / Markup / Trivial 19%, State Mutators Files 18%, Large Core Modules (3) 13%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 77 | 97.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.zig`: 3x Excluded (Machine-Generated Source Code Signature: 701 LOC), 2x Excluded (Machine-Generated Source Code Signature: 823 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1639 LOC)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 73.2 | 10.9 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 30.0 | 47.5 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 97.1 | 5.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 23.2 | 6.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 28.2 | 1.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 15.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 23.1 | 1.9 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.9 | 0.9 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 57.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 453 | 22 | 5 | `src/sokol/c/sokol_app.h` |
| cleanup | 14 | 9 | 1 | `src/sokol/c/sokol_app.h` |
| guards | 3375 | 28 | 78 | `src/sokol/c/sokol_gfx.h` |
| danger | 379 | 24 | 7 | `src/sokol/c/sokol_app.h` |
| concurrency | 53 | 5 | 0 | `src/sokol/c/sokol_fetch.h` |
| connectivity | 3861 | 49 | 100 | `src/sokol/c/sokol_gfx.h` |
| io | 9 | 4 | 0 | `src/sokol/c/sokol_fetch.h` |
| crypto | 0 | 0 | 0 | - |
| ipc | 39 | 4 | 0 | `src/sokol/c/sokol_gfx.h` |
| time | 4 | 2 | 0 | `src/sokol/c/sokol_app.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 100 | 6 | 0 | `src/sokol/c/sokol_app.h` |
| tests | 7 | 1 | 0 | `examples/math.zig` |
| docs | 1771 | 12 | 14 | `src/sokol/gfx.zig` |
| debt | 177 | 21 | 3 | `src/sokol/c/sokol_app.h` |
| mutation | 13014 | 62 | 299 | `src/sokol/c/sokol_gfx.h` |
| dead_code | 123 | 32 | 1 | `src/sokol/app.zig` |
| credential | 1 | 1 | 0 | `build.zig.zon` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 624 | 35 | 9 | `src/sokol/gl.zig` |
| ui | 7 | 2 | 0 | `src/sokol/c/sokol_app.h` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/sokol/c/sokol_fetch.h` (Hits: 4)
- `.github/workflows/main.yml` (Hits: 2)
- `src/sokol/c/sokol_app.h` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sokol.zig** (`src/sokol/sokol.zig`) — 21 inbound connections
2. **sokol_defines.h** (`src/sokol/c/sokol_defines.h`) — 12 inbound connections
3. **sokol_gfx.h** (`src/sokol/c/sokol_gfx.h`) — 11 inbound connections
4. **math.zig** (`examples/math.zig`) — 10 inbound connections
5. **gfx.zig** (`src/sokol/gfx.zig`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sokol_app.h** (`src/sokol/c/sokol_app.h`) — 46 outbound dependencies
2. **sokol_gfx.h** (`src/sokol/c/sokol_gfx.h`) — 23 outbound dependencies
3. **sokol_audio.h** (`src/sokol/c/sokol_audio.h`) — 21 outbound dependencies
4. **sokol.zig** (`src/sokol/sokol.zig`) — 12 outbound dependencies
5. **sokol_fetch.h** (`src/sokol/c/sokol_fetch.h`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_sapp_x11_translate_keysyms` **(Compute Cores)** (@ `src/sokol/c/sokol_app.h`) -> Impact: **253.9** | LOC: 159
  * *Intent:* // translate the X11 KeySyms for a key to sokol-app key code // NOTE: this is only used as a fallback, in case the XBK method fails // it is layout-de...
- `_sfetch_channel_thread_func` **(Compute Cores)** (@ `src/sokol/c/sokol_fetch.h`) -> Impact: **204.9** | LOC: 647
  * *Intent:* #if _SFETCH_PLATFORM_WINDOWS
- `_simgui_map_keycode` **(Compute Cores)** (@ `src/sokol/c/sokol_imgui.h`) -> Impact: **158.2** | LOC: 110
- `_sgimgui_capture_item_string` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **144.9** | LOC: 419
- `_sapp_win32_wndproc` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_app.h`) -> Impact: **134.3** | LOC: 226
- `_sg_d3d11_create_view` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **113.0** | LOC: 216
- `_sg_d3d11_create_shader` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **110.5** | LOC: 166
- `_sg_validate_apply_bindings` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **105.8** | LOC: 220
- `_sg_mtl_apply_bindings` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **103.5** | LOC: 203
- `_sg_wgpu_textureformat` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **102.8** | LOC: 77

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/sokol/c` | 25 | 35888.28 | 21.3% | 9.52% |
| `src/sokol` | 13 | 2275.36 | 1.21% | 10.79% |
| `examples` | 22 | 781.86 | 12.2% | 0.0% |
| `__monolith__` | 4 | 287.66 | 3.78% | 2.46% |
| `examples/shaders` | 13 | 204.28 | 0.0% | 0.0% |
| `src/sokol/web` | 1 | 8.74 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 4.7 | 5.13% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/sokol/c/sokol_defines.h` -> **97.0688%** Exposure
- `src/sokol/c/sokol_audio.h` -> **36.3378%** Exposure
- `src/sokol/app.zig` -> **31.1318%** Exposure
- `src/sokol/audio.zig` -> **23.8538%** Exposure
- `src/sokol/c/sokol_glue.h` -> **23.4296%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/sokol/c/sokol_log.h` -> **99.9997%** Exposure
- `src/sokol/c/sokol_glue.h` -> **99.9927%** Exposure
- `src/sokol/c/sokol_gfx.h` -> **99.9839%** Exposure
- `src/sokol/c/sokol_fetch.h` -> **99.9837%** Exposure
- `src/sokol/c/sokol_app.h` -> **99.9775%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/sokol/c/sokol_audio.h` -> **0** Orphaned Functions | **8** Duplicates
- `src/sokol/c/sokol_fetch.h` -> **0** Orphaned Functions | **2** Duplicates
- `examples/blend.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/bufferoffsets.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/clear.zig` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `288` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/sokol/c/sokol_gfx.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.438)
- **Top Global Matches:** file_cluster_4: 5.438, file_cluster_15: 10.005, file_cluster_16: 10.258
- **Magnitude:** 17286.52 | **LOC:** 26678 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 95.8%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **23**; blast radius 46.272; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (93.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sg_d3d11_create_view` **(Many-Argument Workhorses)** (Impact: 113.0)
  * `_sg_d3d11_create_shader` **(Many-Argument Workhorses)** (Impact: 110.5)
  * `_sg_validate_apply_bindings` **(Compute Cores)** (Impact: 105.8)
  * `_sg_mtl_apply_bindings` **(Compute Cores)** (Impact: 103.5)
  * `_sg_wgpu_textureformat` **(Compute Cores)** (Impact: 102.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1751 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 6456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4364`, `structural_boundaries: 4527`, `args: 2634`, `func_start: 928`, `class_start: 313`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 1`, `state_mutation: 2954`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 45`
* *Architecture:* `api: 1290`, `import: 25`
* *Defense:* `safety: 215`, `immutability_locks: 1242`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 46.272
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.141026
  * `Imports (Out-Degree: 0):` AvailabilityMacros.h, gl.h, gl3.h, gl31.h, gl32.h, gl3ext.h, gl3.h, gl.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_app.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.393)
- **Top Global Matches:** file_cluster_4: 10.393, file_cluster_12: 11.652, file_cluster_15: 11.822
- **Magnitude:** 7667.34 | **LOC:** 14397 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 94.1%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **46**; blast radius 28.061; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (93.3%), Connectivity (formerly Api Exposure) (84.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sapp_x11_translate_keysyms` **(Compute Cores)** (Impact: 253.9)
    * *Intent:* // translate the X11 KeySyms for a key to sokol-app key code // NOTE: this is only used as a fallbac...
  * `_sapp_win32_wndproc` **(Many-Argument Workhorses)** (Impact: 134.3)
  * `_sapp_gl_choose_fbconfig` **(Many-Argument Workhorses)** (Impact: 54.0)
    * *Intent:* // NOTE: this is used only in the GLX code path
  * `_sapp_gl_select_fbconfig` **(Many-Argument Workhorses)** (Impact: 51.8)
    * *Intent:* // NOTE: this is used only in the WGL code path
  * `_sapp_emsc_mouse_cb` **(Many-Argument Workhorses)** (Impact: 51.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 882 instances
* *Concurrency (weighted view):* 29
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 3573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1661`, `structural_boundaries: 2348`, `args: 1552`, `func_start: 464`, `class_start: 87`
* *Risk/State:* `safety_bypasses: 110`, `high_risk_execution: 4`, `state_mutation: 1809`, `dead_code: 8`, `planned_debt: 25`, `fragile_debt: 37`
* *Architecture:* `io: 2`, `api: 595`, `concurrency: 9`, `import: 54`
* *Defense:* `safety: 67`, `sync_locks: 8`, `immutability_locks: 490`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.061
  * `Choke Point (Betweenness):` 0.001166 | `Ripple Effect (Closeness):` 0.078526
  * `Imports (Out-Degree: 1):` AvailabilityMacros.h, egl.h, gl.h, gl3.h, gl3ext.h, gl3.h, gl.h, TargetConditionals.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_gfx_imgui.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_4: 7.308, file_cluster_12: 8.284, file_cluster_15: 9.271
- **Magnitude:** 3794.24 | **LOC:** 5178 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 8.529; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (77.8%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sgimgui_capture_item_string` **(Many-Argument Workhorses)** (Impact: 144.9)
  * `_sgimgui_pixelformat_string` **(Compute Cores)** (Impact: 102.6)
  * `_sgimgui_draw_shader_panel` **(Many-Argument Workhorses)** (Impact: 99.0)
  * `_sgimgui_draw_capture_panel` **(Compute Cores)** (Impact: 76.2)
  * `_sgimgui_draw_passaction_panel` **(Compute Cores)** (Impact: 52.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 373 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 930`, `structural_boundaries: 1060`, `args: 348`, `func_start: 244`, `class_start: 78`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 484`, `fragile_debt: 5`
* *Architecture:* `api: 355`, `import: 7`
* *Defense:* `safety: 37`, `immutability_locks: 217`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.529
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 2):` assert.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_gl.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.21)
- **Top Global Matches:** file_cluster_16: 6.21, file_cluster_15: 6.919, file_cluster_11: 8.063
- **Magnitude:** 1831.84 | **LOC:** 5019 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 9.355; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.3%), Connectivity (formerly Api Exposure) (49.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sgl_init_pipeline` **(Many-Argument Workhorses)** (Impact: 41.9)
  * `_sgl_draw` **(Many-Argument Workhorses)** (Impact: 29.5)
  * `sgl_end` **(Compute Cores)** (Impact: 22.1)
  * `_sgl_vtx` **(Stateful Encapsulated Methods)** (Impact: 18.1)
  * `_sgl_setup_common` **(I/O & Config Routines)** (Impact: 11.5)
    * *Intent:* // create resources which are shared between all contexts
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 190 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 795
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 508`, `args: 368`, `func_start: 163`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 7`, `high_risk_execution: 1`, `state_mutation: 415`, `planned_debt: 1`, `fragile_debt: 3`
* *Architecture:* `api: 209`, `import: 7`
* *Defense:* `safety: 18`, `immutability_locks: 82`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.355
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 1):` assert.h, math.h, stdbool.h, stddef.h, stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_fetch.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.779)
- **Top Global Matches:** file_cluster_4: 7.779, file_cluster_15: 8.064, file_cluster_12: 9.024
- **Magnitude:** 1464.84 | **LOC:** 2811 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 10.388; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.3%), Connectivity (formerly Api Exposure) (67.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sfetch_channel_thread_func` **(Compute Cores)** (Impact: 204.9)
    * *Intent:* #if _SFETCH_PLATFORM_WINDOWS
  * `_sfetch_request_handler` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* #endif /* _SFETCH_PLATFORM_WINDOWS */ // ██████ ██ ██ █████ ███ ██ ███ ██ ███████ ██ ███████ // ██ █...
  * `_sfetch_channel_dowork` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* /* per-frame channel stuff: move requests in and out of the IO threads, call response callbacks */
  * `_sfetch_validate_request` **(Compute Cores)** (Impact: 20.8)
  * `_sfetch_channel_init` **(Many-Argument Workhorses)** (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 135 instances
* *Concurrency (weighted view):* 25
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 341`, `args: 212`, `func_start: 94`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 179`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 135`, `concurrency: 10`, `import: 10`
* *Defense:* `safety: 16`, `sync_locks: 9`, `immutability_locks: 57`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 0):` assert.h, emscripten.h, pthread.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_debugtext.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.439)
- **Top Global Matches:** file_cluster_16: 5.439, file_cluster_15: 6.13, file_cluster_11: 7.073
- **Magnitude:** 980.2 | **LOC:** 5174 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 9.355; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.7%), Connectivity (formerly Api Exposure) (37.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sdtx_set_layer` **(Stateful Encapsulated Methods)** (Impact: 15.2)
  * `_sdtx_setup_common` **(I/O & Config Routines)** (Impact: 13.0)
  * `_sdtx_draw_layer` **(Compute Cores)** (Impact: 11.9)
  * `_sdtx_ctrl_char` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `_sdtx_unpack_font` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* // ███ ███ ██ ███████ ██████ // ████ ████ ██ ██ ██ // ██ ████ ██ ██ ███████ ██ // ██ ██ ██ ██ ██ ██ ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 98 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 453
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 216`, `args: 212`, `func_start: 81`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 257`, `fragile_debt: 2`
* *Architecture:* `api: 102`, `import: 10`
* *Defense:* `safety: 17`, `immutability_locks: 76`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.355
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 1):` assert.h, math.h, stdarg.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_audio.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.509)
- **Top Global Matches:** file_cluster_12: 6.509, file_cluster_15: 7.166, file_cluster_11: 8.251
- **Magnitude:** 889.26 | **LOC:** 2664 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 10.388; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.6%), Guard Balance (formerly Safety Score) (60.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_saudio_fifo_write` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* /* write new data to the write queue, this is called from main thread */
  * `_saudio_wasapi_backend_init` **(I/O & Config Routines)** (Impact: 16.9)
  * `_saudio_n3ds_cb` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* // ███████ ██████ ███████ // ██ ██ ██ ██ // ██████ ██ ██ ███████ // ██ ██ ██ ██ // ███████ ██████ ██...
  * `_saudio_vita_cb` **(Compute Cores)** (Impact: 12.6)
    * *Intent:* // ██ ██ ██ ████████ █████ // ██ ██ ██ ██ ██ ██ // ██ ██ ██ ██ ███████ // ██ ██ ██ ██ ██ ██ // █████...
  * `_saudio_alsa_backend_init` **(I/O & Config Routines)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 15
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 164`, `structural_boundaries: 376`, `args: 279`, `func_start: 82`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 158`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 152`, `concurrency: 10`, `import: 26`
* *Defense:* `safety: 24`, `sync_locks: 4`, `immutability_locks: 52`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 0):` 3ds.h, AVFoundation.h, AudioToolbox.h, TargetConditionals.h, AAudio.h, alloca.h, asoundlib.h, assert.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/gfx.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 10.939)
- **Top Global Matches:** file_cluster_15: 10.939, file_cluster_11: 11.411, file_cluster_16: 11.948
- **Magnitude:** 833.08 | **LOC:** 6024 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 77.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **2**; blast radius 71.552; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.7%), Guard Balance (formerly Safety Score) (44.4%)
- **Documentation Coverage:** 68.709% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asRange` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `applyViewport` **(State Mutators)** (Impact: 2.6)
  * `applyViewportf` **(State Mutators)** (Impact: 2.6)
  * `applyScissorRect` **(State Mutators)** (Impact: 2.6)
  * `applyScissorRectf` **(State Mutators)** (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 102`, `args: 365`, `func_start: 302`, `class_start: 149`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 22`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 316`, `import: 2`
* *Defense:* `safety: 2`, `doc: 1303`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 71.552
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.194712
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_imgui.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.464)
- **Top Global Matches:** file_cluster_4: 6.464, file_cluster_16: 8.54, file_cluster_15: 9.284
- **Magnitude:** 804.8 | **LOC:** 3620 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **7**; blast radius 13.703; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (74.8%), Guard Balance (formerly Safety Score) (54.7%), Connectivity (formerly Api Exposure) (29.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_simgui_map_keycode` **(Compute Cores)** (Impact: 158.2)
  * `simgui_handle_event` **(Compute Cores)** (Impact: 59.5)
  * `simgui_render` **(I/O & Config Routines)** (Impact: 29.4)
  * `simgui_new_frame` **(Compute Cores)** (Impact: 26.0)
  * `simgui_setup` **(Compute Cores)** (Impact: 21.7)
    * *Intent:* // ██████ ██ ██ ██████ ██ ██ ██████ // ██ ██ ██ ██ ██ ██ ██ ██ ██ // ██████ ██ ██ ██████ ██ ██ ██ //...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 41 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 349`, `args: 175`, `func_start: 65`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 170`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `api: 56`, `import: 7`
* *Defense:* `safety: 18`, `immutability_locks: 68`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.703
  * `Choke Point (Betweenness):` 0.000333 | `Ripple Effect (Closeness):` 0.038462
  * `Imports (Out-Degree: 2):` assert.h, emscripten.h, stdbool.h, stddef.h, stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_shape.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.625)
- **Top Global Matches:** file_cluster_16: 6.625, file_cluster_15: 7.85, file_cluster_11: 9.036
- **Magnitude:** 691.68 | **LOC:** 1432 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 9.355; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.2%), Guard Balance (formerly Safety Score) (66.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sshape_build_box` **(Many-Argument Workhorses)** (Impact: 53.4)
  * `sshape_build_cylinder` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `sshape_build_sphere` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* */
  * `sshape_build_torus` **(Many-Argument Workhorses)** (Impact: 18.7)
    * *Intent:* */
  * `sshape_build_plane` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 154`, `args: 115`, `func_start: 59`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 141`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `api: 66`, `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 9.355
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 0):` assert.h, math.h, stdbool.h, stddef.h, stdint.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/gl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.63)
- **Top Global Matches:** file_cluster_2: 7.63, file_cluster_15: 7.643, file_cluster_11: 7.696
- **Magnitude:** 440.98 | **LOC:** 1331 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 14.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.6%), Debt Markers (formerly Tech Debt) (8.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (6.7%)
- **Documentation Coverage:** 84.9624% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lookat` **(State Mutators)** (Impact: 3.3)
  * `v3fT2fC4f` **(State Mutators)** (Impact: 3.3)
  * `v3fT2fC4b` **(State Mutators)** (Impact: 3.3)
  * `sgl_lookat` **(State Mutators)** (Impact: 3.2)
  * `sgl_v3f_t2f_c4f` **(State Mutators)** (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 12`, `args: 180`, `func_start: 177`, `class_start: 8`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 97`, `import: 3`
* *Defense:* `doc: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 1):` builtin, gfx.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `build.zig` (ZIG | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.612)
- **Top Global Matches:** file_cluster_6: 6.612, file_cluster_4: 7.316, file_cluster_15: 14.722
- **Magnitude:** 259.34 | **LOC:** 618 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 92.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.29; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.8%), Guard Balance (formerly Safety Score) (42.8%), Complexity Load (formerly Cognitive Load) (15.1%), Mutation Surface (formerly State Flux) (10.9%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildLibSokol` **(Many-Argument Workhorses)** (Impact: 93.0)
  * `build` **(Defensive Guards)** (Impact: 30.7)
  * `emLinkStep` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `resolveSokolBackend` **(Compute Cores)** (Impact: 19.8)
    * *Intent:* // helper function to resolve .auto backend based on target platform
  * `buildExample` **(Many-Argument Workhorses)** (Impact: 14.0)
    * *Intent:* // build one of the examples
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 1 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 4
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 26`, `args: 15`, `func_start: 15`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 2`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 15`, `import: 3`
* *Defense:* `safety: 46`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 7.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, shdc, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/app.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.064)
- **Top Global Matches:** file_cluster_11: 6.064, file_cluster_2: 7.196, file_cluster_15: 7.199
- **Magnitude:** 251.04 | **LOC:** 2476 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 87.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 21.13; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (72.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.9%), Guard Balance (formerly Safety Score) (47.5%)
- **Documentation Coverage:** 0.6024% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindMouseCursorImage` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /// associate a custom mouse cursor image to a sapp_mouse_cursor enum entry
  * `sapp_bind_mouse_cursor_image` **(State Mutators)** (Impact: 1.8)
    * *Intent:* /// associate a custom mouse cursor image to a sapp_mouse_cursor enum entry
  * `cStrToZig` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `showKeyboard` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /// show or hide the mobile device onscreen keyboard
  * `showMouse` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /// show or hide the mouse cursor
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 40`, `args: 123`, `func_start: 111`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 38`, `planned_debt: 23`, `fragile_debt: 1`
* *Architecture:* `api: 100`, `import: 2`
* *Defense:* `doc: 227`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.13
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.154138
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sokol/debugtext.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.914)
- **Top Global Matches:** file_cluster_12: 7.914, file_cluster_11: 9.17, file_cluster_15: 9.186
- **Magnitude:** 184.84 | **LOC:** 887 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 14.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.6%), Guard Balance (formerly Safety Score) (47.9%), Debt Markers (formerly Tech Debt) (13.5%)
- **Documentation Coverage:** 65.0407% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asRange` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `print` **(Defensive Guards)** (Impact: 3.8)
    * *Intent:* // std.fmt-style formatted print
  * `color4b` **(State Mutators)** (Impact: 2.4)
  * `color4f` **(State Mutators)** (Impact: 2.4)
  * `sdtx_color4b` **(State Mutators)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 14`, `args: 82`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 3`, `fragile_debt: 1`
* *Architecture:* `api: 49`, `import: 4`
* *Defense:* `safety: 4`, `doc: 59`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 1):` builtin, gfx.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_log.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.126)
- **Top Global Matches:** file_cluster_8: 7.126, file_cluster_6: 17.309, file_cluster_3: 20.266
- **Magnitude:** 158.2 | **LOC:** 335 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 34.239; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (54.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `slog_func` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* #endif
  * `_slog_itoa` **(Defensive Guards)** (Impact: 8.7)
  * `_slog_append` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* #endif #ifndef NOMINMAX #define NOMINMAX #endif #include <windows.h> #elif defined(_SLOG_ANDROID) #i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 78
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 22`, `args: 32`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 32`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.061086
  * `Imports (Out-Degree: 0):` log.h, assert.h, emscripten.h, stddef.h, stdint.h, stdio.h, stdlib.h, syslog.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sokol/shape.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.16)
- **Top Global Matches:** file_cluster_15: 7.16, file_cluster_11: 7.62, file_cluster_13: 8.88
- **Magnitude:** 135.56 | **LOC:** 653 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 14.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (64.8%), Debt Markers (formerly Tech Debt) (14.4%), Complexity Load (formerly Cognitive Load) (4.2%)
- **Documentation Coverage:** 74.6835% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asRange` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `color4f` **(Parameter Forwarders)** (Impact: 2.4)
    * *Intent:* /// helper functions to build packed color value from floats or bytes
  * `color4b` **(Parameter Forwarders)** (Impact: 2.4)
  * `sshape_color_4f` **(State Mutators)** (Impact: 2.3)
    * *Intent:* /// helper functions to build packed color value from floats or bytes
  * `sshape_color_4b` **(State Mutators)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 28`, `args: 50`, `func_start: 50`, `class_start: 13`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 2`, `doc: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 1):` builtin, gfx.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/sgimgui.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.945)
- **Top Global Matches:** file_cluster_7: 7.945, file_cluster_14: 9.567, file_cluster_12: 11.007
- **Magnitude:** 124.52 | **LOC:** 388 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 14.827; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.0%)
- **Documentation Coverage:** 98.9474% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cStrToZig` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `setup` **(State Mutators)** (Impact: 1.6)
  * `drawMenu` **(Type Conversions)** (Impact: 1.6)
  * `drawBufferWindow` **(Type Conversions)** (Impact: 1.6)
  * `drawImageWindow` **(Type Conversions)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 1`, `args: 65`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `dead_code: 2`
* *Architecture:* `api: 34`, `import: 2`
* *Defense:* `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/math.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.231)
- **Top Global Matches:** file_cluster_15: 5.231, file_cluster_11: 5.926, file_cluster_2: 7.572
- **Magnitude:** 105.9 | **LOC:** 291 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **1**; blast radius 38.27; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (81.7%), Guard Balance (formerly Safety Score) (54.6%), Complexity Load (formerly Cognitive Load) (27.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mul` **(Defensive Guards)** (Impact: 5.8)
  * `norm` **(Compute Cores)** (Impact: 4.6)
  * `lookat` **(Many-Argument Workhorses)** (Impact: 3.3)
  * `persp` **(Parameter Forwarders)** (Impact: 2.8)
  * `rotate` **(Parameter Forwarders)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 34
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 27`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `state_mutation: 32`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 2`, `test: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.27
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.128205
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/sokol/imgui.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.207)
- **Top Global Matches:** file_cluster_15: 7.207, file_cluster_12: 7.769, file_cluster_2: 7.809
- **Magnitude:** 91.3 | **LOC:** 601 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 14.827; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (58.6%), Guard Balance (formerly Safety Score) (50.1%), Debt Markers (formerly Tech Debt) (22.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `imtextureidWithSampler` **(Parameter Forwarders)** (Impact: 1.9)
  * `addMousePosEvent` **(State Mutators)** (Impact: 1.9)
  * `addTouchPosEvent` **(State Mutators)** (Impact: 1.9)
  * `addMouseButtonEvent` **(State Mutators)** (Impact: 1.9)
  * `addMouseWheelEvent` **(State Mutators)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 42`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 2):` app.zig, builtin, gfx.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_time.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.025)
- **Top Global Matches:** file_cluster_15: 6.025, file_cluster_11: 6.735, file_cluster_17: 7.362
- **Magnitude:** 81.06 | **LOC:** 320 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 10.388; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.8%), Connectivity (formerly Api Exposure) (62.0%), Guard Balance (formerly Safety Score) (53.8%), Complexity Load (formerly Cognitive Load) (13.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stm_round_to_common_refresh_rate` **(Compute Cores)** (Impact: 6.3)
  * `stm_diff` **(Compute Cores)** (Impact: 5.6)
  * `stm_laptime` **(Compute Cores)** (Impact: 3.3)
  * `_stm_int64_muldiv` **(Parameter Forwarders)** (Impact: 2.2)
    * *Intent:* */ #if defined(_WIN32) || (defined(__APPLE__) && defined(__MACH__))
  * `stm_now` **(Interface Declarations)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 28`, `args: 49`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 28`, `import: 7`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.388
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 0):` assert.h, emscripten.h, mach_time.h, stdint.h, string.h, time.h, windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/fetch.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.952)
- **Top Global Matches:** file_cluster_15: 6.952, file_cluster_11: 7.008, file_cluster_2: 8.323
- **Magnitude:** 79.2 | **LOC:** 1166 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 14.827; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.5%), Dead Code Surface (formerly Dead Code) (19.0%), Debt Markers (formerly Tech Debt) (17.8%)
- **Documentation Coverage:** 14.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `asRange` **(Defensive Guards)** (Impact: 10.9)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `bindBuffer` **(State Mutators)** (Impact: 1.9)
    * *Intent:* /// bind a data buffer to a request (request must not currently have a buffer bound, must be called ...
  * `sfetch_bind_buffer` **(State Mutators)** (Impact: 1.8)
    * *Intent:* /// bind a data buffer to a request (request must not currently have a buffer bound, must be called ...
  * `cStrToZig` **(Parameter Forwarders)** (Impact: 1.6)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `setup` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /// setup sokol-fetch (can be called on multiple threads)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 11`, `args: 34`, `func_start: 30`, `class_start: 9`
* *Risk/State:* `dead_code: 15`, `fragile_debt: 1`
* *Architecture:* `api: 25`, `import: 2`
* *Defense:* `safety: 2`, `doc: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.827
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.144305
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/mrt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.38)
- **Top Global Matches:** file_cluster_15: 6.38, file_cluster_2: 7.138, file_cluster_11: 7.857
- **Magnitude:** 74.26 | **LOC:** 314 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (56.1%), Complexity Load (formerly Cognitive Load) (17.3%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 9.0)
  * `recreateOffscreenAttachments` **(Many-Argument Workhorses)** (Impact: 5.5)
    * *Intent:* // helper function to create or re-create attachment resources
  * `event` **(Generic / Templated Code)** (Impact: 3.1)
  * `frame` **(I/O & Config Routines)** (Impact: 3.0)
  * `computeMVP` **(Parameter Forwarders)** (Impact: 2.1)
    * *Intent:* // compute model-view-projection matrix
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 20`, `args: 7`, `func_start: 7`, `class_start: 5`
* *Risk/State:* `state_mutation: 27`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, mrt.glsl.zig, sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/c/sokol_glue.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.054)
- **Top Global Matches:** file_cluster_15: 7.054, file_cluster_17: 7.53, file_cluster_16: 7.779
- **Magnitude:** 64.48 | **LOC:** 208 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 8.839; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (61.4%), Connectivity (formerly Api Exposure) (46.8%), Complexity Load (formerly Cognitive Load) (37.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_sglue_to_sgpixelformat` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* #define _SOKOL_PRIVATE __attribute__((unused)) static #else #define _SOKOL_PRIVATE static #endif #en...
  * `sglue_swapchain` **(I/O & Config Routines)** (Impact: 2.5)
  * `sglue_environment` **(I/O & Config Routines)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 14`, `args: 15`, `func_start: 3`
* *Risk/State:* `state_mutation: 35`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.839
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.012821
  * `Imports (Out-Degree: 1):` assert.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/instancing.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.546)
- **Top Global Matches:** file_cluster_12: 6.546, file_cluster_15: 7.687, file_cluster_11: 7.927
- **Magnitude:** 63.92 | **LOC:** 186 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 7.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (61.8%), Complexity Load (formerly Cognitive Load) (54.2%), Connectivity (formerly Api Exposure) (6.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `frame` **(I/O & Config Routines)** (Impact: 8.3)
  * `init` **(I/O & Config Routines)** (Impact: 2.5)
  * `computeVsParams` **(Parameter Forwarders)** (Impact: 2.1)
  * `rand` **(Type Conversions)** (Impact: 1.9)
  * `xorshift32` **(Interface Declarations)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 38
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 15`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, instancing.glsl.zig, sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/shapes.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.538)
- **Top Global Matches:** file_cluster_12: 6.538, file_cluster_2: 8.058, file_cluster_15: 8.606
- **Magnitude:** 52.78 | **LOC:** 200 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 7.29; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.2%), Complexity Load (formerly Cognitive Load) (17.1%), Connectivity (formerly Api Exposure) (6.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `input` **(State Mutators)** (Impact: 6.2)
  * `init` **(I/O & Config Routines)** (Impact: 4.5)
  * `frame` **(I/O & Config Routines)** (Impact: 3.0)
  * `main` **(I/O & Config Routines)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 7.29
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, shapes.glsl.zig, sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `examples/texcube.zig` (ZIG) | Magnitude: 28.46 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 117, core_var_decl: 22, design_snake_case: 21, state_mutation: 12
- `examples/cube.zig` (ZIG) | Magnitude: 22.98 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 94, core_var_decl: 20, design_snake_case: 20, globals: 9
- `src/sokol/fetch.zig` (ZIG) | Magnitude: 79.2 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 90, doc: 48, core_var_decl: 43, args: 34
- `examples/noninterleaved.zig` (ZIG) | Magnitude: 24.86 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 88, core_var_decl: 22, design_snake_case: 22, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/sokol/sokol.zig` (ZIG) | Magnitude: 27.24 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 12, globals: 12, import: 12, core_var_decl: 12
- `src/sokol/gl.zig` (ZIG) | Magnitude: 440.98 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: scientific: 346, args: 180, func_start: 177, indent_spaces: 125

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/sokol/c/sokol_gfx.h` -> Churn: **100.0%** | Cog Load: 70.0842% | Debt: 10.1964%
- `src/sokol/c/sokol_app.h` -> Churn: **93.3%** | Cog Load: 61.7862% | Debt: 12.4732%
- `src/sokol/c/sokol_gfx_imgui.h` -> Churn: **51.95%** | Cog Load: 63.789% | Debt: 8.8246%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sokol/c/sokol_gfx.h` -> **GH Action** (95.8% isolated ownership) | Magnitude: 17286.52
- `src/sokol/c/sokol_app.h` -> **GH Action** (94.1% isolated ownership) | Magnitude: 7667.34
- `src/sokol/c/sokol_fetch.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 1464.84
- `src/sokol/c/sokol_audio.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 889.26
- `src/sokol/gl.zig` -> **Andre Weissflog** (100.0% isolated ownership) | Magnitude: 440.98

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sokol/c/sokol_app.h` -> **Severity: 0.117** (Bridge: 0.0012 * Flux: 99.9775%)
- `src/sokol/c/sokol_imgui.h` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 74.8005%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sokol/sgimgui.zig` -> **Severity: 11.544** (Embedded: 0.1443 * Error Risk: 80.0%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 9.083** (Embedded: 0.141 * Error Risk: 64.41%)
- `src/sokol/gfx.zig` -> **Severity: 8.649** (Embedded: 0.1947 * Error Risk: 44.4192%)
- `src/sokol/app.zig` -> **Severity: 7.319** (Embedded: 0.1541 * Error Risk: 47.4829%)
- `src/sokol/imgui.zig` -> **Severity: 7.226** (Embedded: 0.1443 * Error Risk: 50.0714%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sokol/gfx.zig` -> **Severity: 4916.266** (Blast Radius: 71.552 * Doc Risk: 68.709%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 4627.2** (Blast Radius: 46.272 * Doc Risk: 100.0%)
- `examples/math.zig` -> **Severity: 3827.0** (Blast Radius: 38.27 * Doc Risk: 100.0%)
- `src/sokol/c/sokol_log.h` -> **Severity: 3423.9** (Blast Radius: 34.239 * Doc Risk: 100.0%)
- `src/sokol/c/sokol_app.h` -> **Severity: 2806.1** (Blast Radius: 28.061 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 18 literal sites + 114 sites through wrappers = 132

- `_sg_free` (function, memory_alloc, primitive): 21 call sites in 1 files -- `src/sokol/c/sokol_gfx.h`
- `_sgimgui_free` (function, memory_alloc, primitive): 12 call sites in 1 files -- `src/sokol/c/sokol_gfx_imgui.h`
- `_saudio_free` (function, memory_alloc, primitive): 9 call sites in 1 files -- `src/sokol/c/sokol_audio.h`
- `_sfetch_ring_discard` (function, memory_alloc, via _sfetch_free): 8 call sites in 1 files -- `src/sokol/c/sokol_fetch.h`
- `_sg_pool_discard` (function, memory_alloc, via _sg_free): 7 call sites in 1 files -- `src/sokol/c/sokol_gfx.h`
- `_sgl_free` (function, memory_alloc, primitive): 7 call sites in 1 files -- `src/sokol/c/sokol_gl.h`
- `_sdtx_free` (function, memory_alloc, primitive): 6 call sites in 1 files -- `src/sokol/c/sokol_debugtext.h`
- `_sgimgui_malloc_clear` (function, memory_alloc, via _sgimgui_malloc): 6 call sites in 1 files -- `src/sokol/c/sokol_gfx_imgui.h`
- `_sfetch_free` (function, memory_alloc, primitive): 5 call sites in 1 files -- `src/sokol/c/sokol_fetch.h`
- `_sgimgui_malloc` (function, memory_alloc, primitive): 5 call sites in 1 files -- `src/sokol/c/sokol_gfx_imgui.h`
- `_sgimgui_bin_dup` (function, memory_alloc, via _sgimgui_malloc): 2 call sites in 1 files -- `src/sokol/c/sokol_gfx_imgui.h`
- `_sgimgui_str_dup` (function, memory_alloc, via _sgimgui_malloc): 2 call sites in 1 files -- `src/sokol/c/sokol_gfx_imgui.h`
*(+22 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 9286 call pairs -- scoped 42.6%, unique 1.6%, ambiguous 0.2%, external 55.6%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 8031 | 42.6% | 1.8% | 0.0% | 55.6% |
| zig | 1251 | 42.5% | 0.0% | 1.8% | 55.7% |
| html | 4 | 0.0% | 0.0% | 0.0% | 100.0% |

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
