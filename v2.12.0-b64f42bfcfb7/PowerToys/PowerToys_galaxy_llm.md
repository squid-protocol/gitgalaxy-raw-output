# ARCHITECTURAL_BRIEF: PowerToys
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/PowerToys.git` |
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
- **Scope:** 4982 analyzed artifact(s), 444614 LOC.
- **Load-bearing artifact:** `src/common/ManagedCommon/Logger.cs` -- 266 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/modules/ZoomIt/ZoomIt/pch.h` -- pulls in 82 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/common/CalculatorEngineCommon/exprtk.hpp` at magnitude 19948.8 (structural weight, not risk).
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
| Total Artifacts | 7751 |
| Analyzed Artifacts (Scanned) | 4982 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2769 |
| Total LOC | 444614 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 64.3% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7508 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1234 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6661 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 504 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 2977 | 249560 | 59.8% |
| CPP | 1265 | 180710 | 25.4% |
| MARKDOWN | 228 | 0 | 4.6% |
| XML | 186 | 428 | 3.7% |
| JSON | 107 | 3852 | 2.1% |
| JAVASCRIPT | 82 | 2605 | 1.6% |
| PLAINTEXT | 48 | 0 | 1.0% |
| MAKEFILE | 34 | 161 | 0.7% |
| POWERSHELL | 27 | 2892 | 0.5% |
| YAML | 14 | 916 | 0.3% |
| HTML | 4 | 206 | 0.1% |
| C | 4 | 598 | 0.1% |
| PYTHON | 4 | 2674 | 0.1% |
| BATCH | 2 | 12 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 1 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2853 |
| utf-8 | bom | 2125 |
| utf-16-le | bom | 3 |
| cp1252 | cp1252-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 25%, Declarative / Non-Code 19%, State Mutators Files 14%, Encapsulated Accessors Files 9%, Large Core Modules (2) 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 4683 | 94.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 276 | 5.5% |
| Static: Minified & Vendor Opaque Mass | 23 | 0.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2769*

**Composition by Extension & Reason:**
- `.png`: 861x Excluded (Explicitly Denied Extension: '.png'), 3x Excluded (Explicitly Denied Extension: '.PNG')
- `.cs`: 406x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 30 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 1576 LOC)
- `.xaml`: 266x Unsupported Format (.xaml), 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 79 exceeds 500 chars)
- `.csproj`: 151x Unsupported Format (.csproj), 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.vcxproj`: 118x Unsupported Format (.vcxproj), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.resx`: 98x Unsupported Format (.resx), 23x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.filters`: 104x Unsupported Format (.filters), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 87x Unsupported Format (.rc), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 70x Excluded (Explicitly Denied Extension: '.ico')
- `.ps1`: 42x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.manifest`: 40x Unsupported Format (.manifest), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Binary Format Detected)
- `.js`: 20x Excluded (Saturation: Line 6 exceeds 500 chars), 15x Statistical Anomaly (Z-Score: -24527.27 < -4.55), 1x Unrecognized Syntax (Dense Structure / Global Regex Timeout)
- `.props`: 28x Unsupported Format (.props), 5x Excluded (Unsupported Extension: '.props'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.wxs`: 33x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 12.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 90.4 | 28.2 | 44.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 25.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.6 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.4 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 34.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.4 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.9 | 90.9 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8021 | 906 | 2 | `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` |
| cleanup | 879 | 336 | 0 | `src/common/CalculatorEngineCommon/exprtk.hpp` |
| guards | 47423 | 2950 | 22 | `src/common/CalculatorEngineCommon/exprtk.hpp` |
| danger | 2302 | 809 | 1 | `src/common/CalculatorEngineCommon/exprtk.hpp` |
| concurrency | 6768 | 715 | 2 | `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` |
| connectivity | 22614 | 3394 | 10 | `src/common/CalculatorEngineCommon/exprtk.hpp` |
| io | 1905 | 405 | 0 | `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 110 | 60 | 0 | `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` |
| time | 532 | 195 | 0 | `src/settings-ui/Settings.UI/SettingsXAML/Controls/Timeline/Timeline.xaml.cs` |
| serialization | 124 | 59 | 0 | `src/settings-ui/Settings.UI.UnitTests/ViewModelTests/PowerPreview.cs` |
| regex | 146 | 52 | 0 | `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.TimeDate/Helpers/TimeAndDateHelper.cs` |
| events | 3484 | 660 | 1 | `src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs` |
| tests | 3822 | 216 | 0 | `src/modules/powerdisplay/PowerDisplay.Lib.UnitTests/MccsCapabilitiesParserTests.cs` |
| docs | 19153 | 1071 | 9 | `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowWalker/Helpers/NativeMethods.cs` |
| debt | 1424 | 294 | 0 | `src/modules/MouseUtils/CursorWrap/CursorWrapTests/analyze_test_results.py` |
| mutation | 105217 | 3109 | 50 | `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` |
| dead_code | 8552 | 2259 | 5 | `src/common/interop/Constants.cpp` |
| credential | 64 | 26 | 0 | `src/common/interop/shared_constants.h` |
| threat | 27 | 10 | 0 | `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Text/PrecomputedFuzzyMatcherEmojiTests.cs` |
| ml_ai | 673 | 147 | 0 | `src/common/ManagedCommon/ColorFormatHelper.cs` |
| ui | 891 | 163 | 0 | `src/settings-ui/Settings.UI/ViewModels/DashboardViewModel.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` (Hits: 87)
- `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` (Hits: 61)
- `src/settings-ui/Settings.UI.Library/SettingsBackupAndRestoreUtils.cs` (Hits: 57)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Logger.cs** (`src/common/ManagedCommon/Logger.cs`) — 266 inbound connections
2. **Microsoft.CommandPalette.Extensions.def** (`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions/Microsoft.CommandPalette.Extensions.def`) — 229 inbound connections
3. **logger.h** (`src/common/logger/logger.h`) — 194 inbound connections
4. **Input.h** (`src/modules/keyboardmanager/common/Input.h`) — 111 inbound connections
5. **CommandResult.cs** (`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/CommandResult.cs`) — 105 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pch.h** (`src/modules/ZoomIt/ZoomIt/pch.h`) — 82 outbound dependencies
2. **pch.h** (`src/modules/cmdpal/Microsoft.Terminal.UI/pch.h`) — 52 outbound dependencies
3. **pch.h** (`src/modules/MeasureTool/MeasureToolCore/pch.h`) — 51 outbound dependencies
4. **CaptureFrameWait.h** (`src/modules/ZoomIt/ZoomIt/CaptureFrameWait.h`) — 50 outbound dependencies
5. **main.cpp** (`src/runner/main.cpp`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `FindBestFrameShiftVerticalOnly` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **2141.3** | LOC: 2011
- `RunPanoramaStitchSelfTest` **(I/O & Config Routines)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **1735.3** | LOC: 6967
  * *Intent:* // next to the solution root (i.e. <repo>\Debug\). // 3. Run: ZoomIt64a.exe /panorama-selftest // Optional stress targeting: // - /panorama-selftest-s...
- `StitchPanoramaFrames` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **1361.2** | LOC: 2783
- `BuildFixedOverlayMask` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **730.9** | LOC: 817
- `MainWndProc` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **724.4** | LOC: 1340
  * *Intent:* //---------------------------------------------------------------------------- // // MainWndProc // //------------------------------------------------...
- `VideoRecordingSession::TrimDialogProc` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **521.3** | LOC: 1302
  * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingSession::TrimDialogProc // // Dialog procedure for ...
- `HandleShortcutRemapEvent` **(Many-Argument Workhorses)** (@ `src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardEventHandlers.cpp`) -> Impact: **505.1** | LOC: 756
  * *Intent:* */ // Function to handle a shortcut remap
- `OptionsProc` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **461.1** | LOC: 860
  * *Intent:* //---------------------------------------------------------------------------- // // OptionsProc // //------------------------------------------------...
- `FindBestFrameShift` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **428.1** | LOC: 482
- `LogStitchedBandDiagnostics` **(Many-Argument Workhorses)** (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **336.0** | LOC: 304
  * *Intent:* // Detect visually dark stitched bands even when the canvas has no unwritten // gaps so we can correlate full-width artifacts with a specific frame ha...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/modules/ZoomIt/ZoomIt` | 29 | 28435.96 | 25.3% | 12.66% |
| `src/common/CalculatorEngineCommon` | 11 | 20061.5 | 4.65% | 12.86% |
| `src/settings-ui/Settings.UI/ViewModels` | 43 | 7757.74 | 25.74% | 17.01% |
| `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels` | 94 | 6027.09 | 19.33% | 28.23% |
| `src/modules/MouseWithoutBorders/App/Core` | 29 | 4858.08 | 37.93% | 21.81% |
| `src/settings-ui/Settings.UI.Library` | 153 | 4734.58 | 5.69% | 40.81% |
| `src/modules/fancyzones/FancyZonesLib` | 70 | 4700.4 | 17.18% | 30.21% |
| `src/modules/powerrename/lib` | 40 | 4606.82 | 22.68% | 17.97% |
| `src/modules/MouseWithoutBorders/App/Class` | 16 | 3835.06 | 43.58% | 27.75% |
| `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit` | 74 | 3303.74 | 15.33% | 30.33% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/common/GPOWrapperProjection/GPOWrapper.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/By.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/Window.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/AdvancedPaste/Helpers/KernelExtensions.cs` -> **100.0%** Exposure
- `src/modules/PowerOCR/PowerOCR/Helpers/OSInterop.cs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/review-tools/Get-PrIncrementalChanges.ps1` -> **100.0%** Exposure
- `.github/skills/winmd-api-search/scripts/Invoke-WinMdQuery.ps1` -> **100.0%** Exposure
- `.github/skills/winmd-api-search/scripts/Update-WinMdCache.ps1` -> **100.0%** Exposure
- `src/PackageIdentity/BuildSparsePackage.ps1` -> **100.0%** Exposure
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/Capture-MonitorLayout.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/common/CalculatorEngineCommon/exprtk.hpp` -> **0** Orphaned Functions | **143** Duplicates
- `src/common/interop/Constants.cpp` -> **73** Orphaned Functions | **0** Duplicates
- `src/common/GPOWrapper/GPOWrapper.cpp` -> **72** Orphaned Functions | **0** Duplicates
- `src/modules/cmdpal/Tests/Microsoft.CommandPalette.Extensions.Toolkit.UnitTests/ListHelpersInPlaceUpdateTests.cs` -> **51** Orphaned Functions | **0** Duplicates
- `src/modules/keyboardmanager/KeyboardManagerEditorUI/Controls/UnifiedMappingControl.xaml.cs` -> **48** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/InternalPage.SampleData.cs` -> **100.0%** Exposure
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Services/Sanitizer/ErrorReportSanitizerTests.TestData.cs` -> **99.9891%** Exposure
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Services/Sanitizer/SecretKeyValueRulesProviderTests.cs` -> **82.1257%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `52` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `18439` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/common/CalculatorEngineCommon/exprtk.hpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.552)
- **Top Global Matches:** file_cluster_4: 9.552, file_cluster_15: 11.349, file_cluster_16: 12.343
- **Magnitude:** 19948.8 | **LOC:** 46252 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **24**; blast radius 0.934; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (63.9%), Guard Balance (formerly Safety Score) (56.2%), Connectivity (formerly Api Exposure) (43.4%)
- **Documentation Coverage:** 78.8% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process` **(Many-Argument Workhorses)** (Impact: 189.1)
  * `parse_expression` **(Compute Cores)** (Impact: 175.3)
  * `parse_define_vector_statement` **(Compute Cores)** (Impact: 156.8)
    * *Intent:* #endif
  * `process` **(Many-Argument Workhorses)** (Impact: 152.1)
  * `process` **(Many-Argument Workhorses)** (Impact: 140.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 1431 instances
* *Memory Alloc (weighted view):* 86
* *State Mutation (weighted view):* 4961
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6311`, `structural_boundaries: 12297`, `args: 1450`, `func_start: 2034`, `class_start: 616`
* *Risk/State:* `safety_bypasses: 64`, `state_mutation: 2099`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 143`
* *Architecture:* `io: 18`, `api: 403`, `import: 20`
* *Defense:* `safety: 213`, `immutability_locks: 4966`, `cleanup: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.934
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.009436
  * `Imports (Out-Degree: 2):` algorithm, cassert, cctype, cmath, cstdio, cstdlib, cstring, ctime...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.234)
- **Top Global Matches:** file_cluster_8: 9.234, file_cluster_6: 11.382, file_cluster_4: 19.108
- **Magnitude:** 15684.82 | **LOC:** 18014 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FindBestFrameShiftVerticalOnly` **(Many-Argument Workhorses)** (Impact: 2141.3)
  * `RunPanoramaStitchSelfTest` **(I/O & Config Routines)** (Impact: 1735.3)
    * *Intent:* // next to the solution root (i.e. <repo>\Debug\). // 3. Run: ZoomIt64a.exe /panorama-selftest // Op...
  * `StitchPanoramaFrames` **(Many-Argument Workhorses)** (Impact: 1361.2)
  * `BuildFixedOverlayMask` **(Many-Argument Workhorses)** (Impact: 730.9)
  * `FindBestFrameShift` **(Many-Argument Workhorses)** (Impact: 428.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 1929 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 6534
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3703`, `structural_boundaries: 484`, `args: 607`, `func_start: 83`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 2676`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 11`
* *Architecture:* `io: 43`, `api: 1`, `concurrency: 3`, `import: 15`
* *Defense:* `safety: 8`, `immutability_locks: 1998`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 10):` PanoramaCapture.h, Utility.h, WindowsVersions.h, arm_neon.h, atomic, cmath, commctrl.h, emmintrin.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.03)
- **Top Global Matches:** file_cluster_6: 7.03, file_cluster_4: 8.264, file_cluster_15: 16.071
- **Magnitude:** 6686.36 | **LOC:** 11756 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 23.1%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **22**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (85.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MainWndProc` **(Many-Argument Workhorses)** (Impact: 724.4)
    * *Intent:* //---------------------------------------------------------------------------- // // MainWndProc // ...
  * `OptionsProc` **(Many-Argument Workhorses)** (Impact: 461.1)
    * *Intent:* //---------------------------------------------------------------------------- // // OptionsProc // ...
  * `LiveZoomWndProc` **(Many-Argument Workhorses)** (Impact: 320.4)
    * *Intent:* //---------------------------------------------------------------------------- // // LiveZoomWndProc...
  * `wWinMain` **(Many-Argument Workhorses)** (Impact: 201.6)
    * *Intent:* #endif //---------------------------------------------------------------------------- // // WinMain ...
  * `AdvancedBreakProc` **(Many-Argument Workhorses)** (Impact: 175.0)
    * *Intent:* //---------------------------------------------------------------------------- // // AdvancedBreakPr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 726 instances
* *Concurrency (weighted view):* 90
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 2581
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2101`, `structural_boundaries: 395`, `args: 855`, `func_start: 122`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1129`, `dead_code: 46`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 10`, `api: 18`, `concurrency: 20`, `import: 23`
* *Defense:* `safety: 28`, `doc: 4`, `immutability_locks: 100`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 35):` trace.h, BreakTimer.h, GifRecordingSession.h, PanoramaCapture.h, Utility.h, WindowsVersions.h, ZoomItSettings.h, array...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.919)
- **Top Global Matches:** file_cluster_6: 5.919, file_cluster_4: 10.021, file_cluster_8: 15.433
- **Magnitude:** 3089.02 | **LOC:** 5443 | **CtrlFlow:** 17.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 0.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.7%), Guard Balance (formerly Safety Score) (59.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VideoRecordingSession::TrimDialogProc` **(Many-Argument Workhorses)** (Impact: 521.3)
    * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingS...
  * `TimelineSubclassProc` **(Many-Argument Workhorses)** (Impact: 253.7)
  * `StartPlaybackAsync` **(Many-Argument Workhorses)** (Impact: 143.6)
  * `LoadGifFrames` **(Many-Argument Workhorses)** (Impact: 105.6)
  * `UpdateVideoPreview` **(Many-Argument Workhorses)** (Impact: 93.0)
    * *Intent:* //---------------------------------------------------------------------------- // // Helper: Update ...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 253 instances
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 907
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 772`, `structural_boundaries: 362`, `args: 273`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 401`, `unreferenced_by_name: 22`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 32`, `import: 10`
* *Defense:* `safety: 80`, `sync_locks: 33`, `immutability_locks: 371`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000267
  * `Imports (Out-Degree: 9):` CaptureFrameWait.h, Utility.h, VideoRecordingSession.h, cstdlib, filesystem, mmsystem.h, pch.h, shlwapi.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.238)
- **Top Global Matches:** file_cluster_4: 7.238, file_cluster_6: 10.33, file_cluster_12: 12.226
- **Magnitude:** 2235.8 | **LOC:** 2376 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.219; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.6%)
- **Documentation Coverage:** 9.7403% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_analyze_wrap_problem` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* """ Analyze why a wrap destination doesn't exist for a given edge range. This provides detailed diag...
  * `_show_segment_detail` **(Many-Argument Workhorses)** (Impact: 56.1)
    * *Intent:* """Show detailed information about a segment in a popup."""
  * `find_nearest_opposite_edge` **(Many-Argument Workhorses)** (Impact: 50.6)
  * `_update_info_panel` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* """Update the info panel with loaded data."""
  * `_draw_cursor_position` **(Many-Argument Workhorses)** (Impact: 35.6)
    * *Intent:* """Draw cursor position on canvas."""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 372 instances
* *State Mutation (weighted view):* 1307
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 182`, `args: 64`, `func_start: 63`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 563`
* *Architecture:* `io: 3`, `api: 25`, `import: 10`
* *Defense:* `safety: 4`, `doc: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.219
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 0):` argparse, csv, dataclasses, enum, json, re, sys, tkinter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.956)
- **Top Global Matches:** file_cluster_4: 5.956, file_cluster_16: 9.593, file_cluster_15: 10.938
- **Magnitude:** 1576.56 | **LOC:** 2914 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **21**; blast radius 0.166; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (48.0%)
- **Documentation Coverage:** 77.6316% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Canvas_PaintSurface` **(Many-Argument Workhorses)** (Impact: 147.0)
  * `OnKeyDown` **(I/O & Config Routines)** (Impact: 84.7)
    * *Intent:* /// <inheritdoc/>
  * `ReadFormattedData` **(I/O & Config Routines)** (Impact: 56.9)
  * `CalculateDataColumnCharWidth` **(I/O & Config Routines)** (Impact: 55.4)
  * `DrawSelectionGeometry` **(Many-Argument Workhorses)** (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 719
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 180`, `args: 121`, `func_start: 68`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 289`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 73`, `import: 21`
* *Defense:* `safety: 69`, `doc: 190`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.166
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00032
  * `Imports (Out-Degree: 3):` Microsoft.UI, Microsoft.UI.Input, Microsoft.UI.Xaml, Microsoft.UI.Xaml.Controls, Microsoft.UI.Xaml.Controls.Primitives, Microsoft.UI.Xaml.Input, Microsoft.UI.Xaml.Media, RegistryPreviewUILib.HexBox.Library.EndianConvert...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.832)
- **Top Global Matches:** file_cluster_6: 5.832, file_cluster_4: 12.17, file_cluster_8: 12.922
- **Magnitude:** 1235.88 | **LOC:** 2131 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **19**; blast radius 0.328; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (55.3%), Guard Balance (formerly Safety Score) (52.3%), Concurrency Surface (formerly Concurrency) (31.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MainTCPRoutine` **(Many-Argument Workhorses)** (Impact: 115.2)
  * `SocketStuff` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `UpdateTcpSockets` **(Many-Argument Workhorses)** (Impact: 51.5)
  * `StartNewTcpClient` **(Many-Argument Workhorses)** (Impact: 44.4)
  * `ClientThread` **(Compute Cores)** (Impact: 43.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 128 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 449
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 101`, `args: 50`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `state_mutation: 193`, `dead_code: 5`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 32`, `concurrency: 15`, `import: 19`
* *Defense:* `safety: 184`, `sync_locks: 12`, `immutability_locks: 9`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.328
  * `Choke Point (Betweenness):` 3.1e-05 | `Ripple Effect (Closeness):` 0.00956
  * `Imports (Out-Degree: 17):` MouseWithoutBorders.Core, MouseWithoutBorders.Core.Clipboard, MouseWithoutBorders.Core.Thread, MouseWithoutBorders.Exceptions, System, System.Collections.Concurrent, System.Collections.Generic, System.Diagnostics...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardEventHandlers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.884)
- **Top Global Matches:** file_cluster_6: 5.884, file_cluster_4: 10.004, file_cluster_8: 15.486
- **Magnitude:** 1155.38 | **LOC:** 1805 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.9%), Guard Balance (formerly Safety Score) (57.6%)
- **Documentation Coverage:** 96.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HandleShortcutRemapEvent` **(Many-Argument Workhorses)** (Impact: 505.1)
    * *Intent:* */ // Function to handle a shortcut remap
  * `ShowProgram` **(Many-Argument Workhorses)** (Impact: 68.8)
  * `HandleSingleKeyRemapEvent` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* // Function to handle a single key remap
  * `CreateOrShowProcessForShortcut` **(Compute Cores)** (Impact: 35.9)
  * `ResetChordsIfNeeded` **(Many-Argument Workhorses)** (Impact: 32.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 10
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 130`, `args: 142`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 91`, `dead_code: 13`, `unreferenced_by_name: 4`
* *Architecture:* `io: 1`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 12`, `doc: 1`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` KeyboardEventHandlers.h, TlHelp32.h, chrono, shared_constants.h, elevation.h, future, trace.h, Helpers.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmMatrix.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.091)
- **Top Global Matches:** file_cluster_16: 6.091, file_cluster_4: 8.026, file_cluster_15: 8.614
- **Magnitude:** 941.44 | **LOC:** 1238 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 0.125; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (97.8%), Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HelperTimer_Tick` **(Many-Argument Workhorses)** (Impact: 44.3)
  * `FrmMatrix_Load` **(Many-Argument Workhorses)** (Impact: 43.9)
  * `Form_DragOver` **(Many-Argument Workhorses)** (Impact: 27.9)
  * `ButtonOK_Click` **(Many-Argument Workhorses)** (Impact: 23.9)
  * `LoadMachines` **(I/O & Config Routines)** (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 144 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 527
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 23`, `args: 59`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 239`, `dead_code: 10`, `unreferenced_by_name: 37`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 6`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.125
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000267
  * `Imports (Out-Degree: 13):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, MouseWithoutBorders.Core, MouseWithoutBorders.Core.Clipboard, System, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Drawing...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ZoomIt/ZoomIt/DemoType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.965)
- **Top Global Matches:** file_cluster_6: 5.965, file_cluster_4: 8.952, file_cluster_8: 16.332
- **Magnitude:** 886.4 | **LOC:** 1446 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 0.122; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.4%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (66.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DemoTypeHookProc` **(Many-Argument Workhorses)** (Impact: 83.2)
    * *Intent:* //---------------------------------------------------------------------------- // // DemoTypeHookPro...
  * `InjectByClipboard` **(Many-Argument Workhorses)** (Impact: 41.3)
    * *Intent:* //---------------------------------------------------------------------------- // // InjectByClipboa...
  * `StartDemoType` **(Many-Argument Workhorses)** (Impact: 31.4)
    * *Intent:* //---------------------------------------------------------------------------- // // StartDemoType /...
  * `HandleControlKeyword` **(I/O & Config Routines)** (Impact: 31.2)
    * *Intent:* //---------------------------------------------------------------------------- // // HandleControlKe...
  * `GetDemoTypeFile` **(Compute Cores)** (Impact: 30.9)
    * *Intent:* //---------------------------------------------------------------------------- // // GetDemoTypeFile...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 63
* *State Mutation (weighted view):* 349
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 82`, `args: 97`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `state_mutation: 119`, `dead_code: 4`, `unreferenced_by_name: 2`
* *Architecture:* `io: 1`, `concurrency: 13`, `import: 2`
* *Defense:* `safety: 16`, `sync_locks: 19`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000267
  * `Imports (Out-Degree: 3):` DemoType.h, pch.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.771)
- **Top Global Matches:** file_cluster_4: 5.771, file_cluster_6: 9.853, file_cluster_15: 11.383
- **Magnitude:** 857.24 | **LOC:** 948 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **11**; blast radius 0.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `D2DOverlayWindow::render` **(Compute Cores)** (Impact: 122.4)
  * `D2DOverlayWindow::show` **(Many-Argument Workhorses)** (Impact: 36.2)
  * `get_window_state` **(Compute Cores)** (Impact: 30.8)
  * `render_arrow` **(Many-Argument Workhorses)** (Impact: 28.3)
  * `D2DOverlaySVG::get_thumbnail_rect_and_scale` **(Many-Argument Workhorses)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 141 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 490
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 93`, `args: 101`, `func_start: 31`
* *Risk/State:* `state_mutation: 208`, `unreferenced_by_name: 28`
* *Architecture:* `concurrency: 2`, `import: 11`
* *Defense:* `safety: 1`, `sync_locks: 12`, `immutability_locks: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.129
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00032
  * `Imports (Out-Degree: 16):` resource.h, monitors.h, MsWindowsSettings.h, resources.h, window.h, overlay_window.h, pch.h, shortcut_guide.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.0)
- **Top Global Matches:** file_cluster_16: 8.0, file_cluster_4: 8.821, file_cluster_10: 9.401
- **Magnitude:** 856.68 | **LOC:** 1485 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (45.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Complexity Load (formerly Cognitive Load) (31.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ShouldReplacePasteAIConfiguration` **(Defensive Guards)** (Impact: 93.7)
  * `OnCustomActionsCollectionChanged` **(Stateful Encapsulated Methods)** (Impact: 24.7)
  * `AdvancedPasteViewModel` **(Defensive Guards)** (Impact: 23.0)
  * `MigrateLegacyAIEnablement` **(I/O & Config Routines)** (Impact: 21.1)
  * `OnPasteAIProvidersCollectionChanged` **(Stateful Encapsulated Methods)** (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 190`, `args: 113`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `unreferenced_by_name: 13`
* *Architecture:* `api: 44`, `import: 19`
* *Defense:* `safety: 212`, `doc: 4`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Microsoft.PowerToys.Settings.UI.Helpers, Microsoft.PowerToys.Settings.UI.Library, Microsoft.PowerToys.Settings.UI.Library.Helpers, Microsoft.PowerToys.Settings.UI.Library.Interfaces, Microsoft.PowerToys.Settings.UI.Library.Utilities, Microsoft.PowerToys.Settings.UI.SerializationContext, Microsoft.UI.Dispatching, Microsoft.Win32...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/WICMetadataExtractor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_8: 6.263, file_cluster_6: 15.844, file_cluster_3: 21.421
- **Magnitude:** 850.62 | **LOC:** 1116 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (70.9%), Guard Balance (formerly Safety Score) (65.3%), Debt Markers (formerly Tech Debt) (43.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WICMetadataExtractor::ReadDouble` **(Many-Argument Workhorses)** (Impact: 94.6)
  * `ParseIso8601DateTime` **(Compute Cores)** (Impact: 80.8)
  * `ValidateAndBuildSystemTime` **(Many-Argument Workhorses)** (Impact: 49.5)
  * `WICMetadataExtractor::ExtractAllEXIFFields` **(Many-Argument Workhorses)** (Impact: 43.2)
  * `WICMetadataExtractor::ReadDateTime` **(Compute Cores)** (Impact: 36.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 122`, `args: 35`, `func_start: 25`
* *Risk/State:* `state_mutation: 155`, `unreferenced_by_name: 20`
* *Architecture:* `concurrency: 2`, `import: 9`
* *Defense:* `safety: 9`, `sync_locks: 4`, `immutability_locks: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` MetadataFormatHelper.h, WICMetadataExtractor.h, algorithm, comdef.h, cwctype, iomanip, pch.h, shlwapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/settings-ui/Settings.UI/SettingsXAML/Views/AdvancedPastePage.xaml.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.413)
- **Top Global Matches:** file_cluster_4: 7.413, file_cluster_16: 7.79, file_cluster_10: 9.558
- **Magnitude:** 838.36 | **LOC:** 1168 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 28.6%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (59.4%), Complexity Load (formerly Cognitive Load) (57.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `RestoreFoundrySelection` **(Defensive Guards)** (Impact: 29.6)
  * `UpdatePasteAIUIVisibility` **(I/O & Config Routines)** (Impact: 28.9)
  * `FoundryLocalPicker_SelectionChanged` **(Defensive Guards)** (Impact: 27.7)
  * `PasteAIProviderConfigurationDialog_PrimaryButtonClick` **(Stateful Encapsulated Methods)** (Impact: 21.1)
  * `UpdateFoundryLocalUIAsync` **(Defensive Guards)** (Impact: 17.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 91 instances
* *Concurrency (weighted view):* 73
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 174`, `args: 97`, `func_start: 61`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 143`, `unreferenced_by_name: 27`
* *Architecture:* `io: 1`, `api: 26`, `concurrency: 23`, `import: 18`
* *Defense:* `safety: 125`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` LanguageModelProvider, Microsoft.PowerToys.Settings.UI.Controls, Microsoft.PowerToys.Settings.UI.Helpers, Microsoft.PowerToys.Settings.UI.Library, Microsoft.PowerToys.Settings.UI.ViewModels, Microsoft.UI.Xaml, Microsoft.UI.Xaml.Controls, Microsoft.UI.Xaml.Media...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/Common.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.603)
- **Top Global Matches:** file_cluster_16: 5.603, file_cluster_12: 8.355, file_cluster_15: 8.364
- **Magnitude:** 817.32 | **LOC:** 1655 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **27** in-repo importer(s); it depends on **21**; blast radius 2.518; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.5%), Complexity Load (formerly Cognitive Load) (40.3%)
- **Documentation Coverage:** 98.4% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SkSend` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* #endif
  * `ExecuteAndTrace` **(Many-Argument Workhorses)** (Impact: 21.4)
  * `ShowToolTip` **(Stateful Encapsulated Methods)** (Impact: 20.9)
  * `InvokeInFormThread` **(Many-Argument Workhorses)** (Impact: 16.0)
  * `GetRemoteStringIP` **(Defensive Guards)** (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 72 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 258
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 134`, `args: 113`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 114`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 13`, `api: 107`, `concurrency: 15`, `import: 21`
* *Defense:* `safety: 60`, `doc: 4`, `sync_locks: 22`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.518
  * `Choke Point (Betweenness):` 0.000363 | `Ripple Effect (Closeness):` 0.011969
  * `Imports (Out-Degree: 17):` Microsoft.PowerToys.Settings.UI.Library, MouseWithoutBorders.Class, MouseWithoutBorders.Core.Clipboard, MouseWithoutBorders.Core.Thread, MouseWithoutBorders.Exceptions, System, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 27):` (Excluded from Brief to save tokens)

### `src/modules/powerrename/lib/Helpers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.236)
- **Top Global Matches:** file_cluster_4: 5.236, file_cluster_6: 8.673, file_cluster_15: 11.945
- **Magnitude:** 812.2 | **LOC:** 927 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **10**; blast radius 0.313; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (91.3%), Guard Balance (formerly Safety Score) (67.7%), Debt Markers (formerly Tech Debt) (37.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetTransformedFileName` **(Many-Argument Workhorses)** (Impact: 198.7)
  * `GetEnumeratedFileName` **(Many-Argument Workhorses)** (Impact: 135.1)
  * `GetMetadataFileName` **(Many-Argument Workhorses)** (Impact: 37.7)
  * `GetDatedFileName` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `isMetadataUsed` **(Many-Argument Workhorses)** (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 282
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 188`, `structural_boundaries: 45`, `args: 58`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `import: 10`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.313
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.002552
  * `Imports (Out-Degree: 5):` Helpers.h, MetadataTypes.h, ShlGuid.h, algorithm, cstring, filesystem, pch.h, regex...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/modules/MouseWithoutBorders/App/Form/frmScreen.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.333)
- **Top Global Matches:** file_cluster_4: 6.333, file_cluster_6: 10.324, file_cluster_16: 10.782
- **Magnitude:** 774.18 | **LOC:** 1227 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **13**; blast radius 0.152; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (95.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HelperTimer_Tick` **(Many-Argument Workhorses)** (Impact: 109.9)
  * `WndProc` **(I/O & Config Routines)** (Impact: 46.2)
    * *Intent:* // private bool checkClipboard = false;
  * `PaintMyNameOnDesktop` **(I/O & Config Routines)** (Impact: 26.6)
  * `ShowMessageOnLogonDesktop` **(Stateful Encapsulated Methods)** (Impact: 18.3)
  * `ChangeIcon` **(I/O & Config Routines)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 105 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 24`, `args: 35`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 161`, `dead_code: 18`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 25`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.152
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.0002
  * `Imports (Out-Degree: 19):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, MouseWithoutBorders.Core, MouseWithoutBorders.Properties, System, System.ComponentModel, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.Utilities.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.263)
- **Top Global Matches:** file_cluster_4: 5.263, file_cluster_6: 10.237, file_cluster_16: 10.315
- **Magnitude:** 761.58 | **LOC:** 1198 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **16**; blast radius 0.315; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (89.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.6%)
- **Documentation Coverage:** 11.5385% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseRegistryFile` **(Many-Argument Workhorses)** (Impact: 156.8)
    * *Intent:* /// <summary> /// Parses the text that is passed in, which should be the same text that's in editor ...
  * `AddTextToTree` **(Many-Argument Workhorses)** (Impact: 37.8)
    * *Intent:* /// <summary> /// Helper method that creates a new TreeView node, attaches it to a parent if any, an...
  * `HandleDirtyClosing` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* /// <summary> /// Wrapper method that shows a Save/Don't Save/Cancel message box, parented by the ma...
  * `SetValueToolTip` **(Stateful Encapsulated Methods)** (Impact: 18.1)
    * *Intent:* /// <summary> /// Loads a string for a given Value's image in the grid, based off the current type a...
  * `GetFolderToolTip` **(Stateful Encapsulated Methods)** (Impact: 12.2)
    * *Intent:* /// <summary> /// Loads and returns a string for a given Key's image in the tree, based off the curr...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 103 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 60`, `args: 27`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 155`, `dead_code: 2`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 14`, `import: 16`
* *Defense:* `safety: 27`, `doc: 73`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.315
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.0006
  * `Imports (Out-Degree: 5):` Microsoft.UI.Input, Microsoft.UI.Xaml, Microsoft.UI.Xaml.Controls, System, System.Collections, System.Collections.Generic, System.Diagnostics, System.Globalization...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/monitor_layout_tests.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.087)
- **Top Global Matches:** file_cluster_5: 8.087, file_cluster_12: 9.207, file_cluster_4: 10.63
- **Magnitude:** 757.2 | **LOC:** 893 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.118; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (45.5%)
- **Documentation Coverage:** 23.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_print_layout_diagram` **(Many-Argument Workhorses)** (Impact: 63.2)
    * *Intent:* """Print a text-based diagram of the monitor layout"""
  * `_run_test_config` **(Many-Argument Workhorses)** (Impact: 33.7)
  * `_is_outer_edge` **(Stateful Encapsulated Methods)** (Impact: 17.4)
    * *Intent:* """ Determine if an edge is "outer" (can wrap) Rules: 1. If edge has an adjacent opposite edge (with...
  * `_get_test_points_on_edge` **(Stateful Encapsulated Methods)** (Impact: 17.0)
  * `_wrap_from_edge` **(Stateful Encapsulated Methods)** (Impact: 16.7)
    * *Intent:* """Calculate wrap destination from an outer edge"""
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 104`, `args: 38`, `func_start: 36`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 153`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 22`, `import: 6`
* *Defense:* `safety: 3`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` argparse, dataclasses, enum, json, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.554)
- **Top Global Matches:** file_cluster_4: 6.554, file_cluster_16: 9.653, file_cluster_15: 11.037
- **Magnitude:** 727.88 | **LOC:** 1231 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 54.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (79.1%), Guard Balance (formerly Safety Score) (53.8%), Complexity Load (formerly Cognitive Load) (41.0%)
- **Documentation Coverage:** 90.566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TrySetSelectionAfterUpdate` **(Many-Argument Workhorses)** (Impact: 57.1)
    * *Intent:* /// <summary> /// Applies selection after an items update. Returns false if ItemView.Items /// is no...
  * `HandleGridArrowNavigation` **(Compute Cores)** (Impact: 45.8)
    * *Intent:* // Find a logical neighbor in the requested direction using containers' positions.
  * `CalculateTargetIndexPageUpDownScrollTo` **(Compute Cores)** (Impact: 34.6)
    * *Intent:* /// <summary> /// Calculates the item index to target when performing a page up or page down /// nav...
  * `Items_PreviewKeyDown` **(Stateful Encapsulated Methods)** (Impact: 20.4)
  * `Items_ItemClick` **(Stateful Encapsulated Methods)** (Impact: 15.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Api Near Db Sink:* 2 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 195`, `structural_boundaries: 160`, `args: 67`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 97`, `doc: 30`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` CommunityToolkit.Mvvm.Messaging, ManagedCommon, Microsoft.CmdPal.UI.Helpers, Microsoft.CmdPal.UI.Messages, Microsoft.CmdPal.UI.ViewModels, Microsoft.CmdPal.UI.ViewModels.Commands, Microsoft.CmdPal.UI.ViewModels.Messages, Microsoft.CmdPal.UI.ViewModels.Services...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.236)
- **Top Global Matches:** file_cluster_6: 8.236, file_cluster_8: 8.397, file_cluster_4: 16.53
- **Magnitude:** 711.22 | **LOC:** 1123 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **9**; blast radius 0.784; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.9%), Complexity Load (formerly Cognitive Load) (54.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MoveRight` **(Many-Argument Workhorses)** (Impact: 67.6)
    * *Intent:* #endif
  * `MoveLeft` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `MoveToMyNeighbourIfNeeded` **(Compute Cores)** (Impact: 60.6)
    * *Intent:* #if OLD_VERSION
  * `MoveToMyNeighbourIfNeeded` **(Many-Argument Workhorses)** (Impact: 50.0)
    * *Intent:* /* Let's say we have 3 machines A, B, and C. A is the controller machine. * (x, y) is the current Mo...
  * `MoveUp` **(Many-Argument Workhorses)** (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 241
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 211`, `structural_boundaries: 86`, `args: 39`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 87`, `dead_code: 5`, `unreferenced_by_name: 10`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 3`, `sync_locks: 4`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.784
  * `Choke Point (Betweenness):` 1.7e-05 | `Ripple Effect (Closeness):` 0.009693
  * `Imports (Out-Degree: 8):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, System, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Drawing, System.Linq, System.Threading...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/FuzzyStringMatcher.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.763)
- **Top Global Matches:** file_cluster_16: 6.763, file_cluster_4: 7.928, file_cluster_15: 8.091
- **Magnitude:** 707.08 | **LOC:** 1095 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **5**; blast radius 1.919; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.2%), Complexity Load (formerly Cognitive Load) (43.0%)
- **Documentation Coverage:** 90.1639% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ScoreNonContiguousWithPositions` **(Many-Argument Workhorses)** (Impact: 59.3)
    * *Intent:* // ============================================================ // Non-contiguous matching (with pos...
  * `ScoreBestVariantWithPositions` **(Many-Argument Workhorses)** (Impact: 37.6)
  * `ScoreNonContiguous` **(Many-Argument Workhorses)** (Impact: 33.3)
    * *Intent:* // ============================================================ // Non-contiguous matching (score on...
  * `FoldForComparison` **(Compute Cores)** (Impact: 23.6)
    * *Intent:* /// <summary> /// Creates a folded string for fast equality comparisons: /// - ALWAYS normalizes sla...
  * `ScoreContiguous` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* // ============================================================ // Contiguous matching // ==========...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 79 instances
* *State Mutation (weighted view):* 247
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 227`, `args: 49`, `func_start: 40`, `class_start: 9`
* *Risk/State:* `state_mutation: 89`, `unreferenced_by_name: 2`
* *Architecture:* `api: 42`, `import: 5`
* *Defense:* `safety: 17`, `doc: 21`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.919
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005623
  * `Imports (Out-Degree: 0):` System.Buffers, System.Globalization, System.Runtime.CompilerServices, System.Text, ToolGood.Words.Pinyin
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/modules/powerrename/lib/PowerRenameManager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.929)
- **Top Global Matches:** file_cluster_15: 5.929, file_cluster_11: 7.674, file_cluster_12: 7.707
- **Magnitude:** 705.18 | **LOC:** 1207 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 0.156; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (67.0%), Guard Balance (formerly Safety Score) (64.1%), Complexity Load (formerly Cognitive Load) (47.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CPowerRenameManager::s_fileOpWorkerThread` **(Compute Cores)** (Impact: 38.5)
  * `CPowerRenameManager::_WndProc` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `CPowerRenameManager::_PerformFileOperation` **(I/O & Config Routines)** (Impact: 13.7)
  * `CPowerRenameManager::UpdateChildrenPath` **(Compute Cores)** (Impact: 12.2)
  * `CPowerRenameManager::SetVisible` **(I/O & Config Routines)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 84`, `args: 56`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 113`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 64`, `import: 9`
* *Defense:* `safety: 2`, `sync_locks: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.156
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.0006
  * `Imports (Out-Degree: 10):` PowerRenameManager.h, PowerRenameRegEx.h, Renaming.h, algorithm, cstring, helpers.h, pch.h, shlobj.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.043)
- **Top Global Matches:** file_cluster_8: 6.043, file_cluster_6: 13.707, file_cluster_4: 22.36
- **Magnitude:** 700.08 | **LOC:** 827 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.8%), Guard Balance (formerly Safety Score) (69.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MonitorTopology::IsOnOuterEdge` **(Many-Argument Workhorses)** (Impact: 96.9)
  * `MonitorTopology::FindNearestOppositeEdge` **(Many-Argument Workhorses)** (Impact: 64.0)
  * `MonitorTopology::GetWrapDestination` **(Many-Argument Workhorses)** (Impact: 50.4)
  * `MonitorTopology::PrioritizeEdgeByDirection` **(Compute Cores)** (Impact: 48.4)
  * `MonitorTopology::FindOppositeOuterEdge` **(Compute Cores)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 65`, `args: 35`, `func_start: 17`
* *Risk/State:* `state_mutation: 111`, `unreferenced_by_name: 17`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` logger.h, CursorWrapCore.h, MonitorTopology.h, algorithm, cmath, pch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.978)
- **Top Global Matches:** file_cluster_4: 7.978, file_cluster_12: 10.057, file_cluster_7: 11.916
- **Magnitude:** 671.48 | **LOC:** 752 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.118; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.8%), Debt Markers (formerly Tech Debt) (81.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetShortcutRemapByType` **(Many-Argument Workhorses)** (Impact: 138.4)
  * `GetShortcutRemapCountByType` **(Many-Argument Workhorses)** (Impact: 67.2)
  * `AddShortcutRemap` **(Many-Argument Workhorses)** (Impact: 55.0)
  * `GetShortcutRemap` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `DeleteShortcutRemap` **(Many-Argument Workhorses)** (Impact: 20.4)
    * *Intent:* // Function to delete a shortcut remapping
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 153`, `structural_boundaries: 99`, `args: 73`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 104`, `unreferenced_by_name: 25`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` KeyboardManagerEditorLibraryWrapper.h, algorithm, keyboard_layout.h, logger_helper.h, cstring, KeyboardManagerEditor.h, EditorHelpers.h, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/modules/Workspaces/WorkspacesLib/Result.h` (CPP) | Magnitude: 27.38 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 21, immutability_locks: 16, func_start: 12
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.ClipboardHistory/Helpers/Analyzers/ImageMetadataAnalyzer.cs` (CSHARP) | Magnitude: 12.7 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 17, core_var_decl: 6, design_snake_case: 5
- `src/modules/peek/Peek.UI/Models/NeighboringItems.cs` (CSHARP) | Magnitude: 11.34 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, api: 4, import: 4
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Services/AppStateService.cs` (CSHARP) | Magnitude: 43.58 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 33, structural_boundaries: 11, state_mutation: 10, core_var_decl: 9
- `src/settings-ui/Settings.UI/ViewModels/SearchResultsViewModel.cs` (CSHARP) | Magnitude: 53.08 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 27, core_var_decl: 21, state_mutation: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/common/Common.UI.Controls/Controls/IsEnabledTextBlock/IsEnabledTextBlock.xaml.cs` (CSHARP) | Magnitude: 16.56 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, structural_boundaries: 9, args: 8, api: 6
- `src/modules/cmdpal/Microsoft.CmdPal.Common/CoreLogger.cs` (CSHARP) | Magnitude: 41.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 36, args: 14, func_start: 13, api: 10
- `src/modules/MouseUtils/MouseJump.Common/Helpers/ConfigHelper.cs` (CSHARP) | Magnitude: 30.46 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 27, branch: 12, core_var_decl: 11
- `src/settings-ui/Settings.UI.Library/EnabledModules.cs` (CSHARP) | Magnitude: 155.54 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 503, core_var_decl: 93, design_camel_case: 50, structural_boundaries: 43
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Pages/AddBookmarkPage.cs` (CSHARP) | Magnitude: 27.98 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, core_var_decl: 9, branch: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/modules/NewPlus/NewShellExtensionContextMenu/settings.cpp` (CPP) | Magnitude: 88.44 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 141, structural_boundaries: 39, func_start: 21, branch: 20
- `src/modules/previewpane/powerpreview/trace.cpp` (CPP) | Magnitude: 14.38 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 51, args: 25, structural_boundaries: 6, func_start: 6
- `src/settings-ui/Settings.UI.Library/LightSwitchSettings.cs` (CSHARP) | Magnitude: 37.76 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 57, core_var_decl: 23, design_pascal_case: 21, structural_boundaries: 18
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/SettingsModel.cs` (CSHARP) | Magnitude: 64.6 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 81, immutability_locks: 55, structural_boundaries: 54, api: 42
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/UWP.cs` (CSHARP) | Magnitude: 85.54 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 51, core_var_decl: 35, branch: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/modules/peek/Peek.FilePreviewer/Previewers/MediaPreviewer/VideoPreviewer.cs` (CSHARP) | Magnitude: 111.72 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 121, structural_boundaries: 44, concurrency: 22, core_var_decl: 21
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsSettings/Commands/OpenSettingsCommand.cs` (CSHARP) | Magnitude: 28.66 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 24, import: 14, core_var_decl: 13
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.Bookmarks.UnitTests/PlaceholderParserTests.cs` (CSHARP) | Magnitude: 37.82 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 131, structural_boundaries: 33, test: 24, args: 17
- `src/modules/imageresizer/ui/Models/CliOptions.cs` (CSHARP) | Magnitude: 86.1 | Delta: **0.065** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 128, debug_prints: 33, structural_boundaries: 26, api: 23
- `src/modules/MeasureTool/MeasureToolCore/PerGlyphOpacityTextRender.cpp` (CPP) | Magnitude: 61.98 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 88, pointers: 27, structural_boundaries: 17, core_var_decl: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/modules/EnvironmentVariables/EnvironmentVariables/Program.cs` (CSHARP) | Magnitude: 12.82 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 11, import: 5, branch: 3
- `src/modules/AdvancedPaste/AdvancedPaste/Models/PasteFormatMetadataAttribute.cs` (CSHARP) | Magnitude: 25.3 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 12, api: 10, immutability_locks: 9, indent_spaces: 9
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.UI.ViewModels.UnitTests/RecentCommandsTests.cs` (CSHARP) | Magnitude: 122.48 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 336, structural_boundaries: 142, core_var_decl: 113, test: 69
- `src/modules/imageresizer/tests/Models/ResizeBatchTests.cs` (CSHARP) | Magnitude: 58.12 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 38, core_var_decl: 15, import: 11
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ProviderSettings.cs` (CSHARP) | Magnitude: 34.14 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 17, immutability_locks: 11, core_var_decl: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/modules/fancyzones/editor/FancyZonesEditor/Models/LayoutHotkeysModel.cs` (CSHARP) | Magnitude: 50.02 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 79, structural_boundaries: 17, branch: 11, api: 8
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/CursorLog/CursorLog/CursorLog.cpp` (CPP) | Magnitude: 84.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 115, branch: 23, core_var_decl: 16, structural_boundaries: 12
- `src/modules/MouseUtils/MouseUtils.UITests/util/MousePointerCrosshairsSettings.cs` (CSHARP) | Magnitude: 28.42 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, api: 12, structural_boundaries: 10, state_mutation: 9
- `src/modules/Workspaces/WorkspacesEditor/Models/Application.cs` (CSHARP) | Magnitude: 123.76 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 215, core_var_decl: 57, state_mutation: 44, api: 41
- `src/modules/fancyzones/editor/FancyZonesEditor/GridData.cs` (CSHARP) | Magnitude: 373.12 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 432, core_var_decl: 111, state_mutation: 83, structural_boundaries: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/settings-ui/Settings.UI/ViewModels/PowerRenameViewModel.cs` (CSHARP) | Magnitude: 119.56 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 237, core_var_decl: 38, state_mutation: 32, structural_boundaries: 28
- `src/modules/EnvironmentVariables/EnvironmentVariablesUILib/ViewModels/MainViewModel.cs` (CSHARP) | Magnitude: 289.18 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 329, structural_boundaries: 71, state_mutation: 65, core_var_decl: 49
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowWalker/Helpers/SettingsManager.cs` (CSHARP) | Magnitude: 35.86 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 93, core_var_decl: 23, structural_boundaries: 18, encapsulation: 15
- `src/modules/colorPicker/ColorPickerUI/Settings/SettingItem`1.cs` (CSHARP) | Magnitude: 10.38 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 5, api: 4, args: 2
- `src/settings-ui/Settings.UI/ViewModels/ShortcutGuideViewModel.cs` (CSHARP) | Magnitude: 116.48 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 220, core_var_decl: 32, state_mutation: 28, structural_boundaries: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/modules/awake/AwakeModuleInterface/AwakeConstants.h` (CPP) | Magnitude: 12.6 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1, immutability_locks: 1, indent_spaces: 1
- `src/modules/poweraccent/PowerAccentModuleInterface/PowerAccentConstants.h` (CPP) | Magnitude: 12.6 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1, immutability_locks: 1, indent_spaces: 1
- `src/modules/registrypreview/RegistryPreviewExt/Constants.h` (CPP) | Magnitude: 12.6 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, import: 1, immutability_locks: 1, indent_spaces: 1
- `src/common/CalculatorEngineCommon/pch.h` (CPP) | Magnitude: 12.08 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 3, macros: 1
- `src/common/GPOWrapper/pch.h` (CPP) | Magnitude: 12.08 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 3, macros: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/modules/poweraccent/PowerAccentKeyboardService/KeyboardListener.h` (CPP) | Magnitude: 18.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 101, structural_boundaries: 25, args: 15, core_var_decl: 6
- `src/modules/AdvancedPaste/AdvancedPaste/Helpers/NamedPipeProcessor.cs` (CSHARP) | Magnitude: 16.32 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 15, concurrency: 6, import: 6
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/IconData.cs` (CSHARP) | Magnitude: 12.78 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 14, api: 6, structural_boundaries: 3, args: 3
- `src/modules/fancyzones/FancyZonesTests/UnitTests/AppliedLayoutsTests.Spec.cpp` (CPP) | Magnitude: 112.74 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 545, args: 210, func_start: 35, core_var_decl: 29
- `src/modules/powerrename/unittests/PowerRenameManagerTests.cpp` (CPP) | Magnitude: 118.42 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 280, pointers: 39, args: 35, func_start: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/modules/powerrename/unittests/WICMetadataExtractorTests.cpp` (CPP) | Magnitude: 178.24 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 388, args: 59, core_var_decl: 40, branch: 33
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/ImageViewer.xaml.cs` (CSHARP) | Magnitude: 245.26 | Delta: **0.102** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 253, state_mutation: 55, branch: 54, core_var_decl: 41
- `src/common/UITestAutomation/WindowHelper.cs` (CSHARP) | Magnitude: 178.88 | Delta: **0.104** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 220, core_var_decl: 53, doc: 44, structural_boundaries: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/ExtensionServer.cs` (CSHARP) | Magnitude: 43.02 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, structural_boundaries: 16, core_var_decl: 11, api: 10
- `src/modules/AdvancedPaste/AdvancedPaste.UnitTests/ServicesTests/AIServiceBatchIntegrationTests.cs` (CSHARP) | Magnitude: 74.88 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 106, structural_boundaries: 68, concurrency: 24, core_var_decl: 23
- `src/modules/Workspaces/WorkspacesEditorUITest/WorkspacesLauncherTest.cs` (CSHARP) | Magnitude: 23.58 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 56, structural_boundaries: 13, generics: 13, core_var_decl: 9
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/AppearancePage.xaml.cs` (CSHARP) | Magnitude: 49.62 | Delta: **0.128** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 59, structural_boundaries: 25, import: 13, core_var_decl: 13
- `src/modules/fancyzones/FancyZones.UITests/DragWindowTests.cs` (CSHARP) | Magnitude: 175.3 | Delta: **0.184** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 446, core_var_decl: 109, doc: 80, design_camel_case: 75

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/runner/UpdateUtils.cpp` (CPP) | Magnitude: 158.56 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 222, branch: 39, core_var_decl: 37, state_mutation: 31
- `src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs` (CSHARP) | Magnitude: 711.22 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 897, branch: 211, core_var_decl: 106, state_mutation: 87
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Shell/Pages/ShellListPage.cs` (CSHARP) | Magnitude: 331.38 | Delta: **0.161** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 391, structural_boundaries: 92, core_var_decl: 91, state_mutation: 63

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/common/UITestAutomation/Element/TextBox.cs` (CSHARP) | Magnitude: 27.5 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 46, doc: 14, branch: 7, structural_boundaries: 7
- `src/modules/powerrename/lib/Helpers.h` (CPP) | Magnitude: 15.58 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: args: 16, immutability_locks: 8, indent_spaces: 6, import: 4
- `src/settings-ui/Settings.UI.Library/CmdPalProperties.cs` (CSHARP) | Magnitude: 25.34 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 7, macros: 7, core_var_decl: 7
- `src/modules/imageresizer/tests/Test/BitmapSourceExtensions.cs` (CSHARP) | Magnitude: 7.82 | Delta: **0.105** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 13, core_var_decl: 7, design_snake_case: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/modules/registrypreview/RegistryPreview.FuzzTests/FuzzTests.cs` (CSHARP) | Magnitude: 129.4 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 125, core_var_decl: 38, state_mutation: 27, branch: 25
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/PackageManagerWrapper.cs` (CSHARP) | Magnitude: 16.0 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 10, branch: 5, core_var_decl: 4
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/Tag.xaml.cs` (CSHARP) | Magnitude: 96.8 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 104, structural_boundaries: 22, branch: 20, safety: 19
- `src/modules/AdvancedPaste/AdvancedPaste/Helpers/OcrHelpers.cs` (CSHARP) | Magnitude: 26.72 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 17, import: 8, core_var_decl: 7
- `src/Update/PowerToys.Update.cpp` (CPP) | Magnitude: 124.46 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 150, structural_boundaries: 31, branch: 28, state_mutation: 27

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs` -> Churn: **95.26%** | Cog Load: 85.3683% | Debt: 13.9504%
- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` -> Churn: **85.38%** | Cog Load: 88.5532% | Debt: 8.2723%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandProviderWrapper.cs` -> Churn: **80.39%** | Cog Load: 65.2632% | Debt: 42.4567%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs` -> Churn: **77.58%** | Cog Load: 50.2429% | Debt: 39.5515%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockWindow.xaml.cs` -> Churn: **71.08%** | Cog Load: 80.0656% | Debt: 10.5543%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` -> **Alex Mihaiuc** (100.0% isolated ownership) | Magnitude: 15684.82
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` -> **Niels Laute** (100.0% isolated ownership) | Magnitude: 2235.8
- `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 1235.88
- `src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardEventHandlers.cpp` -> **Zach Teutsch** (100.0% isolated ownership) | Magnitude: 1155.38
- `src/modules/MouseWithoutBorders/App/Form/frmMatrix.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 941.44

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/modules/MouseWithoutBorders/App/Core/Common.cs` -> **Severity: 0.036** (Bridge: 0.0004 * Flux: 99.4215%)
- `src/modules/MouseWithoutBorders/App/Core/Logger.cs` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.9958%)
- `src/modules/MouseWithoutBorders/App/Core/Thread.cs` -> **Severity: 0.033** (Bridge: 0.0003 * Flux: 99.9704%)
- `src/common/UITestAutomation/UITestBase.cs` -> **Severity: 0.023** (Bridge: 0.0002 * Flux: 97.7478%)
- `src/common/UITestAutomation/Session.cs` -> **Severity: 0.013** (Bridge: 0.0002 * Flux: 85.8089%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/common/ManagedCommon/Logger.cs` -> **Severity: 2.851** (Embedded: 0.0552 * Error Risk: 51.6211%)
- `src/common/utils/json.h` -> **Severity: 1.631** (Embedded: 0.0318 * Error Risk: 51.2928%)
- `src/common/utils/resources.h` -> **Severity: 1.31** (Embedded: 0.0169 * Error Risk: 77.3191%)
- `src/common/utils/winapi_error.h` -> **Severity: 1.303** (Embedded: 0.0276 * Error Risk: 47.146%)
- `src/modules/MouseWithoutBorders/App/Core/Thread.cs` -> **Severity: 1.132** (Embedded: 0.0189 * Error Risk: 59.7686%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/common/ManagedCommon/Logger.cs` -> **Severity: 1370.189** (Blast Radius: 16.271 * Doc Risk: 84.2105%)
- `src/common/logger/logger.h` -> **Severity: 1042.9** (Blast Radius: 10.429 * Doc Risk: 100.0%)
- `src/modules/keyboardmanager/common/Input.h` -> **Severity: 701.6** (Blast Radius: 7.016 * Doc Risk: 100.0%)
- `src/common/utils/json.h` -> **Severity: 693.4** (Blast Radius: 6.934 * Doc Risk: 100.0%)
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/CommandResult.cs` -> **Severity: 611.9** (Blast Radius: 6.119 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 297 literal sites + 636 sites through wrappers = 933
- **`panics_and_aborts`:** 832 literal sites + 3 sites through wrappers = 835

- `case_stmt` (macro, memory_alloc, primitive): 574 call sites in 1 files -- `src/common/CalculatorEngineCommon/exprtk.hpp`
- `AllocateAndCopyString` (function, memory_alloc, primitive): 58 call sites in 1 files -- `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp`
- `LockGdiPlusBitmap` (function, memory_alloc, primitive): 2 call sites in 1 files -- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`
- `ThrowLastWin32Error` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/ReparsePoint.cs`
- `CreateDrawingBitmap` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`
- `ThrowArgumentException` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/WrapPanelCustom/WrapPanel.cs`
- `create_data` (function, memory_alloc, primitive): 1 call sites in 1 files -- `src/common/CalculatorEngineCommon/exprtk.hpp`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 74373 call pairs -- scoped 28.0%, unique 1.7%, ambiguous 26.6%, external 43.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 38055 | 31.2% | 1.2% | 31.9% | 35.7% |
| cpp | 35572 | 24.5% | 2.3% | 21.6% | 51.6% |
| python | 469 | 32.2% | 0.0% | 0.0% | 67.8% |
| c | 95 | 17.9% | 3.2% | 0.0% | 78.9% |
| powershell | 93 | 23.7% | 0.0% | 0.0% | 76.3% |
| javascript | 73 | 13.7% | 0.0% | 15.1% | 71.2% |
| html | 16 | 6.2% | 0.0% | 0.0% | 93.8% |

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
