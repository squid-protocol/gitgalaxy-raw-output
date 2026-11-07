# ARCHITECTURAL_BRIEF: abap-cleaner
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SAP/abap-cleaner` |
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
- **Scope:** 560 analyzed artifact(s), 118235 LOC.
- **Load-bearing artifact:** `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -- 168 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` -- pulls in 47 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` at magnitude 3198.08 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 560 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 171 |
| Total LOC | 118235 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 76.6% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3915 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2007 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 19.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.2737 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 58 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 535 | 117993 | 95.5% |
| PLAINTEXT | 10 | 0 | 1.8% |
| YAML | 5 | 172 | 0.9% |
| XML | 5 | 0 | 0.9% |
| MARKDOWN | 2 | 0 | 0.4% |
| HTML | 2 | 53 | 0.4% |
| JSON | 1 | 17 | 0.2% |

## 4.1 SOURCE ENCODINGS
All 560 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (3) 25%, Parameter Forwarders Files 19%, Large Core Modules 13%, State Mutators Files 10%, Encapsulated Accessors Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 548 | 97.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 12 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 171*

**Composition by Extension & Reason:**
- `.md`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 204015 LOC exceeds the 150000 LOC backstop), 1x Excluded (Lexical Monotony: High structural repetition detected in 145392 LOC)
- `.prefs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mf`: 3x Excluded (Unsupported Extension: '.MF')
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.product`: 1x Excluded (Unsupported Extension: '.product')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 24.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 93.2 | 44.1 | 51.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 30.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 16.9 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.1 | 7.1 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 86.9 | 0.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 36.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 5.1 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 91.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 232 | 133 | 1 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` |
| cleanup | 78 | 21 | 0 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` |
| guards | 6878 | 456 | 30 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| danger | 4737 | 351 | 18 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| concurrency | 530 | 35 | 0 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/AbapDocParametersTest.java` |
| connectivity | 4879 | 470 | 17 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` |
| io | 105 | 23 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/FileSystem.java` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 449 | 121 | 3 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` |
| serialization | 0 | 0 | 0 | - |
| regex | 1 | 1 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotation.java` |
| events | 49 | 8 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/position/RuleForDdlPositionJoinOrAssociation.java` |
| tests | 7079 | 151 | 27 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` |
| docs | 714 | 157 | 2 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/AbapDocParametersTest.java` |
| debt | 339 | 46 | 0 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` |
| mutation | 28331 | 464 | 124 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` |
| dead_code | 4485 | 374 | 20 | `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 3 | 2 | 0 | `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/PersistencyBase.java` |
| ml_ai | 150 | 54 | 0 | `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` |
| ui | 2 | 2 | 0 | `_site/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/FileSystem.java` (Hits: 37)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (Hits: 15)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/PersistencyBase.java` (Hits: 7)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **RuleID.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java`) — 168 inbound connections
2. **Command.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java`) — 151 inbound connections
3. **Token.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java`) — 142 inbound connections
4. **Rule.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java`) — 130 inbound connections
5. **Code.java** (`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java`) — 111 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **AbapCleanerHandlerBase.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java`) — 47 outbound dependencies
2. **FrmMain.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java`) — 43 outbound dependencies
3. **FrmProfiles.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) — 41 outbound dependencies
4. **RuleTestBase.java** (`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java`) — 40 outbound dependencies
5. **CodeDisplay.java** (`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) — 38 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `identifyComment` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`) -> Impact: **323.3** | LOC: 328
- `determineMemoryAccessType` **(I/O & Config Routines)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java`) -> Impact: **242.7** | LOC: 553
- `create` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> Impact: **154.2** | LOC: 208
- `obfuscateIdentifier` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java`) -> Impact: **153.6** | LOC: 151
- `align` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java`) -> Impact: **139.2** | LOC: 188
  * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMultiline true = a Term may cover multiple lines; fal...
- `alignParams` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **136.3** | LOC: 180
- `buildAlignTable` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **133.8** | LOC: 177
- `refine` **(Compute Cores)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefiner.java`) -> Impact: **133.2** | LOC: 260
- `processKeyPressedEvent` **(Compute Cores)** (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) -> Impact: **131.4** | LOC: 252
- `align` **(Many-Argument Workhorses)** (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/TreeAlign.java`) -> Impact: **129.3** | LOC: 153

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser` | 32 | 10251.08 | 42.38% | 17.62% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers` | 56 | 8665.06 | 38.32% | 16.78% |
| `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui` | 31 | 6330.58 | 40.44% | 60.6% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment` | 45 | 5402.88 | 35.93% | 74.72% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base` | 22 | 3128.44 | 19.22% | 18.94% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations` | 26 | 2671.62 | 28.09% | 87.25% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase` | 28 | 2475.06 | 25.33% | 15.9% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment` | 17 | 2007.32 | 0.0% | 0.0% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax` | 22 | 1998.26 | 36.92% | 82.74% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands` | 25 | 1995.74 | 23.79% | 89.17% |

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
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3098` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 13.422)
- **Top Global Matches:** file_cluster_7: 13.422, file_cluster_14: 13.632, file_cluster_12: 14.2
- **Magnitude:** 3198.08 | **LOC:** 3950 | **CtrlFlow:** 38.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **142** in-repo importer(s); it depends on **8**; blast radius 21.986; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.7%), Guard Balance (formerly Safety Score) (85.3%)
- **Documentation Coverage:** 76.8053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `determineMemoryAccessType` **(I/O & Config Routines)** (Impact: 242.7)
  * `getLastTokenOfSequence` **(Many-Argument Workhorses)** (Impact: 125.6)
  * `getStrucInfo` **(I/O & Config Routines)** (Impact: 86.2)
    * *Intent:* /** returns a StrucInfo instance if the Token as a whole is the name of a structure or one of its co...
  * `getLastTokenOfLogicalExpression` **(I/O & Config Routines)** (Impact: 81.5)
    * *Intent:* /** * If this Token starts a logical expression, the last code Token of the logical expression is re...
  * `setWhitespaceInclAttachedComments` **(Many-Argument Workhorses)** (Impact: 69.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 345 instances
* *State Mutation (weighted view):* 1065
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1012`, `structural_boundaries: 664`, `args: 240`, `func_start: 240`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 441`, `state_mutation: 375`, `dead_code: 8`, `planned_debt: 6`
* *Architecture:* `api: 222`, `import: 4`
* *Defense:* `safety: 10`, `doc: 50`, `sync_locks: 4`, `immutability_locks: 174`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 21.986
  * `Choke Point (Betweenness):` 0.030117 | `Ripple Effect (Closeness):` 0.342452
  * `Imports (Out-Degree: 14):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.Rule, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.LogicalExpression, java.security.InvalidParameterException, java.util.*
  * `Imported By (In-Degree: 142):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 11.678)
- **Top Global Matches:** file_cluster_7: 11.678, file_cluster_14: 12.007, file_cluster_5: 12.181
- **Magnitude:** 3145.82 | **LOC:** 4192 | **CtrlFlow:** 29.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **151** in-repo importer(s); it depends on **5**; blast radius 19.658; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Connectivity (formerly Api Exposure) (96.0%), Complexity Load (formerly Cognitive Load) (86.7%), Guard Balance (formerly Safety Score) (84.4%)
- **Documentation Coverage:** 81.3008% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canAddToDdl` **(Many-Argument Workhorses)** (Impact: 115.5)
  * `changesSySubrc` **(I/O & Config Routines)** (Impact: 109.8)
    * *Intent:* /** Returns true if the Command changes sy-subrc */
  * `distinguishOperators` **(Many-Argument Workhorses)** (Impact: 96.2)
  * `finishBuild` **(Many-Argument Workhorses)** (Impact: 89.4)
  * `handleChainElement` **(Many-Argument Workhorses)** (Impact: 81.8)
    * *Intent:* /** * Handles the specified chain element (or, if the Command is not a chain, the entire Command) wi...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 355 instances
* *State Mutation (weighted view):* 1108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 837`, `structural_boundaries: 652`, `args: 266`, `func_start: 267`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 453`, `state_mutation: 398`, `dead_code: 16`, `planned_debt: 6`
* *Architecture:* `api: 231`, `import: 2`
* *Defense:* `safety: 24`, `doc: 48`, `test: 2`, `sync_locks: 3`, `immutability_locks: 203`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.658
  * `Choke Point (Betweenness):` 0.010171 | `Ripple Effect (Closeness):` 0.358284
  * `Imports (Out-Degree: 13):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.base.ABAP.SyField, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.RuleID, java.util.*
  * `Imported By (In-Degree: 151):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.823)
- **Top Global Matches:** file_cluster_12: 7.823, file_cluster_5: 8.593, file_cluster_7: 8.657
- **Magnitude:** 1991.26 | **LOC:** 2986 | **CtrlFlow:** 13.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **43**; blast radius 1.246; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.6%)
- **Documentation Coverage:** 97.0588% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContents` **(I/O & Config Routines)** (Impact: 84.0)
    * *Intent:* /** * Create contents of the window. */
  * `refreshCode` **(Many-Argument Workhorses)** (Impact: 49.0)
  * `open` **(Many-Argument Workhorses)** (Impact: 47.7)
    * *Intent:* /** * @wbp.parser.entryPoint */
  * `writeCleanUpResult` **(Many-Argument Workhorses)** (Impact: 38.9)
  * `keyPressedInCodeDisplay` **(Compute Cores)** (Impact: 35.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 178 instances
* *Concurrency (weighted view):* 11
* *State Mutation (weighted view):* 830
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 333`, `structural_boundaries: 595`, `args: 178`, `func_start: 167`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 158`, `state_mutation: 474`, `dead_code: 9`, `planned_debt: 6`, `fragile_debt: 4`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 115`, `concurrency: 6`, `import: 36`
* *Defense:* `safety: 37`, `doc: 5`, `sync_locks: 1`, `immutability_locks: 32`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.246
  * `Choke Point (Betweenness):` 0.003437 | `Ripple Effect (Closeness):` 0.010078
  * `Imports (Out-Degree: 47):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.comparer.ChangeTypes, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.io.IOException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.162)
- **Top Global Matches:** file_cluster_4: 11.162, file_cluster_5: 11.62, file_cluster_12: 11.755
- **Magnitude:** 1561.16 | **LOC:** 1972 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **41**; blast radius 2.062; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.1%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createContents` **(I/O & Config Routines)** (Impact: 68.0)
    * *Intent:* /** * Create contents of the window. */
  * `generateUnitTestClass` **(Many-Argument Workhorses)** (Impact: 34.3)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `getRuleBackground` **(Stateful Encapsulated Methods)** (Impact: 33.5)
  * `importProfiles` **(I/O & Config Routines)** (Impact: 32.2)
  * `setProfile` **(Compute Cores)** (Impact: 31.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 199 instances
* *State Mutation (weighted view):* 842
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 373`, `args: 83`, `func_start: 81`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 444`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 46`, `import: 36`
* *Defense:* `safety: 27`, `doc: 4`, `test: 2`, `immutability_locks: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.062
  * `Choke Point (Betweenness):` 0.003723 | `Ripple Effect (Closeness):` 0.013742
  * `Imports (Out-Degree: 35):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Obfuscator, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, java.io.IOException, java.util.*...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 13.113)
- **Top Global Matches:** file_cluster_6: 13.113, file_cluster_4: 13.446, file_cluster_5: 15.479
- **Magnitude:** 1194.84 | **LOC:** 1252 | **CtrlFlow:** 32.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **8**; blast radius 0.908; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (16.9%)
- **Documentation Coverage:** 94.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `identifyComment` **(Many-Argument Workhorses)** (Impact: 323.3)
  * `preprocessLine` **(Many-Argument Workhorses)** (Impact: 107.5)
  * `getWordFrequencies` **(Many-Argument Workhorses)** (Impact: 75.5)
  * `addCommentSamples` **(Many-Argument Workhorses)** (Impact: 41.2)
  * `filterForMode` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* // -------------------------------------------------------------------------------------------------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 372
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 172`, `args: 36`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 146`, `dead_code: 9`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 21`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 4`, `doc: 4`, `sync_locks: 3`, `immutability_locks: 36`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.908
  * `Choke Point (Betweenness):` 0.002786 | `Ripple Effect (Closeness):` 0.166326
  * `Imports (Out-Degree: 10):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.Program, java.io.BufferedReader, java.io.IOException, java.io.InputStream, java.io.InputStreamReader, java.nio.charset.StandardCharsets, java.util.*
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.258)
- **Top Global Matches:** file_cluster_12: 9.258, file_cluster_7: 10.529, file_cluster_4: 10.623
- **Magnitude:** 1006.96 | **LOC:** 1455 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **38**; blast radius 0.623; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (99.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.9%)
- **Documentation Coverage:** 94.4444% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processKeyPressedEvent` **(Compute Cores)** (Impact: 131.4)
  * `paintCode` **(Many-Argument Workhorses)** (Impact: 81.9)
  * `getLineBackground` **(Stateful Encapsulated Methods)** (Impact: 60.3)
  * `generateUnitTest` **(Many-Argument Workhorses)** (Impact: 52.2)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `getTextForeground` **(Stateful Encapsulated Methods)** (Impact: 28.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 273
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 259`, `structural_boundaries: 277`, `args: 95`, `func_start: 97`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 69`, `state_mutation: 135`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 9`, `unreferenced_by_name: 36`
* *Architecture:* `api: 69`, `concurrency: 2`, `import: 34`
* *Defense:* `safety: 8`, `doc: 6`, `test: 1`, `immutability_locks: 66`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.623
  * `Choke Point (Betweenness):` 0.000607 | `Ripple Effect (Closeness):` 0.010797
  * `Imports (Out-Degree: 25):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.CompareException, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.programbase.Task...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.368)
- **Top Global Matches:** file_cluster_6: 12.368, file_cluster_4: 12.37, file_cluster_5: 14.488
- **Magnitude:** 952.84 | **LOC:** 1070 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 0.682; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alignParams` **(Many-Argument Workhorses)** (Impact: 136.3)
  * `buildAlignTable` **(Many-Argument Workhorses)** (Impact: 133.8)
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 70.8)
  * `determineTableStart` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `determineKeepOnSingleLine` **(Stateful Encapsulated Methods)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 112 instances
* *State Mutation (weighted view):* 341
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 132`, `args: 34`, `func_start: 32`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 67`, `state_mutation: 117`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 8`, `immutability_locks: 21`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.682
  * `Choke Point (Betweenness):` 0.000188 | `Ripple Effect (Closeness):` 0.007454
  * `Imports (Out-Degree: 17):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/ABAP.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.309)
- **Top Global Matches:** file_cluster_4: 8.309, file_cluster_12: 10.616, file_cluster_5: 11.567
- **Magnitude:** 840.66 | **LOC:** 1158 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **89** in-repo importer(s); it depends on **5**; blast radius 10.873; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (60.5%), Mutation Surface (formerly State Flux) (54.2%), Complexity Load (formerly Cognitive Load) (22.5%)
- **Documentation Coverage:** 85.4167% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isComparisonOperator` **(Compute Cores)** (Impact: 61.6)
  * `negateComparisonOperator` **(Compute Cores)** (Impact: 53.3)
  * `isCharAllowedForTypeNames` **(Many-Argument Workhorses)** (Impact: 47.1)
  * `isCharAllowedForVariableNames` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `mayBeVariableName` **(Many-Argument Workhorses)** (Impact: 33.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 210`, `args: 55`, `func_start: 55`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 44`, `dead_code: 3`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 162`, `import: 4`
* *Defense:* `safety: 4`, `doc: 33`, `immutability_locks: 125`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.873
  * `Choke Point (Betweenness):` 0.001205 | `Ripple Effect (Closeness):` 0.330877
  * `Imports (Out-Degree: 3):` java.io.BufferedReader, java.io.IOException, java.io.InputStream, java.io.InputStreamReader, java.util.*
  * `Imported By (In-Degree: 89):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.24)
- **Top Global Matches:** file_cluster_7: 8.24, file_cluster_5: 9.034, file_cluster_12: 9.279
- **Magnitude:** 822.7 | **LOC:** 831 | **CtrlFlow:** 30.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **103** in-repo importer(s); it depends on **2**; blast radius 182.373; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (59.2%)
- **Documentation Coverage:** 80.8333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `split` **(Many-Argument Workhorses)** (Impact: 40.2)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` **(Many-Argument Workhorses)** (Impact: 32.9)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `containsAt` **(Many-Argument Workhorses)** (Impact: 31.2)
  * `findWholeWord` **(Many-Argument Workhorses)** (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 175`, `args: 61`, `func_start: 61`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 73`, `state_mutation: 67`
* *Architecture:* `api: 60`, `import: 2`
* *Defense:* `doc: 11`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 182.373
  * `Choke Point (Betweenness):` 0.000213 | `Ripple Effect (Closeness):` 0.385821
  * `Imports (Out-Degree: 1):` java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 103):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.321)
- **Top Global Matches:** file_cluster_4: 9.321, file_cluster_5: 11.494, file_cluster_12: 11.615
- **Magnitude:** 780.04 | **LOC:** 970 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 0.706; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.1%)
- **Documentation Coverage:** 92.4242% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `alignGenericTypeComponents` **(Many-Argument Workhorses)** (Impact: 49.8)
    * *Intent:* /** aligns the components of TYPE ANY STRUCTURE CONTAINING ... */
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `readDeclarationLine` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `buildTable` **(Many-Argument Workhorses)** (Impact: 39.5)
  * `joinColumns` **(Many-Argument Workhorses)** (Impact: 30.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 114 instances
* *State Mutation (weighted view):* 350
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 131`, `args: 43`, `func_start: 43`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 122`, `dead_code: 5`, `duplicate_logic: 2`, `unreferenced_by_name: 13`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.706
  * `Choke Point (Betweenness):` 0.000235 | `Ripple Effect (Closeness):` 0.001789
  * `Imports (Out-Degree: 20):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate, java.util.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 9.627)
- **Top Global Matches:** file_cluster_6: 9.627, file_cluster_4: 13.778, file_cluster_8: 16.163
- **Magnitude:** 778.54 | **LOC:** 805 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **4**; blast radius 2.465; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.4%), Guard Balance (formerly Safety Score) (80.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (38.0%)
- **Documentation Coverage:** 83.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `negate` **(Many-Argument Workhorses)** (Impact: 80.3)
  * `LogicalExpression` **(Many-Argument Workhorses)** (Impact: 64.5)
  * `calculateComplexity` **(Compute Cores)** (Impact: 55.3)
    * *Intent:* /** * Calculates the {@link #currentComplexity} of this LogicalExpression and all its inner expressi...
  * `removeFirstNeedlessParentheses` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `toTreeAlign` **(Compute Cores)** (Impact: 30.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 107 instances
* *State Mutation (weighted view):* 335
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 99`, `args: 28`, `func_start: 28`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 121`, `dead_code: 11`, `planned_debt: 1`
* *Architecture:* `api: 20`
* *Defense:* `safety: 6`, `doc: 5`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.465
  * `Choke Point (Betweenness):` 0.002483 | `Ripple Effect (Closeness):` 0.225472
  * `Imports (Out-Degree: 6):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, java.util.*
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleForDeclarations.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 11.96)
- **Top Global Matches:** file_cluster_6: 11.96, file_cluster_4: 15.464, file_cluster_8: 17.913
- **Magnitude:** 762.74 | **LOC:** 856 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **5**; blast radius 0.864; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.3%), Complexity Load (formerly Cognitive Load) (82.3%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 86.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 90.2)
  * `executeOnOtherCommand` **(Many-Argument Workhorses)** (Impact: 64.1)
  * `addMethodDefinitions` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `executeOnDeclarationCommand` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `isNeededPragmaOrPseudoCommentFound` **(Compute Cores)** (Impact: 37.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 316
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 84`, `args: 23`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 66`, `state_mutation: 114`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.864
  * `Choke Point (Betweenness):` 0.003611 | `Ripple Effect (Closeness):` 0.143216
  * `Imports (Out-Degree: 15):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.util.HashMap
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CamelCaseNames.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.53)
- **Top Global Matches:** file_cluster_4: 10.53, file_cluster_5: 11.746, file_cluster_12: 11.987
- **Magnitude:** 756.0 | **LOC:** 875 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **18**; blast radius 0.971; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (98.2%), Guard Balance (formerly Safety Score) (77.0%), Connectivity (formerly Api Exposure) (24.0%)
- **Documentation Coverage:** 95.5556% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createFromTextFiles` **(Many-Argument Workhorses)** (Impact: 74.3)
  * `preprocessFromGTNC` **(Many-Argument Workhorses)** (Impact: 66.9)
  * `createFromTextFile` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `checkDiscardReasons` **(Many-Argument Workhorses)** (Impact: 35.0)
  * `applyCamelCaseTo` **(Many-Argument Workhorses)** (Impact: 34.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 90 instances
* *State Mutation (weighted view):* 297
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 129`, `args: 33`, `func_start: 33`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 117`
* *Architecture:* `io: 3`, `api: 28`, `import: 18`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.971
  * `Choke Point (Betweenness):` 0.00103 | `Ripple Effect (Closeness):` 0.168604
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.Cult, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.Persistency, com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.rulebase.Profile, java.io.BufferedReader, java.io.BufferedWriter...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 9.697)
- **Top Global Matches:** file_cluster_14: 9.697, file_cluster_5: 9.717, file_cluster_7: 9.969
- **Magnitude:** 690.78 | **LOC:** 733 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **111** in-repo importer(s); it depends on **5**; blast radius 8.674; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (90.4%), Connectivity (formerly Api Exposure) (86.0%), Complexity Load (formerly Cognitive Load) (71.2%)
- **Documentation Coverage:** 82.4324% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expandCleanupRange` **(Compute Cores)** (Impact: 40.1)
  * `compareWithSource` **(Compute Cores)** (Impact: 26.7)
  * `replacePart` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `checkSyntax` **(Compute Cores)** (Impact: 23.6)
  * `toDisplayLines` **(Compute Cores)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 348
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 135`, `structural_boundaries: 91`, `args: 41`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 102`, `state_mutation: 126`, `dead_code: 2`
* *Architecture:* `api: 41`
* *Defense:* `safety: 4`, `doc: 6`, `immutability_locks: 30`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.674
  * `Choke Point (Betweenness):` 0.014525 | `Ripple Effect (Closeness):` 0.325916
  * `Imports (Out-Degree: 15):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, java.util.*
  * `Imported By (In-Degree: 111):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffNavigator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.169)
- **Top Global Matches:** file_cluster_7: 9.169, file_cluster_12: 10.33, file_cluster_5: 10.793
- **Magnitude:** 629.32 | **LOC:** 597 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 1.129; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.1%), Guard Balance (formerly Safety Score) (87.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 98.0392% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `search` **(Many-Argument Workhorses)** (Impact: 71.1)
  * `reprocessSelection` **(Many-Argument Workhorses)** (Impact: 65.9)
  * `reprocessAll` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `refreshCode` **(Many-Argument Workhorses)** (Impact: 12.8)
    * *Intent:* /** * * * @param code * @param diffDoc * @param setToTopLineIndex -1 to keep current position, 0 to ...
  * `isLineBitHighlighted` **(Compute Cores)** (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 281
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 80`, `args: 52`, `func_start: 52`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 99`, `dead_code: 3`
* *Architecture:* `api: 51`
* *Defense:* `safety: 4`, `doc: 2`, `immutability_locks: 50`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.129
  * `Choke Point (Betweenness):` 0.002611 | `Ripple Effect (Closeness):` 0.097359
  * `Imports (Out-Degree: 15):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.199)
- **Top Global Matches:** file_cluster_6: 10.199, file_cluster_4: 10.229, file_cluster_12: 14.463
- **Magnitude:** 610.46 | **LOC:** 678 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **12**; blast radius 0.923; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.1%)
- **Documentation Coverage:** 97.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeTo` **(Many-Argument Workhorses)** (Impact: 60.8)
  * `add` **(Compute Cores)** (Impact: 55.1)
  * `checkNestingFor` **(Many-Argument Workhorses)** (Impact: 50.8)
  * `adjustNesting` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `determineTablesInArrays` **(Compute Cores)** (Impact: 22.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 84 instances
* *State Mutation (weighted view):* 256
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 144`, `structural_boundaries: 84`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 88`, `dead_code: 1`
* *Architecture:* `api: 17`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.923
  * `Choke Point (Betweenness):` 0.004548 | `Ripple Effect (Closeness):` 0.165667
  * `Imports (Out-Degree: 17):` com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.713)
- **Top Global Matches:** file_cluster_8: 10.713, file_cluster_6: 14.22, file_cluster_4: 21.927
- **Magnitude:** 603.88 | **LOC:** 466 | **CtrlFlow:** 45.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **9**; blast radius 0.613; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.1%), Guard Balance (formerly Safety Score) (83.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `obfuscateIdentifier` **(Many-Argument Workhorses)** (Impact: 153.6)
  * `getVariableName` **(Many-Argument Workhorses)** (Impact: 65.2)
  * `obfuscate` **(Compute Cores)** (Impact: 60.3)
  * `getTypeName` **(Stateful Encapsulated Methods)** (Impact: 20.6)
  * `clearMaps` **(Stateful Encapsulated Methods)** (Impact: 11.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 246
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 50`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 82`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.613
  * `Choke Point (Betweenness):` 0.000138 | `Ripple Effect (Closeness):` 0.011365
  * `Imports (Out-Degree: 11):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.AbapCult, com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException, com.sap.adt.abapcleaner.rulehelpers.SelectClause, com.sap.adt.abapcleaner.rulehelpers.SelectQuery, java.util.ArrayList...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 13.825)
- **Top Global Matches:** file_cluster_6: 13.825, file_cluster_4: 17.255, file_cluster_8: 18.795
- **Magnitude:** 577.86 | **LOC:** 717 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.65; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.7%), Complexity Load (formerly Cognitive Load) (73.2%), Debt Markers (formerly Tech Debt) (23.5%)
- **Documentation Coverage:** 82.1429% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addField` **(Many-Argument Workhorses)** (Impact: 67.0)
  * `getResult` **(Many-Argument Workhorses)** (Impact: 42.8)
  * `getSourceField` **(Compute Cores)** (Impact: 41.3)
  * `addFile` **(Many-Argument Workhorses)** (Impact: 35.3)
  * `analyzeAnnotations` **(Compute Cores)** (Impact: 26.6)
    * *Intent:* /** * determines the values of (direct or inherited) annotations of select list elements * @param an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 91`, `args: 22`, `func_start: 22`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 87`, `state_mutation: 116`, `dead_code: 1`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `io: 15`, `api: 9`, `import: 9`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.65
  * `Choke Point (Betweenness):` 0.00043 | `Ripple Effect (Closeness):` 0.008945
  * `Imports (Out-Degree: 9):` com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, java.util.ArrayList...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.406)
- **Top Global Matches:** file_cluster_5: 9.406, file_cluster_12: 9.825, file_cluster_4: 10.436
- **Magnitude:** 565.84 | **LOC:** 677 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 52.9)
  * `changeLineBreaks` **(Many-Argument Workhorses)** (Impact: 45.2)
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `changeLineBreaksAfterColumn` **(Stateful Encapsulated Methods)** (Impact: 28.3)
  * `isDeclarationSuitedForMultiDeclarations` **(Many-Argument Workhorses)** (Impact: 26.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 71 instances
* *State Mutation (weighted view):* 219
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 97`, `args: 32`, `func_start: 32`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 77`, `dead_code: 2`, `unreferenced_by_name: 11`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 8`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/LocalDeclarationOrderRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.245)
- **Top Global Matches:** file_cluster_4: 11.245, file_cluster_5: 11.472, file_cluster_12: 12.444
- **Magnitude:** 531.6 | **LOC:** 764 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **26**; blast radius 0.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.3%), Complexity Load (formerly Cognitive Load) (65.9%)
- **Documentation Coverage:** 67.3913% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `moveSection` **(Many-Argument Workhorses)** (Impact: 80.4)
    * *Intent:* /** moves the supplied Section to the next write position under the supplied ('enclosing') parent Co...
  * `moveTermInChain` **(Many-Argument Workhorses)** (Impact: 41.5)
    * *Intent:* /** moves the supplied Term to the next write position within the chain, adjusts whitespace before a...
  * `extendSectionStart` **(Compute Cores)** (Impact: 30.0)
    * *Intent:* /** extends the start of a to-be-moved Section with preceding attached comments */
  * `rearrange` **(Many-Argument Workhorses)** (Impact: 27.8)
    * *Intent:* /** rearranges all declarations of the supplied type in the configured order */
  * `getLineBreaksBetween` **(Stateful Encapsulated Methods)** (Impact: 18.9)
    * *Intent:* /** returns the number of line breaks to put between the supplied commands (or between command 1 and...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 167
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 131`, `structural_boundaries: 140`, `args: 33`, `func_start: 33`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 57`, `dead_code: 1`, `unreferenced_by_name: 12`
* *Architecture:* `api: 14`, `import: 26`
* *Defense:* `safety: 4`, `doc: 15`, `immutability_locks: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Section, com.sap.adt.abapcleaner.parser.Term, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectListsRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.49)
- **Top Global Matches:** file_cluster_4: 11.49, file_cluster_6: 12.557, file_cluster_5: 13.2
- **Magnitude:** 483.14 | **LOC:** 508 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **29**; blast radius 0.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `executeOn` **(Many-Argument Workhorses)** (Impact: 113.7)
  * `buildTableFromSpaceSepList` **(Many-Argument Workhorses)** (Impact: 40.6)
  * `buildTableFromCommaSepList` **(Many-Argument Workhorses)** (Impact: 29.0)
  * `determineLayout` **(Stateful Encapsulated Methods)** (Impact: 19.0)
  * `executeOn` **(Stateful Encapsulated Methods)** (Impact: 14.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 69 instances
* *State Mutation (weighted view):* 212
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 97`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 25`, `state_mutation: 74`, `dead_code: 1`, `unreferenced_by_name: 9`
* *Architecture:* `api: 16`, `import: 29`
* *Defense:* `safety: 4`, `immutability_locks: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 30):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Term, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch, com.sap.adt.abapcleaner.parser.TokenType...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.687)
- **Top Global Matches:** file_cluster_12: 8.687, file_cluster_5: 9.829, file_cluster_7: 10.199
- **Magnitude:** 462.38 | **LOC:** 2336 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 0.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (28.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.5%), Complexity Load (formerly Cognitive Load) (10.2%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.4%)
- **Documentation Coverage:** 99.4186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `assertAccessType` **(Stateful Encapsulated Methods)** (Impact: 16.9)
    * *Intent:* /** * Checks the memory access type that is determined by {@link Token#getMemoryAccessType()} for th...
  * `assertMemoryAccessType` **(Stateful Encapsulated Methods)** (Impact: 15.0)
  * `assertLastTokenOfLogExpr` **(Encapsulated Accessors)** (Impact: 4.3)
  * `assertTextBits` **(Stateful Encapsulated Methods)** (Impact: 4.2)
  * `buildCommand` **(Stateful Encapsulated Methods)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 231`, `args: 182`, `func_start: 172`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 73`, `unreferenced_by_name: 148`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 122`, `doc: 1`, `test: 916`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.comparer.TextBit, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 5.943)
- **Top Global Matches:** file_cluster_13: 5.943, file_cluster_10: 6.563, file_cluster_2: 7.275
- **Magnitude:** 445.72 | **LOC:** 3395 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.55; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (48.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (14.5%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (2.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testComplexParametersWithExporting` **(Callbacks & Closures)** (Impact: 2.0)
  * `testParametersWithAsteriskComments` **(Callbacks & Closures)** (Impact: 2.0)
  * `testComplexParametersWithComment` **(Callbacks & Closures)** (Impact: 2.0)
  * `testValueConstructorInsideParamList` **(Annotated & Test Methods)** (Impact: 2.0)
  * `testMoveParamLeftOfAssignOp` **(Annotated & Test Methods)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 168`, `args: 234`, `func_start: 161`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 90`, `unreferenced_by_name: 160`
* *Architecture:* `import: 5`
* *Defense:* `test: 165`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Assertions.assertFalse, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.863)
- **Top Global Matches:** file_cluster_5: 8.863, file_cluster_7: 9.594, file_cluster_12: 9.785
- **Magnitude:** 438.7 | **LOC:** 400 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **2**; blast radius 1.881; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (96.3%), Guard Balance (formerly Safety Score) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `align` **(Many-Argument Workhorses)** (Impact: 139.2)
    * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMul...
  * `overrideWidthIfColumnIsFollowedByLineBreaks` **(Compute Cores)** (Impact: 12.7)
  * `getTotalMonoLineWidth` **(I/O & Config Routines)** (Impact: 4.8)
  * `removeLineAt` **(Compute Cores)** (Impact: 4.7)
  * `removeAllLinesOfParent` **(Compute Cores)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 62 instances
* *State Mutation (weighted view):* 189
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 46`, `args: 25`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 65`
* *Architecture:* `api: 29`
* *Defense:* `doc: 2`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.881
  * `Choke Point (Betweenness):` 0.000572 | `Ripple Effect (Closeness):` 0.168063
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.parser.*, java.util.*
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Term.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.892)
- **Top Global Matches:** file_cluster_12: 7.892, file_cluster_7: 8.281, file_cluster_5: 9.679
- **Magnitude:** 425.78 | **LOC:** 480 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **2**; blast radius 5.766; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (94.2%), Connectivity (formerly Api Exposure) (90.5%), Guard Balance (formerly Safety Score) (76.3%)
- **Documentation Coverage:** 95.1807% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Term` **(Compute Cores)** (Impact: 62.5)
  * `removeFromCommand` **(Compute Cores)** (Impact: 23.2)
  * `isFirstTokenAllowed` **(Compute Cores)** (Impact: 10.6)
  * `getMaxEndIndexInAnyLine` **(Compute Cores)** (Impact: 9.7)
  * `Term` **(Stateful Encapsulated Methods)** (Impact: 7.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 52 instances
* *State Mutation (weighted view):* 159
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 89`, `args: 46`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 55`, `dead_code: 1`
* *Architecture:* `api: 40`
* *Defense:* `doc: 3`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.766
  * `Choke Point (Betweenness):` 4.1e-05 | `Ripple Effect (Closeness):` 0.244152
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/position/DdlPositionAssociationRule.java` (JAVA) | Magnitude: 29.98 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 75, structural_boundaries: 34, core_var_decl: 20, design_camel_case: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignPerformTest.java` (JAVA) | Magnitude: 55.46 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 271, args: 29, structural_boundaries: 23, state_mutation: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleGroup.java` (JAVA) | Magnitude: 43.24 | Delta: **0.133** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 63, structural_boundaries: 25, branch: 20, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/programbase/ProgramTest.java` (JAVA) | Magnitude: 16.42 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 43, test: 16, structural_boundaries: 12, core_var_decl: 7
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/EqualsSignChainRule.java` (JAVA) | Magnitude: 76.74 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 112, core_var_decl: 31, structural_boundaries: 29, design_camel_case: 17
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignColumn.java` (JAVA) | Magnitude: 262.52 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 264, structural_boundaries: 65, core_var_decl: 61, branch: 49
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java` (JAVA) | Magnitude: 378.38 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 540, core_var_decl: 110, structural_boundaries: 92, branch: 80
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/TreeAlignColumn.java` (JAVA) | Magnitude: 106.94 | Delta: **0.111** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 117, structural_boundaries: 35, branch: 32, args: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationTest.java` (JAVA) | Magnitude: 189.56 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 1574, state_mutation: 68, structural_boundaries: 53, args: 46
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/ICancelable.java` (JAVA) | Magnitude: 2.58 | Delta: **0.06** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignLogicalExpressionsTest.java` (JAVA) | Magnitude: 118.4 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 995, structural_boundaries: 41, state_mutation: 34, args: 32
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/commands/IfBlockAtLoopEndTest.java` (JAVA) | Magnitude: 44.26 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 320, core_var_decl: 69, design_snake_case: 69, state_mutation: 19
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignEntityParametersTest.java` (JAVA) | Magnitude: 37.04 | Delta: **0.109** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 242, structural_boundaries: 17, state_mutation: 16, args: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` (JAVA) | Magnitude: 690.78 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 546, core_var_decl: 145, branch: 135, state_mutation: 126

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/ParseException.java` (JAVA) | Magnitude: 12.72 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 11, structural_boundaries: 5, api: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/CleanupRange.java` (JAVA) | Magnitude: 12.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_tabs: 11, api: 5, structural_boundaries: 4, doc: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/MemoryAccessType.java` (JAVA) | Magnitude: 9.58 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 16, doc: 8, api: 4, state_mutation: 3
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/WordFrequency.java` (JAVA) | Magnitude: 12.26 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_tabs: 10, api: 6, state_mutation: 4, structural_boundaries: 2
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxAfterChanges.java` (JAVA) | Magnitude: 13.56 | Delta: **0.067** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 9, structural_boundaries: 5, api: 5, args: 4
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxBeforeChanges.java` (JAVA) | Magnitude: 7.24 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, api: 3, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/prettyprinter/CamelCaseInCdsTestTest.java` (JAVA) | Magnitude: 55.42 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 673, core_var_decl: 87, design_snake_case: 72, args: 34
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/position/DdlPositionAssociationTest.java` (JAVA) | Magnitude: 68.02 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 509, state_mutation: 24, structural_boundaries: 23, args: 17
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/spaces/DdlCamelCaseNameTest.java` (JAVA) | Magnitude: 53.88 | Delta: **0.098** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 486, structural_boundaries: 22, args: 15, func_start: 15
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignFunctionParametersTest.java` (JAVA) | Magnitude: 39.7 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 325, core_var_decl: 116, design_snake_case: 114, dead_code: 26

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/spaces/ClosingBracketsPositionRule.java` (JAVA) | Magnitude: 107.08 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 109, structural_boundaries: 28, core_var_decl: 28, design_snake_case: 21
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectClausesRule.java` (JAVA) | Magnitude: 199.82 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_tabs: 230, structural_boundaries: 70, core_var_decl: 59, design_camel_case: 47
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/EmptySectionsInClassDefRule.java` (JAVA) | Magnitude: 105.52 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 149, structural_boundaries: 59, branch: 23, core_var_decl: 18
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignAliasesForRule.java` (JAVA) | Magnitude: 154.44 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 128, structural_boundaries: 38, core_var_decl: 28, branch: 25

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands/CallMethodRule.java` (JAVA) | Magnitude: 62.86 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 108, structural_boundaries: 40, core_var_decl: 22, args: 17
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` (JAVA) | Magnitude: 72.76 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 121, structural_boundaries: 74, import: 47, core_var_decl: 42
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignSelectListRule.java` (JAVA) | Magnitude: 280.8 | Delta: **0.068** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 319, structural_boundaries: 89, core_var_decl: 76, branch: 66
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CustomCamelCaseNames.java` (JAVA) | Magnitude: 45.16 | Delta: **0.084** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_tabs: 54, structural_boundaries: 20, core_var_decl: 13, branch: 8
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/emptylines/CdsTestClassLinesRule.java` (JAVA) | Magnitude: 210.62 | Delta: **0.1** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 232, structural_boundaries: 78, core_var_decl: 67, branch: 51

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java` (JAVA) | Magnitude: 952.84 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 738, core_var_decl: 258, branch: 209, design_camel_case: 144
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java` (JAVA) | Magnitude: 610.46 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_tabs: 483, branch: 144, core_var_decl: 135, design_camel_case: 105

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/SectionTest.java` (JAVA) | Magnitude: 54.74 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 168, test: 42, core_var_decl: 29, structural_boundaries: 22
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/TextSettingsWriter.java` (JAVA) | Magnitude: 141.58 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 77, args: 31, func_start: 31
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/commands/RaiseTypeRule.java` (JAVA) | Magnitude: 52.22 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_tabs: 68, structural_boundaries: 37, api: 14, core_var_decl: 14
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` (JAVA) | Magnitude: 3198.08 | Delta: **0.21** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_tabs: 2498, branch: 1012, structural_boundaries: 664, core_var_decl: 459

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> Churn: **60.89%** | Cog Load: 86.7174% | Debt: 8.3615%
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> Churn: **55.68%** | Cog Load: 86.6553% | Debt: 8.4156%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3198.08
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3145.82
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1991.26
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1561.16
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1006.96

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 6.622** (Bridge: 0.1038 * Flux: 63.7789%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` -> **Severity: 3.276** (Bridge: 0.0328 * Flux: 99.9877%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 3.012** (Bridge: 0.0301 * Flux: 99.9996%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` -> **Severity: 1.452** (Bridge: 0.0145 * Flux: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Task.java` -> **Severity: 1.225** (Bridge: 0.0123 * Flux: 99.9987%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 30.866** (Embedded: 0.3858 * Error Risk: 80.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Severity: 30.228** (Embedded: 0.3583 * Error Risk: 84.3678%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` -> **Severity: 29.475** (Embedded: 0.3259 * Error Risk: 90.4365%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 29.22** (Embedded: 0.3425 * Error Risk: 85.3255%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Program.java` -> **Severity: 23.624** (Embedded: 0.3114 * Error Risk: 75.8716%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 14741.811** (Blast Radius: 182.373 * Doc Risk: 80.8333%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/Cult.java` -> **Severity: 14327.06** (Blast Radius: 167.149 * Doc Risk: 85.7143%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -> **Severity: 2849.0** (Blast Radius: 28.49 * Doc Risk: 100.0%)
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java` -> **Severity: 2100.4** (Blast Radius: 21.004 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 1688.641** (Blast Radius: 21.986 * Doc Risk: 76.8053%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 316 literal sites + 4 sites through wrappers = 320

- `getLineToMove` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ValueStatementRule.java`
- `getSection` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/LocalDeclarationOrderRule.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 28022 call pairs -- scoped 72.0%, unique 0.3%, ambiguous 13.8%, external 14.0%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 28022 | 72.0% | 0.3% | 13.8% | 14.0% |

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
