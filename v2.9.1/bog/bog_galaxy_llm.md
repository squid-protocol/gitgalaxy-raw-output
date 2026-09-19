# ARCHITECTURAL_BRIEF: bog
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/Vexu/bog.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 32 analyzed artifact(s), 12902 LOC.
- **Load-bearing artifact:** `src/std.zig` -- 27 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/bog.zig` -- pulls in 11 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/Compiler.zig` at magnitude 1270.38 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 32 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 8 |
| Total LOC | 12902 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 80.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.1769 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.6818 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 68.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3692 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 1 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 29 | 12818 | 90.6% |
| C | 2 | 84 | 6.2% |
| MARKDOWN | 1 | 0 | 3.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.85`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.85; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 56%, Large Core Modules (3) 22%, Data / Markup / Trivial 9%, Type Conversions Files 6%, Declarative / Non-Code 3%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 31 | 96.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 1 | 3.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 8*

**Composition by Extension & Reason:**
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.bog`: 1x Excluded (Unsupported Extension: '.bog')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 80.6 | 19.6 | 14.1 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 87.6 | 35.1 | 20.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 7.3 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 19.6 | 2.5 | 80.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 40.7 | 40.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 48.1 | 3.9 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 56.4 | 59.9 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 24.9 | 3.1 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 77.9 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1021 | 28 | 80 | `src/Vm.zig` |
| cleanup | 169 | 22 | 17 | `src/Compiler.zig` |
| guards | 2181 | 27 | 218 | `src/Compiler.zig` |
| danger | 490 | 25 | 35 | `src/Compiler.zig` |
| concurrency | 27 | 5 | 4 | `src/Bytecode.zig` |
| connectivity | 382 | 28 | 30 | `src/std/math.zig` |
| io | 53 | 14 | 4 | `src/main.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 0 | 0 | 0 | - |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `src/std/json.zig` |
| regex | 0 | 0 | 0 | - |
| events | 1 | 1 | 0 | `src/Gc.zig` |
| tests | 132 | 6 | 10 | `tests/behavior.zig` |
| docs | 537 | 16 | 66 | `src/Map.zig` |
| debt | 78 | 13 | 5 | `src/Bytecode.zig` |
| mutation | 3301 | 29 | 250 | `src/Compiler.zig` |
| dead_code | 49 | 12 | 4 | `src/Tree.zig` |
| credential | 0 | 0 | 0 | - |
| threat | 60 | 10 | 2 | `src/value.zig` |
| ml_ai | 134 | 13 | 9 | `src/std/math.zig` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **4.0167**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0871**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/main.zig` (Hits: 21)
- `src/Vm.zig` (Hits: 7)
- `tests/behavior.zig` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **std.zig** (`src/std.zig`) — 27 inbound connections
2. **bog.zig** (`src/bog.zig`) — 20 inbound connections
3. **multi_array_list.zig** (`src/multi_array_list.zig`) — 4 inbound connections
4. **Compiler.zig** (`src/Compiler.zig`) — 3 inbound connections
5. **parser.zig** (`src/parser.zig`) — 2 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **bog.zig** (`src/bog.zig`) — 11 outbound dependencies
2. **repl.zig** (`src/repl.zig`) — 7 outbound dependencies
3. **std.zig** (`src/std.zig`) — 7 outbound dependencies
4. **value.zig** (`src/value.zig`) — 5 outbound dependencies
5. **Tree.zig** (`src/Tree.zig`) — 4 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `next` **(Many-Argument Workhorses)** (@ `src/tokenizer.zig`) -> Impact: **215.6** | LOC: 691
- `renderNode` **(Many-Argument Workhorses)** (@ `src/render.zig`) -> Impact: **128.8** | LOC: 384
- `get` **(Many-Argument Workhorses)** (@ `src/value.zig`) -> Impact: **71.2** | LOC: 82
  * *Intent:* /// Returns value in `container` at `index`.
- `MultiArrayList` **(Compute Cores)** (@ `src/multi_array_list.zig`) -> Impact: **70.0** | LOC: 410
  * *Intent:* /// A MultiArrayList stores a list of a struct type. /// Instead of storing a single list of items, MultiArrayList /// stores separate lists for each ...
- `lastToken` **(Many-Argument Workhorses)** (@ `src/Tree.zig`) -> Impact: **62.6** | LOC: 178
- `genComparison` **(Defensive Guards)** (@ `src/Compiler.zig`) -> Impact: **58.7** | LOC: 101
- `bogToZig` **(Many-Argument Workhorses)** (@ `src/value.zig`) -> Impact: **58.2** | LOC: 84
  * *Intent:* /// Converts Bog value to Zig value. Returned string is invalidated /// on next garbage collection.
- `dump` **(Defensive Guards)** (@ `src/value.zig`) -> Impact: **46.2** | LOC: 84
  * *Intent:* /// Prints string representation of value to writer
- `as` **(Defensive Guards)** (@ `src/value.zig`) -> Impact: **42.9** | LOC: 58
  * *Intent:* /// `type_id` must be valid and cannot be .err, .range, .func or .native
- `genMatch` **(Defensive Guards)** (@ `src/Compiler.zig`) -> Impact: **41.6** | LOC: 113

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 18 | 6349.22 | 26.33% | 11.44% |
| `src/std` | 7 | 282.52 | 12.79% | 3.13% |
| `tests` | 3 | 113.56 | 3.67% | 0.0% |
| `examples` | 2 | 35.92 | 16.25% | 0.0% |
| `include` | 1 | 33.72 | 0.0% | 0.0% |
| `__monolith__` | 1 | 4.2 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/lib.zig` -> **99.9701%** Exposure
- `src/List.zig` -> **22.0565%** Exposure
- `src/std/fs.zig` -> **21.9173%** Exposure
- `src/String.zig` -> **20.6765%** Exposure
- `src/bog.zig` -> **13.237%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/tokenizer.zig` -> **99.9994%** Exposure
- `src/String.zig` -> **99.9456%** Exposure
- `src/List.zig` -> **99.9448%** Exposure
- `src/std/map.zig` -> **99.9396%** Exposure
- `src/Vm.zig` -> **99.9159%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/lib.zig` -> **11** Orphaned Functions | **0** Duplicates
- `examples/bog_from_c.c` -> **1** Orphaned Functions | **0** Duplicates
- `examples/zig_from_bog.zig` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `87` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/Compiler.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1270.38 | **LOC:** 2922 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **2**; blast radius 28.67; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (59.9%), Connectivity (formerly Api Exposure) (28.7%), Guard Balance (formerly Safety Score) (20.9%), Complexity Load (formerly Cognitive Load) (13.8%)
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
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 73`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `api: 5`, `concurrency: 3`, `import: 3`
* *Defense:* `safety: 568`, `doc: 8`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 28.67
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.36744
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 848.24 | **LOC:** 1494 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 23.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.6%), Complexity Load (formerly Cognitive Load) (80.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `next` **(Many-Argument Workhorses)** (Impact: 215.6)
  * `getIndent` **(Compute Cores)** (Impact: 32.6)
  * `tokenizeRepl` **(Defensive Guards)** (Impact: 12.7)
  * `tokenize` **(Defensive Guards)** (Impact: 7.8)
  * `isWhiteSpace` **(I/O & Config Routines)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 162 instances
* *State Mutation (weighted view):* 510
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 172`, `structural_boundaries: 143`, `args: 9`, `func_start: 9`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 186`, `dead_code: 1`
* *Architecture:* `io: 1`, `api: 10`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 53`, `doc: 9`, `test: 9`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.081
  * `Choke Point (Betweenness):` 0.008602 | `Ripple Effect (Closeness):` 0.361787
  * `Imports (Out-Degree: 3):` bog.zig, multi_array_list.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 707.6 | **LOC:** 1094 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 23.081; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.0%), Connectivity (formerly Api Exposure) (28.0%), Complexity Load (formerly Cognitive Load) (14.1%), Dead Code Surface (formerly Dead Code) (12.4%)
- **Documentation Coverage:** 23.5294% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `primaryExpr` **(Defensive Guards)** (Impact: 32.2)
    * *Intent:* /// | format_string /// | NUMBER /// | "true" /// | "false" /// | "null" /// | initializer /// | "er...
  * `initializer` **(Defensive Guards)** (Impact: 31.9)
    * *Intent:* /// initializer /// : "(" block_or_expr ")" /// | "(" (expr ",")+ expr? ")" /// | "{" (expr "=" expr...
  * `bitExpr` **(Defensive Guards)** (Impact: 31.4)
    * *Intent:* /// bit_expr : shift_expr (("&" shift_expr)* | ("|" shift_expr)* | ("^" shift_expr)*
  * `ifExpr` **(Defensive Guards)** (Impact: 27.0)
    * *Intent:* /// if : "if" ("let" primary_expr "=")? expr block_or_expr ("else" block_or_expr)?
  * `rangeExpr` **(Defensive Guards)** (Impact: 23.2)
    * *Intent:* /// range_expr : bit_expr (":" bit_expr? (":" bit_expr)?)?
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 39 instances
* *State Mutation (weighted view):* 124
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 212`, `structural_boundaries: 218`, `args: 49`, `func_start: 49`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 20`, `state_mutation: 46`, `dead_code: 8`
* *Architecture:* `api: 4`, `import: 4`
* *Defense:* `safety: 295`, `doc: 80`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 23.081
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.361787
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/value.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 655.66 | **LOC:** 1159 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 19.727; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.4%), Connectivity (formerly Api Exposure) (62.8%), Complexity Load (formerly Cognitive Load) (30.6%), Guard Balance (formerly Safety Score) (26.0%)
- **Documentation Coverage:** 73.494% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `get` **(Many-Argument Workhorses)** (Impact: 71.2)
    * *Intent:* /// Returns value in `container` at `index`.
  * `bogToZig` **(Many-Argument Workhorses)** (Impact: 58.2)
    * *Intent:* /// Converts Bog value to Zig value. Returned string is invalidated /// on next garbage collection.
  * `dump` **(Defensive Guards)** (Impact: 46.2)
    * *Intent:* /// Prints string representation of value to writer
  * `as` **(Defensive Guards)** (Impact: 42.9)
    * *Intent:* /// `type_id` must be valid and cannot be .err, .range, .func or .native
  * `native` **(Defensive Guards)** (Impact: 39.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 39 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 126
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 192`, `args: 43`, `func_start: 33`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 2`, `state_mutation: 48`, `dead_code: 4`, `planned_debt: 9`, `fragile_debt: 1`
* *Architecture:* `io: 1`, `api: 48`, `import: 5`
* *Defense:* `safety: 218`, `doc: 19`, `test: 3`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.083871 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 5):` List.zig, Map.zig, String.zig, bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Vm.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 591.08 | **LOC:** 1599 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 19.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (53.0%), Complexity Load (formerly Cognitive Load) (38.2%), Concurrency Surface (formerly Concurrency) (28.5%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `import` **(Defensive Guards)** (Impact: 24.8)
  * `newVal` **(Defensive Guards)** (Impact: 12.0)
  * `push` **(Type Conversions)** (Impact: 11.4)
  * `compileAndRun` **(Defensive Guards)** (Impact: 10.1)
    * *Intent:* /// Compiles and executes the file given by `file_path`.
  * `valDupeSimple` **(Defensive Guards)** (Impact: 8.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 90 instances
* *Concurrency (weighted view):* 19
* *State Mutation (weighted view):* 328
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 263`, `structural_boundaries: 202`, `args: 40`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 148`, `dead_code: 1`, `planned_debt: 6`
* *Architecture:* `io: 7`, `api: 30`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 360`, `doc: 24`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 3):` Compiler.zig, bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/render.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 386.36 | **LOC:** 747 | **CtrlFlow:** 16.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 10.314; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (57.9%), Connectivity (formerly Api Exposure) (46.6%), Complexity Load (formerly Cognitive Load) (14.4%), Guard Balance (formerly Safety Score) (8.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.314
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.258419
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Tree.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 331.86 | **LOC:** 837 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 19.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.0%), Connectivity (formerly Api Exposure) (55.1%)
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
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 66`, `dead_code: 14`
* *Architecture:* `api: 25`, `import: 4`
* *Defense:* `safety: 1`, `doc: 102`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.035484 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 4):` bog.zig, multi_array_list.zig, render.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 297.72 | **LOC:** 673 | **CtrlFlow:** 8.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 9.476; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.8%), Connectivity (formerly Api Exposure) (58.3%)
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
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 43`, `dead_code: 1`
* *Architecture:* `api: 27`, `import: 3`
* *Defense:* `safety: 23`, `doc: 106`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.476
  * `Choke Point (Betweenness):` 0.001075 | `Ripple Effect (Closeness):` 0.258419
  * `Imports (Out-Degree: 3):` bog.zig, multi_array_list.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/multi_array_list.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 293.08 | **LOC:** 428 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 25.128; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Guard Balance (formerly Safety Score) (87.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (74.9%)
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
* *Risk/State:* `safety_bypasses: 26`, `state_mutation: 29`, `dead_code: 2`
* *Architecture:* `api: 30`, `import: 2`
* *Defense:* `safety: 9`, `doc: 66`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 25.128
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.290323
  * `Imports (Out-Degree: 1):` builtin, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/String.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 221.86 | **LOC:** 285 | **CtrlFlow:** 19.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 9.476; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (61.3%), Guard Balance (formerly Safety Score) (59.8%), Complexity Load (formerly Cognitive Load) (58.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.258419
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/Gc.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 195.2 | **LOC:** 386 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 19.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.8%), Guard Balance (formerly Safety Score) (38.7%), Connectivity (formerly Api Exposure) (37.2%), Complexity Load (formerly Cognitive Load) (17.9%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/math.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 131.6 | **LOC:** 212 | **CtrlFlow:** 1.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 36.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (83.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.9%), Mutation Surface (formerly State Flux) (31.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.558
  * `Choke Point (Betweenness):` 0.018638 | `Ripple Effect (Closeness):` 0.443701
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/List.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 105.02 | **LOC:** 118 | **CtrlFlow:** 22.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 9.476; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (57.1%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.476
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.258419
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 99.9 | **LOC:** 276 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (53.8%), Complexity Load (formerly Cognitive Load) (13.9%), Guard Balance (formerly Safety Score) (13.2%), Debt Markers (formerly Tech Debt) (10.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog, builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Bytecode.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 94.02 | **LOC:** 518 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 19.727; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (54.1%), Connectivity (formerly Api Exposure) (49.3%), Concurrency Surface (formerly Concurrency) (48.1%)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 4`, `dead_code: 1`
* *Architecture:* `api: 14`, `concurrency: 10`, `import: 3`
* *Defense:* `safety: 2`, `doc: 64`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.007527 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 3):` bog.zig, multi_array_list.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/repl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 92.06 | **LOC:** 201 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 19.727; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.9%), Guard Balance (formerly Safety Score) (36.4%), Complexity Load (formerly Cognitive Load) (25.8%), Connectivity (formerly Api Exposure) (23.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 19.727
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.356305
  * `Imports (Out-Degree: 5):` Compiler.zig, bog.zig, builtin, linenoise, parser.zig, std, tokenizer.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/lib.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 81.92 | **LOC:** 138 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (43.8%), Complexity Load (formerly Cognitive Load) (28.6%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bog.zig, build_options, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/behavior.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Drift: 0.0 IQR)
- **Magnitude:** 71.68 | **LOC:** 971 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (16.1%), Guard Balance (formerly Safety Score) (15.0%), Complexity Load (formerly Cognitive Load) (4.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `expectCallOutput` **(Defensive Guards)** (Impact: 18.8)
  * `expectOutput` **(Defensive Guards)** (Impact: 11.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 20
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 139`, `args: 38`, `func_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 14`, `planned_debt: 1`
* *Architecture:* `io: 5`, `concurrency: 4`, `import: 3`
* *Defense:* `safety: 119`, `test: 60`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/bog.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 66.42 | **LOC:** 147 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **20** in-repo importer(s); it depends on **11**; blast radius 176.069; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (56.1%), Guard Balance (formerly Safety Score) (20.3%), Debt Markers (formerly Tech Debt) (13.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 176.069
  * `Choke Point (Betweenness):` 0.376344 | `Ripple Effect (Closeness):` 0.587903
  * `Imports (Out-Degree: 10):` Bytecode.zig, Compiler.zig, Gc.zig, Tree.zig, Vm.zig, parser.zig, repl.zig, std...
  * `Imported By (In-Degree: 20):` (Excluded from Brief to save tokens)

### `src/std/fs.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 54.42 | **LOC:** 69 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 36.558; role: Transceiver (Middle-Tier)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.558
  * `Choke Point (Betweenness):` 0.018638 | `Ripple Effect (Closeness):` 0.443701
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/json.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 33.84 | **LOC:** 89 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 36.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.0%), Connectivity (formerly Api Exposure) (27.8%), Complexity Load (formerly Cognitive Load) (16.3%), Guard Balance (formerly Safety Score) (16.2%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.558
  * `Choke Point (Betweenness):` 0.018638 | `Ripple Effect (Closeness):` 0.443701
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `include/bog.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 33.72 | **LOC:** 64 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 11.326; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (80.3%), Test Surface (formerly Verification) (2.3%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 15`, `args: 13`, `class_start: 5`
* *Risk/State:* None
* *Architecture:* `api: 18`, `import: 2`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.326
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.032258
  * `Imports (Out-Degree: 0):` stdbool.h, stdint.h
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/std/map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 32.76 | **LOC:** 70 | **CtrlFlow:** 5.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **2**; blast radius 36.558; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Connectivity (formerly Api Exposure) (43.0%), Guard Balance (formerly Safety Score) (20.1%), Complexity Load (formerly Cognitive Load) (15.4%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 36.558
  * `Choke Point (Betweenness):` 0.018638 | `Ripple Effect (Closeness):` 0.443701
  * `Imports (Out-Degree: 2):` bog.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/bog_from_c.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 23.16 | **LOC:** 59 | **CtrlFlow:** 14.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 6.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (70.2%), Complexity Load (formerly Cognitive Load) (23.9%), Connectivity (formerly Api Exposure) (5.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog.h, stdio.h, stdlib.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `tests/fmt.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 21.84 | **LOC:** 386 | **CtrlFlow:** 5.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 6.122; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (14.0%), Complexity Load (formerly Cognitive Load) (3.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 6.122
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` bog, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/bog.zig` -> **Severity: 21.107** (Bridge: 0.3763 * Flux: 56.0854%)
- `src/value.zig` -> **Severity: 7.752** (Bridge: 0.0839 * Flux: 92.4333%)
- `src/Tree.zig` -> **Severity: 3.539** (Bridge: 0.0355 * Flux: 99.7312%)
- `src/std/map.zig` -> **Severity: 1.863** (Bridge: 0.0186 * Flux: 99.9396%)
- `src/std/fs.zig` -> **Severity: 1.849** (Bridge: 0.0186 * Flux: 99.1943%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/std.zig` -> **Severity: 52.74** (Embedded: 0.871 * Error Risk: 60.5532%)
- `src/tokenizer.zig` -> **Severity: 31.68** (Embedded: 0.3618 * Error Risk: 87.5641%)
- `src/Tree.zig` -> **Severity: 27.808** (Embedded: 0.3563 * Error Risk: 78.0448%)
- `src/multi_array_list.zig` -> **Severity: 25.395** (Embedded: 0.2903 * Error Risk: 87.4721%)
- `src/std/math.zig` -> **Severity: 22.577** (Embedded: 0.4437 * Error Risk: 50.8823%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/std.zig` -> **Severity: 25065.7** (Blast Radius: 250.657 * Doc Risk: 100.0%)
- `src/bog.zig` -> **Severity: 17606.9** (Blast Radius: 176.069 * Doc Risk: 100.0%)
- `src/std/debug.zig` -> **Severity: 3655.8** (Blast Radius: 36.558 * Doc Risk: 100.0%)
- `src/std/fs.zig` -> **Severity: 3655.8** (Blast Radius: 36.558 * Doc Risk: 100.0%)
- `src/std/io.zig` -> **Severity: 3655.8** (Blast Radius: 36.558 * Doc Risk: 100.0%)

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
