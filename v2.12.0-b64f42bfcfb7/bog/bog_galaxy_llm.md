# ARCHITECTURAL_BRIEF: bog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Vexu/bog.git` |
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
- **Scope:** 35 analyzed artifact(s), 13043 LOC.
- **Load-bearing artifact:** `src/std.zig` -- 28 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/bog.zig` -- pulls in 12 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Compiler.zig` at magnitude 1284.08 (structural weight, not risk).
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
| Total Artifacts | 40 |
| Analyzed Artifacts (Scanned) | 35 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 5 |
| Total LOC | 13043 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 87.5% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1829 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5444 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 62.9% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.082 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 31 | 12937 | 88.6% |
| C | 2 | 84 | 5.7% |
| YAML | 1 | 22 | 2.9% |
| MARKDOWN | 1 | 0 | 2.9% |

## 4.1 SOURCE ENCODINGS
All 35 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 54%, Large Core Modules (3) 20%, Data / Markup / Trivial 11%, Declarative / Non-Code 6%, Type Conversions Files 6%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 34 | 97.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 2.9% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 5*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bog`: 1x Excluded (Unsupported Extension: '.bog')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.4 | 18.7 | 13.9 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 74.6 | 36.6 | 38.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 6.8 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 18.0 | 2.4 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 37.6 | 34.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 48.1 | 4.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 51.4 | 57.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.9 | 0.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 75.4 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 170 | 23 | 14 | `src/Compiler.zig` |
| cleanup | 169 | 22 | 17 | `src/Compiler.zig` |
| guards | 2184 | 28 | 218 | `src/Compiler.zig` |
| danger | 490 | 25 | 35 | `src/Compiler.zig` |
| concurrency | 28 | 6 | 4 | `src/Bytecode.zig` |
| connectivity | 385 | 29 | 30 | `src/std/math.zig` |
| io | 53 | 14 | 4 | `src/main.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `src/std/json.zig` |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `src/Gc.zig` |
| tests | 132 | 6 | 10 | `tests/behavior.zig` |
| docs | 538 | 17 | 66 | `src/Map.zig` |
| debt | 78 | 13 | 5 | `src/Bytecode.zig` |
| mutation | 3320 | 30 | 250 | `src/Compiler.zig` |
| dead_code | 16 | 5 | 1 | `src/lib.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 0 | 0 | 0 | - |
| ml_ai | 134 | 13 | 9 | `src/std/math.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **3.3023**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.5**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main.zig` (Hits: 21)
- `src/Vm.zig` (Hits: 7)
- `tests/behavior.zig` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **std.zig** (`src/std.zig`) — 28 inbound connections
2. **bog.zig** (`src/bog.zig`) — 23 inbound connections
3. **value.zig** (`src/value.zig`) — 9 inbound connections
4. **multi_array_list.zig** (`src/multi_array_list.zig`) — 4 inbound connections
5. **repl.zig** (`src/repl.zig`) — 4 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bog.zig** (`src/bog.zig`) — 12 outbound dependencies
2. **std.zig** (`src/std.zig`) — 8 outbound dependencies
3. **repl.zig** (`src/repl.zig`) — 7 outbound dependencies
4. **value.zig** (`src/value.zig`) — 5 outbound dependencies
5. **Tree.zig** (`src/Tree.zig`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `run` **(Many-Argument Workhorses)** (@ `src/Vm.zig`) -> Impact: **421.6** | LOC: 1088
  * *Intent:* /// Continues execution from current instruction pointer.
- `next` **(Many-Argument Workhorses)** (@ `src/tokenizer.zig`) -> Impact: **211.3** | LOC: 691
- `renderNode` **(Many-Argument Workhorses)** (@ `src/render.zig`) -> Impact: **128.8** | LOC: 384
- `get` **(Many-Argument Workhorses)** (@ `src/value.zig`) -> Impact: **71.2** | LOC: 82
  * *Intent:* /// Returns value in `container` at `index`.
- `MultiArrayList` **(Compute Cores)** (@ `src/multi_array_list.zig`) -> Impact: **70.0** | LOC: 410
  * *Intent:* /// A MultiArrayList stores a list of a struct type. /// Instead of storing a single list of items, MultiArrayList /// stores separate lists for each ...
- `lastToken` **(Many-Argument Workhorses)** (@ `src/Tree.zig`) -> Impact: **62.6** | LOC: 178
- `genComparison` **(Defensive Guards)** (@ `src/Compiler.zig`) -> Impact: **58.7** | LOC: 101
- `bogToZig` **(Many-Argument Workhorses)** (@ `src/value.zig`) -> Impact: **58.2** | LOC: 84
  * *Intent:* /// Converts Bog value to Zig value. Returned string is invalidated /// on next garbage collection.
- `zigFnToBog` **(Defensive Guards)** (@ `src/value.zig`) -> Impact: **49.3** | LOC: 85
- `dump` **(Defensive Guards)** (@ `src/value.zig`) -> Impact: **46.2** | LOC: 84
  * *Intent:* /// Prints string representation of value to writer

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 18 | 6856.42 | 27.65% | 10.89% |
| `src/std` | 7 | 282.52 | 12.79% | 2.24% |
| `tests` | 3 | 113.56 | 3.64% | 0.0% |
| `examples` | 2 | 35.92 | 16.25% | 0.0% |
| `__monolith__` | 3 | 35.68 | 2.16% | 6.24% |
| `include` | 1 | 33.72 | 0.0% | 0.0% |
| `.github/workflows` | 1 | 3.64 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/lib.zig` -> **99.9621%** Exposure
- `src/String.zig` -> **19.0066%** Exposure
- `build.zig` -> **18.7084%** Exposure
- `src/List.zig` -> **18.0953%** Exposure
- `src/std/fs.zig` -> **15.7052%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/tokenizer.zig` -> **99.9994%** Exposure
- `src/String.zig` -> **99.9456%** Exposure
- `src/List.zig` -> **99.9448%** Exposure
- `src/std/map.zig` -> **99.9396%** Exposure
- `src/Vm.zig` -> **99.9159%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/lib.zig` -> **11** Orphaned Functions | **0** Duplicates
- `build.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/zig_from_bog.zig` -> **1** Orphaned Functions | **0** Duplicates
- `examples/bog_from_c.c` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `98` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Compiler.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 9.281)
- **Top Global Matches:** file_cluster_12: 9.281, file_cluster_4: 10.059, file_cluster_7: 10.316
- **Magnitude:** 1284.08 | **LOC:** 2922 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 26.673; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (59.9%), Guard Balance (formerly Safety Score) (39.1%), Connectivity (formerly Api Exposure) (28.7%), Complexity Load (formerly Cognitive Load) (13.8%)
- **Documentation Coverage:** 98.9011% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genComparison` **(Defensive Guards)** (Impact: 58.7)
  * `genMatch` **(Defensive Guards)** (Impact: 41.6)
  * `genAs` **(Defensive Guards)** (Impact: 40.2)
  * `genIf` **(Defensive Guards)** (Impact: 37.6)
  * `genWhile` **(Defensive Guards)** (Impact: 35.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 51 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 175
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 396`, `structural_boundaries: 395`, `args: 88`, `func_start: 88`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 73`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 568`, `doc: 8`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.673
  * `Choke Point (Betweenness):` 0.002406 | `Ripple Effect (Closeness):` 0.397566
  * `Imports (Out-Degree: 4):` bog.zig, repl.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Vm.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.368)
- **Top Global Matches:** file_cluster_12: 7.368, file_cluster_15: 9.255, file_cluster_4: 9.64
- **Magnitude:** 1009.18 | **LOC:** 1599 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 17.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Complexity Load (formerly Cognitive Load) (62.5%), Connectivity (formerly Api Exposure) (53.0%), Guard Balance (formerly Safety Score) (39.0%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Many-Argument Workhorses)** (Impact: 421.6)
    * *Intent:* /// Continues execution from current instruction pointer.
  * `import` **(Defensive Guards)** (Impact: 24.8)
  * `newVal` **(Defensive Guards)** (Impact: 12.0)
  * `push` **(Type Conversions)** (Impact: 11.4)
  * `compileAndRun` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /// Compiles and executes the file given by `file_path`.
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 90 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 202`, `args: 40`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 148`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 30`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 360`, `doc: 24`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.384314
  * `Imports (Out-Degree: 4):` Compiler.zig, bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.061)
- **Top Global Matches:** file_cluster_6: 8.061, file_cluster_8: 10.529, file_cluster_4: 15.565
- **Magnitude:** 843.94 | **LOC:** 1494 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 26.878; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (80.4%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (65.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next` **(Many-Argument Workhorses)** (Impact: 211.3)
  * `getIndent` **(Compute Cores)** (Impact: 32.6)
  * `tokenizeRepl` **(Defensive Guards)** (Impact: 12.7)
  * `tokenize` **(Defensive Guards)** (Impact: 7.8)
  * `isWhiteSpace` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 169`, `structural_boundaries: 143`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 186`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 53`, `doc: 9`, `test: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.878
  * `Choke Point (Betweenness):` 0.006788 | `Ripple Effect (Closeness):` 0.397566
  * `Imports (Out-Degree: 4):` bog.zig, multi_array_list.zig, repl.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/value.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 10.052)
- **Top Global Matches:** file_cluster_6: 10.052, file_cluster_8: 13.302, file_cluster_4: 16.135
- **Magnitude:** 741.36 | **LOC:** 1159 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **5**; blast radius 65.264; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.4%), Connectivity (formerly Api Exposure) (62.8%), Guard Balance (formerly Safety Score) (41.3%), Complexity Load (formerly Cognitive Load) (30.5%)
- **Documentation Coverage:** 70.7547% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /// Returns value in `container` at `index`.
  * `bogToZig` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* /// Converts Bog value to Zig value. Returned string is invalidated /// on next garbage collection.
  * `zigFnToBog` **(Defensive Guards)** (Impact: 49.3)
  * `dump` **(Defensive Guards)** (Impact: 46.2)
    * *Intent:* /// Prints string representation of value to writer
  * `as` **(Defensive Guards)** (Impact: 42.9)
    * *Intent:* /// `type_id` must be valid and cannot be .err, .range, .func or .native
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 217`, `structural_boundaries: 192`, `args: 43`, `func_start: 33`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 2`, `state_mutation: 48`, `dead_code: 2`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 48`, `import: 5`
* *Defense:* `safety: 218`, `doc: 19`, `test: 3`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 65.264
  * `Choke Point (Betweenness):` 0.052986 | `Ripple Effect (Closeness):` 0.443439
  * `Imports (Out-Degree: 5):` List.zig, Map.zig, String.zig, bog.zig, std
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.757)
- **Top Global Matches:** file_cluster_12: 6.757, file_cluster_9: 9.231, file_cluster_15: 9.4
- **Magnitude:** 701.6 | **LOC:** 1094 | **CtrlFlow:** 23.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 22.973; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Guard Balance (formerly Safety Score) (28.3%), Connectivity (formerly Api Exposure) (28.0%), Complexity Load (formerly Cognitive Load) (14.0%)
- **Documentation Coverage:** 23.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initializer` **(Defensive Guards)** (Impact: 31.9)
    * *Intent:* /// initializer /// : "(" block_or_expr ")" /// | "(" (expr ",")+ expr? ")" /// | "{" (expr "=" expr...
  * `bitExpr` **(Defensive Guards)** (Impact: 31.4)
    * *Intent:* /// bit_expr : shift_expr (("&" shift_expr)* | ("|" shift_expr)* | ("^" shift_expr)*
  * `ifExpr` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* /// if : "if" ("let" primary_expr "=")? expr block_or_expr ("else" block_or_expr)?
  * `primaryExpr` **(Defensive Guards)** (Impact: 26.2)
    * *Intent:* /// | format_string /// | NUMBER /// | "true" /// | "false" /// | "null" /// | initializer /// | "er...
  * `rangeExpr` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* /// range_expr : bit_expr (":" bit_expr? (":" bit_expr)?)?
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 209`, `structural_boundaries: 218`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 46`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 295`, `doc: 80`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 22.973
  * `Choke Point (Betweenness):` 0.000446 | `Ripple Effect (Closeness):` 0.390828
  * `Imports (Out-Degree: 5):` String.zig, bog.zig, repl.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/render.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.194)
- **Top Global Matches:** file_cluster_4: 6.194, file_cluster_12: 10.536, file_cluster_15: 10.916
- **Magnitude:** 386.36 | **LOC:** 747 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 11.205; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (57.9%), Connectivity (formerly Api Exposure) (46.6%), Guard Balance (formerly Safety Score) (30.8%), Complexity Load (formerly Cognitive Load) (14.4%)
- **Documentation Coverage:** 57.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `renderNode` **(Many-Argument Workhorses)** (Impact: 128.8)
  * `renderComments` **(Many-Argument Workhorses)** (Impact: 40.9)
    * *Intent:* /// Assumes that start is the first byte past the previous token and /// that end is the last byte b...
  * `AutoIndentingWriter` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* /// Automatically inserts indentation of written data by keeping /// track of the current indentatio...
  * `renderCommaList` **(Defensive Guards)** (Impact: 18.4)
  * `isBlock` **(Compute Cores)** (Impact: 15.6)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 44`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 21`
* *Architecture:* `io: 2`, `api: 14`, `import: 2`
* *Defense:* `safety: 162`, `doc: 23`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.205
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.27128
  * `Imports (Out-Degree: 3):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Tree.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.057)
- **Top Global Matches:** file_cluster_4: 6.057, file_cluster_12: 9.496, file_cluster_15: 9.824
- **Magnitude:** 331.86 | **LOC:** 837 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 26.257; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (60.3%), Connectivity (formerly Api Exposure) (55.1%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lastToken` **(Many-Argument Workhorses)** (Impact: 62.6)
  * `nodeItems` **(Many-Argument Workhorses)** (Impact: 15.9)
  * `firstToken` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `get` **(Many-Argument Workhorses)** (Impact: 10.3)
  * `prevToken` **(Compute Cores)** (Impact: 7.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 38 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 47`, `args: 14`, `func_start: 14`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 66`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 1`, `doc: 102`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.257
  * `Choke Point (Betweenness):` 0.031031 | `Ripple Effect (Closeness):` 0.397566
  * `Imports (Out-Degree: 4):` bog.zig, multi_array_list.zig, render.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.26)
- **Top Global Matches:** file_cluster_12: 7.26, file_cluster_5: 7.893, file_cluster_7: 8.395
- **Magnitude:** 297.72 | **LOC:** 673 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 16.72; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (59.6%), Connectivity (formerly Api Exposure) (58.3%)
- **Documentation Coverage:** 20.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getOrPutInternal` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* // // ------------------ No pub fns below this point ------------------ /// Must `ensureTotalCapacit...
  * `insertAllEntriesIntoNewHeaderGeneric` **(Many-Argument Workhorses)** (Impact: 11.8)
  * `ensureTotalCapacity` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /// Increases capacity, guaranteeing that insertions up until the /// `expected_count` will not caus...
  * `getSlotByKey` **(Many-Argument Workhorses)** (Impact: 11.1)
  * `getOrPutAssumeCapacityAdapted` **(Many-Argument Workhorses)** (Impact: 10.5)
    * *Intent:* /// If there is an existing item with `key`, then the result /// `Entry` pointers point to it, and f...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 75`, `args: 40`, `func_start: 40`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 43`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 23`, `doc: 106`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.72
  * `Choke Point (Betweenness):` 0.002629 | `Ripple Effect (Closeness):` 0.295626
  * `Imports (Out-Degree: 3):` bog.zig, multi_array_list.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/multi_array_list.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.487)
- **Top Global Matches:** file_cluster_5: 8.487, file_cluster_12: 9.436, file_cluster_7: 9.552
- **Magnitude:** 293.08 | **LOC:** 428 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 26.588; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.9%), Guard Balance (formerly Safety Score) (70.8%)
- **Documentation Coverage:** 16.0494% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `MultiArrayList` **(Compute Cores)** (Impact: 70.0)
    * *Intent:* /// A MultiArrayList stores a list of a struct type. /// Instead of storing a single list of items, ...
  * `shrinkAndFree` **(Many-Argument Workhorses)** (Impact: 14.3)
    * *Intent:* /// Attempt to reduce allocated capacity to `new_len`. /// If `new_len` is greater than zero, this m...
  * `setCapacity` **(Many-Argument Workhorses)** (Impact: 9.4)
    * *Intent:* /// Modify the array so that it can hold exactly `new_capacity` items. /// Invalidates pointers if a...
  * `ensureTotalCapacity` **(Compute Cores)** (Impact: 8.6)
    * *Intent:* /// Modify the array so that it can hold at least `new_capacity` items. /// Implements super-linear ...
  * `items` **(Type Conversions)** (Impact: 7.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 16 instances
* *State Mutation (weighted view):* 61
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 40`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 29`
* *Architecture:* `api: 30`, `import: 2`
* *Defense:* `safety: 9`, `doc: 66`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.588
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.311606
  * `Imports (Out-Degree: 1):` builtin, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/String.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.455)
- **Top Global Matches:** file_cluster_12: 8.455, file_cluster_4: 8.786, file_cluster_5: 10.009
- **Magnitude:** 221.86 | **LOC:** 285 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 32.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (68.8%), Complexity Load (formerly Cognitive Load) (58.4%), Guard Balance (formerly Safety Score) (52.9%)
- **Documentation Coverage:** 91.8919% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `format` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `as` **(Defensive Guards)** (Impact: 21.6)
  * `get` **(Defensive Guards)** (Impact: 21.3)
  * `from` **(Defensive Guards)** (Impact: 12.9)
  * `join` **(Defensive Guards)** (Impact: 11.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 59
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 47`, `structural_boundaries: 50`, `args: 18`, `func_start: 18`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 21`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 20`, `import: 2`
* *Defense:* `safety: 32`, `doc: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.414
  * `Choke Point (Betweenness):` 0.001337 | `Ripple Effect (Closeness):` 0.397566
  * `Imports (Out-Degree: 3):` bog.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Gc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.625)
- **Top Global Matches:** file_cluster_4: 7.625, file_cluster_12: 10.214, file_cluster_15: 11.817
- **Magnitude:** 195.2 | **LOC:** 386 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 17.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (45.9%), Connectivity (formerly Api Exposure) (37.2%), Complexity Load (formerly Cognitive Load) (17.9%)
- **Documentation Coverage:** 52.6316% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `markGray` **(Defensive Guards)** (Impact: 26.3)
  * `allocExtra` **(Defensive Guards)** (Impact: 17.6)
  * `markVal` **(Defensive Guards)** (Impact: 16.9)
  * `dupe` **(Defensive Guards)** (Impact: 15.3)
    * *Intent:* /// Allocates a shallow copy of `val`.
  * `collect` **(Defensive Guards)** (Impact: 8.5)
    * *Intent:* /// Collect all unreachable values.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 46`, `args: 13`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 26`, `planned_debt: 1`
* *Architecture:* `api: 6`, `import: 3`
* *Defense:* `safety: 52`, `doc: 15`, `test: 2`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.414
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.384314
  * `Imports (Out-Degree: 3):` bog.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/math.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.147)
- **Top Global Matches:** file_cluster_15: 7.147, file_cluster_12: 8.156, file_cluster_11: 8.711
- **Magnitude:** 131.6 | **LOC:** 212 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 27.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (49.7%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 97.561% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sqrt` **(Defensive Guards)** (Impact: 5.9)
  * `fma` **(Parameter Forwarders)** (Impact: 2.1)
  * `scalbn` **(Parameter Forwarders)** (Impact: 1.9)
  * `atan2` **(Parameter Forwarders)** (Impact: 1.9)
  * `hypot` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2`, `structural_boundaries: 44`, `args: 41`, `func_start: 41`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 2`
* *Architecture:* `api: 51`, `import: 2`
* *Defense:* `safety: 4`, `doc: 10`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.882
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.419251
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/List.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.127)
- **Top Global Matches:** file_cluster_7: 9.127, file_cluster_12: 9.208, file_cluster_5: 9.343
- **Magnitude:** 105.02 | **LOC:** 118 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 16.72; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.6%), Complexity Load (formerly Cognitive Load) (57.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 31.3)
  * `set` **(Type Conversions)** (Impact: 16.8)
  * `eql` **(Compute Cores)** (Impact: 7.3)
  * `in` **(Defensive Guards)** (Impact: 5.5)
  * `as` **(Parameter Forwarders)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 19`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 9`, `planned_debt: 2`
* *Architecture:* `api: 9`, `import: 2`
* *Defense:* `safety: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.72
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.291884
  * `Imports (Out-Degree: 3):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.728)
- **Top Global Matches:** file_cluster_12: 7.728, file_cluster_15: 8.839, file_cluster_9: 9.144
- **Magnitude:** 99.9 | **LOC:** 276 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.625; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (53.8%), Guard Balance (formerly Safety Score) (34.5%), Complexity Load (formerly Cognitive Load) (13.9%), Debt Markers (formerly Tech Debt) (9.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `run` **(Defensive Guards)** (Impact: 16.7)
  * `debugTokens` **(Defensive Guards)** (Impact: 14.3)
  * `fmtFile` **(Defensive Guards)** (Impact: 12.9)
  * `main` **(Defensive Guards)** (Impact: 9.4)
  * `debugDump` **(Defensive Guards)** (Impact: 8.2)
    * *Intent:* ;
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 5 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 39`, `structural_boundaries: 51`, `args: 10`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `io: 21`, `api: 1`, `import: 3`
* *Defense:* `safety: 53`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` bog, builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Bytecode.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.002)
- **Top Global Matches:** file_cluster_12: 7.002, file_cluster_15: 7.776, file_cluster_2: 9.354
- **Magnitude:** 94.02 | **LOC:** 518 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 17.414; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.1%), Connectivity (formerly Api Exposure) (49.3%), Concurrency Surface (formerly Concurrency) (48.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `dump` **(Many-Argument Workhorses)** (Impact: 25.5)
  * `dumpLineCol` **(Compute Cores)** (Impact: 5.9)
  * `needsDebugInfo` **(Compute Cores)** (Impact: 5.0)
  * `hasResult` **(Compute Cores)** (Impact: 4.8)
  * `dumpList` **(State Mutators)** (Impact: 4.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 17`, `structural_boundaries: 11`, `args: 9`, `func_start: 9`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`
* *Architecture:* `api: 14`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 2`, `doc: 64`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 17.414
  * `Choke Point (Betweenness):` 0.005006 | `Ripple Effect (Closeness):` 0.384314
  * `Imports (Out-Degree: 3):` bog.zig, multi_array_list.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/repl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.955)
- **Top Global Matches:** file_cluster_12: 7.955, file_cluster_7: 8.692, file_cluster_5: 10.09
- **Magnitude:** 92.06 | **LOC:** 201 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **7**; blast radius 32.699; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (44.8%), Connectivity (formerly Api Exposure) (27.4%), Complexity Load (formerly Cognitive Load) (25.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleLine` **(Defensive Guards)** (Impact: 23.4)
  * `readLine` **(Defensive Guards)** (Impact: 14.3)
  * `run` **(Defensive Guards)** (Impact: 9.4)
  * `init` **(Defensive Guards)** (Impact: 7.3)
  * `deinit` **(State Mutators)** (Impact: 2.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 30
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 21`, `args: 5`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 16`
* *Architecture:* `io: 1`, `api: 2`, `import: 7`
* *Defense:* `safety: 37`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 32.699
  * `Choke Point (Betweenness):` 0.002228 | `Ripple Effect (Closeness):` 0.404541
  * `Imports (Out-Degree: 5):` Compiler.zig, bog.zig, builtin, linenoise, parser.zig, std, tokenizer.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/lib.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.175)
- **Top Global Matches:** file_cluster_12: 7.175, file_cluster_15: 7.666, file_cluster_16: 8.591
- **Magnitude:** 81.92 | **LOC:** 138 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.625; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (47.1%), Complexity Load (formerly Cognitive Load) (28.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `bog_Vm_run` **(Defensive Guards)** (Impact: 6.5)
  * `bog_Vm_call` **(Many-Argument Workhorses)** (Impact: 5.3)
  * `bog_parse` **(Defensive Guards)** (Impact: 4.5)
  * `bog_Tree_render` **(Defensive Guards)** (Impact: 4.3)
  * `bog_Vm_init` **(Defensive Guards)** (Impact: 3.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 11`, `structural_boundaries: 28`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 8`, `unreferenced_by_name: 11`
* *Architecture:* `io: 3`, `api: 13`, `import: 3`
* *Defense:* `safety: 17`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bog.zig, build_options, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/behavior.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 6.826)
- **Top Global Matches:** file_cluster_9: 6.826, file_cluster_15: 8.342, file_cluster_12: 8.632
- **Magnitude:** 71.68 | **LOC:** 971 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.625; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (35.8%), Concurrency Surface (formerly Concurrency) (16.1%), Complexity Load (formerly Cognitive Load) (3.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectCallOutput` **(Defensive Guards)** (Impact: 18.8)
  * `expectOutput` **(Defensive Guards)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 139`, `args: 38`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `planned_debt: 1`
* *Architecture:* `io: 5`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 119`, `test: 60`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog, builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bog.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.718)
- **Top Global Matches:** file_cluster_15: 7.718, file_cluster_16: 9.267, file_cluster_2: 9.719
- **Magnitude:** 66.42 | **LOC:** 147 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **23** in-repo importer(s); it depends on **12**; blast radius 166.429; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (56.1%), Guard Balance (formerly Safety Score) (38.1%), Debt Markers (formerly Tech Debt) (11.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `add` **(Many-Argument Workhorses)** (Impact: 14.9)
  * `render` **(Defensive Guards)** (Impact: 12.3)
  * `deinit` **(State Mutators)** (Impact: 3.2)
  * `init` **(Parameter Forwarders)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 5`, `args: 4`, `func_start: 4`, `class_start: 2`
* *Risk/State:* `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 24`, `import: 13`
* *Defense:* `safety: 21`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 166.429
  * `Choke Point (Betweenness):` 0.270811 | `Ripple Effect (Closeness):` 0.698752
  * `Imports (Out-Degree: 11):` Bytecode.zig, Compiler.zig, Gc.zig, String.zig, Tree.zig, Vm.zig, parser.zig, repl.zig...
  * `Imported By (In-Degree: 23):` (Excluded from Brief to save tokens)

### `src/std/fs.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.595)
- **Top Global Matches:** file_cluster_15: 6.595, file_cluster_16: 8.465, file_cluster_11: 8.578
- **Magnitude:** 54.42 | **LOC:** 69 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 27.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.2%), Connectivity (formerly Api Exposure) (58.9%), Guard Balance (formerly Safety Score) (48.1%), Complexity Load (formerly Cognitive Load) (42.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Defensive Guards)** (Impact: 16.6)
  * `write` **(Defensive Guards)** (Impact: 4.2)
  * `close` **(Parameter Forwarders)** (Impact: 3.7)
  * `read` **(Parameter Forwarders)** (Impact: 3.7)
  * `open` **(Defensive Guards)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 9`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 8`, `import: 2`
* *Defense:* `safety: 7`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.882
  * `Choke Point (Betweenness):` 0.004011 | `Ripple Effect (Closeness):` 0.419251
  * `Imports (Out-Degree: 3):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/json.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.936)
- **Top Global Matches:** file_cluster_12: 6.936, file_cluster_15: 7.509, file_cluster_16: 8.842
- **Magnitude:** 33.84 | **LOC:** 89 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 27.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.0%), Guard Balance (formerly Safety Score) (35.7%), Connectivity (formerly Api Exposure) (27.8%), Complexity Load (formerly Cognitive Load) (16.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseInternal` **(Defensive Guards)** (Impact: 17.3)
  * `stringify` **(Defensive Guards)** (Impact: 2.0)
  * `parse` **(Parameter Forwarders)** (Impact: 1.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 10`, `structural_boundaries: 20`, `args: 3`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 5`
* *Architecture:* `api: 2`, `import: 2`
* *Defense:* `safety: 21`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.882
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.419251
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `include/bog.h` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Centroid distance: 4.133)
- **Top Global Matches:** file_cluster_17: 4.133, file_cluster_2: 6.309, file_cluster_15: 6.621
- **Magnitude:** 33.72 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 10.407; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 13`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 10.407
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.029412
  * `Imports (Out-Degree: 0):` stdbool.h, stdint.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.927)
- **Top Global Matches:** file_cluster_12: 6.927, file_cluster_15: 9.015, file_cluster_7: 9.246
- **Magnitude:** 32.76 | **LOC:** 70 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 27.882; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (43.0%), Guard Balance (formerly Safety Score) (37.4%), Complexity Load (formerly Cognitive Load) (15.4%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `entries` **(Defensive Guards)** (Impact: 4.7)
    * *Intent:* /// Creates a list of kv pairs
  * `keys` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* /// Creates a list of the maps keys
  * `values` **(Defensive Guards)** (Impact: 4.2)
    * *Intent:* /// Creates a list of the maps values
  * `size` **(Type Conversions)** (Impact: 1.6)
    * *Intent:* /// Returns the amount of key value pairs in the map.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 14`, `args: 4`, `func_start: 4`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`
* *Architecture:* `api: 4`, `import: 2`
* *Defense:* `safety: 17`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.882
  * `Choke Point (Betweenness):` 0.004011 | `Ripple Effect (Closeness):` 0.419251
  * `Imports (Out-Degree: 3):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/bog_from_c.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.613)
- **Top Global Matches:** file_cluster_12: 8.613, file_cluster_9: 9.138, file_cluster_15: 10.24
- **Magnitude:** 23.16 | **LOC:** 59 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 5.625; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (54.3%), Complexity Load (formerly Cognitive Load) (23.9%), Connectivity (formerly Api Exposure) (5.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 12.0)
  * `read_file` **(Type Conversions)** (Impact: 5.2)
    * *Intent:* #include <stdio.h> #include <stdlib.h> #include "bog.h"
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 3
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 9`, `args: 2`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 1`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 2`, `import: 3`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/fmt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.122)
- **Top Global Matches:** file_cluster_2: 6.122, file_cluster_15: 6.73, file_cluster_17: 7.23
- **Magnitude:** 21.84 | **LOC:** 386 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 5.625; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (35.1%), Complexity Load (formerly Cognitive Load) (3.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testTransform` **(Defensive Guards)** (Impact: 6.1)
  * `testCanonical` **(Defensive Guards)** (Impact: 1.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 21`, `structural_boundaries: 16`, `args: 11`, `func_start: 2`
* *Risk/State:* `high_risk_execution: 3`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `io: 1`, `import: 2`
* *Defense:* `safety: 47`, `test: 29`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.625
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bog, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/List.zig` (ZIG) | Magnitude: 105.02 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 76, pointers: 27, branch: 23, structural_boundaries: 19

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bog.zig` -> **Severity: 15.189** (Bridge: 0.2708 * Flux: 56.0854%)
- `src/value.zig` -> **Severity: 4.898** (Bridge: 0.053 * Flux: 92.4333%)
- `src/Tree.zig` -> **Severity: 3.095** (Bridge: 0.031 * Flux: 99.7312%)
- `src/tokenizer.zig` -> **Severity: 0.679** (Bridge: 0.0068 * Flux: 99.9994%)
- `src/std/map.zig` -> **Severity: 0.401** (Bridge: 0.004 * Flux: 99.9396%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/std.zig` -> **Severity: 42.94** (Embedded: 0.8235 * Error Risk: 52.1415%)
- `src/bog.zig` -> **Severity: 26.626** (Embedded: 0.6988 * Error Risk: 38.1047%)
- `src/tokenizer.zig` -> **Severity: 26.101** (Embedded: 0.3976 * Error Risk: 65.6513%)
- `src/Tree.zig` -> **Severity: 23.965** (Embedded: 0.3976 * Error Risk: 60.2782%)
- `src/multi_array_list.zig` -> **Severity: 22.047** (Embedded: 0.3116 * Error Risk: 70.7524%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/std.zig` -> **Severity: 20947.7** (Blast Radius: 209.477 * Doc Risk: 100.0%)
- `src/bog.zig` -> **Severity: 16642.9** (Blast Radius: 166.429 * Doc Risk: 100.0%)
- `src/value.zig` -> **Severity: 4617.735** (Blast Radius: 65.264 * Doc Risk: 70.7547%)
- `src/repl.zig` -> **Severity: 3269.9** (Blast Radius: 32.699 * Doc Risk: 100.0%)
- `src/String.zig` -> **Severity: 2978.584** (Blast Radius: 32.414 * Doc Risk: 91.8919%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 2027 call pairs -- scoped 28.5%, unique 0.0%, ambiguous 23.4%, external 48.1%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 2013 | 28.7% | 0.0% | 23.5% | 47.8% |
| c | 14 | 7.1% | 0.0% | 0.0% | 92.9% |

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
