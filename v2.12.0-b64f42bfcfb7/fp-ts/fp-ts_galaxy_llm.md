# ARCHITECTURAL_BRIEF: fp-ts
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/gcanti/fp-ts.git` |
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
- **Scope:** 290 analyzed artifact(s), 46868 LOC.
- **Load-bearing artifact:** `src/function.ts` -- 177 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/index.ts` -- pulls in 121 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/pipeable.ts` at magnitude 1022.64 (structural weight, not risk).
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
| Total Artifacts | 431 |
| Analyzed Artifacts (Scanned) | 290 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 141 |
| Total LOC | 46868 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 67.3% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.268 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2678 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 22.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.9822 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 271 | 46735 | 93.4% |
| JSON | 8 | 84 | 2.8% |
| MARKDOWN | 7 | 0 | 2.4% |
| YAML | 2 | 23 | 0.7% |
| HTML | 1 | 26 | 0.3% |
| PLAINTEXT | 1 | 0 | 0.3% |

## 4.1 SOURCE ENCODINGS
All 290 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 31%, Generic / Templated Code Files 29%, Data / Markup / Trivial 15%, Parameter Forwarders Files 12%, Callbacks & Closures Files 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 282 | 97.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 8 | 2.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 141*

**Composition by Extension & Reason:**
- `.md`: 132x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 11222 LOC)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.scss`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 1x Excluded (Explicitly Denied Extension: '.png')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 49.9 | 3.3 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 21.2 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 12.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 11.6 | 2.3 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 37.6 | 21.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 7.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 98.6 | 7.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 29.3 | 0.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.3 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 781 | 215 | 7 | `src/ReadonlyArray.ts` |
| cleanup | 2 | 2 | 0 | `examples/fp-ts-to-the-max-I.ts` |
| guards | 1911 | 164 | 16 | `src/pipeable.ts` |
| danger | 406 | 74 | 4 | `src/Apply.ts` |
| concurrency | 1357 | 48 | 1 | `test/ReaderTaskEither.ts` |
| connectivity | 5565 | 175 | 63 | `src/pipeable.ts` |
| io | 62 | 7 | 0 | `scripts/linter.ts` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 1 | 0 | `scripts/release.ts` |
| time | 40 | 6 | 0 | `test/Date.ts` |
| serialization | 17 | 10 | 0 | `scripts/build.ts` |
| regex | 42 | 25 | 0 | `src/EitherT.ts` |
| events | 66 | 16 | 0 | `dtslint/Option.ts` |
| tests | 2018 | 81 | 21 | `test/ReadonlyArray.ts` |
| docs | 4342 | 126 | 44 | `src/ReaderTaskEither.ts` |
| debt | 500 | 79 | 4 | `src/EitherT.ts` |
| mutation | 4713 | 203 | 49 | `src/ReadonlyArray.ts` |
| dead_code | 11 | 9 | 0 | `dtslint/Apply.ts` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 29 | 9 | 0 | `src/Random.ts` |
| ui | 521 | 29 | 0 | `src/ReaderTaskEither.ts` |

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

1. **function.ts** (`src/function.ts`) — 177 inbound connections
2. **Either.ts** (`src/Either.ts`) — 92 inbound connections
3. **util.ts** (`test/util.ts`) — 78 inbound connections
4. **Option.ts** (`src/Option.ts`) — 74 inbound connections
5. **HKT.ts** (`src/HKT.ts`) — 71 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index.ts** (`src/index.ts`) — 121 outbound dependencies
2. **ReadonlyArray.ts** (`src/ReadonlyArray.ts`) — 39 outbound dependencies
3. **Array.ts** (`src/Array.ts`) — 38 outbound dependencies
4. **ReaderTaskEither.ts** (`src/ReaderTaskEither.ts`) — 35 outbound dependencies
5. **StateReaderTaskEither.ts** (`src/StateReaderTaskEither.ts`) — 34 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `pipe` **(Many-Argument Workhorses)** (@ `src/function.ts`) -> Impact: **68.4** | LOC: 39
- `flow` **(Many-Argument Workhorses)** (@ `src/function.ts`) -> Impact: **62.5** | LOC: 49
- `parseType` **(Compute Cores)** (@ `scripts/linter.ts`) -> Impact: **35.6** | LOC: 89
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **33.9** | LOC: 84
- `getTypeArguments` **(Compute Cores)** (@ `scripts/linter.ts`) -> Impact: **27.3** | LOC: 66
- `lintType` **(Compute Cores)** (@ `scripts/linter.ts`) -> Impact: **26.5** | LOC: 45
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **25.6** | LOC: 31
  * *Intent:* /** */
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **25.6** | LOC: 31
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **25.6** | LOC: 31
- `pipeable` **(Generic / Templated Code)** (@ `src/pipeable.ts`) -> Impact: **25.6** | LOC: 31

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Generic / Templated Code**: generic / type-parameterized (templated) function
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 123 | 15278.66 | 3.03% | 26.19% |
| `test` | 81 | 3629.39 | 5.44% | 0.0% |
| `dtslint` | 44 | 677.41 | 0.5% | 4.43% |
| `scripts` | 6 | 265.4 | 3.78% | 9.44% |
| `__monolith__` | 12 | 180.56 | 0.34% | 0.0% |
| `examples` | 3 | 91.52 | 5.04% | 0.0% |
| `perf/Task` | 3 | 51.08 | 0.0% | 0.0% |
| `perf/function` | 2 | 35.8 | 27.61% | 37.75% |
| `perf/ReaderTask` | 1 | 18.52 | 0.0% | 0.0% |
| `perf/ReaderTaskEither` | 1 | 18.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/Choice.ts` -> **100.0%** Exposure
- `src/EitherT.ts` -> **100.0%** Exposure
- `src/FromReader.ts` -> **100.0%** Exposure
- `src/FromState.ts` -> **100.0%** Exposure
- `src/Strong.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/NonEmptyArray.ts` -> **98.5842%** Exposure
- `src/Set.ts` -> **98.4137%** Exposure
- `perf/function/flow.ts` -> **98.2014%** Exposure
- `perf/function/pipe.ts` -> **98.2014%** Exposure
- `src/Show.ts` -> **98.2014%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/EitherT.ts` -> **0** Orphaned Functions | **52** Duplicates
- `src/OptionT.ts` -> **0** Orphaned Functions | **36** Duplicates
- `src/pipeable.ts` -> **0** Orphaned Functions | **30** Duplicates
- `src/TheseT.ts` -> **0** Orphaned Functions | **28** Duplicates
- `src/StateT.ts` -> **0** Orphaned Functions | **16** Duplicates

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
- **Unknown Dependencies:** `51` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/pipeable.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 10.198)
- **Top Global Matches:** file_cluster_0: 10.198, file_cluster_5: 11.749, file_cluster_12: 14.634
- **Magnitude:** 1022.64 | **LOC:** 2612 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **24**; blast radius 0.977; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (99.3%), Debt Markers (formerly Tech Debt) (85.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (52.7%)
- **Documentation Coverage:** 75.7009% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipeable` **(Generic / Templated Code)** (Impact: 33.9)
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
    * *Intent:* /** */
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
  * `pipeable` **(Generic / Templated Code)** (Impact: 25.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 36 instances
* *State Mutation (weighted view):* 108
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 128`, `structural_boundaries: 2247`, `args: 1162`, `func_start: 224`, `class_start: 108`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 36`, `duplicate_logic: 30`
* *Architecture:* `api: 313`, `import: 24`
* *Defense:* `safety: 16`, `doc: 143`, `immutability_locks: 255`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.977
  * `Choke Point (Betweenness):` 0.000308 | `Ripple Effect (Closeness):` 0.017795
  * `Imports (Out-Degree: 24):` Alt, Apply, Bifunctor, Chain, Compactable, Contravariant, Either, Extend...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ReadonlyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.952)
- **Top Global Matches:** file_cluster_0: 6.952, file_cluster_5: 11.26, file_cluster_10: 12.038
- **Magnitude:** 885.9 | **LOC:** 2665 | **CtrlFlow:** 11.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **46** in-repo importer(s); it depends on **39**; blast radius 5.103; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (94.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.1%)
- **Documentation Coverage:** 11.1864% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `union` **(Generic / Templated Code)** (Impact: 11.3)
  * `elem` **(Generic / Templated Code)** (Impact: 9.9)
  * `takeLeftWhile` **(Generic / Templated Code)** (Impact: 8.0)
  * `unfold` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* /** */
  * `chainRecDepthFirst` **(Generic / Templated Code)** (Impact: 7.4)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 50 instances
* *State Mutation (weighted view):* 151
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 127`, `structural_boundaries: 777`, `args: 382`, `func_start: 161`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 51`, `planned_debt: 15`, `duplicate_logic: 2`
* *Architecture:* `api: 202`, `import: 39`
* *Defense:* `safety: 4`, `doc: 170`, `immutability_locks: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.103
  * `Choke Point (Betweenness):` 0.012091 | `Ripple Effect (Closeness):` 0.16277
  * `Imports (Out-Degree: 39):` Alt, Alternative, Applicative, Apply, Chain, ChainRec, Compactable, Either...
  * `Imported By (In-Degree: 46):` (Excluded from Brief to save tokens)

### `src/Array.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.499)
- **Top Global Matches:** file_cluster_0: 7.499, file_cluster_5: 10.487, file_cluster_10: 12.582
- **Magnitude:** 718.14 | **LOC:** 3021 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **38**; blast radius 1.511; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (99.6%), Mutation Surface (formerly State Flux) (88.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.2%)
- **Documentation Coverage:** 14.1631% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `union` **(Generic / Templated Code)** (Impact: 11.4)
  * `unfold` **(Generic / Templated Code)** (Impact: 7.7)
    * *Intent:* * import { unfold } from 'fp-ts/Array' * import { option } from 'fp-ts' * * const f = (n: number) =>...
  * `intersection` **(Generic / Templated Code)** (Impact: 7.0)
  * `splitAt` **(Generic / Templated Code)** (Impact: 6.9)
    * *Intent:* /** * Splits an `Array` into two pieces, the first piece has max `n` elements. * * import { splitAt ...
  * `dropLeft` **(Generic / Templated Code)** (Impact: 6.7)
    * *Intent:* * Creates a new `Array` which is a copy of the input dropping a max number of elements from the star...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 103
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 715`, `args: 351`, `func_start: 130`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 35`, `planned_debt: 6`, `duplicate_logic: 2`
* *Architecture:* `api: 194`, `import: 38`
* *Defense:* `safety: 3`, `doc: 167`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.511
  * `Choke Point (Betweenness):` 0.002449 | `Ripple Effect (Closeness):` 0.044291
  * `Imports (Out-Degree: 38):` Alt, Alternative, Applicative, Apply, Chain, ChainRec, Compactable, Either...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/ReadonlyRecord.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.588)
- **Top Global Matches:** file_cluster_0: 6.588, file_cluster_5: 11.05, file_cluster_10: 11.275
- **Magnitude:** 646.24 | **LOC:** 2297 | **CtrlFlow:** 8.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **27**; blast radius 21.363; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (62.4%), Guard Balance (formerly Safety Score) (53.0%)
- **Documentation Coverage:** 22.1854% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isSubrecord` **(Compute Cores)** (Impact: 11.7)
  * `concat` **(Compute Cores)** (Impact: 11.1)
  * `elem` **(Compute Cores)** (Impact: 10.3)
  * `getMonoid` **(Generic / Templated Code)** (Impact: 9.5)
  * `separate` **(Generic / Templated Code)** (Impact: 7.9)
    * *Intent:* * { * right: { * a: "foo", * c: "baz", * }, * left: { * b: "bar", * }, * } * ); * */...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 780`, `args: 382`, `func_start: 147`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 31`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 166`, `import: 27`
* *Defense:* `safety: 3`, `doc: 107`, `immutability_locks: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 21.363
  * `Choke Point (Betweenness):` 0.022432 | `Ripple Effect (Closeness):` 0.35045
  * `Imports (Out-Degree: 27):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/ReadonlyNonEmptyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.823)
- **Top Global Matches:** file_cluster_0: 6.823, file_cluster_5: 10.735, file_cluster_10: 11.943
- **Magnitude:** 504.6 | **LOC:** 1498 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **53** in-repo importer(s); it depends on **27**; blast radius 12.834; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (96.8%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.1%)
- **Documentation Coverage:** 11.1111% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `group` **(Generic / Templated Code)** (Impact: 9.0)
  * `uniq` **(Generic / Templated Code)** (Impact: 8.4)
    * *Intent:* /** * Remove duplicates from a `ReadonlyNonEmptyArray`, keeping the first occurrence of an element. ...
  * `rotate` **(Generic / Templated Code)** (Impact: 8.4)
    * *Intent:* /** * Rotate a `ReadonlyNonEmptyArray` by `n` steps. * * import { rotate } from 'fp-ts/ReadonlyNonEm...
  * `insertAt` **(Generic / Templated Code)** (Impact: 6.9)
    * *Intent:* /** * Use [`insertAt`](./ReadonlyArray.ts.html#insertat) instead. * */
  * `unsafeUpdateAt` **(Generic / Templated Code)** (Impact: 6.5)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 33 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 444`, `args: 205`, `func_start: 96`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `api: 128`, `import: 27`
* *Defense:* `safety: 1`, `doc: 116`, `immutability_locks: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.834
  * `Choke Point (Betweenness):` 0.019048 | `Ripple Effect (Closeness):` 0.40124
  * `Imports (Out-Degree: 27):` Alt, Applicative, Apply, Chain, Comonad, Endomorphism, Eq, Extend...
  * `Imported By (In-Degree: 53):` (Excluded from Brief to save tokens)

### `src/ReadonlyMap.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.993)
- **Top Global Matches:** file_cluster_0: 7.993, file_cluster_5: 8.512, file_cluster_12: 11.153
- **Magnitude:** 496.18 | **LOC:** 1217 | **CtrlFlow:** 9.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **26**; blast radius 0.983; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (83.3%), Connectivity (formerly Api Exposure) (82.4%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (64.8%)
- **Documentation Coverage:** 23.3533% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `union` **(Generic / Templated Code)** (Impact: 15.6)
    * *Intent:* // ------------------------------------------------------------------------------------- // utils //...
  * `isSubmap` **(Generic / Templated Code)** (Impact: 15.2)
  * `getMonoid` **(Generic / Templated Code)** (Impact: 11.7)
    * *Intent:* /** * Gets `Monoid` instance for Maps given `Semigroup` instance for their values * */
  * `concat` **(Compute Cores)** (Impact: 11.4)
  * `difference` **(Generic / Templated Code)** (Impact: 11.4)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 100
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 76`, `structural_boundaries: 480`, `args: 226`, `func_start: 97`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 36`, `planned_debt: 5`, `duplicate_logic: 6`
* *Architecture:* `api: 83`, `import: 28`
* *Defense:* `safety: 2`, `doc: 66`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.983
  * `Choke Point (Betweenness):` 0.000331 | `Ripple Effect (Closeness):` 0.016955
  * `Imports (Out-Degree: 26):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/EitherT.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.057)
- **Top Global Matches:** file_cluster_0: 8.057, file_cluster_5: 13.116, file_cluster_13: 13.873
- **Magnitude:** 495.26 | **LOC:** 949 | **CtrlFlow:** 0.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 1.197; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (2.4%)
- **Documentation Coverage:** 68.6275% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getEitherM` **(Generic / Templated Code)** (Impact: 2.8)
    * *Intent:* /* istanbul ignore next */
  * `altValidation` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* /** */
  * `altValidation` **(Generic / Templated Code)** (Impact: 2.0)
  * `altValidation` **(Generic / Templated Code)** (Impact: 2.0)
  * `bimap` **(Parameter Forwarders)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 935`, `args: 556`, `func_start: 183`, `class_start: 4`
* *Risk/State:* `duplicate_logic: 52`
* *Architecture:* `api: 180`, `import: 10`
* *Defense:* `doc: 49`, `immutability_locks: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.197
  * `Choke Point (Betweenness):` 0.0001 | `Ripple Effect (Closeness):` 0.074437
  * `Imports (Out-Degree: 10):` Applicative, Apply, Chain, Either, Functor, HKT, Monad, Pointed...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/NonEmptyArray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.956)
- **Top Global Matches:** file_cluster_0: 6.956, file_cluster_5: 10.771, file_cluster_10: 12.097
- **Magnitude:** 466.08 | **LOC:** 1408 | **CtrlFlow:** 7.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **26**; blast radius 7.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (98.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.4%)
- **Documentation Coverage:** 7.7922% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `group` **(Generic / Templated Code)** (Impact: 9.0)
  * `rotate` **(Generic / Templated Code)** (Impact: 8.8)
    * *Intent:* /** * Rotate a `NonEmptyArray` by `n` steps. * * import { rotate } from 'fp-ts/NonEmptyArray' * * as...
  * `uniq` **(Generic / Templated Code)** (Impact: 8.4)
    * *Intent:* /** * Remove duplicates from a `NonEmptyArray`, keeping the first occurrence of an element. * * impo...
  * `insertAt` **(Generic / Templated Code)** (Impact: 5.6)
    * *Intent:* /** */
  * `zip` **(Generic / Templated Code)** (Impact: 5.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 31 instances
* *State Mutation (weighted view):* 95
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 433`, `args: 204`, `func_start: 84`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 33`
* *Architecture:* `api: 127`, `import: 26`
* *Defense:* `safety: 1`, `doc: 116`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.5
  * `Choke Point (Betweenness):` 0.006527 | `Ripple Effect (Closeness):` 0.369757
  * `Imports (Out-Degree: 26):` Alt, Applicative, Apply, Chain, Comonad, Endomorphism, Eq, Extend...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `test/ReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.338)
- **Top Global Matches:** file_cluster_10: 6.338, file_cluster_15: 8.886, file_cluster_11: 9.866
- **Magnitude:** 423.56 | **LOC:** 841 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **19**; blast radius 0.769; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.8%), Guard Balance (formerly Safety Score) (42.8%), Connectivity (formerly Api Exposure) (25.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f` **(Parameter Forwarders)** (Impact: 3.2)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 2.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Concurrency (weighted view):* 345
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 449`, `args: 225`, `func_start: 134`
* *Risk/State:* `state_mutation: 12`, `duplicate_logic: 4`
* *Architecture:* `api: 3`, `concurrency: 285`, `import: 19`
* *Defense:* `safety: 1`, `test: 116`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.769
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` Apply, Either, IO, IOEither, Option, Reader, ReaderEither, ReaderIO...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/OptionT.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.503)
- **Top Global Matches:** file_cluster_0: 8.503, file_cluster_5: 13.312, file_cluster_10: 13.943
- **Magnitude:** 408.12 | **LOC:** 696 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 1.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 71.7172% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getOptionM` **(Generic / Templated Code)** (Impact: 2.5)
  * `fold` **(Parameter Forwarders)** (Impact: 2.0)
  * `fromPredicate` **(Generic / Templated Code)** (Impact: 1.9)
  * `fromPredicate` **(Generic / Templated Code)** (Impact: 1.8)
    * *Intent:* /** */
  * `fromPredicate` **(Generic / Templated Code)** (Impact: 1.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 763`, `args: 439`, `func_start: 152`, `class_start: 5`
* *Risk/State:* `duplicate_logic: 36`
* *Architecture:* `api: 152`, `import: 12`
* *Defense:* `doc: 33`, `immutability_locks: 24`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.023
  * `Choke Point (Betweenness):` 0.00011 | `Ripple Effect (Closeness):` 0.044944
  * `Imports (Out-Degree: 12):` Applicative, Apply, Chain, Either, Functor, HKT, Monad, Option...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `test/TaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 5.56)
- **Top Global Matches:** file_cluster_10: 5.56, file_cluster_15: 8.948, file_cluster_13: 9.614
- **Magnitude:** 400.42 | **LOC:** 920 | **CtrlFlow:** 3.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **17**; blast radius 0.769; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.6%), Guard Balance (formerly Safety Score) (44.0%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `api1` **(Callbacks & Closures)** (Impact: 3.6)
  * `api2` **(Callbacks & Closures)** (Impact: 3.6)
  * `api3` **(Callbacks & Closures)** (Impact: 3.6)
  * `f` **(Parameter Forwarders)** (Impact: 3.2)
  * `api` **(Callbacks & Closures)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 12 instances
* *Concurrency (weighted view):* 330
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 438`, `args: 218`, `func_start: 113`
* *Risk/State:* `state_mutation: 12`, `planned_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 1`, `concurrency: 270`, `import: 17`
* *Defense:* `safety: 1`, `test: 103`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.769
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Apply, Either, IO, IOEither, Monoid, Option, ReadonlyArray, ReadonlyNonEmptyArray...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/function.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 7.689)
- **Top Global Matches:** file_cluster_5: 7.689, file_cluster_12: 9.832, file_cluster_0: 10.462
- **Magnitude:** 368.28 | **LOC:** 806 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **177** in-repo importer(s); it depends on **5**; blast radius 119.846; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.6%), Mutation Surface (formerly State Flux) (13.6%)
- **Documentation Coverage:** 50.8197% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pipe` **(Many-Argument Workhorses)** (Impact: 68.4)
  * `flow` **(Many-Argument Workhorses)** (Impact: 62.5)
  * `pipe` **(Many-Argument Workhorses)** (Impact: 5.7)
  * `pipe` **(Many-Argument Workhorses)** (Impact: 5.6)
  * `pipe` **(Many-Argument Workhorses)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 479`, `args: 117`, `func_start: 58`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 17`, `state_mutation: 3`
* *Architecture:* `api: 69`, `import: 6`
* *Defense:* `safety: 1`, `doc: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 119.846
  * `Choke Point (Betweenness):` 0.046434 | `Ripple Effect (Closeness):` 0.653346
  * `Imports (Out-Degree: 5):` BooleanAlgebra, Monoid, Ring, Semigroup, Semiring
  * `Imported By (In-Degree: 177):` (Excluded from Brief to save tokens)

### `src/Record.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.902)
- **Top Global Matches:** file_cluster_0: 6.902, file_cluster_5: 11.024, file_cluster_10: 12.515
- **Magnitude:** 354.44 | **LOC:** 1805 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **29**; blast radius 0.895; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.2%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (51.2%), Guard Balance (formerly Safety Score) (49.8%)
- **Documentation Coverage:** 32.2404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `_traverseWithIndex` **(Generic / Templated Code)** (Impact: 7.4)
  * `pop` **(Generic / Templated Code)** (Impact: 6.5)
  * `collect` **(Generic / Templated Code)** (Impact: 5.1)
  * `union` **(Generic / Templated Code)** (Impact: 4.9)
    * *Intent:* * It uses the `concat` function of the provided `Magma` to * combine the elements with the same key....
  * `keys_` **(Generic / Templated Code)** (Impact: 3.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 575`, `args: 273`, `func_start: 94`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 5`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 131`, `import: 29`
* *Defense:* `safety: 2`, `doc: 86`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.895
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.011073
  * `Imports (Out-Degree: 29):` Applicative, Array, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Either.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.354)
- **Top Global Matches:** file_cluster_5: 8.354, file_cluster_0: 8.538, file_cluster_12: 11.613
- **Magnitude:** 347.76 | **LOC:** 1854 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **92** in-repo importer(s); it depends on **30**; blast radius 17.602; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.3%), Mutation Surface (formerly State Flux) (8.8%)
- **Documentation Coverage:** 16.5049% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `equals` **(Compute Cores)** (Impact: 8.8)
  * `extend` **(Generic / Templated Code)** (Impact: 8.6)
    * *Intent:* /** */
  * `elem` **(Generic / Templated Code)** (Impact: 8.3)
  * `ap` **(Compute Cores)** (Impact: 7.3)
  * `_chainRec` **(Generic / Templated Code)** (Impact: 6.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 486`, `args: 198`, `func_start: 62`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 2`
* *Architecture:* `api: 117`, `import: 32`
* *Defense:* `safety: 6`, `doc: 119`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.602
  * `Choke Point (Betweenness):` 0.024079 | `Ripple Effect (Closeness):` 0.403432
  * `Imports (Out-Degree: 30):` Alt, Applicative, Apply, Bifunctor, Chain, ChainRec, Compactable, Eq...
  * `Imported By (In-Degree: 92):` (Excluded from Brief to save tokens)

### `src/Map.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.158)
- **Top Global Matches:** file_cluster_0: 8.158, file_cluster_5: 8.867, file_cluster_12: 11.8
- **Magnitude:** 336.26 | **LOC:** 925 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **25**; blast radius 0.953; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (96.7%), Mutation Surface (formerly State Flux) (91.0%), Connectivity (formerly Api Exposure) (80.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 22.4138% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getMonoid` **(Generic / Templated Code)** (Impact: 11.7)
    * *Intent:* /** * Gets `Monoid` instance for Maps given `Semigroup` instance for their values * */
  * `concat` **(Compute Cores)** (Impact: 11.4)
  * `lookupWithKey` **(Generic / Templated Code)** (Impact: 10.4)
  * `upsertAt` **(Generic / Templated Code)** (Impact: 6.6)
    * *Intent:* /** * Insert or replace a key/value pair in a `Map`. * */
  * `separate` **(Generic / Templated Code)** (Impact: 6.4)
    * *Intent:* /** */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 22 instances
* *State Mutation (weighted view):* 68
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 399`, `args: 193`, `func_start: 68`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 5`, `duplicate_logic: 8`
* *Architecture:* `api: 74`, `import: 27`
* *Defense:* `safety: 2`, `doc: 62`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.953
  * `Choke Point (Betweenness):` 0.000327 | `Ripple Effect (Closeness):` 0.011073
  * `Imports (Out-Degree: 25):` Applicative, Compactable, Either, Eq, Filterable, FilterableWithIndex, Foldable, FoldableWithIndex...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Apply.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 10.141)
- **Top Global Matches:** file_cluster_5: 10.141, file_cluster_7: 14.482, file_cluster_12: 15.196
- **Magnitude:** 331.76 | **LOC:** 714 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **5**; blast radius 14.587; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Debt Markers (formerly Tech Debt) (87.9%), Guard Balance (formerly Safety Score) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 89.5288% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getRecordConstructor` **(Compute Cores)** (Impact: 14.6)
  * `curried` **(Callbacks & Closures)** (Impact: 6.5)
  * `getTupleConstructor` **(Compute Cores)** (Impact: 3.9)
  * `sequenceT` **(Generic / Templated Code)** (Impact: 3.4)
  * `ap` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* // ------------------------------------------------------------------------------------- // combinat...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 36`, `structural_boundaries: 598`, `args: 317`, `func_start: 96`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 9`, `duplicate_logic: 10`
* *Architecture:* `api: 100`, `import: 5`
* *Defense:* `doc: 15`, `immutability_locks: 22`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 14.587
  * `Choke Point (Betweenness):` 0.003255 | `Ripple Effect (Closeness):` 0.394803
  * `Imports (Out-Degree: 5):` Functor, HKT, Semigroup, function, internal
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `src/Option.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.019)
- **Top Global Matches:** file_cluster_0: 7.019, file_cluster_5: 11.971, file_cluster_10: 12.42
- **Magnitude:** 325.68 | **LOC:** 1527 | **CtrlFlow:** 9.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **74** in-repo importer(s); it depends on **31**; blast radius 14.449; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.3%), Mutation Surface (formerly State Flux) (11.1%)
- **Documentation Coverage:** 8.6538% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `elem` **(Generic / Templated Code)** (Impact: 9.2)
  * `compare` **(Compute Cores)** (Impact: 8.7)
  * `ap` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* /** */
  * `reduceRight` **(Generic / Templated Code)** (Impact: 8.7)
    * *Intent:* /** */
  * `getOrElseW` **(Generic / Templated Code)** (Impact: 8.1)
    * *Intent:* /** * Less strict version of [`getOrElse`](#getorelse). * * The `W` suffix (short for **W**idening) ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 41`, `structural_boundaries: 382`, `args: 169`, `func_start: 58`, `class_start: 3`
* *Risk/State:* `state_mutation: 2`
* *Architecture:* `api: 112`, `import: 31`
* *Defense:* `safety: 5`, `doc: 106`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.449
  * `Choke Point (Betweenness):` 0.019239 | `Ripple Effect (Closeness):` 0.3941
  * `Imports (Out-Degree: 31):` Alt, Alternative, Applicative, Apply, Chain, Compactable, Either, Eq...
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `src/TheseT.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.49)
- **Top Global Matches:** file_cluster_0: 8.49, file_cluster_5: 12.001, file_cluster_13: 14.217
- **Magnitude:** 303.18 | **LOC:** 602 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 0.811; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (89.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%)
- **Documentation Coverage:** 66.0377% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getTheseM` **(Generic / Templated Code)** (Impact: 3.6)
    * *Intent:* /* istanbul ignore next */
  * `toTuple` **(Callbacks & Closures)** (Impact: 2.4)
  * `fold` **(Parameter Forwarders)** (Impact: 2.3)
  * `ap` **(Generic / Templated Code)** (Impact: 2.0)
    * *Intent:* /** */
  * `ap` **(Generic / Templated Code)** (Impact: 2.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 595`, `args: 335`, `func_start: 110`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `duplicate_logic: 28`
* *Architecture:* `api: 108`, `import: 9`
* *Defense:* `doc: 25`, `immutability_locks: 58`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.811
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.010813
  * `Imports (Out-Degree: 9):` Apply, Chain, Functor, HKT, Monad, Pointed, Semigroup, These...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/These.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.727)
- **Top Global Matches:** file_cluster_0: 7.727, file_cluster_5: 8.218, file_cluster_12: 11.121
- **Magnitude:** 275.28 | **LOC:** 807 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **25**; blast radius 1.327; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (85.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Mutation Surface (formerly State Flux) (19.8%)
- **Documentation Coverage:** 8.75% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSemigroup` **(Generic / Templated Code)** (Impact: 16.7)
    * *Intent:* /** */
  * `concat` **(Compute Cores)** (Impact: 16.5)
  * `ap` **(Compute Cores)** (Impact: 16.5)
  * `getEq` **(Generic / Templated Code)** (Impact: 12.6)
    * *Intent:* /** */
  * `matchW` **(Generic / Templated Code)** (Impact: 11.3)
    * *Intent:* /** * Less strict version of [`match`](#match). * * The `W` suffix (short for **W**idening) means th...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 12
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 246`, `args: 104`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 4`, `planned_debt: 2`
* *Architecture:* `api: 57`, `import: 25`
* *Defense:* `safety: 3`, `doc: 58`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.327
  * `Choke Point (Betweenness):` 0.001307 | `Ripple Effect (Closeness):` 0.02548
  * `Imports (Out-Degree: 25):` Applicative, Apply, Bifunctor, Chain, Either, Eq, Foldable, FromEither...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/ReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.857)
- **Top Global Matches:** file_cluster_0: 8.857, file_cluster_5: 8.877, file_cluster_12: 12.238
- **Magnitude:** 271.46 | **LOC:** 2292 | **CtrlFlow:** 0.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **35**; blast radius 1.852; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.6%), Concurrency Surface (formerly Concurrency) (12.8%)
- **Documentation Coverage:** 17.3077% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `traverseReadonlyArrayWithIndex` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverseWithIndex(ApplicativePar)`. * */
  * `traverseReadonlyArrayWithIndexSeq` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverseWithIndex(ApplicativeSeq)`. * */
  * `bracketW` **(Generic / Templated Code)** (Impact: 2.6)
    * *Intent:* /** * Less strict version of [`bracket`](#bracket). * */
  * `getFilterable` **(Generic / Templated Code)** (Impact: 2.4)
    * *Intent:* /** */
  * `bracket` **(Generic / Templated Code)** (Impact: 2.4)
    * *Intent:* // ------------------------------------------------------------------------------------- // utils //...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 784`, `args: 320`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 17`
* *Architecture:* `api: 188`, `concurrency: 1`, `import: 35`
* *Defense:* `doc: 195`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.852
  * `Choke Point (Betweenness):` 0.00258 | `Ripple Effect (Closeness):` 0.042388
  * `Imports (Out-Degree: 35):` Alt, Applicative, Apply, Bifunctor, Chain, Compactable, Either, EitherT...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `test/StateReaderTaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.275)
- **Top Global Matches:** file_cluster_10: 6.275, file_cluster_15: 8.51, file_cluster_11: 9.605
- **Magnitude:** 266.92 | **LOC:** 652 | **CtrlFlow:** 0.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **18**; blast radius 0.769; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (48.6%), Guard Balance (formerly Safety Score) (44.0%), Connectivity (formerly Api Exposure) (19.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `f` **(Parameter Forwarders)** (Impact: 3.0)
  * `left` **(Callbacks & Closures)** (Impact: 2.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Concurrency (weighted view):* 217
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`, `structural_boundaries: 304`, `args: 149`, `func_start: 86`, `class_start: 1`
* *Risk/State:* `state_mutation: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 2`, `concurrency: 172`, `import: 18`
* *Defense:* `safety: 1`, `test: 75`, `immutability_locks: 9`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.769
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 17):` Array, Either, IO, IOEither, Option, Reader, ReaderEither, ReaderTaskEither...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TaskEither.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.378)
- **Top Global Matches:** file_cluster_5: 8.378, file_cluster_0: 9.356, file_cluster_12: 12.193
- **Magnitude:** 263.64 | **LOC:** 1882 | **CtrlFlow:** 2.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **31**; blast radius 4.112; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.2%), Concurrency Surface (formerly Concurrency) (21.4%)
- **Documentation Coverage:** 28.169% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cbResolver` **(Parameter Forwarders)** (Impact: 3.6)
  * `traverseReadonlyArrayWithIndex` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverseWithIndex(ApplicativePar)`. * */
  * `traverseReadonlyArrayWithIndexSeq` **(Generic / Templated Code)** (Impact: 3.1)
    * *Intent:* /** * Equivalent to `ReadonlyArray#traverseWithIndex(ApplicativeSeq)`. * */
  * `taskify` **(Generic / Templated Code)** (Impact: 3.0)
  * `taskify` **(Generic / Templated Code)** (Impact: 3.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 13`, `structural_boundaries: 637`, `args: 256`, `func_start: 41`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 1`
* *Architecture:* `api: 153`, `concurrency: 6`, `import: 32`
* *Defense:* `safety: 2`, `doc: 152`, `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.112
  * `Choke Point (Betweenness):` 0.005894 | `Ripple Effect (Closeness):` 0.084167
  * `Imports (Out-Degree: 31):` Alt, Applicative, Apply, Bifunctor, Chain, Compactable, Either, EitherT...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/ReadonlySet.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 6.709)
- **Top Global Matches:** file_cluster_0: 6.709, file_cluster_10: 11.589, file_cluster_5: 11.89
- **Magnitude:** 261.0 | **LOC:** 605 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **12**; blast radius 1.074; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Connectivity (formerly Api Exposure) (81.9%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (62.2%)
- **Documentation Coverage:** 4.1667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `union` **(Generic / Templated Code)** (Impact: 11.5)
  * `intersection` **(Generic / Templated Code)** (Impact: 11.2)
  * `elem` **(Generic / Templated Code)** (Impact: 9.6)
  * `isSubset` **(Generic / Templated Code)** (Impact: 6.7)
  * `difference` **(Generic / Templated Code)** (Impact: 6.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 17 instances
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 51`, `structural_boundaries: 245`, `args: 139`, `func_start: 48`, `class_start: 1`
* *Risk/State:* `state_mutation: 21`, `planned_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 52`, `import: 12`
* *Defense:* `doc: 39`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.074
  * `Choke Point (Betweenness):` 0.000107 | `Ripple Effect (Closeness):` 0.016955
  * `Imports (Out-Degree: 12):` Either, Eq, Magma, Monoid, Option, Ord, Predicate, Refinement...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `test/TaskOption.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Centroid distance: 6.749)
- **Top Global Matches:** file_cluster_10: 6.749, file_cluster_15: 9.442, file_cluster_11: 10.257
- **Magnitude:** 253.42 | **LOC:** 429 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 0.769; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (49.9%), Guard Balance (formerly Safety Score) (45.3%), Connectivity (formerly Api Exposure) (13.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `f` **(Parameter Forwarders)** (Impact: 3.1)
  * `f` **(Parameter Forwarders)** (Impact: 3.1)
  * `f` **(Parameter Forwarders)** (Impact: 3.1)
  * `f` **(Parameter Forwarders)** (Impact: 3.1)
  * `none` **(Callbacks & Closures)** (Impact: 2.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 10 instances
* *Concurrency (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 231`, `args: 110`, `func_start: 60`
* *Risk/State:* `state_mutation: 10`, `duplicate_logic: 6`
* *Architecture:* `api: 1`, `concurrency: 149`, `import: 10`
* *Defense:* `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.769
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` Either, IO, Option, ReadonlyArray, ReadonlyNonEmptyArray, Task, TaskEither, TaskOption...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `scripts/linter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.059)
- **Top Global Matches:** file_cluster_4: 9.059, file_cluster_6: 11.635, file_cluster_0: 12.918
- **Magnitude:** 213.24 | **LOC:** 653 | **CtrlFlow:** 12.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 0.769; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.5%), Connectivity (formerly Api Exposure) (11.7%), Complexity Load (formerly Cognitive Load) (9.2%), Dead Code Surface (formerly Dead Code) (5.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseType` **(Compute Cores)** (Impact: 35.6)
  * `getTypeArguments` **(Compute Cores)** (Impact: 27.3)
  * `lintType` **(Compute Cores)** (Impact: 26.5)
  * `parseVariableDeclaration` **(Compute Cores)** (Impact: 17.7)
  * `parseInterface` **(Callbacks & Closures)** (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 73`, `structural_boundaries: 281`, `args: 53`, `func_start: 20`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 2`, `dead_code: 1`
* *Architecture:* `io: 22`, `api: 43`, `import: 8`
* *Defense:* `immutability_locks: 51`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.769
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` Monoid, Option, ReadonlyArray, function, string, glob, path, ts-morph
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/ReaderTaskEither.ts` (TYPESCRIPT) | Magnitude: 271.46 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: generics: 857, structural_boundaries: 784, indent_spaces: 495, args: 320
- `test/struct.ts` (TYPESCRIPT) | Magnitude: 7.72 | Delta: **0.094** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 11, args: 7, func_start: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `dtslint/ReadonlyRecord.ts` (TYPESCRIPT) | Magnitude: 7.18 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: structural_boundaries: 68, args: 46, indent_spaces: 25, comprehensions: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `test/FunctorWithIndex.ts` (TYPESCRIPT) | Magnitude: 4.12 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 21, structural_boundaries: 7, args: 4, import: 3
- `test/ReadonlyMap.ts` (TYPESCRIPT) | Magnitude: 64.36 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 1091, core_var_decl: 166, structural_boundaries: 123, design_snake_case: 113

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `dtslint/constrained.ts` (TYPESCRIPT) | Magnitude: 68.6 | Delta: **0.118** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 132, api: 52, core_var_decl: 52, import: 28
- `src/index.ts` (TYPESCRIPT) | Magnitude: 20.88 | Delta: **0.169** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 124, doc: 122, import: 121, indent_spaces: 121

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `dtslint/pipeable.ts` (TYPESCRIPT) | Magnitude: 16.28 | Delta: **0.07** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 14, import: 13, explicit_casts: 12, comprehensions: 8
- `test/Apply.ts` (TYPESCRIPT) | Magnitude: 17.08 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 96, comprehensions: 59, structural_boundaries: 13, args: 7

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/ReadonlyNonEmptyArray.ts` -> **Severity: 1.843** (Bridge: 0.019 * Flux: 96.7557%)
- `src/ReadonlyRecord.ts` -> **Severity: 1.399** (Bridge: 0.0224 * Flux: 62.3757%)
- `src/ReadonlyArray.ts` -> **Severity: 1.139** (Bridge: 0.0121 * Flux: 94.1685%)
- `src/Monoid.ts` -> **Severity: 0.65** (Bridge: 0.0216 * Flux: 30.1207%)
- `src/NonEmptyArray.ts` -> **Severity: 0.643** (Bridge: 0.0065 * Flux: 98.5842%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/HKT.ts` -> **Severity: 38.156** (Embedded: 0.477 * Error Risk: 80.0%)
- `src/function.ts` -> **Severity: 35.672** (Embedded: 0.6533 * Error Risk: 54.5994%)
- `src/Monoid.ts` -> **Severity: 32.989** (Embedded: 0.4784 * Error Risk: 68.961%)
- `src/Apply.ts` -> **Severity: 31.584** (Embedded: 0.3948 * Error Risk: 80.0%)
- `src/Ring.ts` -> **Severity: 30.869** (Embedded: 0.3859 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/function.ts` -> **Severity: 6090.538** (Blast Radius: 119.846 * Doc Risk: 50.8197%)
- `src/Apply.ts` -> **Severity: 1305.957** (Blast Radius: 14.587 * Doc Risk: 89.5288%)
- `test/util.ts` -> **Severity: 1108.4** (Blast Radius: 11.084 * Doc Risk: 100.0%)
- `src/Functor.ts` -> **Severity: 776.768** (Blast Radius: 18.245 * Doc Risk: 42.5743%)
- `src/BooleanAlgebra.ts` -> **Severity: 725.933** (Blast Radius: 21.778 * Doc Risk: 33.3333%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4901 call pairs -- scoped 53.5%, unique 0.0%, ambiguous 9.6%, external 36.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 4896 | 53.5% | 0.0% | 9.6% | 36.8% |
| html | 5 | 20.0% | 0.0% | 0.0% | 80.0% |

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
