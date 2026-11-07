# ARCHITECTURAL_BRIEF: vscode_cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/spgennard/vscode_cobol.git` |
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
- **Scope:** 177 analyzed artifact(s), 25894 LOC.
- **Load-bearing artifact:** `src/iconfiguration.ts` -- 52 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/extension.ts` -- pulls in 45 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/cobolsourcescanner.ts` at magnitude 3693.98 (structural weight, not risk).
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
| Total Artifacts | 217 |
| Analyzed Artifacts (Scanned) | 177 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 40 |
| Total LOC | 25894 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 81.6% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.2076 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3694 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 14.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3794 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 6 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 82 | 20490 | 46.3% |
| JSON | 50 | 4847 | 28.2% |
| PLAINTEXT | 17 | 0 | 9.6% |
| XML | 10 | 0 | 5.6% |
| SHELL | 8 | 167 | 4.5% |
| MARKDOWN | 5 | 0 | 2.8% |
| YAML | 2 | 28 | 1.1% |
| CSS | 1 | 224 | 0.6% |
| COBOL | 1 | 11 | 0.6% |
| JAVASCRIPT | 1 | 127 | 0.6% |

## 4.1 SOURCE ENCODINGS
All 177 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 50%, Large Core Modules (3) 16%, Many-Argument Workhorses Files 8%, Declarative / Non-Code 8%, Compute Cores Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 155 | 87.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 22 | 12.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 40*

**Composition by Extension & Reason:**
- `.png`: 15x Excluded (Explicitly Denied Extension: '.png')
- `.json`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3297 LOC), 1x Excluded (Static Asset Blob without Intent: 2157 LOC)
- `no_extension`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.code-workspace')
- `.gif`: 6x Excluded (Explicitly Denied Extension: '.gif')
- `.ts`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Array/Matrix Payload: 3426 commas in 573 LOC)
- `.md`: 1x Excluded (Lexical Monotony: High structural repetition detected in 2040 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 93.3 | 21.5 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 85.1 | 31.5 | 49.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 3.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 21.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 21.0 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 13.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 97.7 | 5.0 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.0 | 0.8 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 40.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 39 | 19 | 1 | `src/cobolsourcescanner.ts` |
| cleanup | 25 | 12 | 0 | `src/vsminimap.ts` |
| guards | 676 | 71 | 10 | `src/cobolsourcescanner.ts` |
| danger | 86 | 32 | 1 | `src/keywords/mf_mfunit.ts` |
| concurrency | 295 | 39 | 4 | `src/extension.ts` |
| connectivity | 941 | 79 | 11 | `src/cobolsourcescanner.ts` |
| io | 250 | 43 | 5 | `gen_changelog.sh` |
| crypto | 2 | 1 | 0 | `src/cobscanner.ts` |
| ipc | 13 | 7 | 0 | `src/cobscanner_worker.ts` |
| time | 18 | 8 | 0 | `src/extension.ts` |
| serialization | 9 | 5 | 0 | `src/bmspreviewpanel.ts` |
| regex | 156 | 36 | 2 | `src/cobolsourcescanner.ts` |
| events | 50 | 18 | 0 | `src/keywords/ile_apis.ts` |
| tests | 3 | 2 | 0 | `src/test/suite/extension.test.ts` |
| docs | 200 | 51 | 2 | `src/vsformatconverter.ts` |
| debt | 64 | 23 | 1 | `src/isourcehandler.ts` |
| mutation | 5896 | 89 | 87 | `src/cobolsourcescanner.ts` |
| dead_code | 203 | 28 | 1 | `src/vscobolutils.ts` |
| credential | 5 | 5 | 0 | `images/cobol.svg` |
| threat | 0 | 0 | 0 | - |
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
2. **vsexternalfeatures.ts** (`src/vsexternalfeatures.ts`) — 29 inbound connections
3. **vsconfiguration.ts** (`src/vsconfiguration.ts`) — 28 inbound connections
4. **externalfeatures.ts** (`src/externalfeatures.ts`) — 26 inbound connections
5. **cobolsourcescanner.ts** (`src/cobolsourcescanner.ts`) — 23 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **extension.ts** (`src/extension.ts`) — 45 outbound dependencies
2. **extension.ts** (`src/web/extension.ts`) — 25 outbound dependencies
3. **vscobolutils.ts** (`src/vscobolutils.ts`) — 21 outbound dependencies
4. **vscommon_commands.ts** (`src/vscommon_commands.ts`) — 21 outbound dependencies
5. **vscobscanner.ts** (`src/vscobscanner.ts`) — 17 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `processToken` **(Many-Argument Workhorses)** (@ `src/cobolsourcescanner.ts`) -> Impact: **831.9** | LOC: 1164
- `constructor` **(Many-Argument Workhorses)** (@ `src/cobolsourcescanner.ts`) -> Impact: **274.2** | LOC: 385
- `provideCompletionItems` **(Many-Argument Workhorses)** (@ `src/vscobolprovider.ts`) -> Impact: **184.9** | LOC: 210
- `forkScanner` **(Many-Argument Workhorses)** (@ `src/vscobscanner.ts`) -> Impact: **136.7** | LOC: 188
- `provideRenameEdits` **(Many-Argument Workhorses)** (@ `src/vsrenameprovider.ts`) -> Impact: **121.0** | LOC: 183
- `activateCommonCommands` **(Compute Cores)** (@ `src/vscommon_commands.ts`) -> Impact: **119.2** | LOC: 460
- `provideHover` **(Many-Argument Workhorses)** (@ `src/vshoverprovider.ts`) -> Impact: **109.2** | LOC: 144
- `get` **(Many-Argument Workhorses)** (@ `src/sourceformat.ts`) -> Impact: **104.0** | LOC: 174
- `activate` **(Compute Cores)** (@ `src/extension.ts`) -> Impact: **94.7** | LOC: 424
- `provideDocumentSymbols` **(Many-Argument Workhorses)** (@ `src/vssymbolprovider.ts`) -> Impact: **94.3** | LOC: 154

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 70 | 16315.88 | 44.09% | 7.34% |
| `syntaxes` | 21 | 370.2 | 0.0% | 0.0% |
| `src/keywords` | 7 | 366.56 | 3.71% | 0.0% |
| `__monolith__` | 28 | 364.56 | 5.45% | 0.0% |
| `src/web` | 1 | 149.0 | 36.42% | 0.0% |
| `snippets` | 6 | 107.14 | 0.0% | 0.0% |
| `src/test/suite` | 20 | 97.66 | 1.51% | 0.0% |
| `syntaxes/markdown` | 6 | 95.4 | 0.0% | 0.0% |
| `images` | 3 | 31.56 | 0.0% | 0.0% |
| `images/dark` | 3 | 31.56 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/isourcehandler.ts` -> **100.0%** Exposure
- `src/cobscanner_worker.ts` -> **99.9905%** Exposure
- `src/vscodesourcehandler.ts` -> **99.0462%** Exposure
- `src/cobolglobalcache.ts` -> **98.3356%** Exposure
- `src/vscommon_commands.ts` -> **26.2501%** Exposure
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
- `src/vscommon_commands.ts` -> **0** Orphaned Functions | **2** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `117` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/cobolsourcescanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.582)
- **Top Global Matches:** file_cluster_4: 5.582, file_cluster_16: 10.541, file_cluster_15: 10.952
- **Magnitude:** 3693.98 | **LOC:** 3429 | **CtrlFlow:** 24.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **13**; blast radius 9.826; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (90.5%), Connectivity (formerly Api Exposure) (84.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.8261% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processToken` **(Many-Argument Workhorses)** (Impact: 831.9)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 274.2)
  * `newCOBOLToken` **(Many-Argument Workhorses)** (Impact: 87.9)
  * `relaxedParseLineByLine` **(Many-Argument Workhorses)** (Impact: 67.3)
  * `addTargetReference` **(Many-Argument Workhorses)** (Impact: 39.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 426 instances
* *State Mutation (weighted view):* 1633
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 691`, `structural_boundaries: 308`, `args: 69`, `func_start: 69`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 781`, `dead_code: 14`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `io: 9`, `api: 190`, `import: 13`
* *Defense:* `safety: 20`, `doc: 9`, `immutability_locks: 86`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.826
  * `Choke Point (Betweenness):` 0.007463 | `Ripple Effect (Closeness):` 0.146667
  * `Imports (Out-Degree: 12):` cobolglobalcache, cobscannerdata, extensionDefaults, externalfeatures, filesourcehandler, icobolsourcescanner, iconfiguration, isourcehandler...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/vscobolutils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.663)
- **Top Global Matches:** file_cluster_6: 6.663, file_cluster_4: 7.779, file_cluster_16: 15.345
- **Magnitude:** 1041.0 | **LOC:** 1439 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **21**; blast radius 6.061; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Dead Code Surface (formerly Dead Code) (85.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foldTokenLine` **(Many-Argument Workhorses)** (Impact: 87.2)
  * `setupFilePaths` **(Compute Cores)** (Impact: 58.7)
  * `enforceFileExtensions` **(Many-Argument Workhorses)** (Impact: 49.8)
  * `saveGlobalCacheToWorkspace` **(Many-Argument Workhorses)** (Impact: 44.5)
  * `runOrDebug` **(Compute Cores)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 112 instances
* *Concurrency (weighted view):* 24
* *State Mutation (weighted view):* 354
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 134`, `args: 68`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `state_mutation: 130`, `dead_code: 70`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 36`, `concurrency: 14`, `import: 22`
* *Defense:* `safety: 14`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.061
  * `Choke Point (Betweenness):` 0.019234 | `Ripple Effect (Closeness):` 0.122456
  * `Imports (Out-Degree: 19):` cobolglobalcache, cobolsourcescanner, extensionDefaults, externalfeatures, fileutils, globalcachehelper, icobolsourcescanner, iconfiguration...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/vsformatconverter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.063)
- **Top Global Matches:** file_cluster_4: 6.063, file_cluster_6: 9.577, file_cluster_9: 11.216
- **Magnitude:** 785.78 | **LOC:** 1366 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 2.08; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (68.5%)
- **Documentation Coverage:** 3.0303% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mergeFreeContinuations` **(Compute Cores)** (Impact: 41.0)
    * *Intent:* /** * Merge free-format continuation lines (joined with &) starting from the given index. * In free-...
  * `convertSource` **(Compute Cores)** (Impact: 31.4)
    * *Intent:* /** * Perform the format conversion from one source format to another. * Returns the new file conten...
  * `analyzeStringLiteralState` **(Compute Cores)** (Impact: 28.6)
    * *Intent:* /** * Analyze the given text for unclosed string literals, tracking double and * single quotes indep...
  * `convertFreeToFixed` **(Compute Cores)** (Impact: 25.7)
    * *Intent:* /** * Convert from free format to fixed format. */
  * `convertFreeToVariable` **(Compute Cores)** (Impact: 25.0)
    * *Intent:* /** * Convert from free format to variable format. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 359
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 138`, `args: 38`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `state_mutation: 127`
* *Architecture:* `api: 1`, `concurrency: 5`, `import: 8`
* *Defense:* `safety: 2`, `doc: 61`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.08
  * `Choke Point (Betweenness):` 0.000103 | `Ripple Effect (Closeness):` 0.059887
  * `Imports (Out-Degree: 7):` externalfeatures, sourceformat, vscodesourcehandler, vsconfiguration, vsexternalfeatures, vsextutis, vslogger, vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vscommon_commands.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.11)
- **Top Global Matches:** file_cluster_6: 7.11, file_cluster_8: 12.301, file_cluster_4: 13.65
- **Magnitude:** 778.66 | **LOC:** 1013 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **21**; blast radius 2.353; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (88.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 95.4545% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `activateCommonCommands` **(Compute Cores)** (Impact: 119.2)
  * `checkExtensions` **(I/O & Config Routines)** (Impact: 66.7)
  * `getExtensionInformation` **(Compute Cores)** (Impact: 37.4)
  * `newFile` **(Many-Argument Workhorses)** (Impact: 22.6)
  * `checkForExtensionConflicts` **(Defensive Guards)** (Impact: 22.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 20 instances
* *Amplified Cascading Flux:* 77 instances
* *Concurrency (weighted view):* 144
* *State Mutation (weighted view):* 268
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 133`, `args: 73`, `func_start: 16`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 114`, `dead_code: 8`, `fragile_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 12`, `api: 7`, `concurrency: 44`, `import: 22`
* *Defense:* `safety: 19`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.353
  * `Choke Point (Betweenness):` 0.011865 | `Ripple Effect (Closeness):` 0.080437
  * `Imports (Out-Degree: 18):` cobolprogram, cobolsourcescanner, extensionDefaults, iconfiguration, tabstopper, vscallhierarchyprovider, vscobolfolders, vscobolutils...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/extension.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.125)
- **Top Global Matches:** file_cluster_6: 8.125, file_cluster_8: 13.04, file_cluster_4: 14.019
- **Magnitude:** 585.58 | **LOC:** 882 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **45**; blast radius 2.091; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Complexity Load (formerly Cognitive Load) (86.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (73.0%)
- **Documentation Coverage:** 90.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `activate` **(Compute Cores)** (Impact: 94.7)
  * `handleScopedChange` **(Many-Argument Workhorses)** (Impact: 70.9)
  * `activateDesktop` **(Compute Cores)** (Impact: 33.0)
  * `setupLogChannel` **(Many-Argument Workhorses)** (Impact: 32.2)
  * `openChangeLog` **(Compute Cores)** (Impact: 11.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 24 instances
* *Amplified Cascading Flux:* 34 instances
* *Concurrency (weighted view):* 168
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 118`, `args: 45`, `func_start: 18`
* *Risk/State:* `state_mutation: 61`, `dead_code: 18`, `planned_debt: 1`
* *Architecture:* `io: 5`, `api: 6`, `concurrency: 48`, `import: 46`
* *Defense:* `safety: 9`, `doc: 8`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.091
  * `Choke Point (Betweenness):` 0.001312 | `Ripple Effect (Closeness):` 0.005682
  * `Imports (Out-Degree: 41):` bldTaskProvider, bmspreviewpanel, cobollinter, cobolworkspacecache, commenter, extensionDefaults, feedbacktree, globalcachehelper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vsconfiguration.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.562)
- **Top Global Matches:** file_cluster_15: 6.562, file_cluster_4: 7.576, file_cluster_11: 7.816
- **Magnitude:** 560.34 | **LOC:** 695 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **28** in-repo importer(s); it depends on **6**; blast radius 10.291; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (89.0%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (76.6%)
- **Documentation Coverage:** 94.3662% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCopybookdirs_defaults` **(Many-Argument Workhorses)** (Impact: 53.5)
  * `initSettings` **(Many-Argument Workhorses)** (Impact: 19.5)
  * `getConfigValue` **(Stateful Encapsulated Methods)** (Impact: 17.7)
  * `get_resource_settings_via_uri` **(Many-Argument Workhorses)** (Impact: 9.4)
  * `isOutlineEnabled` **(Compute Cores)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 259
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 73`, `args: 39`, `func_start: 38`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 167`, `dead_code: 5`
* *Architecture:* `api: 41`, `import: 6`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.291
  * `Choke Point (Betweenness):` 0.010211 | `Ripple Effect (Closeness):` 0.160873
  * `Imports (Out-Degree: 5):` extensionDefaults, externalfeatures, fileutils, iconfiguration, vscobolutils, vscode
  * `Imported By (In-Degree: 28):` (Excluded from Brief to save tokens)

### `src/vscobolprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.416)
- **Top Global Matches:** file_cluster_6: 6.416, file_cluster_4: 12.385, file_cluster_8: 13.564
- **Magnitude:** 550.54 | **LOC:** 510 | **CtrlFlow:** 33.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 2.082; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.2%), Guard Balance (formerly Safety Score) (71.6%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `provideCompletionItems` **(Many-Argument Workhorses)** (Impact: 184.9)
  * `getItemsFromList` **(Many-Argument Workhorses)** (Impact: 29.8)
  * `getAllTypes` **(Compute Cores)** (Impact: 25.1)
  * `getConstantsOrVariables` **(Stateful Encapsulated Methods)** (Impact: 21.6)
  * `getAllConstantsOrVariables` **(Stateful Encapsulated Methods)** (Impact: 21.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 66 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 205
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 141`, `structural_boundaries: 66`, `args: 12`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 12`
* *Defense:* `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 5.1e-05 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, globalcachehelper, icobolsourcescanner, iconfiguration, vscobolscanner, vsconfiguration, vscustomrules...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vssnippetprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.783)
- **Top Global Matches:** file_cluster_4: 6.783, file_cluster_9: 9.821, file_cluster_6: 11.191
- **Magnitude:** 494.9 | **LOC:** 1825 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 2.233; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.0%), Connectivity (formerly Api Exposure) (14.6%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `provideCompletionItems` **(Many-Argument Workhorses)** (Impact: 48.5)
  * `getExactCallSnipetOrPartialSnippet` **(Many-Argument Workhorses)** (Impact: 41.4)
  * `addSnippet` **(Many-Argument Workhorses)** (Impact: 29.3)
  * `getExactFunctionSnipetOrPartialSnippet` **(Stateful Encapsulated Methods)** (Impact: 27.8)
  * `getExactDollorOrPartial` **(Stateful Encapsulated Methods)** (Impact: 27.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 177
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 58`, `args: 46`, `func_start: 46`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 69`, `dead_code: 1`
* *Architecture:* `api: 9`, `import: 11`
* *Defense:* `safety: 3`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.233
  * `Choke Point (Betweenness):` 0.000658 | `Ripple Effect (Closeness):` 0.015152
  * `Imports (Out-Degree: 10):` cobolsourcescanner, extensionDefaults, icobolsourcescanner, iconfiguration, cobolCallTargets, vscobolscanner, vscobolutils, vsconfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vssourceviewtree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.671)
- **Top Global Matches:** file_cluster_4: 6.671, file_cluster_16: 7.833, file_cluster_15: 8.793
- **Magnitude:** 488.16 | **LOC:** 500 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (93.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addExtension` **(Compute Cores)** (Impact: 74.8)
  * `constructor` **(I/O & Config Routines)** (Impact: 25.3)
  * `getItemsFromMap` **(Compute Cores)** (Impact: 23.7)
  * `setupSourceViewTree` **(Defensive Guards)** (Impact: 17.3)
  * `addExtensionIfInList` **(Stateful Encapsulated Methods)** (Impact: 13.9)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 8.1e-05 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 6):` iconfiguration, sourceItem, vscobolfolders, vscobolutils, vslogger, vssourcescannerutils, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobollinter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.659)
- **Top Global Matches:** file_cluster_8: 6.659, file_cluster_6: 11.68, file_cluster_4: 20.183
- **Magnitude:** 426.02 | **LOC:** 477 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **12**; blast radius 2.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (94.7%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 76.4706% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processScannedDocumentForUnusedSymbols` **(Many-Argument Workhorses)** (Impact: 59.7)
  * `updateLinter` **(Compute Cores)** (Impact: 50.6)
  * `findCopyBookDirectory` **(Many-Argument Workhorses)** (Impact: 40.9)
  * `processParsedDocumentForStandards` **(Many-Argument Workhorses)** (Impact: 33.0)
  * `provideCodeActions` **(Many-Argument Workhorses)** (Impact: 23.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 46 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 147
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 50`, `args: 14`, `func_start: 11`, `class_start: 2`
* *Risk/State:* `state_mutation: 55`
* *Architecture:* `io: 4`, `api: 8`, `concurrency: 16`, `import: 13`
* *Defense:* `safety: 5`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.012
  * `Choke Point (Betweenness):` 1.1e-05 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 10):` cobolsourcescanner, externalfeatures, icobolsourcescanner, iconfiguration, vscobolscanner, vscobolutils, vsconfiguration, vsexternalfeatures...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/filesourcehandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.486)
- **Top Global Matches:** file_cluster_4: 6.486, file_cluster_15: 7.014, file_cluster_11: 8.09
- **Magnitude:** 316.56 | **LOC:** 378 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 3.271; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (85.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%)
- **Documentation Coverage:** 93.0233% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLine` **(Many-Argument Workhorses)** (Impact: 39.8)
  * `sendCommentCallback` **(Many-Argument Workhorses)** (Impact: 35.1)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 17.9)
  * `getText` **(Many-Argument Workhorses)** (Impact: 17.2)
  * `findShortWorkspaceFilename` **(Stateful Encapsulated Methods)** (Impact: 17.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 52`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `state_mutation: 54`, `planned_debt: 2`
* *Architecture:* `io: 8`, `api: 20`, `import: 9`
* *Defense:* `safety: 5`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.271
  * `Choke Point (Betweenness):` 0.000714 | `Ripple Effect (Closeness):` 0.098339
  * `Imports (Out-Degree: 6):` extensionDefaults, externalfeatures, iconfiguration, isourcehandler, cobolKeywords, stringutils, fs, path...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vscodesourcehandler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.21)
- **Top Global Matches:** file_cluster_15: 6.21, file_cluster_11: 7.143, file_cluster_16: 7.253
- **Magnitude:** 311.82 | **LOC:** 431 | **CtrlFlow:** 22.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **10**; blast radius 3.105; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.0%), Complexity Load (formerly Cognitive Load) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 91.4894% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLine` **(Compute Cores)** (Impact: 41.3)
  * `sendCommentCallback` **(Many-Argument Workhorses)** (Impact: 35.2)
  * `getCommentAtLine` **(Compute Cores)** (Impact: 13.2)
  * `getLineTabExpanded` **(Compute Cores)** (Impact: 12.6)
  * `getLineTabExpanded` **(Compute Cores)** (Impact: 12.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 26 instances
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 66`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `state_mutation: 55`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `api: 16`, `import: 11`
* *Defense:* `safety: 2`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.105
  * `Choke Point (Betweenness):` 0.002158 | `Ripple Effect (Closeness):` 0.091162
  * `Imports (Out-Degree: 9):` externalfeatures, iconfiguration, isourcehandler, cobolKeywords, stringutils, vscolourcomments, vsconfiguration, vsexternalfeatures...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vssymbolprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.583)
- **Top Global Matches:** file_cluster_8: 7.583, file_cluster_6: 18.094, file_cluster_3: 19.725
- **Magnitude:** 291.6 | **LOC:** 319 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (79.7%), Complexity Load (formerly Cognitive Load) (74.5%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `provideDocumentSymbols` **(Many-Argument Workhorses)** (Impact: 94.3)
  * `provideDocumentSymbols` **(Compute Cores)** (Impact: 28.1)
  * `provideDocumentSymbols` **(Many-Argument Workhorses)** (Impact: 24.0)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 4.7e-05 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 7):` cobolsourcescanner, iconfiguration, splittoken, vscobolscanner, vsconfiguration, vsexternalfeatures, vslogger, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobolworkspacecache.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.037)
- **Top Global Matches:** file_cluster_15: 6.037, file_cluster_16: 7.1, file_cluster_9: 8.18
- **Magnitude:** 271.3 | **LOC:** 295 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **6**; blast radius 3.29; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (67.0%), Guard Balance (formerly Safety Score) (66.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addSymbolToCache` **(Many-Argument Workhorses)** (Impact: 24.8)
  * `addCalableSymbol` **(Many-Argument Workhorses)** (Impact: 19.8)
  * `loadGlobalTypesCacheFromArray` **(Compute Cores)** (Impact: 17.1)
  * `removeAllProgramSymbols` **(Stateful Encapsulated Methods)** (Impact: 14.9)
  * `loadFileCacheFromArray` **(Many-Argument Workhorses)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 40`, `args: 16`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `state_mutation: 34`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 15`, `import: 6`
* *Defense:* `doc: 2`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.29
  * `Choke Point (Betweenness):` 0.000106 | `Ripple Effect (Closeness):` 0.10124
  * `Imports (Out-Degree: 5):` cobolglobalcache, externalfeatures, fileutils, globalcachehelper, iconfiguration, path
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/bmspreviewpanel.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.931)
- **Top Global Matches:** file_cluster_4: 5.931, file_cluster_6: 9.523, file_cluster_16: 11.661
- **Magnitude:** 251.64 | **LOC:** 651 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 2.012; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.6%), Connectivity (formerly Api Exposure) (38.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseBms` **(Compute Cores)** (Impact: 38.2)
  * `parseField` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `constructor` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `updatePreview` **(Defensive Guards)** (Impact: 9.5)
  * `createOrShow` **(Compute Cores)** (Impact: 8.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 4
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 77`, `args: 18`, `func_start: 13`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 6`, `state_mutation: 56`
* *Architecture:* `api: 19`, `concurrency: 1`, `import: 1`
* *Defense:* `safety: 9`, `immutability_locks: 6`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.012
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 0):` vscode
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vscobscanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.384)
- **Top Global Matches:** file_cluster_8: 8.384, file_cluster_6: 10.184, file_cluster_4: 18.28
- **Magnitude:** 251.14 | **LOC:** 295 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **17**; blast radius 2.012; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Concurrency Surface (formerly Concurrency) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.7%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forkScanner` **(Many-Argument Workhorses)** (Impact: 136.7)
  * `processAllFilesInWorkspaceOutOfProcess` **(Many-Argument Workhorses)** (Impact: 16.3)
  * `getScanData` **(Stateful Encapsulated Methods)** (Impact: 12.6)
  * `getCobScannerDirectory` **(Encapsulated Accessors)** (Impact: 2.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 16
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 35`, `args: 8`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `state_mutation: 33`, `dead_code: 4`
* *Architecture:* `io: 9`, `api: 3`, `concurrency: 11`, `import: 17`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.012
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.005682
  * `Imports (Out-Degree: 14):` cobolglobalcache, cobolworkspacecache, cobscannerdata, extension, extensionDefaults, externalfeatures, globalcachehelper, iconfiguration...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/opencopybook.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.762)
- **Top Global Matches:** file_cluster_6: 7.762, file_cluster_4: 7.869, file_cluster_9: 14.527
- **Magnitude:** 218.6 | **LOC:** 295 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 3.441; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Concurrency Surface (formerly Concurrency) (84.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.4%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveDefinitionsFallback` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `resolveDefinitions` **(Many-Argument Workhorses)** (Impact: 30.6)
  * `expandLogicalCopyBookOrEmpty` **(Many-Argument Workhorses)** (Impact: 29.1)
  * `extractCopyBookFilename` **(Many-Argument Workhorses)** (Impact: 23.5)
  * `getURIForCopybookInDirectory` **(Stateful Encapsulated Methods)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 47`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `state_mutation: 16`
* *Architecture:* `io: 8`, `api: 4`, `concurrency: 12`, `import: 11`
* *Defense:* `safety: 4`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.441
  * `Choke Point (Betweenness):` 0.001556 | `Ripple Effect (Closeness):` 0.101291
  * `Imports (Out-Degree: 8):` externalfeatures, icobolsourcescanner, iconfiguration, vscobolscanner, vsconfiguration, vsexternalfeatures, vsfileutils, vslogger...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/vsfileutils.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.906)
- **Top Global Matches:** file_cluster_9: 5.906, file_cluster_16: 10.588, file_cluster_15: 10.979
- **Magnitude:** 213.0 | **LOC:** 292 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 4.257; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (96.2%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (52.4%), Guard Balance (formerly Safety Score) (51.8%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getShortWorkspaceFilename` **(Compute Cores)** (Impact: 23.5)
  * `_findCopyBookInDirectory` **(Stateful Encapsulated Methods)** (Impact: 17.3)
  * `_findCopyBookInDirectoryViaURL` **(Stateful Encapsulated Methods)** (Impact: 17.2)
  * `getFullWorkspaceFilename` **(Many-Argument Workhorses)** (Impact: 16.8)
  * `findCopyBook` **(Many-Argument Workhorses)** (Impact: 15.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 54`, `args: 14`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 16`, `api: 11`, `concurrency: 16`, `import: 6`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.257
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.113711
  * `Imports (Out-Degree: 3):` externalfeatures, iconfiguration, vscobolfolders, fs, path, vscode
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/vsrenameprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 4.206)
- **Top Global Matches:** file_cluster_1: 4.206, file_cluster_3: 48.099, file_cluster_8: 69.977
- **Magnitude:** 200.68 | **LOC:** 201 | **CtrlFlow:** 28.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.7%), Guard Balance (formerly Safety Score) (65.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `provideRenameEdits` **(Many-Argument Workhorses)** (Impact: 121.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 52`, `structural_boundaries: 16`, `args: 1`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 7`
* *Defense:* `safety: 3`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 5):` cobolsourcescanner, icobolsourcescanner, vscobolscanner, vsconfiguration, vsexternalfeatures, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsfoldingprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.274)
- **Top Global Matches:** file_cluster_8: 6.274, file_cluster_6: 17.239, file_cluster_3: 19.69
- **Magnitude:** 199.76 | **LOC:** 258 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (49.3%)
- **Documentation Coverage:** 28.5714% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `provideFoldingRanges` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `addCommentAndBlockFolds` **(Many-Argument Workhorses)** (Impact: 51.3)
    * *Intent:* /** * Lightweight line-based scan to detect: * - Consecutive comment-line blocks * - IF ... END-IF *...
  * `getSignificantText` **(Stateful Encapsulated Methods)** (Impact: 16.5)
    * *Intent:* /** * Get the significant text from a line, skipping the sequence/indicator area in fixed format. */
  * `isCommentLine` **(Stateful Encapsulated Methods)** (Impact: 11.1)
    * *Intent:* /** * Determine whether a line is a comment line. * Fixed format: column 7 is '*' or '/' * Free form...
  * `findLastBlock` **(Stateful Encapsulated Methods)** (Impact: 5.6)
    * *Intent:* /** * Find the last matching block entry on the stack (searching from the top). */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 49
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 17`
* *Architecture:* `api: 2`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 1`, `doc: 5`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 2e-05 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 5):` cobolsourcescanner, externalfeatures, vscobolscanner, vsconfiguration, vsexternalfeatures, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sourceformat.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.845)
- **Top Global Matches:** file_cluster_8: 7.845, file_cluster_6: 9.722, file_cluster_4: 18.035
- **Magnitude:** 189.68 | **LOC:** 230 | **CtrlFlow:** 36.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **5**; blast radius 3.094; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.1%), Guard Balance (formerly Safety Score) (63.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 104.0)
  * `isValidFixedLine` **(Stateful Encapsulated Methods)** (Impact: 12.0)
  * `getFileFormat` **(Stateful Encapsulated Methods)** (Impact: 8.0)
  * `isNumber` **(Encapsulated Accessors)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 19 instances
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 41`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 19`
* *Architecture:* `api: 2`, `import: 5`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.094
  * `Choke Point (Betweenness):` 5.2e-05 | `Ripple Effect (Closeness):` 0.10182
  * `Imports (Out-Degree: 4):` externalfeatures, iconfiguration, isourcehandler, cobolKeywords, glob-to-regexp
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/vskeywordprovider.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.171)
- **Top Global Matches:** file_cluster_8: 8.171, file_cluster_6: 10.156, file_cluster_4: 18.286
- **Magnitude:** 183.3 | **LOC:** 177 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 2.082; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.9%), Complexity Load (formerly Cognitive Load) (69.4%)
- **Documentation Coverage:** 71.4286% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getKeywordsGivenPartialWord` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `provideCompletionItems` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `constructor` **(State Mutators)** (Impact: 3.9)
  * `reFreshConfiguration` **(State Mutators)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 24 instances
* *State Mutation (weighted view):* 72
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 26`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `state_mutation: 24`
* *Architecture:* `api: 5`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.000176 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 8):` cobolsourcescanner, iconfiguration, cobolKeywords, jclstatements, vsconfiguration, vscustomrules, vsexternalfeatures, vssnippetprovider...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/vsmargindecorations.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.419)
- **Top Global Matches:** file_cluster_6: 7.419, file_cluster_8: 12.805, file_cluster_4: 13.498
- **Magnitude:** 171.44 | **LOC:** 280 | **CtrlFlow:** 27.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 2.082; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.3%), Guard Balance (formerly Safety Score) (60.7%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateDecorations` **(Compute Cores)** (Impact: 92.1)
  * `updateJCLDecorations` **(Stateful Encapsulated Methods)** (Impact: 6.8)
  * `isEnabledViaWorkspace4jcl` **(Stateful Encapsulated Methods)** (Impact: 4.8)
  * `constructor` **(State Mutators)** (Impact: 1.2)
  * `setupTags` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 53
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 33`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 11`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.082
  * `Choke Point (Betweenness):` 0.000199 | `Ripple Effect (Closeness):` 0.012784
  * `Imports (Out-Degree: 10):` externalfeatures, iconfiguration, sourceformat, vscobolfolders, vscobolscanner, vscodesourcehandler, vscolourcomments, vsconfiguration...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/cobscanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 5.693)
- **Top Global Matches:** file_cluster_15: 5.693, file_cluster_16: 7.237, file_cluster_10: 8.486
- **Magnitude:** 166.92 | **LOC:** 363 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **16**; blast radius 2.208; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%), Connectivity (formerly Api Exposure) (47.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processFiles` **(Many-Argument Workhorses)** (Impact: 25.7)
  * `processFileShowFooter` **(Compute Cores)** (Impact: 15.1)
  * `cacheUpdateRequired` **(Defensive Guards)** (Impact: 9.7)
  * `processFileShowHeader` **(Compute Cores)** (Impact: 7.5)
  * `sendMessage` **(Parameter Forwarders)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 73
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 42`, `args: 14`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `state_mutation: 41`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `io: 7`, `api: 13`, `concurrency: 2`, `import: 17`
* *Defense:* `safety: 15`, `doc: 2`, `sync_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.208
  * `Choke Point (Betweenness):` 0.000287 | `Ripple Effect (Closeness):` 0.005682
  * `Imports (Out-Degree: 10):` cobolsourcescanner, cobolsymboltableeventhelper, cobolworkspacecache, cobscannerdata, consoleexternalfeatures, externalfeatures, filesourcehandler, globalcachehelper...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tabstopper.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 5.325)
- **Top Global Matches:** file_cluster_16: 5.325, file_cluster_15: 6.787, file_cluster_11: 7.949
- **Magnitude:** 166.04 | **LOC:** 201 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 2.123; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Concurrency Surface (formerly Concurrency) (98.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeTab` **(Many-Argument Workhorses)** (Impact: 26.3)
  * `singleSelectionUnTab` **(Stateful Encapsulated Methods)** (Impact: 25.2)
  * `cobolUnTabSize` **(Compute Cores)** (Impact: 11.6)
  * `getTabsForLine` **(Stateful Encapsulated Methods)** (Impact: 8.6)
  * `escapeString` **(Stateful Encapsulated Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 12 instances
* *Concurrency (weighted view):* 15
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 29`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `state_mutation: 13`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 10`, `import: 4`
* *Defense:* `safety: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.123
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.060774
  * `Imports (Out-Degree: 3):` iconfiguration, vsconfiguration, vsexternalfeatures, vscode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/sourceItem.ts` (TYPESCRIPT) | Magnitude: 37.04 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 17, api: 8, structural_boundaries: 7, state_mutation: 5
- `src/cobolglobalcache.ts` (TYPESCRIPT) | Magnitude: 106.62 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 63, api: 32, structural_boundaries: 18, branch: 14
- `src/vsexternalfeatures.ts` (TYPESCRIPT) | Magnitude: 65.58 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 85, structural_boundaries: 40, api: 17, args: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/test/runTest.ts` (TYPESCRIPT) | Magnitude: 4.18 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 9, io: 5, structural_boundaries: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/isourcehandler.ts` (TYPESCRIPT) | Magnitude: 69.14 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 37, args: 28, func_start: 28, api: 24
- `src/iconfiguration.ts` (TYPESCRIPT) | Magnitude: 134.22 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 359, state_mutation: 108, structural_boundaries: 20, core_var_decl: 17
- `src/bldTaskProvider.ts` (TYPESCRIPT) | Magnitude: 55.46 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 96, core_var_decl: 28, structural_boundaries: 24, branch: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/doccomment.ts` (TYPESCRIPT) | Magnitude: 15.72 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 6, branch: 4, api: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/opencopybook.ts` (TYPESCRIPT) | Magnitude: 218.6 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 221, branch: 61, core_var_decl: 58, structural_boundaries: 47

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vsconfiguration.ts` -> Churn: **76.61%** | Cog Load: 66.2473% | Debt: 0.0%
- `src/extension.ts` -> Churn: **73.01%** | Cog Load: 86.6677% | Debt: 8.1483%
- `src/cobolsourcescanner.ts` -> Churn: **59.42%** | Cog Load: 90.5103% | Debt: 8.1031%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/cobolsourcescanner.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 3693.98
- `src/vscobolutils.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 1041.0
- `src/vsformatconverter.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 785.78
- `src/vscommon_commands.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 778.66
- `src/extension.ts` -> **spgennard** (100.0% isolated ownership) | Magnitude: 585.58

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/vscobolutils.ts` -> **Severity: 1.923** (Bridge: 0.0192 * Flux: 99.9971%)
- `src/vscommon_commands.ts` -> **Severity: 1.186** (Bridge: 0.0119 * Flux: 99.9978%)
- `src/vscobolscanner.ts` -> **Severity: 1.137** (Bridge: 0.0114 * Flux: 99.9739%)
- `src/vsconfiguration.ts` -> **Severity: 1.021** (Bridge: 0.0102 * Flux: 100.0%)
- `src/cobolsourcescanner.ts` -> **Severity: 0.746** (Bridge: 0.0075 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/iconfiguration.ts` -> **Severity: 18.941** (Embedded: 0.2992 * Error Risk: 63.308%)
- `src/vsconfiguration.ts` -> **Severity: 11.627** (Embedded: 0.1609 * Error Risk: 72.2715%)
- `src/externalfeatures.ts` -> **Severity: 11.503** (Embedded: 0.2206 * Error Risk: 52.1415%)
- `src/cobolsourcescanner.ts` -> **Severity: 11.111** (Embedded: 0.1467 * Error Risk: 75.7578%)
- `src/splittoken.ts` -> **Severity: 9.507** (Embedded: 0.1117 * Error Risk: 85.1083%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/iconfiguration.ts` -> **Severity: 18150.0** (Blast Radius: 181.5 * Doc Risk: 100.0%)
- `src/externalfeatures.ts` -> **Severity: 13577.5** (Blast Radius: 217.24 * Doc Risk: 62.5%)
- `src/isourcehandler.ts` -> **Severity: 9508.605** (Blast Radius: 99.614 * Doc Risk: 95.4545%)
- `src/keywords/cobolCallTargets.ts` -> **Severity: 2689.1** (Blast Radius: 26.891 * Doc Risk: 100.0%)
- `src/fileutils.ts` -> **Severity: 1617.8** (Blast Radius: 16.178 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `1` files carry mainframe facts -- `0` call sites, `0` dataset bindings, `1` record items.

### `src/test/suite/test.cbl` (COBOL)
- **Record layouts (1 items):** `WS-ITEM (1)`

- **Mainframe skeleton completeness:** 0% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (1 gaps).

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2688 call pairs -- scoped 32.5%, unique 0.0%, ambiguous 9.0%, external 58.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 2645 | 33.0% | 0.0% | 9.2% | 57.8% |
| shell | 43 | 0.0% | 0.0% | 0.0% | 100.0% |

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
