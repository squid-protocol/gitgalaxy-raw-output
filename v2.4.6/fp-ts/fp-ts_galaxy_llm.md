# ARCHITECTURAL_BRIEF: fp-ts
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/fp-ts` |
| **Timestamp** | `2026-08-03T19:54:22.133569+00:00` |
| **Scan Duration** | `1.58s` |
| **Git Branch** | `master` |
| **Git Commit** | `09045f5819af260b5a6c4aeabdf2fbc8d9b9e335` |
| **Git Remote** | `https://github.com/gcanti/fp-ts.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 190 malicious artifacts.

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
| Total Artifacts | 431 |
| Analyzed Artifacts (Scanned) | 200 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 231 |
| Total LOC | 25529 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 46.4% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3326 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.3283 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 3.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3296 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 10 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 190 | 25436 | 95.0% |
| JSON | 5 | 67 | 2.5% |
| MARKDOWN | 3 | 0 | 1.5% |
| HTML | 1 | 26 | 0.5% |
| PLAINTEXT | 1 | 0 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.512`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_16 | 110 | 55.0% |
| file_cluster_8 | 44 | 22.0% |
| file_cluster_13 | 34 | 17.0% |
| file_cluster_17 | 5 | 2.5% |
| file_cluster_2 | 2 | 1.0% |
| file_cluster_4 | 1 | 0.5% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 4 | 2.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 231*

**Composition by Extension & Reason:**
- `.md`: 136x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.ts`: 81x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11222 LOC)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 97.5 | 9.9 | 4.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.4 | 22.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 22.0 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.9 | 2.3 | 2.3 |
| API Exposure | 0.0 | 15.4 | 7.0 | 8.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 29.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 41.3 | 20.7 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 5.6 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 5.7 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `scripts/linter.ts` (Hits: 22)
- `scripts/FileSystem.ts` (Hits: 18)
- `scripts/build.ts` (Hits: 13)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **HKT.ts** (`src/HKT.ts`) — 70 inbound connections
2. **Chain.ts** (`src/Chain.ts`) — 43 inbound connections
3. **Monad.ts** (`src/Monad.ts`) — 39 inbound connections
4. **internal.ts** (`src/internal.ts`) — 36 inbound connections
5. **Pointed.ts** (`src/Pointed.ts`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/index.ts`) — 121 outbound dependencies
2. **ReadonlyArray.ts** (`src/ReadonlyArray.ts`) — 48 outbound dependencies
3. **Array.ts** (`src/Array.ts`) — 47 outbound dependencies
4. **Record.ts** (`src/Record.ts`) — 41 outbound dependencies
5. **ReaderTaskEither.ts** (`src/ReaderTaskEither.ts`) — 40 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `parseType` (@ `scripts/linter.ts`) -> Impact: **162.6** | LOC: 89
- `getTypeArguments` (@ `scripts/linter.ts`) -> Impact: **155.4** | LOC: 66
- `pipe` (@ `src/function.ts`) -> Impact: **101.6** | LOC: 39
- `flow` (@ `src/function.ts`) -> Impact: **92.6** | LOC: 49
  * *Intent:* /** * A thunk that returns always `null`. *
- `lintType` (@ `scripts/linter.ts`) -> Impact: **80.2** | LOC: 45
- `main` (@ `examples/fp-ts-to-the-max-II.ts`) -> Impact: **64.2** | LOC: 60
- `parseVariableDeclaration` (@ `scripts/linter.ts`) -> Impact: **55.8** | LOC: 42
- `parseInterface` (@ `scripts/linter.ts`) -> Impact: **55.3** | LOC: 33
- `union` (@ `src/ReadonlySet.ts`) -> Impact: **52.6** | LOC: 24
- `intersection` (@ `src/ReadonlySet.ts`) -> Impact: **52.5** | LOC: 21

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `parseArrowFunction` (@ `scripts/linter.ts`) -> **O(2^N) [Recursive]**
- `gameLoop` (@ `examples/fp-ts-to-the-max-I.ts`) -> **O(2^N) [Recursive]**
- `getTypeArguments` (@ `scripts/linter.ts`) -> **O(2^N) [Recursive]**
- `chain` (@ `src/TheseT.ts`) -> **O(2^N) [Recursive]**
- `shouldContinue` (@ `examples/fp-ts-to-the-max-I.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* // // game //
- `lintType` (@ `scripts/linter.ts`) -> **O(2^N) [Recursive]**
- `parseInterface` (@ `scripts/linter.ts`) -> **O(2^N) [Recursive]**
- `exec` (@ `scripts/release.ts`) -> **O(2^N) [Recursive]**
- `lookupWithKey` (@ `src/Map.ts`) -> **O(2^N) [Recursive]**
- `predicateWithIndex` (@ `src/Map.ts`) -> **O(2^N) [Recursive]**
  * *Intent:* /**

### Highest Data Gravity (Database Complexity)
- `lintType` (@ `scripts/linter.ts`) -> DB Complexity: **24**
- `check` (@ `scripts/linter.ts`) -> DB Complexity: **9**
- `pipe` (@ `scripts/build.ts`) -> DB Complexity: **8**
- `readFile` (@ `scripts/FileSystem.ts`) -> DB Complexity: **6**
- `makeSingleModule` (@ `scripts/build.ts`) -> DB Complexity: **6**
- `lintSignature` (@ `scripts/linter.ts`) -> DB Complexity: **6**
- `lint` (@ `scripts/linter.ts`) -> DB Complexity: **6**
- `exec` (@ `scripts/release.ts`) -> DB Complexity: **6**
- `constructor` (@ `src/IORef.ts`) -> DB Complexity: **6**
- `group` (@ `src/NonEmptyArray.ts`) -> DB Complexity: **6**
  * *Intent:* /** * Rotate a `NonEmptyArray` by `n` steps.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 123 | 1194.39 | 4.23% | 24.98% |
| `dtslint` | 44 | 129.45 | 4.24% | 21.43% |
| `__monolith__` | 9 | 127.92 | 4.59% | 11.09% |
| `scripts` | 6 | 75.78 | 7.31% | 15.63% |
| `examples` | 3 | 32.09 | 10.04% | 0.0% |
| `perf/Task` | 3 | 7.04 | 52.49% | 0.0% |
| `perf/function` | 2 | 5.31 | 95.34% | 0.0% |
| `perf/ReaderTask` | 1 | 2.45 | 66.65% | 0.0% |
| `perf/ReaderTaskEither` | 1 | 2.45 | 66.65% | 0.0% |
| `perf/TaskEither` | 1 | 2.45 | 66.65% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `dtslint/Apply.ts` -> **100.0%** Exposure
- `dtslint/NonEmptyArray.ts` -> **100.0%** Exposure
- `dtslint/ReaderEither.ts` -> **100.0%** Exposure
- `dtslint/ReaderTaskEither.ts` -> **100.0%** Exposure
- `dtslint/ReadonlyNonEmptyArray.ts` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/IORef.ts` -> **99.9998%** Exposure
- `perf/function/pipe.ts` -> **99.9893%** Exposure
- `perf/ReadonlyNonEmptyArray.ts/reverse.ts` -> **99.9835%** Exposure
- `perf/function/flow.ts` -> **99.9294%** Exposure
- `perf/Either/sequenceArray.ts` -> **83.2018%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/pipeable.ts` -> **0** Orphaned Functions | **50** Duplicates
- `dtslint/ReaderTaskEither.ts` -> **0** Orphaned Functions | **24** Duplicates
- `src/Apply.ts` -> **0** Orphaned Functions | **24** Duplicates
- `src/Filterable.ts` -> **0** Orphaned Functions | **18** Duplicates
- `src/Functor.ts` -> **0** Orphaned Functions | **16** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`scripts/linter.ts`** -> AI Confidence: **99.18%**
2. **`src/These.ts`** -> AI Confidence: **99.18%**
3. **`dtslint/ReadonlyRecord.ts`** -> AI Confidence: **99.09%**
4. **`dtslint/Record.ts`** -> AI Confidence: **99.09%**
5. **`dtslint/constrained.ts`** -> AI Confidence: **99.09%**
6. **`dtslint/pipeable.ts`** -> AI Confidence: **99.09%**
7. **`src/Const.ts`** -> AI Confidence: **99.09%**
8. **`src/EitherT.ts`** -> AI Confidence: **99.09%**
9. **`src/Foldable.ts`** -> AI Confidence: **99.09%**
10. **`src/IO.ts`** -> AI Confidence: **99.09%**
11. **`src/IOEither.ts`** -> AI Confidence: **99.09%**
12. **`src/IOOption.ts`** -> AI Confidence: **99.09%**
13. **`src/Identity.ts`** -> AI Confidence: **99.09%**
14. **`src/Monoid.ts`** -> AI Confidence: **99.09%**
15. **`src/Option.ts`** -> AI Confidence: **99.09%**
16. **`src/OptionT.ts`** -> AI Confidence: **99.09%**
17. **`src/Reader.ts`** -> AI Confidence: **99.09%**
18. **`src/ReaderEither.ts`** -> AI Confidence: **99.09%**
19. **`src/ReaderIO.ts`** -> AI Confidence: **99.09%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `scripts/linter.ts` -> **100.0%** Exposure
- `src/Apply.ts` -> **100.0%** Exposure
- `src/EitherT.ts` -> **100.0%** Exposure
- `src/ReadonlyRecord.ts` -> **100.0%** Exposure
- `src/ReadonlySet.ts` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/Task.ts` -> **100.0%** Exposure
### Algorithmic DoS Exposure
- `src/Set.ts` -> **100.0%** Exposure
- `src/ReadonlySet.ts` -> **99.9999%** Exposure
- `scripts/linter.ts` -> **99.9877%** Exposure
- `src/Map.ts` -> **99.9583%** Exposure
- `src/NonEmptyArray.ts` -> **97.906%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `217` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/ReadonlySet.ts` (TYPESCRIPT) -> Cumulative Risk: **752.67**
- **Archetype:** `file_cluster_16` (Distance: 12.141 IQR)
- **Magnitude:** 50.25 | **LOC:** 605 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.9999%), Tech Debt (99.9797%)
- **Heaviest Functions:** `union` (Impact: 52.6), `intersection` (Impact: 52.5), `partitionMap` (Impact: 37.5)

### 2. `src/Set.ts` (TYPESCRIPT) -> Cumulative Risk: **737.61**
- **Archetype:** `file_cluster_16` (Distance: 12.284 IQR)
- **Magnitude:** 37.77 | **LOC:** 495 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Tech Debt (99.8264%)
- **Heaviest Functions:** `union` (Impact: 43.1), `intersection` (Impact: 43.0), `partitionMap` (Impact: 37.5)

### 3. `perf/ReadonlyNonEmptyArray.ts/reverse.ts` (TYPESCRIPT) -> Cumulative Risk: **624.82**
- **Archetype:** `file_cluster_4` (Distance: 12.603 IQR)
- **Magnitude:** 1.84 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9895%), State Flux (99.9835%)
- **Heaviest Functions:** `reverse2` (Impact: 2.5), `reverse2` (Impact: 2.5)

### 4. `src/Apply.ts` (TYPESCRIPT) -> Cumulative Risk: **596.68**
- **Archetype:** `file_cluster_16` (Distance: 11.027 IQR)
- **Magnitude:** 30.39 | **LOC:** 714 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Tech Debt (99.974%), Documentation (98.8079%)
- **Heaviest Functions:** `getRecordConstructor` (Impact: 37.9), `curried` (Impact: 12.5), `apS` (Impact: 6.0)

### 5. `src/TaskThese.ts` (TYPESCRIPT) -> Cumulative Risk: **591.84**
- **Archetype:** `file_cluster_16` (Distance: 11.886 IQR)
- **Magnitude:** 12.99 | **LOC:** 600 | **CtrlFlow:** 2.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Algorithmic Dos (93.3789%), Verification (80.0%)
- **Heaviest Functions:** `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 26.1), `traverseReadonlyArrayWithIndex` (Impact: 4.3), `traverseReadonlyArrayWithIndexSeq` (Impact: 4.3)

### 6. `src/Task.ts` (TYPESCRIPT) -> Cumulative Risk: **578.77**
- **Archetype:** `file_cluster_16` (Distance: 11.103 IQR)
- **Magnitude:** 12.77 | **LOC:** 720 | **CtrlFlow:** 1.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Logic Bomb (100.0%), Injection Surface (100.0%)
- **Heaviest Functions:** `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 4.1), `never` (Impact: 3.9), `f` (Impact: 3.7)

### 7. `src/Map.ts` (TYPESCRIPT) -> Cumulative Risk: **553.35**
- **Archetype:** `file_cluster_16` (Distance: 12.075 IQR)
- **Magnitude:** 45.57 | **LOC:** 925 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9583%), Verification (80.0%), Safety Score (72.7396%)
- **Heaviest Functions:** `lookupWithKey` (Impact: 45.0), `predicateWithIndex` (Impact: 21.7), `getMonoid` (Impact: 19.4)

### 8. `src/TaskEither.ts` (TYPESCRIPT) -> Cumulative Risk: **529.05**
- **Archetype:** `file_cluster_16` (Distance: 12.014 IQR)
- **Magnitude:** 26.07 | **LOC:** 1882 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Logic Bomb (100.0%), Verification (80.0%), Tech Debt (71.0701%)
- **Heaviest Functions:** `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 13.8), `taskify` (Impact: 5.7), `async` (Impact: 5.5)

### 9. `perf/function/flow.ts` (TYPESCRIPT) -> Cumulative Risk: **522.06**
- **Archetype:** `file_cluster_17` (Distance: 12.836 IQR)
- **Magnitude:** 2.69 | **LOC:** 36 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9294%), Concurrency (99.8982%), Cognitive Load (97.0193%)
- **Heaviest Functions:** `flow2` (Impact: 4.5), `flow` (Impact: 3.5), `g` (Impact: 2.3)

### 10. `src/ReadonlyArray.ts` (TYPESCRIPT) -> Cumulative Risk: **509.84**
- **Archetype:** `file_cluster_16` (Distance: 12.795 IQR)
- **Magnitude:** 88.06 | **LOC:** 2665 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (95.0478%), Algorithmic Dos (89.3214%), Verification (80.0%)
- **Heaviest Functions:** `elem` (Impact: 36.8), `union` (Impact: 34.9), `intersection` (Impact: 20.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/ReadonlyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.795 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.475 IQR)
- **Top Global Matches:** file_cluster_16: 12.795, file_cluster_13: 13.166, file_cluster_11: 13.258
- **Magnitude:** 88.06 | **LOC:** 2665 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.9463%), Tech Debt (95.0478%)
**Top Internal Functions/Classes:**
  * `elem` (Impact: 36.8 | O(2^N) | DB: 1)
  * `union` (Impact: 34.9 | O(2^N))
  * `intersection` (Impact: 20.2 | O(2^N))
  * `difference` (Impact: 20.2 | O(2^N))
    * *Intent:* /** * Find the first element which satisfies a predicate (or a refinement) function * * @example * i...
  * `takeLeftWhile` (Impact: 18.6 | O(N^2) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 767`, `args: 410`, `func_start: 233`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 138`, `planned_debt: 15`, `duplicate_logic: 13`
* *Architecture:* `api: 215`, `import: 39`
* *Defense:* `safety: 11`, `doc: 175`, `immutability_locks: 271`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` function, Foldable, Option, Either, Applicative, string, Traversable, Semigroup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlyRecord.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.304 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.534 IQR)
- **Top Global Matches:** file_cluster_16: 11.304, file_cluster_8: 11.888, file_cluster_2: 11.907
- **Magnitude:** 80.37 | **LOC:** 2297 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.3177%), Tech Debt (77.1787%)
**Top Internal Functions/Classes:**
  * `isSubrecord` (Impact: 52.4 | O(2^N))
    * *Intent:* /** * Use the overload constrained by `Ord` instead. * * @deprecated
  * `elem` (Impact: 44.9 | O(2^N))
  * `f` (Impact: 28.8 | O(N^3))
    * *Intent:* // TODO: remove non-curried overloading in v3 /** * Lookup the value for a key in a `ReadonlyRecord`...
  * `foldMapWithIndex` (Impact: 26.6 | O(2^N) | DB: 2)
    * *Intent:* /** * Test whether or not a key exists in a `ReadonlyRecord`. * * Note. This function is not pipeabl...
  * `getShow` (Impact: 26.1 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 734`, `args: 372`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 32`, `planned_debt: 3`, `duplicate_logic: 10`
* *Architecture:* `api: 172`
* *Defense:* `safety: 9`, `doc: 122`, `immutability_locks: 181`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` function, ReadonlyRecord, Foldable, Option, string, Applicative, Traversable, Semigroup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/linter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_17` (Drift: 9.437 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.507 IQR)
- **Top Global Matches:** file_cluster_17: 9.437, file_cluster_8: 9.44, file_cluster_2: 9.759
- **Magnitude:** 67.9 | **LOC:** 653 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 24
- **Risk Profile:** Cognitive Load (9.7501%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parseType` (Impact: 162.6 | O(2^N))
  * `getTypeArguments` (Impact: 155.4 | O(2^N))
  * `lintType` (Impact: 80.2 | O(2^N) | DB: 24)
  * `parseVariableDeclaration` (Impact: 55.8 | O(2^N))
  * `parseInterface` (Impact: 55.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 281`, `args: 55`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 43`, `import: 8`
* *Defense:* `doc: 1`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` path, glob, string, Monoid, Option, function, ReadonlyArray, ts-morph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 67.52 | **LOC:** 3376 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pipeable.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.146 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.617 IQR)
- **Top Global Matches:** file_cluster_16: 11.146, file_cluster_8: 12.088, file_cluster_2: 12.211
- **Magnitude:** 56.59 | **LOC:** 2612 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.1162%), Tech Debt (98.9586%)
**Top Internal Functions/Classes:**
  * `bimap` (Impact: 5.1 | O(2^N))
  * `partition` (Impact: 5.1 | O(2^N))
  * `partitionMap` (Impact: 5.1 | O(2^N))
  * `promap` (Impact: 5.1 | O(2^N))
  * `foldMapWithIndex` (Impact: 4.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 2243`, `args: 1193`, `func_start: 251`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 17`, `duplicate_logic: 50`
* *Architecture:* `api: 313`, `import: 24`
* *Defense:* `safety: 20`, `doc: 260`, `immutability_locks: 279`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` MonadThrow, Foldable, Option, FoldableWithIndex, Refinement, function, Extend, Functor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlySet.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.141 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.64 IQR)
- **Top Global Matches:** file_cluster_16: 12.141, file_cluster_13: 12.576, file_cluster_11: 12.613
- **Magnitude:** 50.25 | **LOC:** 605 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (14.2479%), Tech Debt (99.9797%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 52.6 | O(2^N) | DB: 1)
  * `intersection` (Impact: 52.5 | O(2^N) | DB: 1)
  * `partitionMap` (Impact: 37.5 | O(N^3) | DB: 3)
  * `separate` (Impact: 33.3 | O(N^3) | DB: 2)
    * *Intent:* /** * @since 2.5.0
  * `elem` (Impact: 24.8 | O(2^N) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 240`, `args: 128`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 62`, `import: 12`
* *Defense:* `safety: 1`, `doc: 40`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Separated, function, Eq, Magma, ReadonlySet, Show, Option, Either...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlyNonEmptyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.578 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.443 IQR)
- **Top Global Matches:** file_cluster_16: 12.578, file_cluster_13: 12.935, file_cluster_2: 13.111
- **Magnitude:** 47.07 | **LOC:** 1498 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (9.5456%), Tech Debt (46.5606%)
**Top Internal Functions/Classes:**
  * `rotate` (Impact: 20.8 | O(2^N))
    * *Intent:* /** * Remove duplicates from a `ReadonlyNonEmptyArray`, keeping the first occurrence of an element. ...
  * `group` (Impact: 16.1 | O(N^2) | DB: 6)
    * *Intent:* /** * Rotate a `ReadonlyNonEmptyArray` by `n` steps. * * @example * import { rotate } from 'fp-ts/Re...
  * `groupBy` (Impact: 14.1 | O(N^2) | DB: 1)
    * *Intent:* // ------------------------------------------------------------------------------------- // construc...
  * `uniq` (Impact: 12.8 | O(N^2) | DB: 1)
  * `zip` (Impact: 12.4 | O(2^N))
    * *Intent:* /** * Create a `ReadonlyNonEmptyArray` containing a range of integers, including both endpoints. * *...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 442`, `args: 217`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 98`, `duplicate_logic: 6`
* *Architecture:* `api: 135`, `import: 27`
* *Defense:* `safety: 3`, `doc: 130`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` function, Foldable, Option, string, Applicative, Traversable, Semigroup, FoldableWithIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.075 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.642 IQR)
- **Top Global Matches:** file_cluster_16: 12.075, file_cluster_13: 12.458, file_cluster_11: 12.62
- **Magnitude:** 45.57 | **LOC:** 925 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (10.1594%), Tech Debt (68.4008%)
**Top Internal Functions/Classes:**
  * `lookupWithKey` (Impact: 45.0 | O(2^N) | DB: 1)
  * `predicateWithIndex` (Impact: 21.7 | O(2^N) | DB: 3)
    * *Intent:* /**
  * `getMonoid` (Impact: 19.4 | O(N^2) | DB: 3)
  * `difference` (Impact: 16.2 | O(2^N))
  * `union` (Impact: 12.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 396`, `args: 202`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 96`, `planned_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 81`, `import: 27`
* *Defense:* `safety: 5`, `doc: 65`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` Foldable, Option, Applicative, Semigroup, FoldableWithIndex, Refinement, Ord, function...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/NonEmptyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.705 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.544 IQR)
- **Top Global Matches:** file_cluster_16: 12.705, file_cluster_13: 13.075, file_cluster_2: 13.249
- **Magnitude:** 44.27 | **LOC:** 1408 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (10.7186%), Tech Debt (32.2451%)
**Top Internal Functions/Classes:**
  * `rotate` (Impact: 20.8 | O(2^N))
    * *Intent:* /**
  * `group` (Impact: 16.1 | O(N^2) | DB: 6)
    * *Intent:* /** * Rotate a `NonEmptyArray` by `n` steps.
  * `groupBy` (Impact: 14.1 | O(N^2) | DB: 1)
  * `uniq` (Impact: 12.8 | O(N^2) | DB: 1)
    * *Intent:* /** * @internal */
  * `zip` (Impact: 12.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 432`, `args: 211`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 98`, `duplicate_logic: 4`
* *Architecture:* `api: 134`, `import: 26`
* *Defense:* `safety: 2`, `doc: 129`, `immutability_locks: 157`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` function, Foldable, Option, string, Applicative, Traversable, Semigroup, FoldableWithIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Array.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.53 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.98 IQR)
- **Top Global Matches:** file_cluster_16: 12.53, file_cluster_13: 12.831, file_cluster_11: 13.063
- **Magnitude:** 41.42 | **LOC:** 3021 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (8.7225%), Tech Debt (95.4529%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 28.7 | O(2^N))
    * *Intent:* /** * Get the first element in an array, or `None` if the array is empty *
  * `intersection` (Impact: 16.5 | O(2^N))
    * *Intent:* /** * Get the last element in an array, or `None` if the array is empty * * @example * import { last...
  * `difference` (Impact: 16.5 | O(2^N))
  * `takeLeftWhile` (Impact: 12.6 | O(N^2) | DB: 1)
  * `zip` (Impact: 12.3 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 429`, `args: 239`, `func_start: 125`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`, `planned_debt: 6`, `duplicate_logic: 6`
* *Architecture:* `api: 109`, `import: 38`
* *Defense:* `safety: 3`, `doc: 77`, `immutability_locks: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` function, Foldable, Option, string, Applicative, Either, Traversable, Semigroup...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Set.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.284 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.927 IQR)
- **Top Global Matches:** file_cluster_16: 12.284, file_cluster_13: 12.67, file_cluster_11: 12.751
- **Magnitude:** 37.77 | **LOC:** 495 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (15.147%), Tech Debt (99.8264%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 43.1 | O(2^N) | DB: 1)
  * `intersection` (Impact: 43.0 | O(2^N) | DB: 1)
  * `partitionMap` (Impact: 37.5 | O(N^3) | DB: 3)
    * *Intent:* // TODO: remove non-curried overloading in v3 /**
  * `separate` (Impact: 33.1 | O(N^3) | DB: 2)
    * *Intent:* /**
  * `difference` (Impact: 16.5 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 200`, `args: 108`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `planned_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `api: 52`, `import: 13`
* *Defense:* `safety: 1`, `doc: 36`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Separated, function, ReadonlySet, Eq, Magma, Show, Option, Either...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/function.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.255 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 4.887 IQR)
- **Top Global Matches:** file_cluster_16: 11.255, file_cluster_8: 11.416, file_cluster_13: 11.656
- **Magnitude:** 33.69 | **LOC:** 806 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.7589%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pipe` (Impact: 101.6 | O(N^2) | DB: 2)
  * `flow` (Impact: 92.6 | O(N^2))
    * *Intent:* /** * A thunk that returns always `null`. *
  * `body` (Impact: 11.0 | O(2^N))
  * `flip` (Impact: 4.5 | O(N^1))
  * `absurd` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 450`, `args: 326`, `func_start: 290`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 7`
* *Architecture:* `api: 73`, `import: 6`
* *Defense:* `safety: 30`, `doc: 42`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` function, Ring, BooleanAlgebra, Semigroup, boolean, Monoid, Predicate, Semiring
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Apply.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.027 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.854 IQR)
- **Top Global Matches:** file_cluster_16: 11.027, file_cluster_8: 11.932, file_cluster_2: 11.959
- **Magnitude:** 30.39 | **LOC:** 714 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (6.2146%), Tech Debt (99.974%)
**Top Internal Functions/Classes:**
  * `getRecordConstructor` (Impact: 37.9 | O(N^3) | DB: 1)
  * `curried` (Impact: 12.5 | O(2^N) | DB: 1)
  * `apS` (Impact: 6.0 | O(N^1))
  * `apS` (Impact: 6.0 | O(N^1))
  * `apS` (Impact: 6.0 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 576`, `args: 315`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 18`, `duplicate_logic: 24`
* *Architecture:* `api: 99`, `import: 5`
* *Defense:* `safety: 22`, `doc: 15`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` function, HKT, Functor, Either, internal, Semigroup, Apply, function...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EitherT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.127 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.076 IQR)
- **Top Global Matches:** file_cluster_16: 11.127, file_cluster_8: 11.997, file_cluster_2: 12.012
- **Magnitude:** 29.63 | **LOC:** 949 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (2.4399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `onRight` (Impact: 5.7 | O(2^N))
  * `tapError` (Impact: 5.4 | O(N^1))
    * *Intent:* /** * @category error handling * @since 2.11.0
  * `flatMap` (Impact: 5.1 | O(N^1))
  * `alt` (Impact: 5.1 | O(N^1))
    * *Intent:* /**
  * `match` (Impact: 5.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 900`, `args: 565`, `func_start: 231`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 180`, `import: 10`
* *Defense:* `safety: 35`, `doc: 59`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.927
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.025126
  * `Imports (Out-Degree: 4):` HKT, Functor, Chain, Either, Applicative, Monad, Pointed, Semigroup...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ReadonlyMap.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.249 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.663 IQR)
- **Top Global Matches:** file_cluster_16: 11.249, file_cluster_13: 11.399, file_cluster_11: 11.627
- **Magnitude:** 29.15 | **LOC:** 1217 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (7.8128%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `isSubmap` (Impact: 49.1 | O(2^N) | DB: 1)
  * `lookupWithKey` (Impact: 45.0 | O(2^N) | DB: 1)
  * `elem` (Impact: 36.9 | O(2^N) | DB: 1)
    * *Intent:* // TODO: remove non-curried overloading in v3 /** * Test whether or not a key exists in a map * * @s...
  * `lookup` (Impact: 20.3 | O(2^N))
  * `member` (Impact: 16.5 | O(2^N))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 173`, `args: 79`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 33`, `import: 28`
* *Defense:* `safety: 2`, `doc: 23`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` ReadonlyMap, Foldable, Option, Applicative, Traversable, Semigroup, FoldableWithIndex, Refinement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/These.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.583 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.225 IQR)
- **Top Global Matches:** file_cluster_16: 11.583, file_cluster_13: 11.806, file_cluster_17: 12.093
- **Magnitude:** 27.54 | **LOC:** 807 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (5.6319%), Tech Debt (9.7841%)
**Top Internal Functions/Classes:**
  * `getSemigroup` (Impact: 28.1 | O(N^2))
    * *Intent:* /** * Less strict version of [`match`](#match). *
  * `traverseReadonlyNonEmptyArrayWithIndex` (Impact: 25.2 | O(N^2) | DB: 3)
    * *Intent:* /* istanbul ignore next */
  * `getApply` (Impact: 24.5 | O(N^2))
    * *Intent:* /** * Alias of [`matchW`](#matchw). * * @category pattern matching * @since 2.10.0 */
  * `matchW` (Impact: 17.4 | O(N^2))
    * *Intent:* // ------------------------------------------------------------------------------------- // refineme...
  * `getEq` (Impact: 14.4 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 235`, `args: 127`, `func_start: 66`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`, `planned_debt: 2`
* *Architecture:* `api: 69`, `import: 25`
* *Defense:* `safety: 14`, `doc: 60`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.959
  * `Choke Point (Betweenness):` 0.000955 | `Ripple Effect (Closeness):` 0.025844
  * `Imports (Out-Degree: 12):` MonadThrow, Foldable, Option, Applicative, Traversable, Semigroup, Refinement, These...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/TaskEither.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.014 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.623 IQR)
- **Top Global Matches:** file_cluster_16: 12.014, file_cluster_2: 12.325, file_cluster_13: 12.471
- **Magnitude:** 26.07 | **LOC:** 1882 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.8839%), Tech Debt (71.0701%)
**Top Internal Functions/Classes:**
  * `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 13.8 | O(N^4) | DB: 1)
  * `taskify` (Impact: 5.7 | O(N^2))
  * `async` (Impact: 5.5 | O(N^1))
  * `getFilterable` (Impact: 5.0 | O(2^N))
  * `onLeft` (Impact: 4.4 | O(2^N))
    * *Intent:* /** * Less strict version of [`matchE`](#matche). *
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 590`, `args: 311`, `func_start: 91`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 155`, `concurrency: 6`, `import: 32`
* *Defense:* `safety: 49`, `doc: 158`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` MonadThrow, function, MonadTask, IO, Option, Either, string, Applicative...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/OptionT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.506 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.514 IQR)
- **Top Global Matches:** file_cluster_16: 11.506, file_cluster_8: 12.426, file_cluster_2: 12.463
- **Magnitude:** 24.34 | **LOC:** 696 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (74.9721%)
**Top Internal Functions/Classes:**
  * `match` (Impact: 5.1 | O(2^N))
  * `onSome` (Impact: 5.0 | O(2^N))
    * *Intent:* // ------------------------------------------------------------------------------------- // deprecat...
  * `some` (Impact: 4.2 | O(2^N))
  * `fromNullable` (Impact: 4.2 | O(2^N))
  * `fromEither` (Impact: 4.2 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 733`, `args: 439`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 8`
* *Architecture:* `api: 152`, `import: 12`
* *Defense:* `safety: 30`, `doc: 45`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.667
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.015075
  * `Imports (Out-Degree: 6):` HKT, Functor, Chain, Option, Either, Applicative, Monad, Pointed...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/IOEither.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.622 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.655 IQR)
- **Top Global Matches:** file_cluster_16: 11.622, file_cluster_2: 11.917, file_cluster_13: 12.077
- **Magnitude:** 20.38 | **LOC:** 1395 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (3.1894%), Tech Debt (81.2792%)
**Top Internal Functions/Classes:**
  * `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 11.3 | O(N^2) | DB: 2)
  * `getFilterable` (Impact: 5.0 | O(2^N))
  * `onLeft` (Impact: 4.4 | O(2^N))
    * *Intent:* /*#__PURE__*/ ET.matchE(I.Monad) /** * Alias of [`matchE`](#matche). * * @category pattern matching
  * `f` (Impact: 4.1 | O(N^1))
  * `getCompactable` (Impact: 3.9 | O(2^N))
    * *Intent:* /** * @category error handling * @since 2.11.0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 447`, `args: 231`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 8`, `duplicate_logic: 8`
* *Architecture:* `api: 122`, `import: 26`
* *Defense:* `safety: 25`, `doc: 131`, `immutability_locks: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` MonadThrow, function, IO, Option, Either, Applicative, Semigroup, Refinement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Either.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.187 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.305 IQR)
- **Top Global Matches:** file_cluster_16: 11.187, file_cluster_13: 11.439, file_cluster_2: 11.525
- **Magnitude:** 20.02 | **LOC:** 1854 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (3.6673%), Tech Debt (90.1764%)
**Top Internal Functions/Classes:**
  * `getFilterable` (Impact: 25.4 | O(N^2))
  * `getCompactable` (Impact: 13.7 | O(N^2))
    * *Intent:* // ------------------------------------------------------------------------------------- // construc...
  * `getApplicativeValidation` (Impact: 11.1 | O(N^2))
  * `getEq` (Impact: 10.2 | O(N^1))
  * `isLeft` (Impact: 9.2 | O(2^N))
    * *Intent:* // -------------------------------------------------------------------------------------
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 238`, `args: 130`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 62`, `import: 30`
* *Defense:* `safety: 11`, `doc: 59`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` function, MonadThrow, Foldable, Either, Option, Applicative, string, Traversable...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Tree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.473 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.434 IQR)
- **Top Global Matches:** file_cluster_16: 11.473, file_cluster_13: 11.879, file_cluster_2: 12.1
- **Magnitude:** 19.03 | **LOC:** 647 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (6.6375%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 17.9 | O(2^N) | DB: 3)
    * *Intent:* /** * @category instances * @since 2.0.0 */
  * `reduce` (Impact: 8.5 | O(2^N) | DB: 2)
  * `reduceRight` (Impact: 8.5 | O(2^N) | DB: 2)
    * *Intent:* /** * Fold a tree into a "summary" value in depth-first order. * * For each node in the tree, apply ...
  * `getEq` (Impact: 8.3 | O(2^N) | DB: 1)
  * `predicate` (Impact: 7.1 | O(2^N))
    * *Intent:* /** * @category constructors * @since 2.7.0 */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 239`, `args: 111`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 67`, `import: 18`
* *Defense:* `doc: 51`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Foldable, Applicative, Traversable, function, Show, Extend, Functor, Chain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TheseT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.043 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.415 IQR)
- **Top Global Matches:** file_cluster_16: 11.043, file_cluster_8: 11.925, file_cluster_13: 12.166
- **Magnitude:** 18.76 | **LOC:** 602 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (51.4056%)
**Top Internal Functions/Classes:**
  * `chain` (Impact: 9.0 | O(2^N))
  * `getTheseM` (Impact: 5.2 | O(N^2))
  * `bimap` (Impact: 5.1 | O(2^N))
  * `mapLeft` (Impact: 5.1 | O(2^N))
  * `toTuple2` (Impact: 5.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 565`, `args: 369`, `func_start: 170`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 108`, `import: 9`
* *Defense:* `safety: 30`, `doc: 35`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.696
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.011307
  * `Imports (Out-Degree: 5):` These, HKT, Functor, Chain, Monad, Pointed, Semigroup, function...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/TaskOption.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.339 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.648 IQR)
- **Top Global Matches:** file_cluster_16: 11.339, file_cluster_13: 11.736, file_cluster_2: 11.885
- **Magnitude:** 15.68 | **LOC:** 1061 | **CtrlFlow:** 1.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (3.409%), Tech Debt (37.8798%)
**Top Internal Functions/Classes:**
  * `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 13.8 | O(N^4) | DB: 1)
  * `async` (Impact: 5.5 | O(N^1))
    * *Intent:* /*#__PURE__*/ OT.match(T.Functor) /** * Less strict version of [`match`](#match). * * The `W` suffix...
  * `_apSeq` (Impact: 3.9 | O(2^N))
    * *Intent:* /** * @category error handling * @since 2.10.0 */
  * `f` (Impact: 3.7 | O(N^1))
    * *Intent:* /** * Runs computations sequentially. * * @category instances * @since 2.10.0
  * `f` (Impact: 3.7 | O(N^1))
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`, `structural_boundaries: 332`, `args: 154`, `func_start: 42`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 5`, `duplicate_logic: 3`
* *Architecture:* `api: 99`, `concurrency: 5`, `import: 29`
* *Defense:* `safety: 12`, `doc: 102`, `immutability_locks: 111`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` function, MonadTask, TaskOption, IO, Option, Either, Applicative, Refinement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.58 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (9.027%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.eslint.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.32 | **LOC:** 17 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (14.8047%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/ReaderEither.ts` (TYPESCRIPT) | Magnitude: 2.44 | Delta: **0.024 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 75, generics: 56, indent_spaces: 51, args: 24
- `dtslint/Apply.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.044 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: structural_boundaries: 20, immutability_locks: 16, args: 13, func_start: 13
- `dtslint/Ord.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 4, explicit_casts: 3
- `dtslint/Show.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 4, explicit_casts: 3
- `dtslint/Traversable.ts` (TYPESCRIPT) | Magnitude: 1.31 | Delta: **0.055 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 4, import: 4, explicit_casts: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/IORef.ts` (TYPESCRIPT) | Magnitude: 2.19 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 12, state_mutation: 9, args: 8
- `src/StateReaderTaskEither.ts` (TYPESCRIPT) | Magnitude: 5.8 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 92, generics: 63, indent_spaces: 43, args: 37
- `src/Random.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 14, func_start: 10, args: 9
- `src/ReaderTaskEither.ts` (TYPESCRIPT) | Magnitude: 4.68 | Delta: **0.074 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 136, generics: 110, indent_spaces: 78, args: 56
- `src/Eq.ts` (TYPESCRIPT) | Magnitude: 2.26 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, generics: 16, indent_spaces: 12, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/linter.ts` (TYPESCRIPT) | Magnitude: 67.9 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 466, structural_boundaries: 281, immutability_locks: 100, branch: 83
- `src/Ring.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 27, args: 15, generics: 15, indent_spaces: 12
- `perf/function/flow.ts` (TYPESCRIPT) | Magnitude: 2.69 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 21, args: 10, state_mutation: 9, structural_boundaries: 7
- `perf/function/pipe.ts` (TYPESCRIPT) | Magnitude: 2.62 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, args: 9, state_mutation: 9, structural_boundaries: 6
- `scripts/build.ts` (TYPESCRIPT) | Magnitude: 2.8 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 53, args: 33, comprehensions: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Record.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 75, indent_spaces: 39, ui_framework: 7, generics: 7
- `dtslint/ReaderTask.ts` (TYPESCRIPT) | Magnitude: 5.24 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 14, ui_framework: 12, generics: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `perf/ReadonlyNonEmptyArray.ts/reverse.ts` (TYPESCRIPT) | Magnitude: 1.84 | Delta: **0.031 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, args: 6, state_mutation: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dtslint/NonEmptyArray.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 21, immutability_locks: 15, args: 13, func_start: 8
- `dtslint/ReadonlyNonEmptyArray.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 21, immutability_locks: 15, args: 13, func_start: 8
- `scripts/run.ts` (TYPESCRIPT) | Magnitude: 0.75 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, structural_boundaries: 6, args: 5, func_start: 3
- `dtslint/Eq.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 4, explicit_casts: 3
- `dtslint/Monoid.ts` (TYPESCRIPT) | Magnitude: 1.36 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 4, import: 4, explicit_casts: 3

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/BooleanAlgebra.ts` -> **Severity: 0.101** (Bridge: 0.0025 * Flux: 40.1312%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/HKT.ts` -> **Severity: 31.067** (Embedded: 0.3127 * Error Risk: 99.3568%)
- `src/Chain.ts` -> **Severity: 10.565** (Embedded: 0.2123 * Error Risk: 49.771%)
- `src/Magma.ts` -> **Severity: 5.086** (Embedded: 0.1043 * Error Risk: 48.7503%)
- `src/Bounded.ts` -> **Severity: 5.05** (Embedded: 0.0955 * Error Risk: 52.854%)
- `src/internal.ts` -> **Severity: 4.993** (Embedded: 0.2111 * Error Risk: 23.6524%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/HKT.ts` -> **Severity: 14776.286** (Blast Radius: 149.621 * Doc Risk: 98.7581%)
- `src/internal.ts` -> **Severity: 4070.747** (Blast Radius: 42.767 * Doc Risk: 95.1843%)
- `src/Refinement.ts` -> **Severity: 3166.084** (Blast Radius: 31.813 * Doc Risk: 99.5217%)
- `src/Chain.ts` -> **Severity: 2916.149** (Blast Radius: 29.333 * Doc Risk: 99.4153%)
- `src/number.ts` -> **Severity: 1632.832** (Blast Radius: 28.985 * Doc Risk: 56.3337%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
