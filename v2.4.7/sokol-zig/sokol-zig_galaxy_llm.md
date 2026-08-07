# ARCHITECTURAL_BRIEF: sokol-zig
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/sokol-zig` |
| **Timestamp** | `2026-08-07T04:29:39.868195+00:00` |
| **Scan Duration** | `2.86s` |
| **Git Branch** | `master` |
| **Git Commit** | `bdaddbf17a69fb2837a17ec8bca9e516b8351151` |
| **Git Remote** | `https://github.com/floooh/sokol-zig.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 66 malicious artifacts.

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
| Total Artifacts | 96 |
| Analyzed Artifacts (Scanned) | 69 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 27 |
| Total LOC | 26218 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 71.9% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5101 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6167 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.954 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 5 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 31 | 6519 | 44.9% |
| C | 22 | 19183 | 31.9% |
| GLSL | 13 | 464 | 18.8% |
| MARKDOWN | 2 | 0 | 2.9% |
| HTML | 1 | 52 | 1.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.071`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 63 | 91.3% |
| file_cluster_13 | 3 | 4.3% |
| file_cluster_4 | 1 | 1.4% |

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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 79.4 | 14.8 | 8.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 98.9 | 37.6 | 54.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.3 | 0.0 | 0.0 |
| API Exposure | 0.0 | 19.4 | 3.7 | 0.8 | 0.0 |
| Concurrency Exposure | 0.0 | 76.6 | 1.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 20.9 | 1.6 | 0.0 | 0.0 |
| Specification Exposure | 33.3 | 100.0 | 89.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.8 | 1.5 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/sokol/c/sokol_gfx_imgui.h` (Hits: 43)
- `src/sokol/c/sokol_gfx.h` (Hits: 12)
- `src/sokol/c/sokol_fetch.h` (Hits: 6)

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

- `_sapp_emsc_wheel_cb` (@ `src/sokol/c/sokol_app.h`) -> Impact: **185.9** | LOC: 399
- `_sgimgui_capture_item_string` (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **145.9** | LOC: 419
- `_sgimgui_draw_capture_panel` (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **97.0** | LOC: 139
- `slog_func` (@ `src/sokol/c/sokol_log.h`) -> Impact: **94.7** | LOC: 83
  * *Intent:* #endif
- `_sg_validate_view_desc` (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **79.5** | LOC: 210
- `_sgimgui_pixelformat_string` (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **76.6** | LOC: 72
- `_sapp_emsc_mouse_cb` (@ `src/sokol/c/sokol_app.h`) -> Impact: **71.6** | LOC: 72
- `_sgimgui_draw_passaction_panel` (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **70.3** | LOC: 47
- `_sgimgui_draw_shader_panel` (@ `src/sokol/c/sokol_gfx_imgui.h`) -> Impact: **64.0** | LOC: 179
- `_sg_validate_shader_binding_limits` (@ `src/sokol/c/sokol_gfx.h`) -> Impact: **56.0** | LOC: 99

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/sokol/c` | 22 | 20820.86 | 26.63% | 10.74% |
| `examples` | 22 | 788.74 | 11.3% | 0.0% |
| `src/sokol` | 9 | 769.74 | 5.61% | 4.99% |
| `examples/shaders` | 13 | 204.28 | 8.36% | 0.0% |
| `__monolith__` | 2 | 12.92 | 0.0% | 0.0% |
| `src/sokol/web` | 1 | 7.24 | 0.0% | 86.14% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/sokol/c/sokol_defines.h` -> **100.0%** Exposure
- `src/sokol/web/shell.html` -> **86.1395%** Exposure
- `src/sokol/c/sokol_audio.h` -> **41.3513%** Exposure
- `src/sokol/c/sokol_glue.h` -> **32.1778%** Exposure
- `src/sokol/c/sokol_app.h` -> **17.6901%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/sokol/c/sokol_gfx.h` -> **100.0%** Exposure
- `src/sokol/c/sokol_gfx_imgui.h` -> **100.0%** Exposure
- `src/sokol/c/sokol_log.h` -> **100.0%** Exposure
- `src/sokol/c/sokol_shape.h` -> **100.0%** Exposure
- `src/sokol/c/sokol_time.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `examples/math.zig` -> **0** Orphaned Functions | **7** Duplicates
- `src/sokol/c/sokol_gfx_imgui.h` -> **0** Orphaned Functions | **2** Duplicates
- `examples/blend.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/bufferoffsets.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/clear.zig` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/sokol/c/sokol_log.h`** -> AI Confidence: **99.43%**
2. **`src/sokol/c/sokol_gfx_imgui.c`** -> AI Confidence: **99.34%**
3. **`src/sokol/c/sokol_debugtext.c`** -> AI Confidence: **99.32%**
4. **`src/sokol/c/sokol_gl.c`** -> AI Confidence: **99.32%**
5. **`src/sokol/c/sokol_shape.c`** -> AI Confidence: **99.32%**
6. **`src/sokol/c/sokol_gfx_imgui.h`** -> AI Confidence: **99.31%**
7. **`src/sokol/c/sokol_time.h`** -> AI Confidence: **99.31%**
8. **`src/sokol/c/sokol_app.c`** -> AI Confidence: **99.29%**
9. **`src/sokol/c/sokol_audio.c`** -> AI Confidence: **99.29%**
10. **`src/sokol/c/sokol_fetch.c`** -> AI Confidence: **99.29%**

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

### 1. `src/sokol/c/sokol_gfx.h` (C) -> Cumulative Risk: **668.76**
- **Archetype:** `file_cluster_8` (Distance: 15.382 IQR)
- **Magnitude:** 10704.0 | **LOC:** 26678 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 95.2%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `_sg_validate_view_desc` (Impact: 79.5), `_sg_validate_shader_binding_limits` (Impact: 56.0), `_sg_pixelformat_bytesize` (Impact: 48.8)

### 2. `src/sokol/c/sokol_fetch.h` (C) -> Cumulative Risk: **633.59**
- **Archetype:** `file_cluster_4` (Distance: 12.407 IQR)
- **Magnitude:** 504.36 | **LOC:** 2811 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9758%), Verification (80.0%)
- **Heaviest Functions:** `_sfetch_win32_utf8_to_wide` (Impact: 14.8), `_sfetch_thread_enqueue_incoming` (Impact: 7.7), `_sfetch_thread_dequeue_incoming` (Impact: 6.8)

### 3. `src/sokol/c/sokol_gfx_imgui.h` (C) -> Cumulative Risk: **624.35**
- **Archetype:** `file_cluster_8` (Distance: 14.124 IQR)
- **Magnitude:** 5615.2 | **LOC:** 5178 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (92.7218%)
- **Heaviest Functions:** `_sgimgui_capture_item_string` (Impact: 145.9), `_sgimgui_draw_capture_panel` (Impact: 97.0), `_sgimgui_pixelformat_string` (Impact: 76.6)

### 4. `src/sokol/c/sokol_shape.h` (C) -> Cumulative Risk: **588.0**
- **Archetype:** `file_cluster_8` (Distance: 14.262 IQR)
- **Magnitude:** 1437.82 | **LOC:** 1432 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9999%), Safety Score (98.8794%)
- **Heaviest Functions:** `sshape_build_box` (Impact: 32.9), `sshape_build_cylinder` (Impact: 14.8), `sshape_build_sphere` (Impact: 14.5)

### 5. `src/sokol/c/sokol_log.h` (C) -> Cumulative Risk: **569.47**
- **Archetype:** `file_cluster_13` (Distance: 13.014 IQR)
- **Magnitude:** 311.52 | **LOC:** 335 | **CtrlFlow:** 86.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (87.0079%)
- **Heaviest Functions:** `slog_func` (Impact: 94.7), `_slog_append` (Impact: 8.5), `_slog_itoa` (Impact: 4.7)

### 6. `src/sokol/c/sokol_app.h` (C) -> Cumulative Risk: **550.5**
- **Archetype:** `file_cluster_13` (Distance: 13.669 IQR)
- **Magnitude:** 1784.68 | **LOC:** 14397 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 96.4%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9652%), Churn (92.56%), Safety Score (80.208%)
- **Heaviest Functions:** `_sapp_emsc_wheel_cb` (Impact: 185.9), `_sapp_emsc_mouse_cb` (Impact: 71.6), `sapp_get_swapchain` (Impact: 24.7)

### 7. `src/sokol/c/sokol_glue.h` (C) -> Cumulative Risk: **489.87**
- **Archetype:** `file_cluster_8` (Distance: 11.28 IQR)
- **Magnitude:** 77.18 | **LOC:** 208 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9968%), Safety Score (76.6127%)
- **Heaviest Functions:** `_sglue_to_sgpixelformat` (Impact: 10.7), `sglue_swapchain` (Impact: 2.9), `sglue_environment` (Impact: 2.3)

### 8. `src/sokol/c/sokol_time.h` (C) -> Cumulative Risk: **461.8**
- **Archetype:** `file_cluster_8` (Distance: 12.268 IQR)
- **Magnitude:** 128.62 | **LOC:** 320 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (99.9007%), Safety Score (89.8309%)
- **Heaviest Functions:** `stm_now` (Impact: 6.7), `stm_setup` (Impact: 6.5), `stm_round_to_common_refresh_rate` (Impact: 4.7)

### 9. `src/sokol/sgimgui.zig` (ZIG) -> Cumulative Risk: **424.44**
- **Archetype:** `file_cluster_8` (Distance: 9.936 IQR)
- **Magnitude:** 127.5 | **LOC:** 388 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Verification (80.0%), Safety Score (71.247%)
- **Heaviest Functions:** `cStrToZig` (Impact: 4.2), `drawMenu` (Impact: 2.1), `drawBufferWindow` (Impact: 2.1)

### 10. `src/sokol/c/sokol_audio.h` (C) -> Cumulative Risk: **383.96**
- **Archetype:** `file_cluster_8` (Distance: 10.731 IQR)
- **Magnitude:** 83.66 | **LOC:** 2664 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.1431%), Safety Score (68.9217%), Tech Debt (41.3513%)
- **Heaviest Functions:** `saudio_suspended` (Impact: 7.7), `saudio_push` (Impact: 7.5), `saudio_expect` (Impact: 4.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/sokol/c/sokol_gfx.h` (C | Tier 0 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.382 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.244 IQR)
- **Top Global Matches:** file_cluster_8: 15.382, file_cluster_0: 15.593, file_cluster_11: 15.607
- **Magnitude:** 10704.0 | **LOC:** 26678 | **CtrlFlow:** 58.7% | **Authorship Centralization:** 95.2%
- **Risk Profile:** Cognitive Load (62.4873%), Tech Debt (10.8168%)
**Top Internal Functions/Classes:**
  * `_sg_validate_view_desc` (Impact: 79.5)
  * `_sg_validate_shader_binding_limits` (Impact: 56.0)
  * `_sg_pixelformat_bytesize` (Impact: 48.8)
  * `_sg_pipeline_desc_defaults` (Impact: 46.2)
  * `_sg_uniform_size` (Impact: 41.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2671`, `structural_boundaries: 1877`, `args: 143`, `func_start: 616`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 34`, `state_mutation: 6394`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 27`
* *Architecture:* `io: 12`, `api: 2327`
* *Defense:* `safety: 112`, `immutability_locks: 679`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.859
  * `Choke Point (Betweenness):` 0.003402 | `Ripple Effect (Closeness):` 0.102941
  * `Imports (Out-Degree: 3):` myshader.glsl.h, string.h, windows.h, gl.h, sokol_glue.h, sokol_app.h, assert.h, gl32.h...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_gfx_imgui.h` (C | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.124 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.217 IQR)
- **Top Global Matches:** file_cluster_8: 14.124, file_cluster_0: 14.37, file_cluster_11: 14.38
- **Magnitude:** 5615.2 | **LOC:** 5178 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (79.3659%), Tech Debt (11.2093%)
**Top Internal Functions/Classes:**
  * `_sgimgui_capture_item_string` (Impact: 145.9)
  * `_sgimgui_draw_capture_panel` (Impact: 97.0)
  * `_sgimgui_pixelformat_string` (Impact: 76.6)
  * `_sgimgui_draw_passaction_panel` (Impact: 70.3)
  * `_sgimgui_draw_shader_panel` (Impact: 64.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1206`, `structural_boundaries: 904`, `args: 107`, `func_start: 244`, `class_start: 78`
* *Risk/State:* `safety_bypasses: 78`, `state_mutation: 2420`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `io: 43`, `api: 1338`, `import: 4`
* *Defense:* `safety: 37`, `test: 1`, `immutability_locks: 217`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.34
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, stdint.h, stdio.h, stddef.h, stdlib.h, assert.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_app.h` (C | Tier 0 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.669 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.968 IQR)
- **Top Global Matches:** file_cluster_13: 13.669, file_cluster_8: 13.689, file_cluster_0: 13.747
- **Magnitude:** 1784.68 | **LOC:** 14397 | **CtrlFlow:** 32.5% | **Authorship Centralization:** 96.4%
- **Risk Profile:** Cognitive Load (41.4883%), Tech Debt (17.6901%)
**Top Internal Functions/Classes:**
  * `_sapp_emsc_wheel_cb` (Impact: 185.9)
  * `_sapp_emsc_mouse_cb` (Impact: 71.6)
  * `sapp_get_swapchain` (Impact: 24.7)
  * `_sapp_emsc_size_changed` (Impact: 17.6)
  * `sapp_html5_fetch_dropped_file` (Impact: 15.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 277`, `structural_boundaries: 576`, `args: 59`, `func_start: 45`, `class_start: 63`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 1`, `state_mutation: 564`, `dead_code: 15`, `planned_debt: 4`, `fragile_debt: 11`
* *Architecture:* `io: 2`, `api: 648`, `import: 23`
* *Defense:* `safety: 11`, `immutability_locks: 117`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.087
  * `Choke Point (Betweenness):` 0.000549 | `Ripple Effect (Closeness):` 0.091629
  * `Imports (Out-Degree: 1):` shellapi.h, string.h, windows.h, math.h, Xresource.h, egl.h, windowsx.h, gl.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_shape.h` (C | Tier 0 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.262 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.321 IQR)
- **Top Global Matches:** file_cluster_8: 14.262, file_cluster_0: 14.304, file_cluster_13: 14.316
- **Magnitude:** 1437.82 | **LOC:** 1432 | **CtrlFlow:** 41.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6298%), Tech Debt (9.4799%)
**Top Internal Functions/Classes:**
  * `sshape_build_box` (Impact: 32.9)
    * *Intent:* #endif // SOKOL_SHAPE_INCLUDED /*-- IMPLEMENTATION -------------------------------------------------...
  * `sshape_build_cylinder` (Impact: 14.8)
  * `sshape_build_sphere` (Impact: 14.5)
  * `sshape_build_torus` (Impact: 12.2)
  * `sshape_build_plane` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 151`, `args: 25`, `func_start: 59`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 842`, `dead_code: 5`, `fragile_debt: 1`
* *Architecture:* `api: 368`, `import: 3`
* *Defense:* `safety: 6`, `test: 1`, `immutability_locks: 186`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.945
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` stdbool.h, string.h, math.h, assert.h, stdint.h, stddef.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_fetch.h` (C | Tier 0 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.407 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 5.742 IQR)
- **Top Global Matches:** file_cluster_4: 12.407, file_cluster_13: 12.655, file_cluster_8: 12.706
- **Magnitude:** 504.36 | **LOC:** 2811 | **CtrlFlow:** 37.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.4792%), Tech Debt (13.5236%)
**Top Internal Functions/Classes:**
  * `_sfetch_win32_utf8_to_wide` (Impact: 14.8)
  * `_sfetch_thread_enqueue_incoming` (Impact: 7.7)
  * `_sfetch_thread_dequeue_incoming` (Impact: 6.8)
  * `_sfetch_thread_dequeue_outgoing` (Impact: 6.5)
  * `_sfetch_pool_item_free` (Impact: 5.8)
    * *Intent:* // unbind and free the currently associated buffer, // the buffer pointer could be null if the reque...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 139`, `args: 1`, `func_start: 27`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 152`, `dead_code: 3`, `fragile_debt: 2`
* *Architecture:* `io: 6`, `api: 206`, `concurrency: 35`, `import: 10`
* *Defense:* `safety: 8`, `test: 1`, `sync_locks: 9`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` stdbool.h, string.h, windows.h, assert.h, stdint.h, stdio.h, pthread.h, sokol_log.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_log.h` (C | Tier 0 | 🚨 AI THREAT: 99.43%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.014 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 3.943 IQR)
- **Top Global Matches:** file_cluster_13: 13.014, file_cluster_8: 13.176, file_cluster_11: 13.311
- **Magnitude:** 311.52 | **LOC:** 335 | **CtrlFlow:** 86.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.0434%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `slog_func` (Impact: 94.7)
    * *Intent:* #endif
  * `_slog_append` (Impact: 8.5)
    * *Intent:* #endif #ifndef NOMINMAX #define NOMINMAX #endif #include <windows.h> #elif defined(_SLOG_ANDROID) #i...
  * `_slog_itoa` (Impact: 4.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 13`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 147`, `dead_code: 1`
* *Architecture:* `api: 51`, `import: 10`
* *Defense:* `safety: 9`, `test: 3`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 62.878
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.132353
  * `Imports (Out-Degree: 0):` windows.h, log.h, stdint.h, stdio.h, sokol_log.h, syslog.h, stddef.h, emscripten.h...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/sokol/debugtext.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.823 IQR)
- **Top Global Matches:** file_cluster_8: 9.823, file_cluster_7: 10.17, file_cluster_1: 10.485
- **Magnitude:** 192.14 | **LOC:** 887 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.0776%), Tech Debt (10.3869%)
**Top Internal Functions/Classes:**
  * `asRange` (Impact: 18.4)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `print` (Impact: 5.5)
    * *Intent:* // std.fmt-style formatted print
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `makeContext` (Impact: 3.6)
    * *Intent:* /// context functions
  * `color4b` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 18`, `args: 82`, `func_start: 79`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `dead_code: 3`, `fragile_debt: 1`
* *Architecture:* `api: 74`, `import: 4`
* *Defense:* `safety: 4`, `doc: 59`, `immutability_locks: 33`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` gfx.zig, builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/shape.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.284 IQR)
- **Top Global Matches:** file_cluster_8: 9.284, file_cluster_7: 9.787, file_cluster_1: 10.076
- **Magnitude:** 180.64 | **LOC:** 653 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.6883%), Tech Debt (11.5933%)
**Top Internal Functions/Classes:**
  * `asRange` (Impact: 18.4)
    * *Intent:* // helper function to convert "anything" to a Range struct
  * `color4f` (Impact: 4.6)
    * *Intent:* /// helper functions to build packed color value from floats or bytes
  * `color4b` (Impact: 4.6)
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `color3f` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 30`, `args: 50`, `func_start: 50`, `class_start: 13`
* *Risk/State:* `fragile_debt: 1`
* *Architecture:* `api: 63`, `import: 3`
* *Defense:* `safety: 2`, `doc: 20`, `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` gfx.zig, builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_time.h` (C | Tier 0 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.268 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.564 IQR)
- **Top Global Matches:** file_cluster_8: 12.268, file_cluster_7: 12.71, file_cluster_0: 12.792
- **Magnitude:** 128.62 | **LOC:** 320 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (57.1151%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stm_now` (Impact: 6.7)
  * `stm_setup` (Impact: 6.5)
  * `stm_round_to_common_refresh_rate` (Impact: 4.7)
  * `stm_diff` (Impact: 3.4)
  * `stm_laptime` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 17`, `args: 2`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 57`
* *Architecture:* `api: 39`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 0):` string.h, windows.h, stdint.h, emscripten.h, assert.h, mach_time.h, time.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/sgimgui.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.936 IQR)
- **Top Global Matches:** file_cluster_8: 9.936, file_cluster_7: 10.365, file_cluster_1: 10.698
- **Magnitude:** 127.5 | **LOC:** 388 | **CtrlFlow:** 80.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (4.9536%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `drawMenu` (Impact: 2.1)
  * `drawBufferWindow` (Impact: 2.1)
  * `drawImageWindow` (Impact: 2.1)
  * `drawSamplerWindow` (Impact: 2.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 65`, `func_start: 63`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `dead_code: 2`
* *Architecture:* `api: 63`, `import: 2`
* *Defense:* `doc: 9`, `immutability_locks: 64`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/math.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.058 IQR)
- **Top Global Matches:** file_cluster_8: 9.058, file_cluster_7: 9.736, file_cluster_13: 9.92
- **Magnitude:** 119.36 | **LOC:** 291 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.6581%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `norm` (Impact: 9.1)
  * `mul` (Impact: 7.5)
  * `lookat` (Impact: 5.3)
  * `persp` (Impact: 5.0)
  * `rotate` (Impact: 4.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 27`, `args: 21`, `func_start: 21`, `class_start: 3`
* *Risk/State:* `state_mutation: 9`, `duplicate_logic: 7`
* *Architecture:* `api: 23`, `import: 2`
* *Defense:* `safety: 2`, `test: 7`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 44.774
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.147059
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/sokol/imgui.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.26%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.23 IQR)
- **Top Global Matches:** file_cluster_8: 10.23, file_cluster_7: 10.676, file_cluster_13: 10.958
- **Magnitude:** 102.16 | **LOC:** 601 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (5.3598%), Tech Debt (11.8918%)
**Top Internal Functions/Classes:**
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `imtextureid` (Impact: 3.6)
  * `imtextureidWithSampler` (Impact: 3.6)
  * `textureViewFromImtextureid` (Impact: 3.6)
  * `samplerFromImtextureid` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 9`, `args: 42`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `dead_code: 7`, `fragile_debt: 1`
* *Architecture:* `api: 42`, `import: 4`
* *Defense:* `doc: 14`, `immutability_locks: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` gfx.zig, app.zig, builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_audio.h` (C | Tier 0 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.731 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 3.604 IQR)
- **Top Global Matches:** file_cluster_8: 10.731, file_cluster_7: 11.307, file_cluster_0: 11.442
- **Magnitude:** 83.66 | **LOC:** 2664 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.701%), Tech Debt (41.3513%)
**Top Internal Functions/Classes:**
  * `saudio_suspended` (Impact: 7.7)
  * `saudio_push` (Impact: 7.5)
  * `saudio_expect` (Impact: 4.7)
  * `saudio_shutdown` (Impact: 3.3)
  * `saudio_isvalid` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 32`, `args: 10`, `func_start: 10`
* *Risk/State:* `state_mutation: 16`, `fragile_debt: 1`
* *Architecture:* `api: 33`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.153
  * `Choke Point (Betweenness):` 0.000219 | `Ripple Effect (Closeness):` 0.014706
  * `Imports (Out-Degree: 1):` string.h, audioout.h, windows.h, audioclient.h, AVFoundation.h, assert.h, 3ds.h, winapifamily.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sokol/c/sokol_glue.h` (C | Tier 0 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.28 IQR)
- **Local Micro-Species:** `Cluster 3: Complex Defensive Systems Logic` (Drift: 3.82 IQR)
- **Top Global Matches:** file_cluster_8: 11.28, file_cluster_13: 11.548, file_cluster_0: 11.834
- **Magnitude:** 77.18 | **LOC:** 208 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (50.9601%), Tech Debt (32.1778%)
**Top Internal Functions/Classes:**
  * `_sglue_to_sgpixelformat` (Impact: 10.7)
  * `sglue_swapchain` (Impact: 2.9)
    * *Intent:* #define SOKOL_GLUE_API_DECL SOKOL_API_DECL #endif #ifndef SOKOL_GLUE_API_DECL #if defined(_WIN32) &&...
  * `sglue_environment` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 14`, `args: 4`, `func_start: 3`
* *Risk/State:* `state_mutation: 37`, `fragile_debt: 1`
* *Architecture:* `api: 22`, `import: 2`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.233
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.067227
  * `Imports (Out-Degree: 0):` string.h, assert.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/mrt.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.773 IQR)
- **Top Global Matches:** file_cluster_8: 8.773, file_cluster_13: 9.446, file_cluster_7: 9.469
- **Magnitude:** 68.66 | **LOC:** 314 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.093%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 18.8)
  * `recreateOffscreenAttachments` (Impact: 5.5)
    * *Intent:* // helper function to create or re-create attachment resources
  * `event` (Impact: 4.2)
  * `computeMVP` (Impact: 3.9)
    * *Intent:* // compute model-view-projection matrix
  * `frame` (Impact: 3.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 17`, `args: 7`, `func_start: 7`, `class_start: 5`
* *Risk/State:* `state_mutation: 20`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 6`
* *Defense:* `safety: 3`, `immutability_locks: 29`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sokol, mrt.glsl.zig, math.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/audio.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.416 IQR)
- **Top Global Matches:** file_cluster_8: 10.416, file_cluster_7: 10.825, file_cluster_1: 11.114
- **Magnitude:** 64.02 | **LOC:** 703 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.8783%), Tech Debt (11.0057%)
**Top Internal Functions/Classes:**
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `push` (Impact: 3.6)
    * *Intent:* /// push sample frames from main thread, returns number of frames actually pushed
  * `isvalid` (Impact: 2.1)
    * *Intent:* /// true after setup if audio backend was successfully initialized
  * `userdata` (Impact: 2.1)
    * *Intent:* /// return the saudio_desc.user_data pointer
  * `queryDesc` (Impact: 2.1)
    * *Intent:* /// return a copy of the original saudio_desc struct
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 22`, `args: 28`, `func_start: 23`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `dead_code: 10`, `fragile_debt: 1`
* *Architecture:* `api: 23`, `import: 2`
* *Defense:* `doc: 32`, `immutability_locks: 26`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/instancing.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.617 IQR)
- **Top Global Matches:** file_cluster_8: 9.617, file_cluster_13: 10.115, file_cluster_7: 10.236
- **Magnitude:** 58.42 | **LOC:** 186 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.1034%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `frame` (Impact: 9.3)
  * `init` (Impact: 9.2)
  * `computeVsParams` (Impact: 3.9)
  * `rand` (Impact: 3.6)
  * `xorshift32` (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 13`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 20`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sokol, instancing.glsl.zig, math.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sokol/time.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.103 IQR)
- **Top Global Matches:** file_cluster_8: 8.103, file_cluster_7: 9.009, file_cluster_1: 9.257
- **Magnitude:** 54.16 | **LOC:** 172 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6958%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `cStrToZig` (Impact: 4.2)
    * *Intent:* // helper function to convert a C string to a Zig string slice
  * `diff` (Impact: 3.6)
  * `since` (Impact: 3.6)
  * `laptime` (Impact: 3.6)
  * `roundToCommonRefreshRate` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 12`, `args: 21`, `func_start: 21`
* *Risk/State:* None
* *Architecture:* `api: 15`, `import: 2`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.646
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.165527
  * `Imports (Out-Degree: 0):` builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/sgl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.173 IQR)
- **Top Global Matches:** file_cluster_8: 8.173, file_cluster_7: 8.931, file_cluster_13: 9.157
- **Magnitude:** 49.04 | **LOC:** 258 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.2771%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 10.8)
  * `drawTexCube` (Impact: 4.9)
  * `drawCubes` (Impact: 3.2)
  * `drawQuad` (Impact: 2.4)
  * `frame` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `safety: 2`, `test: 1`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sokol, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/offscreen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.897 IQR)
- **Top Global Matches:** file_cluster_8: 8.897, file_cluster_13: 9.405, file_cluster_7: 9.514
- **Magnitude:** 48.28 | **LOC:** 215 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.5974%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 13.4)
  * `computeVsParams` (Impact: 4.9)
  * `frame` (Impact: 1.5)
  * `main` (Impact: 1.5)
  * `cleanup` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 17`, `args: 5`, `func_start: 5`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 18`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sokol, offscreen.glsl.zig, math.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/shapes.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.119 IQR)
- **Top Global Matches:** file_cluster_8: 8.119, file_cluster_13: 8.799, file_cluster_7: 8.867
- **Magnitude:** 44.86 | **LOC:** 200 | **CtrlFlow:** 40.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.0538%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `input` (Impact: 8.6)
  * `init` (Impact: 8.4)
  * `frame` (Impact: 4.5)
  * `main` (Impact: 1.5)
  * `cleanup` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 12`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 5`
* *Defense:* `safety: 1`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shapes.glsl.zig, sokol, math.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/instancing-compute.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.442 IQR)
- **Top Global Matches:** file_cluster_8: 8.442, file_cluster_13: 9.046, file_cluster_7: 9.095
- **Magnitude:** 43.18 | **LOC:** 203 | **CtrlFlow:** 52.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.2574%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 13.8)
  * `frame` (Impact: 6.0)
  * `computeVsParams` (Impact: 3.9)
  * `main` (Impact: 1.5)
  * `drawFallback` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `args: 6`, `func_start: 6`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 8`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sokol, instancing-compute.glsl.zig, math.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/blend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.61 IQR)
- **Top Global Matches:** file_cluster_8: 9.61, file_cluster_13: 9.936, file_cluster_7: 10.228
- **Magnitude:** 41.54 | **LOC:** 152 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.0174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 11.2)
  * `frame` (Impact: 5.0)
  * `main` (Impact: 1.5)
  * `cleanup` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 10`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 16`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 4`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` sokol, blend.glsl.zig, math.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/texcube.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.727 IQR)
- **Top Global Matches:** file_cluster_8: 7.727, file_cluster_7: 8.53, file_cluster_13: 8.647
- **Magnitude:** 30.7 | **LOC:** 181 | **CtrlFlow:** 38.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.1197%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 8.5)
  * `computeVsParams` (Impact: 3.9)
  * `frame` (Impact: 1.5)
  * `main` (Impact: 1.5)
  * `cleanup` (Impact: 1.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 8`, `args: 5`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` texcube.glsl.zig, sokol, math.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/debugtext-userfont.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.573 IQR)
- **Top Global Matches:** file_cluster_8: 7.573, file_cluster_7: 8.449, file_cluster_1: 8.766
- **Magnitude:** 30.08 | **LOC:** 252 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.7189%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 4.4)
  * `frame` (Impact: 4.2)
  * `main` (Impact: 1.5)
  * `cleanup` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 4`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`, `orphaned_logic: 1`
* *Architecture:* `api: 4`, `import: 1`
* *Defense:* `safety: 1`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 8.528
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` sokol
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/sokol/c/sokol_app.h` (C) | Magnitude: 1784.68 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1533, api: 648, structural_boundaries: 576, state_mutation: 564
- `src/sokol/c/sokol_log.h` (C) | Magnitude: 311.52 | Delta: **0.162 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 194, state_mutation: 147, branch: 81, macros: 71
- `src/sokol/sokol.zig` (ZIG) | Magnitude: 27.24 | Delta: **0.551 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 12, globals: 12, import: 12, immutability_locks: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/sokol/c/sokol_fetch.h` (C) | Magnitude: 504.36 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 366, api: 206, pointers: 188, state_mutation: 152

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/sokol/c/sokol_shape.h` (C) | Magnitude: 1437.82 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 842, indent_spaces: 621, api: 368, immutability_locks: 186
- `src/sokol/c/sokol_glue.c` (C) | Magnitude: 13.64 | Delta: **0.166 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 4, macros: 3, branch: 1
- `src/sokol/c/sokol_gfx.h` (C) | Magnitude: 10704.0 | Delta: **0.211 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 9337, state_mutation: 6394, pointers: 3755, branch: 2671
- `src/sokol/c/sokol_debugtext.c` (C) | Magnitude: 13.12 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 3, macros: 3, branch: 1
- `src/sokol/c/sokol_gl.c` (C) | Magnitude: 13.12 | Delta: **0.239 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 3, macros: 3, branch: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/sokol/c/sokol_gfx.h` -> Churn: **100.0%** | Cog Load: 62.4873% | Debt: 10.8168%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sokol/c/sokol_gfx.h` -> **GH Action** (95.2% isolated ownership) | Magnitude: 10704.0
- `src/sokol/c/sokol_app.h` -> **GH Action** (96.4% isolated ownership) | Magnitude: 1784.68
- `src/sokol/c/sokol_fetch.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 504.36
- `src/sokol/c/sokol_log.h` -> **GH Action** (100.0% isolated ownership) | Magnitude: 311.52
- `src/sokol/shape.zig` -> **GH Action** (100.0% isolated ownership) | Magnitude: 180.64

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sokol/c/sokol_gfx.h` -> **Severity: 0.34** (Bridge: 0.0034 * Flux: 100.0%)
- `src/sokol/c/sokol_app.h` -> **Severity: 0.055** (Bridge: 0.0005 * Flux: 99.9652%)
- `src/sokol/c/sokol_fetch.h` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 99.9758%)
- `src/sokol/c/sokol_audio.h` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 97.1431%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sokol/sgimgui.zig` -> **Severity: 11.793** (Embedded: 0.1655 * Error Risk: 71.247%)
- `src/sokol/c/sokol_log.h` -> **Severity: 11.516** (Embedded: 0.1324 * Error Risk: 87.0079%)
- `src/sokol/log.zig` -> **Severity: 10.628** (Embedded: 0.1655 * Error Risk: 64.2071%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 9.608** (Embedded: 0.1029 * Error Risk: 93.3343%)
- `src/sokol/imgui.zig` -> **Severity: 8.885** (Embedded: 0.1655 * Error Risk: 53.6766%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sokol/sokol.zig` -> **Severity: 9961.28** (Blast Radius: 124.516 * Doc Risk: 80.0%)
- `src/sokol/c/sokol_log.h` -> **Severity: 6287.8** (Blast Radius: 62.878 * Doc Risk: 100.0%)
- `src/sokol/c/sokol_gfx.h` -> **Severity: 2785.9** (Blast Radius: 27.859 * Doc Risk: 100.0%)
- `src/sokol/sgimgui.zig` -> **Severity: 2364.6** (Blast Radius: 23.646 * Doc Risk: 100.0%)
- `src/sokol/shape.zig` -> **Severity: 2364.6** (Blast Radius: 23.646 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
