# ARCHITECTURAL_BRIEF: vscode_cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/vscode_cobol` |
| **Timestamp** | `2026-08-03T19:29:16.582791+00:00` |
| **Scan Duration** | `0.8s` |
| **Git Branch** | `main` |
| **Git Commit** | `89d3f07af1062616bf0c433e049f270d0f5e2c4d` |
| **Git Remote** | `https://github.com/spgennard/vscode_cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 91 malicious artifacts.

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
| Total Artifacts | 217 |
| Analyzed Artifacts (Scanned) | 172 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 45 |
| Total LOC | 23496 |
| Volatility Index | 0.029 |
| % Scanned of codebase = | 79.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2094 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3737 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1376 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 82 | 18148 | 47.7% |
| JSON | 50 | 4847 | 29.1% |
| PLAINTEXT | 16 | 0 | 9.3% |
| XML | 10 | 0 | 5.8% |
| SHELL | 7 | 157 | 4.1% |
| MARKDOWN | 4 | 0 | 2.3% |
| CSS | 1 | 224 | 0.6% |
| COBOL | 1 | 11 | 0.6% |
| JAVASCRIPT | 1 | 109 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.223`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 99 | 57.6% |
| file_cluster_13 | 43 | 25.0% |
| file_cluster_4 | 9 | 5.2% |
| file_cluster_0 | 1 | 0.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 20 | 11.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 45*

**Composition by Extension & Reason:**
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3297 LOC), 1x Excluded (Static Asset Blob without Intent: 2157 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.gif`: 6x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2040 LOC)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3426 commas in 573 LOC)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.1 | 28.3 | 9.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 38.8 | 38.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 10.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 31.2 | 2.3 | 80.0 |
| API Exposure | 0.0 | 18.3 | 3.7 | 1.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 19.3 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 73.6 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.1 | 1.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 58.2 | 57.3 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 44.7 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 39.5 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/fileutils.ts` (Hits: 16)
- `src/vsfileutils.ts` (Hits: 16)
- `gen_changelog.sh` (Hits: 15)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **iconfiguration.ts** (`src/iconfiguration.ts`) — 52 inbound connections
2. **vsexternalfeatures.ts** (`src/vsexternalfeatures.ts`) — 30 inbound connections
3. **vsconfiguration.ts** (`src/vsconfiguration.ts`) — 28 inbound connections
4. **externalfeatures.ts** (`src/externalfeatures.ts`) — 27 inbound connections
5. **cobolsourcescanner.ts** (`src/cobolsourcescanner.ts`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **extension.ts** (`src/extension.ts`) — 51 outbound dependencies
2. **extension.ts** (`src/web/extension.ts`) — 25 outbound dependencies
3. **vscobolutils.ts** (`src/vscobolutils.ts`) — 21 outbound dependencies
4. **vscommon_commands.ts** (`src/vscommon_commands.ts`) — 21 outbound dependencies
5. **vscobscanner.ts** (`src/vscobscanner.ts`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isParagraph` (@ `src/cobolsourcescanner.ts`) -> Impact: **4260.4** | LOC: 927
- `activate` (@ `src/extension.ts`) -> Impact: **847.2** | LOC: 424
- `provideCompletionItems` (@ `src/vscobolprovider.ts`) -> Impact: **675.7** | LOC: 210
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `updateDecorations` (@ `src/vsmargindecorations.ts`) -> Impact: **602.7** | LOC: 202
  * *Intent:* // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
- `provideDocumentSymbols` (@ `src/vssymbolprovider.ts`) -> Impact: **486.6** | LOC: 154
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `forkScanner` (@ `src/vscobscanner.ts`) -> Impact: **484.6** | LOC: 188
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `provideRenameEdits` (@ `src/vsrenameprovider.ts`) -> Impact: **423.9** | LOC: 183
- `getCachedObject` (@ `src/vscobolscanner.ts`) -> Impact: **381.6** | LOC: 114
- `get` (@ `src/sourceformat.ts`) -> Impact: **378.5** | LOC: 174
- `provideHover` (@ `src/vshoverprovider.ts`) -> Impact: **371.2** | LOC: 144

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `isParagraph` (@ `src/cobolsourcescanner.ts`) -> **O(2^N) [Recursive]**
- `activate` (@ `src/extension.ts`) -> **O(2^N) [Recursive]**
- `getCachedObject` (@ `src/vscobolscanner.ts`) -> **O(2^N) [Recursive]**
- `addFolder` (@ `src/vssourceviewtree.ts`) -> **O(2^N) [Recursive]**
- `getFullWorkspaceFilename` (@ `src/consoleexternalfeatures.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `get` (@ `src/vscobolfolders.ts`) -> **O(2^N) [Recursive]**
- `setupSourceViewTree` (@ `src/vssourceviewtree.ts`) -> **O(2^N) [Recursive]**
- `activate` (@ `src/web/extension.ts`) -> **O(2^N) [Recursive]**
- `dispose` (@ `src/bmspreviewpanel.ts`) -> **O(2^N) [Recursive]**
- `cacheUpdateRequired` (@ `src/cobscanner.ts`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `isParagraph` (@ `src/cobolsourcescanner.ts`) -> DB Complexity: **248**
- `constructor` (@ `src/iconfiguration.ts`) -> DB Complexity: **104**
- `constructor` (@ `src/vssourceviewtree.ts`) -> DB Complexity: **92**
- `addExtension` (@ `src/vssourceviewtree.ts`) -> DB Complexity: **40**
- `processToken` (@ `src/cobolsymboltableeventhelper.ts`) -> DB Complexity: **39**
- `constructor` (@ `src/cobolsourcescanner.ts`) -> DB Complexity: **38**
- `activate` (@ `src/extension.ts`) -> DB Complexity: **37**
- `constructor` (@ `src/filesourcehandler.ts`) -> DB Complexity: **35**
- `provideRenameEdits` (@ `src/vsrenameprovider.ts`) -> DB Complexity: **30**
- `provideDocumentSymbols` (@ `src/vssymbolprovider.ts`) -> DB Complexity: **29**
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 70 | 3565.11 | 51.93% | 11.41% |
| `__monolith__` | 26 | 386.22 | 13.46% | 26.31% |
| `syntaxes` | 21 | 370.2 | 2.2% | 0.0% |
| `snippets` | 6 | 107.14 | 3.61% | 0.0% |
| `syntaxes/markdown` | 6 | 95.4 | 6.85% | 0.0% |
| `src/keywords` | 7 | 51.48 | 9.04% | 14.1% |
| `src/test/suite` | 20 | 46.48 | 2.61% | 0.0% |
| `src/web` | 1 | 45.23 | 27.13% | 0.0% |
| `images` | 3 | 31.56 | 5.0% | 0.0% |
| `images/dark` | 3 | 31.56 | 5.0% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `get_dotfiles.sh` -> **100.0%** Exposure
- `justpublish.sh` -> **100.0%** Exposure
- `rm_git_release.sh` -> **100.0%** Exposure
- `upd.sh` -> **100.0%** Exposure
- `src/cobolglobalcache.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/cobolglobalcache.ts` -> **100.0%** Exposure
- `src/cobolsourcescanner.ts` -> **100.0%** Exposure
- `src/cobolsymboltableeventhelper.ts` -> **100.0%** Exposure
- `src/filesourcehandler.ts` -> **100.0%** Exposure
- `src/makedeps.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/cobscanner_worker.ts` -> **15** Orphaned Functions | **0** Duplicates
- `src/vscodesourcehandler.ts` -> **0** Orphaned Functions | **14** Duplicates
- `src/cobolglobalcache.ts` -> **0** Orphaned Functions | **10** Duplicates
- `src/vsconfiguration.ts` -> **0** Orphaned Functions | **3** Duplicates
- `src/vsdirectivesconv.ts` -> **0** Orphaned Functions | **3** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/cobolsourcescanner.ts`** -> AI Confidence: **99.48%**
2. **`src/cobolsymboltableeventhelper.ts`** -> AI Confidence: **99.48%**
3. **`src/vssnippetprovider.ts`** -> AI Confidence: **99.48%**
4. **`src/vssymbolprovider.ts`** -> AI Confidence: **99.48%**
5. **`src/cobollinter.ts`** -> AI Confidence: **99.39%**
6. **`src/vscobolprovider.ts`** -> AI Confidence: **99.39%**
7. **`src/vscobolscanner.ts`** -> AI Confidence: **99.39%**
8. **`src/vscobolutils.ts`** -> AI Confidence: **99.39%**
9. **`src/vsformatconverter.ts`** -> AI Confidence: **99.39%**
10. **`src/vskeywordprovider.ts`** -> AI Confidence: **99.39%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/bmspreviewpanel.ts` -> **100.0%** Exposure
- `src/caseformatter.ts` -> **100.0%** Exposure
- `src/cobollinter.ts` -> **100.0%** Exposure
- `src/cobolprogram.ts` -> **100.0%** Exposure
- `src/cobolsourcescanner.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/test/runTest.ts` -> **100.0%** Exposure
- `webpack.config.js` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/bmspreviewpanel.ts` -> **100.0%** Exposure
- `src/caseformatter.ts` -> **100.0%** Exposure
- `src/cobolglobalcache.ts` -> **100.0%** Exposure
- `src/cobollinter.ts` -> **100.0%** Exposure
- `src/cobolprogram.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `120` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cobscanner_worker.ts` (TYPESCRIPT) -> Cumulative Risk: **924.9**
- **Archetype:** `file_cluster_13` (Distance: 13.951 IQR)
- **Magnitude:** 21.04 | **LOC:** 187 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `logTimedMessage` (Impact: 24.9), `getFullWorkspaceFilename` (Impact: 21.4), `isFile` (Impact: 21.1)

### 2. `src/vsfoldingprovider.ts` (TYPESCRIPT) -> Cumulative Risk: **907.68**
- **Archetype:** `file_cluster_8` (Distance: 11.221 IQR)
- **Magnitude:** 56.93 | **LOC:** 258 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `provideFoldingRanges` (Impact: 220.3), `addCommentAndBlockFolds` (Impact: 192.1), `getSignificantText` (Impact: 39.9)

### 3. `src/vssourceviewtree.ts` (TYPESCRIPT) -> Cumulative Risk: **905.18**
- **Archetype:** `file_cluster_4` (Distance: 13.64 IQR)
- **Magnitude:** 151.42 | **LOC:** 500 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `addExtension` (Impact: 288.7), `addFolder` (Impact: 158.2), `setupSourceViewTree` (Impact: 105.7)

### 4. `src/vscodesourcehandler.ts` (TYPESCRIPT) -> Cumulative Risk: **897.2**
- **Archetype:** `file_cluster_13` (Distance: 13.414 IQR)
- **Magnitude:** 89.62 | **LOC:** 431 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getLine` (Impact: 136.5), `sendCommentCallback` (Impact: 119.0), `getCommentAtLine` (Impact: 62.5)

### 5. `src/vsrenameprovider.ts` (TYPESCRIPT) -> Cumulative Risk: **896.83**
- **Archetype:** `file_cluster_13` (Distance: 11.796 IQR)
- **Magnitude:** 52.66 | **LOC:** 201 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `provideRenameEdits` (Impact: 423.9)

### 6. `src/cobollinter.ts` (TYPESCRIPT) -> Cumulative Risk: **896.75**
- **Archetype:** `file_cluster_4` (Distance: 12.31 IQR)
- **Magnitude:** 118.64 | **LOC:** 477 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `updateLinter` (Impact: 255.8), `processScannedDocumentForUnusedSymbols` (Impact: 231.8), `processParsedDocumentForStandards` (Impact: 151.6)

### 7. `src/tabstopper.ts` (TYPESCRIPT) -> Cumulative Risk: **892.07**
- **Archetype:** `file_cluster_4` (Distance: 12.296 IQR)
- **Magnitude:** 43.29 | **LOC:** 201 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `executeTab` (Impact: 87.8), `singleSelectionUnTab` (Impact: 72.8), `escapeString` (Impact: 36.8)

### 8. `src/vsmargindecorations.ts` (TYPESCRIPT) -> Cumulative Risk: **879.48**
- **Archetype:** `file_cluster_13` (Distance: 11.197 IQR)
- **Magnitude:** 72.41 | **LOC:** 280 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9767%)
- **Heaviest Functions:** `updateDecorations` (Impact: 602.7), `updateJCLDecorations` (Impact: 15.8), `isEnabledViaWorkspace4jcl` (Impact: 12.6)

### 9. `src/opencopybook.ts` (TYPESCRIPT) -> Cumulative Risk: **874.98**
- **Archetype:** `file_cluster_4` (Distance: 11.044 IQR)
- **Magnitude:** 61.91 | **LOC:** 295 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `resolveDefinitionsFallback` (Impact: 186.3), `resolveDefinitions` (Impact: 100.6), `expandLogicalCopyBookOrEmpty` (Impact: 96.5)

### 10. `src/vsconfiguration.ts` (TYPESCRIPT) -> Cumulative Risk: **874.42**
- **Archetype:** `file_cluster_8` (Distance: 12.257 IQR)
- **Magnitude:** 90.38 | **LOC:** 695 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getCopybookdirs_defaults` (Impact: 185.6), `initSettings` (Impact: 40.5), `clearResourceCache` (Impact: 28.9)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/cobolsourcescanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.368 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.445 IQR)
- **Top Global Matches:** file_cluster_13: 14.368, file_cluster_8: 14.416, file_cluster_11: 14.445
- **Magnitude:** 593.29 | **LOC:** 3429 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 248
- **Risk Profile:** Cognitive Load (92.0453%), Tech Debt (8.7692%)
**Top Internal Functions/Classes:**
  * `isParagraph` (Impact: 4260.4 | O(2^N) | DB: 248)
  * `newCOBOLToken` (Impact: 293.4 | O(N^6) | DB: 14)
  * `constructor` (Impact: 187.5 | O(N^6) | DB: 38)
  * `transferReference` (Impact: 44.0 | O(N^4) | DB: 3)
  * `camelize` (Impact: 41.2 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 958`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 33`, `import: 13`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 150`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.9
  * `Choke Point (Betweenness):` 0.008327 | `Ripple Effect (Closeness):` 0.143337
  * `Imports (Out-Degree: 12):` icobolsourcescanner, vsdirectivesconv, filesourcehandler, path, cobolglobalcache, isourcehandler, cobolKeywords, externalfeatures...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/vscobolutils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.643 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.423 IQR)
- **Top Global Matches:** file_cluster_13: 12.643, file_cluster_8: 12.724, file_cluster_11: 12.743
- **Magnitude:** 252.15 | **LOC:** 1439 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (45.7184%), Tech Debt (7.9222%)
**Top Internal Functions/Classes:**
  * `foldTokenLine` (Impact: 361.5 | O(N^6) | DB: 6)
  * `setupFilePaths` (Impact: 350.8 | O(N^6) | DB: 16)
  * `setupUrlPaths` (Impact: 175.1 | O(N^6) | DB: 10)
  * `enforceFileExtensions` (Impact: 174.7 | O(N^6) | DB: 3)
  * `saveGlobalCacheToWorkspace` (Impact: 156.3 | O(N^6) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 104`, `args: 69`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `state_mutation: 216`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `io: 8`, `api: 57`, `concurrency: 19`, `import: 22`
* *Defense:* `safety: 30`, `doc: 2`, `immutability_locks: 217`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.165
  * `Choke Point (Betweenness):` 0.023029 | `Ripple Effect (Closeness):` 0.125802
  * `Imports (Out-Degree: 19):` vscode, vslogger, vsconfiguration, vscobolfolders, vscommon_commands, path, globalcachehelper, vsfileutils...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/vssourceviewtree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.64 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.355 IQR)
- **Top Global Matches:** file_cluster_4: 13.64, file_cluster_13: 13.871, file_cluster_8: 13.956
- **Magnitude:** 151.42 | **LOC:** 500 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 92
- **Risk Profile:** Cognitive Load (96.4804%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addExtension` (Impact: 288.7 | O(N^6) | DB: 40)
  * `addFolder` (Impact: 158.2 | O(2^N) | DB: 10)
  * `setupSourceViewTree` (Impact: 105.7 | O(2^N))
  * `getItemsFromMap` (Impact: 93.4 | O(N^6) | DB: 8)
  * `constructor` (Impact: 56.0 | O(N^3) | DB: 92)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 40`, `args: 29`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 459`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 74`, `import: 8`
* *Defense:* `safety: 9`, `immutability_locks: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 6):` vscode, vslogger, vscobolutils, vssourcescannerutils, vscobolfolders, sourceItem, iconfiguration
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/extension.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.534 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.959 IQR)
- **Top Global Matches:** file_cluster_4: 12.534, file_cluster_13: 12.625, file_cluster_11: 12.878
- **Magnitude:** 150.81 | **LOC:** 882 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 37
- **Risk Profile:** Cognitive Load (67.8614%), Tech Debt (8.1483%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 847.2 | O(2^N) | DB: 37)
  * `handleScopedChange` (Impact: 167.1 | O(N^4))
  * `setupLogChannel` (Impact: 130.2 | O(N^5) | DB: 3)
  * `activateDesktop` (Impact: 78.9 | O(N^4) | DB: 9)
  * `openChangeLog` (Impact: 43.5 | O(N^5) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 114`, `args: 62`, `func_start: 32`
* *Risk/State:* `state_mutation: 95`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 118`, `import: 46`
* *Defense:* `safety: 13`, `doc: 8`, `immutability_locks: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` vsreferenceprovider, cobollinter, vscode, vslogger, vshoverprovider, properties-reader, vscolourcomments, vsconfiguration...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vscobolprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.061 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.731 IQR)
- **Top Global Matches:** file_cluster_13: 12.061, file_cluster_8: 12.19, file_cluster_11: 12.4
- **Magnitude:** 141.41 | **LOC:** 510 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (74.3873%), Tech Debt (8.4593%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 675.7 | O(N^6) | DB: 27)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getItemsFromList` (Impact: 136.0 | O(N^6) | DB: 7)
  * `getAllTypes` (Impact: 116.5 | O(N^5) | DB: 6)
  * `getAllConstantsOrVariables` (Impact: 85.6 | O(N^6) | DB: 3)
  * `getConstantsOrVariables` (Impact: 85.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 48`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 160`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 6`, `import: 12`
* *Defense:* `doc: 5`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 10):` icobolsourcescanner, cobolsourcescanner, vscode, vslogger, globalcachehelper, externalfeatures, vsexternalfeatures, vsconfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsformatconverter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.168 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.061 IQR)
- **Top Global Matches:** file_cluster_8: 12.168, file_cluster_7: 12.475, file_cluster_13: 12.505
- **Magnitude:** 125.75 | **LOC:** 1366 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (33.2484%), Tech Debt (14.0596%)
**Top Internal Functions/Classes:**
  * `convertFreeToFixed` (Impact: 124.5 | O(N^5) | DB: 13)
  * `convertFreeToVariable` (Impact: 123.8 | O(N^5) | DB: 13)
    * *Intent:* // ============================================================================ // Main conversion f...
  * `convertSourceFormat` (Impact: 92.5 | O(N^4) | DB: 5)
  * `convertSource` (Impact: 91.4 | O(N^4))
  * `convertVariableToFixed` (Impact: 57.3 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 84`, `args: 35`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 219`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 8`
* *Defense:* `safety: 5`, `doc: 46`, `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.105
  * `Choke Point (Betweenness):` 0.000109 | `Ripple Effect (Closeness):` 0.064474
  * `Imports (Out-Degree: 7):` vscodesourcehandler, vsextutis, vscode, vslogger, externalfeatures, vsexternalfeatures, vsconfiguration, sourceformat
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vssnippetprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.722 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.62 IQR)
- **Top Global Matches:** file_cluster_8: 10.722, file_cluster_7: 11.281, file_cluster_13: 11.452
- **Magnitude:** 119.34 | **LOC:** 1825 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (15.4071%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 176.0 | O(N^6) | DB: 13)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getExactCallSnipetOrPartialSnippet` (Impact: 140.6 | O(N^6) | DB: 4)
  * `addSnippet` (Impact: 101.6 | O(N^4) | DB: 8)
  * `getExactFunctionSnipetOrPartialSnippet` (Impact: 93.9 | O(N^6) | DB: 4)
  * `getExactDollorOrPartial` (Impact: 93.9 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 45`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 203`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.257
  * `Choke Point (Betweenness):` 0.000628 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 10):` icobolsourcescanner, cobolCallTargets, vscode, vscobolutils, vsexternalfeatures, vsconfiguration, vscobolscanner, extensionDefaults...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobollinter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.31 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_4: 12.31, file_cluster_8: 12.359, file_cluster_13: 12.364
- **Magnitude:** 118.64 | **LOC:** 477 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 25
- **Risk Profile:** Cognitive Load (85.3157%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateLinter` (Impact: 255.8 | O(N^6) | DB: 25)
  * `processScannedDocumentForUnusedSymbols` (Impact: 231.8 | O(N^6) | DB: 9)
  * `processParsedDocumentForStandards` (Impact: 151.6 | O(N^6) | DB: 8)
  * `findCopyBookDirectory` (Impact: 135.9 | O(N^6) | DB: 16)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideCodeActions` (Impact: 89.5 | O(N^6) | DB: 4)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 41`, `args: 13`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 193`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 36`, `import: 13`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.033
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 10):` icobolsourcescanner, cobolsourcescanner, vsextutis, vscode, path, externalfeatures, vscobolutils, vsexternalfeatures...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsconfiguration.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.257 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.804 IQR)
- **Top Global Matches:** file_cluster_8: 12.257, file_cluster_13: 12.313, file_cluster_11: 12.544
- **Magnitude:** 90.38 | **LOC:** 695 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (65.739%), Tech Debt (26.7186%)
**Top Internal Functions/Classes:**
  * `getCopybookdirs_defaults` (Impact: 185.6 | O(N^6) | DB: 13)
  * `initSettings` (Impact: 40.5 | O(N^4) | DB: 1)
  * `clearResourceCache` (Impact: 28.9 | O(N^4) | DB: 3)
  * `isOutlineEnabled` (Impact: 28.4 | O(N^3) | DB: 1)
  * `get_resource_settings_via_uri` (Impact: 21.4 | O(N^4) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 67`, `args: 38`, `func_start: 37`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 196`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 44`, `import: 6`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 41`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.785
  * `Choke Point (Betweenness):` 0.013456 | `Ripple Effect (Closeness):` 0.166384
  * `Imports (Out-Degree: 5):` fileutils, vscode, externalfeatures, vscobolutils, extensionDefaults, iconfiguration
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `src/vscodesourcehandler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.414 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.17 IQR)
- **Top Global Matches:** file_cluster_13: 13.414, file_cluster_11: 13.616, file_cluster_8: 13.675
- **Magnitude:** 89.62 | **LOC:** 431 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (86.7957%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 136.5 | O(N^6) | DB: 16)
  * `sendCommentCallback` (Impact: 119.0 | O(N^6) | DB: 11)
  * `getCommentAtLine` (Impact: 62.5 | O(N^6) | DB: 12)
  * `getText` (Impact: 45.3 | O(2^N) | DB: 2)
  * `getLineTabExpanded` (Impact: 42.8 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 56`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `state_mutation: 280`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `safety: 10`, `doc: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.142
  * `Choke Point (Betweenness):` 0.002591 | `Ripple Effect (Closeness):` 0.09464
  * `Imports (Out-Degree: 9):` vscode, isourcehandler, externalfeatures, cobolKeywords, stringutils, vscolourcomments, vsconfiguration, vsexternalfeatures...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/filesourcehandler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.039 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.171 IQR)
- **Top Global Matches:** file_cluster_13: 13.039, file_cluster_8: 13.122, file_cluster_11: 13.303
- **Magnitude:** 83.07 | **LOC:** 378 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 35
- **Risk Profile:** Cognitive Load (86.5936%), Tech Debt (10.248%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 142.8 | O(N^6) | DB: 15)
  * `sendCommentCallback` (Impact: 119.0 | O(N^6) | DB: 11)
  * `constructor` (Impact: 72.6 | O(N^6) | DB: 35)
  * `getCommentAtLine` (Impact: 62.5 | O(N^6) | DB: 12)
  * `findShortWorkspaceFilename` (Impact: 57.1 | O(N^6) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 43`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 217`, `planned_debt: 2`
* *Architecture:* `io: 8`, `api: 21`, `import: 9`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.308
  * `Choke Point (Betweenness):` 0.000761 | `Ripple Effect (Closeness):` 0.100292
  * `Imports (Out-Degree: 6):` path, externalfeatures, isourcehandler, cobolKeywords, stringutils, fs, url, extensionDefaults...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vssymbolprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.81 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.357 IQR)
- **Top Global Matches:** file_cluster_13: 11.81, file_cluster_8: 11.817, file_cluster_4: 11.926
- **Magnitude:** 81.68 | **LOC:** 319 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 29
- **Risk Profile:** Cognitive Load (79.6375%), Tech Debt (59.4986%)
**Top Internal Functions/Classes:**
  * `provideDocumentSymbols` (Impact: 486.6 | O(N^6) | DB: 29)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 113.0 | O(N^6) | DB: 7)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 82.0 | O(N^6) | DB: 6)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 27`, `args: 5`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 112`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 7):` vscode, vslogger, vsexternalfeatures, vsconfiguration, vscobolscanner, splittoken, cobolsourcescanner, iconfiguration
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsmargindecorations.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.197 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 11.197, file_cluster_8: 11.294, file_cluster_4: 11.562
- **Magnitude:** 72.41 | **LOC:** 280 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (88.9119%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateDecorations` (Impact: 602.7 | O(N^6) | DB: 23)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  * `updateJCLDecorations` (Impact: 15.8 | O(N^4) | DB: 2)
  * `isEnabledViaWorkspace4jcl` (Impact: 12.6 | O(N^3))
  * `setupTags` (Impact: 5.3 | O(2^N) | DB: 1)
  * `constructor` (Impact: 2.3 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 67`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 10):` vscodesourcehandler, vsextutis, vscode, externalfeatures, vscolourcomments, vsexternalfeatures, vsconfiguration, sourceformat...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/bmspreviewpanel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.16 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.139 IQR)
- **Top Global Matches:** file_cluster_8: 11.16, file_cluster_2: 11.516, file_cluster_13: 11.611
- **Magnitude:** 70.54 | **LOC:** 651 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (46.9748%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseBms` (Impact: 193.6 | O(N^6) | DB: 19)
  * `parseField` (Impact: 193.6 | O(N^6) | DB: 16)
  * `constructor` (Impact: 38.4 | O(N^5) | DB: 16)
  * `updatePreview` (Impact: 31.2 | O(N^6))
  * `dispose` (Impact: 26.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 84`, `structural_boundaries: 72`, `args: 51`, `func_start: 16`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 4`, `state_mutation: 138`
* *Architecture:* `api: 21`, `concurrency: 6`, `import: 1`
* *Defense:* `safety: 9`, `immutability_locks: 42`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.033
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 0):` vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vscobolscanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.466 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.773 IQR)
- **Top Global Matches:** file_cluster_13: 13.466, file_cluster_11: 13.804, file_cluster_0: 13.829
- **Magnitude:** 66.66 | **LOC:** 226 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (70.4302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCachedObject` (Impact: 381.6 | O(2^N) | DB: 11)
  * `processToken` (Impact: 112.0 | O(N^4) | DB: 9)
  * `start` (Impact: 36.6 | O(N^3) | DB: 10)
  * `removeCachedObject` (Impact: 10.9 | O(N^3) | DB: 1)
  * `clearCOBOLCache` (Impact: 3.2 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 95`, `dead_code: 2`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 16`, `doc: 2`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.409
  * `Choke Point (Betweenness):` 0.01293 | `Ripple Effect (Closeness):` 0.139403
  * `Imports (Out-Degree: 10):` icobolsourcescanner, vscodesourcehandler, vscode, vslogger, globalcachehelper, cobolglobalcache, vscobolutils, vsexternalfeatures...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/opencopybook.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.044 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.254 IQR)
- **Top Global Matches:** file_cluster_4: 11.044, file_cluster_13: 11.143, file_cluster_8: 11.282
- **Magnitude:** 61.91 | **LOC:** 295 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (85.6695%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveDefinitionsFallback` (Impact: 186.3 | O(N^6) | DB: 10)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `resolveDefinitions` (Impact: 100.6 | O(N^6) | DB: 4)
  * `expandLogicalCopyBookOrEmpty` (Impact: 96.5 | O(N^6) | DB: 18)
  * `extractCopyBookFilename` (Impact: 75.4 | O(N^6) | DB: 5)
  * `getURIForCopybook` (Impact: 28.2 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `io: 8`, `api: 5`, `concurrency: 37`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.824
  * `Choke Point (Betweenness):` 0.003186 | `Ripple Effect (Closeness):` 0.112128
  * `Imports (Out-Degree: 8):` icobolsourcescanner, path, vscode, vslogger, externalfeatures, vsexternalfeatures, vsconfiguration, vsfileutils...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/vscobscanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.965 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.35 IQR)
- **Top Global Matches:** file_cluster_13: 9.965, file_cluster_8: 10.023, file_cluster_4: 10.324
- **Magnitude:** 61.11 | **LOC:** 295 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (35.9615%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `forkScanner` (Impact: 484.6 | O(N^6) | DB: 22)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getScanData` (Impact: 35.0 | O(N^5) | DB: 1)
  * `processAllFilesInWorkspaceOutOfProcess` (Impact: 31.0 | O(N^3) | DB: 2)
  * `getCobScannerDirectory` (Impact: 8.4 | O(N^3) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 33`, `args: 9`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 9`, `api: 4`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.033
  * `Choke Point (Betweenness):` 7.7e-05 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 13):` child_process, path, vscode, vslogger, globalcachehelper, cobolglobalcache, cobscannerdata, vscobolutils...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsfoldingprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.221 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.591 IQR)
- **Top Global Matches:** file_cluster_8: 11.221, file_cluster_13: 11.27, file_cluster_7: 11.572
- **Magnitude:** 56.93 | **LOC:** 258 | **CtrlFlow:** 74.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (59.8395%), Tech Debt (72.4762%)
**Top Internal Functions/Classes:**
  * `provideFoldingRanges` (Impact: 220.3 | O(N^6) | DB: 4)
  * `addCommentAndBlockFolds` (Impact: 192.1 | O(N^6) | DB: 14)
    * *Intent:* /**
  * `getSignificantText` (Impact: 39.9 | O(N^4))
  * `isCommentLine` (Impact: 21.5 | O(N^3))
  * `findLastBlock` (Impact: 15.4 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`, `fragile_debt: 4`
* *Architecture:* `api: 3`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 5):` vscode, externalfeatures, vsexternalfeatures, vsconfiguration, vscobolscanner, cobolsourcescanner
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsfileutils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.489 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.451 IQR)
- **Top Global Matches:** file_cluster_8: 9.489, file_cluster_4: 9.581, file_cluster_13: 9.654
- **Magnitude:** 56.91 | **LOC:** 292 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (34.1279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getShortWorkspaceFilename` (Impact: 78.5 | O(N^6) | DB: 4)
  * `_findCopyBookInDirectory` (Impact: 56.4 | O(N^6) | DB: 9)
  * `_findCopyBookInDirectoryViaURL` (Impact: 56.3 | O(N^6))
  * `getFullWorkspaceFilename` (Impact: 54.8 | O(N^5) | DB: 6)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/ban-types
  * `findCopyBook` (Impact: 50.5 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 52`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 16`, `api: 19`, `concurrency: 16`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.124286
  * `Imports (Out-Degree: 3):` path, vscode, externalfeatures, fs, vscobolfolders, iconfiguration
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/cobolworkspacecache.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.017 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.469 IQR)
- **Top Global Matches:** file_cluster_13: 12.017, file_cluster_8: 12.157, file_cluster_0: 12.251
- **Magnitude:** 56.51 | **LOC:** 295 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (45.8333%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addSymbolToCache` (Impact: 88.1 | O(N^6) | DB: 7)
  * `loadGlobalTypesCacheFromArray` (Impact: 67.0 | O(N^5) | DB: 1)
  * `removeAllProgramSymbols` (Impact: 57.0 | O(N^6) | DB: 4)
  * `addCalableSymbol` (Impact: 46.8 | O(N^4) | DB: 9)
  * `loadFileCacheFromArray` (Impact: 41.3 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 21`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 57`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 23`, `import: 6`
* *Defense:* `safety: 13`, `doc: 2`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.336
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.104867
  * `Imports (Out-Degree: 5):` fileutils, path, globalcachehelper, cobolglobalcache, externalfeatures, iconfiguration
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/fileutils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.759 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.233 IQR)
- **Top Global Matches:** file_cluster_13: 11.759, file_cluster_0: 11.869, file_cluster_8: 11.89
- **Magnitude:** 52.71 | **LOC:** 261 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (38.0622%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expandLogicalCopyBookOrEmpty` (Impact: 96.5 | O(N^6) | DB: 18)
  * `isDirectPath` (Impact: 57.1 | O(N^4))
  * `isDirectory` (Impact: 56.5 | O(2^N) | DB: 3)
  * `_findCopyBookInDirectory` (Impact: 56.4 | O(N^6) | DB: 9)
  * `findCopyBook` (Impact: 50.5 | O(N^6) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 48`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 30`, `dead_code: 3`
* *Architecture:* `io: 16`, `api: 17`, `import: 4`
* *Defense:* `safety: 4`, `immutability_locks: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.788
  * `Choke Point (Betweenness):` 0.000247 | `Ripple Effect (Closeness):` 0.159484
  * `Imports (Out-Degree: 2):` externalfeatures, fs, iconfiguration, path
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/vsrenameprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.796 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.401 IQR)
- **Top Global Matches:** file_cluster_13: 11.796, file_cluster_8: 11.829, file_cluster_4: 12.047
- **Magnitude:** 52.66 | **LOC:** 201 | **CtrlFlow:** 80.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 30
- **Risk Profile:** Cognitive Load (79.3577%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideRenameEdits` (Impact: 423.9 | O(N^6) | DB: 30)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 13`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 90`
* *Architecture:* `api: 2`, `concurrency: 7`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 59`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 2.4e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 5):` icobolsourcescanner, vscode, vsexternalfeatures, vsconfiguration, vscobolscanner, cobolsourcescanner
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sourceformat.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.305 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.849 IQR)
- **Top Global Matches:** file_cluster_8: 11.305, file_cluster_13: 11.336, file_cluster_0: 11.688
- **Magnitude:** 52.59 | **LOC:** 230 | **CtrlFlow:** 70.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (68.4933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 378.5 | O(N^6) | DB: 15)
  * `isValidFixedLine` (Impact: 45.4 | O(N^4))
  * `getFileFormat` (Impact: 37.5 | O(N^6) | DB: 1)
  * `isNumber` (Impact: 10.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 31`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 48`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 6`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.129
  * `Choke Point (Betweenness):` 5.6e-05 | `Ripple Effect (Closeness):` 0.103242
  * `Imports (Out-Degree: 4):` isourcehandler, cobolKeywords, externalfeatures, glob-to-regexp, iconfiguration
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/cobolsymboltableeventhelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.389 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_13: 14.389, file_cluster_8: 14.725, file_cluster_11: 14.771
- **Magnitude:** 52.01 | **LOC:** 130 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 39
- **Risk Profile:** Cognitive Load (97.5679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processToken` (Impact: 268.0 | O(N^5) | DB: 39)
  * `start` (Impact: 60.9 | O(N^4) | DB: 14)
  * `processRawMessage` (Impact: 7.2 | O(N^3) | DB: 2)
  * `constructor` (Impact: 2.8 | O(N^2) | DB: 2)
  * `finish` (Impact: 1.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 167`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.183
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.007797
  * `Imports (Out-Degree: 7):` icobolsourcescanner, globalcachehelper, cobolglobalcache, cobscannerdata, cobolworkspacecache, cobolsourcescanner, iconfiguration
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vshoverprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.104 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.759 IQR)
- **Top Global Matches:** file_cluster_13: 13.104, file_cluster_11: 13.4, file_cluster_0: 13.44
- **Magnitude:** 46.1 | **LOC:** 190 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (78.7286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideHover` (Impact: 371.2 | O(N^6) | DB: 23)
  * `wrapCommentAndCode` (Impact: 11.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 24`, `args: 2`, `func_start: 2`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `dead_code: 3`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 0.000236 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 7):` icobolsourcescanner, cobolCallTargets, vscode, externalfeatures, vscobolutils, vscobolscanner, cobolsourcescanner, iconfiguration
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/cobscannerdata.ts` (TYPESCRIPT) | Magnitude: 7.18 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, api: 42, structural_boundaries: 24, immutability_locks: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/test/suite/index.ts` (TYPESCRIPT) | Magnitude: 2.71 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 7, args: 6, branch: 5
- `src/vssymbolprovider.ts` (TYPESCRIPT) | Magnitude: 81.68 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 112, branch: 107, immutability_locks: 42
- `src/cobolglobalcache.ts` (TYPESCRIPT) | Magnitude: 13.94 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 34, api: 32, structural_boundaries: 18
- `src/test/runTest.ts` (TYPESCRIPT) | Magnitude: 0.84 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 9, io: 5, structural_boundaries: 3, immutability_locks: 3
- `src/vsrenameprovider.ts` (TYPESCRIPT) | Magnitude: 52.66 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 174, state_mutation: 90, immutability_locks: 59, branch: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/vsterminals.ts` (TYPESCRIPT) | Magnitude: 10.39 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 24, state_mutation: 13, concurrency: 13
- `src/cobollinter.ts` (TYPESCRIPT) | Magnitude: 118.64 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 384, state_mutation: 193, branch: 110, immutability_locks: 75
- `src/vscopybookdragdroprovider.ts` (TYPESCRIPT) | Magnitude: 9.08 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 17, branch: 11, concurrency: 11
- `src/extension.ts` (TYPESCRIPT) | Magnitude: 150.81 | Delta: **0.091 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 574, branch: 138, concurrency: 118, structural_boundaries: 114
- `src/opencopybook.ts` (TYPESCRIPT) | Magnitude: 61.91 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 221, branch: 65, state_mutation: 63, structural_boundaries: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/feedbacktree.ts` (TYPESCRIPT) | Magnitude: 23.67 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 99, branch: 38, structural_boundaries: 14, api: 9
- `src/sourceformat.ts` (TYPESCRIPT) | Magnitude: 52.59 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 171, branch: 73, state_mutation: 48, structural_boundaries: 31
- `src/vssourcedefinitionprovider.ts` (TYPESCRIPT) | Magnitude: 45.96 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 203, state_mutation: 56, branch: 52, immutability_locks: 52
- `src/vsdotmarkdown.ts` (TYPESCRIPT) | Magnitude: 42.49 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 321, state_mutation: 72, structural_boundaries: 58, immutability_locks: 52
- `src/vsfoldingprovider.ts` (TYPESCRIPT) | Magnitude: 56.93 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, branch: 70, state_mutation: 63, structural_boundaries: 24

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cobolsourcescanner.ts` -> Churn: **100.0%** | Cog Load: 92.0453% | Debt: 8.7692%
- `src/vsconfiguration.ts` -> Churn: **90.62%** | Cog Load: 65.739% | Debt: 26.7186%
- `src/vscommon_commands.ts` -> Churn: **77.95%** | Cog Load: 53.6034% | Debt: 0.0%
- `src/extension.ts` -> Churn: **77.6%** | Cog Load: 67.8614% | Debt: 8.1483%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cobolsourcescanner.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 593.29
- `src/vscobolutils.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 252.15
- `src/vssourceviewtree.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 151.42
- `src/extension.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 150.81
- `src/vscobolprovider.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 141.41

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/vscobolutils.ts` -> **Severity: 1.93** (Bridge: 0.023 * Flux: 83.8235%)
- `src/vsconfiguration.ts` -> **Severity: 1.346** (Bridge: 0.0135 * Flux: 99.999%)
- `src/vscobolscanner.ts` -> **Severity: 1.293** (Bridge: 0.0129 * Flux: 100.0%)
- `src/cobolsourcescanner.ts` -> **Severity: 0.833** (Bridge: 0.0083 * Flux: 100.0%)
- `src/vscommon_commands.ts` -> **Severity: 0.502** (Bridge: 0.014 * Flux: 35.8514%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/iconfiguration.ts` -> **Severity: 25.257** (Embedded: 0.3033 * Error Risk: 83.2864%)
- `src/vsconfiguration.ts` -> **Severity: 15.073** (Embedded: 0.1664 * Error Risk: 90.5905%)
- `src/cobolsourcescanner.ts` -> **Severity: 14.144** (Embedded: 0.1433 * Error Risk: 98.6775%)
- `src/cobolglobalcache.ts` -> **Severity: 12.148** (Embedded: 0.1346 * Error Risk: 90.2472%)
- `src/vscobolscanner.ts` -> **Severity: 12.032** (Embedded: 0.1394 * Error Risk: 86.3088%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/externalfeatures.ts` -> **Severity: 22674.2** (Blast Radius: 226.742 * Doc Risk: 100.0%)
- `src/iconfiguration.ts` -> **Severity: 10939.552** (Blast Radius: 189.037 * Doc Risk: 57.8699%)
- `src/isourcehandler.ts` -> **Severity: 10357.913** (Blast Radius: 104.058 * Doc Risk: 99.5398%)
- `src/fileutils.ts` -> **Severity: 1678.8** (Blast Radius: 16.788 * Doc Risk: 100.0%)
- `src/keywords/cobolCallTargets.ts` -> **Severity: 1647.5** (Blast Radius: 16.475 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
