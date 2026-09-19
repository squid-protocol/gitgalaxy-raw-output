# ARCHITECTURAL_BRIEF: capy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/capy-ui/capy.git` |
| **Zero-Dependency Mode** | `ACTIVE (Degraded Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |

> **⚠️ ZERO-DEPENDENCY MODE ACTIVE:**
> Optional engines missing during this scan: `tiktoken`, `pandas`, `xgboost`. Metrics that need them were NOT computed -- shown as `n/a` or omitted, and no value shown for them is a measurement: Token Mass and Financial Read Cost (`tiktoken`); AI threat classification (`xgboost`/`pandas`/`numpy`). Every graph metric (PageRank / Blast Radius, the centralities, the repo network table, connection counts) is computed natively and matches full precision. Do not infer values for the missing metrics.

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 150 analyzed artifact(s), 20909 LOC.
- **Load-bearing artifact:** `src/capy.zig` -- 43 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/capy.zig` -- pulls in 34 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `android/src/android-bind.zig` at magnitude 1978.5 (structural weight, not risk).
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
| Total Artifacts | 517 |
| Analyzed Artifacts (Scanned) | 150 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 367 |
| Total LOC | 20909 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 29.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4525 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4094 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 23.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.5869 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 132 | 19715 | 88.0% |
| MARKDOWN | 4 | 0 | 2.7% |
| NIX | 3 | 180 | 2.0% |
| JAVA | 2 | 25 | 1.3% |
| C | 2 | 30 | 1.3% |
| GLSL | 2 | 8 | 1.3% |
| JAVASCRIPT | 2 | 925 | 1.3% |
| PLAINTEXT | 1 | 0 | 0.7% |
| HTML | 1 | 26 | 0.7% |
| XML | 1 | 0 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Small Flat Repo (2)`
> **Architectural Drift Z-Score:** `0.74`
> **Composition Archetype:** `Small Flat Repo (2)` (z +0.74; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 29%, State Mutators Files 18%, Large Core Modules (3) 16%, Type Conversions Files 13%, Data / Markup / Trivial 7%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 145 | 96.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 367*

**Composition by Extension & Reason:**
- `.zig`: 332x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 72269 LOC exceeds safe regex boundaries)
- `no_extension`: 10x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 2x Excluded (Unsupported Extension: '.lock')
- `.class`: 2x Excluded (Explicitly Denied Extension: '.class')
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zon`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.o`: 2x Excluded (Explicitly Denied Extension: '.o')
- `.dex`: 1x Excluded (Unsupported Extension: '.dex')
- `.stl`: 1x Excluded (Explicitly Denied Extension: '.stl')
- `.c`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 1x Unsupported Format (.rc)
- `.md`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.mod`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.9 | 10.2 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 95.8 | 43.7 | 45.7 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 18.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.3 | 2.5 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 44.6 | 53.9 | 100.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.8 | 11.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.1 | 3.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 57.6 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 81.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 3611 | 115 | 49 | `android/src/android-bind.zig` |
| cleanup | 279 | 71 | 5 | `src/data.zig` |
| guards | 1797 | 124 | 27 | `src/backends/android/backend.zig` |
| danger | 1426 | 99 | 18 | `src/backends/android/backend.zig` |
| concurrency | 250 | 24 | 2 | `src/backends/wasm/capy-worker.js` |
| connectivity | 3574 | 139 | 27 | `android/src/android-bind.zig` |
| io | 111 | 19 | 2 | `android/Sdk.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 56 | 11 | 0 | `src/backends/wasm/capy-worker.js` |
| time | 33 | 13 | 0 | `src/fuzz.zig` |
| serialization | 1 | 1 | 0 | `examples/osm-viewer.zig` |
| regex | 2 | 2 | 0 | `android/examples/egl/main.zig` |
| events | 87 | 37 | 1 | `src/backends/wasm/capy.js` |
| tests | 105 | 9 | 0 | `src/data.zig` |
| docs | 557 | 77 | 8 | `src/data.zig` |
| debt | 299 | 81 | 5 | `src/backends/win32/backend.zig` |
| mutation | 6897 | 143 | 74 | `android/src/android-bind.zig` |
| dead_code | 236 | 68 | 4 | `src/backends/wasm/capy-worker.js` |
| credential | 0 | 0 | 0 | - |
| threat | 168 | 29 | 3 | `src/internal.zig` |
| ml_ai | 606 | 51 | 11 | `src/backends/gtk/Canvas.zig` |
| ui | 670 | 73 | 16 | `examples/demo.zig` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.1166**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `android/Sdk.zig` (Hits: 26)
- `src/backends/win32/win32.zig` (Hits: 25)
- `src/assets.zig` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **capy.zig** (`src/capy.zig`) — 43 inbound connections
2. **data.zig** (`src/data.zig`) — 29 inbound connections
3. **internal.zig** (`src/internal.zig`) — 29 inbound connections
4. **shared.zig** (`src/backends/shared.zig`) — 13 inbound connections
5. **js.zig** (`src/backends/wasm/js.zig`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **capy.zig** (`src/capy.zig`) — 34 outbound dependencies
2. **backend.zig** (`src/backends/gtk/backend.zig`) — 22 outbound dependencies
3. **backend.zig** (`src/backends/wasm/backend.zig`) — 17 outbound dependencies
4. **android-support.zig** (`android/src/android-support.zig`) — 11 outbound dependencies
5. **c.zig** (`android/src/c.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Atom` **(Many-Argument Workhorses)** (@ `src/data.zig`) -> Impact: **118.7** | LOC: 592
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `process` **(Many-Argument Workhorses)** (@ `src/backends/win32/backend.zig`) -> Impact: **98.3** | LOC: 222
- `createApp` **(Many-Argument Workhorses)** (@ `android/Sdk.zig`) -> Impact: **86.3** | LOC: 286
  * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
- `Events` **(Type Conversions)** (@ `src/backends/win32/backend.zig`) -> Impact: **82.1** | LOC: 312
- `GridLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **81.2** | LOC: 238
  * *Intent:* /// Grid layout based on the CSS Grid algorithm
- `fromIid` **(Compute Cores)** (@ `android/src/opensl.zig`) -> Impact: **79.2** | LOC: 56
- `Widgeting` **(Defensive Guards)** (@ `src/internal.zig`) -> Impact: **65.1** | LOC: 313
  * *Intent:* /// Convenience function for creating widgets
- `add` **(Many-Argument Workhorses)** (@ `android/Sdk.zig`) -> Impact: **61.3** | LOC: 376
- `RowLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **54.3** | LOC: 81
  * *Intent:* /// Arranges items horizontally.
- `ColumnLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **53.9** | LOC: 74
  * *Intent:* /// Arranges items vertically.

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 25 | 2775.78 | 11.54% | 34.03% |
| `android/src` | 13 | 2699.42 | 8.35% | 16.39% |
| `src/backends/wasm` | 16 | 1629.02 | 19.43% | 23.52% |
| `src/backends/win32` | 5 | 1206.46 | 9.22% | 17.84% |
| `src/backends/gtk` | 19 | 885.62 | 10.77% | 16.45% |
| `examples` | 24 | 648.12 | 7.08% | 0.0% |
| `src/components` | 15 | 614.76 | 8.65% | 16.85% |
| `android` | 5 | 451.12 | 0.99% | 1.6% |
| `src/backends/android` | 1 | 358.24 | 17.08% | 28.42% |
| `android/examples/egl` | 1 | 314.18 | 19.3% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/backends/macos/CapyAppDelegate.zig` -> **100.0%** Exposure
- `src/c_api.zig` -> **100.0%** Exposure
- `src/http.zig` -> **100.0%** Exposure
- `src/backends/wasm/capy-worker.js` -> **100.0%** Exposure
- `src/flat/toggle_switch.zig` -> **99.9999%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/components/Image.zig` -> **100.0%** Exposure
- `src/components/Tabs.zig` -> **100.0%** Exposure
- `src/backends/wasm/capy-worker.js` -> **100.0%** Exposure
- `src/backends/wasm/capy.js` -> **100.0%** Exposure
- `build_capy.zig` -> **99.9443%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/backends/wasm/capy-worker.js` -> **54** Orphaned Functions | **0** Duplicates
- `src/backends/macos/CapyAppDelegate.zig` -> **0** Orphaned Functions | **14** Duplicates
- `src/c_api.zig` -> **12** Orphaned Functions | **0** Duplicates
- `examples/graph.zig` -> **7** Orphaned Functions | **0** Duplicates
- `android/examples/egl/main.zig` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `417` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `android/src/android-bind.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1978.5 | **LOC:** 2624 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); blast radius 4.513; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AHardwareBuffer_lockAndGetInfo` **(State Mutators)** (Impact: 2.9)
  * `ALooper_addFd` **(State Mutators)** (Impact: 2.7)
  * `__android_log_buf_print` **(State Mutators)** (Impact: 2.5)
  * `AInputQueue_attachLooper` **(State Mutators)** (Impact: 2.5)
  * `AHardwareBuffer_lock` **(State Mutators)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 3`, `args: 435`, `func_start: 182`, `class_start: 68`
* *Risk/State:* None
* *Architecture:* `api: 1607`, `import: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.513
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018519
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/win32/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 718.28 | **LOC:** 1773 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **10**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (71.7%), Mutation Surface (formerly State Flux) (24.0%)
- **Documentation Coverage:** 97.1014% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `process` **(Many-Argument Workhorses)** (Impact: 98.3)
  * `Events` **(Type Conversions)** (Impact: 82.1)
  * `setFullscreen` **(Many-Argument Workhorses)** (Impact: 14.2)
  * `runStep` **(Compute Cores)** (Impact: 11.3)
  * `init` **(I/O & Config Routines)** (Impact: 9.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 8 instances
* *Mitigated Memory Allocs:* 16 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 108`, `structural_boundaries: 148`, `args: 101`, `func_start: 99`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 110`, `high_risk_execution: 8`, `state_mutation: 36`, `dead_code: 3`, `planned_debt: 27`
* *Architecture:* `io: 9`, `api: 142`, `import: 11`
* *Defense:* `safety: 72`, `doc: 15`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` capy.zig, trait.zig, shared.zig, Dropdown.zig, Monitor.zig, builtin, gdip.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/data.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 707.42 | **LOC:** 1349 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **5**; blast radius 116.309; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (89.3%), Guard Balance (formerly Safety Score) (35.2%), Complexity Load (formerly Cognitive Load) (21.3%)
- **Documentation Coverage:** 56.6845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Atom` **(Many-Argument Workhorses)** (Impact: 118.7)
    * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to //...
  * `lerp` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /// Linear interpolation between any two values a and b with factor t. /// Both values must be of th...
  * `ListAtom` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* /// A list of atoms, that is itself an atom.
  * `dependOn` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* // TODO: constrain "function"'s type based on tuple // TODO: optionally provide the function with an...
  * `animate` **(Type Conversions)** (Impact: 16.2)
    * *Intent:* /// Starts an animation on the atom, from the current value to the `target` value. The /// animation...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 33 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 116
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 99`, `structural_boundaries: 176`, `args: 89`, `func_start: 83`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 6`, `state_mutation: 50`, `dead_code: 3`, `planned_debt: 8`
* *Architecture:* `api: 76`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 123`, `doc: 77`, `test: 56`, `sync_locks: 48`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 116.309
  * `Choke Point (Betweenness):` 0.015647 | `Ripple Effect (Closeness):` 0.309917
  * `Imports (Out-Degree: 4):` AnimationController.zig, containers.zig, internal.zig, std, trait.zig
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `src/backends/wasm/capy.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 608.64 | **LOC:** 635 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 4.229; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Guard Balance (formerly Safety Score) (91.9%), Complexity Load (formerly Cognitive Load) (91.9%)
- **Documentation Coverage:** 97.8495% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `pushAnswer` **(Defensive Guards)** (Impact: 31.6)
  * `addChunk` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* /** **/
  * `fillImage` **(Many-Argument Workhorses)** (Impact: 14.7)
  * `update` **(I/O & Config Routines)** (Impact: 13.5)
    * *Intent:* // TODO: when we're in blocking mode, avoid updating so often
  * `onmessage` **(Defensive Guards)** (Impact: 12.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 14 instances
* *Amplified Cascading Flux:* 68 instances
* *Concurrency (weighted view):* 88
* *State Mutation (weighted view):* 236
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 77`, `structural_boundaries: 73`, `args: 72`, `func_start: 57`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 100`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 36`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 27`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.229
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.006667
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/internal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 491.76 | **LOC:** 799 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **10**; blast radius 91.671; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (35.3%), Dead Code Surface (formerly Dead Code) (33.3%), Mutation Surface (formerly State Flux) (32.0%)
- **Documentation Coverage:** 56.9149% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Widgeting` **(Defensive Guards)** (Impact: 65.1)
    * *Intent:* /// Convenience function for creating widgets
  * `Events` **(Defensive Guards)** (Impact: 40.1)
    * *Intent:* /// Convenience function for creating widgets
  * `iterateFields` **(Type Conversions)** (Impact: 24.1)
  * `iterateApplyFields` **(Defensive Guards)** (Impact: 16.9)
  * `errorHandler` **(Defensive Guards)** (Impact: 9.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 5 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *High Risk Execution (weighted view):* 1
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 65`, `args: 78`, `func_start: 69`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 6`, `state_mutation: 11`, `dead_code: 17`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 69`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 95`, `doc: 52`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 91.671
  * `Choke Point (Betweenness):` 0.023916 | `Ripple Effect (Closeness):` 0.309917
  * `Imports (Out-Degree: 6):` AnimationController.zig, backend.zig, shared.zig, builtin, containers.zig, data.zig, root, std...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

### `src/containers.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 473.5 | **LOC:** 924 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **7**; blast radius 43.219; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Connectivity (formerly Api Exposure) (72.3%), Guard Balance (formerly Safety Score) (33.0%), Debt Markers (formerly Tech Debt) (25.6%)
- **Documentation Coverage:** 44.9275% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `GridLayout` **(Many-Argument Workhorses)** (Impact: 81.2)
    * *Intent:* /// Grid layout based on the CSS Grid algorithm
  * `RowLayout` **(Many-Argument Workhorses)** (Impact: 54.3)
    * *Intent:* /// Arranges items horizontally.
  * `ColumnLayout` **(Many-Argument Workhorses)** (Impact: 53.9)
    * *Intent:* /// Arranges items vertically.
  * `getChild` **(Defensive Guards)** (Impact: 16.7)
    * *Intent:* /// Searches recursively for a component named `name` and returns the first one found. /// If no com...
  * `MarginLayout` **(Many-Argument Workhorses)** (Impact: 10.9)
    * *Intent:* /// Positions one item according to the given margins.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 7 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 28 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 88
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 95`, `args: 42`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 7`, `state_mutation: 32`, `dead_code: 9`, `planned_debt: 17`, `fragile_debt: 1`
* *Architecture:* `api: 37`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 98`, `doc: 33`, `test: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 43.219
  * `Choke Point (Betweenness):` 0.026412 | `Ripple Effect (Closeness):` 0.201613
  * `Imports (Out-Degree: 5):` AnimationController.zig, backend.zig, capy.zig, data.zig, internal.zig, std, widget.zig
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `android/Sdk.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 416.88 | **LOC:** 1550 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 4.229; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (62.9%), Guard Balance (formerly Safety Score) (44.8%), Mutation Surface (formerly State Flux) (18.0%), Debt Markers (formerly Tech Debt) (8.0%)
- **Documentation Coverage:** 43.9189% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createApp` **(Many-Argument Workhorses)** (Impact: 86.3)
    * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
  * `add` **(Many-Argument Workhorses)** (Impact: 61.3)
  * `validate` **(Many-Argument Workhorses)** (Impact: 27.6)
  * `init` **(Defensive Guards)** (Impact: 19.4)
    * *Intent:* /// Initializes the android SDK. /// It requires some input on which versions of the tool chains sho...
  * `configureModule` **(Many-Argument Workhorses)** (Impact: 8.8)
    * *Intent:* // Note that this function must be accompanied by `configureStep`
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 28
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 114`, `args: 38`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 52`, `high_risk_execution: 11`, `state_mutation: 18`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 26`, `api: 57`, `import: 4`
* *Defense:* `safety: 110`, `doc: 55`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 4.229
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006667
  * `Imports (Out-Degree: 0):` auto-detect.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/win32/win32.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 368.08 | **LOC:** 423 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **2**; blast radius 6.891; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (90.6%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (10.5%)
- **Documentation Coverage:** 96.6102% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setWindowLongPtr` **(Type Conversions)** (Impact: 6.3)
  * `getWindowLongPtr` **(Type Conversions)** (Impact: 5.5)
  * `TabCtrl_InsertItemA` **(Type Conversions)** (Impact: 4.3)
  * `TabCtrl_InsertItemW` **(Type Conversions)** (Impact: 4.3)
  * `TabCtrl_GetItemA` **(Type Conversions)** (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 11`, `args: 64`, `func_start: 59`, `class_start: 18`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 8`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 25`, `api: 221`, `import: 5`
* *Defense:* `safety: 2`, `doc: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 6.891
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 0):` std, zigwin32
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/backends/android/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 358.24 | **LOC:** 873 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (80.0%), Concurrency Surface (formerly Concurrency) (63.3%), Mutation Surface (formerly State Flux) (33.2%)
- **Documentation Coverage:** 98.5401% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Events` **(Defensive Guards)** (Impact: 13.6)
  * `runOnUiThread` **(Many-Argument Workhorses)** (Impact: 8.2)
  * `onClick` **(Defensive Guards)** (Impact: 7.3)
  * `onChangedText` **(Defensive Guards)** (Impact: 7.3)
  * `onDraw` **(Defensive Guards)** (Impact: 6.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 3
* *Concurrency (weighted view):* 27
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 29
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 153`, `args: 75`, `func_start: 75`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 121`, `high_risk_execution: 4`, `state_mutation: 21`, `dead_code: 6`, `planned_debt: 21`
* *Architecture:* `io: 3`, `api: 78`, `concurrency: 12`, `import: 6`
* *Defense:* `safety: 141`, `doc: 2`, `sync_locks: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capy.zig, trait.zig, shared.zig, android, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/capy-worker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 343.46 | **LOC:** 451 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.6%)
- **Documentation Coverage:** 91.1765% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clock_time_get` **(Type Conversions)** (Impact: 15.2)
  * `fd_write` **(Many-Argument Workhorses)** (Impact: 14.5)
  * `waitForAnswer` **(Compute Cores)** (Impact: 9.9)
    * *Intent:* /** **/
  * `path_open` **(Many-Argument Workhorses)** (Impact: 6.6)
  * `environ_get` **(Compute Cores)** (Impact: 6.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 9 instances
* *Amplified Cascading Flux:* 14 instances
* *Concurrency (weighted view):* 96
* *State Mutation (weighted view):* 54
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 76`, `args: 68`, `func_start: 66`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 26`, `dead_code: 1`, `planned_debt: 5`, `unreferenced_by_name: 54`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 51`, `import: 1`
* *Defense:* `safety: 2`, `doc: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/examples/egl/main.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 314.18 | **LOC:** 905 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.286; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (81.7%), Concurrency Surface (formerly Concurrency) (28.7%), Complexity Load (formerly Cognitive Load) (19.3%), Connectivity (formerly Api Exposure) (8.1%)
- **Documentation Coverage:** 84.2105% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mainLoop` **(Many-Argument Workhorses)** (Impact: 41.3)
  * `debugMessageCallback` **(Many-Argument Workhorses)** (Impact: 21.2)
  * `insertPoint` **(Defensive Guards)** (Impact: 17.0)
  * `processMotionEvent` **(Many-Argument Workhorses)** (Impact: 11.9)
  * `renderf32` **(Compute Cores)** (Impact: 9.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 19 instances
* *Concurrency (weighted view):* 31
* *State Mutation (weighted view):* 83
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 57`, `structural_boundaries: 73`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 45`, `dead_code: 3`, `unreferenced_by_name: 5`
* *Architecture:* `api: 15`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 27`, `doc: 11`, `sync_locks: 14`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` android, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gtk/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 215.74 | **LOC:** 320 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (93.7%), Guard Balance (formerly Safety Score) (80.0%), Mutation Surface (formerly State Flux) (39.8%), Complexity Load (formerly Cognitive Load) (18.0%)
- **Documentation Coverage:** 88.2353% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Events` **(Type Conversions)** (Impact: 53.4)
  * `gtkKeyPress` **(Type Conversions)** (Impact: 26.4)
  * `gtkButtonPress` **(Many-Argument Workhorses)** (Impact: 22.3)
  * `gtkMouseMotion` **(Type Conversions)** (Impact: 9.7)
  * `gtkMouseScroll` **(Defensive Guards)** (Impact: 7.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 34`, `structural_boundaries: 36`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 5`
* *Architecture:* `api: 25`, `import: 6`
* *Defense:* `safety: 21`, `doc: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capy.zig, trait.zig, shared.zig, backend.zig, gtk.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/src/android-support.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 189.68 | **LOC:** 384 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 15.74; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (84.3%), Connectivity (formerly Api Exposure) (57.0%), Guard Balance (formerly Safety Score) (52.5%), Complexity Load (formerly Cognitive Load) (28.4%)
- **Documentation Coverage:** 73.1707% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `makeNativeActivityGlue` **(Type Conversions)** (Impact: 20.8)
    * *Intent:* /// Returns a wrapper implementation for the given App type which implements all /// ANativeActivity...
  * `printSymbolInfoAt` **(Defensive Guards)** (Impact: 13.6)
  * `ANativeActivity_onCreate` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* /// Actual application entry point
  * `invoke` **(Type Conversions)** (Impact: 12.8)
  * `panic` **(Defensive Guards)** (Impact: 10.2)
    * *Intent:* // Android Panic implementation
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 9 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 31
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 30`, `structural_boundaries: 25`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 13`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 12`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 30`, `doc: 3`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 15.74
  * `Choke Point (Betweenness):` 0.00085 | `Ripple Effect (Closeness):` 0.026667
  * `Imports (Out-Degree: 6):` NativeActivity.zig, NativeInvocationHandler.zig, android-bind.zig, audio.zig, build_options, builtin, c.zig, egl.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `android/src/opensl.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 176.36 | **LOC:** 497 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (66.8%), Mutation Surface (formerly State Flux) (48.8%), Debt Markers (formerly Tech Debt) (45.0%), Complexity Load (formerly Cognitive Load) (21.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `fromIid` **(Compute Cores)** (Impact: 79.2)
  * `getOutputStream` **(Many-Argument Workhorses)** (Impact: 15.1)
  * `checkResult` **(Defensive Guards)** (Impact: 5.4)
  * `bufferQueueCallback` **(Type Conversions)** (Impact: 5.0)
  * `start` **(Type Conversions)** (Impact: 4.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 70`, `structural_boundaries: 86`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 10`, `planned_debt: 4`, `unreferenced_by_name: 4`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 39`, `sync_locks: 4`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` audio.zig, c.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/macos/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 170.02 | **LOC:** 381 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **9**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (55.0%), Mutation Surface (formerly State Flux) (42.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Events` **(Generic / Templated Code)** (Impact: 9.5)
  * `runStep` **(Compute Cores)** (Impact: 8.9)
  * `setChild` **(Defensive Guards)** (Impact: 5.5)
  * `setCallback` **(State Mutators)** (Impact: 4.8)
  * `getFlippedNSView` **(Defensive Guards)** (Impact: 4.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 4 instances
* *High Risk Execution (weighted view):* 1
* *State Mutation (weighted view):* 16
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 34`, `args: 37`, `func_start: 37`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 3`, `state_mutation: 8`, `planned_debt: 7`
* *Architecture:* `api: 49`, `concurrency: 3`, `import: 9`
* *Defense:* `safety: 9`, `doc: 1`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` capy.zig, trait.zig, shared.zig, AppKit.zig, CapyAppDelegate.zig, Monitor.zig, Button.zig, objc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/js.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 160.64 | **LOC:** 107 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); blast radius 17.539; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (16.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `jsSetAttribute` **(State Mutators)** (Impact: 2.5)
  * `jsSetStyle` **(State Mutators)** (Impact: 2.5)
  * `setColor` **(State Mutators)** (Impact: 2.5)
  * `rectPath` **(State Mutators)** (Impact: 2.5)
  * `fillText` **(State Mutators)** (Impact: 2.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 2`, `args: 53`, `func_start: 53`, `class_start: 1`
* *Risk/State:* `planned_debt: 1`
* *Architecture:* `api: 60`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 17.539
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.087111
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `examples/balls.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 145.94 | **LOC:** 233 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.286; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.1%), Complexity Load (formerly Cognitive Load) (64.9%), Concurrency Surface (formerly Concurrency) (16.5%), Connectivity (formerly Api Exposure) (5.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `simulationThread` **(I/O & Config Routines)** (Impact: 33.1)
  * `onMouseButton` **(Many-Argument Workhorses)** (Impact: 15.7)
  * `onDraw` **(Type Conversions)** (Impact: 13.4)
  * `main` **(Defensive Guards)** (Impact: 4.7)
  * `onMouseMotion` **(Defensive Guards)** (Impact: 4.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 18 instances
* *State Mutation (weighted view):* 67
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 32`, `structural_boundaries: 22`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 31`, `dead_code: 1`, `unreferenced_by_name: 1`
* *Architecture:* `api: 3`, `concurrency: 1`, `import: 2`
* *Defense:* `safety: 15`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` capy, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fuzz.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 130.32 | **LOC:** 218 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 5.879; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.6%), Connectivity (formerly Api Exposure) (59.7%), Dead Code Surface (formerly Dead Code) (36.7%), Guard Balance (formerly Safety Score) (35.3%)
- **Documentation Coverage:** 84.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `testFunction` **(Many-Argument Workhorses)** (Impact: 36.5)
  * `refine` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* /// Tries to find counter-examples (case where there is no error) in the /// given time and adjust t...
  * `Iterator` **(Type Conversions)** (Impact: 8.9)
  * `threwError` **(Defensive Guards)** (Impact: 7.8)
  * `format` **(Defensive Guards)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 14
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 25`, `args: 13`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 6`, `dead_code: 5`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 22`, `doc: 4`, `test: 5`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.879
  * `Choke Point (Betweenness):` 0.000406 | `Ripple Effect (Closeness):` 0.186023
  * `Imports (Out-Degree: 1):` std, trait.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/osm-viewer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 127.18 | **LOC:** 296 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 2.286; role: Isolated/Orphan
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (19.3%), Connectivity (formerly Api Exposure) (9.5%), Dead Code Surface (formerly Dead Code) (2.4%)
- **Documentation Coverage:** 89.6552% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `checkRequests` **(Defensive Guards)** (Impact: 16.5)
  * `mouseScroll` **(Type Conversions)** (Impact: 10.8)
  * `getTile` **(Defensive Guards)** (Impact: 7.9)
    * *Intent:* // Implementation Methods
  * `drawTile` **(Defensive Guards)** (Impact: 7.9)
  * `draw` **(Type Conversions)** (Impact: 5.9)
    * *Intent:* // Component Methods (drawing, showing, ...) // Here we'll draw ourselves the content of the map // ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 7 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 25
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 37`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 11`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 41`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` capy, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gtk/Canvas.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 125.88 | **LOC:** 240 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.3%), Guard Balance (formerly Safety Score) (83.7%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (69.7%)
- **Documentation Coverage:** 94.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `roundedRectangleEx` **(Type Conversions)** (Impact: 16.1)
    * *Intent:* // The radiuses are in order: top left, top right, bottom left, bottom right
  * `text` **(Type Conversions)** (Impact: 8.0)
  * `gtkCanvasDraw` **(Type Conversions)** (Impact: 7.8)
  * `getTextSize` **(Type Conversions)** (Impact: 5.6)
  * `ellipse` **(Type Conversions)** (Impact: 5.5)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 22
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 14`, `args: 18`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 8`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` capy.zig, shared.zig, Window.zig, common.zig, gtk.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build_capy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 124.62 | **LOC:** 301 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **3**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Debt Markers (formerly Tech Debt) (89.4%), Guard Balance (formerly Safety Score) (61.0%), Dead Code Surface (formerly Dead Code) (28.8%)
- **Documentation Coverage:** 35.7143% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `handler` **(Many-Argument Workhorses)** (Impact: 41.8)
  * `runStep` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* /// Takes the given CompileStep and options and returns a run step. /// The run step from this funct...
  * `make` **(Defensive Guards)** (Impact: 4.5)
  * `create` **(Defensive Guards)** (Impact: 2.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 46
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 27`, `structural_boundaries: 23`, `args: 4`, `func_start: 4`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 16`, `dead_code: 7`, `planned_debt: 9`, `unreferenced_by_name: 1`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 20`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` Sdk.zig, builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gles/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 123.84 | **LOC:** 318 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (44.9%), Debt Markers (formerly Tech Debt) (16.7%)
- **Documentation Coverage:** 96.7742% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runStep` **(Defensive Guards)** (Impact: 8.0)
  * `Events` **(Generic / Templated Code)** (Impact: 7.0)
  * `setCallback` **(State Mutators)** (Impact: 4.7)
  * `create` **(I/O & Config Routines)** (Impact: 4.3)
  * `create` **(Defensive Guards)** (Impact: 3.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 12`, `structural_boundaries: 31`, `args: 29`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 1`, `dead_code: 1`, `planned_debt: 4`
* *Architecture:* `api: 41`, `import: 6`
* *Defense:* `safety: 15`, `doc: 1`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capy.zig, trait.zig, shared.zig, glfw3.h, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 115.64 | **LOC:** 177 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (84.5%), Guard Balance (formerly Safety Score) (76.1%), Mutation Surface (formerly State Flux) (36.4%), Complexity Load (formerly Cognitive Load) (22.6%)
- **Documentation Coverage:** 90.625% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Events` **(Type Conversions)** (Impact: 35.3)
  * `processEvent` **(Type Conversions)** (Impact: 33.0)
  * `setCallback` **(Many-Argument Workhorses)** (Impact: 4.9)
  * `setUserData` **(State Mutators)** (Impact: 4.0)
  * `requestDraw` **(State Mutators)** (Impact: 3.1)
    * *Intent:* /// Requests a redraw
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 1 instances
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 19`, `structural_boundaries: 8`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 5`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `safety: 12`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` capy.zig, trait.zig, shared.zig, Container.zig, js.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/capy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 111.72 | **LOC:** 206 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **43** in-repo importer(s); it depends on **34**; blast radius 84.423; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (45.6%), Mutation Surface (formerly State Flux) (36.7%), Debt Markers (formerly Tech Debt) (11.9%)
- **Documentation Coverage:** 69.2308% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `animateAtoms` **(Defensive Guards)** (Impact: 12.9)
  * `runEventLoop` **(Interface Declarations)** (Impact: 3.4)
  * `stepEventLoop` **(Defensive Guards)** (Impact: 3.3)
    * *Intent:* /// Returns false if the last window has been closed. /// Even if the wanted step type is Blocking, ...
  * `init` **(Defensive Guards)** (Impact: 2.9)
  * `deinit` **(I/O & Config Routines)** (Impact: 2.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 2 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *State Mutation (weighted view):* 7
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 18`, `args: 8`, `func_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 2`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `api: 74`, `import: 72`
* *Defense:* `safety: 8`, `doc: 5`, `sync_locks: 2`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 84.423
  * `Choke Point (Betweenness):` 0.096377 | `Ripple Effect (Closeness):` 0.279851
  * `Imports (Out-Degree: 28):` AnimationController.zig, audio.zig, backend.zig, shared.zig, builtin, Alignment.zig, Button.zig, Canvas.zig...
  * `Imported By (In-Degree: 43):` (Excluded from Brief to save tokens)

### `src/backends/gtk/Window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 109.86 | **LOC:** 214 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.286; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (93.7%), Connectivity (formerly Api Exposure) (64.4%), Mutation Surface (formerly State Flux) (55.5%), Debt Markers (formerly Tech Debt) (18.9%)
- **Documentation Coverage:** 96.5517% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `gtkLayout` **(Type Conversions)** (Impact: 26.1)
  * `initMenu` **(Type Conversions)** (Impact: 9.6)
  * `setFullscreen` **(Type Conversions)** (Impact: 6.5)
  * `gtkCloseRequest` **(Defensive Guards)** (Impact: 5.7)
  * `create` **(Type Conversions)** (Impact: 5.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 24`, `structural_boundaries: 10`, `args: 18`, `func_start: 17`
* *Risk/State:* `safety_bypasses: 36`, `state_mutation: 7`, `planned_debt: 3`
* *Architecture:* `api: 14`, `import: 8`
* *Defense:* `safety: 18`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.286
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` capy.zig, ImageData.zig, Monitor.zig, common.zig, gtk.zig, std, windowbin.zig
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

- `src/capy.zig` -> **Severity: 3.536** (Bridge: 0.0964 * Flux: 36.6864%)
- `src/containers.zig` -> **Severity: 2.445** (Bridge: 0.0264 * Flux: 92.5744%)
- `src/data.zig` -> **Severity: 1.397** (Bridge: 0.0156 * Flux: 89.3063%)
- `src/components/Image.zig` -> **Severity: 0.823** (Bridge: 0.0082 * Flux: 100.0%)
- `src/internal.zig` -> **Severity: 0.765** (Bridge: 0.0239 * Flux: 31.9676%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/widget.zig` -> **Severity: 21.087** (Embedded: 0.2604 * Error Risk: 80.9733%)
- `src/AnimationController.zig` -> **Severity: 16.062** (Embedded: 0.2622 * Error Risk: 61.25%)
- `src/components/Slider.zig` -> **Severity: 15.135** (Embedded: 0.182 * Error Risk: 83.1441%)
- `src/components/Dropdown.zig` -> **Severity: 14.563** (Embedded: 0.182 * Error Risk: 80.0%)
- `src/components/Image.zig` -> **Severity: 14.358** (Embedded: 0.182 * Error Risk: 78.8731%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/data.zig` -> **Severity: 6592.918** (Blast Radius: 116.309 * Doc Risk: 56.6845%)
- `src/AnimationController.zig` -> **Severity: 6551.6** (Blast Radius: 65.516 * Doc Risk: 100.0%)
- `src/capy.zig` -> **Severity: 5844.672** (Blast Radius: 84.423 * Doc Risk: 69.2308%)
- `src/internal.zig` -> **Severity: 5217.446** (Blast Radius: 91.671 * Doc Risk: 56.9149%)
- `src/trait.zig` -> **Severity: 5073.5** (Blast Radius: 50.735 * Doc Risk: 100.0%)

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
