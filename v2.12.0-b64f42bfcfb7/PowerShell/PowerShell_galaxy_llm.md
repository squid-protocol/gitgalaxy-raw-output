# ARCHITECTURAL_BRIEF: PowerShell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/PowerShell/PowerShell` |
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
- **Scope:** 2136 analyzed artifact(s), 608623 LOC.
- **Load-bearing artifact:** `src/System.Management.Automation/utils/MshTraceSource.cs` -- 251 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHost.cs` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` at magnitude 7040.34 (structural weight, not risk).
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
| Total Artifacts | 2674 |
| Analyzed Artifacts (Scanned) | 2136 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 538 |
| Total LOC | 608623 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 79.9% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5083 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1047 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.1319 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 145 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1340 | 494114 | 62.7% |
| POWERSHELL | 543 | 103594 | 25.4% |
| XML | 80 | 0 | 3.7% |
| MARKDOWN | 71 | 0 | 3.3% |
| YAML | 39 | 2403 | 1.8% |
| JSON | 30 | 6734 | 1.4% |
| SHELL | 13 | 1304 | 0.6% |
| PLAINTEXT | 11 | 0 | 0.5% |
| CSV | 7 | 386 | 0.3% |
| BATCH | 1 | 1 | 0.0% |
| DOCKERFILE | 1 | 87 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2110 |
| utf-8 | bom | 26 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Encapsulated Accessors Files 25%, Declarative / Non-Code 21%, Data / Markup / Trivial 13%, Large Core Modules (3) 9%, State Mutators Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2054 | 96.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 82 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 538*

**Composition by Extension & Reason:**
- `.resx`: 166x Unsupported Format (.resx)
- `.yml`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 59 exceeds 500 chars)
- `.png`: 61x Excluded (Explicitly Denied Extension: '.png'), 2x Excluded (Explicitly Denied Extension: '.PNG')
- `.csproj`: 33x Unsupported Format (.csproj), 7x Excluded (Unsupported Extension: '.csproj'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 28x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Unsupported Format (.undeterminable)
- `.ps1`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3016 commas in 647 LOC)
- `.xaml`: 16x Unsupported Format (.xaml)
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 4630 LOC)
- `.cab`: 12x Excluded (Explicitly Denied Extension: '.cab')
- `.zip`: 10x Excluded (Explicitly Denied Extension: '.zip')
- `.ico`: 6x Excluded (Explicitly Denied Extension: '.ico')
- `.mof`: 6x Excluded (Unsupported Extension: '.mof')
- `.cs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2159 LOC), 1x Excluded (Machine-Generated Source Code Signature: 2240 LOC)
- `.config`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.7 | 11.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.0 | 41.4 | 49.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 20.8 | 8.3 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 84.1 | 3.4 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 43.7 | 16.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 84.7 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.3 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.1 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.6 | 2.9 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7366 | 768 | 8 | `tools/packaging/packaging.psm1` |
| cleanup | 2150 | 444 | 2 | `test/powershell/Modules/Microsoft.PowerShell.Utility/Implicit.Remoting.Tests.ps1` |
| guards | 58625 | 1550 | 70 | `src/System.Management.Automation/engine/parser/Compiler.cs` |
| danger | 9589 | 955 | 12 | `tools/packaging/packaging.psm1` |
| concurrency | 2387 | 349 | 2 | `test/powershell/Modules/Microsoft.PowerShell.Utility/Foreach-Object-Parallel.Tests.ps1` |
| connectivity | 30633 | 1422 | 35 | `src/Microsoft.PowerShell.Commands.Management/commands/management/GetComputerInfoCommand.cs` |
| io | 3286 | 345 | 2 | `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` |
| crypto | 0 | 0 | 0 | - |
| ipc | 1122 | 90 | 0 | `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` |
| time | 612 | 164 | 0 | `test/powershell/Modules/Microsoft.PowerShell.Utility/Get-Date.Tests.ps1` |
| serialization | 692 | 45 | 0 | `test/powershell/Modules/Microsoft.PowerShell.Utility/ConvertTo-Json.Tests.ps1` |
| regex | 1216 | 196 | 0 | `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` |
| events | 5159 | 480 | 6 | `tools/packaging/packaging.psm1` |
| tests | 28365 | 481 | 35 | `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` |
| docs | 139219 | 1193 | 164 | `src/System.Management.Automation/engine/parser/ast.cs` |
| debt | 1519 | 343 | 1 | `tools/AttackSurfaceAnalyzer/Summarize-AsaResults.ps1` |
| mutation | 140274 | 1780 | 155 | `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` |
| dead_code | 5814 | 1112 | 7 | `src/System.Management.Automation/engine/parser/Compiler.cs` |
| credential | 69 | 28 | 0 | `tools/packaging/packaging.psm1` |
| threat | 30 | 8 | 0 | `test/powershell/Modules/Microsoft.PowerShell.Management/FileSystemProviderExtended.Tests.ps1` |
| ml_ai | 173 | 73 | 0 | `src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleControl.cs` |
| ui | 224 | 58 | 0 | `src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/ManagementList.Generated.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` (Hits: 724)
- `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` (Hits: 76)
- `test/powershell/Modules/Microsoft.PowerShell.Management/Get-Content.Tests.ps1` (Hits: 69)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **MshTraceSource.cs** (`src/System.Management.Automation/utils/MshTraceSource.cs`) — 251 inbound connections
2. **assert.cs** (`src/System.Management.Automation/utils/assert.cs`) — 215 inbound connections
3. **StringUtil.cs** (`src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/StringUtil.cs`) — 210 inbound connections
4. **cmdlet.cs** (`src/System.Management.Automation/engine/cmdlet.cs`) — 172 inbound connections
5. **MshObject.cs** (`src/System.Management.Automation/engine/MshObject.cs`) — 127 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ConsoleHost.cs** (`src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHost.cs`) — 29 outbound dependencies
2. **serialization.cs** (`src/System.Management.Automation/engine/serialization.cs`) — 26 outbound dependencies
3. **CompletionCompleters.cs** (`src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) — 25 outbound dependencies
4. **LanguagePrimitives.cs** (`src/System.Management.Automation/engine/LanguagePrimitives.cs`) — 24 outbound dependencies
5. **ImportModuleCommand.cs** (`src/System.Management.Automation/engine/Modules/ImportModuleCommand.cs`) — 24 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `LoadModuleManifest` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs`) -> Impact: **1332.4** | LOC: 2053
  * *Intent:* /// Routine to process the module manifest data language script. /// </summary> /// <param name="moduleManifestPath">The path to the manifest file.</p...
- `Start-PSBuild` **(Many-Argument Workhorses)** (@ `build.psm1`) -> Impact: **642.7** | LOC: 481
- `Start-PSPackage` **(Many-Argument Workhorses)** (@ `tools/packaging/packaging.psm1`) -> Impact: **608.8** | LOC: 711
- `GetResultHelper` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionAnalysis.cs`) -> Impact: **566.4** | LOC: 808
- `Start-PSBuild` **(Many-Argument Workhorses)** (@ `test/perf/benchmarks/assets/compiler.test.ps1`) -> Impact: **516.6** | LOC: 404
- `Start-PSPester` **(Many-Argument Workhorses)** (@ `test/perf/benchmarks/assets/compiler.test.ps1`) -> Impact: **489.7** | LOC: 354
- `Start-PSPester` **(Many-Argument Workhorses)** (@ `build.psm1`) -> Impact: **487.2** | LOC: 363
- `Start-PSPackage` **(Many-Argument Workhorses)** (@ `test/perf/benchmarks/assets/compiler.test.ps1`) -> Impact: **467.8** | LOC: 525
- `SetValueImpl` **(Compute Cores)** (@ `src/System.Management.Automation/engine/runtime/MutableTuple.cs`) -> Impact: **455.4** | LOC: 135
- `NativeCommandArgumentCompletion` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> Impact: **417.0** | LOC: 403

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/System.Management.Automation/engine` | 147 | 49500.86 | 13.96% | 32.22% |
| `src/System.Management.Automation/engine/parser` | 18 | 25509.92 | 30.48% | 41.32% |
| `src/System.Management.Automation/engine/CommandCompletion` | 8 | 11298.94 | 24.88% | 19.09% |
| `src/System.Management.Automation/namespaces` | 33 | 11168.11 | 9.34% | 33.57% |
| `src/Microsoft.PowerShell.Commands.Utility/commands/utility` | 90 | 11122.3 | 12.41% | 24.45% |
| `test/powershell/Modules/Microsoft.PowerShell.Utility` | 121 | 10859.6 | 19.27% | 0.0% |
| `src/System.Management.Automation/engine/Modules` | 16 | 10390.74 | 22.01% | 29.83% |
| `src/Microsoft.PowerShell.Commands.Management/commands/management` | 52 | 10276.76 | 12.55% | 27.68% |
| `src/System.Management.Automation/engine/hostifaces` | 33 | 9965.82 | 16.34% | 41.8% |
| `src/System.Management.Automation/engine/remoting/commands` | 28 | 9185.4 | 16.56% | 22.19% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/System.Management.Automation/CoreCLR/CorePsStub.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/ComInterop/Errors.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/parser/PreOrderVisitor.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/remoting/client/remotingprotocol.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/remoting/common/PSSessionConfigurationTypeOption.cs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/skills/analyze-pester-failures/scripts/analyze-pr-test-failures.ps1` -> **100.0%** Exposure
- `assets/MicrosoftUpdate/RegisterMicrosoftUpdate.ps1` -> **100.0%** Exposure
- `build.psm1` -> **100.0%** Exposure
- `dsc/pwsh.profile.resource.ps1` -> **100.0%** Exposure
- `src/Modules/Windows/Microsoft.PowerShell.Security/Security.types.ps1xml` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/System.Management.Automation/utils/tracing/TracingGen.cs` -> **82** Orphaned Functions | **0** Duplicates
- `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` -> **71** Orphaned Functions | **4** Duplicates
- `test/xUnit/csharp/test_CommandLineParser.cs` -> **67** Orphaned Functions | **2** Duplicates
- `src/System.Management.Automation/engine/parser/TypeInferenceVisitor.cs` -> **65** Orphaned Functions | **0** Duplicates
- `src/System.Management.Automation/engine/parser/PreOrderVisitor.cs` -> **64** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `test/powershell/Modules/Microsoft.PowerShell.Security/TestData/CatalogTestData/CatalogTestFile2.xml` -> **100.0%** Exposure
- `test/powershell/Modules/Microsoft.PowerShell.Security/CmsMessage.Tests.ps1` -> **94.8688%** Exposure
- `test/powershell/Modules/Microsoft.PowerShell.Security/CmsMessage2.Tests.ps1` -> **88.341%** Exposure
- `src/System.Management.Automation/security/SecuritySupport.cs` -> **19.5611%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `10` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `7388` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.694)
- **Top Global Matches:** file_cluster_6: 6.694, file_cluster_4: 9.747, file_cluster_8: 16.375
- **Magnitude:** 7040.34 | **LOC:** 9263 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **25**; blast radius 0.296; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Complexity Load (formerly Cognitive Load) (52.8%)
- **Documentation Coverage:** 82.7298% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NativeCommandArgumentCompletion` **(Many-Argument Workhorses)** (Impact: 417.0)
  * `CompleteHashtableKey` **(Many-Argument Workhorses)** (Impact: 179.4)
  * `CompleteCommandArgument` **(Many-Argument Workhorses)** (Impact: 176.8)
    * *Intent:* #endregion Command Parameters #region Command Arguments
  * `EscapeCharIfNeeded` **(Many-Argument Workhorses)** (Impact: 135.9)
  * `GetDefaultProviderResults` **(Many-Argument Workhorses)** (Impact: 126.5)
    * *Intent:* /// <summary> /// Helper method for generating path completion results standard providers that don't...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 682 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 2211
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1797`, `structural_boundaries: 1116`, `args: 287`, `func_start: 230`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 847`, `dead_code: 2`, `duplicate_logic: 4`, `unreferenced_by_name: 71`
* *Architecture:* `io: 8`, `api: 158`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 390`, `doc: 273`, `sync_locks: 2`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.296
  * `Choke Point (Betweenness):` 0.001273 | `Ripple Effect (Closeness):` 0.057446
  * `Imports (Out-Degree: 28):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Options, Microsoft.PowerShell, Microsoft.PowerShell.Cim, Microsoft.PowerShell.Commands, Microsoft.PowerShell.Commands.Internal.Format, System.Buffers, System.Collections...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.368)
- **Top Global Matches:** file_cluster_6: 7.368, file_cluster_4: 9.461, file_cluster_16: 16.548
- **Magnitude:** 5267.42 | **LOC:** 7495 | **CtrlFlow:** 18.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **21**; blast radius 1.017; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.1%), Complexity Load (formerly Cognitive Load) (38.2%)
- **Documentation Coverage:** 44.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoadModuleManifest` **(Many-Argument Workhorses)** (Impact: 1332.4)
    * *Intent:* /// Routine to process the module manifest data language script. /// </summary> /// <param name="mod...
  * `LoadBinaryModule` **(Many-Argument Workhorses)** (Impact: 230.9)
    * *Intent:* /// <param name="assemblyToLoad">The assembly to load so no lookup need be done.</param> /// <param ...
  * `LoadModule` **(Many-Argument Workhorses)** (Impact: 230.3)
    * *Intent:* /// <summary> /// Load a module from a file... /// </summary> /// <param name="parentModule">The par...
  * `LoadModuleNamedInManifest` **(Many-Argument Workhorses)** (Impact: 141.0)
  * `ImportModuleMembers` **(Many-Argument Workhorses)** (Impact: 128.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 485 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1040`, `structural_boundaries: 343`, `args: 99`, `func_start: 89`, `class_start: 5`
* *Risk/State:* `state_mutation: 660`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 5`
* *Architecture:* `io: 76`, `api: 85`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 171`, `doc: 527`, `sync_locks: 10`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.017
  * `Choke Point (Betweenness):` 0.005606 | `Ripple Effect (Closeness):` 0.079042
  * `Imports (Out-Degree: 31):` Microsoft.PowerShell.Cmdletization, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Globalization...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/parser/ast.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.492)
- **Top Global Matches:** file_cluster_16: 7.492, file_cluster_0: 8.176, file_cluster_15: 8.836
- **Magnitude:** 4568.38 | **LOC:** 10846 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **15**; blast radius 1.321; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.9%), Complexity Load (formerly Cognitive Load) (24.7%)
- **Documentation Coverage:** 47.0167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ToStringForSerialization` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `ScriptBlockAst` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// This construction uses explicitly named begin/process/end/clean blocks. /// </summary> /// <para...
  * `InternalVisit` **(Compute Cores)** (Impact: 30.7)
  * `GenerateCommandCallPipelineAst` **(I/O & Config Routines)** (Impact: 29.5)
  * `IsImportCommand` **(Many-Argument Workhorses)** (Impact: 27.0)
    * *Intent:* #endregion #region static fields/methods /// <summary> /// </summary> /// <param name="stmt"></param...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 435 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 1441
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 810`, `structural_boundaries: 1023`, `args: 442`, `func_start: 462`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 571`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 20`
* *Architecture:* `api: 761`, `concurrency: 9`, `import: 17`
* *Defense:* `safety: 309`, `doc: 2823`, `sync_locks: 6`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.321
  * `Choke Point (Betweenness):` 0.003426 | `Ripple Effect (Closeness):` 0.086213
  * `Imports (Out-Degree: 23):` Microsoft.PowerShell, Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.Linq...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/parser/Parser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.225)
- **Top Global Matches:** file_cluster_6: 6.225, file_cluster_4: 9.723, file_cluster_8: 15.947
- **Magnitude:** 4523.36 | **LOC:** 8280 | **CtrlFlow:** 19.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **16**; blast radius 2.74; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (62.7%), Guard Balance (formerly Safety Score) (57.7%)
- **Documentation Coverage:** 89.4231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SwitchStatementRule` **(Many-Argument Workhorses)** (Impact: 130.0)
  * `ConfigurationStatementRule` **(Many-Argument Workhorses)** (Impact: 120.2)
  * `GetCommandArgument` **(Many-Argument Workhorses)** (Impact: 100.9)
  * `ClassMemberRule` **(Many-Argument Workhorses)** (Impact: 97.8)
  * `DynamicKeywordStatementRule` **(Many-Argument Workhorses)** (Impact: 91.1)
    * *Intent:* /// <summary> /// Parse a dynamic keyword statement which will be either of the form /// keyword [pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 552 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 1804
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1186`, `structural_boundaries: 498`, `args: 205`, `func_start: 157`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 700`, `dead_code: 5`, `planned_debt: 6`, `unreferenced_by_name: 16`
* *Architecture:* `io: 7`, `api: 67`, `concurrency: 4`, `import: 18`
* *Defense:* `safety: 423`, `doc: 130`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.74
  * `Choke Point (Betweenness):` 0.004995 | `Ripple Effect (Closeness):` 0.100043
  * `Imports (Out-Degree: 19):` Microsoft.PowerShell.DesiredStateConfiguration.Internal, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.Tracing, System.Globalization, System.IO, System.Linq...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.847)
- **Top Global Matches:** file_cluster_4: 5.847, file_cluster_16: 8.655, file_cluster_15: 9.946
- **Magnitude:** 4438.7 | **LOC:** 7952 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **21**; blast radius 2.013; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.8%), Complexity Load (formerly Cognitive Load) (34.9%)
- **Documentation Coverage:** 92.9705% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InvokeMethod` **(Many-Argument Workhorses)** (Impact: 123.4)
  * `GetPSMemberInfo` **(Many-Argument Workhorses)** (Impact: 104.1)
  * `FallbackSetMember` **(Many-Argument Workhorses)** (Impact: 101.2)
  * `BinaryNumericOp` **(Many-Argument Workhorses)** (Impact: 81.8)
  * `FallbackInvokeMember` **(Many-Argument Workhorses)** (Impact: 78.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 394 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 1342
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 978`, `structural_boundaries: 1103`, `args: 350`, `func_start: 268`, `class_start: 37`
* *Risk/State:* `state_mutation: 554`, `dead_code: 31`, `planned_debt: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 203`, `concurrency: 8`, `import: 25`
* *Defense:* `safety: 243`, `doc: 113`, `sync_locks: 37`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.013
  * `Choke Point (Betweenness):` 0.005416 | `Ripple Effect (Closeness):` 0.102356
  * `Imports (Out-Degree: 16):` System.Buffers, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.Specialized, System.Data, System.Dynamic, System.Globalization...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `build.psm1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.52)
- **Top Global Matches:** file_cluster_6: 8.52, file_cluster_4: 10.994, file_cluster_8: 17.353
- **Magnitude:** 4286.82 | **LOC:** 4068 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 1.889; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (89.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.4%)
- **Documentation Coverage:** 48.6207% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Start-PSBuild` **(Many-Argument Workhorses)** (Impact: 642.7)
  * `Start-PSPester` **(Many-Argument Workhorses)** (Impact: 487.2)
  * `Start-PSBootstrap` **(Many-Argument Workhorses)** (Impact: 201.0)
  * `Install-Dotnet` **(Many-Argument Workhorses)** (Impact: 106.5)
  * `New-PSOptions` **(Many-Argument Workhorses)** (Impact: 103.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 526 instances
* *High Risk Execution (weighted view):* 4
* *State Mutation (weighted view):* 1698
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 748`, `structural_boundaries: 176`, `args: 72`, `func_start: 85`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 21`, `high_risk_execution: 8`, `state_mutation: 646`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 34`, `api: 47`, `import: 2`
* *Defense:* `safety: 58`, `doc: 15`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.889
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.005206
  * `Imports (Out-Degree: 2):` $PSScriptRoot\tools\buildCommon\startNativeExecution.ps1, $PSScriptRoot\tools\wix\wix.psm1
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/namespaces/FileSystemProvider.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.816)
- **Top Global Matches:** file_cluster_4: 6.816, file_cluster_6: 8.368, file_cluster_16: 13.495
- **Magnitude:** 3672.86 | **LOC:** 9539 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **22**; blast radius 0.702; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Complexity Load (formerly Cognitive Load) (12.4%)
- **Documentation Coverage:** 43.8053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewItem` **(Many-Argument Workhorses)** (Impact: 164.3)
    * *Intent:* /// Specify "directory" or "container" to create a directory. /// </param> /// <param name="value"> ...
  * `Dir` **(Many-Argument Workhorses)** (Impact: 98.7)
  * `PerformCopyFileFromRemoteSession` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `CopyFileStreamToRemoteSession` **(Stateful Encapsulated Methods)** (Impact: 59.2)
  * `NormalizeRelativePath` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* /// </summary> /// <param name="path"> /// A fully qualifiedpath to an item. The item must exist, //...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 346 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 874`, `structural_boundaries: 412`, `args: 161`, `func_start: 154`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 508`, `unreferenced_by_name: 31`
* *Architecture:* `io: 58`, `api: 143`, `concurrency: 2`, `import: 23`
* *Defense:* `safety: 498`, `doc: 1040`, `immutability_locks: 59`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.702
  * `Choke Point (Betweenness):` 0.00278 | `Ripple Effect (Closeness):` 0.074948
  * `Imports (Out-Degree: 28):` Microsoft.Win32.SafeHandles, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/parser/Compiler.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.444)
- **Top Global Matches:** file_cluster_4: 7.444, file_cluster_16: 10.11, file_cluster_15: 10.891
- **Magnitude:** 3655.58 | **LOC:** 7080 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **18**; blast radius 0.931; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (72.6%), Guard Balance (formerly Safety Score) (57.0%), Debt Markers (formerly Tech Debt) (37.3%)
- **Documentation Coverage:** 96.7359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisitBinaryExpression` **(Compute Cores)** (Impact: 106.5)
  * `NewParameterAttribute` **(Compute Cores)** (Impact: 43.8)
  * `CompileStatementListWithTraps` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `GetRedirectedExpression` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* // A redirected expression requires extra work because there is no CommandProcessor or PipelineProce...
  * `VisitPipeline` **(Defensive Guards)** (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 391 instances
* *State Mutation (weighted view):* 1422
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 831`, `args: 293`, `func_start: 204`, `class_start: 16`
* *Risk/State:* `state_mutation: 640`, `dead_code: 69`, `planned_debt: 17`, `unreferenced_by_name: 61`
* *Architecture:* `io: 4`, `api: 415`, `import: 19`
* *Defense:* `safety: 332`, `doc: 53`, `sync_locks: 2`, `immutability_locks: 266`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.931
  * `Choke Point (Betweenness):` 0.001289 | `Ripple Effect (Closeness):` 0.083483
  * `Imports (Out-Degree: 23):` Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized, System.Diagnostics, System.Dynamic, System.Globalization...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `test/perf/benchmarks/assets/compiler.test.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.139)
- **Top Global Matches:** file_cluster_8: 9.139, file_cluster_6: 19.127, file_cluster_3: 19.746
- **Magnitude:** 3586.42 | **LOC:** 2686 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.7%), Complexity Load (formerly Cognitive Load) (46.2%), Connectivity (formerly Api Exposure) (5.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Start-PSBuild` **(Many-Argument Workhorses)** (Impact: 516.6)
  * `Start-PSPester` **(Many-Argument Workhorses)** (Impact: 489.7)
  * `Start-PSPackage` **(Many-Argument Workhorses)** (Impact: 467.8)
  * `New-UnixPackage` **(Many-Argument Workhorses)** (Impact: 169.0)
  * `Start-PSBootstrap` **(Many-Argument Workhorses)** (Impact: 150.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Amplified Cascading Flux:* 380 instances
* *High Risk Execution (weighted view):* 3
* *State Mutation (weighted view):* 1228
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 591`, `structural_boundaries: 75`, `args: 27`, `func_start: 29`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 16`, `high_risk_execution: 9`, `state_mutation: 468`, `fragile_debt: 6`, `unreferenced_by_name: 6`
* *Architecture:* `io: 8`, `api: 9`, `import: 1`
* *Defense:* `safety: 50`, `doc: 4`, `test: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Microsoft.WSMan.Management/ConfigProvider.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.517)
- **Top Global Matches:** file_cluster_6: 5.517, file_cluster_4: 10.638, file_cluster_8: 14.528
- **Magnitude:** 3510.16 | **LOC:** 6578 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.4%), Complexity Load (formerly Cognitive Load) (22.4%)
- **Documentation Coverage:** 34.6939% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetChildItemsOrNames` **(Many-Argument Workhorses)** (Impact: 226.1)
    * *Intent:* /// <summary> /// Get the child items or Names. Used by GetChildItems and GetChildNames. /// </summa...
  * `SetItem` **(Many-Argument Workhorses)** (Impact: 151.7)
    * *Intent:* /// <summary> /// This cmdlet is used to set the value of a particular item. /// cd wsman:\localhost...
  * `GetItem` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* /// <summary> /// This cmdlet is used to get a particular item. /// cd wsman:\localhost\client> Get-...
  * `GetCorrectCaseOfName` **(Many-Argument Workhorses)** (Impact: 92.5)
  * `NewItemPluginOrPluginChild` **(Many-Argument Workhorses)** (Impact: 89.8)
    * *Intent:* /// <summary> /// This method creates the Plugin and its child items in wsman provider. /// This is ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 351 instances
* *State Mutation (weighted view):* 1246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 895`, `structural_boundaries: 306`, `args: 91`, `func_start: 89`, `class_start: 15`
* *Risk/State:* `state_mutation: 544`, `dead_code: 33`, `planned_debt: 4`, `unreferenced_by_name: 11`
* *Architecture:* `io: 6`, `api: 108`, `import: 16`
* *Defense:* `safety: 83`, `doc: 723`, `sync_locks: 10`, `immutability_locks: 58`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.IO, System.Management.Automation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/tokenizer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.065)
- **Top Global Matches:** file_cluster_6: 7.065, file_cluster_4: 7.578, file_cluster_16: 14.72
- **Magnitude:** 3344.54 | **LOC:** 5084 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **13**; blast radius 0.417; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (41.8%)
- **Documentation Coverage:** 85.1613% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ScanVariable` **(Many-Argument Workhorses)** (Impact: 242.3)
    * *Intent:* #endregion Strings #region Variables // Scan a variable - the first character ($ or @) has been cons...
  * `TryGetNumberValue` **(Many-Argument Workhorses)** (Impact: 241.3)
  * `ScanNumberHelper` **(Many-Argument Workhorses)** (Impact: 224.7)
    * *Intent:* /// <summary> /// Scans a numeric string to determine its characteristics. /// </summary> /// <param...
  * `NextToken` **(I/O & Config Routines)** (Impact: 181.5)
  * `HandleRequiresParameter` **(Many-Argument Workhorses)** (Impact: 169.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 335 instances
* *State Mutation (weighted view):* 1070
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1055`, `structural_boundaries: 376`, `args: 129`, `func_start: 119`, `class_start: 11`
* *Risk/State:* `state_mutation: 400`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 88`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 97`, `doc: 235`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.417
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.076581
  * `Imports (Out-Degree: 12):` Microsoft.PowerShell.Commands, Microsoft.PowerShell.DesiredStateConfiguration.Internal, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Globalization, System.Linq...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/serialization.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.676)
- **Top Global Matches:** file_cluster_16: 6.676, file_cluster_15: 8.199, file_cluster_0: 8.477
- **Magnitude:** 2999.06 | **LOC:** 7680 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **26**; blast radius 3.876; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (20.0%)
- **Documentation Coverage:** 44.6985% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HandleKnownContainerTypes` **(Many-Argument Workhorses)** (Impact: 53.3)
  * `GetKnownContainerTypeInfo` **(Many-Argument Workhorses)** (Impact: 49.7)
    * *Intent:* /// <summary> /// Checks if source is known container type and returns appropriate /// information. ...
  * `HandleComplexTypePSObject` **(Many-Argument Workhorses)** (Impact: 49.6)
  * `RehydrateCimInstance` **(Defensive Guards)** (Impact: 37.4)
    * *Intent:* // NOTE: Win7 change for refid-s that span multiple xml documents: ADMIN: changelist #226414
  * `RehydrateCimClass` **(Defensive Guards)** (Impact: 35.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 206 instances
* *State Mutation (weighted view):* 958
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 403`, `args: 326`, `func_start: 295`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 546`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 248`, `import: 26`
* *Defense:* `safety: 220`, `doc: 1125`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.876
  * `Choke Point (Betweenness):` 0.005244 | `Ripple Effect (Closeness):` 0.115732
  * `Imports (Out-Degree: 23):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Serialization, Microsoft.PowerShell.Commands, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized...
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/CoreAdapter.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.873)
- **Top Global Matches:** file_cluster_16: 7.873, file_cluster_4: 8.927, file_cluster_0: 9.971
- **Magnitude:** 2897.48 | **LOC:** 6260 | **CtrlFlow:** 15.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **21**; blast radius 1.675; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.8%), Complexity Load (formerly Cognitive Load) (32.4%)
- **Documentation Coverage:** 62.7907% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FindBestMethodImpl` **(Many-Argument Workhorses)** (Impact: 183.2)
  * `CompareOverloadCandidates` **(Many-Argument Workhorses)** (Impact: 77.0)
    * *Intent:* /// <summary> /// Compare the 2 methods, determining which method is better. /// </summary> /// <ret...
  * `GetMethodInvoker` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `DoBoxingIfNecessary` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `PopulatePropertyReflectionTable` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /// <summary> /// Called from GetPropertyReflectionTable within a lock to fill the /// property cach...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 263 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 877
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 656`, `structural_boundaries: 518`, `args: 276`, `func_start: 226`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 351`, `dead_code: 3`, `planned_debt: 5`, `duplicate_logic: 5`, `unreferenced_by_name: 22`
* *Architecture:* `api: 134`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 234`, `doc: 851`, `sync_locks: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.675
  * `Choke Point (Betweenness):` 0.001915 | `Ripple Effect (Closeness):` 0.100043
  * `Imports (Out-Degree: 15):` Microsoft.PowerShell, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Data, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/CommandCompletion/CompletionAnalysis.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.523)
- **Top Global Matches:** file_cluster_4: 7.523, file_cluster_6: 8.977, file_cluster_16: 13.674
- **Magnitude:** 2548.78 | **LOC:** 2944 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 0.369; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.7%), Guard Balance (formerly Safety Score) (63.1%)
- **Documentation Coverage:** 85.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetResultHelper` **(Many-Argument Workhorses)** (Impact: 566.4)
  * `GetResultForIdentifier` **(Many-Argument Workhorses)** (Impact: 186.8)
  * `GetResultForEnumPropertyValueOfDSCResource` **(Many-Argument Workhorses)** (Impact: 84.2)
  * `TryGetInferredCompletionsForAssignment` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `CompleteAgainstStatementFlags` **(Many-Argument Workhorses)** (Impact: 43.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 306 instances
* *State Mutation (weighted view):* 1022
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 620`, `structural_boundaries: 295`, `args: 70`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `state_mutation: 410`, `unreferenced_by_name: 3`
* *Architecture:* `api: 30`, `import: 10`
* *Defense:* `safety: 194`, `doc: 56`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.369
  * `Choke Point (Betweenness):` 0.000108 | `Ripple Effect (Closeness):` 0.049068
  * `Imports (Out-Degree: 11):` System, System.Collections, System.Collections.Generic, System.Linq, System.Management.Automation.Language, System.Management.Automation.Subsystem, System.Management.Automation.Subsystem.DSC, System.Reflection...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/LanguagePrimitives.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 7.038)
- **Top Global Matches:** file_cluster_16: 7.038, file_cluster_4: 7.456, file_cluster_15: 8.223
- **Magnitude:** 2525.8 | **LOC:** 5889 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **126** in-repo importer(s); it depends on **24**; blast radius 11.274; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.1%), Debt Markers (formerly Tech Debt) (16.8%)
- **Documentation Coverage:** 60.8563% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FigureLanguageConversion` **(Many-Argument Workhorses)** (Impact: 96.7)
  * `FigureConversion` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `BaseConvertFrom` **(Many-Argument Workhorses)** (Impact: 75.4)
  * `SetObjectProperties` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `IsCustomTypeConversion` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* /// backupTypeTable: /// Used by Remoting Rehydration Logic. While Deserializing a remote object, //...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 171 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 606
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 502`, `structural_boundaries: 497`, `args: 218`, `func_start: 209`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 264`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 4`, `unreferenced_by_name: 14`
* *Architecture:* `api: 144`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 279`, `doc: 660`, `sync_locks: 9`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.274
  * `Choke Point (Betweenness):` 0.012821 | `Ripple Effect (Closeness):` 0.130849
  * `Imports (Out-Degree: 21):` System.Collections, System.Collections.Generic, System.Collections.Specialized, System.ComponentModel, System.Data, System.Diagnostics.CodeAnalysis, System.DirectoryServices, System.Globalization...
  * `Imported By (In-Degree: 126):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/InitialSessionState.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.22)
- **Top Global Matches:** file_cluster_4: 7.22, file_cluster_16: 8.805, file_cluster_15: 9.588
- **Magnitude:** 2407.5 | **LOC:** 5683 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **33** in-repo importer(s); it depends on **20**; blast radius 1.842; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%), Complexity Load (formerly Cognitive Load) (28.0%)
- **Documentation Coverage:** 44.8845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AnalyzePSSnapInAssembly` **(Many-Argument Workhorses)** (Impact: 103.5)
  * `AnalyzeModuleAssemblyWithReflection` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `ProcessModulesToImport` **(Many-Argument Workhorses)** (Impact: 63.5)
  * `Bind_BindCommands` **(Many-Argument Workhorses)** (Impact: 48.7)
  * `LookupCommands` **(Many-Argument Workhorses)** (Impact: 46.3)
    * *Intent:* /// <summary> /// Helper method to search for commands matching the provided commandPattern. /// Sup...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 200 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 787
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 431`, `structural_boundaries: 250`, `args: 190`, `func_start: 174`, `class_start: 18`
* *Risk/State:* `state_mutation: 387`, `dead_code: 5`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `io: 19`, `api: 239`, `concurrency: 16`, `import: 20`
* *Defense:* `safety: 119`, `doc: 709`, `sync_locks: 24`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.842
  * `Choke Point (Betweenness):` 0.008627 | `Ripple Effect (Closeness):` 0.093971
  * `Imports (Out-Degree: 38):` Microsoft.PowerShell.Commands, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Diagnostics.Tracing, System.IO...
  * `Imported By (In-Degree: 33):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/runtime/MutableTuple.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.146)
- **Top Global Matches:** file_cluster_6: 9.146, file_cluster_4: 12.301, file_cluster_8: 16.779
- **Magnitude:** 2385.0 | **LOC:** 2537 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 0.502; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.6%), Guard Balance (formerly Safety Score) (63.4%)
- **Documentation Coverage:** 82.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetValueImpl` **(Compute Cores)** (Impact: 455.4)
  * `SetValueImpl` **(Compute Cores)** (Impact: 230.4)
  * `GetValueImpl` **(Compute Cores)** (Impact: 192.0)
  * `SetValueImpl` **(Compute Cores)** (Impact: 118.0)
  * `GetValueImpl` **(Compute Cores)** (Impact: 98.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 584
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 863`, `structural_boundaries: 458`, `args: 63`, `func_start: 60`, `class_start: 9`
* *Risk/State:* `state_mutation: 442`, `dead_code: 6`, `duplicate_logic: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 181`, `import: 10`
* *Defense:* `safety: 1`, `doc: 37`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.502
  * `Choke Point (Betweenness):` 9.1e-05 | `Ripple Effect (Closeness):` 0.075794
  * `Imports (Out-Degree: 5):` System.CodeDom.Compiler, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Globalization, System.Linq, System.Linq.Expressions, System.Management.Automation.Language...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/parser/TypeInferenceVisitor.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.977)
- **Top Global Matches:** file_cluster_4: 5.977, file_cluster_6: 10.662, file_cluster_16: 11.796
- **Magnitude:** 2363.72 | **LOC:** 3339 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.252; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.6%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InferTypeFrom` **(Many-Argument Workhorses)** (Impact: 156.4)
  * `TryGetTypeFromMember` **(Many-Argument Workhorses)** (Impact: 112.1)
  * `ICustomAstVisitor.VisitBinaryExpression` **(I/O & Config Routines)** (Impact: 90.7)
  * `InferTypesFrom` **(Many-Argument Workhorses)** (Impact: 89.0)
  * `VisitCommand` **(Defensive Guards)** (Impact: 69.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 685
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 420`, `args: 81`, `func_start: 135`, `class_start: 7`
* *Risk/State:* `state_mutation: 259`, `planned_debt: 3`, `unreferenced_by_name: 65`
* *Architecture:* `api: 54`, `import: 12`
* *Defense:* `safety: 159`, `doc: 119`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.252
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.048916
  * `Imports (Out-Degree: 13):` Microsoft.Management.Infrastructure.CimClass, Microsoft.Management.Infrastructure.CimInstance, Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Globalization, System.Linq, System.Management.Automation.Language...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/runtime/Operations/MiscOps.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.591)
- **Top Global Matches:** file_cluster_4: 5.591, file_cluster_16: 9.944, file_cluster_6: 10.889
- **Magnitude:** 2360.1 | **LOC:** 3752 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **19**; blast radius 0.837; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.9%), Debt Markers (formerly Tech Debt) (54.2%)
- **Documentation Coverage:** 80.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddCommand` **(Many-Argument Workhorses)** (Impact: 174.8)
  * `Where` **(Many-Argument Workhorses)** (Impact: 149.8)
    * *Intent:* /// <summary> /// Implements the Where(expression) operation on collections. /// </summary> /// <par...
  * `ForEach` **(Many-Argument Workhorses)** (Impact: 121.0)
    * *Intent:* /// <summary> /// Implements the ForEach() operator. /// </summary> /// <param name="enumerator">The...
  * `Bind` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* // Handle binding file redirection for commands, like: // dir > out
  * `InvokePipeline` **(Many-Argument Workhorses)** (Impact: 41.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 809
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 311`, `args: 100`, `func_start: 99`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 327`, `dead_code: 2`, `fragile_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `io: 4`, `api: 103`, `import: 19`
* *Defense:* `safety: 167`, `doc: 157`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.837
  * `Choke Point (Betweenness):` 0.00195 | `Ripple Effect (Closeness):` 0.088878
  * `Imports (Out-Degree: 25):` Microsoft.PowerShell.Commands, Microsoft.PowerShell.Commands.Internal.Format, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized, System.Globalization, System.IO...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/TypeTable.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.869)
- **Top Global Matches:** file_cluster_4: 5.869, file_cluster_6: 10.424, file_cluster_16: 10.879
- **Magnitude:** 2325.84 | **LOC:** 4780 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **17**; blast radius 2.592; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (33.1%)
- **Documentation Coverage:** 51.2931% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckStandardMembers` **(Many-Argument Workhorses)** (Impact: 101.1)
    * *Intent:* /// Issue appropriate errors and remove members as necessary if: /// - The serialization settings do...
  * `Read_Type` **(I/O & Config Routines)** (Impact: 57.5)
  * `Read_Members` **(Compute Cores)** (Impact: 52.2)
  * `LoadStandardMembersToTypeData` **(Many-Argument Workhorses)** (Impact: 39.3)
    * *Intent:* /// <summary> /// Load the standard members into the passed-in TypeData. /// </summary>
  * `ProcessStandardMembers` **(Many-Argument Workhorses)** (Impact: 28.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 223 instances
* *State Mutation (weighted view):* 846
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 596`, `structural_boundaries: 297`, `args: 155`, `func_start: 143`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 400`, `unreferenced_by_name: 13`
* *Architecture:* `io: 5`, `api: 169`, `import: 17`
* *Defense:* `safety: 77`, `doc: 503`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.592
  * `Choke Point (Betweenness):` 0.005866 | `Ripple Effect (Closeness):` 0.11092
  * `Imports (Out-Degree: 21):` System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Diagnostics, System.Diagnostics.Debug, System.Globalization, System.IO...
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/debugger/debugger.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.643)
- **Top Global Matches:** file_cluster_16: 6.643, file_cluster_0: 8.086, file_cluster_15: 8.344
- **Magnitude:** 2318.96 | **LOC:** 5955 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **18**; blast radius 2.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.5%), Complexity Load (formerly Cognitive Load) (24.7%)
- **Documentation Coverage:** 31.4904% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OnDebuggerStop` **(Many-Argument Workhorses)** (Impact: 33.6)
    * *Intent:* #endregion private members #region private methods /// <summary> /// Raises the DebuggerStop event. ...
  * `ProcessCommand` **(Many-Argument Workhorses)** (Impact: 30.5)
    * *Intent:* /// <summary> /// ProcessCommand. /// </summary> /// <param name="command">PowerShell command.</para...
  * `ResumeExecution` **(Compute Cores)** (Impact: 25.1)
    * *Intent:* /// <summary> /// Resumes execution after a breakpoint/step event has been handled. /// </summary>
  * `OnSequencePointHit` **(Compute Cores)** (Impact: 24.6)
  * `DisplayScript` **(Many-Argument Workhorses)** (Impact: 23.9)
    * *Intent:* /// <summary> /// Executes the list command. /// </summary>
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 199 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 764
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 440`, `structural_boundaries: 346`, `args: 264`, `func_start: 254`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 366`, `planned_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `io: 5`, `api: 255`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 144`, `doc: 1088`, `sync_locks: 36`, `immutability_locks: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.055
  * `Choke Point (Betweenness):` 0.004461 | `Ripple Effect (Closeness):` 0.094251
  * `Imports (Out-Degree: 14):` Microsoft.PowerShell.Commands.Internal.Format, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Globalization...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/cimSupport/cmdletization/xml/CoreCLR/cmdlets-over-objects.xmlSerializer.autogen.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 6.086)
- **Top Global Matches:** file_cluster_16: 6.086, file_cluster_2: 7.077, file_cluster_15: 7.315
- **Magnitude:** 2117.06 | **LOC:** 6689 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.215; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (62.7%), Complexity Load (formerly Cognitive Load) (56.1%)
- **Documentation Coverage:** 99.0566% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ToXmlQualifiedName` **(Stateful Encapsulated Methods)** (Impact: 13.5)
  * `UnknownNode` **(Stateful Encapsulated Methods)** (Impact: 13.4)
  * `CurrentTag` **(Stateful Encapsulated Methods)** (Impact: 10.0)
  * `ShrinkArray` **(Stateful Encapsulated Methods)** (Impact: 9.6)
  * `EnsureArrayIndex` **(Stateful Encapsulated Methods)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 346 instances
* *State Mutation (weighted view):* 1598
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1491`, `structural_boundaries: 304`, `args: 148`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 906`, `dead_code: 4`, `unreferenced_by_name: 38`
* *Architecture:* `api: 47`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.Collections, System.Globalization, System.Xml, System.Xml.Schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/CmdletParameterBinderController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.325)
- **Top Global Matches:** file_cluster_4: 6.325, file_cluster_6: 8.064, file_cluster_16: 13.644
- **Magnitude:** 2016.8 | **LOC:** 4654 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 0.331; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.8%), Complexity Load (formerly Cognitive Load) (23.0%)
- **Documentation Coverage:** 19.5122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetMissingMandatoryParameters` **(Many-Argument Workhorses)** (Impact: 184.4)
    * *Intent:* /// more than one valid parameter sets and the unbound mandatory parameters are not /// consistent a...
  * `GetDefaultParameterValuePairs` **(Compute Cores)** (Impact: 63.4)
    * *Intent:* /// <summary> /// Get all available default parameter value pairs. /// </summary> /// <returns>Retur...
  * `BindParameter` **(Many-Argument Workhorses)** (Impact: 48.0)
    * *Intent:* /// </summary> /// <param name="argument"> /// The argument to be bound. /// </param> /// <param nam...
  * `ValidateParameterSets` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* /// </param> /// <param name="setDefault"> /// If true, the default parameter set will be selected i...
  * `BindParameter` **(Many-Argument Workhorses)** (Impact: 37.3)
    * *Intent:* /// The metadata for the parameter to bind the argument to. /// </param> /// <param name="flags"> //...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 236 instances
* *State Mutation (weighted view):* 791
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 508`, `structural_boundaries: 133`, `args: 70`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 319`, `dead_code: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 82`, `doc: 569`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.331
  * `Choke Point (Betweenness):` 0.000508 | `Ripple Effect (Closeness):` 0.063292
  * `Imports (Out-Degree: 18):` System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.Linq, System.Management.Automation.Host, System.Management.Automation.Internal...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/DscSupport/CimDSCParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.603)
- **Top Global Matches:** file_cluster_4: 5.603, file_cluster_6: 8.703, file_cluster_16: 12.541
- **Magnitude:** 1985.36 | **LOC:** 4077 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 0.366; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.3%), Complexity Load (formerly Cognitive Load) (27.8%)
- **Documentation Coverage:** 18.8312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateKeywordFromCimClass` **(Many-Argument Workhorses)** (Impact: 96.0)
    * *Intent:* /// <summary> /// A method to generate a keyword from a CIM class object. This is used for DSC. /// ...
  * `LoadResourcesFromModule` **(Many-Argument Workhorses)** (Impact: 76.8)
    * *Intent:* /// <summary> /// Load DSC resources from specified module. /// </summary> /// <param name="scriptEx...
  * `ConvertCimInstanceToObject` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* /// <summary> /// Convert Cim Instance representing Resource desired state to Powershell Class Objec...
  * `MapTypeToMofType` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `MapAttributesToMof` **(Many-Argument Workhorses)** (Impact: 54.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 186 instances
* *State Mutation (weighted view):* 638
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 449`, `structural_boundaries: 361`, `args: 110`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `state_mutation: 266`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 58`, `api: 67`, `import: 20`
* *Defense:* `safety: 115`, `doc: 472`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.366
  * `Choke Point (Betweenness):` 0.000626 | `Ripple Effect (Closeness):` 0.076396
  * `Imports (Out-Degree: 15):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Generic, Microsoft.Management.Infrastructure.Serialization, Microsoft.PowerShell.Commands, Microsoft.PowerShell.SecureStringHelper, System, System.Collections, System.Collections.Generic...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 9.27)
- **Top Global Matches:** file_cluster_10: 9.27, file_cluster_9: 10.503, file_cluster_15: 10.679
- **Magnitude:** 1935.1 | **LOC:** 4754 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.5%), Complexity Load (formerly Cognitive Load) (28.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (7.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (3.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExecuteRedirectRequest` **(Many-Argument Workhorses)** (Impact: 34.1)
  * `RunWithNetworkTimeout` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `ExecuteRestMethod` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* # This function calls Invoke-WebRequest with the given uri and # parses the verbose output to determ...
  * `RunCheckingPersistence` **(Many-Argument Workhorses)** (Impact: 18.6)
  * `ExecuteRequestWithCustomUserAgent` **(Many-Argument Workhorses)** (Impact: 11.0)
    * *Intent:* # This function calls either Invoke-WebRequest or Invoke-RestMethod with the given uri # using the c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 244 instances
* *State Mutation (weighted view):* 1687
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 38`, `args: 65`, `func_start: 14`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 1199`
* *Architecture:* `io: 724`
* *Defense:* `safety: 42`, `test: 1046`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.215
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/WebCmdletElementCollection.cs` (CSHARP) | Magnitude: 20.66 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, doc: 18, structural_boundaries: 11, args: 5
- `test/powershell/Language/Parser/Conversions.Tests.ps1` (POWERSHELL) | Magnitude: 360.62 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 491, closures: 193, explicit_casts: 163, test: 160
- `src/System.Management.Automation/engine/remoting/commands/runspacerepository.cs` (CSHARP) | Magnitude: 11.68 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 29, doc: 19, structural_boundaries: 7, api: 4
- `src/System.Management.Automation/engine/interpreter/Interpreter.cs` (CSHARP) | Magnitude: 38.98 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 53, doc: 18, api: 16, encapsulation: 15
- `src/System.Management.Automation/engine/PseudoParameters.cs` (CSHARP) | Magnitude: 66.34 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 112, doc: 95, core_var_decl: 16, api: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/tools/WebListener/Controllers/ResponseHeadersController.cs` (CSHARP) | Magnitude: 0.03 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 30, structural_boundaries: 20, import: 12, branch: 5
- `test/powershell/Modules/Microsoft.PowerShell.Utility/object.tests.ps1` (POWERSHELL) | Magnitude: 58.6 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, test: 28, closures: 22, state_mutation: 20
- `test/powershell/Modules/Microsoft.PowerShell.Core/ImportProvider.Tests.ps1` (POWERSHELL) | Magnitude: 20.3 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 13, state_mutation: 5, test: 4, reflection_metaprogramming: 2
- `test/powershell/Language/Scripting/OutErrorVariable.Tests.ps1` (POWERSHELL) | Magnitude: 71.54 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 301, test: 66, closures: 41, core_var_decl: 31
- `test/powershell/engine/Basic/NativeCommandErrorHandling.Tests.ps1` (POWERSHELL) | Magnitude: 111.98 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 147, test: 58, state_mutation: 40, closures: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/System.Management.Automation/engine/interpreter/TypeOperations.cs` (CSHARP) | Magnitude: 121.56 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 138, api: 35, structural_boundaries: 32, state_mutation: 23
- `tools/AttackSurfaceAnalyzer/docker/Dockerfile` (DOCKERFILE) | Magnitude: 0.03 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 64, branch: 15, func_start: 12, structural_boundaries: 6
- `src/System.Management.Automation/engine/remoting/common/PSSessionConfigurationTypeOption.cs` (CSHARP) | Magnitude: 23.94 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 44, indent_spaces: 42, encapsulation: 12, api: 11
- `test/tools/WebListener/Controllers/MultipartController.cs` (CSHARP) | Magnitude: 0.04 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 68, structural_boundaries: 23, import: 12, core_var_decl: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/powershell/Modules/Microsoft.PowerShell.Utility/Write-Error.Tests.ps1` (POWERSHELL) | Magnitude: 35.02 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 98, test: 73, closures: 13, safety: 10
- `test/powershell/Modules/Microsoft.PowerShell.Utility/Tee-Object.Tests.ps1` (POWERSHELL) | Magnitude: 44.6 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 76, test: 32, state_mutation: 20, closures: 19
- `src/Modules/Windows/PSDiagnostics/PSDiagnostics.psm1` (POWERSHELL) | Magnitude: 238.66 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 207, globals: 57, state_mutation: 50, branch: 49
- `test/powershell/engine/Help/HelpSystem.OnlineHelp.Tests.ps1` (POWERSHELL) | Magnitude: 44.98 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 42, test: 14, state_mutation: 11, branch: 10
- `test/powershell/Modules/PowerShellGet/PowerShellGet.Tests.ps1` (POWERSHELL) | Magnitude: 126.42 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 175, closures: 49, test: 48, state_mutation: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/Microsoft.Management.UI.Internal/ManagementList/Common/PropertyChangedEventArgs.cs` (CSHARP) | Magnitude: 8.46 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 20, doc: 15, api: 4, structural_boundaries: 3
- `src/Microsoft.PowerShell.Security/singleshell/installer/MshSecurityMshSnapin.cs` (CSHARP) | Magnitude: 9.32 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 43, doc: 22, structural_boundaries: 17, import: 10
- `src/Microsoft.Management.UI.Internal/ManagementList/Common/ExtendedFrameworkElementAutomationPeer.cs` (CSHARP) | Magnitude: 16.4 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 38, doc: 36, structural_boundaries: 9, args: 6
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/Remove-PSBreakpoint.cs` (CSHARP) | Magnitude: 3.9 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 11, doc: 6, structural_boundaries: 3, macros: 2
- `src/System.Management.Automation/namespaces/ProviderDeclarationAttribute.cs` (CSHARP) | Magnitude: 14.14 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: doc: 100, indent_spaces: 39, core_var_decl: 12, design_pascal_case: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tools/installpsh-redhat.sh` (SHELL) | Magnitude: 0.14 | Delta: **0.16** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 93, indent_spaces: 70, core_var_decl: 34, branch: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/System.Management.Automation/engine/OrderedHashtable.cs` (CSHARP) | Magnitude: 57.76 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 120, doc: 81, structural_boundaries: 20, api: 19
- `src/System.Management.Automation/utils/tracing/EtwActivity.cs` (CSHARP) | Magnitude: 131.08 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 230, doc: 155, api: 32, structural_boundaries: 30
- `src/Microsoft.Management.UI.Internal/ManagementList/Common/IsNotNullConverter.cs` (CSHARP) | Magnitude: 8.18 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 20, indent_spaces: 14, structural_boundaries: 5, api: 3
- `src/System.Management.Automation/engine/CommandCompletion/CommandCompletion.cs` (CSHARP) | Magnitude: 247.12 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 369, doc: 76, structural_boundaries: 62, branch: 61
- `src/Microsoft.Management.Infrastructure.CimCmdlets/CimWriteProgress.cs` (CSHARP) | Magnitude: 42.8 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 53, doc: 47, state_mutation: 11, structural_boundaries: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/Microsoft.PowerShell.Commands.Management/commands/management/RenamePropertyCommand.cs` (CSHARP) | Magnitude: 19.68 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 90, doc: 33, structural_boundaries: 7, state_mutation: 7
- `src/System.Management.Automation/engine/MshSecurityException.cs` (CSHARP) | Magnitude: 27.14 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 63, doc: 32, state_mutation: 10, core_var_decl: 7
- `src/Microsoft.PowerShell.Commands.Management/commands/management/Service.cs` (CSHARP) | Magnitude: 845.7 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 2060, doc: 458, core_var_decl: 322, branch: 203
- `src/System.Management.Automation/engine/PSClassSearcher.cs` (CSHARP) | Magnitude: 138.66 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 228, core_var_decl: 46, doc: 39, structural_boundaries: 37
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/NewTemporaryFileCommand.cs` (CSHARP) | Magnitude: 10.16 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 33, doc: 6, core_var_decl: 6, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/System.Management.Automation/utils/CommandProcessorExceptions.cs` (CSHARP) | Magnitude: 18.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 44, doc: 41, args: 6, func_start: 6
- `.github/workflows/scorecards.yml` (YAML) | Magnitude: 15.78 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 35, args: 8, import: 4, immutability_locks: 4
- `src/System.Management.Automation/utils/MshObjectDisposedException.cs` (CSHARP) | Magnitude: 16.26 | Delta: **0.077** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 49, indent_spaces: 39, api: 5, structural_boundaries: 4
- `.github/workflows/dependency-review.yml` (YAML) | Magnitude: 15.24 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 8, structural_boundaries: 2, import: 2, immutability_locks: 2
- `src/System.Management.Automation/engine/hostifaces/ChoiceDescription.cs` (CSHARP) | Magnitude: 21.96 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 59, doc: 49, branch: 5, structural_boundaries: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/System.Management.Automation/engine/TypeTable_GetEvent_Types_Ps1Xml.cs` (CSHARP) | Magnitude: 35.28 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 145, state_mutation: 21, core_var_decl: 21, design_camel_case: 21
- `src/Microsoft.WSMan.Management/WsManSnapin.cs` (CSHARP) | Magnitude: 9.32 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 45, doc: 25, structural_boundaries: 15, import: 8
- `src/Microsoft.Management.UI.Internal/ShowCommand/Controls/ImageButton/ImageButtonBase.cs` (CSHARP) | Magnitude: 22.68 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 25, doc: 21, structural_boundaries: 11, api: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/System.Management.Automation/engine/hostifaces/LocalConnection.cs` (CSHARP) | Magnitude: 466.66 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 964, doc: 266, branch: 120, core_var_decl: 99
- `src/System.Management.Automation/help/HelpFileHelpProvider.cs` (CSHARP) | Magnitude: 190.12 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 267, branch: 48, core_var_decl: 48, doc: 38
- `src/System.Management.Automation/engine/interpreter/CallInstruction.Generated.cs` (CSHARP) | Magnitude: 1224.4 | Delta: **0.085** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 717, branch: 319, structural_boundaries: 233, generics: 199
- `src/System.Management.Automation/engine/remoting/commands/SuspendJob.cs` (CSHARP) | Magnitude: 170.28 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 281, branch: 51, core_var_decl: 40, state_mutation: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `test/hosting/test_HostingBasic.cs` (CSHARP) | Magnitude: 55.38 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 164, structural_boundaries: 41, core_var_decl: 33, design_snake_case: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/System.Management.Automation/engine/COM/ComUtil.cs` (CSHARP) | Magnitude: 184.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 222, branch: 49, core_var_decl: 45, doc: 44
- `src/System.Management.Automation/FormatAndOutput/common/ComplexWriter.cs` (CSHARP) | Magnitude: 521.56 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 592, core_var_decl: 116, branch: 113, state_mutation: 90

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/powershell/Provider/AutomountSubstDriveCore.ps1` (POWERSHELL) | Magnitude: 30.48 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 17, branch: 6, closures: 6, state_mutation: 5
- `.github/skills/analyze-pester-failures/scripts/analyze-pr-test-failures.ps1` (POWERSHELL) | Magnitude: 180.0 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 185, branch: 94, state_mutation: 60, closures: 55
- `test/infrastructure/ciModule.Tests.ps1` (POWERSHELL) | Magnitude: 67.52 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 172, test: 90, globals: 80, state_mutation: 37
- `test/powershell/Modules/Microsoft.PowerShell.Core/Import-Module.Tests.ps1` (POWERSHELL) | Magnitude: 180.48 | Delta: **0.09** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 308, test: 104, state_mutation: 61, closures: 59
- `test/powershell/Modules/Microsoft.PowerShell.Utility/Import-Alias.Tests.ps1` (POWERSHELL) | Magnitude: 46.8 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 86, test: 34, state_mutation: 26, panics_and_aborts: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/ResGen/Program.cs` (CSHARP) | Magnitude: 58.84 | Delta: **0.022** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 117, core_var_decl: 33, design_camel_case: 22, structural_boundaries: 21
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/WebCmdlet/CoreCLR/InvokeWebRequestCommand.CoreClr.cs` (CSHARP) | Magnitude: 24.56 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 39, doc: 11, core_var_decl: 8, structural_boundaries: 7
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHostUserInterfaceSecurity.cs` (CSHARP) | Magnitude: 61.32 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 75, doc: 25, core_var_decl: 11, branch: 10
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/TestJsonCommand.cs` (CSHARP) | Magnitude: 89.32 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 228, core_var_decl: 45, doc: 39, branch: 23
- `src/Microsoft.PowerShell.Commands.Utility/commands/utility/WriteConsoleCmdlet.cs` (CSHARP) | Magnitude: 43.12 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 79, doc: 16, branch: 12, structural_boundaries: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/packaging/packaging.psm1` -> Churn: **84.39%** | Cog Load: 57.6994% | Debt: 13.6956%
- `build.psm1` -> Churn: **60.85%** | Cog Load: 89.1243% | Debt: 8.0714%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` -> **Yoshifumi** (100.0% isolated ownership) | Magnitude: 7040.34
- `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` -> **Jordan Borean** (100.0% isolated ownership) | Magnitude: 4438.7
- `src/System.Management.Automation/engine/CommandCompletion/CompletionAnalysis.cs` -> **Yoshifumi** (100.0% isolated ownership) | Magnitude: 2548.78
- `src/System.Management.Automation/engine/runtime/Operations/MiscOps.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 2360.1
- `test/powershell/Modules/Microsoft.PowerShell.Utility/WebCmdlets.Tests.ps1` -> **yotsuda** (100.0% isolated ownership) | Magnitude: 1935.1

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/System.Management.Automation/engine/MshObject.cs` -> **Severity: 1.261** (Bridge: 0.0128 * Flux: 98.5321%)
- `src/System.Management.Automation/engine/LanguagePrimitives.cs` -> **Severity: 1.219** (Bridge: 0.0128 * Flux: 95.0904%)
- `src/System.Management.Automation/engine/InitialSessionState.cs` -> **Severity: 0.859** (Bridge: 0.0086 * Flux: 99.5308%)
- `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` -> **Severity: 0.783** (Bridge: 0.0078 * Flux: 99.8341%)
- `src/System.Management.Automation/engine/ErrorPackage.cs` -> **Severity: 0.623** (Bridge: 0.0063 * Flux: 98.4167%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/StringUtil.cs` -> **Severity: 9.758** (Embedded: 0.1827 * Error Risk: 53.4232%)
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 9.138** (Embedded: 0.1407 * Error Risk: 64.9292%)
- `src/System.Management.Automation/utils/assert.cs` -> **Severity: 8.488** (Embedded: 0.1743 * Error Risk: 48.71%)
- `tools/Xml/Xml.psm1` -> **Severity: 7.754** (Embedded: 0.1322 * Error Risk: 58.65%)
- `src/System.Management.Automation/utils/MshTraceSource.cs` -> **Severity: 7.719** (Embedded: 0.184 * Error Risk: 41.9611%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/Xml/Xml.psm1` -> **Severity: 2882.8** (Blast Radius: 28.828 * Doc Risk: 100.0%)
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Native.cs` -> **Severity: 2874.6** (Blast Radius: 28.746 * Doc Risk: 100.0%)
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/StringUtil.cs` -> **Severity: 2674.4** (Blast Radius: 33.43 * Doc Risk: 80.0%)
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 2412.012** (Blast Radius: 25.843 * Doc Risk: 93.3333%)
- `src/System.Management.Automation/utils/assert.cs` -> **Severity: 1168.399** (Blast Radius: 26.289 * Doc Risk: 44.4444%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 7379 literal sites + 38 sites through wrappers = 7417

- `ThrowError` (function, panics_and_aborts, primitive): 8 call sites in 1 files -- `src/System.Management.Automation/engine/runtime/ScriptBlockToPowerShell.cs`
- `ThrowWin32Error` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `src/Microsoft.PowerShell.Commands.Management/commands/management/TimeZoneCommands.cs`
- `ThrowCommandNotFoundException` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `src/System.Management.Automation/engine/ExternalScriptInfo.cs`
- `ThrowInvalidCastException` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `src/System.Management.Automation/engine/LanguagePrimitives.cs`
- `GetExceptionWhenAuthenticationRequiresCredential` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `src/System.Management.Automation/engine/Modules/RemoteDiscoveryHelper.cs`
- `ThrowTypeOrFormatErrors` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `src/System.Management.Automation/engine/InitialSessionState.cs`
- `ThrowPSInvalidBooleanArgumentCastException` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/System.Management.Automation/engine/ArgumentTypeConverterAttribute.cs`
- `ThrowPathMustBeValidContainersException` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/System.Management.Automation/help/UpdateHelpCommand.cs`
- `CompileListInitExpression` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/System.Management.Automation/engine/interpreter/LightCompiler.cs`
- `CompileMemberInitExpression` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/System.Management.Automation/engine/interpreter/LightCompiler.cs`
- `CompileQuoteUnaryExpression` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/System.Management.Automation/engine/interpreter/LightCompiler.cs`
- `CompileReducibleExpression` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/System.Management.Automation/engine/interpreter/LightCompiler.cs`
*(+3 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 67178 call pairs -- scoped 41.9%, unique 2.6%, ambiguous 31.8%, external 23.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| csharp | 65231 | 42.7% | 2.5% | 32.8% | 22.1% |
| powershell | 1757 | 15.8% | 6.8% | 1.3% | 76.1% |
| shell | 190 | 11.1% | 0.0% | 0.5% | 88.4% |

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
