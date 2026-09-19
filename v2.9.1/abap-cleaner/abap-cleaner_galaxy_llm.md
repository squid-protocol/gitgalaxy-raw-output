# ARCHITECTURAL_BRIEF: abap-cleaner
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SAP/abap-cleaner` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 555 analyzed artifact(s), 118063 LOC.
- **Load-bearing artifact:** `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -- 161 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` at magnitude 3359.58 (structural weight, not risk).
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
| Total Artifacts | 731 |
| Analyzed Artifacts (Scanned) | 555 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 176 |
| Total LOC | 118063 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 75.9% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3779 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2735 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.6295 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 535 | 117993 | 96.4% |
| PLAINTEXT | 10 | 0 | 1.8% |
| XML | 5 | 0 | 0.9% |
| MARKDOWN | 2 | 0 | 0.4% |
| HTML | 2 | 53 | 0.4% |
| JSON | 1 | 17 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Hub-Coupled App`
> **Architectural Drift Z-Score:** `1.385`
> **Composition Archetype:** `Hub-Coupled App` (z +1.39; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 27%, Parameter Forwarders Files 18%, Large Core Modules 13%, State Mutators Files 10%, Encapsulated Accessors Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 543 | 97.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 2.2% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 176*

**Composition by Extension & Reason:**
- `.md`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 204015 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 145392 LOC exceeds safe regex boundaries)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prefs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mf`: 3x Excluded (Unsupported Extension: '.MF')
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.product`: 1x Excluded (Unsupported Extension: '.product')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 28.2 | 11.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 51.5 | 54.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 31.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.4 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.2 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 86.9 | 0.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 37.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 79.6 | 4.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 16.8 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 232 | 133 | 1 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` |
| cleanup | 78 | 21 | 0 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` |
| guards | 6861 | 452 | 30 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| danger | 4737 | 351 | 18 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| concurrency | 528 | 33 | 0 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/AbapDocParametersTest.java` |
| connectivity | 4876 | 467 | 17 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| io | 102 | 23 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/FileSystem.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 449 | 121 | 3 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 49 | 8 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/position/RuleForDdlPositionJoinOrAssociation.java` |
| tests | 7079 | 151 | 27 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` |
| docs | 703 | 153 | 2 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/AbapDocParametersTest.java` |
| debt | 339 | 46 | 0 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` |
| mutation | 28331 | 464 | 125 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` |
| dead_code | 4754 | 410 | 22 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 1 | 1 | 0 | `com.sap.adt.abapcleaner.gui/src/org/eclipse/wb/swt/SWTResourceManager.java` |
| ml_ai | 150 | 54 | 0 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` |
| ui | 2 | 2 | 0 | `_site/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/FileSystem.java` (Hits: 36)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (Hits: 15)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/PersistencyBase.java` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **RuleID.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java`) — 161 inbound connections
2. **RuleTestBase.java** (`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java`) — 100 inbound connections
3. **UnexpectedSyntaxAfterChanges.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxAfterChanges.java`) — 88 inbound connections
4. **ABAP.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/ABAP.java`) — 77 inbound connections
5. **Command.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java`) — 77 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AbapCleanerHandlerBase.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java`) — 47 outbound dependencies
2. **FrmMain.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java`) — 43 outbound dependencies
3. **FrmProfiles.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) — 41 outbound dependencies
4. **RuleTestBase.java** (`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java`) — 40 outbound dependencies
5. **CodeDisplay.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `identifyComment` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`) -> Impact: **355.1** | LOC: 328
- `determineMemoryAccessType` **(Compute Cores)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java`) -> Impact: **253.7** | LOC: 553
- `refine` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java`) -> Impact: **180.2** | LOC: 125
- `processKeyPressedEvent` **(Compute Cores)** (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) -> Impact: **179.5** | LOC: 252
- `create` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> Impact: **178.4** | LOC: 208
- `align` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java`) -> Impact: **168.6** | LOC: 188
  * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMultiline true = a Term may cover multiple lines; fal...
- `align` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/TreeAlign.java`) -> Impact: **163.2** | LOC: 153
- `obfuscateIdentifier` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java`) -> Impact: **159.6** | LOC: 151
- `buildAlignTable` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **148.5** | LOC: 177
- `alignParams` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **147.6** | LOC: 180

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser` | 32 | 10728.18 | 43.62% | 17.62% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers` | 56 | 9317.26 | 40.05% | 16.78% |
| `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui` | 31 | 7162.48 | 43.44% | 60.6% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment` | 45 | 5613.18 | 35.91% | 74.72% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base` | 22 | 3441.94 | 21.01% | 18.94% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations` | 26 | 2928.42 | 29.79% | 87.25% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase` | 28 | 2615.56 | 28.58% | 15.9% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment` | 17 | 2479.02 | 5.96% | 0.0% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands` | 25 | 2218.24 | 28.2% | 89.17% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax` | 22 | 2151.26 | 38.97% | 82.74% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/IFileSystem.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapKeywordFreqBatchJob.java` -> **99.9999%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands/AssertEqualsSubrcRule.java` -> **99.9999%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands/AssertEqualsBooleanRule.java` -> **99.9998%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/DummySearchControls.java` -> **99.999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplayColors.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigIntBox.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmImportTestCode.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmInputBox.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfileDirs.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` -> **160** Orphaned Functions | **0** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` -> **148** Orphaned Functions | **0** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` -> **117** Orphaned Functions | **0** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` -> **113** Orphaned Functions | **0** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsTest.java` -> **85** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3083` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3359.58 | **LOC:** 3950 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **72** in-repo importer(s); it depends on **8**; blast radius 11.163; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.5%), Complexity Load (formerly Cognitive Load) (87.2%)
- **Documentation Coverage:** 76.8053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `determineMemoryAccessType` **(Compute Cores)** (Impact: 253.7)
  * `getLastTokenOfSequence` **(Many-Argument Workhorses)** (Impact: 141.3)
  * `getStrucInfo` **(Compute Cores)** (Impact: 94.2)
    * *Intent:* /** returns a StrucInfo instance if the Token as a whole is the name of a structure or one of its co...
  * `getLastTokenOfLogicalExpression` **(I/O & Config Routines)** (Impact: 87.5)
    * *Intent:* /** * If this Token starts a logical expression, the last code Token of the logical expression is re...
  * `toTextBits` **(Many-Argument Workhorses)** (Impact: 76.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1065
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1126`, `structural_boundaries: 664`, `args: 240`, `func_start: 240`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 441`, `state_mutation: 375`, `dead_code: 26`, `planned_debt: 6`
* *Architecture:* `api: 222`, `import: 4`
* *Defense:* `safety: 10`, `doc: 50`, `sync_locks: 4`, `immutability_locks: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.163
  * `Choke Point (Betweenness):` 0.036562 | `Ripple Effect (Closeness):` 0.201039
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.Rule, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.LogicalExpression, java.security.InvalidParameterException, java.util.*
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 3258.92 | **LOC:** 4192 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **5**; blast radius 10.09; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Connectivity (formerly Api Exposure) (96.0%), Complexity Load (formerly Cognitive Load) (87.2%)
- **Documentation Coverage:** 81.3008% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canAddToDdl` **(Many-Argument Workhorses)** (Impact: 122.5)
  * `changesSySubrc` **(I/O & Config Routines)** (Impact: 109.8)
    * *Intent:* /** Returns true if the Command changes sy-subrc */
  * `distinguishOperators` **(Many-Argument Workhorses)** (Impact: 101.4)
  * `finishBuild` **(Many-Argument Workhorses)** (Impact: 97.4)
  * `handleChainElement` **(Many-Argument Workhorses)** (Impact: 95.8)
    * *Intent:* /** * Handles the specified chain element (or, if the Command is not a chain, the entire Command) wi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 356 instances
* *State Mutation (weighted view):* 1110
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 903`, `structural_boundaries: 652`, `args: 266`, `func_start: 267`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 453`, `state_mutation: 398`, `dead_code: 26`, `planned_debt: 6`
* *Architecture:* `api: 231`, `import: 2`
* *Defense:* `safety: 24`, `doc: 48`, `test: 2`, `sync_locks: 3`, `immutability_locks: 203`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.09
  * `Choke Point (Betweenness):` 5.4e-05 | `Ripple Effect (Closeness):` 0.207299
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.base.ABAP.SyField, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.RuleID, java.util.*
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 2212.76 | **LOC:** 2986 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **43**; blast radius 2.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (95.6%), Complexity Load (formerly Cognitive Load) (95.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContents` **(I/O & Config Routines)** (Impact: 104.0)
    * *Intent:* /** * Create contents of the window. */
  * `refreshCode` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `createReleaseNoteDocumentation` **(I/O & Config Routines)** (Impact: 52.7)
  * `open` **(Many-Argument Workhorses)** (Impact: 50.6)
    * *Intent:* /** * @wbp.parser.entryPoint */
  * `patternMatchesToClip` **(Many-Argument Workhorses)** (Impact: 49.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 210 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 894
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 435`, `structural_boundaries: 595`, `args: 178`, `func_start: 167`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 158`, `state_mutation: 474`, `dead_code: 16`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 115`, `concurrency: 6`, `import: 36`
* *Defense:* `safety: 37`, `doc: 5`, `sync_locks: 1`, `immutability_locks: 32`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.147
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.00361
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.comparer.ChangeTypes, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.io.IOException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1774.66 | **LOC:** 1972 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **41**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.0%), Complexity Load (formerly Cognitive Load) (97.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContents` **(I/O & Config Routines)** (Impact: 87.0)
    * *Intent:* /** * Create contents of the window. */
  * `importProfiles` **(I/O & Config Routines)** (Impact: 45.2)
  * `generateUnitTestClass` **(Many-Argument Workhorses)** (Impact: 43.0)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `setProfile` **(Compute Cores)** (Impact: 41.5)
  * `exportProfiles` **(Compute Cores)** (Impact: 41.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 244 instances
* *State Mutation (weighted view):* 932
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 369`, `structural_boundaries: 373`, `args: 83`, `func_start: 81`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 444`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 46`, `import: 36`
* *Defense:* `safety: 27`, `doc: 4`, `test: 2`, `immutability_locks: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Obfuscator, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, java.io.IOException, java.util.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1405.84 | **LOC:** 1252 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 1.563; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Connectivity (formerly Api Exposure) (16.9%)
- **Documentation Coverage:** 94.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `identifyComment` **(Many-Argument Workhorses)** (Impact: 355.1)
  * `preprocessLine` **(Many-Argument Workhorses)** (Impact: 117.5)
  * `getWordFrequencies` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `initialize` **(Compute Cores)** (Impact: 61.4)
  * `addCommentSamples` **(Many-Argument Workhorses)** (Impact: 51.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 122 instances
* *State Mutation (weighted view):* 390
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 172`, `args: 36`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 146`, `dead_code: 13`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 21`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 4`, `doc: 4`, `sync_locks: 3`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.563
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.083838
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.Program, java.io.BufferedReader, java.io.IOException, java.io.InputStream, java.io.InputStreamReader, java.nio.charset.StandardCharsets, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1181.56 | **LOC:** 1455 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **38**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (99.3%), Guard Balance (formerly Safety Score) (90.8%), Complexity Load (formerly Cognitive Load) (84.4%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processKeyPressedEvent` **(Compute Cores)** (Impact: 179.5)
  * `getLineBackground` **(Stateful Encapsulated Methods)** (Impact: 106.9)
  * `paintCode` **(Many-Argument Workhorses)** (Impact: 102.0)
  * `generateUnitTest` **(Many-Argument Workhorses)** (Impact: 60.9)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `getTextForeground` **(Compute Cores)** (Impact: 52.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 277`, `args: 95`, `func_start: 97`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 135`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 36`
* *Architecture:* `api: 69`, `concurrency: 2`, `import: 34`
* *Defense:* `safety: 8`, `doc: 6`, `test: 1`, `immutability_locks: 66`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.CompareException, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.programbase.Task...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/ABAP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1020.86 | **LOC:** 1158 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **77** in-repo importer(s); it depends on **5**; blast radius 24.333; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (78.3%), Mutation Surface (formerly State Flux) (54.2%), Complexity Load (formerly Cognitive Load) (31.6%)
- **Documentation Coverage:** 85.4167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isComparisonOperator` **(Compute Cores)** (Impact: 117.1)
  * `negateComparisonOperator` **(Compute Cores)** (Impact: 100.0)
  * `isCharAllowedForTypeNames` **(Many-Argument Workhorses)** (Impact: 49.4)
  * `isCharAllowedForVariableNames` **(Many-Argument Workhorses)** (Impact: 48.7)
  * `mayBeVariableName` **(Many-Argument Workhorses)** (Impact: 33.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 373`, `structural_boundaries: 210`, `args: 55`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 44`, `dead_code: 6`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 162`, `import: 4`
* *Defense:* `safety: 4`, `doc: 33`, `immutability_locks: 125`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.333
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.222036
  * `Imports (Out-Degree: 0):` java.io.BufferedReader, java.io.IOException, java.io.InputStream, java.io.InputStreamReader, java.util.*
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 1015.04 | **LOC:** 1070 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 1.448; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.1%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `buildAlignTable` **(Many-Argument Workhorses)** (Impact: 148.5)
  * `alignParams` **(Many-Argument Workhorses)** (Impact: 147.6)
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 76.8)
  * `determineTableStart` **(Many-Argument Workhorses)** (Impact: 70.4)
  * `determineKeepOnSingleLine` **(Stateful Encapsulated Methods)** (Impact: 37.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 248`, `structural_boundaries: 132`, `args: 34`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 117`, `dead_code: 17`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 8`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.448
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.00722
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 883.3 | **LOC:** 831 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **60** in-repo importer(s); it depends on **2**; blast radius 23.909; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.3%), Complexity Load (formerly Cognitive Load) (62.8%)
- **Documentation Coverage:** 80.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `split` **(Many-Argument Workhorses)** (Impact: 44.7)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` **(Many-Argument Workhorses)** (Impact: 39.6)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `containsAt` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `indexOfAny` **(Many-Argument Workhorses)** (Impact: 30.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 175`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 67`, `dead_code: 1`
* *Architecture:* `api: 60`, `import: 2`
* *Defense:* `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.909
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.225461
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 832.34 | **LOC:** 805 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 4.416; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.5%), Complexity Load (formerly Cognitive Load) (84.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (36.7%)
- **Documentation Coverage:** 83.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `negate` **(Many-Argument Workhorses)** (Impact: 94.1)
  * `LogicalExpression` **(Many-Argument Workhorses)** (Impact: 66.7)
  * `calculateComplexity` **(Compute Cores)** (Impact: 56.7)
    * *Intent:* /** * Calculates the {@link #currentComplexity} of this LogicalExpression and all its inner expressi...
  * `removeFirstNeedlessParentheses` **(Many-Argument Workhorses)** (Impact: 54.6)
  * `toTreeAlign` **(Compute Cores)** (Impact: 49.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 240`, `structural_boundaries: 99`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 121`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `api: 20`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.416
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.135839
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CamelCaseNames.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 819.2 | **LOC:** 875 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **18**; blast radius 1.268; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.4%), Connectivity (formerly Api Exposure) (24.0%)
- **Documentation Coverage:** 95.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createFromTextFiles` **(Many-Argument Workhorses)** (Impact: 95.5)
  * `preprocessFromGTNC` **(Many-Argument Workhorses)** (Impact: 76.9)
  * `createFromTextFile` **(Many-Argument Workhorses)** (Impact: 69.6)
  * `checkDiscardReasons` **(Many-Argument Workhorses)** (Impact: 49.7)
  * `applyCamelCaseTo` **(Many-Argument Workhorses)** (Impact: 37.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 129`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 117`, `dead_code: 11`
* *Architecture:* `io: 2`, `api: 28`, `import: 18`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.268
  * `Choke Point (Betweenness):` 0.000257 | `Ripple Effect (Closeness):` 0.090054
  * `Imports (Out-Degree: 6):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.Cult, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.Persistency, com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.rulebase.Profile, java.io.BufferedReader, java.io.BufferedWriter...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 810.44 | **LOC:** 970 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.098; role: Isolated/Orphan
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 92.4242% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 55.4)
  * `alignGenericTypeComponents` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* /** aligns the components of TYPE ANY STRUCTURE CONTAINING ... */
  * `readDeclarationLine` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `buildTable` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `joinColumns` **(Many-Argument Workhorses)** (Impact: 30.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 131`, `args: 43`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 122`, `dead_code: 12`, `duplicate_logic: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate, java.util.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleForDeclarations.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 773.94 | **LOC:** 856 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **5**; blast radius 1.535; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (83.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 91.9)
  * `executeOnOtherCommand` **(Many-Argument Workhorses)** (Impact: 65.8)
  * `addMethodDefinitions` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `executeOnDeclarationCommand` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `isNeededPragmaOrPseudoCommentFound` **(Compute Cores)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 187`, `structural_boundaries: 84`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 114`, `dead_code: 8`, `planned_debt: 3`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.535
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.069684
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.util.HashMap
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 763.18 | **LOC:** 2336 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (21.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (13.9%), Dead Code Surface (formerly Dead Code) (7.4%), Guard Balance (formerly Safety Score) (6.4%)
- **Documentation Coverage:** 99.4186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAccessTypeInternalTables` **(Compute Cores)** (Impact: 53.9)
  * `testAccessTypeStringProcessing` **(Compute Cores)** (Impact: 34.0)
  * `assertAccessType` **(Compute Cores)** (Impact: 24.0)
    * *Intent:* /** * Checks the memory access type that is determined by {@link Token#getMemoryAccessType()} for th...
  * `assertMemoryAccessType` **(Stateful Encapsulated Methods)** (Impact: 23.0)
  * `testAccessTypeTableExpression` **(Compute Cores)** (Impact: 17.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 117
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 231`, `args: 182`, `func_start: 172`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 73`, `dead_code: 2`, `unreferenced_by_name: 148`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 122`, `doc: 1`, `test: 916`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.comparer.TextBit, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 709.08 | **LOC:** 733 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **70** in-repo importer(s); it depends on **5**; blast radius 8.118; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.9%), Connectivity (formerly Api Exposure) (86.0%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 82.4324% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expandCleanupRange` **(Compute Cores)** (Impact: 40.1)
  * `compareWithSource` **(Compute Cores)** (Impact: 31.9)
  * `checkSyntax` **(Compute Cores)** (Impact: 29.3)
  * `replacePart` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `toDisplayLines` **(Compute Cores)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 91`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 126`, `dead_code: 8`
* *Architecture:* `api: 41`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.118
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.193726
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, java.util.*
  * `Imported By (In-Degree: 70):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffNavigator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 672.82 | **LOC:** 597 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 2.421; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.7%), Complexity Load (formerly Cognitive Load) (98.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.0392% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 99.4)
  * `reprocessSelection` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `isLineBitHighlighted` **(Compute Cores)** (Impact: 17.7)
  * `reprocessAll` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `refreshCode` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* /** * * * @param code * @param diffDoc * @param setToTopLineIndex -1 to keep current position, 0 to ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 80`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 99`, `dead_code: 13`
* *Architecture:* `api: 51`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.421
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.091609
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 660.06 | **LOC:** 678 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 1.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (97.9%), Complexity Load (formerly Cognitive Load) (86.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeTo` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `add` **(Compute Cores)** (Impact: 59.4)
  * `checkNestingFor` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `adjustNesting` **(Many-Argument Workhorses)** (Impact: 36.3)
  * `determineTablesInArrays` **(Compute Cores)** (Impact: 24.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 86 instances
* *State Mutation (weighted view):* 260
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 84`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 88`, `dead_code: 6`
* *Architecture:* `api: 17`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.494
  * `Choke Point (Betweenness):` 0.000458 | `Ripple Effect (Closeness):` 0.085206
  * `Imports (Out-Degree: 10):` com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 627.48 | **LOC:** 466 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (93.8%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `obfuscateIdentifier` **(Many-Argument Workhorses)** (Impact: 159.6)
  * `getVariableName` **(Many-Argument Workhorses)** (Impact: 74.2)
  * `obfuscate` **(Compute Cores)** (Impact: 61.7)
  * `getTypeName` **(Stateful Encapsulated Methods)** (Impact: 20.6)
  * `clearMaps` **(Stateful Encapsulated Methods)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 50`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 82`, `dead_code: 6`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.AbapCult, com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException, com.sap.adt.abapcleaner.rulehelpers.SelectClause, com.sap.adt.abapcleaner.rulehelpers.SelectQuery, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 620.76 | **LOC:** 717 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (76.4%), Debt Markers (formerly Tech Debt) (23.5%)
- **Documentation Coverage:** 82.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addField` **(Many-Argument Workhorses)** (Impact: 71.0)
  * `getResult` **(Many-Argument Workhorses)** (Impact: 53.2)
  * `getSourceField` **(Compute Cores)** (Impact: 44.8)
  * `addFile` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `analyzeAnnotations` **(Compute Cores)** (Impact: 31.8)
    * *Intent:* /** * determines the values of (direct or inherited) annotations of select list elements * @param an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 91`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 87`, `state_mutation: 116`, `dead_code: 4`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 15`, `api: 9`, `import: 9`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 582.44 | **LOC:** 677 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.098; role: Isolated/Orphan
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (96.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `changeLineBreaks` **(Many-Argument Workhorses)** (Impact: 47.4)
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 38.6)
  * `changeLineBreaksAfterColumn` **(Stateful Encapsulated Methods)** (Impact: 30.6)
  * `isDeclarationSuitedForMultiDeclarations` **(Many-Argument Workhorses)** (Impact: 28.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 97`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 77`, `dead_code: 14`, `unreferenced_by_name: 11`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 573.22 | **LOC:** 2569 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (46.6%), Complexity Load (formerly Cognitive Load) (10.3%), Dead Code Surface (formerly Dead Code) (7.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testBoundStructuresWith2KeywordsUnused` **(I/O & Config Routines)** (Impact: 22.1)
  * `testNestedBoundStructuresUsedInComment` **(I/O & Config Routines)** (Impact: 15.4)
  * `testNestedBoundStructuresUnused` **(I/O & Config Routines)** (Impact: 15.2)
  * `testBoundStructuresUnused` **(I/O & Config Routines)** (Impact: 14.1)
  * `testRemoveObsoleteComments` **(I/O & Config Routines)** (Impact: 10.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 120`, `args: 125`, `func_start: 114`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 40`, `dead_code: 2`, `planned_debt: 112`, `unreferenced_by_name: 113`
* *Architecture:* `import: 4`
* *Defense:* `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationNestingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 566.94 | **LOC:** 633 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (50.3%), Connectivity (formerly Api Exposure) (0.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testAlwaysPutEmptyLines` **(Compute Cores)** (Impact: 39.7)
  * `testKeepEmptyLines` **(Compute Cores)** (Impact: 39.6)
  * `testSortByFirstLevelOnly` **(Compute Cores)** (Impact: 39.5)
  * `testPutEmptyLinesForNewFirstElemOnly` **(Compute Cores)** (Impact: 39.5)
  * `testNestingFromLevel2` **(Compute Cores)** (Impact: 33.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 10 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 34`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 35`, `unreferenced_by_name: 24`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulebase.RuleTestBase, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationEmptyLines, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationNestingDepth, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationSortOrder, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/LocalDeclarationOrderRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 565.2 | **LOC:** 764 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (49.7%)
- **Documentation Coverage:** 67.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `moveSection` **(Many-Argument Workhorses)** (Impact: 85.7)
    * *Intent:* /** moves the supplied Section to the next write position under the supplied ('enclosing') parent Co...
  * `moveTermInChain` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* /** moves the supplied Term to the next write position within the chain, adjusts whitespace before a...
  * `rearrange` **(Many-Argument Workhorses)** (Impact: 30.6)
    * *Intent:* /** rearranges all declarations of the supplied type in the configured order */
  * `variableMatchesFilter` **(Stateful Encapsulated Methods)** (Impact: 30.6)
    * *Intent:* /** returns true if the supplied variable shall be processed under the supplied declaration type; * ...
  * `extendSectionStart` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* /** extends the start of a to-be-moved Section with preceding attached comments */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 140`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 57`, `dead_code: 15`, `unreferenced_by_name: 12`
* *Architecture:* `api: 14`, `import: 26`
* *Defense:* `safety: 4`, `doc: 15`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 23):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Section, com.sap.adt.abapcleaner.parser.Term, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectListsRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 497.54 | **LOC:** 508 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 1.098; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (98.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 118.6)
  * `buildTableFromSpaceSepList` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `buildTableFromCommaSepList` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `determineLayout` **(Stateful Encapsulated Methods)** (Impact: 23.5)
  * `executeOn` **(Stateful Encapsulated Methods)** (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 74`, `dead_code: 3`, `unreferenced_by_name: 9`
* *Architecture:* `api: 16`, `import: 29`
* *Defense:* `safety: 4`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.098
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 27):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Term, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch, com.sap.adt.abapcleaner.parser.TokenType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 482.8 | **LOC:** 400 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **2**; blast radius 1.624; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (99.4%), Complexity Load (formerly Cognitive Load) (98.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `align` **(Many-Argument Workhorses)** (Impact: 168.6)
    * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMul...
  * `overrideWidthIfColumnIsFollowedByLineBreaks` **(Compute Cores)** (Impact: 15.5)
  * `removeLineAt` **(Compute Cores)** (Impact: 6.1)
  * `getTotalMonoLineWidth` **(I/O & Config Routines)** (Impact: 5.8)
  * `getTotalMultiLineWidth` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 46`, `args: 25`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 65`, `dead_code: 5`
* *Architecture:* `api: 29`
* *Defense:* `doc: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.624
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.085949
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, java.util.*
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> Churn: **58.75%** | Cog Load: 87.2373% | Debt: 8.3615%
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> Churn: **53.72%** | Cog Load: 87.215% | Debt: 8.4156%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3359.58
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3258.92
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 2212.76
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1774.66
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1181.56

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 3.656** (Bridge: 0.0366 * Flux: 99.9996%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 3.148** (Bridge: 0.0494 * Flux: 63.7789%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` -> **Severity: 1.287** (Bridge: 0.0129 * Flux: 99.9877%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxException.java` -> **Severity: 0.552** (Bridge: 0.0072 * Flux: 76.8525%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/prettyprinter/CamelCaseNameRule.java` -> **Severity: 0.448** (Bridge: 0.0046 * Flux: 97.5892%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 21.935** (Embedded: 0.2255 * Error Risk: 97.291%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Severity: 20.599** (Embedded: 0.2073 * Error Risk: 99.3706%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 20.002** (Embedded: 0.201 * Error Risk: 99.4939%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` -> **Severity: 19.35** (Embedded: 0.1937 * Error Risk: 99.8819%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/ABAP.java` -> **Severity: 17.385** (Embedded: 0.222 * Error Risk: 78.296%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -> **Severity: 5927.8** (Blast Radius: 59.278 * Doc Risk: 100.0%)
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java` -> **Severity: 4358.5** (Blast Radius: 43.585 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/ABAP.java` -> **Severity: 2078.445** (Blast Radius: 24.333 * Doc Risk: 85.4167%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 1932.643** (Blast Radius: 23.909 * Doc Risk: 80.8333%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxAfterChanges.java` -> **Severity: 1439.85** (Blast Radius: 19.198 * Doc Risk: 75.0%)

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
