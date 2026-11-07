# ARCHITECTURAL_BRIEF: roslyn
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/dotnet/roslyn` |
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
- **Scope:** 14537 analyzed artifact(s), 4474322 LOC.
- **Load-bearing artifact:** `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -- 3127 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Workspaces/CSharpTest/OrganizeImports/OrganizeUsingsTests.cs` -- pulls in 103 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` at magnitude 14696.7 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 14537 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 6104 |
| Total LOC | 4474322 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 70.4% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5886 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1336 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 15.5359 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1037 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 13913 | 4452570 | 95.7% |
| PLAINTEXT | 231 | 1418 | 1.6% |
| YAML | 115 | 5764 | 0.8% |
| MARKDOWN | 106 | 0 | 0.7% |
| POWERSHELL | 66 | 9135 | 0.5% |
| SHELL | 34 | 4037 | 0.2% |
| BATCH | 28 | 167 | 0.2% |
| XML | 26 | 0 | 0.2% |
| JSON | 14 | 915 | 0.1% |
| FSHARP | 2 | 10 | 0.0% |
| PYTHON | 1 | 251 | 0.0% |
| CSV | 1 | 55 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | bom | 13922 |
| utf-8 | utf-8 | 613 |
| cp1252 | cp1252-fallback | 1 |
| latin-1 | latin-1-fallback | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Encapsulated Accessors Files 22%, Declarative / Non-Code 19%, Callbacks & Closures Files 10%, Large Core Modules (3) 9%, Data / Markup / Trivial 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 14199 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 336 | 2.3% |
| Static: Minified & Vendor Opaque Mass | 2 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 6104*

**Composition by Extension & Reason:**
- `.vb`: 3646x Unsupported Format (.vb), 1x Excluded (Machine-Generated Source Code Signature: 14598 LOC), 1x Excluded (Saturation: Line 11 exceeds 500 chars)
- `.xlf`: 913x Unsupported Format (.xlf), 4x Excluded (Saturation: Line 33 exceeds 500 chars), 3x Excluded (Saturation: Line 96 exceeds 500 chars)
- `.csproj`: 299x Unsupported Format (.csproj), 1x Excluded (Unsupported Extension: '.csproj'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 231x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dll`: 138x Excluded (Explicitly Denied Extension: '.dll'), 6x Excluded (Explicitly Denied Extension: '.Dll')
- `.cs`: 64x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 14 LOC), 1x Excluded (Machine-Generated Source Code Signature: 17743 LOC)
- `.png`: 70x Excluded (Explicitly Denied Extension: '.png')
- `.resx`: 70x Unsupported Format (.resx)
- `no_extension`: 24x Unsupported Format (.undeterminable), 16x Unsupported Format (.vsixmanifest), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xaml`: 60x Unsupported Format (.xaml)
- `.json`: 57x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 75861 LOC)
- `.props`: 31x Unsupported Format (.props), 16x Excluded (Unsupported Extension: '.props'), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vbproj`: 51x Unsupported Format (.vbproj)
- `.targets`: 21x Unsupported Format (.targets), 20x Excluded (Unsupported Extension: '.targets'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.projitems`: 37x Unsupported Format (.projitems), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 13.4 | 5.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.7 | 29.7 | 46.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 37.1 | 32.2 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 5.6 | 4.6 | 1.8 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 13.6 | 1.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 71.1 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 49366 | 3532 | 3 | `src/Compilers/Core/Portable/WellKnownMembers.cs` |
| cleanup | 3928 | 1064 | 0 | `src/ExpressionEvaluator/CSharp/Test/ExpressionCompiler/LocalsTests.cs` |
| guards | 264544 | 13227 | 36 | `src/Compilers/CSharp/Test/Syntax/Parsing/ParsingErrorRecoveryTests.cs` |
| danger | 39651 | 3633 | 3 | `src/Compilers/CSharp/Test/WinRT/Metadata/WinMdEventTests.cs` |
| concurrency | 114960 | 4331 | 13 | `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` |
| connectivity | 317032 | 13911 | 31 | `src/Compilers/VisualBasic/Test/Semantic/Binding/T_1247520.cs` |
| io | 4066 | 606 | 0 | `src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 123 | 43 | 0 | `eng/common/cross/build-rootfs.sh` |
| time | 871 | 267 | 0 | `src/Compilers/CSharp/Test/Semantic/SourceGeneration/StateTableTests.cs` |
| serialization | 105 | 52 | 0 | `src/Compilers/CSharp/Test/Semantic/Semantics/DynamicTests.cs` |
| regex | 328 | 80 | 0 | `.github/skills/vmr-codeflow-status/scripts/Get-CodeflowStatus.ps1` |
| events | 18097 | 1478 | 1 | `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` |
| tests | 170229 | 2371 | 11 | `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` |
| docs | 126617 | 5818 | 20 | `src/Compilers/CSharp/Portable/Compilation/CSharpSemanticModel.cs` |
| debt | 47177 | 2006 | 1 | `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` |
| mutation | 713692 | 11241 | 82 | `src/Compilers/VisualBasic/Test/Semantic/Binding/T_1247520.cs` |
| dead_code | 156471 | 10039 | 15 | `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionTests.cs` |
| credential | 1055 | 74 | 0 | `src/Compilers/CSharp/Test/Emit2/CodeGen/CodeGenCallTests.cs` |
| threat | 340 | 38 | 0 | `src/Compilers/Core/Portable/Xml/XmlCharType.cs` |
| ml_ai | 1123 | 378 | 0 | `src/Compilers/CSharp/Portable/Parser/QuickScanner.cs` |
| ui | 64 | 31 | 0 | `src/VisualStudio/Core/Impl/Options/AbstractOptionPageControl.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs` (Hits: 377)
- `eng/common/cross/build-rootfs.sh` (Hits: 127)
- `eng/common/SetupNugetSources.sh` (Hits: 76)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Diagnostics.cs** (`src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs`) — 3127 inbound connections
2. **SystemHelpers.cs** (`src/ExpressionEvaluator/Core/Source/ResultProvider/SystemHelpers.cs`) — 1788 inbound connections
3. **ExceptionUtilities.cs** (`src/Dependencies/Contracts/ExceptionUtilities.cs`) — 975 inbound connections
4. **Contract.cs** (`src/Dependencies/Contracts/Contract.cs`) — 887 inbound connections
5. **CodeActions.cs** (`src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/CodeActions.cs`) — 662 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **OrganizeUsingsTests.cs** (`src/Workspaces/CSharpTest/OrganizeImports/OrganizeUsingsTests.cs`) — 103 outbound dependencies
2. **AddUsingTests.cs** (`src/EditorFeatures/CSharpTest/CodeActions/AddUsing/AddUsingTests.cs`) — 61 outbound dependencies
3. **CommandLineTests.cs** (`src/Compilers/CSharp/Test/CommandLine/CommandLineTests.cs`) — 53 outbound dependencies
4. **PDBUsingTests.cs** (`src/Compilers/CSharp/Test/Emit2/PDB/PDBUsingTests.cs`) — 53 outbound dependencies
5. **EditorInProcess.cs** (`src/VisualStudio/IntegrationTest/New.IntegrationTests/InProcess/EditorInProcess.cs`) — 53 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `IsBuildOnlyDiagnostic` **(Compute Cores)** (@ `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs`) -> Impact: **2914.5** | LOC: 2004
  * *Intent:* /// <summary> /// Returns true if this is a build-only diagnostic that is never reported from /// <see cref="SemanticModel.GetDiagnostics(Text.TextSpa...
- `Parse` **(Many-Argument Workhorses)** (@ `src/Compilers/CSharp/Portable/CommandLine/CSharpCommandLineParser.cs`) -> Impact: **1311.0** | LOC: 1579
  * *Intent:* /// <summary> /// Parses a command line. /// </summary> /// <param name="args">A collection of strings representing the command line arguments.</param...
- `GetFlowGraph` **(Many-Argument Workhorses)** (@ `src/Compilers/Test/Core/Compilation/ControlFlowGraphVerifier.cs`) -> Impact: **1116.3** | LOC: 1678
- `VisitConversion` **(Many-Argument Workhorses)** (@ `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs`) -> Impact: **867.3** | LOC: 620
  * *Intent:* /// If <see langword="true"/>, the incoming conversion is assumed to be from binding /// and will be re-calculated, this time considering nullability....
- `AnalyzeSemanticsAsync` **(Many-Argument Workhorses)** (@ `src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs`) -> Impact: **838.2** | LOC: 1013
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
| `src/Compilers/CSharp/Test/Semantic/Semantics` | 107 | 93680.66 | 9.92% | 0.0% |
| `src/Compilers/CSharp/Test/Emit/CodeGen` | 73 | 79272.7 | 15.58% | 0.0% |
| `src/Compilers/CSharp/Test/Emit3/Semantics` | 27 | 78807.7 | 8.68% | 0.0% |
| `src/Compilers/CSharp/Portable/Binder` | 117 | 54119.44 | 23.82% | 41.63% |
| `src/Compilers/CSharp/Test/Symbol/Symbols` | 51 | 45447.66 | 6.4% | 0.0% |
| `src/Compilers/CSharp/Test/Syntax/Parsing` | 69 | 27759.4 | 3.57% | 0.0% |
| `src/Compilers/CSharp/Portable/Symbols/Source` | 71 | 26350.66 | 28.66% | 41.03% |
| `src/EditorFeatures/CSharpTest2/Recommendations` | 150 | 24940.24 | 7.37% | 97.39% |
| `src/Compilers/CSharp/Portable/Symbols` | 120 | 20104.84 | 14.73% | 56.84% |
| `src/Compilers/CSharp/Portable/FlowAnalysis` | 34 | 18226.64 | 23.82% | 65.81% |

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
- `eng/build-utils.ps1` -> **100.0%** Exposure
- `eng/build.ps1` -> **100.0%** Exposure
- `eng/common/SetupNugetSources.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionTests.cs` -> **1175** Orphaned Functions | **5** Duplicates
- `src/Features/CSharpTest/EditAndContinue/TopLevelEditingTests.cs` -> **1157** Orphaned Functions | **0** Duplicates
- `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` -> **893** Orphaned Functions | **64** Duplicates
- `src/Compilers/CSharp/Test/Emit3/Semantics/CollectionExpressionTests.cs` -> **932** Orphaned Functions | **7** Duplicates
- `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionTests2.cs` -> **453** Orphaned Functions | **378** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `73` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `84368` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Compilers/CSharp/Test/Symbol/Symbols/DefaultInterfaceImplementationTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.569)
- **Top Global Matches:** file_cluster_16: 8.569, file_cluster_13: 8.676, file_cluster_0: 8.93
- **Magnitude:** 14696.7 | **LOC:** 69414 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **16**; blast radius 0.046; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.7%), Dead Code Surface (formerly Dead Code) (16.6%), Concurrency Surface (formerly Concurrency) (12.2%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 99.9072% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OperatorImplementationInDerived_01` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `EventImplementationInDerived_12` **(Compute Cores)** (Impact: 42.0)
  * `MethodImplementationInDerived_12` **(Compute Cores)** (Impact: 36.6)
  * `ValidatePropertyImplementationInDerived_12` **(Many-Argument Workhorses)** (Impact: 31.9)
  * `EventImplementationInDerived_15` **(Compute Cores)** (Impact: 29.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 370 instances
* *State Mutation (weighted view):* 2049
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1659`, `structural_boundaries: 10157`, `args: 4446`, `func_start: 2962`, `class_start: 3505`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 1309`, `dead_code: 767`, `planned_debt: 895`, `duplicate_logic: 64`, `unreferenced_by_name: 893`
* *Architecture:* `api: 3497`, `concurrency: 16`, `import: 53`
* *Defense:* `safety: 115`, `doc: 3`, `test: 5561`, `immutability_locks: 35`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.046
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000481
  * `Imports (Out-Degree: 11):` Basic.Reference.Assemblies, I0, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit2/CodeGen/CodeGenCallTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.762)
- **Top Global Matches:** file_cluster_0: 6.762, file_cluster_13: 10.261, file_cluster_2: 10.511
- **Magnitude:** 14179.88 | **LOC:** 36548 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **14**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (51.3%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GenericTypeParameterAsReceiver_Assignment_Compound_ImplicitIndexIndexer_Class_IndexAndValue_Async_04` **(Generic / Templated Code)** (Impact: 13.5)
  * `GenericTypeParameterAsReceiver_Assignment_Conditional_ImplicitIndexIndexer_Class_IndexAndValue_Async_04` **(I/O & Config Routines)** (Impact: 13.5)
  * `GenericTypeParameterAsReceiver_Assignment_Compound_Property_Class_Async_02` **(Generic / Templated Code)** (Impact: 13.0)
  * `GenericTypeParameterAsReceiver_Assignment_Conditional_Property_Class_Async_02` **(I/O & Config Routines)** (Impact: 13.0)
  * `GenericTypeParameterAsReceiver_Assignment_Compound_Indexer_Class_Index_Async_02` **(Generic / Templated Code)** (Impact: 13.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1449 instances
* *Concurrency (weighted view):* 8933
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3383`, `args: 1717`, `func_start: 1477`, `class_start: 619`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 2196`, `unreferenced_by_name: 201`
* *Architecture:* `api: 594`, `concurrency: 1688`, `import: 287`
* *Defense:* `safety: 586`, `test: 128`, `immutability_locks: 375`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Microsoft.CodeAnalysis.CSharp.Emit, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.542)
- **Top Global Matches:** file_cluster_6: 8.542, file_cluster_4: 12.461, file_cluster_8: 15.516
- **Magnitude:** 11373.46 | **LOC:** 4351 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.3%), Mutation Surface (formerly State Flux) (44.1%), Debt Markers (formerly Tech Debt) (40.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Main` **(Compute Cores)** (Impact: 258.0)
  * `Main` **(Compute Cores)** (Impact: 257.1)
  * `Main` **(Compute Cores)** (Impact: 256.9)
  * `Main` **(Compute Cores)** (Impact: 256.7)
  * `Main` **(Compute Cores)** (Impact: 255.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 210
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 889`, `args: 518`, `func_start: 493`, `class_start: 278`
* *Risk/State:* `state_mutation: 86`, `duplicate_logic: 26`, `unreferenced_by_name: 17`
* *Architecture:* `io: 1`, `api: 438`, `concurrency: 1`, `import: 40`
* *Defense:* `safety: 16`, `doc: 1`, `test: 3`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Microsoft.CodeAnalysis.Editor.CSharp.CompleteStatement, Microsoft.CodeAnalysis.Editor.UnitTests.CompleteStatement, Microsoft.CodeAnalysis.Options, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.VisualStudio.Commanding, Roslyn.Test.Utilities, System, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/VisualBasic/Test/Semantic/Binding/T_1247520.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_2: 6.43, file_cluster_17: 7.677, file_cluster_15: 7.844
- **Magnitude:** 10852.48 | **LOC:** 50149 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.026; role: Isolated/Orphan
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (17.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `n_RefClass0` **(I/O & Config Routines)** (Impact: 1.5)
  * `n_RefClass1` **(I/O & Config Routines)** (Impact: 1.5)
  * `n_RefClass2` **(I/O & Config Routines)** (Impact: 1.5)
  * `n_RefClass3` **(I/O & Config Routines)** (Impact: 1.5)
  * `n_RefClass4` **(I/O & Config Routines)** (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 10022`, `args: 20`, `func_start: 20`, `class_start: 10020`
* *Risk/State:* None
* *Architecture:* `api: 10020`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.184)
- **Top Global Matches:** file_cluster_0: 8.184, file_cluster_13: 9.608, file_cluster_12: 9.966
- **Magnitude:** 10283.28 | **LOC:** 52987 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **29**; blast radius 0.045; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.9%), Dead Code Surface (formerly Dead Code) (23.4%), Concurrency Surface (formerly Concurrency) (20.6%)
- **Documentation Coverage:** 98.6831% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Implementation_StaticMethod_01` **(I/O & Config Routines)** (Impact: 30.7)
  * `Implementation_InstanceMethod_05_Iterator` **(I/O & Config Routines)** (Impact: 23.7)
  * `Implementation_StaticMethod_02_WithLocalFunction` **(I/O & Config Routines)** (Impact: 23.6)
  * `Implementation_InstanceMethod_10_Iterator_Generic` **(Generic / Templated Code)** (Impact: 23.1)
  * `Implementation_InstanceMethod_02` **(I/O & Config Routines)** (Impact: 22.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 30 instances
* *Amplified Cascading Flux:* 10 instances
* *Concurrency (weighted view):* 358
* *State Mutation (weighted view):* 1036
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 176`, `structural_boundaries: 10560`, `args: 4472`, `func_start: 4993`, `class_start: 2211`
* *Risk/State:* `safety_bypasses: 246`, `state_mutation: 1016`, `dead_code: 837`, `planned_debt: 19`, `duplicate_logic: 5`, `unreferenced_by_name: 1175`
* *Architecture:* `api: 3926`, `concurrency: 208`, `import: 234`
* *Defense:* `safety: 251`, `doc: 134`, `test: 1635`, `immutability_locks: 177`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.045
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.029614
  * `Imports (Out-Degree: 15):` C, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Diagnostics, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Portable/FlowAnalysis/NullableWalker.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.63)
- **Top Global Matches:** file_cluster_4: 8.63, file_cluster_16: 12.95, file_cluster_6: 13.403
- **Magnitude:** 10265.62 | **LOC:** 14301 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 55.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **14**; blast radius 0.074; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.4%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (61.2%), Guard Balance (formerly Safety Score) (54.0%)
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
* *Structure:* `branch: 2094`, `structural_boundaries: 1745`, `args: 727`, `func_start: 593`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 913`, `dead_code: 23`, `planned_debt: 7`, `unreferenced_by_name: 142`
* *Architecture:* `api: 221`, `import: 14`
* *Defense:* `safety: 659`, `doc: 408`, `immutability_locks: 212`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.074
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.03651
  * `Imports (Out-Degree: 41):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Collections, Microsoft.CodeAnalysis.PooledObjects, Roslyn.Utilities, System, System.Collections.Concurrent, System.Collections.Generic...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionTests2.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 12.252)
- **Top Global Matches:** file_cluster_0: 12.252, file_cluster_12: 13.228, file_cluster_5: 13.402
- **Magnitude:** 9284.06 | **LOC:** 38865 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 62.5%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **23**; blast radius 0.364; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.0%), Guard Balance (formerly Safety Score) (51.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (32.2%), Complexity Load (formerly Cognitive Load) (21.2%)
- **Documentation Coverage:** 95.5039% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MarkerTypeRawName_53` **(Annotated & Test Methods)** (Impact: 80.9)
  * `IndexerAccess_CompoundAssignment_WithInterpolationHandler_04` **(Generic / Templated Code)** (Impact: 14.0)
  * `IndexerAccess_Set_WithInterpolationHandler_04` **(Generic / Templated Code)** (Impact: 13.6)
  * `MarkerTypeRawName_13` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `Nullability_NullableContext_04` **(Generic / Templated Code)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 320 instances
* *Amplified Cascading Flux:* 45 instances
* *Concurrency (weighted view):* 2151
* *State Mutation (weighted view):* 1297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 6846`, `args: 2833`, `func_start: 3002`, `class_start: 1574`
* *Risk/State:* `safety_bypasses: 220`, `state_mutation: 1207`, `dead_code: 290`, `duplicate_logic: 378`, `unreferenced_by_name: 453`
* *Architecture:* `api: 2423`, `concurrency: 551`, `import: 144`
* *Defense:* `safety: 161`, `doc: 171`, `test: 944`, `sync_locks: 17`, `immutability_locks: 229`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.364
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.031301
  * `Imports (Out-Degree: 17):` E, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, N1...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Portable/Parser/LanguageParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.291)
- **Top Global Matches:** file_cluster_4: 7.291, file_cluster_6: 8.657, file_cluster_16: 13.986
- **Magnitude:** 9071.74 | **LOC:** 14680 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 72.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (65.1%), Guard Balance (formerly Safety Score) (59.1%)
- **Documentation Coverage:** 93.1238% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ParseNamespaceBodyWorker` **(Many-Argument Workhorses)** (Impact: 180.8)
  * `ParseVariableDeclarator` **(Many-Argument Workhorses)** (Impact: 179.8)
  * `GetPrecedence` **(Compute Cores)** (Impact: 153.6)
  * `ParsePrimaryExpression` **(Compute Cores)** (Impact: 140.9)
  * `ParseMemberDeclarationOrStatementCore` **(Many-Argument Workhorses)** (Impact: 113.3)
    * *Intent:* /// <summary> /// Changes in this function around member parsing should be mirrored in <see cref="Pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 768 instances
* *State Mutation (weighted view):* 2573
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2689`, `structural_boundaries: 1882`, `args: 632`, `func_start: 474`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1037`, `dead_code: 17`, `planned_debt: 2`, `fragile_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 47`, `import: 11`
* *Defense:* `safety: 278`, `doc: 187`, `immutability_locks: 17`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000138
  * `Imports (Out-Degree: 16):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Syntax.InternalSyntax, Microsoft.CodeAnalysis.Text, Roslyn.Utilities, System, System.Collections.Generic, System.Diagnostics...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Portable/Binder/Binder_Expressions.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.708)
- **Top Global Matches:** file_cluster_4: 6.708, file_cluster_6: 9.361, file_cluster_16: 13.015
- **Magnitude:** 8559.56 | **LOC:** 11842 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 30.4%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **15**; blast radius 0.1; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (72.6%), Guard Balance (formerly Safety Score) (57.8%)
- **Documentation Coverage:** 82.3864% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BindExpressionInternal` **(Many-Argument Workhorses)** (Impact: 275.1)
  * `bindExpressionInternal` **(Many-Argument Workhorses)** (Impact: 269.7)
  * `CheckAndCoerceArguments` **(Many-Argument Workhorses)** (Impact: 238.9)
    * *Intent:* #nullable enable
  * `ResolveExtension` **(Many-Argument Workhorses)** (Impact: 208.4)
    * *Intent:* #nullable enable
  * `BindMemberAccessWithBoundLeft` **(Many-Argument Workhorses)** (Impact: 141.8)
    * *Intent:* /// <remarks> /// If new checks are added to this method, they will also need to be added to /// <se...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 614 instances
* *State Mutation (weighted view):* 2114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1729`, `structural_boundaries: 1222`, `args: 365`, `func_start: 304`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 886`, `dead_code: 32`, `planned_debt: 11`, `fragile_debt: 5`, `unreferenced_by_name: 15`
* *Architecture:* `api: 53`, `import: 15`
* *Defense:* `safety: 355`, `doc: 290`, `immutability_locks: 170`, `cleanup: 104`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.1
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.042058
  * `Imports (Out-Degree: 66):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.Collections, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Text, Roslyn.Utilities, System...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit3/Semantics/CollectionExpressionTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 13.721)
- **Top Global Matches:** file_cluster_5: 13.721, file_cluster_0: 13.941, file_cluster_12: 14.207
- **Magnitude:** 8379.9 | **LOC:** 47661 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 57.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **23**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (51.4%), Dead Code Surface (formerly Dead Code) (28.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.0%), Concurrency Surface (formerly Concurrency) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `BetterConversionFromExpression_19` **(Compute Cores)** (Impact: 39.6)
  * `RefSafety_RefStruct` **(Generic / Templated Code)** (Impact: 21.0)
  * `SpreadElement_Dynamic_01_DynamicBinding` **(Generic / Templated Code)** (Impact: 19.9)
  * `BuiltInInlineArrayTypes` **(Generic / Templated Code)** (Impact: 19.2)
  * `CollectionBuilder_02A` **(Generic / Templated Code)** (Impact: 18.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 1298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 7743`, `args: 5060`, `func_start: 4342`, `class_start: 1939`
* *Risk/State:* `safety_bypasses: 540`, `state_mutation: 1272`, `dead_code: 888`, `planned_debt: 1`, `duplicate_logic: 7`, `unreferenced_by_name: 932`
* *Architecture:* `api: 2638`, `concurrency: 69`, `import: 1603`
* *Defense:* `safety: 302`, `test: 1105`, `immutability_locks: 662`, `cleanup: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Operations, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Test.Utilities, N...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Semantic/Semantics/RefFieldTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.252)
- **Top Global Matches:** file_cluster_0: 8.252, file_cluster_13: 10.131, file_cluster_10: 10.268
- **Magnitude:** 8274.24 | **LOC:** 32280 | **CtrlFlow:** 0.6% | **Authorship Centralization:** 28.6%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (60.7%), Guard Balance (formerly Safety Score) (54.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (25.3%), Complexity Load (formerly Cognitive Load) (18.0%)
- **Documentation Coverage:** 97.5592% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LocalScope_01_OutVar` **(I/O & Config Routines)** (Impact: 16.8)
  * `LocalScope_01_Foreach_Deconstruction_01` **(I/O & Config Routines)** (Impact: 16.2)
  * `LocalScope_01_Deconstruction` **(I/O & Config Routines)** (Impact: 16.0)
  * `MethodInvocation_Lvalue_03` **(Generic / Templated Code)** (Impact: 15.0)
  * `RefAssignValueScopeMismatch_02` **(Compute Cores)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 61 instances
* *State Mutation (weighted view):* 2983
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 6755`, `args: 4443`, `func_start: 3459`, `class_start: 1097`
* *Risk/State:* `safety_bypasses: 119`, `state_mutation: 2861`, `dead_code: 1092`, `planned_debt: 2`, `duplicate_logic: 17`, `unreferenced_by_name: 683`
* *Architecture:* `api: 2076`, `import: 123`
* *Defense:* `safety: 84`, `doc: 56`, `test: 880`, `immutability_locks: 551`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000138
  * `Imports (Out-Degree: 13):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, Roslyn.Utilities...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.964)
- **Top Global Matches:** file_cluster_12: 8.964, file_cluster_0: 9.512, file_cluster_13: 9.547
- **Magnitude:** 7953.92 | **LOC:** 15189 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (50.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CompoundRightShiftWithAwait_TypeParameter_Struct` **(I/O & Config Routines)** (Impact: 15.0)
  * `KeepLtrSemantics_ClassFieldAccessOnArray` **(Defensive Guards)** (Impact: 14.9)
  * `KeepLtrSemantics_AssignmentToAssignmentProperties` **(I/O & Config Routines)** (Impact: 14.5)
  * `KeepLtrSemantics_CompoundAssignmentProperties` **(I/O & Config Routines)** (Impact: 14.2)
  * `KeepLtrSemantics_StructFieldAccessOnArray` **(I/O & Config Routines)** (Impact: 14.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 721 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 5408
* *State Mutation (weighted view):* 820
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 2026`, `args: 936`, `func_start: 762`, `class_start: 248`
* *Risk/State:* `safety_bypasses: 151`, `state_mutation: 814`, `dead_code: 16`, `unreferenced_by_name: 128`
* *Architecture:* `api: 591`, `concurrency: 1803`, `import: 300`
* *Defense:* `safety: 460`, `test: 113`, `immutability_locks: 140`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` C, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System, System.Collections, System.Collections.Generic, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Symbol/Symbols/StaticAbstractMembersInInterfacesTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.597)
- **Top Global Matches:** file_cluster_0: 8.597, file_cluster_13: 11.035, file_cluster_12: 11.137
- **Magnitude:** 7314.18 | **LOC:** 34305 | **CtrlFlow:** 3.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (43.2%), Dead Code Surface (formerly Dead Code) (16.8%), Connectivity (formerly Api Exposure) (12.3%), Concurrency Surface (formerly Concurrency) (12.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `consumeAbstractUnaryOperator_03` **(Many-Argument Workhorses)** (Impact: 110.3)
  * `ConsumeAbstractUnaryOperator_03` **(Many-Argument Workhorses)** (Impact: 104.8)
  * `ConsumeAbstractLogicalBinaryOperator_03` **(Many-Argument Workhorses)** (Impact: 83.1)
  * `ImplementAbstractStaticBinaryOperator_04` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `consumeMixed` **(Many-Argument Workhorses)** (Impact: 55.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 95 instances
* *State Mutation (weighted view):* 720
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 918`, `structural_boundaries: 5335`, `args: 2236`, `func_start: 1325`, `class_start: 1254`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 530`, `dead_code: 385`, `planned_debt: 206`, `duplicate_logic: 4`, `unreferenced_by_name: 382`
* *Architecture:* `api: 1130`, `concurrency: 9`, `import: 26`
* *Defense:* `safety: 591`, `test: 3321`, `immutability_locks: 136`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000259
  * `Imports (Out-Degree: 9):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAwaitForeachTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 8.013)
- **Top Global Matches:** file_cluster_13: 8.013, file_cluster_10: 8.032, file_cluster_0: 9.121
- **Magnitude:** 7070.0 | **LOC:** 15181 | **CtrlFlow:** 0.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (98.8%), Guard Balance (formerly Safety Score) (49.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.9%)
- **Documentation Coverage:** 99.5465% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TestWithInterfaceImplementingPattern` **(I/O & Config Routines)** (Impact: 13.9)
  * `DisposePatternPreferredOverIAsyncDisposable` **(Annotated & Test Methods)** (Impact: 12.7)
  * `AsyncEnumerationViaInterfaceUsesIAsyncDisposable` **(Annotated & Test Methods)** (Impact: 12.7)
  * `DisposePatternPreferredOverIAsyncDisposable_Deconstruction` **(Annotated & Test Methods)** (Impact: 12.7)
  * `DisposePatternPreferredOverIAsyncDisposable_NoIAsyncEnumerable` **(Annotated & Test Methods)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 394 instances
* *Concurrency (weighted view):* 3839
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 2992`, `args: 1437`, `func_start: 1115`, `class_start: 599`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 453`, `dead_code: 14`, `planned_debt: 9`, `unreferenced_by_name: 224`
* *Architecture:* `api: 1493`, `concurrency: 1869`, `import: 396`
* *Defense:* `safety: 174`, `doc: 1`, `test: 335`, `immutability_locks: 122`, `cleanup: 28`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, N, N1, N1.N2.N3, N2, N3...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/RecordTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 9.37)
- **Top Global Matches:** file_cluster_13: 9.37, file_cluster_0: 9.581, file_cluster_16: 9.596
- **Magnitude:** 6933.02 | **LOC:** 30628 | **CtrlFlow:** 1.7% | **Authorship Centralization:** 42.9%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.9%), Concurrency Surface (formerly Concurrency) (36.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (35.9%), Dead Code Surface (formerly Dead Code) (17.9%)
- **Documentation Coverage:** 99.5624% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Handle` **(Compute Cores)** (Impact: 48.6)
  * `Handle` **(Compute Cores)** (Impact: 48.0)
  * `Handle11` **(Compute Cores)** (Impact: 48.0)
  * `Handle8` **(Compute Cores)** (Impact: 36.1)
  * `Handle3` **(Compute Cores)** (Impact: 33.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 100 instances
* *Amplified Cascading Flux:* 104 instances
* *Concurrency (weighted view):* 604
* *State Mutation (weighted view):* 851
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 442`, `structural_boundaries: 5369`, `args: 2835`, `func_start: 1737`, `class_start: 1353`
* *Risk/State:* `safety_bypasses: 109`, `state_mutation: 643`, `dead_code: 370`, `planned_debt: 28`, `fragile_debt: 1`, `duplicate_logic: 4`, `unreferenced_by_name: 667`
* *Architecture:* `api: 2077`, `concurrency: 104`, `import: 92`
* *Defense:* `safety: 33`, `doc: 107`, `test: 1670`, `sync_locks: 98`, `immutability_locks: 237`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0281
  * `Imports (Out-Degree: 15):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Diagnostics, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, Roslyn.Utilities, System...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit3/Semantics/ExtensionOperatorsTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.517)
- **Top Global Matches:** file_cluster_0: 9.517, file_cluster_13: 10.042, file_cluster_10: 10.097
- **Magnitude:** 6697.16 | **LOC:** 30118 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (49.7%), Dead Code Surface (formerly Dead Code) (34.0%), Connectivity (formerly Api Exposure) (15.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.3%)
- **Documentation Coverage:** 92.8322% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Binary_011_Consumption` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `Increment_001_Declaration` **(Generic / Templated Code)** (Impact: 15.4)
  * `CompoundAssignment_001_Declaration` **(Generic / Templated Code)** (Impact: 15.4)
  * `CompoundAssignment_006_Consumption` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `Increment_006_Consumption` **(Many-Argument Workhorses)** (Impact: 14.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 1448
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 6067`, `args: 2606`, `func_start: 3057`, `class_start: 2017`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 1430`, `dead_code: 651`, `duplicate_logic: 4`, `unreferenced_by_name: 560`
* *Architecture:* `api: 2496`, `import: 122`
* *Defense:* `safety: 318`, `doc: 259`, `test: 1002`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.CSharp.UnitTests.UserDefinedCompoundAssignmentOperatorsTests, Microsoft.CodeAnalysis.Test.Utilities, N, N1, N1.E1...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/Semantics/PrimaryConstructorTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 9.307)
- **Top Global Matches:** file_cluster_13: 9.307, file_cluster_10: 9.367, file_cluster_0: 9.42
- **Magnitude:** 6468.7 | **LOC:** 22795 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 33.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (66.8%), Guard Balance (formerly Safety Score) (47.3%), Complexity Load (formerly Cognitive Load) (21.0%), Dead Code Surface (formerly Dead Code) (18.3%)
- **Documentation Coverage:** 98.9594% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AssertParameterScope` **(Many-Argument Workhorses)** (Impact: 95.4)
  * `ParameterCapturing_055_ColorColor_Query_Method` **(Many-Argument Workhorses)** (Impact: 68.3)
  * `ParameterScope_MemberData` **(Callbacks & Closures)** (Impact: 50.5)
  * `Handle` **(Compute Cores)** (Impact: 48.6)
  * `Handle` **(Compute Cores)** (Impact: 48.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 135 instances
* *Amplified Cascading Flux:* 180 instances
* *Concurrency (weighted view):* 854
* *State Mutation (weighted view):* 1003
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 727`, `structural_boundaries: 4869`, `args: 2629`, `func_start: 1313`, `class_start: 851`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 643`, `dead_code: 281`, `duplicate_logic: 28`, `unreferenced_by_name: 426`
* *Architecture:* `api: 1423`, `concurrency: 179`, `import: 75`
* *Defense:* `safety: 378`, `doc: 91`, `test: 1497`, `sync_locks: 139`, `immutability_locks: 177`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Diagnostics, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Test.Utilities, PrimaryConstructorTests.TestFlags...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EditorFeatures/CSharpTest/Completion/CompletionProviders/SymbolCompletionProviderTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 10.48)
- **Top Global Matches:** file_cluster_13: 10.48, file_cluster_0: 10.524, file_cluster_10: 10.923
- **Magnitude:** 6097.16 | **LOC:** 14435 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 25.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **33**; blast radius 0.049; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Complexity Load (formerly Cognitive Load) (48.5%), Guard Balance (formerly Safety Score) (47.9%)
- **Documentation Coverage:** 99.5845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M` **(Annotated & Test Methods)** (Impact: 229.0)
  * `M` **(Annotated & Test Methods)** (Impact: 117.2)
  * `M` **(Annotated & Test Methods)** (Impact: 117.0)
  * `M` **(Annotated & Test Methods)** (Impact: 116.8)
  * `M` **(Annotated & Test Methods)** (Impact: 116.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 48 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 1923
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 3460`, `args: 1924`, `func_start: 1470`, `class_start: 988`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 51`, `fragile_debt: 2`, `duplicate_logic: 91`, `unreferenced_by_name: 569`
* *Architecture:* `api: 1414`, `concurrency: 1683`, `import: 221`
* *Defense:* `safety: 131`, `doc: 7`, `test: 327`, `sync_locks: 1`, `immutability_locks: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.049
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.025194
  * `Imports (Out-Degree: 12):` A, B, Goo, IGoo, Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CSharp.Completion.Providers, Microsoft.CodeAnalysis.CSharp.Shared.Extensions, Microsoft.CodeAnalysis.Completion.Providers...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.293)
- **Top Global Matches:** file_cluster_5: 8.293, file_cluster_12: 8.933, file_cluster_0: 9.528
- **Magnitude:** 6089.54 | **LOC:** 11336 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 87.5%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (52.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (41.1%)
- **Documentation Coverage:** 99.4949% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ObjectCreation_ReturningAsync` **(Compute Cores)** (Impact: 29.1)
  * `Conditional_ReturningAsync` **(Compute Cores)** (Impact: 24.2)
  * `Local_ReturningAsync` **(Many-Argument Workhorses)** (Impact: 24.0)
  * `DefaultLiteral_ReturningAsync` **(Many-Argument Workhorses)** (Impact: 23.6)
  * `Cast_ReturningAsync` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 396 instances
* *Amplified Cascading Flux:* 8 instances
* *Concurrency (weighted view):* 3671
* *State Mutation (weighted view):* 342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 2611`, `args: 1131`, `func_start: 904`, `class_start: 432`
* *Risk/State:* `safety_bypasses: 185`, `state_mutation: 326`, `dead_code: 19`, `duplicate_logic: 12`, `unreferenced_by_name: 184`
* *Architecture:* `io: 2`, `api: 949`, `concurrency: 1691`, `import: 368`
* *Defense:* `safety: 165`, `doc: 5`, `test: 165`, `sync_locks: 4`, `immutability_locks: 60`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, Roslyn.Utilities, System, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 10.304)
- **Top Global Matches:** file_cluster_0: 10.304, file_cluster_13: 12.06, file_cluster_16: 12.261
- **Magnitude:** 5916.28 | **LOC:** 29709 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **18**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (47.6%), Concurrency Surface (formerly Concurrency) (46.5%), Dead Code Surface (formerly Dead Code) (15.7%), Connectivity (formerly Api Exposure) (13.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UnscopedRefInImplementation_Indexer_01` **(Many-Argument Workhorses)** (Impact: 142.9)
  * `UnscopedRefInImplementation_Property_01` **(Many-Argument Workhorses)** (Impact: 134.0)
  * `UnscopedRefInImplementation_Method_01` **(I/O & Config Routines)** (Impact: 27.3)
  * `Foreach_IEnumeratorT_03` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `Foreach_IEnumerator_05` **(Many-Argument Workhorses)** (Impact: 24.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 17 instances
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 28 instances
* *Concurrency (weighted view):* 590
* *Memory Alloc (weighted view):* 914
* *State Mutation (weighted view):* 553
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 509`, `structural_boundaries: 5464`, `args: 2705`, `func_start: 2323`, `class_start: 1169`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 497`, `dead_code: 307`, `planned_debt: 21`, `duplicate_logic: 18`, `unreferenced_by_name: 411`
* *Architecture:* `api: 1445`, `concurrency: 540`, `import: 292`
* *Defense:* `safety: 419`, `test: 1010`, `immutability_locks: 82`, `cleanup: 89`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 6.9e-05
  * `Imports (Out-Degree: 7):` Helper, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenTupleTest.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.192)
- **Top Global Matches:** file_cluster_0: 8.192, file_cluster_13: 9.163, file_cluster_12: 9.533
- **Magnitude:** 5909.86 | **LOC:** 29801 | **CtrlFlow:** 0.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.026; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.3%), Dead Code Surface (formerly Dead Code) (25.2%), Concurrency Surface (formerly Concurrency) (15.7%), Connectivity (formerly Api Exposure) (14.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AssertTupleTypeMembersEquality` **(Many-Argument Workhorses)** (Impact: 24.1)
  * `verify` **(Many-Argument Workhorses)** (Impact: 22.5)
  * `verify` **(Many-Argument Workhorses)** (Impact: 20.6)
  * `verifyTupleTypes` **(Many-Argument Workhorses)** (Impact: 20.3)
  * `CreationOfTupleSymbols_01` **(I/O & Config Routines)** (Impact: 19.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 44 instances
* *Concurrency (weighted view):* 98
* *State Mutation (weighted view):* 831
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 5441`, `args: 2515`, `func_start: 2163`, `class_start: 954`
* *Risk/State:* `safety_bypasses: 126`, `state_mutation: 743`, `dead_code: 504`, `planned_debt: 18`, `duplicate_logic: 9`, `unreferenced_by_name: 601`
* *Architecture:* `api: 1957`, `concurrency: 48`, `import: 212`
* *Defense:* `safety: 177`, `test: 2672`, `immutability_locks: 234`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.026
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` Basic.Reference.Assemblies, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Symbols.Retargeting, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.Text...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Analyzers/CSharp/Tests/RemoveUnnecessaryCast/RemoveUnnecessaryCastTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.237)
- **Top Global Matches:** file_cluster_10: 9.237, file_cluster_15: 9.53, file_cluster_11: 9.85
- **Magnitude:** 5543.44 | **LOC:** 13590 | **CtrlFlow:** 3.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **19**; blast radius 0.165; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (57.9%), Guard Balance (formerly Safety Score) (51.1%), Connectivity (formerly Api Exposure) (13.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M` **(Defensive Guards)** (Impact: 17.4)
  * `M` **(Defensive Guards)** (Impact: 17.4)
  * `M` **(Defensive Guards)** (Impact: 17.2)
  * `M` **(Compute Cores)** (Impact: 11.7)
  * `Main` **(I/O & Config Routines)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 147 instances
* *Amplified Cascading Flux:* 73 instances
* *Concurrency (weighted view):* 1738
* *State Mutation (weighted view):* 395
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 2718`, `args: 1666`, `func_start: 1592`, `class_start: 936`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 249`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 354`, `unreferenced_by_name: 17`
* *Architecture:* `api: 1116`, `concurrency: 1003`, `import: 429`
* *Defense:* `safety: 74`, `test: 65`, `immutability_locks: 60`, `cleanup: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.165
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.030847
  * `Imports (Out-Degree: 8):` CSharpCodeFixVerifier, Microsoft.CodeAnalysis.CSharp, Microsoft.CodeAnalysis.CSharp.RemoveUnnecessaryCast, Microsoft.CodeAnalysis.Editor.UnitTests.CodeActions, Microsoft.CodeAnalysis.Test.Utilities, Microsoft.CodeAnalysis.Testing, Roslyn.Test.Utilities, System...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Semantic/Semantics/SemanticErrorTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 10.077)
- **Top Global Matches:** file_cluster_0: 10.077, file_cluster_13: 10.395, file_cluster_12: 10.84
- **Magnitude:** 5389.98 | **LOC:** 25420 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **25**; blast radius 0.03; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Dead Code Surface (formerly Dead Code) (61.3%), Guard Balance (formerly Safety Score) (49.2%), Concurrency Surface (formerly Concurrency) (17.3%), Connectivity (formerly Api Exposure) (13.7%)
- **Documentation Coverage:** 96.6452% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CS1961ERR_UnexpectedVariance_InputUnsafe` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* /// <summary> /// Test all of the contexts that require input safety. /// Note: some also require ou...
  * `GetDiagnosticsWithFilter_MemberLevelFilter` **(Annotated & Test Methods)** (Impact: 8.2)
  * `CSharp7FeaturesInExprTrees` **(Callbacks & Closures)** (Impact: 7.6)
  * `CS0310ERR_NewConstraintNotSatisfied02` **(Generic / Templated Code)** (Impact: 7.4)
  * `CS0854ERR_ExpressionTreeContainsOptionalArgument02` **(C Struct Operations)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 22 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 137
* *State Mutation (weighted view):* 1027
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 3690`, `args: 2714`, `func_start: 2153`, `class_start: 1019`
* *Risk/State:* `safety_bypasses: 92`, `state_mutation: 1025`, `dead_code: 867`, `planned_debt: 14`, `fragile_debt: 2`, `unreferenced_by_name: 777`
* *Architecture:* `io: 1`, `api: 1878`, `concurrency: 27`, `import: 232`
* *Defense:* `safety: 445`, `doc: 125`, `test: 709`, `sync_locks: 19`, `immutability_locks: 92`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.03
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 6.9e-05
  * `Imports (Out-Degree: 14):` A, B, Basic.Reference.Assemblies, C, Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Syntax, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Compilers/CSharp/Test/Emit3/Symbols/UserDefinedCompoundAssignmentOperatorsTests.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.464)
- **Top Global Matches:** file_cluster_0: 8.464, file_cluster_13: 8.858, file_cluster_15: 9.607
- **Magnitude:** 5377.6 | **LOC:** 20378 | **CtrlFlow:** 2.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.031; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (44.0%), Dead Code Surface (formerly Dead Code) (37.7%), Concurrency Surface (formerly Concurrency) (18.3%), Connectivity (formerly Api Exposure) (14.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Increment_070_Consumption_Prefix_NotUsed_Class` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `Increment_074_Consumption_Postfix_NotUsed_Class` **(Many-Argument Workhorses)** (Impact: 34.4)
  * `Increment_033_OverrideAllowedInClass` **(Defensive Guards)** (Impact: 33.4)
  * `CompoundAssignment_00720_Consumption_Used_Class` **(Many-Argument Workhorses)** (Impact: 32.6)
  * `CompoundAssignment_00721_Consumption_Used_Class` **(Many-Argument Workhorses)** (Impact: 32.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 17 instances
* *Amplified Cascading Flux:* 119 instances
* *Concurrency (weighted view):* 107
* *State Mutation (weighted view):* 826
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 2754`, `args: 1436`, `func_start: 1117`, `class_start: 781`
* *Risk/State:* `state_mutation: 588`, `dead_code: 477`, `planned_debt: 71`, `duplicate_logic: 111`, `unreferenced_by_name: 378`
* *Architecture:* `api: 1453`, `concurrency: 22`, `import: 20`
* *Defense:* `safety: 781`, `doc: 256`, `test: 1250`, `immutability_locks: 180`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000348
  * `Imports (Out-Degree: 11):` Microsoft.CodeAnalysis.CSharp.Symbols, Microsoft.CodeAnalysis.CSharp.Symbols.Metadata.PE, Microsoft.CodeAnalysis.CSharp.Test.Utilities, Microsoft.CodeAnalysis.Test.Utilities, Roslyn.Test.Utilities, System.Diagnostics.CodeAnalysis, System.Linq, System.Linq.Expressions...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Features/Core/Portable/EditAndContinue/AbstractEditAndContinueAnalyzer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.098)
- **Top Global Matches:** file_cluster_4: 9.098, file_cluster_16: 10.946, file_cluster_0: 12.203
- **Magnitude:** 5343.7 | **LOC:** 7195 | **CtrlFlow:** 20.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **22**; blast radius 0.077; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.0%), Complexity Load (formerly Cognitive Load) (38.8%)
- **Documentation Coverage:** 78.6301% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AnalyzeSemanticsAsync` **(Many-Argument Workhorses)** (Impact: 838.2)
  * `ReportUpdatedSymbolDeclarationRudeEdits` **(Many-Argument Workhorses)** (Impact: 267.0)
  * `AnalyzeChangedMemberBody` **(Many-Argument Workhorses)** (Impact: 251.7)
  * `ReportLambdaAndClosureRudeEdits` **(Many-Argument Workhorses)** (Impact: 165.0)
    * *Intent:* #endregion #region Lambdas and Closures
  * `AnalyzeTrivia` **(Many-Argument Workhorses)** (Impact: 134.5)
    * *Intent:* #endregion #region Trivia Analysis /// <summary> /// Top-level edit script does not contain edits fo...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 320 instances
* *Concurrency (weighted view):* 57
* *State Mutation (weighted view):* 1044
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1077`, `structural_boundaries: 1084`, `args: 416`, `func_start: 280`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 404`, `dead_code: 1`, `planned_debt: 14`, `fragile_debt: 1`, `unreferenced_by_name: 19`
* *Architecture:* `api: 115`, `concurrency: 27`, `import: 22`
* *Defense:* `safety: 303`, `doc: 239`, `immutability_locks: 87`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.077
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.001143
  * `Imports (Out-Degree: 31):` Microsoft.CodeAnalysis.Collections, Microsoft.CodeAnalysis.Contracts.EditAndContinue, Microsoft.CodeAnalysis.Differencing, Microsoft.CodeAnalysis.Emit, Microsoft.CodeAnalysis.ErrorReporting, Microsoft.CodeAnalysis.Operations, Microsoft.CodeAnalysis.PooledObjects, Microsoft.CodeAnalysis.Shared.Collections...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Workspaces/Core/Portable/FindSymbols/SymbolFinder_FindReferences_Current.cs` (CSHARP) | Magnitude: 45.18 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 58, structural_boundaries: 26, core_var_decl: 8, concurrency: 7
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Formatting/Engine/AbstractTriviaDataFactory.FormattedWhitespace.cs` (CSHARP) | Magnitude: 35.58 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 18, args: 10, api: 10
- `src/Compilers/CSharp/Portable/Emitter/Model/GenericMethodInstanceReference.cs` (CSHARP) | Magnitude: 12.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 11, func_start: 4, api: 4
- `src/EditorFeatures/Test/FindReferences/FindReferencesCommandHandlerTests.cs` (CSHARP) | Magnitude: 25.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 36, import: 16, args: 9
- `src/Analyzers/Core/CodeFixes/UseCollectionExpression/AbstractUseCollectionExpressionCodeFixProvider.cs` (CSHARP) | Magnitude: 12.04 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 11, encapsulation: 7, immutability_locks: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/Compilers/CSharp/Test/Syntax/Parsing/LambdaAttributeParsingTests.cs` (CSHARP) | Magnitude: 439.32 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 4253, structural_boundaries: 259, args: 244, closures: 141
- `src/Workspaces/Remote/Core/ServiceDescriptors.cs` (CSHARP) | Magnitude: 37.48 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 50, import: 33, encapsulation: 17
- `src/VisualStudio/IntegrationTest/Harness/XUnitShared/Harness/MarshalledObjects.cs` (CSHARP) | Magnitude: 9.44 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 19, structural_boundaries: 7, api: 3, import: 3
- `src/EditorFeatures/CSharpTest/PdbSourceDocument/PdbSourceDocumentLoaderServiceTests.cs` (CSHARP) | Magnitude: 19.14 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 48, indent_spaces: 42, core_var_decl: 12, import: 11
- `src/Compilers/CSharp/Test/Emit3/RefReadonlyParameterTests.cs` (CSHARP) | Magnitude: 1797.78 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 6970, structural_boundaries: 1715, core_var_decl: 1007, args: 1000

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/Compilers/CSharp/Portable/Symbols/Wrapped/WrappedMethodSymbol.cs` (CSHARP) | Magnitude: 76.84 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 287, structural_boundaries: 62, api: 57, encapsulation: 30
- `src/Compilers/CSharp/Portable/Emitter/Model/SpecializedFieldReference.cs` (CSHARP) | Magnitude: 13.72 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 63, structural_boundaries: 17, doc: 6, args: 4
- `src/Compilers/Core/CodeAnalysisTest/MetadataReferences/FusionAssemblyPortabilityPolicy.cs` (CSHARP) | Magnitude: 37.68 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 19, doc: 11, import: 10
- `src/Compilers/CSharp/Portable/Symbols/NoPiaMissingCanonicalTypeSymbol.cs` (CSHARP) | Magnitude: 28.04 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 21, api: 13, encapsulation: 12
- `src/Compilers/CSharp/Portable/Compilation/ForEachStatementInfo.cs` (CSHARP) | Magnitude: 36.1 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 65, doc: 43, api: 15, state_mutation: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LanguageServerWorkspace.cs` (CSHARP) | Magnitude: 54.0 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 74, doc: 31, structural_boundaries: 20, branch: 14
- `src/Workspaces/Core/Portable/Serialization/SerializableSourceText.cs` (CSHARP) | Magnitude: 109.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 132, structural_boundaries: 44, doc: 43, core_var_decl: 22
- `src/Features/CSharpTest/RemoveUnnecessaryCast/RemoveUnnecessaryCastTests_AsTests.cs` (CSHARP) | Magnitude: 1302.94 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 2696, structural_boundaries: 576, args: 418, func_start: 402
- `src/EditorFeatures/Core/Preview/PreviewFactoryService.cs` (CSHARP) | Magnitude: 59.62 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 22, import: 16, state_mutation: 12
- `src/Tools/IdeCoreBenchmarks/FindReferencesBenchmarks.cs` (CSHARP) | Magnitude: 0.06 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 40, core_var_decl: 23, design_snake_case: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Tools/ExternalAccess/Razor/Features/Remote/JsonSerializableDocumentId.cs` (CSHARP) | Magnitude: 0.01 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 7, args: 3, api: 3
- `src/VisualStudio/CSharp/Impl/ProjectSystemShim/HACK_VariantStructure.cs` (CSHARP) | Magnitude: 4.96 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, doc: 10, structural_boundaries: 7, immutability_locks: 7
- `src/VisualStudio/CSharp/Test/F1Help/F1HelpTests.cs` (CSHARP) | Magnitude: 645.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1766, structural_boundaries: 474, func_start: 262, args: 254
- `src/Workspaces/CoreTest/CodeCleanup/ReduceTokenTests.cs` (CSHARP) | Magnitude: 174.4 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1661, core_var_decl: 603, design_pascal_case: 578, debug_prints: 432
- `src/Tools/ExternalAccess/Razor/Features/RazorSourceGeneratedDocumentExcerptServiceWrapper.cs` (CSHARP) | Magnitude: 0.02 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 22, import: 8, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/Compilers/CSharp/Test/Emit3/Attributes/AttributeTests_Dynamic.cs` (CSHARP) | Magnitude: 271.52 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 824, safety_bypasses: 230, core_var_decl: 192, structural_boundaries: 191

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/Compilers/Shared/BuildProtocol.cs` (CSHARP) | Magnitude: 281.18 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 372, doc: 108, structural_boundaries: 103, core_var_decl: 70
- `src/Compilers/Core/Portable/RuleSet/RuleSetInclude.cs` (CSHARP) | Magnitude: 65.0 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 79, doc: 20, structural_boundaries: 17, core_var_decl: 12
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/CSharp/Indentation/CSharpSmartTokenFormatter.cs` (CSHARP) | Magnitude: 67.34 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 105, structural_boundaries: 38, core_var_decl: 20, branch: 14
- `src/EditorFeatures/Core/LanguageServer/AlwaysActivateInProcCapabilitiesProvider.cs` (CSHARP) | Magnitude: 39.64 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 20, state_mutation: 19, core_var_decl: 17
- `src/RoslynAnalyzers/Utilities/Compiler/Options/AnalyzerConfigOptionsProviderExtensions.cs` (CSHARP) | Magnitude: 5.5 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 6, import: 3, safety: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/EditorFeatures/Core/Shared/Tagging/EventSources/TaggerConstants.cs` (CSHARP) | Magnitude: 10.8 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, args: 8, closures: 7
- `src/ExpressionEvaluator/Core/Test/ResultProvider/Debugger/Engine/DkmClrDebuggerBrowsableAttribute.cs` (CSHARP) | Magnitude: 7.42 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 15, api: 4, structural_boundaries: 3, class_start: 2
- `src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_LockStatement.cs` (CSHARP) | Magnitude: 67.48 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 161, core_var_decl: 26, design_camel_case: 26, structural_boundaries: 15
- `src/VisualStudio/Core/Def/Preview/ReferenceChange.ProjectReferenceChange.cs` (CSHARP) | Magnitude: 13.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 7, encapsulation: 7, args: 4
- `src/LanguageServer/Protocol/LanguageServerProtocolResources.Designer.cs` (CSHARP) | Magnitude: 16.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 80, doc: 40, encapsulation: 16, structural_boundaries: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/Compilers/Core/Portable/SourceGeneration/GeneratedSourceText.cs` (CSHARP) | Magnitude: 8.34 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 6, api: 4, import: 4
- `src/VisualStudio/CSharp/Impl/Options/Formatting/WrappingViewModel.cs` (CSHARP) | Magnitude: 7.64 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 23, structural_boundaries: 8, import: 4, class_start: 3
- `src/Compilers/Core/Portable/Emit/EditAndContinue/IDeletedEventDefinition.cs` (CSHARP) | Magnitude: 15.12 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, reflection_metaprogramming: 2, class_start: 1
- `src/Compilers/Core/Portable/Emit/EditAndContinue/IDeletedMethodDefinition.cs` (CSHARP) | Magnitude: 15.12 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, reflection_metaprogramming: 2, class_start: 1
- `src/Compilers/Core/Portable/Emit/EditAndContinue/IDeletedPropertyDefinition.cs` (CSHARP) | Magnitude: 15.12 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, reflection_metaprogramming: 2, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Compilers/Test/Core/CultureContext.cs` (CSHARP) | Magnitude: 9.3 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 5, api: 3, state_mutation: 3
- `src/EditorFeatures/Core/CodeDefinitionWindow/CodeDefinitionWindowLocation.cs` (CSHARP) | Magnitude: 12.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, class_start: 1, api: 1
- `src/LanguageServer/Protocol/Handler/PullHandlers/PreviousPullResult.cs` (CSHARP) | Magnitude: 12.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, args: 1, class_start: 1, api: 1
- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/EditorConfig/Parsing/EditorConfigOption.cs` (CSHARP) | Magnitude: 12.56 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 3, args: 1, class_start: 1
- `src/Compilers/CSharp/Portable/Lowering/LocalRewriter/LocalRewriter_PreviousSubmissionReference.cs` (CSHARP) | Magnitude: 4.5 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 9, core_var_decl: 4, design_camel_case: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/Workspaces/Core/Portable/PatternMatching/PatternMatcher.cs` (CSHARP) | Magnitude: 302.88 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 376, structural_boundaries: 104, branch: 67, core_var_decl: 61
- `src/Compilers/CSharp/Portable/Symbols/Source/SourceEventSymbol.cs` (CSHARP) | Magnitude: 518.88 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 740, branch: 132, structural_boundaries: 109, state_mutation: 74
- `src/Compilers/Core/Portable/Emit/EditAndContinue/DeltaMetadataWriter.cs` (CSHARP) | Magnitude: 1091.98 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 1529, structural_boundaries: 280, branch: 217, core_var_decl: 182
- `src/Compilers/CSharp/Test/Syntax/Syntax/SyntaxTests.cs` (CSHARP) | Magnitude: 102.08 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 272, decorators: 63, structural_boundaries: 47, test: 35
- `src/Dependencies/Collections/Internal/ThrowHelper.cs` (CSHARP) | Magnitude: 147.12 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 287, structural_boundaries: 53, args: 48, branch: 39

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/Analyzers/Core/Analyzers/AbstractCodeQualityDiagnosticAnalyzer.cs` (CSHARP) | Magnitude: 22.44 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 38, core_var_decl: 8, structural_boundaries: 7, args: 7
- `src/LanguageServer/ProtocolUnitTests/CodeLens/AbstractCodeLensTests.cs` (CSHARP) | Magnitude: 52.24 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 60, structural_boundaries: 40, core_var_decl: 23, design_camel_case: 19
- `src/Compilers/Core/Portable/Operations/ControlFlowGraphBuilder.InterpolatedStringContext.cs` (CSHARP) | Magnitude: 41.64 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, api: 10, structural_boundaries: 9, immutability_locks: 9
- `src/Features/CSharp/Portable/Completion/CompletionProviders/NamedParameterCompletionProvider.cs` (CSHARP) | Magnitude: 120.44 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 184, structural_boundaries: 103, args: 42, core_var_decl: 35
- `src/Compilers/CSharp/Portable/Binder/WithExternAndUsingAliasesBinder.cs` (CSHARP) | Magnitude: 110.86 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 194, encapsulation: 34, structural_boundaries: 30, immutability_locks: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/Core/MetaAnalyzers/DiagnosticDescriptorCreationAnalyzer_IdRangeAndCategoryValidation.cs` (CSHARP) | Magnitude: 267.1 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 302, core_var_decl: 59, branch: 55, structural_boundaries: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/Workspaces/MSBuild/Test/Utilities/DotNetSdkMSBuildInstalled.cs` (CSHARP) | Magnitude: 28.14 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 35, structural_boundaries: 13, safety: 10, branch: 9
- `src/RoslynAnalyzers/Utilities/Compiler/Options/ValueUsageInfo.cs` (CSHARP) | Magnitude: 13.6 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 36, indent_spaces: 24, core_var_decl: 9, design_pascal_case: 9
- `src/RoslynAnalyzers/PublicApiAnalyzers/Core/Analyzers/PublicApiFile.cs` (CSHARP) | Magnitude: 17.82 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 7, api: 4, core_var_decl: 4
- `src/Dependencies/Contracts/ExperimentalAttribute.cs` (CSHARP) | Magnitude: 7.26 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: doc: 26, indent_spaces: 21, macros: 5, structural_boundaries: 4
- `src/RoslynAnalyzers/Microsoft.CodeAnalysis.Analyzers/UnitTests/MetaAnalyzers/DoNotUseFileLocalTypesForAnalyzersOrGeneratorsTests.cs` (CSHARP) | Magnitude: 58.14 | Delta: **0.075** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 31, core_var_decl: 18, design_pascal_case: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/Analyzers/CSharp/Analyzers/UseCompoundAssignment/CSharpUseCompoundCoalesceAssignmentDiagnosticAnalyzer.cs` (CSHARP) | Magnitude: 93.6 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 52, branch: 30, core_var_decl: 23
- `src/EditorFeatures/CSharp/EventHookup/EventHookupCommandHandler_TabKeyCommand.cs` (CSHARP) | Magnitude: 174.06 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 234, structural_boundaries: 129, core_var_decl: 66, design_camel_case: 52
- `src/Analyzers/CSharp/CodeFixes/UseCollectionExpression/CSharpUseCollectionExpressionForStackAllocCodeFixProvider.cs` (CSHARP) | Magnitude: 37.8 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 36, args: 14, core_var_decl: 13
- `src/Workspaces/Core/Portable/Shared/Utilities/SemanticMap.Walker.cs` (CSHARP) | Magnitude: 22.96 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 11, branch: 7, args: 3
- `src/Features/Core/Portable/EmbeddedLanguages/ExportEmbeddedLanguageFeatureServiceAttribute.cs` (CSHARP) | Magnitude: 37.76 | Delta: **0.016** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 25, doc: 18, safety: 12, api: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/LanguageServerProjectSystem.cs` -> Churn: **72.27%** | Cog Load: 93.5253% | Debt: 68.9269%
- `src/Workspaces/CoreTestUtilities/Workspaces/TestWorkspace`1.cs` -> Churn: **71.82%** | Cog Load: 25.8807% | Debt: 93.1619%
- `src/LanguageServer/Protocol.TestUtilities/LanguageServer/AbstractLanguageServerProtocolTests.cs` -> Churn: **71.5%** | Cog Load: 59.8399% | Debt: 93.0631%
- `src/Compilers/CSharp/Portable/Errors/ErrorFacts.cs` -> Churn: **70.74%** | Cog Load: 55.9365% | Debt: 10.7768%
- `src/LanguageServer/Microsoft.CodeAnalysis.LanguageServer/HostWorkspace/WorkspaceProjectFactoryService.cs` -> Churn: **69.6%** | Cog Load: 27.6684% | Debt: 99.9729%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/EditorFeatures/CSharpTest/CompleteStatement/CSharpCompleteStatementCommandHandlerTests.cs` -> **DoctorKrolic** (100.0% isolated ownership) | Magnitude: 11373.46
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncSpillTests.cs` -> **Fred Silberberg** (100.0% isolated ownership) | Magnitude: 7953.92
- `src/Compilers/CSharp/Test/Symbol/Symbols/StaticAbstractMembersInInterfacesTests.cs` -> **Copilot** (100.0% isolated ownership) | Magnitude: 7314.18
- `src/Compilers/CSharp/Test/Emit/CodeGen/CodeGenAsyncTests.cs` -> **Fred Silberberg** (87.5% isolated ownership) | Magnitude: 6089.54
- `src/Compilers/CSharp/Test/Emit3/RefStructInterfacesTests.cs` -> **AlekseyTs** (100.0% isolated ownership) | Magnitude: 5916.28

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 15.641** (Embedded: 0.3 * Error Risk: 52.1415%)
- `src/LanguageServer/Protocol/Extensions/ProtocolConversions.Diagnostics.cs` -> **Severity: 11.951** (Embedded: 0.194 * Error Risk: 61.5947%)
- `src/ExpressionEvaluator/Core/Source/ResultProvider/SystemHelpers.cs` -> **Severity: 10.921** (Embedded: 0.2216 * Error Risk: 49.2858%)
- `src/LanguageServer/Protocol/Handler/Diagnostics/DiagnosticSources/TaskListDiagnosticSource.cs` -> **Severity: 10.488** (Embedded: 0.194 * Error Risk: 54.0608%)
- `src/Compilers/Core/Portable/InternalUtilities/Hash.cs` -> **Severity: 8.186** (Embedded: 0.1336 * Error Risk: 61.2824%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/Tools/ExternalAccess/Razor/Features/Cohost/Handlers/Diagnostics.cs` -> **Severity: 12083.2** (Blast Radius: 120.832 * Doc Risk: 100.0%)
- `src/LanguageServer/Protocol/Handler/Diagnostics/DiagnosticSources/TaskListDiagnosticSource.cs` -> **Severity: 5120.6** (Blast Radius: 51.206 * Doc Risk: 100.0%)
- `src/LanguageServer/Protocol/Extensions/ProtocolConversions.Diagnostics.cs` -> **Severity: 3585.61** (Blast Radius: 51.223 * Doc Risk: 70.0%)
- `src/ExpressionEvaluator/Core/Source/ResultProvider/SystemHelpers.cs` -> **Severity: 3553.2** (Blast Radius: 35.532 * Doc Risk: 100.0%)
- `src/Workspaces/Core/Portable/TaskList/TaskListItemDescriptor.cs` -> **Severity: 1438.5** (Blast Radius: 14.385 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 39312 literal sites + 16 sites through wrappers = 39328
- **`panics_and_aborts`:** 22191 literal sites + 40 sites through wrappers = 22231

- `SetValueForIsNullComparisonOperator` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`
- `IsStringProperty` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `src/Compilers/Core/Portable/Symbols/Attributes/CommonAttributeData.cs`
- `ReportUnhandledException` (function, debug_prints, primitive): 4 call sites in 1 files -- `src/Interactive/Host/Interactive/Core/InteractiveHost.Service.cs`
- `SetValueForEqualsOrNotEqualsComparisonOperator` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`
- `ThrowDestinationTooShort` (function, panics_and_aborts, primitive): 3 call sites in 2 files -- `src/Compilers/Core/Portable/Hashing/NonCryptographicHashAlgorithm.cs`
- `IsReachableBlockData` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`
- `LogCore` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/Tools/BuildValidator/DemoLogger.cs`
- `StartTrackingPredicatedData` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/RoslynAnalyzers/Utilities/FlowAnalysis/FlowAnalysis/Framework/DataFlow/DataFlowOperationVisitor.cs`
- `ThrowArgumentItemNullException` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/Workspaces/SharedUtilitiesAndExtensions/Compiler/Core/Utilities/PublicContract.cs`
- `ThrowFailedTransferExceptionForCapture` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/Workspaces/CoreTestUtilities/TestExportJoinableTaskContext+DenyExecutionSynchronizationContext.cs`
- `WithChangedOptionInternal` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/Workspaces/Core/Portable/Options/OptionSet.cs`
- `WriteUsage` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/Tools/Source/CompilerGeneratorTools/Source/CSharpSyntaxGenerator/Program.cs`
*(+18 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 667808 call pairs -- scoped 30.7%, unique 0.5%, ambiguous 49.5%, external 19.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 666928 | 30.7% | 0.5% | 49.6% | 19.3% |
| shell | 416 | 34.4% | 3.4% | 0.5% | 61.8% |
| powershell | 356 | 21.9% | 6.5% | 0.0% | 71.6% |
| python | 108 | 12.0% | 0.0% | 0.0% | 88.0% |

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
