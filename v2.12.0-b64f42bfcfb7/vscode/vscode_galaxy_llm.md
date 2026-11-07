# ARCHITECTURAL_BRIEF: vscode
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/vscode.git` |
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
- **Scope:** 8560 analyzed artifact(s), 1905978 LOC.
- **Load-bearing artifact:** `src/vs/base/common/lifecycle.ts` -- 2513 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/vs/sessions/sessions.common.main.ts` -- pulls in 252 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` at magnitude 163297.7 (structural weight, not risk).
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
| Total Artifacts | 10238 |
| Analyzed Artifacts (Scanned) | 8560 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1678 |
| Total LOC | 1905978 |
| Volatility Index | 0.002 |
| % Scanned of codebase = | 83.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.41 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1379 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 10.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.401 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 414 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 6642 | 1664894 | 77.6% |
| JSON | 690 | 152102 | 8.1% |
| CSS | 344 | 38652 | 4.0% |
| PLAINTEXT | 230 | 44 | 2.7% |
| MARKDOWN | 160 | 0 | 1.9% |
| XML | 94 | 425 | 1.1% |
| HTML | 93 | 5796 | 1.1% |
| JAVASCRIPT | 77 | 21932 | 0.9% |
| RUST | 72 | 15022 | 0.8% |
| SHELL | 62 | 2744 | 0.7% |
| YAML | 27 | 1981 | 0.3% |
| BATCH | 20 | 700 | 0.2% |
| POWERSHELL | 10 | 536 | 0.1% |
| DOCKERFILE | 9 | 139 | 0.1% |
| CPP | 6 | 73 | 0.1% |
| PHP | 3 | 43 | 0.0% |
| SCHEME | 3 | 382 | 0.0% |
| GO | 2 | 21 | 0.0% |
| PYTHON | 2 | 65 | 0.0% |
| OBJECTIVE-C | 2 | 66 | 0.0% |
| PERL | 2 | 55 | 0.0% |
| JAVA | 1 | 23 | 0.0% |
| MAKEFILE | 1 | 68 | 0.0% |
| C | 1 | 27 | 0.0% |
| CSHARP | 1 | 27 | 0.0% |
| DART | 1 | 15 | 0.0% |
| FSHARP | 1 | 11 | 0.0% |
| GROOVY | 1 | 106 | 0.0% |
| LUA | 1 | 10 | 0.0% |
| SQLITE | 1 | 6 | 0.0% |
| SWIFT | 1 | 13 | 0.0% |

## 4.1 SOURCE ENCODINGS
> 4 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 8504 |
| unknown | unknown | 43 |
| cp1252 | cp1252-fallback | 3 |
| utf-16-le | bom | 3 |
| utf-16-be | bom | 2 |
| utf-8 | bom | 2 |
| latin-1 | latin-1-fallback | 1 |
| utf-16-be | utf-16-heuristic | 1 |
| utf-16-le | utf-16-heuristic | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Data / Markup / Trivial 20%, Declarative / Non-Code 13%, Large Core Modules (2) 7%, Callbacks & Closures Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 8158 | 95.3% |
| Unknown | 43 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 346 | 4.0% |
| Static: Minified & Vendor Opaque Mass | 13 | 0.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1678*

**Composition by Extension & Reason:**
- `.ts`: 355x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Saturation: Line 26 exceeds 500 chars), 2x Excluded (Saturation: Line 9 exceeds 500 chars)
- `.png`: 321x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 91x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 75x Excluded: Neighborhood Micro-Mass Limit Exceeded, 3x Excluded (Massive Static Asset Blob: 6001 LOC)
- `no_extension`: 145x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 16x Excluded (Unsupported Extension: '.code-snippets'), 7x Unsupported Format (.undeterminable)
- `.snap`: 128x Unsupported Format (.snap), 6x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.tst`: 90x Unsupported Format (.tst)
- `.yml`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ico`: 31x Excluded (Explicitly Denied Extension: '.ico')
- `.mp3`: 31x Excluded (Explicitly Denied Extension: '.mp3')
- `.js`: 16x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 4x Zero-Density Threshold (LOC: 1088, Signals: 0), 3x Zero-Density Threshold (LOC: 1183, Signals: 0)
- `.icns`: 29x Excluded (Unsupported Extension: '.icns')
- `.isl`: 17x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 3x Excluded (Embedded Array/Matrix Payload: 4660 commas in 1136 LOC), 3x Excluded (Binary Format Detected)
- `.css`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 23 exceeds 500 chars), 1x Excluded (Saturation: Line 7 exceeds 500 chars)
- `.bmp`: 14x Excluded (Explicitly Denied Extension: '.bmp')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 32.1 | 16.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.9 | 36.3 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 13.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 15.1 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 16.3 | 4.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 35.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 39.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.9 | 0.6 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 63.8 | 98.1 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 12652 | 2073 | 2 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| cleanup | 7531 | 1926 | 3 | `src/vs/editor/contrib/find/test/browser/findModel.test.ts` |
| guards | 149885 | 5586 | 47 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| danger | 19659 | 2983 | 5 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| concurrency | 82917 | 3712 | 25 | `extensions/git/src/commands.ts` |
| connectivity | 57360 | 5440 | 16 | `src/vscode-dts/vscode.d.ts` |
| io | 17823 | 1841 | 4 | `extensions/terminal-suggest/src/completions/git.ts` |
| crypto | 28 | 27 | 0 | `src/vs/workbench/api/node/proxyResolver.ts` |
| ipc | 422 | 195 | 0 | `src/vs/workbench/contrib/webview/browser/pre/index.html` |
| time | 2395 | 741 | 0 | `src/vs/workbench/contrib/chat/test/browser/agentSessions/agentSessionsDataSource.test.ts` |
| serialization | 2336 | 786 | 0 | `src/vs/base/test/common/oauth.test.ts` |
| regex | 3198 | 1055 | 1 | `src/vs/workbench/services/search/test/node/search.integrationTest.ts` |
| events | 7031 | 1337 | 1 | `extensions/terminal-suggest/src/completions/git.ts` |
| tests | 22486 | 1211 | 5 | `src/vs/base/test/browser/comparers.test.ts` |
| docs | 25503 | 2433 | 5 | `src/vscode-dts/vscode.d.ts` |
| debt | 16999 | 1750 | 2 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| mutation | 354465 | 6346 | 105 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| dead_code | 11259 | 2146 | 3 | `src/vscode-dts/vscode.d.ts` |
| credential | 1728 | 111 | 0 | `test/monaco/package-lock.json` |
| threat | 137 | 63 | 0 | `src/vs/editor/test/common/viewLayout/__snapshots__/renderViewLine2_ws-monospace.0.html` |
| ml_ai | 2828 | 778 | 0 | `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` |
| ui | 5482 | 826 | 0 | `src/vs/workbench/contrib/chat/browser/widget/media/chat.css` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `extensions/terminal-suggest/src/completions/git.ts` (Hits: 374)
- `src/vs/workbench/contrib/notebook/test/browser/diff/notebookDiffService.test.ts` (Hits: 356)
- `src/vs/base/test/common/oauth.test.ts` (Hits: 337)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **lifecycle.ts** (`src/vs/base/common/lifecycle.ts`) — 2513 inbound connections
2. **uri.ts** (`src/vs/base/common/uri.ts`) — 1858 inbound connections
3. **event.ts** (`src/vs/base/common/event.ts`) — 1569 inbound connections
4. **nls.ts** (`src/vs/nls.ts`) — 1534 inbound connections
5. **instantiation.ts** (`src/vs/platform/instantiation/common/instantiation.ts`) — 1481 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **sessions.common.main.ts** (`src/vs/sessions/sessions.common.main.ts`) — 252 outbound dependencies
2. **workbench.common.main.ts** (`src/vs/workbench/workbench.common.main.ts`) — 236 outbound dependencies
3. **workbenchTestServices.ts** (`src/vs/workbench/test/browser/workbenchTestServices.ts`) — 189 outbound dependencies
4. **chat.contribution.ts** (`src/vs/workbench/contrib/chat/browser/chat.contribution.ts`) — 172 outbound dependencies
5. **app.ts** (`src/vs/code/electron-main/app.ts`) — 138 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `checkTypeRelatedTo` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **2839.4** | LOC: 2483
  * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determine which checks are performed and as a cache of p...
- `checkTypeRelatedTo` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **2839.4** | LOC: 2483
  * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determine which checks are performed and as a cache of p...
- `checkTypeRelatedTo` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **2839.4** | LOC: 2483
  * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determine which checks are performed and as a cache of p...
- `_showOutput` **(Many-Argument Workhorses)** (@ `src/vs/workbench/contrib/tasks/browser/abstractTaskService.ts`) -> Impact: **2125.4** | LOC: 3269
- `createNodeBuilder` **(Compute Cores)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1775.2** | LOC: 4604
- `createNodeBuilder` **(Compute Cores)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1775.2** | LOC: 4604
- `createNodeBuilder` **(Compute Cores)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1775.2** | LOC: 4604
- `getFlowTypeOfReference` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1239.1** | LOC: 1217
- `getFlowTypeOfReference` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1239.1** | LOC: 1217
- `getFlowTypeOfReference` **(Many-Argument Workhorses)** (@ `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts`) -> Impact: **1239.1** | LOC: 1217

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `extensions/vscode-colorize-perf-tests/test/colorize-fixtures` | 3 | 165165.04 | 41.33% | 0.0% |
| `src/vs/workbench/api/common` | 113 | 34675.3 | 60.01% | 9.36% |
| `src/vs/base/common` | 105 | 25951.01 | 40.06% | 26.5% |
| `extensions/git/src` | 48 | 18885.84 | 48.79% | 6.27% |
| `src/vs/workbench/browser/parts/editor` | 39 | 14645.74 | 53.25% | 6.48% |
| `src/vs/workbench/api/browser` | 95 | 12435.46 | 55.62% | 4.5% |
| `src/vs/base/test/common` | 75 | 9331.63 | 21.54% | 0.0% |
| `src/vs/platform/userDataSync/test/common` | 19 | 9153.75 | 69.08% | 0.0% |
| `src/vs/platform/userDataSync/common` | 30 | 8809.32 | 69.65% | 12.78% |
| `extensions/vscode-api-tests/src/singlefolder-tests` | 36 | 6757.31 | 34.39% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `extensions/html-language-features/server/lib/jquery.d.ts` -> **100.0%** Exposure
- `extensions/references-view/src/references-view.d.ts` -> **100.0%** Exposure
- `extensions/typescript-language-features/src/commands/reloadProject.ts` -> **100.0%** Exposure
- `src/typings/base-common.d.ts` -> **100.0%** Exposure
- `src/vs/base/browser/ui/hover/hoverDelegateFactory.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `extensions/css-language-features/server/src/languageModelCache.ts` -> **100.0%** Exposure
- `extensions/emmet/src/defaultCompletionProvider.ts` -> **100.0%** Exposure
- `extensions/emmet/src/incrementDecrement.ts` -> **100.0%** Exposure
- `extensions/emmet/src/toggleComment.ts` -> **100.0%** Exposure
- `extensions/extension-editing/src/packageDocumentHelper.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` -> **0** Orphaned Functions | **7167** Duplicates
- `src/vscode-dts/vscode.d.ts` -> **310** Orphaned Functions | **69** Duplicates
- `src/vs/monaco.d.ts` -> **305** Orphaned Functions | **37** Duplicates
- `extensions/html-language-features/server/lib/jquery.d.ts` -> **87** Orphaned Functions | **6** Duplicates
- `src/vs/platform/native/electron-main/nativeHostMainService.ts` -> **87** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `src/vs/sessions/test/e2e/extensions/sessions-e2e-mock/extension.js` -> **99.9986%** Exposure
- `src/vs/platform/terminal/test/node/terminalEnvironment.test.ts` -> **99.9961%** Exposure
- `src/vs/platform/agentHost/test/electron-browser/remoteAgentHostService.test.ts` -> **40.5597%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `20` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4686` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 20.236)
- **Top Global Matches:** file_cluster_6: 20.236, file_cluster_4: 20.262, file_cluster_12: 25.188
- **Magnitude:** 163297.7 | **LOC:** 146621 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.043; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.1%), Complexity Load (formerly Cognitive Load) (36.7%), Concurrency Surface (formerly Concurrency) (12.5%), Connectivity (formerly Api Exposure) (6.9%)
- **Documentation Coverage:** 90.613% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkTypeRelatedTo` **(Many-Argument Workhorses)** (Impact: 2839.4)
    * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determ...
  * `checkTypeRelatedTo` **(Many-Argument Workhorses)** (Impact: 2839.4)
    * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determ...
  * `checkTypeRelatedTo` **(Many-Argument Workhorses)** (Impact: 2839.4)
    * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determ...
  * `createNodeBuilder` **(Compute Cores)** (Impact: 1775.2)
  * `createNodeBuilder` **(Compute Cores)** (Impact: 1775.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 6602 instances
* *Concurrency (weighted view):* 75
* *State Mutation (weighted view):* 21354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49843`, `structural_boundaries: 31253`, `args: 9516`, `func_start: 7169`, `class_start: 85`
* *Risk/State:* `safety_bypasses: 1149`, `high_risk_execution: 3`, `state_mutation: 8150`, `dead_code: 227`, `planned_debt: 176`, `fragile_debt: 55`, `duplicate_logic: 7167`
* *Architecture:* `io: 101`, `api: 119`, `concurrency: 55`, `import: 8`
* *Defense:* `safety: 1308`, `doc: 658`, `immutability_locks: 904`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.043
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.000386
  * `Imports (Out-Degree: 0):` $moduleSpecifier, ), );
                    
                
                if (!specifier) 
                    specifier = getSpecifierForModuleSymbol(chain[0], ts.js, ts.moduleSpecifiers.js, ts.performance.js, :, ])...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/configuration-editing/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/css-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/css-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/debug-auto-launch/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/debug-server-ready/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/emmet/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/extension-editing/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/git-base/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/git/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/github-authentication/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/github/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/grunt/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/gulp/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/html-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/html-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/ipynb/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/jake/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/json-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/json-language-features/server/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/markdown-language-features/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `extensions/markdown-math/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.042
  * `Choke Point (Betweenness):` n/a | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/vs/workbench/services/textfile/common/textFileSaveParticipant.ts` (TYPESCRIPT) | Magnitude: 61.3 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 58, structural_boundaries: 24, branch: 12, import: 10
- `src/vs/workbench/api/common/extHostTypes/diagnostic.ts` (TYPESCRIPT) | Magnitude: 71.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 75, branch: 27, structural_boundaries: 23, state_mutation: 7
- `src/vs/workbench/services/userDataProfile/browser/userDataProfileManagement.ts` (TYPESCRIPT) | Magnitude: 138.6 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 162, structural_boundaries: 74, branch: 42, concurrency: 35
- `src/vs/workbench/contrib/meteredConnection/browser/meteredConnection.contribution.ts` (TYPESCRIPT) | Magnitude: 0.11 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 40, structural_boundaries: 15, import: 8, core_var_decl: 5
- `src/vs/workbench/contrib/accessibility/browser/accessibility.contribution.ts` (TYPESCRIPT) | Magnitude: 0.16 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 16, import: 16, generics: 1, explicit_casts: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `src/vs/workbench/contrib/comments/browser/commentThreadRangeDecorator.ts` (TYPESCRIPT) | Magnitude: 0.78 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 104, structural_boundaries: 27, branch: 23, args: 16
- `src/vs/workbench/contrib/notebook/browser/contrib/find/findMatchDecorationModel.ts` (TYPESCRIPT) | Magnitude: 0.73 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 111, structural_boundaries: 23, args: 15, branch: 10
- `extensions/vscode-colorize-tests/test/colorize-fixtures/test.js` (JAVASCRIPT) | Magnitude: 9.72 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 13, structural_boundaries: 12, core_var_decl: 9, design_snake_case: 9
- `extensions/markdown-language-features/src/client/workspace.ts` (TYPESCRIPT) | Magnitude: 34.56 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 45, structural_boundaries: 21, args: 8, state_mutation: 6
- `src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/chatToolOutputPart.ts` (TYPESCRIPT) | Magnitude: 0.78 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 102, structural_boundaries: 37, import: 19, branch: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/vs/workbench/api/browser/mainThreadEditSessionIdentityParticipant.ts` (TYPESCRIPT) | Magnitude: 18.2 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 19, import: 9, args: 6
- `src/vs/platform/remote/node/wsl.ts` (TYPESCRIPT) | Magnitude: 50.78 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 39, structural_boundaries: 18, branch: 10, concurrency: 8
- `src/vs/workbench/services/extensions/common/remoteExtensionHost.ts` (TYPESCRIPT) | Magnitude: 121.62 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 210, structural_boundaries: 61, immutability_locks: 27, import: 25
- `src/vs/workbench/test/browser/componentFixtures/aiStats.fixture.ts` (TYPESCRIPT) | Magnitude: 34.12 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 56, structural_boundaries: 21, core_var_decl: 17, state_mutation: 12
- `src/vs/workbench/contrib/chat/browser/chatTipCatalog.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 341, structural_boundaries: 45, args: 22, func_start: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/vs/editor/common/viewModelEventDispatcher.ts` (TYPESCRIPT) | Magnitude: 353.96 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 425, structural_boundaries: 111, api: 102, args: 64
- `src/vs/platform/browserView/test/electron-main/browserSessionTrust.test.ts` (TYPESCRIPT) | Magnitude: 75.26 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 242, structural_boundaries: 72, core_var_decl: 48, args: 39
- `src/vs/workbench/contrib/typeHierarchy/browser/typeHierarchyPeek.ts` (TYPESCRIPT) | Magnitude: 2.17 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 315, structural_boundaries: 73, state_mutation: 42, branch: 31
- `src/vs/editor/browser/widget/diffEditor/features/revertButtonsFeature.ts` (TYPESCRIPT) | Magnitude: 76.4 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 120, structural_boundaries: 49, branch: 21, args: 20
- `src/vs/workbench/contrib/notebook/browser/contrib/troubleshoot/layout.ts` (TYPESCRIPT) | Magnitude: 2.02 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 314, state_mutation: 60, structural_boundaries: 57, core_var_decl: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/vs/workbench/contrib/testing/browser/testingViewPaneContainer.ts` (TYPESCRIPT) | Magnitude: 0.15 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 25, structural_boundaries: 20, import: 14, decorators: 11
- `src/vs/platform/userDataProfile/node/userDataProfileStorageService.ts` (TYPESCRIPT) | Magnitude: 3.9 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 8, indent_tabs: 8, import: 5, decorators: 4
- `src/vs/workbench/api/browser/mainThreadAiSettingsSearch.ts` (TYPESCRIPT) | Magnitude: 9.86 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 13, args: 5, import: 4
- `src/vs/server/node/extensionsScannerService.ts` (TYPESCRIPT) | Magnitude: 15.02 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 27, structural_boundaries: 20, import: 12, decorators: 8
- `extensions/vscode-colorize-tests/test/colorize-fixtures/25920.html` (HTML) | Magnitude: 15.26 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 7, design_snake_case: 7, structural_boundaries: 5, indent_tabs: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/vs/base/test/common/sinonUtils.ts` (TYPESCRIPT) | Magnitude: 13.08 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 8, generics: 3, args: 1, safety_bypasses: 1
- `src/vs/workbench/contrib/search/browser/replace.ts` (TYPESCRIPT) | Magnitude: 0.26 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 7, branch: 5, indent_tabs: 5, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/vs/base/common/linkedText.ts` (TYPESCRIPT) | Magnitude: 33.22 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 27, branch: 12, structural_boundaries: 11, state_mutation: 5
- `src/vs/editor/common/model/bracketPairsTextModelPart/bracketPairsTree/beforeEditPositionMapper.ts` (TYPESCRIPT) | Magnitude: 66.34 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 92, structural_boundaries: 23, core_var_decl: 16, design_camel_case: 14
- `src/vs/editor/common/languageFeatureRegistry.ts` (TYPESCRIPT) | Magnitude: 170.5 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 161, structural_boundaries: 50, branch: 46, args: 20
- `extensions/typescript-language-features/src/commands/configurePlugin.ts` (TYPESCRIPT) | Magnitude: 7.72 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 7, structural_boundaries: 6, api: 4, args: 2
- `test/mcp/src/automationTools/index.ts` (TYPESCRIPT) | Magnitude: 27.06 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 42, structural_boundaries: 25, import: 22, state_mutation: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/vs/workbench/api/browser/mainThreadLanguages.ts` (TYPESCRIPT) | Magnitude: 14.44 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 48, structural_boundaries: 25, import: 11, core_var_decl: 7
- `src/vs/workbench/contrib/policyExport/electron-browser/policyExport.contribution.ts` (TYPESCRIPT) | Magnitude: 0.77 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_tabs: 156, structural_boundaries: 55, core_var_decl: 26, branch: 19
- `src/vs/workbench/contrib/terminalContrib/chat/browser/terminalChatService.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 261, structural_boundaries: 64, branch: 53, state_mutation: 40
- `src/vs/base/browser/pixelRatio.ts` (TYPESCRIPT) | Magnitude: 60.48 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 70, structural_boundaries: 25, branch: 22, core_var_decl: 14
- `src/vs/workbench/contrib/languageStatus/browser/languageStatus.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 315, structural_boundaries: 75, branch: 68, core_var_decl: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/vs/workbench/contrib/welcomeViews/common/viewsWelcomeExtensionPoint.ts` (TYPESCRIPT) | Magnitude: 0.21 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 57, structural_boundaries: 19, core_var_decl: 8, immutability_locks: 6
- `src/vs/editor/contrib/inlineCompletions/browser/inlineCompletions.contribution.ts` (TYPESCRIPT) | Magnitude: 0.16 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, import: 10, dependency_injection: 2
- `extensions/typescript-language-features/src/commands/learnMoreAboutRefactorings.ts` (TYPESCRIPT) | Magnitude: 7.66 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 8, structural_boundaries: 6, api: 4, import: 3
- `src/vs/workbench/contrib/chat/browser/widget/chatContentParts/toolInvocationParts/autoApproveMessageWidget.ts` (TYPESCRIPT) | Magnitude: 0.04 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, args: 1, func_start: 1
- `src/vs/editor/contrib/hover/browser/hoverContribution.ts` (TYPESCRIPT) | Magnitude: 0.16 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 17, import: 14, indent_tabs: 7, dependency_injection: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/vs/platform/action/common/actionCommonCategories.ts` (TYPESCRIPT) | Magnitude: 15.68 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_tabs: 6, structural_boundaries: 2, safety: 1, api: 1
- `cli/src/commands.rs` (RUST) | Magnitude: 21.16 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 8, api: 7, import: 1
- `src/vs/workbench/contrib/welcomeGettingStarted/common/media/theme_picker_small.ts` (TYPESCRIPT) | Magnitude: 0.17 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 20, structural_boundaries: 7, core_var_decl: 6, design_snake_case: 6
- `src/vs/workbench/contrib/chat/test/common/promptSyntax/testUtils/mockFilesystem.test.ts` (TYPESCRIPT) | Magnitude: 0.62 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 214, structural_boundaries: 34, concurrency: 15, import: 11
- `src/vs/editor/test/common/model/tokenStore.test.ts` (TYPESCRIPT) | Magnitude: 31.14 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_tabs: 601, core_var_decl: 53, design_snake_case: 52, structural_boundaries: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_3
- `src/vs/workbench/services/preferences/common/preferencesValidation.ts` (TYPESCRIPT) | Magnitude: 341.94 | Delta: **0.242** (centroid distance) | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 327, structural_boundaries: 142, branch: 131, args: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/vs/platform/quickinput/browser/quickInput.ts` (TYPESCRIPT) | Magnitude: 814.76 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 1103, structural_boundaries: 229, branch: 198, args: 163
- `src/vs/workbench/contrib/chat/browser/widget/chatListWidget.ts` (TYPESCRIPT) | Magnitude: 3.78 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 492, structural_boundaries: 130, branch: 101, args: 79
- `src/vs/workbench/contrib/chat/common/tools/chatArtifactsService.ts` (TYPESCRIPT) | Magnitude: 0.17 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 216, structural_boundaries: 66, immutability_locks: 42, core_var_decl: 36
- `src/vs/workbench/contrib/chat/browser/actions/chatToolPicker.ts` (TYPESCRIPT) | Magnitude: 8.49 | Delta: **0.037** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_tabs: 575, branch: 160, structural_boundaries: 131, core_var_decl: 82
- `src/vs/editor/contrib/inlineCompletions/browser/view/inlineEdits/utils/utils.ts` (TYPESCRIPT) | Magnitude: 2.6 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 273, structural_boundaries: 126, core_var_decl: 84, branch: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/vs/workbench/contrib/files/test/browser/editorAutoSave.test.ts` (TYPESCRIPT) | Magnitude: 0.65 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 60, structural_boundaries: 40, import: 21, concurrency: 16
- `src/vs/workbench/api/test/browser/mainThreadManagedSockets.test.ts` (TYPESCRIPT) | Magnitude: 100.04 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 74, structural_boundaries: 47, args: 20, concurrency: 15
- `src/vs/workbench/contrib/search/test/browser/mockSearchTree.ts` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 51, structural_boundaries: 35, args: 28, func_start: 28
- `src/vs/platform/diagnostics/common/diagnostics.ts` (TYPESCRIPT) | Magnitude: 61.06 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 85, structural_boundaries: 54, api: 20, branch: 18
- `src/vs/sessions/contrib/github/test/browser/githubFetchers.test.ts` (TYPESCRIPT) | Magnitude: 2.27 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 348, structural_boundaries: 93, args: 48, concurrency: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionHoverWidget.ts` (TYPESCRIPT) | Magnitude: 1.92 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 217, branch: 57, structural_boundaries: 44, core_var_decl: 40
- `extensions/vscode-colorize-perf-tests/test/colorize-fixtures/test-checker.ts` (TYPESCRIPT) | Magnitude: 163297.7 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 119389, branch: 49843, structural_boundaries: 31253, core_var_decl: 20953
- `src/vs/workbench/services/search/node/ripgrepTextSearchEngine.ts` (TYPESCRIPT) | Magnitude: 695.48 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 547, branch: 135, structural_boundaries: 130, state_mutation: 115
- `src/vs/workbench/api/common/configurationExtensionPoint.ts` (TYPESCRIPT) | Magnitude: 184.92 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 441, structural_boundaries: 96, branch: 68, state_mutation: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/vs/base/common/console.ts` (TYPESCRIPT) | Magnitude: 94.76 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 72, branch: 27, structural_boundaries: 26, core_var_decl: 13
- `src/vs/base/test/common/resourceTree.test.ts` (TYPESCRIPT) | Magnitude: 25.1 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 49, safety_bypasses: 11, test: 10, state_mutation: 9
- `src/vs/platform/product/common/product.ts` (TYPESCRIPT) | Magnitude: 12.36 | Delta: **0.033** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 51, branch: 16, structural_boundaries: 6, core_var_decl: 6
- `src/vs/workbench/services/progress/test/browser/progressIndicator.test.ts` (TYPESCRIPT) | Magnitude: 68.62 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 87, structural_boundaries: 23, state_mutation: 18, args: 14
- `src/vs/workbench/services/extensions/test/common/extensionRunningLocationTracker.test.ts` (TYPESCRIPT) | Magnitude: 22.86 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 113, core_var_decl: 46, design_camel_case: 38, structural_boundaries: 31

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `extensions/markdown-language-features/src/languageFeatures/linkUpdater.ts` (TYPESCRIPT) | Magnitude: 164.82 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 172, structural_boundaries: 53, branch: 36, concurrency: 22
- `src/vs/workbench/contrib/editTelemetry/browser/telemetry/arcTelemetrySender.ts` (TYPESCRIPT) | Magnitude: 0.68 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 206, structural_boundaries: 49, args: 21, core_var_decl: 18
- `src/vs/workbench/contrib/chat/browser/createSlashCommandsUsageTracker.ts` (TYPESCRIPT) | Magnitude: 0.49 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 53, branch: 19, structural_boundaries: 18, core_var_decl: 7
- `src/vs/workbench/contrib/chat/browser/aiCustomization/customizationCreatorService.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 151, structural_boundaries: 88, branch: 41, core_var_decl: 25
- `src/vs/workbench/contrib/comments/browser/commentsInputContentProvider.ts` (TYPESCRIPT) | Magnitude: 0.26 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 26, structural_boundaries: 22, import: 13, branch: 6

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vs/workbench/contrib/chat/browser/agentSessions/agentSessionsViewer.ts` -> Churn: **91.79%** | Cog Load: 68.4761% | Debt: 22.1448%
- `src/vs/workbench/contrib/chat/browser/widget/input/chatInputPart.ts` -> Churn: **91.22%** | Cog Load: 81.8945% | Debt: 91.2846%
- `src/vs/workbench/api/common/extHost.protocol.ts` -> Churn: **85.46%** | Cog Load: 59.0044% | Debt: 7.9154%
- `src/vs/workbench/contrib/chat/browser/widget/chatWidget.ts` -> Churn: **85.04%** | Cog Load: 86.192% | Debt: 8.2408%
- `src/vs/workbench/contrib/terminalContrib/chatAgentTools/browser/tools/runInTerminalTool.ts` -> Churn: **84.9%** | Cog Load: 93.8727% | Debt: 8.2404%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `extensions/git/src/repository.ts` -> **Ladislau Szomoru** (83.0% isolated ownership) | Magnitude: 3170.16
- `src/vs/editor/browser/viewParts/minimap/minimap.ts` -> **Alexandru Dima** (100.0% isolated ownership) | Magnitude: 1630.3
- `src/vs/platform/contextkey/common/contextkey.ts` -> **Alex Ross** (100.0% isolated ownership) | Magnitude: 1402.56
- `.github/skills/azure-pipelines/azure-pipeline.ts` -> **João Moreno** (100.0% isolated ownership) | Magnitude: 1358.46
- `src/vs/base/browser/dompurify/dompurify.js` -> **Henning Dieterichs** (100.0% isolated ownership) | Magnitude: 1335.16

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/vs/base/common/uri.ts` -> **Severity: 23.458** (Embedded: 0.3269 * Error Risk: 71.7533%)
- `src/vs/platform/instantiation/common/instantiation.ts` -> **Severity: 22.49** (Embedded: 0.2811 * Error Risk: 80.0%)
- `src/vs/base/common/lifecycle.ts` -> **Severity: 21.145** (Embedded: 0.3516 * Error Risk: 60.1318%)
- `src/vs/base/common/event.ts` -> **Severity: 20.061** (Embedded: 0.2952 * Error Risk: 67.9541%)
- `src/vs/base/common/errors.ts` -> **Severity: 19.416** (Embedded: 0.2742 * Error Risk: 70.8163%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/vs/base/common/platform.ts` -> **Severity: 1992.083** (Blast Radius: 23.905 * Doc Risk: 83.3333%)
- `src/vs/base/common/errors.ts` -> **Severity: 1954.055** (Blast Radius: 23.332 * Doc Risk: 83.75%)
- `src/vs/base/common/lifecycle.ts` -> **Severity: 1627.46** (Blast Radius: 30.257 * Doc Risk: 53.7879%)
- `src/vs/base/common/event.ts` -> **Severity: 1140.45** (Blast Radius: 20.472 * Doc Risk: 55.7078%)
- `src/vs/base/common/process.ts` -> **Severity: 1023.1** (Blast Radius: 10.231 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 2132 literal sites + 20 sites through wrappers = 2152
- **`panics_and_aborts`:** 4961 literal sites + 96 sites through wrappers = 5057

- `fail` (function, panics_and_aborts, primitive): 41 call sites in 1 files -- `src/vs/workbench/services/themes/common/plistParser.ts`
- `assertNever` (function, panics_and_aborts, primitive): 33 call sites in 27 files -- `src/vs/base/common/assert.ts`
- `fatal` (function, debug_prints, primitive): 5 call sites in 1 files -- `extensions/git/src/askpass-main.ts`
- `fatal` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `extensions/git/src/askpass-main.ts`
- `missingAttribute` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `src/vs/workbench/services/configurationResolver/browser/baseConfigurationResolverService.ts`
- `displayNextSteps` (function, debug_prints, primitive): 2 call sites in 1 files -- `.github/skills/azure-pipelines/azure-pipeline.ts`
- `eventuallyExit` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/vs/server/node/remoteExtensionHostAgentCli.ts`
- `fatal` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/vs/server/node/server.cli.ts`
- `fatal` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `src/vs/server/node/server.cli.ts`
- `handleBugIndicatingErrorRecovery` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/vs/base/common/observableInternal/base.ts`
- `onError` (function, debug_prints, primitive): 2 call sites in 1 files -- `src/vs/base/browser/indexedDB.ts`
- `print_forwarding_addr` (function, debug_prints, primitive): 2 call sites in 1 files -- `cli/src/tunnels/local_forwarding.rs`
*(+13 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 274942 call pairs -- scoped 44.2%, unique 0.0%, ambiguous 39.7%, external 16.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 268111 | 44.9% | 0.0% | 40.5% | 14.6% |
| rust | 4730 | 17.2% | 0.0% | 3.6% | 79.1% |
| javascript | 1255 | 16.4% | 0.0% | 46.1% | 37.5% |
| shell | 438 | 18.7% | 0.0% | 0.0% | 81.3% |
| html | 321 | 11.2% | 0.0% | 0.0% | 88.8% |
| objective-c | 26 | 0.0% | 0.0% | 0.0% | 100.0% |
| python | 13 | 7.7% | 0.0% | 0.0% | 92.3% |
| cpp | 11 | 18.2% | 0.0% | 0.0% | 81.8% |
| go | 6 | 0.0% | 0.0% | 0.0% | 100.0% |
| perl | 6 | 16.7% | 0.0% | 0.0% | 83.3% |

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
