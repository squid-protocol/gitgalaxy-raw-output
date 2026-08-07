# ARCHITECTURAL_BRIEF: abap-cleaner
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/abap-cleaner` |
| **Timestamp** | `2026-08-07T03:46:24.059415+00:00` |
| **Scan Duration** | `2.59s` |
| **Git Branch** | `main` |
| **Git Commit** | `952c68076fb0c5a258d947ca269e876d12603190` |
| **Git Remote** | `https://github.com/SAP/abap-cleaner` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 535 malicious artifacts.

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
> **Architectural Drift Z-Score:** `6.427`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 402 | 73.1% |
| file_cluster_13 | 99 | 18.0% |
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
| Cognitive Load Exposure | 0.0 | 96.9 | 14.8 | 9.2 | 5.0 |
| Error & Exception Exposure | 0.0 | 97.6 | 41.9 | 51.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 48.6 | 34.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.3 | 2.2 | 0.0 |
| API Exposure | 0.0 | 16.5 | 6.2 | 6.7 | 0.0 |
| Concurrency Exposure | 0.0 | 99.3 | 0.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 13.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 79.6 | 4.1 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.3 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 21.0 | 1.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 2.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 50.8 | 61.7 | 0.0 |
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

- `refine` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefinerRnd.java`) -> Impact: **250.2** | LOC: 125
- `refine` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/TokenTypeRefiner.java`) -> Impact: **248.2** | LOC: 260
  * *Intent:* /** * <p>Implementation of the {@link ITokenTypeRefiner} interface which uses ABAP cleaner-internal means of * refining the {@link TokenType}s that we...
- `changesSySubrc` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java`) -> Impact: **224.8** | LOC: 336
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java`) -> Impact: **219.6** | LOC: 277
- `align` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java`) -> Impact: **178.4** | LOC: 188
- `executeOn` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ValueStatementRule.java`) -> Impact: **154.5** | LOC: 183
- `create` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/CommandLineArgs.java`) -> Impact: **150.4** | LOC: 208
- `createContents` (@ `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java`) -> Impact: **145.1** | LOC: 621
- `initialize` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java`) -> Impact: **135.5** | LOC: 27
- `canAddToDdl` (@ `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java`) -> Impact: **122.5** | LOC: 163

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers` | 56 | 7910.34 | 18.68% | 50.05% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser` | 32 | 6129.8 | 17.91% | 46.19% |
| `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui` | 31 | 4951.68 | 30.99% | 77.11% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment` | 45 | 4025.3 | 16.76% | 92.41% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser` | 11 | 3064.62 | 12.34% | 0.0% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations` | 13 | 3019.26 | 10.76% | 0.0% |
| `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment` | 17 | 2930.5 | 6.03% | 0.0% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase` | 28 | 2590.7 | 14.04% | 66.96% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base` | 22 | 2590.23 | 9.37% | 48.54% |
| `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations` | 26 | 2398.06 | 14.99% | 97.43% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundJob.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/BackgroundTask.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/DummySearchControls.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmImportTestCode.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProgress.java` -> **100.0%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigLabel.java` -> **99.9996%** Exposure
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **99.9993%** Exposure
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Config.java` -> **99.9969%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` -> **145** Orphaned Functions | **61** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` -> **117** Orphaned Functions | **76** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` -> **123** Orphaned Functions | **2** Duplicates
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` -> **111** Orphaned Functions | **2** Duplicates
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **3** Orphaned Functions | **83** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `3072` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfileDirs.java` (JAVA) -> Cumulative Risk: **677.75**
- **Archetype:** `file_cluster_13` (Distance: 11.044 IQR)
- **Magnitude:** 301.0 | **LOC:** 426 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9982%), State Flux (99.9748%), Safety Score (87.0623%)
- **Heaviest Functions:** `selectOwnDir` (Impact: 79.2), `createContents` (Impact: 20.4), `updateSettings` (Impact: 17.9)

### 2. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/Variables.java` (JAVA) -> Cumulative Risk: **671.21**
- **Archetype:** `file_cluster_13` (Distance: 12.613 IQR)
- **Magnitude:** 210.12 | **LOC:** 224 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9583%), State Flux (99.8374%), Tech Debt (97.6135%)
- **Heaviest Functions:** `addDeclaration` (Impact: 25.2), `Variables` (Impact: 15.1), `addUsage` (Impact: 12.4)

### 3. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA) -> Cumulative Risk: **652.08**
- **Archetype:** `file_cluster_13` (Distance: 12.767 IQR)
- **Magnitude:** 1987.76 | **LOC:** 1972 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9993%), Cognitive Load (96.9194%)
- **Heaviest Functions:** `createContents` (Impact: 145.1), `importProfiles` (Impact: 92.2), `exportProfiles` (Impact: 67.2)

### 4. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProgress.java` (JAVA) -> Cumulative Risk: **650.43**
- **Archetype:** `file_cluster_13` (Distance: 11.385 IQR)
- **Magnitude:** 132.58 | **LOC:** 161 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9982%), Safety Score (93.1323%)
- **Heaviest Functions:** `open` (Impact: 16.0), `createContents` (Impact: 14.5), `run` (Impact: 8.6)

### 5. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ValueStatementRule.java` (JAVA) -> Cumulative Risk: **616.65**
- **Archetype:** `file_cluster_0` (Distance: 12.251 IQR)
- **Magnitude:** 289.08 | **LOC:** 374 | **CtrlFlow:** 59.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (92.3999%), Tech Debt (87.2336%), Safety Score (82.1811%)
- **Heaviest Functions:** `executeOn` (Impact: 154.5), `createTableFromAssignmentSequence` (Impact: 19.7), `setWhitespaceAfter` (Impact: 16.7)

### 6. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigIntBox.java` (JAVA) -> Cumulative Risk: **614.64**
- **Archetype:** `file_cluster_13` (Distance: 10.588 IQR)
- **Magnitude:** 167.4 | **LOC:** 162 | **CtrlFlow:** 47.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.922%), State Flux (98.5524%), Safety Score (85.1379%)
- **Heaviest Functions:** `txtValueKeyPressed` (Impact: 80.8), `detachControls` (Impact: 9.7), `ConfigIntBox` (Impact: 6.2)

### 7. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Log.java` (JAVA) -> Cumulative Risk: **597.47**
- **Archetype:** `file_cluster_8` (Distance: 9.723 IQR)
- **Magnitude:** 112.92 | **LOC:** 98 | **CtrlFlow:** 66.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (91.97%), State Flux (90.8159%), Cognitive Load (82.202%)
- **Heaviest Functions:** `getSummary` (Impact: 68.8), `add` (Impact: 7.8), `flush` (Impact: 6.4)

### 8. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignCondExpressionsRule.java` (JAVA) -> Cumulative Risk: **587.43**
- **Archetype:** `file_cluster_13` (Distance: 11.232 IQR)
- **Magnitude:** 230.72 | **LOC:** 374 | **CtrlFlow:** 40.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5403%), Tech Debt (88.8466%), Safety Score (83.976%)
- **Heaviest Functions:** `executeOn` (Impact: 86.9), `executeOn` (Impact: 13.1), `readTermUntil` (Impact: 10.9)

### 9. `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/eclipse/AbapCleanerHandlerBase.java` (JAVA) -> Cumulative Risk: **587.28**
- **Archetype:** `file_cluster_13` (Distance: 11.61 IQR)
- **Magnitude:** 141.06 | **LOC:** 257 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.2776%), Safety Score (87.4882%), State Flux (86.5564%)
- **Heaviest Functions:** `execute` (Impact: 30.0), `getAbapReleaseOfProject` (Impact: 20.1), `replaceTextInDocument` (Impact: 11.5)

### 10. `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/RuleForDdlPosition.java` (JAVA) -> Cumulative Risk: **585.9**
- **Archetype:** `file_cluster_13` (Distance: 10.423 IQR)
- **Magnitude:** 143.6 | **LOC:** 145 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.2895%), State Flux (87.5209%), Tech Debt (86.3872%)
- **Heaviest Functions:** `breakBefore` (Impact: 35.1), `getLineBreak` (Impact: 18.4), `setNewIndent` (Impact: 13.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.715 IQR)
- **Top Global Matches:** file_cluster_8: 11.715, file_cluster_7: 11.976, file_cluster_0: 11.993
- **Magnitude:** 3246.42 | **LOC:** 4192 | **CtrlFlow:** 59.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (24.7948%), Tech Debt (99.7581%)
**Top Internal Functions/Classes:**
  * `changesSySubrc` (Impact: 224.8)
  * `canAddToDdl` (Impact: 122.5)
  * `distinguishOperators` (Impact: 112.0)
  * `finishBuild` (Impact: 103.4)
    * *Intent:* // the "}" that ends the select list is a distinct Command
  * `handleChainElement` (Impact: 99.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 925`, `structural_boundaries: 629`, `args: 261`, `func_start: 363`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 444`, `state_mutation: 103`, `dead_code: 26`, `planned_debt: 6`, `duplicate_logic: 62`
* *Architecture:* `api: 316`, `import: 2`
* *Defense:* `safety: 24`, `doc: 88`, `test: 2`, `sync_locks: 3`, `immutability_locks: 199`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.155
  * `Choke Point (Betweenness):` 8.6e-05 | `Ripple Effect (Closeness):` 0.209187
  * `Imports (Out-Degree: 1):` java.util.*, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.base.ABAP.SyField, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 77):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.767 IQR)
- **Top Global Matches:** file_cluster_13: 12.767, file_cluster_0: 12.774, file_cluster_8: 12.775
- **Magnitude:** 1987.76 | **LOC:** 1972 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (96.9194%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `createContents` (Impact: 145.1)
  * `importProfiles` (Impact: 92.2)
  * `exportProfiles` (Impact: 67.2)
  * `setProfile` (Impact: 62.8)
  * `setControlsHighlight` (Impact: 48.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 383`, `structural_boundaries: 367`, `args: 83`, `func_start: 135`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 599`, `dead_code: 3`, `planned_debt: 2`, `duplicate_logic: 83`, `orphaned_logic: 3`
* *Architecture:* `api: 46`, `import: 36`
* *Defense:* `safety: 27`, `doc: 4`, `test: 2`, `immutability_locks: 29`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.eclipse.swt.widgets.DirectoryDialog, org.eclipse.swt.widgets.Composite, org.eclipse.swt.events.ShellAdapter, org.eclipse.swt.layout.FillLayout, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*, org.eclipse.swt.widgets.TableItem, org.eclipse.swt.layout.GridData...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.793 IQR)
- **Top Global Matches:** file_cluster_8: 11.793, file_cluster_0: 11.868, file_cluster_13: 12.4
- **Magnitude:** 1517.28 | **LOC:** 2336 | **CtrlFlow:** 65.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.7309%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAccessTypeInternalTables` (Impact: 105.8)
  * `testAccessTypeStringProcessing` (Impact: 67.0)
  * `assertAccessType` (Impact: 49.8)
    * *Intent:* /**
  * `testAccessTypeTableExpression` (Impact: 34.5)
  * `testGetLastTokenOfDdlLogicalExpression` (Impact: 33.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 225`, `args: 182`, `func_start: 499`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 34`, `dead_code: 2`, `duplicate_logic: 61`, `orphaned_logic: 145`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 122`, `doc: 2`, `test: 916`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` java.security.InvalidParameterException, com.sap.adt.abapcleaner.programbase.ParseException, java.util.ArrayList, com.sap.adt.abapcleaner.comparer.TextBit, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationNestingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.039 IQR)
- **Top Global Matches:** file_cluster_8: 11.039, file_cluster_0: 11.47, file_cluster_13: 11.62
- **Magnitude:** 1036.84 | **LOC:** 633 | **CtrlFlow:** 92.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.846%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testAlwaysPutEmptyLines` (Impact: 77.7)
  * `testKeepEmptyLines` (Impact: 77.7)
  * `testSortByFirstLevelOnly` (Impact: 77.5)
  * `testPutEmptyLinesForNewFirstElemOnly` (Impact: 77.5)
  * `testNestingFromLevel2` (Impact: 65.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 446`, `structural_boundaries: 34`, `args: 25`, `func_start: 433`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 54`, `orphaned_logic: 24`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 24`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationNestingDepth, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationEmptyLines, org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.DdlAnnotationSortOrder
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.697 IQR)
- **Top Global Matches:** file_cluster_8: 11.697, file_cluster_0: 11.837, file_cluster_13: 12.345
- **Magnitude:** 995.96 | **LOC:** 2133 | **CtrlFlow:** 51.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.2348%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testInsertStressTestToken` (Impact: 35.4)
  * `testAppendCommentToLineOfErr` (Impact: 23.9)
  * `testRemoveAllFurtherChainColons` (Impact: 23.1)
  * `testPutCommentAboveLineOfErr` (Impact: 21.6)
  * `assertEqualsOps` (Impact: 19.1)
    * *Intent:* /** ensures that '=' operators are correctly distinguished: in the supplied code, expected assignmen...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 207`, `structural_boundaries: 198`, `args: 157`, `func_start: 467`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 27`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 76`, `orphaned_logic: 117`
* *Architecture:* `api: 1`, `import: 11`
* *Defense:* `safety: 120`, `doc: 1`, `test: 797`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` com.sap.adt.abapcleaner.programbase.ParseException, java.util.ArrayList, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxAfterChanges, org.junit.jupiter.api.Test, java.util.List, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException, com.sap.adt.abapcleaner.base.ABAP.SyField...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.82 IQR)
- **Top Global Matches:** file_cluster_8: 10.82, file_cluster_0: 11.259, file_cluster_7: 11.5
- **Magnitude:** 913.02 | **LOC:** 2569 | **CtrlFlow:** 66.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.9091%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testBoundStructuresWith2KeywordsUnused` (Impact: 42.0)
  * `testNestedBoundStructuresUsedInComment` (Impact: 27.4)
  * `testNestedBoundStructuresUnused` (Impact: 27.2)
  * `testBoundStructuresUnused` (Impact: 26.1)
  * `testRemoveObsoleteComments` (Impact: 19.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 120`, `args: 125`, `func_start: 1436`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 54`, `dead_code: 2`, `planned_debt: 112`, `duplicate_logic: 2`, `orphaned_logic: 111`
* *Architecture:* `import: 4`
* *Defense:* `test: 113`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, com.sap.adt.abapcleaner.rulebase.RuleID, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/LogicalExpression.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.512 IQR)
- **Top Global Matches:** file_cluster_8: 11.512, file_cluster_0: 11.691, file_cluster_13: 11.822
- **Magnitude:** 788.24 | **LOC:** 805 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (40.9941%), Tech Debt (93.6687%)
**Top Internal Functions/Classes:**
  * `negate` (Impact: 102.8)
  * `calculateComplexity` (Impact: 95.0)
  * `toTreeAlign` (Impact: 82.8)
    * *Intent:* // adjust the first token, including for parent expressions, esp. for cases where the first token is...
  * `LogicalExpression` (Impact: 68.9)
  * `removeFirstNeedlessParentheses` (Impact: 59.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 256`, `structural_boundaries: 89`, `args: 28`, `func_start: 33`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 76`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 24`
* *Defense:* `safety: 6`, `doc: 9`, `immutability_locks: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.445
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.137076
  * `Imports (Out-Degree: 0):` java.util.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.17 IQR)
- **Top Global Matches:** file_cluster_8: 11.17, file_cluster_11: 11.186, file_cluster_13: 11.2
- **Magnitude:** 714.86 | **LOC:** 1252 | **CtrlFlow:** 71.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.3176%), Tech Debt (87.4956%)
**Top Internal Functions/Classes:**
  * `initialize` (Impact: 135.5)
  * `getWordFrequencies` (Impact: 120.6)
  * `addCommentSamples` (Impact: 65.2)
  * `getScopeDescription` (Impact: 39.9)
  * `correctText` (Impact: 38.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 269`, `structural_boundaries: 109`, `args: 29`, `func_start: 37`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 30`, `dead_code: 7`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 36`, `concurrency: 3`, `import: 6`
* *Defense:* `safety: 4`, `doc: 2`, `sync_locks: 3`, `immutability_locks: 24`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.573
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.084602
  * `Imports (Out-Degree: 1):` com.sap.adt.abapcleaner.programbase.Program, java.io.InputStreamReader, java.io.IOException, java.io.BufferedReader, java.io.InputStream, java.util.*, com.sap.adt.abapcleaner.base.*, java.nio.charset.StandardCharsets
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/CodeDisplay.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.359 IQR)
- **Top Global Matches:** file_cluster_13: 11.359, file_cluster_8: 11.555, file_cluster_0: 11.587
- **Magnitude:** 661.68 | **LOC:** 1455 | **CtrlFlow:** 39.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.1188%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `generateUnitTest` (Impact: 69.5)
  * `paintCode` (Impact: 58.5)
  * `CodeDisplay` (Impact: 26.1)
  * `refreshRuleStatsInfo` (Impact: 18.6)
  * `paintCode` (Impact: 17.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 171`, `args: 69`, `func_start: 109`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 101`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 42`, `orphaned_logic: 32`
* *Architecture:* `api: 59`, `concurrency: 2`, `import: 34`
* *Defense:* `safety: 8`, `doc: 9`, `test: 1`, `immutability_locks: 52`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.programbase.Program, org.eclipse.swt.events.ControlAdapter, org.eclipse.swt.graphics.GC, org.eclipse.swt.graphics.Image, org.eclipse.swt.widgets.Composite, org.eclipse.swt.events.DisposeEvent, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, com.sap.adt.abapcleaner.base.*...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CamelCaseNames.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.289 IQR)
- **Top Global Matches:** file_cluster_13: 11.289, file_cluster_8: 11.364, file_cluster_0: 11.497
- **Magnitude:** 655.8 | **LOC:** 875 | **CtrlFlow:** 61.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (28.8255%), Tech Debt (90.7158%)
**Top Internal Functions/Classes:**
  * `createFromTextFiles` (Impact: 106.0)
  * `createFromTextFile` (Impact: 83.7)
  * `preprocessFromGTNC` (Impact: 78.9)
  * `checkDiscardReasons` (Impact: 49.7)
  * `applyCamelCaseTo` (Impact: 37.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 193`, `structural_boundaries: 119`, `args: 33`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 28`, `dead_code: 11`, `duplicate_logic: 13`
* *Architecture:* `io: 2`, `api: 36`, `import: 18`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.276
  * `Choke Point (Betweenness):` 0.000286 | `Ripple Effect (Closeness):` 0.090874
  * `Imports (Out-Degree: 6):` com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.programbase.Persistency, com.sap.adt.abapcleaner.rulebase.Profile, java.util.ArrayList, java.io.InputStreamReader, java.io.IOException, java.util.HashMap, java.io.BufferedReader...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.502 IQR)
- **Top Global Matches:** file_cluster_8: 9.502, file_cluster_7: 9.999, file_cluster_13: 10.122
- **Magnitude:** 618.96 | **LOC:** 831 | **CtrlFlow:** 65.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (25.0313%), Tech Debt (99.9279%)
**Top Internal Functions/Classes:**
  * `split` (Impact: 51.4)
  * `findWholeWord` (Impact: 41.9)
  * `split` (Impact: 41.8)
  * `split` (Impact: 41.8)
  * `indexOfAny` (Impact: 37.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 198`, `structural_boundaries: 105`, `args: 38`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 49`, `state_mutation: 24`, `dead_code: 1`, `duplicate_logic: 19`
* *Architecture:* `api: 55`, `import: 2`
* *Defense:* `doc: 8`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 24.063
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.227514
  * `Imports (Out-Degree: 0):` java.util.List, java.util.ArrayList
  * `Imported By (In-Degree: 60):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/alignment/DdlAlignSourceParametersTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.455 IQR)
- **Top Global Matches:** file_cluster_8: 10.455, file_cluster_7: 11.135, file_cluster_0: 11.177
- **Magnitude:** 602.06 | **LOC:** 1030 | **CtrlFlow:** 85.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4756%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testParamsContinueAfterOpeningParens` (Impact: 65.8)
  * `testAsAliasMissingAssociationNextLine` (Impact: 24.4)
  * `testCommentsAboveParentheses` (Impact: 20.0)
  * `testCommentsAboveParenthesesParamsBelowS` (Impact: 20.0)
  * `testDoNotAlignNoSpaceAroundColon` (Impact: 19.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 216`, `structural_boundaries: 37`, `args: 28`, `func_start: 742`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 45`, `orphaned_logic: 27`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `test: 27`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlSpacesAroundBracketsRule, org.junit.jupiter.api.Test, org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlSpacesAroundSignsRule, com.sap.adt.abapcleaner.rulehelpers.ChangeType
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/ddl/annotations/DdlAnnotationLayoutTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.992 IQR)
- **Top Global Matches:** file_cluster_8: 10.992, file_cluster_0: 11.431, file_cluster_13: 11.597
- **Magnitude:** 584.16 | **LOC:** 448 | **CtrlFlow:** 91.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (56.0184%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testMaxOneElementPerLineInMain` (Impact: 73.0)
  * `testMaxOneElementPerLineInSelectList` (Impact: 73.0)
  * `testAlignValues` (Impact: 55.8)
  * `testAllSpaces` (Impact: 51.4)
  * `testNoSpaceinsideBraces` (Impact: 43.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 236`, `structural_boundaries: 23`, `args: 17`, `func_start: 306`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 49`, `orphaned_logic: 16`
* *Architecture:* `api: 1`, `import: 4`
* *Defense:* `test: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, com.sap.adt.abapcleaner.rulebase.RuleID, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnnotationScope.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.304 IQR)
- **Top Global Matches:** file_cluster_13: 11.304, file_cluster_8: 11.331, file_cluster_0: 11.584
- **Magnitude:** 572.96 | **LOC:** 678 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.747%), Tech Debt (88.2682%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 95.1)
  * `writeTo` (Impact: 66.8)
  * `checkNestingFor` (Impact: 50.8)
  * `determineTablesInArrays` (Impact: 37.2)
  * `adjustNesting` (Impact: 36.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 80`, `args: 24`, `func_start: 30`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 52`, `dead_code: 6`, `duplicate_logic: 9`
* *Architecture:* `api: 25`, `import: 12`
* *Defense:* `safety: 2`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.504
  * `Choke Point (Betweenness):` 0.001759 | `Ripple Effect (Closeness):` 0.085982
  * `Imports (Out-Degree: 10):` com.sap.adt.abapcleaner.programbase.ParseException, java.util.ArrayList, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.rulebase.Rule, java.util.HashSet, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxException...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.616 IQR)
- **Top Global Matches:** file_cluster_8: 10.616, file_cluster_0: 10.62, file_cluster_13: 11.02
- **Magnitude:** 534.14 | **LOC:** 970 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.2266%), Tech Debt (95.2114%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 62.7)
  * `readStructureDeclaration` (Impact: 60.4)
  * `buildTable` (Impact: 45.5)
  * `getExample` (Impact: 28.6)
  * `keepEnumOneLiners` (Impact: 23.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 171`, `structural_boundaries: 99`, `args: 38`, `func_start: 49`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 33`, `dead_code: 6`, `duplicate_logic: 7`, `orphaned_logic: 15`
* *Architecture:* `api: 28`, `import: 1`
* *Defense:* `safety: 6`, `doc: 4`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.rulebase.*, java.time.LocalDate, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.rulehelpers.*, java.util.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignParametersTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.867 IQR)
- **Top Global Matches:** file_cluster_8: 9.867, file_cluster_0: 10.549, file_cluster_7: 10.672
- **Magnitude:** 524.34 | **LOC:** 3395 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.6977%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testValueConstructorInsideParamList` (Impact: 7.0)
  * `testMoveParamLeftOfAssignOp` (Impact: 7.0)
  * `testForceKeywordOnOwnLine` (Impact: 7.0)
  * `testAssignmentWithCastMoveLeftOfAssignOp` (Impact: 6.8)
  * `testAssignmentWithCast` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 133`, `args: 177`, `func_start: 1285`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 87`, `duplicate_logic: 2`, `orphaned_logic: 123`
* *Architecture:* `import: 5`
* *Defense:* `test: 130`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleID, org.junit.jupiter.api.Assertions.assertFalse
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Term.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.053 IQR)
- **Top Global Matches:** file_cluster_8: 11.053, file_cluster_0: 11.375, file_cluster_7: 11.42
- **Magnitude:** 514.12 | **LOC:** 480 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.7674%), Tech Debt (47.598%)
**Top Internal Functions/Classes:**
  * `Term` (Impact: 90.3)
  * `removeFromCommand` (Impact: 43.6)
  * `isFirstTokenAllowed` (Impact: 30.1)
  * `getMaxEndIndexInAnyLine` (Impact: 23.2)
  * `getSumTextAndSpaceWidth` (Impact: 20.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 139`, `structural_boundaries: 87`, `args: 46`, `func_start: 46`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 56`, `dead_code: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 56`
* *Defense:* `doc: 5`, `immutability_locks: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.396
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.090674
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 21):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rulebase/RuleTestBase.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.976 IQR)
- **Top Global Matches:** file_cluster_13: 10.976, file_cluster_8: 11.205, file_cluster_0: 11.381
- **Magnitude:** 490.18 | **LOC:** 748 | **CtrlFlow:** 61.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.9733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testRule` (Impact: 118.9)
  * `testDiffNavigator` (Impact: 88.4)
  * `testExampleCode` (Impact: 31.6)
    * *Intent:* // =========================================================================
  * `runStressTest` (Impact: 28.2)
  * `assertTrue` (Impact: 9.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 87`, `args: 29`, `func_start: 50`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 35`, `dead_code: 3`, `duplicate_logic: 14`
* *Architecture:* `api: 44`, `import: 40`
* *Defense:* `safety: 26`, `doc: 3`, `test: 77`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.866
  * `Choke Point (Betweenness):` 0.032884 | `Ripple Effect (Closeness):` 0.182149
  * `Imports (Out-Degree: 28):` com.sap.adt.abapcleaner.programbase.Program, com.sap.adt.abapcleaner.comparer.DiffLine, com.sap.adt.abapcleaner.parser.MemoryAccessType, org.junit.jupiter.api.BeforeEach, org.junit.jupiter.api.Assertions.assertEquals, com.sap.adt.abapcleaner.parser.StressTestParams, com.sap.adt.abapcleaner.programbase.IntegrityBrokenException, org.junit.jupiter.api.Assertions.assertFalse...
  * `Imported By (In-Degree: 100):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.551 IQR)
- **Top Global Matches:** file_cluster_13: 10.551, file_cluster_8: 10.765, file_cluster_16: 11.0
- **Magnitude:** 481.32 | **LOC:** 676 | **CtrlFlow:** 28.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6014%), Tech Debt (99.766%)
**Top Internal Functions/Classes:**
  * `toDocumentation` (Impact: 53.1)
  * `getAllRules` (Impact: 25.1)
  * `unchain` (Impact: 23.5)
  * `hasSameConfigurationAs` (Impact: 21.1)
  * `compare` (Impact: 16.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 237`, `args: 64`, `func_start: 70`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 46`, `dead_code: 2`, `duplicate_logic: 18`
* *Architecture:* `api: 85`, `import: 28`
* *Defense:* `safety: 2`, `doc: 14`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.3
  * `Choke Point (Betweenness):` 0.063718 | `Ripple Effect (Closeness):` 0.150425
  * `Imports (Out-Degree: 26):` com.sap.adt.abapcleaner.rules.ddl.alignment.DdlAlignFunctionParametersRule, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlTypoRule, com.sap.adt.abapcleaner.rules.ddl.position.DdlPositionJoinRule, com.sap.adt.abapcleaner.rules.ddl.annotations.DdlAnnotationNestingRule, com.sap.adt.abapcleaner.rules.syntax.*, com.sap.adt.abapcleaner.rules.commands.*, com.sap.adt.abapcleaner.rules.ddl.spaces.DdlCamelCaseNameRule, com.sap.adt.abapcleaner.base.*...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DiffNavigator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.822 IQR)
- **Top Global Matches:** file_cluster_8: 10.822, file_cluster_0: 11.113, file_cluster_7: 11.15
- **Magnitude:** 470.66 | **LOC:** 597 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.5423%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `search` (Impact: 99.4)
  * `isLineBitHighlighted` (Impact: 30.1)
  * `reprocessSelection` (Impact: 24.8)
  * `refreshCode` (Impact: 12.8)
  * `setBlockRuleInSelection` (Impact: 11.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 77`, `args: 51`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 31`, `state_mutation: 11`, `dead_code: 5`
* *Architecture:* `api: 91`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.437
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.092443
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.rulebase.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationRule.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 10.323 IQR)
- **Top Global Matches:** file_cluster_0: 10.323, file_cluster_8: 10.546, file_cluster_13: 10.88
- **Magnitude:** 470.52 | **LOC:** 677 | **CtrlFlow:** 60.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.9481%), Tech Debt (98.9597%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 219.6)
  * `executeOn` (Impact: 43.1)
  * `changeLineBreaks` (Impact: 37.6)
  * `changeLineBreaksAfterColumn` (Impact: 35.0)
    * *Intent:* // if "FOR TESTING" is directly followed by "RAISING" (with no comment in between), then "RAISING" i...
  * `separateWithEmptyLine` (Impact: 28.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 58`, `args: 22`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 19`, `state_mutation: 15`, `dead_code: 4`, `duplicate_logic: 4`, `orphaned_logic: 13`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 2`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.rulebase.*, java.time.LocalDate, com.sap.adt.abapcleaner.parser.*, com.sap.adt.abapcleaner.rulehelpers.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/DdlAnalyzer.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.032 IQR)
- **Top Global Matches:** file_cluster_8: 10.032, file_cluster_0: 10.1, file_cluster_13: 10.206
- **Magnitude:** 462.56 | **LOC:** 717 | **CtrlFlow:** 70.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.3819%), Tech Debt (99.1527%)
**Top Internal Functions/Classes:**
  * `addField` (Impact: 73.0)
  * `getResult` (Impact: 54.9)
    * *Intent:* // if the view of this data source is not known, the data source can still be used as the "final dat...
  * `getSourceField` (Impact: 53.4)
  * `analyzeAnnotations` (Impact: 42.2)
    * *Intent:* /**
  * `addFile` (Impact: 40.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 173`, `structural_boundaries: 74`, `args: 22`, `func_start: 28`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 87`, `state_mutation: 33`, `dead_code: 4`, `planned_debt: 2`, `duplicate_logic: 9`, `orphaned_logic: 4`
* *Architecture:* `io: 15`, `api: 9`, `import: 9`
* *Defense:* `safety: 2`, `doc: 7`, `immutability_locks: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.util.ArrayList, java.util.HashMap, com.sap.adt.abapcleaner.programbase.UnexpectedSyntaxBeforeChanges, com.sap.adt.abapcleaner.base.DDL, com.sap.adt.abapcleaner.base.StringUtil, com.sap.adt.abapcleaner.parser.Token, com.sap.adt.abapcleaner.parser.TokenSearch, com.sap.adt.abapcleaner.parser.Command...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleForDeclarations.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.541 IQR)
- **Top Global Matches:** file_cluster_8: 9.541, file_cluster_7: 10.086, file_cluster_0: 10.096
- **Magnitude:** 451.68 | **LOC:** 856 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.2274%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `executeOn` (Impact: 98.8)
  * `addMethodDefinitions` (Impact: 58.4)
  * `executeOnDeclarationCommand` (Impact: 54.3)
  * `isNeededPragmaOrPseudoCommentFound` (Impact: 46.4)
  * `addAssignedFieldSymbolOrDataRef` (Impact: 22.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 61`, `args: 19`, `func_start: 34`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 20`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 18`
* *Architecture:* `api: 14`, `import: 1`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.545
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.070318
  * `Imports (Out-Degree: 0):` com.sap.adt.abapcleaner.parser.*, java.util.HashMap, com.sap.adt.abapcleaner.rulehelpers.*, com.sap.adt.abapcleaner.base.*, com.sap.adt.abapcleaner.programbase.*
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/alignment/AlignMethodsDeclarationTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.45 IQR)
- **Top Global Matches:** file_cluster_8: 10.45, file_cluster_7: 11.171, file_cluster_0: 11.268
- **Magnitude:** 429.26 | **LOC:** 1896 | **CtrlFlow:** 56.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.9715%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testDoNotAlignAcrossEmptyLines` (Impact: 16.3)
  * `testDoNotAlignAcrossEmptyLinesOrComments` (Impact: 16.3)
  * `testAlignAcrossEmptyLinesAndComments` (Impact: 16.2)
  * `testDoNotAlignAcrossComments` (Impact: 16.2)
  * `testSeparateWithEmptyLine` (Impact: 14.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 53`, `args: 46`, `func_start: 1199`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 80`, `orphaned_logic: 45`
* *Architecture:* `import: 5`
* *Defense:* `test: 45`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.105
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` com.sap.adt.abapcleaner.rulebase.RuleTestBase, org.junit.jupiter.api.Test, org.junit.jupiter.api.BeforeEach, com.sap.adt.abapcleaner.rulebase.RuleID, com.sap.adt.abapcleaner.rulehelpers.ChangeType
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.006 IQR)
- **Top Global Matches:** file_cluster_8: 12.006, file_cluster_0: 12.009, file_cluster_11: 12.132
- **Magnitude:** 422.2 | **LOC:** 400 | **CtrlFlow:** 74.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.4561%), Tech Debt (30.8939%)
**Top Internal Functions/Classes:**
  * `align` (Impact: 178.4)
  * `overrideWidthIfColumnIsFollowedByLineBre` (Impact: 30.7)
  * `getTotalMonoLineWidth` (Impact: 12.0)
  * `removeLineAt` (Impact: 10.2)
  * `getTotalMultiLineWidth` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 40`, `args: 25`, `func_start: 29`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 29`, `dead_code: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 43`
* *Defense:* `doc: 8`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.634
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.086731
  * `Imports (Out-Degree: 0):` java.util.*, com.sap.adt.abapcleaner.parser.*
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/EmptySectionsInClassDefRule.java` (JAVA) | Magnitude: 121.92 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 149, structural_boundaries: 57, branch: 36, func_start: 16
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/ConfigLabel.java` (JAVA) | Magnitude: 55.32 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 21, state_mutation: 19, branch: 7
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/comparer/DisplayLine.java` (JAVA) | Magnitude: 81.64 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_tabs: 44, api: 24, structural_boundaries: 23, args: 15
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Code.java` (JAVA) | Magnitude: 163.58 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 156, structural_boundaries: 34, branch: 31, api: 29
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/syntax/ReceivingKeywordRule.java` (JAVA) | Magnitude: 76.58 | Delta: **0.033 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 88, structural_boundaries: 29, api: 21, func_start: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` (JAVA) | Magnitude: 1987.76 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 864, state_mutation: 599, indent_spaces: 430, branch: 383
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/NeedlessClearRule.java` (JAVA) | Magnitude: 189.3 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 182, branch: 62, structural_boundaries: 59, import: 21
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Profile.java` (JAVA) | Magnitude: 392.38 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 318, branch: 79, structural_boundaries: 78, api: 60
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/declarations/FinalVariableRule.java` (JAVA) | Magnitude: 120.38 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 92, structural_boundaries: 37, branch: 31, args: 15
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignClearFreeAndSortRule.java` (JAVA) | Magnitude: 188.84 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 198, branch: 63, structural_boundaries: 57, state_mutation: 21

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/Config.java` (JAVA) | Magnitude: 80.64 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 66, state_mutation: 28, structural_boundaries: 17, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/AlignTable.java` (JAVA) | Magnitude: 422.2 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 285, branch: 114, api: 43, structural_boundaries: 40
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/alignment/AlignDeclarationsRule.java` (JAVA) | Magnitude: 534.14 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 490, branch: 171, structural_boundaries: 99, func_start: 49
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/ITokenTypeRefiner.java` (JAVA) | Magnitude: 17.74 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, args: 1, func_start: 1, class_start: 1
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rules/prettyprinter/UpperAndLowerCaseRule.java` (JAVA) | Magnitude: 247.22 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 247, branch: 84, structural_boundaries: 47, func_start: 20
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulehelpers/CommentIdentifier.java` (JAVA) | Magnitude: 714.86 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_tabs: 373, branch: 269, structural_boundaries: 109, indent_spaces: 61

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/SystemInfo.java` (JAVA) | Magnitude: 30.5 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 22, branch: 9, structural_boundaries: 4, api: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> Churn: **68.33%** | Cog Load: 24.7948% | Debt: 99.7581%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 3246.42
- `com.sap.adt.abapcleaner.gui/src/com/sap/adt/abapcleaner/gui/FrmProfiles.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1987.76
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/TokenTest.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 1517.28
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/parser/CommandTest.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 995.96
- `test/com.sap.adt.abapcleaner.test/src/com/sap/adt/abapcleaner/rules/declarations/UnusedVariablesTest.java` -> **Jörg-Michael Grassau** (100.0% isolated ownership) | Magnitude: 913.02

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

- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/RuleID.java` -> **Severity: 2541.022** (Blast Radius: 59.661 * Doc Risk: 42.591%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/base/StringUtil.java` -> **Severity: 2406.3** (Blast Radius: 24.063 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/programbase/UnexpectedSyntaxAfterChanges.java` -> **Severity: 1794.293** (Blast Radius: 19.322 * Doc Risk: 92.8627%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/rulebase/Rule.java` -> **Severity: 1130.0** (Blast Radius: 11.3 * Doc Risk: 100.0%)
- `com.sap.adt.abapcleaner/src/com/sap/adt/abapcleaner/parser/Command.java` -> **Severity: 1015.5** (Blast Radius: 10.155 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
