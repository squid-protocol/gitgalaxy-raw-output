# ARCHITECTURAL_BRIEF: TypeScript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/microsoft/TypeScript.git` |
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
- **Scope:** 50418 analyzed artifact(s), 2447247 LOC.
- **Load-bearing artifact:** `src/compiler/core.ts` -- 213 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/testRunner/tests.ts` -- pulls in 233 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/compiler/checker.ts` at magnitude 59546.04 (structural weight, not risk).
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
| Total Artifacts | 81366 |
| Analyzed Artifacts (Scanned) | 50418 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 30948 |
| Total LOC | 2447247 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 62.0% |
| Dominant Lang | JAVASCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.5515 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2718 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.9329 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 107 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 20382 | 645147 | 40.4% |
| JAVASCRIPT | 17597 | 1663850 | 34.9% |
| PLAINTEXT | 9953 | 11 | 19.7% |
| JSON | 2423 | 136337 | 4.8% |
| MARKDOWN | 32 | 0 | 0.1% |
| YAML | 29 | 1896 | 0.1% |
| SHELL | 2 | 6 | 0.0% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 49476 |
| utf-8 | bom | 937 |
| utf-16-le | bom | 5 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 52%, Declarative / Non-Code 21%, State Mutators Files 10%, Interface Declarations Files 6%, Callbacks & Closures Files 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 40433 | 80.2% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 9984 | 19.8% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.0% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 30948*

**Composition by Extension & Reason:**
- `.symbols`: 14016x Excluded (Unsupported Extension: '.symbols')
- `.types`: 14016x Excluded (Unsupported Extension: '.types')
- `.map`: 665x Unresolved Ambiguity (No Retainable Structure), 105x Excluded (Saturation: Line 3 exceeds 500 chars), 85x Excluded (Saturation: Line 2 exceeds 500 chars)
- `.ts`: 476x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 225x Excluded: Neighborhood Micro-Mass Limit Exceeded, 5x Excluded (Saturation: Line 6 exceeds 500 chars)
- `.js`: 85x Excluded (Saturation: Line 94 exceeds 500 chars), 79x Excluded (Saturation: Line 95 exceeds 500 chars), 78x Excluded (Saturation: Line 89 exceeds 500 chars)
- `.baseline`: 459x Excluded (Unsupported Extension: '.baseline')
- `.md`: 72x Excluded (Lexical Monotony: High structural repetition detected in 2354 LOC), 4x Excluded (Lexical Monotony: High structural repetition detected in 2216 LOC)
- `.txt`: 2x Excluded (Lexical Monotony: High structural repetition detected in 3072 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 2255 LOC), 1x Excluded (Lexical Monotony: High structural repetition detected in 3415 LOC)
- `.diff`: 24x Excluded (Unsupported Extension: '.diff')
- `.json`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Massive Static Asset Blob: 8560 LOC)
- `.lcl`: 13x Unsupported Format (.lcl)
- `.mjs`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.jsonc`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 583721 LOC exceeds the 150000 LOC backstop)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 98.6 | 21.1 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 0.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 3.5 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.3 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.1 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 31.8 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 7050 | 1133 | 0 | `src/compiler/checker.ts` |
| cleanup | 407 | 44 | 0 | `src/lib/dom.generated.d.ts` |
| guards | 61694 | 5301 | 1 | `src/lib/dom.generated.d.ts` |
| danger | 54019 | 9560 | 2 | `src/lib/dom.generated.d.ts` |
| concurrency | 22596 | 2483 | 0 | `src/lib/dom.generated.d.ts` |
| connectivity | 128339 | 12184 | 4 | `tests/baselines/reference/manyConstExports(target=es2015).js` |
| io | 10090 | 678 | 0 | `tests/baselines/reference/reuseProgramStructure/should-not-reuse-ambient-module-declarations-from-non-modified-files.js` |
| crypto | 2 | 1 | 0 | `src/compiler/sys.ts` |
| ipc | 150 | 28 | 0 | `src/lib/webworker.generated.d.ts` |
| time | 503 | 160 | 0 | `src/compiler/sys.ts` |
| serialization | 226 | 90 | 0 | `src/harness/fourslashImpl.ts` |
| regex | 525 | 174 | 0 | `tests/baselines/reference/parserharness.js` |
| events | 5552 | 792 | 0 | `src/lib/dom.generated.d.ts` |
| tests | 3965 | 615 | 0 | `src/testRunner/unittests/evaluation/esDecorators.ts` |
| docs | 37816 | 3213 | 0 | `src/lib/dom.generated.d.ts` |
| debt | 36281 | 5044 | 1 | `src/lib/dom.generated.d.ts` |
| mutation | 354652 | 22908 | 11 | `tests/baselines/reference/largeControlFlowGraph.js` |
| dead_code | 18537 | 6190 | 1 | `tests/baselines/reference/api/typescript.d.ts` |
| credential | 17 | 13 | 0 | `tests/baselines/reference/fixSignatureCaching.js` |
| threat | 43 | 26 | 0 | `src/compiler/utilities.ts` |
| ml_ai | 2150 | 249 | 0 | `tests/baselines/reference/tsbuildWatch/programUpdates/with-circular-project-reference/change-builds-changes-and-reports-found-errors-message.js` |
| ui | 7523 | 1297 | 0 | `tests/baselines/reference/resolvingClassDeclarationWhenInBaseTypeResolution.js` |

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

1. **core.ts** (`src/compiler/core.ts`) — 213 inbound connections
2. **ts.ts** (`src/testRunner/_namespaces/ts.ts`) — 192 inbound connections
3. **utilities.ts** (`src/compiler/utilities.ts`) — 168 inbound connections
4. **virtualFileSystemWithWatch.ts** (`src/testRunner/unittests/helpers/virtualFileSystemWithWatch.ts`) — 164 inbound connections
5. **utilitiesPublic.ts** (`src/compiler/utilitiesPublic.ts`) — 153 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **tests.ts** (`src/testRunner/tests.ts`) — 233 outbound dependencies
2. **ts.ts** (`src/compiler/_namespaces/ts.ts`) — 75 outbound dependencies
3. **nodeFactory.ts** (`src/compiler/factory/nodeFactory.ts`) — 75 outbound dependencies
4. **ts.codefix.ts** (`src/services/_namespaces/ts.codefix.ts`) — 74 outbound dependencies
5. **program.ts** (`src/compiler/program.ts`) — 67 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `checkTypeRelatedTo` **(Many-Argument Workhorses)** (@ `src/compiler/checker.ts`) -> Impact: **2872.5** | LOC: 2521
  * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determine which checks are performed and as a cache of p...
- `createScanner` **(Many-Argument Workhorses)** (@ `src/compiler/scanner.ts`) -> Impact: **2696.1** | LOC: 3011
  * *Intent:* // Creates a scanner over a (possibly unspecified) range of a piece of text.
- `createProgram` **(Many-Argument Workhorses)** (@ `src/compiler/program.ts`) -> Impact: **2451.7** | LOC: 3327
- `getCompletionData` **(Many-Argument Workhorses)** (@ `src/services/completions.ts`) -> Impact: **2369.5** | LOC: 2019
- `createPrinter` **(Many-Argument Workhorses)** (@ `src/compiler/emitter.ts`) -> Impact: **2337.7** | LOC: 5115
- `createNodeFactory` **(Many-Argument Workhorses)** (@ `src/compiler/factory/nodeFactory.ts`) -> Impact: **2125.7** | LOC: 6695
  * *Intent:* /** * Creates a `NodeFactory` that can be used to create and update a syntax tree. * */
- `createNodeBuilder` **(Compute Cores)** (@ `src/compiler/checker.ts`) -> Impact: **1874.9** | LOC: 4858
- `getFlowTypeOfReference` **(Many-Argument Workhorses)** (@ `src/compiler/checker.ts`) -> Impact: **1244.0** | LOC: 1218
- `symbolTableToDeclarationStatements` **(Many-Argument Workhorses)** (@ `src/compiler/checker.ts`) -> Impact: **1098.2** | LOC: 1802
- `getSymbolDisplayPartsDocumentationAndSymbolKindWorker` **(Many-Argument Workhorses)** (@ `src/services/symbolDisplay.ts`) -> Impact: **913.0** | LOC: 749

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `tests/baselines/reference` | 24255 | 463251.29 | 3.91% | 0.0% |
| `src/compiler` | 39 | 130812.84 | 36.35% | 13.96% |
| `tests/cases/fourslash` | 6298 | 93407.19 | 0.04% | 0.0% |
| `tests/cases/compiler` | 6381 | 86934.34 | 1.69% | 0.0% |
| `src/services` | 39 | 33444.2 | 32.57% | 9.41% |
| `tests/baselines/reference/tsserver/projectReferences` | 67 | 19948.61 | 4.56% | 0.0% |
| `src/compiler/transformers` | 21 | 14980.56 | 25.5% | 12.8% |
| `tests/baselines/reference/tsserver/completionsIncomplete` | 6 | 13787.91 | 5.25% | 0.0% |
| `src/harness` | 24 | 13078.96 | 49.39% | 10.77% |
| `src/services/codefixes` | 73 | 11220.29 | 14.16% | 47.55% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/compiler/factory/nodeTests.ts` -> **100.0%** Exposure
- `src/harness/fakesHosts.ts` -> **100.0%** Exposure
- `src/lib/decorators.d.ts` -> **100.0%** Exposure
- `src/lib/dom.generated.d.ts` -> **100.0%** Exposure
- `src/lib/es2015.collection.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `scripts/failed-tests.cjs` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseBuildOptions/errors on missing argument.js` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseCommandLine/Handles did you mean for misspelt flags.js` -> **100.0%** Exposure
- `tests/baselines/reference/config/commandLineParsing/parseCommandLine/Handles may only be used with --build flags.js` -> **100.0%** Exposure
- `src/compiler/performance.ts` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/lib/dom.generated.d.ts` -> **852** Orphaned Functions | **879** Duplicates
- `tests/baselines/reference/api/typescript.d.ts` -> **1269** Orphaned Functions | **194** Duplicates
- `src/lib/webworker.generated.d.ts` -> **409** Orphaned Functions | **220** Duplicates
- `tests/baselines/reference/privacyAccessorDeclFile(target=es5).js` -> **0** Orphaned Functions | **562** Duplicates
- `tests/baselines/reference/privacyFunctionReturnTypeDeclFile.js` -> **0** Orphaned Functions | **527** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `6` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `4899` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/compiler/checker.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 21.087)
- **Top Global Matches:** file_cluster_6: 21.087, file_cluster_4: 21.246, file_cluster_12: 26.159
- **Magnitude:** 59546.04 | **LOC:** 54435 | **CtrlFlow:** 41.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **94** in-repo importer(s); it depends on **9**; blast radius 0.147; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.5%)
- **Documentation Coverage:** 90.9058% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkTypeRelatedTo` **(Many-Argument Workhorses)** (Impact: 2872.5)
    * *Intent:* /** * Checks if 'source' is related to 'target' (e.g.: is a assignable to). * Used as both to determ...
  * `createNodeBuilder` **(Compute Cores)** (Impact: 1874.9)
  * `getFlowTypeOfReference` **(Many-Argument Workhorses)** (Impact: 1244.0)
  * `symbolTableToDeclarationStatements` **(Many-Argument Workhorses)** (Impact: 1098.2)
  * `inferTypes` **(Many-Argument Workhorses)** (Impact: 756.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 2445 instances
* *Concurrency (weighted view):* 35
* *State Mutation (weighted view):* 7911
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18529`, `structural_boundaries: 11376`, `args: 3463`, `func_start: 2630`, `class_start: 30`
* *Risk/State:* `safety_bypasses: 399`, `high_risk_execution: 1`, `state_mutation: 3021`, `dead_code: 91`, `planned_debt: 62`, `fragile_debt: 19`, `duplicate_logic: 4`
* *Architecture:* `io: 39`, `api: 100`, `concurrency: 25`, `import: 3`
* *Defense:* `safety: 537`, `doc: 239`, `immutability_locks: 331`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.147
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.005446
  * `Imports (Out-Degree: 25):` $moduleSpecifier, ), );
                    
                
                if (!specifier) 
                    specifier = getSpecifierForModuleSymbol(chain[0], ts.js, ts.moduleSpecifiers.js, ts.performance.js, :, ])...
  * `Imported By (In-Degree: 94):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/largeControlFlowGraph.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.064)
- **Top Global Matches:** file_cluster_2: 4.064, file_cluster_17: 6.091, file_cluster_15: 7.066
- **Magnitude:** 20415.06 | **LOC:** 20014 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* None
* *Risk/State:* `state_mutation: 20000`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/manyConstExports(target=es2015).js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.791)
- **Top Global Matches:** file_cluster_2: 5.791, file_cluster_12: 6.79, file_cluster_17: 6.797
- **Magnitude:** 20317.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.4%), Connectivity (formerly Api Exposure) (20.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 5100`
* *Architecture:* `api: 15000`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/manyConstExports(target=es5).js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.791)
- **Top Global Matches:** file_cluster_2: 5.791, file_cluster_12: 6.79, file_cluster_17: 6.797
- **Magnitude:** 20317.04 | **LOC:** 10109 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (74.4%), Connectivity (formerly Api Exposure) (20.9%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 5000`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 5100`
* *Architecture:* `api: 15000`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 13.264)
- **Top Global Matches:** file_cluster_4: 13.264, file_cluster_15: 15.406, file_cluster_0: 15.446
- **Magnitude:** 7828.44 | **LOC:** 10824 | **CtrlFlow:** 31.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **135** in-repo importer(s); it depends on **13**; blast radius 0.262; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (68.8%), Guard Balance (formerly Safety Score) (58.0%)
- **Documentation Coverage:** 94.7126% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseJSDocCommentWorker` **(Many-Argument Workhorses)** (Impact: 547.3)
  * `isListElement` **(Compute Cores)** (Impact: 114.6)
    * *Intent:* // True if positioned at the start of a list element
  * `parseJsonText` **(Many-Argument Workhorses)** (Impact: 70.5)
  * `parseTagComments` **(Many-Argument Workhorses)** (Impact: 66.3)
  * `isStartOfType` **(Compute Cores)** (Impact: 66.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 401 instances
* *State Mutation (weighted view):* 1302
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2581`, `structural_boundaries: 1923`, `args: 786`, `func_start: 839`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 500`, `dead_code: 9`, `planned_debt: 16`, `fragile_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 8`, `api: 158`, `import: 1`
* *Defense:* `safety: 21`, `doc: 36`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.262
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.006264
  * `Imports (Out-Degree: 16):` ) 
        return ModuleKind.ESNext;
    
    if (mode ===, ts.js, ts.performance.js, :
                        tag = parseImportTag(start, end: number, indentText);
                        break;
                
                return tag;
            

            function parseTrailingTagComments(pos: number, indentText);
                        break;
                    default:
                        tag = parseUnknownTag(start, indentText.slice(margin));
            

            function parseTagComments(indent: number...
  * `Imported By (In-Degree: 135):` (Excluded from Brief to save tokens)

### `src/compiler/factory/nodeFactory.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 15.509)
- **Top Global Matches:** file_cluster_15: 15.509, file_cluster_4: 15.513, file_cluster_0: 15.544
- **Magnitude:** 7688.24 | **LOC:** 7543 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **120** in-repo importer(s); it depends on **75**; blast radius 0.218; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (76.9%), Guard Balance (formerly Safety Score) (64.2%)
- **Documentation Coverage:** 95.0241% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createNodeFactory` **(Many-Argument Workhorses)** (Impact: 2125.7)
    * *Intent:* /** * Creates a `NodeFactory` that can be used to create and update a syntax tree. * */
  * `getTransformFlagsSubtreeExclusions` **(Compute Cores)** (Impact: 74.3)
    * *Intent:* /** * Gets the transform flags to exclude when unioning the transform flags of a subtree. */
  * `replaceModifiers` **(Compute Cores)** (Impact: 53.7)
  * `createToken` **(Compute Cores)** (Impact: 49.8)
  * `createCallBinding` **(Many-Argument Workhorses)** (Impact: 43.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 362 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 1771
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1149`, `structural_boundaries: 1138`, `args: 647`, `func_start: 615`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 1047`, `dead_code: 2`, `planned_debt: 4`, `unreferenced_by_name: 69`
* *Architecture:* `io: 3`, `api: 6`, `concurrency: 1`
* *Defense:* `safety: 24`, `doc: 25`, `test: 1`, `immutability_locks: 256`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.218
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.005582
  * `Imports (Out-Degree: 12):` ), ts.js, ;
        default:
            return Debug.fail(`Unsupported kind: $Debug.formatSyntaxKind(kind)`);
    


let rawTextScanner: Scanner | undefined;
const invalidValueSentinel: object = ;

function getCookedText(kind: TemplateLiteralToken[, attributes, attributes), attributes: ImportAttributes | undefined, attributes: JsxAttributes) 
        const node = createBaseNode<JsxOpeningElement>(SyntaxKind.JsxOpeningElement);
        node.tagName = tagName;
        node.typeArguments = asNodeArray(typeArguments);
        node.attributes = attributes;
        node.transformFlags |= propagateChildFlags(node.tagName) |
            propagateChildrenFlags(node.typeArguments) |
            propagateChildFlags(node.attributes) |
            TransformFlags.ContainsJsx;
        if (typeArguments) 
            node.transformFlags |= TransformFlags.ContainsTypeScript;
        
        return node;
    

    
    function updateJsxOpeningElement(node: JsxOpeningElement, attributes: JsxAttributes) 
        const node = createBaseNode<JsxSelfClosingElement>(SyntaxKind.JsxSelfClosingElement);
        node.tagName = tagName;
        node.typeArguments = asNodeArray(typeArguments);
        node.attributes = attributes;
        node.transformFlags |= propagateChildFlags(node.tagName) |
            propagateChildrenFlags(node.typeArguments) |
            propagateChildFlags(node.attributes) |
            TransformFlags.ContainsJsx;
        if (node.typeArguments) 
            node.transformFlags |= TransformFlags.ContainsTypeScript;
        
        return node;
    

    
    function updateJsxSelfClosingElement(node: JsxSelfClosingElement...
  * `Imported By (In-Degree: 120):` (Excluded from Brief to save tokens)

### `src/services/completions.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.931)
- **Top Global Matches:** file_cluster_6: 7.931, file_cluster_4: 12.679, file_cluster_8: 14.745
- **Magnitude:** 7598.24 | **LOC:** 6174 | **CtrlFlow:** 33.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 0.029; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (56.5%), Complexity Load (formerly Cognitive Load) (55.1%)
- **Documentation Coverage:** 77.3585% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getCompletionData` **(Many-Argument Workhorses)** (Impact: 2369.5)
  * `createCompletionEntry` **(Many-Argument Workhorses)** (Impact: 492.9)
  * `getCompletionEntriesFromSymbols` **(Many-Argument Workhorses)** (Impact: 352.0)
  * `isSolelyIdentifierDefinitionLocation` **(Compute Cores)** (Impact: 146.3)
    * *Intent:* /** */
  * `getCompletionEntryCodeActionsAndSourceDisplay` **(Many-Argument Workhorses)** (Impact: 129.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 250 instances
* *Concurrency (weighted view):* 17
* *State Mutation (weighted view):* 781
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1687`, `structural_boundaries: 882`, `args: 288`, `func_start: 197`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 281`, `dead_code: 17`, `planned_debt: 13`, `duplicate_logic: 2`
* *Architecture:* `io: 13`, `api: 31`, `concurrency: 7`, `import: 6`
* *Defense:* `safety: 90`, `doc: 78`, `immutability_locks: 49`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.029
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002616
  * `Imports (Out-Degree: 22):` $entry.source, ts.Completions.js, ts.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/compiler/utilities.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.106)
- **Top Global Matches:** file_cluster_4: 11.106, file_cluster_15: 12.445, file_cluster_12: 12.65
- **Magnitude:** 7360.34 | **LOC:** 12448 | **CtrlFlow:** 19.1% | **Authorship Centralization:** 40.0%
- **Blast Radius:** changing it is visible to **168** in-repo importer(s); it depends on **3**; blast radius 0.303; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (89.5%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (71.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (52.7%)
- **Documentation Coverage:** 15.4116% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveNameHelper` **(Many-Argument Workhorses)** (Impact: 472.1)
  * `createNameResolver` **(Compute Cores)** (Impact: 349.3)
  * `isSourceElement` **(Compute Cores)** (Impact: 139.3)
  * `createEvaluator` **(Compute Cores)** (Impact: 80.1)
  * `evaluate` **(Compute Cores)** (Impact: 79.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 265 instances
* *Concurrency (weighted view):* 25
* *State Mutation (weighted view):* 941
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2009`, `structural_boundaries: 2790`, `args: 1078`, `func_start: 929`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 411`, `dead_code: 11`, `planned_debt: 9`, `fragile_debt: 4`, `duplicate_logic: 4`
* *Architecture:* `io: 99`, `api: 745`, `concurrency: 5`, `import: 6`
* *Defense:* `safety: 278`, `doc: 773`, `immutability_locks: 129`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.303
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.006619
  * `Imports (Out-Degree: 20):` ..., ts.js, name
  * `Imported By (In-Degree: 168):` (Excluded from Brief to save tokens)

### `src/compiler/scanner.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.117)
- **Top Global Matches:** file_cluster_4: 8.117, file_cluster_6: 12.063, file_cluster_15: 13.3
- **Magnitude:** 6883.86 | **LOC:** 4102 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **74** in-repo importer(s); it depends on **1**; blast radius 0.133; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (69.7%)
- **Documentation Coverage:** 61.9048% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createScanner` **(Many-Argument Workhorses)** (Impact: 2696.1)
    * *Intent:* // Creates a scanner over a (possibly unspecified) range of a piece of text.
  * `scanRegularExpressionWorker` **(Many-Argument Workhorses)** (Impact: 711.9)
  * `scan` **(I/O & Config Routines)** (Impact: 207.9)
  * `iterateCommentRanges` **(Many-Argument Workhorses)** (Impact: 109.9)
    * *Intent:* * * to reduceLeft. If false, iteration stops when the callback returns a truthy value. * between tha...
  * `scanEscapeSequence` **(Compute Cores)** (Impact: 108.6)
    * *Intent:* // Extract from Section A.1 // EscapeSequence ::= // | CharacterEscapeSequence // | 0 (?![0-9]) // |...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 449 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 1414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1113`, `structural_boundaries: 598`, `args: 220`, `func_start: 211`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 516`, `planned_debt: 4`
* *Architecture:* `api: 44`, `concurrency: 2`, `import: 2`
* *Defense:* `safety: 14`, `doc: 56`, `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.133
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005667
  * `Imports (Out-Degree: 3):` ts.js
  * `Imported By (In-Degree: 74):` (Excluded from Brief to save tokens)

### `src/compiler/emitter.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.398)
- **Top Global Matches:** file_cluster_4: 11.398, file_cluster_15: 13.819, file_cluster_12: 14.075
- **Magnitude:** 6881.38 | **LOC:** 6379 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **47** in-repo importer(s); it depends on **4**; blast radius 0.079; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (82.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.9%), Connectivity (formerly Api Exposure) (42.3%)
- **Documentation Coverage:** 86.637% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createPrinter` **(Many-Argument Workhorses)** (Impact: 2337.7)
  * `pipelineEmitWithHintWorker` **(Many-Argument Workhorses)** (Impact: 467.8)
  * `emitFiles` **(Many-Argument Workhorses)** (Impact: 304.1)
    * *Intent:* // targetSourceFile is when users only want one file in entire project to be emitted. This is used i...
  * `emitNodeListItems` **(Many-Argument Workhorses)** (Impact: 145.6)
    * *Intent:* /** * Emits a list without brackets or raising events. * * NOTE: You probably don't want to call thi...
  * `emitNodeList` **(Many-Argument Workhorses)** (Impact: 81.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 160 instances
* *State Mutation (weighted view):* 528
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1386`, `structural_boundaries: 770`, `args: 459`, `func_start: 429`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 208`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 9`, `api: 25`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 41`, `doc: 46`, `immutability_locks: 15`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.079
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005417
  * `Imports (Out-Degree: 21):` );
        writePunctuation(, ts.js, ts.performance.js, :
  * `Imported By (In-Degree: 47):` (Excluded from Brief to save tokens)

### `src/compiler/program.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.027)
- **Top Global Matches:** file_cluster_4: 10.027, file_cluster_12: 12.87, file_cluster_15: 13.724
- **Magnitude:** 6421.4 | **LOC:** 5202 | **CtrlFlow:** 29.0% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **125** in-repo importer(s); it depends on **67**; blast radius 0.205; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (64.6%), Guard Balance (formerly Safety Score) (58.6%)
- **Documentation Coverage:** 72.4936% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createProgram` **(Many-Argument Workhorses)** (Impact: 2451.7)
  * `verifyCompilerOptions` **(I/O & Config Routines)** (Impact: 186.8)
  * `getJSSyntacticDiagnosticsForFile` **(Compute Cores)** (Impact: 162.5)
  * `findSourceFileWorker` **(Many-Argument Workhorses)** (Impact: 117.7)
  * `walkArray` **(Many-Argument Workhorses)** (Impact: 88.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 266 instances
* *State Mutation (weighted view):* 872
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1237`, `structural_boundaries: 723`, `args: 399`, `func_start: 301`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 340`, `planned_debt: 12`, `duplicate_logic: 4`
* *Architecture:* `io: 130`, `api: 72`, `import: 1`
* *Defense:* `safety: 137`, `doc: 63`, `immutability_locks: 70`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.205
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.006206
  * `Imports (Out-Degree: 28):` && elem.value.text !==, ), ) => ResolutionLoader<Entry, ): ResolutionLoader<StringLiteralLike, ): ResolutionLoader<T, ): readonly Resolution[] 
    if (entries.length === 0) return emptyArray;
    const resolutions: Resolution[] = [];
    const cache = new Map<ModeAwareCacheKey, ts.js, ts.performance.js...
  * `Imported By (In-Degree: 125):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/tsserver/completionsIncomplete/resolves-more-when-available-from-module-specifier-cache-(1).js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.157)
- **Top Global Matches:** file_cluster_2: 4.157, file_cluster_17: 5.695, file_cluster_13: 6.614
- **Magnitude:** 6122.18 | **LOC:** 54159 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%), Connectivity (formerly Api Exposure) (15.6%), Concurrency Surface (formerly Concurrency) (12.0%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 5035`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 3`
* *Architecture:* `api: 5021`, `concurrency: 2`
* *Defense:* `safety: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/editorServices.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.711)
- **Top Global Matches:** file_cluster_4: 6.711, file_cluster_12: 10.506, file_cluster_6: 11.396
- **Magnitude:** 3873.44 | **LOC:** 5728 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **3**; blast radius 0.031; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%), Connectivity (formerly Api Exposure) (35.0%)
- **Documentation Coverage:** 54.9254% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `forEachResolvedProjectReferenceProjectLoad` **(Many-Argument Workhorses)** (Impact: 106.6)
    * *Intent:* /** * Goes through parentConfig's project references and finds, creates or reloads project per kind ...
  * `findCreateOrReloadConfiguredProject` **(Many-Argument Workhorses)** (Impact: 98.3)
    * *Intent:* /** * Depending on kind * - Find the configuedProject and return it - if allowDeferredClosed is set ...
  * `tryFindDefaultConfiguredProjectForOpenScriptInfoOrClosedFileInfo` **(Many-Argument Workhorses)** (Impact: 90.3)
  * `onWildCardDirectoryWatcherInvoke` **(Many-Argument Workhorses)** (Impact: 72.7)
  * `applySafeListWorker` **(Many-Argument Workhorses)** (Impact: 63.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 285 instances
* *Concurrency (weighted view):* 26
* *State Mutation (weighted view):* 901
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1093`, `structural_boundaries: 737`, `args: 426`, `func_start: 275`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 100`, `state_mutation: 331`, `dead_code: 2`, `planned_debt: 8`, `duplicate_logic: 2`
* *Architecture:* `io: 151`, `api: 132`, `concurrency: 16`, `import: 2`
* *Defense:* `safety: 135`, `doc: 195`, `immutability_locks: 100`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.031
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001858
  * `Imports (Out-Degree: 27):` ts.js, ts.server.js, protocol.js
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/compiler/moduleNameResolver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.257)
- **Top Global Matches:** file_cluster_4: 6.257, file_cluster_6: 10.44, file_cluster_15: 12.214
- **Magnitude:** 3826.42 | **LOC:** 3429 | **CtrlFlow:** 33.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **26** in-repo importer(s); it depends on **40**; blast radius 0.055; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.9%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (59.8%), Guard Balance (formerly Safety Score) (54.8%)
- **Documentation Coverage:** 51.1278% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getLoadModuleFromTargetExportOrImport` **(Many-Argument Workhorses)** (Impact: 263.5)
    * *Intent:* /** * Gets the self-recursive function specialized to retrieving the targeted import/export element ...
  * `loadModuleFromTargetExportOrImport` **(Many-Argument Workhorses)** (Impact: 210.7)
  * `nodeModuleNameResolverWorker` **(Many-Argument Workhorses)** (Impact: 210.2)
  * `resolveTypeReferenceDirective` **(Many-Argument Workhorses)** (Impact: 187.5)
    * *Intent:* /** * This is possible in case if resolution is performed for directives specified via 'types' param...
  * `tryAddingExtensions` **(Compute Cores)** (Impact: 162.0)
    * *Intent:* /** Try to return an existing file that adds one of the `extensions` to `candidate`. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 128 instances
* *State Mutation (weighted view):* 406
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 916`, `structural_boundaries: 505`, `args: 249`, `func_start: 217`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 150`, `planned_debt: 3`, `fragile_debt: 1`, `duplicate_logic: 11`
* *Architecture:* `io: 73`, `api: 71`
* *Defense:* `safety: 73`, `doc: 102`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.055
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005087
  * `Imports (Out-Degree: 9):` )
        ) 
            traceIfEnabled(state, )) ? ModuleKind.ESNext : ModuleKind.CommonJS;
    
    
    
    
    
    
    const priorityExtensions = extensions & (Extensions.TypeScript | Extensions.Declaration);
    const secondaryExtensions = extensions & ~(Extensions.TypeScript | Extensions.Declaration);
    
    if (priorityExtensions) 
        traceIfEnabled(state, );

    function tryResolve(extensions: Extensions, ts.js, ;
            const diagnosticResult = tryResolve(extensions & (Extensions.TypeScript | Extensions.Declaration), Diagnostics.Resolution_of_non_relative_name_failed_trying_with_modern_Node_resolution_features_disabled_to_see_if_npm_library_needs_configuration_update);
            const diagnosticState = 
                ...state, Diagnostics.Resolution_of_non_relative_name_failed_trying_with_moduleResolution_bundler_to_see_if_project_may_need_configuration_update);
            const diagnosticsCompilerOptions =  ...state.compilerOptions, Diagnostics.Searching_all_ancestor_node_modules_directories_for_fallback_extensions_Colon_0...
  * `Imported By (In-Degree: 26):` (Excluded from Brief to save tokens)

### `src/services/utilities.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.675)
- **Top Global Matches:** file_cluster_4: 6.675, file_cluster_15: 10.556, file_cluster_12: 11.537
- **Magnitude:** 3492.46 | **LOC:** 4237 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **136** in-repo importer(s); it depends on **1**; blast radius 0.248; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.5%), Connectivity (formerly Api Exposure) (82.1%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%)
- **Documentation Coverage:** 17.004% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getAdjustedLocation` **(Compute Cores)** (Impact: 191.8)
  * `isCompletedNode` **(Compute Cores)** (Impact: 129.7)
  * `getNodeKind` **(Compute Cores)** (Impact: 95.8)
  * `getTokenAtPositionWorker` **(Many-Argument Workhorses)** (Impact: 83.1)
    * *Intent:* /** Get the token whose text contains the position */
  * `createPackageJsonImportFilter` **(Many-Argument Workhorses)** (Impact: 77.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 126 instances
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1148`, `structural_boundaries: 935`, `args: 351`, `func_start: 307`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 135`, `dead_code: 23`, `planned_debt: 2`, `duplicate_logic: 2`
* *Architecture:* `io: 10`, `api: 214`
* *Defense:* `safety: 49`, `doc: 251`, `immutability_locks: 26`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.248
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.00425
  * `Imports (Out-Degree: 19):` ts.js
  * `Imported By (In-Degree: 136):` (Excluded from Brief to save tokens)

### `src/harness/fourslashImpl.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.168)
- **Top Global Matches:** file_cluster_12: 8.168, file_cluster_4: 8.263, file_cluster_16: 10.338
- **Magnitude:** 3307.76 | **LOC:** 5216 | **CtrlFlow:** 19.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 0.038; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.9%), Complexity Load (formerly Cognitive Load) (54.3%)
- **Documentation Coverage:** 97.8667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getBaselineContentForFile` **(Many-Argument Workhorses)** (Impact: 214.2)
  * `parseFileContent` **(Many-Argument Workhorses)** (Impact: 112.5)
  * `verifyCompletionsWorker` **(Defensive Guards)** (Impact: 92.7)
  * `constructor` **(Many-Argument Workhorses)** (Impact: 82.2)
  * `verifyImportFixModuleSpecifiers` **(Many-Argument Workhorses)** (Impact: 54.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 227 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 849
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 858`, `structural_boundaries: 730`, `args: 542`, `func_start: 327`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 93`, `high_risk_execution: 3`, `state_mutation: 395`, `dead_code: 6`, `planned_debt: 7`
* *Architecture:* `io: 17`, `api: 182`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 109`, `doc: 9`, `test: 24`, `immutability_locks: 63`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.038
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.000844
  * `Imports (Out-Degree: 31):` FourSlashInterface.js, Harness.js, Utils.js, fakes.js, ts.js, vfs.js, vpath.js, harnessLanguageService.js...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/services/services.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.067)
- **Top Global Matches:** file_cluster_4: 10.067, file_cluster_12: 10.787, file_cluster_15: 12.172
- **Magnitude:** 3183.32 | **LOC:** 3623 | **CtrlFlow:** 22.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **6**; blast radius 0.075; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.3%), Guard Balance (formerly Safety Score) (57.2%)
- **Documentation Coverage:** 92.4581% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createLanguageService` **(Many-Argument Workhorses)** (Impact: 848.6)
  * `toggleMultilineComment` **(Many-Argument Workhorses)** (Impact: 77.6)
  * `visit` **(Compute Cores)** (Impact: 75.2)
  * `computeNamedDeclarations` **(I/O & Config Routines)** (Impact: 62.4)
  * `synchronizeHostDataWorker` **(I/O & Config Routines)** (Impact: 56.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 101 instances
* *State Mutation (weighted view):* 367
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 661`, `structural_boundaries: 516`, `args: 320`, `func_start: 270`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 47`, `state_mutation: 165`, `dead_code: 4`, `planned_debt: 24`, `fragile_debt: 9`, `duplicate_logic: 8`
* *Architecture:* `io: 19`, `api: 116`, `concurrency: 9`, `import: 5`
* *Defense:* `safety: 41`, `doc: 19`, `immutability_locks: 24`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.075
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.003725
  * `Imports (Out-Degree: 28):` ts.NavigateTo.js, ts.NavigationBar.js, ts.js, ts.refactor.js, classifier.js, classifier2020.js
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/tsserver/projectReferences/solution-with-its-own-files-and-project-is-indirectly-referenced-by-solution.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.711)
- **Top Global Matches:** file_cluster_2: 3.711, file_cluster_17: 5.596, file_cluster_15: 6.615
- **Magnitude:** 3134.88 | **LOC:** 5168 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 0.019; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (52.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%), Connectivity (formerly Api Exposure) (7.7%), Complexity Load (formerly Cognitive Load) (6.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 62`, `structural_boundaries: 83`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 92`
* *Architecture:* `api: 26`, `import: 48`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` functions, main
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/binder.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.356)
- **Top Global Matches:** file_cluster_4: 7.356, file_cluster_6: 10.566, file_cluster_12: 12.662
- **Magnitude:** 2955.32 | **LOC:** 3917 | **CtrlFlow:** 33.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **19** in-repo importer(s); it depends on **2**; blast radius 0.044; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.5%)
- **Documentation Coverage:** 90.6593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bindWorker` **(Compute Cores)** (Impact: 183.6)
  * `declareSymbol` **(Many-Argument Workhorses)** (Impact: 139.8)
    * *Intent:* /** * Declares a Symbol for the node and adds it to symbols. Reports errors for conflicting identifi...
  * `bindChildren` **(Type Conversions)** (Impact: 78.0)
  * `bindContainer` **(Many-Argument Workhorses)** (Impact: 75.5)
    * *Intent:* // All container nodes are kept on a linked list in declaration order. This list is used by // the g...
  * `getContainerFlags` **(Compute Cores)** (Impact: 65.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 213 instances
* *State Mutation (weighted view):* 743
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1053`, `structural_boundaries: 417`, `args: 191`, `func_start: 175`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 53`, `high_risk_execution: 1`, `state_mutation: 317`, `dead_code: 7`, `planned_debt: 6`
* *Architecture:* `io: 3`, `api: 10`, `import: 1`
* *Defense:* `safety: 12`, `doc: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.044
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005008
  * `Imports (Out-Degree: 13):` ts.js, ts.performance.js
  * `Imported By (In-Degree: 19):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/enumLiteralsSubtypeReduction.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 6.604)
- **Top Global Matches:** file_cluster_1: 6.604, file_cluster_3: 48.34, file_cluster_8: 70.144
- **Magnitude:** 2674.8 | **LOC:** 4117 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (62.3%), Complexity Load (formerly Cognitive Load) (25.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Compute Cores)** (Impact: 778.3)
  * `run` **(Compute Cores)** (Impact: 778.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 1036
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1027`, `structural_boundaries: 1025`, `args: 3`, `func_start: 2`
* *Risk/State:* `state_mutation: 1024`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/binaryArithmeticControlFlowGraphNotTooLarge.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 5.765)
- **Top Global Matches:** file_cluster_2: 5.765, file_cluster_15: 7.688, file_cluster_17: 7.823
- **Magnitude:** 2665.02 | **LOC:** 2565 | **CtrlFlow:** 0.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (88.5%), Complexity Load (formerly Cognitive Load) (25.2%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `foo` **(I/O & Config Routines)** (Impact: 10.6)
    * *Intent:* //// [tests/cases/compiler/binaryArithmeticControlFlowGraphNotTooLarge.ts] //// //// [binaryArithmet...
  * `foo` **(I/O & Config Routines)** (Impact: 8.0)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/baselines/reference/parserharness.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.106)
- **Top Global Matches:** file_cluster_12: 7.106, file_cluster_15: 9.51, file_cluster_10: 10.37
- **Magnitude:** 2658.84 | **LOC:** 3820 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 0.019; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (67.0%), Concurrency Surface (formerly Concurrency) (64.1%), Complexity Load (formerly Cognitive Load) (38.4%), Connectivity (formerly Api Exposure) (11.0%)
- **Documentation Coverage:** 43.4375% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Defensive Guards)** (Impact: 54.0)
  * `generateDeclFile` **(Many-Argument Workhorses)** (Impact: 39.8)
    * *Intent:* /** Generates a .d.ts file for the given code */
  * `getTypeInfoName` **(Compute Cores)** (Impact: 39.2)
  * `makeUnitsFromTest` **(Many-Argument Workhorses)** (Impact: 34.2)
  * `makeUnitsFromTest` **(Many-Argument Workhorses)** (Impact: 33.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 16 instances
* *Amplified Cascading Flux:* 331 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 100
* *State Mutation (weighted view):* 1230
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 527`, `structural_boundaries: 905`, `args: 349`, `func_start: 268`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 67`, `high_risk_execution: 4`, `state_mutation: 568`, `dead_code: 34`, `planned_debt: 8`, `fragile_debt: 21`, `duplicate_logic: 24`, `unreferenced_by_name: 1`
* *Architecture:* `io: 2`, `api: 91`, `concurrency: 20`, `import: 2`
* *Defense:* `safety: 130`, `doc: 56`, `test: 60`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` vm
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/compiler/commandLineParser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.98)
- **Top Global Matches:** file_cluster_4: 5.98, file_cluster_6: 8.506, file_cluster_12: 12.721
- **Magnitude:** 2584.22 | **LOC:** 4301 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 33.3%
- **Blast Radius:** changing it is visible to **35** in-repo importer(s); it depends on **1**; blast radius 0.072; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.8%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.9%), Connectivity (formerly Api Exposure) (58.6%)
- **Documentation Coverage:** 51.4793% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseJsonConfigFileContentWorker` **(Many-Argument Workhorses)** (Impact: 168.8)
    * *Intent:* /** * Parse the contents of a config file from json or json source file (tsconfig.json). * file to. ...
  * `parseConfig` **(Many-Argument Workhorses)** (Impact: 103.5)
    * *Intent:* /** * This *just* extracts options/include/exclude/files out of a config file. * It does *not* resol...
  * `convertToJson` **(Many-Argument Workhorses)** (Impact: 89.2)
    * *Intent:* /** * Convert the json syntax tree into the json value and report errors * This returns the json val...
  * `parseOwnConfigOfJsonSourceFile` **(Many-Argument Workhorses)** (Impact: 79.8)
  * `parseOptionValue` **(Many-Argument Workhorses)** (Impact: 78.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 156 instances
* *State Mutation (weighted view):* 480
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 599`, `structural_boundaries: 613`, `args: 199`, `func_start: 130`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 46`, `state_mutation: 168`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `io: 51`, `api: 73`
* *Defense:* `safety: 37`, `doc: 76`, `immutability_locks: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.072
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005215
  * `Imports (Out-Degree: 11):` ts.js
  * `Imported By (In-Degree: 35):` (Excluded from Brief to save tokens)

### `tests/baselines/reference/tsserver/completionsIncomplete/works.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 3.726)
- **Top Global Matches:** file_cluster_2: 3.726, file_cluster_17: 5.396, file_cluster_13: 6.346
- **Magnitude:** 2473.9 | **LOC:** 22661 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 50.0%
- **Blast Radius:** isolated in the scanned graph -- no in-repo artifact imports it and it imports none
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (50.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.7%), Connectivity (formerly Api Exposure) (15.2%), Concurrency Surface (formerly Concurrency) (12.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`, `structural_boundaries: 2043`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 5`
* *Architecture:* `api: 2003`, `concurrency: 6`
* *Defense:* `safety: 15`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.019
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/server/session.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.21)
- **Top Global Matches:** file_cluster_12: 8.21, file_cluster_5: 9.72, file_cluster_16: 10.622
- **Magnitude:** 2410.24 | **LOC:** 4084 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 0.025; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (80.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.6%), Connectivity (formerly Api Exposure) (33.9%)
- **Documentation Coverage:** 93.8735% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getPerProjectReferences` **(Many-Argument Workhorses)** (Impact: 82.9)
    * *Intent:* /** * If multiple projects were searched - even if they didn't return results - the result will be a...
  * `findSourceDefinition` **(Defensive Guards)** (Impact: 72.8)
  * `getReferencesWorker` **(Many-Argument Workhorses)** (Impact: 69.7)
  * `updateErrorCheck` **(Many-Argument Workhorses)** (Impact: 45.0)
    * *Intent:* /** It is the caller's responsibility to verify that `!this.suppressDiagnosticEvents`. */
  * `onMessage` **(Defensive Guards)** (Impact: 39.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 115 instances
* *Concurrency (weighted view):* 13
* *State Mutation (weighted view):* 371
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 583`, `structural_boundaries: 834`, `args: 514`, `func_start: 352`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 101`, `state_mutation: 141`, `planned_debt: 35`
* *Architecture:* `io: 15`, `api: 140`, `concurrency: 3`, `import: 2`
* *Defense:* `safety: 66`, `doc: 25`, `immutability_locks: 77`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.025
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002013
  * `Imports (Out-Degree: 24):` ts.js, ts.server.js, protocol.js
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/cases/compiler/superAccess2.ts` (TYPESCRIPT) | Magnitude: 9.88 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 15, args: 5, func_start: 5, structural_boundaries: 4
- `tests/cases/compiler/typePredicateInLoop.ts` (TYPESCRIPT) | Magnitude: 10.72 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 8, branch: 3, args: 3
- `tests/cases/compiler/super.ts` (TYPESCRIPT) | Magnitude: 13.18 | Delta: **0.018** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 18, structural_boundaries: 13, args: 6, func_start: 6
- `tests/cases/conformance/jsdoc/declarations/jsDeclarationsDefault.ts` (TYPESCRIPT) | Magnitude: 18.56 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 15, api: 10, branch: 6, doc: 4
- `tests/cases/compiler/declarationEmitProtectedMembers.ts` (TYPESCRIPT) | Magnitude: 15.42 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 15, args: 12, func_start: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/baselines/reference/exportsAndImports4(target=es5).js` (JAVASCRIPT) | Magnitude: 73.0 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 51, structural_boundaries: 40, indent_spaces: 26, import: 18
- `src/services/codefixes/splitTypeOnlyImport.ts` (TYPESCRIPT) | Magnitude: 13.42 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 9, args: 6, func_start: 5
- `tests/baselines/reference/exportsAndImports4(target=es2015).js` (JAVASCRIPT) | Magnitude: 73.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 51, structural_boundaries: 34, indent_spaces: 26, import: 18
- `tests/baselines/reference/exportsAndImports4-es6.js` (JAVASCRIPT) | Magnitude: 73.0 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: branch: 51, structural_boundaries: 34, indent_spaces: 26, import: 18
- `tests/cases/compiler/implicitAnyFromCircularInference.ts` (TYPESCRIPT) | Magnitude: 14.96 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: structural_boundaries: 17, indent_spaces: 10, args: 8, func_start: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/cases/conformance/jsdoc/declarations/jsDeclarationsFunctionLikeClasses2.ts` (TYPESCRIPT) | Magnitude: 49.04 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 37, state_mutation: 11, structural_boundaries: 9, args: 8
- `tests/baselines/reference/letDeclarations-validContexts.js` (JAVASCRIPT) | Magnitude: 33.94 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 116, structural_boundaries: 96, core_var_decl: 78, design_snake_case: 74
- `tests/baselines/reference/objectTypesIdentityWithGenericCallSignatures2.js` (JAVASCRIPT) | Magnitude: 130.0 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: func_start: 81, args: 79, structural_boundaries: 18, duplicate_logic: 17
- `tests/cases/conformance/override/override5.ts` (TYPESCRIPT) | Magnitude: 12.7 | Delta: **0.009** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 19, args: 9, func_start: 9
- `tests/baselines/reference/collisionArgumentsClassConstructor(target=es5).js` (JAVASCRIPT) | Magnitude: 84.58 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 111, structural_boundaries: 68, core_var_decl: 34, args: 30

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `tests/cases/compiler/capturedLetConstInLoop9_ES6.ts` (TYPESCRIPT) | Magnitude: 48.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 33, branch: 30, args: 10
- `tests/baselines/reference/getterSetterSubtypeAssignment.js` (JAVASCRIPT) | Magnitude: 125.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 99, state_mutation: 60, func_start: 40, args: 37
- `tests/cases/compiler/capturedLetConstInLoop9.ts` (TYPESCRIPT) | Magnitude: 48.36 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 102, structural_boundaries: 33, branch: 30, args: 10
- `tests/baselines/reference/tsbuild/noEmit/multiFile/changes-with-initial-noEmit-incremental-declaration.js` (JAVASCRIPT) | Magnitude: 256.9 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 712, structural_boundaries: 210, api: 65, bitwise_ops: 63
- `tests/baselines/reference/tscWatch/programUpdates/should-not-trigger-recompilation-because-of-program-emit/without-outDir-or-outFile-is-specified.js` (JAVASCRIPT) | Magnitude: 32.86 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 41, bitwise_ops: 12, api: 9, state_mutation: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `tests/baselines/reference/privateNameEmitHelpers.js` (JAVASCRIPT) | Magnitude: 13.72 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: structural_boundaries: 10, indent_spaces: 7, args: 5, func_start: 5
- `src/testRunner/tests.ts` (TYPESCRIPT) | Magnitude: 252.66 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 238, api: 233, import: 233, generics: 5
- `tests/baselines/reference/decoratorReferences.js` (JAVASCRIPT) | Magnitude: 15.66 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: branch: 16, indent_spaces: 12, structural_boundaries: 11, args: 8
- `tests/cases/compiler/declarationImportTypeAliasInferredAndEmittable.ts` (TYPESCRIPT) | Magnitude: 9.08 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 8, indent_spaces: 7, args: 3, func_start: 3
- `tests/cases/compiler/es6ClassTest9.ts` (TYPESCRIPT) | Magnitude: 1.14 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, args: 1, func_start: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/baselines/reference/exportDefaultAsyncFunction.js` (JAVASCRIPT) | Magnitude: 17.3 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: args: 10, branch: 8, indent_spaces: 8, structural_boundaries: 6
- `tests/baselines/reference/elaborationForPossiblyCallableTypeStillReferencesArgumentAtTopLevel.js` (JAVASCRIPT) | Magnitude: 1.6 | Delta: **0.021** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 2, args: 2, func_start: 1, safety_bypasses: 1
- `tests/baselines/reference/unionReductionMutualSubtypes.js` (JAVASCRIPT) | Magnitude: 10.72 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 6, branch: 5, core_var_decl: 4, safety: 3
- `tests/cases/conformance/jsx/tsxAttributeResolution12.tsx` (TYPESCRIPT) | Magnitude: 22.84 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: structural_boundaries: 23, indent_tabs: 21, branch: 8, class_start: 7
- `tests/baselines/reference/restElementWithNullInitializer(target=es5).js` (JAVASCRIPT) | Magnitude: 18.42 | Delta: **0.047** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: args: 8, func_start: 8, branch: 4, structural_boundaries: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/cases/conformance/parser/ecmascript5/parserRealSource13.ts` (TYPESCRIPT) | Magnitude: 232.58 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 132, func_start: 111, branch: 109, unreferenced_by_name: 107
- `src/compiler/factory/nodeFactory.ts` (TYPESCRIPT) | Magnitude: 7688.24 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 6042, branch: 1149, structural_boundaries: 1138, state_mutation: 1047
- `tests/baselines/reference/jsDeclarationsImportAliasExposedWithinNamespace.js` (JAVASCRIPT) | Magnitude: 13.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 14, doc: 13, structural_boundaries: 11, api: 7
- `.github/workflows/twoslash-repros.yaml` (YAML) | Magnitude: 13.76 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 52, args: 12, doc: 7, branch: 6
- `tests/baselines/reference/objectTypesIdentityWithGenericCallSignaturesDifferingTypeParameterCounts.js` (JAVASCRIPT) | Magnitude: 135.3 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: func_start: 81, args: 79, structural_boundaries: 18, duplicate_logic: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `tests/baselines/reference/privateNamesAndIndexedAccess.js` (JAVASCRIPT) | Magnitude: 7.34 | Delta: **0.05** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, state_mutation: 4, core_var_decl: 4, structural_boundaries: 3
- `tests/cases/compiler/declFileEmitDeclarationOnly.ts` (TYPESCRIPT) | Magnitude: 5.3 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 6, args: 3, func_start: 3, unreferenced_by_name: 2
- `tests/cases/conformance/jsdoc/jsdocLinkTag7.ts` (TYPESCRIPT) | Magnitude: 3.4 | Delta: **0.148** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: args: 3, func_start: 3, indent_spaces: 3, unreferenced_by_name: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/services/_namespaces/ts.formatting.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.017** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7
- `tests/baselines/reference/printerApi/printsNodeCorrectly.functionTypes.js` (JAVASCRIPT) | Magnitude: 10.52 | Delta: **0.023** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 6, args: 6, branch: 1
- `tests/cases/compiler/constantEnumAssert.ts` (TYPESCRIPT) | Magnitude: 16.66 | Delta: **0.04** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 18, design_snake_case: 17, indent_spaces: 11, immutability_locks: 10
- `tests/cases/conformance/types/intersection/intersectionTypeReadonly.ts` (TYPESCRIPT) | Magnitude: 20.5 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, class_start: 5, state_mutation: 5, indent_spaces: 5
- `tests/cases/conformance/types/union/unionTypeReadonly.ts` (TYPESCRIPT) | Magnitude: 20.5 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 10, class_start: 5, state_mutation: 5, indent_spaces: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/baselines/reference/tsserver/plugins/new-files-with-non-ts-extensions-with-wildcard-matching.js` (JAVASCRIPT) | Magnitude: 47.52 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 205, indent_tabs: 23, structural_boundaries: 17, api: 16
- `tests/baselines/reference/tsserver/typingsInstaller/malformed-packagejson.js` (JAVASCRIPT) | Magnitude: 35.9 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 418, decorators: 40, doc: 32, safety_bypasses: 12
- `tests/cases/compiler/mergedModuleDeclarationCodeGen5.ts` (TYPESCRIPT) | Magnitude: 12.72 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, indent_spaces: 12, api: 8, core_var_decl: 6
- `tests/cases/conformance/dynamicImport/importCallExpressionGrammarError.ts` (TYPESCRIPT) | Magnitude: 1.24 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 9, import: 4, core_var_decl: 4, design_snake_case: 4
- `tests/baselines/reference/enumIdentifierLiterals.js` (JAVASCRIPT) | Magnitude: 28.32 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 10, state_mutation: 5, branch: 1, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/compiler/utilitiesPublic.ts` (TYPESCRIPT) | Magnitude: 1877.46 | Delta: **0.005** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 1466, branch: 745, structural_boundaries: 613, args: 259
- `tests/baselines/reference/awaitUsingDeclarations.3(target=es5).js` (JAVASCRIPT) | Magnitude: 261.02 | Delta: **0.012** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 100, branch: 74, structural_boundaries: 50, safety: 36
- `tests/baselines/reference/importCallExpressionNestedES20152(target=es5).js` (JAVASCRIPT) | Magnitude: 134.56 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 53, indent_spaces: 42, structural_boundaries: 38, state_mutation: 19
- `tests/baselines/reference/importCallExpressionNestedES20202(target=es5).js` (JAVASCRIPT) | Magnitude: 134.56 | Delta: **0.013** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: branch: 53, indent_spaces: 42, structural_boundaries: 38, state_mutation: 19
- `src/testRunner/unittests/helpers/tsserver.ts` (TYPESCRIPT) | Magnitude: 440.36 | Delta: **0.026** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 485, structural_boundaries: 153, branch: 99, args: 72

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `tests/cases/conformance/types/typeRelationships/subtypesAndSuperTypes/subtypingWithConstructSignatures3.ts` (TYPESCRIPT) | Magnitude: 38.6 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 136, indent_spaces: 91, args: 45, generics: 29
- `tests/cases/compiler/declarationEmitMappedPrivateTypeTypeParameter.ts` (TYPESCRIPT) | Magnitude: 14.08 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 4, generics: 4, api: 2, safety_bypasses: 1
- `tests/cases/compiler/variableDeclaratorResolvedDuringContextualTyping.ts` (TYPESCRIPT) | Magnitude: 139.32 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 84, structural_boundaries: 65, branch: 34, args: 31
- `tests/cases/conformance/jsx/tsxOpeningClosingNames.tsx` (TYPESCRIPT) | Magnitude: 13.64 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 6, class_start: 1, safety_bypasses: 1, generics: 1
- `tests/cases/compiler/externalModuleExportingGenericClass.ts` (TYPESCRIPT) | Magnitude: 16.16 | Delta: **0.043** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: structural_boundaries: 6, core_var_decl: 4, design_snake_case: 4, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `tests/baselines/reference/awaitUsingDeclarations.2(target=es5).js` (JAVASCRIPT) | Magnitude: 267.06 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 102, branch: 74, structural_boundaries: 53, safety: 36
- `src/services/goToDefinition.ts` (TYPESCRIPT) | Magnitude: 645.66 | Delta: **0.151** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 559, branch: 230, structural_boundaries: 153, core_var_decl: 105
- `src/compiler/checker.ts` (TYPESCRIPT) | Magnitude: 59546.04 | Delta: **0.159** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 44361, branch: 18529, structural_boundaries: 11376, core_var_decl: 7657

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/baselines/reference/es5-asyncFunctionWhileStatements(target=es2015).js` (JAVASCRIPT) | Magnitude: 130.98 | Delta: **0.0** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 126, structural_boundaries: 80, args: 57, branch: 46
- `tests/cases/compiler/commentOnSimpleArrowFunctionBody1.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: args: 2, structural_boundaries: 1, func_start: 1, safety_bypasses: 1
- `tests/cases/compiler/lambdaASIEmit.ts` (TYPESCRIPT) | Magnitude: 1.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: args: 2, structural_boundaries: 1, func_start: 1, safety_bypasses: 1
- `tests/baselines/reference/decoratorChecksFunctionBodies(target=es2015).js` (JAVASCRIPT) | Magnitude: 14.82 | Delta: **0.002** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 18, branch: 14, structural_boundaries: 12, args: 7
- `tests/baselines/reference/comparisonOperatorWithSubtypeObjectOnOptionalProperty.js` (JAVASCRIPT) | Magnitude: 15.88 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: structural_boundaries: 36, core_var_decl: 32, design_snake_case: 32, safety: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `tests/baselines/reference/destructuringAssignmentWithDefault.js` (JAVASCRIPT) | Magnitude: 71.42 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: branch: 37, indent_spaces: 28, structural_boundaries: 22, core_var_decl: 16
- `src/testRunner/unittests/tsserver/events/watchEvents.ts` (TYPESCRIPT) | Magnitude: 40.78 | Delta: **0.014** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 54, structural_boundaries: 30, api: 10, core_var_decl: 8
- `tests/baselines/reference/logicalAssignment2(target=es2015).js` (JAVASCRIPT) | Magnitude: 30.08 | Delta: **0.038** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: branch: 21, safety: 9, indent_spaces: 7, state_mutation: 6
- `tests/baselines/reference/nullishCoalescingOperatorInAsyncGenerator(target=es5).js` (JAVASCRIPT) | Magnitude: 50.66 | Delta: **0.048** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 23, branch: 12, structural_boundaries: 11, args: 4

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler/checker.ts` -> Churn: **69.52%** | Cog Load: 73.2659% | Debt: 9.4023%
- `src/compiler/binder.ts` -> Churn: **56.46%** | Cog Load: 52.2281% | Debt: 8.2729%
- `src/compiler/types.ts` -> Churn: **53.22%** | Cog Load: 5.6302% | Debt: 96.0109%
- `src/compiler/program.ts` -> Churn: **51.6%** | Cog Load: 64.6172% | Debt: 12.602%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/compiler/moduleNameResolver.ts` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 3826.42
- `src/compiler/core.ts` -> **Jake Bailey** (100.0% isolated ownership) | Magnitude: 2270.72
- `src/compiler/resolutionCache.ts` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 1966.38
- `src/compiler/utilitiesPublic.ts` -> **Kenta Moriuchi** (100.0% isolated ownership) | Magnitude: 1877.46
- `src/compiler/transformers/ts.ts` -> **Ryan Cavanaugh** (100.0% isolated ownership) | Magnitude: 1767.94

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/testRunner/runner.ts` -> **Severity: 0.003** (Bridge: 0.0 * Flux: 99.76%)
- `src/testRunner/unittests/helpers/tsc.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)
- `src/testRunner/unittests/helpers/tsserver.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 96.4292%)
- `src/testRunner/unittests/helpers/virtualFileSystemWithWatch.ts` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/compiler/core.ts` -> **Severity: 0.462** (Embedded: 0.0071 * Error Risk: 65.505%)
- `src/compiler/scanner.ts` -> **Severity: 0.395** (Embedded: 0.0057 * Error Risk: 69.7325%)
- `src/compiler/path.ts` -> **Severity: 0.376** (Embedded: 0.006 * Error Risk: 62.6389%)
- `src/compiler/program.ts` -> **Severity: 0.364** (Embedded: 0.0062 * Error Risk: 58.6436%)
- `src/compiler/parser.ts` -> **Severity: 0.363** (Embedded: 0.0063 * Error Risk: 58.0045%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/testRunner/unittests/helpers/virtualFileSystemWithWatch.ts` -> **Severity: 62.0** (Blast Radius: 0.62 * Doc Risk: 100.0%)
- `src/testRunner/unittests/helpers.ts` -> **Severity: 44.9** (Blast Radius: 0.449 * Doc Risk: 100.0%)
- `src/testRunner/unittests/helpers/tsserver.ts` -> **Severity: 35.0** (Blast Radius: 0.35 * Doc Risk: 100.0%)
- `src/compiler/transformers/jsx.ts` -> **Severity: 28.976** (Blast Radius: 0.36 * Doc Risk: 80.4878%)
- `src/compiler/parser.ts` -> **Severity: 24.815** (Blast Radius: 0.262 * Doc Risk: 94.7126%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 5040 literal sites + 24 sites through wrappers = 5064
- **`panics_and_aborts`:** 3967 literal sites + 99 sites through wrappers = 4066

- `notImplemented` (function, panics_and_aborts, primitive): 25 call sites in 2 files -- `src/compiler/core.ts`
- `throwAssertError` (function, panics_and_aborts, primitive): 9 call sites in 1 files -- `tests/cases/conformance/parser/ecmascript5/RealWorld/parserharness.ts`
- `reportError` (function, panics_and_aborts, primitive): 6 call sites in 1 files -- `src/harness/fourslashImpl.ts`
- `error` (function, panics_and_aborts, primitive): 5 call sites in 1 files -- `tests/cases/conformance/types/never/neverType.ts`
- `report` (function, debug_prints, primitive): 4 call sites in 1 files -- `tests/cases/compiler/APISample_linter.ts`
- `check` (function, panics_and_aborts, primitive): 3 call sites in 1 files -- `tests/cases/conformance/types/union/discriminatedUnionTypes4.ts`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesConsistentlyLargerInSize.js`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesConsistentlySmallerInSize.js`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesEqualInSize.js`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesGrowingAndShrinkingInSize.js`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesGrowingInSize.js`
- `a` (function, debug_prints, primitive): 2 call sites in 1 files -- `tests/baselines/reference/tsserver/fourslashServer/pasteEdits_multiplePastesShrinkingInSize.js`
*(+34 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 94523 call pairs -- scoped 60.1%, unique 0.0%, ambiguous 21.1%, external 18.8%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 70593 | 72.4% | 0.0% | 16.2% | 11.4% |
| javascript | 23928 | 23.7% | 0.0% | 35.6% | 40.7% |
| shell | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
