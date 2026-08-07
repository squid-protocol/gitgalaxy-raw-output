# ARCHITECTURAL_BRIEF: godot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/godot` |
| **Timestamp** | `2026-08-07T05:00:50.384233+00:00` |
| **Scan Duration** | `48.96s` |
| **Git Branch** | `master` |
| **Git Commit** | `4a919adccf8e398aceca75399c539078c54fe97f` |
| **Git Remote** | `https://github.com/godotengine/godot.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7913 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.444`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 5982 | 59.7% |
| file_cluster_13 | 2682 | 26.8% |
| file_cluster_9 | 318 | 3.2% |
| file_cluster_12 | 86 | 0.9% |
| file_cluster_16 | 62 | 0.6% |
| file_cluster_0 | 45 | 0.4% |
| file_cluster_7 | 43 | 0.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 27.2 | 12.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 54.6 | 69.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 18.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.9 | 2.7 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 54.3 | 86.4 | 0.0 |
| Commented Logic Exposure | 0.0 | 91.6 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 30.8 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.0 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 22.3 | 13.4 | 11.9 |
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

- `ShaderLanguage::_validate_operator` (@ `servers/rendering/shader_language.cpp`) -> Impact: **2391.1** | LOC: 1838
- `DecodePixelData` (@ `thirdparty/tinyexr/tinyexr.h`) -> Impact: **1649.2** | LOC: 1688
- `RichTextLabel::_draw_line` (@ `scene/gui/rich_text_label.cpp`) -> Impact: **1058.9** | LOC: 699
- `ColladaImport::_create_mesh_surfaces` (@ `editor/import/3d/editor_import_collada.cpp`) -> Impact: **981.2** | LOC: 1057
- `PointInOpPolygon` (@ `thirdparty/clipper2/src/clipper.engine.cpp`) -> Impact: **967.4** | LOC: 1473
- `RichTextLabel::_add_list_prefixes` (@ `scene/gui/rich_text_label.cpp`) -> Impact: **936.1** | LOC: 1283
- `JavaClass::_call_method` (@ `platform/android/java_class_wrapper.cpp`) -> Impact: **932.6** | LOC: 979
  * *Intent:* /* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, */ /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF */ /* MERC...
- `ShaderLanguage::_parse_block` (@ `servers/rendering/shader_language.cpp`) -> Impact: **872.2** | LOC: 1130
- `ClipperBase::InsertLocalMinimaIntoAEL` (@ `thirdparty/clipper2/src/clipper.engine.cpp`) -> Impact: **867.2** | LOC: 1340
- `RendererSceneCull::render_camera` (@ `servers/rendering/renderer_scene_cull.cpp`) -> Impact: **829.7** | LOC: 1005

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `thirdparty/harfbuzz/src` | 325 | 96056.1 | 55.78% | 41.16% |
| `scene/resources` | 136 | 50945.64 | 33.31% | 52.11% |
| `scene/gui` | 130 | 44951.4 | 32.99% | 37.99% |
| `servers/rendering` | 61 | 36331.64 | 41.88% | 43.35% |
| `thirdparty/embree/common/math` | 28 | 35220.59 | 36.04% | 74.74% |
| `scene/3d` | 117 | 31386.16 | 36.15% | 47.29% |
| `thirdparty/pcre2/src` | 41 | 29407.48 | 56.18% | 17.89% |
| `core/math` | 89 | 28611.98 | 49.7% | 61.85% |
| `thirdparty/libwebp/src/dsp` | 76 | 28280.67 | 64.33% | 4.54% |
| `core/io` | 106 | 25297.16 | 34.85% | 46.4% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `misc/utility/godot_gdb_pretty_print.py` -> **100.0%** Exposure
- `core/core_bind.cpp` -> **100.0%** Exposure
- `core/crypto/crypto_core.cpp` -> **100.0%** Exposure
- `core/debugger/local_debugger.cpp` -> **100.0%** Exposure
- `core/extension/gdextension_function_loader.cpp` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `editor/icons/editor_icons_builders.py` -> **100.0%** Exposure
- `misc/scripts/install_angle.py` -> **100.0%** Exposure
- `platform/web/emscripten_helpers.py` -> **100.0%** Exposure
- `core/config/engine.cpp` -> **100.0%** Exposure
- `core/config/engine.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scene/resources/visual_shader_nodes.cpp` -> **586** Orphaned Functions | **452** Duplicates
- `thirdparty/amd-fsr/ffx_a.h` -> **173** Orphaned Functions | **343** Duplicates
- `thirdparty/directx_headers/include/directx/d3dx12_state_object.h` -> **0** Orphaned Functions | **256** Duplicates
- `servers/text/text_server_extension.cpp` -> **203** Orphaned Functions | **45** Duplicates
- `servers/display/display_server.cpp` -> **167** Orphaned Functions | **78** Duplicates

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
192. **`thirdparty/freetype/src/autofit/afglobal.c`** -> AI Confidence: **99.48%**
193. **`thirdparty/freetype/src/bdf/bdfdrivr.c`** -> AI Confidence: **99.48%**
194. **`thirdparty/freetype/src/bzip2/ftbzip2.c`** -> AI Confidence: **99.48%**
195. **`thirdparty/freetype/src/cff/cffgload.c`** -> AI Confidence: **99.48%**
196. **`thirdparty/freetype/src/cff/cffload.c`** -> AI Confidence: **99.48%**
197. **`thirdparty/freetype/src/cff/cffobjs.c`** -> AI Confidence: **99.48%**
198. **`thirdparty/freetype/src/cff/cffparse.c`** -> AI Confidence: **99.48%**
199. **`thirdparty/freetype/src/cid/cidgload.c`** -> AI Confidence: **99.48%**
200. **`thirdparty/freetype/src/cid/cidobjs.c`** -> AI Confidence: **99.48%**
201. **`thirdparty/freetype/src/pcf/pcfdrivr.c`** -> AI Confidence: **99.48%**
202. **`thirdparty/freetype/src/pfr/pfrobjs.c`** -> AI Confidence: **99.48%**
203. **`thirdparty/freetype/src/psaux/cffdecode.c`** -> AI Confidence: **99.48%**
204. **`thirdparty/freetype/src/psaux/psauxmod.c`** -> AI Confidence: **99.48%**
205. **`thirdparty/freetype/src/psaux/psobjs.c`** -> AI Confidence: **99.48%**
206. **`thirdparty/freetype/src/psaux/t1decode.c`** -> AI Confidence: **99.48%**
207. **`thirdparty/freetype/src/raster/ftraster.c`** -> AI Confidence: **99.48%**
208. **`thirdparty/freetype/src/sdf/ftbsdf.c`** -> AI Confidence: **99.48%**
209. **`thirdparty/freetype/src/sdf/ftsdf.c`** -> AI Confidence: **99.48%**
210. **`thirdparty/freetype/src/sdf/ftsdfrend.c`** -> AI Confidence: **99.48%**
211. **`thirdparty/freetype/src/sfnt/sfobjs.c`** -> AI Confidence: **99.48%**
212. **`thirdparty/freetype/src/sfnt/sfwoff2.c`** -> AI Confidence: **99.48%**
213. **`thirdparty/freetype/src/sfnt/ttsbit.c`** -> AI Confidence: **99.48%**
214. **`thirdparty/freetype/src/smooth/ftgrays.c`** -> AI Confidence: **99.48%**
215. **`thirdparty/freetype/src/truetype/ttgload.c`** -> AI Confidence: **99.48%**
216. **`thirdparty/freetype/src/truetype/ttgxvar.c`** -> AI Confidence: **99.48%**
217. **`thirdparty/freetype/src/truetype/ttpload.c`** -> AI Confidence: **99.48%**
218. **`thirdparty/freetype/src/type1/t1driver.c`** -> AI Confidence: **99.48%**
219. **`thirdparty/freetype/src/type1/t1gload.c`** -> AI Confidence: **99.48%**
220. **`thirdparty/freetype/src/type1/t1load.c`** -> AI Confidence: **99.48%**
221. **`thirdparty/freetype/src/winfonts/winfnt.c`** -> AI Confidence: **99.48%**
222. **`thirdparty/libjpeg-turbo/src/jcphuff.c`** -> AI Confidence: **99.48%**
223. **`thirdparty/libjpeg-turbo/src/jdapistd.c`** -> AI Confidence: **99.48%**
224. **`thirdparty/libjpeg-turbo/src/turbojpeg.c`** -> AI Confidence: **99.48%**
225. **`thirdparty/libwebp/src/dec/frame_dec.c`** -> AI Confidence: **99.48%**
226. **`thirdparty/libwebp/src/enc/picture_tools_enc.c`** -> AI Confidence: **99.48%**
227. **`thirdparty/libwebp/src/enc/quant_enc.c`** -> AI Confidence: **99.48%**
228. **`thirdparty/libwebp/src/enc/vp8l_enc.c`** -> AI Confidence: **99.48%**
229. **`thirdparty/libwebp/src/mux/muxread.c`** -> AI Confidence: **99.48%**
230. **`thirdparty/libwebp/src/utils/huffman_encode_utils.c`** -> AI Confidence: **99.48%**
231. **`thirdparty/libwebp/src/utils/rescaler_utils.c`** -> AI Confidence: **99.48%**
232. **`thirdparty/miniupnpc/src/minissdpc.c`** -> AI Confidence: **99.48%**
233. **`thirdparty/miniupnpc/src/miniwget.c`** -> AI Confidence: **99.48%**
234. **`thirdparty/pcre2/src/pcre2_jit_compile.c`** -> AI Confidence: **99.48%**
235. **`thirdparty/directx_headers/include/directx/d3dx12.h`** -> AI Confidence: **99.44%**
236. **`thirdparty/openxr/src/common/xr_dependencies.h`** -> AI Confidence: **99.44%**
237. **`thirdparty/amd-fsr2/shaders/ffx_core.h`** -> AI Confidence: **99.43%**
238. **`thirdparty/zstd/common/compiler.h`** -> AI Confidence: **99.43%**
239. **`thirdparty/zstd/common/zstd_deps.h`** -> AI Confidence: **99.43%**
240. **`drivers/apple_embedded/display_server_apple_embedded.h`** -> AI Confidence: **99.43%**
241. **`drivers/apple_embedded/os_apple_embedded.h`** -> AI Confidence: **99.43%**
242. **`platform/macos/os_macos.h`** -> AI Confidence: **99.43%**
243. **`thirdparty/mbedtls/library/common.h`** -> AI Confidence: **99.43%**
244. **`core/typedefs.h`** -> AI Confidence: **99.42%**
245. **`thirdparty/harfbuzz/src/hb.hh`** -> AI Confidence: **99.42%**
246. **`thirdparty/mbedtls/include/mbedtls/platform.h`** -> AI Confidence: **99.42%**
247. **`thirdparty/sdl/SDL_internal.h`** -> AI Confidence: **99.42%**
248. **`thirdparty/sdl/include/build_config/SDL_build_config.h`** -> AI Confidence: **99.42%**
249. **`thirdparty/volk/volk.h`** -> AI Confidence: **99.42%**
250. **`thirdparty/zlib/zconf.h`** -> AI Confidence: **99.42%**
251. **`doc/tools/make_rst.py`** -> AI Confidence: **99.39%**
252. **`misc/scripts/validate_codeowners.py`** -> AI Confidence: **99.39%**
253. **`platform/windows/detect.py`** -> AI Confidence: **99.39%**
254. **`core/config/project_settings.cpp`** -> AI Confidence: **99.39%**
255. **`core/debugger/remote_debugger.cpp`** -> AI Confidence: **99.39%**
256. **`core/error/error_macros.cpp`** -> AI Confidence: **99.39%**
257. **`core/extension/gdextension_library_loader.cpp`** -> AI Confidence: **99.39%**
258. **`core/input/input_map.cpp`** -> AI Confidence: **99.39%**
259. **`core/io/pck_packer.cpp`** -> AI Confidence: **99.39%**
260. **`core/io/resource.cpp`** -> AI Confidence: **99.39%**
261. **`core/object/object.cpp`** -> AI Confidence: **99.39%**
262. **`core/string/translation_server.cpp`** -> AI Confidence: **99.39%**
263. **`core/string/ustring.cpp`** -> AI Confidence: **99.39%**
264. **`core/variant/variant.cpp`** -> AI Confidence: **99.39%**
265. **`drivers/gles3/rasterizer_scene_gles3.cpp`** -> AI Confidence: **99.39%**
266. **`drivers/gles3/storage/material_storage.cpp`** -> AI Confidence: **99.39%**
267. **`drivers/gles3/storage/texture_storage.cpp`** -> AI Confidence: **99.39%**
268. **`drivers/pulseaudio/audio_driver_pulseaudio.cpp`** -> AI Confidence: **99.39%**
269. **`drivers/windows/file_access_windows.cpp`** -> AI Confidence: **99.39%**
270. **`editor/debugger/debug_adapter/debug_adapter_protocol.cpp`** -> AI Confidence: **99.39%**
271. **`editor/debugger/editor_debugger_node.cpp`** -> AI Confidence: **99.39%**
272. **`editor/debugger/editor_profiler.cpp`** -> AI Confidence: **99.39%**
273. **`editor/debugger/editor_visual_profiler.cpp`** -> AI Confidence: **99.39%**
274. **`editor/doc/editor_help.cpp`** -> AI Confidence: **99.39%**
275. **`editor/docks/editor_dock_manager.cpp`** -> AI Confidence: **99.39%**
276. **`editor/docks/import_dock.cpp`** -> AI Confidence: **99.39%**
277. **`editor/editor_log.cpp`** -> AI Confidence: **99.39%**
278. **`editor/export/editor_export_platform.cpp`** -> AI Confidence: **99.39%**
279. **`editor/export/project_zip_packer.cpp`** -> AI Confidence: **99.39%**
280. **`editor/file_system/dependency_editor.cpp`** -> AI Confidence: **99.39%**
281. **`editor/file_system/editor_file_system.cpp`** -> AI Confidence: **99.39%**
282. **`editor/gui/code_editor.cpp`** -> AI Confidence: **99.39%**
283. **`editor/gui/create_dialog.cpp`** -> AI Confidence: **99.39%**
284. **`editor/gui/editor_dir_dialog.cpp`** -> AI Confidence: **99.39%**
285. **`editor/gui/editor_file_dialog.cpp`** -> AI Confidence: **99.39%**
286. **`editor/gui/editor_object_selector.cpp`** -> AI Confidence: **99.39%**
287. **`editor/gui/editor_quick_open_dialog.cpp`** -> AI Confidence: **99.39%**
288. **`editor/gui/editor_spin_slider.cpp`** -> AI Confidence: **99.39%**
289. **`editor/gui/editor_validation_panel.cpp`** -> AI Confidence: **99.39%**
290. **`editor/gui/touch_actions_panel.cpp`** -> AI Confidence: **99.39%**
291. **`editor/import/audio_stream_import_settings.cpp`** -> AI Confidence: **99.39%**
292. **`editor/import/resource_importer_dynamic_font.cpp`** -> AI Confidence: **99.39%**
293. **`editor/inspector/multi_node_edit.cpp`** -> AI Confidence: **99.39%**
294. **`editor/plugins/editor_plugin.cpp`** -> AI Confidence: **99.39%**
295. **`editor/project_manager/project_list.cpp`** -> AI Confidence: **99.39%**
296. **`editor/project_manager/project_manager.cpp`** -> AI Confidence: **99.39%**
297. **`editor/project_manager/quick_settings_dialog.cpp`** -> AI Confidence: **99.39%**
298. **`editor/scene/2d/abstract_polygon_2d_editor.cpp`** -> AI Confidence: **99.39%**
299. **`editor/scene/2d/parallax_background_editor_plugin.cpp`** -> AI Confidence: **99.39%**
300. **`editor/scene/2d/particles_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
301. **`editor/scene/2d/sprite_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
302. **`editor/scene/2d/tiles/atlas_merging_dialog.cpp`** -> AI Confidence: **99.39%**
303. **`editor/scene/2d/tiles/tile_map_layer_editor.cpp`** -> AI Confidence: **99.39%**
304. **`editor/scene/3d/gizmos/camera_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.39%**
305. **`editor/scene/3d/gizmos/light_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.39%**
306. **`editor/scene/3d/occluder_instance_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
307. **`editor/scene/3d/particles_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
308. **`editor/scene/3d/path_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
309. **`editor/scene/3d/polygon_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
310. **`editor/scene/3d/skeleton_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
311. **`editor/scene/curve_editor_plugin.cpp`** -> AI Confidence: **99.39%**
312. **`editor/scene/gui/control_editor_plugin.cpp`** -> AI Confidence: **99.39%**
313. **`editor/scene/particle_process_material_editor_plugin.cpp`** -> AI Confidence: **99.39%**
314. **`editor/scene/rename_dialog.cpp`** -> AI Confidence: **99.39%**
315. **`editor/scene/sprite_frames_editor_plugin.cpp`** -> AI Confidence: **99.39%**
316. **`editor/scene/texture/gradient_texture_2d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
317. **`editor/settings/action_map_editor.cpp`** -> AI Confidence: **99.39%**
318. **`editor/settings/editor_autoload_settings.cpp`** -> AI Confidence: **99.39%**
319. **`editor/settings/editor_settings.cpp`** -> AI Confidence: **99.39%**
320. **`editor/settings/event_listener_line_edit.cpp`** -> AI Confidence: **99.39%**
321. **`editor/shader/shader_editor_plugin.cpp`** -> AI Confidence: **99.39%**
322. **`editor/shader/shader_file_editor_plugin.cpp`** -> AI Confidence: **99.39%**
323. **`editor/themes/editor_fonts.cpp`** -> AI Confidence: **99.39%**
324. **`editor/translations/editor_translation.cpp`** -> AI Confidence: **99.39%**
325. **`modules/csg/editor/csg_gizmos.cpp`** -> AI Confidence: **99.39%**
326. **`modules/fbx/fbx_document.cpp`** -> AI Confidence: **99.39%**
327. **`modules/gdscript/gdscript.cpp`** -> AI Confidence: **99.39%**
328. **`modules/gdscript/language_server/gdscript_workspace.cpp`** -> AI Confidence: **99.39%**
329. **`modules/gdscript/tests/gdscript_test_runner.cpp`** -> AI Confidence: **99.39%**
330. **`modules/gltf/editor/editor_import_blend_runner.cpp`** -> AI Confidence: **99.39%**
331. **`modules/gltf/editor/editor_scene_importer_blend.cpp`** -> AI Confidence: **99.39%**
332. **`modules/gltf/extensions/physics/gltf_physics_shape.cpp`** -> AI Confidence: **99.39%**
333. **`modules/gltf/gltf_document.cpp`** -> AI Confidence: **99.39%**
334. **`modules/gridmap/grid_map.cpp`** -> AI Confidence: **99.39%**
335. **`modules/jolt_physics/spaces/jolt_contact_listener_3d.cpp`** -> AI Confidence: **99.39%**
336. **`modules/multiplayer/scene_cache_interface.cpp`** -> AI Confidence: **99.39%**
337. **`modules/multiplayer/scene_replication_interface.cpp`** -> AI Confidence: **99.39%**
338. **`modules/navigation_2d/2d/nav_mesh_generator_2d.cpp`** -> AI Confidence: **99.39%**
339. **`modules/navigation_3d/3d/nav_mesh_generator_3d.cpp`** -> AI Confidence: **99.39%**
340. **`modules/navigation_3d/editor/navigation_obstacle_3d_editor_plugin.cpp`** -> AI Confidence: **99.39%**
341. **`modules/objectdb_profiler/editor/data_viewers/class_view.cpp`** -> AI Confidence: **99.39%**
342. **`modules/objectdb_profiler/editor/data_viewers/node_view.cpp`** -> AI Confidence: **99.39%**
343. **`modules/objectdb_profiler/editor/data_viewers/refcounted_view.cpp`** -> AI Confidence: **99.39%**
344. **`modules/objectdb_profiler/editor/data_viewers/summary_view.cpp`** -> AI Confidence: **99.39%**
345. **`modules/openxr/scene/openxr_composition_layer.cpp`** -> AI Confidence: **99.39%**
346. **`platform/linuxbsd/freedesktop_portal_desktop.cpp`** -> AI Confidence: **99.39%**
347. **`platform/linuxbsd/godot_linuxbsd.cpp`** -> AI Confidence: **99.39%**
348. **`platform/linuxbsd/os_linuxbsd.cpp`** -> AI Confidence: **99.39%**
349. **`platform/linuxbsd/wayland/wayland_embedder.cpp`** -> AI Confidence: **99.39%**
350. **`platform/linuxbsd/x11/detect_prime_x11.cpp`** -> AI Confidence: **99.39%**
351. **`platform/windows/export/export_plugin.cpp`** -> AI Confidence: **99.39%**
352. **`platform/windows/windows_utils.cpp`** -> AI Confidence: **99.39%**
353. **`scene/3d/cpu_particles_3d.cpp`** -> AI Confidence: **99.39%**
354. **`scene/3d/physics/collision_object_3d.cpp`** -> AI Confidence: **99.39%**
355. **`scene/3d/physics/collision_shape_3d.cpp`** -> AI Confidence: **99.39%**
356. **`scene/3d/physics/static_body_3d.cpp`** -> AI Confidence: **99.39%**
357. **`scene/3d/skeleton_3d.cpp`** -> AI Confidence: **99.39%**
358. **`scene/animation/animation_player.cpp`** -> AI Confidence: **99.39%**
359. **`scene/debugger/scene_debugger.cpp`** -> AI Confidence: **99.39%**
360. **`scene/gui/color_picker.cpp`** -> AI Confidence: **99.39%**
361. **`scene/gui/control.cpp`** -> AI Confidence: **99.39%**
362. **`scene/gui/file_dialog.cpp`** -> AI Confidence: **99.39%**
363. **`scene/gui/graph_frame.cpp`** -> AI Confidence: **99.39%**
364. **`scene/gui/item_list.cpp`** -> AI Confidence: **99.39%**
365. **`scene/main/node.cpp`** -> AI Confidence: **99.39%**
366. **`scene/main/scene_tree.cpp`** -> AI Confidence: **99.39%**
367. **`scene/main/window.cpp`** -> AI Confidence: **99.39%**
368. **`scene/resources/material.cpp`** -> AI Confidence: **99.39%**
369. **`scene/resources/mesh.cpp`** -> AI Confidence: **99.39%**
370. **`scene/resources/resource_format_text.cpp`** -> AI Confidence: **99.39%**
371. **`scene/resources/shader.cpp`** -> AI Confidence: **99.39%**
372. **`servers/rendering/renderer_rd/renderer_canvas_render_rd.cpp`** -> AI Confidence: **99.39%**
373. **`servers/rendering/renderer_rd/renderer_compositor_rd.cpp`** -> AI Confidence: **99.39%**
374. **`servers/rendering/renderer_rd/renderer_scene_render_rd.cpp`** -> AI Confidence: **99.39%**
375. **`servers/rendering/renderer_rd/shader_rd.cpp`** -> AI Confidence: **99.39%**
376. **`servers/rendering/rendering_device.cpp`** -> AI Confidence: **99.39%**
377. **`tests/scene/test_audio_stream_wav.cpp`** -> AI Confidence: **99.39%**
378. **`thirdparty/brotli/common/platform.h`** -> AI Confidence: **99.39%**
379. **`thirdparty/graphite/src/Code.cpp`** -> AI Confidence: **99.39%**
380. **`thirdparty/graphite/src/Pass.cpp`** -> AI Confidence: **99.39%**
381. **`thirdparty/graphite/src/Silf.cpp`** -> AI Confidence: **99.39%**
382. **`thirdparty/harfbuzz/src/hb-ot-metrics.cc`** -> AI Confidence: **99.39%**
383. **`thirdparty/harfbuzz/src/hb-ot-shape.cc`** -> AI Confidence: **99.39%**
384. **`thirdparty/harfbuzz/src/hb-raster-svg-clip.cc`** -> AI Confidence: **99.39%**
385. **`thirdparty/harfbuzz/src/hb-raster-svg-color.cc`** -> AI Confidence: **99.39%**
386. **`thirdparty/jolt_physics/Jolt/Core/Core.h`** -> AI Confidence: **99.39%**
387. **`thirdparty/mbedtls/include/mbedtls/oid.h`** -> AI Confidence: **99.39%**
388. **`thirdparty/minizip/skipset.h`** -> AI Confidence: **99.39%**
389. **`thirdparty/openxr/src/external/jsoncpp/src/lib_json/json_reader.cpp`** -> AI Confidence: **99.39%**
390. **`thirdparty/openxr/src/external/jsoncpp/src/lib_json/json_writer.cpp`** -> AI Confidence: **99.39%**
391. **`thirdparty/openxr/src/loader/api_layer_interface.cpp`** -> AI Confidence: **99.39%**
392. **`thirdparty/openxr/src/loader/manifest_file.cpp`** -> AI Confidence: **99.39%**
393. **`thirdparty/thorvg/src/loaders/svg/tvgXmlParser.cpp`** -> AI Confidence: **99.39%**
394. **`drivers/apple_embedded/godot_view_renderer.mm`** -> AI Confidence: **99.39%**
395. **`platform/web/eslint.config.cjs`** -> AI Confidence: **99.39%**
396. **`thirdparty/freetype/src/base/ftglyph.c`** -> AI Confidence: **99.39%**
397. **`thirdparty/freetype/src/base/ftobjs.c`** -> AI Confidence: **99.39%**
398. **`thirdparty/freetype/src/cid/cidload.c`** -> AI Confidence: **99.39%**
399. **`thirdparty/freetype/src/gxvalid/gxvmod.c`** -> AI Confidence: **99.39%**
400. **`thirdparty/freetype/src/gzip/ftgzip.c`** -> AI Confidence: **99.39%**
401. **`thirdparty/freetype/src/pfr/pfrdrivr.c`** -> AI Confidence: **99.39%**
402. **`thirdparty/freetype/src/psaux/psintrp.c`** -> AI Confidence: **99.39%**
403. **`thirdparty/freetype/src/sfnt/sfdriver.c`** -> AI Confidence: **99.39%**
404. **`thirdparty/freetype/src/sfnt/ttcmap.c`** -> AI Confidence: **99.39%**
405. **`thirdparty/freetype/src/sfnt/ttcolr.c`** -> AI Confidence: **99.39%**
406. **`thirdparty/freetype/src/sfnt/ttsvg.c`** -> AI Confidence: **99.39%**
407. **`thirdparty/freetype/src/type1/t1objs.c`** -> AI Confidence: **99.39%**
408. **`thirdparty/libpng/pngpriv.h`** -> AI Confidence: **99.39%**
409. **`thirdparty/libwebp/src/dec/alpha_dec.c`** -> AI Confidence: **99.39%**
410. **`thirdparty/libwebp/src/dec/io_dec.c`** -> AI Confidence: **99.39%**
411. **`thirdparty/libwebp/src/dsp/lossless_avx2.c`** -> AI Confidence: **99.39%**
412. **`thirdparty/libwebp/src/dsp/lossless_enc_avx2.c`** -> AI Confidence: **99.39%**
413. **`thirdparty/libwebp/src/dsp/lossless_enc_sse2.c`** -> AI Confidence: **99.39%**
414. **`thirdparty/libwebp/src/dsp/rescaler_sse2.c`** -> AI Confidence: **99.39%**
415. **`thirdparty/libwebp/src/enc/analysis_enc.c`** -> AI Confidence: **99.39%**
416. **`thirdparty/libwebp/src/enc/backward_references_cost_enc.c`** -> AI Confidence: **99.39%**
417. **`thirdparty/libwebp/src/enc/backward_references_enc.c`** -> AI Confidence: **99.39%**
418. **`thirdparty/libwebp/src/enc/filter_enc.c`** -> AI Confidence: **99.39%**
419. **`thirdparty/libwebp/src/enc/frame_enc.c`** -> AI Confidence: **99.39%**
420. **`thirdparty/libwebp/src/enc/histogram_enc.c`** -> AI Confidence: **99.39%**
421. **`thirdparty/libwebp/src/enc/picture_psnr_enc.c`** -> AI Confidence: **99.39%**
422. **`thirdparty/libwebp/src/enc/predictor_enc.c`** -> AI Confidence: **99.39%**
423. **`thirdparty/libwebp/src/enc/webp_enc.c`** -> AI Confidence: **99.39%**
424. **`thirdparty/miniupnpc/src/connecthostport.c`** -> AI Confidence: **99.39%**
425. **`thirdparty/miniupnpc/src/receivedata.c`** -> AI Confidence: **99.39%**
426. **`core/extension/gdextension_manager.cpp`** -> AI Confidence: **99.35%**
427. **`editor/export/export_template_manager.cpp`** -> AI Confidence: **99.35%**
428. **`editor/import/resource_importer_texture_atlas.cpp`** -> AI Confidence: **99.35%**
429. **`editor/inspector/editor_preview_plugins.cpp`** -> AI Confidence: **99.35%**
430. **`editor/run/run_instances_dialog.cpp`** -> AI Confidence: **99.35%**
431. **`editor/scene/2d/tiles/tile_atlas_view.cpp`** -> AI Confidence: **99.35%**
432. **`editor/settings/editor_command_palette.cpp`** -> AI Confidence: **99.35%**
433. **`editor/shader/shader_create_dialog.cpp`** -> AI Confidence: **99.35%**
434. **`editor/shader/shader_globals_editor.cpp`** -> AI Confidence: **99.35%**
435. **`platform/windows/os_windows.cpp`** -> AI Confidence: **99.35%**
436. **`thirdparty/thorvg/src/loaders/svg/tvgSvgSceneBuilder.cpp`** -> AI Confidence: **99.35%**
437. **`thirdparty/freetype/src/truetype/ttdriver.c`** -> AI Confidence: **99.35%**
438. **`thirdparty/libwebp/src/mux/anim_encode.c`** -> AI Confidence: **99.35%**
439. **`drivers/d3d12/SCsub`** -> AI Confidence: **99.34%**
440. **`platform/windows/SCsub`** -> AI Confidence: **99.34%**
441. **`core/debugger/local_debugger.cpp`** -> AI Confidence: **99.34%**
442. **`core/io/dir_access.cpp`** -> AI Confidence: **99.34%**
443. **`core/io/http_client_tcp.cpp`** -> AI Confidence: **99.34%**
444. **`core/math/geometry_2d.cpp`** -> AI Confidence: **99.34%**
445. **`drivers/apple/os_log_logger.cpp`** -> AI Confidence: **99.34%**
446. **`drivers/gles3/shader_gles3.cpp`** -> AI Confidence: **99.34%**
447. **`drivers/gles3/storage/config.cpp`** -> AI Confidence: **99.34%**
448. **`drivers/gles3/storage/mesh_storage.cpp`** -> AI Confidence: **99.34%**
449. **`drivers/metal/metal3_objects.cpp`** -> AI Confidence: **99.34%**
450. **`editor/audio/audio_stream_randomizer_editor_plugin.cpp`** -> AI Confidence: **99.34%**
451. **`editor/gui/editor_title_bar.cpp`** -> AI Confidence: **99.34%**
452. **`editor/import/3d/post_import_plugin_skeleton_track_organizer.cpp`** -> AI Confidence: **99.34%**
453. **`editor/import/editor_atlas_packer.cpp`** -> AI Confidence: **99.34%**
454. **`editor/import/resource_importer_csv_translation.cpp`** -> AI Confidence: **99.34%**
455. **`editor/import/resource_importer_imagefont.cpp`** -> AI Confidence: **99.34%**
456. **`editor/inspector/input_event_editor_plugin.cpp`** -> AI Confidence: **99.34%**
457. **`editor/settings/editor_layouts_dialog.cpp`** -> AI Confidence: **99.34%**
458. **`editor/translations/packed_scene_translation_parser_plugin.cpp`** -> AI Confidence: **99.34%**
459. **`modules/basis_universal/image_compress_basisu.cpp`** -> AI Confidence: **99.34%**
460. **`modules/cvtt/image_compress_cvtt.cpp`** -> AI Confidence: **99.34%**
461. **`modules/dds/tests/test_dds.h`** -> AI Confidence: **99.34%**
462. **`modules/etcpak/image_compress_etcpak.cpp`** -> AI Confidence: **99.34%**
463. **`modules/gdscript/gdscript_resource_format.cpp`** -> AI Confidence: **99.34%**
464. **`modules/gdscript/gdscript_tokenizer.cpp`** -> AI Confidence: **99.34%**
465. **`modules/gdscript/gdscript_vm.cpp`** -> AI Confidence: **99.34%**
466. **`modules/gdscript/language_server/gdscript_extend_parser.cpp`** -> AI Confidence: **99.34%**
467. **`modules/godot_physics_2d/godot_body_2d.cpp`** -> AI Confidence: **99.34%**
468. **`modules/godot_physics_3d/godot_body_3d.cpp`** -> AI Confidence: **99.34%**
469. **`modules/multiplayer/scene_multiplayer.cpp`** -> AI Confidence: **99.34%**
470. **`modules/navigation_2d/2d/nav_map_builder_2d.cpp`** -> AI Confidence: **99.34%**
471. **`modules/navigation_3d/3d/nav_map_builder_3d.cpp`** -> AI Confidence: **99.34%**
472. **`modules/navigation_3d/3d/nav_mesh_queries_3d.cpp`** -> AI Confidence: **99.34%**
473. **`modules/openxr/editor/openxr_binding_modifiers_dialog.cpp`** -> AI Confidence: **99.34%**
474. **`modules/theora/register_types.cpp`** -> AI Confidence: **99.34%**
475. **`platform/ios/export/export_plugin.cpp`** -> AI Confidence: **99.34%**
476. **`platform/windows/windows_terminal_logger.cpp`** -> AI Confidence: **99.34%**
477. **`scene/2d/skeleton_2d.cpp`** -> AI Confidence: **99.34%**
478. **`scene/3d/bone_attachment_3d.cpp`** -> AI Confidence: **99.34%**
479. **`scene/3d/spring_bone_simulator_3d.cpp`** -> AI Confidence: **99.34%**
480. **`scene/3d/voxelizer.cpp`** -> AI Confidence: **99.34%**
481. **`scene/gui/box_container.cpp`** -> AI Confidence: **99.34%**
482. **`scene/gui/grid_container.cpp`** -> AI Confidence: **99.34%**
483. **`scene/gui/menu_bar.cpp`** -> AI Confidence: **99.34%**
484. **`scene/gui/slider.cpp`** -> AI Confidence: **99.34%**
485. **`servers/rendering/renderer_rd/effects/bokeh_dof.cpp`** -> AI Confidence: **99.34%**
486. **`servers/rendering/renderer_rd/effects/copy_effects.cpp`** -> AI Confidence: **99.34%**
487. **`servers/rendering/renderer_rd/effects/ss_effects.cpp`** -> AI Confidence: **99.34%**
488. **`servers/rendering/renderer_rd/effects/vrs.cpp`** -> AI Confidence: **99.34%**
489. **`servers/rendering/renderer_rd/storage_rd/render_scene_data_rd.cpp`** -> AI Confidence: **99.34%**
490. **`tests/core/io/test_logger.cpp`** -> AI Confidence: **99.34%**
491. **`tests/core/math/test_projection.cpp`** -> AI Confidence: **99.34%**
492. **`tests/scene/test_code_edit.cpp`** -> AI Confidence: **99.34%**
493. **`thirdparty/harfbuzz/src/hb-ot-shaper-arabic.cc`** -> AI Confidence: **99.34%**
494. **`thirdparty/harfbuzz/src/hb-ot-shaper-indic.cc`** -> AI Confidence: **99.34%**
495. **`thirdparty/harfbuzz/src/hb-raster-svg-fill.cc`** -> AI Confidence: **99.34%**
496. **`thirdparty/mbedtls/include/mbedtls/pkcs12.h`** -> AI Confidence: **99.34%**
497. **`thirdparty/mbedtls/include/mbedtls/psa_util.h`** -> AI Confidence: **99.34%**
498. **`thirdparty/mbedtls/include/mbedtls/ssl_ciphersuites.h`** -> AI Confidence: **99.34%**
499. **`thirdparty/sdl/include/SDL3/SDL_assert.h`** -> AI Confidence: **99.34%**
500. **`thirdparty/thorvg/src/loaders/svg/tvgSvgLoader.cpp`** -> AI Confidence: **99.34%**
501. **`thirdparty/tinyexr/tinyexr.h`** -> AI Confidence: **99.34%**
502. **`thirdparty/wslay/wslay_net.h`** -> AI Confidence: **99.34%**
503. **`drivers/coreaudio/audio_driver_coreaudio.mm`** -> AI Confidence: **99.34%**
504. **`modules/openxr/extensions/platform/openxr_metal_extension.mm`** -> AI Confidence: **99.34%**
505. **`platform/macos/dir_access_macos.mm`** -> AI Confidence: **99.34%**
506. **`platform/macos/embedded_gl_manager.mm`** -> AI Confidence: **99.34%**
507. **`platform/macos/gl_manager_macos_legacy.mm`** -> AI Confidence: **99.34%**
508. **`platform/macos/godot_main_macos.mm`** -> AI Confidence: **99.34%**
509. **`platform/macos/godot_menu_delegate.mm`** -> AI Confidence: **99.34%**
510. **`platform/macos/godot_window_delegate.mm`** -> AI Confidence: **99.34%**
511. **`platform/macos/key_mapping_macos.mm`** -> AI Confidence: **99.34%**
512. **`platform/macos/native_menu_macos.mm`** -> AI Confidence: **99.34%**
513. **`thirdparty/freetype/src/autofit/afcjk.c`** -> AI Confidence: **99.34%**
514. **`thirdparty/freetype/src/autofit/aflatin.c`** -> AI Confidence: **99.34%**
515. **`thirdparty/freetype/src/autofit/afloader.c`** -> AI Confidence: **99.34%**
516. **`thirdparty/freetype/src/base/ftstroke.c`** -> AI Confidence: **99.34%**
517. **`thirdparty/freetype/src/bdf/bdflib.c`** -> AI Confidence: **99.34%**
518. **`thirdparty/freetype/src/cid/cidparse.c`** -> AI Confidence: **99.34%**
519. **`thirdparty/freetype/src/pcf/pcfread.c`** -> AI Confidence: **99.34%**
520. **`thirdparty/freetype/src/pfr/pfrgload.c`** -> AI Confidence: **99.34%**
521. **`thirdparty/freetype/src/pfr/pfrsbit.c`** -> AI Confidence: **99.34%**
522. **`thirdparty/freetype/src/psaux/afmparse.c`** -> AI Confidence: **99.34%**
523. **`thirdparty/freetype/src/psaux/psblues.c`** -> AI Confidence: **99.34%**
524. **`thirdparty/freetype/src/psaux/psfont.c`** -> AI Confidence: **99.34%**
525. **`thirdparty/freetype/src/psaux/pshints.c`** -> AI Confidence: **99.34%**
526. **`thirdparty/freetype/src/pshinter/pshalgo.c`** -> AI Confidence: **99.34%**
527. **`thirdparty/freetype/src/pshinter/pshrec.c`** -> AI Confidence: **99.34%**
528. **`thirdparty/freetype/src/raster/ftrend1.c`** -> AI Confidence: **99.34%**
529. **`thirdparty/freetype/src/sfnt/pngshim.c`** -> AI Confidence: **99.34%**
530. **`thirdparty/freetype/src/sfnt/sfwoff.c`** -> AI Confidence: **99.34%**
531. **`thirdparty/freetype/src/sfnt/ttbdf.c`** -> AI Confidence: **99.34%**
532. **`thirdparty/freetype/src/sfnt/ttkern.c`** -> AI Confidence: **99.34%**
533. **`thirdparty/freetype/src/sfnt/ttload.c`** -> AI Confidence: **99.34%**
534. **`thirdparty/freetype/src/sfnt/ttmtx.c`** -> AI Confidence: **99.34%**
535. **`thirdparty/freetype/src/sfnt/ttpost.c`** -> AI Confidence: **99.34%**
536. **`thirdparty/freetype/src/smooth/ftsmooth.c`** -> AI Confidence: **99.34%**
537. **`thirdparty/freetype/src/type1/t1parse.c`** -> AI Confidence: **99.34%**
538. **`thirdparty/freetype/src/type42/t42objs.c`** -> AI Confidence: **99.34%**
539. **`thirdparty/libjpeg-turbo/src/jccolor.c`** -> AI Confidence: **99.34%**
540. **`thirdparty/libjpeg-turbo/src/jchuff.c`** -> AI Confidence: **99.34%**
541. **`thirdparty/libjpeg-turbo/src/jdcolor.c`** -> AI Confidence: **99.34%**
542. **`thirdparty/libjpeg-turbo/src/jddctmgr.c`** -> AI Confidence: **99.34%**
543. **`thirdparty/libjpeg-turbo/src/jdhuff.c`** -> AI Confidence: **99.34%**
544. **`thirdparty/libjpeg-turbo/src/jdmerge.c`** -> AI Confidence: **99.34%**
545. **`thirdparty/libjpeg-turbo/src/jmemmgr.c`** -> AI Confidence: **99.34%**
546. **`thirdparty/libjpeg-turbo/src/transupp.c`** -> AI Confidence: **99.34%**
547. **`thirdparty/libwebp/src/dec/quant_dec.c`** -> AI Confidence: **99.34%**
548. **`thirdparty/libwebp/src/dsp/upsampling_neon.c`** -> AI Confidence: **99.34%**
549. **`thirdparty/libwebp/src/enc/cost_enc.c`** -> AI Confidence: **99.34%**
550. **`thirdparty/libwebp/src/enc/token_enc.c`** -> AI Confidence: **99.34%**
551. **`thirdparty/libwebp/src/utils/bit_writer_utils.c`** -> AI Confidence: **99.34%**
552. **`thirdparty/libwebp/src/utils/filters_utils.c`** -> AI Confidence: **99.34%**
553. **`thirdparty/mbedtls/library/ssl_misc.h`** -> AI Confidence: **99.34%**
554. **`thirdparty/pcre2/deps/sljit/sljit_src/sljitConfigInternal.h`** -> AI Confidence: **99.34%**
555. **`core/doc_data.cpp`** -> AI Confidence: **99.32%**
556. **`core/error/error_list.cpp`** -> AI Confidence: **99.32%**
557. **`core/extension/gdextension_special_compat_hashes.cpp`** -> AI Confidence: **99.32%**
558. **`core/io/plist.cpp`** -> AI Confidence: **99.32%**
559. **`core/io/translation_loader_po.cpp`** -> AI Confidence: **99.32%**
560. **`core/math/delaunay_3d.h`** -> AI Confidence: **99.32%**
561. **`core/math/quick_hull.cpp`** -> AI Confidence: **99.32%**
562. **`core/math/triangle_mesh.cpp`** -> AI Confidence: **99.32%**
563. **`core/object/gdtype.cpp`** -> AI Confidence: **99.32%**
564. **`core/os/keyboard.cpp`** -> AI Confidence: **99.32%**
565. **`drivers/png/png_driver_common.cpp`** -> AI Confidence: **99.32%**
566. **`editor/scene/3d/gizmos/physics/collision_polygon_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.32%**
567. **`modules/camera/buffer_decoder.cpp`** -> AI Confidence: **99.32%**
568. **`modules/gdscript/gdscript_tokenizer_buffer.cpp`** -> AI Confidence: **99.32%**
569. **`modules/godot_physics_2d/godot_body_pair_2d.cpp`** -> AI Confidence: **99.32%**
570. **`modules/mono/utils/naming_utils.cpp`** -> AI Confidence: **99.32%**
571. **`modules/mono/utils/string_utils.cpp`** -> AI Confidence: **99.32%**
572. **`modules/regex/tests/test_regex.h`** -> AI Confidence: **99.32%**
573. **`platform/android/java_class_wrapper.cpp`** -> AI Confidence: **99.32%**
574. **`scene/3d/spline_ik_3d.cpp`** -> AI Confidence: **99.32%**
575. **`scene/gui/check_box.cpp`** -> AI Confidence: **99.32%**
576. **`scene/gui/check_button.cpp`** -> AI Confidence: **99.32%**
577. **`scene/gui/graph_edit_arranger.cpp`** -> AI Confidence: **99.32%**
578. **`scene/resources/2d/polygon_path_finder.cpp`** -> AI Confidence: **99.32%**
579. **`scene/resources/bit_map.cpp`** -> AI Confidence: **99.32%**
580. **`tests/core/input/test_input_event_key.cpp`** -> AI Confidence: **99.32%**
581. **`tests/core/io/test_marshalls.cpp`** -> AI Confidence: **99.32%**
582. **`tests/scene/test_fontfile.cpp`** -> AI Confidence: **99.32%**
583. **`thirdparty/embree/common/tasking/taskscheduler.h`** -> AI Confidence: **99.32%**
584. **`thirdparty/freetype/include/freetype/config/mac-support.h`** -> AI Confidence: **99.32%**
585. **`thirdparty/harfbuzz/src/hb-raster-svg-base.cc`** -> AI Confidence: **99.32%**
586. **`thirdparty/harfbuzz/src/hb-raster-svg-gradient.cc`** -> AI Confidence: **99.32%**
587. **`thirdparty/harfbuzz/src/hb-raster-svg-parse.cc`** -> AI Confidence: **99.32%**
588. **`thirdparty/harfbuzz/src/hb-zlib.cc`** -> AI Confidence: **99.32%**
589. **`thirdparty/icu4c/common/unicode/urename.h`** -> AI Confidence: **99.32%**
590. **`thirdparty/icu4c/common/unicode/utf16.h`** -> AI Confidence: **99.32%**
591. **`thirdparty/icu4c/common/unicode/utf8.h`** -> AI Confidence: **99.32%**
592. **`thirdparty/icu4c/common/unicode/utf_old.h`** -> AI Confidence: **99.32%**
593. **`thirdparty/libktx/lib/uthash.h`** -> AI Confidence: **99.32%**
594. **`thirdparty/linuxbsd_headers/dbus/dbus-syntax.h`** -> AI Confidence: **99.32%**
595. **`thirdparty/manifold/src/smoothing.cpp`** -> AI Confidence: **99.32%**
596. **`thirdparty/openxr/src/external/jsoncpp/include/json/assertions.h`** -> AI Confidence: **99.32%**
597. **`thirdparty/sdl/include/SDL3/SDL_platform_defines.h`** -> AI Confidence: **99.32%**
598. **`drivers/apple_embedded/godot_app_delegate.mm`** -> AI Confidence: **99.32%**
599. **`drivers/apple_embedded/rendering_context_driver_vulkan_apple_embedded.mm`** -> AI Confidence: **99.32%**
600. **`drivers/coremidi/midi_driver_coremidi.mm`** -> AI Confidence: **99.32%**
601. **`platform/macos/rendering_context_driver_vulkan_macos.mm`** -> AI Confidence: **99.32%**
602. **`thirdparty/freetype/src/base/ftcid.c`** -> AI Confidence: **99.32%**
603. **`thirdparty/freetype/src/otvalid/otvgpos.c`** -> AI Confidence: **99.32%**
604. **`thirdparty/freetype/src/otvalid/otvjstf.c`** -> AI Confidence: **99.32%**
605. **`thirdparty/libjpeg-turbo/src/jcapistd.c`** -> AI Confidence: **99.32%**
606. **`thirdparty/libjpeg-turbo/src/jccoefct.c`** -> AI Confidence: **99.32%**
607. **`thirdparty/libjpeg-turbo/src/jcicc.c`** -> AI Confidence: **99.32%**
608. **`thirdparty/libjpeg-turbo/src/jcinit.c`** -> AI Confidence: **99.32%**
609. **`thirdparty/libjpeg-turbo/src/jcmainct.c`** -> AI Confidence: **99.32%**
610. **`thirdparty/libjpeg-turbo/src/jcparam.c`** -> AI Confidence: **99.32%**
611. **`thirdparty/libjpeg-turbo/src/jctrans.c`** -> AI Confidence: **99.32%**
612. **`thirdparty/libjpeg-turbo/src/jdapimin.c`** -> AI Confidence: **99.32%**
613. **`thirdparty/libjpeg-turbo/src/jdicc.c`** -> AI Confidence: **99.32%**
614. **`thirdparty/libjpeg-turbo/src/jdpostct.c`** -> AI Confidence: **99.32%**
615. **`thirdparty/libjpeg-turbo/src/jdtrans.c`** -> AI Confidence: **99.32%**
616. **`thirdparty/libjpeg-turbo/src/jfdctfst.c`** -> AI Confidence: **99.32%**
617. **`thirdparty/libjpeg-turbo/src/jfdctint.c`** -> AI Confidence: **99.32%**
618. **`thirdparty/libjpeg-turbo/src/jidctflt.c`** -> AI Confidence: **99.32%**
619. **`thirdparty/libjpeg-turbo/src/jidctfst.c`** -> AI Confidence: **99.32%**
620. **`thirdparty/libjpeg-turbo/src/jidctint.c`** -> AI Confidence: **99.32%**
621. **`thirdparty/libjpeg-turbo/src/jidctred.c`** -> AI Confidence: **99.32%**
622. **`thirdparty/libjpeg-turbo/src/jquant2.c`** -> AI Confidence: **99.32%**
623. **`thirdparty/libwebp/src/dsp/dec_clip_tables.c`** -> AI Confidence: **99.32%**
624. **`thirdparty/libwebp/src/dsp/lossless_msa.c`** -> AI Confidence: **99.32%**
625. **`thirdparty/libwebp/src/dsp/msa_macro.h`** -> AI Confidence: **99.32%**
626. **`thirdparty/libwebp/src/dsp/neon.h`** -> AI Confidence: **99.32%**
627. **`thirdparty/libwebp/src/dsp/rescaler_mips_dsp_r2.c`** -> AI Confidence: **99.32%**
628. **`thirdparty/mbedtls/library/aesce.h`** -> AI Confidence: **99.32%**
629. **`thirdparty/mbedtls/library/padlock.h`** -> AI Confidence: **99.32%**
630. **`thirdparty/mbedtls/library/pkwrite.h`** -> AI Confidence: **99.32%**
631. **`thirdparty/mbedtls/library/ssl_client.h`** -> AI Confidence: **99.32%**
632. **`thirdparty/pcre2/src/pcre2_internal.h`** -> AI Confidence: **99.32%**
633. **`doc/tools/doc_status.py`** -> AI Confidence: **99.31%**
634. **`misc/scripts/install_d3d12_sdk_windows.py`** -> AI Confidence: **99.31%**
635. **`modules/raycast/godot_update_embree.py`** -> AI Confidence: **99.31%**
636. **`platform/android/detect.py`** -> AI Confidence: **99.31%**
637. **`platform/ios/detect.py`** -> AI Confidence: **99.31%**
638. **`platform/macos/detect.py`** -> AI Confidence: **99.31%**
639. **`platform/visionos/detect.py`** -> AI Confidence: **99.31%**
640. **`platform/web/detect.py`** -> AI Confidence: **99.31%**
641. **`core/crypto/crypto_core.cpp`** -> AI Confidence: **99.31%**
642. **`core/debugger/remote_debugger_peer.cpp`** -> AI Confidence: **99.31%**
643. **`core/extension/gdextension.cpp`** -> AI Confidence: **99.31%**
644. **`core/extension/godot_instance.cpp`** -> AI Confidence: **99.31%**
645. **`core/input/input.cpp`** -> AI Confidence: **99.31%**
646. **`core/input/input_event.cpp`** -> AI Confidence: **99.31%**
647. **`core/io/file_access.cpp`** -> AI Confidence: **99.31%**
648. **`core/io/resource_importer.cpp`** -> AI Confidence: **99.31%**
649. **`core/io/resource_loader.cpp`** -> AI Confidence: **99.31%**
650. **`core/io/resource_uid.cpp`** -> AI Confidence: **99.31%**
651. **`core/math/convex_hull.cpp`** -> AI Confidence: **99.31%**
652. **`core/math/projection.cpp`** -> AI Confidence: **99.31%**
653. **`core/object/worker_thread_pool.cpp`** -> AI Confidence: **99.31%**
654. **`core/register_core_types.cpp`** -> AI Confidence: **99.31%**
655. **`core/variant/array.cpp`** -> AI Confidence: **99.31%**
656. **`core/variant/callable.cpp`** -> AI Confidence: **99.31%**
657. **`drivers/alsa/audio_driver_alsa.cpp`** -> AI Confidence: **99.31%**
658. **`drivers/d3d12/rendering_shader_container_d3d12.cpp`** -> AI Confidence: **99.31%**
659. **`drivers/egl/egl_manager.cpp`** -> AI Confidence: **99.31%**
660. **`drivers/gles3/storage/light_storage.cpp`** -> AI Confidence: **99.31%**
661. **`drivers/gles3/storage/particles_storage.cpp`** -> AI Confidence: **99.31%**
662. **`drivers/gles3/storage/utilities.cpp`** -> AI Confidence: **99.31%**
663. **`drivers/metal/metal_objects_shared.cpp`** -> AI Confidence: **99.31%**
664. **`drivers/metal/rendering_device_driver_metal.cpp`** -> AI Confidence: **99.31%**
665. **`drivers/unix/dir_access_unix.cpp`** -> AI Confidence: **99.31%**
666. **`drivers/unix/file_access_unix.cpp`** -> AI Confidence: **99.31%**
667. **`drivers/unix/file_access_unix_pipe.cpp`** -> AI Confidence: **99.31%**
668. **`drivers/unix/ip_unix.cpp`** -> AI Confidence: **99.31%**
669. **`drivers/unix/net_socket_unix.cpp`** -> AI Confidence: **99.31%**
670. **`drivers/unix/os_unix.cpp`** -> AI Confidence: **99.31%**
671. **`drivers/windows/dir_access_windows.cpp`** -> AI Confidence: **99.31%**
672. **`editor/animation/animation_track_editor_plugins.cpp`** -> AI Confidence: **99.31%**
673. **`editor/animation/animation_tree_editor_plugin.cpp`** -> AI Confidence: **99.31%**
674. **`editor/audio/audio_stream_editor_plugin.cpp`** -> AI Confidence: **99.31%**
675. **`editor/debugger/debug_adapter/debug_adapter_parser.cpp`** -> AI Confidence: **99.31%**
676. **`editor/debugger/editor_debugger_inspector.cpp`** -> AI Confidence: **99.31%**
677. **`editor/debugger/editor_expression_evaluator.cpp`** -> AI Confidence: **99.31%**
678. **`editor/debugger/editor_performance_profiler.cpp`** -> AI Confidence: **99.31%**
679. **`editor/debugger/script_editor_debugger.cpp`** -> AI Confidence: **99.31%**
680. **`editor/docks/dock_tab_container.cpp`** -> AI Confidence: **99.31%**
681. **`editor/docks/groups_editor.cpp`** -> AI Confidence: **99.31%**
682. **`editor/editor_data.cpp`** -> AI Confidence: **99.31%**
683. **`editor/editor_interface.cpp`** -> AI Confidence: **99.31%**
684. **`editor/editor_main_screen.cpp`** -> AI Confidence: **99.31%**
685. **`editor/editor_undo_redo_manager.cpp`** -> AI Confidence: **99.31%**
686. **`editor/export/editor_export_platform_pc.cpp`** -> AI Confidence: **99.31%**
687. **`editor/export/editor_export_preset.cpp`** -> AI Confidence: **99.31%**
688. **`editor/export/project_export.cpp`** -> AI Confidence: **99.31%**
689. **`editor/file_system/editor_paths.cpp`** -> AI Confidence: **99.31%**
690. **`editor/gui/directory_create_dialog.cpp`** -> AI Confidence: **99.31%**
691. **`editor/gui/editor_bottom_panel.cpp`** -> AI Confidence: **99.31%**
692. **`editor/gui/editor_zoom_widget.cpp`** -> AI Confidence: **99.31%**
693. **`editor/gui/progress_dialog.cpp`** -> AI Confidence: **99.31%**
694. **`editor/gui/window_wrapper.cpp`** -> AI Confidence: **99.31%**
695. **`editor/import/fbx_importer_manager.cpp`** -> AI Confidence: **99.31%**
696. **`editor/import/import_defaults_editor.cpp`** -> AI Confidence: **99.31%**
697. **`editor/inspector/editor_properties.cpp`** -> AI Confidence: **99.31%**
698. **`editor/inspector/editor_resource_preview.cpp`** -> AI Confidence: **99.31%**
699. **`editor/inspector/editor_resource_tooltip_plugins.cpp`** -> AI Confidence: **99.31%**
700. **`editor/inspector/editor_sectioned_inspector.cpp`** -> AI Confidence: **99.31%**
701. **`editor/run/editor_run_bar.cpp`** -> AI Confidence: **99.31%**
702. **`editor/run/editor_run_native.cpp`** -> AI Confidence: **99.31%**
703. **`editor/run/game_view_plugin.cpp`** -> AI Confidence: **99.31%**
704. **`editor/scene/2d/physics/cast_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
705. **`editor/scene/2d/skeleton_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
706. **`editor/scene/2d/tiles/tile_set_scenes_collection_source_editor.cpp`** -> AI Confidence: **99.31%**
707. **`editor/scene/2d/tiles/tiles_editor_plugin.cpp`** -> AI Confidence: **99.31%**
708. **`editor/scene/3d/gizmos/physics/collision_shape_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
709. **`editor/scene/3d/gizmos/reflection_probe_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
710. **`editor/scene/3d/gizmos/spring_bone_3d_gizmo_plugin.cpp`** -> AI Confidence: **99.31%**
711. **`editor/scene/3d/gpu_particles_collision_sdf_editor_plugin.cpp`** -> AI Confidence: **99.31%**
712. **`editor/scene/3d/multimesh_editor_plugin.cpp`** -> AI Confidence: **99.31%**
713. **`editor/scene/3d/node_3d_editor_gizmos.cpp`** -> AI Confidence: **99.31%**
714. **`editor/scene/3d/root_motion_editor_plugin.cpp`** -> AI Confidence: **99.31%**
715. **`editor/scene/3d/voxel_gi_editor_plugin.cpp`** -> AI Confidence: **99.31%**
716. **`editor/scene/connections_dialog.cpp`** -> AI Confidence: **99.31%**
717. **`editor/scene/group_settings_editor.cpp`** -> AI Confidence: **99.31%**
718. **`editor/scene/gui/font_config_plugin.cpp`** -> AI Confidence: **99.31%**
719. **`editor/scene/gui/theme_editor_preview.cpp`** -> AI Confidence: **99.31%**
720. **`editor/scene/material_editor_plugin.cpp`** -> AI Confidence: **99.31%**
721. **`editor/scene/particles_editor_plugin.cpp`** -> AI Confidence: **99.31%**
722. **`editor/scene/resource_preloader_editor_plugin.cpp`** -> AI Confidence: **99.31%**
723. **`editor/scene/texture/bit_map_editor_plugin.cpp`** -> AI Confidence: **99.31%**
724. **`editor/scene/texture/color_channel_selector.cpp`** -> AI Confidence: **99.31%**
725. **`editor/scene/texture/texture_editor_plugin.cpp`** -> AI Confidence: **99.31%**
726. **`editor/scene/texture/texture_layered_editor_plugin.cpp`** -> AI Confidence: **99.31%**
727. **`editor/script/find_in_files.cpp`** -> AI Confidence: **99.31%**
728. **`editor/script/script_editor_base.cpp`** -> AI Confidence: **99.31%**
729. **`editor/settings/editor_feature_profile.cpp`** -> AI Confidence: **99.31%**
730. **`editor/settings/project_settings_editor.cpp`** -> AI Confidence: **99.31%**
731. **`editor/shader/editor_native_shader_source_visualizer.cpp`** -> AI Confidence: **99.31%**
732. **`editor/themes/editor_icons.cpp`** -> AI Confidence: **99.31%**
733. **`editor/translations/localization_editor.cpp`** -> AI Confidence: **99.31%**
734. **`editor/version_control/version_control_editor_plugin.cpp`** -> AI Confidence: **99.31%**
735. **`main/performance.cpp`** -> AI Confidence: **99.31%**
736. **`modules/camera/camera_linux.cpp`** -> AI Confidence: **99.31%**
737. **`modules/csg/csg_shape.cpp`** -> AI Confidence: **99.31%**
738. **`modules/fbx/editor/editor_scene_importer_fbx2gltf.cpp`** -> AI Confidence: **99.31%**
739. **`modules/gdscript/gdscript_cache.cpp`** -> AI Confidence: **99.31%**
740. **`modules/gdscript/gdscript_editor.cpp`** -> AI Confidence: **99.31%**
741. **`modules/gdscript/gdscript_utility_functions.cpp`** -> AI Confidence: **99.31%**
742. **`modules/gdscript/language_server/gdscript_language_protocol.cpp`** -> AI Confidence: **99.31%**
743. **`modules/gdscript/tests/gdscript_test_runner_suite.h`** -> AI Confidence: **99.31%**
744. **`modules/glslang/register_types.cpp`** -> AI Confidence: **99.31%**
745. **`modules/gltf/tests/test_gltf_images.h`** -> AI Confidence: **99.31%**
746. **`modules/jolt_physics/joints/jolt_hinge_joint_3d.cpp`** -> AI Confidence: **99.31%**
747. **`modules/jolt_physics/objects/jolt_area_3d.cpp`** -> AI Confidence: **99.31%**
748. **`modules/jolt_physics/objects/jolt_body_3d.cpp`** -> AI Confidence: **99.31%**
749. **`modules/jolt_physics/objects/jolt_shaped_object_3d.cpp`** -> AI Confidence: **99.31%**
750. **`modules/jolt_physics/objects/jolt_soft_body_3d.cpp`** -> AI Confidence: **99.31%**
751. **`modules/jolt_physics/shapes/jolt_shape_3d.cpp`** -> AI Confidence: **99.31%**
752. **`modules/jolt_physics/spaces/jolt_motion_filter_3d.cpp`** -> AI Confidence: **99.31%**
753. **`modules/jolt_physics/spaces/jolt_space_3d.cpp`** -> AI Confidence: **99.31%**
754. **`modules/mbedtls/crypto_mbedtls.cpp`** -> AI Confidence: **99.31%**
755. **`modules/mono/csharp_script.cpp`** -> AI Confidence: **99.31%**
756. **`modules/mono/editor/hostfxr_resolver.cpp`** -> AI Confidence: **99.31%**
757. **`modules/mono/godotsharp_dirs.cpp`** -> AI Confidence: **99.31%**
758. **`modules/mono/utils/path_utils.cpp`** -> AI Confidence: **99.31%**
759. **`modules/multiplayer/editor/editor_network_profiler.cpp`** -> AI Confidence: **99.31%**
760. **`modules/multiplayer/editor/multiplayer_editor_plugin.cpp`** -> AI Confidence: **99.31%**
761. **`modules/multiplayer/editor/replication_editor.cpp`** -> AI Confidence: **99.31%**
762. **`modules/multiplayer/register_types.cpp`** -> AI Confidence: **99.31%**
763. **`modules/multiplayer/tests/test_scene_multiplayer.h`** -> AI Confidence: **99.31%**
764. **`modules/navigation_2d/editor/navigation_link_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
765. **`modules/navigation_2d/editor/navigation_region_2d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
766. **`modules/navigation_2d/nav_map_2d.cpp`** -> AI Confidence: **99.31%**
767. **`modules/navigation_3d/editor/navigation_region_3d_editor_plugin.cpp`** -> AI Confidence: **99.31%**
768. **`modules/navigation_3d/nav_map_3d.cpp`** -> AI Confidence: **99.31%**
769. **`modules/navigation_3d/register_types.cpp`** -> AI Confidence: **99.31%**
770. **`modules/noise/editor/noise_editor_plugin.cpp`** -> AI Confidence: **99.31%**
771. **`modules/noise/register_types.cpp`** -> AI Confidence: **99.31%**
772. **`modules/objectdb_profiler/editor/objectdb_profiler_panel.cpp`** -> AI Confidence: **99.31%**
773. **`modules/objectdb_profiler/snapshot_collector.cpp`** -> AI Confidence: **99.31%**
774. **`modules/openxr/editor/openxr_action_map_editor.cpp`** -> AI Confidence: **99.31%**
775. **`modules/openxr/editor/openxr_editor_plugin.cpp`** -> AI Confidence: **99.31%**
776. **`modules/openxr/editor/openxr_select_action_dialog.cpp`** -> AI Confidence: **99.31%**
777. **`modules/openxr/editor/openxr_select_runtime.cpp`** -> AI Confidence: **99.31%**
778. **`modules/openxr/extensions/openxr_android_thread_settings_extension.cpp`** -> AI Confidence: **99.31%**
779. **`modules/openxr/extensions/spatial_entities/openxr_spatial_anchor.cpp`** -> AI Confidence: **99.31%**
780. **`modules/openxr/extensions/spatial_entities/openxr_spatial_plane_tracking.cpp`** -> AI Confidence: **99.31%**
781. **`modules/openxr/openxr_api.cpp`** -> AI Confidence: **99.31%**
782. **`modules/openxr/scene/openxr_render_model_manager.cpp`** -> AI Confidence: **99.31%**
783. **`modules/raycast/raycast_occlusion_cull.cpp`** -> AI Confidence: **99.31%**
784. **`modules/websocket/register_types.cpp`** -> AI Confidence: **99.31%**
785. **`modules/webxr/webxr_interface_js.cpp`** -> AI Confidence: **99.31%**
786. **`platform/android/export/android_editor_gradle_runner.cpp`** -> AI Confidence: **99.31%**
787. **`platform/android/export/gradle_export_util.cpp`** -> AI Confidence: **99.31%**
788. **`platform/android/java_godot_lib_jni.cpp`** -> AI Confidence: **99.31%**
789. **`platform/android/os_android.cpp`** -> AI Confidence: **99.31%**
790. **`platform/linuxbsd/export/export_plugin.cpp`** -> AI Confidence: **99.31%**
791. **`platform/linuxbsd/wayland/display_server_wayland.cpp`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `thirdparty/mbedtls/library/pk_internal.h` -> **100.0%** Exposure
- `thirdparty/icu4c/common/unicode/uloc.h` -> **99.8781%** Exposure
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/X509CertificateUtils.java` -> **99.7922%** Exposure
- `platform/android/java/lib/src/main/java/org/godotengine/godot/utils/GodotNetUtils.java` -> **99.7922%** Exposure
- `platform/macos/os_macos.mm` -> **37.2458%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `68` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `32274` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `thirdparty/libwebp/src/utils/thread_utils.c` (C) -> Cumulative Risk: **699.91**
- **Archetype:** `file_cluster_4` (Distance: 12.637 IQR)
- **Magnitude:** 250.28 | **LOC:** 371 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `pthread_cond_wait` (Impact: 48.3), `Reset` (Impact: 14.9), `WebPSetWorkerInterface` (Impact: 8.5)

### 2. `thirdparty/glslang/glslang/MachineIndependent/reflection.h` (CPP) -> Cumulative Risk: **689.16**
- **Archetype:** `file_cluster_9` (Distance: 17.416 IQR)
- **Magnitude:** 178.52 | **LOC:** 227 | **CtrlFlow:** 39.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9981%), Safety Score (94.8425%)
- **Heaviest Functions:** `getPipeIOIndex` (Impact: 9.1), `getUniformBlock` (Impact: 7.3), `getPipeOutput` (Impact: 7.3)

### 3. `core/variant/variant_op.h` (CPP) -> Cumulative Risk: **679.4**
- **Archetype:** `file_cluster_8` (Distance: 13.985 IQR)
- **Magnitude:** 1418.26 | **LOC:** 1290 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.6619%)
- **Heaviest Functions:** `evaluate` (Impact: 11.9), `evaluate` (Impact: 11.9), `evaluate` (Impact: 11.7)

### 4. `core/math/bvh_split.inc` (CPP) -> Cumulative Risk: **677.34**
- **Archetype:** `file_cluster_0` (Distance: 15.993 IQR)
- **Magnitude:** 382.34 | **LOC:** 299 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9756%), Documentation (99.9705%)
- **Heaviest Functions:** `_split_leaf_sort_groups_simple` (Impact: 72.6), `_split_inform_references` (Impact: 2.6), `constexpr` (Impact: 2.5)

### 5. `platform/web/js/engine/preloader.js` (JAVASCRIPT) -> Cumulative Risk: **673.9**
- **Archetype:** `file_cluster_4` (Distance: 12.344 IQR)
- **Magnitude:** 223.78 | **LOC:** 134 | **CtrlFlow:** 52.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (99.9955%), State Flux (99.9857%)
- **Heaviest Functions:** `Preloader` (Impact: 51.7), `preload` (Impact: 19.2), `animateProgress` (Impact: 17.1)

### 6. `thirdparty/embree/common/math/math_sycl.h` (CPP) -> Cumulative Risk: **671.7**
- **Archetype:** `file_cluster_13` (Distance: 15.021 IQR)
- **Magnitude:** 361.64 | **LOC:** 280 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (98.0454%)
- **Heaviest Functions:** `sign` (Impact: 5.3), `select` (Impact: 4.0), `select` (Impact: 4.0)

### 7. `thirdparty/glslang/glslang/Include/arrays.h` (CPP) -> Cumulative Risk: **669.85**
- **Archetype:** `file_cluster_9` (Distance: 13.67 IQR)
- **Magnitude:** 341.92 | **LOC:** 374 | **CtrlFlow:** 36.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (99.564%)
- **Heaviest Functions:** `sameInnerArrayness` (Impact: 10.7), `operator==` (Impact: 10.4), `operator==` (Impact: 8.4)

### 8. `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/Utils/SemaphoreExtensions.cs` (CSHARP) -> Cumulative Risk: **668.53**
- **Archetype:** `file_cluster_4` (Distance: 11.926 IQR)
- **Magnitude:** 51.66 | **LOC:** 33 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `SemaphoreSlimWaitReleaseWrapper` (Impact: 4.2), `UseAsync` (Impact: 3.7), `Dispose` (Impact: 2.2)

### 9. `editor/editor_node.cpp` (CPP) -> Cumulative Risk: **666.89**
- **Archetype:** `file_cluster_13` (Distance: 13.589 IQR)
- **Magnitude:** 1689.7 | **LOC:** 9612 | **CtrlFlow:** 87.7% | **Authorship Centralization:** 32.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Tech Debt (99.999%), State Flux (99.9238%)
- **Heaviest Functions:** `_plugin_over_edit` (Impact: 427.4), `EditorNode::shortcut_input` (Impact: 76.8), `EditorNode::_find_and_save_edited_subres` (Impact: 36.3)

### 10. `thirdparty/libwebp/src/dec/webp_dec.c` (C) -> Cumulative Risk: **666.29**
- **Archetype:** `file_cluster_13` (Distance: 14.028 IQR)
- **Magnitude:** 608.66 | **LOC:** 932 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (91.5405%)
- **Heaviest Functions:** `ParseOptionalChunks` (Impact: 163.7), `WebPValidateDecoderConfig` (Impact: 22.5), `WebPCheckCropDimensions` (Impact: 18.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `thirdparty/embree/common/math/vec3fa.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 98.79%)
- **Global Archetype:** `file_cluster_7` (Drift: 16.939 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_7: 16.939, file_cluster_8: 17.01, file_cluster_13: 17.044
- **Magnitude:** 11579.83 | **LOC:** 792 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.728%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 245`, `args: 220`, `func_start: 225`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 741`, `dead_code: 1`
* *Architecture:* `import: 3`
* *Defense:* `safety: 4`, `doc: 1590`, `immutability_locks: 394`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.085
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` emath.h, sse.h, vec3fa_sycl.h, alloc.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scene/gui/rich_text_label.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.981 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.346 IQR)
- **Top Global Matches:** file_cluster_8: 15.981, file_cluster_13: 16.244, file_cluster_7: 16.315
- **Magnitude:** 10445.7 | **LOC:** 8433 | **CtrlFlow:** 84.4% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (94.7634%), Tech Debt (93.3032%)
**Top Internal Functions/Classes:**
  * `RichTextLabel::_draw_line` (Impact: 1058.9)
  * `RichTextLabel::_add_list_prefixes` (Impact: 936.1)
  * `RichTextLabel::_find_click_in_line` (Impact: 396.5)
  * `RichTextLabel::gui_input` (Impact: 256.1)
  * `RichTextLabel::_notification` (Impact: 203.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1388`, `structural_boundaries: 257`, `args: 413`, `func_start: 149`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5982`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 138`
* *Architecture:* `import: 25`
* *Defense:* `doc: 4`, `sync_locks: 23`, `immutability_locks: 140`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` scene_tree.h, regex.h, texture.h, scroll_bar.h, accessibility_server.h, timer.h, display_server.h, text_paragraph.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/embree/common/math/emath.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.31 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 6.052 IQR)
- **Top Global Matches:** file_cluster_8: 14.31, file_cluster_13: 14.423, file_cluster_16: 14.475
- **Magnitude:** 10041.24 | **LOC:** 469 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.9476%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 224`, `args: 146`, `func_start: 146`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 383`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.666
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` xmmintrin.h, immintrin.h, constants.h, emmintrin.h, emulation.h, intrinsics.h, platform.h, math_sycl.h...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `servers/rendering/shader_language.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.827 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.499 IQR)
- **Top Global Matches:** file_cluster_8: 14.827, file_cluster_13: 15.15, file_cluster_7: 15.183
- **Magnitude:** 9315.96 | **LOC:** 12235 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 37.5%
- **Risk Profile:** Cognitive Load (96.9059%), Tech Debt (24.9881%)
**Top Internal Functions/Classes:**
  * `ShaderLanguage::_validate_operator` (Impact: 2391.1)
  * `ShaderLanguage::_parse_block` (Impact: 872.2)
  * `ShaderLanguage::_get_token` (Impact: 340.7)
  * `ShaderLanguage::_find_identifier` (Impact: 231.2)
    * *Intent:* #endif // DEBUG_ENABLED
  * `ShaderLanguage::_parse_shader` (Impact: 217.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2086`, `structural_boundaries: 411`, `args: 241`, `func_start: 50`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 2`, `state_mutation: 4396`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `orphaned_logic: 44`
* *Architecture:* `import: 9`
* *Defense:* `doc: 4`, `immutability_locks: 106`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` os.h, rendering_server_globals.h, renderer_compositor.h, rb_set.h, shader_types.h, rendering_server.h, engine.h, shader_language.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platform/linuxbsd/x11/display_server_x11.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.575 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.613 IQR)
- **Top Global Matches:** file_cluster_8: 15.575, file_cluster_13: 15.736, file_cluster_11: 15.793
- **Magnitude:** 8046.02 | **LOC:** 7571 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 38.5%
- **Risk Profile:** Cognitive Load (93.0767%), Tech Debt (92.7734%)
**Top Internal Functions/Classes:**
  * `DisplayServerX11::DisplayServerX11` (Impact: 596.8)
  * `DisplayServerX11::_handle_key_event` (Impact: 216.2)
  * `DisplayServerX11::_create_window` (Impact: 132.4)
  * `DisplayServerX11::_validate_fullscreen_o` (Impact: 119.9)
  * `DisplayServerX11::_clipboard_transfer_ow` (Impact: 93.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1251`, `structural_boundaries: 305`, `args: 223`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 14`, `state_mutation: 4987`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 145`
* *Architecture:* `import: 43`
* *Defense:* `safety: 5`, `doc: 4`, `immutability_locks: 181`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` XKBlib.h, cstdlib, project_settings.h, dbus-so_wrap.h, file_access.h, rendering_context_driver_vulkan_x11.h, dbus.h, rasterizer_dummy.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scene/resources/visual_shader_nodes.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.909 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.936 IQR)
- **Top Global Matches:** file_cluster_8: 13.909, file_cluster_7: 14.194, file_cluster_13: 14.378
- **Magnitude:** 7932.84 | **LOC:** 8589 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (57.1276%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `VisualShaderNodeTexture::generate_code` (Impact: 153.6)
  * `get_sampler_hint` (Impact: 151.2)
    * *Intent:* //////////////
  * `VisualShaderNodeVectorOp::generate_code` (Impact: 87.2)
  * `VisualShaderNodeColorOp::generate_code` (Impact: 85.6)
  * `VisualShaderNodeIntOp::generate_code` (Impact: 76.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1574`, `structural_boundaries: 1332`, `args: 1218`, `func_start: 1039`
* *Risk/State:* `state_mutation: 2805`, `fragile_debt: 3`, `duplicate_logic: 452`, `orphaned_logic: 586`
* *Architecture:* `import: 5`
* *Defense:* `doc: 324`, `immutability_locks: 982`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` os.h, visual_shader_nodes.h, visual_shader_nodes.compat.inc, rendering_server.h, class_db.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/tinyexr/tinyexr.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 16.127 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.951 IQR)
- **Top Global Matches:** file_cluster_11: 16.127, file_cluster_8: 16.267, file_cluster_4: 16.273
- **Magnitude:** 7352.62 | **LOC:** 9401 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.1%), Tech Debt (19.639%)
**Top Internal Functions/Classes:**
  * `DecodePixelData` (Impact: 1649.2)
  * `LoadEXRWithLayer` (Impact: 152.6)
    * *Intent:* // For ZFP_COMPRESSION: // pixel sample data for channel 0 for scanline 0 // pixel sample data for c...
  * `DecodeEXRImage` (Impact: 147.1)
    * *Intent:* #endif
  * `LoadEXRFromMemory` (Impact: 132.0)
  * `isValidTile` (Impact: 76.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 807`, `structural_boundaries: 323`, `args: 220`, `func_start: 92`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 41`, `state_mutation: 3869`, `dead_code: 38`, `planned_debt: 11`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 36`, `import: 5`
* *Defense:* `safety: 6`, `doc: 56`, `immutability_locks: 294`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.054
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` zfp.h, fcntl.h, thread, cstdlib, string, stdint.h, mman.h, cstdio...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `drivers/vulkan/rendering_device_driver_vulkan.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.789 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.165 IQR)
- **Top Global Matches:** file_cluster_8: 15.789, file_cluster_13: 15.995, file_cluster_11: 16.035
- **Magnitude:** 7002.58 | **LOC:** 7438 | **CtrlFlow:** 79.2% | **Authorship Centralization:** 26.7%
- **Risk Profile:** Cognitive Load (78.4149%), Tech Debt (99.7961%)
**Top Internal Functions/Classes:**
  * `RenderingDeviceDriverVulkan::swap_chain_` (Impact: 515.2)
  * `RenderingDeviceDriverVulkan::_add_queue_` (Impact: 296.9)
  * `RenderingDeviceDriverVulkan::_descriptor` (Impact: 208.1)
  * `RenderingDeviceDriverVulkan::shader_crea` (Impact: 198.8)
  * `RenderingDeviceDriverVulkan::render_pipe` (Impact: 188.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 691`, `structural_boundaries: 182`, `args: 471`, `func_start: 119`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 9`, `state_mutation: 4416`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 5`, `duplicate_logic: 70`, `orphaned_logic: 44`
* *Architecture:* `import: 12`
* *Defense:* `safety: 136`, `doc: 65`, `sync_locks: 16`, `immutability_locks: 268`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` os.h, rendering_device_driver_vulkan.h, swappyVk.h, project_settings.h, thread_jandroid.h, file_access.h, java_godot_wrapper.h, smolv.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/text_server_adv/text_server_adv.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.574 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.788 IQR)
- **Top Global Matches:** file_cluster_8: 15.574, file_cluster_13: 15.823, file_cluster_7: 15.895
- **Magnitude:** 6990.2 | **LOC:** 8441 | **CtrlFlow:** 80.4% | **Authorship Centralization:** 72.2%
- **Risk Profile:** Cognitive Load (93.771%), Tech Debt (93.9197%)
**Top Internal Functions/Classes:**
  * `TextServerAdvanced::_shape_run` (Impact: 581.8)
  * `TextServerAdvanced::_is_valid_identifier` (Impact: 311.6)
  * `TextServerAdvanced::_shaped_text_overrun` (Impact: 243.0)
  * `TextServerAdvanced::_shaped_text_update_` (Impact: 188.8)
  * `TextServerAdvanced::_shaped_text_shape` (Impact: 168.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1094`, `structural_boundaries: 266`, `args: 201`, `func_start: 163`
* *Risk/State:* `safety_bypasses: 15`, `high_risk_execution: 2`, `state_mutation: 4090`, `duplicate_logic: 22`, `orphaned_logic: 121`
* *Architecture:* `import: 18`
* *Defense:* `doc: 9`, `sync_locks: 196`, `immutability_locks: 295`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` os.h, icudata.gen.h, ShapeDistanceFinder.h, project_settings.h, image_texture.h, file_access.h, EdgeHolder.h, msdfgen.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `core/string/ustring.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.2 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.936 IQR)
- **Top Global Matches:** file_cluster_8: 15.2, file_cluster_13: 15.436, file_cluster_11: 15.44
- **Magnitude:** 6783.38 | **LOC:** 5832 | **CtrlFlow:** 70.5% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (77.7297%), Tech Debt (99.9973%)
**Top Internal Functions/Classes:**
  * `_xml_unescape` (Impact: 153.7)
  * `built_in_strtod` (Impact: 81.6)
  * `String::to_int` (Impact: 63.1)
  * `String::parse_url` (Impact: 60.4)
  * `_replace_common` (Impact: 52.5)
    * *Intent:* // Copy rest, skipping `char`.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1164`, `structural_boundaries: 488`, `args: 233`, `func_start: 210`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 15`, `state_mutation: 4353`, `dead_code: 6`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 76`, `orphaned_logic: 120`
* *Architecture:* `import: 15`
* *Defense:* `doc: 8`, `immutability_locks: 455`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` color.h, ucaps.h, os.h, ip_address.h, version_generated.gen.h, grisu2.h, variant.h, object.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `editor/scene/canvas_item_editor_plugin.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.791 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.365 IQR)
- **Top Global Matches:** file_cluster_8: 15.791, file_cluster_13: 15.96, file_cluster_11: 16.128
- **Magnitude:** 6491.12 | **LOC:** 6815 | **CtrlFlow:** 87.9% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (94.231%), Tech Debt (82.1083%)
**Top Internal Functions/Classes:**
  * `CanvasItemEditor::_draw_selection` (Impact: 431.5)
  * `CanvasItemEditor::_gui_input_move` (Impact: 186.7)
  * `CanvasItemEditor::_gui_input_resize` (Impact: 162.6)
  * `CanvasItemEditor::_draw_control_helpers` (Impact: 150.7)
  * `CanvasItemEditor::_gui_input_scale` (Impact: 148.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1096`, `structural_boundaries: 151`, `args: 443`, `func_start: 80`, `class_start: 1`
* *Risk/State:* `state_mutation: 3666`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 75`
* *Architecture:* `api: 1`, `import: 48`
* *Defense:* `doc: 4`, `sync_locks: 4`, `immutability_locks: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 48):` canvas_item_editor_plugin.h, editor_node.h, grid_container.h, editor_string_names.h, separator.h, project_settings.h, editor_run_bar.h, editor_scale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/basis_universal/encoder/basisu_enc.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.242 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.477 IQR)
- **Top Global Matches:** file_cluster_8: 15.242, file_cluster_11: 15.393, file_cluster_13: 15.394
- **Magnitude:** 5944.28 | **LOC:** 4319 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.8962%), Tech Debt (99.9993%)
**Top Internal Functions/Classes:**
  * `color_distance` (Impact: 759.1)
  * `generate_hierarchical_codebook_threaded_` (Impact: 78.5)
  * `generate_hierarchical_codebook_threaded` (Impact: 63.8)
  * `string_split_path` (Impact: 61.7)
  * `radix_sort` (Impact: 59.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 696`, `args: 186`, `func_start: 238`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 3921`, `planned_debt: 3`, `duplicate_logic: 109`
* *Architecture:* `api: 85`, `concurrency: 24`, `import: 12`
* *Defense:* `safety: 57`, `sync_locks: 2`, `immutability_locks: 369`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.439
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` unordered_map, ostream, thread, basisu.h, condition_variable, basisu_math.h, basisu_transcoder_internal.h, map...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scene/resources/animation.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.908 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.183 IQR)
- **Top Global Matches:** file_cluster_8: 14.908, file_cluster_13: 15.269, file_cluster_11: 15.277
- **Magnitude:** 5815.4 | **LOC:** 6559 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (94.0802%), Tech Debt (95.8685%)
**Top Internal Functions/Classes:**
  * `Animation::_set` (Impact: 526.7)
    * *Intent:* /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF */ /* MERCHANTABILITY, FITNESS...
  * `Animation::cubic_interpolate_in_time_var` (Impact: 262.3)
  * `Animation::compress` (Impact: 182.7)
  * `Animation::_interpolate` (Impact: 176.8)
  * `Animation::interpolate_variant` (Impact: 159.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 257`, `args: 244`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3169`, `dead_code: 2`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 78`
* *Architecture:* `import: 4`
* *Defense:* `doc: 4`, `immutability_locks: 241`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` animation.compat.inc, marshalls.h, class_db.h, animation.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/pcre2/src/pcre2_compile.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.728 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.379 IQR)
- **Top Global Matches:** file_cluster_8: 14.728, file_cluster_7: 14.976, file_cluster_11: 14.978
- **Magnitude:** 5605.02 | **LOC:** 11344 | **CtrlFlow:** 94.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.6249%), Tech Debt (7.8908%)
**Top Internal Functions/Classes:**
  * `find_recurse` (Impact: 428.1)
    * *Intent:* /* Not a numerical recursion. Perl allows spaces and tabs after { and before } but not for other del...
  * `show_parsed` (Impact: 212.2)
    * *Intent:* /* We also need a table of characters that may follow \c in an EBCDIC environment for characters 0-3...
  * `get_branchlength` (Impact: 176.7)
  * `set_lookbehind_lengths` (Impact: 172.3)
  * `check_posix_syntax` (Impact: 120.3)
    * *Intent:* /* Now process the quantifier for real. We know it must be {n} or {n,} or {,m}
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1569`, `structural_boundaries: 92`, `args: 2`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 3360`, `orphaned_logic: 1`
* *Architecture:* `api: 687`, `import: 2`
* *Defense:* `doc: 18`, `immutability_locks: 17`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` pcre2_printint_inc.h, pcre2_compile.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platform/android/java/editor/src/main/assets/keystores/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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
- **Global Archetype:** `file_cluster_8` (Drift: 13.612 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.242 IQR)
- **Top Global Matches:** file_cluster_8: 13.612, file_cluster_13: 14.091, file_cluster_7: 14.136
- **Magnitude:** 4926.47 | **LOC:** 664 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (53.941%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 31`, `args: 39`, `func_start: 22`
* *Risk/State:* `state_mutation: 682`, `dead_code: 1`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ustring.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `servers/rendering/renderer_rd/storage_rd/texture_storage.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.199 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.945 IQR)
- **Top Global Matches:** file_cluster_8: 15.199, file_cluster_7: 15.481, file_cluster_13: 15.51
- **Magnitude:** 4920.26 | **LOC:** 4956 | **CtrlFlow:** 80.6% | **Authorship Centralization:** 45.5%
- **Risk Profile:** Cognitive Load (77.8689%), Tech Debt (99.6282%)
**Top Internal Functions/Classes:**
  * `TextureStorage::_validate_texture_format` (Impact: 311.8)
  * `TextureStorage::texture_create_from_nati` (Impact: 288.9)
  * `TextureStorage::_texture_format_from_rd` (Impact: 206.6)
  * `TextureStorage::update_decal_buffer` (Impact: 53.8)
    * *Intent:* // The texture supports sRGB override, create it for 3D usage.
  * `TextureStorage::texture_drawable_initial` (Impact: 49.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 610`, `structural_boundaries: 147`, `args: 212`, `func_start: 120`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 3320`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 19`, `orphaned_logic: 100`
* *Architecture:* `import: 8`
* *Defense:* `doc: 54`, `immutability_locks: 61`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` uniform_set_cache_rd.h, texture_storage.h, rendering_server_globals.h, renderer_scene_render_rd.h, material_storage.h, copy_effects.h, framebuffer_cache_rd.h, engine.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `thirdparty/vulkan/include/vulkan/vulkan_core.h` (CPP | Tier 1.5 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.619 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.355 IQR)
- **Top Global Matches:** file_cluster_8: 10.619, file_cluster_7: 11.302, file_cluster_12: 11.383
- **Magnitude:** 4912.4 | **LOC:** 24741 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.4387%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 6344`, `args: 1476`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1154`, `state_mutation: 4481`
* *Architecture:* `import: 12`
* *Defense:* `sync_locks: 13`, `immutability_locks: 2359`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vulkan_video_codec_h265std.h, vulkan_video_codec_av1std.h, vulkan_video_codec_h264std.h, vulkan_video_codec_av1std_decode.h, vulkan_video_codec_h265std_encode.h, vulkan_video_codec_vp9std_decode.h, vulkan_video_codec_h264std_encode.h, vulkan_video_codec_h265std_decode.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `thirdparty/clipper2/src/clipper.engine.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.154 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.184 IQR)
- **Top Global Matches:** file_cluster_8: 15.154, file_cluster_11: 15.333, file_cluster_13: 15.342
- **Magnitude:** 4826.5 | **LOC:** 3162 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.3411%), Tech Debt (71.5906%)
**Top Internal Functions/Classes:**
  * `PointInOpPolygon` (Impact: 967.4)
  * `ClipperBase::InsertLocalMinimaIntoAEL` (Impact: 867.2)
  * `ClipperBase::DoHorizontal` (Impact: 115.3)
  * `ClipperBase::CheckJoinLeft` (Impact: 43.4)
  * `ClipperBase::CheckJoinRight` (Impact: 43.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 590`, `structural_boundaries: 204`, `args: 100`, `func_start: 84`, `class_start: 3`
* *Risk/State:* `state_mutation: 1975`, `dead_code: 9`, `duplicate_logic: 4`, `orphaned_logic: 46`
* *Architecture:* `import: 5`
* *Defense:* `doc: 5`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` xmmintrin.h, clipper.engine.h, emmintrin.h, stdexcept, clipper.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `servers/rendering/rendering_server.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.187 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.122 IQR)
- **Top Global Matches:** file_cluster_8: 15.187, file_cluster_13: 15.543, file_cluster_7: 15.558
- **Magnitude:** 4606.76 | **LOC:** 3822 | **CtrlFlow:** 84.0% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (89.1864%), Tech Debt (32.5892%)
**Top Internal Functions/Classes:**
  * `RenderingServer::_surface_set_data` (Impact: 628.7)
  * `RenderingServer::_get_array_from_surface` (Impact: 268.7)
  * `RenderingServer::mesh_surface_make_offse` (Impact: 216.2)
  * `RenderingServer::mesh_create_surface_dat` (Impact: 145.7)
  * `RenderingServer::global_shader_uniform_t` (Impact: 58.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 462`, `structural_boundaries: 88`, `args: 1261`, `func_start: 46`
* *Risk/State:* `high_risk_execution: 28`, `state_mutation: 2948`, `duplicate_logic: 6`, `orphaned_logic: 35`
* *Architecture:* `import: 11`
* *Defense:* `doc: 4`, `immutability_locks: 134`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` rendering_server.compat.inc, os.h, rendering_server_types.h, rendering_device.h, typed_array.h, project_settings.h, shader_warnings.h, rendering_server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `platform/windows/display_server_windows.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.223 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.773 IQR)
- **Top Global Matches:** file_cluster_8: 15.223, file_cluster_13: 15.38, file_cluster_11: 15.564
- **Magnitude:** 4454.08 | **LOC:** 8293 | **CtrlFlow:** 69.1% | **Authorship Centralization:** 39.1%
- **Risk Profile:** Cognitive Load (91.0257%), Tech Debt (99.3326%)
**Top Internal Functions/Classes:**
  * `_get_monitor_desc` (Impact: 448.1)
  * `DisplayServerWindows::_handle_early_wind` (Impact: 141.2)
  * `DisplayServerWindows::_thread_fd_monitor` (Impact: 113.8)
  * `DisplayServerWindows::_get_window_style` (Impact: 74.5)
  * `DisplayServerWindows::create_sub_window` (Impact: 62.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 555`, `structural_boundaries: 248`, `args: 244`, `func_start: 140`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 9`, `state_mutation: 2450`, `fragile_debt: 1`, `duplicate_logic: 8`, `orphaned_logic: 107`
* *Architecture:* `api: 1`, `import: 38`
* *Defense:* `safety: 2`, `doc: 4`, `sync_locks: 7`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 28):` propkey.h, project_settings.h, native_menu_windows.h, file_access.h, version.h, rasterizer_dummy.h, drop_target_windows.h, dxgi1_6.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `servers/text/text_server.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.31 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.006 IQR)
- **Top Global Matches:** file_cluster_8: 15.31, file_cluster_13: 15.626, file_cluster_7: 15.679
- **Magnitude:** 4374.66 | **LOC:** 2447 | **CtrlFlow:** 85.2% | **Authorship Centralization:** 71.4%
- **Risk Profile:** Cognitive Load (92.0138%), Tech Debt (54.8353%)
**Top Internal Functions/Classes:**
  * `TextServer::shaped_text_get_line_breaks_` (Impact: 244.8)
  * `TextServer::shaped_text_get_line_breaks` (Impact: 230.7)
  * `TextServer::parse_structured_text` (Impact: 164.6)
    * *Intent:* #endif // DISABLE_DEPRECATED
  * `TextServer::shaped_text_draw` (Impact: 123.6)
  * `TextServer::shaped_text_draw_outline` (Impact: 115.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 101`, `args: 611`, `func_start: 59`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 2833`, `orphaned_logic: 54`
* *Architecture:* `import: 9`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.039
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` text_server.compat.inc, os.h, text_server.h, typed_array.h, project_settings.h, main_loop.h, translation_server.h, rendering_server.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/ExportedFields.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, decorators: 62, encapsulation: 61, scientific: 18
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/ExportedToolButtons.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 7, args: 4, closures: 4, indent_spaces: 4
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Bridge/ScriptManagerBridge.types.cs` (CSHARP) | Magnitude: 103.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 78, state_mutation: 57, func_start: 27, structural_boundaries: 25
- `thirdparty/embree/kernels/builders/priminfo.h` (CPP) | Magnitude: 92.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 39, state_mutation: 36, immutability_locks: 29
- `core/math/bvh_cull.inc` (CPP) | Magnitude: 609.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 367, indent_tabs: 316, api: 109, branch: 89

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `platform/web/eslint.config.cjs` (JAVASCRIPT) | Magnitude: 21.96 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 185, events: 45, decorators: 18, doc: 10
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Rect2I.cs` (CSHARP) | Magnitude: 152.56 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 196, doc: 180, structural_boundaries: 39, api: 30
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Rect2.cs` (CSHARP) | Magnitude: 169.92 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 239, doc: 196, structural_boundaries: 44, func_start: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `modules/mono/utils/string_utils.cpp` (CPP) | Magnitude: 368.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 131, indent_tabs: 113, branch: 110, pointers: 26
- `thirdparty/embree/kernels/common/scene_instance.h` (CPP) | Magnitude: 210.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 224, state_mutation: 117, immutability_locks: 69, structural_boundaries: 65
- `thirdparty/harfbuzz/src/hb-set-digest.hh` (CPP) | Magnitude: 211.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 77, structural_boundaries: 27, immutability_locks: 19
- `thirdparty/minizip/skipset.h` (CPP) | Magnitude: 259.88 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 185, pointers: 117, indent_spaces: 106, branch: 29
- `thirdparty/embree/kernels/subdiv/feature_adaptive_eval_simd.h` (CPP) | Magnitude: 276.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 177, indent_spaces: 143, immutability_locks: 59, branch: 40

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
- `thirdparty/jolt_physics/Jolt/Core/RTTI.h` (CPP) | Magnitude: 99.9 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 568, structural_boundaries: 133, indent_tabs: 113, pointers: 92
- `scene/2d/line_2d.cpp` (CPP) | Magnitude: 285.28 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 205, state_mutation: 169, args: 77, pointers: 53
- `scene/3d/remote_transform_3d.h` (CPP) | Magnitude: 21.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 11, immutability_locks: 11, args: 7
- `servers/audio/effects/audio_effect_distortion.cpp` (CPP) | Magnitude: 162.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 103, indent_tabs: 86, args: 28, pointers: 23
- `thirdparty/icu4c/common/dictionarydata.h` (CPP) | Magnitude: 3.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, doc: 9, globals: 8, immutability_locks: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `platform/web/js/engine/features.js` (JAVASCRIPT) | Magnitude: 38.64 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 45, doc: 16, state_mutation: 15, branch: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `thirdparty/jolt_physics/Jolt/Core/StringTools.h` (CPP) | Magnitude: 18.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 15, pointers: 13, immutability_locks: 10, doc: 8
- `platform/macos/display_server_macos_embedded.h` (OBJECTIVE-C) | Magnitude: 103.66 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 107, state_mutation: 81, immutability_locks: 68, func_start: 64
- `platform/android/java/lib/src/main/java/org/godotengine/godot/editor/utils/EditorUtils.kt` (KOTLIN) | Magnitude: 20.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 4, indent_tabs: 4, args: 2
- `thirdparty/mingw-std-threads/mingw.invoke.h` (CPP) | Magnitude: 82.32 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 79, structural_boundaries: 71, indent_spaces: 71, explicit_casts: 18
- `thirdparty/jolt_physics/Jolt/Core/UnorderedMap.h` (CPP) | Magnitude: 81.32 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 63, indent_tabs: 42, structural_boundaries: 29, pointers: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `thirdparty/zstd/common/bits.h` (CPP) | Magnitude: 190.16 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 109, state_mutation: 83, branch: 41, structural_boundaries: 32
- `thirdparty/embree/kernels/subdiv/half_edge.h` (CPP) | Magnitude: 552.54 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 385, indent_spaces: 263, pointers: 84, branch: 70
- `platform/web/js/jsdoc2rst/publish.js` (JAVASCRIPT) | Magnitude: 317.7 | Delta: **0.34 IQR** | Secondary Pull: `file_cluster_8`
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
- `editor/animation/animation_blend_tree_editor_plugin.h` (CPP) | Magnitude: 23.86 | Delta: **0.052 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 110, safety_bypasses: 45, immutability_locks: 45, ui_framework: 17
- `modules/mono/editor/code_completion.cpp` (CPP) | Magnitude: 62.5 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 170, branch: 69, ui_framework: 26, state_mutation: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `drivers/metal/metal_objects_shared.cpp` (CPP) | Magnitude: 481.36 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 322, state_mutation: 270, pointers: 155, branch: 80
- `modules/mono/editor/GodotTools/GodotTools/Ides/MessagingServer.cs` (CSHARP) | Magnitude: 103.26 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 81, structural_boundaries: 39, concurrency: 36, state_mutation: 25
- `modules/mono/editor/GodotTools/GodotTools.IdeMessaging.CLI/Program.cs` (CSHARP) | Magnitude: 123.76 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 167, structural_boundaries: 70, func_start: 35, concurrency: 34
- `thirdparty/vhacd/src/VHACD-ASYNC.cpp` (CPP) | Magnitude: 313.78 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 252, state_mutation: 198, immutability_locks: 52, structural_boundaries: 51
- `platform/web/js/libs/audio.worklet.js` (JAVASCRIPT) | Magnitude: 373.88 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 263, indent_tabs: 164, branch: 38, immutability_locks: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `thirdparty/jolt_physics/Jolt/Renderer/DebugRendererSimple.h` (CPP) | Magnitude: 22.62 | Delta: **0.247 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 29, indent_tabs: 29, structural_boundaries: 13, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `thirdparty/embree/kernels/bvh/node_intersector_packet.h` (CPP) | Magnitude: 874.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: state_mutation: 730, indent_spaces: 663, doc: 616, immutability_locks: 362
- `thirdparty/mbedtls/include/mbedtls/asn1write.h` (CPP) | Magnitude: 28.5 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 142, pointers: 45, indent_spaces: 38, immutability_locks: 30
- `platform/android/java/lib/src/main/java/org/godotengine/godot/FullScreenGodotApp.java` (JAVA) | Magnitude: 12.56 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 6, structural_boundaries: 3, class_start: 1, api: 1
- `thirdparty/sdl/include/SDL3/SDL_asyncio.h` (CPP) | Magnitude: 15.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, pointers: 11, sec_high_risk_execution: 7, structural_boundaries: 6
- `modules/mono/glue/GodotSharp/GodotSharp/Core/Vector3.cs` (CSHARP) | Magnitude: 307.22 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 469, doc: 444, scientific: 126, func_start: 88

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `editor/animation/animation_player_editor_plugin.h` (CPP) | Magnitude: 114.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 227, structural_boundaries: 120, state_mutation: 81, pointers: 76
- `main/main.cpp` (CPP) | Magnitude: 1554.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 1369, indent_tabs: 1343, branch: 482, pointers: 363
- `thirdparty/jolt_physics/Jolt/Core/Factory.h` (CPP) | Magnitude: 18.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 13, doc: 10, immutability_locks: 10, structural_boundaries: 5
- `editor/export/gdextension_export_plugin.h` (CPP) | Magnitude: 160.96 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 98, state_mutation: 81, branch: 33, pointers: 23
- `editor/script/script_create_dialog.h` (CPP) | Magnitude: 50.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 69, state_mutation: 25, immutability_locks: 24, safety_bypasses: 20

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

- `editor/editor_node.cpp` -> Churn: **100.0%** | Cog Load: 82.3159% | Debt: 99.999%
- `editor/scene/3d/node_3d_editor_plugin.cpp` -> Churn: **97.33%** | Cog Load: 85.8255% | Debt: 29.776%
- `editor/inspector/editor_inspector.cpp` -> Churn: **86.56%** | Cog Load: 38.83% | Debt: 99.9898%
- `editor/inspector/editor_properties.cpp` -> Churn: **86.08%** | Cog Load: 45.6555% | Debt: 99.9992%
- `editor/docks/editor_dock_manager.cpp` -> Churn: **85.18%** | Cog Load: 36.0861% | Debt: 96.3053%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `thirdparty/pcre2/src/pcre2_compile.c` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 5605.02
- `thirdparty/vulkan/include/vulkan/vulkan_core.h` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 4912.4
- `thirdparty/jolt_physics/Jolt/Core/Array.h` -> **Mikael Hermansson** (100.0% isolated ownership) | Magnitude: 4271.44
- `thirdparty/pcre2/src/pcre2_match.c` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 3792.24
- `thirdparty/vulkan/vk_mem_alloc.h` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 3388.96

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

- `core/io/resource.h` -> **Severity: 1022.666** (Blast Radius: 12.718 * Doc Risk: 80.4109%)
- `core/typedefs.h` -> **Severity: 675.424** (Blast Radius: 42.491 * Doc Risk: 15.8957%)
- `core/templates/safe_refcount.h` -> **Severity: 664.195** (Blast Radius: 7.905 * Doc Risk: 84.0221%)
- `core/object/ref_counted.h` -> **Severity: 470.189** (Blast Radius: 10.495 * Doc Risk: 44.8012%)
- `core/error/error_macros.h` -> **Severity: 313.533** (Blast Radius: 17.535 * Doc Risk: 17.8804%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
