# ARCHITECTURAL_BRIEF: vscode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_web/vscode` |
| **Timestamp** | `2026-08-07T04:28:53.873951+00:00` |
| **Scan Duration** | `38.06s` |
| **Git Branch** | `main` |
| **Git Commit** | `a8d7dcd8683eef847562052b722d477b5134ef76` |
| **Git Remote** | `https://github.com/microsoft/vscode.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 6697 malicious artifacts.

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
| Total Artifacts | 10238 |
| Analyzed Artifacts (Scanned) | 8172 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 2066 |
| Total LOC | 1491261 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 79.8% |
| Dominant Lang | PLAINTEXT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2605 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 105 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 6472 | 1251212 | 79.2% |
| JSON | 687 | 151619 | 8.4% |
| CSS | 329 | 35559 | 4.0% |
| PLAINTEXT | 218 | 44 | 2.7% |
| XML | 84 | 425 | 1.0% |
| HTML | 79 | 5398 | 1.0% |
| MARKDOWN | 77 | 0 | 0.9% |
| RUST | 68 | 12144 | 0.8% |
| JAVASCRIPT | 66 | 30000 | 0.8% |
| SHELL | 56 | 2628 | 0.7% |
| BATCH | 19 | 729 | 0.2% |
| POWERSHELL | 8 | 447 | 0.1% |
| SCHEME | 5 | 525 | 0.1% |
| DOCKERFILE | 2 | 451 | 0.0% |
| MAKEFILE | 1 | 1 | 0.0% |
| YAML | 1 | 79 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.566`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 3083 | 37.7% |
| file_cluster_13 | 2960 | 36.2% |
| file_cluster_4 | 1464 | 17.9% |
| file_cluster_16 | 99 | 1.2% |
| file_cluster_17 | 91 | 1.1% |
| file_cluster_0 | 90 | 1.1% |
| Unknown | 43 | 0.5% |
| file_cluster_11 | 32 | 0.4% |
| file_cluster_2 | 24 | 0.3% |
| file_cluster_9 | 11 | 0.1% |
| file_cluster_12 | 5 | 0.1% |
| file_cluster_1 | 3 | 0.0% |
| file_cluster_6 | 2 | 0.0% |
| file_cluster_15 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 251 | 3.1% |
| Static: Minified & Vendor Opaque Mass | 12 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 2066*

**Composition by Extension & Reason:**
- `.ts`: 387x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 7x Excluded (Saturation: Line 9 exceeds 500 chars), 6x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.png`: 321x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 75x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Massive Static Asset Blob: 6001 LOC)
- `no_extension`: 153x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 15x Excluded (Unsupported Extension: '.code-snippets'), 5x Unsupported Format (.undeterminable)
- `.snap`: 128x Unsupported Format (.snap), 6x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.md`: 92x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.tst`: 90x Unsupported Format (.tst)
- `.yml`: 63x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 31 LOC)
- `.mts`: 61x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 37x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2482 LOC), 1x Excluded (Saturation: Line 14 exceeds 500 chars)
- `.ico`: 31x Excluded (Explicitly Denied Extension: '.ico')
- `.mp3`: 31x Excluded (Explicitly Denied Extension: '.mp3')
- `.icns`: 29x Excluded (Unsupported Extension: '.icns')
- `.txt`: 12x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Binary Format Detected), 3x Excluded (Embedded Array/Matrix Payload: 4660 commas in 1136 LOC)
- `.css`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Excluded (Binary Format Detected), 1x Excluded (Saturation: Line 23 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 43.6 | 31.7 | 100.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 47.5 | 53.1 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 32.5 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 16.3 | 2.3 | 0.0 |
| API Exposure | 0.0 | 19.8 | 3.4 | 2.4 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 37.0 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 43.4 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.3 | 0.7 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 92.7 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.1 | 0.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 30.3 | 18.6 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 99.9 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/vs/workbench/contrib/notebook/test/browser/diff/notebookDiffService.test.ts` (Hits: 356)
- `src/vs/base/test/common/oauth.test.ts` (Hits: 337)
- `src/vs/base/test/common/path.test.ts` (Hits: 238)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **assert.ts** (`src/vs/base/common/assert.ts`) — 1030 inbound connections
2. **css.scm** (`src/vs/editor/common/languages/highlights/css.scm`) — 340 inbound connections
3. **fs.ts** (`extensions/typescript-language-features/src/utils/fs.ts`) — 158 inbound connections
4. **path.ts** (`src/vs/base/common/path.ts`) — 143 inbound connections
5. **xterm.css** (`src/vs/workbench/contrib/terminal/browser/media/xterm.css`) — 81 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sessions.common.main.ts** (`src/vs/sessions/sessions.common.main.ts`) — 258 outbound dependencies
2. **workbench.common.main.ts** (`src/vs/workbench/workbench.common.main.ts`) — 236 outbound dependencies
3. **workbenchTestServices.ts** (`src/vs/workbench/test/browser/workbenchTestServices.ts`) — 189 outbound dependencies
4. **chat.contribution.ts** (`src/vs/workbench/contrib/chat/browser/chat.contribution.ts`) — 172 outbound dependencies
5. **app.ts** (`src/vs/code/electron-main/app.ts`) — 138 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `_showOutput` (@ `src/vs/workbench/contrib/tasks/browser/abstractTaskService.ts`) -> Impact: **968.0** | LOC: 1361
- `constructor` (@ `src/vs/base/browser/ui/tree/abstractTree.ts`) -> Impact: **818.2** | LOC: 1390
- `webviewPreloads` (@ `src/vs/workbench/contrib/notebook/browser/view/renderers/webviewPreloads.ts`) -> Impact: **804.2** | LOC: 1564
- `constructor` (@ `src/vs/workbench/contrib/testing/browser/testingExplorerView.ts`) -> Impact: **737.8** | LOC: 807
  * *Intent:* /** * @override */
- `resolve` (@ `src/vs/base/common/path.ts`) -> Impact: **661.6** | LOC: 1073
  * *Intent:* /*--------------------------------------------------------------------------------------------- * Copyright (c) Microsoft Corporation. All rights rese...
- `_open` (@ `src/vs/workbench/contrib/terminal/browser/terminalInstance.ts`) -> Impact: **603.2** | LOC: 1082
- `delete` (@ `src/vs/workbench/contrib/chat/browser/widget/input/chatInputPart.ts`) -> Impact: **570.2** | LOC: 984
- `promise` (@ `extensions/typescript-language-features/src/languageFeatures/completions.ts`) -> Impact: **514.0** | LOC: 702
- `doScoreFuzzy` (@ `src/vs/base/common/fuzzyScorer.ts`) -> Impact: **494.9** | LOC: 734
  * *Intent:* // if (DEBUG) { // console.log(`%cFinal Score: ${res[0]}`, 'font-weight: bold'); // console.groupEnd(); // }
- `suite` (@ `src/vs/workbench/contrib/terminalContrib/chatAgentTools/test/electron-browser/treeSitterCommandParser.test.ts`) -> Impact: **444.1** | LOC: 291

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `__monolith__` | 12 | 5162.08 | 1.87% | 0.71% |
| `extensions` | 7 | 5096.98 | 6.02% | 0.0% |
| `extensions/mermaid-chat-features` | 8 | 5096.52 | 3.25% | 0.0% |
| `extensions/markdown-language-features` | 7 | 5094.84 | 2.98% | 0.0% |
| `extensions/emmet` | 9 | 5092.9 | 3.49% | 0.0% |
| `extensions/typescript-language-features` | 7 | 5092.0 | 2.23% | 0.0% |
| `test/monaco` | 5 | 5087.36 | 2.0% | 0.0% |
| `extensions/markdown-math` | 8 | 5078.32 | 4.97% | 0.0% |
| `extensions/npm` | 7 | 5077.32 | 3.67% | 0.0% |
| `extensions/git-base` | 8 | 5077.0 | 2.87% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `cli/src/tunnels/challenge.rs` -> **100.0%** Exposure
- `cli/src/tunnels/socket_signal.rs` -> **100.0%** Exposure
- `cli/src/util/errors.rs` -> **100.0%** Exposure
- `cli/src/util/os.rs` -> **100.0%** Exposure
- `cli/src/util/sync.rs` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `cli/src/tunnels/server_multiplexer.rs` -> **100.0%** Exposure
- `cli/src/util/io.rs` -> **100.0%** Exposure
- `cli/src/util/machine.rs` -> **100.0%** Exposure
- `cli/src/util/os.rs` -> **100.0%** Exposure
- `cli/src/util/ring_buffer.rs` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/vs/platform/userDataSync/test/common/extensionsMerge.test.ts` -> **1** Orphaned Functions | **365** Duplicates
- `src/vs/base/test/common/yaml.test.ts` -> **0** Orphaned Functions | **267** Duplicates
- `src/vs/editor/test/browser/controller/cursor.test.ts` -> **2** Orphaned Functions | **259** Duplicates
- `src/vs/workbench/contrib/terminalContrib/chatAgentTools/test/electron-browser/runInTerminalTool.test.ts` -> **9** Orphaned Functions | **228** Duplicates
- `src/vs/workbench/contrib/chat/test/browser/agentSessions/agentSessionsDataSource.test.ts` -> **3** Orphaned Functions | **204** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`extensions/git/src/actionButton.ts`** -> AI Confidence: **99.39%**
2. **`src/vs/base/browser/ui/actionbar/actionbar.ts`** -> AI Confidence: **99.39%**
3. **`src/vs/base/browser/ui/dialog/dialog.ts`** -> AI Confidence: **99.39%**
4. **`src/vs/base/browser/ui/iconLabel/iconLabel.ts`** -> AI Confidence: **99.39%**
5. **`src/vs/editor/common/diff/defaultLinesDiffComputer/heuristicSequenceOptimizations.ts`** -> AI Confidence: **99.39%**
6. **`src/vs/editor/common/model/guidesTextModelPart.ts`** -> AI Confidence: **99.39%**
7. **`src/vs/editor/common/tokens/sparseTokensStore.ts`** -> AI Confidence: **99.39%**
8. **`src/vs/editor/common/viewModel/monospaceLineBreaksComputer.ts`** -> AI Confidence: **99.39%**
9. **`src/vs/platform/markers/common/markerService.ts`** -> AI Confidence: **99.39%**
10. **`src/vs/workbench/browser/parts/editor/editor.contribution.ts`** -> AI Confidence: **99.39%**
11. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentHost/stateToProgressAdapter.ts`** -> AI Confidence: **99.39%**
12. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugModelTurnContentRenderer.ts`** -> AI Confidence: **99.39%**
13. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatAttachmentsContentPart.ts`** -> AI Confidence: **99.39%**
14. **`src/vs/workbench/contrib/notebook/browser/notebookOptions.ts`** -> AI Confidence: **99.39%**
15. **`src/vs/workbench/contrib/terminal/browser/xterm/decorationStyles.ts`** -> AI Confidence: **99.39%**
16. **`src/vs/workbench/contrib/terminalContrib/links/browser/terminalLocalLinkDetector.ts`** -> AI Confidence: **99.39%**
17. **`src/vs/workbench/contrib/update/browser/updateTooltip.ts`** -> AI Confidence: **99.39%**
18. **`src/vs/workbench/browser/parts/statusbar/statusbarItem.ts`** -> AI Confidence: **99.35%**
19. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugFlowChartView.ts`** -> AI Confidence: **99.35%**
20. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatThinkingContentPart.ts`** -> AI Confidence: **99.35%**
21. **`src/vs/workbench/contrib/chat/test/common/voiceChatService.test.ts`** -> AI Confidence: **99.35%**
22. **`src/vs/workbench/contrib/terminal/common/scripts/shellIntegration-bash.sh`** -> AI Confidence: **99.34%**
23. **`extensions/terminal-suggest/scripts/pullFishBuiltins.ts`** -> AI Confidence: **99.32%**
24. **`extensions/typescript-language-features/src/languageFeatures/util/snippetForFunctionCall.ts`** -> AI Confidence: **99.32%**
25. **`src/vs/base/test/browser/comparers.test.ts`** -> AI Confidence: **99.32%**
26. **`src/vs/editor/common/model/intervalTree.ts`** -> AI Confidence: **99.32%**
27. **`src/vs/platform/product/common/product.ts`** -> AI Confidence: **99.32%**
28. **`cli/src/update_service.rs`** -> AI Confidence: **99.31%**
29. **`scripts/code-sessions-web.js`** -> AI Confidence: **99.31%**
30. **`scripts/code-web.js`** -> AI Confidence: **99.31%**
31. **`src/vs/editor/test/node/diffing/fixtures/difficult-move/1.js`** -> AI Confidence: **99.31%**
32. **`src/vs/editor/test/node/diffing/fixtures/difficult-move/2.js`** -> AI Confidence: **99.31%**
33. **`extensions/emmet/src/updateImageSize.ts`** -> AI Confidence: **99.31%**
34. **`extensions/emmet/src/util.ts`** -> AI Confidence: **99.31%**
35. **`extensions/extension-editing/src/extensionLinter.ts`** -> AI Confidence: **99.31%**
36. **`extensions/git/src/blame.ts`** -> AI Confidence: **99.31%**
37. **`extensions/git/src/cloneManager.ts`** -> AI Confidence: **99.31%**
38. **`extensions/git/src/decorationProvider.ts`** -> AI Confidence: **99.31%**
39. **`extensions/git/src/git.ts`** -> AI Confidence: **99.31%**
40. **`extensions/git/src/historyProvider.ts`** -> AI Confidence: **99.31%**
41. **`extensions/git/src/statusbar.ts`** -> AI Confidence: **99.31%**
42. **`extensions/git/src/timelineProvider.ts`** -> AI Confidence: **99.31%**
43. **`extensions/github-authentication/src/github.ts`** -> AI Confidence: **99.31%**
44. **`extensions/github-authentication/src/githubServer.ts`** -> AI Confidence: **99.31%**
45. **`extensions/github/src/commands.ts`** -> AI Confidence: **99.31%**
46. **`extensions/github/src/publish.ts`** -> AI Confidence: **99.31%**
47. **`extensions/markdown-language-features/preview-src/index.ts`** -> AI Confidence: **99.31%**
48. **`extensions/markdown-language-features/src/languageFeatures/copyFiles/shared.ts`** -> AI Confidence: **99.31%**
49. **`extensions/markdown-language-features/src/markdownEngine.ts`** -> AI Confidence: **99.31%**
50. **`extensions/markdown-language-features/src/preview/preview.ts`** -> AI Confidence: **99.31%**
51. **`extensions/microsoft-authentication/src/node/authProvider.ts`** -> AI Confidence: **99.31%**
52. **`extensions/npm/src/features/packageJSONContribution.ts`** -> AI Confidence: **99.31%**
53. **`extensions/terminal-suggest/src/fig/autocomplete-parser/parseArguments.ts`** -> AI Confidence: **99.31%**
54. **`extensions/terminal-suggest/src/fig/figInterface.ts`** -> AI Confidence: **99.31%**
55. **`extensions/terminal-suggest/src/terminalSuggestMain.ts`** -> AI Confidence: **99.31%**
56. **`extensions/terminal-suggest/src/upstreamSpecs.ts`** -> AI Confidence: **99.31%**
57. **`extensions/typescript-language-features/src/configuration/configuration.electron.ts`** -> AI Confidence: **99.31%**
58. **`extensions/typescript-language-features/src/languageFeatures/completions.ts`** -> AI Confidence: **99.31%**
59. **`extensions/typescript-language-features/src/languageFeatures/documentSymbol.ts`** -> AI Confidence: **99.31%**
60. **`extensions/typescript-language-features/src/tsServer/bufferSyncSupport.ts`** -> AI Confidence: **99.31%**
61. **`extensions/typescript-language-features/src/tsServer/server.ts`** -> AI Confidence: **99.31%**
62. **`extensions/typescript-language-features/src/tsServer/serverProcess.electron.ts`** -> AI Confidence: **99.31%**
63. **`extensions/typescript-language-features/src/tsServer/spawner.ts`** -> AI Confidence: **99.31%**
64. **`extensions/typescript-language-features/src/typescriptServiceClient.ts`** -> AI Confidence: **99.31%**
65. **`extensions/typescript-language-features/web/src/serverHost.ts`** -> AI Confidence: **99.31%**
66. **`src/bootstrap-meta.ts`** -> AI Confidence: **99.31%**
67. **`src/main.ts`** -> AI Confidence: **99.31%**
68. **`src/server-main.ts`** -> AI Confidence: **99.31%**
69. **`src/vs/base/browser/contextmenu.ts`** -> AI Confidence: **99.31%**
70. **`src/vs/base/browser/markdownRenderer.ts`** -> AI Confidence: **99.31%**
71. **`src/vs/base/browser/ui/actionbar/actionViewItems.ts`** -> AI Confidence: **99.31%**
72. **`src/vs/base/browser/ui/breadcrumbs/breadcrumbsWidget.ts`** -> AI Confidence: **99.31%**
73. **`src/vs/base/browser/ui/button/button.ts`** -> AI Confidence: **99.31%**
74. **`src/vs/base/browser/ui/centered/centeredViewLayout.ts`** -> AI Confidence: **99.31%**
75. **`src/vs/base/browser/ui/dropdown/dropdown.ts`** -> AI Confidence: **99.31%**
76. **`src/vs/base/browser/ui/dropdown/dropdownActionViewItem.ts`** -> AI Confidence: **99.31%**
77. **`src/vs/base/browser/ui/findinput/findInput.ts`** -> AI Confidence: **99.31%**
78. **`src/vs/base/browser/ui/findinput/replaceInput.ts`** -> AI Confidence: **99.31%**
79. **`src/vs/base/browser/ui/grid/gridview.ts`** -> AI Confidence: **99.31%**
80. **`src/vs/base/browser/ui/highlightedlabel/highlightedLabel.ts`** -> AI Confidence: **99.31%**
81. **`src/vs/base/browser/ui/icons/iconSelectBox.ts`** -> AI Confidence: **99.31%**
82. **`src/vs/base/browser/ui/inputbox/inputBox.ts`** -> AI Confidence: **99.31%**
83. **`src/vs/base/browser/ui/keybindingLabel/keybindingLabel.ts`** -> AI Confidence: **99.31%**
84. **`src/vs/base/browser/ui/list/listView.ts`** -> AI Confidence: **99.31%**
85. **`src/vs/base/browser/ui/menu/menu.ts`** -> AI Confidence: **99.31%**
86. **`src/vs/base/browser/ui/menu/menubar.ts`** -> AI Confidence: **99.31%**
87. **`src/vs/base/browser/ui/radio/radio.ts`** -> AI Confidence: **99.31%**
88. **`src/vs/base/browser/ui/scrollbar/abstractScrollbar.ts`** -> AI Confidence: **99.31%**
89. **`src/vs/base/browser/ui/scrollbar/scrollableElement.ts`** -> AI Confidence: **99.31%**
90. **`src/vs/base/browser/ui/selectBox/selectBoxCustom.ts`** -> AI Confidence: **99.31%**
91. **`src/vs/base/browser/ui/selectBox/selectBoxNative.ts`** -> AI Confidence: **99.31%**
92. **`src/vs/base/browser/ui/splitview/paneview.ts`** -> AI Confidence: **99.31%**
93. **`src/vs/base/browser/ui/splitview/splitview.ts`** -> AI Confidence: **99.31%**
94. **`src/vs/base/browser/ui/toggle/toggle.ts`** -> AI Confidence: **99.31%**
95. **`src/vs/base/browser/ui/toolbar/toolbar.ts`** -> AI Confidence: **99.31%**
96. **`src/vs/base/browser/ui/tree/abstractTree.ts`** -> AI Confidence: **99.31%**
97. **`src/vs/base/browser/ui/tree/indexTreeModel.ts`** -> AI Confidence: **99.31%**
98. **`src/vs/base/common/event.ts`** -> AI Confidence: **99.31%**
99. **`src/vs/base/common/fuzzyScorer.ts`** -> AI Confidence: **99.31%**
100. **`src/vs/base/common/observableInternal/logging/consoleObservableLogger.ts`** -> AI Confidence: **99.31%**
101. **`src/vs/base/common/observableInternal/observables/derivedImpl.ts`** -> AI Confidence: **99.31%**
102. **`src/vs/base/common/observableInternal/observables/lazyObservableValue.ts`** -> AI Confidence: **99.31%**
103. **`src/vs/base/parts/ipc/node/ipc.cp.ts`** -> AI Confidence: **99.31%**
104. **`src/vs/base/parts/ipc/node/ipc.net.ts`** -> AI Confidence: **99.31%**
105. **`src/vs/base/test/common/fuzzyScorer.test.ts`** -> AI Confidence: **99.31%**
106. **`src/vs/base/test/common/resources.test.ts`** -> AI Confidence: **99.31%**
107. **`src/vs/base/test/common/ternarySearchtree.test.ts`** -> AI Confidence: **99.31%**
108. **`src/vs/code/node/cli.ts`** -> AI Confidence: **99.31%**
109. **`src/vs/editor/browser/config/fontMeasurements.ts`** -> AI Confidence: **99.31%**
110. **`src/vs/editor/browser/controller/editContext/native/screenReaderSupport.ts`** -> AI Confidence: **99.31%**
111. **`src/vs/editor/browser/controller/editContext/screenReaderUtils.ts`** -> AI Confidence: **99.31%**
112. **`src/vs/editor/browser/controller/mouseHandler.ts`** -> AI Confidence: **99.31%**
113. **`src/vs/editor/browser/gpu/raster/glyphRasterizer.ts`** -> AI Confidence: **99.31%**
114. **`src/vs/editor/browser/gpu/renderStrategy/fullFileRenderStrategy.ts`** -> AI Confidence: **99.31%**
115. **`src/vs/editor/browser/services/abstractCodeEditorService.ts`** -> AI Confidence: **99.31%**
116. **`src/vs/editor/browser/services/openerService.ts`** -> AI Confidence: **99.31%**
117. **`src/vs/editor/browser/view/domLineBreaksComputer.ts`** -> AI Confidence: **99.31%**
118. **`src/vs/editor/browser/view/viewController.ts`** -> AI Confidence: **99.31%**
119. **`src/vs/editor/browser/view/viewLayer.ts`** -> AI Confidence: **99.31%**
120. **`src/vs/editor/browser/viewParts/blockDecorations/blockDecorations.ts`** -> AI Confidence: **99.31%**
121. **`src/vs/editor/browser/viewParts/contentWidgets/contentWidgets.ts`** -> AI Confidence: **99.31%**
122. **`src/vs/editor/browser/viewParts/decorations/decorations.ts`** -> AI Confidence: **99.31%**
123. **`src/vs/editor/browser/viewParts/glyphMargin/glyphMargin.ts`** -> AI Confidence: **99.31%**
124. **`src/vs/editor/browser/viewParts/minimap/minimap.ts`** -> AI Confidence: **99.31%**
125. **`src/vs/editor/browser/viewParts/overlayWidgets/overlayWidgets.ts`** -> AI Confidence: **99.31%**
126. **`src/vs/editor/browser/viewParts/overviewRuler/decorationsOverviewRuler.ts`** -> AI Confidence: **99.31%**
127. **`src/vs/editor/browser/viewParts/selections/selections.ts`** -> AI Confidence: **99.31%**
128. **`src/vs/editor/browser/viewParts/viewCursors/viewCursor.ts`** -> AI Confidence: **99.31%**
129. **`src/vs/editor/browser/viewParts/viewCursors/viewCursors.ts`** -> AI Confidence: **99.31%**
130. **`src/vs/editor/browser/viewParts/viewLines/viewLine.ts`** -> AI Confidence: **99.31%**
131. **`src/vs/editor/browser/viewParts/viewLines/viewLines.ts`** -> AI Confidence: **99.31%**
132. **`src/vs/editor/browser/viewParts/viewLinesGpu/viewLinesGpu.ts`** -> AI Confidence: **99.31%**
133. **`src/vs/editor/browser/viewParts/viewZones/viewZones.ts`** -> AI Confidence: **99.31%**
134. **`src/vs/editor/browser/viewParts/whitespace/whitespace.ts`** -> AI Confidence: **99.31%**
135. **`src/vs/editor/browser/widget/codeEditor/codeEditorContributions.ts`** -> AI Confidence: **99.31%**
136. **`src/vs/editor/browser/widget/codeEditor/codeEditorWidget.ts`** -> AI Confidence: **99.31%**
137. **`src/vs/editor/browser/widget/diffEditor/components/accessibleDiffViewer.ts`** -> AI Confidence: **99.31%**
138. **`src/vs/editor/browser/widget/diffEditor/components/diffEditorDecorations.ts`** -> AI Confidence: **99.31%**
139. **`src/vs/editor/browser/widget/diffEditor/components/diffEditorViewZones/diffEditorViewZones.ts`** -> AI Confidence: **99.31%**
140. **`src/vs/editor/browser/widget/diffEditor/diffEditorViewModel.ts`** -> AI Confidence: **99.31%**
141. **`src/vs/editor/browser/widget/diffEditor/diffEditorWidget.ts`** -> AI Confidence: **99.31%**
142. **`src/vs/editor/common/commands/shiftCommand.ts`** -> AI Confidence: **99.31%**
143. **`src/vs/editor/common/commands/trimTrailingWhitespaceCommand.ts`** -> AI Confidence: **99.31%**
144. **`src/vs/editor/common/config/editorConfigurationSchema.ts`** -> AI Confidence: **99.31%**
145. **`src/vs/editor/common/config/editorOptions.ts`** -> AI Confidence: **99.31%**
146. **`src/vs/editor/common/core/edits/lineEdit.ts`** -> AI Confidence: **99.31%**
147. **`src/vs/editor/common/core/edits/textEdit.ts`** -> AI Confidence: **99.31%**
148. **`src/vs/editor/common/cursor/cursor.ts`** -> AI Confidence: **99.31%**
149. **`src/vs/editor/common/cursor/cursorCollection.ts`** -> AI Confidence: **99.31%**
150. **`src/vs/editor/common/cursor/cursorDeleteOperations.ts`** -> AI Confidence: **99.31%**
151. **`src/vs/editor/common/cursor/cursorMoveCommands.ts`** -> AI Confidence: **99.31%**
152. **`src/vs/editor/common/cursor/cursorMoveOperations.ts`** -> AI Confidence: **99.31%**
153. **`src/vs/editor/common/cursor/cursorTypeEditOperations.ts`** -> AI Confidence: **99.31%**
154. **`src/vs/editor/common/cursor/cursorTypeOperations.ts`** -> AI Confidence: **99.31%**
155. **`src/vs/editor/common/cursor/cursorWordOperations.ts`** -> AI Confidence: **99.31%**
156. **`src/vs/editor/common/diff/defaultLinesDiffComputer/computeMovedLines.ts`** -> AI Confidence: **99.31%**
157. **`src/vs/editor/common/diff/defaultLinesDiffComputer/defaultLinesDiffComputer.ts`** -> AI Confidence: **99.31%**
158. **`src/vs/editor/common/diff/defaultLinesDiffComputer/linesSliceCharSequence.ts`** -> AI Confidence: **99.31%**
159. **`src/vs/editor/common/diff/legacyLinesDiffComputer.ts`** -> AI Confidence: **99.31%**
160. **`src/vs/editor/common/diff/rangeMapping.ts`** -> AI Confidence: **99.31%**
161. **`src/vs/editor/common/languages/autoIndent.ts`** -> AI Confidence: **99.31%**
162. **`src/vs/editor/common/languages/textToHtmlTokenizer.ts`** -> AI Confidence: **99.31%**
163. **`src/vs/editor/common/model/bracketPairsTextModelPart/bracketPairsTree/bracketPairsTree.ts`** -> AI Confidence: **99.31%**
164. **`src/vs/editor/common/model/bracketPairsTextModelPart/bracketPairsTree/parser.ts`** -> AI Confidence: **99.31%**
165. **`src/vs/editor/common/model/bracketPairsTextModelPart/bracketPairsTree/tokenizer.ts`** -> AI Confidence: **99.31%**
166. **`src/vs/editor/common/model/textModel.ts`** -> AI Confidence: **99.31%**
167. **`src/vs/editor/common/model/textModelSearch.ts`** -> AI Confidence: **99.31%**
168. **`src/vs/editor/common/model/textModelTokens.ts`** -> AI Confidence: **99.31%**
169. **`src/vs/editor/common/model/tokens/tokenizationFontDecorationsProvider.ts`** -> AI Confidence: **99.31%**
170. **`src/vs/editor/common/model/tokens/tokenizerSyntaxTokenBackend.ts`** -> AI Confidence: **99.31%**
171. **`src/vs/editor/common/model/tokens/treeSitter/treeSitterTokenizationImpl.ts`** -> AI Confidence: **99.31%**
172. **`src/vs/editor/common/model/tokens/treeSitter/treeSitterTree.ts`** -> AI Confidence: **99.31%**
173. **`src/vs/editor/common/services/getIconClasses.ts`** -> AI Confidence: **99.31%**
174. **`src/vs/editor/common/services/languageFeatureDebounce.ts`** -> AI Confidence: **99.31%**
175. **`src/vs/editor/common/services/languagesAssociations.ts`** -> AI Confidence: **99.31%**
176. **`src/vs/editor/common/services/languagesRegistry.ts`** -> AI Confidence: **99.31%**
177. **`src/vs/editor/common/services/markerDecorationsService.ts`** -> AI Confidence: **99.31%**
178. **`src/vs/editor/common/services/modelService.ts`** -> AI Confidence: **99.31%**
179. **`src/vs/editor/common/services/textResourceConfigurationService.ts`** -> AI Confidence: **99.31%**
180. **`src/vs/editor/common/tokens/contiguousMultilineTokens.ts`** -> AI Confidence: **99.31%**
181. **`src/vs/editor/common/tokens/contiguousTokensStore.ts`** -> AI Confidence: **99.31%**
182. **`src/vs/editor/common/viewLayout/viewLineRenderer.ts`** -> AI Confidence: **99.31%**
183. **`src/vs/editor/common/viewModel/viewModelImpl.ts`** -> AI Confidence: **99.31%**
184. **`src/vs/editor/common/viewModel/viewModelLines.ts`** -> AI Confidence: **99.31%**
185. **`src/vs/editor/contrib/codeAction/browser/codeAction.ts`** -> AI Confidence: **99.31%**
186. **`src/vs/editor/contrib/codeAction/browser/codeActionController.ts`** -> AI Confidence: **99.31%**
187. **`src/vs/editor/contrib/codeAction/browser/codeActionModel.ts`** -> AI Confidence: **99.31%**
188. **`src/vs/editor/contrib/codeAction/browser/lightBulbWidget.ts`** -> AI Confidence: **99.31%**
189. **`src/vs/editor/contrib/codelens/browser/codelens.ts`** -> AI Confidence: **99.31%**
190. **`src/vs/editor/contrib/codelens/browser/codelensWidget.ts`** -> AI Confidence: **99.31%**
191. **`src/vs/editor/contrib/comment/browser/blockCommentCommand.ts`** -> AI Confidence: **99.31%**
192. **`src/vs/editor/contrib/dnd/browser/dnd.ts`** -> AI Confidence: **99.31%**
193. **`src/vs/editor/contrib/documentSymbols/browser/outlineModel.ts`** -> AI Confidence: **99.31%**
194. **`src/vs/editor/contrib/dropOrPasteInto/browser/copyPasteController.ts`** -> AI Confidence: **99.31%**
195. **`src/vs/editor/contrib/editorState/browser/editorState.ts`** -> AI Confidence: **99.31%**
196. **`src/vs/editor/contrib/find/browser/findDecorations.ts`** -> AI Confidence: **99.31%**
197. **`src/vs/editor/contrib/find/browser/findModel.ts`** -> AI Confidence: **99.31%**
198. **`src/vs/editor/contrib/find/browser/findWidget.ts`** -> AI Confidence: **99.31%**
199. **`src/vs/editor/contrib/folding/browser/hiddenRangeModel.ts`** -> AI Confidence: **99.31%**
200. **`src/vs/editor/contrib/folding/browser/indentRangeProvider.ts`** -> AI Confidence: **99.31%**
201. **`src/vs/editor/contrib/folding/browser/syntaxRangeProvider.ts`** -> AI Confidence: **99.31%**
202. **`src/vs/editor/contrib/folding/test/browser/foldingModel.test.ts`** -> AI Confidence: **99.31%**
203. **`src/vs/editor/contrib/gotoError/browser/gotoErrorWidget.ts`** -> AI Confidence: **99.31%**
204. **`src/vs/editor/contrib/gotoError/browser/markerNavigationService.ts`** -> AI Confidence: **99.31%**
205. **`src/vs/editor/contrib/gotoSymbol/browser/peek/referencesController.ts`** -> AI Confidence: **99.31%**
206. **`src/vs/editor/contrib/hover/browser/contentHoverController.ts`** -> AI Confidence: **99.31%**
207. **`src/vs/editor/contrib/hover/browser/contentHoverWidget.ts`** -> AI Confidence: **99.31%**
208. **`src/vs/editor/contrib/indentation/common/indentation.ts`** -> AI Confidence: **99.31%**
209. **`src/vs/editor/contrib/inlayHints/browser/inlayHintsController.ts`** -> AI Confidence: **99.31%**
210. **`src/vs/editor/contrib/inlineCompletions/browser/controller/inlineCompletionsController.ts`** -> AI Confidence: **99.31%**
211. **`src/vs/editor/contrib/inlineCompletions/browser/model/computeGhostText.ts`** -> AI Confidence: **99.31%**
212. **`src/vs/editor/contrib/inlineCompletions/browser/model/inlineCompletionsModel.ts`** -> AI Confidence: **99.31%**
213. **`src/vs/editor/contrib/inlineCompletions/browser/model/inlineCompletionsSource.ts`** -> AI Confidence: **99.31%**
214. **`src/vs/editor/contrib/inlineCompletions/browser/model/provideInlineCompletions.ts`** -> AI Confidence: **99.31%**
215. **`src/vs/editor/contrib/inlineCompletions/browser/view/ghostText/ghostTextView.ts`** -> AI Confidence: **99.31%**
216. **`src/vs/editor/contrib/inlineCompletions/browser/view/inlineEdits/inlineEditsNewUsers.ts`** -> AI Confidence: **99.31%**
217. **`src/vs/editor/contrib/inlineCompletions/browser/view/inlineEdits/inlineEditsView.ts`** -> AI Confidence: **99.31%**
218. **`src/vs/editor/contrib/inlineCompletions/browser/view/inlineEdits/inlineEditsViews/originalEditorInlineDiffView.ts`** -> AI Confidence: **99.31%**
219. **`src/vs/editor/contrib/linesOperations/browser/linesOperations.ts`** -> AI Confidence: **99.31%**
220. **`src/vs/editor/contrib/linesOperations/browser/moveLinesCommand.ts`** -> AI Confidence: **99.31%**
221. **`src/vs/editor/contrib/linesOperations/test/browser/moveLinesCommand.test.ts`** -> AI Confidence: **99.31%**
222. **`src/vs/editor/contrib/links/browser/links.ts`** -> AI Confidence: **99.31%**
223. **`src/vs/editor/contrib/parameterHints/browser/parameterHintsWidget.ts`** -> AI Confidence: **99.31%**
224. **`src/vs/editor/contrib/quickAccess/browser/gotoSymbolQuickAccess.ts`** -> AI Confidence: **99.31%**
225. **`src/vs/editor/contrib/semanticTokens/browser/documentSemanticTokens.ts`** -> AI Confidence: **99.31%**
226. **`src/vs/editor/contrib/snippet/browser/snippetController2.ts`** -> AI Confidence: **99.31%**
227. **`src/vs/editor/contrib/snippet/browser/snippetSession.ts`** -> AI Confidence: **99.31%**
228. **`src/vs/editor/contrib/snippet/browser/snippetVariables.ts`** -> AI Confidence: **99.31%**
229. **`src/vs/editor/contrib/stickyScroll/browser/stickyScrollController.ts`** -> AI Confidence: **99.31%**
230. **`src/vs/editor/contrib/stickyScroll/browser/stickyScrollWidget.ts`** -> AI Confidence: **99.31%**
231. **`src/vs/editor/contrib/suggest/browser/completionModel.ts`** -> AI Confidence: **99.31%**
232. **`src/vs/editor/contrib/suggest/browser/suggest.ts`** -> AI Confidence: **99.31%**
233. **`src/vs/editor/contrib/suggest/browser/suggestController.ts`** -> AI Confidence: **99.31%**
234. **`src/vs/editor/contrib/suggest/browser/suggestInlineCompletions.ts`** -> AI Confidence: **99.31%**
235. **`src/vs/editor/contrib/suggest/browser/suggestModel.ts`** -> AI Confidence: **99.31%**
236. **`src/vs/editor/contrib/suggest/browser/suggestWidget.ts`** -> AI Confidence: **99.31%**
237. **`src/vs/editor/contrib/suggest/browser/suggestWidgetDetails.ts`** -> AI Confidence: **99.31%**
238. **`src/vs/editor/contrib/suggest/browser/suggestWidgetRenderer.ts`** -> AI Confidence: **99.31%**
239. **`src/vs/editor/contrib/zoneWidget/browser/zoneWidget.ts`** -> AI Confidence: **99.31%**
240. **`src/vs/editor/standalone/common/monarch/monarchLexer.ts`** -> AI Confidence: **99.31%**
241. **`src/vs/editor/test/browser/config/testConfiguration.ts`** -> AI Confidence: **99.31%**
242. **`src/vs/platform/actionWidget/browser/actionList.ts`** -> AI Confidence: **99.31%**
243. **`src/vs/platform/actionWidget/browser/actionWidget.ts`** -> AI Confidence: **99.31%**
244. **`src/vs/platform/actionWidget/browser/actionWidgetDropdown.ts`** -> AI Confidence: **99.31%**
245. **`src/vs/platform/actions/browser/buttonbar.ts`** -> AI Confidence: **99.31%**
246. **`src/vs/platform/actions/browser/dropdownWithPrimaryActionViewItem.ts`** -> AI Confidence: **99.31%**
247. **`src/vs/platform/actions/browser/menuEntryActionViewItem.ts`** -> AI Confidence: **99.31%**
248. **`src/vs/platform/actions/browser/toolbar.ts`** -> AI Confidence: **99.31%**
249. **`src/vs/platform/actions/common/actions.ts`** -> AI Confidence: **99.31%**
250. **`src/vs/platform/actions/common/menuService.ts`** -> AI Confidence: **99.31%**
251. **`src/vs/platform/agentHost/common/state/sessionClientState.ts`** -> AI Confidence: **99.31%**
252. **`src/vs/platform/agentHost/electron-browser/remoteAgentHostServiceImpl.ts`** -> AI Confidence: **99.31%**
253. **`src/vs/platform/agentHost/node/agentHostServerMain.ts`** -> AI Confidence: **99.31%**
254. **`src/vs/platform/agentHost/node/agentService.ts`** -> AI Confidence: **99.31%**
255. **`src/vs/platform/agentHost/node/agentSideEffects.ts`** -> AI Confidence: **99.31%**
256. **`src/vs/platform/agentHost/node/commandAutoApprover.ts`** -> AI Confidence: **99.31%**
257. **`src/vs/platform/agentHost/node/copilot/copilotAgentSession.ts`** -> AI Confidence: **99.31%**
258. **`src/vs/platform/agentHost/node/copilot/copilotPluginConverters.ts`** -> AI Confidence: **99.31%**
259. **`src/vs/platform/agentHost/node/nodeAgentHostStarter.ts`** -> AI Confidence: **99.31%**
260. **`src/vs/platform/agentHost/node/protocolServerHandler.ts`** -> AI Confidence: **99.31%**
261. **`src/vs/platform/agentHost/node/sshRemoteAgentHostService.ts`** -> AI Confidence: **99.31%**
262. **`src/vs/platform/agentPlugins/common/pluginParsers.ts`** -> AI Confidence: **99.31%**
263. **`src/vs/platform/browserElements/electron-main/nativeBrowserElementsMainService.ts`** -> AI Confidence: **99.31%**
264. **`src/vs/platform/configuration/common/configuration.ts`** -> AI Confidence: **99.31%**
265. **`src/vs/platform/configuration/common/configurationModels.ts`** -> AI Confidence: **99.31%**
266. **`src/vs/platform/configuration/common/configurationRegistry.ts`** -> AI Confidence: **99.31%**
267. **`src/vs/platform/configuration/common/configurationService.ts`** -> AI Confidence: **99.31%**
268. **`src/vs/platform/dialogs/common/dialogs.ts`** -> AI Confidence: **99.31%**
269. **`src/vs/platform/dialogs/electron-main/dialogMainService.ts`** -> AI Confidence: **99.31%**
270. **`src/vs/platform/dnd/browser/dnd.ts`** -> AI Confidence: **99.31%**
271. **`src/vs/platform/extensionManagement/common/allowedExtensionsService.ts`** -> AI Confidence: **99.31%**
272. **`src/vs/platform/extensionManagement/common/extensionManagementCLI.ts`** -> AI Confidence: **99.31%**
273. **`src/vs/platform/extensionManagement/common/extensionStorage.ts`** -> AI Confidence: **99.31%**
274. **`src/vs/platform/extensionManagement/common/extensionsProfileScannerService.ts`** -> AI Confidence: **99.31%**
275. **`src/vs/platform/extensionManagement/common/unsupportedExtensionsMigration.ts`** -> AI Confidence: **99.31%**
276. **`src/vs/platform/extensionManagement/node/extensionManagementService.ts`** -> AI Confidence: **99.31%**
277. **`src/vs/platform/extensionManagement/node/extensionsWatcher.ts`** -> AI Confidence: **99.31%**
278. **`src/vs/platform/extensionManagement/test/common/extensionNls.test.ts`** -> AI Confidence: **99.31%**
279. **`src/vs/platform/extensions/common/extensionValidator.ts`** -> AI Confidence: **99.31%**
280. **`src/vs/platform/extensions/common/extensions.ts`** -> AI Confidence: **99.31%**
281. **`src/vs/platform/files/browser/htmlFileSystemProvider.ts`** -> AI Confidence: **99.31%**
282. **`src/vs/platform/files/node/watcher/baseWatcher.ts`** -> AI Confidence: **99.31%**
283. **`src/vs/platform/files/node/watcher/nodejs/nodejsWatcherLib.ts`** -> AI Confidence: **99.31%**
284. **`src/vs/platform/files/node/watcher/parcel/parcelWatcher.ts`** -> AI Confidence: **99.31%**
285. **`src/vs/platform/hover/browser/hoverWidget.ts`** -> AI Confidence: **99.31%**
286. **`src/vs/platform/hover/browser/updatableHoverWidget.ts`** -> AI Confidence: **99.31%**
287. **`src/vs/platform/instantiation/common/instantiationService.ts`** -> AI Confidence: **99.31%**
288. **`src/vs/platform/keybinding/common/abstractKeybindingService.ts`** -> AI Confidence: **99.31%**
289. **`src/vs/platform/keybinding/common/keybindingsRegistry.ts`** -> AI Confidence: **99.31%**
290. **`src/vs/platform/launch/electron-main/launchMainService.ts`** -> AI Confidence: **99.31%**
291. **`src/vs/platform/mcp/common/mcpGalleryService.ts`** -> AI Confidence: **99.31%**
292. **`src/vs/platform/mcp/common/mcpManagementService.ts`** -> AI Confidence: **99.31%**
293. **`src/vs/platform/mcp/common/mcpResourceScannerService.ts`** -> AI Confidence: **99.31%**
294. **`src/vs/platform/mcp/node/mcpGatewayService.ts`** -> AI Confidence: **99.31%**
295. **`src/vs/platform/mcp/node/mcpGatewaySession.ts`** -> AI Confidence: **99.31%**
296. **`src/vs/platform/menubar/electron-main/menubar.ts`** -> AI Confidence: **99.31%**
297. **`src/vs/platform/native/common/native.ts`** -> AI Confidence: **99.31%**
298. **`src/vs/platform/native/electron-main/auth.ts`** -> AI Confidence: **99.31%**
299. **`src/vs/platform/native/electron-main/nativeHostMainService.ts`** -> AI Confidence: **99.31%**
300. **`src/vs/platform/opener/browser/link.ts`** -> AI Confidence: **99.31%**
301. **`src/vs/platform/profiling/electron-browser/profileAnalysisWorker.ts`** -> AI Confidence: **99.31%**
302. **`src/vs/platform/quickinput/browser/commandsQuickAccess.ts`** -> AI Confidence: **99.31%**
303. **`src/vs/platform/quickinput/browser/quickAccess.ts`** -> AI Confidence: **99.31%**
304. **`src/vs/platform/quickinput/browser/quickInput.ts`** -> AI Confidence: **99.31%**
305. **`src/vs/platform/quickinput/browser/quickInputActions.ts`** -> AI Confidence: **99.31%**
306. **`src/vs/platform/quickinput/browser/quickInputController.ts`** -> AI Confidence: **99.31%**
307. **`src/vs/platform/quickinput/browser/quickInputList.ts`** -> AI Confidence: **99.31%**
308. **`src/vs/platform/quickinput/browser/tree/quickInputTreeController.ts`** -> AI Confidence: **99.31%**
309. **`src/vs/platform/remoteTunnel/node/remoteTunnelService.ts`** -> AI Confidence: **99.31%**
310. **`src/vs/platform/shell/node/shellEnv.ts`** -> AI Confidence: **99.31%**
311. **`src/vs/platform/storage/common/storage.ts`** -> AI Confidence: **99.31%**
312. **`src/vs/platform/storage/electron-main/storageIpc.ts`** -> AI Confidence: **99.31%**
313. **`src/vs/platform/telemetry/common/telemetryService.ts`** -> AI Confidence: **99.31%**
314. **`src/vs/platform/terminal/common/capabilities/commandDetection/promptInputModel.ts`** -> AI Confidence: **99.31%**
315. **`src/vs/platform/terminal/common/capabilities/commandDetectionCapability.ts`** -> AI Confidence: **99.31%**
316. **`src/vs/platform/terminal/node/terminalEnvironment.ts`** -> AI Confidence: **99.31%**
317. **`src/vs/platform/terminal/node/terminalProcess.ts`** -> AI Confidence: **99.31%**
318. **`src/vs/platform/terminal/node/terminalProfiles.ts`** -> AI Confidence: **99.31%**
319. **`src/vs/platform/terminal/node/windowsShellHelper.ts`** -> AI Confidence: **99.31%**
320. **`src/vs/platform/theme/electron-main/themeMainServiceImpl.ts`** -> AI Confidence: **99.31%**
321. **`src/vs/platform/undoRedo/common/undoRedoService.ts`** -> AI Confidence: **99.31%**
322. **`src/vs/platform/userDataProfile/common/userDataProfile.ts`** -> AI Confidence: **99.31%**
323. **`src/vs/platform/userDataSync/common/abstractJsonSynchronizer.ts`** -> AI Confidence: **99.31%**
324. **`src/vs/platform/userDataSync/common/abstractSynchronizer.ts`** -> AI Confidence: **99.31%**
325. **`src/vs/platform/userDataSync/common/extensionsSync.ts`** -> AI Confidence: **99.31%**
326. **`src/vs/platform/userDataSync/common/globalStateSync.ts`** -> AI Confidence: **99.31%**
327. **`src/vs/platform/userDataSync/common/keybindingsMerge.ts`** -> AI Confidence: **99.31%**
328. **`src/vs/platform/userDataSync/common/keybindingsSync.ts`** -> AI Confidence: **99.31%**
329. **`src/vs/platform/userDataSync/common/promptsSync/promptsSync.ts`** -> AI Confidence: **99.31%**
330. **`src/vs/platform/userDataSync/common/settingsMerge.ts`** -> AI Confidence: **99.31%**
331. **`src/vs/platform/userDataSync/common/snippetsSync.ts`** -> AI Confidence: **99.31%**
332. **`src/vs/platform/userDataSync/common/userDataAutoSyncService.ts`** -> AI Confidence: **99.31%**
333. **`src/vs/platform/userDataSync/common/userDataProfilesManifestSync.ts`** -> AI Confidence: **99.31%**
334. **`src/vs/platform/userDataSync/common/userDataSyncLocalStoreService.ts`** -> AI Confidence: **99.31%**
335. **`src/vs/platform/userDataSync/common/userDataSyncResourceProvider.ts`** -> AI Confidence: **99.31%**
336. **`src/vs/platform/userDataSync/common/userDataSyncService.ts`** -> AI Confidence: **99.31%**
337. **`src/vs/platform/userDataSync/common/userDataSyncStoreService.ts`** -> AI Confidence: **99.31%**
338. **`src/vs/platform/utilityProcess/electron-main/utilityProcess.ts`** -> AI Confidence: **99.31%**
339. **`src/vs/platform/webContentExtractor/electron-main/webPageLoader.ts`** -> AI Confidence: **99.31%**
340. **`src/vs/platform/webview/electron-main/webviewMainService.ts`** -> AI Confidence: **99.31%**
341. **`src/vs/platform/windows/electron-main/windowImpl.ts`** -> AI Confidence: **99.31%**
342. **`src/vs/platform/windows/electron-main/windows.ts`** -> AI Confidence: **99.31%**
343. **`src/vs/platform/windows/electron-main/windowsMainService.ts`** -> AI Confidence: **99.31%**
344. **`src/vs/platform/windows/electron-main/windowsStateHandler.ts`** -> AI Confidence: **99.31%**
345. **`src/vs/platform/workspaces/common/workspaces.ts`** -> AI Confidence: **99.31%**
346. **`src/vs/platform/workspaces/electron-main/workspacesHistoryMainService.ts`** -> AI Confidence: **99.31%**
347. **`src/vs/platform/workspaces/test/node/workspacesHistoryStorage.test.ts`** -> AI Confidence: **99.31%**
348. **`src/vs/server/node/remoteExtensionHostAgentServer.ts`** -> AI Confidence: **99.31%**
349. **`src/vs/server/node/server.cli.ts`** -> AI Confidence: **99.31%**
350. **`src/vs/server/node/serverEnvironmentService.ts`** -> AI Confidence: **99.31%**
351. **`src/vs/sessions/browser/workbench.ts`** -> AI Confidence: **99.31%**
352. **`src/vs/sessions/contrib/agentFeedback/browser/agentFeedbackEditorUtils.ts`** -> AI Confidence: **99.31%**
353. **`src/vs/sessions/contrib/agentFeedback/browser/agentFeedbackEditorWidgetContribution.ts`** -> AI Confidence: **99.31%**
354. **`src/vs/sessions/contrib/chat/browser/aiCustomizationWorkspaceService.ts`** -> AI Confidence: **99.31%**
355. **`src/vs/sessions/contrib/chat/browser/newChatViewPane.ts`** -> AI Confidence: **99.31%**
356. **`src/vs/sessions/contrib/chat/browser/runScriptAction.ts`** -> AI Confidence: **99.31%**
357. **`src/vs/sessions/contrib/chat/browser/runScriptCustomTaskWidget.ts`** -> AI Confidence: **99.31%**
358. **`src/vs/sessions/contrib/chat/browser/sessionWorkspacePicker.ts`** -> AI Confidence: **99.31%**
359. **`src/vs/sessions/contrib/chat/browser/sessionsConfigurationService.ts`** -> AI Confidence: **99.31%**
360. **`src/vs/sessions/contrib/chat/browser/syncIndicator.ts`** -> AI Confidence: **99.31%**
361. **`src/vs/sessions/contrib/codeReview/browser/codeReview.contributions.ts`** -> AI Confidence: **99.31%**
362. **`src/vs/sessions/contrib/codeReview/browser/codeReviewService.ts`** -> AI Confidence: **99.31%**
363. **`src/vs/sessions/contrib/copilotChatSessions/browser/branchPicker.ts`** -> AI Confidence: **99.31%**
364. **`src/vs/sessions/contrib/copilotChatSessions/browser/copilotChatSessionsProvider.ts`** -> AI Confidence: **99.31%**
365. **`src/vs/sessions/contrib/copilotChatSessions/browser/isolationPicker.ts`** -> AI Confidence: **99.31%**
366. **`src/vs/sessions/contrib/copilotChatSessions/browser/modePicker.ts`** -> AI Confidence: **99.31%**
367. **`src/vs/sessions/contrib/remoteAgentHost/browser/remoteAgentHostActions.ts`** -> AI Confidence: **99.31%**
368. **`src/vs/sessions/contrib/remoteAgentHost/browser/remoteAgentHostSessionsProvider.ts`** -> AI Confidence: **99.31%**
369. **`src/vs/sessions/contrib/sessions/browser/views/sessionsList.ts`** -> AI Confidence: **99.31%**
370. **`src/vs/sessions/contrib/terminal/browser/sessionsTerminalContribution.ts`** -> AI Confidence: **99.31%**
371. **`src/vs/sessions/services/configuration/browser/configurationService.ts`** -> AI Confidence: **99.31%**
372. **`src/vs/workbench/api/browser/mainThreadChatAgents2.ts`** -> AI Confidence: **99.31%**
373. **`src/vs/workbench/api/browser/mainThreadChatSessions.ts`** -> AI Confidence: **99.31%**
374. **`src/vs/workbench/api/browser/mainThreadConfiguration.ts`** -> AI Confidence: **99.31%**
375. **`src/vs/workbench/api/browser/mainThreadDiagnostics.ts`** -> AI Confidence: **99.31%**
376. **`src/vs/workbench/api/browser/mainThreadEditorTabs.ts`** -> AI Confidence: **99.31%**
377. **`src/vs/workbench/api/browser/mainThreadLanguageModelTools.ts`** -> AI Confidence: **99.31%**
378. **`src/vs/workbench/api/browser/mainThreadNotebookKernels.ts`** -> AI Confidence: **99.31%**
379. **`src/vs/workbench/api/browser/mainThreadQuickOpen.ts`** -> AI Confidence: **99.31%**
380. **`src/vs/workbench/api/browser/mainThreadSCM.ts`** -> AI Confidence: **99.31%**
381. **`src/vs/workbench/api/browser/mainThreadTask.ts`** -> AI Confidence: **99.31%**
382. **`src/vs/workbench/api/common/configurationExtensionPoint.ts`** -> AI Confidence: **99.31%**
383. **`src/vs/workbench/api/common/extHostChatAgents2.ts`** -> AI Confidence: **99.31%**
384. **`src/vs/workbench/api/common/extHostChatContext.ts`** -> AI Confidence: **99.31%**
385. **`src/vs/workbench/api/common/extHostChatDebug.ts`** -> AI Confidence: **99.31%**
386. **`src/vs/workbench/api/common/extHostChatSessions.ts`** -> AI Confidence: **99.31%**
387. **`src/vs/workbench/api/common/extHostComments.ts`** -> AI Confidence: **99.31%**
388. **`src/vs/workbench/api/common/extHostConfiguration.ts`** -> AI Confidence: **99.31%**
389. **`src/vs/workbench/api/common/extHostDiagnostics.ts`** -> AI Confidence: **99.31%**
390. **`src/vs/workbench/api/common/extHostFileSystem.ts`** -> AI Confidence: **99.31%**
391. **`src/vs/workbench/api/common/extHostFileSystemConsumer.ts`** -> AI Confidence: **99.31%**
392. **`src/vs/workbench/api/common/extHostFileSystemEventService.ts`** -> AI Confidence: **99.31%**
393. **`src/vs/workbench/api/common/extHostLanguageModelTools.ts`** -> AI Confidence: **99.31%**
394. **`src/vs/workbench/api/common/extHostLocalizationService.ts`** -> AI Confidence: **99.31%**
395. **`src/vs/workbench/api/common/extHostMcp.ts`** -> AI Confidence: **99.31%**
396. **`src/vs/workbench/api/common/extHostNotebook.ts`** -> AI Confidence: **99.31%**
397. **`src/vs/workbench/api/common/extHostNotebookDocument.ts`** -> AI Confidence: **99.31%**
398. **`src/vs/workbench/api/common/extHostQuickOpen.ts`** -> AI Confidence: **99.31%**
399. **`src/vs/workbench/api/common/extHostSCM.ts`** -> AI Confidence: **99.31%**
400. **`src/vs/workbench/api/common/extHostStatusBar.ts`** -> AI Confidence: **99.31%**
401. **`src/vs/workbench/api/common/extHostTelemetry.ts`** -> AI Confidence: **99.31%**
402. **`src/vs/workbench/api/common/extHostTerminalService.ts`** -> AI Confidence: **99.31%**
403. **`src/vs/workbench/api/common/extHostTerminalShellIntegration.ts`** -> AI Confidence: **99.31%**
404. **`src/vs/workbench/api/common/extHostTextEditor.ts`** -> AI Confidence: **99.31%**
405. **`src/vs/workbench/api/common/extHostTreeViews.ts`** -> AI Confidence: **99.31%**
406. **`src/vs/workbench/api/common/extHostTypes/workspaceEdit.ts`** -> AI Confidence: **99.31%**
407. **`src/vs/workbench/api/common/extHostWorkspace.ts`** -> AI Confidence: **99.31%**
408. **`src/vs/workbench/api/node/extHostCLIServer.ts`** -> AI Confidence: **99.31%**
409. **`src/vs/workbench/api/node/loopbackServer.ts`** -> AI Confidence: **99.31%**
410. **`src/vs/workbench/api/node/proxyResolver.ts`** -> AI Confidence: **99.31%**
411. **`src/vs/workbench/api/test/common/extHostTypeConverters.test.ts`** -> AI Confidence: **99.31%**
412. **`src/vs/workbench/browser/actions/developerActions.ts`** -> AI Confidence: **99.31%**
413. **`src/vs/workbench/browser/actions/helpActions.ts`** -> AI Confidence: **99.31%**
414. **`src/vs/workbench/browser/actions/navigationActions.ts`** -> AI Confidence: **99.31%**
415. **`src/vs/workbench/browser/actions/windowActions.ts`** -> AI Confidence: **99.31%**
416. **`src/vs/workbench/browser/actions/workspaceCommands.ts`** -> AI Confidence: **99.31%**
417. **`src/vs/workbench/browser/layout.ts`** -> AI Confidence: **99.31%**
418. **`src/vs/workbench/browser/panecomposite.ts`** -> AI Confidence: **99.31%**
419. **`src/vs/workbench/browser/parts/activitybar/activitybarPart.ts`** -> AI Confidence: **99.31%**
420. **`src/vs/workbench/browser/parts/compositeBar.ts`** -> AI Confidence: **99.31%**
421. **`src/vs/workbench/browser/parts/compositeBarActions.ts`** -> AI Confidence: **99.31%**
422. **`src/vs/workbench/browser/parts/compositePart.ts`** -> AI Confidence: **99.31%**
423. **`src/vs/workbench/browser/parts/editor/breadcrumbsModel.ts`** -> AI Confidence: **99.31%**
424. **`src/vs/workbench/browser/parts/editor/diffEditorCommands.ts`** -> AI Confidence: **99.31%**
425. **`src/vs/workbench/browser/parts/editor/editor.ts`** -> AI Confidence: **99.31%**
426. **`src/vs/workbench/browser/parts/editor/editorAutoSave.ts`** -> AI Confidence: **99.31%**
427. **`src/vs/workbench/browser/parts/editor/editorCommands.ts`** -> AI Confidence: **99.31%**
428. **`src/vs/workbench/browser/parts/editor/editorCommandsContext.ts`** -> AI Confidence: **99.31%**
429. **`src/vs/workbench/browser/parts/editor/editorDropTarget.ts`** -> AI Confidence: **99.31%**
430. **`src/vs/workbench/browser/parts/editor/editorGroupWatermark.ts`** -> AI Confidence: **99.31%**
431. **`src/vs/workbench/browser/parts/editor/editorPane.ts`** -> AI Confidence: **99.31%**
432. **`src/vs/workbench/browser/parts/editor/editorPanes.ts`** -> AI Confidence: **99.31%**
433. **`src/vs/workbench/browser/parts/editor/editorPart.ts`** -> AI Confidence: **99.31%**
434. **`src/vs/workbench/browser/parts/editor/editorParts.ts`** -> AI Confidence: **99.31%**
435. **`src/vs/workbench/browser/parts/editor/editorStatus.ts`** -> AI Confidence: **99.31%**
436. **`src/vs/workbench/browser/parts/editor/editorsObserver.ts`** -> AI Confidence: **99.31%**
437. **`src/vs/workbench/browser/parts/editor/modalEditorPart.ts`** -> AI Confidence: **99.31%**
438. **`src/vs/workbench/browser/parts/editor/sideBySideEditor.ts`** -> AI Confidence: **99.31%**
439. **`src/vs/workbench/browser/parts/editor/singleEditorTabsControl.ts`** -> AI Confidence: **99.31%**
440. **`src/vs/workbench/browser/parts/editor/textDiffEditor.ts`** -> AI Confidence: **99.31%**
441. **`src/vs/workbench/browser/parts/notifications/notificationsCenter.ts`** -> AI Confidence: **99.31%**
442. **`src/vs/workbench/browser/parts/notifications/notificationsStatus.ts`** -> AI Confidence: **99.31%**
443. **`src/vs/workbench/browser/parts/notifications/notificationsToasts.ts`** -> AI Confidence: **99.31%**
444. **`src/vs/workbench/browser/parts/notifications/notificationsViewer.ts`** -> AI Confidence: **99.31%**
445. **`src/vs/workbench/browser/parts/paneCompositeBar.ts`** -> AI Confidence: **99.31%**
446. **`src/vs/workbench/browser/parts/paneCompositePart.ts`** -> AI Confidence: **99.31%**
447. **`src/vs/workbench/browser/parts/titlebar/menubarControl.ts`** -> AI Confidence: **99.31%**
448. **`src/vs/workbench/browser/parts/titlebar/titlebarPart.ts`** -> AI Confidence: **99.31%**
449. **`src/vs/workbench/browser/parts/titlebar/windowTitle.ts`** -> AI Confidence: **99.31%**
450. **`src/vs/workbench/browser/parts/views/treeView.ts`** -> AI Confidence: **99.31%**
451. **`src/vs/workbench/browser/parts/views/viewPane.ts`** -> AI Confidence: **99.31%**
452. **`src/vs/workbench/browser/parts/views/viewPaneContainer.ts`** -> AI Confidence: **99.31%**
453. **`src/vs/workbench/browser/window.ts`** -> AI Confidence: **99.31%**
454. **`src/vs/workbench/browser/workbench.contribution.ts`** -> AI Confidence: **99.31%**
455. **`src/vs/workbench/common/contributions.ts`** -> AI Confidence: **99.31%**
456. **`src/vs/workbench/common/editor/diffEditorInput.ts`** -> AI Confidence: **99.31%**
457. **`src/vs/workbench/common/editor/editorGroupModel.ts`** -> AI Confidence: **99.31%**
458. **`src/vs/workbench/common/editor/resourceEditorInput.ts`** -> AI Confidence: **99.31%**
459. **`src/vs/workbench/common/editor/sideBySideEditorInput.ts`** -> AI Confidence: **99.31%**
460. **`src/vs/workbench/common/editor/textEditorModel.ts`** -> AI Confidence: **99.31%**
461. **`src/vs/workbench/common/notifications.ts`** -> AI Confidence: **99.31%**
462. **`src/vs/workbench/common/resources.ts`** -> AI Confidence: **99.31%**
463. **`src/vs/workbench/common/views.ts`** -> AI Confidence: **99.31%**
464. **`src/vs/workbench/contrib/accessibility/browser/accessibleView.ts`** -> AI Confidence: **99.31%**
465. **`src/vs/workbench/contrib/browserView/common/browserZoomService.ts`** -> AI Confidence: **99.31%**
466. **`src/vs/workbench/contrib/bulkEdit/browser/bulkEditService.ts`** -> AI Confidence: **99.31%**
467. **`src/vs/workbench/contrib/bulkEdit/browser/bulkTextEdits.ts`** -> AI Confidence: **99.31%**
468. **`src/vs/workbench/contrib/bulkEdit/browser/conflicts.ts`** -> AI Confidence: **99.31%**
469. **`src/vs/workbench/contrib/bulkEdit/browser/preview/bulkEditTree.ts`** -> AI Confidence: **99.31%**
470. **`src/vs/workbench/contrib/chat/browser/accessibility/chatAccessibilityProvider.ts`** -> AI Confidence: **99.31%**
471. **`src/vs/workbench/contrib/chat/browser/accessibility/chatResponseAccessibleView.ts`** -> AI Confidence: **99.31%**
472. **`src/vs/workbench/contrib/chat/browser/actions/chatCodeblockActions.ts`** -> AI Confidence: **99.31%**
473. **`src/vs/workbench/contrib/chat/browser/actions/chatCopyActions.ts`** -> AI Confidence: **99.31%**
474. **`src/vs/workbench/contrib/chat/browser/actions/chatToolPicker.ts`** -> AI Confidence: **99.31%**
475. **`src/vs/workbench/contrib/chat/browser/actions/codeBlockOperations.ts`** -> AI Confidence: **99.31%**
476. **`src/vs/workbench/contrib/chat/browser/actions/createPluginAction.ts`** -> AI Confidence: **99.31%**
477. **`src/vs/workbench/contrib/chat/browser/agentPluginRepositoryService.ts`** -> AI Confidence: **99.31%**
478. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentHost/agentHostSessionHandler.ts`** -> AI Confidence: **99.31%**
479. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionApprovalModel.ts`** -> AI Confidence: **99.31%**
480. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionHoverWidget.ts`** -> AI Confidence: **99.31%**
481. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessions.ts`** -> AI Confidence: **99.31%**
482. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsControl.ts`** -> AI Confidence: **99.31%**
483. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsFilter.ts`** -> AI Confidence: **99.31%**
484. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsModel.ts`** -> AI Confidence: **99.31%**
485. **`src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsViewer.ts`** -> AI Confidence: **99.31%**
486. **`src/vs/workbench/contrib/chat/browser/agentSessions/experiments/agentTitleBarStatusWidget.ts`** -> AI Confidence: **99.31%**
487. **`src/vs/workbench/contrib/chat/browser/agentSessions/experiments/unifiedQuickAccess.ts`** -> AI Confidence: **99.31%**
488. **`src/vs/workbench/contrib/chat/browser/aiCustomization/aiCustomizationDebugPanel.ts`** -> AI Confidence: **99.31%**
489. **`src/vs/workbench/contrib/chat/browser/aiCustomization/aiCustomizationListWidget.ts`** -> AI Confidence: **99.31%**
490. **`src/vs/workbench/contrib/chat/browser/aiCustomization/mcpListWidget.ts`** -> AI Confidence: **99.31%**
491. **`src/vs/workbench/contrib/chat/browser/attachments/chatAttachmentModel.ts`** -> AI Confidence: **99.31%**
492. **`src/vs/workbench/contrib/chat/browser/attachments/chatAttachmentWidgets.ts`** -> AI Confidence: **99.31%**
493. **`src/vs/workbench/contrib/chat/browser/attachments/implicitContextAttachment.ts`** -> AI Confidence: **99.31%**
494. **`src/vs/workbench/contrib/chat/browser/chat.ts`** -> AI Confidence: **99.31%**
495. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatCustomizationDiscoveryRenderer.ts`** -> AI Confidence: **99.31%**
496. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugEditor.ts`** -> AI Confidence: **99.31%**
497. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugHomeView.ts`** -> AI Confidence: **99.31%**
498. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugHookContentRenderer.ts`** -> AI Confidence: **99.31%**
499. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugLogsView.ts`** -> AI Confidence: **99.31%**
500. **`src/vs/workbench/contrib/chat/browser/chatDebug/chatDebugToolCallContentRenderer.ts`** -> AI Confidence: **99.31%**
501. **`src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingActions.ts`** -> AI Confidence: **99.31%**
502. **`src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingCodeEditorIntegration.ts`** -> AI Confidence: **99.31%**
503. **`src/vs/workbench/contrib/chat/browser/chatEditing/chatEditingExplanationWidget.ts`** -> AI Confidence: **99.31%**
504. **`src/vs/workbench/contrib/chat/browser/chatEditing/notebook/chatEditingModifiedNotebookSnapshot.ts`** -> AI Confidence: **99.31%**
505. **`src/vs/workbench/contrib/chat/browser/chatEditing/notebook/chatEditingNotebookEditorIntegration.ts`** -> AI Confidence: **99.31%**
506. **`src/vs/workbench/contrib/chat/browser/chatManagement/chatManagementEditor.ts`** -> AI Confidence: **99.31%**
507. **`src/vs/workbench/contrib/chat/browser/chatManagement/chatModelsViewModel.ts`** -> AI Confidence: **99.31%**
508. **`src/vs/workbench/contrib/chat/browser/chatManagement/chatUsageWidget.ts`** -> AI Confidence: **99.31%**
509. **`src/vs/workbench/contrib/chat/browser/chatParticipant.contribution.ts`** -> AI Confidence: **99.31%**
510. **`src/vs/workbench/contrib/chat/browser/chatRepoInfo.ts`** -> AI Confidence: **99.31%**
511. **`src/vs/workbench/contrib/chat/browser/chatSessions/chatSessionPickerActionItem.ts`** -> AI Confidence: **99.31%**
512. **`src/vs/workbench/contrib/chat/browser/chatSetup/chatSetupController.ts`** -> AI Confidence: **99.31%**
513. **`src/vs/workbench/contrib/chat/browser/chatSetup/chatSetupRunner.ts`** -> AI Confidence: **99.31%**
514. **`src/vs/workbench/contrib/chat/browser/chatStatus/chatStatusDashboard.ts`** -> AI Confidence: **99.31%**
515. **`src/vs/workbench/contrib/chat/browser/chatStatus/chatStatusEntry.ts`** -> AI Confidence: **99.31%**
516. **`src/vs/workbench/contrib/chat/browser/chatTipEligibilityTracker.ts`** -> AI Confidence: **99.31%**
517. **`src/vs/workbench/contrib/chat/browser/chatTipService.ts`** -> AI Confidence: **99.31%**
518. **`src/vs/workbench/contrib/chat/browser/chatWindowNotifier.ts`** -> AI Confidence: **99.31%**
519. **`src/vs/workbench/contrib/chat/browser/contextContrib/chatContext.contribution.ts`** -> AI Confidence: **99.31%**
520. **`src/vs/workbench/contrib/chat/browser/contextContrib/chatContextService.ts`** -> AI Confidence: **99.31%**
521. **`src/vs/workbench/contrib/chat/browser/defaultModelContribution.ts`** -> AI Confidence: **99.31%**
522. **`src/vs/workbench/contrib/chat/browser/pluginInstallService.ts`** -> AI Confidence: **99.31%**
523. **`src/vs/workbench/contrib/chat/browser/pluginSources.ts`** -> AI Confidence: **99.31%**
524. **`src/vs/workbench/contrib/chat/browser/promptSyntax/hookUtils.ts`** -> AI Confidence: **99.31%**
525. **`src/vs/workbench/contrib/chat/browser/tools/languageModelToolsConfirmationService.ts`** -> AI Confidence: **99.31%**
526. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatHookContentPart.ts`** -> AI Confidence: **99.31%**
527. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatMarkdownDecorationsRenderer.ts`** -> AI Confidence: **99.31%**
528. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatQuestionCarouselPart.ts`** -> AI Confidence: **99.31%**
529. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatReferencesContentPart.ts`** -> AI Confidence: **99.31%**
530. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/chatSuggestNextWidget.ts`** -> AI Confidence: **99.31%**
531. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/chatMcpAppModel.ts`** -> AI Confidence: **99.31%**
532. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/chatTerminalToolConfirmationSubPart.ts`** -> AI Confidence: **99.31%**
533. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/chatTerminalToolProgressPart.ts`** -> AI Confidence: **99.31%**
534. **`src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/chatToolInvocationPart.ts`** -> AI Confidence: **99.31%**
535. **`src/vs/workbench/contrib/chat/browser/widget/chatListWidget.ts`** -> AI Confidence: **99.31%**
536. **`src/vs/workbench/contrib/chat/browser/widget/chatWidget.ts`** -> AI Confidence: **99.31%**
537. **`src/vs/workbench/contrib/chat/browser/widget/chatWidgetService.ts`** -> AI Confidence: **99.31%**
538. **`src/vs/workbench/contrib/chat/browser/widget/input/chatInputPart.ts`** -> AI Confidence: **99.31%**
539. **`src/vs/workbench/contrib/chat/browser/widget/input/chatModelPicker.ts`** -> AI Confidence: **99.31%**
540. **`src/vs/workbench/contrib/chat/browser/widget/input/chatSelectedTools.ts`** -> AI Confidence: **99.31%**
541. **`src/vs/workbench/contrib/chat/browser/widget/input/editor/chatInputCompletions.ts`** -> AI Confidence: **99.31%**
542. **`src/vs/workbench/contrib/chat/browser/widgetHosts/chatQuick.ts`** -> AI Confidence: **99.31%**
543. **`src/vs/workbench/contrib/chat/browser/widgetHosts/viewPane/chatContextUsageWidget.ts`** -> AI Confidence: **99.31%**
544. **`src/vs/workbench/contrib/chat/browser/widgetHosts/viewPane/chatViewPane.ts`** -> AI Confidence: **99.31%**
545. **`src/vs/workbench/contrib/chat/common/chatArtifactExtraction.ts`** -> AI Confidence: **99.31%**
546. **`src/vs/workbench/contrib/chat/common/chatDebugServiceImpl.ts`** -> AI Confidence: **99.31%**
547. **`src/vs/workbench/contrib/chat/common/chatImageExtraction.ts`** -> AI Confidence: **99.31%**
548. **`src/vs/workbench/contrib/chat/common/chatModes.ts`** -> AI Confidence: **99.31%**
549. **`src/vs/workbench/contrib/chat/common/chatService/chatServiceTelemetry.ts`** -> AI Confidence: **99.31%**
550. **`src/vs/workbench/contrib/chat/common/languageModels.ts`** -> AI Confidence: **99.31%**
551. **`src/vs/workbench/contrib/chat/common/model/chatProgressTypes/chatToolInvocation.ts`** -> AI Confidence: **99.31%**
552. **`src/vs/workbench/contrib/chat/common/model/chatSessionStore.ts`** -> AI Confidence: **99.31%**
553. **`src/vs/workbench/contrib/chat/common/participants/chatAgents.ts`** -> AI Confidence: **99.31%**
554. **`src/vs/workbench/contrib/chat/common/plugins/pluginMarketplaceService.ts`** -> AI Confidence: **99.31%**
555. **`src/vs/workbench/contrib/chat/common/plugins/workspacePluginSettingsService.ts`** -> AI Confidence: **99.31%**
556. **`src/vs/workbench/contrib/chat/common/promptSyntax/computeAutomaticInstructions.ts`** -> AI Confidence: **99.31%**
557. **`src/vs/workbench/contrib/chat/common/promptSyntax/hookSchema.ts`** -> AI Confidence: **99.31%**
558. **`src/vs/workbench/contrib/chat/common/promptSyntax/languageProviders/promptHeaderAutocompletion.ts`** -> AI Confidence: **99.31%**
559. **`src/vs/workbench/contrib/chat/common/promptSyntax/languageProviders/promptValidator.ts`** -> AI Confidence: **99.31%**
560. **`src/vs/workbench/contrib/chat/common/promptSyntax/promptFileParser.ts`** -> AI Confidence: **99.31%**
561. **`src/vs/workbench/contrib/chat/common/promptSyntax/utils/promptFilesLocator.ts`** -> AI Confidence: **99.31%**
562. **`src/vs/workbench/contrib/chat/common/requestParser/chatRequestParser.ts`** -> AI Confidence: **99.31%**
563. **`src/vs/workbench/contrib/chat/common/tools/builtinTools/chatUrlFetchingConfirmation.ts`** -> AI Confidence: **99.31%**
564. **`src/vs/workbench/contrib/chat/common/tools/builtinTools/runSubagentTool.ts`** -> AI Confidence: **99.31%**
565. **`src/vs/workbench/contrib/chat/common/voiceChatService.ts`** -> AI Confidence: **99.31%**
566. **`src/vs/workbench/contrib/chat/common/widget/annotations.ts`** -> AI Confidence: **99.31%**
567. **`src/vs/workbench/contrib/chat/common/widget/chatWidgetHistoryService.ts`** -> AI Confidence: **99.31%**
568. **`src/vs/workbench/contrib/chat/electron-browser/actions/voiceChatActions.ts`** -> AI Confidence: **99.31%**
569. **`src/vs/workbench/contrib/chat/test/browser/widget/chatContentParts/chatInlineAnchorWidget.test.ts`** -> AI Confidence: **99.31%**
570. **`src/vs/workbench/contrib/chat/test/browser/widget/chatContentParts/chatSubagentContentPart.test.ts`** -> AI Confidence: **99.31%**
571. **`src/vs/workbench/contrib/chat/test/browser/widget/chatContentParts/chatTodoListWidget.test.ts`** -> AI Confidence: **99.31%**
572. **`src/vs/workbench/contrib/codeEditor/browser/editorFindAccessibilityHelp.ts`** -> AI Confidence: **99.31%**
573. **`src/vs/workbench/contrib/codeEditor/browser/find/simpleFindWidget.ts`** -> AI Confidence: **99.31%**
574. **`src/vs/workbench/contrib/codeEditor/browser/inspectEditorTokens/inspectEditorTokens.ts`** -> AI Confidence: **99.31%**
575. **`src/vs/workbench/contrib/codeEditor/browser/outline/documentSymbolsOutline.ts`** -> AI Confidence: **99.31%**
576. **`src/vs/workbench/contrib/codeEditor/common/languageConfigurationExtensionPoint.ts`** -> AI Confidence: **99.31%**
577. **`src/vs/workbench/contrib/comments/browser/commentFormActions.ts`** -> AI Confidence: **99.31%**
578. **`src/vs/workbench/contrib/comments/browser/commentGlyphWidget.ts`** -> AI Confidence: **99.31%**
579. **`src/vs/workbench/contrib/comments/browser/commentReply.ts`** -> AI Confidence: **99.31%**
580. **`src/vs/workbench/contrib/comments/browser/commentService.ts`** -> AI Confidence: **99.31%**
581. **`src/vs/workbench/contrib/comments/browser/commentThreadBody.ts`** -> AI Confidence: **99.31%**
582. **`src/vs/workbench/contrib/comments/browser/commentThreadWidget.ts`** -> AI Confidence: **99.31%**
583. **`src/vs/workbench/contrib/comments/browser/commentThreadZoneWidget.ts`** -> AI Confidence: **99.31%**
584. **`src/vs/workbench/contrib/comments/browser/commentsController.ts`** -> AI Confidence: **99.31%**
585. **`src/vs/workbench/contrib/comments/browser/commentsModel.ts`** -> AI Confidence: **99.31%**
586. **`src/vs/workbench/contrib/comments/browser/commentsView.ts`** -> AI Confidence: **99.31%**
587. **`src/vs/workbench/contrib/editTelemetry/browser/telemetry/editSourceTrackingImpl.ts`** -> AI Confidence: **99.31%**
588. **`src/vs/workbench/contrib/extensions/browser/abstractRuntimeExtensionsEditor.ts`** -> AI Confidence: **99.31%**
589. **`src/vs/workbench/contrib/extensions/browser/extensionFeaturesTab.ts`** -> AI Confidence: **99.31%**
590. **`src/vs/workbench/contrib/extensions/browser/extensionsViews.ts`** -> AI Confidence: **99.31%**
591. **`src/vs/workbench/contrib/extensions/browser/extensionsWidgets.ts`** -> AI Confidence: **99.31%**
592. **`src/vs/workbench/contrib/extensions/browser/extensionsWorkbenchService.ts`** -> AI Confidence: **99.31%**
593. **`src/vs/workbench/contrib/files/browser/explorerService.ts`** -> AI Confidence: **99.31%**
594. **`src/vs/workbench/contrib/files/browser/files.ts`** -> AI Confidence: **99.31%**
595. **`src/vs/workbench/contrib/files/browser/views/explorerViewer.ts`** -> AI Confidence: **99.31%**
596. **`src/vs/workbench/contrib/files/browser/workspaceWatcher.ts`** -> AI Confidence: **99.31%**
597. **`src/vs/workbench/contrib/format/browser/formatActionsMultiple.ts`** -> AI Confidence: **99.31%**
598. **`src/vs/workbench/contrib/imageCarousel/browser/imageCarouselEditor.ts`** -> AI Confidence: **99.31%**
599. **`src/vs/workbench/contrib/inlineChat/browser/inlineChatNotebook.ts`** -> AI Confidence: **99.31%**
600. **`src/vs/workbench/contrib/inlineChat/browser/inlineChatWidget.ts`** -> AI Confidence: **99.31%**
601. **`src/vs/workbench/contrib/interactive/browser/interactive.contribution.ts`** -> AI Confidence: **99.31%**
602. **`src/vs/workbench/contrib/issue/browser/baseIssueReporterService.ts`** -> AI Confidence: **99.31%**
603. **`src/vs/workbench/contrib/languageDetection/browser/languageDetection.contribution.ts`** -> AI Confidence: **99.31%**
604. **`src/vs/workbench/contrib/localization/electron-browser/localization.contribution.ts`** -> AI Confidence: **99.31%**
605. **`src/vs/workbench/contrib/markdown/browser/markdownDocumentRenderer.ts`** -> AI Confidence: **99.31%**
606. **`src/vs/workbench/contrib/markers/browser/markersFileDecorations.ts`** -> AI Confidence: **99.31%**
607. **`src/vs/workbench/contrib/markers/browser/markersFilterOptions.ts`** -> AI Confidence: **99.31%**
608. **`src/vs/workbench/contrib/markers/browser/markersTable.ts`** -> AI Confidence: **99.31%**
609. **`src/vs/workbench/contrib/markers/browser/markersView.ts`** -> AI Confidence: **99.31%**
610. **`src/vs/workbench/contrib/mcp/browser/mcpCommandsAddConfiguration.ts`** -> AI Confidence: **99.31%**
611. **`src/vs/workbench/contrib/mcp/browser/mcpElicitationService.ts`** -> AI Confidence: **99.31%**
612. **`src/vs/workbench/contrib/mcp/browser/mcpLanguageFeatures.ts`** -> AI Confidence: **99.31%**
613. **`src/vs/workbench/contrib/mcp/browser/mcpResourceQuickAccess.ts`** -> AI Confidence: **99.31%**
614. **`src/vs/workbench/contrib/mcp/browser/mcpWorkbenchService.ts`** -> AI Confidence: **99.31%**
615. **`src/vs/workbench/contrib/mcp/common/discovery/installedMcpServersDiscovery.ts`** -> AI Confidence: **99.31%**
616. **`src/vs/workbench/contrib/mcp/common/mcpServerConnection.ts`** -> AI Confidence: **99.31%**
617. **`src/vs/workbench/contrib/mcp/common/mcpTaskManager.ts`** -> AI Confidence: **99.31%**
618. **`src/vs/workbench/contrib/mergeEditor/browser/model/textModelDiffs.ts`** -> AI Confidence: **99.31%**
619. **`src/vs/workbench/contrib/mergeEditor/browser/view/editors/baseCodeEditorView.ts`** -> AI Confidence: **99.31%**
620. **`src/vs/workbench/contrib/mergeEditor/browser/view/editors/inputCodeEditorView.ts`** -> AI Confidence: **99.31%**
621. **`src/vs/workbench/contrib/mergeEditor/browser/view/scrollSynchronizer.ts`** -> AI Confidence: **99.31%**
622. **`src/vs/workbench/contrib/mergeEditor/browser/view/viewZones.ts`** -> AI Confidence: **99.31%**
623. **`src/vs/workbench/contrib/notebook/browser/contrib/cellDiagnostics/cellDiagnosticEditorContrib.ts`** -> AI Confidence: **99.31%**
624. **`src/vs/workbench/contrib/notebook/browser/contrib/cellStatusBar/executionStatusBarItemController.ts`** -> AI Confidence: **99.31%**
625. **`src/vs/workbench/contrib/notebook/browser/contrib/editorStatusBar/editorStatusBar.ts`** -> AI Confidence: **99.31%**
626. **`src/vs/workbench/contrib/notebook/browser/contrib/execute/executionEditorProgress.ts`** -> AI Confidence: **99.31%**
627. **`src/vs/workbench/contrib/notebook/browser/contrib/find/findModel.ts`** -> AI Confidence: **99.31%**
628. **`src/vs/workbench/contrib/notebook/browser/contrib/find/notebookFindWidget.ts`** -> AI Confidence: **99.31%**
629. **`src/vs/workbench/contrib/notebook/browser/contrib/notebookVariables/notebookInlineVariables.ts`** -> AI Confidence: **99.31%**
630. **`src/vs/workbench/contrib/notebook/browser/contrib/outline/notebookOutline.ts`** -> AI Confidence: **99.31%**
631. **`src/vs/workbench/contrib/notebook/browser/contrib/undoRedo/notebookUndoRedo.ts`** -> AI Confidence: **99.31%**
632. **`src/vs/workbench/contrib/notebook/browser/contrib/viewportWarmup/viewportWarmup.ts`** -> AI Confidence: **99.31%**
633. **`src/vs/workbench/contrib/notebook/browser/controller/cellOperations.ts`** -> AI Confidence: **99.31%**
634. **`src/vs/workbench/contrib/notebook/browser/controller/executeActions.ts`** -> AI Confidence: **99.31%**
635. **`src/vs/workbench/contrib/notebook/browser/controller/foldingController.ts`** -> AI Confidence: **99.31%**
636. **`src/vs/workbench/contrib/notebook/browser/diff/diffComponents.ts`** -> AI Confidence: **99.31%**
637. **`src/vs/workbench/contrib/notebook/browser/diff/diffElementViewModel.ts`** -> AI Confidence: **99.31%**
638. **`src/vs/workbench/contrib/notebook/browser/diff/notebookDiffEditor.ts`** -> AI Confidence: **99.31%**
639. **`src/vs/workbench/contrib/notebook/browser/diff/notebookDiffOverviewRuler.ts`** -> AI Confidence: **99.31%**
640. **`src/vs/workbench/contrib/notebook/browser/diff/notebookMultiDiffEditor.ts`** -> AI Confidence: **99.31%**
641. **`src/vs/workbench/contrib/notebook/browser/notebookCellLayoutManager.ts`** -> AI Confidence: **99.31%**
642. **`src/vs/workbench/contrib/notebook/browser/notebookEditor.ts`** -> AI Confidence: **99.31%**
643. **`src/vs/workbench/contrib/notebook/browser/services/notebookEditorServiceImpl.ts`** -> AI Confidence: **99.31%**
644. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellActionView.ts`** -> AI Confidence: **99.31%**
645. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellContextKeys.ts`** -> AI Confidence: **99.31%**
646. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellDnd.ts`** -> AI Confidence: **99.31%**
647. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellEditorOptions.ts`** -> AI Confidence: **99.31%**
648. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellExecution.ts`** -> AI Confidence: **99.31%**
649. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/cellProgressBar.ts`** -> AI Confidence: **99.31%**
650. **`src/vs/workbench/contrib/notebook/browser/view/cellParts/codeCell.ts`** -> AI Confidence: **99.31%**
651. **`src/vs/workbench/contrib/notebook/browser/view/notebookCellList.ts`** -> AI Confidence: **99.31%**
652. **`src/vs/workbench/contrib/notebook/browser/view/renderers/backLayerWebView.ts`** -> AI Confidence: **99.31%**
653. **`src/vs/workbench/contrib/notebook/browser/view/renderers/webviewPreloads.ts`** -> AI Confidence: **99.31%**
654. **`src/vs/workbench/contrib/notebook/browser/viewModel/OutlineEntry.ts`** -> AI Confidence: **99.31%**
655. **`src/vs/workbench/contrib/notebook/browser/viewModel/codeCellViewModel.ts`** -> AI Confidence: **99.31%**
656. **`src/vs/workbench/contrib/notebook/browser/viewModel/foldingModel.ts`** -> AI Confidence: **99.31%**
657. **`src/vs/workbench/contrib/notebook/browser/viewParts/notebookEditorToolbar.ts`** -> AI Confidence: **99.31%**
658. **`src/vs/workbench/contrib/notebook/browser/viewParts/notebookEditorWidgetContextKeys.ts`** -> AI Confidence: **99.31%**
659. **`src/vs/workbench/contrib/notebook/common/model/notebookCellTextModel.ts`** -> AI Confidence: **99.31%**
660. **`src/vs/workbench/contrib/notebook/common/notebookEditorModelResolverServiceImpl.ts`** -> AI Confidence: **99.31%**
661. **`src/vs/workbench/contrib/notebook/test/browser/diff/notebookDiffService.test.ts`** -> AI Confidence: **99.31%**
662. **`src/vs/workbench/contrib/output/browser/outputView.ts`** -> AI Confidence: **99.31%**
663. **`src/vs/workbench/contrib/output/test/browser/outputChannelModel.test.ts`** -> AI Confidence: **99.31%**
664. **`src/vs/workbench/contrib/performance/electron-browser/startupTimings.ts`** -> AI Confidence: **99.31%**
665. **`src/vs/workbench/contrib/preferences/browser/preferencesActions.ts`** -> AI Confidence: **99.31%**
666. **`src/vs/workbench/contrib/preferences/browser/settingsEditorSettingIndicators.ts`** -> AI Confidence: **99.31%**
667. **`src/vs/workbench/contrib/preferences/browser/settingsTreeModels.ts`** -> AI Confidence: **99.31%**
668. **`src/vs/workbench/contrib/relauncher/browser/relauncher.contribution.ts`** -> AI Confidence: **99.31%**
669. **`src/vs/workbench/contrib/remote/browser/explorerViewItems.ts`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `src/vs/platform/terminal/test/node/terminalEnvironment.test.ts` -> **99.9462%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `31` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4376` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/vs/workbench/contrib/webview/browser/overlayWebview.ts` (TYPESCRIPT) -> Cumulative Risk: **799.27**
- **Archetype:** `file_cluster_4` (Distance: 15.487 IQR)
- **Magnitude:** 79.83 | **LOC:** 440 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.9861%)
- **Heaviest Functions:** `_show` (Impact: 25.7), `claim` (Impact: 22.1), `doLayoutWebviewOverElement` (Impact: 17.0)

### 2. `src/vs/editor/contrib/inlineCompletions/browser/model/inlineCompletionsSource.ts` (TYPESCRIPT) -> Cumulative Risk: **795.08**
- **Archetype:** `file_cluster_13` (Distance: 14.004 IQR)
- **Magnitude:** 111.34 | **LOC:** 740 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 60.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Cognitive Load (99.1996%), Concurrency (98.8566%)
- **Heaviest Functions:** `fetch` (Impact: 225.8), `promise` (Impact: 148.2), `_sendInlineCompletionsRequestTelemetry` (Impact: 38.0)

### 3. `src/vs/editor/contrib/inlineCompletions/browser/model/provideInlineCompletions.ts` (TYPESCRIPT) -> Cumulative Risk: **793.67**
- **Archetype:** `file_cluster_13` (Distance: 13.508 IQR)
- **Magnitude:** 86.04 | **LOC:** 689 | **CtrlFlow:** 50.2% | **Authorship Centralization:** 73.3%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Cognitive Load (98.4533%)
- **Heaviest Functions:** `onUnexpectedExternalError` (Impact: 91.6), `provideInlineCompletions` (Impact: 90.4), `toInlineSuggestData` (Impact: 87.5)

### 4. `src/vs/workbench/api/common/extHostStatusBar.ts` (TYPESCRIPT) -> Cumulative Risk: **793.41**
- **Archetype:** `file_cluster_4` (Distance: 14.119 IQR)
- **Magnitude:** 62.75 | **LOC:** 406 | **CtrlFlow:** 59.4% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%)
- **Heaviest Functions:** `update` (Impact: 32.3), `constructor` (Impact: 31.4), `command` (Impact: 25.2)

### 5. `extensions/typescript-language-features/src/tsServer/versionManager.ts` (TYPESCRIPT) -> Cumulative Risk: **792.18**
- **Archetype:** `file_cluster_4` (Distance: 12.846 IQR)
- **Magnitude:** 38.86 | **LOC:** 218 | **CtrlFlow:** 43.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `run` (Impact: 52.0), `constructor` (Impact: 15.6), `promptUseWorkspaceTsdk` (Impact: 15.2)

### 6. `src/vs/platform/userDataSync/common/userDataSyncAccount.ts` (TYPESCRIPT) -> Cumulative Risk: **791.17**
- **Archetype:** `file_cluster_4` (Distance: 14.007 IQR)
- **Magnitude:** 14.24 | **LOC:** 71 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `updateAccount` (Impact: 22.5), `updateAccount` (Impact: 15.1), `constructor` (Impact: 8.8)

### 7. `src/vs/workbench/contrib/chat/common/model/chatProgressTypes/chatToolInvocation.ts` (TYPESCRIPT) -> Cumulative Risk: **784.55**
- **Archetype:** `file_cluster_4` (Distance: 14.876 IQR)
- **Magnitude:** 52.9 | **LOC:** 342 | **CtrlFlow:** 60.6% | **Authorship Centralization:** 26.7%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.1837%), Tech Debt (99.1165%)
- **Heaviest Functions:** `didExecuteTool` (Impact: 45.4), `transitionFromStreaming` (Impact: 35.1), `_setCompleted` (Impact: 16.6)

### 8. `src/vs/editor/browser/widget/diffEditor/diffEditorViewModel.ts` (TYPESCRIPT) -> Cumulative Risk: **784.42**
- **Archetype:** `file_cluster_17` (Distance: 13.798 IQR)
- **Magnitude:** 89.07 | **LOC:** 772 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9233%)
- **Heaviest Functions:** `constructor` (Impact: 103.8), `updateUnchangedRegions` (Impact: 37.5), `fromDiffs` (Impact: 36.3)

### 9. `src/vs/editor/common/tokenizationRegistry.ts` (TYPESCRIPT) -> Cumulative Risk: **781.86**
- **Archetype:** `file_cluster_4` (Distance: 13.712 IQR)
- **Magnitude:** 24.59 | **LOC:** 153 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `getOrCreate` (Impact: 9.8), `isResolved` (Impact: 8.7), `registerFactory` (Impact: 7.6)

### 10. `src/vs/workbench/services/inlineCompletions/common/inlineCompletionsUnification.ts` (TYPESCRIPT) -> Cumulative Risk: **779.47**
- **Archetype:** `file_cluster_4` (Distance: 13.901 IQR)
- **Magnitude:** 30.22 | **LOC:** 183 | **CtrlFlow:** 34.7% | **Authorship Centralization:** 75.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `constructor` (Impact: 21.8), `_update` (Impact: 21.5), `_isExtensionUnificationActive` (Impact: 17.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/configuration-editing/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/css-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/css-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/debug-auto-launch/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/debug-server-ready/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/emmet/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/extension-editing/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/git-base/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/git/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/github-authentication/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/github/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/grunt/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/gulp/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/html-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/html-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/ipynb/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/jake/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/json-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/json-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/markdown-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/markdown-math/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/media-preview/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.099
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/vs/platform/extensionManagement/test/common/configRemotes.test.ts` (TYPESCRIPT) | Magnitude: 3.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 91, sec_high_risk_execution: 51, io: 39, decorators: 30
- `scripts/xterm-update.js` (JAVASCRIPT) | Magnitude: 66.58 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 70, immutability_locks: 21, branch: 17, concurrency: 14
- `test/mcp/src/automationTools/task.ts` (TYPESCRIPT) | Magnitude: 2.22 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 33, structural_boundaries: 11, safety: 9, immutability_locks: 4
- `src/vs/base/common/layout.ts` (TYPESCRIPT) | Magnitude: 11.2 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 90, branch: 41, structural_boundaries: 34, immutability_locks: 24
- `src/vs/editor/browser/viewParts/minimap/minimapCharSheet.ts` (TYPESCRIPT) | Magnitude: 2.6 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 24, structural_boundaries: 10, state_mutation: 9, api: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_1
- `src/vs/editor/contrib/hover/browser/hoverUtils.ts` (TYPESCRIPT) | Magnitude: 2.4 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 13, branch: 8, doc: 6
- `src/vs/base/common/codicons.ts` (TYPESCRIPT) | Magnitude: 0.87 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 33, dependency_injection: 31, structural_boundaries: 12, api: 6
- `src/vs/base/parts/sandbox/node/electronTypes.ts` (TYPESCRIPT) | Magnitude: 1.57 | Delta: **0.152 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 23, args: 20, func_start: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/vs/base/common/linkedList.ts` (TYPESCRIPT) | Magnitude: 20.1 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 119, indent_tabs: 111, branch: 22, structural_boundaries: 18
- `src/vs/workbench/contrib/terminalContrib/chatAgentTools/test/electron-browser/treeSitterCommandParser.test.ts` (TYPESCRIPT) | Magnitude: 147.65 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 261, branch: 247, structural_boundaries: 239, args: 220
- `src/vs/base/browser/ui/tree/indexTreeModel.ts` (TYPESCRIPT) | Magnitude: 69.65 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 531, state_mutation: 312, branch: 151, structural_boundaries: 88
- `src/vs/base/common/fuzzyScorer.ts` (TYPESCRIPT) | Magnitude: 98.68 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 393, branch: 164, structural_boundaries: 95, immutability_locks: 94
- `src/vs/workbench/services/extensionManagement/test/browser/extensionEnablementService.test.ts` (TYPESCRIPT) | Magnitude: 125.62 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1011, concurrency: 512, structural_boundaries: 403, args: 203

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `resources/server/bin/helpers/check-requirements-linux.sh` (SHELL) | Magnitude: 238.4 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 113, state_mutation: 109, indent_spaces: 78, io: 48
- `scripts/node-electron.sh` (SHELL) | Magnitude: 6.24 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 24, branch: 23, indent_tabs: 15, safety_bypasses: 6
- `scripts/test-documentation.sh` (SHELL) | Magnitude: 2.84 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 12, branch: 9, safety_bypasses: 5, indent_tabs: 5
- `test/sanity/scripts/run-macOS.sh` (SHELL) | Magnitude: 0.67 | Delta: **0.248 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: reflection_metaprogramming: 6, debug_prints: 6, args: 4, structural_boundaries: 3
- `src/vs/base/node/ps.sh` (SHELL) | Magnitude: 38.46 | Delta: **0.293 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 18, branch: 15, safety_bypasses: 14, state_mutation: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/vs/base/browser/ui/splitview/paneview.ts` (TYPESCRIPT) | Magnitude: 111.12 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: state_mutation: 770, indent_tabs: 481, structural_boundaries: 109, branch: 104
- `src/vs/workbench/contrib/files/electron-browser/fileCommands.ts` (TYPESCRIPT) | Magnitude: 3.93 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 30, structural_boundaries: 13, branch: 12, import: 6
- `src/vs/workbench/contrib/imageCarousel/browser/imageCarouselTypes.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 13, immutability_locks: 12, structural_boundaries: 10, api: 5
- `src/vs/workbench/contrib/notebook/browser/contrib/troubleshoot/layout.ts` (TYPESCRIPT) | Magnitude: 38.57 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 314, state_mutation: 218, structural_boundaries: 53, args: 47
- `src/vs/platform/remote/common/managedSocket.ts` (TYPESCRIPT) | Magnitude: 13.85 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 93, state_mutation: 51, structural_boundaries: 30, args: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/vs/base/test/common/testUtils.ts` (TYPESCRIPT) | Magnitude: 1.07 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 6, indent_tabs: 6, api: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/vs/editor/browser/gpu/objectCollectionBuffer.ts` (TYPESCRIPT) | Magnitude: 19.32 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 133, indent_tabs: 120, structural_boundaries: 38, immutability_locks: 28
- `src/vscode-dts/vscode.proposed.chatPromptFiles.d.ts` (TYPESCRIPT) | Magnitude: 3.25 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 44, indent_tabs: 31, structural_boundaries: 24, api: 16
- `src/vs/base/browser/ui/tree/objectTree.ts` (TYPESCRIPT) | Magnitude: 24.99 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 197, generics: 90, state_mutation: 81, structural_boundaries: 67
- `src/vs/platform/mcp/common/mcpGateway.ts` (TYPESCRIPT) | Magnitude: 2.75 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 27, immutability_locks: 26, structural_boundaries: 22, doc: 18
- `src/vs/workbench/common/panecomposite.ts` (TYPESCRIPT) | Magnitude: 4.46 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, args: 3, func_start: 3, indent_tabs: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/vs/workbench/contrib/terminalContrib/links/test/browser/linkTestUtils.ts` (TYPESCRIPT) | Magnitude: 1.99 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 32, structural_boundaries: 19, args: 7, state_mutation: 6
- `src/vs/workbench/services/authentication/browser/authenticationExtensionsService.ts` (TYPESCRIPT) | Magnitude: 32.06 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 210, state_mutation: 159, structural_boundaries: 55, immutability_locks: 41
- `src/vs/platform/userDataSync/common/keybindingsMerge.ts` (TYPESCRIPT) | Magnitude: 22.67 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 245, branch: 102, state_mutation: 89, structural_boundaries: 74
- `src/vs/workbench/contrib/notebook/browser/view/renderers/webviewPreloads.ts` (TYPESCRIPT) | Magnitude: 206.59 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 1366, branch: 368, state_mutation: 312, structural_boundaries: 240
- `src/vs/workbench/api/common/extHostTypes/snippetString.ts` (TYPESCRIPT) | Magnitude: 11.54 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 71, state_mutation: 58, structural_boundaries: 15, branch: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `extensions/terminal-suggest/src/fig/fig-autocomplete-shared/specMetadata.ts` (TYPESCRIPT) | Magnitude: 5.82 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 69, structural_boundaries: 32, generics: 21, branch: 20
- `src/vs/editor/test/node/diffing/fixtures/ws-alignment/1.tsx` (TYPESCRIPT) | Magnitude: 0.37 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 5, ui_framework: 4, generics: 4
- `src/vs/platform/defaultAccount/common/defaultAccount.ts` (TYPESCRIPT) | Magnitude: 2.18 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 22, immutability_locks: 15, ui_framework: 12, generics: 12
- `src/vscode-dts/vscode.proposed.taskProblemMatcherStatus.d.ts` (TYPESCRIPT) | Magnitude: 2.03 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 10, api: 5, doc: 5
- `src/vscode-dts/vscode.proposed.fileSearchProvider.d.ts` (TYPESCRIPT) | Magnitude: 0.66 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: doc: 10, structural_boundaries: 9, indent_tabs: 7, api: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/vs/workbench/contrib/search/browser/symbolsQuickAccess.ts` (TYPESCRIPT) | Magnitude: 21.59 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 209, branch: 78, state_mutation: 77, concurrency: 59
- `src/vs/workbench/contrib/notebook/browser/controller/coreActions.ts` (TYPESCRIPT) | Magnitude: 32.57 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 233, structural_boundaries: 95, branch: 74, state_mutation: 54
- `src/vs/code/node/cliProcessMain.ts` (TYPESCRIPT) | Magnitude: 39.55 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 185, state_mutation: 151, structural_boundaries: 108, concurrency: 98
- `src/vs/workbench/contrib/workspace/browser/workspaceTrustEditor.ts` (TYPESCRIPT) | Magnitude: 126.49 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 849, state_mutation: 551, structural_boundaries: 182, branch: 157
- `extensions/typescript-language-features/src/test/smoke/completions.test.ts` (TYPESCRIPT) | Magnitude: 49.81 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 525, concurrency: 355, structural_boundaries: 181, func_start: 98

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/vs/editor/browser/viewParts/viewLines/viewLines.css` (CSS) | Magnitude: 0.76 | Delta: **0.339 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 6, class_start: 5, args: 2, immutability_locks: 2
- `src/vscode-dts/vscode.proposed.authProviderSpecific.d.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.624 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 4, indent_tabs: 3, doc: 2, planned_debt: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/vs/workbench/contrib/testing/common/testId.ts` (TYPESCRIPT) | Magnitude: 24.29 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 139, state_mutation: 96, structural_boundaries: 38, api: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `extensions/php-language-features/src/features/utils/markedTextUtil.ts` (TYPESCRIPT) | Magnitude: 0.42 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1
- `extensions/terminal-suggest/src/completions/git.ts` (TYPESCRIPT) | Magnitude: 3.14 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 21, branch: 13, immutability_locks: 11
- `src/vs/platform/accessibility/browser/accessibleView.ts` (TYPESCRIPT) | Magnitude: 10.09 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 123, structural_boundaries: 59, branch: 42, api: 39
- `src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/alternativeRecommendation.ts` (TYPESCRIPT) | Magnitude: 2.73 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 44, branch: 13, structural_boundaries: 12, state_mutation: 7
- `src/vs/workbench/contrib/testing/test/common/testProfileService.test.ts` (TYPESCRIPT) | Magnitude: 5.99 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 92, args: 38, func_start: 35, structural_boundaries: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/vscode-dts/vscode.proposed.codiconDecoration.d.ts` (TYPESCRIPT) | Magnitude: 11.88 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: doc: 9, branch: 7, indent_tabs: 7, structural_boundaries: 4
- `resources/server/bin-dev/remote-cli/code.sh` (SHELL) | Magnitude: 43.18 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 21, branch: 11, io: 4, args: 3
- `resources/server/bin/code-server-linux.sh` (SHELL) | Magnitude: 20.96 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 12, indent_tabs: 6, safety_bypasses: 4, args: 3
- `resources/linux/bin/code.sh` (SHELL) | Magnitude: 92.12 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 39, indent_tabs: 32, state_mutation: 27, io: 13
- `resources/server/bin/helpers/browser-linux.sh` (SHELL) | Magnitude: 8.16 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 6, args: 1, safety: 1, reflection_metaprogramming: 1

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vs/workbench/contrib/chat/browser/chat.contribution.ts` -> Churn: **100.0%** | Cog Load: 15.8689% | Debt: 97.7972%
- `src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsViewer.ts` -> Churn: **91.52%** | Cog Load: 86.3086% | Debt: 97.0876%
- `src/vs/workbench/contrib/chat/browser/widget/input/chatInputPart.ts` -> Churn: **90.48%** | Cog Load: 87.6943% | Debt: 94.24%
- `src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/runInTerminalTool.ts` -> Churn: **86.44%** | Cog Load: 91.5172% | Debt: 27.8%
- `src/vs/workbench/contrib/chat/browser/widget/chatWidget.ts` -> Churn: **84.35%** | Cog Load: 100.0% | Debt: 23.6923%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `cli/src/tunnels/code_server.rs` -> **Josh Spicer** (100.0% isolated ownership) | Magnitude: 459.16
- `cli/src/commands/serve_web.rs` -> **Dan Plischke** (100.0% isolated ownership) | Magnitude: 353.12
- `resources/linux/snap/electron-launch` -> **Robo** (100.0% isolated ownership) | Magnitude: 292.6
- `src/vs/workbench/contrib/userDataProfile/browser/userDataProfilesEditorModel.ts` -> **Sandeep Somavarapu** (100.0% isolated ownership) | Magnitude: 277.39
- `src/vs/platform/agentHost/node/commandAutoApprover.ts` -> **Rob Lourens** (100.0% isolated ownership) | Magnitude: 274.28

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vs/base/common/assert.ts` -> **Severity: 8155.0** (Blast Radius: 81.55 * Doc Risk: 100.0%)
- `src/vs/editor/common/languages/highlights/css.scm` -> **Severity: 710.827** (Blast Radius: 28.26 * Doc Risk: 25.1531%)
- `extensions/typescript-language-features/src/utils/fs.ts` -> **Severity: 710.297** (Blast Radius: 9.619 * Doc Risk: 73.8431%)
- `extensions/typescript-language-features/src/typescriptService.ts` -> **Severity: 223.397** (Blast Radius: 3.254 * Doc Risk: 68.6531%)
- `cli/src/log.rs` -> **Severity: 198.541** (Blast Radius: 2.413 * Doc Risk: 82.2799%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
