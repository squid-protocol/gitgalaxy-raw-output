# ARCHITECTURAL_BRIEF: cyber
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/fubark/cyber.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 163 analyzed artifact(s), 63076 LOC.
- **Load-bearing artifact:** `src/cyber.zig` -- 52 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/cyber.zig` -- pulls in 40 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/sema.zig` at magnitude 5574.06 (structural weight, not risk).
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
| Total Artifacts | 594 |
| Analyzed Artifacts (Scanned) | 163 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 431 |
| Total LOC | 63076 |
| Volatility Index | 0.037 |
| % Scanned of codebase = | 27.4% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3221 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4541 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.4% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.4921 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 8 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 86 | 56925 | 52.8% |
| C | 15 | 3697 | 9.2% |
| MARKDOWN | 10 | 0 | 6.1% |
| LUA | 10 | 742 | 6.1% |
| PLAINTEXT | 7 | 0 | 4.3% |
| JAVASCRIPT | 6 | 570 | 3.7% |
| PYTHON | 5 | 208 | 3.1% |
| JAVA | 4 | 272 | 2.5% |
| PHP | 4 | 50 | 2.5% |
| RUBY | 4 | 38 | 2.5% |
| MAKEFILE | 2 | 14 | 1.2% |
| JSON | 2 | 74 | 1.2% |
| PERL | 2 | 17 | 1.2% |
| HTML | 1 | 241 | 0.6% |
| CSS | 1 | 141 | 0.6% |
| SHELL | 1 | 40 | 0.6% |
| GO | 1 | 15 | 0.6% |
| CPP | 1 | 22 | 0.6% |
| RUST | 1 | 10 | 0.6% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `1.687`
> **Composition Archetype:** `Small Flat Repo (2)` (z +1.69; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 23%, Data / Markup / Trivial 18%, Large Core Modules (3) 15%, Declarative / Non-Code 12%, Parameter Forwarders Files 9%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 146 | 89.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 17 | 10.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 431*

**Composition by Extension & Reason:**
- `.cy`: 324x Unsupported Format (.cy), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2578 LOC)
- `.c`: 43x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 19x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `no_extension`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 2x Excluded (Unsupported Extension: '.tmPreferences'), 1x Excluded (Unsupported Extension: '.sublime-syntax')
- `.wren`: 5x Unsupported Format (.wren)
- `.yml`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vim`: 4x Excluded (Unsupported Extension: '.vim')
- `.md`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.css`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.txt`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.html`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.js`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.json`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.def`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 92.2 | 18.1 | 10.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 51.5 | 62.8 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 9.1 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 14.8 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 34.4 | 16.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.5 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 32.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 9.5 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.1 | 0.9 | 0.5 | 2.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 28.3 | 15.6 | 15.6 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 72.5 | 95.7 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 9165 | 97 | 174 | `src/sema.zig` |
| cleanup | 655 | 51 | 12 | `src/sema.zig` |
| guards | 8158 | 85 | 124 | `src/sema.zig` |
| danger | 3398 | 85 | 62 | `src/sema.zig` |
| concurrency | 64 | 17 | 1 | `src/worker.zig` |
| connectivity | 4184 | 111 | 89 | `src/sema.zig` |
| io | 184 | 23 | 2 | `src/app_debug.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 50 | 11 | 0 | `src/app_debug.zig` |
| time | 54 | 27 | 2 | `examples/web-playground/index.html` |
| serialization | 0 | 0 | 0 | - |
| regex | 43 | 8 | 0 | `examples/web-playground/cyber-mode.js` |
| events | 17 | 8 | 0 | `examples/web-playground/index.html` |
| tests | 93 | 35 | 1 | `src/lib.zig` |
| docs | 904 | 63 | 20 | `src/sema.zig` |
| debt | 425 | 104 | 7 | `src/sema.zig` |
| mutation | 16376 | 135 | 223 | `src/sema.zig` |
| dead_code | 1247 | 78 | 17 | `src/llvm_gen.zig` |
| credential | 1 | 1 | 0 | `install.sh` |
| threat | 129 | 29 | 2 | `src/vm.h` |
| ml_ai | 330 | 35 | 2 | `src/std/math.zig` |
| ui | 3 | 2 | 0 | `examples/web-playground/index.html` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.1429**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/app_debug.zig` (Hits: 44)
- `src/platform.zig` (Hits: 32)
- `examples/web-playground/index.html` (Hits: 17)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **cyber.zig** (`src/cyber.zig`) — 52 inbound connections
2. **stdx.zig** (`src/stdx/stdx.zig`) — 41 inbound connections
3. **capi.zig** (`src/capi.zig`) — 40 inbound connections
4. **fmt.zig** (`src/fmt.zig`) — 15 inbound connections
5. **bc_gen.zig** (`src/bc_gen.zig`) — 8 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **cyber.zig** (`src/cyber.zig`) — 40 outbound dependencies
2. **compiler.zig** (`src/compiler.zig`) — 20 outbound dependencies
3. **vm.zig** (`src/vm.zig`) — 14 outbound dependencies
4. **cli.zig** (`src/cli.zig`) — 12 outbound dependencies
5. **core.zig** (`src/builtins/core.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `semaExprNoCheck` **(Many-Argument Workhorses)** (@ `src/sema.zig`) -> Impact: **340.6** | LOC: 1132
- `cyber` **(Compute Cores)** (@ `examples/web-playground/cyber-mode.js`) -> Impact: **254.0** | LOC: 384
- `evalExprNoCheck` **(Many-Argument Workhorses)** (@ `src/cte.zig`) -> Impact: **224.5** | LOC: 650
- `formatStringFactory` **(Compute Cores)** (@ `examples/web-playground/cyber-mode.js`) -> Impact: **175.0** | LOC: 210
- `tokenString` **(Compute Cores)** (@ `examples/web-playground/cyber-mode.js`) -> Impact: **161.7** | LOC: 185
- `tokenizeOne` **(Many-Argument Workhorses)** (@ `src/tokenizer.zig`) -> Impact: **139.1** | LOC: 323
  * *Intent:* /// Consumes the next token skipping whitespace and returns the next tokenizer state.
- `semaFitTarget` **(Many-Argument Workhorses)** (@ `src/sema.zig`) -> Impact: **138.6** | LOC: 267
- `write_inst` **(Many-Argument Workhorses)** (@ `src/bytecode.zig`) -> Impact: **125.3** | LOC: 495
- `switchStmt` **(Many-Argument Workhorses)** (@ `src/cte.zig`) -> Impact: **118.1** | LOC: 192
- `LinearFifo` **(Many-Argument Workhorses)** (@ `src/fifo.zig`) -> Impact: **113.1** | LOC: 391

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 61 | 28768.88 | 18.32% | 16.26% |
| `src/builtins` | 6 | 2219.32 | 22.29% | 7.05% |
| `src/jit` | 9 | 1721.96 | 25.45% | 13.58% |
| `src/test/bench/heap` | 6 | 1653.9 | 36.49% | 0.0% |
| `examples/web-playground` | 4 | 1022.62 | 45.69% | 0.0% |
| `src/stdx` | 7 | 552.62 | 20.63% | 11.52% |
| `src/std` | 5 | 539.28 | 11.39% | 15.7% |
| `src/test` | 1 | 256.7 | 19.57% | 0.0% |
| `examples/android/ndk_app` | 5 | 203.88 | 1.86% | 0.0% |
| `src/include` | 1 | 192.88 | 0.0% | 14.51% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/runtime.zig` -> **99.9791%** Exposure
- `src/aot.c` -> **99.9681%** Exposure
- `src/http.zig` -> **99.1089%** Exposure
- `src/fiber.zig` -> **96.4973%** Exposure
- `src/web.zig` -> **95.6274%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `install.sh` -> **100.0%** Exposure
- `src/dce.zig` -> **99.9998%** Exposure
- `src/sema_type.zig` -> **99.9997%** Exposure
- `src/vm.c` -> **99.9993%** Exposure
- `src/stdx/ds/stack.zig` -> **99.9973%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/aot.c` -> **34** Orphaned Functions | **0** Duplicates
- `src/runtime.zig` -> **25** Orphaned Functions | **0** Duplicates
- `src/test/ffi/test_lib.c` -> **19** Orphaned Functions | **0** Duplicates
- `src/fiber.zig` -> **16** Orphaned Functions | **0** Duplicates
- `src/std/os_ffi.zig` -> **13** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `467` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/sema.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 5574.06 | **LOC:** 10486 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 90.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.5%), Connectivity (formerly Api Exposure) (70.6%), Guard Balance (formerly Safety Score) (37.0%)
- **Documentation Coverage:** 92.6493% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `semaExprNoCheck` **(Many-Argument Workhorses)** (Impact: 340.6)
  * `semaFitTarget` **(Many-Argument Workhorses)** (Impact: 138.6)
  * `semaAssignStmt` **(Many-Argument Workhorses)** (Impact: 97.1)
    * *Intent:* /// Pass rightId explicitly to perform custom sema on op assign rhs.
  * `semaCallExpr` **(Defensive Guards)** (Impact: 80.7)
  * `resolveFuncSig` **(Many-Argument Workhorses)** (Impact: 74.6)
    * *Intent:* /// During body sema, all new types should be resolved.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 339 instances
* *High Risk Execution (weighted view):* 3
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 1193
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1262`, `structural_boundaries: 1343`, `args: 379`, `func_start: 379`, `class_start: 50`
* *Risk/State:* `safety_bypasses: 489`, `high_risk_execution: 10`, `state_mutation: 515`, `dead_code: 91`, `planned_debt: 45`
* *Architecture:* `api: 310`, `import: 8`
* *Defense:* `safety: 1725`, `doc: 97`, `test: 1`, `cleanup: 67`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 4):` build_options, builtin, capi.zig, cyber.zig, std, stdx, vm.zig, vmc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/parser.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 2286.78 | **LOC:** 4810 | **CtrlFlow:** 16.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%), Guard Balance (formerly Safety Score) (42.4%), Connectivity (formerly Api Exposure) (38.8%)
- **Documentation Coverage:** 89.6296% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseTightTermLeft` **(Many-Argument Workhorses)** (Impact: 84.9)
  * `parseExprWithLeft` **(Many-Argument Workhorses)** (Impact: 72.9)
  * `parseForCase` **(Defensive Guards)** (Impact: 62.9)
  * `parseFuncDecl` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `parseForStatement` **(Many-Argument Workhorses)** (Impact: 53.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 192 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 610
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 668`, `structural_boundaries: 727`, `args: 130`, `func_start: 121`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 134`, `state_mutation: 226`, `dead_code: 25`, `planned_debt: 3`
* *Architecture:* `api: 17`, `import: 6`
* *Defense:* `safety: 610`, `doc: 29`, `test: 1`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 4):` builtin, capi.zig, cyber.zig, fmt.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/bc_gen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1422.74 | **LOC:** 3082 | **CtrlFlow:** 11.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **5**; blast radius 9.712; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (86.5%), Connectivity (formerly Api Exposure) (70.4%), Complexity Load (formerly Cognitive Load) (20.0%)
- **Documentation Coverage:** 97.0149% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `genAll` **(Defensive Guards)** (Impact: 54.2)
  * `genCompare` **(Many-Argument Workhorses)** (Impact: 38.7)
  * `beginCall` **(Many-Argument Workhorses)** (Impact: 34.9)
    * *Intent:* /// Returns gen strategy and advances the temp local.
  * `gen_switch_stmt` **(Many-Argument Workhorses)** (Impact: 25.9)
  * `genBinOp` **(Defensive Guards)** (Impact: 24.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 82 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 278
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 287`, `structural_boundaries: 192`, `args: 166`, `func_start: 166`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 102`, `high_risk_execution: 4`, `state_mutation: 114`, `dead_code: 17`, `planned_debt: 11`
* *Architecture:* `api: 50`, `import: 5`
* *Defense:* `safety: 617`, `doc: 39`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.712
  * `Choke Point (Betweenness):` 0.000556 | `Ripple Effect (Closeness):` 0.135113
  * `Imports (Out-Degree: 3):` builtin, capi.zig, cyber.zig, gen.zig, std
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/cgen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 1288.4 | **LOC:** 3188 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (56.9%), Dead Code Surface (formerly Dead Code) (55.3%), Connectivity (formerly Api Exposure) (50.2%), Mutation Surface (formerly State Flux) (40.5%)
- **Documentation Coverage:** 93.6047% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `declareType` **(Many-Argument Workhorses)** (Impact: 83.0)
    * *Intent:* /// DFS declaration to ensure type dependencies are declared first.
  * `genBinOp` **(Many-Argument Workhorses)** (Impact: 82.7)
  * `gen` **(Defensive Guards)** (Impact: 54.2)
  * `genHeader` **(Defensive Guards)** (Impact: 45.0)
  * `genVmToExternFunc` **(Many-Argument Workhorses)** (Impact: 33.5)
    * *Intent:* /// If `func` is an extern variant (for variadic), `call_func` is the extern function. /// Otherwise...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 16 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 34 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 323`, `structural_boundaries: 180`, `args: 143`, `func_start: 143`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 40`, `high_risk_execution: 17`, `state_mutation: 63`, `dead_code: 100`, `planned_debt: 17`
* *Architecture:* `io: 7`, `api: 34`, `import: 7`
* *Defense:* `safety: 751`, `doc: 11`, `cleanup: 30`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 2):` build_config, builtin, capi.zig, cyber.zig, std, tcc, vmc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/cte.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1191.48 | **LOC:** 2800 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 88.9%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (83.0%), Connectivity (formerly Api Exposure) (51.8%), Guard Balance (formerly Safety Score) (32.9%), Mutation Surface (formerly State Flux) (26.3%)
- **Documentation Coverage:** 96.9072% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `evalExprNoCheck` **(Many-Argument Workhorses)** (Impact: 224.5)
  * `switchStmt` **(Many-Argument Workhorses)** (Impact: 118.1)
  * `eval_bin_expr2` **(Many-Argument Workhorses)** (Impact: 85.5)
  * `evalCallExpr` **(Many-Argument Workhorses)** (Impact: 37.9)
  * `eval_assign` **(Many-Argument Workhorses)** (Impact: 35.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 86
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 348`, `structural_boundaries: 449`, `args: 64`, `func_start: 63`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 92`, `high_risk_execution: 4`, `state_mutation: 34`, `dead_code: 27`, `planned_debt: 19`
* *Architecture:* `api: 36`, `import: 4`
* *Defense:* `safety: 332`, `doc: 6`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000279 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 3):` bc_gen.zig, capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sema_func.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1012.2 | **LOC:** 1430 | **CtrlFlow:** 17.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (65.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%), Connectivity (formerly Api Exposure) (46.9%)
- **Documentation Coverage:** 97.7778% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveRtArg` **(Many-Argument Workhorses)** (Impact: 112.8)
  * `matchPreArgCt` **(Many-Argument Workhorses)** (Impact: 55.2)
    * *Intent:* // Owns a copy of the argument, unless its obtaining a borrow to a receiver.
  * `matchTemplateArgCt` **(Many-Argument Workhorses)** (Impact: 49.7)
  * `matchTemplateArg` **(Many-Argument Workhorses)** (Impact: 46.3)
  * `matchFuncSym` **(Many-Argument Workhorses)** (Impact: 38.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 91 instances
* *State Mutation (weighted view):* 289
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 199`, `args: 30`, `func_start: 30`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 107`, `dead_code: 15`, `planned_debt: 7`
* *Architecture:* `api: 19`, `import: 3`
* *Defense:* `safety: 145`, `doc: 3`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 2):` capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/builtins/core.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 997.38 | **LOC:** 2220 | **CtrlFlow:** 8.6% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **10**; blast radius 7.584; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.5%), Connectivity (formerly Api Exposure) (79.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.0%), Guard Balance (formerly Safety Score) (64.7%)
- **Documentation Coverage:** 99.1379% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `intFmtExt` **(Type Conversions)** (Impact: 26.0)
  * `bitCast` **(Many-Argument Workhorses)** (Impact: 25.3)
  * `Int_init` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* /// Compile-time version of Int conversions. It should be faster than interpreting `Int[].@init`.
  * `rawFmtExt` **(Defensive Guards)** (Impact: 21.2)
  * `bitTrunc` **(Defensive Guards)** (Impact: 19.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 41 instances
* *Amplified Cascading Flux:* 54 instances
* *High Risk Execution (weighted view):* 2
* *State Mutation (weighted view):* 227
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 163`, `structural_boundaries: 283`, `args: 146`, `func_start: 146`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 123`, `high_risk_execution: 43`, `state_mutation: 119`, `dead_code: 12`, `planned_debt: 7`, `duplicate_logic: 2`
* *Architecture:* `api: 89`, `import: 10`
* *Defense:* `safety: 210`, `doc: 1`, `sync_locks: 2`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.584
  * `Choke Point (Betweenness):` 0.00183 | `Ripple Effect (Closeness):` 0.176686
  * `Imports (Out-Degree: 6):` capi.zig, cyber.zig, fmt.zig, bindings.zig, build_options, builtin, cy.zig, std...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/heap.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 993.5 | **LOC:** 1828 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.3%), Connectivity (formerly Api Exposure) (90.0%), Guard Balance (formerly Safety Score) (74.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%)
- **Documentation Coverage:** 88.8031% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `allocClosure` **(Many-Argument Workhorses)** (Impact: 21.1)
    * *Intent:* /// Captured values are retained during alloc.
  * `deinit` **(Defensive Guards)** (Impact: 19.1)
  * `freePoolObject` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* /// typeId should be cleared in trace mode since tracking may still hold a reference to the object. ...
  * `allocVector` **(Type Conversions)** (Impact: 15.2)
    * *Intent:* /// Reuse `Object` so that address_of refers to the first element for both structs and arrays.
  * `newInstance` **(Defensive Guards)** (Impact: 11.4)
    * *Intent:* /// Arguments are consumed.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 61 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 224
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 158`, `args: 132`, `func_start: 132`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 101`, `high_risk_execution: 6`, `state_mutation: 102`, `dead_code: 3`
* *Architecture:* `api: 255`, `import: 8`
* *Defense:* `safety: 131`, `doc: 34`, `test: 2`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.76
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` build_config, builtin, capi.zig, cyber.zig, heap_value.zig, std, stdx, tcc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sema_type.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 969.54 | **LOC:** 1339 | **CtrlFlow:** 14.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (92.5%), Complexity Load (formerly Cognitive Load) (59.3%), Connectivity (formerly Api Exposure) (58.3%)
- **Documentation Coverage:** 81.7073% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveStructFields` **(Many-Argument Workhorses)** (Impact: 46.9)
    * *Intent:* /// Explicit `decl` node for distinct type declarations. Must belong to `c`.
  * `declare_choice_cases` **(Many-Argument Workhorses)** (Impact: 30.0)
  * `ensure_resolved_type` **(Many-Argument Workhorses)** (Impact: 25.8)
  * `reifyStructType` **(Many-Argument Workhorses)** (Impact: 24.4)
  * `implements` **(Many-Argument Workhorses)** (Impact: 24.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 112 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 428
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 160`, `structural_boundaries: 136`, `args: 44`, `func_start: 44`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 132`, `high_risk_execution: 3`, `state_mutation: 204`, `dead_code: 3`, `planned_debt: 4`
* *Architecture:* `api: 39`, `import: 3`
* *Defense:* `safety: 172`, `doc: 8`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 2):` capi.zig, cyber.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/web-playground/cyber-mode.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Drift: 0.0 IQR)
- **Magnitude:** 880.88 | **LOC:** 385 | **CtrlFlow:** 54.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 3.933; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (99.3%), Complexity Load (formerly Cognitive Load) (92.2%), Concurrency Surface (formerly Concurrency) (71.5%), Connectivity (formerly Api Exposure) (13.3%)
- **Documentation Coverage:** 88.408% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cyber` **(Compute Cores)** (Impact: 254.0)
  * `formatStringFactory` **(Compute Cores)** (Impact: 175.0)
  * `tokenString` **(Compute Cores)** (Impact: 161.7)
  * `tokenBaseInner` **(Many-Argument Workhorses)** (Impact: 76.0)
  * `tokenBase` **(Compute Cores)** (Impact: 25.3)
    * *Intent:* // tokenizers
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 52 instances
* *Concurrency (weighted view):* 12
* *State Mutation (weighted view):* 156
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 95`, `args: 19`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 39`, `state_mutation: 52`, `dead_code: 1`, `planned_debt: 1`
* *Architecture:* `api: 1`, `concurrency: 2`
* *Defense:* `safety: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vm.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 750.38 | **LOC:** 1771 | **CtrlFlow:** 7.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (93.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.6%), Complexity Load (formerly Cognitive Load) (85.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `execBytecode` **(Many-Argument Workhorses)** (Impact: 63.9)
  * `ipow` **(Stateful Encapsulated Methods)** (Impact: 16.7)
    * *Intent:* // Exponentiation by squaring.
  * `retain` **(Stateful Encapsulated Methods)** (Impact: 12.5)
  * `releaseOnly` **(Stateful Encapsulated Methods)** (Impact: 11.2)
  * `allocObjectInit` **(Stateful Encapsulated Methods)** (Impact: 8.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 116 instances
* *State Mutation (weighted view):* 540
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 115`, `structural_boundaries: 82`, `args: 309`, `func_start: 27`
* *Risk/State:* `safety_bypasses: 54`, `state_mutation: 308`, `dead_code: 15`, `planned_debt: 3`, `unreferenced_by_name: 11`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 18`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.76
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdarg.h, vm.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/thread.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 692.66 | **LOC:** 1226 | **CtrlFlow:** 12.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (87.0%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (70.5%)
- **Documentation Coverage:** 83.5616% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `callUnion` **(Many-Argument Workhorses)** (Impact: 23.7)
  * `unwindStack` **(Many-Argument Workhorses)** (Impact: 22.4)
    * *Intent:* /// Unwind from `ctx` and release each frame. /// TODO: See if releaseFiberStack can resuse the same...
  * `markValue` **(Many-Argument Workhorses)** (Impact: 19.3)
    * *Intent:* /// Assumes `v` is a cyclable pointer.
  * `freeHeapPages` **(Type Conversions)** (Impact: 14.0)
    * *Intent:* /// Sweep frees each heap object disregarding any dependencies. Triggered from fatal error. /// Only...
  * `callTraitSymInst` **(Many-Argument Workhorses)** (Impact: 12.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 9 instances
* *Amplified Cascading Flux:* 51 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 117`, `args: 75`, `func_start: 75`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 78`, `high_risk_execution: 9`, `state_mutation: 116`, `dead_code: 4`, `planned_debt: 8`
* *Architecture:* `api: 81`, `import: 8`
* *Defense:* `safety: 66`, `doc: 24`, `test: 1`, `cleanup: 17`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 4):` build_config, builtin, capi.zig, cyber.zig, fmt.zig, std, stdx, vmc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/vm.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 657.74 | **LOC:** 1397 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **14**; blast radius 8.023; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.4%), Connectivity (formerly Api Exposure) (80.9%), Guard Balance (formerly Safety Score) (65.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%)
- **Documentation Coverage:** 95.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deinit` **(Many-Argument Workhorses)** (Impact: 69.1)
  * `eval` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `zAwait` **(Compute Cores)** (Impact: 17.8)
  * `dumpValue` **(Compute Cores)** (Impact: 16.9)
    * *Intent:* /// Like Value.dump but shows heap values.
  * `findType` **(Defensive Guards)** (Impact: 14.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 1
* *Concurrency (weighted view):* 15
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 120`, `structural_boundaries: 117`, `args: 83`, `func_start: 82`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 70`, `high_risk_execution: 7`, `state_mutation: 66`, `dead_code: 14`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 97`, `concurrency: 5`, `import: 14`
* *Defense:* `safety: 107`, `doc: 19`, `test: 1`, `sync_locks: 1`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.023
  * `Choke Point (Betweenness):` 0.002669 | `Ripple Effect (Closeness):` 0.176686
  * `Imports (Out-Degree: 8):` bc_gen.zig, build_config, builtin, bindings.zig, core.zig, capi.zig, cyber.zig, debug.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/sym.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 653.34 | **LOC:** 1733 | **CtrlFlow:** 8.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (73.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.0%), Guard Balance (formerly Safety Score) (49.2%), Mutation Surface (formerly State Flux) (19.8%)
- **Documentation Coverage:** 95.7447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeSymName` **(Many-Argument Workhorses)** (Impact: 80.6)
  * `declNode` **(Type Conversions)** (Impact: 18.6)
  * `writeTemplateParam` **(Many-Argument Workhorses)** (Impact: 14.0)
  * `writeVariantParam` **(Defensive Guards)** (Impact: 12.5)
  * `writeFuncName` **(Defensive Guards)** (Impact: 12.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 11 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 126`, `structural_boundaries: 163`, `args: 98`, `func_start: 97`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 88`, `high_risk_execution: 4`, `state_mutation: 15`, `dead_code: 3`, `planned_debt: 5`, `fragile_debt: 1`
* *Architecture:* `api: 122`, `import: 5`
* *Defense:* `safety: 159`, `doc: 38`, `test: 1`, `cleanup: 49`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 3):` builtin, capi.zig, cyber.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/compiler.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 647.6 | **LOC:** 1504 | **CtrlFlow:** 11.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **20**; blast radius 5.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.6%), Connectivity (formerly Api Exposure) (53.9%), Guard Balance (formerly Safety Score) (28.9%)
- **Documentation Coverage:** 82.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `compileInner` **(Many-Argument Workhorses)** (Impact: 100.0)
    * *Intent:* /// Wrap compile so all errors can be handled in one place.
  * `deinit` **(Many-Argument Workhorses)** (Impact: 39.6)
  * `reserveChunkSyms` **(Defensive Guards)** (Impact: 24.8)
    * *Intent:* // /// `src` is consumed. // pub fn createModule(self: *Compiler, r_uri: []const u8, src: ?[]const u...
  * `loadChunk` **(Defensive Guards)** (Impact: 17.9)
  * `semaChunkFuncs` **(Defensive Guards)** (Impact: 15.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 30 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 137`, `structural_boundaries: 107`, `args: 46`, `func_start: 45`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 48`, `high_risk_execution: 1`, `state_mutation: 139`, `dead_code: 9`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 31`, `import: 20`
* *Defense:* `safety: 262`, `doc: 30`, `test: 1`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.015727 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 16):` bc_gen.zig, build_options, builtin, c.zig, core.zig, cy.zig, meta.zig, capi.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/heap_value.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 631.24 | **LOC:** 1171 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 3.346; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.0%), Connectivity (formerly Api Exposure) (60.2%), Mutation Surface (formerly State Flux) (38.1%)
- **Documentation Coverage:** 92.8571% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `destroyObject` **(Many-Argument Workhorses)** (Impact: 108.3)
  * `writeValue` **(Many-Argument Workhorses)** (Impact: 56.5)
    * *Intent:* /// Assumes `val` is unboxed. /// Returns whether the string written can be assumed to be ASCII. ///...
  * `destructValueAt` **(Many-Argument Workhorses)** (Impact: 29.9)
  * `bufPrintValueShortStr` **(Defensive Guards)** (Impact: 28.1)
  * `copyValueTo` **(Many-Argument Workhorses)** (Impact: 26.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 17 instances
* *High Risk Execution (weighted view):* 14
* *State Mutation (weighted view):* 52
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 179`, `structural_boundaries: 100`, `args: 43`, `func_start: 43`
* *Risk/State:* `safety_bypasses: 64`, `high_risk_execution: 16`, `state_mutation: 18`, `dead_code: 6`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 41`, `import: 6`
* *Defense:* `safety: 77`, `doc: 5`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.346
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 2):` build_config, capi.zig, cyber.zig, std, tcc, vmc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/types.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 612.02 | **LOC:** 1508 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (78.6%), Guard Balance (formerly Safety Score) (70.5%), Mutation Surface (formerly State Flux) (23.2%)
- **Documentation Coverage:** 89.8305% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `isRtTypeCompat` **(Many-Argument Workhorses)** (Impact: 23.3)
  * `get_trait_method_impl` **(Defensive Guards)** (Impact: 15.4)
    * *Intent:* /// Assumes types and functions are already resolved.
  * `createTypeWithId` **(Many-Argument Workhorses)** (Impact: 14.8)
  * `isConstEligible` **(Defensive Guards)** (Impact: 13.5)
    * *Intent:* /// What is const eligible is a subset of what is eval eligible. /// The type must be immutable.
  * `pointeeOrSelf` **(Compute Cores)** (Impact: 10.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 10 instances
* *High Risk Execution (weighted view):* 7
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 206`, `args: 92`, `func_start: 90`, `class_start: 31`
* *Risk/State:* `safety_bypasses: 54`, `high_risk_execution: 10`, `state_mutation: 17`, `dead_code: 3`, `planned_debt: 9`
* *Architecture:* `api: 155`, `import: 6`
* *Defense:* `safety: 33`, `doc: 40`, `test: 1`, `cleanup: 48`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 4):` capi.zig, cyber.zig, fmt.zig, std, stdx, vmc
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/tokenizer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 607.66 | **LOC:** 1219 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (75.2%), Connectivity (formerly Api Exposure) (45.4%), Guard Balance (formerly Safety Score) (29.4%), Complexity Load (formerly Cognitive Load) (25.0%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `tokenizeOne` **(Many-Argument Workhorses)** (Impact: 139.1)
    * *Intent:* /// Consumes the next token skipping whitespace and returns the next tokenizer state.
  * `tokenizeStringOne` **(Many-Argument Workhorses)** (Impact: 86.1)
    * *Intent:* /// Returns the next tokenizer state.
  * `tokenizeNumber` **(Many-Argument Workhorses)** (Impact: 72.5)
    * *Intent:* /// Assumes first digit is consumed.
  * `tokenize` **(Defensive Guards)** (Impact: 24.4)
  * `tokenizeMultiLineRawString` **(Defensive Guards)** (Impact: 20.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 32 instances
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 214`, `structural_boundaries: 108`, `args: 33`, `func_start: 32`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 35`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 3`
* *Defense:* `safety: 137`, `doc: 12`, `test: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 2):` cyber.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/chunk.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 529.18 | **LOC:** 912 | **CtrlFlow:** 10.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 5.088; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.8%), Connectivity (formerly Api Exposure) (84.9%), Test Surface (formerly Verification) (80.0%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (75.0%)
- **Documentation Coverage:** 87.7551% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `patchForBlockJumps` **(Many-Argument Workhorses)** (Impact: 28.5)
  * `patchBreaks` **(Type Conversions)** (Impact: 19.1)
  * `nextTempDestValue` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* /// Given two local values, determine the next destination temp local. /// The type of the dest valu...
  * `deinit` **(I/O & Config Routines)** (Impact: 11.9)
  * `addReportFmt` **(Defensive Guards)** (Impact: 11.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 3 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 96
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 51`, `args: 50`, `func_start: 49`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 43`, `high_risk_execution: 3`, `state_mutation: 38`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 160`, `import: 10`
* *Defense:* `safety: 45`, `doc: 45`, `test: 1`, `cleanup: 39`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.004853 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 8):` bc_gen.zig, builtin, capi.zig, cyber.zig, gen.zig, x64.zig, llvm.zig, llvm_gen.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/string.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 513.14 | **LOC:** 776 | **CtrlFlow:** 16.6% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 2.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (82.5%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (65.2%)
- **Documentation Coverage:** 81.8182% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `indexOfAsciiSetSimdFixed` **(Many-Argument Workhorses)** (Impact: 25.6)
  * `indexOfAsciiSetSimdRemain` **(Many-Argument Workhorses)** (Impact: 23.4)
  * `indexOfCharSimdFixed4` **(Type Conversions)** (Impact: 21.0)
  * `indexOfChar` **(Defensive Guards)** (Impact: 17.0)
    * *Intent:* /// For Ascii needle.
  * `ustringSeekByRuneIndex` **(Many-Argument Workhorses)** (Impact: 16.0)
    * *Intent:* /// `out_bad_byte` can be used to determine if it's an ascii string.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 47 instances
* *State Mutation (weighted view):* 160
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 125`, `args: 42`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 66`, `dead_code: 3`, `planned_debt: 3`
* *Architecture:* `api: 34`, `import: 4`
* *Defense:* `safety: 45`, `doc: 13`, `test: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.76
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` builtin, cyber.zig, std, stdx
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/lib.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 480.26 | **LOC:** 1063 | **CtrlFlow:** 3.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **8**; blast radius 3.542; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.1%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%)
- **Documentation Coverage:** 99.0741% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `cl_vm_evalx` **(Many-Argument Workhorses)** (Impact: 8.5)
  * `cl_vm_eval_path` **(Many-Argument Workhorses)** (Impact: 7.9)
  * `cl_vm_compile` **(Defensive Guards)** (Impact: 7.5)
  * `cl_vm_error_summary` **(Compute Cores)** (Impact: 7.5)
  * `loader` **(Compute Cores)** (Impact: 7.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 15 instances
* *Amplified Cascading Flux:* 25 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 26`, `structural_boundaries: 138`, `args: 120`, `func_start: 113`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 15`, `state_mutation: 47`, `dead_code: 16`, `planned_debt: 1`
* *Architecture:* `api: 109`, `import: 8`
* *Defense:* `safety: 99`, `doc: 1`, `test: 15`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.542
  * `Choke Point (Betweenness):` 0.00023 | `Ripple Effect (Closeness):` 0.006173
  * `Imports (Out-Degree: 4):` build_config, builtin, meta.zig, capi.zig, cyber.zig, mimalloc, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/jit/x64_assembler.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 459.16 | **LOC:** 637 | **CtrlFlow:** 11.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 5.458; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (72.6%), Connectivity (formerly Api Exposure) (71.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%)
- **Documentation Coverage:** 95.7447% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `encodeMemory` **(Many-Argument Workhorses)** (Impact: 65.6)
  * `encodeRexPrefix` **(Many-Argument Workhorses)** (Impact: 26.4)
  * `encode` **(Many-Argument Workhorses)** (Impact: 21.9)
  * `encodeHeader` **(Many-Argument Workhorses)** (Impact: 12.7)
  * `encodeRMOps` **(Many-Argument Workhorses)** (Impact: 8.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 152
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 35`, `args: 53`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `state_mutation: 58`, `dead_code: 5`, `planned_debt: 4`
* *Architecture:* `api: 44`, `import: 7`
* *Defense:* `safety: 103`, `doc: 2`, `test: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.458
  * `Choke Point (Betweenness):` 0.000177 | `Ripple Effect (Closeness):` 0.124157
  * `Imports (Out-Degree: 5):` cyber.zig, assembler.zig, builtin, gen.zig, std, stdx, x64.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/debug.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 455.88 | **LOC:** 878 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **8**; blast radius 2.76; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (90.1%), Connectivity (formerly Api Exposure) (73.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.2%), Guard Balance (formerly Safety Score) (38.3%)
- **Documentation Coverage:** 88.3721% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `write_object_trace` **(Defensive Guards)** (Impact: 21.7)
  * `dumpBytecode` **(Defensive Guards)** (Impact: 21.0)
    * *Intent:* /// When `optPcContext` is null, all the bytecode is dumped along with constants. /// When `optPcCon...
  * `write_value_desc` **(Defensive Guards)** (Impact: 17.6)
  * `compactToStackFrame` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* /// Can only rely on pc and other non-reference values to build the stack frame since /// unwinding ...
  * `writeStackFrames` **(Defensive Guards)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 26 instances
* *High Risk Execution (weighted view):* 2
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 84
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 108`, `args: 46`, `func_start: 46`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 6`, `state_mutation: 32`, `dead_code: 14`, `planned_debt: 4`
* *Architecture:* `io: 1`, `api: 43`, `import: 8`
* *Defense:* `safety: 138`, `doc: 7`, `test: 1`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.76
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` builtin, bytecode.zig, capi.zig, cyber.zig, fmt.zig, std, stdx, vmc
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/jit/gen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 443.8 | **LOC:** 1087 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **10**; blast radius 12.884; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Dead Code Surface (formerly Dead Code) (90.0%), Mutation Surface (formerly State Flux) (89.8%), Connectivity (formerly Api Exposure) (71.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gen_func` **(Many-Argument Workhorses)** (Impact: 60.6)
  * `genStmt` **(Defensive Guards)** (Impact: 26.6)
  * `genExpr` **(Defensive Guards)** (Impact: 19.6)
  * `mainBlock` **(Defensive Guards)** (Impact: 18.0)
  * `prepareFunc` **(Generic / Templated Code)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 24 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 91
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 48`, `args: 41`, `func_start: 41`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 37`, `high_risk_execution: 2`, `state_mutation: 43`, `dead_code: 58`, `planned_debt: 11`
* *Architecture:* `io: 9`, `api: 33`, `import: 12`
* *Defense:* `safety: 150`, `doc: 6`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 12.884
  * `Choke Point (Betweenness):` 0.010351 | `Ripple Effect (Closeness):` 0.180859
  * `Imports (Out-Degree: 8):` bc_gen.zig, capi.zig, cyber.zig, a64.zig, a64_assembler.zig, assembler.zig, builtin, std...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/module.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 433.0 | **LOC:** 670 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **6**; blast radius 5.088; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.8%), Mutation Surface (formerly State Flux) (62.6%), Guard Balance (formerly Safety Score) (47.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (46.1%)
- **Documentation Coverage:** 94.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getResolvedSym` **(Defensive Guards)** (Impact: 55.0)
    * *Intent:* /// Note that resolved refers to a resolved symbol path and not the underlying symbol content.
  * `getRefLikeChildSym` **(Defensive Guards)** (Impact: 37.4)
  * `reserveFunc` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `get_pub_resolved_chunk_sym` **(Many-Argument Workhorses)** (Impact: 15.2)
  * `reserveVariantFunc` **(Defensive Guards)** (Impact: 12.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 8 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 43
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 80`, `args: 53`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 65`, `high_risk_execution: 2`, `state_mutation: 27`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 53`, `import: 6`
* *Defense:* `safety: 124`, `doc: 7`, `test: 1`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.088
  * `Choke Point (Betweenness):` 0.000178 | `Ripple Effect (Closeness):` 0.171411
  * `Imports (Out-Degree: 3):` build_options, builtin, capi.zig, cyber.zig, std, stdx
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/vm.c` -> Churn: **89.62%** | Cog Load: 85.4856% | Debt: 23.0099%
- `src/jit/stencils.c` -> Churn: **75.0%** | Cog Load: 67.5063% | Debt: 19.0407%
- `src/jit/a64_assembler.zig` -> Churn: **70.18%** | Cog Load: 41.4929% | Debt: 77.379%
- `src/jit/x64_assembler.zig` -> Churn: **70.18%** | Cog Load: 72.6201% | Debt: 11.3338%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sema.zig` -> **fubark** (90.0% isolated ownership) | Magnitude: 5574.06
- `src/parser.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 2286.78
- `src/bc_gen.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 1422.74
- `src/cgen.zig` -> **fubark** (100.0% isolated ownership) | Magnitude: 1288.4
- `src/cte.zig` -> **fubark** (88.9% isolated ownership) | Magnitude: 1191.48

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/compiler.zig` -> **Severity: 1.548** (Bridge: 0.0157 * Flux: 98.4087%)
- `src/jit/gen.zig` -> **Severity: 0.93** (Bridge: 0.0104 * Flux: 89.8313%)
- `src/std/os.zig` -> **Severity: 0.49** (Bridge: 0.0074 * Flux: 66.3052%)
- `src/chunk.zig` -> **Severity: 0.46** (Bridge: 0.0049 * Flux: 94.8037%)
- `src/cli.zig` -> **Severity: 0.447** (Bridge: 0.0062 * Flux: 72.0098%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/cyber.zig` -> **Severity: 23.718** (Embedded: 0.3104 * Error Risk: 76.414%)
- `src/capi.zig` -> **Severity: 20.006** (Embedded: 0.2816 * Error Risk: 71.0425%)
- `src/sema_type.zig` -> **Severity: 15.856** (Embedded: 0.1714 * Error Risk: 92.5047%)
- `src/simd.zig` -> **Severity: 15.315** (Embedded: 0.1745 * Error Risk: 87.7764%)
- `src/thread.zig` -> **Severity: 14.913** (Embedded: 0.1714 * Error Risk: 87.0005%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/cyber.zig` -> **Severity: 6778.425** (Blast Radius: 90.379 * Doc Risk: 75.0%)
- `src/capi.zig` -> **Severity: 5418.2** (Blast Radius: 54.182 * Doc Risk: 100.0%)
- `src/stdx/time.zig` -> **Severity: 3913.8** (Blast Radius: 39.138 * Doc Risk: 100.0%)
- `src/stdx/time_wasm.zig` -> **Severity: 3603.5** (Blast Radius: 36.035 * Doc Risk: 100.0%)
- `src/stdx/testing.zig` -> **Severity: 2623.7** (Blast Radius: 26.237 * Doc Risk: 100.0%)

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
