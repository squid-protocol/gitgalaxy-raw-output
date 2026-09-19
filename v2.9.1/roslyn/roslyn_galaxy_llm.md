# ARCHITECTURAL_BRIEF: roslyn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dotnet/roslyn` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 14431 analyzed artifact(s), 4079813 LOC.
- **Load-bearing artifact:** `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -- 3120 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Workspaces/CSharpTest/OrganizeImports/OrganizeUsingsTests.cs` -- pulls in 103 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` at magnitude 637131.05 (structural weight, not risk).
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
| Total Artifacts | 20641 |
| Analyzed Artifacts (Scanned) | 14431 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6210 |
| Total LOC | 4079813 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 69.9% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5748 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2383 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.1096 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 134 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 13926 | 4064776 | 96.5% |
| PLAINTEXT | 222 | 1418 | 1.5% |
| MARKDOWN | 85 | 0 | 0.6% |
| YAML | 62 | 3198 | 0.4% |
| POWERSHELL | 49 | 6765 | 0.3% |
| XML | 25 | 0 | 0.2% |
| SHELL | 25 | 2288 | 0.2% |
| BATCH | 22 | 151 | 0.2% |
| JSON | 13 | 911 | 0.1% |
| PYTHON | 1 | 251 | 0.0% |
| CSV | 1 | 55 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled Monorepo`
> **Architectural Drift Z-Score:** `5.16`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +5.16; from the repo's file-archetype mix)
> **File Composition:** Encapsulated Accessors Files 22%, Declarative / Non-Code 19%, Callbacks & Closures Files 10%, Large Core Modules (3) 9%, Data / Markup / Trivial 7%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14123 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 306 | 2.1% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6210*

**Composition by Extension & Reason:**
- `.vb`: 3642x Unsupported Format (.vb), 1x Excluded (Machine-Generated Source Code Signature: 14598 LOC), 1x Excluded (Monolithic Amalgamation: 58132 LOC exceeds safe regex boundaries)
- `.xlf`: 913x Unsupported Format (.xlf), 4x Excluded (Saturation: Line 33 exceeds 500 chars), 3x Excluded (Saturation: Line 96 exceeds 500 chars)
- `.csproj`: 300x Unsupported Format (.csproj), 1x Excluded (Unsupported Extension: '.csproj')
- `.md`: 252x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dll`: 138x Excluded (Explicitly Denied Extension: '.dll'), 6x Excluded (Explicitly Denied Extension: '.Dll')
- `.png`: 70x Excluded (Explicitly Denied Extension: '.png')
- `.resx`: 70x Unsupported Format (.resx)
- `.cs`: 32x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 80 exceeds 500 chars), 1x Excluded (Machine-Generated Source Code Signature: 17743 LOC)
- `no_extension`: 24x Unsupported Format (.undeterminable), 16x Unsupported Format (.vsixmanifest), 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xaml`: 60x Unsupported Format (.xaml)
- `.json`: 58x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 75861 LOC exceeds safe regex boundaries)
- `.yml`: 54x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 68 exceeds 500 chars), 1x Zero-Density Threshold (LOC: 60, Signals: 0)
- `.props`: 31x Unsupported Format (.props), 13x Excluded (Unsupported Extension: '.props'), 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vbproj`: 51x Unsupported Format (.vbproj)
- `.targets`: 21x Unsupported Format (.targets), 19x Excluded (Unsupported Extension: '.targets'), 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 14.6 | 6.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 32.5 | 42.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 40.5 | 39.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.3 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 4.6 | 1.8 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.8 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 15.3 | 1.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 71024 | 3722 | 3 | `src/Compilers/CSharp/Test/Semantic/Semantics/NativeIntegerTests.cs` |
| cleanup | 3843 | 1051 | 0 | `src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/LocalsTests.cs` |
| guards | 256364 | 13211 | 36 | `src/Compilers/CSharp/Test/Syntax/Parsing/ParsingErrorRecoveryTests.cs` |
| danger | 34032 | 3602 | 3 | `src/Compilers/CSharp/Test/WinRT/Metadata/WinMdEventTests.cs` |
| concurrency | 112210 | 4326 | 14 | `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` |
| connectivity | 283618 | 13909 | 31 | `src/Compilers/CSharp/Test/Symbol/Symbols/SymbolErrorTests.cs` |
| io | 3822 | 591 | 0 | `src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 66 | 34 | 0 | `src/Compilers/Shared/NamedPipeUtil.cs` |
| time | 865 | 264 | 0 | `src/Compilers/CSharp/Test/Semantic/SourceGeneration/StateTableTests.cs` |
| serialization | 104 | 51 | 0 | `src/Compilers/CSharp/Test/Semantic/Semantics/DynamicTests.cs` |
| regex | 301 | 71 | 0 | `.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1` |
| events | 14848 | 1462 | 1 | `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` |
| tests | 151684 | 2353 | 11 | `src/Compilers/CSharp/Test/Symbol/Compilation/SemanticModelGetSemanticInfoTests.cs` |
| docs | 125283 | 5810 | 20 | `src/Compilers/CSharp/Portable/Compilation/CSharpSemanticModel.cs` |
| debt | 39803 | 1970 | 1 | `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` |
| mutation | 645217 | 11197 | 81 | `src/Features/CSharpTest/EditAndContinue/TopLevelEditingTests.cs` |
| dead_code | 130014 | 10183 | 15 | `src/Compilers/CSharp/Test/Symbol/Symbols/SymbolErrorTests.cs` |
| credential | 465 | 67 | 0 | `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenReadOnlySpanConstructionTest.cs` |
| threat | 4625 | 1272 | 0 | `src/Compilers/CSharp/Test/Emit3/Attributes/InternalsVisibleToAndStrongNameTests.cs` |
| ml_ai | 1122 | 377 | 0 | `src/Compilers/CSharp/Portable/Parser/QuickScanner.cs` |
| ui | 64 | 31 | 0 | `src/VisualStudio/Core/Impl/Options/AbstractOptionPageControl.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs` (Hits: 377)
- `eng/common/SetupNugetSources.sh` (Hits: 76)
- `src/EditorFeatures/CSharpTest/PdbSourceDocument/ImplementationAssemblyLookupServiceTests.cs` (Hits: 61)

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

- `IsBuildOnlyDiagnostic` **(Compute Cores)** (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **1328.5** | LOC: 917
  * *Intent:* /// <summary> /// Returns true if this is a build-only diagnostic that is never reported from /// <see cref="SemanticModel.GetDiagnostics(Text.TextSpa...
- `Parse` **(Many-Argument Workhorses)** (@ `src/Compilers/CSharp/Portable/CommandLine/CSharpCommandLineParser.cs`) -> Impact: **1039.1** | LOC: 1150
  * *Intent:* /// <summary> /// Parses a command line. /// </summary> /// <param name="args">A collection of strings representing the command line arguments.</param...
- `VisitConversion` **(Many-Argument Workhorses)** (@ `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`) -> Impact: **867.3** | LOC: 620
  * *Intent:* /// If <see langword="true"/>, the incoming conversion is assumed to be from binding /// and will be re-calculated, this time considering nullability....
- `AnalyzeSemanticsAsync` **(Many-Argument Workhorses)** (@ `src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs`) -> Impact: **838.2** | LOC: 1013
- `GetFlowGraph` **(Many-Argument Workhorses)** (@ `src/Compilers/Test/Core/Compilation/ControlFlowGraphVerifier.cs`) -> Impact: **620.5** | LOC: 1039
- `MakeBinaryOperator` **(Many-Argument Workhorses)** (@ `src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_BinaryOperator.cs`) -> Impact: **557.8** | LOC: 348
- `GetWarningLevel` **(Compute Cores)** (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **508.5** | LOC: 384
- `IsWarning` **(Compute Cores)** (@ `src/Compilers/CSharp/Portable/Generated/ErrorFacts.Generated.cs`) -> Impact: **505.5** | LOC: 351
- `EmitNumericConversion` **(Many-Argument Workhorses)** (@ `src/Compilers/Core/Portable/CodeGen/ILBuilderConversions.cs`) -> Impact: **501.1** | LOC: 343
- `DoUncheckedConversion` **(Compute Cores)** (@ `src/Compilers/CSharp/Portable/Binder/Binder_Conversions.cs`) -> Impact: **408.3** | LOC: 302

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/Compilers/CSharp/Test/Emit3` | 7 | 646401.71 | 21.28% | 0.0% |
| `src/Compilers/CSharp/Test/Emit/CodeGen` | 72 | 510467.64 | 18.91% | 0.0% |
| `src/Compilers/CSharp/Test/Emit3/Semantics` | 21 | 226061.96 | 15.96% | 0.0% |
| `src/Compilers/CSharp/Test/Semantic/Semantics` | 106 | 103069.49 | 14.63% | 0.0% |
| `src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue` | 10 | 95225.92 | 6.91% | 0.0% |
| `src/Compilers/CSharp/Test/Emit2/PDB` | 17 | 83812.28 | 10.21% | 0.0% |
| `src/Compilers/CSharp/Test/Emit2/CodeGen` | 4 | 77886.66 | 7.04% | 0.0% |
| `src/Compilers/CSharp/Portable/Binder` | 117 | 54355.74 | 23.86% | 44.13% |
| `src/EditorFeatures/CSharpTest/Classification` | 12 | 38591.78 | 15.03% | 74.13% |
| `src/Compilers/CSharp/Test/Syntax/Parsing` | 69 | 30404.0 | 5.46% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Compilers/CSharp/Portable/Binder/Binder.QueryUnboundLambdaState.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Portable/Binder/SafeContext.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Portable/Lowering/Instrumentation/CompoundInstrumenter.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Portable/Symbols/Source/SynthesizedSourceOrdinaryMethodSymbol.cs` -> **100.0%** Exposure
- `src/Compilers/CSharp/Portable/Symbols/SymbolVisitor.cs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/skills/ci-analysis/scripts/Get-CIStatus.ps1` -> **100.0%** Exposure
- `.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.ps1` -> **100.0%** Exposure
- `eng/common/darc-init.ps1` -> **100.0%** Exposure
- `eng/common/dotnet-install.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Features/CSharpTest/EditAndContinue/TopLevelEditingTests.cs` -> **1055** Orphaned Functions | **0** Duplicates
- `src/Compilers/CSharp/Test/Semantic/Semantics/SemanticErrorTests.cs` -> **777** Orphaned Functions | **0** Duplicates
- `src/Compilers/CSharp/Test/Symbol/Symbols/SymbolErrorTests.cs` -> **681** Orphaned Functions | **0** Duplicates
- `src/EditorFeatures/CSharpTest/Completion/CompletionProviders/SymbolCompletionProviderTests.cs` -> **558** Orphaned Functions | **115** Duplicates
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleTest.cs` -> **601** Orphaned Functions | **9** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `69` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `84133` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 637131.05 | **LOC:** 29709 | **CtrlFlow:** 4.7% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (46.5%), Guard Balance (formerly Safety Score) (44.3%), Connectivity (formerly Api Exposure) (13.0%), Dead Code Surface (formerly Dead Code) (12.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 21 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 154 instances
* *Concurrency (weighted view):* 590
* *Memory Alloc (weighted view):* 910
* *State Mutation (weighted view):* 805
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1193`, `structural_boundaries: 5464`, `args: 2705`, `func_start: 2331`, `class_start: 1169`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 497`, `dead_code: 228`, `planned_debt: 21`
* *Architecture:* `api: 1445`, `concurrency: 540`, `import: 292`
* *Defense:* `safety: 419`, `test: 1010`, `immutability_locks: 82`, `cleanup: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Helper, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 228406.74 | **LOC:** 12119 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.2%), Connectivity (formerly Api Exposure) (11.7%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (11.0%), Complexity Load (formerly Cognitive Load) (10.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 173 instances
* *State Mutation (weighted view):* 592
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1013`, `structural_boundaries: 872`, `args: 476`, `func_start: 374`, `class_start: 125`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 246`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `api: 314`, `import: 27`
* *Defense:* `safety: 114`, `doc: 9`, `test: 69`, `immutability_locks: 77`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CodeGen, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections.Generic, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncIteratorTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 196424.78 | **LOC:** 11935 | **CtrlFlow:** 6.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (68.5%), Guard Balance (formerly Safety Score) (44.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (18.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 218 instances
* *Amplified Cascading Flux:* 93 instances
* *Concurrency (weighted view):* 2688
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 675`, `structural_boundaries: 2602`, `args: 767`, `func_start: 627`, `class_start: 273`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 130`, `dead_code: 33`
* *Architecture:* `api: 475`, `concurrency: 1598`, `import: 341`
* *Defense:* `safety: 312`, `doc: 3`, `test: 168`, `sync_locks: 3`, `immutability_locks: 28`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.DynamicAnalysis.UnitTests, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests.CodeGen.Instruction, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/InlineArrayTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 178903.11 | **LOC:** 24201 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (87.0%), Guard Balance (formerly Safety Score) (53.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.3%), Complexity Load (formerly Cognitive Load) (13.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 98 instances
* *Amplified Cascading Flux:* 175 instances
* *Concurrency (weighted view):* 1010
* *State Mutation (weighted view):* 1026
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 386`, `structural_boundaries: 3575`, `args: 1815`, `func_start: 1684`, `class_start: 875`
* *Risk/State:* `safety_bypasses: 91`, `state_mutation: 676`, `dead_code: 199`
* *Architecture:* `api: 1203`, `concurrency: 520`, `import: 56`
* *Defense:* `safety: 112`, `test: 557`, `immutability_locks: 295`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/CodeGen/CodeGenLengthBasedSwitchTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 74812.1 | **LOC:** 14126 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.6%), Connectivity (formerly Api Exposure) (8.8%), Complexity Load (formerly Cognitive Load) (6.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 93
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 569`, `structural_boundaries: 707`, `args: 153`, `func_start: 121`, `class_start: 31`
* *Risk/State:* `state_mutation: 47`
* *Architecture:* `api: 91`, `import: 5`
* *Defense:* `safety: 21`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CodeGen, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, Xunit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/PDB/PDBTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 69154.22 | **LOC:** 12998 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.6%), Concurrency Surface (formerly Concurrency) (15.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (10.3%), Connectivity (formerly Api Exposure) (8.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 41 instances
* *Concurrency (weighted view):* 56
* *State Mutation (weighted view):* 183
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 267`, `structural_boundaries: 1494`, `args: 572`, `func_start: 464`, `class_start: 188`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 101`, `planned_debt: 3`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 320`, `concurrency: 36`, `import: 94`
* *Defense:* `safety: 108`, `doc: 27`, `test: 168`, `sync_locks: 4`, `immutability_locks: 63`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CodeGen, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.Text, Microsoft.DiaSymReader, Roslyn.Test.PdbUtilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 47510.34 | **LOC:** 22158 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (31.0%), Concurrency Surface (formerly Concurrency) (12.4%), Connectivity (formerly Api Exposure) (10.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 255
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 4255`, `args: 1863`, `func_start: 1002`, `class_start: 529`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 231`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `api: 407`, `concurrency: 12`, `import: 110`
* *Defense:* `safety: 59`, `doc: 96`, `test: 213`, `immutability_locks: 361`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests, Microsoft.CodeAnalysis.CodeGen, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueStateMachineTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 36883.55 | **LOC:** 11396 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (94.2%), Guard Balance (formerly Safety Score) (57.1%), Complexity Load (formerly Cognitive Load) (11.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.2%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 19 instances
* *Amplified Cascading Flux:* 29 instances
* *Concurrency (weighted view):* 635
* *State Mutation (weighted view):* 137
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 1744`, `args: 521`, `func_start: 502`, `class_start: 145`
* *Risk/State:* `safety_bypasses: 205`, `state_mutation: 79`, `dead_code: 3`
* *Architecture:* `api: 143`, `concurrency: 540`, `import: 193`
* *Defense:* `safety: 93`, `test: 64`, `sync_locks: 3`, `immutability_locks: 126`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/Classification/SyntacticClassifierTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 35379.5 | **LOC:** 6833 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (84.3%), Guard Balance (formerly Safety Score) (47.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.8%), Connectivity (formerly Api Exposure) (11.7%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 298
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 867`, `args: 760`, `func_start: 309`, `class_start: 123`
* *Risk/State:* `state_mutation: 36`
* *Architecture:* `api: 253`, `concurrency: 258`, `import: 21`
* *Defense:* `safety: 75`, `doc: 92`, `test: 1`, `sync_locks: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Classification, Microsoft.CodeAnalysis.Editor.UnitTests.Classification, Microsoft.CodeAnalysis.Editor.UnitTests.Classification.FormattedClassifications, Microsoft.CodeAnalysis.Remote.Testing, Microsoft.CodeAnalysis.Text, Roslyn.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 11777.56 | **LOC:** 4351 | **CtrlFlow:** 4.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Debt Markers (formerly Tech Debt) (51.2%), Mutation Surface (formerly State Flux) (44.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Main` **(Compute Cores)** (Impact: 267.9)
  * `Main` **(Compute Cores)** (Impact: 267.0)
  * `Main` **(Compute Cores)** (Impact: 266.8)
  * `Main` **(Compute Cores)** (Impact: 266.6)
  * `Main` **(Compute Cores)** (Impact: 265.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 889`, `args: 518`, `func_start: 494`, `class_start: 278`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 32`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 438`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 16`, `doc: 1`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.Editor.CSharp.CompleteStatement, Microsoft.CodeAnalysis.Editor.UnitTests.CompleteStatement, Microsoft.CodeAnalysis.Options, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.VisualStudio.Commanding, Roslyn.Test.Utilities, System, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/WinRT/CodeGen/WinRTCollectionTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 11165.04 | **LOC:** 7439 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.3%), Dead Code Surface (formerly Dead Code) (15.0%), Complexity Load (formerly Cognitive Load) (13.8%), Connectivity (formerly Api Exposure) (5.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 124 instances
* *State Mutation (weighted view):* 781
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 521`, `args: 169`, `func_start: 162`, `class_start: 28`
* *Risk/State:* `state_mutation: 533`, `dead_code: 72`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 57`, `import: 121`
* *Defense:* `safety: 83`, `test: 25`, `immutability_locks: 18`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 10277.52 | **LOC:** 14301 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 54.8%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (65.9%), Guard Balance (formerly Safety Score) (61.7%)
- **Documentation Coverage:** 91.3325% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisitConversion` **(Many-Argument Workhorses)** (Impact: 867.3)
    * *Intent:* /// If <see langword="true"/>, the incoming conversion is assumed to be from binding /// and will be...
  * `VisitArgumentsCore` **(Many-Argument Workhorses)** (Impact: 228.4)
  * `Scan` **(Defensive Guards)** (Impact: 183.1)
  * `visitArgumentsCore` **(Many-Argument Workhorses)** (Impact: 181.6)
  * `TrackNullableStateOfTupleConversion` **(Many-Argument Workhorses)** (Impact: 150.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 648 instances
* *State Mutation (weighted view):* 2209
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2099`, `structural_boundaries: 1745`, `args: 727`, `func_start: 600`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 913`, `dead_code: 24`, `planned_debt: 7`, `unreferenced_by_name: 142`
* *Architecture:* `api: 221`, `import: 14`
* *Defense:* `safety: 659`, `doc: 408`, `immutability_locks: 212`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Collections, Microsoft.CodeAnalysis.PooledObjects, Roslyn.Utilities, System, System.Collections.Concurrent, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/LockTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 10202.39 | **LOC:** 4851 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (15.1%), Connectivity (formerly Api Exposure) (13.1%), Dead Code Surface (formerly Dead Code) (10.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Memory Alloc (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 609`, `args: 282`, `func_start: 263`, `class_start: 133`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 40`, `dead_code: 22`
* *Architecture:* `api: 279`, `concurrency: 71`, `import: 84`
* *Defense:* `safety: 100`, `test: 78`, `sync_locks: 476`, `immutability_locks: 33`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections.Generic, System.Linq, System.Threading...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueClosureTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 9446.81 | **LOC:** 10499 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (15.7%), Connectivity (formerly Api Exposure) (11.5%), Complexity Load (formerly Cognitive Load) (5.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 1939`, `args: 927`, `func_start: 555`, `class_start: 199`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 48`
* *Architecture:* `api: 236`, `import: 229`
* *Defense:* `safety: 4`, `doc: 9`, `test: 82`, `immutability_locks: 78`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests, Microsoft.CodeAnalysis.CodeGen, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 9085.74 | **LOC:** 14680 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 54.2%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.1%), Complexity Load (formerly Cognitive Load) (65.2%)
- **Documentation Coverage:** 93.1238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseNamespaceBodyWorker` **(Many-Argument Workhorses)** (Impact: 183.3)
  * `ParseVariableDeclarator` **(Many-Argument Workhorses)** (Impact: 179.8)
  * `GetPrecedence` **(Compute Cores)** (Impact: 153.6)
  * `ParsePrimaryExpression` **(Compute Cores)** (Impact: 140.9)
  * `ParseMemberDeclarationOrStatementCore` **(Many-Argument Workhorses)** (Impact: 113.3)
    * *Intent:* /// <summary> /// Changes in this function around member parsing should be mirrored in <see cref="Pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 770 instances
* *State Mutation (weighted view):* 2577
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2694`, `structural_boundaries: 1882`, `args: 632`, `func_start: 474`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1037`, `dead_code: 54`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 47`, `import: 11`
* *Defense:* `safety: 278`, `doc: 187`, `immutability_locks: 17`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Syntax.InternalSyntax, Microsoft.CodeAnalysis.Text, Roslyn.Utilities, System, System.Collections.Generic, System.Diagnostics...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 8605.22 | **LOC:** 15189 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (57.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CompoundRightShiftWithAwait` **(I/O & Config Routines)** (Impact: 22.1)
  * `SpillArray03WithTaskAndRuntimeAsync` **(I/O & Config Routines)** (Impact: 22.0)
  * `CompoundRightShiftWithAwait_TypeParameter_Struct` **(I/O & Config Routines)** (Impact: 21.6)
  * `CompoundRightShiftWithAwait_TypeParameter_Unconstrained` **(I/O & Config Routines)** (Impact: 21.0)
  * `SpillManagedPointerAssign03WithTaskAndRuntimeAsync` **(I/O & Config Routines)** (Impact: 18.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 721 instances
* *Amplified Cascading Flux:* 230 instances
* *Concurrency (weighted view):* 5408
* *State Mutation (weighted view):* 1274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 186`, `structural_boundaries: 2026`, `args: 936`, `func_start: 783`, `class_start: 248`
* *Risk/State:* `safety_bypasses: 151`, `state_mutation: 814`, `dead_code: 5`, `unreferenced_by_name: 128`
* *Architecture:* `api: 591`, `concurrency: 1803`, `import: 300`
* *Defense:* `safety: 460`, `test: 113`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` C, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections, System.Collections.Generic, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8598.16 | **LOC:** 11842 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 18.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (77.5%), Guard Balance (formerly Safety Score) (72.0%)
- **Documentation Coverage:** 82.5352% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BindExpressionInternal` **(Many-Argument Workhorses)** (Impact: 275.1)
  * `bindExpressionInternal` **(Many-Argument Workhorses)** (Impact: 269.7)
  * `CheckAndCoerceArguments` **(Many-Argument Workhorses)** (Impact: 238.9)
    * *Intent:* #nullable enable
  * `ResolveExtension` **(Many-Argument Workhorses)** (Impact: 208.4)
    * *Intent:* #nullable enable
  * `BindMemberAccessWithBoundLeft` **(Many-Argument Workhorses)** (Impact: 144.6)
    * *Intent:* /// <remarks> /// If new checks are added to this method, they will also need to be added to /// <se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 614 instances
* *State Mutation (weighted view):* 2114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1732`, `structural_boundaries: 1222`, `args: 365`, `func_start: 311`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 886`, `dead_code: 28`, `planned_debt: 11`, `fragile_debt: 5`, `unreferenced_by_name: 18`
* *Architecture:* `api: 53`, `import: 15`
* *Defense:* `safety: 355`, `doc: 290`, `immutability_locks: 170`, `cleanup: 104`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Collections, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Text, Roslyn.Utilities, System...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 8023.04 | **LOC:** 24845 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (50.6%), Complexity Load (formerly Cognitive Load) (15.9%), Dead Code Surface (formerly Dead Code) (15.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NonBoxingUnionMatching_56_TryGetValue` **(Type Conversions)** (Impact: 59.0)
  * `NonBoxingUnionMatching_55_TryGetValue` **(Type Conversions)** (Impact: 54.6)
  * `NonBoxingUnionMatching_54_TryGetValue` **(Type Conversions)** (Impact: 48.1)
  * `NonBoxingUnionMatching_53_TryGetValue` **(Type Conversions)** (Impact: 42.4)
  * `Exhaustiveness_01` **(Callbacks & Closures)** (Impact: 39.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 536 instances
* *State Mutation (weighted view):* 2314
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1846`, `structural_boundaries: 4262`, `args: 3764`, `func_start: 2517`, `class_start: 858`
* *Risk/State:* `safety_bypasses: 308`, `state_mutation: 1242`, `dead_code: 252`, `planned_debt: 3`, `duplicate_logic: 2`, `unreferenced_by_name: 331`
* *Architecture:* `api: 1813`, `import: 13`
* *Defense:* `safety: 590`, `test: 549`, `immutability_locks: 327`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Operations, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 7531.9 | **LOC:** 15181 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (72.0%), Guard Balance (formerly Safety Score) (48.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.8%)
- **Documentation Coverage:** 99.5465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestWithInterfaceImplementingPattern` **(I/O & Config Routines)** (Impact: 19.9)
  * `TestWithPattern_Ref_Iterator` **(Stateful Encapsulated Methods)** (Impact: 17.1)
  * `DisposePatternPreferredOverIAsyncDisposable` **(Annotated & Test Methods)** (Impact: 16.9)
  * `DisposePatternPreferredOverIAsyncDisposable_Deconstruction` **(Annotated & Test Methods)** (Impact: 16.9)
  * `DisposePatternPreferredOverIAsyncDisposable_NoIAsyncEnumerable` **(Annotated & Test Methods)** (Impact: 16.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 394 instances
* *Amplified Cascading Flux:* 21 instances
* *Concurrency (weighted view):* 3839
* *State Mutation (weighted view):* 495
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 2992`, `args: 1437`, `func_start: 1116`, `class_start: 599`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 453`, `dead_code: 13`, `planned_debt: 9`, `unreferenced_by_name: 224`
* *Architecture:* `api: 1493`, `concurrency: 1869`, `import: 396`
* *Defense:* `safety: 174`, `doc: 1`, `test: 335`, `immutability_locks: 122`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, N, N1, N1.N2.N3, N2, N3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 6620.5 | **LOC:** 22795 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (66.8%), Guard Balance (formerly Safety Score) (42.4%), Complexity Load (formerly Cognitive Load) (21.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (20.1%)
- **Documentation Coverage:** 98.9594% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AssertParameterScope` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `ParameterCapturing_055_ColorColor_Query_Method` **(Many-Argument Workhorses)** (Impact: 70.6)
  * `Handle` **(Compute Cores)** (Impact: 48.6)
  * `Handle` **(Compute Cores)** (Impact: 48.0)
  * `Handle11` **(Compute Cores)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 135 instances
* *Amplified Cascading Flux:* 201 instances
* *Concurrency (weighted view):* 854
* *State Mutation (weighted view):* 1045
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 841`, `structural_boundaries: 4869`, `args: 2629`, `func_start: 1350`, `class_start: 851`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 643`, `dead_code: 170`, `duplicate_logic: 28`, `unreferenced_by_name: 426`
* *Architecture:* `api: 1423`, `concurrency: 179`, `import: 75`
* *Defense:* `safety: 378`, `doc: 91`, `test: 1497`, `sync_locks: 139`, `immutability_locks: 177`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Diagnostics, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Test.Utilities, PrimaryConstructorTests.TestFlags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 6544.24 | **LOC:** 11336 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (59.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (45.8%)
- **Documentation Coverage:** 99.4949% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `DefaultLiteral_ReturningAsync` **(Many-Argument Workhorses)** (Impact: 35.7)
  * `ObjectCreation_ReturningAsync` **(Compute Cores)** (Impact: 34.3)
  * `Local_ReturningAsync` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `Conditional_ReturningAsync` **(Compute Cores)** (Impact: 31.1)
  * `Cast_ReturningAsync` **(Compute Cores)** (Impact: 28.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 396 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 3671
* *State Mutation (weighted view):* 556
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 286`, `structural_boundaries: 2611`, `args: 1131`, `func_start: 916`, `class_start: 432`
* *Risk/State:* `safety_bypasses: 185`, `state_mutation: 326`, `dead_code: 3`, `duplicate_logic: 12`, `unreferenced_by_name: 184`
* *Architecture:* `io: 2`, `api: 949`, `concurrency: 1691`, `import: 368`
* *Defense:* `safety: 165`, `doc: 5`, `test: 165`, `sync_locks: 4`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, Roslyn.Utilities, System, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/SemanticErrorTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 6532.48 | **LOC:** 25420 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (23.0%), Concurrency Surface (formerly Concurrency) (17.3%), Complexity Load (formerly Cognitive Load) (13.9%)
- **Documentation Coverage:** 96.6452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CS0464WRN_CmpAlwaysFalse` **(I/O & Config Routines)** (Impact: 90.2)
  * `CS0472WRN_NubExprIsConstBool` **(I/O & Config Routines)** (Impact: 37.7)
  * `CS0458WRN_AlwaysNull` **(I/O & Config Routines)** (Impact: 35.6)
  * `CS1720WRN_DotOnDefault02` **(I/O & Config Routines)** (Impact: 33.6)
  * `CS0165ERR_UseDefViolation03` **(I/O & Config Routines)** (Impact: 33.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 177 instances
* *Concurrency (weighted view):* 137
* *State Mutation (weighted view):* 1379
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 3690`, `args: 2714`, `func_start: 2278`, `class_start: 1019`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 1025`, `dead_code: 173`, `planned_debt: 14`, `fragile_debt: 2`, `unreferenced_by_name: 777`
* *Architecture:* `io: 1`, `api: 1878`, `concurrency: 27`, `import: 232`
* *Defense:* `safety: 445`, `doc: 125`, `test: 709`, `sync_locks: 19`, `immutability_locks: 92`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` A, B, Basic.Reference.Assemblies, C, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleTest.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 6331.06 | **LOC:** 29801 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (40.2%), Concurrency Surface (formerly Concurrency) (15.7%), Connectivity (formerly Api Exposure) (14.2%), Dead Code Surface (formerly Dead Code) (12.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OverriddenMethodWithDifferentTupleNamesInReturnUsingTypeArg` **(Generic / Templated Code)** (Impact: 29.1)
  * `AssertTupleTypeMembersEquality` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `verify` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `verify` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `verifyTupleTypes` **(Many-Argument Workhorses)** (Impact: 20.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 137 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 1017
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 434`, `structural_boundaries: 5441`, `args: 2515`, `func_start: 2224`, `class_start: 954`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 743`, `dead_code: 214`, `planned_debt: 18`, `duplicate_logic: 9`, `unreferenced_by_name: 601`
* *Architecture:* `api: 1957`, `concurrency: 48`, `import: 212`
* *Defense:* `safety: 177`, `test: 2672`, `immutability_locks: 234`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.Text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/MethodTypeInferenceTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 6315.95 | **LOC:** 1239 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.053; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.6%), Concurrency Surface (formerly Concurrency) (27.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (12.4%), Connectivity (formerly Api Exposure) (12.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 18
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 312`, `args: 196`, `func_start: 167`, `class_start: 57`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 47`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 95`, `concurrency: 3`, `import: 24`
* *Defense:* `safety: 15`, `test: 36`, `sync_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections.Generic, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/Completion/CompletionProviders/SymbolCompletionProviderTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 6121.06 | **LOC:** 14435 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 40.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **33**; blast radius 0.053; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (49.5%), Guard Balance (formerly Safety Score) (43.8%)
- **Documentation Coverage:** 99.5946% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M` **(Annotated & Test Methods)** (Impact: 117.2)
  * `M` **(Annotated & Test Methods)** (Impact: 117.0)
  * `M` **(Annotated & Test Methods)** (Impact: 116.8)
  * `M` **(Annotated & Test Methods)** (Impact: 116.8)
  * `M` **(Annotated & Test Methods)** (Impact: 116.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 1923
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 191`, `structural_boundaries: 3460`, `args: 1924`, `func_start: 1486`, `class_start: 988`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 51`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 115`, `unreferenced_by_name: 558`
* *Architecture:* `api: 1414`, `concurrency: 1683`, `import: 221`
* *Defense:* `safety: 131`, `doc: 7`, `test: 327`, `sync_locks: 1`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` A, B, Goo, IGoo, Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CSharp.Completion.Providers, Microsoft.CodeAnalysis.CSharp.Shared.Extensions, Microsoft.CodeAnalysis.Completion.Providers...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs` -> Churn: **74.53%** | Cog Load: 55.4798% | Debt: 10.87%
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/FileBasedPrograms/FileBasedProgramsProjectSystem.cs` -> Churn: **74.25%** | Cog Load: 52.0215% | Debt: 46.1017%
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LanguageServerProjectSystem.cs` -> Churn: **68.91%** | Cog Load: 93.5253% | Debt: 74.4868%
- `src/Workspaces/CoreTestUtilities/Workspaces/TestWorkspace`1.cs` -> Churn: **66.83%** | Cog Load: 25.8807% | Debt: 93.4119%
- `src/LanguageServer/Protocol.TestUtilities/LanguageServer/AbstractLanguageServerProtocolTests.cs` -> Churn: **66.54%** | Cog Load: 59.8434% | Debt: 93.2821%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Compilers/CSharp/Test/Emit/CodeGen/SwitchTests.cs` -> **Fred Silberberg** (100.0% isolated ownership) | Magnitude: 228406.74
- `src/Compilers/CSharp/Test/Emit2/Emit/EditAndContinue/EditAndContinueStateMachineTests.cs` -> **Joey Robichaud** (100.0% isolated ownership) | Magnitude: 36883.55
- `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` -> **DoctorKrolic** (100.0% isolated ownership) | Magnitude: 11777.56
- `src/Compilers/CSharp/Test/Emit3/Semantics/LockTests.cs` -> **Copilot** (100.0% isolated ownership) | Magnitude: 10202.39
- `src/Compilers/CSharp/Test/CSharp15/UnionsTests.cs` -> **AlekseyTs** (100.0% isolated ownership) | Magnitude: 8023.04

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 13.196** (Embedded: 0.2179 * Error Risk: 60.5532%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs` -> **Severity: 2.206** (Embedded: 0.0459 * Error Risk: 48.1022%)
- `src/Compilers/CSharp/Portable/BoundTree/Formatting.cs` -> **Severity: 1.604** (Embedded: 0.0305 * Error Risk: 52.5102%)
- `src/Compilers/Core/Portable/MetadataReference/Metadata.cs` -> **Severity: 0.96** (Embedded: 0.0199 * Error Risk: 48.2864%)
- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Analysis/PointsToAnalysis/PointsToAnalysis.cs` -> **Severity: 0.21** (Embedded: 0.0032 * Error Risk: 66.2622%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 14413.1** (Blast Radius: 144.131 * Doc Risk: 100.0%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs` -> **Severity: 2298.6** (Blast Radius: 22.986 * Doc Risk: 100.0%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Completion.cs` -> **Severity: 612.9** (Blast Radius: 6.129 * Doc Risk: 100.0%)
- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Rename.cs` -> **Severity: 185.7** (Blast Radius: 1.857 * Doc Risk: 100.0%)
- `src/Compilers/Core/Portable/MetadataReference/Metadata.cs` -> **Severity: 182.98** (Blast Radius: 9.149 * Doc Risk: 20.0%)

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
