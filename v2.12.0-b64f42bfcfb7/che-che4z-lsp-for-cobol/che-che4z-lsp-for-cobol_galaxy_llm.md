# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/eclipse/che-che4z-lsp-for-cobol.git` |
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
- **Scope:** 2528 analyzed artifact(s), 214100 LOC.
- **Load-bearing artifact:** `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` -- 579 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `server/engine/src/main/java/org/eclipse/lsp/cobol/cli/di/CliModule.java` -- pulls in 63 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `clients/cobol-lsp-vscode-extension/.npmrc` at magnitude 5000.0 (structural weight, not risk).
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
| Total Artifacts | 3535 |
| Analyzed Artifacts (Scanned) | 2528 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 1007 |
| Total LOC | 214100 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 71.5% |
| Dominant Lang | JAVA |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6743 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2521 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 5.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 4.2821 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 97 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 1570 | 119516 | 62.1% |
| COBOL | 366 | 34785 | 14.5% |
| JSON | 283 | 35866 | 11.2% |
| TYPESCRIPT | 195 | 22284 | 7.7% |
| PLAINTEXT | 33 | 2 | 1.3% |
| MARKDOWN | 31 | 0 | 1.2% |
| XML | 25 | 0 | 1.0% |
| JAVASCRIPT | 15 | 409 | 0.6% |
| YAML | 6 | 627 | 0.2% |
| SHELL | 3 | 49 | 0.1% |
| BMS | 1 | 562 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 2526 |
| unknown | unknown | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 29%, Data / Markup / Trivial 20%, Encapsulated Accessors Files 10%, Interface Declarations Files 8%, Large Core Modules (3) 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 2464 | 97.5% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 62 | 2.5% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 1007*

**Composition by Extension & Reason:**
- `.cbl`: 701x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.dot`: 118x Unsupported Format (.dot), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `no_extension`: 77x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 11x Unsupported Format (.undeterminable), 1x Unsupported Format (.configurator)
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3867 LOC), 1x Excluded (Massive Static Asset Blob: 4112 LOC)
- `.g4`: 24x Unsupported Format (.g4)
- `.gif`: 8x Excluded (Explicitly Denied Extension: '.gif')
- `.cpy`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.2`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.copy`: 3x Excluded (Unsupported Extension: '.COPY')
- `.original`: 2x Unsupported Format (.original)
- `.txt`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 5.2 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 86.6 | 22.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.4 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 9.9 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 6.0 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 62.0 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1074 | 190 | 0 | `tests/test_files/cicsGenApp/copybooks/ssmap.cpy` |
| cleanup | 111 | 41 | 0 | `tests/test_files/cicsGenApp/positive/lgsetup.cbl` |
| guards | 13122 | 1487 | 13 | `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSysSetStatement.java` |
| danger | 2788 | 660 | 3 | `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` |
| concurrency | 2305 | 231 | 0 | `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.test.ts` |
| connectivity | 4755 | 1213 | 5 | `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` |
| io | 1170 | 192 | 0 | `tests/test_files/cicsGenApp/positive/lgsetup.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 376 | 79 | 0 | `tests/test_files/cicsGenApp/positive/lgipdb01.cbl` |
| time | 101 | 54 | 0 | `server/engine/src/test/resources/CM101M.CBL` |
| serialization | 175 | 59 | 0 | `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` |
| regex | 223 | 81 | 0 | `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` |
| events | 257 | 179 | 0 | `clients/cobol-lsp-vscode-extension/src/services/util/TarUtil.ts` |
| tests | 6973 | 901 | 6 | `server/common/src/test/java/org/eclipse/lsp/cobol/common/mapping/ExtendedTextTest.java` |
| docs | 2941 | 1621 | 2 | `clients/analysis/src/vm/vm.ts` |
| debt | 952 | 271 | 1 | `tests/test_files/cicsGenApp/positive/lgwebst5.cbl` |
| mutation | 22687 | 1701 | 21 | `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` |
| dead_code | 3435 | 812 | 3 | `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSysSetStatement.java` |
| credential | 29 | 10 | 0 | `clients/analysis/src/__tests__/__resources__/cfgraph/case121.cfast.json` |
| threat | 2 | 2 | 0 | `clients/cobol-lsp-vscode-extension/src/services/reporter/index.ts` |
| ml_ai | 33 | 17 | 0 | `clients/cobol-lsp-vscode-extension/src/commands/SmartTabCommand.ts` |
| ui | 388 | 29 | 0 | `tests/test_files/cicsGenApp/copybooks/ssmap.bms` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_files/cicsGenApp/positive/lgsetup.cbl` (Hits: 81)
- `tests/test_files/cicsGenApp/positive/lgwebst5.cbl` (Hits: 45)
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/LocalFilesystemResourceService.spec.ts` (Hits: 41)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **UseCaseEngine.java** (`server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java`) — 579 inbound connections
2. **ErrorSource.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java`) — 398 inbound connections
3. **SyntaxError.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java`) — 213 inbound connections
4. **Locality.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/model/Locality.java`) — 188 inbound connections
5. **ErrorSeverity.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSeverity.java`) — 174 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CliModule.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/cli/di/CliModule.java`) — 63 outbound dependencies
2. **CobolLanguageServerTest.java** (`server/engine/src/test/java/org/eclipse/lsp/cobol/service/CobolLanguageServerTest.java`) — 60 outbound dependencies
3. **TestModule.java** (`server/engine/src/test/java/org/eclipse/lsp/cobol/TestModule.java`) — 58 outbound dependencies
4. **CICSVisitor.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSVisitor.java`) — 49 outbound dependencies
5. **ServiceModule.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/domain/modules/ServiceModule.java`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `checkOptions` **(Many-Argument Workhorses)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`) -> Impact: **254.6** | LOC: 707
  * *Intent:* /** * Entrypoint to check CICS SP Inquire rule options * * @param ctx ParserRuleContext subclass containing options * @param <E> A subclass of ParserR...
- `traverse` **(Defensive Guards)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java`) -> Impact: **146.4** | LOC: 191
- `1100-RECEIVE-MAP` **(I/O & Config Routines)** (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> Impact: **117.3** | LOC: 387
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> Impact: **116.5** | LOC: 451
- `checkOptions` **(Compute Cores)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSysSetOptionsCheckUtility.java`) -> Impact: **107.8** | LOC: 205
  * *Intent:* /** * Entrypoint to check CICS SET ASSOCIATION USERCORRDATA rules for required and invalid options * * @param ctx ParserRuleContext subclass containin...
- `addInstructionsForNode` **(Compute Cores)** (@ `clients/analysis/src/vm/listing.ts`) -> Impact: **73.2** | LOC: 247
- `VALIDATE-INPUT-DATA-FIELDS` **(I/O & Config Routines)** (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN02C.cbl`) -> Impact: **56.1** | LOC: 203
  * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *-----------------------------------------------------...
- `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDUPC.cbl`) -> Impact: **47.5** | LOC: 151
- `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/CORPT00C.cbl`) -> Impact: **41.5** | LOC: 249
  * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *--------------------------------------------------------------...
- `processLine` **(Many-Argument Workhorses)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/formations/CapitalFormation.java`) -> Impact: **39.9** | LOC: 77

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/test_files/aws-mainframe-modernization-carddemo/positive` | 26 | 10121.78 | 38.24% | 0.0% |
| `clients/cobol-lsp-vscode-extension` | 10 | 10120.3 | 1.42% | 0.0% |
| `clients/analysis/src/__tests__/__resources__/cfgraph` | 321 | 4532.36 | 1.69% | 14.6% |
| `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases` | 404 | 4173.36 | 0.15% | 0.0% |
| `clients/cobol-lsp-vscode-extension/src/test/suite` | 15 | 4043.52 | 43.23% | 0.0% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility` | 109 | 3501.14 | 4.85% | 27.93% |
| `tests/test_files/cicsGenApp/positive` | 31 | 3412.02 | 41.43% | 0.0% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors` | 39 | 1715.76 | 9.77% | 32.55% |
| `clients/cobol-lsp-vscode-extension/src/__tests__/services` | 8 | 1439.41 | 52.13% | 9.19% |
| `clients/cobol-lsp-vscode-extension/src/services` | 10 | 1332.81 | 33.5% | 6.13% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `clients/cobol-lsp-vscode-extension/src/type/zoweApi.d.ts` -> **100.0%** Exposure
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/semantics/GroupContext.java` -> **99.9994%** Exposure
- `server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/IdmsVisitor.java` -> **99.9977%** Exposure
- `server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/MessageServiceParser.java` -> **99.9788%** Exposure
- `server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/DaCoVisitor.java` -> **99.9729%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `clients/analysis/src/vm/utils.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/FSUtils.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/Memoize.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/SubroutineUtils.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/TarUtil.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSysSetStatement.java` -> **127** Orphaned Functions | **0** Duplicates
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSendStatement.java` -> **84** Orphaned Functions | **0** Duplicates
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSIssue.java` -> **66** Orphaned Functions | **0** Duplicates
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsReceive.java` -> **56** Orphaned Functions | **0** Duplicates
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSInquireSP.java` -> **49** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
- `tests/test_files/cicsGenApp/positive/lgacdb02.cbl` -> **99.9618%** Exposure
- `tests/test_files/cicsGenApp/positive/lgacdb01.cbl` -> **98.86%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14467` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `clients/cobol-lsp-vscode-extension/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/telemetry.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 2.597)
- **Top Global Matches:** file_cluster_2: 2.597, file_cluster_17: 5.167, file_cluster_13: 6.436
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** None above 0%
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.698)
- **Top Global Matches:** file_cluster_4: 8.698, file_cluster_12: 8.78, file_cluster_11: 10.161
- **Magnitude:** 2166.24 | **LOC:** 4245 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.9%), Complexity Load (formerly Cognitive Load) (45.9%), Dead Code Surface (formerly Dead Code) (5.8%), Connectivity (formerly Api Exposure) (1.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` **(I/O & Config Routines)** (Impact: 117.3)
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 116.5)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.4)
  * `1200-EDIT-MAP-INPUTS` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 384 instances
* *State Mutation (weighted view):* 1468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 155`, `func_start: 85`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 700`, `dead_code: 10`, `unreferenced_by_name: 4`
* *Architecture:* `io: 11`, `api: 1`, `import: 56`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` COACTUP, COCOM01Y, COTTL01Y, CSDAT01Y, CSLKPCDY, CSMSG01Y, CSMSG02Y, CSSETATY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.xmlparse.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 7.737)
- **Top Global Matches:** file_cluster_7: 7.737, file_cluster_12: 8.28, file_cluster_10: 9.822
- **Magnitude:** 1093.84 | **LOC:** 246 | **CtrlFlow:** 6.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (54.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 8 instances
* *Concurrency (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 89`, `args: 39`, `func_start: 13`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 8`
* *Architecture:* `concurrency: 59`, `import: 3`
* *Defense:* `test: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` testHelper, assert, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` (JAVA | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.556)
- **Top Global Matches:** file_cluster_5: 7.556, file_cluster_7: 10.922, file_cluster_12: 11.068
- **Magnitude:** 884.12 | **LOC:** 2280 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **46**; blast radius 0.191; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (73.0%), Mutation Surface (formerly State Flux) (61.2%), Connectivity (formerly Api Exposure) (50.3%)
- **Documentation Coverage:** 98.6928% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `validateJavaDirectives` **(Compute Cores)** (Impact: 28.1)
  * `getValidShareableRanges` **(Compute Cores)** (Impact: 23.1)
  * `getCompilerLineTokenType` **(Compute Cores)** (Impact: 13.8)
  * `visitJsonParse` **(Callbacks & Closures)** (Impact: 12.3)
  * `visitJsonGenerate` **(Callbacks & Closures)** (Impact: 10.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 161
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 129`, `structural_boundaries: 480`, `args: 435`, `func_start: 176`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 83`, `planned_debt: 2`
* *Architecture:* `api: 140`, `import: 36`
* *Defense:* `safety: 14`, `doc: 5`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.191
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.000528
  * `Imports (Out-Degree: 25):` com.google.common.collect.ImmutableList, java.util.*, java.util.Collections.emptyList, java.util.Optional.ofNullable, java.util.function.Function, java.util.regex.Matcher, java.util.regex.Pattern, java.util.stream.Collectors...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.075)
- **Top Global Matches:** file_cluster_4: 8.075, file_cluster_12: 9.6, file_cluster_11: 11.187
- **Magnitude:** 800.58 | **LOC:** 1561 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (71.6%), Complexity Load (formerly Cognitive Load) (45.7%), Dead Code Surface (formerly Dead Code) (5.6%), Connectivity (formerly Api Exposure) (1.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 47.5)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 29.9)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `1100-RECEIVE-MAP` **(I/O & Config Routines)** (Impact: 15.9)
  * `3200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 14.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 509
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 66`, `func_start: 45`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 22`, `state_mutation: 283`, `dead_code: 3`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 13`
* *Defense:* `safety: 7`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` COCOM01Y, COCRDUP, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDLIC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.912)
- **Top Global Matches:** file_cluster_4: 7.912, file_cluster_6: 10.431, file_cluster_12: 12.105
- **Magnitude:** 719.06 | **LOC:** 1460 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.6%), Complexity Load (formerly Cognitive Load) (46.0%), Dead Code Surface (formerly Dead Code) (7.1%), Connectivity (formerly Api Exposure) (1.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 38.2)
  * `9000-READ-FORWARD` **(I/O & Config Routines)** (Impact: 28.9)
  * `1250-SETUP-ARRAY-ATTRIBS` **(I/O & Config Routines)** (Impact: 27.2)
  * `9100-READ-BACKWARDS` **(I/O & Config Routines)** (Impact: 19.4)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 81 instances
* *State Mutation (weighted view):* 459
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 78`, `func_start: 39`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 297`, `dead_code: 7`, `unreferenced_by_name: 5`
* *Architecture:* `io: 12`, `api: 1`, `import: 11`
* *Defense:* `safety: 10`, `doc: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` COCOM01Y, COCRDLI, COTTL01Y, CSDAT01Y, CSMSG01Y, CSSTRPFY, CSUSR01Y, CVACT02Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.308)
- **Top Global Matches:** file_cluster_4: 7.308, file_cluster_2: 9.574, file_cluster_15: 9.66
- **Magnitude:** 681.08 | **LOC:** 700 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.6%), Complexity Load (formerly Cognitive Load) (38.4%), Dead Code Surface (formerly Dead Code) (5.4%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 16.2)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-TRAN-DATA *-----------...
  * `INITIALIZE-TRAN-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-TRAN-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 164 instances
* *State Mutation (weighted view):* 525
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 104`, `structural_boundaries: 60`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 197`, `dead_code: 1`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` COCOM01Y, COTRN00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.322)
- **Top Global Matches:** file_cluster_4: 7.322, file_cluster_2: 9.587, file_cluster_15: 9.674
- **Magnitude:** 667.82 | **LOC:** 696 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (86.0%), Complexity Load (formerly Cognitive Load) (38.8%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 27.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `POPULATE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.9)
    * *Intent:* *----------------------------------------------------------------* * POPULATE-USER-DATA *-----------...
  * `INITIALIZE-USER-DATA` **(I/O & Config Routines)** (Impact: 15.8)
    * *Intent:* *----------------------------------------------------------------* * INITIALIZE-USER-DATA *---------...
  * `PROCESS-PAGE-FORWARD` **(I/O & Config Routines)** (Impact: 15.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-FORWARD *---------...
  * `PROCESS-PAGE-BACKWARD` **(I/O & Config Routines)** (Impact: 14.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-PAGE-BACKWARD *--------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 512
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 59`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 192`
* *Architecture:* `io: 4`, `api: 1`, `import: 8`
* *Defense:* `safety: 6`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` COCOM01Y, COTTL01Y, COUSR00, CSDAT01Y, CSMSG01Y, CSUSR01Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/__tests__/provider/TarCopybookFileSystemProvider.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.669)
- **Top Global Matches:** file_cluster_10: 4.669, file_cluster_2: 6.9, file_cluster_13: 7.493
- **Magnitude:** 575.25 | **LOC:** 287 | **CtrlFlow:** 2.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (54.5%), Guard Balance (formerly Safety Score) (39.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.6%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 61
* *State Mutation (weighted view):* 5
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 66`, `args: 27`, `func_start: 17`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 26`, `concurrency: 41`, `import: 4`
* *Defense:* `safety: 8`, `test: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` TarCopybookFileSystemProvider, TarUtil, promises, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.397)
- **Top Global Matches:** file_cluster_4: 7.397, file_cluster_15: 8.997, file_cluster_2: 9.121
- **Magnitude:** 562.38 | **LOC:** 784 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (77.1%), Complexity Load (formerly Cognitive Load) (46.8%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `VALIDATE-INPUT-DATA-FIELDS` **(I/O & Config Routines)** (Impact: 56.1)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-DATA-FIELDS *---...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 16.6)
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `VALIDATE-INPUT-KEY-FIELDS` **(I/O & Config Routines)** (Impact: 8.9)
    * *Intent:* *----------------------------------------------------------------* * VALIDATE-INPUT-KEY-FIELDS *----...
  * `WRITE-TRANSACT-FILE` **(I/O & Config Routines)** (Impact: 8.0)
    * *Intent:* *----------------------------------------------------------------* * WRITE-TRANSACT-FILE *----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 111 instances
* *State Mutation (weighted view):* 407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 97`, `structural_boundaries: 84`, `args: 2`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `state_mutation: 185`
* *Architecture:* `io: 6`, `api: 1`, `import: 10`
* *Defense:* `safety: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` COCOM01Y, COTRN02, COTTL01Y, CSDAT01Y, CSMSG01Y, CVACT01Y, CVACT03Y, CVTRA05Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/cicsGenApp/positive/lgipdb01.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 7.879)
- **Top Global Matches:** file_cluster_2: 7.879, file_cluster_9: 7.902, file_cluster_15: 8.106
- **Magnitude:** 546.46 | **LOC:** 1238 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.248; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (68.3%), Complexity Load (formerly Cognitive Load) (38.1%), Dead Code Surface (formerly Dead Code) (6.2%), Connectivity (formerly Api Exposure) (1.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MAINLINE` **(I/O & Config Routines)** (Impact: 20.2)
    * *Intent:* *----------------------------------------------------------------*
  * `GET-ENDOW-DB2-INFO` **(I/O & Config Routines)** (Impact: 16.3)
    * *Intent:* *----------------------------------------------------------------* *================================...
  * `GET-MOTOR-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.7)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-HOUSE-DB2-INFO` **(I/O & Config Routines)** (Impact: 13.2)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
  * `GET-Commercial-DB2-INFO-1` **(I/O & Config Routines)** (Impact: 11.5)
    * *Intent:* *================================================================* * Use Select on join of Policy an...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 394
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 54`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `state_mutation: 186`, `dead_code: 4`, `unreferenced_by_name: 1`
* *Architecture:* `io: 24`, `api: 1`, `import: 3`
* *Defense:* `safety: 22`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001099
  * `Imports (Out-Degree: 3):` LGCMAREA, LGPOLICY, SQLCA
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `clients/analysis/src/vm/listing.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.46)
- **Top Global Matches:** file_cluster_4: 7.46, file_cluster_16: 8.038, file_cluster_15: 8.196
- **Magnitude:** 523.0 | **LOC:** 888 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **4**; blast radius 0.464; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.9%), Guard Balance (formerly Safety Score) (64.6%)
- **Documentation Coverage:** 78.4615% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `addInstructionsForNode` **(Compute Cores)** (Impact: 73.2)
  * `processPlaceholders` **(I/O & Config Routines)** (Impact: 30.4)
  * `getProcedurePositionsByNames` **(Compute Cores)** (Impact: 15.3)
  * `addChildren` **(Stateful Encapsulated Methods)** (Impact: 14.1)
  * `getProcedurePositionByName` **(Defensive Guards)** (Impact: 9.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 74 instances
* *State Mutation (weighted view):* 250
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 98`, `structural_boundaries: 109`, `args: 46`, `func_start: 46`, `class_start: 16`
* *Risk/State:* `state_mutation: 102`, `duplicate_logic: 5`
* *Architecture:* `api: 28`, `import: 4`
* *Defense:* `safety: 10`, `doc: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.464
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002394
  * `Imports (Out-Degree: 4):` cfast, instructions, utils, vm
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.599)
- **Top Global Matches:** file_cluster_10: 6.599, file_cluster_15: 7.169, file_cluster_2: 8.004
- **Magnitude:** 483.04 | **LOC:** 910 | **CtrlFlow:** 3.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (48.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeLineEndings` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 50 instances
* *Amplified Cascading Flux:* 5 instances
* *Concurrency (weighted view):* 430
* *State Mutation (weighted view):* 36
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 217`, `args: 61`, `func_start: 28`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 26`, `dead_code: 1`
* *Architecture:* `io: 12`, `concurrency: 180`, `import: 5`
* *Defense:* `safety: 21`, `test: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` testHelper, assert, path, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/__tests__/services/ProcessorGroupsLoader.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.154)
- **Top Global Matches:** file_cluster_10: 4.154, file_cluster_2: 6.845, file_cluster_13: 7.244
- **Magnitude:** 467.67 | **LOC:** 240 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **11**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Mutation Surface (formerly State Flux) (75.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.2%), Guard Balance (formerly Safety Score) (40.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Concurrency (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 46`, `args: 28`, `func_start: 5`
* *Risk/State:* `state_mutation: 18`
* *Architecture:* `io: 2`, `concurrency: 11`, `import: 11`
* *Defense:* `safety: 10`, `test: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` getE4EMock.utility, vscode, constants, ExternalAPIsService, ProcessorGroupsLoader, CopybookDownloaderForE4E, DatasetLib, LocalPathLib...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/test/suite/cfast.spec.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.387)
- **Top Global Matches:** file_cluster_10: 5.387, file_cluster_0: 6.35, file_cluster_2: 6.614
- **Magnitude:** 408.89 | **LOC:** 213 | **CtrlFlow:** 3.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (26.9%), Connectivity (formerly Api Exposure) (7.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 29`, `args: 11`, `func_start: 7`, `class_start: 1`
* *Risk/State:* None
* *Architecture:* `api: 7`, `concurrency: 27`, `import: 3`
* *Defense:* `safety: 7`, `test: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` testHelper, assert, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/__tests__/services/BridgeForGitSupport.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.029)
- **Top Global Matches:** file_cluster_10: 5.029, file_cluster_2: 7.72, file_cluster_13: 7.951
- **Magnitude:** 407.14 | **LOC:** 135 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (95.9%), Guard Balance (formerly Safety Score) (36.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 30`, `args: 17`, `func_start: 6`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* `concurrency: 14`, `import: 6`
* *Defense:* `safety: 14`, `test: 23`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` vscode, BridgeForGitLoader, ExternalAPIsService, ProcessorGroups, ProcessorGroupsLoader, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/CBTRN02C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.475)
- **Top Global Matches:** file_cluster_2: 6.475, file_cluster_11: 6.658, file_cluster_15: 6.908
- **Magnitude:** 401.88 | **LOC:** 732 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.8%), Complexity Load (formerly Cognitive Load) (33.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `1000-DALYTRAN-GET-NEXT` **(I/O & Config Routines)** (Impact: 10.2)
    * *Intent:* *---------------------------------------------------------------*
  * `2700-UPDATE-TCATBAL` **(I/O & Config Routines)** (Impact: 9.8)
    * *Intent:* *---------------------------------------------------------------*
  * `CBTRN02C` **(I/O & Config Routines)** (Impact: 9.1)
    * *Intent:* *****************************************************************
  * `1500-B-LOOKUP-ACCT` **(I/O & Config Routines)** (Impact: 8.5)
  * `2700-A-CREATE-TCATBAL-REC` **(I/O & Config Routines)** (Impact: 6.1)
    * *Intent:* *---------------------------------------------------------------*
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 51 instances
* *State Mutation (weighted view):* 238
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 140`, `func_start: 26`, `class_start: 1`
* *Risk/State:* `state_mutation: 136`
* *Architecture:* `io: 16`, `import: 5`
* *Defense:* `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` CVACT01Y, CVACT03Y, CVTRA01Y, CVTRA05Y, CVTRA06Y
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDSLC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.117)
- **Top Global Matches:** file_cluster_4: 8.117, file_cluster_12: 8.614, file_cluster_11: 9.706
- **Magnitude:** 391.64 | **LOC:** 888 | **CtrlFlow:** 11.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **13**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (69.0%), Complexity Load (formerly Cognitive Load) (45.7%), Dead Code Surface (formerly Dead Code) (5.2%), Connectivity (formerly Api Exposure) (2.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 25.2)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 18.9)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.1)
  * `9100-GETCARD-BYACCTCARD` **(I/O & Config Routines)** (Impact: 8.9)
  * `2220-EDIT-CARD` **(I/O & Config Routines)** (Impact: 8.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 55 instances
* *State Mutation (weighted view):* 248
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 42`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 138`, `dead_code: 1`, `unreferenced_by_name: 5`
* *Architecture:* `io: 4`, `api: 1`, `import: 13`
* *Defense:* `safety: 6`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` COCOM01Y, COCRDSL, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.copybooks.test.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.703)
- **Top Global Matches:** file_cluster_10: 4.703, file_cluster_2: 7.021, file_cluster_13: 7.604
- **Magnitude:** 384.12 | **LOC:** 278 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (83.0%), Guard Balance (formerly Safety Score) (45.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (9.8%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 75
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 75`, `args: 36`, `func_start: 9`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `io: 5`, `concurrency: 55`, `import: 5`
* *Defense:* `safety: 9`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` testHelper, assert, path, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTVWC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.13)
- **Top Global Matches:** file_cluster_12: 7.13, file_cluster_11: 8.135, file_cluster_2: 8.878
- **Magnitude:** 383.26 | **LOC:** 942 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **15**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.2%), Complexity Load (formerly Cognitive Load) (43.5%), Dead Code Surface (formerly Dead Code) (6.8%), Connectivity (formerly Api Exposure) (2.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.6)
  * `1200-SETUP-SCREEN-VARS` **(I/O & Config Routines)** (Impact: 11.8)
  * `1300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 10.6)
  * `9200-GETCARDXREF-BYACCT` **(I/O & Config Routines)** (Impact: 8.4)
  * `9300-GETACCTDATA-BYACCT` **(I/O & Config Routines)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 46 instances
* *State Mutation (weighted view):* 245
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 43`, `func_start: 35`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 153`, `dead_code: 4`, `duplicate_logic: 2`, `unreferenced_by_name: 2`
* *Architecture:* `io: 6`, `api: 1`, `import: 15`
* *Defense:* `safety: 8`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` COACTVW, COCOM01Y, COTTL01Y, CSDAT01Y, CSMSG01Y, CSMSG02Y, CSSTRPFY, CSUSR01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/__tests__/services/copybook/libs/DatasetLib.spec.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 4.124)
- **Top Global Matches:** file_cluster_10: 4.124, file_cluster_2: 6.755, file_cluster_13: 7.283
- **Magnitude:** 381.32 | **LOC:** 312 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (49.9%), Complexity Load (formerly Cognitive Load) (47.1%), Guard Balance (formerly Safety Score) (40.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 2 instances
* *Concurrency (weighted view):* 49
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 57`, `args: 34`, `func_start: 11`
* *Risk/State:* `state_mutation: 12`
* *Architecture:* `io: 7`, `concurrency: 29`, `import: 7`
* *Defense:* `safety: 7`, `test: 57`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` vscode, constants, ExternalAPIsService, ZoweExplorerDownloader, DatasetLib, Utils, vscode
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/commands/SmartTabCommand.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.37)
- **Top Global Matches:** file_cluster_12: 6.37, file_cluster_16: 7.076, file_cluster_15: 7.225
- **Magnitude:** 368.9 | **LOC:** 637 | **CtrlFlow:** 15.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 0.265; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.7%), Complexity Load (formerly Cognitive Load) (28.6%)
- **Documentation Coverage:** 56.7568% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleRangeSelectionSmartOutCommand` **(Many-Argument Workhorses)** (Impact: 28.9)
  * `handleRangeSelection` **(Many-Argument Workhorses)** (Impact: 20.7)
  * `getActualSelectionForTab` **(Compute Cores)** (Impact: 19.0)
    * *Intent:* /** * */
  * `getRule` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* /** * Founds a tab rule for current line */
  * `getPrevPosition` **(Many-Argument Workhorses)** (Impact: 14.6)
    * *Intent:* /** * Calculate previous column predefined position */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 37 instances
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 48`, `args: 33`, `func_start: 29`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 49`
* *Architecture:* `api: 11`, `import: 3`
* *Defense:* `safety: 4`, `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.265
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.001583
  * `Imports (Out-Degree: 1):` SmartTabSettings, vscode
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/CORPT00C.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.134)
- **Top Global Matches:** file_cluster_4: 7.134, file_cluster_6: 10.017, file_cluster_2: 12.11
- **Magnitude:** 363.46 | **LOC:** 650 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.0%), Complexity Load (formerly Cognitive Load) (45.3%), Connectivity (formerly Api Exposure) (2.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `PROCESS-ENTER-KEY` **(I/O & Config Routines)** (Impact: 41.5)
    * *Intent:* *----------------------------------------------------------------* * PROCESS-ENTER-KEY *------------...
  * `SUBMIT-JOB-TO-INTRDR` **(I/O & Config Routines)** (Impact: 12.4)
    * *Intent:* *----------------------------------------------------------------* * SUBMIT-JOB-TO-INTRDR *---------...
  * `MAIN-PARA` **(I/O & Config Routines)** (Impact: 11.0)
  * `WIRTE-JOBSUB-TDQ` **(I/O & Config Routines)** (Impact: 5.0)
    * *Intent:* *----------------------------------------------------------------* * WIRTE-JOBSUB-TDQ *-------------...
  * `SEND-TRNRPT-SCREEN` **(I/O & Config Routines)** (Impact: 4.2)
    * *Intent:* *----------------------------------------------------------------* * SEND-TRNRPT-SCREEN *-----------...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 48`, `args: 2`, `func_start: 10`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 144`
* *Architecture:* `io: 9`, `api: 1`, `import: 8`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.185
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` COCOM01Y, CORPT00, COTTL01Y, CSDAT01Y, CSMSG01Y, CVTRA05Y, DFHAID, DFHBMSCA
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.465)
- **Top Global Matches:** file_cluster_15: 7.465, file_cluster_16: 7.5, file_cluster_4: 8.122
- **Magnitude:** 353.4 | **LOC:** 559 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.244; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (99.5%), Mutation Surface (formerly State Flux) (96.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (88.4%), Complexity Load (formerly Cognitive Load) (49.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finishTask` **(Many-Argument Workhorses)** (Impact: 28.7)
  * `start` **(Defensive Guards)** (Impact: 21.8)
  * `finishTaskWithError` **(Defensive Guards)** (Impact: 19.5)
  * `queueAnalysis` **(Defensive Guards)** (Impact: 16.9)
  * `getAnalysis` **(Defensive Guards)** (Impact: 12.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 5 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 46
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 89`, `structural_boundaries: 88`, `args: 52`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `state_mutation: 29`, `planned_debt: 1`
* *Architecture:* `io: 1`, `api: 15`, `concurrency: 21`, `import: 11`
* *Defense:* `safety: 41`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.244
  * `Choke Point (Betweenness):` 6e-06 | `Ripple Effect (Closeness):` 0.00089
  * `Imports (Out-Degree: 5):` constants, Settings, reporter, FSUtils, messages, analysis, GraphDTO, external...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/DialectParserListener.java` (JAVA) | Magnitude: 14.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 26, import: 15, args: 7
- `server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/DialectParserListener.java` (JAVA) | Magnitude: 14.76 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 44, structural_boundaries: 26, import: 15, args: 7
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireOptionsCheckUtility.java` (JAVA) | Magnitude: 17.14 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 19, import: 10, branch: 5
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/action/CodeActionProvider.java` (JAVA) | Magnitude: 3.32 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 8, import: 6, safety: 2, api: 2
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variable/VariableDefinitionNameNode.java` (JAVA) | Magnitude: 12.76 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 22, import: 13, args: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/FunctionReferenceProcessor.java` (JAVA) | Magnitude: 8.96 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 10, structural_boundaries: 9, import: 5, args: 4
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/sql/TestSqlHostVariable.java` (JAVA) | Magnitude: 91.74 | Delta: **0.087** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 612, closures: 113, structural_boundaries: 81, args: 39
- `server/engine/src/main/java/org/eclipse/lsp/cobol/dialects/TrueDialectServiceImpl.java` (JAVA) | Magnitude: 17.22 | Delta: **0.19** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 50, structural_boundaries: 32, import: 21, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR02C.cbl` (COBOL) | Magnitude: 289.96 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 303, state_mutation: 88, branch: 44, structural_boundaries: 43
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/CBACT04C.cbl` (COBOL) | Magnitude: 337.14 | Delta: **0.061** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 552, structural_boundaries: 130, state_mutation: 111, branch: 86
- `server/engine/src/test/java/org/eclipse/lsp/cobol/ClientServerTestModule.java` (JAVA) | Magnitude: 12.88 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 115, indent_spaces: 69, import: 44, encapsulation: 8
- `tests/test_files/cicsGenApp/positive/lgipvs01.cbl` (COBOL) | Magnitude: 58.16 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 128, state_mutation: 19, structural_boundaries: 10, reflection_metaprogramming: 10
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR03C.cbl` (COBOL) | Magnitude: 209.22 | Delta: **0.107** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 251, state_mutation: 65, structural_boundaries: 38, branch: 34

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `server/engine/src/test/java/org/eclipse/lsp/cobol/service/delegates/completions/VariableCompletionTest.java` (JAVA) | Magnitude: 15.28 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 29, import: 13, core_var_decl: 8
- `server/dialect-idms/src/test/java/org/eclipse/lsp/cobol/dialects/idms/CobolErrorStrategyTest.java` (JAVA) | Magnitude: 41.6 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 93, structural_boundaries: 53, test: 27, test_skip: 19
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/ProgramEndCheck.java` (JAVA) | Magnitude: 25.0 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 42, structural_boundaries: 17, import: 9, branch: 8
- `server/engine/src/test/resources/CM101M.CBL` (COBOL) | Magnitude: 327.88 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 659, state_mutation: 167, structural_boundaries: 94, func_start: 65
- `server/engine/src/main/java/org/eclipse/lsp/cobol/cli/command/ListSources.java` (JAVA) | Magnitude: 23.06 | Delta: **0.069** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 51, structural_boundaries: 25, import: 13, core_var_decl: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variables/FileDescriptionNode.java` (JAVA) | Magnitude: 15.5 | Delta: **0.008** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 29, structural_boundaries: 19, import: 11, decorators: 7
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ProgramIdNode.java` (JAVA) | Magnitude: 13.54 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 17, import: 10, decorators: 8
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSErrorListener.java` (JAVA) | Magnitude: 12.68 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 40, structural_boundaries: 25, import: 15, args: 6
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ParagraphNode.java` (JAVA) | Magnitude: 6.84 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, import: 5, api: 3
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ProcedureSectionNode.java` (JAVA) | Magnitude: 6.84 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, import: 5, api: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `clients/analysis/src/__tests__/__resources__/cfgraph/case91.cbl` (COBOL) | Magnitude: 5.96 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 9, func_start: 4, safety_bypasses: 3
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/replacement/ReplacementHelper.java` (JAVA) | Magnitude: 30.34 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, branch: 8, safety_bypasses: 8
- `server/engine/src/test/java/org/eclipse/lsp/cobol/utils/AstToJsonTest.java` (JAVA) | Magnitude: 5.44 | Delta: **0.162** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 14, safety_bypasses: 6, test: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `server/dialect-daco/src/test/java/org/eclipse/lsp/cobol/dialects/daco/utils/Fixtures.java` (JAVA) | Magnitude: 6.46 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, api: 3, doc: 3
- `server/dialect-idms/src/test/java/org/eclipse/lsp/cobol/dialects/idms/utils/Fixtures.java` (JAVA) | Magnitude: 6.46 | Delta: **0.032** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, indent_spaces: 6, api: 3, doc: 3
- `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` (TYPESCRIPT) | Magnitude: 353.4 | Delta: **0.035** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 426, branch: 89, structural_boundaries: 88, args: 52
- `clients/cobol-lsp-vscode-extension/src/services/BridgeForGitLoader.ts` (TYPESCRIPT) | Magnitude: 42.88 | Delta: **0.046** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 27, core_var_decl: 12, branch: 7
- `clients/cobol-lsp-vscode-extension/src/services/snippetcompletion/SnippetCompletionProvider.ts` (TYPESCRIPT) | Magnitude: 134.4 | Delta: **0.088** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 44, core_var_decl: 34, args: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `server/engine/src/main/java/org/eclipse/lsp/cobol/dialects/hp/CopybookParser.java` (JAVA) | Magnitude: 37.88 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 36, structural_boundaries: 21, core_var_decl: 14, design_snake_case: 12
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSIssueOptionsCheckUtility.java` (JAVA) | Magnitude: 124.4 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 310, structural_boundaries: 62, branch: 47, args: 28
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/reader/CobolLineReader.java` (JAVA) | Magnitude: 93.42 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 176, structural_boundaries: 53, core_var_decl: 27, args: 22
- `server/engine/src/test/java/org/eclipse/lsp/cobol/core/engine/processors/RootNodeUpdateCopyNodesByPositionInTreeTest.java` (JAVA) | Magnitude: 13.62 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 88, structural_boundaries: 58, import: 14, core_var_decl: 12
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSExtractSPOptionsCheckUtility.java` (JAVA) | Magnitude: 46.14 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 197, structural_boundaries: 27, args: 16, branch: 14

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `clients/analysis/src/vm/index.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `server/engine/src/test/java/org/eclipse/lsp/cobol/service/delegates/completions/MockCompletionModel.java` (JAVA) | Magnitude: 16.16 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 41, structural_boundaries: 26, import: 14, core_var_decl: 10
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ProgramSubtype.java` (JAVA) | Magnitude: 4.78 | Delta: **0.097** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, structural_boundaries: 2, api: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ReplaceStrategy.java` (JAVA) | Magnitude: 2.44 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, doc: 2, import: 2, indent_spaces: 2
- `tests/test_files/cicsGenApp/positive/lgipdb01.cbl` (COBOL) | Magnitude: 546.46 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 893, state_mutation: 186, branch: 74, structural_boundaries: 54
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestExecCicsSendStatementsArgumentsOrder.java` (JAVA) | Magnitude: 3.74 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 120, structural_boundaries: 7, import: 4, args: 1
- `clients/cobol-lsp-vscode-extension/src/web/extension.ts` (TYPESCRIPT) | Magnitude: 34.68 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 18, import: 11, state_mutation: 6
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/UseCaseInitializer.java` (JAVA) | Magnitude: 3.2 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 3, api: 2, doc: 2, args: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL) | Magnitude: 2166.24 | Delta: **0.082** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 3372, state_mutation: 700, branch: 403, structural_boundaries: 155
- `server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java` (JAVA) | Magnitude: 205.14 | Delta: **0.223** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 282, structural_boundaries: 96, branch: 85, args: 47

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/processor/CICSImplicitVariablesProcessor.java` (JAVA) | Magnitude: 16.66 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 26, structural_boundaries: 17, import: 8, branch: 5
- `server/engine/src/test/java/org/eclipse/lsp/cobol/positive/PositiveTest.java` (JAVA) | Magnitude: 59.6 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 148, structural_boundaries: 65, import: 36, args: 27
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSendOptionsCheckUtility.java` (JAVA) | Magnitude: 78.6 | Delta: **0.039** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 260, structural_boundaries: 38, branch: 30, import: 12
- `server/engine/src/test/java/org/eclipse/lsp/cobol/service/WorkspaceServiceTest.java` (JAVA) | Magnitude: 35.6 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 185, structural_boundaries: 99, core_var_decl: 41, design_camel_case: 34
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSDocumentOptionsCheckUtility.java` (JAVA) | Magnitude: 40.0 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 122, structural_boundaries: 27, branch: 13, import: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/Locality.java` (JAVA) | Magnitude: 5.64 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 11, decorators: 7, import: 6
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/strategy/BasicCobolErrorHandler.java` (JAVA) | Magnitude: 59.88 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 115, structural_boundaries: 35, encapsulation: 16, args: 14
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ExtendedTextLine.java` (JAVA) | Magnitude: 114.3 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 112, structural_boundaries: 38, args: 29, func_start: 23
- `server/engine/src/test/java/org/eclipse/lsp/cobol/core/utils/CustomToken.java` (JAVA) | Magnitude: 44.3 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 57, structural_boundaries: 23, api: 22, decorators: 17
- `tests/native-executable-tests/src/util/util.ts` (TYPESCRIPT) | Magnitude: 13.24 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: structural_boundaries: 11, indent_spaces: 11, io: 8, args: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/test_files/cicsGenApp/positive/lgastat1.cbl` (COBOL) | Magnitude: 44.52 | Delta: **0.058** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 106, state_mutation: 14, structural_boundaries: 9, reflection_metaprogramming: 9

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` -> Churn: **62.72%** | Cog Load: 57.9499% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 884.12
- `clients/cobol-lsp-vscode-extension/src/__tests__/provider/TarCopybookFileSystemProvider.spec.ts` -> **Aman Prashant** (100.0% isolated ownership) | Magnitude: 575.25
- `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.test.ts` -> **Leonid Baranov** (100.0% isolated ownership) | Magnitude: 483.04
- `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.copybooks.test.ts` -> **Leonid Baranov** (100.0% isolated ownership) | Magnitude: 384.12
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/copybook/libs/DatasetLib.spec.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 381.32

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/DocumentModelService.java` -> **Severity: 0.262** (Bridge: 0.0031 * Flux: 83.5617%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSVisitor.java` -> **Severity: 0.235** (Bridge: 0.0024 * Flux: 97.2313%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSOptionsCheckUtility.java` -> **Severity: 0.222** (Bridge: 0.0022 * Flux: 99.9947%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ExtendedText.java` -> **Severity: 0.162** (Bridge: 0.0016 * Flux: 100.0%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSDialect.java` -> **Severity: 0.129** (Bridge: 0.0031 * Flux: 41.2281%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/Node.java` -> **Severity: 15.188** (Embedded: 0.2238 * Error Risk: 67.8497%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 13.912** (Embedded: 0.1739 * Error Risk: 80.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/symbols/ProcedureId.java` -> **Severity: 10.737** (Embedded: 0.1342 * Error Risk: 80.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/Locality.java` -> **Severity: 10.564** (Embedded: 0.1962 * Error Risk: 53.8495%)
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` -> **Severity: 9.348** (Embedded: 0.196 * Error Risk: 47.6832%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` -> **Severity: 2703.822** (Blast Radius: 57.939 * Doc Risk: 46.6667%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java` -> **Severity: 2381.8** (Blast Radius: 23.818 * Doc Risk: 100.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 1210.1** (Blast Radius: 12.101 * Doc Risk: 100.0%)
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/CobolText.java` -> **Severity: 1187.8** (Blast Radius: 11.878 * Doc Risk: 100.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ProgramNode.java` -> **Severity: 536.7** (Blast Radius: 5.367 * Doc Risk: 100.0%)

## 13. MAINFRAME SYSTEM FACTS (Named Relations & Record Layouts)
> **AI CONTEXT:** Named mainframe relations the structural signal counts flatten -- the call graph (`CALL`/CICS `LINK`·`XCTL`/JCL `EXEC PGM=`), the dataset boundary (`SELECT…ASSIGN` + `OPEN` modes, JCL `DD`→dataset), and record layouts (COBOL DATA DIVISION items, PL/I `DECLARE`d structures). BMS screen maps (every field's position, length and attributes, `screen_field_data`) are the 3270 UI surface. These are the schema of the system: use them to trace which program runs which, which dataset a job binds, and the shape of the records that flow between them. Extracted by the engine (`core/mainframe_boundary.py`) and carried in the master DB (`call_site_data`/`dataset_data`/`record_data`); resolution to files is redone per scan.

- **Coverage:** `245` files carry mainframe facts -- `180` call sites, `38` dataset bindings, `10908` record items.

- **DB2 table access:** `48` embedded SQL statements touching `9` tables (SELECT/INSERT/UPDATE/DELETE, cursors, host variables) in `sql_statement_data`; the program x table read/write matrix is `GalaxyIR.sql_table_access()`.

- **CICS operations:** `188` EXEC CICS operations naming a resource (`5` CONTAINER, `60` FILE, `89` MAP, `34` QUEUE); verb, direction, VALUE-resolved name and INTO/FROM record in `cics_resource_data`.

- **CICS task control:** `9` commands (`4` DELAY, `2` DEQ, `2` ENQ, `1` START); child transid (or its STRING-built pattern), channel, CHILD/REQID token and timing in `cics_task_data`.

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CAUP ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (580 items):** `WS-MISC-STORAGE (376)`, `WS-THIS-PROGCOMMAREA (162)`, `WS-LITERALS (33)`, `DFHCOMMAREA (2)`, `LIT-ALL-ALPHA-FROM (1)`, `LIT-ALL-ALPHANUM-FROM (1)`, `LIT-ALL-NUM-FROM (1)`, `LIT-ALPHA-SPACES-TO (1)`, `LIT-ALPHANUM-SPACES-TO (1)`, `LIT-NUM-SPACES-TO (1)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CACTUPA (read/write)`, `FILE CXACAIX (read)`, `FILE ACCTDAT (read/update)`, `FILE CUSTDAT (read/update)`
- **Data moves:** 751 (COMPUTE 5, INITIALIZE 14, MOVE 620, STRING 112); most-fed items `WS-EDIT-ALPHANUM-ONLY`, `WS-RETURN-MSG`, `WS-EDIT-CURRENCY-9-2-F`, `ERROR-RESP`, `ERROR-RESP2`, `WS-EDIT-SIGNED-NUMBER-9V2-X`
- **Unit of work:** `1` commit / `1` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `7/10` RESP results tested

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COTRN00.CPY` (COBOL)
- **Record layouts (712 items):** `COTRN0AI (356)`, `COTRN0AO (356)`

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COUSR00.CPY` (COBOL)
- **Record layouts (712 items):** `COUSR0AI (356)`, `COUSR0AO (356)`

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COACTUP.CPY` (COBOL)
- **Record layouts (652 items):** `CACTUPAI (326)`, `CACTUPAO (326)`

### `tests/test_files/cicsGenApp/copybooks/ssmap.cpy` (COBOL)
- **Record layouts (612 items):** `SSMAPP4I (112)`, `SSMAPP1I (77)`, `SSMAPP2I (67)`, `SSMAPC1I (62)`, `SSMAPP3I (62)`, `SSMAPP5I (52)`, `SSMAPP4O (46)`, `SSMAPP1O (32)`, `SSMAPP2O (28)`, `SSMAPC1O (26)`, `SSMAPP3O (26)`, `SSMAPP5O (22)`

### `tests/test_files/cicsGenApp/positive/lgwebst5.cbl` (COBOL)
- **Calls:** `START TRANSID SSST`
- **Record layouts (218 items):** `SYMBLIST (81)`, `WS-HEADER (6)`, `DFHCOMMAREA (5)`, `WS-HHMMSS (4)`, `WS-OLDV (4)`, `COUNTVAL (1)`, `COUNTSUCCESS (1)`, `COUNTERRORS (1)`, `COUNTINQ (1)`, `COUNTADD (1)`, `COUNTUPD (1)`, `COUNTDEL (1)` … (+111 more)
- **CICS operations:** `QUEUE WS-TSQname? (delete/read/write)`, `QUEUE WS-TSQNAME? (delete/write)`
- **CICS task control:** `START SSST`
- **Data moves:** 275 (COMPUTE 100, INITIALIZE 1, MOVE 124, STRING 50); most-fed items `COUNTERRORS`, `COUNTSUCCESS`, `WS-TSQNAME`, `NRATEVAL`, `COUNTADD`, `COUNTINQ`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/46` RESP results tested

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COCRDLI.CPY` (COBOL)
- **Record layouts (544 items):** `CCRDLIAI (272)`, `CCRDLIAO (272)`

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COACTVW.CPY` (COBOL)
- **Record layouts (448 items):** `CACTVWAI (224)`, `CACTVWAO (224)`

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDUPC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CCUP ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (179 items):** `WS-MISC-STORAGE (111)`, `WS-THIS-PROGCOMMAREA (42)`, `WS-LITERALS (23)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CCRDUPA (read/write)`, `FILE CARDDAT (read/update)`
- **Data moves:** 219 (INITIALIZE 13, MOVE 201, STRING 5); most-fed items `ACCTSIDA OF CCRDUPAI`, `CARDSIDA OF CCRDUPAI`, `CRDNAMEA OF CCRDUPAI`, `CRDSTCDA OF CCRDUPAI`, `EXPMONA OF CCRDUPAI`, `EXPYEARA OF CCRDUPAI`
- **Unit of work:** `1` commit / `0` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `3/6` RESP results tested

### `server/engine/src/test/resources/CM101M.CBL` (COBOL)
- **Datasets:** `XXXXX055(OUTPUT)`
- **Record layouts (174 items):** `LOG-LINE (22)`, `TEST-RESULTS (19)`, `LOG-HDR-4 (15)`, `COLUMNS-LINE-2 (13)`, `LOG-HDR-3 (9)`, `COLUMNS-LINE-1 (8)`, `CCVS-E-2 (7)`, `XXINFO (7)`, `LOG-HDR-2 (6)`, `CCVS-E-3 (6)`, `CCVS-H-2 (5)`, `CCVS-E-1 (5)` … (+27 more)
- **Data moves:** 212 (ACCEPT 9, ADD 6, COMPUTE 13, MOVE 184); most-fed items `PRINT-REC`, `COMPUTED-STATUS`, `MAIN-QUEUE`, `LAG-TIME`, `DUMMY-RECORD`, `COMP-TIME`

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDLIC.cbl` (COBOL)
- **Calls:** `XCTL LIT-MENUPGM`, `XCTL CCARD-NEXT-PROG`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL COMEN01C ← CARDDEMO-COMMAREA`, `XCTL CCARD-NEXT-PROG ← CARDDEMO-COMMAREA`, `RETURN TRANSID CCLI ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (129 items):** `WS-MISC-STORAGE (79)`, `WS-THIS-PROGCOMMAREA (27)`, `WS-CONSTANTS (20)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CCRDLIA (read/write)`, `FILE CARDDAT (browse/read)`
- **Data moves:** 237 (ADD 3, COMPUTE 1, INITIALIZE 8, MOVE 222, SUBTRACT 3); most-fed items `CDEMO-LAST-MAP`, `CDEMO-FROM-PROGRAM`, `CDEMO-LAST-MAPSET`, `WS-EDIT-SELECT`, `CDEMO-FROM-TRANID`, `CCARD-NEXT-MAP`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `4/8` RESP results tested

### `tests/test_files/cicsGenApp/positive/lgipdb01.cbl` (COBOL)
- **Calls:** `LINK LGSTSQ`
- **COMMAREA passed:** `LINK LGSTSQ ← ERROR-MSG LENGTH(LENGTH OF ERROR-MSG)`, `LINK LGSTSQ ← CA-ERROR-MSG LENGTH(LENGTH OF CA-ERROR-MSG)`
- **Record layouts (82 items):** `DB2-OUT-INTEGERS (23)`, `ERROR-MSG (13)`, `WS-HEADER (8)`, `TSAREA (7)`, `DB2-IN-INTEGERS (4)`, `CA-ERROR-MSG (3)`, `WS-COMMAREA-LENGTHS (3)`, `ABS-TIME (1)`, `TIME1 (1)`, `DATE1 (1)`, `MINUS-ONE (1)`, `END-POLICY-POS (1)` … (+16 more)
- **DB2 table access:** `POLICY (read)`, `COMMERCIAL (read)`, `CLAIM (read)`, `ENDOWMENT (read)`, `HOUSE (read)`, `MOTOR (read)`
- **CICS operations:** `CONTAINER ICOM-Data (read/write)`, `CONTAINER ICOM-Count (write)`
- **Data moves:** 178 (ADD 15, INITIALIZE 13, MOVE 148, MULTIPLY 2); most-fed items `WS-REQUIRED-CA-LEN`, `CA-POLICY-COMMON`, `CA-CUSTOMER-NUM`, `CA-COMMERCIAL`, `CA-POLICY-NUM`, `DB2-B-CRIMEPERIL`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/1` RESP results tested

### `tests/test_files/cicsGenApp/copybooks/ssmap.bms` (BMS)
- **Screen maps:** `SSMAPC1 (12 named / 41 fields)`, `SSMAPP1 (15 named / 52 fields)`, `SSMAPP2 (13 named / 45 fields)`, `SSMAPP3 (12 named / 42 fields)`, `SSMAPP4 (22 named / 66 fields)`, `SSMAPP5 (10 named / 33 fields)`

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN02C.cbl` (COBOL)
- **Calls:** `RETURN TRANSID WS-TRANID`, `CALL CSUTLDTC`, `XCTL CDEMO-TO-PROGRAM`
- **COMMAREA passed:** `RETURN TRANSID CT02 ← CARDDEMO-COMMAREA`, `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`
- **Record layouts (43 items):** `WS-VARIABLES (24)`, `CSUTLDTC-PARM (17)`, `DFHCOMMAREA (2)`
- **CICS operations:** `MAP COTRN2A (read/write)`, `FILE CXACAIX (read)`, `FILE CCXREF (read)`, `FILE TRANSACT (browse/read/write)`
- **Data moves:** 210 (ADD 1, COMPUTE 4, INITIALIZE 1, MOVE 200, STRING 4); most-fed items `CARDNINI OF COTRN2AI`, `ACTIDINI OF COTRN2AI`, `CSUTLDTC-DATE`, `CSUTLDTC-DATE-FORMAT`, `TRNAMTI OF COTRN2AI`, `WS-MESSAGE`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `5/6` RESP results tested

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COTRN01.CPY` (COBOL)
- **Record layouts (256 items):** `COTRN1AI (128)`, `COTRN1AO (128)`

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COTRN02.CPY` (COBOL)
- **Record layouts (256 items):** `COTRN2AI (128)`, `COTRN2AO (128)`

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/CBTRN02C.cbl` (COBOL)
- **Calls:** `CALL CEE3ABD`
- **Datasets:** `DALYTRAN(INPUT)`, `TRANFILE(OUTPUT)`, `XREFFILE(INPUT)`, `DALYREJS(OUTPUT)`, `ACCTFILE(I-O)`, `TCATBALF(I-O)`
- **Record layouts (92 items):** `FILLER (15)`, `COBOL-TS (9)`, `FD-TRAN-CAT-BAL-RECORD⟵TCATBAL-FILE (6)`, `WS-COUNTERS (4)`, `FD-TRAN-RECORD⟵DALYTRAN-FILE (3)`, `FD-TRANFILE-REC⟵TRANSACT-FILE (3)`, `FD-XREFFILE-REC⟵XREF-FILE (3)`, `FD-REJS-RECORD⟵DALYREJS-FILE (3)`, `FD-ACCTFILE-REC⟵ACCOUNT-FILE (3)`, `DALYTRAN-STATUS (3)`, `TRANFILE-STATUS (3)`, `XREFFILE-STATUS (3)` … (+15 more)
- **Keyed files:** `TRANSACT-FILE INDEXED/RANDOM key FD-TRANS-ID`, `XREF-FILE INDEXED/RANDOM key FD-XREF-CARD-NUM`, `ACCOUNT-FILE INDEXED/RANDOM key FD-ACCT-ID`, `TCATBAL-FILE INDEXED/RANDOM key FD-TRAN-CAT-KEY`
- **Data moves:** 151 (ADD 7, COMPUTE 3, INITIALIZE 1, MOVE 131, READ 4, REWRITE 2, WRITE 3); most-fed items `IO-STATUS`, `WS-TEMP-BAL`, `FD-TRAN-CAT-BAL-RECORD`, `IO-STATUS-04`, `TRAN-CAT-BAL`, `ACCT-CURR-BAL`

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTVWC.cbl` (COBOL)
- **Calls:** `XCTL CDEMO-TO-PROGRAM`, `RETURN TRANSID LIT-THISTRANID`
- **COMMAREA passed:** `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`, `RETURN TRANSID CAVW ← WS-COMMAREA LENGTH(LENGTH OF WS-COMMAREA)`
- **Record layouts (96 items):** `WS-MISC-STORAGE (59)`, `WS-LITERALS (30)`, `WS-THIS-PROGCOMMAREA (4)`, `DFHCOMMAREA (2)`, `WS-COMMAREA (1)`
- **CICS operations:** `MAP CACTVWA (read/write)`, `FILE CXACAIX (read)`, `FILE ACCTDAT (read)`, `FILE CUSTDAT (read)`
- **Data moves:** 144 (INITIALIZE 5, MOVE 113, STRING 26); most-fed items `WS-RETURN-MSG`, `ERROR-RESP`, `ERROR-RESP2`, `ACCTSIDC OF CACTVWAO`, `ACSTSSNO OF CACTVWAO`, `CCARD-ERROR-MSG`
- **Unit of work:** `0` commit / `0` rollback points; handlers `ABEND->ABEND-ROUTINE`, `ABEND->CANCEL`; `3/6` RESP results tested

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/CORPT00C.cbl` (COBOL)
- **Calls:** `RETURN TRANSID WS-TRANID`, `CALL CSUTLDTC`, `XCTL CDEMO-TO-PROGRAM`
- **COMMAREA passed:** `RETURN TRANSID CR00 ← CARDDEMO-COMMAREA`, `XCTL CDEMO-TO-PROGRAM ← CARDDEMO-COMMAREA`
- **Record layouts (81 items):** `WS-VARIABLES (40)`, `JOB-DATA (31)`, `CSUTLDTC-PARM (8)`, `DFHCOMMAREA (2)`
- **CICS operations:** `QUEUE JOBS (write)`, `MAP CORPT0A (read/write)`
- **Job submission:** `JOB TRNRPT00`, `EXEC PROC=TRANREPT`
- **Data moves:** 162 (ADD 2, COMPUTE 7, INITIALIZE 11, MOVE 134, STRING 8); most-fed items `WS-MESSAGE`, `WS-NUM-99`, `PARM-END-DATE-1`, `PARM-END-DATE-2`, `PARM-START-DATE-1`, `PARM-START-DATE-2`
- **Unit of work:** `0` commit / `0` rollback points; handlers none; `1/2` RESP results tested

### `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/COADM01.CPY` (COBOL)
- **Record layouts (244 items):** `COADM1AI (122)`, `COADM1AO (122)`

*(+225 more files with mainframe facts; full detail in `record_data`/`call_site_data`/`dataset_data`.)*

- **Mainframe skeleton completeness:** 69% (mean channel ratio; channel table in the audit report, section 7). Top missing inputs: JCL and PROC libraries (217 gaps); BMS map sources (37 gaps); copybook libraries (15 gaps).

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`panics_and_aborts`:** 407 literal sites + 10 sites through wrappers = 417

- `throwInvalidParameters` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/TextMapReplacer.java`
- `analyzeAllOpenedDocuments` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/handlers/workspace/DidChangeWatchedFilesHandler.java`
- `checkIntegerLiteral` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblParser.java`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 36946 call pairs -- scoped 31.0%, unique 1.2%, ambiguous 24.8%, external 42.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| java | 33733 | 28.9% | 1.3% | 26.6% | 43.2% |
| typescript | 2172 | 33.7% | 0.0% | 9.1% | 57.3% |
| cobol | 1017 | 97.1% | 0.8% | 0.1% | 2.1% |
| javascript | 18 | 0.0% | 0.0% | 11.1% | 88.9% |
| shell | 6 | 0.0% | 0.0% | 0.0% | 100.0% |

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
