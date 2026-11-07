# ARCHITECTURAL_BRIEF: ghostty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ghostty-org/ghostty` |
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
- **Scope:** 1131 analyzed artifact(s), 221320 LOC.
- **Load-bearing artifact:** `src/quirks.zig` -- 113 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `src/terminal/main.zig` -- pulls in 42 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `src/stb/stb_image.h` at magnitude 9064.94 (structural weight, not risk).
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
| Total Artifacts | 5658 |
| Analyzed Artifacts (Scanned) | 1131 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4527 |
| Total LOC | 221320 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 20.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.683 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1193 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 37.2% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.2337 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 64 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 670 | 174220 | 59.2% |
| SWIFT | 174 | 24026 | 15.4% |
| CPP | 50 | 12124 | 4.4% |
| MARKDOWN | 47 | 0 | 4.2% |
| NIX | 29 | 1273 | 2.6% |
| JSON | 27 | 882 | 2.4% |
| C | 25 | 1075 | 2.2% |
| YAML | 24 | 3481 | 2.1% |
| BLP | 21 | 1157 | 1.9% |
| GLSL | 15 | 583 | 1.3% |
| PLAINTEXT | 13 | 0 | 1.1% |
| XML | 12 | 0 | 1.1% |
| SHELL | 10 | 746 | 0.9% |
| OBJECTIVE-C | 5 | 61 | 0.4% |
| CSS | 4 | 111 | 0.4% |
| HTML | 2 | 952 | 0.2% |
| TD | 1 | 201 | 0.1% |
| MAKEFILE | 1 | 19 | 0.1% |
| PYTHON | 1 | 409 | 0.1% |

## 4.1 SOURCE ENCODINGS
All 1131 parsed files are UTF-8.

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules (2) 27%, Declarative / Non-Code 20%, Data / Markup / Trivial 18%, Large Core Modules (3) 9%, Type Conversions Files 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1071 | 94.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 60 | 5.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4527*

**Composition by Extension & Reason:**
- `no_extension`: 3339x Excluded (Binary Format Detected), 361x Unsupported Format (.undeterminable), 308x Excluded: Neighborhood Micro-Mass Limit Exceeded
- `.txt`: 235x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 92x Excluded (Explicitly Denied Extension: '.png')
- `.zig`: 47x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2775 LOC), 1x Excluded (Embedded Hex Payload: 1617 hex tokens in 674 LOC)
- `.po`: 29x Excluded (Unsupported Extension: '.po')
- `.ttf`: 15x Excluded (Explicitly Denied Extension: '.ttf')
- `.md`: 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2371 LOC)
- `.in`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 20820 hex tokens in 10450 LOC)
- `.nu`: 3x Excluded (Unsupported Extension: '.nu'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 65, Signals: 0)
- `.zon`: 3x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.data`: 3x Excluded (Binary Format Detected)
- `.nix`: 1x Excluded (Machine-Generated Source Code Signature: 382 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.2 | 7.9 | 4.3 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 91.9 | 27.0 | 32.9 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 10.5 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.4 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 27.9 | 21.4 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.7 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.5 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 37.3 | 21.2 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 6336 | 483 | 10 | `src/terminal/Terminal.zig` |
| cleanup | 5651 | 310 | 6 | `src/terminal/Terminal.zig` |
| guards | 33210 | 711 | 51 | `src/terminal/Terminal.zig` |
| danger | 4554 | 442 | 10 | `src/terminal/c/terminal.zig` |
| concurrency | 915 | 122 | 1 | `src/Surface.zig` |
| connectivity | 7454 | 702 | 17 | `src/config/Config.zig` |
| io | 623 | 145 | 1 | `src/shell-integration/bash/ghostty.bash` |
| crypto | 0 | 0 | 0 | - |
| ipc | 186 | 56 | 0 | `macos/Sources/Ghostty/Ghostty.App.swift` |
| time | 13 | 8 | 0 | `macos/Sources/Features/QuickTerminal/QuickTerminalScreenStateCache.swift` |
| serialization | 19 | 7 | 0 | `macos/Tests/ColorizedGhosttyIconTests.swift` |
| regex | 69 | 24 | 0 | `src/config/Config.zig` |
| events | 650 | 224 | 1 | `macos/Sources/Ghostty/Ghostty.App.swift` |
| tests | 3882 | 261 | 6 | `src/terminal/Terminal.zig` |
| docs | 20862 | 667 | 40 | `src/config/Config.zig` |
| debt | 819 | 198 | 1 | `.github/workflows/release-tip.yml` |
| mutation | 50222 | 907 | 83 | `src/terminal/PageList.zig` |
| dead_code | 1005 | 259 | 2 | `src/font/shaper/harfbuzz.zig` |
| credential | 33 | 9 | 0 | `flatpak/zig-packages.json` |
| threat | 39 | 8 | 0 | `src/terminal/Terminal.zig` |
| ml_ai | 1593 | 195 | 2 | `src/terminal/color.zig` |
| ui | 967 | 125 | 1 | `macos/Sources/Ghostty/Surface View/SurfaceView.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/shell-integration/bash/ghostty.bash` (Hits: 65)
- `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish` (Hits: 39)
- `src/cli/ssh-cache/DiskCache.zig` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **quirks.zig** (`src/quirks.zig`) — 113 inbound connections
2. **main.zig** (`src/terminal/main.zig`) — 51 inbound connections
3. **main.zig** (`src/font/main.zig`) — 49 inbound connections
4. **config.zig** (`src/config.zig`) — 46 inbound connections
5. **main.zig** (`src/os/main.zig`) — 41 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/terminal/main.zig`) — 42 outbound dependencies
2. **application.zig** (`src/apprt/gtk/class/application.zig`) — 38 outbound dependencies
3. **surface.zig** (`src/apprt/gtk/class/surface.zig`) — 36 outbound dependencies
4. **main_ghostty.zig** (`src/main_ghostty.zig`) — 34 outbound dependencies
5. **Config.zig** (`src/config/Config.zig`) — 31 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `findSurface` **(Stateful Encapsulated Methods)** (@ `macos/Sources/Ghostty/Ghostty.App.swift`) -> Impact: **978.5** | LOC: 2232
  * *Intent:* #if os(macOS) /// Called when a callback needs access to a specific surface. This should return nil /// when the surface is no longer valid.
- `Renderer` **(Many-Argument Workhorses)** (@ `src/renderer/generic.zig`) -> Impact: **586.1** | LOC: 3294
  * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the input buffers and textures and /// : the vertex/frag...
- `Stream` **(Many-Argument Workhorses)** (@ `src/terminal/stream.zig`) -> Impact: **575.9** | LOC: 1957
  * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T can choose to react to whatever actions it cares ...
- `csiDispatch` **(Many-Argument Workhorses)** (@ `src/terminal/stream.zig`) -> Impact: **484.2** | LOC: 1162
- `rebuildRow` **(Many-Argument Workhorses)** (@ `src/renderer/generic.zig`) -> Impact: **301.4** | LOC: 447
- `stbi__create_png_image_raw` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **265.6** | LOC: 211
  * *Intent:* // create the png data from post-deflated data
- `stbi__bmp_load` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **250.9** | LOC: 202
- `SplitTree` **(Many-Argument Workhorses)** (@ `src/datastruct/split_tree.zig`) -> Impact: **235.5** | LOC: 1315
  * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(*const View, *const View) bool` - Check if two vie...
- `stbi__parse_png_file` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **211.1** | LOC: 182
  * *Intent:* #define STBI__PNG_TYPE(a,b,c,d) (((unsigned) (a) << 24) + ((unsigned) (b) << 16) + ((unsigned) (c) << 8) + (unsigned) (d))
- `load_jpeg_image` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **182.0** | LOC: 162

*Function archetypes referenced above:*
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting
  * **Stateful Encapsulated Methods**: n/a

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/terminal` | 45 | 14012.9 | 7.58% | 5.57% |
| `src/stb` | 4 | 11122.56 | 39.38% | 5.75% |
| `src/apprt/gtk/class` | 22 | 5135.74 | 5.46% | 11.23% |
| `src` | 28 | 3641.56 | 5.68% | 9.24% |
| `macos/Sources/Ghostty` | 16 | 3572.28 | 17.17% | 31.42% |
| `src/renderer` | 17 | 3310.46 | 5.16% | 3.63% |
| `src/config` | 19 | 2473.64 | 3.68% | 5.06% |
| `src/font` | 19 | 2329.96 | 7.1% | 4.99% |
| `macos/Sources/Ghostty/Surface View` | 10 | 2235.06 | 19.21% | 47.04% |
| `macos/Sources/Features/Terminal` | 7 | 2223.98 | 23.54% | 51.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `macos/Sources/Features/Update/UpdateDriver.swift` -> **99.9998%** Exposure
- `macos/Sources/Ghostty/Ghostty.Inspector.swift` -> **99.9998%** Exposure
- `.github/workflows/release-tip.yml` -> **99.9976%** Exposure
- `macos/Sources/Features/About/AboutController.swift` -> **99.9925%** Exposure
- `macos/Sources/Features/QuickTerminal/QuickTerminalWindow.swift` -> **99.9665%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `src/shell-integration/bash/bash-preexec.sh` -> **100.0%** Exposure
- `src/shell-integration/bash/ghostty.bash` -> **100.0%** Exposure
- `src/config/c_get.zig` -> **100.0%** Exposure
- `src/config/key.zig` -> **100.0%** Exposure
- `src/datastruct/intrusive_linked_list.zig` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` -> **54** Orphaned Functions | **0** Duplicates
- `macos/Tests/Splits/SplitTreeTests.swift` -> **50** Orphaned Functions | **0** Duplicates
- `macos/Sources/Features/Terminal/BaseTerminalController.swift` -> **48** Orphaned Functions | **0** Duplicates
- `macos/Tests/Ghostty/ConfigTests.swift` -> **36** Orphaned Functions | **0** Duplicates
- `src/terminal/stream_terminal.zig` -> **0** Orphaned Functions | **30** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `11` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2914` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `src/stb/stb_image.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.538)
- **Top Global Matches:** file_cluster_4: 6.538, file_cluster_6: 7.828, file_cluster_15: 14.15
- **Magnitude:** 9064.94 | **LOC:** 7988 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **12**; blast radius 0.669; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (84.4%), Complexity Load (formerly Cognitive Load) (80.0%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stbi__create_png_image_raw` **(Many-Argument Workhorses)** (Impact: 265.6)
    * *Intent:* // create the png data from post-deflated data
  * `stbi__bmp_load` **(Many-Argument Workhorses)** (Impact: 250.9)
  * `stbi__parse_png_file` **(Many-Argument Workhorses)** (Impact: 211.1)
    * *Intent:* #define STBI__PNG_TYPE(a,b,c,d) (((unsigned) (a) << 24) + ((unsigned) (b) << 16) + ((unsigned) (c) <...
  * `load_jpeg_image` **(Many-Argument Workhorses)** (Impact: 182.0)
  * `stbi__psd_load` **(Many-Argument Workhorses)** (Impact: 171.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 1520 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4792
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1586`, `structural_boundaries: 802`, `args: 242`, `func_start: 258`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 1752`, `dead_code: 13`, `planned_debt: 11`, `fragile_debt: 25`
* *Architecture:* `io: 7`, `import: 14`
* *Defense:* `safety: 11`, `doc: 9`, `immutability_locks: 108`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.669
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.050097
  * `Imports (Out-Degree: 0):` arm_neon.h, assert.h, emmintrin.h, intrin.h, limits.h, math.h, stdarg.h, stddef.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/PageList.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.623)
- **Top Global Matches:** file_cluster_4: 6.623, file_cluster_6: 10.221, file_cluster_12: 11.879
- **Magnitude:** 3254.56 | **LOC:** 14608 | **CtrlFlow:** 8.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **15**; blast radius 1.5; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.8%), Connectivity (formerly Api Exposure) (74.8%), Guard Balance (formerly Safety Score) (35.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (19.9%)
- **Documentation Coverage:** 22.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `writeCell` **(Many-Argument Workhorses)** (Impact: 92.2)
    * *Intent:* /// Write a cell. On error, this will not unwrite the cell but /// the cell may be incomplete (but v...
  * `diagram` **(Defensive Guards)** (Impact: 75.3)
    * *Intent:* /// ... | | /// 50 | foo | /// ... | | /// +--------+ ACTIVE /// 124 | | | 0 /// 125 |Text | | 1 ///...
  * `eraseRowBounded` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /// A variant of eraseRow that shifts only a bounded number of following /// rows up, filling the sp...
  * `scroll` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* /// Scroll the viewport. This will never create new scrollback, allocate /// pages, etc. This can on...
  * `reflowRow` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* /// Reflow the provided row in to this cursor.
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 842`, `structural_boundaries: 1108`, `args: 116`, `func_start: 116`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 4`, `state_mutation: 643`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 6`
* *Architecture:* `api: 104`, `import: 15`
* *Defense:* `safety: 2295`, `doc: 534`, `test: 208`, `cleanup: 243`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.5
  * `Choke Point (Betweenness):` 0.001457 | `Ripple Effect (Closeness):` 0.081692
  * `Imports (Out-Degree: 12):` main.zig, fastmem.zig, mach.zig, quirks.zig, tripwire.zig, builtin, color.zig, highlight.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Ghostty.App.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.866)
- **Top Global Matches:** file_cluster_4: 7.866, file_cluster_9: 11.723, file_cluster_16: 12.229
- **Magnitude:** 2625.44 | **LOC:** 2241 | **CtrlFlow:** 34.8% | **Authorship Centralization:** 66.7%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **3**; blast radius 0.383; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Mutation Surface (formerly State Flux) (64.2%), Concurrency Surface (formerly Concurrency) (62.6%), Complexity Load (formerly Cognitive Load) (50.9%)
- **Documentation Coverage:** 87.619% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `findSurface` **(Stateful Encapsulated Methods)** (Impact: 978.5)
    * *Intent:* #if os(macOS) /// Called when a callback needs access to a specific surface. This should return nil ...
  * `action` **(Many-Argument Workhorses)** (Impact: 148.2)
    * *Intent:* // MARK: Actions (macOS)
  * `commandFinished` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `promptTitle` **(Defensive Guards)** (Impact: 44.4)
  * `toggleFloatWindow` **(Stateful Encapsulated Methods)** (Impact: 35.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 40 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 40 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 56
* *State Mutation (weighted view):* 131
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 612`, `structural_boundaries: 394`, `args: 110`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 51`, `state_mutation: 51`, `unreferenced_by_name: 12`
* *Architecture:* `api: 6`, `concurrency: 16`, `import: 3`
* *Defense:* `safety: 193`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.383
  * `Choke Point (Betweenness):` 7e-06 | `Ripple Effect (Closeness):` 0.000884
  * `Imports (Out-Degree: 8):` GhosttyKit, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/stb/stb_image_resize.h` (CPP | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.734)
- **Top Global Matches:** file_cluster_6: 7.734, file_cluster_4: 8.361, file_cluster_12: 15.039
- **Magnitude:** 2027.86 | **LOC:** 2635 | **CtrlFlow:** 17.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **5**; blast radius 0.669; role: Pure Producer (Foundation)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (77.5%), Guard Balance (formerly Safety Score) (77.3%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `stbir__encode_scanline` **(Many-Argument Workhorses)** (Impact: 144.4)
  * `stbir__decode_scanline` **(Many-Argument Workhorses)** (Impact: 105.3)
    * *Intent:* #define STBIR__DECODE(type, colorspace) ((int)(type) * (STBIR_MAX_COLORSPACES) + (int)(colorspace))
  * `stbir__resize_allocated` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `stbir__normalize_downsample_coefficients` **(Many-Argument Workhorses)** (Impact: 61.9)
  * `stbir__resample_horizontal_downsample` **(Many-Argument Workhorses)** (Impact: 46.0)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 321 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1050
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 176`, `args: 84`, `func_start: 67`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 408`, `dead_code: 2`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `import: 5`
* *Defense:* `safety: 2`, `doc: 4`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.669
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.050097
  * `Imports (Out-Degree: 0):` assert.h, math.h, stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/Surface.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.263)
- **Top Global Matches:** file_cluster_4: 6.263, file_cluster_6: 10.139, file_cluster_12: 11.703
- **Magnitude:** 1947.52 | **LOC:** 6640 | **CtrlFlow:** 12.2% | **Authorship Centralization:** 45.5%
- **Blast Radius:** changing it is visible to **16** in-repo importer(s); it depends on **20**; blast radius 1.554; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (69.6%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (58.2%), Mutation Surface (formerly State Flux) (57.5%), Guard Balance (formerly Safety Score) (37.8%)
- **Documentation Coverage:** 29.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mouseButtonCallback` **(Many-Argument Workhorses)** (Impact: 154.3)
    * *Intent:* /// Called for mouse button press/release events. This will return true /// if the mouse event was c...
  * `performBindingAction` **(Many-Argument Workhorses)** (Impact: 144.9)
    * *Intent:* /// Perform a binding action. A binding is a keybinding. This function /// must be called from the G...
  * `mouseSelection` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /// Calculates the appropriate selection given pins and pixel x positions for /// the click point an...
  * `maybeHandleBinding` **(Many-Argument Workhorses)** (Impact: 69.5)
    * *Intent:* /// Maybe handles a binding for a given event and if so returns the effect. /// Returns null if the ...
  * `scrollCallback` **(Many-Argument Workhorses)** (Impact: 69.1)
    * *Intent:* /// Mouse scroll event. Negative is down, left. Positive is up, right. /// /// "Natural scrolling" i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 73 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 21
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 296
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 534`, `structural_boundaries: 572`, `args: 97`, `func_start: 97`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 1`, `state_mutation: 150`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 49`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 732`, `doc: 368`, `test: 5`, `sync_locks: 94`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.554
  * `Choke Point (Betweenness):` 0.008845 | `Ripple Effect (Closeness):` 0.074038
  * `Imports (Out-Degree: 21):` App.zig, Command.zig, apprt.zig, builtin, config.zig, main.zig, main.zig, global.zig...
  * `Imported By (In-Degree: 16):` (Excluded from Brief to save tokens)

### `src/renderer/generic.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 8.435)
- **Top Global Matches:** file_cluster_4: 8.435, file_cluster_12: 11.594, file_cluster_6: 11.883
- **Magnitude:** 1830.58 | **LOC:** 3375 | **CtrlFlow:** 13.7% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **23**; blast radius 0.774; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (91.9%), Connectivity (formerly Api Exposure) (57.6%), Guard Balance (formerly Safety Score) (48.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (17.1%)
- **Documentation Coverage:** 27.2727% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Renderer` **(Many-Argument Workhorses)** (Impact: 586.1)
    * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the in...
  * `rebuildRow` **(Many-Argument Workhorses)** (Impact: 301.4)
  * `rebuildCells` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /// Convert the terminal state to GPU cells stored in CPU memory. These /// are then synced to the G...
  * `drawFrame` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /// Draw the frame to the screen. /// /// If `sync` is true, this will synchronously block until ///...
  * `updateFrame` **(Many-Argument Workhorses)** (Impact: 59.1)
    * *Intent:* /// Update the frame data.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 71 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 301`, `structural_boundaries: 192`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 123`, `dead_code: 15`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 38`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 233`, `doc: 227`, `sync_locks: 29`, `cleanup: 66`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.774
  * `Choke Point (Betweenness):` 0.005457 | `Ripple Effect (Closeness):` 0.074335
  * `Imports (Out-Degree: 20):` Surface.zig, apprt.zig, config.zig, file_type.zig, main.zig, nerd_font_attributes.zig, input.zig, math.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/terminal/stream.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.89)
- **Top Global Matches:** file_cluster_4: 7.89, file_cluster_12: 9.029, file_cluster_15: 9.227
- **Magnitude:** 1783.72 | **LOC:** 3450 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **17**; blast radius 0.554; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (67.7%), Debt Markers (formerly Tech Debt) (55.7%), Guard Balance (formerly Safety Score) (45.8%)
- **Documentation Coverage:** 85.6% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `Stream` **(Many-Argument Workhorses)** (Impact: 575.9)
    * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T...
  * `csiDispatch` **(Many-Argument Workhorses)** (Impact: 484.2)
  * `escDispatch` **(Many-Argument Workhorses)** (Impact: 88.0)
  * `nextNonUtf8` **(Many-Argument Workhorses)** (Impact: 29.1)
    * *Intent:* /// Process the next character and call any callbacks if necessary. /// /// This assumes that we're ...
  * `nextSliceCapped` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 432`, `structural_boundaries: 164`, `args: 67`, `func_start: 67`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 55`, `planned_debt: 9`, `duplicate_logic: 18`
* *Architecture:* `api: 91`, `import: 17`
* *Defense:* `safety: 187`, `doc: 67`, `test: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.554
  * `Choke Point (Betweenness):` 0.003184 | `Ripple Effect (Closeness):` 0.077813
  * `Imports (Out-Degree: 16):` quirks.zig, main.zig, Parser.zig, UTF8Decoder.zig, ansi.zig, charsets.zig, csi.zig, device_attributes.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/config/Config.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.945)
- **Top Global Matches:** file_cluster_12: 7.945, file_cluster_15: 8.441, file_cluster_4: 8.782
- **Magnitude:** 1643.28 | **LOC:** 10888 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 43.8%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **31**; blast radius 8.926; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (70.1%), Mutation Surface (formerly State Flux) (30.8%), Guard Balance (formerly Safety Score) (25.4%)
- **Documentation Coverage:** 42.3729% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `finalize` **(Defensive Guards)** (Impact: 72.2)
    * *Intent:* /// Call this once after you are done setting configuration. This /// is idempotent but will waste m...
  * `calculate` **(Defensive Guards)** (Impact: 41.4)
  * `parseCLI` **(Many-Argument Workhorses)** (Impact: 37.3)
  * `parseCLI` **(Defensive Guards)** (Impact: 31.9)
  * `loadRecursiveFiles` **(Defensive Guards)** (Impact: 26.1)
    * *Intent:* /// Load and parse the config files that were added in the "config-file" key.
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 71 instances
* *Amplified Cascading Flux:* 48 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 180
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 443`, `structural_boundaries: 867`, `args: 149`, `func_start: 149`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 84`, `dead_code: 1`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 6`
* *Architecture:* `io: 25`, `api: 229`, `import: 34`
* *Defense:* `safety: 1276`, `doc: 3601`, `test: 127`, `cleanup: 161`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 8.926
  * `Choke Point (Betweenness):` 0.018579 | `Ripple Effect (Closeness):` 0.094832
  * `Imports (Out-Degree: 28):` build_config.zig, cli.zig, comparison.zig, main.zig, global.zig, input.zig, key_mods.zig, main.zig...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/terminal/Terminal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.561)
- **Top Global Matches:** file_cluster_4: 7.561, file_cluster_12: 10.437, file_cluster_15: 10.853
- **Magnitude:** 1413.46 | **LOC:** 13090 | **CtrlFlow:** 5.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **18** in-repo importer(s); it depends on **24**; blast radius 1.844; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (71.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (67.0%), Mutation Surface (formerly State Flux) (34.4%)
- **Documentation Coverage:** 9.0164% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `print` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `printCell` **(Many-Argument Workhorses)** (Impact: 54.4)
  * `printAttributes` **(Defensive Guards)** (Impact: 38.6)
    * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// //...
  * `cursorLeft` **(Many-Argument Workhorses)** (Impact: 36.1)
    * *Intent:* /// Move the cursor to the left amount cells. If amount is 0, adjust it to 1.
  * `insertLines` **(Many-Argument Workhorses)** (Impact: 35.2)
    * *Intent:* /// /// This unsets the pending wrap state without wrapping. If the current cursor /// position is o...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 6 instances
* *Mitigated Memory Allocs:* 284 instances
* *Amplified Cascading Flux:* 109 instances
* *Api Near Db Sink:* 1 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 414
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 1201`, `args: 63`, `func_start: 63`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 6`, `state_mutation: 196`, `dead_code: 8`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 70`, `import: 24`
* *Defense:* `safety: 3390`, `doc: 318`, `test: 372`, `cleanup: 671`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.844
  * `Choke Point (Betweenness):` 0.004621 | `Ripple Effect (Closeness):` 0.082174
  * `Imports (Out-Degree: 21):` quirks.zig, main.zig, Screen.zig, ScreenSet.zig, Tabstops.zig, ansi.zig, charsets.zig, color.zig...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/surface.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.85)
- **Top Global Matches:** file_cluster_12: 6.85, file_cluster_15: 7.772, file_cluster_16: 9.294
- **Magnitude:** 1373.24 | **LOC:** 4041 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 44.4%
- **Blast Radius:** changing it is visible to **10** in-repo importer(s); it depends on **36**; blast radius 1.158; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (90.5%), Mutation Surface (formerly State Flux) (64.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (51.0%), Guard Balance (formerly Safety Score) (45.4%)
- **Documentation Coverage:** 63.3166% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `keyEvent` **(Many-Argument Workhorses)** (Impact: 74.7)
    * *Intent:* /// /// We set some state to note we're in a key event (self.in_keyevent) /// because some of the in...
  * `dtDrop` **(Many-Argument Workhorses)** (Impact: 36.1)
  * `filterSnapPaths` **(Defensive Guards)** (Impact: 31.2)
    * *Intent:* /// Filter out environment variables that start with forbidden prefixes.
  * `set` **(Many-Argument Workhorses)** (Impact: 31.2)
    * *Intent:* /// Set the clipboard contents.
  * `commandFinished` **(Defensive Guards)** (Impact: 27.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 64 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 298`, `structural_boundaries: 284`, `args: 132`, `func_start: 132`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 1`, `state_mutation: 90`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `api: 160`, `import: 36`
* *Defense:* `safety: 281`, `doc: 198`, `test: 5`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.158
  * `Choke Point (Betweenness):` 0.007535 | `Ripple Effect (Closeness):` 0.054249
  * `Imports (Out-Degree: 32):` Surface.zig, apprt.zig, build_config.zig, config.zig, main.zig, main.zig, input.zig, i18n.zig...
  * `Imported By (In-Degree: 10):` (Excluded from Brief to save tokens)

### `src/terminal/Screen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.53)
- **Top Global Matches:** file_cluster_4: 6.53, file_cluster_6: 10.174, file_cluster_15: 12.132
- **Magnitude:** 1361.76 | **LOC:** 10353 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **12** in-repo importer(s); it depends on **21**; blast radius 1.526; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (70.7%), Mutation Surface (formerly State Flux) (48.5%), Guard Balance (formerly Safety Score) (28.8%), Debt Markers (formerly Tech Debt) (9.6%)
- **Documentation Coverage:** 17.3554% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `selectLine` **(Many-Argument Workhorses)** (Impact: 54.8)
    * *Intent:* /// Select the line under the given point. This will select across soft-wrapped /// lines and will o...
  * `clearCells` **(Many-Argument Workhorses)** (Impact: 53.7)
    * *Intent:* /// Clear the cells with the blank cell. /// /// This takes care to handle cleaning up graphemes and...
  * `testWriteString` **(Many-Argument Workhorses)** (Impact: 46.8)
    * *Intent:* /// This is basically a really jank version of Terminal.printString. We /// have to reimplement it h...
  * `clone` **(Many-Argument Workhorses)** (Impact: 42.1)
    * *Intent:* /// is only for read-only operations, it is better to not have any /// hyperlink state. Note that al...
  * `promptClickLine` **(Many-Argument Workhorses)** (Impact: 39.4)
    * *Intent:* /// Determine the inputs required to move from the cursor to the given /// click location. If the cu...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 104 instances
* *State Mutation (weighted view):* 420
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 309`, `structural_boundaries: 1004`, `args: 63`, `func_start: 63`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 212`, `dead_code: 16`, `planned_debt: 4`, `fragile_debt: 11`
* *Architecture:* `api: 74`, `import: 21`
* *Defense:* `safety: 1775`, `doc: 383`, `test: 184`, `cleanup: 513`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.526
  * `Choke Point (Betweenness):` 0.001285 | `Ripple Effect (Closeness):` 0.081632
  * `Imports (Out-Degree: 19):` fastmem.zig, quirks.zig, tripwire.zig, main.zig, PageList.zig, Selection.zig, StringMap.zig, ansi.zig...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.609)
- **Top Global Matches:** file_cluster_4: 6.609, file_cluster_15: 8.712, file_cluster_16: 8.862
- **Magnitude:** 1349.6 | **LOC:** 2352 | **CtrlFlow:** 29.4% | **Authorship Centralization:** 42.9%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Concurrency Surface (formerly Concurrency) (96.6%), Debt Markers (formerly Tech Debt) (95.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 88.0282% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 41.6)
  * `performKeyEquivalent` **(Compute Cores)** (Impact: 37.2)
    * *Intent:* /// Special case handling for some control keys
  * `keyDown` **(Compute Cores)** (Impact: 34.3)
  * `setCursorShape` **(Compute Cores)** (Impact: 28.1)
  * `flagsChanged` **(Compute Cores)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 111 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 104
* *State Mutation (weighted view):* 381
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 422`, `args: 142`, `func_start: 103`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 159`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `io: 1`, `api: 50`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 133`, `doc: 81`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` AppKit, Combine, CoreText, GhosttyKit, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `macos/Sources/Features/Terminal/BaseTerminalController.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.271)
- **Top Global Matches:** file_cluster_4: 7.271, file_cluster_16: 9.555, file_cluster_15: 9.892
- **Magnitude:** 1005.78 | **LOC:** 1549 | **CtrlFlow:** 35.3% | **Authorship Centralization:** 100.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **4**; blast radius 0.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.6%), Debt Markers (formerly Tech Debt) (99.5%), Concurrency Surface (formerly Concurrency) (86.6%), Guard Balance (formerly Safety Score) (44.9%)
- **Documentation Coverage:** 88.0795% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `splitDidDrop` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `ghosttyDidResizeSplit` **(Defensive Guards)** (Impact: 27.0)
  * `clipboardConfirmationComplete` **(Defensive Guards)** (Impact: 25.7)
  * `ghosttyDidFocusSplit` **(Defensive Guards)** (Impact: 25.6)
  * `onConfirmClipboardRequest` **(Defensive Guards)** (Impact: 25.5)
    * *Intent:* // MARK: Clipboard Confirmation
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 60 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 199
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 356`, `structural_boundaries: 271`, `args: 108`, `func_start: 91`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 79`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 48`
* *Architecture:* `api: 47`, `concurrency: 15`, `import: 4`
* *Defense:* `safety: 143`, `doc: 91`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` Cocoa, Combine, GhosttyKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/page.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.439)
- **Top Global Matches:** file_cluster_12: 8.439, file_cluster_4: 8.672, file_cluster_15: 10.783
- **Magnitude:** 915.58 | **LOC:** 3919 | **CtrlFlow:** 9.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **13** in-repo importer(s); it depends on **12**; blast radius 1.614; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (88.9%), Connectivity (formerly Api Exposure) (80.7%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (42.2%)
- **Documentation Coverage:** 10.3448% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `verifyIntegrity` **(Many-Argument Workhorses)** (Impact: 82.4)
    * *Intent:* /// Verifies the integrity of the page data. This is not fast, /// but it is useful for assertions, ...
  * `clonePartialRowFrom` **(Many-Argument Workhorses)** (Impact: 73.1)
    * *Intent:* /// Clone a single row from another page into this page, supporting /// partial copy. cloneRowFrom c...
  * `clearCells` **(Many-Argument Workhorses)** (Impact: 50.8)
    * *Intent:* /// Clear the cells in the given row. This will reclaim memory used /// by graphemes and styles. Not...
  * `moveCells` **(Many-Argument Workhorses)** (Impact: 40.3)
    * *Intent:* /// Move a cell from one location to another. This will replace the /// previous contents with a bla...
  * `exactRowCapacity` **(Many-Argument Workhorses)** (Impact: 28.8)
    * *Intent:* /// Compute the exact capacity required to store a range of rows from /// this page. /// /// The ret...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 81 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 294
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 280`, `args: 57`, `func_start: 57`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 1`, `state_mutation: 132`, `dead_code: 4`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 78`, `import: 12`
* *Defense:* `safety: 405`, `doc: 374`, `test: 48`, `cleanup: 71`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.614
  * `Choke Point (Betweenness):` 0.001369 | `Ripple Effect (Closeness):` 0.085912
  * `Imports (Out-Degree: 9):` fastmem.zig, quirks.zig, bitmap_allocator.zig, builtin, color.zig, hash_map.zig, hyperlink.zig, kitty.zig...
  * `Imported By (In-Degree: 13):` (Excluded from Brief to save tokens)

### `macos/Sources/Features/Terminal/TerminalController.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.32)
- **Top Global Matches:** file_cluster_4: 6.32, file_cluster_6: 10.894, file_cluster_9: 11.481
- **Magnitude:** 905.32 | **LOC:** 1665 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 85.7%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **5**; blast radius 1.07; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (96.2%), Debt Markers (formerly Tech Debt) (62.2%), Concurrency Surface (formerly Concurrency) (58.5%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.4%)
- **Documentation Coverage:** 87.6404% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newTab` **(Many-Argument Workhorses)** (Impact: 58.1)
  * `onGotoTab` **(Defensive Guards)** (Impact: 42.1)
  * `newWindow` **(Many-Argument Workhorses)** (Impact: 36.0)
    * *Intent:* /// The "new window" action.
  * `registerUndoForCloseWindow` **(Defensive Guards)** (Impact: 35.4)
    * *Intent:* /// Registers undo for closing window(s), handling both single windows and tab groups.
  * `onMoveTab` **(Defensive Guards)** (Impact: 34.2)
    * *Intent:* // MARK: - Notifications
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 155
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 402`, `structural_boundaries: 240`, `args: 97`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 67`, `fragile_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `api: 19`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 160`, `doc: 40`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.07
  * `Choke Point (Betweenness):` 4.2e-05 | `Ripple Effect (Closeness):` 0.005305
  * `Imports (Out-Degree: 4):` Cocoa, Combine, Foundation, GhosttyKit, SwiftUI
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/application.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 5.941)
- **Top Global Matches:** file_cluster_12: 5.941, file_cluster_15: 7.612, file_cluster_16: 9.069
- **Magnitude:** 876.74 | **LOC:** 2957 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 55.6%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **38**; blast radius 1.493; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (82.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (57.0%), Guard Balance (formerly Safety Score) (43.2%), Mutation Surface (formerly State Flux) (18.4%)
- **Documentation Coverage:** 70.8791% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `glibLogWriterFunction` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* /// Function used to funnel GLib/GObject/GTK log messages into Zig's logging /// system rather than ...
  * `actionNewWindow` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* /// Handle `app.new-window` and `app.new-window-command` GTK actions
  * `new` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* /// Creates a new Application instance. /// /// This does a lot more work than a typical class insta...
  * `run` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /// Run the application. This is a replacement for `gio.Application.run` /// because we want more ti...
  * `setGtkEnv` **(Defensive Guards)** (Impact: 20.7)
    * *Intent:* /// This sets various GTK-related environment variables as necessary /// given the runtime environme...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 303`, `args: 108`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 20`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 82`, `import: 42`
* *Defense:* `safety: 216`, `doc: 124`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.493
  * `Choke Point (Betweenness):` 0.005064 | `Ripple Effect (Closeness):` 0.054382
  * `Imports (Out-Degree: 31):` App.zig, Surface.zig, apprt.zig, build_config.zig, config.zig, global.zig, input.zig, main.zig...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `src/datastruct/split_tree.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.515)
- **Top Global Matches:** file_cluster_4: 7.515, file_cluster_15: 8.73, file_cluster_12: 8.779
- **Magnitude:** 789.0 | **LOC:** 2368 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **5**; blast radius 0.509; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (64.0%), Mutation Surface (formerly State Flux) (50.5%), Guard Balance (formerly Safety Score) (37.3%), Debt Markers (formerly Tech Debt) (8.6%)
- **Documentation Coverage:** 44.186% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `SplitTree` **(Many-Argument Workhorses)** (Impact: 235.5)
    * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(...
  * `formatDiagram` **(Many-Argument Workhorses)** (Impact: 44.6)
  * `split` **(Many-Argument Workhorses)** (Impact: 27.1)
    * *Intent:* /// Insert another tree into this tree at the given node in the /// specified direction. The other t...
  * `nearest` **(Many-Argument Workhorses)** (Impact: 26.8)
    * *Intent:* /// Returns the nearest leaf node (view) in the given direction. /// This does not handle wrapping a...
  * `findParentSplit` **(Many-Argument Workhorses)** (Impact: 21.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 29 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 107
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 206`, `structural_boundaries: 377`, `args: 46`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 49`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 283`, `doc: 155`, `test: 17`, `cleanup: 107`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.509
  * `Choke Point (Betweenness):` 0.000632 | `Ripple Effect (Closeness):` 0.067044
  * `Imports (Out-Degree: 2):` build_config.zig, quirks.zig, glib, gobject, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `macos/Sources/App/macOS/AppDelegate.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.611)
- **Top Global Matches:** file_cluster_4: 7.611, file_cluster_16: 9.159, file_cluster_15: 9.513
- **Magnitude:** 777.96 | **LOC:** 1404 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 50.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **6**; blast radius 0.336; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (99.5%), Test Surface (formerly Verification) (80.0%), Concurrency Surface (formerly Concurrency) (63.0%), Guard Balance (formerly Safety Score) (54.5%)
- **Documentation Coverage:** 83.1579% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setupMenuImages` **(Compute Cores)** (Impact: 41.1)
    * *Intent:* /// Setup all the images for our menu items.
  * `ghosttyConfigDidChange` **(I/O & Config Routines)** (Impact: 35.5)
  * `application` **(Many-Argument Workhorses)** (Impact: 26.2)
  * `applicationShouldTerminate` **(Compute Cores)** (Impact: 25.5)
  * `applicationDidFinishLaunching` **(I/O & Config Routines)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 51 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 179
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 230`, `args: 82`, `func_start: 63`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 77`, `unreferenced_by_name: 20`
* *Architecture:* `io: 13`, `api: 83`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 47`, `doc: 43`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.336
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` AppKit, GhosttyKit, OSLog, Sparkle, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/Binding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 7.876)
- **Top Global Matches:** file_cluster_12: 7.876, file_cluster_15: 7.942, file_cluster_4: 8.007
- **Magnitude:** 774.32 | **LOC:** 4848 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **9**; blast radius 1.691; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (72.2%), Guard Balance (formerly Safety Score) (29.6%), Mutation Surface (formerly State Flux) (23.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (12.2%)
- **Documentation Coverage:** 34.2466% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `parseAndPutRecurse` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* /// Returns the set that was ultimately updated if a binding was /// added. Unbind does not return a...
  * `parse` **(Defensive Guards)** (Impact: 38.8)
    * *Intent:* /// Parse a single trigger. The input is expected to be ONLY the trigger /// (i.e. in the sequence `...
  * `lessThan` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /// Returns true if lhs should be sorted before rhs
  * `putFlags` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /// Add a binding to the set with explicit flags.
  * `parseFlags` **(Compute Cores)** (Impact: 23.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 28 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 203`, `structural_boundaries: 352`, `args: 64`, `func_start: 64`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 43`, `planned_debt: 2`
* *Architecture:* `api: 90`, `import: 12`
* *Defense:* `safety: 661`, `doc: 667`, `test: 85`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.691
  * `Choke Point (Betweenness):` 0.001507 | `Ripple Effect (Closeness):` 0.071704
  * `Imports (Out-Degree: 6):` build_config.zig, formatter.zig, comparison.zig, quirks.zig, gobject, key.zig, key_mods.zig, std...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/terminal/formatter.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.605)
- **Top Global Matches:** file_cluster_6: 7.605, file_cluster_4: 10.679, file_cluster_8: 16.648
- **Magnitude:** 770.72 | **LOC:** 6280 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 1.033; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (61.0%), Mutation Surface (formerly State Flux) (50.2%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (44.3%), Guard Balance (formerly Safety Score) (32.9%)
- **Documentation Coverage:** 75.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `formatWithState` **(Many-Argument Workhorses)** (Impact: 155.9)
  * `format` **(Many-Argument Workhorses)** (Impact: 62.4)
  * `format` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `format` **(Defensive Guards)** (Impact: 23.6)
  * `writeCodepointWithReplacement` **(Defensive Guards)** (Impact: 16.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 263
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 278`, `structural_boundaries: 1025`, `args: 19`, `func_start: 19`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 203`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 33`, `import: 18`
* *Defense:* `safety: 971`, `doc: 166`, `test: 100`, `cleanup: 399`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.033
  * `Choke Point (Betweenness):` 0.000727 | `Ripple Effect (Closeness):` 0.083404
  * `Imports (Out-Degree: 15):` quirks.zig, PageList.zig, Screen.zig, Selection.zig, Terminal.zig, charsets.zig, color.zig, hyperlink.zig...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/apprt/embedded.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 6.713)
- **Top Global Matches:** file_cluster_12: 6.713, file_cluster_15: 9.009, file_cluster_7: 9.711
- **Magnitude:** 764.02 | **LOC:** 2232 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Blast Radius:** changing it is visible to **5** in-repo importer(s); it depends on **16**; blast radius 1.173; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Connectivity (formerly Api Exposure) (92.6%), Guard Balance (formerly Safety Score) (42.8%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (30.9%), Mutation Surface (formerly State Flux) (28.3%)
- **Documentation Coverage:** 50.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 32.5)
  * `performPreAction` **(Many-Argument Workhorses)** (Impact: 19.6)
  * `pin` **(Defensive Guards)** (Impact: 15.9)
  * `init` **(Defensive Guards)** (Impact: 14.8)
    * *Intent:* /// Initialize a Platform a tag and configuration from the C ABI.
  * `keyEvent` **(Defensive Guards)** (Impact: 13.3)
    * *Intent:* /// See CoreApp.keyEvent.
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 116`, `structural_boundaries: 182`, `args: 148`, `func_start: 142`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 32`
* *Architecture:* `io: 2`, `api: 142`, `import: 16`
* *Defense:* `safety: 186`, `doc: 185`, `sync_locks: 8`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.173
  * `Choke Point (Betweenness):` 0.004644 | `Ripple Effect (Closeness):` 0.077596
  * `Imports (Out-Degree: 15):` App.zig, Surface.zig, apprt.zig, config.zig, main.zig, global.zig, input.zig, main.zig...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/terminal/hash_map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Centroid distance: 8.24)
- **Top Global Matches:** file_cluster_12: 8.24, file_cluster_5: 8.446, file_cluster_7: 10.432
- **Magnitude:** 751.04 | **LOC:** 1541 | **CtrlFlow:** 10.2% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **3**; blast radius 0.806; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (97.8%), Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (76.9%), Guard Balance (formerly Safety Score) (46.4%)
- **Documentation Coverage:** 65.1685% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HashMapUnmanaged` **(Many-Argument Workhorses)** (Impact: 175.1)
    * *Intent:* /// Fork of stdlib.HashMap as of Zig 0.12 modified to use offsets for /// the key/values pointer. Th...
  * `getOrPutAssumeCapacityAdapted` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `getIndex` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /// Find the index containing the data for the given key. /// Whether this function returns null is ...
  * `next` **(Compute Cores)** (Impact: 6.8)
  * `init` **(Type Conversions)** (Impact: 6.1)
    * *Intent:* /// Initialize a hash map with a given capacity and a buffer. The /// buffer must fit within the siz...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 172`, `args: 80`, `func_start: 80`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 70`, `planned_debt: 1`
* *Architecture:* `api: 82`, `import: 5`
* *Defense:* `safety: 171`, `doc: 106`, `test: 24`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.806
  * `Choke Point (Betweenness):` 0.000137 | `Ripple Effect (Closeness):` 0.08098
  * `Imports (Out-Degree: 2):` quirks.zig, size.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 6.194)
- **Top Global Matches:** file_cluster_15: 6.194, file_cluster_12: 6.988, file_cluster_16: 8.066
- **Magnitude:** 615.18 | **LOC:** 2112 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 60.0%
- **Blast Radius:** changing it is visible to **9** in-repo importer(s); it depends on **29**; blast radius 1.325; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Test Surface (formerly Verification) (80.0%), Connectivity (formerly Api Exposure) (75.7%), Guard Balance (formerly Safety Score) (45.7%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (39.5%)
- **Documentation Coverage:** 65.1786% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `newTabPage` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `selectTab` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* /// Select the tab as requested. Returns true if the tab selection /// changed.
  * `syncAppearance` **(I/O & Config Routines)** (Impact: 18.5)
    * *Intent:* /// Updates various appearance properties. This should always be safe /// to call multiple times. Th...
  * `moveTab` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* /// Move the tab containing the given surface by the given amount. /// Returns if this affected any ...
  * `actionRingBell` **(Defensive Guards)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 150`, `structural_boundaries: 117`, `args: 95`, `func_start: 95`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 7`, `planned_debt: 7`
* *Architecture:* `api: 52`, `import: 29`
* *Defense:* `safety: 86`, `doc: 66`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.325
  * `Choke Point (Betweenness):` 0.002851 | `Ripple Effect (Closeness):` 0.054276
  * `Imports (Out-Degree: 22):` Surface.zig, apprt.zig, build_config.zig, config.zig, input.zig, main.zig, quirks.zig, adw_version.zig...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `macos/Sources/Features/Splits/SplitTree.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.876)
- **Top Global Matches:** file_cluster_4: 6.876, file_cluster_15: 7.775, file_cluster_16: 8.546
- **Magnitude:** 599.66 | **LOC:** 1414 | **CtrlFlow:** 29.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **2**; blast radius 0.431; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (94.7%), Guard Balance (formerly Safety Score) (49.7%), Debt Markers (formerly Tech Debt) (17.4%), Complexity Load (formerly Cognitive Load) (16.2%)
- **Documentation Coverage:** 26.7857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `resizing` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* /// operation. For up/down resizing, it finds the nearest parent vertical split and adjusts /// its ...
  * `focusTarget` **(Defensive Guards)** (Impact: 39.2)
    * *Intent:* /// Find the next view to focus based on the current focused node and direction
  * `slots` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* /// Distance is calculated from the top-left corners of the bounds, prioritizing nodes that are /// ...
  * `inserting` **(Many-Argument Workhorses)** (Impact: 19.9)
    * *Intent:* /// Inserts a new view into the split tree by creating a split at the location of an existing view. ...
  * `remove` **(Compute Cores)** (Impact: 18.8)
    * *Intent:* /// Remove a node from the tree. Returns the modified tree, or nil if removing /// the node results ...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 34 instances
* *State Mutation (weighted view):* 112
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 256`, `args: 70`, `func_start: 54`, `class_start: 31`
* *Risk/State:* `state_mutation: 44`, `unreferenced_by_name: 8`
* *Architecture:* `import: 2`
* *Defense:* `safety: 33`, `doc: 253`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.431
  * `Choke Point (Betweenness):` 3e-06 | `Ripple Effect (Closeness):` 0.001768
  * `Imports (Out-Degree: 3):` AppKit, Combine
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/stream_terminal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Centroid distance: 7.752)
- **Top Global Matches:** file_cluster_15: 7.752, file_cluster_12: 8.279, file_cluster_16: 9.248
- **Magnitude:** 568.2 | **LOC:** 2072 | **CtrlFlow:** 6.5% | **Authorship Centralization:** 100.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 0.606; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Debt Markers (formerly Tech Debt) (99.2%), Mutation Surface (formerly State Flux) (97.4%), Historical Churn (predictive layer, promotion pending #2987) (formerly Churn) (59.3%), Guard Balance (formerly Safety Score) (35.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `setMode` **(Many-Argument Workhorses)** (Impact: 51.9)
  * `vtFallible` **(Many-Argument Workhorses)** (Impact: 31.5)
  * `colorOperation` **(Many-Argument Workhorses)** (Impact: 21.6)
  * `kittyColorOperation` **(Defensive Guards)** (Impact: 17.3)
  * `deviceStatus` **(Defensive Guards)** (Impact: 13.8)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 19 instances
* *Mitigated Memory Allocs:* 39 instances
* *Amplified Cascading Flux:* 56 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 234
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 100`, `structural_boundaries: 388`, `args: 68`, `func_start: 60`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 9`, `high_risk_execution: 19`, `state_mutation: 122`, `planned_debt: 1`, `duplicate_logic: 30`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 324`, `doc: 41`, `test: 62`, `cleanup: 169`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.606
  * `Choke Point (Betweenness):` 0.004119 | `Ripple Effect (Closeness):` 0.079083
  * `Imports (Out-Degree: 11):` Screen.zig, Terminal.zig, csi.zig, device_attributes.zig, device_status.zig, color.zig, modes.zig, color.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/apprt/gtk/gsettings.zig` (ZIG) | Magnitude: 34.16 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 59, core_var_decl: 22, design_snake_case: 19, safety: 17
- `macos/Sources/Features/Settings/ConfigurationErrorsView.swift` (SWIFT) | Magnitude: 5.24 | Delta: **0.115** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 47, ui_framework: 12, structural_boundaries: 9, args: 3

### Mixed-Responsibility Refactoring Targets for: file_cluster_10
- `macos/Sources/Features/About/AboutViewModel.swift` (SWIFT) | Magnitude: 14.48 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 31, structural_boundaries: 9, core_var_decl: 7, events: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `macos/Sources/Ghostty/Surface View/SurfaceView_UIKit.swift` (SWIFT) | Magnitude: 48.66 | Delta: **0.034** (centroid distance) | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 64, structural_boundaries: 37, branch: 19, core_var_decl: 16
- `macos/Sources/Helpers/Extensions/Transferable+Extension.swift` (SWIFT) | Magnitude: 19.28 | Delta: **0.057** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 32, structural_boundaries: 12, core_var_decl: 8, branch: 5
- `.github/workflows/test.yml` (YAML) | Magnitude: 188.58 | Delta: **0.078** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 1355, structural_boundaries: 197, args: 178, import: 158
- `.github/workflows/release-tag.yml` (YAML) | Magnitude: 58.74 | Delta: **0.119** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 323, globals: 61, structural_boundaries: 29, args: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `pkg/macos/foundation/array.zig` (ZIG) | Magnitude: 64.72 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 136, pointers: 31, core_var_decl: 22, args: 19
- `src/apprt/gtk/class/clipboard_confirmation_dialog.zig` (ZIG) | Magnitude: 97.1 | Delta: **0.031** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 275, core_var_decl: 60, design_snake_case: 48, api: 32
- `src/terminal/c/osc.zig` (ZIG) | Magnitude: 50.16 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 78, core_var_decl: 28, design_snake_case: 20, structural_boundaries: 16
- `src/apprt/gtk/class/dialog.zig` (ZIG) | Magnitude: 33.98 | Delta: **0.062** (centroid distance) | Secondary Pull: `file_cluster_5`
  * Top Architectural Signatures: indent_spaces: 55, core_var_decl: 25, design_snake_case: 16, api: 13
- `src/input/Binding.zig` (ZIG) | Magnitude: 774.32 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 2912, doc: 667, safety: 661, core_var_decl: 526

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `macos/Sources/Features/About/AboutController.swift` (SWIFT) | Magnitude: 26.86 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 28, structural_boundaries: 13, branch: 7, args: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_14
- `pkg/macos/text/run.zig` (ZIG) | Magnitude: 47.88 | Delta: **0.003** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 93, core_var_decl: 23, structural_boundaries: 22, safety_bypasses: 20
- `pkg/fontconfig/font_set.zig` (ZIG) | Magnitude: 18.7 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 27, core_var_decl: 9, pointers: 8, structural_boundaries: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `pkg/glslang/test.zig` (ZIG) | Magnitude: 3.32 | Delta: **0.01** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: structural_boundaries: 2, doc: 2, globals: 2, indent_spaces: 2
- `src/terminal/osc/parsers/mouse_shape.zig` (ZIG) | Magnitude: 14.72 | Delta: **0.042** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 23, core_var_decl: 10, design_snake_case: 7, structural_boundaries: 4
- `pkg/oniguruma/testing.zig` (ZIG) | Magnitude: 3.34 | Delta: **0.056** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 6, globals: 3, core_var_decl: 3, structural_boundaries: 2
- `src/tripwire.zig` (ZIG) | Magnitude: 82.02 | Delta: **0.074** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 116, indent_spaces: 105, core_var_decl: 26, design_snake_case: 20
- `macos/Sources/Features/Command Palette/CommandPalette.swift` (SWIFT) | Magnitude: 115.44 | Delta: **0.079** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 329, branch: 96, structural_boundaries: 56, ui_framework: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `macos/Sources/Ghostty/Surface View/SurfaceView.swift` (SWIFT) | Magnitude: 297.42 | Delta: **0.041** (centroid distance) | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 956, structural_boundaries: 211, branch: 154, ui_framework: 130

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `pkg/fontconfig/main.zig` (ZIG) | Magnitude: 39.84 | Delta: **0.063** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 37, globals: 36, api: 24, design_pascal_case: 18
- `pkg/opengl/main.zig` (ZIG) | Magnitude: 42.56 | Delta: **0.076** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 28, core_var_decl: 28, api: 27, import: 14
- `src/input.zig` (ZIG) | Magnitude: 43.82 | Delta: **0.106** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 36, globals: 35, api: 28, design_pascal_case: 20
- `src/terminal/osc/parsers.zig` (ZIG) | Magnitude: 30.38 | Delta: **0.114** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: globals: 16, import: 16, core_var_decl: 16, design_snake_case: 16
- `src/renderer.zig` (ZIG) | Magnitude: 37.9 | Delta: **0.127** (centroid distance) | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: core_var_decl: 33, globals: 26, api: 22, design_pascal_case: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `src/config.zig` (ZIG) | Magnitude: 57.98 | Delta: **0.024** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 46, core_var_decl: 46, api: 42, design_pascal_case: 34
- `pkg/macos/text.zig` (ZIG) | Magnitude: 37.72 | Delta: **0.027** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: globals: 33, core_var_decl: 33, api: 22, design_pascal_case: 18
- `.github/workflows/clean-artifacts.yml` (YAML) | Magnitude: 15.32 | Delta: **0.029** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 13, args: 3, structural_boundaries: 2, events: 2
- `pkg/afl++/build.zig` (ZIG) | Magnitude: 11.54 | Delta: **0.044** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 33, doc: 8, core_var_decl: 7, pointers: 5
- `src/os/kernel_info.zig` (ZIG) | Magnitude: 4.78 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 13, structural_boundaries: 10, core_var_decl: 7, design_snake_case: 7

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/font/sprite/draw/box.zig` (ZIG) | Magnitude: 210.22 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 590, core_var_decl: 89, design_snake_case: 72, explicit_casts: 66
- `src/datastruct/circ_buf.zig` (ZIG) | Magnitude: 248.26 | Delta: **0.081** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: indent_spaces: 550, safety: 182, core_var_decl: 137, design_snake_case: 106
- `src/terminal/ref_counted_set.zig` (ZIG) | Magnitude: 407.34 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 349, doc: 141, core_var_decl: 79, design_snake_case: 56
- `src/input/mouse_encode.zig` (ZIG) | Magnitude: 89.8 | Delta: **0.191** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 534, structural_boundaries: 81, safety: 81, doc: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_5
- `pkg/macos/foundation/number.zig` (ZIG) | Magnitude: 20.52 | Delta: **0.019** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 61, core_var_decl: 27, design_snake_case: 24, structural_boundaries: 6
- `src/font/sprite/canvas.zig` (ZIG) | Magnitude: 191.22 | Delta: **0.108** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 380, core_var_decl: 57, design_snake_case: 54, structural_boundaries: 33

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `macos/Sources/Helpers/PermissionRequest.swift` (SWIFT) | Magnitude: 163.02 | Delta: **0.066** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 137, branch: 49, doc: 37, structural_boundaries: 29

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/cli/boo.zig` (ZIG) | Magnitude: 95.44 | Delta: **0.083** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: indent_spaces: 159, core_var_decl: 43, structural_boundaries: 33, design_snake_case: 32
- `include/ghostty/vt/grid_ref.h` (CPP) | Magnitude: 15.6 | Delta: **0.117** (centroid distance) | Secondary Pull: `file_cluster_12`
  * Top Architectural Signatures: pointers: 13, indent_spaces: 10, doc: 8, import: 5

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `.github/workflows/test.yml` -> Churn: **87.22%** | Cog Load: 5.8904% | Debt: 63.0723%
- `src/terminal/c/terminal.zig` -> Churn: **87.22%** | Cog Load: 7.5274% | Debt: 59.3409%
- `src/terminal/stream_terminal.zig` -> Churn: **59.31%** | Cog Load: 20.6958% | Debt: 99.1889%
- `macos/Sources/Features/Terminal/TerminalController.swift` -> Churn: **57.39%** | Cog Load: 33.8704% | Debt: 62.1819%
- `src/shell-integration/bash/ghostty.bash` -> Churn: **54.79%** | Cog Load: 75.6001% | Debt: 0.0%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/terminal/PageList.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 3254.56
- `src/renderer/generic.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1830.58
- `src/terminal/stream.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1783.72
- `src/terminal/Terminal.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1413.46
- `macos/Sources/Features/Terminal/BaseTerminalController.swift` -> **Tim Culverhouse** (100.0% isolated ownership) | Magnitude: 1005.78

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/font/discovery.zig` -> **Severity: 1.017** (Bridge: 0.0131 * Flux: 77.403%)
- `src/global.zig` -> **Severity: 0.721** (Bridge: 0.0075 * Flux: 95.9835%)
- `src/config/Config.zig` -> **Severity: 0.572** (Bridge: 0.0186 * Flux: 30.8096%)
- `src/Surface.zig` -> **Severity: 0.509** (Bridge: 0.0088 * Flux: 57.5073%)
- `src/renderer/generic.zig` -> **Severity: 0.502** (Bridge: 0.0055 * Flux: 91.9187%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/quirks.zig` -> **Severity: 7.457** (Embedded: 0.1563 * Error Risk: 47.7159%)
- `pkg/macos/foundation/string.zig` -> **Severity: 6.952** (Embedded: 0.0869 * Error Risk: 80.0%)
- `pkg/macos/text/font.zig` -> **Severity: 6.712** (Embedded: 0.0839 * Error Risk: 80.0%)
- `src/lib/allocator.zig` -> **Severity: 6.257** (Embedded: 0.0782 * Error Risk: 80.0%)
- `src/terminal/device_status.zig` -> **Severity: 5.925** (Embedded: 0.0785 * Error Risk: 75.4545%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/quirks.zig` -> **Severity: 1099.432** (Blast Radius: 32.983 * Doc Risk: 33.3333%)
- `src/lib/allocator/convenience.zig` -> **Severity: 522.5** (Blast Radius: 5.225 * Doc Risk: 100.0%)
- `macos/Sources/Helpers/Extensions/String+Extension.swift` -> **Severity: 495.7** (Blast Radius: 4.957 * Doc Risk: 100.0%)
- `src/config/Config.zig` -> **Severity: 378.221** (Blast Radius: 8.926 * Doc Risk: 42.3729%)
- `src/lib/allocator.zig` -> **Severity: 325.715** (Blast Radius: 5.7 * Doc Risk: 57.1429%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`memory_alloc`:** 1043 literal sites + 44 sites through wrappers = 1087
- **`panics_and_aborts`:** 513 literal sites + 2 sites through wrappers = 515

- `stbi__malloc` (function, memory_alloc, via STBI_MALLOC): 20 call sites in 1 files -- `src/stb/stb_image.h`
- `stbi__malloc_mad3` (function, memory_alloc, via stbi__malloc): 10 call sites in 1 files -- `src/stb/stb_image.h`
- `STBI_REALLOC_SIZED` (macro, memory_alloc, via STBI_REALLOC): 4 call sites in 1 files -- `src/stb/stb_image.h`
- `stbi__malloc_mad2` (function, memory_alloc, via stbi__malloc): 4 call sites in 1 files -- `src/stb/stb_image.h`
- `stbi__malloc_mad4` (function, memory_alloc, via stbi__malloc): 3 call sites in 1 files -- `src/stb/stb_image.h`
- `STBIR_MALLOC` (macro, memory_alloc, primitive): 1 call sites in 1 files -- `src/stb/stb_image_resize.h`
- `STBI_MALLOC` (macro, memory_alloc, primitive): 1 call sites in 1 files -- `src/stb/stb_image.h`
- `fmtScope` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/apprt/gtk/cgroup.zig`
- `formatToken` (function, panics_and_aborts, primitive): 1 call sites in 1 files -- `src/apprt/gtk/portal.zig`
- `stbi__jpeg_info` (function, memory_alloc, via stbi__malloc): 1 call sites in 1 files -- `src/stb/stb_image.h`

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 24156 call pairs -- scoped 22.9%, unique 0.6%, ambiguous 22.2%, external 54.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| zig | 18961 | 21.6% | 0.0% | 25.0% | 53.4% |
| swift | 3606 | 22.3% | 4.2% | 17.0% | 56.5% |
| cpp | 1064 | 53.8% | 0.0% | 0.6% | 45.7% |
| c | 211 | 5.2% | 1.4% | 0.0% | 93.4% |
| html | 121 | 13.2% | 0.0% | 0.0% | 86.8% |
| shell | 106 | 17.9% | 0.0% | 0.0% | 82.1% |
| python | 85 | 16.5% | 0.0% | 0.0% | 83.5% |
| objective-c | 2 | 0.0% | 0.0% | 0.0% | 100.0% |

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
