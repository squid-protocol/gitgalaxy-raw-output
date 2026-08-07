# ARCHITECTURAL_BRIEF: flutter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/flutter` |
| **Timestamp** | `2026-08-07T04:36:19.857306+00:00` |
| **Scan Duration** | `30.59s` |
| **Git Branch** | `master` |
| **Git Commit** | `75910740753c13a858bb39c3686afb71675e8dc4` |
| **Git Remote** | `https://github.com/flutter/flutter` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7182 malicious artifacts.

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
| Total Artifacts | 15525 |
| Analyzed Artifacts (Scanned) | 8544 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6981 |
| Total LOC | 914768 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.0% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2414 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 300 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 2887 | 329186 | 33.8% |
| DART | 2630 | 408772 | 30.8% |
| OBJECTIVE-C | 550 | 52542 | 6.4% |
| JSON | 486 | 38754 | 5.7% |
| XML | 405 | 0 | 4.7% |
| JAVA | 307 | 40620 | 3.6% |
| GLSL | 262 | 5623 | 3.1% |
| PYTHON | 216 | 20633 | 2.5% |
| MARKDOWN | 184 | 0 | 2.2% |
| PLAINTEXT | 149 | 1 | 1.7% |
| YAML | 121 | 2714 | 1.4% |
| SWIFT | 100 | 2954 | 1.2% |
| KOTLIN | 68 | 6301 | 0.8% |
| SHELL | 58 | 1990 | 0.7% |
| GROOVY | 35 | 972 | 0.4% |
| RUBY | 19 | 671 | 0.2% |
| JAVASCRIPT | 18 | 679 | 0.2% |
| HTML | 15 | 297 | 0.2% |
| BATCH | 14 | 567 | 0.2% |
| C | 10 | 196 | 0.1% |
| POWERSHELL | 4 | 141 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| CSV | 1 | 1041 | 0.0% |
| TYPESCRIPT | 1 | 32 | 0.0% |
| YACC | 1 | 73 | 0.0% |
| CSS | 1 | 7 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.961`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4156 | 48.6% |
| file_cluster_13 | 2999 | 35.1% |
| file_cluster_0 | 304 | 3.6% |
| file_cluster_4 | 252 | 2.9% |
| file_cluster_16 | 182 | 2.1% |
| file_cluster_2 | 121 | 1.4% |
| file_cluster_17 | 52 | 0.6% |
| file_cluster_15 | 45 | 0.5% |
| file_cluster_9 | 30 | 0.4% |
| file_cluster_11 | 23 | 0.3% |
| file_cluster_7 | 22 | 0.3% |
| file_cluster_12 | 16 | 0.2% |
| file_cluster_6 | 6 | 0.1% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 332 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6981*

**Composition by Extension & Reason:**
- `.dart`: 3673x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 1016 LOC), 2x Excluded (Monolithic Amalgamation: 47919 LOC exceeds safe regex boundaries)
- `.png`: 614x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 232x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 76x Excluded (Unsupported Extension: '.xcworkspacedata'), 32x Excluded (Unsupported Extension: '.entitlements')
- `.tmpl`: 139x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 110x Excluded (Unsupported Extension: '.tmpl'), 13x Unsupported Format (.tmpl)
- `.md`: 251x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 88 LOC)
- `.h`: 175x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcconfig`: 146x Excluded (Unsupported Extension: '.xcconfig'), 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.xcconfig)
- `.yaml`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 134x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 18448 hex tokens in 1647 LOC), 1x Excluded (Embedded Hex Payload: 1174 hex tokens in 1004 LOC)
- `.gni`: 71x Unsupported Format (.gni), 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 109x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 93x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9726 LOC), 1x Excluded (Massive Static Asset Blob: 3898 LOC)
- `.gn`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lockfile`: 54x Excluded (Unsupported Extension: '.lockfile'), 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 69x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 25.1 | 9.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 35.4 | 27.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 7.0 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.9 | 1.5 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 13.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.3 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.2 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 17.7 | 12.5 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `dev/bots/analyze.dart` (Hits: 125)
- `engine/src/flutter/testing/run_tests.py` (Hits: 125)
- `packages/flutter_tools/lib/src/cache.dart` (Hits: 109)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **memory.dart** (`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart`) — 522 inbound connections
2. **string.cc** (`engine/src/flutter/skwasm/string.cc`) — 272 inbound connections
3. **framework.dart** (`packages/flutter/lib/src/widgets/framework.dart`) — 159 inbound connections
4. **basic.dart** (`packages/flutter/lib/src/widgets/basic.dart`) — 98 inbound connections
5. **Log.java** (`engine/src/flutter/shell/platform/android/io/flutter/Log.java`) — 72 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **engine.dart** (`engine/src/flutter/lib/web_ui/lib/src/engine.dart`) — 159 outbound dependencies
2. **TextInputPluginTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/plugin/editing/TextInputPluginTest.java`) — 86 outbound dependencies
3. **FlutterViewTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/FlutterViewTest.java`) — 78 outbound dependencies
4. **FlutterView.java** (`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/FlutterView.java`) — 73 outbound dependencies
5. **theme_data.dart** (`packages/flutter/lib/src/material/theme_data.dart`) — 69 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `sharedDarwinSource` (@ `packages/flutter_tools/lib/src/flutter_manifest.dart`) -> Impact: **797.9** | LOC: 958
- `RelayoutWhenSystemFontsChangeMixin` (@ `packages/flutter/lib/src/rendering/paragraph.dart`) -> Impact: **648.7** | LOC: 1578
- `properties.add` (@ `packages/flutter/lib/src/material/input_decorator.dart`) -> Impact: **647.7** | LOC: 1018
- `TextLayoutMetrics` (@ `packages/flutter/lib/src/rendering/editable.dart`) -> Impact: **566.6** | LOC: 1885
- `visitedNodes.addAll` (@ `packages/flutter/lib/src/semantics/semantics.dart`) -> Impact: **561.1** | LOC: 1453
- `assert` (@ `packages/flutter/lib/src/semantics/semantics.dart`) -> Impact: **559.2** | LOC: 1450
  * *Intent:* /// Whether the semantics tree this node belongs to is attached to a [SemanticsOwner]. /// /// This becomes true during the call to [attach].
- `assert` (@ `packages/flutter/lib/src/rendering/paragraph.dart`) -> Impact: **540.3** | LOC: 1302
- `newChildren.add` (@ `packages/flutter/lib/src/rendering/paragraph.dart`) -> Impact: **537.7** | LOC: 1307
- `TextLayoutMetrics` (@ `packages/flutter/lib/src/rendering/paragraph.dart`) -> Impact: **537.1** | LOC: 1296
- `sendSemanticsUpdate` (@ `packages/flutter/lib/src/semantics/semantics.dart`) -> Impact: **503.6** | LOC: 1531

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/flutter/lib/src/material` | 182 | 44761.94 | 10.82% | 39.75% |
| `packages/flutter/lib/src/widgets` | 185 | 38413.4 | 8.48% | 61.49% |
| `packages/flutter/lib/src/rendering` | 48 | 20081.8 | 7.61% | 78.8% |
| `engine/src/flutter/shell/platform/linux` | 164 | 18801.72 | 40.17% | 60.85% |
| `packages/flutter_tools/lib/src` | 59 | 18102.14 | 23.32% | 61.54% |
| `engine/src/flutter/shell/platform/darwin/ios/framework/Source` | 122 | 16402.84 | 36.56% | 53.06% |
| `packages/flutter_tools/lib/src/commands` | 52 | 13440.5 | 34.38% | 71.38% |
| `engine/src/flutter/shell/platform/windows` | 127 | 13164.48 | 42.22% | 53.05% |
| `engine/src/flutter/shell/platform/darwin/macos/framework/Source` | 97 | 11400.06 | 38.12% | 40.09% |
| `engine/src/flutter/shell/common` | 89 | 10887.8 | 43.55% | 53.38% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `engine/src/flutter/.github/workflows/engine-cp.yml` -> **100.0%** Exposure
- `bin/internal/update_engine_version.sh` -> **100.0%** Exposure
- `dev/checks` -> **100.0%** Exposure
- `dev/tools/gen_keycodes/bin/gen_keycodes` -> **100.0%** Exposure
- `engine/src/flutter/ci/ban_generated_plugin_registrant_java.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `bin/dart` -> **100.0%** Exposure
- `bin/flutter` -> **100.0%** Exposure
- `bin/flutter-dev` -> **100.0%** Exposure
- `bin/internal/content_aware_hash.sh` -> **100.0%** Exposure
- `bin/internal/last_engine_commit.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart` -> **4** Orphaned Functions | **207** Duplicates
- `engine/src/flutter/impeller/toolkit/interop/impeller.cc` -> **171** Orphaned Functions | **4** Duplicates
- `packages/flutter_driver/test/src/real_tests/flutter_driver_test.dart` -> **2** Orphaned Functions | **155** Duplicates
- `engine/src/flutter/shell/platform/common/text_input_model_unittests.cc` -> **0** Orphaned Functions | **154** Duplicates
- `packages/flutter/lib/src/rendering/proxy_box.dart` -> **0** Orphaned Functions | **145** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`engine/src/flutter/impeller/playground/backend/metal/playground_impl_mtl.mm`** -> AI Confidence: **99.48%**
2. **`engine/src/flutter/impeller/renderer/backend/metal/allocator_mtl.mm`** -> AI Confidence: **99.48%**
3. **`engine/src/flutter/impeller/renderer/backend/metal/allocator_mtl_unittests.mm`** -> AI Confidence: **99.48%**
4. **`engine/src/flutter/impeller/renderer/backend/metal/blit_pass_mtl.mm`** -> AI Confidence: **99.48%**
5. **`engine/src/flutter/impeller/renderer/backend/metal/command_buffer_mtl.mm`** -> AI Confidence: **99.48%**
6. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pass_mtl.mm`** -> AI Confidence: **99.48%**
7. **`engine/src/flutter/impeller/renderer/backend/metal/context_mtl.h`** -> AI Confidence: **99.48%**
8. **`engine/src/flutter/impeller/renderer/backend/metal/context_mtl.mm`** -> AI Confidence: **99.48%**
9. **`engine/src/flutter/impeller/renderer/backend/metal/formats_mtl.h`** -> AI Confidence: **99.48%**
10. **`engine/src/flutter/impeller/renderer/backend/metal/pipeline_library_mtl.mm`** -> AI Confidence: **99.48%**
11. **`engine/src/flutter/impeller/renderer/backend/metal/render_pass_mtl.mm`** -> AI Confidence: **99.48%**
12. **`engine/src/flutter/impeller/renderer/backend/metal/surface_mtl.mm`** -> AI Confidence: **99.48%**
13. **`engine/src/flutter/impeller/renderer/backend/metal/texture_mtl.mm`** -> AI Confidence: **99.48%**
14. **`engine/src/flutter/impeller/toolkit/interop/backend/metal/context_mtl.mm`** -> AI Confidence: **99.48%**
15. **`engine/src/flutter/impeller/toolkit/interop/example_mtl.m`** -> AI Confidence: **99.48%**
16. **`engine/src/flutter/shell/gpu/gpu_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
17. **`engine/src/flutter/shell/gpu/gpu_surface_metal_impeller_unittests.mm`** -> AI Confidence: **99.48%**
18. **`engine/src/flutter/shell/gpu/gpu_surface_metal_skia.mm`** -> AI Confidence: **99.48%**
19. **`engine/src/flutter/shell/gpu/gpu_surface_noop.mm`** -> AI Confidence: **99.48%**
20. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinContextMetalSkia.mm`** -> AI Confidence: **99.48%**
21. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinExternalTextureMetal.mm`** -> AI Confidence: **99.48%**
22. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterAppDelegate.mm`** -> AI Confidence: **99.48%**
23. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterDartProject.mm`** -> AI Confidence: **99.48%**
24. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterEmbedderKeyResponder.mm`** -> AI Confidence: **99.48%**
25. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterEngine.mm`** -> AI Confidence: **99.48%**
26. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterMetalLayer.mm`** -> AI Confidence: **99.48%**
27. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformPlugin.mm`** -> AI Confidence: **99.48%**
28. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsController.mm`** -> AI Confidence: **99.48%**
29. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsTest.mm`** -> AI Confidence: **99.48%**
30. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPluginAppLifeCycleDelegate.mm`** -> AI Confidence: **99.48%**
31. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSceneLifeCycle.mm`** -> AI Confidence: **99.48%**
32. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPlugin.mm`** -> AI Confidence: **99.48%**
33. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm`** -> AI Confidence: **99.48%**
34. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterViewController.mm`** -> AI Confidence: **99.48%**
35. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/accessibility_bridge.mm`** -> AI Confidence: **99.48%**
36. **`engine/src/flutter/shell/platform/darwin/ios/ios_context.mm`** -> AI Confidence: **99.48%**
37. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
38. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface_noop.mm`** -> AI Confidence: **99.48%**
39. **`engine/src/flutter/shell/platform/darwin/ios/platform_view_ios.mm`** -> AI Confidence: **99.48%**
40. **`engine/src/flutter/shell/platform/darwin/ios/rendering_api_selection.mm`** -> AI Confidence: **99.48%**
41. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEmbedderExternalTextureTest.mm`** -> AI Confidence: **99.48%**
42. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEmbedderKeyResponder.mm`** -> AI Confidence: **99.48%**
43. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngine.mm`** -> AI Confidence: **99.48%**
44. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardManager.mm`** -> AI Confidence: **99.48%**
45. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformNodeDelegateMac.mm`** -> AI Confidence: **99.48%**
46. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformNodeDelegateMacTest.mm`** -> AI Confidence: **99.48%**
47. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputPlugin.mm`** -> AI Confidence: **99.48%**
48. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputSemanticsObject.mm`** -> AI Confidence: **99.48%**
49. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputSemanticsObjectTest.mm`** -> AI Confidence: **99.48%**
50. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterVSyncWaiter.mm`** -> AI Confidence: **99.48%**
51. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterWindowController.mm`** -> AI Confidence: **99.48%**
52. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterWindowControllerTest.mm`** -> AI Confidence: **99.48%**
53. **`engine/src/flutter/shell/platform/embedder/embedder_external_texture_metal.mm`** -> AI Confidence: **99.48%**
54. **`engine/src/flutter/shell/platform/embedder/embedder_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
55. **`engine/src/flutter/shell/platform/embedder/tests/embedder_metal_unittests.mm`** -> AI Confidence: **99.48%**
56. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_backingstore_producer_metal.mm`** -> AI Confidence: **99.48%**
57. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_metal.mm`** -> AI Confidence: **99.48%**
58. **`engine/src/flutter/shell/testing/tester_context_mtl_factory.mm`** -> AI Confidence: **99.48%**
59. **`engine/src/flutter/testing/test_metal_context.mm`** -> AI Confidence: **99.48%**
60. **`engine/src/flutter/testing/test_metal_surface_impl.mm`** -> AI Confidence: **99.48%**
61. **`engine/src/flutter/txt/src/txt/platform_mac.mm`** -> AI Confidence: **99.48%**
62. **`engine/src/flutter/display_list/effects/dl_color_source_unittests.cc`** -> AI Confidence: **99.48%**
63. **`engine/src/flutter/fml/thread_unittests.cc`** -> AI Confidence: **99.48%**
64. **`engine/src/flutter/lib/ui/painting/paint.cc`** -> AI Confidence: **99.48%**
65. **`engine/src/flutter/shell/common/skia_event_tracer_impl.cc`** -> AI Confidence: **99.48%**
66. **`dev/bots/custom_rules/protect_public_state_subtypes.dart`** -> AI Confidence: **99.48%**
67. **`dev/devicelab/bin/run.dart`** -> AI Confidence: **99.48%**
68. **`dev/tools/localization/bin/gen_localizations.dart`** -> AI Confidence: **99.48%**
69. **`engine/src/flutter/testing/dart/gpu_test.dart`** -> AI Confidence: **99.48%**
70. **`packages/flutter/lib/src/cupertino/text_form_field_row.dart`** -> AI Confidence: **99.48%**
71. **`packages/flutter/lib/src/material/checkbox_list_tile.dart`** -> AI Confidence: **99.48%**
72. **`packages/flutter/lib/src/material/color_scheme.dart`** -> AI Confidence: **99.48%**
73. **`packages/flutter/lib/src/material/switch_list_tile.dart`** -> AI Confidence: **99.48%**
74. **`packages/flutter/lib/src/material/bottom_navigation_bar.dart`** -> AI Confidence: **99.44%**
75. **`packages/flutter/lib/src/material/data_table.dart`** -> AI Confidence: **99.44%**
76. **`packages/flutter/lib/src/material/selectable_text.dart`** -> AI Confidence: **99.44%**
77. **`packages/flutter/lib/src/services/raw_keyboard.dart`** -> AI Confidence: **99.44%**
78. **`engine/src/flutter/lib/web_ui/lib/src/engine/platform_dispatcher.dart`** -> AI Confidence: **99.43%**
79. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_stub/renderer.dart`** -> AI Confidence: **99.43%**
80. **`engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart`** -> AI Confidence: **99.43%**
81. **`packages/flutter/lib/src/material/list_tile_theme.dart`** -> AI Confidence: **99.43%**
82. **`packages/flutter/lib/src/material/text_form_field.dart`** -> AI Confidence: **99.43%**
83. **`packages/flutter/lib/src/material/time_picker_theme.dart`** -> AI Confidence: **99.43%**
84. **`packages/flutter/lib/src/painting/text_style.dart`** -> AI Confidence: **99.43%**
85. **`packages/flutter/lib/src/widgets/icon.dart`** -> AI Confidence: **99.43%**
86. **`packages/flutter/lib/src/material/button_style.dart`** -> AI Confidence: **99.42%**
87. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterAppDelegate.mm`** -> AI Confidence: **99.39%**
88. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterDisplayLink.mm`** -> AI Confidence: **99.39%**
89. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewController.mm`** -> AI Confidence: **99.39%**
90. **`engine/src/flutter/display_list/dl_builder.cc`** -> AI Confidence: **99.39%**
91. **`engine/src/flutter/examples/vulkan_glfw/src/main.cc`** -> AI Confidence: **99.39%**
92. **`engine/src/flutter/fml/logging.cc`** -> AI Confidence: **99.39%**
93. **`engine/src/flutter/shell/common/switches.cc`** -> AI Confidence: **99.39%**
94. **`engine/src/flutter/shell/platform/linux/fl_text_input_handler_test.cc`** -> AI Confidence: **99.39%**
95. **`engine/src/flutter/tools/licenses_cpp/src/license_file_compare.cc`** -> AI Confidence: **99.39%**
96. **`engine/src/flutter/lib/web_ui/lib/src/engine/renderer.dart`** -> AI Confidence: **99.39%**
97. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/paragraph.dart`** -> AI Confidence: **99.39%**
98. **`engine/src/flutter/lib/web_ui/lib/src/engine/text_editing/text_editing.dart`** -> AI Confidence: **99.39%**
99. **`engine/src/flutter/lib/web_ui/test/engine/raw_keyboard_test.dart`** -> AI Confidence: **99.39%**
100. **`packages/flutter/lib/src/cupertino/button.dart`** -> AI Confidence: **99.39%**
101. **`packages/flutter/lib/src/cupertino/date_picker.dart`** -> AI Confidence: **99.39%**
102. **`packages/flutter/lib/src/cupertino/nav_bar.dart`** -> AI Confidence: **99.39%**
103. **`packages/flutter/lib/src/cupertino/search_field.dart`** -> AI Confidence: **99.39%**
104. **`packages/flutter/lib/src/cupertino/switch.dart`** -> AI Confidence: **99.39%**
105. **`packages/flutter/lib/src/material/app_bar.dart`** -> AI Confidence: **99.39%**
106. **`packages/flutter/lib/src/material/calendar_date_picker.dart`** -> AI Confidence: **99.39%**
107. **`packages/flutter/lib/src/material/choice_chip.dart`** -> AI Confidence: **99.39%**
108. **`packages/flutter/lib/src/material/dialog.dart`** -> AI Confidence: **99.39%**
109. **`packages/flutter/lib/src/material/expansion_tile.dart`** -> AI Confidence: **99.39%**
110. **`packages/flutter/lib/src/material/input_date_picker_form_field.dart`** -> AI Confidence: **99.39%**
111. **`packages/flutter/lib/src/material/input_decorator.dart`** -> AI Confidence: **99.39%**
112. **`packages/flutter/lib/src/material/radio_list_tile.dart`** -> AI Confidence: **99.39%**
113. **`packages/flutter/lib/src/material/refresh_indicator.dart`** -> AI Confidence: **99.39%**
114. **`packages/flutter/lib/src/material/tooltip.dart`** -> AI Confidence: **99.39%**
115. **`packages/flutter/lib/src/semantics/semantics.dart`** -> AI Confidence: **99.39%**
116. **`packages/flutter/lib/src/widgets/media_query.dart`** -> AI Confidence: **99.39%**
117. **`packages/flutter/lib/src/widgets/text.dart`** -> AI Confidence: **99.39%**
118. **`packages/flutter_tools/lib/src/android/deferred_components_gen_snapshot_validator.dart`** -> AI Confidence: **99.39%**
119. **`packages/flutter_tools/lib/src/base/analyze_size.dart`** -> AI Confidence: **99.39%**
120. **`packages/flutter_tools/lib/src/commands/create.dart`** -> AI Confidence: **99.39%**
121. **`packages/flutter_tools/lib/src/debug_adapters/flutter_adapter.dart`** -> AI Confidence: **99.39%**
122. **`packages/flutter_tools/lib/src/ios/core_devices.dart`** -> AI Confidence: **99.39%**
123. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/common/StandardMessageCodec.java`** -> AI Confidence: **99.39%**
124. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paragraph.dart`** -> AI Confidence: **99.35%**
125. **`packages/flutter/lib/src/material/date_picker.dart`** -> AI Confidence: **99.35%**
126. **`packages/flutter/lib/src/material/filter_chip.dart`** -> AI Confidence: **99.35%**
127. **`packages/flutter/lib/src/material/input_chip.dart`** -> AI Confidence: **99.35%**
128. **`packages/flutter/lib/src/material/switch.dart`** -> AI Confidence: **99.35%**
129. **`packages/flutter/lib/src/widgets/form.dart`** -> AI Confidence: **99.35%**
130. **`engine/src/flutter/display_list/testing/dl_test_surface_metal.mm`** -> AI Confidence: **99.34%**
131. **`engine/src/flutter/impeller/golden_tests/metal_screenshotter.mm`** -> AI Confidence: **99.34%**
132. **`engine/src/flutter/impeller/renderer/backend/metal/device_buffer_mtl.mm`** -> AI Confidence: **99.34%**
133. **`engine/src/flutter/impeller/renderer/backend/metal/gpu_tracer_mtl.mm`** -> AI Confidence: **99.34%**
134. **`engine/src/flutter/impeller/renderer/backend/metal/surface_mtl.h`** -> AI Confidence: **99.34%**
135. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterFakeKeyEvents.mm`** -> AI Confidence: **99.34%**
136. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViews.mm`** -> AI Confidence: **99.34%**
137. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterView.mm`** -> AI Confidence: **99.34%**
138. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/profiler_metrics_ios.h`** -> AI Confidence: **99.34%**
139. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/profiler_metrics_ios.mm`** -> AI Confidence: **99.34%**
140. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/vsync_waiter_ios.mm`** -> AI Confidence: **99.34%**
141. **`engine/src/flutter/shell/platform/darwin/ios/ios_context_metal_impeller.mm`** -> AI Confidence: **99.34%**
142. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface.mm`** -> AI Confidence: **99.34%**
143. **`engine/src/flutter/shell/platform/darwin/ios/platform_message_handler_ios.mm`** -> AI Confidence: **99.34%**
144. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/AccessibilityBridgeMac.mm`** -> AI Confidence: **99.34%**
145. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterChannelKeyResponder.mm`** -> AI Confidence: **99.34%**
146. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterDartProject.mm`** -> AI Confidence: **99.34%**
147. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTestUtils.h`** -> AI Confidence: **99.34%**
148. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterMutatorView.mm`** -> AI Confidence: **99.34%**
149. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterRenderer.mm`** -> AI Confidence: **99.34%**
150. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterView.mm`** -> AI Confidence: **99.34%**
151. **`engine/src/flutter/shell/platform/embedder/embedder_surface_metal_skia.mm`** -> AI Confidence: **99.34%**
152. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_context_metal.mm`** -> AI Confidence: **99.34%**
153. **`engine/src/flutter/display_list/dl_vertices_unittests.cc`** -> AI Confidence: **99.34%**
154. **`engine/src/flutter/impeller/compiler/code_gen_template.h`** -> AI Confidence: **99.34%**
155. **`dev/tools/bin/generate_gradle_lockfiles.dart`** -> AI Confidence: **99.34%**
156. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/text.dart`** -> AI Confidence: **99.34%**
157. **`engine/src/flutter/web_sdk/test/api_conform_test.dart`** -> AI Confidence: **99.34%**
158. **`packages/flutter/lib/src/gestures/events.dart`** -> AI Confidence: **99.34%**
159. **`packages/flutter/lib/src/material/app_bar_theme.dart`** -> AI Confidence: **99.34%**
160. **`packages/flutter/lib/src/material/chip.dart`** -> AI Confidence: **99.34%**
161. **`packages/flutter/lib/src/material/date_picker_theme.dart`** -> AI Confidence: **99.34%**
162. **`packages/flutter/lib/src/material/dropdown.dart`** -> AI Confidence: **99.34%**
163. **`packages/flutter/lib/src/material/scaffold.dart`** -> AI Confidence: **99.34%**
164. **`packages/flutter/lib/src/material/tabs.dart`** -> AI Confidence: **99.34%**
165. **`packages/flutter/lib/src/rendering/custom_paint.dart`** -> AI Confidence: **99.34%**
166. **`packages/flutter/lib/src/rendering/paragraph.dart`** -> AI Confidence: **99.34%**
167. **`packages/flutter/lib/src/rendering/sliver.dart`** -> AI Confidence: **99.34%**
168. **`packages/flutter_tools/lib/src/commands/generate_localizations.dart`** -> AI Confidence: **99.34%**
169. **`packages/flutter_tools/lib/src/migrations/lldb_init_migration.dart`** -> AI Confidence: **99.34%**
170. **`dev/integration_tests/hook_user_defines/src/hook_user_defines.h`** -> AI Confidence: **99.34%**
171. **`dev/integration_tests/link_hook/src/link_hook.h`** -> AI Confidence: **99.34%**
172. **`packages/flutter/lib/src/painting/text_span.dart`** -> AI Confidence: **99.33%**
173. **`packages/flutter_tools/lib/src/localizations/gen_l10n_types.dart`** -> AI Confidence: **99.33%**
174. **`dev/benchmarks/macrobenchmarks/ios/Runner/main.m`** -> AI Confidence: **99.32%**
175. **`dev/benchmarks/platform_views_layout_hybrid_composition/ios/Runner/main.m`** -> AI Confidence: **99.32%**
176. **`dev/benchmarks/test_apps/stocks/ios/Runner/main.m`** -> AI Confidence: **99.32%**
177. **`dev/integration_tests/channels/ios/Runner/main.m`** -> AI Confidence: **99.32%**
178. **`dev/integration_tests/external_textures/ios/Runner/main.m`** -> AI Confidence: **99.32%**
179. **`dev/integration_tests/flavors/ios/Runner/main.m`** -> AI Confidence: **99.32%**
180. **`dev/integration_tests/flutter_gallery/ios/Runner/main.m`** -> AI Confidence: **99.32%**
181. **`dev/integration_tests/ios_platform_view_tests/ios/Runner/main.m`** -> AI Confidence: **99.32%**
182. **`dev/integration_tests/platform_interaction/ios/Runner/main.m`** -> AI Confidence: **99.32%**
183. **`dev/integration_tests/spell_check/ios/Runner/main.m`** -> AI Confidence: **99.32%**
184. **`dev/integration_tests/ui/ios/Runner/main.m`** -> AI Confidence: **99.32%**
185. **`engine/src/flutter/fml/platform/darwin/paths_darwin.mm`** -> AI Confidence: **99.32%**
186. **`engine/src/flutter/impeller/renderer/backend/metal/sampler_library_mtl.mm`** -> AI Confidence: **99.32%**
187. **`engine/src/flutter/impeller/renderer/backend/metal/vertex_descriptor_mtl.mm`** -> AI Confidence: **99.32%**
188. **`engine/src/flutter/impeller/toolkit/interop/backend/metal/surface_mtl.mm`** -> AI Confidence: **99.32%**
189. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterNSBundleUtils.mm`** -> AI Confidence: **99.32%**
190. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSemanticsScrollView.mm`** -> AI Confidence: **99.32%**
191. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSharedApplication.mm`** -> AI Confidence: **99.32%**
192. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/SemanticsObject.mm`** -> AI Confidence: **99.32%**
193. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/overlay_layer_pool.mm`** -> AI Confidence: **99.32%**
194. **`engine/src/flutter/shell/platform/darwin/ios/ios_context_noop.mm`** -> AI Confidence: **99.32%**
195. **`engine/src/flutter/shell/platform/darwin/ios/ios_external_view_embedder.mm`** -> AI Confidence: **99.32%**
196. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterCompositor.mm`** -> AI Confidence: **99.32%**
197. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterMouseCursorPlugin.mm`** -> AI Confidence: **99.32%**
198. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/KeyCodeMapTest.mm`** -> AI Confidence: **99.32%**
199. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/Scenarios/main.m`** -> AI Confidence: **99.32%**
200. **`engine/src/flutter/testing/test_metal_surface_unittests.mm`** -> AI Confidence: **99.32%**
201. **`examples/flutter_view/ios/Runner/main.m`** -> AI Confidence: **99.32%**
202. **`examples/hello_world/ios/Runner/main.m`** -> AI Confidence: **99.32%**
203. **`examples/image_list/ios/Runner/main.m`** -> AI Confidence: **99.32%**
204. **`examples/layers/ios/Runner/main.m`** -> AI Confidence: **99.32%**
205. **`examples/platform_channel/ios/Runner/AppDelegate.m`** -> AI Confidence: **99.32%**
206. **`examples/platform_channel/ios/Runner/main.m`** -> AI Confidence: **99.32%**
207. **`examples/platform_view/ios/Runner/main.m`** -> AI Confidence: **99.32%**
208. **`packages/flutter_tools/templates/module/ios/host_app_ephemeral/Runner.tmpl/main.m`** -> AI Confidence: **99.32%**
209. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_standard_method_codec.h`** -> AI Confidence: **99.32%**
210. **`engine/src/flutter/testing/test_gl_utils.cc`** -> AI Confidence: **99.32%**
211. **`engine/src/flutter/shell/testing/vm_service/service_client.dart`** -> AI Confidence: **99.32%**
212. **`packages/flutter/lib/src/cupertino/icon_theme_data.dart`** -> AI Confidence: **99.32%**
213. **`packages/flutter/lib/src/material/button_theme.dart`** -> AI Confidence: **99.32%**
214. **`packages/flutter/lib/src/material/ink_well.dart`** -> AI Confidence: **99.32%**
215. **`packages/flutter/lib/src/material/material_button.dart`** -> AI Confidence: **99.32%**
216. **`packages/flutter/lib/src/rendering/debug.dart`** -> AI Confidence: **99.32%**
217. **`packages/flutter/lib/src/rendering/object.dart`** -> AI Confidence: **99.32%**
218. **`packages/flutter_test/lib/src/event_simulation.dart`** -> AI Confidence: **99.32%**
219. **`packages/flutter_tools/lib/src/build_info.dart`** -> AI Confidence: **99.32%**
220. **`packages/flutter_tools/lib/src/flutter_manifest.dart`** -> AI Confidence: **99.32%**
221. **`packages/flutter_tools/tool/daemon_client.dart`** -> AI Confidence: **99.32%**
222. **`packages/flutter_tools/gradle/src/main/kotlin/DependencyVersionChecker.kt`** -> AI Confidence: **99.31%**
223. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterPlugin.kt`** -> AI Confidence: **99.31%**
224. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt`** -> AI Confidence: **99.31%**
225. **`packages/flutter_tools/gradle/src/main/kotlin/tasks/DeepLinkJsonFromManifestTaskHelper.kt`** -> AI Confidence: **99.31%**
226. **`dev/integration_tests/ios_host_app/Host/MainViewController.m`** -> AI Confidence: **99.31%**
227. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinContextMetalImpeller.mm`** -> AI Confidence: **99.31%**
228. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterAppDelegateTest.mm`** -> AI Confidence: **99.31%**
229. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterDartVMServicePublisher.mm`** -> AI Confidence: **99.31%**
230. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterHeadlessDartRunner.mm`** -> AI Confidence: **99.31%**
231. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/accessibility_bridge_test.mm`** -> AI Confidence: **99.31%**
232. **`engine/src/flutter/shell/platform/darwin/ios/platform_view_ios.h`** -> AI Confidence: **99.31%**
233. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterAppLifecycleDelegate.mm`** -> AI Confidence: **99.31%**
234. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTest.mm`** -> AI Confidence: **99.31%**
235. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardManagerTest.mm`** -> AI Confidence: **99.31%**
236. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputPluginTest.mm`** -> AI Confidence: **99.31%**
237. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewControllerTest.mm`** -> AI Confidence: **99.31%**
238. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewEngineProviderTest.mm`** -> AI Confidence: **99.31%**
239. **`engine/src/flutter/common/graphics/persistent_cache.cc`** -> AI Confidence: **99.31%**
240. **`engine/src/flutter/display_list/benchmarking/dl_benchmarks.cc`** -> AI Confidence: **99.31%**
241. **`engine/src/flutter/display_list/skia/dl_sk_conversions.cc`** -> AI Confidence: **99.31%**
242. **`engine/src/flutter/examples/glfw_drm/FlutterEmbedderGLFW.cc`** -> AI Confidence: **99.31%**
243. **`engine/src/flutter/flow/layers/display_list_layer.cc`** -> AI Confidence: **99.31%**
244. **`engine/src/flutter/flow/layers/display_list_raster_cache_item.cc`** -> AI Confidence: **99.31%**
245. **`engine/src/flutter/flow/layers/layer_tree.cc`** -> AI Confidence: **99.31%**
246. **`engine/src/flutter/flow/raster_cache.cc`** -> AI Confidence: **99.31%**
247. **`engine/src/flutter/flow/skia_gpu_object.h`** -> AI Confidence: **99.31%**
248. **`engine/src/flutter/flow/stopwatch_dl.cc`** -> AI Confidence: **99.31%**
249. **`engine/src/flutter/fml/cpu_affinity.cc`** -> AI Confidence: **99.31%**
250. **`engine/src/flutter/fml/message_loop_task_queues_benchmark.cc`** -> AI Confidence: **99.31%**
251. **`engine/src/flutter/fml/platform/fuchsia/message_loop_fuchsia.cc`** -> AI Confidence: **99.31%**
252. **`engine/src/flutter/fml/platform/posix/file_posix.cc`** -> AI Confidence: **99.31%**
253. **`engine/src/flutter/fml/platform/posix/mapping_posix.cc`** -> AI Confidence: **99.31%**
254. **`engine/src/flutter/fml/platform/win/mapping_win.cc`** -> AI Confidence: **99.31%**
255. **`engine/src/flutter/fml/synchronization/waitable_event_unittest.cc`** -> AI Confidence: **99.31%**
256. **`engine/src/flutter/impeller/compiler/compiler.cc`** -> AI Confidence: **99.31%**
257. **`engine/src/flutter/impeller/compiler/impellerc_main.cc`** -> AI Confidence: **99.31%**
258. **`engine/src/flutter/impeller/compiler/reflector.cc`** -> AI Confidence: **99.31%**
259. **`engine/src/flutter/impeller/compiler/reflector.h`** -> AI Confidence: **99.31%**
260. **`engine/src/flutter/impeller/compiler/runtime_stage_data.cc`** -> AI Confidence: **99.31%**
261. **`engine/src/flutter/impeller/compiler/switches.cc`** -> AI Confidence: **99.31%**
262. **`engine/src/flutter/impeller/core/host_buffer.cc`** -> AI Confidence: **99.31%**
263. **`engine/src/flutter/impeller/display_list/canvas.cc`** -> AI Confidence: **99.31%**
264. **`engine/src/flutter/impeller/display_list/dl_dispatcher.cc`** -> AI Confidence: **99.31%**
265. **`engine/src/flutter/impeller/entity/contents/clip_contents.cc`** -> AI Confidence: **99.31%**
266. **`engine/src/flutter/impeller/entity/contents/filters/blend_filter_contents.cc`** -> AI Confidence: **99.31%**
267. **`engine/src/flutter/impeller/entity/contents/filters/gaussian_blur_filter_contents.cc`** -> AI Confidence: **99.31%**
268. **`engine/src/flutter/impeller/entity/contents/filters/gaussian_blur_filter_contents_unittests.cc`** -> AI Confidence: **99.31%**
269. **`engine/src/flutter/impeller/entity/contents/gradient_generator.cc`** -> AI Confidence: **99.31%**
270. **`engine/src/flutter/impeller/entity/contents/runtime_effect_contents.cc`** -> AI Confidence: **99.31%**
271. **`engine/src/flutter/impeller/entity/contents/text_contents.cc`** -> AI Confidence: **99.31%**
272. **`engine/src/flutter/impeller/entity/entity.cc`** -> AI Confidence: **99.31%**
273. **`engine/src/flutter/impeller/entity/inline_pass_context.cc`** -> AI Confidence: **99.31%**
274. **`engine/src/flutter/impeller/geometry/geometry_asserts.h`** -> AI Confidence: **99.31%**
275. **`engine/src/flutter/impeller/playground/image/backends/skia/compressed_image_skia.cc`** -> AI Confidence: **99.31%**
276. **`engine/src/flutter/impeller/playground/imgui/imgui_impl_impeller.cc`** -> AI Confidence: **99.31%**
277. **`engine/src/flutter/impeller/renderer/backend/gles/blit_command_gles.cc`** -> AI Confidence: **99.31%**
278. **`engine/src/flutter/impeller/renderer/backend/gles/buffer_bindings_gles.cc`** -> AI Confidence: **99.31%**
279. **`engine/src/flutter/impeller/renderer/backend/gles/proc_table_gles.cc`** -> AI Confidence: **99.31%**
280. **`engine/src/flutter/impeller/renderer/backend/gles/render_pass_gles.cc`** -> AI Confidence: **99.31%**
281. **`engine/src/flutter/impeller/renderer/backend/gles/sampler_gles.cc`** -> AI Confidence: **99.31%**
282. **`engine/src/flutter/impeller/renderer/backend/gles/texture_gles.cc`** -> AI Confidence: **99.31%**
283. **`engine/src/flutter/impeller/renderer/backend/vulkan/driver_info_vk.cc`** -> AI Confidence: **99.31%**
284. **`engine/src/flutter/impeller/renderer/backend/vulkan/formats_vk.h`** -> AI Confidence: **99.31%**
285. **`engine/src/flutter/impeller/renderer/backend/vulkan/render_pass_vk.cc`** -> AI Confidence: **99.31%**
286. **`engine/src/flutter/impeller/renderer/backend/vulkan/test/mock_vulkan.cc`** -> AI Confidence: **99.31%**
287. **`engine/src/flutter/impeller/renderer/render_target.cc`** -> AI Confidence: **99.31%**
288. **`engine/src/flutter/impeller/runtime_stage/runtime_stage.cc`** -> AI Confidence: **99.31%**
289. **`engine/src/flutter/impeller/typographer/backends/skia/text_frame_skia.cc`** -> AI Confidence: **99.31%**
290. **`engine/src/flutter/impeller/typographer/backends/skia/typographer_context_skia.cc`** -> AI Confidence: **99.31%**
291. **`engine/src/flutter/impeller/typographer/lazy_glyph_atlas.cc`** -> AI Confidence: **99.31%**
292. **`engine/src/flutter/lib/gpu/shader_library.cc`** -> AI Confidence: **99.31%**
293. **`engine/src/flutter/lib/ui/painting/canvas.cc`** -> AI Confidence: **99.31%**
294. **`engine/src/flutter/lib/ui/painting/fragment_program.cc`** -> AI Confidence: **99.31%**
295. **`engine/src/flutter/lib/ui/painting/image.cc`** -> AI Confidence: **99.31%**
296. **`engine/src/flutter/lib/ui/painting/image_decoder_impeller.cc`** -> AI Confidence: **99.31%**
297. **`engine/src/flutter/lib/ui/painting/image_decoder_skia.cc`** -> AI Confidence: **99.31%**
298. **`engine/src/flutter/lib/ui/painting/image_descriptor.cc`** -> AI Confidence: **99.31%**
299. **`engine/src/flutter/lib/ui/painting/image_generator_apng.cc`** -> AI Confidence: **99.31%**
300. **`engine/src/flutter/lib/ui/painting/multi_frame_codec.cc`** -> AI Confidence: **99.31%**
301. **`engine/src/flutter/lib/ui/semantics/semantics_update_builder.cc`** -> AI Confidence: **99.31%**
302. **`engine/src/flutter/lib/ui/text/font_collection.cc`** -> AI Confidence: **99.31%**
303. **`engine/src/flutter/lib/ui/text/paragraph_builder.cc`** -> AI Confidence: **99.31%**
304. **`engine/src/flutter/runtime/dart_vm_initializer.cc`** -> AI Confidence: **99.31%**
305. **`engine/src/flutter/shell/common/rasterizer.cc`** -> AI Confidence: **99.31%**
306. **`engine/src/flutter/shell/common/shell.cc`** -> AI Confidence: **99.31%**
307. **`engine/src/flutter/shell/common/snapshot_controller_impeller.cc`** -> AI Confidence: **99.31%**
308. **`engine/src/flutter/shell/platform/android/android_context_gl_impeller.cc`** -> AI Confidence: **99.31%**
309. **`engine/src/flutter/shell/platform/android/android_context_vk_impeller.cc`** -> AI Confidence: **99.31%**
310. **`engine/src/flutter/shell/platform/android/android_shell_holder.cc`** -> AI Confidence: **99.31%**
311. **`engine/src/flutter/shell/platform/android/android_surface_software.cc`** -> AI Confidence: **99.31%**
312. **`engine/src/flutter/shell/platform/android/external_view_embedder/external_view_embedder_2.cc`** -> AI Confidence: **99.31%**
313. **`engine/src/flutter/shell/platform/android/flutter_main.cc`** -> AI Confidence: **99.31%**
314. **`engine/src/flutter/shell/platform/android/platform_view_android.cc`** -> AI Confidence: **99.31%**
315. **`engine/src/flutter/shell/platform/common/client_wrapper/include/flutter/event_channel.h`** -> AI Confidence: **99.31%**
316. **`engine/src/flutter/shell/platform/common/client_wrapper/standard_codec.cc`** -> AI Confidence: **99.31%**
317. **`engine/src/flutter/shell/platform/embedder/embedder.cc`** -> AI Confidence: **99.31%**
318. **`engine/src/flutter/shell/platform/embedder/embedder_external_texture_gl.cc`** -> AI Confidence: **99.31%**
319. **`engine/src/flutter/shell/platform/embedder/embedder_surface_software.cc`** -> AI Confidence: **99.31%**
320. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_gl.cc`** -> AI Confidence: **99.31%**
321. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_vulkan.cc`** -> AI Confidence: **99.31%**
322. **`engine/src/flutter/shell/platform/embedder/tests/embedder_unittests_util.cc`** -> AI Confidence: **99.31%**
323. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_component_controller.cc`** -> AI Confidence: **99.31%**
324. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_runner.cc`** -> AI Confidence: **99.31%**
325. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_test_component_controller.cc`** -> AI Confidence: **99.31%**
326. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/main.cc`** -> AI Confidence: **99.31%**
327. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/service_isolate.cc`** -> AI Confidence: **99.31%**
328. **`engine/src/flutter/shell/platform/fuchsia/flutter/accessibility_bridge.cc`** -> AI Confidence: **99.31%**
329. **`engine/src/flutter/shell/platform/fuchsia/flutter/component_v2.cc`** -> AI Confidence: **99.31%**
330. **`engine/src/flutter/shell/platform/fuchsia/flutter/engine.cc`** -> AI Confidence: **99.31%**
331. **`engine/src/flutter/shell/platform/fuchsia/flutter/external_view_embedder.cc`** -> AI Confidence: **99.31%**
332. **`engine/src/flutter/shell/platform/fuchsia/flutter/platform_view.cc`** -> AI Confidence: **99.31%**
333. **`engine/src/flutter/shell/platform/fuchsia/flutter/pointer_delegate.cc`** -> AI Confidence: **99.31%**
334. **`engine/src/flutter/shell/platform/fuchsia/flutter/runner.cc`** -> AI Confidence: **99.31%**
335. **`engine/src/flutter/shell/platform/fuchsia/flutter/tests/integration/utils/screenshot.cc`** -> AI Confidence: **99.31%**
336. **`engine/src/flutter/shell/platform/fuchsia/flutter/text_delegate.cc`** -> AI Confidence: **99.31%**
337. **`engine/src/flutter/shell/platform/fuchsia/flutter/vulkan_surface_producer.cc`** -> AI Confidence: **99.31%**
338. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/handle_exception.cc`** -> AI Confidence: **99.31%**
339. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/mapped_resource.cc`** -> AI Confidence: **99.31%**
340. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/vmo.cc`** -> AI Confidence: **99.31%**
341. **`engine/src/flutter/shell/platform/linux/fl_accessibility_handler_test.cc`** -> AI Confidence: **99.31%**
342. **`engine/src/flutter/shell/platform/linux/fl_compositor_opengl.cc`** -> AI Confidence: **99.31%**
343. **`engine/src/flutter/shell/platform/linux/fl_engine.cc`** -> AI Confidence: **99.31%**
344. **`engine/src/flutter/shell/platform/linux/fl_keyboard_manager.cc`** -> AI Confidence: **99.31%**
345. **`engine/src/flutter/shell/platform/windows/flutter_window.cc`** -> AI Confidence: **99.31%**
346. **`engine/src/flutter/shell/platform/windows/host_window.cc`** -> AI Confidence: **99.31%**
347. **`engine/src/flutter/shell/platform/windows/platform_handler.cc`** -> AI Confidence: **99.31%**
348. **`engine/src/flutter/shell/platform/windows/text_input_plugin.cc`** -> AI Confidence: **99.31%**
349. **`engine/src/flutter/testing/debugger_detection.cc`** -> AI Confidence: **99.31%**
350. **`engine/src/flutter/testing/display_list_testing.cc`** -> AI Confidence: **99.31%**
351. **`engine/src/flutter/testing/test_vulkan_context.cc`** -> AI Confidence: **99.31%**
352. **`engine/src/flutter/tools/font_subset/main.cc`** -> AI Confidence: **99.31%**
353. **`engine/src/flutter/tools/licenses_cpp/src/license_checker.cc`** -> AI Confidence: **99.31%**
354. **`engine/src/flutter/tools/licenses_cpp/src/license_checker_unittests.cc`** -> AI Confidence: **99.31%**
355. **`engine/src/flutter/tools/licenses_cpp/src/main.cc`** -> AI Confidence: **99.31%**
356. **`engine/src/flutter/txt/benchmarks/skparagraph_benchmarks.cc`** -> AI Confidence: **99.31%**
357. **`engine/src/flutter/txt/src/txt/font_collection.cc`** -> AI Confidence: **99.31%**
358. **`engine/src/flutter/vulkan/vulkan_device.cc`** -> AI Confidence: **99.31%**
359. **`engine/src/flutter/vulkan/vulkan_swapchain.cc`** -> AI Confidence: **99.31%**
360. **`examples/platform_channel/windows/runner/flutter_window.cpp`** -> AI Confidence: **99.31%**
361. **`examples/platform_view/windows/runner/flutter_window.cpp`** -> AI Confidence: **99.31%**
362. **`engine/src/flutter/lib/web_ui/flutter_js/src/loader.js`** -> AI Confidence: **99.31%**
363. **`dev/bots/analyze.dart`** -> AI Confidence: **99.31%**
364. **`dev/bots/analyze_snippet_code.dart`** -> AI Confidence: **99.31%**
365. **`dev/bots/custom_rules/analyze.dart`** -> AI Confidence: **99.31%**
366. **`dev/bots/prepare_package.dart`** -> AI Confidence: **99.31%**
367. **`dev/bots/suite_runners/run_android_engine_tests.dart`** -> AI Confidence: **99.31%**
368. **`dev/bots/unpublish_package.dart`** -> AI Confidence: **99.31%**
369. **`dev/bots/utils.dart`** -> AI Confidence: **99.31%**
370. **`dev/forbidden_from_release_tests/bin/main.dart`** -> AI Confidence: **99.31%**
371. **`dev/snippets/bin/snippets.dart`** -> AI Confidence: **99.31%**
372. **`dev/snippets/lib/src/analysis.dart`** -> AI Confidence: **99.31%**
373. **`dev/snippets/lib/src/snippet_generator.dart`** -> AI Confidence: **99.31%**
374. **`dev/snippets/lib/src/util.dart`** -> AI Confidence: **99.31%**
375. **`dev/tools/create_api_docs.dart`** -> AI Confidence: **99.31%**
376. **`dev/tools/gen_keycodes/lib/keyboard_maps_code_gen.dart`** -> AI Confidence: **99.31%**
377. **`dev/tools/update_icons.dart`** -> AI Confidence: **99.31%**
378. **`engine/src/flutter/lib/web_ui/dev/test_runner.dart`** -> AI Confidence: **99.31%**
379. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/image.dart`** -> AI Confidence: **99.31%**
380. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/renderer.dart`** -> AI Confidence: **99.31%**
381. **`engine/src/flutter/lib/web_ui/lib/src/engine/compositing/composition.dart`** -> AI Confidence: **99.31%**
382. **`engine/src/flutter/lib/web_ui/lib/src/engine/keyboard_binding.dart`** -> AI Confidence: **99.31%**
383. **`engine/src/flutter/lib/web_ui/lib/src/engine/pointer_binding.dart`** -> AI Confidence: **99.31%**
384. **`engine/src/flutter/lib/web_ui/lib/src/engine/raw_keyboard.dart`** -> AI Confidence: **99.31%**
385. **`engine/src/flutter/lib/web_ui/lib/src/engine/semantics/semantics.dart`** -> AI Confidence: **99.31%**
386. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/renderer.dart`** -> AI Confidence: **99.31%**
387. **`engine/src/flutter/lib/web_ui/lib/src/engine/window.dart`** -> AI Confidence: **99.31%**
388. **`engine/src/flutter/lib/web_ui/lib/ui_web/src/ui_web/navigation/url_strategy.dart`** -> AI Confidence: **99.31%**
389. **`engine/src/flutter/lib/web_ui/test/common/matchers.dart`** -> AI Confidence: **99.31%**
390. **`engine/src/flutter/lib/web_ui/test/engine/channel_buffers_test.dart`** -> AI Confidence: **99.31%**
391. **`engine/src/flutter/lib/web_ui/test/engine/pointer_binding_test.dart`** -> AI Confidence: **99.31%**
392. **`engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart`** -> AI Confidence: **99.31%**
393. **`engine/src/flutter/lib/web_ui/test/engine/semantics/text_field_test.dart`** -> AI Confidence: **99.31%**
394. **`engine/src/flutter/lib/web_ui/test/engine/text_editing_test.dart`** -> AI Confidence: **99.31%**
395. **`engine/src/flutter/lib/web_ui/test/ui/canvas_golden_test.dart`** -> AI Confidence: **99.31%**
396. **`engine/src/flutter/lib/web_ui/test/ui/fallback_fonts_golden_test.dart`** -> AI Confidence: **99.31%**
397. **`engine/src/flutter/shell/platform/embedder/fixtures/main.dart`** -> AI Confidence: **99.31%**
398. **`engine/src/flutter/testing/dart/vm_service/vmservice_methods_test.dart`** -> AI Confidence: **99.31%**
399. **`engine/src/flutter/testing/ios_scenario_app/bin/run_ios_tests.dart`** -> AI Confidence: **99.31%**
400. **`engine/src/flutter/testing/ios_scenario_app/lib/src/platform_view.dart`** -> AI Confidence: **99.31%**
401. **`engine/src/flutter/testing/skia_gold_client/lib/skia_gold_client.dart`** -> AI Confidence: **99.31%**
402. **`engine/src/flutter/testing/skia_gold_client/test/skia_gold_client_test.dart`** -> AI Confidence: **99.31%**
403. **`engine/src/flutter/tools/clang_tidy/lib/clang_tidy.dart`** -> AI Confidence: **99.31%**
404. **`engine/src/flutter/tools/engine_tool/lib/src/build_plan.dart`** -> AI Confidence: **99.31%**
405. **`engine/src/flutter/tools/engine_tool/lib/src/commands/query_command.dart`** -> AI Confidence: **99.31%**
406. **`engine/src/flutter/tools/engine_tool/test/build_plan_test.dart`** -> AI Confidence: **99.31%**
407. **`engine/src/flutter/tools/gen_web_locale_keymap/lib/github.dart`** -> AI Confidence: **99.31%**
408. **`engine/src/flutter/tools/header_guard_check/lib/header_guard_check.dart`** -> AI Confidence: **99.31%**
409. **`engine/src/flutter/tools/pkg/engine_build_configs/bin/check.dart`** -> AI Confidence: **99.31%**
410. **`engine/src/flutter/tools/pkg/engine_build_configs/bin/run.dart`** -> AI Confidence: **99.31%**
411. **`engine/src/flutter/tools/pkg/engine_build_configs/test/build_config_runner_test.dart`** -> AI Confidence: **99.31%**
412. **`engine/src/flutter/tools/pkg/engine_build_configs/test/ci_yaml_test.dart`** -> AI Confidence: **99.31%**
413. **`packages/flutter/lib/src/animation/animation_controller.dart`** -> AI Confidence: **99.31%**
414. **`packages/flutter/lib/src/cupertino/adaptive_text_selection_toolbar.dart`** -> AI Confidence: **99.31%**
415. **`packages/flutter/lib/src/cupertino/context_menu.dart`** -> AI Confidence: **99.31%**
416. **`packages/flutter/lib/src/cupertino/dialog.dart`** -> AI Confidence: **99.31%**
417. **`packages/flutter/lib/src/cupertino/picker.dart`** -> AI Confidence: **99.31%**
418. **`packages/flutter/lib/src/cupertino/refresh.dart`** -> AI Confidence: **99.31%**
419. **`packages/flutter/lib/src/cupertino/sheet.dart`** -> AI Confidence: **99.31%**
420. **`packages/flutter/lib/src/cupertino/slider.dart`** -> AI Confidence: **99.31%**
421. **`packages/flutter/lib/src/cupertino/sliding_segmented_control.dart`** -> AI Confidence: **99.31%**
422. **`packages/flutter/lib/src/cupertino/text_field.dart`** -> AI Confidence: **99.31%**
423. **`packages/flutter/lib/src/cupertino/text_selection.dart`** -> AI Confidence: **99.31%**
424. **`packages/flutter/lib/src/cupertino/text_selection_toolbar.dart`** -> AI Confidence: **99.31%**
425. **`packages/flutter/lib/src/gestures/long_press.dart`** -> AI Confidence: **99.31%**
426. **`packages/flutter/lib/src/gestures/multitap.dart`** -> AI Confidence: **99.31%**
427. **`packages/flutter/lib/src/gestures/scale.dart`** -> AI Confidence: **99.31%**
428. **`packages/flutter/lib/src/gestures/tap_and_drag.dart`** -> AI Confidence: **99.31%**
429. **`packages/flutter/lib/src/material/about.dart`** -> AI Confidence: **99.31%**
430. **`packages/flutter/lib/src/material/action_chip.dart`** -> AI Confidence: **99.31%**
431. **`packages/flutter/lib/src/material/app.dart`** -> AI Confidence: **99.31%**
432. **`packages/flutter/lib/src/material/bottom_app_bar.dart`** -> AI Confidence: **99.31%**
433. **`packages/flutter/lib/src/material/dropdown_menu.dart`** -> AI Confidence: **99.31%**
434. **`packages/flutter/lib/src/material/expansion_panel.dart`** -> AI Confidence: **99.31%**
435. **`packages/flutter/lib/src/material/mergeable_material.dart`** -> AI Confidence: **99.31%**
436. **`packages/flutter/lib/src/material/popup_menu.dart`** -> AI Confidence: **99.31%**
437. **`packages/flutter/lib/src/material/range_slider.dart`** -> AI Confidence: **99.31%**
438. **`packages/flutter/lib/src/material/reorderable_list.dart`** -> AI Confidence: **99.31%**
439. **`packages/flutter/lib/src/material/search.dart`** -> AI Confidence: **99.31%**
440. **`packages/flutter/lib/src/material/search_anchor.dart`** -> AI Confidence: **99.31%**
441. **`packages/flutter/lib/src/material/segmented_button.dart`** -> AI Confidence: **99.31%**
442. **`packages/flutter/lib/src/material/text_selection.dart`** -> AI Confidence: **99.31%**
443. **`packages/flutter/lib/src/material/theme_data.dart`** -> AI Confidence: **99.31%**
444. **`packages/flutter/lib/src/material/time_picker.dart`** -> AI Confidence: **99.31%**
445. **`packages/flutter/lib/src/material/toggle_buttons.dart`** -> AI Confidence: **99.31%**
446. **`packages/flutter/lib/src/painting/box_decoration.dart`** -> AI Confidence: **99.31%**
447. **`packages/flutter/lib/src/painting/flutter_logo.dart`** -> AI Confidence: **99.31%**
448. **`packages/flutter/lib/src/painting/shape_decoration.dart`** -> AI Confidence: **99.31%**
449. **`packages/flutter/lib/src/painting/stadium_border.dart`** -> AI Confidence: **99.31%**
450. **`packages/flutter/lib/src/painting/star_border.dart`** -> AI Confidence: **99.31%**
451. **`packages/flutter/lib/src/rendering/editable.dart`** -> AI Confidence: **99.31%**
452. **`packages/flutter/lib/src/rendering/flex.dart`** -> AI Confidence: **99.31%**
453. **`packages/flutter/lib/src/rendering/list_wheel_viewport.dart`** -> AI Confidence: **99.31%**
454. **`packages/flutter/lib/src/rendering/platform_view.dart`** -> AI Confidence: **99.31%**
455. **`packages/flutter/lib/src/rendering/proxy_sliver.dart`** -> AI Confidence: **99.31%**
456. **`packages/flutter/lib/src/rendering/shifted_box.dart`** -> AI Confidence: **99.31%**
457. **`packages/flutter/lib/src/rendering/sliver_persistent_header.dart`** -> AI Confidence: **99.31%**
458. **`packages/flutter/lib/src/rendering/sliver_tree.dart`** -> AI Confidence: **99.31%**
459. **`packages/flutter/lib/src/rendering/table.dart`** -> AI Confidence: **99.31%**
460. **`packages/flutter/lib/src/rendering/viewport.dart`** -> AI Confidence: **99.31%**
461. **`packages/flutter/lib/src/scheduler/binding.dart`** -> AI Confidence: **99.31%**
462. **`packages/flutter/lib/src/widgets/_accessibility_evaluations.dart`** -> AI Confidence: **99.31%**
463. **`packages/flutter/lib/src/widgets/_platform_selectable_region_context_menu_web.dart`** -> AI Confidence: **99.31%**
464. **`packages/flutter/lib/src/widgets/_web_image_web.dart`** -> AI Confidence: **99.31%**
465. **`packages/flutter/lib/src/widgets/animated_scroll_view.dart`** -> AI Confidence: **99.31%**
466. **`packages/flutter/lib/src/widgets/binding.dart`** -> AI Confidence: **99.31%**
467. **`packages/flutter/lib/src/widgets/dismissible.dart`** -> AI Confidence: **99.31%**
468. **`packages/flutter/lib/src/widgets/drag_target.dart`** -> AI Confidence: **99.31%**
469. **`packages/flutter/lib/src/widgets/heroes.dart`** -> AI Confidence: **99.31%**
470. **`packages/flutter/lib/src/widgets/image.dart`** -> AI Confidence: **99.31%**
471. **`packages/flutter/lib/src/widgets/image_icon.dart`** -> AI Confidence: **99.31%**
472. **`packages/flutter/lib/src/widgets/interactive_viewer.dart`** -> AI Confidence: **99.31%**
473. **`packages/flutter/lib/src/widgets/list_wheel_scroll_view.dart`** -> AI Confidence: **99.31%**
474. **`packages/flutter/lib/src/widgets/navigator.dart`** -> AI Confidence: **99.31%**
475. **`packages/flutter/lib/src/widgets/nested_scroll_view.dart`** -> AI Confidence: **99.31%**
476. **`packages/flutter/lib/src/widgets/page_view.dart`** -> AI Confidence: **99.31%**
477. **`packages/flutter/lib/src/widgets/radio_group.dart`** -> AI Confidence: **99.31%**
478. **`packages/flutter/lib/src/widgets/raw_menu_anchor.dart`** -> AI Confidence: **99.31%**
479. **`packages/flutter/lib/src/widgets/reorderable_list.dart`** -> AI Confidence: **99.31%**
480. **`packages/flutter/lib/src/widgets/single_child_scroll_view.dart`** -> AI Confidence: **99.31%**
481. **`packages/flutter/lib/src/widgets/sliver_floating_header.dart`** -> AI Confidence: **99.31%**
482. **`packages/flutter/lib/src/widgets/sliver_tree.dart`** -> AI Confidence: **99.31%**
483. **`packages/flutter/lib/src/widgets/snapshot_widget.dart`** -> AI Confidence: **99.31%**
484. **`packages/flutter/lib/src/widgets/toggleable.dart`** -> AI Confidence: **99.31%**
485. **`packages/flutter_driver/lib/src/driver/web_driver.dart`** -> AI Confidence: **99.31%**
486. **`packages/flutter_test/lib/src/mock_canvas.dart`** -> AI Confidence: **99.31%**
487. **`packages/flutter_tools/lib/src/android/android_emulator.dart`** -> AI Confidence: **99.31%**
488. **`packages/flutter_tools/lib/src/android/deferred_components_prebuild_validator.dart`** -> AI Confidence: **99.31%**
489. **`packages/flutter_tools/lib/src/android/gradle.dart`** -> AI Confidence: **99.31%**
490. **`packages/flutter_tools/lib/src/base/build.dart`** -> AI Confidence: **99.31%**
491. **`packages/flutter_tools/lib/src/base/dds.dart`** -> AI Confidence: **99.31%**
492. **`packages/flutter_tools/lib/src/base/error_handling_io.dart`** -> AI Confidence: **99.31%**
493. **`packages/flutter_tools/lib/src/base/net.dart`** -> AI Confidence: **99.31%**
494. **`packages/flutter_tools/lib/src/base/utils.dart`** -> AI Confidence: **99.31%**
495. **`packages/flutter_tools/lib/src/build_system/targets/darwin.dart`** -> AI Confidence: **99.31%**
496. **`packages/flutter_tools/lib/src/build_system/tools/shader_compiler.dart`** -> AI Confidence: **99.31%**
497. **`packages/flutter_tools/lib/src/bundle_builder.dart`** -> AI Confidence: **99.31%**
498. **`packages/flutter_tools/lib/src/commands/assemble.dart`** -> AI Confidence: **99.31%**
499. **`packages/flutter_tools/lib/src/commands/attach.dart`** -> AI Confidence: **99.31%**
500. **`packages/flutter_tools/lib/src/commands/clean.dart`** -> AI Confidence: **99.31%**
501. **`packages/flutter_tools/lib/src/commands/config.dart`** -> AI Confidence: **99.31%**
502. **`packages/flutter_tools/lib/src/commands/daemon.dart`** -> AI Confidence: **99.31%**
503. **`packages/flutter_tools/lib/src/commands/devices.dart`** -> AI Confidence: **99.31%**
504. **`packages/flutter_tools/lib/src/commands/downgrade.dart`** -> AI Confidence: **99.31%**
505. **`packages/flutter_tools/lib/src/commands/emulators.dart`** -> AI Confidence: **99.31%**
506. **`packages/flutter_tools/lib/src/commands/install.dart`** -> AI Confidence: **99.31%**
507. **`packages/flutter_tools/lib/src/commands/symbolize.dart`** -> AI Confidence: **99.31%**
508. **`packages/flutter_tools/lib/src/commands/test.dart`** -> AI Confidence: **99.31%**
509. **`packages/flutter_tools/lib/src/commands/upgrade.dart`** -> AI Confidence: **99.31%**
510. **`packages/flutter_tools/lib/src/compile.dart`** -> AI Confidence: **99.31%**
511. **`packages/flutter_tools/lib/src/custom_devices/custom_device.dart`** -> AI Confidence: **99.31%**
512. **`packages/flutter_tools/lib/src/debug_adapters/flutter_test_adapter.dart`** -> AI Confidence: **99.31%**
513. **`packages/flutter_tools/lib/src/desktop_device.dart`** -> AI Confidence: **99.31%**
514. **`packages/flutter_tools/lib/src/devtools_launcher.dart`** -> AI Confidence: **99.31%**
515. **`packages/flutter_tools/lib/src/drive/drive_service.dart`** -> AI Confidence: **99.31%**
516. **`packages/flutter_tools/lib/src/flutter_application_package.dart`** -> AI Confidence: **99.31%**
517. **`packages/flutter_tools/lib/src/flutter_project_metadata.dart`** -> AI Confidence: **99.31%**
518. **`packages/flutter_tools/lib/src/ios/ios_deploy.dart`** -> AI Confidence: **99.31%**
519. **`packages/flutter_tools/lib/src/ios/simulators.dart`** -> AI Confidence: **99.31%**
520. **`packages/flutter_tools/lib/src/isolated/native_assets/macos/native_assets_host.dart`** -> AI Confidence: **99.31%**
521. **`packages/flutter_tools/lib/src/isolated/native_assets/native_assets.dart`** -> AI Confidence: **99.31%**
522. **`packages/flutter_tools/lib/src/isolated/resident_web_runner.dart`** -> AI Confidence: **99.31%**
523. **`packages/flutter_tools/lib/src/linux/build_linux.dart`** -> AI Confidence: **99.31%**
524. **`packages/flutter_tools/lib/src/localizations/gen_l10n.dart`** -> AI Confidence: **99.31%**
525. **`packages/flutter_tools/lib/src/macos/darwin_dependency_management.dart`** -> AI Confidence: **99.31%**
526. **`packages/flutter_tools/lib/src/macos/xcdevice.dart`** -> AI Confidence: **99.31%**
527. **`packages/flutter_tools/lib/src/migrations/swift_package_manager_integration_migration.dart`** -> AI Confidence: **99.31%**
528. **`packages/flutter_tools/lib/src/reporting/github_template.dart`** -> AI Confidence: **99.31%**
529. **`packages/flutter_tools/lib/src/runner/flutter_command.dart`** -> AI Confidence: **99.31%**
530. **`packages/flutter_tools/lib/src/runner/flutter_command_runner.dart`** -> AI Confidence: **99.31%**
531. **`packages/flutter_tools/lib/src/runner/local_engine.dart`** -> AI Confidence: **99.31%**
532. **`packages/flutter_tools/lib/src/runner/target_devices.dart`** -> AI Confidence: **99.31%**
533. **`packages/flutter_tools/lib/src/test/coverage_collector.dart`** -> AI Confidence: **99.31%**
534. **`packages/flutter_tools/lib/src/test/flutter_platform.dart`** -> AI Confidence: **99.31%**
535. **`packages/flutter_tools/lib/src/test/runner.dart`** -> AI Confidence: **99.31%**
536. **`packages/flutter_tools/lib/src/web/devfs_config.dart`** -> AI Confidence: **99.31%**
537. **`packages/flutter_tools/lib/src/web_template.dart`** -> AI Confidence: **99.31%**
538. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/AndroidTouchProcessor.java`** -> AI Confidence: **99.31%**
539. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/KeyEmbedderResponder.java`** -> AI Confidence: **99.31%**
540. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/FlutterEngineConnectionRegistry.java`** -> AI Confidence: **99.31%**
541. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/deferredcomponents/PlayStoreDeferredComponentManager.java`** -> AI Confidence: **99.31%**
542. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/LifecycleChannel.java`** -> AI Confidence: **99.31%**
543. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/ScribeChannel.java`** -> AI Confidence: **99.31%**
544. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/TextInputChannel.java`** -> AI Confidence: **99.31%**
545. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/common/JSONUtil.java`** -> AI Confidence: **99.31%**
546. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/editing/InputConnectionAdaptor.java`** -> AI Confidence: **99.31%**
547. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/editing/TextInputPlugin.java`** -> AI Confidence: **99.31%**
548. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/localization/LocalizationPlugin.java`** -> AI Confidence: **99.31%**
549. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/platform/PlatformPlugin.java`** -> AI Confidence: **99.31%**
550. **`engine/src/flutter/shell/platform/android/io/flutter/view/AccessibilityBridge.java`** -> AI Confidence: **99.31%**
551. **`engine/src/flutter/testing/fuchsia/run_tests.py`** -> AI Confidence: **99.31%**
552. **`engine/src/flutter/testing/run_tests.py`** -> AI Confidence: **99.31%**
553. **`engine/src/flutter/tools/download_fuchsia_sdk.py`** -> AI Confidence: **99.31%**
554. **`engine/src/flutter/tools/fuchsia/build_fuchsia_artifacts.py`** -> AI Confidence: **99.31%**
555. **`bin/internal/content_aware_hash.sh`** -> AI Confidence: **99.29%**
556. **`bin/internal/last_engine_commit.sh`** -> AI Confidence: **99.29%**
557. **`bin/internal/update_dart_sdk.sh`** -> AI Confidence: **99.29%**
558. **`engine/src/flutter/ci/clang_tidy.sh`** -> AI Confidence: **99.29%**
559. **`engine/src/flutter/lib/web_ui/dev/felt`** -> AI Confidence: **99.29%**
560. **`engine/src/flutter/testing/analyze_core_dump.sh`** -> AI Confidence: **99.29%**
561. **`engine/src/flutter/tools/fuchsia/devshell/lib/vars.sh`** -> AI Confidence: **99.29%**
562. **`engine/src/flutter/tools/fuchsia/devshell/run_integration_test.sh`** -> AI Confidence: **99.29%**
563. **`engine/src/flutter/tools/vscode_workspace/refresh.sh`** -> AI Confidence: **99.29%**
564. **`bin/internal/content_aware_hash.ps1`** -> AI Confidence: **99.29%**
565. **`bin/internal/last_engine_commit.ps1`** -> AI Confidence: **99.29%**
566. **`bin/internal/update_dart_sdk.ps1`** -> AI Confidence: **99.29%**
567. **`dev/integration_tests/pure_android_host_apps/host_app_kotlin_gradle_dsl/settings.gradle.kts`** -> AI Confidence: **99.29%**
568. **`dev/benchmarks/microbenchmarks/ios/Runner/main.m`** -> AI Confidence: **99.29%**
569. **`dev/benchmarks/platform_channels_benchmarks/ios/Runner/main.m`** -> AI Confidence: **99.29%**
570. **`dev/integration_tests/ios_add2app_life_cycle/ios_add2app/main.m`** -> AI Confidence: **99.29%**
571. **`dev/integration_tests/ios_host_app/Host/main.m`** -> AI Confidence: **99.29%**
572. **`engine/src/flutter/display_list/testing/dl_test_surface_provider_metal.mm`** -> AI Confidence: **99.29%**
573. **`engine/src/flutter/fml/platform/darwin/concurrent_message_loop_factory.mm`** -> AI Confidence: **99.29%**
574. **`engine/src/flutter/fml/platform/darwin/message_loop_darwin.mm`** -> AI Confidence: **99.29%**
575. **`engine/src/flutter/fml/platform/darwin/platform_version.mm`** -> AI Confidence: **99.29%**
576. **`engine/src/flutter/fml/platform/darwin/string_range_sanitization.mm`** -> AI Confidence: **99.29%**
577. **`engine/src/flutter/impeller/golden_tests/metal_screenshot.mm`** -> AI Confidence: **99.29%**
578. **`engine/src/flutter/impeller/golden_tests/vulkan_screenshotter.mm`** -> AI Confidence: **99.29%**
579. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pass_bindings_cache_mtl.mm`** -> AI Confidence: **99.29%**
580. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pipeline_mtl.mm`** -> AI Confidence: **99.29%**
581. **`engine/src/flutter/impeller/renderer/backend/metal/formats_mtl.mm`** -> AI Confidence: **99.29%**
582. **`engine/src/flutter/impeller/renderer/backend/metal/pass_bindings_cache_mtl.mm`** -> AI Confidence: **99.29%**
583. **`engine/src/flutter/impeller/renderer/backend/metal/pipeline_mtl.mm`** -> AI Confidence: **99.29%**
584. **`engine/src/flutter/impeller/renderer/backend/metal/sampler_mtl.mm`** -> AI Confidence: **99.29%**
585. **`engine/src/flutter/impeller/renderer/backend/metal/shader_function_mtl.mm`** -> AI Confidence: **99.29%**
586. **`engine/src/flutter/impeller/renderer/backend/metal/shader_library_mtl.mm`** -> AI Confidence: **99.29%**
587. **`engine/src/flutter/impeller/renderer/backend/metal/swapchain_transients_mtl.mm`** -> AI Confidence: **99.29%**
588. **`engine/src/flutter/impeller/renderer/backend/metal/texture_wrapper_mtl.mm`** -> AI Confidence: **99.29%**
589. **`engine/src/flutter/shell/common/shell_test_platform_view_metal.mm`** -> AI Confidence: **99.29%**
590. **`engine/src/flutter/shell/platform/darwin/common/buffer_conversions.mm`** -> AI Confidence: **99.29%**
591. **`engine/src/flutter/shell/platform/darwin/common/command_line.mm`** -> AI Confidence: **99.29%**
592. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterBinaryMessengerRelay.mm`** -> AI Confidence: **99.29%**
593. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterChannels.mm`** -> AI Confidence: **99.29%**
594. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterCodecs.mm`** -> AI Confidence: **99.29%**
595. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterStandardCodec.mm`** -> AI Confidence: **99.29%**
596. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterStandardCodec_Internal.h`** -> AI Confidence: **99.29%**
597. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterTestUtils.mm`** -> AI Confidence: **99.29%**
598. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/flutter_codecs_unittest.mm`** -> AI Confidence: **99.29%**
599. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterChannelKeyResponder.mm`** -> AI Confidence: **99.29%**
600. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterOverlayView.mm`** -> AI Confidence: **99.29%**
601. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterRestorationPlugin.mm`** -> AI Confidence: **99.29%**
602. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextureRegistryRelay.mm`** -> AI Confidence: **99.29%**
603. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/SemanticsObjectTestMocks.h`** -> AI Confidence: **99.29%**
604. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/TextInputSemanticsObject.mm`** -> AI Confidence: **99.29%**
605. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/platform_message_response_darwin.mm`** -> AI Confidence: **99.29%**
606. **`engine/src/flutter/shell/platform/darwin/ios/ios_external_texture_metal.mm`** -> AI Confidence: **99.29%**
607. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterExternalTexture.mm`** -> AI Confidence: **99.29%**
608. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardLayout.mm`** -> AI Confidence: **99.29%**
609. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformViewController.mm`** -> AI Confidence: **99.29%**
610. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterSurface.mm`** -> AI Confidence: **99.29%**
611. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewControllerTestUtils.mm`** -> AI Confidence: **99.29%**
612. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_metal.mm`** -> AI Confidence: **99.29%**
613. **`engine/src/flutter/testing/ios/IosBenchmarks/IosBenchmarks/main.mm`** -> AI Confidence: **99.29%**
614. **`engine/src/flutter/testing/ios/IosUnitTests/App/main.m`** -> AI Confidence: **99.29%**
615. **`engine/src/flutter/testing/ios_scenario_app/ios/FlutterAppExtensionTestHost/FlutterAppExtensionTestHost/main.m`** -> AI Confidence: **99.29%**
616. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/ScenariosUITests/GoldenImage.m`** -> AI Confidence: **99.29%**
617. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/ScenariosUITests/iPadGestureTests.m`** -> AI Confidence: **99.29%**
618. **`engine/src/flutter/testing/test_metal_surface.mm`** -> AI Confidence: **99.29%**
619. **`dev/tools/gen_keycodes/data/supplemental_key_data.inc`** -> AI Confidence: **99.29%**
620. **`engine/src/flutter/benchmarking/library.h`** -> AI Confidence: **99.29%**
621. **`engine/src/flutter/common/macros.h`** -> AI Confidence: **99.29%**
622. **`engine/src/flutter/display_list/dl_paint.cc`** -> AI Confidence: **99.29%**
623. **`engine/src/flutter/display_list/effects/color_filters/dl_blend_color_filter.cc`** -> AI Confidence: **99.29%**
624. **`engine/src/flutter/fml/build_config.h`** -> AI Confidence: **99.29%**
625. **`engine/src/flutter/fml/eintr_wrapper.h`** -> AI Confidence: **99.29%**
626. **`engine/src/flutter/impeller/base/thread_safety.h`** -> AI Confidence: **99.29%**
627. **`engine/src/flutter/impeller/renderer/backend/gles/formats_gles.cc`** -> AI Confidence: **99.29%**
628. **`engine/src/flutter/lib/gpu/export.h`** -> AI Confidence: **99.29%**
629. **`engine/src/flutter/lib/ui/window/viewport_metrics.cc`** -> AI Confidence: **99.29%**
630. **`engine/src/flutter/shell/common/switch_defs.h`** -> AI Confidence: **99.29%**
631. **`engine/src/flutter/shell/platform/android/platform_view_android_delegate/platform_view_android_delegate.cc`** -> AI Confidence: **99.29%**
632. **`engine/src/flutter/shell/platform/common/public/flutter_macros.h`** -> AI Confidence: **99.29%**
633. **`engine/src/flutter/shell/platform/fuchsia/dart_pkg/zircon_ffi/macros.h`** -> AI Confidence: **99.29%**
634. **`engine/src/flutter/shell/platform/glfw/text_input_plugin.cc`** -> AI Confidence: **99.29%**
635. **`engine/src/flutter/shell/platform/linux/fl_application_test.cc`** -> AI Confidence: **99.29%**
636. **`engine/src/flutter/shell/platform/linux/fl_dart_project_test.cc`** -> AI Confidence: **99.29%**
637. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_binary_codec.h`** -> AI Confidence: **99.29%**
638. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_json_method_codec.h`** -> AI Confidence: **99.29%**
639. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_string_codec.h`** -> AI Confidence: **99.29%**
640. **`engine/src/flutter/shell/platform/windows/accessibility_bridge_windows.cc`** -> AI Confidence: **99.29%**
641. **`engine/src/flutter/tools/licenses_cpp/src/catalog_unittests.cc`** -> AI Confidence: **99.29%**
642. **`engine/src/flutter/vulkan/swiftshader_path.h`** -> AI Confidence: **99.29%**
643. **`dev/benchmarks/macrobenchmarks/web/flutter_bootstrap.js`** -> AI Confidence: **99.29%**
644. **`dev/snippets/lib/src/snippet_parser.dart`** -> AI Confidence: **99.29%**
645. **`dev/tools/android_driver_extensions/test/src/fake_adb.dart`** -> AI Confidence: **99.29%**
646. **`engine/src/flutter/lib/ui/lerp.dart`** -> AI Confidence: **99.29%**
647. **`engine/src/flutter/lib/web_ui/dev/generate_scene_test.dart`** -> AI Confidence: **99.29%**
648. **`engine/src/flutter/lib/web_ui/lib/semantics.dart`** -> AI Confidence: **99.29%**
649. **`engine/src/flutter/lib/web_ui/lib/src/engine/onscreen_logging.dart`** -> AI Confidence: **99.29%**
650. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paint_clusters.dart`** -> AI Confidence: **99.29%**
651. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paint_paragraph.dart`** -> AI Confidence: **99.29%**
652. **`engine/src/flutter/lib/web_ui/test/ui/text_style_test.dart`** -> AI Confidence: **99.29%**
653. **`engine/src/flutter/lib/web_ui/test/webparagraph/paragraph_codepoint_info_test.dart`** -> AI Confidence: **99.29%**
654. **`engine/src/flutter/testing/dart/paragraph_test.dart`** -> AI Confidence: **99.29%**
655. **`packages/flutter/lib/src/foundation/_capabilities_io.dart`** -> AI Confidence: **99.29%**
656. **`packages/flutter/lib/src/gestures/resampler.dart`** -> AI Confidence: **99.29%**
657. **`packages/flutter/lib/src/material/menu_anchor.dart`** -> AI Confidence: **99.29%**
658. **`packages/flutter/lib/src/material/navigation_bar.dart`** -> AI Confidence: **99.29%**
659. **`packages/flutter/lib/src/material/navigation_rail.dart`** -> AI Confidence: **99.29%**
660. **`packages/flutter/lib/src/services/flavor.dart`** -> AI Confidence: **99.29%**
661. **`packages/flutter/lib/src/services/flutter_version.dart`** -> AI Confidence: **99.29%**
662. **`packages/flutter/lib/src/services/text_layout_metrics.dart`** -> AI Confidence: **99.29%**
663. **`packages/flutter/lib/src/widgets/raw_tooltip.dart`** -> AI Confidence: **99.29%**
664. **`packages/flutter_tools/bin/tool_backend.dart`** -> AI Confidence: **99.29%**
665. **`packages/flutter_tools/bin/xcode_backend.dart`** -> AI Confidence: **99.29%**
666. **`packages/flutter_tools/lib/src/android/build_validation.dart`** -> AI Confidence: **99.29%**
667. **`packages/flutter_tools/lib/src/debug_adapters/error_formatter.dart`** -> AI Confidence: **99.29%**
668. **`packages/flutter_tools/lib/src/web/web_constants.dart`** -> AI Confidence: **99.29%**
669. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/loader/FlutterApplicationInfo.java`** -> AI Confidence: **99.29%**
670. **`dev/integration_tests/ios_add2app_uiscene/NativeSwiftUIExperiment/Podfile`** -> AI Confidence: **99.29%**
671. **`dev/integration_tests/ios_add2app_uiscene/NativeUIKitSwiftExperiment/Podfile`** -> AI Confidence: **99.29%**
672. **`engine/src/BUILD.gn`** -> AI Confidence: **99.29%**
673. **`engine/src/flutter/BUILD.gn`** -> AI Confidence: **99.29%**
674. **`engine/src/flutter/benchmarking/BUILD.gn`** -> AI Confidence: **99.29%**
675. **`engine/src/flutter/display_list/testing/BUILD.gn`** -> AI Confidence: **99.29%**
676. **`engine/src/flutter/fml/BUILD.gn`** -> AI Confidence: **99.29%**
677. **`engine/src/flutter/impeller/BUILD.gn`** -> AI Confidence: **99.29%**
678. **`engine/src/flutter/impeller/display_list/BUILD.gn`** -> AI Confidence: **99.29%**
679. **`engine/src/flutter/impeller/entity/BUILD.gn`** -> AI Confidence: **99.29%**
680. **`engine/src/flutter/impeller/renderer/BUILD.gn`** -> AI Confidence: **99.29%**
681. **`engine/src/flutter/impeller/toolkit/interop/BUILD.gn`** -> AI Confidence: **99.29%**
682. **`engine/src/flutter/shell/platform/BUILD.gn`** -> AI Confidence: **99.29%**
683. **`engine/src/flutter/shell/platform/embedder/BUILD.gn`** -> AI Confidence: **99.29%**
684. **`engine/src/flutter/shell/testing/BUILD.gn`** -> AI Confidence: **99.29%**
685. **`engine/src/flutter/skia/BUILD.gn`** -> AI Confidence: **99.29%**
686. **`engine/src/flutter/skia/modules/canvaskit/BUILD.gn`** -> AI Confidence: **99.29%**
687. **`engine/src/flutter/skia/modules/skcms/BUILD.gn`** -> AI Confidence: **99.29%**
688. **`engine/src/flutter/skia/modules/skshaper/BUILD.gn`** -> AI Confidence: **99.29%**
689. **`engine/src/flutter/skia/modules/skunicode/BUILD.gn`** -> AI Confidence: **99.29%**
690. **`engine/src/flutter/skwasm/BUILD.gn`** -> AI Confidence: **99.29%**
691. **`engine/src/flutter/testing/BUILD.gn`** -> AI Confidence: **99.29%**
692. **`engine/src/flutter/tools/font_subset/BUILD.gn`** -> AI Confidence: **99.29%**
693. **`engine/src/flutter/txt/BUILD.gn`** -> AI Confidence: **99.29%**
694. **`engine/src/flutter/tools/licenses_cpp/src/comments.l`** -> AI Confidence: **99.29%**
695. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_engine.h`** -> AI Confidence: **99.28%**
696. **`packages/flutter/lib/src/material/button_bar_theme.dart`** -> AI Confidence: **99.28%**
697. **`packages/flutter/lib/src/material/button_style_button.dart`** -> AI Confidence: **99.28%**
698. **`packages/flutter/lib/src/material/chip_theme.dart`** -> AI Confidence: **99.28%**
699. **`packages/flutter/lib/src/material/drawer_theme.dart`** -> AI Confidence: **99.28%**
700. **`packages/flutter/lib/src/material/navigation_drawer_theme.dart`** -> AI Confidence: **99.28%**
701. **`packages/flutter/lib/src/material/search_view_theme.dart`** -> AI Confidence: **99.28%**
702. **`packages/flutter/lib/src/material/tab_bar_theme.dart`** -> AI Confidence: **99.28%**
703. **`packages/flutter/lib/src/widgets/selectable_region.dart`** -> AI Confidence: **99.28%**
704. **`packages/flutter_tools/lib/src/localizations/localizations_utils.dart`** -> AI Confidence: **99.28%**
705. **`packages/flutter/lib/src/widgets/gesture_detector.dart`** -> AI Confidence: **99.27%**
706. **`engine/src/flutter/shell/platform/fuchsia/flutter/accessibility_bridge.h`** -> AI Confidence: **99.25%**
707. **`dev/benchmarks/macrobenchmarks/lib/src/web/recorder.dart`** -> AI Confidence: **99.25%**
708. **`engine/src/flutter/lib/web_ui/lib/src/engine/dom.dart`** -> AI Confidence: **99.25%**
709. **`engine/src/flutter/lib/web_ui/lib/src/engine/util.dart`** -> AI Confidence: **99.25%**
710. **`engine/src/flutter/lib/web_ui/lib/src/engine/view_embedder/dimensions_provider/full_page_dimensions_provider.dart`** -> AI Confidence: **99.25%**
711. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/layout.dart`** -> AI Confidence: **99.25%**
712. **`engine/src/flutter/tools/engine_tool/lib/src/commands/run_command.dart`** -> AI Confidence: **99.25%**
713. **`packages/flutter/lib/src/cupertino/route.dart`** -> AI Confidence: **99.25%**
714. **`packages/flutter/lib/src/gestures/recognizer.dart`** -> AI Confidence: **99.25%**
715. **`packages/flutter/lib/src/gestures/tap.dart`** -> AI Confidence: **99.25%**
716. **`packages/flutter/lib/src/material/adaptive_text_selection_toolbar.dart`** -> AI Confidence: **99.25%**
717. **`packages/flutter/lib/src/material/bottom_sheet.dart`** -> AI Confidence: **99.25%**
718. **`packages/flutter/lib/src/material/carousel.dart`** -> AI Confidence: **99.25%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `26` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36191` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `dev/bots/suite_runners/run_android_engine_tests.dart` (DART) -> Cumulative Risk: **684.06**
- **Archetype:** `file_cluster_11` (Distance: 16.859 IQR)
- **Magnitude:** 120.92 | **LOC:** 156 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9844%), Concurrency (99.937%)
- **Heaviest Functions:** `path.join` (Impact: 29.2), `runTest` (Impact: 15.8), `androidManifestXml.readAsStringSync` (Impact: 10.8)

### 2. `packages/flutter_tools/lib/src/base/build.dart` (DART) -> Cumulative Risk: **674.72**
- **Archetype:** `file_cluster_11` (Distance: 12.925 IQR)
- **Magnitude:** 273.5 | **LOC:** 314 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.8722%), Safety Score (89.189%)
- **Heaviest Functions:** `async` (Impact: 62.4), `toString` (Impact: 16.0), `assert` (Impact: 15.2)

### 3. `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/font_collection.dart` (DART) -> Cumulative Risk: **668.72**
- **Archetype:** `file_cluster_4` (Distance: 12.407 IQR)
- **Magnitude:** 230.58 | **LOC:** 236 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9995%), Tech Debt (99.9888%), Verification (80.0%)
- **Heaviest Functions:** `SkwasmTypeface` (Impact: 46.5), `_downloadFontAsset` (Impact: 15.7), `fontCollectionDispose` (Impact: 12.2)

### 4. `engine/src/flutter/shell/common/shell.cc` (CPP) -> Cumulative Risk: **665.53**
- **Archetype:** `file_cluster_8` (Distance: 13.91 IQR)
- **Magnitude:** 1499.22 | **LOC:** 2484 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.4049%), Cognitive Load (96.4129%)
- **Heaviest Functions:** `Shell::OnEngineHandlePlatformMessage` (Impact: 186.5), `ValidateViewportMetrics` (Impact: 38.5), `Shell::CreateShellOnPlatformThread` (Impact: 36.7)

### 5. `dev/devicelab/bin/tasks/flavors_test_ios.dart` (DART) -> Cumulative Risk: **659.35**
- **Archetype:** `file_cluster_4` (Distance: 11.712 IQR)
- **Magnitude:** 189.54 | **LOC:** 161 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Cognitive Load (99.9537%), State Flux (99.7771%), Tech Debt (99.5386%)
- **Heaviest Functions:** `_testFlavorWhenBuiltFromXcode` (Impact: 15.0), `_testInstallDebugPaidFlavor` (Impact: 10.8), `task` (Impact: 9.1)

### 6. `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsController.mm` (OBJECTIVE-C) -> Cumulative Risk: **658.43**
- **Archetype:** `file_cluster_13` (Distance: 13.497 IQR)
- **Magnitude:** 538.9 | **LOC:** 1118 | **CtrlFlow:** 93.3% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Tech Debt (99.5864%), Cognitive Load (89.5504%)
- **Heaviest Functions:** `applyMutators` (Impact: 170.4), `submitFrame` (Impact: 22.9), `bringLayersIntoView` (Impact: 15.9)

### 7. `packages/flutter_tools/bin/tool_backend.dart` (DART) -> Cumulative Risk: **657.88**
- **Archetype:** `file_cluster_4` (Distance: 14.151 IQR)
- **Magnitude:** 199.56 | **LOC:** 125 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.8841%), Safety Score (98.6279%)
- **Heaviest Functions:** `import` (Impact: 66.1), `exit` (Impact: 17.2), `pathJoin` (Impact: 4.0)

### 8. `packages/flutter_tools/lib/src/build_system/targets/darwin.dart` (DART) -> Cumulative Risk: **649.64**
- **Archetype:** `file_cluster_4` (Distance: 13.276 IQR)
- **Magnitude:** 106.94 | **LOC:** 186 | **CtrlFlow:** 48.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.996%), State Flux (99.485%), Tech Debt (89.7789%)
- **Heaviest Functions:** `import` (Impact: 23.0), `async` (Impact: 9.7), `printXcodeWarning` (Impact: 3.5)

### 9. `engine/src/flutter/display_list/dl_paint.h` (CPP) -> Cumulative Risk: **646.34**
- **Archetype:** `file_cluster_13` (Distance: 13.186 IQR)
- **Magnitude:** 224.92 | **LOC:** 245 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9997%), Documentation (96.6836%)
- **Heaviest Functions:** `setColorSource` (Impact: 4.2), `setColorFilter` (Impact: 4.2), `setImageFilter` (Impact: 4.2)

### 10. `packages/flutter_tools/lib/src/commands/channel.dart` (DART) -> Cumulative Risk: **643.49**
- **Archetype:** `file_cluster_4` (Distance: 11.498 IQR)
- **Magnitude:** 155.26 | **LOC:** 229 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Safety Score (85.6163%)
- **Heaviest Functions:** `precacheArtifacts` (Impact: 60.7), `_checkout` (Impact: 12.6), `rawOutput.add` (Impact: 3.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `engine/src/flutter/testing/android/native_activity/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/semantics/semantics.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_15` (Drift: 15.001 IQR)
- **Top Global Matches:** file_cluster_15: 15.001, file_cluster_11: 15.24, file_cluster_16: 15.345
- **Magnitude:** 4934.7 | **LOC:** 7176 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (33.499%), Tech Debt (99.9845%)
**Top Internal Functions/Classes:**
  * `visitedNodes.addAll` (Impact: 561.1)
  * `assert` (Impact: 559.2)
    * *Intent:* /// Whether the semantics tree this node belongs to is attached to a [SemanticsOwner]. /// /// This ...
  * `sendSemanticsUpdate` (Impact: 503.6)
  * `assert` (Impact: 493.9)
    * *Intent:* /// Whether the semantics tree this node belongs to is attached to a [SemanticsOwner]. /// /// This ...
  * `isFocusable` (Impact: 232.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 323`, `args: 160`, `func_start: 642`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 395`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 81`
* *Architecture:* `api: 49`, `import: 16`
* *Defense:* `safety: 495`, `doc: 1353`, `test: 16`, `immutability_locks: 204`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart:core, dart:ui, services.dart, painting.dart, vector_math_64.dart, binding.dart, semantics_event.dart, dart:math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/paragraph.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.901 IQR)
- **Top Global Matches:** file_cluster_8: 11.901, file_cluster_15: 12.015, file_cluster_17: 12.142
- **Magnitude:** 4289.8 | **LOC:** 3625 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (11.6617%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `RelayoutWhenSystemFontsChangeMixin` (Impact: 648.7)
  * `assert` (Impact: 540.3)
  * `newChildren.add` (Impact: 537.7)
  * `TextLayoutMetrics` (Impact: 537.1)
  * `_updateSelectionEndEdgeAtPlaceholderByMu` (Impact: 168.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 241`, `args: 100`, `func_start: 344`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 38`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 122`
* *Architecture:* `api: 32`, `import: 12`
* *Defense:* `safety: 192`, `doc: 140`, `immutability_locks: 253`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` object.dart, debug.dart, dart:ui, services.dart, layer.dart, selection.dart, box.dart, semantics.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/widget_inspector.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.759 IQR)
- **Top Global Matches:** file_cluster_0: 13.759, file_cluster_15: 13.829, file_cluster_11: 13.853
- **Magnitude:** 2739.18 | **LOC:** 4619 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (12.9308%), Tech Debt (99.9918%)
**Top Internal Functions/Classes:**
  * `_hitTestHelper` (Impact: 470.6)
  * `_getLayoutExplorerNode` (Impact: 356.7)
  * `InspectorSerializationDelegate` (Impact: 347.6)
  * `createState` (Impact: 283.9)
    * *Intent:* /// Remove a list of directories that should no longer be considered part /// of the local project.
  * `containerLayer.dispose` (Impact: 145.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 206`, `args: 164`, `func_start: 371`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 1`, `state_mutation: 87`, `dead_code: 6`, `planned_debt: 6`, `duplicate_logic: 58`
* *Architecture:* `io: 23`, `api: 63`, `concurrency: 23`, `import: 19`
* *Defense:* `safety: 284`, `doc: 461`, `test: 2`, `immutability_locks: 213`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.006
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` dart:collection, media_query.dart, dart:developer, framework.dart, icon_data.dart, dart:async, view.dart, basic.dart...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `engine/src/flutter/shell/platform/embedder/tests/embedder_gl_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.588 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.214 IQR)
- **Top Global Matches:** file_cluster_8: 13.588, file_cluster_7: 13.994, file_cluster_13: 14.001
- **Magnitude:** 2501.76 | **LOC:** 5380 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (80.7851%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `EmbedderTest` (Impact: 25.0)
  * `EmbedderTest` (Impact: 24.6)
  * `TEST_P` (Impact: 24.5)
  * `EmbedderTest` (Impact: 21.1)
    * *Intent:* //------------------------------------------------------------------------------ /// Test the layer ...
  * `EmbedderTest` (Impact: 20.6)
    * *Intent:* //------------------------------------------------------------------------------ /// Test the layer ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 239`, `args: 452`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2012`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 62`
* *Architecture:* `api: 2`, `concurrency: 12`, `import: 30`
* *Defense:* `doc: 40`, `test: 405`, `sync_locks: 14`, `immutability_locks: 97`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` message_loop.h, embedder_surface_gl_impeller.h, embedder_test_context_gl.h, paths.h, count_down_latch.h, gl3.h, raster_cache.h, dart_converter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/text_selection.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.839 IQR)
- **Top Global Matches:** file_cluster_13: 12.839, file_cluster_2: 12.87, file_cluster_15: 12.894
- **Magnitude:** 2494.28 | **LOC:** 4020 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.2727%), Tech Debt (99.9901%)
**Top Internal Functions/Classes:**
  * `_dragStartSelection` (Impact: 475.6)
  * `renderObject.globalToLocal` (Impact: 466.3)
    * *Intent:* /// Call [TextSelectionDelegate.selectAll] to set the current selection to /// contain the entire te...
  * `_buildMagnifier` (Impact: 436.4)
  * `selectionEnabled` (Impact: 251.7)
  * `renderObject.globalToLocal` (Impact: 119.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 133`, `args: 82`, `func_start: 172`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 20`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`, `duplicate_logic: 34`
* *Architecture:* `api: 24`, `concurrency: 6`, `import: 27`
* *Defense:* `safety: 132`, `doc: 304`, `immutability_locks: 109`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` scrollable.dart, framework.dart, transitions.dart, inherited_theme.dart, editable_text.dart, ticker_provider.dart, context_menu_controller.dart, gestures.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/selectable_region.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.418 IQR)
- **Top Global Matches:** file_cluster_15: 13.418, file_cluster_0: 13.443, file_cluster_13: 13.533
- **Magnitude:** 2466.6 | **LOC:** 3661 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.041%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `dispose` (Impact: 457.3)
  * `_scheduleSelectableUpdate` (Impact: 456.4)
  * `super.didChangeSelectables` (Impact: 392.7)
  * `_selectionStatusNotifier.dispose` (Impact: 63.1)
  * `_updateSelectionGeometry` (Impact: 40.6)
    * *Intent:* // This method can be called when the drag is not in progress. This can
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 160`, `args: 101`, `func_start: 267`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 56`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 66`
* *Architecture:* `api: 37`, `concurrency: 23`, `import: 25`
* *Defense:* `safety: 140`, `doc: 510`, `immutability_locks: 100`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` media_query.dart, text_selection_toolbar_anchors.dart, actions.dart, framework.dart, gestures.dart, dart:async, magnifier.dart, text_editing_intents.dart...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `dev/bots/analyze.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.809 IQR)
- **Top Global Matches:** file_cluster_4: 12.809, file_cluster_11: 12.837, file_cluster_16: 12.99
- **Magnitude:** 2394.72 | **LOC:** 2803 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (69.6418%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `errors.add` (Impact: 420.9)
  * `foundError` (Impact: 391.0)
  * `verifyNoBadImportsInFlutter` (Impact: 376.6)
  * `verifyTargetPlatform` (Impact: 58.1)
  * `foundError` (Impact: 37.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 194`, `args: 58`, `func_start: 258`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 8`, `state_mutation: 175`, `dead_code: 3`, `planned_debt: 8`, `duplicate_logic: 69`
* *Architecture:* `io: 125`, `api: 23`, `concurrency: 209`, `import: 22`
* *Defense:* `safety: 88`, `doc: 29`, `test: 30`, `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` results.dart, analyze.dart, avoid_future_catcherror.dart, run_command.dart, ast.dart, visitor.dart, utilities.dart, dart:typed_data...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/display_list/testing/dl_rendering_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.152 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.064 IQR)
- **Top Global Matches:** file_cluster_8: 14.152, file_cluster_13: 14.248, file_cluster_11: 14.363
- **Magnitude:** 2379.22 | **LOC:** 4901 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.3923%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lineAdjust` (Impact: 179.2)
  * `should_match` (Impact: 84.8)
  * `compareToReference` (Impact: 63.0)
  * `RenderWithClips` (Impact: 44.7)
  * `checkGroupOpacity` (Impact: 30.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 254`, `args: 281`, `func_start: 127`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1446`, `dead_code: 3`, `duplicate_logic: 43`, `orphaned_logic: 15`
* *Architecture:* `api: 11`, `import: 39`
* *Defense:* `safety: 40`, `test: 48`, `immutability_locks: 355`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dl_sampling_options.h, text_frame_skia.h, SkStream.h, dl_comparable.h, dl_test_surface_provider.h, SkTypeface.h, dl_path_builder.h, GrTypes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/object.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_15` (Drift: 14.338 IQR)
- **Top Global Matches:** file_cluster_15: 14.338, file_cluster_0: 14.496, file_cluster_11: 14.524
- **Magnitude:** 2230.92 | **LOC:** 6760 | **CtrlFlow:** 72.6% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (17.093%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `super.detach` (Impact: 386.2)
    * *Intent:* /// Release any resources held by this render object. /// /// The object that creates a RenderObject...
  * `describeSemanticsConfiguration` (Impact: 296.1)
    * *Intent:* /// Whether [performResize] for this render object is currently running.
  * `firstAncestorNodeWithCleanGeometry` (Impact: 125.2)
  * `else` (Impact: 110.2)
    * *Intent:* /// Whether this render object's layout information is dirty. /// /// This is only set in debug mode...
  * `requestVisualUpdate` (Impact: 90.6)
    * *Intent:* /// Signature for a function that is called during layout. ///
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 179`, `args: 119`, `func_start: 462`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 82`, `state_mutation: 126`, `dead_code: 6`, `planned_debt: 10`, `fragile_debt: 1`, `duplicate_logic: 110`
* *Architecture:* `api: 61`, `import: 13`
* *Defense:* `safety: 347`, `doc: 824`, `test: 2`, `immutability_locks: 100`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` debug.dart, dart:ui, layer.dart, painting.dart, scheduler.dart, binding.dart, semantics.dart, animation.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/lib/src/flutter_manifest.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_11` (Drift: 14.45 IQR)
- **Top Global Matches:** file_cluster_11: 14.45, file_cluster_16: 14.464, file_cluster_15: 14.505
- **Magnitude:** 1994.5 | **LOC:** 1080 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (39.7743%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `sharedDarwinSource` (Impact: 797.9)
  * `errors.add` (Impact: 143.0)
  * `_validateFlutter` (Impact: 89.8)
  * `_validateFonts` (Impact: 65.3)
  * `static` (Impact: 52.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 137`, `args: 41`, `func_start: 129`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 132`, `planned_debt: 1`, `duplicate_logic: 44`
* *Architecture:* `io: 3`, `api: 21`, `import: 10`
* *Defense:* `safety: 231`, `doc: 57`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.263
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` platform_plugins.dart, file_system.dart, deferred_component.dart, utils.dart, logger.dart, yaml.dart, crypto.dart, meta.dart...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.259 IQR)
- **Top Global Matches:** file_cluster_8: 12.259, file_cluster_7: 12.769, file_cluster_15: 12.816
- **Magnitude:** 1949.64 | **LOC:** 6511 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (19.8101%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test` (Impact: 142.8)
  * `_testFocusable` (Impact: 127.1)
  * `_testContainer` (Impact: 79.6)
  * `_testCheckables` (Impact: 46.9)
  * `_testLabels` (Impact: 45.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 185`, `structural_boundaries: 196`, `args: 213`, `func_start: 1789`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 357`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 207`, `orphaned_logic: 4`
* *Architecture:* `api: 6`, `concurrency: 137`, `import: 12`
* *Defense:* `safety: 161`, `doc: 3`, `test: 772`, `sync_locks: 8`, `immutability_locks: 617`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dart:typed_data, semantics_tester.dart, ui_web.dart, browser.dart, async.dart, rendering.dart, dart:js_interop, ui.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/common/shell_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.786 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.169 IQR)
- **Top Global Matches:** file_cluster_8: 13.786, file_cluster_13: 14.044, file_cluster_11: 14.199
- **Magnitude:** 1937.26 | **LOC:** 5118 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (84.7648%), Tech Debt (99.994%)
**Top Internal Functions/Classes:**
  * `CheckFrameTimings` (Impact: 109.4)
  * `ShellTest` (Impact: 89.7)
  * `ShellTest` (Impact: 14.5)
  * `ShellTest` (Impact: 11.4)
  * `ShellTest` (Impact: 10.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 400`, `args: 540`, `func_start: 124`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1197`, `planned_debt: 4`, `duplicate_logic: 90`, `orphaned_logic: 15`
* *Architecture:* `api: 9`, `concurrency: 12`, `import: 45`
* *Defense:* `safety: 139`, `doc: 3`, `test: 416`, `sync_locks: 2`, `immutability_locks: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` vulkan_application.h, message_loop.h, vsync_waiter_fallback.h, clip_rect_layer.h, switches.h, shell_test.h, thread, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/proxy_box.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.526 IQR)
- **Top Global Matches:** file_cluster_15: 13.526, file_cluster_0: 13.529, file_cluster_17: 13.649
- **Magnitude:** 1865.82 | **LOC:** 4820 | **CtrlFlow:** 60.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.1877%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `properties.add` (Impact: 337.0)
    * *Intent:* /// Applies a filter to the existing painted content and then paints [child]. /// /// This effect is...
  * `properties.add` (Impact: 79.6)
  * `markNeedsPaint` (Impact: 58.3)
    * *Intent:* /// The image filter to apply to the existing painted content. /// /// For example, consider using [...
  * `DiagnosticsProperty` (Impact: 37.2)
  * `description.add` (Impact: 37.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 234`, `args: 176`, `func_start: 455`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 71`, `state_mutation: 70`, `dead_code: 4`, `duplicate_logic: 145`
* *Architecture:* `api: 46`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 226`, `doc: 570`, `immutability_locks: 50`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.348
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` object.dart, layer.dart, dart:ui, services.dart, box.dart, binding.dart, semantics.dart, image_filter_config.dart...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/material/switch.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.571 IQR)
- **Top Global Matches:** file_cluster_17: 13.571, file_cluster_0: 13.635, file_cluster_15: 13.702
- **Magnitude:** 1844.64 | **LOC:** 2398 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (23.7688%), Tech Debt (76.4313%)
**Top Internal Functions/Classes:**
  * `createState` (Impact: 335.4)
    * *Intent:* /// {@template flutter.material.switch.trackColor} /// The color of this [Switch]'s track. /// /// R...
  * `build` (Impact: 320.1)
    * *Intent:* /// The color for the button's [Material] when it has the input focus.
  * `paint` (Impact: 92.9)
  * `padding` (Impact: 71.1)
  * `assert` (Impact: 53.7)
    * *Intent:* /// Creates a Material Design switch.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 253`, `args: 71`, `func_start: 294`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 118`, `duplicate_logic: 24`
* *Architecture:* `api: 12`, `import: 14`
* *Defense:* `safety: 327`, `doc: 121`, `immutability_locks: 175`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` colors.dart, theme_data.dart, debug.dart, dart:ui, color_scheme.dart, constants.dart, cupertino.dart, switch_theme.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/lib/src/commands/daemon.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 14.395 IQR)
- **Top Global Matches:** file_cluster_4: 14.395, file_cluster_11: 14.468, file_cluster_16: 14.531
- **Magnitude:** 1841.84 | **LOC:** 1941 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (44.7794%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `_onExitCompleter.completeError` (Impact: 65.3)
  * `getSupportedPlatforms` (Impact: 63.9)
  * `subscription.cancel` (Impact: 59.8)
  * `Unknown_Block` (Impact: 45.5)
  * `tempDirectory` (Impact: 43.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 239`, `args: 126`, `func_start: 309`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 146`, `planned_debt: 2`, `duplicate_logic: 86`
* *Architecture:* `io: 44`, `api: 41`, `concurrency: 325`, `import: 30`
* *Defense:* `safety: 417`, `doc: 82`, `sync_locks: 14`, `immutability_locks: 199`, `cleanup: 21`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` uuid.dart, common.dart, debounce_data_stream.dart, logger.dart, run_cold.dart, run_hot.dart, utils.dart, android_workflow.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/impeller/display_list/canvas.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.411 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.816 IQR)
- **Top Global Matches:** file_cluster_13: 14.411, file_cluster_8: 14.475, file_cluster_11: 14.715
- **Magnitude:** 1833.04 | **LOC:** 2392 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (85.8709%), Tech Debt (99.5315%)
**Top Internal Functions/Classes:**
  * `Canvas::GetLocalCoverageLimit` (Impact: 161.9)
  * `Canvas::SetupRenderPass` (Impact: 148.5)
  * `Canvas::AttemptDrawBlur` (Impact: 40.1)
  * `Canvas::AddRenderEntityWithFiltersToCurr` (Impact: 37.4)
  * `Canvas::AttemptColorFilterOptimization` (Impact: 27.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 183`, `args: 143`, `func_start: 68`
* *Risk/State:* `state_mutation: 959`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 5`, `orphaned_logic: 57`
* *Architecture:* `import: 53`
* *Defense:* `safety: 40`, `doc: 20`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` solid_rsuperellipse_blur_contents.h, dl_color_source.h, dl_vertices.h, arc_geometry.h, text_shadow_cache.h, text_contents.h, memory, ellipse_geometry.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/display_list/dl_builder.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.005 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.962 IQR)
- **Top Global Matches:** file_cluster_8: 14.005, file_cluster_13: 14.168, file_cluster_11: 14.261
- **Magnitude:** 1783.28 | **LOC:** 2107 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.2114%), Tech Debt (99.6201%)
**Top Internal Functions/Classes:**
  * `DisplayListBuilder::TransformFullPerspec` (Impact: 117.2)
  * `DisplayListBuilder::PaintResult` (Impact: 71.5)
  * `DisplayListBuilder::paint_nops_on_transp` (Impact: 40.6)
  * `DisplayListBuilder::onSetColorSource` (Impact: 36.6)
  * `DisplayListBuilder::onSetImageFilter` (Impact: 36.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 125`, `args: 59`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 981`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 58`
* *Architecture:* `import: 13`
* *Defense:* `safety: 9`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dl_mask_filter.h, dl_geometry_conversions.h, logging.h, dl_op_flags.h, dl_op_records.h, dl_accumulation_rect.h, display_list.h, dl_builder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/editable.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.379 IQR)
- **Top Global Matches:** file_cluster_15: 13.379, file_cluster_17: 13.49, file_cluster_8: 13.53
- **Magnitude:** 1762.82 | **LOC:** 3157 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.9074%), Tech Debt (99.9671%)
**Top Internal Functions/Classes:**
  * `TextLayoutMetrics` (Impact: 566.6)
  * `assert` (Impact: 311.5)
  * `paint` (Impact: 43.2)
  * `describeSemanticsConfiguration` (Impact: 42.1)
  * `paint` (Impact: 33.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 189`, `args: 109`, `func_start: 298`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 4`, `duplicate_logic: 27`, `orphaned_logic: 27`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 200`, `doc: 405`, `immutability_locks: 113`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` object.dart, layer.dart, dart:ui, services.dart, custom_paint.dart, paragraph.dart, viewport_offset.dart, box.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/impeller/entity/entity_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.86 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.219 IQR)
- **Top Global Matches:** file_cluster_8: 13.86, file_cluster_13: 13.933, file_cluster_2: 14.111
- **Magnitude:** 1741.66 | **LOC:** 2934 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (91.8423%), Tech Debt (99.9721%)
**Top Internal Functions/Classes:**
  * `TEST_P` (Impact: 39.5)
  * `TEST_P` (Impact: 38.4)
  * `TEST_P` (Impact: 38.4)
  * `TEST_P` (Impact: 34.9)
  * `TEST_P` (Impact: 21.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 331`, `args: 380`, `func_start: 80`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 1230`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 66`, `orphaned_logic: 5`
* *Architecture:* `api: 3`, `import: 54`
* *Defense:* `safety: 39`, `test: 161`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` host_buffer.h, entity.h, render_pass.h, text_contents.h, vertex_buffer_builder.h, memory, round_superellipse_geometry.h, dl_path_builder.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterViewController.mm` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.343 IQR)
- **Top Global Matches:** file_cluster_13: 14.343, file_cluster_11: 14.431, file_cluster_8: 14.463
- **Magnitude:** 1717.1 | **LOC:** 2710 | **CtrlFlow:** 94.4% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (96.5338%), Tech Debt (98.7663%)
**Top Internal Functions/Classes:**
  * `isKeyboardNotificationForDifferentView` (Impact: 303.6)
  * `handleKeyboardAnimationCallbackWithTarge` (Impact: 257.6)
  * `onAccessibilityStatusChanged` (Impact: 60.8)
    * *Intent:* // If the UIApplicationSupportsIndirectInputEvents in Info.plist returns YES, then the platform // d...
  * `performOrientationUpdate` (Impact: 28.0)
  * `hoverEvent` (Impact: 25.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 268`, `structural_boundaries: 16`, `args: 161`, `func_start: 111`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 634`, `planned_debt: 8`, `fragile_debt: 1`, `duplicate_logic: 10`, `orphaned_logic: 24`
* *Architecture:* `io: 5`, `api: 21`, `concurrency: 12`, `import: 31`
* *Defense:* `safety: 49`, `doc: 14`, `immutability_locks: 22`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` message_loop.h, FlutterKeyPrimaryResponder.h, FlutterEngine_Internal.h, log.h, spring_animation.h, vsync_waiter_ios.h, memory, FlutterPlatformViews_Internal.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.692 IQR)
- **Top Global Matches:** file_cluster_8: 13.692, file_cluster_11: 13.996, file_cluster_13: 14.026
- **Magnitude:** 1658.58 | **LOC:** 4213 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.4089%), Tech Debt (99.8939%)
**Top Internal Functions/Classes:**
  * `testTextEditingDeltasAreBatchedAndForwar` (Impact: 112.8)
  * `testTextEditingDeltasAreGeneratedOnTextI` (Impact: 49.7)
  * `testInteractiveKeyboardAfterUserScrollTo` (Impact: 33.3)
  * `testInteractiveKeyboardKeyboardReappears` (Impact: 26.3)
  * `testInteractiveKeyboardScreenshotWillBeM` (Impact: 26.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 31`, `args: 544`, `func_start: 152`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 741`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 33`, `orphaned_logic: 87`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 99`, `test: 333`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FlutterMacros.h, FlutterEngine.h, FlutterViewController.h, FlutterBinaryMessengerRelay.h, XCTest.h, OCMock.h, FlutterEngine_Test.h, FlutterTextInputPlugin.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/embedder/tests/embedder_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.48 IQR)
- **Local Micro-Species:** `Cluster 2: Verification & Unit Testing` (Drift: 5.438 IQR)
- **Top Global Matches:** file_cluster_8: 13.48, file_cluster_13: 13.766, file_cluster_7: 13.828
- **Magnitude:** 1592.14 | **LOC:** 4344 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (74.1142%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `EmbedderTest` (Impact: 22.4)
  * `EmbedderTest` (Impact: 17.0)
  * `EmbedderTest` (Impact: 16.5)
  * `UnserializeKeyEventDeviceType` (Impact: 14.7)
  * `UnserializeKeyEventType` (Impact: 11.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 231`, `args: 400`, `func_start: 72`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 1137`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 63`
* *Architecture:* `concurrency: 48`, `import: 29`
* *Defense:* `safety: 3`, `doc: 58`, `test: 294`, `sync_locks: 24`, `immutability_locks: 76`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` message_loop.h, pthread.h, embedder_engine.h, paths.h, count_down_latch.h, raster_cache.h, dart_converter.h, file.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/lib/src/artifacts.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.079 IQR)
- **Top Global Matches:** file_cluster_8: 11.079, file_cluster_7: 11.367, file_cluster_0: 11.452
- **Magnitude:** 1556.98 | **LOC:** 1772 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.703%), Tech Debt (99.7471%)
**Top Internal Functions/Classes:**
  * `localEngineInfo` (Impact: 373.6)
  * `usesLocalArtifacts` (Impact: 119.3)
  * `_getIosArtifactPath` (Impact: 88.3)
  * `_getHostArtifactPath` (Impact: 88.0)
  * `_artifactToFileName` (Impact: 81.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 250`, `args: 55`, `func_start: 136`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 9`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 33`
* *Architecture:* `io: 53`, `api: 19`, `import: 12`
* *Defense:* `safety: 110`, `doc: 127`, `test: 4`, `immutability_locks: 127`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.898
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cache.dart, globals.dart, process.dart, memory.dart, utils.dart, common.dart, platform.dart, user_messages.dart...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `engine/src/flutter/shell/platform/android/platform_view_android_jni_impl.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.252 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.046 IQR)
- **Top Global Matches:** file_cluster_8: 13.252, file_cluster_13: 13.561, file_cluster_7: 13.712
- **Magnitude:** 1513.6 | **LOC:** 2412 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 57.1%
- **Risk Profile:** Cognitive Load (93.088%), Tech Debt (97.5849%)
**Top Internal Functions/Classes:**
  * `PlatformViewAndroid::Register` (Impact: 85.8)
  * `PlatformViewAndroidJNIImpl::onDisplayPla` (Impact: 73.0)
  * `PlatformViewAndroidJNIImpl::FlutterViewO` (Impact: 65.6)
  * `RegisterApi` (Impact: 37.3)
  * `SpawnJNI` (Impact: 17.2)
    * *Intent:* // Signature is similar to RunBundleAndSnapshotFromLibrary but it can't change // the bundle path or...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 311`, `args: 139`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 847`, `planned_debt: 7`, `duplicate_logic: 18`, `orphaned_logic: 32`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 20`, `immutability_locks: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` platform_view_android_jni.h, android_shell_holder.h, jni_util.h, jni.h, native_window_jni.h, jni_weak_ref.h, scoped_java_ref.h, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `engine/src/flutter/tools/githooks/lib/src/post_checkout_command.dart` (DART) | Magnitude: 0.01 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 4, decorators: 3, func_start: 2
- `packages/flutter/lib/src/animation/animation_style.dart` (DART) | Magnitude: 111.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, branch: 38, safety: 29, doc: 26
- `packages/flutter_tools/lib/src/convert.dart` (DART) | Magnitude: 40.2 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 15, doc: 10, immutability_locks: 10
- `dev/tools/gen_defaults/lib/input_chip_template.dart` (DART) | Magnitude: 0.05 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 96, branch: 29, safety: 28, structural_boundaries: 20
- `engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/canvaskit_api.dart` (DART) | Magnitude: 759.76 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1213, func_start: 612, structural_boundaries: 257, encapsulation: 232

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `bin/internal/shared.sh` (SHELL) | Magnitude: 154.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 119, branch: 86, io: 43, state_mutation: 40
- `packages/flutter_tools/lib/src/build_system/targets/ios.dart` (DART) | Magnitude: 362.14 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 319, structural_boundaries: 79, func_start: 61, immutability_locks: 59
- `dev/integration_tests/widget_preview_scaffold/lib/src/utils/url/_url_web.dart` (DART) | Magnitude: 11.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, branch: 9, globals: 9, func_start: 6
- `packages/flutter_tools/templates/widget_preview_scaffold/lib/src/utils/url/_url_web.dart.tmpl` (DART) | Magnitude: 11.6 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, branch: 9, globals: 9, func_start: 6
- `packages/flutter_tools/lib/src/flutter_manifest.dart` (DART) | Magnitude: 1994.5 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 762, branch: 375, safety: 231, closures: 149

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `engine/src/flutter/tools/fuchsia/devshell/run_integration_test.sh` (SHELL) | Magnitude: 0.21 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 103, indent_spaces: 78, branch: 68, reflection_metaprogramming: 36
- `engine/src/flutter/ci/check_build_configs.sh` (SHELL) | Magnitude: 4.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 16, reflection_metaprogramming: 9, branch: 8
- `engine/src/flutter/shell/platform/darwin/common/framework/Headers/FlutterMacros.h` (CPP) | Magnitude: 16.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 19, reflection_metaprogramming: 11, branch: 5, doc: 2
- `engine/src/flutter/tools/find_pubspecs_to_workspacify.sh` (SHELL) | Magnitude: 0.04 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 19, branch: 15, structural_boundaries: 9
- `dev/tools/gen_keycodes/bin/gen_keycodes` (SHELL) | Magnitude: 0.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 14, indent_spaces: 9, reflection_metaprogramming: 7, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/flutter/lib/src/material/menu_anchor.dart` (DART) | Magnitude: 1366.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 1298, doc: 483, branch: 423, safety: 283
- `packages/flutter_tools/lib/src/macos/swift_packages.dart` (DART) | Magnitude: 109.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 121, doc: 41, immutability_locks: 37, encapsulation: 29
- `engine/src/flutter/lib/ui/painting/gradient.cc` (CPP) | Magnitude: 124.38 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 76, branch: 13, args: 9
- `dev/devicelab/bin/tasks/hot_mode_dev_cycle_ios_simulator.dart` (DART) | Magnitude: 25.4 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, func_start: 8, concurrency: 8
- `engine/src/flutter/tools/mcp/bin/main.dart` (DART) | Magnitude: 0.01 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 5, func_start: 5, import: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `engine/src/flutter/lib/web_ui/lib/src/engine/frame_timing_recorder.dart` (DART) | Magnitude: 98.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 85, encapsulation: 53, doc: 21, branch: 18
- `packages/flutter/lib/src/widgets/tap_region.dart` (DART) | Magnitude: 261.82 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 219, indent_spaces: 190, branch: 50, func_start: 41
- `packages/flutter/lib/src/widgets/toggleable.dart` (DART) | Magnitude: 277.22 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 221, doc: 126, encapsulation: 95, func_start: 71
- `packages/flutter/lib/src/rendering/proxy_box.dart` (DART) | Magnitude: 1865.82 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1735, doc: 570, func_start: 455, encapsulation: 390
- `packages/flutter/lib/src/widgets/shortcuts.dart` (DART) | Magnitude: 266.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 404, indent_spaces: 339, encapsulation: 70, branch: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `engine/src/flutter/impeller/geometry/point.h` (CPP) | Magnitude: 334.98 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 218, structural_boundaries: 196, state_mutation: 170, immutability_locks: 159
- `packages/flutter_driver/lib/src/common/wait.dart` (DART) | Magnitude: 90.6 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 119, doc: 55, structural_boundaries: 39, closures: 34
- `packages/flutter_test/lib/src/stack_manipulation.dart` (DART) | Magnitude: 20.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, doc: 9, func_start: 8, branch: 7
- `engine/src/flutter/tools/engine_tool/bin/et.dart` (DART) | Magnitude: 0.02 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, closures: 1
- `dev/tools/android_driver_extensions/test/src/fake_process_manager.dart` (DART) | Magnitude: 0.03 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 11, generics: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/flutter_tools/lib/src/android/android_console.dart` (DART) | Magnitude: 70.78 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, encapsulation: 20, func_start: 16, structural_boundaries: 15
- `packages/flutter/lib/src/widgets/display_feature_sub_screen.dart` (DART) | Magnitude: 209.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, doc: 75, branch: 41, closures: 30
- `packages/flutter/lib/src/material/ink_well.dart` (DART) | Magnitude: 932.96 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 574, doc: 251, branch: 163, encapsulation: 128
- `packages/flutter_tools/gradle/src/main/kotlin/tasks/DeepLinkJsonFromManifestTaskHelper.kt` (KOTLIN) | Magnitude: 77.5 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, state_mutation: 37, immutability_locks: 22, args: 20
- `packages/flutter/lib/src/foundation/annotations.dart` (DART) | Magnitude: 16.16 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 43, immutability_locks: 4, indent_spaces: 4, dead_code: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/flutter/lib/src/foundation/licenses.dart` (DART) | Magnitude: 148.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 136, doc: 96, branch: 36, func_start: 29
- `packages/flutter/lib/src/material/refresh_indicator.dart` (DART) | Magnitude: 382.74 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 317, encapsulation: 139, doc: 118, branch: 94
- `packages/flutter/lib/src/material/paginated_data_table.dart` (DART) | Magnitude: 74.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 123, doc: 60, ui_framework: 35, structural_boundaries: 22
- `packages/flutter_tools/templates/widget_preview_scaffold/lib/src/utils.dart.tmpl` (DART) | Magnitude: 54.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, safety: 37, structural_boundaries: 24, ui_framework: 21
- `dev/integration_tests/widget_preview_scaffold/lib/src/utils.dart` (DART) | Magnitude: 54.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, safety: 37, structural_boundaries: 24, ui_framework: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `engine/src/flutter/tools/engine_tool/lib/src/commands/test_command.dart` (DART) | Magnitude: 0.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 23, concurrency: 16, immutability_locks: 14
- `engine/src/flutter/lib/web_ui/lib/src/engine/initialization.dart` (DART) | Magnitude: 71.34 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, doc: 47, concurrency: 23, encapsulation: 23
- `dev/tools/android_driver_extensions/test/src/fake_adb.dart` (DART) | Magnitude: 0.13 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 57, branch: 46, safety: 40, concurrency: 33
- `dev/integration_tests/external_textures/android/app/src/main/java/io/flutter/externalui/MainActivity.java` (JAVA) | Magnitude: 178.72 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 50, concurrency: 36, import: 23
- `engine/src/flutter/lib/web_ui/dev/roll_fallback_fonts.dart` (DART) | Magnitude: 424.48 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 440, state_mutation: 103, doc: 103, immutability_locks: 89

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `engine/src/flutter/shell/platform/fuchsia/flutter/tests/fakes/scenic/fake_flatland.cc` (CPP) | Magnitude: 537.86 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 645, state_mutation: 321, structural_boundaries: 160, branch: 83
- `packages/flutter/lib/src/widgets/preferred_size.dart` (DART) | Magnitude: 5.54 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 39, structural_boundaries: 6, indent_spaces: 6, ui_framework: 3
- `packages/flutter_tools/lib/src/web/web_constants.dart` (DART) | Magnitude: 12.6 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 4, globals: 2, immutability_locks: 2, indent_spaces: 2
- `engine/src/flutter/shell/platform/glfw/client_wrapper/testing/stub_flutter_glfw_api.h` (CPP) | Magnitude: 58.96 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 42, indent_spaces: 37, func_start: 19, api: 19
- `engine/src/flutter/ci/compatibility_helper.py` (PYTHON) | Magnitude: 7.48 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, api: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `packages/flutter/lib/src/dart_plugin_registrant.dart` (DART) | Magnitude: 12.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, api: 1, decorators: 1, immutability_locks: 1
- `engine/src/flutter/lib/ui/semantics.dart` (DART) | Magnitude: 120.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 499, indent_spaces: 412, safety: 98, encapsulation: 81
- `packages/flutter/lib/src/scheduler/debug.dart` (DART) | Magnitude: 6.9 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 59, indent_spaces: 7, structural_boundaries: 4, closures: 3
- `engine/src/flutter/impeller/toolkit/interop/impeller.h` (CPP) | Magnitude: 18.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 490, indent_spaces: 68, args: 49, structural_boundaries: 20
- `dev/devicelab/bin/tasks/smoke_test_setup_failure.dart` (DART) | Magnitude: 3.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 9, concurrency: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTest.mm` (OBJECTIVE-C) | Magnitude: 485.82 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 744, state_mutation: 370, args: 218, pointers: 79
- `engine/src/flutter/shell/platform/windows/keyboard_handler_base.h` (CPP) | Magnitude: 25.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, state_mutation: 9, args: 3
- `engine/src/flutter/txt/src/skia/paragraph_builder_skia.h` (CPP) | Magnitude: 15.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, import: 3, indent_spaces: 3, macros: 2
- `engine/src/flutter/flutter_frontend_server/test/to_string_test.dart` (DART) | Magnitude: 44.64 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 76, immutability_locks: 20, state_mutation: 18, func_start: 14
- `engine/src/flutter/lib/web_ui/lib/ui_web/src/ui_web/browser_detection.dart` (DART) | Magnitude: 11.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, branch: 17, doc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/flutter_tools/bin/xcode_backend.sh` (SHELL) | Magnitude: 25.08 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 15, indent_spaces: 9, reflection_metaprogramming: 7, branch: 4
- `engine/src/flutter/flow/stopwatch_dl.h` (CPP) | Magnitude: 19.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, indent_spaces: 17, state_mutation: 15, immutability_locks: 7
- `packages/flutter/lib/src/widgets/_web_browser_detection_io.dart` (DART) | Magnitude: 12.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, func_start: 1, class_start: 1
- `bin/internal/update_engine_version.sh` (SHELL) | Magnitude: 39.08 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 14, safety: 7, reflection_metaprogramming: 7
- `bin/internal/content_aware_hash.sh` (SHELL) | Magnitude: 52.4 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 24, state_mutation: 23, indent_spaces: 18, io: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `dev/bots/check_tests_cross_imports.dart` -> Churn: **100.0%** | Cog Load: 3.5074% | Debt: 93.6719%
- `engine/src/flutter/lib/ui/painting.dart` -> Churn: **84.37%** | Cog Load: 7.5877% | Debt: 99.9946%
- `packages/flutter_tools/lib/src/commands/run.dart` -> Churn: **73.92%** | Cog Load: 35.5026% | Debt: 86.9466%
- `packages/flutter_tools/lib/src/runner/flutter_command.dart` -> Churn: **70.01%** | Cog Load: 25.2729% | Debt: 72.1188%
- `engine/src/flutter/impeller/entity/entity_unittests.cc` -> Churn: **65.45%** | Cog Load: 91.8423% | Debt: 99.9721%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/flutter/lib/src/widgets/selectable_region.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 2466.6
- `engine/src/flutter/display_list/testing/dl_rendering_unittests.cc` -> **bungeman** (100.0% isolated ownership) | Magnitude: 2379.22
- `engine/src/flutter/display_list/dl_builder.cc` -> **b-luk** (100.0% isolated ownership) | Magnitude: 1783.28
- `packages/flutter/lib/src/rendering/editable.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 1762.82
- `packages/flutter_tools/lib/src/artifacts.dart` -> **Valentin Haudiquet** (100.0% isolated ownership) | Magnitude: 1556.98

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `engine/src/flutter/shell/platform/android/io/flutter/embedding/android/FlutterView.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 75.6892%)
- `engine/src/flutter/shell/platform/android/io/flutter/plugin/platform/PlatformViewsController2.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 82.4078%)
- `engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/FlutterJNI.java` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 24.2772%)
- `engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/dart/DartExecutor.java` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 23.8321%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 28.4702%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `engine/src/flutter/skwasm/string.cc` -> **Severity: 1602.6** (Blast Radius: 16.026 * Doc Risk: 100.0%)
- `engine/src/flutter/shell/platform/android/io/flutter/Log.java` -> **Severity: 413.325** (Blast Radius: 4.136 * Doc Risk: 99.9336%)
- `engine/src/flutter/shell/platform/android/io/flutter/Build.java` -> **Severity: 313.584** (Blast Radius: 3.136 * Doc Risk: 99.9949%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 285.253** (Blast Radius: 19.144 * Doc Risk: 14.9004%)
- `engine/src/flutter/shell/platform/darwin/macos/framework/Headers/FlutterMacOS.h` -> **Severity: 157.313** (Blast Radius: 2.435 * Doc Risk: 64.6048%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
