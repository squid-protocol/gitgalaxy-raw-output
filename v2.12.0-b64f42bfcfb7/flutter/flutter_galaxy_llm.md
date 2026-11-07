# ARCHITECTURAL_BRIEF: flutter
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/flutter/flutter` |
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
- **Scope:** 12038 analyzed artifact(s), 2104187 LOC.
- **Load-bearing artifact:** `packages/flutter/lib/material.dart` -- 1858 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `packages/flutter/lib/material.dart` -- pulls in 182 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` at magnitude 19184.04 (structural weight, not risk).
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
| Total Artifacts | 15526 |
| Analyzed Artifacts (Scanned) | 12038 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 3488 |
| Total LOC | 2104187 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 77.5% |
| Dominant Lang | DART |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6718 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1475 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.9269 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 559 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| DART | 5636 | 1504811 | 46.8% |
| CPP | 2926 | 370949 | 24.3% |
| JSON | 575 | 47616 | 4.8% |
| OBJECTIVE-C | 546 | 69197 | 4.5% |
| XML | 438 | 0 | 3.6% |
| JAVA | 308 | 54685 | 2.6% |
| YAML | 265 | 9305 | 2.2% |
| GLSL | 262 | 5667 | 2.2% |
| MARKDOWN | 223 | 0 | 1.9% |
| PYTHON | 211 | 20241 | 1.8% |
| PLAINTEXT | 196 | 1 | 1.6% |
| SWIFT | 108 | 3206 | 0.9% |
| GROOVY | 104 | 3367 | 0.9% |
| KOTLIN | 81 | 7185 | 0.7% |
| SHELL | 64 | 2247 | 0.5% |
| RUBY | 28 | 900 | 0.2% |
| JAVASCRIPT | 18 | 1335 | 0.1% |
| HTML | 16 | 301 | 0.1% |
| BATCH | 14 | 358 | 0.1% |
| C | 10 | 196 | 0.1% |
| POWERSHELL | 4 | 188 | 0.0% |
| LIVECODE | 2 | 1318 | 0.0% |
| CSV | 1 | 1041 | 0.0% |
| TYPESCRIPT | 1 | 66 | 0.0% |
| CSS | 1 | 7 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 12037 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 21%, Declarative / Non-Code 14%, Large Core Modules (2) 13%, State Mutators Files 10%, Interface Declarations Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 11618 | 96.5% |
| Unknown | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 418 | 3.5% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 3488*

**Composition by Extension & Reason:**
- `.dart`: 676x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Excluded (Machine-Generated Source Code Signature: 1016 LOC), 2x Excluded (Machine-Generated Source Code Signature: 3286 LOC)
- `.png`: 614x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 204x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 85x Excluded (Unsupported Extension: '.xcworkspacedata'), 36x Unsupported Format (.undeterminable)
- `.tmpl`: 159x Excluded (Unsupported Extension: '.tmpl'), 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 13x Unsupported Format (.tmpl)
- `.md`: 214x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xcconfig`: 166x Excluded (Unsupported Extension: '.xcconfig'), 1x Unsupported Format (.xcconfig)
- `.h`: 159x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cc`: 147x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gni`: 71x Unsupported Format (.gni), 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gn`: 97x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lockfile`: 86x Excluded (Unsupported Extension: '.lockfile')
- `.txt`: 76x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.pbxproj`: 51x Excluded (Unsupported Extension: '.pbxproj'), 4x Unsupported Format (.pbxproj)
- `.xcscheme`: 50x Excluded (Unsupported Extension: '.xcscheme'), 2x Unsupported Format (.xcscheme)
- `.py`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.8 | 2.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.2 | 27.6 | 36.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 10.2 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 23.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 18.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.5 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.2 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.5 | 85.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 24150 | 2678 | 3 | `engine/src/flutter/shell/platform/darwin/ios/framework/Source/FlutterPlatformViewsTest.mm` |
| cleanup | 5689 | 1513 | 1 | `dev/integration_tests/flutter_gallery/test/accessibility_test.dart` |
| guards | 277688 | 8191 | 48 | `packages/flutter/lib/src/material/icons.dart` |
| danger | 35314 | 3527 | 6 | `engine/src/flutter/lib/web_ui/test/engine/text_editing_test.dart` |
| concurrency | 112816 | 3566 | 13 | `packages/flutter/test/material/text_field_test.dart` |
| connectivity | 42215 | 7499 | 7 | `dev/integration_tests/new_gallery/lib/gallery_localizations.dart` |
| io | 6300 | 930 | 0 | `engine/src/flutter/testing/run_tests.py` |
| crypto | 2 | 2 | 0 | `engine/src/flutter/tools/fuchsia/copy_debug_symbols.py` |
| ipc | 450 | 138 | 0 | `engine/src/flutter/testing/android_systrace_test.py` |
| time | 7343 | 1028 | 0 | `packages/flutter/test/gestures/velocity_tracker_data.dart` |
| serialization | 1107 | 288 | 0 | `engine/src/flutter/shell/platform/windows/text_input_plugin_unittest.cc` |
| regex | 701 | 234 | 0 | `packages/flutter_tools/test/integration.shard/test_test.dart` |
| events | 4457 | 752 | 0 | `engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/FlutterActivityAndFragmentDelegateTest.java` |
| tests | 220324 | 3015 | 25 | `packages/flutter/test/material/input_decorator_test.dart` |
| docs | 231400 | 3589 | 18 | `packages/flutter/lib/src/material/icons.dart` |
| debt | 62483 | 2703 | 4 | `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` |
| mutation | 344869 | 8380 | 61 | `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` |
| dead_code | 26375 | 5696 | 5 | `engine/src/flutter/display_list/display_list_unittests.cc` |
| credential | 174 | 37 | 0 | `dev/integration_tests/wide_gamut_test/lib/main.dart` |
| threat | 1931 | 64 | 0 | `dev/benchmarks/macrobenchmarks/lib/src/fullscreen_textfield.dart` |
| ml_ai | 4668 | 803 | 0 | `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_test.dart` |
| ui | 52127 | 2575 | 9 | `packages/flutter/test/material/menu_anchor_test.dart` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `engine/src/flutter/testing/run_tests.py` (Hits: 117)
- `packages/flutter_tools/test/commands.shard/hermetic/build_swift_package_test.dart` (Hits: 90)
- `dev/bots/analyze.dart` (Hits: 85)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **material.dart** (`packages/flutter/lib/material.dart`) — 1858 inbound connections
2. **flutter_test.dart** (`packages/flutter_test/lib/flutter_test.dart`) — 1805 inbound connections
3. **foundation.dart** (`packages/flutter/lib/foundation.dart`) — 910 inbound connections
4. **widgets.dart** (`packages/flutter/lib/widgets.dart`) — 739 inbound connections
5. **rendering.dart** (`packages/flutter/lib/rendering.dart`) — 665 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **material.dart** (`packages/flutter/lib/material.dart`) — 182 outbound dependencies
2. **widgets.dart** (`packages/flutter/lib/widgets.dart`) — 173 outbound dependencies
3. **engine.dart** (`engine/src/flutter/lib/web_ui/lib/src/engine.dart`) — 159 outbound dependencies
4. **TextInputPluginTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/plugin/editing/TextInputPluginTest.java`) — 86 outbound dependencies
5. **FlutterViewTest.java** (`engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/FlutterViewTest.java`) — 78 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `ThemeData` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/theme_data.dart`) -> Impact: **2358.5** | LOC: 427
  * *Intent:* /// a component theme parameter like [sliderTheme], [toggleButtonsTheme], /// or [bottomNavigationBarTheme]. /// /// When [useSystemColors] is true an...
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/theme_data.dart`) -> Impact: **1662.3** | LOC: 241
  * *Intent:* /// Creates a copy of this theme but with the given fields replaced with the new values. /// /// The [brightness] value is applied to the [colorScheme...
- `updateNode` **(Many-Argument Workhorses)** (@ `engine/src/flutter/lib/web_ui/test/engine/semantics/semantics_tester.dart`) -> Impact: **1196.7** | LOC: 211
  * *Intent:* /// Updates one semantics node. /// /// Provides reasonable defaults for the missing attributes, and conveniences /// for specifying flags, such as [i...
- `copyWith` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/input_decorator.dart`) -> Impact: **920.1** | LOC: 122
  * *Intent:* /// Creates a copy of this input decoration with the given fields replaced /// by the new values.
- `_MatchesSemanticsData` **(Many-Argument Workhorses)** (@ `packages/flutter_test/lib/src/matchers.dart`) -> Impact: **793.7** | LOC: 118
- `containsSemantics` **(Many-Argument Workhorses)** (@ `packages/flutter_test/lib/src/matchers.dart`) -> Impact: **778.8** | LOC: 179
  * *Intent:* /// validated. /// /// To find a [SemanticsNode] directly, use [CommonFinders.semantics]. /// These methods will search the semantics tree directly an...
- `isSemantics` **(Many-Argument Workhorses)** (@ `packages/flutter_test/lib/src/matchers.dart`) -> Impact: **778.6** | LOC: 175
  * *Intent:* /// /// ```dart /// testWidgets('isSemantics', (WidgetTester tester) async { /// final SemanticsHandle handle = tester.ensureSemantics(); /// // ... /...
- `_SemanticsBase` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/widgets/basic.dart`) -> Impact: **764.7** | LOC: 174
  * *Intent:* /// /// To create a `const` instance of [_SemanticsBase], use the /// [_SemanticsBase.fromProperties] constructor. /// /// See also: /// /// * [Semant...
- `TextFormField` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/text_form_field.dart`) -> Impact: **761.1** | LOC: 208
  * *Intent:* /// Creates a [FormField] that contains a [TextField]. /// /// When a [controller] is specified, [initialValue] must be null (the /// default). If [co...
- `fromImageProvider` **(Many-Argument Workhorses)** (@ `packages/flutter/lib/src/material/color_scheme.dart`) -> Impact: **735.7** | LOC: 165
  * *Intent:* /// /// ** See code in examples/api/lib/material/color_scheme/dynamic_content_color.0.dart ** /// /// See also: /// /// * [M3 Guidelines: Dynamic colo...

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `packages/flutter/test/material` | 192 | 122077.76 | 19.58% | 0.0% |
| `packages/flutter/test/widgets` | 407 | 108943.1 | 16.03% | 0.0% |
| `packages/flutter/lib/src/material` | 182 | 75248.1 | 18.55% | 13.43% |
| `packages/flutter/lib/src/widgets` | 185 | 54241.98 | 16.27% | 12.27% |
| `packages/flutter_localizations/lib/src/l10n` | 352 | 36246.44 | 0.04% | 0.85% |
| `packages/flutter/test/cupertino` | 55 | 26786.56 | 22.57% | 0.0% |
| `packages/flutter/lib/src/rendering` | 48 | 25645.56 | 24.08% | 12.99% |
| `engine/src/flutter/shell/platform/darwin/ios/framework/Source` | 123 | 16588.68 | 16.84% | 45.42% |
| `packages/flutter_test/lib/src` | 39 | 15432.92 | 27.81% | 15.8% |
| `packages/flutter_tools/test/commands.shard/hermetic` | 45 | 15255.02 | 60.25% | 0.0% |

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
- `dev/bots/docs.sh` -> **100.0%** Exposure
- `dev/tools/repackage_gradle_wrapper.sh` -> **100.0%** Exposure
- `engine/src/flutter/bin/et` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` -> **0** Orphaned Functions | **6831** Duplicates
- `packages/flutter/test/material/text_field_test.dart` -> **8** Orphaned Functions | **2690** Duplicates
- `packages/flutter_localizations/lib/src/l10n/generated_cupertino_localizations.dart` -> **0** Orphaned Functions | **2652** Duplicates
- `packages/flutter/test/cupertino/text_field_test.dart` -> **11** Orphaned Functions | **1593** Duplicates
- `packages/flutter/test/widgets/editable_text_test.dart` -> **17** Orphaned Functions | **1226** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `examples/image_list/lib/main.dart` -> **99.9999%** Exposure
- `dev/packages_autoroller/test/packages_autoroller_test.dart` -> **20.5011%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `18` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `46657` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 66.652)
- **Top Global Matches:** file_cluster_4: 66.652, file_cluster_12: 67.102, file_cluster_16: 67.142
- **Magnitude:** 19184.04 | **LOC:** 46987 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (54.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.4%)
- **Documentation Coverage:** 49.5929% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMaterialTranslation` **(Many-Argument Workhorses)** (Impact: 455.5)
    * *Intent:* /// * `th` - Thai /// * `tl` - Tagalog /// * `tr` - Turkish /// * `ug` - Uighur Uyghur /// * `uk` - ...
  * `MaterialLocalizationAf` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Afrikaans. /// /// For details on the meaning o...
  * `MaterialLocalizationAm` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Amharic. /// /// For details on the meaning of ...
  * `MaterialLocalizationAr` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Arabic. /// /// For details on the meaning of t...
  * `MaterialLocalizationAs` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Assamese. /// /// For details on the meaning of...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1429`, `structural_boundaries: 14986`, `args: 1`, `func_start: 14860`, `class_start: 119`
* *Risk/State:* `planned_debt: 3`, `duplicate_logic: 6831`
* *Architecture:* `api: 120`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 2376`, `doc: 583`, `sync_locks: 216`, `immutability_locks: 120`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.081
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.041882
  * `Imports (Out-Degree: 2):` material_localizations.dart, dart:collection, material.dart, intl.dart
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/flutter/test/material/text_field_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 16.367)
- **Top Global Matches:** file_cluster_12: 16.367, file_cluster_11: 16.929, file_cluster_15: 16.965
- **Magnitude:** 10005.62 | **LOC:** 19564 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (44.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (40.3%), Guard Balance (formerly Safety Score) (37.5%)
- **Documentation Coverage:** 99.9389% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 96.2)
  * `async` **(I/O & Config Routines)** (Impact: 20.4)
  * `async` **(I/O & Config Routines)** (Impact: 20.1)
  * `async` **(I/O & Config Routines)** (Impact: 18.5)
  * `async` **(I/O & Config Routines)** (Impact: 17.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 68 instances
* *Amplified Cascading Flux:* 38 instances
* *Concurrency (weighted view):* 4014
* *State Mutation (weighted view):* 379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 280`, `structural_boundaries: 3440`, `args: 118`, `func_start: 3474`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 127`, `state_mutation: 303`, `planned_debt: 7`, `fragile_debt: 2`, `duplicate_logic: 2690`, `unreferenced_by_name: 8`
* *Architecture:* `api: 11`, `concurrency: 3674`, `import: 16`
* *Defense:* `safety: 297`, `doc: 1`, `test: 4147`, `immutability_locks: 1158`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` clipboard_utils.dart, editable_text_utils.dart, feedback_tester.dart, live_text_utils.dart, process_text_utils.dart, semantics_tester.dart, text_selection_toolbar_utils.dart, dart:math...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_localizations/lib/src/l10n/generated_cupertino_localizations.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 40.092)
- **Top Global Matches:** file_cluster_4: 40.092, file_cluster_12: 40.216, file_cluster_16: 40.25
- **Magnitude:** 8877.56 | **LOC:** 17846 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 0.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (59.6%), Concurrency Surface (formerly Concurrency) (12.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.4%)
- **Documentation Coverage:** 48.8359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCupertinoTranslation` **(Many-Argument Workhorses)** (Impact: 452.1)
    * *Intent:* /// * `th` - Thai /// * `tl` - Tagalog /// * `tr` - Turkish /// * `ug` - Uighur Uyghur /// * `uk` - ...
  * `CupertinoLocalizationAf` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Afrikaans. /// /// For details on the meaning o...
  * `CupertinoLocalizationAm` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Amharic. /// /// For details on the meaning of ...
  * `CupertinoLocalizationAr` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Arabic. /// /// For details on the meaning of t...
  * `CupertinoLocalizationAs` **(Defensive Guards)** (Impact: 3.9)
    * *Intent:* /// Create an instance of the translation bundle for Assamese. /// /// For details on the meaning of...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2195`, `structural_boundaries: 5277`, `args: 1`, `func_start: 5153`, `class_start: 118`
* *Risk/State:* `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 2652`
* *Architecture:* `api: 119`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 3131`, `doc: 578`, `immutability_locks: 119`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.088
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.041915
  * `Imports (Out-Degree: 2):` cupertino_localizations.dart, dart:collection, cupertino.dart, intl.dart
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/flutter/test/widgets/editable_text_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 11.409)
- **Top Global Matches:** file_cluster_12: 11.409, file_cluster_5: 12.263, file_cluster_0: 13.078
- **Magnitude:** 7236.4 | **LOC:** 18344 | **CtrlFlow:** 2.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.7%), Guard Balance (formerly Safety Score) (43.5%), Complexity Load (formerly Cognitive Load) (34.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 91.7)
  * `testTextEditing` **(Many-Argument Workhorses)** (Impact: 75.2)
  * `verifyVisibility` **(Many-Argument Workhorses)** (Impact: 29.7)
  * `verifyVisibility` **(Many-Argument Workhorses)** (Impact: 29.4)
  * `async` **(I/O & Config Routines)** (Impact: 23.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 164 instances
* *Amplified Cascading Flux:* 61 instances
* *Concurrency (weighted view):* 2709
* *State Mutation (weighted view):* 659
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 1834`, `args: 148`, `func_start: 1895`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 273`, `state_mutation: 537`, `planned_debt: 2`, `duplicate_logic: 1226`, `unreferenced_by_name: 17`
* *Architecture:* `api: 15`, `concurrency: 1889`, `import: 16`
* *Defense:* `safety: 416`, `test: 2677`, `immutability_locks: 870`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.07775
  * `Imports (Out-Degree: 26):` clipboard_utils.dart, dart:convert, dart:math, dart:ui, editable_text_tester.dart, editable_text_utils.dart, live_text_utils.dart, cupertino.dart...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/flutter/test/cupertino/text_field_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 24.782)
- **Top Global Matches:** file_cluster_12: 24.782, file_cluster_15: 25.478, file_cluster_11: 25.644
- **Magnitude:** 6374.8 | **LOC:** 10914 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.04; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.1%), Guard Balance (formerly Safety Score) (36.5%)
- **Documentation Coverage:** 92.401% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 662.6)
  * `async` **(I/O & Config Routines)** (Impact: 18.4)
  * `describeMismatch` **(Defensive Guards)** (Impact: 16.8)
  * `matches` **(Defensive Guards)** (Impact: 14.6)
  * `async` **(I/O & Config Routines)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 44 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 2358
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 151`, `structural_boundaries: 1983`, `args: 40`, `func_start: 2035`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 165`, `planned_debt: 4`, `fragile_debt: 1`, `duplicate_logic: 1593`, `unreferenced_by_name: 11`
* *Architecture:* `api: 4`, `concurrency: 2138`, `import: 12`
* *Defense:* `safety: 190`, `test: 2519`, `immutability_locks: 731`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.04
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.068958
  * `Imports (Out-Degree: 24):` clipboard_utils.dart, editable_text_utils.dart, live_text_utils.dart, semantics_tester.dart, text_selection_toolbar_utils.dart, dart:ui, cupertino.dart, foundation.dart...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `engine/src/flutter/testing/android/native_activity/debug.keystore` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/material/theme_data.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.222)
- **Top Global Matches:** file_cluster_4: 9.222, file_cluster_12: 10.77, file_cluster_5: 10.95
- **Magnitude:** 4877.5 | **LOC:** 3490 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **112** in-repo importer(s); it depends on **69**; blast radius 1.538; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (36.4%), Complexity Load (formerly Cognitive Load) (35.4%)
- **Documentation Coverage:** 33.8462% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ThemeData` **(Many-Argument Workhorses)** (Impact: 2358.5)
    * *Intent:* /// a component theme parameter like [sliderTheme], [toggleButtonsTheme], /// or [bottomNavigationBa...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 1662.3)
    * *Intent:* /// Creates a copy of this theme but with the given fields replaced with the new values. /// /// The...
  * `operator==` **(Compute Cores)** (Impact: 125.1)
  * `lerp` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// Linearly interpolate between two themes. ///
  * `_overrideWithSystemColors` **(I/O & Config Routines)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 109 instances
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 594`, `structural_boundaries: 139`, `args: 43`, `func_start: 59`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 196`, `planned_debt: 9`
* *Architecture:* `api: 19`, `import: 69`
* *Defense:* `safety: 563`, `doc: 805`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.538
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.099485
  * `Imports (Out-Degree: 68):` action_buttons.dart, action_icons_theme.dart, app_bar_theme.dart, badge_theme.dart, banner_theme.dart, bottom_app_bar_theme.dart, bottom_navigation_bar_theme.dart, bottom_sheet_theme.dart...
  * `Imported By (In-Degree: 112):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/material/input_decorator.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.53)
- **Top Global Matches:** file_cluster_4: 8.53, file_cluster_12: 10.549, file_cluster_5: 11.693
- **Magnitude:** 4591.56 | **LOC:** 6108 | **CtrlFlow:** 37.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **17**; blast radius 0.288; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Complexity Load (formerly Cognitive Load) (28.6%), Guard Balance (formerly Safety Score) (28.2%)
- **Documentation Coverage:** 77.5591% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 920.1)
    * *Intent:* /// Creates a copy of this input decoration with the given fields replaced /// by the new values.
  * `InputDecorationTheme` **(Many-Argument Workhorses)** (Impact: 543.9)
    * *Intent:* /// Creates a [InputDecorationTheme] that controls visual parameters for /// descendant [InputDecora...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 466.3)
    * *Intent:* /// Creates a copy of this object but with the given fields replaced with the /// new values. /// //...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 466.3)
    * *Intent:* /// Creates a copy of this object but with the given fields replaced with the /// new values.
  * `build` **(Defensive Guards)** (Impact: 162.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1428`, `structural_boundaries: 392`, `args: 131`, `func_start: 238`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 90`, `state_mutation: 157`, `planned_debt: 7`, `duplicate_logic: 4`
* *Architecture:* `api: 34`, `import: 17`
* *Defense:* `safety: 1052`, `doc: 1634`, `immutability_locks: 59`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.288
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.098228
  * `Imports (Out-Degree: 25):` button_style.dart, color_scheme.dart, colors.dart, constants.dart, dart:math, dart:ui, icon_button_theme.dart, input_border.dart...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/material/color_scheme.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.119)
- **Top Global Matches:** file_cluster_6: 7.119, file_cluster_4: 10.741, file_cluster_8: 15.935
- **Magnitude:** 4195.44 | **LOC:** 2240 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **122** in-repo importer(s); it depends on **7**; blast radius 0.965; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (62.1%), Mutation Surface (formerly State Flux) (46.6%), Complexity Load (formerly Cognitive Load) (35.3%)
- **Documentation Coverage:** 16.4384% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromImageProvider` **(Many-Argument Workhorses)** (Impact: 735.7)
    * *Intent:* /// /// ** See code in examples/api/lib/material/color_scheme/dynamic_content_color.0.dart ** /// //...
  * `ColorScheme.fromSeed` **(Many-Argument Workhorses)** (Impact: 735.2)
    * *Intent:* /// This sample shows how to use [ColorScheme.fromSeed] to create dynamic /// color schemes with dif...
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 727.2)
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
* *Structure:* `branch: 665`, `structural_boundaries: 85`, `args: 18`, `func_start: 106`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 74`
* *Architecture:* `api: 14`, `concurrency: 23`, `import: 7`
* *Defense:* `safety: 624`, `doc: 454`, `sync_locks: 1`, `immutability_locks: 32`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.965
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.099202
  * `Imports (Out-Degree: 6):` colors.dart, dart:async, dart:ui, foundation.dart, widgets.dart, material_color_utilities.dart, theme.dart
  * `Imported By (In-Degree: 122):` (Excluded from Brief to save tokens)

### `packages/flutter_test/lib/src/matchers.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.089)
- **Top Global Matches:** file_cluster_5: 9.089, file_cluster_12: 10.381, file_cluster_7: 11.312
- **Magnitude:** 4049.7 | **LOC:** 3312 | **CtrlFlow:** 29.7% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **19**; blast radius 0.448; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Guard Balance (formerly Safety Score) (44.0%), Complexity Load (formerly Cognitive Load) (35.7%), Concurrency Surface (formerly Concurrency) (31.2%)
- **Documentation Coverage:** 67.1795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_MatchesSemanticsData` **(Many-Argument Workhorses)** (Impact: 793.7)
  * `containsSemantics` **(Many-Argument Workhorses)** (Impact: 778.8)
    * *Intent:* /// validated. /// /// To find a [SemanticsNode] directly, use [CommonFinders.semantics]. /// These ...
  * `isSemantics` **(Many-Argument Workhorses)** (Impact: 778.6)
    * *Intent:* /// /// ```dart /// testWidgets('isSemantics', (WidgetTester tester) async { /// final SemanticsHand...
  * `matchesSemantics` **(Many-Argument Workhorses)** (Impact: 283.7)
    * *Intent:* /// /// ```dart /// testWidgets('matchesSemantics', (WidgetTester tester) async { /// final Semantic...
  * `matches` **(Many-Argument Workhorses)** (Impact: 147.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 682`, `structural_boundaries: 350`, `args: 160`, `func_start: 167`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 157`, `duplicate_logic: 10`
* *Architecture:* `api: 32`, `concurrency: 15`, `import: 18`
* *Defense:* `safety: 517`, `doc: 717`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.448
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.091119
  * `Imports (Out-Degree: 15):` _matchers_io.dart, _matchers_web.dart, accessibility.dart, binding.dart, controller.dart, dart:convert, dart:math, dart:ui...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `packages/flutter/test/widgets/selectable_region_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 20.365)
- **Top Global Matches:** file_cluster_12: 20.365, file_cluster_0: 21.052, file_cluster_15: 21.112
- **Magnitude:** 4043.3 | **LOC:** 6843 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.1%), Complexity Load (formerly Cognitive Load) (43.8%), Guard Balance (formerly Safety Score) (33.7%)
- **Documentation Coverage:** 99.9178% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 444.2)
  * `async` **(Defensive Guards)** (Impact: 21.1)
  * `async` **(Defensive Guards)** (Impact: 15.7)
  * `async` **(I/O & Config Routines)** (Impact: 12.7)
  * `async` **(Callbacks & Closures)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 1461
* *State Mutation (weighted view):* 164
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 1385`, `args: 56`, `func_start: 1331`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 53`, `state_mutation: 96`, `planned_debt: 1`, `duplicate_logic: 1051`, `unreferenced_by_name: 12`
* *Architecture:* `api: 8`, `concurrency: 1386`, `import: 12`
* *Defense:* `safety: 321`, `doc: 2`, `test: 1654`, `immutability_locks: 546`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` clipboard_utils.dart, editable_text_tester.dart, keyboard_utils.dart, foundation.dart, gestures.dart, material.dart, rendering.dart, services.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/test/material/input_decorator_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 14.015)
- **Top Global Matches:** file_cluster_12: 14.015, file_cluster_15: 14.17, file_cluster_11: 14.448
- **Magnitude:** 3969.5 | **LOC:** 15774 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 20.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.9%), Guard Balance (formerly Safety Score) (33.2%), Complexity Load (formerly Cognitive Load) (16.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildInputDecorator` **(Many-Argument Workhorses)** (Impact: 47.0)
  * `main` **(I/O & Config Routines)** (Impact: 40.5)
  * `buildInputDecoratorM2` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* // These tests are only relevant for Material 2. Once Material 2 // support is deprecated and the AP...
  * `buildInputDecoratorWithFloatingLabel` **(Defensive Guards)** (Impact: 13.3)
  * `buildFrame` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 1554
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 1114`, `args: 110`, `func_start: 1132`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 51`, `dead_code: 1`, `planned_debt: 7`, `duplicate_logic: 557`, `unreferenced_by_name: 2`
* *Architecture:* `api: 42`, `concurrency: 1524`, `import: 6`
* *Defense:* `safety: 305`, `test: 4159`, `sync_locks: 4`, `immutability_locks: 1434`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` dart:async, dart:ui, foundation.dart, material.dart, rendering.dart, flutter_test.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/semantics/semantics.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.226)
- **Top Global Matches:** file_cluster_12: 9.226, file_cluster_5: 9.439, file_cluster_4: 11.534
- **Magnitude:** 3613.16 | **LOC:** 7176 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **10**; blast radius 0.385; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (98.8%), Complexity Load (formerly Cognitive Load) (50.6%), Guard Balance (formerly Safety Score) (45.8%)
- **Documentation Coverage:** 16.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SemanticsProperties` **(Many-Argument Workhorses)** (Impact: 94.3)
    * *Intent:* /// Creates a semantic annotation.
  * `_addToUpdate` **(Defensive Guards)** (Impact: 89.2)
  * `getSemanticsData` **(I/O & Config Routines)** (Impact: 73.0)
    * *Intent:* /// Returns a summary of the semantics for this node. /// /// If this node has [mergeAllDescendantsI...
  * `absorb` **(Defensive Guards)** (Impact: 63.2)
    * *Intent:* /// Absorb the semantic information from `child` into this configuration. /// /// This adds the sema...
  * `SemanticsData` **(Many-Argument Workhorses)** (Impact: 57.2)
    * *Intent:* /// Creates a semantics data object. /// /// If [label] is not empty, then [textDirection] must also...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 369 instances
* *State Mutation (weighted view):* 1331
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1166`, `structural_boundaries: 532`, `args: 248`, `func_start: 411`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 125`, `state_mutation: 593`, `planned_debt: 6`, `fragile_debt: 1`, `duplicate_logic: 70`
* *Architecture:* `api: 60`, `import: 16`
* *Defense:* `safety: 769`, `doc: 2494`, `immutability_locks: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.385
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.088176
  * `Imports (Out-Degree: 8):` binding.dart, dart:core, dart:math, dart:ui, collection.dart, foundation.dart, painting.dart, services.dart...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `packages/flutter/lib/src/gestures/events.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.444)
- **Top Global Matches:** file_cluster_4: 8.444, file_cluster_6: 10.374, file_cluster_15: 14.239
- **Magnitude:** 3591.88 | **LOC:** 2607 | **CtrlFlow:** 41.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **25** in-repo importer(s); it depends on **5**; blast radius 1.22; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (32.4%), Complexity Load (formerly Cognitive Load) (21.6%), Debt Markers (formerly Tech Debt) (16.2%)
- **Documentation Coverage:** 63.0573% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 232.6)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 227.9)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 223.0)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 223.0)
  * `copyWith` **(Many-Argument Workhorses)** (Impact: 223.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 33
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 724`, `structural_boundaries: 182`, `args: 77`, `func_start: 146`, `class_start: 51`
* *Risk/State:* `state_mutation: 31`, `duplicate_logic: 6`
* *Architecture:* `api: 31`, `import: 9`
* *Defense:* `safety: 705`, `doc: 603`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.22
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.089787
  * `Imports (Out-Degree: 3):` constants.dart, dart:ui, gesture_settings.dart, foundation.dart, vector_math_64.dart
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `packages/flutter/test/material/menu_anchor_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 18.944)
- **Top Global Matches:** file_cluster_0: 18.944, file_cluster_15: 19.137, file_cluster_11: 19.197
- **Magnitude:** 3576.44 | **LOC:** 7129 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (38.4%), Complexity Load (formerly Cognitive Load) (34.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (28.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 540.9)
  * `createTestMenus` **(Many-Argument Workhorses)** (Impact: 43.8)
  * `buildTestApp` **(Many-Argument Workhorses)** (Impact: 43.4)
  * `menuItemButton` **(Defensive Guards)** (Impact: 17.9)
  * `buildSimpleMenuAnchor` **(Generic / Templated Code)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 40 instances
* *Concurrency (weighted view):* 1092
* *State Mutation (weighted view):* 197
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 1037`, `args: 64`, `func_start: 980`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 117`, `duplicate_logic: 733`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 3`, `concurrency: 1067`, `import: 9`
* *Defense:* `safety: 163`, `test: 1328`, `immutability_locks: 432`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` semantics_tester.dart, foundation.dart, gestures.dart, material.dart, rendering.dart, services.dart, flutter_test.dart, leak_tracker.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter_tools/test/commands.shard/permeable/create_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 12.12)
- **Top Global Matches:** file_cluster_0: 12.12, file_cluster_10: 13.032, file_cluster_12: 13.632
- **Magnitude:** 3541.1 | **LOC:** 5240 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **38**; blast radius 0.256; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.2%)
- **Documentation Coverage:** 99.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 297.9)
  * `_createProject` **(Generic / Templated Code)** (Impact: 18.8)
  * `async` **(I/O & Config Routines)** (Impact: 12.8)
  * `async` **(I/O & Config Routines)** (Impact: 9.5)
  * `async` **(I/O & Config Routines)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 256 instances
* *Amplified Cascading Flux:* 23 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 1754
* *State Mutation (weighted view):* 586
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 540`, `args: 188`, `func_start: 365`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 2`, `state_mutation: 540`, `planned_debt: 1`, `duplicate_logic: 132`, `unreferenced_by_name: 4`
* *Architecture:* `io: 85`, `api: 1`, `concurrency: 474`, `import: 38`
* *Defense:* `safety: 76`, `doc: 1`, `test: 443`, `sync_locks: 4`, `immutability_locks: 64`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.256
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.002494
  * `Imports (Out-Degree: 11):` common.dart, context.dart, fake_http_client.dart, fakes.dart, pubspec_schema.dart, test_flutter_command_runner.dart, dart:async, dart:convert...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `packages/flutter/test/material/tabs_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 17.12)
- **Top Global Matches:** file_cluster_12: 17.12, file_cluster_5: 17.74, file_cluster_0: 18.137
- **Magnitude:** 3511.14 | **LOC:** 9798 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 22.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Guard Balance (formerly Safety Score) (40.5%), Complexity Load (formerly Cognitive Load) (22.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 545.6)
  * `buildFrame` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `boilerplate` **(Defensive Guards)** (Impact: 15.8)
  * `buildTabBar` **(Defensive Guards)** (Impact: 9.0)
  * `buildLeftRightApp` **(Defensive Guards)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 9 instances
* *Concurrency (weighted view):* 1036
* *State Mutation (weighted view):* 347
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 995`, `args: 133`, `func_start: 892`
* *Risk/State:* `safety_bypasses: 122`, `state_mutation: 329`, `planned_debt: 2`, `duplicate_logic: 539`, `unreferenced_by_name: 3`
* *Architecture:* `api: 4`, `concurrency: 956`, `import: 9`
* *Defense:* `safety: 107`, `test: 2093`, `immutability_locks: 812`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 24):` feedback_tester.dart, semantics_tester.dart, foundation.dart, gestures.dart, material.dart, rendering.dart, services.dart, flutter_test.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `dev/benchmarks/macrobenchmarks/lib/src/web/bench_paths_recording.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.846)
- **Top Global Matches:** file_cluster_2: 6.846, file_cluster_15: 7.545, file_cluster_17: 7.566
- **Magnitude:** 3266.7 | **LOC:** 6742 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 0.041; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPaths` **(I/O & Config Routines)** (Impact: 1.5)
  * `pathOps0` **(I/O & Config Routines)** (Impact: 1.5)
  * `pathOps1` **(I/O & Config Routines)** (Impact: 1.5)
  * `pathOps2` **(I/O & Config Routines)** (Impact: 1.5)
  * `pathOps3` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 212`, `args: 582`, `func_start: 612`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 1764`
* *Architecture:* `api: 581`, `import: 1`
* *Defense:* `safety: 211`, `immutability_locks: 427`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.041
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000124
  * `Imports (Out-Degree: 2):` dart:ui
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `packages/flutter/test/widgets/navigator_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 16.537)
- **Top Global Matches:** file_cluster_5: 16.537, file_cluster_12: 17.366, file_cluster_7: 18.341
- **Magnitude:** 3241.92 | **LOC:** 6780 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (41.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (34.8%), Complexity Load (formerly Cognitive Load) (33.2%)
- **Documentation Coverage:** 99.8601% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 514.4)
  * `resolve` **(Defensive Guards)** (Impact: 22.0)
  * `tester.pumpWidget` **(Callbacks & Closures)** (Impact: 19.7)
  * `tester.pumpWidget` **(Callbacks & Closures)** (Impact: 17.4)
  * `tester.pumpWidget` **(Callbacks & Closures)** (Impact: 17.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 26 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 896
* *State Mutation (weighted view):* 384
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 254`, `structural_boundaries: 1175`, `args: 283`, `func_start: 769`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 378`, `state_mutation: 238`, `duplicate_logic: 543`, `unreferenced_by_name: 13`
* *Architecture:* `api: 25`, `concurrency: 766`, `import: 12`
* *Defense:* `safety: 305`, `doc: 12`, `test: 1888`, `immutability_locks: 402`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` dart:ui, list_tile_tester.dart, navigator_utils.dart, observer_tester.dart, foundation.dart, material.dart, rendering.dart, scheduler.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/rendering/object.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.955)
- **Top Global Matches:** file_cluster_12: 9.955, file_cluster_5: 10.008, file_cluster_4: 11.504
- **Magnitude:** 3153.5 | **LOC:** 6760 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **42** in-repo importer(s); it depends on **10**; blast radius 1.456; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (48.8%), Complexity Load (formerly Cognitive Load) (47.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.1%)
- **Documentation Coverage:** 28.2051% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `describeSemanticsConfiguration` **(Many-Argument Workhorses)** (Impact: 131.0)
  * `computeChildGeometry` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `layout` **(Defensive Guards)** (Impact: 57.0)
    * *Intent:* /// be marked as needing layout whenever the child is marked as needing layout /// because the paren...
  * `flushSemantics` **(I/O & Config Routines)** (Impact: 54.5)
    * *Intent:* /// Update the semantics for render objects marked as needing a semantics /// update. /// /// Initia...
  * `updateChildren` **(I/O & Config Routines)** (Impact: 44.8)
    * *Intent:* /// [_RenderObjectSemantics]. /// /// Gather all the merge up _RenderObjectSemantics(s) by walking t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 386 instances
* *State Mutation (weighted view):* 1252
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 907`, `structural_boundaries: 355`, `args: 241`, `func_start: 311`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 159`, `state_mutation: 480`, `planned_debt: 16`, `duplicate_logic: 2`
* *Architecture:* `api: 68`, `import: 13`
* *Defense:* `safety: 708`, `doc: 2033`, `test: 1`, `immutability_locks: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.456
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.091119
  * `Imports (Out-Degree: 14):` binding.dart, dart:ui, debug.dart, layer.dart, animation.dart, foundation.dart, gestures.dart, painting.dart...
  * `Imported By (In-Degree: 42):` (Excluded from Brief to save tokens)

### `packages/flutter/test/material/chip_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 16.7)
- **Top Global Matches:** file_cluster_12: 16.7, file_cluster_15: 16.751, file_cluster_11: 17.012
- **Magnitude:** 3118.62 | **LOC:** 6478 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.8%), Guard Balance (formerly Safety Score) (32.5%), Complexity Load (formerly Cognitive Load) (31.4%)
- **Documentation Coverage:** 99.4261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 547.7)
  * `buildApp` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `buildApp` **(Many-Argument Workhorses)** (Impact: 33.5)
  * `chipWithOptionalDeleteButton` **(Many-Argument Workhorses)** (Impact: 33.2)
  * `getBorderSide` **(Defensive Guards)** (Impact: 16.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 783
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 804`, `args: 91`, `func_start: 687`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 171`, `duplicate_logic: 477`, `unreferenced_by_name: 5`
* *Architecture:* `api: 21`, `concurrency: 763`, `import: 9`
* *Defense:* `safety: 202`, `doc: 5`, `test: 1888`, `immutability_locks: 649`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` feedback_tester.dart, semantics_tester.dart, foundation.dart, gestures.dart, material.dart, rendering.dart, scheduler.dart, services.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/lib/src/widgets/editable_text.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.027)
- **Top Global Matches:** file_cluster_4: 8.027, file_cluster_12: 10.72, file_cluster_5: 11.496
- **Magnitude:** 3106.96 | **LOC:** 6793 | **CtrlFlow:** 27.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **50**; blast radius 0.211; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (93.2%), Guard Balance (formerly Safety Score) (42.4%), Concurrency Surface (formerly Concurrency) (41.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%)
- **Documentation Coverage:** 73.1884% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `EditableText` **(Many-Argument Workhorses)** (Impact: 367.1)
    * *Intent:* /// Creates a basic text input control. /// /// The [maxLines] property can be set to null to remove...
  * `getEditableButtonItems` **(Many-Argument Workhorses)** (Impact: 75.4)
    * *Intent:* /// For example, [EditableText] uses this to generate the default buttons for /// its context menu. ...
  * `didUpdateWidget` **(Defensive Guards)** (Impact: 67.1)
  * `build` **(Defensive Guards)** (Impact: 65.5)
  * `invoke` **(Defensive Guards)** (Impact: 44.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 162 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 548
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1141`, `structural_boundaries: 415`, `args: 221`, `func_start: 255`, `class_start: 27`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 224`, `planned_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `api: 43`, `concurrency: 31`, `import: 50`
* *Defense:* `safety: 575`, `doc: 1641`, `immutability_locks: 51`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.211
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.098268
  * `Imports (Out-Degree: 58):` _web_browser_detection_io.dart, _web_browser_detection_web.dart, actions.dart, app_lifecycle_listener.dart, autofill.dart, automatic_keep_alive.dart, basic.dart, binding.dart...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `engine/src/flutter/lib/ui/painting.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.633)
- **Top Global Matches:** file_cluster_0: 8.633, file_cluster_16: 9.687, file_cluster_12: 9.781
- **Magnitude:** 2892.26 | **LOC:** 9279 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **194** in-repo importer(s); blast radius 2.371; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (84.4%), Concurrency Surface (formerly Concurrency) (58.9%), Mutation Surface (formerly State Flux) (56.6%), Guard Balance (formerly Safety Score) (33.3%)
- **Documentation Coverage:** 47.9042% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `drawAtlas` **(Many-Argument Workhorses)** (Impact: 57.0)
  * `withValues` **(Defensive Guards)** (Impact: 50.2)
    * *Intent:* /// /// Each component ([alpha], [red], [green], [blue]) represents a /// floating-point value; see ...
  * `Vertices` **(Defensive Guards)** (Impact: 46.3)
    * *Intent:* /// entries, but may be of any length beyond this. Indicies may refer to /// offsets in the position...
  * `decodeImageFromPixels` **(Many-Argument Workhorses)** (Impact: 45.9)
    * *Intent:* /// The `targetWidth` and `targetHeight` arguments specify the size of the /// output image, in imag...
  * `drawRawAtlas` **(Many-Argument Workhorses)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 92 instances
* *Concurrency (weighted view):* 129
* *State Mutation (weighted view):* 324
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 490`, `args: 299`, `func_start: 603`, `class_start: 77`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 140`, `dead_code: 2`, `planned_debt: 3`, `fragile_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 100`, `concurrency: 49`
* *Defense:* `safety: 499`, `doc: 4120`, `sync_locks: 15`, `immutability_locks: 97`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.371
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.111502
  * `Imports (Out-Degree: 2):` None
  * `Imported By (In-Degree: 194):` (Excluded from Brief to save tokens)

### `packages/flutter/test/material/date_picker_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 14.634)
- **Top Global Matches:** file_cluster_12: 14.634, file_cluster_5: 15.339, file_cluster_10: 16.112
- **Magnitude:** 2856.12 | **LOC:** 2899 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (50.0%), Guard Balance (formerly Safety Score) (33.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 260.6)
  * `prepareDatePicker` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `buildApp` **(Defensive Guards)** (Impact: 8.1)
  * `buildApp` **(Defensive Guards)** (Impact: 8.1)
  * `prepareDatePicker` **(Many-Argument Workhorses)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 123 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 1442
* *State Mutation (weighted view):* 229
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 629`, `args: 39`, `func_start: 561`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 119`, `duplicate_logic: 423`, `unreferenced_by_name: 9`
* *Architecture:* `api: 2`, `concurrency: 827`, `import: 6`
* *Defense:* `safety: 161`, `test: 857`, `immutability_locks: 88`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` clipboard_utils.dart, dart:ui, material.dart, rendering.dart, services.dart, flutter_test.dart
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `packages/flutter/test/material/selectable_text_test.dart` (DART | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 16.739)
- **Top Global Matches:** file_cluster_12: 16.739, file_cluster_5: 17.639, file_cluster_15: 17.96
- **Magnitude:** 2822.82 | **LOC:** 5739 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.028; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (41.1%), Guard Balance (formerly Safety Score) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(I/O & Config Routines)** (Impact: 337.6)
  * `async` **(Defensive Guards)** (Impact: 8.2)
  * `async` **(I/O & Config Routines)** (Impact: 7.6)
  * `async` **(Callbacks & Closures)** (Impact: 6.8)
  * `selectableTextBuilder` **(Defensive Guards)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 21 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 1072
* *State Mutation (weighted view):* 118
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 898`, `args: 38`, `func_start: 935`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 80`, `planned_debt: 4`, `fragile_debt: 2`, `duplicate_logic: 588`, `unreferenced_by_name: 4`
* *Architecture:* `api: 7`, `concurrency: 967`, `import: 13`
* *Defense:* `safety: 72`, `test: 1163`, `immutability_locks: 507`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.028
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 21):` clipboard_utils.dart, editable_text_utils.dart, semantics_tester.dart, dart:ui, cupertino.dart, foundation.dart, gestures.dart, material.dart...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `packages/flutter/test/widgets/animated_align_test.dart` (DART) | Magnitude: 35.36 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 144, test: 42, immutability_locks: 20, concurrency: 17
- `examples/api/lib/widgets/keep_alive/automatic_keep_alive_client_mixin.0.dart` (DART) | Magnitude: 29.1 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, ui_framework: 13, structural_boundaries: 11, func_start: 11
- `dev/integration_tests/flutter_gallery/lib/demo/transformations/transformations_demo_color_picker.dart` (DART) | Magnitude: 15.1 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 43, safety: 11, structural_boundaries: 6, immutability_locks: 6
- `dev/integration_tests/android_engine_test/lib/hcpp/hc_errors_with_hcpp_enabled.dart` (DART) | Magnitude: 49.28 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 29, immutability_locks: 17, ui_framework: 15
- `dev/integration_tests/android_engine_test/lib/hcpp/tlhc_with_fallback_to_hc_errors_with_hcpp_enabled.dart` (DART) | Magnitude: 49.28 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 103, structural_boundaries: 29, immutability_locks: 17, ui_framework: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `examples/api/lib/widgets/gesture_detector/gesture_detector.3.dart` (DART) | Magnitude: 15.4 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 58, ui_framework: 9, core_var_decl: 7, structural_boundaries: 6
- `engine/src/flutter/shell/common/vsync_waiters_test.cc` (CPP) | Magnitude: 26.52 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 11, func_start: 7, import: 7
- `packages/flutter/test/widgets/async_lifecycle_test.dart` (DART) | Magnitude: 35.58 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, func_start: 15, structural_boundaries: 14, concurrency: 11
- `packages/flutter/test/rendering/mutations_test.dart` (DART) | Magnitude: 60.6 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 188, test: 34, state_mutation: 24, closures: 23
- `packages/flutter/lib/src/rendering/texture.dart` (DART) | Magnitude: 42.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 55, doc: 32, core_var_decl: 14, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `engine/src/flutter/impeller/renderer/command.h` (CPP) | Magnitude: 16.08 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: doc: 51, indent_spaces: 35, structural_boundaries: 12, core_var_decl: 12
- `engine/src/flutter/lib/web_ui/lib/ui_web/src/ui_web/initialization.dart` (DART) | Magnitude: 35.58 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 20, indent_spaces: 20, branch: 10, concurrency: 7
- `examples/api/test/material/refresh_indicator/refresh_indicator.0_test.dart` (DART) | Magnitude: 35.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 15, concurrency: 14, func_start: 13
- `examples/api/test/material/icon_button/icon_button.1_test.dart` (DART) | Magnitude: 8.98 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 14, test: 8, structural_boundaries: 5, func_start: 3
- `examples/api/test/services/keyboard_key/logical_keyboard_key.0_test.dart` (DART) | Magnitude: 20.56 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 13, test: 12, structural_boundaries: 10, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `dev/tools/gen_keycodes/lib/testing_key_codes_java_gen.dart` (DART) | Magnitude: 0.02 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 13, func_start: 6, import: 5
- `packages/flutter/lib/src/rendering/proxy_sliver.dart` (DART) | Magnitude: 255.58 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 336, doc: 104, branch: 53, structural_boundaries: 43
- `packages/integration_test/example/integration_test/_extended_test_web.dart` (DART) | Magnitude: 23.26 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 10, func_start: 6, concurrency: 6
- `packages/flutter/test/cupertino/dialog_test.dart` (DART) | Magnitude: 1047.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 1938, test: 509, structural_boundaries: 399, concurrency: 365
- `dev/integration_tests/new_gallery/lib/demos/cupertino/cupertino_switch_demo.dart` (DART) | Magnitude: 20.64 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 7, ui_framework: 7, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `dev/integration_tests/ios_add2app_uiscene/native/UITests-StateRestoration.swift` (SWIFT) | Magnitude: 6.5 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 6, test: 4, core_var_decl: 4
- `examples/api/lib/widgets/basic/absorb_pointer.0.dart` (DART) | Magnitude: 12.56 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 37, ui_framework: 7, structural_boundaries: 6, func_start: 5
- `dev/benchmarks/complex_layout/test_driver/scroll_perf_bad.dart` (DART) | Magnitude: 2.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 2, indent_spaces: 2, args: 1
- `examples/api/lib/cupertino/context_menu/cupertino_context_menu.1.dart` (DART) | Magnitude: 18.12 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 93, ui_framework: 13, immutability_locks: 11, structural_boundaries: 8
- `examples/api/lib/widgets/interactive_viewer/interactive_viewer.0.dart` (DART) | Magnitude: 12.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 31, ui_framework: 7, immutability_locks: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `packages/flutter_test/test/test_config/flutter_test_config.dart` (DART) | Magnitude: 9.48 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: concurrency: 4, structural_boundaries: 2, func_start: 2, api: 2
- `engine/src/flutter/shell/platform/android/io/flutter/plugin/common/EventChannel.java` (JAVA) | Magnitude: 118.94 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 130, structural_boundaries: 37, safety_bypasses: 30, branch: 18
- `dev/tools/gen_defaults/lib/text_field_template.dart` (DART) | Magnitude: 0.01 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 8, func_start: 5, closures: 5
- `dev/tools/repackage_gradle_wrapper.sh` (SHELL) | Magnitude: 0.04 | Delta: **0.08** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 28, indent_spaces: 16, state_mutation: 12, debug_prints: 12
- `engine/src/flutter/testing/test_gl_context.h` (CPP) | Magnitude: 15.32 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 9, safety_bypasses: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `engine/src/flutter/impeller/shader_archive/shader_archive.h` (CPP) | Magnitude: 7.38 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 38, immutability_locks: 13, structural_boundaries: 9, args: 8
- `packages/flutter/test/widgets/editable_text_shortcuts_test.dart` (DART) | Magnitude: 2440.12 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 2376, test: 591, func_start: 581, concurrency: 566
- `examples/platform_view/ios/Runner/AppDelegate.m` (OBJECTIVE-C) | Magnitude: 18.7 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 24, explicit_casts: 7, state_mutation: 5, core_var_decl: 5
- `packages/flutter_tools/test/web.shard/test_data/hot_restart_web_test_common.dart` (DART) | Magnitude: 138.2 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 92, concurrency: 31, structural_boundaries: 28, func_start: 18
- `engine/src/flutter/impeller/renderer/backend/vulkan/context_vk_unittests.cc` (CPP) | Magnitude: 143.44 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 285, pointers: 110, test: 78, args: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `dev/integration_tests/widget_preview_scaffold/lib/src/theme/theme.dart` (DART) | Magnitude: 76.1 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 229, core_var_decl: 45, immutability_locks: 40, design_camel_case: 38
- `engine/src/flutter/tools/fuchsia/toolchain/copy.py` (PYTHON) | Magnitude: 0.02 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 21, io: 11, branch: 8, structural_boundaries: 7
- `dev/integration_tests/flutter_gallery/lib/gallery/themes.dart` (DART) | Magnitude: 7.22 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 47, structural_boundaries: 15, immutability_locks: 12, core_var_decl: 10
- `examples/multiple_windows/lib/app/dialog_window_edit_dialog.dart` (DART) | Magnitude: 74.58 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 125, branch: 19, safety: 17, structural_boundaries: 15
- `dev/manual_tests/lib/card_collection.dart` (DART) | Magnitude: 205.94 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 442, core_var_decl: 48, ui_framework: 40, branch: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dev/manual_tests/lib/main.dart` (DART) | Magnitude: 2.58 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, func_start: 2, structural_boundaries: 1, args: 1
- `engine/src/flutter/shell/platform/common/client_wrapper/method_call_unittests.cc` (CPP) | Magnitude: 2.38 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, test: 4, import: 4, immutability_locks: 2
- `packages/flutter/lib/physics.dart` (DART) | Magnitude: 21.16 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7, import: 7, doc: 4
- `engine/src/flutter/shell/platform/darwin/ios/framework/Headers/FlutterHeadlessDartRunner.h` (OBJECTIVE-C) | Magnitude: 9.84 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: explicit_casts: 13, func_start: 6, doc: 6, import: 5
- `engine/src/flutter/shell/platform/common/path_utils.cc` (CPP) | Magnitude: 4.58 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, macros: 7, structural_boundaries: 6, io: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `engine/src/flutter/shell/platform/linux/fl_pointer_manager.h` (CPP) | Magnitude: 15.86 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 29, args: 7, doc: 6, import: 2
- `engine/src/flutter/shell/platform/windows/sequential_id_generator_unittests.cc` (CPP) | Magnitude: 5.74 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 22, test: 12, immutability_locks: 4, core_var_decl: 4
- `engine/src/flutter/sky/tools/cp.py` (PYTHON) | Magnitude: 0.01 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 5, io: 5, branch: 3
- `engine/src/flutter/shell/gpu/gpu_surface_unittests.cc` (CPP) | Magnitude: 1.92 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, test: 1
- `engine/src/flutter/flow/layers/transform_layer_unittests.cc` (CPP) | Magnitude: 55.68 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 404, pointers: 146, core_var_decl: 97, test: 96

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `packages/flutter/lib/src/widgets/form.dart` (DART) | Magnitude: 324.4 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 400, doc: 349, branch: 115, safety: 67
- `packages/flutter/lib/src/widgets/page_view.dart` (DART) | Magnitude: 501.82 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 568, doc: 360, safety: 131, branch: 129
- `packages/flutter/test/painting/gradient_test.dart` (DART) | Magnitude: 192.46 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 921, immutability_locks: 111, test: 109, core_var_decl: 105
- `engine/src/flutter/shell/platform/android/io/flutter/embedding/engine/deferredcomponents/PlayStoreDeferredComponentManager.java` (JAVA) | Magnitude: 231.88 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 374, structural_boundaries: 99, branch: 49, state_mutation: 44
- `engine/src/flutter/shell/platform/darwin/macos/framework/Source/FlutterMenuPlugin.mm` (OBJECTIVE-C) | Magnitude: 208.84 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 222, core_var_decl: 69, design_camel_case: 42, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `packages/flutter/test/rendering/localized_fonts_test.dart` (DART) | Magnitude: 64.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 237, ui_framework: 40, immutability_locks: 30, structural_boundaries: 21
- `dev/integration_tests/new_gallery/lib/demos/reference/motion_demo_fade_scale_transition.dart` (DART) | Magnitude: 34.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 124, ui_framework: 21, structural_boundaries: 15, func_start: 10
- `dev/integration_tests/new_gallery/lib/demos/material/picker_demo.dart` (DART) | Magnitude: 88.36 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 35, branch: 24, closures: 23
- `packages/flutter/lib/src/widgets/icon_data.dart` (DART) | Magnitude: 37.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 80, indent_spaces: 58, branch: 14, decorators: 13
- `packages/flutter/test/material/dropdown_form_field_test.dart` (DART) | Magnitude: 746.32 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1270, test: 295, structural_boundaries: 182, concurrency: 156

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `packages/flutter/test/material/menu_bar_theme_test.dart` (DART) | Magnitude: 213.5 | Delta: **0.071** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 306, branch: 52, safety: 52, args: 49

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `engine/src/flutter/lib/web_ui/test/engine/view_embedder/embedding_strategy/full_page_embedding_strategy_test.dart` (DART) | Magnitude: 15.98 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 58, test: 21, core_var_decl: 15, design_camel_case: 8
- `packages/integration_test/example/test_driver/failure.dart` (DART) | Magnitude: 12.44 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 6, doc: 5, test: 5
- `engine/src/flutter/shell/platform/android/test/io/flutter/embedding/android/SplashShadowResources.java` (JAVA) | Magnitude: 18.2 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 27, import: 12, decorators: 8
- `engine/src/flutter/lib/web_ui/flutter_js/src/canvaskit_loader.js` (JAVASCRIPT) | Magnitude: 50.32 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 13, branch: 10, core_var_decl: 10
- `engine/src/flutter/testing/dart/http_allow_http_connections_test.dart` (DART) | Magnitude: 17.16 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 11, concurrency: 11, closures: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `dev/integration_tests/new_gallery/lib/studies/reply/mailbox_body.dart` (DART) | Magnitude: 28.48 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 18, branch: 12, closures: 12
- `packages/flutter/lib/src/physics/utils.dart` (DART) | Magnitude: 18.26 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: doc: 8, branch: 6, indent_spaces: 5, structural_boundaries: 3
- `engine/src/flutter/tools/fuchsia/copy_debug_symbols.py` (PYTHON) | Magnitude: 0.08 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 91, core_var_decl: 38, design_snake_case: 38, structural_boundaries: 27
- `packages/flutter/lib/src/cupertino/adaptive_text_selection_toolbar.dart` (DART) | Magnitude: 91.1 | Delta: **0.089** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 108, indent_spaces: 100, safety: 34, branch: 30
- `engine/src/flutter/testing/skia_gold_client/tool/generate.dart` (DART) | Magnitude: 26.36 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 86, core_var_decl: 10, structural_boundaries: 9, branch: 8

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `engine/src/flutter/impeller/entity/entity_unittests.cc` -> Churn: **65.45%** | Cog Load: 25.1491% | Debt: 87.6239%
- `engine/src/flutter/shell/platform/android/io/flutter/view/AccessibilityBridge.java` -> Churn: **65.45%** | Cog Load: 74.4708% | Debt: 11.7483%
- `engine/src/flutter/testing/dart/fragment_shader_test.dart` -> Churn: **64.64%** | Cog Load: 94.7985% | Debt: 0.0%
- `packages/flutter_test/lib/src/binding.dart` -> Churn: **62.24%** | Cog Load: 43.141% | Debt: 99.3015%
- `engine/src/flutter/impeller/display_list/aiks_dl_basic_unittests.cc` -> Churn: **59.97%** | Cog Load: 12.0047% | Debt: 78.3383%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `packages/flutter_localizations/lib/src/l10n/generated_material_localizations.dart` -> **Qun Cheng** (100.0% isolated ownership) | Magnitude: 19184.04
- `packages/flutter_localizations/lib/src/l10n/generated_cupertino_localizations.dart` -> **Qun Cheng** (100.0% isolated ownership) | Magnitude: 8877.56
- `packages/flutter/lib/src/material/color_scheme.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 4195.44
- `packages/flutter/lib/src/gestures/events.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 3591.88
- `dev/benchmarks/macrobenchmarks/lib/src/web/bench_paths_recording.dart` -> **Kate Lovett** (100.0% isolated ownership) | Magnitude: 3266.7

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `packages/flutter/lib/src/widgets/drag_boundary.dart` -> **Severity: 7.756** (Embedded: 0.097 * Error Risk: 80.0%)
- `packages/flutter/lib/src/widgets/will_pop_scope.dart` -> **Severity: 7.756** (Embedded: 0.097 * Error Risk: 80.0%)
- `packages/flutter/lib/src/material/tab_indicator.dart` -> **Severity: 7.71** (Embedded: 0.0964 * Error Risk: 80.0%)
- `packages/flutter/lib/src/material/arc.dart` -> **Severity: 7.677** (Embedded: 0.096 * Error Risk: 80.0%)
- `engine/src/flutter/lib/web_ui/lib/src/engine/vector_math.dart` -> **Severity: 7.667** (Embedded: 0.1168 * Error Risk: 65.66%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `engine/src/flutter/fml/logging.h` -> **Severity: 939.2** (Blast Radius: 9.392 * Doc Risk: 100.0%)
- `engine/src/flutter/fml/logging.cc` -> **Severity: 580.7** (Blast Radius: 5.807 * Doc Risk: 100.0%)
- `engine/src/flutter/lib/web_ui/lib/src/engine/dom.dart` -> **Severity: 502.485** (Blast Radius: 5.516 * Doc Risk: 91.0959%)
- `engine/src/flutter/impeller/geometry/scalar.h` -> **Severity: 424.739** (Blast Radius: 4.579 * Doc Risk: 92.758%)
- `packages/flutter/lib/src/widgets/framework.dart` -> **Severity: 270.171** (Blast Radius: 6.843 * Doc Risk: 39.4813%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2115 literal sites + 118 sites through wrappers = 2233
- **`memory_alloc`:** 3991 literal sites + 31 sites through wrappers = 4022
- **`panics_and_aborts`:** 4605 literal sites + 358 sites through wrappers = 4963

- `ProcessResultMatcher` (function, panics_and_aborts, primitive): 129 call sites in 31 files -- `packages/flutter_tools/test/integration.shard/test_utils.dart`
- `FakeFlutterTestRunner` (function, panics_and_aborts, primitive): 34 call sites in 1 files -- `packages/flutter_tools/test/commands.shard/hermetic/test_test.dart`
- `debugPrint` (function, debug_prints, primitive): 30 call sites in 1 files -- `packages/flutter_tools/test/integration.shard/transition_test_utils.dart`
- `ToolExit` (function, panics_and_aborts, primitive): 24 call sites in 8 files -- `engine/src/flutter/lib/web_ui/dev/exceptions.dart`
- `CannedProcess` (function, panics_and_aborts, primitive): 23 call sites in 6 files -- `engine/src/flutter/tools/engine_tool/test/src/utils.dart`
- `createTempManifestFile` (function, panics_and_aborts, primitive): 14 call sites in 1 files -- `packages/flutter_tools/gradle/src/test/kotlin/tasks/DeepLinkJsonFromManifestTaskTest.kt`
- `log_error` (function, debug_prints, primitive): 14 call sites in 1 files -- `engine/src/flutter/sky/tools/sky_utils.py`
- `_send` (function, debug_prints, primitive): 12 call sites in 1 files -- `packages/flutter_tools/tool/daemon_client.dart`
- `getLegacyAndroidExtension` (function, panics_and_aborts, primitive): 12 call sites in 2 files -- `packages/flutter_tools/gradle/src/main/kotlin/FlutterPluginUtils.kt`
- `failure` (function, debug_prints, primitive): 9 call sites in 1 files -- `dev/customer_testing/lib/runner.dart`
- `exitWithError` (function, panics_and_aborts, primitive): 8 call sites in 5 files -- `dev/tools/localization/localizations_utils.dart`
- `_runString` (function, panics_and_aborts, primitive): 7 call sites in 1 files -- `dev/tools/android_driver_extensions/lib/src/backend/android/adb.dart`
*(+92 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 404299 call pairs -- scoped 25.4%, unique 2.2%, ambiguous 50.9%, external 21.5%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| dart | 252957 | 27.2% | 0.0% | 64.6% | 8.2% |
| cpp | 110592 | 20.3% | 6.7% | 32.7% | 40.3% |
| java | 18107 | 36.7% | 0.3% | 17.7% | 45.3% |
| objective-c | 16872 | 23.7% | 6.7% | 15.9% | 53.6% |
| python | 2218 | 16.1% | 0.0% | 3.0% | 80.9% |
| kotlin | 1706 | 22.2% | 2.4% | 12.7% | 62.7% |
| ruby | 549 | 2.4% | 7.1% | 0.0% | 90.5% |
| swift | 529 | 8.7% | 3.8% | 9.3% | 78.3% |
| shell | 273 | 12.1% | 18.3% | 0.0% | 69.6% |
| javascript | 264 | 25.4% | 0.0% | 3.0% | 71.6% |

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
