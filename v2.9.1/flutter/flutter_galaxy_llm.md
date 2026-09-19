# ARCHITECTURAL_BRIEF: flutter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/flutter/flutter` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 8661 analyzed artifact(s), 1203120 LOC.
- **Load-bearing artifact:** `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart` -- 537 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `engine/src/flutter/lib/web_ui/lib/src/engine.dart` -- pulls in 159 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/flutter/lib/src/material/theme_data.dart` at magnitude 6547.9 (structural weight, not risk).
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
| Total Artifacts | 15525 |
| Analyzed Artifacts (Scanned) | 8661 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6864 |
| Total LOC | 1203120 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 55.8% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7665 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1257 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.181 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 631 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 2894 | 368159 | 33.4% |
| DART | 2641 | 626019 | 30.5% |
| OBJECTIVE-C | 560 | 69102 | 6.5% |
| JSON | 488 | 38766 | 5.6% |
| XML | 421 | 0 | 4.9% |
| JAVA | 307 | 54120 | 3.5% |
| GLSL | 262 | 5667 | 3.0% |
| PYTHON | 212 | 20530 | 2.4% |
| MARKDOWN | 186 | 0 | 2.1% |
| YAML | 178 | 3032 | 2.1% |
| PLAINTEXT | 156 | 1 | 1.8% |
| SWIFT | 103 | 3113 | 1.2% |
| KOTLIN | 68 | 6784 | 0.8% |
| SHELL | 58 | 2043 | 0.7% |
| GROOVY | 37 | 1146 | 0.4% |
| RUBY | 22 | 756 | 0.3% |
| JAVASCRIPT | 18 | 1355 | 0.2% |
| HTML | 15 | 284 | 0.2% |
| BATCH | 14 | 358 | 0.2% |
| C | 10 | 196 | 0.1% |
| POWERSHELL | 4 | 188 | 0.0% |
| BINARY_THREAT | 2 | 2 | 0.0% |
| CSV | 1 | 1041 | 0.0% |
| TYPESCRIPT | 1 | 66 | 0.0% |
| YACC | 1 | 73 | 0.0% |
| CSS | 1 | 7 | 0.0% |
| LIVECODE | 1 | 312 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `4.321`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +4.32; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 24%, Declarative / Non-Code 18%, Large Core Modules (2) 17%, Large Core Modules (3) 10%, State Mutators Files 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8316 | 96.0% |
| Unknown | 3 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 341 | 3.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6864*

**Composition by Extension & Reason:**
- `.dart`: 3662x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 1016 LOC), 2x Excluded (Monolithic Amalgamation: 47919 LOC exceeds safe regex boundaries)
- `.png`: 614x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 222x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 81x Excluded (Unsupported Extension: '.xcworkspacedata'), 34x Excluded (Unsupported Extension: '.entitlements')
- `.tmpl`: 125x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 124x Excluded (Unsupported Extension: '.tmpl'), 13x Unsupported Format (.tmpl)
- `.md`: 249x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 5 LOC), 1x Excluded (Machine-Generated Source Code Signature: 88 LOC)
- `.xcconfig`: 156x Excluded (Unsupported Extension: '.xcconfig'), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.xcconfig)
- `.h`: 167x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 134x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 18448 hex tokens in 1647 LOC), 1x Excluded (Embedded Hex Payload: 1174 hex tokens in 1004 LOC)
- `.gni`: 71x Unsupported Format (.gni), 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gn`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 9726 LOC), 1x Excluded (Massive Static Asset Blob: 3898 LOC)
- `.yaml`: 79x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 192, Signals: 0), 1x Zero-Density Threshold (LOC: 147, Signals: 0)
- `.lockfile`: 60x Excluded (Unsupported Extension: '.lockfile'), 26x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 67x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.5 | 4.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 29.3 | 16.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 23.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 11.0 | 1.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 26.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.7 | 1.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 50.6 | 54.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 71966 | 3132 | 16 | `engine/src/flutter/shell/platform/common/text_input_model_unittests.cc` |
| cleanup | 2986 | 932 | 1 | `packages/flutter/lib/src/material/scaffold.dart` |
| guards | 186813 | 5429 | 47 | `packages/flutter/lib/src/material/icons.dart` |
| danger | 24542 | 2414 | 7 | `engine/src/flutter/lib/web_ui/test/engine/text_editing_test.dart` |
| concurrency | 24091 | 1725 | 4 | `packages/flutter_driver/test/src/real_tests/flutter_driver_test.dart` |
| connectivity | 32464 | 4479 | 9 | `engine/src/flutter/shell/platform/android/test/io/flutter/util/KeyCodes.java` |
| io | 6202 | 811 | 0 | `engine/src/flutter/testing/run_tests.py` |
| crypto | 2 | 2 | 0 | `engine/src/flutter/tools/fuchsia/copy_debug_symbols.py` |
| ipc | 393 | 111 | 0 | `engine/src/flutter/testing/android_systrace_test.py` |
| time | 979 | 373 | 0 | `engine/src/flutter/lib/web_ui/test/engine/keyboard_converter_test.dart` |
| serialization | 954 | 246 | 0 | `engine/src/flutter/shell/platform/windows/text_input_plugin_unittest.cc` |
| regex | 731 | 226 | 0 | `dev/bots/analyze.dart` |
| events | 3846 | 620 | 0 | `engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/FlutterActivityAndFragmentDelegateTest.java` |
| tests | 49623 | 997 | 3 | `engine/src/flutter/lib/web_ui/test/engine/pointer_binding_test.dart` |
| docs | 230710 | 2930 | 40 | `packages/flutter/lib/src/material/icons.dart` |
| debt | 6707 | 1443 | 2 | `engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/canvaskit_api.dart` |
| mutation | 230139 | 5913 | 63 | `packages/flutter/lib/src/material/icons.dart` |
| dead_code | 18550 | 3471 | 6 | `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm` |
| credential | 55 | 30 | 0 | `packages/flutter_tools/gradle/src/test/kotlin/tasks/BaseFlutterTaskHelperTest.kt` |
| threat | 2837 | 1705 | 1 | `packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt` |
| ml_ai | 3603 | 583 | 0 | `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart` |
| ui | 8571 | 757 | 0 | `dev/benchmarks/macrobenchmarks/lib/src/web/material3.dart` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.8333**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `engine/src/flutter/testing/run_tests.py` (Hits: 117)
- `packages/flutter_tools/lib/src/commands/build_swift_package.dart` (Hits: 89)
- `dev/bots/analyze.dart` (Hits: 85)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **memory.dart** (`engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart`) — 537 inbound connections
2. **framework.dart** (`packages/flutter/lib/src/widgets/framework.dart`) — 457 inbound connections
3. **logging.h** (`engine/src/flutter/fml/logging.h`) — 346 inbound connections
4. **macros.h** (`engine/src/flutter/fml/macros.h`) — 332 inbound connections
5. **string.cc** (`engine/src/flutter/skwasm/string.cc`) — 275 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **engine.dart** (`engine/src/flutter/lib/web_ui/lib/src/engine.dart`) — 159 outbound dependencies
2. **TextInputPluginTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/plugin/editing/TextInputPluginTest.java`) — 86 outbound dependencies
3. **FlutterViewTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/FlutterViewTest.java`) — 78 outbound dependencies
4. **FlutterView.java** (`engine/src/flutter/shell/platform/android/io/flutter/embedding/android/FlutterView.java`) — 73 outbound dependencies
5. **theme_data.dart** (`packages/flutter/lib/src/material/theme_data.dart`) — 69 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ThemeData` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/theme_data.dart`) -> Impact: **3245.7** | LOC: 427
  * *Intent:* /// a component theme parameter like [sliderTheme], [toggleButtonsTheme], /// or [bottomNavigationBarTheme]. /// /// When [useSystemColors] is true an...
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/theme_data.dart`) -> Impact: **2427.6** | LOC: 241
  * *Intent:* /// Creates a copy of this theme but with the given fields replaced with the new values. /// /// The [brightness] value is applied to the [colorScheme...
- `updateNode` **(Many-Argument Workhorses)** (@ `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart`) -> Impact: **1635.4** | LOC: 211
  * *Intent:* /// Updates one semantics node. /// /// Provides reasonable defaults for the missing attributes, and conveniences /// for specifying flags, such as [i...
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/input_decorator.dart`) -> Impact: **1369.4** | LOC: 122
  * *Intent:* /// Creates a copy of this input decoration with the given fields replaced /// by the new values.
- `compile` **(Many-Argument Workhorses)** (@ `packages/flutter_tools/lib/src/compile.dart`) -> Impact: **1333.8** | LOC: 971
- `fromImageProvider` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/color_scheme.dart`) -> Impact: **1095.8** | LOC: 165
  * *Intent:* /// /// ** See code in examples/api/lib/material/color_scheme/dynamic_content_color.0.dart ** /// /// See also: /// /// * [M3 Guidelines: Dynamic colo...
- `ColorScheme.fromSeed` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/color_scheme.dart`) -> Impact: **1095.3** | LOC: 155
  * *Intent:* /// This sample shows how to use [ColorScheme.fromSeed] to create dynamic /// color schemes with different [DynamicSchemeVariant]s and different /// c...
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/color_scheme.dart`) -> Impact: **1084.3** | LOC: 118
  * *Intent:* /// Creates a copy of this color scheme with the given fields /// replaced by the non-null parameter values.
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/date_picker_theme.dart`) -> Impact: **879.4** | LOC: 91
  * *Intent:* /// Creates a copy of this object with the given fields replaced with the /// new values.
- `TextFormField` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/text_form_field.dart`) -> Impact: **875.9** | LOC: 208
  * *Intent:* /// Creates a [FormField] that contains a [TextField]. /// /// When a [controller] is specified, [initialValue] must be null (the /// default). If [co...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/flutter/lib/src/material` | 182 | 86638.0 | 20.4% | 20.96% |
| `packages/flutter/lib/src/widgets` | 185 | 56690.88 | 17.1% | 32.61% |
| `packages/flutter/lib/src/rendering` | 48 | 26519.86 | 25.46% | 32.82% |
| `packages/flutter_tools/lib/src` | 59 | 22599.72 | 30.46% | 16.42% |
| `engine/src/flutter/shell/platform/darwin/ios/framework/Source` | 122 | 16763.79 | 16.98% | 45.08% |
| `packages/flutter_test/lib/src` | 39 | 16025.42 | 28.09% | 30.32% |
| `packages/flutter/lib/src/cupertino` | 51 | 14289.14 | 14.33% | 15.44% |
| `engine/src/flutter/shell/platform/linux` | 164 | 13730.86 | 16.98% | 37.72% |
| `packages/flutter_tools/lib/src/commands` | 52 | 12885.28 | 49.23% | 26.25% |
| `packages/flutter/lib/src/painting` | 48 | 11590.0 | 19.57% | 30.83% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `engine/src/flutter/shell/platform/darwin/common/framework/Headers/FlutterChannels.h` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/darwin/ios/framework/Headers/FlutterSceneLifeCycle.h` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterEnginePlatformViewTest.mm` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterSemanticsScrollView.mm` -> **100.0%** Exposure
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/SemanticsObjectTestMocks.h` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/internal/content_aware_hash.sh` -> **100.0%** Exposure
- `bin/internal/update_dart_sdk.sh` -> **100.0%** Exposure
- `dev/tools/repackage_gradle_wrapper.sh` -> **100.0%** Exposure
- `engine/src/flutter/bin/et` -> **100.0%** Exposure
- `engine/src/flutter/ci/analyze.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPluginTest.mm` -> **145** Orphaned Functions | **0** Duplicates
- `engine/src/flutter/lib/web_ui/test/ui/platform_view_test.dart` -> **2** Orphaned Functions | **101** Duplicates
- `engine/src/flutter/impeller/entity/contents/content_context.cc` -> **97** Orphaned Functions | **0** Duplicates
- `engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/canvaskit_api.dart` -> **0** Orphaned Functions | **97** Duplicates
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterViewControllerTest.mm` -> **94** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `36319` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/flutter/lib/src/material/theme_data.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6547.9 | **LOC:** 3490 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **69**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (41.1%), Connectivity (formerly Api Exposure) (33.9%)
- **Documentation Coverage:** 33.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThemeData` **(Many-Argument Workhorses)** (Impact: 3245.7)
    * *Intent:* /// a component theme parameter like [sliderTheme], [toggleButtonsTheme], /// or [bottomNavigationBa...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 2427.6)
    * *Intent:* /// Creates a copy of this theme but with the given fields replaced with the new values. /// /// The...
  * `operator==` **(Compute Cores)** (Impact: 125.1)
  * `_overrideWithSystemColors` **(Defensive Guards)** (Impact: 35.2)
  * `lerp` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// Linearly interpolate between two themes. ///
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 785`, `structural_boundaries: 139`, `args: 43`, `func_start: 59`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 196`, `dead_code: 5`, `planned_debt: 9`
* *Architecture:* `api: 19`, `import: 69`
* *Defense:* `safety: 563`, `doc: 805`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 59):` action_buttons.dart, action_icons_theme.dart, app_bar_theme.dart, badge_theme.dart, banner_theme.dart, bottom_app_bar_theme.dart, bottom_navigation_bar_theme.dart, bottom_sheet_theme.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/input_decorator.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 6004.36 | **LOC:** 6108 | **CtrlFlow:** 45.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Complexity Load (formerly Cognitive Load) (35.5%)
- **Documentation Coverage:** 77.5591% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 1369.4)
    * *Intent:* /// Creates a copy of this input decoration with the given fields replaced /// by the new values.
  * `InputDecorationTheme` **(Many-Argument Workhorses)** (Impact: 819.2)
    * *Intent:* /// Creates a [InputDecorationTheme] that controls visual parameters for /// descendant [InputDecora...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 694.4)
    * *Intent:* /// Creates a copy of this object but with the given fields replaced with the /// new values. /// //...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 694.4)
    * *Intent:* /// Creates a copy of this object but with the given fields replaced with the /// new values.
  * `build` **(Defensive Guards)** (Impact: 190.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1766`, `structural_boundaries: 389`, `args: 131`, `func_start: 238`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 157`, `dead_code: 20`, `planned_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `api: 34`, `import: 17`
* *Defense:* `safety: 1052`, `doc: 1634`, `immutability_locks: 59`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` button_style.dart, color_scheme.dart, colors.dart, constants.dart, dart:math, dart:ui, icon_button_theme.dart, input_border.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/color_scheme.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 5324.34 | **LOC:** 2240 | **CtrlFlow:** 52.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (62.1%), Mutation Surface (formerly State Flux) (46.6%), Complexity Load (formerly Cognitive Load) (40.9%)
- **Documentation Coverage:** 16.4384% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromImageProvider` **(Many-Argument Workhorses)** (Impact: 1095.8)
    * *Intent:* /// /// ** See code in examples/api/lib/material/color_scheme/dynamic_content_color.0.dart ** /// //...
  * `ColorScheme.fromSeed` **(Many-Argument Workhorses)** (Impact: 1095.3)
    * *Intent:* /// This sample shows how to use [ColorScheme.fromSeed] to create dynamic /// color schemes with dif...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 1084.3)
    * *Intent:* /// Creates a copy of this color scheme with the given fields /// replaced by the non-null parameter...
  * `ColorScheme` **(Many-Argument Workhorses)** (Impact: 305.2)
    * *Intent:* /// [ThemeData.useMaterial3] is false, then components will only /// use the following colors for de...
  * `ColorScheme.light` **(Many-Argument Workhorses)** (Impact: 305.2)
    * *Intent:* /// This example demonstrates how to create a color scheme similar to [ColorScheme.light] /// using ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 17 instances
* *Concurrency (weighted view):* 53
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 85`, `args: 18`, `func_start: 106`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 74`, `dead_code: 1`
* *Architecture:* `api: 14`, `concurrency: 23`, `import: 7`
* *Defense:* `safety: 624`, `doc: 454`, `sync_locks: 1`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` colors.dart, dart:async, dart:ui, foundation.dart, widgets.dart, material_color_utilities.dart, theme.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/testing/android/native_activity/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/gestures/events.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4665.68 | **LOC:** 2607 | **CtrlFlow:** 54.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (32.4%), Complexity Load (formerly Cognitive Load) (28.6%), Debt Markers (formerly Tech Debt) (16.4%)
- **Documentation Coverage:** 63.0573% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 337.6)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 335.7)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 325.8)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 325.8)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 325.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 954`, `structural_boundaries: 182`, `args: 77`, `func_start: 146`, `class_start: 51`
* *Risk/State:* `state_mutation: 31`, `dead_code: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 705`, `doc: 603`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` constants.dart, dart:ui, gesture_settings.dart, foundation.dart, vector_math_64.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_test/lib/src/matchers.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 4073.0 | **LOC:** 3312 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Complexity Load (formerly Cognitive Load) (36.0%), Guard Balance (formerly Safety Score) (32.7%), Concurrency Surface (formerly Concurrency) (31.2%)
- **Documentation Coverage:** 67.1795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_MatchesSemanticsData` **(Many-Argument Workhorses)** (Impact: 793.7)
  * `containsSemantics` **(Many-Argument Workhorses)** (Impact: 778.8)
    * *Intent:* /// validated. /// /// To find a [SemanticsNode] directly, use [CommonFinders.semantics]. /// These ...
  * `isSemantics` **(Many-Argument Workhorses)** (Impact: 778.6)
    * *Intent:* /// /// ```dart /// testWidgets('isSemantics', (WidgetTester tester) async { /// final SemanticsHand...
  * `matchesSemantics` **(Many-Argument Workhorses)** (Impact: 283.7)
    * *Intent:* /// /// ```dart /// testWidgets('matchesSemantics', (WidgetTester tester) async { /// final Semantic...
  * `matches` **(Many-Argument Workhorses)** (Impact: 152.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 349`, `args: 160`, `func_start: 167`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 157`, `duplicate_logic: 10`
* *Architecture:* `api: 32`, `concurrency: 15`, `import: 18`
* *Defense:* `safety: 517`, `doc: 717`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` _matchers_io.dart, accessibility.dart, binding.dart, controller.dart, dart:convert, dart:math, dart:ui, finders.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/semantics/semantics.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3744.06 | **LOC:** 7176 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 25.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Complexity Load (formerly Cognitive Load) (51.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.6%)
- **Documentation Coverage:** 16.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_addToUpdate` **(Defensive Guards)** (Impact: 115.2)
  * `SemanticsProperties` **(Many-Argument Workhorses)** (Impact: 112.1)
    * *Intent:* /// Creates a semantic annotation.
  * `getSemanticsData` **(I/O & Config Routines)** (Impact: 89.0)
    * *Intent:* /// Returns a summary of the semantics for this node. /// /// If this node has [mergeAllDescendantsI...
  * `absorb` **(Defensive Guards)** (Impact: 88.7)
    * *Intent:* /// Absorb the semantic information from `child` into this configuration. /// /// This adds the sema...
  * `sendSemanticsUpdate` **(Defensive Guards)** (Impact: 65.2)
    * *Intent:* /// Update the semantics using [onSemanticsUpdate].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 371 instances
* *State Mutation (weighted view):* 1335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1250`, `structural_boundaries: 528`, `args: 248`, `func_start: 411`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 125`, `state_mutation: 593`, `dead_code: 6`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 70`
* *Architecture:* `api: 60`, `import: 16`
* *Defense:* `safety: 769`, `doc: 2494`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` binding.dart, dart:core, dart:math, dart:ui, collection.dart, foundation.dart, painting.dart, services.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/editable_text.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3366.66 | **LOC:** 6793 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **49**; blast radius 0.202; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.3%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (41.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%)
- **Documentation Coverage:** 73.1884% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EditableText` **(Many-Argument Workhorses)** (Impact: 489.9)
    * *Intent:* /// Creates a basic text input control. /// /// The [maxLines] property can be set to null to remove...
  * `build` **(Defensive Guards)** (Impact: 76.8)
  * `getEditableButtonItems` **(Many-Argument Workhorses)** (Impact: 75.4)
    * *Intent:* /// For example, [EditableText] uses this to generate the default buttons for /// its context menu. ...
  * `didUpdateWidget` **(Defensive Guards)** (Impact: 69.9)
  * `_finalizeEditing` **(Many-Argument Workhorses)** (Impact: 47.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 163 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 550
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1241`, `structural_boundaries: 406`, `args: 221`, `func_start: 255`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 224`, `dead_code: 13`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 31`, `import: 50`
* *Defense:* `safety: 575`, `doc: 1641`, `immutability_locks: 51`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.202
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.001136
  * `Imports (Out-Degree: 27):` _web_browser_detection_io.dart, actions.dart, app_lifecycle_listener.dart, autofill.dart, automatic_keep_alive.dart, basic.dart, binding.dart, constants.dart...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/rendering/object.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 3310.3 | **LOC:** 6760 | **CtrlFlow:** 25.9% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (48.2%), Guard Balance (formerly Safety Score) (46.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.1%)
- **Documentation Coverage:** 28.2051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `describeSemanticsConfiguration` **(Many-Argument Workhorses)** (Impact: 138.1)
  * `computeChildGeometry` **(Many-Argument Workhorses)** (Impact: 73.2)
  * `layout` **(Defensive Guards)** (Impact: 62.2)
    * *Intent:* /// be marked as needing layout whenever the child is marked as needing layout /// because the paren...
  * `flushSemantics` **(I/O & Config Routines)** (Impact: 60.5)
    * *Intent:* /// Update the semantics for render objects marked as needing a semantics /// update. /// /// Initia...
  * `updateChildren` **(I/O & Config Routines)** (Impact: 49.8)
    * *Intent:* /// [_RenderObjectSemantics]. /// /// Gather all the merge up _RenderObjectSemantics(s) by walking t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 335`, `args: 241`, `func_start: 311`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 480`, `dead_code: 11`, `planned_debt: 16`, `duplicate_logic: 2`
* *Architecture:* `api: 68`, `import: 13`
* *Defense:* `safety: 708`, `doc: 2033`, `test: 1`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` binding.dart, dart:ui, debug.dart, layer.dart, animation.dart, foundation.dart, gestures.dart, painting.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/lib/ui/painting.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2993.16 | **LOC:** 9279 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.047; role: Isolated/Orphan
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.4%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (58.9%), Mutation Surface (formerly State Flux) (57.6%)
- **Documentation Coverage:** 47.9042% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `withValues` **(Defensive Guards)** (Impact: 64.9)
    * *Intent:* /// /// Each component ([alpha], [red], [green], [blue]) represents a /// floating-point value; see ...
  * `drawAtlas` **(Many-Argument Workhorses)** (Impact: 62.7)
  * `Vertices` **(Defensive Guards)** (Impact: 48.8)
    * *Intent:* /// entries, but may be of any length beyond this. Indicies may refer to /// offsets in the position...
  * `decodeImageFromPixels` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /// The `targetWidth` and `targetHeight` arguments specify the size of the /// output image, in imag...
  * `drawRawAtlas` **(Many-Argument Workhorses)** (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 94 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 690`, `structural_boundaries: 486`, `args: 299`, `func_start: 603`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 140`, `dead_code: 69`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 100`, `concurrency: 49`
* *Defense:* `safety: 499`, `doc: 4120`, `sync_locks: 15`, `immutability_locks: 97`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` dart:async, dart:typed_data, dart:ui
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/paragraph.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2810.36 | **LOC:** 3625 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.3%), Complexity Load (formerly Cognitive Load) (38.6%)
- **Documentation Coverage:** 64.1304% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RelayoutWhenSystemFontsChangeMixin` **(Stateful Encapsulated Methods)** (Impact: 238.4)
  * `_updateSelectionStartEdgeAtPlaceholderByMultiSelectableTextBoundary` **(Many-Argument Workhorses)** (Impact: 157.5)
    * *Intent:* // This method handles updating the start edge by a text boundary that may // not be contained withi...
  * `_updateSelectionEndEdgeAtPlaceholderByMultiSelectableTextBoundary` **(Many-Argument Workhorses)** (Impact: 157.5)
    * *Intent:* // This method handles updating the end edge by a text boundary that may // not be contained within ...
  * `_updateSelectionStartEdgeByMultiSelectableTextBoundary` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* // This method handles updating the start edge by a text boundary that may // not be contained withi...
  * `_updateSelectionEndEdgeByMultiSelectableTextBoundary` **(Many-Argument Workhorses)** (Impact: 145.5)
    * *Intent:* // This method handles updating the end edge by a text boundary that may // not be contained within ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 195 instances
* *State Mutation (weighted view):* 621
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 298`, `args: 143`, `func_start: 156`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 70`, `state_mutation: 231`, `dead_code: 5`, `planned_debt: 7`
* *Architecture:* `api: 40`, `import: 12`
* *Defense:* `safety: 260`, `doc: 239`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` box.dart, dart:math, dart:ui, debug.dart, layer.dart, layout_helper.dart, object.dart, foundation.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/widget_inspector.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2535.24 | **LOC:** 4619 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 7.601; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Concurrency Surface (formerly Concurrency) (84.7%), Complexity Load (formerly Cognitive Load) (38.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (33.2%)
- **Documentation Coverage:** 59.2798% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_getLayoutExplorerNode` **(Defensive Guards)** (Impact: 50.6)
  * `initServiceExtensions` **(Defensive Guards)** (Impact: 44.1)
    * *Intent:* /// Called to register service extensions. /// /// See also: /// /// * <https://github.com/dart-lang...
  * `_getRootWidgetTreeImpl` **(Defensive Guards)** (Impact: 43.9)
  * `screenshot` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* /// Captures an image of the current state of an [object] that is a /// [RenderObject] or [Element]....
  * `_hitTestHelper` **(Many-Argument Workhorses)** (Impact: 39.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 173 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 150
* *State Mutation (weighted view):* 579
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 350`, `args: 260`, `func_start: 294`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 86`, `high_risk_execution: 2`, `state_mutation: 233`, `dead_code: 10`, `planned_debt: 8`, `duplicate_logic: 4`
* *Architecture:* `io: 4`, `api: 85`, `concurrency: 65`, `import: 19`
* *Defense:* `safety: 550`, `doc: 740`, `immutability_locks: 51`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.601
  * `Choke Point (Betweenness):` 0.000278 | `Ripple Effect (Closeness):` 0.028894
  * `Imports (Out-Degree: 4):` basic.dart, binding.dart, dart:async, dart:collection, dart:convert, dart:developer, dart:math, dart:ui...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/widgets/navigator.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2526.5 | **LOC:** 6451 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Complexity Load (formerly Cognitive Load) (26.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.6%), Concurrency Surface (formerly Concurrency) (22.2%)
- **Documentation Coverage:** 49.481% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_flushHistoryUpdates` **(Defensive Guards)** (Impact: 110.3)
  * `_updatePages` **(I/O & Config Routines)** (Impact: 66.5)
  * `resolve` **(Many-Argument Workhorses)** (Impact: 47.2)
  * `update` **(Defensive Guards)** (Impact: 45.9)
    * *Intent:* // Updating.
  * `handlePush` **(Defensive Guards)** (Impact: 43.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 203 instances
* *State Mutation (weighted view):* 662
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 798`, `structural_boundaries: 340`, `args: 218`, `func_start: 276`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 146`, `state_mutation: 256`, `dead_code: 61`, `planned_debt: 7`
* *Architecture:* `io: 1`, `api: 35`, `concurrency: 35`, `import: 22`
* *Defense:* `safety: 688`, `doc: 2651`, `sync_locks: 4`, `immutability_locks: 30`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` basic.dart, binding.dart, dart:async, dart:collection, dart:convert, dart:developer, dart:ui, focus_manager.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/proxy_box.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2496.96 | **LOC:** 4820 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 0.16; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Debt Markers (formerly Tech Debt) (97.1%), Guard Balance (formerly Safety Score) (43.7%), Connectivity (formerly Api Exposure) (23.9%)
- **Documentation Coverage:** 50.7009% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `paint` **(Defensive Guards)** (Impact: 26.5)
  * `RenderBackdropFilter` **(Defensive Guards)** (Impact: 24.8)
    * *Intent:* /// Creates a backdrop filter. /// /// Exactly one of [filter] or [filterConfig] must be provided. /...
  * `paint` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `paint` **(Defensive Guards)** (Impact: 20.2)
  * `handleEvent` **(Defensive Guards)** (Impact: 19.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 183 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 618
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 424`, `args: 329`, `func_start: 426`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 122`, `high_risk_execution: 1`, `state_mutation: 252`, `dead_code: 16`, `planned_debt: 2`, `duplicate_logic: 51`
* *Architecture:* `api: 69`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 449`, `doc: 1122`, `immutability_locks: 15`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.16
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000481
  * `Imports (Out-Degree: 3):` binding.dart, box.dart, dart:ui, image_filter_config.dart, layer.dart, layout_helper.dart, object.dart, animation.dart...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/widgets/framework.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2376.9 | **LOC:** 7456 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **457** in-repo importer(s); it depends on **10**; blast radius 37.3; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Complexity Load (formerly Cognitive Load) (34.0%), Concurrency Surface (formerly Concurrency) (26.9%), Debt Markers (formerly Tech Debt) (26.9%)
- **Documentation Coverage:** 39.4813% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateChildren` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* /// Using the previous sibling as a [slot] is not enough, though, because /// child [RenderObject]s ...
  * `updateChild` **(Many-Argument Workhorses)** (Impact: 56.9)
    * *Intent:* /// /// | | **newWidget == null** | **newWidget != null** | /// | :-----------------: | :-----------...
  * `finalizeTree` **(Defensive Guards)** (Impact: 41.4)
    * *Intent:* /// Complete the element build pass by unmounting any elements that are no /// longer active. /// //...
  * `size` **(I/O & Config Routines)** (Impact: 33.2)
  * `inflateWidget` **(Defensive Guards)** (Impact: 30.3)
    * *Intent:* /// /// This method is typically called by [updateChild] but can be called /// directly by subclasse...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 191 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 654
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 688`, `structural_boundaries: 333`, `args: 241`, `func_start: 331`, `class_start: 44`
* *Risk/State:* `safety_bypasses: 72`, `state_mutation: 272`, `dead_code: 73`, `planned_debt: 14`, `fragile_debt: 1`, `duplicate_logic: 10`
* *Architecture:* `api: 53`, `concurrency: 19`, `import: 16`
* *Defense:* `safety: 752`, `doc: 3388`, `test: 1`, `sync_locks: 1`, `immutability_locks: 24`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 37.3
  * `Choke Point (Betweenness):` 0.000458 | `Ripple Effect (Closeness):` 0.038166
  * `Imports (Out-Degree: 4):` binding.dart, dart:async, dart:collection, debug.dart, focus_manager.dart, inherited_model.dart, notification_listener.dart, foundation.dart...
  * `Imported By (In-Degree: 457):` (Excluded from Brief to save tokens)

### `packages/flutter_tools/lib/src/compile.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2346.58 | **LOC:** 1220 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.7%)
- **Documentation Coverage:** 64.1026% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compile` **(Many-Argument Workhorses)** (Impact: 1333.8)
  * `_compile` **(Many-Argument Workhorses)** (Impact: 92.4)
  * `recompile` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `compileExpression` **(Many-Argument Workhorses)** (Impact: 41.5)
  * `_recompile` **(Defensive Guards)** (Impact: 39.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 23 instances
* *Amplified Cascading Flux:* 87 instances
* *Concurrency (weighted view):* 200
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 310`, `structural_boundaries: 104`, `args: 40`, `func_start: 56`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 99`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 7`, `api: 15`, `concurrency: 85`, `import: 19`
* *Defense:* `safety: 217`, `doc: 74`, `sync_locks: 26`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` artifacts.dart, common.dart, config.dart, context.dart, file_system.dart, io.dart, logger.dart, platform.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/basic.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2314.94 | **LOC:** 8574 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **99** in-repo importer(s); it depends on **14**; blast radius 5.447; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.1%), Mutation Surface (formerly State Flux) (64.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.5%)
- **Documentation Coverage:** 41.5698% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_SemanticsBase` **(Many-Argument Workhorses)** (Impact: 764.7)
    * *Intent:* /// /// To create a `const` instance of [_SemanticsBase], use the /// [_SemanticsBase.fromProperties...
  * `Transform.scale` **(Defensive Guards)** (Impact: 54.7)
    * *Intent:* /// scale: 0.5, /// child: Container( /// padding: const EdgeInsets.all(8.0), /// color: const Color...
  * `Positioned.directional` **(Defensive Guards)** (Impact: 36.1)
    * *Intent:* /// Only two out of the three horizontal values (`start`, `end`, /// [width]), and only two out of t...
  * `RichText` **(Many-Argument Workhorses)** (Impact: 21.7)
    * *Intent:* /// Creates a paragraph of rich text. /// /// The [maxLines] property may be null (and indeed defaul...
  * `_getTextDirection` **(Stateful Encapsulated Methods)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 41 instances
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 392`, `structural_boundaries: 239`, `args: 263`, `func_start: 320`, `class_start: 81`
* *Risk/State:* `safety_bypasses: 5`, `high_risk_execution: 1`, `state_mutation: 186`, `dead_code: 41`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 6`
* *Architecture:* `api: 103`, `import: 18`
* *Defense:* `safety: 457`, `doc: 4937`, `immutability_locks: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.447
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.024356
  * `Imports (Out-Degree: 4):` binding.dart, dart:math, dart:ui, debug.dart, framework.dart, localizations.dart, animation.dart, foundation.dart...
  * `Imported By (In-Degree: 99):` (Excluded from Brief to save tokens)

### `engine/src/flutter/lib/web_ui/lib/src/engine/dom.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2309.6 | **LOC:** 2720 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **73** in-repo importer(s); it depends on **7**; blast radius 6.081; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Concurrency Surface (formerly Concurrency) (62.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.2%)
- **Documentation Coverage:** 91.0959% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawImage` **(Many-Argument Workhorses)** (Impact: 42.7)
  * `DomLocaleOptions` **(Defensive Guards)** (Impact: 32.2)
  * `observe` **(Defensive Guards)** (Impact: 16.1)
  * `createImageBitmap` **(Defensive Guards)** (Impact: 14.6)
  * `initEvent` **(Defensive Guards)** (Impact: 14.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 16 instances
* *Concurrency (weighted view):* 65
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 487`, `structural_boundaries: 496`, `args: 221`, `func_start: 789`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 20`, `dead_code: 2`, `planned_debt: 7`, `duplicate_logic: 90`
* *Architecture:* `io: 2`, `api: 383`, `concurrency: 60`, `import: 7`
* *Defense:* `safety: 405`, `doc: 250`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.022006
  * `Imports (Out-Degree: 0):` browser_detection.dart, dart:async, dart:js_interop, dart:js_interop_unsafe, dart:math, dart:typed_data, meta.dart
  * `Imported By (In-Degree: 73):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/material/menu_anchor.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2035.7 | **LOC:** 4263 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **30**; blast radius 0.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.1%), Debt Markers (formerly Tech Debt) (55.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (42.3%), Complexity Load (formerly Cognitive Load) (31.6%)
- **Documentation Coverage:** 75.6098% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `styleFrom` **(Many-Argument Workhorses)** (Impact: 143.1)
    * *Intent:* /// [MenuItemButton], as well as its overlay color, with all of the standard /// opacity adjustments...
  * `styleFrom` **(Many-Argument Workhorses)** (Impact: 143.1)
    * *Intent:* /// /// For example, to override the default foreground color for a /// [SubmenuButton], as well as ...
  * `build` **(Defensive Guards)** (Impact: 126.1)
  * `_getModifierLabel` **(Compute Cores)** (Impact: 74.3)
  * `build` **(Defensive Guards)** (Impact: 69.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 113 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 358
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 766`, `structural_boundaries: 299`, `args: 148`, `func_start: 205`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 132`, `dead_code: 8`, `planned_debt: 2`, `duplicate_logic: 18`
* *Architecture:* `api: 18`, `concurrency: 3`, `import: 30`
* *Defense:* `safety: 500`, `doc: 1075`, `immutability_locks: 55`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.141
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.000671
  * `Imports (Out-Degree: 11):` button_style.dart, button_style_button.dart, checkbox.dart, color_scheme.dart, colors.dart, constants.dart, dart:async, dart:math...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/material/date_picker.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2002.64 | **LOC:** 3492 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **28**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.9%), Complexity Load (formerly Cognitive Load) (32.4%), Debt Markers (formerly Tech Debt) (28.9%), Guard Balance (formerly Safety Score) (18.0%)
- **Documentation Coverage:** 75.3968% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `showDateRangePicker` **(Many-Argument Workhorses)** (Impact: 226.7)
    * *Intent:* /// This is accomplished by enabling state restoration by specifying /// [MaterialApp.restorationSco...
  * `showDatePicker` **(Many-Argument Workhorses)** (Impact: 185.9)
    * *Intent:* /// push [DatePickerDialog] when the button is tapped. /// /// ** See code in examples/api/lib/mater...
  * `build` **(Defensive Guards)** (Impact: 117.6)
  * `build` **(Defensive Guards)** (Impact: 99.0)
  * `build` **(Defensive Guards)** (Impact: 96.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 125 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 390
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 180`, `args: 138`, `func_start: 140`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 140`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 6`, `unreferenced_by_name: 11`
* *Architecture:* `api: 5`, `concurrency: 4`, `import: 28`
* *Defense:* `safety: 529`, `doc: 564`, `immutability_locks: 84`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` app_bar.dart, back_button.dart, button_style.dart, calendar_date_picker.dart, color_scheme.dart, dart:math, date.dart, date_picker_theme.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/editable.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1963.64 | **LOC:** 3157 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (73.0%), Guard Balance (formerly Safety Score) (46.0%)
- **Documentation Coverage:** 43.7768% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RenderEditable` **(Many-Argument Workhorses)** (Impact: 264.6)
    * *Intent:* /// Creates a render object that implements the visual aspects of a text field. /// /// The [textAli...
  * `assembleSemanticsNode` **(Many-Argument Workhorses)** (Impact: 73.4)
  * `calculateBoundedFloatingCursorOffset` **(Many-Argument Workhorses)** (Impact: 46.5)
    * *Intent:* /// Returns the position within the text field closest to the raw cursor offset. /// /// See also: /...
  * `describeSemanticsConfiguration` **(Defensive Guards)** (Impact: 35.1)
  * `getWordAtOffset` **(Compute Cores)** (Impact: 34.1)
    * *Intent:* /// Returns a [TextSelection] that encompasses the word at the given /// [TextPosition].
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 520
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 262`, `args: 162`, `func_start: 233`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 208`, `dead_code: 2`, `planned_debt: 9`, `duplicate_logic: 2`, `unreferenced_by_name: 41`
* *Architecture:* `api: 4`, `import: 14`
* *Defense:* `safety: 303`, `doc: 537`, `immutability_locks: 9`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` box.dart, custom_paint.dart, dart:math, dart:ui, layer.dart, layout_helper.dart, object.dart, characters.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/selectable_region.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1924.96 | **LOC:** 3661 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 0.06; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (44.2%)
- **Documentation Coverage:** 60.1036% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_startNewMouseSelectionGesture` **(Compute Cores)** (Impact: 57.3)
  * `_adjustSelection` **(Defensive Guards)** (Impact: 56.4)
    * *Intent:* /// Adjusts the selection based on the drag selection update event if there /// is already a selecta...
  * `_handleMouseDragUpdate` **(Compute Cores)** (Impact: 49.3)
  * `_handleMouseTapUp` **(Compute Cores)** (Impact: 45.4)
  * `_initSelection` **(Defensive Guards)** (Impact: 38.7)
    * *Intent:* /// Initializes the selection of the selectable children. /// /// The goal is to find the selectable...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 182 instances
* *Concurrency (weighted view):* 34
* *State Mutation (weighted view):* 597
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 666`, `structural_boundaries: 235`, `args: 161`, `func_start: 178`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 233`, `dead_code: 6`, `planned_debt: 6`
* *Architecture:* `api: 24`, `concurrency: 14`, `import: 25`
* *Defense:* `safety: 246`, `doc: 707`, `immutability_locks: 16`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.06
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.000346
  * `Imports (Out-Degree: 12):` actions.dart, basic.dart, context_menu_button_item.dart, dart:async, dart:math, debug.dart, focus_manager.dart, focus_scope.dart...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPlugin.mm` (OBJECTIVE-C | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1915.92 | **LOC:** 3310 | **CtrlFlow:** 19.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.047; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (84.7%), Guard Balance (formerly Safety Score) (82.0%), Complexity Load (formerly Cognitive Load) (73.2%)
- **Documentation Coverage:** 98.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleMethodCall` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `editMenuInteraction` **(Many-Argument Workhorses)** (Impact: 56.1)
  * `firstRectForRange` **(Compute Cores)** (Impact: 52.4)
    * *Intent:* // The following methods are required to support force-touch cursor positioning // and to position t...
  * `IsSelectionRectBoundaryCloserToPoint` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* // this means the right-center point. // // If useTrailingBoundaryOfSelectionRect is set, the traili...
  * `ToUITextContentType` **(I/O & Config Routines)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 473`, `structural_boundaries: 274`, `args: 131`, `func_start: 185`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 255`, `dead_code: 3`, `planned_debt: 17`, `fragile_debt: 4`, `unreferenced_by_name: 53`
* *Architecture:* `io: 1`, `api: 165`, `concurrency: 1`, `import: 9`
* *Defense:* `safety: 21`, `doc: 3`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.047
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Foundation.h, UIKit.h, logging.h, string_range_sanitization.h, InternalFlutterSwiftCommon.h, FlutterSharedApplication.h, FlutterTextInputPlugin.h, UIViewController+FlutterScreenAndSceneIfLoaded.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `engine/src/flutter/shell/platform/android/io/flutter/view/AccessibilityBridge.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1909.2 | **LOC:** 3260 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 30.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **43**; blast radius 0.356; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.6%), Complexity Load (formerly Cognitive Load) (77.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.5%)
- **Documentation Coverage:** 50.7576% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createAccessibilityNodeInfo` **(Many-Argument Workhorses)** (Impact: 203.9)
    * *Intent:* * represented by {@link #flutterSemanticsTree}, is searched for a {@link SemanticsNode} with the * g...
  * `performAction` **(Many-Argument Workhorses)** (Impact: 130.4)
    * *Intent:* /** * Instructs the view represented by {@code virtualViewId} to carry out the desired {@code * acce...
  * `updateSemantics` **(Many-Argument Workhorses)** (Impact: 106.7)
    * *Intent:* /** * Updates {@link #flutterSemanticsTree} to reflect the latest state of Flutter's semantics tree....
  * `predictCursorMovement` **(Many-Argument Workhorses)** (Impact: 86.1)
  * `performCursorMoveAction` **(Many-Argument Workhorses)** (Impact: 45.6)
    * *Intent:* /** * Handles the responsibilities of {@link #performAction(int, int, Bundle)} for the specific * sc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 210 instances
* *State Mutation (weighted view):* 755
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 471`, `structural_boundaries: 297`, `args: 100`, `func_start: 98`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 335`, `dead_code: 3`, `planned_debt: 16`, `fragile_debt: 2`
* *Architecture:* `api: 39`, `import: 42`
* *Defense:* `safety: 57`, `doc: 45`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.356
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.006912
  * `Imports (Out-Degree: 6):` android.annotation.SuppressLint, android.app.Activity, android.content.ContentResolver, android.content.Context, android.content.res.Configuration, android.database.ContentObserver, android.graphics.Rect, android.net.Uri...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `engine/src/flutter/lib/web_ui/lib/src/engine/canvaskit/canvaskit_api.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1886.66 | **LOC:** 2490 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **8**; blast radius 0.992; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (82.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (37.1%)
- **Documentation Coverage:** 92.4731% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MakeVertices` **(Defensive Guards)** (Impact: 17.5)
  * `saveLayer` **(Defensive Guards)** (Impact: 15.0)
  * `_saveLayer` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `MakeTwoPointConicalGradient` **(Many-Argument Workhorses)** (Impact: 10.5)
  * `MakeSweepGradient` **(Many-Argument Workhorses)** (Impact: 10.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 308`, `args: 146`, `func_start: 702`, `class_start: 124`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 48`, `planned_debt: 6`, `duplicate_logic: 97`
* *Architecture:* `api: 355`, `concurrency: 11`, `import: 8`
* *Defense:* `safety: 213`, `doc: 140`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.992
  * `Choke Point (Betweenness):` 3.3e-05 | `Ripple Effect (Closeness):` 0.016379
  * `Imports (Out-Degree: 1):` dart:async, dart:convert, dart:js_interop, dart:js_interop_unsafe, dart:typed_data, meta.dart, engine.dart, ui.dart
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `packages/flutter_tools/lib/src/commands/run.dart` -> Churn: **73.92%** | Cog Load: 94.8904% | Debt: 0.0%
- `engine/src/flutter/shell/platform/android/io/flutter/view/AccessibilityBridge.java` -> Churn: **65.45%** | Cog Load: 76.994% | Debt: 11.7483%
- `engine/src/flutter/testing/dart/fragment_shader_test.dart` -> Churn: **64.64%** | Cog Load: 95.4274% | Debt: 0.0%
- `packages/flutter_test/lib/src/binding.dart` -> Churn: **62.24%** | Cog Load: 43.9416% | Debt: 99.3138%
- `engine/src/flutter/impeller/entity/contents/content_context.cc` -> Churn: **59.97%** | Cog Load: 52.4245% | Debt: 99.1042%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/flutter/lib/src/material/color_scheme.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 5324.34
- `packages/flutter/lib/src/gestures/events.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 4665.68
- `packages/flutter/lib/src/rendering/editable.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 1963.64
- `packages/flutter/lib/src/widgets/selectable_region.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 1924.96
- `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterTextInputPlugin.mm` -> **Koji Wakamiya** (100.0% isolated ownership) | Magnitude: 1915.92

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `packages/flutter_tools/lib/src/base/process.dart` -> **Severity: 0.049** (Bridge: 0.0006 * Flux: 81.1052%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 0.046** (Bridge: 0.0005 * Flux: 99.4501%)
- `packages/flutter_tools/lib/src/build_system/build_system.dart` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 92.9335%)
- `packages/flutter/lib/src/widgets/async.dart` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 99.1977%)
- `packages/flutter/lib/src/widgets/widget_inspector.dart` -> **Severity: 0.027** (Bridge: 0.0003 * Flux: 98.9053%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `engine/src/flutter/skwasm/string.cc` -> **Severity: 6.863** (Embedded: 0.1032 * Error Risk: 66.5013%)
- `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart` -> **Severity: 6.785** (Embedded: 0.1312 * Error Risk: 51.7136%)
- `engine/src/flutter/impeller/geometry/scalar.h` -> **Severity: 3.903** (Embedded: 0.0532 * Error Risk: 73.3123%)
- `engine/src/flutter/fml/memory/ref_ptr.h` -> **Severity: 3.252** (Embedded: 0.0473 * Error Risk: 68.691%)
- `engine/src/flutter/fml/closure.h` -> **Severity: 2.987** (Embedded: 0.0426 * Error Risk: 70.2063%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 1472.652** (Blast Radius: 37.3 * Doc Risk: 39.4813%)
- `engine/src/flutter/skwasm/string.cc` -> **Severity: 1472.0** (Blast Radius: 14.72 * Doc Risk: 100.0%)
- `engine/src/flutter/lib/web_ui/lib/src/engine/skwasm/skwasm_impl/memory.dart` -> **Severity: 1182.8** (Blast Radius: 14.785 * Doc Risk: 80.0%)
- `packages/flutter/test_fixes/widgets/widgets.dart` -> **Severity: 1030.1** (Blast Radius: 10.301 * Doc Risk: 100.0%)
- `engine/src/flutter/fml/logging.h` -> **Severity: 1014.9** (Blast Radius: 10.149 * Doc Risk: 100.0%)

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
