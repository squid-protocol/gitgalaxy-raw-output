# ARCHITECTURAL_BRIEF: godot
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/godotengine/godot.git` |
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
- **Scope:** 6916 analyzed artifact(s), 1293564 LOC.
- **Load-bearing artifact:** `core/object/class_db.h` -- 856 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `scene/register_scene_types.cpp` -- pulls in 313 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `servers/rendering/shader_language.cpp` at magnitude 15553.62 (structural weight, not risk).
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
| Total Artifacts | 14219 |
| Analyzed Artifacts (Scanned) | 6916 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 7303 |
| Total LOC | 1293564 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 48.6% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4407 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.093 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 22.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 8.0794 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 128 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 3583 | 1146668 | 51.8% |
| XML | 1420 | 34 | 20.5% |
| PLAINTEXT | 680 | 2 | 9.8% |
| PYTHON | 334 | 16397 | 4.8% |
| CSHARP | 291 | 35292 | 4.2% |
| JAVA | 190 | 29359 | 2.7% |
| GLSL | 141 | 27129 | 2.0% |
| OBJECTIVE-C | 108 | 17500 | 1.6% |
| KOTLIN | 50 | 7194 | 0.7% |
| MARKDOWN | 26 | 0 | 0.4% |
| JAVASCRIPT | 26 | 6336 | 0.4% |
| YAML | 25 | 1324 | 0.4% |
| C | 17 | 4119 | 0.2% |
| GROOVY | 11 | 1411 | 0.2% |
| SHELL | 6 | 312 | 0.1% |
| JSON | 3 | 363 | 0.0% |
| CSV | 2 | 11 | 0.0% |
| MAKEFILE | 1 | 25 | 0.0% |
| SWIFT | 1 | 22 | 0.0% |
| BATCH | 1 | 66 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 6914 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 36%, Large Core Modules (3) 18%, Declarative / Non-Code 16%, Parameter Forwarders Files 7%, Interface Declarations Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 6193 | 89.5% |
| Unknown | 2 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 704 | 10.2% |
| Static: Minified & Vendor Opaque Mass | 17 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 7303*

**Composition by Extension & Reason:**
- `.h`: 2359x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5103 LOC), 1x Excluded (Machine-Generated Source Code Signature: 1423 LOC)
- `.xml`: 946x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 7 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.c`: 902x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Machine-Generated Source Code Signature: 68 LOC), 1x Excluded (Machine-Generated Source Code Signature: 14005 LOC)
- `.gd`: 754x Unsupported Format (.gd), 39x Excluded: Neighborhood Micro-Mass Limit Exceeded, 10x Excluded (Unsupported Extension: '.gd')
- `.cpp`: 671x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 7192 hex tokens in 3653 LOC)
- `.hh`: 267x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.hpp`: 201x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.out`: 136x Excluded: Neighborhood Micro-Mass Limit Exceeded, 1x Excluded (Saturation: Line 3 exceeds 500 chars)
- `.cfg`: 131x Unsupported Format (.cfg)
- `no_extension`: 123x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable), 1x Excluded (Lexical Monotony: High structural repetition detected in 2433 LOC)
- `.po`: 113x Excluded (Unsupported Extension: '.po')
- `.cc`: 113x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.patch`: 80x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.patch')
- `.strings`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 34x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 47748 commas in 2223 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.4 | 29.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.0 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 29.3 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.1 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 30.8 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 8.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.7 | 66.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 99.8 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 15898 | 1621 | 4 | `core/variant/variant.cpp` |
| cleanup | 1119 | 432 | 0 | `drivers/d3d12/rendering_device_driver_d3d12.cpp` |
| guards | 135463 | 3740 | 49 | `scene/resources/visual_shader_nodes.h` |
| danger | 6858 | 1156 | 1 | `modules/mono/glue/runtime_interop.cpp` |
| concurrency | 3053 | 346 | 0 | `modules/text_server_adv/text_server_adv.cpp` |
| connectivity | 19891 | 2425 | 6 | `servers/physics_3d/physics_server_3d_dummy.h` |
| io | 1789 | 236 | 0 | `methods.py` |
| crypto | 1 | 1 | 0 | `methods.py` |
| ipc | 178 | 50 | 0 | `methods.py` |
| time | 39 | 18 | 0 | `platform/macos/os_macos.mm` |
| serialization | 21 | 8 | 0 | `misc/scripts/install_vulkan_sdk_macos.sh` |
| regex | 61 | 30 | 0 | `methods.py` |
| events | 4997 | 546 | 0 | `editor/inspector/editor_properties_array_dict.cpp` |
| tests | 13053 | 237 | 0 | `tests/scene/test_text_edit.cpp` |
| docs | 31426 | 4109 | 5 | `modules/mono/glue/GodotSharp/GodotSharp/Core/Mathf.cs` |
| debt | 2522 | 654 | 0 | `tests/scene/test_control.cpp` |
| mutation | 353756 | 3733 | 114 | `servers/rendering/shader_language.cpp` |
| dead_code | 34449 | 1974 | 12 | `scene/resources/visual_shader_nodes.cpp` |
| credential | 19 | 14 | 0 | `drivers/gles3/storage/material_storage.cpp` |
| threat | 9 | 3 | 0 | `tests/servers/test_text_server.cpp` |
| ml_ai | 1605 | 91 | 0 | `modules/mono/glue/GodotSharp/GodotSharp/Core/Vector3.cs` |
| ui | 148 | 32 | 0 | `platform/android/java/editor/src/main/java/org/godotengine/editor/embed/GameMenuFragment.kt` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `methods.py` (Hits: 92)
- `modules/mono/build_scripts/build_assemblies.py` (Hits: 82)
- `platform/windows/detect.py` (Hits: 73)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **class_db.h** (`core/object/class_db.h`) — 856 inbound connections
2. **memory.h** (`core/os/memory.h`) — 773 inbound connections
3. **variant.h** (`core/variant/variant.h`) — 721 inbound connections
4. **ustring.cpp** (`core/string/ustring.cpp`) — 680 inbound connections
5. **typedefs.h** (`core/typedefs.h`) — 594 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **register_scene_types.cpp** (`scene/register_scene_types.cpp`) — 313 outbound dependencies
2. **editor_node.cpp** (`editor/editor_node.cpp`) — 156 outbound dependencies
3. **register_editor_types.cpp** (`editor/register_editor_types.cpp`) — 111 outbound dependencies
4. **node_3d_editor_plugin.cpp** (`editor/scene/3d/node_3d_editor_plugin.cpp`) — 84 outbound dependencies
5. **main.cpp** (`main/main.cpp`) — 84 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ShaderLanguage::_parse_expression` **(Many-Argument Workhorses)** (@ `servers/rendering/shader_language.cpp`) -> Impact: **1628.0** | LOC: 1880
- `ShaderLanguage::_parse_shader` **(Many-Argument Workhorses)** (@ `servers/rendering/shader_language.cpp`) -> Impact: **1381.8** | LOC: 1921
- `ShaderCompiler::_dump_node_code` **(Many-Argument Workhorses)** (@ `servers/rendering/shader_compiler.cpp`) -> Impact: **1184.9** | LOC: 1070
- `Main::setup` **(Many-Argument Workhorses)** (@ `main/main.cpp`) -> Impact: **1180.4** | LOC: 1606
  * *Intent:* * command line arguments to configure things accordingly. * If p_second_phase is true, it will chain into setup2() (default behavior). This is * disab...
- `DisplayServerWindows::WndProc` **(Many-Argument Workhorses)** (@ `platform/windows/display_server_windows.cpp`) -> Impact: **1156.3** | LOC: 1391
  * *Intent:* // The window procedure for our window class "Engine", used to handle processing of window-related system messages/events. // See: https://docs.micros...
- `RichTextLabel::_draw_line` **(Many-Argument Workhorses)** (@ `scene/gui/rich_text_label.cpp`) -> Impact: **1058.9** | LOC: 699
- `VisualShader::_write_node` **(Many-Argument Workhorses)** (@ `scene/resources/visual_shader.cpp`) -> Impact: **1039.5** | LOC: 560
- `TextServerAdvanced::_ensure_glyph` **(Many-Argument Workhorses)** (@ `modules/text_server_adv/text_server_adv.cpp`) -> Impact: **974.7** | LOC: 1367
  * *Intent:* #endif /*************************************************************************/ /* Font Cache */ /*************************************************...
- `ShaderLanguage::_validate_operator` **(Many-Argument Workhorses)** (@ `servers/rendering/shader_language.cpp`) -> Impact: **969.1** | LOC: 491
- `GDScriptCompiler::_parse_expression` **(Many-Argument Workhorses)** (@ `modules/gdscript/gdscript_compiler.cpp`) -> Impact: **940.7** | LOC: 1178

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `scene/gui` | 130 | 62934.84 | 30.08% | 32.06% |
| `scene/resources` | 139 | 54798.8 | 25.63% | 38.59% |
| `servers/rendering` | 62 | 48752.84 | 30.36% | 32.83% |
| `modules/gdscript` | 39 | 36039.9 | 35.84% | 16.84% |
| `core/io` | 106 | 24125.1 | 23.64% | 34.67% |
| `scene/3d` | 117 | 23913.16 | 26.34% | 34.33% |
| `core/math` | 89 | 21437.02 | 34.83% | 28.28% |
| `servers/rendering/renderer_rd/storage_rd` | 21 | 17769.7 | 34.12% | 36.8% |
| `editor/animation` | 21 | 17166.86 | 35.46% | 29.33% |
| `core/variant` | 38 | 16237.06 | 26.77% | 40.98% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug_report.yml` -> **100.0%** Exposure
- `misc/utility/godot_gdb_pretty_print.py` -> **100.0%** Exposure
- `core/config/engine.cpp` -> **100.0%** Exposure
- `core/crypto/crypto_core.cpp` -> **100.0%** Exposure
- `core/debugger/script_debugger.cpp` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `SConstruct` -> **100.0%** Exposure
- `core/core_builders.py` -> **100.0%** Exposure
- `core/crypto/SCsub` -> **100.0%** Exposure
- `core/extension/make_interface_header.py` -> **100.0%** Exposure
- `core/extension/make_wrappers.py` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `scene/resources/visual_shader_nodes.cpp` -> **867** Orphaned Functions | **0** Duplicates
- `modules/text_server_adv/text_server_adv.cpp` -> **265** Orphaned Functions | **0** Duplicates
- `servers/text/text_server_extension.cpp` -> **252** Orphaned Functions | **0** Duplicates
- `modules/mono/glue/GodotSharp/GodotSharp/Core/NativeInterop/NativeFuncs.cs` -> **237** Orphaned Functions | **0** Duplicates
- `modules/jolt_physics/jolt_physics_server_3d.cpp` -> **235** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/X509CertificateUtils.java` -> **99.7922%** Exposure
- `platform/android/java/lib/src/main/java/org/godotengine/godot/utils/GodotNetUtils.java` -> **99.7922%** Exposure
- `modules/mbedtls/crypto_mbedtls.cpp` -> **29.6661%** Exposure
- `platform/macos/os_macos.mm` -> **22.2134%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `14` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `22219` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `servers/rendering/shader_language.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.254)
- **Top Global Matches:** file_cluster_8: 7.254, file_cluster_6: 17.943, file_cluster_3: 19.417
- **Magnitude:** 15553.62 | **LOC:** 12235 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 37.5%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **9**; blast radius 0.073; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ShaderLanguage::_parse_expression` **(Many-Argument Workhorses)** (Impact: 1628.0)
  * `ShaderLanguage::_parse_shader` **(Many-Argument Workhorses)** (Impact: 1381.8)
  * `ShaderLanguage::_validate_operator` **(Many-Argument Workhorses)** (Impact: 969.1)
  * `ShaderLanguage::_parse_block` **(Many-Argument Workhorses)** (Impact: 798.7)
  * `ShaderLanguage::complete` **(Many-Argument Workhorses)** (Impact: 570.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2057 instances
* *State Mutation (weighted view):* 6332
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4001`, `structural_boundaries: 765`, `args: 535`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `state_mutation: 2218`, `dead_code: 3`, `planned_debt: 7`, `fragile_debt: 6`, `unreferenced_by_name: 93`
* *Architecture:* `import: 9`
* *Defense:* `safety: 2`, `doc: 6`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.073
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.057255
  * `Imports (Out-Degree: 31):` engine.h, os.h, local_vector.h, rb_set.h, renderer_compositor.h, rendering_server.h, rendering_server_globals.h, shader_types.h...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `modules/text_server_adv/text_server_adv.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.81)
- **Top Global Matches:** file_cluster_4: 7.81, file_cluster_6: 11.802, file_cluster_15: 12.856
- **Magnitude:** 9939.78 | **LOC:** 8441 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 72.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.046; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (76.1%)
- **Documentation Coverage:** 97.9866% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TextServerAdvanced::_ensure_glyph` **(Many-Argument Workhorses)** (Impact: 974.7)
    * *Intent:* #endif /*************************************************************************/ /* Font Cache */ ...
  * `TextServerAdvanced::_shape_run` **(Many-Argument Workhorses)** (Impact: 574.6)
  * `TextServerAdvanced::_ensure_cache_for_size` **(Many-Argument Workhorses)** (Impact: 528.4)
  * `TextServerAdvanced::_shaped_text_overrun_trim_to_width` **(Many-Argument Workhorses)** (Impact: 243.0)
  * `TextServerAdvanced::_is_valid_identifier` **(Compute Cores)** (Impact: 223.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1184 instances
* *State Mutation (weighted view):* 3800
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2094`, `structural_boundaries: 482`, `args: 459`, `func_start: 298`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 1432`, `unreferenced_by_name: 265`
* *Architecture:* `api: 1`, `import: 18`
* *Defense:* `safety: 1`, `doc: 15`, `sync_locks: 362`, `immutability_locks: 608`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` EdgeHolder.h, ShapeDistanceFinder.h, project_settings.h, contour-combiners.h, edge-selectors.h, error_macros.h, file_access.h, math_funcs_binary.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scene/gui/rich_text_label.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.245)
- **Top Global Matches:** file_cluster_4: 8.245, file_cluster_6: 11.177, file_cluster_15: 13.936
- **Magnitude:** 9372.52 | **LOC:** 8433 | **CtrlFlow:** 30.7% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **25**; blast radius 0.052; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RichTextLabel::_draw_line` **(Many-Argument Workhorses)** (Impact: 1058.9)
  * `RichTextLabel::append_text` **(Many-Argument Workhorses)** (Impact: 755.2)
  * `RichTextLabel::_find_click_in_line` **(Many-Argument Workhorses)** (Impact: 396.5)
  * `RichTextLabel::gui_input` **(Compute Cores)** (Impact: 186.9)
  * `RichTextLabel::_shape_line` **(Many-Argument Workhorses)** (Impact: 178.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1246 instances
* *State Mutation (weighted view):* 4033
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2202`, `structural_boundaries: 388`, `args: 584`, `func_start: 254`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1541`, `fragile_debt: 3`, `unreferenced_by_name: 105`
* *Architecture:* `import: 25`
* *Defense:* `doc: 4`, `sync_locks: 31`, `immutability_locks: 222`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.052
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000289
  * `Imports (Out-Degree: 46):` input_map.h, resource_loader.h, math_defs.h, callable_mp.h, class_db.h, keyboard.h, os.h, translation_server.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scene/gui/text_edit.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.448)
- **Top Global Matches:** file_cluster_4: 10.448, file_cluster_15: 13.32, file_cluster_16: 14.197
- **Magnitude:** 7416.0 | **LOC:** 9390 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 22.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **21**; blast radius 0.061; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.7%)
- **Documentation Coverage:** 99.3023% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TextEdit::_notification` **(Many-Argument Workhorses)** (Impact: 765.4)
  * `TextEdit::gui_input` **(Compute Cores)** (Impact: 259.3)
  * `TextEdit::alt_input` **(Compute Cores)** (Impact: 153.1)
  * `TextEdit::menu_option` **(Compute Cores)** (Impact: 115.1)
  * `TextEdit::_offset_carets_after` **(Many-Argument Workhorses)** (Impact: 74.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 919 instances
* *State Mutation (weighted view):* 2904
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2216`, `structural_boundaries: 706`, `args: 846`, `func_start: 426`, `class_start: 1`
* *Risk/State:* `state_mutation: 1066`, `fragile_debt: 3`, `unreferenced_by_name: 156`
* *Architecture:* `import: 21`
* *Defense:* `doc: 11`, `immutability_locks: 350`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.061
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000325
  * `Imports (Out-Degree: 42):` engine.h, project_settings.h, input.h, input_map.h, callable_mp.h, class_db.h, script_language.h, keyboard.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `editor/scene/3d/node_3d_editor_plugin.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.572)
- **Top Global Matches:** file_cluster_6: 9.572, file_cluster_4: 9.807, file_cluster_15: 16.697
- **Magnitude:** 7381.98 | **LOC:** 11167 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 39.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **84**; blast radius 0.051; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (97.3%), Complexity Load (formerly Cognitive Load) (90.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.2032% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Node3DEditorViewport::_sinput` **(Compute Cores)** (Impact: 670.2)
  * `Node3DEditorViewport::_notification` **(Many-Argument Workhorses)** (Impact: 262.3)
  * `Node3DEditorViewport::_menu_option` **(Compute Cores)** (Impact: 177.6)
  * `Node3DEditorViewport::update_transform` **(Compute Cores)** (Impact: 153.5)
    * *Intent:* // Update the current transform operation in response to an input.
  * `Node3DEditorViewport::_transform_gizmo_select` **(Many-Argument Workhorses)** (Impact: 125.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 935 instances
* *State Mutation (weighted view):* 3203
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2286`, `structural_boundaries: 391`, `args: 1465`, `func_start: 262`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1333`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `unreferenced_by_name: 171`
* *Architecture:* `import: 84`
* *Defense:* `doc: 6`, `sync_locks: 11`, `immutability_locks: 378`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.051
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000289
  * `Imports (Out-Degree: 110):` project_settings.h, input.h, input_map.h, resource_loader.h, geometry_3d.h, math_funcs.h, projection.h, callable_mp.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `modules/gltf/gltf_document.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.184)
- **Top Global Matches:** file_cluster_6: 6.184, file_cluster_4: 9.237, file_cluster_8: 16.244
- **Magnitude:** 7310.24 | **LOC:** 7268 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **36**; blast radius 0.067; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%)
- **Documentation Coverage:** 89.193% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GLTFDocument::_convert_animation_node_track` **(Many-Argument Workhorses)** (Impact: 334.2)
  * `GLTFDocument::_import_animation` **(Many-Argument Workhorses)** (Impact: 227.5)
  * `GLTFDocument::_parse_meshes` **(Many-Argument Workhorses)** (Impact: 203.5)
  * `GLTFDocument::export_object_model_property` **(Many-Argument Workhorses)** (Impact: 195.0)
  * `GLTFDocument::import_object_model_property` **(Many-Argument Workhorses)** (Impact: 180.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1110 instances
* *State Mutation (weighted view):* 3589
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1550`, `structural_boundaries: 314`, `args: 347`, `func_start: 161`, `class_start: 2`
* *Risk/State:* `state_mutation: 1369`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 118`, `import: 36`
* *Defense:* `doc: 4`, `immutability_locks: 445`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.067
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.00065
  * `Imports (Out-Degree: 71):` engine.h, project_settings.h, crypto_core.h, config_file.h, dir_access.h, file_access.h, file_access_memory.h, json.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `editor/animation/animation_track_editor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.695)
- **Top Global Matches:** file_cluster_4: 8.695, file_cluster_6: 9.275, file_cluster_15: 15.44
- **Magnitude:** 7201.56 | **LOC:** 9996 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 12.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **39**; blast radius 0.049; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.6971% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AnimationTrackEditor::_edit_menu_pressed` **(Many-Argument Workhorses)** (Impact: 356.5)
  * `AnimationTrackEdit::_notification` **(Compute Cores)** (Impact: 167.5)
    * *Intent:* ////////////////////////////////////
  * `AnimationTrackEdit::gui_input` **(Compute Cores)** (Impact: 144.9)
  * `AnimationMultiTrackKeyEdit::_set` **(Many-Argument Workhorses)** (Impact: 137.6)
  * `AnimationTrackKeyEdit::_set` **(Many-Argument Workhorses)** (Impact: 119.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 916 instances
* *State Mutation (weighted view):* 3019
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2084`, `structural_boundaries: 517`, `args: 1290`, `func_start: 305`, `class_start: 3`
* *Risk/State:* `state_mutation: 1187`, `planned_debt: 1`, `fragile_debt: 6`, `unreferenced_by_name: 203`
* *Architecture:* `import: 39`
* *Defense:* `doc: 8`, `sync_locks: 1`, `immutability_locks: 294`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.047093
  * `Imports (Out-Degree: 67):` animation_track_editor.h, project_settings.h, error_macros.h, input.h, resource_loader.h, callable_mp.h, class_db.h, translation_server.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `platform/windows/display_server_windows.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.212)
- **Top Global Matches:** file_cluster_4: 8.212, file_cluster_6: 12.493, file_cluster_15: 13.164
- **Magnitude:** 7176.7 | **LOC:** 8293 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 39.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **38**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.4%), Debt Markers (formerly Tech Debt) (91.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (81.2%)
- **Documentation Coverage:** 85.42% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DisplayServerWindows::WndProc` **(Many-Argument Workhorses)** (Impact: 1156.3)
    * *Intent:* // The window procedure for our window class "Engine", used to handle processing of window-related s...
  * `DisplayServerWindows::DisplayServerWindows` **(Many-Argument Workhorses)** (Impact: 497.8)
  * `DisplayServerWindows::_create_window` **(Many-Argument Workhorses)** (Impact: 195.8)
  * `DisplayServerWindows::_get_window_style` **(Many-Argument Workhorses)** (Impact: 140.1)
  * `DisplayServerWindows::window_set_flag` **(Many-Argument Workhorses)** (Impact: 97.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 792 instances
* *State Mutation (weighted view):* 2675
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1795`, `structural_boundaries: 509`, `args: 637`, `func_start: 249`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 1091`, `planned_debt: 3`, `fragile_debt: 3`, `unreferenced_by_name: 214`
* *Architecture:* `api: 1`, `import: 38`
* *Defense:* `safety: 4`, `doc: 4`, `sync_locks: 7`, `immutability_locks: 289`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.00026
  * `Imports (Out-Degree: 60):` avrt.h, engine.h, project_settings.h, input.h, dir_access.h, file_access.h, marshalls.h, xml_parser.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scene/resources/2d/tile_set.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.922)
- **Top Global Matches:** file_cluster_4: 8.922, file_cluster_15: 11.615, file_cluster_16: 12.723
- **Magnitude:** 7152.64 | **LOC:** 7210 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 27.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.3%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (79.4%)
- **Documentation Coverage:** 98.3562% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TileSet::get_neighbor_cell` **(Compute Cores)** (Impact: 614.0)
  * `TileSet::_set` **(Many-Argument Workhorses)** (Impact: 280.5)
    * *Intent:* #endif // DISABLE_DEPRECATED
  * `TileSet::transform_coords_layout` **(Many-Argument Workhorses)** (Impact: 144.0)
  * `TileSet::_get_half_offset_corner_or_side_terrain_peering_bit_polygon` **(Many-Argument Workhorses)** (Impact: 142.0)
  * `TileSet::_get` **(Compute Cores)** (Impact: 140.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 892 instances
* *State Mutation (weighted view):* 2858
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1944`, `structural_boundaries: 658`, `args: 887`, `func_start: 364`, `class_start: 1`
* *Risk/State:* `state_mutation: 1074`, `planned_debt: 3`, `unreferenced_by_name: 155`
* *Architecture:* `import: 13`
* *Defense:* `doc: 10`, `immutability_locks: 275`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.044357
  * `Imports (Out-Degree: 38):` engine.h, marshalls.h, geometry_2d.h, callable_mp.h, class_db.h, local_vector.h, rb_set.h, control.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `modules/gdscript/gdscript_analyzer.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.125)
- **Top Global Matches:** file_cluster_8: 6.125, file_cluster_6: 12.715, file_cluster_4: 21.29
- **Magnitude:** 7096.34 | **LOC:** 6634 | **CtrlFlow:** 40.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **14**; blast radius 0.065; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (95.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GDScriptAnalyzer::reduce_call` **(Many-Argument Workhorses)** (Impact: 512.6)
    * *Intent:* #endif // SUGGEST_GODOT4_RENAMES
  * `GDScriptAnalyzer::reduce_subscript` **(Many-Argument Workhorses)** (Impact: 364.5)
  * `GDScriptAnalyzer::reduce_identifier` **(Many-Argument Workhorses)** (Impact: 205.7)
  * `GDScriptAnalyzer::resolve_class_member` **(Many-Argument Workhorses)** (Impact: 187.0)
  * `GDScriptAnalyzer::resolve_function_signature` **(Many-Argument Workhorses)** (Impact: 174.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 754 instances
* *State Mutation (weighted view):* 2385
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2236`, `structural_boundaries: 485`, `args: 379`, `func_start: 112`
* *Risk/State:* `state_mutation: 877`, `planned_debt: 20`, `fragile_debt: 7`
* *Architecture:* `api: 83`, `import: 14`
* *Defense:* `safety: 3`, `doc: 4`, `test: 2`, `immutability_locks: 200`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.065
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.045
  * `Imports (Out-Degree: 44):` engine.h, project_settings.h, core_constants.h, file_access.h, resource_loader.h, class_db.h, script_language.h, hash_map.h...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `servers/rendering/rendering_device.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.237)
- **Top Global Matches:** file_cluster_4: 6.237, file_cluster_6: 10.669, file_cluster_15: 11.915
- **Magnitude:** 7009.86 | **LOC:** 9463 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 29.4%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **15**; blast radius 0.129; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 93.0403% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RenderingDevice::uniform_set_create` **(Many-Argument Workhorses)** (Impact: 265.3)
  * `RenderingDevice::_render_pass_create` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* /*********************/ /**** FRAMEBUFFER ****/ /*********************/
  * `RenderingDevice::texture_create` **(Many-Argument Workhorses)** (Impact: 142.9)
    * *Intent:* /*****************/ /**** TEXTURE ****/ /*****************/
  * `RenderingDevice::initialize` **(Many-Argument Workhorses)** (Impact: 95.3)
  * `RenderingDevice::draw_list_begin` **(Many-Argument Workhorses)** (Impact: 82.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 925 instances
* *State Mutation (weighted view):* 3315
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1335`, `structural_boundaries: 388`, `args: 1252`, `func_start: 273`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1465`, `dead_code: 4`, `planned_debt: 1`, `fragile_debt: 7`, `unreferenced_by_name: 138`
* *Architecture:* `import: 15`
* *Defense:* `safety: 23`, `doc: 67`, `sync_locks: 21`, `immutability_locks: 264`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.094647
  * `Imports (Out-Degree: 39):` engine.h, project_settings.h, dir_access.h, file_access.h, class_db.h, os.h, profiling.h, fixed_vector.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `scene/gui/tree.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.417)
- **Top Global Matches:** file_cluster_4: 7.417, file_cluster_15: 9.317, file_cluster_16: 10.691
- **Magnitude:** 6935.4 | **LOC:** 7477 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 14.8%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **22**; blast radius 0.125; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (82.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 99.6923% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Tree::draw_item` **(Many-Argument Workhorses)** (Impact: 575.7)
  * `Tree::propagate_mouse_event` **(Many-Argument Workhorses)** (Impact: 335.4)
  * `Tree::gui_input` **(Compute Cores)** (Impact: 333.2)
  * `Tree::_notification` **(Many-Argument Workhorses)** (Impact: 259.9)
  * `Tree::_find_item_at_pos` **(Many-Argument Workhorses)** (Impact: 224.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 921 instances
* *State Mutation (weighted view):* 2877
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1756`, `structural_boundaries: 536`, `args: 734`, `func_start: 325`
* *Risk/State:* `state_mutation: 1035`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 2`, `unreferenced_by_name: 99`
* *Architecture:* `import: 22`
* *Defense:* `doc: 5`, `immutability_locks: 291`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.125
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.048381
  * `Imports (Out-Degree: 44):` climits, project_settings.h, input.h, math_funcs.h, callable_mp.h, class_db.h, keyboard.h, os.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `scene/resources/animation.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.58)
- **Top Global Matches:** file_cluster_6: 6.58, file_cluster_4: 12.233, file_cluster_8: 13.532
- **Magnitude:** 6879.74 | **LOC:** 6559 | **CtrlFlow:** 31.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **4**; blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.2%)
- **Documentation Coverage:** 96.9697% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Animation::track_get_key_indices_in_range` **(Many-Argument Workhorses)** (Impact: 489.5)
  * `Animation::cubic_interpolate_in_time_variant` **(Many-Argument Workhorses)** (Impact: 262.3)
  * `Animation::_interpolate` **(Many-Argument Workhorses)** (Impact: 258.9)
  * `Animation::_set` **(Many-Argument Workhorses)** (Impact: 218.8)
    * *Intent:* /* EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF */ /* MERCHANTABILITY, FITNESS...
  * `Animation::track_find_key` **(Many-Argument Workhorses)** (Impact: 217.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 792 instances
* *State Mutation (weighted view):* 2494
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1703`, `structural_boundaries: 519`, `args: 334`, `func_start: 165`, `class_start: 5`
* *Risk/State:* `state_mutation: 910`, `planned_debt: 4`, `fragile_debt: 1`, `unreferenced_by_name: 61`
* *Architecture:* `import: 4`
* *Defense:* `safety: 1`, `doc: 9`, `immutability_locks: 415`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.052675
  * `Imports (Out-Degree: 29):` animation.compat.inc, animation.h, marshalls.h, class_db.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `scene/resources/visual_shader_nodes.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.941)
- **Top Global Matches:** file_cluster_15: 8.941, file_cluster_11: 9.852, file_cluster_4: 10.004
- **Magnitude:** 6429.04 | **LOC:** 8589 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.057; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.0%)
- **Documentation Coverage:** 92.204% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisualShaderNodeTexture::generate_code` **(Many-Argument Workhorses)** (Impact: 153.6)
  * `get_sampler_hint` **(Many-Argument Workhorses)** (Impact: 151.2)
    * *Intent:* //////////////
  * `VisualShaderNodeVectorOp::generate_code` **(Many-Argument Workhorses)** (Impact: 87.2)
  * `VisualShaderNodeIntOp::generate_code` **(Many-Argument Workhorses)** (Impact: 76.3)
  * `VisualShaderNodeUIntOp::generate_code` **(Many-Argument Workhorses)** (Impact: 76.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 522 instances
* *State Mutation (weighted view):* 1772
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1555`, `structural_boundaries: 1332`, `args: 1218`, `func_start: 1039`
* *Risk/State:* `state_mutation: 728`, `fragile_debt: 3`, `unreferenced_by_name: 867`
* *Architecture:* `import: 5`
* *Defense:* `doc: 84`, `immutability_locks: 982`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.057
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000145
  * `Imports (Out-Degree: 16):` class_db.h, os.h, rendering_server.h, visual_shader_nodes.compat.inc, visual_shader_nodes.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `modules/gdscript/gdscript_parser.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.776)
- **Top Global Matches:** file_cluster_8: 7.776, file_cluster_6: 9.961, file_cluster_4: 18.175
- **Magnitude:** 6285.94 | **LOC:** 6541 | **CtrlFlow:** 34.6% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.6%), Guard Balance (formerly Safety Score) (71.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GDScriptParser::export_annotations` **(Many-Argument Workhorses)** (Impact: 240.7)
  * `GDScriptParser::DataType::to_property_info` **(Compute Cores)** (Impact: 153.8)
  * `_process_doc_line` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `GDScriptParser::parse_statement` **(I/O & Config Routines)** (Impact: 101.0)
  * `GDScriptParser::parse_class_body` **(Compute Cores)** (Impact: 97.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 795 instances
* *State Mutation (weighted view):* 2540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1900`, `structural_boundaries: 423`, `args: 639`, `func_start: 177`, `class_start: 1`
* *Risk/State:* `state_mutation: 950`, `planned_debt: 8`, `fragile_debt: 10`
* *Architecture:* `api: 116`, `import: 11`
* *Defense:* `safety: 15`, `doc: 4`, `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.044996
  * `Imports (Out-Degree: 28):` project_settings.h, resource_loader.h, math_defs.h, class_db.h, string_builder.h, editor_settings.h, gdscript.h, gdscript_parser.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `drivers/vulkan/rendering_device_driver_vulkan.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.249)
- **Top Global Matches:** file_cluster_4: 6.249, file_cluster_6: 9.078, file_cluster_15: 12.788
- **Magnitude:** 6222.52 | **LOC:** 7438 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 26.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.049; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.0%)
- **Documentation Coverage:** 90.8602% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RenderingDeviceDriverVulkan::shader_create_from_container` **(Many-Argument Workhorses)** (Impact: 186.6)
  * `RenderingDeviceDriverVulkan::render_pipeline_create` **(Many-Argument Workhorses)** (Impact: 159.5)
  * `RenderingDeviceDriverVulkan::uniform_set_create` **(Many-Argument Workhorses)** (Impact: 154.1)
  * `RenderingDeviceDriverVulkan::swap_chain_resize` **(Many-Argument Workhorses)** (Impact: 115.8)
  * `RenderingDeviceDriverVulkan::_check_device_capabilities` **(I/O & Config Routines)** (Impact: 92.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 916 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 3662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1024`, `structural_boundaries: 355`, `args: 670`, `func_start: 185`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 1`, `state_mutation: 1830`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 8`, `unreferenced_by_name: 174`
* *Architecture:* `import: 12`
* *Defense:* `safety: 148`, `doc: 80`, `sync_locks: 21`, `immutability_locks: 390`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000145
  * `Imports (Out-Degree: 24):` engine.h, project_settings.h, file_access.h, os.h, fixed_vector.h, vulkan_hooks.h, java_godot_wrapper.h, os_android.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `editor/editor_node.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.24)
- **Top Global Matches:** file_cluster_4: 8.24, file_cluster_6: 11.494, file_cluster_15: 13.693
- **Magnitude:** 5999.3 | **LOC:** 9612 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 32.7%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **156**; blast radius 0.147; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (87.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EditorNode::_menu_option_confirm` **(Many-Argument Workhorses)** (Impact: 451.6)
  * `EditorNode::_edit_current` **(Many-Argument Workhorses)** (Impact: 128.1)
  * `EditorNode::_notification` **(Compute Cores)** (Impact: 125.0)
  * `EditorNode::load_scene` **(Many-Argument Workhorses)** (Impact: 116.6)
  * `EditorNode::_dialog_action` **(Compute Cores)** (Impact: 114.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 573 instances
* *State Mutation (weighted view):* 1907
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2000`, `structural_boundaries: 527`, `args: 1114`, `func_start: 300`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 761`, `dead_code: 3`, `planned_debt: 8`, `fragile_debt: 7`, `unreferenced_by_name: 212`
* *Architecture:* `import: 156`
* *Defense:* `safety: 1`, `doc: 4`, `sync_locks: 2`, `immutability_locks: 322`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.065911
  * `Imports (Out-Degree: 227):` engine.h, project_settings.h, gdextension_manager.h, input.h, config_file.h, file_access.h, image.h, resource_importer.h...
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `platform/linuxbsd/x11/display_server_x11.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.921)
- **Top Global Matches:** file_cluster_4: 7.921, file_cluster_6: 8.718, file_cluster_15: 14.928
- **Magnitude:** 5877.62 | **LOC:** 7571 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 38.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **43**; blast radius 0.046; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.0%), Debt Markers (formerly Tech Debt) (89.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.9744% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DisplayServerX11::DisplayServerX11` **(Many-Argument Workhorses)** (Impact: 549.5)
  * `DisplayServerX11::process_events` **(I/O & Config Routines)** (Impact: 284.2)
  * `DisplayServerX11::_handle_key_event` **(Many-Argument Workhorses)** (Impact: 207.8)
  * `DisplayServerX11::_create_window` **(Many-Argument Workhorses)** (Impact: 127.5)
  * `DisplayServerX11::screen_get_usable_rect` **(Many-Argument Workhorses)** (Impact: 119.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 767 instances
* *State Mutation (weighted view):* 2477
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1577`, `structural_boundaries: 364`, `args: 266`, `func_start: 194`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 943`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 183`
* *Architecture:* `import: 43`
* *Defense:* `safety: 5`, `doc: 5`, `immutability_locks: 213`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 57):` XKBlib.h, Xatom.h, Xutil.h, Xext.h, Xinerama.h, Xrender.h, shape.h, climits...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `drivers/d3d12/rendering_device_driver_d3d12.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.431)
- **Top Global Matches:** file_cluster_6: 6.431, file_cluster_4: 7.916, file_cluster_15: 15.583
- **Magnitude:** 5756.7 | **LOC:** 6395 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 47.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.05; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (94.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (79.4%)
- **Documentation Coverage:** 90.0524% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RenderingDeviceDriverD3D12::render_pipeline_create` **(Many-Argument Workhorses)** (Impact: 164.2)
  * `RenderingDeviceDriverD3D12::_resource_transition_batch` **(Many-Argument Workhorses)** (Impact: 150.1)
  * `RenderingDeviceDriverD3D12::uniform_set_create` **(Many-Argument Workhorses)** (Impact: 139.8)
    * *Intent:* /*********************/ /**** UNIFORM SET ****/ /*********************/
  * `RenderingDeviceDriverD3D12::texture_create` **(Many-Argument Workhorses)** (Impact: 124.4)
  * `RenderingDeviceDriverD3D12::_texture_create_shared_from_slice` **(Many-Argument Workhorses)** (Impact: 111.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 764 instances
* *State Mutation (weighted view):* 2639
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1174`, `structural_boundaries: 295`, `args: 341`, `func_start: 190`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 1111`, `dead_code: 1`, `planned_debt: 6`, `unreferenced_by_name: 180`
* *Architecture:* `import: 12`
* *Defense:* `doc: 71`, `sync_locks: 17`, `immutability_locks: 266`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.05
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000145
  * `Imports (Out-Degree: 22):` pix3.h, engine.h, project_settings.h, os.h, d3d12_hooks.h, godot_d3d12ma.h, godot_nir.h, rendering_context_driver_d3d12.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `scene/resources/visual_shader.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.167)
- **Top Global Matches:** file_cluster_4: 9.167, file_cluster_15: 11.167, file_cluster_16: 12.323
- **Magnitude:** 5721.38 | **LOC:** 5665 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 22.2%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Complexity Load (formerly Cognitive Load) (86.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.3416% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisualShader::_write_node` **(Many-Argument Workhorses)** (Impact: 1039.5)
  * `VisualShader::_update_shader` **(I/O & Config Routines)** (Impact: 173.4)
  * `VisualShaderNode::set_input_port_default_value` **(Many-Argument Workhorses)** (Impact: 166.8)
  * `VisualShaderNodeParameter::get_warning` **(Compute Cores)** (Impact: 96.5)
  * `VisualShader::_set` **(Compute Cores)** (Impact: 96.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 698 instances
* *State Mutation (weighted view):* 2223
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1327`, `structural_boundaries: 506`, `args: 443`, `func_start: 322`
* *Risk/State:* `state_mutation: 827`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 217`
* *Architecture:* `import: 10`
* *Defense:* `doc: 41`, `immutability_locks: 364`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000462
  * `Imports (Out-Degree: 26):` engine.h, callable_mp.h, class_db.h, rb_map.h, variant_utility.h, visual_shader_nodes.h, visual_shader_particle_nodes.h, rendering_server.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `core/string/ustring.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.669)
- **Top Global Matches:** file_cluster_4: 7.669, file_cluster_6: 11.137, file_cluster_15: 13.236
- **Magnitude:** 5687.96 | **LOC:** 5832 | **CtrlFlow:** 32.0% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **680** in-repo importer(s); it depends on **15**; blast radius 6.162; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.3%), Debt Markers (formerly Tech Debt) (87.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.6285% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `String::sprintf` **(Many-Argument Workhorses)** (Impact: 315.5)
    * *Intent:* // sprintf is implemented in GDScript via: // "fish %s pie" % "frog" // "fish %s %d pie" % ["frog", ...
  * `_xml_unescape` **(Many-Argument Workhorses)** (Impact: 153.7)
  * `String::append_utf8` **(Many-Argument Workhorses)** (Impact: 138.3)
  * `built_in_strtod` **(Many-Argument Workhorses)** (Impact: 80.1)
  * `String::append_utf16` **(Many-Argument Workhorses)** (Impact: 74.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 839 instances
* *State Mutation (weighted view):* 2569
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1486`, `structural_boundaries: 569`, `args: 311`, `func_start: 250`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 891`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 135`
* *Architecture:* `import: 15`
* *Defense:* `doc: 11`, `immutability_locks: 560`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.162
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.180119
  * `Imports (Out-Degree: 21):` crypto_core.h, ip_address.h, color.h, math_funcs.h, object.h, os.h, print_string.h, string_name.h...
  * `Imported By (In-Degree: 680):` (Excluded from Brief to save tokens)

### `servers/rendering/renderer_rd/storage_rd/texture_storage.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.099)
- **Top Global Matches:** file_cluster_4: 6.099, file_cluster_15: 10.043, file_cluster_16: 11.33
- **Magnitude:** 5680.42 | **LOC:** 4956 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **8**; blast radius 0.08; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.6%), Complexity Load (formerly Cognitive Load) (90.9%), Guard Balance (formerly Safety Score) (86.2%)
- **Documentation Coverage:** 98.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TextureStorage::_validate_texture_format` **(Many-Argument Workhorses)** (Impact: 311.8)
  * `TextureStorage::texture_create_from_native_handle` **(Many-Argument Workhorses)** (Impact: 288.9)
    * *Intent:* // Note: We make some big assumptions about format and usage. If developers need more control, // th...
  * `TextureStorage::_texture_format_from_rd` **(Many-Argument Workhorses)** (Impact: 208.5)
  * `TextureStorage::texture_drawable_blit_rect` **(Many-Argument Workhorses)** (Impact: 70.3)
    * *Intent:* // Output textures in p_textures must ALL BE THE SAME SIZE
  * `TextureStorage::canvas_texture_get_info` **(Many-Argument Workhorses)** (Impact: 60.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1057 instances
* *State Mutation (weighted view):* 3665
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 780`, `structural_boundaries: 200`, `args: 272`, `func_start: 162`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 1551`, `dead_code: 1`, `planned_debt: 7`, `fragile_debt: 1`, `unreferenced_by_name: 161`
* *Architecture:* `import: 8`
* *Defense:* `doc: 7`, `immutability_locks: 87`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.08
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.06418
  * `Imports (Out-Degree: 28):` engine.h, copy_effects.h, framebuffer_cache_rd.h, renderer_scene_render_rd.h, material_storage.h, uniform_set_cache_rd.h, rendering_server_globals.h, texture_storage.h
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `editor/shader/visual_shader_editor_plugin.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.846)
- **Top Global Matches:** file_cluster_4: 7.846, file_cluster_6: 9.771, file_cluster_15: 14.187
- **Magnitude:** 5674.78 | **LOC:** 8538 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 16.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **53**; blast radius 0.046; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (83.1%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.0%)
- **Documentation Coverage:** 97.0339% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisualShaderGraphPlugin::add_node` **(Many-Argument Workhorses)** (Impact: 426.6)
  * `VisualShaderEditor::_add_node` **(Many-Argument Workhorses)** (Impact: 224.7)
  * `VisualShaderEditor::_update_options_menu` **(I/O & Config Routines)** (Impact: 87.2)
  * `VisualShaderEditor::_graph_gui_input` **(Compute Cores)** (Impact: 83.6)
  * `VisualShaderEditor::_dup_paste_nodes` **(Many-Argument Workhorses)** (Impact: 77.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 538 instances
* *State Mutation (weighted view):* 2342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1440`, `structural_boundaries: 413`, `args: 1524`, `func_start: 236`, `class_start: 5`
* *Risk/State:* `state_mutation: 1266`, `dead_code: 3`, `planned_debt: 19`, `unreferenced_by_name: 98`
* *Architecture:* `api: 4`, `import: 53`
* *Defense:* `doc: 27`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 81):` project_settings.h, input.h, resource_loader.h, resource_saver.h, math_defs.h, callable_mp.h, class_db.h, keyboard.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `modules/gdscript/gdscript_editor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.215)
- **Top Global Matches:** file_cluster_8: 8.215, file_cluster_6: 9.739, file_cluster_4: 17.846
- **Magnitude:** 5511.36 | **LOC:** 4649 | **CtrlFlow:** 37.1% | **Authorship Centralization:** 20.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **19**; blast radius 0.048; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%)
- **Documentation Coverage:** 49.0196% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_list_call_arguments` **(Many-Argument Workhorses)** (Impact: 385.6)
  * `_guess_expression_type` **(Many-Argument Workhorses)** (Impact: 365.9)
  * `_find_identifiers_in_base` **(Many-Argument Workhorses)** (Impact: 267.8)
  * `_guess_identifier_type` **(Many-Argument Workhorses)** (Impact: 218.2)
  * `_lookup_symbol_from_base` **(Many-Argument Workhorses)** (Impact: 213.7)
    * *Intent:* #ifdef TOOLS_ENABLED
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 753 instances
* *State Mutation (weighted view):* 2350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1500`, `structural_boundaries: 255`, `args: 147`, `func_start: 72`, `class_start: 2`
* *Risk/State:* `state_mutation: 844`, `planned_debt: 10`, `fragile_debt: 1`
* *Architecture:* `api: 30`, `import: 19`
* *Defense:* `safety: 3`, `doc: 6`, `immutability_locks: 341`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000145
  * `Imports (Out-Degree: 44):` engine.h, project_settings.h, core_constants.h, file_access.h, resource_loader.h, expression.h, class_db.h, container_type_validate.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `servers/rendering/renderer_rd/forward_clustered/render_forward_clustered.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.754)
- **Top Global Matches:** file_cluster_6: 6.754, file_cluster_4: 9.078, file_cluster_15: 16.877
- **Magnitude:** 5444.92 | **LOC:** 5202 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.048; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.5%)
- **Documentation Coverage:** 92.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RenderForwardClustered::_render_scene` **(Many-Argument Workhorses)** (Impact: 477.9)
  * `RenderForwardClustered::_setup_render_pass_uniform_set` **(Many-Argument Workhorses)** (Impact: 305.0)
  * `RenderForwardClustered::_fill_render_list` **(Many-Argument Workhorses)** (Impact: 299.8)
  * `RenderForwardClustered::_render_list_template` **(Many-Argument Workhorses)** (Impact: 256.1)
    * *Intent:* /// RENDERING ///
  * `RenderForwardClustered::_pre_opaque_render` **(Many-Argument Workhorses)** (Impact: 132.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 708 instances
* *State Mutation (weighted view):* 2536
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1089`, `structural_boundaries: 131`, `args: 351`, `func_start: 106`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 1120`, `dead_code: 4`, `fragile_debt: 2`, `unreferenced_by_name: 93`
* *Architecture:* `import: 11`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 135`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.048
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000145
  * `Imports (Out-Degree: 35):` project_settings.h, render_forward_clustered.h, fog.h, framebuffer_cache_rd.h, light_storage.h, mesh_storage.h, particles_storage.h, texture_storage.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `editor/editor_undo_redo_manager.h` (CPP) | Magnitude: 30.9 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 83, pointers: 36, structural_boundaries: 29, args: 28
- `platform/macos/editor/embedded_game_view_plugin.mm` (OBJECTIVE-C) | Magnitude: 42.44 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 75, pointers: 39, func_start: 18, bitwise_ops: 18
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/Methods.cs` (CSHARP) | Magnitude: 0.01 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 15, args: 5, func_start: 5, encapsulation: 5
- `platform/macos/native_menu_macos.h` (OBJECTIVE-C) | Magnitude: 70.46 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: immutability_locks: 147, bitwise_ops: 113, pointers: 112, indent_tabs: 100
- `core/templates/command_queue_mt.h` (CPP) | Magnitude: 105.04 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 176, structural_boundaries: 70, pointers: 32, args: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/core/templates/test_self_list.cpp` (CPP) | Magnitude: 27.38 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 27, pointers: 14, core_var_decl: 7, state_mutation: 6
- `modules/mono/glue/GodotSharp/GodotSharp/Core/NativeInterop/NativeVariantPtrArgs.cs` (CSHARP) | Magnitude: 7.48 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 5, core_var_decl: 4, design_snake_case: 4
- `platform/android/java/editor/src/main/java/org/godotengine/editor/buildprovider/GradleBuildProvider.kt` (KOTLIN) | Magnitude: 20.42 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 14, args: 8, api: 6
- `modules/mono/editor/GodotTools/GodotTools.IdeMessaging.CLI/ForwarderMessageHandler.cs` (CSHARP) | Magnitude: 54.44 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 31, concurrency: 27, args: 8
- `modules/mono/editor/GodotTools/GodotTools/Internals/Internal.cs` (CSHARP) | Magnitude: 125.48 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 108, args: 50, func_start: 50, api: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `modules/mp3/resource_importer_mp3.cpp` (CPP) | Magnitude: 26.82 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 35, pointers: 27, immutability_locks: 18, structural_boundaries: 15
- `editor/project_upgrade/project_upgrade_tool.cpp` (CPP) | Magnitude: 55.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 71, pointers: 42, args: 27, import: 14
- `tests/signal_watcher.h` (CPP) | Magnitude: 2.64 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: pointers: 21, indent_tabs: 16, structural_boundaries: 12, args: 12
- `editor/script/script_editor_base.h` (CPP) | Magnitude: 74.54 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 158, structural_boundaries: 124, pointers: 62, args: 31
- `scene/gui/option_button.h` (CPP) | Magnitude: 15.64 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 87, immutability_locks: 45, structural_boundaries: 42, args: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `platform/android/java/lib/src/main/java/org/godotengine/godot/input/GodotEditText.java` (JAVA) | Magnitude: 206.98 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 209, structural_boundaries: 60, state_mutation: 37, core_var_decl: 37
- `modules/multiplayer/multiplayer_debugger.h` (CPP) | Magnitude: 7.72 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 73, structural_boundaries: 24, args: 20, pointers: 16
- `drivers/apple_embedded/godot_view_controller.mm` (OBJECTIVE-C) | Magnitude: 198.0 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 187, branch: 61, explicit_casts: 38, structural_boundaries: 33
- `platform/windows/drop_target_windows.h` (CPP) | Magnitude: 3.62 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 18, pointers: 14, args: 8, safety: 7
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/VerityTreeBuilder.java` (JAVA) | Magnitude: 101.4 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 53, core_var_decl: 47, design_camel_case: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `modules/mono/glue/GodotSharp/GodotSharp/Core/GodotUnhandledExceptionEvent.cs` (CSHARP) | Magnitude: 9.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 6, import: 3, args: 2
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/ScriptMethodsGeneratorTests.cs` (CSHARP) | Magnitude: 12.24 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, concurrency: 6, api: 3
- `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/IHandshake.cs` (CSHARP) | Magnitude: 6.68 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, api: 3, args: 2
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/Sources/ExportDiagnostics_GD0109.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 4, decorators: 2, import: 2, indent_spaces: 2
- `modules/mono/editor/GodotTools/GodotTools.IdeMessaging/ILogger.cs` (CSHARP) | Magnitude: 14.04 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, api: 6, args: 5, func_start: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `misc/scripts/make_icons.sh` (SHELL) | Magnitude: 0.44 | Delta: **0.054** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 3, indent_spaces: 3, safety_bypasses: 2, branch: 1
- `modules/mono/editor/editor_internal_calls.h` (CPP) | Magnitude: 12.6 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, safety_bypasses: 1
- `modules/mono/glue/runtime_interop.h` (CPP) | Magnitude: 12.6 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `servers/physics_3d/physics_server_3d_dummy.h` (CPP) | Magnitude: 675.74 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 505, indent_tabs: 266, api: 254, func_start: 252
- `modules/jolt_physics/register_types.cpp` (CPP) | Magnitude: 8.7 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 14, import: 7, structural_boundaries: 5, args: 4
- `editor/shader/editor_native_shader_source_visualizer.cpp` (CPP) | Magnitude: 28.86 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 85, pointers: 61, args: 39, import: 10
- `scene/3d/sprite_3d.cpp` (CPP) | Magnitude: 1023.02 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1002, branch: 223, args: 197, pointers: 195
- `servers/navigation_3d/navigation_server_3d_dummy.h` (CPP) | Magnitude: 426.0 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 162, api: 161, indent_tabs: 161, func_start: 160

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/GeneratedSources/ScriptBoilerplate_ScriptSerialization.generated.cs` (CSHARP) | Magnitude: 0.01 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 5, branch: 2, args: 2
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/ByteArrayDataSink.java` (JAVA) | Magnitude: 102.02 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 162, structural_boundaries: 57, branch: 20, args: 18
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Tests/TestData/GeneratedSources/ExportDiagnostics_GD0111_ScriptProperties.generated.cs` (CSHARP) | Magnitude: 0.06 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 74, doc: 34, structural_boundaries: 19, state_mutation: 13
- `platform/android/java/editor/src/main/java/com/android/apksig/internal/util/ByteBufferUtils.java` (JAVA) | Magnitude: 5.0 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 5, args: 2, func_start: 2
- `modules/mono/editor/GodotTools/GodotTools/Inspector/InspectorPlugin.cs` (CSHARP) | Magnitude: 38.1 | Delta: **0.12** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, structural_boundaries: 16, branch: 14, core_var_decl: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `servers/physics_2d/physics_server_2d_dummy.h` (CPP) | Magnitude: 515.06 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 387, indent_tabs: 207, api: 195, func_start: 193
- `platform/linuxbsd/x11/key_mapping_x11.h` (CPP) | Magnitude: 8.72 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 19, structural_boundaries: 12, args: 10, func_start: 5
- `modules/svg/register_types.cpp` (CPP) | Magnitude: 10.42 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 18, structural_boundaries: 6, branch: 4, doc: 4
- `core/string/alt_codes.h` (CPP) | Magnitude: 15.74 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 32, doc: 4, structural_boundaries: 2, globals: 2
- `servers/rendering/renderer_rd/effects/sort_effects.h` (CPP) | Magnitude: 16.52 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 17, structural_boundaries: 5, doc: 4, class_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators/Common.cs` (CSHARP) | Magnitude: 42.14 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 202, structural_boundaries: 35, safety: 32, api: 23
- `tests/scene/test_camera_3d.cpp` (CPP) | Magnitude: 75.36 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 240, pointers: 186, args: 130, test: 77
- `servers/xr/xr_controller_tracker.h` (CPP) | Magnitude: 3.32 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 5, indent_tabs: 5, import: 2, structural_boundaries: 1
- `tests/core/math/test_geometry_2d.cpp` (CPP) | Magnitude: 319.1 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 685, args: 336, test: 217, state_mutation: 165
- `modules/camera/camera_win.h` (CPP) | Magnitude: 3.28 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 4, indent_tabs: 3, structural_boundaries: 2, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `scene/3d/lightmap_gi.cpp` (CPP) | Magnitude: 1668.84 | Delta: **0.055** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 1302, pointers: 348, branch: 322, state_mutation: 290
- `modules/jolt_physics/objects/jolt_area_3d.cpp` (CPP) | Magnitude: 334.66 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 325, pointers: 124, branch: 99, structural_boundaries: 71
- `modules/mono/editor/GodotTools/GodotTools/Ides/GodotIdeManager.cs` (CSHARP) | Magnitude: 163.5 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 185, branch: 44, structural_boundaries: 37, args: 21
- `scene/main/timer.cpp` (CPP) | Magnitude: 143.26 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 133, branch: 45, args: 38, structural_boundaries: 25
- `modules/openxr/extensions/spatial_entities/openxr_spatial_plane_tracking.cpp` (CPP) | Magnitude: 546.24 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 484, pointers: 151, branch: 113, state_mutation: 111

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/compatibility_test/run_compatibility_test.py` (PYTHON) | Magnitude: 92.44 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 92, structural_boundaries: 32, branch: 27, core_var_decl: 19
- `drivers/apple_embedded/rendering_context_driver_vulkan_apple_embedded.h` (OBJECTIVE-C) | Magnitude: 15.34 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 7, doc: 4, immutability_locks: 4, macros: 3
- `platform/macos/rendering_context_driver_vulkan_macos.h` (OBJECTIVE-C) | Magnitude: 15.34 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 7, doc: 4, immutability_locks: 4, macros: 3
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Sample/Generic1T.cs` (CSHARP) | Magnitude: 15.16 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, class_start: 1, safety_bypasses: 1
- `modules/mono/editor/Godot.NET.Sdk/Godot.SourceGenerators.Sample/Generic2T.cs` (CSHARP) | Magnitude: 15.16 | Delta: **0.147** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 4, structural_boundaries: 2, class_start: 1, safety_bypasses: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `modules/theora/editor/movie_writer_ogv.cpp` (CPP) | Magnitude: 306.48 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 275, pointers: 110, state_mutation: 76, branch: 69
- `modules/navigation_3d/3d/nav_map_builder_3d.cpp` (CPP) | Magnitude: 307.32 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 269, pointers: 106, state_mutation: 98, branch: 50
- `modules/navigation_2d/2d/nav_map_builder_2d.cpp` (CPP) | Magnitude: 306.2 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 267, pointers: 106, state_mutation: 97, branch: 50
- `editor/project_manager/project_dialog.cpp` (CPP) | Magnitude: 643.7 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 881, pointers: 373, branch: 239, args: 217
- `scene/main/shader_globals_override.cpp` (CPP) | Magnitude: 343.68 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 214, branch: 90, state_mutation: 63, pointers: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/test_tools.h` (CPP) | Magnitude: 13.12 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 17, pointers: 9, structural_boundaries: 4, func_start: 4
- `platform/android/java/lib/build.gradle` (GROOVY) | Magnitude: 42.66 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 133, core_var_decl: 28, design_camel_case: 23, state_mutation: 21
- `drivers/windows/thread_windows.cpp` (CPP) | Magnitude: 10.2 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 8, core_var_decl: 5, structural_boundaries: 4, doc: 4
- `core/io/stream_peer_gzip.h` (CPP) | Magnitude: 16.54 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 19, pointers: 11, structural_boundaries: 10, args: 9
- `platform/macos/embedded_debugger.h` (CPP) | Magnitude: 17.56 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 17, pointers: 16, args: 11, immutability_locks: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `core/crypto/hashing_context.cpp` (CPP) | Magnitude: 0.88 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 80, branch: 31, pointers: 18, structural_boundaries: 12
- `modules/gdscript/language_server/scene_cache.cpp` (CPP) | Magnitude: 108.56 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 104, branch: 34, pointers: 22, state_mutation: 16

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `editor/editor_node.cpp` -> Churn: **100.0%** | Cog Load: 75.216% | Debt: 87.3524%
- `editor/scene/3d/node_3d_editor_plugin.cpp` -> Churn: **97.33%** | Cog Load: 90.1735% | Debt: 59.815%
- `editor/inspector/editor_inspector.cpp` -> Churn: **86.56%** | Cog Load: 92.0011% | Debt: 87.4165%
- `editor/inspector/editor_properties.cpp` -> Churn: **86.08%** | Cog Load: 72.6925% | Debt: 99.5354%
- `editor/docks/editor_dock_manager.cpp` -> Churn: **85.18%** | Cog Load: 43.0622% | Debt: 88.6508%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `core/variant/variant_parser.cpp` -> **StarryWorm** (100.0% isolated ownership) | Magnitude: 3583.22
- `servers/rendering/renderer_canvas_cull.cpp` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 2736.1
- `core/io/marshalls.cpp` -> **Mikael Hermansson** (100.0% isolated ownership) | Magnitude: 2717.52
- `editor/scene/2d/tiles/tile_data_editors.cpp` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 2531.48
- `core/math/convex_hull.cpp` -> **Rémi Verschelde** (100.0% isolated ownership) | Magnitude: 2425.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `core/os/memory.h` -> **Severity: 16.724** (Embedded: 0.209 * Error Risk: 80.0%)
- `core/string/ustring.cpp` -> **Severity: 13.529** (Embedded: 0.1801 * Error Risk: 75.1136%)
- `core/string/print_string.cpp` -> **Severity: 13.4** (Embedded: 0.1591 * Error Risk: 84.2137%)
- `core/os/memory.cpp` -> **Severity: 12.691** (Embedded: 0.1586 * Error Risk: 80.0%)
- `core/templates/list.h` -> **Severity: 12.507** (Embedded: 0.1587 * Error Risk: 78.8141%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `core/typedefs.h` -> **Severity: 8378.5** (Blast Radius: 83.785 * Doc Risk: 100.0%)
- `core/os/mutex.cpp` -> **Severity: 3656.8** (Blast Radius: 36.568 * Doc Risk: 100.0%)
- `core/os/mutex.h` -> **Severity: 3406.8** (Blast Radius: 34.068 * Doc Risk: 100.0%)
- `core/error/error_macros.h` -> **Severity: 1865.8** (Blast Radius: 18.658 * Doc Risk: 100.0%)
- `core/variant/variant.h` -> **Severity: 1247.8** (Blast Radius: 12.478 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 440 literal sites + 49 sites through wrappers = 489
- **`memory_alloc`:** 674 literal sites + 1807 sites through wrappers = 2481
- **`panics_and_aborts`:** 1600 literal sites + 22 sites through wrappers = 1622

- `memnew` (macro, memory_alloc, primitive): 1055 call sites in 181 files -- `core/os/memory.h`
- `SEND_GUI_MOUSE_MOTION_EVENT` (macro, memory_alloc, via instantiate): 243 call sites in 9 files -- `tests/display_server_mock.h`
- `memnew_placement` (macro, memory_alloc, primitive): 213 call sites in 17 files -- `core/os/memory.h`
- `SEND_GUI_MOUSE_BUTTON_EVENT` (macro, memory_alloc, via _CREATE_GUI_MOUSE_EVENT): 128 call sites in 7 files -- `tests/display_server_mock.h`
- `SEND_GUI_MOUSE_BUTTON_RELEASED_EVENT` (macro, memory_alloc, via _CREATE_GUI_MOUSE_EVENT): 96 call sites in 7 files -- `tests/display_server_mock.h`
- `print_error` (function, debug_prints, primitive): 35 call sites in 1 files -- `doc/tools/make_rst.py`
- `make_empty_stylebox` (function, memory_alloc, via memnew): 16 call sites in 1 files -- `scene/theme/default_theme.cpp`
- `SEND_GUI_DOUBLE_CLICK` (macro, memory_alloc, via _CREATE_GUI_MOUSE_EVENT): 14 call sites in 2 files -- `tests/display_server_mock.h`
- `print_warning` (function, debug_prints, primitive): 14 call sites in 1 files -- `doc/tools/make_rst.py`
- `memnew_allocator` (macro, memory_alloc, primitive): 11 call sites in 4 files -- `core/os/memory.h`
- `hasFileId` (function, panics_and_aborts, primitive): 10 call sites in 1 files -- `platform/android/java/lib/src/main/java/org/godotengine/godot/io/file/FileAccessHandler.kt`
- `GLTF_REGISTER_DOCUMENT_EXTENSION` (macro, memory_alloc, via instantiate): 4 call sites in 1 files -- `modules/gltf/register_types.cpp`
*(+32 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 326055 call pairs -- scoped 21.7%, unique 6.9%, ambiguous 47.0%, external 24.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| cpp | 303289 | 21.2% | 7.0% | 49.4% | 22.3% |
| java | 6044 | 36.0% | 1.4% | 16.9% | 45.6% |
| csharp | 5231 | 44.8% | 2.4% | 15.9% | 37.0% |
| objective-c | 4950 | 14.6% | 19.9% | 24.0% | 41.5% |
| python | 3084 | 13.1% | 0.0% | 1.5% | 85.4% |
| kotlin | 1764 | 28.6% | 0.6% | 10.5% | 60.3% |
| javascript | 1316 | 12.1% | 0.0% | 3.7% | 84.2% |
| c | 243 | 12.8% | 18.5% | 41.6% | 27.2% |
| groovy | 91 | 3.3% | 0.0% | 4.4% | 92.3% |
| shell | 42 | 9.5% | 0.0% | 0.0% | 90.5% |

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
