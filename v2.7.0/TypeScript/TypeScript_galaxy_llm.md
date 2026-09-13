# ARCHITECTURAL_BRIEF: TypeScript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/TypeScript.git` |
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
| Total Artifacts | 81366 |
| Analyzed Artifacts (Scanned) | 50256 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 31110 |
| Total LOC | 2272541 |
| Volatility Index | 0.001 |
| % Scanned of codebase = | 61.8% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.0 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2399 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 0.0 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 42 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 20360 | 578773 | 40.5% |
| JAVASCRIPT | 17491 | 1557187 | 34.8% |
| PLAINTEXT | 9949 | 11 | 19.8% |
| JSON | 2423 | 136337 | 4.8% |
| MARKDOWN | 29 | 0 | 0.1% |
| YAML | 2 | 227 | 0.0% |
| SHELL | 2 | 6 | 0.0% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 40278 | 80.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9977 | 19.9% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 31110*

**Composition by Extension & Reason:**
- `.symbols`: 14016x Excluded (Unsupported Extension: '.symbols')
- `.types`: 14016x Excluded (Unsupported Extension: '.types')
- `.map`: 801x Excluded (Unsupported Extension: '.map'), 64x Excluded (Saturation: Line 1 exceeds 500 chars), 56x Unsupported Format (.map)
- `.ts`: 476x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 225x Excluded: Neighborhood Micro-Mass Limit Exceeded, 7x Excluded (Binary Format Detected)
- `.js`: 85x Excluded (Saturation: Line 94 exceeds 500 chars), 82x Excluded (Saturation: Line 95 exceeds 500 chars), 80x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.baseline`: 459x Excluded (Unsupported Extension: '.baseline')
- `.md`: 72x Excluded (Lexical Monotony: High structural repetition detected in 2354 LOC), 4x Excluded (Lexical Monotony: High structural repetition detected in 2216 LOC), 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 2x Excluded (Lexical Monotony: High structural repetition detected in 3072 LOC), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 56 LOC)
- `.diff`: 24x Excluded (Unsupported Extension: '.diff')
- `.yml`: 18x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 8560 LOC)
- `.lcl`: 13x Unsupported Format (.lcl)
- `.yaml`: 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 25.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 6.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 56.1 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 31.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 5094 | 1126 | 0 | `src/compiler/utilities.ts` |
| cleanup | 163 | 41 | 0 | `src/lib/webworker.generated.d.ts` |
| guards | 55654 | 5239 | 1 | `src/lib/webworker.generated.d.ts` |
| danger | 49877 | 9446 | 2 | `src/lib/webworker.generated.d.ts` |
| concurrency | 19906 | 2452 | 0 | `src/testRunner/unittests/evaluation/awaitUsingDeclarations.ts` |
| connectivity | 119189 | 12084 | 4 | `tests/baselines/reference/manyConstExports(target=es2015).js` |
| io | 9987 | 666 | 0 | `tests/baselines/reference/reuseProgramStructure/should-not-reuse-ambient-module-declarations-from-non-modified-files.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 127 | 27 | 0 | `src/lib/webworker.generated.d.ts` |
| time | 495 | 159 | 0 | `src/compiler/sys.ts` |
| serialization | 226 | 90 | 0 | `src/harness/fourslashImpl.ts` |
| regex | 487 | 171 | 0 | `tests/baselines/reference/parserharness.js` |
| events | 4716 | 744 | 0 | `src/lib/webworker.generated.d.ts` |
| tests | 3953 | 605 | 0 | `src/testRunner/unittests/evaluation/esDecorators.ts` |
| docs | 31144 | 3182 | 0 | `src/lib/webworker.generated.d.ts` |
| debt | 31615 | 4748 | 0 | `tests/baselines/reference/privacyAccessorDeclFile(target=es5).js` |
| mutation | 334649 | 22777 | 11 | `tests/baselines/reference/largeControlFlowGraph.js` |
| dead_code | 29319 | 10714 | 1 | `tests/baselines/reference/api/typescript.d.ts` |
| credential | 11 | 11 | 0 | `tests/baselines/reference/tsserver/cachingFileSystemInformation/npm-install-works-when-timeout-occurs-after-installation.js` |
| threat | 18610 | 4503 | 0 | `tests/baselines/reference/superInStaticMembers1(target=es5).js` |
| ml_ai | 2117 | 247 | 0 | `tests/baselines/reference/tsbuildWatch/programUpdates/with-circular-project-reference/change-builds-changes-and-reports-found-errors-message.js` |
| ui | 6898 | 1286 | 0 | `src/harness/fourslashInterfaceImpl.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `tests/baselines/reference/reuseProgramStructure/should-not-reuse-ambient-module-declarations-from-non-modified-files.js` (Hits: 651)
- `src/testRunner/unittests/tsserver/projectReferenceCompileOnSave.ts` (Hits: 296)
- `src/testRunner/unittests/services/convertToAsyncFunction.ts` (Hits: 271)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **package.json** (`package.json`) — 91 inbound connections
2. **module.ts** (`src/compiler/transformers/module/module.ts`) — 83 inbound connections
3. **lib.ts** (`tests/cases/projects/reference-path-static/lib.ts`) — 61 inbound connections
4. **path.ts** (`src/compiler/path.ts`) — 45 inbound connections
5. **utils.cjs** (`scripts/eslint/rules/utils.cjs`) — 40 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **ts.ts** (`src/compiler/_namespaces/ts.ts`) — 75 outbound dependencies
2. **nodeFactory.ts** (`src/compiler/factory/nodeFactory.ts`) — 75 outbound dependencies
3. **ts.codefix.ts** (`src/services/_namespaces/ts.codefix.ts`) — 74 outbound dependencies
4. **program.ts** (`src/compiler/program.ts`) — 71 outbound dependencies
5. **ramdaToolsNoInfinite2.js** (`tests/baselines/reference/ramdaToolsNoInfinite2.js`) — 51 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `getCompletionData` (@ `src/services/completions.ts`) -> Impact: **1290.5** | LOC: 1135
- `createScanner` (@ `src/compiler/scanner.ts`) -> Impact: **1121.7** | LOC: 1278
  * *Intent:* // Creates a scanner over a (possibly unspecified) range of a piece of text.
- `getSymbolDisplayPartsDocumentationAndSymbolKindWorker` (@ `src/services/symbolDisplay.ts`) -> Impact: **919.7** | LOC: 749
- `run` (@ `tests/baselines/reference/enumLiteralsSubtypeReduction.js`) -> Impact: **778.3** | LOC: 1028
- `run` (@ `tests/baselines/reference/enumLiteralsSubtypeReduction.js`) -> Impact: **778.3** | LOC: 1028
- `formatSpanWorker` (@ `src/services/formatting/formatting.ts`) -> Impact: **749.0** | LOC: 877
- `scanRegularExpressionWorker` (@ `src/compiler/scanner.ts`) -> Impact: **721.9** | LOC: 997
- `createProgram` (@ `src/compiler/program.ts`) -> Impact: **672.3** | LOC: 1051
- `createSyntacticTypeNodeBuilder` (@ `src/compiler/expressionToTypeNode.ts`) -> Impact: **654.3** | LOC: 927
  * *Intent:* /** @internal */
- `createResolutionCache` (@ `src/compiler/resolutionCache.ts`) -> Impact: **651.0** | LOC: 1060
  * *Intent:* /** @internal */

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/baselines/reference` | 24214 | 455703.88 | 3.9% | 0.0% |
| `tests/cases/fourslash` | 6303 | 109344.05 | 0.35% | 0.0% |
| `tests/cases/compiler` | 6366 | 84710.59 | 1.68% | 0.0% |
| `src/compiler` | 38 | 67384.7 | 36.35% | 13.6% |
| `tests/baselines/reference/tsserver/projectReferences` | 67 | 34790.73 | 6.32% | 0.0% |
| `src/services` | 39 | 32852.5 | 32.94% | 9.87% |
| `src/compiler/transformers` | 21 | 14810.06 | 24.75% | 14.17% |
| `src/harness` | 24 | 14452.06 | 50.93% | 11.05% |
| `tests/baselines/reference/tsserver/declarationFileMaps` | 21 | 13190.92 | 6.58% | 0.0% |
| `src/services/codefixes` | 73 | 11397.54 | 14.26% | 53.32% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/compiler/factory/nodeTests.ts` -> **100.0%** Exposure
- `src/harness/fakesHosts.ts` -> **100.0%** Exposure
- `src/lib/decorators.d.ts` -> **100.0%** Exposure
- `src/lib/es2015.collection.d.ts` -> **100.0%** Exposure
- `src/lib/es2015.core.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/failed-tests.cjs` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseBuildOptions/errors on missing argument.js` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseCommandLine/Handles did you mean for misspelt flags.js` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseCommandLine/Handles may only be used with --build flags.js` -> **100.0%** Exposure
- `src/compiler/performance.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/baselines/reference/api/typescript.d.ts` -> **1269** Orphaned Functions | **194** Duplicates
- `src/lib/webworker.generated.d.ts` -> **409** Orphaned Functions | **220** Duplicates
- `tests/baselines/reference/privacyAccessorDeclFile(target=es5).js` -> **0** Orphaned Functions | **562** Duplicates
- `tests/baselines/reference/privacyFunctionReturnTypeDeclFile.js` -> **0** Orphaned Functions | **527** Duplicates
- `tests/baselines/reference/privacyAccessorDeclFile(target=es2015).js` -> **0** Orphaned Functions | **492** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `5418` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/testRunner/parallel/host.ts` (TYPESCRIPT) -> Cumulative Risk: **705.96**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 885.6 | **LOC:** 661 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9997%), Cognitive Load (96.574%)
- **Heaviest Functions:** `start` (Impact: 205.2), `startDelayed` (Impact: 155.0), `killChild` (Impact: 74.4)

### 2. `src/harness/util.ts` (TYPESCRIPT) -> Cumulative Risk: **696.24**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 135.52 | **LOC:** 131 | **CtrlFlow:** 41.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Safety Score (91.7551%), Concurrency (90.6769%)
- **Heaviest Functions:** `dedent` (Impact: 19.2), `getByteOrderMarkLength` (Impact: 18.9), `guessIndentation` (Impact: 12.0)

### 3. `src/harness/fakesHosts.ts` (TYPESCRIPT) -> Cumulative Risk: **692.37**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 346.58 | **LOC:** 425 | **CtrlFlow:** 17.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9129%), Documentation (99.0566%)
- **Heaviest Functions:** `getSourceFile` (Impact: 32.9), `readDirectory` (Impact: 12.4), `readDirectory` (Impact: 12.4)

### 4. `src/testRunner/runner.ts` (TYPESCRIPT) -> Cumulative Risk: **660.63**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 256.84 | **LOC:** 278 | **CtrlFlow:** 32.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9999%), Safety Score (93.9805%)
- **Heaviest Functions:** `tryGetConfig` (Impact: 96.5), `runTests` (Impact: 16.8), `startTestEnvironment` (Impact: 6.7)

### 5. `src/compiler/program.ts` (TYPESCRIPT) -> Cumulative Risk: **653.67**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 4868.1 | **LOC:** 5202 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.5761%), Churn (87.58%), Verification (80.0%)
- **Heaviest Functions:** `createProgram` (Impact: 672.3), `verifyCompilerOptions` (Impact: 186.8), `getJSSyntacticDiagnosticsForFile` (Impact: 163.9)

### 6. `src/compiler/binder.ts` (TYPESCRIPT) -> Cumulative Risk: **652.74**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 2959.82 | **LOC:** 3917 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9021%), Churn (95.83%), Documentation (90.6593%)
- **Heaviest Functions:** `bindWorker` (Impact: 183.6), `declareSymbol` (Impact: 139.8), `bindChildren` (Impact: 78.0)

### 7. `src/tsserver/nodeServer.ts` (TYPESCRIPT) -> Cumulative Risk: **644.39**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 737.84 | **LOC:** 721 | **CtrlFlow:** 25.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9392%), Documentation (91.8033%), Safety Score (84.7834%)
- **Heaviest Functions:** `startNodeSession` (Impact: 139.9), `initializeNodeSystem` (Impact: 73.5), `watchDirectory` (Impact: 40.4)

### 8. `src/services/preProcess.ts` (TYPESCRIPT) -> Cumulative Risk: **643.55**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 561.34 | **LOC:** 452 | **CtrlFlow:** 32.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Safety Score (91.4189%), Cognitive Load (89.1473%)
- **Heaviest Functions:** `preProcessFile` (Impact: 259.8), `tryConsumeImport` (Impact: 43.2), `tryConsumeExport` (Impact: 27.6)

### 9. `src/harness/harnessIO.ts` (TYPESCRIPT) -> Cumulative Risk: **638.36**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 1659.0 | **LOC:** 1593 | **CtrlFlow:** 30.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9943%), Documentation (97.7273%), Safety Score (89.3189%)
- **Heaviest Functions:** `sanitizeTestFilePath` (Impact: 206.7), `doTypeAndSymbolBaseline` (Impact: 174.4), `doJsEmitBaseline` (Impact: 79.5)

### 10. `src/harness/tsserverLogger.ts` (TYPESCRIPT) -> Cumulative Risk: **637.05**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 263.82 | **LOC:** 179 | **CtrlFlow:** 37.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.6553%)
- **Heaviest Functions:** `sanitizeLog` (Impact: 60.8), `handleLoggerGroup` (Impact: 11.7), `replaceAll` (Impact: 11.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `tests/baselines/reference/largeControlFlowGraph.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20415.06 | **LOC:** 20014 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 20000`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/manyConstExports(target=es2015).js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20317.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 5100`
* *Architecture:* `api: 15000`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/manyConstExports(target=es5).js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 20317.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 5100`
* *Architecture:* `api: 15000`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7871.74 | **LOC:** 10824 | **CtrlFlow:** 31.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (36.7537%), Tech Debt (11.4822%)
**Top Internal Functions/Classes:**
  * `parseJSDocCommentWorker` (Impact: 544.5)
  * `isListElement` (Impact: 116.3)
    * *Intent:* // True if positioned at the start of a list element
  * `parseTagComments` (Impact: 71.5)
  * `parseJsonText` (Impact: 70.5)
  * `isStartOfType` (Impact: 66.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 403 instances
* *State Mutation (weighted view):* 1306
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2600`, `structural_boundaries: 1923`, `args: 786`, `func_start: 850`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 500`, `dead_code: 32`, `planned_debt: 16`, `fragile_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 158`, `import: 1`
* *Defense:* `safety: 21`, `doc: 36`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ) 
        return ModuleKind.ESNext;
    
    if (mode ===, ts.js, ts.performance.js,  We don, :
                        tag = parseImportTag(start, end: number, have already parsed their comments earlier
                if (!indentText) 
                    margin += end - pos;
                
                return parseTagComments(margin, indentText);
                        break;
                
                return tag;
            

            function parseTrailingTagComments(pos: number...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/compiler/utilities.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 7648.14 | **LOC:** 12448 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 40.0%
- **Risk Profile:** Cognitive Load (25.6929%), Tech Debt (9.9337%)
**Top Internal Functions/Classes:**
  * `resolveNameHelper` (Impact: 472.1)
  * `createNameResolver` (Impact: 349.3)
    * *Intent:* /** @internal */
  * `isSourceElement` (Impact: 139.3)
    * *Intent:* /** @internal */
  * `createEvaluator` (Impact: 80.1)
    * *Intent:* /** @internal */
  * `evaluate` (Impact: 79.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 338 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 1087
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3468`, `structural_boundaries: 2790`, `args: 1078`, `func_start: 936`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 411`, `dead_code: 19`, `planned_debt: 9`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 99`, `api: 746`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 278`, `doc: 773`, `immutability_locks: 129`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` ..., ts.js, module, name
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/services/completions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6644.84 | **LOC:** 6174 | **CtrlFlow:** 34.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (54.4724%), Tech Debt (10.4486%)
**Top Internal Functions/Classes:**
  * `getCompletionData` (Impact: 1290.5)
  * `createCompletionEntry` (Impact: 527.9)
  * `getCompletionEntriesFromSymbols` (Impact: 362.4)
    * *Intent:* /** @internal */
  * `isSolelyIdentifierDefinitionLocation` (Impact: 146.3)
    * *Intent:* /** * @returns true if we are certain that the currently edited location must define a new location;...
  * `getCompletionEntryCodeActionsAndSourceDisplay` (Impact: 133.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 250 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 781
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1708`, `structural_boundaries: 882`, `args: 288`, `func_start: 198`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 281`, `dead_code: 33`, `planned_debt: 13`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 32`, `concurrency: 7`, `import: 6`
* *Defense:* `safety: 90`, `doc: 78`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $entry.source, ..., ts.Completions.js, ts.js, other, foo, moduleName, os
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/cases/fourslash/formattingFatArrowFunctions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 6414.82 | **LOC:** 294 | **CtrlFlow:** 34.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2501%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 108`, `args: 103`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `dead_code: 1`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/factory/nodeFactory.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5944.04 | **LOC:** 7543 | **CtrlFlow:** 19.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.5466%), Tech Debt (32.2084%)
**Top Internal Functions/Classes:**
  * `createNodeFactory` (Impact: 331.0)
    * *Intent:* /** * Creates a `NodeFactory` that can be used to create and update a syntax tree. * @param flags Fl...
  * `getTransformFlagsSubtreeExclusions` (Impact: 74.3)
    * *Intent:* /** * Gets the transform flags to exclude when unioning the transform flags of a subtree. */
  * `replaceModifiers` (Impact: 55.4)
  * `createToken` (Impact: 49.8)
  * `createCallBinding` (Impact: 43.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 362 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1173`, `structural_boundaries: 1138`, `args: 647`, `func_start: 618`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1047`, `dead_code: 4`, `planned_debt: 4`, `unreferenced_by_name: 69`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 1`
* *Defense:* `safety: 24`, `doc: 25`, `test: 1`, `immutability_locks: 256`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ), ts.js, ;
        default:
            return Debug.fail(`Unsupported kind: $Debug.formatSyntaxKind(kind)`);
    


let rawTextScanner: Scanner | undefined;
const invalidValueSentinel: object = ;

function getCookedText(kind: TemplateLiteralToken[, attributes, attributes), attributes: ImportAttributes | undefined,  @api
    function updateJsxOpeningElement(node: JsxOpeningElement,  @api
    function updateJsxSelfClosingElement(node: JsxSelfClosingElement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/scanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5337.26 | **LOC:** 4102 | **CtrlFlow:** 33.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (80.4301%), Tech Debt (8.0676%)
**Top Internal Functions/Classes:**
  * `createScanner` (Impact: 1121.7)
    * *Intent:* // Creates a scanner over a (possibly unspecified) range of a piece of text.
  * `scanRegularExpressionWorker` (Impact: 721.9)
  * `scan` (Impact: 207.9)
  * `iterateCommentRanges` (Impact: 109.9)
    * *Intent:* * * @param reduce If true, accumulates the result of calling the callback in a fashion similar * to ...
  * `scanEscapeSequence` (Impact: 108.6)
    * *Intent:* // Extract from Section A.1 // EscapeSequence ::= // | CharacterEscapeSequence // | 0 (?![0-9]) // |...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 450 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1416
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1132`, `structural_boundaries: 598`, `args: 220`, `func_start: 213`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 516`, `dead_code: 4`, `planned_debt: 4`
* *Architecture:* `api: 44`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 14`, `doc: 56`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/emitter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 5166.88 | **LOC:** 6379 | **CtrlFlow:** 26.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.1227%), Tech Debt (7.754%)
**Top Internal Functions/Classes:**
  * `createPrinter` (Impact: 623.5)
  * `pipelineEmitWithHintWorker` (Impact: 469.8)
  * `emitFiles` (Impact: 304.1)
    * *Intent:* /** @internal */ // targetSourceFile is when users only want one file in entire project to be emitte...
  * `emitNodeListItems` (Impact: 145.6)
    * *Intent:* /** * Emits a list without brackets or raising events. * * NOTE: You probably don't want to call thi...
  * `emitNodeList` (Impact: 81.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1398`, `structural_boundaries: 770`, `args: 459`, `func_start: 435`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 208`, `dead_code: 6`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 25`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 41`, `doc: 46`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` );
        writePunctuation(, ts.js, ts.performance.js, :
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/program.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4868.1 | **LOC:** 5202 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (63.7587%), Tech Debt (8.6805%)
**Top Internal Functions/Classes:**
  * `createProgram` (Impact: 672.3)
  * `verifyCompilerOptions` (Impact: 186.8)
  * `getJSSyntacticDiagnosticsForFile` (Impact: 163.9)
  * `actualResolveLibrary` (Impact: 125.3)
  * `findSourceFileWorker` (Impact: 119.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 266 instances
* *State Mutation (weighted view):* 872
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1261`, `structural_boundaries: 723`, `args: 399`, `func_start: 303`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 340`, `dead_code: 5`, `planned_debt: 12`
* *Architecture:* `io: 130`, `api: 72`, `import: 1`
* *Defense:* `safety: 137`, `doc: 63`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` && elem.value.text !==, ), ) => ResolutionLoader<Entry, ): ResolutionLoader<StringLiteralLike, ): ResolutionLoader<T, ): readonly Resolution[] 
    if (entries.length === 0) return emptyArray;
    const resolutions: Resolution[] = [];
    const cache = new Map<ModeAwareCacheKey, ts.js, ts.performance.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/projectReferences/solution-with-its-own-files-and-project-is-indirectly-referenced-by-solution.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4844.88 | **LOC:** 5168 | **CtrlFlow:** 2.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.534%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 83`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 92`
* *Architecture:* `api: 26`, `import: 48`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functions, main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/harness/fourslashImpl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4142.36 | **LOC:** 5216 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.9296%), Tech Debt (8.2034%)
**Top Internal Functions/Classes:**
  * `verifyImportFixModuleSpecifiers` (Impact: 518.7)
  * `getBaselineContentForFile` (Impact: 219.5)
  * `parseFileContent` (Impact: 112.5)
  * `verifyCompletionsWorker` (Impact: 98.3)
  * `constructor` (Impact: 84.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 295 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 985
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1180`, `structural_boundaries: 730`, `args: 542`, `func_start: 330`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 3`, `state_mutation: 395`, `dead_code: 3`, `planned_debt: 7`
* *Architecture:* `io: 17`, `api: 187`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 109`, `doc: 9`, `test: 24`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` FourSlashInterface.js, Harness.js, Utils.js, fakes.js, ts.js, vfs.js, vpath.js, harnessLanguageService.js...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/editorServices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4068.04 | **LOC:** 5728 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (24.4493%), Tech Debt (10.1091%)
**Top Internal Functions/Classes:**
  * `forEachResolvedProjectReferenceProjectLoad` (Impact: 118.6)
    * *Intent:* /** * Goes through parentConfig's project references and finds, creates or reloads project per kind ...
  * `findCreateOrReloadConfiguredProject` (Impact: 111.0)
    * *Intent:* /** * Depending on kind * - Find the configuedProject and return it - if allowDeferredClosed is set ...
  * `tryFindDefaultConfiguredProjectForOpenScriptInfoOrClosedFileInfo` (Impact: 106.1)
  * `onWildCardDirectoryWatcherInvoke` (Impact: 72.7)
  * `applySafeListWorker` (Impact: 63.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 286 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 903
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1149`, `structural_boundaries: 737`, `args: 426`, `func_start: 277`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 331`, `dead_code: 6`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 151`, `api: 134`, `concurrency: 16`, `import: 2`
* *Defense:* `safety: 135`, `doc: 195`, `immutability_locks: 100`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.js, ts.server.js, protocol.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/moduleNameResolver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 4016.62 | **LOC:** 3429 | **CtrlFlow:** 33.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (38.9708%), Tech Debt (30.4411%)
**Top Internal Functions/Classes:**
  * `getLoadModuleFromTargetExportOrImport` (Impact: 272.0)
    * *Intent:* /** * Gets the self-recursive function specialized to retrieving the targeted import/export element ...
  * `nodeModuleNameResolverWorker` (Impact: 220.1)
  * `loadModuleFromTargetExportOrImport` (Impact: 217.4)
  * `resolveTypeReferenceDirective` (Impact: 187.5)
    * *Intent:* /** * @param {string | undefined} containingFile - file that contains type reference directive, can ...
  * `tryAddingExtensions` (Impact: 162.0)
    * *Intent:* /** Try to return an existing file that adds one of the `extensions` to `candidate`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 934`, `structural_boundaries: 505`, `args: 249`, `func_start: 220`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 150`, `dead_code: 3`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 73`, `api: 71`
* *Defense:* `safety: 73`, `doc: 102`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` )
        ) 
            traceIfEnabled(state,    1. For each ancestor node_modules directory, );

    function tryResolve(extensions: Extensions, , ts.js, file2,  true);
        const resolved = tryLoadModuleUsingOptionalResolutionSettings(extensions, ;
            const diagnosticResult = tryResolve(extensions & (Extensions.TypeScript | Extensions.Declaration)...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/services/utilities.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3512.86 | **LOC:** 4237 | **CtrlFlow:** 35.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.2968%), Tech Debt (7.8631%)
**Top Internal Functions/Classes:**
  * `getAdjustedLocation` (Impact: 191.8)
  * `isCompletedNode` (Impact: 129.7)
  * `getNodeKind` (Impact: 95.8)
    * *Intent:* /** @internal */
  * `getTokenAtPositionWorker` (Impact: 88.0)
    * *Intent:* /** Get the token whose text contains the position */
  * `createPackageJsonImportFilter` (Impact: 77.2)
    * *Intent:* /** @internal */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1154`, `structural_boundaries: 935`, `args: 351`, `func_start: 307`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 135`, `dead_code: 40`, `planned_debt: 2`
* *Architecture:* `io: 10`, `api: 214`
* *Defense:* `safety: 49`, `doc: 251`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.js, [|module|]
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/projectReferences/solution-with-its-own-files-and-project-found-is-not-solution-but-references-open-file-through-project-reference.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3404.04 | **LOC:** 3899 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.7774%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 92
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 58`, `args: 10`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 82`
* *Architecture:* `api: 22`, `import: 29`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functions, main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/testRunner/unittests/evaluation/forAwaitOf.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3386.42 | **LOC:** 336 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9891%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 37 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 277
* *State Mutation (weighted view):* 57
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 128`, `args: 56`, `func_start: 58`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 19`
* *Architecture:* `api: 15`, `concurrency: 92`, `import: 2`
* *Defense:* `safety: 14`, `test: 12`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` evaluator.js, ts.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/tsserver/projectReferences/project-is-indirectly-referenced-by-solution.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 3183.1 | **LOC:** 4508 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.6846%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 101
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 55`, `args: 8`, `func_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 91`
* *Architecture:* `api: 20`, `import: 27`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` functions, main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/binder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2959.82 | **LOC:** 3917 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (52.3166%), Tech Debt (8.3326%)
**Top Internal Functions/Classes:**
  * `bindWorker` (Impact: 183.6)
  * `declareSymbol` (Impact: 139.8)
    * *Intent:* /** * Declares a Symbol for the node and adds it to symbols. Reports errors for conflicting identifi...
  * `bindChildren` (Impact: 78.0)
  * `bindContainer` (Impact: 75.5)
    * *Intent:* // All container nodes are kept on a linked list in declaration order. This list is used by // the g...
  * `getContainerFlags` (Impact: 65.3)
    * *Intent:* /** @internal */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 743
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1056`, `structural_boundaries: 417`, `args: 191`, `func_start: 175`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 1`, `state_mutation: 317`, `dead_code: 10`, `planned_debt: 6`
* *Architecture:* `io: 3`, `api: 10`, `import: 1`
* *Defense:* `safety: 12`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.js, ts.performance.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/services/services.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2881.12 | **LOC:** 3623 | **CtrlFlow:** 23.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.5211%), Tech Debt (40.6527%)
**Top Internal Functions/Classes:**
  * `createLanguageService` (Impact: 498.0)
  * `toggleMultilineComment` (Impact: 77.6)
  * `visit` (Impact: 75.2)
  * `computeNamedDeclarations` (Impact: 62.4)
  * `synchronizeHostDataWorker` (Impact: 56.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 516`, `args: 320`, `func_start: 270`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 165`, `dead_code: 6`, `planned_debt: 24`, `fragile_debt: 9`, `duplicate_logic: 6`
* *Architecture:* `io: 19`, `api: 119`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 41`, `doc: 19`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.053
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.NavigateTo.js, ts.NavigationBar.js, ts.js, ts.refactor.js, classifier.js, classifier2020.js, mod, something
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/parserharness.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2737.84 | **LOC:** 3820 | **CtrlFlow:** 17.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.3261%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `get` (Impact: 55.8)
  * `generateDeclFile` (Impact: 39.8)
    * *Intent:* /** Generates a .d.ts file for the given code * @param verifyNoDeclFile pass true when the given cod...
  * `makeUnitsFromTest` (Impact: 39.4)
    * *Intent:* /** Given a test file containing // @Filename directives, return an array of named units of code to ...
  * `getTypeInfoName` (Impact: 39.2)
  * `makeUnitsFromTest` (Impact: 39.1)
    * *Intent:* /** Given a test file containing // @Filename directives, return an array of named units of code to ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Rce:* 2 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 333 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 100
* *Sec Tainted Injection (weighted view):* 2
* *State Mutation (weighted view):* 1234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 541`, `structural_boundaries: 905`, `args: 349`, `func_start: 268`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 4`, `state_mutation: 568`, `dead_code: 12`, `planned_debt: 8`, `fragile_debt: 21`, `duplicate_logic: 20`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 91`, `concurrency: 20`, `import: 2`
* *Defense:* `safety: 130`, `doc: 56`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/enumLiteralsSubtypeReduction.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2674.8 | **LOC:** 4117 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.2007%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `run` (Impact: 778.3)
  * `run` (Impact: 778.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 1036
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 1025`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 1024`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/binaryArithmeticControlFlowGraphNotTooLarge.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2665.02 | **LOC:** 2565 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (25.1587%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `foo` (Impact: 10.6)
    * *Intent:* //// [tests/cases/compiler/binaryArithmeticControlFlowGraphNotTooLarge.ts] //// //// [binaryArithmet...
  * `foo` (Impact: 8.0)
    * *Intent:* // Repro from #29926 (expanded 10x for good measure)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 48 instances
* *State Mutation (weighted view):* 2596
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 2`, `args: 2`, `func_start: 2`
* *Risk/State:* `state_mutation: 2500`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/commandLineParser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 2628.12 | **LOC:** 4301 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 33.3%
- **Risk Profile:** Cognitive Load (17.1779%), Tech Debt (10.1179%)
**Top Internal Functions/Classes:**
  * `parseJsonConfigFileContentWorker` (Impact: 168.8)
    * *Intent:* /** * Parse the contents of a config file from json or json source file (tsconfig.json). * @param js...
  * `parseConfig` (Impact: 103.5)
    * *Intent:* /** * This *just* extracts options/include/exclude/files out of a config file. * It does *not* resol...
  * `convertToJson` (Impact: 91.7)
    * *Intent:* /** * Convert the json syntax tree into the json value and report errors * This returns the json val...
  * `parseOwnConfigOfJsonSourceFile` (Impact: 84.7)
  * `parseOptionValue` (Impact: 78.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 612`, `structural_boundaries: 613`, `args: 199`, `func_start: 138`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 168`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 51`, `api: 74`
* *Defense:* `safety: 37`, `doc: 76`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.02
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` ts.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler/binder.ts` -> Churn: **95.83%** | Cog Load: 52.3166% | Debt: 8.3326%
- `src/compiler/types.ts` -> Churn: **90.33%** | Cog Load: 5.6418% | Debt: 96.0305%
- `src/compiler/program.ts` -> Churn: **87.58%** | Cog Load: 63.7587% | Debt: 8.6805%
- `tests/baselines/reference/tsc/commandLine/help-all.js` -> Churn: **77.49%** | Cog Load: 81.5039% | Debt: 0.0%
- `src/lib/webworker.generated.d.ts` -> Churn: **75.18%** | Cog Load: 14.8558% | Debt: 100.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/compiler/moduleNameResolver.ts` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 4016.62
- `src/compiler/core.ts` -> **Jake Bailey** (100.0% isolated ownership) | Magnitude: 2294.72
- `src/compiler/resolutionCache.ts` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 1983.08
- `src/compiler/utilitiesPublic.ts` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 1880.96
- `tests/baselines/reference/emitter.asyncGenerators.classMethods.es5(target=es5).js` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 1654.28

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/compiler/transformers/module/module.ts` -> **Severity: 44.084** (Blast Radius: 1.396 * Doc Risk: 31.5789%)
- `src/typescript/typescript.ts` -> **Severity: 35.7** (Blast Radius: 0.357 * Doc Risk: 100.0%)
- `tests/cases/projects/MultipleLevels/A/A.ts` -> **Severity: 32.4** (Blast Radius: 0.324 * Doc Risk: 100.0%)
- `src/compiler/transformers/jsx.ts` -> **Severity: 29.056** (Blast Radius: 0.361 * Doc Risk: 80.4878%)
- `src/testRunner/unittests/tsbuildWatch/reexport.ts` -> **Severity: 20.3** (Blast Radius: 0.203 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
