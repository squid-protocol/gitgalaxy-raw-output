# ARCHITECTURAL_BRIEF: abap-cleaner
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/abap-cleaner` |
| **Timestamp** | `2026-08-03T19:23:47.951976+00:00` |
| **Scan Duration** | `2.71s` |
| **Git Branch** | `main` |
| **Git Commit** | `952c68076fb0c5a258d947ca269e876d12603190` |
| **Git Remote** | `https://github.com/SAP/abap-cleaner` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 535 malicious artifacts.

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
| Total Artifacts | 731 |
| Analyzed Artifacts (Scanned) | 550 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 181 |
| Total LOC | 103796 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 75.2% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3806 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2748 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 6.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8349 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 26 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 535 | 103726 | 97.3% |
| XML | 5 | 0 | 0.9% |
| PLAINTEXT | 5 | 0 | 0.9% |
| MARKDOWN | 2 | 0 | 0.4% |
| HTML | 2 | 53 | 0.4% |
| JSON | 1 | 17 | 0.2% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.44`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 403 | 73.3% |
| file_cluster_13 | 98 | 17.8% |
| file_cluster_0 | 40 | 7.3% |
| file_cluster_9 | 1 | 0.2% |
| file_cluster_16 | 1 | 0.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 7 | 1.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 181*

**Composition by Extension & Reason:**
- `.md`: 106x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 32x Excluded (Explicitly Denied Extension: '.png')
- `no_extension`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 204015 LOC exceeds safe regex boundaries), 1x Excluded (Monolithic Amalgamation: 145392 LOC exceeds safe regex boundaries)
- `.yml`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.prefs`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mf`: 2x Excluded (Unsupported Extension: '.MF'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.toml`: 1x Excluded (Unsupported Extension: '.toml')
- `.product`: 1x Excluded (Unsupported Extension: '.product')
- `.ico`: 1x Excluded (Explicitly Denied Extension: '.ico')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 84.6 | 14.8 | 9.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.6 | 41.9 | 51.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 44.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 23.5 | 2.2 | 0.0 |
| API Exposure | 0.0 | 16.5 | 6.2 | 6.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 79.6 | 4.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 21.0 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 56.5 | 73.3 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 3.9 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.2 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `create` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> Impact: **696.2** | LOC: 207
- `compareTo` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java`) -> Impact: **577.8** | LOC: 160
- `refine` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java`) -> Impact: **494.2** | LOC: 125
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java`) -> Impact: **425.3** | LOC: 276
- `refine` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefiner.java`) -> Impact: **334.9** | LOC: 259
  * *Intent:* /** * <p>Implementation of the {@link ITokenTypeRefiner} interface which uses ABAP cleaner-internal means of * refining the {@link TokenType}s that we...
- `distinguishOperators` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java`) -> Impact: **323.7** | LOC: 124
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectClausesRule.java`) -> Impact: **302.6** | LOC: 148
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ValueStatementRule.java`) -> Impact: **299.8** | LOC: 182
- `getWordFrequencies` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`) -> Impact: **268.0** | LOC: 160
- `align` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java`) -> Impact: **262.9** | LOC: 188

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `compareTo` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java`) -> **O(2^N) [Recursive]**
- `getLoadPaths` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java`) -> **O(2^N) [Recursive]**
- `getSavePath` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java`) -> **O(2^N) [Recursive]**
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleForLogicalExpressions.java`) -> **O(2^N) [Recursive]**
- `open` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /**
- `add` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffDoc.java`) -> **O(2^N) [Recursive]**
- `toContextInfo` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/KeywordMetrics.java`) -> **O(2^N) [Recursive]**
- `create` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> **O(2^N) [Recursive]**
- `buttonClicked` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> **O(2^N) [Recursive]**
- `containsSourceLineNum` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffLine.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `createContents` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> DB Complexity: **147**
- `createContents` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfileDirs.java`) -> DB Complexity: **47**
- `createContents` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmImportTestCode.java`) -> DB Complexity: **33**
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignCondExpressionsRule.java`) -> DB Complexity: **25**
- `setProfile` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> DB Complexity: **23**
- `CodeDisplay` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java`) -> DB Complexity: **17**
- `createContents` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmInputBox.java`) -> DB Complexity: **17**
- `setControlsHighlight` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> DB Complexity: **16**
- `toTreeAlign` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java`) -> DB Complexity: **15**
  * *Intent:* // adjust the first token, including for parent expressions, esp. for cases where the first token is required // later to insert an opening parenthesi...
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectFromRule.java`) -> DB Complexity: **15**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers` | 56 | 9377.94 | 18.76% | 39.39% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser` | 32 | 6889.3 | 18.11% | 45.06% |
| `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui` | 31 | 5214.98 | 29.04% | 58.55% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment` | 45 | 4505.5 | 17.0% | 87.02% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase` | 28 | 2840.0 | 14.06% | 61.7% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base` | 22 | 2801.53 | 9.32% | 48.51% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations` | 13 | 2747.56 | 10.76% | 0.0% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment` | 17 | 2687.5 | 6.03% | 0.0% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations` | 26 | 2547.96 | 14.99% | 97.27% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase` | 27 | 2497.32 | 13.85% | 63.98% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundJob.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundTask.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/DummySearchControls.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/Message.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/CleanupResultWrapper.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmImportTestCode.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProgress.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigLabel.java` -> **99.9996%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **99.9994%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Config.java` -> **99.9969%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` -> **145** Orphaned Functions | **8** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` -> **117** Orphaned Functions | **12** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` -> **123** Orphaned Functions | **2** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` -> **111** Orphaned Functions | **2** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignLogicalExpressionsTest.java` -> **57** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java`** -> AI Confidence: **99.48%**
2. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignEntityParametersTest.java`** -> AI Confidence: **99.48%**
3. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignSourceParametersTest.java`** -> AI Confidence: **99.48%**
4. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationNestingTest.java`** -> AI Confidence: **99.48%**
5. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`** -> AI Confidence: **99.39%**
6. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/DdlObfuscatorTest.java`** -> AI Confidence: **99.39%**
7. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java`** -> AI Confidence: **99.34%**
8. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/spaces/DdlCamelCaseNameTest.java`** -> AI Confidence: **99.34%**
9. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`** -> AI Confidence: **99.32%**
10. **`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigIntBox.java`** -> AI Confidence: **99.31%**
11. **`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmMain.java`** -> AI Confidence: **99.31%**
12. **`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`** -> AI Confidence: **99.31%**
13. **`com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/MainSettings.java`** -> AI Confidence: **99.31%**
14. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/AbapObfuscator.java`** -> AI Confidence: **99.31%**
15. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/DdlObfuscator.java`** -> AI Confidence: **99.31%**
16. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Obfuscator.java`** -> AI Confidence: **99.31%**
17. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java`** -> AI Confidence: **99.31%**
18. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java`** -> AI Confidence: **99.31%**
19. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CamelCaseNames.java`** -> AI Confidence: **99.31%**
20. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java`** -> AI Confidence: **99.31%**
21. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/ReadTableCommand.java`** -> AI Confidence: **99.31%**
22. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/RuleForDdlAlignParameters.java`** -> AI Confidence: **99.31%**
23. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/RuleForDdlPosition.java`** -> AI Confidence: **99.31%**
24. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/SelectQuery.java`** -> AI Confidence: **99.31%**
25. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignClearFreeAndSortRule.java`** -> AI Confidence: **99.31%**
26. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java`** -> AI Confidence: **99.31%**
27. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsWithoutParamsRuleBase.java`** -> AI Confidence: **99.31%**
28. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersRule.java`** -> AI Confidence: **99.31%**
29. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectClausesRule.java`** -> AI Confidence: **99.31%**
30. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectFromRule.java`** -> AI Confidence: **99.31%**
31. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignFieldListsRule.java`** -> AI Confidence: **99.31%**
32. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignSelectListRule.java`** -> AI Confidence: **99.31%**
33. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/emptylines/DdlEmptyLinesBetweenSectionsRule.java`** -> AI Confidence: **99.31%**
34. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/emptylines/DdlEmptyLinesWithinSectionsRule.java`** -> AI Confidence: **99.31%**
35. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/position/RuleForDdlPositionJoinOrAssociation.java`** -> AI Confidence: **99.31%**
36. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/spaces/DdlCamelCaseNameRule.java`** -> AI Confidence: **99.31%**
37. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/spaces/DdlSpacesAroundSignsRule.java`** -> AI Confidence: **99.31%**
38. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/ClassDefinitionRule.java`** -> AI Confidence: **99.31%**
39. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/ImplicitTypeRule.java`** -> AI Confidence: **99.31%**
40. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/NeedlessClearRule.java`** -> AI Confidence: **99.31%**
41. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/UnusedParametersRule.java`** -> AI Confidence: **99.31%**
42. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesRule.java`** -> AI Confidence: **99.31%**
43. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/emptylines/CdsTestClassLinesRule.java`** -> AI Confidence: **99.31%**
44. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/prettyprinter/CamelCaseNameRule.java`** -> AI Confidence: **99.31%**
45. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/spaces/NeedlessSpacesRule.java`** -> AI Confidence: **99.31%**
46. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/PragmaPositionRule.java`** -> AI Confidence: **99.31%**
47. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/StringTemplateRule.java`** -> AI Confidence: **99.31%**
48. **`com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ValueStatementRule.java`** -> AI Confidence: **99.31%**
49. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java`** -> AI Confidence: **99.31%**
50. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java`** -> AI Confidence: **99.31%**
51. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/ProfileTest.java`** -> AI Confidence: **99.31%**
52. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTest.java`** -> AI Confidence: **99.31%**
53. **`test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java`** -> AI Confidence: **99.31%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Obfuscation & Evasion Surface
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/PersistencyBase.java` -> **0.0021%** Exposure
### Exploit Generation Surface
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigIntBox.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmInputBox.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffDoc.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmInputBox.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffDoc.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectClausesRule.java` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3072` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmImportTestCode.java` (JAVA) -> Cumulative Risk: **810.42**
- **Archetype:** `file_cluster_13` (Distance: 11.294 IQR)
- **Magnitude:** 200.36 | **LOC:** 209 | **CtrlFlow:** 28.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Logic Bomb (99.9999%), Algorithmic Dos (99.2903%)
- **Heaviest Functions:** `processCode` (Impact: 60.2), `open` (Impact: 22.1), `createContents` (Impact: 13.7)

### 2. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA) -> Cumulative Risk: **785.79**
- **Archetype:** `file_cluster_8` (Distance: 12.814 IQR)
- **Magnitude:** 2257.36 | **LOC:** 1972 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9994%)
- **Heaviest Functions:** `createContents` (Impact: 259.1), `open` (Impact: 131.1), `setProfile` (Impact: 121.0)

### 3. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` (JAVA) -> Cumulative Risk: **782.66**
- **Archetype:** `file_cluster_13` (Distance: 11.669 IQR)
- **Magnitude:** 159.06 | **LOC:** 257 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Injection Surface (100.0%), Concurrency (99.9993%), Algorithmic Dos (93.1955%)
- **Heaviest Functions:** `execute` (Impact: 39.9), `getAbapReleaseOfProject` (Impact: 29.1), `getAdtSourcePage` (Impact: 20.5)

### 4. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigIntBox.java` (JAVA) -> Cumulative Risk: **774.95**
- **Archetype:** `file_cluster_13` (Distance: 10.39 IQR)
- **Magnitude:** 230.0 | **LOC:** 162 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9998%), State Flux (97.5131%)
- **Heaviest Functions:** `txtValueKeyPressed` (Impact: 159.0), `detachControls` (Impact: 12.8), `ConfigIntBox` (Impact: 8.2)

### 5. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java` (JAVA) -> Cumulative Risk: **771.85**
- **Archetype:** `file_cluster_8` (Distance: 11.612 IQR)
- **Magnitude:** 798.32 | **LOC:** 273 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.8881%)
- **Heaviest Functions:** `compareTo` (Impact: 577.8), `findSimilarLines` (Impact: 135.3), `CompareDoc` (Impact: 12.3)

### 6. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectFromRule.java` (JAVA) -> Cumulative Risk: **764.45**
- **Archetype:** `file_cluster_13` (Distance: 10.904 IQR)
- **Magnitude:** 431.16 | **LOC:** 456 | **CtrlFlow:** 54.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (99.9528%), State Flux (91.9602%)
- **Heaviest Functions:** `executeOn` (Impact: 180.3), `executeOn` (Impact: 49.5), `calculateAddIndent` (Impact: 43.7)

### 7. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignSelectClausesRule.java` (JAVA) -> Cumulative Risk: **759.99**
- **Archetype:** `file_cluster_13` (Distance: 11.07 IQR)
- **Magnitude:** 413.32 | **LOC:** 322 | **CtrlFlow:** 51.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (96.257%)
- **Heaviest Functions:** `executeOn` (Impact: 302.6), `executeOn` (Impact: 33.1), `getExample` (Impact: 9.2)

### 8. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/AbapDocLangRule.java` (JAVA) -> Cumulative Risk: **691.73**
- **Archetype:** `file_cluster_8` (Distance: 9.396 IQR)
- **Magnitude:** 91.66 | **LOC:** 104 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9984%), Tech Debt (99.9929%)
- **Heaviest Functions:** `executeOn` (Impact: 37.0), `getExample` (Impact: 7.8), `AbapDocLangRule` (Impact: 2.2)

### 9. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmInputBox.java` (JAVA) -> Cumulative Risk: **688.37**
- **Archetype:** `file_cluster_13` (Distance: 10.21 IQR)
- **Magnitude:** 118.68 | **LOC:** 154 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.8134%)
- **Heaviest Functions:** `setResult` (Impact: 31.9), `open` (Impact: 19.0), `txtResultKeyPressed` (Impact: 14.1)

### 10. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/Variables.java` (JAVA) -> Cumulative Risk: **671.24**
- **Archetype:** `file_cluster_13` (Distance: 12.622 IQR)
- **Magnitude:** 231.42 | **LOC:** 224 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9876%), State Flux (99.8374%), Tech Debt (97.6135%)
- **Heaviest Functions:** `addDeclaration` (Impact: 25.2), `addUsage` (Impact: 23.7), `Variables` (Impact: 15.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.756 IQR)
- **Top Global Matches:** file_cluster_8: 11.756, file_cluster_7: 12.017, file_cluster_0: 12.041
- **Magnitude:** 3388.82 | **LOC:** 4192 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (25.0071%), Tech Debt (90.4348%)
**Top Internal Functions/Classes:**
  * `distinguishOperators` (Impact: 323.7 | O(2^N))
  * `changesSySubrc` (Impact: 224.8 | O(N^1))
  * `canAddToDdl` (Impact: 122.5 | O(N^1))
  * `finishBuild` (Impact: 103.4 | O(N^1) | DB: 1)
    * *Intent:* // the "}" that ends the select list is a distinct Command
  * `handleChainElement` (Impact: 99.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 925`, `structural_boundaries: 629`, `args: 299`, `func_start: 385`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 444`, `state_mutation: 103`, `dead_code: 26`, `planned_debt: 6`, `duplicate_logic: 34`
* *Architecture:* `api: 305`, `import: 2`
* *Defense:* `safety: 24`, `doc: 88`, `test: 2`, `sync_locks: 3`, `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.155
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.209187
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.programbase.*, com.sap.adt.abapcleaner.base.ABAP.SyField, java.util.*
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.814 IQR)
- **Top Global Matches:** file_cluster_8: 12.814, file_cluster_13: 12.825, file_cluster_0: 12.837
- **Magnitude:** 2257.36 | **LOC:** 1972 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 147
- **Risk Profile:** Cognitive Load (76.0761%), Tech Debt (8.9737%)
**Top Internal Functions/Classes:**
  * `createContents` (Impact: 259.1 | O(N^3) | DB: 147)
  * `open` (Impact: 131.1 | O(2^N) | DB: 12)
    * *Intent:* /**
  * `setProfile` (Impact: 121.0 | O(N^3) | DB: 23)
  * `chkRulesItemCheck` (Impact: 110.0 | O(N^5) | DB: 4)
  * `createConfigControls` (Impact: 92.5 | O(N^3) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 367`, `args: 92`, `func_start: 155`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 605`, `dead_code: 3`, `planned_debt: 2`, `orphaned_logic: 1`
* *Architecture:* `api: 46`, `import: 36`
* *Defense:* `safety: 27`, `doc: 4`, `test: 2`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.base.*, org.eclipse.swt.events.KeyEvent, org.eclipse.swt.widgets.Display, org.eclipse.swt.widgets.Button, org.eclipse.swt.widgets.Control, org.eclipse.swt.widgets.DirectoryDialog, org.eclipse.swt.graphics.FontData, org.eclipse.swt.layout.GridLayout...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.014 IQR)
- **Top Global Matches:** file_cluster_8: 12.014, file_cluster_0: 12.101, file_cluster_13: 12.619
- **Magnitude:** 1237.58 | **LOC:** 2336 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (19.0254%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAccessTypeInternalTables` (Impact: 91.9 | O(N^1))
  * `testAccessTypeStringProcessing` (Impact: 58.1 | O(N^1))
  * `assertAccessType` (Impact: 49.8 | O(N^1) | DB: 4)
    * *Intent:* /**
  * `testAccessTypeTableExpression` (Impact: 29.9 | O(N^1))
  * `testAddNextErr` (Impact: 28.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 225`, `args: 183`, `func_start: 1049`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 34`, `dead_code: 2`, `duplicate_logic: 8`, `orphaned_logic: 145`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 122`, `doc: 2`, `test: 916`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException, java.security.InvalidParameterException, com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.comparer.TextBit...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.56 IQR)
- **Top Global Matches:** file_cluster_8: 11.56, file_cluster_0: 11.75, file_cluster_11: 11.878
- **Magnitude:** 1196.94 | **LOC:** 805 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (40.9941%), Tech Debt (8.1995%)
**Top Internal Functions/Classes:**
  * `negate` (Impact: 199.8 | O(2^N) | DB: 6)
  * `calculateComplexity` (Impact: 185.7 | O(2^N))
  * `toTreeAlign` (Impact: 163.3 | O(2^N) | DB: 15)
    * *Intent:* // adjust the first token, including for parent expressions, esp. for cases where the first token is...
  * `LogicalExpression` (Impact: 133.8 | O(2^N) | DB: 2)
  * `removeFirstNeedlessParentheses` (Impact: 115.4 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 89`, `args: 31`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 76`, `dead_code: 7`, `planned_debt: 1`
* *Architecture:* `api: 24`
* *Defense:* `safety: 6`, `doc: 9`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.137076
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.base.*, java.util.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.19 IQR)
- **Top Global Matches:** file_cluster_8: 11.19, file_cluster_11: 11.208, file_cluster_13: 11.222
- **Magnitude:** 967.56 | **LOC:** 1252 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (64.6557%), Tech Debt (62.5152%)
**Top Internal Functions/Classes:**
  * `getWordFrequencies` (Impact: 268.0 | O(N^3) | DB: 3)
  * `initialize` (Impact: 135.5 | O(N^1))
  * `addCommentSamples` (Impact: 127.2 | O(N^3) | DB: 2)
  * `filterForMode` (Impact: 72.2 | O(N^4))
  * `getScopeDescription` (Impact: 39.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 109`, `args: 32`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 30`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 36`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`, `sync_locks: 3`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.573
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.084602
  * `Imports (Out-Degree: 1):` java.io.IOException, com.sap.adt.abapcleaner.base.*, java.io.InputStream, java.nio.charset.StandardCharsets, com.sap.adt.abapcleaner.programbase.Program, java.io.BufferedReader, java.util.*, java.io.InputStreamReader
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationNestingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.011 IQR)
- **Top Global Matches:** file_cluster_8: 11.011, file_cluster_0: 11.445, file_cluster_13: 11.595
- **Magnitude:** 909.54 | **LOC:** 633 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (49.846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAlwaysPutEmptyLines` (Impact: 67.5 | O(N^1) | DB: 1)
  * `testKeepEmptyLines` (Impact: 67.4 | O(N^1) | DB: 1)
  * `testSortByFirstLevelOnly` (Impact: 67.3 | O(N^1) | DB: 1)
  * `testPutEmptyLinesForNewFirstElemOnly` (Impact: 67.2 | O(N^1) | DB: 1)
  * `testNestingFromLevel2` (Impact: 56.9 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 34`, `args: 25`, `func_start: 436`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `orphaned_logic: 24`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationNestingDepth, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationSortOrder, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationEmptyLines
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 7.888 IQR)
- **Top Global Matches:** file_cluster_8: 7.888, file_cluster_7: 8.603, file_cluster_1: 8.929
- **Magnitude:** 826.24 | **LOC:** 534 | **CtrlFlow:** 82.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (24.1309%), Tech Debt (63.0411%)
**Top Internal Functions/Classes:**
  * `create` (Impact: 696.2 | O(2^N) | DB: 9)
  * `getHelp` (Impact: 62.6 | O(N^1) | DB: 9)
  * `getOptionsLinePrefix` (Impact: 7.7 | O(N^1))
  * `CommandLineArgs` (Impact: 5.2 | O(N^1))
  * `CommandLineArgs` (Impact: 4.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 27`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 1`, `duplicate_logic: 3`, `orphaned_logic: 5`
* *Architecture:* `io: 6`, `api: 25`, `import: 3`
* *Defense:* `doc: 1`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.abapcleaner.parser.CleanupRange, com.sap.adt.abapcleaner.base.StringUtil
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.86 IQR)
- **Top Global Matches:** file_cluster_8: 10.86, file_cluster_0: 11.299, file_cluster_7: 11.538
- **Magnitude:** 814.02 | **LOC:** 2569 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (9.9091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBoundStructuresWith2KeywordsUnused` (Impact: 36.6 | O(N^1))
  * `testNestedBoundStructuresUsedInComment` (Impact: 24.2 | O(N^1))
  * `testNestedBoundStructuresUnused` (Impact: 24.0 | O(N^1))
  * `testBoundStructuresUnused` (Impact: 22.8 | O(N^1))
  * `testRemoveObsoleteComments` (Impact: 17.5 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 120`, `args: 125`, `func_start: 1721`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `dead_code: 2`, `planned_debt: 112`, `duplicate_logic: 2`, `orphaned_logic: 111`
* *Architecture:* `import: 4`
* *Defense:* `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.rulebase.RuleID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/CompareDoc.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.612 IQR)
- **Top Global Matches:** file_cluster_8: 11.612, file_cluster_0: 11.812, file_cluster_11: 11.839
- **Magnitude:** 798.32 | **LOC:** 273 | **CtrlFlow:** 72.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (48.6811%), Tech Debt (46.7463%)
**Top Internal Functions/Classes:**
  * `compareTo` (Impact: 577.8 | O(2^N) | DB: 13)
  * `findSimilarLines` (Impact: 135.3 | O(N^5) | DB: 3)
  * `CompareDoc` (Impact: 12.3 | O(N^2) | DB: 1)
  * `CompareDoc` (Impact: 8.2 | O(N^2) | DB: 1)
  * `createFromDisplayLines` (Impact: 2.6 | O(N^1))
    * *Intent:* /** * <p>Represents a single text document which is split into {@link CompareLine}s * and can be com...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 26`, `args: 6`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 50`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `api: 6`
* *Defense:* `safety: 4`, `doc: 4`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.094727
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, java.util.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.91 IQR)
- **Top Global Matches:** file_cluster_8: 11.91, file_cluster_0: 12.062, file_cluster_7: 12.554
- **Magnitude:** 772.26 | **LOC:** 2133 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (9.2348%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testInsertStressTestToken` (Impact: 30.7 | O(N^1))
  * `testAppendCommentToLineOfErr` (Impact: 21.0 | O(N^1))
  * `testRemoveAllFurtherChainColons` (Impact: 20.1 | O(N^1))
  * `assertEqualsOps` (Impact: 19.1 | O(N^1) | DB: 2)
    * *Intent:* /** ensures that '=' operators are correctly distinguished: in the supplied code, expected assignmen...
  * `testPutCommentAboveLineOfErr` (Impact: 18.9 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 198`, `args: 157`, `func_start: 937`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 27`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 12`, `orphaned_logic: 117`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 120`, `doc: 1`, `test: 797`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.base.Language, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException, com.sap.adt.abapcleaner.base.ABAP, org.junit.jupiter.api.Assertions.*, com.sap.adt.abapcleaner.programbase.ParseException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Term.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.095 IQR)
- **Top Global Matches:** file_cluster_8: 11.095, file_cluster_0: 11.416, file_cluster_7: 11.461
- **Magnitude:** 689.82 | **LOC:** 480 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (57.7674%), Tech Debt (47.598%)
**Top Internal Functions/Classes:**
  * `Term` (Impact: 176.9 | O(2^N))
  * `removeFromCommand` (Impact: 85.3 | O(2^N) | DB: 8)
  * `isFirstTokenAllowed` (Impact: 30.1 | O(N^1))
  * `getMaxEndIndexInAnyLine` (Impact: 23.2 | O(N^1))
  * `getSumTextAndSpaceWidth` (Impact: 20.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 87`, `args: 48`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 56`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 56`
* *Defense:* `doc: 5`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090674
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.329 IQR)
- **Top Global Matches:** file_cluster_13: 11.329, file_cluster_8: 11.354, file_cluster_0: 11.609
- **Magnitude:** 670.16 | **LOC:** 678 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (34.747%), Tech Debt (62.5286%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 184.5 | O(2^N) | DB: 8)
  * `writeTo` (Impact: 66.8 | O(N^1) | DB: 2)
  * `checkNestingFor` (Impact: 50.8 | O(N^1) | DB: 4)
  * `determineTablesInArrays` (Impact: 37.2 | O(N^1) | DB: 2)
  * `adjustNesting` (Impact: 36.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 80`, `args: 26`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 52`, `dead_code: 6`, `duplicate_logic: 6`
* *Architecture:* `api: 25`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.504
  * `Choke Point (Betweenness):` 0.001759 | `Ripple Effect (Closeness):` 0.085982
  * `Imports (Out-Degree: 10):` com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CamelCaseNames.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.368 IQR)
- **Top Global Matches:** file_cluster_13: 11.368, file_cluster_8: 11.446, file_cluster_0: 11.576
- **Magnitude:** 658.0 | **LOC:** 875 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (29.6233%), Tech Debt (42.6996%)
**Top Internal Functions/Classes:**
  * `createFromTextFiles` (Impact: 106.0 | O(N^1) | DB: 3)
  * `createFromTextFile` (Impact: 88.5 | O(N^1) | DB: 3)
  * `preprocessFromGTNC` (Impact: 78.9 | O(N^1) | DB: 2)
  * `checkDiscardReasons` (Impact: 49.7 | O(N^1))
  * `applyCamelCaseTo` (Impact: 37.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 119`, `args: 36`, `func_start: 45`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 30`, `dead_code: 11`, `duplicate_logic: 6`
* *Architecture:* `io: 2`, `api: 36`, `import: 18`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 0.000286 | `Ripple Effect (Closeness):` 0.090874
  * `Imports (Out-Degree: 6):` java.io.IOException, java.util.HashMap, com.sap.adt.abapcleaner.programbase.Persistency, java.io.OutputStreamWriter, com.sap.adt.abapcleaner.base.Cult, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.rulebase.Profile, java.io.InputStream...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.575 IQR)
- **Top Global Matches:** file_cluster_8: 9.575, file_cluster_7: 10.069, file_cluster_13: 10.191
- **Magnitude:** 637.26 | **LOC:** 831 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (25.0313%), Tech Debt (99.9279%)
**Top Internal Functions/Classes:**
  * `split` (Impact: 51.4 | O(N^1) | DB: 4)
  * `findWholeWord` (Impact: 41.9 | O(N^1))
  * `split` (Impact: 41.8 | O(N^1) | DB: 2)
  * `split` (Impact: 41.8 | O(N^1) | DB: 2)
  * `indexOfAny` (Impact: 37.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 105`, `args: 53`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 24`, `dead_code: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 55`, `import: 2`
* *Defense:* `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.227514
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.489 IQR)
- **Top Global Matches:** file_cluster_8: 9.489, file_cluster_13: 9.678, file_cluster_0: 10.012
- **Magnitude:** 601.84 | **LOC:** 310 | **CtrlFlow:** 81.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (56.3447%), Tech Debt (63.0203%)
**Top Internal Functions/Classes:**
  * `refine` (Impact: 494.2 | O(N^3))
  * `getRndParseResult` (Impact: 59.6 | O(N^1) | DB: 2)
  * `refine` (Impact: 23.1 | O(2^N) | DB: 1)
  * `create` (Impact: 2.4 | O(N^1))
  * `createParseException` (Impact: 2.1 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 167`, `structural_boundaries: 37`, `args: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.531
  * `Choke Point (Betweenness):` 0.000957 | `Ripple Effect (Closeness):` 0.115781
  * `Imports (Out-Degree: 4):` com.sap.rnd.rndrt.Category, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.base.ABAP, com.sap.adt.tools.abapsource.parser.ABAPRndParser, com.sap.adt.abapcleaner.programbase.ParseException, com.sap.adt.abapcleaner.base.PadResourceResolver, java.util.List, java.util.ArrayList...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.074 IQR)
- **Top Global Matches:** file_cluster_8: 10.074, file_cluster_0: 10.147, file_cluster_13: 10.251
- **Magnitude:** 594.46 | **LOC:** 717 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (20.3819%), Tech Debt (81.1726%)
**Top Internal Functions/Classes:**
  * `getSourceField` (Impact: 103.7 | O(2^N) | DB: 9)
  * `getResult` (Impact: 80.0 | O(N^2) | DB: 1)
    * *Intent:* // if the view of this data source is not known, the data source can still be used as the "final dat...
  * `addField` (Impact: 73.0 | O(N^1) | DB: 2)
  * `analyzeAnnotations` (Impact: 62.1 | O(N^2) | DB: 2)
    * *Intent:* /**
  * `analyzeFieldDataSources` (Impact: 46.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 74`, `args: 23`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 87`, `state_mutation: 33`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 4`, `orphaned_logic: 4`
* *Architecture:* `io: 15`, `api: 9`, `import: 9`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.parser.Token, java.util.HashMap, com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.parser.Command, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Code, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.363 IQR)
- **Top Global Matches:** file_cluster_13: 11.363, file_cluster_8: 11.541, file_cluster_0: 11.596
- **Magnitude:** 587.68 | **LOC:** 1455 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (40.358%), Tech Debt (99.754%)
**Top Internal Functions/Classes:**
  * `generateUnitTest` (Impact: 69.5 | O(N^1) | DB: 3)
  * `paintCode` (Impact: 58.5 | O(N^1) | DB: 6)
  * `paintCode` (Impact: 33.8 | O(2^N) | DB: 3)
  * `CodeDisplay` (Impact: 26.1 | O(N^1) | DB: 17)
  * `refreshCode` (Impact: 22.1 | O(2^N) | DB: 2)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 171`, `args: 69`, `func_start: 111`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 101`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 4`, `orphaned_logic: 28`
* *Architecture:* `api: 59`, `concurrency: 2`, `import: 34`
* *Defense:* `safety: 8`, `doc: 9`, `test: 1`, `immutability_locks: 52`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.eclipse.swt.events.MouseMoveListener, org.eclipse.swt.events.PaintEvent, com.sap.adt.abapcleaner.base.*, org.eclipse.swt.events.KeyEvent, org.eclipse.swt.widgets.Display, org.eclipse.swt.graphics.Image, org.eclipse.swt.events.DisposeListener, org.eclipse.swt.graphics.FontData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffDoc.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.414 IQR)
- **Top Global Matches:** file_cluster_8: 10.414, file_cluster_0: 10.739, file_cluster_7: 10.862
- **Magnitude:** 565.14 | **LOC:** 362 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (22.7235%), Tech Debt (30.0615%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 73.0 | O(2^N) | DB: 4)
  * `getLineOfNextChangedCommand` (Impact: 66.4 | O(N^4))
  * `toText` (Impact: 59.0 | O(N^3))
  * `replacePart` (Impact: 30.4 | O(N^3) | DB: 3)
  * `getRuleStatsOfLineRange` (Impact: 29.2 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 62`, `args: 35`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 20`, `dead_code: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 23`
* *Defense:* `doc: 3`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.551
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.094727
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.base.*, java.util.*, com.sap.adt.abapcleaner.rulebase.*
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.015 IQR)
- **Top Global Matches:** file_cluster_8: 12.015, file_cluster_0: 12.02, file_cluster_11: 12.143
- **Magnitude:** 536.7 | **LOC:** 400 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (44.2347%), Tech Debt (30.8939%)
**Top Internal Functions/Classes:**
  * `align` (Impact: 262.9 | O(N^2) | DB: 6)
  * `overrideWidthIfColumnIsFollowedByLineBre` (Impact: 30.7 | O(N^1) | DB: 1)
  * `getFirstToken` (Impact: 13.5 | O(2^N))
  * `getFirstTokenColumnIndex` (Impact: 13.5 | O(2^N))
  * `getParentCode` (Impact: 13.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 40`, `args: 27`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 29`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 42`
* *Defense:* `doc: 8`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.634
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.086731
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, java.util.*
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignSourceParametersTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.456 IQR)
- **Top Global Matches:** file_cluster_8: 10.456, file_cluster_7: 11.136, file_cluster_0: 11.179
- **Magnitude:** 534.76 | **LOC:** 1030 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (17.4756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testParamsContinueAfterOpeningParens` (Impact: 57.5 | O(N^1))
  * `testAsAliasMissingAssociationNextLine` (Impact: 21.5 | O(N^1))
  * `testCommentsAboveParentheses` (Impact: 17.5 | O(N^1) | DB: 1)
  * `testCommentsAboveParenthesesParamsBelowS` (Impact: 17.5 | O(N^1) | DB: 1)
  * `testDoNotAlignNoSpaceAroundColon` (Impact: 17.4 | O(N^1) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 37`, `args: 28`, `func_start: 803`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `orphaned_logic: 27`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulehelpers.ChangeType, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlSpacesAroundBracketsRule, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlSpacesAroundSignsRule
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.843 IQR)
- **Top Global Matches:** file_cluster_13: 10.843, file_cluster_8: 11.051, file_cluster_16: 11.28
- **Magnitude:** 527.32 | **LOC:** 676 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.6014%), Tech Debt (99.766%)
**Top Internal Functions/Classes:**
  * `toDocumentation` (Impact: 53.1 | O(N^1))
  * `getAllRules` (Impact: 34.1 | O(N^2))
  * `unchain` (Impact: 23.5 | O(N^1) | DB: 2)
  * `hasSameConfigurationAs` (Impact: 21.1 | O(N^1))
  * `setDefault` (Impact: 16.4 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 237`, `args: 177`, `func_start: 73`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 46`, `dead_code: 2`, `duplicate_logic: 18`
* *Architecture:* `api: 85`, `import: 28`
* *Defense:* `safety: 2`, `doc: 14`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.3
  * `Choke Point (Betweenness):` 0.063718 | `Ripple Effect (Closeness):` 0.150425
  * `Imports (Out-Degree: 26):` com.sap.adt.abapcleaner.rules.ddl.position.DdlPositionBracesRule, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.rules.commands.*, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlSpacesAroundBracketsRule, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlCamelCaseNameRule, com.sap.adt.abapcleaner.rules.ddl.alignment.DdlAlignLogicalExpressionsRule, com.sap.adt.abapcleaner.rules.ddl.annotations.DdlAnnotationNestingRule, com.sap.adt.abapcleaner.rules.ddl.alignment.DdlAlignSourceParametersRule...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationLayoutTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.972 IQR)
- **Top Global Matches:** file_cluster_8: 10.972, file_cluster_0: 11.413, file_cluster_13: 11.58
- **Magnitude:** 516.16 | **LOC:** 448 | **CtrlFlow:** 91.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (56.0184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMaxOneElementPerLineInMain` (Impact: 63.6 | O(N^1) | DB: 1)
  * `testMaxOneElementPerLineInSelectList` (Impact: 63.6 | O(N^1) | DB: 1)
  * `testAlignValues` (Impact: 48.5 | O(N^1) | DB: 2)
  * `testAllSpaces` (Impact: 44.7 | O(N^1))
  * `testNoSpaceinsideBraces` (Impact: 37.8 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 23`, `args: 17`, `func_start: 314`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 49`, `orphaned_logic: 16`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.rulebase.RuleID
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.313 IQR)
- **Top Global Matches:** file_cluster_0: 10.313, file_cluster_8: 10.521, file_cluster_13: 10.867
- **Magnitude:** 504.12 | **LOC:** 677 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (32.6674%), Tech Debt (70.5626%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 425.3 | O(2^N) | DB: 5)
  * `getExample` (Impact: 8.7 | O(N^1))
  * `getNumberOfPasses` (Impact: 6.2 | O(N^1))
  * `AlignMethodsDeclarationRule` (Impact: 2.2 | O(N^1))
  * `isMatchForFurtherCommand` (Impact: 2.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 58`, `args: 22`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 15`, `dead_code: 4`, `orphaned_logic: 11`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.rulehelpers.*, com.sap.adt.abapcleaner.programbase.*, java.time.LocalDate, com.sap.adt.abapcleaner.rulebase.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.627 IQR)
- **Top Global Matches:** file_cluster_8: 10.627, file_cluster_0: 10.64, file_cluster_13: 11.038
- **Magnitude:** 498.84 | **LOC:** 970 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (31.3471%), Tech Debt (67.0282%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 62.7 | O(N^1) | DB: 3)
  * `readStructureDeclaration` (Impact: 60.4 | O(N^1) | DB: 3)
  * `buildTable` (Impact: 45.5 | O(N^1))
  * `getExample` (Impact: 26.0 | O(N^1))
  * `keepEnumOneLiners` (Impact: 23.6 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 99`, `args: 40`, `func_start: 50`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 33`, `dead_code: 6`, `duplicate_logic: 2`, `orphaned_logic: 14`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.rulehelpers.*, com.sap.adt.abapcleaner.programbase.*, java.time.LocalDate, com.sap.adt.abapcleaner.rulebase.*, java.util.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffNavigator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.827 IQR)
- **Top Global Matches:** file_cluster_8: 10.827, file_cluster_0: 11.118, file_cluster_7: 11.155
- **Magnitude:** 498.36 | **LOC:** 597 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.5423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 99.4 | O(N^1))
  * `isLineBitHighlighted` (Impact: 30.1 | O(N^1))
  * `reprocessSelection` (Impact: 24.8 | O(N^1))
  * `getLine` (Impact: 14.8 | O(2^N))
  * `getLineCount` (Impact: 13.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 77`, `args: 52`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 11`, `dead_code: 5`
* *Architecture:* `api: 91`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.092443
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/EmptySectionsInClassDefRule.java` (JAVA) | Magnitude: 133.02 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 149, structural_boundaries: 57, branch: 36, func_start: 16
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigLabel.java` (JAVA) | Magnitude: 53.42 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, state_mutation: 19, branch: 7
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DisplayLine.java` (JAVA) | Magnitude: 88.04 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 44, api: 24, structural_boundaries: 23, args: 15
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` (JAVA) | Magnitude: 194.08 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 156, structural_boundaries: 34, branch: 31, api: 29
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ReceivingKeywordRule.java` (JAVA) | Magnitude: 98.38 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 29, api: 21, args: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` (JAVA) | Magnitude: 485.28 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 318, branch: 79, structural_boundaries: 78, api: 60
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/NeedlessClearRule.java` (JAVA) | Magnitude: 176.3 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 182, branch: 62, structural_boundaries: 59, import: 21
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/FinalVariableRule.java` (JAVA) | Magnitude: 114.78 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 92, structural_boundaries: 37, branch: 31, args: 17
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignClearFreeAndSortRule.java` (JAVA) | Magnitude: 184.14 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 198, branch: 63, structural_boundaries: 57, state_mutation: 21
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/emptylines/DdlEmptyLinesBetweenSectionsRule.java` (JAVA) | Magnitude: 126.84 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 162, structural_boundaries: 47, branch: 46, func_start: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Config.java` (JAVA) | Magnitude: 74.94 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 66, state_mutation: 28, structural_boundaries: 17, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/ITokenTypeRefiner.java` (JAVA) | Magnitude: 17.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, args: 1, func_start: 1, class_start: 1
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA) | Magnitude: 536.7 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 285, branch: 114, api: 42, structural_boundaries: 40
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/prettyprinter/UpperAndLowerCaseRule.java` (JAVA) | Magnitude: 239.32 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 247, branch: 84, structural_boundaries: 47, args: 22
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA) | Magnitude: 2257.36 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 864, state_mutation: 605, indent_spaces: 430, branch: 383
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA) | Magnitude: 498.84 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 490, branch: 171, structural_boundaries: 99, func_start: 50

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/SystemInfo.java` (JAVA) | Magnitude: 30.5 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 22, branch: 9, structural_boundaries: 4, api: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> Churn: **68.33%** | Cog Load: 25.0071% | Debt: 90.4348%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3388.82
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 2257.36
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1237.58
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1196.94
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 826.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 2.639** (Bridge: 0.0637 * Flux: 41.4166%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` -> **Severity: 0.65** (Bridge: 0.0161 * Flux: 40.269%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/Variables.java` -> **Severity: 0.39** (Bridge: 0.0039 * Flux: 99.8374%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/spaces/DdlCamelCaseNameRule.java` -> **Severity: 0.302** (Bridge: 0.0042 * Flux: 72.7575%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignFieldListsRule.java` -> **Severity: 0.281** (Bridge: 0.0029 * Flux: 97.9658%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 20.041** (Embedded: 0.2275 * Error Risk: 88.088%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Severity: 19.857** (Embedded: 0.2092 * Error Risk: 94.9266%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Token.java` -> **Severity: 19.685** (Embedded: 0.2029 * Error Risk: 97.0321%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` -> **Severity: 16.76** (Embedded: 0.1955 * Error Risk: 85.7353%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/IntegrityBrokenException.java` -> **Severity: 13.943** (Embedded: 0.1689 * Error Risk: 82.5338%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -> **Severity: 2918.222** (Blast Radius: 59.661 * Doc Risk: 48.9134%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 2406.3** (Blast Radius: 24.063 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxAfterChanges.java` -> **Severity: 1931.271** (Blast Radius: 19.322 * Doc Risk: 99.9519%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 1130.0** (Blast Radius: 11.3 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Severity: 1015.5** (Blast Radius: 10.155 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
