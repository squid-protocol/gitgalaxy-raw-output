# ARCHITECTURAL_BRIEF: ghostty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/ghostty-org/ghostty` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
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
## 2. THE 13-POINT STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (EQUATIONS & CONTEXT)
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

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5658 |
| Analyzed Artifacts (Scanned) | 1120 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4538 |
| Total LOC | 218839 |
| Volatility Index | 0.005 |
| % Scanned of codebase = | 19.8% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6744 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2054 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 16.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.3505 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 73 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 684 | 175270 | 61.1% |
| SWIFT | 174 | 24026 | 15.5% |
| C | 65 | 12452 | 5.8% |
| MARKDOWN | 44 | 0 | 3.9% |
| NIX | 29 | 1273 | 2.6% |
| JSON | 27 | 882 | 2.4% |
| BLP | 21 | 1157 | 1.9% |
| GLSL | 15 | 583 | 1.3% |
| PLAINTEXT | 13 | 0 | 1.2% |
| XML | 12 | 0 | 1.1% |
| CPP | 11 | 756 | 1.0% |
| SHELL | 9 | 654 | 0.8% |
| OBJECTIVE-C | 5 | 61 | 0.4% |
| CSS | 4 | 111 | 0.4% |
| YAML | 3 | 234 | 0.3% |
| HTML | 2 | 952 | 0.2% |
| MAKEFILE | 1 | 19 | 0.1% |
| PYTHON | 1 | 409 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled Monorepo` (z +0.12; from the repo's file-archetype mix)
> **File Composition:** Large Core Modules 22%, Declarative / Non-Code 20%, Defensive Guards Files 17%, Data / Markup / Trivial 16%, State Mutators Files 9%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 1059 | 94.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 61 | 5.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4538*

**Composition by Extension & Reason:**
- `no_extension`: 3494x Excluded (Binary Format Detected), 308x Excluded: Neighborhood Micro-Mass Limit Exceeded, 208x Unsupported Format (.undeterminable)
- `.txt`: 235x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 92x Excluded (Explicitly Denied Extension: '.png')
- `.zig`: 36x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2775 LOC), 1x Excluded (Embedded Hex Payload: 1617 hex tokens in 674 LOC)
- `.po`: 29x Excluded (Unsupported Extension: '.po')
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Zero-Density Threshold (LOC: 65, Signals: 0)
- `.ttf`: 15x Excluded (Explicitly Denied Extension: '.ttf')
- `.md`: 8x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Machine-Generated Source Code Signature: 288 LOC)
- `.in`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2371 LOC), 1x Excluded (Machine-Generated Source Code Signature: 220 LOC)
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 20820 hex tokens in 10450 LOC)
- `.nu`: 3x Excluded (Unsupported Extension: '.nu'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.data`: 3x Excluded (Binary Format Detected)
- `.nix`: 1x Excluded (Machine-Generated Source Code Signature: 382 LOC), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.html`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.3 | 8.1 | 4.4 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 23.8 | 9.2 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 11.2 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 8.6 | 2.4 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 29.3 | 25.7 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 3.6 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 22.6 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 100.0 | 2.2 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 76.0 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 2.7 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 37.4 | 21.7 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 16611 | 658 | 27 | `src/stb/stb_image.h` |
| cleanup | 5649 | 310 | 6 | `src/terminal/Terminal.zig` |
| guards | 33439 | 707 | 52 | `src/terminal/Terminal.zig` |
| danger | 4512 | 429 | 10 | `src/terminal/c/terminal.zig` |
| concurrency | 902 | 114 | 1 | `src/Surface.zig` |
| connectivity | 8156 | 733 | 18 | `src/config/Config.zig` |
| io | 586 | 139 | 1 | `src/shell-integration/bash/ghostty.bash` |
| crypto | 0 | 0 | 0 | - |
| ipc | 186 | 56 | 0 | `macos/Sources/Ghostty/Ghostty.App.swift` |
| time | 13 | 8 | 0 | `macos/Sources/Features/QuickTerminal/QuickTerminalScreenStateCache.swift` |
| serialization | 19 | 7 | 0 | `macos/Tests/ColorizedGhosttyIconTests.swift` |
| regex | 61 | 23 | 0 | `src/config/Config.zig` |
| events | 647 | 220 | 1 | `macos/Sources/Ghostty/Ghostty.App.swift` |
| tests | 3890 | 263 | 6 | `src/terminal/Terminal.zig` |
| docs | 20808 | 654 | 41 | `src/config/Config.zig` |
| debt | 646 | 187 | 1 | `src/stb/stb_image.h` |
| mutation | 50204 | 904 | 84 | `src/terminal/PageList.zig` |
| dead_code | 1329 | 367 | 2 | `src/font/shaper/harfbuzz.zig` |
| credential | 33 | 9 | 0 | `flatpak/zig-packages.json` |
| threat | 855 | 204 | 2 | `src/cli/args.zig` |
| ml_ai | 1597 | 197 | 3 | `src/terminal/color.zig` |
| ui | 967 | 125 | 1 | `macos/Sources/Ghostty/Surface View/SurfaceView.swift` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.0884**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/shell-integration/bash/ghostty.bash` (Hits: 65)
- `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish` (Hits: 39)
- `src/cli/ssh-cache/DiskCache.zig` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **quirks.zig** (`src/quirks.zig`) — 113 inbound connections
2. **main.zig** (`src/terminal/main.zig`) — 44 inbound connections
3. **lib.zig** (`src/terminal/lib.zig`) — 37 inbound connections
4. **apprt.zig** (`src/apprt.zig`) — 34 inbound connections
5. **gtk.zig** (`src/apprt/gtk.zig`) — 34 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/terminal/main.zig`) — 40 outbound dependencies
2. **application.zig** (`src/apprt/gtk/class/application.zig`) — 38 outbound dependencies
3. **surface.zig** (`src/apprt/gtk/class/surface.zig`) — 36 outbound dependencies
4. **main_ghostty.zig** (`src/main_ghostty.zig`) — 33 outbound dependencies
5. **window.zig** (`src/apprt/gtk/class/window.zig`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `findSurface` **(Compute Cores)** (@ `macos/Sources/Ghostty/Ghostty.App.swift`) -> Impact: **579.1** | LOC: 1372
  * *Intent:* #if os(macOS) /// Called when a callback needs access to a specific surface. This should return nil /// when the surface is no longer valid.
- `csiDispatch` **(Many-Argument Workhorses)** (@ `src/terminal/stream.zig`) -> Impact: **484.2** | LOC: 1162
- `Stream` **(Compute Cores)** (@ `src/terminal/stream.zig`) -> Impact: **406.9** | LOC: 1321
  * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T can choose to react to whatever actions it cares ...
- `rebuildRow` **(Many-Argument Workhorses)** (@ `src/renderer/generic.zig`) -> Impact: **301.4** | LOC: 447
- `stbi__bmp_load` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **250.9** | LOC: 202
- `SplitTree` **(Compute Cores)** (@ `src/datastruct/split_tree.zig`) -> Impact: **235.5** | LOC: 1315
  * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(*const View, *const View) bool` - Check if two vie...
- `Renderer` **(Compute Cores)** (@ `src/renderer/generic.zig`) -> Impact: **223.0** | LOC: 1631
  * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the input buffers and textures and /// : the vertex/frag...
- `stbi__create_png_image_raw` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **217.6** | LOC: 211
  * *Intent:* // create the png data from post-deflated data
- `stbi__parse_png_file` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **203.1** | LOC: 182
  * *Intent:* #define STBI__PNG_TYPE(a,b,c,d) (((unsigned) (a) << 24) + ((unsigned) (b) << 16) + ((unsigned) (c) << 8) + (unsigned) (d))
- `load_jpeg_image` **(Many-Argument Workhorses)** (@ `src/stb/stb_image.h`) -> Impact: **182.0** | LOC: 162

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/terminal` | 45 | 13646.2 | 7.6% | 5.67% |
| `src/stb` | 4 | 11020.76 | 38.49% | 5.83% |
| `src/apprt/gtk/class` | 22 | 5133.64 | 5.53% | 12.23% |
| `src` | 28 | 3661.26 | 5.95% | 11.21% |
| `macos/Sources/Ghostty` | 16 | 3209.88 | 16.35% | 31.38% |
| `src/renderer` | 17 | 2959.36 | 5.46% | 7.13% |
| `src/config` | 19 | 2417.94 | 3.69% | 10.65% |
| `src/font` | 19 | 2318.06 | 7.16% | 5.7% |
| `macos/Sources/Ghostty/Surface View` | 10 | 2284.96 | 20.01% | 47.04% |
| `macos/Sources/Features/Terminal` | 7 | 2284.78 | 24.17% | 51.82% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `macos/Sources/Features/Update/UpdateDriver.swift` -> **99.9998%** Exposure
- `macos/Sources/Ghostty/Ghostty.Inspector.swift` -> **99.9998%** Exposure
- `macos/Sources/Features/About/AboutController.swift` -> **99.9925%** Exposure
- `macos/Sources/Features/QuickTerminal/QuickTerminalWindow.swift` -> **99.9665%** Exposure
- `pkg/apple-sdk/build.zig` -> **99.956%** Exposure
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
- **Unknown Dependencies:** `2841` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT) -> Cumulative Risk: **720.71**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.38)
- **Magnitude:** 1372.9 | **LOC:** 2352 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9673%), Concurrency (96.6137%), Tech Debt (95.9167%)
- **Heaviest Functions:** `init` (Many-Argument Workhorses, Impact: 45.6), `performKeyEquivalent` (Compute Cores, Impact: 40.0), `keyDown` (Compute Cores, Impact: 38.6)

### 2. `macos/Sources/Features/Update/UpdateDriver.swift` (SWIFT) -> Cumulative Risk: **702.58**
- **Archetype:** `file_cluster_17` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.04)
- **Magnitude:** 137.1 | **LOC:** 213 | **CtrlFlow:** 18.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.9998%), State Flux (99.8901%), Concurrency (99.131%)
- **Heaviest Functions:** `showUpdaterError` (Defensive Guards, Impact: 15.0), `showDownloadDidReceiveExpectedContentLength` (Compute Cores, Impact: 6.4), `showDownloadDidReceiveData` (Compute Cores, Impact: 6.4)

### 3. `macos/Sources/Features/QuickTerminal/QuickTerminalController.swift` (SWIFT) -> Cumulative Risk: **699.49**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.19)
- **Magnitude:** 500.52 | **LOC:** 789 | **CtrlFlow:** 30.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9993%), Concurrency (99.7487%), Documentation (93.1818%)
- **Heaviest Functions:** `animateWindowOut` (Defensive Guards, Impact: 25.4), `windowDidResignKey` (Compute Cores, Impact: 24.2), `init` (Many-Argument Workhorses, Impact: 22.8)

### 4. `macos/Sources/Features/Terminal/Window Styles/TitlebarTabsTahoeTerminalWindow.swift` (SWIFT) -> Cumulative Risk: **697.08**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.58)
- **Magnitude:** 179.42 | **LOC:** 347 | **CtrlFlow:** 18.9% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), State Flux (99.9449%), Tech Debt (98.8079%)
- **Heaviest Functions:** `sendEvent` (Compute Cores, Impact: 15.7), `setupTabBar` (I/O & Config Routines, Impact: 15.7), `toolbar` (Compute Cores, Impact: 15.1)

### 5. `macos/GhosttyUITests/GhosttyThemeTests.swift` (SWIFT) -> Cumulative Risk: **673.75**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.14)
- **Magnitude:** 203.76 | **LOC:** 160 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Tech Debt (98.9347%), Cognitive Load (92.1656%)
- **Heaviest Functions:** `assertTitlebarAppearance` (Defensive Guards, Impact: 51.5), `testIssue8282` (Interface Declarations, Impact: 4.8), `testQuickTerminalThemeChange` (Interface Declarations, Impact: 4.8)

### 6. `macos/Sources/Features/Terminal/Window Styles/TerminalWindow.swift` (SWIFT) -> Cumulative Risk: **673.01**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.74)
- **Magnitude:** 426.08 | **LOC:** 843 | **CtrlFlow:** 27.3% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9959%), Concurrency (95.7396%), Documentation (93.9394%)
- **Heaviest Functions:** `syncAppearance` (Defensive Guards, Impact: 21.8), `awakeFromNib` (I/O & Config Routines, Impact: 20.7), `appendTabModifierSection` (Defensive Guards, Impact: 20.5)

### 7. `macos/Sources/Features/Terminal/Window Styles/TitlebarTabsVenturaTerminalWindow.swift` (SWIFT) -> Cumulative Risk: **663.46**
- **Archetype:** `file_cluster_2` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.07)
- **Magnitude:** 439.52 | **LOC:** 714 | **CtrlFlow:** 35.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.6692%), Documentation (95.0%)
- **Heaviest Functions:** `pushTabsToTitlebar` (Defensive Guards, Impact: 22.1), `toolbar` (Many-Argument Workhorses, Impact: 17.6), `update` (I/O & Config Routines, Impact: 16.9)

### 8. `macos/Sources/Helpers/Fullscreen.swift` (SWIFT) -> Cumulative Risk: **657.65**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.14)
- **Magnitude:** 219.32 | **LOC:** 459 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (85.9404%), Documentation (83.3333%)
- **Heaviest Functions:** `init?` (Defensive Guards, Impact: 23.1), `exit` (I/O & Config Routines, Impact: 21.8), `enter` (I/O & Config Routines, Impact: 13.6)

### 9. `macos/Sources/Ghostty/Surface View/InspectorView.swift` (SWIFT) -> Cumulative Risk: **653.36**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.59)
- **Magnitude:** 251.0 | **LOC:** 442 | **CtrlFlow:** 25.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.8064%), Tech Debt (99.4738%), Documentation (97.2973%)
- **Heaviest Functions:** `scrollWheel` (Compute Cores, Impact: 18.8), `onControlInspector` (Defensive Guards, Impact: 15.1), `insertText` (Defensive Guards, Impact: 14.9)

### 10. `macos/Sources/Features/Terminal/BaseTerminalController.swift` (SWIFT) -> Cumulative Risk: **644.65**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Defensive Guards Files` (z +0.54)
- **Magnitude:** 1027.08 | **LOC:** 1549 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.6197%), Tech Debt (99.4677%), Documentation (88.0795%)
- **Heaviest Functions:** `splitDidDrop` (Many-Argument Workhorses, Impact: 49.9), `clipboardConfirmationComplete` (Defensive Guards, Impact: 27.4), `ghosttyDidResizeSplit` (Defensive Guards, Impact: 27.0)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/stb/stb_image.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 9036.34 | **LOC:** 7988 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (79.4935%), Tech Debt (14.7368%)
**Top Internal Functions/Classes:**
  * `stbi__bmp_load` **(Many-Argument Workhorses)** (Impact: 250.9)
  * `stbi__create_png_image_raw` **(Many-Argument Workhorses)** (Impact: 217.6)
    * *Intent:* // create the png data from post-deflated data
  * `stbi__parse_png_file` **(Many-Argument Workhorses)** (Impact: 203.1)
    * *Intent:* #define STBI__PNG_TYPE(a,b,c,d) (((unsigned) (a) << 24) + ((unsigned) (b) << 16) + ((unsigned) (c) <...
  * `load_jpeg_image` **(Many-Argument Workhorses)** (Impact: 182.0)
  * `stbi__psd_load` **(Many-Argument Workhorses)** (Impact: 176.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 1481 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 4714
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1710`, `structural_boundaries: 862`, `args: 451`, `func_start: 221`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 94`, `state_mutation: 1752`, `dead_code: 35`, `planned_debt: 11`, `fragile_debt: 25`
* *Architecture:* `io: 8`, `api: 125`, `concurrency: 1`, `import: 14`
* *Defense:* `safety: 13`, `doc: 9`, `immutability_locks: 99`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002039
  * `Imports (Out-Degree: 0):` arm_neon.h, assert.h, emmintrin.h, intrin.h, limits.h, math.h, stb_image.h, stdarg.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/PageList.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 3123.46 | **LOC:** 14608 | **CtrlFlow:** 8.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (9.1475%), Tech Debt (8.3547%)
**Top Internal Functions/Classes:**
  * `diagram` **(Defensive Guards)** (Impact: 75.3)
    * *Intent:* /// ... | | /// 50 | foo | /// ... | | /// +--------+ ACTIVE /// 124 | | | 0 /// 125 |Text | | 1 ///...
  * `eraseRowBounded` **(Many-Argument Workhorses)** (Impact: 69.6)
    * *Intent:* /// A variant of eraseRow that shifts only a bounded number of following /// rows up, filling the sp...
  * `scroll` **(Many-Argument Workhorses)** (Impact: 69.3)
    * *Intent:* /// Scroll the viewport. This will never create new scrollback, allocate /// pages, etc. This can on...
  * `reflowRow` **(Many-Argument Workhorses)** (Impact: 56.0)
    * *Intent:* /// Reflow the provided row in to this cursor.
  * `resizeWithoutReflowGrowCols` **(Many-Argument Workhorses)** (Impact: 52.5)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 423 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 1489
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 849`, `structural_boundaries: 1108`, `args: 116`, `func_start: 116`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 4`, `state_mutation: 643`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 6`
* *Architecture:* `api: 104`, `import: 15`
* *Defense:* `safety: 2295`, `doc: 534`, `test: 208`, `cleanup: 243`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.739
  * `Choke Point (Betweenness):` 0.001427 | `Ripple Effect (Closeness):` 0.058855
  * `Imports (Out-Degree: 7):` main.zig, fastmem.zig, mach.zig, quirks.zig, tripwire.zig, builtin, color.zig, highlight.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Ghostty.App.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 2255.24 | **LOC:** 2241 | **CtrlFlow:** 35.8% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (33.2846%), Tech Debt (13.3087%)
**Top Internal Functions/Classes:**
  * `findSurface` **(Compute Cores)** (Impact: 579.1)
    * *Intent:* #if os(macOS) /// Called when a callback needs access to a specific surface. This should return nil ...
  * `action` **(Many-Argument Workhorses)** (Impact: 148.2)
    * *Intent:* // MARK: Actions (macOS)
  * `commandFinished` **(Many-Argument Workhorses)** (Impact: 53.8)
  * `promptTitle` **(Defensive Guards)** (Impact: 46.4)
  * `gotoWindow` **(Defensive Guards)** (Impact: 36.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 40 instances
* *Amplified Race Conditions:* 8 instances
* *Amplified Cascading Flux:* 44 instances
* *High Risk Execution (weighted view):* 11
* *Concurrency (weighted view):* 56
* *State Mutation (weighted view):* 139
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 629`, `structural_boundaries: 394`, `args: 110`, `func_start: 96`, `class_start: 5`
* *Risk/State:* `high_risk_execution: 51`, `state_mutation: 51`, `unreferenced_by_name: 11`
* *Architecture:* `api: 6`, `concurrency: 16`, `import: 3`
* *Defense:* `safety: 193`, `doc: 19`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GhosttyKit, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/Surface.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1969.72 | **LOC:** 6640 | **CtrlFlow:** 12.4% | **Authorship Centralization:** 45.5%
- **Risk Profile:** Cognitive Load (9.1252%), Tech Debt (8.5587%)
**Top Internal Functions/Classes:**
  * `mouseButtonCallback` **(Many-Argument Workhorses)** (Impact: 154.3)
    * *Intent:* /// Called for mouse button press/release events. This will return true /// if the mouse event was c...
  * `performBindingAction` **(Many-Argument Workhorses)** (Impact: 146.6)
    * *Intent:* /// Perform a binding action. A binding is a keybinding. This function /// must be called from the G...
  * `mouseSelection` **(Many-Argument Workhorses)** (Impact: 83.8)
    * *Intent:* /// Calculates the appropriate selection given pins and pixel x positions for /// the click point an...
  * `maybeHandleBinding` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* /// Maybe handles a binding for a given event and if so returns the effect. /// Returns null if the ...
  * `scrollCallback` **(Many-Argument Workhorses)** (Impact: 69.1)
    * *Intent:* /// Mouse scroll event. Negative is down, left. Positive is up, right. /// /// "Natural scrolling" i...
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Race Conditions:* 3 instances
* *Amplified Cascading Flux:* 74 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 21
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 298
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 545`, `structural_boundaries: 572`, `args: 97`, `func_start: 97`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 1`, `state_mutation: 150`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 2`
* *Architecture:* `io: 5`, `api: 49`, `concurrency: 6`, `import: 20`
* *Defense:* `safety: 732`, `doc: 368`, `test: 5`, `sync_locks: 94`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` App.zig, Command.zig, apprt.zig, builtin, config.zig, main.zig, main.zig, input.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/stb/stb_image_resize.h` (C | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1954.66 | **LOC:** 2635 | **CtrlFlow:** 15.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4644%), Tech Debt (8.5817%)
**Top Internal Functions/Classes:**
  * `stbir__encode_scanline` **(Many-Argument Workhorses)** (Impact: 121.8)
  * `stbir__decode_scanline` **(Many-Argument Workhorses)** (Impact: 88.0)
    * *Intent:* #define STBIR__DECODE(type, colorspace) ((int)(type) * (STBIR_MAX_COLORSPACES) + (int)(colorspace))
  * `stbir__resize_allocated` **(Many-Argument Workhorses)** (Impact: 74.1)
  * `stbir__normalize_downsample_coefficients` **(Many-Argument Workhorses)** (Impact: 51.3)
  * `stbir__edge_wrap_slow` **(Many-Argument Workhorses)** (Impact: 38.9)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 312 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1032
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 224`, `args: 79`, `func_start: 67`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 408`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`
* *Architecture:* `api: 43`, `import: 5`
* *Defense:* `safety: 12`, `doc: 4`, `immutability_locks: 42`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 0.834
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002039
  * `Imports (Out-Degree: 0):` assert.h, math.h, stb_image_resize.h, stdint.h, stdlib.h, string.h
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/config/Config.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1644.58 | **LOC:** 10888 | **CtrlFlow:** 7.9% | **Authorship Centralization:** 43.8%
- **Risk Profile:** Cognitive Load (3.0408%), Tech Debt (14.5305%)
**Top Internal Functions/Classes:**
  * `finalize` **(Compute Cores)** (Impact: 72.2)
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
* *Structure:* `branch: 444`, `structural_boundaries: 867`, `args: 149`, `func_start: 149`, `class_start: 96`
* *Risk/State:* `safety_bypasses: 59`, `state_mutation: 84`, `dead_code: 20`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 6`
* *Architecture:* `io: 25`, `api: 229`, `import: 34`
* *Defense:* `safety: 1276`, `doc: 3601`, `test: 127`, `cleanup: 161`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.559
  * `Choke Point (Betweenness):` 0.007829 | `Ripple Effect (Closeness):` 0.072571
  * `Imports (Out-Degree: 17):` build_config.zig, cli.zig, comparison.zig, main.zig, input.zig, key_mods.zig, main.zig, quirks.zig...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `src/terminal/stream.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1614.72 | **LOC:** 3450 | **CtrlFlow:** 15.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.8717%), Tech Debt (56.0344%)
**Top Internal Functions/Classes:**
  * `csiDispatch` **(Many-Argument Workhorses)** (Impact: 484.2)
  * `Stream` **(Compute Cores)** (Impact: 406.9)
    * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T...
  * `escDispatch` **(Many-Argument Workhorses)** (Impact: 88.0)
  * `nextNonUtf8` **(Defensive Guards)** (Impact: 29.1)
    * *Intent:* /// Process the next character and call any callbacks if necessary. /// /// This assumes that we're ...
  * `nextSliceCapped` **(Many-Argument Workhorses)** (Impact: 26.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 30 instances
* *State Mutation (weighted view):* 115
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 433`, `structural_boundaries: 164`, `args: 67`, `func_start: 67`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 24`, `high_risk_execution: 1`, `state_mutation: 55`, `dead_code: 3`, `planned_debt: 9`, `duplicate_logic: 18`
* *Architecture:* `api: 91`, `import: 17`
* *Defense:* `safety: 187`, `doc: 67`, `test: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.804
  * `Choke Point (Betweenness):` 0.001768 | `Ripple Effect (Closeness):` 0.055197
  * `Imports (Out-Degree: 10):` quirks.zig, main.zig, Parser.zig, UTF8Decoder.zig, ansi.zig, charsets.zig, csi.zig, device_attributes.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/renderer/generic.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1477.08 | **LOC:** 3375 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (16.3052%), Tech Debt (7.995%)
**Top Internal Functions/Classes:**
  * `rebuildRow` **(Many-Argument Workhorses)** (Impact: 301.4)
  * `Renderer` **(Compute Cores)** (Impact: 223.0)
    * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the in...
  * `rebuildCells` **(Many-Argument Workhorses)** (Impact: 111.3)
    * *Intent:* /// Convert the terminal state to GPU cells stored in CPU memory. These /// are then synced to the G...
  * `updateFrame` **(Many-Argument Workhorses)** (Impact: 63.1)
    * *Intent:* /// Update the frame data.
  * `drawFrame` **(Many-Argument Workhorses)** (Impact: 59.6)
    * *Intent:* /// Draw the frame to the screen. /// /// If `sync` is true, this will synchronously block until ///...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 71 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 265
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 307`, `structural_boundaries: 192`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 123`, `dead_code: 20`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 38`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 233`, `doc: 227`, `sync_locks: 29`, `cleanup: 66`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.855
  * `Choke Point (Betweenness):` 0.000433 | `Ripple Effect (Closeness):` 0.004588
  * `Imports (Out-Degree: 10):` Surface.zig, apprt.zig, config.zig, file_type.zig, main.zig, nerd_font_attributes.zig, input.zig, math.zig...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/terminal/Terminal.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1415.46 | **LOC:** 13090 | **CtrlFlow:** 5.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (5.3506%), Tech Debt (8.1416%)
**Top Internal Functions/Classes:**
  * `print` **(Many-Argument Workhorses)** (Impact: 124.3)
  * `printCell` **(Many-Argument Workhorses)** (Impact: 56.4)
  * `printAttributes` **(Defensive Guards)** (Impact: 38.6)
    * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// //...
  * `cursorLeft` **(Compute Cores)** (Impact: 36.1)
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
* *Structure:* `branch: 500`, `structural_boundaries: 1201`, `args: 63`, `func_start: 63`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 95`, `high_risk_execution: 6`, `state_mutation: 196`, `dead_code: 17`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 70`, `import: 24`
* *Defense:* `safety: 3390`, `doc: 318`, `test: 372`, `cleanup: 671`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.866
  * `Choke Point (Betweenness):` 0.002654 | `Ripple Effect (Closeness):` 0.057767
  * `Imports (Out-Degree: 11):` quirks.zig, main.zig, Screen.zig, ScreenSet.zig, Tabstops.zig, ansi.zig, charsets.zig, color.zig...
  * `Imported By (In-Degree: 18):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/surface.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1376.64 | **LOC:** 4041 | **CtrlFlow:** 10.4% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (6.1196%), Tech Debt (10.3082%)
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
* *Structure:* `branch: 300`, `structural_boundaries: 284`, `args: 132`, `func_start: 132`, `class_start: 42`
* *Risk/State:* `safety_bypasses: 39`, `high_risk_execution: 1`, `state_mutation: 90`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 5`
* *Architecture:* `api: 160`, `import: 36`
* *Defense:* `safety: 281`, `doc: 198`, `test: 5`, `cleanup: 46`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.415
  * `Choke Point (Betweenness):` 0.004292 | `Ripple Effect (Closeness):` 0.044383
  * `Imports (Out-Degree: 22):` Surface.zig, apprt.zig, build_config.zig, config.zig, main.zig, main.zig, input.zig, i18n.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 1372.9 | **LOC:** 2352 | **CtrlFlow:** 30.3% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (39.1694%), Tech Debt (95.9167%)
**Top Internal Functions/Classes:**
  * `init` **(Many-Argument Workhorses)** (Impact: 45.6)
  * `performKeyEquivalent` **(Compute Cores)** (Impact: 40.0)
    * *Intent:* /// Special case handling for some control keys
  * `keyDown` **(Compute Cores)** (Impact: 38.6)
  * `setCursorShape` **(Compute Cores)** (Impact: 28.1)
  * `flagsChanged` **(Compute Cores)** (Impact: 26.3)
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 15 instances
* *Amplified Cascading Flux:* 114 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 104
* *State Mutation (weighted view):* 387
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 450`, `structural_boundaries: 422`, `args: 142`, `func_start: 103`, `class_start: 10`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 159`, `planned_debt: 1`, `fragile_debt: 1`, `unreferenced_by_name: 54`
* *Architecture:* `io: 1`, `api: 50`, `concurrency: 29`, `import: 6`
* *Defense:* `safety: 133`, `doc: 81`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AppKit, Combine, CoreText, GhosttyKit, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/Screen.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1361.76 | **LOC:** 10353 | **CtrlFlow:** 4.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.3285%), Tech Debt (9.6305%)
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
* *Structure:* `branch: 311`, `structural_boundaries: 1004`, `args: 63`, `func_start: 63`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 212`, `dead_code: 24`, `planned_debt: 4`, `fragile_debt: 11`
* *Architecture:* `api: 74`, `import: 21`
* *Defense:* `safety: 1775`, `doc: 383`, `test: 184`, `cleanup: 513`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.722
  * `Choke Point (Betweenness):` 0.001003 | `Ripple Effect (Closeness):` 0.058943
  * `Imports (Out-Degree: 10):` fastmem.zig, quirks.zig, tripwire.zig, main.zig, PageList.zig, Selection.zig, StringMap.zig, ansi.zig...
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `macos/Sources/Features/Terminal/BaseTerminalController.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1027.08 | **LOC:** 1549 | **CtrlFlow:** 36.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (36.4748%), Tech Debt (99.4677%)
**Top Internal Functions/Classes:**
  * `splitDidDrop` **(Many-Argument Workhorses)** (Impact: 49.9)
  * `clipboardConfirmationComplete` **(Defensive Guards)** (Impact: 27.4)
  * `ghosttyDidResizeSplit` **(Defensive Guards)** (Impact: 27.0)
  * `ghosttyDidFocusSplit` **(Defensive Guards)** (Impact: 25.6)
  * `onConfirmClipboardRequest` **(Defensive Guards)** (Impact: 25.5)
    * *Intent:* // MARK: Clipboard Confirmation
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 4 instances
* *Amplified Race Conditions:* 7 instances
* *Amplified Cascading Flux:* 61 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 50
* *State Mutation (weighted view):* 201
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 370`, `structural_boundaries: 271`, `args: 108`, `func_start: 91`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 4`, `state_mutation: 79`, `planned_debt: 5`, `fragile_debt: 1`, `unreferenced_by_name: 48`
* *Architecture:* `api: 47`, `concurrency: 15`, `import: 4`
* *Defense:* `safety: 143`, `doc: 91`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cocoa, Combine, GhosttyKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `macos/Sources/Features/Terminal/TerminalController.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 934.42 | **LOC:** 1665 | **CtrlFlow:** 38.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (35.4764%), Tech Debt (62.1819%)
**Top Internal Functions/Classes:**
  * `newTab` **(Many-Argument Workhorses)** (Impact: 62.1)
  * `onGotoTab` **(Defensive Guards)** (Impact: 42.1)
  * `newWindow` **(Many-Argument Workhorses)** (Impact: 38.0)
    * *Intent:* /// The "new window" action.
  * `registerUndoForCloseWindow` **(Defensive Guards)** (Impact: 35.4)
    * *Intent:* /// Registers undo for closing window(s), handling both single windows and tab groups.
  * `onMoveTab` **(Defensive Guards)** (Impact: 34.2)
    * *Intent:* // MARK: - Notifications
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 1 instances
* *Amplified Race Conditions:* 2 instances
* *Amplified Cascading Flux:* 45 instances
* *High Risk Execution (weighted view):* 0
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 157
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 426`, `structural_boundaries: 240`, `args: 97`, `func_start: 60`, `class_start: 6`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 67`, `dead_code: 1`, `fragile_debt: 2`, `unreferenced_by_name: 19`
* *Architecture:* `api: 19`, `concurrency: 23`, `import: 5`
* *Defense:* `safety: 160`, `doc: 40`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Cocoa, Combine, Foundation, GhosttyKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/page.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 908.28 | **LOC:** 3919 | **CtrlFlow:** 9.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (12.099%), Tech Debt (7.7886%)
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
* *Structure:* `branch: 248`, `structural_boundaries: 280`, `args: 57`, `func_start: 57`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 74`, `high_risk_execution: 1`, `state_mutation: 132`, `dead_code: 10`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 78`, `import: 12`
* *Defense:* `safety: 405`, `doc: 374`, `test: 48`, `cleanup: 71`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` fastmem.zig, quirks.zig, bitmap_allocator.zig, builtin, color.zig, hash_map.zig, hyperlink.zig, kitty.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/gtk/class/application.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 857.54 | **LOC:** 2957 | **CtrlFlow:** 10.7% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (4.4114%), Tech Debt (10.2477%)
**Top Internal Functions/Classes:**
  * `glibLogWriterFunction` **(Many-Argument Workhorses)** (Impact: 38.8)
    * *Intent:* /// Function used to funnel GLib/GObject/GTK log messages into Zig's logging /// system rather than ...
  * `actionNewWindow` **(Many-Argument Workhorses)** (Impact: 27.6)
    * *Intent:* /// Handle `app.new-window` and `app.new-window-command` GTK actions
  * `new` **(Many-Argument Workhorses)** (Impact: 26.6)
    * *Intent:* /// Creates a new Application instance. /// /// This does a lot more work than a typical class insta...
  * `run` **(Compute Cores)** (Impact: 25.6)
    * *Intent:* /// Run the application. This is a replacement for `gio.Application.run` /// because we want more ti...
  * `gotoWindow` **(Defensive Guards)** (Impact: 20.6)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 15 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 50
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 303`, `args: 108`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 20`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 82`, `import: 42`
* *Defense:* `safety: 216`, `doc: 124`, `cleanup: 26`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.93
  * `Choke Point (Betweenness):` 0.004602 | `Ripple Effect (Closeness):` 0.044816
  * `Imports (Out-Degree: 21):` App.zig, Surface.zig, apprt.zig, build_config.zig, config.zig, global.zig, input.zig, main.zig...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `macos/Sources/App/macOS/AppDelegate.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 799.46 | **LOC:** 1404 | **CtrlFlow:** 34.3% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (34.4492%), Tech Debt (41.7474%)
**Top Internal Functions/Classes:**
  * `setupMenuImages` **(Compute Cores)** (Impact: 41.1)
    * *Intent:* /// Setup all the images for our menu items.
  * `ghosttyConfigDidChange` **(Compute Cores)** (Impact: 36.9)
  * `applicationShouldTerminate` **(Compute Cores)** (Impact: 28.3)
  * `application` **(Compute Cores)** (Impact: 27.9)
  * `applicationDidFinishLaunching` **(Compute Cores)** (Impact: 21.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Race Conditions:* 4 instances
* *Amplified Cascading Flux:* 55 instances
* *Concurrency (weighted view):* 33
* *State Mutation (weighted view):* 187
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 317`, `structural_boundaries: 230`, `args: 82`, `func_start: 63`, `class_start: 8`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 77`, `dead_code: 3`, `unreferenced_by_name: 20`
* *Architecture:* `io: 13`, `api: 83`, `concurrency: 13`, `import: 6`
* *Defense:* `safety: 47`, `doc: 43`, `sync_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AppKit, GhosttyKit, OSLog, Sparkle, SwiftUI, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/datastruct/split_tree.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 784.6 | **LOC:** 2368 | **CtrlFlow:** 11.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.6045%), Tech Debt (8.7493%)
**Top Internal Functions/Classes:**
  * `SplitTree` **(Compute Cores)** (Impact: 235.5)
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
* *Risk/State:* `safety_bypasses: 14`, `high_risk_execution: 1`, `state_mutation: 49`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 283`, `doc: 155`, `test: 17`, `cleanup: 107`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` build_config.zig, quirks.zig, glib, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/formatter.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 770.72 | **LOC:** 6280 | **CtrlFlow:** 6.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (7.6489%), Tech Debt (8.5622%)
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
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 203`, `dead_code: 1`, `planned_debt: 2`, `fragile_debt: 3`
* *Architecture:* `io: 2`, `api: 33`, `import: 18`
* *Defense:* `safety: 971`, `doc: 166`, `test: 100`, `cleanup: 399`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.768
  * `Choke Point (Betweenness):` 0.000597 | `Ripple Effect (Closeness):` 0.047084
  * `Imports (Out-Degree: 8):` quirks.zig, PageList.zig, Screen.zig, Selection.zig, Terminal.zig, charsets.zig, color.zig, hyperlink.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/apprt/embedded.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 764.02 | **LOC:** 2232 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (5.1253%), Tech Debt (0.0%)
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
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 32`, `dead_code: 5`
* *Architecture:* `io: 2`, `api: 142`, `import: 16`
* *Defense:* `safety: 186`, `doc: 185`, `sync_locks: 8`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 1.525
  * `Choke Point (Betweenness):` 0.005171 | `Ripple Effect (Closeness):` 0.060729
  * `Imports (Out-Degree: 6):` App.zig, Surface.zig, apprt.zig, config.zig, main.zig, input.zig, main.zig, main.zig...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/terminal/hash_map.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 751.04 | **LOC:** 1541 | **CtrlFlow:** 10.3% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.5086%), Tech Debt (8.0571%)
**Top Internal Functions/Classes:**
  * `HashMapUnmanaged` **(Many-Argument Workhorses)** (Impact: 175.1)
    * *Intent:* /// Fork of stdlib.HashMap as of Zig 0.12 modified to use offsets for /// the key/values pointer. Th...
  * `getOrPutAssumeCapacityAdapted` **(Many-Argument Workhorses)** (Impact: 21.1)
  * `getIndex` **(Many-Argument Workhorses)** (Impact: 16.1)
    * *Intent:* /// Find the index containing the data for the given key. /// Whether this function returns null is ...
  * `next` **(Compute Cores)** (Impact: 6.8)
  * `init` **(Compute Cores)** (Impact: 6.1)
    * *Intent:* /// Initialize a hash map with a given capacity and a buffer. The /// buffer must fit within the siz...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 54 instances
* *State Mutation (weighted view):* 178
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 118`, `structural_boundaries: 172`, `args: 80`, `func_start: 80`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 1`
* *Architecture:* `api: 82`, `import: 5`
* *Defense:* `safety: 171`, `doc: 106`, `test: 24`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.974
  * `Choke Point (Betweenness):` 0.000195 | `Ripple Effect (Closeness):` 0.051933
  * `Imports (Out-Degree: 1):` quirks.zig, size.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/input/Binding.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 742.82 | **LOC:** 4848 | **CtrlFlow:** 6.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (4.6778%), Tech Debt (7.8723%)
**Top Internal Functions/Classes:**
  * `parseAndPutRecurse` **(Many-Argument Workhorses)** (Impact: 44.4)
    * *Intent:* /// Returns the set that was ultimately updated if a binding was /// added. Unbind does not return a...
  * `parse` **(Defensive Guards)** (Impact: 38.8)
    * *Intent:* /// Parse a single trigger. The input is expected to be ONLY the trigger /// (i.e. in the sequence `...
  * `lessThan` **(Many-Argument Workhorses)** (Impact: 27.9)
    * *Intent:* /// Returns true if lhs should be sorted before rhs
  * `putFlags` **(Many-Argument Workhorses)** (Impact: 23.3)
    * *Intent:* /// Add a binding to the set with explicit flags.
  * `parse` **(Defensive Guards)** (Impact: 21.6)
    * *Intent:* /// Parse an action in the format of "key=value" where key is the /// action name and value is the a...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 28 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 99
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 204`, `structural_boundaries: 352`, `args: 64`, `func_start: 64`, `class_start: 34`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 43`, `dead_code: 11`, `planned_debt: 2`
* *Architecture:* `api: 90`, `import: 12`
* *Defense:* `safety: 661`, `doc: 667`, `test: 85`, `cleanup: 82`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.967
  * `Choke Point (Betweenness):` 0.001185 | `Ripple Effect (Closeness):` 0.053644
  * `Imports (Out-Degree: 5):` build_config.zig, formatter.zig, comparison.zig, quirks.zig, key.zig, key_mods.zig, std, uucode
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/window.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 622.08 | **LOC:** 2112 | **CtrlFlow:** 9.8% | **Authorship Centralization:** 60.0%
- **Risk Profile:** Cognitive Load (4.4561%), Tech Debt (9.4405%)
**Top Internal Functions/Classes:**
  * `newTabPage` **(Many-Argument Workhorses)** (Impact: 20.1)
  * `selectTab` **(Defensive Guards)** (Impact: 19.7)
    * *Intent:* /// Select the tab as requested. Returns true if the tab selection /// changed.
  * `syncAppearance` **(Compute Cores)** (Impact: 18.5)
    * *Intent:* /// Updates various appearance properties. This should always be safe /// to call multiple times. Th...
  * `moveTab` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* /// Move the tab containing the given surface by the given amount. /// Returns if this affected any ...
  * `actionRingBell` **(Defensive Guards)** (Impact: 15.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 117`, `args: 95`, `func_start: 95`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 7`, `planned_debt: 7`
* *Architecture:* `api: 52`, `import: 29`
* *Defense:* `safety: 86`, `doc: 66`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.254
  * `Choke Point (Betweenness):` 0.001539 | `Ripple Effect (Closeness):` 0.044816
  * `Imports (Out-Degree: 16):` Surface.zig, apprt.zig, build_config.zig, config.zig, input.zig, main.zig, quirks.zig, adw_version.zig...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `macos/Sources/Features/Splits/SplitTree.swift` (SWIFT | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_2` (Drift: 0.0 IQR)
- **Magnitude:** 603.86 | **LOC:** 1414 | **CtrlFlow:** 29.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.4549%), Tech Debt (17.4135%)
**Top Internal Functions/Classes:**
  * `resizing` **(Many-Argument Workhorses)** (Impact: 52.9)
    * *Intent:* /// operation. For up/down resizing, it finds the nearest parent vertical split and adjusts /// its ...
  * `focusTarget` **(Compute Cores)** (Impact: 40.9)
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
* *Structure:* `branch: 251`, `structural_boundaries: 256`, `args: 70`, `func_start: 54`, `class_start: 31`
* *Risk/State:* `state_mutation: 44`, `dead_code: 1`, `unreferenced_by_name: 8`
* *Architecture:* `import: 2`
* *Defense:* `safety: 33`, `doc: 253`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.426
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` AppKit, Combine
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/list_themes.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 568.24 | **LOC:** 1742 | **CtrlFlow:** 9.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.4579%), Tech Debt (7.9271%)
**Top Internal Functions/Classes:**
  * `drawPreview` **(Many-Argument Workhorses)** (Impact: 136.1)
  * `update` **(Many-Argument Workhorses)** (Impact: 66.8)
  * `draw` **(Many-Argument Workhorses)** (Impact: 58.6)
  * `updateFiltered` **(Defensive Guards)** (Impact: 31.3)
  * `run` **(Defensive Guards)** (Impact: 25.9)
    * *Intent:* /// directory). If you're running Ghostty from the source, this is the /// `zig-out/share/ghostty/th...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 12 instances
* *Amplified Cascading Flux:* 40 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 123
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 146`, `structural_boundaries: 108`, `args: 30`, `func_start: 30`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 43`, `planned_debt: 1`
* *Architecture:* `io: 9`, `api: 22`, `import: 11`
* *Defense:* `safety: 107`, `doc: 41`, `cleanup: 19`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.465
  * `Choke Point (Betweenness):` 2.2e-05 | `Ripple Effect (Closeness):` 0.001606
  * `Imports (Out-Degree: 3):` config.zig, Config.zig, theme.zig, args.zig, ghostty.zig, std, tui.zig, vaxis...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/terminal/c/terminal.zig` -> Churn: **93.76%** | Cog Load: 7.5274% | Debt: 59.6561%
- `src/terminal/stream_terminal.zig` -> Churn: **63.75%** | Cog Load: 20.6958% | Debt: 99.2082%
- `macos/Sources/Features/Terminal/TerminalController.swift` -> Churn: **61.69%** | Cog Load: 35.4764% | Debt: 62.1819%
- `src/shell-integration/bash/ghostty.bash` -> Churn: **58.9%** | Cog Load: 75.6001% | Debt: 0.0%
- `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` -> Churn: **55.29%** | Cog Load: 39.1694% | Debt: 95.9167%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/terminal/PageList.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 3123.46
- `src/terminal/stream.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1614.72
- `src/renderer/generic.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1477.08
- `src/terminal/Terminal.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 1415.46
- `macos/Sources/Features/Terminal/BaseTerminalController.swift` -> **Tim Culverhouse** (100.0% isolated ownership) | Magnitude: 1027.08

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/apprt/gtk/class/surface.zig` -> **Severity: 0.278** (Bridge: 0.0043 * Flux: 64.7943%)
- `src/config/Config.zig` -> **Severity: 0.241** (Bridge: 0.0078 * Flux: 30.8096%)
- `src/inspector/widgets.zig` -> **Severity: 0.217** (Bridge: 0.0027 * Flux: 80.3691%)
- `src/global.zig` -> **Severity: 0.195** (Bridge: 0.002 * Flux: 95.9835%)
- `src/font/sprite/Face.zig` -> **Severity: 0.179** (Bridge: 0.0022 * Flux: 81.5253%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/quirks.zig` -> **Severity: 6.504** (Embedded: 0.1371 * Error Risk: 47.4308%)
- `src/terminal/charsets.zig` -> **Severity: 5.272** (Embedded: 0.0588 * Error Risk: 89.7035%)
- `src/font/sprite/draw/braille.zig` -> **Severity: 4.752** (Embedded: 0.0483 * Error Risk: 98.426%)
- `src/terminal/ref_counted_set.zig` -> **Severity: 4.373** (Embedded: 0.0586 * Error Risk: 74.6313%)
- `src/datastruct/intrusive_linked_list.zig` -> **Severity: 4.223** (Embedded: 0.0522 * Error Risk: 80.8171%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/quirks.zig` -> **Severity: 1760.265** (Blast Radius: 52.808 * Doc Risk: 33.3333%)
- `src/font/discovery.zig` -> **Severity: 393.386** (Blast Radius: 6.506 * Doc Risk: 60.4651%)
- `src/terminal/Parser.zig` -> **Severity: 345.03** (Blast Radius: 4.929 * Doc Risk: 70.0%)
- `src/config/Config.zig` -> **Severity: 320.297** (Blast Radius: 7.559 * Doc Risk: 42.3729%)
- `pkg/opengl/glad.zig` -> **Severity: 266.46** (Blast Radius: 4.441 * Doc Risk: 60.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
