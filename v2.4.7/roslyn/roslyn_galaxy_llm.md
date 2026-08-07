# ARCHITECTURAL_BRIEF: roslyn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/roslyn` |
| **Timestamp** | `2026-08-07T05:31:27.069391+00:00` |
| **Scan Duration** | `103.53s` |
| **Git Branch** | `main` |
| **Git Commit** | `849bed61024b171e673b9a1fac565b30e3ae1934` |
| **Git Remote** | `https://github.com/dotnet/roslyn` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 14021 malicious artifacts.

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
> **Architectural Drift Z-Score:** `4.924`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 6627 | 45.9% |
| file_cluster_13 | 5308 | 36.8% |
| file_cluster_16 | 921 | 6.4% |
| file_cluster_0 | 618 | 4.3% |
| file_cluster_4 | 433 | 3.0% |
| file_cluster_7 | 105 | 0.7% |
| file_cluster_17 | 27 | 0.2% |
| file_cluster_11 | 21 | 0.1% |
| file_cluster_15 | 20 | 0.1% |
| file_cluster_1 | 15 | 0.1% |
| file_cluster_9 | 13 | 0.1% |
| file_cluster_6 | 4 | 0.0% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 19.3 | 9.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 35.6 | 45.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 53.5 | 67.5 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 12.8 | 2.3 | 0.0 |
| API Exposure | 0.0 | 20.0 | 5.5 | 4.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 23.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 35.9 | 10.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 1.8 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 18.7 | 2.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 40.1 | 28.7 | 0.0 |
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

- `IsBuildOnlyDiagnostic` (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **2267.5** | LOC: 917
  * *Intent:* // Note: when adding a warning here, consider whether it should be registered as a nullability warning too
- `parseSwitchHeader` (@ `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`) -> Impact: **914.2** | LOC: 1186
- `ParseSwitchStatement` (@ `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`) -> Impact: **902.9** | LOC: 1288
- `Parse` (@ `src/Compilers/CSharp/Portable/CommandLine/CSharpCommandLineParser.cs`) -> Impact: **898.9** | LOC: 983
  * *Intent:* /// <summary> /// Parses a command line. /// </summary> /// <param name="args">A collection of strings representing the command line arguments.</param...
- `VisitConversion` (@ `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`) -> Impact: **885.1** | LOC: 618
- `MemberGroupFinalValidationAccessibilityC` (@ `src/Compilers/CSharp/Portable/Binder/Binder_Conversions.cs`) -> Impact: **867.4** | LOC: 839
- `GetWarningLevel` (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **866.7** | LOC: 384
- `IsWarning` (@ `src/Compilers/CSharp/Portable/Generated/ErrorFacts.Generated.cs`) -> Impact: **862.6** | LOC: 351
- `Trait` (@ `src/Features/CSharpTest/InvertIf/InvertIfTests.cs`) -> Impact: **801.3** | LOC: 1649
- `visitArgumentsCore` (@ `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`) -> Impact: **799.1** | LOC: 1165

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/Compilers/CSharp/Test/Semantic/Semantics` | 106 | 107519.44 | 17.38% | 0.0% |
| `src/Compilers/CSharp/Test/Emit/CodeGen` | 72 | 86489.16 | 20.71% | 0.0% |
| `src/Compilers/CSharp/Test/Emit3/Semantics` | 21 | 43615.64 | 18.03% | 0.0% |
| `src/EditorFeatures/CSharpTest2/Recommendations` | 150 | 37078.42 | 29.46% | 98.66% |
| `src/Compilers/CSharp/Test/Syntax/Parsing` | 69 | 36696.38 | 5.9% | 0.0% |
| `src/Compilers/CSharp/Portable/Binder` | 117 | 35454.12 | 28.44% | 62.79% |
| `src/Compilers/CSharp/Test/IOperation/IOperation` | 84 | 33586.2 | 8.87% | 0.0% |
| `src/Compilers/CSharp/Test/Symbol/Symbols` | 49 | 27800.58 | 9.78% | 0.0% |
| `src/Compilers/CSharp/Portable/Symbols/Source` | 71 | 21089.24 | 29.48% | 66.47% |
| `src/Compilers/CSharp/Portable/Parser` | 23 | 19514.06 | 27.95% | 55.44% |

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
- `src/Features/CSharpTest/EditAndContinue/TopLevelEditingTests.cs` -> **474** Orphaned Functions | **148** Duplicates
- `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` -> **371** Orphaned Functions | **172** Duplicates
- `src/Compilers/CSharp/Test/Symbol/Symbols/SymbolErrorTests.cs` -> **301** Orphaned Functions | **242** Duplicates
- `src/Features/CSharpTest/EditAndContinue/StatementEditingTests.cs` -> **428** Orphaned Functions | **79** Duplicates
- `src/Compilers/Test/Resources/Core/SymbolsTests/BigVisitor.cs` -> **0** Orphaned Functions | **500** Duplicates

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
9. **`src/Compilers/CSharp/Portable/Binder/ExpressionVariableFinder.cs`** -> AI Confidence: **99.39%**
10. **`src/Compilers/CSharp/Portable/Symbols/VarianceSafety.cs`** -> AI Confidence: **99.39%**
11. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowTests.cs`** -> AI Confidence: **99.39%**
12. **`src/Compilers/CSharp/Test/Syntax/Diagnostics/DiagnosticTest.cs`** -> AI Confidence: **99.39%**
13. **`src/Compilers/Core/Portable/Hashing/XxHashShared.cs`** -> AI Confidence: **99.39%**
14. **`src/Features/CSharp/Portable/Debugging/CSharpProximityExpressionsService.Worker.cs`** -> AI Confidence: **99.39%**
15. **`src/LanguageServer/Protocol/Handler/Completion/CompletionCapabilityHelper.cs`** -> AI Confidence: **99.39%**
16. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService_Prototype.cs`** -> AI Confidence: **99.39%**
17. **`src/Compilers/Core/Portable/Symbols/Attributes/MarshalAsAttributeDecoder.cs`** -> AI Confidence: **99.34%**
18. **`src/Compilers/CSharp/Portable/Errors/MessageID.cs`** -> AI Confidence: **99.32%**
19. **`src/Compilers/CSharp/Test/Syntax/Parsing/ForStatementParsingTest.cs`** -> AI Confidence: **99.32%**
20. **`src/Compilers/Core/Portable/Operations/ControlFlowRegion.cs`** -> AI Confidence: **99.32%**
21. **`eng/common/SetupNugetSources.sh`** -> AI Confidence: **99.31%**
22. **`eng/common/cross/install-debs.py`** -> AI Confidence: **99.31%**
23. **`src/Analyzers/CSharp/Analyzers/UseNameofInNullableAttribute/CSharpUseNameofInNullableAttributeDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
24. **`src/Analyzers/CSharp/Analyzers/UsePatternMatching/CSharpAsAndNullCheckDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
25. **`src/Analyzers/CSharp/Tests/FileHeaders/FileHeaderTests.cs`** -> AI Confidence: **99.31%**
26. **`src/Analyzers/CSharp/Tests/PopulateSwitch/PopulateSwitchStatementTests.cs`** -> AI Confidence: **99.31%**
27. **`src/Analyzers/CSharp/Tests/UsePatternMatching/CSharpAsAndMemberAccessTests.cs`** -> AI Confidence: **99.31%**
28. **`src/Analyzers/Core/Analyzers/UseConditionalExpression/ForAssignment/UseConditionalExpressionForAssignmentHelpers.cs`** -> AI Confidence: **99.31%**
29. **`src/CodeStyle/Tools/Program.cs`** -> AI Confidence: **99.31%**
30. **`src/Compilers/CSharp/CSharpAnalyzerDriver/CSharpDeclarationComputer.cs`** -> AI Confidence: **99.31%**
31. **`src/Compilers/CSharp/Portable/Binder/Binder.CapturedParametersFinder.cs`** -> AI Confidence: **99.31%**
32. **`src/Compilers/CSharp/Portable/Binder/Binder.IdentifierUsedAsValueFinder.cs`** -> AI Confidence: **99.31%**
33. **`src/Compilers/CSharp/Portable/Binder/Binder.ValueChecks.cs`** -> AI Confidence: **99.31%**
34. **`src/Compilers/CSharp/Portable/Binder/BinderFactory.BinderFactoryVisitor.cs`** -> AI Confidence: **99.31%**
35. **`src/Compilers/CSharp/Portable/Binder/Binder_AnonymousTypes.cs`** -> AI Confidence: **99.31%**
36. **`src/Compilers/CSharp/Portable/Binder/Binder_Attributes.cs`** -> AI Confidence: **99.31%**
37. **`src/Compilers/CSharp/Portable/Binder/Binder_Await.cs`** -> AI Confidence: **99.31%**
38. **`src/Compilers/CSharp/Portable/Binder/Binder_Constraints.cs`** -> AI Confidence: **99.31%**
39. **`src/Compilers/CSharp/Portable/Binder/Binder_Conversions.cs`** -> AI Confidence: **99.31%**
40. **`src/Compilers/CSharp/Portable/Binder/Binder_Crefs.cs`** -> AI Confidence: **99.31%**
41. **`src/Compilers/CSharp/Portable/Binder/Binder_Deconstruct.cs`** -> AI Confidence: **99.31%**
42. **`src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs`** -> AI Confidence: **99.31%**
43. **`src/Compilers/CSharp/Portable/Binder/Binder_InterpolatedString.cs`** -> AI Confidence: **99.31%**
44. **`src/Compilers/CSharp/Portable/Binder/Binder_Invocation.cs`** -> AI Confidence: **99.31%**
45. **`src/Compilers/CSharp/Portable/Binder/Binder_Lambda.cs`** -> AI Confidence: **99.31%**
46. **`src/Compilers/CSharp/Portable/Binder/Binder_Lookup.cs`** -> AI Confidence: **99.31%**
47. **`src/Compilers/CSharp/Portable/Binder/Binder_Operators.cs`** -> AI Confidence: **99.31%**
48. **`src/Compilers/CSharp/Portable/Binder/Binder_Patterns.cs`** -> AI Confidence: **99.31%**
49. **`src/Compilers/CSharp/Portable/Binder/Binder_Query.cs`** -> AI Confidence: **99.31%**
50. **`src/Compilers/CSharp/Portable/Binder/Binder_QueryErrors.cs`** -> AI Confidence: **99.31%**
51. **`src/Compilers/CSharp/Portable/Binder/Binder_Statements.cs`** -> AI Confidence: **99.31%**
52. **`src/Compilers/CSharp/Portable/Binder/Binder_TupleOperators.cs`** -> AI Confidence: **99.31%**
53. **`src/Compilers/CSharp/Portable/Binder/DecisionDagBuilder.cs`** -> AI Confidence: **99.31%**
54. **`src/Compilers/CSharp/Portable/Binder/DecisionDagBuilder_CheckOrReachability.cs`** -> AI Confidence: **99.31%**
55. **`src/Compilers/CSharp/Portable/Binder/ExecutableCodeBinder.cs`** -> AI Confidence: **99.31%**
56. **`src/Compilers/CSharp/Portable/Binder/ForEachLoopBinder.cs`** -> AI Confidence: **99.31%**
57. **`src/Compilers/CSharp/Portable/Binder/InMethodBinder.cs`** -> AI Confidence: **99.31%**
58. **`src/Compilers/CSharp/Portable/Binder/LocalBinderFactory.cs`** -> AI Confidence: **99.31%**
59. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/ConversionsBase.cs`** -> AI Confidence: **99.31%**
60. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedConversions.cs`** -> AI Confidence: **99.31%**
61. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedExplicitConversions.cs`** -> AI Confidence: **99.31%**
62. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/UserDefinedImplicitConversions.cs`** -> AI Confidence: **99.31%**
63. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/BinaryOperatorOverloadResolution.cs`** -> AI Confidence: **99.31%**
64. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/OperatorKindExtensions.cs`** -> AI Confidence: **99.31%**
65. **`src/Compilers/CSharp/Portable/Binder/Semantics/Operators/UnaryOperatorOverloadResolution.cs`** -> AI Confidence: **99.31%**
66. **`src/Compilers/CSharp/Portable/Binder/Semantics/OverloadResolution/OverloadResolution.cs`** -> AI Confidence: **99.31%**
67. **`src/Compilers/CSharp/Portable/Binder/Semantics/OverloadResolution/OverloadResolutionResult.cs`** -> AI Confidence: **99.31%**
68. **`src/Compilers/CSharp/Portable/Binder/SwitchBinder.cs`** -> AI Confidence: **99.31%**
69. **`src/Compilers/CSharp/Portable/Binder/UsingStatementBinder.cs`** -> AI Confidence: **99.31%**
70. **`src/Compilers/CSharp/Portable/BoundTree/BoundTreeVisitors.cs`** -> AI Confidence: **99.31%**
71. **`src/Compilers/CSharp/Portable/BoundTree/VariablePendingInference.cs`** -> AI Confidence: **99.31%**
72. **`src/Compilers/CSharp/Portable/CodeGen/CodeGenerator.cs`** -> AI Confidence: **99.31%**
73. **`src/Compilers/CSharp/Portable/CodeGen/EmitAddress.cs`** -> AI Confidence: **99.31%**
74. **`src/Compilers/CSharp/Portable/CodeGen/EmitStatement.cs`** -> AI Confidence: **99.31%**
75. **`src/Compilers/CSharp/Portable/Compilation/BuiltInOperators.cs`** -> AI Confidence: **99.31%**
76. **`src/Compilers/CSharp/Portable/Compilation/CSharpDiagnosticFilter.cs`** -> AI Confidence: **99.31%**
77. **`src/Compilers/CSharp/Portable/Compilation/CSharpSemanticModel.cs`** -> AI Confidence: **99.31%**
78. **`src/Compilers/CSharp/Portable/Compilation/MemberSemanticModel.NodeMapBuilder.cs`** -> AI Confidence: **99.31%**
79. **`src/Compilers/CSharp/Portable/Compilation/MemberSemanticModel.cs`** -> AI Confidence: **99.31%**
80. **`src/Compilers/CSharp/Portable/Compilation/SyntaxTreeSemanticModel.cs`** -> AI Confidence: **99.31%**
81. **`src/Compilers/CSharp/Portable/Compiler/ClsComplianceChecker.cs`** -> AI Confidence: **99.31%**
82. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.cs`** -> AI Confidence: **99.31%**
83. **`src/Compilers/CSharp/Portable/Declarations/DeclarationTreeBuilder.cs`** -> AI Confidence: **99.31%**
84. **`src/Compilers/CSharp/Portable/DocumentationComments/DocumentationCommentIDVisitor.PartVisitor.cs`** -> AI Confidence: **99.31%**
85. **`src/Compilers/CSharp/Portable/FlowAnalysis/AbstractFlowPass.cs`** -> AI Confidence: **99.31%**
86. **`src/Compilers/CSharp/Portable/FlowAnalysis/DefiniteAssignment.cs`** -> AI Confidence: **99.31%**
87. **`src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`** -> AI Confidence: **99.31%**
88. **`src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker_Patterns.cs`** -> AI Confidence: **99.31%**
89. **`src/Compilers/CSharp/Portable/FlowAnalysis/VariablesDeclaredWalker.cs`** -> AI Confidence: **99.31%**
90. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ClosureConversion.cs`** -> AI Confidence: **99.31%**
91. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ExpressionLambdaRewriter.cs`** -> AI Confidence: **99.31%**
92. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/SynthesizedClosureMethod.cs`** -> AI Confidence: **99.31%**
93. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/CodeCoverageInstrumenter.cs`** -> AI Confidence: **99.31%**
94. **`src/Compilers/CSharp/Portable/Lowering/Instrumentation/ModuleCancellationInstrumenter.cs`** -> AI Confidence: **99.31%**
95. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.DecisionDagRewriter.cs`** -> AI Confidence: **99.31%**
96. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Call.cs`** -> AI Confidence: **99.31%**
97. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_CompoundAssignmentOperator.cs`** -> AI Confidence: **99.31%**
98. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Conversion.cs`** -> AI Confidence: **99.31%**
99. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Event.cs`** -> AI Confidence: **99.31%**
100. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_FixedStatement.cs`** -> AI Confidence: **99.31%**
101. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_IndexerAccess.cs`** -> AI Confidence: **99.31%**
102. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Literal.cs`** -> AI Confidence: **99.31%**
103. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_Range.cs`** -> AI Confidence: **99.31%**
104. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_StringConcat.cs`** -> AI Confidence: **99.31%**
105. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_UsingStatement.cs`** -> AI Confidence: **99.31%**
106. **`src/Compilers/CSharp/Portable/Operations/CSharpOperationFactory.cs`** -> AI Confidence: **99.31%**
107. **`src/Compilers/CSharp/Portable/Operations/CSharpOperationFactory_Methods.cs`** -> AI Confidence: **99.31%**
108. **`src/Compilers/CSharp/Portable/Parser/Directives.cs`** -> AI Confidence: **99.31%**
109. **`src/Compilers/CSharp/Portable/Parser/LanguageParser.cs`** -> AI Confidence: **99.31%**
110. **`src/Compilers/CSharp/Portable/Parser/SyntaxParser.cs`** -> AI Confidence: **99.31%**
111. **`src/Compilers/CSharp/Portable/SymbolDisplay/SymbolDisplayVisitor.cs`** -> AI Confidence: **99.31%**
112. **`src/Compilers/CSharp/Portable/SymbolDisplay/SymbolDisplayVisitor_Minimal.cs`** -> AI Confidence: **99.31%**
113. **`src/Compilers/CSharp/Portable/Symbols/Attributes/AttributeData.cs`** -> AI Confidence: **99.31%**
114. **`src/Compilers/CSharp/Portable/Symbols/Compilation_UsedAssemblies.cs`** -> AI Confidence: **99.31%**
115. **`src/Compilers/CSharp/Portable/Symbols/Compilation_WellKnownMembers.cs`** -> AI Confidence: **99.31%**
116. **`src/Compilers/CSharp/Portable/Symbols/ConstraintsHelper.cs`** -> AI Confidence: **99.31%**
117. **`src/Compilers/CSharp/Portable/Symbols/MemberSymbolExtensions.cs`** -> AI Confidence: **99.31%**
118. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/MetadataDecoder.cs`** -> AI Confidence: **99.31%**
119. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEMethodSymbol.cs`** -> AI Confidence: **99.31%**
120. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PETypeParameterSymbol.cs`** -> AI Confidence: **99.31%**
121. **`src/Compilers/CSharp/Portable/Symbols/OverriddenOrHiddenMembersHelpers.cs`** -> AI Confidence: **99.31%**
122. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingSymbolTranslator.cs`** -> AI Confidence: **99.31%**
123. **`src/Compilers/CSharp/Portable/Symbols/Source/AttributeLocation.cs`** -> AI Confidence: **99.31%**
124. **`src/Compilers/CSharp/Portable/Symbols/Source/ExplicitInterfaceHelpers.cs`** -> AI Confidence: **99.31%**
125. **`src/Compilers/CSharp/Portable/Symbols/Source/ParameterHelpers.cs`** -> AI Confidence: **99.31%**
126. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceAssemblySymbol.cs`** -> AI Confidence: **99.31%**
127. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceComplexParameterSymbol.cs`** -> AI Confidence: **99.31%**
128. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceConstructorSymbol.cs`** -> AI Confidence: **99.31%**
129. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceEventSymbol.cs`** -> AI Confidence: **99.31%**
130. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceLocalSymbol.cs`** -> AI Confidence: **99.31%**
131. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberContainerSymbol.cs`** -> AI Confidence: **99.31%**
132. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberContainerSymbol_ImplementationChecks.cs`** -> AI Confidence: **99.31%**
133. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberFieldSymbol.cs`** -> AI Confidence: **99.31%**
134. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMemberMethodSymbol.cs`** -> AI Confidence: **99.31%**
135. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceMethodSymbolWithAttributes.cs`** -> AI Confidence: **99.31%**
136. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceModuleSymbol.cs`** -> AI Confidence: **99.31%**
137. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol.cs`** -> AI Confidence: **99.31%**
138. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol_Bases.cs`** -> AI Confidence: **99.31%**
139. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamedTypeSymbol_Extension.cs`** -> AI Confidence: **99.31%**
140. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamespaceSymbol.AliasesAndUsings.cs`** -> AI Confidence: **99.31%**
141. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceNamespaceSymbol.cs`** -> AI Confidence: **99.31%**
142. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodOrUserDefinedOperatorSymbol.cs`** -> AI Confidence: **99.31%**
143. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodSymbol.cs`** -> AI Confidence: **99.31%**
144. **`src/Compilers/CSharp/Portable/Symbols/Source/SourcePropertySymbol.cs`** -> AI Confidence: **99.31%**
145. **`src/Compilers/CSharp/Portable/Symbols/Source/SourcePropertySymbolBase.cs`** -> AI Confidence: **99.31%**
146. **`src/Compilers/CSharp/Portable/Symbols/Source/TypeParameterConstraintClause.cs`** -> AI Confidence: **99.31%**
147. **`src/Compilers/CSharp/Portable/Symbols/Symbol_Attributes.cs`** -> AI Confidence: **99.31%**
148. **`src/Compilers/CSharp/Portable/Symbols/Tuples/TupleTypeSymbol.cs`** -> AI Confidence: **99.31%**
149. **`src/Compilers/CSharp/Portable/Symbols/TypeSymbol.cs`** -> AI Confidence: **99.31%**
150. **`src/Compilers/CSharp/Portable/Syntax/DirectiveTriviaSyntax.cs`** -> AI Confidence: **99.31%**
151. **`src/Compilers/CSharp/Portable/Syntax/LambdaUtilities.cs`** -> AI Confidence: **99.31%**
152. **`src/Compilers/CSharp/Portable/Syntax/SyntaxExtensions.cs`** -> AI Confidence: **99.31%**
153. **`src/Compilers/CSharp/Portable/Syntax/SyntaxFacts.cs`** -> AI Confidence: **99.31%**
154. **`src/Compilers/CSharp/Portable/Syntax/SyntaxNodeRemover.cs`** -> AI Confidence: **99.31%**
155. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTryFinally.cs`** -> AI Confidence: **99.31%**
156. **`src/Compilers/CSharp/Test/Emit/CodeGen/GotoTest.cs`** -> AI Confidence: **99.31%**
157. **`src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs`** -> AI Confidence: **99.31%**
158. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternSwitchTests.cs`** -> AI Confidence: **99.31%**
159. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_InvalidStatement.cs`** -> AI Confidence: **99.31%**
160. **`src/Compilers/CSharp/Test/Semantic/Semantics/StackAllocInitializerTests.cs`** -> AI Confidence: **99.31%**
161. **`src/Compilers/CSharp/Test/Semantic/Semantics/SwitchTests.cs`** -> AI Confidence: **99.31%**
162. **`src/Compilers/CSharp/Test/Semantic/Semantics/TargetTypedDefaultTests.cs`** -> AI Confidence: **99.31%**
163. **`src/Compilers/CSharp/Test/Semantic/Semantics/UserDefinedConversionTests.cs`** -> AI Confidence: **99.31%**
164. **`src/Compilers/CSharp/Test/Syntax/Parsing/CrefParsingTests.cs`** -> AI Confidence: **99.31%**
165. **`src/Compilers/CSharp/Test/Syntax/Parsing/NullConditionalAssignmentParsingTests.cs`** -> AI Confidence: **99.31%**
166. **`src/Compilers/CSharp/Test/Syntax/Parsing/ParsingTests.cs`** -> AI Confidence: **99.31%**
167. **`src/Compilers/CSharp/Test/Syntax/Parsing/PatternParsingTests.cs`** -> AI Confidence: **99.31%**
168. **`src/Compilers/CSharp/Test/Syntax/Parsing/StatementParsingTests.cs`** -> AI Confidence: **99.31%**
169. **`src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxTests.cs`** -> AI Confidence: **99.31%**
170. **`src/Compilers/CSharp/Test/WinRT/Metadata/WinMdDumpTest.cs`** -> AI Confidence: **99.31%**
171. **`src/Compilers/Core/CodeAnalysisTest/Collections/ImmutablesTestBase.cs`** -> AI Confidence: **99.31%**
172. **`src/Compilers/Core/CodeAnalysisTest/Collections/List/IEnumerable.Generic.Tests.cs`** -> AI Confidence: **99.31%**
173. **`src/Compilers/Core/CodeAnalysisTest/DiagnosticBagTests.cs`** -> AI Confidence: **99.31%**
174. **`src/Compilers/Core/CodeAnalysisTest/MetadataReferences/MetadataHelpersTests.cs`** -> AI Confidence: **99.31%**
175. **`src/Compilers/Core/MSBuildTask/CommandLineBuilderExtension.cs`** -> AI Confidence: **99.31%**
176. **`src/Compilers/Core/MSBuildTask/GenerateMSBuildEditorConfig.cs`** -> AI Confidence: **99.31%**
177. **`src/Compilers/Core/MSBuildTask/Vbc.cs`** -> AI Confidence: **99.31%**
178. **`src/Compilers/Core/MSBuildTaskTests/TestUtilities/IntegrationTestBase.cs`** -> AI Confidence: **99.31%**
179. **`src/Compilers/Core/Portable/Binding/UseSiteInfo.cs`** -> AI Confidence: **99.31%**
180. **`src/Compilers/Core/Portable/CodeGen/BasicBlock.cs`** -> AI Confidence: **99.31%**
181. **`src/Compilers/Core/Portable/CodeGen/ILBuilder.cs`** -> AI Confidence: **99.31%**
182. **`src/Compilers/Core/Portable/CodeGen/SwitchIntegralJumpTableEmitter.cs`** -> AI Confidence: **99.31%**
183. **`src/Compilers/Core/Portable/CommandLine/AnalyzerConfig.SectionNameMatching.cs`** -> AI Confidence: **99.31%**
184. **`src/Compilers/Core/Portable/CommandLine/CommandLineParser.cs`** -> AI Confidence: **99.31%**
185. **`src/Compilers/Core/Portable/CommandLine/SarifV1ErrorLogger.cs`** -> AI Confidence: **99.31%**
186. **`src/Compilers/Core/Portable/CommandLine/SarifV2ErrorLogger.cs`** -> AI Confidence: **99.31%**
187. **`src/Compilers/Core/Portable/Compilation/Compilation.cs`** -> AI Confidence: **99.31%**
188. **`src/Compilers/Core/Portable/Compilation/DeterministicKeyBuilder.cs`** -> AI Confidence: **99.31%**
189. **`src/Compilers/Core/Portable/DiaSymReader/Writer/SymUnmanagedWriterImpl.cs`** -> AI Confidence: **99.31%**
190. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalysisResultBuilder.cs`** -> AI Confidence: **99.31%**
191. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/DiagnosticAnalysisContextHelpers.cs`** -> AI Confidence: **99.31%**
192. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/SuppressMessageAttributeState.TargetSymbolResolver.cs`** -> AI Confidence: **99.31%**
193. **`src/Compilers/Core/Portable/Emit/EditAndContinue/SymbolChanges.cs`** -> AI Confidence: **99.31%**
194. **`src/Compilers/Core/Portable/Emit/EditAndContinueMethodDebugInformation.cs`** -> AI Confidence: **99.31%**
195. **`src/Compilers/Core/Portable/Emit/SemanticEdit.cs`** -> AI Confidence: **99.31%**
196. **`src/Compilers/Core/Portable/Hashing/XxHash128.cs`** -> AI Confidence: **99.31%**
197. **`src/Compilers/Core/Portable/InternalUtilities/JsonWriter.cs`** -> AI Confidence: **99.31%**
198. **`src/Compilers/Core/Portable/MetadataReader/MetadataDecoder.cs`** -> AI Confidence: **99.31%**
199. **`src/Compilers/Core/Portable/MetadataReader/MetadataHelpers.cs`** -> AI Confidence: **99.31%**
200. **`src/Compilers/Core/Portable/MetadataReader/PEModule.cs`** -> AI Confidence: **99.31%**
201. **`src/Compilers/Core/Portable/MetadataReference/AssemblyIdentity.DisplayName.cs`** -> AI Confidence: **99.31%**
202. **`src/Compilers/Core/Portable/NativePdbWriter/PdbWriter.cs`** -> AI Confidence: **99.31%**
203. **`src/Compilers/Core/Portable/Operations/ControlFlowGraph.cs`** -> AI Confidence: **99.31%**
204. **`src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.cs`** -> AI Confidence: **99.31%**
205. **`src/Compilers/Core/Portable/Operations/OperationExtensions.cs`** -> AI Confidence: **99.31%**
206. **`src/Compilers/Core/Portable/PEWriter/MetadataVisitor.cs`** -> AI Confidence: **99.31%**
207. **`src/Compilers/Core/Portable/PEWriter/MetadataWriter.cs`** -> AI Confidence: **99.31%**
208. **`src/Compilers/Core/Portable/PEWriter/NativeResourceWriter.cs`** -> AI Confidence: **99.31%**
209. **`src/Compilers/Core/Portable/PEWriter/TypeNameSerializer.cs`** -> AI Confidence: **99.31%**
210. **`src/Compilers/Core/Portable/ReferenceManager/CommonReferenceManager.Resolution.cs`** -> AI Confidence: **99.31%**
211. **`src/Compilers/Core/Portable/Symbols/Attributes/CommonAttributeData.cs`** -> AI Confidence: **99.31%**
212. **`src/Compilers/Core/Portable/Syntax/SyntaxDiffer.cs`** -> AI Confidence: **99.31%**
213. **`src/Compilers/Core/Portable/Syntax/SyntaxToken.cs`** -> AI Confidence: **99.31%**
214. **`src/Compilers/Core/Portable/Syntax/SyntaxTrivia.cs`** -> AI Confidence: **99.31%**
215. **`src/Compilers/Core/Portable/Text/LargeText.cs`** -> AI Confidence: **99.31%**
216. **`src/Compilers/Server/VBCSCompiler/BuildProtocolUtil.cs`** -> AI Confidence: **99.31%**
217. **`src/Compilers/Server/VBCSCompiler/ServerDispatcher.cs`** -> AI Confidence: **99.31%**
218. **`src/Compilers/Test/Core/Compilation/OperationTreeVerifier.cs`** -> AI Confidence: **99.31%**
219. **`src/Compilers/Test/Core/Compilation/TestOperationVisitor.cs`** -> AI Confidence: **99.31%**
220. **`src/Compilers/Test/Core/Diagnostics/OperationTestAnalyzer.cs`** -> AI Confidence: **99.31%**
221. **`src/Compilers/Test/Core/Metadata/ILBuilderVisualizer.cs`** -> AI Confidence: **99.31%**
222. **`src/Compilers/Test/Core/Platform/Custom/MetadataSignatureHelper.cs`** -> AI Confidence: **99.31%**
223. **`src/Compilers/Test/Core/Platform/Custom/SigningTestHelpers.cs`** -> AI Confidence: **99.31%**
224. **`src/Compilers/Test/Utilities/CSharp/CompilationTestUtils.cs`** -> AI Confidence: **99.31%**
225. **`src/Compilers/Test/Utilities/CSharp/CompilingTestBase.cs`** -> AI Confidence: **99.31%**
226. **`src/Compilers/Test/Utilities/CSharp/FunctionPointerUtilities.cs`** -> AI Confidence: **99.31%**
227. **`src/Dependencies/Collections/Segmented/SegmentedDictionary`2.cs`** -> AI Confidence: **99.31%**
228. **`src/Dependencies/Collections/Segmented/SegmentedHashSet`1.cs`** -> AI Confidence: **99.31%**
229. **`src/Dependencies/Collections/Segmented/SegmentedList`1.cs`** -> AI Confidence: **99.31%**
230. **`src/Dependencies/Collections/TemporaryArray`1.cs`** -> AI Confidence: **99.31%**
231. **`src/EditorFeatures/CSharp/CompleteStatement/CompleteStatementCommandHandler.cs`** -> AI Confidence: **99.31%**
232. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PDB/MethodDebugInfo.Native.cs`** -> AI Confidence: **99.31%**
233. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PDB/MethodDebugInfo.Portable.cs`** -> AI Confidence: **99.31%**
234. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Formatter.Values.cs`** -> AI Confidence: **99.31%**
235. **`src/Features/CSharp/Portable/BraceCompletion/CurlyBraceCompletionService.cs`** -> AI Confidence: **99.31%**
236. **`src/Features/CSharp/Portable/Completion/CompletionProviders/OverrideCompletionProvider.cs`** -> AI Confidence: **99.31%**
237. **`src/Features/CSharp/Portable/Completion/Providers/ContextVariableArgumentProvider.cs`** -> AI Confidence: **99.31%**
238. **`src/Features/CSharp/Portable/Diagnostics/Analyzers/TypeSyntaxSimplifierWalker.cs`** -> AI Confidence: **99.31%**
239. **`src/Features/CSharp/Portable/EditAndContinue/CSharpEditAndContinueAnalyzer.cs`** -> AI Confidence: **99.31%**
240. **`src/Features/CSharp/Portable/EditAndContinue/SyntaxComparer.cs`** -> AI Confidence: **99.31%**
241. **`src/Features/CSharp/Portable/GoToDefinition/CSharpGoToDefinitionSymbolService.cs`** -> AI Confidence: **99.31%**
242. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/LoopHighlighter.cs`** -> AI Confidence: **99.31%**
243. **`src/Features/CSharpTest/ConvertIfToSwitch/ConvertIfToSwitchTests.cs`** -> AI Confidence: **99.31%**
244. **`src/Features/CSharpTest/InvertIf/InvertIfTests.cs`** -> AI Confidence: **99.31%**
245. **`src/Features/CSharpTest/UseRecursivePatterns/UseRecursivePatternsRefactoringTests.cs`** -> AI Confidence: **99.31%**
246. **`src/Features/Core/Portable/Completion/CompletionItem.cs`** -> AI Confidence: **99.31%**
247. **`src/Features/Core/Portable/DocumentationComments/AbstractDocumentationCommentFormattingService.cs`** -> AI Confidence: **99.31%**
248. **`src/Features/Core/Portable/EmbeddedLanguages/Json/LanguageServices/JsonClassifier.cs`** -> AI Confidence: **99.31%**
249. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/RegexParser.CaptureInfoAnalyzer.cs`** -> AI Confidence: **99.31%**
250. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.State.cs`** -> AI Confidence: **99.31%**
251. **`src/Features/Core/Portable/PdbSourceDocument/PdbFileLocatorService.cs`** -> AI Confidence: **99.31%**
252. **`src/Features/Core/Portable/Shared/Extensions/ISymbolExtensions_2.cs`** -> AI Confidence: **99.31%**
253. **`src/Features/Core/Portable/SolutionExplorer/ISolutionExplorerSymbolTreeItemProvider.cs`** -> AI Confidence: **99.31%**
254. **`src/Features/Core/Portable/SpellCheck/AbstractSpellCheckSpanService.cs`** -> AI Confidence: **99.31%**
255. **`src/Features/DiagnosticsTestUtilities/CodeActions/CodeFixVerifierHelper.cs`** -> AI Confidence: **99.31%**
256. **`src/Interactive/Host/Interactive/Core/InteractiveHost.RemoteService.cs`** -> AI Confidence: **99.31%**
257. **`src/LanguageServer/Protocol/Handler/Definitions/AbstractGoToDefinitionHandler.cs`** -> AI Confidence: **99.31%**
258. **`src/LanguageServer/Protocol/Protocol/Converters/FormattingOptionsConverter.cs`** -> AI Confidence: **99.31%**
259. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticDescriptorCreationAnalyzer_IdRangeAndCategoryValidation.cs`** -> AI Confidence: **99.31%**
260. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/Fixers/AnalyzerReleaseTrackingFix.cs`** -> AI Confidence: **99.31%**
261. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/RegisterActionAnalyzer.cs`** -> AI Confidence: **99.31%**
262. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/ReleaseTrackingHelper.cs`** -> AI Confidence: **99.31%**
263. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/ReportDiagnosticAnalyzer.cs`** -> AI Confidence: **99.31%**
264. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.BannedApiAnalyzers/Core/SymbolIsBannedAnalyzerBase.cs`** -> AI Confidence: **99.31%**
265. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.ResxSourceGenerator/Microsoft.CodeAnalysis.ResxSourceGenerator/AbstractResxGenerator.cs`** -> AI Confidence: **99.31%**
266. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/TypeConversionAllocationAnalyzer.cs`** -> AI Confidence: **99.31%**
267. **`src/RoslynAnalyzers/Tools/GenerateDocumentationAndConfigFiles/CodeFixerExtensions.cs`** -> AI Confidence: **99.31%**
268. **`src/RoslynAnalyzers/Tools/Metrics/MetricsOutputWriter.cs`** -> AI Confidence: **99.31%**
269. **`src/RoslynAnalyzers/Tools/Metrics/Program.cs`** -> AI Confidence: **99.31%**
270. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/MetricsHelper.cs`** -> AI Confidence: **99.31%**
271. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/IOperationExtensions.cs`** -> AI Confidence: **99.31%**
272. **`src/RoslynAnalyzers/Utilities/Compiler/WellKnownTypeProvider.cs`** -> AI Confidence: **99.31%**
273. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/GlobalFlowStateAnalysis/GlobalFlowStateAnalysis.GlobalFlowStateAnalysisValueSetDomain.cs`** -> AI Confidence: **99.31%**
274. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataConfig.cs`** -> AI Confidence: **99.31%**
275. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataSymbolMap.cs`** -> AI Confidence: **99.31%**
276. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/TaintedDataSymbolMapExtensions.cs`** -> AI Confidence: **99.31%**
277. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/ValueContentAnalysis/ValueContentAbstractValue.cs`** -> AI Confidence: **99.31%**
278. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AnalysisEntityFactory.cs`** -> AI Confidence: **99.31%**
279. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowAnalysis.cs`** -> AI Confidence: **99.31%**
280. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/LValueFlowCapturesProvider.cs`** -> AI Confidence: **99.31%**
281. **`src/Scripting/Core/Hosting/AssemblyLoader/MetadataShadowCopyProvider.cs`** -> AI Confidence: **99.31%**
282. **`src/Scripting/Core/Hosting/ObjectFormatter/CommonObjectFormatter.Visitor.cs`** -> AI Confidence: **99.31%**
283. **`src/Scripting/Core/Hosting/ObjectFormatter/CommonTypeNameFormatter.cs`** -> AI Confidence: **99.31%**
284. **`src/Tools/Source/CompilerGeneratorTools/Source/IOperationGenerator/IOperationClassWriter.cs`** -> AI Confidence: **99.31%**
285. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService.CodeModelEventCollector.cs`** -> AI Confidence: **99.31%**
286. **`src/VisualStudio/CSharp/Impl/CodeModel/CSharpCodeModelService.cs`** -> AI Confidence: **99.31%**
287. **`src/VisualStudio/CSharp/Impl/ObjectBrowser/DescriptionBuilder.cs`** -> AI Confidence: **99.31%**
288. **`src/VisualStudio/Core/Def/LanguageService/AbstractLanguageService`2.IVsLanguageDebugInfo.cs`** -> AI Confidence: **99.31%**
289. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/ObjectList.cs`** -> AI Confidence: **99.31%**
290. **`src/VisualStudio/Core/Def/Options/VisualStudioSettingsOptionPersister.cs`** -> AI Confidence: **99.31%**
291. **`src/VisualStudio/Core/Def/Preview/TopLevelChange.cs`** -> AI Confidence: **99.31%**
292. **`src/VisualStudio/Core/Def/PreviewPane/PreviewPane.xaml.cs`** -> AI Confidence: **99.31%**
293. **`src/VisualStudio/Core/Impl/CodeModel/FileCodeModel_Events.cs`** -> AI Confidence: **99.31%**
294. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/InProcessIdeTestInvoker.cs`** -> AI Confidence: **99.31%**
295. **`src/Workspaces/CSharp/Portable/Classification/ClassificationHelpers.cs`** -> AI Confidence: **99.31%**
296. **`src/Workspaces/CSharp/Portable/Classification/Worker.cs`** -> AI Confidence: **99.31%**
297. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpEscapingReducer.cs`** -> AI Confidence: **99.31%**
298. **`src/Workspaces/Core/Portable/CodeFixes/CodeFixContext.cs`** -> AI Confidence: **99.31%**
299. **`src/Workspaces/Core/Portable/Diagnostics/DiagnosticAnalysisResultBuilder.cs`** -> AI Confidence: **99.31%**
300. **`src/Workspaces/Core/Portable/ObsoleteSymbol/AbstractObsoleteSymbolService.cs`** -> AI Confidence: **99.31%**
301. **`src/Workspaces/Core/Portable/Recommendations/AbstractRecommendationServiceRunner.cs`** -> AI Confidence: **99.31%**
302. **`src/Workspaces/Core/Portable/Shared/Extensions/SyntaxGeneratorExtensions.cs`** -> AI Confidence: **99.31%**
303. **`src/Workspaces/Core/Portable/Shared/Utilities/DocumentationComment.cs`** -> AI Confidence: **99.31%**
304. **`src/Workspaces/CoreTest/CodeCleanup/ReduceTokenTests.cs`** -> AI Confidence: **99.31%**
305. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/EmbeddedLanguages/VirtualChars/CSharpVirtualCharService.cs`** -> AI Confidence: **99.31%**
306. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/ExpressionSyntaxExtensions.cs`** -> AI Confidence: **99.31%**
307. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/ParenthesizedExpressionSyntaxExtensions.cs`** -> AI Confidence: **99.31%**
308. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/SemanticModelExtensions.cs`** -> AI Confidence: **99.31%**
309. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Extensions/SyntaxTokenExtensions.cs`** -> AI Confidence: **99.31%**
310. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/ElasticTriviaFormattingRule.cs`** -> AI Confidence: **99.31%**
311. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/IndentBlockFormattingRule.cs`** -> AI Confidence: **99.31%**
312. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/SpacingFormattingRule.cs`** -> AI Confidence: **99.31%**
313. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/SuppressFormattingRule.cs`** -> AI Confidence: **99.31%**
314. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/TokenBasedFormattingRule.cs`** -> AI Confidence: **99.31%**
315. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Utilities/FormattingRangeHelper.cs`** -> AI Confidence: **99.31%**
316. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Extensions/OperationExtensions.cs`** -> AI Confidence: **99.31%**
317. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/FlowAnalysis/SymbolUsageAnalysis/SymbolUsageAnalysis.Walker.cs`** -> AI Confidence: **99.31%**
318. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/EditorConfig/EditorConfigNamingStyleParser_SymbolSpec.cs`** -> AI Confidence: **99.31%**
319. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Serialization/ObjectWriter.cs`** -> AI Confidence: **99.31%**
320. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/CodeGeneration/NamedTypeGenerator.cs`** -> AI Confidence: **99.31%**
321. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ContextQuery/SyntaxTreeExtensions.cs`** -> AI Confidence: **99.31%**
322. **`.github/skills/ci-analysis/scripts/Get-CIStatus.ps1`** -> AI Confidence: **99.29%**
323. **`.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1`** -> AI Confidence: **99.29%**
324. **`eng/common/dotnet-install.ps1`** -> AI Confidence: **99.29%**
325. **`eng/common/dotnet.ps1`** -> AI Confidence: **99.29%**
326. **`eng/common/generate-locproject.ps1`** -> AI Confidence: **99.29%**
327. **`eng/common/init-tools-native.ps1`** -> AI Confidence: **99.29%**
328. **`eng/common/internal-feed-operations.ps1`** -> AI Confidence: **99.29%**
329. **`eng/common/pipeline-logging-functions.ps1`** -> AI Confidence: **99.29%**
330. **`eng/common/sdk-task.ps1`** -> AI Confidence: **99.29%**
331. **`eng/common/sdl/configure-sdl-tool.ps1`** -> AI Confidence: **99.29%**
332. **`eng/common/sdl/execute-all-sdl-tools.ps1`** -> AI Confidence: **99.29%**
333. **`eng/common/sdl/extract-artifact-archives.ps1`** -> AI Confidence: **99.29%**
334. **`eng/common/sdl/extract-artifact-packages.ps1`** -> AI Confidence: **99.29%**
335. **`eng/common/sdl/run-sdl.ps1`** -> AI Confidence: **99.29%**
336. **`eng/common/tools.ps1`** -> AI Confidence: **99.29%**
337. **`eng/common/vmr-sync.ps1`** -> AI Confidence: **99.29%**
338. **`eng/make-bootstrap.ps1`** -> AI Confidence: **99.29%**
339. **`eng/todo-check.ps1`** -> AI Confidence: **99.29%**
340. **`eng/validate-code-formatting.ps1`** -> AI Confidence: **99.29%**
341. **`eng/validate-rules-missing-documentation.ps1`** -> AI Confidence: **99.29%**
342. **`scripts/PublicApi/mark-shipped.ps1`** -> AI Confidence: **99.29%**
343. **`scripts/UploadAzureZip/CreateAndUploadNugetZip.ps1`** -> AI Confidence: **99.29%**
344. **`scripts/cleanup_perf.ps1`** -> AI Confidence: **99.29%**
345. **`scripts/vscode-run-tests.ps1`** -> AI Confidence: **99.29%**
346. **`src/RoslynAnalyzers/assets/install.ps1`** -> AI Confidence: **99.29%**
347. **`src/RoslynAnalyzers/assets/uninstall.ps1`** -> AI Confidence: **99.29%**
348. **`src/Setup/PowerShell/install.ps1`** -> AI Confidence: **99.29%**
349. **`src/Setup/PowerShell/uninstall.ps1`** -> AI Confidence: **99.29%**
350. **`eng/common/init-tools-native.sh`** -> AI Confidence: **99.29%**
351. **`eng/common/native/init-compiler.sh`** -> AI Confidence: **99.29%**
352. **`eng/common/native/init-distro-rid.sh`** -> AI Confidence: **99.29%**
353. **`src/Compilers/CSharp/Portable/Binder/EarlyWellKnownAttributeBinder.cs`** -> AI Confidence: **99.29%**
354. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/ConversionKindExtensions.cs`** -> AI Confidence: **99.29%**
355. **`src/Compilers/CSharp/Portable/BoundTree/BoundAwaitableInfo.cs`** -> AI Confidence: **99.29%**
356. **`src/Compilers/CSharp/Portable/BoundTree/BoundConversion.cs`** -> AI Confidence: **99.29%**
357. **`src/Compilers/CSharp/Portable/BoundTree/BoundNode_Source.cs`** -> AI Confidence: **99.29%**
358. **`src/Compilers/CSharp/Portable/Errors/ErrorCode.cs`** -> AI Confidence: **99.29%**
359. **`src/Compilers/CSharp/Portable/Generated/ErrorFacts.Generated.cs`** -> AI Confidence: **99.29%**
360. **`src/Compilers/CSharp/Portable/Parser/Lexer_StringLiteral.cs`** -> AI Confidence: **99.29%**
361. **`src/Compilers/CSharp/Portable/Symbols/SpecialTypeExtensions.cs`** -> AI Confidence: **99.29%**
362. **`src/Compilers/Core/Portable/CodeGen/ILBuilderConversions.cs`** -> AI Confidence: **99.29%**
363. **`src/Compilers/Core/Portable/CodeGen/ILOpCodeExtensions.cs`** -> AI Confidence: **99.29%**
364. **`src/Compilers/Core/Portable/GlobalSuppressions.cs`** -> AI Confidence: **99.29%**
365. **`src/Dependencies/Collections/Internal/SR.cs`** -> AI Confidence: **99.29%**
366. **`src/Features/ExternalAccess/OmniSharp.CSharp/Formatting/OmniSharpSyntaxFormattingOptionsFactory.cs`** -> AI Confidence: **99.29%**
367. **`src/RoslynAnalyzers/Utilities/Compiler/DiagnosticHelpers.cs`** -> AI Confidence: **99.29%**
368. **`src/Workspaces/CSharp/Portable/Classification/Worker_Preprocesser.cs`** -> AI Confidence: **99.29%**
369. **`src/Analyzers/CSharp/Analyzers/UseCollectionExpression/UseCollectionExpressionHelpers.cs`** -> AI Confidence: **99.25%**
370. **`src/EditorFeatures/CSharp/StringCopyPaste/StringCopyPasteHelpers.cs`** -> AI Confidence: **99.25%**
371. **`src/Analyzers/CSharp/Analyzers/AddBraces/CSharpAddBracesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
372. **`src/Analyzers/CSharp/Analyzers/ConvertProgram/ConvertProgramAnalysis_TopLevelStatements.cs`** -> AI Confidence: **99.24%**
373. **`src/Analyzers/CSharp/Analyzers/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionDiagnosticAnalyzer.Analyzer.cs`** -> AI Confidence: **99.24%**
374. **`src/Analyzers/CSharp/Analyzers/InlineDeclaration/CSharpInlineDeclarationDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
375. **`src/Analyzers/CSharp/Analyzers/MakeStructMemberReadOnly/CSharpMakeStructMemberReadOnlyAnalyzer.cs`** -> AI Confidence: **99.24%**
376. **`src/Analyzers/CSharp/Analyzers/UseAutoProperty/CSharpUseAutoPropertyAnalyzer.cs`** -> AI Confidence: **99.24%**
377. **`src/Analyzers/CSharp/Analyzers/UseCollectionExpression/CSharpUseCollectionExpressionForBuilderDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
378. **`src/Analyzers/CSharp/CodeFixes/ConvertToRecord/ConvertToRecordEngine.cs`** -> AI Confidence: **99.24%**
379. **`src/Analyzers/CSharp/CodeFixes/GenerateMethod/GenerateDeconstructMethodCodeFixProvider.cs`** -> AI Confidence: **99.24%**
380. **`src/Analyzers/CSharp/CodeFixes/GenerateParameterizedMember/CSharpGenerateConversionService.cs`** -> AI Confidence: **99.24%**
381. **`src/Analyzers/CSharp/CodeFixes/Nullable/CSharpDeclareAsNullableCodeFixProvider.cs`** -> AI Confidence: **99.24%**
382. **`src/Analyzers/CSharp/CodeFixes/ReplaceDefaultLiteral/CSharpReplaceDefaultLiteralCodeFixProvider.cs`** -> AI Confidence: **99.24%**
383. **`src/Analyzers/CSharp/Tests/AddRequiredParentheses/AddRequiredPatternParenthesesTests.cs`** -> AI Confidence: **99.24%**
384. **`src/Analyzers/CSharp/Tests/ConditionalExpressionInStringInterpolation/CSharpAddParenthesesAroundConditionalExpressionInInterpolatedStringCodeFixProviderTests.cs`** -> AI Confidence: **99.24%**
385. **`src/Analyzers/CSharp/Tests/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionTests.cs`** -> AI Confidence: **99.24%**
386. **`src/Analyzers/CSharp/Tests/NewLines/ConsecutiveStatementPlacement/ConsecutiveStatementPlacementTests.cs`** -> AI Confidence: **99.24%**
387. **`src/Analyzers/CSharp/Tests/RemoveUnnecessaryParentheses/RemoveUnnecessaryPatternParenthesesTests.cs`** -> AI Confidence: **99.24%**
388. **`src/Analyzers/CSharp/Tests/ReplaceDefaultLiteral/ReplaceDefaultLiteralTests.cs`** -> AI Confidence: **99.24%**
389. **`src/Analyzers/CSharp/Tests/UseConditionalExpression/UseConditionalExpressionForAssignmentTests.cs`** -> AI Confidence: **99.24%**
390. **`src/Analyzers/Core/Analyzers/RemoveUnnecessarySuppressions/AbstractRemoveUnnecessaryPragmaSuppressionsDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
391. **`src/Analyzers/Core/Analyzers/RemoveUnusedMembers/AbstractRemoveUnusedMembersDiagnosticAnalyzer.cs`** -> AI Confidence: **99.24%**
392. **`src/Analyzers/Core/Analyzers/SimplifyInterpolation/AbstractSimplifyInterpolationHelpers.cs`** -> AI Confidence: **99.24%**
393. **`src/Compilers/CSharp/Portable/Binder/Binder.WithQueryLambdaParametersBinder.cs`** -> AI Confidence: **99.24%**
394. **`src/Compilers/CSharp/Portable/Binder/Binder_Symbols.cs`** -> AI Confidence: **99.24%**
395. **`src/Compilers/CSharp/Portable/Binder/Semantics/Conversions/Conversion.cs`** -> AI Confidence: **99.24%**
396. **`src/Compilers/CSharp/Portable/BoundTree/BoundDecisionDag.cs`** -> AI Confidence: **99.24%**
397. **`src/Compilers/CSharp/Portable/CodeGen/Optimizer.cs`** -> AI Confidence: **99.24%**
398. **`src/Compilers/CSharp/Portable/Compilation/CSharpCompilation.cs`** -> AI Confidence: **99.24%**
399. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.DocumentationCommentWalker.cs`** -> AI Confidence: **99.24%**
400. **`src/Compilers/CSharp/Portable/Compiler/MethodCompiler.cs`** -> AI Confidence: **99.24%**
401. **`src/Compilers/CSharp/Portable/Emitter/Model/PEModuleBuilder.cs`** -> AI Confidence: **99.24%**
402. **`src/Compilers/CSharp/Portable/Emitter/NoPia/EmbeddedTypesManager.cs`** -> AI Confidence: **99.24%**
403. **`src/Compilers/CSharp/Portable/Lowering/AsyncRewriter/AsyncMethodToStateMachineRewriter.cs`** -> AI Confidence: **99.24%**
404. **`src/Compilers/CSharp/Portable/Lowering/ClosureConversion/ClosureConversion.Analysis.cs`** -> AI Confidence: **99.24%**
405. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.cs`** -> AI Confidence: **99.24%**
406. **`src/Compilers/CSharp/Portable/Parser/SlidingTextWindow.cs`** -> AI Confidence: **99.24%**
407. **`src/Compilers/CSharp/Portable/Symbols/FunctionPointers/FunctionPointerMethodSymbol.cs`** -> AI Confidence: **99.24%**
408. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEFieldSymbol.cs`** -> AI Confidence: **99.24%**
409. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEModuleSymbol.cs`** -> AI Confidence: **99.24%**
410. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PENamedTypeSymbol.cs`** -> AI Confidence: **99.24%**
411. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEParameterSymbol.cs`** -> AI Confidence: **99.24%**
412. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEPropertySymbol.cs`** -> AI Confidence: **99.24%**
413. **`src/Compilers/CSharp/Portable/Symbols/NamedTypeSymbol.cs`** -> AI Confidence: **99.24%**
414. **`src/Compilers/CSharp/Portable/Symbols/ReferenceManager.cs`** -> AI Confidence: **99.24%**
415. **`src/Compilers/CSharp/Portable/Symbols/Source/GlobalExpressionVariable.cs`** -> AI Confidence: **99.24%**
416. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceConstructorSymbolBase.cs`** -> AI Confidence: **99.24%**
417. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceFieldLikeEventSymbol.cs`** -> AI Confidence: **99.24%**
418. **`src/Compilers/CSharp/Portable/Symbols/Symbol.cs`** -> AI Confidence: **99.24%**
419. **`src/Compilers/CSharp/Portable/Syntax/CSharpSyntaxTree.cs`** -> AI Confidence: **99.24%**
420. **`src/Compilers/CSharp/Portable/Syntax/SyntaxFactory.cs`** -> AI Confidence: **99.24%**
421. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncEHTests.cs`** -> AI Confidence: **99.24%**
422. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenNullCoalescingAssignmentTests.cs`** -> AI Confidence: **99.24%**
423. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTestBase.cs`** -> AI Confidence: **99.24%**
424. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IObjectCreationExpression.cs`** -> AI Confidence: **99.24%**
425. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullConditionalAssignmentTests.cs`** -> AI Confidence: **99.24%**
426. **`src/Compilers/CSharp/Test/Symbol/Symbols/MissingSpecialMember.cs`** -> AI Confidence: **99.24%**
427. **`src/Compilers/CSharp/Test/Syntax/Parsing/DeclarationParsingTests.cs`** -> AI Confidence: **99.24%**
428. **`src/Compilers/Core/CodeAnalysisTest/Collections/DebuggerAttributes.cs`** -> AI Confidence: **99.24%**
429. **`src/Compilers/Core/CodeAnalysisTest/FileUtilitiesTests.cs`** -> AI Confidence: **99.24%**
430. **`src/Compilers/Core/MSBuildTask/MapSourceRoots.cs`** -> AI Confidence: **99.24%**
431. **`src/Compilers/Core/Portable/CaseInsensitiveComparison.cs`** -> AI Confidence: **99.24%**
432. **`src/Compilers/Core/Portable/CodeGen/LocalScopeManager.cs`** -> AI Confidence: **99.24%**
433. **`src/Compilers/Core/Portable/CommandLine/CommandLineArguments.cs`** -> AI Confidence: **99.24%**
434. **`src/Compilers/Core/Portable/CommandLine/CommonCompiler.cs`** -> AI Confidence: **99.24%**
435. **`src/Compilers/Core/Portable/CryptographicHashProvider.cs`** -> AI Confidence: **99.24%**
436. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerAssemblyLoader.cs`** -> AI Confidence: **99.24%**
437. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerDriver.cs`** -> AI Confidence: **99.24%**
438. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerFileReference.cs`** -> AI Confidence: **99.24%**
439. **`src/Compilers/Core/Portable/Emit/EditAndContinue/DefinitionMap.cs`** -> AI Confidence: **99.24%**
440. **`src/Compilers/Core/Portable/Emit/EditAndContinue/DeltaMetadataWriter.cs`** -> AI Confidence: **99.24%**
441. **`src/Compilers/Core/Portable/FileSystem/PathUtilities.cs`** -> AI Confidence: **99.24%**
442. **`src/Compilers/Core/Portable/PEWriter/MetadataWriter.DynamicAnalysis.cs`** -> AI Confidence: **99.24%**
443. **`src/Compilers/Core/Portable/PEWriter/PeWriter.cs`** -> AI Confidence: **99.24%**
444. **`src/Compilers/Core/Portable/ReferenceManager/CommonReferenceManager.Binding.cs`** -> AI Confidence: **99.24%**
445. **`src/Compilers/Core/Portable/ResourceDescription.cs`** -> AI Confidence: **99.24%**
446. **`src/Compilers/Core/Portable/SourceGeneration/AdditionalSourcesCollection.cs`** -> AI Confidence: **99.24%**
447. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/PredicateSyntaxStrategy.cs`** -> AI Confidence: **99.24%**
448. **`src/Compilers/Core/Portable/SourceGeneration/Nodes/SourceOutputNode.cs`** -> AI Confidence: **99.24%**
449. **`src/Compilers/Core/Portable/StrongName/StrongNameKeys.cs`** -> AI Confidence: **99.24%**
450. **`src/Compilers/Core/Portable/Syntax/GreenNode.cs`** -> AI Confidence: **99.24%**
451. **`src/Compilers/Core/Portable/Syntax/SyntaxList`1.cs`** -> AI Confidence: **99.24%**
452. **`src/Compilers/Core/Portable/Syntax/SyntaxNodeExtensions_Tracking.cs`** -> AI Confidence: **99.24%**
453. **`src/Compilers/Core/Portable/Syntax/SyntaxTriviaList.cs`** -> AI Confidence: **99.24%**
454. **`src/Compilers/Core/Portable/Text/CompositeText.cs`** -> AI Confidence: **99.24%**
455. **`src/Compilers/Core/Portable/Text/SourceText.cs`** -> AI Confidence: **99.24%**
456. **`src/Compilers/Core/Portable/TreeDumper.cs`** -> AI Confidence: **99.24%**
457. **`src/Compilers/Server/VBCSCompiler/BuildServerController.cs`** -> AI Confidence: **99.24%**
458. **`src/Compilers/Server/VBCSCompiler/NamedPipeClientConnectionHost.cs`** -> AI Confidence: **99.24%**
459. **`src/Compilers/Shared/CompilerServerLogger.cs`** -> AI Confidence: **99.24%**
460. **`src/Compilers/Test/Core/Assert/AssertEx.cs`** -> AI Confidence: **99.24%**
461. **`src/Compilers/Test/Core/Compilation/CompilationExtensions.cs`** -> AI Confidence: **99.24%**
462. **`src/Compilers/Test/Core/InstrumentationChecker.cs`** -> AI Confidence: **99.24%**
463. **`src/Compilers/Test/Core/Platform/Desktop/RuntimeAssemblyManager.cs`** -> AI Confidence: **99.24%**
464. **`src/Compilers/Test/Utilities/CSharp/Extensions.cs`** -> AI Confidence: **99.24%**
465. **`src/Dependencies/Collections/OneOrMany.cs`** -> AI Confidence: **99.24%**
466. **`src/EditorFeatures/CSharp/StringCopyPaste/KnownSourcePasteProcessor.cs`** -> AI Confidence: **99.24%**
467. **`src/EditorFeatures/CSharpTest/Formatting/Indentation/SmartIndenterEnterOnTokenTests.cs`** -> AI Confidence: **99.24%**
468. **`src/EditorFeatures/Core/InlineRename/AbstractInlineRenameUndoManager.cs`** -> AI Confidence: **99.24%**
469. **`src/EditorFeatures/Core/LineSeparators/LineSeparatorAdornmentManager.cs`** -> AI Confidence: **99.24%**
470. **`src/EditorFeatures/Core/Preview/SolutionPreviewResult.cs`** -> AI Confidence: **99.24%**
471. **`src/EditorFeatures/Test/Snippets/RoslynLSPSnippetConvertTests.cs`** -> AI Confidence: **99.24%**
472. **`src/EditorFeatures/Test/Utilities/StackFrameUtils.cs`** -> AI Confidence: **99.24%**
473. **`src/EditorFeatures/TestUtilities/Workspaces/EditorTestHostDocument.cs`** -> AI Confidence: **99.24%**
474. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/CompilationContext.cs`** -> AI Confidence: **99.24%**
475. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/SyntaxHelpers.cs`** -> AI Confidence: **99.24%**
476. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/DkmUtilities.cs`** -> AI Confidence: **99.24%**
477. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/FrameDecoder.cs`** -> AI Confidence: **99.24%**
478. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/MetadataUtilities.cs`** -> AI Confidence: **99.24%**
479. **`src/ExpressionEvaluator/Core/Source/FunctionResolver/MetadataResolver.cs`** -> AI Confidence: **99.24%**
480. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Helpers/TypeHelpers.cs`** -> AI Confidence: **99.24%**
481. **`src/ExpressionEvaluator/Core/Test/ResultProvider/Debugger/Engine/DkmClrValue.cs`** -> AI Confidence: **99.24%**
482. **`src/Features/CSharp/Portable/AddImport/CSharpAddImportFeatureService.cs`** -> AI Confidence: **99.24%**
483. **`src/Features/CSharp/Portable/ConvertForToForEach/CSharpConvertForToForEachCodeRefactoringProvider.cs`** -> AI Confidence: **99.24%**
484. **`src/Features/CSharp/Portable/ConvertLinq/CSharpConvertLinqQueryToForEachProvider.cs`** -> AI Confidence: **99.24%**
485. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/AbstractToMethodConverter.cs`** -> AI Confidence: **99.24%**
486. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/CSharpConvertForEachToLinqQueryProvider.cs`** -> AI Confidence: **99.24%**
487. **`src/Features/CSharp/Portable/DocumentationComments/CSharpDocumentationCommentSnippetService.cs`** -> AI Confidence: **99.24%**
488. **`src/Features/CSharp/Portable/GenerateType/CSharpGenerateTypeService.cs`** -> AI Confidence: **99.24%**
489. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/SwitchStatementHighlighter.cs`** -> AI Confidence: **99.24%**
490. **`src/Features/CSharp/Portable/LineSeparators/CSharpLineSeparatorService.cs`** -> AI Confidence: **99.24%**
491. **`src/Features/CSharp/Portable/QuickInfo/CSharpSyntacticQuickInfoProvider.cs`** -> AI Confidence: **99.24%**
492. **`src/Features/CSharp/Portable/SolutionExplorer/CSharpSolutionExplorerSymbolTreeItemProvider.cs`** -> AI Confidence: **99.24%**
493. **`src/Features/CSharpTest/ReplaceConditionalWithStatements/ReplaceConditionalWithStatementsTests.cs`** -> AI Confidence: **99.24%**
494. **`src/Features/Core/Portable/Completion/FileSystemCompletionHelper.cs`** -> AI Confidence: **99.24%**
495. **`src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs`** -> AI Confidence: **99.24%**
496. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexEmbeddedCompletionProvider.cs`** -> AI Confidence: **99.24%**
497. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/RegexLexer.cs`** -> AI Confidence: **99.24%**
498. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.cs`** -> AI Confidence: **99.24%**
499. **`src/Features/Core/Portable/LanguageServices/SymbolDisplayService/AbstractSymbolDisplayService.AbstractSymbolDescriptionBuilder.cs`** -> AI Confidence: **99.24%**
500. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/AutoLoadProjectsInitializer.cs`** -> AI Confidence: **99.24%**
501. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LoadedProject.cs`** -> AI Confidence: **99.24%**
502. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/Logging/RoslynLogger.cs`** -> AI Confidence: **99.24%**
503. **`src/LanguageServer/Protocol/Extensions/ProtocolConversions.cs`** -> AI Confidence: **99.24%**
504. **`src/LanguageServer/Protocol/Protocol/Converters/SumConverter.cs`** -> AI Confidence: **99.24%**
505. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompareSymbolsCorrectlyAnalyzer.cs`** -> AI Confidence: **99.24%**
506. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticAnalyzerAPIUsageAnalyzer.cs`** -> AI Confidence: **99.24%**
507. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/CallSiteImplicitAllocationAnalyzer.cs`** -> AI Confidence: **99.24%**
508. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/Analyzers/EnumeratorAllocationAnalyzer.cs`** -> AI Confidence: **99.24%**
509. **`src/RoslynAnalyzers/PublicApiAnalyzers/Core/CodeFixes/AnnotatePublicApiFix.cs`** -> AI Confidence: **99.24%**
510. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/CSharpSpecializedEnumerableCreationAnalyzer.cs`** -> AI Confidence: **99.24%**
511. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/AbstractDoNotCopyValue.cs`** -> AI Confidence: **99.24%**
512. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/AbstractExposeMemberForTesting`1.cs`** -> AI Confidence: **99.24%**
513. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/DefaultableTypeShouldHaveDefaultableFieldsAnalyzer.cs`** -> AI Confidence: **99.24%**
514. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/DoNotCallGetTestAccessor.cs`** -> AI Confidence: **99.24%**
515. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/ExportedPartsShouldHaveImportingConstructorCodeFixProvider.cs`** -> AI Confidence: **99.24%**
516. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/SymbolDeclaredEventMustBeGeneratedForSourceSymbols.cs`** -> AI Confidence: **99.24%**
517. **`src/RoslynAnalyzers/Text.Analyzers/Core/IdentifiersShouldBeSpelledCorrectly.cs`** -> AI Confidence: **99.24%**
518. **`src/RoslynAnalyzers/Tools/GenerateDocumentationAndConfigFiles/Program.cs`** -> AI Confidence: **99.24%**
519. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/CodeAnalysisMetricData.cs`** -> AI Confidence: **99.24%**
520. **`src/RoslynAnalyzers/Utilities/Compiler/Options/SymbolNamesWithValueOption.cs`** -> AI Confidence: **99.24%**
521. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/CopyAnalysis/CopyAnalysis.CopyDataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
522. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/PropertySetAnalysis.cs`** -> AI Confidence: **99.24%**
523. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`** -> AI Confidence: **99.24%**
524. **`src/Scripting/CSharpTest/ObjectFormatterTests.cs`** -> AI Confidence: **99.24%**
525. **`src/Scripting/Core/Hosting/AssemblyLoader/InteractiveAssemblyLoader.cs`** -> AI Confidence: **99.24%**
526. **`src/Scripting/Core/Hosting/CommandLine/CommandLineRunner.cs`** -> AI Confidence: **99.24%**
527. **`src/Tools/ExternalAccess/Razor/Features/RazorAnalyzerAssemblyResolver.cs`** -> AI Confidence: **99.24%**
528. **`src/Tools/Source/RunTests/ProcessRunner.cs`** -> AI Confidence: **99.24%**
529. **`src/Tools/Source/RunTests/TestRunner.cs`** -> AI Confidence: **99.24%**
530. **`src/VisualStudio/CSharp/Impl/LanguageService/CSharpHelpContextService.cs`** -> AI Confidence: **99.24%**
531. **`src/VisualStudio/Core/Def/DocumentOutline/DocumentOutlineView.xaml.cs`** -> AI Confidence: **99.24%**
532. **`src/VisualStudio/Core/Def/GenerateType/GenerateTypeDialogViewModel.cs`** -> AI Confidence: **99.24%**
533. **`src/VisualStudio/Core/Def/Implementation/ContainedLanguageRefactorNotifyService.cs`** -> AI Confidence: **99.24%**
534. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractDescriptionBuilder.cs`** -> AI Confidence: **99.24%**
535. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractListItemFactory.cs`** -> AI Confidence: **99.24%**
536. **`src/VisualStudio/Core/Def/Library/ObjectBrowser/AbstractObjectBrowserLibraryManager.cs`** -> AI Confidence: **99.24%**
537. **`src/VisualStudio/Core/Def/NavigationBar/NavigationBarClient.cs`** -> AI Confidence: **99.24%**
538. **`src/VisualStudio/Core/Def/PreviewPane/PreviewPaneService.cs`** -> AI Confidence: **99.24%**
539. **`src/VisualStudio/Core/Def/ProjectSystem/VisualStudioWorkspaceImpl.cs`** -> AI Confidence: **99.24%**
540. **`src/VisualStudio/Core/Def/UnusedReferences/Dialog/UnusedReferencesTableProvider.DataSource.cs`** -> AI Confidence: **99.24%**
541. **`src/VisualStudio/Core/Def/Utilities/AutomationDelegatingListView.cs`** -> AI Confidence: **99.24%**
542. **`src/VisualStudio/Core/Impl/SolutionExplorer/AnalyzerReferenceManager.cs`** -> AI Confidence: **99.24%**
543. **`src/VisualStudio/Core/Impl/SolutionExplorer/AnalyzersCommandHandler.cs`** -> AI Confidence: **99.24%**
544. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/VisualStudioInstance.cs`** -> AI Confidence: **99.24%**
545. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/NameSyntaxClassifier.cs`** -> AI Confidence: **99.24%**
546. **`src/Workspaces/CSharp/Portable/Recommendations/CSharpRecommendationServiceRunner.cs`** -> AI Confidence: **99.24%**
547. **`src/Workspaces/CSharp/Portable/Rename/CSharpRenameRewriterLanguageService.cs`** -> AI Confidence: **99.24%**
548. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpExtensionMethodReducer.cs`** -> AI Confidence: **99.24%**
549. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/CSharpMiscellaneousReducer.cs`** -> AI Confidence: **99.24%**
550. **`src/Workspaces/CSharp/Portable/Simplification/Simplifiers/ExpressionSimplifier.cs`** -> AI Confidence: **99.24%**
551. **`src/Workspaces/CSharp/Portable/Simplification/Simplifiers/NameSimplifier.cs`** -> AI Confidence: **99.24%**
552. **`src/Workspaces/Core/Portable/FindSymbols/FindLiterals/FindLiteralsSearchEngine.cs`** -> AI Confidence: **99.24%**
553. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/OrdinaryMethodReferenceFinder.cs`** -> AI Confidence: **99.24%**
554. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/ParameterSymbolReferenceFinder.cs`** -> AI Confidence: **99.24%**
555. **`src/Workspaces/Core/Portable/PatternMatching/PatternMatcher.cs`** -> AI Confidence: **99.24%**
556. **`src/Workspaces/Core/Portable/Shared/Extensions/ISymbolExtensions.cs`** -> AI Confidence: **99.24%**
557. **`src/Workspaces/Core/Portable/Shared/Extensions/SemanticModelExtensions.cs`** -> AI Confidence: **99.24%**
558. **`src/Workspaces/CoreTestUtilities/Workspaces/TestHostProject`1.cs`** -> AI Confidence: **99.24%**
559. **`src/Workspaces/MSBuild/Core/MSBuild/BuildHostProcessManager.cs`** -> AI Confidence: **99.24%**
560. **`src/Workspaces/MSBuild/Core/MSBuild/MSBuildWorkspace.cs`** -> AI Confidence: **99.24%**
561. **`src/Workspaces/Remote/Core/Serialization/MessagePackFormatters.cs`** -> AI Confidence: **99.24%**
562. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Formatting/Rules/WrappingFormattingRule.cs`** -> AI Confidence: **99.24%**
563. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Simplification/Simplifiers/CastSimplifier.cs`** -> AI Confidence: **99.24%**
564. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/BottomUpBaseIndentationFinder.cs`** -> AI Confidence: **99.24%**
565. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/NamingStyle.cs`** -> AI Confidence: **99.24%**
566. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/AbstractSpeculationAnalyzer.cs`** -> AI Confidence: **99.24%**
567. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Extensions/Symbols/ITypeSymbolExtensions.cs`** -> AI Confidence: **99.24%**
568. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/CodeGeneration/EnumMemberGenerator.cs`** -> AI Confidence: **99.24%**
569. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Extensions/ITypeParameterSymbolExtensions.cs`** -> AI Confidence: **99.24%**
570. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/Indentation/CSharpIndentationService.Indenter.cs`** -> AI Confidence: **99.24%**
571. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/CSharp/LanguageServices/CSharpReplaceDiscardDeclarationsWithAssignmentsService.cs`** -> AI Confidence: **99.24%**
572. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/ISolutionExtensions.cs`** -> AI Confidence: **99.24%**
573. **`src/Workspaces/SharedUtilitiesAndExtensions/Workspace/Core/Extensions/SyntaxGeneratorExtensions_CreateEqualsMethod.cs`** -> AI Confidence: **99.24%**
574. **`src/Analyzers/CSharp/Analyzers/RemoveUnnecessaryNullableDirective/NullableImpactingSpanWalker.cs`** -> AI Confidence: **99.23%**
575. **`src/Analyzers/CSharp/Tests/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionFixAllTests.cs`** -> AI Confidence: **99.23%**
576. **`src/Analyzers/CSharp/Tests/RemoveConfusingSuppression/RemoveConfusingSuppressionTests.cs`** -> AI Confidence: **99.23%**
577. **`src/Analyzers/CSharp/Tests/UseDefaultLiteral/UseDefaultLiteralTests.cs`** -> AI Confidence: **99.23%**
578. **`src/Analyzers/Core/Analyzers/UseObjectInitializer/UseNamedMemberInitializerAnalyzer.cs`** -> AI Confidence: **99.23%**
579. **`src/Analyzers/Core/CodeFixes/GenerateMember/AbstractGenerateMemberService.cs`** -> AI Confidence: **99.23%**
580. **`src/Compilers/CSharp/Portable/Binder/Binder.cs`** -> AI Confidence: **99.23%**
581. **`src/Compilers/CSharp/Portable/Binder/PatternExplainer.cs`** -> AI Confidence: **99.23%**
582. **`src/Compilers/CSharp/Portable/Binder/RefSafetyAnalysis.cs`** -> AI Confidence: **99.23%**
583. **`src/Compilers/CSharp/Portable/Binder/SwitchBinder_Patterns.cs`** -> AI Confidence: **99.23%**
584. **`src/Compilers/CSharp/Portable/Binder/SwitchExpressionBinder.cs`** -> AI Confidence: **99.23%**
585. **`src/Compilers/CSharp/Portable/Binder/WithCrefTypeParametersBinder.cs`** -> AI Confidence: **99.23%**
586. **`src/Compilers/CSharp/Portable/BoundTree/BoundNodeExtensions.cs`** -> AI Confidence: **99.23%**
587. **`src/Compilers/CSharp/Portable/CSharpExtensions.cs`** -> AI Confidence: **99.23%**
588. **`src/Compilers/CSharp/Portable/CodeGen/EmitArrayInitializer.cs`** -> AI Confidence: **99.23%**
589. **`src/Compilers/CSharp/Portable/CodeGen/EmitOperators.cs`** -> AI Confidence: **99.23%**
590. **`src/Compilers/CSharp/Portable/Declarations/MergedTypeDeclaration.cs`** -> AI Confidence: **99.23%**
591. **`src/Compilers/CSharp/Portable/DocumentationComments/SourceDocumentationCommentUtils.cs`** -> AI Confidence: **99.23%**
592. **`src/Compilers/CSharp/Portable/FlowAnalysis/AlwaysAssignedWalker.cs`** -> AI Confidence: **99.23%**
593. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter.PatternLocalRewriter.cs`** -> AI Confidence: **99.23%**
594. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_DeconstructionAssignmentOperator.cs`** -> AI Confidence: **99.23%**
595. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_ForEachStatement.cs`** -> AI Confidence: **99.23%**
596. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LoweredDynamicOperationFactory.cs`** -> AI Confidence: **99.23%**
597. **`src/Compilers/CSharp/Portable/Lowering/SpillSequenceSpiller.cs`** -> AI Confidence: **99.23%**
598. **`src/Compilers/CSharp/Portable/Lowering/StateMachineRewriter/ResumableStateMachineStateAllocator.cs`** -> AI Confidence: **99.23%**
599. **`src/Compilers/CSharp/Portable/Symbols/AbstractTypeMap.cs`** -> AI Confidence: **99.23%**
600. **`src/Compilers/CSharp/Portable/Symbols/Attributes/PEAttributeData.cs`** -> AI Confidence: **99.23%**
601. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/DynamicTypeDecoder.cs`** -> AI Confidence: **99.23%**
602. **`src/Compilers/CSharp/Portable/Symbols/MetadataOrSourceAssemblySymbol.cs`** -> AI Confidence: **99.23%**
603. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceFieldSymbol.cs`** -> AI Confidence: **99.23%**
604. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/Records/SynthesizedPrimaryConstructor.cs`** -> AI Confidence: **99.23%**
605. **`src/Compilers/CSharp/Portable/Utilities/ValueSetFactory.NumericValueSet.cs`** -> AI Confidence: **99.23%**
606. **`src/Compilers/CSharp/Test/Emit3/Diagnostics/OperationAnalyzerTests.cs`** -> AI Confidence: **99.23%**
607. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests2.cs`** -> AI Confidence: **99.23%**
608. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ICompoundAssignmentOperation.cs`** -> AI Confidence: **99.23%**
609. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IMethodReferenceOperation.cs`** -> AI Confidence: **99.23%**
610. **`src/Compilers/Core/Portable/Binding/BindingDiagnosticBag.cs`** -> AI Confidence: **99.23%**
611. **`src/Compilers/Core/Portable/CodeGen/ILBuilderEmit.cs`** -> AI Confidence: **99.23%**
612. **`src/Compilers/Core/Portable/CodeGen/LocalSlotManager.cs`** -> AI Confidence: **99.23%**
613. **`src/Compilers/Core/Portable/CommandLine/AnalyzerConfig.cs`** -> AI Confidence: **99.23%**
614. **`src/Compilers/Core/Portable/Diagnostic/DiagnosticDescriptor.cs`** -> AI Confidence: **99.23%**
615. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/ShadowCopyAnalyzerPathResolver.cs`** -> AI Confidence: **99.23%**
616. **`src/Compilers/Core/Portable/Emit/NoPia/CommonEmbeddedType.cs`** -> AI Confidence: **99.23%**
617. **`src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.RegionBuilder.cs`** -> AI Confidence: **99.23%**
618. **`src/Compilers/Core/Portable/RuleSet/RuleSet.cs`** -> AI Confidence: **99.23%**
619. **`src/Compilers/Core/Portable/RuleSet/RuleSetProcessor.cs`** -> AI Confidence: **99.23%**
620. **`src/Compilers/Core/Portable/Syntax/SyntaxNodeOrToken.cs`** -> AI Confidence: **99.23%**
621. **`src/Compilers/Test/Utilities/CSharp/MockCSharpCompiler.cs`** -> AI Confidence: **99.23%**
622. **`src/EditorFeatures/CSharpTest/DecompiledSource/DecompiledSourceFormattingTests.cs`** -> AI Confidence: **99.23%**
623. **`src/EditorFeatures/CSharpTest/KeywordHighlighting/LoopHighlighterTests.cs`** -> AI Confidence: **99.23%**
624. **`src/EditorFeatures/CSharpTest/SymbolKey/SymbolKeyTestBase.cs`** -> AI Confidence: **99.23%**
625. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Expansion/MemberExpansion.cs`** -> AI Confidence: **99.23%**
626. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Helpers/InlineArrayHelpers.cs`** -> AI Confidence: **99.23%**
627. **`src/Features/CSharp/Portable/CodeLens/CSharpCodeLensDisplayInfoService.cs`** -> AI Confidence: **99.23%**
628. **`src/Features/CSharp/Portable/Completion/KeywordRecommenders/RefKeywordRecommender.cs`** -> AI Confidence: **99.23%**
629. **`src/Features/CSharp/Portable/EditAndContinue/BreakpointSpans.cs`** -> AI Confidence: **99.23%**
630. **`src/Features/CSharp/Portable/ExtractMethod/Extensions.cs`** -> AI Confidence: **99.23%**
631. **`src/Features/Core/Portable/Completion/Providers/AbstractObjectInitializerCompletionProvider.cs`** -> AI Confidence: **99.23%**
632. **`src/Features/Core/Portable/PdbSourceDocument/SourceLinkMap.cs`** -> AI Confidence: **99.23%**
633. **`src/Features/Core/Portable/QuickInfo/Presentation/QuickInfoContentBuilder.cs`** -> AI Confidence: **99.23%**
634. **`src/Interactive/Host/Interactive/Core/InteractiveHost.LazyRemoteService.cs`** -> AI Confidence: **99.23%**
635. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompilerExtensionStrictApiAnalyzer.cs`** -> AI Confidence: **99.23%**
636. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/CompilerExtensionTargetFrameworkAnalyzer.cs`** -> AI Confidence: **99.23%**
637. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/PreferNullLiteral.cs`** -> AI Confidence: **99.23%**
638. **`src/RoslynAnalyzers/Utilities/Compiler/RulesetToEditorconfigConverter.cs`** -> AI Confidence: **99.23%**
639. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/TaintedDataAnalysis/PooledHashSetExtensions.cs`** -> AI Confidence: **99.23%**
640. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/PredicatedAnalysisData.cs`** -> AI Confidence: **99.23%**
641. **`src/Scripting/CSharp/CSharpScript.cs`** -> AI Confidence: **99.23%**
642. **`src/Scripting/Core/Hosting/Resolvers/RuntimeMetadataReferenceResolver.cs`** -> AI Confidence: **99.23%**
643. **`src/Test/PdbUtilities/Reader/SymReaderFactory.cs`** -> AI Confidence: **99.23%**
644. **`src/Test/PdbUtilities/Shared/DummyMetadataImport.cs`** -> AI Confidence: **99.23%**
645. **`src/VisualStudio/CSharp/Impl/CodeModel/ModifierFlagsExtensions.cs`** -> AI Confidence: **99.23%**
646. **`src/VisualStudio/Core/Def/ChangeSignature/AddParameterDialogViewModel.cs`** -> AI Confidence: **99.23%**
647. **`src/VisualStudio/Core/Def/ErrorReporting/VisualStudioErrorReportingService.ExceptionFormatting.cs`** -> AI Confidence: **99.23%**
648. **`src/VisualStudio/Core/Def/Notification/VSNotificationServiceFactory.cs`** -> AI Confidence: **99.23%**
649. **`src/VisualStudio/Core/Def/PdbSourceDocument/AbstractSourceLinkService.cs`** -> AI Confidence: **99.23%**
650. **`src/VisualStudio/Core/Def/Venus/VenusCommandFilter`2.cs`** -> AI Confidence: **99.23%**
651. **`src/VisualStudio/IntegrationTest/Harness/SourceGeneratorUnitTests/TestServicesSourceGeneratorTests.cs`** -> AI Confidence: **99.23%**
652. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/AutomationElementExtensions.cs`** -> AI Confidence: **99.23%**
653. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/QuickInfoToStringConverter.cs`** -> AI Confidence: **99.23%**
654. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/DiscardSyntaxClassifier.cs`** -> AI Confidence: **99.23%**
655. **`src/Workspaces/Core/Portable/Recommendations/AbstractRecommendationService.cs`** -> AI Confidence: **99.23%**
656. **`src/Workspaces/Core/Portable/Workspace/Host/TemporaryStorage/LegacyTemporaryStorageService.cs`** -> AI Confidence: **99.23%**
657. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/CodeStyle/TypeStyle/TypeStyleHelper.cs`** -> AI Confidence: **99.23%**
658. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/NamingStyles/Serialization/NamingStylePreferencesEditorConfigSerializer.cs`** -> AI Confidence: **99.23%**
659. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Serialization/ObjectReader.cs`** -> AI Confidence: **99.23%**
660. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Services/RefactoringHelpers/AbstractRefactoringHelpers.cs`** -> AI Confidence: **99.23%**
661. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/AsyncLazy`1.cs`** -> AI Confidence: **99.23%**
662. **`src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/SpecializedTasks.cs`** -> AI Confidence: **99.23%**
663. **`src/Compilers/CSharp/Portable/FlowAnalysis/ReadWriteWalker.cs`** -> AI Confidence: **99.22%**
664. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_ISwitchOperation.cs`** -> AI Confidence: **99.22%**
665. **`src/Compilers/Core/Portable/DiaSymReader/Utilities/ComMemoryStream.cs`** -> AI Confidence: **99.22%**
666. **`src/EditorFeatures/CSharpTest/KeywordHighlighting/SwitchStatementHighlighterTests.cs`** -> AI Confidence: **99.22%**
667. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/ComputationalComplexityMetrics.cs`** -> AI Confidence: **99.22%**
668. **`src/Compilers/CSharp/Portable/BoundTree/BoundInlineArrayAccess.cs`** -> AI Confidence: **99.2%**
669. **`src/Compilers/Core/Portable/EnumConstantHelper.cs`** -> AI Confidence: **99.2%**
670. **`src/Dependencies/Threading/ParallelExtensions.NetFramework.cs`** -> AI Confidence: **99.2%**
671. **`src/Analyzers/CSharp/Analyzers/HiddenExplicitCast/CSharpHiddenExplicitCastDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
672. **`src/Analyzers/CSharp/Analyzers/MisplacedUsingDirectives/MisplacedUsingDirectivesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
673. **`src/Analyzers/CSharp/Analyzers/NewLines/ConstructorInitializerPlacement/ConstructorInitializerPlacementDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
674. **`src/Analyzers/CSharp/Analyzers/SimplifyLinqExpression/CSharpSimplifyLinqTypeCheckAndCastDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
675. **`src/Analyzers/CSharp/Analyzers/UseExpressionBodyForLambda/UseExpressionBodyForLambdaHelpers.cs`** -> AI Confidence: **99.18%**
676. **`src/Analyzers/CSharp/Analyzers/UseIndexOrRangeOperator/CSharpUseIndexOperatorDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
677. **`src/Analyzers/CSharp/Analyzers/UseIsNullCheck/CSharpUseNullCheckOverTypeCheckDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
678. **`src/Analyzers/CSharp/Analyzers/UsePatternMatching/CSharpAsAndNullCheckDiagnosticAnalyzer.Analyzer.cs`** -> AI Confidence: **99.18%**
679. **`src/Analyzers/CSharp/Analyzers/UseSimpleUsingStatement/UseSimpleUsingStatementDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
680. **`src/Analyzers/CSharp/Analyzers/UseUnboundGenericTypeInNameOf/CSharpUseUnboundGenericTypeInNameOfDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
681. **`src/Analyzers/CSharp/CodeFixes/AssignOutParameters/AssignOutParametersAboveReturnCodeFixProvider.cs`** -> AI Confidence: **99.18%**
682. **`src/Analyzers/CSharp/CodeFixes/ConvertNamespace/ConvertNamespaceTransform.cs`** -> AI Confidence: **99.18%**
683. **`src/Analyzers/CSharp/CodeFixes/ConvertSwitchStatementToExpression/ConvertSwitchStatementToExpressionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
684. **`src/Analyzers/CSharp/CodeFixes/ConvertToRecord/PositionalParameterInfo.cs`** -> AI Confidence: **99.18%**
685. **`src/Analyzers/CSharp/CodeFixes/FixIncorrectConstraint/CSharpFixIncorrectConstraintCodeFixProvider.cs`** -> AI Confidence: **99.18%**
686. **`src/Analyzers/CSharp/CodeFixes/GenerateDefaultConstructors/CSharpGenerateDefaultConstructorsService.cs`** -> AI Confidence: **99.18%**
687. **`src/Analyzers/CSharp/CodeFixes/GenerateMethod/GenerateMethodCodeFixProvider.cs`** -> AI Confidence: **99.18%**
688. **`src/Analyzers/CSharp/CodeFixes/GenerateParameterizedMember/CSharpGenerateDeconstructMethodService.cs`** -> AI Confidence: **99.18%**
689. **`src/Analyzers/CSharp/CodeFixes/Iterator/CSharpAddYieldCodeFixProvider.cs`** -> AI Confidence: **99.18%**
690. **`src/Analyzers/CSharp/CodeFixes/MakeLocalFunctionStatic/MakeLocalFunctionStaticCodeFixHelper.cs`** -> AI Confidence: **99.18%**
691. **`src/Analyzers/CSharp/CodeFixes/MakeMemberRequired/CSharpMakeMemberRequiredCodeFixProvider.cs`** -> AI Confidence: **99.18%**
692. **`src/Analyzers/CSharp/CodeFixes/MakeMethodSynchronous/CSharpMakeMethodSynchronousCodeFixProvider.cs`** -> AI Confidence: **99.18%**
693. **`src/Analyzers/CSharp/CodeFixes/MakeStructFieldsWritable/CSharpMakeStructFieldsWritableCodeFixProvider.cs`** -> AI Confidence: **99.18%**
694. **`src/Analyzers/CSharp/CodeFixes/MakeStructMemberReadOnly/CSharpMakeStructMemberReadOnlyCodeFixProvider.cs`** -> AI Confidence: **99.18%**
695. **`src/Analyzers/CSharp/CodeFixes/QualifyMemberAccess/CSharpQualifyMemberAccessCodeFixProvider.cs`** -> AI Confidence: **99.18%**
696. **`src/Analyzers/CSharp/CodeFixes/RemoveUnnecessaryDiscardDesignation/CSharpRemoveUnnecessaryDiscardDesignationCodeFixProvider.cs`** -> AI Confidence: **99.18%**
697. **`src/Analyzers/CSharp/CodeFixes/RemoveUnnecessaryNullableDirective/CSharpRemoveUnnecessaryNullableDirectiveCodeFixProvider.cs`** -> AI Confidence: **99.18%**
698. **`src/Analyzers/CSharp/CodeFixes/SimplifyPropertyAccessor/CSharpSimplifyPropertyAccessorCodeFixProvider.cs`** -> AI Confidence: **99.18%**
699. **`src/Analyzers/CSharp/CodeFixes/TransposeRecordKeyword/CSharpTransposeRecordKeywordCodeFixProvider.cs`** -> AI Confidence: **99.18%**
700. **`src/Analyzers/CSharp/CodeFixes/UseAutoProperty/CSharpUseAutoPropertyCodeFixProvider.cs`** -> AI Confidence: **99.18%**
701. **`src/Analyzers/CSharp/CodeFixes/UseCollectionExpression/CSharpUseCollectionExpressionForArrayCodeFixProvider.cs`** -> AI Confidence: **99.18%**
702. **`src/Analyzers/CSharp/CodeFixes/UseCollectionInitializer/CSharpUseCollectionInitializerCodeFixProvider_CollectionInitializer.cs`** -> AI Confidence: **99.18%**
703. **`src/Analyzers/CSharp/CodeFixes/UseExplicitArrayInExpressionTree/CSharpUseExplicitArrayInExpressionTreeCodeFixProvider.cs`** -> AI Confidence: **99.18%**
704. **`src/Analyzers/CSharp/CodeFixes/UseIndexOrRangeOperator/CSharpUseRangeOperatorCodeFixProvider.cs`** -> AI Confidence: **99.18%**
705. **`src/Analyzers/CSharp/CodeFixes/UseLocalFunction/CSharpUseLocalFunctionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
706. **`src/Analyzers/CSharp/CodeFixes/UsePatternMatching/CSharpAsAndMemberAccessCodeFixProvider.cs`** -> AI Confidence: **99.18%**
707. **`src/Analyzers/CSharp/CodeFixes/UsePrimaryConstructor/CSharpUsePrimaryConstructorCodeFixProvider_DocComments.cs`** -> AI Confidence: **99.18%**
708. **`src/Analyzers/CSharp/CodeFixes/UsePrimaryConstructor/CSharpUsePrimaryConstructorFixAllProvider.cs`** -> AI Confidence: **99.18%**
709. **`src/Analyzers/CSharp/CodeFixes/UseSimpleUsingStatement/UseSimpleUsingStatementCodeFixProvider.cs`** -> AI Confidence: **99.18%**
710. **`src/Analyzers/CSharp/Tests/AssignOutParameters/AssignOutParametersAboveReturnTests.cs`** -> AI Confidence: **99.18%**
711. **`src/Analyzers/CSharp/Tests/Formatting/FormattingAnalyzerTests.cs`** -> AI Confidence: **99.18%**
712. **`src/Analyzers/CSharp/Tests/InlineDeclaration/CSharpInlineDeclarationTests.cs`** -> AI Confidence: **99.18%**
713. **`src/Analyzers/CSharp/Tests/MakeMemberRequired/MakeMemberRequiredTests.cs`** -> AI Confidence: **99.18%**
714. **`src/Analyzers/CSharp/Tests/NewLines/ConditionalExpressionPlacement/ConditionalExpressionPlacementTests.cs`** -> AI Confidence: **99.18%**
715. **`src/Analyzers/CSharp/Tests/NewLines/EmbeddedStatementPlacement/EmbeddedStatementPlacementTests.cs`** -> AI Confidence: **99.18%**
716. **`src/Analyzers/CSharp/Tests/RemoveUnnecessaryDiscardDesignation/RemoveUnnecessaryDiscardDesignationTests.cs`** -> AI Confidence: **99.18%**
717. **`src/Analyzers/CSharp/Tests/RemoveUnreachableCode/RemoveUnreachableCodeTests.cs`** -> AI Confidence: **99.18%**
718. **`src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValueAssignmentTests.cs`** -> AI Confidence: **99.18%**
719. **`src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValuesTestsBase.cs`** -> AI Confidence: **99.18%**
720. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForIfNullStatementCheckTests.cs`** -> AI Confidence: **99.18%**
721. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForNullableTernaryConditionalCheckTests.cs`** -> AI Confidence: **99.18%**
722. **`src/Analyzers/CSharp/Tests/UseCoalesceExpression/UseCoalesceExpressionForTernaryConditionalCheckTests.cs`** -> AI Confidence: **99.18%**
723. **`src/Analyzers/CSharp/Tests/UseDeconstruction/UseDeconstructionTests.cs`** -> AI Confidence: **99.18%**
724. **`src/Analyzers/CSharp/Tests/UseExplicitTupleName/UseExplicitTupleNameTests.cs`** -> AI Confidence: **99.18%**
725. **`src/Analyzers/CSharp/Tests/UseIsNullCheck/UseIsNullCheckForCastAndEqualityOperatorTests.cs`** -> AI Confidence: **99.18%**
726. **`src/Analyzers/CSharp/Tests/UseIsNullCheck/UseIsNullCheckForReferenceEqualsTests.cs`** -> AI Confidence: **99.18%**
727. **`src/Analyzers/CSharp/Tests/UseThrowExpression/UseThrowExpressionTests.cs`** -> AI Confidence: **99.18%**
728. **`src/Analyzers/Core/Analyzers/MakeFieldReadonly/AbstractMakeFieldReadonlyDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
729. **`src/Analyzers/Core/Analyzers/MatchFolderAndNamespace/AbstractMatchFolderAndNamespaceDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
730. **`src/Analyzers/Core/Analyzers/NamingStyle/NamingStyleDiagnosticAnalyzerBase.cs`** -> AI Confidence: **99.18%**
731. **`src/Analyzers/Core/Analyzers/RemoveUnnecessaryParentheses/AbstractRemoveUnnecessaryParenthesesDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
732. **`src/Analyzers/Core/Analyzers/RemoveUnusedParametersAndValues/AbstractRemoveUnusedParametersAndValuesDiagnosticAnalyzer.SymbolStartAnalyzer.cs`** -> AI Confidence: **99.18%**
733. **`src/Analyzers/Core/Analyzers/SimplifyTypeNames/SimplifyTypeNamesDiagnosticAnalyzerBase.cs`** -> AI Confidence: **99.18%**
734. **`src/Analyzers/Core/Analyzers/UseAutoProperty/AbstractUseAutoPropertyAnalyzer.cs`** -> AI Confidence: **99.18%**
735. **`src/Analyzers/Core/Analyzers/UseCollectionInitializer/AbstractUseCollectionInitializerDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
736. **`src/Analyzers/Core/Analyzers/UseConditionalExpression/UseConditionalExpressionHelpers.cs`** -> AI Confidence: **99.18%**
737. **`src/Analyzers/Core/Analyzers/UseObjectInitializer/AbstractUseObjectInitializerDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
738. **`src/Analyzers/Core/Analyzers/ValidateFormatString/AbstractValidateFormatStringDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
739. **`src/Analyzers/Core/CodeFixes/DocumentationComments/AbstractAddDocCommentNodesCodeFixProvider.cs`** -> AI Confidence: **99.18%**
740. **`src/Analyzers/Core/CodeFixes/DocumentationComments/AbstractRemoveDocCommentNodeCodeFixProvider.cs`** -> AI Confidence: **99.18%**
741. **`src/Analyzers/Core/CodeFixes/FileHeaders/AbstractFileHeaderCodeFixProvider.cs`** -> AI Confidence: **99.18%**
742. **`src/Analyzers/Core/CodeFixes/GenerateConstructor/AbstractGenerateConstructorService.cs`** -> AI Confidence: **99.18%**
743. **`src/Analyzers/Core/CodeFixes/GenerateDefaultConstructors/GenerateDefaultConstructorsCodeAction.cs`** -> AI Confidence: **99.18%**
744. **`src/Analyzers/Core/CodeFixes/GenerateEnumMember/AbstractGenerateEnumMemberService.State.cs`** -> AI Confidence: **99.18%**
745. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateMethodService.State.cs`** -> AI Confidence: **99.18%**
746. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateParameterizedMemberService.AbstractInvocationInfo.cs`** -> AI Confidence: **99.18%**
747. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/AbstractGenerateParameterizedMemberService.SignatureInfo.cs`** -> AI Confidence: **99.18%**
748. **`src/Analyzers/Core/CodeFixes/GenerateParameterizedMember/TypeParameterSubstitution.cs`** -> AI Confidence: **99.18%**
749. **`src/Analyzers/Core/CodeFixes/GenerateVariable/AbstractGenerateVariableService.State.cs`** -> AI Confidence: **99.18%**
750. **`src/Analyzers/Core/CodeFixes/RemoveAsyncModifier/AbstractRemoveAsyncModifierCodeFixProvider.cs`** -> AI Confidence: **99.18%**
751. **`src/Analyzers/Core/CodeFixes/RemoveUnnecessarySuppressions/RemoveUnnecessaryPragmaSuppressionsCodeFixProvider.cs`** -> AI Confidence: **99.18%**
752. **`src/Analyzers/Core/CodeFixes/RemoveUnusedMembers/AbstractRemoveUnusedMembersCodeFixProvider.cs`** -> AI Confidence: **99.18%**
753. **`src/Analyzers/Core/CodeFixes/SimplifyInterpolation/AbstractSimplifyInterpolationCodeFixProvider.cs`** -> AI Confidence: **99.18%**
754. **`src/Analyzers/Core/CodeFixes/SimplifyLinqExpression/SimplifyLinqExpressionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
755. **`src/Analyzers/Core/CodeFixes/UseConditionalExpression/ForReturn/AbstractUseConditionalExpressionForReturnCodeFixProvider.cs`** -> AI Confidence: **99.18%**
756. **`src/Compilers/CSharp/Portable/Binder/EmbeddedStatementBinder.cs`** -> AI Confidence: **99.18%**
757. **`src/Compilers/CSharp/Portable/Binder/FixedStatementBinder.cs`** -> AI Confidence: **99.18%**
758. **`src/Compilers/CSharp/Portable/Binder/WhileBinder.cs`** -> AI Confidence: **99.18%**
759. **`src/Compilers/CSharp/Portable/BoundTree/LengthBasedStringSwitchData.cs`** -> AI Confidence: **99.18%**
760. **`src/Compilers/CSharp/Portable/CommandLine/CSharpCompiler.cs`** -> AI Confidence: **99.18%**
761. **`src/Compilers/CSharp/Portable/Compiler/DocumentationCommentCompiler.IncludeElementExpander.cs`** -> AI Confidence: **99.18%**
762. **`src/Compilers/CSharp/Portable/Emitter/EditAndContinue/CSharpSymbolMatcher.cs`** -> AI Confidence: **99.18%**
763. **`src/Compilers/CSharp/Portable/Emitter/EditAndContinue/EmitHelpers.cs`** -> AI Confidence: **99.18%**
764. **`src/Compilers/CSharp/Portable/Emitter/Model/ExpandedVarargsMethodReference.cs`** -> AI Confidence: **99.18%**
765. **`src/Compilers/CSharp/Portable/Emitter/Model/PEAssemblyBuilder.cs`** -> AI Confidence: **99.18%**
766. **`src/Compilers/CSharp/Portable/FlowAnalysis/CSharpDataFlowAnalysis.cs`** -> AI Confidence: **99.18%**
767. **`src/Compilers/CSharp/Portable/FlowAnalysis/EntryPointsWalker.cs`** -> AI Confidence: **99.18%**
768. **`src/Compilers/CSharp/Portable/Lowering/AsyncRewriter/AsyncExceptionHandlerRewriter.cs`** -> AI Confidence: **99.18%**
769. **`src/Compilers/CSharp/Portable/Lowering/LocalRewriter/DelegateCacheRewriter.cs`** -> AI Confidence: **99.18%**
770. **`src/Compilers/CSharp/Portable/Lowering/StateMachineRewriter/SynthesizedStateMachineMethod.cs`** -> AI Confidence: **99.18%**
771. **`src/Compilers/CSharp/Portable/Symbols/AnonymousTypes/SynthesizedSymbols/AnonymousType.TemplateSymbol.cs`** -> AI Confidence: **99.18%**
772. **`src/Compilers/CSharp/Portable/Symbols/EventSymbol.cs`** -> AI Confidence: **99.18%**
773. **`src/Compilers/CSharp/Portable/Symbols/Extensions/SourceExtensionImplementationMethodSymbol.cs`** -> AI Confidence: **99.18%**
774. **`src/Compilers/CSharp/Portable/Symbols/LocalSymbol.cs`** -> AI Confidence: **99.18%**
775. **`src/Compilers/CSharp/Portable/Symbols/MergedNamespaceSymbol.cs`** -> AI Confidence: **99.18%**
776. **`src/Compilers/CSharp/Portable/Symbols/Metadata/PE/PEAssemblySymbol.cs`** -> AI Confidence: **99.18%**
777. **`src/Compilers/CSharp/Portable/Symbols/MetadataOrSourceOrRetargetingAssemblySymbol.cs`** -> AI Confidence: **99.18%**
778. **`src/Compilers/CSharp/Portable/Symbols/NamespaceSymbol.cs`** -> AI Confidence: **99.18%**
779. **`src/Compilers/CSharp/Portable/Symbols/NativeIntegerTypeSymbol.cs`** -> AI Confidence: **99.18%**
780. **`src/Compilers/CSharp/Portable/Symbols/PublicModel/MethodSymbol.cs`** -> AI Confidence: **99.18%**
781. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingModuleSymbol.cs`** -> AI Confidence: **99.18%**
782. **`src/Compilers/CSharp/Portable/Symbols/Retargeting/RetargetingNamedTypeSymbol.cs`** -> AI Confidence: **99.18%**
783. **`src/Compilers/CSharp/Portable/Symbols/Source/FieldSymbolWithAttributesAndModifiers.cs`** -> AI Confidence: **99.18%**
784. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceDelegateMethodSymbol.cs`** -> AI Confidence: **99.18%**
785. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceOrdinaryMethodSymbolBase.cs`** -> AI Confidence: **99.18%**
786. **`src/Compilers/CSharp/Portable/Symbols/Source/SourceTypeParameterSymbol.cs`** -> AI Confidence: **99.18%**
787. **`src/Compilers/CSharp/Portable/Symbols/SubstitutedNamedTypeSymbol.cs`** -> AI Confidence: **99.18%**
788. **`src/Compilers/CSharp/Portable/Symbols/SymbolExtensions.cs`** -> AI Confidence: **99.18%**
789. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedAccessorValueParameterSymbol.cs`** -> AI Confidence: **99.18%**
790. **`src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedEventAccessorSymbol.cs`** -> AI Confidence: **99.18%**
791. **`src/Compilers/CSharp/Portable/Symbols/UnboundGenericType.cs`** -> AI Confidence: **99.18%**
792. **`src/Compilers/CSharp/Portable/Syntax/CSharpSyntaxTree.LazySyntaxTree.cs`** -> AI Confidence: **99.18%**
793. **`src/Compilers/CSharp/Portable/Utilities/InterceptableLocation.cs`** -> AI Confidence: **99.18%**
794. **`src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs`** -> AI Confidence: **99.18%**
795. **`src/Compilers/CSharp/Test/Emit/BreakingChanges.cs`** -> AI Confidence: **99.18%**
796. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncIteratorTests.cs`** -> AI Confidence: **99.18%**
797. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs`** -> AI Confidence: **99.18%**
798. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenDynamicTests.cs`** -> AI Confidence: **99.18%**
799. **`src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenOperators.cs`** -> AI Confidence: **99.18%**
800. **`src/Compilers/CSharp/Test/Emit/CodeGen/ForeachTest.cs`** -> AI Confidence: **99.18%**
801. **`src/Compilers/CSharp/Test/Emit/CodeGen/PatternTests.cs`** -> AI Confidence: **99.18%**
802. **`src/Compilers/CSharp/Test/Emit/Emit/DynamicAnalysis/DynamicAnalysisResourceTests.cs`** -> AI Confidence: **99.18%**
803. **`src/Compilers/CSharp/Test/Emit/PrivateProtected.cs`** -> AI Confidence: **99.18%**
804. **`src/Compilers/CSharp/Test/Emit2/Emit/LocalStateTracing/LocalStateTracingTests.cs`** -> AI Confidence: **99.18%**
805. **`src/Compilers/CSharp/Test/Emit2/PDB/PDBTests.cs`** -> AI Confidence: **99.18%**
806. **`src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Security.cs`** -> AI Confidence: **99.18%**
807. **`src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Tuples.cs`** -> AI Confidence: **99.18%**
808. **`src/Compilers/CSharp/Test/Emit3/Diagnostics/DiagnosticAnalyzerTests.cs`** -> AI Confidence: **99.18%**
809. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowDiagnosticTests.cs`** -> AI Confidence: **99.18%**
810. **`src/Compilers/CSharp/Test/Emit3/FlowAnalysis/PatternsVsRegions.cs`** -> AI Confidence: **99.18%**
811. **`src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs`** -> AI Confidence: **99.18%**
812. **`src/Compilers/CSharp/Test/Emit3/RefUnsafeInIteratorAndAsyncTests.cs`** -> AI Confidence: **99.18%**
813. **`src/Compilers/CSharp/Test/Emit3/Semantics/PatternMatchingTests.cs`** -> AI Confidence: **99.18%**
814. **`src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs`** -> AI Confidence: **99.18%**
815. **`src/Compilers/CSharp/Test/IOperation/IOperation/IOperationTests_IInterpolatedStringOperation.cs`** -> AI Confidence: **99.18%**
816. **`src/Compilers/CSharp/Test/Semantic/Semantics/FuzzTests.cs`** -> AI Confidence: **99.18%**
817. **`src/Compilers/CSharp/Test/Semantic/Semantics/LocalFunctionTests.cs`** -> AI Confidence: **99.18%**
818. **`src/Compilers/CSharp/Test/Semantic/Semantics/LookupPositionTests.cs`** -> AI Confidence: **99.18%**
819. **`src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs`** -> AI Confidence: **99.18%**
820. **`src/Compilers/CSharp/Test/Semantic/Semantics/NullableTests.cs`** -> AI Confidence: **99.18%**
821. **`src/Compilers/CSharp/Test/Semantic/Semantics/SpanStackSafetyTests.cs`** -> AI Confidence: **99.18%**
822. **`src/Compilers/CSharp/Test/Semantic/SourceGeneration/GeneratorDriverFuzzTests.cs`** -> AI Confidence: **99.18%**
823. **`src/Compilers/CSharp/Test/Semantic/SourceGeneration/StateTableTests.cs`** -> AI Confidence: **99.18%**
824. **`src/Compilers/CSharp/Test/Symbol/Symbols/AnonymousTypesSemanticsTests.cs`** -> AI Confidence: **99.18%**
825. **`src/Compilers/CSharp/Test/Symbol/Symbols/CovariantReturnTests.cs`** -> AI Confidence: **99.18%**
826. **`src/Compilers/CSharp/Test/Symbol/Symbols/MockSymbolTests.cs`** -> AI Confidence: **99.18%**
827. **`src/Compilers/CSharp/Test/Symbol/Symbols/PartialPropertiesTests.cs`** -> AI Confidence: **99.18%**
828. **`src/Compilers/CSharp/Test/Symbol/Symbols/Source/DeclaringSyntaxNodeTests.cs`** -> AI Confidence: **99.18%**
829. **`src/Compilers/CSharp/Test/Syntax/LexicalAndXml/LexicalTests.cs`** -> AI Confidence: **99.18%**
830. **`src/Compilers/CSharp/Test/Syntax/Parsing/MemberDeclarationParsingTests.cs`** -> AI Confidence: **99.18%**
831. **`src/Compilers/CSharp/Test/Syntax/Parsing/ParserErrorMessageTests.cs`** -> AI Confidence: **99.18%**
832. **`src/Compilers/CSharp/Test/Syntax/Parsing/ParserRegressionTests.cs`** -> AI Confidence: **99.18%**
833. **`src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxListTests.cs`** -> AI Confidence: **99.18%**
834. **`src/Compilers/Core/CodeAnalysisTest/Collections/ImmutableListTestBase.cs`** -> AI Confidence: **99.18%**
835. **`src/Compilers/Core/CodeAnalysisTest/Collections/SmallDictionaryTests.cs`** -> AI Confidence: **99.18%**
836. **`src/Compilers/Core/CodeAnalysisTest/Diagnostics/SarifErrorLoggerTests.cs`** -> AI Confidence: **99.18%**
837. **`src/Compilers/Core/MSBuildTask/ManagedToolTask.cs`** -> AI Confidence: **99.18%**
838. **`src/Compilers/Core/MSBuildTask/ValidateBootstrap.cs`** -> AI Confidence: **99.18%**
839. **`src/Compilers/Core/MSBuildTaskTests/TestUtilities/DotNetSdkTestBase.cs`** -> AI Confidence: **99.18%**
840. **`src/Compilers/Core/Portable/Collections/ByteSequenceComparer.cs`** -> AI Confidence: **99.18%**
841. **`src/Compilers/Core/Portable/Collections/CachingDictionary.cs`** -> AI Confidence: **99.18%**
842. **`src/Compilers/Core/Portable/Collections/KeyedStack.cs`** -> AI Confidence: **99.18%**
843. **`src/Compilers/Core/Portable/Collections/UnionCollection.cs`** -> AI Confidence: **99.18%**
844. **`src/Compilers/Core/Portable/CommandLine/ReportAnalyzerUtil.cs`** -> AI Confidence: **99.18%**
845. **`src/Compilers/Core/Portable/Compilation/ParseOptions.cs`** -> AI Confidence: **99.18%**
846. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalysisScope.cs`** -> AI Confidence: **99.18%**
847. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/AnalyzerAssemblyLoader.Core.cs`** -> AI Confidence: **99.18%**
848. **`src/Compilers/Core/Portable/DiagnosticAnalyzer/DiagnosticStartAnalysisScope.cs`** -> AI Confidence: **99.18%**
849. **`src/Compilers/Core/Portable/EmbeddedText.cs`** -> AI Confidence: **99.18%**
850. **`src/Compilers/Core/Portable/MetadataReference/AssemblyIdentity.cs`** -> AI Confidence: **99.18%**
851. **`src/Compilers/Core/Portable/MetadataReference/MetadataReference.cs`** -> AI Confidence: **99.18%**
852. **`src/Compilers/Core/Portable/Operations/IOperation.OperationList.Reversed.cs`** -> AI Confidence: **99.18%**
853. **`src/Compilers/Core/Portable/PEWriter/CustomDebugInfoWriter.cs`** -> AI Confidence: **99.18%**
854. **`src/Compilers/Core/Portable/PEWriter/ManagedResource.cs`** -> AI Confidence: **99.18%**
855. **`src/Compilers/Core/Portable/PEWriter/Members.cs`** -> AI Confidence: **99.18%**
856. **`src/Compilers/Core/Portable/PEWriter/PooledBlobBuilder.cs`** -> AI Confidence: **99.18%**
857. **`src/Compilers/Core/Portable/PEWriter/SigningUtilities.cs`** -> AI Confidence: **99.18%**
858. **`src/Compilers/Core/Portable/SourceGeneration/GeneratorContexts.cs`** -> AI Confidence: **99.18%**
859. **`src/Compilers/Core/Portable/SourceGeneration/SyntaxStore.cs`** -> AI Confidence: **99.18%**
860. **`src/Compilers/Core/Rebuild/CompilationOptionsReader.cs`** -> AI Confidence: **99.18%**
861. **`src/Compilers/Core/RebuildTest/RebuildCommandLineTests.cs`** -> AI Confidence: **99.18%**
862. **`src/Compilers/Server/VBCSCompiler/MetadataCache.cs`** -> AI Confidence: **99.18%**
863. **`src/Compilers/Server/VBCSCompiler/NamedPipeClientConnection.cs`** -> AI Confidence: **99.18%**
864. **`src/Compilers/Server/VBCSCompilerTests/BuildServerConnectionTests.cs`** -> AI Confidence: **99.18%**
865. **`src/Compilers/Server/VBCSCompilerTests/NamedPipeTestUtil.cs`** -> AI Confidence: **99.18%**
866. **`src/Compilers/Server/VBCSCompilerTests/ServerUtil.cs`** -> AI Confidence: **99.18%**
867. **`src/Compilers/Shared/BuildClient.cs`** -> AI Confidence: **99.18%**
868. **`src/Compilers/Shared/BuildProtocol.cs`** -> AI Confidence: **99.18%**
869. **`src/Compilers/Shared/GlobalAssemblyCacheHelpers/GacFileResolver.cs`** -> AI Confidence: **99.18%**
870. **`src/Compilers/Test/Core/Compilation/CompilationDifference.cs`** -> AI Confidence: **99.18%**
871. **`src/Compilers/Test/Core/Compilation/CompilationTestDataExtensions.cs`** -> AI Confidence: **99.18%**
872. **`src/Compilers/Test/Core/Diagnostics/DiagnosticExtensions.cs`** -> AI Confidence: **99.18%**
873. **`src/Compilers/Test/Core/MarkedSource/SourceWithMarkedNodes.cs`** -> AI Confidence: **99.18%**
874. **`src/Compilers/Test/Core/Metadata/MetadataReaderUtils.cs`** -> AI Confidence: **99.18%**
875. **`src/Compilers/Test/Core/Metadata/MetadataValidation.cs`** -> AI Confidence: **99.18%**
876. **`src/Compilers/Test/Core/Platform/CoreClr/TestExecutionLoadContext.cs`** -> AI Confidence: **99.18%**
877. **`src/Compilers/Test/Core/TempFiles/TempFile.cs`** -> AI Confidence: **99.18%**
878. **`src/Compilers/Test/Core/TestHelpers.cs`** -> AI Confidence: **99.18%**
879. **`src/Compilers/Test/Core/TestableFile.cs`** -> AI Confidence: **99.18%**
880. **`src/Compilers/Test/Utilities/CSharp/CSharpTestSource.cs`** -> AI Confidence: **99.18%**
881. **`src/Compilers/Test/Utilities/CSharp/EmitMetadataTestBase.cs`** -> AI Confidence: **99.18%**
882. **`src/Compilers/Test/Utilities/CSharp/LifetimeAnnotationAttributesVisitor.cs`** -> AI Confidence: **99.18%**
883. **`src/Compilers/Test/Utilities/CSharp/SemanticModelTestBase.cs`** -> AI Confidence: **99.18%**
884. **`src/EditorFeatures/CSharp/BlockCommentEditing/CloseBlockCommentCommandHandler.cs`** -> AI Confidence: **99.18%**
885. **`src/EditorFeatures/CSharp/ConvertNamespace/ConvertNamespaceCommandHandler.cs`** -> AI Confidence: **99.18%**
886. **`src/EditorFeatures/CSharp/EventHookup/EventHookupCommandHandler_TabKeyCommand.cs`** -> AI Confidence: **99.18%**
887. **`src/EditorFeatures/CSharp/GoToBase/CSharpGoToBaseService.cs`** -> AI Confidence: **99.18%**
888. **`src/EditorFeatures/CSharp/Interactive/CSharpSendToInteractiveSubmissionProvider.cs`** -> AI Confidence: **99.18%**
889. **`src/EditorFeatures/CSharp/RawStringLiteral/RawStringLiteralCommandHandler_TypeChar.cs`** -> AI Confidence: **99.18%**
890. **`src/EditorFeatures/CSharp/StringCopyPaste/StringCopyPasteCommandHandler.cs`** -> AI Confidence: **99.18%**
891. **`src/EditorFeatures/CSharp/StringCopyPaste/StringInfo.cs`** -> AI Confidence: **99.18%**
892. **`src/EditorFeatures/CSharpTest/CodeActions/SyncNamespace/CSharpSyncNamespaceTestsBase.cs`** -> AI Confidence: **99.18%**
893. **`src/EditorFeatures/CSharpTest/Debugging/ProximityExpressionsGetterTests.cs`** -> AI Confidence: **99.18%**
894. **`src/EditorFeatures/CSharpTest/PdbSourceDocument/AbstractPdbSourceDocumentTests.cs`** -> AI Confidence: **99.18%**
895. **`src/EditorFeatures/CSharpTest/Structure/IfDirectiveTriviaStructureTests.cs`** -> AI Confidence: **99.18%**
896. **`src/EditorFeatures/Core/Adornments/AbstractAdornmentManager.cs`** -> AI Confidence: **99.18%**
897. **`src/EditorFeatures/Core/AutomaticCompletion/AbstractAutomaticLineEnderCommandHandler.cs`** -> AI Confidence: **99.18%**
898. **`src/EditorFeatures/Core/AutomaticCompletion/BraceCompletionSessionProvider.BraceCompletionSession.cs`** -> AI Confidence: **99.18%**
899. **`src/EditorFeatures/Core/ChangeSignature/AbstractChangeSignatureCommandHandler.cs`** -> AI Confidence: **99.18%**
900. **`src/EditorFeatures/Core/Classification/Semantic/AbstractSemanticOrEmbeddedClassificationViewTaggerProvider.cs`** -> AI Confidence: **99.18%**
901. **`src/EditorFeatures/Core/Classification/Syntactic/SyntacticClassificationTaggerProvider.ClassifiedLineCache.cs`** -> AI Confidence: **99.18%**
902. **`src/EditorFeatures/Core/CommentSelection/AbstractToggleBlockCommentBase.cs`** -> AI Confidence: **99.18%**
903. **`src/EditorFeatures/Core/CommentSelection/CommentUncommentSelectionCommandHandler.cs`** -> AI Confidence: **99.18%**
904. **`src/EditorFeatures/Core/Copilot/RoslynProposalAdjusterProvider.cs`** -> AI Confidence: **99.18%**
905. **`src/EditorFeatures/Core/DocumentationComments/AbstractDocumentationCommentCommandHandler.cs`** -> AI Confidence: **99.18%**
906. **`src/EditorFeatures/Core/DocumentationComments/CopilotGenerateDocumentationCommentManager.cs`** -> AI Confidence: **99.18%**
907. **`src/EditorFeatures/Core/EditAndContinue/PdbMatchingSourceTextProvider.cs`** -> AI Confidence: **99.18%**
908. **`src/EditorFeatures/Core/Editor/EditorLayerExtensionManager.cs`** -> AI Confidence: **99.18%**
909. **`src/EditorFeatures/Core/Editor/GoToAdjacentMemberCommandHandler.cs`** -> AI Confidence: **99.18%**
910. **`src/EditorFeatures/Core/EditorConfigSettings/DataProvider/SettingsProviderBase.cs`** -> AI Confidence: **99.18%**
911. **`src/EditorFeatures/Core/EditorConfigSettings/Updater/NamingStyles/NamingStyleSettingsUpdater.cs`** -> AI Confidence: **99.18%**
912. **`src/EditorFeatures/Core/ExternalAccess/IntelliCode/Api/IIntentSourceProvider.cs`** -> AI Confidence: **99.18%**
913. **`src/EditorFeatures/Core/FindUsages/BufferedFindUsagesContext.cs`** -> AI Confidence: **99.18%**
914. **`src/EditorFeatures/Core/Formatting/FormatCommandHandler.Paste.cs`** -> AI Confidence: **99.18%**
915. **`src/EditorFeatures/Core/Formatting/FormatCommandHandler.cs`** -> AI Confidence: **99.18%**
916. **`src/EditorFeatures/Core/IWpfDifferenceViewerExtensions.cs`** -> AI Confidence: **99.18%**
917. **`src/EditorFeatures/Core/InlineDiagnostics/InlineDiagnosticsTaggerProvider.cs`** -> AI Confidence: **99.18%**
918. **`src/EditorFeatures/Core/InlineHints/InlineHintDataTag.cs`** -> AI Confidence: **99.18%**
919. **`src/EditorFeatures/Core/InlineHints/InlineHintsKeyProcessorProvider.cs`** -> AI Confidence: **99.18%**
920. **`src/EditorFeatures/Core/InlineRename/CommandHandlers/AbstractRenameCommandHandler_RenameHandler.cs`** -> AI Confidence: **99.18%**
921. **`src/EditorFeatures/Core/InlineRename/InlineRenameSession.cs`** -> AI Confidence: **99.18%**
922. **`src/EditorFeatures/Core/InlineRename/UndoManagerServiceFactory.cs`** -> AI Confidence: **99.18%**
923. **`src/EditorFeatures/Core/IntelliSense/AsyncCompletion/CompletionSource.cs`** -> AI Confidence: **99.18%**
924. **`src/EditorFeatures/Core/Interactive/InertClassifierProvider.cs`** -> AI Confidence: **99.18%**
925. **`src/EditorFeatures/Core/Interactive/InteractivePasteCommandHandler.cs`** -> AI Confidence: **99.18%**
926. **`src/EditorFeatures/Core/Interactive/InteractiveSession.cs`** -> AI Confidence: **99.18%**
927. **`src/EditorFeatures/Core/NavigateTo/NavigateToItemProvider.cs`** -> AI Confidence: **99.18%**
928. **`src/EditorFeatures/Core/NavigationBar/NavigationBarController.cs`** -> AI Confidence: **99.18%**
929. **`src/EditorFeatures/Core/NavigationBar/NavigationBarController_ModelComputation.cs`** -> AI Confidence: **99.18%**
930. **`src/EditorFeatures/Core/Peek/PeekableItemFactory.cs`** -> AI Confidence: **99.18%**
931. **`src/EditorFeatures/Core/Peek/PeekableItemSource.cs`** -> AI Confidence: **99.18%**
932. **`src/EditorFeatures/Core/Preview/AbstractPreviewFactoryService.cs`** -> AI Confidence: **99.18%**
933. **`src/EditorFeatures/Core/Preview/DifferenceViewerPreview.cs`** -> AI Confidence: **99.18%**
934. **`src/EditorFeatures/Core/Preview/PreviewFactoryService.cs`** -> AI Confidence: **99.18%**
935. **`src/EditorFeatures/Core/QuickInfo/LazyToolTip.cs`** -> AI Confidence: **99.18%**
936. **`src/EditorFeatures/Core/QuickInfo/OnTheFlyDocsView.xaml.cs`** -> AI Confidence: **99.18%**
937. **`src/EditorFeatures/Core/ReferenceHighlighting/ReferenceHighlightingViewTaggerProvider.cs`** -> AI Confidence: **99.18%**
938. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.StateMachine.cs`** -> AI Confidence: **99.18%**
939. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.TrackingSession.cs`** -> AI Confidence: **99.18%**
940. **`src/EditorFeatures/Core/RenameTracking/RenameTrackingTaggerProvider.cs`** -> AI Confidence: **99.18%**
941. **`src/EditorFeatures/Core/Shared/Extensions/ITextViewExtensions.PerSubjectBufferProperty.cs`** -> AI Confidence: **99.18%**
942. **`src/EditorFeatures/Core/Shared/Extensions/ITextViewExtensions.cs`** -> AI Confidence: **99.18%**
943. **`src/EditorFeatures/Core/SignatureHelp/Controller.Session_UpdateModel.cs`** -> AI Confidence: **99.18%**
944. **`src/EditorFeatures/Core/SignatureHelp/Presentation/Signature.cs`** -> AI Confidence: **99.18%**
945. **`src/EditorFeatures/Core/SignatureHelp/Presentation/SignatureHelpClassifier.cs`** -> AI Confidence: **99.18%**
946. **`src/EditorFeatures/Core/SignatureHelp/Presentation/SignatureHelpPresenter.SignatureHelpPresenterSession.cs`** -> AI Confidence: **99.18%**
947. **`src/EditorFeatures/Core/SolutionEvents/HostLegacySolutionEventsWorkspaceEventListener.cs`** -> AI Confidence: **99.18%**
948. **`src/EditorFeatures/Core/StringIndentation/StringIndentationAdornmentManager.VisibleBlock.cs`** -> AI Confidence: **99.18%**
949. **`src/EditorFeatures/Core/StringIndentation/StringIndentationTag.cs`** -> AI Confidence: **99.18%**
950. **`src/EditorFeatures/Core/Structure/StructureTag.cs`** -> AI Confidence: **99.18%**
951. **`src/EditorFeatures/Core/Suggestions/SuggestedActionsSource.cs`** -> AI Confidence: **99.18%**
952. **`src/EditorFeatures/Core/Tagging/AbstractAsynchronousTaggerProvider.TagSource.cs`** -> AI Confidence: **99.18%**
953. **`src/EditorFeatures/Core/Undo/EditorSourceTextUndoService.cs`** -> AI Confidence: **99.18%**
954. **`src/EditorFeatures/Core/Workspaces/AbstractTextBufferVisibilityTracker.cs`** -> AI Confidence: **99.18%**
955. **`src/EditorFeatures/Test/CodeActions/CodeChangeProviderMetadataTests.cs`** -> AI Confidence: **99.18%**
956. **`src/EditorFeatures/Test/CodeGeneration/AbstractCodeGenerationTests.cs`** -> AI Confidence: **99.18%**
957. **`src/EditorFeatures/Test/Diagnostics/IDEDiagnosticIDConfigurationTests.cs`** -> AI Confidence: **99.18%**
958. **`src/EditorFeatures/Test/EmbeddedLanguages/StackFrame/StackFrameSyntaxFactory.cs`** -> AI Confidence: **99.18%**
959. **`src/EditorFeatures/Test/MetadataAsSource/DocCommentFormatterTests.cs`** -> AI Confidence: **99.18%**
960. **`src/EditorFeatures/Test/Utilities/BloomFilterTests.cs`** -> AI Confidence: **99.18%**
961. **`src/EditorFeatures/Test/ValueTracking/AbstractBaseValueTrackingTests.cs`** -> AI Confidence: **99.18%**
962. **`src/EditorFeatures/TestUtilities/AutomaticCompletion/AbstractAutomaticBraceCompletionTests.cs`** -> AI Confidence: **99.18%**
963. **`src/EditorFeatures/TestUtilities/ChangeSignature/TestChangeSignatureOptionsService.cs`** -> AI Confidence: **99.18%**
964. **`src/EditorFeatures/TestUtilities/Completion/AbstractCompletionProviderTests.cs`** -> AI Confidence: **99.18%**
965. **`src/EditorFeatures/TestUtilities/Diagnostics/DiagnosticTaggerWrapper.cs`** -> AI Confidence: **99.18%**
966. **`src/EditorFeatures/TestUtilities/SignatureHelp/AbstractSignatureHelpProviderTests.cs`** -> AI Confidence: **99.18%**
967. **`src/EditorFeatures/TestUtilities/Workspaces/EditorTestWorkspace.cs`** -> AI Confidence: **99.18%**
968. **`src/EditorFeatures/TestUtilities/Workspaces/TestWorkspaceFixture.cs`** -> AI Confidence: **99.18%**
969. **`src/EditorFeatures/Text/Extensions.SnapshotSourceText.cs`** -> AI Confidence: **99.18%**
970. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/Binders/PlaceholderLocalBinder.cs`** -> AI Confidence: **99.18%**
971. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/CSharpEESymbolProvider.cs`** -> AI Confidence: **99.18%**
972. **`src/ExpressionEvaluator/CSharp/Source/ExpressionCompiler/EEAssemblyBuilder.cs`** -> AI Confidence: **99.18%**
973. **`src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/ExpressionCompilerTestBase.cs`** -> AI Confidence: **99.18%**
974. **`src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/HoistedStateMachineLocalTests.cs`** -> AI Confidence: **99.18%**
975. **`src/ExpressionEvaluator/CSharp/Test/ResultProvider/CSharpResultProviderTestBase.cs`** -> AI Confidence: **99.18%**
976. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/EvaluationContextBase.cs`** -> AI Confidence: **99.18%**
977. **`src/ExpressionEvaluator/Core/Source/ExpressionCompiler/PseudoVariableUtilities.cs`** -> AI Confidence: **99.18%**
978. **`src/ExpressionEvaluator/Core/Source/FunctionResolver/FunctionResolver.cs`** -> AI Confidence: **99.18%**
979. **`src/ExpressionEvaluator/Core/Source/ResultProvider/Expansion/TupleExpansion.cs`** -> AI Confidence: **99.18%**
980. **`src/ExpressionEvaluator/Core/Test/ResultProvider/Debugger/Engine/DkmClrRuntimeInstance.cs`** -> AI Confidence: **99.18%**
981. **`src/Features/CSharp/Portable/BraceCompletion/StringLiteralBraceCompletionService.cs`** -> AI Confidence: **99.18%**
982. **`src/Features/CSharp/Portable/CodeRefactorings/ConvertLocalFunctionToMethod/CSharpConvertLocalFunctionToMethodCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
983. **`src/Features/CSharp/Portable/CodeRefactorings/EnableNullable/EnableNullableCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
984. **`src/Features/CSharp/Portable/CodeRefactorings/InlineTemporary/InlineTemporaryCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
985. **`src/Features/CSharp/Portable/CodeRefactorings/SyncNamespace/CSharpSyncNamespaceCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
986. **`src/Features/CSharp/Portable/CodeRefactorings/UseExplicitOrImplicitType/AbstractUseTypeCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
987. **`src/Features/CSharp/Portable/CodeRefactorings/UseRecursivePatterns/UseRecursivePatternsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
988. **`src/Features/CSharp/Portable/Completion/CompletionProviders/CompletionUtilities.cs`** -> AI Confidence: **99.18%**
989. **`src/Features/CSharp/Portable/Completion/CompletionProviders/CrefCompletionProvider.cs`** -> AI Confidence: **99.18%**
990. **`src/Features/CSharp/Portable/Completion/CompletionProviders/DeclarationName/DeclarationNameRecommender.NameGenerator.cs`** -> AI Confidence: **99.18%**
991. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ExplicitInterfaceMemberCompletionProvider.ItemGetter.cs`** -> AI Confidence: **99.18%**
992. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ExplicitInterfaceMemberCompletionProvider.cs`** -> AI Confidence: **99.18%**
993. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ExplicitInterfaceTypeCompletionProvider.cs`** -> AI Confidence: **99.18%**
994. **`src/Features/CSharp/Portable/Completion/CompletionProviders/FunctionPointerUnmanagedCallingConventionCompletionProvider.cs`** -> AI Confidence: **99.18%**
995. **`src/Features/CSharp/Portable/Completion/CompletionProviders/InternalsVisibleToCompletionProvider.cs`** -> AI Confidence: **99.18%**
996. **`src/Features/CSharp/Portable/Completion/CompletionProviders/NamedParameterCompletionProvider.cs`** -> AI Confidence: **99.18%**
997. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ObjectAndWithInitializerCompletionProvider.cs`** -> AI Confidence: **99.18%**
998. **`src/Features/CSharp/Portable/Completion/CompletionProviders/ObjectCreationCompletionProvider.cs`** -> AI Confidence: **99.18%**
999. **`src/Features/CSharp/Portable/Completion/CompletionProviders/PartialMethodCompletionProvider.cs`** -> AI Confidence: **99.18%**
1000. **`src/Features/CSharp/Portable/Completion/CompletionProviders/PropertySubPatternCompletionProvider.cs`** -> AI Confidence: **99.18%**
1001. **`src/Features/CSharp/Portable/Completion/CompletionProviders/SymbolCompletionProvider.cs`** -> AI Confidence: **99.18%**
1002. **`src/Features/CSharp/Portable/Completion/Providers/OutVariableArgumentProvider.cs`** -> AI Confidence: **99.18%**
1003. **`src/Features/CSharp/Portable/ConvertBetweenRegularAndVerbatimString/AbstractConvertBetweenRegularAndVerbatimStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1004. **`src/Features/CSharp/Portable/ConvertLinq/ConvertForEachToLinqQuery/AbstractConverter.cs`** -> AI Confidence: **99.18%**
1005. **`src/Features/CSharp/Portable/ConvertPrimaryToRegularConstructor/ConvertPrimaryToRegularConstructorCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1006. **`src/Features/CSharp/Portable/ConvertProgram/ConvertProgramTransform_ProgramMain.cs`** -> AI Confidence: **99.18%**
1007. **`src/Features/CSharp/Portable/ConvertToExtension/ConvertToExtensionCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1008. **`src/Features/CSharp/Portable/ConvertToRawString/ConvertInterpolatedStringToRawStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1009. **`src/Features/CSharp/Portable/ConvertToRawString/ConvertStringToRawStringCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1010. **`src/Features/CSharp/Portable/Copilot/CSharpCopilotCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1011. **`src/Features/CSharp/Portable/Debugging/BreakpointResolver.cs`** -> AI Confidence: **99.18%**
1012. **`src/Features/CSharp/Portable/EmbeddedLanguages/CSharpTestEmbeddedLanguageClassifier.cs`** -> AI Confidence: **99.18%**
1013. **`src/Features/CSharp/Portable/GenerateConstructors/CSharpGenerateConstructorsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1014. **`src/Features/CSharp/Portable/GenerateMember/GenerateVariable/CSharpGenerateVariableService.cs`** -> AI Confidence: **99.18%**
1015. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/AsyncAwaitHighlighter.cs`** -> AI Confidence: **99.18%**
1016. **`src/Features/CSharp/Portable/Highlighting/KeywordHighlighters/TryStatementHighlighter.cs`** -> AI Confidence: **99.18%**
1017. **`src/Features/CSharp/Portable/InitializeParameter/CSharpInitializeMemberFromPrimaryConstructorParameterCodeRefactoringProvider_Update.cs`** -> AI Confidence: **99.18%**
1018. **`src/Features/CSharp/Portable/InlineHints/CSharpInlineParameterNameHintsService.cs`** -> AI Confidence: **99.18%**
1019. **`src/Features/CSharp/Portable/InlineHints/CSharpInlineTypeHintsService.cs`** -> AI Confidence: **99.18%**
1020. **`src/Features/CSharp/Portable/IntroduceUsingStatement/CSharpIntroduceUsingStatementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1021. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService.cs`** -> AI Confidence: **99.18%**
1022. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService_IntroduceField.cs`** -> AI Confidence: **99.18%**
1023. **`src/Features/CSharp/Portable/IntroduceVariable/CSharpIntroduceVariableService_IntroduceLocal.cs`** -> AI Confidence: **99.18%**
1024. **`src/Features/CSharp/Portable/Options/CSharpEditorConfigOptionsEnumerator.cs`** -> AI Confidence: **99.18%**
1025. **`src/Features/CSharp/Portable/QuickInfo/CSharpDiagnosticAnalyzerQuickInfoProvider.cs`** -> AI Confidence: **99.18%**
1026. **`src/Features/CSharp/Portable/RawStringLiteral/CSharpRawStringLiteralOnAutoInsertService.cs`** -> AI Confidence: **99.18%**
1027. **`src/Features/CSharp/Portable/ReplaceMethodWithProperty/CSharpReplaceMethodWithPropertyService.cs`** -> AI Confidence: **99.18%**
1028. **`src/Features/CSharp/Portable/ReplacePropertyWithMethods/CSharpReplacePropertyWithMethodsService.cs`** -> AI Confidence: **99.18%**
1029. **`src/Features/CSharp/Portable/ReverseForStatement/CSharpReverseForStatementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1030. **`src/Features/CSharp/Portable/SignatureHelp/ElementAccessExpressionSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1031. **`src/Features/CSharp/Portable/SignatureHelp/InvocationExpressionSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1032. **`src/Features/CSharp/Portable/SignatureHelp/TupleConstructionSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1033. **`src/Features/CSharp/Portable/Snippets/CSharpSnippetFunctionService.cs`** -> AI Confidence: **99.18%**
1034. **`src/Features/CSharp/Portable/SplitOrMergeIfStatements/CSharpMergeConsecutiveIfStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1035. **`src/Features/CSharp/Portable/SplitOrMergeIfStatements/CSharpMergeNestedIfStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1036. **`src/Features/CSharp/Portable/SplitStringLiteral/InterpolatedStringSplitter.cs`** -> AI Confidence: **99.18%**
1037. **`src/Features/CSharp/Portable/UsePatternMatching/CSharpIsAndCastCheckWithoutNameDiagnosticAnalyzer.cs`** -> AI Confidence: **99.18%**
1038. **`src/Features/CSharpTest/ConvertForToForEach/ConvertForToForEachTests.cs`** -> AI Confidence: **99.18%**
1039. **`src/Features/CSharpTest/ConvertProgram/ConvertToTopLevelStatementsRefactoringTests.cs`** -> AI Confidence: **99.18%**
1040. **`src/Features/CSharpTest/Copilot/CSharpImplementNotImplementedExceptionDiagnosticAnalyzerTests.cs`** -> AI Confidence: **99.18%**
1041. **`src/Features/CSharpTest/Copilot/CSharpImplementNotImplementedExceptionFixProviderTests.cs`** -> AI Confidence: **99.18%**
1042. **`src/Features/CSharpTest/ExtractMethod/ExtractMethodCodeRefactoringTests.cs`** -> AI Confidence: **99.18%**
1043. **`src/Features/CSharpTest/InvertConditional/InvertConditionalTests.cs`** -> AI Confidence: **99.18%**
1044. **`src/Features/CSharpTest/SimplifyPropertyPattern/SimplifyPropertyPatternTests.cs`** -> AI Confidence: **99.18%**
1045. **`src/Features/Core/Portable/AddDebuggerDisplay/AbstractAddDebuggerDisplayCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1046. **`src/Features/Core/Portable/AddImport/AbstractAddImportCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1047. **`src/Features/Core/Portable/AddImport/AbstractAddImportFeatureService.cs`** -> AI Confidence: **99.18%**
1048. **`src/Features/Core/Portable/AddImport/References/ProjectSymbolReference.cs`** -> AI Confidence: **99.18%**
1049. **`src/Features/Core/Portable/AddImport/SymbolReferenceFinder.cs`** -> AI Confidence: **99.18%**
1050. **`src/Features/Core/Portable/AddPackage/InstallPackageDirectlyCodeActionOperation.cs`** -> AI Confidence: **99.18%**
1051. **`src/Features/Core/Portable/AddPackage/ParentInstallPackageCodeAction.cs`** -> AI Confidence: **99.18%**
1052. **`src/Features/Core/Portable/BraceCompletion/AbstractBraceCompletionService.cs`** -> AI Confidence: **99.18%**
1053. **`src/Features/Core/Portable/ChangeSignature/DelegateInvokeMethodReferenceFinder.cs`** -> AI Confidence: **99.18%**
1054. **`src/Features/Core/Portable/CodeFixes/Configuration/ConfigurationUpdater.cs`** -> AI Confidence: **99.18%**
1055. **`src/Features/Core/Portable/CodeFixes/Configuration/ConfigureCodeStyle/ConfigureCodeStyleOptionCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1056. **`src/Features/Core/Portable/CodeFixes/Service/CodeFixService.cs`** -> AI Confidence: **99.18%**
1057. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.AbstractGlobalSuppressMessageCodeAction.cs`** -> AI Confidence: **99.18%**
1058. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.RemoveSuppressionCodeAction.BatchFixer.cs`** -> AI Confidence: **99.18%**
1059. **`src/Features/Core/Portable/CodeFixes/Suppression/AbstractSuppressionCodeFixProvider.RemoveSuppressionCodeAction_Pragma.cs`** -> AI Confidence: **99.18%**
1060. **`src/Features/Core/Portable/CodeFixesAndRefactorings/AbstractFixAllGetFixesService.cs`** -> AI Confidence: **99.18%**
1061. **`src/Features/Core/Portable/CodeLens/CodeLensFindReferenceProgress.cs`** -> AI Confidence: **99.18%**
1062. **`src/Features/Core/Portable/CodeRefactorings/AddAwait/AbstractAddAwaitCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1063. **`src/Features/Core/Portable/CodeRefactorings/MoveType/AbstractMoveTypeService.MoveTypeNamespaceScopeEditor.cs`** -> AI Confidence: **99.18%**
1064. **`src/Features/Core/Portable/CodeRefactorings/MoveType/AbstractMoveTypeService.cs`** -> AI Confidence: **99.18%**
1065. **`src/Features/Core/Portable/CodeRefactorings/SyncNamespace/AbstractSyncNamespaceCodeRefactoringProvider.State.cs`** -> AI Confidence: **99.18%**
1066. **`src/Features/Core/Portable/Common/TaggedText.cs`** -> AI Confidence: **99.18%**
1067. **`src/Features/Core/Portable/Completion/CommonCompletionProvider.cs`** -> AI Confidence: **99.18%**
1068. **`src/Features/Core/Portable/Completion/CommonCompletionUtilities.cs`** -> AI Confidence: **99.18%**
1069. **`src/Features/Core/Portable/Completion/CompletionService.ProviderManager.cs`** -> AI Confidence: **99.18%**
1070. **`src/Features/Core/Portable/Completion/CompletionService_GetCompletions.cs`** -> AI Confidence: **99.18%**
1071. **`src/Features/Core/Portable/Completion/Providers/AbstractAggregateEmbeddedLanguageCompletionProvider.cs`** -> AI Confidence: **99.18%**
1072. **`src/Features/Core/Portable/Completion/Providers/AbstractInternalsVisibleToCompletionProvider.cs`** -> AI Confidence: **99.18%**
1073. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/AbstractTypeImportCompletionProvider.cs`** -> AI Confidence: **99.18%**
1074. **`src/Features/Core/Portable/Completion/Providers/ImportCompletionProvider/ImportCompletionItem.cs`** -> AI Confidence: **99.18%**
1075. **`src/Features/Core/Portable/ConvertAnonymousType/AbstractConvertAnonymousTypeToClassCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1076. **`src/Features/Core/Portable/ConvertAnonymousType/AbstractConvertAnonymousTypeToTupleCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1077. **`src/Features/Core/Portable/ConvertForEachToFor/AbstractConvertForEachToForCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1078. **`src/Features/Core/Portable/ConvertNumericLiteral/AbstractConvertNumericLiteralCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1079. **`src/Features/Core/Portable/ConvertToInterpolatedString/AbstractConvertConcatenationToInterpolatedStringRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1080. **`src/Features/Core/Portable/ConvertToInterpolatedString/AbstractConvertPlaceholderToInterpolatedStringRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1081. **`src/Features/Core/Portable/Debugging/AbstractBreakpointResolver.cs`** -> AI Confidence: **99.18%**
1082. **`src/Features/Core/Portable/Debugging/DebugInformationReaderProvider.cs`** -> AI Confidence: **99.18%**
1083. **`src/Features/Core/Portable/DesignerAttribute/DesignerAttributeDiscoveryService.cs`** -> AI Confidence: **99.18%**
1084. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService.HostAnalyzerInfo.cs`** -> AI Confidence: **99.18%**
1085. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_ComputeDiagnosticAnalysisResults.cs`** -> AI Confidence: **99.18%**
1086. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_CoreAnalyze.cs`** -> AI Confidence: **99.18%**
1087. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_GetDiagnosticsForSpan.cs`** -> AI Confidence: **99.18%**
1088. **`src/Features/Core/Portable/Diagnostics/Service/DiagnosticAnalyzerService_RemoteOrLocalDispatcher.cs`** -> AI Confidence: **99.18%**
1089. **`src/Features/Core/Portable/Diagnostics/Service/DocumentAnalysisExecutor.cs`** -> AI Confidence: **99.18%**
1090. **`src/Features/Core/Portable/Diagnostics/Service/DocumentAnalysisExecutor_Helpers.cs`** -> AI Confidence: **99.18%**
1091. **`src/Features/Core/Portable/DocumentationComments/AbstractDocumentationCommentSnippetService.cs`** -> AI Confidence: **99.18%**
1092. **`src/Features/Core/Portable/EditAndContinue/ActiveStatementsMap.cs`** -> AI Confidence: **99.18%**
1093. **`src/Features/Core/Portable/EditAndContinue/DebuggingSession.cs`** -> AI Confidence: **99.18%**
1094. **`src/Features/Core/Portable/EditAndContinue/DeclarationBody.cs`** -> AI Confidence: **99.18%**
1095. **`src/Features/Core/Portable/EditAndContinue/EditAndContinueDocumentAnalysesCache.cs`** -> AI Confidence: **99.18%**
1096. **`src/Features/Core/Portable/EditAndContinue/EmitSolutionUpdateResults.cs`** -> AI Confidence: **99.18%**
1097. **`src/Features/Core/Portable/EditAndContinue/Remote/RemoteDebuggingSessionProxy.cs`** -> AI Confidence: **99.18%**
1098. **`src/Features/Core/Portable/EditAndContinue/Remote/RemoteEditAndContinueServiceProxy.cs`** -> AI Confidence: **99.18%**
1099. **`src/Features/Core/Portable/EditAndContinue/Utilities/Extensions.cs`** -> AI Confidence: **99.18%**
1100. **`src/Features/Core/Portable/EmbeddedLanguages/Json/LanguageServices/AbstractJsonDetectionAnalyzer.cs`** -> AI Confidence: **99.18%**
1101. **`src/Features/Core/Portable/EmbeddedLanguages/RegularExpressions/LanguageServices/RegexClassifier.cs`** -> AI Confidence: **99.18%**
1102. **`src/Features/Core/Portable/EmbeddedLanguages/StackFrame/StackFrameLexer.cs`** -> AI Confidence: **99.18%**
1103. **`src/Features/Core/Portable/Extensions/ExtensionFolder.cs`** -> AI Confidence: **99.18%**
1104. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/API/UnitTestingHotReloadService.cs`** -> AI Confidence: **99.18%**
1105. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/Notification/AbstractGlobalOperationNotificationService.cs`** -> AI Confidence: **99.18%**
1106. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.AbstractUnitTestingPriorityProcessor.cs`** -> AI Confidence: **99.18%**
1107. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingAsyncWorkItemQueue.cs`** -> AI Confidence: **99.18%**
1108. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingLowPriorityProcessor.cs`** -> AI Confidence: **99.18%**
1109. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingSemanticChangeProcessor.cs`** -> AI Confidence: **99.18%**
1110. **`src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingWorkCoordinator.UnitTestingWorkItem.cs`** -> AI Confidence: **99.18%**
1111. **`src/Features/Core/Portable/ExtractInterface/AbstractExtractInterfaceService.cs`** -> AI Confidence: **99.18%**
1112. **`src/Features/Core/Portable/ExtractMethod/MethodExtractor.CodeGenerator.cs`** -> AI Confidence: **99.18%**
1113. **`src/Features/Core/Portable/ExtractMethod/MethodExtractor.cs`** -> AI Confidence: **99.18%**
1114. **`src/Features/Core/Portable/ExtractMethod/SelectionResult.cs`** -> AI Confidence: **99.18%**
1115. **`src/Features/Core/Portable/FindUsages/AbstractFindUsagesService_FindImplementations.cs`** -> AI Confidence: **99.18%**
1116. **`src/Features/Core/Portable/FindUsages/DefinitionItem.DefaultDefinitionItem.cs`** -> AI Confidence: **99.18%**
1117. **`src/Features/Core/Portable/Formatting/AbstractNewDocumentFormattingService.cs`** -> AI Confidence: **99.18%**
1118. **`src/Features/Core/Portable/GenerateComparisonOperators/GenerateComparisonOperatorsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1119. **`src/Features/Core/Portable/GenerateEqualsAndGetHashCodeFromMembers/GenerateEqualsAndHashWithDialogCodeAction.cs`** -> AI Confidence: **99.18%**
1120. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.CodeAction.cs`** -> AI Confidence: **99.18%**
1121. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.GenerateNamedType.cs`** -> AI Confidence: **99.18%**
1122. **`src/Features/Core/Portable/GenerateType/AbstractGenerateTypeService.cs`** -> AI Confidence: **99.18%**
1123. **`src/Features/Core/Portable/GoToBase/AbstractGoToBaseService.cs`** -> AI Confidence: **99.18%**
1124. **`src/Features/Core/Portable/GoToDefinition/AbstractGoToDefinitionSymbolService.cs`** -> AI Confidence: **99.18%**
1125. **`src/Features/Core/Portable/InheritanceMargin/AbstractInheritanceMarginService_Helpers.cs`** -> AI Confidence: **99.18%**
1126. **`src/Features/Core/Portable/InitializeParameter/AbstractInitializeMemberFromParameterCodeRefactoringProviderMemberCreation.cs`** -> AI Confidence: **99.18%**
1127. **`src/Features/Core/Portable/InitializeParameter/AbstractInitializeParameterCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1128. **`src/Features/Core/Portable/InlineHints/AbstractInlineParameterNameHintsService.cs`** -> AI Confidence: **99.18%**
1129. **`src/Features/Core/Portable/IntroduceParameter/IntroduceParameterDocumentRewriter.cs`** -> AI Confidence: **99.18%**
1130. **`src/Features/Core/Portable/IntroduceUsingStatement/AbstractIntroduceUsingStatementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1131. **`src/Features/Core/Portable/IntroduceVariable/AbstractIntroduceVariableService.IntroduceVariableCodeAction.cs`** -> AI Confidence: **99.18%**
1132. **`src/Features/Core/Portable/InvertIf/AbstractInvertIfCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1133. **`src/Features/Core/Portable/InvertLogical/AbstractInvertLogicalCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1134. **`src/Features/Core/Portable/NameTupleElement/AbstractNameTupleElementCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1135. **`src/Features/Core/Portable/NavigateTo/AbstractNavigateToSearchService.cs`** -> AI Confidence: **99.18%**
1136. **`src/Features/Core/Portable/NavigateTo/IRemoteNavigateToSearchService.cs`** -> AI Confidence: **99.18%**
1137. **`src/Features/Core/Portable/NavigateTo/NavigateToSearcher.cs`** -> AI Confidence: **99.18%**
1138. **`src/Features/Core/Portable/NavigateTo/RoslynNavigateToItem.cs`** -> AI Confidence: **99.18%**
1139. **`src/Features/Core/Portable/Navigation/IDefinitionLocationService.cs`** -> AI Confidence: **99.18%**
1140. **`src/Features/Core/Portable/Options/EditorConfig/EditorConfigOptionsEnumerator.cs`** -> AI Confidence: **99.18%**
1141. **`src/Features/Core/Portable/PdbSourceDocument/ImplementationAssemblyLookupService.cs`** -> AI Confidence: **99.18%**
1142. **`src/Features/Core/Portable/PdbSourceDocument/PdbSourceDocumentMetadataAsSourceFileProvider.cs`** -> AI Confidence: **99.18%**
1143. **`src/Features/Core/Portable/PullMemberUp/MembersPuller.cs`** -> AI Confidence: **99.18%**
1144. **`src/Features/Core/Portable/QuickInfo/CommonSemanticQuickInfoProvider.cs`** -> AI Confidence: **99.18%**
1145. **`src/Features/Core/Portable/ReplaceConditionalWithStatements/AbstractReplaceConditionalWithStatementsCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1146. **`src/Features/Core/Portable/ReplaceDocCommentTextWithTag/AbstractReplaceDocCommentTextWithTagCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1147. **`src/Features/Core/Portable/ReplaceMethodWithProperty/ReplaceMethodWithPropertyCodeRefactoringProvider.cs`** -> AI Confidence: **99.18%**
1148. **`src/Features/Core/Portable/ReplacePropertyWithMethods/AbstractReplacePropertyWithMethodsService.cs`** -> AI Confidence: **99.18%**
1149. **`src/Features/Core/Portable/SemanticSearch/IRemoteSemanticSearchService.cs`** -> AI Confidence: **99.18%**
1150. **`src/Features/Core/Portable/SignatureHelp/AbstractSignatureHelpProvider.cs`** -> AI Confidence: **99.18%**
1151. **`src/Features/Core/Portable/SpellCheck/AbstractSpellCheckCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1152. **`src/Features/Core/Portable/StackTraceExplorer/StackTraceAnalyzer.cs`** -> AI Confidence: **99.18%**
1153. **`src/Features/Core/Portable/StackTraceExplorer/StackTraceExplorerService.cs`** -> AI Confidence: **99.18%**
1154. **`src/Features/Core/Portable/StackTraceExplorer/StackTraceExplorerUtilities.cs`** -> AI Confidence: **99.18%**
1155. **`src/Features/Core/Portable/SymbolSearch/Windows/SymbolSearchUpdateEngine.Update.cs`** -> AI Confidence: **99.18%**
1156. **`src/Features/Core/Portable/SymbolSearch/Windows/SymbolSearchUpdateEngine.cs`** -> AI Confidence: **99.18%**
1157. **`src/Features/Core/Portable/TaskList/AbstractTaskListService.cs`** -> AI Confidence: **99.18%**
1158. **`src/Features/Core/Portable/Wrapping/BinaryExpression/AbstractBinaryExpressionWrapper.cs`** -> AI Confidence: **99.18%**
1159. **`src/Features/Core/Portable/Wrapping/ChainedExpression/AbstractChainedExpressionWrapper.cs`** -> AI Confidence: **99.18%**
1160. **`src/Features/DiagnosticsTestUtilities/CodeActionsLegacy/AbstractCodeActionOrUserDiagnosticTest_NoEditor.cs`** -> AI Confidence: **99.18%**
1161. **`src/Features/DiagnosticsTestUtilities/Diagnostics/AbstractUserDiagnosticTest_GenerateTypeDialog.cs`** -> AI Confidence: **99.18%**
1162. **`src/Features/DiagnosticsTestUtilities/NamingStyles/NamingStylesTestOptionSets.cs`** -> AI Confidence: **99.18%**
1163. **`src/Features/ExternalAccess/Copilot/Internal/Analyzer/AbstractCopilotCodeAnalysisService.cs`** -> AI Confidence: **99.18%**
1164. **`src/Features/ExternalAccess/HotReload/Api/HotReloadMSBuildWorkspace.cs`** -> AI Confidence: **99.18%**
1165. **`src/Features/Test/EditAndContinue/RudeEditDiagnosticTests.cs`** -> AI Confidence: **99.18%**
1166. **`src/Interactive/HostTest/AbstractInteractiveHostTests.cs`** -> AI Confidence: **99.18%**
1167. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer.UnitTests/Utilities/AbstractLanguageServerClientTests.TestLspClient.cs`** -> AI Confidence: **99.18%**
1168. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/FileBasedPrograms/FileBasedProgramsProjectSystem.cs`** -> AI Confidence: **99.18%**
1169. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LanguageServerProjectLoader.cs`** -> AI Confidence: **99.18%**
1170. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/Program.cs`** -> AI Confidence: **99.18%**
1171. **`src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/Testing/TestRunner.TestRunHandler.cs`** -> AI Confidence: **99.18%**
1172. **`src/LanguageServer/Microsoft.CommonLanguageServerProtocol.Framework/RequestExecutionQueue.cs`** -> AI Confidence: **99.18%**
1173. **`src/LanguageServer/Protocol/Extensions/Extensions.cs`** -> AI Confidence: **99.18%**
1174. **`src/LanguageServer/Protocol/Extensions/ProtocolConversions.Diagnostics.cs`** -> AI Confidence: **99.18%**
1175. **`src/LanguageServer/Protocol/Features/DecompiledSource/CSharpCodeDecompilerDecompilationService.cs`** -> AI Confidence: **99.18%**
1176. **`src/LanguageServer/Protocol/Features/Suggestions/UnifiedSuggestedActionsSource.cs`** -> AI Confidence: **99.18%**
1177. **`src/LanguageServer/Protocol/Handler/CodeActions/CodeActionHelpers.cs`** -> AI Confidence: **99.18%**
1178. **`src/LanguageServer/Protocol/Handler/CodeActions/CodeActionResolveHelper.cs`** -> AI Confidence: **99.18%**
1179. **`src/LanguageServer/Protocol/Handler/Configuration/DidChangeConfigurationNotificationHandler.cs`** -> AI Confidence: **99.18%**
1180. **`src/LanguageServer/Protocol/Handler/Diagnostics/AbstractWorkspacePullDiagnosticsHandler.cs`** -> AI Confidence: **99.18%**
1181. **`src/LanguageServer/Protocol/Handler/Diagnostics/DiagnosticsPullCache.cs`** -> AI Confidence: **99.18%**
1182. **`src/LanguageServer/Protocol/Handler/FoldingRanges/FoldingRangesHandler.cs`** -> AI Confidence: **99.18%**
1183. **`src/LanguageServer/Protocol/Handler/InlineCompletions/XmlSnippetParser.ParsedXmlSnippet.cs`** -> AI Confidence: **99.18%**
1184. **`src/LanguageServer/Protocol/Handler/MapCode/MapCodeHandler.cs`** -> AI Confidence: **99.18%**
1185. **`src/LanguageServer/Protocol/Handler/References/FindUsagesLSPContext.cs`** -> AI Confidence: **99.18%**
1186. **`src/LanguageServer/Protocol/Handler/SemanticTokens/SemanticTokensHelpers.cs`** -> AI Confidence: **99.18%**
1187. **`src/LanguageServer/Protocol/Handler/SpellCheck/AbstractSpellCheckingHandler.cs`** -> AI Confidence: **99.18%**
1188. **`src/LanguageServer/Protocol/Handler/SpellCheck/WorkspaceSpellCheckHandler.cs`** -> AI Confidence: **99.18%**
1189. **`src/LanguageServer/Protocol/Protocol/Converters/StringEnumConverter.cs`** -> AI Confidence: **99.18%**
1190. **`src/LanguageServer/Protocol/RoslynLanguageServer.cs`** -> AI Confidence: **99.18%**
1191. **`src/LanguageServer/ProtocolUnitTests/Diagnostics/AbstractPullDiagnosticTestsBase.cs`** -> AI Confidence: **99.18%**
1192. **`src/LanguageServer/ProtocolUnitTests/InlineCompletions/InlineCompletionsTests.cs`** -> AI Confidence: **99.18%**
1193. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/CSharp/MetaAnalyzers/Fixers/CSharpConfigureGeneratedCodeAnalysisFix.cs`** -> AI Confidence: **99.18%**
1194. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/CSharp/MetaAnalyzers/Fixers/CSharpEnableConcurrentExecutionFix.cs`** -> AI Confidence: **99.18%**
1195. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/ImmutableObjectMethodAnalyzer.cs`** -> AI Confidence: **99.18%**
1196. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/ImplementationIsObsoleteAnalyzer.cs`** -> AI Confidence: **99.18%**
1197. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/InternalImplementationOnlyAnalyzer.cs`** -> AI Confidence: **99.18%**
1198. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticDescriptorCreationAnalyzer_ResourceStringsFormat.cs`** -> AI Confidence: **99.18%**
1199. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/Fixers/CompareSymbolsCorrectlyFix.cs`** -> AI Confidence: **99.18%**
1200. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/Fixers/DefineDiagnosticDescriptorArgumentsCorrectlyFix.CustomFixAllProvider.cs`** -> AI Confidence: **99.18%**
1201. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/UnitTests/UseReturnValueFromImmutableObjectMethodTests.cs`** -> AI Confidence: **99.18%**
1202. **`src/RoslynAnalyzers/Microsoft.CodeAnalysis.BannedApiAnalyzers/Core/SymbolIsBannedAnalyzer.cs`** -> AI Confidence: **99.18%**
1203. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/CSharp/CodeFixes/AvoidAllocationWithArrayEmptyCodeFix.cs`** -> AI Confidence: **99.18%**
1204. **`src/RoslynAnalyzers/PerformanceSensitiveAnalyzers/UnitTests/EnumeratorAllocationAnalyzerTests.cs`** -> AI Confidence: **99.18%**
1205. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/CSharpDoNotCapturePrimaryContructorParameters.cs`** -> AI Confidence: **99.18%**
1206. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/CSharp/CSharpDoNotUseDebugAssertForInterpolatedStrings.cs`** -> AI Confidence: **99.18%**
1207. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/ImportingConstructorShouldBeObsoleteCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1208. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/RelaxTestNamingSuppressor.cs`** -> AI Confidence: **99.18%**
1209. **`src/RoslynAnalyzers/Roslyn.Diagnostics.Analyzers/Core/TestExportsShouldNotBeDiscoverableCodeFixProvider.cs`** -> AI Confidence: **99.18%**
1210. **`src/RoslynAnalyzers/Utilities.UnitTests/FlowAnalysis/Analysis/PropertySetAnalysis/PropertySetAnalysisTests.cs`** -> AI Confidence: **99.18%**
1211. **`src/RoslynAnalyzers/Utilities/Compiler/CodeMetrics/CodeAnalysisMetricData.AssemblyMetricData.cs`** -> AI Confidence: **99.18%**
1212. **`src/RoslynAnalyzers/Utilities/Compiler/DoNotCatchGeneralUnlessRethrown.cs`** -> AI Confidence: **99.18%**
1213. **`src/RoslynAnalyzers/Utilities/Compiler/Extensions/DiagnosticExtensions.cs`** -> AI Confidence: **99.18%**
1214. **`src/RoslynAnalyzers/Utilities/Compiler/Options/AggregateCategorizedAnalyzerConfigOptions.cs`** -> AI Confidence: **99.18%**
1215. **`src/RoslynAnalyzers/Utilities/Compiler/Options/AnalyzerOptionsExtensions.cs`** -> AI Confidence: **99.18%**
1216. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/DisposeAnalysis/DisposeAnalysisHelper.cs`** -> AI Confidence: **99.18%**
1217. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/GlobalFlowStateAnalysis/GlobalFlowStateAnalysisValueSet.cs`** -> AI Confidence: **99.18%**
1218. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PropertySetAnalysis/HazardousUsageEvaluatorCollection.cs`** -> AI Confidence: **99.18%**
1219. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AbstractDataFlowAnalysisContext.cs`** -> AI Confidence: **99.18%**
1220. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/AnalysisEntity.cs`** -> AI Confidence: **99.18%**
1221. **`src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/ThrownExceptionInfo.cs`** -> AI Confidence: **99.18%**
1222. **`src/Scripting/Core/ScriptBuilder.cs`** -> AI Confidence: **99.18%**
1223. **`src/Scripting/Core/ScriptOptions.cs`** -> AI Confidence: **99.18%**
1224. **`src/Scripting/CoreTest.Desktop/GlobalAssemblyCacheTests.cs`** -> AI Confidence: **99.18%**
1225. **`src/Test/PdbUtilities/EditAndContinue/EditAndContinueTest.cs`** -> AI Confidence: **99.18%**
1226. **`src/Test/PdbUtilities/Reader/PdbTestUtilities.cs`** -> AI Confidence: **99.18%**
1227. **`src/Test/PdbUtilities/Reader/PdbValidation.cs`** -> AI Confidence: **99.18%**
1228. **`src/Tools/AnalyzerRunner/CodeRefactoringRunner.cs`** -> AI Confidence: **99.18%**
1229. **`src/Tools/BuildBoss/CompilerNuGetCheckerUtil.cs`** -> AI Confidence: **99.18%**
1230. **`src/Tools/BuildBoss/OptProfCheckerUtil.cs`** -> AI Confidence: **99.18%**
1231. **`src/Tools/ExternalAccess/Razor/Features/Cohost/RazorStartupServiceFactory.cs`** -> AI Confidence: **99.18%**
1232. **`src/Tools/ExternalAccess/Razor/Features/RazorMappingServiceWrapper.cs`** -> AI Confidence: **99.18%**
1233. **`src/Tools/ExternalAccess/Razor/Features/RazorSourceGeneratedDocumentSpanMappingServiceWrapper.cs`** -> AI Confidence: **99.18%**
1234. **`src/Tools/ExternalAccess/Xaml/Internal/DescriptionService.cs`** -> AI Confidence: **99.18%**
1235. **`src/Tools/SemanticSearch/Extensions/ProjectModel.cs`** -> AI Confidence: **99.18%**
1236. **`src/Tools/Source/RunTests/AssemblyScheduler.cs`** -> AI Confidence: **99.18%**
1237. **`src/Tools/Source/RunTests/ProcessTestExecutor.cs`** -> AI Confidence: **99.18%**
1238. **`src/VisualStudio/CSharp/Impl/EditorConfigSettings/DataProvider/CodeStyle/CSharpCodeStyleSettingsProvider.cs`** -> AI Confidence: **99.18%**
1239. **`src/VisualStudio/CSharp/Impl/EditorConfigSettings/DataProvider/Whitespace/CSharpWhitespaceSettingsProvider.cs`** -> AI Confidence: **99.18%**
1240. **`src/VisualStudio/CSharp/Impl/ProjectSystemShim/TempPECompilerService.cs`** -> AI Confidence: **99.18%**
1241. **`src/VisualStudio/CSharp/Impl/Utilities/CSharpParseOptionsChangingService.cs`** -> AI Confidence: **99.18%**
1242. **`src/VisualStudio/CodeLens/ReferenceCodeLensProvider.cs`** -> AI Confidence: **99.18%**
1243. **`src/VisualStudio/Core/Def/CommonControls/MemberSelectionViewModel.cs`** -> AI Confidence: **99.18%**
1244. **`src/VisualStudio/Core/Def/DesignerAttribute/VisualStudioDesignerAttributeService.cs`** -> AI Confidence: **99.18%**
1245. **`src/VisualStudio/Core/Def/Diagnostics/VisualStudioVenusSpanMappingService.cs`** -> AI Confidence: **99.18%**
1246. **`src/VisualStudio/Core/Def/EditorConfigSettings/DataProvider/CodeStyle/CommonCodeStyleSettingsProvider.cs`** -> AI Confidence: **99.18%**
1247. **`src/VisualStudio/Core/Def/EditorConfigSettings/SettingsEditorFactory.cs`** -> AI Confidence: **99.18%**
1248. **`src/VisualStudio/Core/Def/ErrorReporting/VisualStudioInfoBar.cs`** -> AI Confidence: **99.18%**
1249. **`src/VisualStudio/Core/Def/Extensions/DocumentExtensions.cs`** -> AI Confidence: **99.18%**
1250. **`src/VisualStudio/Core/Def/Extensions/VisualStudioWorkspaceImplExtensions.cs`** -> AI Confidence: **99.18%**
1251. **`src/VisualStudio/Core/Def/FindReferences/Contexts/WithReferencesFindUsagesContext.cs`** -> AI Confidence: **99.18%**
1252. **`src/VisualStudio/Core/Def/FindReferences/RoslynDefinitionBucket.cs`** -> AI Confidence: **99.18%**
1253. **`src/VisualStudio/Core/Def/FindReferences/StreamingFindUsagesPresenter.cs`** -> AI Confidence: **99.18%**
1254. **`src/VisualStudio/Core/Def/Implementation/AbstractEditorFactory.cs`** -> AI Confidence: **99.18%**
1255. **`src/VisualStudio/Core/Def/Implementation/AbstractVsTextViewFilter.cs`** -> AI Confidence: **99.18%**
1256. **`src/VisualStudio/Core/Def/Implementation/HierarchyItemToProjectIdMap.cs`** -> AI Confidence: **99.18%**
1257. **`src/VisualStudio/Core/Def/InheritanceMargin/InheritanceGlyphManager.cs`** -> AI Confidence: **99.18%**
1258. **`src/VisualStudio/Core/Def/InheritanceMargin/InheritanceMarginHelpers.cs`** -> AI Confidence: **99.18%**
1259. **`src/VisualStudio/Core/Def/InheritanceMargin/MarginGlyph/InheritanceMarginGlyph.cs`** -> AI Confidence: **99.18%**
1260. **`src/VisualStudio/Core/Def/InlineRename/InlineRenameUndoManager.cs`** -> AI Confidence: **99.18%**
1261. **`src/VisualStudio/Core/Def/Interactive/VsResetInteractive.cs`** -> AI Confidence: **99.18%**
1262. **`src/VisualStudio/Core/Def/LanguageService/AbstractCreateServicesOnTextViewConnection.cs`** -> AI Confidence: **99.18%**
1263. **`src/VisualStudio/Core/Def/LanguageService/AbstractLanguageService`2.IVsImmediateStatementCompletion2.cs`** -> AI Confidence: **99.18%**
1264. **`src/VisualStudio/Core/Def/LanguageService/AbstractLanguageService`2.VsCodeWindowManager.cs`** -> AI Confidence: **99.18%**
1265. **`src/VisualStudio/Core/Def/LanguageService/AbstractLanguageService`2.VsLanguageDebugInfo.cs`** -> AI Confidence: **99.18%**
1266. **`src/VisualStudio/Core/Def/LanguageService/PackageLoadTasks.cs`** -> AI Confidence: **99.18%**
1267. **`src/VisualStudio/Core/Def/Library/AbstractObjectList.cs`** -> AI Confidence: **99.18%**
1268. **`src/VisualStudio/Core/Def/Library/ClassView/AbstractSyncClassViewCommandHandler.cs`** -> AI Confidence: **99.18%**
1269. **`src/VisualStudio/Core/Def/NavigateTo/RoslynSearchResultViewFactory.cs`** -> AI Confidence: **99.18%**
1270. **`src/VisualStudio/Core/Def/Options/VisualStudioUnifiedSettingsOptionPersister.cs`** -> AI Confidence: **99.18%**
1271. **`src/VisualStudio/Core/Def/Packaging/PackageInstallerServiceFactory.cs`** -> AI Confidence: **99.18%**
1272. **`src/VisualStudio/Core/Def/PdbSourceDocument/PdbSourceDocumentOutputWindowLogger.cs`** -> AI Confidence: **99.18%**
1273. **`src/VisualStudio/Core/Def/PickMembers/PickMembersDialogViewModel.cs`** -> AI Confidence: **99.18%**
1274. **`src/VisualStudio/Core/Def/Preview/FileChange.cs`** -> AI Confidence: **99.18%**
1275. **`src/VisualStudio/Core/Def/Preview/PreviewEngine.cs`** -> AI Confidence: **99.18%**
1276. **`src/VisualStudio/Core/Def/ProjectSystem/Extensions/ProjectExtensions.cs`** -> AI Confidence: **99.18%**
1277. **`src/VisualStudio/Core/Def/ProjectSystem/FileChangeTracker.cs`** -> AI Confidence: **99.18%**
1278. **`src/VisualStudio/Core/Def/ProjectSystem/FileChangeWatcher.cs`** -> AI Confidence: **99.18%**
1279. **`src/VisualStudio/Core/Def/ProjectSystem/MetadataReferences/VisualStudioPortableExecutableReference.cs`** -> AI Confidence: **99.18%**
1280. **`src/VisualStudio/Core/Def/ProjectSystem/OpenTextBufferProvider.cs`** -> AI Confidence: **99.18%**
1281. **`src/VisualStudio/Core/Def/StackTraceExplorer/StackFrameViewModel.cs`** -> AI Confidence: **99.18%**
1282. **`src/VisualStudio/Core/Def/StackTraceExplorer/StackTraceExplorerToolWindow.cs`** -> AI Confidence: **99.18%**
1283. **`src/VisualStudio/Core/Def/SyncNamespaces/SyncNamespacesCommandHandler.cs`** -> AI Confidence: **99.18%**
1284. **`src/VisualStudio/Core/Def/TaskList/ProjectExternalErrorReporter.cs`** -> AI Confidence: **99.18%**
1285. **`src/VisualStudio/Core/Def/TaskList/VisualStudioDiagnosticIdCache.cs`** -> AI Confidence: **99.18%**
1286. **`src/VisualStudio/Core/Def/Utilities/VsCodeWindowViewTracker.cs`** -> AI Confidence: **99.18%**
1287. **`src/VisualStudio/Core/Def/ValueTracking/ValueTrackingTreeViewModel.cs`** -> AI Confidence: **99.18%**
1288. **`src/VisualStudio/Core/Def/Venus/ContainedDocument.DocumentServiceProvider.cs`** -> AI Confidence: **99.18%**
1289. **`src/VisualStudio/Core/Def/Workspace/VisualStudioDocumentNavigationService.cs`** -> AI Confidence: **99.18%**
1290. **`src/VisualStudio/Core/Def/Workspace/VisualStudioFormattingRuleFactoryServiceFactory.cs`** -> AI Confidence: **99.18%**
1291. **`src/VisualStudio/Core/Def/Workspace/VisualStudioSourceGeneratorTelemetryCollectorWorkspaceServiceFactory.cs`** -> AI Confidence: **99.18%**
1292. **`src/VisualStudio/Core/Def/Workspace/VisualStudioSymbolNavigationService.cs`** -> AI Confidence: **99.18%**
1293. **`src/VisualStudio/Core/Def/Workspace/VisualStudioSymbolRenamedCodeActionOperationFactoryWorkspaceService.cs`** -> AI Confidence: **99.18%**
1294. **`src/VisualStudio/Core/Def/Workspace/VisualStudioTextUndoHistoryWorkspaceServiceFactory.cs`** -> AI Confidence: **99.18%**
1295. **`src/VisualStudio/Core/Impl/CodeModel/CodeTypeRef.cs`** -> AI Confidence: **99.18%**
1296. **`src/VisualStudio/Core/Impl/CodeModel/Collections/BasesCollection.cs`** -> AI Confidence: **99.18%**
1297. **`src/VisualStudio/Core/Impl/CodeModel/Collections/ExternalMemberCollection.cs`** -> AI Confidence: **99.18%**
1298. **`src/VisualStudio/Core/Impl/CodeModel/Collections/ExternalNamespaceEnumerator.cs`** -> AI Confidence: **99.18%**
1299. **`src/VisualStudio/Core/Impl/CodeModel/ExternalElements/AbstractExternalCodeElement.cs`** -> AI Confidence: **99.18%**
1300. **`src/VisualStudio/Core/Impl/CodeModel/FileCodeModel.cs`** -> AI Confidence: **99.18%**
1301. **`src/VisualStudio/Core/Impl/CodeModel/FileCodeModel_CodeGen.cs`** -> AI Confidence: **99.18%**
1302. **`src/VisualStudio/Core/Impl/CodeModel/MethodXml/AbstractMethodXmlBuilder.cs`** -> AI Confidence: **99.18%**
1303. **`src/VisualStudio/Core/Impl/Options/AbstractOptionPageControl.cs`** -> AI Confidence: **99.18%**
1304. **`src/VisualStudio/Core/Impl/Options/Style/NamingPreferences/NamingStyleOptionPageControl.xaml.cs`** -> AI Confidence: **99.18%**
1305. **`src/VisualStudio/Core/Impl/RoslynVisualStudioWorkspace.cs`** -> AI Confidence: **99.18%**
1306. **`src/VisualStudio/Core/Impl/SolutionExplorer/SymbolTree/RootSymbolTreeItemSourceProvider.cs`** -> AI Confidence: **99.18%**
1307. **`src/VisualStudio/Core/Test.Next/Options/VisualStudioOptionStorageTests.cs`** -> AI Confidence: **99.18%**
1308. **`src/VisualStudio/Core/Test.Next/Options/VisualStudioSettingsOptionPersisterTests.cs`** -> AI Confidence: **99.18%**
1309. **`src/VisualStudio/Core/Test.Next/UnifiedSettings/TestModel/Utilities.cs`** -> AI Confidence: **99.18%**
1310. **`src/VisualStudio/DevKit/Impl/Logging/VSCodeTelemetryLogger.cs`** -> AI Confidence: **99.18%**
1311. **`src/VisualStudio/ExternalAccess/FSharp/Editor/Shared/Utilities/FSharpClassificationTypeMap.cs`** -> AI Confidence: **99.18%**
1312. **`src/VisualStudio/ExternalAccess/FSharp/InlineHints/FSharpInlineHint.cs`** -> AI Confidence: **99.18%**
1313. **`src/VisualStudio/ExternalAccess/FSharp/Internal/DocumentHighlighting/FSharpDocumentHighlightsService.cs`** -> AI Confidence: **99.18%**
1314. **`src/VisualStudio/ExternalAccess/FSharp/Internal/Editor/FSharpEditorInlineRenameService.cs`** -> AI Confidence: **99.18%**
1315. **`src/VisualStudio/IntegrationTest/Harness/IntegrationTestServiceShared/IntegrationTestServiceCommands.cs`** -> AI Confidence: **99.18%**
1316. **`src/VisualStudio/IntegrationTest/Harness/SourceGeneratorUnitTests/Resources/TestGenerationForVS18/AbstractIdeIntegrationTest.g.cs`** -> AI Confidence: **99.18%**
1317. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/InProcessIdeTestAssemblyRunner.cs`** -> AI Confidence: **99.18%**
1318. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/VisualStudioInstanceFactory.cs`** -> AI Confidence: **99.18%**
1319. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/IdeTestCase.cs`** -> AI Confidence: **99.18%**
1320. **`src/VisualStudio/IntegrationTest/Harness/XUnitShared/Threading/IdeTheoryTestCase.cs`** -> AI Confidence: **99.18%**
1321. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/AbstractIntegrationTest.cs`** -> AI Confidence: **99.18%**
1322. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/CSharp/CSharpFindReferences.cs`** -> AI Confidence: **99.18%**
1323. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/DialogHelpers.cs`** -> AI Confidence: **99.18%**
1324. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/EditorVerifierInProcess.cs`** -> AI Confidence: **99.18%**
1325. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/ITextViewWindowVerifierInProcessExtensions.cs`** -> AI Confidence: **99.18%**
1326. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/LocalsWindowInProcess.cs`** -> AI Confidence: **99.18%**
1327. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/SolutionExplorerVerifierInProcess.cs`** -> AI Confidence: **99.18%**
1328. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/InfrastructureTests.cs`** -> AI Confidence: **99.18%**
1329. **`src/VisualStudio/IntegrationTest/New.IntegrationTests/IntegrationHelper.cs`** -> AI Confidence: **99.18%**
1330. **`src/VisualStudio/Razor/RazorLanguageServiceClient.cs`** -> AI Confidence: **99.18%**
1331. **`src/VisualStudio/Razor/RazorLanguageServiceClientFactory.cs`** -> AI Confidence: **99.18%**
1332. **`src/VisualStudio/VisualStudioDiagnosticsToolWindow/OptionPages/InternalOptionsControl.cs`** -> AI Confidence: **99.18%**
1333. **`src/VisualStudio/VisualStudioDiagnosticsToolWindow/Panels/TelemetryPanel.xaml.cs`** -> AI Confidence: **99.18%**
1334. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/FunctionPointerUnmanagedCallingConventionClassifier.cs`** -> AI Confidence: **99.18%**
1335. **`src/Workspaces/CSharp/Portable/Classification/SyntaxClassification/SyntaxTokenClassifier.cs`** -> AI Confidence: **99.18%**
1336. **`src/Workspaces/CSharp/Portable/FindSymbols/CSharpDeclaredSymbolInfoFactoryService.cs`** -> AI Confidence: **99.18%**
1337. **`src/Workspaces/CSharp/Portable/Simplification/Reducers/AbstractCSharpReducer.AbstractReductionRewriter.cs`** -> AI Confidence: **99.18%**
1338. **`src/Workspaces/CSharp/Portable/Simplification/Simplifiers/MemberAccessExpressionSimplifier.cs`** -> AI Confidence: **99.18%**
1339. **`src/Workspaces/CSharpTest/Formatting/FormattingElasticTriviaTests.cs`** -> AI Confidence: **99.18%**
1340. **`src/Workspaces/CSharpTest/Formatting/FormattingTests.cs`** -> AI Confidence: **99.18%**
1341. **`src/Workspaces/Core/Portable/CaseCorrection/CaseCorrector.cs`** -> AI Confidence: **99.18%**
1342. **`src/Workspaces/Core/Portable/Classification/AbstractClassificationService.cs`** -> AI Confidence: **99.18%**
1343. **`src/Workspaces/Core/Portable/CodeActions/CodeAction.cs`** -> AI Confidence: **99.18%**
1344. **`src/Workspaces/Core/Portable/CodeActions/Operations/ApplyChangesOperation.cs`** -> AI Confidence: **99.18%**
1345. **`src/Workspaces/Core/Portable/CodeCleanup/AbstractCodeCleanerService.cs`** -> AI Confidence: **99.18%**
1346. **`src/Workspaces/Core/Portable/Diagnostics/DiagnosticAnalyzerInfoCache.cs`** -> AI Confidence: **99.18%**
1347. **`src/Workspaces/Core/Portable/FindSymbols/Declarations/DeclarationFinder.cs`** -> AI Confidence: **99.18%**
1348. **`src/Workspaces/Core/Portable/FindSymbols/Declarations/DeclarationFinder_AllDeclarations.cs`** -> AI Confidence: **99.18%**
1349. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/FindReferenceCache.cs`** -> AI Confidence: **99.18%**
1350. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/FindReferencesSearchEngine_FindReferencesInDocuments.cs`** -> AI Confidence: **99.18%**
1351. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/AbstractReferenceFinder.cs`** -> AI Confidence: **99.18%**
1352. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/CrefTypeParameterSymbolReferenceFinder.cs`** -> AI Confidence: **99.18%**
1353. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/Finders/NamespaceSymbolReferenceFinder.cs`** -> AI Confidence: **99.18%**
1354. **`src/Workspaces/Core/Portable/FindSymbols/FindReferences/StreamingFindReferencesProgress.cs`** -> AI Confidence: **99.18%**
1355. **`src/Workspaces/Core/Portable/FindSymbols/SymbolTree/SymbolTreeInfo.cs`** -> AI Confidence: **99.18%**
1356. **`src/Workspaces/Core/Portable/FindSymbols/SymbolTree/SymbolTreeInfoCacheService.cs`** -> AI Confidence: **99.18%**
1357. **`src/Workspaces/Core/Portable/LinkedFileDiffMerging/LinkedFileDiffMergingSession.cs`** -> AI Confidence: **99.18%**
1358. **`src/Workspaces/Core/Portable/Options/GlobalOptionService.cs`** -> AI Confidence: **99.18%**
1359. **`src/Workspaces/Core/Portable/Options/LegacyWorkspaceOptionService.cs`** -> AI Confidence: **99.18%**
1360. **`src/Workspaces/Core/Portable/Rename/ConflictEngine/ConflictResolver.cs`** -> AI Confidence: **99.18%**
1361. **`src/Workspaces/Core/Portable/Rename/ConflictEngine/RenamedSpansTracker.cs`** -> AI Confidence: **99.18%**
1362. **`src/Workspaces/Core/Portable/Rename/Renamer.cs`** -> AI Confidence: **99.18%**
1363. **`src/Workspaces/Core/Portable/Serialization/SerializableSourceText.cs`** -> AI Confidence: **99.18%**
1364. **`src/Workspaces/Core/Portable/Serialization/SerializerService.cs`** -> AI Confidence: **99.18%**
1365. **`src/Workspaces/Core/Portable/Serialization/SerializerService_Reference.cs`** -> AI Confidence: **99.18%**
1366. **`src/Workspaces/Core/Portable/Shared/Extensions/IFindReferencesResultExtensions.cs`** -> AI Confidence: **99.18%**
1367. **`src/Workspaces/Core/Portable/Shared/Extensions/INamespaceSymbolExtensions.cs`** -> AI Confidence: **99.18%**
1368. **`src/Workspaces/Core/Portable/Shared/Extensions/ITypeSymbolExtensions.cs`** -> AI Confidence: **99.18%**
1369. **`src/Workspaces/Core/Portable/Storage/AbstractPersistentStorageService.cs`** -> AI Confidence: **99.18%**
1370. **`src/Workspaces/Core/Portable/Storage/SQLite/v2/Interop/SqlConnection.cs`** -> AI Confidence: **99.18%**
1371. **`src/Workspaces/Core/Portable/Utilities/Documentation/XmlDocumentationProvider.cs`** -> AI Confidence: **99.18%**
1372. **`src/Workspaces/Core/Portable/Workspace/CommandLineProject.cs`** -> AI Confidence: **99.18%**
1373. **`src/Workspaces/Core/Portable/Workspace/IsolatedAnalyzerReferenceSet.Core.cs`** -> AI Confidence: **99.18%**
1374. **`src/Workspaces/Core/Portable/Workspace/ProjectSystem/FileWatchedPortableExecutableReferenceFactory.cs`** -> AI Confidence: **99.18%**
1375. **`src/Workspaces/Core/Portable/Workspace/Solution/ChecksumCollection.cs`** -> AI Confidence: **99.18%**
1376. **`src/Workspaces/Core/Portable/Workspace/Solution/Document.cs`** -> AI Confidence: **99.18%**
1377. **`src/Workspaces/Core/Portable/Workspace/Solution/DocumentState.cs`** -> AI Confidence: **99.18%**
1378. **`src/Workspaces/Core/Portable/Workspace/Solution/ProjectState.cs`** -> AI Confidence: **99.18%**
1379. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.CompilationTracker.CompilationTrackerState.cs`** -> AI Confidence: **99.18%**
1380. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.RegularCompilationTracker_Generators.cs`** -> AI Confidence: **99.18%**
1381. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.SkeletonReferenceCache.cs`** -> AI Confidence: **99.18%**
1382. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.WithFrozenSourceGeneratedDocumentsCompilationTracker.cs`** -> AI Confidence: **99.18%**
1383. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionCompilationState.cs`** -> AI Confidence: **99.18%**
1384. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionState.cs`** -> AI Confidence: **99.18%**
1385. **`src/Workspaces/Core/Portable/Workspace/Solution/SolutionState_Checksum.cs`** -> AI Confidence: **99.18%**
1386. **`src/Workspaces/Core/Portable/Workspace/Solution/TextLoader.cs`** -> AI Confidence: **99.18%**
1387. **`src/Workspaces/Core/Portable/Workspace/Solution/VersionSource/RecoverableTextAndVersion.RecoverableText.cs`** -> AI Confidence: **99.18%**
1388. **`src/Workspaces/Core/Portable/Workspace/WorkspaceEventMap.cs`** -> AI Confidence: **99.18%**
1389. **`src/Workspaces/CoreTest/Remote/ServiceDescriptorTests.cs`** -> AI Confidence: **99.18%**
1390. **`src/Workspaces/CoreTestUtilities/Remote/TestSerializerService.cs`** -> AI Confidence: **99.18%**
1391. **`src/Workspaces/CoreTestUtilities/Workspaces/TestWorkspace`1.cs`** -> AI Confidence: **99.18%**
1392. **`src/Workspaces/MSBuild/BuildHost/MSBuild/ProjectFile/ProjectInstanceReader.cs`** -> AI Confidence: **99.18%**
1393. **`src/Workspaces/MSBuild/Core/MSBuild/SolutionFileReader.cs`** -> AI Confidence: **99.18%**
1394. **`src/Workspaces/Remote/Core/BrokeredServiceConnection.cs`** -> AI Confidence: **99.18%**
1395. **`src/Workspaces/Remote/Core/RemoteCallback.cs`** -> AI Confidence: **99.18%**
1396. **`src/Workspaces/Remote/Core/RemoteSerializationOptions.cs`** -> AI Confidence: **99.18%**
1397. **`src/Workspaces/Remote/Core/ServiceHubRemoteHostClient.cs`** -> AI Confidence: **99.18%**
1398. **`src/Workspaces/Remote/ServiceHub/Host/RemoteExportProviderBuilder.cs`** -> AI Confidence: **99.18%**
1399. **`src/Workspaces/Remote/ServiceHub/Host/RemoteWorkspace.cs`** -> AI Confidence: **99.18%**
1400. **`src/Workspaces/Remote/ServiceHub/Host/SolutionAssetCache.cs`** -> AI Confidence: **99.18%**
1401. **`src/Workspaces/Remote/ServiceHub/Services/BrokeredServiceBase.cs`** -> AI Confidence: **99.18%**
1402. **`src/Workspaces/Remote/ServiceHub/Services/DiagnosticAnalyzer/PerformanceTrackerService.cs`** -> AI Confidence: **99.18%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `988` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `84094` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/Features/ExternalAccess/Copilot/Internal/SemanticSearch/CopilotSemanticSearchQueryExecutor.cs` (CSHARP) -> Cumulative Risk: **801.22**
- **Archetype:** `file_cluster_4` (Distance: 12.881 IQR)
- **Magnitude:** 177.9 | **LOC:** 143 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 94.4%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `CopilotSemanticSearchQueryExecutor` (Impact: 21.7), `ExecuteAsync` (Impact: 19.2), `ResultsObserver` (Impact: 9.3)

### 2. `src/Workspaces/Core/Portable/Workspace/Solution/TextDocumentState.cs` (CSHARP) -> Cumulative Risk: **796.93**
- **Archetype:** `file_cluster_4` (Distance: 12.176 IQR)
- **Magnitude:** 209.6 | **LOC:** 231 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 94.7%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.972%)
- **Heaviest Functions:** `GetTextAndVersionAsync` (Impact: 7.9), `TryGetText` (Impact: 7.4), `TextDocumentState` (Impact: 5.7)

### 3. `src/VisualStudio/CSharp/Impl/SemanticSearch/SemanticSearchQueryExecutor.cs` (CSHARP) -> Cumulative Risk: **784.85**
- **Archetype:** `file_cluster_4` (Distance: 11.759 IQR)
- **Magnitude:** 268.24 | **LOC:** 229 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 94.4%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `SemanticSearchQueryExecutor` (Impact: 64.2), `ResultsObserver` (Impact: 21.5), `ExecuteAsync` (Impact: 20.9)

### 4. `src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/MessageBoxInProcess.cs` (CSHARP) -> Cumulative Risk: **765.1**
- **Archetype:** `file_cluster_4` (Distance: 14.855 IQR)
- **Magnitude:** 193.72 | **LOC:** 232 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), State Flux (99.9979%)
- **Heaviest Functions:** `ShowHotReloadDialog` (Impact: 33.2), `ShowMessageBox` (Impact: 11.6), `QueryService` (Impact: 6.8)

### 5. `src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/ShellInProcess.cs` (CSHARP) -> Cumulative Risk: **758.01**
- **Archetype:** `file_cluster_4` (Distance: 10.887 IQR)
- **Magnitude:** 163.2 | **LOC:** 210 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `ShowNavigateToDialogAsync` (Impact: 16.8), `WaitForNavigateToFocusAsync` (Impact: 15.1), `IsActiveTabProvisionalAsync` (Impact: 10.7)

### 6. `src/Features/CSharpTest/GenerateFromMembers/AddConstructorParametersFromMembers/AddConstructorParametersFromMembersTests.cs` (CSHARP) -> Cumulative Risk: **752.56**
- **Archetype:** `file_cluster_8` (Distance: 11.15 IQR)
- **Magnitude:** 1390.82 | **LOC:** 2628 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9986%), State Flux (98.6393%)
- **Heaviest Functions:** `TestMultipleConstructors_OneMustBeOption` (Impact: 9.6), `TestTupleOptionalCSharp7` (Impact: 6.2), `TestTupleOptionalWithNames_CSharp7` (Impact: 6.2)

### 7. `src/VisualStudio/Xaml/Impl/Features/InlineRename/XamlEditorInlineRenameService.cs` (CSHARP) -> Cumulative Risk: **747.23**
- **Archetype:** `file_cluster_13` (Distance: 11.153 IQR)
- **Magnitude:** 137.4 | **LOC:** 204 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 94.4%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.1139%), Concurrency (94.7294%)
- **Heaviest Functions:** `FromSymbolKind` (Impact: 25.6), `GetReplacementsAsync` (Impact: 4.7), `GetReplacements` (Impact: 4.7)

### 8. `src/Workspaces/Core/Portable/Workspace/Host/TemporaryStorage/LegacyTemporaryStorageService.cs` (CSHARP) -> Cumulative Risk: **746.61**
- **Archetype:** `file_cluster_4` (Distance: 12.187 IQR)
- **Magnitude:** 137.54 | **LOC:** 116 | **CtrlFlow:** 44.7% | **Authorship Centralization:** 94.1%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9988%)
- **Heaviest Functions:** `WriteStreamAsync` (Impact: 11.1), `ReadStream` (Impact: 8.3), `ReadText` (Impact: 8.0)

### 9. `src/RoslynAnalyzers/PublicApiAnalyzers/Core/CodeFixes/NullableEnablePublicApiFix.cs` (CSHARP) -> Cumulative Risk: **742.48**
- **Archetype:** `file_cluster_13` (Distance: 10.892 IQR)
- **Magnitude:** 160.58 | **LOC:** 163 | **CtrlFlow:** 31.6% | **Authorship Centralization:** 95.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.4578%), Concurrency (97.1656%), Tech Debt (96.9826%)
- **Heaviest Functions:** `NullableEnablePublicApiFix` (Impact: 40.0), `GetFixAsync` (Impact: 31.1), `GetChangedSolutionAsync` (Impact: 17.5)

### 10. `src/VisualStudio/Core/Impl/ProjectSystem/CPS/CPSProject_IWorkspaceProjectContext.cs` (CSHARP) -> Cumulative Risk: **734.61**
- **Archetype:** `file_cluster_13` (Distance: 11.558 IQR)
- **Magnitude:** 208.96 | **LOC:** 300 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9929%), Concurrency (99.9235%)
- **Heaviest Functions:** `SetProperty` (Impact: 35.7), `Dispose` (Impact: 15.6), `DisposeAsync` (Impact: 9.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.438 IQR)
- **Top Global Matches:** file_cluster_8: 10.438, file_cluster_0: 10.611, file_cluster_7: 11.045
- **Magnitude:** 17094.18 | **LOC:** 4351 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.0554%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `Main` (Impact: 382.7)
  * `Main` (Impact: 382.5)
  * `Main` (Impact: 382.2)
  * `Main` (Impact: 380.3)
  * `Main` (Impact: 380.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 889`, `args: 518`, `func_start: 631`, `class_start: 278`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 46`, `duplicate_logic: 237`, `orphaned_logic: 19`
* *Architecture:* `io: 1`, `api: 443`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 16`, `doc: 1`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.Editor.UnitTests.CompleteStatement, Microsoft.CodeAnalysis.Test.Utilities, System.Runtime.CompilerServices, Xunit, Microsoft.CodeAnalysis.Options, Microsoft.VisualStudio.Commanding, Microsoft.CodeAnalysis.Editor.CSharp.CompleteStatement, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.79 IQR)
- **Top Global Matches:** file_cluster_8: 13.79, file_cluster_11: 13.941, file_cluster_13: 14.026
- **Magnitude:** 13745.92 | **LOC:** 14680 | **CtrlFlow:** 59.0% | **Authorship Centralization:** 51.9%
- **Risk Profile:** Cognitive Load (69.4198%), Tech Debt (82.1896%)
**Top Internal Functions/Classes:**
  * `parseSwitchHeader` (Impact: 914.2)
  * `ParseSwitchStatement` (Impact: 902.9)
  * `ParseMemberName` (Impact: 726.7)
  * `not` (Impact: 635.0)
    * *Intent:* // even if we saw a { or think we should parse members bail out early since // we know namespaces ca...
  * `ParseParameterModifiers` (Impact: 577.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1705`, `structural_boundaries: 1186`, `args: 390`, `func_start: 1021`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 9`, `state_mutation: 1723`, `dead_code: 37`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 49`, `orphaned_logic: 55`
* *Architecture:* `api: 38`, `import: 11`
* *Defense:* `safety: 161`, `doc: 143`, `immutability_locks: 12`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Text, Roslyn.Utilities, Microsoft.CodeAnalysis.Syntax.InternalSyntax, Microsoft.CodeAnalysis.CSharp.Symbols, System.Threading, System.Diagnostics, Microsoft.CodeAnalysis.PooledObjects, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.092 IQR)
- **Top Global Matches:** file_cluster_8: 14.092, file_cluster_11: 14.283, file_cluster_13: 14.322
- **Magnitude:** 10705.04 | **LOC:** 14301 | **CtrlFlow:** 57.2% | **Authorship Centralization:** 51.4%
- **Risk Profile:** Cognitive Load (46.8154%), Tech Debt (95.5921%)
**Top Internal Functions/Classes:**
  * `VisitConversion` (Impact: 885.1)
  * `visitArgumentsCore` (Impact: 799.1)
  * `ConvertConditionalOperandOrSwitchExpress` (Impact: 604.1)
  * `VisitArgumentEvaluateEpilogue` (Impact: 519.8)
  * `VisitNullCoalescingOperator` (Impact: 471.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1327`, `structural_boundaries: 991`, `args: 396`, `func_start: 1379`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 1`, `state_mutation: 1463`, `dead_code: 18`, `planned_debt: 4`, `duplicate_logic: 66`, `orphaned_logic: 87`
* *Architecture:* `api: 158`, `import: 14`
* *Defense:* `safety: 395`, `doc: 223`, `immutability_locks: 119`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections.Concurrent, System.Text, System.Runtime.CompilerServices, Roslyn.Utilities, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.Collections, System.Diagnostics, Microsoft.CodeAnalysis.CSharp.Syntax...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.15%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.235 IQR)
- **Top Global Matches:** file_cluster_0: 14.235, file_cluster_11: 14.454, file_cluster_8: 14.521
- **Magnitude:** 10244.46 | **LOC:** 24845 | **CtrlFlow:** 30.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (14.2403%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `NonBoxingUnionMatching_56_TryGetValue` (Impact: 111.0)
  * `NonBoxingUnionMatching_55_TryGetValue` (Impact: 101.6)
  * `NonBoxingUnionMatching_54_TryGetValue` (Impact: 88.9)
  * `UnionMatching_37_SwitchStatement_01` (Impact: 82.5)
  * `NonBoxingUnionMatching_53_TryGetValue` (Impact: 78.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1871`, `structural_boundaries: 4262`, `args: 3829`, `func_start: 5615`, `class_start: 852`
* *Risk/State:* `safety_bypasses: 308`, `high_risk_execution: 23`, `state_mutation: 1966`, `dead_code: 252`, `planned_debt: 3`, `duplicate_logic: 19`, `orphaned_logic: 316`
* *Architecture:* `api: 1827`, `import: 13`
* *Defense:* `safety: 590`, `test: 549`, `immutability_locks: 327`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.Test.Utilities, Xunit, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Operations, System.Linq, Microsoft.CodeAnalysis.CSharp.Symbols, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.176 IQR)
- **Top Global Matches:** file_cluster_4: 12.176, file_cluster_8: 12.326, file_cluster_0: 12.49
- **Magnitude:** 7459.7 | **LOC:** 15181 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (81.3665%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `TestWithInterface_OnStruct_ImplicitInter` (Impact: 205.6)
  * `TestWithPattern_RefStructEnumerator_Asyn` (Impact: 48.2)
  * `TestWithUIntToIntConversion` (Impact: 38.2)
  * `TestWithObsoletePatternMethodsViaExtensi` (Impact: 31.9)
    * *Intent:* // Code size 40 (0x28)
  * `TestWithPattern_RefStructCurrent_AsyncIt` (Impact: 29.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 721`, `structural_boundaries: 2737`, `args: 1230`, `func_start: 1870`, `class_start: 520`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 437`, `dead_code: 11`, `planned_debt: 9`, `duplicate_logic: 74`, `orphaned_logic: 86`
* *Architecture:* `api: 1371`, `concurrency: 3265`, `import: 334`
* *Defense:* `safety: 141`, `test: 259`, `immutability_locks: 102`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Test.Utilities, N1, System.Runtime.CompilerServices, System.Globalization, Microsoft.CodeAnalysis.CSharp.Syntax, System, Xunit, N2...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.644 IQR)
- **Top Global Matches:** file_cluster_0: 13.644, file_cluster_11: 13.691, file_cluster_4: 13.71
- **Magnitude:** 7422.66 | **LOC:** 29709 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (66.0448%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `UnscopedRefInImplementation_Indexer_01` (Impact: 142.9)
  * `UnscopedRefInImplementation_Property_01` (Impact: 134.0)
  * `AwaitForeach_IAsyncEnumerableT_07` (Impact: 116.0)
  * `AwaitForeach_IAsyncEnumerableT_05` (Impact: 102.0)
  * `AwaitForeach_IAsyncEnumerableT_04` (Impact: 99.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 784`, `structural_boundaries: 2712`, `args: 999`, `func_start: 2722`, `class_start: 424`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2322`, `dead_code: 108`, `planned_debt: 8`, `duplicate_logic: 35`, `orphaned_logic: 171`
* *Architecture:* `api: 820`, `concurrency: 963`, `import: 190`
* *Defense:* `safety: 219`, `test: 445`, `immutability_locks: 52`, `cleanup: 65`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections, Microsoft.CodeAnalysis.Test.Utilities, System.Runtime.CompilerServices, System.Threading.Tasks, Xunit, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.CSharp.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/FlowAnalysis/FlowTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_0` (Drift: 17.063 IQR)
- **Top Global Matches:** file_cluster_0: 17.063, file_cluster_11: 17.196, file_cluster_17: 17.439
- **Magnitude:** 7381.48 | **LOC:** 6187 | **CtrlFlow:** 75.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SwitchStatement` (Impact: 766.3)
  * `TernaryOperator` (Impact: 594.5)
    * *Intent:* // Whidbey bug #467493
  * `IfStatement` (Impact: 304.9)
  * `LogicalExpression` (Impact: 243.2)
  * `WhileStatement` (Impact: 231.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1747`, `structural_boundaries: 574`, `args: 563`, `func_start: 1322`, `class_start: 136`
* *Risk/State:* `safety_bypasses: 18`, `high_risk_execution: 8`, `state_mutation: 2681`, `dead_code: 131`, `planned_debt: 1`, `fragile_debt: 27`, `duplicate_logic: 10`, `orphaned_logic: 118`
* *Architecture:* `api: 390`, `import: 29`
* *Defense:* `safety: 345`, `test: 113`, `sync_locks: 7`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.Test.Utilities, Xunit, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.Syntax, System.Runtime.InteropServices, System.Linq, Microsoft.CodeAnalysis.CSharp.Symbols, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/RefEscapingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.444 IQR)
- **Top Global Matches:** file_cluster_0: 14.444, file_cluster_11: 14.675, file_cluster_13: 14.692
- **Magnitude:** 5891.88 | **LOC:** 15468 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (71.2114%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MismatchedRefTernaryEscapeBlock` (Impact: 58.3)
  * `MismatchedRefTernaryEscapeBlock_UnsafeCo` (Impact: 58.3)
  * `RefLikeEscapeMixingIndexer1` (Impact: 48.8)
  * `PropertyEscape` (Impact: 36.0)
  * `ObjectInitializer_Constructor_Escape` (Impact: 31.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 2380`, `args: 1353`, `func_start: 2150`, `class_start: 324`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 2775`, `dead_code: 179`, `planned_debt: 4`, `duplicate_logic: 25`, `orphaned_logic: 230`
* *Architecture:* `api: 877`, `concurrency: 129`, `import: 363`
* *Defense:* `safety: 111`, `test: 202`, `sync_locks: 1`, `immutability_locks: 87`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections, Microsoft.CodeAnalysis.Test.Utilities, System.Runtime.CompilerServices, Roslyn.Utilities, System.Threading.Tasks, Xunit, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.Syntax...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Analyzers/CSharp/Tests/PopulateSwitch/PopulateSwitchStatementTests_FixAllTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.207 IQR)
- **Top Global Matches:** file_cluster_8: 8.207, file_cluster_16: 8.976, file_cluster_7: 9.227
- **Magnitude:** 5647.98 | **LOC:** 483 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.5313%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 72`, `args: 21`, `func_start: 21`, `class_start: 29`
* *Risk/State:* None
* *Architecture:* `api: 4`, `concurrency: 3`, `import: 3`
* *Defense:* `test: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Threading.Tasks, Xunit, Microsoft.CodeAnalysis.Test.Utilities
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.425 IQR)
- **Top Global Matches:** file_cluster_8: 13.425, file_cluster_0: 13.437, file_cluster_11: 13.663
- **Magnitude:** 5537.98 | **LOC:** 15896 | **CtrlFlow:** 28.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4989%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Conversions` (Impact: 215.5)
  * `BinaryOperators` (Impact: 156.9)
  * `IncrementOperators` (Impact: 121.7)
  * `SwitchStatement_01` (Impact: 108.9)
  * `SwitchStatement_02` (Impact: 106.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 835`, `structural_boundaries: 2152`, `args: 1013`, `func_start: 5334`, `class_start: 540`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 12`, `state_mutation: 778`, `dead_code: 92`, `planned_debt: 17`, `duplicate_logic: 69`, `orphaned_logic: 163`
* *Architecture:* `api: 979`, `concurrency: 24`, `import: 19`
* *Defense:* `safety: 348`, `doc: 45`, `test: 432`, `immutability_locks: 144`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Utilities, System.Linq.Expressions, Xunit, System.Console, Microsoft.CodeAnalysis.Emit, nuint, Microsoft.CodeAnalysis.CSharp.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/Test/Utilities/CSharp/TestSources.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.571 IQR)
- **Top Global Matches:** file_cluster_16: 11.571, file_cluster_8: 11.641, file_cluster_11: 11.893
- **Magnitude:** 5508.47 | **LOC:** 590 | **CtrlFlow:** 38.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (22.0922%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 107`, `args: 56`, `func_start: 55`, `class_start: 8`
* *Risk/State:* `state_mutation: 105`
* *Architecture:* `api: 96`, `import: 2`
* *Defense:* `safety: 7`, `doc: 19`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Runtime.CompilerServices
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncIteratorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.311 IQR)
- **Top Global Matches:** file_cluster_4: 12.311, file_cluster_8: 12.419, file_cluster_0: 12.456
- **Magnitude:** 5383.74 | **LOC:** 11935 | **CtrlFlow:** 27.8% | **Authorship Centralization:** 28.6%
- **Risk Profile:** Cognitive Load (59.4062%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MissingTypeAndMembers_IAsyncEnumerable` (Impact: 372.8)
  * `AsyncIteratorWithCustomCode` (Impact: 43.7)
  * `TryFinally_01` (Impact: 42.6)
  * `CancellationTokenParameter_SomeTokenPass` (Impact: 38.5)
  * `TryFinally_YieldBreakInDisposeMode` (Impact: 37.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 988`, `structural_boundaries: 2561`, `args: 650`, `func_start: 1839`, `class_start: 252`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 202`, `dead_code: 32`, `duplicate_logic: 75`, `orphaned_logic: 103`
* *Architecture:* `api: 427`, `concurrency: 2209`, `import: 292`
* *Defense:* `safety: 351`, `doc: 3`, `test: 164`, `sync_locks: 5`, `immutability_locks: 27`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Basic.Reference.Assemblies, System.Text, Microsoft.CodeAnalysis.CSharp.DynamicAnalysis.UnitTests, Microsoft.CodeAnalysis.CSharp.Test.Utilities, System.Reflection.PortableExecutable, Microsoft.CodeAnalysis.CSharp.UnitTests.CodeGen.Instruction, System.Runtime.CompilerServices, System.Reflection.Metadata...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/SemanticErrorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.273 IQR)
- **Top Global Matches:** file_cluster_0: 13.273, file_cluster_11: 13.55, file_cluster_8: 13.587
- **Magnitude:** 5349.06 | **LOC:** 25420 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (18.9521%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CS0165ERR_UseDefViolation05` (Impact: 180.2)
  * `CS0156ERR_BadEmptyThrow_Nesting` (Impact: 127.7)
    * *Intent:* // (13,26): error CS0029: Cannot implicitly convert type 'TS' to 'System.Exception'
  * `CS0156ERR_BadEmptyThrow_Lambdas` (Impact: 105.2)
  * `CS0165ERR_UseDefViolation03` (Impact: 67.7)
  * `CS0155ERR_BadExceptionType_TypeParameter` (Impact: 44.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1067`, `structural_boundaries: 2320`, `args: 1268`, `func_start: 2859`, `class_start: 598`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 19`, `state_mutation: 917`, `dead_code: 77`, `planned_debt: 6`, `duplicate_logic: 200`, `orphaned_logic: 284`
* *Architecture:* `io: 1`, `api: 1082`, `concurrency: 66`, `import: 141`
* *Defense:* `safety: 584`, `doc: 53`, `test: 397`, `sync_locks: 2`, `immutability_locks: 57`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Test.Utilities, B, System.Globalization, Microsoft.CodeAnalysis.CSharp.Syntax, System.Diagnostics, System.Linq.Expressions, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.223 IQR)
- **Top Global Matches:** file_cluster_0: 14.223, file_cluster_11: 14.596, file_cluster_6: 14.721
- **Magnitude:** 5336.56 | **LOC:** 20378 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.1191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CompoundAssignmentOperatorToBinaryOperat` (Impact: 35.2)
  * `Increment_070_Consumption_Prefix_NotUsed` (Impact: 31.6)
  * `Increment_074_Consumption_Postfix_NotUse` (Impact: 30.9)
  * `CompoundAssignment_00720_Consumption_Use` (Impact: 29.9)
  * `CompoundAssignment_00721_Consumption_Use` (Impact: 29.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 2670`, `args: 1185`, `func_start: 3907`, `class_start: 717`
* *Risk/State:* `state_mutation: 545`, `dead_code: 432`, `planned_debt: 71`, `duplicate_logic: 172`, `orphaned_logic: 371`
* *Architecture:* `api: 1575`, `import: 18`
* *Defense:* `safety: 743`, `doc: 256`, `test: 1241`, `immutability_locks: 179`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Test.Utilities, System.Runtime.CompilerServices, System.Threading.Tasks, System.Linq.Expressions, Xunit, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Test.Utilities, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleTest.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.824 IQR)
- **Top Global Matches:** file_cluster_0: 12.824, file_cluster_8: 12.939, file_cluster_11: 13.076
- **Magnitude:** 5267.62 | **LOC:** 29801 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.2871%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `MissingTypeInAlias` (Impact: 125.7)
  * `RealFieldsAreNotWrapped` (Impact: 28.8)
  * `verify` (Impact: 22.5)
  * `TestValueTuplesDefinition` (Impact: 21.2)
  * `verify` (Impact: 20.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 872`, `structural_boundaries: 5700`, `args: 2124`, `func_start: 7094`, `class_start: 950`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 888`, `dead_code: 214`, `planned_debt: 18`, `duplicate_logic: 46`, `orphaned_logic: 190`
* *Architecture:* `api: 2155`, `concurrency: 72`, `import: 211`
* *Defense:* `safety: 485`, `test: 2629`, `immutability_locks: 231`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Basic.Reference.Assemblies, System.Text, Microsoft.CodeAnalysis.CSharp.Test.Utilities, TestResources.NetFX.ValueTuple, System.Reflection.Metadata, System.Globalization, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/Completion/CompletionProviders/SymbolCompletionProviderTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.338 IQR)
- **Top Global Matches:** file_cluster_8: 11.338, file_cluster_0: 11.493, file_cluster_4: 11.626
- **Magnitude:** 5163.58 | **LOC:** 14435 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (54.3064%), Tech Debt (99.6274%)
**Top Internal Functions/Classes:**
  * `NestedType4_Regular` (Impact: 96.6)
  * `MethodOverloadDifferencesIgnored_Contain` (Impact: 13.7)
  * `CompletionInObjectCreationContextForType` (Impact: 12.0)
  * `TestTargetTypeCompletionInCreationContex` (Impact: 11.0)
  * `InstanceMembersFromBaseOuterType2` (Impact: 10.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 201`, `structural_boundaries: 3040`, `args: 1639`, `func_start: 2336`, `class_start: 917`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 136`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 91`, `orphaned_logic: 392`
* *Architecture:* `api: 1229`, `concurrency: 1832`, `import: 177`
* *Defense:* `safety: 110`, `doc: 7`, `test: 309`, `sync_locks: 1`, `immutability_locks: 26`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Editor.Implementation.IntelliSense.AsyncCompletion, System.Text, System.String, Namespace1, B, System.Int32, Namespace1.Namespace2, Namespace1.Namespace3.Namespace4...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Symbol/Symbols/SymbolErrorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_0` (Drift: 14.804 IQR)
- **Top Global Matches:** file_cluster_0: 14.804, file_cluster_11: 15.142, file_cluster_6: 15.315
- **Magnitude:** 5125.98 | **LOC:** 22340 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (10.3188%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `CS1747ERR_NoPIAAssemblyMissingAttribute` (Impact: 257.8)
  * `CS0646ERR_DefaultMemberOnIndexedType02` (Impact: 90.5)
  * `CS0466ERR_ExplicitImplParams` (Impact: 13.2)
  * `CS0106ERR_BadMemberFlag05` (Impact: 11.4)
  * `InnerDelegate` (Impact: 11.2)
    * *Intent:* // (12,32): error CS0564: The first operand of an overloaded shift operator must have the same type ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 497`, `structural_boundaries: 3931`, `args: 1109`, `func_start: 3265`, `class_start: 1181`
* *Risk/State:* `safety_bypasses: 76`, `state_mutation: 574`, `dead_code: 451`, `planned_debt: 48`, `fragile_debt: 5`, `duplicate_logic: 242`, `orphaned_logic: 301`
* *Architecture:* `api: 2041`, `import: 95`
* *Defense:* `safety: 400`, `doc: 62`, `test: 499`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Basic.Reference.Assemblies, TestSpace, NoExistNS2, Goo.Bar, Microsoft.CodeAnalysis.CSharp.Test.Utilities, ABC.X, n1, N1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.552 IQR)
- **Top Global Matches:** file_cluster_8: 12.552, file_cluster_0: 12.957, file_cluster_7: 13.033
- **Magnitude:** 4973.44 | **LOC:** 12119 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.7761%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `StringSwitch_HashTableSwitch_02` (Impact: 273.9)
  * `NullableAsSwitchExpression_02` (Impact: 141.1)
  * `MultipleSwitchSectionsWithGotoCase` (Impact: 102.3)
  * `NotDegenerateSwitch006` (Impact: 80.2)
  * `NullableEnumTypeSwitchArgumentExpression` (Impact: 69.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1041`, `structural_boundaries: 864`, `args: 444`, `func_start: 863`, `class_start: 124`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 12`, `state_mutation: 1695`, `dead_code: 9`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 90`
* *Architecture:* `api: 318`, `import: 27`
* *Defense:* `safety: 114`, `doc: 9`, `test: 68`, `immutability_locks: 74`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Text, Microsoft.CodeAnalysis.Test.Utilities, System.Threading.Tasks, Microsoft.CodeAnalysis.CodeGen, Xunit, Microsoft.CodeAnalysis.CSharp.Test.Utilities, System.Linq, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Features/CSharpTest/EditAndContinue/StatementEditingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.865 IQR)
- **Top Global Matches:** file_cluster_8: 11.865, file_cluster_0: 12.001, file_cluster_13: 12.02
- **Magnitude:** 4963.38 | **LOC:** 14794 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.0465%), Tech Debt (99.6272%)
**Top Internal Functions/Classes:**
  * `Switch1` (Impact: 63.4)
    * *Intent:* #endregion #region Switch Statement
  * `ForEach1` (Impact: 46.0)
    * *Intent:* #endregion #region ForEach Statement
  * `Do1` (Impact: 43.1)
    * *Intent:* #endregion #region Do Statement
  * `Switch_Case_Reorder` (Impact: 43.0)
  * `VarPattern_Update` (Impact: 39.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 844`, `structural_boundaries: 4996`, `args: 2333`, `func_start: 2289`, `class_start: 530`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 220`, `planned_debt: 2`, `duplicate_logic: 79`, `orphaned_logic: 428`
* *Architecture:* `io: 1`, `api: 560`, `concurrency: 329`, `import: 557`
* *Defense:* `safety: 267`, `doc: 6`, `test: 443`, `sync_locks: 16`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.EditAndContinue.UnitTests, System.Threading.Tasks, Roslyn.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests, Xunit, Microsoft.CodeAnalysis.Emit, System.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Workspaces/CSharpTest/Formatting/FormattingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.135 IQR)
- **Top Global Matches:** file_cluster_8: 12.135, file_cluster_0: 12.327, file_cluster_4: 12.478
- **Magnitude:** 4908.92 | **LOC:** 12767 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 73.3%
- **Risk Profile:** Cognitive Load (27.6192%), Tech Debt (99.8496%)
**Top Internal Functions/Classes:**
  * `TestWrappingNonDefault` (Impact: 60.6)
  * `TestWrappingNonDefault_FormatBlock` (Impact: 60.0)
  * `TestWrappingNonDefault_FormatStatmtMethD` (Impact: 59.8)
  * `TestWrappingDefault` (Impact: 53.5)
  * `IndentUserSettingNonDefaultTest` (Impact: 46.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 736`, `structural_boundaries: 2313`, `args: 1379`, `func_start: 1528`, `class_start: 885`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 28`, `state_mutation: 409`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 8`, `duplicate_logic: 130`, `orphaned_logic: 354`
* *Architecture:* `api: 703`, `concurrency: 874`, `import: 67`
* *Defense:* `safety: 177`, `doc: 16`, `test: 211`, `sync_locks: 16`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` System.Collections.Generic, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.CSharp.Formatting.CSharpFormattingOptions2, System.Threading.Tasks, System.Data, Microsoft.CodeAnalysis.Formatting, System.Threading, Microsoft.CodeAnalysis.CSharp.Shared.Extensions...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.382 IQR)
- **Top Global Matches:** file_cluster_0: 13.382, file_cluster_4: 13.424, file_cluster_11: 13.682
- **Magnitude:** 4792.22 | **LOC:** 22795 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.1561%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AssertParameterScope` (Impact: 95.4)
  * `Handle` (Impact: 74.9)
  * `Handle` (Impact: 74.3)
  * `Handle11` (Impact: 74.3)
  * `Handle` (Impact: 58.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 2011`, `args: 764`, `func_start: 2093`, `class_start: 242`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 812`, `dead_code: 55`, `duplicate_logic: 97`, `orphaned_logic: 148`
* *Architecture:* `api: 695`, `concurrency: 804`, `import: 44`
* *Defense:* `safety: 273`, `doc: 91`, `test: 1092`, `sync_locks: 134`, `immutability_locks: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` PrimaryConstructorTests.TestFlags, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Diagnostics, System.Runtime.CompilerServices, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.CSharp.Symbols...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Analyzers/CSharp/Tests/RemoveUnusedParametersAndValues/RemoveUnusedValueAssignmentTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.072 IQR)
- **Top Global Matches:** file_cluster_0: 13.072, file_cluster_8: 13.193, file_cluster_4: 13.278
- **Magnitude:** 4415.7 | **LOC:** 9496 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (53.4371%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `RemoveUnusedValueAssignmentTests` (Impact: 136.1)
  * `IfElse_OverwrittenInAllControlFlowPaths` (Impact: 42.5)
    * *Intent:* // Simple if-else.
  * `IfElse_OverwrittenInCondition_LogicalOpe` (Impact: 38.4)
  * `FixAll_MoveMultipleVariableDeclarations_` (Impact: 32.1)
  * `FixAll_MoveMultipleVariableDeclarations_` (Impact: 32.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 1764`, `args: 1224`, `func_start: 1238`, `class_start: 473`
* *Risk/State:* `state_mutation: 1163`, `duplicate_logic: 84`, `orphaned_logic: 222`
* *Architecture:* `io: 2`, `api: 404`, `concurrency: 605`, `import: 164`
* *Defense:* `safety: 384`, `test: 190`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.CodeAnalysis.CSharp.CodeStyle, Roslyn.Test.Utilities.TestHelpers, Microsoft.CodeAnalysis.CSharp.RemoveUnusedParametersAndValues, Microsoft.CodeAnalysis.Test.Utilities, System, CSharpCodeFixVerifier, System.Threading.Tasks, Microsoft.CodeAnalysis.Testing...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.074 IQR)
- **Top Global Matches:** file_cluster_8: 14.074, file_cluster_11: 14.196, file_cluster_13: 14.214
- **Magnitude:** 4378.6 | **LOC:** 11842 | **CtrlFlow:** 55.3% | **Authorship Centralization:** 20.0%
- **Risk Profile:** Cognitive Load (38.6876%), Tech Debt (98.4158%)
**Top Internal Functions/Classes:**
  * `BindArgList` (Impact: 367.5)
  * `BindConstructorInitializerCore` (Impact: 217.9)
  * `ResolveExtension` (Impact: 208.4)
    * *Intent:* // SPEC begins // // An array-creation-expression is used to create a new instance of an array-type....
  * `BindConstructorInitializerCoreContinued` (Impact: 101.5)
  * `tryResolveExtensionInScope` (Impact: 101.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 746`, `structural_boundaries: 604`, `args: 206`, `func_start: 784`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 962`, `dead_code: 23`, `planned_debt: 3`, `duplicate_logic: 48`, `orphaned_logic: 65`
* *Architecture:* `api: 33`, `import: 15`
* *Defense:* `safety: 187`, `doc: 179`, `immutability_locks: 74`, `cleanup: 68`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.Text, System.Runtime.CompilerServices, Roslyn.Utilities, Microsoft.CodeAnalysis.CSharp.Symbols, System.Reflection, Microsoft.CodeAnalysis.Collections, System.Diagnostics, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Features/CSharpTest/EditAndContinue/TopLevelEditingTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.654 IQR)
- **Top Global Matches:** file_cluster_8: 10.654, file_cluster_0: 10.692, file_cluster_13: 11.095
- **Magnitude:** 4214.96 | **LOC:** 26413 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (8.0951%), Tech Debt (99.9825%)
**Top Internal Functions/Classes:**
  * `Using_Insert_CreatesAmbiguousCode` (Impact: 9.2)
  * `Record_Property_Delete_ReplacingCustomWi` (Impact: 9.0)
  * `Method_Update_Type` (Impact: 8.7)
  * `Method_Update_Parameter_Type_WithRename` (Impact: 8.5)
  * `Record_Method_Delete_ReplacingSynthesize` (Impact: 8.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 5959`, `args: 2371`, `func_start: 2891`, `class_start: 340`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 2`, `state_mutation: 358`, `planned_debt: 13`, `duplicate_logic: 148`, `orphaned_logic: 474`
* *Architecture:* `api: 1399`, `concurrency: 93`, `import: 208`
* *Defense:* `safety: 15`, `doc: 6`, `test: 617`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Timers, Microsoft.CodeAnalysis.EditAndContinue, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.CSharp.Syntax, System.Diagnostics, string, Microsoft.CodeAnalysis.CSharp.Symbols, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/ParamsCollectionTests.cs` (CSHARP | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.295 IQR)
- **Top Global Matches:** file_cluster_0: 12.295, file_cluster_13: 12.471, file_cluster_8: 12.487
- **Magnitude:** 4166.92 | **LOC:** 17089 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 75.0%
- **Risk Profile:** Cognitive Load (11.0932%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `VerifyParameterRefSafetyScope` (Impact: 53.5)
  * `UsingPatternWithParamsTest_Foreach` (Impact: 31.5)
  * `StringInterpolation_01` (Impact: 28.6)
  * `VerifyAttributeEmbedding` (Impact: 26.7)
  * `assertAttributes` (Impact: 23.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 2503`, `args: 1552`, `func_start: 3312`, `class_start: 622`
* *Risk/State:* `safety_bypasses: 121`, `state_mutation: 578`, `dead_code: 150`, `duplicate_logic: 60`, `orphaned_logic: 252`
* *Architecture:* `api: 1129`, `concurrency: 120`, `import: 362`
* *Defense:* `safety: 62`, `test: 434`, `immutability_locks: 28`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Test.Utilities, System.Runtime.CompilerServices, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.PooledObjects, System.Linq.Expressions, Microsoft.CodeAnalysis.CSharp.Symbols, Program, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/LanguageServer/Protocol/Protocol/SignatureHelp.cs` (CSHARP) | Magnitude: 22.54 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 41, indent_spaces: 21, decorators: 6, api: 4
- `src/Tools/IdeCoreBenchmarks/SegmentedListBenchmarks_InsertRange.cs` (CSHARP) | Magnitude: 0.05 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 66, state_mutation: 17, structural_boundaries: 13, func_start: 13
- `src/Compilers/Core/CodeAnalysisTest/Collections/ImmutableSegmentedHashSetTest.cs` (CSHARP) | Magnitude: 77.78 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 168, func_start: 68, test: 50, sec_high_risk_execution: 48
- `src/EditorFeatures/CSharpTest/Completion/CompletionProviders/LoadDirectiveCompletionProviderTests.cs` (CSHARP) | Magnitude: 29.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 27, decorators: 20, import: 12
- `src/Features/Core/Portable/Testing/TestFrameworks/XUnitTestFrameworkMetadata.cs` (CSHARP) | Magnitude: 14.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, branch: 3, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/VisualStudio/Core/Impl/SolutionExplorer/DiagnosticItem/CpsUtilities.cs` (CSHARP) | Magnitude: 22.52 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 20, doc: 19, structural_boundaries: 7, state_mutation: 6
- `src/Workspaces/Core/Portable/Workspace/Host/SourceFiles/IDynamicFileInfoProvider.cs` (CSHARP) | Magnitude: 24.0 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 13, structural_boundaries: 5, import: 3, indent_spaces: 3
- `src/Features/Core/Portable/ExternalAccess/UnitTesting/SolutionCrawler/UnitTestingSolutionCrawlerProgressReporter.cs` (CSHARP) | Magnitude: 20.38 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 12, structural_boundaries: 8, doc: 7, api: 5
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/Rules/AbstractFormattingRule.cs` (CSHARP) | Magnitude: 23.52 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 23, indent_spaces: 14, structural_boundaries: 11, api: 8
- `src/EditorFeatures/Core/EditAndContinue/IEditAndContinueSolutionProvider.cs` (CSHARP) | Magnitude: 14.64 | Delta: **0.102 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, class_start: 1, api: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Features/Core/Portable/InlineMethod/AbstractInlineMethodRefactoringProvider.cs` (CSHARP) | Magnitude: 137.58 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 152, structural_boundaries: 63, branch: 35, dead_code: 27
- `src/Compilers/CSharp/Portable/Syntax/TryStatementSyntax.cs` (CSHARP) | Magnitude: 35.3 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 12, branch: 8, structural_boundaries: 8, safety: 6
- `eng/common/generate-sbom-prep.sh` (SHELL) | Magnitude: 45.28 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 24, structural_boundaries: 18, branch: 14, safety_bypasses: 9
- `scripts/crossgen.sh` (SHELL) | Magnitude: 4.14 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: state_mutation: 21, branch: 14, io: 9, structural_boundaries: 8
- `eng/common/dotnet-install.sh` (SHELL) | Magnitude: 114.48 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 72, indent_spaces: 47, branch: 28, structural_boundaries: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/Compilers/Core/Portable/Emit/AnonymousDelegateWithIndexedNamePartialKey.cs` (CSHARP) | Magnitude: 16.7 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 3, doc: 3, args: 1, func_start: 1
- `eng/common/native/init-distro-rid.sh` (SHELL) | Magnitude: 173.74 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 81, indent_spaces: 60, branch: 58, reflection_metaprogramming: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Compilers/CSharp/Portable/Binder/SimpleProgramBinder.cs` (CSHARP) | Magnitude: 59.62 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 18, branch: 12, func_start: 12
- `src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedEnumValueFieldSymbol.cs` (CSHARP) | Magnitude: 15.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, api: 7, args: 5
- `src/Compilers/Core/Portable/SourceGeneration/Nodes/TransformNode.cs` (CSHARP) | Magnitude: 57.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 24, generics: 19, branch: 12
- `src/Features/Core/Portable/ChangeSignature/ParameterConfiguration.cs` (CSHARP) | Magnitude: 78.76 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 55, state_mutation: 18, structural_boundaries: 14, func_start: 11
- `src/LanguageServer/Microsoft.CommonLanguageServerProtocol.Framework.Example/ExampleLspServices.cs` (CSHARP) | Magnitude: 35.28 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 15, generics: 12, state_mutation: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `eng/common/pipeline-logging-functions.ps1` (POWERSHELL) | Magnitude: 43.48 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 26, indent_spaces: 20, sec_high_risk_execution: 10, closures: 6
- `src/Workspaces/Core/Portable/CodeRefactorings/FixAllOccurences/RefactorAllScope.cs` (CSHARP) | Magnitude: 22.92 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 26, doc: 24, args: 19
- `src/Compilers/CSharp/Portable/Symbols/NullableAnnotationExtensions.cs` (CSHARP) | Magnitude: 80.84 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 91, structural_boundaries: 42, args: 34, func_start: 28
- `eng/common/init-tools-native.ps1` (POWERSHELL) | Magnitude: 167.82 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 124, branch: 47, closures: 27
- `src/Compilers/CSharp/Portable/Symbols/Synthesized/SynthesizedPropertySymbol.cs` (CSHARP) | Magnitude: 114.96 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 94, structural_boundaries: 74, args: 70, api: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxTriviaListTests.cs` (CSHARP) | Magnitude: 108.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 176, func_start: 114, test: 99, sec_high_risk_execution: 96
- `src/Dependencies/Collections/Specialized/SpecializedCollections.Empty.List.cs` (CSHARP) | Magnitude: 20.56 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 9, api: 9, generics: 8
- `src/Workspaces/Core/Portable/Workspace/Host/DocumentService/Extensions.cs` (CSHARP) | Magnitude: 54.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 15, safety: 12, branch: 11, structural_boundaries: 10
- `src/Workspaces/CoreTest/WorkspaceServiceTests/ReferenceCountedDisposableTests.cs` (CSHARP) | Magnitude: 60.54 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 130, func_start: 51, structural_boundaries: 43, test: 43
- `src/LanguageServer/Protocol/Protocol/WorkspaceDiagnosticParams.cs` (CSHARP) | Magnitude: 24.52 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 24, indent_spaces: 19, decorators: 7, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `eng/common/vmr-sync.sh` (SHELL) | Magnitude: 208.18 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 89, indent_spaces: 83, branch: 74, structural_boundaries: 35
- `src/Features/Core/Portable/InvertIf/AbstractInvertIfCodeRefactoringProvider.cs` (CSHARP) | Magnitude: 291.66 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 491, structural_boundaries: 175, func_start: 83, state_mutation: 55
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/SymbolKey/SymbolKey.MethodSymbolKey.cs` (CSHARP) | Magnitude: 172.64 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 155, state_mutation: 62, structural_boundaries: 45, branch: 40
- `src/VisualStudio/Core/Test.Next/Options/VisualStudioOptionStorageTests.cs` (CSHARP) | Magnitude: 113.56 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 230, structural_boundaries: 69, dead_code: 32, func_start: 30
- `src/Scripting/CoreTest.Desktop/GlobalAssemblyCacheTests.cs` (CSHARP) | Magnitude: 54.52 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 84, sec_high_risk_execution: 39, func_start: 29, test: 27

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Scripting/CoreTestUtilities/ScriptTaskExtensions.cs` (CSHARP) | Magnitude: 33.62 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 20, concurrency: 16, ui_framework: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Features/CSharp/Portable/Completion/CSharpCompletionService.cs` (CSHARP) | Magnitude: 43.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 24, import: 11, concurrency: 9
- `src/LanguageServer/ProtocolUnitTests/Ordering/MutatingRequestHandler.cs` (CSHARP) | Magnitude: 26.24 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 19, concurrency: 14, structural_boundaries: 13, api: 6
- `src/VisualStudio/Core/Def/ValueTracking/ValueTrackingToolWindow.cs` (CSHARP) | Magnitude: 48.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, state_mutation: 18, structural_boundaries: 13, concurrency: 12
- `src/EditorFeatures/Core/Interactive/IResettableInteractiveEvaluator.cs` (CSHARP) | Magnitude: 27.86 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: concurrency: 6, structural_boundaries: 5, import: 3, immutability_locks: 2
- `src/Analyzers/Core/CodeFixes/UpgradeProject/AbstractUpgradeProjectCodeFixProvider.cs` (CSHARP) | Magnitude: 101.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 45, concurrency: 31, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/SoftCrashException.cs` (CSHARP) | Magnitude: 18.66 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 20, api: 7, args: 6, func_start: 6
- `src/VisualStudio/Core/Def/Interop/WrapperPolicy.cs` (CSHARP) | Magnitude: 15.38 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, structural_boundaries: 9, doc: 8, api: 4
- `src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/UnitTests/InternalImplementationOnlyTests.cs` (CSHARP) | Magnitude: 173.94 | Delta: **0.094 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 467, func_start: 228, planned_debt: 218, concurrency: 66
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/IReferenceCountedDisposable.cs` (CSHARP) | Magnitude: 20.82 | Delta: **0.165 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 28, structural_boundaries: 4, indent_spaces: 3, generics: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Features/Core/Portable/ChangeSignature/CallSiteKind.cs` (CSHARP) | Magnitude: 16.2 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 24, indent_spaces: 5, structural_boundaries: 2, class_start: 1
- `src/Workspaces/Core/Portable/CodeFixes/FixAllOccurrences/WellKnownFixAllProviders.cs` (CSHARP) | Magnitude: 15.64 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 16, structural_boundaries: 4, api: 2, args: 1
- `src/Features/Core/Portable/Copilot/ImplementationDetails.cs` (CSHARP) | Magnitude: 16.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, api: 3, immutability_locks: 2
- `src/Features/ExternalAccess/Copilot/GenerateImplementation/ImplementationDetailsWrapper.cs` (CSHARP) | Magnitude: 16.64 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 4, api: 3, immutability_locks: 2
- `src/RoslynAnalyzers/Utilities/Compiler/Options/ValueUsageInfo.cs` (CSHARP) | Magnitude: 26.42 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 36, indent_spaces: 24, state_mutation: 9, structural_boundaries: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/Compilers/CSharp/Portable/Binder/CatchClauseBinder.cs` (CSHARP) | Magnitude: 27.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 13, func_start: 10, import: 6
- `src/Compilers/CSharp/Portable/BoundTree/BoundNewT.cs` (CSHARP) | Magnitude: 22.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 10, args: 7, api: 7
- `src/Compilers/CSharp/Portable/BoundTree/BoundNoPiaObjectCreationExpression.cs` (CSHARP) | Magnitude: 22.32 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 10, args: 7, api: 7
- `src/Compilers/Core/Portable/Emit/Context.cs` (CSHARP) | Magnitude: 41.94 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 56, state_mutation: 16, api: 12, structural_boundaries: 10
- `src/EditorFeatures/Core/Shared/Tagging/EventSources/AbstractWorkspaceTrackingTaggerEventSource.cs` (CSHARP) | Magnitude: 32.06 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 40, func_start: 10, state_mutation: 10, encapsulation: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/RoslynAnalyzers/Utilities/FlowAnalysis/Options/EditorConfigOptionNames_FlowAnalysis.cs` (CSHARP) | Magnitude: 24.34 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 47, indent_spaces: 13, api: 9, immutability_locks: 8
- `src/Workspaces/Core/Portable/Workspace/Host/SourceFiles/DynamicFileInfo.cs` (CSHARP) | Magnitude: 10.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 22, api: 6, indent_spaces: 5, dead_code: 3
- `src/EditorFeatures/Core/Tagging/TaggerDelay.cs` (CSHARP) | Magnitude: 16.22 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 31, indent_spaces: 6, structural_boundaries: 2, dead_code: 2
- `src/Features/CSharp/Portable/Completion/KeywordRecommenders/UsingKeywordRecommender.cs` (CSHARP) | Magnitude: 31.54 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, dead_code: 11, func_start: 6
- `src/Compilers/CSharp/Portable/Symbols/Synthesized/Records/SynthesizedRecordEqualityOperator.cs` (CSHARP) | Magnitude: 38.98 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, doc: 18, state_mutation: 10, branch: 8

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Workspaces/Remote/ServiceHub/Services/DiagnosticAnalyzer/RemoteDiagnosticAnalyzerService.cs` -> Churn: **77.74%** | Cog Load: 57.6867% | Debt: 81.7574%
- `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` -> Churn: **75.2%** | Cog Load: 38.6876% | Debt: 98.4158%
- `src/Compilers/CSharp/Portable/Errors/ErrorCode.cs` -> Churn: **73.74%** | Cog Load: 57.1805% | Debt: 0.0%
- `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs` -> Churn: **73.74%** | Cog Load: 56.6978% | Debt: 16.9306%
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/FileBasedPrograms/FileBasedProgramsProjectSystem.cs` -> Churn: **72.45%** | Cog Load: 52.3831% | Debt: 82.6484%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` -> **DoctorKrolic** (100.0% isolated ownership) | Magnitude: 17094.18
- `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` -> **AlekseyTs** (100.0% isolated ownership) | Magnitude: 10244.46
- `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` -> **Julien Couvreur** (100.0% isolated ownership) | Magnitude: 5336.56
- `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` -> **Fred Silberberg** (100.0% isolated ownership) | Magnitude: 4973.44
- `src/Features/CSharpTest/EditAndContinue/StatementEditingTests.cs` -> **Tomáš Matoušek** (100.0% isolated ownership) | Magnitude: 4963.38

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 10652.329** (Blast Radius: 144.534 * Doc Risk: 73.7012%)
- `src/Compilers/CSharp/Portable/BoundTree/Formatting.cs` -> **Severity: 1447.737** (Blast Radius: 14.513 * Doc Risk: 99.7545%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs` -> **Severity: 1344.865** (Blast Radius: 23.069 * Doc Risk: 58.2975%)
- `src/Compilers/Core/Portable/MetadataReference/Metadata.cs` -> **Severity: 534.308** (Blast Radius: 9.182 * Doc Risk: 58.1908%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Completion.cs` -> **Severity: 407.635** (Blast Radius: 6.152 * Doc Risk: 66.2605%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
