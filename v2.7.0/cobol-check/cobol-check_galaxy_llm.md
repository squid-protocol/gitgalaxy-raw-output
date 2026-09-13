# ARCHITECTURAL_BRIEF: cobol-check
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-check.git` |
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
| Total Artifacts | 384 |
| Analyzed Artifacts (Scanned) | 338 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 46 |
| Total LOC | 23014 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 88.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4686 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0671 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.6% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.7799 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 23 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 143 | 16433 | 42.3% |
| COBOL | 110 | 4181 | 32.5% |
| PLAINTEXT | 20 | 0 | 5.9% |
| TYPESCRIPT | 20 | 1689 | 5.9% |
| MARKDOWN | 12 | 0 | 3.6% |
| BATCH | 9 | 89 | 2.7% |
| SHELL | 9 | 171 | 2.7% |
| JSON | 7 | 318 | 2.1% |
| CSS | 3 | 116 | 0.9% |
| XML | 2 | 0 | 0.6% |
| YAML | 1 | 1 | 0.3% |
| GROOVY | 1 | 1 | 0.3% |
| JAVASCRIPT | 1 | 15 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 306 | 90.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 32 | 9.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 46*

**Composition by Extension & Reason:**
- `no_extension`: 14x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 18.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 43.0 | 56.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 17.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 5.8 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.4 | 2.9 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 73.7 | 1.3 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 63.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 3.8 | 0.3 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 53.6 | 2.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 50.6 | 52.3 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 33 | 18 | 0 | `TESTPRG.CBL` |
| cleanup | 32 | 17 | 0 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| guards | 1081 | 94 | 9 | `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` |
| danger | 586 | 100 | 3 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| concurrency | 134 | 13 | 0 | `vs-code-extension/client/src/extension.ts` |
| connectivity | 1464 | 166 | 10 | `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` |
| io | 335 | 61 | 3 | `vs-code-extension/client/src/services/CobolCheckLauncher.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 110 | 20 | 0 | `src/test/cobol/MOCKTEST/MockCallTest.cut` |
| time | 21 | 7 | 0 | `vs-code-extension/client/src/services/TestTree.ts` |
| serialization | 28 | 6 | 0 | `src/main/resources/org/openmainframeproject/cobolcheck/copybooks/CCHECKPARAGRAPHSPD.CPY` |
| regex | 51 | 21 | 0 | `vs-code-extension/client/src/services/CobolCheckConfiguration.ts` |
| events | 4 | 2 | 0 | `vs-code-extension/client/src/extension.ts` |
| tests | 1330 | 34 | 0 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| docs | 239 | 55 | 1 | `vs-code-extension/client/src/vscode.proposed.testCoverage.d.ts` |
| debt | 277 | 57 | 2 | `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` |
| mutation | 6805 | 192 | 56 | `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` |
| dead_code | 736 | 100 | 6 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 44 | 14 | 0 | `TESTPRG.CBL` |
| ml_ai | 8 | 3 | 0 | `vs-code-extension/client/src/services/TestTree.ts` |
| ui | 20 | 3 | 0 | `vs-code-extension/client/src/services/CobolCheckOutputParser.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (Hits: 52)
- `vs-code-extension/client/src/Helpers/PathHelper.ts` (Hits: 22)
- `gradlew` (Hits: 15)

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

- `getParsedTestSuiteLines` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **340.9** | LOC: 547
  * *Intent:* /** * Process the test suite as a series of tokens. When we have processed all the * input, getNextTokenFromTestSuite() * returns a null reference. * ...
- `setFlagsForCurrentLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> Impact: **88.7** | LOC: 94
  * *Intent:* /** * Sets flags based on a line, to be able to know which kinds of source * statements to look for when reading and interpreting lines. * * @param li...
- `activate` (@ `vs-code-extension/client/src/extension.ts`) -> Impact: **75.6** | LOC: 211
- `constructor` (@ `vs-code-extension/client/src/services/CobolCheckOutputParser.ts`) -> Impact: **67.2** | LOC: 64
- `writeMultiLine` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java`) -> Impact: **45.0** | LOC: 61
  * *Intent:* /** * Lines of test code in a test suite are Cobol-like, but not strictly Cobol. The descriptions for TESTSUITE and * TESTCASE specifications may exce...
- `parseText` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java`) -> Impact: **41.6** | LOC: 69
  * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the constructor of the Formmatter. * @param text Test res...
- `getLinesUntilKeywordHit` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **38.2** | LOC: 49
- `extractTokensFrom` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java`) -> Impact: **36.0** | LOC: 69
- `getKeywordFor` (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> Impact: **35.2** | LOC: 46
- `it_parses_file_section_variables_from_split_lines` (@ `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java`) -> Impact: **32.2** | LOC: 84
  * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/test/java/org/openmainframeproject/cobolcheck` | 27 | 3491.42 | 19.7% | 0.0% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser` | 21 | 2657.12 | 43.44% | 49.21% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter` | 8 | 1032.78 | 47.04% | 37.11% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic` | 8 | 790.2 | 20.82% | 5.64% |
| `src/main/java/org/openmainframeproject/cobolcheck/services` | 8 | 719.56 | 21.18% | 2.41% |
| `vs-code-extension/client/src/services` | 6 | 651.7 | 52.03% | 15.61% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects` | 5 | 600.62 | 37.79% | 46.53% |
| `__monolith__` | 27 | 552.82 | 5.88% | 2.24% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace` | 6 | 475.04 | 52.17% | 49.39% |
| `src/main/cobol/copy` | 39 | 453.26 | 0.57% | 10.26% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/main/cobol/copy/COPYP001-padded.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP001.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP002-padded.CBL` -> **100.0%** Exposure
- `src/main/cobol/copy/COPYP002.CBL` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `copybooks/CCHECKPD.CPY` -> **100.0%** Exposure
- `src/main/resources/org/openmainframeproject/cobolcheck/copybooks/CCHECKPARAGRAPHSPD.CPY` -> **100.0%** Exposure
- `gradlew` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/Status/Emitter.java` -> **100.0%** Exposure
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` -> **37** Orphaned Functions | **42** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` -> **54** Orphaned Functions | **0** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` -> **43** Orphaned Functions | **0** Duplicates
- `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` -> **41** Orphaned Functions | **0** Duplicates
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` -> **27** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `4` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `858` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT) -> Cumulative Risk: **837.72**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 179.62 | **LOC:** 224 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9882%), Tech Debt (93.6777%)
- **Heaviest Functions:** `run` (Impact: 17.2), `updateFromDisk` (Impact: 9.7), `updateFromContents` (Impact: 6.3)

### 2. `vs-code-extension/client/src/extension.ts` (TYPESCRIPT) -> Cumulative Risk: **730.33**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 426.0 | **LOC:** 417 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9996%)
- **Heaviest Functions:** `activate` (Impact: 75.6), `discoverTests` (Impact: 30.4), `createDirectoryItems` (Impact: 29.5)

### 3. `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (TYPESCRIPT) -> Cumulative Risk: **669.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 218.48 | **LOC:** 298 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.8592%), Concurrency (98.3054%)
- **Heaviest Functions:** `findFile` (Impact: 21.6), `runCobolCheck` (Impact: 17.5), `getCobolProgramPathForGivenContext` (Impact: 16.8)

### 4. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Mock.java` (JAVA) -> Cumulative Risk: **650.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 126.04 | **LOC:** 170 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.989%)
- **Heaviest Functions:** `getCommentText` (Impact: 8.8), `getMockDescription` (Impact: 5.2), `getArgumentText` (Impact: 3.4)

### 5. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA) -> Cumulative Risk: **647.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 146.0 | **LOC:** 238 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.1085%), Tech Debt (95.5022%)
- **Heaviest Functions:** `setCounts` (Impact: 10.1), `setCurrentTestCaseFailure` (Impact: 1.9), `setCurrentTestCaseErrorMessage` (Impact: 1.9)

### 6. `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA) -> Cumulative Risk: **639.81**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 305.38 | **LOC:** 341 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9809%)
- **Heaviest Functions:** `setTestCounts` (Impact: 7.0), `setCurrentTestCaseFailure` (Impact: 2.1), `setCurrentTestCaseErrorMessage` (Impact: 2.1)

### 7. `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/LineRepository.java` (JAVA) -> Cumulative Risk: **604.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 77.68 | **LOC:** 152 | **CtrlFlow:** 11.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9983%), Tech Debt (99.9798%), Documentation (92.8571%)
- **Heaviest Functions:** `addAccumulatedTokensFromCopyStatementToCopyTokens` (Impact: 9.1), `addExpandedCopyStatementsToFileSectionStatements` (Impact: 8.8), `addFileControlStatement` (Impact: 3.1)

### 8. `vs-code-extension/client/src/Helpers/ExtensionHelper.ts` (TYPESCRIPT) -> Cumulative Risk: **603.22**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 114.02 | **LOC:** 127 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `handleCobolCheckOut` (Impact: 25.2), `handleCobolCheckOutput` (Impact: 15.6), `showWebWiev` (Impact: 6.1)

### 9. `vs-code-extension/client/src/services/CobolCheckConfiguration.ts` (TYPESCRIPT) -> Cumulative Risk: **595.87**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 96.54 | **LOC:** 129 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.5724%), Verification (80.0%)
- **Heaviest Functions:** `setConfiguration` (Impact: 26.1), `getConfigurationValueFor` (Impact: 15.4), `getConfigurationMap` (Impact: 13.5)

### 10. `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/BeforeAfterRepo.java` (JAVA) -> Cumulative Risk: **589.62**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 70.6 | **LOC:** 106 | **CtrlFlow:** 14.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Tech Debt (96.7148%)
- **Heaviest Functions:** `getAllBranchingParagraphs` (Impact: 13.7), `getBeforeEachParagraphLines` (Impact: 3.6), `getAfterEachParagraphLines` (Impact: 3.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1148.82 | **LOC:** 1241 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (88.6446%), Tech Debt (23.7521%)
**Top Internal Functions/Classes:**
  * `getParsedTestSuiteLines` (Impact: 340.9)
    * *Intent:* /** * Process the test suite as a series of tokens. When we have processed all the * input, getNextT...
  * `getLinesUntilKeywordHit` (Impact: 38.2)
  * `addTestCodeForAssertion` (Impact: 21.2)
  * `getNextTokenFromTestSuite` (Impact: 14.3)
    * *Intent:* * we exhaust the list of tokens. * When the file read routine returns a null reference, it means we ...
  * `handleEndOfVerifyStatement` (Impact: 13.1)
    * *Intent:* /** * Finds the mock, that the current verify statement is referencing and attaches * it. * Generate...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 169 instances
* *State Mutation (weighted view):* 585
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 253`, `structural_boundaries: 110`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 247`, `dead_code: 2`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 5`, `doc: 14`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.io.BufferedReader, java.io.IOException, java.util.ArrayList, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Locale, java.util.concurrent.TransferQueue...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 972.98 | **LOC:** 1163 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.9177%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `multiple_mock_perform_evaluates_are_generated_correctly` (Impact: 14.4)
  * `single_mock_call_with_args_gets_generated_correctly_with_comment` (Impact: 13.8)
  * `multiple_mock_sections_gets_generated_correctly` (Impact: 13.2)
  * `single_mock_section_gets_generated_correctly_with_comment` (Impact: 12.7)
  * `single_mock_paragraph_gets_generated_correctly_with_comment` (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 196 instances
* *State Mutation (weighted view):* 635
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 146`, `args: 43`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 243`, `unreferenced_by_name: 43`
* *Architecture:* `io: 2`, `api: 42`, `import: 15`
* *Defense:* `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.io.BufferedReader, java.io.IOException, java.io.Writer, java.util.ArrayList, java.util.Arrays, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteErrorLogTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 635.44 | **LOC:** 590 | **CtrlFlow:** 37.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (89.7133%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_catches_unexpected_keyword_inside_before_each_block` (Impact: 18.4)
  * `it_catches_unexpected_keyword_in_a_verify_context` (Impact: 16.2)
  * `it_catches_unexpected_keyword_in_a_mock_context` (Impact: 15.3)
  * `it_catches_unexpected_keyword_at_the_end_of_mock_context_with_arguments_and_commas_1` (Impact: 15.3)
  * `it_catches_unexpected_keyword_at_the_end_of_mock_context_with_arguments_and_commas_2` (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 119 instances
* *State Mutation (weighted view):* 368
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 119`, `args: 44`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 130`, `unreferenced_by_name: 26`
* *Architecture:* `io: 2`, `api: 24`, `import: 17`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.io.BufferedReader, java.io.StringReader, java.io.Writer, org.junit.jupiter.api.AfterAll, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertThrows, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 526.22 | **LOC:** 624 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.1348%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `setFlagsForCurrentLine` (Impact: 88.7)
    * *Intent:* /** * Sets flags based on a line, to be able to know which kinds of source * statements to look for ...
  * `isEndOfStatement` (Impact: 28.1)
    * *Intent:* /** * Recognizes end of statement when * (a) - sourceLine ends with a period * (b) - previous line c...
  * `shouldLineBeStubbed` (Impact: 21.9)
    * *Intent:* /** * @param line * @param state * @return true if the source line should be commented out */
  * `getBeginningArea` (Impact: 17.0)
    * *Intent:* /** * Looks through the prefix-spaces in the source line in order to determine the * beginning area ...
  * `updateCurrentDataStructure` (Impact: 15.5)
    * *Intent:* /** * Depending on the line that is being interpreted, we want to make sure that we update * the cur...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 119`, `structural_boundaries: 80`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 75`, `dead_code: 2`
* *Architecture:* `api: 26`, `import: 5`
* *Defense:* `safety: 2`, `doc: 16`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.681
  * `Choke Point (Betweenness):` 0.000344 | `Ripple Effect (Closeness):` 0.025135
  * `Imports (Out-Degree: 5):` java.util.*, java.util.regex.*, org.openmainframeproject.cobolcheck.features.interpreter.Area, org.openmainframeproject.cobolcheck.features.interpreter.State, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.platform.Platform, org.openmainframeproject.cobolcheck.services.platform.PlatformLookup
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 469.6 | **LOC:** 1211 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (23.596%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_parses_file_section_variables_from_split_lines` (Impact: 32.2)
    * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
  * `it_parses_WS_section_variables_from_split_lines` (Impact: 10.4)
  * `it_stores_file_section_lines_in_lineRepository` (Impact: 9.3)
    * *Intent:* // Test the lines in the DATA DIVISION FILE SECTION are stored in the lineRepository
  * `it_updates_numeric_fields` (Impact: 7.8)
  * `it_sets_CBL_rules_on_first_line_when_empty` (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 38 instances
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 155`, `structural_boundaries: 165`, `args: 65`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 55`, `planned_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `io: 2`, `api: 53`, `import: 15`
* *Defense:* `test: 255`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.io.BufferedReader, java.io.IOException, java.util.ArrayList, java.util.Arrays, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vs-code-extension/client/src/extension.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 426.0 | **LOC:** 417 | **CtrlFlow:** 23.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (99.8418%), Tech Debt (28.235%)
**Top Internal Functions/Classes:**
  * `activate` (Impact: 75.6)
  * `discoverTests` (Impact: 30.4)
  * `createDirectoryItems` (Impact: 29.5)
  * `gatherTestItems` (Impact: 19.5)
  * `getDirectoryItems` (Impact: 9.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 84
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 80`, `structural_boundaries: 91`, `args: 37`, `func_start: 20`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 46`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`, `api: 2`, `concurrency: 34`, `import: 8`
* *Defense:* `safety: 5`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` ExtensionHelper, CobolCheckConfiguration, CobolCheckLauncher, TestTree, cutLanguageClientServerSetup, path, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 410.12 | **LOC:** 932 | **CtrlFlow:** 7.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.5759%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `it_throws_if_the_mock_that_verify_references_does_not_exist` (Impact: 8.9)
  * `multiple_testcases_with_same_name_exists_for_a_testsuite` (Impact: 7.5)
  * `it_parses_testsuite_with_sequnece_area` (Impact: 6.5)
  * `verify_can_attach_to_call_mock_with_arguments` (Impact: 6.4)
  * `it_generates_after_each_branching_paragraphs_correctly_with_comments` (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 215`, `args: 49`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 179`, `unreferenced_by_name: 41`
* *Architecture:* `io: 2`, `api: 40`, `import: 23`
* *Defense:* `safety: 1`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` java.io.BufferedReader, java.io.IOException, java.io.StringReader, java.io.Writer, java.util.ArrayList, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 352.88 | **LOC:** 659 | **CtrlFlow:** 20.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.4944%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `updateLineRepository` (Impact: 24.9)
    * *Intent:* /** * Updates the line repository with the given line, if it might have further use when testing. * ...
  * `updateLineRepoByFileStatusToken` (Impact: 21.2)
    * *Intent:* /** * If the given line contains a file status token, it will be added to a map to a * corresponding...
  * `updateNumericFields` (Impact: 17.1)
    * *Intent:* /** * If the current line is a numeric field, it will be added to the list of numeric fields. * We n...
  * `updateDependencies` (Impact: 10.0)
    * *Intent:* /** * Updates dependencies of the interpreter. * The following values can be updated, based on the g...
  * `updatePossibleMock` (Impact: 8.6)
    * *Intent:* /** * Updates possibleMockIdentifier, possibleMockType and possibleMockArgs * if a specific part of ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 94`, `structural_boundaries: 108`, `args: 50`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 45`
* *Architecture:* `api: 36`, `import: 12`
* *Defense:* `safety: 10`, `doc: 12`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.984
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.012364
  * `Imports (Out-Degree: 8):` java.io.BufferedReader, java.io.IOException, java.util.*, org.openmainframeproject.cobolcheck.exceptions.CobolSourceCouldNotBeReadException, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 305.38 | **LOC:** 341 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.6826%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `setTestCounts` (Impact: 7.0)
  * `setCurrentTestCaseFailure` (Impact: 2.1)
  * `setCurrentTestCaseErrorMessage` (Impact: 2.1)
  * `setNumberOfAllTests` (Impact: 1.6)
  * `setNumberOffAllFailures` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 117`, `args: 95`, `func_start: 95`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `duplicate_logic: 42`, `unreferenced_by_name: 37`
* *Architecture:* `api: 96`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, javax.xml.bind.annotation.*
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 293.52 | **LOC:** 415 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.2001%), Tech Debt (8.6468%)
**Top Internal Functions/Classes:**
  * `getCharsetForPlatform` (Impact: 22.0)
  * `getTestResultFormatStyle` (Impact: 12.8)
  * `getTestResultFormat` (Impact: 10.7)
  * `getCorrectRunContext` (Impact: 9.1)
  * `resolveFilenameSuffixes` (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 92`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `io: 3`, `api: 81`, `import: 14`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 28.085
  * `Choke Point (Betweenness):` 0.002171 | `Ripple Effect (Closeness):` 0.128527
  * `Imports (Out-Degree: 6):` java.io.File, java.io.FileInputStream, java.io.IOException, java.util.ArrayList, java.util.List, java.util.Locale, java.util.Properties, org.openmainframeproject.cobolcheck.exceptions.IOExceptionProcessingConfigFile...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `TESTPRG.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 230.56 | **LOC:** 470 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (55.8245%), Tech Debt (27.6207%)
**Top Internal Functions/Classes:**
  * `UT-ASSERT-ACCESSES` (Impact: 18.1)
  * `UT-LOOKUP-MOCK` (Impact: 13.9)
  * `FILE-CONTROL` (Impact: 11.0)
  * `2000-SPEAK` (Impact: 7.8)
  * `UT-SET-MOCK` (Impact: 6.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 68`, `func_start: 20`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `unreferenced_by_name: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vs-code-extension/client/src/services/CobolCheckLauncher.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 218.48 | **LOC:** 298 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.1892%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `findFile` (Impact: 21.6)
  * `runCobolCheck` (Impact: 17.5)
  * `getCobolProgramPathForGivenContext` (Impact: 16.8)
  * `getSourceFolderContextPath` (Impact: 11.3)
  * `getFileName` (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 20
* *State Mutation (weighted view):* 41
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 72`, `args: 22`, `func_start: 18`
* *Risk/State:* `state_mutation: 15`
* *Architecture:* `io: 52`, `api: 16`, `concurrency: 10`, `import: 9`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.228
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.008902
  * `Imports (Out-Degree: 3):` Logger, CobolCheckConfiguration, CobolCheckOutputParser, child_process, fs, path, vscode, vscode-languageclient
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 204.72 | **LOC:** 254 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.2624%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `writeMultiLine` (Impact: 45.0)
    * *Intent:* /** * Lines of test code in a test suite are Cobol-like, but not strictly Cobol. The descriptions fo...
  * `getStringContinuationSign` (Impact: 25.8)
  * `writeLine` (Impact: 7.9)
    * *Intent:* /** * Writes a line of cobol code to the test output file. If the given line is too * long for cobol...
  * `writeLines` (Impact: 4.5)
    * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines * are to...
  * `writeCommentedLines` (Impact: 4.5)
    * *Intent:* /** * Comments out and writes all the given lines of cobol code to the test output file. * If the an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`, `structural_boundaries: 34`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `io: 3`, `api: 8`, `import: 8`
* *Defense:* `doc: 10`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.464
  * `Choke Point (Betweenness):` 0.000157 | `Ripple Effect (Closeness):` 0.017804
  * `Imports (Out-Degree: 3):` java.io.IOException, java.io.Writer, java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteErrorLog.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 201.56 | **LOC:** 223 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.8615%), Tech Debt (90.7814%)
**Top Internal Functions/Classes:**
  * `checkSyntaxInsideBlock` (Impact: 23.0)
  * `checkExpectedTokenSyntax` (Impact: 20.9)
  * `logIdenticalMocks` (Impact: 12.0)
  * `logVerifyReferencesNonExistentMock` (Impact: 11.9)
  * `logUnusedMocks` (Impact: 10.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 79
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 35`, `unreferenced_by_name: 9`
* *Architecture:* `io: 6`, `api: 12`, `import: 10`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` java.io.*, java.util.Arrays, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 199.42 | **LOC:** 287 | **CtrlFlow:** 26.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.8755%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `stubLine` (Impact: 16.8)
  * `ExcludeBetweenTags` (Impact: 15.0)
  * `occursFirst` (Impact: 10.6)
    * *Intent:* /** * Checks if a character occurs before another * * @param expectedFirst - The char expected to be...
  * `swapChars` (Impact: 10.5)
    * *Intent:* /** * Swaps two characters in a given string. * Example: swapChars("1.000.000,00", '.', ',') ~ "1,00...
  * `equalsAny` (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 50`, `structural_boundaries: 48`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 14`
* *Architecture:* `api: 23`, `import: 4`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.109
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.078484
  * `Imports (Out-Degree: 0):` java.util.Collection, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 24):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 180.44 | **LOC:** 305 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2428%), Tech Debt (99.8691%)
**Top Internal Functions/Classes:**
  * `appendNextMeaningfulLineToCurrentLine` (Impact: 11.8)
  * `readTillHitToken` (Impact: 8.1)
    * *Intent:* /** * Reads lines from the current line, until a specific token is hit. This will forward the reader...
  * `peekNextMeaningfulLine` (Impact: 8.0)
    * *Intent:* /** * Peeks the next line of the cobol file that is meaningful - that is; a line that is * not empty...
  * `readLine` (Impact: 4.0)
    * *Intent:* /** * Reads the next line of the cobol file. * * @return (CobolLine) The line that was read * * @thr...
  * `readTillEndOfStatement` (Impact: 3.9)
    * *Intent:* /** * Reads the current statement till the end. This will forward the reader till the end of * the s...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 105
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 69`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 47`, `unreferenced_by_name: 18`
* *Architecture:* `io: 1`, `api: 3`, `import: 6`
* *Defense:* `doc: 10`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` java.io.*, java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.cobolLogic.CobolLine, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `vs-code-extension/client/src/services/TestTree.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 179.62 | **LOC:** 224 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (93.4063%), Tech Debt (93.6777%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 17.2)
  * `updateFromDisk` (Impact: 9.7)
  * `updateFromContents` (Impact: 6.3)
    * *Intent:* /** * Parses the tests from the input text, and updates the tests contained * by this file to be tho...
  * `getContentFromFilesystem` (Impact: 6.2)
  * `setDirectoryDetails` (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 13 instances
* *Concurrency (weighted view):* 42
* *State Mutation (weighted view):* 48
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 47`, `args: 22`, `func_start: 19`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 22`, `dead_code: 3`, `planned_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 17`, `concurrency: 22`, `import: 8`
* *Defense:* `safety: 4`, `doc: 1`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.358
  * `Choke Point (Betweenness):` 9e-06 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 5):` ExtensionHelper, CobolCheckConfiguration, CobolCheckInputParser, CobolCheckLauncher, stream, util, vscode, vscode-languageclient
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 171.5 | **LOC:** 204 | **CtrlFlow:** 21.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.0702%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `extractTokensFrom` (Impact: 36.0)
  * `handleEndOfWord` (Impact: 21.9)
  * `isDecimalPoint` (Impact: 7.2)
    * *Intent:* /** * Decimal point is recognized when a period or comma appears between two numeric digits. */
  * `tokenListEndsDuringMultiToken` (Impact: 4.7)
  * `addTokenAndClearBuffer` (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.82
  * `Choke Point (Betweenness):` 3.5e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 3):` java.util.*, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `gradlew` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 164.92 | **LOC:** 168 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.6679%), Tech Debt (32.8653%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 14.9)
    * *Intent:* # For Cygwin or MSYS, switch paths to Windows format before running java
  * `Anonymous_Block` (Impact: 8.0)
    * *Intent:* # Determine the Java command to use to start the JVM.
  * `Anonymous_Block` (Impact: 6.7)
    * *Intent:* # Increase the maximum file descriptors if we can.
  * `Anonymous_Block` (Impact: 4.5)
    * *Intent:* # Need this for relative symlinks.
  * `__global_context__` (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 71`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 40`, `fragile_debt: 1`
* *Architecture:* `io: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.065
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 157.92 | **LOC:** 183 | **CtrlFlow:** 31.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.8063%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseText` (Impact: 41.6)
    * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the con...
  * `instantiateBasedOnStyle` (Impact: 14.7)
  * `setTestCaseValues` (Impact: 12.5)
  * `getFailureType` (Impact: 9.2)
  * `Formatter` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.29
  * `Choke Point (Betweenness):` 3.8e-05 | `Ripple Effect (Closeness):` 0.003956
  * `Imports (Out-Degree: 5):` java.text.ParseException, java.util.Arrays, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.features.interpreter.StringTokenizerExtractor, org.openmainframeproject.cobolcheck.features.launcher.Formatter.DataTransferObjects.*, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/StringTokenizerExtractor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 157.32 | **LOC:** 169 | **CtrlFlow:** 21.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (58.8396%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `swapStringsOutWithMappedTokens` (Impact: 32.1)
    * *Intent:* /** * Swaps out strings in the given line, with tags, so each string will be seen as a single * toke...
  * `extractTokensFrom` (Impact: 16.1)
    * *Intent:* /** * Extracts tokens meaningful for processing Cobol source code from a Cobol source line. * * Such...
  * `swapMappedTokensOutWithSavedStrings` (Impact: 5.5)
  * `StringTokenizerExtractor` (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.472
  * `Choke Point (Betweenness):` 0.000105 | `Ripple Effect (Closeness):` 0.017455
  * `Imports (Out-Degree: 4):` java.util.*, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 152.8 | **LOC:** 200 | **CtrlFlow:** 25.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.7751%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `processCommandLineArgumentArray` (Impact: 22.1)
  * `storeOptionSettings` (Impact: 15.7)
    * *Intent:* /** * Convert an option specification string into a map of option keys and values. * * @param option...
  * `loadArgProgramPaths` (Impact: 9.1)
  * `lookupOption` (Impact: 6.1)
  * `ArgumentHandler` (Impact: 5.6)
    * *Intent:* /** * Parse command-line options using the optionsString to validate. * * @param args - String[] - o...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 66
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 37`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`, `dead_code: 1`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.416
  * `Choke Point (Betweenness):` 1.8e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 6):` java.util.Arrays, java.util.HashMap, java.util.List, java.util.Map, org.openmainframeproject.cobolcheck.exceptions.CommandLineArgumentException, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParserController.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 147.04 | **LOC:** 347 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.6199%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getBoilerplateCodeFromCopybooks` (Impact: 9.6)
    * *Intent:* /** * Gets the lines from the cobol-check boilerplate copybooks, one for Working-Storage * and one f...
  * `generateCobolLinesForUnmockedCalls` (Impact: 5.0)
  * `getWorkingStorageTestCode` (Impact: 3.8)
    * *Intent:* /** * Gets the Working-Storage Section test code to be inserted into the program being generated. * ...
  * `getProcedureDivisionTestCode` (Impact: 3.7)
    * *Intent:* /** * Gets the PROCEDURE DIVISION test code to be inserted into the program being generated. * * @re...
  * `concatenateTestSuites` (Impact: 3.2)
    * *Intent:* /** * Each testsuite might be in its own file. This method combines all the testsuites, pertaining t...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 68`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 54`
* *Architecture:* `io: 2`, `api: 25`, `import: 10`
* *Defense:* `safety: 2`, `doc: 14`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.218
  * `Choke Point (Betweenness):` 0.000119 | `Ripple Effect (Closeness):` 0.012364
  * `Imports (Out-Degree: 7):` java.io.*, java.util.ArrayList, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.exceptions.TestSuiteCouldNotBeReadException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 146.0 | **LOC:** 238 | **CtrlFlow:** 4.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.5109%), Tech Debt (95.5022%)
**Top Internal Functions/Classes:**
  * `setCounts` (Impact: 10.1)
  * `setCurrentTestCaseFailure` (Impact: 1.9)
  * `setCurrentTestCaseErrorMessage` (Impact: 1.9)
  * `setCurrentTestSuiteName` (Impact: 1.8)
  * `setNumberOfAllTests` (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 56`, `args: 43`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 4`
* *Architecture:* `api: 44`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.714
  * `Choke Point (Betweenness):` 2.6e-05 | `Ripple Effect (Closeness):` 0.004451
  * `Imports (Out-Degree: 1):` java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.services.RunInfo
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 143.28 | **LOC:** 226 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (51.224%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `expand` (Impact: 27.9)
  * `findCopyBookNameEndPositionInCopyStatement` (Impact: 14.7)
  * `expandDB2` (Impact: 13.2)
  * `extractCopybookNameFrom` (Impact: 6.6)
  * `extractCopybookNameFromCopyStatement` (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 47`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`
* *Architecture:* `io: 2`, `api: 5`, `import: 16`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.358
  * `Choke Point (Betweenness):` 6.9e-05 | `Ripple Effect (Closeness):` 0.002967
  * `Imports (Out-Degree: 9):` java.io.*, java.nio.file.Files, java.nio.file.Paths, java.util.ArrayList, java.util.Arrays, java.util.List, java.util.StringTokenizer, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/test/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace/ReplaceTest.java` -> Churn: **52.48%** | Cog Load: 77.5515% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 469.6
- `vs-code-extension/client/src/extension.ts` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 426.0
- `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 352.88
- `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 204.72
- `vs-code-extension/client/src/services/TestTree.ts` -> **Thomas Nellemann Kramer** (100.0% isolated ownership) | Magnitude: 179.62

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 0.192** (Bridge: 0.0022 * Flux: 88.5385%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` -> **Severity: 0.034** (Bridge: 0.0003 * Flux: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` -> **Severity: 0.03** (Bridge: 0.0003 * Flux: 99.8854%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/PathHelper.java` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 92.6321%)
- `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 10.383** (Embedded: 0.1285 * Error Risk: 80.7853%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 7.398** (Embedded: 0.1398 * Error Risk: 52.9188%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 7.008** (Embedded: 0.0785 * Error Risk: 89.2869%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/PathHelper.java` -> **Severity: 5.444** (Embedded: 0.0762 * Error Risk: 71.4253%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 5.421** (Embedded: 0.1007 * Error Risk: 53.8495%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java` -> **Severity: 5274.8** (Blast Radius: 52.748 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 3959.5** (Blast Radius: 39.595 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 2808.5** (Blast Radius: 28.085 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 2326.0** (Blast Radius: 23.26 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 933.219** (Blast Radius: 17.109 * Doc Risk: 54.5455%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
