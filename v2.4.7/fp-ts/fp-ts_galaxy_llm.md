# ARCHITECTURAL_BRIEF: fp-ts
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_typescript/fp-ts` |
| **Timestamp** | `2026-08-07T04:15:09.688556+00:00` |
| **Scan Duration** | `1.57s` |
| **Git Branch** | `master` |
| **Git Commit** | `09045f5819af260b5a6c4aeabdf2fbc8d9b9e335` |
| **Git Remote** | `https://github.com/gcanti/fp-ts.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 190 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 99.7 | 10.0 | 4.7 | 0.0 |
| Error & Exception Exposure | 0.0 | 99.4 | 22.5 | 0.0 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 27.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 11.5 | 2.3 | 2.3 |
| API Exposure | 0.0 | 15.4 | 7.0 | 8.9 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 8.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 29.3 | 0.2 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 88.5 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 0.5 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 33.5 | 14.4 | 0.0 |
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

- `parseType` (@ `scripts/linter.ts`) -> Impact: **83.5** | LOC: 89
- `pipe` (@ `src/function.ts`) -> Impact: **68.4** | LOC: 39
- `flow` (@ `src/function.ts`) -> Impact: **62.5** | LOC: 49
  * *Intent:* /** * A thunk that returns always `null`. *
- `getTypeArguments` (@ `scripts/linter.ts`) -> Impact: **41.3** | LOC: 66
- `parseVariableDeclaration` (@ `scripts/linter.ts`) -> Impact: **28.9** | LOC: 42
- `lintType` (@ `scripts/linter.ts`) -> Impact: **28.2** | LOC: 45
- `main` (@ `examples/fp-ts-to-the-max-II.ts`) -> Impact: **27.5** | LOC: 60
- `getRecordConstructor` (@ `src/Apply.ts`) -> Impact: **19.9** | LOC: 38
- `parseInterface` (@ `scripts/linter.ts`) -> Impact: **19.5** | LOC: 33
- `union` (@ `src/ReadonlySet.ts`) -> Impact: **18.3** | LOC: 24

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 123 | 1048.55 | 4.24% | 29.11% |
| `dtslint` | 44 | 129.17 | 4.24% | 21.43% |
| `__monolith__` | 9 | 126.22 | 4.59% | 11.09% |
| `scripts` | 6 | 38.04 | 7.32% | 20.97% |
| `examples` | 3 | 27.96 | 9.94% | 0.0% |
| `perf/Task` | 3 | 7.04 | 52.49% | 0.0% |
| `perf/function` | 2 | 6.01 | 99.47% | 100.0% |
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
- `src/pipeable.ts` -> **0** Orphaned Functions | **58** Duplicates
- `dtslint/ReaderTaskEither.ts` -> **0** Orphaned Functions | **24** Duplicates
- `src/Apply.ts` -> **0** Orphaned Functions | **24** Duplicates
- `src/Filterable.ts` -> **0** Orphaned Functions | **22** Duplicates
- `src/Witherable.ts` -> **0** Orphaned Functions | **19** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `217` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `perf/function/flow.ts` (TYPESCRIPT) -> Cumulative Risk: **615.95**
- **Archetype:** `file_cluster_17` (Distance: 12.822 IQR)
- **Magnitude:** 3.03 | **LOC:** 36 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9294%), Concurrency (99.8982%)
- **Heaviest Functions:** `flow2` (Impact: 4.5), `flow` (Impact: 3.5), `flow2` (Impact: 3.4)

### 2. `perf/ReadonlyNonEmptyArray.ts/reverse.ts` (TYPESCRIPT) -> Cumulative Risk: **614.15**
- **Archetype:** `file_cluster_4` (Distance: 12.564 IQR)
- **Magnitude:** 1.76 | **LOC:** 29 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9895%), State Flux (99.9835%)
- **Heaviest Functions:** `reverse2` (Impact: 2.5), `reverse2` (Impact: 1.7)

### 3. `perf/function/pipe.ts` (TYPESCRIPT) -> Cumulative Risk: **595.87**
- **Archetype:** `file_cluster_17` (Distance: 13.759 IQR)
- **Magnitude:** 2.98 | **LOC:** 33 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), State Flux (99.9893%), Concurrency (99.9396%)
- **Heaviest Functions:** `pipe2` (Impact: 3.8), `pipe2` (Impact: 3.6), `pipe` (Impact: 3.6)

### 4. `perf/Either/sequenceArray.ts` (TYPESCRIPT) -> Cumulative Risk: **551.41**
- **Archetype:** `file_cluster_13` (Distance: 11.457 IQR)
- **Magnitude:** 1.34 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9828%), Cognitive Load (85.8149%)
- **Heaviest Functions:** `pipe` (Impact: 2.0), `pipe` (Impact: 2.0)

### 5. `perf/IO/sequenceArray.ts` (TYPESCRIPT) -> Cumulative Risk: **551.41**
- **Archetype:** `file_cluster_13` (Distance: 11.457 IQR)
- **Magnitude:** 1.34 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9828%), Cognitive Load (85.8149%)
- **Heaviest Functions:** `pipe` (Impact: 2.0), `pipe` (Impact: 2.0)

### 6. `perf/StateReaderTaskEither/sequenceArray.ts` (TYPESCRIPT) -> Cumulative Risk: **551.41**
- **Archetype:** `file_cluster_13` (Distance: 11.457 IQR)
- **Magnitude:** 1.34 | **LOC:** 33 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (99.9828%), Cognitive Load (85.8149%)
- **Heaviest Functions:** `pipe` (Impact: 2.0), `pipe` (Impact: 2.0)

### 7. `src/ReadonlySet.ts` (TYPESCRIPT) -> Cumulative Risk: **540.52**
- **Archetype:** `file_cluster_16` (Distance: 12.134 IQR)
- **Magnitude:** 34.52 | **LOC:** 605 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9797%), Documentation (84.7082%), Verification (80.0%)
- **Heaviest Functions:** `union` (Impact: 18.3), `intersection` (Impact: 18.2), `partitionMap` (Impact: 17.1)

### 8. `src/Set.ts` (TYPESCRIPT) -> Cumulative Risk: **534.65**
- **Archetype:** `file_cluster_16` (Distance: 12.279 IQR)
- **Magnitude:** 25.89 | **LOC:** 495 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.8264%), Documentation (85.4917%), Verification (80.0%)
- **Heaviest Functions:** `partitionMap` (Impact: 17.1), `union` (Impact: 15.1), `separate` (Impact: 15.0)

### 9. `src/Apply.ts` (TYPESCRIPT) -> Cumulative Risk: **492.59**
- **Archetype:** `file_cluster_16` (Distance: 11.016 IQR)
- **Magnitude:** 27.09 | **LOC:** 714 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.974%), Documentation (97.8801%), Safety Score (84.8538%)
- **Heaviest Functions:** `getRecordConstructor` (Impact: 19.9), `curried` (Impact: 6.5), `apS` (Impact: 6.0)

### 10. `src/Map.ts` (TYPESCRIPT) -> Cumulative Risk: **451.34**
- **Archetype:** `file_cluster_16` (Distance: 12.045 IQR)
- **Magnitude:** 35.44 | **LOC:** 925 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Verification (80.0%), Safety Score (72.7396%), Documentation (69.0804%)
- **Heaviest Functions:** `lookupWithKey` (Impact: 15.6), `getMonoid` (Impact: 11.7), `concat` (Impact: 11.4)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/ReadonlyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.77 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.471 IQR)
- **Top Global Matches:** file_cluster_16: 12.77, file_cluster_13: 13.141, file_cluster_11: 13.235
- **Magnitude:** 72.32 | **LOC:** 2665 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.84%), Tech Debt (98.6851%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 17.7)
  * `elem` (Impact: 12.8)
  * `takeLeftWhile` (Impact: 12.7)
  * `chainRecBreadthFirst` (Impact: 12.4)
    * *Intent:* // TODO: remove non-curried overloading in v3 /** * Creates an array of unique values, in order, fro...
  * `intersection` (Impact: 10.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 130`, `structural_boundaries: 767`, `args: 410`, `func_start: 233`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 136`, `planned_debt: 15`, `duplicate_logic: 17`
* *Architecture:* `api: 215`, `import: 39`
* *Defense:* `safety: 11`, `doc: 175`, `immutability_locks: 271`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` HKT, Either, function, Functor, Show, Unfoldable, Refinement, FunctorWithIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `CHANGELOG.md` (MARKDOWN | Tier 1 | AI Safe: 0.0%)
- **Global Archetype:** `Static: Literature & Documentation` (Drift: N/A IQR)
- **Magnitude:** 67.52 | **LOC:** 3376 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `src/ReadonlyRecord.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.28 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.535 IQR)
- **Top Global Matches:** file_cluster_16: 11.28, file_cluster_8: 11.864, file_cluster_2: 11.883
- **Magnitude:** 56.83 | **LOC:** 2297 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.3177%), Tech Debt (90.6431%)
**Top Internal Functions/Classes:**
  * `isSubrecord` (Impact: 18.1)
    * *Intent:* /** * Use the overload constrained by `Ord` instead. * * @deprecated
  * `union` (Impact: 17.2)
    * *Intent:* /** * Create a `ReadonlyRecord` with one key/value pair.
  * `elem` (Impact: 15.5)
  * `f` (Impact: 14.9)
    * *Intent:* // TODO: remove non-curried overloading in v3 /** * Lookup the value for a key in a `ReadonlyRecord`...
  * `getMonoid` (Impact: 13.0)
    * *Intent:* /** * Create a `ReadonlyRecord` from a foldable collection of key/value pairs, using the * specified...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 101`, `structural_boundaries: 734`, `args: 372`, `func_start: 188`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 32`, `planned_debt: 3`, `duplicate_logic: 13`
* *Architecture:* `api: 172`
* *Defense:* `safety: 9`, `doc: 122`, `immutability_locks: 181`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` HKT, ReadonlyRecord, Apply, function, Functor, Show, Unfoldable, Refinement...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/pipeable.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.119 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.618 IQR)
- **Top Global Matches:** file_cluster_16: 11.119, file_cluster_8: 12.062, file_cluster_2: 12.186
- **Magnitude:** 51.89 | **LOC:** 2612 | **CtrlFlow:** 5.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1162%), Tech Debt (99.6608%)
**Top Internal Functions/Classes:**
  * `partition` (Impact: 3.3)
  * `partition` (Impact: 3.2)
    * *Intent:* /** * Returns a pipeable `filter` *
  * `f` (Impact: 3.2)
    * *Intent:* /** * @category zone of death * @since 2.0.0
  * `filter` (Impact: 3.1)
  * `filter` (Impact: 3.1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 2243`, `args: 1193`, `func_start: 251`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 17`, `duplicate_logic: 58`
* *Architecture:* `api: 313`, `import: 24`
* *Defense:* `safety: 20`, `doc: 260`, `immutability_locks: 279`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` HKT, Contravariant, Functor, Refinement, FunctorWithIndex, FoldableWithIndex, Chain, Alt...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlyNonEmptyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.569 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.438 IQR)
- **Top Global Matches:** file_cluster_16: 12.569, file_cluster_13: 12.924, file_cluster_2: 13.102
- **Magnitude:** 42.62 | **LOC:** 1498 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.5456%), Tech Debt (73.9488%)
**Top Internal Functions/Classes:**
  * `group` (Impact: 11.2)
    * *Intent:* /** * Rotate a `ReadonlyNonEmptyArray` by `n` steps. * * @example * import { rotate } from 'fp-ts/Re...
  * `rotate` (Impact: 10.8)
    * *Intent:* /** * Remove duplicates from a `ReadonlyNonEmptyArray`, keeping the first occurrence of an element. ...
  * `groupBy` (Impact: 9.6)
    * *Intent:* // ------------------------------------------------------------------------------------- // construc...
  * `uniq` (Impact: 8.8)
  * `insertAt` (Impact: 7.0)
    * *Intent:* /** * @category traversing
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 442`, `args: 217`, `func_start: 123`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 98`, `duplicate_logic: 9`
* *Architecture:* `api: 135`, `import: 27`
* *Defense:* `safety: 3`, `doc: 130`, `immutability_locks: 173`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` HKT, function, Functor, Show, Refinement, FunctorWithIndex, FoldableWithIndex, Chain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/NonEmptyArray.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.695 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.534 IQR)
- **Top Global Matches:** file_cluster_16: 12.695, file_cluster_13: 13.062, file_cluster_2: 13.239
- **Magnitude:** 40.17 | **LOC:** 1408 | **CtrlFlow:** 8.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.7186%), Tech Debt (73.3986%)
**Top Internal Functions/Classes:**
  * `group` (Impact: 11.2)
    * *Intent:* /** * Rotate a `NonEmptyArray` by `n` steps.
  * `rotate` (Impact: 10.8)
    * *Intent:* /**
  * `groupBy` (Impact: 9.6)
  * `uniq` (Impact: 8.8)
    * *Intent:* /** * @internal */
  * `sortBy` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 432`, `args: 211`, `func_start: 103`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 98`, `duplicate_logic: 8`
* *Architecture:* `api: 134`, `import: 26`
* *Defense:* `safety: 2`, `doc: 129`, `immutability_locks: 157`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` HKT, function, Functor, Show, Refinement, FunctorWithIndex, FoldableWithIndex, Chain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Map.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.045 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.642 IQR)
- **Top Global Matches:** file_cluster_16: 12.045, file_cluster_13: 12.43, file_cluster_11: 12.592
- **Magnitude:** 35.44 | **LOC:** 925 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.1594%), Tech Debt (68.4008%)
**Top Internal Functions/Classes:**
  * `lookupWithKey` (Impact: 15.6)
  * `getMonoid` (Impact: 11.7)
  * `concat` (Impact: 11.4)
  * `predicateWithIndex` (Impact: 7.8)
    * *Intent:* /**
  * `fromFoldable` (Impact: 6.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 396`, `args: 202`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 96`, `planned_debt: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 81`, `import: 27`
* *Defense:* `safety: 5`, `doc: 65`, `immutability_locks: 137`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` HKT, Functor, Show, Unfoldable, Refinement, FoldableWithIndex, Semigroup, Eq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlySet.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.134 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.64 IQR)
- **Top Global Matches:** file_cluster_16: 12.134, file_cluster_13: 12.57, file_cluster_11: 12.606
- **Magnitude:** 34.52 | **LOC:** 605 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.2479%), Tech Debt (99.9797%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 18.3)
  * `intersection` (Impact: 18.2)
  * `partitionMap` (Impact: 17.1)
  * `separate` (Impact: 15.2)
    * *Intent:* /** * @since 2.5.0
  * `elem` (Impact: 12.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `structural_boundaries: 240`, `args: 128`, `func_start: 54`, `class_start: 1`
* *Risk/State:* `state_mutation: 70`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 62`, `import: 12`
* *Defense:* `safety: 1`, `doc: 40`, `immutability_locks: 72`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Predicate, Option, Semigroup, Eq, Monoid, function, Separated, Show...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Array.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.519 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.98 IQR)
- **Top Global Matches:** file_cluster_16: 12.519, file_cluster_13: 12.821, file_cluster_11: 13.053
- **Magnitude:** 32.5 | **LOC:** 3021 | **CtrlFlow:** 14.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.7225%), Tech Debt (95.4529%)
**Top Internal Functions/Classes:**
  * `union` (Impact: 14.7)
    * *Intent:* /** * Get the first element in an array, or `None` if the array is empty *
  * `takeLeftWhile` (Impact: 8.6)
  * `intersection` (Impact: 8.5)
    * *Intent:* /** * Get the last element in an array, or `None` if the array is empty * * @example * import { last...
  * `difference` (Impact: 8.5)
  * `spanLeftIndex` (Impact: 7.4)
    * *Intent:* /** * Create an array from an `Either`. The resulting array will contain the content of the * `Eithe...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 72`, `structural_boundaries: 429`, `args: 239`, `func_start: 125`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 52`, `planned_debt: 6`, `duplicate_logic: 6`
* *Architecture:* `api: 109`, `import: 38`
* *Defense:* `safety: 3`, `doc: 77`, `immutability_locks: 123`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 26):` HKT, Either, function, Functor, Show, Unfoldable, Refinement, FunctorWithIndex...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/linter.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_17` (Drift: 9.408 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 5.496 IQR)
- **Top Global Matches:** file_cluster_17: 9.408, file_cluster_8: 9.423, file_cluster_2: 9.74
- **Magnitude:** 32.14 | **LOC:** 653 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.842%), Tech Debt (32.044%)
**Top Internal Functions/Classes:**
  * `parseType` (Impact: 83.5)
  * `getTypeArguments` (Impact: 41.3)
  * `parseVariableDeclaration` (Impact: 28.9)
  * `lintType` (Impact: 28.2)
  * `parseInterface` (Impact: 19.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 83`, `structural_boundaries: 281`, `args: 55`, `func_start: 51`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `io: 22`, `api: 43`, `import: 8`
* *Defense:* `doc: 1`, `immutability_locks: 100`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Monoid, function, string, path, Option, ReadonlyArray, ts-morph, glob
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/EitherT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.126 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.076 IQR)
- **Top Global Matches:** file_cluster_16: 11.126, file_cluster_8: 11.996, file_cluster_2: 12.011
- **Magnitude:** 27.79 | **LOC:** 949 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (2.4399%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `tapError` (Impact: 5.4)
    * *Intent:* /** * @category error handling * @since 2.11.0
  * `flatMap` (Impact: 5.1)
  * `alt` (Impact: 5.1)
    * *Intent:* /**
  * `orElse` (Impact: 5.1)
  * `onRight` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 900`, `args: 565`, `func_start: 231`, `class_start: 4`
* *Risk/State:* None
* *Architecture:* `api: 180`, `import: 10`
* *Defense:* `safety: 35`, `doc: 59`, `immutability_locks: 52`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.927
  * `Choke Point (Betweenness):` 8e-06 | `Ripple Effect (Closeness):` 0.025126
  * `Imports (Out-Degree: 4):` HKT, Pointed, Semigroup, Monad, Functor, Either, Apply, function...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Apply.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.016 IQR)
- **Local Micro-Species:** `Cluster 2: Type Definitions & Bypasses` (Drift: 5.854 IQR)
- **Top Global Matches:** file_cluster_16: 11.016, file_cluster_8: 11.922, file_cluster_2: 11.948
- **Magnitude:** 27.09 | **LOC:** 714 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.2146%), Tech Debt (99.974%)
**Top Internal Functions/Classes:**
  * `getRecordConstructor` (Impact: 19.9)
  * `curried` (Impact: 6.5)
  * `apS` (Impact: 6.0)
  * `apS` (Impact: 6.0)
  * `apS` (Impact: 6.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 576`, `args: 315`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 18`, `duplicate_logic: 24`
* *Architecture:* `api: 99`, `import: 5`
* *Defense:* `safety: 22`, `doc: 15`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` HKT, internal, Apply, Semigroup, Option, Either, function, Functor...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/function.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.248 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 4.845 IQR)
- **Top Global Matches:** file_cluster_16: 11.248, file_cluster_8: 11.409, file_cluster_13: 11.645
- **Magnitude:** 27.06 | **LOC:** 806 | **CtrlFlow:** 8.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.7889%), Tech Debt (17.9803%)
**Top Internal Functions/Classes:**
  * `pipe` (Impact: 68.4)
  * `flow` (Impact: 62.5)
    * *Intent:* /** * A thunk that returns always `null`. *
  * `body` (Impact: 5.8)
  * `flip` (Impact: 4.5)
  * `getRing` (Impact: 2.9)
    * *Intent:* * * const f: Predicate<number> = (n) => n <= 2 * const g: Predicate<number> = (n) => n >= 0 * * cons...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 450`, `args: 327`, `func_start: 290`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 73`, `import: 6`
* *Defense:* `safety: 30`, `doc: 42`, `immutability_locks: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` Ring, Semigroup, Monoid, boolean, function, BooleanAlgebra, Predicate, Semiring
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Set.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.279 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.927 IQR)
- **Top Global Matches:** file_cluster_16: 12.279, file_cluster_13: 12.665, file_cluster_11: 12.746
- **Magnitude:** 25.89 | **LOC:** 495 | **CtrlFlow:** 18.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (15.147%), Tech Debt (99.8264%)
**Top Internal Functions/Classes:**
  * `partitionMap` (Impact: 17.1)
    * *Intent:* // TODO: remove non-curried overloading in v3 /**
  * `union` (Impact: 15.1)
  * `separate` (Impact: 15.0)
    * *Intent:* /**
  * `intersection` (Impact: 14.9)
  * `partition` (Impact: 8.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 200`, `args: 108`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 56`, `planned_debt: 4`, `duplicate_logic: 6`
* *Architecture:* `api: 52`, `import: 13`
* *Defense:* `safety: 1`, `doc: 36`, `immutability_locks: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Predicate, Option, ReadonlySet, Semigroup, Eq, Monoid, Set, Separated...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TaskEither.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.008 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.623 IQR)
- **Top Global Matches:** file_cluster_16: 12.008, file_cluster_2: 12.319, file_cluster_13: 12.466
- **Magnitude:** 24.36 | **LOC:** 1882 | **CtrlFlow:** 2.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.8913%), Tech Debt (71.0701%)
**Top Internal Functions/Classes:**
  * `async` (Impact: 5.5)
  * `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 5.0)
  * `f` (Impact: 4.1)
  * `f` (Impact: 3.7)
    * *Intent:* /** * Less strict version of [`apSecond`](#apsecond). * * The `W` suffix (short for **W**idening) me...
  * `f` (Impact: 3.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 590`, `args: 311`, `func_start: 91`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 5`, `duplicate_logic: 9`
* *Architecture:* `api: 155`, `concurrency: 6`, `import: 32`
* *Defense:* `safety: 49`, `doc: 158`, `immutability_locks: 168`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 18):` Either, function, Functor, Refinement, MonadTask, Chain, Task, Pointed...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/OptionT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.503 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.514 IQR)
- **Top Global Matches:** file_cluster_16: 11.503, file_cluster_8: 12.422, file_cluster_2: 12.459
- **Magnitude:** 23.15 | **LOC:** 696 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (74.9721%)
**Top Internal Functions/Classes:**
  * `fromPredicate` (Impact: 3.2)
  * `fromPredicate` (Impact: 3.2)
  * `fromPredicate` (Impact: 3.2)
    * *Intent:* /** * @category lifting * @since 2.10.0 */
  * `fromPredicate` (Impact: 3.2)
  * `onSome` (Impact: 3.0)
    * *Intent:* // ------------------------------------------------------------------------------------- // deprecat...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 733`, `args: 439`, `func_start: 177`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 8`
* *Architecture:* `api: 152`, `import: 12`
* *Defense:* `safety: 30`, `doc: 45`, `immutability_locks: 39`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.667
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.015075
  * `Imports (Out-Degree: 6):` HKT, Pointed, Option, Predicate, Monad, Functor, Refinement, Either...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/These.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.18%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.556 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.225 IQR)
- **Top Global Matches:** file_cluster_16: 11.556, file_cluster_13: 11.78, file_cluster_17: 12.068
- **Magnitude:** 22.94 | **LOC:** 807 | **CtrlFlow:** 21.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.6319%), Tech Debt (9.7841%)
**Top Internal Functions/Classes:**
  * `traverseReadonlyNonEmptyArrayWithIndex` (Impact: 17.2)
    * *Intent:* /* istanbul ignore next */
  * `getSemigroup` (Impact: 16.7)
    * *Intent:* /** * Less strict version of [`match`](#match). *
  * `getApply` (Impact: 13.9)
    * *Intent:* /** * Alias of [`matchW`](#matchw). * * @category pattern matching * @since 2.10.0 */
  * `getEq` (Impact: 12.6)
  * `matchW` (Impact: 11.8)
    * *Intent:* // ------------------------------------------------------------------------------------- // refineme...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 235`, `args: 127`, `func_start: 66`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 9`, `planned_debt: 2`
* *Architecture:* `api: 69`, `import: 25`
* *Defense:* `safety: 14`, `doc: 60`, `immutability_locks: 62`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.959
  * `Choke Point (Betweenness):` 0.000955 | `Ripple Effect (Closeness):` 0.025844
  * `Imports (Out-Degree: 12):` HKT, Functor, Show, Refinement, Chain, Pointed, These, NonEmptyArray...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/IOEither.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.617 IQR)
- **Local Micro-Species:** `Cluster 4: Heavily Documented Core Classes` (Drift: 6.655 IQR)
- **Top Global Matches:** file_cluster_16: 11.617, file_cluster_2: 11.913, file_cluster_13: 12.073
- **Magnitude:** 19.35 | **LOC:** 1395 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.1927%), Tech Debt (81.2792%)
**Top Internal Functions/Classes:**
  * `traverseReadonlyNonEmptyArrayWithIndexSe` (Impact: 6.6)
  * `f` (Impact: 4.1)
  * `f` (Impact: 3.7)
  * `f` (Impact: 3.7)
  * `getIOValidation` (Impact: 3.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 447`, `args: 231`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 8`, `duplicate_logic: 8`
* *Architecture:* `api: 122`, `import: 26`
* *Defense:* `safety: 25`, `doc: 131`, `immutability_locks: 142`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` Either, function, Functor, Refinement, Chain, Pointed, Alt, NonEmptyArray...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Either.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.171 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.305 IQR)
- **Top Global Matches:** file_cluster_16: 11.171, file_cluster_13: 11.423, file_cluster_2: 11.508
- **Magnitude:** 18.33 | **LOC:** 1854 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (3.6673%), Tech Debt (90.1764%)
**Top Internal Functions/Classes:**
  * `getFilterable` (Impact: 14.7)
  * `getEq` (Impact: 8.9)
  * `getCompactable` (Impact: 7.8)
    * *Intent:* // ------------------------------------------------------------------------------------- // construc...
  * `getApplicativeValidation` (Impact: 6.4)
  * `partition` (Impact: 5.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 238`, `args: 130`, `func_start: 71`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 62`, `import: 30`
* *Defense:* `safety: 11`, `doc: 59`, `immutability_locks: 82`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 20):` HKT, Either, Apply, function, Functor, Show, Refinement, Chain...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ReadonlyMap.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.234 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.663 IQR)
- **Top Global Matches:** file_cluster_16: 11.234, file_cluster_13: 11.384, file_cluster_11: 11.613
- **Magnitude:** 17.68 | **LOC:** 1217 | **CtrlFlow:** 15.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.8128%), Tech Debt (99.9997%)
**Top Internal Functions/Classes:**
  * `lookupWithKey` (Impact: 15.6)
  * `isSubmap` (Impact: 15.0)
  * `elem` (Impact: 12.8)
    * *Intent:* // TODO: remove non-curried overloading in v3 /** * Test whether or not a key exists in a map * * @s...
  * `lookup` (Impact: 10.5)
  * `member` (Impact: 8.5)
    * *Intent:* /**
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 173`, `args: 79`, `func_start: 32`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 29`, `planned_debt: 5`, `duplicate_logic: 10`
* *Architecture:* `api: 33`, `import: 28`
* *Defense:* `safety: 2`, `doc: 23`, `immutability_locks: 64`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` HKT, Functor, Show, Unfoldable, Refinement, FunctorWithIndex, FoldableWithIndex, ReadonlyMap...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TheseT.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.08%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.036 IQR)
- **Local Micro-Species:** `Cluster 5: Declarative Glue & Inert Types` (Drift: 6.415 IQR)
- **Top Global Matches:** file_cluster_16: 11.036, file_cluster_8: 11.919, file_cluster_13: 12.16
- **Magnitude:** 16.65 | **LOC:** 602 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (51.4056%)
**Top Internal Functions/Classes:**
  * `getTheseM` (Impact: 4.2)
  * `mapT` (Impact: 3.4)
    * *Intent:* /** * @category zone of death
  * `chain` (Impact: 2.7)
  * `bimap` (Impact: 2.7)
  * `mapLeft` (Impact: 2.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 565`, `args: 369`, `func_start: 170`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 5`
* *Architecture:* `api: 108`, `import: 9`
* *Defense:* `safety: 30`, `doc: 35`, `immutability_locks: 68`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.696
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.011307
  * `Imports (Out-Degree: 5):` HKT, Pointed, Semigroup, Monad, Functor, Apply, function, Chain...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Tree.ts` (TYPESCRIPT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_16` (Drift: 11.462 IQR)
- **Local Micro-Species:** `Cluster 8: Algorithmic Data Processing` (Drift: 6.434 IQR)
- **Top Global Matches:** file_cluster_16: 11.462, file_cluster_13: 11.869, file_cluster_2: 12.09
- **Magnitude:** 16.55 | **LOC:** 647 | **CtrlFlow:** 4.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.5988%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `draw` (Impact: 9.3)
    * *Intent:* /** * @category instances * @since 2.0.0 */
  * `show` (Impact: 4.7)
  * `getShow` (Impact: 4.5)
    * *Intent:* /** * @category model * @since 2.0.0 */
  * `getEq` (Impact: 4.3)
  * `elem` (Impact: 4.2)
    * *Intent:* /** * @category traversing * @since 2.6.3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 239`, `args: 111`, `func_start: 51`, `class_start: 2`
* *Risk/State:* `state_mutation: 26`
* *Architecture:* `api: 67`, `import: 18`
* *Defense:* `doc: 51`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.4
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` HKT, Functor, Show, Array, Chain, Pointed, Monoid, Eq...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 15.58 | **LOC:** 30 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
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

### `dtslint/tsconfig.json` (JSON | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 4.447 IQR)
- **Top Global Matches:** file_cluster_8: 4.447, file_cluster_7: 6.25, file_cluster_1: 6.315
- **Magnitude:** 14.68 | **LOC:** 10 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.0%), Tech Debt (0.0%)
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
- `src/StateReaderTaskEither.ts` (TYPESCRIPT) | Magnitude: 3.8 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 92, generics: 63, indent_spaces: 43, args: 37
- `src/Random.ts` (TYPESCRIPT) | Magnitude: 1.05 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: structural_boundaries: 16, indent_spaces: 14, func_start: 10, args: 9
- `src/ReaderTaskEither.ts` (TYPESCRIPT) | Magnitude: 4.59 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 136, generics: 110, indent_spaces: 78, args: 56
- `src/Eq.ts` (TYPESCRIPT) | Magnitude: 2.26 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 26, generics: 16, indent_spaces: 12, args: 10

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `scripts/linter.ts` (TYPESCRIPT) | Magnitude: 32.14 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 466, structural_boundaries: 281, immutability_locks: 100, branch: 83
- `src/Ring.ts` (TYPESCRIPT) | Magnitude: 1.32 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 27, args: 15, generics: 15, indent_spaces: 12
- `perf/function/flow.ts` (TYPESCRIPT) | Magnitude: 3.03 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 21, args: 10, state_mutation: 9, structural_boundaries: 7
- `perf/function/pipe.ts` (TYPESCRIPT) | Magnitude: 2.98 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 18, args: 9, state_mutation: 9, structural_boundaries: 6
- `scripts/build.ts` (TYPESCRIPT) | Magnitude: 2.32 | Delta: **0.346 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 69, structural_boundaries: 53, args: 33, comprehensions: 17

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/Record.ts` (TYPESCRIPT) | Magnitude: 1.11 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: sec_high_risk_execution: 75, indent_spaces: 39, ui_framework: 7, generics: 7
- `dtslint/ReaderTask.ts` (TYPESCRIPT) | Magnitude: 5.24 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 17, structural_boundaries: 14, ui_framework: 12, generics: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `perf/ReadonlyNonEmptyArray.ts/reverse.ts` (TYPESCRIPT) | Magnitude: 1.76 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 13, args: 6, state_mutation: 6, concurrency: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `dtslint/NonEmptyArray.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 21, immutability_locks: 15, args: 13, func_start: 8
- `dtslint/ReadonlyNonEmptyArray.ts` (TYPESCRIPT) | Magnitude: 0.76 | Delta: **0.01 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 21, immutability_locks: 15, args: 13, func_start: 8
- `scripts/run.ts` (TYPESCRIPT) | Magnitude: 0.7 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
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

- `src/HKT.ts` -> **Severity: 12325.598** (Blast Radius: 149.621 * Doc Risk: 82.3788%)
- `src/internal.ts` -> **Severity: 3957.03** (Blast Radius: 42.767 * Doc Risk: 92.5253%)
- `src/Refinement.ts` -> **Severity: 2992.496** (Blast Radius: 31.813 * Doc Risk: 94.0652%)
- `src/Chain.ts` -> **Severity: 2882.9** (Blast Radius: 29.333 * Doc Risk: 98.2818%)
- `src/number.ts` -> **Severity: 1189.052** (Blast Radius: 28.985 * Doc Risk: 41.023%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
