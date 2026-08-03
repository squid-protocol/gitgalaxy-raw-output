# ARCHITECTURAL_BRIEF: godot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/godot` |
| **Timestamp** | `2026-08-03T20:57:09.612879+00:00` |
| **Scan Duration** | `49.82s` |
| **Git Branch** | `master` |
| **Git Commit** | `4a919adccf8e398aceca75399c539078c54fe97f` |
| **Git Remote** | `https://github.com/godotengine/godot.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7913 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
| Total Artifacts | 14219 |
| Analyzed Artifacts (Scanned) | 10020 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4199 |
| Total LOC | 1554144 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 70.5% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0596 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 548 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 5991 | 1278033 | 59.8% |
| XML | 1403 | 34 | 14.0% |
| C | 809 | 158650 | 8.1% |
| PLAINTEXT | 673 | 4 | 6.7% |
| PYTHON | 327 | 15991 | 3.3% |
| CSHARP | 247 | 27074 | 2.5% |
| JAVA | 190 | 22004 | 1.9% |
| GLSL | 133 | 23988 | 1.3% |
| OBJECTIVE-C | 119 | 16107 | 1.2% |
| KOTLIN | 50 | 5826 | 0.5% |
| JAVASCRIPT | 26 | 5237 | 0.3% |
| MARKDOWN | 24 | 0 | 0.2% |
| BINARY_THREAT | 7 | 7 | 0.1% |
| SHELL | 6 | 304 | 0.1% |
| GROOVY | 5 | 292 | 0.0% |
| JSON | 3 | 363 | 0.0% |
| YAML | 2 | 105 | 0.0% |
| CSV | 2 | 11 | 0.0% |
| MAKEFILE | 1 | 25 | 0.0% |
| SWIFT | 1 | 22 | 0.0% |
| BATCH | 1 | 67 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.454`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 6001 | 59.9% |
| file_cluster_13 | 2668 | 26.6% |
| file_cluster_9 | 318 | 3.2% |
| file_cluster_12 | 86 | 0.9% |
| file_cluster_16 | 60 | 0.6% |
| file_cluster_0 | 43 | 0.4% |
| file_cluster_7 | 42 | 0.4% |
| file_cluster_11 | 32 | 0.3% |
| file_cluster_4 | 17 | 0.2% |
| file_cluster_2 | 15 | 0.1% |
| Unknown | 11 | 0.1% |
| file_cluster_17 | 4 | 0.0% |
| file_cluster_1 | 3 | 0.0% |
| file_cluster_6 | 1 | 0.0% |
| file_cluster_15 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 701 | 7.0% |
| Static: Minified & Vendor Opaque Mass | 17 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4199*

**Composition by Extension & Reason:**
- `.xml`: 946x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.gd`: 754x Unsupported Format (.gd), 39x Excluded: Neighborhood Micro-Mass Limit Exceeded, 10x Excluded (Unsupported Extension: '.gd')
- `.cpp`: 562x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Saturation: Line 13 exceeds 500 chars), 1x Excluded (Embedded Hex Payload: 7192 hex tokens in 3653 LOC)
- `.c`: 474x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 68 LOC), 1x Excluded (Machine-Generated Source Code Signature: 14005 LOC)
- `.hpp`: 187x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out`: 136x Excluded: Neighborhood Micro-Mass Limit Exceeded, 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.cfg`: 131x Unsupported Format (.cfg)
- `no_extension`: 125x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Machine-Generated Source Code Signature: 2433 LOC)
- `.po`: 113x Excluded (Unsupported Extension: '.po')
- `.patch`: 82x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.strings`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 10x Excluded (Saturation: Line 13 exceeds 500 chars), 2x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.cs`: 52x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 258 LOC), 1x Excluded (Machine-Generated Source Code Signature: 22 LOC)
- `.txt`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 47748 commas in 2223 LOC)
- `.svg`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 27.2 | 12.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 33.4 | 16.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 29.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 20.4 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.9 | 2.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 54.3 | 86.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.6 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 30.8 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 27.9 | 14.5 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 14.0 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 99.8 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.3 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `methods.py` (Hits: 97)
- `platform/windows/detect.py` (Hits: 73)
- `thirdparty/libwebp/src/dsp/dec_neon.c` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **class_db.h** (`core/object/class_db.h`) — 831 inbound connections
2. **callable_mp.h** (`core/object/callable_mp.h`) — 444 inbound connections
3. **project_settings.h** (`core/config/project_settings.h`) — 314 inbound connections
4. **os.h** (`core/os/os.h`) — 286 inbound connections
5. **engine.h** (`core/config/engine.h`) — 248 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **register_scene_types.cpp** (`scene/register_scene_types.cpp`) — 313 outbound dependencies
2. **editor_node.cpp** (`editor/editor_node.cpp`) — 156 outbound dependencies
3. **register_editor_types.cpp** (`editor/register_editor_types.cpp`) — 111 outbound dependencies
4. **node_3d_editor_plugin.cpp** (`editor/scene/3d/node_3d_editor_plugin.cpp`) — 84 outbound dependencies
5. **main.cpp** (`main/main.cpp`) — 84 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `DecodePixelData` (@ `thirdparty/tinyexr/tinyexr.h`) -> Impact: **11038.3** | LOC: 1688
- `match_input` (@ `thirdparty/harfbuzz/src/hb-ot-layout-gsubgpos.hh`) -> Impact: **5193.2** | LOC: 1711
- `ShaderLanguage::_validate_operator` (@ `servers/rendering/shader_language.cpp`) -> Impact: **4690.2** | LOC: 1838
- `getCompleteString` (@ `thirdparty/glslang/glslang/Include/Types.h`) -> Impact: **2685.8** | LOC: 377
- `HB_MARK_AS_FLAG_T` (@ `thirdparty/harfbuzz/src/hb-ot-layout-common.hh`) -> Impact: **2382.4** | LOC: 1817
- `PointInOpPolygon` (@ `thirdparty/clipper2/src/clipper.engine.cpp`) -> Impact: **2308.0** | LOC: 1473
- `find_text_end` (@ `thirdparty/pcre2/src/pcre2_substitute.c`) -> Impact: **2048.1** | LOC: 921
  * *Intent:* * Neither the name of the University of Cambridge nor the names of its
- `ft_bitmap_assure_buffer` (@ `thirdparty/freetype/src/base/ftbitmap.c`) -> Impact: **2043.8** | LOC: 836
- `ft_glyphslot_clear` (@ `thirdparty/freetype/src/base/ftobjs.c`) -> Impact: **1916.8** | LOC: 1517
- `RichTextLabel::_add_list_prefixes` (@ `scene/gui/rich_text_label.cpp`) -> Impact: **1808.2** | LOC: 1283

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `include_file_in_gles3_header` (@ `gles3_builders.py`) -> **O(2^N) [Recursive]**
- `include_file_in_rd_header` (@ `glsl_builders.py`) -> **O(2^N) [Recursive]**
- `configure_mingw` (@ `platform/windows/detect.py`) -> **O(2^N) [Recursive]**
- `detect_build_env_arch` (@ `platform/windows/detect.py`) -> **O(2^N) [Recursive]**
- `vk_object_to_tracked_object` (@ `drivers/vulkan/rendering_context_driver_vulkan.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif #if defined(VK_TRACK_DRIVER_MEMORY) || defined(VK_TRACK_DEVICE_MEMORY)
- `SpdSetup` (@ `thirdparty/amd-fsr2/shaders/ffx_spd.h`) -> **O(2^N) [Recursive]**
- `BrotliTakeBits` (@ `thirdparty/brotli/dec/bit_reader.h`) -> **O(2^N) [Recursive]**
  * *Intent:* #endif
- `Init` (@ `thirdparty/cvtt/ConvectionKernels_IndexSelector.h`) -> **O(2^N) [Recursive]**
- `CreateAdapterListByWorkload` (@ `thirdparty/directx_headers/include/directx/dxcore_interface.h`) -> **O(2^N) [Recursive]**
- `SetState` (@ `thirdparty/directx_headers/include/directx/dxcore_interface.h`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `get_ise_sequence_bits` (@ `thirdparty/basis_universal/transcoder/basisu_astc_helpers.h`) -> DB Complexity: **889**
- `ShaderLanguage::_validate_operator` (@ `servers/rendering/shader_language.cpp`) -> DB Complexity: **776**
- `RichTextLabel::_add_list_prefixes` (@ `scene/gui/rich_text_label.cpp`) -> DB Complexity: **744**
- `color_distance` (@ `thirdparty/basis_universal/encoder/basisu_enc.h`) -> DB Complexity: **723**
- `Animation::_set` (@ `scene/resources/animation.cpp`) -> DB Complexity: **549**
  * *Intent:* /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF */ /* MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. */ ...
- `RenderingDeviceDriverVulkan::_add_queue_` (@ `drivers/vulkan/rendering_device_driver_vulkan.cpp`) -> DB Complexity: **534**
- `blendv_mask_ps` (@ `thirdparty/basis_universal/encoder/cppspmd_sse.h`) -> DB Complexity: **532**
- `ProjectConverter3To4::fix_tool_declarati` (@ `editor/project_upgrade/project_converter_3_to_4.cpp`) -> DB Complexity: **531**
  * *Intent:* // Check file by file.
- `PointInOpPolygon` (@ `thirdparty/clipper2/src/clipper.engine.cpp`) -> DB Complexity: **529**
- `DecodePixelData` (@ `thirdparty/tinyexr/tinyexr.h`) -> DB Complexity: **523**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `thirdparty/harfbuzz/src` | 325 | 118148.7 | 55.76% | 40.02% |
| `scene/resources` | 136 | 46914.84 | 33.22% | 50.28% |
| `scene/gui` | 130 | 44812.0 | 32.98% | 37.19% |
| `servers/rendering` | 61 | 39248.94 | 42.01% | 42.51% |
| `thirdparty/embree/common/math` | 28 | 35753.78 | 36.04% | 74.74% |
| `thirdparty/pcre2/src` | 41 | 35194.38 | 56.44% | 17.42% |
| `scene/3d` | 117 | 31331.46 | 35.97% | 46.02% |
| `thirdparty/libwebp/src/dsp` | 76 | 29996.57 | 63.4% | 3.72% |
| `core/math` | 89 | 28981.28 | 49.76% | 59.89% |
| `thirdparty/embree/kernels/geometry` | 70 | 27884.02 | 54.56% | 91.36% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `misc/utility/godot_gdb_pretty_print.py` -> **100.0%** Exposure
- `core/crypto/crypto_core.cpp` -> **100.0%** Exposure
- `core/extension/gdextension_function_loader.cpp` -> **100.0%** Exposure
- `core/io/file_access_encrypted.cpp` -> **100.0%** Exposure
- `core/io/missing_resource.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `editor/icons/editor_icons_builders.py` -> **100.0%** Exposure
- `misc/scripts/install_angle.py` -> **100.0%** Exposure
- `platform/web/emscripten_helpers.py` -> **100.0%** Exposure
- `core/config/engine.cpp` -> **100.0%** Exposure
- `core/config/engine.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scene/resources/visual_shader_nodes.cpp` -> **147** Orphaned Functions | **103** Duplicates
- `servers/text/text_server_extension.cpp` -> **203** Orphaned Functions | **45** Duplicates
- `servers/display/display_server.cpp` -> **167** Orphaned Functions | **78** Duplicates
- `modules/jolt_physics/jolt_physics_server_3d.cpp` -> **176** Orphaned Functions | **56** Duplicates
- `core/input/input_event.cpp` -> **211** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`SConstruct`** -> AI Confidence: **99.48%**
2. **`platform/linuxbsd/detect.py`** -> AI Confidence: **99.48%**
3. **`core/extension/extension_api_dump.cpp`** -> AI Confidence: **99.48%**
4. **`core/io/image.cpp`** -> AI Confidence: **99.48%**
5. **`core/io/logger.cpp`** -> AI Confidence: **99.48%**
6. **`core/io/marshalls.cpp`** -> AI Confidence: **99.48%**
7. **`core/io/resource_format_binary.cpp`** -> AI Confidence: **99.48%**
8. **`core/object/script_language.cpp`** -> AI Confidence: **99.48%**
9. **`core/variant/variant_parser.cpp`** -> AI Confidence: **99.48%**
10. **`drivers/d3d12/rendering_device_driver_d3d12.cpp`** -> AI Confidence: **99.48%**
11. **`drivers/gles3/rasterizer_canvas_gles3.cpp`** -> AI Confidence: **99.48%**
12. **`drivers/gles3/rasterizer_gles3.cpp`** -> AI Confidence: **99.48%**
13. **`drivers/metal/metal_device_properties.cpp`** -> AI Confidence: **99.48%**
14. **`drivers/metal/rendering_shader_container_metal.cpp`** -> AI Confidence: **99.48%**
15. **`drivers/sdl/joypad_sdl.cpp`** -> AI Confidence: **99.48%**
16. **`drivers/vulkan/rendering_device_driver_vulkan.cpp`** -> AI Confidence: **99.48%**
17. **`editor/animation/animation_bezier_editor.cpp`** -> AI Confidence: **99.48%**
18. **`editor/animation/animation_blend_space_1d_editor.cpp`** -> AI Confidence: **99.48%**
19. **`editor/animation/animation_blend_space_2d_editor.cpp`** -> AI Confidence: **99.48%**
20. **`editor/animation/animation_blend_tree_editor_plugin.cpp`** -> AI Confidence: **99.48%**
21. **`editor/animation/animation_library_editor.cpp`** -> AI Confidence: **99.48%**
22. **`editor/animation/animation_player_editor_plugin.cpp`** -> AI Confidence: **99.48%**
23. **`editor/animation/animation_state_machine_editor.cpp`** -> AI Confidence: **99.48%**
24. **`editor/animation/animation_track_editor.cpp`** -> AI Confidence: **99.48%**
25. **`editor/audio/editor_audio_buses.cpp`** -> AI Confidence: **99.48%**
26. **`editor/debugger/debugger_editor_plugin.cpp`** -> AI Confidence: **99.48%**
27. **`editor/debugger/editor_debugger_tree.cpp`** -> AI Confidence: **99.48%**
28. **`editor/doc/doc_tools.cpp`** -> AI Confidence: **99.48%**
29. **`editor/doc/editor_help_search.cpp`** -> AI Confidence: **99.48%**
30. **`editor/docks/filesystem_dock.cpp`** -> AI Confidence: **99.48%**
31. **`editor/docks/history_dock.cpp`** -> AI Confidence: **99.48%**
32. **`editor/docks/inspector_dock.cpp`** -> AI Confidence: **99.48%**
33. **`editor/docks/scene_tree_dock.cpp`** -> AI Confidence: **99.48%**
34. **`editor/editor_node.cpp`** -> AI Confidence: **99.48%**
35. **`editor/export/codesign.cpp`** -> AI Confidence: **99.48%**
36. **`editor/export/shader_baker_export_plugin.cpp`** -> AI Confidence: **99.48%**
37. **`editor/gui/credits_roll.cpp`** -> AI Confidence: **99.48%**
38. **`editor/gui/editor_toaster.cpp`** -> AI Confidence: **99.48%**
39. **`editor/import/3d/editor_import_collada.cpp`** -> AI Confidence: **99.48%**
40. **`editor/import/3d/post_import_plugin_skeleton_renamer.cpp`** -> AI Confidence: **99.48%**
41. **`editor/import/3d/post_import_plugin_skeleton_rest_fixer.cpp`** -> AI Confidence: **99.48%**
42. **`editor/import/3d/resource_importer_obj.cpp`** -> AI Confidence: **99.48%**
43. **`editor/import/3d/resource_importer_scene.cpp`** -> AI Confidence: **99.48%**
44. **`editor/import/3d/scene_import_settings.cpp`** -> AI Confidence: **99.48%**
45. **`editor/import/dynamic_font_import_settings.cpp`** -> AI Confidence: **99.48%**
46. **`editor/import/resource_importer_layered_texture.cpp`** -> AI Confidence: **99.48%**
47. **`editor/import/resource_importer_texture.cpp`** -> AI Confidence: **99.48%**
48. **`editor/inspector/editor_inspector.cpp`** -> AI Confidence: **99.48%**
49. **`editor/inspector/editor_properties_array_dict.cpp`** -> AI Confidence: **99.48%**
50. **`editor/inspector/editor_properties_vector.cpp`** -> AI Confidence: **99.48%**
51. **`editor/inspector/editor_resource_picker.cpp`** -> AI Confidence: **99.48%**
52. **`editor/inspector/property_selector.cpp`** -> AI Confidence: **99.48%**
53. **`editor/plugins/editor_plugin_settings.cpp`** -> AI Confidence: **99.48%**
54. **`editor/plugins/plugin_config_dialog.cpp`** -> AI Confidence: **99.48%**
55. **`editor/project_manager/engine_update_label.cpp`** -> AI Confidence: **99.48%**
56. **`editor/project_manager/project_dialog.cpp`** -> AI Confidence: **99.48%**
57. **`editor/project_upgrade/project_converter_3_to_4.cpp`** -> AI Confidence: **99.48%**
58. **`editor/run/editor_run.cpp`** -> AI Confidence: **99.48%**
59. **`editor/run/embedded_process.cpp`** -> AI Confidence: **99.48%**
60. **`editor/scene/2d/camera_2d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
61. **`editor/scene/2d/path_2d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
62. **`editor/scene/2d/physics/collision_shape_2d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
63. **`editor/scene/2d/scene_paint_2d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
64. **`editor/scene/2d/tiles/tile_proxies_manager_dialog.cpp`** -> AI Confidence: **99.48%**
65. **`editor/scene/2d/tiles/tile_set_atlas_source_editor.cpp`** -> AI Confidence: **99.48%**
66. **`editor/scene/2d/tiles/tile_set_editor.cpp`** -> AI Confidence: **99.48%**
67. **`editor/scene/3d/bone_map_editor_plugin.cpp`** -> AI Confidence: **99.48%**
68. **`editor/scene/3d/gizmos/audio_stream_player_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.48%**
69. **`editor/scene/3d/gizmos/gpu_particles_collision_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.48%**
70. **`editor/scene/3d/gizmos/physics/joint_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.48%**
71. **`editor/scene/3d/lightmap_gi_editor_plugin.cpp`** -> AI Confidence: **99.48%**
72. **`editor/scene/3d/mesh_instance_3d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
73. **`editor/scene/3d/mesh_library_editor_plugin.cpp`** -> AI Confidence: **99.48%**
74. **`editor/scene/3d/node_3d_editor_plugin.cpp`** -> AI Confidence: **99.48%**
75. **`editor/scene/canvas_item_editor_plugin.cpp`** -> AI Confidence: **99.48%**
76. **`editor/scene/editor_scene_tabs.cpp`** -> AI Confidence: **99.48%**
77. **`editor/scene/gradient_editor_plugin.cpp`** -> AI Confidence: **99.48%**
78. **`editor/scene/gui/theme_editor_plugin.cpp`** -> AI Confidence: **99.48%**
79. **`editor/scene/scene_create_dialog.cpp`** -> AI Confidence: **99.48%**
80. **`editor/scene/scene_tree_editor.cpp`** -> AI Confidence: **99.48%**
81. **`editor/scene/texture/texture_region_editor_plugin.cpp`** -> AI Confidence: **99.48%**
82. **`editor/script/script_create_dialog.cpp`** -> AI Confidence: **99.48%**
83. **`editor/script/script_editor_plugin.cpp`** -> AI Confidence: **99.48%**
84. **`editor/script/script_text_editor.cpp`** -> AI Confidence: **99.48%**
85. **`editor/settings/editor_folding.cpp`** -> AI Confidence: **99.48%**
86. **`editor/settings/editor_settings_dialog.cpp`** -> AI Confidence: **99.48%**
87. **`editor/settings/input_event_configuration_dialog.cpp`** -> AI Confidence: **99.48%**
88. **`editor/shader/text_shader_editor.cpp`** -> AI Confidence: **99.48%**
89. **`editor/shader/visual_shader_editor_plugin.cpp`** -> AI Confidence: **99.48%**
90. **`editor/themes/theme_classic.cpp`** -> AI Confidence: **99.48%**
91. **`editor/themes/theme_modern.cpp`** -> AI Confidence: **99.48%**
92. **`editor/translations/editor_locale_dialog.cpp`** -> AI Confidence: **99.48%**
93. **`main/main.cpp`** -> AI Confidence: **99.48%**
94. **`modules/betsy/image_compress_betsy.cpp`** -> AI Confidence: **99.48%**
95. **`modules/gdscript/editor/gdscript_highlighter.cpp`** -> AI Confidence: **99.48%**
96. **`modules/gdscript/gdscript_analyzer.cpp`** -> AI Confidence: **99.48%**
97. **`modules/gdscript/gdscript_compiler.cpp`** -> AI Confidence: **99.48%**
98. **`modules/gdscript/gdscript_parser.cpp`** -> AI Confidence: **99.48%**
99. **`modules/gdscript/language_server/gdscript_text_document.cpp`** -> AI Confidence: **99.48%**
100. **`modules/gdscript/tests/test_completion.h`** -> AI Confidence: **99.48%**
101. **`modules/gdscript/tests/test_gdscript.cpp`** -> AI Confidence: **99.48%**
102. **`modules/gltf/extensions/physics/gltf_physics_body.cpp`** -> AI Confidence: **99.48%**
103. **`modules/gridmap/editor/grid_map_editor_plugin.cpp`** -> AI Confidence: **99.48%**
104. **`modules/interactive_music/editor/audio_stream_interactive_editor_plugin.cpp`** -> AI Confidence: **99.48%**
105. **`modules/ktx/texture_loader_ktx.cpp`** -> AI Confidence: **99.48%**
106. **`modules/lightmapper_rd/lightmapper_rd.cpp`** -> AI Confidence: **99.48%**
107. **`modules/mono/editor/bindings_generator.cpp`** -> AI Confidence: **99.48%**
108. **`modules/mono/editor/code_completion.cpp`** -> AI Confidence: **99.48%**
109. **`modules/multiplayer/scene_rpc_interface.cpp`** -> AI Confidence: **99.48%**
110. **`modules/navigation_2d/2d/nav_mesh_queries_2d.cpp`** -> AI Confidence: **99.48%**
111. **`modules/objectdb_profiler/editor/snapshot_data.cpp`** -> AI Confidence: **99.48%**
112. **`modules/openxr/openxr_platform_inc.h`** -> AI Confidence: **99.48%**
113. **`modules/openxr/register_types.cpp`** -> AI Confidence: **99.48%**
114. **`modules/text_server_adv/text_server_adv.cpp`** -> AI Confidence: **99.48%**
115. **`modules/text_server_adv/thorvg_svg_in_ot.cpp`** -> AI Confidence: **99.48%**
116. **`modules/text_server_fb/text_server_fb.cpp`** -> AI Confidence: **99.48%**
117. **`modules/text_server_fb/thorvg_svg_in_ot.cpp`** -> AI Confidence: **99.48%**
118. **`platform/android/editor/editor_utils_jni.cpp`** -> AI Confidence: **99.48%**
119. **`platform/android/export/export_plugin.cpp`** -> AI Confidence: **99.48%**
120. **`platform/linuxbsd/crash_handler_linuxbsd.cpp`** -> AI Confidence: **99.48%**
121. **`platform/linuxbsd/wayland/detect_prime_egl.cpp`** -> AI Confidence: **99.48%**
122. **`platform/linuxbsd/x11/display_server_x11.cpp`** -> AI Confidence: **99.48%**
123. **`scene/2d/tile_map_layer.cpp`** -> AI Confidence: **99.48%**
124. **`scene/3d/label_3d.cpp`** -> AI Confidence: **99.48%**
125. **`scene/debugger/runtime_node_select.cpp`** -> AI Confidence: **99.48%**
126. **`scene/debugger/view_3d_controller.cpp`** -> AI Confidence: **99.48%**
127. **`scene/gui/code_edit.cpp`** -> AI Confidence: **99.48%**
128. **`scene/gui/graph_node.cpp`** -> AI Confidence: **99.48%**
129. **`scene/gui/line_edit.cpp`** -> AI Confidence: **99.48%**
130. **`scene/gui/popup.cpp`** -> AI Confidence: **99.48%**
131. **`scene/gui/popup_menu.cpp`** -> AI Confidence: **99.48%**
132. **`scene/gui/progress_bar.cpp`** -> AI Confidence: **99.48%**
133. **`scene/gui/rich_text_label.cpp`** -> AI Confidence: **99.48%**
134. **`scene/gui/scroll_bar.cpp`** -> AI Confidence: **99.48%**
135. **`scene/gui/scroll_container.cpp`** -> AI Confidence: **99.48%**
136. **`scene/gui/spin_box.cpp`** -> AI Confidence: **99.48%**
137. **`scene/gui/split_container.cpp`** -> AI Confidence: **99.48%**
138. **`scene/main/scene_tree_fti.cpp`** -> AI Confidence: **99.48%**
139. **`scene/property_utils.cpp`** -> AI Confidence: **99.48%**
140. **`scene/register_scene_types.cpp`** -> AI Confidence: **99.48%**
141. **`scene/resources/3d/importer_mesh.cpp`** -> AI Confidence: **99.48%**
142. **`scene/resources/packed_scene.cpp`** -> AI Confidence: **99.48%**
143. **`servers/rendering/renderer_rd/environment/gi.cpp`** -> AI Confidence: **99.48%**
144. **`servers/rendering/renderer_rd/environment/sky.cpp`** -> AI Confidence: **99.48%**
145. **`servers/rendering/renderer_rd/forward_clustered/render_forward_clustered.cpp`** -> AI Confidence: **99.48%**
146. **`servers/rendering/renderer_rd/forward_mobile/render_forward_mobile.cpp`** -> AI Confidence: **99.48%**
147. **`servers/rendering/renderer_rd/storage_rd/material_storage.cpp`** -> AI Confidence: **99.48%**
148. **`servers/rendering/renderer_rd/storage_rd/texture_storage.cpp`** -> AI Confidence: **99.48%**
149. **`servers/rendering/renderer_scene_cull.cpp`** -> AI Confidence: **99.48%**
150. **`servers/rendering/renderer_viewport.cpp`** -> AI Confidence: **99.48%**
151. **`servers/rendering/rendering_server.cpp`** -> AI Confidence: **99.48%**
152. **`servers/rendering/shader_language.cpp`** -> AI Confidence: **99.48%**
153. **`servers/text/text_server.cpp`** -> AI Confidence: **99.48%**
154. **`tests/scene/test_control.cpp`** -> AI Confidence: **99.48%**
155. **`tests/scene/test_viewport.cpp`** -> AI Confidence: **99.48%**
156. **`thirdparty/embree/common/simd/avx.h`** -> AI Confidence: **99.48%**
157. **`thirdparty/graphite/src/Collider.cpp`** -> AI Confidence: **99.48%**
158. **`thirdparty/graphite/src/Justifier.cpp`** -> AI Confidence: **99.48%**
159. **`thirdparty/graphite/src/Segment.cpp`** -> AI Confidence: **99.48%**
160. **`thirdparty/harfbuzz/src/hb-raster-svg-render.cc`** -> AI Confidence: **99.48%**
161. **`thirdparty/harfbuzz/src/hb-vector-svg-subset.cc`** -> AI Confidence: **99.48%**
162. **`thirdparty/icu4c/common/unicode/platform.h`** -> AI Confidence: **99.48%**
163. **`thirdparty/mbedtls/include/mbedtls/build_info.h`** -> AI Confidence: **99.48%**
164. **`thirdparty/mbedtls/include/mbedtls/config_psa.h`** -> AI Confidence: **99.48%**
165. **`thirdparty/mbedtls/include/mbedtls/pkcs5.h`** -> AI Confidence: **99.48%**
166. **`thirdparty/mbedtls/include/psa/crypto_builtin_primitives.h`** -> AI Confidence: **99.48%**
167. **`thirdparty/sdl/include/SDL3/SDL_endian.h`** -> AI Confidence: **99.48%**
168. **`thirdparty/sdl/include/SDL3/SDL_intrin.h`** -> AI Confidence: **99.48%**
169. **`thirdparty/thorvg/src/common/tvgStr.cpp`** -> AI Confidence: **99.48%**
170. **`thirdparty/thorvg/src/loaders/svg/tvgSvgPath.cpp`** -> AI Confidence: **99.48%**
171. **`thirdparty/zlib/gzguts.h`** -> AI Confidence: **99.48%**
172. **`thirdparty/zlib/zutil.h`** -> AI Confidence: **99.48%**
173. **`drivers/apple_embedded/app_delegate_service.mm`** -> AI Confidence: **99.48%**
174. **`drivers/apple_embedded/apple_embedded.mm`** -> AI Confidence: **99.48%**
175. **`drivers/apple_embedded/display_server_apple_embedded.mm`** -> AI Confidence: **99.48%**
176. **`drivers/apple_embedded/godot_view_apple_embedded.mm`** -> AI Confidence: **99.48%**
177. **`drivers/apple_embedded/godot_view_controller.mm`** -> AI Confidence: **99.48%**
178. **`drivers/apple_embedded/os_apple_embedded.mm`** -> AI Confidence: **99.48%**
179. **`platform/ios/display_layer_ios.mm`** -> AI Confidence: **99.48%**
180. **`platform/ios/main_ios.mm`** -> AI Confidence: **99.48%**
181. **`platform/macos/crash_handler_macos.mm`** -> AI Confidence: **99.48%**
182. **`platform/macos/display_server_macos.mm`** -> AI Confidence: **99.48%**
183. **`platform/macos/display_server_macos_base.mm`** -> AI Confidence: **99.48%**
184. **`platform/macos/display_server_macos_embedded.mm`** -> AI Confidence: **99.48%**
185. **`platform/macos/editor/embedded_game_view_plugin.mm`** -> AI Confidence: **99.48%**
186. **`platform/macos/editor/embedded_process_macos.mm`** -> AI Confidence: **99.48%**
187. **`platform/macos/embedded_debugger.mm`** -> AI Confidence: **99.48%**
188. **`platform/macos/godot_application_delegate.mm`** -> AI Confidence: **99.48%**
189. **`platform/macos/godot_content_view.mm`** -> AI Confidence: **99.48%**
190. **`platform/macos/os_macos.mm`** -> AI Confidence: **99.48%**
191. **`platform/visionos/main_visionos.mm`** -> AI Confidence: **99.48%**
192. **`platform/android/java/app/src/androidTestInstrumented/java/com/godot/game/GodotAppTest.kt`** -> AI Confidence: **99.48%**
193. **`platform/android/java/app/src/instrumented/java/com/godot/game/test/GodotAppInstrumentedTestPlugin.kt`** -> AI Confidence: **99.48%**
194. **`platform/android/java/editor/src/main/java/org/godotengine/editor/BaseGodotEditor.kt`** -> AI Confidence: **99.48%**
195. **`platform/android/java/editor/src/main/java/org/godotengine/editor/BaseGodotGame.kt`** -> AI Confidence: **99.48%**
196. **`platform/android/java/editor/src/main/java/org/godotengine/editor/EditorMessageDispatcher.kt`** -> AI Confidence: **99.48%**
197. **`platform/android/java/editor/src/main/java/org/godotengine/editor/GodotGame.kt`** -> AI Confidence: **99.48%**
198. **`platform/android/java/editor/src/main/java/org/godotengine/editor/buildprovider/GradleBuildEnvironmentClient.kt`** -> AI Confidence: **99.48%**
199. **`platform/android/java/editor/src/main/java/org/godotengine/editor/embed/EmbeddedGodotGame.kt`** -> AI Confidence: **99.48%**
200. **`platform/android/java/editor/src/main/java/org/godotengine/editor/embed/GameMenuFragment.kt`** -> AI Confidence: **99.48%**
201. **`platform/android/java/editor/src/main/java/org/godotengine/editor/utils/ApkSignerUtil.kt`** -> AI Confidence: **99.48%**
202. **`platform/android/java/lib/src/main/java/org/godotengine/godot/GodotActivity.kt`** -> AI Confidence: **99.48%**
203. **`platform/android/java/lib/src/main/java/org/godotengine/godot/input/GodotGestureHandler.kt`** -> AI Confidence: **99.48%**
204. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/FilePicker.kt`** -> AI Confidence: **99.48%**
205. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/StorageScope.kt`** -> AI Confidence: **99.48%**
206. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/directory/AssetsDirectoryAccess.kt`** -> AI Confidence: **99.48%**
207. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/directory/DirectoryAccessHandler.kt`** -> AI Confidence: **99.48%**
208. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/directory/FilesystemDirectoryAccess.kt`** -> AI Confidence: **99.48%**
209. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/AssetData.kt`** -> AI Confidence: **99.48%**
210. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/DataAccess.kt`** -> AI Confidence: **99.48%**
211. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/FileAccessHandler.kt`** -> AI Confidence: **99.48%**
212. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/FileData.kt`** -> AI Confidence: **99.48%**
213. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/MediaStoreData.kt`** -> AI Confidence: **99.48%**
214. **`platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/SAFData.kt`** -> AI Confidence: **99.48%**
215. **`platform/android/java/lib/src/main/java/org/godotengine/godot/service/GodotService.kt`** -> AI Confidence: **99.48%**
216. **`platform/android/java/lib/src/main/java/org/godotengine/godot/service/RemoteGodotFragment.kt`** -> AI Confidence: **99.48%**
217. **`platform/android/java/lib/src/main/java/org/godotengine/godot/utils/BenchmarkUtils.kt`** -> AI Confidence: **99.48%**
218. **`platform/android/java/lib/src/main/java/org/godotengine/godot/utils/DialogUtils.kt`** -> AI Confidence: **99.48%**
219. **`thirdparty/freetype/src/autofit/afglobal.c`** -> AI Confidence: **99.48%**
220. **`thirdparty/freetype/src/bdf/bdfdrivr.c`** -> AI Confidence: **99.48%**
221. **`thirdparty/freetype/src/bzip2/ftbzip2.c`** -> AI Confidence: **99.48%**
222. **`thirdparty/freetype/src/cff/cffgload.c`** -> AI Confidence: **99.48%**
223. **`thirdparty/freetype/src/cff/cffload.c`** -> AI Confidence: **99.48%**
224. **`thirdparty/freetype/src/cff/cffobjs.c`** -> AI Confidence: **99.48%**
225. **`thirdparty/freetype/src/cff/cffparse.c`** -> AI Confidence: **99.48%**
226. **`thirdparty/freetype/src/cid/cidgload.c`** -> AI Confidence: **99.48%**
227. **`thirdparty/freetype/src/cid/cidobjs.c`** -> AI Confidence: **99.48%**
228. **`thirdparty/freetype/src/pcf/pcfdrivr.c`** -> AI Confidence: **99.48%**
229. **`thirdparty/freetype/src/pfr/pfrobjs.c`** -> AI Confidence: **99.48%**
230. **`thirdparty/freetype/src/psaux/cffdecode.c`** -> AI Confidence: **99.48%**
231. **`thirdparty/freetype/src/psaux/psauxmod.c`** -> AI Confidence: **99.48%**
232. **`thirdparty/freetype/src/psaux/psobjs.c`** -> AI Confidence: **99.48%**
233. **`thirdparty/freetype/src/psaux/t1decode.c`** -> AI Confidence: **99.48%**
234. **`thirdparty/freetype/src/raster/ftraster.c`** -> AI Confidence: **99.48%**
235. **`thirdparty/freetype/src/sdf/ftbsdf.c`** -> AI Confidence: **99.48%**
236. **`thirdparty/freetype/src/sdf/ftsdf.c`** -> AI Confidence: **99.48%**
237. **`thirdparty/freetype/src/sdf/ftsdfrend.c`** -> AI Confidence: **99.48%**
238. **`thirdparty/freetype/src/sfnt/sfobjs.c`** -> AI Confidence: **99.48%**
239. **`thirdparty/freetype/src/sfnt/sfwoff2.c`** -> AI Confidence: **99.48%**
240. **`thirdparty/freetype/src/sfnt/ttsbit.c`** -> AI Confidence: **99.48%**
241. **`thirdparty/freetype/src/smooth/ftgrays.c`** -> AI Confidence: **99.48%**
242. **`thirdparty/freetype/src/truetype/ttgload.c`** -> AI Confidence: **99.48%**
243. **`thirdparty/freetype/src/truetype/ttgxvar.c`** -> AI Confidence: **99.48%**
244. **`thirdparty/freetype/src/truetype/ttpload.c`** -> AI Confidence: **99.48%**
245. **`thirdparty/freetype/src/type1/t1driver.c`** -> AI Confidence: **99.48%**
246. **`thirdparty/freetype/src/type1/t1gload.c`** -> AI Confidence: **99.48%**
247. **`thirdparty/freetype/src/type1/t1load.c`** -> AI Confidence: **99.48%**
248. **`thirdparty/freetype/src/winfonts/winfnt.c`** -> AI Confidence: **99.48%**
249. **`thirdparty/libjpeg-turbo/src/jcphuff.c`** -> AI Confidence: **99.48%**
250. **`thirdparty/libjpeg-turbo/src/jdapistd.c`** -> AI Confidence: **99.48%**
251. **`thirdparty/libjpeg-turbo/src/turbojpeg.c`** -> AI Confidence: **99.48%**
252. **`thirdparty/libwebp/src/dec/frame_dec.c`** -> AI Confidence: **99.48%**
253. **`thirdparty/libwebp/src/enc/picture_tools_enc.c`** -> AI Confidence: **99.48%**
254. **`thirdparty/libwebp/src/enc/quant_enc.c`** -> AI Confidence: **99.48%**
255. **`thirdparty/libwebp/src/enc/vp8l_enc.c`** -> AI Confidence: **99.48%**
256. **`thirdparty/libwebp/src/mux/muxread.c`** -> AI Confidence: **99.48%**
257. **`thirdparty/libwebp/src/utils/huffman_encode_utils.c`** -> AI Confidence: **99.48%**
258. **`thirdparty/libwebp/src/utils/rescaler_utils.c`** -> AI Confidence: **99.48%**
259. **`thirdparty/miniupnpc/src/minissdpc.c`** -> AI Confidence: **99.48%**
260. **`thirdparty/miniupnpc/src/miniwget.c`** -> AI Confidence: **99.48%**
261. **`thirdparty/pcre2/src/pcre2_jit_compile.c`** -> AI Confidence: **99.48%**
262. **`thirdparty/directx_headers/include/directx/d3dx12.h`** -> AI Confidence: **99.44%**
263. **`thirdparty/openxr/src/common/xr_dependencies.h`** -> AI Confidence: **99.44%**
264. **`thirdparty/amd-fsr2/shaders/ffx_core.h`** -> AI Confidence: **99.43%**
265. **`thirdparty/zstd/common/compiler.h`** -> AI Confidence: **99.43%**
266. **`thirdparty/zstd/common/zstd_deps.h`** -> AI Confidence: **99.43%**
267. **`drivers/apple_embedded/display_server_apple_embedded.h`** -> AI Confidence: **99.43%**
268. **`drivers/apple_embedded/os_apple_embedded.h`** -> AI Confidence: **99.43%**
269. **`platform/macos/os_macos.h`** -> AI Confidence: **99.43%**
270. **`thirdparty/mbedtls/library/common.h`** -> AI Confidence: **99.43%**
271. **`core/typedefs.h`** -> AI Confidence: **99.42%**
272. **`thirdparty/harfbuzz/src/hb.hh`** -> AI Confidence: **99.42%**
273. **`thirdparty/mbedtls/include/mbedtls/platform.h`** -> AI Confidence: **99.42%**
274. **`thirdparty/sdl/SDL_internal.h`** -> AI Confidence: **99.42%**
275. **`thirdparty/sdl/include/build_config/SDL_build_config.h`** -> AI Confidence: **99.42%**
276. **`thirdparty/volk/volk.h`** -> AI Confidence: **99.42%**
277. **`thirdparty/zlib/zconf.h`** -> AI Confidence: **99.42%**
278. **`platform/android/java/lib/src/main/java/org/godotengine/godot/Godot.kt`** -> AI Confidence: **99.42%**
279. **`doc/tools/make_rst.py`** -> AI Confidence: **99.39%**
280. **`misc/scripts/validate_codeowners.py`** -> AI Confidence: **99.39%**
281. **`platform/windows/detect.py`** -> AI Confidence: **99.39%**
282. **`core/config/project_settings.cpp`** -> AI Confidence: **99.39%**
283. **`core/debugger/remote_debugger.cpp`** -> AI Confidence: **99.39%**
284. **`core/error/error_macros.cpp`** -> AI Confidence: **99.39%**
285. **`core/extension/gdextension_library_loader.cpp`** -> AI Confidence: **99.39%**
286. **`core/input/input_map.cpp`** -> AI Confidence: **99.39%**
287. **`core/io/pck_packer.cpp`** -> AI Confidence: **99.39%**
288. **`core/io/resource.cpp`** -> AI Confidence: **99.39%**
289. **`core/object/object.cpp`** -> AI Confidence: **99.39%**
290. **`core/string/translation_server.cpp`** -> AI Confidence: **99.39%**
291. **`core/string/ustring.cpp`** -> AI Confidence: **99.39%**
292. **`core/variant/variant.cpp`** -> AI Confidence: **99.39%**
293. **`drivers/gles3/rasterizer_scene_gles3.cpp`** -> AI Confidence: **99.39%**
294. **`drivers/gles3/storage/material_storage.cpp`** -> AI Confidence: **99.39%**
295. **`drivers/gles3/storage/texture_storage.cpp`** -> AI Confidence: **99.39%**
296. **`drivers/pulseaudio/audio_driver_pulseaudio.cpp`** -> AI Confidence: **99.39%**
297. **`drivers/windows/file_access_windows.cpp`** -> AI Confidence: **99.39%**
298. **`editor/debugger/debug_adapter/debug_adapter_protocol.cpp`** -> AI Confidence: **99.39%**
299. **`editor/debugger/editor_debugger_node.cpp`** -> AI Confidence: **99.39%**
300. **`editor/debugger/editor_profiler.cpp`** -> AI Confidence: **99.39%**
301. **`editor/debugger/editor_visual_profiler.cpp`** -> AI Confidence: **99.39%**
302. **`editor/doc/editor_help.cpp`** -> AI Confidence: **99.39%**
303. **`editor/docks/editor_dock_manager.cpp`** -> AI Confidence: **99.39%**
304. **`editor/docks/import_dock.cpp`** -> AI Confidence: **99.39%**
305. **`editor/editor_log.cpp`** -> AI Confidence: **99.39%**
306. **`editor/export/editor_export_platform.cpp`** -> AI Confidence: **99.39%**
307. **`editor/export/project_zip_packer.cpp`** -> AI Confidence: **99.39%**
308. **`editor/file_system/dependency_editor.cpp`** -> AI Confidence: **99.39%**
309. **`editor/file_system/editor_file_system.cpp`** -> AI Confidence: **99.39%**
310. **`editor/gui/code_editor.cpp`** -> AI Confidence: **99.39%**
311. **`editor/gui/create_dialog.cpp`** -> AI Confidence: **99.39%**
312. **`editor/gui/editor_dir_dialog.cpp`** -> AI Confidence: **99.39%**
313. **`editor/gui/editor_file_dialog.cpp`** -> AI Confidence: **99.39%**
314. **`editor/gui/editor_object_selector.cpp`** -> AI Confidence: **99.39%**
315. **`editor/gui/editor_quick_open_dialog.cpp`** -> AI Confidence: **99.39%**
316. **`editor/gui/editor_spin_slider.cpp`** -> AI Confidence: **99.39%**
317. **`editor/gui/editor_validation_panel.cpp`** -> AI Confidence: **99.39%**
318. **`editor/gui/touch_actions_panel.cpp`** -> AI Confidence: **99.39%**
319. **`editor/import/audio_stream_import_settings.cpp`** -> AI Confidence: **99.39%**
320. **`editor/import/resource_importer_dynamic_font.cpp`** -> AI Confidence: **99.39%**
321. **`editor/inspector/multi_node_edit.cpp`** -> AI Confidence: **99.39%**
322. **`editor/plugins/editor_plugin.cpp`** -> AI Confidence: **99.39%**
323. **`editor/project_manager/project_list.cpp`** -> AI Confidence: **99.39%**
324. **`editor/project_manager/project_manager.cpp`** -> AI Confidence: **99.39%**
325. **`editor/project_manager/quick_settings_dialog.cpp`** -> AI Confidence: **99.39%**
326. **`editor/scene/2d/abstract_polygon_2d_editor.cpp`** -> AI Confidence: **99.39%**
327. **`editor/scene/2d/parallax_background_editor_plugin.cpp`** -> AI Confidence: **99.39%**
328. **`editor/scene/2d/particles_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
329. **`editor/scene/2d/sprite_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
330. **`editor/scene/2d/tiles/atlas_merging_dialog.cpp`** -> AI Confidence: **99.39%**
331. **`editor/scene/2d/tiles/tile_map_layer_editor.cpp`** -> AI Confidence: **99.39%**
332. **`editor/scene/3d/gizmos/camera_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.39%**
333. **`editor/scene/3d/gizmos/light_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.39%**
334. **`editor/scene/3d/occluder_instance_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
335. **`editor/scene/3d/particles_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
336. **`editor/scene/3d/path_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
337. **`editor/scene/3d/polygon_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
338. **`editor/scene/3d/skeleton_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
339. **`editor/scene/curve_editor_plugin.cpp`** -> AI Confidence: **99.39%**
340. **`editor/scene/gui/control_editor_plugin.cpp`** -> AI Confidence: **99.39%**
341. **`editor/scene/particle_process_material_editor_plugin.cpp`** -> AI Confidence: **99.39%**
342. **`editor/scene/rename_dialog.cpp`** -> AI Confidence: **99.39%**
343. **`editor/scene/sprite_frames_editor_plugin.cpp`** -> AI Confidence: **99.39%**
344. **`editor/scene/texture/gradient_texture_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
345. **`editor/settings/action_map_editor.cpp`** -> AI Confidence: **99.39%**
346. **`editor/settings/editor_autoload_settings.cpp`** -> AI Confidence: **99.39%**
347. **`editor/settings/editor_settings.cpp`** -> AI Confidence: **99.39%**
348. **`editor/settings/event_listener_line_edit.cpp`** -> AI Confidence: **99.39%**
349. **`editor/shader/shader_editor_plugin.cpp`** -> AI Confidence: **99.39%**
350. **`editor/shader/shader_file_editor_plugin.cpp`** -> AI Confidence: **99.39%**
351. **`editor/themes/editor_fonts.cpp`** -> AI Confidence: **99.39%**
352. **`editor/translations/editor_translation.cpp`** -> AI Confidence: **99.39%**
353. **`modules/csg/editor/csg_gizmos.cpp`** -> AI Confidence: **99.39%**
354. **`modules/fbx/fbx_document.cpp`** -> AI Confidence: **99.39%**
355. **`modules/gdscript/gdscript.cpp`** -> AI Confidence: **99.39%**
356. **`modules/gdscript/language_server/gdscript_workspace.cpp`** -> AI Confidence: **99.39%**
357. **`modules/gdscript/tests/gdscript_test_runner.cpp`** -> AI Confidence: **99.39%**
358. **`modules/gltf/editor/editor_import_blend_runner.cpp`** -> AI Confidence: **99.39%**
359. **`modules/gltf/editor/editor_scene_importer_blend.cpp`** -> AI Confidence: **99.39%**
360. **`modules/gltf/extensions/physics/gltf_physics_shape.cpp`** -> AI Confidence: **99.39%**
361. **`modules/gltf/gltf_document.cpp`** -> AI Confidence: **99.39%**
362. **`modules/gridmap/grid_map.cpp`** -> AI Confidence: **99.39%**
363. **`modules/jolt_physics/spaces/jolt_contact_listener_3d.cpp`** -> AI Confidence: **99.39%**
364. **`modules/multiplayer/scene_cache_interface.cpp`** -> AI Confidence: **99.39%**
365. **`modules/multiplayer/scene_replication_interface.cpp`** -> AI Confidence: **99.39%**
366. **`modules/navigation_2d/2d/nav_mesh_generator_2d.cpp`** -> AI Confidence: **99.39%**
367. **`modules/navigation_3d/3d/nav_mesh_generator_3d.cpp`** -> AI Confidence: **99.39%**
368. **`modules/navigation_3d/editor/navigation_obstacle_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
369. **`modules/objectdb_profiler/editor/data_viewers/class_view.cpp`** -> AI Confidence: **99.39%**
370. **`modules/objectdb_profiler/editor/data_viewers/node_view.cpp`** -> AI Confidence: **99.39%**
371. **`modules/objectdb_profiler/editor/data_viewers/refcounted_view.cpp`** -> AI Confidence: **99.39%**
372. **`modules/objectdb_profiler/editor/data_viewers/summary_view.cpp`** -> AI Confidence: **99.39%**
373. **`modules/openxr/scene/openxr_composition_layer.cpp`** -> AI Confidence: **99.39%**
374. **`platform/linuxbsd/freedesktop_portal_desktop.cpp`** -> AI Confidence: **99.39%**
375. **`platform/linuxbsd/godot_linuxbsd.cpp`** -> AI Confidence: **99.39%**
376. **`platform/linuxbsd/os_linuxbsd.cpp`** -> AI Confidence: **99.39%**
377. **`platform/linuxbsd/wayland/wayland_embedder.cpp`** -> AI Confidence: **99.39%**
378. **`platform/linuxbsd/x11/detect_prime_x11.cpp`** -> AI Confidence: **99.39%**
379. **`platform/windows/export/export_plugin.cpp`** -> AI Confidence: **99.39%**
380. **`platform/windows/windows_utils.cpp`** -> AI Confidence: **99.39%**
381. **`scene/3d/cpu_particles_3d.cpp`** -> AI Confidence: **99.39%**
382. **`scene/3d/physics/collision_object_3d.cpp`** -> AI Confidence: **99.39%**
383. **`scene/3d/physics/collision_shape_3d.cpp`** -> AI Confidence: **99.39%**
384. **`scene/3d/physics/static_body_3d.cpp`** -> AI Confidence: **99.39%**
385. **`scene/3d/skeleton_3d.cpp`** -> AI Confidence: **99.39%**
386. **`scene/animation/animation_player.cpp`** -> AI Confidence: **99.39%**
387. **`scene/debugger/scene_debugger.cpp`** -> AI Confidence: **99.39%**
388. **`scene/gui/color_picker.cpp`** -> AI Confidence: **99.39%**
389. **`scene/gui/control.cpp`** -> AI Confidence: **99.39%**
390. **`scene/gui/file_dialog.cpp`** -> AI Confidence: **99.39%**
391. **`scene/gui/graph_frame.cpp`** -> AI Confidence: **99.39%**
392. **`scene/gui/item_list.cpp`** -> AI Confidence: **99.39%**
393. **`scene/main/node.cpp`** -> AI Confidence: **99.39%**
394. **`scene/main/scene_tree.cpp`** -> AI Confidence: **99.39%**
395. **`scene/main/window.cpp`** -> AI Confidence: **99.39%**
396. **`scene/resources/material.cpp`** -> AI Confidence: **99.39%**
397. **`scene/resources/mesh.cpp`** -> AI Confidence: **99.39%**
398. **`scene/resources/resource_format_text.cpp`** -> AI Confidence: **99.39%**
399. **`scene/resources/shader.cpp`** -> AI Confidence: **99.39%**
400. **`servers/rendering/renderer_rd/renderer_canvas_render_rd.cpp`** -> AI Confidence: **99.39%**
401. **`servers/rendering/renderer_rd/renderer_compositor_rd.cpp`** -> AI Confidence: **99.39%**
402. **`servers/rendering/renderer_rd/renderer_scene_render_rd.cpp`** -> AI Confidence: **99.39%**
403. **`servers/rendering/renderer_rd/shader_rd.cpp`** -> AI Confidence: **99.39%**
404. **`servers/rendering/rendering_device.cpp`** -> AI Confidence: **99.39%**
405. **`tests/scene/test_audio_stream_wav.cpp`** -> AI Confidence: **99.39%**
406. **`thirdparty/brotli/common/platform.h`** -> AI Confidence: **99.39%**
407. **`thirdparty/graphite/src/Code.cpp`** -> AI Confidence: **99.39%**
408. **`thirdparty/graphite/src/Pass.cpp`** -> AI Confidence: **99.39%**
409. **`thirdparty/graphite/src/Silf.cpp`** -> AI Confidence: **99.39%**
410. **`thirdparty/harfbuzz/src/hb-ot-metrics.cc`** -> AI Confidence: **99.39%**
411. **`thirdparty/harfbuzz/src/hb-ot-shape.cc`** -> AI Confidence: **99.39%**
412. **`thirdparty/harfbuzz/src/hb-raster-svg-clip.cc`** -> AI Confidence: **99.39%**
413. **`thirdparty/harfbuzz/src/hb-raster-svg-color.cc`** -> AI Confidence: **99.39%**
414. **`thirdparty/jolt_physics/Jolt/Core/Core.h`** -> AI Confidence: **99.39%**
415. **`thirdparty/mbedtls/include/mbedtls/oid.h`** -> AI Confidence: **99.39%**
416. **`thirdparty/minizip/skipset.h`** -> AI Confidence: **99.39%**
417. **`thirdparty/openxr/src/external/jsoncpp/src/lib_json/json_reader.cpp`** -> AI Confidence: **99.39%**
418. **`thirdparty/openxr/src/external/jsoncpp/src/lib_json/json_writer.cpp`** -> AI Confidence: **99.39%**
419. **`thirdparty/openxr/src/loader/api_layer_interface.cpp`** -> AI Confidence: **99.39%**
420. **`thirdparty/openxr/src/loader/manifest_file.cpp`** -> AI Confidence: **99.39%**
421. **`thirdparty/thorvg/src/loaders/svg/tvgXmlParser.cpp`** -> AI Confidence: **99.39%**
422. **`drivers/apple_embedded/godot_view_renderer.mm`** -> AI Confidence: **99.39%**
423. **`platform/web/eslint.config.cjs`** -> AI Confidence: **99.39%**
424. **`thirdparty/freetype/src/base/ftglyph.c`** -> AI Confidence: **99.39%**
425. **`thirdparty/freetype/src/base/ftobjs.c`** -> AI Confidence: **99.39%**
426. **`thirdparty/freetype/src/cid/cidload.c`** -> AI Confidence: **99.39%**
427. **`thirdparty/freetype/src/gxvalid/gxvmod.c`** -> AI Confidence: **99.39%**
428. **`thirdparty/freetype/src/gzip/ftgzip.c`** -> AI Confidence: **99.39%**
429. **`thirdparty/freetype/src/pfr/pfrdrivr.c`** -> AI Confidence: **99.39%**
430. **`thirdparty/freetype/src/psaux/psintrp.c`** -> AI Confidence: **99.39%**
431. **`thirdparty/freetype/src/sfnt/sfdriver.c`** -> AI Confidence: **99.39%**
432. **`thirdparty/freetype/src/sfnt/ttcmap.c`** -> AI Confidence: **99.39%**
433. **`thirdparty/freetype/src/sfnt/ttcolr.c`** -> AI Confidence: **99.39%**
434. **`thirdparty/freetype/src/sfnt/ttsvg.c`** -> AI Confidence: **99.39%**
435. **`thirdparty/freetype/src/type1/t1objs.c`** -> AI Confidence: **99.39%**
436. **`thirdparty/libpng/pngpriv.h`** -> AI Confidence: **99.39%**
437. **`thirdparty/libwebp/src/dec/alpha_dec.c`** -> AI Confidence: **99.39%**
438. **`thirdparty/libwebp/src/dec/io_dec.c`** -> AI Confidence: **99.39%**
439. **`thirdparty/libwebp/src/dsp/lossless_avx2.c`** -> AI Confidence: **99.39%**
440. **`thirdparty/libwebp/src/dsp/lossless_enc_avx2.c`** -> AI Confidence: **99.39%**
441. **`thirdparty/libwebp/src/dsp/lossless_enc_sse2.c`** -> AI Confidence: **99.39%**
442. **`thirdparty/libwebp/src/dsp/rescaler_sse2.c`** -> AI Confidence: **99.39%**
443. **`thirdparty/libwebp/src/enc/analysis_enc.c`** -> AI Confidence: **99.39%**
444. **`thirdparty/libwebp/src/enc/backward_references_cost_enc.c`** -> AI Confidence: **99.39%**
445. **`thirdparty/libwebp/src/enc/backward_references_enc.c`** -> AI Confidence: **99.39%**
446. **`thirdparty/libwebp/src/enc/filter_enc.c`** -> AI Confidence: **99.39%**
447. **`thirdparty/libwebp/src/enc/frame_enc.c`** -> AI Confidence: **99.39%**
448. **`thirdparty/libwebp/src/enc/histogram_enc.c`** -> AI Confidence: **99.39%**
449. **`thirdparty/libwebp/src/enc/picture_psnr_enc.c`** -> AI Confidence: **99.39%**
450. **`thirdparty/libwebp/src/enc/predictor_enc.c`** -> AI Confidence: **99.39%**
451. **`thirdparty/libwebp/src/enc/webp_enc.c`** -> AI Confidence: **99.39%**
452. **`thirdparty/miniupnpc/src/connecthostport.c`** -> AI Confidence: **99.39%**
453. **`thirdparty/miniupnpc/src/receivedata.c`** -> AI Confidence: **99.39%**
454. **`core/extension/gdextension_manager.cpp`** -> AI Confidence: **99.35%**
455. **`editor/export/export_template_manager.cpp`** -> AI Confidence: **99.35%**
456. **`editor/import/resource_importer_texture_atlas.cpp`** -> AI Confidence: **99.35%**
457. **`editor/inspector/editor_preview_plugins.cpp`** -> AI Confidence: **99.35%**
458. **`editor/run/run_instances_dialog.cpp`** -> AI Confidence: **99.35%**
459. **`editor/scene/2d/tiles/tile_atlas_view.cpp`** -> AI Confidence: **99.35%**
460. **`editor/settings/editor_command_palette.cpp`** -> AI Confidence: **99.35%**
461. **`editor/shader/shader_create_dialog.cpp`** -> AI Confidence: **99.35%**
462. **`editor/shader/shader_globals_editor.cpp`** -> AI Confidence: **99.35%**
463. **`platform/windows/os_windows.cpp`** -> AI Confidence: **99.35%**
464. **`thirdparty/thorvg/src/loaders/svg/tvgSvgSceneBuilder.cpp`** -> AI Confidence: **99.35%**
465. **`thirdparty/freetype/src/truetype/ttdriver.c`** -> AI Confidence: **99.35%**
466. **`thirdparty/libwebp/src/mux/anim_encode.c`** -> AI Confidence: **99.35%**
467. **`drivers/d3d12/SCsub`** -> AI Confidence: **99.34%**
468. **`platform/windows/SCsub`** -> AI Confidence: **99.34%**
469. **`core/debugger/local_debugger.cpp`** -> AI Confidence: **99.34%**
470. **`core/io/dir_access.cpp`** -> AI Confidence: **99.34%**
471. **`core/io/http_client_tcp.cpp`** -> AI Confidence: **99.34%**
472. **`core/math/geometry_2d.cpp`** -> AI Confidence: **99.34%**
473. **`drivers/apple/os_log_logger.cpp`** -> AI Confidence: **99.34%**
474. **`drivers/gles3/shader_gles3.cpp`** -> AI Confidence: **99.34%**
475. **`drivers/gles3/storage/config.cpp`** -> AI Confidence: **99.34%**
476. **`drivers/gles3/storage/mesh_storage.cpp`** -> AI Confidence: **99.34%**
477. **`drivers/metal/metal3_objects.cpp`** -> AI Confidence: **99.34%**
478. **`editor/audio/audio_stream_randomizer_editor_plugin.cpp`** -> AI Confidence: **99.34%**
479. **`editor/gui/editor_title_bar.cpp`** -> AI Confidence: **99.34%**
480. **`editor/import/3d/post_import_plugin_skeleton_track_organizer.cpp`** -> AI Confidence: **99.34%**
481. **`editor/import/editor_atlas_packer.cpp`** -> AI Confidence: **99.34%**
482. **`editor/import/resource_importer_csv_translation.cpp`** -> AI Confidence: **99.34%**
483. **`editor/import/resource_importer_imagefont.cpp`** -> AI Confidence: **99.34%**
484. **`editor/inspector/input_event_editor_plugin.cpp`** -> AI Confidence: **99.34%**
485. **`editor/settings/editor_layouts_dialog.cpp`** -> AI Confidence: **99.34%**
486. **`editor/translations/packed_scene_translation_parser_plugin.cpp`** -> AI Confidence: **99.34%**
487. **`modules/basis_universal/image_compress_basisu.cpp`** -> AI Confidence: **99.34%**
488. **`modules/cvtt/image_compress_cvtt.cpp`** -> AI Confidence: **99.34%**
489. **`modules/dds/tests/test_dds.h`** -> AI Confidence: **99.34%**
490. **`modules/etcpak/image_compress_etcpak.cpp`** -> AI Confidence: **99.34%**
491. **`modules/gdscript/gdscript_resource_format.cpp`** -> AI Confidence: **99.34%**
492. **`modules/gdscript/gdscript_tokenizer.cpp`** -> AI Confidence: **99.34%**
493. **`modules/gdscript/gdscript_vm.cpp`** -> AI Confidence: **99.34%**
494. **`modules/gdscript/language_server/gdscript_extend_parser.cpp`** -> AI Confidence: **99.34%**
495. **`modules/godot_physics_2d/godot_body_2d.cpp`** -> AI Confidence: **99.34%**
496. **`modules/godot_physics_3d/godot_body_3d.cpp`** -> AI Confidence: **99.34%**
497. **`modules/multiplayer/scene_multiplayer.cpp`** -> AI Confidence: **99.34%**
498. **`modules/navigation_2d/2d/nav_map_builder_2d.cpp`** -> AI Confidence: **99.34%**
499. **`modules/navigation_3d/3d/nav_map_builder_3d.cpp`** -> AI Confidence: **99.34%**
500. **`modules/navigation_3d/3d/nav_mesh_queries_3d.cpp`** -> AI Confidence: **99.34%**
501. **`modules/openxr/editor/openxr_binding_modifiers_dialog.cpp`** -> AI Confidence: **99.34%**
502. **`modules/theora/register_types.cpp`** -> AI Confidence: **99.34%**
503. **`platform/ios/export/export_plugin.cpp`** -> AI Confidence: **99.34%**
504. **`platform/windows/windows_terminal_logger.cpp`** -> AI Confidence: **99.34%**
505. **`scene/2d/skeleton_2d.cpp`** -> AI Confidence: **99.34%**
506. **`scene/3d/bone_attachment_3d.cpp`** -> AI Confidence: **99.34%**
507. **`scene/3d/spring_bone_simulator_3d.cpp`** -> AI Confidence: **99.34%**
508. **`scene/3d/voxelizer.cpp`** -> AI Confidence: **99.34%**
509. **`scene/gui/box_container.cpp`** -> AI Confidence: **99.34%**
510. **`scene/gui/grid_container.cpp`** -> AI Confidence: **99.34%**
511. **`scene/gui/menu_bar.cpp`** -> AI Confidence: **99.34%**
512. **`scene/gui/slider.cpp`** -> AI Confidence: **99.34%**
513. **`servers/rendering/renderer_rd/effects/bokeh_dof.cpp`** -> AI Confidence: **99.34%**
514. **`servers/rendering/renderer_rd/effects/copy_effects.cpp`** -> AI Confidence: **99.34%**
515. **`servers/rendering/renderer_rd/effects/ss_effects.cpp`** -> AI Confidence: **99.34%**
516. **`servers/rendering/renderer_rd/effects/vrs.cpp`** -> AI Confidence: **99.34%**
517. **`servers/rendering/renderer_rd/storage_rd/render_scene_data_rd.cpp`** -> AI Confidence: **99.34%**
518. **`tests/core/io/test_logger.cpp`** -> AI Confidence: **99.34%**
519. **`tests/core/math/test_projection.cpp`** -> AI Confidence: **99.34%**
520. **`tests/scene/test_code_edit.cpp`** -> AI Confidence: **99.34%**
521. **`thirdparty/harfbuzz/src/hb-ot-shaper-arabic.cc`** -> AI Confidence: **99.34%**
522. **`thirdparty/harfbuzz/src/hb-ot-shaper-indic.cc`** -> AI Confidence: **99.34%**
523. **`thirdparty/harfbuzz/src/hb-raster-svg-fill.cc`** -> AI Confidence: **99.34%**
524. **`thirdparty/mbedtls/include/mbedtls/pkcs12.h`** -> AI Confidence: **99.34%**
525. **`thirdparty/mbedtls/include/mbedtls/psa_util.h`** -> AI Confidence: **99.34%**
526. **`thirdparty/mbedtls/include/mbedtls/ssl_ciphersuites.h`** -> AI Confidence: **99.34%**
527. **`thirdparty/sdl/include/SDL3/SDL_assert.h`** -> AI Confidence: **99.34%**
528. **`thirdparty/thorvg/src/loaders/svg/tvgSvgLoader.cpp`** -> AI Confidence: **99.34%**
529. **`thirdparty/tinyexr/tinyexr.h`** -> AI Confidence: **99.34%**
530. **`thirdparty/wslay/wslay_net.h`** -> AI Confidence: **99.34%**
531. **`drivers/coreaudio/audio_driver_coreaudio.mm`** -> AI Confidence: **99.34%**
532. **`modules/openxr/extensions/platform/openxr_metal_extension.mm`** -> AI Confidence: **99.34%**
533. **`platform/macos/dir_access_macos.mm`** -> AI Confidence: **99.34%**
534. **`platform/macos/embedded_gl_manager.mm`** -> AI Confidence: **99.34%**
535. **`platform/macos/gl_manager_macos_legacy.mm`** -> AI Confidence: **99.34%**
536. **`platform/macos/godot_main_macos.mm`** -> AI Confidence: **99.34%**
537. **`platform/macos/godot_menu_delegate.mm`** -> AI Confidence: **99.34%**
538. **`platform/macos/godot_window_delegate.mm`** -> AI Confidence: **99.34%**
539. **`platform/macos/key_mapping_macos.mm`** -> AI Confidence: **99.34%**
540. **`platform/macos/native_menu_macos.mm`** -> AI Confidence: **99.34%**
541. **`modules/mono/glue/GodotSharp/GodotSharp/Core/DebuggingUtils.cs`** -> AI Confidence: **99.34%**
542. **`platform/android/java/lib/src/main/java/org/godotengine/godot/plugin/AndroidRuntimePlugin.kt`** -> AI Confidence: **99.34%**
543. **`thirdparty/freetype/src/autofit/afcjk.c`** -> AI Confidence: **99.34%**
544. **`thirdparty/freetype/src/autofit/aflatin.c`** -> AI Confidence: **99.34%**
545. **`thirdparty/freetype/src/autofit/afloader.c`** -> AI Confidence: **99.34%**
546. **`thirdparty/freetype/src/base/ftstroke.c`** -> AI Confidence: **99.34%**
547. **`thirdparty/freetype/src/bdf/bdflib.c`** -> AI Confidence: **99.34%**
548. **`thirdparty/freetype/src/cid/cidparse.c`** -> AI Confidence: **99.34%**
549. **`thirdparty/freetype/src/pcf/pcfread.c`** -> AI Confidence: **99.34%**
550. **`thirdparty/freetype/src/pfr/pfrgload.c`** -> AI Confidence: **99.34%**
551. **`thirdparty/freetype/src/pfr/pfrsbit.c`** -> AI Confidence: **99.34%**
552. **`thirdparty/freetype/src/psaux/afmparse.c`** -> AI Confidence: **99.34%**
553. **`thirdparty/freetype/src/psaux/psblues.c`** -> AI Confidence: **99.34%**
554. **`thirdparty/freetype/src/psaux/psfont.c`** -> AI Confidence: **99.34%**
555. **`thirdparty/freetype/src/psaux/pshints.c`** -> AI Confidence: **99.34%**
556. **`thirdparty/freetype/src/pshinter/pshalgo.c`** -> AI Confidence: **99.34%**
557. **`thirdparty/freetype/src/pshinter/pshrec.c`** -> AI Confidence: **99.34%**
558. **`thirdparty/freetype/src/raster/ftrend1.c`** -> AI Confidence: **99.34%**
559. **`thirdparty/freetype/src/sfnt/pngshim.c`** -> AI Confidence: **99.34%**
560. **`thirdparty/freetype/src/sfnt/sfwoff.c`** -> AI Confidence: **99.34%**
561. **`thirdparty/freetype/src/sfnt/ttbdf.c`** -> AI Confidence: **99.34%**
562. **`thirdparty/freetype/src/sfnt/ttkern.c`** -> AI Confidence: **99.34%**
563. **`thirdparty/freetype/src/sfnt/ttload.c`** -> AI Confidence: **99.34%**
564. **`thirdparty/freetype/src/sfnt/ttmtx.c`** -> AI Confidence: **99.34%**
565. **`thirdparty/freetype/src/sfnt/ttpost.c`** -> AI Confidence: **99.34%**
566. **`thirdparty/freetype/src/smooth/ftsmooth.c`** -> AI Confidence: **99.34%**
567. **`thirdparty/freetype/src/type1/t1parse.c`** -> AI Confidence: **99.34%**
568. **`thirdparty/freetype/src/type42/t42objs.c`** -> AI Confidence: **99.34%**
569. **`thirdparty/libjpeg-turbo/src/jccolor.c`** -> AI Confidence: **99.34%**
570. **`thirdparty/libjpeg-turbo/src/jchuff.c`** -> AI Confidence: **99.34%**
571. **`thirdparty/libjpeg-turbo/src/jdcolor.c`** -> AI Confidence: **99.34%**
572. **`thirdparty/libjpeg-turbo/src/jddctmgr.c`** -> AI Confidence: **99.34%**
573. **`thirdparty/libjpeg-turbo/src/jdhuff.c`** -> AI Confidence: **99.34%**
574. **`thirdparty/libjpeg-turbo/src/jdmerge.c`** -> AI Confidence: **99.34%**
575. **`thirdparty/libjpeg-turbo/src/jmemmgr.c`** -> AI Confidence: **99.34%**
576. **`thirdparty/libjpeg-turbo/src/transupp.c`** -> AI Confidence: **99.34%**
577. **`thirdparty/libwebp/src/dec/quant_dec.c`** -> AI Confidence: **99.34%**
578. **`thirdparty/libwebp/src/dsp/upsampling_neon.c`** -> AI Confidence: **99.34%**
579. **`thirdparty/libwebp/src/enc/cost_enc.c`** -> AI Confidence: **99.34%**
580. **`thirdparty/libwebp/src/enc/token_enc.c`** -> AI Confidence: **99.34%**
581. **`thirdparty/libwebp/src/utils/bit_writer_utils.c`** -> AI Confidence: **99.34%**
582. **`thirdparty/libwebp/src/utils/filters_utils.c`** -> AI Confidence: **99.34%**
583. **`thirdparty/mbedtls/library/ssl_misc.h`** -> AI Confidence: **99.34%**
584. **`thirdparty/pcre2/deps/sljit/sljit_src/sljitConfigInternal.h`** -> AI Confidence: **99.34%**
585. **`core/doc_data.cpp`** -> AI Confidence: **99.32%**
586. **`core/error/error_list.cpp`** -> AI Confidence: **99.32%**
587. **`core/extension/gdextension_special_compat_hashes.cpp`** -> AI Confidence: **99.32%**
588. **`core/io/plist.cpp`** -> AI Confidence: **99.32%**
589. **`core/io/translation_loader_po.cpp`** -> AI Confidence: **99.32%**
590. **`core/math/delaunay_3d.h`** -> AI Confidence: **99.32%**
591. **`core/math/quick_hull.cpp`** -> AI Confidence: **99.32%**
592. **`core/math/triangle_mesh.cpp`** -> AI Confidence: **99.32%**
593. **`core/object/gdtype.cpp`** -> AI Confidence: **99.32%**
594. **`core/os/keyboard.cpp`** -> AI Confidence: **99.32%**
595. **`drivers/png/png_driver_common.cpp`** -> AI Confidence: **99.32%**
596. **`editor/scene/3d/gizmos/physics/collision_polygon_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.32%**
597. **`modules/camera/buffer_decoder.cpp`** -> AI Confidence: **99.32%**
598. **`modules/gdscript/gdscript_tokenizer_buffer.cpp`** -> AI Confidence: **99.32%**
599. **`modules/godot_physics_2d/godot_body_pair_2d.cpp`** -> AI Confidence: **99.32%**
600. **`modules/mono/utils/naming_utils.cpp`** -> AI Confidence: **99.32%**
601. **`modules/mono/utils/string_utils.cpp`** -> AI Confidence: **99.32%**
602. **`modules/regex/tests/test_regex.h`** -> AI Confidence: **99.32%**
603. **`platform/android/java_class_wrapper.cpp`** -> AI Confidence: **99.32%**
604. **`scene/3d/spline_ik_3d.cpp`** -> AI Confidence: **99.32%**
605. **`scene/gui/check_box.cpp`** -> AI Confidence: **99.32%**
606. **`scene/gui/check_button.cpp`** -> AI Confidence: **99.32%**
607. **`scene/gui/graph_edit_arranger.cpp`** -> AI Confidence: **99.32%**
608. **`scene/resources/2d/polygon_path_finder.cpp`** -> AI Confidence: **99.32%**
609. **`scene/resources/bit_map.cpp`** -> AI Confidence: **99.32%**
610. **`tests/core/input/test_input_event_key.cpp`** -> AI Confidence: **99.32%**
611. **`tests/core/io/test_marshalls.cpp`** -> AI Confidence: **99.32%**
612. **`tests/scene/test_fontfile.cpp`** -> AI Confidence: **99.32%**
613. **`thirdparty/embree/common/tasking/taskscheduler.h`** -> AI Confidence: **99.32%**
614. **`thirdparty/freetype/include/freetype/config/mac-support.h`** -> AI Confidence: **99.32%**
615. **`thirdparty/harfbuzz/src/hb-raster-svg-base.cc`** -> AI Confidence: **99.32%**
616. **`thirdparty/harfbuzz/src/hb-raster-svg-gradient.cc`** -> AI Confidence: **99.32%**
617. **`thirdparty/harfbuzz/src/hb-raster-svg-parse.cc`** -> AI Confidence: **99.32%**
618. **`thirdparty/harfbuzz/src/hb-zlib.cc`** -> AI Confidence: **99.32%**
619. **`thirdparty/icu4c/common/unicode/urename.h`** -> AI Confidence: **99.32%**
620. **`thirdparty/icu4c/common/unicode/utf16.h`** -> AI Confidence: **99.32%**
621. **`thirdparty/icu4c/common/unicode/utf8.h`** -> AI Confidence: **99.32%**
622. **`thirdparty/icu4c/common/unicode/utf_old.h`** -> AI Confidence: **99.32%**
623. **`thirdparty/libktx/lib/uthash.h`** -> AI Confidence: **99.32%**
624. **`thirdparty/linuxbsd_headers/dbus/dbus-syntax.h`** -> AI Confidence: **99.32%**
625. **`thirdparty/manifold/src/smoothing.cpp`** -> AI Confidence: **99.32%**
626. **`thirdparty/openxr/src/external/jsoncpp/include/json/assertions.h`** -> AI Confidence: **99.32%**
627. **`thirdparty/sdl/include/SDL3/SDL_platform_defines.h`** -> AI Confidence: **99.32%**
628. **`drivers/apple_embedded/godot_app_delegate.mm`** -> AI Confidence: **99.32%**
629. **`drivers/apple_embedded/rendering_context_driver_vulkan_apple_embedded.mm`** -> AI Confidence: **99.32%**
630. **`drivers/coremidi/midi_driver_coremidi.mm`** -> AI Confidence: **99.32%**
631. **`platform/macos/rendering_context_driver_vulkan_macos.mm`** -> AI Confidence: **99.32%**
632. **`platform/android/java/app/src/instrumented/java/com/godot/game/test/javaclasswrapper/TestClass.kt`** -> AI Confidence: **99.32%**
633. **`platform/android/java/lib/src/main/java/org/godotengine/godot/utils/CommandLineFileParser.kt`** -> AI Confidence: **99.32%**
634. **`platform/android/java/lib/src/main/java/org/godotengine/godot/vulkan/VkSurfaceView.kt`** -> AI Confidence: **99.32%**
635. **`thirdparty/freetype/src/base/ftcid.c`** -> AI Confidence: **99.32%**
636. **`thirdparty/freetype/src/otvalid/otvgpos.c`** -> AI Confidence: **99.32%**
637. **`thirdparty/freetype/src/otvalid/otvjstf.c`** -> AI Confidence: **99.32%**
638. **`thirdparty/libjpeg-turbo/src/jcapistd.c`** -> AI Confidence: **99.32%**
639. **`thirdparty/libjpeg-turbo/src/jccoefct.c`** -> AI Confidence: **99.32%**
640. **`thirdparty/libjpeg-turbo/src/jcicc.c`** -> AI Confidence: **99.32%**
641. **`thirdparty/libjpeg-turbo/src/jcinit.c`** -> AI Confidence: **99.32%**
642. **`thirdparty/libjpeg-turbo/src/jcmainct.c`** -> AI Confidence: **99.32%**
643. **`thirdparty/libjpeg-turbo/src/jcparam.c`** -> AI Confidence: **99.32%**
644. **`thirdparty/libjpeg-turbo/src/jctrans.c`** -> AI Confidence: **99.32%**
645. **`thirdparty/libjpeg-turbo/src/jdapimin.c`** -> AI Confidence: **99.32%**
646. **`thirdparty/libjpeg-turbo/src/jdicc.c`** -> AI Confidence: **99.32%**
647. **`thirdparty/libjpeg-turbo/src/jdpostct.c`** -> AI Confidence: **99.32%**
648. **`thirdparty/libjpeg-turbo/src/jdtrans.c`** -> AI Confidence: **99.32%**
649. **`thirdparty/libjpeg-turbo/src/jfdctfst.c`** -> AI Confidence: **99.32%**
650. **`thirdparty/libjpeg-turbo/src/jfdctint.c`** -> AI Confidence: **99.32%**
651. **`thirdparty/libjpeg-turbo/src/jidctflt.c`** -> AI Confidence: **99.32%**
652. **`thirdparty/libjpeg-turbo/src/jidctfst.c`** -> AI Confidence: **99.32%**
653. **`thirdparty/libjpeg-turbo/src/jidctint.c`** -> AI Confidence: **99.32%**
654. **`thirdparty/libjpeg-turbo/src/jidctred.c`** -> AI Confidence: **99.32%**
655. **`thirdparty/libjpeg-turbo/src/jquant2.c`** -> AI Confidence: **99.32%**
656. **`thirdparty/libwebp/src/dsp/dec_clip_tables.c`** -> AI Confidence: **99.32%**
657. **`thirdparty/libwebp/src/dsp/lossless_msa.c`** -> AI Confidence: **99.32%**
658. **`thirdparty/libwebp/src/dsp/msa_macro.h`** -> AI Confidence: **99.32%**
659. **`thirdparty/libwebp/src/dsp/neon.h`** -> AI Confidence: **99.32%**
660. **`thirdparty/libwebp/src/dsp/rescaler_mips_dsp_r2.c`** -> AI Confidence: **99.32%**
661. **`thirdparty/mbedtls/library/aesce.h`** -> AI Confidence: **99.32%**
662. **`thirdparty/mbedtls/library/padlock.h`** -> AI Confidence: **99.32%**
663. **`thirdparty/mbedtls/library/pkwrite.h`** -> AI Confidence: **99.32%**
664. **`thirdparty/mbedtls/library/ssl_client.h`** -> AI Confidence: **99.32%**
665. **`thirdparty/pcre2/src/pcre2_internal.h`** -> AI Confidence: **99.32%**
666. **`doc/tools/doc_status.py`** -> AI Confidence: **99.31%**
667. **`misc/scripts/install_d3d12_sdk_windows.py`** -> AI Confidence: **99.31%**
668. **`modules/raycast/godot_update_embree.py`** -> AI Confidence: **99.31%**
669. **`platform/android/detect.py`** -> AI Confidence: **99.31%**
670. **`platform/ios/detect.py`** -> AI Confidence: **99.31%**
671. **`platform/macos/detect.py`** -> AI Confidence: **99.31%**
672. **`platform/visionos/detect.py`** -> AI Confidence: **99.31%**
673. **`platform/web/detect.py`** -> AI Confidence: **99.31%**
674. **`core/crypto/crypto_core.cpp`** -> AI Confidence: **99.31%**
675. **`core/debugger/remote_debugger_peer.cpp`** -> AI Confidence: **99.31%**
676. **`core/extension/gdextension.cpp`** -> AI Confidence: **99.31%**
677. **`core/extension/godot_instance.cpp`** -> AI Confidence: **99.31%**
678. **`core/input/input.cpp`** -> AI Confidence: **99.31%**
679. **`core/input/input_event.cpp`** -> AI Confidence: **99.31%**
680. **`core/io/file_access.cpp`** -> AI Confidence: **99.31%**
681. **`core/io/resource_importer.cpp`** -> AI Confidence: **99.31%**
682. **`core/io/resource_loader.cpp`** -> AI Confidence: **99.31%**
683. **`core/io/resource_uid.cpp`** -> AI Confidence: **99.31%**
684. **`core/math/convex_hull.cpp`** -> AI Confidence: **99.31%**
685. **`core/math/projection.cpp`** -> AI Confidence: **99.31%**
686. **`core/object/worker_thread_pool.cpp`** -> AI Confidence: **99.31%**
687. **`core/register_core_types.cpp`** -> AI Confidence: **99.31%**
688. **`core/variant/array.cpp`** -> AI Confidence: **99.31%**
689. **`core/variant/callable.cpp`** -> AI Confidence: **99.31%**
690. **`drivers/alsa/audio_driver_alsa.cpp`** -> AI Confidence: **99.31%**
691. **`drivers/d3d12/rendering_shader_container_d3d12.cpp`** -> AI Confidence: **99.31%**
692. **`drivers/egl/egl_manager.cpp`** -> AI Confidence: **99.31%**
693. **`drivers/gles3/storage/light_storage.cpp`** -> AI Confidence: **99.31%**
694. **`drivers/gles3/storage/particles_storage.cpp`** -> AI Confidence: **99.31%**
695. **`drivers/gles3/storage/utilities.cpp`** -> AI Confidence: **99.31%**
696. **`drivers/metal/metal_objects_shared.cpp`** -> AI Confidence: **99.31%**
697. **`drivers/metal/rendering_device_driver_metal.cpp`** -> AI Confidence: **99.31%**
698. **`drivers/unix/dir_access_unix.cpp`** -> AI Confidence: **99.31%**
699. **`drivers/unix/file_access_unix.cpp`** -> AI Confidence: **99.31%**
700. **`drivers/unix/file_access_unix_pipe.cpp`** -> AI Confidence: **99.31%**
701. **`drivers/unix/ip_unix.cpp`** -> AI Confidence: **99.31%**
702. **`drivers/unix/net_socket_unix.cpp`** -> AI Confidence: **99.31%**
703. **`drivers/unix/os_unix.cpp`** -> AI Confidence: **99.31%**
704. **`drivers/windows/dir_access_windows.cpp`** -> AI Confidence: **99.31%**
705. **`editor/animation/animation_track_editor_plugins.cpp`** -> AI Confidence: **99.31%**
706. **`editor/animation/animation_tree_editor_plugin.cpp`** -> AI Confidence: **99.31%**
707. **`editor/audio/audio_stream_editor_plugin.cpp`** -> AI Confidence: **99.31%**
708. **`editor/debugger/debug_adapter/debug_adapter_parser.cpp`** -> AI Confidence: **99.31%**
709. **`editor/debugger/editor_debugger_inspector.cpp`** -> AI Confidence: **99.31%**
710. **`editor/debugger/editor_expression_evaluator.cpp`** -> AI Confidence: **99.31%**
711. **`editor/debugger/editor_performance_profiler.cpp`** -> AI Confidence: **99.31%**
712. **`editor/debugger/script_editor_debugger.cpp`** -> AI Confidence: **99.31%**
713. **`editor/docks/dock_tab_container.cpp`** -> AI Confidence: **99.31%**
714. **`editor/docks/groups_editor.cpp`** -> AI Confidence: **99.31%**
715. **`editor/editor_data.cpp`** -> AI Confidence: **99.31%**
716. **`editor/editor_interface.cpp`** -> AI Confidence: **99.31%**
717. **`editor/editor_main_screen.cpp`** -> AI Confidence: **99.31%**
718. **`editor/editor_undo_redo_manager.cpp`** -> AI Confidence: **99.31%**
719. **`editor/export/editor_export_platform_pc.cpp`** -> AI Confidence: **99.31%**
720. **`editor/export/editor_export_preset.cpp`** -> AI Confidence: **99.31%**
721. **`editor/export/project_export.cpp`** -> AI Confidence: **99.31%**
722. **`editor/file_system/editor_paths.cpp`** -> AI Confidence: **99.31%**
723. **`editor/gui/directory_create_dialog.cpp`** -> AI Confidence: **99.31%**
724. **`editor/gui/editor_bottom_panel.cpp`** -> AI Confidence: **99.31%**
725. **`editor/gui/editor_zoom_widget.cpp`** -> AI Confidence: **99.31%**
726. **`editor/gui/progress_dialog.cpp`** -> AI Confidence: **99.31%**
727. **`editor/gui/window_wrapper.cpp`** -> AI Confidence: **99.31%**
728. **`editor/import/fbx_importer_manager.cpp`** -> AI Confidence: **99.31%**
729. **`editor/import/import_defaults_editor.cpp`** -> AI Confidence: **99.31%**
730. **`editor/inspector/editor_properties.cpp`** -> AI Confidence: **99.31%**
731. **`editor/inspector/editor_resource_preview.cpp`** -> AI Confidence: **99.31%**
732. **`editor/inspector/editor_resource_tooltip_plugins.cpp`** -> AI Confidence: **99.31%**
733. **`editor/inspector/editor_sectioned_inspector.cpp`** -> AI Confidence: **99.31%**
734. **`editor/run/editor_run_bar.cpp`** -> AI Confidence: **99.31%**
735. **`editor/run/editor_run_native.cpp`** -> AI Confidence: **99.31%**
736. **`editor/run/game_view_plugin.cpp`** -> AI Confidence: **99.31%**
737. **`editor/scene/2d/physics/cast_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
738. **`editor/scene/2d/skeleton_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
739. **`editor/scene/2d/tiles/tile_set_scenes_collection_source_editor.cpp`** -> AI Confidence: **99.31%**
740. **`editor/scene/2d/tiles/tiles_editor_plugin.cpp`** -> AI Confidence: **99.31%**
741. **`editor/scene/3d/gizmos/physics/collision_shape_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
742. **`editor/scene/3d/gizmos/reflection_probe_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
743. **`editor/scene/3d/gizmos/spring_bone_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
744. **`editor/scene/3d/gpu_particles_collision_sdf_editor_plugin.cpp`** -> AI Confidence: **99.31%**
745. **`editor/scene/3d/multimesh_editor_plugin.cpp`** -> AI Confidence: **99.31%**
746. **`editor/scene/3d/node_3d_editor_gizmos.cpp`** -> AI Confidence: **99.31%**
747. **`editor/scene/3d/root_motion_editor_plugin.cpp`** -> AI Confidence: **99.31%**
748. **`editor/scene/3d/voxel_gi_editor_plugin.cpp`** -> AI Confidence: **99.31%**
749. **`editor/scene/connections_dialog.cpp`** -> AI Confidence: **99.31%**
750. **`editor/scene/group_settings_editor.cpp`** -> AI Confidence: **99.31%**
751. **`editor/scene/gui/font_config_plugin.cpp`** -> AI Confidence: **99.31%**
752. **`editor/scene/gui/theme_editor_preview.cpp`** -> AI Confidence: **99.31%**
753. **`editor/scene/material_editor_plugin.cpp`** -> AI Confidence: **99.31%**
754. **`editor/scene/particles_editor_plugin.cpp`** -> AI Confidence: **99.31%**
755. **`editor/scene/resource_preloader_editor_plugin.cpp`** -> AI Confidence: **99.31%**
756. **`editor/scene/texture/bit_map_editor_plugin.cpp`** -> AI Confidence: **99.31%**
757. **`editor/scene/texture/color_channel_selector.cpp`** -> AI Confidence: **99.31%**
758. **`editor/scene/texture/texture_editor_plugin.cpp`** -> AI Confidence: **99.31%**
759. **`editor/scene/texture/texture_layered_editor_plugin.cpp`** -> AI Confidence: **99.31%**
760. **`editor/script/find_in_files.cpp`** -> AI Confidence: **99.31%**
761. **`editor/script/script_editor_base.cpp`** -> AI Confidence: **99.31%**
762. **`editor/settings/editor_feature_profile.cpp`** -> AI Confidence: **99.31%**
763. **`editor/settings/project_settings_editor.cpp`** -> AI Confidence: **99.31%**
764. **`editor/shader/editor_native_shader_source_visualizer.cpp`** -> AI Confidence: **99.31%**
765. **`editor/themes/editor_icons.cpp`** -> AI Confidence: **99.31%**
766. **`editor/translations/localization_editor.cpp`** -> AI Confidence: **99.31%**
767. **`editor/version_control/version_control_editor_plugin.cpp`** -> AI Confidence: **99.31%**
768. **`main/performance.cpp`** -> AI Confidence: **99.31%**
769. **`modules/camera/camera_linux.cpp`** -> AI Confidence: **99.31%**
770. **`modules/csg/csg_shape.cpp`** -> AI Confidence: **99.31%**
771. **`modules/fbx/editor/editor_scene_importer_fbx2gltf.cpp`** -> AI Confidence: **99.31%**
772. **`modules/gdscript/gdscript_cache.cpp`** -> AI Confidence: **99.31%**
773. **`modules/gdscript/gdscript_editor.cpp`** -> AI Confidence: **99.31%**
774. **`modules/gdscript/gdscript_utility_functions.cpp`** -> AI Confidence: **99.31%**
775. **`modules/gdscript/language_server/gdscript_language_protocol.cpp`** -> AI Confidence: **99.31%**
776. **`modules/gdscript/tests/gdscript_test_runner_suite.h`** -> AI Confidence: **99.31%**
777. **`modules/glslang/register_types.cpp`** -> AI Confidence: **99.31%**
778. **`modules/gltf/tests/test_gltf_images.h`** -> AI Confidence: **99.31%**
779. **`modules/jolt_physics/joints/jolt_hinge_joint_3d.cpp`** -> AI Confidence: **99.31%**
780. **`modules/jolt_physics/objects/jolt_area_3d.cpp`** -> AI Confidence: **99.31%**
781. **`modules/jolt_physics/objects/jolt_body_3d.cpp`** -> AI Confidence: **99.31%**
782. **`modules/jolt_physics/objects/jolt_shaped_object_3d.cpp`** -> AI Confidence: **99.31%**
783. **`modules/jolt_physics/objects/jolt_soft_body_3d.cpp`** -> AI Confidence: **99.31%**
784. **`modules/jolt_physics/shapes/jolt_shape_3d.cpp`** -> AI Confidence: **99.31%**
785. **`modules/jolt_physics/spaces/jolt_motion_filter_3d.cpp`** -> AI Confidence: **99.31%**
786. **`modules/jolt_physics/spaces/jolt_space_3d.cpp`** -> AI Confidence: **99.31%**
787. **`modules/mbedtls/crypto_mbedtls.cpp`** -> AI Confidence: **99.31%**
788. **`modules/mono/csharp_script.cpp`** -> AI Confidence: **99.31%**
789. **`modules/mono/editor/hostfxr_resolver.cpp`** -> AI Confidence: **99.31%**
790. **`modules/mono/godotsharp_dirs.cpp`** -> AI Confidence: **99.31%**
791. **`modules/mono/utils/path_utils.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `thirdparty/pcre2/src/pcre2_internal.h` -> **99.8385%** Exposure
- `thirdparty/freetype/src/autofit/afscript.h` -> **0.0014%** Exposure
- `tests/core/string/test_string.cpp` -> **0.0001%** Exposure
- `thirdparty/basis_universal/encoder/basisu_miniz.h` -> **0.0001%** Exposure
### Exploit Generation Surface
- `SConstruct` -> **100.0%** Exposure
- `core/core_builders.py` -> **100.0%** Exposure
- `core/extension/make_interface_header.py` -> **100.0%** Exposure
- `doc/tools/doc_status.py` -> **100.0%** Exposure
- `doc/tools/make_rst.py` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `editor/editor_builders.py` -> **100.0%** Exposure
- `misc/scripts/dotnet_format.py` -> **100.0%** Exposure
- `misc/scripts/install_d3d12_sdk_windows.py` -> **100.0%** Exposure
- `modules/raycast/godot_update_embree.py` -> **100.0%** Exposure
- `platform/linuxbsd/detect.py` -> **100.0%** Exposure
### Raw Memory Manipulation
- `core/core_bind.cpp` -> **10.0%** Exposure
- `core/input/input_event_codec.cpp` -> **10.0%** Exposure
- `core/variant/variant_internal.h` -> **10.0%** Exposure
- `drivers/d3d12/rendering_device_driver_d3d12.cpp` -> **10.0%** Exposure
- `drivers/gles3/storage/particles_storage.cpp` -> **10.0%** Exposure
### Hardcoded Payload Artifacts
- `thirdparty/mbedtls/library/pk_internal.h` -> **100.0%** Exposure
- `thirdparty/icu4c/common/unicode/uloc.h` -> **99.8781%** Exposure
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/X509CertificateUtils.java` -> **99.7922%** Exposure
- `platform/android/java/lib/src/main/java/org/godotengine/godot/utils/GodotNetUtils.java` -> **99.7922%** Exposure
- `platform/macos/os_macos.mm` -> **37.2458%** Exposure
### Algorithmic DoS Exposure
- `core/core_builders.py` -> **100.0%** Exposure
- `core/extension/make_interface_header.py` -> **100.0%** Exposure
- `editor/editor_builders.py` -> **100.0%** Exposure
- `editor/icons/editor_icons_builders.py` -> **100.0%** Exposure
- `editor/template_builders.py` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `68` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `32274` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `modules/mono/editor/GodotTools/GodotTools/Ides/MessagingServer.cs` (CSHARP) -> Cumulative Risk: **956.23**
- **Archetype:** `file_cluster_4` (Distance: 11.572 IQR)
- **Magnitude:** 196.56 | **LOC:** 400 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 41.0), `Dispose` (Impact: 40.9), `MessagingServer` (Impact: 19.0)

### 2. `modules/mono/editor/GodotTools/GodotTools/Ides/MonoDevelop/Instance.cs` (CSHARP) -> Cumulative Risk: **954.22**
- **Archetype:** `file_cluster_13` (Distance: 12.664 IQR)
- **Magnitude:** 245.58 | **LOC:** 144 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Execute` (Impact: 87.2), `Instance` (Impact: 43.5), `Dispose` (Impact: 16.2)

### 3. `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/Client.cs` (CSHARP) -> Cumulative Risk: **914.45**
- **Archetype:** `file_cluster_4` (Distance: 11.034 IQR)
- **Magnitude:** 506.44 | **LOC:** 364 | **CtrlFlow:** 39.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `AcceptClient` (Impact: 53.5), `OnMetaFileDeleted` (Impact: 43.4), `ReadMetadataFile` (Impact: 43.0)

### 4. `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/Utils/SemaphoreExtensions.cs` (CSHARP) -> Cumulative Risk: **889.66**
- **Archetype:** `file_cluster_4` (Distance: 11.926 IQR)
- **Magnitude:** 64.16 | **LOC:** 33 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `SemaphoreSlimWaitReleaseWrapper` (Impact: 10.2), `UseAsync` (Impact: 7.2), `Dispose` (Impact: 5.2)

### 5. `modules/mono/editor/GodotTools/GodotTools/Ides/GodotIdeManager.cs` (CSHARP) -> Cumulative Risk: **872.28**
- **Archetype:** `file_cluster_8` (Distance: 10.975 IQR)
- **Magnitude:** 476.0 | **LOC:** 237 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `LaunchIde` (Impact: 185.0), `GetExternalEditorIdentity` (Impact: 75.0), `Dispose` (Impact: 37.2)

### 6. `modules/mono/editor/GodotTools/GodotTools.IdeMessaging.CLI/Program.cs` (CSHARP) -> Cumulative Risk: **871.05**
- **Archetype:** `file_cluster_4` (Distance: 9.712 IQR)
- **Magnitude:** 318.76 | **LOC:** 218 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `StartAsync` (Impact: 158.8), `SendRequest` (Impact: 49.6), `Main` (Impact: 19.1)

### 7. `thirdparty/libwebp/src/utils/thread_utils.c` (C) -> Cumulative Risk: **865.4**
- **Archetype:** `file_cluster_4` (Distance: 12.626 IQR)
- **Magnitude:** 462.68 | **LOC:** 371 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `pthread_cond_wait` (Impact: 294.3), `pthread_cond_init` (Impact: 5.8), `pthread_cond_signal` (Impact: 5.3)

### 8. `thirdparty/openxr/src/loader/runtime_interface.cpp` (CPP) -> Cumulative Risk: **849.96**
- **Archetype:** `file_cluster_4` (Distance: 13.963 IQR)
- **Magnitude:** 775.68 | **LOC:** 417 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9999%)
- **Heaviest Functions:** `RuntimeInterface::TryLoadingSingleRuntim` (Impact: 190.5), `RuntimeInterface::LoadRuntime` (Impact: 101.9), `RuntimeInterface::GetInstanceExtensionPr` (Impact: 44.2)

### 9. `modules/mono/glue/GodotSharp/GodotSharp/Core/Bridge/ScriptManagerBridge.types.cs` (CSHARP) -> Cumulative Risk: **845.79**
- **Archetype:** `file_cluster_13` (Distance: 12.795 IQR)
- **Magnitude:** 178.8 | **LOC:** 121 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `Remove` (Impact: 33.8), `Add` (Impact: 18.0), `RemoveByScriptType` (Impact: 16.2)

### 10. `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/Utils/NotifyAwaiter.cs` (CSHARP) -> Cumulative Risk: **844.88**
- **Archetype:** `file_cluster_13` (Distance: 13.169 IQR)
- **Magnitude:** 108.04 | **LOC:** 68 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `SetResult` (Impact: 17.3), `SetException` (Impact: 17.3), `OnCompleted` (Impact: 11.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `thirdparty/tinyexr/tinyexr.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.15 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.95 IQR)
- **Top Global Matches:** file_cluster_11: 16.15, file_cluster_8: 16.29, file_cluster_4: 16.295
- **Magnitude:** 17256.72 | **LOC:** 9401 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 523
- **Risk Profile:** Cognitive Load (71.1454%), Tech Debt (23.2349%)
**Top Internal Functions/Classes:**
  * `DecodePixelData` (Impact: 11038.3 | O(2^N) | DB: 523)
  * `FindZFPCompressionParam` (Impact: 230.7 | O(N^6) | DB: 26)
  * `DecompressPiz` (Impact: 206.8 | O(N^6) | DB: 46)
    * *Intent:* // // Encode (compress) ni values based on the Huffman encoding table hcode: //
  * `hufDecode` (Impact: 175.5 | O(N^5) | DB: 22)
    * *Intent:* // // This function assumes that when it is called, array frq // indicates the frequency of all poss...
  * `DecompressZfp` (Impact: 152.1 | O(N^6) | DB: 24)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 807`, `structural_boundaries: 323`, `args: 270`, `func_start: 92`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 41`, `state_mutation: 3873`, `dead_code: 38`, `planned_debt: 11`, `fragile_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 36`, `import: 5`
* *Defense:* `safety: 6`, `doc: 56`, `immutability_locks: 294`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` float.h, intrin.h, nanozlib.h, sstream, cstdlib, string, fcntl.h, cstdint...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `thirdparty/embree/common/math/vec3fa.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.939 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_7: 16.939, file_cluster_8: 17.01, file_cluster_13: 17.044
- **Magnitude:** 11579.83 | **LOC:** 792 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (26.728%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 245`, `args: 220`, `func_start: 225`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 741`, `dead_code: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 4`, `doc: 1590`, `immutability_locks: 394`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` vec3fa_sycl.h, sse.h, emath.h, alloc.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `servers/rendering/shader_language.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.859 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.501 IQR)
- **Top Global Matches:** file_cluster_8: 14.859, file_cluster_13: 15.181, file_cluster_7: 15.214
- **Magnitude:** 11191.96 | **LOC:** 12235 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 776
- **Risk Profile:** Cognitive Load (96.9272%), Tech Debt (24.4337%)
**Top Internal Functions/Classes:**
  * `ShaderLanguage::_validate_operator` (Impact: 4690.2 | O(N^3) | DB: 776)
  * `ShaderLanguage::_get_token` (Impact: 603.5 | O(N^2) | DB: 150)
  * `ShaderLanguage::_parse_shader` (Impact: 345.7 | O(N^2) | DB: 118)
  * `ShaderLanguage::_find_identifier` (Impact: 231.2 | O(N^1) | DB: 54)
    * *Intent:* #endif // DEBUG_ENABLED
  * `ShaderLanguage::_parse_shader_mode` (Impact: 139.3 | O(N^2) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2086`, `structural_boundaries: 411`, `args: 324`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 2`, `state_mutation: 4396`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 43`
* *Architecture:* `import: 9`
* *Defense:* `doc: 4`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` local_vector.h, engine.h, rendering_server_globals.h, shader_language.h, rendering_server.h, rb_set.h, shader_types.h, renderer_compositor.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `servers/server_wrap_mt_common.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.381 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.724 IQR)
- **Top Global Matches:** file_cluster_8: 13.381, file_cluster_12: 13.734, file_cluster_11: 13.852
- **Magnitude:** 10860.8 | **LOC:** 814 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (59.9443%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 144`, `args: 63`, `func_start: 61`
* *Risk/State:* `state_mutation: 249`
* *Architecture:* `import: 1`
* *Defense:* `safety: 61`, `doc: 19`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.066
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` engine.h
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `scene/gui/rich_text_label.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 16.006 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.353 IQR)
- **Top Global Matches:** file_cluster_8: 16.006, file_cluster_13: 16.269, file_cluster_7: 16.339
- **Magnitude:** 9892.2 | **LOC:** 8433 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 744
- **Risk Profile:** Cognitive Load (94.6063%), Tech Debt (91.9301%)
**Top Internal Functions/Classes:**
  * `RichTextLabel::_add_list_prefixes` (Impact: 1808.2 | O(N^3) | DB: 744)
  * `RichTextLabel::gui_input` (Impact: 374.1 | O(N^2) | DB: 224)
  * `RichTextLabel::_accessibility_update_lin` (Impact: 213.3 | O(N^2) | DB: 106)
  * `RichTextLabel::_notification` (Impact: 203.9 | O(N^1) | DB: 106)
  * `RichTextLabel::_update_selection` (Impact: 97.4 | O(N^1) | DB: 63)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1388`, `structural_boundaries: 257`, `args: 494`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5982`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 132`
* *Architecture:* `import: 25`
* *Defense:* `doc: 4`, `sync_locks: 23`, `immutability_locks: 140`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` resource_loader.h, popup_menu.h, class_db.h, rich_text_effect.h, theme_db.h, os.h, scene_tree.h, accessibility_server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/embree/common/math/emath.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.3 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.047 IQR)
- **Top Global Matches:** file_cluster_8: 14.3, file_cluster_13: 14.412, file_cluster_16: 14.464
- **Magnitude:** 9846.23 | **LOC:** 469 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.9476%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 224`, `args: 140`, `func_start: 146`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 383`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.666
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` xmmintrin.h, cmath, platform.h, emmintrin.h, intrinsics.h, math_sycl.h, immintrin.h, constants.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `platform/linuxbsd/x11/display_server_x11.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.609 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.616 IQR)
- **Top Global Matches:** file_cluster_8: 15.609, file_cluster_13: 15.769, file_cluster_11: 15.826
- **Magnitude:** 8359.02 | **LOC:** 7571 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 38.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 176
- **Risk Profile:** Cognitive Load (93.6102%), Tech Debt (89.1223%)
**Top Internal Functions/Classes:**
  * `DisplayServerX11::DisplayServerX11` (Impact: 878.7 | O(N^2) | DB: 176)
  * `DisplayServerX11::_handle_key_event` (Impact: 216.2 | O(N^1) | DB: 127)
  * `DisplayServerX11::_clipboard_transfer_ow` (Impact: 136.3 | O(N^2) | DB: 102)
  * `DisplayServerX11::_create_window` (Impact: 132.4 | O(N^1) | DB: 105)
  * `DisplayServerX11::_validate_fullscreen_o` (Impact: 119.9 | O(N^1) | DB: 92)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1251`, `structural_boundaries: 305`, `args: 302`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 14`, `state_mutation: 4989`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 131`
* *Architecture:* `import: 43`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` freedesktop_portal_desktop.h, project_settings.h, Xutil.h, Xinerama.h, renderer_compositor_rd.h, display_server_x11.h, cstdlib, shape.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/harfbuzz/src/hb-ot-layout-gsubgpos.hh` (CPP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.921 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.757 IQR)
- **Top Global Matches:** file_cluster_8: 13.921, file_cluster_11: 14.157, file_cluster_13: 14.218
- **Magnitude:** 7712.02 | **LOC:** 5061 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 454
- **Risk Profile:** Cognitive Load (92.0078%), Tech Debt (97.7278%)
**Top Internal Functions/Classes:**
  * `match_input` (Impact: 5193.2 | O(2^N) | DB: 454)
  * `recurse` (Impact: 56.0 | O(2^N) | DB: 11)
  * `next` (Impact: 23.4 | O(N^1) | DB: 6)
  * `prev` (Impact: 23.4 | O(N^1) | DB: 6)
  * `would_match_input` (Impact: 20.8 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 670`, `args: 103`, `func_start: 196`, `class_start: 48`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 1920`, `planned_debt: 2`, `duplicate_logic: 45`
* *Architecture:* `api: 23`, `import: 7`
* *Defense:* `safety: 8`, `immutability_locks: 378`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` hb-set.hh, hb-ot-layout-gdef-table.hh, hb-ot-map.hh, hb-buffer.hh, hb.hh, hb-ot-layout-common.hh, hb-map.hh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/text_server_adv/text_server_adv.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.588 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.79 IQR)
- **Top Global Matches:** file_cluster_8: 15.588, file_cluster_13: 15.837, file_cluster_7: 15.909
- **Magnitude:** 7167.1 | **LOC:** 8441 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 72.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 230
- **Risk Profile:** Cognitive Load (93.8351%), Tech Debt (93.9197%)
**Top Internal Functions/Classes:**
  * `TextServerAdvanced::_shape_run` (Impact: 581.8 | O(N^1) | DB: 230)
  * `TextServerAdvanced::_is_valid_identifier` (Impact: 311.6 | O(N^1) | DB: 78)
  * `TextServerAdvanced::_shaped_text_update_` (Impact: 277.8 | O(N^2) | DB: 122)
  * `TextServerAdvanced::_shaped_text_shape` (Impact: 247.8 | O(N^2) | DB: 90)
  * `TextServerAdvanced::_shaped_text_overrun` (Impact: 243.0 | O(N^1) | DB: 151)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1094`, `structural_boundaries: 266`, `args: 247`, `func_start: 163`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 2`, `state_mutation: 4090`, `duplicate_logic: 22`, `orphaned_logic: 121`
* *Architecture:* `import: 18`
* *Defense:* `doc: 9`, `sync_locks: 196`, `immutability_locks: 295`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` project_settings.h, edge-selectors.h, msdfgen.h, worker_thread_pool.h, modules_enabled.gen.h, icudata.gen.h, EdgeHolder.h, translation_server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/string/ustring.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.209 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.936 IQR)
- **Top Global Matches:** file_cluster_8: 15.209, file_cluster_13: 15.444, file_cluster_11: 15.447
- **Magnitude:** 6919.78 | **LOC:** 5832 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 95
- **Risk Profile:** Cognitive Load (79.0413%), Tech Debt (99.9973%)
**Top Internal Functions/Classes:**
  * `_xml_unescape` (Impact: 239.7 | O(N^1) | DB: 95)
  * `built_in_strtod` (Impact: 81.5 | O(N^1) | DB: 49)
  * `String::_separate_compound_words` (Impact: 62.6 | O(N^1) | DB: 40)
  * `String::parse_url` (Impact: 60.4 | O(N^1) | DB: 43)
  * `_replace_common` (Impact: 52.5 | O(N^1) | DB: 28)
    * *Intent:* // Copy rest, skipping `char`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1164`, `structural_boundaries: 488`, `args: 231`, `func_start: 210`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 15`, `state_mutation: 4353`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 76`, `orphaned_logic: 120`
* *Architecture:* `import: 15`
* *Defense:* `doc: 8`, `immutability_locks: 455`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` math_funcs.h, grisu2.h, print_string.h, version_generated.gen.h, ustring.h, translation_server.h, color.h, ucaps.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/pcre2/src/pcre2_compile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.727 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.379 IQR)
- **Top Global Matches:** file_cluster_8: 14.727, file_cluster_7: 14.976, file_cluster_11: 14.978
- **Magnitude:** 6679.72 | **LOC:** 11344 | **CtrlFlow:** 94.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 250
- **Risk Profile:** Cognitive Load (88.6249%), Tech Debt (7.8908%)
**Top Internal Functions/Classes:**
  * `find_recurse` (Impact: 1553.1 | O(2^N) | DB: 250)
    * *Intent:* /* Not a numerical recursion. Perl allows spaces and tabs after { and before } but not for other del...
  * `check_posix_syntax` (Impact: 388.8 | O(N^6) | DB: 76)
    * *Intent:* /* Now process the quantifier for real. We know it must be {n} or {n,} or {,m}
  * `show_parsed` (Impact: 311.1 | O(N^2) | DB: 79)
    * *Intent:* /* We also need a table of characters that may follow \c in an EBCDIC environment for characters 0-3...
  * `is_anchored` (Impact: 134.7 | O(2^N) | DB: 6)
  * `first_significant_code` (Impact: 63.3 | O(N^2) | DB: 8)
    * *Intent:* /************************************************* * Read a subpattern or VERB name * **************...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1569`, `structural_boundaries: 92`, `args: 2`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 3362`, `orphaned_logic: 1`
* *Architecture:* `api: 687`, `import: 2`
* *Defense:* `doc: 18`, `immutability_locks: 17`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pcre2_compile.h, pcre2_printint_inc.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/vulkan/rendering_device_driver_vulkan.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.784 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.178 IQR)
- **Top Global Matches:** file_cluster_8: 15.784, file_cluster_13: 15.992, file_cluster_11: 16.032
- **Magnitude:** 6364.68 | **LOC:** 7438 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 26.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 534
- **Risk Profile:** Cognitive Load (79.0667%), Tech Debt (94.8551%)
**Top Internal Functions/Classes:**
  * `RenderingDeviceDriverVulkan::swap_chain_` (Impact: 744.2 | O(N^2) | DB: 506)
  * `RenderingDeviceDriverVulkan::_add_queue_` (Impact: 296.9 | O(N^1) | DB: 534)
  * `RenderingDeviceDriverVulkan::render_pipe` (Impact: 188.3 | O(N^1) | DB: 203)
  * `RenderingDeviceDriverVulkan::command_que` (Impact: 86.6 | O(N^1) | DB: 59)
  * `RenderingDeviceDriverVulkan::swap_chain_` (Impact: 61.3 | O(N^2) | DB: 31)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 691`, `structural_boundaries: 182`, `args: 473`, `func_start: 119`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 9`, `state_mutation: 4416`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 5`, `duplicate_logic: 44`, `orphaned_logic: 23`
* *Architecture:* `import: 12`
* *Defense:* `safety: 136`, `doc: 65`, `sync_locks: 16`, `immutability_locks: 268`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` project_settings.h, vulkan_hooks.h, engine.h, fixed_vector.h, smolv.h, swappyVk.h, rendering_device_driver_vulkan.h, java_godot_wrapper.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/scene/canvas_item_editor_plugin.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.815 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.386 IQR)
- **Top Global Matches:** file_cluster_8: 15.815, file_cluster_13: 15.984, file_cluster_11: 16.152
- **Magnitude:** 6163.92 | **LOC:** 6815 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(N^2) | **DB Complexity:** 351
- **Risk Profile:** Cognitive Load (79.1888%), Tech Debt (40.2617%)
**Top Internal Functions/Classes:**
  * `CanvasItemEditor::_draw_selection` (Impact: 431.5 | O(N^1) | DB: 351)
  * `CanvasItemEditor::_gui_input_anchors` (Impact: 217.2 | O(N^2) | DB: 55)
  * `CanvasItemEditor::_gui_input_select` (Impact: 192.9 | O(N^2) | DB: 53)
  * `CanvasItemEditor::_gui_input_move` (Impact: 186.7 | O(N^1) | DB: 99)
  * `CanvasItemEditor::_gui_input_resize` (Impact: 162.6 | O(N^1) | DB: 76)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1096`, `structural_boundaries: 151`, `args: 530`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `state_mutation: 3670`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 39`
* *Architecture:* `api: 1`, `import: 48`
* *Defense:* `doc: 4`, `sync_locks: 4`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` audio_stream_player_2d.h, resource_loader.h, project_settings.h, base_button.h, rich_text_label.h, sprite_2d.h, class_db.h, packed_scene.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/basis_universal/encoder/basisu_enc.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.199 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.415 IQR)
- **Top Global Matches:** file_cluster_8: 15.199, file_cluster_11: 15.365, file_cluster_13: 15.368
- **Magnitude:** 5624.48 | **LOC:** 4319 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 723
- **Risk Profile:** Cognitive Load (79.3267%), Tech Debt (98.4326%)
**Top Internal Functions/Classes:**
  * `color_distance` (Impact: 1089.0 | O(N^2) | DB: 723)
  * `clean_astc_hdr_pixels` (Impact: 51.1 | O(N^2) | DB: 29)
  * `radix_sort` (Impact: 37.3 | O(N^1) | DB: 96)
  * `compute_pca_from_covar` (Impact: 24.6 | O(N^1) | DB: 18)
  * `float_to_half_non_neg_no_nan_inf` (Impact: 20.9 | O(N^1) | DB: 23)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 696`, `args: 135`, `func_start: 237`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 3945`, `planned_debt: 3`, `duplicate_logic: 50`
* *Architecture:* `api: 60`, `concurrency: 24`, `import: 12`
* *Defense:* `safety: 57`, `sync_locks: 2`, `immutability_locks: 369`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` unordered_map, ostream, basisu_transcoder_internal.h, map, basisu_math.h, basisu.h, functional, condition_variable...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `thirdparty/glslang/glslang/Include/Types.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.668 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.996 IQR)
- **Top Global Matches:** file_cluster_8: 13.668, file_cluster_11: 13.786, file_cluster_13: 13.803
- **Magnitude:** 5443.28 | **LOC:** 3089 | **CtrlFlow:** 64.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (82.4391%), Tech Debt (99.7367%)
**Top Internal Functions/Classes:**
  * `getCompleteString` (Impact: 2685.8 | O(2^N) | DB: 63)
  * `merge` (Impact: 183.6 | O(N^4) | DB: 41)
  * `getString` (Impact: 160.8 | O(N^4))
  * `deepCopy` (Impact: 158.6 | O(2^N) | DB: 25)
  * `computeNumComponents` (Impact: 123.5 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 528`, `structural_boundaries: 294`, `args: 59`, `func_start: 167`, `class_start: 6`
* *Risk/State:* `state_mutation: 977`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 32`
* *Architecture:* `api: 91`, `import: 6`
* *Defense:* `safety: 15`, `immutability_locks: 169`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Common.h, BaseTypes.h, ShaderLang.h, algorithm, arrays.h, SpirvIntrinsics.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scene/resources/animation.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.878 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.225 IQR)
- **Top Global Matches:** file_cluster_8: 14.878, file_cluster_13: 15.244, file_cluster_7: 15.251
- **Magnitude:** 5326.2 | **LOC:** 6559 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 549
- **Risk Profile:** Cognitive Load (76.5294%), Tech Debt (27.816%)
**Top Internal Functions/Classes:**
  * `Animation::_set` (Impact: 526.7 | O(N^1) | DB: 549)
    * *Intent:* /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF */ /* MERCHANTABILITY, FITNESS...
  * `Animation::compress` (Impact: 265.6 | O(N^1) | DB: 146)
  * `Animation::cubic_interpolate_in_time_var` (Impact: 262.3 | O(N^1) | DB: 67)
  * `Animation::interpolate_variant` (Impact: 159.2 | O(N^1) | DB: 40)
  * `Animation::blend_variant` (Impact: 138.8 | O(N^1) | DB: 38)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 257`, `args: 269`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3169`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `orphaned_logic: 26`
* *Architecture:* `import: 4`
* *Defense:* `doc: 4`, `immutability_locks: 241`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` animation.h, marshalls.h, animation.compat.inc, class_db.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platform/android/java/editor/src/main/assets/keystores/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/data/crypto/in.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/data/crypto/in.pub` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/certs/ca-bundle.crt` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/misc/ok_color_shader.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.615 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.243 IQR)
- **Top Global Matches:** file_cluster_8: 13.615, file_cluster_13: 14.094, file_cluster_7: 14.14
- **Magnitude:** 4975.97 | **LOC:** 664 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 31`, `args: 40`, `func_start: 22`
* *Risk/State:* `state_mutation: 682`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ustring.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `servers/rendering/renderer_rd/storage_rd/texture_storage.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.229 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.953 IQR)
- **Top Global Matches:** file_cluster_8: 15.229, file_cluster_7: 15.511, file_cluster_13: 15.54
- **Magnitude:** 4958.06 | **LOC:** 4956 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 296
- **Risk Profile:** Cognitive Load (78.088%), Tech Debt (99.6282%)
**Top Internal Functions/Classes:**
  * `TextureStorage::_validate_texture_format` (Impact: 311.8 | O(N^1) | DB: 296)
  * `TextureStorage::texture_create_from_nati` (Impact: 288.9 | O(N^1) | DB: 48)
  * `TextureStorage::_texture_format_from_rd` (Impact: 206.6 | O(N^1) | DB: 295)
  * `TextureStorage::update_decal_atlas` (Impact: 79.8 | O(N^2) | DB: 82)
  * `TextureStorage::update_decal_buffer` (Impact: 53.8 | O(N^1) | DB: 92)
    * *Intent:* // The texture supports sRGB override, create it for 3D usage.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 147`, `args: 267`, `func_start: 120`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 3320`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 19`, `orphaned_logic: 100`
* *Architecture:* `import: 8`
* *Defense:* `doc: 54`, `immutability_locks: 61`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` material_storage.h, engine.h, rendering_server_globals.h, uniform_set_cache_rd.h, renderer_scene_render_rd.h, copy_effects.h, texture_storage.h, framebuffer_cache_rd.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/vulkan/include/vulkan/vulkan_core.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.619 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 10.619, file_cluster_7: 11.302, file_cluster_12: 11.383
- **Magnitude:** 4912.4 | **LOC:** 24741 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (41.4387%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 6344`, `args: 1476`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1154`, `state_mutation: 4481`
* *Architecture:* `import: 12`
* *Defense:* `sync_locks: 13`, `immutability_locks: 2359`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vk_platform.h, vulkan_video_codec_h264std_encode.h, vulkan_video_codec_vp9std.h, vulkan_video_codec_av1std_encode.h, vulkan_video_codec_h265std.h, vulkan_video_codec_vp9std_decode.h, vulkan_video_codec_av1std_decode.h, vulkan_video_codec_av1std.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `servers/rendering/rendering_server.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.206 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.129 IQR)
- **Top Global Matches:** file_cluster_8: 15.206, file_cluster_13: 15.561, file_cluster_7: 15.577
- **Magnitude:** 4823.66 | **LOC:** 3822 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 303
- **Risk Profile:** Cognitive Load (91.3575%), Tech Debt (32.5892%)
**Top Internal Functions/Classes:**
  * `RenderingServer::_surface_set_data` (Impact: 927.6 | O(N^2) | DB: 303)
  * `RenderingServer::mesh_surface_make_offse` (Impact: 227.5 | O(N^1) | DB: 60)
  * `RenderingServer::_get_array_from_surface` (Impact: 185.4 | O(N^2) | DB: 170)
  * `RenderingServer::mesh_create_surface_dat` (Impact: 145.7 | O(N^1) | DB: 100)
  * `RenderingServer::global_shader_uniform_t` (Impact: 58.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `structural_boundaries: 88`, `args: 1319`, `func_start: 46`
* *Risk/State:* `high_risk_execution: 28`, `state_mutation: 2948`, `duplicate_logic: 6`, `orphaned_logic: 35`
* *Architecture:* `import: 11`
* *Defense:* `doc: 4`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` project_settings.h, class_db.h, shader_language.h, typed_array.h, shader_warnings.h, rendering_server.compat.inc, rendering_server_types.h, rendering_device.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/scene/3d/node_3d_editor_plugin.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.569 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.068 IQR)
- **Top Global Matches:** file_cluster_8: 14.569, file_cluster_13: 14.917, file_cluster_7: 14.946
- **Magnitude:** 4707.4 | **LOC:** 11167 | **CtrlFlow:** 85.9% | **Authorship Centralization:** 39.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 191
- **Risk Profile:** Cognitive Load (85.8657%), Tech Debt (29.776%)
**Top Internal Functions/Classes:**
  * `Node3DEditorViewport::_sinput` (Impact: 702.7 | O(N^2) | DB: 191)
  * `Node3DEditorViewport::_select_region` (Impact: 166.6 | O(N^1) | DB: 47)
  * `Node3DEditorViewport::_transform_gizmo_s` (Impact: 125.6 | O(N^1) | DB: 109)
  * `Node3DEditorViewport::_compute_transform` (Impact: 54.0 | O(N^1) | DB: 16)
  * `Node3DEditorViewport::_list_select` (Impact: 50.9 | O(N^1) | DB: 32)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 813`, `structural_boundaries: 134`, `args: 222`, `func_start: 74`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 2669`, `planned_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 68`
* *Architecture:* `import: 84`
* *Defense:* `safety: 3`, `doc: 24`, `immutability_locks: 180`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 84):` class_db.h, ray_cast_3d_gizmo_plugin.h, audio_stream_player_3d.h, editor_plugin_list.h, editor_translation_preview_menu.h, os.h, subviewport_container.h, fog_volume_gizmo_plugin.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `thirdparty/embree/kernels/common/scene_instance.h` (CPP) | Magnitude: 266.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 224, state_mutation: 117, immutability_locks: 69, structural_boundaries: 65
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/ExportedFields.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, decorators: 62, encapsulation: 61, scientific: 18
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/ExportedToolButtons.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, args: 4, closures: 4, indent_spaces: 4
- `thirdparty/embree/kernels/builders/priminfo.h` (CPP) | Magnitude: 107.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 39, state_mutation: 36, immutability_locks: 29
- `core/math/bvh_cull.inc` (CPP) | Magnitude: 609.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 367, indent_tabs: 316, api: 109, branch: 89

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `platform/web/eslint.config.cjs` (JAVASCRIPT) | Magnitude: 21.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 185, events: 45, decorators: 18, doc: 10
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Rect2I.cs` (CSHARP) | Magnitude: 306.86 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 196, doc: 180, structural_boundaries: 39, api: 30
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Rect2.cs` (CSHARP) | Magnitude: 365.52 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 239, doc: 196, structural_boundaries: 44, api: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `modules/mono/utils/string_utils.cpp` (CPP) | Magnitude: 370.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 131, indent_tabs: 113, branch: 110, pointers: 26
- `thirdparty/minizip/skipset.h` (CPP) | Magnitude: 264.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 185, pointers: 117, indent_spaces: 106, branch: 29
- `thirdparty/harfbuzz/src/hb-set-digest.hh` (CPP) | Magnitude: 238.78 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 77, structural_boundaries: 27, immutability_locks: 19
- `thirdparty/embree/kernels/subdiv/feature_adaptive_eval_simd.h` (CPP) | Magnitude: 484.5 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 177, indent_spaces: 143, immutability_locks: 59, branch: 40
- `thirdparty/harfbuzz/src/hb-bit-set.hh` (CPP) | Magnitude: 508.24 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 249, indent_spaces: 203, structural_boundaries: 76, branch: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `thirdparty/icu4c/common/utrie2.h` (CPP) | Magnitude: 116.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 140, state_mutation: 99, indent_spaces: 57, pointers: 37
- `thirdparty/freetype/include/freetype/config/public-macros.h` (CPP) | Magnitude: 16.36 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 13, reflection_metaprogramming: 9, explicit_casts: 4, branch: 1
- `thirdparty/icu4c/common/unicode/ustringtrie.h` (CPP) | Magnitude: 16.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, macros: 5, reflection_metaprogramming: 4, indent_spaces: 4
- `thirdparty/freetype/src/otvalid/otvcommn.h` (C) | Magnitude: 103.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 175, macros: 76, doc: 64, state_mutation: 42
- `core/profiling/profiling.h` (CPP) | Magnitude: 229.48 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 49, indent_tabs: 43, reflection_metaprogramming: 39, structural_boundaries: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `thirdparty/jolt_physics/Jolt/Core/RTTI.h` (CPP) | Magnitude: 110.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 568, structural_boundaries: 133, indent_tabs: 113, pointers: 92
- `scene/3d/remote_transform_3d.h` (CPP) | Magnitude: 21.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 11, immutability_locks: 11, args: 7
- `servers/rendering/renderer_rd/framebuffer_cache_rd.h` (CPP) | Magnitude: 437.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 310, indent_tabs: 200, pointers: 63, branch: 47
- `thirdparty/embree/common/algorithms/parallel_for.h` (CPP) | Magnitude: 239.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, state_mutation: 87, args: 38, structural_boundaries: 31
- `thirdparty/harfbuzz/src/hb-multimap.hh` (CPP) | Magnitude: 46.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, state_mutation: 18, structural_boundaries: 12, pointers: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `platform/web/js/engine/features.js` (JAVASCRIPT) | Magnitude: 40.34 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 45, doc: 16, state_mutation: 15, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `thirdparty/embree/kernels/bvh/node_intersector_packet.h` (CPP) | Magnitude: 1188.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: state_mutation: 730, indent_spaces: 663, doc: 616, immutability_locks: 362
- `thirdparty/jolt_physics/Jolt/Core/StringTools.h` (CPP) | Magnitude: 18.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, pointers: 13, immutability_locks: 10, doc: 8
- `platform/macos/display_server_macos_embedded.h` (OBJECTIVE-C) | Magnitude: 103.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 107, state_mutation: 81, immutability_locks: 68, func_start: 64
- `thirdparty/mingw-std-threads/mingw.invoke.h` (CPP) | Magnitude: 82.62 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, structural_boundaries: 71, indent_spaces: 71, explicit_casts: 18
- `thirdparty/jolt_physics/Jolt/Core/UnorderedMap.h` (CPP) | Magnitude: 83.32 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 63, indent_tabs: 42, structural_boundaries: 29, pointers: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `thirdparty/zstd/common/bits.h` (CPP) | Magnitude: 264.66 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, state_mutation: 83, branch: 41, structural_boundaries: 32
- `thirdparty/embree/kernels/subdiv/half_edge.h` (CPP) | Magnitude: 639.94 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 385, indent_spaces: 263, pointers: 84, branch: 70
- `platform/web/js/jsdoc2rst/publish.js` (JAVASCRIPT) | Magnitude: 284.7 | Delta: **0.304 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 255, state_mutation: 119, branch: 63, structural_boundaries: 53
- `drivers/gles3/shaders/SCsub` (PYTHON) | Magnitude: 15.36 | Delta: **0.454 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, branch: 5, comprehensions: 3, explicit_casts: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `core/object/script_instance.cpp` (CPP) | Magnitude: 8.4 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 36, immutability_locks: 10, branch: 9, structural_boundaries: 5
- `core/debugger/debugger_marshalls.h` (CPP) | Magnitude: 19.7 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 30, immutability_locks: 5, state_mutation: 4, doc: 4
- `modules/gdscript/gdscript_analyzer.h` (CPP) | Magnitude: 48.36 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 114, pointers: 98, immutability_locks: 73, args: 64
- `editor/animation/animation_blend_tree_editor_plugin.h` (CPP) | Magnitude: 22.96 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 110, safety_bypasses: 45, immutability_locks: 45, ui_framework: 17
- `modules/mono/editor/code_completion.cpp` (CPP) | Magnitude: 56.8 | Delta: **0.06 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 170, branch: 69, ui_framework: 26, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `modules/mono/editor/GodotTools/GodotTools/Ides/MessagingServer.cs` (CSHARP) | Magnitude: 196.56 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 39, concurrency: 36, state_mutation: 25
- `modules/mono/editor/GodotTools/GodotTools.IdeMessaging.CLI/ForwarderMessageHandler.cs` (CSHARP) | Magnitude: 69.14 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 43, concurrency: 37, structural_boundaries: 31, func_start: 21
- `drivers/metal/metal_objects_shared.cpp` (CPP) | Magnitude: 459.26 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 322, state_mutation: 270, pointers: 155, branch: 80
- `thirdparty/vhacd/src/VHACD-ASYNC.cpp` (CPP) | Magnitude: 331.08 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 252, state_mutation: 198, immutability_locks: 52, structural_boundaries: 51
- `platform/web/js/libs/audio.worklet.js` (JAVASCRIPT) | Magnitude: 371.88 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 263, indent_tabs: 164, branch: 38, immutability_locks: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `thirdparty/jolt_physics/Jolt/Renderer/DebugRendererSimple.h` (CPP) | Magnitude: 22.62 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 29, indent_tabs: 29, structural_boundaries: 13, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `thirdparty/mbedtls/include/mbedtls/asn1write.h` (CPP) | Magnitude: 28.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 142, pointers: 45, indent_spaces: 38, immutability_locks: 30
- `platform/android/java/lib/src/main/java/org/godotengine/godot/FullScreenGodotApp.java` (JAVA) | Magnitude: 12.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 3, class_start: 1, api: 1
- `thirdparty/sdl/include/SDL3/SDL_asyncio.h` (CPP) | Magnitude: 15.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, pointers: 11, sec_high_risk_execution: 7, structural_boundaries: 6
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Vector3.cs` (CSHARP) | Magnitude: 563.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 469, doc: 444, scientific: 126, structural_boundaries: 82
- `modules/mono/glue/GodotSharp/GodotSharp/Core/StringExtensions.cs` (CSHARP) | Magnitude: 1816.66 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 816, doc: 603, func_start: 180, structural_boundaries: 152

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `editor/animation/animation_player_editor_plugin.h` (CPP) | Magnitude: 118.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 227, structural_boundaries: 120, state_mutation: 81, pointers: 76
- `main/main.cpp` (CPP) | Magnitude: 1701.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1369, indent_tabs: 1343, branch: 482, pointers: 363
- `modules/godot_physics_2d/godot_body_2d.h` (CPP) | Magnitude: 418.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 257, state_mutation: 221, structural_boundaries: 87, immutability_locks: 73
- `thirdparty/graphite/src/inc/Main.h` (CPP) | Magnitude: 83.18 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 58, state_mutation: 58, indent_spaces: 49, macros: 45
- `thirdparty/jolt_physics/Jolt/Core/Factory.h` (CPP) | Magnitude: 18.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 13, doc: 10, immutability_locks: 10, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `editor/docks/history_dock.h` (CPP) | Magnitude: 25.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 16, structural_boundaries: 15, state_mutation: 9, pointers: 8
- `editor/gui/directory_create_dialog.h` (CPP) | Magnitude: 28.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 11, state_mutation: 11, pointers: 9
- `scene/3d/ccd_ik_3d.h` (CPP) | Magnitude: 14.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, ownership: 4, structural_boundaries: 3, pointers: 3
- `scene/3d/fabr_ik_3d.h` (CPP) | Magnitude: 14.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, ownership: 4, structural_boundaries: 3, pointers: 3
- `scene/3d/jacobian_ik_3d.h` (CPP) | Magnitude: 14.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, ownership: 4, structural_boundaries: 3, pointers: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `editor/editor_node.cpp` -> Churn: **100.0%** | Cog Load: 84.4567% | Debt: 66.285%
- `editor/scene/3d/node_3d_editor_plugin.cpp` -> Churn: **97.33%** | Cog Load: 85.8657% | Debt: 29.776%
- `editor/inspector/editor_inspector.cpp` -> Churn: **86.56%** | Cog Load: 39.312% | Debt: 94.4784%
- `editor/inspector/editor_properties.cpp` -> Churn: **86.08%** | Cog Load: 45.7426% | Debt: 98.7687%
- `editor/docks/editor_dock_manager.cpp` -> Churn: **85.18%** | Cog Load: 36.0861% | Debt: 96.3053%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `servers/server_wrap_mt_common.h` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 10860.8
- `thirdparty/pcre2/src/pcre2_compile.c` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 6679.72
- `thirdparty/glslang/glslang/Include/Types.h` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 5443.28
- `thirdparty/vulkan/include/vulkan/vulkan_core.h` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 4912.4
- `thirdparty/libjpeg-turbo/src/turbojpeg.c` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 4629.02

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `core/variant/variant.h` -> **Severity: 0.093** (Bridge: 0.0009 * Flux: 99.9491%)
- `core/object/object.h` -> **Severity: 0.069** (Bridge: 0.0007 * Flux: 100.0%)
- `core/object/class_db.h` -> **Severity: 0.048** (Bridge: 0.0005 * Flux: 100.0%)
- `core/io/resource.h` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 99.4812%)
- `servers/rendering/rendering_server.h` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 100.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/templates/safe_refcount.h` -> **Severity: 710.411** (Blast Radius: 7.905 * Doc Risk: 89.8686%)
- `core/typedefs.h` -> **Severity: 675.424** (Blast Radius: 42.491 * Doc Risk: 15.8957%)
- `core/object/ref_counted.h` -> **Severity: 523.644** (Blast Radius: 10.495 * Doc Risk: 49.8946%)
- `thirdparty/enet/enet/utility.h` -> **Severity: 398.264** (Blast Radius: 20.285 * Doc Risk: 19.6334%)
- `thirdparty/embree/common/sys/atomic.h` -> **Severity: 319.968** (Blast Radius: 4.221 * Doc Risk: 75.8039%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
