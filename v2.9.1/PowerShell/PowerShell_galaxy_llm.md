# ARCHITECTURAL_BRIEF: PowerShell
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/PowerShell/PowerShell` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 1490 analyzed artifact(s), 510376 LOC.
- **Load-bearing artifact:** `tools/Xml/Xml.psm1` -- 68 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleHost.cs` -- pulls in 29 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` at magnitude 7068.64 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 1490 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1184 |
| Total LOC | 510376 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 55.7% |
| Dominant Lang | CSHARP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7427 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3414 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.3152 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CSHARP | 1279 | 486348 | 85.8% |
| POWERSHELL | 78 | 15952 | 5.2% |
| XML | 55 | 0 | 3.7% |
| MARKDOWN | 34 | 0 | 2.3% |
| JSON | 23 | 6665 | 1.5% |
| SHELL | 13 | 1304 | 0.9% |
| PLAINTEXT | 4 | 0 | 0.3% |
| YAML | 2 | 19 | 0.1% |
| BATCH | 1 | 1 | 0.1% |
| DOCKERFILE | 1 | 87 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Flat Modular Platform`
> **Architectural Drift Z-Score:** `2.889`
> **Composition Archetype:** `Flat Modular Platform` (z +2.89; from the repo's file-archetype mix)
> **File Composition:** Encapsulated Accessors Files 35%, Large Core Modules (3) 12%, State Mutators Files 12%, Data / Markup / Trivial 9%, Declarative / Non-Code 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1452 | 97.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 2.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1184*

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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 15.2 | 10.6 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 46.8 | 52.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.9 | 21.4 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 26.1 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 59.5 | 4.2 | 4.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 61.2 | 89.2 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 96.4 | 3.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.6 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 30.3 | 12.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 19.6 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 8337 | 665 | 13 | `src/Microsoft.PowerShell.CoreCLR.Eventing/DotNetCode/Eventing/Reader/NativeWrapper.cs` |
| cleanup | 1194 | 251 | 2 | `tools/packaging/packaging.psm1` |
| guards | 55314 | 1269 | 91 | `src/System.Management.Automation/engine/parser/Compiler.cs` |
| danger | 5815 | 607 | 10 | `tools/packaging/packaging.psm1` |
| concurrency | 1734 | 247 | 2 | `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` |
| connectivity | 29798 | 1294 | 49 | `src/Microsoft.PowerShell.Commands.Management/commands/management/GetComputerInfoCommand.cs` |
| io | 1670 | 218 | 2 | `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` |
| crypto | 0 | 0 | 0 | - |
| ipc | 113 | 39 | 0 | `tools/install-powershell.ps1` |
| time | 262 | 93 | 0 | `src/System.Management.Automation/engine/serialization.cs` |
| serialization | 63 | 18 | 0 | `tools/UpdateDotnetRuntime.ps1` |
| regex | 310 | 64 | 0 | `tools/packaging/packaging.psm1` |
| events | 4535 | 397 | 8 | `tools/packaging/packaging.psm1` |
| tests | 165 | 40 | 0 | `test/tools/Modules/HelpersLanguage/HelpersLanguage.psm1` |
| docs | 138334 | 1117 | 245 | `src/System.Management.Automation/engine/parser/ast.cs` |
| debt | 1184 | 263 | 2 | `tools/AttackSurfaceAnalyzer/Summarize-AsaResults.ps1` |
| mutation | 114647 | 1278 | 177 | `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` |
| dead_code | 6705 | 1105 | 11 | `src/System.Management.Automation/engine/parser/Compiler.cs` |
| credential | 28 | 10 | 0 | `tools/packaging/packaging.psm1` |
| threat | 2027 | 289 | 1 | `src/System.Management.Automation/engine/parser/Compiler.cs` |
| ml_ai | 144 | 62 | 0 | `src/Microsoft.PowerShell.ConsoleHost/host/msh/ConsoleControl.cs` |
| ui | 222 | 56 | 0 | `src/Microsoft.Management.UI.Internal/ManagementList/ManagementList/ManagementList.Generated.cs` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **5.75**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` (Hits: 76)
- `src/System.Management.Automation/help/UpdatableHelpSystem.cs` (Hits: 61)
- `src/System.Management.Automation/DscSupport/CimDSCParser.cs` (Hits: 58)

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

- `LoadModuleManifest` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs`) -> Impact: **886.4** | LOC: 1238
  * *Intent:* /// Routine to process the module manifest data language script. /// </summary> /// <param name="moduleManifestPath">The path to the manifest file.</p...
- `GetResultHelper` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionAnalysis.cs`) -> Impact: **566.4** | LOC: 808
- `SetValueImpl` **(Compute Cores)** (@ `src/System.Management.Automation/engine/runtime/MutableTuple.cs`) -> Impact: **455.4** | LOC: 135
- `ToString` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/MshObject.cs`) -> Impact: **429.0** | LOC: 1170
  * *Intent:* /// If the BaseObject is not null we try enumerating. If that fails we try the BaseObject's ToString. /// </param> /// <param name="separator">The sep...
- `NativeCommandArgumentCompletion` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs`) -> Impact: **417.0** | LOC: 403
- `GetMessage` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/CoreCLR/EventResource.cs`) -> Impact: **361.5** | LOC: 579
  * *Intent:* /// <summary> /// Gets the message resource id for the specified event id. /// </summary> /// <param name="eventId">The event id for the message resou...
- `ScanVariable` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/parser/tokenizer.cs`) -> Impact: **244.1** | LOC: 309
  * *Intent:* #endregion Strings #region Variables // Scan a variable - the first character ($ or @) has been consumed already.
- `TryGetNumberValue` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/parser/tokenizer.cs`) -> Impact: **241.3** | LOC: 328
- `LoadModule` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs`) -> Impact: **236.9** | LOC: 493
  * *Intent:* /// <summary> /// Load a module from a file... /// </summary> /// <param name="parentModule">The parent module, if any.</param> /// <param name="fileN...
- `LoadBinaryModule` **(Many-Argument Workhorses)** (@ `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs`) -> Impact: **230.9** | LOC: 292
  * *Intent:* /// <param name="assemblyToLoad">The assembly to load so no lookup need be done.</param> /// <param name="moduleBase">The module base to use for this ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/System.Management.Automation/engine` | 146 | 50041.44 | 14.34% | 34.26% |
| `src/System.Management.Automation/engine/parser` | 18 | 25680.32 | 29.58% | 41.82% |
| `src/System.Management.Automation/namespaces` | 33 | 11744.81 | 9.22% | 35.48% |
| `src/System.Management.Automation/engine/CommandCompletion` | 8 | 11332.54 | 24.9% | 21.69% |
| `src/Microsoft.PowerShell.Commands.Utility/commands/utility` | 89 | 10760.22 | 12.64% | 28.95% |
| `src/Microsoft.PowerShell.Commands.Management/commands/management` | 52 | 10311.96 | 12.61% | 31.6% |
| `src/System.Management.Automation/engine/Modules` | 16 | 10141.94 | 22.57% | 31.18% |
| `src/System.Management.Automation/engine/hostifaces` | 33 | 10040.02 | 16.36% | 43.25% |
| `src/System.Management.Automation/engine/remoting/commands` | 28 | 9274.1 | 16.92% | 24.18% |
| `src/System.Management.Automation/engine/interpreter` | 38 | 8400.62 | 40.32% | 54.34% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/System.Management.Automation/CoreCLR/CorePsStub.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/ComInterop/Errors.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/parser/PreOrderVisitor.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/remoting/client/remotingprotocol.cs` -> **100.0%** Exposure
- `src/System.Management.Automation/engine/remoting/common/PSSessionConfigurationTypeOption.cs` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `.github/skills/analyze-pester-failures/scripts/analyze-pr-test-failures.ps1` -> **100.0%** Exposure
- `dsc/pwsh.profile.resource.ps1` -> **100.0%** Exposure
- `src/Modules/Windows/Microsoft.PowerShell.Security/Security.types.ps1xml` -> **100.0%** Exposure
- `src/PowerShell.Core.Instrumentation/RegisterManifest.ps1` -> **100.0%** Exposure
- `tools/AttackSurfaceAnalyzer/Summarize-AsaResults.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/System.Management.Automation/utils/tracing/TracingGen.cs` -> **82** Orphaned Functions | **0** Duplicates
- `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` -> **71** Orphaned Functions | **4** Duplicates
- `src/System.Management.Automation/engine/parser/TypeInferenceVisitor.cs` -> **65** Orphaned Functions | **0** Duplicates
- `src/System.Management.Automation/engine/parser/PreOrderVisitor.cs` -> **64** Orphaned Functions | **0** Duplicates
- `src/System.Management.Automation/engine/interpreter/InstructionList.cs` -> **63** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/System.Management.Automation/security/SecuritySupport.cs` -> **19.5611%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `6867` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/System.Management.Automation/engine/CommandCompletion/CompletionCompleters.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 7068.64 | **LOC:** 9263 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 60.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.2%), Complexity Load (formerly Cognitive Load) (52.9%)
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
* *Amplified Cascading Flux:* 683 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 2213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1812`, `structural_boundaries: 1116`, `args: 287`, `func_start: 233`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 847`, `dead_code: 4`, `duplicate_logic: 4`, `unreferenced_by_name: 71`
* *Architecture:* `io: 8`, `api: 158`, `concurrency: 2`, `import: 25`
* *Defense:* `safety: 390`, `doc: 273`, `sync_locks: 2`, `immutability_locks: 29`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Options, Microsoft.PowerShell, Microsoft.PowerShell.Cim, Microsoft.PowerShell.Commands, Microsoft.PowerShell.Commands.Internal.Format, System.Buffers, System.Collections...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4927.12 | **LOC:** 7495 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%), Complexity Load (formerly Cognitive Load) (38.7%)
- **Documentation Coverage:** 44.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `LoadModuleManifest` **(Many-Argument Workhorses)** (Impact: 886.4)
    * *Intent:* /// Routine to process the module manifest data language script. /// </summary> /// <param name="mod...
  * `LoadModule` **(Many-Argument Workhorses)** (Impact: 236.9)
    * *Intent:* /// <summary> /// Load a module from a file... /// </summary> /// <param name="parentModule">The par...
  * `LoadBinaryModule` **(Many-Argument Workhorses)** (Impact: 230.9)
    * *Intent:* /// <param name="assemblyToLoad">The assembly to load so no lookup need be done.</param> /// <param ...
  * `LoadModuleNamedInManifest` **(Many-Argument Workhorses)** (Impact: 141.0)
  * `ImportModuleMembers` **(Many-Argument Workhorses)** (Impact: 128.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 493 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 1646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1115`, `structural_boundaries: 343`, `args: 99`, `func_start: 89`, `class_start: 5`
* *Risk/State:* `state_mutation: 660`, `dead_code: 15`, `planned_debt: 2`, `fragile_debt: 7`, `unreferenced_by_name: 5`
* *Architecture:* `io: 76`, `api: 85`, `concurrency: 2`, `import: 21`
* *Defense:* `safety: 171`, `doc: 527`, `sync_locks: 10`, `immutability_locks: 13`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.Cmdletization, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/ast.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 4636.78 | **LOC:** 10846 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.8%), Complexity Load (formerly Cognitive Load) (27.1%)
- **Documentation Coverage:** 47.0167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `IsImportCommand` **(Many-Argument Workhorses)** (Impact: 42.6)
    * *Intent:* #endregion #region static fields/methods /// <summary> /// </summary> /// <param name="stmt"></param...
  * `ToStringForSerialization` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `GenerateCommandCallPipelineAst` **(I/O & Config Routines)** (Impact: 35.5)
  * `ScriptBlockAst` **(Many-Argument Workhorses)** (Impact: 31.5)
    * *Intent:* /// This construction uses explicitly named begin/process/end/clean blocks. /// </summary> /// <para...
  * `InternalVisit` **(Compute Cores)** (Impact: 30.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 440 instances
* *Concurrency (weighted view):* 44
* *State Mutation (weighted view):* 1451
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1029`, `structural_boundaries: 1023`, `args: 442`, `func_start: 464`, `class_start: 98`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 571`, `dead_code: 8`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 12`, `unreferenced_by_name: 20`
* *Architecture:* `api: 761`, `concurrency: 9`, `import: 17`
* *Defense:* `safety: 309`, `doc: 2823`, `sync_locks: 6`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell, Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/Parser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 4543.76 | **LOC:** 8280 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 0.803; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Complexity Load (formerly Cognitive Load) (62.8%)
- **Documentation Coverage:** 89.4231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SwitchStatementRule` **(Many-Argument Workhorses)** (Impact: 130.0)
  * `ConfigurationStatementRule` **(Many-Argument Workhorses)** (Impact: 120.2)
  * `GetCommandArgument` **(Many-Argument Workhorses)** (Impact: 102.7)
  * `ClassMemberRule` **(Many-Argument Workhorses)** (Impact: 99.6)
  * `DynamicKeywordStatementRule` **(Many-Argument Workhorses)** (Impact: 92.8)
    * *Intent:* /// <summary> /// Parse a dynamic keyword statement which will be either of the form /// keyword [pa...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 553 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 1806
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1197`, `structural_boundaries: 498`, `args: 205`, `func_start: 157`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 700`, `dead_code: 9`, `planned_debt: 6`, `unreferenced_by_name: 16`
* *Architecture:* `io: 7`, `api: 67`, `concurrency: 4`, `import: 18`
* *Defense:* `safety: 423`, `doc: 130`, `immutability_locks: 8`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.803
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000671
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.DesiredStateConfiguration.Internal, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.Tracing, System.Globalization, System.IO, System.Linq...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 4521.9 | **LOC:** 7952 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%), Complexity Load (formerly Cognitive Load) (35.9%)
- **Documentation Coverage:** 92.9705% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `InvokeMethod` **(Many-Argument Workhorses)** (Impact: 130.7)
  * `GetPSMemberInfo` **(Many-Argument Workhorses)** (Impact: 106.9)
  * `FallbackSetMember` **(Many-Argument Workhorses)** (Impact: 105.2)
  * `BinaryNumericOp` **(Many-Argument Workhorses)** (Impact: 85.8)
  * `FallbackInvokeMember` **(Many-Argument Workhorses)** (Impact: 84.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 406 instances
* *Concurrency (weighted view):* 48
* *State Mutation (weighted view):* 1366
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1008`, `structural_boundaries: 1103`, `args: 350`, `func_start: 268`, `class_start: 37`
* *Risk/State:* `state_mutation: 554`, `dead_code: 37`, `planned_debt: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 203`, `concurrency: 8`, `import: 25`
* *Defense:* `safety: 243`, `doc: 113`, `sync_locks: 37`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Buffers, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.Specialized, System.Data, System.Dynamic, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/namespaces/FileSystemProvider.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3905.16 | **LOC:** 9539 | **CtrlFlow:** 16.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **22**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.6%), Complexity Load (formerly Cognitive Load) (14.8%)
- **Documentation Coverage:** 43.8053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `NewItem` **(Many-Argument Workhorses)** (Impact: 164.3)
    * *Intent:* /// Specify "directory" or "container" to create a directory. /// </param> /// <param name="value"> ...
  * `Dir` **(Many-Argument Workhorses)** (Impact: 148.9)
  * `PerformCopyFileFromRemoteSession` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `CopyFileStreamToRemoteSession` **(Stateful Encapsulated Methods)** (Impact: 59.2)
  * `NormalizeRelativePath` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* /// </summary> /// <param name="path"> /// A fully qualifiedpath to an item. The item must exist, //...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 380 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1176`, `structural_boundaries: 412`, `args: 161`, `func_start: 156`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 1`, `state_mutation: 508`, `dead_code: 18`, `unreferenced_by_name: 31`
* *Architecture:* `io: 58`, `api: 143`, `concurrency: 2`, `import: 23`
* *Defense:* `safety: 498`, `doc: 1040`, `immutability_locks: 59`, `cleanup: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.Win32.SafeHandles, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/Compiler.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 3694.58 | **LOC:** 7080 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **18**; blast radius 1.281; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (51.7%)
- **Documentation Coverage:** 96.7359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VisitBinaryExpression` **(Compute Cores)** (Impact: 106.5)
  * `NewParameterAttribute` **(Compute Cores)** (Impact: 43.8)
  * `CompileStatementListWithTraps` **(Many-Argument Workhorses)** (Impact: 42.5)
  * `GetRedirectedExpression` **(Many-Argument Workhorses)** (Impact: 41.8)
    * *Intent:* // A redirected expression requires extra work because there is no CommandProcessor or PipelineProce...
  * `VisitPipeline` **(Defensive Guards)** (Impact: 40.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 395 instances
* *State Mutation (weighted view):* 1430
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 690`, `structural_boundaries: 831`, `args: 293`, `func_start: 209`, `class_start: 16`
* *Risk/State:* `state_mutation: 640`, `dead_code: 35`, `planned_debt: 17`, `unreferenced_by_name: 61`
* *Architecture:* `io: 4`, `api: 415`, `import: 19`
* *Defense:* `safety: 332`, `doc: 53`, `sync_locks: 2`, `immutability_locks: 266`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.281
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001341
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized, System.Diagnostics, System.Dynamic, System.Globalization...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Microsoft.WSMan.Management/ConfigProvider.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3514.16 | **LOC:** 6578 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (22.5%)
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
* *Amplified Cascading Flux:* 352 instances
* *State Mutation (weighted view):* 1248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 899`, `structural_boundaries: 306`, `args: 91`, `func_start: 90`, `class_start: 15`
* *Risk/State:* `state_mutation: 544`, `dead_code: 17`, `planned_debt: 4`, `unreferenced_by_name: 11`
* *Architecture:* `io: 6`, `api: 108`, `import: 16`
* *Defense:* `safety: 83`, `doc: 723`, `sync_locks: 10`, `immutability_locks: 58`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.IO, System.Management.Automation...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/tokenizer.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 3356.44 | **LOC:** 5084 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.563; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.3%), Complexity Load (formerly Cognitive Load) (42.1%)
- **Documentation Coverage:** 85.1613% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ScanVariable` **(Many-Argument Workhorses)** (Impact: 244.1)
    * *Intent:* #endregion Strings #region Variables // Scan a variable - the first character ($ or @) has been cons...
  * `TryGetNumberValue` **(Many-Argument Workhorses)** (Impact: 241.3)
  * `ScanNumberHelper` **(Many-Argument Workhorses)** (Impact: 224.7)
    * *Intent:* /// <summary> /// Scans a numeric string to determine its characteristics. /// </summary> /// <param...
  * `NextToken` **(I/O & Config Routines)** (Impact: 181.5)
  * `HandleRequiresParameter` **(Many-Argument Workhorses)** (Impact: 169.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 338 instances
* *State Mutation (weighted view):* 1076
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1072`, `structural_boundaries: 376`, `args: 129`, `func_start: 122`, `class_start: 11`
* *Risk/State:* `state_mutation: 400`, `dead_code: 6`, `planned_debt: 1`, `unreferenced_by_name: 23`
* *Architecture:* `api: 88`, `concurrency: 1`, `import: 13`
* *Defense:* `safety: 97`, `doc: 235`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.PowerShell.Commands, Microsoft.PowerShell.DesiredStateConfiguration.Internal, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Globalization, System.Linq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/serialization.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 3018.46 | **LOC:** 7680 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.3%), Complexity Load (formerly Cognitive Load) (20.1%)
- **Documentation Coverage:** 44.6985% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HandleKnownContainerTypes` **(Many-Argument Workhorses)** (Impact: 55.6)
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
* *Structure:* `branch: 572`, `structural_boundaries: 403`, `args: 326`, `func_start: 296`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 546`, `dead_code: 11`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 4`, `unreferenced_by_name: 11`
* *Architecture:* `api: 248`, `import: 26`
* *Defense:* `safety: 220`, `doc: 1125`, `immutability_locks: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Serialization, Microsoft.PowerShell.Commands, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/CoreAdapter.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2982.78 | **LOC:** 6260 | **CtrlFlow:** 16.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **21**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (58.7%), Complexity Load (formerly Cognitive Load) (32.7%)
- **Documentation Coverage:** 62.7907% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FindBestMethodImpl` **(Many-Argument Workhorses)** (Impact: 183.2)
  * `CompareOverloadCandidates` **(Many-Argument Workhorses)** (Impact: 81.0)
    * *Intent:* /// <summary> /// Compare the 2 methods, determining which method is better. /// </summary> /// <ret...
  * `GetMethodInvoker` **(Many-Argument Workhorses)** (Impact: 69.3)
  * `DoBoxingIfNecessary` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `PopulatePropertyReflectionTable` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /// <summary> /// Called from GetPropertyReflectionTable within a lock to fill the /// property cach...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 266 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 883
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 704`, `structural_boundaries: 518`, `args: 276`, `func_start: 228`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 351`, `dead_code: 12`, `planned_debt: 5`, `duplicate_logic: 5`, `unreferenced_by_name: 22`
* *Architecture:* `api: 134`, `concurrency: 1`, `import: 21`
* *Defense:* `safety: 234`, `doc: 851`, `sync_locks: 7`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.PowerShell, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Data, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/LanguagePrimitives.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2585.0 | **LOC:** 5889 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **24**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.7%), Complexity Load (formerly Cognitive Load) (17.2%)
- **Documentation Coverage:** 60.8563% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FigureLanguageConversion` **(Many-Argument Workhorses)** (Impact: 96.7)
  * `BaseConvertFrom` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `FigureConversion` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `SetObjectProperties` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `IsCustomTypeConversion` **(Many-Argument Workhorses)** (Impact: 43.4)
    * *Intent:* /// backupTypeTable: /// Used by Remoting Rehydration Logic. While Deserializing a remote object, //...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 175 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 614
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 526`, `structural_boundaries: 497`, `args: 218`, `func_start: 209`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 264`, `dead_code: 11`, `planned_debt: 5`, `duplicate_logic: 4`, `unreferenced_by_name: 14`
* *Architecture:* `api: 144`, `concurrency: 1`, `import: 24`
* *Defense:* `safety: 279`, `doc: 660`, `sync_locks: 9`, `immutability_locks: 32`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.Collections, System.Collections.Generic, System.Collections.Specialized, System.ComponentModel, System.Data, System.Diagnostics.CodeAnalysis, System.DirectoryServices, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/CommandCompletion/CompletionAnalysis.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2554.08 | **LOC:** 2944 | **CtrlFlow:** 27.2% | **Authorship Centralization:** 66.7%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.563; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.8%)
- **Documentation Coverage:** 85.4839% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetResultHelper` **(Many-Argument Workhorses)** (Impact: 566.4)
  * `GetResultForIdentifier` **(Many-Argument Workhorses)** (Impact: 186.8)
  * `GetResultForEnumPropertyValueOfDSCResource` **(Many-Argument Workhorses)** (Impact: 86.7)
  * `TryGetInferredCompletionsForAssignment` **(Many-Argument Workhorses)** (Impact: 58.7)
  * `CompleteAgainstStatementFlags` **(Many-Argument Workhorses)** (Impact: 43.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 306 instances
* *State Mutation (weighted view):* 1022
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 623`, `structural_boundaries: 295`, `args: 70`, `func_start: 53`, `class_start: 3`
* *Risk/State:* `state_mutation: 410`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 30`, `import: 10`
* *Defense:* `safety: 194`, `doc: 56`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System, System.Collections, System.Collections.Generic, System.Linq, System.Management.Automation.Language, System.Management.Automation.Subsystem, System.Management.Automation.Subsystem.DSC, System.Reflection...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/InitialSessionState.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2443.5 | **LOC:** 5683 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.0%), Complexity Load (formerly Cognitive Load) (29.7%)
- **Documentation Coverage:** 44.8845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AnalyzePSSnapInAssembly` **(Many-Argument Workhorses)** (Impact: 118.5)
  * `AnalyzeModuleAssemblyWithReflection` **(Many-Argument Workhorses)** (Impact: 77.9)
  * `ProcessModulesToImport` **(Many-Argument Workhorses)** (Impact: 66.0)
  * `ImportPSSnapIn` **(Stateful Encapsulated Methods)** (Impact: 50.7)
  * `Bind_BindCommands` **(Many-Argument Workhorses)** (Impact: 48.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 201 instances
* *Concurrency (weighted view):* 86
* *State Mutation (weighted view):* 789
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 522`, `structural_boundaries: 250`, `args: 190`, `func_start: 181`, `class_start: 18`
* *Risk/State:* `state_mutation: 387`, `dead_code: 14`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 28`
* *Architecture:* `io: 19`, `api: 239`, `concurrency: 16`, `import: 20`
* *Defense:* `safety: 119`, `doc: 709`, `sync_locks: 24`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.Commands, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Diagnostics.Tracing, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/runtime/MutableTuple.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2385.0 | **LOC:** 2537 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.6%)
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
* *Risk/State:* `state_mutation: 442`, `duplicate_logic: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 181`, `import: 10`
* *Defense:* `safety: 1`, `doc: 37`, `sync_locks: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System.CodeDom.Compiler, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Globalization, System.Linq, System.Linq.Expressions, System.Management.Automation.Language...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/runtime/Operations/MiscOps.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2370.1 | **LOC:** 3752 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Debt Markers (formerly Tech Debt) (54.5%)
- **Documentation Coverage:** 80.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AddCommand` **(Many-Argument Workhorses)** (Impact: 174.8)
  * `Where` **(Many-Argument Workhorses)** (Impact: 149.8)
    * *Intent:* /// <summary> /// Implements the Where(expression) operation on collections. /// </summary> /// <par...
  * `ForEach` **(Many-Argument Workhorses)** (Impact: 123.0)
    * *Intent:* /// <summary> /// Implements the ForEach() operator. /// </summary> /// <param name="enumerator">The...
  * `Bind` **(Many-Argument Workhorses)** (Impact: 45.1)
    * *Intent:* // Handle binding file redirection for commands, like: // dir > out
  * `InvokePipeline` **(Many-Argument Workhorses)** (Impact: 41.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 241 instances
* *State Mutation (weighted view):* 809
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 531`, `structural_boundaries: 311`, `args: 100`, `func_start: 99`, `class_start: 17`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 327`, `dead_code: 8`, `fragile_debt: 1`, `unreferenced_by_name: 49`
* *Architecture:* `io: 4`, `api: 103`, `import: 19`
* *Defense:* `safety: 167`, `doc: 157`, `immutability_locks: 2`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.Commands, Microsoft.PowerShell.Commands.Internal.Format, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized, System.Globalization, System.IO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/parser/TypeInferenceVisitor.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2365.52 | **LOC:** 3339 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.563; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (77.8%), Guard Balance (formerly Safety Score) (68.4%)
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
* *Structure:* `branch: 684`, `structural_boundaries: 420`, `args: 81`, `func_start: 135`, `class_start: 7`
* *Risk/State:* `state_mutation: 259`, `dead_code: 1`, `planned_debt: 3`, `unreferenced_by_name: 65`
* *Architecture:* `api: 54`, `import: 12`
* *Defense:* `safety: 159`, `doc: 119`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Microsoft.Management.Infrastructure.CimClass, Microsoft.Management.Infrastructure.CimInstance, Microsoft.PowerShell.Commands, System.Collections, System.Collections.Generic, System.Globalization, System.Linq, System.Management.Automation.Language...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/TypeTable.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2350.74 | **LOC:** 4780 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **17**; blast radius 1.561; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.3%), Complexity Load (formerly Cognitive Load) (33.4%)
- **Documentation Coverage:** 51.2931% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CheckStandardMembers` **(Many-Argument Workhorses)** (Impact: 101.1)
    * *Intent:* /// Issue appropriate errors and remove members as necessary if: /// - The serialization settings do...
  * `Read_Type` **(I/O & Config Routines)** (Impact: 57.5)
  * `Read_Members` **(Compute Cores)** (Impact: 52.2)
  * `LoadStandardMembersToTypeData` **(Many-Argument Workhorses)** (Impact: 39.3)
    * *Intent:* /// <summary> /// Load the standard members into the passed-in TypeData. /// </summary>
  * `ProcessTypeDataToAdd` **(Many-Argument Workhorses)** (Impact: 29.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 850
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 609`, `structural_boundaries: 297`, `args: 155`, `func_start: 148`, `class_start: 16`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 400`, `dead_code: 2`, `unreferenced_by_name: 13`
* *Architecture:* `io: 5`, `api: 169`, `import: 17`
* *Defense:* `safety: 77`, `doc: 503`, `immutability_locks: 41`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.561
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.003353
  * `Imports (Out-Degree: 2):` System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.ComponentModel, System.Diagnostics, System.Diagnostics.Debug, System.Globalization, System.IO...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/debugger/debugger.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2344.86 | **LOC:** 5955 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.5%), Complexity Load (formerly Cognitive Load) (24.9%)
- **Documentation Coverage:** 31.4904% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `OnDebuggerStop` **(Many-Argument Workhorses)** (Impact: 35.3)
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
* *Structure:* `branch: 454`, `structural_boundaries: 346`, `args: 264`, `func_start: 256`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 366`, `dead_code: 2`, `planned_debt: 2`, `unreferenced_by_name: 17`
* *Architecture:* `io: 5`, `api: 255`, `concurrency: 5`, `import: 18`
* *Defense:* `safety: 144`, `doc: 1088`, `sync_locks: 36`, `immutability_locks: 46`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Microsoft.PowerShell.Commands.Internal.Format, System.Collections, System.Collections.Concurrent, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Diagnostics.CodeAnalysis, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/cimSupport/cmdletization/xml/CoreCLR/cmdlets-over-objects.xmlSerializer.autogen.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 2118.46 | **LOC:** 6689 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (56.1%)
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
* *Structure:* `branch: 1492`, `structural_boundaries: 304`, `args: 148`, `func_start: 65`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 906`, `dead_code: 1`, `unreferenced_by_name: 38`
* *Architecture:* `api: 47`, `import: 5`
* *Defense:* `safety: 2`, `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` System, System.Collections, System.Globalization, System.Xml, System.Xml.Schema
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/namespaces/LocationGlobber.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 2083.42 | **LOC:** 4733 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.563; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (39.3%), Complexity Load (formerly Cognitive Load) (15.9%)
- **Documentation Coverage:** 7.4074% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `ExpandMshGlobPath` **(Many-Argument Workhorses)** (Impact: 153.6)
    * *Intent:* /// processing the <paramref name="path"/>. /// </exception> /// <exception cref="ItemNotFoundExcept...
  * `ExpandGlobPath` **(Many-Argument Workhorses)** (Impact: 136.7)
    * *Intent:* /// <exception cref="InvalidOperationException"> /// If the <paramref name="path"/> starts with "~" ...
  * `GenerateRelativePath` **(Many-Argument Workhorses)** (Impact: 129.5)
    * *Intent:* /// If <paramref name="path"/> or <paramref name="drive"/> is null. /// </exception> /// <exception ...
  * `GenerateNewPSPathsWithGlobLeaf` **(Many-Argument Workhorses)** (Impact: 93.3)
    * *Intent:* /// </exception> /// <exception cref="ProviderInvocationException"> /// If the provider associated w...
  * `GetChildNamesInDir` **(Many-Argument Workhorses)** (Impact: 85.0)
    * *Intent:* /// </exception> /// <exception cref="ProviderInvocationException"> /// If the provider associated w...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 179 instances
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 714`, `structural_boundaries: 107`, `args: 49`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `state_mutation: 245`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 35`, `import: 5`
* *Defense:* `safety: 295`, `doc: 1321`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections.Generic, System.Collections.ObjectModel, System.Management.Automation, System.Management.Automation.Provider, System.Text
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/CmdletParameterBinderController.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 2081.1 | **LOC:** 4654 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.563; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.8%), Complexity Load (formerly Cognitive Load) (23.8%)
- **Documentation Coverage:** 19.5122% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GetMissingMandatoryParameters` **(Many-Argument Workhorses)** (Impact: 184.4)
    * *Intent:* /// more than one valid parameter sets and the unbound mandatory parameters are not /// consistent a...
  * `GetDefaultParameterValuePairs` **(Compute Cores)** (Impact: 64.8)
    * *Intent:* /// <summary> /// Get all available default parameter value pairs. /// </summary> /// <returns>Retur...
  * `BindParameter` **(Many-Argument Workhorses)** (Impact: 64.0)
    * *Intent:* /// </summary> /// <param name="argument"> /// The argument to be bound. /// </param> /// <param nam...
  * `ValidateParameterSets` **(Many-Argument Workhorses)** (Impact: 43.6)
    * *Intent:* /// </param> /// <param name="setDefault"> /// If true, the default parameter set will be selected i...
  * `RestoreParameter` **(Stateful Encapsulated Methods)** (Impact: 42.2)
    * *Intent:* /// <summary> /// Restores the specified parameter to the original value. /// </summary> /// <param ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 239 instances
* *State Mutation (weighted view):* 797
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 543`, `structural_boundaries: 133`, `args: 70`, `func_start: 62`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 319`, `dead_code: 11`, `unreferenced_by_name: 5`
* *Architecture:* `api: 33`, `import: 11`
* *Defense:* `safety: 82`, `doc: 569`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics.CodeAnalysis, System.Globalization, System.Linq, System.Management.Automation.Host, System.Management.Automation.Internal...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/DscSupport/CimDSCParser.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2014.76 | **LOC:** 4077 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **20**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (31.1%)
- **Documentation Coverage:** 18.8312% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateKeywordFromCimClass` **(Many-Argument Workhorses)** (Impact: 100.9)
    * *Intent:* /// <summary> /// A method to generate a keyword from a CIM class object. This is used for DSC. /// ...
  * `LoadResourcesFromModule` **(Many-Argument Workhorses)** (Impact: 76.8)
    * *Intent:* /// <summary> /// Load DSC resources from specified module. /// </summary> /// <param name="scriptEx...
  * `ConvertCimInstanceToObject` **(Many-Argument Workhorses)** (Impact: 63.0)
    * *Intent:* /// <summary> /// Convert Cim Instance representing Resource desired state to Powershell Class Objec...
  * `MapTypeToMofType` **(Many-Argument Workhorses)** (Impact: 60.7)
  * `MapAttributesToMof` **(Many-Argument Workhorses)** (Impact: 54.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 191 instances
* *State Mutation (weighted view):* 648
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 579`, `structural_boundaries: 361`, `args: 110`, `func_start: 97`, `class_start: 5`
* *Risk/State:* `state_mutation: 266`, `dead_code: 6`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 12`
* *Architecture:* `io: 58`, `api: 67`, `import: 20`
* *Defense:* `safety: 115`, `doc: 472`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` Microsoft.Management.Infrastructure, Microsoft.Management.Infrastructure.Generic, Microsoft.Management.Infrastructure.Serialization, Microsoft.PowerShell.Commands, Microsoft.PowerShell.SecureStringHelper, System, System.Collections, System.Collections.Generic...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1801.5 | **LOC:** 6192 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **21** in-repo importer(s); it depends on **17**; blast radius 7.904; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (48.9%), Guard Balance (formerly Safety Score) (44.3%)
- **Documentation Coverage:** 5.8559% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SetStateChanged` **(Many-Argument Workhorses)** (Impact: 65.3)
    * *Intent:* /// <summary> /// Sets the state of this powershell instance. /// </summary> /// <param name="stateI...
  * `CoreInvokeAsync` **(Many-Argument Workhorses)** (Impact: 57.7)
    * *Intent:* /// The output buffer to attach to the IAsyncResult returned by this method /// </param> /// <except...
  * `CoreStop` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* /// Called by both Sync Stop and Async Stop. /// If isSyncCall is false, then an IAsyncResult object...
  * `CoreInvoke` **(Many-Argument Workhorses)** (Impact: 46.2)
    * *Intent:* /// <summary> /// Core invocation method. /// </summary> /// <typeparam name="TInput">input type</ty...
  * `ConnectAsync` **(Many-Argument Workhorses)** (Impact: 40.0)
    * *Intent:* /// <summary> /// Asynchronously connects to a running command on a remote server. /// The returned ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 165 instances
* *State Mutation (weighted view):* 646
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 374`, `structural_boundaries: 144`, `args: 131`, `func_start: 131`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 316`, `dead_code: 15`, `planned_debt: 2`, `fragile_debt: 1`, `unreferenced_by_name: 14`
* *Architecture:* `api: 157`, `concurrency: 14`, `import: 17`
* *Defense:* `safety: 143`, `doc: 2432`, `sync_locks: 36`, `immutability_locks: 16`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.904
  * `Choke Point (Betweenness):` 2.5e-05 | `Ripple Effect (Closeness):` 0.014085
  * `Imports (Out-Degree: 2):` Microsoft.Management.Infrastructure, Microsoft.PowerShell.Telemetry, System, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Diagnostics, System.Diagnostics.CodeAnalysis...
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `src/System.Management.Automation/engine/MshMemberInfo.cs` (CSHARP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1702.4 | **LOC:** 5158 | **CtrlFlow:** 11.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.563; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (48.7%), Debt Markers (formerly Tech Debt) (19.2%)
- **Documentation Coverage:** 31.0249% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `CreateMethodGroup` **(Stateful Encapsulated Methods)** (Impact: 29.5)
  * `GetIntegratedMembers` **(Stateful Encapsulated Methods)** (Impact: 27.4)
  * `EnsureReservedMemberIsLoaded` **(Stateful Encapsulated Methods)** (Impact: 24.1)
    * *Intent:* /// <summary> /// Method which checks if the <paramref name="name"/> is reserved and if so /// it wi...
  * `ToString` **(I/O & Config Routines)** (Impact: 18.9)
  * `Match` **(Stateful Encapsulated Methods)** (Impact: 17.4)
    * *Intent:* /// <summary> /// Returns all members in memberList matching name and memberTypes. /// </summary> //...
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 120 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 485
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 354`, `structural_boundaries: 373`, `args: 258`, `func_start: 188`, `class_start: 46`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 245`, `dead_code: 2`, `duplicate_logic: 10`, `unreferenced_by_name: 8`
* *Architecture:* `api: 332`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 136`, `doc: 1269`, `sync_locks: 12`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.563
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` Microsoft.PowerShell, System.Collections, System.Collections.Generic, System.Collections.ObjectModel, System.Collections.Specialized, System.ComponentModel, System.Diagnostics.CodeAnalysis, System.Globalization...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `tools/packaging/packaging.psm1` -> Churn: **100.0%** | Cog Load: 57.6994% | Debt: 13.8916%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/System.Management.Automation/engine/Modules/ModuleCmdletBase.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 4927.12
- `src/System.Management.Automation/engine/runtime/Binding/Binders.cs` -> **Jordan Borean** (100.0% isolated ownership) | Magnitude: 4521.9
- `src/System.Management.Automation/namespaces/FileSystemProvider.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 3905.16
- `src/Microsoft.WSMan.Management/ConfigProvider.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 3514.16
- `src/System.Management.Automation/engine/serialization.cs` -> **xtqqczze** (100.0% isolated ownership) | Magnitude: 3018.46

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.999%)
- `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` -> **Severity: 0.002** (Bridge: 0.0 * Flux: 99.8341%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `tools/Xml/Xml.psm1` -> **Severity: 4.657** (Embedded: 0.0595 * Error Risk: 78.2714%)
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 4.015** (Embedded: 0.0461 * Error Risk: 86.9992%)
- `src/System.Management.Automation/utils/tracing/Tracing.cs` -> **Severity: 1.54** (Embedded: 0.0275 * Error Risk: 55.9714%)
- `src/System.Management.Automation/engine/hostifaces/PowerShell.cs` -> **Severity: 0.623** (Embedded: 0.0141 * Error Risk: 44.2516%)
- `src/System.Management.Automation/utils/Telemetry.cs` -> **Severity: 0.619** (Embedded: 0.013 * Error Risk: 47.7978%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `tools/Xml/Xml.psm1` -> **Severity: 5600.6** (Blast Radius: 56.006 * Doc Risk: 100.0%)
- `src/Microsoft.PowerShell.ConsoleHost/host/msh/Serialization.cs` -> **Severity: 2937.572** (Blast Radius: 31.474 * Doc Risk: 93.3333%)
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Extensions.cs` -> **Severity: 452.556** (Blast Radius: 13.011 * Doc Risk: 34.7826%)
- `src/System.Management.Automation/utils/tracing/Tracing.cs` -> **Severity: 327.04** (Blast Radius: 16.352 * Doc Risk: 20.0%)
- `src/Microsoft.PowerShell.LocalAccounts/LocalAccounts/Native.cs` -> **Severity: 128.1** (Blast Radius: 1.281 * Doc Risk: 100.0%)

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
