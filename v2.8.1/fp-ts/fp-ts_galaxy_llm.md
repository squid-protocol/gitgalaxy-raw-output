# ARCHITECTURAL_BRIEF: fp-ts
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gcanti/fp-ts.git` |
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
| Total Artifacts | 431 |
| Analyzed Artifacts (Scanned) | 276 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 155 |
| Total LOC | 43879 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 64.0% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3426 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2655 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7271 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 11 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 263 | 43769 | 95.3% |
| JSON | 8 | 84 | 2.9% |
| MARKDOWN | 3 | 0 | 1.1% |
| HTML | 1 | 26 | 0.4% |
| PLAINTEXT | 1 | 0 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Typed Library` (z +1.27; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 33%, Generic / Templated Code Files 28%, Callbacks & Closures Files 20%, Data / Markup / Trivial 13%, Interface Declarations Files 3%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 272 | 98.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 1.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 155*

**Composition by Extension & Reason:**
- `.md`: 136x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 3x Packed Payload Guard (Impossible Density: 3.19 hits/line), 1x Packed Payload Guard (Impossible Density: 3.20 hits/line), 1x Packed Payload Guard (Impossible Density: 3.58 hits/line)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11222 LOC)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 49.9 | 3.4 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.8 | 22.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 88.1 | 2.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 12.5 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 36.8 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.2 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 98.6 | 8.0 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 29.3 | 0.1 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 69.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 30.0 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 754 | 208 | 7 | `src/ReadonlyArray.ts` |
| cleanup | 2 | 2 | 0 | `examples/fp-ts-to-the-max-I.ts` |
| guards | 1582 | 156 | 15 | `src/pipeable.ts` |
| danger | 403 | 72 | 4 | `src/Apply.ts` |
| concurrency | 1356 | 47 | 1 | `test/ReaderTaskEither.ts` |
| connectivity | 4881 | 169 | 58 | `src/pipeable.ts` |
| io | 61 | 6 | 0 | `scripts/linter.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `scripts/release.ts` |
| time | 40 | 6 | 0 | `test/Date.ts` |
| serialization | 17 | 10 | 0 | `scripts/build.ts` |
| regex | 28 | 22 | 0 | `scripts/linter.ts` |
| events | 66 | 16 | 0 | `dtslint/Option.ts` |
| tests | 2017 | 80 | 24 | `test/ReadonlyArray.ts` |
| docs | 4133 | 117 | 48 | `src/ReaderTaskEither.ts` |
| debt | 153 | 48 | 2 | `src/ReadonlyArray.ts` |
| mutation | 4587 | 195 | 51 | `src/ReadonlyArray.ts` |
| dead_code | 13 | 9 | 0 | `dtslint/Apply.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 143 | 70 | 1 | `src/ReadonlyRecord.ts` |
| ml_ai | 29 | 9 | 0 | `src/Random.ts` |
| ui | 482 | 26 | 0 | `src/ReaderTaskEither.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.5**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/linter.ts` (Hits: 22)
- `scripts/FileSystem.ts` (Hits: 18)
- `scripts/build.ts` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **function.ts** (`src/function.ts`) — 101 inbound connections
2. **util.ts** (`test/util.ts`) — 79 inbound connections
3. **HKT.ts** (`src/HKT.ts`) — 71 inbound connections
4. **Either.ts** (`src/Either.ts`) — 56 inbound connections
5. **number.ts** (`src/number.ts`) — 51 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/index.ts`) — 121 outbound dependencies
2. **ReadonlyArray.ts** (`src/ReadonlyArray.ts`) — 48 outbound dependencies
3. **Array.ts** (`src/Array.ts`) — 47 outbound dependencies
4. **Record.ts** (`src/Record.ts`) — 41 outbound dependencies
5. **ReaderTaskEither.ts** (`src/ReaderTaskEither.ts`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `isPositive` **(Compute Cores)** (@ `test/ReadonlyArray.ts`) -> Impact: **69.5** | LOC: 145
- `pipe` **(Many-Argument Workhorses)** (@ `src/function.ts`) -> Impact: **68.4** | LOC: 39
- `compose` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **67.1** | LOC: 1313
- `flow` **(Many-Argument Workhorses)** (@ `src/function.ts`) -> Impact: **62.5** | LOC: 49
- `altW` **(Generic / Templated Code)** (@ `src/StateReaderTaskEither.ts`) -> Impact: **45.7** | LOC: 830
  * *Intent:* /** * Less strict version of [`alt`](#alt). * * The `W` suffix (short for **W**idening) means that the environment, the error and the return types wil...
- `parseType` **(Compute Cores)** (@ `scripts/linter.ts`) -> Impact: **39.8** | LOC: 89
- `partitionMap` **(Generic / Templated Code)** (@ `src/TaskEither.ts`) -> Impact: **37.0** | LOC: 706
- `alt` **(Generic / Templated Code)** (@ `src/ReaderEither.ts`) -> Impact: **35.9** | LOC: 614
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **33.9** | LOC: 84
  * *Intent:* /** @deprecated */
- `fromReaderIOK` **(Generic / Templated Code)** (@ `src/ReaderTaskEither.ts`) -> Impact: **30.2** | LOC: 575
  * *Intent:* /** * @category lifting * @since 2.13.0 */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 115 | 14841.54 | 3.11% | 2.82% |
| `test` | 81 | 4314.39 | 5.55% | 0.0% |
| `dtslint` | 44 | 681.21 | 0.5% | 5.41% |
| `scripts` | 6 | 285.2 | 3.91% | 13.74% |
| `__monolith__` | 12 | 180.56 | 0.34% | 0.0% |
| `examples` | 3 | 104.12 | 5.61% | 0.0% |
| `perf/Task` | 3 | 51.08 | 0.0% | 0.0% |
| `perf/function` | 2 | 35.8 | 27.61% | 50.0% |
| `perf/ReaderTask` | 1 | 18.52 | 0.0% | 0.0% |
| `perf/ReaderTaskEither` | 1 | 18.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `dtslint/index.ts` -> **88.0797%** Exposure
- `src/Applicative.ts` -> **70.3784%** Exposure
- `src/Ord.ts` -> **57.4864%** Exposure
- `dtslint/Apply.ts` -> **50.0%** Exposure
- `dtslint/NonEmptyArray.ts` -> **50.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/NonEmptyArray.ts` -> **98.5842%** Exposure
- `src/Set.ts` -> **98.4137%** Exposure
- `perf/function/flow.ts` -> **98.2014%** Exposure
- `perf/function/pipe.ts` -> **98.2014%** Exposure
- `src/Show.ts` -> **98.2014%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `test/TaskOption.ts` -> **0** Orphaned Functions | **6** Duplicates
- `test/IOEither.ts` -> **0** Orphaned Functions | **4** Duplicates
- `test/ReaderTaskEither.ts` -> **0** Orphaned Functions | **4** Duplicates
- `test/State.ts` -> **0** Orphaned Functions | **4** Duplicates
- `test/TaskEither.ts` -> **0** Orphaned Functions | **4** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `241` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `perf/function/flow.ts` (TYPESCRIPT) -> Cumulative Risk: **504.6**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.01)
- **Magnitude:** 17.68 | **LOC:** 36 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.2014%), Safety Score (86.8266%)
- **Heaviest Functions:** `flow2` (Callbacks & Closures, Impact: 3.3), `g` (Callbacks & Closures, Impact: 2.3), `f` (Interface Declarations, Impact: 1.5)

### 2. `src/Apply.ts` (TYPESCRIPT) -> Cumulative Risk: **491.72**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.01)
- **Magnitude:** 372.16 | **LOC:** 714 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Safety Score (90.8389%), Documentation (89.5833%)
- **Heaviest Functions:** `getRecordConstructor` (Compute Cores, Impact: 14.6), `curried` (Callbacks & Closures, Impact: 6.5), `apS` (Generic / Templated Code, Impact: 4.0)

### 3. `perf/function/pipe.ts` (TYPESCRIPT) -> Cumulative Risk: **481.89**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Declarative / Non-Code` (z +3.09)
- **Magnitude:** 18.12 | **LOC:** 33 | **CtrlFlow:** 3.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.2014%), Safety Score (79.7611%)
- **Heaviest Functions:** `pipe2` (Generic / Templated Code, Impact: 3.8), `g` (Callbacks & Closures, Impact: 2.3), `f` (Interface Declarations, Impact: 1.5)

### 4. `src/ReadonlyArray.ts` (TYPESCRIPT) -> Cumulative Risk: **474.41**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.39)
- **Magnitude:** 933.7 | **LOC:** 2665 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (94.1685%), Verification (80.0%)
- **Heaviest Functions:** `concat` (Many-Argument Workhorses, Impact: 16.2), `union` (Generic / Templated Code, Impact: 11.3), `elem` (Generic / Templated Code, Impact: 9.9)

### 5. `src/NonEmptyArray.ts` (TYPESCRIPT) -> Cumulative Risk: **471.92**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.22)
- **Magnitude:** 493.98 | **LOC:** 1408 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (98.5842%), Verification (80.0%)
- **Heaviest Functions:** `concat` (Many-Argument Workhorses, Impact: 13.5), `group` (Generic / Templated Code, Impact: 9.0), `rotate` (Generic / Templated Code, Impact: 8.8)

### 6. `src/ReadonlyNonEmptyArray.ts` (TYPESCRIPT) -> Cumulative Risk: **471.06**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.29)
- **Magnitude:** 533.7 | **LOC:** 1498 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), State Flux (96.7557%), Verification (80.0%)
- **Heaviest Functions:** `concat` (Many-Argument Workhorses, Impact: 14.4), `group` (Generic / Templated Code, Impact: 9.0), `uniq` (Compute Cores, Impact: 8.4)

### 7. `src/Array.ts` (TYPESCRIPT) -> Cumulative Risk: **466.65**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.46)
- **Magnitude:** 794.74 | **LOC:** 3021 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Api Exposure (99.5548%), State Flux (88.8319%), Verification (80.0%)
- **Heaviest Functions:** `concat` (Many-Argument Workhorses, Impact: 21.7), `separate` (Generic / Templated Code, Impact: 15.7), `union` (Generic / Templated Code, Impact: 11.4)

### 8. `src/Map.ts` (TYPESCRIPT) -> Cumulative Risk: **464.94**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z -0.06)
- **Magnitude:** 375.56 | **LOC:** 925 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (90.9869%), Api Exposure (80.7298%), Verification (80.0%)
- **Heaviest Functions:** `concat` (Compute Cores, Impact: 11.9), `getMonoid` (Generic / Templated Code, Impact: 11.7), `lookupWithKey` (Generic / Templated Code, Impact: 11.4)

### 9. `src/ReadonlySet.ts` (TYPESCRIPT) -> Cumulative Risk: **462.75**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.03)
- **Magnitude:** 290.0 | **LOC:** 605 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (96.8119%), Api Exposure (81.9163%), Verification (80.0%)
- **Heaviest Functions:** `partitionMap` (Generic / Templated Code, Impact: 14.4), `separate` (Generic / Templated Code, Impact: 11.9), `union` (Generic / Templated Code, Impact: 11.5)

### 10. `src/Set.ts` (TYPESCRIPT) -> Cumulative Risk: **461.46**
- **Archetype:** `file_cluster_6` (Distance: N/A IQR)
- **Composition Archetype:** `Generic / Templated Code Files` (z +0.23)
- **Magnitude:** 226.36 | **LOC:** 495 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (98.4137%), Verification (80.0%), Api Exposure (77.8753%)
- **Heaviest Functions:** `partitionMap` (Generic / Templated Code, Impact: 14.4), `separate` (Generic / Templated Code, Impact: 11.8), `union` (Generic / Templated Code, Impact: 11.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/pipeable.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 1097.74 | **LOC:** 2612 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7995%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compose` **(Generic / Templated Code)** (Impact: 67.1)
  * `pipeable` **(Generic / Templated Code)** (Impact: 33.9)
    * *Intent:* /** @deprecated */
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
    * *Intent:* /** * @category zone of death * @since 2.0.0 * @deprecated */
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
    * *Intent:* /** @deprecated */
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
    * *Intent:* /** @deprecated */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 2247`, `args: 1162`, `func_start: 224`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 36`
* *Architecture:* `api: 313`, `import: 24`
* *Defense:* `safety: 16`, `doc: 143`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.86
  * `Choke Point (Betweenness):` 0.000201 | `Ripple Effect (Closeness):` 0.014134
  * `Imports (Out-Degree: 10):` Alt, Apply, Bifunctor, Chain, Compactable, Contravariant, Either, Extend...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/ReadonlyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 933.7 | **LOC:** 2665 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.5773%), Tech Debt (14.2405%)
**Top Internal Functions/Classes:**
  * `concat` **(Many-Argument Workhorses)** (Impact: 16.2)
  * `union` **(Generic / Templated Code)** (Impact: 11.3)
  * `elem` **(Generic / Templated Code)** (Impact: 9.9)
  * `unfold` **(Generic / Templated Code)** (Impact: 8.9)
    * *Intent:* /** * @since 2.6.6 */
  * `intercalate` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* /** * Places an element in between members of a `ReadonlyArray`, then folds the results using the pr...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 777`, `args: 382`, `func_start: 162`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `planned_debt: 15`
* *Architecture:* `api: 202`, `import: 39`
* *Defense:* `safety: 4`, `doc: 170`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.722
  * `Choke Point (Betweenness):` 0.003837 | `Ripple Effect (Closeness):` 0.155477
  * `Imports (Out-Degree: 13):` Alt, Alternative, Applicative, Apply, Chain, ChainRec, Compactable, Either...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `src/Array.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 794.74 | **LOC:** 3021 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.0511%), Tech Debt (10.4927%)
**Top Internal Functions/Classes:**
  * `concat` **(Many-Argument Workhorses)** (Impact: 21.7)
  * `separate` **(Generic / Templated Code)** (Impact: 15.7)
    * *Intent:* * one containing all the left values and one containing all the right values. * * @example * import ...
  * `union` **(Generic / Templated Code)** (Impact: 11.4)
  * `unfold` **(Generic / Templated Code)** (Impact: 10.1)
    * *Intent:* * @example * import { unfold } from 'fp-ts/Array' * import { option } from 'fp-ts' * * const f = (n:...
  * `some` **(Generic / Templated Code)** (Impact: 10.1)
    * *Intent:* /** * `some` tells if the provided predicate holds true at least for one element in the `Array`. * *...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 715`, `args: 351`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`, `planned_debt: 6`
* *Architecture:* `api: 194`, `import: 38`
* *Defense:* `safety: 3`, `doc: 167`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.715
  * `Choke Point (Betweenness):` 0.000648 | `Ripple Effect (Closeness):` 0.031802
  * `Imports (Out-Degree: 13):` Alt, Alternative, Applicative, Apply, Chain, ChainRec, Compactable, Either...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/ReadonlyRecord.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 754.74 | **LOC:** 2297 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (13.879%), Tech Debt (16.8318%)
**Top Internal Functions/Classes:**
  * `union` **(Compute Cores)** (Impact: 13.6)
    * *Intent:* * It uses the `concat` function of the provided `Magma` to * combine the elements with the same key....
  * `concat` **(Many-Argument Workhorses)** (Impact: 13.6)
  * `isSubrecord` **(Compute Cores)** (Impact: 11.7)
  * `difference` **(Compute Cores)** (Impact: 11.1)
    * *Intent:* * Difference between two `ReadonlyRecord`s. * Takes two `ReadonlyRecord`s and produces a `ReadonlyRe...
  * `partitionMapWithIndex` **(Generic / Templated Code)** (Impact: 10.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 780`, `args: 382`, `func_start: 153`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `planned_debt: 3`, `duplicate_logic: 2`
* *Architecture:* `api: 166`, `import: 27`
* *Defense:* `safety: 3`, `doc: 107`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.137
  * `Choke Point (Betweenness):` 0.00014 | `Ripple Effect (Closeness):` 0.017668
  * `Imports (Out-Degree: 5):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ReadonlyMap.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 534.98 | **LOC:** 1217 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.9098%), Tech Debt (10.2094%)
**Top Internal Functions/Classes:**
  * `union` **(Generic / Templated Code)** (Impact: 15.9)
    * *Intent:* // ------------------------------------------------------------------------------------- // utils //...
  * `isSubmap` **(Generic / Templated Code)** (Impact: 15.6)
  * `difference` **(Generic / Templated Code)** (Impact: 13.1)
    * *Intent:* /** * @since 2.11.0 */
  * `concat` **(Compute Cores)** (Impact: 12.0)
  * `getMonoid` **(Generic / Templated Code)** (Impact: 11.7)
    * *Intent:* /** * Gets `Monoid` instance for Maps given `Semigroup` instance for their values * * @category inst...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 480`, `args: 226`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `planned_debt: 5`
* *Architecture:* `api: 83`, `import: 28`
* *Defense:* `safety: 2`, `doc: 66`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.808
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.007067
  * `Imports (Out-Degree: 5):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/ReadonlyNonEmptyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 533.7 | **LOC:** 1498 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.2191%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `concat` **(Many-Argument Workhorses)** (Impact: 14.4)
  * `group` **(Generic / Templated Code)** (Impact: 9.0)
  * `uniq` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /** * Remove duplicates from a `ReadonlyNonEmptyArray`, keeping the first occurrence of an element. ...
  * `rotate` **(Generic / Templated Code)** (Impact: 8.4)
    * *Intent:* /** * Rotate a `ReadonlyNonEmptyArray` by `n` steps. * * @example * import { rotate } from 'fp-ts/Re...
  * `insertAt` **(Generic / Templated Code)** (Impact: 8.0)
    * *Intent:* /** * Use [`insertAt`](./ReadonlyArray.ts.html#insertat) instead. * * @category zone of death * @sin...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 444`, `args: 205`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `api: 128`, `import: 27`
* *Defense:* `safety: 1`, `doc: 116`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.268
  * `Choke Point (Betweenness):` 0.001851 | `Ripple Effect (Closeness):` 0.106007
  * `Imports (Out-Degree: 9):` Alt, Applicative, Apply, Chain, Comonad, Endomorphism, Eq, Extend...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/NonEmptyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 493.98 | **LOC:** 1408 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.6064%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `concat` **(Many-Argument Workhorses)** (Impact: 13.5)
  * `group` **(Generic / Templated Code)** (Impact: 9.0)
  * `rotate` **(Generic / Templated Code)** (Impact: 8.8)
    * *Intent:* /** * Rotate a `NonEmptyArray` by `n` steps. * * @example * import { rotate } from 'fp-ts/NonEmptyAr...
  * `uniq` **(Compute Cores)** (Impact: 8.4)
    * *Intent:* /** * Remove duplicates from a `NonEmptyArray`, keeping the first occurrence of an element. * * @exa...
  * `groupBy` **(Generic / Templated Code)** (Impact: 6.6)
    * *Intent:* /** * Splits an array into sub-non-empty-arrays stored in an object, based on the result of calling ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 433`, `args: 204`, `func_start: 84`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `api: 127`, `import: 26`
* *Defense:* `safety: 1`, `doc: 116`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.00024 | `Ripple Effect (Closeness):` 0.010601
  * `Imports (Out-Degree: 9):` Alt, Applicative, Apply, Chain, Comonad, Endomorphism, Eq, Extend...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `test/ReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 429.16 | **LOC:** 841 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.7731%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` **(Interface Declarations)** (Impact: 3.3)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 345
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 449`, `args: 225`, `func_start: 134`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `concurrency: 285`, `import: 19`
* *Defense:* `safety: 1`, `test: 116`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` Apply, Either, IO, IOEither, Option, Reader, ReaderEither, ReaderIO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/TaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 409.12 | **LOC:** 920 | **CtrlFlow:** 5.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.8027%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `api3` **(Callbacks & Closures)** (Impact: 3.9)
  * `api1` **(Callbacks & Closures)** (Impact: 3.7)
  * `api2` **(Callbacks & Closures)** (Impact: 3.7)
  * `api` **(Callbacks & Closures)** (Impact: 3.6)
  * `f` **(Interface Declarations)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Amplified Cascading Flux:* 1 instances
* *Concurrency (weighted view):* 330
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 438`, `args: 218`, `func_start: 113`
* *Risk/State:* `state_mutation: 12`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `concurrency: 270`, `import: 17`
* *Defense:* `safety: 1`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Apply, Either, IO, IOEither, Monoid, Option, ReadonlyArray, ReadonlyNonEmptyArray...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Either.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 404.96 | **LOC:** 1854 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.747%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getOrElseW` **(Generic / Templated Code)** (Impact: 16.6)
    * *Intent:* /** * Less strict version of [`getOrElse`](#getorelse). * * The `W` suffix (short for **W**idening) ...
  * `extend` **(Generic / Templated Code)** (Impact: 10.2)
    * *Intent:* /** * @since 2.0.0 */
  * `exists` **(Generic / Templated Code)** (Impact: 9.9)
    * *Intent:* /** * Returns `false` if `Left` or returns the result of the application of the given predicate to t...
  * `equals` **(Compute Cores)** (Impact: 9.8)
    * *Intent:* /** * @category instances * @since 2.0.0 */
  * `ap` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 486`, `args: 198`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2`
* *Architecture:* `api: 117`, `import: 32`
* *Defense:* `safety: 6`, `doc: 119`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.754
  * `Choke Point (Betweenness):` 0.003675 | `Ripple Effect (Closeness):` 0.197941
  * `Imports (Out-Degree: 11):` Alt, Applicative, Apply, Bifunctor, Chain, ChainRec, Compactable, Eq...
  * `Imported By (In-Degree: 56):` (Excluded from Brief to save tokens)

### `src/Record.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 404.74 | **LOC:** 1805 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.9235%), Tech Debt (9.6085%)
**Top Internal Functions/Classes:**
  * `_traverseWithIndex` **(Generic / Templated Code)** (Impact: 11.1)
  * `concat` **(Many-Argument Workhorses)** (Impact: 10.3)
    * *Intent:* * * @example * import { getDifferenceMagma, difference } from "fp-ts/Record" * import { Magma } from...
  * `pop` **(Generic / Templated Code)** (Impact: 8.3)
  * `union` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* * It uses the `concat` function of the provided `Magma` to * combine the elements with the same key....
  * `difference` **(Generic / Templated Code)** (Impact: 5.8)
    * *Intent:* * Difference between two `Record`s. * Takes two `Record`s and produces a `Record` composed by the * ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 575`, `args: 273`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `planned_debt: 3`
* *Architecture:* `api: 131`, `import: 29`
* *Defense:* `safety: 2`, `doc: 86`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.701
  * `Choke Point (Betweenness):` 4.4e-05 | `Ripple Effect (Closeness):` 0.007067
  * `Imports (Out-Degree: 5):` Applicative, Array, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/function.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 380.68 | **LOC:** 806 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.9767%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pipe` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `flow` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `concat` **(Generic / Templated Code)** (Impact: 7.5)
    * *Intent:* /** * Use `Endomorphism` module instead. * * @category zone of death * @since 2.10.0 * @deprecated *...
  * `pipe` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `pipe` **(Many-Argument Workhorses)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 479`, `args: 117`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 3`
* *Architecture:* `api: 70`, `import: 6`
* *Defense:* `safety: 1`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 30.996
  * `Choke Point (Betweenness):` 0.001253 | `Ripple Effect (Closeness):` 0.35689
  * `Imports (Out-Degree: 1):` BooleanAlgebra, Monoid, Ring, Semigroup, Semiring, Predicate, boolean, function
  * `Imported By (In-Degree: 101):` (Excluded from Brief to save tokens)

### `src/Map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 375.56 | **LOC:** 925 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.9891%), Tech Debt (11.7112%)
**Top Internal Functions/Classes:**
  * `concat` **(Compute Cores)** (Impact: 11.9)
  * `getMonoid` **(Generic / Templated Code)** (Impact: 11.7)
    * *Intent:* /** * Gets `Monoid` instance for Maps given `Semigroup` instance for their values * * @category inst...
  * `lookupWithKey` **(Generic / Templated Code)** (Impact: 11.4)
  * `separate` **(Generic / Templated Code)** (Impact: 7.6)
    * *Intent:* /** * @category filtering * @since 2.0.0 */
  * `upsertAt` **(Callbacks & Closures)** (Impact: 7.0)
    * *Intent:* /** * Insert or replace a key/value pair in a `Map`. * * @since 2.0.0 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 399`, `args: 193`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 5`
* *Architecture:* `api: 74`, `import: 27`
* *Defense:* `safety: 2`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.814
  * `Choke Point (Betweenness):` 7.3e-05 | `Ripple Effect (Closeness):` 0.007067
  * `Imports (Out-Degree: 5):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Apply.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 372.16 | **LOC:** 714 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.0773%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getRecordConstructor` **(Compute Cores)** (Impact: 14.6)
  * `curried` **(Callbacks & Closures)** (Impact: 6.5)
  * `apS` **(Generic / Templated Code)** (Impact: 4.0)
  * `getTupleConstructor` **(Interface Declarations)** (Impact: 3.9)
  * `sequenceT` **(Generic / Templated Code)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 598`, `args: 317`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 9`
* *Architecture:* `api: 100`, `import: 5`
* *Defense:* `doc: 15`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.318
  * `Choke Point (Betweenness):` 0.000159 | `Ripple Effect (Closeness):` 0.15705
  * `Imports (Out-Degree: 2):` Functor, HKT, Semigroup, function, internal, Apply, Either, Option...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/ReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 359.16 | **LOC:** 2292 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.5518%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `fromReaderIOK` **(Generic / Templated Code)** (Impact: 30.2)
    * *Intent:* /** * @category lifting * @since 2.13.0 */
  * `alt` **(Generic / Templated Code)** (Impact: 29.3)
  * `fromReaderEither` **(Generic / Templated Code)** (Impact: 12.7)
    * *Intent:* /** * @category conversions * @since 2.0.0 */
  * `_alt` **(Generic / Templated Code)** (Impact: 11.2)
    * *Intent:* /* istanbul ignore next */
  * `traverseSeqArray` **(Generic / Templated Code)** (Impact: 9.5)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverse(ApplicativeSeq)`. * * @category traversing * @since 2.9....
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 784`, `args: 320`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`
* *Architecture:* `api: 188`, `concurrency: 1`, `import: 35`
* *Defense:* `doc: 195`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.478
  * `Choke Point (Betweenness):` 0.000617 | `Ripple Effect (Closeness):` 0.035336
  * `Imports (Out-Degree: 13):` Alt, Applicative, Apply, Bifunctor, Chain, Compactable, Either, EitherT...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/TaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 345.44 | **LOC:** 1882 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.707%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `partitionMap` **(Generic / Templated Code)** (Impact: 37.0)
  * `_alt` **(Generic / Templated Code)** (Impact: 14.8)
    * *Intent:* /* istanbul ignore next */
  * `bracketW` **(Generic / Templated Code)** (Impact: 10.4)
    * *Intent:* /** * Less strict version of [`bracket`](#bracket). * * The `W` suffix (short for **W**idening) mean...
  * `traverseSeqArray` **(Generic / Templated Code)** (Impact: 9.0)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverse(ApplicativeSeq)`. * * @category traversing * @since 2.9....
  * `tryCatchK` **(Generic / Templated Code)** (Impact: 6.8)
    * *Intent:* /** * Converts a function returning a `Promise` to one returning a `TaskEither`. * * @category inter...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 637`, `args: 256`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1`
* *Architecture:* `api: 153`, `concurrency: 6`, `import: 32`
* *Defense:* `safety: 2`, `doc: 152`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.639
  * `Choke Point (Betweenness):` 0.001389 | `Ripple Effect (Closeness):` 0.067138
  * `Imports (Out-Degree: 12):` Alt, Applicative, Apply, Bifunctor, Chain, Compactable, Either, EitherT...
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `src/Option.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 340.68 | **LOC:** 1527 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8726%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `compare` **(Compute Cores)** (Impact: 10.1)
  * `getOrElseW` **(Generic / Templated Code)** (Impact: 9.7)
    * *Intent:* /** * Less strict version of [`getOrElse`](#getorelse). * * The `W` suffix (short for **W**idening) ...
  * `elem` **(Generic / Templated Code)** (Impact: 9.2)
  * `ap` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* /** * @since 2.0.0 */
  * `reduceRight` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* /** * @category folding * @since 2.0.0 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 382`, `args: 169`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 112`, `import: 31`
* *Defense:* `safety: 5`, `doc: 106`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.631
  * `Choke Point (Betweenness):` 0.002092 | `Ripple Effect (Closeness):` 0.151943
  * `Imports (Out-Degree: 10):` Alt, Alternative, Applicative, Apply, Chain, Compactable, Either, Eq...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/These.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 307.28 | **LOC:** 807 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.9748%), Tech Debt (10.4162%)
**Top Internal Functions/Classes:**
  * `concat` **(Compute Cores)** (Impact: 16.9)
  * `ap` **(Compute Cores)** (Impact: 16.8)
  * `getSemigroup` **(Generic / Templated Code)** (Impact: 16.7)
    * *Intent:* /** * @category instances * @since 2.0.0 */
  * `traverseReadonlyNonEmptyArrayWithIndex` **(Generic / Templated Code)** (Impact: 13.0)
    * *Intent:* // ------------------------------------------------------------------------------------- // array ut...
  * `getEq` **(Generic / Templated Code)** (Impact: 12.6)
    * *Intent:* /** * @category instances * @since 2.0.0 */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 246`, `args: 104`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 4`, `planned_debt: 2`
* *Architecture:* `api: 57`, `import: 25`
* *Defense:* `safety: 3`, `doc: 58`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.858
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.010601
  * `Imports (Out-Degree: 9):` Applicative, Apply, Bifunctor, Chain, Either, Eq, Foldable, FromEither...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/ReadonlySet.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 290.0 | **LOC:** 605 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.4006%), Tech Debt (14.5957%)
**Top Internal Functions/Classes:**
  * `partitionMap` **(Generic / Templated Code)** (Impact: 14.4)
    * *Intent:* /** * @since 2.5.0 */
  * `separate` **(Generic / Templated Code)** (Impact: 11.9)
    * *Intent:* /** * @since 2.5.0 */
  * `union` **(Generic / Templated Code)** (Impact: 11.5)
  * `intersection` **(Generic / Templated Code)** (Impact: 11.2)
  * `elem` **(Generic / Templated Code)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 245`, `args: 139`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `planned_debt: 5`
* *Architecture:* `api: 52`, `import: 12`
* *Defense:* `doc: 39`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.918
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007067
  * `Imports (Out-Degree: 0):` Either, Eq, Magma, Monoid, Option, Ord, Predicate, Refinement...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/StateReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 281.98 | **LOC:** 1661 | **CtrlFlow:** 0.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.9208%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `altW` **(Generic / Templated Code)** (Impact: 45.7)
    * *Intent:* /** * Less strict version of [`alt`](#alt). * * The `W` suffix (short for **W**idening) means that t...
  * `mapLeft` **(Generic / Templated Code)** (Impact: 14.0)
    * *Intent:* /** * Map a function over the third type argument of a bifunctor. * * @category error handling * @si...
  * `traverseArray` **(Generic / Templated Code)** (Impact: 7.4)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverse(Applicative)`. * * @category traversing * @since 2.9.0 *...
  * `traverseReadonlyNonEmptyArrayWithIndex` **(Generic / Templated Code)** (Impact: 5.9)
    * *Intent:* // ------------------------------------------------------------------------------------- // array ut...
  * `traverseReadonlyArrayWithIndex` **(Generic / Templated Code)** (Impact: 4.0)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverseWithIndex(Applicative)`. * * @category traversing * @sinc...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *Api Near Db Sink:* 1 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 586`, `args: 254`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 2`
* *Architecture:* `api: 136`, `concurrency: 2`, `import: 34`
* *Defense:* `doc: 143`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.529
  * `Choke Point (Betweenness):` 0.000392 | `Ripple Effect (Closeness):` 0.017668
  * `Imports (Out-Degree: 15):` Alt, Applicative, Apply, Bifunctor, Chain, Either, Endomorphism, FromEither...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `test/StateReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 268.32 | **LOC:** 652 | **CtrlFlow:** 1.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.5921%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `f` **(Interface Declarations)** (Impact: 3.1)
  * `left` **(Callbacks & Closures)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Concurrency (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 304`, `args: 149`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 172`, `import: 18`
* *Defense:* `safety: 1`, `test: 75`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Array, Either, IO, IOEither, Option, Reader, ReaderEither, ReaderTaskEither...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `test/TaskOption.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 255.72 | **LOC:** 429 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.9373%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `f` **(Interface Declarations)** (Impact: 3.3)
  * `f` **(Interface Declarations)** (Impact: 3.3)
  * `f` **(Interface Declarations)** (Impact: 3.3)
  * `f` **(Interface Declarations)** (Impact: 3.3)
  * `none` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 231`, `args: 110`, `func_start: 60`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 149`, `import: 10`
* *Defense:* `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Either, IO, Option, ReadonlyArray, ReadonlyNonEmptyArray, Task, TaskEither, TaskOption...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/IOEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 251.98 | **LOC:** 1395 | **CtrlFlow:** 1.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.0761%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `partitionMap` **(Generic / Templated Code)** (Impact: 27.4)
  * `bracketW` **(Generic / Templated Code)** (Impact: 10.4)
    * *Intent:* /** * Less strict version of [`bracket`](#bracket). * * The `W` suffix (short for **W**idening) mean...
  * `_alt` **(Generic / Templated Code)** (Impact: 10.2)
    * *Intent:* /* istanbul ignore next */
  * `traverseSeqArray` **(Generic / Templated Code)** (Impact: 8.3)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverse(ApplicativeSeq)`. * * @category traversing * @since 2.9....
  * `traverseReadonlyNonEmptyArrayWithIndexSeq` **(Generic / Templated Code)** (Impact: 7.0)
    * *Intent:* /** * Equivalent to `ReadonlyNonEmptyArray#traverseWithIndex(ApplicativeSeq)`. * * @category travers...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 472`, `args: 187`, `func_start: 27`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 2`
* *Architecture:* `api: 120`, `import: 26`
* *Defense:* `doc: 125`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.812
  * `Choke Point (Betweenness):` 0.000245 | `Ripple Effect (Closeness):` 0.031802
  * `Imports (Out-Degree: 10):` Alt, Applicative, Apply, Bifunctor, Chain, Compactable, Either, EitherT...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `scripts/linter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 232.34 | **LOC:** 653 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.9109%), Tech Debt (9.2669%)
**Top Internal Functions/Classes:**
  * `parseType` **(Compute Cores)** (Impact: 39.8)
  * `lintType` **(Compute Cores)** (Impact: 28.3)
  * `getTypeArguments` **(Callbacks & Closures)** (Impact: 27.4)
  * `parseVariableDeclaration` **(Compute Cores)** (Impact: 19.2)
  * `parseInterface` **(Callbacks & Closures)** (Impact: 13.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 281`, `args: 53`, `func_start: 20`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 22`, `api: 43`, `import: 8`
* *Defense:* `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.478
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Monoid, Option, ReadonlyArray, function, string, glob, path, ts-morph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Set.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 226.36 | **LOC:** 495 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.3508%), Tech Debt (15.2032%)
**Top Internal Functions/Classes:**
  * `partitionMap` **(Generic / Templated Code)** (Impact: 14.4)
    * *Intent:* /** * @since 2.0.0 */
  * `separate` **(Generic / Templated Code)** (Impact: 11.8)
    * *Intent:* /** * @since 2.0.0 */
  * `union` **(Generic / Templated Code)** (Impact: 11.4)
  * `intersection` **(Generic / Templated Code)** (Impact: 11.1)
  * `partition` **(Generic / Templated Code)** (Impact: 6.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 15 instances
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 205`, `args: 115`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 17`, `planned_debt: 4`
* *Architecture:* `api: 43`, `import: 13`
* *Defense:* `doc: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.918
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007067
  * `Imports (Out-Degree: 0):` Either, Eq, Magma, Monoid, Option, Ord, Predicate, ReadonlySet...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/ReadonlyArray.ts` -> **Severity: 0.361** (Bridge: 0.0038 * Flux: 94.1685%)
- `src/ReadonlyNonEmptyArray.ts` -> **Severity: 0.179** (Bridge: 0.0019 * Flux: 96.7557%)
- `src/Array.ts` -> **Severity: 0.058** (Bridge: 0.0006 * Flux: 88.8319%)
- `src/IO.ts` -> **Severity: 0.033** (Bridge: 0.0008 * Flux: 41.3693%)
- `src/Either.ts` -> **Severity: 0.032** (Bridge: 0.0037 * Flux: 8.8329%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/HKT.ts` -> **Severity: 44.403** (Embedded: 0.4587 * Error Risk: 96.806%)
- `src/function.ts` -> **Severity: 22.91** (Embedded: 0.3569 * Error Risk: 64.1928%)
- `src/Chain.ts` -> **Severity: 17.703** (Embedded: 0.3402 * Error Risk: 52.029%)
- `test/util.ts` -> **Severity: 16.327** (Embedded: 0.2792 * Error Risk: 58.4884%)
- `src/internal.ts` -> **Severity: 14.486** (Embedded: 0.3277 * Error Risk: 44.2043%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `test/util.ts` -> **Severity: 2187.8** (Blast Radius: 21.878 * Doc Risk: 100.0%)
- `src/Chain.ts` -> **Severity: 2161.32** (Blast Radius: 36.022 * Doc Risk: 60.0%)
- `src/function.ts` -> **Severity: 1525.198** (Blast Radius: 30.996 * Doc Risk: 49.2063%)
- `src/Apply.ts` -> **Severity: 655.571** (Blast Radius: 7.318 * Doc Risk: 89.5833%)
- `src/Alt.ts` -> **Severity: 596.25** (Blast Radius: 7.95 * Doc Risk: 75.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
