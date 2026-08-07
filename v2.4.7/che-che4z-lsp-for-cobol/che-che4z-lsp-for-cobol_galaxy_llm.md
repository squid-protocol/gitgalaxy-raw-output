# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/che-che4z-lsp-for-cobol` |
| **Timestamp** | `2026-08-07T03:50:40.424159+00:00` |
| **Scan Duration** | `21.64s` |
| **Git Branch** | `development` |
| **Git Commit** | `dd1133952579575082914476fa699667b8790e1d` |
| **Git Remote** | `https://github.com/eclipse/che-che4z-lsp-for-cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2749 malicious artifacts.

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
| Total Artifacts | 3535 |
| Analyzed Artifacts (Scanned) | 3127 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 408 |
| Total LOC | 678343 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.5% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6307 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3311 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.1286 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 101 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 1570 | 119049 | 50.2% |
| COBOL | 968 | 500520 | 31.0% |
| JSON | 283 | 35863 | 9.1% |
| TYPESCRIPT | 194 | 21859 | 6.2% |
| PLAINTEXT | 39 | 2 | 1.2% |
| MARKDOWN | 29 | 0 | 0.9% |
| XML | 24 | 0 | 0.8% |
| JAVASCRIPT | 14 | 327 | 0.4% |
| YAML | 3 | 24 | 0.1% |
| SHELL | 2 | 11 | 0.1% |
| JCL | 1 | 688 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `6.386`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2240 | 71.6% |
| file_cluster_13 | 714 | 22.8% |
| file_cluster_4 | 44 | 1.4% |
| file_cluster_16 | 22 | 0.7% |
| file_cluster_0 | 16 | 0.5% |
| file_cluster_11 | 11 | 0.4% |
| file_cluster_17 | 8 | 0.3% |
| Unknown | 2 | 0.1% |
| file_cluster_9 | 2 | 0.1% |
| file_cluster_2 | 1 | 0.0% |
| file_cluster_7 | 1 | 0.0% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 408*

**Composition by Extension & Reason:**
- `.dot`: 118x Unsupported Format (.dot), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.cbl`: 11x Excluded (Saturation: Line 53 exceeds 500 chars), 10x Excluded (Saturation: Line 2 exceeds 500 chars), 6x Excluded (Saturation: Line 72 exceeds 500 chars)
- `no_extension`: 54x Unsupported Format (.undeterminable), 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3867 LOC), 1x Excluded (Massive Static Asset Blob: 4112 LOC)
- `.g4`: 24x Unsupported Format (.g4)
- `.cpy`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.gif`: 8x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.copy`: 3x Excluded (Unsupported Extension: '.COPY')
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.original`: 2x Unsupported Format (.original)
- `.ts`: 1x Excluded (Saturation: Line 84 exceeds 500 chars)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 13.7 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 34.8 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 11.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 3.0 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.0 | 2.5 | 0.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.8 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 13.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` (Hits: 1410)
- `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2094.2.cbl` (Hits: 1347)
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2154.2.cbl` (Hits: 1150)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **UseCaseEngine.java** (`server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java`) — 579 inbound connections
2. **ErrorSource.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java`) — 397 inbound connections
3. **Diagnostic.java** (`server/parser/src/main/java/org/eclipse/lsp/cobol/parser/Diagnostic.java`) — 362 inbound connections
4. **SyntaxError.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java`) — 213 inbound connections
5. **Locality.java** (`server/common/src/main/java/org/eclipse/lsp/cobol/common/model/Locality.java`) — 187 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **CliModule.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/cli/di/CliModule.java`) — 63 outbound dependencies
2. **CobolLanguageServerTest.java** (`server/engine/src/test/java/org/eclipse/lsp/cobol/service/CobolLanguageServerTest.java`) — 60 outbound dependencies
3. **TestModule.java** (`server/engine/src/test/java/org/eclipse/lsp/cobol/TestModule.java`) — 58 outbound dependencies
4. **CICSVisitor.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSVisitor.java`) — 49 outbound dependencies
5. **ServiceModule.java** (`server/engine/src/main/java/org/eclipse/lsp/cobol/domain/modules/ServiceModule.java`) — 48 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl`) -> Impact: **919.5** | LOC: 3071
- `FAIL` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl`) -> Impact: **874.1** | LOC: 803
- `checkOptions` (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`) -> Impact: **677.4** | LOC: 707
- `DNAME42` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl`) -> Impact: **652.1** | LOC: 1223
- `WRK-DU-18V00` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl`) -> Impact: **605.2** | LOC: 1144
- `checkOptions` (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSysSetOptionsCheckUtility.java`) -> Impact: **584.4** | LOC: 205
- `SECT-NC201A-001` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl`) -> Impact: **517.3** | LOC: 386
- `SECT-IC225A-001` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/IC2254.2.cbl`) -> Impact: **454.7** | LOC: 572
- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1084.2.cbl`) -> Impact: **375.5** | LOC: 1590
- `phrase` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl`) -> Impact: **374.2** | LOC: 1965

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/test_files/Cobol85PositiveTestsSuite/positive` | 233 | 193005.82 | 36.45% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/compileListing` | 233 | 134591.4 | 28.5% | 0.0% |
| `tests/test_files/aws-mainframe-modernization-carddemo/positive` | 26 | 12803.8 | 42.03% | 0.0% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility` | 109 | 10825.38 | 21.58% | 37.46% |
| `clients/cobol-lsp-vscode-extension` | 9 | 10094.96 | 2.43% | 0.0% |
| `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases` | 404 | 8499.62 | 4.52% | 0.0% |
| `clients/analysis/src/__tests__/__resources__/cfgraph` | 321 | 4653.66 | 10.36% | 15.16% |
| `tests/test_files/cicsGenApp/positive` | 31 | 4101.12 | 44.52% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot` | 139 | 3200.26 | 3.36% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/negative` | 3 | 2591.38 | 26.64% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/verify_musl_setup.sh` -> **100.0%** Exposure
- `delombok.sh` -> **100.0%** Exposure
- `clients/analysis/src/vm/instructions.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/__tests__/CommentCommandTest.spec.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/__tests__/commands/ClearCopybookCacheCommand.spec.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `clients/analysis/src/model/Graph.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/listing.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/utils.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/vm.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/vp.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2184.2.cbl` -> **585** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1264.2.cbl` -> **457** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2234.2.cbl` -> **421** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2174.2.cbl` -> **400** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/negative/NC1074.2.cbl` -> **364** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`tests/test_files/Cobol85PositiveTestsSuite/negative/SM2064.2.cbl`** -> AI Confidence: **99.48%**
2. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COADM01C.cbl`** -> AI Confidence: **99.48%**
3. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COBIL00C.cbl`** -> AI Confidence: **99.48%**
4. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COMEN01C.cbl`** -> AI Confidence: **99.48%**
5. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/CORPT00C.cbl`** -> AI Confidence: **99.48%**
6. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COSGN00C.cbl`** -> AI Confidence: **99.48%**
7. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN00C.cbl`** -> AI Confidence: **99.48%**
8. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN01C.cbl`** -> AI Confidence: **99.48%**
9. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN02C.cbl`** -> AI Confidence: **99.48%**
10. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR00C.cbl`** -> AI Confidence: **99.48%**
11. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR01C.cbl`** -> AI Confidence: **99.48%**
12. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR02C.cbl`** -> AI Confidence: **99.48%**
13. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COUSR03C.cbl`** -> AI Confidence: **99.48%**
14. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`** -> AI Confidence: **99.48%**
15. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`** -> AI Confidence: **99.39%**
16. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDUPC.cbl`** -> AI Confidence: **99.39%**
17. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSExtractOptionsUtility.java`** -> AI Confidence: **99.39%**
18. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSysSetOptionsCheckUtility.java`** -> AI Confidence: **99.39%**
19. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSWebOptionsCheckUtility.java`** -> AI Confidence: **99.39%**
20. **`server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestReplaceCompilerDirective.java`** -> AI Confidence: **99.39%**
21. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDLIC.cbl`** -> AI Confidence: **99.35%**
22. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSIssueOptionsCheckUtility.java`** -> AI Confidence: **99.35%**
23. **`tests/test_files/cicsGenApp/positive/lgipdb01.cbl`** -> AI Confidence: **99.32%**
24. **`tests/test_files/cicsGenApp/positive/lgupdb01.cbl`** -> AI Confidence: **99.32%**
25. **`clients/analysis/src/graphbuilder.ts`** -> AI Confidence: **99.31%**
26. **`clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts`** -> AI Confidence: **99.31%**
27. **`clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts`** -> AI Confidence: **99.31%**
28. **`clients/cobol-lsp-vscode-extension/src/services/Settings.ts`** -> AI Confidence: **99.31%**
29. **`clients/cobol-lsp-vscode-extension/src/services/copybookLibs/TarCopybookLib.ts`** -> AI Confidence: **99.31%**
30. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTVWC.cbl`** -> AI Confidence: **99.31%**
31. **`tests/test_files/aws-mainframe-modernization-carddemo/positive/COCRDSLC.cbl`** -> AI Confidence: **99.31%**
32. **`server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/VisitorHelper.java`** -> AI Confidence: **99.31%**
33. **`server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/processors/DaCoCopyFromProcessor.java`** -> AI Confidence: **99.31%**
34. **`server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/processors/implicit/TreeScanner.java`** -> AI Confidence: **99.31%**
35. **`server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/IdmsParserHelper.java`** -> AI Confidence: **99.31%**
36. **`server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java`** -> AI Confidence: **99.31%**
37. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/FileOperationProcess.java`** -> AI Confidence: **99.31%**
38. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/JsonGenerateProcess.java`** -> AI Confidence: **99.31%**
39. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/JsonParseProcess.java`** -> AI Confidence: **99.31%**
40. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/QualifiedReferenceUpdateVariableUsage.java`** -> AI Confidence: **99.31%**
41. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/SectionNodeProcessorHelper.java`** -> AI Confidence: **99.31%**
42. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors/XmlGenerateProcess.java`** -> AI Confidence: **99.31%**
43. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/model/NodeUtils.java`** -> AI Confidence: **99.31%**
44. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblParser.java`** -> AI Confidence: **99.31%**
45. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/replacement/SearchPattern.java`** -> AI Confidence: **99.31%**
46. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java`** -> AI Confidence: **99.31%**
47. **`server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/VisitorHelper.java`** -> AI Confidence: **99.31%**
48. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSCsdSpOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
49. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSDefineOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
50. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSDeleteOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
51. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSDocumentOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
52. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSExtractSPOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
53. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSGetOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
54. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSGetnextOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
55. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSHandleOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
56. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSOptionsCheckBaseUtility.java`** -> AI Confidence: **99.31%**
57. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSPerformSPOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
58. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSReceiveOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
59. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSendOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
60. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSStartOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
61. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSTransformOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
62. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSWaitOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
63. **`server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSWriteOptionsCheckUtility.java`** -> AI Confidence: **99.31%**
64. **`server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/SourceUnitGraph.java`** -> AI Confidence: **99.31%**
65. **`server/engine/src/main/java/org/eclipse/lsp/cobol/service/copybooks/CopybookIdentificationServiceBasedOnContent.java`** -> AI Confidence: **99.31%**
66. **`server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/formations/CapitalFormation.java`** -> AI Confidence: **99.31%**
67. **`server/engine/src/main/java/org/eclipse/lsp/cobol/service/settings/ConfigHelper.java`** -> AI Confidence: **99.31%**
68. **`server/engine/src/main/java/org/eclipse/lsp/cobol/service/settings/layout/CodeLayoutStore.java`** -> AI Confidence: **99.31%**
69. **`server/engine/src/main/java/org/eclipse/lsp/cobol/service/utils/BuildOutlineTreeFromSyntaxTree.java`** -> AI Confidence: **99.31%**
70. **`server/engine/src/test/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/util/impl/ReplacingServiceImplTest.java`** -> AI Confidence: **99.31%**
71. **`server/engine/src/test/java/org/eclipse/lsp/cobol/positive/FolderTextRegistry.java`** -> AI Confidence: **99.31%**
72. **`server/engine/src/test/java/org/eclipse/lsp/cobol/positive/PositiveTestUtility.java`** -> AI Confidence: **99.31%**
73. **`server/engine/src/test/java/org/eclipse/lsp/cobol/positive/SnapshotReader.java`** -> AI Confidence: **99.31%**
74. **`server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/sql/TestSqlAllCreateStatements.java`** -> AI Confidence: **99.31%**
75. **`server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/sql/TestSqlAllSetStatements.java`** -> AI Confidence: **99.31%**
76. **`server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/sql/TestSqlInsertStatement.java`** -> AI Confidence: **99.31%**
77. **`server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/sql/TestSqlSelectStatement.java`** -> AI Confidence: **99.31%**
78. **`server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java`** -> AI Confidence: **99.31%**
79. **`clients/analysis/jest.config.js`** -> AI Confidence: **99.29%**
80. **`clients/cobol-lsp-vscode-extension/jest.config.js`** -> AI Confidence: **99.29%**
81. **`clients/analysis/src/utils.ts`** -> AI Confidence: **99.29%**
82. **`clients/cobol-lsp-vscode-extension/src/type/codeLayout.d.ts`** -> AI Confidence: **99.29%**
83. **`clients/analysis/src/__tests__/__resources__/cfgraph/case118.cbl`** -> AI Confidence: **99.29%**
84. **`server/engine/src/main/resources/implicitCopybooks/SQLCA_DATACOM.cpy`** -> AI Confidence: **99.29%**
85. **`server/engine/src/main/resources/implicitCopybooks/SQLCA_DB2.cpy`** -> AI Confidence: **99.29%**
86. **`server/engine/src/main/resources/implicitCopybooks/SQLDA.cpy`** -> AI Confidence: **99.29%**
87. **`server/engine/src/test/resources/ALTL1.CPY`** -> AI Confidence: **99.29%**
88. **`server/engine/src/test/resources/ALTLB.CPY`** -> AI Confidence: **99.29%**
89. **`server/engine/src/test/resources/CM101M.CBL`** -> AI Confidence: **99.29%**
90. **`server/engine/src/test/resources/KP001.CPY`** -> AI Confidence: **99.29%**
91. **`server/engine/src/test/resources/implicitCopybooks/SQLCA_DATACOM.cpy`** -> AI Confidence: **99.29%**
92. **`server/engine/src/test/resources/implicitCopybooks/SQLCA_DB2.cpy`** -> AI Confidence: **99.29%**
93. **`server/engine/src/test/resources/implicitCopybooks/SQLDA.cpy`** -> AI Confidence: **99.29%**
94. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/DB1014.2.cbl`** -> AI Confidence: **99.29%**
95. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/DB1024.2.cbl`** -> AI Confidence: **99.29%**
96. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/DB1034.2.cbl`** -> AI Confidence: **99.29%**
97. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/DB1044.2.cbl`** -> AI Confidence: **99.29%**
98. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC1064.2.cbl`** -> AI Confidence: **99.29%**
99. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC1084.2.cbl`** -> AI Confidence: **99.29%**
100. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC2014.2.cbl`** -> AI Confidence: **99.29%**
101. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC2034.2.cbl`** -> AI Confidence: **99.29%**
102. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC2074.2.cbl`** -> AI Confidence: **99.29%**
103. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC2254.2.cbl`** -> AI Confidence: **99.29%**
104. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1014.2.cbl`** -> AI Confidence: **99.29%**
105. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1024.2.cbl`** -> AI Confidence: **99.29%**
106. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1034.2.cbl`** -> AI Confidence: **99.29%**
107. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1044.2.cbl`** -> AI Confidence: **99.29%**
108. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1054.2.cbl`** -> AI Confidence: **99.29%**
109. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1064.2.cbl`** -> AI Confidence: **99.29%**
110. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1084.2.cbl`** -> AI Confidence: **99.29%**
111. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1094.2.cbl`** -> AI Confidence: **99.29%**
112. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1104.2.cbl`** -> AI Confidence: **99.29%**
113. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1114.2.cbl`** -> AI Confidence: **99.29%**
114. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1124.2.cbl`** -> AI Confidence: **99.29%**
115. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1134.2.cbl`** -> AI Confidence: **99.29%**
116. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1144.2.cbl`** -> AI Confidence: **99.29%**
117. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1154.2.cbl`** -> AI Confidence: **99.29%**
118. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1164.2.cbl`** -> AI Confidence: **99.29%**
119. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1174.2.cbl`** -> AI Confidence: **99.29%**
120. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1184.2.cbl`** -> AI Confidence: **99.29%**
121. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1194.2.cbl`** -> AI Confidence: **99.29%**
122. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1204.2.cbl`** -> AI Confidence: **99.29%**
123. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1214.2.cbl`** -> AI Confidence: **99.29%**
124. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1224.2.cbl`** -> AI Confidence: **99.29%**
125. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1234.2.cbl`** -> AI Confidence: **99.29%**
126. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1244.2.cbl`** -> AI Confidence: **99.29%**
127. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1254.2.cbl`** -> AI Confidence: **99.29%**
128. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1264.2.cbl`** -> AI Confidence: **99.29%**
129. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1274.2.cbl`** -> AI Confidence: **99.29%**
130. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1284.2.cbl`** -> AI Confidence: **99.29%**
131. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1294.2.cbl`** -> AI Confidence: **99.29%**
132. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1304.2.cbl`** -> AI Confidence: **99.29%**
133. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1314.2.cbl`** -> AI Confidence: **99.29%**
134. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1324.2.cbl`** -> AI Confidence: **99.29%**
135. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1334.2.cbl`** -> AI Confidence: **99.29%**
136. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1344.2.cbl`** -> AI Confidence: **99.29%**
137. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1354.2.cbl`** -> AI Confidence: **99.29%**
138. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1364.2.cbl`** -> AI Confidence: **99.29%**
139. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1374.2.cbl`** -> AI Confidence: **99.29%**
140. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1384.2.cbl`** -> AI Confidence: **99.29%**
141. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1394.2.cbl`** -> AI Confidence: **99.29%**
142. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1404.2.cbl`** -> AI Confidence: **99.29%**
143. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1414.2.cbl`** -> AI Confidence: **99.29%**
144. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1024.2.cbl`** -> AI Confidence: **99.29%**
145. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1034.2.cbl`** -> AI Confidence: **99.29%**
146. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1044.2.cbl`** -> AI Confidence: **99.29%**
147. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1054.2.cbl`** -> AI Confidence: **99.29%**
148. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1084.2.cbl`** -> AI Confidence: **99.29%**
149. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1094.2.cbl`** -> AI Confidence: **99.29%**
150. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1124.2.cbl`** -> AI Confidence: **99.29%**
151. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1134.2.cbl`** -> AI Confidence: **99.29%**
152. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1194.2.cbl`** -> AI Confidence: **99.29%**
153. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1214.2.cbl`** -> AI Confidence: **99.29%**
154. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2034.2.cbl`** -> AI Confidence: **99.29%**
155. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2044.2.cbl`** -> AI Confidence: **99.29%**
156. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2054.2.cbl`** -> AI Confidence: **99.29%**
157. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2094.2.cbl`** -> AI Confidence: **99.29%**
158. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2104.2.cbl`** -> AI Confidence: **99.29%**
159. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2114.2.cbl`** -> AI Confidence: **99.29%**
160. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2124.2.cbl`** -> AI Confidence: **99.29%**
161. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2134.2.cbl`** -> AI Confidence: **99.29%**
162. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2144.2.cbl`** -> AI Confidence: **99.29%**
163. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl`** -> AI Confidence: **99.29%**
164. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2164.2.cbl`** -> AI Confidence: **99.29%**
165. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2174.2.cbl`** -> AI Confidence: **99.29%**
166. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2184.2.cbl`** -> AI Confidence: **99.29%**
167. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1014.2.cbl`** -> AI Confidence: **99.29%**
168. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1024.2.cbl`** -> AI Confidence: **99.29%**
169. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1064.2.cbl`** -> AI Confidence: **99.29%**
170. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1114.2.cbl`** -> AI Confidence: **99.29%**
171. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1124.2.cbl`** -> AI Confidence: **99.29%**
172. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1154.2.cbl`** -> AI Confidence: **99.29%**
173. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1164.2.cbl`** -> AI Confidence: **99.29%**
174. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1174.2.cbl`** -> AI Confidence: **99.29%**
175. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1184.2.cbl`** -> AI Confidence: **99.29%**
176. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1194.2.cbl`** -> AI Confidence: **99.29%**
177. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1204.2.cbl`** -> AI Confidence: **99.29%**
178. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1214.2.cbl`** -> AI Confidence: **99.29%**
179. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1224.2.cbl`** -> AI Confidence: **99.29%**
180. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1234.2.cbl`** -> AI Confidence: **99.29%**
181. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1244.2.cbl`** -> AI Confidence: **99.29%**
182. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1264.2.cbl`** -> AI Confidence: **99.29%**
183. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1314.2.cbl`** -> AI Confidence: **99.29%**
184. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1324.2.cbl`** -> AI Confidence: **99.29%**
185. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1334.2.cbl`** -> AI Confidence: **99.29%**
186. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1344.2.cbl`** -> AI Confidence: **99.29%**
187. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1364.2.cbl`** -> AI Confidence: **99.29%**
188. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1374.2.cbl`** -> AI Confidence: **99.29%**
189. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1384.2.cbl`** -> AI Confidence: **99.29%**
190. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1394.2.cbl`** -> AI Confidence: **99.29%**
191. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1404.2.cbl`** -> AI Confidence: **99.29%**
192. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1414.2.cbl`** -> AI Confidence: **99.29%**
193. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1704.2.cbl`** -> AI Confidence: **99.29%**
194. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1714.2.cbl`** -> AI Confidence: **99.29%**
195. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1724.2.cbl`** -> AI Confidence: **99.29%**
196. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1734.2.cbl`** -> AI Confidence: **99.29%**
197. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1754.2.cbl`** -> AI Confidence: **99.29%**
198. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1764.2.cbl`** -> AI Confidence: **99.29%**
199. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1774.2.cbl`** -> AI Confidence: **99.29%**
200. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2014.2.cbl`** -> AI Confidence: **99.29%**
201. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl`** -> AI Confidence: **99.29%**
202. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2054.2.cbl`** -> AI Confidence: **99.29%**
203. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2064.2.cbl`** -> AI Confidence: **99.29%**
204. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2074.2.cbl`** -> AI Confidence: **99.29%**
205. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2094.2.cbl`** -> AI Confidence: **99.29%**
206. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2104.2.cbl`** -> AI Confidence: **99.29%**
207. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2154.2.cbl`** -> AI Confidence: **99.29%**
208. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2164.2.cbl`** -> AI Confidence: **99.29%**
209. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2174.2.cbl`** -> AI Confidence: **99.29%**
210. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2184.2.cbl`** -> AI Confidence: **99.29%**
211. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2194.2.cbl`** -> AI Confidence: **99.29%**
212. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2214.2.cbl`** -> AI Confidence: **99.29%**
213. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2224.2.cbl`** -> AI Confidence: **99.29%**
214. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2234.2.cbl`** -> AI Confidence: **99.29%**
215. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2244.2.cbl`** -> AI Confidence: **99.29%**
216. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2254.2.cbl`** -> AI Confidence: **99.29%**
217. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2314.2.cbl`** -> AI Confidence: **99.29%**
218. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2324.2.cbl`** -> AI Confidence: **99.29%**
219. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2334.2.cbl`** -> AI Confidence: **99.29%**
220. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2344.2.cbl`** -> AI Confidence: **99.29%**
221. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2354.2.cbl`** -> AI Confidence: **99.29%**
222. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2364.2.cbl`** -> AI Confidence: **99.29%**
223. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2374.2.cbl`** -> AI Confidence: **99.29%**
224. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2384.2.cbl`** -> AI Confidence: **99.29%**
225. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2394.2.cbl`** -> AI Confidence: **99.29%**
226. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2404.2.cbl`** -> AI Confidence: **99.29%**
227. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2414.2.cbl`** -> AI Confidence: **99.29%**
228. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2424.2.cbl`** -> AI Confidence: **99.29%**
229. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2434.2.cbl`** -> AI Confidence: **99.29%**
230. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2454.2.cbl`** -> AI Confidence: **99.29%**
231. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2464.2.cbl`** -> AI Confidence: **99.29%**
232. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2474.2.cbl`** -> AI Confidence: **99.29%**
233. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2484.2.cbl`** -> AI Confidence: **99.29%**
234. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2504.2.cbl`** -> AI Confidence: **99.29%**
235. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2514.2.cbl`** -> AI Confidence: **99.29%**
236. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2524.2.cbl`** -> AI Confidence: **99.29%**
237. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2534.2.cbl`** -> AI Confidence: **99.29%**
238. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/OBNC24.2.cbl`** -> AI Confidence: **99.29%**
239. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/OBSQ54.2.cbl`** -> AI Confidence: **99.29%**
240. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/SM1074.2.cbl`** -> AI Confidence: **99.29%**
241. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/ST1084.2.cbl`** -> AI Confidence: **99.29%**
242. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/ST1184.2.cbl`** -> AI Confidence: **99.29%**
243. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/ST1274.2.cbl`** -> AI Confidence: **99.29%**
244. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot/IF4034.2.cbl`** -> AI Confidence: **99.29%**
245. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot/NC1104.2.cbl`** -> AI Confidence: **99.29%**
246. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot/NC2504.2.cbl`** -> AI Confidence: **99.29%**
247. **`tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot/OBNC24.2.cbl`** -> AI Confidence: **99.29%**
248. **`tests/test_files/Cobol85PositiveTestsSuite/negative/NC1074.2.cbl`** -> AI Confidence: **99.29%**
249. **`tests/test_files/Cobol85PositiveTestsSuite/positive/DB1014.2.cbl`** -> AI Confidence: **99.29%**
250. **`tests/test_files/Cobol85PositiveTestsSuite/positive/DB1024.2.cbl`** -> AI Confidence: **99.29%**
251. **`tests/test_files/Cobol85PositiveTestsSuite/positive/DB1034.2.cbl`** -> AI Confidence: **99.29%**
252. **`tests/test_files/Cobol85PositiveTestsSuite/positive/DB1044.2.cbl`** -> AI Confidence: **99.29%**
253. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC1014.2.cbl`** -> AI Confidence: **99.29%**
254. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC1064.2.cbl`** -> AI Confidence: **99.29%**
255. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC1084.2.cbl`** -> AI Confidence: **99.29%**
256. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2014.2.cbl`** -> AI Confidence: **99.29%**
257. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2034.2.cbl`** -> AI Confidence: **99.29%**
258. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2074.2.cbl`** -> AI Confidence: **99.29%**
259. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2094.2.cbl`** -> AI Confidence: **99.29%**
260. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2224.2.cbl`** -> AI Confidence: **99.29%**
261. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2234.2.cbl`** -> AI Confidence: **99.29%**
262. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2254.2.cbl`** -> AI Confidence: **99.29%**
263. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IC2274.2.cbl`** -> AI Confidence: **99.29%**
264. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1014.2.cbl`** -> AI Confidence: **99.29%**
265. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1024.2.cbl`** -> AI Confidence: **99.29%**
266. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1034.2.cbl`** -> AI Confidence: **99.29%**
267. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1044.2.cbl`** -> AI Confidence: **99.29%**
268. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1054.2.cbl`** -> AI Confidence: **99.29%**
269. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1064.2.cbl`** -> AI Confidence: **99.29%**
270. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1074.2.cbl`** -> AI Confidence: **99.29%**
271. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1084.2.cbl`** -> AI Confidence: **99.29%**
272. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1094.2.cbl`** -> AI Confidence: **99.29%**
273. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1104.2.cbl`** -> AI Confidence: **99.29%**
274. **`tests/test_files/Cobol85PositiveTestsSuite/positive/IF1114.2.cbl`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Hardcoded Payload Artifacts
- `tests/test_files/cicsGenApp/positive/lgacdb02.cbl` -> **99.9618%** Exposure
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/TextMapReplacer.java` -> **99.1181%** Exposure
- `tests/test_files/cicsGenApp/positive/lgacdb01.cbl` -> **98.86%** Exposure
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2104.2.cbl` -> **12.8772%** Exposure
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2144.2.cbl` -> **12.7657%** Exposure

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14451` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` (TYPESCRIPT) -> Cumulative Risk: **707.27**
- **Archetype:** `file_cluster_4` (Distance: 13.935 IQR)
- **Magnitude:** 75.59 | **LOC:** 559 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9999%), Tech Debt (95.7912%)
- **Heaviest Functions:** `finishTask` (Impact: 41.8), `start` (Impact: 35.3), `finishTaskWithError` (Impact: 30.6)

### 2. `clients/cobol-lsp-vscode-extension/src/services/copybook/downloader/ZoweExplorerDownloader.ts` (TYPESCRIPT) -> Cumulative Risk: **695.85**
- **Archetype:** `file_cluster_4` (Distance: 11.787 IQR)
- **Magnitude:** 11.64 | **LOC:** 110 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.8814%)
- **Heaviest Functions:** `request` (Impact: 18.7), `hasMember` (Impact: 7.5), `fsChanged` (Impact: 4.6)

### 3. `clients/cobol-lsp-vscode-extension/src/services/snippetcompletion/SnippetCompletionProvider.ts` (TYPESCRIPT) -> Cumulative Risk: **681.87**
- **Archetype:** `file_cluster_4` (Distance: 11.32 IQR)
- **Magnitude:** 15.37 | **LOC:** 252 | **CtrlFlow:** 30.2% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9649%), Tech Debt (92.4142%), State Flux (86.9892%)
- **Heaviest Functions:** `provideCompletionItems` (Impact: 15.0), `pickSnippet` (Impact: 13.8), `importDialectSnippets` (Impact: 8.9)

### 4. `clients/analysis/src/vm/listing.ts` (TYPESCRIPT) -> Cumulative Risk: **624.35**
- **Archetype:** `file_cluster_8` (Distance: 13.424 IQR)
- **Magnitude:** 101.19 | **LOC:** 888 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9323%), Safety Score (99.2381%)
- **Heaviest Functions:** `addInstructionsForNode` (Impact: 104.3), `processPlaceholders` (Impact: 47.3), `addChildren` (Impact: 19.4)

### 5. `clients/cobol-lsp-vscode-extension/src/services/util/Memoize.ts` (TYPESCRIPT) -> Cumulative Risk: **620.56**
- **Archetype:** `file_cluster_4` (Distance: 14.587 IQR)
- **Magnitude:** 8.91 | **LOC:** 59 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `execute` (Impact: 14.3), `invalidateCache` (Impact: 2.4), `string` (Impact: 1.9)

### 6. `clients/analysis/src/vm/vm.ts` (TYPESCRIPT) -> Cumulative Risk: **620.54**
- **Archetype:** `file_cluster_13` (Distance: 13.834 IQR)
- **Magnitude:** 44.86 | **LOC:** 528 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (98.3708%), Safety Score (95.9364%)
- **Heaviest Functions:** `equals` (Impact: 21.7), `deactivatePerform` (Impact: 17.1), `setCurrentProgramUnitByPosition` (Impact: 12.8)

### 7. `clients/cobol-lsp-vscode-extension/src/services/copybook/ZoweThrottling.ts` (TYPESCRIPT) -> Cumulative Risk: **606.31**
- **Archetype:** `file_cluster_4` (Distance: 14.678 IQR)
- **Magnitude:** 8.78 | **LOC:** 42 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `locked` (Impact: 16.4), `constructor` (Impact: 6.9)

### 8. `clients/cobol-lsp-vscode-extension/src/services/worker/Worker.ts` (TYPESCRIPT) -> Cumulative Risk: **601.62**
- **Archetype:** `file_cluster_4` (Distance: 12.183 IQR)
- **Magnitude:** 8.31 | **LOC:** 129 | **CtrlFlow:** 29.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9993%), State Flux (99.7183%), Cognitive Load (96.8877%)
- **Heaviest Functions:** `processMessage` (Impact: 12.3), `sendMessagesIfNeeded` (Impact: 4.3), `postMessage` (Impact: 4.2)

### 9. `clients/cobol-lsp-vscode-extension/src/services/copybook/downloader/CopybookBinaryDownloader.ts` (TYPESCRIPT) -> Cumulative Risk: **593.35**
- **Archetype:** `file_cluster_4` (Distance: 11.326 IQR)
- **Magnitude:** 8.44 | **LOC:** 81 | **CtrlFlow:** 32.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `downloadFile` (Impact: 12.9), `isPresentLocally` (Impact: 12.9), `constructor` (Impact: 2.2)

### 10. `clients/analysis/src/graphbuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **589.23**
- **Archetype:** `file_cluster_8` (Distance: 11.637 IQR)
- **Magnitude:** 29.54 | **LOC:** 425 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.7644%), Tech Debt (85.9404%), Verification (80.0%)
- **Heaviest Functions:** `report` (Impact: 37.1), `collectDeadCodeDiagnostics` (Impact: 36.2), `getLabel` (Impact: 26.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `clients/cobol-lsp-vscode-extension/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/telemetry.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.569 IQR)
- **Top Global Matches:** file_cluster_8: 14.569, file_cluster_11: 14.902, file_cluster_7: 14.931
- **Magnitude:** 4294.12 | **LOC:** 2415 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.7791%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DNAME42` (Impact: 652.1)
  * `SECT-NC176A-001` (Impact: 152.0)
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 836`, `structural_boundaries: 23`, `func_start: 38`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `high_risk_execution: 1`, `state_mutation: 3347`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 18`
* *Architecture:* `io: 255`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.499 IQR)
- **Top Global Matches:** file_cluster_8: 14.499, file_cluster_11: 14.84, file_cluster_7: 14.866
- **Magnitude:** 3854.06 | **LOC:** 2135 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8467%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WRK-DU-18V00` (Impact: 605.2)
  * `SECT-NC177A-001` (Impact: 146.2)
  * `ERROR-HOLD` (Impact: 27.1)
  * `WRK-DS-18V00` (Impact: 18.4)
  * `PRINT-DETAIL` (Impact: 9.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 754`, `structural_boundaries: 20`, `func_start: 40`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 125`, `high_risk_execution: 1`, `state_mutation: 2940`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 21`
* *Architecture:* `io: 187`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.117 IQR)
- **Top Global Matches:** file_cluster_8: 14.117, file_cluster_7: 14.502, file_cluster_13: 14.557
- **Magnitude:** 3818.84 | **LOC:** 3265 | **CtrlFlow:** 94.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9035%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `phrase` (Impact: 374.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 469`, `structural_boundaries: 25`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 274`, `high_risk_execution: 3`, `state_mutation: 3378`, `fragile_debt: 3`
* *Architecture:* `io: 500`, `api: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2024.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.567 IQR)
- **Top Global Matches:** file_cluster_8: 14.567, file_cluster_11: 14.9, file_cluster_13: 14.925
- **Magnitude:** 3772.88 | **LOC:** 2217 | **CtrlFlow:** 95.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.0362%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BUILD-TABLE2` (Impact: 324.6)
  * `SECT-NC202A-001` (Impact: 164.3)
  * `ERROR-HOLD` (Impact: 19.9)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 465`, `structural_boundaries: 20`, `func_start: 31`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 263`, `high_risk_execution: 1`, `state_mutation: 3158`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 20`
* *Architecture:* `io: 342`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1764.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.94 IQR)
- **Top Global Matches:** file_cluster_8: 13.94, file_cluster_7: 14.442, file_cluster_13: 14.49
- **Magnitude:** 3528.54 | **LOC:** 3301 | **CtrlFlow:** 96.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.7044%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 843`, `structural_boundaries: 28`
* *Risk/State:* `safety_bypasses: 164`, `high_risk_execution: 3`, `state_mutation: 3446`, `fragile_debt: 3`
* *Architecture:* `io: 375`, `api: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1244.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.78 IQR)
- **Top Global Matches:** file_cluster_8: 13.78, file_cluster_7: 14.244, file_cluster_13: 14.308
- **Magnitude:** 3419.24 | **LOC:** 2352 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.1912%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PICTURE-TEST-26-C` (Impact: 13.8)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `PICTURE-TEST-1-A` (Impact: 7.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1128`, `structural_boundaries: 19`, `func_start: 316`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 83`, `high_risk_execution: 1`, `state_mutation: 1828`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 5`, `orphaned_logic: 300`
* *Architecture:* `io: 96`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1064.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.824 IQR)
- **Top Global Matches:** file_cluster_8: 13.824, file_cluster_7: 14.275, file_cluster_11: 14.308
- **Magnitude:** 3202.58 | **LOC:** 2531 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.0447%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `SUB-TEST-F1-20` (Impact: 8.8)
  * `SUB-TEST-F1-34-1` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 849`, `structural_boundaries: 23`, `func_start: 358`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 1`, `state_mutation: 1862`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 337`
* *Architecture:* `io: 267`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1774.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.853 IQR)
- **Top Global Matches:** file_cluster_8: 13.853, file_cluster_7: 14.36, file_cluster_13: 14.412
- **Magnitude:** 3092.6 | **LOC:** 2902 | **CtrlFlow:** 96.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.0515%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 759`, `structural_boundaries: 25`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 3`, `state_mutation: 3018`, `fragile_debt: 3`
* *Architecture:* `io: 274`, `api: 2`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.279 IQR)
- **Top Global Matches:** file_cluster_8: 13.279, file_cluster_7: 13.684, file_cluster_11: 13.734
- **Magnitude:** 3011.86 | **LOC:** 3636 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.037%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `definition` (Impact: 919.5)
  * `definition` (Impact: 1.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 773`, `structural_boundaries: 120`, `args: 1`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 261`, `high_risk_execution: 3`, `state_mutation: 2017`, `fragile_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `io: 1410`, `api: 2`
* *Defense:* `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2184.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.385 IQR)
- **Top Global Matches:** file_cluster_8: 13.385, file_cluster_7: 13.861, file_cluster_11: 13.9
- **Magnitude:** 3009.62 | **LOC:** 3074 | **CtrlFlow:** 97.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.2321%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 19.9)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `XXXXX055` (Impact: 8.0)
  * `COLUMN-NAMES-ROUTINE` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 21`, `func_start: 597`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 420`, `high_risk_execution: 1`, `state_mutation: 1386`, `dead_code: 1`, `fragile_debt: 18`, `orphaned_logic: 585`
* *Architecture:* `io: 547`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2154.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.77 IQR)
- **Top Global Matches:** file_cluster_8: 13.77, file_cluster_11: 14.098, file_cluster_0: 14.163
- **Magnitude:** 2906.72 | **LOC:** 2803 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.7198%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `START-WRITE-GF-18` (Impact: 35.6)
  * `START-TERM-003` (Impact: 33.5)
  * `SECT-0001-IX215A` (Impact: 32.2)
  * `ERROR-HOLD` (Impact: 27.1)
  * `START-TEST-GF-22` (Impact: 14.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 761`, `structural_boundaries: 102`, `func_start: 181`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 258`, `high_risk_execution: 1`, `state_mutation: 2109`, `dead_code: 3`, `fragile_debt: 6`, `orphaned_logic: 171`
* *Architecture:* `io: 1150`, `api: 1`
* *Defense:* `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1714.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.704 IQR)
- **Top Global Matches:** file_cluster_8: 13.704, file_cluster_7: 14.165, file_cluster_11: 14.219
- **Magnitude:** 2855.72 | **LOC:** 2266 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.5442%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `DIV-TEST-F1-15-1` (Impact: 8.7)
  * `DIV-TEST-F1-14-2` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 786`, `structural_boundaries: 21`, `func_start: 267`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 1680`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 254`
* *Architecture:* `io: 135`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1734.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.73 IQR)
- **Top Global Matches:** file_cluster_8: 13.73, file_cluster_7: 14.19, file_cluster_11: 14.243
- **Magnitude:** 2824.04 | **LOC:** 2216 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.4443%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `DIV-TEST-F3-27-2` (Impact: 8.7)
  * `DIV-TEST-F3-27-3` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 757`, `structural_boundaries: 21`, `func_start: 252`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 1`, `state_mutation: 1696`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 237`
* *Architecture:* `io: 121`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1724.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.716 IQR)
- **Top Global Matches:** file_cluster_8: 13.716, file_cluster_7: 14.176, file_cluster_11: 14.228
- **Magnitude:** 2786.66 | **LOC:** 2213 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.2903%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `DIV-TEST-F2-26-1` (Impact: 8.7)
  * `DIV-TEST-F2-26-2` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 744`, `structural_boundaries: 21`, `func_start: 259`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 92`, `high_risk_execution: 1`, `state_mutation: 1665`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 245`
* *Architecture:* `io: 131`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1264.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.325 IQR)
- **Top Global Matches:** file_cluster_8: 13.325, file_cluster_7: 13.794, file_cluster_11: 13.824
- **Magnitude:** 2746.76 | **LOC:** 2634 | **CtrlFlow:** 91.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.1389%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `BREAKDOWN-PARA` (Impact: 21.3)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `COLUMN-NAMES-ROUTINE` (Impact: 7.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 862`, `structural_boundaries: 78`, `func_start: 470`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 307`, `high_risk_execution: 1`, `state_mutation: 1318`, `dead_code: 1`, `fragile_debt: 4`, `orphaned_logic: 457`
* *Architecture:* `io: 618`, `api: 1`
* *Defense:* `safety: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.125 IQR)
- **Top Global Matches:** file_cluster_8: 14.125, file_cluster_13: 14.139, file_cluster_11: 14.181
- **Magnitude:** 2677.64 | **LOC:** 4245 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (47.2627%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` (Impact: 163.7)
  * `3300-SETUP-SCREEN-ATTRS` (Impact: 110.3)
  * `1200-EDIT-MAP-INPUTS` (Impact: 60.8)
  * `0000-MAIN` (Impact: 32.1)
  * `2000-DECIDE-ACTION` (Impact: 30.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 238`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1750`, `dead_code: 14`, `fragile_debt: 1`, `orphaned_logic: 99`
* *Architecture:* `io: 101`, `api: 1`, `import: 56`
* *Defense:* `safety: 177`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` CVACT03Y, CVCUS01Y, CSDAT01Y, COACTUP, CSSTRPFY, CSMSG02Y, COTTL01Y, CVCRD01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_7: 13.236, file_cluster_11: 13.283
- **Magnitude:** 2628.02 | **LOC:** 1969 | **CtrlFlow:** 98.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.4182%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FAIL` (Impact: 874.1)
  * `SECT-NC201A-001` (Impact: 517.3)
  * `XXXXX055` (Impact: 76.3)
  * `FAIL` (Impact: 37.5)
  * `BUMMER-122` (Impact: 34.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1532`, `structural_boundaries: 24`, `func_start: 32`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 147`, `high_risk_execution: 1`, `state_mutation: 973`, `dead_code: 1`, `fragile_debt: 28`, `duplicate_logic: 2`, `orphaned_logic: 19`
* *Architecture:* `io: 404`
* *Defense:* `safety: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2094.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_11: 14.14, file_cluster_0: 14.171
- **Magnitude:** 2585.48 | **LOC:** 2854 | **CtrlFlow:** 93.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.4562%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `SECT-0001-IX209A` (Impact: 32.1)
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `START-TEST-GF-01` (Impact: 8.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 582`, `structural_boundaries: 39`, `func_start: 228`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `high_risk_execution: 1`, `state_mutation: 1663`, `dead_code: 5`, `fragile_debt: 3`, `orphaned_logic: 217`
* *Architecture:* `io: 848`, `api: 1`
* *Defense:* `cleanup: 10`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1754.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.652 IQR)
- **Top Global Matches:** file_cluster_8: 13.652, file_cluster_7: 14.11, file_cluster_11: 14.15
- **Magnitude:** 2568.8 | **LOC:** 2077 | **CtrlFlow:** 97.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.9564%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `SUB-TEST-F2-34-1` (Impact: 8.7)
  * `SUB-TEST-F2-34-2` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 684`, `structural_boundaries: 21`, `func_start: 275`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 126`, `high_risk_execution: 1`, `state_mutation: 1500`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 255`
* *Architecture:* `io: 187`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1014.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.792 IQR)
- **Top Global Matches:** file_cluster_8: 13.792, file_cluster_7: 14.246, file_cluster_11: 14.263
- **Magnitude:** 2540.54 | **LOC:** 1864 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5772%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `MPY-TEST-F1-14-1` (Impact: 8.7)
  * `MPY-TEST-F1-16-1` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 21`, `func_start: 246`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 1501`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 233`
* *Architecture:* `io: 127`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1704.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.657 IQR)
- **Top Global Matches:** file_cluster_8: 13.657, file_cluster_7: 14.118, file_cluster_11: 14.161
- **Magnitude:** 2537.3 | **LOC:** 2013 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.6154%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 27.1)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
  * `MPY-TEST-F2-17-2` (Impact: 8.7)
  * `MPY-TEST-F2-19-2` (Impact: 8.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 21`, `func_start: 265`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 1`, `state_mutation: 1467`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 253`
* *Architecture:* `io: 139`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/SM1074.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.535 IQR)
- **Top Global Matches:** file_cluster_8: 13.535, file_cluster_7: 14.07, file_cluster_13: 14.166
- **Magnitude:** 2424.98 | **LOC:** 2523 | **CtrlFlow:** 94.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.7747%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 461`, `structural_boundaries: 25`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 3`, `state_mutation: 2358`, `fragile_debt: 3`
* *Architecture:* `io: 45`, `api: 2`, `import: 1`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2074.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.305 IQR)
- **Top Global Matches:** file_cluster_8: 13.305, file_cluster_7: 13.751, file_cluster_13: 13.839
- **Magnitude:** 2347.8 | **LOC:** 2720 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.809%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `COMPUTED-N` (Impact: 87.2)
  * `ERROR-HOLD` (Impact: 19.9)
  * `COMPUTED-N` (Impact: 11.5)
  * `PRINT-DETAIL` (Impact: 9.6)
  * `HEAD-ROUTINE` (Impact: 9.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 20`, `func_start: 346`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 272`, `high_risk_execution: 1`, `state_mutation: 1370`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 17`, `orphaned_logic: 318`
* *Architecture:* `io: 378`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/test_files/cicsGenApp/positive/lgucus01.cbl` (COBOL) | Magnitude: 59.68 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 39, structural_boundaries: 13, branch: 11
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IC2224.2.cbl` (COBOL) | Magnitude: 1056.7 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 543, api: 179, branch: 178, io: 70
- `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/CSUTLDPY.cpy` (COBOL) | Magnitude: 16.81 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 288, state_mutation: 203, branch: 78, structural_boundaries: 40
- `tests/test_files/project/ADSORT.cbl` (COBOL) | Magnitude: 46.66 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 28, branch: 9, structural_boundaries: 7
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IC2244.2.cbl` (COBOL) | Magnitude: 607.16 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 322, branch: 117, api: 85, io: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/test_files/cicsGenApp/positive/lgicdb01.cbl` (COBOL) | Magnitude: 90.76 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 61, branch: 18, structural_boundaries: 13
- `tests/test_files/cicsGenApp/positive/lgapol01.cbl` (COBOL) | Magnitude: 60.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 37, branch: 14, structural_boundaries: 12
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2474.2.cbl` (COBOL) | Magnitude: 903.34 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 528, branch: 217, io: 123, func_start: 121
- `tests/test_files/cicsGenApp/positive/lgdpol01.cbl` (COBOL) | Magnitude: 70.42 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 45, branch: 16, structural_boundaries: 13
- `tests/test_files/cicsGenApp/positive/lgupol01.cbl` (COBOL) | Magnitude: 98.36 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 66, branch: 21, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSAsktime.java` (JAVA) | Magnitude: 8.72 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, import: 9, args: 3
- `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/sql/Db2ErrorStrategy.java` (JAVA) | Magnitude: 17.32 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 17, encapsulation: 7, import: 6
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestDefinitionOnLongCopybooks.java` (JAVA) | Magnitude: 17.24 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 49, structural_boundaries: 37, import: 18, branch: 6
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/settings/layout/CodeLayoutUtil.java` (JAVA) | Magnitude: 9.5 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 27, structural_boundaries: 9, doc: 9, safety: 6
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestErrorRecovery.java` (JAVA) | Magnitude: 12.24 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, import: 12, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/formations/Formation.java` (JAVA) | Magnitude: 18.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, generics: 3, import: 3, args: 1
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variable/VariableDefinitionNode.java` (JAVA) | Magnitude: 155.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, structural_boundaries: 52, api: 46, doc: 45
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/pipeline/Pipeline.java` (JAVA) | Magnitude: 28.1 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, branch: 9, state_mutation: 6
- `server/engine/src/test/java/org/eclipse/lsp/cobol/positive/CobolTextRegistry.java` (JAVA) | Magnitude: 27.76 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 7, indent_spaces: 6, func_start: 4
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` (JAVA) | Magnitude: 212.64 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 367, branch: 88, structural_boundaries: 71, args: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/processor/CompilerDirectiveContext.java` (JAVA) | Magnitude: 35.78 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, args: 15, comprehensions: 13, structural_boundaries: 11
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/settings/SettingsServiceImpl.java` (JAVA) | Magnitude: 103.1 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 38, args: 29, branch: 27
- `tests/test_files/Cobol85PositiveTestsSuite/positive/EXEC84.2.cbl` (COBOL) | Magnitude: 1403.82 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 778, branch: 418, structural_boundaries: 215, func_start: 204
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/references/ElementOccurrences.java` (JAVA) | Magnitude: 26.7 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 30, comprehensions: 21, branch: 18
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1384.2.cbl` (COBOL) | Magnitude: 667.26 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 401, branch: 143, func_start: 102, io: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `clients/cobol-lsp-vscode-extension/src/services/copybook/E4ECopybookService.ts` (TYPESCRIPT) | Magnitude: 2.56 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 12, args: 11, func_start: 11, generics: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `clients/cobol-lsp-vscode-extension/src/test/runTest.ts` (TYPESCRIPT) | Magnitude: 2.68 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, io: 14, structural_boundaries: 8, concurrency: 8
- `clients/cobol-lsp-vscode-extension/src/test/suite/index.ts` (TYPESCRIPT) | Magnitude: 1.72 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, args: 6, concurrency: 5
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/ControlFlowService.spec.ts` (TYPESCRIPT) | Magnitude: 12.81 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 43, args: 39, func_start: 34
- `clients/cobol-lsp-vscode-extension/src/services/snippetcompletion/SnippetCompletionProvider.ts` (TYPESCRIPT) | Magnitude: 15.37 | Delta: **0.054 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 44, state_mutation: 38, immutability_locks: 33
- `tests/test_files/cicsGenApp/positive/lgicvs01.cbl` (COBOL) | Magnitude: 116.9 | Delta: **0.116 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 180, state_mutation: 69, io: 30, branch: 23

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/LanguageEngineFacade.java` (JAVA) | Magnitude: 20.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCasePreprocessorListener.java` (JAVA) | Magnitude: 372.66 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 126, args: 80, func_start: 74
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN01C.cbl` (COBOL) | Magnitude: 212.52 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 231, state_mutation: 140, branch: 52, structural_boundaries: 10
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSConditionCanBeUsedForVariableDeclaration.java` (JAVA) | Magnitude: 7.68 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, import: 6, args: 2
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ReplaceStrategy.java` (JAVA) | Magnitude: 17.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, import: 2, indent_spaces: 2
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/model/extendedapi/Program.java` (JAVA) | Magnitude: 4.14 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, api: 2, decorators: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `clients/cobol-lsp-vscode-extension/src/commands/UpdateCobolProgramRuler.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 7
- `clients/analysis/src/__tests__/__resources__/cfgraph/case60.cbl` (COBOL) | Magnitude: 5.58 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, branch: 4, func_start: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `clients/cobol-lsp-vscode-extension/src/extension.ts` -> Churn: **100.0%** | Cog Load: 18.4421% | Debt: 91.5641%
- `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` -> Churn: **80.86%** | Cog Load: 94.9997% | Debt: 95.7912%
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblParser.java` -> Churn: **64.82%** | Cog Load: 14.5812% | Debt: 99.3954%
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ExtendedDocument.java` -> Churn: **54.02%** | Cog Load: 7.1064% | Debt: 99.978%
- `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` -> Churn: **53.62%** | Cog Load: 72.6018% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCasePreprocessorListener.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 372.66
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblParser.java` -> **Iurii Shchekochikhin** (100.0% isolated ownership) | Magnitude: 312.64
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSendStatement.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 301.34
- `server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/SourceUnitGraph.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 294.98
- `server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java` -> **Hizir** (100.0% isolated ownership) | Magnitude: 278.24

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variable/VariableNode.java` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/IdmsDialect.java` -> **Severity: 0.025** (Bridge: 0.0003 * Flux: 88.0797%)
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/common/CICSTestUtils.java` -> **Severity: 0.018** (Bridge: 0.0002 * Flux: 100.0%)
- `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` -> **Severity: 0.014** (Bridge: 0.0001 * Flux: 100.0%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/symbols/SymbolAccumulator.java` -> **Severity: 0.012** (Bridge: 0.0002 * Flux: 68.9145%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/Node.java` -> **Severity: 772.595** (Blast Radius: 9.189 * Doc Risk: 84.0783%)
- `clients/cobol-lsp-vscode-extension/src/constants.ts` -> **Severity: 737.0** (Blast Radius: 7.37 * Doc Risk: 100.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java` -> **Severity: 674.223** (Blast Radius: 16.022 * Doc Risk: 42.0811%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 602.856** (Blast Radius: 11.02 * Doc Risk: 54.7056%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/copybook/CopybookProcessingMode.java` -> **Severity: 570.057** (Blast Radius: 8.131 * Doc Risk: 70.1091%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
