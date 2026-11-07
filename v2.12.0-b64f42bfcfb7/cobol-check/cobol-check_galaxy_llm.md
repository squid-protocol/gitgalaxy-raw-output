# ARCHITECTURAL_BRIEF: cobol-check
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/openmainframeproject/cobol-check.git` |
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
- **Scope:** 288 analyzed artifact(s), 21238 LOC.
- **Load-bearing artifact:** `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -- 45 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` -- pulls in 25 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` at magnitude 1045.12 (structural weight, not risk).
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
| Total Artifacts | 384 |
| Analyzed Artifacts (Scanned) | 288 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 96 |
| Total LOC | 21238 |
| Volatility Index | 0.007 |
| % Scanned of codebase = | 75.0% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4471 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0746 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.2667 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 25 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 143 | 16433 | 49.7% |
| COBOL | 98 | 4213 | 34.0% |
| PLAINTEXT | 16 | 0 | 5.6% |
| MARKDOWN | 10 | 0 | 3.5% |
| BATCH | 7 | 83 | 2.4% |
| SHELL | 6 | 160 | 2.1% |
| YAML | 5 | 87 | 1.7% |
| GROOVY | 2 | 256 | 0.7% |
| JSON | 1 | 6 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 288 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 35%, Declarative / Non-Code 18%, Large Core Modules (3) 12%, Large Core Modules 8%, Interface Declarations Files 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 262 | 91.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 26 | 9.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 96*

**Composition by Extension & Reason:**
- `no_extension`: 16x Unsupported Format (.undeterminable), 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 20x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cut`: 15x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jar`: 3x Excluded (Explicitly Denied Extension: '.jar')
- `.cbl`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.java`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.cmd`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.properties`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.svg`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zip`: 1x Excluded (Explicitly Denied Extension: '.zip')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 95.6 | 16.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 94.9 | 35.6 | 50.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 15.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 4.2 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 12.0 | 3.3 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 63.9 | 0.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 33.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 47.3 | 0.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.1 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 53.4 | 66.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 25 | 11 | 0 | `TESTPRG.CBL` |
| cleanup | 35 | 18 | 0 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| guards | 1044 | 86 | 10 | `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` |
| danger | 582 | 93 | 4 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| concurrency | 23 | 4 | 0 | `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java` |
| connectivity | 1363 | 148 | 12 | `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` |
| io | 231 | 53 | 3 | `gradlew` |
| crypto | 0 | 0 | 0 | - |
| ipc | 80 | 12 | 0 | `src/test/cobol/MOCKTEST/MockCallTest.cut` |
| time | 3 | 1 | 0 | `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/TableEmbedDto.java` |
| serialization | 14 | 6 | 0 | `TESTPRG.CBL` |
| regex | 21 | 12 | 0 | `copybooks/CCHECKPD.CPY` |
| events | 0 | 0 | 0 | - |
| tests | 1326 | 33 | 3 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| docs | 207 | 54 | 2 | `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` |
| debt | 232 | 41 | 2 | `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` |
| mutation | 6357 | 163 | 59 | `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` |
| dead_code | 682 | 86 | 7 | `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 4 | 2 | 0 | `gradlew` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `gradlew` (Hits: 15)
- `src/main/java/org/openmainframeproject/cobolcheck/features/prepareMerge/IO_FileGetter.java` (Hits: 11)
- `testfiles/FILE-MOCK-AFTER.CBL` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **Config.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Config.java`) — 45 inbound connections
2. **Constants.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java`) — 45 inbound connections
3. **Messages.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java`) — 27 inbound connections
4. **PossibleInternalLogicErrorException.java** (`src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java`) — 26 inbound connections
5. **StringHelper.java** (`src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java`) — 26 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **TestSuiteParserParsingTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java`) — 25 outbound dependencies
2. **CopybookExpanderIT.java** (`src/test/java/org/openmainframeproject/cobolcheck/CopybookExpanderIT.java`) — 23 outbound dependencies
3. **MockIT.java** (`src/test/java/org/openmainframeproject/cobolcheck/MockIT.java`) — 22 outbound dependencies
4. **TestSuiteParserCodeInsertionTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserCodeInsertionTest.java`) — 22 outbound dependencies
5. **ExpanderTest.java** (`src/test/java/org/openmainframeproject/cobolcheck/ExpanderTest.java`) — 21 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getParsedTestSuiteLines` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **266.4** | LOC: 547
  * *Intent:* /** * Process the test suite as a series of tokens. When we have processed all the * input, getNextTokenFromTestSuite() * returns a null reference. * ...
- `setFlagsForCurrentLine` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> Impact: **88.7** | LOC: 94
  * *Intent:* /** * Sets flags based on a line, to be able to know which kinds of source * statements to look for when reading and interpreting lines. * * @param li...
- `writeMultiLine` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java`) -> Impact: **45.0** | LOC: 61
  * *Intent:* /** * Lines of test code in a test suite are Cobol-like, but not strictly Cobol. The descriptions for TESTSUITE and * TESTCASE specifications may exce...
- `parseText` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java`) -> Impact: **39.8** | LOC: 69
  * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the constructor of the Formmatter. * @param text Test res...
- `getLinesUntilKeywordHit` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java`) -> Impact: **38.2** | LOC: 49
- `extractTokensFrom` **(Compute Cores)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java`) -> Impact: **36.0** | LOC: 69
- `getKeywordFor` **(Compute Cores)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/Keywords.java`) -> Impact: **31.7** | LOC: 46
- `swapStringsOutWithMappedTokens` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/StringTokenizerExtractor.java`) -> Impact: **30.4** | LOC: 53
  * *Intent:* /** * Swaps out strings in the given line, with tags, so each string will be seen as a single * token, when extracting tokens. Additionally, spaces ar...
- `generateMockPerformCalls` **(Many-Argument Workhorses)** (@ `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/MockGenerator.java`) -> Impact: **26.4** | LOC: 36
  * *Intent:* /**Generates the lines for 'Evaluate when' to perform the correct generated Paragraphs * for a specific identifier. * @param identifier - The identifi...
- `isEndOfStatement` **(Compute Cores)** (@ `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java`) -> Impact: **26.4** | LOC: 43
  * *Intent:* /** * Recognizes end of statement when * (a) - sourceLine ends with a period * (b) - previous line contains just a period * (c) - first token on this ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/test/java/org/openmainframeproject/cobolcheck` | 27 | 2508.32 | 8.03% | 0.0% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser` | 21 | 2387.62 | 34.17% | 49.21% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter` | 8 | 1000.48 | 45.3% | 37.11% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic` | 8 | 765.3 | 19.55% | 5.64% |
| `src/main/java/org/openmainframeproject/cobolcheck/services` | 8 | 677.46 | 18.77% | 2.41% |
| `__monolith__` | 30 | 640.7 | 6.44% | 1.41% |
| `testfiles` | 12 | 634.44 | 43.44% | 48.46% |
| `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects` | 5 | 537.22 | 29.39% | 46.53% |
| `src/main/cobol/copy` | 39 | 455.34 | 0.57% | 10.26% |
| `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/replace` | 6 | 415.24 | 46.15% | 49.39% |

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
- `testfiles/CALL-MOCK-AFTER.CBL` -> **100.0%** Exposure
- `testfiles/FILE-MOCK-AFTER.CBL` -> **100.0%** Exposure
- `testfiles/PARA-MOCK-AFTER.CBL` -> **100.0%** Exposure
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
- **Unknown Dependencies:** `843` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.289)
- **Top Global Matches:** file_cluster_4: 7.289, file_cluster_12: 9.944, file_cluster_5: 10.801
- **Magnitude:** 1045.12 | **LOC:** 1241 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **12**; blast radius 3.106; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (86.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.6%)
- **Documentation Coverage:** 66.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getParsedTestSuiteLines` **(Many-Argument Workhorses)** (Impact: 266.4)
    * *Intent:* /** * Process the test suite as a series of tokens. When we have processed all the * input, getNextT...
  * `getLinesUntilKeywordHit` **(Many-Argument Workhorses)** (Impact: 38.2)
  * `addTestCodeForAssertion` **(Many-Argument Workhorses)** (Impact: 17.7)
  * `getNextTokenFromTestSuite` **(Stateful Encapsulated Methods)** (Impact: 11.5)
    * *Intent:* * we exhaust the list of tokens. * When the file read routine returns a null reference, it means we ...
  * `handleEndOfMockStatement` **(Stateful Encapsulated Methods)** (Impact: 10.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 575
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 197`, `structural_boundaries: 110`, `args: 31`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 247`, `dead_code: 1`, `planned_debt: 1`, `unreferenced_by_name: 8`
* *Architecture:* `api: 15`, `import: 9`
* *Defense:* `safety: 5`, `doc: 14`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.106
  * `Choke Point (Betweenness):` 0.001004 | `Ripple Effect (Closeness):` 0.021777
  * `Imports (Out-Degree: 16):` java.io.BufferedReader, java.io.IOException, java.util.ArrayList, java.util.HashMap, java.util.HashSet, java.util.List, java.util.Locale, java.util.concurrent.TransferQueue...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/MockingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.96)
- **Top Global Matches:** file_cluster_5: 6.96, file_cluster_7: 8.002, file_cluster_12: 8.113
- **Magnitude:** 575.38 | **LOC:** 1163 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 2.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.2%), Complexity Load (formerly Cognitive Load) (59.7%), Connectivity (formerly Api Exposure) (9.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `multiple_mock_perform_evaluates_are_generated_correctly` **(I/O & Config Routines)** (Impact: 5.4)
  * `multiple_mock_sections_gets_generated_correctly` **(I/O & Config Routines)** (Impact: 4.5)
  * `it_generates_lines_for_initialize_mock_count_section_correctly` **(I/O & Config Routines)** (Impact: 4.4)
  * `CALL_MOCK_param_five_is_qualified_six_is_not` **(I/O & Config Routines)** (Impact: 4.0)
  * `single_mock_call_with_args_gets_generated_correctly_with_comment` **(Annotated & Test Methods)** (Impact: 3.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 377
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 146`, `args: 43`, `func_start: 43`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 243`, `unreferenced_by_name: 43`
* *Architecture:* `io: 2`, `api: 42`, `import: 15`
* *Defense:* `test: 131`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` java.io.BufferedReader, java.io.IOException, java.io.Writer, java.util.ArrayList, java.util.Arrays, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.431)
- **Top Global Matches:** file_cluster_12: 7.431, file_cluster_5: 8.137, file_cluster_4: 9.155
- **Magnitude:** 518.22 | **LOC:** 624 | **CtrlFlow:** 26.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **7**; blast radius 6.811; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (74.5%), Complexity Load (formerly Cognitive Load) (63.9%), Connectivity (formerly Api Exposure) (44.9%)
- **Documentation Coverage:** 42.1053% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setFlagsForCurrentLine` **(Many-Argument Workhorses)** (Impact: 88.7)
    * *Intent:* /** * Sets flags based on a line, to be able to know which kinds of source * statements to look for ...
  * `isEndOfStatement` **(Compute Cores)** (Impact: 26.4)
    * *Intent:* /** * Recognizes end of statement when * (a) - sourceLine ends with a period * (b) - previous line c...
  * `shouldLineBeStubbed` **(Compute Cores)** (Impact: 18.5)
    * *Intent:* /** * @param line * @param state * @return true if the source line should be commented out */
  * `getBeginningArea` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* /** * Looks through the prefix-spaces in the source line in order to determine the * beginning area ...
  * `updateCurrentDataStructure` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** * Depending on the line that is being interpreted, we want to make sure that we update * the cur...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 66 instances
* *State Mutation (weighted view):* 207
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 114`, `structural_boundaries: 80`, `args: 32`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 75`
* *Architecture:* `api: 26`, `import: 5`
* *Defense:* `safety: 2`, `doc: 16`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.811
  * `Choke Point (Betweenness):` 0.001096 | `Ripple Effect (Closeness):` 0.043902
  * `Imports (Out-Degree: 7):` java.util.*, java.util.regex.*, org.openmainframeproject.cobolcheck.features.interpreter.Area, org.openmainframeproject.cobolcheck.features.interpreter.State, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.platform.Platform, org.openmainframeproject.cobolcheck.services.platform.PlatformLookup
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/InterpreterControllerTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.095)
- **Top Global Matches:** file_cluster_7: 8.095, file_cluster_5: 8.661, file_cluster_12: 10.081
- **Magnitude:** 448.6 | **LOC:** 1211 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **16**; blast radius 2.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (21.9%), Connectivity (formerly Api Exposure) (11.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `it_parses_file_section_variables_from_split_lines` **(I/O & Config Routines)** (Impact: 20.2)
    * *Intent:* // verify the variables in FILE-SECTION may be split on multiple lines
  * `it_parses_WS_section_variables_from_split_lines` **(Annotated & Test Methods)** (Impact: 8.4)
  * `it_stores_file_section_lines_in_lineRepository` **(Annotated & Test Methods)** (Impact: 7.3)
    * *Intent:* // Test the lines in the DATA DIVISION FILE SECTION are stored in the lineRepository
  * `it_sets_CBL_rules_on_first_line_when_empty` **(Annotated & Test Methods)** (Impact: 6.3)
  * `it_sets_CBL_rules_on_first_line_when_it_is_a_comment` **(Annotated & Test Methods)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 129
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 165`, `args: 65`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 106`, `state_mutation: 55`, `planned_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `io: 2`, `api: 53`, `import: 15`
* *Defense:* `test: 255`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` java.io.BufferedReader, java.io.IOException, java.util.ArrayList, java.util.Arrays, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteParserParsingTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Centroid distance: 7.59)
- **Top Global Matches:** file_cluster_13: 7.59, file_cluster_0: 7.91, file_cluster_12: 8.212
- **Magnitude:** 349.22 | **LOC:** 932 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **25**; blast radius 2.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.3%), Complexity Load (formerly Cognitive Load) (50.8%), Connectivity (formerly Api Exposure) (9.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `it_inserts_start_and_end_tag_as_comments` **(Annotated & Test Methods)** (Impact: 5.3)
  * `it_generates_after_each_branching_paragraphs_correctly_no_comments` **(I/O & Config Routines)** (Impact: 4.5)
  * `it_generates_before_each_paragraph_correctly` **(I/O & Config Routines)** (Impact: 4.2)
  * `it_generates_after_each_paragraph_correctly` **(I/O & Config Routines)** (Impact: 4.2)
  * `it_generates_after_each_branching_paragraphs_correctly_with_comments` **(I/O & Config Routines)** (Impact: 4.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 215`, `args: 49`, `func_start: 41`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 179`, `unreferenced_by_name: 41`
* *Architecture:* `io: 2`, `api: 40`, `import: 23`
* *Defense:* `safety: 1`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` java.io.BufferedReader, java.io.IOException, java.io.StringReader, java.io.Writer, java.util.ArrayList, java.util.List, org.junit.jupiter.api.Assertions.*, org.junit.jupiter.api.BeforeAll...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/InterpreterController.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.097)
- **Top Global Matches:** file_cluster_5: 6.097, file_cluster_12: 7.032, file_cluster_7: 9.495
- **Magnitude:** 340.88 | **LOC:** 659 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 2.977; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (49.4%), Connectivity (formerly Api Exposure) (40.7%)
- **Documentation Coverage:** 83.7209% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `updateLineRepository` **(Stateful Encapsulated Methods)** (Impact: 22.0)
    * *Intent:* /** * Updates the line repository with the given line, if it might have further use when testing. * ...
  * `updateLineRepoByFileStatusToken` **(Stateful Encapsulated Methods)** (Impact: 18.4)
    * *Intent:* /** * If the given line contains a file status token, it will be added to a map to a * corresponding...
  * `updateNumericFields` **(Stateful Encapsulated Methods)** (Impact: 15.6)
    * *Intent:* /** * If the current line is a numeric field, it will be added to the list of numeric fields. * We n...
  * `updateDependencies` **(Stateful Encapsulated Methods)** (Impact: 10.0)
    * *Intent:* /** * Updates dependencies of the interpreter. * The following values can be updated, based on the g...
  * `updatePossibleMock` **(Stateful Encapsulated Methods)** (Impact: 8.6)
    * *Intent:* /** * Updates possibleMockIdentifier, possibleMockType and possibleMockArgs * if a specific part of ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 108`, `args: 50`, `func_start: 51`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 45`, `dead_code: 1`
* *Architecture:* `api: 36`, `import: 12`
* *Defense:* `safety: 10`, `doc: 12`, `immutability_locks: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.977
  * `Choke Point (Betweenness):` 0.000812 | `Ripple Effect (Closeness):` 0.014518
  * `Imports (Out-Degree: 16):` java.io.BufferedReader, java.io.IOException, java.util.*, org.openmainframeproject.cobolcheck.exceptions.CobolSourceCouldNotBeReadException, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.55)
- **Top Global Matches:** file_cluster_0: 9.55, file_cluster_11: 9.602, file_cluster_13: 9.615
- **Magnitude:** 303.38 | **LOC:** 341 | **CtrlFlow:** 1.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.209; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setTestCounts` **(I/O & Config Routines)** (Impact: 5.0)
  * `setCurrentTestCaseFailure` **(Parameter Forwarders)** (Impact: 2.1)
  * `setCurrentTestCaseErrorMessage` **(Parameter Forwarders)** (Impact: 2.1)
  * `setNumberOfAllTests` **(Annotated & Test Methods)** (Impact: 1.6)
  * `setNumberOffAllFailures` **(Annotated & Test Methods)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 71
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 117`, `args: 95`, `func_start: 95`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 65`, `duplicate_logic: 42`, `unreferenced_by_name: 37`
* *Architecture:* `api: 96`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.106893
  * `Imports (Out-Degree: 0):` java.util.ArrayList, java.util.List, javax.xml.bind.annotation.*
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.824)
- **Top Global Matches:** file_cluster_12: 6.824, file_cluster_5: 7.403, file_cluster_7: 9.245
- **Magnitude:** 267.42 | **LOC:** 415 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **14**; blast radius 65.203; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (88.5%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (26.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCharsetForPlatform` **(Compute Cores)** (Impact: 12.1)
  * `getTestResultFormatStyle` **(Compute Cores)** (Impact: 7.8)
  * `setDefaultLocaleOverride` **(Stateful Encapsulated Methods)** (Impact: 6.9)
  * `getTestResultFormat` **(Compute Cores)** (Impact: 6.7)
  * `getCorrectRunContext` **(Stateful Encapsulated Methods)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 92`, `args: 47`, `func_start: 47`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `io: 4`, `api: 81`, `import: 14`
* *Defense:* `safety: 3`, `doc: 1`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 65.203
  * `Choke Point (Betweenness):` 0.007543 | `Ripple Effect (Closeness):` 0.164407
  * `Imports (Out-Degree: 9):` java.io.File, java.io.FileInputStream, java.io.IOException, java.util.ArrayList, java.util.List, java.util.Locale, java.util.Properties, org.openmainframeproject.cobolcheck.exceptions.IOExceptionProcessingConfigFile...
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `TESTPRG.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.619)
- **Top Global Matches:** file_cluster_2: 6.619, file_cluster_11: 6.655, file_cluster_15: 6.977
- **Magnitude:** 224.76 | **LOC:** 470 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); blast radius 18.694; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (63.4%), Complexity Load (formerly Cognitive Load) (55.8%), Debt Markers (formerly Tech Debt) (21.1%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `UT-ASSERT-ACCESSES` **(I/O & Config Routines)** (Impact: 18.1)
  * `UT-LOOKUP-MOCK` **(I/O & Config Routines)** (Impact: 13.9)
  * `2000-SPEAK` **(I/O & Config Routines)** (Impact: 7.8)
  * `UT-SET-MOCK` **(I/O & Config Routines)** (Impact: 6.8)
  * `UT-COMPARE` **(I/O & Config Routines)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 54`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `state_mutation: 72`, `unreferenced_by_name: 5`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.694
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.034843
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/test/java/org/openmainframeproject/cobolcheck/TestSuiteErrorLogTest.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.71)
- **Top Global Matches:** file_cluster_5: 6.71, file_cluster_7: 8.977, file_cluster_12: 9.694
- **Magnitude:** 216.64 | **LOC:** 590 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 2.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (63.9%), Connectivity (formerly Api Exposure) (8.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `it_catches_unexpected_keyword_inside_before_each_block` **(Annotated & Test Methods)** (Impact: 2.4)
  * `it_catches_unexpected_keyword_in_an_expect_context` **(Annotated & Test Methods)** (Impact: 2.4)
  * `it_catches_unexpected_keyword_in_a_mock_context` **(Annotated & Test Methods)** (Impact: 2.3)
  * `it_catches_unexpected_keyword_at_the_end_of_mock_context_with_arguments_and_commas_1` **(Annotated & Test Methods)** (Impact: 2.3)
  * `it_catches_unexpected_keyword_at_the_end_of_mock_context_with_arguments_and_commas_2` **(Annotated & Test Methods)** (Impact: 2.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 119`, `args: 44`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 130`, `unreferenced_by_name: 26`
* *Architecture:* `io: 2`, `api: 24`, `import: 17`
* *Defense:* `test: 69`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` java.io.BufferedReader, java.io.StringReader, java.io.Writer, org.junit.jupiter.api.AfterAll, org.junit.jupiter.api.Assertions.assertEquals, org.junit.jupiter.api.Assertions.assertThrows, org.junit.jupiter.api.BeforeAll, org.junit.jupiter.api.BeforeEach...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/writer/CobolWriter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.176)
- **Top Global Matches:** file_cluster_4: 6.176, file_cluster_15: 10.456, file_cluster_12: 10.567
- **Magnitude:** 198.82 | **LOC:** 254 | **CtrlFlow:** 24.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 4.152; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.6%), Complexity Load (formerly Cognitive Load) (51.0%)
- **Documentation Coverage:** 25.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeMultiLine` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* /** * Lines of test code in a test suite are Cobol-like, but not strictly Cobol. The descriptions fo...
  * `getStringContinuationSign` **(Stateful Encapsulated Methods)** (Impact: 24.1)
  * `writeLine` **(Compute Cores)** (Impact: 7.9)
    * *Intent:* /** * Writes a line of cobol code to the test output file. If the given line is too * long for cobol...
  * `writeLines` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Writes all the given lines of cobol code to the test output file. If any of the lines * are to...
  * `writeCommentedLines` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Comments out and writes all the given lines of cobol code to the test output file. * If the an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 28 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 34`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `io: 3`, `api: 8`, `import: 8`
* *Defense:* `doc: 10`, `immutability_locks: 3`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.152
  * `Choke Point (Betweenness):` 0.000569 | `Ripple Effect (Closeness):` 0.024888
  * `Imports (Out-Degree: 3):` java.io.IOException, java.io.Writer, java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.991)
- **Top Global Matches:** file_cluster_5: 6.991, file_cluster_12: 7.477, file_cluster_7: 7.666
- **Magnitude:** 185.42 | **LOC:** 287 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **4**; blast radius 23.474; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (92.2%), Guard Balance (formerly Safety Score) (67.0%), Complexity Load (formerly Cognitive Load) (23.5%)
- **Documentation Coverage:** 54.5455% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stubLine` **(Compute Cores)** (Impact: 16.8)
  * `ExcludeBetweenTags` **(Many-Argument Workhorses)** (Impact: 13.0)
  * `swapChars` **(Compute Cores)** (Impact: 10.5)
    * *Intent:* /** * Swaps two characters in a given string. * Example: swapChars("1.000.000,00", '.', ',') ~ "1,00...
  * `occursFirst` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* /** * Checks if a character occurs before another * * @param expectedFirst - The char expected to be...
  * `equalsAny` **(Generic / Templated Code)** (Impact: 7.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 48`, `args: 22`, `func_start: 22`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 14`
* *Architecture:* `api: 23`, `import: 4`
* *Defense:* `doc: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.474
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.133905
  * `Imports (Out-Degree: 0):` java.util.Collection, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.services.log.Log
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CobolReader.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 6.191)
- **Top Global Matches:** file_cluster_5: 6.191, file_cluster_12: 7.266, file_cluster_7: 8.047
- **Magnitude:** 180.44 | **LOC:** 305 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.494; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (77.8%)
- **Documentation Coverage:** 62.963% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `appendNextMeaningfulLineToCurrentLine` **(Compute Cores)** (Impact: 11.8)
  * `readTillHitToken` **(Generic / Templated Code)** (Impact: 8.1)
    * *Intent:* /** * Reads lines from the current line, until a specific token is hit. This will forward the reader...
  * `peekNextMeaningfulLine` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* /** * Peeks the next line of the cobol file that is meaningful - that is; a line that is * not empty...
  * `readLine` **(I/O & Config Routines)** (Impact: 4.0)
    * *Intent:* /** * Reads the next line of the cobol file. * * @return (CobolLine) The line that was read * * @thr...
  * `readTillEndOfStatement` **(Generic / Templated Code)** (Impact: 3.9)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.494
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.018339
  * `Imports (Out-Degree: 6):` java.io.*, java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.cobolLogic.CobolLine, org.openmainframeproject.cobolcheck.services.cobolLogic.Interpreter, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/KeywordExtractor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.407)
- **Top Global Matches:** file_cluster_4: 7.407, file_cluster_6: 9.501, file_cluster_16: 12.778
- **Magnitude:** 169.5 | **LOC:** 204 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 4.37; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.8%), Guard Balance (formerly Safety Score) (70.9%), Connectivity (formerly Api Exposure) (6.3%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `extractTokensFrom` **(Compute Cores)** (Impact: 36.0)
  * `handleEndOfWord` **(Stateful Encapsulated Methods)** (Impact: 19.9)
  * `isDecimalPoint` **(Stateful Encapsulated Methods)** (Impact: 7.2)
    * *Intent:* /** * Decimal point is recognized when a period or comma appears between two numeric digits. */
  * `tokenListEndsDuringMultiToken` **(Generic / Templated Code)** (Impact: 4.7)
  * `addTokenAndClearBuffer` **(Encapsulated Accessors)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 23 instances
* *State Mutation (weighted view):* 82
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 28`, `args: 9`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 36`
* *Architecture:* `api: 4`, `import: 3`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.37
  * `Choke Point (Betweenness):` 0.000214 | `Ripple Effect (Closeness):` 0.025602
  * `Imports (Out-Degree: 3):` java.util.*, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.StringHelper, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `gradlew` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 6.421)
- **Top Global Matches:** file_cluster_14: 6.421, file_cluster_7: 9.404, file_cluster_5: 12.775
- **Magnitude:** 164.92 | **LOC:** 168 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (94.9%), Complexity Load (formerly Cognitive Load) (80.7%), Debt Markers (formerly Tech Debt) (21.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `save` **(Interface Declarations)** (Impact: 2.2)
    * *Intent:* # Escape application args
  * `die` **(Parameter Forwarders)** (Impact: 1.7)
  * `warn` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 71`, `args: 5`, `func_start: 3`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 40`, `fragile_debt: 1`
* *Architecture:* `io: 15`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/StringTokenizerExtractor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.11)
- **Top Global Matches:** file_cluster_8: 9.11, file_cluster_6: 10.693, file_cluster_4: 18.585
- **Magnitude:** 154.22 | **LOC:** 169 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **5**; blast radius 6.112; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (79.6%), Complexity Load (formerly Cognitive Load) (57.7%), Connectivity (formerly Api Exposure) (15.7%)
- **Documentation Coverage:** 16.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `swapStringsOutWithMappedTokens` **(Many-Argument Workhorses)** (Impact: 30.4)
    * *Intent:* /** * Swaps out strings in the given line, with tags, so each string will be seen as a single * toke...
  * `extractTokensFrom` **(Generic / Templated Code)** (Impact: 14.7)
    * *Intent:* /** * Extracts tokens meaningful for processing Cobol source code from a Cobol source line. * * Such...
  * `swapMappedTokensOutWithSavedStrings` **(Stateful Encapsulated Methods)** (Impact: 5.5)
  * `StringTokenizerExtractor` **(State Mutators)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 25`, `structural_boundaries: 19`, `args: 4`, `func_start: 4`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 43`
* *Architecture:* `api: 3`, `import: 4`
* *Defense:* `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.112
  * `Choke Point (Betweenness):` 0.000694 | `Ripple Effect (Closeness):` 0.041812
  * `Imports (Out-Degree: 4):` java.util.*, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/Formats/Formatter.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.738)
- **Top Global Matches:** file_cluster_6: 6.738, file_cluster_4: 10.966, file_cluster_8: 15.329
- **Magnitude:** 146.32 | **LOC:** 183 | **CtrlFlow:** 24.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 3.805; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.1%), Complexity Load (formerly Cognitive Load) (68.3%)
- **Documentation Coverage:** 33.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseText` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* /** * Parses text from text results to a data transfer object style. The style is given * in the con...
  * `setTestCaseValues` **(Stateful Encapsulated Methods)** (Impact: 9.7)
  * `instantiateBasedOnStyle` **(Stateful Encapsulated Methods)** (Impact: 9.1)
  * `getFailureType` **(Stateful Encapsulated Methods)** (Impact: 7.8)
  * `Formatter` **(State Mutators)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 1`
* *Risk/State:* `state_mutation: 25`
* *Architecture:* `api: 5`, `import: 10`
* *Defense:* `safety: 2`, `doc: 2`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.805
  * `Choke Point (Betweenness):` 0.000384 | `Ripple Effect (Closeness):` 0.012195
  * `Imports (Out-Degree: 6):` java.text.ParseException, java.util.Arrays, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.features.interpreter.StringTokenizerExtractor, org.openmainframeproject.cobolcheck.features.launcher.Formatter.DataTransferObjects.*, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/DataTransferObject.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Centroid distance: 6.237)
- **Top Global Matches:** file_cluster_11: 6.237, file_cluster_15: 6.882, file_cluster_0: 7.64
- **Magnitude:** 144.0 | **LOC:** 238 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 3.53; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.1%), Debt Markers (formerly Tech Debt) (95.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (62.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setCounts` **(I/O & Config Routines)** (Impact: 8.1)
  * `setCurrentTestCaseFailure` **(Parameter Forwarders)** (Impact: 1.9)
  * `setCurrentTestCaseErrorMessage` **(Parameter Forwarders)** (Impact: 1.9)
  * `setCurrentTestSuiteName` **(Parameter Forwarders)** (Impact: 1.8)
  * `setNumberOfAllTests` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 56`, `args: 43`, `func_start: 43`, `class_start: 4`
* *Risk/State:* `state_mutation: 26`, `duplicate_logic: 4`
* *Architecture:* `api: 44`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.53
  * `Choke Point (Betweenness):` 4.9e-05 | `Ripple Effect (Closeness):` 0.012829
  * `Imports (Out-Degree: 1):` java.util.ArrayList, java.util.List, org.openmainframeproject.cobolcheck.services.RunInfo
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParserController.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.189)
- **Top Global Matches:** file_cluster_5: 7.189, file_cluster_0: 8.521, file_cluster_12: 8.68
- **Magnitude:** 143.64 | **LOC:** 347 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 3.619; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.1%), Connectivity (formerly Api Exposure) (46.0%)
- **Documentation Coverage:** 37.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBoilerplateCodeFromCopybooks` **(Generic / Templated Code)** (Impact: 8.2)
    * *Intent:* /** * Gets the lines from the cobol-check boilerplate copybooks, one for Working-Storage * and one f...
  * `getWorkingStorageTestCode` **(Generic / Templated Code)** (Impact: 3.8)
    * *Intent:* /** * Gets the Working-Storage Section test code to be inserted into the program being generated. * ...
  * `getProcedureDivisionTestCode` **(I/O & Config Routines)** (Impact: 3.7)
    * *Intent:* /** * Gets the PROCEDURE DIVISION test code to be inserted into the program being generated. * * @re...
  * `concatenateTestSuites` **(Parameter Forwarders)** (Impact: 3.2)
    * *Intent:* /** * Each testsuite might be in its own file. This method combines all the testsuites, pertaining t...
  * `generateCobolLinesForUnmockedCalls` **(I/O & Config Routines)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 68`, `args: 24`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 54`
* *Architecture:* `io: 2`, `api: 25`, `import: 10`
* *Defense:* `safety: 2`, `doc: 14`, `immutability_locks: 6`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.619
  * `Choke Point (Betweenness):` 0.00181 | `Ripple Effect (Closeness):` 0.021341
  * `Imports (Out-Degree: 16):` java.io.*, java.util.ArrayList, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.exceptions.TestSuiteCouldNotBeReadException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/interpreter/CopybookExpander.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.072)
- **Top Global Matches:** file_cluster_5: 7.072, file_cluster_12: 7.345, file_cluster_16: 9.981
- **Magnitude:** 137.28 | **LOC:** 226 | **CtrlFlow:** 18.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **17**; blast radius 3.249; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (65.9%), Complexity Load (formerly Cognitive Load) (49.6%), Connectivity (formerly Api Exposure) (18.8%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expand` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `findCopyBookNameEndPositionInCopyStatement` **(Compute Cores)** (Impact: 14.7)
  * `expandDB2` **(Defensive Guards)** (Impact: 13.2)
  * `extractCopybookNameFrom` **(Stateful Encapsulated Methods)** (Impact: 6.6)
  * `extractCopybookNameFromCopyStatement` **(Compute Cores)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 47`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 20`
* *Architecture:* `io: 4`, `api: 5`, `import: 16`
* *Defense:* `safety: 2`, `doc: 3`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.249
  * `Choke Point (Betweenness):` 0.000448 | `Ripple Effect (Closeness):` 0.01344
  * `Imports (Out-Degree: 10):` java.io.*, java.nio.file.Files, java.nio.file.Paths, java.util.ArrayList, java.util.Arrays, java.util.List, java.util.StringTokenizer, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/features/argumentHandler/ArgumentHandler.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.05)
- **Top Global Matches:** file_cluster_12: 7.05, file_cluster_5: 8.553, file_cluster_16: 9.192
- **Magnitude:** 137.1 | **LOC:** 200 | **CtrlFlow:** 18.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 3.1; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (70.5%), Complexity Load (formerly Cognitive Load) (60.7%), Connectivity (formerly Api Exposure) (24.5%)
- **Documentation Coverage:** 76.9231% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `processCommandLineArgumentArray` **(Stateful Encapsulated Methods)** (Impact: 19.3)
  * `storeOptionSettings` **(Stateful Encapsulated Methods)** (Impact: 12.9)
    * *Intent:* /** * Convert an option specification string into a map of option keys and values. * * @param option...
  * `loadArgProgramPaths` **(I/O & Config Routines)** (Impact: 7.0)
  * `lookupOption` **(Encapsulated Accessors)** (Impact: 4.6)
  * `isKey` **(Encapsulated Accessors)** (Impact: 4.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 37`, `args: 9`, `func_start: 9`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 24`
* *Architecture:* `api: 10`, `import: 11`
* *Defense:* `doc: 3`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.1
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.007964
  * `Imports (Out-Degree: 6):` java.util.Arrays, java.util.HashMap, java.util.List, java.util.Map, org.openmainframeproject.cobolcheck.exceptions.CommandLineArgumentException, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Centroid distance: 8.973)
- **Top Global Matches:** file_cluster_16: 8.973, file_cluster_17: 9.119, file_cluster_2: 9.662
- **Magnitude:** 128.88 | **LOC:** 165 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **45** in-repo importer(s); it depends on **3**; blast radius 38.36; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (50.3%), Debt Markers (formerly Tech Debt) (10.7%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Constants` **(Encapsulated Accessors)** (Impact: 1.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 6`, `args: 2`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `state_mutation: 1`, `planned_debt: 1`
* *Architecture:* `api: 124`, `import: 3`
* *Defense:* `immutability_locks: 124`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 38.36
  * `Choke Point (Betweenness):` 0.002061 | `Ripple Effect (Closeness):` 0.166691
  * `Imports (Out-Degree: 2):` java.util.Arrays, java.util.List, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException
  * `Imported By (In-Degree: 45):` (Excluded from Brief to save tokens)

### `testfiles/FILE-MOCK-AFTER.CBL` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.35)
- **Top Global Matches:** file_cluster_2: 5.35, file_cluster_15: 6.677, file_cluster_11: 6.994
- **Magnitude:** 128.44 | **LOC:** 218 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.06; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (73.1%), Complexity Load (formerly Cognitive Load) (53.8%), Debt Markers (formerly Tech Debt) (19.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `FILEDEMO` **(I/O & Config Routines)** (Impact: 7.9)
  * `0100-OPEN-INPUT` **(I/O & Config Routines)** (Impact: 5.1)
  * `0200-READ-INPUT-FILE` **(I/O & Config Routines)** (Impact: 5.1)
  * `UT-INITIALIZE` **(I/O & Config Routines)** (Impact: 1.2)
  * `UT-END` **(I/O & Config Routines)** (Impact: 1.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 43`, `func_start: 7`, `class_start: 1`
* *Risk/State:* `state_mutation: 73`, `unreferenced_by_name: 2`
* *Architecture:* `io: 10`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.06
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ZUTZCPD, ZUTZCWS
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteErrorLog.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.638)
- **Top Global Matches:** file_cluster_12: 6.638, file_cluster_5: 7.288, file_cluster_7: 9.212
- **Magnitude:** 123.86 | **LOC:** 223 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 2.612; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (90.8%), Guard Balance (formerly Safety Score) (62.8%), Complexity Load (formerly Cognitive Load) (37.4%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkExpectedTokenSyntax` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `checkSyntaxInsideBlock` **(Many-Argument Workhorses)** (Impact: 10.7)
  * `logIdenticalMocks` **(Compute Cores)** (Impact: 4.9)
  * `logUnusedMocks` **(Generic / Templated Code)** (Impact: 4.9)
  * `getTestSuiteParserErrorLogPath` **(Stateful Encapsulated Methods)** (Impact: 4.7)
    * *Intent:* /** * Gets the path for the TestSuite Parser error log */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 51
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 32`, `args: 14`, `func_start: 14`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 35`, `unreferenced_by_name: 9`
* *Architecture:* `io: 7`, `api: 12`, `import: 10`
* *Defense:* `safety: 7`, `doc: 2`, `immutability_locks: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.612
  * `Choke Point (Betweenness):` 0.000452 | `Ripple Effect (Closeness):` 0.02108
  * `Imports (Out-Degree: 11):` java.io.*, java.util.Arrays, java.util.List, java.util.Locale, org.openmainframeproject.cobolcheck.services.Config, org.openmainframeproject.cobolcheck.services.Constants, org.openmainframeproject.cobolcheck.services.Messages, org.openmainframeproject.cobolcheck.services.cobolLogic.TokenExtractor...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/main/java/org/openmainframeproject/cobolcheck/workers/Generator.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.715)
- **Top Global Matches:** file_cluster_12: 6.715, file_cluster_16: 8.475, file_cluster_5: 8.633
- **Magnitude:** 122.7 | **LOC:** 285 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **20**; blast radius 3.013; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.2%), Complexity Load (formerly Cognitive Load) (26.6%)
- **Documentation Coverage:** 42.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeToSource` **(Stateful Encapsulated Methods)** (Impact: 18.5)
    * *Intent:* /** * Writes the given line to the output file. If a multiline statement has been read, this will * ...
  * `processingAfterEchoingSourceLineToOutput` **(I/O & Config Routines)** (Impact: 14.9)
    * *Intent:* /** * Perform appropriate processing after echoing (or skipping) the current source line from the pr...
  * `tryInsertEndEvaluateAtMockedCompomentEnd` **(Stateful Encapsulated Methods)** (Impact: 7.9)
  * `prepareAndRunMerge` **(Compute Cores)** (Impact: 6.9)
    * *Intent:* /** * Finds any test-directory that matches the given program name. For each of these directories, a...
  * `echoingSourceLineToOutput` **(Stateful Encapsulated Methods)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 12 instances
* *State Mutation (weighted view):* 45
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 49`, `args: 11`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 21`
* *Architecture:* `io: 9`, `api: 4`, `import: 20`
* *Defense:* `safety: 6`, `doc: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.013
  * `Choke Point (Betweenness):` 0.000967 | `Ripple Effect (Closeness):` 0.010453
  * `Imports (Out-Degree: 13):` java.io.BufferedReader, java.io.File, java.io.IOException, java.io.Reader, java.io.Writer, java.util.List, org.openmainframeproject.cobolcheck.exceptions.CobolSourceCouldNotBeReadException, org.openmainframeproject.cobolcheck.exceptions.PossibleInternalLogicErrorException...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` (JAVA) | Magnitude: 303.38 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 231, structural_boundaries: 117, api: 96, args: 95

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/TableDocumentDto.java` (JAVA) | Magnitude: 8.14 | Delta: **0.051** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 83, structural_boundaries: 7, core_var_decl: 4, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `insert_notice.sh` (SHELL) | Magnitude: 14.58 | Delta: **0.059** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 15, io: 6, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` (JAVA) | Magnitude: 128.88 | Delta: **0.146** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 128, globals: 125, api: 124, immutability_locks: 124

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `TESTPRG.CBL` (COBOL) | Magnitude: 224.76 | Delta: **0.036** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 423, state_mutation: 72, branch: 58, structural_boundaries: 54

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/test/java/org/openmainframeproject/cobolcheck/StringHelperTest.java` (JAVA) | Magnitude: 57.78 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 123, test: 48, structural_boundaries: 31, api: 25
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/ContextHandler.java` (JAVA) | Magnitude: 39.22 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 38, structural_boundaries: 16, state_mutation: 8, api: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 0.668** (Bridge: 0.0075 * Flux: 88.5385%)
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParserController.java` -> **Severity: 0.181** (Bridge: 0.0018 * Flux: 99.9937%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/filehelpers/PathHelper.java` -> **Severity: 0.125** (Bridge: 0.0013 * Flux: 92.6321%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/cobolLogic/Interpreter.java` -> **Severity: 0.11** (Bridge: 0.0011 * Flux: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/features/testSuiteParser/TestSuiteParser.java` -> **Severity: 0.1** (Bridge: 0.001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 10.151** (Embedded: 0.1644 * Error Risk: 61.7442%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 8.968** (Embedded: 0.1339 * Error Risk: 66.9693%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 8.432** (Embedded: 0.1644 * Error Risk: 51.2854%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 8.389** (Embedded: 0.1667 * Error Risk: 50.3247%)
- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/Formatter/DataTransferObjects/JUnitDto.java` -> **Severity: 6.73** (Embedded: 0.1069 * Error Risk: 62.9592%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/main/java/org/openmainframeproject/cobolcheck/services/Config.java` -> **Severity: 6520.3** (Blast Radius: 65.203 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Messages.java` -> **Severity: 4609.8** (Blast Radius: 46.098 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/Constants.java` -> **Severity: 3836.0** (Blast Radius: 38.36 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/exceptions/PossibleInternalLogicErrorException.java` -> **Severity: 3634.6** (Blast Radius: 36.346 * Doc Risk: 100.0%)
- `src/main/java/org/openmainframeproject/cobolcheck/services/StringHelper.java` -> **Severity: 1280.401** (Blast Radius: 23.474 * Doc Risk: 54.5455%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `91` files carry mainframe facts -- `44` call sites, `8` dataset bindings, `618` record items.

- **DB2 schemas:** `7` columns of `EXEC SQL DECLARE ... TABLE` (inline or DCLGEN members), full shape in `sql_table_data`.

- **DB2 table access:** `5` embedded SQL statements touching `1` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

### `src/test/cobol/NUMBERS/SymbolicRelationsTest.cut` (COBOL)
- **Data moves:** 216 (MOVE 216)

### `TESTPRG.CBL` (COBOL)
- **Record layouts (109 items):** `UT-MOCKS (45)`, `UT-FIELDS (38)`, `FILLER (13)`, `UT-FILES (11)`, `FILLER (1)`, `FILLER (1)`
- **Data moves:** 65 (ACCEPT 1, ADD 10, MOVE 32, STRING 22); most-fed items `UT-DISPLAY-MESSAGE`, `UT-TEST-CASE-NUMBER`, `UT-ACTUAL`, `RETURN-CODE`, `UT-ACTUAL-ACCESSES-FMT`, `UT-EXPECTED-ACCESSES-FMT`

### `src/test/cobol/MOCKTEST/BeforeAfterTest.cut` (COBOL)
- **Data moves:** 137 (MOVE 137)

### `src/test/cobol/MOCKTEST/MockCallTest.cut` (COBOL)
- **Calls:** `CALL PROG1`, `CALL VALUE-2`, `CALL PROG3`, `CALL PROGRAM`, `CALL PROGRAM2`, `CALL MYCOBOL`
- **Data moves:** 57 (MOVE 57)

### `src/test/cobol/ALPHA/AlphaExpectationsTest.cut` (COBOL)
- **Data moves:** 67 (MOVE 67)

### `testfiles/FILE-MOCK-AFTER.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(declared)`, `OUTPUT-FILENAME(declared)`
- **Record layouts (9 items):** `WS-FILE-STATUS (4)`, `WS-RECORD-AREAS (3)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`
- **Data moves:** 53 (ADD 7, MOVE 46); most-fed items `UT-ACTUAL`, `INPUT-RECORD`, `WS-INPUT-FILE-STATUS`, `UT-ACTUAL-ACCESSES`

### `testfiles/PARA-MOCK-AFTER.CBL` (COBOL)
- **Datasets:** `INPUT-FILENAME(INPUT)`, `OUTPUT-FILENAME(declared)`
- **Record layouts (12 items):** `WS-FILE-STATUS (4)`, `WS-RECORD-AREAS (3)`, `WS-TEST-AREAS (3)`, `INPUT-RECORD⟵INPUT-FILE (1)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`
- **Data moves:** 36 (ADD 8, MOVE 28); most-fed items `UT-ACTUAL`, `UT-ACTUAL-ACCESSES`

### `src/main/cobol/MOCK.CBL` (COBOL)
- **Calls:** `CALL PROG1`, `CALL MYCOBOL`, `CALL VALUE-2`, `CALL PROG3`
- **Record layouts (9 items):** `FILLER (5)`, `COBOL-STRUCTURE (4)`
- **Data moves:** 28 (MOVE 28); most-fed items `VALUE-1`, `TEMP`, `VALUE-2`

### `testfiles/CALL-MOCK-AFTER.CBL` (COBOL)
- **Record layouts (3 items):** `WS-ALPHA (1)`, `WS-OMEGA (1)`, `WS-SUBPROGRAM-NAME (1)`
- **Data moves:** 42 (ADD 8, MOVE 34); most-fed items `UT-ACTUAL`, `UT-ACTUAL-ACCESSES`

### `src/test/cobol/FDTEST/FDTEST01.CUT` (COBOL)
- **Data moves:** 43 (MOVE 43)

### `src/main/cobol/WS88LEVEL.CBL` (COBOL)
- **Datasets:** `LINEFILE(OUTPUT)`
- **Record layouts (30 items):** `LINIE1⟵LINEFILE (13)`, `WS-88-LEVELS (6)`, `WS-88-LEVELS-NUMERIC (6)`, `WORK-FIELDS (2)`, `STATUS-LINEFILE (1)`, `WS-OMEGA (1)`, `WS-SUBPROGRAM-NAME (1)`
- **Special names:** `DECIMAL-POINT IS COMMA`
- **Data moves:** 2 (MOVE 2)

### `testfiles/INVDATE-AFTER.CBL` (COBOL)
- **Record layouts (3 items):** `WS-NEXT-INVOICE-DATE (1)`, `WS-QUOTIENT (1)`, `WS-REMAINDER (1)`
- **Data moves:** 30 (ADD 4, DIVIDE 4, MOVE 22); most-fed items `UT-ACTUAL`, `WS-NEXT-INVOICE-DATE`, `WS-QUOTIENT`, `WS-REMAINDER`

### `copybooks/DFHEIBLK.CPY` (COBOL)
- **Record layouts (32 items):** `DFHEIBLK (32)`

### `src/main/cobol/FileCopy.cbl` (COBOL)
- **Datasets:** `INFILE(INPUT)`
- **Record layouts (15 items):** `FILLER (10)`, `INPUT-RECORD⟵INPUT-FILE (4)`, `OUTPUT-RECORD⟵OUTPUT-FILE (1)`
- **Data moves:** 14 (ADD 1, MOVE 7, STRING 6); most-fed items `WS-ERROR-MESSAGE`, `OUT-FIELD-1`, `OUT-FIELD-2`, `WS-COUNT-FORMATTED`

### `src/main/resources/org/openmainframeproject/cobolcheck/copybooks/DFHEIBLK.CPY` (COBOL)
- **Record layouts (32 items):** `DFHEIBLK (32)`

### `testfiles/CICDEMO-AFTER.CBL` (COBOL)
- **Record layouts (6 items):** `WS-RECORD (5)`, `DFHCOMMAREA (1)`
- **Data moves:** 25 (ADD 6, MOVE 19); most-fed items `UT-ACTUAL-NUMERIC`, `UT-ACTUAL`, `UT-ACTUAL-ACCESSES`

### `testfiles/CONVERT-TEST-AFTER.CBL` (COBOL)
- **Datasets:** `EXPECTED-RESULT-FILENAME(INPUT)`, `ACTUAL-RESULT-FILENAME(INPUT)`
- **Record layouts (16 items):** `ARG-VALUES (3)`, `TEST-STATUS (3)`, `EOF-EXPECTED (2)`, `EOF-ACTUAL (2)`, `EXPECTED-RESULT-RECORD⟵EXPECTED-RESULT-FILE (1)`, `ACTUAL-RESULT-RECORD⟵ACTUAL-RESULT-FILE (1)`, `ARGS (1)`, `EXPECTED-LINE-NUMBER (1)`, `ACTUAL-LINE-NUMBER (1)`, `STATUS-MESSAGE (1)`
- **Data moves:** 8 (ACCEPT 1, ADD 2, MOVE 3, UNSTRING 2); most-fed items `ACTUAL-RESULT-FILENAME`, `EXPECTED-RESULT-FILENAME`

### `src/test/cobol/MOCKTEST/MockSectionsAndParagraphsTest.cut` (COBOL)
- **Data moves:** 27 (MOVE 27)

### `testfiles/REPLACE.CBL` (COBOL)
- **Record layouts (11 items):** `WS-OMEGA (1)`, `WS-GAMMA (1)`, `UT-OMEGA (1)`, `UT-GAMMA (1)`, `WS-SUBPROGRAM-NAME (1)`, `UT-COMPARE-DEFAULT (1)`, `UT-NORMAL-COMPARE (1)`, `UT-ACTUAL (1)`, `UT-EXPECTED (1)`, `UT-TEST-CASE-COUNT (1)`, `UT-TEST-CASE-COUNT (1)`
- **Data moves:** 16 (ADD 1, MOVE 15); most-fed items `UT-ACTUAL`

### `testfiles/REPLACE2.CBL` (COBOL)
- **Record layouts (11 items):** `WS-OMEGA (1)`, `WS-GAMMA (1)`, `UT-OMEGA (1)`, `UT-GAMMA (1)`, `WS-SUBPROGRAM-NAME (1)`, `UT-COMPARE-DEFAULT (1)`, `UT-NORMAL-COMPARE (1)`, `UT-ACTUAL (1)`, `UT-EXPECTED (1)`, `UT-TEST-CASE-COUNT (1)`, `UT-TEST-CASE-COUNT (1)`
- **Data moves:** 16 (ADD 2, MOVE 14); most-fed items `UT-ACTUAL`

*(+71 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 23% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: application programs (source or load-module list) (38 gaps); JCL and PROC libraries (26 gaps); CSD extract (DFHCSDUP LIST / CICSPlex SM), or the web / API layer that LINKs it (1 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 139 literal sites + 1 sites through wrappers = 140

- `writeOutPutToConsole` (function, debug_prints, primitive): 1 call sites in 1 files -- `src/main/java/org/openmainframeproject/cobolcheck/features/launcher/ProcessOutputWriter.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4828 call pairs -- scoped 40.7%, unique 1.9%, ambiguous 13.0%, external 44.4%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 4687 | 40.3% | 1.4% | 13.3% | 45.0% |
| cobol | 110 | 68.2% | 24.5% | 0.0% | 7.3% |
| groovy | 17 | 0.0% | 0.0% | 11.8% | 88.2% |
| shell | 14 | 14.3% | 0.0% | 0.0% | 85.7% |

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
