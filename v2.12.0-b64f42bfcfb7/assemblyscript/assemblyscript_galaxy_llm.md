# ARCHITECTURAL_BRIEF: assemblyscript
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/AssemblyScript/assemblyscript.git` |
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
- **Scope:** 724 analyzed artifact(s), 94800 LOC.
- **Load-bearing artifact:** `src/common.ts` -- 17 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/index-js.ts` -- pulls in 16 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/compiler.ts` at magnitude 8186.14 (structural weight, not risk).
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
| Total Artifacts | 1274 |
| Analyzed Artifacts (Scanned) | 724 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 550 |
| Total LOC | 94800 |
| Volatility Index | 0.003 |
| % Scanned of codebase = | 56.8% |
| Dominant Lang | TYPESCRIPT |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6552 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | 0.2011 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 2.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3472 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 40 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| TYPESCRIPT | 455 | 83064 | 62.8% |
| JSON | 151 | 1900 | 20.9% |
| JAVASCRIPT | 66 | 9231 | 9.1% |
| PLAINTEXT | 23 | 1 | 3.2% |
| MARKDOWN | 16 | 0 | 2.2% |
| YAML | 8 | 315 | 1.1% |
| HTML | 3 | 287 | 0.4% |
| XML | 2 | 2 | 0.3% |

## 4.1 SOURCE ENCODINGS
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 723 |
| unknown | unknown | 1 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Data / Markup / Trivial 47%, Declarative / Non-Code 12%, Parameter Forwarders Files 10%, Interface Declarations Files 7%, State Mutators Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 684 | 94.5% |
| Unknown | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 38 | 5.2% |
| Static: Minified & Vendor Opaque Mass | 1 | 0.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 550*

**Composition by Extension & Reason:**
- `.wat`: 381x Excluded (Unsupported Extension: '.wat')
- `.json`: 112x Excluded: Neighborhood Micro-Mass Limit Exceeded, 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Static Asset Blob without Intent: 1356 LOC)
- `.ts`: 19x Excluded: Neighborhood Micro-Mass Limit Exceeded, 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 53, Signals: 0)
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 542 LOC), 1x Excluded (Machine-Generated Source Code Signature: 391 LOC)
- `.wasm`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 2x Excluded (Explicitly Denied Extension: '.png')
- `.cjs`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.xml`: 1x Excluded (Saturation: Line 1 exceeds 500 chars)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.4 | 8.0 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 96.5 | 18.9 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 6.9 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 9.8 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 2.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 4.3 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 2.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 43.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 623 | 53 | 0 | `src/compiler.ts` |
| cleanup | 3 | 3 | 0 | `bin/asinit.js` |
| guards | 1351 | 103 | 3 | `cli/index.js` |
| danger | 724 | 96 | 1 | `std/assembly/index.d.ts` |
| concurrency | 213 | 32 | 0 | `cli/index.js` |
| connectivity | 5982 | 277 | 10 | `src/glue/binaryen.d.ts` |
| io | 324 | 47 | 0 | `bin/asinit.js` |
| crypto | 0 | 0 | 0 | - |
| ipc | 10 | 4 | 0 | `tests/compiler.js` |
| time | 73 | 15 | 0 | `tests/compiler/std/date.ts` |
| serialization | 28 | 10 | 0 | `bin/asinit.js` |
| regex | 101 | 17 | 0 | `tests/compiler/std/string.ts` |
| events | 125 | 18 | 0 | `eslint.config.js` |
| tests | 7745 | 175 | 10 | `tests/compiler/std/math.ts` |
| docs | 4697 | 108 | 2 | `std/assembly/index.d.ts` |
| debt | 1117 | 118 | 2 | `std/assembly/index.d.ts` |
| mutation | 27902 | 364 | 55 | `src/builtins.ts` |
| dead_code | 2070 | 176 | 4 | `src/glue/binaryen.d.ts` |
| credential | 5 | 2 | 0 | `tests/compiler/std/string-casemapping.ts` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 68 | 11 | 0 | `std/assembly/bindings/dom.ts` |
| ui | 538 | 22 | 0 | `src/compiler.ts` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `bin/asinit.js` (Hits: 44)
- `cli/index.js` (Hits: 30)
- `src/util/path.ts` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **common.ts** (`src/common.ts`) — 17 inbound connections
2. **error.ts** (`std/assembly/util/error.ts`) — 17 inbound connections
3. **ast.ts** (`src/ast.ts`) — 15 inbound connections
4. **util.ts** (`src/util.ts`) — 14 inbound connections
5. **module.ts** (`src/module.ts`) — 12 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **index-js.ts** (`src/index-js.ts`) — 16 outbound dependencies
2. **compiler.js** (`tests/compiler.js`) — 15 outbound dependencies
3. **compiler.ts** (`src/compiler.ts`) — 14 outbound dependencies
4. **program.ts** (`src/program.ts`) — 12 outbound dependencies
5. **build.js** (`scripts/build.js`) — 11 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `replaceChild` **(Many-Argument Workhorses)** (@ `src/passes/pass.ts`) -> Impact: **425.9** | LOC: 799
  * *Intent:* /** Replaces an expression within a parent expression. Returns the replaced expression on success, otherwise `0`. */
- `main` **(Many-Argument Workhorses)** (@ `cli/index.js`) -> Impact: **408.3** | LOC: 961
  * *Intent:* /** Runs the command line utility using the specified arguments array. */
- `compileBinaryExpression` **(Many-Argument Workhorses)** (@ `src/compiler.ts`) -> Impact: **347.4** | LOC: 747
- `parseClassMember` **(Many-Argument Workhorses)** (@ `src/parser.ts`) -> Impact: **296.4** | LOC: 559
- `unsafeNext` **(Many-Argument Workhorses)** (@ `src/tokenizer.ts`) -> Impact: **275.1** | LOC: 445
- `convertExpression` **(Many-Argument Workhorses)** (@ `src/compiler.ts`) -> Impact: **247.6** | LOC: 249
  * *Intent:* /** Converts an expression's result from one type to another. */
- `canOverflow` **(Many-Argument Workhorses)** (@ `src/flow.ts`) -> Impact: **225.8** | LOC: 256
  * *Intent:* /** * Tests if an expression can possibly overflow in the context of this flow. Assumes that the * expression might already have overflown and returns...
- `compileUnaryPrefixExpression` **(Many-Argument Workhorses)** (@ `src/compiler.ts`) -> Impact: **205.8** | LOC: 355
- `resolveBinaryExpression` **(Many-Argument Workhorses)** (@ `src/resolver.ts`) -> Impact: **175.8** | LOC: 207
  * *Intent:* /** Resolves a binary expression to its static type. */
- `visit` **(Compute Cores)** (@ `src/passes/pass.ts`) -> Impact: **174.4** | LOC: 603
  * *Intent:* // Delegate /** Visits any expression, delegating to the respective visitor methods. */

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 21 | 31172.11 | 23.02% | 6.94% |
| `std/assembly` | 34 | 9359.55 | 19.53% | 57.63% |
| `tests/compiler` | 227 | 5058.6 | 2.54% | 0.0% |
| `__monolith__` | 7 | 5041.28 | 0.35% | 2.24% |
| `std/assembly/util` | 10 | 3442.74 | 54.47% | 3.33% |
| `tests/compiler/bindings` | 20 | 2983.74 | 17.56% | 0.0% |
| `src/bindings` | 3 | 2818.06 | 60.28% | 20.29% |
| `tests/compiler/std` | 53 | 2355.12 | 4.01% | 0.0% |
| `src/passes` | 4 | 1720.84 | 31.47% | 16.25% |
| `cli` | 5 | 1491.69 | 20.54% | 21.58% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/workflows/test.yml` -> **100.0%** Exposure
- `lib/loader/index.d.ts` -> **100.0%** Exposure
- `lib/rtrace/index.d.ts` -> **100.0%** Exposure
- `src/glue/binaryen.d.ts` -> **100.0%** Exposure
- `src/glue/js/i64.d.ts` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `bin/asc.js` -> **100.0%** Exposure
- `cli/index.js` -> **100.0%** Exposure
- `scripts/hexfloat.js` -> **100.0%** Exposure
- `scripts/unicode-identifier.js` -> **100.0%** Exposure
- `src/glue/js/i64.js` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/glue/binaryen.d.ts` -> **797** Orphaned Functions | **0** Duplicates
- `std/assembly/index.d.ts` -> **286** Orphaned Functions | **242** Duplicates
- `std/assembly/builtins.ts` -> **0** Orphaned Functions | **196** Duplicates
- `src/glue/js/i64.d.ts` -> **47** Orphaned Functions | **0** Duplicates
- `std/portable/index.d.ts` -> **37** Orphaned Functions | **6** Duplicates

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
- **Unknown Dependencies:** `123` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/compiler.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.321)
- **Top Global Matches:** file_cluster_8: 6.321, file_cluster_6: 14.27, file_cluster_4: 22.887
- **Magnitude:** 8186.14 | **LOC:** 10689 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **14**; blast radius 2.992; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.4%)
- **Documentation Coverage:** 29.8779% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileBinaryExpression` **(Many-Argument Workhorses)** (Impact: 347.4)
  * `convertExpression` **(Many-Argument Workhorses)** (Impact: 247.6)
    * *Intent:* /** Converts an expression's result from one type to another. */
  * `compileUnaryPrefixExpression` **(Many-Argument Workhorses)** (Impact: 205.8)
  * `makePow` **(Many-Argument Workhorses)** (Impact: 145.9)
  * `compileIdentifierExpression` **(Many-Argument Workhorses)** (Impact: 137.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 983 instances
* *State Mutation (weighted view):* 3131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2162`, `structural_boundaries: 2394`, `args: 156`, `func_start: 156`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 8`, `high_risk_execution: 3`, `state_mutation: 1165`, `dead_code: 12`, `planned_debt: 78`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 21`, `import: 14`
* *Defense:* `doc: 236`, `test: 231`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.992
  * `Choke Point (Betweenness):` 0.000346 | `Ripple Effect (Closeness):` 0.019072
  * `Imports (Out-Degree: 18):` ast, js, builtins, common, diagnostics, flow, module, rtrace...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/builtins.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.94)
- **Top Global Matches:** file_cluster_4: 7.94, file_cluster_15: 10.644, file_cluster_12: 11.443
- **Magnitude:** 6975.3 | **LOC:** 11395 | **CtrlFlow:** 15.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **10**; blast radius 2.648; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (70.4%)
- **Documentation Coverage:** 53.7989% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `builtin_assert` **(Compute Cores)** (Impact: 122.6)
    * *Intent:* // assert<T?>(isTrueish: T, message?: string) -> T{!= null}
  * `builtin_v128_shuffle` **(Compute Cores)** (Impact: 46.5)
    * *Intent:* // v128.shuffle<T!>(a: v128, b: v128, ...lanes: u8[]) -> v128
  * `ensureVisitMembersOf` **(Many-Argument Workhorses)** (Impact: 43.2)
    * *Intent:* /** Ensures that the visitor function of the specified class is compiled. */
  * `builtin_v128_load_lane` **(Compute Cores)** (Impact: 39.5)
    * *Intent:* // v128.load_lane<TFrom!>(ptr: usize, vec: v128, idx: u8, immOffset?: usize, immAlign?: usize) -> v1...
  * `builtin_v128_store_lane` **(Compute Cores)** (Impact: 39.5)
    * *Intent:* // v128.store_lane<TFrom!>(ptr: usize, vec: v128, idx: u8, immOffset?: usize, immAlign?: usize) -> v...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 403 instances
* *State Mutation (weighted view):* 2677
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1497`, `structural_boundaries: 3768`, `args: 620`, `func_start: 616`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 56`, `state_mutation: 1871`, `planned_debt: 11`, `fragile_debt: 1`
* *Architecture:* `api: 638`, `import: 10`
* *Defense:* `doc: 35`, `test: 44`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.648
  * `Choke Point (Betweenness):` 6.3e-05 | `Ripple Effect (Closeness):` 0.01746
  * `Imports (Out-Degree: 12):` ast, common, compiler, diagnostics, flow, module, program, resolver...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `.npmrc` (PLAINTEXT | Tier 0 | AI Safe: 0.0%)
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
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `std/assembly/math.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.089)
- **Top Global Matches:** file_cluster_6: 6.089, file_cluster_4: 9.677, file_cluster_8: 15.801
- **Magnitude:** 3645.34 | **LOC:** 3290 | **CtrlFlow:** 24.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 8.921; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (81.3%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (69.8%)
- **Documentation Coverage:** 95.3368% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pow` **(Many-Argument Workhorses)** (Impact: 137.3)
  * `atan2` **(Compute Cores)** (Impact: 54.2)
  * `atan2` **(Compute Cores)** (Impact: 54.1)
  * `rem` **(Compute Cores)** (Impact: 48.4)
  * `rem` **(Compute Cores)** (Impact: 48.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 575 instances
* *State Mutation (weighted view):* 2079
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 696`, `structural_boundaries: 494`, `args: 107`, `func_start: 107`
* *Risk/State:* `state_mutation: 929`, `dead_code: 14`, `planned_debt: 6`
* *Architecture:* `api: 109`, `import: 3`
* *Defense:* `doc: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.921
  * `Choke Point (Betweenness):` 0.000111 | `Ripple Effect (Closeness):` 0.012705
  * `Imports (Out-Degree: 3):` dom, builtins, math
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.639)
- **Top Global Matches:** file_cluster_8: 5.639, file_cluster_6: 15.641, file_cluster_3: 21.244
- **Magnitude:** 3321.08 | **LOC:** 4588 | **CtrlFlow:** 25.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 1.556; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (63.0%), Complexity Load (formerly Cognitive Load) (51.6%)
- **Documentation Coverage:** 41.1456% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseClassMember` **(Many-Argument Workhorses)** (Impact: 296.4)
  * `parseExpressionStart` **(Compute Cores)** (Impact: 158.1)
    * *Intent:* // expressions
  * `parseExpression` **(Many-Argument Workhorses)** (Impact: 144.3)
  * `parseType` **(Many-Argument Workhorses)** (Impact: 133.9)
    * *Intent:* /** Parses a type. */
  * `parseTopLevelStatement` **(Many-Argument Workhorses)** (Impact: 130.2)
    * *Intent:* /** Parses a top-level statement. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 367 instances
* *State Mutation (weighted view):* 1120
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1055`, `structural_boundaries: 505`, `args: 63`, `func_start: 63`, `class_start: 3`
* *Risk/State:* `state_mutation: 386`, `planned_debt: 5`
* *Architecture:* `io: 17`, `api: 9`, `import: 5`
* *Defense:* `safety: 2`, `doc: 28`, `test: 17`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.556
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.015893
  * `Imports (Out-Degree: 6):` ast, common, diagnostics, tokenizer, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/program.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.35)
- **Top Global Matches:** file_cluster_4: 8.35, file_cluster_15: 10.617, file_cluster_16: 10.956
- **Magnitude:** 3105.08 | **LOC:** 5125 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **12**; blast radius 5.044; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (59.9%)
- **Documentation Coverage:** 1.9033% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initialize` **(I/O & Config Routines)** (Impact: 137.8)
    * *Intent:* /** Initializes the program and its elements prior to compilation. */
  * `fromDecorator` **(Compute Cores)** (Impact: 107.8)
    * *Intent:* /** Returns the operator kind represented by the specified decorator and string argument. */
  * `doProcessOverride` **(Many-Argument Workhorses)** (Impact: 72.6)
    * *Intent:* /** Processes a single overridden member by this class in a base class. */
  * `writeField` **(Many-Argument Workhorses)** (Impact: 61.6)
    * *Intent:* /** Writes a field value to a buffer and returns the number of bytes written. */
  * `tryMerge` **(Many-Argument Workhorses)** (Impact: 60.3)
    * *Intent:* /** Attempts to merge two elements. Returns the merged element on success. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 306 instances
* *State Mutation (weighted view):* 995
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 856`, `structural_boundaries: 660`, `args: 226`, `func_start: 226`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 2`, `state_mutation: 383`, `dead_code: 6`, `planned_debt: 27`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 1`, `api: 123`, `import: 33`
* *Defense:* `doc: 524`, `test: 99`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.044
  * `Choke Point (Betweenness):` 0.000295 | `Ripple Effect (Closeness):` 0.022539
  * `Imports (Out-Degree: 13):` ast, builtins, common, compiler, diagnostics, flow, module, parser...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/resolver.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.43)
- **Top Global Matches:** file_cluster_8: 6.43, file_cluster_6: 11.941, file_cluster_4: 20.516
- **Magnitude:** 2633.52 | **LOC:** 3716 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **9**; blast radius 1.885; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (63.1%), Guard Balance (formerly Safety Score) (57.2%)
- **Documentation Coverage:** 3.5687% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveBinaryExpression` **(Many-Argument Workhorses)** (Impact: 175.8)
    * *Intent:* /** Resolves a binary expression to its static type. */
  * `finishResolveClass` **(Many-Argument Workhorses)** (Impact: 145.2)
    * *Intent:* /** Finishes resolving the specified class. */
  * `resolveFunction` **(Many-Argument Workhorses)** (Impact: 131.2)
    * *Intent:* // ==================================================== Elements ===================================...
  * `lookupPropertyAccessExpression` **(Many-Argument Workhorses)** (Impact: 130.7)
    * *Intent:* /** Looks up the program element the specified property access expression refers to. */
  * `resolveNamedType` **(Many-Argument Workhorses)** (Impact: 114.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 187 instances
* *State Mutation (weighted view):* 571
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 764`, `structural_boundaries: 517`, `args: 58`, `func_start: 58`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 197`, `dead_code: 5`, `planned_debt: 8`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `doc: 275`, `test: 75`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.885
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.016311
  * `Imports (Out-Degree: 11):` ast, builtins, common, diagnostics, flow, program, tokenizer, types...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/module.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.651)
- **Top Global Matches:** file_cluster_15: 6.651, file_cluster_11: 8.334, file_cluster_16: 8.569
- **Magnitude:** 2136.5 | **LOC:** 4010 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **6**; blast radius 5.141; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (99.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (57.8%)
- **Documentation Coverage:** 53.4038% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `optimize` **(Many-Argument Workhorses)** (Impact: 124.9)
  * `binary` **(Compute Cores)** (Impact: 109.9)
  * `prepareType` **(Many-Argument Workhorses)** (Impact: 74.3)
    * *Intent:* /** Recursively prepares the given GC type, potentially returning a temporary type. */
  * `tryEnsureBasicType` **(Compute Cores)** (Impact: 40.5)
    * *Intent:* /** Obtains the basic type of the given type, if any. */
  * `leastUpperBound` **(Compute Cores)** (Impact: 38.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 180 instances
* *State Mutation (weighted view):* 599
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 733`, `args: 247`, `func_start: 249`, `class_start: 25`
* *Risk/State:* `state_mutation: 239`, `dead_code: 5`, `planned_debt: 9`, `fragile_debt: 4`
* *Architecture:* `api: 283`, `import: 6`
* *Defense:* `safety: 1`, `doc: 507`, `test: 25`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.141
  * `Choke Point (Betweenness):` 0.000189 | `Ripple Effect (Closeness):` 0.021374
  * `Imports (Out-Degree: 7):` builtins, common, binaryen, program, types, util
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `std/assembly/builtins.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 8.582)
- **Top Global Matches:** file_cluster_0: 8.582, file_cluster_13: 10.079, file_cluster_15: 10.84
- **Magnitude:** 2119.18 | **LOC:** 2632 | **CtrlFlow:** 14.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **1**; blast radius 10.257; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.0%)
- **Documentation Coverage:** 99.9127% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `trace` **(Many-Argument Workhorses)** (Impact: 20.2)
  * `abort` **(Compute Cores)** (Impact: 11.5)
  * `load_lane` **(Generic / Templated Code)** (Impact: 7.4)
  * `store_lane` **(Generic / Templated Code)** (Impact: 7.4)
  * `load8_lane` **(Compute Cores)** (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 1281`, `args: 574`, `func_start: 574`, `class_start: 2`
* *Risk/State:* `state_mutation: 1`, `fragile_debt: 1`, `duplicate_logic: 196`
* *Architecture:* `api: 644`, `import: 1`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.257
  * `Choke Point (Betweenness):` 6.1e-05 | `Ripple Effect (Closeness):` 0.017418
  * `Imports (Out-Degree: 1):` string
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/bindings/js.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.299)
- **Top Global Matches:** file_cluster_6: 6.299, file_cluster_8: 11.208, file_cluster_4: 13.62
- **Magnitude:** 2037.98 | **LOC:** 1607 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **8**; blast radius 5.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (87.0%), Guard Balance (formerly Safety Score) (85.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 68.4211% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `build` **(I/O & Config Routines)** (Impact: 137.3)
  * `makeLowerToValue` **(Many-Argument Workhorses)** (Impact: 109.5)
    * *Intent:* /** Lowers a JavaScript value to a WebAssembly value, as an expression. */
  * `makeLiftFromValue` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /** Lifts a WebAssembly value to a JavaScript value, as an expression. */
  * `makeFunctionImport` **(Many-Argument Workhorses)** (Impact: 40.2)
  * `visitFunction` **(Many-Argument Workhorses)** (Impact: 37.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 6 instances
* *Amplified Cascading Flux:* 386 instances
* *Concurrency (weighted view):* 39
* *State Mutation (weighted view):* 1291
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 339`, `structural_boundaries: 227`, `args: 60`, `func_start: 53`, `class_start: 2`
* *Risk/State:* `state_mutation: 519`, `dead_code: 7`, `planned_debt: 5`
* *Architecture:* `io: 2`, `api: 36`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 6`, `doc: 13`, `test: 13`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.18
  * `Choke Point (Betweenness):` 0.000408 | `Ripple Effect (Closeness):` 0.015692
  * `Imports (Out-Degree: 8):` ast, common, compiler, program, types, util, util, promises
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/tokenizer.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.328)
- **Top Global Matches:** file_cluster_6: 6.328, file_cluster_8: 12.422, file_cluster_4: 12.969
- **Magnitude:** 1563.72 | **LOC:** 1798 | **CtrlFlow:** 31.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **4**; blast radius 2.956; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%), Guard Balance (formerly Safety Score) (67.4%)
- **Documentation Coverage:** 52.9473% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `unsafeNext` **(Many-Argument Workhorses)** (Impact: 275.1)
  * `tokenFromKeyword` **(Compute Cores)** (Impact: 147.1)
  * `operatorTokenToString` **(Compute Cores)** (Impact: 74.9)
  * `readEscapeSequence` **(Compute Cores)** (Impact: 43.9)
  * `tokenIsAlsoIdentifier` **(Compute Cores)** (Impact: 30.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 200 instances
* *State Mutation (weighted view):* 625
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 524`, `structural_boundaries: 340`, `args: 37`, `func_start: 36`, `class_start: 5`
* *Risk/State:* `state_mutation: 225`, `dead_code: 5`, `planned_debt: 1`
* *Architecture:* `api: 27`, `concurrency: 2`, `import: 3`
* *Defense:* `safety: 3`, `doc: 11`, `test: 5`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.956
  * `Choke Point (Betweenness):` 4e-06 | `Ripple Effect (Closeness):` 0.01937
  * `Imports (Out-Degree: 4):` ) return Token.Import;
          break;
        
        case CharCode.t: 
          if (text ==, ast, diagnostics, util
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/extra/ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.988)
- **Top Global Matches:** file_cluster_4: 7.988, file_cluster_15: 8.909, file_cluster_0: 9.96
- **Magnitude:** 1459.78 | **LOC:** 1631 | **CtrlFlow:** 20.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 1.226; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (72.9%), Complexity Load (formerly Cognitive Load) (68.1%)
- **Documentation Coverage:** 97.4359% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `visitNode` **(Type Conversions)** (Impact: 104.4)
  * `visitClassDeclaration` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `visitFunctionCommon` **(Compute Cores)** (Impact: 35.0)
  * `visitInterfaceDeclaration` **(Compute Cores)** (Impact: 19.4)
  * `serializeAccessModifiers` **(Stateful Encapsulated Methods)** (Impact: 16.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 247 instances
* *State Mutation (weighted view):* 780
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 212`, `args: 77`, `func_start: 75`, `class_start: 1`
* *Risk/State:* `state_mutation: 286`
* *Architecture:* `io: 5`, `api: 13`, `import: 4`
* *Defense:* `safety: 3`, `doc: 3`, `test: 17`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.226
  * `Choke Point (Betweenness):` 1e-06 | `Ripple Effect (Closeness):` 0.002449
  * `Imports (Out-Degree: 5):` );
     else if (node.is(CommonFlags.Declare)) 
      sb.push(, );
    let declarations = node.declarations;
    let namespaceName = node.namespaceName;
    if (declarations) 
      let numDeclarations = declarations.length;
      if (numDeclarations) 
        sb.push(, );
    this.visitIdentifierExpression(node.externalName);
    sb.push(, ast, common, tokenizer, util
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `cli/index.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.046)
- **Top Global Matches:** file_cluster_4: 8.046, file_cluster_12: 11.05, file_cluster_6: 11.835
- **Magnitude:** 1450.7 | **LOC:** 1291 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 1.084; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (84.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 41.9739% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 408.3)
    * *Intent:* /** Runs the command line utility using the specified arguments array. */
  * `getFile` **(Compute Cores)** (Impact: 52.1)
    * *Intent:* // Gets the file matching the specified source path, imported at the given dependee path
  * `checkDiagnostics` **(Many-Argument Workhorses)** (Impact: 43.7)
    * *Intent:* /** Checks diagnostics emitted so far for errors. */
  * `getConfig` **(Defensive Guards)** (Impact: 26.1)
  * `configToArguments` **(Defensive Guards)** (Impact: 14.6)
    * *Intent:* /** Converts a configuration object to an arguments array. */
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 36 instances
* *Amplified Cascading Flux:* 170 instances
* *Concurrency (weighted view):* 222
* *State Mutation (weighted view):* 542
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 257`, `structural_boundaries: 279`, `args: 52`, `func_start: 34`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 28`, `high_risk_execution: 1`, `state_mutation: 202`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `io: 30`, `api: 16`, `concurrency: 42`, `import: 12`
* *Defense:* `safety: 102`, `doc: 16`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` binaryen.js, node.js, options.js, terminal.js, text.js, index.generated.js, index.js, assemblyscript
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/passes/pass.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.596)
- **Top Global Matches:** file_cluster_15: 6.596, file_cluster_11: 8.034, file_cluster_16: 8.533
- **Magnitude:** 1278.54 | **LOC:** 2121 | **CtrlFlow:** 16.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 1.724; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (63.0%), Guard Balance (formerly Safety Score) (60.1%)
- **Documentation Coverage:** 83.1776% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `replaceChild` **(Many-Argument Workhorses)** (Impact: 425.9)
    * *Intent:* /** Replaces an expression within a parent expression. Returns the replaced expression on success, o...
  * `visit` **(Compute Cores)** (Impact: 174.4)
    * *Intent:* // Delegate /** Visits any expression, delegating to the respective visitor methods. */
  * `replaceCurrent` **(Compute Cores)** (Impact: 6.3)
    * *Intent:* // Utility /** Replaces the current expression with the specified replacement. */
  * `walkFunction` **(Compute Cores)** (Impact: 3.2)
    * *Intent:* /** Walks a specific function. */
  * `walkGlobal` **(Parameter Forwarders)** (Impact: 3.1)
    * *Intent:* /** Walks a specific global variable. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 155 instances
* *State Mutation (weighted view):* 465
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 304`, `structural_boundaries: 362`, `args: 97`, `func_start: 97`, `class_start: 2`
* *Risk/State:* `state_mutation: 155`
* *Architecture:* `api: 12`, `import: 1`
* *Defense:* `doc: 20`, `test: 66`, `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.724
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01078
  * `Imports (Out-Degree: 2):` binaryen, module
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/flow.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.019)
- **Top Global Matches:** file_cluster_4: 7.019, file_cluster_6: 8.034, file_cluster_15: 14.067
- **Magnitude:** 1252.04 | **LOC:** 1480 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **9**; blast radius 2.03; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (64.7%), Connectivity (formerly Api Exposure) (62.0%)
- **Documentation Coverage:** 6.4237% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `canOverflow` **(Many-Argument Workhorses)** (Impact: 225.8)
    * *Intent:* /** * Tests if an expression can possibly overflow in the context of this flow. Assumes that the * e...
  * `inheritAlternatives` **(Many-Argument Workhorses)** (Impact: 102.4)
    * *Intent:* /** Inherits two alternate branches to become this flow, i.e. then with else. */
  * `inheritNonnullIfTrue` **(Many-Argument Workhorses)** (Impact: 78.3)
    * *Intent:* /** Updates local states to reflect that this branch is only taken when `expr` is true-ish. */
  * `inheritNonnullIfFalse` **(Compute Cores)** (Impact: 65.1)
    * *Intent:* /** Updates local states to reflect that this branch is only taken when `expr` is false-ish. */
  * `mergeSideEffects` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* /** Merges only the side effects of a branch, i.e. when not taken. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 135 instances
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 390`, `structural_boundaries: 203`, `args: 49`, `func_start: 49`, `class_start: 5`
* *Risk/State:* `state_mutation: 150`, `dead_code: 2`, `planned_debt: 3`
* *Architecture:* `api: 36`, `import: 9`
* *Defense:* `doc: 104`, `test: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.03
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.016529
  * `Imports (Out-Degree: 10):` ast, builtins, common, compiler, diagnostics, module, program, types...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/ast.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 8.847)
- **Top Global Matches:** file_cluster_15: 8.847, file_cluster_0: 9.109, file_cluster_11: 9.881
- **Magnitude:** 1030.82 | **LOC:** 2420 | **CtrlFlow:** 6.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **6**; blast radius 5.635; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.1%), Mutation Surface (formerly State Flux) (41.9%)
- **Documentation Coverage:** 26.3275% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromNode` **(Compute Cores)** (Impact: 53.0)
  * `hasGenericComponent` **(Compute Cores)** (Impact: 27.0)
    * *Intent:* /** Tests if this type has a generic component matching one of the given type parameters. */
  * `lineAt` **(Compute Cores)** (Impact: 15.5)
    * *Intent:* /** Determines the line number at the specified position. Starts at `1`. */
  * `constructor` **(Many-Argument Workhorses)** (Impact: 14.6)
  * `compilesToConst` **(Compute Cores)** (Impact: 10.8)
    * *Intent:* /** Tests whether this node is guaranteed to compile to a constant value. */
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 27 instances
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 442`, `args: 187`, `func_start: 187`, `class_start: 89`
* *Risk/State:* `state_mutation: 37`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 21`, `api: 319`, `import: 6`
* *Defense:* `doc: 413`, `test: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.635
  * `Choke Point (Betweenness):` 0.000193 | `Ripple Effect (Closeness):` 0.025299
  * `Imports (Out-Degree: 7):` common, diagnostics, module, tokenizer, types, util
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `std/assembly/typedarray.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 9.936)
- **Top Global Matches:** file_cluster_0: 9.936, file_cluster_15: 12.728, file_cluster_16: 12.81
- **Magnitude:** 922.44 | **LOC:** 1946 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 2.006; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (95.9%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.3%), Guard Balance (formerly Safety Score) (53.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SET` **(Generic / Templated Code)** (Impact: 49.0)
  * `INCLUDES` **(Generic / Templated Code)** (Impact: 19.1)
  * `WRAP` **(Generic / Templated Code)** (Impact: 17.6)
  * `LAST_INDEX_OF` **(Generic / Templated Code)** (Impact: 14.8)
  * `INDEX_OF` **(Generic / Templated Code)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 40 instances
* *State Mutation (weighted view):* 121
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 102`, `structural_boundaries: 575`, `args: 336`, `func_start: 341`, `class_start: 11`
* *Risk/State:* `state_mutation: 41`, `duplicate_logic: 35`
* *Architecture:* `api: 11`, `import: 6`
* *Defense:* `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.006
  * `Choke Point (Betweenness):` 2.3e-05 | `Ripple Effect (Closeness):` 0.001377
  * `Imports (Out-Degree: 6):` arraybuffer, builtins, bytes, error, sort, string
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `std/assembly/util/string.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.775)
- **Top Global Matches:** file_cluster_4: 6.775, file_cluster_9: 10.691, file_cluster_15: 10.966
- **Magnitude:** 782.0 | **LOC:** 1203 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **2**; blast radius 18.544; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.8%), Connectivity (formerly Api Exposure) (62.7%)
- **Documentation Coverage:** 95.6522% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `strtol` **(Many-Argument Workhorses)** (Impact: 71.7)
    * *Intent:* /** Parses a string to an integer (usually), using the specified radix. */
  * `strtod` **(Compute Cores)** (Impact: 51.8)
  * `joinIntegerArray` **(Generic / Templated Code)** (Impact: 28.4)
  * `parseExp` **(Compute Cores)** (Impact: 24.0)
    * *Intent:* // Adopted from metallic lib: // https://github.com/jdh8/metallic/blob/master/src/stdlib/parse/scien...
  * `scientific` **(Compute Cores)** (Impact: 23.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 113 instances
* *State Mutation (weighted view):* 351
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 181`, `structural_boundaries: 117`, `args: 27`, `func_start: 27`, `class_start: 1`
* *Risk/State:* `state_mutation: 125`
* *Architecture:* `api: 20`, `import: 2`
* *Defense:* `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 18.544
  * `Choke Point (Betweenness):` 0.000209 | `Ripple Effect (Closeness):` 0.018303
  * `Imports (Out-Degree: 2):` math, number
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `std/assembly/util/number.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.756)
- **Top Global Matches:** file_cluster_4: 7.756, file_cluster_0: 9.68, file_cluster_15: 10.353
- **Magnitude:** 714.12 | **LOC:** 874 | **CtrlFlow:** 20.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 10.304; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.9%), Guard Balance (formerly Safety Score) (69.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genDigits` **(Many-Argument Workhorses)** (Impact: 56.6)
  * `itoa_buffered` **(Many-Argument Workhorses)** (Impact: 36.8)
  * `prettify` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `itoa64` **(Generic / Templated Code)** (Impact: 22.4)
  * `utoa64` **(Generic / Templated Code)** (Impact: 18.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 97 instances
* *State Mutation (weighted view):* 303
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 147`, `structural_boundaries: 92`, `args: 33`, `func_start: 33`
* *Risk/State:* `state_mutation: 109`, `dead_code: 1`
* *Architecture:* `api: 12`, `import: 2`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.304
  * `Choke Point (Betweenness):` 1.6e-05 | `Ripple Effect (Closeness):` 0.013011
  * `Imports (Out-Degree: 2):` builtins, string
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `std/assembly/string.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.141)
- **Top Global Matches:** file_cluster_4: 8.141, file_cluster_0: 9.257, file_cluster_15: 10.841
- **Magnitude:** 655.36 | **LOC:** 848 | **CtrlFlow:** 23.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 1.084; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.2%), Complexity Load (formerly Cognitive Load) (63.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encodeUnsafe` **(Many-Argument Workhorses)** (Impact: 37.0)
  * `split` **(Generic / Templated Code)** (Impact: 30.4)
  * `replaceAll` **(Many-Argument Workhorses)** (Impact: 30.2)
  * `decodeUnsafe` **(Many-Argument Workhorses)** (Impact: 30.1)
  * `toLowerCase` **(I/O & Config Routines)** (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 78 instances
* *State Mutation (weighted view):* 240
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 174`, `structural_boundaries: 151`, `args: 45`, `func_start: 45`, `class_start: 2`
* *Risk/State:* `state_mutation: 84`, `planned_debt: 2`
* *Architecture:* `api: 46`, `import: 6`
* *Defense:* `test: 2`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` array, builtins, common, casemap, error, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bindings/tsd.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.847)
- **Top Global Matches:** file_cluster_4: 5.847, file_cluster_15: 9.029, file_cluster_16: 9.852
- **Magnitude:** 620.5 | **LOC:** 416 | **CtrlFlow:** 22.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 1.77; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (88.1%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (59.8%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `toTypeScriptType` **(Compute Cores)** (Impact: 85.9)
  * `visitFunction` **(Compute Cores)** (Impact: 14.4)
  * `build` **(Compute Cores)** (Impact: 14.1)
  * `makeRecordType` **(Compute Cores)** (Impact: 13.6)
  * `isPlainObject` **(Compute Cores)** (Impact: 12.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 130 instances
* *Concurrency (weighted view):* 6
* *State Mutation (weighted view):* 408
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 85`, `structural_boundaries: 99`, `args: 20`, `func_start: 20`, `class_start: 2`
* *Risk/State:* `state_mutation: 148`, `planned_debt: 1`
* *Architecture:* `api: 20`, `concurrency: 1`, `import: 6`
* *Defense:* `doc: 14`, `test: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.77
  * `Choke Point (Betweenness):` 2.8e-05 | `Ripple Effect (Closeness):` 0.003306
  * `Imports (Out-Degree: 7):` ast, common, program, types, util, util
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `std/assembly/util/math.ts` (TYPESCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.107)
- **Top Global Matches:** file_cluster_4: 6.107, file_cluster_15: 10.308, file_cluster_9: 10.907
- **Magnitude:** 618.14 | **LOC:** 1923 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 3.594; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.2%), Connectivity (formerly Api Exposure) (40.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pow_lut` **(Compute Cores)** (Impact: 41.4)
  * `powf_lut` **(Compute Cores)** (Impact: 37.2)
  * `exp2_lut` **(Compute Cores)** (Impact: 18.1)
  * `exp_inline` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* // Computes sign*exp(x+xtail) where |xtail| < 2^-8/N and |xtail| <= |x|. // The sign_bias argument i...
  * `log2_lut` **(I/O & Config Routines)** (Impact: 15.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 63 instances
* *State Mutation (weighted view):* 325
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 103`, `args: 26`, `func_start: 26`
* *Risk/State:* `state_mutation: 199`, `dead_code: 26`
* *Architecture:* `api: 10`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.594
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.010161
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `util/browser/path.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 10.806)
- **Top Global Matches:** file_cluster_8: 10.806, file_cluster_3: 15.268, file_cluster_6: 22.692
- **Magnitude:** 615.08 | **LOC:** 521 | **CtrlFlow:** 45.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **1**; blast radius 3.251; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (92.2%), Connectivity (formerly Api Exposure) (66.6%), Guard Balance (formerly Safety Score) (60.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `normalizeStringPosix` **(Defensive Guards)** (Impact: 60.4)
    * *Intent:* // Resolves . and .. elements in a path with directory names
  * `relative` **(Defensive Guards)** (Impact: 58.2)
  * `basename` **(Defensive Guards)** (Impact: 50.3)
  * `parse` **(Defensive Guards)** (Impact: 47.6)
  * `extname` **(Defensive Guards)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 93 instances
* *State Mutation (weighted view):* 279
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 177`, `structural_boundaries: 124`, `args: 13`, `func_start: 13`
* *Risk/State:* `state_mutation: 93`
* *Architecture:* `api: 13`, `import: 2`
* *Defense:* `safety: 98`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.251
  * `Choke Point (Betweenness):` 2e-06 | `Ripple Effect (Closeness):` 0.00684
  * `Imports (Out-Degree: 1):` process.js
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `tests/compiler/bindings/esm.debug.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_12: 6.526, file_cluster_15: 9.04, file_cluster_7: 9.825
- **Magnitude:** 600.22 | **LOC:** 562 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.084; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (44.2%), Concurrency Surface (formerly Concurrency) (33.3%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instantiate` **(Defensive Guards)** (Impact: 137.0)
  * `__lowerStaticArray` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `__lowerRecord13` **(Compute Cores)** (Impact: 9.7)
  * `arrayOfStringsFunction` **(Defensive Guards)** (Impact: 9.2)
  * `__release` **(Defensive Guards)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 108`, `args: 71`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/compiler/bindings/esm.release.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.526)
- **Top Global Matches:** file_cluster_12: 6.526, file_cluster_15: 9.04, file_cluster_7: 9.825
- **Magnitude:** 600.22 | **LOC:** 562 | **CtrlFlow:** 12.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.084; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (60.4%), Complexity Load (formerly Cognitive Load) (44.2%), Concurrency Surface (formerly Concurrency) (33.3%), Connectivity (formerly Api Exposure) (12.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `instantiate` **(Defensive Guards)** (Impact: 137.0)
  * `__lowerStaticArray` **(Many-Argument Workhorses)** (Impact: 12.9)
  * `__lowerRecord13` **(Compute Cores)** (Impact: 9.7)
  * `arrayOfStringsFunction` **(Defensive Guards)** (Impact: 9.2)
  * `__release` **(Defensive Guards)** (Impact: 8.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 185
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 68`, `structural_boundaries: 108`, `args: 71`, `func_start: 59`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 77`, `duplicate_logic: 3`, `unreferenced_by_name: 2`
* *Architecture:* `io: 2`, `api: 44`, `concurrency: 9`, `import: 1`
* *Defense:* `safety: 53`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 1.084
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` promises
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `tests/compiler/std/arraybuffer.ts` (TYPESCRIPT) | Magnitude: 23.7 | Delta: **0.001** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 31, test: 21, core_var_decl: 11, design_snake_case: 11
- `tests/compiler/constructor-errors.ts` (TYPESCRIPT) | Magnitude: 19.96 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, core_var_decl: 11, design_snake_case: 11, structural_boundaries: 10
- `tests/compiler/call-super.ts` (TYPESCRIPT) | Magnitude: 13.26 | Delta: **0.126** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 43, structural_boundaries: 25, test: 16, core_var_decl: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `tests/compiler/typeof.ts` (TYPESCRIPT) | Magnitude: 5.18 | Delta: **0.064** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: test: 24, structural_boundaries: 16, core_var_decl: 9, design_short_vars: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `tests/compiler/exports-lazy.ts` (TYPESCRIPT) | Magnitude: 6.32 | Delta: **0.091** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, api: 4, decorators: 4, args: 2
- `util/web.js` (JAVASCRIPT) | Magnitude: 10.22 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 22, structural_boundaries: 11, args: 6, io: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `scripts/build.js` (JAVASCRIPT) | Magnitude: 94.96 | Delta: **0.124** (centroid distance) | Secondary Pull: `file_cluster_10`
  * Top Architectural Signatures: indent_spaces: 198, structural_boundaries: 47, core_var_decl: 46, design_snake_case: 27
- `tests/browser.js` (JAVASCRIPT) | Magnitude: 40.82 | Delta: **0.154** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 40, bitwise_ops: 22, debug_prints: 19, structural_boundaries: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/glue/wasm/i64.ts` (TYPESCRIPT) | Magnitude: 166.34 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: decorators: 98, indent_spaces: 61, structural_boundaries: 51, args: 47
- `util/terminal.d.ts` (TYPESCRIPT) | Magnitude: 1.3 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 23, structural_boundaries: 13, api: 12, indent_spaces: 10
- `tests/parser/string-binding.ts` (TYPESCRIPT) | Magnitude: 23.9 | Delta: **0.131** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 32, decorators: 18, structural_boundaries: 17, args: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `tests/tokenizer.js` (JAVASCRIPT) | Magnitude: 15.58 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 18, branch: 13, core_var_decl: 7, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `tests/asconfig/index.js` (JAVASCRIPT) | Magnitude: 31.58 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 42, branch: 15, structural_boundaries: 14, core_var_decl: 13
- `src/diagnostics.ts` (TYPESCRIPT) | Magnitude: 398.08 | Delta: **0.086** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 354, core_var_decl: 77, branch: 72, state_mutation: 65

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/index-js.ts` (TYPESCRIPT) | Magnitude: 30.34 | Delta: **0.187** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 18, api: 15, import: 15

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `tests/parser.js` (JAVASCRIPT) | Magnitude: 31.62 | Delta: **0.006** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 54, core_var_decl: 19, design_snake_case: 17, structural_boundaries: 16
- `util/text.d.ts` (TYPESCRIPT) | Magnitude: 0.63 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 9, structural_boundaries: 5, api: 5, args: 4
- `util/node.js` (JAVASCRIPT) | Magnitude: 99.52 | Delta: **0.025** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 25, indent_spaces: 15, core_var_decl: 11, state_mutation: 10
- `.github/workflows/test.yml` (YAML) | Magnitude: 48.36 | Delta: **0.03** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 140, structural_boundaries: 25, func_start: 25, branch: 13
- `src/util.ts` (TYPESCRIPT) | Magnitude: 20.64 | Delta: **0.049** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: structural_boundaries: 7, api: 7, import: 7, io: 1

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/compiler.ts` -> Churn: **100.0%** | Cog Load: 52.8909% | Debt: 11.6823%
- `.github/workflows/test.yml` -> Churn: **63.25%** | Cog Load: 5.2057% | Debt: 100.0%
- `cli/index.js` -> Churn: **63.09%** | Cog Load: 84.656% | Debt: 7.9265%
- `std/portable/index.js` -> Churn: **63.09%** | Cog Load: 92.8739% | Debt: 8.6565%
- `util/text.js` -> Churn: **63.09%** | Cog Load: 76.1477% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/program.ts` -> **Changqing  Jing** (100.0% isolated ownership) | Magnitude: 3105.08
- `src/resolver.ts` -> **Changqing  Jing** (100.0% isolated ownership) | Magnitude: 2633.52
- `cli/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 1450.7
- `src/ast.ts` -> **Congcong Cai** (100.0% isolated ownership) | Magnitude: 1030.82
- `std/portable/index.js` -> **Max Graey** (100.0% isolated ownership) | Magnitude: 316.76

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bindings/js.ts` -> **Severity: 0.041** (Bridge: 0.0004 * Flux: 100.0%)
- `src/compiler.ts` -> **Severity: 0.035** (Bridge: 0.0003 * Flux: 99.9988%)
- `src/program.ts` -> **Severity: 0.029** (Bridge: 0.0003 * Flux: 99.94%)
- `util/options.js` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)
- `std/assembly/util/string.ts` -> **Severity: 0.021** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/util/text.ts` -> **Severity: 1.454** (Embedded: 0.0234 * Error Risk: 62.0562%)
- `src/diagnostics.ts` -> **Severity: 1.407** (Embedded: 0.0203 * Error Risk: 69.2542%)
- `src/common.ts` -> **Severity: 1.388** (Embedded: 0.0288 * Error Risk: 48.1005%)
- `src/program.ts` -> **Severity: 1.35** (Embedded: 0.0225 * Error Risk: 59.8853%)
- `src/bindings/js.ts` -> **Severity: 1.334** (Embedded: 0.0157 * Error Risk: 85.0411%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `std/assembly/util/string.ts` -> **Severity: 1773.774** (Blast Radius: 18.544 * Doc Risk: 95.6522%)
- `std/assembly/util/number.ts` -> **Severity: 1030.4** (Blast Radius: 10.304 * Doc Risk: 100.0%)
- `std/assembly/builtins.ts` -> **Severity: 1024.805** (Blast Radius: 10.257 * Doc Risk: 99.9127%)
- `std/assembly/math.ts` -> **Severity: 850.5** (Blast Radius: 8.921 * Doc Risk: 95.3368%)
- `std/assembly/bindings/dom.ts` -> **Severity: 775.591** (Blast Radius: 8.987 * Doc Risk: 86.3014%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 233 literal sites + 5 sites through wrappers = 238
- **`panics_and_aborts`:** 311 literal sites + 104 sites through wrappers = 415

- `__notnull` (function, panics_and_aborts, primitive): 25 call sites in 1 files -- `tests/compiler/bindings/esm.debug.js`
- `__notnull` (function, panics_and_aborts, primitive): 25 call sites in 1 files -- `tests/compiler/bindings/esm.release.js`
- `__notnull` (function, panics_and_aborts, primitive): 25 call sites in 1 files -- `tests/compiler/bindings/raw.debug.js`
- `__notnull` (function, panics_and_aborts, primitive): 25 call sites in 1 files -- `tests/compiler/bindings/raw.release.js`
- `defer` (function, debug_prints, primitive): 4 call sites in 1 files -- `tests/transform/index.js`
- `__notnull` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/compiler/bindings/noExportRuntime.debug.js`
- `__notnull` (function, panics_and_aborts, primitive): 2 call sites in 1 files -- `tests/compiler/bindings/noExportRuntime.release.js`
- `log` (function, debug_prints, primitive): 1 call sites in 1 files -- `tests/allocators/index.js`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 13447 call pairs -- scoped 52.0%, unique 0.0%, ambiguous 30.4%, external 17.7%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| typescript | 11344 | 55.8% | 0.0% | 29.8% | 14.4% |
| javascript | 2068 | 31.7% | 0.0% | 33.9% | 34.4% |
| html | 35 | 17.1% | 0.0% | 0.0% | 82.9% |

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
