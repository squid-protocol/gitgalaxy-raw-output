# ARCHITECTURAL_BRIEF: PowerToys
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/PowerToys.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 7753 |
| Analyzed Artifacts (Scanned) | 5289 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2464 |
| Total LOC | 422153 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 68.2% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3035 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 251 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 3366 | 279289 | 63.6% |
| CPP | 1273 | 128835 | 24.1% |
| MARKDOWN | 195 | 0 | 3.7% |
| XML | 193 | 428 | 3.6% |
| JSON | 131 | 6279 | 2.5% |
| PLAINTEXT | 39 | 0 | 0.7% |
| MAKEFILE | 36 | 202 | 0.7% |
| POWERSHELL | 31 | 3525 | 0.6% |
| JAVASCRIPT | 10 | 622 | 0.2% |
| BATCH | 4 | 32 | 0.1% |
| HTML | 4 | 206 | 0.1% |
| PYTHON | 4 | 2674 | 0.1% |
| C | 3 | 61 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 5040 | 95.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 234 | 4.4% |
| Static: Minified & Vendor Opaque Mass | 15 | 0.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2464*

**Composition by Extension & Reason:**
- `.png`: 861x Excluded (Explicitly Denied Extension: '.png'), 3x Excluded (Explicitly Denied Extension: '.PNG')
- `.xaml`: 278x Unsupported Format (.xaml), 1x Excluded (Saturation: Line 79 exceeds 500 chars), 1x Excluded (Saturation: Line 33 exceeds 500 chars)
- `.csproj`: 186x Unsupported Format (.csproj), 1x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.vcxproj`: 119x Unsupported Format (.vcxproj), 2x Excluded (Unsupported Extension: '.vcxproj')
- `.resx`: 121x Unsupported Format (.resx)
- `.js`: 87x Excluded (Saturation: Line 8 exceeds 500 chars), 20x Excluded (Saturation: Line 6 exceeds 500 chars), 1x Excluded (Embedded Array/Matrix Payload: 113380 commas in 761 LOC)
- `.filters`: 105x Unsupported Format (.filters), 1x Excluded (Unsupported Extension: '.filters')
- `.rc`: 76x Unsupported Format (.rc), 12x Excluded (Binary Format Detected), 1x Excluded (Unsupported Extension: '.rc')
- `.ico`: 70x Excluded (Explicitly Denied Extension: '.ico')
- `.md`: 39x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 8 LOC), 1x Excluded (Machine-Generated Source Code Signature: 70 LOC)
- `.yml`: 41x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.manifest`: 41x Unsupported Format (.manifest)
- `.ps1`: 38x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.props`: 29x Unsupported Format (.props), 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.props')
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.appxmanifest), 8x Unsupported Format (.undeterminable)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.4 | 2.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 33.3 | 38.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 28.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.5 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.9 | 3.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 35.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 83.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 8.9 | 1.4 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 5.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 54.8 | 96.6 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 82.1 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16287 | 1281 | 5 | `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` |
| cleanup | 898 | 361 | 0 | `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` |
| guards | 43177 | 3207 | 23 | `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` |
| danger | 2429 | 893 | 1 | `src/modules/MouseUtils/MouseUtils.UITests/FindMyMouseTests.cs` |
| concurrency | 6875 | 744 | 2 | `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` |
| connectivity | 25013 | 3799 | 11 | `src/modules/MouseWithoutBorders/App/Class/NativeMethods.cs` |
| io | 2022 | 447 | 0 | `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 66 | 0 | `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` |
| time | 563 | 211 | 0 | `src/settings-ui/Settings.UI/SettingsXAML/Controls/Timeline/Timeline.xaml.cs` |
| serialization | 135 | 67 | 0 | `src/settings-ui/Settings.UI.UnitTests/ViewModelTests/PowerPreview.cs` |
| regex | 229 | 67 | 0 | `src/modules/launcher/Plugins/Microsoft.PowerToys.Run.Plugin.TimeDate/Components/TimeAndDateHelper.cs` |
| events | 3752 | 716 | 2 | `src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs` |
| tests | 4368 | 264 | 0 | `src/modules/powerdisplay/PowerDisplay.Lib.UnitTests/MccsCapabilitiesParserTests.cs` |
| docs | 23263 | 1187 | 10 | `src/modules/launcher/Wox.Plugin/Common/Win32/NativeMethods.cs` |
| debt | 1288 | 325 | 0 | `src/modules/MouseUtils/CursorWrap/CursorWrapTests/analyze_test_results.py` |
| mutation | 100711 | 3403 | 51 | `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` |
| dead_code | 8872 | 2488 | 5 | `src/common/interop/Constants.cpp` |
| credential | 63 | 25 | 0 | `src/common/interop/shared_constants.h` |
| threat | 2111 | 540 | 1 | `src/modules/ZoomIt/ZoomIt/resource.h` |
| ml_ai | 686 | 154 | 0 | `src/common/ManagedCommon/ColorFormatHelper.cs` |
| ui | 895 | 165 | 0 | `src/settings-ui/Settings.UI/ViewModels/DashboardViewModel.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `.github/skills/winmd-api-search/scripts/cache-generator/Program.cs` (Hits: 87)
- `src/modules/AdvancedPaste/UITest-AdvancedPaste/AdvancedPasteUITest.cs` (Hits: 61)
- `src/settings-ui/Settings.UI.Library/SettingsBackupAndRestoreUtils.cs` (Hits: 57)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Microsoft.CommandPalette.Extensions.def** (`src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions/Microsoft.CommandPalette.Extensions.def`) — 228 inbound connections
2. **Input.h** (`src/modules/keyboardmanager/common/Input.h`) — 136 inbound connections
3. **logger.h** (`src/common/logger/logger.h`) — 135 inbound connections
4. **Services.svg** (`src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WindowsServices/Assets/Services.svg`) — 107 inbound connections
5. **settings_helpers.h** (`src/common/SettingsAPI/settings_helpers.h`) — 76 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **pch.h** (`src/modules/ZoomIt/ZoomIt/pch.h`) — 82 outbound dependencies
2. **pch.h** (`src/modules/cmdpal/Microsoft.Terminal.UI/pch.h`) — 52 outbound dependencies
3. **pch.h** (`src/modules/MeasureTool/MeasureToolCore/pch.h`) — 51 outbound dependencies
4. **CaptureFrameWait.h** (`src/modules/ZoomIt/ZoomIt/CaptureFrameWait.h`) — 50 outbound dependencies
5. **main.cpp** (`src/runner/main.cpp`) — 49 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `MainWndProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **755.7** | LOC: 1340
  * *Intent:* //---------------------------------------------------------------------------- // // MainWndProc // //------------------------------------------------...
- `VideoRecordingSession::TrimDialogProc` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **523.5** | LOC: 1302
  * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingSession::TrimDialogProc // // Dialog procedure for ...
- `OptionsProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **476.8** | LOC: 860
  * *Intent:* //---------------------------------------------------------------------------- // // OptionsProc // //------------------------------------------------...
- `LiveZoomWndProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **331.6** | LOC: 505
  * *Intent:* //---------------------------------------------------------------------------- // // LiveZoomWndProc // //--------------------------------------------...
- `ValidateShortcutBufferElement` (@ `src/modules/keyboardmanager/KeyboardManagerEditorLibrary/BufferValidationHelpers.cpp`) -> Impact: **267.1** | LOC: 241
  * *Intent:* // Function to validate an element of the shortcut remap buffer when the selection has changed
- `TimelineSubclassProc` (@ `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp`) -> Impact: **253.7** | LOC: 417
- `SettingsLoader::ParseHotkeyObject` (@ `tools/module_loader/src/SettingsLoader.cpp`) -> Impact: **206.3** | LOC: 126
- `wWinMain` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **206.1** | LOC: 365
  * *Intent:* #endif //---------------------------------------------------------------------------- // // WinMain // //---------------------------------------------...
- `GetTransformedFileName` (@ `src/modules/powerrename/lib/Helpers.cpp`) -> Impact: **201.2** | LOC: 202
- `AdvancedBreakProc` (@ `src/modules/ZoomIt/ZoomIt/Zoomit.cpp`) -> Impact: **179.5** | LOC: 325
  * *Intent:* //---------------------------------------------------------------------------- // // AdvancedBreakProc // //------------------------------------------...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/modules/ZoomIt/ZoomIt` | 28 | 12756.64 | 22.9% | 13.46% |
| `src/settings-ui/Settings.UI/ViewModels` | 41 | 6753.06 | 25.49% | 19.17% |
| `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels` | 94 | 6129.69 | 19.46% | 33.01% |
| `src/modules/MouseWithoutBorders/App/Core` | 29 | 4956.48 | 38.8% | 20.79% |
| `src/settings-ui/Settings.UI.Library` | 153 | 4786.38 | 5.91% | 45.16% |
| `src/modules/fancyzones/FancyZonesLib` | 70 | 4708.6 | 17.33% | 31.83% |
| `src/modules/powerrename/lib` | 40 | 4653.32 | 22.96% | 18.68% |
| `src/modules/MouseWithoutBorders/App/Class` | 16 | 3964.36 | 44.73% | 30.6% |
| `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit` | 74 | 3314.44 | 15.48% | 33.04% |
| `src/modules/MouseWithoutBorders/App/Form` | 14 | 3092.8 | 46.78% | 62.33% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/common/GPOWrapperProjection/GPOWrapper.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/By.cs` -> **100.0%** Exposure
- `src/common/UITestAutomation/Element/Window.cs` -> **100.0%** Exposure
- `src/modules/AdvancedPaste/AdvancedPaste/Helpers/KernelExtensions.cs` -> **100.0%** Exposure
- `src/modules/PowerOCR/PowerOCR/Helpers/OSInterop.cs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/skills/release-note-generation/scripts/apply-labels.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/collect-or-apply-milestones.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/diff_prs.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/dump-prs-since-commit.ps1` -> **100.0%** Exposure
- `.github/skills/release-note-generation/scripts/find-commit-by-title.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/common/interop/Constants.cpp` -> **73** Orphaned Functions | **0** Duplicates
- `src/common/GPOWrapper/GPOWrapper.cpp` -> **72** Orphaned Functions | **0** Duplicates
- `src/modules/cmdpal/Tests/Microsoft.CommandPalette.Extensions.Toolkit.UnitTests/ListHelpersInPlaceUpdateTests.cs` -> **51** Orphaned Functions | **0** Duplicates
- `src/modules/keyboardmanager/KeyboardManagerEditorUI/Controls/UnifiedMappingControl.xaml.cs` -> **48** Orphaned Functions | **0** Duplicates
- `src/modules/powerdisplay/PowerDisplay.Lib.UnitTests/MccsCapabilitiesParserTests.cs` -> **46** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/modules/cmdpal/Tests/Microsoft.CmdPal.Common.UnitTests/Services/Sanitizer/SecretKeyValueRulesProviderTests.cs` -> **82.1257%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `49` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `20054` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/modules/MouseWithoutBorders/App/Core/DragDrop.cs` (CSHARP) -> Cumulative Risk: **751.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 244.44 | **LOC:** 405 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (91.2628%)
- **Heaviest Functions:** `DragDropStep05Ex` (Impact: 13.8), `DragDropStep04` (Impact: 12.3), `DragDropStep01` (Impact: 9.8)

### 2. `src/modules/LightSwitch/LightSwitchService/LightSwitchSettings.cpp` (CPP) -> Cumulative Risk: **733.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 156.82 | **LOC:** 302 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9457%), Cognitive Load (91.0033%)
- **Heaviest Functions:** `LightSwitchSettings::LoadSettings` (Impact: 36.1), `LightSwitchSettings::InitFileWatcher` (Impact: 9.8), `LightSwitchSettings::~LightSwitchSettings` (Impact: 5.3)

### 3. `src/settings-ui/Settings.UI/SettingsXAML/Views/LightSwitchPage.xaml.cs` (CSHARP) -> Cumulative Risk: **728.54**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 261.76 | **LOC:** 422 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 58.3%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `ModeSelector_SelectionChanged` (Impact: 18.4), `ViewModel_PropertyChanged` (Impact: 17.6), `CityAutoSuggestBox_TextChanged` (Impact: 11.2)

### 4. `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` (CPP) -> Cumulative Risk: **715.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 6671.66 | **LOC:** 11756 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 20.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9928%), Cognitive Load (89.0414%)
- **Heaviest Functions:** `MainWndProc` (Impact: 755.7), `OptionsProc` (Impact: 476.8), `LiveZoomWndProc` (Impact: 331.6)

### 5. `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/TopLevelCommandManager.cs` (CSHARP) -> Cumulative Risk: **715.86**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 582.08 | **LOC:** 870 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9986%), Documentation (98.3051%), State Flux (96.8284%)
- **Heaviest Functions:** `AppendCommandsWhenReadyAsync` (Impact: 40.3), `TryLoadCommandsAsync` (Impact: 32.6), `RegisterAndLoadCommandsAsync` (Impact: 29.7)

### 6. `src/modules/cmdpal/Microsoft.CmdPal.UI/Helpers/Icons/IconLoaderService.cs` (CSHARP) -> Cumulative Risk: **714.88**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 189.56 | **LOC:** 222 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `EnqueueLoad` (Impact: 12.6), `LoadIconCoreAsync` (Impact: 12.1), `ProcessQueueAsync` (Impact: 11.7)

### 7. `src/modules/MouseWithoutBorders/App/Core/Event.cs` (CSHARP) -> Cumulative Risk: **713.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 203.78 | **LOC:** 280 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Concurrency (99.4585%)
- **Heaviest Functions:** `PrepareToSwitchToMachine` (Impact: 31.7), `MouseEvent` (Impact: 26.4), `KeybdEvent` (Impact: 8.5)

### 8. `src/modules/cmdpal/ext/Microsoft.CmdPal.Ext.WinGet/Pages/InstallPackageCommand.cs` (CSHARP) -> Cumulative Risk: **709.99**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 253.58 | **LOC:** 252 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `OnInstallProgress` (Impact: 29.7), `OnUninstallProgress` (Impact: 22.1), `Invoke` (Impact: 9.4)

### 9. `src/modules/peek/Peek.FilePreviewer/FilePreview.xaml.cs` (CSHARP) -> Cumulative Risk: **707.17**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 266.82 | **LOC:** 413 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.992%), State Flux (99.9691%), Tech Debt (98.42%)
- **Heaviest Functions:** `Previewer_PropertyChanged` (Impact: 11.3), `UpdateTooltipAsync` (Impact: 11.2), `KeyboardAccelerator_Space_Invoked` (Impact: 8.0)

### 10. `src/modules/PowerOCR/PowerOCR/OCROverlay.xaml.cs` (CSHARP) -> Cumulative Risk: **707.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 378.5 | **LOC:** 521 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9995%), Cognitive Load (88.3002%)
- **Heaviest Functions:** `LanguagesComboBox_SelectionChanged` (Impact: 53.2), `KeyPressed` (Impact: 42.6), `RegionClickCanvas_MouseUp` (Impact: 23.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6671.66 | **LOC:** 11756 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (89.0414%), Tech Debt (8.317%)
**Top Internal Functions/Classes:**
  * `MainWndProc` (Impact: 755.7)
    * *Intent:* //---------------------------------------------------------------------------- // // MainWndProc // ...
  * `OptionsProc` (Impact: 476.8)
    * *Intent:* //---------------------------------------------------------------------------- // // OptionsProc // ...
  * `LiveZoomWndProc` (Impact: 331.6)
    * *Intent:* //---------------------------------------------------------------------------- // // LiveZoomWndProc...
  * `wWinMain` (Impact: 206.1)
    * *Intent:* #endif //---------------------------------------------------------------------------- // // WinMain ...
  * `AdvancedBreakProc` (Impact: 179.5)
    * *Intent:* //---------------------------------------------------------------------------- // // AdvancedBreakPr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 730 instances
* *Concurrency (weighted view):* 90
* *Memory Alloc (weighted view):* 16
* *State Mutation (weighted view):* 2589
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2154`, `structural_boundaries: 395`, `args: 855`, `func_start: 121`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 1129`, `dead_code: 22`, `planned_debt: 1`, `fragile_debt: 5`
* *Architecture:* `io: 10`, `api: 18`, `concurrency: 20`, `import: 23`
* *Defense:* `safety: 28`, `doc: 4`, `immutability_locks: 100`, `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` trace.h, BreakTimer.h, GifRecordingSession.h, PanoramaCapture.h, Utility.h, WindowsVersions.h, ZoomItSettings.h, array...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/VideoRecordingSession.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3105.72 | **LOC:** 5443 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (66.0621%), Tech Debt (12.1139%)
**Top Internal Functions/Classes:**
  * `VideoRecordingSession::TrimDialogProc` (Impact: 523.5)
    * *Intent:* //---------------------------------------------------------------------------- // // VideoRecordingS...
  * `TimelineSubclassProc` (Impact: 253.7)
  * `StartPlaybackAsync` (Impact: 150.6)
  * `LoadGifFrames` (Impact: 107.3)
  * `VideoRecordingSession::ShowTrimDialogInternal` (Impact: 94.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 11 instances
* *Amplified Cascading Flux:* 254 instances
* *Concurrency (weighted view):* 87
* *State Mutation (weighted view):* 909
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 780`, `structural_boundaries: 362`, `args: 273`, `func_start: 67`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 401`, `unreferenced_by_name: 22`
* *Architecture:* `io: 3`, `api: 1`, `concurrency: 32`, `import: 10`
* *Defense:* `safety: 80`, `sync_locks: 33`, `immutability_locks: 371`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` CaptureFrameWait.h, Utility.h, VideoRecordingSession.h, cstdlib, filesystem, mmsystem.h, pch.h, shlwapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` (PYTHON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2235.8 | **LOC:** 2376 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.6127%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `_analyze_wrap_problem` (Impact: 73.5)
    * *Intent:* """ Analyze why a wrap destination doesn't exist for a given edge range. This provides detailed diag...
  * `_show_segment_detail` (Impact: 56.1)
    * *Intent:* """Show detailed information about a segment in a popup."""
  * `find_nearest_opposite_edge` (Impact: 50.6)
  * `_update_info_panel` (Impact: 50.6)
    * *Intent:* """Update the info panel with loaded data."""
  * `_draw_cursor_position` (Impact: 35.6)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argparse, csv, dataclasses, enum, json, re, sys, tkinter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/registrypreview/RegistryPreviewUILib/Controls/HexBox/HexBox.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1578.56 | **LOC:** 2914 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.9954%), Tech Debt (18.0962%)
**Top Internal Functions/Classes:**
  * `Canvas_PaintSurface` (Impact: 147.0)
  * `OnKeyDown` (Impact: 84.7)
    * *Intent:* /// <inheritdoc/>
  * `ReadFormattedData` (Impact: 56.9)
  * `CalculateDataColumnCharWidth` (Impact: 55.4)
  * `DrawSelectionGeometry` (Impact: 47.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 215 instances
* *State Mutation (weighted view):* 719
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 391`, `structural_boundaries: 180`, `args: 121`, `func_start: 68`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 289`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 13`
* *Architecture:* `api: 73`, `import: 21`
* *Defense:* `safety: 69`, `doc: 190`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.203
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.UI, Microsoft.UI.Input, Microsoft.UI.Xaml, Microsoft.UI.Xaml.Controls, Microsoft.UI.Xaml.Controls.Primitives, Microsoft.UI.Xaml.Input, Microsoft.UI.Xaml.Media, RegistryPreviewUILib.HexBox.Library.EndianConvert...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1340.28 | **LOC:** 2131 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (59.4057%), Tech Debt (9.4193%)
**Top Internal Functions/Classes:**
  * `MainTCPRoutine` (Impact: 117.2)
  * `SendClipboardData` (Impact: 71.0)
  * `SocketStuff` (Impact: 64.2)
  * `UpdateTcpSockets` (Impact: 56.7)
  * `StartNewTcpClient` (Impact: 55.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 132 instances
* *Concurrency (weighted view):* 45
* *State Mutation (weighted view):* 457
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 101`, `args: 50`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `state_mutation: 193`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 32`, `concurrency: 15`, `import: 19`
* *Defense:* `safety: 184`, `sync_locks: 12`, `immutability_locks: 9`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` MouseWithoutBorders.Core, MouseWithoutBorders.Core.Clipboard, MouseWithoutBorders.Core.Thread, MouseWithoutBorders.Exceptions, System, System.Collections.Concurrent, System.Collections.Generic, System.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmMatrix.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 952.34 | **LOC:** 1238 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.9345%), Tech Debt (78.7963%)
**Top Internal Functions/Classes:**
  * `HelperTimer_Tick` (Impact: 46.0)
  * `FrmMatrix_Load` (Impact: 43.9)
  * `Form_DragOver` (Impact: 27.9)
  * `ButtonOK_Click` (Impact: 23.9)
  * `LoadMachines` (Impact: 13.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 146 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 531
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 23`, `args: 59`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 239`, `dead_code: 2`, `unreferenced_by_name: 37`
* *Architecture:* `api: 5`, `concurrency: 1`, `import: 12`
* *Defense:* `safety: 6`, `sync_locks: 2`, `immutability_locks: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, MouseWithoutBorders.Core, MouseWithoutBorders.Core.Clipboard, System, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Drawing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/ZoomIt/ZoomIt/DemoType.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 886.4 | **LOC:** 1446 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.4248%), Tech Debt (9.5136%)
**Top Internal Functions/Classes:**
  * `DemoTypeHookProc` (Impact: 83.2)
    * *Intent:* //---------------------------------------------------------------------------- // // DemoTypeHookPro...
  * `InjectByClipboard` (Impact: 41.3)
    * *Intent:* //---------------------------------------------------------------------------- // // InjectByClipboa...
  * `StartDemoType` (Impact: 31.4)
    * *Intent:* //---------------------------------------------------------------------------- // // StartDemoType /...
  * `HandleControlKeyword` (Impact: 31.2)
    * *Intent:* //---------------------------------------------------------------------------- // // HandleControlKe...
  * `GetDemoTypeFile` (Impact: 30.9)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` DemoType.h, pch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/settings-ui/Settings.UI/ViewModels/AdvancedPasteViewModel.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 865.18 | **LOC:** 1485 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (31.3726%), Tech Debt (19.3683%)
**Top Internal Functions/Classes:**
  * `ShouldReplacePasteAIConfiguration` (Impact: 93.7)
  * `OnCustomActionsCollectionChanged` (Impact: 24.7)
  * `AdvancedPasteViewModel` (Impact: 23.0)
  * `MigrateLegacyAIEnablement` (Impact: 21.1)
  * `OnPasteAIProvidersCollectionChanged` (Impact: 20.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 98 instances
* *State Mutation (weighted view):* 319
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 242`, `structural_boundaries: 190`, `args: 113`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `state_mutation: 123`, `unreferenced_by_name: 13`
* *Architecture:* `api: 44`, `import: 19`
* *Defense:* `safety: 212`, `doc: 4`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.PowerToys.Settings.UI.Helpers, Microsoft.PowerToys.Settings.UI.Library, Microsoft.PowerToys.Settings.UI.Library.Helpers, Microsoft.PowerToys.Settings.UI.Library.Interfaces, Microsoft.PowerToys.Settings.UI.Library.Utilities, Microsoft.PowerToys.Settings.UI.SerializationContext, Microsoft.UI.Dispatching, Microsoft.Win32...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `installer/PowerToysSetupCustomActionsVNext/CustomAction.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 863.32 | **LOC:** 1829 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 25.0%
- **Risk Profile:** Cognitive Load (40.556%), Tech Debt (8.3193%)
**Top Internal Functions/Classes:**
  * `SetBundleInstallLocationCA` (Impact: 29.7)
  * `TerminateProcessesCA` (Impact: 25.6)
  * `RemoveScheduledTasksCA` (Impact: 24.0)
    * *Intent:* // Removes all Scheduled Tasks in the PowerToys folder and deletes the folder afterwards. // Based o...
  * `UninstallPackageIdentityMSIXCA` (Impact: 21.7)
  * `InstallPackageIdentityMSIXCA` (Impact: 21.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 397
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 147`, `args: 164`, `func_start: 42`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 2`, `state_mutation: 173`, `planned_debt: 2`
* *Architecture:* `io: 10`, `api: 36`, `import: 24`
* *Defense:* `safety: 30`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.155
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` EtwTrace.h, logger.h, installer.h, MsiUtils.h, clean_video_conference.h, gpo.h, modulesRegistry.h, package.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/ShortcutGuide/ShortcutGuide/overlay_window.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 858.24 | **LOC:** 948 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (92.2148%), Tech Debt (68.7229%)
**Top Internal Functions/Classes:**
  * `D2DOverlayWindow::render` (Impact: 122.4)
  * `D2DOverlayWindow::show` (Impact: 36.2)
  * `get_window_state` (Impact: 30.8)
  * `render_arrow` (Impact: 28.3)
  * `D2DOverlaySVG::get_thumbnail_rect_and_scale` (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 141 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 490
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 168`, `structural_boundaries: 93`, `args: 101`, `func_start: 32`
* *Risk/State:* `state_mutation: 208`, `unreferenced_by_name: 28`
* *Architecture:* `concurrency: 2`, `import: 11`
* *Defense:* `safety: 1`, `sync_locks: 12`, `immutability_locks: 12`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.156
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` resource.h, monitors.h, MsWindowsSettings.h, resources.h, window.h, overlay_window.h, pch.h, shortcut_guide.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/powerrename/lib/WICMetadataExtractor.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 850.62 | **LOC:** 1116 | **CtrlFlow:** 28.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (71.1203%), Tech Debt (45.036%)
**Top Internal Functions/Classes:**
  * `WICMetadataExtractor::ReadDouble` (Impact: 94.6)
  * `ParseIso8601DateTime` (Impact: 80.8)
  * `ValidateAndBuildSystemTime` (Impact: 49.5)
  * `WICMetadataExtractor::ExtractAllEXIFFields` (Impact: 43.2)
  * `WICMetadataExtractor::ReadDateTime` (Impact: 36.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 75 instances
* *State Mutation (weighted view):* 305
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 122`, `args: 35`, `func_start: 25`
* *Risk/State:* `state_mutation: 155`, `unreferenced_by_name: 20`
* *Architecture:* `concurrency: 2`, `import: 9`
* *Defense:* `safety: 9`, `sync_locks: 4`, `immutability_locks: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` MetadataFormatHelper.h, WICMetadataExtractor.h, algorithm, comdef.h, cwctype, iomanip, pch.h, shlwapi.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/Helpers.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 838.2 | **LOC:** 927 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (91.8198%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GetTransformedFileName` (Impact: 201.2)
  * `GetEnumeratedFileName` (Impact: 135.1)
  * `GetMetadataFileName` (Impact: 37.7)
  * `GetDatedFileName` (Impact: 26.1)
  * `isMetadataUsed` (Impact: 21.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 286
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 45`, `args: 58`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 120`
* *Architecture:* `io: 1`, `api: 15`, `import: 10`
* *Defense:* `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Helpers.h, MetadataTypes.h, ShlGuid.h, algorithm, cstring, filesystem, pch.h, regex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/Common.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 837.62 | **LOC:** 1655 | **CtrlFlow:** 12.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (42.0917%), Tech Debt (9.1544%)
**Top Internal Functions/Classes:**
  * `SkSend` (Impact: 34.9)
    * *Intent:* #endif
  * `ExecuteAndTrace` (Impact: 21.4)
  * `ShowToolTip` (Impact: 20.9)
  * `SendOrReceiveARandomDataBlockPerInitialIV` (Impact: 20.7)
  * `InvokeInFormThread` (Impact: 16.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 76 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 266
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 134`, `args: 113`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 114`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 13`, `api: 107`, `concurrency: 15`, `import: 21`
* *Defense:* `safety: 60`, `doc: 4`, `sync_locks: 22`, `immutability_locks: 10`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerToys.Settings.UI.Library, MouseWithoutBorders.Class, MouseWithoutBorders.Core.Clipboard, MouseWithoutBorders.Core.Thread, MouseWithoutBorders.Exceptions, System, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmScreen.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 781.18 | **LOC:** 1227 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (29.0482%)
**Top Internal Functions/Classes:**
  * `HelperTimer_Tick` (Impact: 113.4)
  * `WndProc` (Impact: 46.2)
    * *Intent:* // private bool checkClipboard = false;
  * `PaintMyNameOnDesktop` (Impact: 26.6)
  * `ShowMessageOnLogonDesktop` (Impact: 18.3)
  * `ChangeIcon` (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 105 instances
* *Concurrency (weighted view):* 14
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 24`, `args: 35`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 161`, `dead_code: 3`, `unreferenced_by_name: 15`
* *Architecture:* `io: 1`, `api: 20`, `concurrency: 4`, `import: 13`
* *Defense:* `safety: 25`, `immutability_locks: 5`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, MouseWithoutBorders.Core, MouseWithoutBorders.Properties, System, System.ComponentModel, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/registrypreview/RegistryPreviewUILib/RegistryPreviewMainPage.Utilities.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 764.38 | **LOC:** 1198 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0982%), Tech Debt (13.3923%)
**Top Internal Functions/Classes:**
  * `ParseRegistryFile` (Impact: 159.6)
    * *Intent:* /// <summary> /// Parses the text that is passed in, which should be the same text that's in editor ...
  * `AddTextToTree` (Impact: 37.8)
    * *Intent:* /// <summary> /// Helper method that creates a new TreeView node, attaches it to a parent if any, an...
  * `HandleDirtyClosing` (Impact: 27.6)
    * *Intent:* /// <summary> /// Wrapper method that shows a Save/Don't Save/Cancel message box, parented by the ma...
  * `SetValueToolTip` (Impact: 18.1)
    * *Intent:* /// <summary> /// Loads a string for a given Value's image in the grid, based off the current type a...
  * `GetFolderToolTip` (Impact: 12.2)
    * *Intent:* /// <summary> /// Loads and returns a string for a given Key's image in the tree, based off the curr...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 103 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 361
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 60`, `args: 27`, `func_start: 23`, `class_start: 1`
* *Risk/State:* `state_mutation: 155`, `dead_code: 9`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 5`, `concurrency: 14`, `import: 16`
* *Defense:* `safety: 27`, `doc: 73`, `immutability_locks: 3`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.UI.Input, Microsoft.UI.Xaml, Microsoft.UI.Xaml.Controls, System, System.Collections, System.Collections.Generic, System.Diagnostics, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Form/frmMatrix.Designer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 763.64 | **LOC:** 1208 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (51.3837%), Tech Debt (9.3272%)
**Top Internal Functions/Classes:**
  * `InitializeComponent` (Impact: 38.5)
    * *Intent:* #region Windows Form Designer generated code /// <summary> /// Required method for Designer support ...
  * `Dispose` (Impact: 3.2)
    * *Intent:* /// <summary> /// Clean up any resources being used. /// </summary> /// <param name="disposing">true...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 702
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 8`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 636`, `unreferenced_by_name: 2`
* *Architecture:* `import: 4`
* *Defense:* `safety: 9`, `doc: 11`, `sync_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Drawing, System.Windows.Forms, Windows.UI.Notifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/CursorWrapTests/monitor_layout_tests.py` (PYTHON | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 753.9 | **LOC:** 893 | **CtrlFlow:** 23.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.5019%), Tech Debt (12.8234%)
**Top Internal Functions/Classes:**
  * `_print_layout_diagram` (Impact: 63.2)
    * *Intent:* """Print a text-based diagram of the monitor layout"""
  * `_run_test_config` (Impact: 33.7)
  * `_is_outer_edge` (Impact: 17.4)
    * *Intent:* """ Determine if an edge is "outer" (can wrap) Rules: 1. If edge has an adjacent opposite edge (with...
  * `_get_test_points_on_edge` (Impact: 17.0)
  * `_wrap_from_edge` (Impact: 16.7)
    * *Intent:* """Calculate wrap destination from an outer edge"""
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 114 instances
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 104`, `args: 38`, `func_start: 36`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 2`, `state_mutation: 153`, `unreferenced_by_name: 3`
* *Architecture:* `io: 4`, `api: 22`, `import: 6`
* *Defense:* `safety: 3`, `doc: 37`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` argparse, dataclasses, enum, json, sys, typing
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/cmdpal/Microsoft.CmdPal.UI/ExtViews/ListPage.xaml.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 735.88 | **LOC:** 1231 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 53.3%
- **Risk Profile:** Cognitive Load (41.3464%), Tech Debt (22.9848%)
**Top Internal Functions/Classes:**
  * `TrySetSelectionAfterUpdate` (Impact: 57.1)
    * *Intent:* /// <summary> /// Applies selection after an items update. Returns false if ItemView.Items /// is no...
  * `HandleGridArrowNavigation` (Impact: 45.8)
    * *Intent:* // Find a logical neighbor in the requested direction using containers' positions.
  * `CalculateTargetIndexPageUpDownScrollTo` (Impact: 34.6)
    * *Intent:* /// <summary> /// Calculates the item index to target when performing a page up or page down /// nav...
  * `DelayRenderer` (Impact: 21.6)
  * `Items_PreviewKeyDown` (Impact: 20.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 86 instances
* *Amplified Sql Injection:* 2 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 271
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 199`, `structural_boundaries: 160`, `args: 67`, `func_start: 43`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 99`, `dead_code: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 13`, `concurrency: 1`, `import: 19`
* *Defense:* `safety: 97`, `doc: 30`, `sync_locks: 1`, `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` CommunityToolkit.Mvvm.Messaging, ManagedCommon, Microsoft.CmdPal.UI.Helpers, Microsoft.CmdPal.UI.Messages, Microsoft.CmdPal.UI.ViewModels, Microsoft.CmdPal.UI.ViewModels.Commands, Microsoft.CmdPal.UI.ViewModels.Messages, Microsoft.CmdPal.UI.ViewModels.Services...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseWithoutBorders/App/Core/MachineStuff.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 718.42 | **LOC:** 1123 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (55.7721%), Tech Debt (19.8915%)
**Top Internal Functions/Classes:**
  * `MoveRight` (Impact: 67.6)
    * *Intent:* #endif
  * `MoveLeft` (Impact: 60.8)
  * `MoveToMyNeighbourIfNeeded` (Impact: 60.6)
    * *Intent:* #if OLD_VERSION
  * `MoveToMyNeighbourIfNeeded` (Impact: 50.0)
    * *Intent:* /* Let's say we have 3 machines A, B, and C. A is the controller machine. * (x, y) is the current Mo...
  * `MoveUp` (Impact: 36.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 243
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 86`, `args: 39`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 87`, `dead_code: 3`, `unreferenced_by_name: 10`
* *Architecture:* `api: 38`, `import: 9`
* *Defense:* `safety: 3`, `sync_locks: 4`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.PowerToys.Telemetry, MouseWithoutBorders.Class, System, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Drawing, System.Linq, System.Threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/MouseUtils/CursorWrap/MonitorTopology.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 707.78 | **LOC:** 827 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (77.2762%), Tech Debt (56.4698%)
**Top Internal Functions/Classes:**
  * `MonitorTopology::IsOnOuterEdge` (Impact: 101.8)
  * `MonitorTopology::FindNearestOppositeEdge` (Impact: 64.0)
  * `MonitorTopology::GetWrapDestination` (Impact: 50.4)
  * `MonitorTopology::PrioritizeEdgeByDirection` (Impact: 48.4)
  * `MonitorTopology::FindOppositeOuterEdge` (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 77 instances
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 194`, `structural_boundaries: 65`, `args: 35`, `func_start: 17`
* *Risk/State:* `state_mutation: 111`, `unreferenced_by_name: 17`
* *Architecture:* `import: 6`
* *Defense:* `immutability_locks: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` logger.h, CursorWrapCore.h, MonitorTopology.h, algorithm, cmath, pch.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/cmdpal/extensionsdk/Microsoft.CommandPalette.Extensions.Toolkit/FuzzyStringMatcher.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 707.08 | **LOC:** 1095 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (42.968%), Tech Debt (9.7504%)
**Top Internal Functions/Classes:**
  * `ScoreNonContiguousWithPositions` (Impact: 59.3)
    * *Intent:* // ============================================================ // Non-contiguous matching (with pos...
  * `ScoreBestVariantWithPositions` (Impact: 37.6)
  * `ScoreNonContiguous` (Impact: 33.3)
    * *Intent:* // ============================================================ // Non-contiguous matching (score on...
  * `FoldForComparison` (Impact: 23.6)
    * *Intent:* /// <summary> /// Creates a folded string for fast equality comparisons: /// - ALWAYS normalizes sla...
  * `ScoreContiguous` (Impact: 20.4)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Buffers, System.Globalization, System.Runtime.CompilerServices, System.Text, ToolGood.Words.Pinyin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/powerrename/lib/PowerRenameManager.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 705.18 | **LOC:** 1207 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (47.8308%), Tech Debt (10.033%)
**Top Internal Functions/Classes:**
  * `CPowerRenameManager::s_fileOpWorkerThread` (Impact: 38.5)
  * `CPowerRenameManager::_WndProc` (Impact: 35.7)
  * `CPowerRenameManager::_PerformFileOperation` (Impact: 13.7)
  * `CPowerRenameManager::UpdateChildrenPath` (Impact: 12.2)
  * `CPowerRenameManager::SetVisible` (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 84`, `args: 56`, `func_start: 64`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 113`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 64`, `import: 9`
* *Defense:* `safety: 2`, `sync_locks: 20`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.168
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` PowerRenameManager.h, PowerRenameRegEx.h, Renaming.h, algorithm, cstring, helpers.h, pch.h, shlobj.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/modules/launcher/PowerLauncher/ViewModel/MainViewModel.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 677.44 | **LOC:** 1365 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8314%), Tech Debt (43.3433%)
**Top Internal Functions/Classes:**
  * `QueryResults` (Impact: 41.2)
  * `SetHotkey` (Impact: 21.2)
  * `OpenResultsEvent` (Impact: 20.3)
  * `RegisterHotkey` (Impact: 16.8)
  * `UpdateResultsListViewAfterQuery` (Impact: 13.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 77 instances
* *Amplified Sql Injection:* 4 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 141`, `args: 88`, `func_start: 60`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 124`, `planned_debt: 2`, `unreferenced_by_name: 15`
* *Architecture:* `api: 63`, `concurrency: 10`, `import: 28`
* *Defense:* `safety: 39`, `doc: 14`, `sync_locks: 7`, `immutability_locks: 9`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Common.UI, Mages.Core.Runtime.Converters, Microsoft.PowerLauncher.Telemetry, Microsoft.PowerToys.Telemetry, PowerLauncher.Helper, PowerLauncher.Plugin, PowerLauncher.Storage, PowerToys.Interop...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/KeyboardManagerEditorLibraryWrapper/KeyboardManagerEditorLibraryWrapper.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 675.78 | **LOC:** 752 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (92.9143%), Tech Debt (83.0129%)
**Top Internal Functions/Classes:**
  * `GetShortcutRemapByType` (Impact: 138.4)
  * `GetShortcutRemapCountByType` (Impact: 67.2)
  * `AddShortcutRemap` (Impact: 55.0)
  * `GetShortcutRemap` (Impact: 34.4)
  * `DeleteShortcutRemap` (Impact: 20.4)
    * *Intent:* // Function to delete a shortcut remapping
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 73 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 156`, `structural_boundaries: 99`, `args: 73`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 104`, `unreferenced_by_name: 25`
* *Architecture:* `import: 11`
* *Defense:* `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` KeyboardManagerEditorLibraryWrapper.h, algorithm, keyboard_layout.h, logger_helper.h, cstring, KeyboardManagerEditor.h, EditorHelpers.h, memory...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/modules/keyboardmanager/common/Shortcut.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 666.1 | **LOC:** 945 | **CtrlFlow:** 35.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4643%), Tech Debt (78.8879%)
**Top Internal Functions/Classes:**
  * `Shortcut::IsKeyboardStateClearExceptShortcut` (Impact: 105.0)
    * *Intent:* // Function to check if any keys are pressed down except those in the shortcut
  * `Shortcut::SetKey` (Impact: 59.2)
    * *Intent:* // Function to set a key in the shortcut based on the passed key code argument. Returns false if it ...
  * `Shortcut::CheckModifiersKeyboardState` (Impact: 52.9)
    * *Intent:* // Function to check if all the modifiers in the shortcut have been pressed down
  * `IgnoreKeyCode` (Impact: 42.9)
    * *Intent:* // Function to check if the key code is to be ignored
  * `Shortcut::ResetKey` (Impact: 23.8)
    * *Intent:* // Function to reset the state of a shortcut key based on the passed key code argument. Since there ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 113`, `args: 80`, `func_start: 38`
* *Risk/State:* `state_mutation: 56`, `dead_code: 1`, `unreferenced_by_name: 31`
* *Architecture:* `import: 8`
* *Defense:* `immutability_locks: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.142
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Helpers.h, InputInterface.h, Shortcut.h, keyboard_layout.h, shared_constants.h, pch.h, sstream, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/Commands/MainListPage.cs` -> Churn: **100.0%** | Cog Load: 85.3683% | Debt: 14.7876%
- `src/modules/ZoomIt/ZoomIt/Zoomit.cpp` -> Churn: **84.12%** | Cog Load: 89.0414% | Debt: 8.317%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/CommandProviderWrapper.cs` -> Churn: **77.82%** | Cog Load: 68.8431% | Debt: 44.5321%
- `src/modules/cmdpal/Microsoft.CmdPal.UI/Controls/SearchBar.xaml.cs` -> Churn: **73.22%** | Cog Load: 50.2134% | Debt: 91.0306%
- `src/modules/cmdpal/Microsoft.CmdPal.UI.ViewModels/ListViewModel.cs` -> Churn: **72.76%** | Cog Load: 50.3296% | Debt: 40.6353%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/modules/MouseUtils/CursorWrap/CursorWrapTests/WrapSimulator/wrap_simulator.py` -> **Niels Laute** (100.0% isolated ownership) | Magnitude: 2235.8
- `src/modules/MouseWithoutBorders/App/Class/SocketStuff.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 1340.28
- `src/modules/MouseWithoutBorders/App/Form/frmMatrix.cs` -> **Michael Clayton** (100.0% isolated ownership) | Magnitude: 952.34
- `src/modules/ZoomIt/ZoomIt/DemoType.cpp` -> **Mario Hewardt** (100.0% isolated ownership) | Magnitude: 886.4
- `src/modules/powerrename/lib/WICMetadataExtractor.cpp` -> **moooyo** (100.0% isolated ownership) | Magnitude: 850.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/modules/keyboardmanager/common/Input.h` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 13.7083%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/modules/keyboardmanager/common/Input.h` -> **Severity: 1422.9** (Blast Radius: 14.229 * Doc Risk: 100.0%)
- `src/common/logger/logger.h` -> **Severity: 939.6** (Blast Radius: 9.396 * Doc Risk: 100.0%)
- `src/common/utils/json.h` -> **Severity: 878.8** (Blast Radius: 8.788 * Doc Risk: 100.0%)
- `src/common/Telemetry/TraceBase.h` -> **Severity: 684.07** (Blast Radius: 7.847 * Doc Risk: 87.176%)
- `src/common/utils/winapi_error.h` -> **Severity: 556.1** (Blast Radius: 5.561 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
