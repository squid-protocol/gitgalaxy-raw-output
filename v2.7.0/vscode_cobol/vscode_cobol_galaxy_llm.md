# ARCHITECTURAL_BRIEF: vscode_cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spgennard/vscode_cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 217 |
| Analyzed Artifacts (Scanned) | 174 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 43 |
| Total LOC | 25866 |
| Volatility Index | 0.023 |
| % Scanned of codebase = | 80.2% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2038 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3737 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 13.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1376 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 82 | 20490 | 47.1% |
| JSON | 50 | 4847 | 28.7% |
| PLAINTEXT | 17 | 0 | 9.8% |
| XML | 10 | 0 | 5.7% |
| SHELL | 8 | 167 | 4.6% |
| MARKDOWN | 4 | 0 | 2.3% |
| CSS | 1 | 224 | 0.6% |
| COBOL | 1 | 11 | 0.6% |
| JAVASCRIPT | 1 | 127 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 153 | 87.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 21 | 12.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 43*

**Composition by Extension & Reason:**
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3297 LOC), 1x Excluded (Static Asset Blob without Intent: 2157 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.gif`: 6x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2040 LOC)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3426 commas in 573 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.3 | 22.3 | 5.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.5 | 40.3 | 55.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 22.1 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.3 | 4.8 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 14.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 42.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 73.6 | 2.9 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 52.3 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 9.7 | 1.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 41.1 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 39 | 19 | 1 | `src/cobolsourcescanner.ts` |
| cleanup | 25 | 12 | 0 | `src/vsminimap.ts` |
| guards | 676 | 71 | 11 | `src/cobolsourcescanner.ts` |
| danger | 86 | 32 | 1 | `src/keywords/mf_mfunit.ts` |
| concurrency | 295 | 39 | 5 | `src/extension.ts` |
| connectivity | 941 | 79 | 12 | `src/cobolsourcescanner.ts` |
| io | 250 | 43 | 5 | `gen_changelog.sh` |
| crypto | 1 | 1 | 0 | `webpack.config.js` |
| ipc | 13 | 7 | 0 | `src/cobscanner_worker.ts` |
| time | 18 | 8 | 0 | `src/extension.ts` |
| serialization | 9 | 5 | 0 | `src/bmspreviewpanel.ts` |
| regex | 156 | 36 | 2 | `src/cobolsourcescanner.ts` |
| events | 48 | 17 | 0 | `src/keywords/ile_apis.ts` |
| tests | 3 | 2 | 0 | `src/test/suite/extension.test.ts` |
| docs | 199 | 50 | 3 | `src/vsformatconverter.ts` |
| debt | 62 | 23 | 1 | `src/isourcehandler.ts` |
| mutation | 5896 | 89 | 90 | `src/cobolsourcescanner.ts` |
| dead_code | 101 | 25 | 1 | `src/cobscanner_worker.ts` |
| credential | 5 | 5 | 0 | `images/cobol.svg` |
| threat | 10 | 2 | 0 | `gen_changelog.sh` |
| ml_ai | 16 | 8 | 0 | `src/vssnippetprovider.ts` |
| ui | 38 | 4 | 0 | `src/bmspreviewpanel.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `gen_changelog.sh` (Hits: 18)
- `src/fileutils.ts` (Hits: 16)
- `src/vsfileutils.ts` (Hits: 16)

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

- `processToken` (@ `src/cobolsourcescanner.ts`) -> Impact: **612.4** | LOC: 934
- `constructor` (@ `src/cobolsourcescanner.ts`) -> Impact: **280.2** | LOC: 385
- `provideCompletionItems` (@ `src/vscobolprovider.ts`) -> Impact: **187.1** | LOC: 210
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `forkScanner` (@ `src/vscobscanner.ts`) -> Impact: **139.5** | LOC: 188
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `activateCommonCommands` (@ `src/vscommon_commands.ts`) -> Impact: **126.2** | LOC: 460
- `provideRenameEdits` (@ `src/vsrenameprovider.ts`) -> Impact: **121.0** | LOC: 183
- `provideHover` (@ `src/vshoverprovider.ts`) -> Impact: **109.2** | LOC: 144
- `get` (@ `src/sourceformat.ts`) -> Impact: **104.0** | LOC: 174
- `activate` (@ `src/extension.ts`) -> Impact: **101.8** | LOC: 424
- `provideDocumentSymbols` (@ `src/vssymbolprovider.ts`) -> Impact: **94.3** | LOC: 154
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 70 | 16322.98 | 44.79% | 7.31% |
| `syntaxes` | 21 | 370.2 | 0.0% | 0.0% |
| `src/keywords` | 7 | 366.56 | 7.85% | 0.0% |
| `__monolith__` | 28 | 364.56 | 5.45% | 0.0% |
| `src/web` | 1 | 149.0 | 36.42% | 0.0% |
| `snippets` | 6 | 107.14 | 0.0% | 0.0% |
| `src/test/suite` | 20 | 97.66 | 1.55% | 0.0% |
| `syntaxes/markdown` | 6 | 95.4 | 0.0% | 0.0% |
| `images` | 3 | 31.56 | 0.0% | 0.0% |
| `images/dark` | 3 | 31.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/isourcehandler.ts` -> **100.0%** Exposure
- `src/cobscanner_worker.ts` -> **99.9921%** Exposure
- `src/vscodesourcehandler.ts` -> **99.146%** Exposure
- `src/cobolglobalcache.ts` -> **98.7966%** Exposure
- `src/vslogger.ts` -> **26.8941%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/cobolsourcescanner.ts` -> **100.0%** Exposure
- `src/makedeps.ts` -> **100.0%** Exposure
- `src/splittoken.ts` -> **100.0%** Exposure
- `src/vscobolprovider.ts` -> **100.0%** Exposure
- `src/vsconfiguration.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/cobscanner_worker.ts` -> **16** Orphaned Functions | **0** Duplicates
- `src/isourcehandler.ts` -> **0** Orphaned Functions | **12** Duplicates
- `src/vscodesourcehandler.ts` -> **0** Orphaned Functions | **6** Duplicates
- `src/cobolglobalcache.ts` -> **0** Orphaned Functions | **2** Duplicates
- `src/test/suite/test.cbl` -> **2** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `123` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/vscommon_commands.ts` (TYPESCRIPT) -> Cumulative Risk: **751.28**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 809.56 | **LOC:** 1013 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9991%), State Flux (99.9983%), Documentation (95.4545%)
- **Heaviest Functions:** `activateCommonCommands` (Impact: 126.2), `checkExtensions` (Impact: 68.7), `getExtensionInformation` (Impact: 37.4)

### 2. `src/cobolsourcescanner.ts` (TYPESCRIPT) -> Cumulative Risk: **728.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 3482.28 | **LOC:** 3429 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (97.8261%), Safety Score (96.9262%)
- **Heaviest Functions:** `processToken` (Impact: 612.4), `constructor` (Impact: 280.2), `newCOBOLToken` (Impact: 87.9)

### 3. `src/vsconfiguration.ts` (TYPESCRIPT) -> Cumulative Risk: **720.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 560.34 | **LOC:** 695 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (94.7631%), Documentation (94.3662%)
- **Heaviest Functions:** `getCopybookdirs_defaults` (Impact: 53.5), `initSettings` (Impact: 19.5), `getConfigValue` (Impact: 17.7)

### 4. `src/vscodesourcehandler.ts` (TYPESCRIPT) -> Cumulative Risk: **709.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 311.82 | **LOC:** 431 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9968%), Tech Debt (99.146%), Documentation (91.4894%)
- **Heaviest Functions:** `getLine` (Impact: 41.3), `sendCommentCallback` (Impact: 35.2), `getCommentAtLine` (Impact: 13.2)

### 5. `src/vscobolutils.ts` (TYPESCRIPT) -> Cumulative Risk: **703.38**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1053.5 | **LOC:** 1439 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9971%), Safety Score (85.8756%)
- **Heaviest Functions:** `foldTokenLine` (Impact: 87.2), `setupFilePaths` (Impact: 61.6), `enforceFileExtensions` (Impact: 52.2)

### 6. `src/vssourceviewtree.ts` (TYPESCRIPT) -> Cumulative Risk: **703.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 488.16 | **LOC:** 500 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Concurrency (99.957%)
- **Heaviest Functions:** `addExtension` (Impact: 74.8), `constructor` (Impact: 25.3), `getItemsFromMap` (Impact: 23.7)

### 7. `src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **690.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 629.88 | **LOC:** 882 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.5882%)
- **Heaviest Functions:** `activate` (Impact: 101.8), `handleScopedChange` (Impact: 70.9), `validateInput` (Impact: 35.5)

### 8. `src/cobollinter.ts` (TYPESCRIPT) -> Cumulative Risk: **681.02**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 432.32 | **LOC:** 477 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9996%), Concurrency (94.6981%), Safety Score (88.6079%)
- **Heaviest Functions:** `processScannedDocumentForUnusedSymbols` (Impact: 59.7), `updateLinter` (Impact: 50.6), `findCopyBookDirectory` (Impact: 40.9)

### 9. `src/tabstopper.ts` (TYPESCRIPT) -> Cumulative Risk: **665.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 166.04 | **LOC:** 201 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.8283%), Concurrency (98.8075%)
- **Heaviest Functions:** `executeTab` (Impact: 26.3), `singleSelectionUnTab` (Impact: 25.2), `cobolUnTabSize` (Impact: 11.6)

### 10. `src/vsdotmarkdown.ts` (TYPESCRIPT) -> Cumulative Risk: **651.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 166.34 | **LOC:** 416 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5418%), Concurrency (98.239%)
- **Heaviest Functions:** `generate_partial_graph` (Impact: 28.6), `render` (Impact: 8.6), `_getWebviewContent` (Impact: 5.5)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/cobolsourcescanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3482.28 | **LOC:** 3429 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (90.2841%), Tech Debt (8.17%)
**Top Internal Functions/Classes:**
  * `processToken` (Impact: 612.4)
  * `constructor` (Impact: 280.2)
  * `newCOBOLToken` (Impact: 87.9)
  * `relaxedParseLineByLine` (Impact: 67.3)
  * `addTargetReference` (Impact: 39.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 426 instances
* *State Mutation (weighted view):* 1633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 694`, `structural_boundaries: 308`, `args: 69`, `func_start: 69`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 781`, `dead_code: 17`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 190`, `import: 13`
* *Defense:* `safety: 20`, `doc: 9`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.861
  * `Choke Point (Betweenness):` 0.008135 | `Ripple Effect (Closeness):` 0.14168
  * `Imports (Out-Degree: 12):` cobolglobalcache, cobscannerdata, extensionDefaults, externalfeatures, filesourcehandler, icobolsourcescanner, iconfiguration, isourcehandler...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/vscobolutils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1053.5 | **LOC:** 1439 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (68.0476%), Tech Debt (8.4218%)
**Top Internal Functions/Classes:**
  * `foldTokenLine` (Impact: 87.2)
  * `setupFilePaths` (Impact: 61.6)
  * `enforceFileExtensions` (Impact: 52.2)
  * `saveGlobalCacheToWorkspace` (Impact: 44.5)
  * `runOrDebug` (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 112 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 134`, `args: 68`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `state_mutation: 130`, `dead_code: 15`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 36`, `concurrency: 14`, `import: 22`
* *Defense:* `safety: 14`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.141
  * `Choke Point (Betweenness):` 0.022499 | `Ripple Effect (Closeness):` 0.124348
  * `Imports (Out-Degree: 19):` cobolglobalcache, cobolsourcescanner, extensionDefaults, externalfeatures, fileutils, globalcachehelper, icobolsourcescanner, iconfiguration...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/vscommon_commands.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 809.56 | **LOC:** 1013 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (89.2119%), Tech Debt (10.8836%)
**Top Internal Functions/Classes:**
  * `activateCommonCommands` (Impact: 126.2)
  * `checkExtensions` (Impact: 68.7)
  * `getExtensionInformation` (Impact: 37.4)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-explicit-any
  * `newFile` (Impact: 22.6)
  * `checkForExtensionConflicts` (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 80 instances
* *Concurrency (weighted view):* 144
* *State Mutation (weighted view):* 274
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 189`, `structural_boundaries: 133`, `args: 73`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 114`, `dead_code: 4`, `fragile_debt: 2`
* *Architecture:* `io: 12`, `api: 7`, `concurrency: 44`, `import: 22`
* *Defense:* `safety: 19`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.37
  * `Choke Point (Betweenness):` 0.013693 | `Ripple Effect (Closeness):` 0.084269
  * `Imports (Out-Degree: 18):` cobolprogram, cobolsourcescanner, extensionDefaults, iconfiguration, tabstopper, vscallhierarchyprovider, vscobolfolders, vscobolutils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vsformatconverter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 787.78 | **LOC:** 1366 | **CtrlFlow:** 24.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.9586%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mergeFreeContinuations` (Impact: 41.0)
    * *Intent:* /** * Merge free-format continuation lines (joined with &) starting from the given index. * In free-...
  * `convertSource` (Impact: 31.4)
    * *Intent:* /** * Perform the format conversion from one source format to another. * Returns the new file conten...
  * `analyzeStringLiteralState` (Impact: 28.6)
    * *Intent:* /** * Analyze the given text for unclosed string literals, tracking double and * single quotes indep...
  * `convertSourceFormat` (Impact: 25.9)
    * *Intent:* // ============================================================================ // VS Code command e...
  * `convertFreeToFixed` (Impact: 25.7)
    * *Intent:* /** * Convert from free format to fixed format. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 138`, `args: 38`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `state_mutation: 127`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 8`
* *Defense:* `safety: 2`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 0.000106 | `Ripple Effect (Closeness):` 0.063728
  * `Imports (Out-Degree: 7):` externalfeatures, sourceformat, vscodesourcehandler, vsconfiguration, vsexternalfeatures, vsextutis, vslogger, vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extension.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 629.88 | **LOC:** 882 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.5737%), Tech Debt (8.4436%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 101.8)
  * `handleScopedChange` (Impact: 70.9)
  * `validateInput` (Impact: 35.5)
  * `activateDesktop` (Impact: 34.7)
  * `setupLogChannel` (Impact: 34.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 33 instances
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 118`, `args: 45`, `func_start: 18`
* *Risk/State:* `state_mutation: 61`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 6`, `concurrency: 48`, `import: 46`
* *Defense:* `safety: 9`, `doc: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.985
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` bldTaskProvider, bmspreviewpanel, caseformatter, cobollinter, cobolworkspacecache, commenter, extensionDefaults, feedbacktree...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vsconfiguration.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 560.34 | **LOC:** 695 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.2473%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCopybookdirs_defaults` (Impact: 53.5)
  * `initSettings` (Impact: 19.5)
  * `getConfigValue` (Impact: 17.7)
  * `get_resource_settings_via_uri` (Impact: 9.4)
  * `isOutlineEnabled` (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 73`, `args: 39`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `dead_code: 2`
* *Architecture:* `api: 41`, `import: 6`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.742
  * `Choke Point (Betweenness):` 0.013145 | `Ripple Effect (Closeness):` 0.16446
  * `Imports (Out-Degree: 5):` extensionDefaults, externalfeatures, fileutils, iconfiguration, vscobolutils, vscode
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `src/vscobolprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 552.74 | **LOC:** 510 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (72.2875%), Tech Debt (8.9295%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 187.1)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getItemsFromList` (Impact: 29.8)
  * `getAllTypes` (Impact: 25.1)
  * `getConstantsOrVariables` (Impact: 21.6)
  * `getAllConstantsOrVariables` (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 66 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 142`, `structural_boundaries: 66`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, globalcachehelper, icobolsourcescanner, iconfiguration, vscobolscanner, vsconfiguration, vscustomrules...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vssnippetprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 494.9 | **LOC:** 1825 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.6037%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 48.5)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getExactCallSnipetOrPartialSnippet` (Impact: 41.4)
  * `addSnippet` (Impact: 29.3)
  * `getExactFunctionSnipetOrPartialSnippet` (Impact: 27.8)
  * `getExactDollorOrPartial` (Impact: 27.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 58`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`
* *Architecture:* `api: 9`, `import: 11`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.248
  * `Choke Point (Betweenness):` 0.000614 | `Ripple Effect (Closeness):` 0.013006
  * `Imports (Out-Degree: 10):` cobolsourcescanner, extensionDefaults, icobolsourcescanner, iconfiguration, cobolCallTargets, vscobolscanner, vscobolutils, vsconfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vssourceviewtree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 488.16 | **LOC:** 500 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.2867%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addExtension` (Impact: 74.8)
  * `constructor` (Impact: 25.3)
  * `getItemsFromMap` (Impact: 23.7)
  * `setupSourceViewTree` (Impact: 17.3)
  * `addExtensionIfInList` (Impact: 13.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 53 instances
* *Concurrency (weighted view):* 54
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 113`, `structural_boundaries: 53`, `args: 26`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `state_mutation: 73`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 14`, `import: 8`
* *Defense:* `safety: 4`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 6.7e-05 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 6):` iconfiguration, sourceItem, vscobolfolders, vscobolutils, vslogger, vssourcescannerutils, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobollinter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 432.32 | **LOC:** 477 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.1614%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processScannedDocumentForUnusedSymbols` (Impact: 59.7)
  * `updateLinter` (Impact: 50.6)
  * `findCopyBookDirectory` (Impact: 40.9)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `processParsedDocumentForStandards` (Impact: 35.0)
  * `provideCodeActions` (Impact: 25.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 47 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 149
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 50`, `args: 14`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 16`, `import: 13`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.025
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, icobolsourcescanner, iconfiguration, vscobolscanner, vscobolutils, vsconfiguration, vsexternalfeatures...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bmspreviewpanel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 334.04 | **LOC:** 651 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.0603%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseField` (Impact: 59.4)
  * `parseBms` (Impact: 39.6)
  * `constructor` (Impact: 14.1)
  * `updatePreview` (Impact: 9.5)
  * `createOrShow` (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 150
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 77`, `args: 18`, `func_start: 13`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 56`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 9`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 0):` vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/filesourcehandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 316.56 | **LOC:** 378 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.4192%), Tech Debt (11.0322%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 39.8)
  * `sendCommentCallback` (Impact: 35.1)
  * `constructor` (Impact: 17.9)
  * `getText` (Impact: 17.2)
  * `findShortWorkspaceFilename` (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 52`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `planned_debt: 2`
* *Architecture:* `io: 8`, `api: 20`, `import: 9`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.295
  * `Choke Point (Betweenness):` 0.000743 | `Ripple Effect (Closeness):` 0.099133
  * `Imports (Out-Degree: 6):` extensionDefaults, externalfeatures, iconfiguration, isourcehandler, cobolKeywords, stringutils, fs, path...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vscodesourcehandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 311.82 | **LOC:** 431 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (80.6618%), Tech Debt (99.146%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 41.3)
  * `sendCommentCallback` (Impact: 35.2)
  * `getCommentAtLine` (Impact: 13.2)
  * `getLineTabExpanded` (Impact: 12.6)
  * `getLineTabExpanded` (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 66`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `state_mutation: 55`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.13
  * `Choke Point (Betweenness):` 0.002531 | `Ripple Effect (Closeness):` 0.093546
  * `Imports (Out-Degree: 9):` extension, externalfeatures, iconfiguration, isourcehandler, cobolKeywords, stringutils, vscolourcomments, vsconfiguration...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vssymbolprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 291.6 | **LOC:** 319 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.5286%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideDocumentSymbols` (Impact: 94.3)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 28.1)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 24.0)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 59`, `args: 5`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 44`
* *Architecture:* `api: 6`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 7):` cobolsourcescanner, iconfiguration, splittoken, vscobolscanner, vsconfiguration, vsexternalfeatures, vslogger, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobolworkspacecache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 271.3 | **LOC:** 295 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.0137%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addSymbolToCache` (Impact: 24.8)
  * `addCalableSymbol` (Impact: 19.8)
  * `loadGlobalTypesCacheFromArray` (Impact: 17.1)
  * `removeAllProgramSymbols` (Impact: 14.9)
  * `loadFileCacheFromArray` (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 40`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 34`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 15`, `import: 6`
* *Defense:* `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.323
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.103654
  * `Imports (Out-Degree: 5):` cobolglobalcache, externalfeatures, fileutils, globalcachehelper, iconfiguration, path
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/vscobscanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 253.94 | **LOC:** 295 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (56.0855%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `forkScanner` (Impact: 139.5)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `processAllFilesInWorkspaceOutOfProcess` (Impact: 16.3)
  * `getScanData` (Impact: 12.6)
  * `getCobScannerDirectory` (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 35`, `args: 8`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 33`
* *Architecture:* `io: 9`, `api: 3`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.025
  * `Choke Point (Betweenness):` 7.5e-05 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 13):` cobolglobalcache, cobolworkspacecache, cobscannerdata, extension, extensionDefaults, externalfeatures, globalcachehelper, iconfiguration...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/opencopybook.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 218.6 | **LOC:** 295 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (53.0467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveDefinitionsFallback` (Impact: 56.4)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `resolveDefinitions` (Impact: 30.6)
  * `expandLogicalCopyBookOrEmpty` (Impact: 29.1)
  * `extractCopyBookFilename` (Impact: 23.5)
  * `getURIForCopybookInDirectory` (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 8`, `api: 4`, `concurrency: 12`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.809
  * `Choke Point (Betweenness):` 0.003113 | `Ripple Effect (Closeness):` 0.110832
  * `Imports (Out-Degree: 8):` externalfeatures, icobolsourcescanner, iconfiguration, vscobolscanner, vsconfiguration, vsexternalfeatures, vsfileutils, vslogger...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/vsfileutils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 216.9 | **LOC:** 292 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.4608%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getShortWorkspaceFilename` (Impact: 23.5)
  * `_findCopyBookInDirectory` (Impact: 17.3)
  * `_findCopyBookInDirectoryViaURL` (Impact: 17.2)
  * `getFullWorkspaceFilename` (Impact: 16.8)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/ban-types
  * `findCopyBook` (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 54`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `io: 16`, `api: 11`, `concurrency: 16`, `import: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.669
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.122849
  * `Imports (Out-Degree: 3):` externalfeatures, iconfiguration, vscobolfolders, fs, path, vscode
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/vsrenameprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 200.68 | **LOC:** 201 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.6829%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideRenameEdits` (Impact: 121.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 16`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 5):` cobolsourcescanner, icobolsourcescanner, vscobolscanner, vsconfiguration, vsexternalfeatures, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsfoldingprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 199.76 | **LOC:** 258 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (49.632%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideFoldingRanges` (Impact: 55.4)
  * `addCommentAndBlockFolds` (Impact: 51.3)
    * *Intent:* /** * Lightweight line-based scan to detect: * - Consecutive comment-line blocks * - IF ... END-IF *...
  * `getSignificantText` (Impact: 16.5)
    * *Intent:* /** * Get the significant text from a line, skipping the sequence/indicator area in fixed format. */
  * `isCommentLine` (Impact: 11.1)
    * *Intent:* /** * Determine whether a line is a comment line. * Fixed format: column 7 is '*' or '/' * Free form...
  * `findLastBlock` (Impact: 5.6)
    * *Intent:* /** * Find the last matching block entry on the stack (searching from the top). */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 5):` cobolsourcescanner, externalfeatures, vscobolscanner, vsconfiguration, vsexternalfeatures, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sourceformat.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 189.68 | **LOC:** 230 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (73.1059%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 104.0)
  * `isValidFixedLine` (Impact: 12.0)
  * `getFileFormat` (Impact: 8.0)
  * `isNumber` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 41`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`, `dead_code: 1`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.117
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.102049
  * `Imports (Out-Degree: 4):` externalfeatures, iconfiguration, isourcehandler, cobolKeywords, glob-to-regexp
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vskeywordprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 183.3 | **LOC:** 177 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (69.4365%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getKeywordsGivenPartialWord` (Impact: 69.7)
  * `provideCompletionItems` (Impact: 26.6)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `constructor` (Impact: 3.9)
  * `reFreshConfiguration` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 26`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 0.000149 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 8):` cobolsourcescanner, iconfiguration, cobolKeywords, jclstatements, vsconfiguration, vscustomrules, vsexternalfeatures, vssnippetprovider...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsmargindecorations.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 171.44 | **LOC:** 280 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (76.2579%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateDecorations` (Impact: 92.1)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  * `updateJCLDecorations` (Impact: 6.8)
  * `isEnabledViaWorkspace4jcl` (Impact: 4.8)
  * `constructor` (Impact: 1.2)
  * `setupTags` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 11`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 0.000174 | `Ripple Effect (Closeness):` 0.011561
  * `Imports (Out-Degree: 10):` externalfeatures, iconfiguration, sourceformat, vscobolfolders, vscobolscanner, vscodesourcehandler, vscolourcomments, vsconfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobscanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.92 | **LOC:** 363 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.9519%), Tech Debt (9.4927%)
**Top Internal Functions/Classes:**
  * `processFiles` (Impact: 25.7)
  * `processFileShowFooter` (Impact: 15.1)
  * `cacheUpdateRequired` (Impact: 9.7)
  * `processFileShowHeader` (Impact: 7.5)
  * `sendMessage` (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 42`, `args: 14`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 41`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 15`, `doc: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.226
  * `Choke Point (Betweenness):` 0.000297 | `Ripple Effect (Closeness):` 0.00578
  * `Imports (Out-Degree: 10):` cobolsourcescanner, cobolsymboltableeventhelper, cobolworkspacecache, cobscannerdata, consoleexternalfeatures, externalfeatures, filesourcehandler, globalcachehelper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsdotmarkdown.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 166.34 | **LOC:** 416 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.6489%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generate_partial_graph` (Impact: 28.6)
  * `render` (Impact: 8.6)
  * `_getWebviewContent` (Impact: 5.5)
  * `get_programWindowState` (Impact: 4.0)
  * `constructor` (Impact: 2.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 15 instances
* *Concurrency (weighted view):* 28
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 60`, `args: 23`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `state_mutation: 38`
* *Architecture:* `io: 5`, `api: 7`, `concurrency: 13`, `import: 7`
* *Defense:* `safety: 2`, `immutability_locks: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.097
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.063728
  * `Imports (Out-Degree: 4):` cobolsourcescanner, icobolsourcescanner, iconfiguration, vscobolscanner, fs, mermaid.esm.min.mjs, vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vsconfiguration.ts` -> Churn: **85.83%** | Cog Load: 66.2473% | Debt: 0.0%
- `src/extension.ts` -> Churn: **73.01%** | Cog Load: 86.5737% | Debt: 8.4436%
- `src/cobolsourcescanner.ts` -> Churn: **59.42%** | Cog Load: 90.2841% | Debt: 8.17%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cobolsourcescanner.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 3482.28
- `src/vscobolutils.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 1053.5
- `src/vscommon_commands.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 809.56
- `src/vsformatconverter.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 787.78
- `src/extension.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 629.88

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/vscobolutils.ts` -> **Severity: 2.25** (Bridge: 0.0225 * Flux: 99.9971%)
- `src/vscommon_commands.ts` -> **Severity: 1.369** (Bridge: 0.0137 * Flux: 99.9983%)
- `src/vsconfiguration.ts` -> **Severity: 1.315** (Bridge: 0.0131 * Flux: 100.0%)
- `src/vscobolscanner.ts` -> **Severity: 1.263** (Bridge: 0.0126 * Flux: 99.9739%)
- `src/cobolsourcescanner.ts` -> **Severity: 0.814** (Bridge: 0.0081 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/iconfiguration.ts` -> **Severity: 25.213** (Embedded: 0.2998 * Error Risk: 84.1131%)
- `src/vsconfiguration.ts` -> **Severity: 15.585** (Embedded: 0.1645 * Error Risk: 94.7631%)
- `src/externalfeatures.ts` -> **Severity: 13.988** (Embedded: 0.231 * Error Risk: 60.5532%)
- `src/cobolsourcescanner.ts` -> **Severity: 13.733** (Embedded: 0.1417 * Error Risk: 96.9262%)
- `src/vscobolfolders.ts` -> **Severity: 12.116** (Embedded: 0.1393 * Error Risk: 86.9472%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/iconfiguration.ts` -> **Severity: 18828.6** (Blast Radius: 188.286 * Doc Risk: 100.0%)
- `src/externalfeatures.ts` -> **Severity: 14115.0** (Blast Radius: 225.84 * Doc Risk: 62.5%)
- `src/isourcehandler.ts` -> **Severity: 9893.191** (Blast Radius: 103.643 * Doc Risk: 95.4545%)
- `src/fileutils.ts` -> **Severity: 1672.2** (Blast Radius: 16.722 * Doc Risk: 100.0%)
- `src/keywords/cobolCallTargets.ts` -> **Severity: 1641.0** (Blast Radius: 16.41 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
