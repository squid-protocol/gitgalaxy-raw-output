# ARCHITECTURAL_BRIEF: zls
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/zigtools/zls.git` |
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
- **Scope:** 130 analyzed artifact(s), 58116 LOC.
- **Load-bearing artifact:** `src/zls.zig` -- 24 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/zls.zig` -- pulls in 35 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/analysis.zig` at magnitude 4057.38 (structural weight, not risk).
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
| Total Artifacts | 134 |
| Analyzed Artifacts (Scanned) | 130 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4 |
| Total LOC | 58116 |
| Volatility Index | 0.046 |
| % Scanned of codebase = | 97.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3973 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5231 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 18.5% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.3069 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 106 | 49527 | 81.5% |
| JSON | 10 | 451 | 7.7% |
| YAML | 6 | 246 | 4.6% |
| MARKDOWN | 3 | 0 | 2.3% |
| XML | 2 | 0 | 1.5% |
| NIX | 2 | 103 | 1.5% |
| HTML | 1 | 7789 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 130 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 42%, Data / Markup / Trivial 23%, Declarative / Non-Code 14%, State Mutators Files 7%, Many-Argument Workhorses Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 127 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4*

**Composition by Extension & Reason:**
- `no_extension`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (Unsupported Extension: '.lock')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 38.5 | 5.6 | 3.2 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.2 | 26.6 | 32.6 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 2.6 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.5 | 0.0 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 19.9 | 3.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 46.9 | 1.4 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 9.5 | 0.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 14.2 | 2.1 | 0.8 | 0.1 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 26.4 | 19.9 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 60.5 | 83.3 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 854 | 71 | 21 | `src/analyser/InternPool.zig` |
| cleanup | 696 | 57 | 11 | `src/DocumentStore.zig` |
| guards | 8764 | 81 | 163 | `src/analysis.zig` |
| danger | 1284 | 78 | 28 | `src/analyser/InternPool.zig` |
| concurrency | 215 | 16 | 2 | `src/analyser/InternPool.zig` |
| connectivity | 1000 | 78 | 17 | `src/analysis.zig` |
| io | 86 | 4 | 0 | `src/tools/langref.html.in` |
| crypto | 0 | 0 | 0 | - |
| ipc | 4 | 3 | 0 | `src/build_runner/shared.zig` |
| time | 0 | 0 | 0 | - |
| serialization | 4 | 3 | 0 | `src/DocumentStore.zig` |
| regex | 0 | 0 | 0 | - |
| events | 40 | 17 | 1 | `tests/analysis_check.zig` |
| tests | 843 | 36 | 18 | `tests/lsp_features/completion.zig` |
| docs | 1222 | 66 | 28 | `src/analyser/InternPool.zig` |
| debt | 263 | 51 | 7 | `src/analyser/InternPool.zig` |
| mutation | 9881 | 109 | 171 | `src/analysis.zig` |
| dead_code | 75 | 29 | 1 | `tests/analysis/capture.zig` |
| credential | 6 | 2 | 0 | `build.zig.zon` |
| threat | 0 | 0 | 0 | - |
| ml_ai | 259 | 30 | 3 | `src/analyser/InternPool.zig` |
| ui | 50 | 1 | 0 | `src/tools/langref.html.in` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **2.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/tools/langref.html.in` (Hits: 78)
- `.github/workflows/artifacts.yml` (Hits: 5)
- `src/build_runner/shared.zig` (Hits: 2)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **zls.zig** (`src/zls.zig`) — 24 inbound connections
2. **offsets.zig** (`src/offsets.zig`) — 22 inbound connections
3. **ast.zig** (`src/ast.zig`) — 17 inbound connections
4. **tracy.zig** (`src/tracy.zig`) — 17 inbound connections
5. **DocumentStore.zig** (`src/DocumentStore.zig`) — 15 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **zls.zig** (`src/zls.zig`) — 35 outbound dependencies
2. **Server.zig** (`src/Server.zig`) — 28 outbound dependencies
3. **tests.zig** (`tests/tests.zig`) — 19 outbound dependencies
4. **DocumentStore.zig** (`src/DocumentStore.zig`) — 14 outbound dependencies
5. **completions.zig** (`src/features/completions.zig`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `resolveTypeOfNodeUncached` **(Many-Argument Workhorses)** (@ `src/analysis.zig`) -> Impact: **442.6** | LOC: 1092
- `main` **(Defensive Guards)** (@ `src/build_runner/build_runner.zig`) -> Impact: **269.3** | LOC: 437
- `resolvePeerTypes` **(Many-Argument Workhorses)** (@ `src/analyser/InternPool.zig`) -> Impact: **234.8** | LOC: 495
- `getPositionContext` **(Many-Argument Workhorses)** (@ `src/analysis.zig`) -> Impact: **215.8** | LOC: 291
  * *Intent:* /// Given a byte index in a document (typically cursor offset), classify what kind of entity is at that index. /// /// Classification is based on the ...
- `resolveExpressionTypeFromAncestors` **(Many-Argument Workhorses)** (@ `src/analysis.zig`) -> Impact: **211.3** | LOC: 424
- `writeNodeTokens` **(Many-Argument Workhorses)** (@ `src/features/semantic_tokens.zig`) -> Impact: **193.1** | LOC: 675
- `getFieldAccessType` **(Many-Argument Workhorses)** (@ `src/analysis.zig`) -> Impact: **167.3** | LOC: 215
- `initializeHandler` **(Many-Argument Workhorses)** (@ `src/Server.zig`) -> Impact: **160.2** | LOC: 244
- `getSignatureInfo` **(Many-Argument Workhorses)** (@ `src/features/signature_help.zig`) -> Impact: **137.5** | LOC: 252
- `lastToken` **(Many-Argument Workhorses)** (@ `src/ast.zig`) -> Impact: **126.2** | LOC: 410
  * *Intent:* /// Similar to `std.zig.Ast.lastToken` but also handles ASTs with syntax errors.

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 20 | 10111.94 | 10.2% | 4.03% |
| `src/features` | 13 | 4261.72 | 13.49% | 4.93% |
| `src/analyser` | 8 | 2305.2 | 8.14% | 4.03% |
| `src/build_runner` | 3 | 1088.98 | 18.2% | 2.73% |
| `tests/lsp_features` | 13 | 887.16 | 2.73% | 0.0% |
| `tests` | 9 | 586.08 | 4.16% | 0.0% |
| `tests/analysis` | 25 | 429.52 | 2.67% | 0.0% |
| `tests/utility` | 3 | 310.22 | 2.61% | 0.0% |
| `__monolith__` | 7 | 219.58 | 1.07% | 0.0% |
| `tests/build_runner_cases` | 16 | 148.76 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `.github/ISSUE_TEMPLATE/bug.yml` -> **99.9998%** Exposure
- `.github/workflows/prepare_release_payload.zig` -> **23.1244%** Exposure
- `src/features/diagnostics.zig` -> **18.8978%** Exposure
- `src/DocumentScope.zig` -> **16.5889%** Exposure
- `src/analyser/segmented_list.zig` -> **12.2798%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/analyser/segmented_list.zig` -> **99.9892%** Exposure
- `src/tools/config_gen.zig` -> **98.5157%** Exposure
- `src/ast.zig` -> **98.3683%** Exposure
- `src/build_runner/build_runner.zig` -> **98.2542%** Exposure
- `src/features/signature_help.zig` -> **95.5794%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `tests/analysis/capture.zig` -> **12** Orphaned Functions | **0** Duplicates
- `tests/analysis/assign_destructure.zig` -> **7** Orphaned Functions | **0** Duplicates
- `tests/analysis/optional.zig` -> **7** Orphaned Functions | **0** Duplicates
- `tests/analysis/either.zig` -> **3** Orphaned Functions | **2** Duplicates
- `tests/analysis/generics.zig` -> **5** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `324` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/analysis.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.507)
- **Top Global Matches:** file_cluster_4: 7.507, file_cluster_6: 11.622, file_cluster_12: 12.558
- **Magnitude:** 4057.38 | **LOC:** 7016 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 44.8%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **12**; blast radius 13.849; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (100.0%), Connectivity (formerly Api Exposure) (88.5%), Mutation Surface (formerly State Flux) (65.4%), Guard Balance (formerly Safety Score) (32.2%)
- **Documentation Coverage:** 84.1791% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveTypeOfNodeUncached` **(Many-Argument Workhorses)** (Impact: 442.6)
  * `getPositionContext` **(Many-Argument Workhorses)** (Impact: 215.8)
    * *Intent:* /// Given a byte index in a document (typically cursor offset), classify what kind of entity is at t...
  * `resolveExpressionTypeFromAncestors` **(Many-Argument Workhorses)** (Impact: 211.3)
  * `getFieldAccessType` **(Many-Argument Workhorses)** (Impact: 167.3)
  * `rawStringify` **(Many-Argument Workhorses)** (Impact: 114.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 150 instances
* *Memory Alloc (weighted view):* 19
* *State Mutation (weighted view):* 463
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1357`, `structural_boundaries: 1369`, `args: 197`, `func_start: 197`, `class_start: 37`
* *Risk/State:* `safety_bypasses: 55`, `state_mutation: 163`, `dead_code: 1`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 168`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 1439`, `doc: 111`, `test: 1`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 13.849
  * `Choke Point (Betweenness):` 0.012186 | `Ripple Effect (Closeness):` 0.191111
  * `Imports (Out-Degree: 9):` DocumentScope.zig, DocumentStore.zig, Uri.zig, InternPool.zig, error_msg.zig, ast.zig, builtin, references.zig...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `src/analyser/InternPool.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 9.032)
- **Top Global Matches:** file_cluster_4: 9.032, file_cluster_12: 9.309, file_cluster_5: 11.275
- **Magnitude:** 1679.2 | **LOC:** 5361 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 56.2%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **5**; blast radius 18.618; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (77.1%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.5%), Guard Balance (formerly Safety Score) (31.8%), Mutation Surface (formerly State Flux) (26.8%)
- **Documentation Coverage:** 76.5336% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolvePeerTypes` **(Many-Argument Workhorses)** (Impact: 234.8)
  * `printInternal` **(Many-Argument Workhorses)** (Impact: 107.7)
  * `coerce` **(Many-Argument Workhorses)** (Impact: 102.3)
    * *Intent:* // --------------------------------------------- // UTILITY // -------------------------------------...
  * `eqlCustom` **(Many-Argument Workhorses)** (Impact: 94.4)
  * `coerceInMemoryAllowed` **(Many-Argument Workhorses)** (Impact: 64.8)
    * *Intent:* /// If types have the same representation in runtime memory /// * int/float: same number of bits ///...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 47 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 153
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 455`, `structural_boundaries: 573`, `args: 134`, `func_start: 113`, `class_start: 68`
* *Risk/State:* `safety_bypasses: 114`, `high_risk_execution: 2`, `state_mutation: 59`, `dead_code: 5`, `planned_debt: 32`
* *Architecture:* `api: 130`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 1050`, `doc: 166`, `test: 48`, `sync_locks: 80`, `cleanup: 63`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 18.618
  * `Choke Point (Betweenness):` 0.003886 | `Ripple Effect (Closeness):` 0.141406
  * `Imports (Out-Degree: 3):` builtin, error_msg.zig, segmented_list.zig, std, string_pool.zig
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/features/completions.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.05)
- **Top Global Matches:** file_cluster_6: 6.05, file_cluster_8: 11.629, file_cluster_4: 13.312
- **Magnitude:** 1221.78 | **LOC:** 1872 | **CtrlFlow:** 26.1% | **Authorship Centralization:** 68.4%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 6.685; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (89.8%), Connectivity (formerly Api Exposure) (38.5%), Guard Balance (formerly Safety Score) (38.4%)
- **Documentation Coverage:** 91.3043% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSwitchOrStructInitContext` **(Many-Argument Workhorses)** (Impact: 122.7)
    * *Intent:* /// Looks for an identifier that can be passed to `collectContainerNodes()` /// Returns the token in...
  * `completeFileSystemStringLiteral` **(Defensive Guards)** (Impact: 119.8)
    * *Intent:* /// Asserts that `pos_context` is one of the following: /// - `.import_string_literal` /// - `.cincl...
  * `declToCompletion` **(Defensive Guards)** (Impact: 103.1)
  * `collectContainerFields` **(Many-Argument Workhorses)** (Impact: 94.4)
    * *Intent:* /// Given a Type that is a container, adds it's `.container_field*`s to completions
  * `getEnumLiteralContext` **(Many-Argument Workhorses)** (Impact: 47.4)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 67 instances
* *State Mutation (weighted view):* 213
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 419`, `structural_boundaries: 263`, `args: 40`, `func_start: 40`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 79`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 2`
* *Architecture:* `api: 8`, `import: 13`
* *Defense:* `safety: 309`, `doc: 22`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.685
  * `Choke Point (Betweenness):` 0.006261 | `Ripple Effect (Closeness):` 0.140523
  * `Imports (Out-Degree: 10):` DocumentScope.zig, DocumentStore.zig, Server.zig, Uri.zig, completions.zig, analysis.zig, ast.zig, offsets.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/Server.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.664)
- **Top Global Matches:** file_cluster_4: 6.664, file_cluster_15: 9.513, file_cluster_12: 10.063
- **Magnitude:** 1076.2 | **LOC:** 2030 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 80.8%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **28**; blast radius 7.446; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.8%), Mutation Surface (formerly State Flux) (65.5%), Connectivity (formerly Api Exposure) (52.7%), Guard Balance (formerly Safety Score) (35.1%)
- **Documentation Coverage:** 82.9787% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `initializeHandler` **(Many-Argument Workhorses)** (Impact: 160.2)
  * `resolveConfiguration` **(Compute Cores)** (Impact: 65.8)
  * `refreshBuildOnSave` **(Defensive Guards)** (Impact: 34.2)
  * `handleResponse` **(Defensive Guards)** (Impact: 33.4)
  * `validateMessage` **(Defensive Guards)** (Impact: 26.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 35 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 39 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 31
* *State Mutation (weighted view):* 127
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 371`, `structural_boundaries: 294`, `args: 71`, `func_start: 71`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 49`, `planned_debt: 11`
* *Architecture:* `api: 17`, `concurrency: 1`, `import: 28`
* *Defense:* `safety: 330`, `doc: 56`, `cleanup: 47`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.446
  * `Choke Point (Betweenness):` 0.020403 | `Ripple Effect (Closeness):` 0.159259
  * `Imports (Out-Degree: 24):` Config.zig, DiagnosticsCollection.zig, DocumentStore.zig, Uri.zig, analyser.zig, analysis.zig, build_options, shared.zig...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/build_runner/build_runner.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.1)
- **Top Global Matches:** file_cluster_4: 7.1, file_cluster_6: 10.101, file_cluster_12: 12.134
- **Magnitude:** 998.06 | **LOC:** 1503 | **CtrlFlow:** 28.9% | **Authorship Centralization:** 73.1%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (80.8%), Guard Balance (formerly Safety Score) (40.3%), Complexity Load (formerly Cognitive Load) (38.2%)
- **Documentation Coverage:** 84.6154% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `main` **(Defensive Guards)** (Impact: 269.3)
  * `extractBuildInformation` **(Many-Argument Workhorses)** (Impact: 115.4)
  * `runPkgConfig` **(Defensive Guards)** (Impact: 70.5)
    * *Intent:* /// Run pkg-config for the given library name and parse the output, returning the arguments /// that...
  * `makeStep` **(Many-Argument Workhorses)** (Impact: 44.6)
    * *Intent:* /// Runs the "make" function of the single step `s`, updates its state, and then spawns newly-ready ...
  * `processModule` **(Many-Argument Workhorses)** (Impact: 28.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 63 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 195
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 350`, `structural_boundaries: 162`, `args: 31`, `func_start: 31`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 23`, `high_risk_execution: 9`, `state_mutation: 69`, `dead_code: 6`, `unreferenced_by_name: 1`
* *Architecture:* `api: 4`, `concurrency: 5`, `import: 5`
* *Defense:* `safety: 252`, `doc: 49`, `sync_locks: 5`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` @build, @dependencies, builtin, shared.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/ast.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.015)
- **Top Global Matches:** file_cluster_4: 7.015, file_cluster_12: 10.761, file_cluster_6: 11.131
- **Magnitude:** 930.62 | **LOC:** 1847 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 77.8%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **2**; blast radius 169.897; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (98.4%), Connectivity (formerly Api Exposure) (83.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (53.6%)
- **Documentation Coverage:** 84.9057% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `lastToken` **(Many-Argument Workhorses)** (Impact: 126.2)
    * *Intent:* /// Similar to `std.zig.Ast.lastToken` but also handles ASTs with syntax errors.
  * `indexOfBreakTarget` **(Defensive Guards)** (Impact: 45.8)
  * `fullPtrTypeComponents` **(Compute Cores)** (Impact: 37.1)
  * `next` **(Defensive Guards)** (Impact: 32.1)
  * `next` **(Compute Cores)** (Impact: 28.7)
    * *Intent:* /// Iterates over FnProto Params w/ added bounds check to support incomplete ast nodes
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 83 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 226`, `structural_boundaries: 219`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 99`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `api: 52`, `concurrency: 4`, `import: 2`
* *Defense:* `safety: 120`, `doc: 34`, `test: 9`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 169.897
  * `Choke Point (Betweenness):` 3e-05 | `Ripple Effect (Closeness):` 0.232903
  * `Imports (Out-Degree: 1):` offsets.zig, std
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/DocumentStore.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.196)
- **Top Global Matches:** file_cluster_4: 8.196, file_cluster_12: 8.664, file_cluster_15: 10.752
- **Magnitude:** 881.78 | **LOC:** 2059 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 90.2%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **14**; blast radius 15.844; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (91.7%), Connectivity (formerly Api Exposure) (78.0%), Mutation Surface (formerly State Flux) (50.5%), Guard Balance (formerly Safety Score) (36.3%)
- **Documentation Coverage:** 56.1798% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `uriFromImportStr` **(Defensive Guards)** (Impact: 53.2)
    * *Intent:* /// takes the string inside a @import() node (without the quotation marks) /// and returns it's uri ...
  * `resolveCImport` **(Defensive Guards)** (Impact: 47.3)
    * *Intent:* /// returns the document behind `@cImport()` where `node` is the `cImport` node /// if a cImport can...
  * `createAndStoreDocument` **(Many-Argument Workhorses)** (Impact: 38.9)
    * *Intent:* /// **Thread safe** takes an exclusive lock
  * `invalidateBuildFileWorker` **(Many-Argument Workhorses)** (Impact: 30.7)
  * `loadTrigramStores` **(Defensive Guards)** (Impact: 30.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 52 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 24 instances
* *Concurrency (weighted view):* 19
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 97
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 274`, `structural_boundaries: 372`, `args: 59`, `func_start: 59`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 49`, `planned_debt: 12`
* *Architecture:* `api: 45`, `concurrency: 14`, `import: 16`
* *Defense:* `safety: 323`, `doc: 101`, `sync_locks: 33`, `cleanup: 100`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.844
  * `Choke Point (Betweenness):` 0.014059 | `Ripple Effect (Closeness):` 0.196347
  * `Imports (Out-Degree: 11):` BuildAssociatedConfig.zig, DiagnosticsCollection.zig, DocumentScope.zig, TrigramStore.zig, Uri.zig, analysis.zig, shared.zig, builtin...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/features/code_actions.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.288)
- **Top Global Matches:** file_cluster_4: 6.288, file_cluster_12: 10.835, file_cluster_9: 10.911
- **Magnitude:** 584.0 | **LOC:** 1230 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **8**; blast radius 5.276; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (60.4%), Mutation Surface (formerly State Flux) (48.5%), Guard Balance (formerly Safety Score) (39.3%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (37.1%)
- **Documentation Coverage:** 80.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handleUnusedCapture` **(Many-Argument Workhorses)** (Impact: 40.8)
  * `getImportsDecls` **(Many-Argument Workhorses)** (Impact: 38.1)
  * `getDiscardLoc` **(Defensive Guards)** (Impact: 29.7)
    * *Intent:* /// takes the location of an identifier which is part of a discard `_ = location_here;` /// and retu...
  * `collectAutoDiscardDiagnostics` **(Many-Argument Workhorses)** (Impact: 25.1)
  * `createDiscardText` **(Many-Argument Workhorses)** (Impact: 24.6)
    * *Intent:* /// returns a discard string `_ = identifier_name; // autofix` with appropriate newlines and /// ind...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 55
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 208`, `structural_boundaries: 209`, `args: 38`, `func_start: 38`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 19`, `dead_code: 3`, `planned_debt: 2`
* *Architecture:* `api: 28`, `import: 10`
* *Defense:* `safety: 143`, `doc: 21`, `test: 9`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.276
  * `Choke Point (Betweenness):` 0.000135 | `Ripple Effect (Closeness):` 0.149306
  * `Imports (Out-Degree: 6):` DocumentScope.zig, DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, tracy
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/features/semantic_tokens.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.718)
- **Top Global Matches:** file_cluster_6: 7.718, file_cluster_4: 9.077, file_cluster_9: 15.453
- **Magnitude:** 494.12 | **LOC:** 1200 | **CtrlFlow:** 16.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **6**; blast radius 4.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (55.2%), Connectivity (formerly Api Exposure) (27.7%), Mutation Surface (formerly State Flux) (26.5%), Guard Balance (formerly Safety Score) (26.2%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeNodeTokens` **(Many-Argument Workhorses)** (Impact: 193.1)
  * `colorIdentifierBasedOnType` **(Many-Argument Workhorses)** (Impact: 63.4)
  * `handleComments` **(Many-Argument Workhorses)** (Impact: 26.2)
    * *Intent:* /// Highlight normal comments and doc comments.
  * `writeIdentifier` **(Defensive Guards)** (Impact: 23.2)
  * `writeFieldAccess` **(Defensive Guards)** (Impact: 22.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 11 instances
* *State Mutation (weighted view):* 37
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 55`, `args: 15`, `func_start: 15`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 15`, `state_mutation: 15`, `planned_debt: 1`
* *Architecture:* `api: 4`, `concurrency: 2`, `import: 6`
* *Defense:* `safety: 323`, `doc: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.766
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.137821
  * `Imports (Out-Degree: 4):` DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/DocumentScope.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.97)
- **Top Global Matches:** file_cluster_12: 6.97, file_cluster_7: 8.776, file_cluster_5: 9.797
- **Magnitude:** 435.0 | **LOC:** 1346 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 15.614; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.1%), Guard Balance (formerly Safety Score) (42.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (22.7%), Mutation Surface (formerly State Flux) (19.1%)
- **Documentation Coverage:** 83.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `walkWhileNode` **(Defensive Guards)** (Impact: 41.8)
    * *Intent:* /// label_token: inline_token while (cond_expr) |payload_token| : (cont_expr) then_expr else |error_...
  * `walkSwitchNode` **(Defensive Guards)** (Impact: 20.8)
  * `walkForNode` **(Defensive Guards)** (Impact: 20.6)
    * *Intent:* /// label_token: inline_token for (inputs) |capture_tokens| then_expr else else_expr
  * `pushDeclaration` **(Many-Argument Workhorses)** (Impact: 20.4)
  * `walkContainerDecl` **(Defensive Guards)** (Impact: 19.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 8 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 109`, `structural_boundaries: 81`, `args: 45`, `func_start: 45`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 11`, `duplicate_logic: 4`
* *Architecture:* `api: 41`, `concurrency: 2`, `import: 5`
* *Defense:* `safety: 165`, `doc: 38`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.614
  * `Choke Point (Betweenness):` 0.000529 | `Ripple Effect (Closeness):` 0.190267
  * `Imports (Out-Degree: 3):` ast.zig, builtin, offsets.zig, std, tracy
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/configuration.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.213)
- **Top Global Matches:** file_cluster_8: 8.213, file_cluster_6: 10.083, file_cluster_4: 18.34
- **Magnitude:** 415.3 | **LOC:** 778 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 73.3%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **4**; blast radius 4.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (76.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.0%), Connectivity (formerly Api Exposure) (53.0%), Guard Balance (formerly Safety Score) (40.6%)
- **Documentation Coverage:** 60.6061% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resolveConfiguration` **(Defensive Guards)** (Impact: 109.7)
  * `validateConfiguration` **(Many-Argument Workhorses)** (Impact: 60.1)
  * `findZig` **(Defensive Guards)** (Impact: 35.0)
  * `getZigEnv` **(Many-Argument Workhorses)** (Impact: 32.8)
  * `eql` **(Compute Cores)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 25 instances
* *Amplified Cascading Flux:* 18 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 149`, `structural_boundaries: 134`, `args: 12`, `func_start: 12`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 24`, `planned_debt: 1`
* *Architecture:* `api: 17`, `import: 4`
* *Defense:* `safety: 106`, `doc: 19`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.766
  * `Choke Point (Betweenness):` 0.00109 | `Ripple Effect (Closeness):` 0.138961
  * `Imports (Out-Degree: 2):` Config.zig, check.zig, builtin, std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/features/references.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.474)
- **Top Global Matches:** file_cluster_6: 7.474, file_cluster_8: 10.771, file_cluster_4: 14.95
- **Magnitude:** 395.64 | **LOC:** 794 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 6.074; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (66.4%), Guard Balance (formerly Safety Score) (31.6%), Connectivity (formerly Api Exposure) (30.8%), Mutation Surface (formerly State Flux) (18.2%)
- **Documentation Coverage:** 87.5% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `controlFlowReferences` **(Many-Argument Workhorses)** (Impact: 88.0)
  * `referenceNode` **(Many-Argument Workhorses)** (Impact: 83.2)
  * `referencesHandler` **(Defensive Guards)** (Impact: 47.5)
  * `gatherWorkspaceReferenceCandidates` **(Defensive Guards)** (Impact: 32.3)
  * `symbolReferences` **(Many-Argument Workhorses)** (Impact: 30.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 5 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 140`, `structural_boundaries: 131`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 9`
* *Defense:* `safety: 148`, `doc: 10`, `cleanup: 9`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.074
  * `Choke Point (Betweenness):` 0.005126 | `Ripple Effect (Closeness):` 0.161049
  * `Imports (Out-Degree: 7):` DocumentStore.zig, Server.zig, Uri.zig, analysis.zig, ast.zig, offsets.zig, lsp, std...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/analyser/segmented_list.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.642)
- **Top Global Matches:** file_cluster_5: 8.642, file_cluster_12: 8.87, file_cluster_7: 9.911
- **Magnitude:** 343.32 | **LOC:** 444 | **CtrlFlow:** 13.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 8.209; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (66.3%), Connectivity (formerly Api Exposure) (61.5%)
- **Documentation Coverage:** 67.725% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SegmentedList` **(Many-Argument Workhorses)** (Impact: 82.4)
    * *Intent:* /// This is a stack data structure where pointers to indexes have the same lifetime as the data stru...
  * `BaseIterator` **(Compute Cores)** (Impact: 24.1)
  * `shrinkCapacity` **(Type Conversions)** (Impact: 11.6)
    * *Intent:* /// Only shrinks capacity or retains current capacity. /// It may fail to reduce the capacity in whi...
  * `writeToSlice` **(Many-Argument Workhorses)** (Impact: 11.2)
  * `growCapacity` **(Defensive Guards)** (Impact: 11.1)
    * *Intent:* /// Only grows capacity, or retains current capacity.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 81
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 38`, `structural_boundaries: 50`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 35`, `planned_debt: 3`
* *Architecture:* `api: 26`, `import: 1`
* *Defense:* `safety: 11`, `doc: 25`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.209
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.105055
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `tests/lsp_features/completion.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.579)
- **Top Global Matches:** file_cluster_4: 8.579, file_cluster_6: 10.148, file_cluster_12: 12.805
- **Magnitude:** 330.84 | **LOC:** 5074 | **CtrlFlow:** 3.2% | **Authorship Centralization:** 56.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (69.6%), Connectivity (formerly Api Exposure) (53.5%), Guard Balance (formerly Safety Score) (41.5%), Concurrency Surface (formerly Concurrency) (14.8%)
- **Documentation Coverage:** 91.6667% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testCompletionWithOptions` **(Many-Argument Workhorses)** (Impact: 103.5)
  * `extractCompletionLabels` **(Defensive Guards)** (Impact: 12.3)
  * `searchCompletionItemWithLabel` **(Defensive Guards)** (Impact: 7.9)
  * `testCompletionTextEdit` **(Defensive Guards)** (Impact: 6.6)
    * *Intent:* /// TODO this function should allow asserting where the cursor is placed after the text edit
  * `printLabels` **(Defensive Guards)** (Impact: 6.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Memory Alloc (weighted view):* 1
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 165`, `args: 292`, `func_start: 9`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 117`, `state_mutation: 15`, `planned_debt: 15`, `fragile_debt: 1`
* *Architecture:* `api: 54`, `concurrency: 15`, `import: 37`
* *Defense:* `safety: 507`, `doc: 9`, `test: 172`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.064
  * `Choke Point (Betweenness):` 0.000143 | `Ripple Effect (Closeness):` 0.007752
  * `Imports (Out-Degree: 3):` ErrorBuilder.zig, context.zig, builtin, std, zls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/offsets.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.815)
- **Top Global Matches:** file_cluster_15: 6.815, file_cluster_12: 7.315, file_cluster_16: 8.769
- **Magnitude:** 326.14 | **LOC:** 806 | **CtrlFlow:** 9.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **22** in-repo importer(s); it depends on **3**; blast radius 172.778; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (39.6%), Guard Balance (formerly Safety Score) (27.6%)
- **Documentation Coverage:** 71.9512% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `sourceIndexToTokenIndex` **(Many-Argument Workhorses)** (Impact: 28.8)
  * `identifierIndexToLoc` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* /// The source index must be at the start of the valid identifier. /// /// Supported formats: /// - ...
  * `tokenToLoc` **(Defensive Guards)** (Impact: 15.8)
  * `multilineLocAtIndex` **(Compute Cores)** (Impact: 15.3)
    * *Intent:* /// return the source location /// that starts `n` lines before the line at which `index` is located...
  * `pickTokenTag` **(Defensive Guards)** (Impact: 12.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 10 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 104`, `args: 42`, `func_start: 42`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 11`
* *Architecture:* `api: 70`, `import: 3`
* *Defense:* `safety: 141`, `doc: 42`, `test: 68`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 172.778
  * `Choke Point (Betweenness):` 0.000186 | `Ripple Effect (Closeness):` 0.246603
  * `Imports (Out-Degree: 1):` ast.zig, lsp, std
  * `Imported By (In-Degree: 22):` (Excluded from Brief to save tokens)

### `src/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.719)
- **Top Global Matches:** file_cluster_8: 9.719, file_cluster_6: 11.257, file_cluster_4: 19.007
- **Magnitude:** 317.82 | **LOC:** 605 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 93.3%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.933; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (68.0%), Guard Balance (formerly Safety Score) (34.5%), Complexity Load (formerly Cognitive Load) (11.2%)
- **Documentation Coverage:** 73.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseArgs` **(Many-Argument Workhorses)** (Impact: 59.5)
  * `main` **(Defensive Guards)** (Impact: 42.6)
  * `logFn` **(Defensive Guards)** (Impact: 41.6)
  * `@"zls env"` **(Defensive Guards)** (Impact: 30.9)
  * `loadConfiguration` **(Many-Argument Workhorses)** (Impact: 22.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 39 instances
* *Amplified Cascading Flux:* 13 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 112`, `structural_boundaries: 113`, `args: 12`, `func_start: 12`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 8`, `state_mutation: 16`, `planned_debt: 1`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 121`, `doc: 21`, `sync_locks: 2`, `cleanup: 38`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.933
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` builtin, exe_options, known-folders, std, tracy, zls
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/TrigramStore.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.29)
- **Top Global Matches:** file_cluster_12: 8.29, file_cluster_4: 9.642, file_cluster_7: 10.094
- **Magnitude:** 297.34 | **LOC:** 695 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **4**; blast radius 6.18; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (87.5%), Connectivity (formerly Api Exposure) (61.2%), Guard Balance (formerly Safety Score) (47.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (14.2%)
- **Documentation Coverage:** 89.1892% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Defensive Guards)** (Impact: 46.1)
  * `appendDeclaration` **(Many-Argument Workhorses)** (Impact: 26.5)
  * `declarationsForQuery` **(Many-Argument Workhorses)** (Impact: 20.1)
    * *Intent:* /// Asserts `query.len >= 1`. Asserts declaration_buffer.items.len == 0.
  * `isVarDeclAlias` **(Defensive Guards)** (Impact: 15.0)
    * *Intent:* /// Check if the init expression is a sequence of field accesses /// where the last field name match...
  * `mergeIntersection` **(Many-Argument Workhorses)** (Impact: 13.5)
    * *Intent:* /// Asserts `@min(a.len, b.len) <= out.len`.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 19 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 85`, `args: 23`, `func_start: 23`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 22`
* *Architecture:* `api: 22`, `import: 4`
* *Defense:* `safety: 76`, `doc: 17`, `test: 4`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.18
  * `Choke Point (Betweenness):` 0.002211 | `Ripple Effect (Closeness):` 0.166753
  * `Imports (Out-Degree: 3):` ast.zig, offsets.zig, std, testing.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `tests/utility/position_context.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 4.325)
- **Top Global Matches:** file_cluster_2: 4.325, file_cluster_17: 5.515, file_cluster_13: 6.117
- **Magnitude:** 289.88 | **LOC:** 768 | **CtrlFlow:** 0.1% | **Authorship Centralization:** 75.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 3.064; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (53.9%), Guard Balance (formerly Safety Score) (22.5%), Complexity Load (formerly Cognitive Load) (2.3%), Historical Stability (predictive layer, promotion pending #2987) (formerly Stability) (0.1%)
- **Documentation Coverage:** 0.0% of unit weight undocumented
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 91`, `args: 30`, `func_start: 1`, `class_start: 1`
* *Risk/State:* `high_risk_execution: 7`, `state_mutation: 5`, `planned_debt: 2`
* *Architecture:* `import: 9`
* *Defense:* `safety: 200`, `doc: 6`, `test: 35`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.064
  * `Choke Point (Betweenness):` 0.000138 | `Ripple Effect (Closeness):` 0.007752
  * `Imports (Out-Degree: 3):` ErrorBuilder.zig, helper.zig, std, zls
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/features/diagnostics.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 10.962)
- **Top Global Matches:** file_cluster_4: 10.962, file_cluster_6: 10.966, file_cluster_12: 14.504
- **Magnitude:** 281.76 | **LOC:** 750 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 92.3%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **13**; blast radius 5.991; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (64.7%), Connectivity (formerly Api Exposure) (42.4%), Guard Balance (formerly Safety Score) (38.7%), Mutation Surface (formerly State Flux) (19.2%)
- **Documentation Coverage:** 90.9091% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `loop` **(Many-Argument Workhorses)** (Impact: 54.0)
  * `getErrorBundleFromStderr` **(Many-Argument Workhorses)** (Impact: 43.9)
  * `collectWarnStyleDiagnostics` **(Many-Argument Workhorses)** (Impact: 37.5)
  * `generateDiagnostics` **(Defensive Guards)** (Impact: 17.5)
  * `getAstCheckDiagnostics` **(Defensive Guards)** (Impact: 16.4)
    * *Intent:* /// caller owns the returned ErrorBundle
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 11 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *Concurrency (weighted view):* 6
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 15
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 82`, `structural_boundaries: 130`, `args: 16`, `func_start: 16`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 32`, `state_mutation: 9`, `planned_debt: 13`
* *Architecture:* `api: 8`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 129`, `doc: 3`, `sync_locks: 3`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.991
  * `Choke Point (Betweenness):` 0.006711 | `Ripple Effect (Closeness):` 0.162879
  * `Imports (Out-Degree: 10):` DiagnosticsCollection.zig, DocumentStore.zig, Server.zig, Uri.zig, analysis.zig, ast.zig, shared.zig, offsets.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/features/hover.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_9` (Centroid distance: 5.693)
- **Top Global Matches:** file_cluster_9: 5.693, file_cluster_15: 9.461, file_cluster_16: 9.499
- **Magnitude:** 258.74 | **LOC:** 537 | **CtrlFlow:** 14.7% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **8**; blast radius 4.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (47.9%), Guard Balance (formerly Safety Score) (31.2%), Mutation Surface (formerly State Flux) (15.1%), Connectivity (formerly Api Exposure) (13.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `hoverSymbolResolved` **(Many-Argument Workhorses)** (Impact: 44.8)
  * `hoverNumberLiteral` **(Many-Argument Workhorses)** (Impact: 27.1)
  * `hoverDefinitionBuiltin` **(Many-Argument Workhorses)** (Impact: 26.6)
  * `hoverDefinitionFieldAccess` **(Many-Argument Workhorses)** (Impact: 24.6)
  * `hoverSymbol` **(Many-Argument Workhorses)** (Impact: 21.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 8
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 69`, `args: 12`, `func_start: 12`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 4`
* *Architecture:* `api: 1`, `import: 9`
* *Defense:* `safety: 105`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.766
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.137821
  * `Imports (Out-Degree: 5):` DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, tracy, version_data
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/tracy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.377)
- **Top Global Matches:** file_cluster_12: 6.377, file_cluster_7: 8.684, file_cluster_5: 8.834
- **Magnitude:** 245.54 | **LOC:** 344 | **CtrlFlow:** 18.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **17** in-repo importer(s); it depends on **3**; blast radius 23.253; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (91.9%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (50.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (21.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `TracyAllocator` **(Type Conversions)** (Impact: 20.9)
  * `resizeFn` **(Type Conversions)** (Impact: 10.4)
  * `remapFn` **(Defensive Guards)** (Impact: 10.4)
  * `allocFn` **(Defensive Guards)** (Impact: 9.6)
  * `allocNamed` **(Compute Cores)** (Impact: 8.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Memory Alloc (weighted view):* 2
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 49`, `structural_boundaries: 30`, `args: 57`, `func_start: 57`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`
* *Architecture:* `api: 29`, `import: 3`
* *Defense:* `safety: 10`, `doc: 1`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 23.253
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.178432
  * `Imports (Out-Degree: 0):` builtin, options, std
  * `Imported By (In-Degree: 17):` (Excluded from Brief to save tokens)

### `src/features/inlay_hints.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.121)
- **Top Global Matches:** file_cluster_6: 6.121, file_cluster_4: 9.342, file_cluster_8: 16.225
- **Magnitude:** 241.44 | **LOC:** 576 | **CtrlFlow:** 16.9% | **Authorship Centralization:** 77.8%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 4.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (49.0%), Mutation Surface (formerly State Flux) (43.6%), Guard Balance (formerly Safety Score) (37.6%), Connectivity (formerly Api Exposure) (26.6%)
- **Documentation Coverage:** 60.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeNodeInlayHint` **(Defensive Guards)** (Impact: 68.7)
  * `writeCallHint` **(Defensive Guards)** (Impact: 30.5)
    * *Intent:* /// writes parameter hints into `builder.hints`
  * `appendParameterHint` **(Many-Argument Workhorses)** (Impact: 27.2)
  * `writeBuiltinHint` **(Defensive Guards)** (Impact: 19.9)
    * *Intent:* /// takes parameter nodes from the ast and function parameter names from `Builtin.parameters` and wr...
  * `getInlayHints` **(Defensive Guards)** (Impact: 10.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 79`, `structural_boundaries: 58`, `args: 13`, `func_start: 13`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 9`
* *Architecture:* `api: 3`, `import: 9`
* *Defense:* `safety: 79`, `doc: 11`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.766
  * `Choke Point (Betweenness):` 9.9e-05 | `Ripple Effect (Closeness):` 0.137821
  * `Imports (Out-Degree: 6):` Config.zig, DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, tracy...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/DiagnosticsCollection.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.364)
- **Top Global Matches:** file_cluster_4: 7.364, file_cluster_12: 11.085, file_cluster_6: 11.335
- **Magnitude:** 238.34 | **LOC:** 648 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **6**; blast radius 6.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (51.9%), Connectivity (formerly Api Exposure) (44.9%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (43.9%), Guard Balance (formerly Safety Score) (32.4%)
- **Documentation Coverage:** 88.8889% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `convertErrorBundleToLSPDiangostics` **(Many-Argument Workhorses)** (Impact: 54.5)
  * `pushErrorBundle` **(Many-Argument Workhorses)** (Impact: 38.0)
  * `pushSingleDocumentDiagnostics` **(Many-Argument Workhorses)** (Impact: 18.3)
  * `collectUrisFromErrorBundle` **(Defensive Guards)** (Impact: 14.4)
  * `publishDiagnostics` **(Defensive Guards)** (Impact: 9.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 14 instances
* *Amplified Cascading Flux:* 10 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 32
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 81`, `args: 12`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 12`, `planned_debt: 3`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `safety: 113`, `doc: 21`, `test: 20`, `sync_locks: 7`, `cleanup: 41`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.5
  * `Choke Point (Betweenness):` 9.5e-05 | `Ripple Effect (Closeness):` 0.168626
  * `Imports (Out-Degree: 3):` Uri.zig, builtin, lsp, offsets.zig, std, tracy
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/Uri.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.813)
- **Top Global Matches:** file_cluster_12: 7.813, file_cluster_4: 8.286, file_cluster_15: 8.944
- **Magnitude:** 232.3 | **LOC:** 579 | **CtrlFlow:** 12.1% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **2**; blast radius 13.301; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (86.1%), Connectivity (formerly Api Exposure) (63.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.8%), Guard Balance (formerly Safety Score) (30.7%)
- **Documentation Coverage:** 51.3514% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseWithOs` **(Many-Argument Workhorses)** (Impact: 37.8)
  * `fromPathWithOs` **(Defensive Guards)** (Impact: 22.4)
  * `resolveImport` **(Defensive Guards)** (Impact: 20.0)
  * `toFsPathWithOs` **(Defensive Guards)** (Impact: 16.1)
  * `normalizePercentEncoded` **(Many-Argument Workhorses)** (Impact: 15.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 9 instances
* *Amplified Cascading Flux:* 15 instances
* *Memory Alloc (weighted view):* 5
* *State Mutation (weighted view):* 47
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 54`, `structural_boundaries: 95`, `args: 25`, `func_start: 25`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 17`
* *Architecture:* `api: 14`, `import: 4`
* *Defense:* `safety: 114`, `doc: 44`, `test: 21`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 13.301
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.193798
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/features/signature_help.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.478)
- **Top Global Matches:** file_cluster_8: 5.478, file_cluster_6: 17.021, file_cluster_3: 19.363
- **Magnitude:** 217.2 | **LOC:** 323 | **CtrlFlow:** 20.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 4.766; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (95.6%), Guard Balance (formerly Safety Score) (43.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (27.9%), Complexity Load (formerly Cognitive Load) (24.5%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getSignatureInfo` **(Many-Argument Workhorses)** (Impact: 137.5)
  * `fnProtoToSignatureInfo` **(Many-Argument Workhorses)** (Impact: 29.2)
  * `from` **(Compute Cores)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 13 instances
* *State Mutation (weighted view):* 39
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 59`, `structural_boundaries: 36`, `args: 5`, `func_start: 3`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 13`
* *Architecture:* `api: 1`, `import: 7`
* *Defense:* `safety: 40`, `doc: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.766
  * `Choke Point (Betweenness):` 5e-06 | `Ripple Effect (Closeness):` 0.137821
  * `Imports (Out-Degree: 4):` DocumentStore.zig, analysis.zig, ast.zig, offsets.zig, lsp, std, version_data
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/testing.zig` (ZIG) | Magnitude: 130.62 | Delta: **0.121** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 210, branch: 30, structural_boundaries: 29, safety: 24

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/features/workspace_symbols.zig` (ZIG) | Magnitude: 24.56 | Delta: **0.092** (centroid distance) | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 63, core_var_decl: 23, design_snake_case: 18, structural_boundaries: 10
- `tests/lsp_features/code_actions.zig` (ZIG) | Magnitude: 53.48 | Delta: **0.096** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 873, core_var_decl: 270, design_snake_case: 198, safety: 121

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `tests/tests.zig` (ZIG) | Magnitude: 15.42 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: import: 19, indent_spaces: 19, core_var_decl: 19, design_short_vars: 19
- `src/zls.zig` (ZIG) | Magnitude: 47.76 | Delta: **0.256** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 35, core_var_decl: 33, api: 32, globals: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/BuildAssociatedConfig.zig` (ZIG) | Magnitude: 14.82 | Delta: **0.02** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 21, doc: 11, safety: 7, core_var_decl: 6
- `tests/lsp_features/selection_range.zig` (ZIG) | Magnitude: 9.28 | Delta: **0.129** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 52, core_var_decl: 19, design_snake_case: 17, safety: 13

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/features/diagnostics.zig` (ZIG) | Magnitude: 281.76 | Delta: **0.004** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 577, structural_boundaries: 130, safety: 129, core_var_decl: 110

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `tests/analysis/error_union.zig` (ZIG) | Magnitude: 13.64 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: globals: 7, core_var_decl: 7, design_pascal_case: 6, class_start: 2
- `tests/analysis/decl_literal.zig` (ZIG) | Magnitude: 2.82 | Delta: **0.011** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 16, core_var_decl: 14, design_pascal_case: 13, globals: 10

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/Server.zig` -> **Techatrix** (80.8% isolated ownership) | Magnitude: 1076.2
- `src/DocumentStore.zig` -> **Techatrix** (90.2% isolated ownership) | Magnitude: 881.78
- `src/features/code_actions.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 584.0
- `src/features/references.zig` -> **Techatrix** (85.7% isolated ownership) | Magnitude: 395.64
- `src/offsets.zig` -> **Techatrix** (100.0% isolated ownership) | Magnitude: 326.14

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/Server.zig` -> **Severity: 1.337** (Bridge: 0.0204 * Flux: 65.5186%)
- `src/analysis.zig` -> **Severity: 0.797** (Bridge: 0.0122 * Flux: 65.3976%)
- `src/DocumentStore.zig` -> **Severity: 0.71** (Bridge: 0.0141 * Flux: 50.4738%)
- `src/features/completions.zig` -> **Severity: 0.594** (Bridge: 0.0063 * Flux: 94.8423%)
- `src/TrigramStore.zig` -> **Severity: 0.194** (Bridge: 0.0022 * Flux: 87.5209%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/ast.zig` -> **Severity: 12.491** (Embedded: 0.2329 * Error Risk: 53.6338%)
- `src/tracy.zig` -> **Severity: 9.04** (Embedded: 0.1784 * Error Risk: 50.662%)
- `src/DocumentScope.zig` -> **Severity: 8.072** (Embedded: 0.1903 * Error Risk: 42.424%)
- `src/TrigramStore.zig` -> **Severity: 7.895** (Embedded: 0.1668 * Error Risk: 47.3452%)
- `src/testing.zig` -> **Severity: 7.703** (Embedded: 0.1505 * Error Risk: 51.1864%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/ast.zig` -> **Severity: 14425.224** (Blast Radius: 169.897 * Doc Risk: 84.9057%)
- `src/offsets.zig` -> **Severity: 12431.584** (Blast Radius: 172.778 * Doc Risk: 71.9512%)
- `src/tracy.zig` -> **Severity: 2325.3** (Blast Radius: 23.253 * Doc Risk: 100.0%)
- `tests/context.zig` -> **Severity: 1682.6** (Blast Radius: 16.826 * Doc Risk: 100.0%)
- `src/testing.zig` -> **Severity: 1537.83** (Blast Radius: 17.087 * Doc Risk: 90.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 62 literal sites + 10 sites through wrappers = 72
- **`panics_and_aborts`:** 228 literal sites + 4 sites through wrappers = 232

- `fatalWithHint` (function, debug_prints, primitive): 10 call sites in 1 files -- `src/build_runner/build_runner.zig`
- `formatRawAssumeCapacity` (function, panics_and_aborts, primitive): 4 call sites in 1 files -- `src/Uri.zig`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 6902 call pairs -- scoped 28.3%, unique 0.0%, ambiguous 14.4%, external 57.2%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 6902 | 28.3% | 0.0% | 14.4% | 57.2% |

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
