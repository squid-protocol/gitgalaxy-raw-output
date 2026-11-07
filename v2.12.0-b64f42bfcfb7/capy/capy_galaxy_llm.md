# ARCHITECTURAL_BRIEF: capy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/capy-ui/capy.git` |
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
- **Scope:** 132 analyzed artifact(s), 14739 LOC.
- **Load-bearing artifact:** `src/capy.zig` -- 44 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/capy.zig` -- pulls in 38 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/backends/win32/backend.zig` at magnitude 718.28 (structural weight, not risk).
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
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 385 |
| Total LOC | 14739 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 25.5% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.4323 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.4257 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 54.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 3.0426 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 118 | 13586 | 89.4% |
| MARKDOWN | 3 | 0 | 2.3% |
| YAML | 2 | 58 | 1.5% |
| C | 2 | 30 | 1.5% |
| GLSL | 2 | 8 | 1.5% |
| JAVASCRIPT | 2 | 925 | 1.5% |
| NIX | 1 | 106 | 0.8% |
| HTML | 1 | 26 | 0.8% |
| XML | 1 | 0 | 0.8% |

## 4.1 SOURCE ENCODINGS
All 132 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 27%, Large Core Modules (3) 17%, State Mutators Files 16%, Type Conversions Files 15%, Data / Markup / Trivial 8%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 129 | 97.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 3 | 2.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 385*

**Composition by Extension & Reason:**
- `.zig`: 347x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unrecognized Syntax (Dense Structure / Global Regex Timeout)
- `no_extension`: 11x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 5x Excluded (Explicitly Denied Extension: '.png')
- `.md`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.nix`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lock`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Unsupported Extension: '.lock')
- `.class`: 2x Excluded (Explicitly Denied Extension: '.class')
- `.java`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.o`: 2x Excluded (Explicitly Denied Extension: '.o')
- `.dex`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.stl`: 1x Excluded (Explicitly Denied Extension: '.stl')
- `.c`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.rc`: 1x Unsupported Format (.rc)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 91.9 | 9.8 | 5.5 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 80.0 | 44.4 | 47.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 7.4 | 2.4 | 0.0 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 45.8 | 55.6 | 100.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 4.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 27.4 | 14.1 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.1 | 3.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 57.6 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 82.6 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 1194 | 88 | 25 | `src/backends/win32/backend.zig` |
| cleanup | 248 | 62 | 5 | `src/data.zig` |
| guards | 1408 | 111 | 20 | `src/backends/android/backend.zig` |
| danger | 1152 | 87 | 17 | `src/backends/android/backend.zig` |
| concurrency | 193 | 19 | 2 | `src/backends/wasm/capy-worker.js` |
| connectivity | 1778 | 122 | 27 | `src/backends/win32/win32.zig` |
| io | 78 | 17 | 2 | `src/backends/win32/win32.zig` |
| crypto | 0 | 0 | 0 | - |
| ipc | 52 | 7 | 0 | `src/backends/wasm/capy-worker.js` |
| time | 29 | 9 | 0 | `src/fuzz.zig` |
| serialization | 1 | 1 | 0 | `examples/osm-viewer.zig` |
| regex | 1 | 1 | 0 | `src/assets.zig` |
| events | 57 | 25 | 1 | `src/backends/wasm/capy.js` |
| tests | 105 | 9 | 0 | `src/data.zig` |
| docs | 462 | 70 | 8 | `src/data.zig` |
| debt | 288 | 78 | 5 | `src/backends/win32/backend.zig` |
| mutation | 4121 | 125 | 74 | `src/backends/win32/backend.zig` |
| dead_code | 195 | 54 | 3 | `src/backends/wasm/capy-worker.js` |
| credential | 2 | 1 | 0 | `build.zig.zon` |
| threat | 2 | 1 | 0 | `src/backend.zig` |
| ml_ai | 515 | 48 | 9 | `src/backends/gtk/Canvas.zig` |
| ui | 679 | 75 | 17 | `examples/demo.zig` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.1166**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/backends/win32/win32.zig` (Hits: 25)
- `src/assets.zig` (Hits: 10)
- `src/backends/win32/backend.zig` (Hits: 9)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **capy.zig** (`src/capy.zig`) — 44 inbound connections
2. **data.zig** (`src/data.zig`) — 39 inbound connections
3. **backend.zig** (`src/backend.zig`) — 32 inbound connections
4. **internal.zig** (`src/internal.zig`) — 30 inbound connections
5. **window.zig** (`src/window.zig`) — 29 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **capy.zig** (`src/capy.zig`) — 38 outbound dependencies
2. **backend.zig** (`src/backends/gtk/backend.zig`) — 21 outbound dependencies
3. **backend.zig** (`src/backends/wasm/backend.zig`) — 17 outbound dependencies
4. **backend.zig** (`src/backends/win32/backend.zig`) — 11 outbound dependencies
5. **internal.zig** (`src/internal.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Atom` **(Many-Argument Workhorses)** (@ `src/data.zig`) -> Impact: **115.9** | LOC: 592
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `process` **(Many-Argument Workhorses)** (@ `src/backends/win32/backend.zig`) -> Impact: **98.3** | LOC: 222
- `Events` **(Type Conversions)** (@ `src/backends/win32/backend.zig`) -> Impact: **82.1** | LOC: 312
- `GridLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **81.2** | LOC: 238
  * *Intent:* /// Grid layout based on the CSS Grid algorithm
- `Widgeting` **(Defensive Guards)** (@ `src/internal.zig`) -> Impact: **65.1** | LOC: 313
  * *Intent:* /// Convenience function for creating widgets
- `RowLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **54.3** | LOC: 81
  * *Intent:* /// Arranges items horizontally.
- `ColumnLayout` **(Many-Argument Workhorses)** (@ `src/containers.zig`) -> Impact: **53.9** | LOC: 74
  * *Intent:* /// Arranges items vertically.
- `Events` **(Type Conversions)** (@ `src/backends/gtk/common.zig`) -> Impact: **53.4** | LOC: 248
- `handler` **(Many-Argument Workhorses)** (@ `build_capy.zig`) -> Impact: **41.8** | LOC: 75
- `Events` **(Defensive Guards)** (@ `src/internal.zig`) -> Impact: **40.1** | LOC: 236
  * *Intent:* /// Convenience function for creating widgets

*Function archetypes referenced above:*
  * **Defensive Guards**: validation and error handling (null checks, guards, early bailouts)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Type Conversions**: cast- and conversion-heavy function

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src` | 25 | 2763.08 | 11.37% | 28.53% |
| `src/backends/wasm` | 16 | 1628.82 | 19.43% | 21.3% |
| `src/backends/win32` | 5 | 1206.46 | 9.22% | 14.92% |
| `src/backends/gtk` | 19 | 885.62 | 10.77% | 13.38% |
| `examples` | 25 | 651.0 | 6.78% | 0.0% |
| `src/components` | 15 | 614.76 | 8.65% | 13.93% |
| `src/backends/android` | 1 | 358.24 | 17.08% | 27.68% |
| `src/backends/macos` | 4 | 266.22 | 5.52% | 33.54% |
| `__monolith__` | 5 | 224.24 | 6.41% | 16.7% |
| `src/backends/gles` | 1 | 123.84 | 8.27% | 15.36% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `src/backends/macos/CapyAppDelegate.zig` -> **100.0%** Exposure
- `src/c_api.zig` -> **100.0%** Exposure
- `src/http.zig` -> **100.0%** Exposure
- `src/backends/wasm/capy-worker.js` -> **100.0%** Exposure
- `src/flat/toggle_switch.zig` -> **99.9998%** Exposure
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
- `src/flat/button.zig` -> **5** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `381` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/backends/win32/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.976)
- **Top Global Matches:** file_cluster_12: 8.976, file_cluster_7: 9.099, file_cluster_5: 10.201
- **Magnitude:** 718.28 | **LOC:** 1773 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **11**; blast radius 14.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (67.3%), Mutation Surface (formerly State Flux) (24.0%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.806
  * `Choke Point (Betweenness):` 0.029255 | `Ripple Effect (Closeness):` 0.300144
  * `Imports (Out-Degree: 9):` backend.zig, capy.zig, trait.zig, shared.zig, Dropdown.zig, Monitor.zig, builtin, gdip.zig...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `src/data.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.402)
- **Top Global Matches:** file_cluster_12: 8.402, file_cluster_5: 9.272, file_cluster_7: 10.981
- **Magnitude:** 696.02 | **LOC:** 1349 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **39** in-repo importer(s); it depends on **7**; blast radius 88.261; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (88.5%), Guard Balance (formerly Safety Score) (44.7%), Complexity Load (formerly Cognitive Load) (20.9%)
- **Documentation Coverage:** 56.6845% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Atom` **(Many-Argument Workhorses)** (Impact: 115.9)
    * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to //...
  * `lerp` **(Many-Argument Workhorses)** (Impact: 31.9)
    * *Intent:* /// Linear interpolation between any two values a and b with factor t. /// Both values must be of th...
  * `ListAtom` **(Defensive Guards)** (Impact: 26.8)
    * *Intent:* /// A list of atoms, that is itself an atom.
  * `dependOn` **(Many-Argument Workhorses)** (Impact: 18.0)
    * *Intent:* // TODO: constrain "function"'s type based on tuple // TODO: optionally provide the function with an...
  * `extendedSet` **(Many-Argument Workhorses)** (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 8
* *State Mutation (weighted view):* 114
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 96`, `structural_boundaries: 176`, `args: 89`, `func_start: 83`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 31`, `high_risk_execution: 6`, `state_mutation: 50`, `planned_debt: 8`
* *Architecture:* `api: 76`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 123`, `doc: 77`, `test: 56`, `sync_locks: 48`, `cleanup: 35`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 88.261
  * `Choke Point (Betweenness):` 0.021073 | `Ripple Effect (Closeness):` 0.484848
  * `Imports (Out-Degree: 6):` AnimationController.zig, color.zig, containers.zig, internal.zig, listener.zig, std, trait.zig
  * `Imported By (In-Degree: 39):` (Excluded from Brief to save tokens)

### `src/backends/wasm/capy.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.344)
- **Top Global Matches:** file_cluster_12: 7.344, file_cluster_10: 9.009, file_cluster_7: 9.859
- **Magnitude:** 608.44 | **LOC:** 635 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **1**; blast radius 3.588; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Complexity Load (formerly Cognitive Load) (91.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 97.8723% of unit weight undocumented
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
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 100`, `dead_code: 5`, `planned_debt: 3`
* *Architecture:* `io: 1`, `api: 36`, `concurrency: 18`, `import: 1`
* *Defense:* `safety: 27`, `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.588
  * `Choke Point (Betweenness):` 5.8e-05 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/internal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 8.671)
- **Top Global Matches:** file_cluster_5: 8.671, file_cluster_12: 9.782, file_cluster_7: 10.767
- **Magnitude:** 491.76 | **LOC:** 799 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **30** in-repo importer(s); it depends on **10**; blast radius 72.593; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (44.8%), Mutation Surface (formerly State Flux) (32.0%), Complexity Load (formerly Cognitive Load) (30.0%)
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
* *Risk/State:* `safety_bypasses: 34`, `high_risk_execution: 6`, `state_mutation: 11`, `dead_code: 15`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 69`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 95`, `doc: 52`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 72.593
  * `Choke Point (Betweenness):` 0.033023 | `Ripple Effect (Closeness):` 0.460334
  * `Imports (Out-Degree: 7):` AnimationController.zig, backend.zig, shared.zig, builtin, containers.zig, data.zig, root, std...
  * `Imported By (In-Degree: 30):` (Excluded from Brief to save tokens)

### `src/containers.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.769)
- **Top Global Matches:** file_cluster_4: 7.769, file_cluster_12: 10.685, file_cluster_15: 11.702
- **Magnitude:** 473.5 | **LOC:** 924 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **8**; blast radius 27.555; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (92.6%), Connectivity (formerly Api Exposure) (75.4%), Guard Balance (formerly Safety Score) (44.0%), Debt Markers (formerly Tech Debt) (24.9%)
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
* *Risk/State:* `safety_bypasses: 10`, `high_risk_execution: 7`, `state_mutation: 32`, `dead_code: 6`, `planned_debt: 17`, `fragile_debt: 1`
* *Architecture:* `api: 37`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 98`, `doc: 33`, `test: 4`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 27.555
  * `Choke Point (Betweenness):` 0.018311 | `Ripple Effect (Closeness):` 0.364175
  * `Imports (Out-Degree: 8):` AnimationController.zig, backend.zig, capy.zig, Alignment.zig, data.zig, internal.zig, std, widget.zig
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/backends/win32/win32.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.351)
- **Top Global Matches:** file_cluster_7: 8.351, file_cluster_12: 9.389, file_cluster_5: 10.547
- **Magnitude:** 368.08 | **LOC:** 423 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **3**; blast radius 8.54; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (78.7%), Debt Markers (formerly Tech Debt) (9.9%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 8.54
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.22699
  * `Imports (Out-Degree: 0):` builtin, std, zigwin32
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/backends/android/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 9.992)
- **Top Global Matches:** file_cluster_7: 9.992, file_cluster_14: 10.064, file_cluster_5: 10.913
- **Magnitude:** 358.24 | **LOC:** 873 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **6**; blast radius 24.045; role: Transceiver (Middle-Tier)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 24.045
  * `Choke Point (Betweenness):` 0.029085 | `Ripple Effect (Closeness):` 0.348678
  * `Imports (Out-Degree: 4):` capy.zig, trait.zig, shared.zig, android, root, std
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/backends/wasm/capy-worker.js` (JAVASCRIPT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.071)
- **Top Global Matches:** file_cluster_12: 8.071, file_cluster_10: 8.577, file_cluster_15: 10.11
- **Magnitude:** 343.36 | **LOC:** 451 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **1**; blast radius 1.94; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (100.0%), Concurrency Surface (formerly Concurrency) (100.0%), Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (81.6%)
- **Documentation Coverage:** 89.7059% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `clock_time_get` **(Many-Argument Workhorses)** (Impact: 15.2)
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
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 26`, `dead_code: 3`, `planned_debt: 5`, `unreferenced_by_name: 54`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 51`, `import: 1`
* *Defense:* `safety: 2`, `doc: 6`, `sync_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gtk/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Centroid distance: 9.729)
- **Top Global Matches:** file_cluster_5: 9.729, file_cluster_7: 9.864, file_cluster_12: 10.593
- **Magnitude:** 215.74 | **LOC:** 320 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **6**; blast radius 16.152; role: Transceiver (Middle-Tier)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 16.152
  * `Choke Point (Betweenness):` 0.015017 | `Ripple Effect (Closeness):` 0.242424
  * `Imports (Out-Degree: 5):` capy.zig, trait.zig, shared.zig, backend.zig, gtk.zig, std
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/backends/macos/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.605)
- **Top Global Matches:** file_cluster_15: 6.605, file_cluster_11: 7.939, file_cluster_0: 7.949
- **Magnitude:** 170.02 | **LOC:** 381 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **9**; blast radius 10.429; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (51.3%), Mutation Surface (formerly State Flux) (42.3%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 10.429
  * `Choke Point (Betweenness):` 0.024007 | `Ripple Effect (Closeness):` 0.294746
  * `Imports (Out-Degree: 8):` capy.zig, trait.zig, shared.zig, AppKit.zig, CapyAppDelegate.zig, Monitor.zig, Button.zig, objc...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/backends/wasm/js.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Centroid distance: 6.944)
- **Top Global Matches:** file_cluster_2: 6.944, file_cluster_15: 7.037, file_cluster_17: 7.43
- **Magnitude:** 160.74 | **LOC:** 107 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); blast radius 15.271; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Debt Markers (formerly Tech Debt) (12.7%)
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
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 15.271
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.246138
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `examples/balls.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.694)
- **Top Global Matches:** file_cluster_6: 8.694, file_cluster_8: 13.114, file_cluster_4: 14.864
- **Magnitude:** 145.94 | **LOC:** 233 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.94; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Complexity Load (formerly Cognitive Load) (64.9%), Guard Balance (formerly Safety Score) (60.9%), Concurrency Surface (formerly Concurrency) (16.5%), Connectivity (formerly Api Exposure) (5.1%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` capy, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fuzz.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.556)
- **Top Global Matches:** file_cluster_12: 7.556, file_cluster_5: 7.97, file_cluster_7: 10.117
- **Magnitude:** 130.32 | **LOC:** 218 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **3**; blast radius 4.325; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (72.6%), Connectivity (formerly Api Exposure) (59.7%), Guard Balance (formerly Safety Score) (44.4%), Dead Code Surface (formerly Dead Code) (36.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.325
  * `Choke Point (Betweenness):` 0.000117 | `Ripple Effect (Closeness):` 0.27934
  * `Imports (Out-Degree: 2):` color.zig, std, trait.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/osm-viewer.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.858)
- **Top Global Matches:** file_cluster_7: 8.858, file_cluster_12: 10.063, file_cluster_5: 10.922
- **Magnitude:** 127.18 | **LOC:** 296 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.94; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Complexity Load (formerly Cognitive Load) (19.3%), Connectivity (formerly Api Exposure) (9.5%)
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
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 11`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 3`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 41`, `doc: 2`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` capy, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gtk/Canvas.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.499)
- **Top Global Matches:** file_cluster_7: 8.499, file_cluster_12: 9.785, file_cluster_5: 10.567
- **Magnitude:** 125.88 | **LOC:** 240 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **7**; blast radius 2.5; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.3%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.2%), Connectivity (formerly Api Exposure) (69.7%)
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
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 8`, `planned_debt: 3`
* *Architecture:* `api: 22`, `import: 7`
* *Defense:* `safety: 9`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.5
  * `Choke Point (Betweenness):` 0.00027 | `Ripple Effect (Closeness):` 0.223268
  * `Imports (Out-Degree: 5):` backend.zig, capy.zig, shared.zig, Window.zig, common.zig, gtk.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `build_capy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 8.641)
- **Top Global Matches:** file_cluster_8: 8.641, file_cluster_6: 10.422, file_cluster_4: 18.518
- **Magnitude:** 124.62 | **LOC:** 301 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 3.588; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.9%), Guard Balance (formerly Safety Score) (53.2%), Debt Markers (formerly Tech Debt) (48.0%), Connectivity (formerly Api Exposure) (35.7%)
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
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 16`, `dead_code: 6`, `planned_debt: 9`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 1`, `import: 4`
* *Defense:* `safety: 20`, `doc: 8`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.588
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007576
  * `Imports (Out-Degree: 0):` Sdk.zig, builtin, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/gles/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.643)
- **Top Global Matches:** file_cluster_12: 6.643, file_cluster_5: 8.21, file_cluster_7: 9.307
- **Magnitude:** 123.84 | **LOC:** 318 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **5**; blast radius 1.94; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (47.9%), Debt Markers (formerly Tech Debt) (15.4%)
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
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capy.zig, trait.zig, shared.zig, glfw3.h, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/common.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 12.805)
- **Top Global Matches:** file_cluster_6: 12.805, file_cluster_4: 15.325, file_cluster_5: 18.402
- **Magnitude:** 115.64 | **LOC:** 177 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **6**; blast radius 9.26; role: Transceiver (Middle-Tier)
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
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 5`, `planned_debt: 3`
* *Architecture:* `api: 13`, `import: 6`
* *Defense:* `safety: 12`, `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 9.26
  * `Choke Point (Betweenness):` 0.001523 | `Ripple Effect (Closeness):` 0.231467
  * `Imports (Out-Degree: 6):` capy.zig, trait.zig, shared.zig, Container.zig, js.zig, std
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/capy.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 11.606)
- **Top Global Matches:** file_cluster_15: 11.606, file_cluster_12: 11.719, file_cluster_11: 12.031
- **Magnitude:** 111.72 | **LOC:** 206 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **44** in-repo importer(s); it depends on **38**; blast radius 76.128; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Guard Balance (formerly Safety Score) (48.0%), Mutation Surface (formerly State Flux) (36.7%), Debt Markers (formerly Tech Debt) (10.3%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 76.128
  * `Choke Point (Betweenness):` 0.231025 | `Ripple Effect (Closeness):` 0.418058
  * `Imports (Out-Degree: 35):` AnimationController.zig, audio.zig, backend.zig, shared.zig, builtin, color.zig, Alignment.zig, Button.zig...
  * `Imported By (In-Degree: 44):` (Excluded from Brief to save tokens)

### `src/backends/gtk/Window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Centroid distance: 9.009)
- **Top Global Matches:** file_cluster_14: 9.009, file_cluster_7: 9.466, file_cluster_5: 11.925
- **Magnitude:** 109.86 | **LOC:** 214 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **7**; blast radius 2.925; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (64.4%), Mutation Surface (formerly State Flux) (55.5%), Debt Markers (formerly Tech Debt) (16.7%)
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
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.925
  * `Choke Point (Betweenness):` 0.00212 | `Ripple Effect (Closeness):` 0.224491
  * `Imports (Out-Degree: 5):` capy.zig, ImageData.zig, Monitor.zig, common.zig, gtk.zig, std, windowbin.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `examples/graph.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.177)
- **Top Global Matches:** file_cluster_12: 8.177, file_cluster_7: 8.663, file_cluster_5: 10.339
- **Magnitude:** 100.12 | **LOC:** 227 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **2**; blast radius 1.94; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (57.0%), Complexity Load (formerly Cognitive Load) (24.0%), Connectivity (formerly Api Exposure) (9.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `draw` **(Type Conversions)** (Impact: 14.8)
  * `myDataFunction` **(Compute Cores)** (Impact: 10.6)
  * `main` **(I/O & Config Routines)** (Impact: 5.8)
  * `callback` **(Type Conversions)** (Impact: 4.7)
  * `show` **(Defensive Guards)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 35`, `args: 21`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 11`, `planned_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 12`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.94
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` capy, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/backend.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.917)
- **Top Global Matches:** file_cluster_15: 7.917, file_cluster_0: 9.16, file_cluster_11: 9.482
- **Magnitude:** 93.58 | **LOC:** 193 | **CtrlFlow:** 10.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 10.855; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (100.0%), Mutation Surface (formerly State Flux) (50.4%), Guard Balance (formerly Safety Score) (45.6%), Complexity Load (formerly Cognitive Load) (22.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `runStep` **(Defensive Guards)** (Impact: 14.3)
    * *Intent:* // Temporary execution until async is added back in Zig
  * `log` **(Defensive Guards)** (Impact: 7.4)
  * `panic` **(State Mutators)** (Impact: 4.5)
  * `create` **(Defensive Guards)** (Impact: 3.5)
  * `executeMain` **(Defensive Guards)** (Impact: 3.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 15`, `structural_boundaries: 11`, `args: 15`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `api: 30`, `import: 20`
* *Defense:* `safety: 12`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 10.855
  * `Choke Point (Betweenness):` 0.070791 | `Ripple Effect (Closeness):` 0.29369
  * `Imports (Out-Degree: 15):` capy.zig, trait.zig, shared.zig, Button.zig, Canvas.zig, Container.zig, Dropdown.zig, ImageData.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/dev_tools.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Centroid distance: 7.852)
- **Top Global Matches:** file_cluster_0: 7.852, file_cluster_5: 8.496, file_cluster_12: 8.651
- **Magnitude:** 82.58 | **LOC:** 176 | **CtrlFlow:** 14.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **4**; blast radius 3.788; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Concurrency Surface (formerly Concurrency) (84.3%), Mutation Surface (formerly State Flux) (50.4%), Connectivity (formerly Api Exposure) (48.3%), Guard Balance (formerly Safety Score) (38.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `connectionRunner` **(Defensive Guards)** (Impact: 9.8)
  * `writeStructField` **(Defensive Guards)** (Impact: 8.4)
  * `readStructField` **(Defensive Guards)** (Impact: 7.4)
  * `writeResponse` **(Defensive Guards)** (Impact: 5.7)
  * `writeRequest` **(Defensive Guards)** (Impact: 5.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 1 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 8
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 9`, `args: 10`, `func_start: 10`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 2`, `high_risk_execution: 1`, `state_mutation: 3`, `planned_debt: 2`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 3`, `import: 4`
* *Defense:* `safety: 28`, `doc: 1`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.788
  * `Choke Point (Betweenness):` 0.000102 | `Ripple Effect (Closeness):` 0.27589
  * `Imports (Out-Degree: 2):` builtin, internal.zig, std, trait.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/win32/Monitor.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Centroid distance: 8.905)
- **Top Global Matches:** file_cluster_7: 8.905, file_cluster_14: 10.049, file_cluster_12: 10.914
- **Magnitude:** 78.92 | **LOC:** 197 | **CtrlFlow:** 10.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 3.338; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Guard Balance (formerly Safety Score) (80.0%), Connectivity (formerly Api Exposure) (71.2%), Mutation Surface (formerly State Flux) (50.2%), Complexity Load (formerly Cognitive Load) (15.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `getList` **(Defensive Guards)** (Impact: 13.4)
  * `getDpi` **(Defensive Guards)** (Impact: 6.4)
  * `getInternalName` **(Defensive Guards)** (Impact: 4.6)
  * `deinitAllPeers` **(Defensive Guards)** (Impact: 3.4)
  * `getNumberOfVideoModes` **(Parameter Forwarders)** (Impact: 3.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 10 instances
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 3 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 10
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 39`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 10`, `state_mutation: 4`, `planned_debt: 1`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 26`, `cleanup: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.338
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.219089
  * `Imports (Out-Degree: 2):` capy.zig, builtin, std, win32.zig, zigwin32
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.195)
- **Top Global Matches:** file_cluster_12: 7.195, file_cluster_15: 9.128, file_cluster_5: 9.904
- **Magnitude:** 78.9 | **LOC:** 200 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **29** in-repo importer(s); it depends on **9**; blast radius 41.571; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (59.5%), Guard Balance (formerly Safety Score) (44.8%), Debt Markers (formerly Tech Debt) (37.8%), Mutation Surface (formerly State Flux) (31.0%)
- **Documentation Coverage:** 59.2593% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setPreferredSize` **(Type Conversions)** (Impact: 13.1)
    * *Intent:* /// Attempt to resize the window to the given size. /// On certain platforms (e.g. mobile) or config...
  * `propertyChanged` **(Type Conversions)** (Impact: 8.4)
  * `setFullscreen` **(Defensive Guards)** (Impact: 7.4)
    * *Intent:* /// Set the fullscreen state of the window.
  * `set` **(Defensive Guards)** (Impact: 5.9)
    * *Intent:* /// wrappedContainer can be an error union, a pointer to the container or the container itself.
  * `deinit` **(Defensive Guards)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 2 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 6
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 14`, `structural_boundaries: 8`, `args: 14`, `func_start: 14`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `high_risk_execution: 1`, `state_mutation: 2`, `dead_code: 2`, `planned_debt: 6`
* *Architecture:* `api: 15`, `import: 12`
* *Defense:* `safety: 15`, `doc: 13`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 41.571
  * `Choke Point (Betweenness):` 0.115572 | `Ripple Effect (Closeness):` 0.374152
  * `Imports (Out-Degree: 9):` AnimationController.zig, backend.zig, Menu.zig, data.zig, internal.zig, listener.zig, monitor.zig, std...
  * `Imported By (In-Degree: 29):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/components/Navigation.zig` (ZIG) | Magnitude: 73.48 | Delta: **0.052** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 94, core_var_decl: 22, pointers: 19, safety: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/AnimationController.zig` (ZIG) | Magnitude: 31.4 | Delta: **0.015** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 58, core_var_decl: 19, structural_boundaries: 10, globals: 10
- `src/components/TextField.zig` (ZIG) | Magnitude: 39.04 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 57, core_var_decl: 13, args: 11, func_start: 11
- `src/backends/win32/backend.zig` (ZIG) | Magnitude: 718.28 | Delta: **0.123** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 1384, core_var_decl: 399, explicit_casts: 167, design_short_vars: 155
- `src/image.zig` (ZIG) | Magnitude: 28.64 | Delta: **0.134** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 62, core_var_decl: 18, design_snake_case: 13, structural_boundaries: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `src/backends/macos/CapyAppDelegate.zig` (ZIG) | Magnitude: 57.06 | Delta: **0.157** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 93, core_var_decl: 32, structural_boundaries: 28, args: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `src/capy.zig` (ZIG) | Magnitude: 111.72 | Delta: **0.113** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: core_var_decl: 77, api: 74, import: 72, globals: 67

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/foo_app.zig` (ZIG) | Magnitude: 6.66 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 18, ui_framework: 12, safety: 10, structural_boundaries: 7
- `src/backends/wasm/js.zig` (ZIG) | Magnitude: 160.74 | Delta: **0.093** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: api: 60, args: 53, func_start: 53, pointers: 24
- `src/testing.zig` (ZIG) | Magnitude: 6.02 | Delta: **0.152** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 8, api: 3, ui_framework: 3, core_var_decl: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `src/backends/gtk/common.zig` (ZIG) | Magnitude: 215.74 | Delta: **0.135** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 236, core_var_decl: 69, design_snake_case: 49, explicit_casts: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/components/TextArea.zig` (ZIG) | Magnitude: 33.7 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 14, structural_boundaries: 9, args: 9
- `src/components/Label.zig` (ZIG) | Magnitude: 36.06 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 51, core_var_decl: 13, structural_boundaries: 9, args: 9
- `src/backends/android/backend.zig` (ZIG) | Magnitude: 358.24 | Delta: **0.072** (centroid distance) | Secondary Pull: `file_cluster_14`
  * Top Architectural Signatures: indent_spaces: 629, core_var_decl: 218, structural_boundaries: 153, safety: 141
- `examples/abc.zig` (ZIG) | Magnitude: 12.2 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, ui_framework: 12, core_var_decl: 10, design_snake_case: 6
- `src/c_api.zig` (ZIG) | Magnitude: 34.96 | Delta: **0.101** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 29, api: 14, args: 12, func_start: 12

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/capy.zig` -> **Severity: 8.475** (Bridge: 0.231 * Flux: 36.6864%)
- `src/backends/gtk/backend.zig` -> **Severity: 3.665** (Bridge: 0.1058 * Flux: 34.6311%)
- `src/window.zig` -> **Severity: 3.583** (Bridge: 0.1156 * Flux: 31.0026%)
- `src/backends/wasm/backend.zig` -> **Severity: 3.568** (Bridge: 0.0708 * Flux: 50.4027%)
- `src/data.zig` -> **Severity: 1.866** (Bridge: 0.0211 * Flux: 88.5385%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/widget.zig` -> **Severity: 32.613** (Embedded: 0.4077 * Error Risk: 80.0%)
- `src/backends/android/backend.zig` -> **Severity: 27.894** (Embedded: 0.3487 * Error Risk: 80.0%)
- `src/AnimationController.zig` -> **Severity: 24.969** (Embedded: 0.4077 * Error Risk: 61.25%)
- `src/components/Dropdown.zig` -> **Severity: 21.997** (Embedded: 0.275 * Error Risk: 80.0%)
- `src/components/Slider.zig` -> **Severity: 21.997** (Embedded: 0.275 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/capy.zig` -> **Severity: 5270.402** (Blast Radius: 76.128 * Doc Risk: 69.2308%)
- `src/data.zig` -> **Severity: 5003.031** (Blast Radius: 88.261 * Doc Risk: 56.6845%)
- `src/internal.zig` -> **Severity: 4131.623** (Blast Radius: 72.593 * Doc Risk: 56.9149%)
- `src/AnimationController.zig` -> **Severity: 3999.1** (Blast Radius: 39.991 * Doc Risk: 100.0%)
- `src/trait.zig` -> **Severity: 3954.5** (Blast Radius: 39.545 * Doc Risk: 100.0%)

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 4408 call pairs -- scoped 19.1%, unique 0.0%, ambiguous 14.0%, external 66.9%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 4169 | 18.9% | 0.0% | 14.8% | 66.4% |
| javascript | 231 | 24.7% | 0.0% | 0.0% | 75.3% |
| c | 8 | 0.0% | 0.0% | 0.0% | 100.0% |

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
