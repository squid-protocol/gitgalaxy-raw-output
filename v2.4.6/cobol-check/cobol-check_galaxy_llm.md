# ARCHITECTURAL_BRIEF: cobol-check
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cobol-check` |
| **Timestamp** | `2026-08-03T19:26:09.543409+00:00` |
| **Scan Duration** | `0.99s` |
| **Git Branch** | `Developer` |
| **Git Commit** | `e372dd7f436c471883bd58ac71aab49861a57e5d` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-check.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 293 malicious artifacts.

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
| Total Artifacts | 384 |
| Analyzed Artifacts (Scanned) | 338 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 46 |
| Total LOC | 22518 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 88.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4644 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0795 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7799 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 22 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 143 | 16064 | 42.3% |
| COBOL | 110 | 4181 | 32.5% |
| PLAINTEXT | 20 | 0 | 5.9% |
| TYPESCRIPT | 20 | 1556 | 5.9% |
| MARKDOWN | 12 | 0 | 3.6% |
| BATCH | 9 | 99 | 2.7% |
| SHELL | 9 | 167 | 2.7% |
| JSON | 7 | 318 | 2.1% |
| CSS | 3 | 116 | 0.9% |
| XML | 2 | 0 | 0.6% |
| YAML | 1 | 1 | 0.3% |
| GROOVY | 1 | 1 | 0.3% |
| JAVASCRIPT | 1 | 15 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.892`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 230 | 68.0% |
| file_cluster_13 | 55 | 16.3% |
| file_cluster_0 | 9 | 2.7% |
| file_cluster_4 | 5 | 1.5% |
| file_cluster_16 | 4 | 1.2% |
| file_cluster_12 | 1 | 0.3% |
| file_cluster_2 | 1 | 0.3% |
| file_cluster_6 | 1 | 0.3% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 9.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 46*

**Composition by Extension & Reason:**
- `no_extension`: 13x Unsupported Format (.undeterminable), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cbl`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 3x Excluded (Explicitly Denied Extension: '.jar')
- `.java`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gradle`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 1x Excluded (Machine-Generated Source Code Signature: 200 LOC)
- `.cut`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 22.4 | 6.6 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.8 | 32.8 | 26.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 26.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.0 | 1.0 | 0.0 |
| API Exposure | 0.0 | 18.7 | 4.3 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 73.7 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 53.6 | 2.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 49.9 | 46.7 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 37.2 | 2.4 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 27.1 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (Hits: 52)
- `vs-code-extension/client/src/Helpers/PathHelper.ts` (Hits: 22)
- `src/main/cobol/DB2PROG.cbl` (Hits: 14)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Constants.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java`) — 45 inbound connections
2. **Config.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Config.java`) — 43 inbound connections
3. **PossibleInternalLogicErrorException.java** (`src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java`) — 26 inbound connections
4. **Messages.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java`) — 24 inbound connections
5. **StringHelper.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java`) — 24 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TestSuiteParserParsingTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java`) — 25 outbound dependencies
2. **CopybookExpanderIT.java** (`src/test/java/org/openmainframeproject/cobolcheck/CopybookExpanderIT.java`) — 23 outbound dependencies
3. **MockIT.java** (`src/test/java/org/openmainframeproject/cobolcheck/MockIT.java`) — 22 outbound dependencies
4. **TestSuiteParserCodeInsertionTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserCodeInsertionTest.java`) — 22 outbound dependencies
5. **ExpanderTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/ExpanderTest.java`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getParsedTestSuiteLines` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **1335.7** | LOC: 526
- `writeMultiLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java`) -> Impact: **311.1** | LOC: 61
  * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines
- `it_parses_file_section_variables_from_sp` (@ `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java`) -> Impact: **238.2** | LOC: 83
  * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
- `expand` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java`) -> Impact: **197.8** | LOC: 37
  * *Intent:* /** * Expand copybooks referenced by the code under test. * <p> * In the general use case, COPY statements are left alone and the compiler handles exp...
- `extractTokensFrom` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java`) -> Impact: **191.2** | LOC: 68
- `setFlagsForCurrentLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> Impact: **172.7** | LOC: 94
- `activate` (@ `vs-code-extension/client/src/extension.ts`) -> Impact: **157.6** | LOC: 211
- `run` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/LinuxProcessLauncher.java`) -> Impact: **150.2** | LOC: 53
- `readNextLineFromTestSuite` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **135.4** | LOC: 24
- `updateLineRepository` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java`) -> Impact: **135.3** | LOC: 45

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `OUTPUT-VALUE` (@ `src/test/cobol/MOCK/MockCallTest.cut`) -> **O(2^N) [Recursive]**
- `OUTPUT-VALUE` (@ `src/test/cobol/MOCK/MockCallTest.cut`) -> **O(2^N) [Recursive]**
- `expand` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java`) -> **O(2^N) [Recursive]**
  * *Intent:* /** * Expand copybooks referenced by the code under test. * <p> * In the general use case, COPY statements are left alone and the compiler handles exp...
- `extractCopybookNameFrom` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java`) -> **O(2^N) [Recursive]**
- `extractCopybookNameFromCopyStatement` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java`) -> **O(2^N) [Recursive]**
- `put` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> **O(2^N) [Recursive]**
- `put` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> **O(2^N) [Recursive]**
- `put` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> **O(2^N) [Recursive]**
- `put` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> **O(2^N) [Recursive]**
- `put` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `endsPath` (@ `vs-code-extension/client/src/Helpers/PathHelper.ts`) -> DB Complexity: **57**
- `constructor` (@ `vs-code-extension/client/src/services/CobolCheckOutputParser.ts`) -> DB Complexity: **38**
- `UT-ASSERT-ACCESSES` (@ `TESTPRG.CBL`) -> DB Complexity: **32**
- `findFile` (@ `vs-code-extension/client/src/services/CobolCheckLauncher.ts`) -> DB Complexity: **32**
- `Anonymous_Block` (@ `gradlew`) -> DB Complexity: **31**
  * *Intent:* # For Cygwin or MSYS, switch paths to Windows format before running java
- `setFlagsForCurrentLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> DB Complexity: **27**
- `multiple_mock_sections_gets_generated_co` (@ `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java`) -> DB Complexity: **27**
- `getSourceFolderContextPath` (@ `vs-code-extension/client/src/services/CobolCheckLauncher.ts`) -> DB Complexity: **26**
- `getParsedTestSuiteLines` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> DB Complexity: **22**
- `1000-INITIALIZE` (@ `src/main/cobol/FileCopy.cbl`) -> DB Complexity: **21**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/test/java/org/openmainframeproject/cobolcheck` | 27 | 6719.12 | 13.5% | 0.0% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser` | 21 | 5105.18 | 29.37% | 62.17% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter` | 8 | 2224.24 | 22.96% | 39.92% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic` | 8 | 1378.94 | 12.73% | 11.42% |
| `src/main/java/org/openmainframeproject/cobolcheck/services` | 8 | 1330.78 | 12.94% | 12.32% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace` | 6 | 1134.54 | 31.7% | 77.48% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects` | 5 | 1074.42 | 32.88% | 42.42% |
| `__monolith__` | 27 | 995.18 | 11.78% | 18.18% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/launcher` | 7 | 833.32 | 10.97% | 45.21% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers` | 5 | 642.88 | 28.79% | 59.95% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/main/cobol/DPICNUMBERS.CBL` -> **100.0%** Exposure
- `src/main/cobol/MOCKPARA.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP001-padded.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP001.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP002-padded.CBL` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `TESTPRG.CBL` -> **100.0%** Exposure
- `copybooks/CCHECKPD.CPY` -> **100.0%** Exposure
- `src/main/cobol/MOCK.CBL` -> **100.0%** Exposure
- `src/main/cobol/TESTNESTED.CBL` -> **100.0%** Exposure
- `src/main/resources/org/openmainframeproject/cobolcheck/copybooks/CCHECKPARAGRAPHSPD.CPY` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` -> **37** Orphaned Functions | **48** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` -> **43** Orphaned Functions | **11** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` -> **41** Orphaned Functions | **2** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` -> **30** Orphaned Functions | **11** Duplicates
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` -> **27** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`** -> AI Confidence: **99.48%**
2. **`src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandler.java`** -> AI Confidence: **99.31%**
3. **`src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java`** -> AI Confidence: **99.31%**
4. **`src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/TableEmbedDto.java`** -> AI Confidence: **99.31%**
5. **`src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java`** -> AI Confidence: **99.31%**
6. **`src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java`** -> AI Confidence: **99.31%**
7. **`src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteErrorLog.java`** -> AI Confidence: **99.31%**
8. **`src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java`** -> AI Confidence: **99.31%**
9. **`src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`** -> AI Confidence: **99.31%**
10. **`src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/Replace.java`** -> AI Confidence: **99.31%**
11. **`src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java`** -> AI Confidence: **99.31%**
12. **`src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java`** -> AI Confidence: **99.31%**
13. **`src/test/java/org/openmainframeproject/cobolcheck/MockIT.java`** -> AI Confidence: **99.31%**
14. **`src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java`** -> AI Confidence: **99.31%**
15. **`src/test/java/org/openmainframeproject/cobolcheck/TestSuiteErrorLogTest.java`** -> AI Confidence: **99.31%**
16. **`vs-code-extension/client/src/Helpers/ExtensionHelper.ts`** -> AI Confidence: **99.31%**
17. **`vs-code-extension/client/src/extension.ts`** -> AI Confidence: **99.31%**
18. **`copybooks/CCHECKPD.CPY`** -> AI Confidence: **99.29%**
19. **`src/main/cobol/copy/COPYR001-padded.CBL`** -> AI Confidence: **99.29%**
20. **`src/main/cobol/copy/COPYR001.CBL`** -> AI Confidence: **99.29%**
21. **`src/main/cobol/copy/EXR001-padded.CBL`** -> AI Confidence: **99.29%**
22. **`src/main/cobol/copy/EXR001.CBL`** -> AI Confidence: **99.29%**
23. **`src/main/resources/org/openmainframeproject/cobolcheck/copybooks/CCHECKPARAGRAPHSPD.CPY`** -> AI Confidence: **99.29%**
24. **`src/test/cobol/BIPM012/replac_more.cut`** -> AI Confidence: **99.29%**
25. **`src/test/cobol/BIPM012/replacing.cut`** -> AI Confidence: **99.29%**
26. **`src/test/cobol/DPICNUMBERS/NumbersExpect.cut`** -> AI Confidence: **99.29%**
27. **`src/test/cobol/FileCopy/FilecopyTests.cut`** -> AI Confidence: **99.29%**
28. **`src/test/cobol/GREETING/GreetingByName.cut`** -> AI Confidence: **99.29%**
29. **`src/test/cobol/GREETING/GreetingByType.cut`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandler.java` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandlerController.java` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/environmentSetup/EnvironmentSetup.java` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `vs-code-extension/client/src/test/runTest.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `TESTPRG.CBL` -> **100.0%** Exposure
- `src/main/cobol/FileCopy.cbl` -> **100.0%** Exposure
- `src/main/cobol/MOCK.CBL` -> **100.0%** Exposure
- `src/test/cobol/MOCK/MockCallTest.cut` -> **100.0%** Exposure
- `testfiles/CICDEMO-AFTER.CBL` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `857` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/FilePermission.java` (JAVA) -> Cumulative Risk: **869.7**
- **Archetype:** `file_cluster_13` (Distance: 12.421 IQR)
- **Magnitude:** 94.08 | **LOC:** 44 | **CtrlFlow:** 56.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9995%)
- **Heaviest Functions:** `setFilePermissionForAllUsers` (Impact: 62.1), `setFilePermissionForAllUsers` (Impact: 5.3)

### 2. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/CobolGenerator.java` (JAVA) -> Cumulative Risk: **855.4**
- **Archetype:** `file_cluster_13` (Distance: 12.057 IQR)
- **Magnitude:** 171.94 | **LOC:** 100 | **CtrlFlow:** 48.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `generateWhenOtherLines` (Impact: 40.2), `generateParagraphLines` (Impact: 25.9), `generateCommentBlock` (Impact: 13.9)

### 3. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA) -> Cumulative Risk: **845.78**
- **Archetype:** `file_cluster_0` (Distance: 11.541 IQR)
- **Magnitude:** 427.58 | **LOC:** 341 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setTestCounts` (Impact: 37.0), `setCurrentTestSuiteName` (Impact: 3.5), `setCurrentTestSuiteTests` (Impact: 3.5)

### 4. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/EvaluationGenerator.java` (JAVA) -> Cumulative Risk: **844.94**
- **Archetype:** `file_cluster_8` (Distance: 11.35 IQR)
- **Magnitude:** 125.68 | **LOC:** 90 | **CtrlFlow:** 37.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getEvaluationBody` (Impact: 20.6), `getEvaluationLines` (Impact: 16.8), `getEvaluationHeader` (Impact: 15.6)

### 5. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/BeforeAfterRepo.java` (JAVA) -> Cumulative Risk: **827.28**
- **Archetype:** `file_cluster_16` (Distance: 10.433 IQR)
- **Magnitude:** 110.4 | **LOC:** 106 | **CtrlFlow:** 36.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Documentation (99.9809%)
- **Heaviest Functions:** `getAllBranchingParagraphs` (Impact: 46.0), `getBeforeEachParagraphLines` (Impact: 13.6), `getAfterEachParagraphLines` (Impact: 13.6)

### 6. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` (JAVA) -> Cumulative Risk: **817.4**
- **Archetype:** `file_cluster_8` (Distance: 10.991 IQR)
- **Magnitude:** 223.14 | **LOC:** 170 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getCommentText` (Impact: 32.8), `getMockDescription` (Impact: 25.2), `getArgumentText` (Impact: 12.3)

### 7. `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT) -> Cumulative Risk: **815.39**
- **Archetype:** `file_cluster_4` (Distance: 13.284 IQR)
- **Magnitude:** 24.09 | **LOC:** 224 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.999%)
- **Heaviest Functions:** `updateFromDisk` (Impact: 25.2), `run` (Impact: 17.2), `getContentFromFilesystem` (Impact: 9.4)

### 8. `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/EncodingIO.java` (JAVA) -> Cumulative Risk: **803.77**
- **Archetype:** `file_cluster_13` (Distance: 9.337 IQR)
- **Magnitude:** 195.62 | **LOC:** 53 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `getReaderWithCorrectEncoding` (Impact: 103.7), `getWriterWithCorrectEncoding` (Impact: 73.5), `getWriterWithCorrectEncoding` (Impact: 7.5)

### 9. `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandlerController.java` (JAVA) -> Cumulative Risk: **791.05**
- **Archetype:** `file_cluster_8` (Distance: 11.06 IQR)
- **Magnitude:** 60.78 | **LOC:** 53 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (99.9998%)
- **Heaviest Functions:** `loadSettingsFromArguments` (Impact: 25.2), `isKeySet` (Impact: 3.5), `getKeyValue` (Impact: 3.5)

### 10. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA) -> Cumulative Risk: **790.87**
- **Archetype:** `file_cluster_8` (Distance: 10.189 IQR)
- **Magnitude:** 324.7 | **LOC:** 238 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `setCounts` (Impact: 64.0), `addTestSuite` (Impact: 4.6), `setName` (Impact: 4.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.349 IQR)
- **Top Global Matches:** file_cluster_8: 11.349, file_cluster_7: 11.648, file_cluster_13: 11.655
- **Magnitude:** 2244.66 | **LOC:** 1241 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (48.2437%), Tech Debt (24.2187%)
**Top Internal Functions/Classes:**
  * `getParsedTestSuiteLines` (Impact: 1335.7 | O(N^6) | DB: 22)
  * `readNextLineFromTestSuite` (Impact: 135.4 | O(2^N))
  * `getLinesUntilKeywordHit` (Impact: 127.7 | O(N^6) | DB: 6)
  * `getNextTokenFromTestSuite` (Impact: 72.0 | O(N^6) | DB: 1)
  * `addTestCodeForAssertion` (Impact: 68.8 | O(N^6) | DB: 8)
    * *Intent:* /** * Finds the mock, that the current verify statement is referencing and attaches * it. * Generate...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 68`, `args: 33`, `func_start: 78`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 158`, `dead_code: 2`, `planned_debt: 1`, `orphaned_logic: 8`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 5`, `doc: 33`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.List, java.io.BufferedReader, org.openmainframeproject.cobolcheck.services.log.Log, java.util.HashMap, org.openmainframeproject.cobolcheck.services.*, org.openmainframeproject.cobolcheck.exceptions.*, java.util.ArrayList, java.util.Locale...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.39 IQR)
- **Top Global Matches:** file_cluster_0: 13.39, file_cluster_8: 13.457, file_cluster_13: 13.547
- **Magnitude:** 1609.28 | **LOC:** 1163 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (74.9177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `multiple_mock_perform_evaluates_are_gene` (Impact: 58.4 | O(N^4) | DB: 21)
  * `multiple_mock_sections_gets_generated_co` (Impact: 53.1 | O(N^4) | DB: 27)
  * `section_mocks_generates_unique_identifie` (Impact: 46.6 | O(N^4))
  * `single_mock_call_with_args_gets_generate` (Impact: 37.7 | O(N^2) | DB: 15)
  * `CALL_MOCK_param_five_is_qualified_six_is` (Impact: 36.9 | O(N^6) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 146`, `args: 43`, `func_start: 88`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 626`, `duplicate_logic: 2`, `orphaned_logic: 41`
* *Architecture:* `io: 2`, `api: 42`, `import: 15`
* *Defense:* `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.services.Constants, org.mockito.Mockito, java.io.BufferedReader, java.util.List, org.mockito.Mock, java.io.Writer, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteErrorLogTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.798 IQR)
- **Top Global Matches:** file_cluster_8: 9.798, file_cluster_16: 9.98, file_cluster_0: 10.131
- **Magnitude:** 1261.84 | **LOC:** 590 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (20.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_catches_unexpected_keyword_inside_bef` (Impact: 103.3 | O(N^5))
  * `it_catches_unexpected_keyword_in_a_verif` (Impact: 91.2 | O(N^5))
  * `it_catches_unexpected_keyword_in_an_expe` (Impact: 85.3 | O(N^5))
  * `it_catches_unexpected_keyword_in_a_mock_` (Impact: 85.2 | O(N^5))
  * `it_catches_unexpected_keyword_at_the_end` (Impact: 85.2 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 119`, `args: 44`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 1`, `duplicate_logic: 9`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 24`, `import: 17`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.mockito.Mockito, org.openmainframeproject.cobolcheck.features.writer.CobolWriter, org.openmainframeproject.cobolcheck.services.Constants, java.io.BufferedReader, org.mockito.Mock, java.io.Writer, org.openmainframeproject.cobolcheck.exceptions.TestSuiteSyntaxException, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.443 IQR)
- **Top Global Matches:** file_cluster_8: 10.443, file_cluster_0: 10.662, file_cluster_13: 10.927
- **Magnitude:** 1230.2 | **LOC:** 1211 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (12.0663%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_parses_file_section_variables_from_sp` (Impact: 238.2 | O(N^5) | DB: 1)
    * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
  * `it_parses_WS_section_variables_from_spli` (Impact: 58.4 | O(N^6) | DB: 4)
  * `it_stores_file_section_lines_in_lineRepo` (Impact: 37.3 | O(N^4) | DB: 1)
    * *Intent:* // Test the lines in the DATA DIVISION FILE SECTION are stored in the lineRepository
  * `it_updates_numeric_fields` (Impact: 31.8 | O(N^4) | DB: 3)
  * `it_sets_CBL_rules_on_first_line` (Impact: 26.2 | O(N^4) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 154`, `args: 65`, `func_start: 201`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 28`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 43`
* *Architecture:* `io: 2`, `api: 53`, `import: 15`
* *Defense:* `test: 255`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.services.Constants, org.mockito.Mockito, java.io.BufferedReader, java.util.List, org.junit.jupiter.api.Assertions.*, java.io.IOException, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.431 IQR)
- **Top Global Matches:** file_cluster_8: 10.431, file_cluster_13: 10.609, file_cluster_16: 10.621
- **Magnitude:** 1031.78 | **LOC:** 659 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.3455%), Tech Debt (19.4283%)
**Top Internal Functions/Classes:**
  * `updateLineRepository` (Impact: 135.3 | O(N^6) | DB: 1)
  * `updateLineRepoByFileStatusToken` (Impact: 111.0 | O(N^6))
  * `updateNumericFields` (Impact: 95.4 | O(N^6) | DB: 3)
  * `interpretNextLine` (Impact: 43.5 | O(N^5) | DB: 1)
  * `updateLineRepoByCopyStatement` (Impact: 43.0 | O(N^5))
    * *Intent:* /** * If we are in the FILE SECTION and have read a multiline statement, we need to * add all lines ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 106`, `args: 52`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 27`, `duplicate_logic: 2`
* *Architecture:* `api: 61`, `import: 12`
* *Defense:* `safety: 10`, `doc: 20`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.004
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.012364
  * `Imports (Out-Degree: 8):` org.openmainframeproject.cobolcheck.services.Constants, java.io.BufferedReader, org.openmainframeproject.cobolcheck.services.log.Log, java.util.*, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.*, java.io.IOException, org.openmainframeproject.cobolcheck.services.platform.PlatformLookup...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.953 IQR)
- **Top Global Matches:** file_cluster_8: 11.953, file_cluster_13: 11.975, file_cluster_7: 12.087
- **Magnitude:** 903.62 | **LOC:** 624 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 27
- **Risk Profile:** Cognitive Load (41.1216%), Tech Debt (46.1928%)
**Top Internal Functions/Classes:**
  * `setFlagsForCurrentLine` (Impact: 172.7 | O(N^3) | DB: 27)
  * `isEndOfStatement` (Impact: 80.1 | O(N^5))
  * `getUsingArgs` (Impact: 79.4 | O(N^6) | DB: 3)
    * *Intent:* /** * @param line * @return true if the source line contains a batch file IO verb */
  * `shouldLineBeStubbed` (Impact: 73.9 | O(N^6))
    * *Intent:* /**
  * `getBeginningArea` (Impact: 40.4 | O(N^4))
    * *Intent:* /** * Checks if the line is in the format of a paragraph header, which is: * - It begins in area 'A'
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 78`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 98`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 40`, `import: 5`
* *Defense:* `safety: 2`, `doc: 55`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.711
  * `Choke Point (Betweenness):` 0.000344 | `Ripple Effect (Closeness):` 0.025135
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.features.interpreter.State, org.openmainframeproject.cobolcheck.features.interpreter.Area, java.util.*, java.util.regex.*, org.openmainframeproject.cobolcheck.services.platform.PlatformLookup, org.openmainframeproject.cobolcheck.services.platform.Platform
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.541 IQR)
- **Top Global Matches:** file_cluster_13: 10.541, file_cluster_8: 10.595, file_cluster_16: 11.003
- **Magnitude:** 816.02 | **LOC:** 415 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (21.6525%), Tech Debt (87.9444%)
**Top Internal Functions/Classes:**
  * `getCharsetForPlatform` (Impact: 92.7 | O(N^4) | DB: 1)
  * `load` (Impact: 69.7 | O(2^N) | DB: 10)
  * `getTestResultFormatStyle` (Impact: 67.8 | O(N^4))
  * `getTestResultFormat` (Impact: 56.6 | O(N^4))
  * `setDefaultLocaleOverride` (Impact: 41.1 | O(N^5) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 92`, `args: 53`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 113`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.267
  * `Choke Point (Betweenness):` 0.002171 | `Ripple Effect (Closeness):` 0.128527
  * `Imports (Out-Degree: 6):` java.util.List, org.openmainframeproject.cobolcheck.features.launcher.Formatter.DataTransferObjects.DataTransferObjectStyle, org.openmainframeproject.cobolcheck.services.log.Log, org.openmainframeproject.cobolcheck.services.platform.Platform, java.io.FileInputStream, java.io.File, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.TestOutputFormat, java.util.ArrayList...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.751 IQR)
- **Top Global Matches:** file_cluster_8: 11.751, file_cluster_0: 11.777, file_cluster_13: 11.869
- **Magnitude:** 788.82 | **LOC:** 932 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (34.6407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_throws_if_the_mock_that_verify_refere` (Impact: 56.9 | O(N^6))
  * `it_inserts_start_and_end_tag_as_comments` (Impact: 37.2 | O(N^3))
  * `verify_can_attach_to_call_mock_with_argu` (Impact: 26.4 | O(N^4) | DB: 7)
  * `it_parses_testsuite_with_sequnece_area` (Impact: 26.4 | O(N^4) | DB: 7)
  * `it_generates_after_each_branching_paragr` (Impact: 21.9 | O(N^4) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 215`, `args: 74`, `func_start: 83`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 198`, `duplicate_logic: 11`, `orphaned_logic: 30`
* *Architecture:* `io: 2`, `api: 40`, `import: 23`
* *Defense:* `safety: 1`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.extension.ExtendWith, org.openmainframeproject.cobolcheck.exceptions.VerifyReferencesNonexistentMockException, java.util.ArrayList, org.openmainframeproject.cobolcheck.services.cobolLogic.NumericFields, java.util.List, java.io.Writer, org.openmainframeproject.cobolcheck.exceptions.TestCaseAlreadyExistsException...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TESTPRG.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.825 IQR)
- **Top Global Matches:** file_cluster_8: 12.825, file_cluster_0: 13.233, file_cluster_11: 13.247
- **Magnitude:** 589.26 | **LOC:** 470 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 32
- **Risk Profile:** Cognitive Load (81.3843%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `UT-ASSERT-ACCESSES` (Impact: 77.4 | O(N^6) | DB: 32)
  * `UT-LOOKUP-MOCK` (Impact: 68.2 | O(N^6) | DB: 5)
  * `UT-COMPARE` (Impact: 40.5 | O(2^N) | DB: 3)
    * *Intent:* ***************************************************************** * COMPARE EXPECTED AND ACTUAL VALU...
  * `UT-SET-MOCK` (Impact: 33.6 | O(N^5) | DB: 5)
  * `2000-SPEAK` (Impact: 28.2 | O(N^4) | DB: 4)
    * *Intent:* ***************************************************************** * LOOK UP A FILE SPECIFICATION. **...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 111`, `structural_boundaries: 43`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 196`, `orphaned_logic: 19`
* *Architecture:* `api: 16`
* *Defense:* `safety: 30`, `test: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.629 IQR)
- **Top Global Matches:** file_cluster_8: 9.629, file_cluster_13: 9.755, file_cluster_7: 9.892
- **Magnitude:** 501.52 | **LOC:** 254 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (12.6001%), Tech Debt (13.2517%)
**Top Internal Functions/Classes:**
  * `writeMultiLine` (Impact: 311.1 | O(2^N))
    * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines
  * `getStringContinuationSign` (Impact: 86.4 | O(N^6))
  * `writeLine` (Impact: 25.9 | O(N^4) | DB: 1)
    * *Intent:* /**
  * `writeLines` (Impact: 12.2 | O(N^3))
  * `writeCommentedLines` (Impact: 12.2 | O(N^3))
    * *Intent:* /** * Writes an out-commented line of cobol code to the test output file. If the given line is too *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 33`, `args: 19`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 10`, `import: 8`
* *Defense:* `doc: 26`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.486
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.017804
  * `Imports (Out-Degree: 3):` java.util.List, java.io.Writer, org.openmainframeproject.cobolcheck.services.log.Log, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, java.util.ArrayList, java.io.IOException, org.openmainframeproject.cobolcheck.services.Config
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.12 IQR)
- **Top Global Matches:** file_cluster_13: 9.12, file_cluster_8: 9.242, file_cluster_16: 9.639
- **Magnitude:** 462.08 | **LOC:** 226 | **CtrlFlow:** 43.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (7.0863%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expand` (Impact: 197.8 | O(2^N) | DB: 4)
    * *Intent:* /** * Expand copybooks referenced by the code under test. * <p> * In the general use case, COPY stat...
  * `extractCopybookNameFrom` (Impact: 63.5 | O(2^N))
  * `extractCopybookNameFromCopyStatement` (Impact: 56.9 | O(2^N))
  * `expandDB2` (Impact: 49.6 | O(N^6) | DB: 4)
  * `findCopyBookNameEndPositionInCopyStateme` (Impact: 35.5 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 47`, `args: 11`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 5`
* *Architecture:* `io: 2`, `api: 7`, `import: 16`
* *Defense:* `safety: 2`, `doc: 9`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.373
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 9):` org.openmainframeproject.cobolcheck.services.Constants, java.util.List, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, org.openmainframeproject.cobolcheck.services.cobolLogic.CobolLine, org.openmainframeproject.cobolcheck.services.log.Log, java.nio.file.Files, java.nio.file.Paths, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.86%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.753 IQR)
- **Top Global Matches:** file_cluster_8: 9.753, file_cluster_16: 10.344, file_cluster_7: 10.437
- **Magnitude:** 430.94 | **LOC:** 725 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (21.2871%), Tech Debt (99.181%)
**Top Internal Functions/Classes:**
  * `getKeywordFor` (Impact: 123.5 | O(N^6))
  * `put` (Impact: 31.1 | O(2^N) | DB: 5)
  * `put` (Impact: 22.2 | O(2^N) | DB: 3)
  * `put` (Impact: 21.3 | O(2^N) | DB: 4)
  * `put` (Impact: 21.2 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 75`, `args: 42`, `func_start: 37`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 77`, `planned_debt: 1`, `duplicate_logic: 12`
* *Architecture:* `api: 3`, `import: 2`
* *Defense:* `doc: 2`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.52
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 1):` org.openmainframeproject.cobolcheck.services.Constants, java.util.*, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.541 IQR)
- **Top Global Matches:** file_cluster_0: 11.541, file_cluster_8: 11.941, file_cluster_13: 12.2
- **Magnitude:** 427.58 | **LOC:** 341 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (70.4702%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setTestCounts` (Impact: 37.0 | O(N^5) | DB: 5)
  * `setCurrentTestSuiteName` (Impact: 3.5 | O(N^2) | DB: 2)
  * `setCurrentTestSuiteTests` (Impact: 3.5 | O(N^2) | DB: 2)
  * `setCurrentTestSuiteFailures` (Impact: 3.5 | O(N^2) | DB: 2)
  * `setCurrentTestSuitePackage` (Impact: 3.5 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 117`, `args: 96`, `func_start: 108`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `duplicate_logic: 48`, `orphaned_logic: 37`
* *Architecture:* `api: 96`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, javax.xml.bind.annotation.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/Replace.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.161 IQR)
- **Top Global Matches:** file_cluster_13: 12.161, file_cluster_0: 12.679, file_cluster_8: 12.685
- **Magnitude:** 418.7 | **LOC:** 263 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (27.9735%), Tech Debt (74.4868%)
**Top Internal Functions/Classes:**
  * `replace` (Impact: 131.5 | O(2^N) | DB: 4)
  * `replaceInProgram` (Impact: 99.2 | O(2^N) | DB: 4)
  * `inspectProgram` (Impact: 49.7 | O(2^N) | DB: 4)
    * *Intent:* /** * Looks in the source line for the replace-key and replaces is with the replace-to-value. * * @p...
  * `showReplaceSets` (Impact: 36.0 | O(2^N))
    * *Intent:* /**
  * `getOutputFileName` (Impact: 11.9 | O(N^4) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 34`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 23`, `dead_code: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 5`, `api: 10`, `import: 8`
* *Defense:* `safety: 2`, `doc: 27`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.484
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.010682
  * `Imports (Out-Degree: 3):` java.util.LinkedList, org.openmainframeproject.cobolcheck.services.log.Log, java.io.*, java.util.regex.Matcher, org.openmainframeproject.cobolcheck.services.filehelpers.EncodingIO, java.util.regex.Pattern, org.openmainframeproject.cobolcheck.services.log.LogLevel, org.openmainframeproject.cobolcheck.services.Config...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteErrorLog.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.189 IQR)
- **Top Global Matches:** file_cluster_8: 9.189, file_cluster_13: 9.415, file_cluster_7: 9.844
- **Magnitude:** 409.46 | **LOC:** 223 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (14.356%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `checkExpectedTokenSyntax` (Impact: 69.9 | O(N^6))
  * `checkSyntaxInsideBlock` (Impact: 67.1 | O(N^5))
  * `logUnusedMocks` (Impact: 55.5 | O(N^6))
  * `logIdenticalMocks` (Impact: 45.4 | O(N^4))
  * `logVerifyReferencesNonExistentMock` (Impact: 45.3 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 32`, `args: 14`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` org.openmainframeproject.cobolcheck.services.Constants, java.util.List, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, org.openmainframeproject.cobolcheck.services.log.Log, java.io.*, org.openmainframeproject.cobolcheck.services.filehelpers.EncodingIO, java.util.Locale, java.util.Arrays...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.747 IQR)
- **Top Global Matches:** file_cluster_13: 10.747, file_cluster_8: 11.091, file_cluster_7: 11.46
- **Magnitude:** 377.52 | **LOC:** 285 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.1424%), Tech Debt (56.5234%)
**Top Internal Functions/Classes:**
  * `writeToSource` (Impact: 95.4 | O(N^6) | DB: 1)
  * `processingAfterEchoingSourceLineToOutput` (Impact: 93.0 | O(N^6) | DB: 2)
  * `echoingSourceLineToOutput` (Impact: 48.0 | O(N^5) | DB: 1)
  * `tryInsertEndEvaluateAtMockedCompomentEnd` (Impact: 34.3 | O(N^5) | DB: 2)
  * `processingBeforeEchoingSourceLineToOutpu` (Impact: 28.9 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 41`, `args: 11`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 5`, `import: 20`
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.04
  * `Choke Point (Betweenness):` 0.000298 | `Ripple Effect (Closeness):` 0.008902
  * `Imports (Out-Degree: 13):` org.openmainframeproject.cobolcheck.features.testSuiteParser.MockGenerator, org.openmainframeproject.cobolcheck.features.writer.WriterController, org.openmainframeproject.cobolcheck.exceptions.CobolSourceCouldNotBeReadException, java.util.List, org.openmainframeproject.cobolcheck.services.RunInfo, java.io.Writer, org.openmainframeproject.cobolcheck.services.cobolLogic.replace.Replace, java.io.Reader...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandler.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 9.075 IQR)
- **Top Global Matches:** file_cluster_13: 9.075, file_cluster_8: 9.145, file_cluster_7: 9.558
- **Magnitude:** 344.2 | **LOC:** 200 | **CtrlFlow:** 52.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (8.5904%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processCommandLineArgumentArray` (Impact: 111.9 | O(N^6))
  * `storeOptionSettings` (Impact: 79.8 | O(N^6) | DB: 1)
  * `loadArgProgramPaths` (Impact: 57.0 | O(N^6))
  * `lookupOption` (Impact: 22.8 | O(N^4))
  * `isKey` (Impact: 17.2 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 37`, `args: 9`, `func_start: 11`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 11`
* *Defense:* `doc: 7`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.432
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 6):` org.openmainframeproject.cobolcheck.services.Constants, java.util.List, org.openmainframeproject.cobolcheck.exceptions.CommandLineArgumentException, org.openmainframeproject.cobolcheck.services.log.Log, org.openmainframeproject.cobolcheck.services.StringHelper, java.util.HashMap, java.util.Map, java.util.Arrays...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.613 IQR)
- **Top Global Matches:** file_cluster_8: 8.613, file_cluster_16: 9.154, file_cluster_7: 9.199
- **Magnitude:** 338.9 | **LOC:** 204 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (21.9433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractTokensFrom` (Impact: 191.2 | O(N^6))
  * `handleEndOfWord` (Impact: 71.8 | O(N^6))
  * `tokenListEndsDuringMultiToken` (Impact: 13.9 | O(N^3))
  * `isDecimalPoint` (Impact: 13.9 | O(N^3))
  * `getPreviousCharacterFromBuffer` (Impact: 9.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 27`, `args: 12`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.845
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, java.util.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceStatementLocator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.651 IQR)
- **Top Global Matches:** file_cluster_13: 14.651, file_cluster_0: 14.776, file_cluster_11: 14.793
- **Magnitude:** 338.0 | **LOC:** 150 | **CtrlFlow:** 65.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (34.8902%), Tech Debt (96.1368%)
**Top Internal Functions/Classes:**
  * `createStatements` (Impact: 123.4 | O(N^6) | DB: 7)
  * `ReplaceStatementLocator` (Impact: 110.8 | O(2^N) | DB: 6)
  * `accumulateStatement` (Impact: 31.8 | O(N^4))
  * `ReplaceStatementLocator` (Impact: 15.7 | O(2^N))
  * `updateUntilInReplaceSets` (Impact: 14.1 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 21`, `args: 6`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 25`, `dead_code: 4`, `duplicate_logic: 2`, `orphaned_logic: 1`
* *Architecture:* `io: 2`, `api: 12`, `import: 3`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.LinkedList, java.io.*, org.jetbrains.annotations.NotNull, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.383 IQR)
- **Top Global Matches:** file_cluster_13: 10.383, file_cluster_8: 10.445, file_cluster_7: 10.86
- **Magnitude:** 331.68 | **LOC:** 183 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (31.6364%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseText` (Impact: 133.4 | O(N^5) | DB: 7)
    * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the con...
  * `instantiateBasedOnStyle` (Impact: 56.5 | O(N^4))
  * `setTestCaseValues` (Impact: 54.9 | O(N^5) | DB: 2)
  * `getFailureType` (Impact: 47.7 | O(N^6))
  * `Formatter` (Impact: 3.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 33`, `args: 14`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.305
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.003956
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.services.Constants, java.util.List, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, org.openmainframeproject.cobolcheck.services.log.Log, org.openmainframeproject.cobolcheck.features.launcher.Formatter.DataTransferObjects.*, org.openmainframeproject.cobolcheck.services.StringHelper, java.util.Locale, java.text.ParseException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.189 IQR)
- **Top Global Matches:** file_cluster_8: 10.189, file_cluster_13: 10.594, file_cluster_16: 10.77
- **Magnitude:** 324.7 | **LOC:** 238 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (33.7028%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `setCounts` (Impact: 64.0 | O(N^6) | DB: 1)
  * `addTestSuite` (Impact: 4.6 | O(N^3) | DB: 1)
  * `setName` (Impact: 4.6 | O(N^3) | DB: 1)
  * `addTestCase` (Impact: 4.6 | O(N^3) | DB: 1)
  * `setProgramName` (Impact: 4.6 | O(N^3) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 56`, `args: 46`, `func_start: 45`, `class_start: 4`
* *Risk/State:* `state_mutation: 29`, `duplicate_logic: 4`
* *Architecture:* `api: 65`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.732
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004451
  * `Imports (Out-Degree: 1):` java.util.ArrayList, org.openmainframeproject.cobolcheck.services.RunInfo, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.897 IQR)
- **Top Global Matches:** file_cluster_8: 9.897, file_cluster_13: 9.929, file_cluster_4: 10.351
- **Magnitude:** 322.08 | **LOC:** 171 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (23.4555%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeProcessOutputToTestResultsFile` (Impact: 130.7 | O(N^6) | DB: 1)
  * `getProcessOut` (Impact: 72.8 | O(N^6))
  * `cleanupOldTestResults` (Impact: 36.0 | O(N^4) | DB: 9)
  * `writeProcessOutputToFile` (Impact: 28.9 | O(N^4))
  * `writeProcessOutputWithFormat` (Impact: 20.6 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 39`, `args: 13`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 12`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.667
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 10):` org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.XMLFormat, org.openmainframeproject.cobolcheck.services.log.Log, java.io.*, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.TestOutputFormat, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.HTMLFormat, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.Formatter...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/TableEmbedDto.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.326 IQR)
- **Top Global Matches:** file_cluster_13: 10.326, file_cluster_8: 10.442, file_cluster_0: 10.884
- **Magnitude:** 292.26 | **LOC:** 133 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (55.2434%), Tech Debt (16.5889%)
**Top Internal Functions/Classes:**
  * `formatGeneratedArtifacts` (Impact: 68.1 | O(N^4) | DB: 7)
  * `getTestOverView` (Impact: 64.0 | O(N^6))
  * `generateHtmlForTestCase` (Impact: 45.5 | O(N^4) | DB: 2)
  * `setHtmlCharacterEnities` (Impact: 28.5 | O(N^4) | DB: 2)
  * `getDataTransferObject` (Impact: 25.8 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 33`, `args: 9`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 2`, `import: 9`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.RunInfo, java.time.format.DateTimeFormatter, java.io.File, java.util.HashMap, java.util.Map, org.openmainframeproject.cobolcheck.services.filehelpers.PathHelper, java.io.IOException, org.openmainframeproject.cobolcheck.services.Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.63 IQR)
- **Top Global Matches:** file_cluster_8: 11.63, file_cluster_13: 11.68, file_cluster_16: 11.863
- **Magnitude:** 279.24 | **LOC:** 305 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (35.2874%), Tech Debt (99.9828%)
**Top Internal Functions/Classes:**
  * `appendNextMeaningfulLineToCurrentLine` (Impact: 50.9 | O(N^6) | DB: 4)
    * *Intent:* /** * Sets and unsets flags that signifies the current state of the cobol being read, based * on the...
  * `peekNextMeaningfulLine` (Impact: 37.4 | O(N^5) | DB: 1)
    * *Intent:* /**
  * `readLine` (Impact: 21.7 | O(2^N) | DB: 3)
    * *Intent:* /**
  * `readTillHitToken` (Impact: 18.5 | O(N^4) | DB: 2)
  * `readTillEndOfStatement` (Impact: 13.8 | O(N^4) | DB: 5)
    * *Intent:* /** * Peeks the next line of the cobol file that is meaningful - that is; a line that is * not empty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 69`, `args: 25`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 52`, `duplicate_logic: 2`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 3`, `import: 6`
* *Defense:* `doc: 26`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.util.List, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, org.openmainframeproject.cobolcheck.services.cobolLogic.CobolLine, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, java.util.ArrayList, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, java.io.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/MockGenerator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.757 IQR)
- **Top Global Matches:** file_cluster_16: 11.757, file_cluster_13: 11.844, file_cluster_8: 12.067
- **Magnitude:** 234.96 | **LOC:** 168 | **CtrlFlow:** 44.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (39.3313%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `generateMockPerformCalls` (Impact: 89.0 | O(N^5) | DB: 1)
    * *Intent:* /**Generates the lines for Paragraphs based on mocks, * for each mock in a given list. * @param mock...
  * `generateMockCountInitializer` (Impact: 26.0 | O(N^4) | DB: 7)
  * `generateParagraphsForMock` (Impact: 18.0 | O(N^4) | DB: 3)
  * `generateMockParagraphs` (Impact: 17.9 | O(N^3) | DB: 3)
  * `generateMockCountValues` (Impact: 13.9 | O(N^3) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 32`, `args: 9`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 46`
* *Architecture:* `api: 8`, `import: 6`
* *Defense:* `doc: 13`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.277
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.006783
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.Constants, java.util.List, org.openmainframeproject.cobolcheck.services.StringHelper, java.util.ArrayList, java.util.Arrays, org.openmainframeproject.cobolcheck.services.Config
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/test/java/org/openmainframeproject/cobolcheck/ConfigIT.java` (JAVA) | Magnitude: 71.62 | Delta: **0.038 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 35, test: 24, func_start: 23
- `testfiles/REPLACE3.CBL` (COBOL) | Magnitude: 29.28 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 22, structural_boundaries: 5, func_start: 2
- `testfiles/REPLACE.CBL` (COBOL) | Magnitude: 43.14 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 33, structural_boundaries: 5, api: 4
- `testfiles/REPLACE2.CBL` (COBOL) | Magnitude: 57.24 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 43, structural_boundaries: 6, test: 5
- `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA) | Magnitude: 1609.28 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 929, state_mutation: 626, branch: 180, structural_boundaries: 146

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `vs-code-extension/Cobol-check/scripts/linux_gnucobol_run_tests` (SHELL) | Magnitude: 0.31 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, reflection_metaprogramming: 3, structural_boundaries: 2, safety: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/EIBResponseTable.java` (JAVA) | Magnitude: 90.96 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 84, state_mutation: 76, doc: 5
- `src/test/java/org/openmainframeproject/cobolcheck/LauncherTest.java` (JAVA) | Magnitude: 4.1 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, import: 5, func_start: 2
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/SectionOrParagraph.java` (JAVA) | Magnitude: 15.56 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, args: 4, func_start: 4
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/StringTokenizerExtractor.java` (JAVA) | Magnitude: 20.78 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, branch: 5, import: 4
- `src/main/java/org/openmainframeproject/cobolcheck/Main.java` (JAVA) | Magnitude: 49.78 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, branch: 5, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `vs-code-extension/client/src/vscode.proposed.testContinuousRun.d.ts` (TYPESCRIPT) | Magnitude: 1.75 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, structural_boundaries: 11, indent_tabs: 11, branch: 8
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keyword.java` (JAVA) | Magnitude: 69.84 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 13, api: 7, branch: 6
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/MockGenerator.java` (JAVA) | Magnitude: 234.96 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 46, structural_boundaries: 32, branch: 26
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/BeforeAfterRepo.java` (JAVA) | Magnitude: 110.4 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 21, state_mutation: 20, generics: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `vs-code-extension/client/src/services/CobolCheckOutputParser.ts` (TYPESCRIPT) | Magnitude: 19.16 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 115, indent_tabs: 83, branch: 32, ui_framework: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (TYPESCRIPT) | Magnitude: 33.78 | Delta: **0.348 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 184, state_mutation: 88, structural_boundaries: 72, branch: 59
- `vs-code-extension/client/src/Helpers/ExtensionHelper.ts` (TYPESCRIPT) | Magnitude: 12.52 | Delta: **0.349 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 92, concurrency: 39, branch: 29, args: 29
- `vs-code-extension/client/src/test/helper.ts` (TYPESCRIPT) | Magnitude: 4.6 | Delta: **0.383 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, indent_tabs: 17, api: 10, concurrency: 10
- `vs-code-extension/client/src/extension.ts` (TYPESCRIPT) | Magnitude: 49.31 | Delta: **0.455 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 302, state_mutation: 115, concurrency: 99, structural_boundaries: 90
- `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT) | Magnitude: 24.09 | Delta: **0.533 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 143, concurrency: 72, state_mutation: 62, structural_boundaries: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vs-code-extension/client/src/vscode.proposed.testCoverage.d.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 45, indent_tabs: 12, structural_boundaries: 9, dead_code: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceSet.java` (JAVA) | Magnitude: 195.34 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 26, branch: 20, api: 18
- `src/test/java/org/openmainframeproject/cobolcheck/testhelpers/Utilities.java` (JAVA) | Magnitude: 110.4 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, branch: 15, structural_boundaries: 9, api: 5
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA) | Magnitude: 903.62 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 416, branch: 123, state_mutation: 98, structural_boundaries: 78
- `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA) | Magnitude: 788.82 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 797, structural_boundaries: 215, state_mutation: 198, test: 99
- `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandlerController.java` (JAVA) | Magnitude: 60.78 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 15, structural_boundaries: 9, api: 7

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/test/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceTest.java` -> Churn: **52.48%** | Cog Load: 77.5515% | Debt: 0.0%
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/Replace.java` -> Churn: **50.27%** | Cog Load: 27.9735% | Debt: 74.4868%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 1230.2
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 1031.78
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 903.62
- `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 501.52
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 462.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 0.084** (Bridge: 0.0022 * Flux: 38.6351%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 99.8307%)
- `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 97.7857%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/EncodingIO.java` -> **Severity: 0.015** (Bridge: 0.0002 * Flux: 94.3608%)
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParserController.java` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 58.8707%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 9.587** (Embedded: 0.1285 * Error Risk: 74.5943%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 6.618** (Embedded: 0.0785 * Error Risk: 84.3201%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 5.58** (Embedded: 0.1007 * Error Risk: 55.433%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/PathHelper.java` -> **Severity: 4.3** (Embedded: 0.0762 * Error Risk: 56.416%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/platform/PlatformLookup.java` -> **Severity: 2.506** (Embedded: 0.0409 * Error Risk: 61.25%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java` -> **Severity: 4247.147** (Blast Radius: 53.09 * Doc Risk: 79.999%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 3985.1** (Blast Radius: 39.851 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 2826.7** (Blast Radius: 28.267 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 2341.0** (Blast Radius: 23.41 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 1720.371** (Blast Radius: 17.221 * Doc Risk: 99.8996%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
