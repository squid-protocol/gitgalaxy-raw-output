# ARCHITECTURAL_BRIEF: flutter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/flutter` |
| **Timestamp** | `2026-08-03T20:16:00.875813+00:00` |
| **Scan Duration** | `31.1s` |
| **Git Branch** | `master` |
| **Git Commit** | `75910740753c13a858bb39c3686afb71675e8dc4` |
| **Git Remote** | `https://github.com/flutter/flutter` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 7182 malicious artifacts.

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
| Total Artifacts | 15525 |
| Analyzed Artifacts (Scanned) | 8544 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6981 |
| Total LOC | 914768 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.0% |
| Dominant Lang | CPP |

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
> **Architectural Drift Z-Score:** `4.979`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 4199 | 49.1% |
| file_cluster_13 | 2974 | 34.8% |
| file_cluster_0 | 280 | 3.3% |
| file_cluster_4 | 250 | 2.9% |
| file_cluster_16 | 182 | 2.1% |
| file_cluster_2 | 122 | 1.4% |
| file_cluster_17 | 57 | 0.7% |
| file_cluster_15 | 47 | 0.6% |
| file_cluster_9 | 29 | 0.3% |
| file_cluster_11 | 24 | 0.3% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 25.2 | 9.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 19.9 | 7.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 13.1 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.9 | 1.3 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 15.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 31.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.3 | 0.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 86.8 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 3.2 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 32.0 | 17.0 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 10.9 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
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

- `TextLayoutMetrics` (@ `packages/flutter/lib/src/rendering/editable.dart`) -> Impact: **5939.2** | LOC: 1885
- `async` (@ `packages/flutter_tools/lib/src/vmservice.dart`) -> Impact: **4895.0** | LOC: 790
- `deleteIconColor` (@ `packages/flutter/lib/src/material/chip.dart`) -> Impact: **4054.9** | LOC: 860
  * *Intent:* /// Theme used for all icons in the chip. /// /// If this is null and [ThemeData.useMaterial3] is true, then [IconThemeData] /// with a [ColorScheme.p...
- `RelayoutWhenSystemFontsChangeMixin` (@ `packages/flutter/lib/src/rendering/paragraph.dart`) -> Impact: **3568.5** | LOC: 1578
- `import` (@ `packages/flutter/lib/src/material/app_bar_theme.dart`) -> Impact: **3162.7** | LOC: 352
- `import` (@ `packages/flutter_tools/lib/src/test/runner.dart`) -> Impact: **2962.6** | LOC: 691
- `Size.fromHeight` (@ `packages/flutter/lib/src/material/tabs.dart`) -> Impact: **2920.2** | LOC: 1491
- `_dragStartSelection` (@ `packages/flutter/lib/src/widgets/text_selection.dart`) -> Impact: **2855.4** | LOC: 1579
- `import` (@ `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart`) -> Impact: **2468.1** | LOC: 249
- `dispose` (@ `packages/flutter/lib/src/widgets/selectable_region.dart`) -> Impact: **2387.7** | LOC: 1425

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `onCreate` (@ `dev/integration_tests/pure_android_host_apps/host_app_kotlin_gradle_dsl/app/src/main/java/com/example/myapplication/MainActivity.kt`) -> **O(2^N) [Recursive]**
- `readPropertiesIfExist` (@ `packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt`) -> **O(2^N) [Recursive]**
- `register` (@ `examples/platform_channel_swift/ios/Runner/AppDelegate.swift`) -> **O(2^N) [Recursive]**
- `application` (@ `dev/benchmarks/platform_views_layout_hybrid_composition/ios/Runner/AppDelegate.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Copyright 2014 The Flutter Authors. All rights reserved. // Use of this source code is governed by a BSD-style license that can be // found in the ...
- `application` (@ `dev/integration_tests/channels/ios/Runner/AppDelegate.m`) -> **O(2^N) [Recursive]**
- `awakeFromNib` (@ `dev/integration_tests/external_textures/ios/Runner/TextureViewController.m`) -> **O(2^N) [Recursive]**
- `viewDidLoad` (@ `dev/integration_tests/ios_host_app/Host/DualFlutterViewController.m`) -> **O(2^N) [Recursive]**
  * *Intent:* // Copyright 2014 The Flutter Authors. All rights reserved. // Use of this source code is governed by a BSD-style license that can be // found in the ...
- `viewDidLoad` (@ `dev/integration_tests/ios_host_app/Host/HybridViewController.m`) -> **O(2^N) [Recursive]**
- `viewDidLoad` (@ `dev/integration_tests/ios_host_app/Host/NativeViewController.m`) -> **O(2^N) [Recursive]**
- `lock` (@ `engine/src/flutter/impeller/renderer/backend/metal/gpu_tracer_mtl.mm`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `CheckFrameTimings` (@ `engine/src/flutter/shell/common/shell_unittests.cc`) -> DB Complexity: **427**
- `foundError` (@ `dev/bots/analyze.dart`) -> DB Complexity: **283**
- `lineAdjust` (@ `engine/src/flutter/display_list/testing/dl_rendering_unittests.cc`) -> DB Complexity: **260**
- `DartIsolate::CreatePlatformIsolate` (@ `engine/src/flutter/runtime/dart_isolate.cc`) -> DB Complexity: **205**
- `applicationShouldTerminate` (@ `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTest.mm`) -> DB Complexity: **204**
- `Shell::OnEngineHandlePlatformMessage` (@ `engine/src/flutter/shell/common/shell.cc`) -> DB Complexity: **193**
- `AdvancedBlend` (@ `engine/src/flutter/impeller/entity/contents/filters/blend_filter_contents.cc`) -> DB Complexity: **189**
- `Reflector::GenerateTemplateArguments` (@ `engine/src/flutter/impeller/compiler/reflector.cc`) -> DB Complexity: **188**
- `isKeyboardNotificationForDifferentView` (@ `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterViewController.mm`) -> DB Complexity: **182**
- `import` (@ `packages/flutter_tools/lib/src/commands/build_ios_framework.dart`) -> DB Complexity: **175**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `packages/flutter/lib/src/material` | 182 | 71988.74 | 11.08% | 19.3% |
| `packages/flutter/lib/src/widgets` | 185 | 38689.2 | 8.55% | 33.15% |
| `engine/src/flutter/shell/platform/linux` | 164 | 28338.22 | 40.32% | 60.85% |
| `packages/flutter/lib/src/rendering` | 48 | 26821.7 | 7.67% | 34.57% |
| `packages/flutter_tools/lib/src` | 59 | 25124.94 | 22.22% | 18.65% |
| `engine/src/flutter/shell/platform/darwin/ios/framework/Source` | 122 | 24148.44 | 36.65% | 50.46% |
| `engine/src/flutter/shell/platform/windows` | 127 | 18428.18 | 42.54% | 52.85% |
| `engine/src/flutter/shell/platform/darwin/macos/framework/Source` | 97 | 14984.66 | 37.93% | 39.81% |
| `engine/src/flutter/shell/common` | 89 | 14833.0 | 43.7% | 53.0% |
| `engine/src/flutter/impeller/display_list` | 53 | 14530.9 | 44.99% | 61.39% |

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
- `engine/src/flutter/impeller/toolkit/interop/impeller.cc` -> **171** Orphaned Functions | **4** Duplicates
- `engine/src/flutter/shell/platform/common/text_input_model_unittests.cc` -> **0** Orphaned Functions | **154** Duplicates
- `engine/src/flutter/shell/platform/linux/fl_standard_message_codec_test.cc` -> **4** Orphaned Functions | **126** Duplicates
- `engine/src/flutter/shell/platform/linux/fl_json_message_codec_test.cc` -> **0** Orphaned Functions | **115** Duplicates
- `engine/src/flutter/flow/layers/layer_state_stack.cc` -> **34** Orphaned Functions | **79** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`dev/benchmarks/multiple_flutters/android/app/src/main/java/dev/flutter/multipleflutters/MainActivity.kt`** -> AI Confidence: **99.48%**
2. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/extensions/NativeDriverSupportPlugin.kt`** -> AI Confidence: **99.48%**
3. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/fixtures/BlueOrangeGradientSurfaceViewPlatformViewFactory.kt`** -> AI Confidence: **99.48%**
4. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/fixtures/ChangingColorButtonPlatformViewFactory.kt`** -> AI Confidence: **99.48%**
5. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/fixtures/OtherFaceTexturePlugin.kt`** -> AI Confidence: **99.48%**
6. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/fixtures/SmileyFaceTexturePlugin.kt`** -> AI Confidence: **99.48%**
7. **`dev/integration_tests/display_cutout_rotation/android/app/src/main/java/com/example/display_cutout_rotation/MainActivity.kt`** -> AI Confidence: **99.48%**
8. **`dev/integration_tests/pure_android_host_apps/host_app_kotlin_gradle_dsl/app/src/main/java/com/example/myapplication/ui/theme/Theme.kt`** -> AI Confidence: **99.48%**
9. **`packages/flutter_tools/gradle/src/main/kotlin/DependencyVersionChecker.kt`** -> AI Confidence: **99.48%**
10. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterPlugin.kt`** -> AI Confidence: **99.48%**
11. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt`** -> AI Confidence: **99.48%**
12. **`packages/flutter_tools/gradle/src/main/kotlin/plugins/PluginHandler.kt`** -> AI Confidence: **99.48%**
13. **`packages/flutter_tools/gradle/src/main/kotlin/tasks/BaseFlutterTaskHelper.kt`** -> AI Confidence: **99.48%**
14. **`packages/flutter_tools/gradle/src/main/kotlin/tasks/DeepLinkJsonFromManifestTaskHelper.kt`** -> AI Confidence: **99.48%**
15. **`packages/flutter_tools/gradle/src/test/kotlin/BaseApplicationNameHandlerTest.kt`** -> AI Confidence: **99.48%**
16. **`packages/flutter_tools/gradle/src/test/kotlin/DependencyVersionCheckerTest.kt`** -> AI Confidence: **99.48%**
17. **`packages/flutter_tools/gradle/src/test/kotlin/FlutterPluginTest.kt`** -> AI Confidence: **99.48%**
18. **`packages/flutter_tools/gradle/src/test/kotlin/FlutterPluginUtilsTest.kt`** -> AI Confidence: **99.48%**
19. **`packages/flutter_tools/gradle/src/test/kotlin/VersionFetcherTest.kt`** -> AI Confidence: **99.48%**
20. **`packages/flutter_tools/gradle/src/test/kotlin/plugins/PluginHandlerTest.kt`** -> AI Confidence: **99.48%**
21. **`packages/flutter_tools/gradle/src/test/kotlin/tasks/BaseFlutterTaskHelperTest.kt`** -> AI Confidence: **99.48%**
22. **`packages/flutter_tools/gradle/src/test/kotlin/tasks/DeepLinkJsonFromManifestTaskTest.kt`** -> AI Confidence: **99.48%**
23. **`packages/flutter_tools/gradle/src/test/kotlin/tasks/FlutterTaskHelperTest.kt`** -> AI Confidence: **99.48%**
24. **`engine/src/flutter/impeller/playground/backend/metal/playground_impl_mtl.mm`** -> AI Confidence: **99.48%**
25. **`engine/src/flutter/impeller/renderer/backend/metal/allocator_mtl.mm`** -> AI Confidence: **99.48%**
26. **`engine/src/flutter/impeller/renderer/backend/metal/allocator_mtl_unittests.mm`** -> AI Confidence: **99.48%**
27. **`engine/src/flutter/impeller/renderer/backend/metal/blit_pass_mtl.mm`** -> AI Confidence: **99.48%**
28. **`engine/src/flutter/impeller/renderer/backend/metal/command_buffer_mtl.mm`** -> AI Confidence: **99.48%**
29. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pass_mtl.mm`** -> AI Confidence: **99.48%**
30. **`engine/src/flutter/impeller/renderer/backend/metal/context_mtl.h`** -> AI Confidence: **99.48%**
31. **`engine/src/flutter/impeller/renderer/backend/metal/context_mtl.mm`** -> AI Confidence: **99.48%**
32. **`engine/src/flutter/impeller/renderer/backend/metal/formats_mtl.h`** -> AI Confidence: **99.48%**
33. **`engine/src/flutter/impeller/renderer/backend/metal/pipeline_library_mtl.mm`** -> AI Confidence: **99.48%**
34. **`engine/src/flutter/impeller/renderer/backend/metal/render_pass_mtl.mm`** -> AI Confidence: **99.48%**
35. **`engine/src/flutter/impeller/renderer/backend/metal/surface_mtl.mm`** -> AI Confidence: **99.48%**
36. **`engine/src/flutter/impeller/renderer/backend/metal/texture_mtl.mm`** -> AI Confidence: **99.48%**
37. **`engine/src/flutter/impeller/toolkit/interop/backend/metal/context_mtl.mm`** -> AI Confidence: **99.48%**
38. **`engine/src/flutter/impeller/toolkit/interop/example_mtl.m`** -> AI Confidence: **99.48%**
39. **`engine/src/flutter/shell/gpu/gpu_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
40. **`engine/src/flutter/shell/gpu/gpu_surface_metal_impeller_unittests.mm`** -> AI Confidence: **99.48%**
41. **`engine/src/flutter/shell/gpu/gpu_surface_metal_skia.mm`** -> AI Confidence: **99.48%**
42. **`engine/src/flutter/shell/gpu/gpu_surface_noop.mm`** -> AI Confidence: **99.48%**
43. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinContextMetalSkia.mm`** -> AI Confidence: **99.48%**
44. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinExternalTextureMetal.mm`** -> AI Confidence: **99.48%**
45. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterAppDelegate.mm`** -> AI Confidence: **99.48%**
46. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterDartProject.mm`** -> AI Confidence: **99.48%**
47. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterEmbedderKeyResponder.mm`** -> AI Confidence: **99.48%**
48. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterEngine.mm`** -> AI Confidence: **99.48%**
49. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterMetalLayer.mm`** -> AI Confidence: **99.48%**
50. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformPlugin.mm`** -> AI Confidence: **99.48%**
51. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsController.mm`** -> AI Confidence: **99.48%**
52. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsTest.mm`** -> AI Confidence: **99.48%**
53. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPluginAppLifeCycleDelegate.mm`** -> AI Confidence: **99.48%**
54. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSceneLifeCycle.mm`** -> AI Confidence: **99.48%**
55. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPlugin.mm`** -> AI Confidence: **99.48%**
56. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm`** -> AI Confidence: **99.48%**
57. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterViewController.mm`** -> AI Confidence: **99.48%**
58. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/accessibility_bridge.mm`** -> AI Confidence: **99.48%**
59. **`engine/src/flutter/shell/platform/darwin/ios/ios_context.mm`** -> AI Confidence: **99.48%**
60. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
61. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface_noop.mm`** -> AI Confidence: **99.48%**
62. **`engine/src/flutter/shell/platform/darwin/ios/platform_view_ios.mm`** -> AI Confidence: **99.48%**
63. **`engine/src/flutter/shell/platform/darwin/ios/rendering_api_selection.mm`** -> AI Confidence: **99.48%**
64. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEmbedderExternalTextureTest.mm`** -> AI Confidence: **99.48%**
65. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEmbedderKeyResponder.mm`** -> AI Confidence: **99.48%**
66. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngine.mm`** -> AI Confidence: **99.48%**
67. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardManager.mm`** -> AI Confidence: **99.48%**
68. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformNodeDelegateMac.mm`** -> AI Confidence: **99.48%**
69. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformNodeDelegateMacTest.mm`** -> AI Confidence: **99.48%**
70. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputPlugin.mm`** -> AI Confidence: **99.48%**
71. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputSemanticsObject.mm`** -> AI Confidence: **99.48%**
72. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputSemanticsObjectTest.mm`** -> AI Confidence: **99.48%**
73. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterVSyncWaiter.mm`** -> AI Confidence: **99.48%**
74. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterWindowController.mm`** -> AI Confidence: **99.48%**
75. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterWindowControllerTest.mm`** -> AI Confidence: **99.48%**
76. **`engine/src/flutter/shell/platform/embedder/embedder_external_texture_metal.mm`** -> AI Confidence: **99.48%**
77. **`engine/src/flutter/shell/platform/embedder/embedder_surface_metal_impeller.mm`** -> AI Confidence: **99.48%**
78. **`engine/src/flutter/shell/platform/embedder/tests/embedder_metal_unittests.mm`** -> AI Confidence: **99.48%**
79. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_backingstore_producer_metal.mm`** -> AI Confidence: **99.48%**
80. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_metal.mm`** -> AI Confidence: **99.48%**
81. **`engine/src/flutter/shell/testing/tester_context_mtl_factory.mm`** -> AI Confidence: **99.48%**
82. **`engine/src/flutter/testing/test_metal_context.mm`** -> AI Confidence: **99.48%**
83. **`engine/src/flutter/testing/test_metal_surface_impl.mm`** -> AI Confidence: **99.48%**
84. **`engine/src/flutter/txt/src/txt/platform_mac.mm`** -> AI Confidence: **99.48%**
85. **`engine/src/flutter/display_list/effects/dl_color_source_unittests.cc`** -> AI Confidence: **99.48%**
86. **`engine/src/flutter/fml/thread_unittests.cc`** -> AI Confidence: **99.48%**
87. **`engine/src/flutter/lib/ui/painting/paint.cc`** -> AI Confidence: **99.48%**
88. **`engine/src/flutter/shell/common/skia_event_tracer_impl.cc`** -> AI Confidence: **99.48%**
89. **`dev/bots/custom_rules/protect_public_state_subtypes.dart`** -> AI Confidence: **99.48%**
90. **`dev/devicelab/bin/run.dart`** -> AI Confidence: **99.48%**
91. **`dev/tools/localization/bin/gen_localizations.dart`** -> AI Confidence: **99.48%**
92. **`engine/src/flutter/testing/dart/gpu_test.dart`** -> AI Confidence: **99.48%**
93. **`packages/flutter/lib/src/cupertino/text_form_field_row.dart`** -> AI Confidence: **99.48%**
94. **`packages/flutter/lib/src/material/checkbox_list_tile.dart`** -> AI Confidence: **99.48%**
95. **`packages/flutter/lib/src/material/color_scheme.dart`** -> AI Confidence: **99.48%**
96. **`packages/flutter/lib/src/material/switch_list_tile.dart`** -> AI Confidence: **99.48%**
97. **`packages/flutter/lib/src/material/bottom_navigation_bar.dart`** -> AI Confidence: **99.44%**
98. **`packages/flutter/lib/src/material/data_table.dart`** -> AI Confidence: **99.44%**
99. **`packages/flutter/lib/src/material/selectable_text.dart`** -> AI Confidence: **99.44%**
100. **`packages/flutter/lib/src/services/raw_keyboard.dart`** -> AI Confidence: **99.44%**
101. **`engine/src/flutter/lib/web_ui/lib/src/engine/platform_dispatcher.dart`** -> AI Confidence: **99.43%**
102. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_stub/renderer.dart`** -> AI Confidence: **99.43%**
103. **`engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart`** -> AI Confidence: **99.43%**
104. **`packages/flutter/lib/src/material/list_tile_theme.dart`** -> AI Confidence: **99.43%**
105. **`packages/flutter/lib/src/material/text_form_field.dart`** -> AI Confidence: **99.43%**
106. **`packages/flutter/lib/src/material/time_picker_theme.dart`** -> AI Confidence: **99.43%**
107. **`packages/flutter/lib/src/painting/text_style.dart`** -> AI Confidence: **99.43%**
108. **`packages/flutter/lib/src/widgets/icon.dart`** -> AI Confidence: **99.43%**
109. **`packages/flutter/lib/src/material/button_style.dart`** -> AI Confidence: **99.42%**
110. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterAppDelegate.mm`** -> AI Confidence: **99.39%**
111. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterDisplayLink.mm`** -> AI Confidence: **99.39%**
112. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewController.mm`** -> AI Confidence: **99.39%**
113. **`engine/src/flutter/display_list/dl_builder.cc`** -> AI Confidence: **99.39%**
114. **`engine/src/flutter/examples/vulkan_glfw/src/main.cc`** -> AI Confidence: **99.39%**
115. **`engine/src/flutter/fml/logging.cc`** -> AI Confidence: **99.39%**
116. **`engine/src/flutter/shell/common/switches.cc`** -> AI Confidence: **99.39%**
117. **`engine/src/flutter/shell/platform/linux/fl_text_input_handler_test.cc`** -> AI Confidence: **99.39%**
118. **`engine/src/flutter/tools/licenses_cpp/src/license_file_compare.cc`** -> AI Confidence: **99.39%**
119. **`engine/src/flutter/lib/web_ui/lib/src/engine/renderer.dart`** -> AI Confidence: **99.39%**
120. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/paragraph.dart`** -> AI Confidence: **99.39%**
121. **`engine/src/flutter/lib/web_ui/lib/src/engine/text_editing/text_editing.dart`** -> AI Confidence: **99.39%**
122. **`engine/src/flutter/lib/web_ui/test/engine/raw_keyboard_test.dart`** -> AI Confidence: **99.39%**
123. **`packages/flutter/lib/src/cupertino/button.dart`** -> AI Confidence: **99.39%**
124. **`packages/flutter/lib/src/cupertino/date_picker.dart`** -> AI Confidence: **99.39%**
125. **`packages/flutter/lib/src/cupertino/nav_bar.dart`** -> AI Confidence: **99.39%**
126. **`packages/flutter/lib/src/cupertino/search_field.dart`** -> AI Confidence: **99.39%**
127. **`packages/flutter/lib/src/cupertino/switch.dart`** -> AI Confidence: **99.39%**
128. **`packages/flutter/lib/src/material/app_bar.dart`** -> AI Confidence: **99.39%**
129. **`packages/flutter/lib/src/material/calendar_date_picker.dart`** -> AI Confidence: **99.39%**
130. **`packages/flutter/lib/src/material/choice_chip.dart`** -> AI Confidence: **99.39%**
131. **`packages/flutter/lib/src/material/dialog.dart`** -> AI Confidence: **99.39%**
132. **`packages/flutter/lib/src/material/expansion_tile.dart`** -> AI Confidence: **99.39%**
133. **`packages/flutter/lib/src/material/input_date_picker_form_field.dart`** -> AI Confidence: **99.39%**
134. **`packages/flutter/lib/src/material/input_decorator.dart`** -> AI Confidence: **99.39%**
135. **`packages/flutter/lib/src/material/radio_list_tile.dart`** -> AI Confidence: **99.39%**
136. **`packages/flutter/lib/src/material/refresh_indicator.dart`** -> AI Confidence: **99.39%**
137. **`packages/flutter/lib/src/material/tooltip.dart`** -> AI Confidence: **99.39%**
138. **`packages/flutter/lib/src/semantics/semantics.dart`** -> AI Confidence: **99.39%**
139. **`packages/flutter/lib/src/widgets/media_query.dart`** -> AI Confidence: **99.39%**
140. **`packages/flutter/lib/src/widgets/text.dart`** -> AI Confidence: **99.39%**
141. **`packages/flutter_tools/lib/src/android/deferred_components_gen_snapshot_validator.dart`** -> AI Confidence: **99.39%**
142. **`packages/flutter_tools/lib/src/base/analyze_size.dart`** -> AI Confidence: **99.39%**
143. **`packages/flutter_tools/lib/src/commands/create.dart`** -> AI Confidence: **99.39%**
144. **`packages/flutter_tools/lib/src/debug_adapters/flutter_adapter.dart`** -> AI Confidence: **99.39%**
145. **`packages/flutter_tools/lib/src/ios/core_devices.dart`** -> AI Confidence: **99.39%**
146. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/common/StandardMessageCodec.java`** -> AI Confidence: **99.39%**
147. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paragraph.dart`** -> AI Confidence: **99.35%**
148. **`packages/flutter/lib/src/material/date_picker.dart`** -> AI Confidence: **99.35%**
149. **`packages/flutter/lib/src/material/filter_chip.dart`** -> AI Confidence: **99.35%**
150. **`packages/flutter/lib/src/material/input_chip.dart`** -> AI Confidence: **99.35%**
151. **`packages/flutter/lib/src/material/switch.dart`** -> AI Confidence: **99.35%**
152. **`packages/flutter/lib/src/widgets/form.dart`** -> AI Confidence: **99.35%**
153. **`dev/benchmarks/platform_channels_benchmarks/android/app/src/main/kotlin/com/example/platform_channels_benchmarks/MainActivity.kt`** -> AI Confidence: **99.34%**
154. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterAppPluginLoaderPlugin.kt`** -> AI Confidence: **99.34%**
155. **`packages/flutter_tools/gradle/src/main/kotlin/VersionFetcher.kt`** -> AI Confidence: **99.34%**
156. **`packages/flutter_tools/gradle/src/main/kotlin/tasks/FlutterTaskHelper.kt`** -> AI Confidence: **99.34%**
157. **`packages/flutter_tools/gradle/src/test/kotlin/DeeplinkTest.kt`** -> AI Confidence: **99.34%**
158. **`packages/flutter_tools/templates/plugin/android-kotlin.tmpl/src/main/kotlin/androidIdentifier/pluginClass.kt.tmpl`** -> AI Confidence: **99.34%**
159. **`engine/src/flutter/display_list/testing/dl_test_surface_metal.mm`** -> AI Confidence: **99.34%**
160. **`engine/src/flutter/impeller/golden_tests/metal_screenshotter.mm`** -> AI Confidence: **99.34%**
161. **`engine/src/flutter/impeller/renderer/backend/metal/device_buffer_mtl.mm`** -> AI Confidence: **99.34%**
162. **`engine/src/flutter/impeller/renderer/backend/metal/gpu_tracer_mtl.mm`** -> AI Confidence: **99.34%**
163. **`engine/src/flutter/impeller/renderer/backend/metal/surface_mtl.h`** -> AI Confidence: **99.34%**
164. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterFakeKeyEvents.mm`** -> AI Confidence: **99.34%**
165. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViews.mm`** -> AI Confidence: **99.34%**
166. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterView.mm`** -> AI Confidence: **99.34%**
167. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/profiler_metrics_ios.h`** -> AI Confidence: **99.34%**
168. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/profiler_metrics_ios.mm`** -> AI Confidence: **99.34%**
169. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/vsync_waiter_ios.mm`** -> AI Confidence: **99.34%**
170. **`engine/src/flutter/shell/platform/darwin/ios/ios_context_metal_impeller.mm`** -> AI Confidence: **99.34%**
171. **`engine/src/flutter/shell/platform/darwin/ios/ios_surface.mm`** -> AI Confidence: **99.34%**
172. **`engine/src/flutter/shell/platform/darwin/ios/platform_message_handler_ios.mm`** -> AI Confidence: **99.34%**
173. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/AccessibilityBridgeMac.mm`** -> AI Confidence: **99.34%**
174. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterChannelKeyResponder.mm`** -> AI Confidence: **99.34%**
175. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterDartProject.mm`** -> AI Confidence: **99.34%**
176. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTestUtils.h`** -> AI Confidence: **99.34%**
177. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterMutatorView.mm`** -> AI Confidence: **99.34%**
178. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterRenderer.mm`** -> AI Confidence: **99.34%**
179. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterView.mm`** -> AI Confidence: **99.34%**
180. **`engine/src/flutter/shell/platform/embedder/embedder_surface_metal_skia.mm`** -> AI Confidence: **99.34%**
181. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_context_metal.mm`** -> AI Confidence: **99.34%**
182. **`engine/src/flutter/display_list/dl_vertices_unittests.cc`** -> AI Confidence: **99.34%**
183. **`engine/src/flutter/impeller/compiler/code_gen_template.h`** -> AI Confidence: **99.34%**
184. **`dev/tools/bin/generate_gradle_lockfiles.dart`** -> AI Confidence: **99.34%**
185. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/text.dart`** -> AI Confidence: **99.34%**
186. **`engine/src/flutter/web_sdk/test/api_conform_test.dart`** -> AI Confidence: **99.34%**
187. **`packages/flutter/lib/src/gestures/events.dart`** -> AI Confidence: **99.34%**
188. **`packages/flutter/lib/src/material/app_bar_theme.dart`** -> AI Confidence: **99.34%**
189. **`packages/flutter/lib/src/material/chip.dart`** -> AI Confidence: **99.34%**
190. **`packages/flutter/lib/src/material/date_picker_theme.dart`** -> AI Confidence: **99.34%**
191. **`packages/flutter/lib/src/material/dropdown.dart`** -> AI Confidence: **99.34%**
192. **`packages/flutter/lib/src/material/scaffold.dart`** -> AI Confidence: **99.34%**
193. **`packages/flutter/lib/src/material/tabs.dart`** -> AI Confidence: **99.34%**
194. **`packages/flutter/lib/src/rendering/custom_paint.dart`** -> AI Confidence: **99.34%**
195. **`packages/flutter/lib/src/rendering/paragraph.dart`** -> AI Confidence: **99.34%**
196. **`packages/flutter/lib/src/rendering/sliver.dart`** -> AI Confidence: **99.34%**
197. **`packages/flutter_tools/lib/src/commands/generate_localizations.dart`** -> AI Confidence: **99.34%**
198. **`packages/flutter_tools/lib/src/migrations/lldb_init_migration.dart`** -> AI Confidence: **99.34%**
199. **`dev/integration_tests/hook_user_defines/src/hook_user_defines.h`** -> AI Confidence: **99.34%**
200. **`dev/integration_tests/link_hook/src/link_hook.h`** -> AI Confidence: **99.34%**
201. **`packages/flutter/lib/src/painting/text_span.dart`** -> AI Confidence: **99.33%**
202. **`packages/flutter_tools/lib/src/localizations/gen_l10n_types.dart`** -> AI Confidence: **99.33%**
203. **`dev/integration_tests/android_engine_test/android/app/src/main/kotlin/com/example/native_driver_test/extensions/NativeSelector.kt`** -> AI Confidence: **99.32%**
204. **`dev/benchmarks/macrobenchmarks/ios/Runner/main.m`** -> AI Confidence: **99.32%**
205. **`dev/benchmarks/platform_views_layout_hybrid_composition/ios/Runner/main.m`** -> AI Confidence: **99.32%**
206. **`dev/benchmarks/test_apps/stocks/ios/Runner/main.m`** -> AI Confidence: **99.32%**
207. **`dev/integration_tests/channels/ios/Runner/main.m`** -> AI Confidence: **99.32%**
208. **`dev/integration_tests/external_textures/ios/Runner/main.m`** -> AI Confidence: **99.32%**
209. **`dev/integration_tests/flavors/ios/Runner/main.m`** -> AI Confidence: **99.32%**
210. **`dev/integration_tests/flutter_gallery/ios/Runner/main.m`** -> AI Confidence: **99.32%**
211. **`dev/integration_tests/ios_platform_view_tests/ios/Runner/main.m`** -> AI Confidence: **99.32%**
212. **`dev/integration_tests/platform_interaction/ios/Runner/main.m`** -> AI Confidence: **99.32%**
213. **`dev/integration_tests/spell_check/ios/Runner/main.m`** -> AI Confidence: **99.32%**
214. **`dev/integration_tests/ui/ios/Runner/main.m`** -> AI Confidence: **99.32%**
215. **`engine/src/flutter/fml/platform/darwin/paths_darwin.mm`** -> AI Confidence: **99.32%**
216. **`engine/src/flutter/impeller/renderer/backend/metal/sampler_library_mtl.mm`** -> AI Confidence: **99.32%**
217. **`engine/src/flutter/impeller/renderer/backend/metal/vertex_descriptor_mtl.mm`** -> AI Confidence: **99.32%**
218. **`engine/src/flutter/impeller/toolkit/interop/backend/metal/surface_mtl.mm`** -> AI Confidence: **99.32%**
219. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterNSBundleUtils.mm`** -> AI Confidence: **99.32%**
220. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSemanticsScrollView.mm`** -> AI Confidence: **99.32%**
221. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSharedApplication.mm`** -> AI Confidence: **99.32%**
222. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/SemanticsObject.mm`** -> AI Confidence: **99.32%**
223. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/overlay_layer_pool.mm`** -> AI Confidence: **99.32%**
224. **`engine/src/flutter/shell/platform/darwin/ios/ios_context_noop.mm`** -> AI Confidence: **99.32%**
225. **`engine/src/flutter/shell/platform/darwin/ios/ios_external_view_embedder.mm`** -> AI Confidence: **99.32%**
226. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterCompositor.mm`** -> AI Confidence: **99.32%**
227. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterMouseCursorPlugin.mm`** -> AI Confidence: **99.32%**
228. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/KeyCodeMapTest.mm`** -> AI Confidence: **99.32%**
229. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/Scenarios/main.m`** -> AI Confidence: **99.32%**
230. **`engine/src/flutter/testing/test_metal_surface_unittests.mm`** -> AI Confidence: **99.32%**
231. **`examples/flutter_view/ios/Runner/main.m`** -> AI Confidence: **99.32%**
232. **`examples/hello_world/ios/Runner/main.m`** -> AI Confidence: **99.32%**
233. **`examples/image_list/ios/Runner/main.m`** -> AI Confidence: **99.32%**
234. **`examples/layers/ios/Runner/main.m`** -> AI Confidence: **99.32%**
235. **`examples/platform_channel/ios/Runner/AppDelegate.m`** -> AI Confidence: **99.32%**
236. **`examples/platform_channel/ios/Runner/main.m`** -> AI Confidence: **99.32%**
237. **`examples/platform_view/ios/Runner/main.m`** -> AI Confidence: **99.32%**
238. **`packages/flutter_tools/templates/module/ios/host_app_ephemeral/Runner.tmpl/main.m`** -> AI Confidence: **99.32%**
239. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_standard_method_codec.h`** -> AI Confidence: **99.32%**
240. **`engine/src/flutter/testing/test_gl_utils.cc`** -> AI Confidence: **99.32%**
241. **`engine/src/flutter/shell/testing/vm_service/service_client.dart`** -> AI Confidence: **99.32%**
242. **`packages/flutter/lib/src/cupertino/icon_theme_data.dart`** -> AI Confidence: **99.32%**
243. **`packages/flutter/lib/src/material/button_theme.dart`** -> AI Confidence: **99.32%**
244. **`packages/flutter/lib/src/material/ink_well.dart`** -> AI Confidence: **99.32%**
245. **`packages/flutter/lib/src/material/material_button.dart`** -> AI Confidence: **99.32%**
246. **`packages/flutter/lib/src/rendering/debug.dart`** -> AI Confidence: **99.32%**
247. **`packages/flutter/lib/src/rendering/object.dart`** -> AI Confidence: **99.32%**
248. **`packages/flutter_test/lib/src/event_simulation.dart`** -> AI Confidence: **99.32%**
249. **`packages/flutter_tools/lib/src/build_info.dart`** -> AI Confidence: **99.32%**
250. **`packages/flutter_tools/lib/src/flutter_manifest.dart`** -> AI Confidence: **99.32%**
251. **`packages/flutter_tools/tool/daemon_client.dart`** -> AI Confidence: **99.32%**
252. **`dev/integration_tests/ios_host_app/Host/MainViewController.m`** -> AI Confidence: **99.31%**
253. **`engine/src/flutter/shell/platform/darwin/graphics/FlutterDarwinContextMetalImpeller.mm`** -> AI Confidence: **99.31%**
254. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterAppDelegateTest.mm`** -> AI Confidence: **99.31%**
255. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterDartVMServicePublisher.mm`** -> AI Confidence: **99.31%**
256. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterHeadlessDartRunner.mm`** -> AI Confidence: **99.31%**
257. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/accessibility_bridge_test.mm`** -> AI Confidence: **99.31%**
258. **`engine/src/flutter/shell/platform/darwin/ios/platform_view_ios.h`** -> AI Confidence: **99.31%**
259. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterAppLifecycleDelegate.mm`** -> AI Confidence: **99.31%**
260. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTest.mm`** -> AI Confidence: **99.31%**
261. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardManagerTest.mm`** -> AI Confidence: **99.31%**
262. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterTextInputPluginTest.mm`** -> AI Confidence: **99.31%**
263. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewControllerTest.mm`** -> AI Confidence: **99.31%**
264. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewEngineProviderTest.mm`** -> AI Confidence: **99.31%**
265. **`engine/src/flutter/common/graphics/persistent_cache.cc`** -> AI Confidence: **99.31%**
266. **`engine/src/flutter/display_list/benchmarking/dl_benchmarks.cc`** -> AI Confidence: **99.31%**
267. **`engine/src/flutter/display_list/skia/dl_sk_conversions.cc`** -> AI Confidence: **99.31%**
268. **`engine/src/flutter/examples/glfw_drm/FlutterEmbedderGLFW.cc`** -> AI Confidence: **99.31%**
269. **`engine/src/flutter/flow/layers/display_list_layer.cc`** -> AI Confidence: **99.31%**
270. **`engine/src/flutter/flow/layers/display_list_raster_cache_item.cc`** -> AI Confidence: **99.31%**
271. **`engine/src/flutter/flow/layers/layer_tree.cc`** -> AI Confidence: **99.31%**
272. **`engine/src/flutter/flow/raster_cache.cc`** -> AI Confidence: **99.31%**
273. **`engine/src/flutter/flow/skia_gpu_object.h`** -> AI Confidence: **99.31%**
274. **`engine/src/flutter/flow/stopwatch_dl.cc`** -> AI Confidence: **99.31%**
275. **`engine/src/flutter/fml/cpu_affinity.cc`** -> AI Confidence: **99.31%**
276. **`engine/src/flutter/fml/message_loop_task_queues_benchmark.cc`** -> AI Confidence: **99.31%**
277. **`engine/src/flutter/fml/platform/fuchsia/message_loop_fuchsia.cc`** -> AI Confidence: **99.31%**
278. **`engine/src/flutter/fml/platform/posix/file_posix.cc`** -> AI Confidence: **99.31%**
279. **`engine/src/flutter/fml/platform/posix/mapping_posix.cc`** -> AI Confidence: **99.31%**
280. **`engine/src/flutter/fml/platform/win/mapping_win.cc`** -> AI Confidence: **99.31%**
281. **`engine/src/flutter/fml/synchronization/waitable_event_unittest.cc`** -> AI Confidence: **99.31%**
282. **`engine/src/flutter/impeller/compiler/compiler.cc`** -> AI Confidence: **99.31%**
283. **`engine/src/flutter/impeller/compiler/impellerc_main.cc`** -> AI Confidence: **99.31%**
284. **`engine/src/flutter/impeller/compiler/reflector.cc`** -> AI Confidence: **99.31%**
285. **`engine/src/flutter/impeller/compiler/reflector.h`** -> AI Confidence: **99.31%**
286. **`engine/src/flutter/impeller/compiler/runtime_stage_data.cc`** -> AI Confidence: **99.31%**
287. **`engine/src/flutter/impeller/compiler/switches.cc`** -> AI Confidence: **99.31%**
288. **`engine/src/flutter/impeller/core/host_buffer.cc`** -> AI Confidence: **99.31%**
289. **`engine/src/flutter/impeller/display_list/canvas.cc`** -> AI Confidence: **99.31%**
290. **`engine/src/flutter/impeller/display_list/dl_dispatcher.cc`** -> AI Confidence: **99.31%**
291. **`engine/src/flutter/impeller/entity/contents/clip_contents.cc`** -> AI Confidence: **99.31%**
292. **`engine/src/flutter/impeller/entity/contents/filters/blend_filter_contents.cc`** -> AI Confidence: **99.31%**
293. **`engine/src/flutter/impeller/entity/contents/filters/gaussian_blur_filter_contents.cc`** -> AI Confidence: **99.31%**
294. **`engine/src/flutter/impeller/entity/contents/filters/gaussian_blur_filter_contents_unittests.cc`** -> AI Confidence: **99.31%**
295. **`engine/src/flutter/impeller/entity/contents/gradient_generator.cc`** -> AI Confidence: **99.31%**
296. **`engine/src/flutter/impeller/entity/contents/runtime_effect_contents.cc`** -> AI Confidence: **99.31%**
297. **`engine/src/flutter/impeller/entity/contents/text_contents.cc`** -> AI Confidence: **99.31%**
298. **`engine/src/flutter/impeller/entity/entity.cc`** -> AI Confidence: **99.31%**
299. **`engine/src/flutter/impeller/entity/inline_pass_context.cc`** -> AI Confidence: **99.31%**
300. **`engine/src/flutter/impeller/geometry/geometry_asserts.h`** -> AI Confidence: **99.31%**
301. **`engine/src/flutter/impeller/playground/image/backends/skia/compressed_image_skia.cc`** -> AI Confidence: **99.31%**
302. **`engine/src/flutter/impeller/playground/imgui/imgui_impl_impeller.cc`** -> AI Confidence: **99.31%**
303. **`engine/src/flutter/impeller/renderer/backend/gles/blit_command_gles.cc`** -> AI Confidence: **99.31%**
304. **`engine/src/flutter/impeller/renderer/backend/gles/buffer_bindings_gles.cc`** -> AI Confidence: **99.31%**
305. **`engine/src/flutter/impeller/renderer/backend/gles/proc_table_gles.cc`** -> AI Confidence: **99.31%**
306. **`engine/src/flutter/impeller/renderer/backend/gles/render_pass_gles.cc`** -> AI Confidence: **99.31%**
307. **`engine/src/flutter/impeller/renderer/backend/gles/sampler_gles.cc`** -> AI Confidence: **99.31%**
308. **`engine/src/flutter/impeller/renderer/backend/gles/texture_gles.cc`** -> AI Confidence: **99.31%**
309. **`engine/src/flutter/impeller/renderer/backend/vulkan/driver_info_vk.cc`** -> AI Confidence: **99.31%**
310. **`engine/src/flutter/impeller/renderer/backend/vulkan/formats_vk.h`** -> AI Confidence: **99.31%**
311. **`engine/src/flutter/impeller/renderer/backend/vulkan/render_pass_vk.cc`** -> AI Confidence: **99.31%**
312. **`engine/src/flutter/impeller/renderer/backend/vulkan/test/mock_vulkan.cc`** -> AI Confidence: **99.31%**
313. **`engine/src/flutter/impeller/renderer/render_target.cc`** -> AI Confidence: **99.31%**
314. **`engine/src/flutter/impeller/runtime_stage/runtime_stage.cc`** -> AI Confidence: **99.31%**
315. **`engine/src/flutter/impeller/typographer/backends/skia/text_frame_skia.cc`** -> AI Confidence: **99.31%**
316. **`engine/src/flutter/impeller/typographer/backends/skia/typographer_context_skia.cc`** -> AI Confidence: **99.31%**
317. **`engine/src/flutter/impeller/typographer/lazy_glyph_atlas.cc`** -> AI Confidence: **99.31%**
318. **`engine/src/flutter/lib/gpu/shader_library.cc`** -> AI Confidence: **99.31%**
319. **`engine/src/flutter/lib/ui/painting/canvas.cc`** -> AI Confidence: **99.31%**
320. **`engine/src/flutter/lib/ui/painting/fragment_program.cc`** -> AI Confidence: **99.31%**
321. **`engine/src/flutter/lib/ui/painting/image.cc`** -> AI Confidence: **99.31%**
322. **`engine/src/flutter/lib/ui/painting/image_decoder_impeller.cc`** -> AI Confidence: **99.31%**
323. **`engine/src/flutter/lib/ui/painting/image_decoder_skia.cc`** -> AI Confidence: **99.31%**
324. **`engine/src/flutter/lib/ui/painting/image_descriptor.cc`** -> AI Confidence: **99.31%**
325. **`engine/src/flutter/lib/ui/painting/image_generator_apng.cc`** -> AI Confidence: **99.31%**
326. **`engine/src/flutter/lib/ui/painting/multi_frame_codec.cc`** -> AI Confidence: **99.31%**
327. **`engine/src/flutter/lib/ui/semantics/semantics_update_builder.cc`** -> AI Confidence: **99.31%**
328. **`engine/src/flutter/lib/ui/text/font_collection.cc`** -> AI Confidence: **99.31%**
329. **`engine/src/flutter/lib/ui/text/paragraph_builder.cc`** -> AI Confidence: **99.31%**
330. **`engine/src/flutter/runtime/dart_vm_initializer.cc`** -> AI Confidence: **99.31%**
331. **`engine/src/flutter/shell/common/rasterizer.cc`** -> AI Confidence: **99.31%**
332. **`engine/src/flutter/shell/common/shell.cc`** -> AI Confidence: **99.31%**
333. **`engine/src/flutter/shell/common/snapshot_controller_impeller.cc`** -> AI Confidence: **99.31%**
334. **`engine/src/flutter/shell/platform/android/android_context_gl_impeller.cc`** -> AI Confidence: **99.31%**
335. **`engine/src/flutter/shell/platform/android/android_context_vk_impeller.cc`** -> AI Confidence: **99.31%**
336. **`engine/src/flutter/shell/platform/android/android_shell_holder.cc`** -> AI Confidence: **99.31%**
337. **`engine/src/flutter/shell/platform/android/android_surface_software.cc`** -> AI Confidence: **99.31%**
338. **`engine/src/flutter/shell/platform/android/external_view_embedder/external_view_embedder_2.cc`** -> AI Confidence: **99.31%**
339. **`engine/src/flutter/shell/platform/android/flutter_main.cc`** -> AI Confidence: **99.31%**
340. **`engine/src/flutter/shell/platform/android/platform_view_android.cc`** -> AI Confidence: **99.31%**
341. **`engine/src/flutter/shell/platform/common/client_wrapper/include/flutter/event_channel.h`** -> AI Confidence: **99.31%**
342. **`engine/src/flutter/shell/platform/common/client_wrapper/standard_codec.cc`** -> AI Confidence: **99.31%**
343. **`engine/src/flutter/shell/platform/embedder/embedder.cc`** -> AI Confidence: **99.31%**
344. **`engine/src/flutter/shell/platform/embedder/embedder_external_texture_gl.cc`** -> AI Confidence: **99.31%**
345. **`engine/src/flutter/shell/platform/embedder/embedder_surface_software.cc`** -> AI Confidence: **99.31%**
346. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_gl.cc`** -> AI Confidence: **99.31%**
347. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_compositor_vulkan.cc`** -> AI Confidence: **99.31%**
348. **`engine/src/flutter/shell/platform/embedder/tests/embedder_unittests_util.cc`** -> AI Confidence: **99.31%**
349. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_component_controller.cc`** -> AI Confidence: **99.31%**
350. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_runner.cc`** -> AI Confidence: **99.31%**
351. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_test_component_controller.cc`** -> AI Confidence: **99.31%**
352. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/main.cc`** -> AI Confidence: **99.31%**
353. **`engine/src/flutter/shell/platform/fuchsia/dart_runner/service_isolate.cc`** -> AI Confidence: **99.31%**
354. **`engine/src/flutter/shell/platform/fuchsia/flutter/accessibility_bridge.cc`** -> AI Confidence: **99.31%**
355. **`engine/src/flutter/shell/platform/fuchsia/flutter/component_v2.cc`** -> AI Confidence: **99.31%**
356. **`engine/src/flutter/shell/platform/fuchsia/flutter/engine.cc`** -> AI Confidence: **99.31%**
357. **`engine/src/flutter/shell/platform/fuchsia/flutter/external_view_embedder.cc`** -> AI Confidence: **99.31%**
358. **`engine/src/flutter/shell/platform/fuchsia/flutter/platform_view.cc`** -> AI Confidence: **99.31%**
359. **`engine/src/flutter/shell/platform/fuchsia/flutter/pointer_delegate.cc`** -> AI Confidence: **99.31%**
360. **`engine/src/flutter/shell/platform/fuchsia/flutter/runner.cc`** -> AI Confidence: **99.31%**
361. **`engine/src/flutter/shell/platform/fuchsia/flutter/tests/integration/utils/screenshot.cc`** -> AI Confidence: **99.31%**
362. **`engine/src/flutter/shell/platform/fuchsia/flutter/text_delegate.cc`** -> AI Confidence: **99.31%**
363. **`engine/src/flutter/shell/platform/fuchsia/flutter/vulkan_surface_producer.cc`** -> AI Confidence: **99.31%**
364. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/handle_exception.cc`** -> AI Confidence: **99.31%**
365. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/mapped_resource.cc`** -> AI Confidence: **99.31%**
366. **`engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/vmo.cc`** -> AI Confidence: **99.31%**
367. **`engine/src/flutter/shell/platform/linux/fl_accessibility_handler_test.cc`** -> AI Confidence: **99.31%**
368. **`engine/src/flutter/shell/platform/linux/fl_compositor_opengl.cc`** -> AI Confidence: **99.31%**
369. **`engine/src/flutter/shell/platform/linux/fl_engine.cc`** -> AI Confidence: **99.31%**
370. **`engine/src/flutter/shell/platform/linux/fl_keyboard_manager.cc`** -> AI Confidence: **99.31%**
371. **`engine/src/flutter/shell/platform/windows/flutter_window.cc`** -> AI Confidence: **99.31%**
372. **`engine/src/flutter/shell/platform/windows/host_window.cc`** -> AI Confidence: **99.31%**
373. **`engine/src/flutter/shell/platform/windows/platform_handler.cc`** -> AI Confidence: **99.31%**
374. **`engine/src/flutter/shell/platform/windows/text_input_plugin.cc`** -> AI Confidence: **99.31%**
375. **`engine/src/flutter/testing/debugger_detection.cc`** -> AI Confidence: **99.31%**
376. **`engine/src/flutter/testing/display_list_testing.cc`** -> AI Confidence: **99.31%**
377. **`engine/src/flutter/testing/test_vulkan_context.cc`** -> AI Confidence: **99.31%**
378. **`engine/src/flutter/tools/font_subset/main.cc`** -> AI Confidence: **99.31%**
379. **`engine/src/flutter/tools/licenses_cpp/src/license_checker.cc`** -> AI Confidence: **99.31%**
380. **`engine/src/flutter/tools/licenses_cpp/src/license_checker_unittests.cc`** -> AI Confidence: **99.31%**
381. **`engine/src/flutter/tools/licenses_cpp/src/main.cc`** -> AI Confidence: **99.31%**
382. **`engine/src/flutter/txt/benchmarks/skparagraph_benchmarks.cc`** -> AI Confidence: **99.31%**
383. **`engine/src/flutter/txt/src/txt/font_collection.cc`** -> AI Confidence: **99.31%**
384. **`engine/src/flutter/vulkan/vulkan_device.cc`** -> AI Confidence: **99.31%**
385. **`engine/src/flutter/vulkan/vulkan_swapchain.cc`** -> AI Confidence: **99.31%**
386. **`examples/platform_channel/windows/runner/flutter_window.cpp`** -> AI Confidence: **99.31%**
387. **`examples/platform_view/windows/runner/flutter_window.cpp`** -> AI Confidence: **99.31%**
388. **`engine/src/flutter/lib/web_ui/flutter_js/src/loader.js`** -> AI Confidence: **99.31%**
389. **`dev/bots/analyze.dart`** -> AI Confidence: **99.31%**
390. **`dev/bots/analyze_snippet_code.dart`** -> AI Confidence: **99.31%**
391. **`dev/bots/custom_rules/analyze.dart`** -> AI Confidence: **99.31%**
392. **`dev/bots/prepare_package.dart`** -> AI Confidence: **99.31%**
393. **`dev/bots/suite_runners/run_android_engine_tests.dart`** -> AI Confidence: **99.31%**
394. **`dev/bots/unpublish_package.dart`** -> AI Confidence: **99.31%**
395. **`dev/bots/utils.dart`** -> AI Confidence: **99.31%**
396. **`dev/forbidden_from_release_tests/bin/main.dart`** -> AI Confidence: **99.31%**
397. **`dev/snippets/bin/snippets.dart`** -> AI Confidence: **99.31%**
398. **`dev/snippets/lib/src/analysis.dart`** -> AI Confidence: **99.31%**
399. **`dev/snippets/lib/src/snippet_generator.dart`** -> AI Confidence: **99.31%**
400. **`dev/snippets/lib/src/util.dart`** -> AI Confidence: **99.31%**
401. **`dev/tools/create_api_docs.dart`** -> AI Confidence: **99.31%**
402. **`dev/tools/gen_keycodes/lib/keyboard_maps_code_gen.dart`** -> AI Confidence: **99.31%**
403. **`dev/tools/update_icons.dart`** -> AI Confidence: **99.31%**
404. **`engine/src/flutter/lib/web_ui/dev/test_runner.dart`** -> AI Confidence: **99.31%**
405. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/image.dart`** -> AI Confidence: **99.31%**
406. **`engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/renderer.dart`** -> AI Confidence: **99.31%**
407. **`engine/src/flutter/lib/web_ui/lib/src/engine/compositing/composition.dart`** -> AI Confidence: **99.31%**
408. **`engine/src/flutter/lib/web_ui/lib/src/engine/keyboard_binding.dart`** -> AI Confidence: **99.31%**
409. **`engine/src/flutter/lib/web_ui/lib/src/engine/pointer_binding.dart`** -> AI Confidence: **99.31%**
410. **`engine/src/flutter/lib/web_ui/lib/src/engine/raw_keyboard.dart`** -> AI Confidence: **99.31%**
411. **`engine/src/flutter/lib/web_ui/lib/src/engine/semantics/semantics.dart`** -> AI Confidence: **99.31%**
412. **`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/renderer.dart`** -> AI Confidence: **99.31%**
413. **`engine/src/flutter/lib/web_ui/lib/src/engine/window.dart`** -> AI Confidence: **99.31%**
414. **`engine/src/flutter/lib/web_ui/lib/ui_web/src/ui_web/navigation/url_strategy.dart`** -> AI Confidence: **99.31%**
415. **`engine/src/flutter/lib/web_ui/test/common/matchers.dart`** -> AI Confidence: **99.31%**
416. **`engine/src/flutter/lib/web_ui/test/engine/channel_buffers_test.dart`** -> AI Confidence: **99.31%**
417. **`engine/src/flutter/lib/web_ui/test/engine/pointer_binding_test.dart`** -> AI Confidence: **99.31%**
418. **`engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart`** -> AI Confidence: **99.31%**
419. **`engine/src/flutter/lib/web_ui/test/engine/semantics/text_field_test.dart`** -> AI Confidence: **99.31%**
420. **`engine/src/flutter/lib/web_ui/test/engine/text_editing_test.dart`** -> AI Confidence: **99.31%**
421. **`engine/src/flutter/lib/web_ui/test/ui/canvas_golden_test.dart`** -> AI Confidence: **99.31%**
422. **`engine/src/flutter/lib/web_ui/test/ui/fallback_fonts_golden_test.dart`** -> AI Confidence: **99.31%**
423. **`engine/src/flutter/shell/platform/embedder/fixtures/main.dart`** -> AI Confidence: **99.31%**
424. **`engine/src/flutter/testing/dart/vm_service/vmservice_methods_test.dart`** -> AI Confidence: **99.31%**
425. **`engine/src/flutter/testing/ios_scenario_app/bin/run_ios_tests.dart`** -> AI Confidence: **99.31%**
426. **`engine/src/flutter/testing/ios_scenario_app/lib/src/platform_view.dart`** -> AI Confidence: **99.31%**
427. **`engine/src/flutter/testing/skia_gold_client/lib/skia_gold_client.dart`** -> AI Confidence: **99.31%**
428. **`engine/src/flutter/testing/skia_gold_client/test/skia_gold_client_test.dart`** -> AI Confidence: **99.31%**
429. **`engine/src/flutter/tools/clang_tidy/lib/clang_tidy.dart`** -> AI Confidence: **99.31%**
430. **`engine/src/flutter/tools/engine_tool/lib/src/build_plan.dart`** -> AI Confidence: **99.31%**
431. **`engine/src/flutter/tools/engine_tool/lib/src/commands/query_command.dart`** -> AI Confidence: **99.31%**
432. **`engine/src/flutter/tools/engine_tool/test/build_plan_test.dart`** -> AI Confidence: **99.31%**
433. **`engine/src/flutter/tools/gen_web_locale_keymap/lib/github.dart`** -> AI Confidence: **99.31%**
434. **`engine/src/flutter/tools/header_guard_check/lib/header_guard_check.dart`** -> AI Confidence: **99.31%**
435. **`engine/src/flutter/tools/pkg/engine_build_configs/bin/check.dart`** -> AI Confidence: **99.31%**
436. **`engine/src/flutter/tools/pkg/engine_build_configs/bin/run.dart`** -> AI Confidence: **99.31%**
437. **`engine/src/flutter/tools/pkg/engine_build_configs/test/build_config_runner_test.dart`** -> AI Confidence: **99.31%**
438. **`engine/src/flutter/tools/pkg/engine_build_configs/test/ci_yaml_test.dart`** -> AI Confidence: **99.31%**
439. **`packages/flutter/lib/src/animation/animation_controller.dart`** -> AI Confidence: **99.31%**
440. **`packages/flutter/lib/src/cupertino/adaptive_text_selection_toolbar.dart`** -> AI Confidence: **99.31%**
441. **`packages/flutter/lib/src/cupertino/context_menu.dart`** -> AI Confidence: **99.31%**
442. **`packages/flutter/lib/src/cupertino/dialog.dart`** -> AI Confidence: **99.31%**
443. **`packages/flutter/lib/src/cupertino/picker.dart`** -> AI Confidence: **99.31%**
444. **`packages/flutter/lib/src/cupertino/refresh.dart`** -> AI Confidence: **99.31%**
445. **`packages/flutter/lib/src/cupertino/sheet.dart`** -> AI Confidence: **99.31%**
446. **`packages/flutter/lib/src/cupertino/slider.dart`** -> AI Confidence: **99.31%**
447. **`packages/flutter/lib/src/cupertino/sliding_segmented_control.dart`** -> AI Confidence: **99.31%**
448. **`packages/flutter/lib/src/cupertino/text_field.dart`** -> AI Confidence: **99.31%**
449. **`packages/flutter/lib/src/cupertino/text_selection.dart`** -> AI Confidence: **99.31%**
450. **`packages/flutter/lib/src/cupertino/text_selection_toolbar.dart`** -> AI Confidence: **99.31%**
451. **`packages/flutter/lib/src/gestures/long_press.dart`** -> AI Confidence: **99.31%**
452. **`packages/flutter/lib/src/gestures/multitap.dart`** -> AI Confidence: **99.31%**
453. **`packages/flutter/lib/src/gestures/scale.dart`** -> AI Confidence: **99.31%**
454. **`packages/flutter/lib/src/gestures/tap_and_drag.dart`** -> AI Confidence: **99.31%**
455. **`packages/flutter/lib/src/material/about.dart`** -> AI Confidence: **99.31%**
456. **`packages/flutter/lib/src/material/action_chip.dart`** -> AI Confidence: **99.31%**
457. **`packages/flutter/lib/src/material/app.dart`** -> AI Confidence: **99.31%**
458. **`packages/flutter/lib/src/material/bottom_app_bar.dart`** -> AI Confidence: **99.31%**
459. **`packages/flutter/lib/src/material/dropdown_menu.dart`** -> AI Confidence: **99.31%**
460. **`packages/flutter/lib/src/material/expansion_panel.dart`** -> AI Confidence: **99.31%**
461. **`packages/flutter/lib/src/material/mergeable_material.dart`** -> AI Confidence: **99.31%**
462. **`packages/flutter/lib/src/material/popup_menu.dart`** -> AI Confidence: **99.31%**
463. **`packages/flutter/lib/src/material/range_slider.dart`** -> AI Confidence: **99.31%**
464. **`packages/flutter/lib/src/material/reorderable_list.dart`** -> AI Confidence: **99.31%**
465. **`packages/flutter/lib/src/material/search.dart`** -> AI Confidence: **99.31%**
466. **`packages/flutter/lib/src/material/search_anchor.dart`** -> AI Confidence: **99.31%**
467. **`packages/flutter/lib/src/material/segmented_button.dart`** -> AI Confidence: **99.31%**
468. **`packages/flutter/lib/src/material/text_selection.dart`** -> AI Confidence: **99.31%**
469. **`packages/flutter/lib/src/material/theme_data.dart`** -> AI Confidence: **99.31%**
470. **`packages/flutter/lib/src/material/time_picker.dart`** -> AI Confidence: **99.31%**
471. **`packages/flutter/lib/src/material/toggle_buttons.dart`** -> AI Confidence: **99.31%**
472. **`packages/flutter/lib/src/painting/box_decoration.dart`** -> AI Confidence: **99.31%**
473. **`packages/flutter/lib/src/painting/flutter_logo.dart`** -> AI Confidence: **99.31%**
474. **`packages/flutter/lib/src/painting/shape_decoration.dart`** -> AI Confidence: **99.31%**
475. **`packages/flutter/lib/src/painting/stadium_border.dart`** -> AI Confidence: **99.31%**
476. **`packages/flutter/lib/src/painting/star_border.dart`** -> AI Confidence: **99.31%**
477. **`packages/flutter/lib/src/rendering/editable.dart`** -> AI Confidence: **99.31%**
478. **`packages/flutter/lib/src/rendering/flex.dart`** -> AI Confidence: **99.31%**
479. **`packages/flutter/lib/src/rendering/list_wheel_viewport.dart`** -> AI Confidence: **99.31%**
480. **`packages/flutter/lib/src/rendering/platform_view.dart`** -> AI Confidence: **99.31%**
481. **`packages/flutter/lib/src/rendering/proxy_sliver.dart`** -> AI Confidence: **99.31%**
482. **`packages/flutter/lib/src/rendering/shifted_box.dart`** -> AI Confidence: **99.31%**
483. **`packages/flutter/lib/src/rendering/sliver_persistent_header.dart`** -> AI Confidence: **99.31%**
484. **`packages/flutter/lib/src/rendering/sliver_tree.dart`** -> AI Confidence: **99.31%**
485. **`packages/flutter/lib/src/rendering/table.dart`** -> AI Confidence: **99.31%**
486. **`packages/flutter/lib/src/rendering/viewport.dart`** -> AI Confidence: **99.31%**
487. **`packages/flutter/lib/src/scheduler/binding.dart`** -> AI Confidence: **99.31%**
488. **`packages/flutter/lib/src/widgets/_accessibility_evaluations.dart`** -> AI Confidence: **99.31%**
489. **`packages/flutter/lib/src/widgets/_platform_selectable_region_context_menu_web.dart`** -> AI Confidence: **99.31%**
490. **`packages/flutter/lib/src/widgets/_web_image_web.dart`** -> AI Confidence: **99.31%**
491. **`packages/flutter/lib/src/widgets/animated_scroll_view.dart`** -> AI Confidence: **99.31%**
492. **`packages/flutter/lib/src/widgets/binding.dart`** -> AI Confidence: **99.31%**
493. **`packages/flutter/lib/src/widgets/dismissible.dart`** -> AI Confidence: **99.31%**
494. **`packages/flutter/lib/src/widgets/drag_target.dart`** -> AI Confidence: **99.31%**
495. **`packages/flutter/lib/src/widgets/heroes.dart`** -> AI Confidence: **99.31%**
496. **`packages/flutter/lib/src/widgets/image.dart`** -> AI Confidence: **99.31%**
497. **`packages/flutter/lib/src/widgets/image_icon.dart`** -> AI Confidence: **99.31%**
498. **`packages/flutter/lib/src/widgets/interactive_viewer.dart`** -> AI Confidence: **99.31%**
499. **`packages/flutter/lib/src/widgets/list_wheel_scroll_view.dart`** -> AI Confidence: **99.31%**
500. **`packages/flutter/lib/src/widgets/navigator.dart`** -> AI Confidence: **99.31%**
501. **`packages/flutter/lib/src/widgets/nested_scroll_view.dart`** -> AI Confidence: **99.31%**
502. **`packages/flutter/lib/src/widgets/page_view.dart`** -> AI Confidence: **99.31%**
503. **`packages/flutter/lib/src/widgets/radio_group.dart`** -> AI Confidence: **99.31%**
504. **`packages/flutter/lib/src/widgets/raw_menu_anchor.dart`** -> AI Confidence: **99.31%**
505. **`packages/flutter/lib/src/widgets/reorderable_list.dart`** -> AI Confidence: **99.31%**
506. **`packages/flutter/lib/src/widgets/single_child_scroll_view.dart`** -> AI Confidence: **99.31%**
507. **`packages/flutter/lib/src/widgets/sliver_floating_header.dart`** -> AI Confidence: **99.31%**
508. **`packages/flutter/lib/src/widgets/sliver_tree.dart`** -> AI Confidence: **99.31%**
509. **`packages/flutter/lib/src/widgets/snapshot_widget.dart`** -> AI Confidence: **99.31%**
510. **`packages/flutter/lib/src/widgets/toggleable.dart`** -> AI Confidence: **99.31%**
511. **`packages/flutter_driver/lib/src/driver/web_driver.dart`** -> AI Confidence: **99.31%**
512. **`packages/flutter_test/lib/src/mock_canvas.dart`** -> AI Confidence: **99.31%**
513. **`packages/flutter_tools/lib/src/android/android_emulator.dart`** -> AI Confidence: **99.31%**
514. **`packages/flutter_tools/lib/src/android/deferred_components_prebuild_validator.dart`** -> AI Confidence: **99.31%**
515. **`packages/flutter_tools/lib/src/android/gradle.dart`** -> AI Confidence: **99.31%**
516. **`packages/flutter_tools/lib/src/base/build.dart`** -> AI Confidence: **99.31%**
517. **`packages/flutter_tools/lib/src/base/dds.dart`** -> AI Confidence: **99.31%**
518. **`packages/flutter_tools/lib/src/base/error_handling_io.dart`** -> AI Confidence: **99.31%**
519. **`packages/flutter_tools/lib/src/base/net.dart`** -> AI Confidence: **99.31%**
520. **`packages/flutter_tools/lib/src/base/utils.dart`** -> AI Confidence: **99.31%**
521. **`packages/flutter_tools/lib/src/build_system/targets/darwin.dart`** -> AI Confidence: **99.31%**
522. **`packages/flutter_tools/lib/src/build_system/tools/shader_compiler.dart`** -> AI Confidence: **99.31%**
523. **`packages/flutter_tools/lib/src/bundle_builder.dart`** -> AI Confidence: **99.31%**
524. **`packages/flutter_tools/lib/src/commands/assemble.dart`** -> AI Confidence: **99.31%**
525. **`packages/flutter_tools/lib/src/commands/attach.dart`** -> AI Confidence: **99.31%**
526. **`packages/flutter_tools/lib/src/commands/clean.dart`** -> AI Confidence: **99.31%**
527. **`packages/flutter_tools/lib/src/commands/config.dart`** -> AI Confidence: **99.31%**
528. **`packages/flutter_tools/lib/src/commands/daemon.dart`** -> AI Confidence: **99.31%**
529. **`packages/flutter_tools/lib/src/commands/devices.dart`** -> AI Confidence: **99.31%**
530. **`packages/flutter_tools/lib/src/commands/downgrade.dart`** -> AI Confidence: **99.31%**
531. **`packages/flutter_tools/lib/src/commands/emulators.dart`** -> AI Confidence: **99.31%**
532. **`packages/flutter_tools/lib/src/commands/install.dart`** -> AI Confidence: **99.31%**
533. **`packages/flutter_tools/lib/src/commands/symbolize.dart`** -> AI Confidence: **99.31%**
534. **`packages/flutter_tools/lib/src/commands/test.dart`** -> AI Confidence: **99.31%**
535. **`packages/flutter_tools/lib/src/commands/upgrade.dart`** -> AI Confidence: **99.31%**
536. **`packages/flutter_tools/lib/src/compile.dart`** -> AI Confidence: **99.31%**
537. **`packages/flutter_tools/lib/src/custom_devices/custom_device.dart`** -> AI Confidence: **99.31%**
538. **`packages/flutter_tools/lib/src/debug_adapters/flutter_test_adapter.dart`** -> AI Confidence: **99.31%**
539. **`packages/flutter_tools/lib/src/desktop_device.dart`** -> AI Confidence: **99.31%**
540. **`packages/flutter_tools/lib/src/devtools_launcher.dart`** -> AI Confidence: **99.31%**
541. **`packages/flutter_tools/lib/src/drive/drive_service.dart`** -> AI Confidence: **99.31%**
542. **`packages/flutter_tools/lib/src/flutter_application_package.dart`** -> AI Confidence: **99.31%**
543. **`packages/flutter_tools/lib/src/flutter_project_metadata.dart`** -> AI Confidence: **99.31%**
544. **`packages/flutter_tools/lib/src/ios/ios_deploy.dart`** -> AI Confidence: **99.31%**
545. **`packages/flutter_tools/lib/src/ios/simulators.dart`** -> AI Confidence: **99.31%**
546. **`packages/flutter_tools/lib/src/isolated/native_assets/macos/native_assets_host.dart`** -> AI Confidence: **99.31%**
547. **`packages/flutter_tools/lib/src/isolated/native_assets/native_assets.dart`** -> AI Confidence: **99.31%**
548. **`packages/flutter_tools/lib/src/isolated/resident_web_runner.dart`** -> AI Confidence: **99.31%**
549. **`packages/flutter_tools/lib/src/linux/build_linux.dart`** -> AI Confidence: **99.31%**
550. **`packages/flutter_tools/lib/src/localizations/gen_l10n.dart`** -> AI Confidence: **99.31%**
551. **`packages/flutter_tools/lib/src/macos/darwin_dependency_management.dart`** -> AI Confidence: **99.31%**
552. **`packages/flutter_tools/lib/src/macos/xcdevice.dart`** -> AI Confidence: **99.31%**
553. **`packages/flutter_tools/lib/src/migrations/swift_package_manager_integration_migration.dart`** -> AI Confidence: **99.31%**
554. **`packages/flutter_tools/lib/src/reporting/github_template.dart`** -> AI Confidence: **99.31%**
555. **`packages/flutter_tools/lib/src/runner/flutter_command.dart`** -> AI Confidence: **99.31%**
556. **`packages/flutter_tools/lib/src/runner/flutter_command_runner.dart`** -> AI Confidence: **99.31%**
557. **`packages/flutter_tools/lib/src/runner/local_engine.dart`** -> AI Confidence: **99.31%**
558. **`packages/flutter_tools/lib/src/runner/target_devices.dart`** -> AI Confidence: **99.31%**
559. **`packages/flutter_tools/lib/src/test/coverage_collector.dart`** -> AI Confidence: **99.31%**
560. **`packages/flutter_tools/lib/src/test/flutter_platform.dart`** -> AI Confidence: **99.31%**
561. **`packages/flutter_tools/lib/src/test/runner.dart`** -> AI Confidence: **99.31%**
562. **`packages/flutter_tools/lib/src/web/devfs_config.dart`** -> AI Confidence: **99.31%**
563. **`packages/flutter_tools/lib/src/web_template.dart`** -> AI Confidence: **99.31%**
564. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/AndroidTouchProcessor.java`** -> AI Confidence: **99.31%**
565. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/KeyEmbedderResponder.java`** -> AI Confidence: **99.31%**
566. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/FlutterEngineConnectionRegistry.java`** -> AI Confidence: **99.31%**
567. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/deferredcomponents/PlayStoreDeferredComponentManager.java`** -> AI Confidence: **99.31%**
568. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/LifecycleChannel.java`** -> AI Confidence: **99.31%**
569. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/ScribeChannel.java`** -> AI Confidence: **99.31%**
570. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/systemchannels/TextInputChannel.java`** -> AI Confidence: **99.31%**
571. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/common/JSONUtil.java`** -> AI Confidence: **99.31%**
572. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/editing/InputConnectionAdaptor.java`** -> AI Confidence: **99.31%**
573. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/editing/TextInputPlugin.java`** -> AI Confidence: **99.31%**
574. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/localization/LocalizationPlugin.java`** -> AI Confidence: **99.31%**
575. **`engine/src/flutter/shell/platform/android/io/flutter/plugin/platform/PlatformPlugin.java`** -> AI Confidence: **99.31%**
576. **`engine/src/flutter/shell/platform/android/io/flutter/view/AccessibilityBridge.java`** -> AI Confidence: **99.31%**
577. **`engine/src/flutter/testing/fuchsia/run_tests.py`** -> AI Confidence: **99.31%**
578. **`engine/src/flutter/testing/run_tests.py`** -> AI Confidence: **99.31%**
579. **`engine/src/flutter/tools/download_fuchsia_sdk.py`** -> AI Confidence: **99.31%**
580. **`engine/src/flutter/tools/fuchsia/build_fuchsia_artifacts.py`** -> AI Confidence: **99.31%**
581. **`bin/internal/content_aware_hash.sh`** -> AI Confidence: **99.29%**
582. **`bin/internal/last_engine_commit.sh`** -> AI Confidence: **99.29%**
583. **`engine/src/flutter/lib/web_ui/dev/felt`** -> AI Confidence: **99.29%**
584. **`engine/src/flutter/testing/analyze_core_dump.sh`** -> AI Confidence: **99.29%**
585. **`engine/src/flutter/tools/fuchsia/devshell/lib/vars.sh`** -> AI Confidence: **99.29%**
586. **`engine/src/flutter/tools/fuchsia/devshell/run_integration_test.sh`** -> AI Confidence: **99.29%**
587. **`engine/src/flutter/tools/vscode_workspace/refresh.sh`** -> AI Confidence: **99.29%**
588. **`bin/internal/content_aware_hash.ps1`** -> AI Confidence: **99.29%**
589. **`bin/internal/last_engine_commit.ps1`** -> AI Confidence: **99.29%**
590. **`bin/internal/update_dart_sdk.ps1`** -> AI Confidence: **99.29%**
591. **`dev/integration_tests/pure_android_host_apps/host_app_kotlin_gradle_dsl/settings.gradle.kts`** -> AI Confidence: **99.29%**
592. **`packages/flutter_tools/gradle/resolve_dependencies.gradle.kts`** -> AI Confidence: **99.29%**
593. **`packages/flutter_tools/gradle/src/main/kotlin/AppLinkSettings.kt`** -> AI Confidence: **99.29%**
594. **`packages/flutter_tools/gradle/src/main/kotlin/BaseApplicationNameHandler.kt`** -> AI Confidence: **99.29%**
595. **`packages/flutter_tools/gradle/src/main/kotlin/Deeplink.kt`** -> AI Confidence: **99.29%**
596. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterExtension.kt`** -> AI Confidence: **99.29%**
597. **`packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginConstants.kt`** -> AI Confidence: **99.29%**
598. **`packages/flutter_tools/gradle/src/main/kotlin/NativePluginLoaderReflectionBridge.kt`** -> AI Confidence: **99.29%**
599. **`packages/flutter_tools/gradle/src/main/kotlin/VersionUtils.kt`** -> AI Confidence: **99.29%**
600. **`packages/flutter_tools/gradle/src/main/scripts/native_plugin_loader.gradle.kts`** -> AI Confidence: **99.29%**
601. **`packages/flutter_tools/gradle/src/test/kotlin/FlutterExtensionTest.kt`** -> AI Confidence: **99.29%**
602. **`dev/benchmarks/multiple_flutters/android/settings.gradle`** -> AI Confidence: **99.29%**
603. **`dev/integration_tests/module_host_with_custom_build_v2_embedding/settings.gradle`** -> AI Confidence: **99.29%**
604. **`dev/integration_tests/pure_android_host_apps/android_custom_host_app/settings.gradle`** -> AI Confidence: **99.29%**
605. **`engine/src/flutter/shell/platform/android/build.gradle`** -> AI Confidence: **99.29%**
606. **`engine/src/flutter/shell/platform/android/test_runner/build.gradle`** -> AI Confidence: **99.29%**
607. **`engine/src/flutter/tools/cipd/android_embedding_bundle/build.gradle`** -> AI Confidence: **99.29%**
608. **`packages/flutter_tools/gradle/app_plugin_loader.gradle`** -> AI Confidence: **99.29%**
609. **`packages/flutter_tools/gradle/flutter.gradle`** -> AI Confidence: **99.29%**
610. **`dev/integration_tests/ios_app_with_extensions/ios/watch Extension/ExtensionDelegate.swift`** -> AI Confidence: **99.29%**
611. **`dev/benchmarks/microbenchmarks/ios/Runner/main.m`** -> AI Confidence: **99.29%**
612. **`dev/benchmarks/platform_channels_benchmarks/ios/Runner/main.m`** -> AI Confidence: **99.29%**
613. **`dev/integration_tests/ios_add2app_life_cycle/ios_add2app/main.m`** -> AI Confidence: **99.29%**
614. **`dev/integration_tests/ios_host_app/Host/main.m`** -> AI Confidence: **99.29%**
615. **`engine/src/flutter/display_list/testing/dl_test_surface_provider_metal.mm`** -> AI Confidence: **99.29%**
616. **`engine/src/flutter/fml/platform/darwin/concurrent_message_loop_factory.mm`** -> AI Confidence: **99.29%**
617. **`engine/src/flutter/fml/platform/darwin/message_loop_darwin.mm`** -> AI Confidence: **99.29%**
618. **`engine/src/flutter/fml/platform/darwin/platform_version.mm`** -> AI Confidence: **99.29%**
619. **`engine/src/flutter/fml/platform/darwin/string_range_sanitization.mm`** -> AI Confidence: **99.29%**
620. **`engine/src/flutter/impeller/golden_tests/metal_screenshot.mm`** -> AI Confidence: **99.29%**
621. **`engine/src/flutter/impeller/golden_tests/vulkan_screenshotter.mm`** -> AI Confidence: **99.29%**
622. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pass_bindings_cache_mtl.mm`** -> AI Confidence: **99.29%**
623. **`engine/src/flutter/impeller/renderer/backend/metal/compute_pipeline_mtl.mm`** -> AI Confidence: **99.29%**
624. **`engine/src/flutter/impeller/renderer/backend/metal/formats_mtl.mm`** -> AI Confidence: **99.29%**
625. **`engine/src/flutter/impeller/renderer/backend/metal/pass_bindings_cache_mtl.mm`** -> AI Confidence: **99.29%**
626. **`engine/src/flutter/impeller/renderer/backend/metal/pipeline_mtl.mm`** -> AI Confidence: **99.29%**
627. **`engine/src/flutter/impeller/renderer/backend/metal/sampler_mtl.mm`** -> AI Confidence: **99.29%**
628. **`engine/src/flutter/impeller/renderer/backend/metal/shader_function_mtl.mm`** -> AI Confidence: **99.29%**
629. **`engine/src/flutter/impeller/renderer/backend/metal/shader_library_mtl.mm`** -> AI Confidence: **99.29%**
630. **`engine/src/flutter/impeller/renderer/backend/metal/swapchain_transients_mtl.mm`** -> AI Confidence: **99.29%**
631. **`engine/src/flutter/impeller/renderer/backend/metal/texture_wrapper_mtl.mm`** -> AI Confidence: **99.29%**
632. **`engine/src/flutter/shell/common/shell_test_platform_view_metal.mm`** -> AI Confidence: **99.29%**
633. **`engine/src/flutter/shell/platform/darwin/common/buffer_conversions.mm`** -> AI Confidence: **99.29%**
634. **`engine/src/flutter/shell/platform/darwin/common/command_line.mm`** -> AI Confidence: **99.29%**
635. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterBinaryMessengerRelay.mm`** -> AI Confidence: **99.29%**
636. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterChannels.mm`** -> AI Confidence: **99.29%**
637. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterCodecs.mm`** -> AI Confidence: **99.29%**
638. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterStandardCodec.mm`** -> AI Confidence: **99.29%**
639. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterStandardCodec_Internal.h`** -> AI Confidence: **99.29%**
640. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/FlutterTestUtils.mm`** -> AI Confidence: **99.29%**
641. **`engine/src/flutter/shell/platform/darwin/common/framework/Source/flutter_codecs_unittest.mm`** -> AI Confidence: **99.29%**
642. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterChannelKeyResponder.mm`** -> AI Confidence: **99.29%**
643. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterOverlayView.mm`** -> AI Confidence: **99.29%**
644. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterRestorationPlugin.mm`** -> AI Confidence: **99.29%**
645. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextureRegistryRelay.mm`** -> AI Confidence: **99.29%**
646. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/SemanticsObjectTestMocks.h`** -> AI Confidence: **99.29%**
647. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/TextInputSemanticsObject.mm`** -> AI Confidence: **99.29%**
648. **`engine/src/flutter/shell/platform/darwin/ios/framework/Source/platform_message_response_darwin.mm`** -> AI Confidence: **99.29%**
649. **`engine/src/flutter/shell/platform/darwin/ios/ios_external_texture_metal.mm`** -> AI Confidence: **99.29%**
650. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterExternalTexture.mm`** -> AI Confidence: **99.29%**
651. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterKeyboardLayout.mm`** -> AI Confidence: **99.29%**
652. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterPlatformViewController.mm`** -> AI Confidence: **99.29%**
653. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterSurface.mm`** -> AI Confidence: **99.29%**
654. **`engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewControllerTestUtils.mm`** -> AI Confidence: **99.29%**
655. **`engine/src/flutter/shell/platform/embedder/tests/embedder_test_metal.mm`** -> AI Confidence: **99.29%**
656. **`engine/src/flutter/testing/ios/IosBenchmarks/IosBenchmarks/main.mm`** -> AI Confidence: **99.29%**
657. **`engine/src/flutter/testing/ios/IosUnitTests/App/main.m`** -> AI Confidence: **99.29%**
658. **`engine/src/flutter/testing/ios_scenario_app/ios/FlutterAppExtensionTestHost/FlutterAppExtensionTestHost/main.m`** -> AI Confidence: **99.29%**
659. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/ScenariosUITests/GoldenImage.m`** -> AI Confidence: **99.29%**
660. **`engine/src/flutter/testing/ios_scenario_app/ios/Scenarios/ScenariosUITests/iPadGestureTests.m`** -> AI Confidence: **99.29%**
661. **`engine/src/flutter/testing/test_metal_surface.mm`** -> AI Confidence: **99.29%**
662. **`dev/tools/gen_keycodes/data/supplemental_key_data.inc`** -> AI Confidence: **99.29%**
663. **`engine/src/flutter/benchmarking/library.h`** -> AI Confidence: **99.29%**
664. **`engine/src/flutter/common/macros.h`** -> AI Confidence: **99.29%**
665. **`engine/src/flutter/display_list/dl_paint.cc`** -> AI Confidence: **99.29%**
666. **`engine/src/flutter/display_list/effects/color_filters/dl_blend_color_filter.cc`** -> AI Confidence: **99.29%**
667. **`engine/src/flutter/fml/build_config.h`** -> AI Confidence: **99.29%**
668. **`engine/src/flutter/fml/eintr_wrapper.h`** -> AI Confidence: **99.29%**
669. **`engine/src/flutter/impeller/base/thread_safety.h`** -> AI Confidence: **99.29%**
670. **`engine/src/flutter/impeller/renderer/backend/gles/formats_gles.cc`** -> AI Confidence: **99.29%**
671. **`engine/src/flutter/lib/gpu/export.h`** -> AI Confidence: **99.29%**
672. **`engine/src/flutter/lib/ui/window/viewport_metrics.cc`** -> AI Confidence: **99.29%**
673. **`engine/src/flutter/shell/common/switch_defs.h`** -> AI Confidence: **99.29%**
674. **`engine/src/flutter/shell/platform/android/platform_view_android_delegate/platform_view_android_delegate.cc`** -> AI Confidence: **99.29%**
675. **`engine/src/flutter/shell/platform/common/public/flutter_macros.h`** -> AI Confidence: **99.29%**
676. **`engine/src/flutter/shell/platform/fuchsia/dart_pkg/zircon_ffi/macros.h`** -> AI Confidence: **99.29%**
677. **`engine/src/flutter/shell/platform/glfw/text_input_plugin.cc`** -> AI Confidence: **99.29%**
678. **`engine/src/flutter/shell/platform/linux/fl_application_test.cc`** -> AI Confidence: **99.29%**
679. **`engine/src/flutter/shell/platform/linux/fl_dart_project_test.cc`** -> AI Confidence: **99.29%**
680. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_binary_codec.h`** -> AI Confidence: **99.29%**
681. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_json_method_codec.h`** -> AI Confidence: **99.29%**
682. **`engine/src/flutter/shell/platform/linux/public/flutter_linux/fl_string_codec.h`** -> AI Confidence: **99.29%**
683. **`engine/src/flutter/shell/platform/windows/accessibility_bridge_windows.cc`** -> AI Confidence: **99.29%**
684. **`engine/src/flutter/tools/licenses_cpp/src/catalog_unittests.cc`** -> AI Confidence: **99.29%**
685. **`engine/src/flutter/vulkan/swiftshader_path.h`** -> AI Confidence: **99.29%**
686. **`dev/benchmarks/macrobenchmarks/web/flutter_bootstrap.js`** -> AI Confidence: **99.29%**
687. **`dev/snippets/lib/src/snippet_parser.dart`** -> AI Confidence: **99.29%**
688. **`dev/tools/android_driver_extensions/test/src/fake_adb.dart`** -> AI Confidence: **99.29%**
689. **`engine/src/flutter/lib/ui/lerp.dart`** -> AI Confidence: **99.29%**
690. **`engine/src/flutter/lib/web_ui/dev/generate_scene_test.dart`** -> AI Confidence: **99.29%**
691. **`engine/src/flutter/lib/web_ui/lib/semantics.dart`** -> AI Confidence: **99.29%**
692. **`engine/src/flutter/lib/web_ui/lib/src/engine/onscreen_logging.dart`** -> AI Confidence: **99.29%**
693. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paint_clusters.dart`** -> AI Confidence: **99.29%**
694. **`engine/src/flutter/lib/web_ui/lib/src/engine/web_paragraph/paint_paragraph.dart`** -> AI Confidence: **99.29%**
695. **`engine/src/flutter/lib/web_ui/test/ui/text_style_test.dart`** -> AI Confidence: **99.29%**
696. **`engine/src/flutter/lib/web_ui/test/webparagraph/paragraph_codepoint_info_test.dart`** -> AI Confidence: **99.29%**
697. **`engine/src/flutter/testing/dart/paragraph_test.dart`** -> AI Confidence: **99.29%**
698. **`packages/flutter/lib/src/foundation/_capabilities_io.dart`** -> AI Confidence: **99.29%**
699. **`packages/flutter/lib/src/gestures/resampler.dart`** -> AI Confidence: **99.29%**
700. **`packages/flutter/lib/src/material/menu_anchor.dart`** -> AI Confidence: **99.29%**
701. **`packages/flutter/lib/src/material/navigation_bar.dart`** -> AI Confidence: **99.29%**
702. **`packages/flutter/lib/src/material/navigation_rail.dart`** -> AI Confidence: **99.29%**
703. **`packages/flutter/lib/src/services/flavor.dart`** -> AI Confidence: **99.29%**
704. **`packages/flutter/lib/src/services/flutter_version.dart`** -> AI Confidence: **99.29%**
705. **`packages/flutter/lib/src/services/text_layout_metrics.dart`** -> AI Confidence: **99.29%**
706. **`packages/flutter/lib/src/widgets/raw_tooltip.dart`** -> AI Confidence: **99.29%**
707. **`packages/flutter_tools/bin/tool_backend.dart`** -> AI Confidence: **99.29%**
708. **`packages/flutter_tools/bin/xcode_backend.dart`** -> AI Confidence: **99.29%**
709. **`packages/flutter_tools/lib/src/android/build_validation.dart`** -> AI Confidence: **99.29%**
710. **`packages/flutter_tools/lib/src/debug_adapters/error_formatter.dart`** -> AI Confidence: **99.29%**
711. **`packages/flutter_tools/lib/src/web/web_constants.dart`** -> AI Confidence: **99.29%**
712. **`engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/loader/FlutterApplicationInfo.java`** -> AI Confidence: **99.29%**
713. **`dev/integration_tests/ios_add2app_uiscene/NativeSwiftUIExperiment/Podfile`** -> AI Confidence: **99.29%**
714. **`dev/integration_tests/ios_add2app_uiscene/NativeUIKitSwiftExperiment/Podfile`** -> AI Confidence: **99.29%**
715. **`engine/src/BUILD.gn`** -> AI Confidence: **99.29%**
716. **`engine/src/flutter/BUILD.gn`** -> AI Confidence: **99.29%**
717. **`engine/src/flutter/benchmarking/BUILD.gn`** -> AI Confidence: **99.29%**
718. **`engine/src/flutter/display_list/testing/BUILD.gn`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `dev/benchmarks/macrobenchmarks/lib/src/fullscreen_textfield.dart` -> **99.9412%** Exposure
- `engine/src/flutter/shell/platform/fuchsia/dart_pkg/zircon/test/zircon_tests.dart` -> **74.9657%** Exposure
### Exploit Generation Surface
- `dev/tools/repackage_gradle_wrapper.sh` -> **100.0%** Exposure
- `engine/src/flutter/lib/web_ui/dev/felt` -> **100.0%** Exposure
- `dev/benchmarks/multiple_flutters/android/app/src/main/java/dev/flutter/multipleflutters/MainActivity.kt` -> **100.0%** Exposure
- `dev/benchmarks/platform_channels_benchmarks/android/app/src/main/kotlin/com/example/platform_channels_benchmarks/MainActivity.kt` -> **100.0%** Exposure
- `packages/flutter_tools/gradle/src/main/kotlin/DependencyVersionChecker.kt` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `bin/internal/update_dart_sdk.sh` -> **100.0%** Exposure
- `dev/tools/repackage_gradle_wrapper.sh` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/fuchsia/runtime/dart/utils/run_vmservice_object_tests.sh` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterViewController.mm` -> **100.0%** Exposure
- `dev/bots/analyze.dart` -> **100.0%** Exposure
### Raw Memory Manipulation
- `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEmbedderKeyResponderTest.mm` -> **10.0%** Exposure
- `engine/src/flutter/shell/platform/linux/fl_text_input_handler.cc` -> **10.0%** Exposure
- `engine/src/flutter/shell/platform/windows/keyboard_key_embedder_handler_unittests.cc` -> **10.0%** Exposure
- `engine/src/flutter/flow/layers/image_filter_layer_unittests.cc` -> **9.9999%** Exposure
- `engine/src/flutter/impeller/renderer/renderer_unittests.cc` -> **9.9995%** Exposure
### Algorithmic DoS Exposure
- `bin/internal/shared.sh` -> **100.0%** Exposure
- `bin/internal/update_dart_sdk.sh` -> **100.0%** Exposure
- `packages/flutter_tools/gradle/src/main/kotlin/DependencyVersionChecker.kt` -> **100.0%** Exposure
- `packages/flutter_tools/gradle/src/main/kotlin/FlutterPlugin.kt` -> **100.0%** Exposure
- `packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `26` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36191` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `packages/flutter/test_private/bin/test_private.dart` (DART) -> Cumulative Risk: **917.62**
- **Archetype:** `file_cluster_4` (Distance: 12.466 IQR)
- **Magnitude:** 194.0 | **LOC:** 289 | **CtrlFlow:** 63.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `File` (Impact: 63.5), `stderr.writeln` (Impact: 12.3), `_usage` (Impact: 11.1)

### 2. `engine/src/flutter/tools/licenses_cpp/tools/convert.dart` (DART) -> Cumulative Risk: **890.12**
- **Archetype:** `file_cluster_17` (Distance: 15.833 IQR)
- **Magnitude:** 0.41 | **LOC:** 145 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `currentType` (Impact: 82.3), `main` (Impact: 22.4), `import` (Impact: 3.7)

### 3. `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/font_collection.dart` (DART) -> Cumulative Risk: **860.79**
- **Archetype:** `file_cluster_4` (Distance: 12.413 IQR)
- **Magnitude:** 168.78 | **LOC:** 236 | **CtrlFlow:** 35.2% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `withStackScope` (Impact: 26.4), `loadAssetFonts` (Impact: 22.4), `setDefaultFontFamilies` (Impact: 8.4)

### 4. `dev/bots/suite_runners/run_android_engine_tests.dart` (DART) -> Cumulative Risk: **860.68**
- **Archetype:** `file_cluster_11` (Distance: 16.75 IQR)
- **Magnitude:** 103.32 | **LOC:** 156 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), State Flux (99.9844%)
- **Heaviest Functions:** `try` (Impact: 53.2), `return` (Impact: 1.2), `runAndroidEngineTests` (Impact: 1.1)

### 5. `engine/src/flutter/shell/platform/fuchsia/dart_runner/dart_runner.cc` (CPP) -> Cumulative Risk: **857.79**
- **Archetype:** `file_cluster_13` (Distance: 12.822 IQR)
- **Magnitude:** 136.76 | **LOC:** 283 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `IsolateGroupCreateCallback` (Impact: 40.5), `IsolateShutdownCallback` (Impact: 22.3), `DartRunner::handle_unknown_method` (Impact: 5.2)

### 6. `engine/src/flutter/impeller/entity/contents/runtime_effect_contents.cc` (CPP) -> Cumulative Risk: **852.14**
- **Archetype:** `file_cluster_13` (Distance: 14.14 IQR)
- **Magnitude:** 618.76 | **LOC:** 394 | **CtrlFlow:** 59.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `MakeShaderMetadata` (Impact: 150.5), `RuntimeEffectContents::Render` (Impact: 75.4), `RuntimeEffectContents::RegisterShader` (Impact: 49.6)

### 7. `engine/src/flutter/lib/web_ui/dev/chrome.dart` (DART) -> Cumulative Risk: **847.04**
- **Archetype:** `file_cluster_11` (Distance: 12.853 IQR)
- **Magnitude:** 191.56 | **LOC:** 409 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `BrowserProcess` (Impact: 116.5), `import` (Impact: 5.3), `Chrome` (Impact: 1.4)

### 8. `dev/tools/bin/format.dart` (DART) -> Cumulative Risk: **833.94**
- **Archetype:** `file_cluster_4` (Distance: 13.001 IQR)
- **Magnitude:** 0.51 | **LOC:** 288 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `exit` (Impact: 339.3), `main` (Impact: 22.8), `return` (Impact: 5.7)

### 9. `engine/src/flutter/shell/platform/glfw/event_loop.cc` (CPP) -> Cumulative Risk: **832.77**
- **Archetype:** `file_cluster_4` (Distance: 11.912 IQR)
- **Magnitude:** 119.22 | **LOC:** 104 | **CtrlFlow:** 43.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `EventLoop::WaitForEvents` (Impact: 45.0), `EventLoop::PostTask` (Impact: 7.1), `EventLoop::EventLoop` (Impact: 5.3)

### 10. `engine/src/flutter/lib/gpu/context.cc` (CPP) -> Cumulative Risk: **828.96**
- **Archetype:** `file_cluster_13` (Distance: 13.486 IQR)
- **Magnitude:** 136.5 | **LOC:** 139 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Concurrency (99.9998%)
- **Heaviest Functions:** `Context::GetDefaultContext` (Impact: 44.1), `InternalFlutterGpu_Context_InitializeDef` (Impact: 4.1), `SupportsNormalOffscreenMSAA` (Impact: 3.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `packages/flutter/lib/src/rendering/editable.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.555 IQR)
- **Top Global Matches:** file_cluster_15: 13.555, file_cluster_17: 13.684, file_cluster_8: 13.71
- **Magnitude:** 6060.02 | **LOC:** 3157 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (13.0631%), Tech Debt (11.265%)
**Top Internal Functions/Classes:**
  * `TextLayoutMetrics` (Impact: 5939.2 | O(N^4) | DB: 17)
  * `moveByOffset` (Impact: 24.6 | O(N^2))
  * `import` (Impact: 6.0 | O(N^1))
  * `_getTextPositionForLine` (Impact: 5.9 | O(N^1))
    * *Intent:* /// The consecutive sequence of [TextPosition]s that the caret should move to /// when the user navi...
  * `moveNext` (Impact: 3.4 | O(N^1))
    * *Intent:* /// horizontal location and move to the second line. Similarly the caret moves /// to the end of the...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 189`, `args: 109`, `func_start: 410`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 49`, `dead_code: 2`, `planned_debt: 4`, `orphaned_logic: 2`
* *Architecture:* `api: 1`, `import: 14`
* *Defense:* `safety: 200`, `doc: 405`, `immutability_locks: 113`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` object.dart, foundation.dart, characters.dart, custom_paint.dart, layer.dart, services.dart, dart:ui, box.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/lib/src/vmservice.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_16` (Drift: 14.154 IQR)
- **Top Global Matches:** file_cluster_16: 14.154, file_cluster_4: 14.162, file_cluster_15: 14.303
- **Magnitude:** 5218.46 | **LOC:** 1018 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (46.9579%), Tech Debt (13.859%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 4895.0 | O(2^N) | DB: 6)
  * `async` (Impact: 112.0 | O(2^N) | DB: 7)
  * `openChannelForTesting` (Impact: 7.1 | O(N^1))
    * *Intent:* /// A testing only override of the WebSocket connector. /// /// Provide a `null` value to restore th...
  * `import` (Impact: 2.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 152`, `args: 57`, `func_start: 177`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 10`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 14`, `concurrency: 163`, `import: 14`
* *Defense:* `safety: 268`, `doc: 101`, `sync_locks: 1`, `immutability_locks: 80`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.269
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` cache.dart, dart:async, logger.dart, utils.dart, globals.dart, context.dart, convert.dart, vm_service.dart...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `engine/src/flutter/testing/android/native_activity/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/paragraph.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.033 IQR)
- **Top Global Matches:** file_cluster_8: 12.033, file_cluster_15: 12.164, file_cluster_17: 12.293
- **Magnitude:** 4714.3 | **LOC:** 3625 | **CtrlFlow:** 72.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (11.7566%), Tech Debt (52.1264%)
**Top Internal Functions/Classes:**
  * `RelayoutWhenSystemFontsChangeMixin` (Impact: 3568.5 | O(N^4) | DB: 12)
  * `_updateSelectionStartEdgeAtPlaceholderBy` (Impact: 400.9 | O(N^4))
  * `_getClampedParagraphBoundaryAtPosition` (Impact: 259.9 | O(N^3) | DB: 4)
  * `_updateSelectionEndEdgeByMultiSelectable` (Impact: 54.1 | O(N^4))
    * *Intent:* // A paragraph boundary may not be completely contained within this root // selectable fragment. Kee...
  * `hashCode` (Impact: 48.2 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 241`, `args: 100`, `func_start: 561`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 40`, `dead_code: 3`, `planned_debt: 6`, `duplicate_logic: 15`
* *Architecture:* `api: 13`, `import: 12`
* *Defense:* `safety: 192`, `doc: 140`, `immutability_locks: 253`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` object.dart, foundation.dart, layer.dart, debug.dart, services.dart, selection.dart, dart:ui, box.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/chip.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.138 IQR)
- **Top Global Matches:** file_cluster_0: 14.138, file_cluster_13: 14.23, file_cluster_2: 14.283
- **Magnitude:** 4073.74 | **LOC:** 2570 | **CtrlFlow:** 74.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.508%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `deleteIconColor` (Impact: 4054.9 | O(2^N) | DB: 2)
    * *Intent:* /// Theme used for all icons in the chip. /// /// If this is null and [ThemeData.useMaterial3] is tr...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 55`, `args: 13`, `func_start: 161`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `api: 3`, `import: 18`
* *Defense:* `safety: 144`, `doc: 392`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` foundation.dart, debug.dart, constants.dart, tooltip.dart, rendering.dart, material.dart, widgets.dart, theme.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/app_bar_theme.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.808 IQR)
- **Top Global Matches:** file_cluster_8: 14.808, file_cluster_0: 14.851, file_cluster_13: 14.861
- **Magnitude:** 3463.42 | **LOC:** 638 | **CtrlFlow:** 89.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (19.4181%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import` (Impact: 3162.7 | O(N^5))
  * `debugFillProperties` (Impact: 196.2 | O(2^N) | DB: 17)
  * `operator==` (Impact: 31.4 | O(N^2))
  * `copyWith` (Impact: 20.2 | O(N^1))
  * `lerp` (Impact: 17.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 335`, `structural_boundaries: 40`, `args: 11`, `func_start: 107`, `class_start: 2`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 251`, `doc: 150`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` foundation.dart, widgets.dart, services.dart, dart:ui, theme.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/semantics/semantics.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_15` (Drift: 15.058 IQR)
- **Top Global Matches:** file_cluster_15: 15.058, file_cluster_11: 15.299, file_cluster_16: 15.401
- **Magnitude:** 3366.8 | **LOC:** 7176 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (32.9429%), Tech Debt (43.075%)
**Top Internal Functions/Classes:**
  * `visitedNodes.addAll` (Impact: 1049.5 | O(N^3) | DB: 26)
  * `detach` (Impact: 641.9 | O(2^N) | DB: 26)
    * *Intent:* /// If non-null, whether the node is able to hold input focus. /// /// If [focusable] is set to fals...
  * `debugFillProperties` (Impact: 249.3 | O(2^N) | DB: 40)
    * *Intent:* /// The handler for [SemanticsAction.collapse].
  * `assert` (Impact: 85.3 | O(N^4) | DB: 3)
  * `debugFillProperties` (Impact: 71.2 | O(2^N) | DB: 31)
    * *Intent:* /// A tag for a [SemanticsNode]. /// /// Tags can be interpreted by the parent of a [SemanticsNode] ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 323`, `args: 160`, `func_start: 834`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 397`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 15`
* *Architecture:* `api: 33`, `import: 16`
* *Defense:* `safety: 495`, `doc: 1353`, `test: 16`, `immutability_locks: 204`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` foundation.dart, semantics_event.dart, binding.dart, services.dart, collection.dart, dart:ui, painting.dart, dart:core...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/lib/src/test/runner.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.306 IQR)
- **Top Global Matches:** file_cluster_4: 14.306, file_cluster_13: 14.306, file_cluster_11: 14.357
- **Magnitude:** 3269.2 | **LOC:** 758 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 164
- **Risk Profile:** Cognitive Load (88.0848%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import` (Impact: 2962.6 | O(2^N) | DB: 164)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 121`, `structural_boundaries: 83`, `args: 24`, `func_start: 111`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 197`, `dead_code: 1`
* *Architecture:* `io: 31`, `api: 4`, `concurrency: 93`, `import: 40`
* *Defense:* `safety: 78`, `doc: 6`, `test: 9`, `sync_locks: 2`, `immutability_locks: 81`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` flutter_web_platform.dart, dart:async, isolate_channel.dart, cache.dart, dart:ui, device.dart, watcher.dart, io.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm` (OBJECTIVE-C | Tier 0 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.697 IQR)
- **Top Global Matches:** file_cluster_8: 13.697, file_cluster_11: 14.001, file_cluster_13: 14.031
- **Magnitude:** 3257.08 | **LOC:** 4213 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (64.1828%), Tech Debt (99.7032%)
**Top Internal Functions/Classes:**
  * `testTextEditingDeltasAreBatchedAndForwar` (Impact: 390.5 | O(N^6) | DB: 6)
  * `testTextEditingDeltasAreGeneratedOnTextI` (Impact: 158.0 | O(N^6) | DB: 10)
  * `testInteractiveKeyboardAfterUserScrollTo` (Impact: 110.7 | O(N^6) | DB: 10)
  * `testInteractiveKeyboardKeyboardReappears` (Impact: 84.4 | O(N^6) | DB: 13)
  * `testInteractiveKeyboardScreenshotWillBeM` (Impact: 84.3 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 31`, `args: 544`, `func_start: 152`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 741`, `dead_code: 1`, `fragile_debt: 1`, `duplicate_logic: 33`, `orphaned_logic: 68`
* *Architecture:* `io: 1`, `api: 14`, `concurrency: 12`, `import: 9`
* *Defense:* `safety: 99`, `test: 333`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FlutterViewController.h, UIViewController+FlutterScreenAndSceneIfLoaded.h, FlutterEngine_Test.h, OCMock.h, FlutterTextInputPlugin.h, FlutterBinaryMessengerRelay.h, XCTest.h, FlutterEngine.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/display_list/testing/dl_rendering_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.165 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.073 IQR)
- **Top Global Matches:** file_cluster_8: 14.165, file_cluster_13: 14.262, file_cluster_11: 14.378
- **Magnitude:** 3206.32 | **LOC:** 4901 | **CtrlFlow:** 44.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 260
- **Risk Profile:** Cognitive Load (96.9471%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `lineAdjust` (Impact: 539.1 | O(N^6) | DB: 260)
  * `should_match` (Impact: 245.8 | O(N^5) | DB: 28)
  * `SetUpTestSuite` (Impact: 113.0 | O(N^6) | DB: 41)
  * `test_attributes_image` (Impact: 57.9 | O(N^6) | DB: 17)
  * `adjust` (Impact: 50.2 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 254`, `args: 317`, `func_start: 127`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1446`, `dead_code: 3`, `duplicate_logic: 41`, `orphaned_logic: 12`
* *Architecture:* `api: 11`, `import: 39`
* *Defense:* `safety: 40`, `test: 48`, `immutability_locks: 355`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SkColor.h, SkImageFilters.h, utility, dl_matrix_color_filter.h, SkBBHFactory.h, SkFontMgr.h, SkPictureRecorder.h, dl_text_impeller.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/impeller/renderer/backend/vulkan/test/mock_vulkan.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.559 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.357 IQR)
- **Top Global Matches:** file_cluster_8: 12.559, file_cluster_13: 12.901, file_cluster_7: 13.039
- **Magnitude:** 3187.5 | **LOC:** 1087 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (96.1899%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GetMockVulkanProcAddress` (Impact: 1778.3 | O(2^N))
  * `vkGetQueryPoolResults` (Impact: 127.2 | O(2^N) | DB: 9)
  * `vkCmdPipelineBarrier` (Impact: 70.6 | O(2^N) | DB: 3)
  * `format_properties_callback_` (Impact: 42.9 | O(N^6) | DB: 3)
  * `vkResetCommandPool` (Impact: 42.5 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 194`, `args: 99`, `func_start: 91`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 2`, `state_mutation: 306`, `orphaned_logic: 8`
* *Architecture:* `api: 2`, `import: 10`
* *Defense:* `safety: 11`, `sync_locks: 15`, `immutability_locks: 86`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vulkan.hpp, vulkan_core.h, utility, cstring, cstdint, logging.h, thread_safety.h, vk.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/gradle/src/test/kotlin/FlutterPluginUtilsTest.kt` (KOTLIN | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.068 IQR)
- **Top Global Matches:** file_cluster_8: 12.068, file_cluster_0: 12.156, file_cluster_16: 12.227
- **Magnitude:** 3160.95 | **LOC:** 1072 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (19.2334%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `args: 50`, `func_start: 50`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 63`
* *Architecture:* `io: 8`, `api: 3`, `import: 31`
* *Defense:* `safety: 33`, `test: 288`, `immutability_locks: 148`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.gradle.api.Action, io.mockk.verify, org.gradle.api.file.Directory, io.mockk.mockk, org.junit.jupiter.api.assertThrows, java.io.File, org.gradle.api.Task, com.android.build.gradle.internal.dsl.DefaultConfig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/tabs.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_2` (Drift: 13.959 IQR)
- **Top Global Matches:** file_cluster_2: 13.959, file_cluster_17: 14.055, file_cluster_13: 14.067
- **Magnitude:** 3071.26 | **LOC:** 2941 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (20.3544%), Tech Debt (16.9795%)
**Top Internal Functions/Classes:**
  * `Size.fromHeight` (Impact: 2920.2 | O(N^5) | DB: 12)
  * `build` (Impact: 39.8 | O(N^3))
    * *Intent:* /// The margin added around the tab's icon. ///
  * `Size.fromHeight` (Impact: 10.2 | O(2^N))
  * `_buildLabelText` (Impact: 4.4 | O(N^1))
    * *Intent:* /// An icon to display as the tab's label.
  * `debugFillProperties` (Impact: 3.7 | O(2^N) | DB: 1)
    * *Intent:* /// bottom: const PreferredSize( /// preferredSize: Size.fromHeight(20.0), /// child: TabBar( /// ta...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 124`, `args: 63`, `func_start: 283`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 37`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `concurrency: 27`, `import: 19`
* *Defense:* `safety: 218`, `doc: 386`, `immutability_locks: 144`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` tab_bar_theme.dart, tab_controller.dart, dart:ui, material_localizations.dart, gestures.dart, foundation.dart, material.dart, text_theme.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/display_list/dl_builder.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.031 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.963 IQR)
- **Top Global Matches:** file_cluster_8: 14.031, file_cluster_13: 14.194, file_cluster_11: 14.286
- **Magnitude:** 3059.18 | **LOC:** 2107 | **CtrlFlow:** 73.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 48
- **Risk Profile:** Cognitive Load (76.5125%), Tech Debt (99.6201%)
**Top Internal Functions/Classes:**
  * `DisplayListBuilder::TransformFullPerspec` (Impact: 405.8 | O(N^6) | DB: 48)
  * `DisplayListBuilder::PaintResult` (Impact: 172.9 | O(N^4) | DB: 1)
  * `DisplayListBuilder::drawAtlas` (Impact: 169.8 | O(N^6) | DB: 17)
  * `DisplayListBuilder::Transform2DAffine` (Impact: 112.2 | O(N^6) | DB: 16)
    * *Intent:* // All of the above computations deferred the flooded parent status
  * `DisplayListBuilder::GetEffectiveColor` (Impact: 105.1 | O(N^6) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 347`, `structural_boundaries: 125`, `args: 72`, `func_start: 62`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 1`, `state_mutation: 981`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 58`
* *Architecture:* `import: 13`
* *Defense:* `safety: 9`, `immutability_locks: 91`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` display_list.h, dl_op_records.h, dl_blend_mode.h, dl_mask_filter.h, dl_geometry_conversions.h, logging.h, dl_op_flags.h, dl_accumulation_rect.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/text_selection.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.978 IQR)
- **Top Global Matches:** file_cluster_2: 12.978, file_cluster_13: 12.983, file_cluster_15: 13.027
- **Magnitude:** 2952.18 | **LOC:** 4020 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.0795%), Tech Debt (10.4442%)
**Top Internal Functions/Classes:**
  * `_dragStartSelection` (Impact: 2855.4 | O(2^N) | DB: 6)
  * `_getEndGlyphHeight` (Impact: 17.8 | O(N^2))
  * `startHandleRect` (Impact: 15.8 | O(2^N))
    * *Intent:* /// Builds a toolbar near a text selection. /// /// Typically displays buttons for copying and pasti...
  * `dispose` (Impact: 3.3 | O(2^N))
  * `_updateSelectionOverlay` (Impact: 3.1 | O(N^2))
    * *Intent:* /// The type for a Function that builds a toolbar's container with the given /// child. /// /// See ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 133`, `args: 82`, `func_start: 274`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 22`, `dead_code: 1`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 6`, `concurrency: 6`, `import: 27`
* *Defense:* `safety: 132`, `doc: 304`, `immutability_locks: 109`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` scheduler.dart, characters.dart, dart:async, services.dart, gestures.dart, transitions.dart, scrollable.dart, foundation.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/embedder/tests/embedder_gl_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.589 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.214 IQR)
- **Top Global Matches:** file_cluster_8: 13.589, file_cluster_7: 13.996, file_cluster_13: 14.003
- **Magnitude:** 2877.66 | **LOC:** 5380 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 107
- **Risk Profile:** Cognitive Load (80.7605%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `EmbedderTest` (Impact: 72.6 | O(N^6) | DB: 54)
  * `EmbedderTest` (Impact: 72.2 | O(N^6) | DB: 53)
  * `TEST_P` (Impact: 72.1 | O(N^6) | DB: 50)
  * `EmbedderTest` (Impact: 51.4 | O(N^6) | DB: 107)
    * *Intent:* //------------------------------------------------------------------------------ /// Test the layer ...
  * `EmbedderTest` (Impact: 45.9 | O(N^6) | DB: 17)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 239`, `args: 452`, `func_start: 64`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 2012`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 60`
* *Architecture:* `api: 2`, `concurrency: 12`, `import: 30`
* *Defense:* `doc: 40`, `test: 405`, `sync_locks: 14`, `immutability_locks: 97`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` embedder_assertions.h, embedder_surface_gl_impeller.h, embedder_unittests_util.h, embedder_test.h, raster_cache.h, message_loop_task_queues.h, message_loop.h, paths.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/selectable_region.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_15` (Drift: 13.539 IQR)
- **Top Global Matches:** file_cluster_15: 13.539, file_cluster_0: 13.592, file_cluster_13: 13.666
- **Magnitude:** 2802.5 | **LOC:** 3661 | **CtrlFlow:** 69.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (20.1107%), Tech Debt (15.0131%)
**Top Internal Functions/Classes:**
  * `dispose` (Impact: 2387.7 | O(2^N) | DB: 19)
  * `didUpdateWidget` (Impact: 58.1 | O(2^N))
  * `didChangeDependencies` (Impact: 48.0 | O(2^N))
  * `contextMenuButtonItems` (Impact: 47.8 | O(N^3) | DB: 1)
  * `_lastPointerDeviceKind` (Impact: 24.1 | O(N^2))
    * *Intent:* /// Whether the native browser context menu is enabled.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 160`, `args: 101`, `func_start: 350`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 38`, `state_mutation: 62`, `dead_code: 5`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 16`, `concurrency: 28`, `import: 25`
* *Defense:* `safety: 140`, `doc: 510`, `immutability_locks: 100`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.107
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` scheduler.dart, dart:async, text_selection.dart, platform_selectable_region_context_menu.dart, services.dart, text_editing_intents.dart, vector_math_64.dart, actions.dart...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `engine/src/flutter/impeller/entity/contents/filters/blend_filter_contents.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.283 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.376 IQR)
- **Top Global Matches:** file_cluster_8: 13.283, file_cluster_13: 13.314, file_cluster_11: 13.592
- **Magnitude:** 2659.06 | **LOC:** 1009 | **CtrlFlow:** 47.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 189
- **Risk Profile:** Cognitive Load (70.885%), Tech Debt (13.6351%)
**Top Internal Functions/Classes:**
  * `AdvancedBlend` (Impact: 2250.7 | O(2^N) | DB: 189)
  * `InvertPorterDuffBlend` (Impact: 31.1 | O(N^1))
  * `BlendModeToFilterString` (Impact: 1.9 | O(N^1))
  * `BlendFilterContents::BlendFilterContents` (Impact: 1.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 126`, `args: 56`, `func_start: 10`
* *Risk/State:* `state_mutation: 360`, `planned_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `import: 23`
* *Defense:* `safety: 27`, `doc: 4`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` texture_fill.frag.h, filter_input.h, array, texture_fill.vert.h, logging.h, vertex_buffer.h, contents.h, snapshot.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/android/platform_view_android_jni_impl.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.245 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.046 IQR)
- **Top Global Matches:** file_cluster_8: 13.245, file_cluster_13: 13.555, file_cluster_7: 13.706
- **Magnitude:** 2634.2 | **LOC:** 2412 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 159
- **Risk Profile:** Cognitive Load (93.088%), Tech Debt (97.5849%)
**Top Internal Functions/Classes:**
  * `PlatformViewAndroid::Register` (Impact: 263.3 | O(N^6) | DB: 38)
  * `PlatformViewAndroidJNIImpl::FlutterViewO` (Impact: 215.6 | O(N^6) | DB: 21)
  * `RegisterApi` (Impact: 93.6 | O(N^6) | DB: 159)
  * `LoadDartDeferredLibrary` (Impact: 87.6 | O(2^N) | DB: 12)
  * `PlatformViewAndroidJNIImpl::onDisplayPla` (Impact: 84.0 | O(N^6) | DB: 26)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 311`, `args: 136`, `func_start: 91`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 847`, `planned_debt: 7`, `duplicate_logic: 18`, `orphaned_logic: 32`
* *Architecture:* `api: 1`, `import: 22`
* *Defense:* `safety: 20`, `immutability_locks: 39`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` jni_weak_ref.h, utility, constants.h, embedded_views.h, proc_table.h, dlfcn.h, native_window_jni.h, scoped_java_ref.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/impeller/display_list/canvas.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.422 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.823 IQR)
- **Top Global Matches:** file_cluster_13: 14.422, file_cluster_8: 14.487, file_cluster_11: 14.725
- **Magnitude:** 2632.34 | **LOC:** 2392 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(N^6) | **DB Complexity:** 138
- **Risk Profile:** Cognitive Load (85.6933%), Tech Debt (97.9804%)
**Top Internal Functions/Classes:**
  * `Canvas::SetupRenderPass` (Impact: 534.3 | O(N^6) | DB: 138)
  * `Canvas::AttemptDrawBlur` (Impact: 126.7 | O(N^6) | DB: 33)
  * `Canvas::DrawImageRect` (Impact: 86.3 | O(N^6) | DB: 14)
    * *Intent:* /*reuse_depth=*/false,
  * `Canvas::DrawVertices` (Impact: 74.8 | O(N^6) | DB: 31)
    * *Intent:* /*transform=*/clip_transform, // /*global_pass_position=*/GetGlobalPassPosition(), // /*clip_depth=*...
  * `Canvas::DrawOval` (Impact: 74.7 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 222`, `structural_boundaries: 183`, `args: 162`, `func_start: 68`
* *Risk/State:* `state_mutation: 965`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 5`, `orphaned_logic: 43`
* *Architecture:* `import: 53`
* *Defense:* `safety: 40`, `doc: 20`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dl_image.h, dl_vertices_geometry.h, point_field_geometry.h, rstransform.h, utility, trace_event.h, logging.h, shadow_vertices_contents.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.43%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.03 IQR)
- **Top Global Matches:** file_cluster_13: 14.03, file_cluster_15: 14.06, file_cluster_11: 14.109
- **Magnitude:** 2514.88 | **LOC:** 317 | **CtrlFlow:** 88.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (34.6737%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import` (Impact: 2468.1 | O(N^2) | DB: 3)
  * `findScrollable` (Impact: 10.9 | O(N^2))
  * `_idLog` (Impact: 7.5 | O(N^1))
  * `SemanticsActionLogger` (Impact: 3.1 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 205`, `structural_boundaries: 27`, `args: 12`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 9`, `dead_code: 1`
* *Architecture:* `api: 4`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 126`, `doc: 17`, `test: 4`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.654
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dart:async, semantics.dart, dart:typed_data, test.dart, matchers.dart, dom.dart, ui.dart, vector_math.dart
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `dev/bots/analyze.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.005 IQR)
- **Top Global Matches:** file_cluster_4: 13.005, file_cluster_11: 13.025, file_cluster_16: 13.176
- **Magnitude:** 2412.42 | **LOC:** 2803 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 25.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 283
- **Risk Profile:** Cognitive Load (72.9971%), Tech Debt (21.161%)
**Top Internal Functions/Classes:**
  * `foundError` (Impact: 1700.4 | O(2^N) | DB: 283)
  * `verifyTargetPlatform` (Impact: 84.9 | O(N^2) | DB: 8)
  * `continue` (Impact: 45.1 | O(2^N) | DB: 7)
  * `run` (Impact: 38.4 | O(2^N) | DB: 24)
  * `result` (Impact: 28.1 | O(2^N) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 194`, `args: 58`, `func_start: 414`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 8`, `state_mutation: 183`, `dead_code: 3`, `planned_debt: 8`, `duplicate_logic: 3`
* *Architecture:* `io: 125`, `api: 5`, `concurrency: 224`, `import: 22`
* *Defense:* `safety: 88`, `doc: 29`, `test: 30`, `immutability_locks: 328`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` results.dart, meta.dart, avoid_future_catcherror.dart, utils.dart, run_command.dart, visitor.dart, path.dart, analyze.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/switch.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_17` (Drift: 13.699 IQR)
- **Top Global Matches:** file_cluster_17: 13.699, file_cluster_0: 13.782, file_cluster_15: 13.834
- **Magnitude:** 2406.64 | **LOC:** 2398 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (23.8864%), Tech Debt (13.1558%)
**Top Internal Functions/Classes:**
  * `ToggleableStateMixin` (Impact: 985.4 | O(N^4) | DB: 7)
    * *Intent:* /// * [WidgetState.hovered]. /// * [WidgetState.focused]. /// * [WidgetState.disabled]. /// /// {@to...
  * `paint` (Impact: 342.3 | O(2^N))
  * `padding` (Impact: 199.1 | O(2^N))
  * `try` (Impact: 77.4 | O(N^3))
  * `build` (Impact: 61.4 | O(N^3))
    * *Intent:* /// {@template flutter.material.switch.activeColor} /// The color to use when this switch is on. ///...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 575`, `structural_boundaries: 253`, `args: 71`, `func_start: 463`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 61`, `state_mutation: 120`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `import: 14`
* *Defense:* `safety: 327`, `doc: 121`, `immutability_locks: 175`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` switch_theme.dart, foundation.dart, material_state.dart, debug.dart, constants.dart, rendering.dart, color_scheme.dart, dart:ui...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/tab_bar_theme.dart` (DART | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.573 IQR)
- **Top Global Matches:** file_cluster_8: 14.573, file_cluster_13: 14.655, file_cluster_7: 14.705
- **Magnitude:** 2388.34 | **LOC:** 620 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.7918%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `import` (Impact: 2380.3 | O(N^5))
  * `TabBarThemeData` (Impact: 1.5 | O(N^1))
    * *Intent:* /// /// Typically a [TabBarThemeData] is specified as part of the overall [Theme] /// with [ThemeDat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 30`, `args: 6`, `func_start: 52`, `class_start: 2`
* *Risk/State:* None
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 143`, `doc: 125`, `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.103
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tabs.dart, foundation.dart, widgets.dart, ink_well.dart, theme.dart
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `engine/src/flutter/impeller/entity/entity_unittests.cc` (CPP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.865 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.221 IQR)
- **Top Global Matches:** file_cluster_8: 13.865, file_cluster_13: 13.938, file_cluster_2: 14.116
- **Magnitude:** 2338.86 | **LOC:** 2934 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (92.38%), Tech Debt (99.9721%)
**Top Internal Functions/Classes:**
  * `TEST_P` (Impact: 121.7 | O(N^6) | DB: 34)
  * `TEST_P` (Impact: 120.7 | O(N^6) | DB: 46)
  * `TEST_P` (Impact: 120.7 | O(N^6) | DB: 42)
  * `TEST_P` (Impact: 99.8 | O(N^6) | DB: 60)
  * `TEST_P` (Impact: 69.2 | O(N^6) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 331`, `args: 392`, `func_start: 80`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 1230`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 66`, `orphaned_logic: 5`
* *Architecture:* `api: 3`, `import: 54`
* *Defense:* `safety: 39`, `test: 161`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.083
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` algorithm, logging.h, point_field_geometry.h, filter_input.h, radial_gradient_contents.h, entity_playground.h, round_superellipse_geometry.h, utility...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `engine/src/flutter/lib/web_ui/lib/src/engine/occlusion_map.dart` (DART) | Magnitude: 13.34 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, func_start: 10, closures: 6
- `packages/flutter/lib/src/animation/animations.dart` (DART) | Magnitude: 117.04 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 170, doc: 121, func_start: 69, closures: 58
- `packages/flutter_tools/lib/src/convert.dart` (DART) | Magnitude: 60.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 15, func_start: 15, doc: 10
- `packages/flutter/lib/src/rendering/sliver_fixed_extent_list.dart` (DART) | Magnitude: 345.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 344, doc: 122, branch: 84, func_start: 84
- `bin/internal/shared.sh` (SHELL) | Magnitude: 162.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 119, branch: 78, io: 43, state_mutation: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `engine/src/flutter/tools/engine_tool/lib/src/commands/query_command.dart` (DART) | Magnitude: 0.13 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 128, branch: 32, func_start: 24, immutability_locks: 24
- `packages/flutter_driver/test/src/real_tests/stubs/stub_finder.dart` (DART) | Magnitude: 5.42 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 8, func_start: 5, structural_boundaries: 4, api: 2
- `dev/integration_tests/widget_preview_scaffold/lib/src/utils/url/_url_web.dart` (DART) | Magnitude: 9.5 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, branch: 9, globals: 9, func_start: 7
- `packages/flutter_tools/templates/widget_preview_scaffold/lib/src/utils/url/_url_web.dart.tmpl` (DART) | Magnitude: 9.5 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, branch: 9, globals: 9, func_start: 7
- `packages/flutter_tools/lib/src/flutter_manifest.dart` (DART) | Magnitude: 2085.1 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 762, branch: 375, func_start: 248, safety: 231

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `engine/src/flutter/tools/fuchsia/devshell/run_integration_test.sh` (SHELL) | Magnitude: 0.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 97, indent_spaces: 78, branch: 68, reflection_metaprogramming: 36
- `engine/src/flutter/ci/check_build_configs.sh` (SHELL) | Magnitude: 4.24 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 16, reflection_metaprogramming: 9, branch: 8
- `engine/src/flutter/shell/platform/darwin/common/framework/Headers/FlutterMacros.h` (CPP) | Magnitude: 16.42 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: macros: 19, reflection_metaprogramming: 11, branch: 5, doc: 2
- `engine/src/flutter/tools/find_pubspecs_to_workspacify.sh` (SHELL) | Magnitude: 0.04 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 19, branch: 15, structural_boundaries: 9
- `dev/tools/gen_keycodes/bin/gen_keycodes` (SHELL) | Magnitude: 0.02 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 14, indent_spaces: 9, reflection_metaprogramming: 7, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `packages/flutter/lib/src/services/text_input.dart` (DART) | Magnitude: 261.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 655, indent_spaces: 531, func_start: 188, structural_boundaries: 110
- `packages/flutter/lib/src/widgets/toggleable.dart` (DART) | Magnitude: 243.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 221, doc: 126, encapsulation: 95, func_start: 84
- `engine/src/flutter/display_list/effects/image_filters/dl_dilate_image_filter.cc` (CPP) | Magnitude: 97.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 21, immutability_locks: 11, structural_boundaries: 8
- `engine/src/flutter/display_list/effects/image_filters/dl_erode_image_filter.cc` (CPP) | Magnitude: 97.48 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 41, indent_spaces: 21, immutability_locks: 11, structural_boundaries: 8
- `engine/src/flutter/lib/ui/painting/gradient.cc` (CPP) | Magnitude: 215.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 82, indent_spaces: 76, branch: 13, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `engine/src/flutter/lib/web_ui/lib/src/engine/text_editing/text_editing.dart` (DART) | Magnitude: 1424.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 830, func_start: 251, doc: 240, branch: 198
- `packages/flutter/lib/src/rendering/shifted_box.dart` (DART) | Magnitude: 573.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 474, doc: 167, func_start: 160, branch: 121
- `packages/flutter_tools/lib/src/features.dart` (DART) | Magnitude: 41.84 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, doc: 24, func_start: 16, branch: 15
- `engine/src/flutter/lib/web_ui/lib/src/engine/keyboard_binding.dart` (DART) | Magnitude: 480.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 388, encapsulation: 197, func_start: 118, closures: 90
- `packages/flutter_tools/lib/src/daemon.dart` (DART) | Magnitude: 456.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 214, func_start: 87, encapsulation: 70, branch: 62

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `packages/flutter_test/lib/src/stack_manipulation.dart` (DART) | Magnitude: 24.5 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 21, doc: 9, func_start: 8, branch: 7
- `engine/src/flutter/impeller/geometry/point.h` (CPP) | Magnitude: 365.58 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 218, structural_boundaries: 196, state_mutation: 172, immutability_locks: 159
- `dev/tools/android_driver_extensions/test/src/fake_process_manager.dart` (DART) | Magnitude: 0.01 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 11, func_start: 10, generics: 7
- `packages/flutter_tools/lib/src/macos/swift_packages.dart` (DART) | Magnitude: 191.84 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 121, func_start: 43, doc: 41, immutability_locks: 37
- `packages/flutter_driver/lib/src/driver/gc_summarizer.dart` (DART) | Magnitude: 27.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, doc: 11, branch: 7, func_start: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `packages/flutter/lib/src/widgets/radio_group.dart` (DART) | Magnitude: 162.86 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 194, doc: 106, func_start: 71, generics: 61
- `bin/internal/content_aware_hash.sh` (SHELL) | Magnitude: 52.4 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: branch: 24, state_mutation: 23, indent_spaces: 18, io: 9
- `packages/flutter/lib/src/widgets/visibility.dart` (DART) | Magnitude: 127.38 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 166, indent_spaces: 142, func_start: 54, encapsulation: 29
- `packages/flutter/lib/src/material/scaffold.dart` (DART) | Magnitude: 1205.58 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1305, doc: 353, func_start: 336, encapsulation: 311
- `packages/flutter/lib/src/material/refresh_indicator.dart` (DART) | Magnitude: 587.84 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 317, encapsulation: 139, doc: 118, func_start: 97

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `packages/flutter/lib/src/cupertino/activity_indicator.dart` (DART) | Magnitude: 72.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 154, doc: 74, func_start: 57, encapsulation: 39
- `packages/flutter/lib/src/cupertino/tab_scaffold.dart` (DART) | Magnitude: 52.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, doc: 65, func_start: 32, structural_boundaries: 18
- `packages/flutter/lib/src/widgets/repeating_animation_builder.dart` (DART) | Magnitude: 37.0 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, doc: 63, func_start: 26, ui_framework: 21
- `packages/flutter/lib/src/widgets/text_selection.dart` (DART) | Magnitude: 2952.18 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1089, doc: 304, func_start: 274, encapsulation: 272
- `dev/integration_tests/widget_preview_scaffold/lib/src/utils.dart` (DART) | Magnitude: 56.18 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 142, func_start: 40, safety: 37, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/flutter_tools/lib/src/test/runner.dart` (DART) | Magnitude: 3269.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 549, state_mutation: 197, branch: 121, func_start: 111
- `dev/integration_tests/external_textures/android/app/src/main/java/io/flutter/externalui/MainActivity.java` (JAVA) | Magnitude: 194.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, structural_boundaries: 50, concurrency: 36, import: 23
- `packages/flutter_tools/lib/src/base/signals.dart` (DART) | Magnitude: 89.02 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, encapsulation: 28, structural_boundaries: 24, concurrency: 24
- `dev/tools/android_driver_extensions/test/src/fake_adb.dart` (DART) | Magnitude: 0.21 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 57, branch: 46, safety: 40, concurrency: 33
- `packages/flutter_tools/lib/src/macos/cocoapods_validator.dart` (DART) | Magnitude: 61.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 62, func_start: 22, concurrency: 15, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `engine/src/flutter/shell/platform/fuchsia/flutter/tests/fakes/scenic/fake_flatland.cc` (CPP) | Magnitude: 1149.96 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 645, state_mutation: 321, structural_boundaries: 160, branch: 83
- `packages/flutter/lib/src/widgets/preferred_size.dart` (DART) | Magnitude: 5.54 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 39, structural_boundaries: 6, indent_spaces: 6, func_start: 5
- `packages/flutter_tools/lib/src/web/web_constants.dart` (DART) | Magnitude: 12.6 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 4, globals: 2, immutability_locks: 2, indent_spaces: 2
- `engine/src/flutter/shell/platform/glfw/client_wrapper/testing/stub_flutter_glfw_api.h` (CPP) | Magnitude: 60.96 | Delta: **0.058 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 42, indent_spaces: 37, func_start: 19, api: 19
- `engine/src/flutter/ci/compatibility_helper.py` (PYTHON) | Magnitude: 7.48 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 2, structural_boundaries: 2, api: 2, doc: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `engine/src/flutter/lib/ui/semantics.dart` (DART) | Magnitude: 98.98 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 499, indent_spaces: 412, safety: 98, encapsulation: 81
- `packages/flutter/lib/src/dart_plugin_registrant.dart` (DART) | Magnitude: 12.04 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, func_start: 1, api: 1, decorators: 1
- `packages/flutter/lib/src/scheduler/debug.dart` (DART) | Magnitude: 6.9 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 59, indent_spaces: 7, func_start: 5, structural_boundaries: 4
- `engine/src/flutter/impeller/toolkit/interop/impeller.h` (CPP) | Magnitude: 18.52 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 490, indent_spaces: 68, args: 49, structural_boundaries: 20
- `dev/devicelab/bin/tasks/smoke_test_setup_failure.dart` (DART) | Magnitude: 3.52 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 9, concurrency: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterEngineTest.mm` (OBJECTIVE-C) | Magnitude: 630.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 744, state_mutation: 370, args: 218, pointers: 79
- `engine/src/flutter/shell/platform/windows/keyboard_handler_base.h` (CPP) | Magnitude: 25.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, structural_boundaries: 10, state_mutation: 9, args: 3
- `engine/src/flutter/txt/src/skia/paragraph_builder_skia.h` (CPP) | Magnitude: 15.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 3, import: 3, indent_spaces: 3, macros: 2
- `packages/flutter_tools/lib/src/template.dart` (DART) | Magnitude: 767.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 324, branch: 112, func_start: 73, immutability_locks: 64
- `packages/flutter_tools/lib/src/web/migrations/scrub_generated_plugin_registrant.dart` (DART) | Magnitude: 20.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, func_start: 16, structural_boundaries: 13, io: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `packages/flutter_tools/bin/xcode_backend.sh` (SHELL) | Magnitude: 25.08 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 15, indent_spaces: 9, reflection_metaprogramming: 7, branch: 4
- `engine/src/flutter/flow/stopwatch_dl.h` (CPP) | Magnitude: 24.92 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 23, indent_spaces: 17, state_mutation: 15, immutability_locks: 7
- `packages/flutter/lib/src/widgets/_web_browser_detection_io.dart` (DART) | Magnitude: 12.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, func_start: 1, class_start: 1
- `dev/tools/format.sh` (SHELL) | Magnitude: 0.03 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 18, indent_spaces: 11, reflection_metaprogramming: 8, structural_boundaries: 5
- `bin/internal/update_engine_version.sh` (SHELL) | Magnitude: 33.08 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 18, branch: 8, safety: 7, reflection_metaprogramming: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/flutter_tools/lib/src/runner/flutter_command.dart` -> Churn: **70.01%** | Cog Load: 15.4824% | Debt: 51.0592%
- `engine/src/flutter/impeller/entity/entity_unittests.cc` -> Churn: **65.45%** | Cog Load: 92.38% | Debt: 99.9721%
- `engine/src/flutter/testing/dart/fragment_shader_test.dart` -> Churn: **64.64%** | Cog Load: 77.3335% | Debt: 0.0%
- `packages/flutter_test/lib/src/binding.dart` -> Churn: **62.24%** | Cog Load: 12.8142% | Debt: 95.7767%
- `engine/src/flutter/impeller/display_list/aiks_dl_basic_unittests.cc` -> Churn: **59.97%** | Cog Load: 83.3409% | Debt: 99.8871%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/flutter/lib/src/rendering/editable.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 6060.02
- `packages/flutter_tools/lib/src/vmservice.dart` -> **Mohellebi Abdessalem** (100.0% isolated ownership) | Magnitude: 5218.46
- `packages/flutter/lib/src/material/app_bar_theme.dart` -> **Bruno Leroux** (100.0% isolated ownership) | Magnitude: 3463.42
- `engine/src/flutter/display_list/testing/dl_rendering_unittests.cc` -> **bungeman** (100.0% isolated ownership) | Magnitude: 3206.32
- `packages/flutter_tools/gradle/src/test/kotlin/FlutterPluginUtilsTest.kt` -> **Gray Mackall** (100.0% isolated ownership) | Magnitude: 3160.95

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `engine/src/flutter/shell/platform/android/io/flutter/embedding/android/FlutterView.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 75.6892%)
- `engine/src/flutter/shell/platform/android/io/flutter/plugin/platform/PlatformViewsController2.java` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 82.4078%)
- `engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/FlutterJNI.java` -> **Severity: 0.005** (Bridge: 0.0002 * Flux: 24.2772%)
- `engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/dart/DartExecutor.java` -> **Severity: 0.003** (Bridge: 0.0001 * Flux: 23.8321%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 0.002** (Bridge: 0.0001 * Flux: 29.9995%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `engine/src/flutter/skwasm/string.cc` -> **Severity: 1602.6** (Blast Radius: 16.026 * Doc Risk: 100.0%)
- `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart` -> **Severity: 599.011** (Blast Radius: 33.501 * Doc Risk: 17.8804%)
- `engine/src/flutter/shell/platform/android/io/flutter/Log.java` -> **Severity: 413.579** (Blast Radius: 4.136 * Doc Risk: 99.995%)
- `engine/src/flutter/shell/platform/android/io/flutter/Build.java` -> **Severity: 313.6** (Blast Radius: 3.136 * Doc Risk: 100.0%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 285.253** (Blast Radius: 19.144 * Doc Risk: 14.9004%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
