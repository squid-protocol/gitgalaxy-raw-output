# ARCHITECTURAL_BRIEF: sokol-zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/floooh/sokol-zig.git` |
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
| Total Artifacts | 96 |
| Analyzed Artifacts (Scanned) | 69 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 46744 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 71.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5101 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.6929 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 31 | 3781 | 44.9% |
| C | 22 | 42447 | 31.9% |
| GLSL | 13 | 464 | 18.8% |
| MARKDOWN | 2 | 0 | 2.9% |
| HTML | 1 | 52 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z +3.10; from the repo's file-archetype mix)
> **File Composition:** State Mutators Files 33%, Declarative / Non-Code 25%, Data / Markup / Trivial 20%, Large Core Modules 19%, Interface Declarations Files 1%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 67 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 27*

**Composition by Extension & Reason:**
- `.zig`: 3x Excluded (Embedded Hex Payload: 4615 hex tokens in 701 LOC), 2x Excluded (Embedded Hex Payload: 5397 hex tokens in 823 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 1x Excluded (Embedded Hex Payload: 31078 hex tokens in 5174 LOC), 1x Excluded (Embedded Hex Payload: 21315 hex tokens in 5019 LOC), 1x Excluded (Embedded Hex Payload: 19964 hex tokens in 3620 LOC)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 74.2 | 12.3 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.6 | 36.5 | 52.4 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 98.9 | 4.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 13.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 20.6 | 6.2 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 19.8 | 0.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 20.9 | 1.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 59.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.5 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 56.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 10461 | 25 | 18 | `src/sokol/c/sokol_gfx.h` |
| cleanup | 10 | 5 | 0 | `src/sokol/c/sokol_app.h` |
| guards | 2827 | 22 | 6 | `src/sokol/c/sokol_gfx.h` |
| danger | 346 | 18 | 3 | `src/sokol/c/sokol_app.h` |
| concurrency | 50 | 3 | 0 | `src/sokol/c/sokol_fetch.h` |
| connectivity | 2941 | 41 | 39 | `src/sokol/c/sokol_gfx.h` |
| io | 6 | 2 | 0 | `src/sokol/c/sokol_fetch.h` |
| crypto | 0 | 0 | 0 | - |
| ipc | 22 | 2 | 0 | `src/sokol/c/sokol_gfx.h` |
| time | 4 | 2 | 0 | `src/sokol/c/sokol_app.h` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 98 | 5 | 0 | `src/sokol/c/sokol_app.h` |
| tests | 7 | 1 | 0 | `examples/math.zig` |
| docs | 151 | 7 | 0 | `src/sokol/debugtext.zig` |
| debt | 138 | 13 | 1 | `src/sokol/c/sokol_app.h` |
| mutation | 10507 | 54 | 70 | `src/sokol/c/sokol_gfx.h` |
| dead_code | 127 | 30 | 3 | `src/sokol/c/sokol_app.h` |
| credential | 0 | 0 | 0 | - |
| threat | 144 | 11 | 3 | `src/sokol/c/sokol_gfx.h` |
| ml_ai | 232 | 30 | 8 | `src/sokol/debugtext.zig` |
| ui | 7 | 2 | 0 | `src/sokol/c/sokol_app.h` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/sokol/c/sokol_fetch.h` (Hits: 4)
- `src/sokol/c/sokol_app.h` (Hits: 2)
- `CHANGELOG.md` (Hits: 0)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **sokol.zig** (`src/sokol/sokol.zig`) — 21 inbound connections
2. **sokol_defines.h** (`src/sokol/c/sokol_defines.h`) — 12 inbound connections
3. **math.zig** (`examples/math.zig`) — 10 inbound connections
4. **sokol_gfx.h** (`src/sokol/c/sokol_gfx.h`) — 7 inbound connections
5. **sokol_app.h** (`src/sokol/c/sokol_app.h`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sokol_app.h** (`src/sokol/c/sokol_app.h`) — 46 outbound dependencies
2. **sokol_gfx.h** (`src/sokol/c/sokol_gfx.h`) — 28 outbound dependencies
3. **sokol_audio.h** (`src/sokol/c/sokol_audio.h`) — 22 outbound dependencies
4. **sokol.zig** (`src/sokol/sokol.zig`) — 12 outbound dependencies
5. **sokol_fetch.h** (`src/sokol/c/sokol_fetch.h`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_sapp_x11_translate_keysyms` **(Compute Cores)** (@ `src/sokol/c/sokol_app.h`) -> Impact: **253.9** | LOC: 159
  * *Intent:* // translate the X11 KeySyms for a key to sokol-app key code // NOTE: this is only used as a fallback, in case the XBK method fails // it is layout-de...
- `_sfetch_channel_thread_func` **(Compute Cores)** (@ `src/sokol/c/sokol_fetch.h`) -> Impact: **214.8** | LOC: 647
  * *Intent:* #if _SFETCH_PLATFORM_WINDOWS
- `_sgimgui_capture_item_string` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **150.9** | LOC: 419
- `_sapp_win32_wndproc` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_app.h`) -> Impact: **134.3** | LOC: 226
- `_sg_validate_shader_desc` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **113.9** | LOC: 269
- `_sg_d3d11_create_view` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **113.0** | LOC: 216
- `_sg_d3d11_create_shader` **(Many-Argument Workhorses)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **110.5** | LOC: 166
- `_sg_validate_apply_bindings` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **108.6** | LOC: 220
- `_sgimgui_pixelformat_string` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **106.8** | LOC: 72
- `_sg_gl_teximage_internal_format` **(Compute Cores)** (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **104.2** | LOC: 76

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/sokol/c` | 22 | 33779.84 | 24.98% | 10.25% |
| `examples` | 22 | 783.36 | 12.22% | 0.0% |
| `src/sokol` | 9 | 671.06 | 0.91% | 9.45% |
| `examples/shaders` | 13 | 204.28 | 0.0% | 0.0% |
| `__monolith__` | 2 | 12.92 | 0.0% | 0.0% |
| `src/sokol/web` | 1 | 8.74 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/sokol/c/sokol_defines.h` -> **98.9013%** Exposure
- `src/sokol/c/sokol_audio.h` -> **37.3874%** Exposure
- `src/sokol/c/sokol_glue.h` -> **32.1778%** Exposure
- `src/sokol/audio.zig` -> **28.1406%** Exposure
- `src/sokol/imgui.zig` -> **26.0829%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/sokol/c/sokol_log.h` -> **100.0%** Exposure
- `src/sokol/c/sokol_glue.h` -> **99.9927%** Exposure
- `src/sokol/c/sokol_fetch.h` -> **99.9882%** Exposure
- `src/sokol/c/sokol_gfx.h` -> **99.9879%** Exposure
- `src/sokol/c/sokol_app.h` -> **99.9862%** Exposure
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
- **Unknown Dependencies:** `252` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/sokol/c/sokol_gfx.h` (C) -> Cumulative Risk: **731.74**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.00)
- **Magnitude:** 18140.32 | **LOC:** 26678 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 97.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), State Flux (99.9879%)
- **Heaviest Functions:** `_sg_validate_shader_desc` (Compute Cores, Impact: 113.9), `_sg_d3d11_create_view` (Compute Cores, Impact: 113.0), `_sg_d3d11_create_shader` (Many-Argument Workhorses, Impact: 110.5)

### 2. `src/sokol/c/sokol_app.h` (C) -> Cumulative Risk: **725.42**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.35)
- **Magnitude:** 8049.24 | **LOC:** 14397 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 95.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9862%), Churn (90.81%)
- **Heaviest Functions:** `_sapp_x11_translate_keysyms` (Compute Cores, Impact: 253.9), `_sapp_win32_wndproc` (Many-Argument Workhorses, Impact: 134.3), `_sapp_gl_choose_fbconfig` (Many-Argument Workhorses, Impact: 54.0)

### 3. `src/sokol/c/sokol_gfx_imgui.h` (C) -> Cumulative Risk: **666.32**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.29)
- **Magnitude:** 3956.34 | **LOC:** 5178 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9432%), Safety Score (86.2002%)
- **Heaviest Functions:** `_sgimgui_capture_item_string` (Many-Argument Workhorses, Impact: 150.9), `_sgimgui_pixelformat_string` (Compute Cores, Impact: 106.8), `_sgimgui_draw_shader_panel` (Many-Argument Workhorses, Impact: 99.0)

### 4. `src/sokol/c/sokol_fetch.h` (C) -> Cumulative Risk: **663.72**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.53)
- **Magnitude:** 1507.54 | **LOC:** 2811 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9882%), Safety Score (86.2107%)
- **Heaviest Functions:** `_sfetch_channel_thread_func` (Compute Cores, Impact: 214.8), `_sfetch_channel_dowork` (Compute Cores, Impact: 52.5), `_sfetch_request_handler` (Compute Cores, Impact: 49.5)

### 5. `src/sokol/c/sokol_audio.h` (C) -> Cumulative Risk: **643.26**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.09)
- **Magnitude:** 906.26 | **LOC:** 2664 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3672%), Verification (80.0%)
- **Heaviest Functions:** `_saudio_fifo_write` (Many-Argument Workhorses, Impact: 20.4), `_saudio_wasapi_backend_init` (Compute Cores, Impact: 16.9), `_saudio_n3ds_cb` (Compute Cores, Impact: 15.1)

### 6. `src/sokol/c/sokol_log.h` (C) -> Cumulative Risk: **605.89**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.29)
- **Magnitude:** 187.2 | **LOC:** 335 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (93.6178%)
- **Heaviest Functions:** `slog_func` (Many-Argument Workhorses, Impact: 69.2), `_slog_itoa` (Defensive Guards, Impact: 8.7), `_slog_append` (Compute Cores, Impact: 8.5)

### 7. `src/sokol/c/sokol_shape.h` (C) -> Cumulative Risk: **604.66**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.02)
- **Magnitude:** 691.68 | **LOC:** 1432 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9482%), Safety Score (88.8771%)
- **Heaviest Functions:** `sshape_build_box` (Compute Cores, Impact: 53.4), `sshape_build_cylinder` (Many-Argument Workhorses, Impact: 22.8), `sshape_build_sphere` (Many-Argument Workhorses, Impact: 22.6)

### 8. `src/sokol/c/sokol_glue.h` (C) -> Cumulative Risk: **531.05**
- **Archetype:** `file_cluster_13` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.85)
- **Magnitude:** 64.48 | **LOC:** 208 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9927%), Safety Score (82.7379%)
- **Heaviest Functions:** `_sglue_to_sgpixelformat` (Compute Cores, Impact: 14.8), `sglue_swapchain` (I/O & Config Routines, Impact: 2.5), `sglue_environment` (Interface Declarations, Impact: 1.9)

### 9. `src/sokol/sgimgui.zig` (ZIG) -> Cumulative Risk: **494.62**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `State Mutators Files` (z +1.16)
- **Magnitude:** 124.52 | **LOC:** 388 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.9474%), Safety Score (90.025%), Verification (80.0%)
- **Heaviest Functions:** `cStrToZig` (Interface Declarations, Impact: 1.6), `setup` (State Mutators, Impact: 1.6), `drawMenu` (Type Conversions, Impact: 1.6)

### 10. `src/sokol/c/sokol_time.h` (C) -> Cumulative Risk: **463.49**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.45)
- **Magnitude:** 102.96 | **LOC:** 320 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.3611%), Safety Score (73.8553%)
- **Heaviest Functions:** `stm_round_to_common_refresh_rate` (Compute Cores, Impact: 6.3), `stm_diff` (Compute Cores, Impact: 5.6), `stm_now` (Interface Declarations, Impact: 5.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/sokol/c/sokol_gfx.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 18140.32 | **LOC:** 26678 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 97.0%
- **Risk Profile:** Cognitive Load (53.2025%), Tech Debt (10.2183%)
**Top Internal Functions/Classes:**
  * `_sg_validate_shader_desc` **(Compute Cores)** (Impact: 113.9)
  * `_sg_d3d11_create_view` **(Compute Cores)** (Impact: 113.0)
  * `_sg_d3d11_create_shader` **(Many-Argument Workhorses)** (Impact: 110.5)
  * `_sg_validate_apply_bindings` **(Compute Cores)** (Impact: 108.6)
  * `_sg_gl_teximage_internal_format` **(Compute Cores)** (Impact: 104.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1825 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 6604
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4960`, `structural_boundaries: 4527`, `args: 2634`, `func_start: 928`, `class_start: 313`
* *Risk/State:* `safety_bypasses: 63`, `high_risk_execution: 1`, `state_mutation: 2954`, `dead_code: 25`, `planned_debt: 1`, `fragile_debt: 45`
* *Architecture:* `api: 1290`, `import: 25`
* *Defense:* `safety: 215`, `immutability_locks: 1242`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.859
  * `Choke Point (Betweenness):` 0.003402 | `Ripple Effect (Closeness):` 0.102941
  * `Imports (Out-Degree: 3):` AvailabilityMacros.h, gl.h, gl3.h, gl31.h, gl32.h, gl3ext.h, gl3.h, gl.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_app.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 8049.24 | **LOC:** 14397 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 95.2%
- **Risk Profile:** Cognitive Load (46.3491%), Tech Debt (12.5175%)
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
* *Amplified Cascading Flux:* 957 instances
* *Concurrency (weighted view):* 29
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 3723
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2117`, `structural_boundaries: 2348`, `args: 1552`, `func_start: 464`, `class_start: 87`
* *Risk/State:* `safety_bypasses: 110`, `high_risk_execution: 4`, `state_mutation: 1809`, `dead_code: 32`, `planned_debt: 25`, `fragile_debt: 37`
* *Architecture:* `io: 2`, `api: 595`, `concurrency: 9`, `import: 54`
* *Defense:* `safety: 67`, `sync_locks: 8`, `immutability_locks: 490`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.087
  * `Choke Point (Betweenness):` 0.000549 | `Ripple Effect (Closeness):` 0.091629
  * `Imports (Out-Degree: 1):` AvailabilityMacros.h, egl.h, gl.h, gl3.h, gl3ext.h, gl3.h, gl.h, TargetConditionals.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_gfx_imgui.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 3956.34 | **LOC:** 5178 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (66.2084%), Tech Debt (8.9134%)
**Top Internal Functions/Classes:**
  * `_sgimgui_capture_item_string` **(Many-Argument Workhorses)** (Impact: 150.9)
  * `_sgimgui_pixelformat_string` **(Compute Cores)** (Impact: 106.8)
  * `_sgimgui_draw_shader_panel` **(Many-Argument Workhorses)** (Impact: 99.0)
  * `_sgimgui_draw_passaction_panel` **(Compute Cores)** (Impact: 83.8)
  * `_sgimgui_draw_capture_panel` **(Compute Cores)** (Impact: 76.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 374 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 1232
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1059`, `structural_boundaries: 1060`, `args: 348`, `func_start: 244`, `class_start: 78`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 484`, `fragile_debt: 5`
* *Architecture:* `api: 355`, `import: 7`
* *Defense:* `safety: 37`, `immutability_locks: 217`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` assert.h, stdbool.h, stddef.h, stdint.h, stdio.h, stdlib.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_fetch.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1507.54 | **LOC:** 2811 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.2314%), Tech Debt (16.0199%)
**Top Internal Functions/Classes:**
  * `_sfetch_channel_thread_func` **(Compute Cores)** (Impact: 214.8)
    * *Intent:* #if _SFETCH_PLATFORM_WINDOWS
  * `_sfetch_channel_dowork` **(Compute Cores)** (Impact: 52.5)
    * *Intent:* /* per-frame channel stuff: move requests in and out of the IO threads, call response callbacks */
  * `_sfetch_request_handler` **(Compute Cores)** (Impact: 49.5)
    * *Intent:* #endif /* _SFETCH_PLATFORM_WINDOWS */ // ██████ ██ ██ █████ ███ ██ ███ ██ ███████ ██ ███████ // ██ █...
  * `_sfetch_channel_init` **(Many-Argument Workhorses)** (Impact: 21.0)
  * `_sfetch_validate_request` **(Compute Cores)** (Impact: 20.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 141 instances
* *Concurrency (weighted view):* 25
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 461
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 341`, `args: 212`, `func_start: 94`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 179`, `dead_code: 12`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 135`, `concurrency: 10`, `import: 10`
* *Defense:* `safety: 16`, `sync_locks: 9`, `immutability_locks: 57`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` assert.h, emscripten.h, pthread.h, sokol_log.h, stdbool.h, stddef.h, stdint.h, stdio.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_audio.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 906.26 | **LOC:** 2664 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.7707%), Tech Debt (37.3874%)
**Top Internal Functions/Classes:**
  * `_saudio_fifo_write` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* /* write new data to the write queue, this is called from main thread */
  * `_saudio_wasapi_backend_init` **(Compute Cores)** (Impact: 16.9)
  * `_saudio_n3ds_cb` **(Compute Cores)** (Impact: 15.1)
    * *Intent:* // ███████ ██████ ███████ // ██ ██ ██ ██ // ██████ ██ ██ ███████ // ██ ██ ██ ██ // ███████ ██████ ██...
  * `_saudio_alsa_backend_init` **(Compute Cores)** (Impact: 13.2)
  * `_saudio_log` **(Compute Cores)** (Impact: 12.9)
    * *Intent:* #undef _SAUDIO_LOGITEM_XMACRO #endif // SOKOL_DEBUG #define _SAUDIO_PANIC(code) _saudio_log(SAUDIO_L...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 89 instances
* *Concurrency (weighted view):* 15
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 336
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 232`, `structural_boundaries: 376`, `args: 279`, `func_start: 82`, `class_start: 26`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 158`, `dead_code: 7`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 152`, `concurrency: 10`, `import: 26`
* *Defense:* `safety: 24`, `sync_locks: 4`, `immutability_locks: 52`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` 3ds.h, AVFoundation.h, AudioToolbox.h, TargetConditionals.h, AAudio.h, alloca.h, asoundlib.h, assert.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_shape.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 691.68 | **LOC:** 1432 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2148%), Tech Debt (9.4112%)
**Top Internal Functions/Classes:**
  * `sshape_build_box` **(Compute Cores)** (Impact: 53.4)
  * `sshape_build_cylinder` **(Many-Argument Workhorses)** (Impact: 22.8)
  * `sshape_build_sphere` **(Many-Argument Workhorses)** (Impact: 22.6)
    * *Intent:* */
  * `sshape_build_torus` **(Compute Cores)** (Impact: 18.7)
    * *Intent:* */
  * `sshape_build_plane` **(Compute Cores)** (Impact: 18.0)
    * *Intent:* */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 154`, `args: 115`, `func_start: 59`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 141`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `api: 66`, `import: 6`
* *Defense:* `safety: 7`, `immutability_locks: 187`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.945
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` assert.h, math.h, stdbool.h, stddef.h, stdint.h, string.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_log.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 187.2 | **LOC:** 335 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (63.3502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `slog_func` **(Many-Argument Workhorses)** (Impact: 69.2)
    * *Intent:* #endif
  * `_slog_itoa` **(Defensive Guards)** (Impact: 8.7)
  * `_slog_append` **(Compute Cores)** (Impact: 8.5)
    * *Intent:* #endif #ifndef NOMINMAX #define NOMINMAX #endif #include <windows.h> #elif defined(_SLOG_ANDROID) #i...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 90
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 22`, `args: 32`, `func_start: 3`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 32`, `dead_code: 1`
* *Architecture:* `api: 7`, `import: 9`
* *Defense:* `safety: 4`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.878
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.132353
  * `Imports (Out-Degree: 0):` log.h, assert.h, emscripten.h, sokol_log.h, stddef.h, stdint.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sokol/debugtext.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 184.84 | **LOC:** 887 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.0304%), Tech Debt (14.8592%)
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
* *Risk/State:* `safety_bypasses: 3`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 49`, `import: 4`
* *Defense:* `safety: 4`, `doc: 59`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, gfx.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/shape.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 135.56 | **LOC:** 653 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.1652%), Tech Debt (15.9943%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin, gfx.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/sgimgui.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 124.52 | **LOC:** 388 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cStrToZig` **(Interface Declarations)** (Impact: 1.6)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/math.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 105.9 | **LOC:** 291 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.3031%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mul` **(Defensive Guards)** (Impact: 5.8)
  * `norm` **(Interface Declarations)** (Impact: 4.6)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.147059
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_time.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 102.96 | **LOC:** 320 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.8137%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stm_round_to_common_refresh_rate` **(Compute Cores)** (Impact: 6.3)
  * `stm_diff` **(Compute Cores)** (Impact: 5.6)
  * `stm_now` **(Interface Declarations)** (Impact: 5.0)
  * `stm_setup` **(Interface Declarations)** (Impact: 4.8)
    * *Intent:* #endif
  * `stm_laptime` **(Interface Declarations)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 28`, `args: 49`, `func_start: 11`, `class_start: 6`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `api: 28`, `import: 7`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` assert.h, emscripten.h, mach_time.h, stdint.h, string.h, time.h, windows.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/imgui.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 91.3 | **LOC:** 601 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (26.0829%)
**Top Internal Functions/Classes:**
  * `imtextureidWithSampler` **(Parameter Forwarders)** (Impact: 1.9)
  * `addMousePosEvent` **(State Mutators)** (Impact: 1.9)
  * `addTouchPosEvent` **(State Mutators)** (Impact: 1.9)
  * `addMouseButtonEvent` **(State Mutators)** (Impact: 1.9)
  * `addMouseWheelEvent` **(State Mutators)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 7`, `args: 42`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* `api: 26`, `import: 4`
* *Defense:* `doc: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` app.zig, builtin, gfx.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/mrt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 74.26 | **LOC:** 314 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.3%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 9.0)
  * `recreateOffscreenAttachments` **(State Mutators)** (Impact: 5.5)
    * *Intent:* // helper function to create or re-create attachment resources
  * `event` **(State Mutators)** (Impact: 3.1)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, mrt.glsl.zig, sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/c/sokol_glue.h` (C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 64.48 | **LOC:** 208 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (46.5882%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `_sglue_to_sgpixelformat` **(Compute Cores)** (Impact: 14.8)
    * *Intent:* #define _SOKOL_PRIVATE __attribute__((unused)) static #else #define _SOKOL_PRIVATE static #endif #en...
  * `sglue_swapchain` **(I/O & Config Routines)** (Impact: 2.5)
  * `sglue_environment` **(Interface Declarations)** (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 14`, `args: 15`, `func_start: 3`
* *Risk/State:* `state_mutation: 35`, `fragile_debt: 1`
* *Architecture:* `api: 8`, `import: 2`
* *Defense:* `safety: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.067227
  * `Imports (Out-Degree: 0):` assert.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/instancing.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 63.92 | **LOC:** 186 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.2461%), Tech Debt (0.0%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, instancing.glsl.zig, sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/shapes.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 54.28 | **LOC:** 200 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `input` **(State Mutators)** (Impact: 6.2)
  * `init` **(I/O & Config Routines)** (Impact: 4.5)
  * `frame` **(I/O & Config Routines)** (Impact: 4.5)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 13`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 24`, `unreferenced_by_name: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, shapes.glsl.zig, sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/audio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 48.44 | **LOC:** 703 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (28.1406%)
**Top Internal Functions/Classes:**
  * `push` **(Parameter Forwarders)** (Impact: 1.9)
    * *Intent:* /// push sample frames from main thread, returns number of frames actually pushed
  * `saudio_push` **(State Mutators)** (Impact: 1.8)
    * *Intent:* /// push sample frames from main thread, returns number of frames actually pushed
  * `cStrToZig` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `setup` **(State Mutators)** (Impact: 1.6)
    * *Intent:* /// setup sokol-audio
  * `saudio_setup` **(State Mutators)** (Impact: 1.5)
    * *Intent:* /// setup sokol-audio
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 28`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `doc: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/offscreen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 46.3 | **LOC:** 215 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 6.0)
  * `computeVsParams` **(Parameter Forwarders)** (Impact: 2.7)
  * `frame` **(I/O & Config Routines)** (Impact: 1.5)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 20`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 26`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, offscreen.glsl.zig, sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/sgl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 44.04 | **LOC:** 258 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.6416%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 7.8)
  * `drawCubes` **(State Mutators)** (Impact: 2.4)
  * `drawTexCube` **(State Mutators)** (Impact: 2.4)
  * `drawQuad` **(State Mutators)** (Impact: 2.1)
  * `frame` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 12`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `state_mutation: 10`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/time.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 43.28 | **LOC:** 172 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `diff` **(Parameter Forwarders)** (Impact: 1.9)
  * `stm_diff` **(State Mutators)** (Impact: 1.8)
  * `cStrToZig` **(Interface Declarations)** (Impact: 1.6)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `since` **(Interface Declarations)** (Impact: 1.6)
  * `laptime` **(Interface Declarations)** (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 21`, `func_start: 21`
* *Risk/State:* None
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/instancing-compute.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 41.76 | **LOC:** 203 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.8251%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `frame` **(I/O & Config Routines)** (Impact: 5.0)
  * `init` **(I/O & Config Routines)** (Impact: 4.5)
  * `computeVsParams` **(Parameter Forwarders)** (Impact: 2.1)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `drawFallback` **(State Mutators)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 12`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 13`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, instancing-compute.glsl.zig, sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/blend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 38.34 | **LOC:** 152 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.9293%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 6.2)
  * `frame` **(I/O & Config Routines)** (Impact: 5.0)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 13`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 14`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, blend.glsl.zig, sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/texcube.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 28.46 | **LOC:** 181 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` **(I/O & Config Routines)** (Impact: 3.5)
  * `computeVsParams` **(Parameter Forwarders)** (Impact: 2.1)
  * `frame` **(State Mutators)** (Impact: 1.5)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 12`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` math.zig, texcube.glsl.zig, sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/saudio.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 28.02 | **LOC:** 67 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.661%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `frame` **(I/O & Config Routines)** (Impact: 5.7)
  * `init` **(State Mutators)** (Impact: 1.5)
  * `main` **(State Mutators)** (Impact: 1.5)
  * `cleanup` **(State Mutators)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 4`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/sokol/c/sokol_gfx.h` -> Churn: **100.0%** | Cog Load: 53.2025% | Debt: 10.2183%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sokol/c/sokol_gfx.h` -> **GH Action** (97.0% isolated ownership) | Magnitude: 18140.32
- `src/sokol/c/sokol_app.h` -> **GH Action** (95.2% isolated ownership) | Magnitude: 8049.24
- `src/sokol/c/sokol_fetch.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 1507.54
- `src/sokol/c/sokol_audio.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 906.26
- `src/sokol/c/sokol_log.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 187.2

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sokol/c/sokol_gfx.h` -> **Severity: 0.34** (Bridge: 0.0034 * Flux: 99.9879%)
- `src/sokol/c/sokol_app.h` -> **Severity: 0.055** (Bridge: 0.0005 * Flux: 99.9862%)
- `src/sokol/c/sokol_audio.h` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 99.3672%)
- `src/sokol/c/sokol_fetch.h` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 99.9882%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sokol/sgimgui.zig` -> **Severity: 14.902** (Embedded: 0.1655 * Error Risk: 90.025%)
- `src/sokol/c/sokol_log.h` -> **Severity: 12.391** (Embedded: 0.1324 * Error Risk: 93.6178%)
- `examples/math.zig` -> **Severity: 9.495** (Embedded: 0.1471 * Error Risk: 64.5656%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 8.863** (Embedded: 0.1029 * Error Risk: 86.0935%)
- `src/sokol/imgui.zig` -> **Severity: 8.666** (Embedded: 0.1655 * Error Risk: 52.3554%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sokol/c/sokol_log.h` -> **Severity: 6287.8** (Blast Radius: 62.878 * Doc Risk: 100.0%)
- `examples/math.zig` -> **Severity: 4477.4** (Blast Radius: 44.774 * Doc Risk: 100.0%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 2785.9** (Blast Radius: 27.859 * Doc Risk: 100.0%)
- `src/sokol/c/sokol_app.h` -> **Severity: 2608.7** (Blast Radius: 26.087 * Doc Risk: 100.0%)
- `src/sokol/glue.zig` -> **Severity: 2364.6** (Blast Radius: 23.646 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
