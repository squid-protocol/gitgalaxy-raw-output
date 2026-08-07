# ARCHITECTURAL_BRIEF: cobol-check
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/cobol-check` |
| **Timestamp** | `2026-08-07T03:48:37.297185+00:00` |
| **Scan Duration** | `0.89s` |
| **Git Branch** | `Developer` |
| **Git Commit** | `e372dd7f436c471883bd58ac71aab49861a57e5d` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-check.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 293 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 100.0 | 22.3 | 6.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.9 | 41.1 | 52.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 28.8 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 6.7 | 1.0 | 0.0 |
| API Exposure | 0.0 | 18.7 | 4.3 | 3.7 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 29.2 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 73.7 | 1.3 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 78.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 4.4 | 0.4 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 53.6 | 2.9 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.6 | 24.9 | 0.0 |
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

- `getParsedTestSuiteLines` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **400.4** | LOC: 526
- `activate` (@ `vs-code-extension/client/src/extension.ts`) -> Impact: **108.5** | LOC: 211
- `it_parses_file_section_variables_from_sp` (@ `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java`) -> Impact: **91.4** | LOC: 84
  * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
- `setFlagsForCurrentLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> Impact: **88.7** | LOC: 94
- `constructor` (@ `vs-code-extension/client/src/services/CobolCheckOutputParser.ts`) -> Impact: **69.2** | LOC: 64
- `startTestRun` (@ `vs-code-extension/client/src/extension.ts`) -> Impact: **66.5** | LOC: 90
- `extractTokensFrom` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java`) -> Impact: **62.2** | LOC: 69
- `discoverTests` (@ `vs-code-extension/client/src/extension.ts`) -> Impact: **48.0** | LOC: 41
- `writeMultiLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java`) -> Impact: **47.0** | LOC: 61
  * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines
- `parseText` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java`) -> Impact: **46.8** | LOC: 69
  * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the constructor of the Formmatter. * @param text Test res...

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/test/java/org/openmainframeproject/cobolcheck` | 27 | 4127.42 | 13.5% | 0.0% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser` | 21 | 2415.58 | 28.86% | 61.44% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter` | 8 | 998.64 | 20.55% | 50.0% |
| `src/main/java/org/openmainframeproject/cobolcheck/services` | 8 | 804.38 | 12.94% | 12.32% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic` | 8 | 780.54 | 12.73% | 11.42% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects` | 5 | 770.32 | 32.88% | 45.6% |
| `__monolith__` | 27 | 744.68 | 11.79% | 18.18% |
| `testfiles` | 8 | 504.1 | 75.12% | 99.16% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace` | 6 | 494.04 | 31.68% | 82.21% |
| `src/main/cobol/copy` | 39 | 453.26 | 5.33% | 10.26% |

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
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` -> **8** Orphaned Functions | **36** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` -> **41** Orphaned Functions | **2** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` -> **30** Orphaned Functions | **11** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `5` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `857` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT) -> Cumulative Risk: **815.9**
- **Archetype:** `file_cluster_4` (Distance: 13.286 IQR)
- **Magnitude:** 24.44 | **LOC:** 224 | **CtrlFlow:** 32.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `run` (Impact: 17.2), `updateFromDisk` (Impact: 13.1), `getContentFromFilesystem` (Impact: 9.4)

### 2. `vs-code-extension/client/src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **730.5**
- **Archetype:** `file_cluster_4` (Distance: 11.815 IQR)
- **Magnitude:** 60.86 | **LOC:** 417 | **CtrlFlow:** 48.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9844%), Cognitive Load (98.2989%)
- **Heaviest Functions:** `activate` (Impact: 108.5), `startTestRun` (Impact: 66.5), `discoverTests` (Impact: 48.0)

### 3. `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **692.73**
- **Archetype:** `file_cluster_4` (Distance: 11.659 IQR)
- **Magnitude:** 32.78 | **LOC:** 298 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9976%), Concurrency (99.996%), Cognitive Load (94.9857%)
- **Heaviest Functions:** `findFile` (Impact: 21.6), `runCobolCheck` (Impact: 21.0), `getCobolProgramPathForGivenContext` (Impact: 16.8)

### 4. `testfiles/REPLACE3.CBL` (COBOL) -> Cumulative Risk: **655.71**
- **Archetype:** `file_cluster_0` (Distance: 16.62 IQR)
- **Magnitude:** 27.28 | **LOC:** 49 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9141%)
- **Heaviest Functions:** `3000-DYNAMIC-CALL` (Impact: 1.5), `9999-END` (Impact: 1.1)

### 5. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA) -> Cumulative Risk: **645.78**
- **Archetype:** `file_cluster_0` (Distance: 11.504 IQR)
- **Magnitude:** 395.78 | **LOC:** 341 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.9991%), State Flux (99.9897%)
- **Heaviest Functions:** `setTestCounts` (Impact: 13.0), `moveToNextTestSuite` (Impact: 2.6), `setNumberOfAllTests` (Impact: 2.6)

### 6. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` (JAVA) -> Cumulative Risk: **617.19**
- **Archetype:** `file_cluster_8` (Distance: 10.991 IQR)
- **Magnitude:** 156.04 | **LOC:** 170 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (99.7888%), State Flux (99.6926%)
- **Heaviest Functions:** `getCommentText` (Impact: 16.8), `getMockDescription` (Impact: 10.2), `getArgumentText` (Impact: 6.3)

### 7. `testfiles/REPLACE.CBL` (COBOL) -> Cumulative Risk: **611.41**
- **Archetype:** `file_cluster_0` (Distance: 16.543 IQR)
- **Magnitude:** 40.64 | **LOC:** 67 | **CtrlFlow:** 16.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.7023%), Safety Score (92.3261%)
- **Heaviest Functions:** `3000-DYNAMIC-CALL` (Impact: 1.5), `9999-END` (Impact: 1.1)

### 8. `testfiles/REPLACE2.CBL` (COBOL) -> Cumulative Risk: **599.27**
- **Archetype:** `file_cluster_0` (Distance: 16.421 IQR)
- **Magnitude:** 52.74 | **LOC:** 77 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (96.09%), Safety Score (94.6019%)
- **Heaviest Functions:** `3000-DYNAMIC-CALL` (Impact: 3.5), `9999-END` (Impact: 1.1)

### 9. `gradlew` (SHELL) -> Cumulative Risk: **591.38**
- **Archetype:** `file_cluster_8` (Distance: 13.503 IQR)
- **Magnitude:** 217.24 | **LOC:** 168 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), State Flux (100.0%), Spec Match (100.0%), Safety Score (99.8936%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 34.7), `Anonymous_Block` (Impact: 18.7), `Anonymous_Block` (Impact: 17.0)

### 10. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA) -> Cumulative Risk: **590.87**
- **Archetype:** `file_cluster_8` (Distance: 10.161 IQR)
- **Magnitude:** 209.7 | **LOC:** 238 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.9982%), State Flux (98.2782%), Tech Debt (95.5022%)
- **Heaviest Functions:** `setCounts` (Impact: 19.1), `setCurrentTestSuiteName` (Impact: 2.6), `setNumberOfAllTests` (Impact: 2.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.37 IQR)
- **Top Global Matches:** file_cluster_0: 13.37, file_cluster_8: 13.438, file_cluster_13: 13.528
- **Magnitude:** 1238.68 | **LOC:** 1163 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `single_mock_call_with_args_gets_generate` (Impact: 28.6)
  * `multiple_mock_perform_evaluates_are_gene` (Impact: 28.0)
  * `single_mock_section_gets_generated_corre` (Impact: 26.3)
  * `single_mock_paragraph_gets_generated_cor` (Impact: 26.3)
  * `single_mock_call_gets_generated_correctl` (Impact: 26.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 146`, `args: 43`, `func_start: 65`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 626`, `duplicate_logic: 2`, `orphaned_logic: 41`
* *Architecture:* `io: 2`, `api: 42`, `import: 15`
* *Defense:* `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.junit.jupiter.api.Test, org.openmainframeproject.cobolcheck.services.cobolLogic.NumericFields, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.features.writer.CobolWriter, org.mockito.Mockito, org.openmainframeproject.cobolcheck.services.Config, org.junit.jupiter.api.Assertions.*, org.mockito.Mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.261 IQR)
- **Top Global Matches:** file_cluster_8: 11.261, file_cluster_13: 11.555, file_cluster_7: 11.562
- **Magnitude:** 1001.56 | **LOC:** 1241 | **CtrlFlow:** 81.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.874%), Tech Debt (99.9998%)
**Top Internal Functions/Classes:**
  * `getParsedTestSuiteLines` (Impact: 400.4)
  * `getLinesUntilKeywordHit` (Impact: 38.2)
  * `readNextLineFromTestSuite` (Impact: 23.6)
  * `getNextTokenFromTestSuite` (Impact: 21.7)
  * `addTestCodeForAssertion` (Impact: 21.2)
    * *Intent:* /** * Finds the mock, that the current verify statement is referencing and attaches * it. * Generate...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 293`, `structural_boundaries: 68`, `args: 31`, `func_start: 77`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 154`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 36`, `orphaned_logic: 8`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 5`, `doc: 33`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.Locale, org.openmainframeproject.cobolcheck.services.*, org.openmainframeproject.cobolcheck.exceptions.*, java.util.ArrayList, org.openmainframeproject.cobolcheck.services.log.Log, java.util.List, java.io.IOException, java.util.HashMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.245 IQR)
- **Top Global Matches:** file_cluster_8: 10.245, file_cluster_0: 10.47, file_cluster_13: 10.742
- **Magnitude:** 648.7 | **LOC:** 1211 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.0663%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_parses_file_section_variables_from_sp` (Impact: 91.4)
    * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
  * `it_parses_WS_section_variables_from_spli` (Impact: 20.3)
  * `it_stores_file_section_lines_in_lineRepo` (Impact: 18.0)
    * *Intent:* // Test the lines in the DATA DIVISION FILE SECTION are stored in the lineRepository
  * `it_updates_numeric_fields` (Impact: 15.3)
  * `it_sets_CBL_rules_on_first_line_when_emp` (Impact: 12.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 166`, `structural_boundaries: 154`, `args: 65`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 28`, `planned_debt: 1`, `duplicate_logic: 11`, `orphaned_logic: 43`
* *Architecture:* `io: 2`, `api: 53`, `import: 15`
* *Defense:* `test: 255`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.features.interpreter.InterpreterController, org.openmainframeproject.cobolcheck.services.cobolLogic.DataType, org.openmainframeproject.cobolcheck.services.Constants, org.junit.jupiter.api.Assertions.*, org.mockito.Mockito, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, java.util.ArrayList...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.652 IQR)
- **Top Global Matches:** file_cluster_8: 11.652, file_cluster_0: 11.678, file_cluster_13: 11.772
- **Magnitude:** 528.82 | **LOC:** 932 | **CtrlFlow:** 22.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.6407%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_inserts_start_and_end_tag_as_comments` (Impact: 21.4)
  * `it_throws_if_the_mock_that_verify_refere` (Impact: 18.8)
  * `multiple_testcases_with_same_name_exists` (Impact: 16.2)
  * `it_parses_testsuite_with_sequnece_area` (Impact: 12.7)
  * `verify_can_attach_to_call_mock_with_argu` (Impact: 12.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 63`, `structural_boundaries: 215`, `args: 49`, `func_start: 58`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 198`, `duplicate_logic: 11`, `orphaned_logic: 30`
* *Architecture:* `io: 2`, `api: 40`, `import: 23`
* *Defense:* `safety: 1`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` org.openmainframeproject.cobolcheck.services.cobolLogic.NumericFields, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.mockito.junit.jupiter.MockitoExtension, org.openmainframeproject.cobolcheck.exceptions.VerifyReferencesNonexistentMockException, java.io.Writer, org.openmainframeproject.cobolcheck.features.writer.CobolWriter, org.mockito.Mock...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteErrorLogTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.757 IQR)
- **Top Global Matches:** file_cluster_8: 9.757, file_cluster_16: 9.939, file_cluster_0: 10.091
- **Magnitude:** 523.44 | **LOC:** 590 | **CtrlFlow:** 60.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.1174%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_catches_unexpected_keyword_inside_bef` (Impact: 39.4)
  * `it_catches_unexpected_keyword_in_a_verif` (Impact: 34.7)
  * `it_catches_unexpected_keyword_in_an_expe` (Impact: 32.7)
  * `it_catches_unexpected_keyword_in_a_mock_` (Impact: 32.6)
  * `it_catches_unexpected_keyword_at_the_end` (Impact: 32.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 119`, `args: 44`, `func_start: 49`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 1`, `duplicate_logic: 9`, `orphaned_logic: 17`
* *Architecture:* `io: 2`, `api: 24`, `import: 17`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` org.junit.jupiter.api.Assertions.assertEquals, org.openmainframeproject.cobolcheck.services.cobolLogic.DataType, org.openmainframeproject.cobolcheck.services.cobolLogic.NumericFields, org.junit.jupiter.api.Assertions.assertThrows, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.features.writer.CobolWriter, org.mockito.Mockito, org.openmainframeproject.cobolcheck.services.Config...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.405 IQR)
- **Top Global Matches:** file_cluster_8: 10.405, file_cluster_13: 10.567, file_cluster_16: 10.596
- **Magnitude:** 486.48 | **LOC:** 659 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.3336%), Tech Debt (99.9851%)
**Top Internal Functions/Classes:**
  * `updateLineRepository` (Impact: 40.3)
  * `updateLineRepoByFileStatusToken` (Impact: 32.7)
  * `updateNumericFields` (Impact: 28.3)
  * `interpretNextLine` (Impact: 15.4)
  * `updateDependencies` (Impact: 15.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 106`, `structural_boundaries: 106`, `args: 50`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 27`, `duplicate_logic: 21`
* *Architecture:* `api: 61`, `import: 12`
* *Defense:* `safety: 10`, `doc: 20`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.004
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.012364
  * `Imports (Out-Degree: 8):` org.openmainframeproject.cobolcheck.services.platform.PlatformLookup, org.openmainframeproject.cobolcheck.services.platform.Platform, java.util.*, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.log.Log...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.955 IQR)
- **Top Global Matches:** file_cluster_8: 11.955, file_cluster_13: 11.977, file_cluster_7: 12.089
- **Magnitude:** 480.12 | **LOC:** 624 | **CtrlFlow:** 61.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (41.1216%), Tech Debt (46.1928%)
**Top Internal Functions/Classes:**
  * `setFlagsForCurrentLine` (Impact: 88.7)
  * `isEndOfStatement` (Impact: 28.1)
  * `getUsingArgs` (Impact: 24.2)
    * *Intent:* /** * @param line * @return true if the source line contains a batch file IO verb */
  * `shouldLineBeStubbed` (Impact: 21.9)
    * *Intent:* /**
  * `getBeginningArea` (Impact: 17.0)
    * *Intent:* /** * Checks if the line is in the format of a paragraph header, which is: * - It begins in area 'A'
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `structural_boundaries: 78`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 98`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 40`, `import: 5`
* *Defense:* `safety: 2`, `doc: 55`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.711
  * `Choke Point (Betweenness):` 0.000344 | `Ripple Effect (Closeness):` 0.025135
  * `Imports (Out-Degree: 5):` org.openmainframeproject.cobolcheck.services.platform.PlatformLookup, org.openmainframeproject.cobolcheck.services.platform.Platform, java.util.*, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.features.interpreter.Area, org.openmainframeproject.cobolcheck.features.interpreter.State, java.util.regex.*
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.508 IQR)
- **Top Global Matches:** file_cluster_13: 10.508, file_cluster_8: 10.562, file_cluster_16: 10.971
- **Magnitude:** 430.12 | **LOC:** 415 | **CtrlFlow:** 42.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.6525%), Tech Debt (87.9444%)
**Top Internal Functions/Classes:**
  * `getCharsetForPlatform` (Impact: 37.5)
  * `getTestResultFormatStyle` (Impact: 27.6)
  * `getTestResultFormat` (Impact: 23.1)
  * `getCorrectRunContext` (Impact: 15.3)
  * `setDefaultLocaleOverride` (Impact: 14.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 92`, `args: 47`, `func_start: 56`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 113`, `import: 14`
* *Defense:* `safety: 3`, `doc: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.267
  * `Choke Point (Betweenness):` 0.002171 | `Ripple Effect (Closeness):` 0.128527
  * `Imports (Out-Degree: 6):` java.util.Locale, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.TestOutputFormat, org.openmainframeproject.cobolcheck.services.platform.Platform, java.io.File, java.io.FileInputStream, java.util.ArrayList, java.util.List, java.util.Properties...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_0` (Drift: 11.504 IQR)
- **Top Global Matches:** file_cluster_0: 11.504, file_cluster_8: 11.905, file_cluster_13: 12.165
- **Magnitude:** 395.78 | **LOC:** 341 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.4702%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setTestCounts` (Impact: 13.0)
  * `moveToNextTestSuite` (Impact: 2.6)
  * `setNumberOfAllTests` (Impact: 2.6)
  * `setNumberOffAllFailures` (Impact: 2.6)
  * `setCurrentTestSuiteName` (Impact: 2.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 117`, `args: 95`, `func_start: 96`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 75`, `duplicate_logic: 48`, `orphaned_logic: 37`
* *Architecture:* `api: 96`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` javax.xml.bind.annotation.*, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `TESTPRG.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.825 IQR)
- **Top Global Matches:** file_cluster_8: 12.825, file_cluster_0: 13.233, file_cluster_11: 13.247
- **Magnitude:** 350.96 | **LOC:** 470 | **CtrlFlow:** 72.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.3843%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `UT-ASSERT-ACCESSES` (Impact: 24.9)
  * `UT-LOOKUP-MOCK` (Impact: 20.7)
  * `2000-SPEAK` (Impact: 11.8)
    * *Intent:* ***************************************************************** * LOOK UP A FILE SPECIFICATION. **...
  * `UT-SET-MOCK` (Impact: 11.6)
  * `UT-COMPARE` (Impact: 8.6)
    * *Intent:* ***************************************************************** * COMPARE EXPECTED AND ACTUAL VALU...
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

### `gradlew` (SHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.503 IQR)
- **Top Global Matches:** file_cluster_8: 13.503, file_cluster_12: 13.541, file_cluster_11: 13.573
- **Magnitude:** 217.24 | **LOC:** 168 | **CtrlFlow:** 84.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.5691%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 34.7)
    * *Intent:* # For Cygwin or MSYS, switch paths to Windows format before running java
  * `Anonymous_Block` (Impact: 18.7)
    * *Intent:* # Increase the maximum file descriptors if we can.
  * `Anonymous_Block` (Impact: 17.0)
    * *Intent:* # Determine the Java command to use to start the JVM.
  * `Anonymous_Block` (Impact: 8.4)
    * *Intent:* # Need this for relative symlinks.
  * `save_[Truncated]` (Impact: 4.7)
    * *Intent:* # Escape application args
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 12`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 118`, `fragile_debt: 1`, `duplicate_logic: 6`, `orphaned_logic: 2`
* *Architecture:* `io: 14`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.87%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.161 IQR)
- **Top Global Matches:** file_cluster_8: 10.161, file_cluster_13: 10.568, file_cluster_16: 10.744
- **Magnitude:** 209.7 | **LOC:** 238 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.7028%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `setCounts` (Impact: 19.1)
  * `setCurrentTestSuiteName` (Impact: 2.6)
  * `setNumberOfAllTests` (Impact: 2.4)
  * `setNumberOffAllFailures` (Impact: 2.4)
  * `setCurrentTestSuiteTests` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 56`, `args: 43`, `func_start: 44`, `class_start: 4`
* *Risk/State:* `state_mutation: 29`, `duplicate_logic: 4`
* *Architecture:* `api: 65`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.732
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004451
  * `Imports (Out-Degree: 1):` org.openmainframeproject.cobolcheck.services.RunInfo, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteErrorLog.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.189 IQR)
- **Top Global Matches:** file_cluster_8: 9.189, file_cluster_13: 9.415, file_cluster_7: 9.844
- **Magnitude:** 170.86 | **LOC:** 223 | **CtrlFlow:** 62.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.356%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `checkSyntaxInsideBlock` (Impact: 23.0)
  * `checkExpectedTokenSyntax` (Impact: 20.9)
  * `logIdenticalMocks` (Impact: 18.6)
  * `logVerifyReferencesNonExistentMock` (Impact: 18.5)
  * `outputError` (Impact: 16.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 32`, `args: 14`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.util.Locale, org.openmainframeproject.cobolcheck.services.filehelpers.FilePermission, java.io.*, org.openmainframeproject.cobolcheck.services.filehelpers.EncodingIO, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Config, java.util.List, org.openmainframeproject.cobolcheck.services.log.Log...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.566 IQR)
- **Top Global Matches:** file_cluster_8: 11.566, file_cluster_13: 11.608, file_cluster_16: 11.802
- **Magnitude:** 169.94 | **LOC:** 305 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.9949%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `appendNextMeaningfulLineToCurrentLine` (Impact: 15.9)
    * *Intent:* /** * Sets and unsets flags that signifies the current state of the cobol being read, based * on the...
  * `peekNextMeaningfulLine` (Impact: 13.1)
    * *Intent:* /**
  * `readTillHitToken` (Impact: 8.1)
  * `readLine` (Impact: 6.1)
    * *Intent:* /**
  * `readTillEndOfStatement` (Impact: 6.0)
    * *Intent:* /** * Peeks the next line of the cobol file that is meaningful - that is; a line that is * not empty...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 69`, `args: 25`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 50`, `duplicate_logic: 10`, `orphaned_logic: 17`
* *Architecture:* `io: 1`, `api: 3`, `import: 6`
* *Defense:* `doc: 26`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, java.util.ArrayList, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor, java.util.List, org.openmainframeproject.cobolcheck.services.cobolLogic.CobolLine, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, java.io.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/cobol/MOCKTEST/MockCallTest.cut` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.288 IQR)
- **Top Global Matches:** file_cluster_8: 12.288, file_cluster_7: 12.752, file_cluster_0: 12.85
- **Magnitude:** 156.72 | **LOC:** 200 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (31.8389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `OUTPUT-value` (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `args: 21`, `func_start: 1`
* *Risk/State:* `state_mutation: 89`, `orphaned_logic: 1`
* *Architecture:* `api: 62`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` (JAVA | Tier 2 | 🚨 AI THREAT: 98.88%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.991 IQR)
- **Top Global Matches:** file_cluster_8: 10.991, file_cluster_13: 11.183, file_cluster_16: 11.28
- **Magnitude:** 156.04 | **LOC:** 170 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.2412%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `getCommentText` (Impact: 16.8)
  * `getMockDescription` (Impact: 10.2)
  * `getArgumentText` (Impact: 6.3)
  * `Mock` (Impact: 2.9)
  * `setIdentifier` (Impact: 2.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 39`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`, `orphaned_logic: 27`
* *Architecture:* `api: 31`, `import: 4`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.113
  * `Choke Point (Betweenness):` 1.3e-05 | `Ripple Effect (Closeness):` 0.011869
  * `Imports (Out-Degree: 2):` org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.Config, java.util.ArrayList, java.util.List
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.707 IQR)
- **Top Global Matches:** file_cluster_13: 10.707, file_cluster_8: 11.061, file_cluster_7: 11.43
- **Magnitude:** 155.02 | **LOC:** 285 | **CtrlFlow:** 49.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.1424%), Tech Debt (99.6943%)
**Top Internal Functions/Classes:**
  * `writeToSource` (Impact: 28.3)
  * `processingAfterEchoingSourceLineToOutput` (Impact: 27.9)
  * `echoingSourceLineToOutput` (Impact: 16.7)
  * `tryInsertEndEvaluateAtMockedCompomentEnd` (Impact: 12.0)
  * `mergeTestSuite` (Impact: 10.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 41`, `args: 10`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 28`, `duplicate_logic: 6`
* *Architecture:* `io: 3`, `api: 5`, `import: 20`
* *Defense:* `safety: 6`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.04
  * `Choke Point (Betweenness):` 0.000298 | `Ripple Effect (Closeness):` 0.008902
  * `Imports (Out-Degree: 13):` org.openmainframeproject.cobolcheck.features.interpreter.InterpreterController, org.openmainframeproject.cobolcheck.features.prepareMerge.PrepareMergeController, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.RunInfo, java.io.Writer, org.openmainframeproject.cobolcheck.features.writer.WriterController, org.openmainframeproject.cobolcheck.features.testSuiteParser.MockGenerator...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/Replace.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.136 IQR)
- **Top Global Matches:** file_cluster_13: 12.136, file_cluster_0: 12.655, file_cluster_8: 12.667
- **Magnitude:** 143.9 | **LOC:** 263 | **CtrlFlow:** 48.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (27.85%), Tech Debt (99.0462%)
**Top Internal Functions/Classes:**
  * `replace` (Impact: 27.5)
  * `replaceInProgram` (Impact: 20.8)
  * `inspectProgram` (Impact: 13.0)
    * *Intent:* /** * Looks in the source line for the replace-key and replaces is with the replace-to-value. * * @p...
  * `showReplaceSets` (Impact: 9.2)
    * *Intent:* /**
  * `sourceLineIsComment` (Impact: 5.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 34`, `args: 14`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 23`, `dead_code: 2`, `duplicate_logic: 4`
* *Architecture:* `io: 5`, `api: 10`, `import: 8`
* *Defense:* `safety: 2`, `doc: 27`, `immutability_locks: 7`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.484
  * `Choke Point (Betweenness):` 7.1e-05 | `Ripple Effect (Closeness):` 0.010682
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.filehelpers.FilePermission, org.openmainframeproject.cobolcheck.services.filehelpers.EncodingIO, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.log.Log, java.util.LinkedList, org.openmainframeproject.cobolcheck.services.log.LogLevel, java.util.regex.Pattern, java.util.regex.Matcher...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.211 IQR)
- **Top Global Matches:** file_cluster_13: 10.211, file_cluster_8: 10.285, file_cluster_7: 10.706
- **Magnitude:** 143.38 | **LOC:** 183 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (31.6364%), Tech Debt (67.8471%)
**Top Internal Functions/Classes:**
  * `parseText` (Impact: 46.8)
    * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the con...
  * `instantiateBasedOnStyle` (Impact: 23.0)
  * `setTestCaseValues` (Impact: 19.1)
  * `getFailureType` (Impact: 14.1)
  * `setTestCaseValues` (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 33`, `args: 6`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 27`, `duplicate_logic: 2`
* *Architecture:* `api: 6`, `import: 10`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.305
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.003956
  * `Imports (Out-Degree: 5):` java.util.Locale, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, java.util.Arrays, org.openmainframeproject.cobolcheck.services.log.Log, java.util.List, org.openmainframeproject.cobolcheck.features.launcher.Formatter.DataTransferObjects.*...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `testfiles/INVDATE-AFTER.CBL` (COBOL | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.06 IQR)
- **Top Global Matches:** file_cluster_8: 13.06, file_cluster_13: 13.229, file_cluster_11: 13.534
- **Magnitude:** 142.9 | **LOC:** 147 | **CtrlFlow:** 74.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (95.0448%), Tech Debt (99.9313%)
**Top Internal Functions/Classes:**
  * `2000-NEXT-INVOICE-DATE` (Impact: 7.7)
  * `2100-HANDLE-FEBRUARY` (Impact: 4.5)
  * `0000-MAIN` (Impact: 3.2)
  * `1000-PROCESS-INVOICES` (Impact: 2.2)
  * `UT-BEFORE` (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 10`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `state_mutation: 116`, `orphaned_logic: 10`
* *Architecture:* `import: 3`
* *Defense:* `safety: 2`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` DATETIME, ZUTZCWS, ZUTZCPD
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.496 IQR)
- **Top Global Matches:** file_cluster_8: 9.496, file_cluster_13: 9.604, file_cluster_7: 9.761
- **Magnitude:** 142.32 | **LOC:** 254 | **CtrlFlow:** 57.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.5017%), Tech Debt (99.9958%)
**Top Internal Functions/Classes:**
  * `writeMultiLine` (Impact: 47.0)
    * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines
  * `getStringContinuationSign` (Impact: 25.8)
  * `writeLine` (Impact: 10.8)
    * *Intent:* /**
  * `writeLines` (Impact: 6.2)
  * `writeCommentedLines` (Impact: 6.2)
    * *Intent:* /** * Writes an out-commented line of cobol code to the test output file. If the given line is too *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 33`, `args: 13`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 4`, `planned_debt: 2`, `duplicate_logic: 5`
* *Architecture:* `io: 3`, `api: 10`, `import: 8`
* *Defense:* `doc: 26`, `immutability_locks: 3`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.486
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.017804
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.Config, java.util.ArrayList, org.openmainframeproject.cobolcheck.services.log.Log, java.util.List, java.io.IOException, java.io.Writer, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/TableEmbedDto.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_13` (Drift: 10.346 IQR)
- **Top Global Matches:** file_cluster_13: 10.346, file_cluster_8: 10.462, file_cluster_0: 10.899
- **Magnitude:** 141.56 | **LOC:** 133 | **CtrlFlow:** 54.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.2434%), Tech Debt (32.5175%)
**Top Internal Functions/Classes:**
  * `formatGeneratedArtifacts` (Impact: 27.9)
  * `getTestOverView` (Impact: 19.1)
  * `generateHtmlForTestCase` (Impact: 18.7)
  * `getDataTransferObject` (Impact: 12.0)
  * `setHtmlCharacterEnities` (Impact: 11.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 33`, `args: 9`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 23`, `orphaned_logic: 2`
* *Architecture:* `io: 3`, `api: 2`, `import: 9`
* *Defense:* `safety: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` java.io.File, org.openmainframeproject.cobolcheck.services.RunInfo, org.openmainframeproject.cobolcheck.services.Config, java.time.format.DateTimeFormatter, java.io.IOException, java.util.HashMap, java.time.LocalDateTime, java.util.Map...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.8 IQR)
- **Top Global Matches:** file_cluster_8: 9.8, file_cluster_13: 9.816, file_cluster_4: 10.227
- **Magnitude:** 141.48 | **LOC:** 171 | **CtrlFlow:** 46.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.4555%), Tech Debt (98.8393%)
**Top Internal Functions/Classes:**
  * `writeProcessOutputToTestResultsFile` (Impact: 38.1)
  * `getProcessOut` (Impact: 22.5)
  * `cleanupOldTestResults` (Impact: 14.9)
  * `writeOutPutToConsole` (Impact: 13.8)
  * `writeProcessOutputToFile` (Impact: 12.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 39`, `args: 11`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 12`, `sync_locks: 5`, `immutability_locks: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.667
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 10):` org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.Formatter, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.TestOutputFormat, org.openmainframeproject.cobolcheck.services.filehelpers.FilePermission, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.HTMLFormat, org.openmainframeproject.cobolcheck.features.launcher.Formatter.Formats.XMLFormat, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.Config...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceTest.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.137 IQR)
- **Top Global Matches:** file_cluster_0: 12.137, file_cluster_13: 12.281, file_cluster_8: 12.496
- **Magnitude:** 137.52 | **LOC:** 147 | **CtrlFlow:** 43.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (77.5515%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `test_replace_leading` (Impact: 20.5)
  * `test_replace_FI01_only_when_the_line_is_` (Impact: 16.0)
  * `test_what_happends_when_we_have_a_big_re` (Impact: 11.6)
  * `test_for_linenumber_0_every_replace_is_p` (Impact: 11.5)
  * `test_output_file_name_is_set_to_path_for` (Impact: 3.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 29`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `state_mutation: 44`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 9`
* *Architecture:* `io: 10`, `api: 12`, `import: 6`
* *Defense:* `test: 47`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` org.junit.jupiter.api.Assertions.assertEquals, java.io.File, org.junit.jupiter.api.Assertions.*, org.openmainframeproject.cobolcheck.services.Config, java.nio.file.FileSystems, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.Test
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.561 IQR)
- **Top Global Matches:** file_cluster_8: 8.561, file_cluster_16: 9.104, file_cluster_7: 9.15
- **Magnitude:** 133.3 | **LOC:** 204 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.9433%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractTokensFrom` (Impact: 62.2)
  * `handleEndOfWord` (Impact: 21.9)
  * `tokenListEndsDuringMultiToken` (Impact: 7.2)
  * `isDecimalPoint` (Impact: 7.2)
  * `getPreviousCharacterFromBuffer` (Impact: 4.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 27`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 10`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.845
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 3):` org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, java.util.*, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/test/java/org/openmainframeproject/cobolcheck/ConfigIT.java` (JAVA) | Magnitude: 45.52 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 70, structural_boundaries: 35, test: 24, args: 13
- `testfiles/REPLACE3.CBL` (COBOL) | Magnitude: 27.28 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 34, state_mutation: 22, structural_boundaries: 5, func_start: 2
- `testfiles/REPLACE.CBL` (COBOL) | Magnitude: 40.64 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 52, state_mutation: 33, structural_boundaries: 5, api: 4
- `testfiles/REPLACE2.CBL` (COBOL) | Magnitude: 52.74 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 57, state_mutation: 43, structural_boundaries: 6, test: 5
- `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA) | Magnitude: 1238.68 | Delta: **0.068 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 929, state_mutation: 626, branch: 180, structural_boundaries: 146

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `vs-code-extension/Cobol-check/scripts/linux_gnucobol_run_tests` (SHELL) | Magnitude: 0.31 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: args: 3, reflection_metaprogramming: 3, structural_boundaries: 2, safety: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/EIBResponseTable.java` (JAVA) | Magnitude: 86.06 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 87, structural_boundaries: 84, state_mutation: 76, doc: 5
- `src/test/java/org/openmainframeproject/cobolcheck/LauncherTest.java` (JAVA) | Magnitude: 3.6 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 7, import: 5, test: 2
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/SectionOrParagraph.java` (JAVA) | Magnitude: 12.16 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 8, args: 4, func_start: 4
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/StringTokenizerExtractor.java` (JAVA) | Magnitude: 10.98 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 10, branch: 5, import: 4
- `src/main/java/org/openmainframeproject/cobolcheck/Main.java` (JAVA) | Magnitude: 20.38 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 10, branch: 5, state_mutation: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `vs-code-extension/client/src/vscode.proposed.testContinuousRun.d.ts` (TYPESCRIPT) | Magnitude: 2.91 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 18, structural_boundaries: 11, indent_tabs: 11, branch: 8
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keyword.java` (JAVA) | Magnitude: 33.24 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 13, api: 7, branch: 6
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/MockGenerator.java` (JAVA) | Magnitude: 130.56 | Delta: **0.087 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 104, state_mutation: 46, structural_boundaries: 32, branch: 26
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/BeforeAfterRepo.java` (JAVA) | Magnitude: 63.0 | Delta: **0.098 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 78, structural_boundaries: 21, state_mutation: 20, generics: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `vs-code-extension/client/src/services/CobolCheckOutputParser.ts` (TYPESCRIPT) | Magnitude: 19.16 | Delta: **0.278 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 115, indent_tabs: 83, branch: 32, ui_framework: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `vs-code-extension/client/src/Helpers/ExtensionHelper.ts` (TYPESCRIPT) | Magnitude: 12.52 | Delta: **0.349 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 92, concurrency: 39, branch: 29, args: 29
- `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (TYPESCRIPT) | Magnitude: 32.78 | Delta: **0.355 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 184, state_mutation: 88, structural_boundaries: 72, branch: 59
- `vs-code-extension/client/src/test/helper.ts` (TYPESCRIPT) | Magnitude: 4.0 | Delta: **0.383 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 22, indent_tabs: 17, api: 10, concurrency: 10
- `vs-code-extension/client/src/extension.ts` (TYPESCRIPT) | Magnitude: 60.86 | Delta: **0.457 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 302, state_mutation: 113, concurrency: 94, structural_boundaries: 90
- `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT) | Magnitude: 24.44 | Delta: **0.536 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 143, concurrency: 72, state_mutation: 62, structural_boundaries: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `vs-code-extension/client/src/vscode.proposed.testCoverage.d.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: doc: 45, indent_tabs: 12, structural_boundaries: 9, dead_code: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceSet.java` (JAVA) | Magnitude: 118.94 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 97, structural_boundaries: 26, branch: 20, api: 18
- `src/test/java/org/openmainframeproject/cobolcheck/testhelpers/Utilities.java` (JAVA) | Magnitude: 42.3 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 38, branch: 15, structural_boundaries: 9, api: 5
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java` (JAVA) | Magnitude: 141.48 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 129, structural_boundaries: 39, branch: 34, func_start: 16
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA) | Magnitude: 480.12 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 416, branch: 123, state_mutation: 98, structural_boundaries: 78
- `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA) | Magnitude: 528.82 | Delta: **0.026 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 797, structural_boundaries: 215, state_mutation: 198, test: 99

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/test/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceTest.java` -> Churn: **52.48%** | Cog Load: 77.5515% | Debt: 0.0%
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/Replace.java` -> Churn: **50.27%** | Cog Load: 27.85% | Debt: 99.0462%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 648.7
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 486.48
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 480.12
- `src/test/cobol/MOCKTEST/MockCallTest.cut` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 156.72
- `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 155.02

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

- `src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java` -> **Severity: 4045.771** (Blast Radius: 53.09 * Doc Risk: 76.2059%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 3985.1** (Blast Radius: 39.851 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 2826.578** (Blast Radius: 28.267 * Doc Risk: 99.9957%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 1923.382** (Blast Radius: 23.41 * Doc Risk: 82.1607%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/PathHelper.java` -> **Severity: 850.533** (Blast Radius: 11.061 * Doc Risk: 76.8948%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
