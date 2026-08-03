# ARCHITECTURAL_BRIEF: PowerShell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/PowerShell` |
| **Timestamp** | `2026-08-03T19:23:15.347871+00:00` |
| **Scan Duration** | `9.94s` |
| **Git Branch** | `master` |
| **Git Commit** | `a17f1761eca57d90856062e35add0f013a1c703f` |
| **Git Remote** | `https://github.com/PowerShell/PowerShell` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 1374 malicious artifacts.

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
| Total Artifacts | 2674 |
| Analyzed Artifacts (Scanned) | 1492 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1182 |
| Total LOC | 363565 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 55.8% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.725 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2132 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.4197 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 20 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1279 | 341966 | 85.7% |
| POWERSHELL | 80 | 13582 | 5.4% |
| XML | 55 | 0 | 3.7% |
| MARKDOWN | 34 | 0 | 2.3% |
| JSON | 23 | 6665 | 1.5% |
| SHELL | 13 | 1245 | 0.9% |
| PLAINTEXT | 4 | 0 | 0.3% |
| YAML | 2 | 19 | 0.1% |
| BATCH | 1 | 1 | 0.1% |
| DOCKERFILE | 1 | 87 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.793`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 743 | 49.8% |
| file_cluster_13 | 433 | 29.0% |
| file_cluster_0 | 133 | 8.9% |
| file_cluster_7 | 53 | 3.6% |
| file_cluster_16 | 50 | 3.4% |
| file_cluster_1 | 11 | 0.7% |
| file_cluster_11 | 8 | 0.5% |
| file_cluster_15 | 7 | 0.5% |
| file_cluster_4 | 5 | 0.3% |
| file_cluster_12 | 4 | 0.3% |
| file_cluster_2 | 3 | 0.2% |
| file_cluster_6 | 2 | 0.1% |
| file_cluster_9 | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1182*

**Composition by Extension & Reason:**
- `.ps1`: 447x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.resx`: 166x Unsupported Format (.resx)
- `.yml`: 108x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cs`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 1372 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2159 LOC)
- `.md`: 65x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 61x Excluded (Explicitly Denied Extension: '.png'), 2x Excluded (Explicitly Denied Extension: '.PNG')
- `.csproj`: 33x Unsupported Format (.csproj), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4630 LOC)
- `.psd1`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.xaml`: 16x Unsupported Format (.xaml)
- `.yaml`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.psm1`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cab`: 12x Excluded (Explicitly Denied Extension: '.cab')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 16.5 | 11.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 43.5 | 50.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 49.5 | 44.4 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 46.5 | 80.0 | 80.0 |
| API Exposure | 0.0 | 17.8 | 4.3 | 4.1 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 63.2 | 90.3 | 0.0 |
| Commented Logic Exposure | 0.0 | 96.4 | 2.9 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 5.8 | 0.9 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 37.2 | 14.3 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 79.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 69.2 | 100.0 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 41.4 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tools/installpsh-debian.sh` (Hits: 55)
- `src/System.Management.Automation/DscSupport/CimDSCParser.cs` (Hits: 55)
- `tools/install-powershell.sh` (Hits: 50)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Xml.psm1** (`tools/Xml/Xml.psm1`) — 68 inbound connections
2. **Serialization.cs** (`src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs`) — 64 inbound connections
3. **Tracing.cs** (`src/System.Management.Automation/utils/tracing/Tracing.cs`) — 41 inbound connections
4. **Format.xsd** (`src/Schemas/Format.xsd`) — 35 inbound connections
5. **Extensions.cs** (`src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Extensions.cs`) — 27 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ConsoleHost.cs** (`src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHost.cs`) — 29 outbound dependencies
2. **serialization.cs** (`src/System.Management.Automation/engine/serialization.cs`) — 26 outbound dependencies
3. **CompletionCompleters.cs** (`src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) — 25 outbound dependencies
4. **LanguagePrimitives.cs** (`src/System.Management.Automation/engine/LanguagePrimitives.cs`) — 24 outbound dependencies
5. **ImportModuleCommand.cs** (`src/System.Management.Automation/engine/Modules/ImportModuleCommand.cs`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `New-UnixPackage` (@ `tools/packaging/packaging.psm1`) -> Impact: **3690.5** | LOC: 1496
- `CompleteCommandArgument` (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> Impact: **2923.4** | LOC: 1198
- `BindParameter` (@ `src/System.Management.Automation/engine/ParameterBinderBase.cs`) -> Impact: **2806.9** | LOC: 1258
  * *Intent:* /// protected BindParameter method. /// </remarks> /// <exception cref="ArgumentNullException"> /// If <paramref name="parameter"/> or <paramref name=...
- `GetValue` (@ `src/System.Management.Automation/engine/InternalCommands.cs`) -> Impact: **2664.3** | LOC: 1637
- `NativeCompletionCimCommands` (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> Impact: **2580.3** | LOC: 1206
- `EscapeCharIfNeeded` (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> Impact: **2455.1** | LOC: 1189
- `ConstructTransportErrorEventArgs` (@ `src/System.Management.Automation/engine/remoting/fanin/WSManTransportManager.cs`) -> Impact: **2327.3** | LOC: 1356
  * *Intent:* /// <param name="wsmanSessionTM"> /// Session Transportmanager to use to get error messages (for redirect) /// </param> /// <param name="errorStruct">...
- `GetHelpInfo` (@ `src/System.Management.Automation/help/CommandHelpProvider.cs`) -> Impact: **2079.8** | LOC: 787
- `IsValidPath` (@ `src/System.Management.Automation/namespaces/FileSystemProvider.cs`) -> Impact: **2009.5** | LOC: 1440
- `MoveNext` (@ `src/System.Management.Automation/engine/CommandSearcher.cs`) -> Impact: **1754.2** | LOC: 644
  * *Intent:* /// <summary> /// Moves the enumerator to the next command match. Public for IEnumerable. /// </summary> /// <returns> /// true if there was another c...

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Start-HTTPListener` (@ `test/tools/Modules/HttpListener/HttpListener.psm1`) -> **O(2^N) [Recursive]**
- `Find-LastHarvestedVersion` (@ `tools/clearlyDefined/Find-LastHarvestedVersion.ps1`) -> **O(2^N) [Recursive]**
- `Start-PSPackage` (@ `tools/packaging/packaging.psm1`) -> **O(2^N) [Recursive]**
- `GetBaseObject` (@ `src/Microsoft.Management.Infrastructure.CimCmdlets/CimAsyncOperation.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Retrieve the base object out if wrapped in psobject. /// </summary> /// <param name="value"></param> /// <returns></returns>
- `WriteObject` (@ `src/Microsoft.Management.Infrastructure.CimCmdlets/CmdletOperation.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// <para> /// Object here need to be removed if it is CimInstance /// </para> /// </summary> /// <param name="sendToPipeline"></param>
- `ValidateArgumentIsValidName` (@ `src/Microsoft.Management.Infrastructure.CimCmdlets/Utils.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Validate given arry argument contains all valid name (for -SelectProperties). /// * is valid for this case. /// </summary> /// <para...
- `OnClosed` (@ `src/Microsoft.Management.UI.Internal/ManagementList/Common/DismissiblePopup.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Responds when the value of the IsOpen property changes from to true to false. /// </summary> /// <param name="e">The event arguments...
- `OnOpened` (@ `src/Microsoft.Management.UI.Internal/ManagementList/Common/DismissiblePopup.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Responds to the condition in which the value of the IsOpen property changes from false to true. /// </summary> /// <param name="e">T...
- `OnPreviewMouseLeftButtonUp` (@ `src/Microsoft.Management.UI.Internal/ManagementList/Common/PopupControlButton.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Invoked when an unhandled PreviewMouseLeftButtonUp routed event reaches an element in its route that is derived from this class. Imp...
- `Evaluate` (@ `src/Microsoft.Management.UI.Internal/ManagementList/FilterCore/FilterRules/PropertiesTextContainsFilterRule.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// <summary> /// Evaluates whether the specified properties on <paramref name="item"/> contain the current value. /// </summary> /// <param name="ite...

### Highest Data Gravity (Database Complexity)
- `install` (@ `tools/install-powershell.sh`) -> DB Complexity: **252**
  * *Intent:* #!/bin/bash # Copyright (c) Microsoft Corporation. # Licensed under the MIT License.
- `InitIDs` (@ `src/System.Management.Automation/cimSupport/cmdletization/xml/CoreCLR/cmdlets-over-objects.xmlSerializer.autogen.cs`) -> DB Complexity: **244**
- `New-UnixPackage` (@ `tools/packaging/packaging.psm1`) -> DB Complexity: **238**
- `Read_MemberSet` (@ `src/System.Management.Automation/engine/TypeTable.cs`) -> DB Complexity: **203**
- `GetMessage` (@ `src/System.Management.Automation/CoreCLR/EventResource.cs`) -> DB Complexity: **192**
  * *Intent:* /// <summary> /// Gets the message resource id for the specified event id.
- `Process_Types_Ps1Xml` (@ `src/System.Management.Automation/engine/TypeTable_Types_Ps1Xml.cs`) -> DB Complexity: **185**
- `LoadResourcesFromModule` (@ `src/System.Management.Automation/DscSupport/CimDSCParser.cs`) -> DB Complexity: **163**
- `IsValidPath` (@ `src/System.Management.Automation/namespaces/FileSystemProvider.cs`) -> DB Complexity: **130**
- `GetValue` (@ `src/System.Management.Automation/engine/InternalCommands.cs`) -> DB Complexity: **129**
- `NativeCompletionCimCommands` (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> DB Complexity: **126**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/System.Management.Automation/engine` | 146 | 82894.3 | 15.98% | 67.3% |
| `src/Microsoft.PowerShell.Commands.Utility/commands/utility` | 89 | 25957.12 | 14.64% | 38.0% |
| `src/System.Management.Automation/engine/parser` | 18 | 24740.46 | 25.99% | 76.51% |
| `src/Microsoft.PowerShell.Commands.Management/commands/management` | 52 | 21494.48 | 14.21% | 40.62% |
| `src/System.Management.Automation/engine/remoting/commands` | 28 | 19589.8 | 17.06% | 38.89% |
| `src/System.Management.Automation/namespaces` | 33 | 19373.24 | 11.68% | 48.39% |
| `src/System.Management.Automation/engine/interpreter` | 38 | 19013.44 | 30.64% | 81.94% |
| `src/System.Management.Automation/engine/hostifaces` | 33 | 18072.4 | 14.9% | 82.38% |
| `src/System.Management.Automation/help` | 43 | 15768.56 | 16.09% | 54.37% |
| `src/System.Management.Automation/engine/CommandCompletion` | 8 | 13669.38 | 24.12% | 66.59% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `docker/InstallTarballPackage.sh` -> **100.0%** Exposure
- `tools/debug.sh` -> **100.0%** Exposure
- `tools/download.sh` -> **100.0%** Exposure
- `tools/generate-icns.sh` -> **100.0%** Exposure
- `tools/installpsh-osx.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/skills/analyze-pester-failures/scripts/analyze-pr-test-failures.ps1` -> **100.0%** Exposure
- `dsc/pwsh.profile.resource.ps1` -> **100.0%** Exposure
- `src/PowerShell.Core.Instrumentation/RegisterManifest.ps1` -> **100.0%** Exposure
- `tools/AttackSurfaceAnalyzer/Summarize-AsaResults.ps1` -> **100.0%** Exposure
- `tools/UpdateDotnetRuntime.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/System.Management.Automation/engine/parser/AstVisitor.cs` -> **3** Orphaned Functions | **240** Duplicates
- `src/System.Management.Automation/engine/parser/ast.cs` -> **12** Orphaned Functions | **121** Duplicates
- `src/System.Management.Automation/engine/interpreter/CallInstruction.Generated.cs` -> **2** Orphaned Functions | **116** Duplicates
- `src/System.Management.Automation/engine/InitialSessionState.cs` -> **43** Orphaned Functions | **56** Duplicates
- `src/System.Management.Automation/engine/runtime/Operations/NumericOps.cs` -> **14** Orphaned Functions | **84** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Microsoft.PowerShell.Commands.Management/commands/management/Eventlog.cs`** -> AI Confidence: **99.48%**
2. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/CsvCommands.cs`** -> AI Confidence: **99.48%**
3. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/DebugRunspaceCommand.cs`** -> AI Confidence: **99.48%**
4. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Select-Object.cs`** -> AI Confidence: **99.48%**
5. **`src/Microsoft.WSMan.Management/ConfigProvider.cs`** -> AI Confidence: **99.48%**
6. **`src/System.Management.Automation/FormatAndOutput/common/TableWriter.cs`** -> AI Confidence: **99.48%**
7. **`src/System.Management.Automation/cimSupport/cmdletization/ScriptWriter.cs`** -> AI Confidence: **99.48%**
8. **`src/System.Management.Automation/engine/ParameterBinderBase.cs`** -> AI Confidence: **99.48%**
9. **`src/System.Management.Automation/engine/SessionStateContainer.cs`** -> AI Confidence: **99.48%**
10. **`src/System.Management.Automation/engine/SessionStateDriveAPIs.cs`** -> AI Confidence: **99.48%**
11. **`src/System.Management.Automation/engine/remoting/commands/CustomShellCommands.cs`** -> AI Confidence: **99.48%**
12. **`src/System.Management.Automation/engine/remoting/commands/InvokeCommandCommand.cs`** -> AI Confidence: **99.48%**
13. **`src/Microsoft.PowerShell.Commands.Diagnostics/GetEventCommand.cs`** -> AI Confidence: **99.39%**
14. **`src/Microsoft.PowerShell.Commands.Management/commands/management/Computer.cs`** -> AI Confidence: **99.39%**
15. **`src/Microsoft.PowerShell.Commands.Management/commands/management/WMIHelper.cs`** -> AI Confidence: **99.39%**
16. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/FormatAndOutput/OutGridView/TableView.cs`** -> AI Confidence: **99.39%**
17. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/GetRandomCommandBase.cs`** -> AI Confidence: **99.39%**
18. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Set-PSBreakpoint.cs`** -> AI Confidence: **99.39%**
19. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Update-TypeData.cs`** -> AI Confidence: **99.39%**
20. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/Common/BasicHtmlWebResponseObject.Common.cs`** -> AI Confidence: **99.39%**
21. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/XmlCommands.cs`** -> AI Confidence: **99.39%**
22. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/trace/TraceListenerCommandBase.cs`** -> AI Confidence: **99.39%**
23. **`src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHost.cs`** -> AI Confidence: **99.39%**
24. **`src/Microsoft.PowerShell.Security/security/CertificateProvider.cs`** -> AI Confidence: **99.39%**
25. **`src/Microsoft.PowerShell.Security/security/CmsCommands.cs`** -> AI Confidence: **99.39%**
26. **`src/System.Management.Automation/FormatAndOutput/common/ComplexWriter.cs`** -> AI Confidence: **99.39%**
27. **`src/System.Management.Automation/FormatAndOutput/common/ListWriter.cs`** -> AI Confidence: **99.39%**
28. **`src/System.Management.Automation/engine/CmdletParameterBinderController.cs`** -> AI Confidence: **99.39%**
29. **`src/System.Management.Automation/engine/CommandCompletion/PseudoParameterBinder.cs`** -> AI Confidence: **99.39%**
30. **`src/System.Management.Automation/engine/CommandDiscovery.cs`** -> AI Confidence: **99.39%**
31. **`src/System.Management.Automation/engine/CommandSearcher.cs`** -> AI Confidence: **99.39%**
32. **`src/System.Management.Automation/engine/GetCommandCommand.cs`** -> AI Confidence: **99.39%**
33. **`src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs`** -> AI Confidence: **99.39%**
34. **`src/System.Management.Automation/engine/NativeCommandParameterBinder.cs`** -> AI Confidence: **99.39%**
35. **`src/System.Management.Automation/engine/hostifaces/Connection.cs`** -> AI Confidence: **99.39%**
36. **`src/System.Management.Automation/engine/hostifaces/LocalPipeline.cs`** -> AI Confidence: **99.39%**
37. **`src/System.Management.Automation/engine/hostifaces/PowerShell.cs`** -> AI Confidence: **99.39%**
38. **`src/System.Management.Automation/engine/interpreter/LightCompiler.cs`** -> AI Confidence: **99.39%**
39. **`src/System.Management.Automation/engine/parser/DebugViewWriter.cs`** -> AI Confidence: **99.39%**
40. **`src/System.Management.Automation/engine/parser/tokenizer.cs`** -> AI Confidence: **99.39%**
41. **`src/System.Management.Automation/engine/remoting/client/RemoteRunspacePoolInternal.cs`** -> AI Confidence: **99.39%**
42. **`src/System.Management.Automation/engine/remoting/commands/PSRemotingCmdlet.cs`** -> AI Confidence: **99.39%**
43. **`src/System.Management.Automation/engine/remoting/commands/PushRunspaceCommand.cs`** -> AI Confidence: **99.39%**
44. **`src/System.Management.Automation/engine/remoting/commands/RemoveJob.cs`** -> AI Confidence: **99.39%**
45. **`src/System.Management.Automation/engine/remoting/commands/WaitJob.cs`** -> AI Confidence: **99.39%**
46. **`src/System.Management.Automation/engine/remoting/commands/newrunspacecommand.cs`** -> AI Confidence: **99.39%**
47. **`src/System.Management.Automation/engine/remoting/commands/removerunspacecommand.cs`** -> AI Confidence: **99.39%**
48. **`src/System.Management.Automation/engine/remoting/common/RemoteSessionHyperVSocket.cs`** -> AI Confidence: **99.39%**
49. **`src/System.Management.Automation/engine/remoting/fanin/InitialSessionStateProvider.cs`** -> AI Confidence: **99.39%**
50. **`src/System.Management.Automation/help/UpdatableHelpSystem.cs`** -> AI Confidence: **99.39%**
51. **`src/System.Management.Automation/help/UpdateHelpCommand.cs`** -> AI Confidence: **99.39%**
52. **`src/System.Management.Automation/namespaces/FileSystemProvider.cs`** -> AI Confidence: **99.39%**
53. **`src/System.Management.Automation/namespaces/RegistryProvider.cs`** -> AI Confidence: **99.39%**
54. **`src/System.Management.Automation/namespaces/TransactedRegistryKey.cs`** -> AI Confidence: **99.39%**
55. **`src/System.Management.Automation/security/CatalogHelper.cs`** -> AI Confidence: **99.39%**
56. **`src/System.Management.Automation/security/SecurityManager.cs`** -> AI Confidence: **99.39%**
57. **`test/tools/TestExe/TestExe.cs`** -> AI Confidence: **99.39%**
58. **`src/Microsoft.PowerShell.Commands.Diagnostics/GetCounterCommand.cs`** -> AI Confidence: **99.35%**
59. **`src/System.Management.Automation/engine/TypeTable.cs`** -> AI Confidence: **99.35%**
60. **`src/System.Management.Automation/engine/parser/Parser.cs`** -> AI Confidence: **99.35%**
61. **`src/System.Management.Automation/engine/remoting/fanin/WSManTransportManager.cs`** -> AI Confidence: **99.35%**
62. **`tools/findMissingNotices.ps1`** -> AI Confidence: **99.34%**
63. **`src/Microsoft.Management.Infrastructure.CimCmdlets/CimInvokeCimMethod.cs`** -> AI Confidence: **99.34%**
64. **`src/Microsoft.Management.Infrastructure.CimCmdlets/CimSessionOperations.cs`** -> AI Confidence: **99.34%**
65. **`src/Microsoft.PowerShell.Commands.Management/commands/management/GetWMIObjectCommand.cs`** -> AI Confidence: **99.34%**
66. **`src/Microsoft.PowerShell.Commands.Management/commands/management/Hotfix.cs`** -> AI Confidence: **99.34%**
67. **`src/Microsoft.PowerShell.Commands.Management/commands/management/ParsePathCommand.cs`** -> AI Confidence: **99.34%**
68. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/CustomSerialization.cs`** -> AI Confidence: **99.34%**
69. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/GetDateCommand.cs`** -> AI Confidence: **99.34%**
70. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Send-MailMessage.cs`** -> AI Confidence: **99.34%**
71. **`src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs`** -> AI Confidence: **99.34%**
72. **`src/System.Management.Automation/cimSupport/cmdletization/xml/CoreCLR/cmdlets-over-objects.xmlSerializer.autogen.cs`** -> AI Confidence: **99.34%**
73. **`src/System.Management.Automation/engine/SessionStateProviderAPIs.cs`** -> AI Confidence: **99.34%**
74. **`src/System.Management.Automation/engine/remoting/client/JobManager.cs`** -> AI Confidence: **99.34%**
75. **`src/System.Management.Automation/engine/remoting/client/remotingprotocolimplementation.cs`** -> AI Confidence: **99.34%**
76. **`src/System.Management.Automation/engine/remoting/commands/SuspendJob.cs`** -> AI Confidence: **99.34%**
77. **`src/System.Management.Automation/engine/remoting/server/ServerSteppablePipelineDriver.cs`** -> AI Confidence: **99.34%**
78. **`src/System.Management.Automation/namespaces/LocationGlobber.cs`** -> AI Confidence: **99.34%**
79. **`tools/ci.psm1`** -> AI Confidence: **99.32%**
80. **`tools/packaging/packaging.psm1`** -> AI Confidence: **99.32%**
81. **`src/Microsoft.PowerShell.Commands.Management/commands/management/CombinePathCommand.cs`** -> AI Confidence: **99.32%**
82. **`src/System.Management.Automation/engine/SessionStateDynamicProperty.cs`** -> AI Confidence: **99.32%**
83. **`src/System.Management.Automation/engine/remoting/client/clientremotesessionprotocolstatemachine.cs`** -> AI Confidence: **99.32%**
84. **`src/Microsoft.Management.Infrastructure.CimCmdlets/CimCommandBase.cs`** -> AI Confidence: **99.31%**
85. **`src/Microsoft.Management.Infrastructure.CimCmdlets/CimSessionProxy.cs`** -> AI Confidence: **99.31%**
86. **`src/Microsoft.Management.UI.Internal/ManagementList/Common/DismissiblePopup.cs`** -> AI Confidence: **99.31%**
87. **`src/Microsoft.Management.UI.Internal/ManagementList/Common/ListOrganizerItem.cs`** -> AI Confidence: **99.31%**
88. **`src/Microsoft.Management.UI.Internal/ManagementList/CommonControls/Resizer.cs`** -> AI Confidence: **99.31%**
89. **`src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/InnerListGridView.cs`** -> AI Confidence: **99.31%**
90. **`src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/Innerlist.cs`** -> AI Confidence: **99.31%**
91. **`src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/ManagementListStateDescriptor.cs`** -> AI Confidence: **99.31%**
92. **`src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/managementlist.cs`** -> AI Confidence: **99.31%**
93. **`src/Microsoft.Management.UI.Internal/ShowCommand/Controls/ParameterSetControl.xaml.cs`** -> AI Confidence: **99.31%**
94. **`src/Microsoft.Management.UI.Internal/ShowCommand/ViewModel/ModuleViewModel.cs`** -> AI Confidence: **99.31%**
95. **`src/Microsoft.Management.UI.Internal/ShowCommand/ViewModel/ParameterSetViewModel.cs`** -> AI Confidence: **99.31%**
96. **`src/Microsoft.Management.UI.Internal/commandHelpers/OutGridView.cs`** -> AI Confidence: **99.31%**
97. **`src/Microsoft.PowerShell.Commands.Diagnostics/ExportCounterCommand.cs`** -> AI Confidence: **99.31%**
98. **`src/Microsoft.PowerShell.Commands.Diagnostics/ImportCounterCommand.cs`** -> AI Confidence: **99.31%**
99. **`src/Microsoft.PowerShell.Commands.Diagnostics/NewWinEventCommand.cs`** -> AI Confidence: **99.31%**
100. **`src/Microsoft.PowerShell.Commands.Diagnostics/PdhHelper.cs`** -> AI Confidence: **99.31%**
101. **`src/Microsoft.PowerShell.Commands.Management/cimSupport/cmdletization/SessionBasedWrapper.cs`** -> AI Confidence: **99.31%**
102. **`src/Microsoft.PowerShell.Commands.Management/cimSupport/cmdletization/cim/ExtrinsicMethodInvocationJob.cs`** -> AI Confidence: **99.31%**
103. **`src/Microsoft.PowerShell.Commands.Management/cimSupport/cmdletization/cim/cimChildJobBase.cs`** -> AI Confidence: **99.31%**
104. **`src/Microsoft.PowerShell.Commands.Management/commands/management/ClearRecycleBinCommand.cs`** -> AI Confidence: **99.31%**
105. **`src/Microsoft.PowerShell.Commands.Management/commands/management/ControlPanelItemCommand.cs`** -> AI Confidence: **99.31%**
106. **`src/Microsoft.PowerShell.Commands.Management/commands/management/GetComputerInfoCommand.cs`** -> AI Confidence: **99.31%**
107. **`src/Microsoft.PowerShell.Commands.Management/commands/management/GetContentCommand.cs`** -> AI Confidence: **99.31%**
108. **`src/Microsoft.PowerShell.Commands.Management/commands/management/InvokeWMIMethodCommand.cs`** -> AI Confidence: **99.31%**
109. **`src/Microsoft.PowerShell.Commands.Management/commands/management/Process.cs`** -> AI Confidence: **99.31%**
110. **`src/Microsoft.PowerShell.Commands.Management/commands/management/Service.cs`** -> AI Confidence: **99.31%**
111. **`src/Microsoft.PowerShell.Commands.Management/commands/management/SetWMIInstanceCommand.cs`** -> AI Confidence: **99.31%**
112. **`src/Microsoft.PowerShell.Commands.Management/commands/management/TestConnectionCommand.cs`** -> AI Confidence: **99.31%**
113. **`src/Microsoft.PowerShell.Commands.Management/commands/management/TimeZoneCommands.cs`** -> AI Confidence: **99.31%**
114. **`src/Microsoft.PowerShell.Commands.Management/commands/management/WebServiceProxy.cs`** -> AI Confidence: **99.31%**
115. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/AddMember.cs`** -> AI Confidence: **99.31%**
116. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ConvertFromMarkdownCommand.cs`** -> AI Confidence: **99.31%**
117. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ConvertTo-Html.cs`** -> AI Confidence: **99.31%**
118. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/EnableDisableRunspaceDebugCommand.cs`** -> AI Confidence: **99.31%**
119. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/FormatAndOutput/OutGridView/OutGridViewCommand.cs`** -> AI Confidence: **99.31%**
120. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/FormatAndOutput/common/GetFormatDataCommand.cs`** -> AI Confidence: **99.31%**
121. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/FormatAndOutput/format-hex/Format-Hex.cs`** -> AI Confidence: **99.31%**
122. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/GetHash.cs`** -> AI Confidence: **99.31%**
123. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Group-Object.cs`** -> AI Confidence: **99.31%**
124. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ImplicitRemotingCommands.cs`** -> AI Confidence: **99.31%**
125. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/Import-LocalizedData.cs`** -> AI Confidence: **99.31%**
126. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/MatchString.cs`** -> AI Confidence: **99.31%**
127. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/New-Object.cs`** -> AI Confidence: **99.31%**
128. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/OrderObjectBase.cs`** -> AI Confidence: **99.31%**
129. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ReadConsoleCmdlet.cs`** -> AI Confidence: **99.31%**
130. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ShowCommand/ShowCommand.cs`** -> AI Confidence: **99.31%**
131. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/ShowMarkdownCommand.cs`** -> AI Confidence: **99.31%**
132. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/TestJsonCommand.cs`** -> AI Confidence: **99.31%**
133. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/UnblockFile.cs`** -> AI Confidence: **99.31%**
134. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/Common/ContentHelper.Common.cs`** -> AI Confidence: **99.31%**
135. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/Common/InvokeRestMethodCommand.Common.cs`** -> AI Confidence: **99.31%**
136. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/Common/WebRequestPSCmdlet.Common.cs`** -> AI Confidence: **99.31%**
137. **`src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/Common/WebResponseObject.Common.cs`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/System.Management.Automation/cimSupport/cmdletization/xml/CoreCLR/cmdlets-over-objects.xmlSerializer.autogen.cs` -> **99.968%** Exposure
- `src/Microsoft.WSMan.Management/WsManHelper.cs` -> **0.0147%** Exposure
- `src/System.Management.Automation/engine/remoting/client/remoterunspace.cs` -> **0.001%** Exposure
- `src/System.Management.Automation/utils/VTUtils.cs` -> **0.0001%** Exposure
### Exploit Generation Surface
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimAsyncOperation.cs` -> **100.0%** Exposure
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimCommandBase.cs` -> **100.0%** Exposure
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimGetAssociatedInstance.cs` -> **100.0%** Exposure
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimGetCimClass.cs` -> **100.0%** Exposure
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimGetInstance.cs` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `test/tools/Modules/HttpListener/HttpListener.psm1` -> **100.0%** Exposure
- `tools/debug.sh` -> **100.0%** Exposure
- `tools/installpsh-amazonlinux.sh` -> **100.0%** Exposure
- `tools/installpsh-debian.sh` -> **100.0%** Exposure
- `tools/installpsh-gentoo.sh` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `src/System.Management.Automation/security/SecuritySupport.cs` -> **41.3994%** Exposure
### Algorithmic DoS Exposure
- `dsc/pwsh.profile.resource.ps1` -> **100.0%** Exposure
- `src/Modules/Windows/PSDiagnostics/PSDiagnostics.psm1` -> **100.0%** Exposure
- `src/powershell-native/Install-PowerShellRemoting.ps1` -> **100.0%** Exposure
- `test/tools/CodeCoverageAutomation/Start-CodeCoverageRun.ps1` -> **100.0%** Exposure
- `test/tools/Modules/HelpersCommon/HelpersCommon.psm1` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `12` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6856` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/System.Management.Automation/utils/PSTelemetryMethods.cs` (CSHARP) -> Cumulative Risk: **914.6**
- **Archetype:** `file_cluster_13` (Distance: 12.386 IQR)
- **Magnitude:** 372.12 | **LOC:** 535 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ReportTabCompletionTelemetry` (Impact: 66.2), `ReportStartupTelemetry` (Impact: 38.6), `VisitTypeDefinition` (Impact: 24.9)

### 2. `src/System.Management.Automation/engine/interpreter/Utilities.cs` (CSHARP) -> Cumulative Risk: **897.76**
- **Archetype:** `file_cluster_8` (Distance: 11.724 IQR)
- **Magnitude:** 1947.16 | **LOC:** 1158 | **CtrlFlow:** 56.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `MakeDelegate` (Impact: 244.2), `GetPrimitiveDefaultValue` (Impact: 178.8), `IsReadWriteAssignment` (Impact: 160.2)

### 3. `src/System.Management.Automation/utils/StringUtil.cs` (CSHARP) -> Cumulative Risk: **887.83**
- **Archetype:** `file_cluster_13` (Distance: 11.616 IQR)
- **Magnitude:** 389.68 | **LOC:** 274 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `VtSubstring` (Impact: 201.8), `TruncateToBufferCellWidth` (Impact: 31.4), `EndsWith` (Impact: 21.7)

### 4. `src/Microsoft.PowerShell.Commands.Management/cimSupport/cmdletization/cim/clientSideQuery.cs` (CSHARP) -> Cumulative Risk: **885.85**
- **Archetype:** `file_cluster_8` (Distance: 11.065 IQR)
- **Magnitude:** 1009.88 | **LOC:** 705 | **CtrlFlow:** 45.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetNotFoundErrors_IfThisIsTheOnlyFilter` (Impact: 63.8), `GetNotFoundErrors_IfThisIsTheOnlyFilter` (Impact: 55.7), `ShouldReportErrorOnNoMatches_IfMultipleF` (Impact: 47.8)

### 5. `src/System.Management.Automation/engine/hostifaces/PSTask.cs` (CSHARP) -> Cumulative Risk: **873.72**
- **Archetype:** `file_cluster_8` (Distance: 12.893 IQR)
- **Magnitude:** 1325.66 | **LOC:** 1594 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Add` (Impact: 127.2), `GetRunspace` (Impact: 96.5), `Start` (Impact: 57.5)

### 6. `src/System.Management.Automation/engine/BytePipe.cs` (CSHARP) -> Cumulative Risk: **872.37**
- **Archetype:** `file_cluster_13` (Distance: 12.677 IQR)
- **Magnitude:** 104.06 | **LOC:** 114 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `Create` (Impact: 23.4), `GetStream` (Impact: 21.8), `Bind` (Impact: 7.0)

### 7. `src/System.Management.Automation/engine/Utils.cs` (CSHARP) -> Cumulative Risk: **870.29**
- **Archetype:** `file_cluster_13` (Distance: 13.583 IQR)
- **Magnitude:** 1682.12 | **LOC:** 1867 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `TrySetPolicySettingsFromRegistryKey` (Impact: 200.6), `GetPolicySettingFromConfigFile` (Impact: 154.3), `ParseBinary` (Impact: 113.4)

### 8. `src/System.Management.Automation/engine/ComInterop/ComTypeDesc.cs` (CSHARP) -> Cumulative Risk: **867.25**
- **Archetype:** `file_cluster_8` (Distance: 11.804 IQR)
- **Magnitude:** 310.72 | **LOC:** 216 | **CtrlFlow:** 42.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetMemberNames` (Impact: 88.8), `FromITypeInfo` (Impact: 37.2), `TryGetFunc` (Impact: 9.2)

### 9. `src/System.Management.Automation/engine/InitialSessionState.cs` (CSHARP) -> Cumulative Risk: **864.74**
- **Archetype:** `file_cluster_0` (Distance: 13.408 IQR)
- **Magnitude:** 3299.44 | **LOC:** 5683 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.9844%)
- **Heaviest Functions:** `Bind` (Impact: 965.6), `UpdateFormats` (Impact: 772.7), `Clone` (Impact: 93.5)

### 10. `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` (CSHARP) -> Cumulative Risk: **859.61**
- **Archetype:** `file_cluster_8` (Distance: 13.015 IQR)
- **Magnitude:** 4179.36 | **LOC:** 7952 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `BinaryAdd` (Impact: 594.4), `InvokeMethod` (Impact: 328.0), `Bind` (Impact: 124.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.652 IQR)
- **Top Global Matches:** file_cluster_8: 13.652, file_cluster_13: 13.823, file_cluster_11: 13.878
- **Magnitude:** 10605.08 | **LOC:** 9263 | **CtrlFlow:** 62.5% | **Authorship Centralization:** 57.1%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 126
- **Risk Profile:** Cognitive Load (55.235%), Tech Debt (20.8623%)
**Top Internal Functions/Classes:**
  * `CompleteCommandArgument` (Impact: 2923.4 | O(N^6) | DB: 65)
  * `NativeCompletionCimCommands` (Impact: 2580.3 | O(N^6) | DB: 126)
  * `EscapeCharIfNeeded` (Impact: 2455.1 | O(N^6) | DB: 92)
  * `GetDefaultProviderResults` (Impact: 425.0 | O(N^6) | DB: 24)
  * `CompleteCommandParameter` (Impact: 352.9 | O(N^6) | DB: 19)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1010`, `structural_boundaries: 605`, `args: 220`, `func_start: 436`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1011`, `dead_code: 2`, `duplicate_logic: 9`, `orphaned_logic: 22`
* *Architecture:* `io: 4`, `api: 96`, `concurrency: 6`, `import: 25`
* *Defense:* `safety: 182`, `doc: 130`, `sync_locks: 1`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Reflection, Microsoft.PowerShell, System.Globalization, Microsoft.Management.Infrastructure.Options, Microsoft.PowerShell.Commands, System.Linq, System.Threading, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/ast.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 14.225 IQR)
- **Top Global Matches:** file_cluster_7: 14.225, file_cluster_8: 14.235, file_cluster_16: 14.239
- **Magnitude:** 6779.62 | **LOC:** 10846 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 59
- **Risk Profile:** Cognitive Load (28.996%), Tech Debt (99.9988%)
**Top Internal Functions/Classes:**
  * `GetReflectionType` (Impact: 1113.6 | O(2^N) | DB: 59)
  * `GetAncestorTypeDefinitionAst` (Impact: 491.6 | O(N^6) | DB: 36)
  * `InternalVisit` (Impact: 158.0 | O(2^N) | DB: 2)
    * *Intent:* /// <summary> /// Copy the NamedAttributeArgumentAst instance. /// </summary>
  * `InternalVisit` (Impact: 155.8 | O(2^N) | DB: 2)
  * `InternalVisit` (Impact: 148.3 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 452`, `structural_boundaries: 515`, `args: 273`, `func_start: 598`, `class_start: 58`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 751`, `dead_code: 3`, `planned_debt: 3`, `duplicate_logic: 121`, `orphaned_logic: 12`
* *Architecture:* `api: 455`, `concurrency: 30`, `import: 14`
* *Defense:* `safety: 105`, `doc: 1774`, `sync_locks: 3`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Linq, System.Reflection, System.Collections.Generic, System.Threading, Tuple, Microsoft.PowerShell, System.Diagnostics.CodeAnalysis, System.Reflection.Emit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/runtime/MutableTuple.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.733 IQR)
- **Top Global Matches:** file_cluster_16: 11.733, file_cluster_8: 11.836, file_cluster_7: 12.165
- **Magnitude:** 5463.4 | **LOC:** 2537 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (64.8147%), Tech Debt (92.8278%)
**Top Internal Functions/Classes:**
  * `SetValueImpl` (Impact: 1128.3 | O(N^4))
  * `GetValueImpl` (Impact: 809.0 | O(N^4))
  * `SetValueImpl` (Impact: 570.8 | O(N^4))
  * `GetValueImpl` (Impact: 413.8 | O(N^4))
  * `SetValueImpl` (Impact: 292.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 458`, `args: 83`, `func_start: 95`, `class_start: 9`
* *Risk/State:* `state_mutation: 348`, `duplicate_logic: 39`, `orphaned_logic: 7`
* *Architecture:* `api: 181`, `import: 9`
* *Defense:* `safety: 1`, `doc: 37`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Linq, System.CodeDom.Compiler, System.Collections.Generic, System.Reflection, System.Management.Automation.LanguagePrimitives.Null, System.Management.Automation.Language, System.Globalization, System.Linq.Expressions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/namespaces/FileSystemProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.593 IQR)
- **Top Global Matches:** file_cluster_0: 13.593, file_cluster_8: 13.635, file_cluster_7: 13.792
- **Magnitude:** 5414.0 | **LOC:** 9539 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 130
- **Risk Profile:** Cognitive Load (24.1298%), Tech Debt (14.2714%)
**Top Internal Functions/Classes:**
  * `IsValidPath` (Impact: 2009.5 | O(N^6) | DB: 130)
  * `CopyFileFromRemoteSession` (Impact: 251.0 | O(N^6) | DB: 23)
  * `InitializeDefaultDrives` (Impact: 250.4 | O(N^6) | DB: 11)
  * `CopyDirectoryFromRemoteSession` (Impact: 246.4 | O(2^N) | DB: 4)
    * *Intent:* /// <param name="type"> /// Specify "file" to create a file. /// Specify "directory" or "container" ...
  * `SetProperty` (Impact: 236.9 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 744`, `structural_boundaries: 237`, `args: 111`, `func_start: 354`, `class_start: 17`
* *Risk/State:* `state_mutation: 628`, `dead_code: 8`, `orphaned_logic: 28`
* *Architecture:* `io: 28`, `api: 92`, `concurrency: 1`, `import: 22`
* *Defense:* `safety: 266`, `doc: 471`, `immutability_locks: 46`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Xml, System.Globalization, System.Diagnostics, System.Linq, System.Management.Automation, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel, System.ComponentModel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.538 IQR)
- **Top Global Matches:** file_cluster_8: 13.538, file_cluster_13: 13.635, file_cluster_7: 13.675
- **Magnitude:** 4700.06 | **LOC:** 7495 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (25.3139%), Tech Debt (78.4876%)
**Top Internal Functions/Classes:**
  * `RemoveModule` (Impact: 345.9 | O(N^6) | DB: 20)
  * `LoadUsingExtensions` (Impact: 344.3 | O(N^6) | DB: 18)
  * `LoadModuleManifest` (Impact: 335.3 | O(N^6) | DB: 17)
  * `ImportFunctions` (Impact: 295.7 | O(N^6) | DB: 2)
  * `LoadModule` (Impact: 283.2 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 195`, `args: 82`, `func_start: 295`, `class_start: 5`
* *Risk/State:* `state_mutation: 723`, `dead_code: 10`, `planned_debt: 1`, `fragile_debt: 2`, `duplicate_logic: 18`, `orphaned_logic: 20`
* *Architecture:* `io: 34`, `api: 73`, `concurrency: 12`, `import: 20`
* *Defense:* `safety: 89`, `doc: 372`, `sync_locks: 8`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Reflection, System.Management.Automation.Diagnostics, System.Xml, System.Globalization, System.Diagnostics, System.Linq, System.Management.Automation, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Microsoft.WSMan.Management/ConfigProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.148 IQR)
- **Top Global Matches:** file_cluster_8: 13.148, file_cluster_7: 13.278, file_cluster_13: 13.328
- **Magnitude:** 4627.44 | **LOC:** 6578 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (21.4484%), Tech Debt (26.5156%)
**Top Internal Functions/Classes:**
  * `CheckValidContainerOrPath` (Impact: 791.9 | O(N^6) | DB: 19)
  * `HasChildItems` (Impact: 561.2 | O(N^6) | DB: 15)
  * `GetCorrectCaseOfName` (Impact: 312.6 | O(N^6) | DB: 22)
    * *Intent:* #endregion
  * `IsItemContainer` (Impact: 237.8 | O(N^6) | DB: 21)
  * `GetChildItemOrNamesForListenerOrCertMapp` (Impact: 169.7 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 539`, `structural_boundaries: 145`, `args: 91`, `func_start: 332`, `class_start: 6`
* *Risk/State:* `state_mutation: 565`, `dead_code: 11`, `planned_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 13`
* *Architecture:* `api: 61`, `import: 16`
* *Defense:* `safety: 42`, `doc: 346`, `sync_locks: 4`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Security, System.Collections.Generic, System.Xml, System.IO, System.Management.Automation, System.Xml.XPath, System.Diagnostics.CodeAnalysis, System.Runtime.InteropServices...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/namespaces/LocationGlobber.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.252 IQR)
- **Top Global Matches:** file_cluster_8: 14.252, file_cluster_7: 14.36, file_cluster_13: 14.554
- **Magnitude:** 4533.62 | **LOC:** 4733 | **CtrlFlow:** 88.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (23.4891%), Tech Debt (23.1551%)
**Top Internal Functions/Classes:**
  * `ExpandMshGlobPath` (Impact: 496.5 | O(N^6) | DB: 18)
    * *Intent:* // If there is no : then the path is relative to the // current working drive
  * `ExpandGlobPath` (Impact: 438.6 | O(N^6) | DB: 19)
    * *Intent:* /// <summary> /// Generates an array of provider specific paths from the single provider specific //...
  * `GenerateRelativePath` (Impact: 423.5 | O(N^6) | DB: 17)
    * *Intent:* /// <summary> /// Gets a provider specific path when given an Msh path without resolving the /// glo...
  * `GenerateNewPSPathsWithGlobLeaf` (Impact: 305.0 | O(N^6) | DB: 9)
  * `GetChildNamesInDir` (Impact: 301.1 | O(N^6) | DB: 12)
    * *Intent:* /// <summary> /// Removes the drive qualifier from a drive qualified MSH path. /// </summary> /// <p...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 636`, `structural_boundaries: 86`, `args: 46`, `func_start: 250`, `class_start: 1`
* *Risk/State:* `state_mutation: 699`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 7`
* *Architecture:* `api: 32`, `import: 4`
* *Defense:* `safety: 267`, `doc: 896`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Management.Automation, System.Collections.ObjectModel, System.Management.Automation.Provider, System.Text
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Microsoft.PowerShell.Security/security/CertificateProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.481 IQR)
- **Top Global Matches:** file_cluster_8: 13.481, file_cluster_7: 13.597, file_cluster_13: 13.626
- **Magnitude:** 4374.8 | **LOC:** 3566 | **CtrlFlow:** 74.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (14.3445%), Tech Debt (56.0925%)
**Top Internal Functions/Classes:**
  * `GetChildItemsOrNames` (Impact: 416.7 | O(2^N) | DB: 2)
  * `GetItemAtPath` (Impact: 216.8 | O(N^6) | DB: 10)
    * *Intent:* //
  * `DoDeleteKey` (Impact: 194.1 | O(N^6) | DB: 11)
  * `GetStoresOrNames` (Impact: 168.4 | O(N^6) | DB: 3)
    * *Intent:* // // children at the root path are store locations
  * `GetStoreNamesAtLocation` (Impact: 156.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 503`, `structural_boundaries: 169`, `args: 91`, `func_start: 198`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 1`, `state_mutation: 395`, `dead_code: 11`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 17`
* *Architecture:* `io: 4`, `api: 66`, `import: 19`
* *Defense:* `safety: 157`, `doc: 618`, `sync_locks: 4`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Xml, System.Security.Cryptography.X509Certificates, System.Globalization, System.Diagnostics, System.Management.Automation, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel, System.Management.Automation.Host...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/DscSupport/CimDSCParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.38 IQR)
- **Top Global Matches:** file_cluster_8: 13.38, file_cluster_13: 13.498, file_cluster_7: 13.499
- **Magnitude:** 4203.0 | **LOC:** 4077 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 163
- **Risk Profile:** Cognitive Load (31.0553%), Tech Debt (56.7444%)
**Top Internal Functions/Classes:**
  * `LoadResourcesFromModule` (Impact: 1617.0 | O(N^6) | DB: 163)
  * `ConvertCimInstanceToObject` (Impact: 398.9 | O(2^N) | DB: 11)
    * *Intent:* /// <summary> /// Convert Cim Instance representing Resource desired state to Powershell Class Objec...
  * `GetModuleInfoHelper` (Impact: 381.4 | O(N^6) | DB: 28)
    * *Intent:* /// <summary> /// Get the module name and module version. /// </summary> /// <param name="moduleFold...
  * `GetDSCResourceUsageString` (Impact: 183.4 | O(N^6) | DB: 6)
  * `Initialize` (Impact: 145.6 | O(N^6) | DB: 74)
    * *Intent:* /// <summary> /// Initialize the class cache with the default classes in $ENV:SystemDirectory\Config...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 541`, `structural_boundaries: 334`, `args: 116`, `func_start: 351`, `class_start: 5`
* *Risk/State:* `state_mutation: 520`, `dead_code: 2`, `planned_debt: 5`, `duplicate_logic: 14`, `orphaned_logic: 11`
* *Architecture:* `io: 55`, `api: 67`, `import: 20`
* *Defense:* `safety: 103`, `doc: 470`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Reflection, System.Globalization, System.Diagnostics, Microsoft.PowerShell.Commands, System.Linq, System.Management.Automation, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.015 IQR)
- **Top Global Matches:** file_cluster_8: 13.015, file_cluster_13: 13.095, file_cluster_17: 13.134
- **Magnitude:** 4179.36 | **LOC:** 7952 | **CtrlFlow:** 46.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (46.2911%), Tech Debt (99.4846%)
**Top Internal Functions/Classes:**
  * `BinaryAdd` (Impact: 594.4 | O(N^6) | DB: 14)
    * *Intent:* /*useLocalScope=*/ ExpressionCache.Constant(true),
  * `InvokeMethod` (Impact: 328.0 | O(N^6) | DB: 11)
  * `Bind` (Impact: 124.5 | O(2^N))
  * `FallbackGetIndex` (Impact: 122.5 | O(N^6) | DB: 3)
  * `PSGetStaticMemberRestriction` (Impact: 104.6 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 428`, `structural_boundaries: 493`, `args: 210`, `func_start: 412`, `class_start: 19`
* *Risk/State:* `state_mutation: 441`, `dead_code: 15`, `planned_debt: 2`, `duplicate_logic: 43`, `orphaned_logic: 20`
* *Architecture:* `api: 94`, `concurrency: 36`, `import: 20`
* *Defense:* `safety: 115`, `doc: 59`, `sync_locks: 14`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Reflection, System.Xml, System.Globalization, System.Linq, System.Threading, Tuple, System.Linq.Expressions, System.Management.Automation.Internal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/CoreAdapter.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.267 IQR)
- **Top Global Matches:** file_cluster_8: 13.267, file_cluster_16: 13.326, file_cluster_7: 13.364
- **Magnitude:** 3977.4 | **LOC:** 6260 | **CtrlFlow:** 56.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 75
- **Risk Profile:** Cognitive Load (29.1466%), Tech Debt (94.9816%)
**Top Internal Functions/Classes:**
  * `GetMethodInvoker` (Impact: 1295.6 | O(N^6) | DB: 75)
  * `CompareOverloadCandidates` (Impact: 713.0 | O(N^6) | DB: 43)
    * *Intent:* /// <summary> /// Called after a non null return from GetMember to try to call /// the method with t...
  * `Unify` (Impact: 210.6 | O(2^N) | DB: 2)
  * `DoBoxingIfNecessary` (Impact: 137.4 | O(N^5) | DB: 1)
  * `GetInferredType` (Impact: 105.0 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 329`, `args: 160`, `func_start: 331`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 385`, `dead_code: 5`, `planned_debt: 2`, `duplicate_logic: 33`, `orphaned_logic: 5`
* *Architecture:* `api: 62`, `import: 20`
* *Defense:* `safety: 75`, `doc: 541`, `sync_locks: 6`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Reflection, System.Management.Automation.Diagnostics, System.Xml, Microsoft.PowerShell, System.Globalization, System.Diagnostics, System.Linq, System.Threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/LanguagePrimitives.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.373 IQR)
- **Top Global Matches:** file_cluster_8: 13.373, file_cluster_13: 13.487, file_cluster_7: 13.501
- **Magnitude:** 3741.82 | **LOC:** 5889 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 55
- **Risk Profile:** Cognitive Load (23.8532%), Tech Debt (75.0213%)
**Top Internal Functions/Classes:**
  * `NumericCompare` (Impact: 1250.6 | O(N^6) | DB: 55)
  * `FigureLanguageConversion` (Impact: 314.7 | O(N^6) | DB: 14)
  * `Compare` (Impact: 269.9 | O(2^N) | DB: 5)
  * `ConvertStringToReal` (Impact: 185.3 | O(N^6) | DB: 3)
  * `CalculateGetEnumerable` (Impact: 111.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 389`, `structural_boundaries: 283`, `args: 120`, `func_start: 371`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 368`, `dead_code: 5`, `planned_debt: 5`, `duplicate_logic: 14`, `orphaned_logic: 20`
* *Architecture:* `api: 92`, `concurrency: 6`, `import: 22`
* *Defense:* `safety: 149`, `doc: 394`, `sync_locks: 8`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Reflection, System.Management.Automation.Diagnostics, System.Xml, System.Globalization, System.DirectoryServices, System.Numerics, System.Diagnostics.CodeAnalysis, System.Management.Automation.DotNetAdapter.MethodCacheEntry...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/FormatAndOutput/DefaultFormatters/PowerShellCore_format_ps1xml.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.541 IQR)
- **Top Global Matches:** file_cluster_8: 9.541, file_cluster_7: 10.267, file_cluster_1: 10.332
- **Magnitude:** 3506.44 | **LOC:** 2332 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (14.1827%), Tech Debt (93.7633%)
**Top Internal Functions/Classes:**
  * `ViewsOf_System_Management_Automation_Err` (Impact: 904.4 | O(N^6) | DB: 3)
  * `GetFormatData` (Impact: 538.8 | O(N^6) | DB: 11)
  * `ViewsOf_System_Management_Automation_Get` (Impact: 519.1 | O(N^6) | DB: 11)
    * *Intent:* // This generates a custom view for ErrorRecords and Exceptions making // specific nested types defi...
  * `ViewsOf_System_Management_Automation_Run` (Impact: 72.8 | O(N^6))
  * `ViewsOf_Microsoft_PowerShell_Commands_Ac` (Impact: 63.6 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 359`, `structural_boundaries: 304`, `args: 65`, `func_start: 245`, `class_start: 1`
* *Risk/State:* `state_mutation: 49`, `duplicate_logic: 32`, `orphaned_logic: 29`
* *Architecture:* `io: 2`, `api: 2`, `import: 1`
* *Defense:* `safety: 26`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/TypeTable.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.116 IQR)
- **Top Global Matches:** file_cluster_8: 13.116, file_cluster_7: 13.329, file_cluster_13: 13.335
- **Magnitude:** 3327.5 | **LOC:** 4780 | **CtrlFlow:** 69.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 203
- **Risk Profile:** Cognitive Load (41.1594%), Tech Debt (9.8189%)
**Top Internal Functions/Classes:**
  * `Read_MemberSet` (Impact: 1360.3 | O(N^6) | DB: 203)
  * `Read_Type` (Impact: 351.4 | O(N^6) | DB: 6)
  * `Read_Members` (Impact: 288.4 | O(N^6) | DB: 11)
  * `Read_TypeX` (Impact: 89.1 | O(N^6) | DB: 2)
  * `SkipUntilNodeEnd` (Impact: 81.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 150`, `args: 92`, `func_start: 305`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 547`, `duplicate_logic: 2`
* *Architecture:* `io: 4`, `api: 36`, `import: 16`
* *Defense:* `safety: 40`, `doc: 142`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.566
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003353
  * `Imports (Out-Degree: 2):` System.Security, System.Linq, System.Reflection, System.Collections.Generic, System.Xml, System.IO, System.Management.Automation.Language, System.Collections.ObjectModel...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/InitialSessionState.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.408 IQR)
- **Top Global Matches:** file_cluster_0: 13.408, file_cluster_8: 13.45, file_cluster_7: 13.481
- **Magnitude:** 3299.44 | **LOC:** 5683 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 47
- **Risk Profile:** Cognitive Load (27.4202%), Tech Debt (99.9844%)
**Top Internal Functions/Classes:**
  * `Bind` (Impact: 965.6 | O(N^6) | DB: 47)
  * `UpdateFormats` (Impact: 772.7 | O(N^6) | DB: 33)
    * *Intent:* // If this occurs while loading a module manifest, just
  * `Clone` (Impact: 93.5 | O(2^N) | DB: 14)
  * `CreateDefault` (Impact: 89.1 | O(N^6) | DB: 8)
  * `LookUpByName` (Impact: 32.4 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 156`, `args: 310`, `func_start: 302`, `class_start: 16`
* *Risk/State:* `state_mutation: 400`, `dead_code: 7`, `fragile_debt: 1`, `duplicate_logic: 56`, `orphaned_logic: 43`
* *Architecture:* `io: 9`, `api: 207`, `concurrency: 72`, `import: 19`
* *Defense:* `safety: 54`, `doc: 598`, `sync_locks: 20`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Reflection, System.Management.Automation.Diagnostics, Microsoft.PowerShell.Commands, System.Linq, System.Threading, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel, System.Management.Automation.Host...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.533 IQR)
- **Top Global Matches:** file_cluster_13: 14.533, file_cluster_16: 14.558, file_cluster_7: 14.564
- **Magnitude:** 3191.44 | **LOC:** 6192 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 75.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (24.1213%), Tech Debt (99.2598%)
**Top Internal Functions/Classes:**
  * `SetStateChanged` (Impact: 368.8 | O(N^6) | DB: 8)
  * `Prepare` (Impact: 225.4 | O(N^6) | DB: 14)
    * *Intent:* /// Input to the command /// </param> /// <param name="output"> /// A collection supplied by the use...
  * `FromPSObjectForRemoting` (Impact: 174.4 | O(2^N) | DB: 4)
  * `CoreInvokeAsync` (Impact: 134.8 | O(N^6) | DB: 6)
    * *Intent:* /// <summary> /// Invoke the <see cref="Command"/> synchronously and return /// the output. /// </su...
  * `Stop` (Impact: 127.5 | O(2^N) | DB: 1)
    * *Intent:* /// </remarks> /// <typeparam name="TInput"> /// Type of input object(s) for the command invocation....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 292`, `structural_boundaries: 102`, `args: 82`, `func_start: 319`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 376`, `dead_code: 13`, `planned_debt: 2`, `duplicate_logic: 35`, `orphaned_logic: 10`
* *Architecture:* `api: 100`, `concurrency: 8`, `import: 16`
* *Defense:* `safety: 92`, `doc: 1302`, `sync_locks: 30`, `immutability_locks: 12`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.934
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.014085
  * `Imports (Out-Degree: 2):` System.Management.Automation.Diagnostics, System.Management.Automation.Runspaces, System.Collections.Generic, System.Threading, System.Management.Automation, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel, System.Management.Automation.Host...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/ParameterBinderBase.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.525 IQR)
- **Top Global Matches:** file_cluster_8: 13.525, file_cluster_13: 13.559, file_cluster_7: 13.634
- **Magnitude:** 3174.1 | **LOC:** 2068 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 65
- **Risk Profile:** Cognitive Load (29.3477%), Tech Debt (19.7165%)
**Top Internal Functions/Classes:**
  * `BindParameter` (Impact: 2806.9 | O(2^N) | DB: 65)
    * *Intent:* /// protected BindParameter method. /// </remarks> /// <exception cref="ArgumentNullException"> /// ...
  * `ValidatePSTypeName` (Impact: 50.2 | O(N^6) | DB: 2)
  * `ParameterBinderBase` (Impact: 18.8 | O(N^3) | DB: 6)
    * *Intent:* /// for a single instance of a bindable object and only for the duration of a command. /// </summary...
  * `ParameterBinderBase` (Impact: 12.8 | O(N^3) | DB: 5)
    * *Intent:* /// <summary> /// Constructs the parameter binder with the specified type metadata. The binder is on...
  * `CopyBoundPositionalParameters` (Impact: 10.5 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 58`, `args: 44`, `func_start: 118`, `class_start: 5`
* *Risk/State:* `state_mutation: 223`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 30`, `import: 10`
* *Defense:* `safety: 68`, `doc: 176`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, System.Reflection, System.Collections.Generic, System.Management.Automation.Diagnostics, System.Diagnostics.CodeAnalysis, System.Management.Automation.Language, System.Collections.ObjectModel, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/InternalCommands.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.014 IQR)
- **Top Global Matches:** file_cluster_0: 13.014, file_cluster_8: 13.05, file_cluster_13: 13.107
- **Magnitude:** 3115.26 | **LOC:** 2846 | **CtrlFlow:** 65.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 129
- **Risk Profile:** Cognitive Load (27.8719%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `GetValue` (Impact: 2664.3 | O(2^N) | DB: 129)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 213`, `structural_boundaries: 112`, `args: 58`, `func_start: 84`, `class_start: 4`
* *Risk/State:* `state_mutation: 369`, `dead_code: 2`
* *Architecture:* `api: 38`, `concurrency: 19`, `import: 14`
* *Defense:* `safety: 29`, `doc: 156`, `immutability_locks: 2`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Management.Automation.Internal.CommonParameters, System.Management.Automation.Diagnostics, System.Collections.Generic, System.Threading, System.Management.Automation.Security, System.Diagnostics.CodeAnalysis.NotNullWhenAttribute, System.Management.Automation, System.Management.Automation.Language...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/TypeInferenceVisitor.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.891 IQR)
- **Top Global Matches:** file_cluster_8: 12.891, file_cluster_13: 13.068, file_cluster_7: 13.13
- **Magnitude:** 3107.02 | **LOC:** 3339 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (37.3481%), Tech Debt (97.7886%)
**Top Internal Functions/Classes:**
  * `AddMembersByInferredTypeDefinitionAst` (Impact: 603.7 | O(N^6) | DB: 17)
  * `ICustomAstVisitor.VisitStatementBlock` (Impact: 456.4 | O(N^6) | DB: 17)
  * `AddTypesFromMethodCacheEntry` (Impact: 376.5 | O(N^6) | DB: 17)
  * `VisitCommand` (Impact: 263.1 | O(N^6) | DB: 5)
  * `InferTypeFrom` (Impact: 215.3 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 215`, `args: 64`, `func_start: 158`, `class_start: 6`
* *Risk/State:* `state_mutation: 294`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 30`
* *Architecture:* `api: 44`, `import: 10`
* *Defense:* `safety: 71`, `doc: 119`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, System.Management.Automation.Runspaces, System.Collections.Generic, System.Reflection, Microsoft.Management.Infrastructure.CimInstance, System.Management.Automation.Language, System.Globalization, Microsoft.Management.Infrastructure.CimClass...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/debugger/debugger.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_7` (Drift: 14.119 IQR)
- **Top Global Matches:** file_cluster_7: 14.119, file_cluster_8: 14.132, file_cluster_13: 14.154
- **Magnitude:** 3066.38 | **LOC:** 5955 | **CtrlFlow:** 53.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 122
- **Risk Profile:** Cognitive Load (29.0821%), Tech Debt (96.4166%)
**Top Internal Functions/Classes:**
  * `EnterScriptFunction` (Impact: 1419.1 | O(N^6) | DB: 122)
    * *Intent:* #endregion #region Call stack management // Called from generated code on entering the script functi...
  * `DisplayScript` (Impact: 178.2 | O(2^N) | DB: 4)
  * `DoProcessCommand` (Impact: 96.2 | O(N^6) | DB: 2)
  * `GetFrameVariables` (Impact: 68.8 | O(N^6) | DB: 1)
  * `WriteErrorLine` (Impact: 42.6 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 251`, `structural_boundaries: 218`, `args: 172`, `func_start: 355`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 445`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 22`, `orphaned_logic: 21`
* *Architecture:* `io: 4`, `api: 193`, `import: 18`
* *Defense:* `safety: 72`, `doc: 888`, `sync_locks: 5`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Linq, System.Management.Automation.Runspaces, System.Collections.Generic, System.Management.Automation.Internal.Host, System.Threading, System.IO, Microsoft.PowerShell.Commands.Internal.Format, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/remoting/fanin/WSManTransportManager.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.85 IQR)
- **Top Global Matches:** file_cluster_8: 12.85, file_cluster_7: 12.958, file_cluster_13: 13.044
- **Magnitude:** 3013.22 | **LOC:** 4163 | **CtrlFlow:** 70.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 94
- **Risk Profile:** Cognitive Load (17.564%), Tech Debt (11.1652%)
**Top Internal Functions/Classes:**
  * `ConstructTransportErrorEventArgs` (Impact: 2327.3 | O(2^N) | DB: 94)
    * *Intent:* /// <param name="wsmanSessionTM"> /// Session Transportmanager to use to get error messages (for red...
  * `CreateAsync` (Impact: 177.0 | O(N^6) | DB: 30)
  * `OnRemoteSessionDataReceived` (Impact: 82.9 | O(N^6) | DB: 2)
  * `OnRemoteSessionSendCompleted` (Impact: 73.1 | O(N^6) | DB: 2)
  * `SendOneItem` (Impact: 20.1 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 69`, `args: 48`, `func_start: 181`, `class_start: 4`
* *Risk/State:* `state_mutation: 263`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `api: 32`, `concurrency: 12`, `import: 12`
* *Defense:* `safety: 28`, `doc: 210`, `sync_locks: 18`, `immutability_locks: 11`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Management.Automation.Diagnostics, System.Collections.Generic, System.Management.Automation.Remoting.Server, System.Security.Principal, System.Xml, System.IO, System.Threading, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/SessionStateContainer.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.349 IQR)
- **Top Global Matches:** file_cluster_8: 13.349, file_cluster_7: 13.42, file_cluster_13: 13.667
- **Magnitude:** 2917.9 | **LOC:** 4898 | **CtrlFlow:** 78.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (9.5587%), Tech Debt (84.1524%)
**Top Internal Functions/Classes:**
  * `ProcessPathItems` (Impact: 661.4 | O(2^N) | DB: 9)
  * `RemoveItem` (Impact: 192.5 | O(2^N) | DB: 1)
    * *Intent:* /// </param> /// <exception cref="ProviderNotFoundException"> /// If the <paramref name="path"/> ref...
  * `GetChildItems` (Impact: 174.9 | O(2^N) | DB: 1)
    * *Intent:* /// <exception cref="DriveNotFoundException"> /// If the <paramref name="path"/> refers to a drive t...
  * `IsItemContainer` (Impact: 172.3 | O(2^N) | DB: 5)
    * *Intent:* /// The path to the item if it was specified on the command line. /// </param> /// <param name="cont...
  * `CopyItemDynamicParameters` (Impact: 144.5 | O(2^N) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 50`, `args: 56`, `func_start: 191`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 180`, `dead_code: 2`, `duplicate_logic: 22`, `orphaned_logic: 4`
* *Architecture:* `io: 2`, `api: 19`, `import: 7`
* *Defense:* `safety: 83`, `doc: 784`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Reflection, System.Management.Automation.Runspaces, System.IO, System.Management.Automation, System.Collections.ObjectModel, System.Management.Automation.Provider, System.Management.Automation.Internal, System.Collections
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/remoting/fanin/InitialSessionStateProvider.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.746 IQR)
- **Top Global Matches:** file_cluster_8: 12.746, file_cluster_7: 12.898, file_cluster_13: 12.899
- **Magnitude:** 2758.48 | **LOC:** 3032 | **CtrlFlow:** 77.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 44
- **Risk Profile:** Cognitive Load (15.6578%), Tech Debt (35.7809%)
**Top Internal Functions/Classes:**
  * `GetInitialSessionState` (Impact: 812.4 | O(N^6) | DB: 27)
  * `LoadSsnStateProviderAssembly` (Impact: 447.6 | O(N^6) | DB: 44)
  * `Update` (Impact: 155.0 | O(N^6) | DB: 11)
    * *Intent:* #endregion #region Methods /// <summary> /// Using optionName and optionValue updates the current ob...
  * `Create` (Impact: 139.9 | O(2^N) | DB: 2)
  * `ProcessCommandModification` (Impact: 123.3 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 82`, `args: 43`, `func_start: 145`, `class_start: 3`
* *Risk/State:* `state_mutation: 226`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 8`
* *Architecture:* `io: 16`, `api: 57`, `import: 15`
* *Defense:* `safety: 70`, `doc: 216`, `sync_locks: 2`, `immutability_locks: 25`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Linq, System.Management.Automation.Runspaces, System.Collections.Generic, System.Reflection, System.Threading, System.Xml, System.IO, System.Management.Automation.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/remoting/commands/ReceiveJob.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.643 IQR)
- **Top Global Matches:** file_cluster_8: 12.643, file_cluster_0: 12.645, file_cluster_13: 12.668
- **Magnitude:** 2599.86 | **LOC:** 1614 | **CtrlFlow:** 67.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (11.4241%), Tech Debt (20.764%)
**Top Internal Functions/Classes:**
  * `ProcessRecord` (Impact: 541.8 | O(2^N) | DB: 8)
    * *Intent:* /// <summary> /// Retrieve the results for the specified computers or /// runspaces. /// </summary>
  * `WriteJobResults` (Impact: 319.8 | O(N^6))
    * *Intent:* /// <summary> /// Write the results from this Job object. This does not write from the /// child job...
  * `AutoRemoveJobIfRequired` (Impact: 190.1 | O(2^N) | DB: 1)
  * `Dispose` (Impact: 175.1 | O(2^N) | DB: 2)
    * *Intent:* /// <summary> /// </summary> /// <param name="disposing"></param>
  * `AggregateResultsFromJob` (Impact: 159.7 | O(2^N) | DB: 1)
    * *Intent:* /// <summary> /// </summary> /// <param name="job"></param> /// <remarks>this method should always b...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 102`, `args: 38`, `func_start: 206`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 138`, `dead_code: 6`, `planned_debt: 1`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 19`, `import: 12`
* *Defense:* `safety: 67`, `doc: 134`, `sync_locks: 18`, `immutability_locks: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Management.Automation.Diagnostics, System.Management.Automation.Remoting, System.Collections.Generic, System.Management.Automation.Runspaces, System.Threading, System.Management.Automation, System.Diagnostics.CodeAnalysis, System.Collections.ObjectModel...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/serialization.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.111 IQR)
- **Top Global Matches:** file_cluster_8: 13.111, file_cluster_7: 13.229, file_cluster_13: 13.259
- **Magnitude:** 2572.78 | **LOC:** 7680 | **CtrlFlow:** 67.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (10.4142%), Tech Debt (99.1515%)
**Top Internal Functions/Classes:**
  * `HandleKnownContainerTypes` (Impact: 184.2 | O(N^6) | DB: 3)
  * `Add` (Impact: 124.5 | O(2^N) | DB: 3)
  * `HandleComplexTypePSObject` (Impact: 96.7 | O(N^6) | DB: 5)
  * `WriteDictionary` (Impact: 94.7 | O(N^6) | DB: 3)
  * `ReadMemberSet` (Impact: 79.7 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 238`, `structural_boundaries: 114`, `args: 103`, `func_start: 383`, `class_start: 8`
* *Risk/State:* `state_mutation: 231`, `dead_code: 4`, `fragile_debt: 1`, `duplicate_logic: 21`, `orphaned_logic: 28`
* *Architecture:* `api: 72`, `import: 23`
* *Defense:* `safety: 68`, `doc: 427`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.565
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Reflection, System.Management.Automation.Diagnostics, System.Xml, System.Globalization, Microsoft.PowerShell.Commands, System.Linq, System.Management.Automation, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Microsoft.PowerShell.Commands.Management/commands/management/RemovePropertyCommand.cs` (CSHARP) | Magnitude: 142.62 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 111, doc: 42, state_mutation: 19, branch: 15
- `src/System.Management.Automation/engine/remoting/commands/removerunspacecommand.cs` (CSHARP) | Magnitude: 252.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 44, doc: 35, branch: 25
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Native.cs` (CSHARP) | Magnitude: 185.36 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 270, api: 105, encapsulation: 72, immutability_locks: 48
- `src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/ManagementListTitle.Generated.cs` (CSHARP) | Magnitude: 68.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 133, doc: 63, func_start: 39, decorators: 17
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/Set-PSBreakpoint.cs` (CSHARP) | Magnitude: 263.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 157, doc: 30, branch: 26, decorators: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/System.Management.Automation/utils/IObjectWriter.cs` (CSHARP) | Magnitude: 87.3 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 84, indent_spaces: 80, api: 18, structural_boundaries: 12
- `src/Microsoft.Management.UI.Internal/commandHelpers/HelpWindowHelper.cs` (CSHARP) | Magnitude: 20.9 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 14, doc: 8, import: 7
- `src/System.Management.Automation/engine/remoting/common/fragmentor.cs` (CSHARP) | Magnitude: 805.4 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 573, doc: 349, func_start: 94, state_mutation: 89
- `src/System.Management.Automation/engine/remoting/server/serverremotesessionstatemachine.cs` (CSHARP) | Magnitude: 859.02 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 530, doc: 300, func_start: 124, branch: 98
- `src/Microsoft.Management.UI.Internal/ShowCommand/Controls/ShowModuleControl.xaml.cs` (CSHARP) | Magnitude: 26.88 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 34, indent_spaces: 32, structural_boundaries: 8, func_start: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tools/windows/Reset-PWSHSystemPath.ps1` (POWERSHELL) | Magnitude: 0.04 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 26, state_mutation: 21, doc: 8, branch: 7
- `tools/UpdateDotnetRuntime.ps1` (POWERSHELL) | Magnitude: 0.72 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 268, state_mutation: 178, branch: 92, closures: 44
- `tools/installpsh-amazonlinux.sh` (SHELL) | Magnitude: 0.25 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 95, branch: 74, indent_spaces: 74, io: 34
- `tools/ci.psm1` (POWERSHELL) | Magnitude: 0.76 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 380, state_mutation: 257, branch: 93, api: 54
- `tools/installpsh-mariner.sh` (SHELL) | Magnitude: 0.27 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: state_mutation: 106, branch: 74, indent_spaces: 73, io: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tools/installpsh-debian.sh` (SHELL) | Magnitude: 0.35 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 118, state_mutation: 114, branch: 83, io: 55
- `tools/installpsh-redhat.sh` (SHELL) | Magnitude: 0.24 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 70, branch: 64, io: 29
- `tools/installpsh-gentoo.sh` (SHELL) | Magnitude: 0.3 | Delta: **0.089 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 100, branch: 84, indent_spaces: 83, io: 47
- `tools/install-powershell.sh` (SHELL) | Magnitude: 0.56 | Delta: **0.104 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 148, indent_spaces: 123, io: 50, branch: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Microsoft.Management.UI.Internal/ShowCommand/Controls/ImageButton/ImageButtonToolTipConverter.cs` (CSHARP) | Magnitude: 31.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 28, doc: 20, structural_boundaries: 10, sec_high_risk_execution: 6
- `src/Microsoft.Management.UI.Internal/ManagementList/Common/PropertyChangedEventArgs.cs` (CSHARP) | Magnitude: 12.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 15, api: 4, state_mutation: 4
- `src/System.Management.Automation/namespaces/RegistrySecurity.cs` (CSHARP) | Magnitude: 154.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 115, doc: 56, state_mutation: 21, branch: 20
- `src/System.Management.Automation/utils/MshArgumentNullException.cs` (CSHARP) | Magnitude: 32.7 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 63, indent_spaces: 51, api: 7, sec_high_risk_execution: 7
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/PSUserAgent.cs` (CSHARP) | Magnitude: 365.06 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 21, doc: 18, args: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/tools/Modules/HelpersRemoting/HelpersRemoting.psm1` (POWERSHELL) | Magnitude: 0.84 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 444, state_mutation: 180, branch: 103, closures: 69
- `test/tools/Modules/HttpListener/HttpListener.psm1` (POWERSHELL) | Magnitude: 1.15 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 325, state_mutation: 198, branch: 73, closures: 41
- `.github/skills/analyze-pester-failures/scripts/analyze-pr-test-failures.ps1` (POWERSHELL) | Magnitude: 229.7 | Delta: **0.15 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 185, state_mutation: 170, branch: 96, closures: 55
- `src/System.Management.Automation/engine/parser/PreOrderVisitor.cs` (CSHARP) | Magnitude: 242.14 | Delta: **0.167 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 94, indent_spaces: 92, structural_boundaries: 72, api: 69
- `src/System.Management.Automation/engine/parser/AstVisitor.cs` (CSHARP) | Magnitude: 1040.68 | Delta: **0.172 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 381, structural_boundaries: 283, func_start: 273, args: 263

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/trace/TraceListenerCommandBase.cs` (CSHARP) | Magnitude: 633.26 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 262, doc: 60, state_mutation: 51, branch: 40
- `src/Microsoft.Management.UI.Internal/ManagementList/FilterProviders/SearchTextParser.cs` (CSHARP) | Magnitude: 150.26 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 130, doc: 63, state_mutation: 26, func_start: 21
- `src/System.Management.Automation/engine/SessionStateCmdletAPIs.cs` (CSHARP) | Magnitude: 231.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, doc: 48, branch: 15, state_mutation: 14
- `src/System.Management.Automation/engine/ManagementObjectAdapter.cs` (CSHARP) | Magnitude: 624.34 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 483, doc: 192, func_start: 84, branch: 70
- `src/System.Management.Automation/FormatAndOutput/common/DisplayDatabase/displayDescriptionData.cs` (CSHARP) | Magnitude: 660.82 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 528, doc: 247, api: 166, encapsulation: 145

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/InnerList.Generated.cs` (CSHARP) | Magnitude: 72.56 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 109, doc: 60, func_start: 40, args: 18
- `src/Microsoft.Management.UI.Internal/ManagementList/Common/TextBlockService.Generated.cs` (CSHARP) | Magnitude: 62.38 | Delta: **0.12 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 66, indent_spaces: 61, func_start: 28, args: 16
- `test/tools/OpenCover/OpenCover.Types.ps1xml` (POWERSHELL) | Magnitude: 0.02 | Delta: **0.18 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 16, ui_framework: 6, state_mutation: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/System.Management.Automation/engine/remoting/client/Job2.cs` (CSHARP) | Magnitude: 969.26 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 566, doc: 350, state_mutation: 118, func_start: 103
- `src/System.Management.Automation/engine/remoting/common/throttlemanager.cs` (CSHARP) | Magnitude: 231.86 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 210, doc: 138, encapsulation: 41, func_start: 36
- `test/tools/WebListener/Controllers/DelayController.cs` (CSHARP) | Magnitude: 0.27 | Delta: **0.088 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 113, structural_boundaries: 33, state_mutation: 27, concurrency: 24
- `src/System.Management.Automation/engine/Subsystem/FeedbackSubsystem/FeedbackHub.cs` (CSHARP) | Magnitude: 645.7 | Delta: **0.13 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 228, branch: 73, state_mutation: 70, concurrency: 44
- `src/System.Management.Automation/engine/AsyncByteStreamTransfer.cs` (CSHARP) | Magnitude: 150.22 | Delta: **0.469 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 54, indent_spaces: 52, structural_boundaries: 13, state_mutation: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/System.Management.Automation/namespaces/IContentProvider.cs` (CSHARP) | Magnitude: 167.55 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 124, indent_spaces: 11, sec_high_risk_execution: 9, args: 6
- `src/System.Management.Automation/engine/ICommandRuntime.cs` (CSHARP) | Magnitude: 575.38 | Delta: **0.086 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: doc: 325, sec_high_risk_execution: 55, indent_spaces: 28, state_mutation: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/System.Management.Automation/namespaces/IPermissionProvider.cs` (CSHARP) | Magnitude: 30.88 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 63, indent_spaces: 14, sec_high_risk_execution: 4, structural_boundaries: 3
- `src/Microsoft.Management.Infrastructure.CimCmdlets/Utils.cs` (CSHARP) | Magnitude: 315.98 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 205, doc: 168, api: 49, encapsulation: 49
- `src/System.Management.Automation/engine/EventManager.cs` (CSHARP) | Magnitude: 986.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 736, doc: 724, func_start: 122, state_mutation: 109
- `src/System.Management.Automation/engine/CommandCompletion/CompletionHelpers.cs` (CSHARP) | Magnitude: 211.76 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 137, doc: 135, state_mutation: 29, structural_boundaries: 27
- `src/Microsoft.PowerShell.Commands.Management/commands/management/GetComputerInfoCommand.cs` (CSHARP) | Magnitude: 1215.2 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 1193, indent_spaces: 1042, state_mutation: 391, sec_high_risk_execution: 159

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/OrderObjectBase.cs` (CSHARP) | Magnitude: 916.86 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 527, state_mutation: 92, branch: 80, func_start: 58
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/PSBreakpointUpdaterCommandBase.cs` (CSHARP) | Magnitude: 149.46 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 109, structural_boundaries: 20, state_mutation: 19, doc: 15
- `src/Microsoft.Management.UI.Internal/ManagementList/FilterCore/ItemsControlFilterEvaluator.cs` (CSHARP) | Magnitude: 109.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, doc: 18, state_mutation: 16, branch: 11
- `src/Microsoft.Management.UI.Internal/ManagementList/FilterCore/FilterRules/IsNotEmptyValidationRule.cs` (CSHARP) | Magnitude: 37.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, doc: 16, structural_boundaries: 8, branch: 4
- `src/System.Management.Automation/engine/Interop/Windows/VariantClear.cs` (CSHARP) | Magnitude: 23.34 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 5, structural_boundaries: 3, api: 3, encapsulation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/System.Management.Automation/engine/hostifaces/InternalHostRawUserInterface.cs` (CSHARP) | Magnitude: 316.62 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 350, doc: 176, func_start: 50, branch: 31
- `tools/AttackSurfaceAnalyzer/docker/Dockerfile` (DOCKERFILE) | Magnitude: 0.21 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, branch: 15, func_start: 12, structural_boundaries: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/packaging/packaging.psm1` -> Churn: **100.0%** | Cog Load: 81.0507% | Debt: 21.1499%
- `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` -> Churn: **54.65%** | Cog Load: 24.1213% | Debt: 99.2598%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4700.06
- `src/Microsoft.WSMan.Management/ConfigProvider.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4627.44
- `src/System.Management.Automation/namespaces/LocationGlobber.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4533.62
- `src/Microsoft.PowerShell.Security/security/CertificateProvider.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4374.8
- `src/System.Management.Automation/DscSupport/CimDSCParser.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4203.0

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 0.004** (Bridge: 0.0 * Flux: 99.9962%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 3.914** (Embedded: 0.0461 * Error Risk: 84.8101%)
- `src/System.Management.Automation/utils/tracing/Tracing.cs` -> **Severity: 1.434** (Embedded: 0.0275 * Error Risk: 52.104%)
- `tools/Xml/Xml.psm1` -> **Severity: 1.2** (Embedded: 0.0592 * Error Risk: 20.2792%)
- `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` -> **Severity: 0.645** (Embedded: 0.0141 * Error Risk: 45.8155%)
- `src/System.Management.Automation/utils/Telemetry.cs` -> **Severity: 0.616** (Embedded: 0.013 * Error Risk: 47.5062%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/Xml/Xml.psm1` -> **Severity: 5415.066** (Blast Radius: 56.048 * Doc Risk: 96.6148%)
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 3155.642** (Blast Radius: 31.593 * Doc Risk: 99.8842%)
- `src/System.Management.Automation/utils/tracing/Tracing.cs` -> **Severity: 1641.4** (Blast Radius: 16.414 * Doc Risk: 100.0%)
- `src/System.Management.Automation/engine/interpreter/Interpreter.cs` -> **Severity: 229.892** (Blast Radius: 2.299 * Doc Risk: 99.9966%)
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Extensions.cs` -> **Severity: 155.679** (Blast Radius: 13.06 * Doc Risk: 11.9203%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
