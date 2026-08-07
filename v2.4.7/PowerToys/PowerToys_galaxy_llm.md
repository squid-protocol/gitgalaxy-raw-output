# ARCHITECTURAL_BRIEF: PowerToys
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/PowerToys` |
| **Timestamp** | `2026-08-07T03:46:14.329166+00:00` |
| **Scan Duration** | `16.72s` |
| **Git Branch** | `main` |
| **Git Commit** | `4ce451edd0a66ba4fe1366ff6a912c30be59feb3` |
| **Git Remote** | `https://github.com/microsoft/PowerToys.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4728 malicious artifacts.

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
| Total Artifacts | 7753 |
| Analyzed Artifacts (Scanned) | 5193 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2560 |
| Total LOC | 386973 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 67.0% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3179 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 239 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 3366 | 254001 | 64.8% |
| CPP | 1274 | 119144 | 24.5% |
| XML | 193 | 428 | 3.7% |
| JSON | 131 | 6280 | 2.5% |
| MARKDOWN | 97 | 0 | 1.9% |
| PLAINTEXT | 39 | 0 | 0.8% |
| MAKEFILE | 36 | 201 | 0.7% |
| POWERSHELL | 31 | 3201 | 0.6% |
| JAVASCRIPT | 10 | 622 | 0.2% |
| BATCH | 4 | 34 | 0.1% |
| HTML | 4 | 237 | 0.1% |
| PYTHON | 4 | 2674 | 0.1% |
| C | 3 | 61 | 0.1% |
| YAML | 1 | 90 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.296`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2854 | 55.0% |
| file_cluster_13 | 1664 | 32.0% |
| file_cluster_0 | 214 | 4.1% |
| file_cluster_4 | 102 | 2.0% |
| file_cluster_12 | 74 | 1.4% |
| file_cluster_16 | 59 | 1.1% |
| file_cluster_7 | 29 | 0.6% |
| file_cluster_15 | 17 | 0.3% |
| file_cluster_1 | 9 | 0.2% |
| file_cluster_17 | 7 | 0.1% |
| file_cluster_11 | 5 | 0.1% |
| file_cluster_2 | 5 | 0.1% |
| file_cluster_9 | 3 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 136 | 2.6% |
| Static: Minified & Vendor Opaque Mass | 15 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2560*

**Composition by Extension & Reason:**
- `.png`: 861x Excluded (Explicitly Denied Extension: '.png'), 3x Excluded (Explicitly Denied Extension: '.PNG')
- `.xaml`: 278x Unsupported Format (.xaml), 1x Excluded (Saturation: Line 79 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.csproj`: 186x Unsupported Format (.csproj), 1x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.md`: 144x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vcxproj`: 119x Unsupported Format (.vcxproj), 2x Excluded (Unsupported Extension: '.vcxproj')
- `.resx`: 121x Unsupported Format (.resx)
- `.js`: 87x Excluded (Saturation: Line 8 exceeds 500 chars), 20x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 113380 commas in 761 LOC)
- `.filters`: 105x Unsupported Format (.filters), 1x Excluded (Unsupported Extension: '.filters')
- `.rc`: 76x Unsupported Format (.rc), 12x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.rc')
- `.ico`: 70x Excluded (Explicitly Denied Extension: '.ico')
- `.yml`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.manifest`: 41x Unsupported Format (.manifest)
- `.ps1`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 29x Unsupported Format (.props), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.props')
- `.wxs`: 33x Excluded (Unsupported Extension: '.wxs')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 22.7 | 8.5 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 42.6 | 52.9 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 36.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 9.0 | 2.3 | 0.0 |
| API Exposure | 0.0 | 18.3 | 4.4 | 4.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 53.3 | 71.1 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.5 | 1.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.0 | 26.7 | 100.0 |
| Hardcoded Payload Artifacts | 0.0 | 82.1 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` (Hits: 76)
- `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` (Hits: 55)
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.UI.ViewModels.UnitTests/ExtensionTemplateServiceTests.cs` (Hits: 53)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Microsoft.CommandPalette.Extensions.def** (`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions/Microsoft.CommandPalette.Extensions.def`) — 228 inbound connections
2. **Input.h** (`src/modules/keyboardmanager/common/Input.h`) — 133 inbound connections
3. **Services.svg** (`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsServices/Assets/Services.svg`) — 107 inbound connections
4. **Utils.h** (`src/modules/powerrename/PowerRenameUILib/Utils.h`) — 74 inbound connections
5. **PowerToys.Interop.def** (`src/common/interop/PowerToys.Interop.def`) — 65 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pch.h** (`src/modules/ZoomIt/ZoomIt/pch.h`) — 82 outbound dependencies
2. **pch.h** (`src/modules/cmdpal/Microsoft.Terminal.UI/pch.h`) — 52 outbound dependencies
3. **pch.h** (`src/modules/MeasureTool/MeasureToolCore/pch.h`) — 51 outbound dependencies
4. **CaptureFrameWait.h** (`src/modules/ZoomIt/ZoomIt/CaptureFrameWait.h`) — 50 outbound dependencies
5. **main.cpp** (`src/runner/main.cpp`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `OptionsTabProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **692.9** | LOC: 1604
- `TimelineSubclassProc` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **678.3** | LOC: 1343
- `VideoRecordingSession::ShowTrimDialogInt` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **637.5** | LOC: 1433
- `RunPanoramaStitchSelfTest` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **508.9** | LOC: 1241
- `VideoRecordingSession::TrimDialogProc` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **499.2** | LOC: 1173
- `BuildFixedOverlayMask` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **483.1** | LOC: 542
- `StartPlaybackAsync` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **441.9** | LOC: 1356
  * *Intent:* // The selection (trimStart..trimEnd) determines what will be trimmed, // but playback may start before trimStart. Clamp only to valid media bounds.
- `LoadGifFrames` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **337.6** | LOC: 1245
- `FetchItems` (@ `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs`) -> Impact: **331.3** | LOC: 723
- `_on_mouse_move` (@ `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py`) -> Impact: **331.0** | LOC: 869

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/modules/ZoomIt/ZoomIt` | 29 | 31505.48 | 42.24% | 19.79% |
| `src/modules/fancyzones/FancyZonesLib` | 70 | 8120.28 | 45.94% | 38.63% |
| `src/settings-ui/Settings.UI/ViewModels` | 41 | 7756.82 | 31.7% | 25.45% |
| `src/settings-ui/Settings.UI.Library` | 153 | 6981.2 | 17.68% | 64.45% |
| `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels` | 94 | 6739.51 | 29.53% | 41.16% |
| `src/modules/powerrename/lib` | 40 | 5103.4 | 36.72% | 37.87% |
| `src/modules/keyboardmanager/KeyboardManagerEditorLibrary` | 40 | 4799.16 | 36.31% | 28.88% |
| `src/modules/MouseWithoutBorders/App/Core` | 29 | 4707.5 | 36.26% | 28.16% |
| `src/common/utils` | 34 | 4084.32 | 51.69% | 21.89% |
| `src/modules/fancyzones/FancyZonesTests/UnitTests` | 22 | 3628.86 | 29.65% | 81.16% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/common/Common.Search/FuzzSearch/MatchResult.cs` -> **100.0%** Exposure
- `src/common/PowerToys.ModuleContracts/OperationResult.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/By.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/UITestBase.cs` -> **100.0%** Exposure
- `src/dsc/PowerToys.Settings.DSC.Schema.Generator/Common.cs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/skills/release-note-generation/scripts/apply-labels.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/collect-or-apply-milestones.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/diff_prs.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/dump-prs-since-commit.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/find-commit-by-title.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/common/interop/Constants.cpp` -> **73** Orphaned Functions | **0** Duplicates
- `src/common/GPOWrapper/GPOWrapper.cpp` -> **70** Orphaned Functions | **2** Duplicates
- `src/modules/fancyzones/FancyZonesTests/UnitTests/JsonHelpers.Tests.cpp` -> **0** Orphaned Functions | **68** Duplicates
- `src/modules/powerrename/unittests/MetadataFormatHelperTests.cpp` -> **0** Orphaned Functions | **66** Duplicates
- `src/common/UnitTests-CommonLib/Settings.Tests.cpp` -> **0** Orphaned Functions | **65** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/modules/MouseWithoutBorders/App/Class/InputSimulation.cs`** -> AI Confidence: **99.48%**
2. **`src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs`** -> AI Confidence: **99.48%**
3. **`src/modules/MouseWithoutBorders/App/Core/Receiver.cs`** -> AI Confidence: **99.48%**
4. **`src/modules/MouseWithoutBorders/App/Form/frmMatrix.cs`** -> AI Confidence: **99.48%**
5. **`src/modules/MouseWithoutBorders/App/Form/frmScreen.cs`** -> AI Confidence: **99.48%**
6. **`src/modules/MouseWithoutBorders/App/Helper/FormHelper.cs`** -> AI Confidence: **99.48%**
7. **`src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.ValueGenerator/InputParser.cs`** -> AI Confidence: **99.48%**
8. **`src/ActionRunner/actionRunner.cpp`** -> AI Confidence: **99.48%**
9. **`src/modules/LightSwitch/LightSwitchService/LightSwitchService.cpp`** -> AI Confidence: **99.48%**
10. **`src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`** -> AI Confidence: **99.48%**
11. **`src/modules/ZoomIt/ZoomIt/Zoomit.cpp`** -> AI Confidence: **99.48%**
12. **`src/modules/ZoomIt/ZoomItSettingsInterop/ZoomItSettings.cpp`** -> AI Confidence: **99.48%**
13. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/BufferValidationHelpers.cpp`** -> AI Confidence: **99.48%**
14. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/LoadingAndSavingRemappingHelper.cpp`** -> AI Confidence: **99.48%**
15. **`src/modules/powerrename/lib/Helpers.cpp`** -> AI Confidence: **99.48%**
16. **`src/modules/powerrename/lib/Renaming.cpp`** -> AI Confidence: **99.48%**
17. **`src/runner/main.cpp`** -> AI Confidence: **99.48%**
18. **`tools/module_loader/src/SettingsLoader.cpp`** -> AI Confidence: **99.48%**
19. **`src/modules/MouseWithoutBorders/App/Class/InputHook.cs`** -> AI Confidence: **99.39%**
20. **`src/modules/MouseWithoutBorders/App/Core/Helper.cs`** -> AI Confidence: **99.39%**
21. **`src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs`** -> AI Confidence: **99.39%**
22. **`src/modules/awake/Awake/Core/TrayHelper.cs`** -> AI Confidence: **99.39%**
23. **`src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.Utilities.cs`** -> AI Confidence: **99.39%**
24. **`src/settings-ui/Settings.UI/SettingsXAML/OobeWindow.xaml.cs`** -> AI Confidence: **99.39%**
25. **`src/modules/fancyzones/FancyZones/FancyZonesApp.cpp`** -> AI Confidence: **99.39%**
26. **`src/modules/fancyzones/FancyZonesLib/WindowDrag.cpp`** -> AI Confidence: **99.39%**
27. **`src/modules/fancyzones/FancyZonesLib/WindowMouseSnap.cpp`** -> AI Confidence: **99.39%**
28. **`src/modules/keyboardmanager/common/Helpers.cpp`** -> AI Confidence: **99.39%**
29. **`src/modules/keyboardmanager/common/Shortcut.cpp`** -> AI Confidence: **99.39%**
30. **`src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/App.xaml.cpp`** -> AI Confidence: **99.39%**
31. **`src/modules/fancyzones/editor/FancyZonesEditor/LayoutPreview.xaml.cs`** -> AI Confidence: **99.34%**
32. **`src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp`** -> AI Confidence: **99.34%**
33. **`src/modules/powerrename/lib/WICMetadataExtractor.cpp`** -> AI Confidence: **99.34%**
34. **`src/runner/auto_start_helper.cpp`** -> AI Confidence: **99.34%**
35. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPageResultFactory.cs`** -> AI Confidence: **99.32%**
36. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.cs`** -> AI Confidence: **99.32%**
37. **`src/modules/NewPlus/NewShellExtensionContextMenu/Helpers.cpp`** -> AI Confidence: **99.32%**
38. **`src/modules/ZoomIt/ZoomItBreak/BreakTimer.cpp`** -> AI Confidence: **99.32%**
39. **`src/modules/powerrename/lib/Enumerating.cpp`** -> AI Confidence: **99.32%**
40. **`src/common/FilePreviewCommon/HTMLParsingExtension.cs`** -> AI Confidence: **99.31%**
41. **`src/common/ManagedCommon/Logger.cs`** -> AI Confidence: **99.31%**
42. **`src/common/UITestAutomation/SessionHelper.cs`** -> AI Confidence: **99.31%**
43. **`src/common/UITestAutomation/SettingsConfigHelper.cs`** -> AI Confidence: **99.31%**
44. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/Pages/MainPage.xaml.cs`** -> AI Confidence: **99.31%**
45. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/UserSettings.cs`** -> AI Confidence: **99.31%**
46. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActions/SemanticKernelPasteProvider.cs`** -> AI Confidence: **99.31%**
47. **`src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs`** -> AI Confidence: **99.31%**
48. **`src/modules/FileLocksmith/FileLocksmithUI/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.31%**
49. **`src/modules/MouseUtils/MouseUtils.UITests/FindMyMouseTests.cs`** -> AI Confidence: **99.31%**
50. **`src/modules/MouseUtils/MouseUtils.UITests/MouseHighlighterTests.cs`** -> AI Confidence: **99.31%**
51. **`src/modules/MouseWithoutBorders/App/Class/IClipboardHelper.cs`** -> AI Confidence: **99.31%**
52. **`src/modules/MouseWithoutBorders/App/Class/TcpServer.cs`** -> AI Confidence: **99.31%**
53. **`src/modules/MouseWithoutBorders/App/Core/Clipboard.cs`** -> AI Confidence: **99.31%**
54. **`src/modules/MouseWithoutBorders/App/Core/DragDrop.cs`** -> AI Confidence: **99.31%**
55. **`src/modules/MouseWithoutBorders/App/Core/Event.cs`** -> AI Confidence: **99.31%**
56. **`src/modules/MouseWithoutBorders/App/Core/InitAndCleanup.cs`** -> AI Confidence: **99.31%**
57. **`src/modules/MouseWithoutBorders/App/Core/Launch.cs`** -> AI Confidence: **99.31%**
58. **`src/modules/MouseWithoutBorders/App/Core/Logger.cs`** -> AI Confidence: **99.31%**
59. **`src/modules/MouseWithoutBorders/App/Core/Service.cs`** -> AI Confidence: **99.31%**
60. **`src/modules/MouseWithoutBorders/App/Core/WinAPI.cs`** -> AI Confidence: **99.31%**
61. **`src/modules/MouseWithoutBorders/App/Form/Settings/SetupPage3a.cs`** -> AI Confidence: **99.31%**
62. **`src/modules/MouseWithoutBorders/App/Service/Worker.cs`** -> AI Confidence: **99.31%**
63. **`src/modules/PowerOCR/PowerOCR/Models/ResultTable.cs`** -> AI Confidence: **99.31%**
64. **`src/modules/PowerOCR/PowerOCR/OCROverlay.xaml.cs`** -> AI Confidence: **99.31%**
65. **`src/modules/Workspaces/WorkspacesEditor/Utils/DrawHelper.cs`** -> AI Confidence: **99.31%**
66. **`src/modules/Workspaces/WorkspacesEditor/Utils/WorkspacesEditorIO.cs`** -> AI Confidence: **99.31%**
67. **`src/modules/Workspaces/WorkspacesLauncherUI/App.xaml.cs`** -> AI Confidence: **99.31%**
68. **`src/modules/awake/Awake/Core/Manager.cs`** -> AI Confidence: **99.31%**
69. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs`** -> AI Confidence: **99.31%**
70. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ContentPageViewModel.cs`** -> AI Confidence: **99.31%**
71. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ExtensionObjectViewModel.cs`** -> AI Confidence: **99.31%**
72. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs`** -> AI Confidence: **99.31%**
73. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ShellViewModel.cs`** -> AI Confidence: **99.31%**
74. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/FiltersDropDown.xaml.cs`** -> AI Confidence: **99.31%**
75. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockWindow.xaml.cs`** -> AI Confidence: **99.31%**
76. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ContentPage.xaml.cs`** -> AI Confidence: **99.31%**
77. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/Controls/PlainTextContentViewer.xaml.cs`** -> AI Confidence: **99.31%**
78. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs`** -> AI Confidence: **99.31%**
79. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Pages/ShellPage.xaml.cs`** -> AI Confidence: **99.31%**
80. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/SettingsWindow.xaml.cs`** -> AI Confidence: **99.31%**
81. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/Win32Program.cs`** -> AI Confidence: **99.31%**
82. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.ClipboardHistory/Pages/ClipboardListItem.cs`** -> AI Confidence: **99.31%**
83. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Program.cs`** -> AI Confidence: **99.31%**
84. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.System/Helpers/NetworkConnectionProperties.cs`** -> AI Confidence: **99.31%**
85. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/Pages/InstallPackageCommand.cs`** -> AI Confidence: **99.31%**
86. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/Pages/InstallPackageListItem.cs`** -> AI Confidence: **99.31%**
87. **`src/modules/colorPicker/ColorPickerUI/App.xaml.cs`** -> AI Confidence: **99.31%**
88. **`src/modules/fancyzones/FancyZonesCLI/CommandLine/Commands/FancyZonesBaseCommand.cs`** -> AI Confidence: **99.31%**
89. **`src/modules/fancyzones/FancyZonesCLI/CommandLine/Commands/SetLayoutCommand.cs`** -> AI Confidence: **99.31%**
90. **`src/modules/fancyzones/FancyZonesEditor.UITests/DefaultLayoutsTest.cs`** -> AI Confidence: **99.31%**
91. **`src/modules/fancyzones/editor/FancyZonesEditor/CanvasZone.xaml.cs`** -> AI Confidence: **99.31%**
92. **`src/modules/fancyzones/editor/FancyZonesEditor/GridEditor.xaml.cs`** -> AI Confidence: **99.31%**
93. **`src/modules/fancyzones/editor/FancyZonesEditor/GridZone.xaml.cs`** -> AI Confidence: **99.31%**
94. **`src/modules/fancyzones/editor/FancyZonesEditor/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
95. **`src/modules/fancyzones/editor/FancyZonesEditor/Utils/FancyZonesEditorIO.cs`** -> AI Confidence: **99.31%**
96. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Controls/UnifiedMappingControl.xaml.cs`** -> AI Confidence: **99.31%**
97. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/KeyboardHookHelper.cs`** -> AI Confidence: **99.31%**
98. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/RemappingHelper.cs`** -> AI Confidence: **99.31%**
99. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Pages/MainPage.xaml.cs`** -> AI Confidence: **99.31%**
100. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Storage/Win32ProgramRepository.cs`** -> AI Confidence: **99.31%**
101. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Service/Helpers/ServiceHelper.cs`** -> AI Confidence: **99.31%**
102. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.System/Components/NetworkConnectionProperties.cs`** -> AI Confidence: **99.31%**
103. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate.UnitTests/QueryTests.cs`** -> AI Confidence: **99.31%**
104. **`src/modules/launcher/PowerLauncher/Helper/EnvironmentHelper.cs`** -> AI Confidence: **99.31%**
105. **`src/modules/launcher/PowerLauncher/Helper/ThemeManager.cs`** -> AI Confidence: **99.31%**
106. **`src/modules/launcher/PowerLauncher/ViewModel/MainViewModel.cs`** -> AI Confidence: **99.31%**
107. **`src/modules/launcher/Wox.Infrastructure/Exception/ExceptionFormatter.cs`** -> AI Confidence: **99.31%**
108. **`src/modules/launcher/Wox.Infrastructure/Helper.cs`** -> AI Confidence: **99.31%**
109. **`src/modules/launcher/Wox.Infrastructure/Image/ImageLoader.cs`** -> AI Confidence: **99.31%**
110. **`src/modules/launcher/Wox.Infrastructure/Image/WindowsThumbnailProvider.cs`** -> AI Confidence: **99.31%**
111. **`src/modules/launcher/Wox.Plugin/Common/VirtualDesktop/VirtualDesktopHelper.cs`** -> AI Confidence: **99.31%**
112. **`src/modules/launcher/Wox.Plugin/PluginPair.cs`** -> AI Confidence: **99.31%**
113. **`src/modules/peek/Peek.FilePreviewer/Controls/ShellPreviewHandlerControl.xaml.cs`** -> AI Confidence: **99.31%**
114. **`src/modules/poweraccent/PowerAccent.Core/PowerAccent.cs`** -> AI Confidence: **99.31%**
115. **`src/modules/poweraccent/PowerAccent.Core/Services/SettingsService.cs`** -> AI Confidence: **99.31%**
116. **`src/modules/powerdisplay/PowerDisplay.Lib/Drivers/DDC/MonitorDiscoveryHelper.cs`** -> AI Confidence: **99.31%**
117. **`src/modules/powerdisplay/PowerDisplay/Helpers/DisplayChangeWatcher.cs`** -> AI Confidence: **99.31%**
118. **`src/modules/powerdisplay/PowerDisplay/Helpers/TrayIconService.cs`** -> AI Confidence: **99.31%**
119. **`src/modules/powerdisplay/PowerDisplay/PowerDisplayXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
120. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MainViewModel.Settings.cs`** -> AI Confidence: **99.31%**
121. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MonitorViewModel.cs`** -> AI Confidence: **99.31%**
122. **`src/modules/previewpane/MarkdownPreviewHandler/MarkdownPreviewHandlerControl.cs`** -> AI Confidence: **99.31%**
123. **`src/modules/previewpane/MonacoPreviewHandler/MonacoPreviewHandlerControl.cs`** -> AI Confidence: **99.31%**
124. **`src/modules/registrypreview/RegistryPreview/RegistryPreviewXAML/App.xaml.cs`** -> AI Confidence: **99.31%**
125. **`src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs`** -> AI Confidence: **99.31%**
126. **`src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.DataPreview.cs`** -> AI Confidence: **99.31%**
127. **`src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.Events.cs`** -> AI Confidence: **99.31%**
128. **`src/settings-ui/QuickAccess.UI/QuickAccessXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
129. **`src/settings-ui/Settings.UI.Library/HotkeySettings.cs`** -> AI Confidence: **99.31%**
130. **`src/settings-ui/Settings.UI.Library/SettingsUtils.cs`** -> AI Confidence: **99.31%**
131. **`src/settings-ui/Settings.UI/SettingsXAML/App.xaml.cs`** -> AI Confidence: **99.31%**
132. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/ModelPicker/FoundryLocalModelPicker.xaml.cs`** -> AI Confidence: **99.31%**
133. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/Timeline/Timeline.xaml.cs`** -> AI Confidence: **99.31%**
134. **`src/settings-ui/Settings.UI/SettingsXAML/Views/AwakePage.xaml.cs`** -> AI Confidence: **99.31%**
135. **`src/settings-ui/Settings.UI/SettingsXAML/Views/CustomVcpMappingEditorDialog.xaml.cs`** -> AI Confidence: **99.31%**
136. **`src/settings-ui/Settings.UI/SettingsXAML/Views/LightSwitchPage.xaml.cs`** -> AI Confidence: **99.31%**
137. **`src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs`** -> AI Confidence: **99.31%**
138. **`src/settings-ui/Settings.UI/ViewModels/LightSwitchViewModel.cs`** -> AI Confidence: **99.31%**
139. **`src/settings-ui/Settings.UI/ViewModels/PowerLauncherViewModel.cs`** -> AI Confidence: **99.31%**
140. **`src/settings-ui/Settings.UI/ViewModels/ShortcutConflictViewModel.cs`** -> AI Confidence: **99.31%**
141. **`src/settings-ui/Settings.UI/ViewModels/ShortcutGuideViewModel.cs`** -> AI Confidence: **99.31%**
142. **`src/settings-ui/UITest-Settings/OOBEUITests.cs`** -> AI Confidence: **99.31%**
143. **`installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp`** -> AI Confidence: **99.31%**
144. **`src/Update/PowerToys.Update.cpp`** -> AI Confidence: **99.31%**
145. **`src/common/Display/DisplayUtils.cpp`** -> AI Confidence: **99.31%**
146. **`src/common/updating/updating.cpp`** -> AI Confidence: **99.31%**
147. **`src/common/utils/UnhandledExceptionHandler.h`** -> AI Confidence: **99.31%**
148. **`src/common/utils/elevation.h`** -> AI Confidence: **99.31%**
149. **`src/common/utils/package.h`** -> AI Confidence: **99.31%**
150. **`src/modules/AdvancedPaste/AdvancedPasteModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
151. **`src/modules/EnvironmentVariables/EnvironmentVariablesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
152. **`src/modules/FileLocksmith/FileLocksmithCLI/CLILogic.cpp`** -> AI Confidence: **99.31%**
153. **`src/modules/FileLocksmith/FileLocksmithExt/ExplorerCommand.cpp`** -> AI Confidence: **99.31%**
154. **`src/modules/Hosts/HostsModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
155. **`src/modules/LightSwitch/LightSwitchModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
156. **`src/modules/LightSwitch/LightSwitchService/LightSwitchSettings.cpp`** -> AI Confidence: **99.31%**
157. **`src/modules/MeasureTool/MeasureToolCore/MeasureToolOverlayUI.cpp`** -> AI Confidence: **99.31%**
158. **`src/modules/MeasureTool/MeasureToolCore/PowerToys.MeasureToolCore.cpp`** -> AI Confidence: **99.31%**
159. **`src/modules/MouseUtils/CursorWrap/dllmain.cpp`** -> AI Confidence: **99.31%**
160. **`src/modules/MouseUtils/FindMyMouse/dllmain.cpp`** -> AI Confidence: **99.31%**
161. **`src/modules/MouseUtils/MouseHighlighter/dllmain.cpp`** -> AI Confidence: **99.31%**
162. **`src/modules/MouseWithoutBorders/ModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
163. **`src/modules/NewPlus/NewShellExtensionContextMenu/template_item.cpp`** -> AI Confidence: **99.31%**
164. **`src/modules/ShortcutGuide/ShortcutGuide/main.cpp`** -> AI Confidence: **99.31%**
165. **`src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp`** -> AI Confidence: **99.31%**
166. **`src/modules/ShortcutGuide/ShortcutGuide/shortcut_guide.cpp`** -> AI Confidence: **99.31%**
167. **`src/modules/Workspaces/WorkspacesLauncher/AppLauncher.cpp`** -> AI Confidence: **99.31%**
168. **`src/modules/Workspaces/WorkspacesLauncher/Launcher.cpp`** -> AI Confidence: **99.31%**
169. **`src/modules/Workspaces/WorkspacesLauncher/LauncherUIHelper.cpp`** -> AI Confidence: **99.31%**
170. **`src/modules/Workspaces/WorkspacesLauncher/WindowArrangerHelper.cpp`** -> AI Confidence: **99.31%**
171. **`src/modules/Workspaces/WorkspacesLauncher/main.cpp`** -> AI Confidence: **99.31%**
172. **`src/modules/Workspaces/WorkspacesLib/AppUtils.cpp`** -> AI Confidence: **99.31%**
173. **`src/modules/Workspaces/WorkspacesLib/PwaHelper.cpp`** -> AI Confidence: **99.31%**
174. **`src/modules/Workspaces/WorkspacesLib/WindowUtils.cpp`** -> AI Confidence: **99.31%**
175. **`src/modules/Workspaces/WorkspacesSnapshotTool/SnapshotUtils.cpp`** -> AI Confidence: **99.31%**
176. **`src/modules/Workspaces/WorkspacesWindowArranger/WindowArranger.cpp`** -> AI Confidence: **99.31%**
177. **`src/modules/Workspaces/WorkspacesWindowArranger/main.cpp`** -> AI Confidence: **99.31%**
178. **`src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`** -> AI Confidence: **99.31%**
179. **`src/modules/ZoomIt/ZoomItBreak/ZoomItBreakScr.cpp`** -> AI Confidence: **99.31%**
180. **`src/modules/alwaysontop/AlwaysOnTop/AlwaysOnTop.cpp`** -> AI Confidence: **99.31%**
181. **`src/modules/alwaysontop/AlwaysOnTop/WindowBorder.cpp`** -> AI Confidence: **99.31%**
182. **`src/modules/alwaysontop/AlwaysOnTop/main.cpp`** -> AI Confidence: **99.31%**
183. **`src/modules/cmdpal/CmdPalModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
184. **`src/modules/fancyzones/FancyZones/main.cpp`** -> AI Confidence: **99.31%**
185. **`src/modules/fancyzones/FancyZonesLib/FancyZones.cpp`** -> AI Confidence: **99.31%**
186. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/AppZoneHistory.cpp`** -> AI Confidence: **99.31%**
187. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/AppliedLayouts.cpp`** -> AI Confidence: **99.31%**
188. **`src/modules/fancyzones/FancyZonesLib/JsonHelpers.cpp`** -> AI Confidence: **99.31%**
189. **`src/modules/fancyzones/FancyZonesLib/Layout.cpp`** -> AI Confidence: **99.31%**
190. **`src/modules/fancyzones/FancyZonesLib/MonitorUtils.cpp`** -> AI Confidence: **99.31%**
191. **`src/modules/fancyzones/FancyZonesLib/Settings.cpp`** -> AI Confidence: **99.31%**
192. **`src/modules/fancyzones/FancyZonesLib/WindowKeyboardSnap.cpp`** -> AI Confidence: **99.31%**
193. **`src/modules/fancyzones/FancyZonesLib/WindowUtils.cpp`** -> AI Confidence: **99.31%**
194. **`src/modules/fancyzones/FancyZonesLib/WorkArea.cpp`** -> AI Confidence: **99.31%**
195. **`src/modules/fancyzones/FancyZonesLib/ZonesOverlay.cpp`** -> AI Confidence: **99.31%**
196. **`src/modules/fancyzones/FancyZonesLib/util.cpp`** -> AI Confidence: **99.31%**
197. **`src/modules/imageresizer/ImageResizerLib/Settings.cpp`** -> AI Confidence: **99.31%**
198. **`src/modules/imageresizer/dll/ContextMenuHandler.cpp`** -> AI Confidence: **99.31%**
199. **`src/modules/keyboardmanager/KeyboardManagerEditor/KeyboardManagerEditor.cpp`** -> AI Confidence: **99.31%**
200. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditKeyboardWindow.cpp`** -> AI Confidence: **99.31%**
201. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditShortcutsWindow.cpp`** -> AI Confidence: **99.31%**
202. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/KeyDropDownControl.cpp`** -> AI Confidence: **99.31%**
203. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/ShortcutControl.cpp`** -> AI Confidence: **99.31%**
204. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/SingleKeyRemapControl.cpp`** -> AI Confidence: **99.31%**
205. **`src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp`** -> AI Confidence: **99.31%**
206. **`src/modules/keyboardmanager/KeyboardManagerEngine/main.cpp`** -> AI Confidence: **99.31%**
207. **`src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardManager.cpp`** -> AI Confidence: **99.31%**
208. **`src/modules/keyboardmanager/common/MappingConfiguration.cpp`** -> AI Confidence: **99.31%**
209. **`src/modules/keyboardmanager/dll/dllmain.cpp`** -> AI Confidence: **99.31%**
210. **`src/modules/peek/peek/dllmain.cpp`** -> AI Confidence: **99.31%**
211. **`src/modules/poweraccent/PowerAccentKeyboardService/KeyboardListener.cpp`** -> AI Confidence: **99.31%**
212. **`src/modules/powerdisplay/PowerDisplayModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
213. **`src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/MainWindow.xaml.cpp`** -> AI Confidence: **99.31%**
214. **`src/modules/powerrename/dll/PowerRenameExt.cpp`** -> AI Confidence: **99.31%**
215. **`src/modules/powerrename/lib/MetadataPatternExtractor.cpp`** -> AI Confidence: **99.31%**
216. **`src/modules/powerrename/lib/PowerRenameManager.cpp`** -> AI Confidence: **99.31%**
217. **`src/modules/powerrename/lib/PowerRenameRegEx.cpp`** -> AI Confidence: **99.31%**
218. **`src/modules/powerrename/lib/Settings.cpp`** -> AI Confidence: **99.31%**
219. **`src/modules/powerrename/unittests/PowerRenameManagerTests.cpp`** -> AI Confidence: **99.31%**
220. **`src/modules/previewpane/BgcodePreviewHandlerCpp/BgcodePreviewHandler.cpp`** -> AI Confidence: **99.31%**
221. **`src/modules/previewpane/BgcodeThumbnailProviderCpp/BgcodeThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
222. **`src/modules/previewpane/GcodePreviewHandlerCpp/GcodePreviewHandler.cpp`** -> AI Confidence: **99.31%**
223. **`src/modules/previewpane/GcodeThumbnailProviderCpp/GcodeThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
224. **`src/modules/previewpane/MarkdownPreviewHandlerCpp/MarkdownPreviewHandler.cpp`** -> AI Confidence: **99.31%**
225. **`src/modules/previewpane/MonacoPreviewHandlerCpp/MonacoPreviewHandler.cpp`** -> AI Confidence: **99.31%**
226. **`src/modules/previewpane/PdfPreviewHandlerCpp/PdfPreviewHandler.cpp`** -> AI Confidence: **99.31%**
227. **`src/modules/previewpane/PdfThumbnailProviderCpp/PdfThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
228. **`src/modules/previewpane/QoiPreviewHandlerCpp/QoiPreviewHandler.cpp`** -> AI Confidence: **99.31%**
229. **`src/modules/previewpane/QoiThumbnailProviderCpp/QoiThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
230. **`src/modules/previewpane/StlThumbnailProviderCpp/StlThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
231. **`src/modules/previewpane/SvgPreviewHandlerCpp/SvgPreviewHandler.cpp`** -> AI Confidence: **99.31%**
232. **`src/modules/previewpane/SvgThumbnailProviderCpp/SvgThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
233. **`src/modules/previewpane/powerpreview/powerpreview.cpp`** -> AI Confidence: **99.31%**
234. **`src/runner/UpdateUtils.cpp`** -> AI Confidence: **99.31%**
235. **`src/runner/general_settings.cpp`** -> AI Confidence: **99.31%**
236. **`src/runner/quick_access_host.cpp`** -> AI Confidence: **99.31%**
237. **`src/runner/settings_window.cpp`** -> AI Confidence: **99.31%**
238. **`src/runner/tray_icon.cpp`** -> AI Confidence: **99.31%**
239. **`tools/BugReportTool/BugReportTool/EventViewer.cpp`** -> AI Confidence: **99.31%**
240. **`tools/MonitorReportTool/MonitorReportTool.cpp`** -> AI Confidence: **99.31%**
241. **`tools/module_loader/src/main.cpp`** -> AI Confidence: **99.31%**
242. **`src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py`** -> AI Confidence: **99.31%**
243. **`.github/skills/release-note-generation/scripts/collect-or-apply-milestones.ps1`** -> AI Confidence: **99.29%**
244. **`.github/skills/release-note-generation/scripts/diff_prs.ps1`** -> AI Confidence: **99.29%**
245. **`.github/skills/release-note-generation/scripts/dump-prs-since-commit.ps1`** -> AI Confidence: **99.29%**
246. **`.github/skills/release-note-generation/scripts/find-commit-by-title.ps1`** -> AI Confidence: **99.29%**
247. **`.github/skills/release-note-generation/scripts/group-prs-by-label.ps1`** -> AI Confidence: **99.29%**
248. **`.github/skills/winmd-api-search/scripts/Update-WinMdCache.ps1`** -> AI Confidence: **99.29%**
249. **`installer/PowerToysSetupVNext/generateMonacoWxs.ps1`** -> AI Confidence: **99.29%**
250. **`src/PackageIdentity/BuildSparsePackage.ps1`** -> AI Confidence: **99.29%**
251. **`src/codeAnalysis/format_sources.ps1`** -> AI Confidence: **99.29%**
252. **`src/modules/MouseUtils/CursorWrap/CursorWrapTests/Capture-MonitorLayout.ps1`** -> AI Confidence: **99.29%**
253. **`src/modules/cmdpal/check-extensions.ps1`** -> AI Confidence: **99.29%**
254. **`src/modules/cmdpal/doc/initial-sdk-spec/generate-interface.ps1`** -> AI Confidence: **99.29%**
255. **`src/modules/cmdpal/extensionsdk/nuget/BuildSDKHelper.ps1`** -> AI Confidence: **99.29%**
256. **`src/modules/cmdpal/format_sources.ps1`** -> AI Confidence: **99.29%**
257. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/CheckCmdNotFoundRequirements.ps1`** -> AI Confidence: **99.29%**
258. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/DisableModule.ps1`** -> AI Confidence: **99.29%**
259. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/EnableModule.ps1`** -> AI Confidence: **99.29%**
260. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/InstallPowerShell7.ps1`** -> AI Confidence: **99.29%**
261. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/InstallWinGetClientModule.ps1`** -> AI Confidence: **99.29%**
262. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/UpgradeModule.ps1`** -> AI Confidence: **99.29%**
263. **`tools/CleanUp_tool_powershell_script/CleanUp_tool.ps1`** -> AI Confidence: **99.29%**
264. **`tools/Verification scripts/verify-installation-script.ps1`** -> AI Confidence: **99.29%**
265. **`tools/clear-copilot-context.ps1`** -> AI Confidence: **99.29%**
266. **`src/modules/AdvancedPaste/AdvancedPaste/Models/PasteFormats.cs`** -> AI Confidence: **99.29%**
267. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/AdaptiveCardsConfig.cs`** -> AI Confidence: **99.29%**
268. **`src/modules/cmdpal/Microsoft.CmdPal.UI/LocalSuppressions.cs`** -> AI Confidence: **99.29%**
269. **`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/GlobalSuppressions.cs`** -> AI Confidence: **99.29%**
270. **`src/common/utils/resources.h`** -> AI Confidence: **99.29%**
271. **`src/modules/MeasureTool/MeasureToolCore/BGRATextureView.cpp`** -> AI Confidence: **99.29%**
272. **`src/modules/cmdpal/Microsoft.Terminal.UI/init.cpp`** -> AI Confidence: **99.29%**
273. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/Dialog.cpp`** -> AI Confidence: **99.29%**
274. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditorHelpers.cpp`** -> AI Confidence: **99.29%**
275. **`src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/dllmain.cpp`** -> AI Confidence: **99.29%**
276. **`src/modules/powerrename/lib/Randomizer.cpp`** -> AI Confidence: **99.29%**
277. **`tools/module_loader/src/ConsoleHost.cpp`** -> AI Confidence: **99.29%**
278. **`src/Monaco/customLanguages/gitignore.js`** -> AI Confidence: **99.29%**
279. **`src/common/UITestAutomation/Session.cs`** -> AI Confidence: **99.24%**
280. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActions/FoundryLocalPasteProvider.cs`** -> AI Confidence: **99.24%**
281. **`src/modules/AdvancedPaste/AdvancedPaste/ViewModels/OptionsViewModel.cs`** -> AI Confidence: **99.24%**
282. **`src/modules/Hosts/HostsUILib/Helpers/HostsService.cs`** -> AI Confidence: **99.24%**
283. **`src/modules/LightSwitch/Tests/LightSwitch.UITests/TestHelper.cs`** -> AI Confidence: **99.24%**
284. **`src/modules/MouseUtils/MouseJumpUI/MainForm.cs`** -> AI Confidence: **99.24%**
285. **`src/modules/MouseWithoutBorders/App/Class/MyKnownBitmap.cs`** -> AI Confidence: **99.24%**
286. **`src/modules/PowerOCR/PowerOCR/App.xaml.cs`** -> AI Confidence: **99.24%**
287. **`src/modules/Workspaces/WorkspacesCsharpLibrary/Models/BaseApplication.cs`** -> AI Confidence: **99.24%**
288. **`src/modules/Workspaces/WorkspacesEditor/Models/Project.cs`** -> AI Confidence: **99.24%**
289. **`src/modules/Workspaces/WorkspacesEditor/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.24%**
290. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Services/SettingsService.cs`** -> AI Confidence: **99.24%**
291. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelCommandManager.cs`** -> AI Confidence: **99.24%**
292. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelViewModel.cs`** -> AI Confidence: **99.24%**
293. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/BlurImageControl.cs`** -> AI Confidence: **99.24%**
294. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockControl.xaml.cs`** -> AI Confidence: **99.24%**
295. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockItemControl.xaml.cs`** -> AI Confidence: **99.24%**
296. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/TrayIconService.cs`** -> AI Confidence: **99.24%**
297. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.System.UnitTests/ImageTests.cs`** -> AI Confidence: **99.24%**
298. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AppListItem.cs`** -> AI Confidence: **99.24%**
299. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Pages/BookmarkListItem.cs`** -> AI Confidence: **99.24%**
300. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/FallbackOpenFileItem.cs`** -> AI Confidence: **99.24%**
301. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/ActionsListContextItem.cs`** -> AI Confidence: **99.24%**
302. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/DirectoryExplorePage.cs`** -> AI Confidence: **99.24%**
303. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/IndexerPage.cs`** -> AI Confidence: **99.24%**
304. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Helpers/FancyZonesDataService.cs`** -> AI Confidence: **99.24%**
305. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Helpers/ResultHelper.cs`** -> AI Confidence: **99.24%**
306. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsServices/Helpers/ServiceHelper.cs`** -> AI Confidence: **99.24%**
307. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsTerminal/Pages/ProfilesListPage.cs`** -> AI Confidence: **99.24%**
308. **`src/modules/colorPicker/ColorPickerUI/Helpers/AppStateHandler.cs`** -> AI Confidence: **99.24%**
309. **`src/modules/colorPicker/ColorPickerUI/Helpers/ZoomWindowHelper.cs`** -> AI Confidence: **99.24%**
310. **`src/modules/colorPicker/ColorPickerUI/Settings/UserSettings.cs`** -> AI Confidence: **99.24%**
311. **`src/modules/fancyzones/FancyZones.UITests/LayoutApplyHotKeyTests.cs`** -> AI Confidence: **99.24%**
312. **`src/modules/fancyzones/editor/FancyZonesEditor/App.xaml.cs`** -> AI Confidence: **99.24%**
313. **`src/modules/imageresizer/ui/ImageResizerXAML/App.xaml.cs`** -> AI Confidence: **99.24%**
314. **`src/modules/imageresizer/ui/Models/ResizeBatch.cs`** -> AI Confidence: **99.24%**
315. **`src/modules/imageresizer/ui/Models/ResizeOperation.cs`** -> AI Confidence: **99.24%**
316. **`src/modules/imageresizer/ui/Properties/Settings.cs`** -> AI Confidence: **99.24%**
317. **`src/modules/imageresizer/ui/ViewModels/InputViewModel.cs`** -> AI Confidence: **99.24%**
318. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Settings/SettingsManager.cs`** -> AI Confidence: **99.24%**
319. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/Win32Program.cs`** -> AI Confidence: **99.24%**
320. **`src/modules/launcher/Plugins/Microsoft.Plugin.Shell/Main.cs`** -> AI Confidence: **99.24%**
321. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Calculator/Main.cs`** -> AI Confidence: **99.24%**
322. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Registry/Helper/RegistryHelper.cs`** -> AI Confidence: **99.24%**
323. **`src/modules/launcher/PowerLauncher/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
324. **`src/modules/launcher/PowerLauncher/SettingsReader.cs`** -> AI Confidence: **99.24%**
325. **`src/modules/launcher/PowerLauncher/ViewModel/ResultsViewModel.cs`** -> AI Confidence: **99.24%**
326. **`src/modules/launcher/Wox.Infrastructure/Storage/JsonStorage`1.cs`** -> AI Confidence: **99.24%**
327. **`src/modules/peek/Peek.FilePreviewer/FilePreview.xaml.cs`** -> AI Confidence: **99.24%**
328. **`src/modules/peek/Peek.FilePreviewer/Previewers/WebBrowserPreviewer/Helpers/MonacoHelper.cs`** -> AI Confidence: **99.24%**
329. **`src/modules/peek/Peek.UI/MainWindowViewModel.cs`** -> AI Confidence: **99.24%**
330. **`src/modules/peek/Peek.UI/PeekXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
331. **`src/modules/peek/Peek.UITests/PeekFilePreviewTests.cs`** -> AI Confidence: **99.24%**
332. **`src/modules/powerdisplay/PowerDisplay.Lib/Drivers/DDC/DdcCiController.cs`** -> AI Confidence: **99.24%**
333. **`src/modules/powerdisplay/PowerDisplay/Helpers/MonitorManager.cs`** -> AI Confidence: **99.24%**
334. **`src/modules/powerdisplay/PowerDisplay/PowerDisplayXAML/App.xaml.cs`** -> AI Confidence: **99.24%**
335. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.24%**
336. **`src/modules/previewpane/SvgPreviewHandler/SvgPreviewControl.cs`** -> AI Confidence: **99.24%**
337. **`src/modules/registrypreview/RegistryPreview/RegistryPreviewXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
338. **`src/settings-ui/Settings.UI.Library/Utilities/SetAdditionalSettingsCommandLineCommand.cs`** -> AI Confidence: **99.24%**
339. **`src/settings-ui/Settings.UI/Helpers/NavigablePage.cs`** -> AI Confidence: **99.24%**
340. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.WASDK.cs`** -> AI Confidence: **99.24%**
341. **`src/settings-ui/Settings.UI/SettingsXAML/Views/ShellPage.xaml.cs`** -> AI Confidence: **99.24%**
342. **`src/settings-ui/Settings.UI/ViewModels/CmdNotFoundViewModel.cs`** -> AI Confidence: **99.24%**
343. **`src/settings-ui/Settings.UI/ViewModels/ColorPickerViewModel.cs`** -> AI Confidence: **99.24%**
344. **`src/settings-ui/Settings.UI/ViewModels/ImageResizerViewModel.cs`** -> AI Confidence: **99.24%**
345. **`src/settings-ui/Settings.UI/ViewModels/KeyboardManagerViewModel.cs`** -> AI Confidence: **99.24%**
346. **`src/settings-ui/Settings.UI/ViewModels/MouseWithoutBordersViewModel.cs`** -> AI Confidence: **99.24%**
347. **`src/settings-ui/Settings.UI/ViewModels/NewPlusViewModel.cs`** -> AI Confidence: **99.24%**
348. **`src/settings-ui/Settings.UI/ViewModels/PageViewModelBase.cs`** -> AI Confidence: **99.24%**
349. **`src/settings-ui/Settings.UI/ViewModels/PeekViewModel.cs`** -> AI Confidence: **99.24%**
350. **`src/settings-ui/Settings.UI/ViewModels/PowerOcrViewModel.cs`** -> AI Confidence: **99.24%**
351. **`src/common/notifications/notifications.cpp`** -> AI Confidence: **99.24%**
352. **`src/modules/MeasureTool/MeasureToolCore/OverlayUI.cpp`** -> AI Confidence: **99.24%**
353. **`src/modules/MeasureTool/MeasureToolCore/ScreenCapturing.cpp`** -> AI Confidence: **99.24%**
354. **`src/modules/MouseUtils/FindMyMouse/FindMyMouse.cpp`** -> AI Confidence: **99.24%**
355. **`src/modules/MouseUtils/MouseJump/dllmain.cpp`** -> AI Confidence: **99.24%**
356. **`src/modules/PowerOCR/PowerOCRModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
357. **`src/modules/ShortcutGuide/ShortcutGuideModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
358. **`src/modules/Workspaces/WorkspacesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
359. **`src/modules/Workspaces/WorkspacesSnapshotTool/main.cpp`** -> AI Confidence: **99.24%**
360. **`src/modules/colorPicker/ColorPicker/dllmain.cpp`** -> AI Confidence: **99.24%**
361. **`src/modules/fancyzones/FancyZonesLib/EditorParameters.cpp`** -> AI Confidence: **99.24%**
362. **`src/modules/fancyzones/FancyZonesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
363. **`src/modules/imageresizer/ImageResizerContextMenu/dllmain.cpp`** -> AI Confidence: **99.24%**
364. **`src/modules/launcher/Microsoft.Launcher/dllmain.cpp`** -> AI Confidence: **99.24%**
365. **`src/modules/powerrename/PowerRenameContextMenu/dllmain.cpp`** -> AI Confidence: **99.24%**
366. **`src/modules/registrypreview/RegistryPreviewExt/dllmain.cpp`** -> AI Confidence: **99.24%**
367. **`tools/BugReportTool/BugReportTool/Main.cpp`** -> AI Confidence: **99.24%**
368. **`tools/FancyZones_DrawLayoutTest/FancyZones_DrawLayoutTest.cpp`** -> AI Confidence: **99.24%**
369. **`tools/StylesReportTool/StylesReportTool.cpp`** -> AI Confidence: **99.24%**
370. **`src/common/ManagedTelemetry/Telemetry/EtwTrace.cs`** -> AI Confidence: **99.23%**
371. **`src/common/UITestAutomation/ScreenRecording.cs`** -> AI Confidence: **99.23%**
372. **`src/common/UITestAutomation/UITestBase.cs`** -> AI Confidence: **99.23%**
373. **`src/dsc/PowerToys.Settings.DSC.Schema.Generator/DSCGeneration.cs`** -> AI Confidence: **99.23%**
374. **`src/modules/Workspaces/WorkspacesEditor/WorkspacesEditorPage.xaml.cs`** -> AI Confidence: **99.23%**
375. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandBarViewModel.cs`** -> AI Confidence: **99.23%**
376. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandItemViewModel.cs`** -> AI Confidence: **99.23%**
377. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/TextBoxCaretColor.cs`** -> AI Confidence: **99.23%**
378. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.Bookmarks.UnitTests/BookmarkResolverTests.cs`** -> AI Confidence: **99.23%**
379. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AllAppsCommandProvider.cs`** -> AI Confidence: **99.23%**
380. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/ReparsePoint.cs`** -> AI Confidence: **99.23%**
381. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Storage/Win32ProgramRepository.cs`** -> AI Confidence: **99.23%**
382. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Helpers/RegistryHelper.cs`** -> AI Confidence: **99.23%**
383. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Interop/KeyboardMappingService.cs`** -> AI Confidence: **99.23%**
384. **`src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.UnitConverter/InputInterpreter.cs`** -> AI Confidence: **99.23%**
385. **`src/modules/launcher/Plugins/Microsoft.Plugin.Folder.UnitTests/InternalQueryFolderTests.cs`** -> AI Confidence: **99.23%**
386. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.History/Main.cs`** -> AI Confidence: **99.23%**
387. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate/Components/ResultHelper.cs`** -> AI Confidence: **99.23%**
388. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate/Components/SearchController.cs`** -> AI Confidence: **99.23%**
389. **`src/modules/launcher/PowerLauncher/Plugin/PluginConfig.cs`** -> AI Confidence: **99.23%**
390. **`src/modules/peek/Peek.FilePreviewer/Previewers/PreviewerFactory.cs`** -> AI Confidence: **99.23%**
391. **`src/modules/registrypreview/RegistryPreview.FuzzTests/FuzzTests.cs`** -> AI Confidence: **99.23%**
392. **`src/settings-ui/QuickAccess.UI/Services/QuickAccessCoordinator.cs`** -> AI Confidence: **99.23%**
393. **`src/settings-ui/Settings.UI.Library/SettingsFactory.cs`** -> AI Confidence: **99.23%**
394. **`src/settings-ui/Settings.UI.XamlIndexBuilder/Program.cs`** -> AI Confidence: **99.23%**
395. **`src/settings-ui/Settings.UI/ViewModels/FancyZonesViewModel.cs`** -> AI Confidence: **99.23%**
396. **`src/modules/MeasureTool/MeasureToolModuleInterface/dllmain.cpp`** -> AI Confidence: **99.23%**
397. **`src/modules/Workspaces/WorkspacesLib/SteamGameHelper.cpp`** -> AI Confidence: **99.23%**
398. **`src/modules/alwaysontop/AlwaysOnTop/Settings.cpp`** -> AI Confidence: **99.23%**
399. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData.cpp`** -> AI Confidence: **99.23%**
400. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/CustomLayouts.cpp`** -> AI Confidence: **99.23%**
401. **`src/modules/previewpane/powerpreview/dllmain.cpp`** -> AI Confidence: **99.23%**
402. **`src/common/sysinternals/dll.c`** -> AI Confidence: **99.23%**
403. **`src/modules/LightSwitch/LightSwitchService/LightSwitchStateManager.cpp`** -> AI Confidence: **99.22%**
404. **`src/common/Common.UI.Controls/Controls/KeyVisual/KeyVisual.xaml.cs`** -> AI Confidence: **99.2%**
405. **`src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs`** -> AI Confidence: **99.2%**
406. **`src/common/SettingsAPI/FileWatcher.cpp`** -> AI Confidence: **99.2%**
407. **`src/modules/Workspaces/WorkspacesLib/trace.cpp`** -> AI Confidence: **99.2%**
408. **`src/modules/ZoomIt/ZoomIt/LoopbackCapture.cpp`** -> AI Confidence: **99.2%**
409. **`src/modules/ZoomIt/ZoomIt/Utility.cpp`** -> AI Confidence: **99.2%**
410. **`src/common/UITestAutomation/Element/Element.cs`** -> AI Confidence: **99.18%**
411. **`src/dsc/v3/PowerToys.DSC/DSCResources/SettingsResource.cs`** -> AI Confidence: **99.18%**
412. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/Converters/DateTimeToFriendlyStringConverter.cs`** -> AI Confidence: **99.18%**
413. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.18%**
414. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/DataPackageHelpers.cs`** -> AI Confidence: **99.18%**
415. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/KernelExtensions.cs`** -> AI Confidence: **99.18%**
416. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActionKernelQueryCacheService.cs`** -> AI Confidence: **99.18%**
417. **`src/modules/EnvironmentVariables/EnvironmentVariables/EnvironmentVariablesXAML/App.xaml.cs`** -> AI Confidence: **99.18%**
418. **`src/modules/Hosts/Hosts/HostsXAML/App.xaml.cs`** -> AI Confidence: **99.18%**
419. **`src/modules/Hosts/HostsUILib/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.18%**
420. **`src/modules/MouseUtils/MouseUtils.UITests/MousePointerCrosshairsTests.cs`** -> AI Confidence: **99.18%**
421. **`src/modules/PowerOCR/PowerOCR/Helpers/ImageMethods.cs`** -> AI Confidence: **99.18%**
422. **`src/modules/PowerOCR/PowerOCR/Helpers/OcrExtensions.cs`** -> AI Confidence: **99.18%**
423. **`src/modules/Workspaces/WorkspacesLauncherUI/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.18%**
424. **`src/modules/awake/Awake/Program.cs`** -> AI Confidence: **99.18%**
425. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandProviderWrapper.cs`** -> AI Confidence: **99.18%**
426. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Dock/DockViewModel.cs`** -> AI Confidence: **99.18%**
427. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/DockAppearanceSettingsViewModel.cs`** -> AI Confidence: **99.18%**
428. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/Controls/ImageContentViewer.xaml.cs`** -> AI Confidence: **99.18%**
429. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/MarkdownImageProviders/ImageSourceFactory.cs`** -> AI Confidence: **99.18%**
430. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Services/ThemeService.cs`** -> AI Confidence: **99.18%**
431. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/DockSettingsPage.xaml.cs`** -> AI Confidence: **99.18%**
432. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/ExtensionsPage.xaml.cs`** -> AI Confidence: **99.18%**
433. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/GeneralPage.xaml.cs`** -> AI Confidence: **99.18%**
434. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ViewModels/DevRibbonViewModel.cs`** -> AI Confidence: **99.18%**
435. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.System.UnitTests/QueryTests.cs`** -> AI Confidence: **99.18%**
436. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.UI.ViewModels.UnitTests/RecentCommandsTests.cs`** -> AI Confidence: **99.18%**
437. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.UITests/CommandPaletteTestBase.cs`** -> AI Confidence: **99.18%**
438. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AllAppsPage.cs`** -> AI Confidence: **99.18%**
439. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Commands/LaunchBookmarkCommand.cs`** -> AI Confidence: **99.18%**
440. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Pages/BookmarkPlaceholderForm.cs`** -> AI Confidence: **99.18%**
441. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.ClipboardHistory/Helpers/Analyzers/WebLinkMetadataProvider.cs`** -> AI Confidence: **99.18%**
442. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/DirectoryPage.cs`** -> AI Confidence: **99.18%**
443. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/ExploreListItem.cs`** -> AI Confidence: **99.18%**
444. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Modules/KeyboardManagerModuleCommandProvider.cs`** -> AI Confidence: **99.18%**
445. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Modules/WorkspacesModuleCommandProvider.cs`** -> AI Confidence: **99.18%**
446. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Pages/FancyZonesMonitorsPage.cs`** -> AI Confidence: **99.18%**
447. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Pages/RegistryListPage.cs`** -> AI Confidence: **99.18%**
448. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.System/Helpers/Commands.cs`** -> AI Confidence: **99.18%**
449. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WebSearch/WebSearchTopLevelCommandItem.cs`** -> AI Confidence: **99.18%**
450. **`src/modules/cmdpal/ext/SamplePagesExtension/Pages/SampleListPage.cs`** -> AI Confidence: **99.18%**
451. **`src/modules/colorPicker/ColorPickerUI/ViewModels/ColorEditorViewModel.cs`** -> AI Confidence: **99.18%**
452. **`src/modules/fancyzones/FancyZones.UITests/OneZoneSwitchTests.cs`** -> AI Confidence: **99.18%**
453. **`src/modules/fancyzones/FancyZones.UITests/Utils/ZoneSwitchHelper.cs`** -> AI Confidence: **99.18%**
454. **`src/modules/fancyzones/FancyZonesEditor.UITests/Utils/FancyZonesEditorHelper.cs`** -> AI Confidence: **99.18%**
455. **`src/modules/imageresizer/tests/Properties/SettingsTests.cs`** -> AI Confidence: **99.18%**
456. **`src/modules/imageresizer/ui/ImageResizerXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.18%**
457. **`src/modules/imageresizer/ui/Models/ResizeSize.cs`** -> AI Confidence: **99.18%**
458. **`src/modules/imageresizer/ui/ViewModels/ProgressViewModel.cs`** -> AI Confidence: **99.18%**
459. **`src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.UnitConverter/Main.cs`** -> AI Confidence: **99.18%**
460. **`src/modules/launcher/Plugins/Microsoft.Plugin.Indexer/ContextMenuLoader.cs`** -> AI Confidence: **99.18%**
461. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program.UnitTests/Programs/Win32Tests.cs`** -> AI Confidence: **99.18%**
462. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Main.cs`** -> AI Confidence: **99.18%**
463. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/UWP.cs`** -> AI Confidence: **99.18%**
464. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/UWPApplication.cs`** -> AI Confidence: **99.18%**
465. **`src/modules/launcher/Plugins/Microsoft.Plugin.WindowWalker/Main.cs`** -> AI Confidence: **99.18%**
466. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.OneNote/Main.cs`** -> AI Confidence: **99.18%**
467. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.PowerToys/Main.cs`** -> AI Confidence: **99.18%**
468. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.System/Components/Commands.cs`** -> AI Confidence: **99.18%**
469. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.WindowsSettings/Helper/ContextMenuHelper.cs`** -> AI Confidence: **99.18%**
470. **`src/modules/launcher/PowerLauncher/Helper/SingleInstance`1.cs`** -> AI Confidence: **99.18%**
471. **`src/modules/launcher/PowerLauncher/Plugin/PluginManager.cs`** -> AI Confidence: **99.18%**
472. **`src/modules/launcher/PowerLauncher/PublicAPIInstance.cs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Services/Sanitizer/SecretKeyValueRulesProviderTests.cs` -> **82.1257%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `111` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19571` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AppListItem.cs` (CSHARP) -> Cumulative Risk: **774.01**
- **Archetype:** `file_cluster_4` (Distance: 13.009 IQR)
- **Magnitude:** 360.06 | **LOC:** 269 | **CtrlFlow:** 45.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `BuildDetails` (Impact: 34.8), `FetchIcon` (Impact: 16.0), `TryLoadThumbnail` (Impact: 15.2)

### 2. `src/modules/peek/Peek.FilePreviewer/Previewers/WebBrowserPreviewer/WebBrowserPreviewer.cs` (CSHARP) -> Cumulative Risk: **752.28**
- **Archetype:** `file_cluster_4` (Distance: 11.331 IQR)
- **Magnitude:** 163.2 | **LOC:** 177 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9768%)
- **Heaviest Functions:** `LoadDisplayInfoAsync` (Impact: 22.5), `HasFailedLoadingPreview` (Impact: 6.2), `Dispose` (Impact: 5.7)

### 3. `src/modules/cmdpal/Microsoft.CmdPal.Common/Helpers/ThrottledDebouncedAction.cs` (CSHARP) -> Cumulative Risk: **747.82**
- **Archetype:** `file_cluster_4` (Distance: 12.225 IQR)
- **Magnitude:** 163.82 | **LOC:** 164 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Invoke` (Impact: 38.7), `Cancel` (Impact: 6.7), `ThrottledDebouncedAction` (Impact: 2.5)

### 4. `src/modules/cmdpal/ext/SamplePagesExtension/Pages/SendMessageCommand.cs` (CSHARP) -> Cumulative Risk: **738.5**
- **Archetype:** `file_cluster_4` (Distance: 11.246 IQR)
- **Magnitude:** 116.5 | **LOC:** 135 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.6851%)
- **Heaviest Functions:** `Invoke` (Impact: 23.1), `Invoke` (Impact: 12.0), `Invoke` (Impact: 10.5)

### 5. `src/common/UnitTests-CommonUtils/Serialized.Tests.cpp` (CPP) -> Cumulative Risk: **708.31**
- **Archetype:** `file_cluster_8` (Distance: 13.655 IQR)
- **Magnitude:** 320.34 | **LOC:** 287 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9993%), Cognitive Load (98.8366%)
- **Heaviest Functions:** `TEST_CLASS` (Impact: 28.4), `TEST_METHOD` (Impact: 12.8), `TEST_METHOD` (Impact: 8.5)

### 6. `src/modules/peek/Peek.FilePreviewer/Previewers/MediaPreviewer/ImagePreviewer.cs` (CSHARP) -> Cumulative Risk: **707.01**
- **Archetype:** `file_cluster_4` (Distance: 11.42 IQR)
- **Magnitude:** 206.02 | **LOC:** 187 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), State Flux (99.5568%)
- **Heaviest Functions:** `GetPreviewSizeAsync` (Impact: 13.4), `UpdateMaxImageSize` (Impact: 12.4), `LoadFullQualityImageAsync` (Impact: 8.0)

### 7. `src/common/UnitTests-CommonUtils/LoggerHelper.Tests.cpp` (CPP) -> Cumulative Risk: **700.38**
- **Archetype:** `file_cluster_4` (Distance: 11.875 IQR)
- **Magnitude:** 138.36 | **LOC:** 181 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `TEST_CLASS` (Impact: 21.2), `TEST_METHOD` (Impact: 6.8), `TEST_METHOD` (Impact: 6.8)

### 8. `src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/Icons/CachedIconSourceProvider.cs` (CSHARP) -> Cumulative Risk: **693.95**
- **Archetype:** `file_cluster_4` (Distance: 12.003 IQR)
- **Magnitude:** 84.74 | **LOC:** 104 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9982%), Concurrency (99.713%)
- **Heaviest Functions:** `GetOrCreateSlowPath` (Impact: 7.8), `IconCacheKey` (Impact: 5.6), `GetIconSource` (Impact: 3.9)

### 9. `src/modules/LightSwitch/LightSwitchService/LightSwitchSettings.cpp` (CPP) -> Cumulative Risk: **693.88**
- **Archetype:** `file_cluster_4` (Distance: 13.066 IQR)
- **Magnitude:** 282.52 | **LOC:** 302 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (97.8273%), Safety Score (93.0254%)
- **Heaviest Functions:** `LightSwitchSettings::LoadSettings` (Impact: 49.2), `LightSwitchSettings::InitFileWatcher` (Impact: 16.6), `LightSwitchSettings` (Impact: 11.1)

### 10. `src/common/UnitTests-CommonUtils/Resources.Tests.cpp` (CPP) -> Cumulative Risk: **692.64**
- **Archetype:** `file_cluster_8` (Distance: 11.985 IQR)
- **Magnitude:** 124.62 | **LOC:** 145 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Cognitive Load (97.0227%)
- **Heaviest Functions:** `TEST_CLASS` (Impact: 18.0), `TEST_METHOD` (Impact: 6.9), `TEST_METHOD` (Impact: 3.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.806 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.385 IQR)
- **Top Global Matches:** file_cluster_8: 15.806, file_cluster_11: 16.101, file_cluster_13: 16.139
- **Magnitude:** 14782.14 | **LOC:** 18014 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.5286%), Tech Debt (10.238%)
**Top Internal Functions/Classes:**
  * `RunPanoramaStitchSelfTest` (Impact: 508.9)
  * `BuildFixedOverlayMask` (Impact: 483.1)
  * `RepairOverlayDarkBands` (Impact: 210.7)
  * `RepairSuppressedOverlayHoles` (Impact: 107.6)
  * `LogGapBridgeProbeDiagnostics` (Impact: 87.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2249`, `structural_boundaries: 320`, `args: 430`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 17`, `state_mutation: 12086`, `dead_code: 5`, `duplicate_logic: 4`, `orphaned_logic: 20`
* *Architecture:* `io: 42`, `api: 1`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 7`, `immutability_locks: 1249`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` commctrl.h, atomic, cmath, WindowsVersions.h, functional, arm_neon.h, pch.h, emmintrin.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.204 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.435 IQR)
- **Top Global Matches:** file_cluster_8: 15.204, file_cluster_4: 15.315, file_cluster_13: 15.479
- **Magnitude:** 6636.04 | **LOC:** 5443 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (77.0763%), Tech Debt (8.6546%)
**Top Internal Functions/Classes:**
  * `TimelineSubclassProc` (Impact: 678.3)
  * `VideoRecordingSession::ShowTrimDialogInt` (Impact: 637.5)
  * `VideoRecordingSession::TrimDialogProc` (Impact: 499.2)
  * `StartPlaybackAsync` (Impact: 441.9)
    * *Intent:* // The selection (trimStart..trimEnd) determines what will be trimmed, // but playback may start bef...
  * `LoadGifFrames` (Impact: 337.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 285`, `args: 190`, `func_start: 59`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 2`, `state_mutation: 3651`, `orphaned_logic: 4`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 132`, `import: 10`
* *Defense:* `safety: 66`, `sync_locks: 10`, `immutability_locks: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Windows.Graphics.Imaging.h, shlwapi.h, CaptureFrameWait.h, VideoRecordingSession.h, mmsystem.h, pch.h, Windows.Media.h, filesystem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.005 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.572 IQR)
- **Top Global Matches:** file_cluster_8: 15.005, file_cluster_13: 15.303, file_cluster_7: 15.361
- **Magnitude:** 5865.7 | **LOC:** 11756 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (94.0604%), Tech Debt (8.265%)
**Top Internal Functions/Classes:**
  * `OptionsTabProc` (Impact: 692.9)
  * `OptionsProc` (Impact: 319.5)
  * `RestoreScreenSaverSettings` (Impact: 145.6)
  * `LiveZoomWndProc` (Impact: 128.4)
  * `GroupBoxSubclassProc` (Impact: 126.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 962`, `structural_boundaries: 227`, `args: 499`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 3295`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 31`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 3`, `immutability_locks: 44`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` ZoomItSettings.h, logger.h, process_path.h, GifRecordingSession.h, WindowsVersions.h, EtwTrace.h, array, zoomit.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.61 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.205 IQR)
- **Top Global Matches:** file_cluster_8: 12.61, file_cluster_16: 12.782, file_cluster_7: 12.798
- **Magnitude:** 1431.0 | **LOC:** 2376 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (48.5741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_on_mouse_move` (Impact: 331.0)
  * `from_csv_line` (Impact: 304.0)
  * `_load_cursor_log` (Impact: 145.0)
  * `_export_analysis` (Impact: 24.0)
  * `_on_algorithm_change` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 175`, `args: 64`, `func_start: 63`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 539`
* *Architecture:* `io: 3`, `api: 26`, `import: 10`
* *Defense:* `safety: 15`, `doc: 140`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` re, dataclasses, typing, csv, argparse, sys, enum, json...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.991 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.664 IQR)
- **Top Global Matches:** file_cluster_8: 13.991, file_cluster_13: 14.263, file_cluster_7: 14.422
- **Magnitude:** 1275.24 | **LOC:** 948 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.3063%), Tech Debt (66.1919%)
**Top Internal Functions/Classes:**
  * `D2DOverlayWindow::render` (Impact: 146.6)
  * `get_window_state` (Impact: 37.2)
  * `D2DOverlayWindow::show` (Impact: 36.2)
  * `render_arrow` (Impact: 28.3)
  * `D2DOverlaySVG::get_thumbnail_rect_and_sc` (Impact: 18.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 93`, `args: 101`, `func_start: 32`
* *Risk/State:* `state_mutation: 855`, `orphaned_logic: 27`
* *Architecture:* `concurrency: 12`, `import: 10`
* *Defense:* `safety: 1`, `sync_locks: 12`, `immutability_locks: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` resources.h, start_visible.h, trace.h, overlay_window.h, resource.h, monitors.h, shortcut_guide.h, MsWindowsSettings.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.429 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.957 IQR)
- **Top Global Matches:** file_cluster_8: 13.429, file_cluster_13: 13.581, file_cluster_11: 13.836
- **Magnitude:** 1116.62 | **LOC:** 1829 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 22.2%
- **Risk Profile:** Cognitive Load (63.1645%), Tech Debt (17.4464%)
**Top Internal Functions/Classes:**
  * `UninstallPackageIdentityMSIXCA` (Impact: 210.1)
  * `SetBundleInstallLocationCA` (Impact: 33.3)
  * `TerminateProcessesCA` (Impact: 30.0)
  * `InstallPackageIdentityMSIXCA` (Impact: 28.2)
  * `UninstallDSCModuleCA` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 109`, `args: 130`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 584`, `planned_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 8`, `import: 24`
* *Defense:* `safety: 26`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` clean_video_conference.h, string_view, gpo.h, Windows.Management.Deployment.h, logger.h, version.h, UserEnv.h, processthreadsapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/MainWindow.xaml.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.404 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.664 IQR)
- **Top Global Matches:** file_cluster_8: 13.404, file_cluster_13: 13.608, file_cluster_11: 13.799
- **Magnitude:** 1085.54 | **LOC:** 1394 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.037%), Tech Debt (87.0207%)
**Top Internal Functions/Classes:**
  * `MainWindow::UpdateMetadataShortcuts` (Impact: 163.0)
  * `MainWindow::SetCheckboxesFromFlags` (Impact: 41.5)
  * `MainWindow::SetHandlers` (Impact: 27.9)
  * `MainWindow::ValidateFlags` (Impact: 22.8)
  * `MainWindow::CreateShellItemArrayFromPath` (Impact: 21.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 185`, `args: 229`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 624`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 35`
* *Architecture:* `import: 23`
* *Defense:* `safety: 5`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` atlstr.h, trace.h, sstream, settings.h, logger.h, MainWindow.g.cpp, Windows.UI.ViewManagement.h, process_path.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/fancyzones/FancyZonesLib/FancyZones.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.505 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.124 IQR)
- **Top Global Matches:** file_cluster_13: 13.505, file_cluster_8: 13.529, file_cluster_11: 13.873
- **Magnitude:** 1059.44 | **LOC:** 1194 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (92.9458%), Tech Debt (54.5438%)
**Top Internal Functions/Classes:**
  * `FancyZones::OnKeyDown` (Impact: 282.0)
  * `FancyZones::WndProc` (Impact: 140.3)
  * `FancyZones::UpdateWorkAreas` (Impact: 104.8)
    * *Intent:* // Changes in taskbar position resulted in different size of work area.
  * `HandleWinHookEvent` (Impact: 31.4)
  * `FancyZones::SettingsUpdate` (Impact: 26.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 110`, `args: 91`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `state_mutation: 304`, `orphaned_logic: 19`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 34`
* *Defense:* `safety: 45`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` VirtualDesktop.h, FileWatcher.h, EventWaiter.h, FancyZonesData.h, FancyZonesWindowProcessing.h, trace.h, logger.h, EditorParameters.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/Helpers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.977 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.277 IQR)
- **Top Global Matches:** file_cluster_8: 13.977, file_cluster_13: 14.223, file_cluster_17: 14.306
- **Magnitude:** 1051.82 | **LOC:** 927 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (92.6849%), Tech Debt (40.4609%)
**Top Internal Functions/Classes:**
  * `GetTransformedFileName` (Impact: 120.4)
  * `GetEnumeratedFileName` (Impact: 76.0)
  * `GetMetadataFileName` (Impact: 19.1)
  * `isMetadataUsed` (Impact: 13.8)
  * `DataObjectContainsRenamableItem` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 40`, `args: 35`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 719`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `import: 10`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MetadataTypes.h, ShlGuid.h, cstring, Helpers.h, regex, unordered_map, algorithm, pch.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.466 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.183 IQR)
- **Top Global Matches:** file_cluster_8: 13.466, file_cluster_13: 13.742, file_cluster_7: 13.925
- **Magnitude:** 1030.92 | **LOC:** 827 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (79.279%), Tech Debt (43.2735%)
**Top Internal Functions/Classes:**
  * `MonitorTopology::IsOnOuterEdge` (Impact: 263.0)
  * `MonitorTopology::FindNearestOppositeEdge` (Impact: 56.6)
  * `MonitorTopology::GetWrapDestination` (Impact: 50.4)
  * `MonitorTopology::PrioritizeEdgeByDirecti` (Impact: 48.4)
  * `MonitorTopology::FindOppositeOuterEdge` (Impact: 38.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 43`, `args: 25`, `func_start: 10`
* *Risk/State:* `state_mutation: 473`, `orphaned_logic: 10`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MonitorTopology.h, CursorWrapCore.h, algorithm, pch.h, logger.h, cmath
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.888 IQR)
- **Top Global Matches:** file_cluster_13: 12.888, file_cluster_8: 12.925, file_cluster_2: 12.962
- **Magnitude:** 990.98 | **LOC:** 2914 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (29.3739%), Tech Debt (19.6503%)
**Top Internal Functions/Classes:**
  * `ReadFormattedData` (Impact: 105.8)
  * `CalculateDataColumnCharWidth` (Impact: 103.3)
  * `Canvas_PaintSurface` (Impact: 87.4)
  * `DrawSelectionGeometry` (Impact: 47.8)
  * `ConvertPositionToOffset` (Impact: 36.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 145`, `args: 91`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 267`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 72`, `import: 21`
* *Defense:* `safety: 47`, `doc: 177`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.Collections.Generic, Windows.Foundation, System.Runtime.CompilerServices, Windows.ApplicationModel.DataTransfer, Windows.System, Microsoft.UI.Xaml.Media, System.IO...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.73 IQR)
- **Top Global Matches:** file_cluster_13: 13.73, file_cluster_8: 13.732, file_cluster_4: 13.773
- **Magnitude:** 942.1 | **LOC:** 1098 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (78.8627%), Tech Debt (34.8645%)
**Top Internal Functions/Classes:**
  * `FetchItems` (Impact: 331.3)
  * `FetchProperty` (Impact: 56.1)
  * `OnSearchTextBoxUpdated` (Impact: 27.1)
  * `SelectedItemPropertyChanged` (Impact: 25.9)
  * `InvokeSecondaryCommand` (Impact: 22.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 107`, `args: 66`, `func_start: 147`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 191`, `planned_debt: 2`, `orphaned_logic: 8`
* *Architecture:* `api: 13`, `concurrency: 48`, `import: 13`
* *Defense:* `safety: 95`, `doc: 9`, `sync_locks: 14`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Collections.ObjectModel, Microsoft.CmdPal.Common, Microsoft.CmdPal.UI.ViewModels.Models, CommunityToolkit.Mvvm.Messaging, Microsoft.CmdPal.UI.ViewModels.Messages, CommunityToolkit.Mvvm.Input, Microsoft.CmdPal.Common.Helpers, Microsoft.CommandPalette.Extensions.Toolkit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.742 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.388 IQR)
- **Top Global Matches:** file_cluster_8: 13.742, file_cluster_13: 13.957, file_cluster_7: 14.189
- **Magnitude:** 923.48 | **LOC:** 752 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.031%), Tech Debt (75.134%)
**Top Internal Functions/Classes:**
  * `GetShortcutRemapByType` (Impact: 138.4)
  * `GetShortcutRemapCountByType` (Impact: 67.2)
  * `AddShortcutRemap` (Impact: 55.0)
  * `GetShortcutRemap` (Impact: 34.4)
  * `DeleteShortcutRemap` (Impact: 20.4)
    * *Intent:* // Function to delete a shortcut remapping
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 73`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 489`, `orphaned_logic: 22`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` string, keyboard_layout.h, cstring, KeyboardManagerEditorLibraryWrapper.h, memory, logger_helper.h, KeyboardManagerEditor.h, algorithm...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/WICMetadataExtractor.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.875 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.049 IQR)
- **Top Global Matches:** file_cluster_8: 13.875, file_cluster_13: 14.003, file_cluster_11: 14.221
- **Magnitude:** 870.0 | **LOC:** 1116 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.186%), Tech Debt (36.3264%)
**Top Internal Functions/Classes:**
  * `ParseIso8601DateTime` (Impact: 110.7)
  * `ValidateAndBuildSystemTime` (Impact: 49.5)
  * `ParseExifDateTime` (Impact: 49.0)
  * `WICMetadataExtractor::InitializeWIC` (Impact: 21.4)
  * `WICMetadataExtractor::ExtractAllXMPField` (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 50`, `args: 16`, `func_start: 12`
* *Risk/State:* `state_mutation: 576`, `orphaned_logic: 9`
* *Architecture:* `concurrency: 1`, `import: 9`
* *Defense:* `safety: 4`, `sync_locks: 1`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shlwapi.h, comdef.h, WICMetadataExtractor.h, algorithm, sstream, pch.h, iomanip, cwctype...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.671 IQR)
- **Top Global Matches:** file_cluster_8: 13.671, file_cluster_13: 13.721, file_cluster_11: 13.853
- **Magnitude:** 850.46 | **LOC:** 1485 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (27.2208%), Tech Debt (37.181%)
**Top Internal Functions/Classes:**
  * `ShouldReplacePasteAIConfiguration` (Impact: 93.7)
  * `MigrateLegacyAIEnablement` (Impact: 38.1)
  * `ApplyExternalProperties` (Impact: 24.6)
  * `IsServiceTypeAllowedByGPO` (Impact: 24.5)
  * `AdvancedPasteViewModel` (Impact: 23.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 160`, `args: 83`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `state_mutation: 229`, `duplicate_logic: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 41`, `import: 19`
* *Defense:* `safety: 197`, `doc: 4`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, Microsoft.PowerToys.Settings.UI.Library.Helpers, Microsoft.PowerToys.Settings.UI.Library, System.Collections.Generic, Microsoft.PowerToys.Settings.UI.Library.Utilities, System.Globalization, System.Collections.ObjectModel, Microsoft.PowerToys.Settings.UI.Helpers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/launcher/PowerLauncher/ViewModel/MainViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.593 IQR)
- **Top Global Matches:** file_cluster_8: 12.593, file_cluster_13: 12.636, file_cluster_11: 12.897
- **Magnitude:** 845.86 | **LOC:** 1365 | **CtrlFlow:** 50.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.2785%), Tech Debt (92.9417%)
**Top Internal Functions/Classes:**
  * `QueryResults` (Impact: 72.7)
  * `SetHotkey` (Impact: 25.2)
  * `RegisterHotkey` (Impact: 25.0)
  * `Dispose` (Impact: 20.7)
    * *Intent:* // Using OrdinalIgnoreCase since this is internal
  * `OpenResultsEvent` (Impact: 20.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 141`, `args: 88`, `func_start: 188`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 294`, `planned_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 16`
* *Architecture:* `api: 63`, `concurrency: 30`, `import: 28`
* *Defense:* `safety: 39`, `doc: 13`, `sync_locks: 7`, `immutability_locks: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System, System.Collections.Generic, Wox.Infrastructure.Hotkey, System.Globalization, System.Collections.ObjectModel, System.Threading.Tasks, System.Reflection, Common.UI...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/AdvancedPaste/AdvancedPasteModuleInterface/dllmain.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.135 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.012 IQR)
- **Top Global Matches:** file_cluster_8: 13.135, file_cluster_13: 13.278, file_cluster_17: 13.531
- **Magnitude:** 835.96 | **LOC:** 1083 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (88.4541%), Tech Debt (41.4881%)
**Top Internal Functions/Classes:**
  * `try_to_paste_as_plain_text` (Impact: 50.3)
  * `read_settings` (Impact: 42.6)
  * `on_hotkey` (Impact: 27.3)
  * `send_copy_selection` (Impact: 26.1)
  * `has_advanced_ai_provider` (Impact: 22.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 123`, `args: 119`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 505`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `io: 5`, `api: 2`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 20`, `sync_locks: 2`, `immutability_locks: 80`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` EventWaiter.h, AdvancedPasteConstants.h, trace.h, algorithm, logger.h, resources.h, settings_objects.h, shared_constants.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/fancyzones/FancyZonesLib/FancyZonesData/AppZoneHistory.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.608 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.189 IQR)
- **Top Global Matches:** file_cluster_8: 13.608, file_cluster_13: 13.668, file_cluster_11: 13.921
- **Magnitude:** 786.24 | **LOC:** 631 | **CtrlFlow:** 51.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6368%), Tech Debt (39.4367%)
**Top Internal Functions/Classes:**
  * `AppZoneHistory::RemoveAppLastZone` (Impact: 110.6)
  * `AppZoneHistory::SyncVirtualDesktops` (Impact: 37.1)
  * `AppZoneHistory::AdjustWorkAreaIds` (Impact: 23.6)
  * `AppZoneHistory::SetAppLastZones` (Impact: 23.2)
  * `AppZoneHistory::GetAppLastZoneIndexSet` (Impact: 21.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 94`, `args: 50`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 463`, `dead_code: 1`, `orphaned_logic: 10`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 13`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` AppZoneHistory.h, VirtualDesktop.h, process_path.h, JsonHelpers.h, util.h, call_tracer.h, GuidUtils.h, FancyZonesWindowProperties.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.152 IQR)
- **Top Global Matches:** file_cluster_8: 11.152, file_cluster_13: 11.544, file_cluster_7: 11.666
- **Magnitude:** 740.94 | **LOC:** 1123 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.9846%), Tech Debt (41.5202%)
**Top Internal Functions/Classes:**
  * `MoveRight` (Impact: 76.4)
  * `MoveLeft` (Impact: 69.4)
  * `MoveToMyNeighbourIfNeeded` (Impact: 60.6)
    * *Intent:* #if OLD_VERSION
  * `MoveToMyNeighbourIfNeeded` (Impact: 49.9)
    * *Intent:* /* Let's say we have 3 machines A, B, and C. A is the controller machine. * (x, y) is the current Mo...
  * `MoveUp` (Impact: 36.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 86`, `args: 39`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 166`, `dead_code: 3`, `duplicate_logic: 4`, `orphaned_logic: 10`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 3`, `sync_locks: 4`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.Linq, MouseWithoutBorders.Class, System.Threading, System.Diagnostics.CodeAnalysis, System.Drawing, System.Diagnostics, System.Windows.Forms...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmScreen.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.232 IQR)
- **Top Global Matches:** file_cluster_8: 12.232, file_cluster_0: 12.313, file_cluster_13: 12.427
- **Magnitude:** 740.2 | **LOC:** 1227 | **CtrlFlow:** 88.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.3477%), Tech Debt (30.6658%)
**Top Internal Functions/Classes:**
  * `HelperTimer_Tick` (Impact: 117.9)
  * `WndProc` (Impact: 78.9)
  * `PaintMyNameOnDesktop` (Impact: 48.6)
  * `ChangeIcon` (Impact: 27.6)
  * `ShowMessageOnLogonDesktop` (Impact: 27.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 24`, `args: 35`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 213`, `dead_code: 3`, `orphaned_logic: 16`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 9`, `import: 12`
* *Defense:* `safety: 25`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MouseWithoutBorders.Properties, System, MouseWithoutBorders.Core, System.Windows.Forms.Timer, System.IO, System.ComponentModel, MouseWithoutBorders.Class, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/Win32Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.615 IQR)
- **Top Global Matches:** file_cluster_8: 12.615, file_cluster_13: 12.649, file_cluster_11: 12.806
- **Magnitude:** 736.64 | **LOC:** 1097 | **CtrlFlow:** 47.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (57.0697%), Tech Debt (92.9946%)
**Top Internal Functions/Classes:**
  * `GetPathFromRegistrySubkey` (Impact: 46.7)
  * `GetAppFromPath` (Impact: 45.8)
    * *Intent:* // Function to get the Win32 application, given the path to the application
  * `LnkProgram` (Impact: 41.2)
  * `InternetShortcutProgram` (Impact: 40.6)
    * *Intent:* // This function filters Internet Shortcut programs
  * `ProgramPaths` (Impact: 40.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 174`, `args: 36`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `state_mutation: 200`, `dead_code: 1`, `duplicate_logic: 13`, `orphaned_logic: 6`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 58`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Windows.System, System, Microsoft.Win32, System.Threading.Tasks, System.Text.RegularExpressions, System.IO, System.Collections.Generic, System.Security...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.341 IQR)
- **Top Global Matches:** file_cluster_8: 12.341, file_cluster_17: 12.377, file_cluster_11: 12.503
- **Magnitude:** 736.1 | **LOC:** 1223 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.3163%), Tech Debt (84.7725%)
**Top Internal Functions/Classes:**
  * `ParseMembers` (Impact: 80.8)
  * `FindPackagesFromAssets` (Impact: 50.8)
  * `FindWinMdFromProjectReferences` (Impact: 37.3)
  * `FindPackagesFromConfig` (Impact: 33.3)
  * `libraries.EnumerateObject` (Impact: 27.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 282`, `args: 82`, `func_start: 104`, `class_start: 2`
* *Risk/State:* `state_mutation: 204`, `duplicate_logic: 4`, `orphaned_logic: 25`
* *Architecture:* `io: 76`, `api: 25`, `import: 8`
* *Defense:* `safety: 33`, `doc: 13`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Immutable, System.Reflection.PortableExecutable, System.Text.Json, System.Security.Cryptography, System.Reflection, System.Text.Json.Serialization, System.Reflection.Metadata, System.Xml.Linq
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/DemoType.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.454 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.764 IQR)
- **Top Global Matches:** file_cluster_4: 13.454, file_cluster_8: 13.78, file_cluster_11: 13.906
- **Magnitude:** 732.42 | **LOC:** 1446 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.8841%), Tech Debt (42.2215%)
**Top Internal Functions/Classes:**
  * `GetClipboard` (Impact: 78.3)
    * *Intent:* //---------------------------------------------------------------------------- // // GetClipboard //...
  * `DemoTypeController` (Impact: 40.4)
  * `StartDemoType` (Impact: 31.4)
  * `SendKeyInput` (Impact: 25.8)
    * *Intent:* //---------------------------------------------------------------------------- // // SendKeyInput //...
  * `IsAutoFormatTrigger` (Impact: 18.2)
    * *Intent:* //---------------------------------------------------------------------------- // // IsAutoFormatTri...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 49`, `args: 36`, `func_start: 21`, `class_start: 1`
* *Risk/State:* `state_mutation: 371`, `dead_code: 4`, `orphaned_logic: 11`
* *Architecture:* `concurrency: 72`, `import: 2`
* *Defense:* `safety: 9`, `sync_locks: 17`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DemoType.h, pch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/common/Shortcut.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.419 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.393 IQR)
- **Top Global Matches:** file_cluster_8: 12.419, file_cluster_13: 12.811, file_cluster_7: 12.94
- **Magnitude:** 720.44 | **LOC:** 945 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (92.5802%)
**Top Internal Functions/Classes:**
  * `Shortcut::IsKeyboardStateClearExceptShor` (Impact: 126.9)
  * `Shortcut::CheckModifiersKeyboardState` (Impact: 63.7)
  * `IgnoreKeyCode` (Impact: 52.1)
    * *Intent:* // Function to return the string representation of the shortcut in virtual key codes appended in a s...
  * `Shortcut::ResetKey` (Impact: 33.2)
  * `Shortcut::SetKeyCodes` (Impact: 21.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 224`, `structural_boundaries: 71`, `args: 58`, `func_start: 28`
* *Risk/State:* `state_mutation: 313`, `duplicate_logic: 4`, `orphaned_logic: 21`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` string, Helpers.h, Shortcut.h, InputInterface.h, sstream, pch.h, shared_constants.h, keyboard_layout.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/AudioSampleGenerator.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.2 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.59 IQR)
- **Top Global Matches:** file_cluster_8: 13.2, file_cluster_4: 13.31, file_cluster_13: 13.502
- **Magnitude:** 695.38 | **LOC:** 749 | **CtrlFlow:** 63.7% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (84.0393%), Tech Debt (32.2173%)
**Top Internal Functions/Classes:**
  * `AudioSampleGenerator::AppendResampledLoo` (Impact: 58.2)
  * `AudioSampleGenerator::OnAudioQuantumStar` (Impact: 50.7)
  * `AudioSampleGenerator::InitializeAsync` (Impact: 46.8)
  * `AudioSampleGenerator::FlushRemainingAudi` (Impact: 22.1)
  * `AudioSampleGenerator::CombineQueuedSampl` (Impact: 16.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 62`, `args: 13`, `func_start: 9`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 442`, `orphaned_logic: 8`
* *Architecture:* `api: 1`, `concurrency: 30`, `import: 5`
* *Defense:* `safety: 2`, `sync_locks: 3`, `immutability_locks: 15`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` LoopbackCapture.h, CaptureFrameWait.h, pch.h, client.h, AudioSampleGenerator.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Helpers/NativeMethods.cs` (CSHARP) | Magnitude: 63.73 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 13, pointers: 9, api: 7
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.cs` (CSHARP) | Magnitude: 82.5 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 144, encapsulation: 36, func_start: 33, immutability_locks: 26
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Dock/DockWindowViewModel.cs` (CSHARP) | Magnitude: 47.68 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 54, state_mutation: 23, encapsulation: 15, api: 14
- `src/modules/powerdisplay/PowerDisplay.Lib/Serialization/ProfileSerializationContext.cs` (CSHARP) | Magnitude: 19.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, decorators: 9, structural_boundaries: 5, doc: 4
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/BackdropStyles.cs` (CSHARP) | Magnitude: 85.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 27, doc: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/modules/MouseWithoutBorders/App/Form/frmScreen.Designer.cs` (CSHARP) | Magnitude: 64.12 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 213, sec_high_risk_execution: 115, state_mutation: 48, events: 30
- `src/modules/MouseWithoutBorders/App/Form/Settings/SettingsFormPage.Designer.cs` (CSHARP) | Magnitude: 19.52 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, sec_high_risk_execution: 21, doc: 11, state_mutation: 9
- `src/modules/MouseUtils/MouseJumpUI/MainForm.Designer.cs` (CSHARP) | Magnitude: 26.54 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, state_mutation: 15, sec_high_risk_execution: 15, doc: 11
- `src/modules/MouseWithoutBorders/App/Form/frmMouseCursor.Designer.cs` (CSHARP) | Magnitude: 26.52 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 17, sec_high_risk_execution: 13, doc: 11
- `src/modules/MouseWithoutBorders/App/Form/frmLogon.Designer.cs` (CSHARP) | Magnitude: 26.38 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, sec_high_risk_execution: 21, state_mutation: 16, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tools/project_template/ModuleTemplate/dllmain.cpp` (CPP) | Magnitude: 0.06 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 17, state_mutation: 17, branch: 9
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/CommandItem.cs` (CSHARP) | Magnitude: 95.96 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, state_mutation: 57, structural_boundaries: 21, branch: 17
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListItemViewModel.cs` (CSHARP) | Magnitude: 260.58 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 220, state_mutation: 77, safety: 59, func_start: 54
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/ListPage.cs` (CSHARP) | Magnitude: 38.84 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 19, args: 12, api: 11
- `src/modules/cmdpal/Microsoft.Terminal.UI/til_string.h` (CPP) | Magnitude: 618.76 | Delta: **0.168 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 386, indent_spaces: 379, structural_boundaries: 115, branch: 92

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/modules/CropAndLock/CropAndLock/resource.h` (CPP) | Magnitude: 15.24 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, macros: 10, reflection_metaprogramming: 8
- `src/modules/poweraccent/PowerAccentModuleInterface/resource.h` (CPP) | Magnitude: 15.24 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, macros: 10, reflection_metaprogramming: 8
- `src/modules/powerrename/testapp/resource.h` (CPP) | Magnitude: 15.3 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, macros: 13, reflection_metaprogramming: 11
- `src/runner/resource.base.h` (CPP) | Magnitude: 15.22 | Delta: **0.181 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, reflection_metaprogramming: 11, macros: 11
- `src/modules/previewpane/powerpreview/resource.base.h` (CPP) | Magnitude: 14.16 | Delta: **0.202 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 20, reflection_metaprogramming: 8, macros: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/common/UITestAutomation/EnvironmentConfig.cs` (CSHARP) | Magnitude: 68.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 16, doc: 15, structural_boundaries: 10, args: 6
- `src/dsc/v3/PowerToys.DSC/Models/FunctionData/ISettingsFunctionData.cs` (CSHARP) | Magnitude: 39.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 27, api: 8, indent_spaces: 7, args: 5
- `src/modules/MouseWithoutBorders/App/Core/Logger.cs` (CSHARP) | Magnitude: 330.36 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 380, state_mutation: 90, branch: 61, func_start: 36
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/WinGetExtensionCommandsProvider.cs` (CSHARP) | Magnitude: 21.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, state_mutation: 7, api: 5
- `src/modules/cmdpal/ext/SamplePagesExtension/Pages/SampleCommentsPage.cs` (CSHARP) | Magnitude: 59.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 21, structural_boundaries: 20, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/common/UITestAutomation/Element/By.cs` (CSHARP) | Magnitude: 55.32 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 47, indent_spaces: 41, structural_boundaries: 16, func_start: 15
- `src/modules/cmdpal/Microsoft.CmdPal.Common/Helpers/InterlockedBoolean.cs` (CSHARP) | Magnitude: 43.12 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 16, state_mutation: 15, doc: 14, structural_boundaries: 8
- `src/modules/cmdpal/doc/initial-sdk-spec/generate-interface.ps1` (POWERSHELL) | Magnitude: 63.64 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 41, closures: 12, regex_execution: 12
- `.github/skills/release-note-generation/scripts/diff_prs.ps1` (POWERSHELL) | Magnitude: 55.7 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: branch: 38, state_mutation: 35, indent_spaces: 28, closures: 19
- `.github/skills/winmd-api-search/scripts/Update-WinMdCache.ps1` (POWERSHELL) | Magnitude: 155.68 | Delta: **0.077 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 112, state_mutation: 102, branch: 52, closures: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/IAppCache.cs` (CSHARP) | Magnitude: 24.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 5, indent_spaces: 4, import: 3
- `src/common/UITestAutomation/Element/ComboBox.cs` (CSHARP) | Magnitude: 13.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, doc: 11, func_start: 7, api: 4
- `src/modules/Workspaces/WorkspacesEditorUITest/WorkspacesEditingPageTests.cs` (CSHARP) | Magnitude: 103.2 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 57, func_start: 47, generics: 40
- `src/modules/cmdpal/Microsoft.CmdPal.Common/Services/IExtensionService.cs` (CSHARP) | Magnitude: 37.22 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, args: 6, func_start: 6, doc: 6
- `src/modules/launcher/Plugins/Microsoft.Plugin.Program/ProgramPluginSettings.cs` (CSHARP) | Magnitude: 37.4 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, api: 12, state_mutation: 10, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/settings-ui/Settings.UI/ViewModels/ProfileEditorViewModel.cs` (CSHARP) | Magnitude: 71.68 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 29, structural_boundaries: 25, args: 15
- `src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/Win32Program.cs` (CSHARP) | Magnitude: 594.72 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 693, structural_boundaries: 173, state_mutation: 166, branch: 125
- `src/modules/cmdpal/Tests/Microsoft.CommandPalette.Extensions.Toolkit.UnitTests/ListHelpersInPlaceUpdateTests.cs` (CSHARP) | Magnitude: 181.9 | Delta: **0.083 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 360, func_start: 147, structural_boundaries: 144, test: 60
- `src/common/Common.Search/FuzzSearch/StringMatcher.cs` (CSHARP) | Magnitude: 173.62 | Delta: **0.105 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 181, state_mutation: 59, structural_boundaries: 38, branch: 35
- `src/modules/EnvironmentVariables/EnvironmentVariablesUILib/ViewModels/MainViewModel.cs` (CSHARP) | Magnitude: 291.0 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 329, state_mutation: 93, structural_boundaries: 71, func_start: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/CommandPalettePreview.xaml.cs` (CSHARP) | Magnitude: 103.66 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 41, args: 33, state_mutation: 32
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/OOBEPageControl.xaml.cs` (CSHARP) | Magnitude: 21.76 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, api: 12, structural_boundaries: 11, ui_framework: 10
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.Properties.cs` (CSHARP) | Magnitude: 73.48 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, doc: 72, structural_boundaries: 30, args: 29
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockContentControl.xaml.cs` (CSHARP) | Magnitude: 41.36 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 22, api: 20, args: 19
- `src/modules/colorPicker/ColorPickerUI/Helpers/ControlHelper.cs` (CSHARP) | Magnitude: 97.3 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 158, doc: 72, func_start: 47, args: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/modules/peek/Peek.FilePreviewer/Previewers/MediaPreviewer/AudioPreviewer.cs` (CSHARP) | Magnitude: 133.7 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 55, concurrency: 44, func_start: 37
- `src/modules/Workspaces/WorkspacesEditor/Models/Project.cs` (CSHARP) | Magnitude: 269.12 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 331, state_mutation: 137, structural_boundaries: 56, branch: 36
- `src/modules/fancyzones/FancyZonesLib/ZonesOverlay.h` (CPP) | Magnitude: 44.22 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, concurrency: 18, import: 11, structural_boundaries: 10
- `src/common/UnitTests-CommonUtils/LoggerHelper.Tests.cpp` (CPP) | Magnitude: 138.36 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 125, state_mutation: 60, args: 37, sec_high_risk_execution: 18
- `src/modules/powerdisplay/PowerDisplay.Lib/Utils/SimpleDebouncer.cs` (CSHARP) | Magnitude: 81.82 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 79, concurrency: 18, state_mutation: 16, doc: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Registry/Constants/MaxTextLength.cs` (CSHARP) | Magnitude: 20.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 7, api: 5, immutability_locks: 4
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/WindowPosition.cs` (CSHARP) | Magnitude: 12.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, structural_boundaries: 12, indent_spaces: 12, api: 10
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Helpers/CommandKind.cs` (CSHARP) | Magnitude: 17.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 36, indent_spaces: 11, structural_boundaries: 2, class_start: 1
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Services/IExtensionTemplateService.cs` (CSHARP) | Magnitude: 17.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 2, args: 1, func_start: 1
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Messages/ErrorOccurredMessage.cs` (CSHARP) | Magnitude: 16.18 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 4, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/modules/MeasureTool/MeasureToolUI/MeasureToolXAML/MainWindow.xaml.cs` (CSHARP) | Magnitude: 93.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 167, func_start: 45, structural_boundaries: 36, args: 27
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/Setting`1.cs` (CSHARP) | Magnitude: 49.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 36, state_mutation: 22, api: 14, structural_boundaries: 9
- `src/modules/launcher/Wox.Plugin/PluginLoadContext.cs` (CSHARP) | Magnitude: 19.24 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 14, import: 6, func_start: 5
- `src/settings-ui/Settings.UI/SettingsXAML/Views/PowerOcrPage.xaml.cs` (CSHARP) | Magnitude: 15.12 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, func_start: 8, args: 5
- `src/modules/ShortcutGuide/ShortcutGuide/d2d_text.h` (CPP) | Magnitude: 22.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, args: 3, structural_boundaries: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/modules/cmdpal/Microsoft.Terminal.UI/ResourceString.cpp` (CPP) | Magnitude: 10.52 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: dead_code: 4, import: 1
- `src/modules/cmdpal/Microsoft.Terminal.UI/ResourceString.h` (CPP) | Magnitude: 10.52 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 6
- `src/modules/awake/Awake/Core/Constants.cs` (CSHARP) | Magnitude: 21.24 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 8, api: 6, encapsulation: 6, immutability_locks: 5

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/modules/cmdpal/Microsoft.CmdPal.UI/MainWindow.xaml.cs` -> Churn: **100.0%** | Cog Load: 31.9128% | Debt: 99.7745%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs` -> Churn: **97.38%** | Cog Load: 72.6454% | Debt: 49.3132%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Pages/ShellPage.xaml.cs` -> Churn: **94.49%** | Cog Load: 14.3005% | Debt: 72.8069%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs` -> Churn: **83.79%** | Cog Load: 55.4749% | Debt: 47.8084%
- `src/settings-ui/Settings.UI/ViewModels/DashboardViewModel.cs` -> Churn: **83.7%** | Cog Load: 12.0571% | Debt: 53.7668%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` -> **Alex Mihaiuc** (100.0% isolated ownership) | Magnitude: 14782.14
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` -> **Niels Laute** (100.0% isolated ownership) | Magnitude: 1431.0
- `src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/MainWindow.xaml.cpp` -> **moooyo** (100.0% isolated ownership) | Magnitude: 1085.54
- `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp` -> **Zach Teutsch** (100.0% isolated ownership) | Magnitude: 923.48
- `src/modules/powerrename/lib/WICMetadataExtractor.cpp` -> **moooyo** (100.0% isolated ownership) | Magnitude: 870.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/modules/keyboardmanager/common/Input.h` -> **Severity: 1340.327** (Blast Radius: 15.848 * Doc Risk: 84.5739%)
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions/Microsoft.CommandPalette.Extensions.def` -> **Severity: 531.701** (Blast Radius: 29.126 * Doc Risk: 18.2552%)
- `src/modules/powerrename/PowerRenameUILib/Utils.h` -> **Severity: 344.185** (Blast Radius: 8.453 * Doc Risk: 40.7175%)
- `src/modules/powerrename/lib/PowerRenameInterfaces.h` -> **Severity: 194.324** (Blast Radius: 2.375 * Doc Risk: 81.8207%)
- `src/common/interop/PowerToys.Interop.def` -> **Severity: 150.496** (Blast Radius: 8.244 * Doc Risk: 18.2552%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
