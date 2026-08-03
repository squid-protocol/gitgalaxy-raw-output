# ARCHITECTURAL_BRIEF: PowerToys
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/PowerToys` |
| **Timestamp** | `2026-08-03T19:23:37.492255+00:00` |
| **Scan Duration** | `17.65s` |
| **Git Branch** | `main` |
| **Git Commit** | `4ce451edd0a66ba4fe1366ff6a912c30be59feb3` |
| **Git Remote** | `https://github.com/microsoft/PowerToys.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 4728 malicious artifacts.

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
> **Architectural Drift Z-Score:** `5.267`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2827 | 54.4% |
| file_cluster_13 | 1676 | 32.3% |
| file_cluster_0 | 222 | 4.3% |
| file_cluster_4 | 103 | 2.0% |
| file_cluster_12 | 74 | 1.4% |
| file_cluster_16 | 58 | 1.1% |
| file_cluster_7 | 27 | 0.5% |
| file_cluster_15 | 22 | 0.4% |
| file_cluster_1 | 9 | 0.2% |
| file_cluster_11 | 8 | 0.2% |
| file_cluster_17 | 8 | 0.2% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 23.3 | 8.9 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 35.8 | 40.6 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 17.6 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.3 | 4.4 | 4.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 53.6 | 73.6 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 83.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 10.8 | 1.8 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 63.4 | 80.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 50.6 | 53.2 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
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

- `FetchItems` (@ `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs`) -> Impact: **2243.1** | LOC: 723
- `OptionsTabProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **2224.6** | LOC: 1604
- `VideoRecordingSession::ShowTrimDialogInt` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **2052.1** | LOC: 1433
- `LoadGifFrames` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **1990.0** | LOC: 1245
- `FancyZones::OnKeyDown` (@ `src/modules/fancyzones/FancyZonesLib/FancyZones.cpp`) -> Impact: **1809.6** | LOC: 547
- `RunPanoramaStitchSelfTest` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **1626.1** | LOC: 1241
- `BuildFixedOverlayMask` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> Impact: **1623.1** | LOC: 542
- `UninstallPackageIdentityMSIXCA` (@ `installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp`) -> Impact: **1218.2** | LOC: 842
- `TryGetMonitors` (@ `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Helpers/FancyZonesDataService.cs`) -> Impact: **1187.9** | LOC: 480
- `WndProc` (@ `src/modules/MouseWithoutBorders/App/Helper/FormHelper.cs`) -> Impact: **1122.5** | LOC: 225

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `GetStringRepresentation` (@ `src/common/ManagedCommon/ColorFormatHelper.cs`) -> **O(2^N) [Recursive]**
- `Start` (@ `src/common/ManagedTelemetry/Telemetry/EtwTrace.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Starts the trace session. /// </summary>
- `FindAll` (@ `src/common/UITestAutomation/Element/Element.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Finds all elements by the selector. /// </summary> /// <typeparam name="T">The class type of the elements to find.</typeparam> /// <...
- `FindAll` (@ `src/common/UITestAutomation/Session.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Finds all Element or its derived class by selector. /// </summary> /// <typeparam name="T">The class of the elements, should be Elem...
- `KillPowerToysProcesses` (@ `src/common/UITestAutomation/SessionHelper.cs`) -> **O(2^N) [Recursive]**
- `ConfigureGlobalModuleSettings` (@ `src/common/UITestAutomation/SettingsConfigHelper.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Configures global PowerToys settings to enable only specified modules and disable all others. /// </summary> /// <param name="module...
- `TestCleanup` (@ `src/common/UITestAutomation/UITestBase.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Cleanups the test. /// </summary>
- `AreEqual` (@ `src/common/UITestAutomation/VisualAssert.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Asserts current visual state of the element is equal with base line image. /// To use this VisualAssert, you need to set Window Them...
- `ExecutePasteFormatAsync` (@ `src/modules/AdvancedPaste/AdvancedPaste/ViewModels/OptionsViewModel.cs`) -> **O(2^N) [Recursive]**
- `TestCaseClipboardHistoryDisableTest` (@ `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* // [x] Open Settings and Disable clipboard history.Open Advanced Paste window with hotkey and observe that Clipboard history button is disabled.

### Highest Data Gravity (Database Complexity)
- `LoadGifFrames` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> DB Complexity: **1022**
- `RunPanoramaStitchSelfTest` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> DB Complexity: **546**
- `OptionsTabProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> DB Complexity: **474**
- `VideoRecordingSession::ShowTrimDialogInt` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> DB Complexity: **386**
- `TEST_CLASS` (@ `src/modules/fancyzones/FancyZonesTests/UnitTests/Util.Spec.cpp`) -> DB Complexity: **266**
- `BuildFixedOverlayMask` (@ `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp`) -> DB Complexity: **254**
- `TEST_CLASS` (@ `src/modules/powerrename/unittests/CommonRegExTests.h`) -> DB Complexity: **227**
- `TEST_CLASS` (@ `src/modules/fancyzones/FancyZonesTests/UnitTests/AppliedLayoutsTests.Spec.cpp`) -> DB Complexity: **198**
- `TEST_CLASS` (@ `src/modules/fancyzones/FancyZonesTests/UnitTests/WorkAreaIdTests.Spec.cpp`) -> DB Complexity: **195**
- `UninstallPackageIdentityMSIXCA` (@ `installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp`) -> DB Complexity: **191**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/modules/ZoomIt/ZoomIt` | 29 | 43281.38 | 42.95% | 19.76% |
| `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels` | 94 | 12387.06 | 31.09% | 36.62% |
| `src/settings-ui/Settings.UI/ViewModels` | 41 | 12385.82 | 31.99% | 21.35% |
| `src/modules/fancyzones/FancyZonesLib` | 70 | 12211.88 | 46.18% | 38.07% |
| `src/modules/MouseWithoutBorders/App/Core` | 29 | 11867.9 | 36.27% | 26.53% |
| `src/settings-ui/Settings.UI.Library` | 153 | 10020.9 | 17.67% | 63.53% |
| `src/modules/keyboardmanager/KeyboardManagerEditorLibrary` | 40 | 7486.06 | 36.31% | 28.88% |
| `src/modules/powerrename/lib` | 40 | 7192.5 | 36.73% | 37.87% |
| `src/modules/MouseWithoutBorders/App/Class` | 16 | 6835.9 | 34.16% | 30.59% |
| `src/common/utils` | 34 | 6383.12 | 52.03% | 21.89% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/common/Common.Search/FuzzSearch/MatchResult.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/By.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/AdvancedPaste.FuzzTests/Logger.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/AdvancedPaste.UnitTests/Mocks/NoOpKernelQueryCacheService.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/AdvancedPaste/Helpers/AIServiceFormatEvent.cs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/skills/release-note-generation/scripts/apply-labels.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/collect-or-apply-milestones.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/diff_prs.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/dump-prs-since-commit.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/find-commit-by-title.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/common/interop/Constants.cpp` -> **73** Orphaned Functions | **0** Duplicates
- `src/common/GPOWrapper/GPOWrapper.cpp` -> **70** Orphaned Functions | **2** Duplicates
- `src/modules/keyboardmanager/KeyboardManagerEditorUI/Controls/UnifiedMappingControl.xaml.cs` -> **48** Orphaned Functions | **2** Duplicates
- `src/modules/powerdisplay/PowerDisplay.Lib.UnitTests/MccsCapabilitiesParserTests.cs` -> **46** Orphaned Functions | **0** Duplicates
- `src/common/SettingsAPI/settings_objects.cpp` -> **20** Orphaned Functions | **21** Duplicates

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
31. **`src/modules/PowerOCR/PowerOCR/OCROverlay.xaml.cs`** -> AI Confidence: **99.35%**
32. **`src/modules/fancyzones/editor/FancyZonesEditor/LayoutPreview.xaml.cs`** -> AI Confidence: **99.34%**
33. **`src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp`** -> AI Confidence: **99.34%**
34. **`src/modules/powerrename/lib/WICMetadataExtractor.cpp`** -> AI Confidence: **99.34%**
35. **`src/runner/auto_start_helper.cpp`** -> AI Confidence: **99.34%**
36. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPageResultFactory.cs`** -> AI Confidence: **99.32%**
37. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.cs`** -> AI Confidence: **99.32%**
38. **`src/modules/NewPlus/NewShellExtensionContextMenu/Helpers.cpp`** -> AI Confidence: **99.32%**
39. **`src/modules/ZoomIt/ZoomItBreak/BreakTimer.cpp`** -> AI Confidence: **99.32%**
40. **`src/modules/powerrename/lib/Enumerating.cpp`** -> AI Confidence: **99.32%**
41. **`src/common/FilePreviewCommon/HTMLParsingExtension.cs`** -> AI Confidence: **99.31%**
42. **`src/common/ManagedCommon/Logger.cs`** -> AI Confidence: **99.31%**
43. **`src/common/UITestAutomation/ScreenRecording.cs`** -> AI Confidence: **99.31%**
44. **`src/common/UITestAutomation/Session.cs`** -> AI Confidence: **99.31%**
45. **`src/common/UITestAutomation/SessionHelper.cs`** -> AI Confidence: **99.31%**
46. **`src/common/UITestAutomation/SettingsConfigHelper.cs`** -> AI Confidence: **99.31%**
47. **`src/common/UITestAutomation/UITestBase.cs`** -> AI Confidence: **99.31%**
48. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/Pages/MainPage.xaml.cs`** -> AI Confidence: **99.31%**
49. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/UserSettings.cs`** -> AI Confidence: **99.31%**
50. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActions/SemanticKernelPasteProvider.cs`** -> AI Confidence: **99.31%**
51. **`src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs`** -> AI Confidence: **99.31%**
52. **`src/modules/FileLocksmith/FileLocksmithUI/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.31%**
53. **`src/modules/MouseUtils/MouseUtils.UITests/FindMyMouseTests.cs`** -> AI Confidence: **99.31%**
54. **`src/modules/MouseUtils/MouseUtils.UITests/MouseHighlighterTests.cs`** -> AI Confidence: **99.31%**
55. **`src/modules/MouseWithoutBorders/App/Class/IClipboardHelper.cs`** -> AI Confidence: **99.31%**
56. **`src/modules/MouseWithoutBorders/App/Class/TcpServer.cs`** -> AI Confidence: **99.31%**
57. **`src/modules/MouseWithoutBorders/App/Core/Clipboard.cs`** -> AI Confidence: **99.31%**
58. **`src/modules/MouseWithoutBorders/App/Core/DragDrop.cs`** -> AI Confidence: **99.31%**
59. **`src/modules/MouseWithoutBorders/App/Core/Event.cs`** -> AI Confidence: **99.31%**
60. **`src/modules/MouseWithoutBorders/App/Core/InitAndCleanup.cs`** -> AI Confidence: **99.31%**
61. **`src/modules/MouseWithoutBorders/App/Core/Launch.cs`** -> AI Confidence: **99.31%**
62. **`src/modules/MouseWithoutBorders/App/Core/Logger.cs`** -> AI Confidence: **99.31%**
63. **`src/modules/MouseWithoutBorders/App/Core/Service.cs`** -> AI Confidence: **99.31%**
64. **`src/modules/MouseWithoutBorders/App/Core/WinAPI.cs`** -> AI Confidence: **99.31%**
65. **`src/modules/MouseWithoutBorders/App/Form/Settings/SetupPage3a.cs`** -> AI Confidence: **99.31%**
66. **`src/modules/MouseWithoutBorders/App/Service/Worker.cs`** -> AI Confidence: **99.31%**
67. **`src/modules/PowerOCR/PowerOCR/App.xaml.cs`** -> AI Confidence: **99.31%**
68. **`src/modules/PowerOCR/PowerOCR/Models/ResultTable.cs`** -> AI Confidence: **99.31%**
69. **`src/modules/Workspaces/WorkspacesEditor/Utils/DrawHelper.cs`** -> AI Confidence: **99.31%**
70. **`src/modules/Workspaces/WorkspacesEditor/Utils/WorkspacesEditorIO.cs`** -> AI Confidence: **99.31%**
71. **`src/modules/Workspaces/WorkspacesLauncherUI/App.xaml.cs`** -> AI Confidence: **99.31%**
72. **`src/modules/awake/Awake/Core/Manager.cs`** -> AI Confidence: **99.31%**
73. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandBarViewModel.cs`** -> AI Confidence: **99.31%**
74. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandItemViewModel.cs`** -> AI Confidence: **99.31%**
75. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs`** -> AI Confidence: **99.31%**
76. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ContentPageViewModel.cs`** -> AI Confidence: **99.31%**
77. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ExtensionObjectViewModel.cs`** -> AI Confidence: **99.31%**
78. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs`** -> AI Confidence: **99.31%**
79. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ShellViewModel.cs`** -> AI Confidence: **99.31%**
80. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelViewModel.cs`** -> AI Confidence: **99.31%**
81. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/BlurImageControl.cs`** -> AI Confidence: **99.31%**
82. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/FiltersDropDown.xaml.cs`** -> AI Confidence: **99.31%**
83. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockControl.xaml.cs`** -> AI Confidence: **99.31%**
84. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockWindow.xaml.cs`** -> AI Confidence: **99.31%**
85. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ContentPage.xaml.cs`** -> AI Confidence: **99.31%**
86. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/Controls/PlainTextContentViewer.xaml.cs`** -> AI Confidence: **99.31%**
87. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs`** -> AI Confidence: **99.31%**
88. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/GlobalErrorHandler.cs`** -> AI Confidence: **99.31%**
89. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/Icons/IconLoaderService.cs`** -> AI Confidence: **99.31%**
90. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/TrayIconService.cs`** -> AI Confidence: **99.31%**
91. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Pages/ShellPage.xaml.cs`** -> AI Confidence: **99.31%**
92. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/SettingsWindow.xaml.cs`** -> AI Confidence: **99.31%**
93. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.Bookmarks.UnitTests/BookmarkResolverTests.cs`** -> AI Confidence: **99.31%**
94. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AllAppsCommandProvider.cs`** -> AI Confidence: **99.31%**
95. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AppListItem.cs`** -> AI Confidence: **99.31%**
96. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/ReparsePoint.cs`** -> AI Confidence: **99.31%**
97. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/Win32Program.cs`** -> AI Confidence: **99.31%**
98. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Storage/Win32ProgramRepository.cs`** -> AI Confidence: **99.31%**
99. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.ClipboardHistory/Pages/ClipboardListItem.cs`** -> AI Confidence: **99.31%**
100. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/FallbackOpenFileItem.cs`** -> AI Confidence: **99.31%**
101. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/IndexerPage.cs`** -> AI Confidence: **99.31%**
102. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Helpers/FancyZonesDataService.cs`** -> AI Confidence: **99.31%**
103. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Program.cs`** -> AI Confidence: **99.31%**
104. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Helpers/RegistryHelper.cs`** -> AI Confidence: **99.31%**
105. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.System/Helpers/NetworkConnectionProperties.cs`** -> AI Confidence: **99.31%**
106. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/Pages/InstallPackageCommand.cs`** -> AI Confidence: **99.31%**
107. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/Pages/InstallPackageListItem.cs`** -> AI Confidence: **99.31%**
108. **`src/modules/colorPicker/ColorPickerUI/App.xaml.cs`** -> AI Confidence: **99.31%**
109. **`src/modules/fancyzones/FancyZonesCLI/CommandLine/Commands/FancyZonesBaseCommand.cs`** -> AI Confidence: **99.31%**
110. **`src/modules/fancyzones/FancyZonesCLI/CommandLine/Commands/SetLayoutCommand.cs`** -> AI Confidence: **99.31%**
111. **`src/modules/fancyzones/FancyZonesEditor.UITests/DefaultLayoutsTest.cs`** -> AI Confidence: **99.31%**
112. **`src/modules/fancyzones/editor/FancyZonesEditor/CanvasZone.xaml.cs`** -> AI Confidence: **99.31%**
113. **`src/modules/fancyzones/editor/FancyZonesEditor/GridEditor.xaml.cs`** -> AI Confidence: **99.31%**
114. **`src/modules/fancyzones/editor/FancyZonesEditor/GridZone.xaml.cs`** -> AI Confidence: **99.31%**
115. **`src/modules/fancyzones/editor/FancyZonesEditor/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
116. **`src/modules/fancyzones/editor/FancyZonesEditor/Utils/FancyZonesEditorIO.cs`** -> AI Confidence: **99.31%**
117. **`src/modules/imageresizer/ui/Models/CliOptions.cs`** -> AI Confidence: **99.31%**
118. **`src/modules/imageresizer/ui/ViewModels/InputViewModel.cs`** -> AI Confidence: **99.31%**
119. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Controls/UnifiedMappingControl.xaml.cs`** -> AI Confidence: **99.31%**
120. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/KeyboardHookHelper.cs`** -> AI Confidence: **99.31%**
121. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/RemappingHelper.cs`** -> AI Confidence: **99.31%**
122. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Pages/MainPage.xaml.cs`** -> AI Confidence: **99.31%**
123. **`src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.UnitConverter/InputInterpreter.cs`** -> AI Confidence: **99.31%**
124. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Storage/Win32ProgramRepository.cs`** -> AI Confidence: **99.31%**
125. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Service/Helpers/ServiceHelper.cs`** -> AI Confidence: **99.31%**
126. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.System/Components/NetworkConnectionProperties.cs`** -> AI Confidence: **99.31%**
127. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate.UnitTests/QueryTests.cs`** -> AI Confidence: **99.31%**
128. **`src/modules/launcher/PowerLauncher/Helper/EnvironmentHelper.cs`** -> AI Confidence: **99.31%**
129. **`src/modules/launcher/PowerLauncher/Helper/ThemeManager.cs`** -> AI Confidence: **99.31%**
130. **`src/modules/launcher/PowerLauncher/ViewModel/MainViewModel.cs`** -> AI Confidence: **99.31%**
131. **`src/modules/launcher/Wox.Infrastructure/Exception/ExceptionFormatter.cs`** -> AI Confidence: **99.31%**
132. **`src/modules/launcher/Wox.Infrastructure/Helper.cs`** -> AI Confidence: **99.31%**
133. **`src/modules/launcher/Wox.Infrastructure/Image/ImageLoader.cs`** -> AI Confidence: **99.31%**
134. **`src/modules/launcher/Wox.Infrastructure/Image/WindowsThumbnailProvider.cs`** -> AI Confidence: **99.31%**
135. **`src/modules/launcher/Wox.Plugin/Common/VirtualDesktop/VirtualDesktopHelper.cs`** -> AI Confidence: **99.31%**
136. **`src/modules/launcher/Wox.Plugin/PluginPair.cs`** -> AI Confidence: **99.31%**
137. **`src/modules/peek/Peek.Common/Helpers/PropertyStoreHelper.cs`** -> AI Confidence: **99.31%**
138. **`src/modules/peek/Peek.FilePreviewer/Controls/ShellPreviewHandlerControl.xaml.cs`** -> AI Confidence: **99.31%**
139. **`src/modules/peek/Peek.FilePreviewer/FilePreview.xaml.cs`** -> AI Confidence: **99.31%**
140. **`src/modules/peek/Peek.UI/MainWindowViewModel.cs`** -> AI Confidence: **99.31%**
141. **`src/modules/poweraccent/PowerAccent.Core/PowerAccent.cs`** -> AI Confidence: **99.31%**
142. **`src/modules/poweraccent/PowerAccent.Core/Services/SettingsService.cs`** -> AI Confidence: **99.31%**
143. **`src/modules/powerdisplay/PowerDisplay.Lib/Drivers/DDC/MonitorDiscoveryHelper.cs`** -> AI Confidence: **99.31%**
144. **`src/modules/powerdisplay/PowerDisplay/Helpers/DisplayChangeWatcher.cs`** -> AI Confidence: **99.31%**
145. **`src/modules/powerdisplay/PowerDisplay/Helpers/TrayIconService.cs`** -> AI Confidence: **99.31%**
146. **`src/modules/powerdisplay/PowerDisplay/PowerDisplayXAML/App.xaml.cs`** -> AI Confidence: **99.31%**
147. **`src/modules/powerdisplay/PowerDisplay/PowerDisplayXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
148. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MainViewModel.Settings.cs`** -> AI Confidence: **99.31%**
149. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MonitorViewModel.cs`** -> AI Confidence: **99.31%**
150. **`src/modules/previewpane/MarkdownPreviewHandler/MarkdownPreviewHandlerControl.cs`** -> AI Confidence: **99.31%**
151. **`src/modules/previewpane/MonacoPreviewHandler/MonacoPreviewHandlerControl.cs`** -> AI Confidence: **99.31%**
152. **`src/modules/registrypreview/RegistryPreview/RegistryPreviewXAML/App.xaml.cs`** -> AI Confidence: **99.31%**
153. **`src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs`** -> AI Confidence: **99.31%**
154. **`src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.DataPreview.cs`** -> AI Confidence: **99.31%**
155. **`src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.Events.cs`** -> AI Confidence: **99.31%**
156. **`src/settings-ui/QuickAccess.UI/QuickAccessXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.31%**
157. **`src/settings-ui/QuickAccess.UI/Services/QuickAccessCoordinator.cs`** -> AI Confidence: **99.31%**
158. **`src/settings-ui/Settings.UI.Library/HotkeySettings.cs`** -> AI Confidence: **99.31%**
159. **`src/settings-ui/Settings.UI.Library/SettingsUtils.cs`** -> AI Confidence: **99.31%**
160. **`src/settings-ui/Settings.UI/SettingsXAML/App.xaml.cs`** -> AI Confidence: **99.31%**
161. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/ModelPicker/FoundryLocalModelPicker.xaml.cs`** -> AI Confidence: **99.31%**
162. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/Timeline/Timeline.xaml.cs`** -> AI Confidence: **99.31%**
163. **`src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.WASDK.cs`** -> AI Confidence: **99.31%**
164. **`src/settings-ui/Settings.UI/SettingsXAML/Views/AwakePage.xaml.cs`** -> AI Confidence: **99.31%**
165. **`src/settings-ui/Settings.UI/SettingsXAML/Views/CustomVcpMappingEditorDialog.xaml.cs`** -> AI Confidence: **99.31%**
166. **`src/settings-ui/Settings.UI/SettingsXAML/Views/LightSwitchPage.xaml.cs`** -> AI Confidence: **99.31%**
167. **`src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs`** -> AI Confidence: **99.31%**
168. **`src/settings-ui/Settings.UI/ViewModels/LightSwitchViewModel.cs`** -> AI Confidence: **99.31%**
169. **`src/settings-ui/Settings.UI/ViewModels/PowerLauncherViewModel.cs`** -> AI Confidence: **99.31%**
170. **`src/settings-ui/Settings.UI/ViewModels/ShortcutConflictViewModel.cs`** -> AI Confidence: **99.31%**
171. **`src/settings-ui/Settings.UI/ViewModels/ShortcutGuideViewModel.cs`** -> AI Confidence: **99.31%**
172. **`src/settings-ui/UITest-Settings/OOBEUITests.cs`** -> AI Confidence: **99.31%**
173. **`installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp`** -> AI Confidence: **99.31%**
174. **`src/Update/PowerToys.Update.cpp`** -> AI Confidence: **99.31%**
175. **`src/common/Display/DisplayUtils.cpp`** -> AI Confidence: **99.31%**
176. **`src/common/updating/updating.cpp`** -> AI Confidence: **99.31%**
177. **`src/common/utils/UnhandledExceptionHandler.h`** -> AI Confidence: **99.31%**
178. **`src/common/utils/elevation.h`** -> AI Confidence: **99.31%**
179. **`src/common/utils/package.h`** -> AI Confidence: **99.31%**
180. **`src/modules/AdvancedPaste/AdvancedPasteModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
181. **`src/modules/EnvironmentVariables/EnvironmentVariablesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
182. **`src/modules/FileLocksmith/FileLocksmithCLI/CLILogic.cpp`** -> AI Confidence: **99.31%**
183. **`src/modules/FileLocksmith/FileLocksmithExt/ExplorerCommand.cpp`** -> AI Confidence: **99.31%**
184. **`src/modules/Hosts/HostsModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
185. **`src/modules/LightSwitch/LightSwitchModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
186. **`src/modules/LightSwitch/LightSwitchService/LightSwitchSettings.cpp`** -> AI Confidence: **99.31%**
187. **`src/modules/MeasureTool/MeasureToolCore/MeasureToolOverlayUI.cpp`** -> AI Confidence: **99.31%**
188. **`src/modules/MeasureTool/MeasureToolCore/PowerToys.MeasureToolCore.cpp`** -> AI Confidence: **99.31%**
189. **`src/modules/MouseUtils/CursorWrap/dllmain.cpp`** -> AI Confidence: **99.31%**
190. **`src/modules/MouseUtils/FindMyMouse/dllmain.cpp`** -> AI Confidence: **99.31%**
191. **`src/modules/MouseUtils/MouseHighlighter/dllmain.cpp`** -> AI Confidence: **99.31%**
192. **`src/modules/MouseWithoutBorders/ModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
193. **`src/modules/NewPlus/NewShellExtensionContextMenu/template_item.cpp`** -> AI Confidence: **99.31%**
194. **`src/modules/ShortcutGuide/ShortcutGuide/main.cpp`** -> AI Confidence: **99.31%**
195. **`src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp`** -> AI Confidence: **99.31%**
196. **`src/modules/ShortcutGuide/ShortcutGuide/shortcut_guide.cpp`** -> AI Confidence: **99.31%**
197. **`src/modules/Workspaces/WorkspacesLauncher/AppLauncher.cpp`** -> AI Confidence: **99.31%**
198. **`src/modules/Workspaces/WorkspacesLauncher/Launcher.cpp`** -> AI Confidence: **99.31%**
199. **`src/modules/Workspaces/WorkspacesLauncher/LauncherUIHelper.cpp`** -> AI Confidence: **99.31%**
200. **`src/modules/Workspaces/WorkspacesLauncher/WindowArrangerHelper.cpp`** -> AI Confidence: **99.31%**
201. **`src/modules/Workspaces/WorkspacesLauncher/main.cpp`** -> AI Confidence: **99.31%**
202. **`src/modules/Workspaces/WorkspacesLib/AppUtils.cpp`** -> AI Confidence: **99.31%**
203. **`src/modules/Workspaces/WorkspacesLib/PwaHelper.cpp`** -> AI Confidence: **99.31%**
204. **`src/modules/Workspaces/WorkspacesLib/WindowUtils.cpp`** -> AI Confidence: **99.31%**
205. **`src/modules/Workspaces/WorkspacesSnapshotTool/SnapshotUtils.cpp`** -> AI Confidence: **99.31%**
206. **`src/modules/Workspaces/WorkspacesWindowArranger/WindowArranger.cpp`** -> AI Confidence: **99.31%**
207. **`src/modules/Workspaces/WorkspacesWindowArranger/main.cpp`** -> AI Confidence: **99.31%**
208. **`src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`** -> AI Confidence: **99.31%**
209. **`src/modules/ZoomIt/ZoomItBreak/ZoomItBreakScr.cpp`** -> AI Confidence: **99.31%**
210. **`src/modules/alwaysontop/AlwaysOnTop/AlwaysOnTop.cpp`** -> AI Confidence: **99.31%**
211. **`src/modules/alwaysontop/AlwaysOnTop/WindowBorder.cpp`** -> AI Confidence: **99.31%**
212. **`src/modules/alwaysontop/AlwaysOnTop/main.cpp`** -> AI Confidence: **99.31%**
213. **`src/modules/cmdpal/CmdPalModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
214. **`src/modules/fancyzones/FancyZones/main.cpp`** -> AI Confidence: **99.31%**
215. **`src/modules/fancyzones/FancyZonesLib/FancyZones.cpp`** -> AI Confidence: **99.31%**
216. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/AppZoneHistory.cpp`** -> AI Confidence: **99.31%**
217. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/AppliedLayouts.cpp`** -> AI Confidence: **99.31%**
218. **`src/modules/fancyzones/FancyZonesLib/JsonHelpers.cpp`** -> AI Confidence: **99.31%**
219. **`src/modules/fancyzones/FancyZonesLib/Layout.cpp`** -> AI Confidence: **99.31%**
220. **`src/modules/fancyzones/FancyZonesLib/MonitorUtils.cpp`** -> AI Confidence: **99.31%**
221. **`src/modules/fancyzones/FancyZonesLib/Settings.cpp`** -> AI Confidence: **99.31%**
222. **`src/modules/fancyzones/FancyZonesLib/WindowKeyboardSnap.cpp`** -> AI Confidence: **99.31%**
223. **`src/modules/fancyzones/FancyZonesLib/WindowUtils.cpp`** -> AI Confidence: **99.31%**
224. **`src/modules/fancyzones/FancyZonesLib/WorkArea.cpp`** -> AI Confidence: **99.31%**
225. **`src/modules/fancyzones/FancyZonesLib/ZonesOverlay.cpp`** -> AI Confidence: **99.31%**
226. **`src/modules/fancyzones/FancyZonesLib/util.cpp`** -> AI Confidence: **99.31%**
227. **`src/modules/imageresizer/ImageResizerLib/Settings.cpp`** -> AI Confidence: **99.31%**
228. **`src/modules/imageresizer/dll/ContextMenuHandler.cpp`** -> AI Confidence: **99.31%**
229. **`src/modules/keyboardmanager/KeyboardManagerEditor/KeyboardManagerEditor.cpp`** -> AI Confidence: **99.31%**
230. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditKeyboardWindow.cpp`** -> AI Confidence: **99.31%**
231. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditShortcutsWindow.cpp`** -> AI Confidence: **99.31%**
232. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/KeyDropDownControl.cpp`** -> AI Confidence: **99.31%**
233. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/ShortcutControl.cpp`** -> AI Confidence: **99.31%**
234. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/SingleKeyRemapControl.cpp`** -> AI Confidence: **99.31%**
235. **`src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp`** -> AI Confidence: **99.31%**
236. **`src/modules/keyboardmanager/KeyboardManagerEngine/main.cpp`** -> AI Confidence: **99.31%**
237. **`src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardManager.cpp`** -> AI Confidence: **99.31%**
238. **`src/modules/keyboardmanager/common/MappingConfiguration.cpp`** -> AI Confidence: **99.31%**
239. **`src/modules/keyboardmanager/dll/dllmain.cpp`** -> AI Confidence: **99.31%**
240. **`src/modules/peek/peek/dllmain.cpp`** -> AI Confidence: **99.31%**
241. **`src/modules/poweraccent/PowerAccentKeyboardService/KeyboardListener.cpp`** -> AI Confidence: **99.31%**
242. **`src/modules/powerdisplay/PowerDisplayModuleInterface/dllmain.cpp`** -> AI Confidence: **99.31%**
243. **`src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/MainWindow.xaml.cpp`** -> AI Confidence: **99.31%**
244. **`src/modules/powerrename/dll/PowerRenameExt.cpp`** -> AI Confidence: **99.31%**
245. **`src/modules/powerrename/lib/MetadataPatternExtractor.cpp`** -> AI Confidence: **99.31%**
246. **`src/modules/powerrename/lib/PowerRenameManager.cpp`** -> AI Confidence: **99.31%**
247. **`src/modules/powerrename/lib/PowerRenameRegEx.cpp`** -> AI Confidence: **99.31%**
248. **`src/modules/powerrename/lib/Settings.cpp`** -> AI Confidence: **99.31%**
249. **`src/modules/powerrename/unittests/PowerRenameManagerTests.cpp`** -> AI Confidence: **99.31%**
250. **`src/modules/previewpane/BgcodePreviewHandlerCpp/BgcodePreviewHandler.cpp`** -> AI Confidence: **99.31%**
251. **`src/modules/previewpane/BgcodeThumbnailProviderCpp/BgcodeThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
252. **`src/modules/previewpane/GcodePreviewHandlerCpp/GcodePreviewHandler.cpp`** -> AI Confidence: **99.31%**
253. **`src/modules/previewpane/GcodeThumbnailProviderCpp/GcodeThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
254. **`src/modules/previewpane/MarkdownPreviewHandlerCpp/MarkdownPreviewHandler.cpp`** -> AI Confidence: **99.31%**
255. **`src/modules/previewpane/MonacoPreviewHandlerCpp/MonacoPreviewHandler.cpp`** -> AI Confidence: **99.31%**
256. **`src/modules/previewpane/PdfPreviewHandlerCpp/PdfPreviewHandler.cpp`** -> AI Confidence: **99.31%**
257. **`src/modules/previewpane/PdfThumbnailProviderCpp/PdfThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
258. **`src/modules/previewpane/QoiPreviewHandlerCpp/QoiPreviewHandler.cpp`** -> AI Confidence: **99.31%**
259. **`src/modules/previewpane/QoiThumbnailProviderCpp/QoiThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
260. **`src/modules/previewpane/StlThumbnailProviderCpp/StlThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
261. **`src/modules/previewpane/SvgPreviewHandlerCpp/SvgPreviewHandler.cpp`** -> AI Confidence: **99.31%**
262. **`src/modules/previewpane/SvgThumbnailProviderCpp/SvgThumbnailProvider.cpp`** -> AI Confidence: **99.31%**
263. **`src/modules/previewpane/powerpreview/powerpreview.cpp`** -> AI Confidence: **99.31%**
264. **`src/runner/UpdateUtils.cpp`** -> AI Confidence: **99.31%**
265. **`src/runner/general_settings.cpp`** -> AI Confidence: **99.31%**
266. **`src/runner/quick_access_host.cpp`** -> AI Confidence: **99.31%**
267. **`src/runner/settings_window.cpp`** -> AI Confidence: **99.31%**
268. **`src/runner/tray_icon.cpp`** -> AI Confidence: **99.31%**
269. **`tools/BugReportTool/BugReportTool/EventViewer.cpp`** -> AI Confidence: **99.31%**
270. **`tools/MonitorReportTool/MonitorReportTool.cpp`** -> AI Confidence: **99.31%**
271. **`tools/module_loader/src/main.cpp`** -> AI Confidence: **99.31%**
272. **`src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py`** -> AI Confidence: **99.31%**
273. **`.github/skills/release-note-generation/scripts/collect-or-apply-milestones.ps1`** -> AI Confidence: **99.29%**
274. **`.github/skills/release-note-generation/scripts/diff_prs.ps1`** -> AI Confidence: **99.29%**
275. **`.github/skills/release-note-generation/scripts/dump-prs-since-commit.ps1`** -> AI Confidence: **99.29%**
276. **`.github/skills/release-note-generation/scripts/find-commit-by-title.ps1`** -> AI Confidence: **99.29%**
277. **`.github/skills/release-note-generation/scripts/group-prs-by-label.ps1`** -> AI Confidence: **99.29%**
278. **`.github/skills/winmd-api-search/scripts/Update-WinMdCache.ps1`** -> AI Confidence: **99.29%**
279. **`installer/PowerToysSetupVNext/generateMonacoWxs.ps1`** -> AI Confidence: **99.29%**
280. **`src/PackageIdentity/BuildSparsePackage.ps1`** -> AI Confidence: **99.29%**
281. **`src/codeAnalysis/format_sources.ps1`** -> AI Confidence: **99.29%**
282. **`src/modules/cmdpal/check-extensions.ps1`** -> AI Confidence: **99.29%**
283. **`src/modules/cmdpal/doc/initial-sdk-spec/generate-interface.ps1`** -> AI Confidence: **99.29%**
284. **`src/modules/cmdpal/format_sources.ps1`** -> AI Confidence: **99.29%**
285. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/CheckCmdNotFoundRequirements.ps1`** -> AI Confidence: **99.29%**
286. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/DisableModule.ps1`** -> AI Confidence: **99.29%**
287. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/EnableModule.ps1`** -> AI Confidence: **99.29%**
288. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/InstallPowerShell7.ps1`** -> AI Confidence: **99.29%**
289. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/InstallWinGetClientModule.ps1`** -> AI Confidence: **99.29%**
290. **`src/settings-ui/Settings.UI/Assets/Settings/Scripts/UpgradeModule.ps1`** -> AI Confidence: **99.29%**
291. **`tools/CleanUp_tool_powershell_script/CleanUp_tool.ps1`** -> AI Confidence: **99.29%**
292. **`tools/Verification scripts/verify-installation-script.ps1`** -> AI Confidence: **99.29%**
293. **`tools/clear-copilot-context.ps1`** -> AI Confidence: **99.29%**
294. **`src/modules/AdvancedPaste/AdvancedPaste/Models/PasteFormats.cs`** -> AI Confidence: **99.29%**
295. **`src/modules/cmdpal/Microsoft.CmdPal.Common/Services/Sanitizer/NetworkRuleProvider.cs`** -> AI Confidence: **99.29%**
296. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/AdaptiveCardsConfig.cs`** -> AI Confidence: **99.29%**
297. **`src/modules/cmdpal/Microsoft.CmdPal.UI/LocalSuppressions.cs`** -> AI Confidence: **99.29%**
298. **`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/GlobalSuppressions.cs`** -> AI Confidence: **99.29%**
299. **`src/common/utils/resources.h`** -> AI Confidence: **99.29%**
300. **`src/modules/MeasureTool/MeasureToolCore/BGRATextureView.cpp`** -> AI Confidence: **99.29%**
301. **`src/modules/cmdpal/Microsoft.Terminal.UI/init.cpp`** -> AI Confidence: **99.29%**
302. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/Dialog.cpp`** -> AI Confidence: **99.29%**
303. **`src/modules/keyboardmanager/KeyboardManagerEditorLibrary/EditorHelpers.cpp`** -> AI Confidence: **99.29%**
304. **`src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/dllmain.cpp`** -> AI Confidence: **99.29%**
305. **`src/modules/powerrename/lib/Randomizer.cpp`** -> AI Confidence: **99.29%**
306. **`tools/module_loader/src/ConsoleHost.cpp`** -> AI Confidence: **99.29%**
307. **`src/Monaco/customLanguages/gitignore.js`** -> AI Confidence: **99.29%**
308. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActions/FoundryLocalPasteProvider.cs`** -> AI Confidence: **99.24%**
309. **`src/modules/AdvancedPaste/AdvancedPaste/ViewModels/OptionsViewModel.cs`** -> AI Confidence: **99.24%**
310. **`src/modules/Hosts/HostsUILib/Helpers/HostsService.cs`** -> AI Confidence: **99.24%**
311. **`src/modules/LightSwitch/Tests/LightSwitch.UITests/TestHelper.cs`** -> AI Confidence: **99.24%**
312. **`src/modules/MouseUtils/MouseJumpUI/MainForm.cs`** -> AI Confidence: **99.24%**
313. **`src/modules/MouseWithoutBorders/App/Class/MyKnownBitmap.cs`** -> AI Confidence: **99.24%**
314. **`src/modules/Workspaces/WorkspacesCsharpLibrary/Models/BaseApplication.cs`** -> AI Confidence: **99.24%**
315. **`src/modules/Workspaces/WorkspacesEditor/Models/Project.cs`** -> AI Confidence: **99.24%**
316. **`src/modules/Workspaces/WorkspacesEditor/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.24%**
317. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ContentFormViewModel.cs`** -> AI Confidence: **99.24%**
318. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Models/ExtensionService.cs`** -> AI Confidence: **99.24%**
319. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Models/ExtensionWrapper.cs`** -> AI Confidence: **99.24%**
320. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelCommandManager.cs`** -> AI Confidence: **99.24%**
321. **`src/modules/cmdpal/Microsoft.CmdPal.UI/CommandPaletteContextMenuFactory.cs`** -> AI Confidence: **99.24%**
322. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/ShortcutControl/ShortcutControl.xaml.cs`** -> AI Confidence: **99.24%**
323. **`src/modules/cmdpal/Microsoft.CmdPal.UI/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
324. **`src/modules/cmdpal/Microsoft.CmdPal.UI/PowerToysRootPageService.cs`** -> AI Confidence: **99.24%**
325. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.System.UnitTests/ImageTests.cs`** -> AI Confidence: **99.24%**
326. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Commands/UninstallApplicationCommand.cs`** -> AI Confidence: **99.24%**
327. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Pages/BookmarkListItem.cs`** -> AI Confidence: **99.24%**
328. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Calc/Helper/ResultHelper.cs`** -> AI Confidence: **99.24%**
329. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/ActionsListContextItem.cs`** -> AI Confidence: **99.24%**
330. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Helpers/ResultHelper.cs`** -> AI Confidence: **99.24%**
331. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsServices/Helpers/ServiceHelper.cs`** -> AI Confidence: **99.24%**
332. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsTerminal/Pages/ProfilesListPage.cs`** -> AI Confidence: **99.24%**
333. **`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/ThumbnailHelper.cs`** -> AI Confidence: **99.24%**
334. **`src/modules/colorPicker/ColorPickerUI/Helpers/AppStateHandler.cs`** -> AI Confidence: **99.24%**
335. **`src/modules/colorPicker/ColorPickerUI/Helpers/ZoomWindowHelper.cs`** -> AI Confidence: **99.24%**
336. **`src/modules/colorPicker/ColorPickerUI/Settings/UserSettings.cs`** -> AI Confidence: **99.24%**
337. **`src/modules/fancyzones/FancyZones.UITests/DragWindowTests.cs`** -> AI Confidence: **99.24%**
338. **`src/modules/fancyzones/FancyZones.UITests/LayoutApplyHotKeyTests.cs`** -> AI Confidence: **99.24%**
339. **`src/modules/fancyzones/editor/FancyZonesEditor/App.xaml.cs`** -> AI Confidence: **99.24%**
340. **`src/modules/imageresizer/ui/ImageResizerXAML/App.xaml.cs`** -> AI Confidence: **99.24%**
341. **`src/modules/imageresizer/ui/Models/ResizeBatch.cs`** -> AI Confidence: **99.24%**
342. **`src/modules/imageresizer/ui/Models/ResizeOperation.cs`** -> AI Confidence: **99.24%**
343. **`src/modules/imageresizer/ui/Properties/Settings.cs`** -> AI Confidence: **99.24%**
344. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Settings/SettingsManager.cs`** -> AI Confidence: **99.24%**
345. **`src/modules/launcher/Plugins/Microsoft.Plugin.Folder/Sources/QueryInternalDirectory.cs`** -> AI Confidence: **99.24%**
346. **`src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/Win32Program.cs`** -> AI Confidence: **99.24%**
347. **`src/modules/launcher/Plugins/Microsoft.Plugin.Shell/Main.cs`** -> AI Confidence: **99.24%**
348. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Calculator/Main.cs`** -> AI Confidence: **99.24%**
349. **`src/modules/launcher/PowerLauncher/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
350. **`src/modules/launcher/PowerLauncher/SettingsReader.cs`** -> AI Confidence: **99.24%**
351. **`src/modules/launcher/PowerLauncher/ViewModel/ResultsViewModel.cs`** -> AI Confidence: **99.24%**
352. **`src/modules/launcher/Wox.Infrastructure/Storage/JsonStorage`1.cs`** -> AI Confidence: **99.24%**
353. **`src/modules/peek/Peek.FilePreviewer/Controls/BrowserControl.xaml.cs`** -> AI Confidence: **99.24%**
354. **`src/modules/peek/Peek.FilePreviewer/Previewers/Archives/Helpers/IconCache.cs`** -> AI Confidence: **99.24%**
355. **`src/modules/peek/Peek.FilePreviewer/Previewers/WebBrowserPreviewer/Helpers/MonacoHelper.cs`** -> AI Confidence: **99.24%**
356. **`src/modules/peek/Peek.UI/Helpers/FileExplorerHelper.cs`** -> AI Confidence: **99.24%**
357. **`src/modules/peek/Peek.UI/PeekXAML/App.xaml.cs`** -> AI Confidence: **99.24%**
358. **`src/modules/peek/Peek.UI/PeekXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
359. **`src/modules/peek/Peek.UITests/PeekFilePreviewTests.cs`** -> AI Confidence: **99.24%**
360. **`src/modules/powerdisplay/PowerDisplay.Lib/Drivers/DDC/DdcCiController.cs`** -> AI Confidence: **99.24%**
361. **`src/modules/powerdisplay/PowerDisplay/Helpers/MonitorManager.cs`** -> AI Confidence: **99.24%**
362. **`src/modules/powerdisplay/PowerDisplay/Program.cs`** -> AI Confidence: **99.24%**
363. **`src/modules/powerdisplay/PowerDisplay/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.24%**
364. **`src/modules/previewpane/SvgPreviewHandler/SvgPreviewControl.cs`** -> AI Confidence: **99.24%**
365. **`src/modules/registrypreview/RegistryPreview/RegistryPreviewXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.24%**
366. **`src/settings-ui/Settings.UI.Library/Utilities/SetAdditionalSettingsCommandLineCommand.cs`** -> AI Confidence: **99.24%**
367. **`src/settings-ui/Settings.UI/Helpers/NavigablePage.cs`** -> AI Confidence: **99.24%**
368. **`src/settings-ui/Settings.UI/SettingsXAML/Views/ShellPage.xaml.cs`** -> AI Confidence: **99.24%**
369. **`src/settings-ui/Settings.UI/ViewModels/CmdNotFoundViewModel.cs`** -> AI Confidence: **99.24%**
370. **`src/settings-ui/Settings.UI/ViewModels/ColorPickerViewModel.cs`** -> AI Confidence: **99.24%**
371. **`src/settings-ui/Settings.UI/ViewModels/ImageResizerViewModel.cs`** -> AI Confidence: **99.24%**
372. **`src/settings-ui/Settings.UI/ViewModels/KeyboardManagerViewModel.cs`** -> AI Confidence: **99.24%**
373. **`src/settings-ui/Settings.UI/ViewModels/MouseWithoutBordersViewModel.cs`** -> AI Confidence: **99.24%**
374. **`src/settings-ui/Settings.UI/ViewModels/NewPlusViewModel.cs`** -> AI Confidence: **99.24%**
375. **`src/settings-ui/Settings.UI/ViewModels/PageViewModelBase.cs`** -> AI Confidence: **99.24%**
376. **`src/settings-ui/Settings.UI/ViewModels/PeekViewModel.cs`** -> AI Confidence: **99.24%**
377. **`src/settings-ui/Settings.UI/ViewModels/PowerOcrViewModel.cs`** -> AI Confidence: **99.24%**
378. **`src/settings-ui/Settings.UI/ViewModels/PowerRenameViewModel.cs`** -> AI Confidence: **99.24%**
379. **`src/common/notifications/notifications.cpp`** -> AI Confidence: **99.24%**
380. **`src/modules/MeasureTool/MeasureToolCore/OverlayUI.cpp`** -> AI Confidence: **99.24%**
381. **`src/modules/MeasureTool/MeasureToolCore/ScreenCapturing.cpp`** -> AI Confidence: **99.24%**
382. **`src/modules/MouseUtils/FindMyMouse/FindMyMouse.cpp`** -> AI Confidence: **99.24%**
383. **`src/modules/MouseUtils/MouseJump/dllmain.cpp`** -> AI Confidence: **99.24%**
384. **`src/modules/PowerOCR/PowerOCRModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
385. **`src/modules/ShortcutGuide/ShortcutGuideModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
386. **`src/modules/Workspaces/WorkspacesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
387. **`src/modules/Workspaces/WorkspacesSnapshotTool/main.cpp`** -> AI Confidence: **99.24%**
388. **`src/modules/colorPicker/ColorPicker/dllmain.cpp`** -> AI Confidence: **99.24%**
389. **`src/modules/fancyzones/FancyZonesLib/EditorParameters.cpp`** -> AI Confidence: **99.24%**
390. **`src/modules/fancyzones/FancyZonesModuleInterface/dllmain.cpp`** -> AI Confidence: **99.24%**
391. **`src/modules/imageresizer/ImageResizerContextMenu/dllmain.cpp`** -> AI Confidence: **99.24%**
392. **`src/modules/launcher/Microsoft.Launcher/dllmain.cpp`** -> AI Confidence: **99.24%**
393. **`src/modules/powerrename/PowerRenameContextMenu/dllmain.cpp`** -> AI Confidence: **99.24%**
394. **`src/modules/registrypreview/RegistryPreviewExt/dllmain.cpp`** -> AI Confidence: **99.24%**
395. **`tools/BugReportTool/BugReportTool/Main.cpp`** -> AI Confidence: **99.24%**
396. **`tools/FancyZones_DrawLayoutTest/FancyZones_DrawLayoutTest.cpp`** -> AI Confidence: **99.24%**
397. **`tools/StylesReportTool/StylesReportTool.cpp`** -> AI Confidence: **99.24%**
398. **`src/common/ManagedTelemetry/Telemetry/EtwTrace.cs`** -> AI Confidence: **99.23%**
399. **`src/dsc/PowerToys.Settings.DSC.Schema.Generator/DSCGeneration.cs`** -> AI Confidence: **99.23%**
400. **`src/modules/Workspaces/WorkspacesEditor/WorkspacesEditorPage.xaml.cs`** -> AI Confidence: **99.23%**
401. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Services/SettingsService.cs`** -> AI Confidence: **99.23%**
402. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockItemControl.xaml.cs`** -> AI Confidence: **99.23%**
403. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/TextBoxCaretColor.cs`** -> AI Confidence: **99.23%**
404. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Commands/UninstallApplicationConfirmation.cs`** -> AI Confidence: **99.23%**
405. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/DirectoryExplorePage.cs`** -> AI Confidence: **99.23%**
406. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PerformanceMonitor/DevHome/Helpers/MemoryStats.cs`** -> AI Confidence: **99.23%**
407. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/ValidationHelper.cs`** -> AI Confidence: **99.23%**
408. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Interop/KeyboardMappingService.cs`** -> AI Confidence: **99.23%**
409. **`src/modules/launcher/Plugins/Microsoft.Plugin.Folder.UnitTests/InternalQueryFolderTests.cs`** -> AI Confidence: **99.23%**
410. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.History/Main.cs`** -> AI Confidence: **99.23%**
411. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Registry/Helper/RegistryHelper.cs`** -> AI Confidence: **99.23%**
412. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate/Components/ResultHelper.cs`** -> AI Confidence: **99.23%**
413. **`src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate/Components/SearchController.cs`** -> AI Confidence: **99.23%**
414. **`src/modules/launcher/PowerLauncher/Plugin/PluginConfig.cs`** -> AI Confidence: **99.23%**
415. **`src/modules/peek/Peek.FilePreviewer/Previewers/Helpers/ThumbnailHelper.cs`** -> AI Confidence: **99.23%**
416. **`src/modules/peek/Peek.FilePreviewer/Previewers/PreviewerFactory.cs`** -> AI Confidence: **99.23%**
417. **`src/modules/registrypreview/RegistryPreview.FuzzTests/FuzzTests.cs`** -> AI Confidence: **99.23%**
418. **`src/settings-ui/QuickAccess.UI/Services/QuickAccessLauncher.cs`** -> AI Confidence: **99.23%**
419. **`src/settings-ui/Settings.UI.Library/SettingsFactory.cs`** -> AI Confidence: **99.23%**
420. **`src/settings-ui/Settings.UI.XamlIndexBuilder/Program.cs`** -> AI Confidence: **99.23%**
421. **`src/settings-ui/Settings.UI/ViewModels/FancyZonesViewModel.cs`** -> AI Confidence: **99.23%**
422. **`src/modules/MeasureTool/MeasureToolModuleInterface/dllmain.cpp`** -> AI Confidence: **99.23%**
423. **`src/modules/Workspaces/WorkspacesLib/SteamGameHelper.cpp`** -> AI Confidence: **99.23%**
424. **`src/modules/alwaysontop/AlwaysOnTop/Settings.cpp`** -> AI Confidence: **99.23%**
425. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData.cpp`** -> AI Confidence: **99.23%**
426. **`src/modules/fancyzones/FancyZonesLib/FancyZonesData/CustomLayouts.cpp`** -> AI Confidence: **99.23%**
427. **`src/modules/previewpane/powerpreview/dllmain.cpp`** -> AI Confidence: **99.23%**
428. **`src/common/sysinternals/dll.c`** -> AI Confidence: **99.23%**
429. **`src/modules/LightSwitch/LightSwitchService/LightSwitchStateManager.cpp`** -> AI Confidence: **99.22%**
430. **`src/common/Common.UI.Controls/Controls/KeyVisual/KeyVisual.xaml.cs`** -> AI Confidence: **99.2%**
431. **`src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs`** -> AI Confidence: **99.2%**
432. **`src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.VSCodeWorkspaces/WorkspacesHelper/Rfc3986Uri.cs`** -> AI Confidence: **99.2%**
433. **`src/common/SettingsAPI/FileWatcher.cpp`** -> AI Confidence: **99.2%**
434. **`src/modules/Workspaces/WorkspacesLib/trace.cpp`** -> AI Confidence: **99.2%**
435. **`src/modules/ZoomIt/ZoomIt/LoopbackCapture.cpp`** -> AI Confidence: **99.2%**
436. **`src/modules/ZoomIt/ZoomIt/Utility.cpp`** -> AI Confidence: **99.2%**
437. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/Converters/DateTimeToFriendlyStringConverter.cs`** -> AI Confidence: **99.18%**
438. **`src/modules/AdvancedPaste/AdvancedPaste/AdvancedPasteXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.18%**
439. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/DataPackageHelpers.cs`** -> AI Confidence: **99.18%**
440. **`src/modules/AdvancedPaste/AdvancedPaste/Helpers/KernelExtensions.cs`** -> AI Confidence: **99.18%**
441. **`src/modules/AdvancedPaste/AdvancedPaste/Services/CustomActionKernelQueryCacheService.cs`** -> AI Confidence: **99.18%**
442. **`src/modules/EnvironmentVariables/EnvironmentVariables/EnvironmentVariablesXAML/App.xaml.cs`** -> AI Confidence: **99.18%**
443. **`src/modules/Hosts/Hosts/HostsXAML/App.xaml.cs`** -> AI Confidence: **99.18%**
444. **`src/modules/Hosts/HostsUILib/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.18%**
445. **`src/modules/MouseUtils/MouseUtils.UITests/MousePointerCrosshairsTests.cs`** -> AI Confidence: **99.18%**
446. **`src/modules/PowerOCR/PowerOCR/Helpers/OcrExtensions.cs`** -> AI Confidence: **99.18%**
447. **`src/modules/Workspaces/WorkspacesLauncherUI/ViewModels/MainViewModel.cs`** -> AI Confidence: **99.18%**
448. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/NewExtensionFormBase.cs`** -> AI Confidence: **99.18%**
449. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Dock/DockViewModel.cs`** -> AI Confidence: **99.18%**
450. **`src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/SettingsExtensionsViewModel.cs`** -> AI Confidence: **99.18%**
451. **`src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/Controls/ImageContentViewer.xaml.cs`** -> AI Confidence: **99.18%**
452. **`src/modules/cmdpal/Microsoft.CmdPal.UI/Settings/DockSettingsPage.xaml.cs`** -> AI Confidence: **99.18%**
453. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.Ext.System.UnitTests/QueryTests.cs`** -> AI Confidence: **99.18%**
454. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.UI.ViewModels.UnitTests/RecentCommandsTests.cs`** -> AI Confidence: **99.18%**
455. **`src/modules/cmdpal/Tests/Microsoft.CmdPal.UITests/CommandPaletteTestBase.cs`** -> AI Confidence: **99.18%**
456. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AllAppsPage.cs`** -> AI Confidence: **99.18%**
457. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Pages/BookmarkPlaceholderForm.cs`** -> AI Confidence: **99.18%**
458. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.ClipboardHistory/Helpers/Analyzers/WebLinkMetadataProvider.cs`** -> AI Confidence: **99.18%**
459. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/ExploreListItem.cs`** -> AI Confidence: **99.18%**
460. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Modules/KeyboardManagerModuleCommandProvider.cs`** -> AI Confidence: **99.18%**
461. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Modules/WorkspacesModuleCommandProvider.cs`** -> AI Confidence: **99.18%**
462. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.PowerToys/Pages/FancyZonesMonitorsPage.cs`** -> AI Confidence: **99.18%**
463. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Registry/Pages/RegistryListPage.cs`** -> AI Confidence: **99.18%**
464. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.System/Helpers/Commands.cs`** -> AI Confidence: **99.18%**
465. **`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WebSearch/WebSearchTopLevelCommandItem.cs`** -> AI Confidence: **99.18%**
466. **`src/modules/colorPicker/ColorPickerUI/ViewModels/ColorEditorViewModel.cs`** -> AI Confidence: **99.18%**
467. **`src/modules/fancyzones/FancyZones.UITests/Utils/ZoneSwitchHelper.cs`** -> AI Confidence: **99.18%**
468. **`src/modules/imageresizer/tests/Properties/SettingsTests.cs`** -> AI Confidence: **99.18%**
469. **`src/modules/imageresizer/ui/ImageResizerXAML/MainWindow.xaml.cs`** -> AI Confidence: **99.18%**
470. **`src/modules/imageresizer/ui/Models/ResizeSize.cs`** -> AI Confidence: **99.18%**
471. **`src/modules/imageresizer/ui/ViewModels/ProgressViewModel.cs`** -> AI Confidence: **99.18%**
472. **`src/modules/keyboardmanager/KeyboardManagerEditorUI/Helpers/Remapping.cs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/modules/MouseWithoutBorders/App/Form/Settings/SettingsPage4.Designer.cs` -> **100.0%** Exposure
- `src/modules/MouseWithoutBorders/App/Form/frmScreen.Designer.cs` -> **100.0%** Exposure
- `src/modules/powerrename/unittests/CommonRegExTests.h` -> **100.0%** Exposure
- `src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs` -> **99.9997%** Exposure
- `src/modules/launcher/Plugins/Microsoft.Plugin.Uri.UnitTests/UriHelper/ExtendedUriParserTests.cs` -> **99.9578%** Exposure
### Exploit Generation Surface
- `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` -> **100.0%** Exposure
- `src/common/Common.Search/FuzzSearch/StringMatcher.cs` -> **100.0%** Exposure
- `src/common/Common.UI.Controls/Controls/KeyVisual/KeyVisual.xaml.cs` -> **100.0%** Exposure
- `src/common/Common.UI.Controls/Controls/ShortcutWithTextLabelControl/ShortcutWithTextLabelControl.xaml.cs` -> **100.0%** Exposure
- `src/common/Common.UI/SettingsDeepLink.cs` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `.github/skills/winmd-api-search/scripts/Invoke-WinMdQuery.ps1` -> **100.0%** Exposure
- `src/PackageIdentity/BuildSparsePackage.ps1` -> **100.0%** Exposure
- `src/common/UITestAutomation/SessionHelper.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` -> **100.0%** Exposure
- `src/modules/Hosts/HostsUILib/Helpers/HostsService.cs` -> **100.0%** Exposure
### Raw Memory Manipulation
- `src/common/UnitTests-CommonUtils/ColorUtils.Tests.cpp` -> **10.0%** Exposure
- `src/modules/ZoomIt/ZoomIt/ZoomItSettings.h` -> **10.0%** Exposure
- `src/modules/powerrename/unittests/CommonRegExTests.h` -> **10.0%** Exposure
- `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` -> **9.6506%** Exposure
- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` -> **5.0675%** Exposure
### Hardcoded Payload Artifacts
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Services/Sanitizer/SecretKeyValueRulesProviderTests.cs` -> **82.1257%** Exposure
### Algorithmic DoS Exposure
- `.github/skills/release-note-generation/scripts/group-prs-by-label.ps1` -> **100.0%** Exposure
- `.github/skills/winmd-api-search/scripts/Invoke-WinMdQuery.ps1` -> **100.0%** Exposure
- `.github/skills/winmd-api-search/scripts/Update-WinMdCache.ps1` -> **100.0%** Exposure
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/Capture-MonitorLayout.ps1` -> **100.0%** Exposure
- `src/modules/awake/scripts/Build-Awake.ps1` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `111` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `19571` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Indexer/Pages/IndexerPage.cs` (CSHARP) -> Cumulative Risk: **1054.09**
- **Archetype:** `file_cluster_13` (Distance: 12.391 IQR)
- **Magnitude:** 331.84 | **LOC:** 285 | **CtrlFlow:** 47.6% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `LoadMore` (Impact: 52.2), `Dispose` (Impact: 41.0), `FullSearchString` (Impact: 39.8)

### 2. `src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Service/Main.cs` (CSHARP) -> Cumulative Risk: **1033.93**
- **Archetype:** `file_cluster_4` (Distance: 12.202 IQR)
- **Magnitude:** 187.04 | **LOC:** 153 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `LoadContextMenus` (Impact: 43.2), `Query` (Impact: 27.1), `UpdateIconPath` (Impact: 17.3)

### 3. `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/AppListItem.cs` (CSHARP) -> Cumulative Risk: **992.73**
- **Archetype:** `file_cluster_4` (Distance: 13.195 IQR)
- **Magnitude:** 546.96 | **LOC:** 269 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `BuildDetails` (Impact: 104.1), `TryLoadThumbnail` (Impact: 49.1), `FetchIcon` (Impact: 44.2)

### 4. `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowWalker/Pages/WindowWalkerListPage.cs` (CSHARP) -> Cumulative Risk: **987.06**
- **Archetype:** `file_cluster_13` (Distance: 10.63 IQR)
- **Magnitude:** 146.38 | **LOC:** 136 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 45.3), `Query` (Impact: 24.0), `Receive` (Impact: 23.4)

### 5. `src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/Icons/CachedIconSourceProvider.cs` (CSHARP) -> Cumulative Risk: **987.04**
- **Archetype:** `file_cluster_4` (Distance: 12.353 IQR)
- **Magnitude:** 148.94 | **LOC:** 104 | **CtrlFlow:** 40.6% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `GetOrCreateSlowPath` (Impact: 36.8), `IconCacheKey` (Impact: 13.4), `GetIconSource` (Impact: 10.8)

### 6. `src/modules/peek/Peek.FilePreviewer/Previewers/WebBrowserPreviewer/WebBrowserPreviewer.cs` (CSHARP) -> Cumulative Risk: **985.11**
- **Archetype:** `file_cluster_4` (Distance: 11.471 IQR)
- **Magnitude:** 252.8 | **LOC:** 177 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `LoadDisplayInfoAsync` (Impact: 72.8), `Dispose` (Impact: 13.6), `LoadPreviewAsync` (Impact: 12.8)

### 7. `src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.ValueGenerator/Main.cs` (CSHARP) -> Cumulative Risk: **977.88**
- **Archetype:** `file_cluster_13` (Distance: 11.875 IQR)
- **Magnitude:** 387.68 | **LOC:** 242 | **CtrlFlow:** 33.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `Query` (Impact: 136.1), `Dispose` (Impact: 35.0), `GetIcoPath` (Impact: 28.9)

### 8. `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelCommandManager.cs` (CSHARP) -> Cumulative Risk: **976.43**
- **Archetype:** `file_cluster_4` (Distance: 12.765 IQR)
- **Magnitude:** 684.08 | **LOC:** 870 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `AppendCommandsWhenReadyAsync` (Impact: 158.8), `TryLoadCommandsAsync` (Impact: 77.6), `ExtensionService_OnExtensionRemoved` (Impact: 63.0)

### 9. `src/modules/cmdpal/Microsoft.CmdPal.Common/Helpers/ThrottledDebouncedAction.cs` (CSHARP) -> Cumulative Risk: **976.22**
- **Archetype:** `file_cluster_4` (Distance: 12.3 IQR)
- **Magnitude:** 296.32 | **LOC:** 164 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Invoke` (Impact: 138.2), `Cancel` (Impact: 32.7), `Invoke` (Impact: 4.0)

### 10. `src/modules/launcher/Plugins/Community.PowerToys.Run.Plugin.UnitConverter/Main.cs` (CSHARP) -> Cumulative Risk: **974.87**
- **Archetype:** `file_cluster_13` (Distance: 11.55 IQR)
- **Magnitude:** 222.04 | **LOC:** 190 | **CtrlFlow:** 25.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `Dispose` (Impact: 35.0), `GetResult` (Impact: 25.1), `CreateContextMenuEntry` (Impact: 25.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.881 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.394 IQR)
- **Top Global Matches:** file_cluster_8: 15.881, file_cluster_11: 16.174, file_cluster_13: 16.212
- **Magnitude:** 20157.34 | **LOC:** 18014 | **CtrlFlow:** 87.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 546
- **Risk Profile:** Cognitive Load (92.7777%), Tech Debt (9.753%)
**Top Internal Functions/Classes:**
  * `RunPanoramaStitchSelfTest` (Impact: 1626.1 | O(N^6) | DB: 546)
  * `BuildFixedOverlayMask` (Impact: 1623.1 | O(N^6) | DB: 254)
  * `RepairOverlayDarkBands` (Impact: 705.6 | O(N^6) | DB: 101)
  * `RepairSuppressedOverlayHoles` (Impact: 362.2 | O(N^6) | DB: 56)
  * `FindBestSmallShiftDownsampledLuma` (Impact: 272.2 | O(N^6) | DB: 60)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2249`, `structural_boundaries: 320`, `args: 784`, `func_start: 66`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 17`, `state_mutation: 12088`, `dead_code: 5`, `duplicate_logic: 2`, `orphaned_logic: 20`
* *Architecture:* `io: 42`, `api: 1`, `concurrency: 18`, `import: 15`
* *Defense:* `safety: 7`, `immutability_locks: 1249`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` fstream, commctrl.h, thread, atomic, pch.h, Utility.h, emmintrin.h, WindowsVersions.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.022 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.578 IQR)
- **Top Global Matches:** file_cluster_8: 15.022, file_cluster_13: 15.321, file_cluster_7: 15.379
- **Magnitude:** 8401.1 | **LOC:** 11756 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 474
- **Risk Profile:** Cognitive Load (94.5192%), Tech Debt (8.265%)
**Top Internal Functions/Classes:**
  * `OptionsTabProc` (Impact: 2224.6 | O(N^6) | DB: 474)
  * `RestoreScreenSaverSettings` (Impact: 913.6 | O(2^N) | DB: 48)
  * `LiveZoomWndProc` (Impact: 424.6 | O(N^6) | DB: 59)
  * `DrawShape` (Impact: 309.9 | O(N^6) | DB: 28)
  * `ApplyScreenSaverSnapshot` (Impact: 105.5 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 962`, `structural_boundaries: 227`, `args: 575`, `func_start: 73`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 3295`, `dead_code: 3`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 29`, `concurrency: 12`, `import: 23`
* *Defense:* `safety: 3`, `immutability_locks: 44`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` logger_helper.h, BreakTimer.h, WindowsVersions.h, gpo.h, vector, tlhelp32.h, trace.h, ProcessWaiter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.224 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.439 IQR)
- **Top Global Matches:** file_cluster_8: 15.224, file_cluster_4: 15.335, file_cluster_13: 15.499
- **Magnitude:** 8137.04 | **LOC:** 5443 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1022
- **Risk Profile:** Cognitive Load (93.9069%), Tech Debt (8.4059%)
**Top Internal Functions/Classes:**
  * `VideoRecordingSession::ShowTrimDialogInt` (Impact: 2052.1 | O(N^6) | DB: 386)
  * `LoadGifFrames` (Impact: 1990.0 | O(2^N) | DB: 1022)
  * `VideoRecordingSession::ShowSaveDialogWit` (Impact: 107.5 | O(N^6) | DB: 25)
    * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingS...
  * `VideoRecordingSession::ShowTrimDialog` (Impact: 96.0 | O(N^4) | DB: 26)
    * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingS...
  * `FindGifFrameIndex` (Impact: 18.4 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 553`, `structural_boundaries: 285`, `args: 231`, `func_start: 59`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 2`, `state_mutation: 3651`, `orphaned_logic: 3`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 132`, `import: 10`
* *Defense:* `safety: 66`, `sync_locks: 10`, `immutability_locks: 235`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` pch.h, Utility.h, cstdlib, Windows.Graphics.Imaging.h, CaptureFrameWait.h, shlwapi.h, filesystem, mmsystem.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` (PYTHON | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.61 IQR)
- **Local Micro-Species:** `Cluster 1: Declarative Glue & Initialization` (Drift: 4.205 IQR)
- **Top Global Matches:** file_cluster_8: 12.61, file_cluster_16: 12.782, file_cluster_7: 12.798
- **Magnitude:** 3192.4 | **LOC:** 2376 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 171
- **Risk Profile:** Cognitive Load (48.5741%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_on_mouse_move` (Impact: 1049.8 | O(N^6) | DB: 171)
  * `from_csv_line` (Impact: 964.0 | O(N^6) | DB: 33)
  * `_load_cursor_log` (Impact: 456.8 | O(N^6) | DB: 38)
  * `_export_analysis` (Impact: 71.6 | O(N^6) | DB: 6)
  * `_create_legend_item` (Impact: 8.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 382`, `structural_boundaries: 175`, `args: 64`, `func_start: 63`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 539`
* *Architecture:* `io: 3`, `api: 26`, `import: 10`
* *Defense:* `safety: 15`, `doc: 140`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` tkinter, csv, typing, enum, re, argparse, dataclasses, sys...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.812 IQR)
- **Top Global Matches:** file_cluster_13: 13.812, file_cluster_8: 13.824, file_cluster_4: 13.85
- **Magnitude:** 2681.4 | **LOC:** 1098 | **CtrlFlow:** 60.1% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (81.4153%), Tech Debt (13.2964%)
**Top Internal Functions/Classes:**
  * `FetchItems` (Impact: 2243.1 | O(2^N) | DB: 73)
  * `OnSearchTextBoxUpdated` (Impact: 88.3 | O(N^6) | DB: 3)
  * `QueueObservedBackgroundFetch` (Impact: 21.7 | O(N^5) | DB: 1)
  * `UpdateCurrentFilter` (Impact: 17.9 | O(N^4) | DB: 1)
  * `FiltersPropertyChanged` (Impact: 14.4 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 161`, `structural_boundaries: 107`, `args: 68`, `func_start: 147`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 205`, `planned_debt: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 13`, `concurrency: 48`, `import: 13`
* *Defense:* `safety: 95`, `doc: 9`, `sync_locks: 14`, `immutability_locks: 3`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.CmdPal.UI.ViewModels.Models, Microsoft.CmdPal.UI.ViewModels.Messages, CommunityToolkit.Mvvm.Input, CommunityToolkit.Mvvm.Messaging, Microsoft.CmdPal.Common, System.Runtime.CompilerServices, Microsoft.CommandPalette.Extensions, Windows.Foundation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/Clipboard.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.674 IQR)
- **Top Global Matches:** file_cluster_8: 12.674, file_cluster_13: 12.86, file_cluster_11: 13.075
- **Magnitude:** 2486.96 | **LOC:** 1156 | **CtrlFlow:** 64.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 60
- **Risk Profile:** Cognitive Load (44.0307%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ReceiveAndProcessClipboardData` (Impact: 718.1 | O(2^N) | DB: 60)
  * `CheckClipboardEx` (Impact: 384.2 | O(2^N) | DB: 29)
  * `ShakeHand` (Impact: 357.5 | O(2^N) | DB: 18)
  * `ConnectAndGetData` (Impact: 244.3 | O(2^N) | DB: 12)
  * `SetClipboardData` (Impact: 151.7 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 78`, `args: 45`, `func_start: 154`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 199`
* *Architecture:* `io: 15`, `api: 14`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 72`, `sync_locks: 1`, `immutability_locks: 11`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Threading.Tasks, System.Globalization, System.Windows.Forms.Clipboard, MouseWithoutBorders.Exceptions, System.Linq, System.Runtime.InteropServices, System.Collections.Specialized...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.922 IQR)
- **Top Global Matches:** file_cluster_13: 12.922, file_cluster_8: 12.959, file_cluster_2: 12.996
- **Magnitude:** 2321.48 | **LOC:** 2914 | **CtrlFlow:** 62.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (29.3739%), Tech Debt (19.6503%)
**Top Internal Functions/Classes:**
  * `ReadFormattedData` (Impact: 350.9 | O(N^6) | DB: 14)
  * `CalculateDataColumnCharWidth` (Impact: 343.4 | O(N^6) | DB: 11)
  * `Canvas_PaintSurface` (Impact: 273.6 | O(N^6) | DB: 15)
  * `DrawSelectionGeometry` (Impact: 147.0 | O(N^6) | DB: 13)
  * `ConvertPositionToOffset` (Impact: 114.9 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 145`, `args: 115`, `func_start: 107`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 267`, `dead_code: 1`, `duplicate_logic: 4`, `orphaned_logic: 5`
* *Architecture:* `api: 72`, `import: 21`
* *Defense:* `safety: 47`, `doc: 177`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Generic, Microsoft.UI, System.Runtime.CompilerServices, Windows.Foundation, Microsoft.UI.Xaml.Input, SkiaSharp.Views.Windows, System.Windows.Input, System.IO...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/fancyzones/FancyZonesLib/FancyZones.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.48 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.143 IQR)
- **Top Global Matches:** file_cluster_13: 13.48, file_cluster_8: 13.502, file_cluster_11: 13.85
- **Magnitude:** 2293.04 | **LOC:** 1194 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 91
- **Risk Profile:** Cognitive Load (93.6656%), Tech Debt (14.8873%)
**Top Internal Functions/Classes:**
  * `FancyZones::OnKeyDown` (Impact: 1809.6 | O(2^N) | DB: 91)
  * `HandleWinHookEvent` (Impact: 76.5 | O(N^4) | DB: 2)
  * `FancyZones::Run` (Impact: 33.1 | O(N^6) | DB: 11)
  * `DisplayChangeTypeName` (Impact: 24.2 | O(N^2))
  * `FancyZones::VirtualDesktopChanged` (Impact: 14.7 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 110`, `args: 104`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `state_mutation: 304`, `orphaned_logic: 5`
* *Architecture:* `api: 1`, `concurrency: 6`, `import: 34`
* *Defense:* `safety: 45`, `immutability_locks: 31`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` VirtualDesktop.h, WindowKeyboardSnap.h, MonitorUtils.h, Settings.h, FancyZonesWinHookEventIDs.h, WorkArea.h, WorkAreaConfiguration.h, KeyboardInput.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.457 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.967 IQR)
- **Top Global Matches:** file_cluster_8: 13.457, file_cluster_13: 13.607, file_cluster_11: 13.862
- **Magnitude:** 2239.12 | **LOC:** 1829 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 22.2%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 191
- **Risk Profile:** Cognitive Load (63.1645%), Tech Debt (13.6426%)
**Top Internal Functions/Classes:**
  * `UninstallPackageIdentityMSIXCA` (Impact: 1218.2 | O(2^N) | DB: 191)
  * `InstallPackageIdentityMSIXCA` (Impact: 163.3 | O(2^N) | DB: 28)
  * `UninstallDSCModuleCA` (Impact: 72.2 | O(2^N) | DB: 19)
  * `InstallDSCModuleCA` (Impact: 63.4 | O(2^N) | DB: 23)
  * `InstallEmbeddedMSIXCA` (Impact: 43.5 | O(2^N) | DB: 10)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 109`, `args: 139`, `func_start: 29`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 590`, `planned_debt: 2`, `orphaned_logic: 3`
* *Architecture:* `io: 8`, `import: 24`
* *Defense:* `safety: 26`, `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` package.h, base_sink.h, string_view, modulesRegistry.h, Windows.Security.Credentials.h, EtwTrace.h, logger.h, clean_video_conference.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.481 IQR)
- **Top Global Matches:** file_cluster_8: 12.481, file_cluster_0: 12.592, file_cluster_13: 12.605
- **Magnitude:** 2090.58 | **LOC:** 2131 | **CtrlFlow:** 78.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (42.686%), Tech Debt (14.0297%)
**Top Internal Functions/Classes:**
  * `SocketStuff` (Impact: 420.9 | O(2^N) | DB: 14)
  * `Close` (Impact: 412.9 | O(2^N) | DB: 5)
  * `StartNewTcpClient` (Impact: 281.7 | O(N^6) | DB: 9)
  * `PreProcessData` (Impact: 208.2 | O(N^6))
  * `TcpReceiveData` (Impact: 184.5 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 45`, `args: 22`, `func_start: 98`, `class_start: 3`
* *Risk/State:* `state_mutation: 144`, `fragile_debt: 1`, `orphaned_logic: 2`
* *Architecture:* `io: 1`, `api: 28`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 64`, `sync_locks: 8`, `immutability_locks: 6`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Generic, System.Collections.Concurrent, System.Net.Sockets, System.Windows.Forms, MouseWithoutBorders.Core, System.Diagnostics.CodeAnalysis, System.Threading, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmScreen.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.257 IQR)
- **Top Global Matches:** file_cluster_8: 12.257, file_cluster_0: 12.338, file_cluster_13: 12.451
- **Magnitude:** 1958.0 | **LOC:** 1227 | **CtrlFlow:** 88.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (72.3477%), Tech Debt (30.6658%)
**Top Internal Functions/Classes:**
  * `WndProc` (Impact: 523.4 | O(2^N) | DB: 14)
  * `HelperTimer_Tick` (Impact: 377.7 | O(N^6) | DB: 9)
  * `PaintMyNameOnDesktop` (Impact: 158.6 | O(N^6) | DB: 5)
  * `ShowMessageOnLogonDesktop` (Impact: 88.8 | O(N^6) | DB: 16)
  * `ChangeIcon` (Impact: 76.8 | O(N^5) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 24`, `args: 44`, `func_start: 162`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 213`, `dead_code: 3`, `orphaned_logic: 16`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 9`, `import: 12`
* *Defense:* `safety: 25`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` MouseWithoutBorders.Core, System.Globalization, MouseWithoutBorders.Class, System.Windows.Forms.Timer, System.Diagnostics.CodeAnalysis, MouseWithoutBorders.Properties, System.Diagnostics, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Helper/FormHelper.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.033 IQR)
- **Top Global Matches:** file_cluster_8: 12.033, file_cluster_13: 12.305, file_cluster_7: 12.531
- **Magnitude:** 1928.06 | **LOC:** 788 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (72.0519%), Tech Debt (30.6641%)
**Top Internal Functions/Classes:**
  * `WndProc` (Impact: 1122.5 | O(2^N) | DB: 23)
  * `MouseUpHandler` (Impact: 101.0 | O(N^6) | DB: 19)
  * `GetClipboardText` (Impact: 86.0 | O(2^N) | DB: 3)
  * `FormHelper_DragEnter` (Impact: 61.9 | O(2^N))
  * `MouseDownMoveHandler` (Impact: 59.0 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 122`, `structural_boundaries: 27`, `args: 31`, `func_start: 136`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 156`, `planned_debt: 1`, `orphaned_logic: 7`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 6`, `import: 11`
* *Defense:* `safety: 32`, `sync_locks: 7`, `immutability_locks: 8`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Globalization, System.Runtime.InteropServices, System.Collections.Specialized, System.Drawing.Imaging, System.Threading, System.Diagnostics, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/launcher/PowerLauncher/ViewModel/MainViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.61 IQR)
- **Top Global Matches:** file_cluster_8: 12.61, file_cluster_13: 12.652, file_cluster_11: 12.911
- **Magnitude:** 1914.36 | **LOC:** 1365 | **CtrlFlow:** 51.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (49.8102%), Tech Debt (90.9149%)
**Top Internal Functions/Classes:**
  * `QueryResults` (Impact: 237.0 | O(N^6) | DB: 14)
  * `RegisterHotkey` (Impact: 159.2 | O(2^N) | DB: 2)
  * `Dispose` (Impact: 138.3 | O(2^N) | DB: 2)
    * *Intent:* // Using OrdinalIgnoreCase since this is internal
  * `OnHotkey` (Impact: 127.7 | O(2^N) | DB: 2)
  * `Save` (Impact: 85.3 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 148`, `structural_boundaries: 141`, `args: 92`, `func_start: 188`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 296`, `planned_debt: 2`, `duplicate_logic: 8`, `orphaned_logic: 14`
* *Architecture:* `api: 63`, `concurrency: 30`, `import: 28`
* *Defense:* `safety: 39`, `doc: 13`, `sync_locks: 7`, `immutability_locks: 9`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Collections.Generic, Common.UI, PowerLauncher.Storage, Mages.Core.Runtime.Converters, System.Windows.Input, Wox.Infrastructure.Hotkey, Wox.Plugin, Wox.Infrastructure.UserSettings...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.236 IQR)
- **Top Global Matches:** file_cluster_8: 11.236, file_cluster_13: 11.625, file_cluster_7: 11.747
- **Magnitude:** 1869.14 | **LOC:** 1123 | **CtrlFlow:** 71.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (37.9846%), Tech Debt (36.3952%)
**Top Internal Functions/Classes:**
  * `MoveRight` (Impact: 280.3 | O(N^6) | DB: 7)
  * `MoveLeft` (Impact: 255.8 | O(N^6) | DB: 7)
  * `MoveToMyNeighbourIfNeeded` (Impact: 199.1 | O(N^6) | DB: 8)
    * *Intent:* #if OLD_VERSION
  * `MoveToMyNeighbourIfNeeded` (Impact: 164.8 | O(N^6) | DB: 1)
    * *Intent:* /* Let's say we have 3 machines A, B, and C. A is the controller machine. * (x, y) is the current Mo...
  * `MoveUp` (Impact: 118.6 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 86`, `args: 68`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 166`, `dead_code: 3`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 3`, `sync_locks: 4`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, MouseWithoutBorders.Class, System.Diagnostics.CodeAnalysis, System.Threading, System.Diagnostics, System, System.Windows.Forms, Microsoft.PowerToys.Telemetry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/PowerRenameUILib/PowerRenameXAML/MainWindow.xaml.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.433 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.673 IQR)
- **Top Global Matches:** file_cluster_8: 13.433, file_cluster_13: 13.634, file_cluster_11: 13.824
- **Magnitude:** 1786.14 | **LOC:** 1394 | **CtrlFlow:** 52.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 89
- **Risk Profile:** Cognitive Load (99.2107%), Tech Debt (82.5498%)
**Top Internal Functions/Classes:**
  * `MainWindow::UpdateMetadataShortcuts` (Impact: 464.4 | O(N^5) | DB: 13)
  * `FindScrollViewer` (Impact: 80.2 | O(2^N) | DB: 6)
  * `MainWindow::SetCheckboxesFromFlags` (Impact: 79.6 | O(N^3) | DB: 17)
  * `MainWindow::CreateShellItemArrayFromPath` (Impact: 59.5 | O(N^5) | DB: 20)
  * `MainWindow::InitAutoComplete` (Impact: 56.4 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 185`, `args: 249`, `func_start: 44`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 624`, `dead_code: 1`, `duplicate_logic: 6`, `orphaned_logic: 31`
* *Architecture:* `import: 23`
* *Defense:* `safety: 5`, `immutability_locks: 96`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` logger_helper.h, microsoft.ui.xaml.window.h, theme_listener.h, theme_helpers.h, string, sstream, exception, vector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.68 IQR)
- **Top Global Matches:** file_cluster_8: 13.68, file_cluster_13: 13.733, file_cluster_11: 13.864
- **Magnitude:** 1783.16 | **LOC:** 1485 | **CtrlFlow:** 59.6% | **Authorship Centralization:** 60.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (27.2208%), Tech Debt (18.7674%)
**Top Internal Functions/Classes:**
  * `ShouldReplacePasteAIConfiguration` (Impact: 273.8 | O(N^5))
  * `Dispose` (Impact: 121.4 | O(2^N) | DB: 2)
  * `MigrateLegacyAIEnablement` (Impact: 106.2 | O(N^5) | DB: 4)
  * `IsServiceTypeAllowedByGPO` (Impact: 69.2 | O(N^5) | DB: 2)
  * `OnPasteAIProvidersCollectionChanged` (Impact: 58.3 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 160`, `args: 83`, `func_start: 150`, `class_start: 1`
* *Risk/State:* `state_mutation: 229`, `orphaned_logic: 11`
* *Architecture:* `api: 41`, `import: 19`
* *Defense:* `safety: 197`, `doc: 4`, `immutability_locks: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, Microsoft.Win32, Microsoft.UI.Dispatching, Microsoft.PowerToys.Settings.UI.Library.Helpers, System.Globalization, Microsoft.PowerToys.Settings.UI.Library.Utilities, System.Collections.Specialized, System.Collections.ObjectModel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/Win32Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.504 IQR)
- **Top Global Matches:** file_cluster_17: 12.504, file_cluster_13: 12.529, file_cluster_8: 12.545
- **Magnitude:** 1770.12 | **LOC:** 1036 | **CtrlFlow:** 41.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (46.7663%), Tech Debt (11.0957%)
**Top Internal Functions/Classes:**
  * `ProgramPaths` (Impact: 270.0 | O(2^N) | DB: 12)
  * `InternetShortcutProgram` (Impact: 261.1 | O(2^N) | DB: 22)
    * *Intent:* // This function filters Internet Shortcut programs
  * `LnkProgram` (Impact: 208.9 | O(2^N) | DB: 15)
  * `GetAppFromPath` (Impact: 134.0 | O(N^5) | DB: 5)
    * *Intent:* // Function to get the Win32 application, given the path to the application
  * `Result` (Impact: 111.2 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 125`, `structural_boundaries: 173`, `args: 63`, `func_start: 79`, `class_start: 3`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 166`, `dead_code: 1`, `orphaned_logic: 3`
* *Architecture:* `io: 18`, `api: 34`, `concurrency: 2`, `import: 19`
* *Defense:* `safety: 55`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Wox.Infrastructure.FileSystemHelper, System.Collections.Generic, Microsoft.Win32, System.Security, Wox.Infrastructure.FileSystemHelper.DirectoryWrapper, System.Windows.Input, Wox.Plugin, System.Text.RegularExpressions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.999 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.666 IQR)
- **Top Global Matches:** file_cluster_8: 13.999, file_cluster_13: 14.271, file_cluster_7: 14.43
- **Magnitude:** 1769.74 | **LOC:** 948 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 138
- **Risk Profile:** Cognitive Load (92.3063%), Tech Debt (66.1919%)
**Top Internal Functions/Classes:**
  * `D2DOverlayWindow::render` (Impact: 409.9 | O(N^5) | DB: 138)
  * `D2DOverlayWindow::show` (Impact: 83.0 | O(N^4) | DB: 41)
  * `render_arrow` (Impact: 79.2 | O(N^5) | DB: 13)
  * `get_window_state` (Impact: 71.8 | O(N^3) | DB: 23)
  * `D2DWindow` (Impact: 43.8 | O(N^5) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 93`, `args: 106`, `func_start: 32`
* *Risk/State:* `state_mutation: 855`, `orphaned_logic: 27`
* *Architecture:* `concurrency: 12`, `import: 10`
* *Defense:* `safety: 1`, `sync_locks: 12`, `immutability_locks: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` window.h, resource.h, start_visible.h, overlay_window.h, tasklist_positions.h, monitors.h, shortcut_guide.h, trace.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.729 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.386 IQR)
- **Top Global Matches:** file_cluster_8: 13.729, file_cluster_13: 13.945, file_cluster_7: 14.177
- **Magnitude:** 1737.68 | **LOC:** 752 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 63
- **Risk Profile:** Cognitive Load (93.031%), Tech Debt (75.134%)
**Top Internal Functions/Classes:**
  * `GetShortcutRemapByType` (Impact: 462.6 | O(N^6) | DB: 63)
  * `GetShortcutRemapCountByType` (Impact: 223.1 | O(N^6) | DB: 29)
  * `AddShortcutRemap` (Impact: 184.9 | O(N^6) | DB: 15)
  * `GetShortcutRemap` (Impact: 94.3 | O(N^5) | DB: 41)
  * `DeleteShortcutRemap` (Impact: 65.3 | O(N^6) | DB: 5)
    * *Intent:* // Function to delete a shortcut remapping
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 70`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 489`, `orphaned_logic: 22`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` logger_helper.h, KeyboardManagerEditor.h, pch.h, keyboard_layout.h, memory, algorithm, EditorHelpers.h, vector...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/common/UITestAutomation/KeyboardHelper.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.55 IQR)
- **Top Global Matches:** file_cluster_8: 8.55, file_cluster_7: 9.044, file_cluster_1: 9.29
- **Magnitude:** 1700.16 | **LOC:** 476 | **CtrlFlow:** 49.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (14.7643%), Tech Debt (14.1965%)
**Top Internal Functions/Classes:**
  * `TranslateKeyHex` (Impact: 1094.9 | O(2^N))
    * *Intent:* /// <summary> /// map the virtual key codes to the corresponding keys. /// </summary>
  * `TranslateKey` (Impact: 536.4 | O(N^5))
    * *Intent:* /// <summary> /// Translates a key to its corresponding SendKeys representation. /// </summary> /// ...
  * `SendWinKeyCombination` (Impact: 19.3 | O(N^4) | DB: 2)
    * *Intent:* /// <summary> /// Sends a combination of keys, including the Windows key, to the system. /// </summa...
  * `SendKeys` (Impact: 5.5 | O(N^3))
    * *Intent:* #pragma warning restore SA1310 // Field names should not contain underscore /// <summary> /// Sends ...
  * `PressKey` (Impact: 5.1 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 148`, `args: 10`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`, `orphaned_logic: 3`
* *Architecture:* `api: 6`, `import: 6`
* *Defense:* `safety: 1`, `doc: 28`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Threading.Tasks, System.Linq, System, System.Runtime.InteropServices, System.Text
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/Helpers.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.05 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.285 IQR)
- **Top Global Matches:** file_cluster_8: 14.05, file_cluster_13: 14.294, file_cluster_17: 14.376
- **Magnitude:** 1693.72 | **LOC:** 927 | **CtrlFlow:** 82.0% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (92.6849%), Tech Debt (40.4609%)
**Top Internal Functions/Classes:**
  * `GetTransformedFileName` (Impact: 396.2 | O(N^6) | DB: 68)
  * `GetEnumeratedFileName` (Impact: 299.1 | O(N^6) | DB: 67)
  * `DataObjectContainsRenamableItem` (Impact: 42.8 | O(N^5) | DB: 12)
  * `GetTrimmedFileName` (Impact: 36.0 | O(N^4) | DB: 14)
  * `GetMetadataFileName` (Impact: 34.1 | O(N^3) | DB: 18)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 182`, `structural_boundaries: 40`, `args: 57`, `func_start: 19`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 719`, `orphaned_logic: 14`
* *Architecture:* `io: 1`, `import: 10`
* *Defense:* `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` regex, pch.h, MetadataTypes.h, unordered_map, unordered_set, algorithm, Helpers.h, filesystem...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.494 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.192 IQR)
- **Top Global Matches:** file_cluster_8: 13.494, file_cluster_13: 13.77, file_cluster_7: 13.953
- **Magnitude:** 1661.92 | **LOC:** 827 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 116
- **Risk Profile:** Cognitive Load (79.279%), Tech Debt (24.6019%)
**Top Internal Functions/Classes:**
  * `MonitorTopology::IsOnOuterEdge` (Impact: 875.4 | O(N^6) | DB: 116)
  * `MonitorTopology::PrioritizeEdgeByDirecti` (Impact: 161.0 | O(N^6) | DB: 1)
  * `MonitorTopology::Initialize` (Impact: 62.2 | O(N^3) | DB: 15)
    * *Intent:* // Copyright (c) Microsoft Corporation // The Microsoft Corporation licenses this file to you under ...
  * `MonitorTopology::IdentifyOuterEdges` (Impact: 41.4 | O(N^4) | DB: 4)
  * `MonitorTopology::EdgesAreAdjacent` (Impact: 34.5 | O(N^2) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 43`, `args: 35`, `func_start: 10`
* *Risk/State:* `state_mutation: 473`, `orphaned_logic: 6`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MonitorTopology.h, pch.h, algorithm, logger.h, cmath, CursorWrapCore.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.519 IQR)
- **Top Global Matches:** file_cluster_0: 11.519, file_cluster_8: 11.542, file_cluster_4: 11.62
- **Magnitude:** 1532.86 | **LOC:** 1029 | **CtrlFlow:** 56.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 100
- **Risk Profile:** Cognitive Load (58.3685%), Tech Debt (30.6407%)
**Top Internal Functions/Classes:**
  * `TestCaseClipboardHistoryDisableTest` (Impact: 1104.2 | O(2^N) | DB: 100)
    * *Intent:* // [x] Open Settings and Disable clipboard history.Open Advanced Paste window with hotkey and observ...
  * `TestCaseClipboardHistoryDeleteTest` (Impact: 95.4 | O(2^N))
    * *Intent:* * Disable Advanced Paste, try different Advanced Paste hotkeys and confirm that it's disabled and no...
  * `TestCaseClipboardHistorySelectTest` (Impact: 55.8 | O(2^N))
  * `AdvancedPasteUITest` (Impact: 21.5 | O(2^N) | DB: 11)
  * `TestCasePasteAsMarkdownCase1` (Impact: 14.2 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 70`, `args: 30`, `func_start: 321`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 22`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `io: 55`, `api: 14`, `concurrency: 95`, `import: 20`
* *Defense:* `safety: 27`, `doc: 6`, `test: 36`, `immutability_locks: 14`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Runtime.CompilerServices, System.Windows.Forms, Microsoft.AdvancedPaste.UITests.Helper, System.Drawing, System.Resources.ResXFileRef, System.Runtime.InteropServices.JavaScript.JSType, System.Threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/fancyzones/editor/FancyZonesEditor/Utils/FancyZonesEditorIO.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.102 IQR)
- **Top Global Matches:** file_cluster_8: 12.102, file_cluster_13: 12.369, file_cluster_0: 12.609
- **Magnitude:** 1485.72 | **LOC:** 992 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (57.1314%), Tech Debt (23.5719%)
**Top Internal Functions/Classes:**
  * `SetAppliedLayouts` (Impact: 113.9 | O(N^6) | DB: 13)
  * `SetCustomLayouts` (Impact: 104.3 | O(N^6) | DB: 9)
  * `SerializeDefaultLayouts` (Impact: 103.0 | O(N^6) | DB: 23)
  * `SetDefaultLayouts` (Impact: 96.7 | O(N^6) | DB: 4)
  * `SerializeCustomLayouts` (Impact: 96.0 | O(N^6) | DB: 35)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 111`, `args: 32`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `state_mutation: 257`, `orphaned_logic: 11`
* *Architecture:* `io: 4`, `api: 13`, `import: 11`
* *Defense:* `safety: 35`, `sync_locks: 48`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Generic, System.Globalization, FancyZonesEditor.Models, FancyZonesEditorCommon.Data, System.Collections.ObjectModel, System.Text.Json, System.Windows, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/Programs/Win32Program.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.712 IQR)
- **Top Global Matches:** file_cluster_8: 12.712, file_cluster_13: 12.755, file_cluster_11: 12.903
- **Magnitude:** 1463.84 | **LOC:** 1097 | **CtrlFlow:** 47.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (57.9397%), Tech Debt (13.7111%)
**Top Internal Functions/Classes:**
  * `GetPathFromRegistrySubkey` (Impact: 146.3 | O(N^6) | DB: 7)
  * `LnkProgram` (Impact: 133.1 | O(N^6) | DB: 15)
  * `InternetShortcutProgram` (Impact: 132.4 | O(N^6) | DB: 22)
    * *Intent:* // This function filters Internet Shortcut programs
  * `ProgramPaths` (Impact: 130.0 | O(N^6) | DB: 12)
  * `GetAppFromPath` (Impact: 124.2 | O(N^4) | DB: 5)
    * *Intent:* // Function to get the Win32 application, given the path to the application
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 174`, `args: 50`, `func_start: 87`, `class_start: 2`
* *Risk/State:* `state_mutation: 202`, `dead_code: 1`, `orphaned_logic: 5`
* *Architecture:* `io: 19`, `api: 34`, `concurrency: 9`, `import: 16`
* *Defense:* `safety: 58`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.161
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Collections.Generic, System.Threading.Tasks, Microsoft.Win32, Microsoft.CommandPalette.Extensions, System.Text.RegularExpressions, Microsoft.CmdPal.Ext.Apps.Properties, System.Collections.Concurrent, Microsoft.CmdPal.Ext.Apps.Utils...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Helpers/NativeMethods.cs` (CSHARP) | Magnitude: 63.73 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 31, state_mutation: 13, pointers: 9, api: 7
- `src/modules/colorPicker/ColorPickerUI.UnitTests/Helpers/ColorRepresentationHelperTest.cs` (CSHARP) | Magnitude: 10.98 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 26, decorators: 18, structural_boundaries: 7, import: 4
- `src/modules/powerdisplay/PowerDisplay.Lib/Serialization/ProfileSerializationContext.cs` (CSHARP) | Magnitude: 19.42 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, decorators: 9, structural_boundaries: 5, doc: 4
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.cs` (CSHARP) | Magnitude: 154.8 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 144, encapsulation: 36, func_start: 33, immutability_locks: 26
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/BackdropStyles.cs` (CSHARP) | Magnitude: 85.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 45, state_mutation: 27, doc: 9, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/modules/MouseWithoutBorders/App/Form/frmScreen.Designer.cs` (CSHARP) | Magnitude: 87.72 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 213, sec_high_risk_execution: 115, state_mutation: 48, events: 30
- `src/modules/MouseWithoutBorders/App/Form/Settings/SettingsFormPage.Designer.cs` (CSHARP) | Magnitude: 41.12 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, sec_high_risk_execution: 21, doc: 11, state_mutation: 9
- `src/modules/MouseUtils/MouseJumpUI/MainForm.Designer.cs` (CSHARP) | Magnitude: 42.24 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, state_mutation: 15, sec_high_risk_execution: 15, doc: 11
- `src/modules/MouseWithoutBorders/App/Form/frmMouseCursor.Designer.cs` (CSHARP) | Magnitude: 48.12 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, state_mutation: 17, sec_high_risk_execution: 13, doc: 11
- `src/modules/MouseWithoutBorders/App/Form/frmLogon.Designer.cs` (CSHARP) | Magnitude: 47.98 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 51, sec_high_risk_execution: 21, state_mutation: 16, doc: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tools/project_template/ModuleTemplate/dllmain.cpp` (CPP) | Magnitude: 0.07 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 17, state_mutation: 17, branch: 9
- `src/modules/cmdpal/doc/initial-sdk-spec/generate-interface.ps1` (POWERSHELL) | Magnitude: 83.64 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 68, state_mutation: 61, branch: 16, closures: 12
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/TreeContent.cs` (CSHARP) | Magnitude: 35.4 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, state_mutation: 6, branch: 5
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/ContentPage.cs` (CSHARP) | Magnitude: 33.1 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 8, state_mutation: 6, branch: 5
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListItemViewModel.cs` (CSHARP) | Magnitude: 653.48 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 220, state_mutation: 87, safety: 59, branch: 56

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
- `src/dsc/v3/PowerToys.DSC/Models/FunctionData/ISettingsFunctionData.cs` (CSHARP) | Magnitude: 39.77 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 27, api: 8, indent_spaces: 7, args: 5
- `src/modules/MeasureTool/MeasureToolUI/MeasureToolXAML/MainWindow.xaml.cs` (CSHARP) | Magnitude: 201.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 167, func_start: 45, structural_boundaries: 36, args: 28
- `src/modules/MouseWithoutBorders/App/Core/Logger.cs` (CSHARP) | Magnitude: 698.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 380, state_mutation: 90, branch: 61, func_start: 36
- `src/modules/cmdpal/ext/SamplePagesExtension/Pages/SampleCommentsPage.cs` (CSHARP) | Magnitude: 80.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 82, state_mutation: 21, structural_boundaries: 20, args: 15
- `src/modules/launcher/Wox.Plugin/PluginLoadContext.cs` (CSHARP) | Magnitude: 39.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 14, import: 6, args: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/StatusMessage.cs` (CSHARP) | Magnitude: 24.64 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 8, state_mutation: 7, api: 4, args: 3
- `src/modules/powerdisplay/PowerDisplay.Lib/Models/Monitor.cs` (CSHARP) | Magnitude: 186.96 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 190, doc: 134, state_mutation: 113, structural_boundaries: 40
- `src/modules/powerdisplay/PowerDisplay.Lib/Models/VcpCapabilities.cs` (CSHARP) | Magnitude: 252.96 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 128, indent_spaces: 128, state_mutation: 59, api: 51
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/CommandProvider.cs` (CSHARP) | Magnitude: 82.46 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 41, doc: 22, api: 16, structural_boundaries: 13
- `src/modules/cmdpal/Microsoft.CmdPal.Common/Helpers/InterlockedBoolean.cs` (CSHARP) | Magnitude: 40.12 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: state_mutation: 17, indent_spaces: 16, doc: 14, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Apps/IAppCache.cs` (CSHARP) | Magnitude: 24.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 5, indent_spaces: 4, import: 3
- `src/common/UITestAutomation/Element/ComboBox.cs` (CSHARP) | Magnitude: 23.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, doc: 11, func_start: 7, api: 4
- `src/modules/Workspaces/WorkspacesEditorUITest/WorkspacesEditingPageTests.cs` (CSHARP) | Magnitude: 180.1 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 166, structural_boundaries: 57, func_start: 47, generics: 40
- `src/modules/launcher/Plugins/Microsoft.Plugin.Program/ProgramPluginSettings.cs` (CSHARP) | Magnitude: 37.4 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, api: 12, state_mutation: 10, structural_boundaries: 4
- `src/modules/LightSwitch/Tests/LightSwitch.UITests/TestHelper.cs` (CSHARP) | Magnitude: 539.52 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 313, func_start: 120, structural_boundaries: 78, sec_high_risk_execution: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/settings-ui/Settings.UI/ViewModels/ProfileEditorViewModel.cs` (CSHARP) | Magnitude: 150.28 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, state_mutation: 29, structural_boundaries: 25, branch: 20
- `src/modules/launcher/Plugins/Microsoft.Plugin.Program/Programs/Win32Program.cs` (CSHARP) | Magnitude: 1770.12 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 693, structural_boundaries: 173, state_mutation: 166, branch: 125
- `src/modules/cmdpal/Tests/Microsoft.CommandPalette.Extensions.Toolkit.UnitTests/ListHelpersInPlaceUpdateTests.cs` (CSHARP) | Magnitude: 233.3 | Delta: **0.082 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 360, func_start: 147, structural_boundaries: 144, test: 60
- `src/common/Common.Search/FuzzSearch/StringMatcher.cs` (CSHARP) | Magnitude: 351.42 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 181, state_mutation: 59, structural_boundaries: 38, branch: 35
- `src/modules/EnvironmentVariables/EnvironmentVariablesUILib/ViewModels/MainViewModel.cs` (CSHARP) | Magnitude: 540.6 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 329, state_mutation: 93, structural_boundaries: 71, func_start: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/CommandPalettePreview.xaml.cs` (CSHARP) | Magnitude: 142.36 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, structural_boundaries: 41, state_mutation: 38, args: 33
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/TitleBar/TitleBar.Properties.cs` (CSHARP) | Magnitude: 86.08 | Delta: **0.128 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 105, doc: 72, structural_boundaries: 30, state_mutation: 30
- `src/settings-ui/Settings.UI/SettingsXAML/Controls/OOBEPageControl.xaml.cs` (CSHARP) | Magnitude: 23.56 | Delta: **0.138 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 37, api: 12, structural_boundaries: 11, ui_framework: 10
- `src/modules/colorPicker/ColorPickerUI/Helpers/ControlHelper.cs` (CSHARP) | Magnitude: 164.1 | Delta: **0.145 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 158, doc: 72, func_start: 47, args: 29
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Dock/DockContentControl.xaml.cs` (CSHARP) | Magnitude: 42.26 | Delta: **0.147 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 67, structural_boundaries: 22, api: 20, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/modules/peek/Peek.FilePreviewer/Previewers/MediaPreviewer/AudioPreviewer.cs` (CSHARP) | Magnitude: 233.6 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 55, concurrency: 44, func_start: 37
- `src/modules/Workspaces/WorkspacesEditor/Models/Project.cs` (CSHARP) | Magnitude: 401.42 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 331, state_mutation: 137, structural_boundaries: 56, branch: 36
- `src/modules/fancyzones/FancyZonesLib/ZonesOverlay.h` (CPP) | Magnitude: 44.22 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, concurrency: 18, import: 11, structural_boundaries: 10
- `src/modules/LightSwitch/LightSwitchService/LightSwitchStateManager.h` (CPP) | Magnitude: 21.74 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, state_mutation: 12, structural_boundaries: 10, concurrency: 6
- `src/modules/MouseUtils/MousePointerCrosshairs/dllmain.cpp` (CPP) | Magnitude: 183.64 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 187, state_mutation: 71, structural_boundaries: 43, immutability_locks: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.Registry/Constants/MaxTextLength.cs` (CSHARP) | Magnitude: 20.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 15, indent_spaces: 7, api: 5, immutability_locks: 4
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/WindowPosition.cs` (CSHARP) | Magnitude: 13.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 27, structural_boundaries: 12, indent_spaces: 12, api: 10
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Bookmark/Helpers/CommandKind.cs` (CSHARP) | Magnitude: 17.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 36, indent_spaces: 11, structural_boundaries: 2, class_start: 1
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/AsyncNavigationRequest.cs` (CSHARP) | Magnitude: 30.32 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 5, structural_boundaries: 2, branch: 1, args: 1
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Services/IExtensionTemplateService.cs` (CSHARP) | Magnitude: 17.74 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 2, args: 1, func_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.Shell/Pages/ShellListPage.cs` (CSHARP) | Magnitude: 419.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 328, state_mutation: 110, structural_boundaries: 80, branch: 64
- `src/settings-ui/Settings.UI/SettingsXAML/Views/PowerOcrPage.xaml.cs` (CSHARP) | Magnitude: 27.22 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 8, func_start: 8, args: 5
- `src/modules/ShortcutGuide/ShortcutGuide/d2d_text.h` (CPP) | Magnitude: 22.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 8, state_mutation: 6, args: 3, structural_boundaries: 2
- `src/modules/keyboardmanager/KeyboardManagerEditorLibrary/KeyDropDownControl.cpp` (CPP) | Magnitude: 624.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 244, state_mutation: 233, args: 50, branch: 46
- `src/modules/keyboardmanager/KeyboardManagerEngineLibrary/KeyboardEventHandlers.h` (CPP) | Magnitude: 43.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 29, state_mutation: 28, args: 22, immutability_locks: 14

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

- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs` -> Churn: **97.48%** | Cog Load: 50.3302% | Debt: 49.3132%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Pages/ShellPage.xaml.cs` -> Churn: **93.72%** | Cog Load: 16.3803% | Debt: 72.8069%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs` -> Churn: **83.11%** | Cog Load: 57.6887% | Debt: 13.6802%
- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` -> Churn: **77.98%** | Cog Load: 94.5192% | Debt: 8.265%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandProviderWrapper.cs` -> Churn: **76.17%** | Cog Load: 66.0756% | Debt: 17.1636%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/modules/ZoomIt/ZoomIt/PanoramaCapture.cpp` -> **Alex Mihaiuc** (100.0% isolated ownership) | Magnitude: 20157.34
- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` -> **Niels Laute** (100.0% isolated ownership) | Magnitude: 3192.4
- `src/modules/MouseWithoutBorders/App/Core/Clipboard.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 2486.96
- `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 2090.58
- `src/modules/MouseWithoutBorders/App/Form/frmScreen.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 1958.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/modules/keyboardmanager/common/Input.h` -> **Severity: 1558.7** (Blast Radius: 15.848 * Doc Risk: 98.3531%)
- `src/modules/powerrename/PowerRenameUILib/Utils.h` -> **Severity: 681.964** (Blast Radius: 8.453 * Doc Risk: 80.6771%)
- `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions/Microsoft.CommandPalette.Extensions.def` -> **Severity: 582.52** (Blast Radius: 29.126 * Doc Risk: 20.0%)
- `src/modules/MouseWithoutBorders/App/Class/Extensions.cs` -> **Severity: 246.898** (Blast Radius: 2.469 * Doc Risk: 99.9991%)
- `src/modules/powerrename/lib/PowerRenameInterfaces.h` -> **Severity: 217.694** (Blast Radius: 2.375 * Doc Risk: 91.6608%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
