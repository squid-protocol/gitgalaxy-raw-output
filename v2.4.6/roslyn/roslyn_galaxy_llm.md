# ARCHITECTURAL_BRIEF: roslyn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/roslyn` |
| **Timestamp** | `2026-08-03T21:30:35.119365+00:00` |
| **Scan Duration** | `116.52s` |
| **Git Branch** | `main` |
| **Git Commit** | `849bed61024b171e673b9a1fac565b30e3ae1934` |
| **Git Remote** | `https://github.com/dotnet/roslyn` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 14021 malicious artifacts.

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
| Total Artifacts | 20641 |
| Analyzed Artifacts (Scanned) | 14423 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6218 |
| Total LOC | 3441496 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.9% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3171 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 127 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 13930 | 3428992 | 96.6% |
| PLAINTEXT | 222 | 1418 | 1.5% |
| MARKDOWN | 85 | 0 | 0.6% |
| YAML | 56 | 3019 | 0.4% |
| POWERSHELL | 47 | 4595 | 0.3% |
| XML | 25 | 0 | 0.2% |
| SHELL | 22 | 2082 | 0.2% |
| BATCH | 21 | 172 | 0.1% |
| JSON | 13 | 912 | 0.1% |
| PYTHON | 1 | 251 | 0.0% |
| CSV | 1 | 55 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.9`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 6452 | 44.7% |
| file_cluster_13 | 5441 | 37.7% |
| file_cluster_16 | 890 | 6.2% |
| file_cluster_0 | 652 | 4.5% |
| file_cluster_4 | 467 | 3.2% |
| file_cluster_7 | 100 | 0.7% |
| file_cluster_17 | 27 | 0.2% |
| file_cluster_15 | 26 | 0.2% |
| file_cluster_11 | 26 | 0.2% |
| file_cluster_1 | 14 | 0.1% |
| file_cluster_9 | 12 | 0.1% |
| file_cluster_6 | 5 | 0.0% |
| file_cluster_12 | 2 | 0.0% |
| file_cluster_2 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 306 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6218*

**Composition by Extension & Reason:**
- `.vb`: 3642x Unsupported Format (.vb), 1x Excluded (Machine-Generated Source Code Signature: 14598 LOC), 1x Excluded (Monolithic Amalgamation: 58132 LOC exceeds safe regex boundaries)
- `.xlf`: 913x Unsupported Format (.xlf), 4x Excluded (Saturation: Line 33 exceeds 500 chars), 3x Excluded (Saturation: Line 96 exceeds 500 chars)
- `.csproj`: 300x Unsupported Format (.csproj), 1x Excluded (Unsupported Extension: '.csproj')
- `.md`: 252x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dll`: 138x Excluded (Explicitly Denied Extension: '.dll'), 6x Excluded (Explicitly Denied Extension: '.Dll')
- `.png`: 70x Excluded (Explicitly Denied Extension: '.png')
- `.resx`: 70x Unsupported Format (.resx)
- `no_extension`: 24x Unsupported Format (.undeterminable), 16x Unsupported Format (.vsixmanifest), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 68 exceeds 500 chars)
- `.cs`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 80 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 17743 LOC)
- `.xaml`: 60x Unsupported Format (.xaml)
- `.json`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 75861 LOC exceeds safe regex boundaries)
- `.props`: 31x Unsupported Format (.props), 13x Excluded (Unsupported Extension: '.props'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vbproj`: 51x Unsupported Format (.vbproj)
- `.targets`: 21x Unsupported Format (.targets), 18x Excluded (Unsupported Extension: '.targets'), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 20.9 | 10.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 36.2 | 46.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 45.3 | 36.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.9 | 2.4 | 80.0 |
| API Exposure | 0.0 | 20.0 | 5.5 | 4.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 37.3 | 10.7 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 19.8 | 2.3 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 67.4 | 98.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 66.6 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 100.0 | 1.9 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 49.3 | 33.8 | 100.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs` (Hits: 213)
- `eng/common/SetupNugetSources.sh` (Hits: 76)
- `eng/common/tools.sh` (Hits: 54)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Diagnostics.cs** (`src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs`) — 3120 inbound connections
2. **CodeActions.cs** (`src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs`) — 662 inbound connections
3. **Formatting.cs** (`src/Compilers/CSharp/Portable/BoundTree/Formatting.cs`) — 440 inbound connections
4. **Metadata.cs** (`src/Compilers/Core/Portable/MetadataReference/Metadata.cs`) — 287 inbound connections
5. **Completion.cs** (`src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Completion.cs`) — 152 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **OrganizeUsingsTests.cs** (`src/Workspaces/CSharpTest/OrganizeImports/OrganizeUsingsTests.cs`) — 103 outbound dependencies
2. **AddUsingTests.cs** (`src/EditorFeatures/CSharpTest/CodeActions/AddUsing/AddUsingTests.cs`) — 61 outbound dependencies
3. **CommandLineTests.cs** (`src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs`) — 53 outbound dependencies
4. **PDBUsingTests.cs** (`src/Compilers/CSharp/Test/Emit2/PDB/PDBUsingTests.cs`) — 53 outbound dependencies
5. **EditorInProcess.cs** (`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/EditorInProcess.cs`) — 53 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `IsBuildOnlyDiagnostic` (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **6710.9** | LOC: 917
  * *Intent:* // Note: when adding a warning here, consider whether it should be registered as a nullability warning too
- `ParseMemberName` (@ `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`) -> Impact: **4720.3** | LOC: 1431
- `Create` (@ `src/Compilers/CSharp/Portable/Operations/CSharpOperationFactory.cs`) -> Impact: **3993.2** | LOC: 597
- `Trait` (@ `src/Features/CSharpTest/InvertIf/InvertIfTests.cs`) -> Impact: **3914.7** | LOC: 1649
- `BinaryOperators` (@ `src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs`) -> Impact: **3721.2** | LOC: 500
- `BinaryOperators` (@ `src/Compilers/CSharp/Test/Emit2/Emit/NumericIntPtrTests.cs`) -> Impact: **3519.6** | LOC: 493
- `IsTypeDeclarationContext` (@ `src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ContextQuery/SyntaxTreeExtensions.cs`) -> Impact: **3263.6** | LOC: 1097
- `Parse` (@ `src/Compilers/CSharp/Portable/CommandLine/CSharpCommandLineParser.cs`) -> Impact: **3250.1** | LOC: 983
  * *Intent:* /// <summary> /// Parses a command line. /// </summary> /// <param name="args">A collection of strings representing the command line arguments.</param...
- `ParseSwitchStatement` (@ `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`) -> Impact: **3022.7** | LOC: 1288
- `GetMemberModel` (@ `src/Compilers/CSharp/Portable/Compilation/SyntaxTreeSemanticModel.cs`) -> Impact: **2905.6** | LOC: 823

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `Recurse` (@ `src/Analyzers/CSharp/Analyzers/OrderModifiers/CSharpOrderModifiersDiagnosticAnalyzer.cs`) -> **O(2^N) [Recursive]**
- `CSharpRemoveUnnecessaryNullableDirective` (@ `src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryNullableDirective/CSharpRemoveUnnecessaryNullableDirectiveDiagnosticAnalyzer.cs`) -> **O(2^N) [Recursive]**
- `CSharpUsePrimaryConstructorDiagnosticAna` (@ `src/Analyzers/CSharp/Analyzers/UsePrimaryConstructor/CSharpUsePrimaryConstructorDiagnosticAnalyzer.cs`) -> **O(2^N) [Recursive]**
  * *Intent:* /// public C(int x, int y) /// { /// this.x = x; /// this.y = y; /// } /// } /// </code> /// and converts it to: /// <code> /// class Point(int x, int...
- `CSharpDisambiguateSameVariableCodeFixPro` (@ `src/Analyzers/CSharp/CodeFixes/DisambiguateSameVariable/CSharpDisambiguateSameVariableCodeFixProvider.cs`) -> **O(2^N) [Recursive]**
- `CSharpFixIncorrectConstraintCodeFixProvi` (@ `src/Analyzers/CSharp/CodeFixes/FixIncorrectConstraint/CSharpFixIncorrectConstraintCodeFixProvider.cs`) -> **O(2^N) [Recursive]**
- `CSharpUseAutoPropertyCodeFixProvider` (@ `src/Analyzers/CSharp/CodeFixes/UseAutoProperty/CSharpUseAutoPropertyCodeFixProvider.cs`) -> **O(2^N) [Recursive]**
- `AddOptionMapping` (@ `src/Analyzers/Core/Analyzers/IDEDiagnosticIdToOptionMappingHelper.cs`) -> **O(2^N) [Recursive]**
- `AddDebuggerDisplayAttributeArguments` (@ `src/Analyzers/Core/Analyzers/RemoveUnusedMembers/AbstractRemoveUnusedMembersDiagnosticAnalyzer.cs`) -> **O(2^N) [Recursive]**
- `ShouldAnalyze` (@ `src/Analyzers/Core/Analyzers/RemoveUnusedMembers/AbstractRemoveUnusedMembersDiagnosticAnalyzer.cs`) -> **O(2^N) [Recursive]**
- `SymbolStartAnalyzer` (@ `src/Analyzers/Core/Analyzers/RemoveUnusedParametersAndValues/AbstractRemoveUnusedParametersAndValuesDiagnosticAnalyzer.SymbolStartAnalyzer.cs`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `IsWarningSwitchEmit` (@ `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs`) -> DB Complexity: **745**
- `TernaryOperator` (@ `src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowTests.cs`) -> DB Complexity: **227**
  * *Intent:* // Whidbey bug #467493
- `TestNormalizeRawInterpolatedString` (@ `src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxNormalizerTests.cs`) -> DB Complexity: **195**
- `Exec-Process` (@ `eng/common/tools.ps1`) -> DB Complexity: **190**
  * *Intent:* # Initialize variables if they aren't already defined. # These may be defined as parameters of the importing script, or set after importing this scrip...
- `TestBadConstantValue` (@ `src/Compilers/CSharp/Test/Semantic/Semantics/ConstantTests.cs`) -> DB Complexity: **190**
- `RemoveUnusedValueAssignmentTests` (@ `src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValueAssignmentTests.cs`) -> DB Complexity: **187**
- `ParseNamespaceDeclarationCore` (@ `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`) -> DB Complexity: **167**
- `CSharpInlineDeclarationTests` (@ `src/Analyzers/CSharp/Tests/InlineDeclaration/CSharpInlineDeclarationTests.cs`) -> DB Complexity: **165**
- `GenerateEnumMemberTests` (@ `src/Analyzers/CSharp/Tests/GenerateEnumMember/GenerateEnumMemberTests.cs`) -> DB Complexity: **154**
- `MakeFieldReadonlyTests` (@ `src/Analyzers/CSharp/Tests/MakeFieldReadonly/MakeFieldReadonlyTests.cs`) -> DB Complexity: **149**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Compilers/CSharp/Test/Semantic/Semantics` | 106 | 178417.74 | 19.03% | 0.0% |
| `src/Compilers/CSharp/Test/Emit/CodeGen` | 72 | 133623.96 | 21.25% | 0.0% |
| `src/Compilers/CSharp/Test/Emit3/Semantics` | 21 | 82300.64 | 20.0% | 0.0% |
| `src/Compilers/CSharp/Test/IOperation/IOperation` | 84 | 77013.3 | 9.51% | 0.0% |
| `src/Compilers/CSharp/Portable/Binder` | 117 | 69818.12 | 29.76% | 54.02% |
| `src/Compilers/CSharp/Test/Syntax/Parsing` | 69 | 68611.18 | 6.23% | 0.0% |
| `src/EditorFeatures/CSharpTest2/Recommendations` | 150 | 55507.42 | 29.62% | 98.66% |
| `src/Compilers/CSharp/Portable/Symbols/Source` | 71 | 41909.34 | 30.02% | 57.63% |
| `src/Compilers/CSharp/Test/Symbol/Symbols` | 49 | 40546.68 | 10.45% | 0.0% |
| `src/Compilers/CSharp/Portable/Symbols` | 120 | 35002.86 | 18.42% | 64.31% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `eng/common/pipeline-logging-functions.ps1` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.sh` -> **100.0%** Exposure
- `eng/common/dotnet-install.sh` -> **100.0%** Exposure
- `eng/common/dotnet.sh` -> **100.0%** Exposure
- `eng/common/generate-sbom-prep.sh` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `.github/skills/ci-analysis/scripts/Get-CIStatus.ps1` -> **100.0%** Exposure
- `.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.ps1` -> **100.0%** Exposure
- `eng/common/darc-init.ps1` -> **100.0%** Exposure
- `eng/common/dotnet-install.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Analyzers/CSharp/Tests/GenerateMethod/GenerateMethodTests.cs` -> **218** Orphaned Functions | **32** Duplicates
- `src/Compilers/CSharp/Test/Emit3/FlowAnalysis/RegionAnalysisTests.cs` -> **248** Orphaned Functions | **2** Duplicates
- `src/Compilers/CSharp/Test/Semantic/Semantics/RefEscapingTests.cs` -> **227** Orphaned Functions | **23** Duplicates
- `src/Compilers/Test/Resources/Core/SymbolsTests/BigVisitor.cs` -> **0** Orphaned Functions | **250** Duplicates
- `src/EditorFeatures/CSharpTest/Debugging/ProximityExpressionsGetterTests.Lines.cs` -> **250** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/Compilers/CSharp/Portable/CodeGen/EmitExpression.cs`** -> AI Confidence: **99.48%**
2. **`src/Compilers/CSharp/Portable/CommandLine/CSharpCommandLineParser.cs`** -> AI Confidence: **99.48%**
3. **`src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`** -> AI Confidence: **99.48%**
4. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_UnaryOperator.cs`** -> AI Confidence: **99.48%**
5. **`src/Compilers/CSharp/Portable/Parser/Lexer.cs`** -> AI Confidence: **99.48%**
6. **`src/Compilers/CSharp/Portable/SymbolDisplay/SymbolDisplayVisitor.Members.cs`** -> AI Confidence: **99.48%**
7. **`src/Compilers/Test/Core/Compilation/ControlFlowGraphVerifier.cs`** -> AI Confidence: **99.48%**
8. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService.NodeLocator.cs`** -> AI Confidence: **99.48%**
9. **`src/VisualStudio/CSharp/Impl/LanguageService/CSharpCodeCleanupFixerDiagnosticIds.cs`** -> AI Confidence: **99.48%**
10. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SyntaxFacts/ISyntaxFacts.cs`** -> AI Confidence: **99.48%**
11. **`src/Compilers/CSharp/Portable/Binder/Binder_Crefs.cs`** -> AI Confidence: **99.39%**
12. **`src/Compilers/CSharp/Portable/Binder/ExpressionVariableFinder.cs`** -> AI Confidence: **99.39%**
13. **`src/Compilers/CSharp/Portable/Symbols/VarianceSafety.cs`** -> AI Confidence: **99.39%**
14. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowTests.cs`** -> AI Confidence: **99.39%**
15. **`src/Compilers/CSharp/Test/Semantic/Semantics/UserDefinedConversionTests.cs`** -> AI Confidence: **99.39%**
16. **`src/Compilers/CSharp/Test/Syntax/Diagnostics/DiagnosticTest.cs`** -> AI Confidence: **99.39%**
17. **`src/Compilers/Core/MSBuildTask/CommandLineBuilderExtension.cs`** -> AI Confidence: **99.39%**
18. **`src/Compilers/Core/Portable/Emit/SemanticEdit.cs`** -> AI Confidence: **99.39%**
19. **`src/Compilers/Core/Portable/Hashing/XxHashShared.cs`** -> AI Confidence: **99.39%**
20. **`src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.cs`** -> AI Confidence: **99.39%**
21. **`src/Features/CSharp/Portable/Debugging/CSharpProximityExpressionsService.Worker.cs`** -> AI Confidence: **99.39%**
22. **`src/LanguageServer/Protocol/Handler/Completion/CompletionCapabilityHelper.cs`** -> AI Confidence: **99.39%**
23. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService_Prototype.cs`** -> AI Confidence: **99.39%**
24. **`src/Compilers/CSharp/Portable/Binder/UsingStatementBinder.cs`** -> AI Confidence: **99.34%**
25. **`src/Compilers/CSharp/Portable/SymbolDisplay/SymbolDisplayVisitor.cs`** -> AI Confidence: **99.34%**
26. **`src/Compilers/CSharp/Portable/Symbols/Source/ParameterHelpers.cs`** -> AI Confidence: **99.34%**
27. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests_NullableTypes.cs`** -> AI Confidence: **99.34%**
28. **`src/Compilers/Core/CodeAnalysisTest/Collections/List/SegmentedList.Generic.Tests.Misc.cs`** -> AI Confidence: **99.34%**
29. **`src/Compilers/Core/Portable/Binding/UseSiteInfo.cs`** -> AI Confidence: **99.34%**
30. **`src/Compilers/Core/Portable/PEWriter/MetadataVisitor.cs`** -> AI Confidence: **99.34%**
31. **`src/Compilers/Core/Portable/Symbols/Attributes/MarshalAsAttributeDecoder.cs`** -> AI Confidence: **99.34%**
32. **`src/Features/CSharpTest/UseRecursivePatterns/UseRecursivePatternsRefactoringTests.cs`** -> AI Confidence: **99.34%**
33. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/PooledHashSetExtensions.cs`** -> AI Confidence: **99.34%**
34. **`src/VisualStudio/Core/Def/CodeCleanup/CommonCodeCleanUpFixerDiagnosticIds.cs`** -> AI Confidence: **99.34%**
35. **`src/Compilers/CSharp/Portable/Errors/MessageID.cs`** -> AI Confidence: **99.32%**
36. **`src/Compilers/CSharp/Test/Syntax/Parsing/ForStatementParsingTest.cs`** -> AI Confidence: **99.32%**
37. **`src/Compilers/Core/Portable/Operations/ControlFlowRegion.cs`** -> AI Confidence: **99.32%**
38. **`eng/common/SetupNugetSources.sh`** -> AI Confidence: **99.31%**
39. **`eng/common/cross/install-debs.py`** -> AI Confidence: **99.31%**
40. **`src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryNullableDirective/NullableImpactingSpanWalker.cs`** -> AI Confidence: **99.31%**
41. **`src/Analyzers/CSharp/Analyzers/UseNameofInNullableAttribute/CSharpUseNameofInNullableAttributeDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
42. **`src/Analyzers/CSharp/Analyzers/UsePatternMatching/CSharpAsAndNullCheckDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
43. **`src/Analyzers/CSharp/CodeFixes/GenerateParameterizedMember/CSharpGenerateConversionService.cs`** -> AI Confidence: **99.31%**
44. **`src/Analyzers/CSharp/CodeFixes/Nullable/CSharpDeclareAsNullableCodeFixProvider.cs`** -> AI Confidence: **99.31%**
45. **`src/Analyzers/CSharp/Tests/FileHeaders/FileHeaderTests.cs`** -> AI Confidence: **99.31%**
46. **`src/Analyzers/CSharp/Tests/PopulateSwitch/PopulateSwitchStatementTests.cs`** -> AI Confidence: **99.31%**
47. **`src/Analyzers/CSharp/Tests/UsePatternMatching/CSharpAsAndMemberAccessTests.cs`** -> AI Confidence: **99.31%**
48. **`src/Analyzers/Core/Analyzers/SimplifyInterpolation/AbstractSimplifyInterpolationHelpers.cs`** -> AI Confidence: **99.31%**
49. **`src/Analyzers/Core/Analyzers/UseConditionalExpression/ForAssignment/UseConditionalExpressionForAssignmentHelpers.cs`** -> AI Confidence: **99.31%**
50. **`src/Analyzers/Core/Analyzers/UseObjectInitializer/UseNamedMemberInitializerAnalyzer.cs`** -> AI Confidence: **99.31%**
51. **`src/Analyzers/Core/CodeFixes/GenerateMember/AbstractGenerateMemberService.cs`** -> AI Confidence: **99.31%**
52. **`src/CodeStyle/Tools/Program.cs`** -> AI Confidence: **99.31%**
53. **`src/Compilers/CSharp/CSharpAnalyzerDriver/CSharpDeclarationComputer.cs`** -> AI Confidence: **99.31%**
54. **`src/Compilers/CSharp/Portable/Binder/Binder.CapturedParametersFinder.cs`** -> AI Confidence: **99.31%**
55. **`src/Compilers/CSharp/Portable/Binder/Binder.IdentifierUsedAsValueFinder.cs`** -> AI Confidence: **99.31%**
56. **`src/Compilers/CSharp/Portable/Binder/Binder.ValueChecks.cs`** -> AI Confidence: **99.31%**
57. **`src/Compilers/CSharp/Portable/Binder/Binder.cs`** -> AI Confidence: **99.31%**
58. **`src/Compilers/CSharp/Portable/Binder/BinderFactory.BinderFactoryVisitor.cs`** -> AI Confidence: **99.31%**
59. **`src/Compilers/CSharp/Portable/Binder/Binder_AnonymousTypes.cs`** -> AI Confidence: **99.31%**
60. **`src/Compilers/CSharp/Portable/Binder/Binder_Attributes.cs`** -> AI Confidence: **99.31%**
61. **`src/Compilers/CSharp/Portable/Binder/Binder_Await.cs`** -> AI Confidence: **99.31%**
62. **`src/Compilers/CSharp/Portable/Binder/Binder_Constraints.cs`** -> AI Confidence: **99.31%**
63. **`src/Compilers/CSharp/Portable/Binder/Binder_Conversions.cs`** -> AI Confidence: **99.31%**
64. **`src/Compilers/CSharp/Portable/Binder/Binder_Deconstruct.cs`** -> AI Confidence: **99.31%**
65. **`src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs`** -> AI Confidence: **99.31%**
66. **`src/Compilers/CSharp/Portable/Binder/Binder_Initializers.cs`** -> AI Confidence: **99.31%**
67. **`src/Compilers/CSharp/Portable/Binder/Binder_InterpolatedString.cs`** -> AI Confidence: **99.31%**
68. **`src/Compilers/CSharp/Portable/Binder/Binder_Invocation.cs`** -> AI Confidence: **99.31%**
69. **`src/Compilers/CSharp/Portable/Binder/Binder_Lambda.cs`** -> AI Confidence: **99.31%**
70. **`src/Compilers/CSharp/Portable/Binder/Binder_Lookup.cs`** -> AI Confidence: **99.31%**
71. **`src/Compilers/CSharp/Portable/Binder/Binder_Operators.cs`** -> AI Confidence: **99.31%**
72. **`src/Compilers/CSharp/Portable/Binder/Binder_Patterns.cs`** -> AI Confidence: **99.31%**
73. **`src/Compilers/CSharp/Portable/Binder/Binder_Query.cs`** -> AI Confidence: **99.31%**
74. **`src/Compilers/CSharp/Portable/Binder/Binder_QueryErrors.cs`** -> AI Confidence: **99.31%**
75. **`src/Compilers/CSharp/Portable/Binder/Binder_Statements.cs`** -> AI Confidence: **99.31%**
76. **`src/Compilers/CSharp/Portable/Binder/Binder_TupleOperators.cs`** -> AI Confidence: **99.31%**
77. **`src/Compilers/CSharp/Portable/Binder/DecisionDagBuilder.cs`** -> AI Confidence: **99.31%**
78. **`src/Compilers/CSharp/Portable/Binder/DecisionDagBuilder_CheckOrReachability.cs`** -> AI Confidence: **99.31%**
79. **`src/Compilers/CSharp/Portable/Binder/ExecutableCodeBinder.cs`** -> AI Confidence: **99.31%**
80. **`src/Compilers/CSharp/Portable/Binder/ForEachLoopBinder.cs`** -> AI Confidence: **99.31%**
81. **`src/Compilers/CSharp/Portable/Binder/InMethodBinder.cs`** -> AI Confidence: **99.31%**
82. **`src/Compilers/CSharp/Portable/Binder/LocalBinderFactory.cs`** -> AI Confidence: **99.31%**
83. **`src/Compilers/CSharp/Portable/Binder/RefSafetyAnalysis.cs`** -> AI Confidence: **99.31%**
84. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/ConversionsBase.cs`** -> AI Confidence: **99.31%**
85. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedConversions.cs`** -> AI Confidence: **99.31%**
86. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedExplicitConversions.cs`** -> AI Confidence: **99.31%**
87. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedImplicitConversions.cs`** -> AI Confidence: **99.31%**
88. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/BinaryOperatorOverloadResolution.cs`** -> AI Confidence: **99.31%**
89. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/OperatorKindExtensions.cs`** -> AI Confidence: **99.31%**
90. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/UnaryOperatorOverloadResolution.cs`** -> AI Confidence: **99.31%**
91. **`src/Compilers/CSharp/Portable/Binder/Semantics/OverloadResolution/OverloadResolution.cs`** -> AI Confidence: **99.31%**
92. **`src/Compilers/CSharp/Portable/Binder/Semantics/OverloadResolution/OverloadResolutionResult.cs`** -> AI Confidence: **99.31%**
93. **`src/Compilers/CSharp/Portable/Binder/SwitchBinder.cs`** -> AI Confidence: **99.31%**
94. **`src/Compilers/CSharp/Portable/Binder/SwitchExpressionBinder.cs`** -> AI Confidence: **99.31%**
95. **`src/Compilers/CSharp/Portable/Binder/WithUsingNamespacesAndTypesBinder.cs`** -> AI Confidence: **99.31%**
96. **`src/Compilers/CSharp/Portable/BoundTree/BoundNodeExtensions.cs`** -> AI Confidence: **99.31%**
97. **`src/Compilers/CSharp/Portable/BoundTree/BoundTreeVisitors.cs`** -> AI Confidence: **99.31%**
98. **`src/Compilers/CSharp/Portable/BoundTree/VariablePendingInference.cs`** -> AI Confidence: **99.31%**
99. **`src/Compilers/CSharp/Portable/CSharpCompilationOptions.cs`** -> AI Confidence: **99.31%**
100. **`src/Compilers/CSharp/Portable/CSharpExtensions.cs`** -> AI Confidence: **99.31%**
101. **`src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`** -> AI Confidence: **99.31%**
102. **`src/Compilers/CSharp/Portable/CodeGen/EmitAddress.cs`** -> AI Confidence: **99.31%**
103. **`src/Compilers/CSharp/Portable/CodeGen/EmitStatement.cs`** -> AI Confidence: **99.31%**
104. **`src/Compilers/CSharp/Portable/Compilation/BuiltInOperators.cs`** -> AI Confidence: **99.31%**
105. **`src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`** -> AI Confidence: **99.31%**
106. **`src/Compilers/CSharp/Portable/Compilation/CSharpDiagnosticFilter.cs`** -> AI Confidence: **99.31%**
107. **`src/Compilers/CSharp/Portable/Compilation/CSharpSemanticModel.cs`** -> AI Confidence: **99.31%**
108. **`src/Compilers/CSharp/Portable/Compilation/MemberSemanticModel.NodeMapBuilder.cs`** -> AI Confidence: **99.31%**
109. **`src/Compilers/CSharp/Portable/Compilation/MemberSemanticModel.cs`** -> AI Confidence: **99.31%**
110. **`src/Compilers/CSharp/Portable/Compilation/SpeculativeSemanticModelWithMemberModel.cs`** -> AI Confidence: **99.31%**
111. **`src/Compilers/CSharp/Portable/Compilation/SyntaxTreeSemanticModel.cs`** -> AI Confidence: **99.31%**
112. **`src/Compilers/CSharp/Portable/Compiler/ClsComplianceChecker.cs`** -> AI Confidence: **99.31%**
113. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.cs`** -> AI Confidence: **99.31%**
114. **`src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`** -> AI Confidence: **99.31%**
115. **`src/Compilers/CSharp/Portable/Compiler/TypeCompilationState.cs`** -> AI Confidence: **99.31%**
116. **`src/Compilers/CSharp/Portable/Declarations/DeclarationTreeBuilder.cs`** -> AI Confidence: **99.31%**
117. **`src/Compilers/CSharp/Portable/DocumentationComments/DocumentationCommentIDVisitor.PartVisitor.cs`** -> AI Confidence: **99.31%**
118. **`src/Compilers/CSharp/Portable/FlowAnalysis/AbstractFlowPass.cs`** -> AI Confidence: **99.31%**
119. **`src/Compilers/CSharp/Portable/FlowAnalysis/DefiniteAssignment.cs`** -> AI Confidence: **99.31%**
120. **`src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`** -> AI Confidence: **99.31%**
121. **`src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker_Patterns.cs`** -> AI Confidence: **99.31%**
122. **`src/Compilers/CSharp/Portable/FlowAnalysis/VariablesDeclaredWalker.cs`** -> AI Confidence: **99.31%**
123. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ClosureConversion.cs`** -> AI Confidence: **99.31%**
124. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ExpressionLambdaRewriter.cs`** -> AI Confidence: **99.31%**
125. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/SynthesizedClosureMethod.cs`** -> AI Confidence: **99.31%**
126. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/CodeCoverageInstrumenter.cs`** -> AI Confidence: **99.31%**
127. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/ModuleCancellationInstrumenter.cs`** -> AI Confidence: **99.31%**
128. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.DecisionDagRewriter.cs`** -> AI Confidence: **99.31%**
129. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`** -> AI Confidence: **99.31%**
130. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Call.cs`** -> AI Confidence: **99.31%**
131. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_CompoundAssignmentOperator.cs`** -> AI Confidence: **99.31%**
132. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Conversion.cs`** -> AI Confidence: **99.31%**
133. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_DeconstructionAssignmentOperator.cs`** -> AI Confidence: **99.31%**
134. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Event.cs`** -> AI Confidence: **99.31%**
135. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_FixedStatement.cs`** -> AI Confidence: **99.31%**
136. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_IndexerAccess.cs`** -> AI Confidence: **99.31%**
137. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Literal.cs`** -> AI Confidence: **99.31%**
138. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Range.cs`** -> AI Confidence: **99.31%**
139. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_StringConcat.cs`** -> AI Confidence: **99.31%**
140. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_UsingStatement.cs`** -> AI Confidence: **99.31%**
141. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LoweredDynamicOperationFactory.cs`** -> AI Confidence: **99.31%**
142. **`src/Compilers/CSharp/Portable/Lowering/StateMachineRewriter/ResumableStateMachineStateAllocator.cs`** -> AI Confidence: **99.31%**
143. **`src/Compilers/CSharp/Portable/Operations/CSharpOperationFactory.cs`** -> AI Confidence: **99.31%**
144. **`src/Compilers/CSharp/Portable/Operations/CSharpOperationFactory_Methods.cs`** -> AI Confidence: **99.31%**
145. **`src/Compilers/CSharp/Portable/Parser/Directives.cs`** -> AI Confidence: **99.31%**
146. **`src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`** -> AI Confidence: **99.31%**
147. **`src/Compilers/CSharp/Portable/Parser/SyntaxParser.cs`** -> AI Confidence: **99.31%**
148. **`src/Compilers/CSharp/Portable/SymbolDisplay/SymbolDisplayVisitor_Minimal.cs`** -> AI Confidence: **99.31%**
149. **`src/Compilers/CSharp/Portable/Symbols/Attributes/AttributeData.cs`** -> AI Confidence: **99.31%**
150. **`src/Compilers/CSharp/Portable/Symbols/Attributes/PEAttributeData.cs`** -> AI Confidence: **99.31%**
151. **`src/Compilers/CSharp/Portable/Symbols/Compilation_UsedAssemblies.cs`** -> AI Confidence: **99.31%**
152. **`src/Compilers/CSharp/Portable/Symbols/Compilation_WellKnownMembers.cs`** -> AI Confidence: **99.31%**
153. **`src/Compilers/CSharp/Portable/Symbols/ConstraintsHelper.cs`** -> AI Confidence: **99.31%**
154. **`src/Compilers/CSharp/Portable/Symbols/MemberSymbolExtensions.cs`** -> AI Confidence: **99.31%**
155. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/MetadataDecoder.cs`** -> AI Confidence: **99.31%**
156. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEMethodSymbol.cs`** -> AI Confidence: **99.31%**
157. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEModuleSymbol.cs`** -> AI Confidence: **99.31%**
158. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PETypeParameterSymbol.cs`** -> AI Confidence: **99.31%**
159. **`src/Compilers/CSharp/Portable/Symbols/MetadataOrSourceAssemblySymbol.cs`** -> AI Confidence: **99.31%**
160. **`src/Compilers/CSharp/Portable/Symbols/OverriddenOrHiddenMembersHelpers.cs`** -> AI Confidence: **99.31%**
161. **`src/Compilers/CSharp/Portable/Symbols/ReferenceManager.cs`** -> AI Confidence: **99.31%**
162. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingSymbolTranslator.cs`** -> AI Confidence: **99.31%**
163. **`src/Compilers/CSharp/Portable/Symbols/Source/AttributeLocation.cs`** -> AI Confidence: **99.31%**
164. **`src/Compilers/CSharp/Portable/Symbols/Source/ExplicitInterfaceHelpers.cs`** -> AI Confidence: **99.31%**
165. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceAssemblySymbol.cs`** -> AI Confidence: **99.31%**
166. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceComplexParameterSymbol.cs`** -> AI Confidence: **99.31%**
167. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceConstructorSymbol.cs`** -> AI Confidence: **99.31%**
168. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceEventSymbol.cs`** -> AI Confidence: **99.31%**
169. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceFieldLikeEventSymbol.cs`** -> AI Confidence: **99.31%**
170. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceLocalSymbol.cs`** -> AI Confidence: **99.31%**
171. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberContainerSymbol.cs`** -> AI Confidence: **99.31%**
172. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberContainerSymbol_ImplementationChecks.cs`** -> AI Confidence: **99.31%**
173. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberFieldSymbol.cs`** -> AI Confidence: **99.31%**
174. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberMethodSymbol.cs`** -> AI Confidence: **99.31%**
175. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMethodSymbolWithAttributes.cs`** -> AI Confidence: **99.31%**
176. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceModuleSymbol.cs`** -> AI Confidence: **99.31%**
177. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol.cs`** -> AI Confidence: **99.31%**
178. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol_Bases.cs`** -> AI Confidence: **99.31%**
179. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol_Extension.cs`** -> AI Confidence: **99.31%**
180. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamespaceSymbol.AliasesAndUsings.cs`** -> AI Confidence: **99.31%**
181. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamespaceSymbol.cs`** -> AI Confidence: **99.31%**
182. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodOrUserDefinedOperatorSymbol.cs`** -> AI Confidence: **99.31%**
183. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodSymbol.cs`** -> AI Confidence: **99.31%**
184. **`src/Compilers/CSharp/Portable/Symbols/Source/SourcePropertySymbol.cs`** -> AI Confidence: **99.31%**
185. **`src/Compilers/CSharp/Portable/Symbols/Source/SourcePropertySymbolBase.cs`** -> AI Confidence: **99.31%**
186. **`src/Compilers/CSharp/Portable/Symbols/Source/TypeParameterConstraintClause.cs`** -> AI Confidence: **99.31%**
187. **`src/Compilers/CSharp/Portable/Symbols/Symbol.cs`** -> AI Confidence: **99.31%**
188. **`src/Compilers/CSharp/Portable/Symbols/SymbolExtensions.cs`** -> AI Confidence: **99.31%**
189. **`src/Compilers/CSharp/Portable/Symbols/Symbol_Attributes.cs`** -> AI Confidence: **99.31%**
190. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/Records/SynthesizedPrimaryConstructor.cs`** -> AI Confidence: **99.31%**
191. **`src/Compilers/CSharp/Portable/Symbols/Tuples/TupleTypeSymbol.cs`** -> AI Confidence: **99.31%**
192. **`src/Compilers/CSharp/Portable/Symbols/TypeSymbol.cs`** -> AI Confidence: **99.31%**
193. **`src/Compilers/CSharp/Portable/Syntax/CSharpSyntaxTree.cs`** -> AI Confidence: **99.31%**
194. **`src/Compilers/CSharp/Portable/Syntax/DirectiveTriviaSyntax.cs`** -> AI Confidence: **99.31%**
195. **`src/Compilers/CSharp/Portable/Syntax/LambdaUtilities.cs`** -> AI Confidence: **99.31%**
196. **`src/Compilers/CSharp/Portable/Syntax/SyntaxExtensions.cs`** -> AI Confidence: **99.31%**
197. **`src/Compilers/CSharp/Portable/Syntax/SyntaxFacts.cs`** -> AI Confidence: **99.31%**
198. **`src/Compilers/CSharp/Portable/Syntax/SyntaxNodeRemover.cs`** -> AI Confidence: **99.31%**
199. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenNullCoalescingAssignmentTests.cs`** -> AI Confidence: **99.31%**
200. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenOptimizedNullableOperators.cs`** -> AI Confidence: **99.31%**
201. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTryFinally.cs`** -> AI Confidence: **99.31%**
202. **`src/Compilers/CSharp/Test/Emit/CodeGen/GotoTest.cs`** -> AI Confidence: **99.31%**
203. **`src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs`** -> AI Confidence: **99.31%**
204. **`src/Compilers/CSharp/Test/Emit2/Emit/NumericIntPtrTests.cs`** -> AI Confidence: **99.31%**
205. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowDiagnosticTests.cs`** -> AI Confidence: **99.31%**
206. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternSwitchTests.cs`** -> AI Confidence: **99.31%**
207. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ICompoundAssignmentOperation.cs`** -> AI Confidence: **99.31%**
208. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IObjectCreationExpression.cs`** -> AI Confidence: **99.31%**
209. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_InvalidStatement.cs`** -> AI Confidence: **99.31%**
210. **`src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs`** -> AI Confidence: **99.31%**
211. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullableConversionTests.cs`** -> AI Confidence: **99.31%**
212. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullableTests.cs`** -> AI Confidence: **99.31%**
213. **`src/Compilers/CSharp/Test/Semantic/Semantics/StackAllocInitializerTests.cs`** -> AI Confidence: **99.31%**
214. **`src/Compilers/CSharp/Test/Semantic/Semantics/SwitchTests.cs`** -> AI Confidence: **99.31%**
215. **`src/Compilers/CSharp/Test/Semantic/Semantics/TargetTypedDefaultTests.cs`** -> AI Confidence: **99.31%**
216. **`src/Compilers/CSharp/Test/Symbol/Symbols/MissingSpecialMember.cs`** -> AI Confidence: **99.31%**
217. **`src/Compilers/CSharp/Test/Syntax/Parsing/CrefParsingTests.cs`** -> AI Confidence: **99.31%**
218. **`src/Compilers/CSharp/Test/Syntax/Parsing/NullConditionalAssignmentParsingTests.cs`** -> AI Confidence: **99.31%**
219. **`src/Compilers/CSharp/Test/Syntax/Parsing/ParsingTests.cs`** -> AI Confidence: **99.31%**
220. **`src/Compilers/CSharp/Test/Syntax/Parsing/PatternParsingTests.cs`** -> AI Confidence: **99.31%**
221. **`src/Compilers/CSharp/Test/Syntax/Parsing/StatementParsingTests.cs`** -> AI Confidence: **99.31%**
222. **`src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxTests.cs`** -> AI Confidence: **99.31%**
223. **`src/Compilers/CSharp/Test/WinRT/Metadata/WinMdDumpTest.cs`** -> AI Confidence: **99.31%**
224. **`src/Compilers/Core/CodeAnalysisTest/Collections/DebuggerAttributes.cs`** -> AI Confidence: **99.31%**
225. **`src/Compilers/Core/CodeAnalysisTest/Collections/ImmutablesTestBase.cs`** -> AI Confidence: **99.31%**
226. **`src/Compilers/Core/CodeAnalysisTest/Collections/List/IEnumerable.Generic.Tests.cs`** -> AI Confidence: **99.31%**
227. **`src/Compilers/Core/CodeAnalysisTest/Collections/SegmentedCollectionsMarshalTests.cs`** -> AI Confidence: **99.31%**
228. **`src/Compilers/Core/CodeAnalysisTest/CommonCommandLineParserTests.cs`** -> AI Confidence: **99.31%**
229. **`src/Compilers/Core/CodeAnalysisTest/DiagnosticBagTests.cs`** -> AI Confidence: **99.31%**
230. **`src/Compilers/Core/CodeAnalysisTest/FileUtilitiesTests.cs`** -> AI Confidence: **99.31%**
231. **`src/Compilers/Core/CodeAnalysisTest/MetadataReferences/MetadataHelpersTests.cs`** -> AI Confidence: **99.31%**
232. **`src/Compilers/Core/MSBuildTask/Csc.cs`** -> AI Confidence: **99.31%**
233. **`src/Compilers/Core/MSBuildTask/GenerateMSBuildEditorConfig.cs`** -> AI Confidence: **99.31%**
234. **`src/Compilers/Core/MSBuildTask/ManagedCompiler.cs`** -> AI Confidence: **99.31%**
235. **`src/Compilers/Core/MSBuildTask/Vbc.cs`** -> AI Confidence: **99.31%**
236. **`src/Compilers/Core/MSBuildTaskTests/TestUtilities/IntegrationTestBase.cs`** -> AI Confidence: **99.31%**
237. **`src/Compilers/Core/Portable/Binding/BindingDiagnosticBag.cs`** -> AI Confidence: **99.31%**
238. **`src/Compilers/Core/Portable/CodeGen/BasicBlock.cs`** -> AI Confidence: **99.31%**
239. **`src/Compilers/Core/Portable/CodeGen/ILBuilder.cs`** -> AI Confidence: **99.31%**
240. **`src/Compilers/Core/Portable/CodeGen/LocalSlotManager.cs`** -> AI Confidence: **99.31%**
241. **`src/Compilers/Core/Portable/CodeGen/SwitchIntegralJumpTableEmitter.cs`** -> AI Confidence: **99.31%**
242. **`src/Compilers/Core/Portable/CommandLine/AnalyzerConfig.SectionNameMatching.cs`** -> AI Confidence: **99.31%**
243. **`src/Compilers/Core/Portable/CommandLine/AnalyzerConfig.cs`** -> AI Confidence: **99.31%**
244. **`src/Compilers/Core/Portable/CommandLine/CommandLineArguments.cs`** -> AI Confidence: **99.31%**
245. **`src/Compilers/Core/Portable/CommandLine/CommandLineParser.cs`** -> AI Confidence: **99.31%**
246. **`src/Compilers/Core/Portable/CommandLine/CommonCompiler.cs`** -> AI Confidence: **99.31%**
247. **`src/Compilers/Core/Portable/CommandLine/SarifV1ErrorLogger.cs`** -> AI Confidence: **99.31%**
248. **`src/Compilers/Core/Portable/CommandLine/SarifV2ErrorLogger.cs`** -> AI Confidence: **99.31%**
249. **`src/Compilers/Core/Portable/Compilation/Compilation.cs`** -> AI Confidence: **99.31%**
250. **`src/Compilers/Core/Portable/Compilation/CompilationOptions.cs`** -> AI Confidence: **99.31%**
251. **`src/Compilers/Core/Portable/Compilation/DeterministicKeyBuilder.cs`** -> AI Confidence: **99.31%**
252. **`src/Compilers/Core/Portable/Compilation/SemanticModel.cs`** -> AI Confidence: **99.31%**
253. **`src/Compilers/Core/Portable/DiaSymReader/Writer/SymUnmanagedWriterImpl.cs`** -> AI Confidence: **99.31%**
254. **`src/Compilers/Core/Portable/Diagnostic/Diagnostic.cs`** -> AI Confidence: **99.31%**
255. **`src/Compilers/Core/Portable/Diagnostic/DiagnosticDescriptor.cs`** -> AI Confidence: **99.31%**
256. **`src/Compilers/Core/Portable/Diagnostic/Diagnostic_SimpleDiagnostic.cs`** -> AI Confidence: **99.31%**
257. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalysisResultBuilder.cs`** -> AI Confidence: **99.31%**
258. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerAssemblyLoader.cs`** -> AI Confidence: **99.31%**
259. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerDriver.cs`** -> AI Confidence: **99.31%**
260. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerFileReference.cs`** -> AI Confidence: **99.31%**
261. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/DiagnosticAnalysisContextHelpers.cs`** -> AI Confidence: **99.31%**
262. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/SuppressMessageAttributeState.TargetSymbolResolver.cs`** -> AI Confidence: **99.31%**
263. **`src/Compilers/Core/Portable/Emit/EditAndContinue/DefinitionMap.cs`** -> AI Confidence: **99.31%**
264. **`src/Compilers/Core/Portable/Emit/EditAndContinue/EncVariableSlotAllocator.cs`** -> AI Confidence: **99.31%**
265. **`src/Compilers/Core/Portable/Emit/EditAndContinue/SymbolChanges.cs`** -> AI Confidence: **99.31%**
266. **`src/Compilers/Core/Portable/Emit/EditAndContinueMethodDebugInformation.cs`** -> AI Confidence: **99.31%**
267. **`src/Compilers/Core/Portable/FileSystem/PathUtilities.cs`** -> AI Confidence: **99.31%**
268. **`src/Compilers/Core/Portable/Hashing/XxHash128.cs`** -> AI Confidence: **99.31%**
269. **`src/Compilers/Core/Portable/InternalUtilities/JsonWriter.cs`** -> AI Confidence: **99.31%**
270. **`src/Compilers/Core/Portable/MetadataReader/MetadataDecoder.cs`** -> AI Confidence: **99.31%**
271. **`src/Compilers/Core/Portable/MetadataReader/MetadataHelpers.cs`** -> AI Confidence: **99.31%**
272. **`src/Compilers/Core/Portable/MetadataReader/PEModule.cs`** -> AI Confidence: **99.31%**
273. **`src/Compilers/Core/Portable/MetadataReference/AssemblyIdentity.DisplayName.cs`** -> AI Confidence: **99.31%**
274. **`src/Compilers/Core/Portable/NativePdbWriter/PdbWriter.cs`** -> AI Confidence: **99.31%**
275. **`src/Compilers/Core/Portable/Operations/ControlFlowGraph.cs`** -> AI Confidence: **99.31%**
276. **`src/Compilers/Core/Portable/Operations/OperationExtensions.cs`** -> AI Confidence: **99.31%**
277. **`src/Compilers/Core/Portable/PEWriter/MetadataWriter.cs`** -> AI Confidence: **99.31%**
278. **`src/Compilers/Core/Portable/PEWriter/NativeResourceWriter.cs`** -> AI Confidence: **99.31%**
279. **`src/Compilers/Core/Portable/PEWriter/PeWriter.cs`** -> AI Confidence: **99.31%**
280. **`src/Compilers/Core/Portable/PEWriter/TypeNameSerializer.cs`** -> AI Confidence: **99.31%**
281. **`src/Compilers/Core/Portable/ReferenceManager/CommonReferenceManager.Binding.cs`** -> AI Confidence: **99.31%**
282. **`src/Compilers/Core/Portable/ReferenceManager/CommonReferenceManager.Resolution.cs`** -> AI Confidence: **99.31%**
283. **`src/Compilers/Core/Portable/ReferenceManager/CommonReferenceManager.State.cs`** -> AI Confidence: **99.31%**
284. **`src/Compilers/Core/Portable/ResourceDescription.cs`** -> AI Confidence: **99.31%**
285. **`src/Compilers/Core/Portable/RuleSet/RuleSet.cs`** -> AI Confidence: **99.31%**
286. **`src/Compilers/Core/Portable/SourceFileResolver.cs`** -> AI Confidence: **99.31%**
287. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/InputNode.cs`** -> AI Confidence: **99.31%**
288. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/PredicateSyntaxStrategy.cs`** -> AI Confidence: **99.31%**
289. **`src/Compilers/Core/Portable/StrongName/StrongNameKeys.cs`** -> AI Confidence: **99.31%**
290. **`src/Compilers/Core/Portable/Symbols/Attributes/CommonAttributeData.cs`** -> AI Confidence: **99.31%**
291. **`src/Compilers/Core/Portable/Syntax/GreenNode.cs`** -> AI Confidence: **99.31%**
292. **`src/Compilers/Core/Portable/Syntax/SyntaxDiffer.cs`** -> AI Confidence: **99.31%**
293. **`src/Compilers/Core/Portable/Syntax/SyntaxToken.cs`** -> AI Confidence: **99.31%**
294. **`src/Compilers/Core/Portable/Syntax/SyntaxTrivia.cs`** -> AI Confidence: **99.31%**
295. **`src/Compilers/Core/Portable/Text/LargeText.cs`** -> AI Confidence: **99.31%**
296. **`src/Compilers/Core/Portable/TreeDumper.cs`** -> AI Confidence: **99.31%**
297. **`src/Compilers/Server/VBCSCompiler/BuildProtocolUtil.cs`** -> AI Confidence: **99.31%**
298. **`src/Compilers/Server/VBCSCompiler/BuildServerController.cs`** -> AI Confidence: **99.31%**
299. **`src/Compilers/Server/VBCSCompiler/NamedPipeClientConnectionHost.cs`** -> AI Confidence: **99.31%**
300. **`src/Compilers/Server/VBCSCompiler/ServerDispatcher.cs`** -> AI Confidence: **99.31%**
301. **`src/Compilers/Shared/CompilerServerLogger.cs`** -> AI Confidence: **99.31%**
302. **`src/Compilers/Test/Core/CommonTestBase.cs`** -> AI Confidence: **99.31%**
303. **`src/Compilers/Test/Core/Compilation/OperationTreeVerifier.cs`** -> AI Confidence: **99.31%**
304. **`src/Compilers/Test/Core/Compilation/TestOperationVisitor.cs`** -> AI Confidence: **99.31%**
305. **`src/Compilers/Test/Core/Diagnostics/DiagnosticDescription.cs`** -> AI Confidence: **99.31%**
306. **`src/Compilers/Test/Core/Diagnostics/OperationTestAnalyzer.cs`** -> AI Confidence: **99.31%**
307. **`src/Compilers/Test/Core/Metadata/ILBuilderVisualizer.cs`** -> AI Confidence: **99.31%**
308. **`src/Compilers/Test/Core/Platform/Custom/MetadataSignatureHelper.cs`** -> AI Confidence: **99.31%**
309. **`src/Compilers/Test/Core/Platform/Custom/SigningTestHelpers.cs`** -> AI Confidence: **99.31%**
310. **`src/Compilers/Test/Utilities/CSharp/CSharpTestBase.cs`** -> AI Confidence: **99.31%**
311. **`src/Compilers/Test/Utilities/CSharp/CompilationTestUtils.cs`** -> AI Confidence: **99.31%**
312. **`src/Compilers/Test/Utilities/CSharp/CompilingTestBase.cs`** -> AI Confidence: **99.31%**
313. **`src/Compilers/Test/Utilities/CSharp/FunctionPointerUtilities.cs`** -> AI Confidence: **99.31%**
314. **`src/Dependencies/Collections/Segmented/SegmentedDictionary`2.cs`** -> AI Confidence: **99.31%**
315. **`src/Dependencies/Collections/Segmented/SegmentedHashSet`1.cs`** -> AI Confidence: **99.31%**
316. **`src/Dependencies/Collections/Segmented/SegmentedList`1.cs`** -> AI Confidence: **99.31%**
317. **`src/Dependencies/Collections/TemporaryArray`1.cs`** -> AI Confidence: **99.31%**
318. **`src/Dependencies/Threading/AsyncBatchingWorkQueue`2.cs`** -> AI Confidence: **99.31%**
319. **`src/EditorFeatures/CSharp/CompleteStatement/CompleteStatementCommandHandler.cs`** -> AI Confidence: **99.31%**
320. **`src/EditorFeatures/CSharpTest2/Recommendations/RecommenderTests.cs`** -> AI Confidence: **99.31%**
321. **`src/EditorFeatures/Core/EditorConfigSettings/Updater/SettingsUpdateHelper.cs`** -> AI Confidence: **99.31%**
322. **`src/EditorFeatures/Core/Preview/SolutionPreviewResult.cs`** -> AI Confidence: **99.31%**
323. **`src/EditorFeatures/Core/Tagging/TaggerMainThreadManager.cs`** -> AI Confidence: **99.31%**
324. **`src/EditorFeatures/Test/Utilities/StackFrameUtils.cs`** -> AI Confidence: **99.31%**
325. **`src/EditorFeatures/TestUtilities/Workspaces/EditorTestHostDocument.cs`** -> AI Confidence: **99.31%**
326. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/DkmUtilities.cs`** -> AI Confidence: **99.31%**
327. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/MetadataUtilities.cs`** -> AI Confidence: **99.31%**
328. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PDB/MethodDebugInfo.Native.cs`** -> AI Confidence: **99.31%**
329. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PDB/MethodDebugInfo.Portable.cs`** -> AI Confidence: **99.31%**
330. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Formatter.Values.cs`** -> AI Confidence: **99.31%**
331. **`src/Features/CSharp/Portable/BraceCompletion/CurlyBraceCompletionService.cs`** -> AI Confidence: **99.31%**
332. **`src/Features/CSharp/Portable/Completion/CompletionProviders/OverrideCompletionProvider.cs`** -> AI Confidence: **99.31%**
333. **`src/Features/CSharp/Portable/Completion/Providers/ContextVariableArgumentProvider.cs`** -> AI Confidence: **99.31%**
334. **`src/Features/CSharp/Portable/ConvertForToForEach/CSharpConvertForToForEachCodeRefactoringProvider.cs`** -> AI Confidence: **99.31%**
335. **`src/Features/CSharp/Portable/Diagnostics/Analyzers/TypeSyntaxSimplifierWalker.cs`** -> AI Confidence: **99.31%**
336. **`src/Features/CSharp/Portable/DocumentationComments/CSharpDocumentationCommentSnippetService.cs`** -> AI Confidence: **99.31%**
337. **`src/Features/CSharp/Portable/EditAndContinue/BreakpointSpans.cs`** -> AI Confidence: **99.31%**
338. **`src/Features/CSharp/Portable/EditAndContinue/CSharpEditAndContinueAnalyzer.cs`** -> AI Confidence: **99.31%**
339. **`src/Features/CSharp/Portable/EditAndContinue/DeclarationBody/PropertyOrIndexerAccessorDeclarationBody.cs`** -> AI Confidence: **99.31%**
340. **`src/Features/CSharp/Portable/EditAndContinue/SyntaxComparer.cs`** -> AI Confidence: **99.31%**
341. **`src/Features/CSharp/Portable/ExtractMethod/Extensions.cs`** -> AI Confidence: **99.31%**
342. **`src/Features/CSharp/Portable/GoToDefinition/CSharpGoToDefinitionSymbolService.cs`** -> AI Confidence: **99.31%**
343. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/LoopHighlighter.cs`** -> AI Confidence: **99.31%**
344. **`src/Features/CSharp/Portable/QuickInfo/CSharpSyntacticQuickInfoProvider.cs`** -> AI Confidence: **99.31%**
345. **`src/Features/CSharpTest/ConvertIfToSwitch/ConvertIfToSwitchTests.cs`** -> AI Confidence: **99.31%**
346. **`src/Features/CSharpTest/InvertIf/InvertIfTests.cs`** -> AI Confidence: **99.31%**
347. **`src/Features/Core/Portable/Completion/CompletionItem.cs`** -> AI Confidence: **99.31%**
348. **`src/Features/Core/Portable/DocumentationComments/AbstractDocumentationCommentFormattingService.cs`** -> AI Confidence: **99.31%**
349. **`src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs`** -> AI Confidence: **99.31%**
350. **`src/Features/Core/Portable/EmbeddedLanguages/Json/JsonParser.StrictSyntaxChecker.cs`** -> AI Confidence: **99.31%**
351. **`src/Features/Core/Portable/EmbeddedLanguages/Json/LanguageServices/JsonClassifier.cs`** -> AI Confidence: **99.31%**
352. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexEmbeddedCompletionProvider.cs`** -> AI Confidence: **99.31%**
353. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/RegexParser.CaptureInfoAnalyzer.cs`** -> AI Confidence: **99.31%**
354. **`src/Features/Core/Portable/FindUsages/DefinitionItem.cs`** -> AI Confidence: **99.31%**
355. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.State.cs`** -> AI Confidence: **99.31%**
356. **`src/Features/Core/Portable/PdbSourceDocument/PdbFileLocatorService.cs`** -> AI Confidence: **99.31%**
357. **`src/Features/Core/Portable/QuickInfo/Presentation/QuickInfoContentBuilder.cs`** -> AI Confidence: **99.31%**
358. **`src/Features/Core/Portable/Shared/Extensions/ISymbolExtensions_2.cs`** -> AI Confidence: **99.31%**
359. **`src/Features/Core/Portable/SolutionExplorer/ISolutionExplorerSymbolTreeItemProvider.cs`** -> AI Confidence: **99.31%**
360. **`src/Features/Core/Portable/SpellCheck/AbstractSpellCheckSpanService.cs`** -> AI Confidence: **99.31%**
361. **`src/Features/DiagnosticsTestUtilities/CodeActions/CodeFixVerifierHelper.cs`** -> AI Confidence: **99.31%**
362. **`src/Features/TestUtilities/EditAndContinue/MockEditAndContinueService.cs`** -> AI Confidence: **99.31%**
363. **`src/Interactive/Host/Interactive/Core/InteractiveHost.LazyRemoteService.cs`** -> AI Confidence: **99.31%**
364. **`src/Interactive/Host/Interactive/Core/InteractiveHost.RemoteService.cs`** -> AI Confidence: **99.31%**
365. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LoadedProject.cs`** -> AI Confidence: **99.31%**
366. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/Logging/RoslynLogger.cs`** -> AI Confidence: **99.31%**
367. **`src/LanguageServer/Protocol/Handler/Definitions/AbstractGoToDefinitionHandler.cs`** -> AI Confidence: **99.31%**
368. **`src/LanguageServer/Protocol/Protocol/Converters/FormattingOptionsConverter.cs`** -> AI Confidence: **99.31%**
369. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompareSymbolsCorrectlyAnalyzer.cs`** -> AI Confidence: **99.31%**
370. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompilerExtensionTargetFrameworkAnalyzer.cs`** -> AI Confidence: **99.31%**
371. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticAnalyzerAttributeAnalyzer.cs`** -> AI Confidence: **99.31%**
372. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticAnalyzerFieldsAnalyzer.cs`** -> AI Confidence: **99.31%**
373. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticDescriptorCreationAnalyzer_IdRangeAndCategoryValidation.cs`** -> AI Confidence: **99.31%**
374. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticDescriptorCreationAnalyzer_ReleaseTracking.cs`** -> AI Confidence: **99.31%**
375. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/Fixers/AnalyzerReleaseTrackingFix.cs`** -> AI Confidence: **99.31%**
376. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/RegisterActionAnalyzer.cs`** -> AI Confidence: **99.31%**
377. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/ReleaseTrackingHelper.cs`** -> AI Confidence: **99.31%**
378. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/ReportDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
379. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.BannedApiAnalyzers/Core/SymbolIsBannedAnalyzerBase.cs`** -> AI Confidence: **99.31%**
380. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.ResxSourceGenerator/Microsoft.CodeAnalysis.ResxSourceGenerator/AbstractResxGenerator.cs`** -> AI Confidence: **99.31%**
381. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/TypeConversionAllocationAnalyzer.cs`** -> AI Confidence: **99.31%**
382. **`src/RoslynAnalyzers/PublicApiAnalyzers/Core/CodeFixes/AnnotatePublicApiFix.cs`** -> AI Confidence: **99.31%**
383. **`src/RoslynAnalyzers/PublicApiAnalyzers/Core/CodeFixes/DeclarePublicApiFix.cs`** -> AI Confidence: **99.31%**
384. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/AbstractDoNotCopyValue.cs`** -> AI Confidence: **99.31%**
385. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/SymbolDeclaredEventMustBeGeneratedForSourceSymbols.cs`** -> AI Confidence: **99.31%**
386. **`src/RoslynAnalyzers/Tools/GenerateDocumentationAndConfigFiles/CodeFixerExtensions.cs`** -> AI Confidence: **99.31%**
387. **`src/RoslynAnalyzers/Tools/Metrics/MetricsOutputWriter.cs`** -> AI Confidence: **99.31%**
388. **`src/RoslynAnalyzers/Tools/Metrics/Program.cs`** -> AI Confidence: **99.31%**
389. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/MetricsHelper.cs`** -> AI Confidence: **99.31%**
390. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/DiagnosticExtensions.cs`** -> AI Confidence: **99.31%**
391. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/IMethodSymbolExtensions.cs`** -> AI Confidence: **99.31%**
392. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/IOperationExtensions.cs`** -> AI Confidence: **99.31%**
393. **`src/RoslynAnalyzers/Utilities/Compiler/Options/SymbolNamesWithValueOption.cs`** -> AI Confidence: **99.31%**
394. **`src/RoslynAnalyzers/Utilities/Compiler/RulesetToEditorconfigConverter.cs`** -> AI Confidence: **99.31%**
395. **`src/RoslynAnalyzers/Utilities/Compiler/WellKnownTypeProvider.cs`** -> AI Confidence: **99.31%**
396. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/CopyAnalysis/CopyAnalysisContext.cs`** -> AI Confidence: **99.31%**
397. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/GlobalFlowStateAnalysis/GlobalFlowStateAnalysis.GlobalFlowStateAnalysisValueSetDomain.cs`** -> AI Confidence: **99.31%**
398. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/HazardousUsageEvaluatorCollection.cs`** -> AI Confidence: **99.31%**
399. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/PropertySetAnalysis.PropertySetDataFlowOperationVisitor.cs`** -> AI Confidence: **99.31%**
400. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/PropertySetAnalysis.cs`** -> AI Confidence: **99.31%**
401. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataAnalysisContext.cs`** -> AI Confidence: **99.31%**
402. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataConfig.cs`** -> AI Confidence: **99.31%**
403. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataSymbolMap.cs`** -> AI Confidence: **99.31%**
404. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataSymbolMapExtensions.cs`** -> AI Confidence: **99.31%**
405. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/ValueContentAnalysis/ValueContentAbstractValue.cs`** -> AI Confidence: **99.31%**
406. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/ValueContentAnalysis/ValueContentAnalysisContext.cs`** -> AI Confidence: **99.31%**
407. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AbstractDataFlowAnalysisContext.cs`** -> AI Confidence: **99.31%**
408. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AnalysisEntityFactory.cs`** -> AI Confidence: **99.31%**
409. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowAnalysis.cs`** -> AI Confidence: **99.31%**
410. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`** -> AI Confidence: **99.31%**
411. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/LValueFlowCapturesProvider.cs`** -> AI Confidence: **99.31%**
412. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/PredicatedAnalysisData.cs`** -> AI Confidence: **99.31%**
413. **`src/Scripting/Core/Hosting/AssemblyLoader/InteractiveAssemblyLoader.cs`** -> AI Confidence: **99.31%**
414. **`src/Scripting/Core/Hosting/AssemblyLoader/MetadataShadowCopyProvider.cs`** -> AI Confidence: **99.31%**
415. **`src/Scripting/Core/Hosting/CommandLine/CommandLineRunner.cs`** -> AI Confidence: **99.31%**
416. **`src/Scripting/Core/Hosting/ObjectFormatter/CommonObjectFormatter.Visitor.cs`** -> AI Confidence: **99.31%**
417. **`src/Scripting/Core/Hosting/ObjectFormatter/CommonTypeNameFormatter.cs`** -> AI Confidence: **99.31%**
418. **`src/Scripting/Core/Hosting/Resolvers/RuntimeMetadataReferenceResolver.cs`** -> AI Confidence: **99.31%**
419. **`src/Tools/Source/CompilerGeneratorTools/Source/IOperationGenerator/IOperationClassWriter.cs`** -> AI Confidence: **99.31%**
420. **`src/Tools/Source/RunTests/ProcessRunner.cs`** -> AI Confidence: **99.31%**
421. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService.CodeModelEventCollector.cs`** -> AI Confidence: **99.31%**
422. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService.cs`** -> AI Confidence: **99.31%**
423. **`src/VisualStudio/CSharp/Impl/LanguageService/CSharpHelpContextService.cs`** -> AI Confidence: **99.31%**
424. **`src/VisualStudio/CSharp/Impl/ObjectBrowser/DescriptionBuilder.cs`** -> AI Confidence: **99.31%**
425. **`src/VisualStudio/Core/Def/ChangeSignature/AddParameterDialogViewModel.cs`** -> AI Confidence: **99.31%**
426. **`src/VisualStudio/Core/Def/LanguageService/AbstractLanguageService`2.IVsLanguageDebugInfo.cs`** -> AI Confidence: **99.31%**
427. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/ObjectList.cs`** -> AI Confidence: **99.31%**
428. **`src/VisualStudio/Core/Def/NavigationBar/NavigationBarClient.cs`** -> AI Confidence: **99.31%**
429. **`src/VisualStudio/Core/Def/Options/VisualStudioSettingsOptionPersister.cs`** -> AI Confidence: **99.31%**
430. **`src/VisualStudio/Core/Def/PdbSourceDocument/AbstractSourceLinkService.cs`** -> AI Confidence: **99.31%**
431. **`src/VisualStudio/Core/Def/Preview/TopLevelChange.cs`** -> AI Confidence: **99.31%**
432. **`src/VisualStudio/Core/Def/PreviewPane/PreviewPane.xaml.cs`** -> AI Confidence: **99.31%**
433. **`src/VisualStudio/Core/Def/Utilities/AutomationDelegatingListView.cs`** -> AI Confidence: **99.31%**
434. **`src/VisualStudio/Core/Impl/CodeModel/FileCodeModel_Events.cs`** -> AI Confidence: **99.31%**
435. **`src/VisualStudio/Core/Impl/CodeModel/ICodeModelService.cs`** -> AI Confidence: **99.31%**
436. **`src/VisualStudio/Core/Test.Next/Options/VisualStudioStorageReadFallbackTests.cs`** -> AI Confidence: **99.31%**
437. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/IdeTestCaseRunner.cs`** -> AI Confidence: **99.31%**
438. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/InProcessIdeTestInvoker.cs`** -> AI Confidence: **99.31%**
439. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/QuickInfoToStringConverter.cs`** -> AI Confidence: **99.31%**
440. **`src/Workspaces/CSharp/Portable/Classification/ClassificationHelpers.cs`** -> AI Confidence: **99.31%**
441. **`src/Workspaces/CSharp/Portable/Classification/Worker.cs`** -> AI Confidence: **99.31%**
442. **`src/Workspaces/CSharp/Portable/Rename/CSharpRenameRewriterLanguageService.cs`** -> AI Confidence: **99.31%**
443. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpEscapingReducer.cs`** -> AI Confidence: **99.31%**
444. **`src/Workspaces/Core/Portable/CodeFixes/CodeFixContext.cs`** -> AI Confidence: **99.31%**
445. **`src/Workspaces/Core/Portable/Diagnostics/DiagnosticAnalysisResultBuilder.cs`** -> AI Confidence: **99.31%**
446. **`src/Workspaces/Core/Portable/Diagnostics/DiagnosticData.cs`** -> AI Confidence: **99.31%**
447. **`src/Workspaces/Core/Portable/FindSymbols/SyntaxTree/SyntaxTreeIndex_Persistence.cs`** -> AI Confidence: **99.31%**
448. **`src/Workspaces/Core/Portable/Formatting/Formatter.cs`** -> AI Confidence: **99.31%**
449. **`src/Workspaces/Core/Portable/ObsoleteSymbol/AbstractObsoleteSymbolService.cs`** -> AI Confidence: **99.31%**
450. **`src/Workspaces/Core/Portable/Recommendations/AbstractRecommendationServiceRunner.cs`** -> AI Confidence: **99.31%**
451. **`src/Workspaces/Core/Portable/Shared/Extensions/SemanticModelExtensions.cs`** -> AI Confidence: **99.31%**
452. **`src/Workspaces/Core/Portable/Shared/Extensions/SyntaxGeneratorExtensions.cs`** -> AI Confidence: **99.31%**
453. **`src/Workspaces/Core/Portable/Shared/Utilities/DocumentationComment.cs`** -> AI Confidence: **99.31%**
454. **`src/Workspaces/Core/Portable/Workspace/Host/TemporaryStorage/LegacyTemporaryStorageService.cs`** -> AI Confidence: **99.31%**
455. **`src/Workspaces/CoreTest/CodeCleanup/ReduceTokenTests.cs`** -> AI Confidence: **99.31%**
456. **`src/Workspaces/CoreTestUtilities/Workspaces/TestWorkspace.cs`** -> AI Confidence: **99.31%**
457. **`src/Workspaces/MSBuild/Core/MSBuild/BuildHostProcessManager.cs`** -> AI Confidence: **99.31%**
458. **`src/Workspaces/MSBuild/Core/MSBuild/MSBuildWorkspace.cs`** -> AI Confidence: **99.31%**
459. **`src/Workspaces/Remote/Core/Serialization/MessagePackFormatters.cs`** -> AI Confidence: **99.31%**
460. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/EmbeddedLanguages/VirtualChars/CSharpVirtualCharService.cs`** -> AI Confidence: **99.31%**
461. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/ExpressionSyntaxExtensions.cs`** -> AI Confidence: **99.31%**
462. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/ParenthesizedExpressionSyntaxExtensions.cs`** -> AI Confidence: **99.31%**
463. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/SemanticModelExtensions.cs`** -> AI Confidence: **99.31%**
464. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/SyntaxTokenExtensions.cs`** -> AI Confidence: **99.31%**
465. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/ElasticTriviaFormattingRule.cs`** -> AI Confidence: **99.31%**
466. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/IndentBlockFormattingRule.cs`** -> AI Confidence: **99.31%**
467. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/SpacingFormattingRule.cs`** -> AI Confidence: **99.31%**
468. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/SuppressFormattingRule.cs`** -> AI Confidence: **99.31%**
469. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/TokenBasedFormattingRule.cs`** -> AI Confidence: **99.31%**
470. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Services/SyntaxFacts/CSharpSyntaxFacts.cs`** -> AI Confidence: **99.31%**
471. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Utilities/FormattingRangeHelper.cs`** -> AI Confidence: **99.31%**
472. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Extensions/OperationExtensions.cs`** -> AI Confidence: **99.31%**
473. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/FlowAnalysis/SymbolUsageAnalysis/SymbolUsageAnalysis.Walker.cs`** -> AI Confidence: **99.31%**
474. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/EditorConfig/EditorConfigNamingStyleParser_SymbolSpec.cs`** -> AI Confidence: **99.31%**
475. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Serialization/ObjectWriter.cs`** -> AI Confidence: **99.31%**
476. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/RefactoringHelpers/AbstractRefactoringHelpers.cs`** -> AI Confidence: **99.31%**
477. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/AsyncLazy`1.cs`** -> AI Confidence: **99.31%**
478. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/SpecializedTasks.cs`** -> AI Confidence: **99.31%**
479. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Extensions/Compilation/CompilationExtensions.cs`** -> AI Confidence: **99.31%**
480. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Extensions/Symbols/ITypeSymbolExtensions.cs`** -> AI Confidence: **99.31%**
481. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/CodeGeneration/EnumMemberGenerator.cs`** -> AI Confidence: **99.31%**
482. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/CodeGeneration/NamedTypeGenerator.cs`** -> AI Confidence: **99.31%**
483. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ContextQuery/SyntaxTreeExtensions.cs`** -> AI Confidence: **99.31%**
484. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/SyntaxGeneratorExtensions_CreateEqualsMethod.cs`** -> AI Confidence: **99.31%**
485. **`.github/skills/ci-analysis/scripts/Get-CIStatus.ps1`** -> AI Confidence: **99.29%**
486. **`.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1`** -> AI Confidence: **99.29%**
487. **`eng/common/dotnet-install.ps1`** -> AI Confidence: **99.29%**
488. **`eng/common/dotnet.ps1`** -> AI Confidence: **99.29%**
489. **`eng/common/generate-locproject.ps1`** -> AI Confidence: **99.29%**
490. **`eng/common/internal-feed-operations.ps1`** -> AI Confidence: **99.29%**
491. **`eng/common/pipeline-logging-functions.ps1`** -> AI Confidence: **99.29%**
492. **`eng/common/sdk-task.ps1`** -> AI Confidence: **99.29%**
493. **`eng/common/sdl/configure-sdl-tool.ps1`** -> AI Confidence: **99.29%**
494. **`eng/common/sdl/execute-all-sdl-tools.ps1`** -> AI Confidence: **99.29%**
495. **`eng/common/sdl/extract-artifact-packages.ps1`** -> AI Confidence: **99.29%**
496. **`eng/common/vmr-sync.ps1`** -> AI Confidence: **99.29%**
497. **`eng/todo-check.ps1`** -> AI Confidence: **99.29%**
498. **`eng/validate-code-formatting.ps1`** -> AI Confidence: **99.29%**
499. **`eng/validate-rules-missing-documentation.ps1`** -> AI Confidence: **99.29%**
500. **`scripts/PublicApi/mark-shipped.ps1`** -> AI Confidence: **99.29%**
501. **`scripts/UploadAzureZip/CreateAndUploadNugetZip.ps1`** -> AI Confidence: **99.29%**
502. **`scripts/UploadAzureZip/UploadPerfProject.ps1`** -> AI Confidence: **99.29%**
503. **`scripts/cleanup_perf.ps1`** -> AI Confidence: **99.29%**
504. **`src/RoslynAnalyzers/assets/install.ps1`** -> AI Confidence: **99.29%**
505. **`src/RoslynAnalyzers/assets/uninstall.ps1`** -> AI Confidence: **99.29%**
506. **`src/Setup/PowerShell/install.ps1`** -> AI Confidence: **99.29%**
507. **`src/Setup/PowerShell/uninstall.ps1`** -> AI Confidence: **99.29%**
508. **`eng/common/init-tools-native.sh`** -> AI Confidence: **99.29%**
509. **`src/Compilers/CSharp/Portable/Binder/EarlyWellKnownAttributeBinder.cs`** -> AI Confidence: **99.29%**
510. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/ConversionKindExtensions.cs`** -> AI Confidence: **99.29%**
511. **`src/Compilers/CSharp/Portable/BoundTree/BoundAwaitableInfo.cs`** -> AI Confidence: **99.29%**
512. **`src/Compilers/CSharp/Portable/BoundTree/BoundConversion.cs`** -> AI Confidence: **99.29%**
513. **`src/Compilers/CSharp/Portable/BoundTree/BoundNode_Source.cs`** -> AI Confidence: **99.29%**
514. **`src/Compilers/CSharp/Portable/Errors/ErrorCode.cs`** -> AI Confidence: **99.29%**
515. **`src/Compilers/CSharp/Portable/Generated/ErrorFacts.Generated.cs`** -> AI Confidence: **99.29%**
516. **`src/Compilers/CSharp/Portable/Parser/Lexer_StringLiteral.cs`** -> AI Confidence: **99.29%**
517. **`src/Compilers/CSharp/Portable/Symbols/SpecialTypeExtensions.cs`** -> AI Confidence: **99.29%**
518. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IConditionalAccessExpression.cs`** -> AI Confidence: **99.29%**
519. **`src/Compilers/Core/Portable/CodeGen/ILBuilderConversions.cs`** -> AI Confidence: **99.29%**
520. **`src/Compilers/Core/Portable/CodeGen/ILOpCodeExtensions.cs`** -> AI Confidence: **99.29%**
521. **`src/Compilers/Core/Portable/GlobalSuppressions.cs`** -> AI Confidence: **99.29%**
522. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/NodeExtensions.cs`** -> AI Confidence: **99.29%**
523. **`src/Compilers/Test/Core/ThrowingTraceListener.cs`** -> AI Confidence: **99.29%**
524. **`src/Dependencies/Collections/Internal/SR.cs`** -> AI Confidence: **99.29%**
525. **`src/EditorFeatures/CSharpTest2/EmbeddedLanguages/RegularExpressions/CSharpRegexParserTests_ReferenceTests.cs`** -> AI Confidence: **99.29%**
526. **`src/EditorFeatures/TestUtilities/SignatureHelp/SignatureHelpTestItem.cs`** -> AI Confidence: **99.29%**
527. **`src/EditorFeatures/TestUtilities/Workspaces/EditorTestHostProject.cs`** -> AI Confidence: **99.29%**
528. **`src/Features/ExternalAccess/OmniSharp.CSharp/Formatting/OmniSharpSyntaxFormattingOptionsFactory.cs`** -> AI Confidence: **99.29%**
529. **`src/LanguageServer/Protocol/Protocol/Methods.Document.cs`** -> AI Confidence: **99.29%**
530. **`src/LanguageServer/Protocol/Protocol/Methods.Navigation.cs`** -> AI Confidence: **99.29%**
531. **`src/LanguageServer/Protocol/Protocol/Methods.Workspace.cs`** -> AI Confidence: **99.29%**
532. **`src/LanguageServer/Protocol/Protocol/TextDocumentClientCapabilities.cs`** -> AI Confidence: **99.29%**
533. **`src/RoslynAnalyzers/Utilities/Compiler/DiagnosticHelpers.cs`** -> AI Confidence: **99.29%**
534. **`src/Workspaces/CSharp/Portable/Classification/Worker_Preprocesser.cs`** -> AI Confidence: **99.29%**
535. **`src/Workspaces/Core/Portable/Workspace/Host/PersistentStorage/IChecksummedPersistentStorage.cs`** -> AI Confidence: **99.29%**
536. **`src/Workspaces/CoreTest/UtilityTest/StringEscapingTests.cs`** -> AI Confidence: **99.29%**
537. **`src/Workspaces/Remote/ServiceHub/Host/ThrowingTraceListener.cs`** -> AI Confidence: **99.29%**
538. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SemanticFacts/ForEachSymbols.cs`** -> AI Confidence: **99.29%**
539. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SyntaxFacts/ISyntaxKinds.cs`** -> AI Confidence: **99.29%**
540. **`src/Analyzers/CSharp/Analyzers/UseCollectionExpression/UseCollectionExpressionHelpers.cs`** -> AI Confidence: **99.25%**
541. **`src/EditorFeatures/CSharp/StringCopyPaste/StringCopyPasteHelpers.cs`** -> AI Confidence: **99.25%**
542. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowAnalysisResult.cs`** -> AI Confidence: **99.25%**
543. **`src/Analyzers/CSharp/Analyzers/AddBraces/CSharpAddBracesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
544. **`src/Analyzers/CSharp/Analyzers/InlineDeclaration/CSharpInlineDeclarationDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
545. **`src/Analyzers/CSharp/Analyzers/MakeStructMemberReadOnly/CSharpMakeStructMemberReadOnlyAnalyzer.cs`** -> AI Confidence: **99.24%**
546. **`src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryLambdaExpression/CSharpRemoveUnnecessaryLambdaExpressionDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
547. **`src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryNullableDirective/CSharpRemoveUnnecessaryNullableDirectiveDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
548. **`src/Analyzers/CSharp/Analyzers/UseAutoProperty/CSharpUseAutoPropertyAnalyzer.cs`** -> AI Confidence: **99.24%**
549. **`src/Analyzers/CSharp/Analyzers/UseCollectionExpression/CSharpUseCollectionExpressionForBuilderDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
550. **`src/Analyzers/CSharp/CodeFixes/ConvertToRecord/ConvertToRecordEngine.cs`** -> AI Confidence: **99.24%**
551. **`src/Analyzers/CSharp/CodeFixes/ConvertToRecord/ConvertToRecordHelpers.cs`** -> AI Confidence: **99.24%**
552. **`src/Analyzers/CSharp/CodeFixes/GenerateConstructor/CSharpGenerateConstructorService.cs`** -> AI Confidence: **99.24%**
553. **`src/Analyzers/CSharp/CodeFixes/GenerateMethod/GenerateDeconstructMethodCodeFixProvider.cs`** -> AI Confidence: **99.24%**
554. **`src/Analyzers/CSharp/CodeFixes/ReplaceDefaultLiteral/CSharpReplaceDefaultLiteralCodeFixProvider.cs`** -> AI Confidence: **99.24%**
555. **`src/Analyzers/CSharp/Tests/AddRequiredParentheses/AddRequiredPatternParenthesesTests.cs`** -> AI Confidence: **99.24%**
556. **`src/Analyzers/CSharp/Tests/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionTests.cs`** -> AI Confidence: **99.24%**
557. **`src/Analyzers/CSharp/Tests/NewLines/ConsecutiveStatementPlacement/ConsecutiveStatementPlacementTests.cs`** -> AI Confidence: **99.24%**
558. **`src/Analyzers/CSharp/Tests/RemoveUnnecessaryParentheses/RemoveUnnecessaryPatternParenthesesTests.cs`** -> AI Confidence: **99.24%**
559. **`src/Analyzers/CSharp/Tests/ReplaceDefaultLiteral/ReplaceDefaultLiteralTests.cs`** -> AI Confidence: **99.24%**
560. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForNullableTernaryConditionalCheckTests.cs`** -> AI Confidence: **99.24%**
561. **`src/Analyzers/CSharp/Tests/UseConditionalExpression/UseConditionalExpressionForAssignmentTests.cs`** -> AI Confidence: **99.24%**
562. **`src/Analyzers/CSharp/Tests/UseNullPropagation/UseNullPropagationTests.cs`** -> AI Confidence: **99.24%**
563. **`src/Analyzers/Core/Analyzers/Helpers/DiagnosticHelper.cs`** -> AI Confidence: **99.24%**
564. **`src/Analyzers/Core/Analyzers/RemoveUnnecessarySuppressions/AbstractRemoveUnnecessaryPragmaSuppressionsDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
565. **`src/Analyzers/Core/Analyzers/RemoveUnusedMembers/AbstractRemoveUnusedMembersDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
566. **`src/Analyzers/Core/Analyzers/SimplifyBooleanExpression/AbstractSimplifyConditionalDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
567. **`src/Analyzers/Core/Analyzers/SimplifyLinqExpression/AbstractSimplifyLinqExpressionDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
568. **`src/Analyzers/Core/Analyzers/UseCollectionInitializer/AbstractUseCollectionInitializerAnalyzer.cs`** -> AI Confidence: **99.24%**
569. **`src/Compilers/CSharp/Portable/Binder/Binder.WithQueryLambdaParametersBinder.cs`** -> AI Confidence: **99.24%**
570. **`src/Compilers/CSharp/Portable/Binder/Binder_Symbols.cs`** -> AI Confidence: **99.24%**
571. **`src/Compilers/CSharp/Portable/BoundTree/UnboundLambda.cs`** -> AI Confidence: **99.24%**
572. **`src/Compilers/CSharp/Portable/CodeGen/Optimizer.cs`** -> AI Confidence: **99.24%**
573. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.DocumentationCommentWalker.cs`** -> AI Confidence: **99.24%**
574. **`src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`** -> AI Confidence: **99.24%**
575. **`src/Compilers/CSharp/Portable/Emitter/NoPia/EmbeddedTypesManager.cs`** -> AI Confidence: **99.24%**
576. **`src/Compilers/CSharp/Portable/Lowering/AsyncRewriter/AsyncMethodToStateMachineRewriter.cs`** -> AI Confidence: **99.24%**
577. **`src/Compilers/CSharp/Portable/Lowering/BoundTreeToDifferentEnclosingContextRewriter.cs`** -> AI Confidence: **99.24%**
578. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ClosureConversion.Analysis.cs`** -> AI Confidence: **99.24%**
579. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/LambdaCapturedVariable.cs`** -> AI Confidence: **99.24%**
580. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/DebugInfoInjector.cs`** -> AI Confidence: **99.24%**
581. **`src/Compilers/CSharp/Portable/Lowering/StateMachineRewriter/StateMachineRewriter.cs`** -> AI Confidence: **99.24%**
582. **`src/Compilers/CSharp/Portable/Parser/SlidingTextWindow.cs`** -> AI Confidence: **99.24%**
583. **`src/Compilers/CSharp/Portable/Symbols/AssemblySymbol.cs`** -> AI Confidence: **99.24%**
584. **`src/Compilers/CSharp/Portable/Symbols/FunctionPointers/FunctionPointerMethodSymbol.cs`** -> AI Confidence: **99.24%**
585. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEFieldSymbol.cs`** -> AI Confidence: **99.24%**
586. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PENamedTypeSymbol.cs`** -> AI Confidence: **99.24%**
587. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PENamespaceSymbol.cs`** -> AI Confidence: **99.24%**
588. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEParameterSymbol.cs`** -> AI Confidence: **99.24%**
589. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEPropertySymbol.cs`** -> AI Confidence: **99.24%**
590. **`src/Compilers/CSharp/Portable/Symbols/NamedTypeSymbol.cs`** -> AI Confidence: **99.24%**
591. **`src/Compilers/CSharp/Portable/Symbols/NamespaceOrTypeSymbol.cs`** -> AI Confidence: **99.24%**
592. **`src/Compilers/CSharp/Portable/Symbols/NonMissingAssemblySymbol.cs`** -> AI Confidence: **99.24%**
593. **`src/Compilers/CSharp/Portable/Symbols/Source/ExtensionGroupingInfo.cs`** -> AI Confidence: **99.24%**
594. **`src/Compilers/CSharp/Portable/Symbols/Source/GlobalExpressionVariable.cs`** -> AI Confidence: **99.24%**
595. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceEnumConstantSymbol.cs`** -> AI Confidence: **99.24%**
596. **`src/Compilers/CSharp/Portable/Symbols/Source/SourcePropertyAccessorSymbol.cs`** -> AI Confidence: **99.24%**
597. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedSimpleProgramEntryPointSymbol.cs`** -> AI Confidence: **99.24%**
598. **`src/Compilers/CSharp/Portable/Symbols/TypeSymbolExtensions.cs`** -> AI Confidence: **99.24%**
599. **`src/Compilers/CSharp/Portable/Syntax/CSharpSyntaxTree.ParsedSyntaxTree.cs`** -> AI Confidence: **99.24%**
600. **`src/Compilers/CSharp/Portable/Syntax/SyntaxFactory.cs`** -> AI Confidence: **99.24%**
601. **`src/Compilers/CSharp/Test/CommandLine/CommandLineTestBase.cs`** -> AI Confidence: **99.24%**
602. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncEHTests.cs`** -> AI Confidence: **99.24%**
603. **`src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueTest.cs`** -> AI Confidence: **99.24%**
604. **`src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Nullable.cs`** -> AI Confidence: **99.24%**
605. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTestBase.cs`** -> AI Confidence: **99.24%**
606. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests4.cs`** -> AI Confidence: **99.24%**
607. **`src/Compilers/CSharp/Test/Semantic/Semantics/ConditionalOperatorTests.cs`** -> AI Confidence: **99.24%**
608. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullConditionalAssignmentTests.cs`** -> AI Confidence: **99.24%**
609. **`src/Compilers/CSharp/Test/Semantic/Semantics/SemanticAnalyzerTests.cs`** -> AI Confidence: **99.24%**
610. **`src/Compilers/CSharp/Test/Syntax/LexicalAndXml/CrefLexerTests.cs`** -> AI Confidence: **99.24%**
611. **`src/Compilers/CSharp/Test/Syntax/LexicalAndXml/NameAttributeValueLexerTests.cs`** -> AI Confidence: **99.24%**
612. **`src/Compilers/CSharp/Test/Syntax/Parsing/DeclarationParsingTests.cs`** -> AI Confidence: **99.24%**
613. **`src/Compilers/CSharp/Test/Syntax/Parsing/ExpressionParsingTests.cs`** -> AI Confidence: **99.24%**
614. **`src/Compilers/Core/MSBuildTask/Utilities.cs`** -> AI Confidence: **99.24%**
615. **`src/Compilers/Core/Portable/CodeGen/LocalScopeManager.cs`** -> AI Confidence: **99.24%**
616. **`src/Compilers/Core/Portable/CommandLine/AnalyzerConfigSet.cs`** -> AI Confidence: **99.24%**
617. **`src/Compilers/Core/Portable/CryptographicHashProvider.cs`** -> AI Confidence: **99.24%**
618. **`src/Compilers/Core/Portable/CvtRes.cs`** -> AI Confidence: **99.24%**
619. **`src/Compilers/Core/Portable/Diagnostic/DiagnosticBag.cs`** -> AI Confidence: **99.24%**
620. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerAssemblyLoader.Desktop.cs`** -> AI Confidence: **99.24%**
621. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerManager.AnalyzerExecutionContext.cs`** -> AI Confidence: **99.24%**
622. **`src/Compilers/Core/Portable/Emit/CommonPEModuleBuilder.cs`** -> AI Confidence: **99.24%**
623. **`src/Compilers/Core/Portable/Emit/EditAndContinue/DeltaMetadataWriter.cs`** -> AI Confidence: **99.24%**
624. **`src/Compilers/Core/Portable/MetadataReference/AssemblyMetadata.cs`** -> AI Confidence: **99.24%**
625. **`src/Compilers/Core/Portable/MetadataReference/ModuleMetadata.cs`** -> AI Confidence: **99.24%**
626. **`src/Compilers/Core/Portable/SourceGeneration/AdditionalSourcesCollection.cs`** -> AI Confidence: **99.24%**
627. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/HostOutputNode.cs`** -> AI Confidence: **99.24%**
628. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/NodeStateTable.cs`** -> AI Confidence: **99.24%**
629. **`src/Compilers/Core/Portable/Syntax/SyntaxList`1.cs`** -> AI Confidence: **99.24%**
630. **`src/Compilers/Core/Portable/Syntax/SyntaxNode.cs`** -> AI Confidence: **99.24%**
631. **`src/Compilers/Core/Portable/Syntax/SyntaxTokenList.cs`** -> AI Confidence: **99.24%**
632. **`src/Compilers/Core/Portable/Syntax/SyntaxTree.cs`** -> AI Confidence: **99.24%**
633. **`src/Compilers/Core/Portable/Syntax/SyntaxTriviaList.cs`** -> AI Confidence: **99.24%**
634. **`src/Compilers/Core/Portable/Text/SourceText.cs`** -> AI Confidence: **99.24%**
635. **`src/Compilers/Core/Portable/Text/StringText.cs`** -> AI Confidence: **99.24%**
636. **`src/Compilers/Server/VBCSCompiler/CompilerRequestHandler.cs`** -> AI Confidence: **99.24%**
637. **`src/Compilers/Shared/BuildServerConnection.cs`** -> AI Confidence: **99.24%**
638. **`src/Compilers/Test/Core/Assert/AssertEx.cs`** -> AI Confidence: **99.24%**
639. **`src/Compilers/Test/Core/Compilation/CompilationExtensions.cs`** -> AI Confidence: **99.24%**
640. **`src/Compilers/Test/Core/EncodingTestHelpers.cs`** -> AI Confidence: **99.24%**
641. **`src/Compilers/Test/Core/InstrumentationChecker.cs`** -> AI Confidence: **99.24%**
642. **`src/Compilers/Test/Core/MarkedSource/MarkupTestFile.cs`** -> AI Confidence: **99.24%**
643. **`src/Compilers/Test/Core/Platform/Desktop/RuntimeAssemblyManager.cs`** -> AI Confidence: **99.24%**
644. **`src/Compilers/Test/Core/TestableCompiler.cs`** -> AI Confidence: **99.24%**
645. **`src/Compilers/Test/Utilities/CSharp/Extensions.cs`** -> AI Confidence: **99.24%**
646. **`src/Dependencies/Collections/Extensions/IEnumerableExtensions.cs`** -> AI Confidence: **99.24%**
647. **`src/EditorFeatures/CSharp/StringCopyPaste/KnownSourcePasteProcessor.cs`** -> AI Confidence: **99.24%**
648. **`src/EditorFeatures/CSharp/StringCopyPaste/StringCopyPasteData.cs`** -> AI Confidence: **99.24%**
649. **`src/EditorFeatures/CSharpTest/Completion/CompletionProviders/AbstractCSharpCompletionProviderTests.cs`** -> AI Confidence: **99.24%**
650. **`src/EditorFeatures/CSharpTest/Formatting/Indentation/SmartIndenterEnterOnTokenTests.cs`** -> AI Confidence: **99.24%**
651. **`src/EditorFeatures/Core/EditAndContinue/EditAndContinueLanguageService.cs`** -> AI Confidence: **99.24%**
652. **`src/EditorFeatures/Core/EditorConfigSettings/Aggregator/SettingsAggregator.cs`** -> AI Confidence: **99.24%**
653. **`src/EditorFeatures/Core/InlineRename/AbstractInlineRenameUndoManager.cs`** -> AI Confidence: **99.24%**
654. **`src/EditorFeatures/Core/InlineRename/UI/Adornment/RenameFlyoutViewModel.cs`** -> AI Confidence: **99.24%**
655. **`src/EditorFeatures/Core/LineSeparators/LineSeparatorAdornmentManager.cs`** -> AI Confidence: **99.24%**
656. **`src/EditorFeatures/Test/MetadataAsSource/AbstractMetadataAsSourceTests.TestContext.cs`** -> AI Confidence: **99.24%**
657. **`src/EditorFeatures/Test/Snippets/RoslynLSPSnippetConvertTests.cs`** -> AI Confidence: **99.24%**
658. **`src/EditorFeatures/TestUtilities/Completion/AbstractCompletionProviderTests.cs`** -> AI Confidence: **99.24%**
659. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/CompilationContext.cs`** -> AI Confidence: **99.24%**
660. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/EvaluationContext.cs`** -> AI Confidence: **99.24%**
661. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/EvaluationContextBase.cs`** -> AI Confidence: **99.24%**
662. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/ExpressionCompiler.cs`** -> AI Confidence: **99.24%**
663. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/FrameDecoder.cs`** -> AI Confidence: **99.24%**
664. **`src/ExpressionEvaluator/Core/Source/FunctionResolver/MetadataResolver.cs`** -> AI Confidence: **99.24%**
665. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Helpers/TypeHelpers.cs`** -> AI Confidence: **99.24%**
666. **`src/ExpressionEvaluator/Core/Test/ResultProvider/Debugger/Engine/DkmClrValue.cs`** -> AI Confidence: **99.24%**
667. **`src/Features/CSharp/Portable/AddImport/CSharpAddImportFeatureService.cs`** -> AI Confidence: **99.24%**
668. **`src/Features/CSharp/Portable/BraceMatching/StringLiteralBraceMatcher.cs`** -> AI Confidence: **99.24%**
669. **`src/Features/CSharp/Portable/CodeRefactorings/SyncNamespace/CSharpChangeNamespaceService.cs`** -> AI Confidence: **99.24%**
670. **`src/Features/CSharp/Portable/Completion/CompletionProviders/CSharpSuggestionModeCompletionProvider.cs`** -> AI Confidence: **99.24%**
671. **`src/Features/CSharp/Portable/ConvertLinq/CSharpConvertLinqQueryToForEachProvider.cs`** -> AI Confidence: **99.24%**
672. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/AbstractToMethodConverter.cs`** -> AI Confidence: **99.24%**
673. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/CSharpConvertForEachToLinqQueryProvider.cs`** -> AI Confidence: **99.24%**
674. **`src/Features/CSharp/Portable/ConvertPrimaryToRegularConstructor/ConvertPrimaryToRegularConstructorCodeRefactoringProvider_DocumentationComments.cs`** -> AI Confidence: **99.24%**
675. **`src/Features/CSharp/Portable/GenerateType/CSharpGenerateTypeService.cs`** -> AI Confidence: **99.24%**
676. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/SwitchStatementHighlighter.cs`** -> AI Confidence: **99.24%**
677. **`src/Features/CSharp/Portable/LineSeparators/CSharpLineSeparatorService.cs`** -> AI Confidence: **99.24%**
678. **`src/Features/CSharp/Portable/Rename/CSharpRenameIssuesService.cs`** -> AI Confidence: **99.24%**
679. **`src/Features/CSharp/Portable/SolutionExplorer/CSharpSolutionExplorerSymbolTreeItemProvider.cs`** -> AI Confidence: **99.24%**
680. **`src/Features/CSharp/Portable/Structure/CSharpStructureHelpers.cs`** -> AI Confidence: **99.24%**
681. **`src/Features/CSharpTest/ReplaceConditionalWithStatements/ReplaceConditionalWithStatementsTests.cs`** -> AI Confidence: **99.24%**
682. **`src/Features/Core/Portable/Completion/FileSystemCompletionHelper.cs`** -> AI Confidence: **99.24%**
683. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/ExtensionMemberImportCompletionHelper.SymbolComputer.cs`** -> AI Confidence: **99.24%**
684. **`src/Features/Core/Portable/Completion/Providers/SymbolCompletionItem.cs`** -> AI Confidence: **99.24%**
685. **`src/Features/Core/Portable/ConvertIfToSwitch/AbstractConvertIfToSwitchCodeRefactoringProvider.Analyzer.cs`** -> AI Confidence: **99.24%**
686. **`src/Features/Core/Portable/EditAndContinue/CommittedSolution.cs`** -> AI Confidence: **99.24%**
687. **`src/Features/Core/Portable/EditAndContinue/EditAndContinueDebugInfoReader.cs`** -> AI Confidence: **99.24%**
688. **`src/Features/Core/Portable/EditAndContinue/EditSession.cs`** -> AI Confidence: **99.24%**
689. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexBraceMatcher.cs`** -> AI Confidence: **99.24%**
690. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexLanguageDetector.cs`** -> AI Confidence: **99.24%**
691. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/RegexLexer.cs`** -> AI Confidence: **99.24%**
692. **`src/Features/Core/Portable/Extensions/IExtensionAssemblyLoaderProvider.cs`** -> AI Confidence: **99.24%**
693. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingWorkItem.cs`** -> AI Confidence: **99.24%**
694. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.cs`** -> AI Confidence: **99.24%**
695. **`src/Features/Core/Portable/LanguageServices/SymbolDisplayService/AbstractSymbolDisplayService.AbstractSymbolDescriptionBuilder.cs`** -> AI Confidence: **99.24%**
696. **`src/Features/Core/Portable/MetadataAsSource/DecompilationMetadataAsSourceFileProvider.cs`** -> AI Confidence: **99.24%**
697. **`src/Features/Core/Portable/MetadataAsSource/MetadataAsSourceFileService.cs`** -> AI Confidence: **99.24%**
698. **`src/Features/Core/Portable/NavigateTo/AbstractNavigateToSearchService.InProcess.cs`** -> AI Confidence: **99.24%**
699. **`src/Features/Core/Portable/PdbSourceDocument/PdbSourceDocumentLoaderService.cs`** -> AI Confidence: **99.24%**
700. **`src/Features/Core/Portable/ReplacePropertyWithMethods/AbstractReplacePropertyWithMethodsService.cs`** -> AI Confidence: **99.24%**
701. **`src/Features/ExternalAccess/Copilot/Internal/Analyzer/CSharp/CSharpCopilotCodeAnalysisService.cs`** -> AI Confidence: **99.24%**
702. **`src/Features/TestUtilities/EditAndContinue/SourceMarkers.cs`** -> AI Confidence: **99.24%**
703. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/AutoLoadProjectsInitializer.cs`** -> AI Confidence: **99.24%**
704. **`src/LanguageServer/Protocol/Extensions/ProtocolConversions.cs`** -> AI Confidence: **99.24%**
705. **`src/LanguageServer/Protocol/Handler/AbstractRefreshQueue.cs`** -> AI Confidence: **99.24%**
706. **`src/LanguageServer/Protocol/Handler/RequestContext.cs`** -> AI Confidence: **99.24%**
707. **`src/LanguageServer/Protocol/Protocol/Converters/SumConverter.cs`** -> AI Confidence: **99.24%**
708. **`src/LanguageServer/ProtocolUnitTests/Diagnostics/AbstractPullDiagnosticTestsBase.cs`** -> AI Confidence: **99.24%**
709. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/FixAnalyzers/FixerWithFixAllAnalyzer.cs`** -> AI Confidence: **99.24%**
710. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/ConfigureGeneratedCodeAnalysisAnalyzer.cs`** -> AI Confidence: **99.24%**
711. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticAnalyzerAPIUsageAnalyzer.cs`** -> AI Confidence: **99.24%**
712. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/EnableConcurrentExecutionAnalyzer.cs`** -> AI Confidence: **99.24%**
713. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/CallSiteImplicitAllocationAnalyzer.cs`** -> AI Confidence: **99.24%**
714. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/EnumeratorAllocationAnalyzer.cs`** -> AI Confidence: **99.24%**
715. **`src/RoslynAnalyzers/PublicApiAnalyzers/Core/Analyzers/DeclarePublicApiAnalyzer.cs`** -> AI Confidence: **99.24%**
716. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/CSharpSpecializedEnumerableCreationAnalyzer.cs`** -> AI Confidence: **99.24%**
717. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/DefaultableTypeShouldHaveDefaultableFieldsAnalyzer.cs`** -> AI Confidence: **99.24%**
718. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/DoNotCallGetTestAccessor.cs`** -> AI Confidence: **99.24%**
719. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/ExportedPartsShouldHaveImportingConstructorCodeFixProvider.cs`** -> AI Confidence: **99.24%**
720. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/SpecializedEnumerableCreationAnalyzer.cs`** -> AI Confidence: **99.24%**
721. **`src/RoslynAnalyzers/Text.Analyzers/Core/IdentifiersShouldBeSpelledCorrectly.cs`** -> AI Confidence: **99.24%**
722. **`src/RoslynAnalyzers/Tools/GenerateDocumentationAndConfigFiles/Program.cs`** -> AI Confidence: **99.24%**
723. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/ISymbolExtensions.cs`** -> AI Confidence: **99.24%**
724. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/CopyAnalysis/CopyAnalysis.CopyDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
725. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/DisposeAnalysis/DisposeAnalysis.DisposeDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
726. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/DisposeAnalysis/DisposeAnalysisContext.cs`** -> AI Confidence: **99.24%**
727. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/DisposeAnalysis/DisposeAnalysisHelper.cs`** -> AI Confidence: **99.24%**
728. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/GlobalFlowStateAnalysis/GlobalFlowStateAnalysisContext.cs`** -> AI Confidence: **99.24%**
729. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/ParameterValidationAnalysis/ParameterValidationAnalysis.ParameterValidationDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
730. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PointsToAnalysis/PointsToAnalysis.PointsToDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
731. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AnalysisEntityDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
732. **`src/Scripting/CSharpTest/ObjectFormatterTests.cs`** -> AI Confidence: **99.24%**
733. **`src/Tools/BuildActionTelemetryTable/Program.cs`** -> AI Confidence: **99.24%**
734. **`src/Tools/ExternalAccess/Razor/Features/RazorAnalyzerAssemblyResolver.cs`** -> AI Confidence: **99.24%**
735. **`src/Tools/ExternalAccess/Xaml/Internal/OnInitializedServiceFactory.cs`** -> AI Confidence: **99.24%**
736. **`src/Tools/Source/CompilerGeneratorTools/Source/CSharpSyntaxGenerator/Program.cs`** -> AI Confidence: **99.24%**
737. **`src/VisualStudio/CSharp/Impl/Options/CSharpVisualStudioOptionStorageReadFallbacks.cs`** -> AI Confidence: **99.24%**
738. **`src/VisualStudio/CSharp/Impl/ProjectSystemShim/CSharpProjectShim.OptionsProcessor.cs`** -> AI Confidence: **99.24%**
739. **`src/VisualStudio/Core/Def/DocumentOutline/DocumentOutlineView.xaml.cs`** -> AI Confidence: **99.24%**
740. **`src/VisualStudio/Core/Def/GenerateType/GenerateTypeDialogViewModel.cs`** -> AI Confidence: **99.24%**
741. **`src/VisualStudio/Core/Def/Implementation/ContainedLanguageRefactorNotifyService.cs`** -> AI Confidence: **99.24%**
742. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractDescriptionBuilder.cs`** -> AI Confidence: **99.24%**
743. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractListItemFactory.cs`** -> AI Confidence: **99.24%**
744. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractObjectBrowserLibraryManager.cs`** -> AI Confidence: **99.24%**
745. **`src/VisualStudio/Core/Def/PreviewPane/PreviewPaneService.cs`** -> AI Confidence: **99.24%**
746. **`src/VisualStudio/Core/Def/ProjectSystem/InvisibleEditor.cs`** -> AI Confidence: **99.24%**
747. **`src/VisualStudio/Core/Def/ProjectSystem/Logging/RoslynWorkspaceStructureLogger.cs`** -> AI Confidence: **99.24%**
748. **`src/VisualStudio/Core/Def/ProjectSystem/VisualStudioWorkspaceImpl.cs`** -> AI Confidence: **99.24%**
749. **`src/VisualStudio/Core/Def/Remote/VisualStudioWorkspaceServiceHubConnector.cs`** -> AI Confidence: **99.24%**
750. **`src/VisualStudio/Core/Def/TableDataSource/Suppression/VisualStudioDiagnosticListSuppressionStateService.cs`** -> AI Confidence: **99.24%**
751. **`src/VisualStudio/Core/Impl/CodeModel/CodeModelProjectCache.cs`** -> AI Confidence: **99.24%**
752. **`src/VisualStudio/Core/Impl/ProjectSystem/CPS/CPSProject_IWorkspaceProjectContext.cs`** -> AI Confidence: **99.24%**
753. **`src/VisualStudio/Core/Impl/SolutionExplorer/AnalyzersCommandHandler.cs`** -> AI Confidence: **99.24%**
754. **`src/VisualStudio/Core/Impl/SolutionExplorer/DiagnosticItem/CpsDiagnosticItemSourceProvider.cs`** -> AI Confidence: **99.24%**
755. **`src/VisualStudio/Core/Test.Next/Options/VisualStudioSettingsOptionPersisterTests.cs`** -> AI Confidence: **99.24%**
756. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/VisualStudioInstance.cs`** -> AI Confidence: **99.24%**
757. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/NameSyntaxClassifier.cs`** -> AI Confidence: **99.24%**
758. **`src/Workspaces/CSharp/Portable/CodeGeneration/CSharpSyntaxGenerator.cs`** -> AI Confidence: **99.24%**
759. **`src/Workspaces/CSharp/Portable/Recommendations/CSharpRecommendationServiceRunner.cs`** -> AI Confidence: **99.24%**
760. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpExtensionMethodReducer.cs`** -> AI Confidence: **99.24%**
761. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpMiscellaneousReducer.cs`** -> AI Confidence: **99.24%**
762. **`src/Workspaces/CSharp/Portable/Simplification/Simplifiers/ExpressionSimplifier.cs`** -> AI Confidence: **99.24%**
763. **`src/Workspaces/CSharp/Portable/Simplification/Simplifiers/NameSimplifier.cs`** -> AI Confidence: **99.24%**
764. **`src/Workspaces/Core/Portable/CodeRefactorings/FixAllOccurences/RefactorAllState.cs`** -> AI Confidence: **99.24%**
765. **`src/Workspaces/Core/Portable/Diagnostics/Extensions.cs`** -> AI Confidence: **99.24%**
766. **`src/Workspaces/Core/Portable/FindSymbols/FindLiterals/FindLiteralsSearchEngine.cs`** -> AI Confidence: **99.24%**
767. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/OrdinaryMethodReferenceFinder.cs`** -> AI Confidence: **99.24%**
768. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/ParameterSymbolReferenceFinder.cs`** -> AI Confidence: **99.24%**
769. **`src/Workspaces/Core/Portable/Serialization/SerializableSourceText.cs`** -> AI Confidence: **99.24%**
770. **`src/Workspaces/Core/Portable/Shared/Extensions/ISymbolExtensions.cs`** -> AI Confidence: **99.24%**
771. **`src/Workspaces/Core/Portable/Shared/TestHooks/AsynchronousOperationListenerProvider.cs`** -> AI Confidence: **99.24%**
772. **`src/Workspaces/Core/Portable/Simplification/Simplifier.cs`** -> AI Confidence: **99.24%**
773. **`src/Workspaces/Core/Portable/Workspace/Solution/Solution.cs`** -> AI Confidence: **99.24%**
774. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.WithFrozenSourceGeneratedDocumentsCompilationTracker.cs`** -> AI Confidence: **99.24%**
775. **`src/Workspaces/CoreTestUtilities/Workspaces/TestHostProject`1.cs`** -> AI Confidence: **99.24%**
776. **`src/Workspaces/MSBuild/BuildHost/MSBuild/ProjectFile/ProjectFile.cs`** -> AI Confidence: **99.24%**
777. **`src/Workspaces/MSBuild/BuildHost/Rpc/RpcServer.cs`** -> AI Confidence: **99.24%**
778. **`src/Workspaces/MSBuild/Core/MSBuild/MSBuildProjectLoader.cs`** -> AI Confidence: **99.24%**
779. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/BlockSyntaxExtensions.cs`** -> AI Confidence: **99.24%**
780. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/SyntaxNodeExtensions.cs`** -> AI Confidence: **99.24%**
781. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/WrappingFormattingRule.cs`** -> AI Confidence: **99.24%**
782. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Simplification/Simplifiers/CastSimplifier.cs`** -> AI Confidence: **99.24%**
783. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Extensions/SyntaxNodeExtensions.cs`** -> AI Confidence: **99.24%**
784. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/AbstractSyntaxFormatting.cs`** -> AI Confidence: **99.24%**
785. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/BottomUpBaseIndentationFinder.cs`** -> AI Confidence: **99.24%**
786. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/NamingStyle.cs`** -> AI Confidence: **99.24%**
787. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/Serialization/SymbolSpecification.cs`** -> AI Confidence: **99.24%**
788. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/AbstractSpeculationAnalyzer.cs`** -> AI Confidence: **99.24%**
789. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/CommonFormattingHelpers.cs`** -> AI Confidence: **99.24%**
790. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/LightweightOverloadResolution.cs`** -> AI Confidence: **99.24%**
791. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Extensions/Symbols/ISymbolExtensions.cs`** -> AI Confidence: **99.24%**
792. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ITypeParameterSymbolExtensions.cs`** -> AI Confidence: **99.24%**
793. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Indentation/CSharpIndentationService.Indenter.cs`** -> AI Confidence: **99.24%**
794. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/LanguageServices/CSharpAddImportsService.cs`** -> AI Confidence: **99.24%**
795. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/LanguageServices/CSharpReplaceDiscardDeclarationsWithAssignmentsService.cs`** -> AI Confidence: **99.24%**
796. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/ProjectExtensions.cs`** -> AI Confidence: **99.24%**
797. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/SyntaxGeneratorExtensions_Negate.cs`** -> AI Confidence: **99.24%**
798. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/LanguageServices/SemanticsFactsService/AbstractSemanticFactsService.cs`** -> AI Confidence: **99.24%**
799. **`src/VisualStudio/IntegrationTest/Harness/EqualException/Test.ps1`** -> AI Confidence: **99.23%**
800. **`src/Analyzers/CSharp/Analyzers/ConvertProgram/ConvertProgramAnalysis_TopLevelStatements.cs`** -> AI Confidence: **99.23%**
801. **`src/Analyzers/CSharp/Analyzers/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionDiagnosticAnalyzer.Analyzer.cs`** -> AI Confidence: **99.23%**
802. **`src/Analyzers/CSharp/Tests/ConditionalExpressionInStringInterpolation/CSharpAddParenthesesAroundConditionalExpressionInInterpolatedStringCodeFixProviderTests.cs`** -> AI Confidence: **99.23%**
803. **`src/Analyzers/CSharp/Tests/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionFixAllTests.cs`** -> AI Confidence: **99.23%**
804. **`src/Analyzers/CSharp/Tests/RemoveConfusingSuppression/RemoveConfusingSuppressionTests.cs`** -> AI Confidence: **99.23%**
805. **`src/Analyzers/CSharp/Tests/UseDefaultLiteral/UseDefaultLiteralTests.cs`** -> AI Confidence: **99.23%**
806. **`src/Analyzers/Core/Analyzers/RemoveUnnecessarySuppressions/SuppressMessageAttributeState.cs`** -> AI Confidence: **99.23%**
807. **`src/Compilers/CSharp/Portable/Binder/PatternExplainer.cs`** -> AI Confidence: **99.23%**
808. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/Conversion.cs`** -> AI Confidence: **99.23%**
809. **`src/Compilers/CSharp/Portable/Binder/SwitchBinder_Patterns.cs`** -> AI Confidence: **99.23%**
810. **`src/Compilers/CSharp/Portable/Binder/WithCrefTypeParametersBinder.cs`** -> AI Confidence: **99.23%**
811. **`src/Compilers/CSharp/Portable/Binder/WithExternAndUsingAliasesBinder.cs`** -> AI Confidence: **99.23%**
812. **`src/Compilers/CSharp/Portable/BoundTree/BoundDecisionDag.cs`** -> AI Confidence: **99.23%**
813. **`src/Compilers/CSharp/Portable/CodeGen/EmitArrayInitializer.cs`** -> AI Confidence: **99.23%**
814. **`src/Compilers/CSharp/Portable/CodeGen/EmitOperators.cs`** -> AI Confidence: **99.23%**
815. **`src/Compilers/CSharp/Portable/Declarations/DeclarationTable.cs`** -> AI Confidence: **99.23%**
816. **`src/Compilers/CSharp/Portable/Declarations/MergedTypeDeclaration.cs`** -> AI Confidence: **99.23%**
817. **`src/Compilers/CSharp/Portable/DocumentationComments/SourceDocumentationCommentUtils.cs`** -> AI Confidence: **99.23%**
818. **`src/Compilers/CSharp/Portable/FlowAnalysis/AlwaysAssignedWalker.cs`** -> AI Confidence: **99.23%**
819. **`src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.SnapshotManager.cs`** -> AI Confidence: **99.23%**
820. **`src/Compilers/CSharp/Portable/Lowering/AsyncRewriter/AsyncRewriter.cs`** -> AI Confidence: **99.23%**
821. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/LocalStateTracingInstrumenter.cs`** -> AI Confidence: **99.23%**
822. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.PatternLocalRewriter.cs`** -> AI Confidence: **99.23%**
823. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_CollectionExpression.cs`** -> AI Confidence: **99.23%**
824. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_ForEachStatement.cs`** -> AI Confidence: **99.23%**
825. **`src/Compilers/CSharp/Portable/Lowering/MethodToClassRewriter.cs`** -> AI Confidence: **99.23%**
826. **`src/Compilers/CSharp/Portable/Lowering/SpillSequenceSpiller.cs`** -> AI Confidence: **99.23%**
827. **`src/Compilers/CSharp/Portable/Symbols/AbstractTypeMap.cs`** -> AI Confidence: **99.23%**
828. **`src/Compilers/CSharp/Portable/Symbols/AliasSymbol.cs`** -> AI Confidence: **99.23%**
829. **`src/Compilers/CSharp/Portable/Symbols/EventSymbol.cs`** -> AI Confidence: **99.23%**
830. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/DynamicTypeDecoder.cs`** -> AI Confidence: **99.23%**
831. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceConstructorSymbolBase.cs`** -> AI Confidence: **99.23%**
832. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceCustomEventSymbol.cs`** -> AI Confidence: **99.23%**
833. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceFieldSymbol.cs`** -> AI Confidence: **99.23%**
834. **`src/Compilers/CSharp/Portable/Syntax/CSharpSyntaxNode.cs`** -> AI Confidence: **99.23%**
835. **`src/Compilers/CSharp/Portable/Utilities/ValueSetFactory.NumericValueSet.cs`** -> AI Confidence: **99.23%**
836. **`src/Compilers/CSharp/Test/Emit3/Diagnostics/OperationAnalyzerTests.cs`** -> AI Confidence: **99.23%**
837. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests2.cs`** -> AI Confidence: **99.23%**
838. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ICoalesceAssignmentOperation.cs`** -> AI Confidence: **99.23%**
839. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IMethodReferenceOperation.cs`** -> AI Confidence: **99.23%**
840. **`src/Compilers/CSharp/Test/Syntax/Parsing/PatternParsingTests2.cs`** -> AI Confidence: **99.23%**
841. **`src/Compilers/Core/MSBuildTask/MapSourceRoots.cs`** -> AI Confidence: **99.23%**
842. **`src/Compilers/Core/Portable/CaseInsensitiveComparison.cs`** -> AI Confidence: **99.23%**
843. **`src/Compilers/Core/Portable/CodeGen/ILBuilderEmit.cs`** -> AI Confidence: **99.23%**
844. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/ShadowCopyAnalyzerPathResolver.cs`** -> AI Confidence: **99.23%**
845. **`src/Compilers/Core/Portable/Emit/EditAndContinue/SymbolMatcher.cs`** -> AI Confidence: **99.23%**
846. **`src/Compilers/Core/Portable/Emit/NoPia/CommonEmbeddedType.cs`** -> AI Confidence: **99.23%**
847. **`src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.RegionBuilder.cs`** -> AI Confidence: **99.23%**
848. **`src/Compilers/Core/Portable/PEWriter/MetadataWriter.DynamicAnalysis.cs`** -> AI Confidence: **99.23%**
849. **`src/Compilers/Core/Portable/RuleSet/RuleSetProcessor.cs`** -> AI Confidence: **99.23%**
850. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/SourceOutputNode.cs`** -> AI Confidence: **99.23%**
851. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/TransformNode.cs`** -> AI Confidence: **99.23%**
852. **`src/Compilers/Core/Portable/Syntax/SyntaxNodeExtensions_Tracking.cs`** -> AI Confidence: **99.23%**
853. **`src/Compilers/Core/Portable/Syntax/SyntaxNodeOrToken.cs`** -> AI Confidence: **99.23%**
854. **`src/Compilers/Core/Portable/Text/CompositeText.cs`** -> AI Confidence: **99.23%**
855. **`src/Compilers/Test/Utilities/CSharp/MockCSharpCompiler.cs`** -> AI Confidence: **99.23%**
856. **`src/Dependencies/Collections/OneOrMany.cs`** -> AI Confidence: **99.23%**
857. **`src/Dependencies/Contracts/Contract.cs`** -> AI Confidence: **99.23%**
858. **`src/EditorFeatures/CSharpTest/DecompiledSource/DecompiledSourceFormattingTests.cs`** -> AI Confidence: **99.23%**
859. **`src/EditorFeatures/CSharpTest/KeywordHighlighting/LoopHighlighterTests.cs`** -> AI Confidence: **99.23%**
860. **`src/EditorFeatures/CSharpTest/SymbolKey/SymbolKeyTestBase.cs`** -> AI Confidence: **99.23%**
861. **`src/EditorFeatures/Core/StringCopyPaste/WpfStringCopyPasteService.cs`** -> AI Confidence: **99.23%**
862. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/SyntaxHelpers.cs`** -> AI Confidence: **99.23%**
863. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Expansion/MemberExpansion.cs`** -> AI Confidence: **99.23%**
864. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Helpers/InlineArrayHelpers.cs`** -> AI Confidence: **99.23%**
865. **`src/Features/CSharp/Portable/CodeLens/CSharpCodeLensDisplayInfoService.cs`** -> AI Confidence: **99.23%**
866. **`src/Features/CSharp/Portable/Completion/KeywordRecommenders/RefKeywordRecommender.cs`** -> AI Confidence: **99.23%**
867. **`src/Features/CSharp/Portable/EditAndContinue/SyntaxUtilities.cs`** -> AI Confidence: **99.23%**
868. **`src/Features/Core/Portable/Completion/Providers/AbstractObjectInitializerCompletionProvider.cs`** -> AI Confidence: **99.23%**
869. **`src/Features/Core/Portable/EditAndContinue/TraceLog.cs`** -> AI Confidence: **99.23%**
870. **`src/Features/Core/Portable/EmbeddedLanguages/DateAndTime/LanguageServices/DateAndTimeLanguageDetector.cs`** -> AI Confidence: **99.23%**
871. **`src/Features/Core/Portable/EmbeddedLanguages/EmbeddedLanguageDetector.cs`** -> AI Confidence: **99.23%**
872. **`src/Features/Core/Portable/PdbSourceDocument/SourceLinkMap.cs`** -> AI Confidence: **99.23%**
873. **`src/Features/TestUtilities/EditAndContinue/MockManagedEditAndContinueDebuggerService.cs`** -> AI Confidence: **99.23%**
874. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompilerExtensionStrictApiAnalyzer.cs`** -> AI Confidence: **99.23%**
875. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/PreferNullLiteral.cs`** -> AI Confidence: **99.23%**
876. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/AbstractExposeMemberForTesting`1.cs`** -> AI Confidence: **99.23%**
877. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/CodeAnalysisMetricData.cs`** -> AI Confidence: **99.23%**
878. **`src/RoslynAnalyzers/Utilities/Compiler/Options/AbstractCategorizedAnalyzerConfigOptions.cs`** -> AI Confidence: **99.23%**
879. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PointsToAnalysis/PointsToAnalysisContext.cs`** -> AI Confidence: **99.23%**
880. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/ValueContentAnalysis/ValueContentAnalysis.cs`** -> AI Confidence: **99.23%**
881. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AnalysisEntity.cs`** -> AI Confidence: **99.23%**
882. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/ThrownExceptionInfo.cs`** -> AI Confidence: **99.23%**
883. **`src/Scripting/CSharp/CSharpScript.cs`** -> AI Confidence: **99.23%**
884. **`src/Test/PdbUtilities/Reader/SymReaderFactory.cs`** -> AI Confidence: **99.23%**
885. **`src/Test/PdbUtilities/Shared/DummyMetadataImport.cs`** -> AI Confidence: **99.23%**
886. **`src/Tools/Source/RunTests/TestRunner.cs`** -> AI Confidence: **99.23%**
887. **`src/VisualStudio/CSharp/Impl/CodeModel/ModifierFlagsExtensions.cs`** -> AI Confidence: **99.23%**
888. **`src/VisualStudio/Core/Def/ErrorReporting/VisualStudioErrorReportingService.ExceptionFormatting.cs`** -> AI Confidence: **99.23%**
889. **`src/VisualStudio/Core/Def/Notification/VSNotificationServiceFactory.cs`** -> AI Confidence: **99.23%**
890. **`src/VisualStudio/Core/Def/UnusedReferences/Dialog/UnusedReferencesTableProvider.DataSource.cs`** -> AI Confidence: **99.23%**
891. **`src/VisualStudio/Core/Def/Venus/VenusCommandFilter`2.cs`** -> AI Confidence: **99.23%**
892. **`src/VisualStudio/Core/Impl/SolutionExplorer/AnalyzerReferenceManager.cs`** -> AI Confidence: **99.23%**
893. **`src/VisualStudio/ExternalAccess/FSharp/Internal/SignatureHelp/FSharpSignatureHelpProvider.cs`** -> AI Confidence: **99.23%**
894. **`src/VisualStudio/IntegrationTest/Harness/SourceGeneratorUnitTests/TestServicesSourceGeneratorTests.cs`** -> AI Confidence: **99.23%**
895. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/IdeFactDiscoverer.cs`** -> AI Confidence: **99.23%**
896. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/AutomationElementExtensions.cs`** -> AI Confidence: **99.23%**
897. **`src/VisualStudio/IntegrationTest/TestSetup/TestTraceListener.cs`** -> AI Confidence: **99.23%**
898. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/DiscardSyntaxClassifier.cs`** -> AI Confidence: **99.23%**
899. **`src/Workspaces/Core/Portable/CodeFixes/FixAllOccurrences/FixAllContext.cs`** -> AI Confidence: **99.23%**
900. **`src/Workspaces/Core/Portable/PatternMatching/AllLowerCamelCaseMatcher.cs`** -> AI Confidence: **99.23%**
901. **`src/Workspaces/Core/Portable/PatternMatching/PatternMatcher.cs`** -> AI Confidence: **99.23%**
902. **`src/Workspaces/Core/Portable/Recommendations/AbstractRecommendationService.cs`** -> AI Confidence: **99.23%**
903. **`src/Workspaces/Core/Portable/Workspace/Solution/DocumentInfo.cs`** -> AI Confidence: **99.23%**
904. **`src/Workspaces/Core/Portable/Workspace/Solution/ProjectDependencyGraph.cs`** -> AI Confidence: **99.23%**
905. **`src/Workspaces/Core/Portable/Workspace/Solution/ProjectInfo.cs`** -> AI Confidence: **99.23%**
906. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/CodeStyle/TypeStyle/TypeStyleHelper.cs`** -> AI Confidence: **99.23%**
907. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Diagnostics/StructuredAnalyzerConfigOptions.cs`** -> AI Confidence: **99.23%**
908. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/Serialization/NamingStylePreferencesEditorConfigSerializer.cs`** -> AI Confidence: **99.23%**
909. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Serialization/ObjectReader.cs`** -> AI Confidence: **99.23%**
910. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/SymbolKey/SymbolKey.BodyLevelSymbolKey.cs`** -> AI Confidence: **99.23%**
911. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/SymbolKey/SymbolKey.SymbolKeyWriter.cs`** -> AI Confidence: **99.23%**
912. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/CodeGeneration/AttributeGenerator.cs`** -> AI Confidence: **99.23%**
913. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/ISolutionExtensions.cs`** -> AI Confidence: **99.23%**
914. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/SymbolFinder/SymbolFinderInternal.cs`** -> AI Confidence: **99.23%**
915. **`src/Compilers/CSharp/Portable/FlowAnalysis/ReadWriteWalker.cs`** -> AI Confidence: **99.22%**
916. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ICoalesceOperation.cs`** -> AI Confidence: **99.22%**
917. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ISwitchOperation.cs`** -> AI Confidence: **99.22%**
918. **`src/Compilers/Core/Portable/DiaSymReader/Utilities/ComMemoryStream.cs`** -> AI Confidence: **99.22%**
919. **`src/EditorFeatures/CSharpTest/KeywordHighlighting/SwitchStatementHighlighterTests.cs`** -> AI Confidence: **99.22%**
920. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/ComputationalComplexityMetrics.cs`** -> AI Confidence: **99.22%**
921. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SemanticFacts/ISemanticFacts.cs`** -> AI Confidence: **99.22%**
922. **`src/Compilers/CSharp/Portable/BoundTree/BoundBinaryOperator.UncommonData.cs`** -> AI Confidence: **99.2%**
923. **`src/Compilers/CSharp/Portable/BoundTree/BoundInlineArrayAccess.cs`** -> AI Confidence: **99.2%**
924. **`src/Compilers/Core/MSBuildTask/CanonicalError.cs`** -> AI Confidence: **99.2%**
925. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalysisContextInfo.cs`** -> AI Confidence: **99.2%**
926. **`src/Compilers/Core/Portable/EnumConstantHelper.cs`** -> AI Confidence: **99.2%**
927. **`src/Dependencies/Threading/ParallelExtensions.NetFramework.cs`** -> AI Confidence: **99.2%**
928. **`src/Analyzers/CSharp/Analyzers/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
929. **`src/Analyzers/CSharp/Analyzers/MisplacedUsingDirectives/MisplacedUsingDirectivesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
930. **`src/Analyzers/CSharp/Analyzers/NewLines/ConstructorInitializerPlacement/ConstructorInitializerPlacementDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
931. **`src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryImports/CSharpRemoveUnnecessaryImportsDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
932. **`src/Analyzers/CSharp/Analyzers/RemoveUnreachableCode/CSharpRemoveUnreachableCodeDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
933. **`src/Analyzers/CSharp/Analyzers/UseCoalesceExpression/CSharpUseCoalesceExpressionForIfNullStatementCheckDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
934. **`src/Analyzers/CSharp/Analyzers/UseCollectionExpression/CSharpUseCollectionExpressionForNewDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
935. **`src/Analyzers/CSharp/Analyzers/UseExpressionBody/Helpers/UseExpressionBodyForMethodsHelper.cs`** -> AI Confidence: **99.18%**
936. **`src/Analyzers/CSharp/Analyzers/UseExpressionBody/Helpers/UseExpressionBodyHelper.cs`** -> AI Confidence: **99.18%**
937. **`src/Analyzers/CSharp/Analyzers/UseExpressionBodyForLambda/UseExpressionBodyForLambdaHelpers.cs`** -> AI Confidence: **99.18%**
938. **`src/Analyzers/CSharp/Analyzers/UseIsNullCheck/CSharpUseNullCheckOverTypeCheckDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
939. **`src/Analyzers/CSharp/Analyzers/UseSimpleUsingStatement/UseSimpleUsingStatementDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
940. **`src/Analyzers/CSharp/Analyzers/UseUnboundGenericTypeInNameOf/CSharpUseUnboundGenericTypeInNameOfDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
941. **`src/Analyzers/CSharp/Analyzers/UseUtf8StringLiteral/UseUtf8StringLiteralDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
942. **`src/Analyzers/CSharp/CodeFixes/AssignOutParameters/AssignOutParametersAboveReturnCodeFixProvider.cs`** -> AI Confidence: **99.18%**
943. **`src/Analyzers/CSharp/CodeFixes/ConvertNamespace/ConvertNamespaceTransform.cs`** -> AI Confidence: **99.18%**
944. **`src/Analyzers/CSharp/CodeFixes/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
945. **`src/Analyzers/CSharp/CodeFixes/ConvertToAsync/CSharpConvertToAsyncMethodCodeFixProvider.cs`** -> AI Confidence: **99.18%**
946. **`src/Analyzers/CSharp/CodeFixes/ConvertToRecord/PositionalParameterInfo.cs`** -> AI Confidence: **99.18%**
947. **`src/Analyzers/CSharp/CodeFixes/GenerateDefaultConstructors/CSharpGenerateDefaultConstructorsService.cs`** -> AI Confidence: **99.18%**
948. **`src/Analyzers/CSharp/CodeFixes/GenerateMethod/GenerateConversionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
949. **`src/Analyzers/CSharp/CodeFixes/GenerateMethod/GenerateMethodCodeFixProvider.cs`** -> AI Confidence: **99.18%**
950. **`src/Analyzers/CSharp/CodeFixes/GenerateParameterizedMember/CSharpGenerateDeconstructMethodService.cs`** -> AI Confidence: **99.18%**
951. **`src/Analyzers/CSharp/CodeFixes/MakeLocalFunctionStatic/MakeLocalFunctionStaticCodeFixHelper.cs`** -> AI Confidence: **99.18%**
952. **`src/Analyzers/CSharp/CodeFixes/MakeMemberRequired/CSharpMakeMemberRequiredCodeFixProvider.cs`** -> AI Confidence: **99.18%**
953. **`src/Analyzers/CSharp/CodeFixes/MakeMemberStatic/CSharpMakeMemberStaticCodeFixProvider.cs`** -> AI Confidence: **99.18%**
954. **`src/Analyzers/CSharp/CodeFixes/MakeMethodSynchronous/CSharpMakeMethodSynchronousCodeFixProvider.cs`** -> AI Confidence: **99.18%**
955. **`src/Analyzers/CSharp/CodeFixes/MakeStructFieldsWritable/CSharpMakeStructFieldsWritableCodeFixProvider.cs`** -> AI Confidence: **99.18%**
956. **`src/Analyzers/CSharp/CodeFixes/MakeStructMemberReadOnly/CSharpMakeStructMemberReadOnlyCodeFixProvider.cs`** -> AI Confidence: **99.18%**
957. **`src/Analyzers/CSharp/CodeFixes/QualifyMemberAccess/CSharpQualifyMemberAccessCodeFixProvider.cs`** -> AI Confidence: **99.18%**
958. **`src/Analyzers/CSharp/CodeFixes/RemoveUnnecessaryDiscardDesignation/CSharpRemoveUnnecessaryDiscardDesignationCodeFixProvider.cs`** -> AI Confidence: **99.18%**
959. **`src/Analyzers/CSharp/CodeFixes/RemoveUnnecessaryNullableDirective/CSharpRemoveUnnecessaryNullableDirectiveCodeFixProvider.cs`** -> AI Confidence: **99.18%**
960. **`src/Analyzers/CSharp/CodeFixes/SimplifyPropertyAccessor/CSharpSimplifyPropertyAccessorCodeFixProvider.cs`** -> AI Confidence: **99.18%**
961. **`src/Analyzers/CSharp/CodeFixes/TransposeRecordKeyword/CSharpTransposeRecordKeywordCodeFixProvider.cs`** -> AI Confidence: **99.18%**
962. **`src/Analyzers/CSharp/CodeFixes/UseAutoProperty/CSharpUseAutoPropertyCodeFixProvider.cs`** -> AI Confidence: **99.18%**
963. **`src/Analyzers/CSharp/CodeFixes/UseCollectionExpression/CSharpUseCollectionExpressionForArrayCodeFixProvider.cs`** -> AI Confidence: **99.18%**
964. **`src/Analyzers/CSharp/CodeFixes/UseCollectionExpression/CSharpUseCollectionExpressionForStackAllocCodeFixProvider.cs`** -> AI Confidence: **99.18%**
965. **`src/Analyzers/CSharp/CodeFixes/UseCollectionInitializer/CSharpUseCollectionInitializerCodeFixProvider_CollectionInitializer.cs`** -> AI Confidence: **99.18%**
966. **`src/Analyzers/CSharp/CodeFixes/UseExplicitArrayInExpressionTree/CSharpUseExplicitArrayInExpressionTreeCodeFixProvider.cs`** -> AI Confidence: **99.18%**
967. **`src/Analyzers/CSharp/CodeFixes/UseImplicitOrExplicitType/UseExplicitTypeCodeFixProvider.cs`** -> AI Confidence: **99.18%**
968. **`src/Analyzers/CSharp/CodeFixes/UseLocalFunction/CSharpUseLocalFunctionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
969. **`src/Analyzers/CSharp/CodeFixes/UsePrimaryConstructor/CSharpUsePrimaryConstructorFixAllProvider.cs`** -> AI Confidence: **99.18%**
970. **`src/Analyzers/CSharp/CodeFixes/UseSimpleUsingStatement/UseSimpleUsingStatementCodeFixProvider.cs`** -> AI Confidence: **99.18%**
971. **`src/Analyzers/CSharp/CodeFixes/UseSystemThreadingLock/CSharpUseSystemThreadingLockFixAllProvider.cs`** -> AI Confidence: **99.18%**
972. **`src/Analyzers/CSharp/Tests/AssignOutParameters/AssignOutParametersAboveReturnTests.cs`** -> AI Confidence: **99.18%**
973. **`src/Analyzers/CSharp/Tests/Formatting/FormattingAnalyzerTests.cs`** -> AI Confidence: **99.18%**
974. **`src/Analyzers/CSharp/Tests/InlineDeclaration/CSharpInlineDeclarationTests.cs`** -> AI Confidence: **99.18%**
975. **`src/Analyzers/CSharp/Tests/MakeMemberRequired/MakeMemberRequiredTests.cs`** -> AI Confidence: **99.18%**
976. **`src/Analyzers/CSharp/Tests/NewLines/EmbeddedStatementPlacement/EmbeddedStatementPlacementTests.cs`** -> AI Confidence: **99.18%**
977. **`src/Analyzers/CSharp/Tests/RemoveUnnecessaryCast/RemoveUnnecessaryCastTests.cs`** -> AI Confidence: **99.18%**
978. **`src/Analyzers/CSharp/Tests/RemoveUnnecessaryDiscardDesignation/RemoveUnnecessaryDiscardDesignationTests.cs`** -> AI Confidence: **99.18%**
979. **`src/Analyzers/CSharp/Tests/RemoveUnreachableCode/RemoveUnreachableCodeTests.cs`** -> AI Confidence: **99.18%**
980. **`src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValueAssignmentTests.cs`** -> AI Confidence: **99.18%**
981. **`src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValuesTestsBase.cs`** -> AI Confidence: **99.18%**
982. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForIfNullStatementCheckTests.cs`** -> AI Confidence: **99.18%**
983. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForTernaryConditionalCheckTests.cs`** -> AI Confidence: **99.18%**
984. **`src/Analyzers/CSharp/Tests/UseDeconstruction/UseDeconstructionTests.cs`** -> AI Confidence: **99.18%**
985. **`src/Analyzers/CSharp/Tests/UseExplicitTupleName/UseExplicitTupleNameTests.cs`** -> AI Confidence: **99.18%**
986. **`src/Analyzers/CSharp/Tests/UseIsNullCheck/UseIsNullCheckForCastAndEqualityOperatorTests.cs`** -> AI Confidence: **99.18%**
987. **`src/Analyzers/CSharp/Tests/UseIsNullCheck/UseIsNullCheckForReferenceEqualsTests.cs`** -> AI Confidence: **99.18%**
988. **`src/Analyzers/CSharp/Tests/UseThrowExpression/UseThrowExpressionTests.cs`** -> AI Confidence: **99.18%**
989. **`src/Analyzers/Core/Analyzers/MatchFolderAndNamespace/AbstractMatchFolderAndNamespaceDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
990. **`src/Analyzers/Core/Analyzers/RemoveUnnecessaryParentheses/AbstractRemoveUnnecessaryParenthesesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
991. **`src/Analyzers/Core/Analyzers/SimplifyInterpolation/AbstractSimplifyInterpolationDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
992. **`src/Analyzers/Core/Analyzers/UseObjectInitializer/AbstractUseObjectInitializerDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
993. **`src/Analyzers/Core/CodeFixes/AddAnonymousTypeMemberName/AbstractAddAnonymousTypeMemberNameCodeFixProvider.cs`** -> AI Confidence: **99.18%**
994. **`src/Analyzers/Core/CodeFixes/AddParameter/AbstractAddParameterCodeFixProvider.cs`** -> AI Confidence: **99.18%**
995. **`src/Analyzers/Core/CodeFixes/DocumentationComments/AbstractAddDocCommentNodesCodeFixProvider.cs`** -> AI Confidence: **99.18%**
996. **`src/Analyzers/Core/CodeFixes/DocumentationComments/AbstractRemoveDocCommentNodeCodeFixProvider.cs`** -> AI Confidence: **99.18%**
997. **`src/Analyzers/Core/CodeFixes/GenerateDefaultConstructors/AbstractGenerateDefaultConstructorsService.State.cs`** -> AI Confidence: **99.18%**
998. **`src/Analyzers/Core/CodeFixes/GenerateDefaultConstructors/GenerateDefaultConstructorsCodeAction.cs`** -> AI Confidence: **99.18%**
999. **`src/Analyzers/Core/CodeFixes/GenerateEnumMember/AbstractGenerateEnumMemberService.State.cs`** -> AI Confidence: **99.18%**
1000. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateConversionService.cs`** -> AI Confidence: **99.18%**
1001. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateMethodService.State.cs`** -> AI Confidence: **99.18%**
1002. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateMethodService.cs`** -> AI Confidence: **99.18%**
1003. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateParameterizedMemberService.AbstractInvocationInfo.cs`** -> AI Confidence: **99.18%**
1004. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateParameterizedMemberService.SignatureInfo.cs`** -> AI Confidence: **99.18%**
1005. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/TypeParameterSubstitution.cs`** -> AI Confidence: **99.18%**
1006. **`src/Analyzers/Core/CodeFixes/GenerateVariable/AbstractGenerateVariableService.State.cs`** -> AI Confidence: **99.18%**
1007. **`src/Analyzers/Core/CodeFixes/ImplementAbstractClass/ImplementAbstractClassData.cs`** -> AI Confidence: **99.18%**
1008. **`src/Analyzers/Core/CodeFixes/ImplementInterface/ImplementInterfaceGenerator.cs`** -> AI Confidence: **99.18%**
1009. **`src/Analyzers/Core/CodeFixes/ImplementInterface/ImplementInterfaceGenerator_Conflicts.cs`** -> AI Confidence: **99.18%**
1010. **`src/Analyzers/Core/CodeFixes/MakeMemberStatic/AbstractMakeMemberStaticCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1011. **`src/Analyzers/Core/CodeFixes/RemoveAsyncModifier/AbstractRemoveAsyncModifierCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1012. **`src/Analyzers/Core/CodeFixes/RemoveUnnecessarySuppressions/RemoveUnnecessaryPragmaSuppressionsCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1013. **`src/Analyzers/Core/CodeFixes/RemoveUnusedMembers/AbstractRemoveUnusedMembersCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1014. **`src/Analyzers/Core/CodeFixes/SimplifyLinqExpression/SimplifyLinqExpressionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1015. **`src/Analyzers/Core/CodeFixes/UseCoalesceExpression/AbstractUseCoalesceExpressionForIfNullStatementCheckCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1016. **`src/Analyzers/Core/CodeFixes/UseConditionalExpression/ForReturn/AbstractUseConditionalExpressionForReturnCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1017. **`src/Analyzers/Core/CodeFixes/UseNullPropagation/AbstractUseNullPropagationCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1018. **`src/Compilers/CSharp/Portable/Binder/EmbeddedStatementBinder.cs`** -> AI Confidence: **99.18%**
1019. **`src/Compilers/CSharp/Portable/Binder/FixedStatementBinder.cs`** -> AI Confidence: **99.18%**
1020. **`src/Compilers/CSharp/Portable/Binder/WhileBinder.cs`** -> AI Confidence: **99.18%**
1021. **`src/Compilers/CSharp/Portable/Binder/WithExternAliasesBinder.cs`** -> AI Confidence: **99.18%**
1022. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.IncludeElementExpander.cs`** -> AI Confidence: **99.18%**
1023. **`src/Compilers/CSharp/Portable/Emitter/EditAndContinue/CSharpSymbolMatcher.cs`** -> AI Confidence: **99.18%**
1024. **`src/Compilers/CSharp/Portable/Emitter/EditAndContinue/EmitHelpers.cs`** -> AI Confidence: **99.18%**
1025. **`src/Compilers/CSharp/Portable/Emitter/Model/ExpandedVarargsMethodReference.cs`** -> AI Confidence: **99.18%**
1026. **`src/Compilers/CSharp/Portable/Emitter/Model/PEAssemblyBuilder.cs`** -> AI Confidence: **99.18%**
1027. **`src/Compilers/CSharp/Portable/FlowAnalysis/EntryPointsWalker.cs`** -> AI Confidence: **99.18%**
1028. **`src/Compilers/CSharp/Portable/Lowering/AsyncRewriter/AsyncExceptionHandlerRewriter.cs`** -> AI Confidence: **99.18%**
1029. **`src/Compilers/CSharp/Portable/Lowering/StateMachineRewriter/SynthesizedStateMachineMethod.cs`** -> AI Confidence: **99.18%**
1030. **`src/Compilers/CSharp/Portable/Symbols/AnonymousTypes/SynthesizedSymbols/AnonymousType.TemplateSymbol.cs`** -> AI Confidence: **99.18%**
1031. **`src/Compilers/CSharp/Portable/Symbols/FunctionPointers/FunctionPointerTypeSymbol.cs`** -> AI Confidence: **99.18%**
1032. **`src/Compilers/CSharp/Portable/Symbols/LocalSymbol.cs`** -> AI Confidence: **99.18%**
1033. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEAssemblySymbol.cs`** -> AI Confidence: **99.18%**
1034. **`src/Compilers/CSharp/Portable/Symbols/MetadataOrSourceOrRetargetingAssemblySymbol.cs`** -> AI Confidence: **99.18%**
1035. **`src/Compilers/CSharp/Portable/Symbols/NoPiaIllegalGenericInstantiationSymbol.cs`** -> AI Confidence: **99.18%**
1036. **`src/Compilers/CSharp/Portable/Symbols/PublicModel/MethodSymbol.cs`** -> AI Confidence: **99.18%**
1037. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingAssemblySymbol.cs`** -> AI Confidence: **99.18%**
1038. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingModuleSymbol.cs`** -> AI Confidence: **99.18%**
1039. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingNamespaceSymbol.cs`** -> AI Confidence: **99.18%**
1040. **`src/Compilers/CSharp/Portable/Symbols/Source/LambdaSymbol.cs`** -> AI Confidence: **99.18%**
1041. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceDelegateMethodSymbol.cs`** -> AI Confidence: **99.18%**
1042. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodSymbolBase.cs`** -> AI Confidence: **99.18%**
1043. **`src/Compilers/CSharp/Portable/Symbols/Source/SynthesizedSourceOrdinaryMethodSymbol.cs`** -> AI Confidence: **99.18%**
1044. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/Records/SynthesizedRecordEqualityOperatorBase.cs`** -> AI Confidence: **99.18%**
1045. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedAccessorValueParameterSymbol.cs`** -> AI Confidence: **99.18%**
1046. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedEventAccessorSymbol.cs`** -> AI Confidence: **99.18%**
1047. **`src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs`** -> AI Confidence: **99.18%**
1048. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncIteratorTests.cs`** -> AI Confidence: **99.18%**
1049. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs`** -> AI Confidence: **99.18%**
1050. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenDynamicTests.cs`** -> AI Confidence: **99.18%**
1051. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenRefConditionalOperatorTests.cs`** -> AI Confidence: **99.18%**
1052. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleEqualityTests.cs`** -> AI Confidence: **99.18%**
1053. **`src/Compilers/CSharp/Test/Emit/CodeGen/ForeachTest.cs`** -> AI Confidence: **99.18%**
1054. **`src/Compilers/CSharp/Test/Emit/Emit/DynamicAnalysis/DynamicAnalysisResourceTests.cs`** -> AI Confidence: **99.18%**
1055. **`src/Compilers/CSharp/Test/Emit/PrivateProtected.cs`** -> AI Confidence: **99.18%**
1056. **`src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueTestBase.cs`** -> AI Confidence: **99.18%**
1057. **`src/Compilers/CSharp/Test/Emit2/Emit/LocalStateTracing/LocalStateTracingTests.cs`** -> AI Confidence: **99.18%**
1058. **`src/Compilers/CSharp/Test/Emit2/PDB/PDBTests.cs`** -> AI Confidence: **99.18%**
1059. **`src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Tuples.cs`** -> AI Confidence: **99.18%**
1060. **`src/Compilers/CSharp/Test/Emit3/Diagnostics/DiagnosticAnalyzerTests.cs`** -> AI Confidence: **99.18%**
1061. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/PatternsVsRegions.cs`** -> AI Confidence: **99.18%**
1062. **`src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs`** -> AI Confidence: **99.18%**
1063. **`src/Compilers/CSharp/Test/Emit3/RefUnsafeInIteratorAndAsyncTests.cs`** -> AI Confidence: **99.18%**
1064. **`src/Compilers/CSharp/Test/Emit3/Semantics/CollectionExpressionTests_WithElement_Nullable.cs`** -> AI Confidence: **99.18%**
1065. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests.cs`** -> AI Confidence: **99.18%**
1066. **`src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs`** -> AI Confidence: **99.18%**
1067. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IInterpolatedStringOperation.cs`** -> AI Confidence: **99.18%**
1068. **`src/Compilers/CSharp/Test/Semantic/Semantics/FuzzTests.cs`** -> AI Confidence: **99.18%**
1069. **`src/Compilers/CSharp/Test/Semantic/Semantics/LocalFunctionTests.cs`** -> AI Confidence: **99.18%**
1070. **`src/Compilers/CSharp/Test/Semantic/Semantics/MethodTypeInferenceTests.cs`** -> AI Confidence: **99.18%**
1071. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullCoalesceAssignmentTests.cs`** -> AI Confidence: **99.18%**
1072. **`src/Compilers/CSharp/Test/Semantic/Semantics/SpanStackSafetyTests.cs`** -> AI Confidence: **99.18%**
1073. **`src/Compilers/CSharp/Test/Semantic/SourceGeneration/GeneratorDriverFuzzTests.cs`** -> AI Confidence: **99.18%**
1074. **`src/Compilers/CSharp/Test/Semantic/SourceGeneration/StateTableTests.cs`** -> AI Confidence: **99.18%**
1075. **`src/Compilers/CSharp/Test/Symbol/DocumentationComments/DocumentationCommentCompilerTests.cs`** -> AI Confidence: **99.18%**
1076. **`src/Compilers/CSharp/Test/Symbol/DocumentationComments/DocumentationModeTests.cs`** -> AI Confidence: **99.18%**
1077. **`src/Compilers/CSharp/Test/Symbol/Symbols/AnonymousTypesSemanticsTests.cs`** -> AI Confidence: **99.18%**
1078. **`src/Compilers/CSharp/Test/Symbol/Symbols/CovariantReturnTests.cs`** -> AI Confidence: **99.18%**
1079. **`src/Compilers/CSharp/Test/Symbol/Symbols/MockSymbolTests.cs`** -> AI Confidence: **99.18%**
1080. **`src/Compilers/CSharp/Test/Symbol/Symbols/PartialPropertiesTests.cs`** -> AI Confidence: **99.18%**
1081. **`src/Compilers/CSharp/Test/Symbol/Symbols/Source/DeclaringSyntaxNodeTests.cs`** -> AI Confidence: **99.18%**
1082. **`src/Compilers/CSharp/Test/Symbol/Symbols/UnsignedRightShiftTests.cs`** -> AI Confidence: **99.18%**
1083. **`src/Compilers/CSharp/Test/Syntax/LexicalAndXml/LexicalTests.cs`** -> AI Confidence: **99.18%**
1084. **`src/Compilers/CSharp/Test/Syntax/Parsing/LambdaAttributeParsingTests.cs`** -> AI Confidence: **99.18%**
1085. **`src/Compilers/CSharp/Test/Syntax/Parsing/MemberDeclarationParsingTests.cs`** -> AI Confidence: **99.18%**
1086. **`src/Compilers/CSharp/Test/Syntax/Parsing/ParserErrorMessageTests.cs`** -> AI Confidence: **99.18%**
1087. **`src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxListTests.cs`** -> AI Confidence: **99.18%**
1088. **`src/Compilers/Core/AnalyzerDriver/DeclarationComputer.cs`** -> AI Confidence: **99.18%**
1089. **`src/Compilers/Core/CodeAnalysisTest/Collections/ImmutableSegmentedHashSetTest.cs`** -> AI Confidence: **99.18%**
1090. **`src/Compilers/Core/CodeAnalysisTest/Collections/SmallDictionaryTests.cs`** -> AI Confidence: **99.18%**
1091. **`src/Compilers/Core/CodeAnalysisTest/Diagnostics/SarifErrorLoggerTests.cs`** -> AI Confidence: **99.18%**
1092. **`src/Compilers/Core/MSBuildTaskTests/GenerateMSBuildEditorConfigTests.cs`** -> AI Confidence: **99.18%**
1093. **`src/Compilers/Core/MSBuildTaskTests/IntegrationTests.cs`** -> AI Confidence: **99.18%**
1094. **`src/Compilers/Core/Portable/CodeGen/ArrayMembers.cs`** -> AI Confidence: **99.18%**
1095. **`src/Compilers/Core/Portable/CodeGen/PrivateImplementationDetails.cs`** -> AI Confidence: **99.18%**
1096. **`src/Compilers/Core/Portable/Collections/UnionCollection.cs`** -> AI Confidence: **99.18%**
1097. **`src/Compilers/Core/Portable/CommandLine/CommonCompiler.ExistingReferencesResolver.cs`** -> AI Confidence: **99.18%**
1098. **`src/Compilers/Core/Portable/CommandLine/ReportAnalyzerUtil.cs`** -> AI Confidence: **99.18%**
1099. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/DiagnosticAnalysisContext.cs`** -> AI Confidence: **99.18%**
1100. **`src/Compilers/Core/Portable/DocumentationCommentId.cs`** -> AI Confidence: **99.18%**
1101. **`src/Compilers/Core/Portable/EmbeddedText.cs`** -> AI Confidence: **99.18%**
1102. **`src/Compilers/Core/Portable/Operations/IOperation.OperationList.Reversed.cs`** -> AI Confidence: **99.18%**
1103. **`src/Compilers/Core/Portable/PEWriter/CustomDebugInfoWriter.cs`** -> AI Confidence: **99.18%**
1104. **`src/Compilers/Core/Portable/PEWriter/PooledBlobBuilder.cs`** -> AI Confidence: **99.18%**
1105. **`src/Compilers/Core/Portable/PEWriter/SigningUtilities.cs`** -> AI Confidence: **99.18%**
1106. **`src/Compilers/Core/Portable/PEWriter/Types.cs`** -> AI Confidence: **99.18%**
1107. **`src/Compilers/Core/Portable/ReferenceManager/AssemblyDataForAssemblyBeingBuilt.cs`** -> AI Confidence: **99.18%**
1108. **`src/Compilers/Core/Portable/Syntax/SyntaxTokenList.Reversed.cs`** -> AI Confidence: **99.18%**
1109. **`src/Compilers/Core/Portable/Syntax/SyntaxTriviaList.Reversed.cs`** -> AI Confidence: **99.18%**
1110. **`src/Compilers/Core/RebuildTest/DeterministicKeyBuilderTests.cs`** -> AI Confidence: **99.18%**
1111. **`src/Compilers/Extension/CompilerPackage.cs`** -> AI Confidence: **99.18%**
1112. **`src/Compilers/Server/VBCSCompiler/CSharpCompilerServer.cs`** -> AI Confidence: **99.18%**
1113. **`src/Compilers/Server/VBCSCompiler/NamedPipeClientConnection.cs`** -> AI Confidence: **99.18%**
1114. **`src/Compilers/Server/VBCSCompilerTests/BuildServerConnectionTests.cs`** -> AI Confidence: **99.18%**
1115. **`src/Compilers/Shared/GlobalAssemblyCacheHelpers/GacFileResolver.cs`** -> AI Confidence: **99.18%**
1116. **`src/Compilers/Test/Core/Compilation/CompilationDifference.cs`** -> AI Confidence: **99.18%**
1117. **`src/Compilers/Test/Core/Compilation/CompilationTestDataExtensions.cs`** -> AI Confidence: **99.18%**
1118. **`src/Compilers/Test/Core/Diagnostics/DiagnosticExtensions.cs`** -> AI Confidence: **99.18%**
1119. **`src/Compilers/Test/Core/Diagnostics/ThrowingDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
1120. **`src/Compilers/Test/Core/Metadata/MetadataReaderUtils.cs`** -> AI Confidence: **99.18%**
1121. **`src/Compilers/Test/Core/Metadata/MetadataValidation.cs`** -> AI Confidence: **99.18%**
1122. **`src/Compilers/Test/Core/TempFiles/TempFile.cs`** -> AI Confidence: **99.18%**
1123. **`src/Compilers/Test/Core/TestHelpers.cs`** -> AI Confidence: **99.18%**
1124. **`src/Compilers/Test/Core/TestableFile.cs`** -> AI Confidence: **99.18%**
1125. **`src/Compilers/Test/Utilities/CSharp/CSharpTestSource.cs`** -> AI Confidence: **99.18%**
1126. **`src/Compilers/Test/Utilities/CSharp/EmitMetadataTestBase.cs`** -> AI Confidence: **99.18%**
1127. **`src/Compilers/Test/Utilities/CSharp/LifetimeAnnotationAttributesVisitor.cs`** -> AI Confidence: **99.18%**
1128. **`src/Compilers/Test/Utilities/CSharp/SemanticModelTestBase.cs`** -> AI Confidence: **99.18%**
1129. **`src/EditorFeatures/CSharp/BlockCommentEditing/CloseBlockCommentCommandHandler.cs`** -> AI Confidence: **99.18%**
1130. **`src/EditorFeatures/CSharp/ConvertNamespace/ConvertNamespaceCommandHandler.cs`** -> AI Confidence: **99.18%**
1131. **`src/EditorFeatures/CSharp/EventHookup/EventHookupCommandHandler_TabKeyCommand.cs`** -> AI Confidence: **99.18%**
1132. **`src/EditorFeatures/CSharp/EventHookup/EventHookupSessionManager_EventHookupSession.cs`** -> AI Confidence: **99.18%**
1133. **`src/EditorFeatures/CSharp/GoToBase/CSharpGoToBaseService.cs`** -> AI Confidence: **99.18%**
1134. **`src/EditorFeatures/CSharp/Interactive/CSharpSendToInteractiveSubmissionProvider.cs`** -> AI Confidence: **99.18%**
1135. **`src/EditorFeatures/CSharp/RawStringLiteral/RawStringLiteralCommandHandler_TypeChar.cs`** -> AI Confidence: **99.18%**
1136. **`src/EditorFeatures/CSharp/StringCopyPaste/StringCopyPasteCommandHandler.cs`** -> AI Confidence: **99.18%**
1137. **`src/EditorFeatures/CSharp/StringCopyPaste/StringInfo.cs`** -> AI Confidence: **99.18%**
1138. **`src/EditorFeatures/CSharpTest/CodeActions/SyncNamespace/CSharpSyncNamespaceTestsBase.cs`** -> AI Confidence: **99.18%**
1139. **`src/EditorFeatures/CSharpTest/Completion/CompletionProviders/OperatorCompletionProviderTests.cs`** -> AI Confidence: **99.18%**
1140. **`src/EditorFeatures/CSharpTest/Completion/CompletionProviders/XmlDocumentationCommentCompletionProviderTests.cs`** -> AI Confidence: **99.18%**
1141. **`src/EditorFeatures/CSharpTest/Debugging/ProximityExpressionsGetterTests.cs`** -> AI Confidence: **99.18%**
1142. **`src/EditorFeatures/CSharpTest/Formatting/CodeCleanupTests.TestFixers.cs`** -> AI Confidence: **99.18%**
1143. **`src/EditorFeatures/CSharpTest/Structure/IfDirectiveTriviaStructureTests.cs`** -> AI Confidence: **99.18%**
1144. **`src/EditorFeatures/Core/Adornments/AbstractAdornmentManager.cs`** -> AI Confidence: **99.18%**
1145. **`src/EditorFeatures/Core/AutomaticCompletion/AbstractAutomaticLineEnderCommandHandler.cs`** -> AI Confidence: **99.18%**
1146. **`src/EditorFeatures/Core/AutomaticCompletion/BraceCompletionSessionProvider.BraceCompletionSession.cs`** -> AI Confidence: **99.18%**
1147. **`src/EditorFeatures/Core/BackgroundWorkIndicator/WpfBackgroundWorkIndicatorFactory.cs`** -> AI Confidence: **99.18%**
1148. **`src/EditorFeatures/Core/BraceMatching/BraceHighlightingViewTaggerProvider.cs`** -> AI Confidence: **99.18%**
1149. **`src/EditorFeatures/Core/ChangeSignature/AbstractChangeSignatureCommandHandler.cs`** -> AI Confidence: **99.18%**
1150. **`src/EditorFeatures/Core/Classification/CopyPasteAndPrintingClassificationBufferTaggerProvider.Tagger.cs`** -> AI Confidence: **99.18%**
1151. **`src/EditorFeatures/Core/Classification/Semantic/AbstractSemanticOrEmbeddedClassificationViewTaggerProvider.cs`** -> AI Confidence: **99.18%**
1152. **`src/EditorFeatures/Core/Classification/Syntactic/SyntacticClassificationTaggerProvider.TagComputer.cs`** -> AI Confidence: **99.18%**
1153. **`src/EditorFeatures/Core/CommentSelection/AbstractToggleBlockCommentBase.cs`** -> AI Confidence: **99.18%**
1154. **`src/EditorFeatures/Core/CommentSelection/CommentUncommentSelectionCommandHandler.cs`** -> AI Confidence: **99.18%**
1155. **`src/EditorFeatures/Core/Copilot/CopilotEditorUtilities.cs`** -> AI Confidence: **99.18%**
1156. **`src/EditorFeatures/Core/Copilot/CopilotTaggerProvider.cs`** -> AI Confidence: **99.18%**
1157. **`src/EditorFeatures/Core/Copilot/RoslynProposalAdjusterProvider.cs`** -> AI Confidence: **99.18%**
1158. **`src/EditorFeatures/Core/Editor/EditorLayerExtensionManager.cs`** -> AI Confidence: **99.18%**
1159. **`src/EditorFeatures/Core/Editor/GoToAdjacentMemberCommandHandler.cs`** -> AI Confidence: **99.18%**
1160. **`src/EditorFeatures/Core/EditorConfigSettings/Updater/NamingStyles/EditorConfigNamingStylesExtensions.cs`** -> AI Confidence: **99.18%**
1161. **`src/EditorFeatures/Core/EditorConfigSettings/Updater/SettingsUpdaterBase.cs`** -> AI Confidence: **99.18%**
1162. **`src/EditorFeatures/Core/Extensibility/NavigationBar/WrappedNavigationBarItem.cs`** -> AI Confidence: **99.18%**
1163. **`src/EditorFeatures/Core/Formatting/FormatCommandHandler.Paste.cs`** -> AI Confidence: **99.18%**
1164. **`src/EditorFeatures/Core/Formatting/FormatCommandHandler.cs`** -> AI Confidence: **99.18%**
1165. **`src/EditorFeatures/Core/IWpfDifferenceViewerExtensions.cs`** -> AI Confidence: **99.18%**
1166. **`src/EditorFeatures/Core/InlineDiagnostics/AbstractDiagnosticsTaggerProvider.cs`** -> AI Confidence: **99.18%**
1167. **`src/EditorFeatures/Core/InlineDiagnostics/InlineDiagnosticsTag.cs`** -> AI Confidence: **99.18%**
1168. **`src/EditorFeatures/Core/InlineDiagnostics/InlineDiagnosticsTaggerProvider.cs`** -> AI Confidence: **99.18%**
1169. **`src/EditorFeatures/Core/InlineHints/InlineHintsKeyProcessorProvider.cs`** -> AI Confidence: **99.18%**
1170. **`src/EditorFeatures/Core/InlineHints/InlineHintsTagger.cs`** -> AI Confidence: **99.18%**
1171. **`src/EditorFeatures/Core/InlineHints/InlineHintsTaggerProvider.cs`** -> AI Confidence: **99.18%**
1172. **`src/EditorFeatures/Core/InlineRename/CommandHandlers/AbstractRenameCommandHandler_RenameHandler.cs`** -> AI Confidence: **99.18%**
1173. **`src/EditorFeatures/Core/InlineRename/InlineRenameService.cs`** -> AI Confidence: **99.18%**
1174. **`src/EditorFeatures/Core/InlineRename/InlineRenameSession.cs`** -> AI Confidence: **99.18%**
1175. **`src/EditorFeatures/Core/InlineRename/UndoManagerServiceFactory.cs`** -> AI Confidence: **99.18%**
1176. **`src/EditorFeatures/Core/IntelliSense/AsyncCompletion/CommitManagerProvider.cs`** -> AI Confidence: **99.18%**
1177. **`src/EditorFeatures/Core/IntelliSense/AsyncCompletion/CompletionSessionData.cs`** -> AI Confidence: **99.18%**
1178. **`src/EditorFeatures/Core/IntelliSense/AsyncCompletion/CompletionSource.cs`** -> AI Confidence: **99.18%**
1179. **`src/EditorFeatures/Core/Interactive/InertClassifierProvider.cs`** -> AI Confidence: **99.18%**
1180. **`src/EditorFeatures/Core/Interactive/InteractiveEvaluator.cs`** -> AI Confidence: **99.18%**
1181. **`src/EditorFeatures/Core/Interactive/InteractivePasteCommandHandler.cs`** -> AI Confidence: **99.18%**
1182. **`src/EditorFeatures/Core/NavigateTo/NavigateToItemProvider.Callback.cs`** -> AI Confidence: **99.18%**
1183. **`src/EditorFeatures/Core/NavigateTo/NavigateToItemProvider.cs`** -> AI Confidence: **99.18%**
1184. **`src/EditorFeatures/Core/Navigation/AbstractDefinitionLocationService.cs`** -> AI Confidence: **99.18%**
1185. **`src/EditorFeatures/Core/NavigationBar/NavigationBarController_ModelComputation.cs`** -> AI Confidence: **99.18%**
1186. **`src/EditorFeatures/Core/Peek/PeekableItemFactory.cs`** -> AI Confidence: **99.18%**
1187. **`src/EditorFeatures/Core/Peek/PeekableItemSource.cs`** -> AI Confidence: **99.18%**
1188. **`src/EditorFeatures/Core/Preview/AbstractPreviewFactoryService.cs`** -> AI Confidence: **99.18%**
1189. **`src/EditorFeatures/Core/Preview/PreviewFactoryService.cs`** -> AI Confidence: **99.18%**
1190. **`src/EditorFeatures/Core/QuickInfo/LazyToolTip.cs`** -> AI Confidence: **99.18%**
1191. **`src/EditorFeatures/Core/QuickInfo/OnTheFlyDocsViewFactory.cs`** -> AI Confidence: **99.18%**
1192. **`src/EditorFeatures/Core/ReferenceHighlighting/ReferenceHighlightingViewTaggerProvider.cs`** -> AI Confidence: **99.18%**
1193. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.StateMachine.cs`** -> AI Confidence: **99.18%**
1194. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.TrackingSession.cs`** -> AI Confidence: **99.18%**
1195. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.cs`** -> AI Confidence: **99.18%**
1196. **`src/EditorFeatures/Core/SemanticSearch/SemanticSearchEditorWorkspace.cs`** -> AI Confidence: **99.18%**
1197. **`src/EditorFeatures/Core/Shared/Extensions/HostWorkspaceServicesExtensions.cs`** -> AI Confidence: **99.18%**
1198. **`src/EditorFeatures/Core/Shared/Extensions/ITextViewExtensions.cs`** -> AI Confidence: **99.18%**
1199. **`src/EditorFeatures/Core/Shared/Utilities/ClassificationTypeMap.cs`** -> AI Confidence: **99.18%**
1200. **`src/EditorFeatures/Core/SignatureHelp/Presentation/Signature.cs`** -> AI Confidence: **99.18%**
1201. **`src/EditorFeatures/Core/SignatureHelp/Presentation/SignatureHelpClassifier.cs`** -> AI Confidence: **99.18%**
1202. **`src/EditorFeatures/Core/SignatureHelp/Presentation/SignatureHelpPresenter.SignatureHelpPresenterSession.cs`** -> AI Confidence: **99.18%**
1203. **`src/EditorFeatures/Core/StringIndentation/StringIndentationAdornmentManager.VisibleBlock.cs`** -> AI Confidence: **99.18%**
1204. **`src/EditorFeatures/Core/Suggestions/SuggestedActionsSource_Async.cs`** -> AI Confidence: **99.18%**
1205. **`src/EditorFeatures/Core/Tagging/AbstractAsynchronousTaggerProvider.TagSource.cs`** -> AI Confidence: **99.18%**
1206. **`src/EditorFeatures/Core/Tagging/AsynchronousViewportTaggerProvider.cs`** -> AI Confidence: **99.18%**
1207. **`src/EditorFeatures/Core/Undo/EditorSourceTextUndoService.cs`** -> AI Confidence: **99.18%**
1208. **`src/EditorFeatures/Core/Workspaces/EditorTextFactoryService.cs`** -> AI Confidence: **99.18%**
1209. **`src/EditorFeatures/Test/CodeActions/CodeChangeProviderMetadataTests.cs`** -> AI Confidence: **99.18%**
1210. **`src/EditorFeatures/Test/CodeGeneration/AbstractCodeGenerationTests.cs`** -> AI Confidence: **99.18%**
1211. **`src/EditorFeatures/Test/Diagnostics/IDEDiagnosticIDConfigurationTests.cs`** -> AI Confidence: **99.18%**
1212. **`src/EditorFeatures/Test/Emit/CompilationOutputsTests.cs`** -> AI Confidence: **99.18%**
1213. **`src/EditorFeatures/Test/MetadataAsSource/DocCommentFormatterTests.cs`** -> AI Confidence: **99.18%**
1214. **`src/EditorFeatures/Test/Options/GlobalOptionsTests.cs`** -> AI Confidence: **99.18%**
1215. **`src/EditorFeatures/Test/Utilities/BloomFilterTests.cs`** -> AI Confidence: **99.18%**
1216. **`src/EditorFeatures/Test/ValueTracking/AbstractBaseValueTrackingTests.cs`** -> AI Confidence: **99.18%**
1217. **`src/EditorFeatures/TestUtilities/AutomaticCompletion/AbstractAutomaticBraceCompletionTests.cs`** -> AI Confidence: **99.18%**
1218. **`src/EditorFeatures/TestUtilities/ChangeSignature/TestChangeSignatureOptionsService.cs`** -> AI Confidence: **99.18%**
1219. **`src/EditorFeatures/TestUtilities/MoveStaticMembers/TestMoveStaticMembersService.cs`** -> AI Confidence: **99.18%**
1220. **`src/EditorFeatures/TestUtilities/SignatureHelp/AbstractSignatureHelpProviderTests.cs`** -> AI Confidence: **99.18%**
1221. **`src/EditorFeatures/TestUtilities/Workspaces/TestWorkspaceFixture.cs`** -> AI Confidence: **99.18%**
1222. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/Binders/PlaceholderLocalBinder.cs`** -> AI Confidence: **99.18%**
1223. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/CompilationExtensions.cs`** -> AI Confidence: **99.18%**
1224. **`src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/DebuggerDisplayAttributeTests.cs`** -> AI Confidence: **99.18%**
1225. **`src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/ExpressionCompilerTestBase.cs`** -> AI Confidence: **99.18%**
1226. **`src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/HoistedStateMachineLocalTests.cs`** -> AI Confidence: **99.18%**
1227. **`src/ExpressionEvaluator/CSharp/Test/ResultProvider/CSharpResultProviderTestBase.cs`** -> AI Confidence: **99.18%**
1228. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PseudoVariableUtilities.cs`** -> AI Confidence: **99.18%**
1229. **`src/ExpressionEvaluator/Core/Source/FunctionResolver/FunctionResolver.cs`** -> AI Confidence: **99.18%**
1230. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Expansion/TupleExpansion.cs`** -> AI Confidence: **99.18%**
1231. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Helpers/MemberAndDeclarationInfo.cs`** -> AI Confidence: **99.18%**
1232. **`src/ExpressionEvaluator/Core/Test/FunctionResolver/VisualBasicParsingTests.cs`** -> AI Confidence: **99.18%**
1233. **`src/ExpressionEvaluator/Core/Test/ResultProvider/Debugger/Engine/DkmClrRuntimeInstance.cs`** -> AI Confidence: **99.18%**
1234. **`src/Features/CSharp/Portable/BraceCompletion/StringLiteralBraceCompletionService.cs`** -> AI Confidence: **99.18%**
1235. **`src/Features/CSharp/Portable/CodeRefactorings/ConvertLocalFunctionToMethod/CSharpConvertLocalFunctionToMethodCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1236. **`src/Features/CSharp/Portable/CodeRefactorings/EnableNullable/EnableNullableCodeRefactoringProvider.FixAllProvider.cs`** -> AI Confidence: **99.18%**
1237. **`src/Features/CSharp/Portable/CodeRefactorings/EnableNullable/EnableNullableCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1238. **`src/Features/CSharp/Portable/CodeRefactorings/InlineTemporary/InlineTemporaryCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1239. **`src/Features/CSharp/Portable/CodeRefactorings/UseExplicitOrImplicitType/AbstractUseTypeCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1240. **`src/Features/CSharp/Portable/Completion/CompletionProviders/DeclarationName/DeclarationNameRecommender.NameGenerator.cs`** -> AI Confidence: **99.18%**
1241. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ExplicitInterfaceMemberCompletionProvider.ItemGetter.cs`** -> AI Confidence: **99.18%**
1242. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ExplicitInterfaceMemberCompletionProvider.cs`** -> AI Confidence: **99.18%**
1243. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ImportCompletion/ExtensionMemberImportCompletionProvider.cs`** -> AI Confidence: **99.18%**
1244. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ObjectAndWithInitializerCompletionProvider.cs`** -> AI Confidence: **99.18%**
1245. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ObjectCreationCompletionProvider.cs`** -> AI Confidence: **99.18%**
1246. **`src/Features/CSharp/Portable/Completion/CompletionProviders/OperatorsAndIndexer/UnnamedSymbolCompletionProvider_Conversions.cs`** -> AI Confidence: **99.18%**
1247. **`src/Features/CSharp/Portable/Completion/CompletionProviders/PartialMethodCompletionProvider.cs`** -> AI Confidence: **99.18%**
1248. **`src/Features/CSharp/Portable/Completion/CompletionProviders/SymbolCompletionProvider.cs`** -> AI Confidence: **99.18%**
1249. **`src/Features/CSharp/Portable/Completion/CompletionProviders/TupleNameCompletionProvider.cs`** -> AI Confidence: **99.18%**
1250. **`src/Features/CSharp/Portable/Completion/Providers/OutVariableArgumentProvider.cs`** -> AI Confidence: **99.18%**
1251. **`src/Features/CSharp/Portable/ConvertBetweenRegularAndVerbatimString/AbstractConvertBetweenRegularAndVerbatimStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1252. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/AbstractConverter.cs`** -> AI Confidence: **99.18%**
1253. **`src/Features/CSharp/Portable/ConvertNamespace/ConvertNamespaceCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1254. **`src/Features/CSharp/Portable/ConvertPrimaryToRegularConstructor/ConvertPrimaryToRegularConstructorCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1255. **`src/Features/CSharp/Portable/ConvertProgram/ConvertProgramTransform_ProgramMain.cs`** -> AI Confidence: **99.18%**
1256. **`src/Features/CSharp/Portable/ConvertToRawString/ConvertInterpolatedStringToRawStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1257. **`src/Features/CSharp/Portable/ConvertToRawString/ConvertStringToRawStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1258. **`src/Features/CSharp/Portable/Copilot/CSharpCopilotCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1259. **`src/Features/CSharp/Portable/Debugging/BreakpointResolver.cs`** -> AI Confidence: **99.18%**
1260. **`src/Features/CSharp/Portable/DecompiledSource/CSharpDecompiledSourceService.cs`** -> AI Confidence: **99.18%**
1261. **`src/Features/CSharp/Portable/EditAndContinue/DeclarationBody/CSharpLambdaBody.cs`** -> AI Confidence: **99.18%**
1262. **`src/Features/CSharp/Portable/EditAndContinue/DeclarationBody/FieldWithInitializerDeclarationBody.cs`** -> AI Confidence: **99.18%**
1263. **`src/Features/CSharp/Portable/EditAndContinue/DeclarationBody/TopLevelCodeDeclarationBody.cs`** -> AI Confidence: **99.18%**
1264. **`src/Features/CSharp/Portable/EmbeddedLanguages/CSharpTestEmbeddedLanguageClassifier.cs`** -> AI Confidence: **99.18%**
1265. **`src/Features/CSharp/Portable/Formatting/CSharpAccessibilityModifiersNewDocumentFormattingProvider.cs`** -> AI Confidence: **99.18%**
1266. **`src/Features/CSharp/Portable/GenerateMember/GenerateVariable/CSharpGenerateVariableService.cs`** -> AI Confidence: **99.18%**
1267. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/AsyncAwaitHighlighter.cs`** -> AI Confidence: **99.18%**
1268. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/TryStatementHighlighter.cs`** -> AI Confidence: **99.18%**
1269. **`src/Features/CSharp/Portable/InitializeParameter/CSharpInitializeMemberFromPrimaryConstructorParameterCodeRefactoringProvider_Update.cs`** -> AI Confidence: **99.18%**
1270. **`src/Features/CSharp/Portable/IntroduceUsingStatement/CSharpIntroduceUsingStatementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1271. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService.cs`** -> AI Confidence: **99.18%**
1272. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService_IntroduceField.cs`** -> AI Confidence: **99.18%**
1273. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService_IntroduceLocal.cs`** -> AI Confidence: **99.18%**
1274. **`src/Features/CSharp/Portable/Options/CSharpEditorConfigOptionsEnumerator.cs`** -> AI Confidence: **99.18%**
1275. **`src/Features/CSharp/Portable/QuickInfo/CSharpDiagnosticAnalyzerQuickInfoProvider.cs`** -> AI Confidence: **99.18%**
1276. **`src/Features/CSharp/Portable/ReplaceMethodWithProperty/CSharpReplaceMethodWithPropertyService.cs`** -> AI Confidence: **99.18%**
1277. **`src/Features/CSharp/Portable/ReplacePropertyWithMethods/CSharpReplacePropertyWithMethodsService.cs`** -> AI Confidence: **99.18%**
1278. **`src/Features/CSharp/Portable/SignatureHelp/ConstructorInitializerSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1279. **`src/Features/CSharp/Portable/SignatureHelp/GenericNameFullyWrittenSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1280. **`src/Features/CSharp/Portable/SignatureHelp/InvocationExpressionSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1281. **`src/Features/CSharp/Portable/SignatureHelp/InvocationExpressionSignatureHelpProviderBase_DelegateAndFunctionPointerInvoke.cs`** -> AI Confidence: **99.18%**
1282. **`src/Features/CSharp/Portable/SignatureHelp/ObjectCreationExpressionSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1283. **`src/Features/CSharp/Portable/SignatureHelp/SignatureHelpUtilities.cs`** -> AI Confidence: **99.18%**
1284. **`src/Features/CSharp/Portable/SignatureHelp/WithElementSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1285. **`src/Features/CSharp/Portable/Snippets/CSharpForEachLoopSnippetProvider.cs`** -> AI Confidence: **99.18%**
1286. **`src/Features/CSharp/Portable/Snippets/CSharpProprSnippetProvider.cs`** -> AI Confidence: **99.18%**
1287. **`src/Features/CSharp/Portable/Snippets/CSharpReversedForLoopSnippetProvider.cs`** -> AI Confidence: **99.18%**
1288. **`src/Features/CSharp/Portable/Snippets/CSharpSnippetFunctionService.cs`** -> AI Confidence: **99.18%**
1289. **`src/Features/CSharp/Portable/SplitOrMergeIfStatements/CSharpMergeConsecutiveIfStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1290. **`src/Features/CSharp/Portable/SplitOrMergeIfStatements/CSharpMergeNestedIfStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1291. **`src/Features/CSharp/Portable/SplitStringLiteral/InterpolatedStringSplitter.cs`** -> AI Confidence: **99.18%**
1292. **`src/Features/CSharp/Portable/SplitStringLiteral/StringSplitter.cs`** -> AI Confidence: **99.18%**
1293. **`src/Features/CSharp/Portable/UseExpressionBody/UseExpressionBodyCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1294. **`src/Features/CSharp/Portable/UsePatternMatching/CSharpIsAndCastCheckWithoutNameDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
1295. **`src/Features/CSharpTest/ConvertForToForEach/ConvertForToForEachTests.cs`** -> AI Confidence: **99.18%**
1296. **`src/Features/CSharpTest/ConvertProgram/ConvertToTopLevelStatementsRefactoringTests.cs`** -> AI Confidence: **99.18%**
1297. **`src/Features/CSharpTest/Copilot/CSharpImplementNotImplementedExceptionDiagnosticAnalyzerTests.cs`** -> AI Confidence: **99.18%**
1298. **`src/Features/CSharpTest/ExtractMethod/ExtractLocalFunctionTests.cs`** -> AI Confidence: **99.18%**
1299. **`src/Features/CSharpTest/InvertConditional/InvertConditionalTests.cs`** -> AI Confidence: **99.18%**
1300. **`src/Features/CSharpTest/SimplifyPropertyPattern/SimplifyPropertyPatternTests.cs`** -> AI Confidence: **99.18%**
1301. **`src/Features/CSharpTest/UseExplicitOrImplicitType/UseExplicitTypeRefactoringTests.cs`** -> AI Confidence: **99.18%**
1302. **`src/Features/CSharpTest/UseNameofInAttribute/UseNameofInAttributeTests.cs`** -> AI Confidence: **99.18%**
1303. **`src/Features/Core/Portable/AddDebuggerDisplay/AbstractAddDebuggerDisplayCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1304. **`src/Features/Core/Portable/AddImport/AbstractAddImportFeatureService.cs`** -> AI Confidence: **99.18%**
1305. **`src/Features/Core/Portable/AddImport/References/ProjectSymbolReference.cs`** -> AI Confidence: **99.18%**
1306. **`src/Features/Core/Portable/AddImport/SymbolReferenceFinder.cs`** -> AI Confidence: **99.18%**
1307. **`src/Features/Core/Portable/BraceCompletion/AbstractBraceCompletionService.cs`** -> AI Confidence: **99.18%**
1308. **`src/Features/Core/Portable/ChangeSignature/DelegateInvokeMethodReferenceFinder.cs`** -> AI Confidence: **99.18%**
1309. **`src/Features/Core/Portable/CodeFixes/Configuration/ConfigureSeverity/ConfigureSeverityLevelCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1310. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.AbstractGlobalSuppressMessageCodeAction.cs`** -> AI Confidence: **99.18%**
1311. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.RemoveSuppressionCodeAction.BatchFixer.cs`** -> AI Confidence: **99.18%**
1312. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.RemoveSuppressionCodeAction_Pragma.cs`** -> AI Confidence: **99.18%**
1313. **`src/Features/Core/Portable/CodeLens/CodeLensFindReferenceProgress.cs`** -> AI Confidence: **99.18%**
1314. **`src/Features/Core/Portable/CodeRefactorings/AddAwait/AbstractAddAwaitCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1315. **`src/Features/Core/Portable/CodeRefactorings/MoveType/AbstractMoveTypeService.cs`** -> AI Confidence: **99.18%**
1316. **`src/Features/Core/Portable/Common/TaggedText.cs`** -> AI Confidence: **99.18%**
1317. **`src/Features/Core/Portable/Completion/CommonCompletionUtilities.cs`** -> AI Confidence: **99.18%**
1318. **`src/Features/Core/Portable/Completion/CompletionService.cs`** -> AI Confidence: **99.18%**
1319. **`src/Features/Core/Portable/Completion/Providers/AbstractAwaitCompletionProvider.cs`** -> AI Confidence: **99.18%**
1320. **`src/Features/Core/Portable/Completion/Providers/AbstractPartialMethodCompletionProvider.cs`** -> AI Confidence: **99.18%**
1321. **`src/Features/Core/Portable/Completion/Providers/AbstractPartialTypeCompletionProvider.cs`** -> AI Confidence: **99.18%**
1322. **`src/Features/Core/Portable/Completion/Providers/AbstractSymbolCompletionProvider.cs`** -> AI Confidence: **99.18%**
1323. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/AbstractTypeImportCompletionProvider.cs`** -> AI Confidence: **99.18%**
1324. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/ExtensionMemberImportCompletionHelper.cs`** -> AI Confidence: **99.18%**
1325. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/ImportCompletionItem.cs`** -> AI Confidence: **99.18%**
1326. **`src/Features/Core/Portable/Completion/Providers/Scripting/AbstractDirectivePathCompletionProvider.cs`** -> AI Confidence: **99.18%**
1327. **`src/Features/Core/Portable/ConvertAnonymousType/AbstractConvertAnonymousTypeToClassCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1328. **`src/Features/Core/Portable/ConvertAnonymousType/AbstractConvertAnonymousTypeToTupleCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1329. **`src/Features/Core/Portable/ConvertAutoPropertyToFullProperty/AbstractConvertAutoPropertyToFullPropertyCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1330. **`src/Features/Core/Portable/ConvertForEachToFor/AbstractConvertForEachToForCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1331. **`src/Features/Core/Portable/ConvertLinq/ConvertForEachToLinqQuery/AbstractConvertForEachToLinqQueryProvider.cs`** -> AI Confidence: **99.18%**
1332. **`src/Features/Core/Portable/ConvertNumericLiteral/AbstractConvertNumericLiteralCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1333. **`src/Features/Core/Portable/ConvertToInterpolatedString/AbstractConvertConcatenationToInterpolatedStringRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1334. **`src/Features/Core/Portable/ConvertToInterpolatedString/AbstractConvertPlaceholderToInterpolatedStringRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1335. **`src/Features/Core/Portable/Copilot/ICopilotCodeAnalysisService.cs`** -> AI Confidence: **99.18%**
1336. **`src/Features/Core/Portable/Copilot/IProposalAdjusterService.cs`** -> AI Confidence: **99.18%**
1337. **`src/Features/Core/Portable/Debugging/AbstractBreakpointResolver.cs`** -> AI Confidence: **99.18%**
1338. **`src/Features/Core/Portable/Debugging/AbstractDataTipInfoGetter.cs`** -> AI Confidence: **99.18%**
1339. **`src/Features/Core/Portable/Debugging/DebugInformationReaderProvider.cs`** -> AI Confidence: **99.18%**
1340. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService.HostAnalyzerInfo.cs`** -> AI Confidence: **99.18%**
1341. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService.IncrementalMemberEditAnalyzer.cs`** -> AI Confidence: **99.18%**
1342. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_CompilationWithAnalyzersPair.cs`** -> AI Confidence: **99.18%**
1343. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_GetDiagnosticsForSpan.cs`** -> AI Confidence: **99.18%**
1344. **`src/Features/Core/Portable/DocumentationComments/AbstractDocumentationCommentSnippetService.cs`** -> AI Confidence: **99.18%**
1345. **`src/Features/Core/Portable/EditAndContinue/ActiveStatementsMap.cs`** -> AI Confidence: **99.18%**
1346. **`src/Features/Core/Portable/EditAndContinue/EditAndContinueService.cs`** -> AI Confidence: **99.18%**
1347. **`src/Features/Core/Portable/EditAndContinue/EmitSolutionUpdateResults.cs`** -> AI Confidence: **99.18%**
1348. **`src/Features/Core/Portable/EditAndContinue/Remote/IRemoteEditAndContinueService.cs`** -> AI Confidence: **99.18%**
1349. **`src/Features/Core/Portable/EditAndContinue/Remote/RemoteDebuggingSessionProxy.cs`** -> AI Confidence: **99.18%**
1350. **`src/Features/Core/Portable/EditAndContinue/Remote/RemoteEditAndContinueServiceProxy.cs`** -> AI Confidence: **99.18%**
1351. **`src/Features/Core/Portable/EditAndContinue/Utilities/Extensions.cs`** -> AI Confidence: **99.18%**
1352. **`src/Features/Core/Portable/EmbeddedLanguages/DateAndTime/DateAndTimeEmbeddedCompletionProvider.cs`** -> AI Confidence: **99.18%**
1353. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexClassifier.cs`** -> AI Confidence: **99.18%**
1354. **`src/Features/Core/Portable/EmbeddedLanguages/StackFrame/StackFrameNodeDefinitions.cs`** -> AI Confidence: **99.18%**
1355. **`src/Features/Core/Portable/Extensions/ExtensionFolder.cs`** -> AI Confidence: **99.18%**
1356. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/API/UnitTestingHotReloadService.cs`** -> AI Confidence: **99.18%**
1357. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.AbstractUnitTestingPriorityProcessor.cs`** -> AI Confidence: **99.18%**
1358. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingIncrementalAnalyzerProcessor.cs`** -> AI Confidence: **99.18%**
1359. **`src/Features/Core/Portable/ExternalAccess/VSTypeScript/VSTypeScriptClassificationService.cs`** -> AI Confidence: **99.18%**
1360. **`src/Features/Core/Portable/ExtractClass/AbstractExtractClassRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1361. **`src/Features/Core/Portable/ExtractInterface/AbstractExtractInterfaceService.cs`** -> AI Confidence: **99.18%**
1362. **`src/Features/Core/Portable/ExtractMethod/MethodExtractor.CodeGenerator.cs`** -> AI Confidence: **99.18%**
1363. **`src/Features/Core/Portable/ExtractMethod/MethodExtractor.cs`** -> AI Confidence: **99.18%**
1364. **`src/Features/Core/Portable/ExtractMethod/SelectionResult.cs`** -> AI Confidence: **99.18%**
1365. **`src/Features/Core/Portable/FindUsages/AbstractFindUsagesService_FindImplementations.cs`** -> AI Confidence: **99.18%**
1366. **`src/Features/Core/Portable/FindUsages/DefinitionItem.DetachedDefinitionItem.cs`** -> AI Confidence: **99.18%**
1367. **`src/Features/Core/Portable/FindUsages/FindUsagesHelpers.cs`** -> AI Confidence: **99.18%**
1368. **`src/Features/Core/Portable/Formatting/AbstractNewDocumentFormattingService.cs`** -> AI Confidence: **99.18%**
1369. **`src/Features/Core/Portable/FullyQualify/AbstractFullyQualifyService.cs`** -> AI Confidence: **99.18%**
1370. **`src/Features/Core/Portable/GenerateComparisonOperators/GenerateComparisonOperatorsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1371. **`src/Features/Core/Portable/GenerateConstructors/AbstractGenerateConstructorsCodeRefactoringProvider.State.cs`** -> AI Confidence: **99.18%**
1372. **`src/Features/Core/Portable/GenerateEqualsAndGetHashCodeFromMembers/GenerateEqualsAndHashWithDialogCodeAction.cs`** -> AI Confidence: **99.18%**
1373. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.CodeAction.cs`** -> AI Confidence: **99.18%**
1374. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.GenerateNamedType.cs`** -> AI Confidence: **99.18%**
1375. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.cs`** -> AI Confidence: **99.18%**
1376. **`src/Features/Core/Portable/GoToBase/AbstractGoToBaseService.cs`** -> AI Confidence: **99.18%**
1377. **`src/Features/Core/Portable/GoToDefinition/GoToDefinitionFeatureHelpers.cs`** -> AI Confidence: **99.18%**
1378. **`src/Features/Core/Portable/InheritanceMargin/AbstractInheritanceMarginService_Helpers.cs`** -> AI Confidence: **99.18%**
1379. **`src/Features/Core/Portable/InitializeParameter/AbstractInitializeParameterCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1380. **`src/Features/Core/Portable/InlineHints/AbstractInlineParameterNameHintsService.cs`** -> AI Confidence: **99.18%**
1381. **`src/Features/Core/Portable/IntroduceUsingStatement/AbstractIntroduceUsingStatementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1382. **`src/Features/Core/Portable/IntroduceVariable/AbstractIntroduceVariableService.IntroduceVariableCodeAction.cs`** -> AI Confidence: **99.18%**
1383. **`src/Features/Core/Portable/InvertIf/AbstractInvertIfCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1384. **`src/Features/Core/Portable/InvertLogical/AbstractInvertLogicalCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1385. **`src/Features/Core/Portable/MetadataAsSource/SymbolMappingServiceFactory.cs`** -> AI Confidence: **99.18%**
1386. **`src/Features/Core/Portable/NameTupleElement/AbstractNameTupleElementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1387. **`src/Features/Core/Portable/NavigateTo/AbstractNavigateToSearchService.CachedDocumentSearch.cs`** -> AI Confidence: **99.18%**
1388. **`src/Features/Core/Portable/NavigateTo/AbstractNavigateToSearchService.cs`** -> AI Confidence: **99.18%**
1389. **`src/Features/Core/Portable/NavigateTo/INavigateToSearcherHost.cs`** -> AI Confidence: **99.18%**
1390. **`src/Features/Core/Portable/NavigateTo/IRemoteNavigateToSearchService.cs`** -> AI Confidence: **99.18%**
1391. **`src/Features/Core/Portable/NavigateTo/NavigateToSearcher.cs`** -> AI Confidence: **99.18%**
1392. **`src/Features/Core/Portable/NavigateTo/RoslynNavigateToItem.cs`** -> AI Confidence: **99.18%**
1393. **`src/Features/Core/Portable/Navigation/AbstractNavigableItemsService.cs`** -> AI Confidence: **99.18%**
1394. **`src/Features/Core/Portable/Navigation/IDefinitionLocationService.cs`** -> AI Confidence: **99.18%**
1395. **`src/Features/Core/Portable/NavigationBar/AbstractNavigationBarItemService.cs`** -> AI Confidence: **99.18%**
1396. **`src/Features/Core/Portable/Options/EditorConfig/EditorConfigOptionsEnumerator.cs`** -> AI Confidence: **99.18%**
1397. **`src/Features/Core/Portable/PdbSourceDocument/PdbSourceDocumentMetadataAsSourceFileProvider.cs`** -> AI Confidence: **99.18%**
1398. **`src/Features/Core/Portable/PullMemberUp/AbstractPullMemberUpRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1399. **`src/Features/Core/Portable/PullMemberUp/MembersPuller.cs`** -> AI Confidence: **99.18%**
1400. **`src/Features/Core/Portable/Rename/SymbolicRenameInfo.cs`** -> AI Confidence: **99.18%**
1401. **`src/Features/Core/Portable/ReplaceConditionalWithStatements/AbstractReplaceConditionalWithStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1402. **`src/Features/Core/Portable/ReplaceDocCommentTextWithTag/AbstractReplaceDocCommentTextWithTagCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `src/Compilers/CSharp/Portable/Binder/Semantics/OverloadResolution/MethodTypeInference.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncMethodBuilderOverrideTests.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenNullCoalescingAssignmentTests.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenReadOnlySpanConstructionTest.cs` -> **100.0%** Exposure
### Exploit Generation Surface
- `eng/common/cross/install-debs.py` -> **100.0%** Exposure
- `eng/ensure-sources-synced.cs` -> **100.0%** Exposure
- `eng/generate-compiler-code.cs` -> **100.0%** Exposure
- `eng/snap.cs` -> **100.0%** Exposure
- `src/Analyzers/CSharp/Analyzers/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionDiagnosticAnalyzer.Analyzer.cs` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `eng/common/init-tools-native.ps1` -> **100.0%** Exposure
- `eng/common/cross/install-debs.py` -> **100.0%** Exposure
- `eng/generate-compiler-code.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Portable/Parser/Blender.Cursor.cs` -> **100.0%** Exposure
- `src/Compilers/Core/CodeAnalysisTest/CompilerResolverTests.cs` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `.github/skills/ci-analysis/scripts/Get-CIStatus.ps1` -> **100.0%** Exposure
- `.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1` -> **100.0%** Exposure
- `eng/common/dotnet-install.ps1` -> **100.0%** Exposure
- `eng/common/internal-feed-operations.ps1` -> **100.0%** Exposure
- `eng/common/native/install-tool.ps1` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `988` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `84094` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/UnitTests/MetaAnalyzers/SymbolIsBannedInAnalyzersTests.cs` (CSHARP) -> Cumulative Risk: **1042.3**
- **Archetype:** `file_cluster_4` (Distance: 11.121 IQR)
- **Magnitude:** 204.42 | **LOC:** 301 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `UseBannedApi_ISourceGenerator` (Impact: 25.4), `VerifyVB.Diagnostic` (Impact: 11.1), `VerifyCS.Diagnostic` (Impact: 11.0)

### 2. `src/VisualStudio/Core/Def/Library/AbstractObjectList.cs` (CSHARP) -> Cumulative Risk: **1017.18**
- **Archetype:** `file_cluster_8` (Distance: 12.386 IQR)
- **Magnitude:** 424.08 | **LOC:** 408 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 94.4%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `IVsBrowseContainersList.GetContainerData` (Impact: 18.5), `IVsSimpleObjectList2.GetNavInfo` (Impact: 15.8), `IVsSimpleObjectList2.FillDescription2` (Impact: 15.6)

### 3. `src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/MessageBoxInProcess.cs` (CSHARP) -> Cumulative Risk: **1010.15**
- **Archetype:** `file_cluster_4` (Distance: 14.919 IQR)
- **Magnitude:** 321.12 | **LOC:** 232 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ShowHotReloadDialog` (Impact: 108.2), `ShowMessageBox` (Impact: 31.5), `InitializeCoreAsync` (Impact: 20.2)

### 4. `src/Workspaces/Core/Portable/Workspace/Solution/TextDocumentState.cs` (CSHARP) -> Cumulative Risk: **1000.14**
- **Archetype:** `file_cluster_4` (Distance: 12.364 IQR)
- **Magnitude:** 308.9 | **LOC:** 231 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 94.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `TryGetText` (Impact: 18.5), `GetNewerVersion` (Impact: 16.4), `GetTextAndVersionAsync` (Impact: 15.2)

### 5. `src/Compilers/Core/Portable/InternalUtilities/ThreadSafeFlagOperations.cs` (CSHARP) -> Cumulative Risk: **995.31**
- **Archetype:** `file_cluster_4` (Distance: 11.788 IQR)
- **Magnitude:** 126.56 | **LOC:** 60 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `Set` (Impact: 21.5), `Set` (Impact: 21.5), `Clear` (Impact: 21.5)

### 6. `src/VisualStudio/Core/Test.Next/Options/VisualStudioSettingsOptionPersisterTests.cs` (CSHARP) -> Cumulative Risk: **994.61**
- **Archetype:** `file_cluster_13` (Distance: 12.564 IQR)
- **Magnitude:** 383.04 | **LOC:** 315 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 96.2%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetRoundtripTestCases` (Impact: 54.3), `Roundtrip_DefaultImmutableArray` (Impact: 41.5), `SettingsManagerReadOptionValue_Error` (Impact: 33.9)

### 7. `src/Features/Core/Portable/CodeFixes/Configuration/ConfigureSeverity/ConfigureSeverityLevelCodeFixProvider.cs` (CSHARP) -> Cumulative Risk: **988.04**
- **Archetype:** `file_cluster_13` (Distance: 11.363 IQR)
- **Magnitude:** 127.28 | **LOC:** 118 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 94.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `GetConfigurations` (Impact: 73.2), `GetFixAllProvider` (Impact: 6.1), `IsFixableDiagnostic` (Impact: 3.5)

### 8. `src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/VisualStudioInstanceFactory.cs` (CSHARP) -> Cumulative Risk: **985.18**
- **Archetype:** `file_cluster_13` (Distance: 11.293 IQR)
- **Magnitude:** 292.12 | **LOC:** 505 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `UpdateCurrentlyRunningInstanceAsync` (Impact: 93.0), `TakeSnapshotEveryTimeSpanUntilProcessExi` (Impact: 27.5), `AssemblyResolveHandler` (Impact: 21.9)

### 9. `src/Interactive/HostTest/AbstractInteractiveHostTests.cs` (CSHARP) -> Cumulative Risk: **981.08**
- **Archetype:** `file_cluster_4` (Distance: 10.693 IQR)
- **Magnitude:** 248.58 | **LOC:** 223 | **CtrlFlow:** 21.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `ReadOutputToEnd` (Impact: 52.4), `AbstractInteractiveHostTests` (Impact: 25.5), `InitializeAsync` (Impact: 18.2)

### 10. `src/EditorFeatures/CSharpTest/SymbolKey/SymbolKeyTests.cs` (CSHARP) -> Cumulative Risk: **981.05**
- **Archetype:** `file_cluster_4` (Distance: 10.929 IQR)
- **Magnitude:** 238.04 | **LOC:** 323 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `ResolveBodySymbolsInMultiProjectReferenc` (Impact: 67.7), `TestGenericsAndNullability` (Impact: 18.1), `FileType_01` (Impact: 8.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.853 IQR)
- **Top Global Matches:** file_cluster_8: 13.853, file_cluster_11: 14.001, file_cluster_13: 14.091
- **Magnitude:** 17414.52 | **LOC:** 14680 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 51.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 167
- **Risk Profile:** Cognitive Load (71.7228%), Tech Debt (13.4466%)
**Top Internal Functions/Classes:**
  * `ParseMemberName` (Impact: 4720.3 | O(2^N) | DB: 95)
  * `ParseSwitchStatement` (Impact: 3022.7 | O(N^6) | DB: 85)
  * `ParseNamespaceDeclarationCore` (Impact: 1611.8 | O(N^6) | DB: 167)
  * `ScanExplicitlyTypedLambda` (Impact: 1581.4 | O(N^6) | DB: 60)
  * `TryParseConversionOperatorDeclaration` (Impact: 1403.4 | O(N^6) | DB: 133)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1737`, `structural_boundaries: 1186`, `args: 484`, `func_start: 1022`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 8`, `state_mutation: 1769`, `dead_code: 37`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`, `orphaned_logic: 21`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 161`, `doc: 143`, `immutability_locks: 12`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Text, System.Linq, Roslyn.Utilities, System.Diagnostics.CodeAnalysis, System.Threading, System, Microsoft.CodeAnalysis.Syntax.InternalSyntax, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.203 IQR)
- **Top Global Matches:** file_cluster_8: 14.203, file_cluster_11: 14.373, file_cluster_13: 14.425
- **Magnitude:** 15980.04 | **LOC:** 14301 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 51.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 104
- **Risk Profile:** Cognitive Load (51.4948%), Tech Debt (55.5392%)
**Top Internal Functions/Classes:**
  * `VisitArgumentEvaluateEpilogue` (Impact: 1819.8 | O(N^6) | DB: 63)
  * `VisitNullCoalescingOperator` (Impact: 1720.8 | O(N^6) | DB: 104)
  * `getMembersNeedingDefaultInitialState` (Impact: 1600.1 | O(N^6) | DB: 79)
  * `VisitLocalFunctionUse` (Impact: 1210.6 | O(N^6) | DB: 46)
  * `Scan` (Impact: 412.2 | O(2^N) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1602`, `structural_boundaries: 991`, `args: 471`, `func_start: 1382`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 1517`, `dead_code: 18`, `planned_debt: 4`, `duplicate_logic: 24`, `orphaned_logic: 62`
* *Architecture:* `api: 158`, `import: 14`
* *Defense:* `safety: 395`, `doc: 223`, `immutability_locks: 119`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, System.Linq, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, System.Collections.Concurrent, System.Diagnostics.CodeAnalysis, System.Text, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.335 IQR)
- **Top Global Matches:** file_cluster_0: 14.335, file_cluster_11: 14.536, file_cluster_8: 14.626
- **Magnitude:** 15857.26 | **LOC:** 24845 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (16.1677%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnionConversion_37_Cast_ToNullableOfUnio` (Impact: 183.2 | O(N^3) | DB: 4)
  * `Exhaustiveness_01` (Impact: 183.0 | O(N^4))
  * `UnionMatching_37_SwitchStatement_01` (Impact: 169.7 | O(N^3))
  * `NullableAnalysis_20_State_From_Null_Test` (Impact: 168.5 | O(N^4) | DB: 10)
  * `NullableAnalysis_24_State_From_NotType_T` (Impact: 168.3 | O(N^4) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2421`, `structural_boundaries: 4262`, `args: 3755`, `func_start: 5615`, `class_start: 852`
* *Risk/State:* `safety_bypasses: 308`, `high_risk_execution: 23`, `state_mutation: 2024`, `dead_code: 252`, `planned_debt: 3`, `duplicate_logic: 16`, `orphaned_logic: 233`
* *Architecture:* `api: 1827`, `import: 13`
* *Defense:* `safety: 590`, `test: 549`, `immutability_locks: 327`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Roslyn.Test.Utilities, System.Linq, System, Microsoft.CodeAnalysis.Operations, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Xunit, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.084 IQR)
- **Top Global Matches:** file_cluster_0: 14.084, file_cluster_8: 14.147, file_cluster_11: 14.198
- **Magnitude:** 15530.38 | **LOC:** 15896 | **CtrlFlow:** 63.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 70
- **Risk Profile:** Cognitive Load (35.364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BinaryOperators` (Impact: 3721.2 | O(N^5) | DB: 3)
  * `Conversions` (Impact: 2054.6 | O(N^6))
  * `IncrementOperators` (Impact: 574.5 | O(N^6) | DB: 4)
  * `MaskShiftCount` (Impact: 433.2 | O(N^5))
  * `UnaryOperators` (Impact: 406.8 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3681`, `structural_boundaries: 2152`, `args: 936`, `func_start: 5332`, `class_start: 540`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 12`, `state_mutation: 924`, `dead_code: 92`, `planned_debt: 17`, `duplicate_logic: 17`, `orphaned_logic: 162`
* *Architecture:* `api: 979`, `concurrency: 24`, `import: 19`
* *Defense:* `safety: 348`, `doc: 45`, `test: 432`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, Roslyn.Test.Utilities, System.Linq, Roslyn.Utilities, System.Console, Microsoft.CodeAnalysis.Emit, System, nuint...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.095 IQR)
- **Top Global Matches:** file_cluster_0: 17.095, file_cluster_11: 17.223, file_cluster_17: 17.47
- **Magnitude:** 14774.28 | **LOC:** 6187 | **CtrlFlow:** 77.8% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 227
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SwitchStatement` (Impact: 1910.0 | O(N^4) | DB: 13)
  * `TernaryOperator` (Impact: 1908.3 | O(N^4) | DB: 227)
    * *Intent:* // Whidbey bug #467493
  * `IfStatement` (Impact: 741.0 | O(N^4) | DB: 70)
  * `LogicalExpression` (Impact: 593.1 | O(N^4) | DB: 87)
  * `WhileStatement` (Impact: 566.4 | O(N^4) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2007`, `structural_boundaries: 574`, `args: 563`, `func_start: 1308`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 2687`, `dead_code: 131`, `planned_debt: 1`, `fragile_debt: 27`, `duplicate_logic: 10`, `orphaned_logic: 118`
* *Architecture:* `api: 390`, `import: 29`
* *Defense:* `safety: 345`, `test: 113`, `sync_locks: 7`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Immutable, Roslyn.Test.Utilities, System.Linq, System, Microsoft.CodeAnalysis.CSharp.Symbols, System.Runtime.InteropServices, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Xunit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SyntaxFacts/ISyntaxFacts.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_16` (Drift: 15.472 IQR)
- **Top Global Matches:** file_cluster_16: 15.472, file_cluster_13: 15.483, file_cluster_8: 15.613
- **Magnitude:** 14024.38 | **LOC:** 586 | **CtrlFlow:** 90.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (48.3309%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 11`, `args: 176`, `func_start: 177`, `class_start: 1`
* *Risk/State:* `state_mutation: 213`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 2`, `doc: 74`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Immutable, Microsoft.CodeAnalysis.Text, System.Diagnostics.CodeAnalysis, System.Threading, System, System.Collections.Generic, Microsoft.CodeAnalysis.PooledObjects
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/Emit/NumericIntPtrTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.588 IQR)
- **Top Global Matches:** file_cluster_8: 13.588, file_cluster_0: 13.756, file_cluster_11: 13.898
- **Magnitude:** 12632.18 | **LOC:** 11855 | **CtrlFlow:** 66.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (32.9763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BinaryOperators` (Impact: 3519.6 | O(N^5) | DB: 4)
  * `Conversions` (Impact: 2029.7 | O(N^6))
  * `IncrementOperators` (Impact: 613.5 | O(N^6) | DB: 4)
  * `MaskShiftCount` (Impact: 427.5 | O(N^5))
  * `IncrementOperators_RefOperand` (Impact: 418.5 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2788`, `structural_boundaries: 1401`, `args: 735`, `func_start: 3616`, `class_start: 312`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 12`, `state_mutation: 528`, `dead_code: 17`, `duplicate_logic: 2`, `orphaned_logic: 106`
* *Architecture:* `api: 609`, `concurrency: 48`, `import: 35`
* *Defense:* `safety: 392`, `doc: 20`, `test: 181`, `immutability_locks: 299`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, Microsoft.CodeAnalysis.CSharp, System, System.Collections.Generic, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.653 IQR)
- **Top Global Matches:** file_cluster_0: 13.653, file_cluster_11: 13.699, file_cluster_4: 13.721
- **Magnitude:** 11882.36 | **LOC:** 29709 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (41.9113%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnscopedRefInImplementation_Indexer_01` (Impact: 439.2 | O(N^6) | DB: 29)
  * `UnscopedRefInImplementation_Property_01` (Impact: 407.9 | O(N^6) | DB: 29)
  * `AwaitForeach_IAsyncEnumerableT_07` (Impact: 360.8 | O(N^6) | DB: 6)
  * `AwaitForeach_IAsyncEnumerableT_05` (Impact: 313.7 | O(N^6) | DB: 6)
  * `AwaitForeach_IAsyncEnumerableT_04` (Impact: 304.2 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 786`, `structural_boundaries: 2712`, `args: 981`, `func_start: 2725`, `class_start: 424`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2326`, `dead_code: 108`, `planned_debt: 8`, `duplicate_logic: 5`, `orphaned_logic: 171`
* *Architecture:* `api: 820`, `concurrency: 963`, `import: 190`
* *Defense:* `safety: 219`, `test: 445`, `immutability_locks: 52`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Threading.Tasks, Roslyn.Test.Utilities, System.Linq, System.Collections, System.Diagnostics.CodeAnalysis, System.Threading, Microsoft.CodeAnalysis.Emit, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.209 IQR)
- **Top Global Matches:** file_cluster_4: 12.209, file_cluster_8: 12.362, file_cluster_0: 12.523
- **Magnitude:** 10880.9 | **LOC:** 15181 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 40.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (81.9195%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestWithInterface_OnStruct_ImplicitInter` (Impact: 602.5 | O(N^6) | DB: 35)
  * `TestWithPattern_RefStructEnumerator_Asyn` (Impact: 162.7 | O(N^6) | DB: 2)
  * `TestWithUIntToIntConversion` (Impact: 105.3 | O(N^6) | DB: 5)
  * `TestWithObsoletePatternMethodsViaExtensi` (Impact: 99.0 | O(N^6) | DB: 2)
    * *Intent:* // Code size 40 (0x28)
  * `TestWithPattern_RefStructCurrent_AsyncIt` (Impact: 85.3 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 757`, `structural_boundaries: 2737`, `args: 1084`, `func_start: 1870`, `class_start: 520`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 441`, `dead_code: 11`, `planned_debt: 9`, `duplicate_logic: 63`, `orphaned_logic: 86`
* *Architecture:* `api: 1371`, `concurrency: 3275`, `import: 334`
* *Defense:* `safety: 141`, `test: 259`, `immutability_locks: 102`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, System.Collections, System.Threading, Microsoft.CodeAnalysis.CSharp.Syntax, N2, System, System.Collections.Generic, Xunit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.764 IQR)
- **Top Global Matches:** file_cluster_8: 10.764, file_cluster_7: 11.279, file_cluster_1: 11.504
- **Magnitude:** 9768.48 | **LOC:** 2674 | **CtrlFlow:** 97.8% | **Authorship Centralization:** 28.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 57
- **Risk Profile:** Cognitive Load (56.5721%), Tech Debt (16.3932%)
**Top Internal Functions/Classes:**
  * `IsBuildOnlyDiagnostic` (Impact: 6710.9 | O(N^5))
    * *Intent:* // Note: when adding a warning here, consider whether it should be registered as a nullability warni...
  * `GetWarningLevel` (Impact: 2561.8 | O(N^5))
  * `PreventsSuccessfulDelegateConversion` (Impact: 119.1 | O(N^5))
    * *Intent:* /// <summary>
  * `GetSeverity` (Impact: 68.7 | O(N^4))
  * `PreventsSuccessfulDelegateConversion` (Impact: 44.7 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2368`, `structural_boundaries: 54`, `args: 23`, `func_start: 79`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`, `duplicate_logic: 5`, `orphaned_logic: 10`
* *Architecture:* `api: 17`, `import: 7`
* *Defense:* `doc: 21`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, System.Reflection, Roslyn.Utilities, System, System.Collections.Generic, System.Diagnostics, System.Globalization
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.402 IQR)
- **Top Global Matches:** file_cluster_0: 13.402, file_cluster_4: 13.445, file_cluster_11: 13.7
- **Magnitude:** 9224.52 | **LOC:** 22795 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 112
- **Risk Profile:** Cognitive Load (64.6721%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AssertParameterScope` (Impact: 303.6 | O(N^6) | DB: 19)
  * `Handle` (Impact: 253.8 | O(N^6) | DB: 4)
  * `Handle` (Impact: 253.1 | O(N^6) | DB: 4)
  * `Handle11` (Impact: 253.1 | O(N^6) | DB: 4)
  * `Handle` (Impact: 198.5 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 2011`, `args: 782`, `func_start: 2093`, `class_start: 242`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 812`, `dead_code: 55`, `duplicate_logic: 76`, `orphaned_logic: 148`
* *Architecture:* `api: 695`, `concurrency: 804`, `import: 44`
* *Defense:* `safety: 273`, `doc: 91`, `test: 1092`, `sync_locks: 134`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Diagnostics, System.Linq, System.Threading, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, System, System.Collections.Generic, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Features/CSharpTest/ExtractMethod/ExtractMethodCodeRefactoringTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.958 IQR)
- **Top Global Matches:** file_cluster_8: 11.958, file_cluster_4: 12.223, file_cluster_0: 12.295
- **Magnitude:** 9079.56 | **LOC:** 8787 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (32.1776%), Tech Debt (70.3054%)
**Top Internal Functions/Classes:**
  * `TestFlowControl_BreakAndContinueAndRetur` (Impact: 152.1 | O(N^6))
  * `TestFlowControl_BreakAndContinueAndRetur` (Impact: 144.7 | O(N^6))
  * `TestFlowControl_BreakAndContinueAndRetur` (Impact: 144.3 | O(N^6))
  * `TestFlowControl_BreakAndContinueAndFallT` (Impact: 128.5 | O(N^6))
  * `TestFlowControl_BreakAndContinueAndFallT` (Impact: 128.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 816`, `structural_boundaries: 1780`, `args: 968`, `func_start: 1239`, `class_start: 438`
* *Risk/State:* `safety_bypasses: 6`, `high_risk_execution: 4`, `state_mutation: 483`, `duplicate_logic: 38`, `orphaned_logic: 168`
* *Architecture:* `api: 359`, `concurrency: 869`, `import: 176`
* *Defense:* `safety: 67`, `test: 113`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Linq, Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CodeRefactorings.ExtractMethod, System.Threading, Microsoft.CodeAnalysis.CSharp.CodeStyle, Microsoft.CodeAnalysis.Testing, Microsoft.CodeAnalysis.Editor.UnitTests.CodeActions, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.612 IQR)
- **Top Global Matches:** file_cluster_8: 12.612, file_cluster_0: 13.006, file_cluster_7: 13.081
- **Magnitude:** 9034.74 | **LOC:** 12119 | **CtrlFlow:** 57.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 745
- **Risk Profile:** Cognitive Load (21.9866%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `StringSwitch_HashTableSwitch_02` (Impact: 1008.4 | O(N^4) | DB: 78)
  * `NullableAsSwitchExpression_02` (Impact: 340.2 | O(N^4))
  * `MultipleSwitchSectionsWithGotoCase` (Impact: 243.1 | O(N^4) | DB: 1)
  * `NullableEnumTypeSwitchArgumentExpression` (Impact: 179.7 | O(N^4) | DB: 2)
  * `NotDegenerateSwitch006` (Impact: 154.0 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1162`, `structural_boundaries: 864`, `args: 365`, `func_start: 864`, `class_start: 124`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 12`, `state_mutation: 1705`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 90`
* *Architecture:* `api: 318`, `import: 27`
* *Defense:* `safety: 114`, `doc: 9`, `test: 68`, `immutability_locks: 74`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Threading.Tasks, Microsoft.CodeAnalysis.CodeGen, System.Linq, System.Text, System, System.Collections.Generic, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests3.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.885 IQR)
- **Top Global Matches:** file_cluster_0: 12.885, file_cluster_8: 13.021, file_cluster_11: 13.028
- **Magnitude:** 8776.84 | **LOC:** 7663 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 33.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (16.398%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `New9PatternsSemanticModel_01` (Impact: 581.2 | O(N^6))
  * `New9PatternsSemanticModel_02` (Impact: 484.5 | O(N^6) | DB: 8)
  * `TargetTypedSwitch_AnyTypedSwitchWithoutT` (Impact: 284.6 | O(N^6) | DB: 2)
  * `DisallowDesignatorsUnderNotAndOr` (Impact: 283.8 | O(N^4) | DB: 2)
  * `OutputType_02` (Impact: 268.2 | O(N^3) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1081`, `structural_boundaries: 1776`, `args: 828`, `func_start: 1693`, `class_start: 275`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 2`, `state_mutation: 553`, `dead_code: 35`, `duplicate_logic: 17`, `orphaned_logic: 137`
* *Architecture:* `api: 363`, `import: 59`
* *Defense:* `safety: 198`, `doc: 3`, `test: 456`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Roslyn.Test.Utilities, System.Linq, System.Console, System.Text, System, System.Collections.Generic, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/RefEscapingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.462 IQR)
- **Top Global Matches:** file_cluster_0: 14.462, file_cluster_11: 14.692, file_cluster_13: 14.71
- **Magnitude:** 8702.58 | **LOC:** 15468 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(N^6) | **DB Complexity:** 42
- **Risk Profile:** Cognitive Load (71.3326%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RefLikeEscapeMixingIndexer1` (Impact: 146.3 | O(N^6) | DB: 25)
  * `MismatchedRefTernaryEscapeBlock` (Impact: 139.0 | O(N^4) | DB: 42)
  * `MismatchedRefTernaryEscapeBlock_UnsafeCo` (Impact: 139.0 | O(N^4) | DB: 42)
  * `PropertyEscape` (Impact: 113.8 | O(N^6) | DB: 11)
  * `ObjectInitializer_Constructor_Escape` (Impact: 92.8 | O(N^6) | DB: 29)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 2380`, `args: 1336`, `func_start: 2151`, `class_start: 324`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2781`, `dead_code: 179`, `planned_debt: 4`, `duplicate_logic: 23`, `orphaned_logic: 227`
* *Architecture:* `api: 877`, `concurrency: 129`, `import: 363`
* *Defense:* `safety: 111`, `test: 202`, `sync_locks: 1`, `immutability_locks: 87`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Threading.Tasks, Roslyn.Test.Utilities, System.Linq, Roslyn.Utilities, System.Collections, System.Diagnostics.CodeAnalysis, System, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncIteratorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.28 IQR)
- **Top Global Matches:** file_cluster_4: 12.28, file_cluster_8: 12.387, file_cluster_0: 12.425
- **Magnitude:** 8636.84 | **LOC:** 11935 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 28.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 20
- **Risk Profile:** Cognitive Load (60.1604%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MissingTypeAndMembers_IAsyncEnumerable` (Impact: 1196.8 | O(N^6) | DB: 20)
  * `TryFinally_YieldBreakInDisposeMode` (Impact: 153.0 | O(N^6) | DB: 2)
  * `AsyncIteratorWithCustomCode` (Impact: 138.7 | O(N^6))
  * `TryFinally_Nested_WithYields` (Impact: 109.9 | O(N^4))
  * `TryFinally_MultipleSameLevelTrys` (Impact: 101.9 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 989`, `structural_boundaries: 2561`, `args: 406`, `func_start: 1841`, `class_start: 252`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 202`, `dead_code: 32`, `duplicate_logic: 37`, `orphaned_logic: 103`
* *Architecture:* `api: 427`, `concurrency: 2229`, `import: 292`
* *Defense:* `safety: 351`, `doc: 3`, `test: 164`, `sync_locks: 5`, `immutability_locks: 27`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Linq, System.Collections, System.Text, System.Threading, Microsoft.CodeAnalysis.Emit, System.Reflection.PortableExecutable, Microsoft.CodeAnalysis.CSharp.Syntax, System.Reflection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.169 IQR)
- **Top Global Matches:** file_cluster_8: 14.169, file_cluster_11: 14.284, file_cluster_13: 14.308
- **Magnitude:** 8111.2 | **LOC:** 11842 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 20.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 82
- **Risk Profile:** Cognitive Load (41.3871%), Tech Debt (58.0744%)
**Top Internal Functions/Classes:**
  * `BindArgList` (Impact: 1176.4 | O(N^6) | DB: 82)
  * `ResolveExtension` (Impact: 878.7 | O(N^6) | DB: 42)
    * *Intent:* // SPEC begins // // An array-creation-expression is used to create a new instance of an array-type....
  * `BindConstructorInitializerCore` (Impact: 688.0 | O(N^6) | DB: 46)
  * `BindElementOrIndexerAccess` (Impact: 323.9 | O(N^6) | DB: 30)
    * *Intent:* // If the bound could have been converted to int, then it was. If it could not have been
  * `GetMethodGroupOrLambdaDelegateType` (Impact: 302.5 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 789`, `structural_boundaries: 604`, `args: 318`, `func_start: 784`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 990`, `dead_code: 23`, `planned_debt: 3`, `duplicate_logic: 18`, `orphaned_logic: 33`
* *Architecture:* `api: 33`, `import: 15`
* *Defense:* `safety: 187`, `doc: 179`, `immutability_locks: 74`, `cleanup: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, System.Reflection, Microsoft.CodeAnalysis.Text, System.Linq, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, System.Diagnostics.CodeAnalysis, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Workspaces/CSharpTest/Formatting/FormattingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.145 IQR)
- **Top Global Matches:** file_cluster_8: 12.145, file_cluster_0: 12.348, file_cluster_4: 12.491
- **Magnitude:** 7937.22 | **LOC:** 12767 | **CtrlFlow:** 24.6% | **Authorship Centralization:** 73.3%
- **Algorithmic:** O(N^6) | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (29.5022%), Tech Debt (77.0704%)
**Top Internal Functions/Classes:**
  * `TestWrappingNonDefault` (Impact: 201.4 | O(N^6) | DB: 5)
  * `TestWrappingNonDefault_FormatBlock` (Impact: 200.9 | O(N^6) | DB: 2)
  * `TestWrappingNonDefault_FormatStatmtMethD` (Impact: 200.7 | O(N^6) | DB: 4)
  * `TestWrappingDefault` (Impact: 182.1 | O(N^6) | DB: 2)
  * `TestSpacingOptionAroundControlFlow` (Impact: 156.4 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 756`, `structural_boundaries: 2313`, `args: 1383`, `func_start: 1538`, `class_start: 885`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 28`, `state_mutation: 409`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 8`, `duplicate_logic: 15`, `orphaned_logic: 235`
* *Architecture:* `api: 703`, `concurrency: 899`, `import: 67`
* *Defense:* `safety: 177`, `doc: 16`, `test: 211`, `sync_locks: 16`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` System.Linq, Microsoft.CodeAnalysis.CSharp.Formatting.CSharpFormattingOptions2, System.Threading, System, Microsoft.CodeAnalysis.Editor.UnitTests.CodeActions, System.Data, System.Collections.Generic, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValueAssignmentTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.091 IQR)
- **Top Global Matches:** file_cluster_0: 13.091, file_cluster_8: 13.211, file_cluster_4: 13.296
- **Magnitude:** 7810.6 | **LOC:** 9496 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 187
- **Risk Profile:** Cognitive Load (53.2462%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RemoveUnusedValueAssignmentTests` (Impact: 240.0 | O(N^5) | DB: 187)
  * `IfElse_OverwrittenInAllControlFlowPaths` (Impact: 230.3 | O(N^6))
    * *Intent:* // Simple if-else.
  * `IfElse_OverwrittenInSomeControlFlowPaths` (Impact: 160.1 | O(N^6))
    * *Intent:* // Overwrite missing in if path. // Overwrite missing in else path.
  * `IfElse_OverwrittenInCondition_LogicalOpe` (Impact: 128.5 | O(N^6) | DB: 8)
  * `FixAll_MoveMultipleVariableDeclarations_` (Impact: 104.8 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 481`, `structural_boundaries: 1764`, `args: 1224`, `func_start: 1240`, `class_start: 473`
* *Risk/State:* `state_mutation: 1167`, `duplicate_logic: 57`, `orphaned_logic: 190`
* *Architecture:* `io: 2`, `api: 404`, `concurrency: 605`, `import: 164`
* *Defense:* `safety: 384`, `test: 190`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CSharp.CodeStyle, Microsoft.CodeAnalysis.Testing, Microsoft.CodeAnalysis.Editor.UnitTests.CodeActions, Microsoft.CodeAnalysis.CSharp.RemoveUnusedParametersAndValues, System, Microsoft.CodeAnalysis.Test.Utilities, Xunit.Abstractions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.756 IQR)
- **Top Global Matches:** file_cluster_8: 12.756, file_cluster_16: 13.114, file_cluster_13: 13.128
- **Magnitude:** 7516.16 | **LOC:** 8134 | **CtrlFlow:** 70.3% | **Authorship Centralization:** 80.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 68
- **Risk Profile:** Cognitive Load (52.786%), Tech Debt (60.8539%)
**Top Internal Functions/Classes:**
  * `PackBlocks` (Impact: 1463.8 | O(N^6) | DB: 68)
  * `VisitConditionalBranchCore` (Impact: 709.4 | O(2^N) | DB: 24)
    * *Intent:* /// <summary> /// This class captures information about beginning of stack frame /// and correspondi...
  * `VisitSwitch` (Impact: 452.8 | O(N^6) | DB: 12)
  * `VisitForToLoop` (Impact: 367.4 | O(N^6) | DB: 37)
  * `VisitConditionalAccess` (Impact: 286.5 | O(N^6) | DB: 12)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 877`, `structural_boundaries: 370`, `args: 264`, `func_start: 986`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `high_risk_execution: 4`, `state_mutation: 630`, `dead_code: 6`, `fragile_debt: 1`, `duplicate_logic: 5`, `orphaned_logic: 59`
* *Architecture:* `api: 81`, `import: 10`
* *Defense:* `safety: 111`, `doc: 42`, `immutability_locks: 74`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, System.Linq, Roslyn.Utilities, System.Diagnostics.CodeAnalysis, System, Microsoft.CodeAnalysis.Operations, System.Collections.Generic, System.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/SemanticErrorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.303 IQR)
- **Top Global Matches:** file_cluster_0: 13.303, file_cluster_11: 13.567, file_cluster_8: 13.61
- **Magnitude:** 7236.66 | **LOC:** 25420 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 42.9%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 54
- **Risk Profile:** Cognitive Load (20.2705%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CS0165ERR_UseDefViolation05` (Impact: 498.8 | O(N^6) | DB: 54)
  * `CS0156ERR_BadEmptyThrow_Nesting` (Impact: 373.7 | O(N^5))
    * *Intent:* // (13,26): error CS0029: Cannot implicitly convert type 'TS' to 'System.Exception'
  * `CS0156ERR_BadEmptyThrow_Lambdas` (Impact: 306.5 | O(N^5) | DB: 4)
  * `CS0165ERR_UseDefViolation03` (Impact: 192.9 | O(N^5))
  * `CS0019ERR_BadBinaryOps14` (Impact: 108.4 | O(N^4))
    * *Intent:* /// <summary> /// Conversion errors for Null Coalescing operator(??) /// </summary>
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1149`, `structural_boundaries: 2320`, `args: 1263`, `func_start: 2918`, `class_start: 598`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 19`, `state_mutation: 941`, `dead_code: 77`, `planned_debt: 6`, `duplicate_logic: 64`, `orphaned_logic: 169`
* *Architecture:* `io: 1`, `api: 1082`, `concurrency: 66`, `import: 141`
* *Defense:* `safety: 584`, `doc: 53`, `test: 397`, `sync_locks: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` System.Linq, System.Collections, System.Threading, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, System, System.Collections.Generic, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IObjectCreationExpression.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.211 IQR)
- **Top Global Matches:** file_cluster_8: 12.211, file_cluster_0: 12.605, file_cluster_13: 12.735
- **Magnitude:** 7129.32 | **LOC:** 15547 | **CtrlFlow:** 48.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (11.6466%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ObjectCreationFlow_58` (Impact: 373.1 | O(N^6) | DB: 7)
  * `ObjectCreationFlow_56` (Impact: 324.4 | O(N^6) | DB: 8)
  * `ObjectCreationFlow_57` (Impact: 324.0 | O(N^6) | DB: 7)
  * `ObjectCreationFlow_59` (Impact: 268.3 | O(N^6) | DB: 9)
  * `ObjectCreationFlow_55` (Impact: 248.6 | O(N^6) | DB: 7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 678`, `structural_boundaries: 713`, `args: 583`, `func_start: 3979`, `class_start: 194`
* *Risk/State:* `safety_bypasses: 183`, `state_mutation: 768`, `dead_code: 9`, `planned_debt: 5`, `duplicate_logic: 15`, `orphaned_logic: 111`
* *Architecture:* `api: 491`, `import: 100`
* *Defense:* `safety: 255`, `test: 111`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Linq, Microsoft.CodeAnalysis.CSharp.Syntax, System.Collections, System, System.Collections.Generic, System.Runtime.InteropServices, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Xunit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Binder/Binder_Conversions.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.926 IQR)
- **Top Global Matches:** file_cluster_8: 12.926, file_cluster_13: 13.211, file_cluster_11: 13.239
- **Magnitude:** 6867.88 | **LOC:** 4308 | **CtrlFlow:** 57.3% | **Authorship Centralization:** 40.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 72
- **Risk Profile:** Cognitive Load (51.1826%), Tech Debt (23.5795%)
**Top Internal Functions/Classes:**
  * `CreateConversion` (Impact: 2351.0 | O(2^N) | DB: 21)
  * `filterOutBadGenericMethods` (Impact: 1543.1 | O(N^6) | DB: 72)
  * `DoUncheckedConversion` (Impact: 1391.2 | O(N^6) | DB: 2)
  * `ConvertObjectCreationExpression` (Impact: 514.4 | O(N^6) | DB: 39)
  * `FoldConstantNumericConversion` (Impact: 136.6 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 613`, `structural_boundaries: 457`, `args: 127`, `func_start: 334`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 369`, `dead_code: 8`, `planned_debt: 2`, `duplicate_logic: 7`, `orphaned_logic: 1`
* *Architecture:* `api: 14`, `import: 10`
* *Defense:* `safety: 93`, `doc: 50`, `immutability_locks: 15`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Immutable, System.Linq, Microsoft.CodeAnalysis.CSharp.Syntax, Roslyn.Utilities, System.Diagnostics.CodeAnalysis, System, Microsoft.CodeAnalysis.CSharp.Symbols, System.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleTest.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.022 IQR)
- **Top Global Matches:** file_cluster_0: 13.022, file_cluster_8: 13.149, file_cluster_11: 13.247
- **Magnitude:** 6649.82 | **LOC:** 29801 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (11.4962%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MissingTypeInAlias` (Impact: 322.3 | O(N^6) | DB: 15)
  * `TupleAsMemberTests` (Impact: 137.2 | O(N^6) | DB: 1)
  * `VerifyInternalType` (Impact: 94.7 | O(2^N))
  * `RealFieldsAreNotWrapped` (Impact: 84.7 | O(N^6) | DB: 1)
  * `TestValueTuplesDefinition` (Impact: 76.1 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1294`, `structural_boundaries: 5700`, `args: 1930`, `func_start: 7008`, `class_start: 950`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 936`, `dead_code: 214`, `planned_debt: 18`, `duplicate_logic: 2`, `orphaned_logic: 189`
* *Architecture:* `api: 2155`, `concurrency: 72`, `import: 211`
* *Defense:* `safety: 485`, `test: 2629`, `immutability_locks: 231`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` alias1, System.Linq, System.Collections, System.Text, Microsoft.CodeAnalysis.CSharp.Syntax, TestResources.NetFX.ValueTuple, Roslyn.Utilities, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/LambdaTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.107 IQR)
- **Top Global Matches:** file_cluster_0: 13.107, file_cluster_11: 13.149, file_cluster_13: 13.28
- **Magnitude:** 6607.02 | **LOC:** 9469 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 37.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 49
- **Risk Profile:** Cognitive Load (40.7075%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Main` (Impact: 304.9 | O(N^4) | DB: 15)
  * `LambdaAttributes_05` (Impact: 141.5 | O(N^4))
  * `LambdaReturnType_07` (Impact: 141.3 | O(N^4))
  * `LambdaReturnType_09` (Impact: 108.1 | O(N^4) | DB: 18)
  * `LambdaReturnType_08` (Impact: 108.0 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 794`, `structural_boundaries: 3815`, `args: 1555`, `func_start: 2104`, `class_start: 368`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 721`, `dead_code: 36`, `duplicate_logic: 32`, `orphaned_logic: 190`
* *Architecture:* `api: 464`, `concurrency: 448`, `import: 220`
* *Defense:* `safety: 203`, `doc: 3`, `test: 539`, `immutability_locks: 56`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` System.Linq, System.Collections, System.Text, System.Threading, Microsoft.CodeAnalysis.Emit, System.Security.Permissions, Microsoft.CodeAnalysis.CSharp.Syntax, stdole...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Conditional.cs` (CSHARP) | Magnitude: 268.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 350, func_start: 116, macros: 102, structural_boundaries: 100
- `src/Compilers/Core/CodeAnalysisTest/Analyzers/AnalyzerConfigTests.cs` (CSHARP) | Magnitude: 1367.72 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 1613, func_start: 649, test: 449, sec_high_risk_execution: 372
- `src/Compilers/Core/CodeAnalysisTest/Collections/ImmutableDictionaryTestBase.nonnetstandard.cs` (CSHARP) | Magnitude: 252.6 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 235, func_start: 107, test: 77, sec_high_risk_execution: 72
- `src/LanguageServer/Protocol/Protocol/CompletionParams.cs` (CSHARP) | Magnitude: 25.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, doc: 12, state_mutation: 6, decorators: 6
- `src/LanguageServer/Protocol/Protocol/LocationLink.cs` (CSHARP) | Magnitude: 31.84 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 30, indent_spaces: 25, structural_boundaries: 13, decorators: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/VisualStudio/Core/Impl/SolutionExplorer/DiagnosticItem/CpsUtilities.cs` (CSHARP) | Magnitude: 22.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 19, structural_boundaries: 7, state_mutation: 6
- `src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingSolutionCrawlerProgressReporter.cs` (CSHARP) | Magnitude: 20.38 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, doc: 7, api: 5
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/Rules/AbstractFormattingRule.cs` (CSHARP) | Magnitude: 36.82 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 23, indent_spaces: 14, structural_boundaries: 11, api: 8
- `src/EditorFeatures/Core/EditAndContinue/IEditAndContinueSolutionProvider.cs` (CSHARP) | Magnitude: 14.64 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, class_start: 1, api: 1
- `src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/IUnitTestingSolutionCrawlerProgressReporter.cs` (CSHARP) | Magnitude: 11.12 | Delta: **0.121 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 16, indent_spaces: 9, structural_boundaries: 6, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `eng/common/generate-sbom-prep.sh` (SHELL) | Magnitude: 43.28 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 24, structural_boundaries: 18, branch: 12, safety_bypasses: 9
- `src/Compilers/CSharp/Portable/Symbols/TypeSymbol.cs` (CSHARP) | Magnitude: 1286.16 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 791, state_mutation: 236, branch: 155, doc: 153
- `src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs` (CSHARP) | Magnitude: 5572.36 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 2201, branch: 551, structural_boundaries: 526, state_mutation: 502
- `src/Compilers/Core/Portable/Emit/EditAndContinue/DefinitionMap.cs` (CSHARP) | Magnitude: 823.94 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 435, state_mutation: 202, structural_boundaries: 104, branch: 95
- `src/VisualStudio/Xaml/Impl/Features/Diagnostics/XamlDiagnostic.cs` (CSHARP) | Magnitude: 50.44 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 30, api: 11, indent_spaces: 11, branch: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Compilers/Core/Portable/Emit/AnonymousDelegateWithIndexedNamePartialKey.cs` (CSHARP) | Magnitude: 12.56 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, func_start: 1, api: 1
- `eng/common/native/init-distro-rid.sh` (SHELL) | Magnitude: 212.64 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 81, indent_spaces: 60, branch: 33, reflection_metaprogramming: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Compilers/CSharp/Portable/Binder/Binder_Lookup.cs` (CSHARP) | Magnitude: 1538.48 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 680, state_mutation: 296, branch: 149, func_start: 130
- `src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedEnumValueFieldSymbol.cs` (CSHARP) | Magnitude: 20.68 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, api: 7, args: 5
- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/PropertySetAnalysisResult.cs` (CSHARP) | Magnitude: 18.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 6, generics: 6, immutability_locks: 6
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Helpers/RemoveUnnecessaryImports/AbstractUnnecessaryImportsProvider.cs` (CSHARP) | Magnitude: 66.78 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 18, generics: 12, args: 9
- `src/CodeStyle/Tools/Program.cs` (CSHARP) | Magnitude: 0.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 217, structural_boundaries: 54, branch: 53, func_start: 42

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Features/Core/Portable/EmbeddedLanguages/StackFrame/StackFrameCompilationUnit.cs` (CSHARP) | Magnitude: 37.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 17, indent_spaces: 14, structural_boundaries: 13, state_mutation: 12
- `eng/common/pipeline-logging-functions.ps1` (POWERSHELL) | Magnitude: 43.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 20, sec_high_risk_execution: 10, closures: 6
- `src/Workspaces/Core/Portable/CodeRefactorings/FixAllOccurences/RefactorAllScope.cs` (CSHARP) | Magnitude: 36.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 26, doc: 24, args: 19
- `src/Dependencies/Collections/Segmented/ImmutableSegmentedList`1+Builder.cs` (CSHARP) | Magnitude: 753.04 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 133, structural_boundaries: 72, state_mutation: 68, args: 65
- `eng/common/init-tools-native.ps1` (POWERSHELL) | Magnitude: 167.82 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 124, branch: 48, closures: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxTriviaListTests.cs` (CSHARP) | Magnitude: 141.74 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, func_start: 114, test: 99, sec_high_risk_execution: 96
- `src/Compilers/Core/Portable/PEWriter/Miscellaneous.cs` (CSHARP) | Magnitude: 66.8 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 138, doc: 113, structural_boundaries: 31, api: 18
- `src/Dependencies/Collections/Specialized/SpecializedCollections.Empty.List.cs` (CSHARP) | Magnitude: 35.66 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 9, api: 9, generics: 8
- `src/VisualStudio/Core/Def/Interop/ComAggregate.cs` (CSHARP) | Magnitude: 69.16 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, doc: 22, structural_boundaries: 21, func_start: 13
- `src/Workspaces/CoreTest/WorkspaceServiceTests/ReferenceCountedDisposableTests.cs` (CSHARP) | Magnitude: 81.94 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 130, func_start: 51, structural_boundaries: 43, test: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Features/Core/Portable/InvertIf/AbstractInvertIfCodeRefactoringProvider.cs` (CSHARP) | Magnitude: 567.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 175, func_start: 83, state_mutation: 61
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/SymbolKey/SymbolKey.MethodSymbolKey.cs` (CSHARP) | Magnitude: 349.44 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 62, branch: 46, structural_boundaries: 45
- `eng/common/vmr-sync.sh` (SHELL) | Magnitude: 300.08 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 83, branch: 74, structural_boundaries: 38
- `src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ContextQuery/SyntaxTreeExtensions.cs` (CSHARP) | Magnitude: 3527.0 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 838, branch: 219, structural_boundaries: 212, state_mutation: 112
- `src/Tools/Source/CompilerGeneratorTools/Source/IOperationGenerator/IOperationClassWriter.Verifier.cs` (CSHARP) | Magnitude: 0.5 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, branch: 55, state_mutation: 48, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Scripting/CoreTestUtilities/ScriptTaskExtensions.cs` (CSHARP) | Magnitude: 33.62 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, concurrency: 16, ui_framework: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/EditorFeatures/DiagnosticsTestUtilities/Diagnostics/AbstractUserDiagnosticTest.cs` (CSHARP) | Magnitude: 211.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 175, structural_boundaries: 95, concurrency: 50, func_start: 35
- `src/Features/CSharp/Portable/Completion/CSharpCompletionService.cs` (CSHARP) | Magnitude: 65.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 24, import: 11, concurrency: 9
- `src/Features/Core/Portable/SplitOrMergeIfStatements/Consecutive/AbstractSplitIntoConsecutiveIfStatementsCodeRefactoringProvider.cs` (CSHARP) | Magnitude: 69.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 31, func_start: 13, dead_code: 13
- `src/LanguageServer/Protocol/Handler/Diagnostics/DiagnosticSourceProviders/WorkspaceDocumentsAndProjectDiagnosticSourceProvider.cs` (CSHARP) | Magnitude: 104.9 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 36, concurrency: 21, doc: 18
- `src/LanguageServer/ProtocolUnitTests/Ordering/MutatingRequestHandler.cs` (CSHARP) | Magnitude: 28.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, concurrency: 14, structural_boundaries: 13, api: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/Workspaces/Core/Portable/Workspace/Host/SourceFiles/DynamicFileInfo.cs` (CSHARP) | Magnitude: 15.0 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 22, api: 6, indent_spaces: 5, dead_code: 3
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/SoftCrashException.cs` (CSHARP) | Magnitude: 18.66 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 20, api: 7, args: 6, func_start: 6
- `src/VisualStudio/Core/Def/Interop/WrapperPolicy.cs` (CSHARP) | Magnitude: 30.08 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, doc: 8, api: 4
- `src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/UnitTests/InternalImplementationOnlyTests.cs` (CSHARP) | Magnitude: 249.84 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 467, func_start: 228, planned_debt: 218, concurrency: 66
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/IReferenceCountedDisposable.cs` (CSHARP) | Magnitude: 34.96 | Delta: **0.156 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 28, structural_boundaries: 4, indent_spaces: 3, generics: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Features/Core/Portable/ChangeSignature/CallSiteKind.cs` (CSHARP) | Magnitude: 16.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 24, indent_spaces: 5, structural_boundaries: 2, class_start: 1
- `src/Workspaces/Core/Portable/CodeFixes/FixAllOccurrences/WellKnownFixAllProviders.cs` (CSHARP) | Magnitude: 15.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 4, api: 2, args: 1
- `src/RoslynAnalyzers/Utilities/Compiler/Options/ValueUsageInfo.cs` (CSHARP) | Magnitude: 37.22 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, indent_spaces: 24, state_mutation: 9, structural_boundaries: 8
- `src/Compilers/CSharp/Portable/Symbols/NullableFlowState.cs` (CSHARP) | Magnitude: 19.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 14, indent_spaces: 6, state_mutation: 3, structural_boundaries: 2
- `src/Compilers/Core/Portable/Compilation/Extensions.cs` (CSHARP) | Magnitude: 167.04 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 106, indent_spaces: 51, func_start: 24, structural_boundaries: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Compilers/CSharp/Portable/Binder/CatchClauseBinder.cs` (CSHARP) | Magnitude: 49.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 13, func_start: 10, import: 6
- `src/Compilers/CSharp/Portable/Binder/LocalScopeBinder.cs` (CSHARP) | Magnitude: 85.0 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 113, state_mutation: 24, structural_boundaries: 23, immutability_locks: 20
- `src/Compilers/CSharp/Portable/BoundTree/BoundBinaryOperator.UncommonData.cs` (CSHARP) | Magnitude: 238.96 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 71, branch: 29, structural_boundaries: 12, func_start: 12
- `src/Compilers/CSharp/Portable/Symbols/NamespaceSymbol.cs` (CSHARP) | Magnitude: 350.52 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, doc: 79, structural_boundaries: 55, api: 31
- `src/Compilers/Core/Portable/Syntax/SyntaxTriviaList.Enumerator.cs` (CSHARP) | Magnitude: 152.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 108, state_mutation: 27, structural_boundaries: 20, func_start: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/RoslynAnalyzers/Utilities/FlowAnalysis/Options/EditorConfigOptionNames_FlowAnalysis.cs` (CSHARP) | Magnitude: 24.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 47, indent_spaces: 13, api: 9, immutability_locks: 8
- `src/EditorFeatures/Core/Tagging/TaggerDelay.cs` (CSHARP) | Magnitude: 16.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 31, indent_spaces: 6, structural_boundaries: 2, dead_code: 2
- `src/Features/CSharp/Portable/Completion/KeywordRecommenders/UsingKeywordRecommender.cs` (CSHARP) | Magnitude: 30.14 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, dead_code: 11, func_start: 6
- `src/Features/CSharp/Portable/Completion/KeywordRecommenders/NamespaceKeywordRecommender.cs` (CSHARP) | Magnitude: 116.02 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 66, structural_boundaries: 23, branch: 18, dead_code: 10
- `src/Compilers/CSharp/Portable/Symbols/Synthesized/Records/SynthesizedRecordEqualityOperator.cs` (CSHARP) | Magnitude: 81.58 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, doc: 18, state_mutation: 10, branch: 9

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Features/Core/Portable/Diagnostics/IDiagnosticAnalyzerService.cs` -> Churn: **74.91%** | Cog Load: 20.1806% | Debt: 100.0%
- `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` -> Churn: **74.85%** | Cog Load: 41.3871% | Debt: 58.0744%
- `src/Compilers/CSharp/Portable/Errors/ErrorCode.cs` -> Churn: **73.84%** | Cog Load: 57.1805% | Debt: 0.0%
- `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs` -> Churn: **73.84%** | Cog Load: 56.5721% | Debt: 16.3932%
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/FileBasedPrograms/FileBasedProgramsProjectSystem.cs` -> Churn: **72.11%** | Cog Load: 67.0583% | Debt: 63.3134%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` -> **AlekseyTs** (100.0% isolated ownership) | Magnitude: 15857.26
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/SyntaxFacts/ISyntaxFacts.cs` -> **Cyrus Najmabadi** (100.0% isolated ownership) | Magnitude: 14024.38
- `src/Features/CSharpTest/ExtractMethod/ExtractMethodCodeRefactoringTests.cs` -> **Copilot** (100.0% isolated ownership) | Magnitude: 9079.56
- `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` -> **Fred Silberberg** (100.0% isolated ownership) | Magnitude: 9034.74
- `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` -> **Julien Couvreur** (100.0% isolated ownership) | Magnitude: 6552.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 14453.4** (Blast Radius: 144.534 * Doc Risk: 100.0%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs` -> **Severity: 2266.312** (Blast Radius: 23.069 * Doc Risk: 98.2406%)
- `src/Compilers/CSharp/Portable/BoundTree/Formatting.cs` -> **Severity: 1449.807** (Blast Radius: 14.513 * Doc Risk: 99.8971%)
- `src/Compilers/Core/Portable/MetadataReference/Metadata.cs` -> **Severity: 917.353** (Blast Radius: 9.182 * Doc Risk: 99.9077%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Completion.cs` -> **Severity: 615.2** (Blast Radius: 6.152 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
