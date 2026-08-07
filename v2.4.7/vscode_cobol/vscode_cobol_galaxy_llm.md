# ARCHITECTURAL_BRIEF: vscode_cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/vscode_cobol` |
| **Timestamp** | `2026-08-07T03:51:24.947590+00:00` |
| **Scan Duration** | `0.71s` |
| **Git Branch** | `main` |
| **Git Commit** | `89d3f07af1062616bf0c433e049f270d0f5e2c4d` |
| **Git Remote** | `https://github.com/spgennard/vscode_cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 91 malicious artifacts.

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
| Modularity | 0.2144 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
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
| Cognitive Load Exposure | 0.0 | 99.1 | 28.6 | 9.6 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 39.5 | 38.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 24.0 | 2.3 | 2.3 |
| API Exposure | 0.0 | 18.3 | 3.8 | 1.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 15.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 39.1 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 73.6 | 2.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 90.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.1 | 1.7 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.7 | 32.2 | 100.0 |
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

- `isParagraph` (@ `src/cobolsourcescanner.ts`) -> Impact: **648.4** | LOC: 927
- `provideCompletionItems` (@ `src/vscobolprovider.ts`) -> Impact: **200.6** | LOC: 210
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `updateDecorations` (@ `src/vsmargindecorations.ts`) -> Impact: **179.4** | LOC: 202
  * *Intent:* // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
- `forkScanner` (@ `src/vscobscanner.ts`) -> Impact: **145.2** | LOC: 188
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `provideDocumentSymbols` (@ `src/vssymbolprovider.ts`) -> Impact: **144.5** | LOC: 154
  * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
- `activate` (@ `src/extension.ts`) -> Impact: **139.2** | LOC: 424
- `provideRenameEdits` (@ `src/vsrenameprovider.ts`) -> Impact: **127.7** | LOC: 183
- `get` (@ `src/sourceformat.ts`) -> Impact: **114.4** | LOC: 174
- `provideHover` (@ `src/vshoverprovider.ts`) -> Impact: **111.2** | LOC: 144
- `foldTokenLine` (@ `src/vscobolutils.ts`) -> Impact: **107.0** | LOC: 103

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 70 | 1643.54 | 52.24% | 14.08% |
| `__monolith__` | 26 | 388.12 | 13.87% | 26.31% |
| `syntaxes` | 21 | 370.2 | 2.2% | 0.0% |
| `snippets` | 6 | 107.14 | 3.61% | 0.0% |
| `syntaxes/markdown` | 6 | 95.4 | 6.85% | 0.0% |
| `src/keywords` | 7 | 53.23 | 9.04% | 14.1% |
| `src/test/suite` | 20 | 36.26 | 2.61% | 0.0% |
| `images` | 3 | 31.56 | 5.0% | 0.0% |
| `images/dark` | 3 | 31.56 | 5.0% | 0.0% |
| `images/light` | 3 | 31.56 | 5.0% | 0.0% |

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
- `src/extension.ts` -> **0** Orphaned Functions | **18** Duplicates
- `src/cobscanner_worker.ts` -> **15** Orphaned Functions | **0** Duplicates
- `src/vscodesourcehandler.ts` -> **0** Orphaned Functions | **14** Duplicates
- `src/cobolglobalcache.ts` -> **0** Orphaned Functions | **10** Duplicates
- `src/vsdotmarkdown.ts` -> **0** Orphaned Functions | **4** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `8` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `120` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/cobscanner_worker.ts` (TYPESCRIPT) -> Cumulative Risk: **687.12**
- **Archetype:** `file_cluster_13` (Distance: 13.942 IQR)
- **Magnitude:** 13.33 | **LOC:** 187 | **CtrlFlow:** 36.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9802%), State Flux (97.4154%)
- **Heaviest Functions:** `logTimedMessage` (Impact: 12.8), `isFile` (Impact: 9.1), `getFileModTimeStamp` (Impact: 8.6)

### 2. `src/vsconfiguration.ts` (TYPESCRIPT) -> Cumulative Risk: **676.06**
- **Archetype:** `file_cluster_8` (Distance: 12.257 IQR)
- **Magnitude:** 54.47 | **LOC:** 695 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.999%), Churn (92.26%)
- **Heaviest Functions:** `getCopybookdirs_defaults` (Impact: 55.5), `initSettings` (Impact: 19.5), `isOutlineEnabled` (Impact: 14.6)

### 3. `src/cobollinter.ts` (TYPESCRIPT) -> Cumulative Risk: **657.03**
- **Archetype:** `file_cluster_4` (Distance: 12.314 IQR)
- **Magnitude:** 53.25 | **LOC:** 477 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9998%), Concurrency (99.1512%), Safety Score (92.5316%)
- **Heaviest Functions:** `updateLinter` (Impact: 76.9), `processScannedDocumentForUnusedSymbols` (Impact: 65.0), `processParsedDocumentForStandards` (Impact: 41.0)

### 4. `src/vssourceviewtree.ts` (TYPESCRIPT) -> Cumulative Risk: **654.9**
- **Archetype:** `file_cluster_4` (Distance: 13.628 IQR)
- **Magnitude:** 83.93 | **LOC:** 500 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9988%), Safety Score (99.7561%)
- **Heaviest Functions:** `addExtension` (Impact: 85.2), `constructor` (Impact: 30.0), `addFolder` (Impact: 24.0)

### 5. `src/vscodesourcehandler.ts` (TYPESCRIPT) -> Cumulative Risk: **654.66**
- **Archetype:** `file_cluster_13` (Distance: 13.414 IQR)
- **Magnitude:** 51.99 | **LOC:** 431 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), Safety Score (98.7572%)
- **Heaviest Functions:** `getLine` (Impact: 41.3), `sendCommentCallback` (Impact: 35.2), `getCommentAtLine` (Impact: 19.2)

### 6. `src/vssymbolprovider.ts` (TYPESCRIPT) -> Cumulative Risk: **650.91**
- **Archetype:** `file_cluster_13` (Distance: 11.81 IQR)
- **Magnitude:** 34.04 | **LOC:** 319 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9991%), Safety Score (90.8995%), Verification (80.0%)
- **Heaviest Functions:** `provideDocumentSymbols` (Impact: 144.5), `provideDocumentSymbols` (Impact: 35.0), `provideDocumentSymbols` (Impact: 25.7)

### 7. `src/tabstopper.ts` (TYPESCRIPT) -> Cumulative Risk: **647.01**
- **Archetype:** `file_cluster_4` (Distance: 12.284 IQR)
- **Magnitude:** 23.57 | **LOC:** 201 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9994%), Concurrency (99.998%), Cognitive Load (96.0273%)
- **Heaviest Functions:** `executeTab` (Impact: 26.3), `singleSelectionUnTab` (Impact: 25.2), `escapeString` (Impact: 12.8)

### 8. `src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **635.71**
- **Archetype:** `file_cluster_4` (Distance: 12.506 IQR)
- **Magnitude:** 63.18 | **LOC:** 882 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9967%), Tech Debt (99.9696%), Cognitive Load (81.0045%)
- **Heaviest Functions:** `activate` (Impact: 139.2), `handleScopedChange` (Impact: 70.9), `setupLogChannel` (Impact: 46.2)

### 9. `src/cobolsourcescanner.ts` (TYPESCRIPT) -> Cumulative Risk: **613.65**
- **Archetype:** `file_cluster_13` (Distance: 14.35 IQR)
- **Magnitude:** 205.18 | **LOC:** 3429 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Churn (100.0%), Safety Score (98.6775%)
- **Heaviest Functions:** `isParagraph` (Impact: 648.4), `newCOBOLToken` (Impact: 87.9), `constructor` (Impact: 56.6)

### 10. `src/cobolsymboltableeventhelper.ts` (TYPESCRIPT) -> Cumulative Risk: **607.49**
- **Archetype:** `file_cluster_13` (Distance: 14.389 IQR)
- **Magnitude:** 30.37 | **LOC:** 130 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8424%)
- **Heaviest Functions:** `processToken` (Impact: 92.0), `start` (Impact: 24.9), `processRawMessage` (Impact: 3.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/cobolsourcescanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.35 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.445 IQR)
- **Top Global Matches:** file_cluster_13: 14.35, file_cluster_8: 14.399, file_cluster_11: 14.428
- **Magnitude:** 205.18 | **LOC:** 3429 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (91.6974%), Tech Debt (8.7692%)
**Top Internal Functions/Classes:**
  * `isParagraph` (Impact: 648.4)
  * `newCOBOLToken` (Impact: 87.9)
  * `constructor` (Impact: 56.6)
  * `processCopyBook` (Impact: 49.2)
  * `processComment` (Impact: 36.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 427`, `structural_boundaries: 57`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `state_mutation: 958`, `dead_code: 13`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 5`, `api: 34`, `import: 13`
* *Defense:* `safety: 16`, `doc: 5`, `immutability_locks: 150`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.9
  * `Choke Point (Betweenness):` 0.008327 | `Ripple Effect (Closeness):` 0.143337
  * `Imports (Out-Degree: 12):` externalfeatures, sourceformat, isourcehandler, iconfiguration, path, filesourcehandler, icobolsourcescanner, extensionDefaults...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/vscobolutils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.637 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.415 IQR)
- **Top Global Matches:** file_cluster_13: 12.637, file_cluster_8: 12.72, file_cluster_11: 12.737
- **Magnitude:** 106.34 | **LOC:** 1439 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.7184%), Tech Debt (15.137%)
**Top Internal Functions/Classes:**
  * `foldTokenLine` (Impact: 107.0)
  * `setupFilePaths` (Impact: 104.8)
  * `setupUrlPaths` (Impact: 52.6)
  * `enforceFileExtensions` (Impact: 52.2)
  * `saveGlobalCacheToWorkspace` (Impact: 48.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 272`, `structural_boundaries: 104`, `args: 68`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `state_mutation: 216`, `dead_code: 10`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 58`, `concurrency: 19`, `import: 22`
* *Defense:* `safety: 30`, `doc: 2`, `immutability_locks: 217`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.165
  * `Choke Point (Betweenness):` 0.023029 | `Ripple Effect (Closeness):` 0.125802
  * `Imports (Out-Degree: 19):` vsexternalfeatures, vscobolscanner, globalcachehelper, vscommon_commands, externalfeatures, path, iconfiguration, vsconfiguration...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/vssourceviewtree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.628 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.353 IQR)
- **Top Global Matches:** file_cluster_4: 13.628, file_cluster_13: 13.859, file_cluster_8: 13.943
- **Magnitude:** 83.93 | **LOC:** 500 | **CtrlFlow:** 75.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.4804%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addExtension` (Impact: 85.2)
  * `constructor` (Impact: 30.0)
  * `addFolder` (Impact: 24.0)
  * `getItemsFromMap` (Impact: 23.7)
  * `setupSourceViewTree` (Impact: 19.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 40`, `args: 29`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `state_mutation: 457`
* *Architecture:* `io: 2`, `api: 10`, `concurrency: 74`, `import: 8`
* *Defense:* `safety: 9`, `immutability_locks: 37`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 6):` vslogger, vscode, iconfiguration, vscobolfolders, vssourcescannerutils, vscobolutils, sourceItem
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsformatconverter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.168 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.061 IQR)
- **Top Global Matches:** file_cluster_8: 12.168, file_cluster_7: 12.475, file_cluster_13: 12.505
- **Magnitude:** 70.08 | **LOC:** 1366 | **CtrlFlow:** 71.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (33.2484%), Tech Debt (14.0596%)
**Top Internal Functions/Classes:**
  * `convertFreeToFixed` (Impact: 44.5)
  * `convertFreeToVariable` (Impact: 43.8)
    * *Intent:* // ============================================================================ // Main conversion f...
  * `convertSourceFormat` (Impact: 40.5)
  * `convertSource` (Impact: 37.4)
  * `convertFixedToFree` (Impact: 26.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 215`, `structural_boundaries: 84`, `args: 35`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `state_mutation: 219`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 5`, `import: 8`
* *Defense:* `safety: 5`, `doc: 46`, `immutability_locks: 118`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.105
  * `Choke Point (Betweenness):` 0.000109 | `Ripple Effect (Closeness):` 0.064474
  * `Imports (Out-Degree: 7):` vsexternalfeatures, externalfeatures, sourceformat, vscode, vscodesourcehandler, vslogger, vsconfiguration, vsextutis
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/extension.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.506 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.944 IQR)
- **Top Global Matches:** file_cluster_4: 12.506, file_cluster_13: 12.572, file_cluster_11: 12.832
- **Magnitude:** 63.18 | **LOC:** 882 | **CtrlFlow:** 54.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.0045%), Tech Debt (99.9696%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 139.2)
  * `handleScopedChange` (Impact: 70.9)
  * `setupLogChannel` (Impact: 46.2)
  * `activateDesktop` (Impact: 34.7)
  * `openChangeLog` (Impact: 15.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 138`, `structural_boundaries: 114`, `args: 62`, `func_start: 32`
* *Risk/State:* `state_mutation: 95`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 18`
* *Architecture:* `io: 5`, `api: 6`, `concurrency: 103`, `import: 46`
* *Defense:* `safety: 13`, `doc: 8`, `immutability_locks: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 42):` tabstopper, vsexternalfeatures, os, core, bmspreviewpanel, vscobolscanner, vscobolutils, vscobolcalltargetprovider...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vscobolprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.061 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.731 IQR)
- **Top Global Matches:** file_cluster_13: 12.061, file_cluster_8: 12.19, file_cluster_11: 12.4
- **Magnitude:** 56.46 | **LOC:** 510 | **CtrlFlow:** 76.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (74.3873%), Tech Debt (8.4593%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 200.6)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getItemsFromList` (Impact: 41.0)
  * `getAllTypes` (Impact: 40.5)
  * `getConstantsOrVariables` (Impact: 25.6)
  * `getAllConstantsOrVariables` (Impact: 25.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 48`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 160`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 6`, `import: 12`
* *Defense:* `doc: 5`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 5.3e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, vsexternalfeatures, vscode, vslogger, iconfiguration, vsconfiguration, icobolsourcescanner...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vssnippetprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.717 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.62 IQR)
- **Top Global Matches:** file_cluster_8: 10.717, file_cluster_7: 11.277, file_cluster_13: 11.448
- **Magnitude:** 55.83 | **LOC:** 1825 | **CtrlFlow:** 79.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.4071%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `provideCompletionItems` (Impact: 53.0)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getExactCallSnipetOrPartialSnippet` (Impact: 41.4)
  * `addSnippet` (Impact: 39.1)
  * `getCompletionItemForAPI` (Impact: 30.5)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `getExactFunctionSnipetOrPartialSnippet` (Impact: 27.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 45`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 203`
* *Architecture:* `api: 13`, `import: 11`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 76`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.257
  * `Choke Point (Betweenness):` 0.000628 | `Ripple Effect (Closeness):` 0.013158
  * `Imports (Out-Degree: 10):` cobolsourcescanner, vsexternalfeatures, vscode, iconfiguration, cobolCallTargets, vsconfiguration, icobolsourcescanner, extensionDefaults...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsconfiguration.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.257 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 3.804 IQR)
- **Top Global Matches:** file_cluster_8: 12.257, file_cluster_13: 12.313, file_cluster_11: 12.544
- **Magnitude:** 54.47 | **LOC:** 695 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.739%), Tech Debt (26.7186%)
**Top Internal Functions/Classes:**
  * `getCopybookdirs_defaults` (Impact: 55.5)
  * `initSettings` (Impact: 19.5)
  * `isOutlineEnabled` (Impact: 14.6)
  * `clearResourceCache` (Impact: 12.1)
  * `getmetadata_files` (Impact: 10.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 67`, `args: 38`, `func_start: 37`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 196`, `dead_code: 2`, `duplicate_logic: 3`
* *Architecture:* `api: 44`, `import: 6`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 41`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.785
  * `Choke Point (Betweenness):` 0.013456 | `Ripple Effect (Closeness):` 0.166384
  * `Imports (Out-Degree: 5):` externalfeatures, vscode, iconfiguration, extensionDefaults, vscobolutils, fileutils
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `src/cobollinter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.314 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.82 IQR)
- **Top Global Matches:** file_cluster_4: 12.314, file_cluster_8: 12.363, file_cluster_13: 12.368
- **Magnitude:** 53.25 | **LOC:** 477 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.3157%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateLinter` (Impact: 76.9)
  * `processScannedDocumentForUnusedSymbols` (Impact: 65.0)
  * `processParsedDocumentForStandards` (Impact: 41.0)
  * `findCopyBookDirectory` (Impact: 40.9)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideCodeActions` (Impact: 28.0)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 110`, `structural_boundaries: 41`, `args: 14`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 193`
* *Architecture:* `io: 4`, `api: 9`, `concurrency: 36`, `import: 13`
* *Defense:* `safety: 8`, `doc: 2`, `immutability_locks: 75`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.033
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, vsexternalfeatures, vscode, iconfiguration, path, vsconfiguration, icobolsourcescanner...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `publish.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.827 IQR)
- **Top Global Matches:** file_cluster_8: 10.827, file_cluster_7: 11.408, file_cluster_13: 11.461
- **Magnitude:** 53.04 | **LOC:** 55 | **CtrlFlow:** 81.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (94.3188%), Tech Debt (99.4718%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block_[Truncated]` (Impact: 28.4)
  * `__global_context__` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 7`, `args: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 15`, `orphaned_logic: 2`
* *Architecture:* `io: 1`
* *Defense:* `sync_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vscodesourcehandler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.414 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.17 IQR)
- **Top Global Matches:** file_cluster_13: 13.414, file_cluster_11: 13.616, file_cluster_8: 13.675
- **Magnitude:** 51.99 | **LOC:** 431 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.7957%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 41.3)
  * `sendCommentCallback` (Impact: 35.2)
  * `getCommentAtLine` (Impact: 19.2)
  * `getLineTabExpanded` (Impact: 15.1)
  * `getLineTabExpanded` (Impact: 15.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 78`, `structural_boundaries: 56`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `state_mutation: 280`, `dead_code: 2`, `planned_debt: 2`, `duplicate_logic: 14`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `safety: 10`, `doc: 2`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.142
  * `Choke Point (Betweenness):` 0.002591 | `Ripple Effect (Closeness):` 0.09464
  * `Imports (Out-Degree: 9):` stringutils, externalfeatures, vsexternalfeatures, extension, vscode, isourcehandler, iconfiguration, vscolourcomments...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/filesourcehandler.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.039 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.171 IQR)
- **Top Global Matches:** file_cluster_13: 13.039, file_cluster_8: 13.122, file_cluster_11: 13.303
- **Magnitude:** 44.63 | **LOC:** 378 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (86.5936%), Tech Debt (10.248%)
**Top Internal Functions/Classes:**
  * `getLine` (Impact: 43.2)
  * `sendCommentCallback` (Impact: 35.1)
  * `constructor` (Impact: 22.3)
  * `getCommentAtLine` (Impact: 19.2)
  * `getText` (Impact: 17.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 43`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 217`, `planned_debt: 2`
* *Architecture:* `io: 8`, `api: 21`, `import: 9`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.308
  * `Choke Point (Betweenness):` 0.000761 | `Ripple Effect (Closeness):` 0.100292
  * `Imports (Out-Degree: 6):` stringutils, externalfeatures, isourcehandler, path, fs, iconfiguration, url, extensionDefaults...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/bmspreviewpanel.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.154 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.139 IQR)
- **Top Global Matches:** file_cluster_8: 11.154, file_cluster_2: 11.51, file_cluster_13: 11.605
- **Magnitude:** 34.98 | **LOC:** 651 | **CtrlFlow:** 53.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (43.3933%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseField` (Impact: 59.4)
  * `parseBms` (Impact: 59.3)
  * `constructor` (Impact: 14.1)
  * `updatePreview` (Impact: 9.5)
  * `createOrShow` (Impact: 8.2)
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

### `src/vssymbolprovider.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.81 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.357 IQR)
- **Top Global Matches:** file_cluster_13: 11.81, file_cluster_8: 11.817, file_cluster_4: 11.926
- **Magnitude:** 34.04 | **LOC:** 319 | **CtrlFlow:** 79.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (79.6375%), Tech Debt (59.4986%)
**Top Internal Functions/Classes:**
  * `provideDocumentSymbols` (Impact: 144.5)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 35.0)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `provideDocumentSymbols` (Impact: 25.7)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 27`, `args: 5`, `func_start: 3`, `class_start: 3`
* *Risk/State:* `state_mutation: 112`, `duplicate_logic: 3`
* *Architecture:* `api: 6`, `concurrency: 12`, `import: 8`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 42`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 7):` cobolsourcescanner, vsexternalfeatures, vscode, vslogger, iconfiguration, vsconfiguration, vscobolscanner, splittoken
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobolsymboltableeventhelper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.389 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.667 IQR)
- **Top Global Matches:** file_cluster_13: 14.389, file_cluster_8: 14.725, file_cluster_11: 14.771
- **Magnitude:** 30.37 | **LOC:** 130 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.5679%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processToken` (Impact: 92.0)
  * `start` (Impact: 24.9)
  * `processRawMessage` (Impact: 3.7)
  * `constructor` (Impact: 1.9)
  * `finish` (Impact: 1.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 12`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 167`
* *Architecture:* `api: 10`, `import: 7`
* *Defense:* `safety: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.183
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.007797
  * `Imports (Out-Degree: 7):` cobolsourcescanner, iconfiguration, icobolsourcescanner, cobolworkspacecache, cobscannerdata, cobolglobalcache, globalcachehelper
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsmargindecorations.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.197 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.281 IQR)
- **Top Global Matches:** file_cluster_13: 11.197, file_cluster_8: 11.294, file_cluster_4: 11.562
- **Magnitude:** 28.17 | **LOC:** 280 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (88.9119%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateDecorations` (Impact: 179.4)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/explicit-module-boundary-types
  * `updateJCLDecorations` (Impact: 6.8)
  * `isEnabledViaWorkspace4jcl` (Impact: 6.6)
  * `setupTags` (Impact: 1.9)
  * `constructor` (Impact: 1.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 24`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 67`
* *Architecture:* `api: 6`, `concurrency: 8`, `import: 11`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.104
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.011696
  * `Imports (Out-Degree: 10):` externalfeatures, vsexternalfeatures, vscodesourcehandler, vscode, sourceformat, iconfiguration, vscolourcomments, vscobolfolders...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/opencopybook.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.044 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.254 IQR)
- **Top Global Matches:** file_cluster_4: 11.044, file_cluster_13: 11.143, file_cluster_8: 11.282
- **Magnitude:** 26.93 | **LOC:** 295 | **CtrlFlow:** 58.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (85.6695%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `resolveDefinitionsFallback` (Impact: 56.4)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `resolveDefinitions` (Impact: 30.6)
  * `expandLogicalCopyBookOrEmpty` (Impact: 29.1)
  * `extractCopyBookFilename` (Impact: 23.5)
  * `getURIForCopybookInDirectory` (Impact: 8.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 63`
* *Architecture:* `io: 8`, `api: 5`, `concurrency: 37`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.824
  * `Choke Point (Betweenness):` 0.003186 | `Ripple Effect (Closeness):` 0.112128
  * `Imports (Out-Degree: 8):` externalfeatures, vsexternalfeatures, vscode, vslogger, path, iconfiguration, vsconfiguration, icobolsourcescanner...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/cobolworkspacecache.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.22%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.013 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.469 IQR)
- **Top Global Matches:** file_cluster_13: 12.013, file_cluster_8: 12.154, file_cluster_0: 12.248
- **Magnitude:** 26.58 | **LOC:** 295 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.8333%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addSymbolToCache` (Impact: 24.8)
  * `loadGlobalTypesCacheFromArray` (Impact: 23.1)
  * `addCalableSymbol` (Impact: 19.8)
  * `addClass` (Impact: 18.5)
  * `removeAllProgramSymbols` (Impact: 14.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 21`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 57`, `dead_code: 2`
* *Architecture:* `io: 4`, `api: 23`, `import: 6`
* *Defense:* `safety: 13`, `doc: 2`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.336
  * `Choke Point (Betweenness):` 0.000113 | `Ripple Effect (Closeness):` 0.104867
  * `Imports (Out-Degree: 5):` externalfeatures, path, iconfiguration, cobolglobalcache, fileutils, globalcachehelper
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `syntaxes/openesql.tmLanguage.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 25.5 | **LOC:** 526 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `snippets/cobol.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 25.38 | **LOC:** 520 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.993
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/vscobolscanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.466 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.773 IQR)
- **Top Global Matches:** file_cluster_13: 13.466, file_cluster_11: 13.804, file_cluster_0: 13.829
- **Magnitude:** 25.24 | **LOC:** 226 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.4302%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getCachedObject` (Impact: 59.4)
  * `processToken` (Impact: 46.0)
  * `start` (Impact: 18.6)
  * `removeCachedObject` (Impact: 5.7)
  * `clearCOBOLCache` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 2`
* *Risk/State:* `state_mutation: 95`, `dead_code: 2`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 16`, `doc: 2`, `immutability_locks: 18`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.409
  * `Choke Point (Betweenness):` 0.01293 | `Ripple Effect (Closeness):` 0.139403
  * `Imports (Out-Degree: 10):` cobolsourcescanner, vsexternalfeatures, vscodesourcehandler, vscode, vslogger, iconfiguration, icobolsourcescanner, cobolworkspacecache...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/vsdotmarkdown.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.0 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.628 IQR)
- **Top Global Matches:** file_cluster_8: 11.0, file_cluster_4: 11.037, file_cluster_13: 11.239
- **Magnitude:** 24.69 | **LOC:** 416 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.6271%), Tech Debt (58.8349%)
**Top Internal Functions/Classes:**
  * `generate_partial_graph` (Impact: 30.8)
  * `view_dot_callgraph` (Impact: 23.8)
  * `getProgramName` (Impact: 12.6)
  * `newFile_dot_callgraph` (Impact: 10.2)
  * `getCurrentProgramCallGraph` (Impact: 9.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 58`, `args: 22`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 72`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 8`, `concurrency: 36`, `import: 7`
* *Defense:* `safety: 10`, `immutability_locks: 52`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.105
  * `Choke Point (Betweenness):` 2.1e-05 | `Ripple Effect (Closeness):` 0.064474
  * `Imports (Out-Degree: 4):` cobolsourcescanner, mermaid.esm.min.mjs, vscode, iconfiguration, fs, icobolsourcescanner, vscobolscanner
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsfileutils.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.504 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 4.451 IQR)
- **Top Global Matches:** file_cluster_8: 9.504, file_cluster_4: 9.592, file_cluster_13: 9.665
- **Magnitude:** 23.96 | **LOC:** 292 | **CtrlFlow:** 55.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (34.1279%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getShortWorkspaceFilename` (Impact: 23.5)
  * `getFullWorkspaceFilename` (Impact: 19.0)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/ban-types
  * `_findCopyBookInDirectory` (Impact: 17.3)
  * `_findCopyBookInDirectoryViaURL` (Impact: 17.2)
  * `validateInput` (Impact: 16.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 52`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 12`, `dead_code: 1`
* *Architecture:* `io: 16`, `api: 20`, `concurrency: 16`, `import: 6`
* *Defense:* `safety: 1`, `doc: 2`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.687
  * `Choke Point (Betweenness):` 4.8e-05 | `Ripple Effect (Closeness):` 0.124286
  * `Imports (Out-Degree: 3):` externalfeatures, vscode, path, fs, iconfiguration, vscobolfolders
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/vscobscanner.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.941 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.345 IQR)
- **Top Global Matches:** file_cluster_13: 9.941, file_cluster_8: 10.008, file_cluster_4: 10.299
- **Magnitude:** 23.62 | **LOC:** 295 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.9615%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `forkScanner` (Impact: 145.2)
    * *Intent:* // eslint-disable-next-line @typescript-eslint/no-unused-vars
  * `processAllFilesInWorkspaceOutOfProcess` (Impact: 16.3)
  * `getScanData` (Impact: 12.6)
  * `clearTimeout` (Impact: 4.6)
  * `getCobScannerDirectory` (Impact: 4.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 33`, `args: 9`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 9`, `api: 5`, `concurrency: 21`, `import: 17`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.033
  * `Choke Point (Betweenness):` 7.7e-05 | `Ripple Effect (Closeness):` 0.005848
  * `Imports (Out-Degree: 13):` makedeps, opencopybook, child_process, externalfeatures, extension, vscode, vslogger, path...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tabstopper.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.284 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.295 IQR)
- **Top Global Matches:** file_cluster_4: 12.284, file_cluster_13: 12.565, file_cluster_8: 12.578
- **Magnitude:** 23.57 | **LOC:** 201 | **CtrlFlow:** 65.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.0273%), Tech Debt (10.0529%)
**Top Internal Functions/Classes:**
  * `executeTab` (Impact: 26.3)
  * `singleSelectionUnTab` (Impact: 25.2)
  * `escapeString` (Impact: 12.8)
  * `cobolUnTabSize` (Impact: 11.6)
  * `getTabsForLine` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 21`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 77`, `planned_debt: 1`
* *Architecture:* `api: 7`, `concurrency: 30`, `import: 4`
* *Defense:* `safety: 9`, `immutability_locks: 37`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.146
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.064879
  * `Imports (Out-Degree: 3):` iconfiguration, vsexternalfeatures, vsconfiguration, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/cobscannerdata.ts` (TYPESCRIPT) | Magnitude: 6.29 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 56, api: 42, structural_boundaries: 24, immutability_locks: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/test/suite/index.ts` (TYPESCRIPT) | Magnitude: 2.46 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 22, structural_boundaries: 7, args: 6, branch: 5
- `src/vssymbolprovider.ts` (TYPESCRIPT) | Magnitude: 34.04 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 246, state_mutation: 112, branch: 107, immutability_locks: 42
- `src/cobolglobalcache.ts` (TYPESCRIPT) | Magnitude: 11.58 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 63, state_mutation: 34, api: 32, structural_boundaries: 18
- `src/test/runTest.ts` (TYPESCRIPT) | Magnitude: 0.84 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 9, io: 5, structural_boundaries: 3, immutability_locks: 3
- `src/vsrenameprovider.ts` (TYPESCRIPT) | Magnitude: 23.04 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 174, state_mutation: 90, immutability_locks: 59, branch: 55

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/vsterminals.ts` (TYPESCRIPT) | Magnitude: 7.28 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 24, state_mutation: 13, concurrency: 13
- `src/cobollinter.ts` (TYPESCRIPT) | Magnitude: 53.25 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 384, state_mutation: 193, branch: 110, immutability_locks: 75
- `src/extension.ts` (TYPESCRIPT) | Magnitude: 63.18 | Delta: **0.066 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 574, branch: 138, structural_boundaries: 114, concurrency: 103
- `src/vscopybookdragdroprovider.ts` (TYPESCRIPT) | Magnitude: 5.17 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 17, branch: 11, concurrency: 11
- `src/opencopybook.ts` (TYPESCRIPT) | Magnitude: 26.93 | Delta: **0.099 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 221, branch: 65, state_mutation: 63, structural_boundaries: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/feedbacktree.ts` (TYPESCRIPT) | Magnitude: 10.55 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 99, branch: 38, structural_boundaries: 14, api: 9
- `src/sourceformat.ts` (TYPESCRIPT) | Magnitude: 20.36 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 171, branch: 73, state_mutation: 48, structural_boundaries: 31
- `src/vssourcedefinitionprovider.ts` (TYPESCRIPT) | Magnitude: 19.85 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 203, state_mutation: 56, branch: 52, immutability_locks: 52
- `src/vsdotmarkdown.ts` (TYPESCRIPT) | Magnitude: 24.69 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 321, state_mutation: 72, structural_boundaries: 58, immutability_locks: 52
- `src/vsfoldingprovider.ts` (TYPESCRIPT) | Magnitude: 23.25 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 165, branch: 70, state_mutation: 63, structural_boundaries: 24

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/cobolsourcescanner.ts` -> Churn: **100.0%** | Cog Load: 91.6974% | Debt: 8.7692%
- `src/vsconfiguration.ts` -> Churn: **92.26%** | Cog Load: 65.739% | Debt: 26.7186%
- `src/vscommon_commands.ts` -> Churn: **79.35%** | Cog Load: 53.6034% | Debt: 54.334%
- `src/extension.ts` -> Churn: **79.0%** | Cog Load: 81.0045% | Debt: 99.9696%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cobolsourcescanner.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 205.18
- `src/vscobolutils.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 106.34
- `src/vssourceviewtree.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 83.93
- `src/vsformatconverter.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 70.08
- `src/extension.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 63.18

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
- `src/isourcehandler.ts` -> **Severity: 10171.701** (Blast Radius: 104.058 * Doc Risk: 97.7503%)
- `src/iconfiguration.ts` -> **Severity: 8115.491** (Blast Radius: 189.037 * Doc Risk: 42.9307%)
- `src/fileutils.ts` -> **Severity: 1678.8** (Blast Radius: 16.788 * Doc Risk: 100.0%)
- `src/keywords/cobolCallTargets.ts` -> **Severity: 1647.5** (Blast Radius: 16.475 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
