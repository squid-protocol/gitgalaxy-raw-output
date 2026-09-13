# ARCHITECTURAL_BRIEF: abap-cleaner
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/SAP/abap-cleaner` |
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
| Avg Path Length | 2.8349 | Hops between files. Lower = Tighter coupling. |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

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
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 98.9 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 17.4 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 91.7 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `identifyComment` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`) -> Impact: **355.1** | LOC: 328
- `determineMemoryAccessType` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java`) -> Impact: **253.7** | LOC: 553
- `refine` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java`) -> Impact: **180.2** | LOC: 125
- `processKeyPressedEvent` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) -> Impact: **179.5** | LOC: 252
- `create` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> Impact: **178.4** | LOC: 208
- `align` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java`) -> Impact: **168.6** | LOC: 188
  * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMultiline true = a Term may cover multiple lines; fal...
- `align` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/TreeAlign.java`) -> Impact: **163.2** | LOC: 153
- `obfuscateIdentifier` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java`) -> Impact: **159.6** | LOC: 151
- `buildAlignTable` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **148.5** | LOC: 177
- `alignParams` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`) -> Impact: **147.6** | LOC: 180

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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignAssignmentsRule.java` (JAVA) -> Cumulative Risk: **711.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 127.66 | **LOC:** 207 | **CtrlFlow:** 11.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9972%), Tech Debt (97.4294%)
- **Heaviest Functions:** `executeOn` (Impact: 31.2), `alignSection` (Impact: 10.3), `getExample` (Impact: 3.4)

### 2. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationWriter.java` (JAVA) -> Cumulative Risk: **702.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 176.04 | **LOC:** 188 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9844%)
- **Heaviest Functions:** `startAnnotation` (Impact: 25.4), `addToken` (Impact: 9.8), `addComma` (Impact: 7.4)

### 3. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA) -> Cumulative Risk: **691.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1181.56 | **LOC:** 1455 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6484%), Tech Debt (99.2741%), Documentation (94.4444%)
- **Heaviest Functions:** `processKeyPressedEvent` (Impact: 179.5), `getLineBackground` (Impact: 106.9), `paintCode` (Impact: 102.0)

### 4. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CleanException.java` (JAVA) -> Cumulative Risk: **691.73**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 69.12 | **LOC:** 68 | **CtrlFlow:** 43.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.6316%), Safety Score (97.0606%)
- **Heaviest Functions:** `CleanException` (Impact: 22.4), `CleanException` (Impact: 11.5), `getMessage` (Impact: 6.5)

### 5. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignClearFreeAndSortRule.java` (JAVA) -> Cumulative Risk: **689.66**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 226.44 | **LOC:** 285 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `executeOn` (Impact: 94.2), `getExample` (Impact: 6.9), `getDescription` (Impact: 3.2)

### 6. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/ImplicitTypeRule.java` (JAVA) -> Cumulative Risk: **687.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 293.06 | **LOC:** 342 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `executeOn` (Impact: 81.5), `executeOn` (Impact: 44.5), `getExample` (Impact: 19.0)

### 7. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/CommentTypeRule.java` (JAVA) -> Cumulative Risk: **687.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 190.26 | **LOC:** 225 | **CtrlFlow:** 28.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Cognitive Load (98.378%)
- **Heaviest Functions:** `executeOn` (Impact: 66.1), `createSeparator` (Impact: 21.5), `getExample` (Impact: 3.5)

### 8. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignCellTerm.java` (JAVA) -> Cumulative Risk: **687.2**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 111.82 | **LOC:** 98 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `setWhitespace` (Impact: 36.2), `createSpecial` (Impact: 4.3), `getMonoLineWidth` (Impact: 3.2)

### 9. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignPerformRule.java` (JAVA) -> Cumulative Risk: **685.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 199.12 | **LOC:** 313 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9976%), Tech Debt (98.4839%)
- **Heaviest Functions:** `executeOn` (Impact: 44.8), `condenseParameterLists` (Impact: 13.5), `setForceLineBreakAndIndent` (Impact: 12.8)

### 10. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffNavigator.java` (JAVA) -> Cumulative Risk: **684.92**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 672.82 | **LOC:** 597 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.665%), Cognitive Load (98.2498%)
- **Heaviest Functions:** `search` (Impact: 99.4), `reprocessSelection` (Impact: 65.9), `isLineBitHighlighted` (Impact: 17.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3359.58 | **LOC:** 3950 | **CtrlFlow:** 42.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.215%), Tech Debt (8.4156%)
**Top Internal Functions/Classes:**
  * `determineMemoryAccessType` (Impact: 253.7)
  * `getLastTokenOfSequence` (Impact: 141.3)
  * `getStrucInfo` (Impact: 94.2)
    * *Intent:* /** returns a StrucInfo instance if the Token as a whole is the name of a structure or one of its co...
  * `getLastTokenOfLogicalExpression` (Impact: 87.5)
    * *Intent:* /** * If this Token starts a logical expression, the last code Token of the logical expression is re...
  * `toTextBits` (Impact: 76.3)
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
  * `Choke Point (Betweenness):` 0.026267 | `Ripple Effect (Closeness):` 0.201039
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.Rule, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.LogicalExpression, java.security.InvalidParameterException, java.util.*
  * `Imported By (In-Degree: 72):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3258.92 | **LOC:** 4192 | **CtrlFlow:** 31.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (87.2373%), Tech Debt (8.3615%)
**Top Internal Functions/Classes:**
  * `canAddToDdl` (Impact: 122.5)
  * `changesSySubrc` (Impact: 109.8)
    * *Intent:* /** Returns true if the Command changes sy-subrc */
  * `distinguishOperators` (Impact: 101.4)
  * `finishBuild` (Impact: 97.4)
  * `handleChainElement` (Impact: 95.8)
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
  * `Choke Point (Betweenness):` 3.6e-05 | `Ripple Effect (Closeness):` 0.207299
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.base.ABAP.SyField, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.RuleID, java.util.*
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2212.76 | **LOC:** 2986 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (95.0921%), Tech Debt (35.1543%)
**Top Internal Functions/Classes:**
  * `createContents` (Impact: 104.0)
    * *Intent:* /** * Create contents of the window. */
  * `refreshCode` (Impact: 65.6)
  * `createReleaseNoteDocumentation` (Impact: 52.7)
  * `open` (Impact: 50.6)
    * *Intent:* /** * @wbp.parser.entryPoint */
  * `patternMatchesToClip` (Impact: 49.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00361
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.comparer.*, com.sap.adt.abapcleaner.comparer.ChangeTypes, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.io.IOException...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1774.66 | **LOC:** 1972 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (97.2967%), Tech Debt (11.4851%)
**Top Internal Functions/Classes:**
  * `createContents` (Impact: 87.0)
    * *Intent:* /** * Create contents of the window. */
  * `importProfiles` (Impact: 45.2)
  * `generateUnitTestClass` (Impact: 43.0)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `setProfile` (Impact: 41.5)
  * `exportProfiles` (Impact: 41.3)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1405.84 | **LOC:** 1252 | **CtrlFlow:** 46.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (7.9563%)
**Top Internal Functions/Classes:**
  * `identifyComment` (Impact: 355.1)
  * `preprocessLine` (Impact: 117.5)
  * `getWordFrequencies` (Impact: 113.7)
  * `initialize` (Impact: 61.4)
  * `addCommentSamples` (Impact: 51.2)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.083838
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.Program, java.io.BufferedReader, java.io.IOException, java.io.InputStream, java.io.InputStreamReader, java.nio.charset.StandardCharsets, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1181.56 | **LOC:** 1455 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.3923%), Tech Debt (99.2741%)
**Top Internal Functions/Classes:**
  * `processKeyPressedEvent` (Impact: 179.5)
  * `getLineBackground` (Impact: 106.9)
  * `paintCode` (Impact: 102.0)
  * `generateUnitTest` (Impact: 60.9)
    * *Intent:* /** builds the Java code for a Unit Test from the currently selected code */
  * `getTextForeground` (Impact: 52.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1020.86 | **LOC:** 1158 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.6376%), Tech Debt (8.0175%)
**Top Internal Functions/Classes:**
  * `isComparisonOperator` (Impact: 117.1)
  * `negateComparisonOperator` (Impact: 100.0)
  * `isCharAllowedForTypeNames` (Impact: 49.4)
  * `isCharAllowedForVariableNames` (Impact: 48.7)
  * `mayBeVariableName` (Impact: 33.0)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1015.04 | **LOC:** 1070 | **CtrlFlow:** 31.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (8.0464%)
**Top Internal Functions/Classes:**
  * `buildAlignTable` (Impact: 148.5)
  * `alignParams` (Impact: 147.6)
  * `executeOn` (Impact: 76.8)
  * `determineTableStart` (Impact: 70.4)
  * `determineKeepOnSingleLine` (Impact: 37.0)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.00722
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.rulehelpers.*, java.time.LocalDate, java.util.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 883.3 | **LOC:** 831 | **CtrlFlow:** 34.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (62.8013%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `split` (Impact: 44.7)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` (Impact: 39.6)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `split` (Impact: 39.6)
    * *Intent:* /** * returns null only if text == null, otherwise a String array that may have .length == 0 if empt...
  * `containsAt` (Impact: 36.1)
  * `indexOfAny` (Impact: 30.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 832.34 | **LOC:** 805 | **CtrlFlow:** 40.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (84.0943%), Tech Debt (8.1995%)
**Top Internal Functions/Classes:**
  * `negate` (Impact: 94.1)
  * `LogicalExpression` (Impact: 66.7)
  * `calculateComplexity` (Impact: 56.7)
    * *Intent:* /** * Calculates the {@link #currentComplexity} of this LogicalExpression and all its inner expressi...
  * `removeFirstNeedlessParentheses` (Impact: 54.6)
  * `toTreeAlign` (Impact: 49.0)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 819.2 | **LOC:** 875 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createFromTextFiles` (Impact: 95.5)
  * `preprocessFromGTNC` (Impact: 76.9)
  * `createFromTextFile` (Impact: 69.6)
  * `checkDiscardReasons` (Impact: 49.7)
  * `applyCamelCaseTo` (Impact: 37.0)
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
  * `Choke Point (Betweenness):` 0.000162 | `Ripple Effect (Closeness):` 0.090054
  * `Imports (Out-Degree: 6):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.base.Cult, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.Persistency, com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.rulebase.Profile, java.io.BufferedReader, java.io.BufferedWriter...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 810.44 | **LOC:** 970 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.8054%), Tech Debt (48.1477%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 55.4)
  * `alignGenericTypeComponents` (Impact: 49.8)
    * *Intent:* /** aligns the components of TYPE ANY STRUCTURE CONTAINING ... */
  * `readDeclarationLine` (Impact: 41.6)
  * `buildTable` (Impact: 39.5)
  * `joinColumns` (Impact: 30.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 773.94 | **LOC:** 856 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (83.0333%), Tech Debt (9.5828%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 91.9)
  * `executeOnOtherCommand` (Impact: 65.8)
  * `addMethodDefinitions` (Impact: 54.4)
  * `executeOnDeclarationCommand` (Impact: 45.6)
  * `isNeededPragmaOrPseudoCommentFound` (Impact: 37.7)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 763.18 | **LOC:** 2336 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.8628%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAccessTypeInternalTables` (Impact: 53.9)
  * `testAccessTypeStringProcessing` (Impact: 34.0)
  * `assertAccessType` (Impact: 24.0)
    * *Intent:* /** * Checks the memory access type that is determined by {@link Token#getMemoryAccessType()} for th...
  * `assertMemoryAccessType` (Impact: 23.0)
  * `testAccessTypeTableExpression` (Impact: 17.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 709.08 | **LOC:** 733 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.7382%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expandCleanupRange` (Impact: 40.1)
  * `compareWithSource` (Impact: 31.9)
  * `checkSyntax` (Impact: 29.3)
  * `replacePart` (Impact: 26.6)
  * `toDisplayLines` (Impact: 13.8)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 672.82 | **LOC:** 597 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (98.2498%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 99.4)
  * `reprocessSelection` (Impact: 65.9)
  * `isLineBitHighlighted` (Impact: 17.7)
  * `reprocessAll` (Impact: 14.5)
  * `refreshCode` (Impact: 12.8)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 660.06 | **LOC:** 678 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (86.0113%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeTo` (Impact: 66.8)
  * `add` (Impact: 59.4)
  * `checkNestingFor` (Impact: 50.8)
  * `adjustNesting` (Impact: 36.3)
  * `determineTablesInArrays` (Impact: 24.9)
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
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.085206
  * `Imports (Out-Degree: 10):` com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 627.48 | **LOC:** 466 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.7654%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `obfuscateIdentifier` (Impact: 159.6)
  * `getVariableName` (Impact: 74.2)
  * `obfuscate` (Impact: 61.7)
  * `getTypeName` (Impact: 20.6)
  * `clearMaps` (Impact: 15.3)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 620.76 | **LOC:** 717 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (76.4188%), Tech Debt (23.5128%)
**Top Internal Functions/Classes:**
  * `addField` (Impact: 71.0)
  * `getResult` (Impact: 53.2)
  * `getSourceField` (Impact: 44.8)
  * `addFile` (Impact: 35.3)
  * `analyzeAnnotations` (Impact: 31.8)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 582.44 | **LOC:** 677 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (42.3416%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 52.9)
  * `changeLineBreaks` (Impact: 47.4)
  * `executeOn` (Impact: 38.6)
  * `changeLineBreaksAfterColumn` (Impact: 30.6)
  * `isDeclarationSuitedForMultiDeclarations` (Impact: 28.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 573.22 | **LOC:** 2569 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2765%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBoundStructuresWith2KeywordsUnused` (Impact: 22.1)
  * `testNestedBoundStructuresUsedInComment` (Impact: 15.4)
  * `testNestedBoundStructuresUnused` (Impact: 15.2)
  * `testBoundStructuresUnused` (Impact: 14.1)
  * `testRemoveObsoleteComments` (Impact: 10.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 566.94 | **LOC:** 633 | **CtrlFlow:** 83.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (50.2562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAlwaysPutEmptyLines` (Impact: 39.7)
  * `testKeepEmptyLines` (Impact: 39.6)
  * `testSortByFirstLevelOnly` (Impact: 39.5)
  * `testPutEmptyLinesForNewFirstElemOnly` (Impact: 39.5)
  * `testNestingFromLevel2` (Impact: 33.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 565.2 | **LOC:** 764 | **CtrlFlow:** 27.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7437%), Tech Debt (41.6335%)
**Top Internal Functions/Classes:**
  * `moveSection` (Impact: 85.7)
    * *Intent:* /** moves the supplied Section to the next write position under the supplied ('enclosing') parent Co...
  * `moveTermInChain` (Impact: 43.7)
    * *Intent:* /** moves the supplied Term to the next write position within the chain, adjusts whitespace before a...
  * `rearrange` (Impact: 30.6)
    * *Intent:* /** rearranges all declarations of the supplied type in the configured order */
  * `variableMatchesFilter` (Impact: 30.6)
    * *Intent:* /** returns true if the supplied variable shall be processed under the supplied declaration type; * ...
  * `extendSectionStart` (Impact: 30.0)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 497.54 | **LOC:** 508 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (100.0%), Tech Debt (42.1765%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 118.6)
  * `buildTableFromSpaceSepList` (Impact: 40.6)
  * `buildTableFromCommaSepList` (Impact: 29.0)
  * `determineLayout` (Impact: 23.5)
  * `executeOn` (Impact: 16.1)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 482.8 | **LOC:** 400 | **CtrlFlow:** 36.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (98.2888%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `align` (Impact: 168.6)
    * *Intent:* /** * aligns all cells of the table * * @param basicIndent * @param firstLineBreaks * @param keepMul...
  * `overrideWidthIfColumnIsFollowedByLineBreaks` (Impact: 15.5)
  * `removeLineAt` (Impact: 6.1)
  * `getTotalMonoLineWidth` (Impact: 5.8)
  * `getTotalMultiLineWidth` (Impact: 4.7)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> Churn: **56.94%** | Cog Load: 87.2373% | Debt: 8.3615%
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> Churn: **52.07%** | Cog Load: 87.215% | Debt: 8.4156%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3359.58
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3258.92
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 2212.76
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1774.66
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1181.56

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 2.627** (Bridge: 0.0263 * Flux: 99.9996%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 2.253** (Bridge: 0.0353 * Flux: 63.7789%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` -> **Severity: 0.881** (Bridge: 0.0088 * Flux: 99.9877%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxException.java` -> **Severity: 0.375** (Bridge: 0.0049 * Flux: 76.8525%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/prettyprinter/CamelCaseNameRule.java` -> **Severity: 0.267** (Bridge: 0.0027 * Flux: 97.5892%)

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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
