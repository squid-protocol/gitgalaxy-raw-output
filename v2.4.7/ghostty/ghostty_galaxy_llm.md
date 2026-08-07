# ARCHITECTURAL_BRIEF: ghostty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/ghostty` |
| **Timestamp** | `2026-08-07T04:59:09.123560+00:00` |
| **Scan Duration** | `8.12s` |
| **Git Branch** | `main` |
| **Git Commit** | `debcffbadb75221a030319c075fae12cfe114176` |
| **Git Remote** | `https://github.com/ghostty-org/ghostty` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 907 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are a Senior Technical Storyteller and Codebase Architect. GitGalaxy has translated the non-visual architecture of this repository into measurable Structural Signatures (regex-derived counts, not an AST or compiler pass). Your job is to weave those signatures into a coherent, factual narrative about how this system is built -- its architecture, design patterns, and complexity -- not to render a verdict.
> 
> **CORE DIRECTIVES:**
> 1. **Narrate the Architecture, Don't Judge the Author:** Frame every observation as a blameless description of the system's physical reality. High Risk Exposure (e.g., Cognitive Load Exposure) describes where the architecture may be drifting into fragile territory, not developer incompetence -- it is a prompt to investigate, never a verdict.
> 2. **The Physical Reality Rule:** Base your narrative strictly on the provided Structural Signatures and the numbers derived from them. Do not hallucinate meaning, and do not restate a heuristic's raw label (e.g. a 'Logic Bomb' or 'O(2^N)' flag) as a confirmed finding of malice or a guaranteed defect -- explain what the signature actually measures, weave it into the story of the file, and let the reader draw their own conclusion.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`. Tell that balance as part of the narrative, not as an isolated alarm.
> 
> **THE STRUCTURAL SIGNATURE LEXICON:**
> * **Structure & Mass:** `branch` (splits), `linear` (paths), `args` (coupling), `func_start` (entry points).
> * **Risk & Volatility:** `danger` (dynamic execution), `flux` (state mutation), `graveyard` (commented-out logic), `safety_neg` (security bypasses).
> * **Architecture & Domain:** `io` (network latency), `concurrency` (async orchestration), `api` (public surface), `import` (dependencies).
> * **Defensive Guardrails:** `safety` (Error handling), `freeze_hits` (immutability), `cleanup` (state destruction).
## 2. THE 13-POINT RISK EXPOSURE ANALYSIS (EQUATIONS & CONTEXT)
> **How the SAST Engine Calculates Risk Exposure (Lower Risk 0 - Higher Risk Exposure 100%):**
> Most scores use a Sigmoid curve based on density (Hits / LOC) to prevent massive files from mathematically hiding their flaws.
> 
> 1. **Cognitive Load Exposure:** Measures the mental effort required for a developer to read and understand the file. `Density(Branches + (Flux * 2) + Async/Danger)` mitigated by `Doc Coverage`.
> 2. **Error & Exception Risk Exposure:** Measures structural integrity and resilience against runtime errors. `Net Exposure = (Danger + Safety_Neg + Flux) - (Safety + Tests + Docs)`.
> 3. **Tech Debt Exposure:** Measures the density of developer-annotated structural stress. `Density(TODOs [1x] + FIXMEs/Hacks [3x] + Empty Stubs [0.5x])`.
> 4. **Verification Risk Exposure:** Evaluates test coverage by comparing a function's structural complexity against the scope of the tests validating it.
> 5. **API Risk Exposure:** Measures the public surface area of a module. `Ratio(API Hits / Total Functions & Classes)`.
> 6. **Concurrency Risk Exposure:** Measures the density of asynchronous operations, threading, and parallel execution logic.
> 7. **State Flux Risk Exposure:** Measures the frequency of data mutation and variable reassignment.
> 8. **Commented Logic (dead code):** Measures the presence of abandoned, commented-out logic blocks.
> 9. **Spec Match Risk Exposure:** Measures how closely code aligns with formal specifications or architectural requirements.
> 10. **Stability:** Measures the recency of edits relative to the repository's entire lifespan.
> 11. **Deep Churn:** Measures the historical volatility and frequency of modification.
> 12. **Documentation Risk Exposure:** Measures the lack of structured documentation and ownership metadata.
> 13. **Indentation Consistency:** Measures formatting alignment (Tabs vs. Spaces). Provided for codebase standardization context, not a functional risk.
> 
> **--- THE SECURITY & VULNERABILITY LENS ---**
> 14. **Obfuscation & Evasion Risk:** Measures the density of obfuscated logic, packed strings, and non-standard encoding.
> 15. **Logic Bomb / Sabotage Risk:** Measures condition-heavy execution leading to destructive OS, memory, or process commands.
> 16. **Injection Surface Risk Exposure:** Measures external network/I/O input flowing directly into dynamic execution contexts (XSS, SQLi, RCE).
> 17. **Memory Corruption Risk Exposure:** Measures the density of raw pointer math and manual memory allocations (Buffer Overflows, UAF).
> 18. **Secrets Risk Exposure:** Measures the presence of hardcoded credentials exposed to logs or globals.
> 
> **--- STRUCTURAL MAGNITUDE (NOT RISK) ---**
> **19. Function Magnitude (Impact Score):** Measures the physical footprint and 'heaviness' of a specific function. `((BranchHits + 1) * (Args + 1) + (0.05 * LOC)) * 10`. This is NOT a risk score.
> **20. File Magnitude (Total Impact):** Measures the total structural impact of a file. `Sum(Function Impacts) + API + Concurrency + Flux + (LOC / 50)`. This is NOT a risk score.

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 5658 |
| Analyzed Artifacts (Scanned) | 983 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 4675 |
| Total LOC | 238763 |
| Volatility Index | 0.006 |
| % Scanned of codebase = | 17.4% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.9085 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2646 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.8% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 5.7669 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 64 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 591 | 209299 | 60.1% |
| SWIFT | 169 | 16583 | 17.2% |
| C | 64 | 6332 | 6.5% |
| MARKDOWN | 39 | 0 | 4.0% |
| NIX | 25 | 1169 | 2.5% |
| BLP | 21 | 1068 | 2.1% |
| GLSL | 14 | 489 | 1.4% |
| PLAINTEXT | 12 | 0 | 1.2% |
| CPP | 11 | 727 | 1.1% |
| XML | 11 | 0 | 1.1% |
| YAML | 5 | 479 | 0.5% |
| SHELL | 5 | 614 | 0.5% |
| OBJECTIVE-C | 5 | 61 | 0.5% |
| CSS | 4 | 111 | 0.4% |
| JSON | 3 | 397 | 0.3% |
| HTML | 2 | 1006 | 0.2% |
| MAKEFILE | 1 | 19 | 0.1% |
| PYTHON | 1 | 409 | 0.1% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.25`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 546 | 55.5% |
| file_cluster_13 | 305 | 31.0% |
| file_cluster_2 | 19 | 1.9% |
| file_cluster_17 | 15 | 1.5% |
| file_cluster_0 | 15 | 1.5% |
| file_cluster_16 | 11 | 1.1% |
| file_cluster_4 | 7 | 0.7% |
| file_cluster_11 | 4 | 0.4% |
| file_cluster_9 | 4 | 0.4% |
| file_cluster_12 | 1 | 0.1% |
| file_cluster_7 | 1 | 0.1% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 55 | 5.6% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 4675*

**Composition by Extension & Reason:**
- `no_extension`: 4021x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 8x Unsupported Format (.undeterminable), 3x Excluded (Unsupported Extension: '.entitlements')
- `.txt`: 236x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.png`: 92x Excluded (Explicitly Denied Extension: '.png')
- `.zig`: 85x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 2775 LOC), 1x Excluded (Embedded Hex Payload: 1617 hex tokens in 674 LOC)
- `.zon`: 44x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.po`: 29x Excluded (Unsupported Extension: '.po')
- `.json`: 24x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 22x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 13x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 125 LOC), 1x Excluded (Machine-Generated Source Code Signature: 288 LOC)
- `.ttf`: 15x Excluded (Explicitly Denied Extension: '.ttf')
- `.nix`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 4 LOC)
- `.in`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.sh`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.h`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 2371 LOC), 1x Excluded (Machine-Generated Source Code Signature: 220 LOC)
- `.py`: 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Embedded Hex Payload: 20820 hex tokens in 10450 LOC)

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 99.9 | 19.2 | 12.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.7 | 38.1 | 44.3 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 21.2 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 25.2 | 2.5 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.3 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 3.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 42.7 | 34.5 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/shell-integration/bash/ghostty.bash` (Hits: 61)
- `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish` (Hits: 33)
- `src/cli/ssh-cache/DiskCache.zig` (Hits: 30)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **gtk.zig** (`src/apprt/gtk.zig`) — 33 inbound connections
2. **macos.zig** (`src/os/macos.zig`) — 18 inbound connections
3. **result.zig** (`src/terminal/c/result.zig`) — 17 inbound connections
4. **lib.zig** (`src/terminal/lib.zig`) — 15 inbound connections
5. **build_options.zig** (`src/terminal/build_options.zig`) — 13 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/terminal/main.zig`) — 40 outbound dependencies
2. **application.zig** (`src/apprt/gtk/class/application.zig`) — 38 outbound dependencies
3. **surface.zig** (`src/apprt/gtk/class/surface.zig`) — 36 outbound dependencies
4. **main_ghostty.zig** (`src/main_ghostty.zig`) — 33 outbound dependencies
5. **window.zig** (`src/apprt/gtk/class/window.zig`) — 29 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `legacy` (@ `src/input/key_encode.zig`) -> Impact: **893.3** | LOC: 1587
  * *Intent:* /// Perform legacy encoding of the key event. "Legacy" in this case /// is referring to the behavior of traditional terminals, plus /// xterm's `modif...
- `printAttributes` (@ `src/terminal/Terminal.zig`) -> Impact: **860.1** | LOC: 1406
  * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// /// Boolean attributes are printed first, followed b...
- `maybePromptClick` (@ `src/Surface.zig`) -> Impact: **745.8** | LOC: 1440
- `format` (@ `src/terminal/tmux/output.zig`) -> Impact: **717.6** | LOC: 533
  * *Intent:* /// Format a set of variables into the proper format string for tmux /// that we can handle with `parseFormatStruct`.
- `Stream` (@ `src/terminal/stream.zig`) -> Impact: **677.1** | LOC: 1183
  * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T can choose to react to whatever actions it cares ...
- `deviceStatus` (@ `src/terminal/stream_terminal.zig`) -> Impact: **636.5** | LOC: 1507
- `SplitTree` (@ `src/datastruct/split_tree.zig`) -> Impact: **614.7** | LOC: 1294
  * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(*const View, *const View) bool` - Check if two vie...
- `stbi__decode_jpeg_image` (@ `src/stb/stb_image.h`) -> Impact: **610.6** | LOC: 1076
- `csiDispatch` (@ `src/terminal/stream.zig`) -> Impact: **579.9** | LOC: 1136
- `parse` (@ `src/terminal/osc/parsers/osc9.zig`) -> Impact: **578.1** | LOC: 1135
  * *Intent:* /// Parse OSC 9, which could be an iTerm2 notification or a ConEmu extension.

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/terminal` | 45 | 25019.54 | 19.81% | 20.46% |
| `src/apprt/gtk/class` | 22 | 7628.16 | 7.68% | 64.37% |
| `src/config` | 19 | 6085.64 | 19.45% | 30.51% |
| `src` | 28 | 6056.34 | 12.97% | 22.4% |
| `src/stb` | 4 | 5783.42 | 20.52% | 3.21% |
| `src/input` | 16 | 5483.2 | 14.69% | 16.67% |
| `src/renderer` | 17 | 4766.72 | 15.0% | 18.47% |
| `src/cli` | 24 | 4548.94 | 27.65% | 16.66% |
| `src/font` | 19 | 4153.64 | 12.43% | 25.06% |
| `src/terminal/osc/parsers` | 15 | 3611.84 | 40.68% | 6.2% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/check-translations.sh` -> **100.0%** Exposure
- `snap/local/launcher` -> **100.0%** Exposure
- `pkg/macos/text/ext.c` -> **100.0%** Exposure
- `pkg/highway/bridge.cpp` -> **100.0%** Exposure
- `pkg/utfcpp/empty.cc` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/shell-integration/bash/bash-preexec.sh` -> **100.0%** Exposure
- `src/shell-integration/bash/ghostty.bash` -> **100.0%** Exposure
- `include/ghostty/vt/build_info.h` -> **100.0%** Exposure
- `include/ghostty/vt/osc.h` -> **100.0%** Exposure
- `include/ghostty/vt/screen.h` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/config/Config.zig` -> **0** Orphaned Functions | **86** Duplicates
- `macos/Tests/Splits/SplitTreeTests.swift` -> **49** Orphaned Functions | **3** Duplicates
- `macos/Sources/Features/Terminal/BaseTerminalController.swift` -> **43** Orphaned Functions | **4** Duplicates
- `macos/Sources/Ghostty/Ghostty.App.swift` -> **41** Orphaned Functions | **2** Duplicates
- `macos/Tests/Ghostty/ConfigTests.swift` -> **35** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/pty.c`** -> AI Confidence: **99.48%**
2. **`pkg/macos/main.zig`** -> AI Confidence: **99.48%**
3. **`pkg/opengl/main.zig`** -> AI Confidence: **99.48%**
4. **`src/App.zig`** -> AI Confidence: **99.48%**
5. **`src/Surface.zig`** -> AI Confidence: **99.48%**
6. **`src/apprt/action.zig`** -> AI Confidence: **99.48%**
7. **`src/apprt/gtk/class/clipboard_confirmation_dialog.zig`** -> AI Confidence: **99.48%**
8. **`src/apprt/gtk/winproto.zig`** -> AI Confidence: **99.48%**
9. **`src/apprt/surface.zig`** -> AI Confidence: **99.48%**
10. **`src/config.zig`** -> AI Confidence: **99.48%**
11. **`src/font/main.zig`** -> AI Confidence: **99.48%**
12. **`src/font/sprite/draw/symbols_for_legacy_computing.zig`** -> AI Confidence: **99.48%**
13. **`src/global.zig`** -> AI Confidence: **99.48%**
14. **`src/lib_vt.zig`** -> AI Confidence: **99.48%**
15. **`src/main_ghostty.zig`** -> AI Confidence: **99.48%**
16. **`src/main_wasm.zig`** -> AI Confidence: **99.48%**
17. **`src/os/main.zig`** -> AI Confidence: **99.48%**
18. **`src/renderer/OpenGL.zig`** -> AI Confidence: **99.48%**
19. **`src/renderer/generic.zig`** -> AI Confidence: **99.48%**
20. **`src/renderer/metal/Frame.zig`** -> AI Confidence: **99.48%**
21. **`src/renderer/metal/RenderPass.zig`** -> AI Confidence: **99.48%**
22. **`src/renderer/opengl/Frame.zig`** -> AI Confidence: **99.48%**
23. **`src/terminal/c/main.zig`** -> AI Confidence: **99.48%**
24. **`src/terminal/main.zig`** -> AI Confidence: **99.48%**
25. **`src/terminal/search.zig`** -> AI Confidence: **99.48%**
26. **`src/termio/Exec.zig`** -> AI Confidence: **99.48%**
27. **`src/termio/stream_handler.zig`** -> AI Confidence: **99.48%**
28. **`src/font/shape.zig`** -> AI Confidence: **99.44%**
29. **`src/input.zig`** -> AI Confidence: **99.44%**
30. **`src/renderer.zig`** -> AI Confidence: **99.44%**
31. **`src/terminal/stream.zig`** -> AI Confidence: **99.44%**
32. **`src/apprt.zig`** -> AI Confidence: **99.43%**
33. **`src/build_config.zig`** -> AI Confidence: **99.43%**
34. **`src/cli/version.zig`** -> AI Confidence: **99.43%**
35. **`src/font/face.zig`** -> AI Confidence: **99.43%**
36. **`src/termio.zig`** -> AI Confidence: **99.43%**
37. **`src/apprt/gtk.zig`** -> AI Confidence: **99.42%**
38. **`src/terminal/osc.zig`** -> AI Confidence: **99.42%**
39. **`src/apprt/embedded.zig`** -> AI Confidence: **99.39%**
40. **`src/apprt/gtk/class/resize_overlay.zig`** -> AI Confidence: **99.39%**
41. **`src/apprt/gtk/class/search_overlay.zig`** -> AI Confidence: **99.39%**
42. **`src/apprt/gtk/class/surface.zig`** -> AI Confidence: **99.39%**
43. **`src/apprt/gtk/winproto/wayland.zig`** -> AI Confidence: **99.39%**
44. **`src/cli/explain_config.zig`** -> AI Confidence: **99.39%**
45. **`src/cli/ghostty.zig`** -> AI Confidence: **99.39%**
46. **`src/cli/list_themes.zig`** -> AI Confidence: **99.39%**
47. **`src/cli/new_window.zig`** -> AI Confidence: **99.39%**
48. **`src/crash/sentry.zig`** -> AI Confidence: **99.39%**
49. **`src/font/sprite/Face.zig`** -> AI Confidence: **99.39%**
50. **`src/inspector/Inspector.zig`** -> AI Confidence: **99.39%**
51. **`src/inspector/widgets/screen.zig`** -> AI Confidence: **99.39%**
52. **`src/main_c.zig`** -> AI Confidence: **99.39%**
53. **`src/renderer/Metal.zig`** -> AI Confidence: **99.39%**
54. **`src/renderer/Thread.zig`** -> AI Confidence: **99.39%**
55. **`src/renderer/cell.zig`** -> AI Confidence: **99.39%**
56. **`src/terminal/search/Thread.zig`** -> AI Confidence: **99.39%**
57. **`src/terminal/search/viewport.zig`** -> AI Confidence: **99.39%**
58. **`src/terminal/tmux/viewer.zig`** -> AI Confidence: **99.39%**
59. **`src/termio/Termio.zig`** -> AI Confidence: **99.39%**
60. **`src/shell-integration/bash/ghostty.bash`** -> AI Confidence: **99.34%**
61. **`pkg/libintl/libintl.h`** -> AI Confidence: **99.34%**
62. **`pkg/harfbuzz/c.zig`** -> AI Confidence: **99.34%**
63. **`pkg/harfbuzz/shape.zig`** -> AI Confidence: **99.34%**
64. **`src/apprt/gtk/class/global_shortcuts.zig`** -> AI Confidence: **99.34%**
65. **`src/apprt/gtk/class/imgui_widget.zig`** -> AI Confidence: **99.34%**
66. **`src/apprt/gtk/class/tab.zig`** -> AI Confidence: **99.34%**
67. **`src/apprt/gtk/class/title_dialog.zig`** -> AI Confidence: **99.34%**
68. **`src/apprt/gtk/class/window.zig`** -> AI Confidence: **99.34%**
69. **`src/cli/list_keybinds.zig`** -> AI Confidence: **99.34%**
70. **`src/config/Config.zig`** -> AI Confidence: **99.34%**
71. **`src/font/face/coretext.zig`** -> AI Confidence: **99.34%**
72. **`src/font/shaper/run.zig`** -> AI Confidence: **99.34%**
73. **`src/font/sprite/draw/symbols_for_legacy_computing_supplement.zig`** -> AI Confidence: **99.34%**
74. **`src/inspector/widgets/surface.zig`** -> AI Confidence: **99.34%**
75. **`src/inspector/widgets/termio.zig`** -> AI Confidence: **99.34%**
76. **`src/os/desktop.zig`** -> AI Confidence: **99.34%**
77. **`src/renderer/State.zig`** -> AI Confidence: **99.34%**
78. **`src/synthetic/Osc.zig`** -> AI Confidence: **99.34%**
79. **`src/synthetic/main.zig`** -> AI Confidence: **99.34%**
80. **`src/terminal/PageList.zig`** -> AI Confidence: **99.34%**
81. **`src/terminal/Screen.zig`** -> AI Confidence: **99.34%**
82. **`src/terminal/Terminal.zig`** -> AI Confidence: **99.34%**
83. **`src/terminal/c/style.zig`** -> AI Confidence: **99.34%**
84. **`src/terminal/osc/parsers/kitty_clipboard_protocol.zig`** -> AI Confidence: **99.34%**
85. **`src/terminal/osc/parsers/kitty_color.zig`** -> AI Confidence: **99.34%**
86. **`src/terminal/search/screen.zig`** -> AI Confidence: **99.34%**
87. **`src/termio/Options.zig`** -> AI Confidence: **99.34%**
88. **`src/termio/backend.zig`** -> AI Confidence: **99.34%**
89. **`src/termio/message.zig`** -> AI Confidence: **99.34%**
90. **`src/apprt/gtk/App.zig`** -> AI Confidence: **99.33%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2754` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `snap/local/launcher` (SHELL) -> Cumulative Risk: **703.57**
- **Archetype:** `file_cluster_12` (Distance: 11.393 IQR)
- **Magnitude:** 96.26 | **LOC:** 72 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), State Flux (99.9901%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 12.3), `Anonymous_Block` (Impact: 9.3), `Anonymous_Block` (Impact: 7.3)

### 2. `macos/Sources/App/macOS/AppDelegate.swift` (SWIFT) -> Cumulative Risk: **612.37**
- **Archetype:** `file_cluster_0` (Distance: 12.629 IQR)
- **Magnitude:** 800.68 | **LOC:** 1404 | **CtrlFlow:** 53.9% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9987%), Tech Debt (95.5429%), Safety Score (84.9726%)
- **Heaviest Functions:** `toggleVisibility` (Impact: 120.8), `applicationDidFinishLaunching` (Impact: 44.7), `applicationShouldTerminate` (Impact: 30.7)

### 3. `macos/Sources/Helpers/VibrantLayer.m` (OBJECTIVE-C) -> Cumulative Risk: **577.45**
- **Archetype:** `file_cluster_13` (Distance: 11.969 IQR)
- **Magnitude:** 20.3 | **LOC:** 28 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), Cognitive Load (94.5262%)
- **Heaviest Functions:** `compositingFilter` (Impact: 5.3), `initForAppearance` (Impact: 4.6)

### 4. `src/stb/stb_image.h` (C) -> Cumulative Risk: **573.54**
- **Archetype:** `file_cluster_11` (Distance: 15.303 IQR)
- **Magnitude:** 5741.1 | **LOC:** 7988 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.3138%), Documentation (94.2867%)
- **Heaviest Functions:** `stbi__decode_jpeg_image` (Impact: 610.6), `stbi__parse_png_file` (Impact: 112.1), `stbi__hdr_load` (Impact: 89.2)

### 5. `src/shell-integration/bash/bash-preexec.sh` (SHELL) -> Cumulative Risk: **569.51**
- **Archetype:** `file_cluster_11` (Distance: 14.782 IQR)
- **Magnitude:** 261.74 | **LOC:** 383 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9988%), Safety Score (85.923%)
- **Heaviest Functions:** `__bp_trim_whitespace` (Impact: 117.8), `Anonymous_Block` (Impact: 8.2), `Anonymous_Block` (Impact: 6.2)

### 6. `macos/Sources/Features/App Intents/InputIntent.swift` (SWIFT) -> Cumulative Risk: **568.87**
- **Archetype:** `file_cluster_0` (Distance: 11.853 IQR)
- **Magnitude:** 168.3 | **LOC:** 328 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9927%), Tech Debt (90.9512%), Safety Score (81.1095%)
- **Heaviest Functions:** `perform` (Impact: 11.6), `perform` (Impact: 11.6), `perform` (Impact: 11.6)

### 7. `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT) -> Cumulative Risk: **565.81**
- **Archetype:** `file_cluster_0` (Distance: 13.042 IQR)
- **Magnitude:** 1303.3 | **LOC:** 2352 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (95.8994%), State Flux (94.5131%), Verification (80.0%)
- **Heaviest Functions:** `performKeyEquivalent` (Impact: 280.0), `menu` (Impact: 221.2), `attributedSubstring` (Impact: 137.1)

### 8. `src/pty.zig` (ZIG) -> Cumulative Risk: **565.56**
- **Archetype:** `file_cluster_8` (Distance: 12.164 IQR)
- **Magnitude:** 272.18 | **LOC:** 507 | **CtrlFlow:** 65.1% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9999%), Verification (80.0%)
- **Heaviest Functions:** `getProcessInfo` (Impact: 44.2), `open` (Impact: 36.1), `open` (Impact: 25.2)

### 9. `src/benchmark/CodepointWidth.zig` (ZIG) -> Cumulative Risk: **564.12**
- **Archetype:** `file_cluster_4` (Distance: 13.453 IQR)
- **Magnitude:** 183.06 | **LOC:** 208 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (99.9998%), State Flux (99.2127%), Safety Score (84.6291%)
- **Heaviest Functions:** `stepWcwidth` (Impact: 22.3), `stepTable` (Impact: 22.3), `stepSimd` (Impact: 18.6)

### 10. `src/shell-integration/bash/ghostty.bash` (SHELL) -> Cumulative Risk: **562.99**
- **Archetype:** `file_cluster_13` (Distance: 13.27 IQR)
- **Magnitude:** 406.26 | **LOC:** 325 | **CtrlFlow:** 87.6% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.1624%), Cognitive Load (87.5892%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 295.3)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/stb/stb_image.h` (C | Tier 4 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.303 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.442 IQR)
- **Top Global Matches:** file_cluster_11: 15.303, file_cluster_8: 15.305, file_cluster_0: 15.354
- **Magnitude:** 5741.1 | **LOC:** 7988 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (67.0891%), Tech Debt (12.8355%)
**Top Internal Functions/Classes:**
  * `stbi__decode_jpeg_image` (Impact: 610.6)
  * `stbi__parse_png_file` (Impact: 112.1)
  * `stbi__hdr_load` (Impact: 89.2)
    * *Intent:* // this is a reduced-precision calculation of YCbCr-to-RGB introduced // to make sure the code produ...
  * `stbi__create_png_image_raw` (Impact: 69.6)
  * `stbi__tga_test` (Impact: 56.2)
    * *Intent:* // wide add #define dct_wadd(out, a, b) \
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 894`, `structural_boundaries: 412`, `args: 31`, `func_start: 114`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 3270`, `dead_code: 17`, `planned_debt: 1`, `fragile_debt: 4`, `duplicate_logic: 2`
* *Architecture:* `io: 11`, `api: 652`
* *Defense:* `safety: 3`, `doc: 62`, `immutability_locks: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.453
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002035
  * `Imports (Out-Degree: 0):` stddef.h, stdarg.h, intrin.h, stdint.h, arm_neon.h, limits.h, stdio.h, emmintrin.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/PageList.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.59 IQR)
- **Top Global Matches:** file_cluster_8: 14.59, file_cluster_7: 14.815, file_cluster_0: 14.908
- **Magnitude:** 4514.92 | **LOC:** 14608 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (21.6108%), Tech Debt (18.7098%)
**Top Internal Functions/Classes:**
  * `diagram` (Impact: 195.4)
    * *Intent:* /// ... | | /// 50 | foo | /// ... | | /// +--------+ ACTIVE /// 124 | | | 0 /// 125 |Text | | 1 ///...
  * `eraseRowBounded` (Impact: 121.4)
    * *Intent:* /// A variant of eraseRow that shifts only a bounded number of following /// rows up, filling the sp...
  * `scroll` (Impact: 110.9)
    * *Intent:* /// Scroll the viewport. This will never create new scrollback, allocate /// pages, etc. This can on...
  * `resizeWithoutReflowGrowCols` (Impact: 106.7)
  * `resizeCols` (Impact: 100.1)
    * *Intent:* /// Resize the pagelist with reflow by adding or removing columns.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3262`, `structural_boundaries: 984`, `args: 116`, `func_start: 116`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1670`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 6`, `duplicate_logic: 30`
* *Architecture:* `api: 116`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 2304`, `doc: 534`, `test: 220`, `immutability_locks: 1697`, `cleanup: 260`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.194
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.007825
  * `Imports (Out-Degree: 2):` quirks.zig, tripwire.zig, std, size.zig, kitty.zig, mach.zig, style.zig, fastmem.zig...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/config/Config.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.09 IQR)
- **Top Global Matches:** file_cluster_8: 15.09, file_cluster_7: 15.096, file_cluster_13: 15.238
- **Magnitude:** 4224.0 | **LOC:** 10888 | **CtrlFlow:** 73.2% | **Authorship Centralization:** 43.8%
- **Risk Profile:** Cognitive Load (8.4631%), Tech Debt (73.7552%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 271.6)
  * `format` (Impact: 173.4)
  * `finalize` (Impact: 119.1)
    * *Intent:* /// Call this once after you are done setting configuration. This /// is idempotent but will waste m...
  * `parseCLI` (Impact: 91.3)
  * `formatEntry` (Impact: 88.1)
    * *Intent:* /// Used by Formatter
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2277`, `structural_boundaries: 832`, `args: 149`, `func_start: 149`, `class_start: 95`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 1056`, `dead_code: 20`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 86`
* *Architecture:* `io: 26`, `api: 235`, `import: 34`
* *Defense:* `safety: 1280`, `doc: 3601`, `test: 135`, `sync_locks: 1`, `immutability_locks: 766`, `cleanup: 172`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.869
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005086
  * `Imports (Out-Degree: 6):` x11_color.zig, comparison.zig, help_strings, formatter.zig, key.zig, ClipboardCodepointMap.zig, path.zig, RepeatableStringMap.zig...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/Surface.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.344 IQR)
- **Top Global Matches:** file_cluster_8: 13.344, file_cluster_7: 13.538, file_cluster_13: 13.702
- **Magnitude:** 3529.66 | **LOC:** 6640 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 45.5%
- **Risk Profile:** Cognitive Load (16.8666%), Tech Debt (12.6159%)
**Top Internal Functions/Classes:**
  * `maybePromptClick` (Impact: 745.8)
  * `mouseButtonCallback` (Impact: 328.7)
    * *Intent:* /// Called for mouse button press/release events. This will return true /// if the mouse event was c...
  * `init` (Impact: 194.0)
    * *Intent:* /// Create a new surface. This must be called from the main thread. The /// pointer to the memory fo...
  * `maybeHandleBinding` (Impact: 172.5)
    * *Intent:* /// Maybe handles a binding for a given event and if so returns the effect. /// Returns null if the ...
  * `keyCallback` (Impact: 143.6)
    * *Intent:* /// Called for any key events. This handles keybindings, encoding and /// sending to the terminal, e...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1598`, `structural_boundaries: 443`, `args: 97`, `func_start: 97`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 246`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 5`, `api: 61`, `concurrency: 11`, `import: 20`
* *Defense:* `safety: 739`, `doc: 368`, `test: 7`, `sync_locks: 106`, `immutability_locks: 408`, `cleanup: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` termio.zig, renderer.zig, config.zig, main.zig, main.zig, main.zig, pty.zig, surface_mouse.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/Terminal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.265 IQR)
- **Top Global Matches:** file_cluster_8: 15.265, file_cluster_0: 15.477, file_cluster_7: 15.499
- **Magnitude:** 3383.54 | **LOC:** 13090 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (45.872%), Tech Debt (8.1232%)
**Top Internal Functions/Classes:**
  * `printAttributes` (Impact: 860.1)
    * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// //...
  * `print` (Impact: 212.6)
  * `printCell` (Impact: 84.4)
  * `cursorLeft` (Impact: 60.3)
    * *Intent:* /// Move the cursor to the left amount cells. If amount is 0, adjust it to 1.
  * `eraseDisplay` (Impact: 60.1)
    * *Intent:* /// Erase the display.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3914`, `structural_boundaries: 1167`, `args: 63`, `func_start: 63`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 1210`, `dead_code: 17`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 74`, `import: 24`
* *Defense:* `safety: 3424`, `doc: 318`, `test: 380`, `sync_locks: 1`, `immutability_locks: 1237`, `cleanup: 674`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004069
  * `Imports (Out-Degree: 9):` sgr.zig, kitty.zig, stream_terminal.zig, style.zig, Tabstops.zig, color.zig, page.zig, size.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/terminal/stream.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.864 IQR)
- **Top Global Matches:** file_cluster_8: 11.864, file_cluster_7: 12.196, file_cluster_13: 12.318
- **Magnitude:** 2560.1 | **LOC:** 3450 | **CtrlFlow:** 83.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (20.4482%), Tech Debt (81.6219%)
**Top Internal Functions/Classes:**
  * `Stream` (Impact: 677.1)
    * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T...
  * `csiDispatch` (Impact: 579.9)
  * `nextNonUtf8` (Impact: 571.2)
    * *Intent:* /// Process the next character and call any callbacks if necessary. /// /// This assumes that we're ...
  * `escDispatch` (Impact: 131.7)
  * `nextSliceCapped` (Impact: 45.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 135`, `args: 68`, `func_start: 67`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 134`, `dead_code: 3`, `planned_debt: 9`, `duplicate_logic: 30`
* *Architecture:* `api: 91`, `import: 17`
* *Defense:* `safety: 188`, `doc: 67`, `test: 39`, `immutability_locks: 161`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002543
  * `Imports (Out-Degree: 8):` charsets.zig, quirks.zig, device_status.zig, std, ansi.zig, kitty.zig, sgr.zig, device_attributes.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/Screen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.258 IQR)
- **Top Global Matches:** file_cluster_8: 14.258, file_cluster_7: 14.494, file_cluster_0: 14.512
- **Magnitude:** 2476.76 | **LOC:** 10353 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (18.0978%), Tech Debt (11.0806%)
**Top Internal Functions/Classes:**
  * `selectLine` (Impact: 101.6)
    * *Intent:* /// Select the line under the given point. This will select across soft-wrapped /// lines and will o...
  * `clone` (Impact: 92.0)
    * *Intent:* /// is only for read-only operations, it is better to not have any /// hyperlink state. Note that al...
  * `resize` (Impact: 80.8)
    * *Intent:* /// Resize the screen. The rows or cols can be bigger or smaller. /// /// If this returns an error, ...
  * `promptClickLine` (Impact: 70.6)
    * *Intent:* /// Determine the inputs required to move from the cursor to the given /// click location. If the cu...
  * `testWriteString` (Impact: 67.6)
    * *Intent:* /// This is basically a really jank version of Terminal.printString. We /// have to reimplement it h...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2278`, `structural_boundaries: 944`, `args: 63`, `func_start: 63`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 934`, `dead_code: 24`, `planned_debt: 4`, `fragile_debt: 11`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 81`, `import: 21`
* *Defense:* `safety: 1795`, `doc: 383`, `test: 202`, `sync_locks: 1`, `immutability_locks: 1245`, `cleanup: 520`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009248
  * `Imports (Out-Degree: 6):` sgr.zig, kitty.zig, style.zig, fastmem.zig, page.zig, size.zig, formatter.zig, cursor.zig...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/terminal/formatter.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.737 IQR)
- **Top Global Matches:** file_cluster_8: 14.737, file_cluster_13: 14.95, file_cluster_0: 14.981
- **Magnitude:** 2097.68 | **LOC:** 6280 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.5332%), Tech Debt (11.8851%)
**Top Internal Functions/Classes:**
  * `formatWithState` (Impact: 366.3)
  * `writeCodepointWithReplacement` (Impact: 37.9)
  * `formatStyleOpen` (Impact: 37.0)
    * *Intent:* /// Write a string with HTML escaping. Used for escaping href attributes /// and other HTML attribut...
  * `format` (Impact: 34.8)
  * `writeCodepoint` (Impact: 32.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1209`, `structural_boundaries: 1001`, `args: 16`, `func_start: 16`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1402`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 23`, `import: 18`
* *Defense:* `safety: 962`, `doc: 90`, `test: 105`, `immutability_locks: 669`, `cleanup: 402`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` charsets.zig, quirks.zig, std, kitty.zig, hyperlink.zig, point.zig, style.zig, Selection.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/key_encode.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.656 IQR)
- **Top Global Matches:** file_cluster_8: 13.656, file_cluster_13: 13.897, file_cluster_7: 13.899
- **Magnitude:** 2092.62 | **LOC:** 2425 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (65.6911%), Tech Debt (28.0397%)
**Top Internal Functions/Classes:**
  * `legacy` (Impact: 893.3)
    * *Intent:* /// Perform legacy encoding of the key event. "Legacy" in this case /// is referring to the behavior...
  * `kitty` (Impact: 209.9)
    * *Intent:* /// Perform Kitty keyboard protocol encoding of the key event.
  * `pcStyleFunctionKey` (Impact: 90.9)
    * *Intent:* /// Determines whether the key should be encoded in the xterm /// "PC-style Function Key" syntax (ro...
  * `ctrlSeq` (Impact: 78.4)
    * *Intent:* /// Returns the C0 byte for the key event if it should be used. /// This converts a key event into t...
  * `encodeFull` (Impact: 58.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 260`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 571`, `dead_code: 2`, `fragile_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `api: 14`, `import: 9`
* *Defense:* `safety: 280`, `doc: 66`, `test: 87`, `sync_locks: 7`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, function_keys.zig, kitty.zig, key.zig, config.zig, key.zig, Terminal.zig, builtin
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/gtk/class/surface.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.587 IQR)
- **Top Global Matches:** file_cluster_8: 12.587, file_cluster_7: 12.815, file_cluster_13: 12.947
- **Magnitude:** 2087.84 | **LOC:** 4041 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 44.4%
- **Risk Profile:** Cognitive Load (7.7582%), Tech Debt (13.7993%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 221.7)
    * *Intent:* /// Set the clipboard contents.
  * `keyEvent` (Impact: 186.6)
    * *Intent:* /// /// We set some state to note we're in a key event (self.in_keyevent) /// because some of the in...
  * `dtDrop` (Impact: 99.5)
  * `filterSnapPaths` (Impact: 50.2)
    * *Intent:* /// Filter out environment variables that start with forbidden prefixes.
  * `commandFinished` (Impact: 48.3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 689`, `structural_boundaries: 243`, `args: 132`, `func_start: 132`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 80`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 187`, `import: 36`
* *Defense:* `safety: 282`, `doc: 198`, `test: 5`, `sync_locks: 1`, `immutability_locks: 518`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` i18n.zig, build_config.zig, adw, key.zig, gdk, config.zig, surface_child_exited.zig, gtk...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/renderer/generic.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.825 IQR)
- **Top Global Matches:** file_cluster_8: 12.825, file_cluster_7: 12.977, file_cluster_13: 13.006
- **Magnitude:** 2074.58 | **LOC:** 3375 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (11.9006%), Tech Debt (29.742%)
**Top Internal Functions/Classes:**
  * `Renderer` (Impact: 455.9)
    * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the in...
  * `rebuildRow` (Impact: 237.3)
  * `rebuildCells` (Impact: 186.6)
    * *Intent:* /// Convert the terminal state to GPU cells stored in CPU memory. These /// are then synced to the G...
  * `updateFrame` (Impact: 156.0)
    * *Intent:* /// Update the frame data.
  * `drawFrame` (Impact: 134.6)
    * *Intent:* /// Draw the frame to the screen. /// /// If `sync` is true, this will synchronously block until ///...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 654`, `structural_boundaries: 138`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 107`, `dead_code: 20`, `planned_debt: 2`, `duplicate_logic: 12`
* *Architecture:* `io: 2`, `api: 46`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 246`, `doc: 227`, `sync_locks: 34`, `immutability_locks: 245`, `cleanup: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` shadertoy.zig, file_type.zig, cell.zig, image.zig, input.zig, builtin, Surface.zig, renderer.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/datastruct/split_tree.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.821 IQR)
- **Top Global Matches:** file_cluster_8: 13.821, file_cluster_7: 13.977, file_cluster_13: 13.994
- **Magnitude:** 1811.96 | **LOC:** 2368 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (39.1695%), Tech Debt (17.8888%)
**Top Internal Functions/Classes:**
  * `SplitTree` (Impact: 614.7)
    * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(...
  * `formatDiagram` (Impact: 112.2)
  * `split` (Impact: 51.3)
    * *Intent:* /// Insert another tree into this tree at the given node in the /// specified direction. The other t...
  * `nearest` (Impact: 42.0)
    * *Intent:* /// Returns the nearest leaf node (view) in the given direction. /// This does not handle wrapping a...
  * `formatTextInner` (Impact: 35.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 334`, `args: 50`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 435`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 284`, `doc: 155`, `test: 18`, `immutability_locks: 206`, `cleanup: 114`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` quirks.zig, glib, build_config.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/input/Binding.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.822 IQR)
- **Top Global Matches:** file_cluster_8: 13.822, file_cluster_7: 13.938, file_cluster_13: 14.037
- **Magnitude:** 1648.18 | **LOC:** 4848 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (13.0616%), Tech Debt (59.5489%)
**Top Internal Functions/Classes:**
  * `parseAndPutRecurse` (Impact: 119.1)
    * *Intent:* /// Returns the set that was ultimately updated if a binding was /// added. Unbind does not return a...
  * `parse` (Impact: 102.9)
    * *Intent:* /// Parse a single trigger. The input is expected to be ONLY the trigger /// (i.e. in the sequence `...
  * `parse` (Impact: 55.2)
    * *Intent:* /// Parse an action in the format of "key=value" where key is the /// action name and value is the a...
  * `formatEntries` (Impact: 47.0)
    * *Intent:* /// Writes the configuration entries for the binding /// that this value is part of. /// /// The val...
  * `parseParameter` (Impact: 46.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1077`, `structural_boundaries: 325`, `args: 64`, `func_start: 64`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 2`, `state_mutation: 392`, `dead_code: 11`, `planned_debt: 2`, `duplicate_logic: 31`
* *Architecture:* `api: 92`, `import: 12`
* *Defense:* `safety: 665`, `doc: 667`, `test: 88`, `immutability_locks: 427`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002035
  * `Imports (Out-Degree: 1):` quirks.zig, build_config.zig, std, comparison.zig, formatter.zig, key.zig, key_mods.zig, uucode
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/apprt/gtk/class/application.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.61 IQR)
- **Top Global Matches:** file_cluster_8: 12.61, file_cluster_13: 12.837, file_cluster_7: 12.876
- **Magnitude:** 1536.14 | **LOC:** 2957 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 55.6%
- **Risk Profile:** Cognitive Load (10.4028%), Tech Debt (10.1461%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 79.3)
    * *Intent:* /// Creates a new Application instance. /// /// This does a lot more work than a typical class insta...
  * `glibLogWriterFunction` (Impact: 79.0)
    * *Intent:* /// Function used to funnel GLib/GObject/GTK log messages into Zig's logging /// system rather than ...
  * `actionNewWindow` (Impact: 72.6)
    * *Intent:* /// Handle `app.new-window` and `app.new-window-command` GTK actions
  * `performAction` (Impact: 63.0)
    * *Intent:* /// apprt API to perform an action.
  * `run` (Impact: 54.3)
    * *Intent:* /// Run the application. This is a replacement for `gio.Application.run` /// because we want more ti...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 254`, `args: 108`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 103`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 84`, `import: 42`
* *Defense:* `safety: 217`, `doc: 124`, `immutability_locks: 258`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007121
  * `Imports (Out-Degree: 6):` systemd.zig, build_config.zig, gtk_version.zig, adw, App.zig, key.zig, gdk, main.zig...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Ghostty.App.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.185 IQR)
- **Top Global Matches:** file_cluster_8: 11.185, file_cluster_1: 11.678, file_cluster_7: 11.692
- **Magnitude:** 1500.84 | **LOC:** 2241 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 66.7%
- **Risk Profile:** Cognitive Load (26.8525%), Tech Debt (75.5954%)
**Top Internal Functions/Classes:**
  * `commandFinished` (Impact: 63.8)
  * `promptTitle` (Impact: 58.4)
  * `gotoSplit` (Impact: 50.4)
  * `toggleSecureInput` (Impact: 45.6)
  * `toggleFloatWindow` (Impact: 43.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 652`, `structural_boundaries: 294`, `args: 60`, `func_start: 56`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 15`, `duplicate_logic: 2`, `orphaned_logic: 41`
* *Architecture:* `api: 4`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 164`, `doc: 19`, `immutability_locks: 233`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SwiftUI, UserNotifications, GhosttyKit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/font/shaper/coretext.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.8 IQR)
- **Top Global Matches:** file_cluster_8: 14.8, file_cluster_0: 14.924, file_cluster_13: 14.927
- **Magnitude:** 1439.16 | **LOC:** 2679 | **CtrlFlow:** 54.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (66.4158%), Tech Debt (17.2239%)
**Top Internal Functions/Classes:**
  * `shape` (Impact: 115.5)
    * *Intent:* /// Note that this will accumulate garbage in the release pool. The /// caller must ensure you're pr...
  * `debugPositions` (Impact: 108.5)
  * `getFont` (Impact: 58.4)
    * *Intent:* /// Get an attr dict for a font from a specific index. /// These items are cached, do not retain or ...
  * `init` (Impact: 33.5)
    * *Intent:* /// The cell_buf argument is the buffer to use for storing shaped results. /// This should be at lea...
  * `testShaperWithDiscoveredFont` (Impact: 23.0)
    * *Intent:* /// Return a fully initialized shaper by discovering a named font on the system.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 620`, `structural_boundaries: 516`, `args: 19`, `func_start: 19`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 945`, `dead_code: 5`, `fragile_debt: 2`, `duplicate_logic: 4`
* *Architecture:* `api: 14`, `concurrency: 7`, `import: 8`
* *Defense:* `safety: 514`, `doc: 46`, `test: 29`, `sync_locks: 3`, `immutability_locks: 188`, `cleanup: 167`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` main.zig, builtin, quirks.zig, std, macos, main.zig, main.zig, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/embedded.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.879 IQR)
- **Top Global Matches:** file_cluster_8: 12.879, file_cluster_7: 13.043, file_cluster_13: 13.102
- **Magnitude:** 1378.84 | **LOC:** 2232 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (6.7639%), Tech Debt (74.2402%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 64.5)
  * `CGSDefaultConnectionForThread` (Impact: 39.0)
  * `ghostty_surface_quicklook_font` (Impact: 28.0)
    * *Intent:* /// This returns a CTFontRef that should be used for quicklook /// highlighted text. This is always ...
  * `cursorPosCallback` (Impact: 26.3)
  * `init` (Impact: 25.1)
    * *Intent:* /// Initialize a Platform a tag and configuration from the C ABI.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 170`, `args: 148`, `func_start: 142`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 69`, `dead_code: 5`, `duplicate_logic: 27`
* *Architecture:* `io: 2`, `api: 214`, `import: 16`
* *Defense:* `safety: 186`, `doc: 185`, `sync_locks: 9`, `immutability_locks: 201`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` renderer.zig, main.zig, quirks.zig, std, dcimgui, main.zig, App.zig, main.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/page.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.625 IQR)
- **Top Global Matches:** file_cluster_8: 13.625, file_cluster_7: 13.752, file_cluster_13: 13.838
- **Magnitude:** 1354.48 | **LOC:** 3919 | **CtrlFlow:** 75.4% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (18.662%), Tech Debt (17.5095%)
**Top Internal Functions/Classes:**
  * `clonePartialRowFrom` (Impact: 145.4)
    * *Intent:* /// Clone a single row from another page into this page, supporting /// partial copy. cloneRowFrom c...
  * `verifyIntegrity` (Impact: 134.3)
    * *Intent:* /// Verifies the integrity of the page data. This is not fast, /// but it is useful for assertions, ...
  * `clearCells` (Impact: 60.1)
    * *Intent:* /// Clear the cells in the given row. This will reclaim memory used /// by graphemes and styles. Not...
  * `moveCells` (Impact: 51.4)
    * *Intent:* /// Move a cell from one location to another. This will replace the /// previous contents with a bla...
  * `exactRowCapacity` (Impact: 47.3)
    * *Intent:* /// Compute the exact capacity required to store a range of rows from /// this page. /// /// The ret...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 795`, `structural_boundaries: 259`, `args: 57`, `func_start: 57`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 74`, `state_mutation: 374`, `dead_code: 10`, `planned_debt: 1`, `duplicate_logic: 8`
* *Architecture:* `io: 2`, `api: 87`, `import: 12`
* *Defense:* `safety: 407`, `doc: 374`, `test: 51`, `immutability_locks: 463`, `cleanup: 77`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` bitmap_allocator.zig, quirks.zig, std, size.zig, kitty.zig, style.zig, fastmem.zig, color.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/stream_terminal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.733 IQR)
- **Top Global Matches:** file_cluster_8: 14.733, file_cluster_13: 14.858, file_cluster_0: 14.952
- **Magnitude:** 1326.84 | **LOC:** 2072 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (75.5261%), Tech Debt (40.7263%)
**Top Internal Functions/Classes:**
  * `deviceStatus` (Impact: 636.5)
  * `vtFallible` (Impact: 45.8)
  * `reportDeviceAttributes` (Impact: 12.9)
  * `writePty` (Impact: 5.4)
  * `bell` (Impact: 5.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 386`, `args: 68`, `func_start: 60`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 529`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 9`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 325`, `doc: 41`, `test: 65`, `immutability_locks: 161`, `cleanup: 170`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.918
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002713
  * `Imports (Out-Degree: 6):` color.zig, size_report.zig, color.zig, std, stream.zig, device_attributes.zig, Terminal.zig, csi.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/hash_map.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.693 IQR)
- **Top Global Matches:** file_cluster_8: 13.693, file_cluster_16: 13.74, file_cluster_13: 13.767
- **Magnitude:** 1311.52 | **LOC:** 1541 | **CtrlFlow:** 68.9% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (35.1424%), Tech Debt (35.8122%)
**Top Internal Functions/Classes:**
  * `HashMapUnmanaged` (Impact: 450.5)
    * *Intent:* /// Fork of stdlib.HashMap as of Zig 0.12 modified to use offsets for /// the key/values pointer. Th...
  * `getOrPutAssumeCapacityAdapted` (Impact: 35.1)
  * `getIndex` (Impact: 28.1)
    * *Intent:* /// Find the index containing the data for the given key. /// Whether this function returns null is ...
  * `getOrPutContextAdapted` (Impact: 18.7)
  * `OffsetHashMap` (Impact: 15.6)
    * *Intent:* /// A HashMap type that uses offsets rather than pointers, making it /// possible to efficiently mov...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 393`, `structural_boundaries: 177`, `args: 80`, `func_start: 80`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 42`, `state_mutation: 223`, `dead_code: 2`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `api: 86`, `import: 5`
* *Defense:* `safety: 173`, `doc: 106`, `test: 24`, `immutability_locks: 228`, `cleanup: 25`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.48
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003052
  * `Imports (Out-Degree: 0):` size.zig, quirks.zig, std
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_0` (Drift: 13.042 IQR)
- **Top Global Matches:** file_cluster_0: 13.042, file_cluster_13: 13.129, file_cluster_8: 13.139
- **Magnitude:** 1303.3 | **LOC:** 2352 | **CtrlFlow:** 61.3% | **Authorship Centralization:** 42.9%
- **Risk Profile:** Cognitive Load (42.1583%), Tech Debt (95.8994%)
**Top Internal Functions/Classes:**
  * `performKeyEquivalent` (Impact: 280.0)
  * `menu` (Impact: 221.2)
  * `attributedSubstring` (Impact: 137.1)
  * `setCursorShape` (Impact: 45.1)
  * `insertText` (Impact: 43.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 266`, `structural_boundaries: 168`, `args: 52`, `func_start: 41`, `class_start: 4`
* *Risk/State:* `state_mutation: 138`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 24`
* *Architecture:* `io: 1`, `api: 22`, `concurrency: 10`, `import: 6`
* *Defense:* `safety: 53`, `doc: 81`, `sync_locks: 1`, `immutability_locks: 95`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GhosttyKit, Combine, SwiftUI, AppKit, CoreText, UserNotifications
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `macos/Sources/Features/Terminal/TerminalController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.285 IQR)
- **Top Global Matches:** file_cluster_17: 12.285, file_cluster_0: 12.429, file_cluster_8: 12.463
- **Magnitude:** 1298.12 | **LOC:** 1665 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 85.7%
- **Risk Profile:** Cognitive Load (31.8987%), Tech Debt (94.6908%)
**Top Internal Functions/Classes:**
  * `newWindow` (Impact: 494.8)
  * `registerUndoForCloseWindow` (Impact: 312.9)
  * `onMoveTab` (Impact: 118.7)
  * `closeOtherTabs` (Impact: 35.1)
  * `closeTabsOnTheRight` (Impact: 34.9)
    * *Intent:* /// Surface-level config will be updated in
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 112`, `args: 42`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `dead_code: 1`, `fragile_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 8`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 71`, `doc: 40`, `immutability_locks: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` GhosttyKit, Cocoa, Combine, SwiftUI, Foundation
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/font/shaper/harfbuzz.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_17` (Drift: 17.356 IQR)
- **Top Global Matches:** file_cluster_17: 17.356, file_cluster_0: 17.368, file_cluster_9: 17.406
- **Magnitude:** 1153.84 | **LOC:** 2173 | **CtrlFlow:** 53.7% | **Authorship Centralization:** 50.0%
- **Risk Profile:** Cognitive Load (69.2619%), Tech Debt (10.2916%)
**Top Internal Functions/Classes:**
  * `debugPositions` (Impact: 88.7)
  * `shape` (Impact: 56.7)
    * *Intent:* /// Shape the given text run. The text run must be the immediately previous /// text run that was it...
  * `testShaperWithFont` (Impact: 35.3)
  * `testShaperWithDiscoveredFont` (Impact: 33.9)
  * `init` (Impact: 17.2)
    * *Intent:* /// The cell_buf argument is the buffer to use for storing shaped results. /// This should be at lea...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 529`, `structural_boundaries: 456`, `args: 13`, `func_start: 13`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 843`, `dead_code: 66`, `duplicate_logic: 2`
* *Architecture:* `api: 15`, `import: 6`
* *Defense:* `safety: 437`, `doc: 27`, `test: 34`, `sync_locks: 6`, `immutability_locks: 141`, `cleanup: 145`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 2.01
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003052
  * `Imports (Out-Degree: 0):` harfbuzz, quirks.zig, std, main.zig, main.zig, main.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/terminal/style.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.581 IQR)
- **Top Global Matches:** file_cluster_8: 13.581, file_cluster_13: 13.677, file_cluster_7: 13.753
- **Magnitude:** 1151.22 | **LOC:** 1079 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (37.7111%), Tech Debt (37.8294%)
**Top Internal Functions/Classes:**
  * `formatColor` (Impact: 393.4)
  * `formatColor` (Impact: 301.3)
  * `format` (Impact: 64.6)
    * *Intent:* /// Formatting to make debug logs easier to read /// by only including non-default attributes.
  * `format` (Impact: 57.6)
  * `fg` (Impact: 38.2)
    * *Intent:* /// Returns the fg color for a cell with this style given the palette /// and various configuration ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 130`, `args: 20`, `func_start: 20`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 191`, `dead_code: 1`, `duplicate_logic: 7`
* *Architecture:* `api: 25`, `import: 7`
* *Defense:* `safety: 169`, `doc: 72`, `test: 37`, `immutability_locks: 135`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quirks.zig, std, sgr.zig, color.zig, page.zig, ref_counted_set.zig, size.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/args.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.902 IQR)
- **Top Global Matches:** file_cluster_8: 13.902, file_cluster_11: 13.945, file_cluster_13: 14.027
- **Magnitude:** 1072.62 | **LOC:** 1628 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8535%), Tech Debt (49.2759%)
**Top Internal Functions/Classes:**
  * `parseIntoField` (Impact: 191.0)
    * *Intent:* /// Parse a single key/value pair into the destination type T. /// /// This may result in allocation...
  * `parse` (Impact: 141.1)
    * *Intent:* /// "DiagnosticList" and any diagnostic messages will be added to that list. /// When diagnostics ar...
  * `next` (Impact: 109.0)
  * `parseAutoStruct` (Impact: 77.5)
  * `parseTaggedUnion` (Impact: 32.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 447`, `structural_boundaries: 203`, `args: 29`, `func_start: 28`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 264`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 8`
* *Architecture:* `api: 29`, `import: 5`
* *Defense:* `safety: 256`, `doc: 78`, `test: 36`, `immutability_locks: 214`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` quirks.zig, CommaSplitter.zig, std, main.zig, diagnostics.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `macos/Sources/Helpers/Private/Dock.swift` (SWIFT) | Magnitude: 19.76 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 12, structural_boundaries: 10, pointers: 4
- `macos/Sources/Features/App Intents/CommandPaletteIntent.swift` (SWIFT) | Magnitude: 22.64 | Delta: **0.04 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 11, state_mutation: 8, branch: 6
- `macos/Sources/Features/App Intents/KeybindIntent.swift` (SWIFT) | Magnitude: 22.6 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 12, state_mutation: 8, branch: 6
- `macos/Tests/Splits/SplitTreeTests.swift` (SWIFT) | Magnitude: 469.72 | Delta: **0.05 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 519, immutability_locks: 167, branch: 148, test: 146
- `macos/Sources/Ghostty/Ghostty.Surface.swift` (SWIFT) | Magnitude: 51.98 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 66, doc: 60, structural_boundaries: 17, args: 11

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/stb/stb_image.h` (C) | Magnitude: 5741.1 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3270, indent_spaces: 2524, pointers: 1126, branch: 894
- `src/shell-integration/bash/bash-preexec.sh` (SHELL) | Magnitude: 261.74 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 141, branch: 101, state_mutation: 101, structural_boundaries: 38
- `macos/Sources/Helpers/CodableBridge.swift` (SWIFT) | Magnitude: 34.64 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 12, structural_boundaries: 10, safety: 6
- `src/cli/action.zig` (ZIG) | Magnitude: 148.26 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 205, branch: 78, encapsulation: 54, globals: 52

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `snap/local/launcher` (SHELL) | Magnitude: 96.26 | Delta: **0.079 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 49, structural_boundaries: 22, api: 17, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/config.zig` (ZIG) | Magnitude: 58.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 46, immutability_locks: 46, api: 42, import: 14
- `src/font/SharedGrid.zig` (ZIG) | Magnitude: 267.42 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 336, branch: 109, globals: 71, encapsulation: 70
- `pkg/harfbuzz/main.zig` (ZIG) | Magnitude: 33.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 26, immutability_locks: 26, api: 18, import: 12
- `macos/Sources/Features/App Intents/GetTerminalDetailsIntent.swift` (SWIFT) | Magnitude: 49.56 | Delta: **0.006 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 48, structural_boundaries: 26, branch: 22, state_mutation: 15
- `pkg/macos/text/ext.c` (C) | Magnitude: 6.56 | Delta: **0.007 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: api: 4, indent_spaces: 4, pointers: 2, structural_boundaries: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/terminal/c/cell.zig` (ZIG) | Magnitude: 72.46 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 32, doc: 30, branch: 25
- `macos/Sources/Helpers/Extensions/Optional+Extension.swift` (SWIFT) | Magnitude: 20.28 | Delta: **0.008 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, branch: 6, structural_boundaries: 4, generics: 2
- `src/unicode/lut.zig` (ZIG) | Magnitude: 234.6 | Delta: **0.028 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 144, branch: 52, safety: 28, immutability_locks: 26
- `src/apprt/gtk/ext.zig` (ZIG) | Magnitude: 59.62 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, immutability_locks: 22, branch: 20, globals: 17
- `src/apprt/gtk/class.zig` (ZIG) | Magnitude: 265.48 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 322, doc: 88, branch: 44, immutability_locks: 43

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/font/shaper/harfbuzz.zig` (ZIG) | Magnitude: 1153.84 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1774, state_mutation: 843, branch: 529, structural_boundaries: 456
- `macos/Sources/Features/AppleScript/ScriptWindow.swift` (SWIFT) | Magnitude: 128.24 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 130, branch: 82, doc: 74, structural_boundaries: 65
- `macos/Sources/Features/App Intents/QuickTerminalIntent.swift` (SWIFT) | Magnitude: 29.9 | Delta: **0.034 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 19, branch: 11, structural_boundaries: 10, state_mutation: 7
- `macos/Sources/Helpers/Extensions/NSWindow+Extension.swift` (SWIFT) | Magnitude: 10.26 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, doc: 12, branch: 7, structural_boundaries: 7
- `macos/Sources/Features/Terminal/Window Styles/TerminalWindow.swift` (SWIFT) | Magnitude: 279.38 | Delta: **0.123 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 433, branch: 135, structural_boundaries: 95, immutability_locks: 68

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `macos/Sources/Helpers/NonDraggableHostingView.swift` (SWIFT) | Magnitude: 13.08 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 3, ui_framework: 2, generics: 2
- `macos/Sources/Helpers/HostingWindow.swift` (SWIFT) | Magnitude: 18.22 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, state_mutation: 3, class_start: 2
- `macos/Sources/Helpers/Extensions/NSView+Extension.swift` (SWIFT) | Magnitude: 154.52 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 73, indent_tabs: 63, structural_boundaries: 50, branch: 45
- `macos/Sources/Features/QuickTerminal/QuickTerminalSpaceBehavior.swift` (SWIFT) | Magnitude: 16.16 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, branch: 10, structural_boundaries: 8, ui_framework: 4
- `macos/Sources/Ghostty/Surface View/SurfaceScrollView.swift` (SWIFT) | Magnitude: 89.34 | Delta: **0.032 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, doc: 70, structural_boundaries: 25, branch: 18

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/benchmark/GraphemeBreak.zig` (ZIG) | Magnitude: 129.44 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, encapsulation: 40, state_mutation: 37, globals: 37
- `macos/Sources/Features/AppleScript/AppDelegate+AppleScript.swift` (SWIFT) | Magnitude: 74.92 | Delta: **0.1 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 77, indent_spaces: 46, branch: 28, structural_boundaries: 27
- `src/benchmark/IsSymbol.zig` (ZIG) | Magnitude: 127.12 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, encapsulation: 39, globals: 35, state_mutation: 33
- `macos/Sources/Features/App Intents/Entities/TerminalEntity.swift` (SWIFT) | Magnitude: 106.78 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 39, structural_boundaries: 35, concurrency: 34
- `macos/Sources/Features/App Intents/IntentPermission.swift` (SWIFT) | Magnitude: 25.64 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 24, indent_spaces: 24, branch: 8, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/terminal/cursor.zig` (ZIG) | Magnitude: 16.28 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, doc: 8, branch: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pkg/macos/text/frame.zig` (ZIG) | Magnitude: 15.88 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, globals: 8, immutability_locks: 8, api: 7
- `src/lib/string.zig` (ZIG) | Magnitude: 9.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 5, immutability_locks: 4, indent_spaces: 3, safety: 2
- `src/main_c.zig` (ZIG) | Magnitude: 99.4 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, branch: 56, immutability_locks: 56, globals: 41
- `macos/Sources/Ghostty/Surface View/SurfaceProgressBar.swift` (SWIFT) | Magnitude: 34.82 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 27, branch: 21, state_mutation: 18
- `pkg/macos/foundation.zig` (ZIG) | Magnitude: 37.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: globals: 32, immutability_locks: 32, api: 22, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/freetype/tag.zig` (ZIG) | Magnitude: 12.1 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 12, branch: 4, api: 4, structural_boundaries: 3
- `src/simd/codepoint_width.zig` (ZIG) | Magnitude: 12.66 | Delta: **0.075 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 23, indent_spaces: 15, explicit_casts: 14, safety: 13
- `Makefile` (MAKEFILE) | Magnitude: 19.38 | Delta: **0.076 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_tabs: 10, func_start: 6, api: 4, cleanup: 3
- `src/stb/stb_image_resize.h` (C) | Magnitude: 10.52 | Delta: **0.277 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: doc: 70, ownership: 6, sec_high_risk_execution: 6

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/config/Config.zig` -> Churn: **75.33%** | Cog Load: 8.4631% | Debt: 73.7552%
- `src/terminal/stream_terminal.zig` -> Churn: **63.75%** | Cog Load: 75.5261% | Debt: 40.7263%
- `macos/Sources/Features/Terminal/TerminalController.swift` -> Churn: **61.69%** | Cog Load: 31.8987% | Debt: 94.6908%
- `src/shell-integration/bash/ghostty.bash` -> Churn: **58.9%** | Cog Load: 87.5892% | Debt: 20.365%
- `src/terminal/c/formatter.zig` -> Churn: **55.29%** | Cog Load: 58.0653% | Debt: 31.9909%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/terminal/PageList.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 4514.92
- `src/terminal/Terminal.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 3383.54
- `src/terminal/stream.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 2560.1
- `src/terminal/formatter.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 2097.68
- `src/renderer/generic.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 2074.58

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/terminal/PageList.zig` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 62.3304%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/os/macos.zig` -> **Severity: 1.079** (Embedded: 0.0222 * Error Risk: 48.5445%)
- `pkg/opengl/glad.zig` -> **Severity: 1.058** (Embedded: 0.0122 * Error Risk: 86.6541%)
- `src/terminal/build_options.zig` -> **Severity: 0.966** (Embedded: 0.0159 * Error Risk: 60.7717%)
- `src/terminal/charsets.zig` -> **Severity: 0.522** (Embedded: 0.0073 * Error Risk: 71.278%)
- `src/renderer/metal/api.zig` -> **Severity: 0.422** (Embedded: 0.0081 * Error Risk: 51.8758%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/apprt/gtk.zig` -> **Severity: 2193.5** (Blast Radius: 21.935 * Doc Risk: 100.0%)
- `src/terminal/lib.zig` -> **Severity: 1176.6** (Blast Radius: 11.766 * Doc Risk: 100.0%)
- `src/os/macos.zig` -> **Severity: 1104.431** (Blast Radius: 12.539 * Doc Risk: 88.0797%)
- `pkg/opengl/glad.zig` -> **Severity: 816.607** (Blast Radius: 8.183 * Doc Risk: 99.7931%)
- `src/build_config.zig` -> **Severity: 721.697** (Blast Radius: 7.354 * Doc Risk: 98.1366%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
