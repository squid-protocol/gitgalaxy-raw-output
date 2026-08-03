# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_cobol/che-che4z-lsp-for-cobol` |
| **Timestamp** | `2026-08-03T19:28:26.242861+00:00` |
| **Scan Duration** | `22.83s` |
| **Git Branch** | `development` |
| **Git Commit** | `dd1133952579575082914476fa699667b8790e1d` |
| **Git Remote** | `https://github.com/eclipse/che-che4z-lsp-for-cobol.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 2749 malicious artifacts.

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
> **Architectural Drift Z-Score:** `6.383`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 2239 | 71.6% |
| file_cluster_13 | 714 | 22.8% |
| file_cluster_4 | 45 | 1.4% |
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
| Cognitive Load Exposure | 0.0 | 100.0 | 14.5 | 5.0 | 0.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 28.2 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 9.4 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.4 | 0.0 | 0.0 |
| API Exposure | 0.0 | 18.0 | 2.5 | 0.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 6.1 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 99.9 | 0.6 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 94.2 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 11.8 | 0.6 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 1.7 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 21.5 | 0.0 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 16.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 8.0 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
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

- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl`) -> Impact: **2834.6** | LOC: 3071
- `FAIL` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl`) -> Impact: **1708.2** | LOC: 803
- `checkOptions` (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`) -> Impact: **1640.5** | LOC: 707
- `DNAME42` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl`) -> Impact: **1243.2** | LOC: 1223
- `WRK-DU-18V00` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl`) -> Impact: **1153.2** | LOC: 1144
- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1084.2.cbl`) -> Impact: **1115.5** | LOC: 1590
- `phrase` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2534.2.cbl`) -> Impact: **1073.2** | LOC: 1653
- `phrase` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl`) -> Impact: **1064.2** | LOC: 1965
- `1100-RECEIVE-MAP` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> Impact: **1045.7** | LOC: 334
- `checkOptions` (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSysSetOptionsCheckUtility.java`) -> Impact: **871.5** | LOC: 205

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `EDIT-MONTH` (@ `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/CSUTLDPY.cpy`) -> **O(2^N) [Recursive]**
- `EDIT-DAY` (@ `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/CSUTLDPY.cpy`) -> **O(2^N) [Recursive]**
- `1100-RECEIVE-MAP` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `1200-EDIT-MAP-INPUTS` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `9600-WRITE-PROCESSING` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `1245-EDIT-NUM-REQD` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `9000-READ-ACCT` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `1210-EDIT-ACCOUNT` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `1230-EDIT-ALPHANUM-REQD` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**
- `1225-EDIT-ALPHA-REQD` (@ `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl`) -> DB Complexity: **4743**
- `phrase` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl`) -> DB Complexity: **2490**
- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1084.2.cbl`) -> DB Complexity: **1953**
- `BUILD-TABLE2` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2024.2.cbl`) -> DB Complexity: **1567**
- `DNAME42` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl`) -> DB Complexity: **1134**
- `definition` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1054.2.cbl`) -> DB Complexity: **1121**
- `phrase` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2534.2.cbl`) -> DB Complexity: **1066**
- `WRK-DU-18V00` (@ `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl`) -> DB Complexity: **923**
- `put` (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`) -> DB Complexity: **879**
- `operands` (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2524.2.cbl`) -> DB Complexity: **856**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `tests/test_files/Cobol85PositiveTestsSuite/positive` | 233 | 201082.32 | 37.17% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/compileListing` | 233 | 148081.1 | 29.45% | 0.0% |
| `tests/test_files/aws-mainframe-modernization-carddemo/positive` | 26 | 22423.7 | 42.03% | 0.0% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility` | 109 | 13842.38 | 21.58% | 34.38% |
| `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases` | 404 | 12982.42 | 4.49% | 0.0% |
| `clients/cobol-lsp-vscode-extension` | 9 | 10094.96 | 2.43% | 0.0% |
| `tests/test_files/cicsGenApp/positive` | 31 | 5991.82 | 44.52% | 0.0% |
| `clients/analysis/src/__tests__/__resources__/cfgraph` | 321 | 5670.76 | 16.1% | 15.16% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/processors` | 39 | 4883.9 | 13.01% | 61.88% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor` | 7 | 3673.8 | 8.18% | 36.11% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/verify_musl_setup.sh` -> **100.0%** Exposure
- `delombok.sh` -> **100.0%** Exposure
- `clients/analysis/src/vm/instructions.ts` -> **100.0%** Exposure
- `clients/sample-dialect-support/src/__mocks__/vscode.ts` -> **100.0%** Exposure
- `clients/analysis/src/__tests__/__resources__/cfgraph/case102.cbl` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `clients/analysis/src/model/Graph.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/listing.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/utils.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/vm.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/vp.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1064.2.cbl` -> **240** Orphaned Functions | **8** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1164.2.cbl` -> **248** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1214.2.cbl` -> **248** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1244.2.cbl` -> **244** Orphaned Functions | **4** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1264.2.cbl` -> **248** Orphaned Functions | **0** Duplicates

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

### Exploit Generation Surface
- `clients/analysis/src/graphbuilder.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/listing.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/ProcessorGroups.spec.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/commands/CommentCommand.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/commands/SmartTabCommand.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `clients/analysis/src/vm/instructions.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/commands/SmartTabCommand.ts` -> **100.0%** Exposure
- `clients/daco-dialect-support/src/test/runTest.ts` -> **100.0%** Exposure
- `clients/idms-dialect-support/src/test/runTest.ts` -> **100.0%** Exposure
- `tests/test_files/Cobol85PositiveTestsSuite/compileListing/DB1014.2.cbl` -> **100.0%** Exposure
### Hardcoded Payload Artifacts
- `tests/test_files/cicsGenApp/positive/lgacdb02.cbl` -> **99.9618%** Exposure
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/TextMapReplacer.java` -> **99.1181%** Exposure
- `tests/test_files/cicsGenApp/positive/lgacdb01.cbl` -> **98.86%** Exposure
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2104.2.cbl` -> **12.8772%** Exposure
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2144.2.cbl` -> **12.7657%** Exposure
### Algorithmic DoS Exposure
- `clients/analysis/src/graphbuilder.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/instructions.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/listing.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/optimizer.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/utils.ts` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `14451` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` (TYPESCRIPT) -> Cumulative Risk: **922.53**
- **Archetype:** `file_cluster_4` (Distance: 13.943 IQR)
- **Magnitude:** 82.6 | **LOC:** 559 | **CtrlFlow:** 61.8% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `start` (Impact: 67.8), `finishTask` (Impact: 65.2), `finishTaskWithError` (Impact: 45.1)

### 2. `clients/cobol-lsp-vscode-extension/src/services/LanguageClientService.ts` (TYPESCRIPT) -> Cumulative Risk: **893.74**
- **Archetype:** `file_cluster_4` (Distance: 11.569 IQR)
- **Magnitude:** 23.75 | **LOC:** 275 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 40.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `start` (Impact: 13.9), `infoUserAboutRuntimeAbilities` (Impact: 12.8), `createServerOptions` (Impact: 10.7)

### 3. `clients/cobol-lsp-vscode-extension/src/services/copybook/downloader/CopybookDownloaderForUss.ts` (TYPESCRIPT) -> Cumulative Risk: **878.66**
- **Archetype:** `file_cluster_4` (Distance: 12.109 IQR)
- **Magnitude:** 11.97 | **LOC:** 82 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getAllMembers` (Impact: 64.0), `constructor` (Impact: 1.6)

### 4. `clients/cobol-lsp-vscode-extension/src/services/copybook/downloader/ZoweExplorerDownloader.ts` (TYPESCRIPT) -> Cumulative Risk: **875.85**
- **Archetype:** `file_cluster_4` (Distance: 11.842 IQR)
- **Magnitude:** 17.82 | **LOC:** 110 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `request` (Impact: 88.0), `fsChanged` (Impact: 4.6), `hasMember` (Impact: 3.1)

### 5. `clients/analysis/src/vm/listing.ts` (TYPESCRIPT) -> Cumulative Risk: **835.27**
- **Archetype:** `file_cluster_8` (Distance: 13.432 IQR)
- **Magnitude:** 117.09 | **LOC:** 888 | **CtrlFlow:** 48.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addInstructionsForNode` (Impact: 196.3), `processPlaceholders` (Impact: 87.1), `addChildren` (Impact: 55.4)

### 6. `clients/analysis/src/vm/instructions.ts` (TYPESCRIPT) -> Cumulative Risk: **830.29**
- **Archetype:** `file_cluster_8` (Distance: 12.317 IQR)
- **Magnitude:** 38.84 | **LOC:** 540 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getLocation` (Impact: 24.6), `execute` (Impact: 21.3), `execute` (Impact: 13.7)

### 7. `clients/analysis/src/graphbuilder.ts` (TYPESCRIPT) -> Cumulative Risk: **815.75**
- **Archetype:** `file_cluster_8` (Distance: 11.643 IQR)
- **Magnitude:** 38.25 | **LOC:** 425 | **CtrlFlow:** 55.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `report` (Impact: 76.2), `collectDeadCodeDiagnostics` (Impact: 59.2), `getLabel` (Impact: 38.6)

### 8. `server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/SourceUnitGraph.java` (JAVA) -> Cumulative Risk: **809.99**
- **Archetype:** `file_cluster_13` (Distance: 12.43 IQR)
- **Magnitude:** 487.88 | **LOC:** 398 | **CtrlFlow:** 47.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `remove` (Impact: 69.7), `notifyState` (Impact: 47.5), `updateGraphLink` (Impact: 41.9)

### 9. `clients/cobol-lsp-vscode-extension/src/services/copybook/downloader/CopybookDownloaderForDsn.ts` (TYPESCRIPT) -> Cumulative Risk: **800.18**
- **Archetype:** `file_cluster_4` (Distance: 11.479 IQR)
- **Magnitude:** 6.33 | **LOC:** 67 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `getAllMembers` (Impact: 9.8), `constructor` (Impact: 1.6)

### 10. `clients/cobol-lsp-vscode-extension/src/dialect/DialectService.ts` (TYPESCRIPT) -> Cumulative Risk: **797.94**
- **Archetype:** `file_cluster_8` (Distance: 10.842 IQR)
- **Magnitude:** 25.48 | **LOC:** 426 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (99.9619%), Algorithmic Dos (99.2874%)
- **Heaviest Functions:** `constructor` (Impact: 37.9), `serializeContext` (Impact: 25.5), `serializeResults` (Impact: 14.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.125 IQR)
- **Top Global Matches:** file_cluster_8: 14.125, file_cluster_13: 14.139, file_cluster_11: 14.181
- **Magnitude:** 5680.14 | **LOC:** 4245 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 110
- **Risk Profile:** Cognitive Load (47.2627%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` (Impact: 1045.7 | O(2^N) | DB: 110)
  * `3300-SETUP-SCREEN-ATTRS` (Impact: 620.3 | O(2^N) | DB: 65)
  * `1200-EDIT-MAP-INPUTS` (Impact: 354.8 | O(2^N) | DB: 101)
  * `9600-WRITE-PROCESSING` (Impact: 148.7 | O(2^N) | DB: 94)
  * `1245-EDIT-NUM-REQD` (Impact: 108.0 | O(2^N) | DB: 25)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 637`, `structural_boundaries: 238`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 1750`, `dead_code: 14`, `fragile_debt: 1`, `orphaned_logic: 99`
* *Architecture:* `io: 101`, `api: 1`, `import: 56`
* *Defense:* `safety: 177`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` CVCUS01Y, CSMSG01Y, CSUTLDWY, COTTL01Y, CVACT03Y, CSSETATY, CSSTRPFY, CVACT01Y...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `Unknown Archetype` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
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

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.279 IQR)
- **Top Global Matches:** file_cluster_8: 13.279, file_cluster_7: 13.684, file_cluster_11: 13.734
- **Magnitude:** 4927.96 | **LOC:** 3636 | **CtrlFlow:** 86.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4743
- **Risk Profile:** Cognitive Load (37.1967%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `definition` (Impact: 2834.6 | O(N^6) | DB: 4743)
  * `definition` (Impact: 2.5 | O(2^N))
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.569 IQR)
- **Top Global Matches:** file_cluster_8: 14.569, file_cluster_11: 14.902, file_cluster_7: 14.931
- **Magnitude:** 4921.12 | **LOC:** 2415 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1134
- **Risk Profile:** Cognitive Load (48.7939%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `DNAME42` (Impact: 1243.2 | O(2^N) | DB: 1134)
  * `SECT-NC176A-001` (Impact: 152.0 | O(N^1) | DB: 606)
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `FAIL-ROUTINE` (Impact: 10.4 | O(2^N) | DB: 13)
  * `PRINT-DETAIL` (Impact: 9.6 | O(N^1) | DB: 14)
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

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.117 IQR)
- **Top Global Matches:** file_cluster_8: 14.117, file_cluster_7: 14.502, file_cluster_13: 14.557
- **Magnitude:** 4508.84 | **LOC:** 3265 | **CtrlFlow:** 94.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 2490
- **Risk Profile:** Cognitive Load (33.1117%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `phrase` (Impact: 1064.2 | O(N^6) | DB: 2490)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.499 IQR)
- **Top Global Matches:** file_cluster_8: 14.499, file_cluster_11: 14.84, file_cluster_7: 14.866
- **Magnitude:** 4459.96 | **LOC:** 2135 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 923
- **Risk Profile:** Cognitive Load (48.8626%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `WRK-DU-18V00` (Impact: 1153.2 | O(2^N) | DB: 923)
  * `SECT-NC177A-001` (Impact: 146.2 | O(N^1) | DB: 576)
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `WRK-DS-18V00` (Impact: 34.4 | O(2^N) | DB: 69)
  * `WRK-CS-18V00` (Impact: 12.8 | O(2^N) | DB: 23)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2024.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.567 IQR)
- **Top Global Matches:** file_cluster_8: 14.567, file_cluster_11: 14.9, file_cluster_13: 14.925
- **Magnitude:** 3800.88 | **LOC:** 2217 | **CtrlFlow:** 95.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1567
- **Risk Profile:** Cognitive Load (47.0743%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BUILD-TABLE2` (Impact: 324.6 | O(N^1) | DB: 1567)
  * `SECT-NC202A-001` (Impact: 164.3 | O(N^1) | DB: 838)
  * `ERROR-HOLD` (Impact: 37.9 | O(2^N) | DB: 57)
  * `FAIL-ROUTINE` (Impact: 10.4 | O(2^N) | DB: 13)
  * `PRINT-DETAIL` (Impact: 9.6 | O(N^1) | DB: 14)
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
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (37.8734%), Tech Debt (0.0%)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.813 IQR)
- **Top Global Matches:** file_cluster_8: 12.813, file_cluster_7: 13.236, file_cluster_11: 13.283
- **Magnitude:** 3526.12 | **LOC:** 1969 | **CtrlFlow:** 98.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 829
- **Risk Profile:** Cognitive Load (49.427%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `FAIL` (Impact: 1708.2 | O(2^N) | DB: 829)
  * `SECT-NC201A-001` (Impact: 517.3 | O(N^1) | DB: 422)
  * `XXXXX055` (Impact: 76.3 | O(N^1) | DB: 8)
  * `FAIL` (Impact: 73.5 | O(2^N) | DB: 31)
  * `ERROR-HOLD` (Impact: 37.9 | O(2^N) | DB: 57)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1244.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.746 IQR)
- **Top Global Matches:** file_cluster_8: 13.746, file_cluster_7: 14.212, file_cluster_13: 14.276
- **Magnitude:** 3308.14 | **LOC:** 2352 | **CtrlFlow:** 98.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (44.2351%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `FAIL-ROUTINE` (Impact: 10.4 | O(2^N) | DB: 13)
  * `PRINT-DETAIL` (Impact: 9.6 | O(N^1) | DB: 14)
  * `HEAD-ROUTINE` (Impact: 9.2 | O(N^1) | DB: 16)
  * `PICTURE-TEST-1-A` (Impact: 7.5 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1128`, `structural_boundaries: 19`, `func_start: 316`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 83`, `high_risk_execution: 1`, `state_mutation: 1828`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 4`, `orphaned_logic: 244`
* *Architecture:* `io: 96`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1734.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.73 IQR)
- **Top Global Matches:** file_cluster_8: 13.73, file_cluster_7: 14.19, file_cluster_11: 14.243
- **Magnitude:** 3185.84 | **LOC:** 2216 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.511%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `DIV-TEST-F3-3-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F3-4-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F3-15-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F3-16-2` (Impact: 16.6 | O(2^N) | DB: 4)
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

### `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_0` (Drift: 12.047 IQR)
- **Top Global Matches:** file_cluster_0: 12.047, file_cluster_8: 12.199, file_cluster_17: 12.228
- **Magnitude:** 3151.82 | **LOC:** 2280 | **CtrlFlow:** 50.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (17.3038%), Tech Debt (28.7846%)
**Top Internal Functions/Classes:**
  * `visitJsonParse` (Impact: 121.1 | O(N^6))
  * `visitAlterStatement` (Impact: 108.0 | O(N^4) | DB: 1)
  * `visitDataDescriptionEntryFormat2` (Impact: 101.9 | O(N^5))
  * `validateJavaDirectives` (Impact: 81.8 | O(N^3))
  * `visitJsonGenerate` (Impact: 74.0 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 475`, `structural_boundaries: 474`, `args: 530`, `func_start: 311`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 170`, `state_mutation: 98`, `planned_debt: 2`, `duplicate_logic: 8`
* *Architecture:* `api: 266`, `import: 36`
* *Defense:* `safety: 38`, `doc: 6`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.181
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 16):` org.eclipse.lsp4j.Location, org.eclipse.lsp.cobol.core.visitor.MappingUtils.retrieveLocality, java.util.regex.Matcher, org.eclipse.lsp.cobol.service.settings.CachingConfigurationService, org.eclipse.lsp.cobol.core.CobolParser.*, org.eclipse.lsp.cobol.common.utils.StringUtils, org.eclipse.lsp.cobol.common.OutlineNodeNames.FILLER_NAME, org.antlr.v4.runtime.tree.TerminalNode...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1774.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.853 IQR)
- **Top Global Matches:** file_cluster_8: 13.853, file_cluster_7: 14.36, file_cluster_13: 14.412
- **Magnitude:** 3092.6 | **LOC:** 2902 | **CtrlFlow:** 96.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (38.2399%), Tech Debt (0.0%)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1724.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.716 IQR)
- **Top Global Matches:** file_cluster_8: 13.716, file_cluster_7: 14.176, file_cluster_11: 14.228
- **Magnitude:** 3079.26 | **LOC:** 2213 | **CtrlFlow:** 97.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.358%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `DIV-TEST-F2-15-2` (Impact: 16.6 | O(2^N) | DB: 4)
  * `DIV-TEST-F2-17-2` (Impact: 16.6 | O(2^N) | DB: 4)
  * `DIV-TEST-F2-25-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F2-25-2` (Impact: 16.6 | O(2^N) | DB: 5)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2154.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.77 IQR)
- **Top Global Matches:** file_cluster_8: 13.77, file_cluster_11: 14.098, file_cluster_0: 14.163
- **Magnitude:** 2957.72 | **LOC:** 2803 | **CtrlFlow:** 88.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 174
- **Risk Profile:** Cognitive Load (39.7803%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `START-WRITE-GF-18` (Impact: 35.6 | O(N^1) | DB: 174)
  * `START-TERM-003` (Impact: 33.5 | O(N^1) | DB: 164)
  * `SECT-0001-IX215A` (Impact: 32.2 | O(N^1) | DB: 159)
  * `START-TEST-GF-22` (Impact: 14.2 | O(N^1) | DB: 62)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1754.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.642 IQR)
- **Top Global Matches:** file_cluster_8: 13.642, file_cluster_7: 14.1, file_cluster_11: 14.14
- **Magnitude:** 2918.8 | **LOC:** 2077 | **CtrlFlow:** 97.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.0299%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `SUB-TEST-F2-28-6` (Impact: 16.6 | O(2^N) | DB: 4)
  * `SUB-TEST-F2-29-5` (Impact: 16.6 | O(2^N) | DB: 4)
  * `SUB-TEST-F2-30-6` (Impact: 16.6 | O(2^N) | DB: 4)
  * `SUB-TEST-F2-31-5` (Impact: 16.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 684`, `structural_boundaries: 21`, `func_start: 275`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 126`, `high_risk_execution: 1`, `state_mutation: 1500`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 240`
* *Architecture:* `io: 187`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1714.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.699 IQR)
- **Top Global Matches:** file_cluster_8: 13.699, file_cluster_7: 14.16, file_cluster_11: 14.215
- **Magnitude:** 2916.82 | **LOC:** 2266 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.6086%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `DIV-TEST-F1-14-2` (Impact: 16.6 | O(2^N) | DB: 4)
  * `DIV-TEST-F1-15-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F1-14-1` (Impact: 14.6 | O(2^N) | DB: 5)
  * `DIV-TEST-F1-15-2` (Impact: 14.6 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 786`, `structural_boundaries: 21`, `func_start: 267`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 1680`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 247`
* *Architecture:* `io: 135`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1014.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.792 IQR)
- **Top Global Matches:** file_cluster_8: 13.792, file_cluster_7: 14.246, file_cluster_11: 14.263
- **Magnitude:** 2827.34 | **LOC:** 1864 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (42.6481%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `MPY-TEST-F1-14-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F1-16-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F1-24-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F1-24-2` (Impact: 16.6 | O(2^N) | DB: 5)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2094.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_11: 14.14, file_cluster_0: 14.171
- **Magnitude:** 2779.48 | **LOC:** 2854 | **CtrlFlow:** 93.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 153
- **Risk Profile:** Cognitive Load (38.5392%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `SECT-0001-IX209A` (Impact: 32.1 | O(N^1) | DB: 153)
  * `START-TEST-GF-11` (Impact: 14.6 | O(2^N) | DB: 23)
  * `START-TEST-GF-12` (Impact: 14.6 | O(2^N) | DB: 23)
  * `START-TEST-GF-13` (Impact: 14.6 | O(2^N) | DB: 23)
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

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1704.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.652 IQR)
- **Top Global Matches:** file_cluster_8: 13.652, file_cluster_7: 14.114, file_cluster_11: 14.157
- **Magnitude:** 2767.3 | **LOC:** 2013 | **CtrlFlow:** 97.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.6872%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `MPY-TEST-F2-17-2` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F2-19-2` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F2-28-1` (Impact: 16.6 | O(2^N) | DB: 5)
  * `MPY-TEST-F2-28-3` (Impact: 16.6 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 695`, `structural_boundaries: 21`, `func_start: 265`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 1`, `state_mutation: 1467`, `dead_code: 1`, `fragile_debt: 3`, `orphaned_logic: 247`
* *Architecture:* `io: 139`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1064.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.768 IQR)
- **Top Global Matches:** file_cluster_8: 13.768, file_cluster_7: 14.221, file_cluster_11: 14.255
- **Magnitude:** 2731.08 | **LOC:** 2531 | **CtrlFlow:** 97.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 61
- **Risk Profile:** Cognitive Load (41.1044%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` (Impact: 52.1 | O(2^N) | DB: 61)
  * `SUB-TEST-F1-27-1` (Impact: 14.4 | O(2^N) | DB: 5)
  * `SUB-TEST-F1-28-1` (Impact: 14.4 | O(2^N) | DB: 5)
  * `SUB-TEST-F1-28-5` (Impact: 14.4 | O(2^N) | DB: 5)
  * `SUB-TEST-F1-27-2` (Impact: 14.3 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 849`, `structural_boundaries: 23`, `func_start: 358`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 1`, `state_mutation: 1862`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 8`, `orphaned_logic: 240`
* *Architecture:* `io: 267`, `api: 1`
* *Defense:* `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java` (JAVA | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.665 IQR)
- **Top Global Matches:** file_cluster_8: 13.665, file_cluster_7: 14.063, file_cluster_13: 14.149
- **Magnitude:** 2716.98 | **LOC:** 1852 | **CtrlFlow:** 93.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 879
- **Risk Profile:** Cognitive Load (91.5651%), Tech Debt (7.9929%)
**Top Internal Functions/Classes:**
  * `checkOptions` (Impact: 1640.5 | O(N^4))
  * `checkCompIDMutuallyExclusive` (Impact: 4.9 | O(N^1))
  * `put` (Impact: 4.0 | O(2^N) | DB: 879)
  * `CICSInquireSPOptionsCheckUtility` (Impact: 2.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 16`, `args: 10`, `func_start: 1274`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1025`, `orphaned_logic: 1`
* *Architecture:* `api: 5`, `import: 7`
* *Defense:* `doc: 6`, `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.176
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` org.eclipse.lsp.cobol.implicitDialects.cics.CICSParser.RULE_cics_inquire_system_programming, org.eclipse.lsp.cobol.implicitDialects.cics.CICSParser, org.eclipse.lsp.cobol.common.error.ErrorSeverity, org.eclipse.lsp.cobol.common.dialects.DialectProcessingContext, org.eclipse.lsp.cobol.implicitDialects.cics.CICSLexer, org.antlr.v4.runtime.ParserRuleContext, java.util.*, org.eclipse.lsp.cobol.common.error.SyntaxError
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/SM1074.2.cbl` (COBOL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.535 IQR)
- **Top Global Matches:** file_cluster_8: 13.535, file_cluster_7: 14.07, file_cluster_13: 14.166
- **Magnitude:** 2424.98 | **LOC:** 2523 | **CtrlFlow:** 94.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.0277%), Tech Debt (0.0%)
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
- **Global Archetype:** `file_cluster_8` (Drift: 13.252 IQR)
- **Top Global Matches:** file_cluster_8: 13.252, file_cluster_7: 13.7, file_cluster_13: 13.79
- **Magnitude:** 2290.4 | **LOC:** 2720 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 381
- **Risk Profile:** Cognitive Load (34.8901%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `COMPUTED-N` (Impact: 158.2 | O(2^N) | DB: 381)
  * `ERROR-HOLD` (Impact: 37.9 | O(2^N) | DB: 57)
  * `COMPUTED-N` (Impact: 20.5 | O(2^N) | DB: 31)
  * `FAIL-ROUTINE` (Impact: 10.4 | O(2^N) | DB: 13)
  * `PRINT-DETAIL` (Impact: 9.6 | O(N^1) | DB: 14)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 485`, `structural_boundaries: 20`, `func_start: 346`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 272`, `high_risk_execution: 1`, `state_mutation: 1370`, `dead_code: 1`, `fragile_debt: 3`, `duplicate_logic: 17`, `orphaned_logic: 231`
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
- `tests/test_files/cicsGenApp/positive/lgucus01.cbl` (COBOL) | Magnitude: 82.18 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 39, structural_boundaries: 13, branch: 11
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IC2224.2.cbl` (COBOL) | Magnitude: 1084.7 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 543, api: 179, branch: 178, io: 70
- `tests/test_files/aws-mainframe-modernization-carddemo/copybooks/CSUTLDPY.cpy` (COBOL) | Magnitude: 35.34 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 288, state_mutation: 203, branch: 78, structural_boundaries: 40
- `tests/test_files/project/ADSORT.cbl` (COBOL) | Magnitude: 46.66 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 33, state_mutation: 28, branch: 9, structural_boundaries: 7
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IC2244.2.cbl` (COBOL) | Magnitude: 635.16 | Delta: **0.051 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 322, branch: 117, api: 85, io: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/test_files/cicsGenApp/positive/lgicdb01.cbl` (COBOL) | Magnitude: 130.26 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 143, state_mutation: 61, branch: 18, structural_boundaries: 13
- `tests/test_files/cicsGenApp/positive/lgapol01.cbl` (COBOL) | Magnitude: 95.08 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 114, state_mutation: 37, branch: 14, structural_boundaries: 12
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2474.2.cbl` (COBOL) | Magnitude: 964.34 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 528, branch: 217, io: 123, func_start: 121
- `tests/test_files/cicsGenApp/positive/lgdpol01.cbl` (COBOL) | Magnitude: 103.42 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 111, state_mutation: 45, branch: 16, structural_boundaries: 13
- `tests/test_files/cicsGenApp/positive/lgupol01.cbl` (COBOL) | Magnitude: 139.36 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 138, state_mutation: 66, branch: 21, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/model/extendedapi/Program.java` (JAVA) | Magnitude: 4.14 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 5, indent_spaces: 5, func_start: 2, api: 2
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/transformer/ContinuationLineTransformation.java` (JAVA) | Magnitude: 204.76 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 205, structural_boundaries: 70, branch: 43, args: 29
- `server/engine/src/test/java/org/eclipse/lsp/cobol/core/model/tree/NodeTest.java` (JAVA) | Magnitude: 12.38 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 46, structural_boundaries: 28, import: 14, func_start: 8
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestErrorRecovery.java` (JAVA) | Magnitude: 28.24 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 18, import: 12, args: 5
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/model/extendedapi/Perform.java` (JAVA) | Magnitude: 40.16 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 19, branch: 10, structural_boundaries: 7, args: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variable/VariableDefinitionNode.java` (JAVA) | Magnitude: 196.24 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 214, structural_boundaries: 52, api: 46, doc: 45
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/formations/Formation.java` (JAVA) | Magnitude: 18.78 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 5, generics: 3, import: 3, args: 1
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/pipeline/Pipeline.java` (JAVA) | Magnitude: 76.1 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 12, branch: 9, state_mutation: 6
- `server/engine/src/test/java/org/eclipse/lsp/cobol/positive/CobolTextRegistry.java` (JAVA) | Magnitude: 27.76 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 7, indent_spaces: 6, func_start: 4
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` (JAVA) | Magnitude: 403.64 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 367, branch: 88, structural_boundaries: 71, args: 69

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/processor/CompilerDirectiveContext.java` (JAVA) | Magnitude: 69.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, args: 15, comprehensions: 13, structural_boundaries: 11
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/settings/SettingsServiceImpl.java` (JAVA) | Magnitude: 220.4 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 82, structural_boundaries: 38, args: 33, branch: 27
- `tests/test_files/Cobol85PositiveTestsSuite/positive/EXEC84.2.cbl` (COBOL) | Magnitude: 1425.82 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: state_mutation: 778, branch: 418, structural_boundaries: 215, func_start: 204
- `server/engine/src/main/java/org/eclipse/lsp/cobol/service/delegates/references/ElementOccurrences.java` (JAVA) | Magnitude: 28.8 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 77, structural_boundaries: 30, comprehensions: 21, branch: 18
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1384.2.cbl` (COBOL) | Magnitude: 705.16 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 401, branch: 143, func_start: 102, io: 102

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `clients/cobol-lsp-vscode-extension/src/services/copybook/E4ECopybookService.ts` (TYPESCRIPT) | Magnitude: 2.56 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 12, func_start: 11, generics: 11, branch: 9

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/ControlFlowService.spec.ts` (TYPESCRIPT) | Magnitude: 9.1 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 163, structural_boundaries: 43, args: 39, func_start: 34
- `clients/cobol-lsp-vscode-extension/src/test/runTest.ts` (TYPESCRIPT) | Magnitude: 3.28 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 46, io: 14, structural_boundaries: 8, concurrency: 8
- `clients/cobol-lsp-vscode-extension/src/test/suite/index.ts` (TYPESCRIPT) | Magnitude: 2.29 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 9, args: 6, concurrency: 5
- `clients/cobol-lsp-vscode-extension/src/services/snippetcompletion/SnippetCompletionProvider.ts` (TYPESCRIPT) | Magnitude: 16.45 | Delta: **0.053 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 161, structural_boundaries: 44, state_mutation: 38, immutability_locks: 33
- `clients/cobol-lsp-vscode-extension/src/services/worker/Worker.ts` (TYPESCRIPT) | Magnitude: 8.31 | Delta: **0.106 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, state_mutation: 22, structural_boundaries: 17, args: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/LanguageEngineFacade.java` (JAVA) | Magnitude: 20.92 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: doc: 12, structural_boundaries: 2, args: 2, func_start: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `tests/test_files/aws-mainframe-modernization-carddemo/positive/COTRN01C.cbl` (COBOL) | Magnitude: 349.22 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 231, state_mutation: 140, branch: 52, structural_boundaries: 10
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSAsktime.java` (JAVA) | Magnitude: 10.42 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 16, import: 9, args: 4
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCasePreprocessorListener.java` (JAVA) | Magnitude: 584.66 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 527, structural_boundaries: 126, func_start: 126, args: 87
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ReplaceStrategy.java` (JAVA) | Magnitude: 17.78 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 7, structural_boundaries: 4, import: 2, indent_spaces: 2
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCICSConditionCanBeUsedForVariableDeclaration.java` (JAVA) | Magnitude: 9.38 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 20, structural_boundaries: 10, import: 6, args: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `clients/cobol-lsp-vscode-extension/src/commands/UpdateCobolProgramRuler.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: dead_code: 7
- `clients/analysis/src/__tests__/__resources__/cfgraph/case60.cbl` (COBOL) | Magnitude: 9.58 | Delta: **0.07 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 14, structural_boundaries: 5, branch: 4, func_start: 4

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` -> Churn: **80.86%** | Cog Load: 94.9997% | Debt: 82.6712%
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/mapping/ExtendedDocument.java` -> Churn: **54.02%** | Cog Load: 7.1064% | Debt: 99.926%
- `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` -> Churn: **53.62%** | Cog Load: 72.6018% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java` -> **Hizir** (100.0% isolated ownership) | Magnitude: 1017.44
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCasePreprocessorListener.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 584.66
- `server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/SourceUnitGraph.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 487.88
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSendStatement.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 440.84
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblParser.java` -> **Iurii Shchekochikhin** (100.0% isolated ownership) | Magnitude: 383.84

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

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java` -> **Severity: 1371.244** (Blast Radius: 16.022 * Doc Risk: 85.5851%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 845.494** (Blast Radius: 11.02 * Doc Risk: 76.7236%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/Node.java` -> **Severity: 838.353** (Blast Radius: 9.189 * Doc Risk: 91.2344%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/copybook/CopybookProcessingMode.java` -> **Severity: 793.577** (Blast Radius: 8.131 * Doc Risk: 97.599%)
- `clients/cobol-lsp-vscode-extension/src/constants.ts` -> **Severity: 737.0** (Blast Radius: 7.37 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
