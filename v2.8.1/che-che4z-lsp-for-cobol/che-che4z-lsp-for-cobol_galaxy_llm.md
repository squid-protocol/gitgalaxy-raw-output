# ARCHITECTURAL_BRIEF: che-che4z-lsp-for-cobol
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/eclipse/che-che4z-lsp-for-cobol.git` |
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
| Total Artifacts | 3535 |
| Analyzed Artifacts (Scanned) | 3126 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 409 |
| Total LOC | 677066 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 88.4% |
| Dominant Lang | COBOL |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6322 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3262 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.6211 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 102 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| JAVA | 1570 | 119516 | 50.2% |
| COBOL | 968 | 499175 | 31.0% |
| JSON | 283 | 35866 | 9.1% |
| TYPESCRIPT | 194 | 22145 | 6.2% |
| PLAINTEXT | 39 | 2 | 1.2% |
| MARKDOWN | 29 | 0 | 0.9% |
| XML | 24 | 0 | 0.8% |
| JAVASCRIPT | 14 | 327 | 0.4% |
| YAML | 3 | 24 | 0.1% |
| SHELL | 2 | 11 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +1.29; from the repo's file-archetype mix)
> **File Composition:** Tests & Verification Files 22%, Declarative / Non-Code 16%, Data / Markup / Trivial 16%, I/O & Config Routines Files 11%, Interface Declarations Files 10%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 3058 | 97.8% |
| Unknown | 2 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 66 | 2.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 409*

**Composition by Extension & Reason:**
- `.dot`: 118x Unsupported Format (.dot), 2x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.cbl`: 11x Excluded (Saturation: Line 53 exceeds 500 chars), 10x Excluded (Saturation: Line 2 exceeds 500 chars), 6x Excluded (Saturation: Line 72 exceeds 500 chars)
- `no_extension`: 54x Unsupported Format (.undeterminable), 31x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Binary Format Detected)
- `.json`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 3867 LOC), 1x Excluded (Massive Static Asset Blob: 4112 LOC)
- `.g4`: 24x Unsupported Format (.g4)
- `.cpy`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 1283, Signals: 0), 1x Zero-Density Threshold (LOC: 85, Signals: 0)
- `.gif`: 8x Excluded (Explicitly Denied Extension: '.gif')
- `.md`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.copy`: 3x Excluded (Unsupported Extension: '.COPY')
- `.sh`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.original`: 2x Unsupported Format (.original)
- `.ts`: 1x Excluded (Saturation: Line 84 exceeds 500 chars)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 35.0 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 2.1 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 6.9 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 8.2 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 99.9 | 0.6 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 74.7 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 11.8 | 0.5 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 58.0 | 90.5 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 100.0 | 0.1 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6166 | 595 | 10 | `tests/test_files/cicsGenApp/copybooks/ssmap.cpy` |
| cleanup | 1200 | 433 | 1 | `tests/test_files/cicsGenApp/positive/lgsetup.cbl` |
| guards | 13345 | 1575 | 11 | `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/TestCicsSysSetStatement.java` |
| danger | 29955 | 1115 | 28 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2184.2.cbl` |
| concurrency | 2286 | 229 | 0 | `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.test.ts` |
| connectivity | 7085 | 1335 | 4 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2314.2.cbl` |
| io | 66178 | 703 | 67 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` |
| crypto | 0 | 0 | 0 | - |
| ipc | 972 | 332 | 1 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IC2224.2.cbl` |
| time | 374 | 143 | 0 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF4014.2.cbl` |
| serialization | 425 | 68 | 0 | `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` |
| regex | 3288 | 550 | 5 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2164.2.cbl` |
| events | 251 | 178 | 0 | `clients/cobol-lsp-vscode-extension/src/services/util/TarUtil.ts` |
| tests | 6966 | 901 | 4 | `server/common/src/test/java/org/eclipse/lsp/cobol/common/mapping/ExtendedTextTest.java` |
| docs | 2913 | 1624 | 2 | `clients/analysis/src/vm/vm.ts` |
| debt | 2909 | 685 | 3 | `tests/test_files/aws-mainframe-modernization-carddemo/positive/CBTRN03C.cbl` |
| mutation | 136854 | 2165 | 152 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl` |
| dead_code | 15381 | 1121 | 8 | `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2184.2.cbl` |
| credential | 34 | 15 | 0 | `clients/analysis/src/__tests__/__resources__/cfgraph/case121.cfast.json` |
| threat | 6557 | 519 | 10 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2524.2.cbl` |
| ml_ai | 1500 | 79 | 0 | `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IF1174.2.cbl` |
| ui | 101 | 28 | 0 | `clients/sample-dialect-support/src/statements.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0152**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` (Hits: 1395)
- `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2094.2.cbl` (Hits: 1335)
- `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2154.2.cbl` (Hits: 1136)

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

- `definition` **(Compute Cores)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl`) -> Impact: **628.2** | LOC: 3224
- `checkOptions` **(Compute Cores)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSInquireSPOptionsCheckUtility.java`) -> Impact: **305.5** | LOC: 707
  * *Intent:* /** * Entrypoint to check CICS SP Inquire rule options * * @param ctx ParserRuleContext subclass containing options * @param <E> A subclass of ParserR...
- `definition` **(Compute Cores)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1084.2.cbl`) -> Impact: **231.6** | LOC: 1771
- `checkOptions` **(Compute Cores)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility/CICSSysSetOptionsCheckUtility.java`) -> Impact: **202.6** | LOC: 205
  * *Intent:* /** * Entrypoint to check CICS SET ASSOCIATION USERCORRDATA rules for required and invalid options * * @param ctx ParserRuleContext subclass containin...
- `phrase` **(I/O & Config Routines)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2534.2.cbl`) -> Impact: **182.7** | LOC: 2053
- `definition` **(Compute Cores)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1094.2.cbl`) -> Impact: **178.4** | LOC: 1289
- `phrase` **(I/O & Config Routines)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl`) -> Impact: **173.1** | LOC: 2022
- `definition` **(Compute Cores)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2054.2.cbl`) -> Impact: **166.3** | LOC: 1127
- `definition` **(Compute Cores)** (@ `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX1054.2.cbl`) -> Impact: **164.9** | LOC: 1079
- `traverse` **(Defensive Guards)** (@ `server/engine/src/main/java/org/eclipse/lsp/cobol/cfg/CFASTBuilderImpl.java`) -> Impact: **151.6** | LOC: 191

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **I/O & Config Routines**: dominated by I/O and configuration handling

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/test_files/Cobol85PositiveTestsSuite/positive` | 233 | 145651.72 | 36.66% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/compileListing` | 233 | 102541.4 | 20.69% | 0.0% |
| `tests/test_files/aws-mainframe-modernization-carddemo/positive` | 26 | 10276.7 | 38.97% | 0.0% |
| `clients/cobol-lsp-vscode-extension` | 9 | 10098.96 | 0.82% | 0.0% |
| `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases` | 404 | 5347.56 | 3.04% | 0.0% |
| `clients/cobol-lsp-vscode-extension/src/test/suite` | 15 | 4822.49 | 59.45% | 0.0% |
| `clients/analysis/src/__tests__/__resources__/cfgraph` | 321 | 4368.36 | 1.64% | 21.7% |
| `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/utility` | 109 | 4005.74 | 5.42% | 27.93% |
| `tests/test_files/cicsGenApp/positive` | 31 | 3407.42 | 41.43% | 0.0% |
| `tests/test_files/Cobol85PositiveTestsSuite/compileListing/snapshot` | 139 | 2818.26 | 0.5% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `clients/cobol-lsp-vscode-extension/src/type/zoweApi.d.ts` -> **100.0%** Exposure
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/semantics/GroupContext.java` -> **99.9994%** Exposure
- `server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/IdmsVisitor.java` -> **99.9977%** Exposure
- `clients/analysis/src/__tests__/__resources__/cfgraph/case52.cbl` -> **99.9797%** Exposure
- `server/dialect-daco/src/main/java/org/eclipse/lsp/cobol/dialects/daco/MessageServiceParser.java` -> **99.9788%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `clients/analysis/src/__tests__/graphbuilder.unit.test.ts` -> **100.0%** Exposure
- `clients/analysis/src/vm/utils.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/util/ConfigurationWatcher.spec.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/FSUtils.ts` -> **100.0%** Exposure
- `clients/cobol-lsp-vscode-extension/src/services/util/Memoize.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2184.2.cbl` -> **247** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2234.2.cbl` -> **200** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1244.2.cbl` -> **197** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/negative/NC1074.2.cbl` -> **191** Orphaned Functions | **0** Duplicates
- `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1074.2.cbl` -> **191** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Credential Material (formerly Hardcoded Payload Artifacts)
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
- **Unknown Dependencies:** `14460` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` (TYPESCRIPT) -> Cumulative Risk: **724.73**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.14)
- **Magnitude:** 138.3 | **LOC:** 188 | **CtrlFlow:** 25.3% | **Authorship Centralization:** 33.3%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.1837%), Concurrency (98.0976%), Documentation (95.6522%)
- **Heaviest Functions:** `initializeExternalAPIs` (Compute Cores, Impact: 31.6), `constructor` (Many-Argument Workhorses, Impact: 20.1), `explorerAppeared` (Callbacks & Closures, Impact: 5.6)

### 2. `clients/cobol-lsp-vscode-extension/src/services/snippetcompletion/SnippetCompletionProvider.ts` (TYPESCRIPT) -> Cumulative Risk: **705.5**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -1.49)
- **Magnitude:** 135.4 | **LOC:** 252 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9941%), State Flux (99.6316%), Documentation (94.1176%)
- **Heaviest Functions:** `provideCompletionItems` (Many-Argument Workhorses, Impact: 13.9), `pickSnippet` (Defensive Guards, Impact: 6.7), `findPosition` (Compute Cores, Impact: 5.7)

### 3. `clients/cobol-lsp-vscode-extension/src/__tests__/services/ControlFlowService.spec.ts` (TYPESCRIPT) -> Cumulative Risk: **649.42**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.40)
- **Magnitude:** 137.22 | **LOC:** 242 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `postMessage` (Callbacks & Closures, Impact: 3.2), `constructor` (Callbacks & Closures, Impact: 3.1), `lastWorkerErrorTrigger` (Callbacks & Closures, Impact: 3.1)

### 4. `clients/cobol-lsp-vscode-extension/src/services/copybook/CopybooksCompletionProvider.ts` (TYPESCRIPT) -> Cumulative Risk: **649.34**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +2.36)
- **Magnitude:** 133.24 | **LOC:** 159 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `provideCompletionItems` (Many-Argument Workhorses, Impact: 34.3), `isDefaultCopyStatement` (Callbacks & Closures, Impact: 16.5)

### 5. `clients/cobol-lsp-vscode-extension/src/services/util/Memoize.ts` (TYPESCRIPT) -> Cumulative Risk: **644.57**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.49)
- **Magnitude:** 60.54 | **LOC:** 59 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `execute` (Defensive Guards, Impact: 5.3), `constructor` (Generic / Templated Code, Impact: 3.0), `generateKey` (Interface Declarations, Impact: 1.6)

### 6. `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` (TYPESCRIPT) -> Cumulative Risk: **623.13**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.53)
- **Magnitude:** 387.5 | **LOC:** 559 | **CtrlFlow:** 22.5% | **Authorship Centralization:** 57.1%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Concurrency (99.4969%), State Flux (96.0202%)
- **Heaviest Functions:** `finishTask` (Many-Argument Workhorses, Impact: 39.2), `finishTaskWithError` (Defensive Guards, Impact: 27.5), `start` (Defensive Guards, Impact: 21.8)

### 7. `clients/cobol-lsp-vscode-extension/src/services/subroutines/SubroutinesCompletionsProvider.ts` (TYPESCRIPT) -> Cumulative Risk: **619.55**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.01)
- **Magnitude:** 92.84 | **LOC:** 88 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `provideCompletionItems` (Many-Argument Workhorses, Impact: 30.3)

### 8. `server/engine/src/main/java/org/eclipse/lsp/cobol/implicitDialects/cics/CICSVisitor.java` (JAVA) -> Cumulative Risk: **614.95**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.07)
- **Magnitude:** 179.58 | **LOC:** 437 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.2313%), Tech Debt (94.32%), Documentation (90.0%)
- **Heaviest Functions:** `visitCicsExecBlock` (Callbacks & Closures, Impact: 22.2), `getCheckParams` (Compute Cores, Impact: 20.8), `visitVariableNameUsage` (Annotated Framework Methods, Impact: 7.9)

### 9. `clients/cobol-lsp-vscode-extension/src/services/copybook/ZoweThrottling.ts` (TYPESCRIPT) -> Cumulative Risk: **614.78**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +1.68)
- **Magnitude:** 66.66 | **LOC:** 42 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Cognitive Load (100.0%), Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%)
- **Heaviest Functions:** `locked` (Defensive Guards, Impact: 7.8), `constructor` (State Mutators, Impact: 4.4)

### 10. `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/delegates/copybooks/CopybookPreprocessorService.java` (JAVA) -> Cumulative Risk: **610.42**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.13)
- **Magnitude:** 163.68 | **LOC:** 338 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9289%), Safety Score (87.3932%)
- **Heaviest Functions:** `prepareReplacements` (Compute Cores, Impact: 26.2), `addCopybook` (Many-Argument Workhorses, Impact: 14.2), `validateCopybookName` (Many-Argument Workhorses, Impact: 8.7)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `clients/cobol-lsp-vscode-extension/.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `clients/cobol-lsp-vscode-extension/telemetry.key` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: N/A IQR)
- **Magnitude:** 5000.0 | **LOC:** 1 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1764.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2966.42 | **LOC:** 2415 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1965%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `ADD-TEST-F1-19` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 427 instances
* *State Mutation (weighted view):* 2201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 583`, `func_start: 341`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `high_risk_execution: 1`, `state_mutation: 1347`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 165`
* *Architecture:* `io: 252`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2024.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2732.08 | **LOC:** 2217 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.242%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `XXXXX055` **(I/O & Config Routines)** (Impact: 6.5)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `COLUMN-NAMES-ROUTINE` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 239 instances
* *State Mutation (weighted view):* 2047
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 355`, `func_start: 434`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 263`, `high_risk_execution: 1`, `state_mutation: 1569`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 165`
* *Architecture:* `io: 339`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1774.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2729.06 | **LOC:** 2135 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.7754%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `ADD-TEST-F2-34-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 415 instances
* *State Mutation (weighted view):* 2041
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 513`, `func_start: 295`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 125`, `high_risk_execution: 1`, `state_mutation: 1211`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 149`
* *Architecture:* `io: 184`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC2024.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 2716.74 | **LOC:** 3265 | **CtrlFlow:** 4.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.8801%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `phrase` **(I/O & Config Routines)** (Impact: 173.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 229 instances
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 2479
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 362`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 274`, `high_risk_execution: 3`, `state_mutation: 2021`, `fragile_debt: 3`
* *Architecture:* `io: 496`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2154.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2584.32 | **LOC:** 2803 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `START-TEST-GF-27` **(I/O & Config Routines)** (Impact: 25.0)
  * `START-TEST-GF-09` **(I/O & Config Routines)** (Impact: 24.9)
  * `START-TEST-GF-18` **(I/O & Config Routines)** (Impact: 24.9)
  * `START-TEST-GF-06` **(I/O & Config Routines)** (Impact: 19.7)
  * `START-TEST-GF-25` **(I/O & Config Routines)** (Impact: 19.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 388 instances
* *State Mutation (weighted view):* 1739
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 464`, `structural_boundaries: 399`, `func_start: 219`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 258`, `high_risk_execution: 1`, `state_mutation: 963`, `dead_code: 3`, `fragile_debt: 6`, `unreferenced_by_name: 57`
* *Architecture:* `io: 1136`
* *Defense:* `cleanup: 29`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1764.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2536.54 | **LOC:** 3301 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.2751%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 400 instances
* *State Mutation (weighted view):* 2456
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 590`
* *Risk/State:* `safety_bypasses: 164`, `high_risk_execution: 3`, `state_mutation: 1656`, `fragile_debt: 3`
* *Architecture:* `io: 371`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2504.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2426.32 | **LOC:** 1969 | **CtrlFlow:** 53.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (44.7763%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `XXXXX055` **(I/O & Config Routines)** (Impact: 74.3)
  * `IF--TEST-71` **(I/O & Config Routines)** (Impact: 9.8)
  * `IF--TEST-120` **(I/O & Config Routines)** (Impact: 9.8)
  * `IF--TEST-121` **(I/O & Config Routines)** (Impact: 9.8)
  * `IF--TEST-47` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 269 instances
* *State Mutation (weighted view):* 879
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1006`, `structural_boundaries: 550`, `func_start: 412`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 147`, `high_risk_execution: 1`, `state_mutation: 341`, `dead_code: 1`, `fragile_debt: 28`, `unreferenced_by_name: 157`
* *Architecture:* `io: 401`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/IX2154.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2404.56 | **LOC:** 3636 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5353%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `definition` **(Compute Cores)** (Impact: 628.2)
  * `definition` **(I/O & Config Routines)** (Impact: 1.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 370 instances
* *State Mutation (weighted view):* 1703
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 474`, `structural_boundaries: 419`, `args: 6`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 261`, `high_risk_execution: 3`, `state_mutation: 963`, `fragile_debt: 6`
* *Architecture:* `io: 1395`
* *Defense:* `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/compileListing/NC1774.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2336.6 | **LOC:** 2902 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.6968%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 396 instances
* *State Mutation (weighted view):* 2264
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 264`, `structural_boundaries: 520`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 3`, `state_mutation: 1472`, `fragile_debt: 3`
* *Architecture:* `io: 270`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1064.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2212.38 | **LOC:** 2531 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.1502%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `SUB-TEST-F1-20` **(I/O & Config Routines)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 299 instances
* *State Mutation (weighted view):* 1420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 281`, `structural_boundaries: 591`, `func_start: 360`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 173`, `high_risk_execution: 1`, `state_mutation: 822`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 168`
* *Architecture:* `io: 264`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/aws-mainframe-modernization-carddemo/positive/COACTUPC.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2199.14 | **LOC:** 4245 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.0746%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `1100-RECEIVE-MAP` **(Compute Cores)** (Impact: 117.3)
  * `3300-SETUP-SCREEN-ATTRS` **(I/O & Config Routines)** (Impact: 116.5)
  * `2000-DECIDE-ACTION` **(I/O & Config Routines)** (Impact: 24.1)
  * `0000-MAIN` **(I/O & Config Routines)** (Impact: 23.4)
  * `1200-EDIT-MAP-INPUTS` **(I/O & Config Routines)** (Impact: 23.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 384 instances
* *State Mutation (weighted view):* 1468
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 403`, `structural_boundaries: 299`, `func_start: 101`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 52`, `state_mutation: 700`, `dead_code: 14`, `unreferenced_by_name: 3`
* *Architecture:* `io: 101`, `api: 1`, `import: 56`
* *Defense:* `safety: 14`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` COACTUP, COCOM01Y, COTTL01Y, CSDAT01Y, CSLKPCDY, CSMSG01Y, CSMSG02Y, CSSETATY...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2184.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 2196.42 | **LOC:** 3074 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.1723%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `XXXXX055` **(I/O & Config Routines)** (Impact: 8.0)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `COLUMN-NAMES-ROUTINE` **(I/O & Config Routines)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 172 instances
* *State Mutation (weighted view):* 1123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 282`, `structural_boundaries: 597`, `func_start: 599`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 420`, `high_risk_execution: 1`, `state_mutation: 779`, `dead_code: 1`, `fragile_debt: 8`, `unreferenced_by_name: 247`
* *Architecture:* `io: 544`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2094.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2080.68 | **LOC:** 2854 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.4723%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `XXXXX055` **(I/O & Config Routines)** (Impact: 8.0)
  * `START-TEST-GF-42` **(I/O & Config Routines)** (Impact: 7.9)
  * `START-TEST-GF-06` **(I/O & Config Routines)** (Impact: 7.7)
  * `START-TEST-GF-24` **(I/O & Config Routines)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 319 instances
* *State Mutation (weighted view):* 1407
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 342`, `func_start: 245`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 161`, `high_risk_execution: 1`, `state_mutation: 769`, `dead_code: 5`, `fragile_debt: 3`, `unreferenced_by_name: 73`
* *Architecture:* `io: 838`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1244.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 2027.54 | **LOC:** 2352 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.5782%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PICTURE-TEST-26-C` **(I/O & Config Routines)** (Impact: 5.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 211 instances
* *State Mutation (weighted view):* 1182
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 367`, `structural_boundaries: 780`, `func_start: 318`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 83`, `high_risk_execution: 1`, `state_mutation: 760`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 197`
* *Architecture:* `io: 93`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1734.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1936.34 | **LOC:** 2216 | **CtrlFlow:** 13.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.0237%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F3-27-2` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 256 instances
* *State Mutation (weighted view):* 1270
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 500`, `func_start: 253`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 82`, `high_risk_execution: 1`, `state_mutation: 758`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 163`
* *Architecture:* `io: 118`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1724.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1883.56 | **LOC:** 2213 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.9318%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F2-26-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 236 instances
* *State Mutation (weighted view):* 1217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 273`, `structural_boundaries: 492`, `func_start: 260`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 92`, `high_risk_execution: 1`, `state_mutation: 745`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 157`
* *Architecture:* `io: 128`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1714.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1881.72 | **LOC:** 2266 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.0241%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `DIV-TEST-F1-15-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 221 instances
* *State Mutation (weighted view):* 1190
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 520`, `func_start: 268`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 748`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 165`
* *Architecture:* `io: 132`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1014.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1853.24 | **LOC:** 1864 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (34.0767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `MPY-TEST-F1-14-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 285 instances
* *State Mutation (weighted view):* 1231
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 454`, `func_start: 247`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 1`, `state_mutation: 661`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 146`
* *Architecture:* `io: 124`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1754.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1839.9 | **LOC:** 2077 | **CtrlFlow:** 11.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (32.4078%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `SUB-TEST-F2-34-1` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 257 instances
* *State Mutation (weighted view):* 1200
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 237`, `structural_boundaries: 468`, `func_start: 277`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 126`, `high_risk_execution: 1`, `state_mutation: 686`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 131`
* *Architecture:* `io: 184`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1704.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1788.2 | **LOC:** 2013 | **CtrlFlow:** 12.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.003%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `MPY-TEST-F2-17-2` **(I/O & Config Routines)** (Impact: 4.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 232 instances
* *State Mutation (weighted view):* 1153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 470`, `func_start: 266`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 1`, `state_mutation: 689`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 163`
* *Architecture:* `io: 136`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC1264.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1730.36 | **LOC:** 2634 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.9993%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `BREAKDOWN-PARA` **(I/O & Config Routines)** (Impact: 12.5)
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `WRITE-LINE` **(I/O & Config Routines)** (Impact: 6.8)
  * `XXXXX055` **(I/O & Config Routines)** (Impact: 6.5)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 864
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 234`, `structural_boundaries: 706`, `func_start: 472`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 307`, `high_risk_execution: 1`, `state_mutation: 656`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 162`
* *Architecture:* `io: 615`
* *Defense:* `safety: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/NC2074.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 1724.7 | **LOC:** 2720 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (41.5575%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `PRINT-DETAIL` **(I/O & Config Routines)** (Impact: 5.6)
  * `HEAD-ROUTINE` **(Compute Cores)** (Impact: 5.2)
  * `COLUMN-NAMES-ROUTINE` **(I/O & Config Routines)** (Impact: 4.5)
  * `FAIL-ROUTINE` **(I/O & Config Routines)** (Impact: 4.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 53 instances
* *State Mutation (weighted view):* 982
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 393`, `func_start: 473`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 272`, `high_risk_execution: 1`, `state_mutation: 876`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 183`
* *Architecture:* `io: 375`
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/test_files/Cobol85PositiveTestsSuite/positive/IX2144.2.cbl` (COBOL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1687.7 | **LOC:** 2354 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (33.6572%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `START-TEST-GF-37` **(I/O & Config Routines)** (Impact: 9.6)
  * `START-TEST-GF-09` **(I/O & Config Routines)** (Impact: 8.4)
  * `START-TEST-GF-27` **(I/O & Config Routines)** (Impact: 8.4)
  * `ERROR-HOLD` **(I/O & Config Routines)** (Impact: 8.3)
  * `START-TEST-GF-07` **(I/O & Config Routines)** (Impact: 8.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 260 instances
* *State Mutation (weighted view):* 1122
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 261`, `structural_boundaries: 287`, `func_start: 182`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 1`, `state_mutation: 602`, `dead_code: 4`, `fragile_debt: 3`, `unreferenced_by_name: 56`
* *Architecture:* `io: 633`
* *Defense:* `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.175
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `clients/cobol-lsp-vscode-extension/src/services/ControlFlowService.ts` -> Churn: **90.19%** | Cog Load: 53.0288% | Debt: 8.7564%
- `clients/cobol-lsp-vscode-extension/src/services/ExternalAPIsService.ts` -> Churn: **59.81%** | Cog Load: 57.9499% | Debt: 0.0%
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/preprocessor/cbl/CblDiagnosticException.java` -> Churn: **52.17%** | Cog Load: 6.7907% | Debt: 81.7574%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `clients/cobol-lsp-vscode-extension/src/__tests__/provider/TarCopybookFileSystemProvider.spec.ts` -> **Aman Prashant** (100.0% isolated ownership) | Magnitude: 1104.4
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/visitor/CobolVisitor.java` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 939.62
- `clients/cobol-lsp-vscode-extension/src/test/suite/lsp.spec.copybooks.test.ts` -> **Leonid Baranov** (100.0% isolated ownership) | Magnitude: 627.43
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/copybook/libs/DatasetLib.spec.ts` -> **slavek-kucera** (100.0% isolated ownership) | Magnitude: 617.97
- `clients/cobol-lsp-vscode-extension/src/__tests__/services/copybook/libs/TarCopybookLib.spec.ts` -> **Aman Prashant** (100.0% isolated ownership) | Magnitude: 576.02

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/variable/VariableNode.java` -> **Severity: 0.045** (Bridge: 0.0005 * Flux: 100.0%)
- `server/engine/src/test/java/org/eclipse/lsp/cobol/usecases/common/CICSTestUtils.java` -> **Severity: 0.028** (Bridge: 0.0003 * Flux: 100.0%)
- `server/dialect-idms/src/main/java/org/eclipse/lsp/cobol/dialects/idms/IdmsDialect.java` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 95.0734%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/core/engine/dialects/DialectService.java` -> **Severity: 0.016** (Bridge: 0.0002 * Flux: 84.8606%)
- `server/engine/src/main/java/org/eclipse/lsp/cobol/lsp/analysis/AsyncAnalysisService.java` -> **Severity: 0.014** (Bridge: 0.0002 * Flux: 78.8551%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/Node.java` -> **Severity: 11.651** (Embedded: 0.1289 * Error Risk: 90.3839%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 11.218** (Embedded: 0.1366 * Error Risk: 82.1378%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/symbols/ProcedureId.java` -> **Severity: 9.919** (Embedded: 0.1095 * Error Risk: 90.5754%)
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/CobolText.java` -> **Severity: 9.693** (Embedded: 0.1163 * Error Risk: 83.361%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/Locality.java` -> **Severity: 9.464** (Embedded: 0.1542 * Error Risk: 61.3692%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `server/test/src/main/java/org/eclipse/lsp/cobol/test/engine/UseCaseEngine.java` -> **Severity: 2182.882** (Blast Radius: 46.776 * Doc Risk: 46.6667%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/ErrorSource.java` -> **Severity: 1596.3** (Blast Radius: 15.963 * Doc Risk: 100.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/error/SyntaxError.java` -> **Severity: 1097.9** (Blast Radius: 10.979 * Doc Risk: 100.0%)
- `server/test/src/main/java/org/eclipse/lsp/cobol/test/CobolText.java` -> **Severity: 1017.5** (Blast Radius: 10.175 * Doc Risk: 100.0%)
- `server/common/src/main/java/org/eclipse/lsp/cobol/common/model/tree/ProgramNode.java` -> **Severity: 568.0** (Blast Radius: 5.68 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
