# ARCHITECTURAL_BRIEF: ghostty
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/ghostty` |
| **Timestamp** | `2026-08-03T20:55:25.524392+00:00` |
| **Scan Duration** | `8.6s` |
| **Git Branch** | `main` |
| **Git Commit** | `debcffbadb75221a030319c075fae12cfe114176` |
| **Git Remote** | `https://github.com/ghostty-org/ghostty` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 907 malicious artifacts.

## 1. SYSTEM ROLE & PHILOSOPHY
> You are analyzing software architecture through the lens of GitGalaxy Static Application Security Testing (SAST). GitGalaxy translates the non-visual architecture of repositories into measurable technical metrics.
> 
> **CORE DIRECTIVES:**
> 1. **Measure Risk, Not Quality:** Do not judge. We measure Risk Exposure (e.g., Cognitive Load Exposure). Frame all insights as blameless, objective observations. High risk highlights where the architecture might be drifting into fragile territory, not developer incompetence.
> 2. **The Physical Reality Rule:** Base your analysis strictly on the provided Structural Signatures (regex hit counts). Do not hallucinate meaning.
> 3. **Risk vs. Defense:** Code is a balance. A file with high `flux` (state mutation) is risky unless balanced by `freeze_hits` (immutability). High `danger` is brittle unless wrapped in `safety`.
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
> **Architectural Drift Z-Score:** `5.249`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 546 | 55.5% |
| file_cluster_13 | 305 | 31.0% |
| file_cluster_2 | 19 | 1.9% |
| file_cluster_17 | 16 | 1.6% |
| file_cluster_0 | 15 | 1.5% |
| file_cluster_16 | 11 | 1.1% |
| file_cluster_4 | 7 | 0.7% |
| file_cluster_9 | 4 | 0.4% |
| file_cluster_11 | 3 | 0.3% |
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
| Cognitive Load Exposure | 0.0 | 99.9 | 19.1 | 12.3 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.3 | 21.5 | 5.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 19.7 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 35.4 | 2.8 | 80.0 |
| API Exposure | 0.0 | 18.0 | 3.3 | 1.6 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 26.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 2.3 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 91.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 2.7 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.1 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 59.1 | 63.1 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 43.7 | 8.7 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 11.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.4 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.0 | 0.0 | 0.0 |
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

- `legacy` (@ `src/input/key_encode.zig`) -> Impact: **4962.9** | LOC: 1587
  * *Intent:* /// Perform legacy encoding of the key event. "Legacy" in this case /// is referring to the behavior of traditional terminals, plus /// xterm's `modif...
- `SplitTree` (@ `src/datastruct/split_tree.zig`) -> Impact: **3914.7** | LOC: 1294
  * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(*const View, *const View) bool` - Check if two vie...
- `parse` (@ `src/terminal/osc/parsers/osc9.zig`) -> Impact: **3706.2** | LOC: 1135
  * *Intent:* /// Parse OSC 9, which could be an iTerm2 notification or a ConEmu extension.
- `format` (@ `src/terminal/tmux/output.zig`) -> Impact: **3481.4** | LOC: 533
  * *Intent:* /// Format a set of variables into the proper format string for tmux /// that we can handle with `parseFormatStruct`.
- `newWindow` (@ `macos/Sources/Features/Terminal/TerminalController.swift`) -> Impact: **3266.8** | LOC: 656
- `encode` (@ `src/terminal/kitty/graphics_command.zig`) -> Impact: **3139.4** | LOC: 954
- `Renderer` (@ `src/renderer/generic.zig`) -> Impact: **2845.8** | LOC: 1197
  * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the input buffers and textures and /// : the vertex/frag...
- `printAttributes` (@ `src/terminal/Terminal.zig`) -> Impact: **2834.7** | LOC: 1406
  * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// /// Boolean attributes are printed first, followed b...
- `parse` (@ `src/terminal/osc/parsers/semantic_prompt.zig`) -> Impact: **2646.3** | LOC: 965
  * *Intent:* /// Parse OSC 133, semantic prompts
- `formatColor` (@ `src/terminal/style.zig`) -> Impact: **2539.2** | LOC: 716

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `DecodeUTF8UntilControlSeqImpl` (@ `src/simd/vt.cpp`) -> **O(2^N) [Recursive]**
- `DecodeUTF8UntilControlSeq` (@ `src/simd/vt.cpp`) -> **O(2^N) [Recursive]**
- `DecodeUTF8` (@ `src/simd/vt.cpp`) -> **O(2^N) [Recursive]**
  * *Intent:* // Decode the UTF-8 text in input into output. Returns the number of decoded // characters. This function assumes output is large enough. // // This f...
- `init` (@ `src/apprt/embedded.zig`) -> **O(2^N) [Recursive]**
- `pin` (@ `src/apprt/embedded.zig`) -> **O(2^N) [Recursive]**
- `Common` (@ `src/apprt/gtk/class.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Common methods for all GObject classes we create.
- `run` (@ `src/apprt/gtk/class/application.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Run the application. This is a replacement for `gio.Application.run` /// because we want more tight control over our event loop so we can /// inte...
- `promptTitle` (@ `src/apprt/gtk/class/application.zig`) -> **O(2^N) [Recursive]**
- `present` (@ `src/apprt/gtk/class/dialog.zig`) -> **O(2^N) [Recursive]**
- `makePayload` (@ `src/apprt/gtk/class/global_shortcuts.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Construct the payload expected by the XDG portal call.

### Highest Data Gravity (Database Complexity)
- `stbi__decode_jpeg_image` (@ `src/stb/stb_image.h`) -> DB Complexity: **480**
- `Anonymous_Block_[Truncated]` (@ `src/shell-integration/bash/ghostty.bash`) -> DB Complexity: **210**
  * *Intent:* # This program is free software: you can redistribute it and/or modify # it under the terms of the GNU General Public License as published by # the Fr...
- `deviceStatus` (@ `src/terminal/stream_terminal.zig`) -> DB Complexity: **155**
- `stbi__idct_block` (@ `src/stb/stb_image.h`) -> DB Complexity: **144**
  * *Intent:* // // - If you define STBI_MAX_DIMENSIONS, stb_image will reject images greater // than that size (in either width or height) without further processi...
- `legacy` (@ `src/input/key_encode.zig`) -> DB Complexity: **125**
  * *Intent:* /// Perform legacy encoding of the key event. "Legacy" in this case /// is referring to the behavior of traditional terminals, plus /// xterm's `modif...
- `Anonymous_Block_[Truncated]` (@ `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish`) -> DB Complexity: **100**
  * *Intent:* # If we don't have our own data dir then we don't need to do anything.
- `__bp_trim_whitespace` (@ `src/shell-integration/bash/bash-preexec.sh`) -> DB Complexity: **77**
  * *Intent:* # Trims leading and trailing whitespace from $2 and writes it to the variable # name passed as $1
- `formatColor` (@ `src/terminal/style.zig`) -> DB Complexity: **77**
- `parse` (@ `src/terminal/osc/parsers/semantic_prompt.zig`) -> DB Complexity: **73**
  * *Intent:* /// Parse OSC 133, semantic prompts
- `stbi__parse_png_file` (@ `src/stb/stb_image.h`) -> DB Complexity: **70**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/terminal` | 45 | 52182.04 | 19.74% | 18.61% |
| `src/apprt/gtk/class` | 22 | 19198.26 | 7.68% | 64.37% |
| `src/config` | 19 | 15816.94 | 19.45% | 30.51% |
| `src/input` | 16 | 15792.4 | 13.29% | 15.31% |
| `src` | 28 | 14904.84 | 12.65% | 22.4% |
| `src/renderer` | 17 | 13626.72 | 14.99% | 14.37% |
| `src/terminal/osc/parsers` | 15 | 11464.34 | 40.68% | 6.2% |
| `src/cli` | 24 | 11128.24 | 26.98% | 12.04% |
| `src/font` | 19 | 11116.34 | 11.92% | 25.06% |
| `src/termio` | 9 | 8746.38 | 15.1% | 29.69% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `.github/scripts/check-translations.sh` -> **100.0%** Exposure
- `snap/local/launcher` -> **100.0%** Exposure
- `pkg/macos/text/ext.c` -> **100.0%** Exposure
- `pkg/highway/bridge.cpp` -> **100.0%** Exposure
- `pkg/utfcpp/empty.cc` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/shell-integration/bash/bash-preexec.sh` -> **100.0%** Exposure
- `include/ghostty/vt/build_info.h` -> **100.0%** Exposure
- `include/ghostty/vt/osc.h` -> **100.0%** Exposure
- `include/ghostty/vt/screen.h` -> **100.0%** Exposure
- `include/ghostty/vt/sgr.h` -> **100.0%** Exposure
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

### Exploit Generation Surface
- `example/wasm-key-encode/index.html` -> **100.0%** Exposure
- `example/wasm-sgr/index.html` -> **100.0%** Exposure
- `macos/Sources/App/macOS/AppDelegate.swift` -> **100.0%** Exposure
- `macos/Sources/Features/App Intents/InputIntent.swift` -> **100.0%** Exposure
- `macos/Sources/Features/App Intents/NewTerminalIntent.swift` -> **100.0%** Exposure
### Weaponizable Injection Vectors
- `src/shell-integration/bash/ghostty.bash` -> **100.0%** Exposure
- `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish` -> **100.0%** Exposure
- `include/ghostty/vt/terminal.h` -> **100.0%** Exposure
- `include/ghostty/vt/modes.h` -> **99.9978%** Exposure
- `src/terminal/kitty/graphics_exec.zig` -> **2.2819%** Exposure
### Raw Memory Manipulation
- `src/stb/stb_image.h` -> **10.0%** Exposure
- `pkg/macos/text/font.zig` -> **0.9046%** Exposure
- `pkg/macos/graphics/context.zig` -> **0.1213%** Exposure
- `pkg/macos/iosurface/iosurface.zig` -> **0.0116%** Exposure
- `pkg/macos/text/run.zig` -> **0.0046%** Exposure
### Algorithmic DoS Exposure
- `src/shell-integration/bash/bash-preexec.sh` -> **100.0%** Exposure
- `src/shell-integration/bash/ghostty.bash` -> **100.0%** Exposure
- `src/shell-integration/fish/vendor_conf.d/ghostty-shell-integration.fish` -> **100.0%** Exposure
- `example/c-vt-cmake-static/src/main.c` -> **100.0%** Exposure
- `example/c-vt-cmake/src/main.c` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `13` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `2754` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `macos/Sources/App/macOS/AppDelegate.swift` (SWIFT) -> Cumulative Risk: **908.58**
- **Archetype:** `file_cluster_0` (Distance: 12.67 IQR)
- **Magnitude:** 1229.38 | **LOC:** 1404 | **CtrlFlow:** 61.5% | **Authorship Centralization:** 50.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `toggleVisibility` (Impact: 285.2), `applicationDidFinishLaunching` (Impact: 101.7), `applicationShouldTerminate` (Impact: 88.8)

### 2. `macos/Sources/Features/Terminal/Window Styles/TerminalWindow.swift` (SWIFT) -> Cumulative Risk: **796.48**
- **Archetype:** `file_cluster_17` (Distance: 12.164 IQR)
- **Magnitude:** 539.68 | **LOC:** 843 | **CtrlFlow:** 67.2% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Logic Bomb (100.0%), Algorithmic Dos (99.6286%)
- **Heaviest Functions:** `configureTabContextMenuIfNeeded` (Impact: 51.9), `renameTabFromContextMenu` (Impact: 40.7), `appendTabModifierSection` (Impact: 39.5)

### 3. `macos/Sources/Ghostty/Surface View/SurfaceView_AppKit.swift` (SWIFT) -> Cumulative Risk: **769.92**
- **Archetype:** `file_cluster_0` (Distance: 13.027 IQR)
- **Magnitude:** 1707.8 | **LOC:** 2352 | **CtrlFlow:** 68.0% | **Authorship Centralization:** 42.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), State Flux (94.5131%)
- **Heaviest Functions:** `performKeyEquivalent` (Impact: 794.3), `keyDown` (Impact: 128.3), `setCursorShape` (Impact: 108.8)

### 4. `macos/Sources/Features/Terminal/BaseTerminalController.swift` (SWIFT) -> Cumulative Risk: **760.11**
- **Archetype:** `file_cluster_0` (Distance: 12.826 IQR)
- **Magnitude:** 1729.9 | **LOC:** 1549 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `splitDidDrop` (Impact: 143.0), `replaceSurfaceTree` (Impact: 122.9), `didChangeScreenParametersNotification` (Impact: 97.2)

### 5. `macos/Sources/Ghostty/Surface View/InspectorView.swift` (SWIFT) -> Cumulative Risk: **751.84**
- **Archetype:** `file_cluster_8` (Distance: 11.811 IQR)
- **Magnitude:** 621.7 | **LOC:** 442 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `scrollWheel` (Impact: 74.5), `onControlInspector` (Impact: 68.0), `init` (Impact: 62.1)

### 6. `src/shell-integration/bash/ghostty.bash` (SHELL) -> Cumulative Risk: **750.52**
- **Archetype:** `file_cluster_13` (Distance: 12.905 IQR)
- **Magnitude:** 633.96 | **LOC:** 325 | **CtrlFlow:** 84.2% | **Authorship Centralization:** 88.9%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Injection Surface (100.0%), State Flux (99.9999%)
- **Heaviest Functions:** `Anonymous_Block_[Truncated]` (Impact: 547.0)

### 7. `macos/GhosttyUITests/GhosttyCustomConfigCase.swift` (SWIFT) -> Cumulative Risk: **747.78**
- **Archetype:** `file_cluster_8` (Distance: 12.079 IQR)
- **Magnitude:** 68.62 | **LOC:** 63 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9295%), State Flux (99.8309%)
- **Heaviest Functions:** `updateConfig` (Impact: 22.8), `ghosttyApplication` (Impact: 15.2), `tearDown` (Impact: 14.1)

### 8. `src/benchmark/CodepointWidth.zig` (ZIG) -> Cumulative Risk: **739.34**
- **Archetype:** `file_cluster_4` (Distance: 13.453 IQR)
- **Magnitude:** 299.76 | **LOC:** 208 | **CtrlFlow:** 61.4% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Concurrency (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `stepTable` (Impact: 63.9), `stepWcwidth` (Impact: 53.5), `stepSimd` (Impact: 44.6)

### 9. `macos/Sources/Ghostty/Surface View/SurfaceView.swift` (SWIFT) -> Cumulative Risk: **738.79**
- **Archetype:** `file_cluster_2` (Distance: 11.991 IQR)
- **Magnitude:** 486.82 | **LOC:** 1281 | **CtrlFlow:** 51.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%), Concurrency (99.9867%)
- **Heaviest Functions:** `updateOSView` (Impact: 221.8), `centerPosition` (Impact: 35.8), `backgroundColor` (Impact: 30.4)

### 10. `macos/Sources/Ghostty/Ghostty.App.swift` (SWIFT) -> Cumulative Risk: **731.3**
- **Archetype:** `file_cluster_8` (Distance: 11.207 IQR)
- **Magnitude:** 5277.74 | **LOC:** 2241 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 66.7%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `promptTitle` (Impact: 394.4), `progressReport` (Impact: 239.8), `commandFinished` (Impact: 213.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/config/Config.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.091 IQR)
- **Top Global Matches:** file_cluster_8: 15.091, file_cluster_7: 15.097, file_cluster_13: 15.239
- **Magnitude:** 10972.3 | **LOC:** 10888 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 43.8%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 21
- **Risk Profile:** Cognitive Load (8.4684%), Tech Debt (73.7552%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 978.8 | O(2^N) | DB: 4)
  * `init` (Impact: 856.2 | O(N^6) | DB: 1)
  * `finalize` (Impact: 773.8 | O(2^N) | DB: 7)
    * *Intent:* /// Call this once after you are done setting configuration. This /// is idempotent but will waste m...
  * `formatEntry` (Impact: 503.8 | O(2^N) | DB: 7)
    * *Intent:* /// Used by Formatter
  * `equalSet` (Impact: 325.0 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2279`, `structural_boundaries: 832`, `args: 149`, `func_start: 149`, `class_start: 95`
* *Risk/State:* `safety_bypasses: 60`, `state_mutation: 1056`, `dead_code: 20`, `planned_debt: 3`, `fragile_debt: 7`, `duplicate_logic: 86`
* *Architecture:* `io: 26`, `api: 235`, `import: 34`
* *Defense:* `safety: 1280`, `doc: 3601`, `test: 135`, `sync_locks: 1`, `immutability_locks: 766`, `cleanup: 172`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.869
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.005086
  * `Imports (Out-Degree: 6):` path.zig, ClipboardCodepointMap.zig, help_strings, style.zig, quirks.zig, builtin, color.zig, input.zig...
  * `Imported By (In-Degree: 5):` (Excluded from Brief to save tokens)

### `src/terminal/PageList.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.589 IQR)
- **Top Global Matches:** file_cluster_8: 14.589, file_cluster_7: 14.815, file_cluster_0: 14.908
- **Magnitude:** 10401.12 | **LOC:** 14608 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (21.6108%), Tech Debt (18.7098%)
**Top Internal Functions/Classes:**
  * `scroll` (Impact: 713.6 | O(2^N) | DB: 10)
    * *Intent:* /// Scroll the viewport. This will never create new scrollback, allocate /// pages, etc. This can on...
  * `diagram` (Impact: 660.5 | O(N^6) | DB: 10)
    * *Intent:* /// ... | | /// 50 | foo | /// ... | | /// +--------+ ACTIVE /// 124 | | | 0 /// 125 |Text | | 1 ///...
  * `reflowRow` (Impact: 602.8 | O(2^N) | DB: 3)
    * *Intent:* /// Reflow the provided row in to this cursor.
  * `resizeWithoutReflowGrowCols` (Impact: 587.5 | O(2^N) | DB: 4)
  * `eraseRowBounded` (Impact: 400.9 | O(N^6) | DB: 3)
    * *Intent:* /// A variant of eraseRow that shifts only a bounded number of following /// rows up, filling the sp...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3262`, `structural_boundaries: 984`, `args: 116`, `func_start: 116`, `class_start: 25`
* *Risk/State:* `safety_bypasses: 131`, `state_mutation: 1670`, `dead_code: 12`, `planned_debt: 3`, `fragile_debt: 6`, `duplicate_logic: 30`
* *Architecture:* `api: 116`, `concurrency: 1`, `import: 15`
* *Defense:* `safety: 2304`, `doc: 534`, `test: 220`, `immutability_locks: 1697`, `cleanup: 260`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.194
  * `Choke Point (Betweenness):` 1e-05 | `Ripple Effect (Closeness):` 0.007825
  * `Imports (Out-Degree: 2):` main.zig, highlight.zig, point.zig, quirks.zig, page.zig, std, builtin, size.zig...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/Surface.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.344 IQR)
- **Top Global Matches:** file_cluster_8: 13.344, file_cluster_7: 13.538, file_cluster_13: 13.702
- **Magnitude:** 9905.26 | **LOC:** 6640 | **CtrlFlow:** 78.3% | **Authorship Centralization:** 45.5%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (16.8666%), Tech Debt (12.6159%)
**Top Internal Functions/Classes:**
  * `maybePromptClick` (Impact: 2430.2 | O(N^6) | DB: 14)
  * `mouseButtonCallback` (Impact: 1100.3 | O(N^6))
    * *Intent:* /// Called for mouse button press/release events. This will return true /// if the mouse event was c...
  * `init` (Impact: 1084.9 | O(2^N) | DB: 11)
    * *Intent:* /// Create a new surface. This must be called from the main thread. The /// pointer to the memory fo...
  * `keyCallback` (Impact: 679.5 | O(2^N) | DB: 4)
    * *Intent:* /// Called for any key events. This handles keybindings, encoding and /// sending to the terminal, e...
  * `maybeHandleBinding` (Impact: 575.0 | O(N^6) | DB: 1)
    * *Intent:* /// Maybe handles a binding for a given event and if so returns the effect. /// Returns null if the ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1598`, `structural_boundaries: 443`, `args: 97`, `func_start: 97`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 51`, `state_mutation: 246`, `dead_code: 10`, `planned_debt: 5`, `fragile_debt: 2`, `duplicate_logic: 6`
* *Architecture:* `io: 5`, `api: 61`, `concurrency: 11`, `import: 20`
* *Defense:* `safety: 739`, `doc: 368`, `test: 7`, `sync_locks: 106`, `immutability_locks: 408`, `cleanup: 95`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` termio.zig, apprt.zig, renderer.zig, main.zig, surface_mouse.zig, builtin, main.zig, main.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/Terminal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 15.265 IQR)
- **Top Global Matches:** file_cluster_8: 15.265, file_cluster_0: 15.477, file_cluster_7: 15.499
- **Magnitude:** 8419.84 | **LOC:** 13090 | **CtrlFlow:** 77.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (45.8927%), Tech Debt (8.1232%)
**Top Internal Functions/Classes:**
  * `printAttributes` (Impact: 2834.7 | O(N^6) | DB: 40)
    * *Intent:* /// Print the active attributes as a string. This is used to respond to DECRQSS /// requests. /// //...
  * `print` (Impact: 1376.6 | O(2^N) | DB: 5)
  * `eraseDisplay` (Impact: 382.1 | O(2^N) | DB: 1)
    * *Intent:* /// Erase the display.
  * `insertLines` (Impact: 360.8 | O(2^N) | DB: 5)
    * *Intent:* /// /// This unsets the pending wrap state without wrapping. If the current cursor /// position is o...
  * `deleteLines` (Impact: 348.0 | O(2^N) | DB: 5)
    * *Intent:* /// filled with empty lines. /// /// If the current cursor position is outside of the current scroll...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3916`, `structural_boundaries: 1169`, `args: 63`, `func_start: 63`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 96`, `state_mutation: 1210`, `dead_code: 17`, `planned_debt: 8`, `fragile_debt: 2`
* *Architecture:* `io: 1`, `api: 74`, `import: 24`
* *Defense:* `safety: 3424`, `doc: 318`, `test: 380`, `sync_locks: 1`, `immutability_locks: 1237`, `cleanup: 674`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 1.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004069
  * `Imports (Out-Degree: 9):` page.zig, osc.zig, Screen.zig, mouse.zig, point.zig, quirks.zig, terminal_options, sgr.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/renderer/generic.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.856 IQR)
- **Top Global Matches:** file_cluster_8: 12.856, file_cluster_7: 13.01, file_cluster_13: 13.042
- **Magnitude:** 8077.48 | **LOC:** 3375 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 19
- **Risk Profile:** Cognitive Load (11.578%), Tech Debt (8.1383%)
**Top Internal Functions/Classes:**
  * `Renderer` (Impact: 2845.8 | O(2^N) | DB: 19)
    * *Intent:* /// : one or more `Step`s applied to the same target(s), /// [ Step ] - - - - each describing the in...
  * `rebuildRow` (Impact: 1704.7 | O(N^6) | DB: 7)
  * `rebuildCells` (Impact: 1215.3 | O(2^N) | DB: 3)
    * *Intent:* /// Convert the terminal state to GPU cells stored in CPU memory. These /// are then synced to the G...
  * `drawFrame` (Impact: 854.6 | O(2^N) | DB: 3)
    * *Intent:* /// Draw the frame to the screen. /// /// If `sync` is true, this will synchronously block until ///...
  * `addCursor` (Impact: 218.7 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 655`, `structural_boundaries: 138`, `args: 56`, `func_start: 56`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 75`, `state_mutation: 107`, `dead_code: 20`, `planned_debt: 2`
* *Architecture:* `io: 2`, `api: 41`, `concurrency: 3`, `import: 23`
* *Defense:* `safety: 246`, `doc: 227`, `sync_locks: 34`, `immutability_locks: 245`, `cleanup: 78`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` link.zig, Overlay.zig, xev, quirks.zig, builtin, config.zig, row.zig, input.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/stb/stb_image.h` (C | Tier 4 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.309 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 5.448 IQR)
- **Top Global Matches:** file_cluster_11: 15.309, file_cluster_8: 15.311, file_cluster_0: 15.36
- **Magnitude:** 7549.2 | **LOC:** 7988 | **CtrlFlow:** 68.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 480
- **Risk Profile:** Cognitive Load (67.0747%), Tech Debt (9.3407%)
**Top Internal Functions/Classes:**
  * `stbi__decode_jpeg_image` (Impact: 2002.5 | O(N^6) | DB: 480)
  * `stbi__parse_png_file` (Impact: 266.6 | O(N^4) | DB: 70)
  * `stbi__tga_test` (Impact: 132.7 | O(N^4) | DB: 37)
    * *Intent:* // wide add #define dct_wadd(out, a, b) \
  * `stbi__pic_load_core` (Impact: 131.4 | O(N^6) | DB: 44)
  * `stbi__out_gif_code` (Impact: 117.7 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 894`, `structural_boundaries: 412`, `args: 37`, `func_start: 114`, `class_start: 11`
* *Risk/State:* `safety_bypasses: 58`, `state_mutation: 3276`, `dead_code: 17`, `planned_debt: 1`, `fragile_debt: 4`
* *Architecture:* `io: 11`, `api: 641`
* *Defense:* `safety: 3`, `doc: 62`, `immutability_locks: 38`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.453
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002035
  * `Imports (Out-Degree: 0):` stdarg.h, stddef.h, assert.h, math.h, stdint.h, intrin.h, limits.h, stdio.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/input/key_encode.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.671 IQR)
- **Top Global Matches:** file_cluster_8: 13.671, file_cluster_7: 13.914, file_cluster_13: 13.916
- **Magnitude:** 7024.32 | **LOC:** 2425 | **CtrlFlow:** 68.1% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 125
- **Risk Profile:** Cognitive Load (43.195%), Tech Debt (8.5139%)
**Top Internal Functions/Classes:**
  * `legacy` (Impact: 4962.9 | O(2^N) | DB: 125)
    * *Intent:* /// Perform legacy encoding of the key event. "Legacy" in this case /// is referring to the behavior...
  * `kitty` (Impact: 1404.0 | O(2^N) | DB: 3)
    * *Intent:* /// Perform Kitty keyboard protocol encoding of the key event.
  * `encode` (Impact: 20.9 | O(N^2))
    * *Intent:* /// Encode the key event to the writer in the proper format given /// the options. For example, this...
  * `fromTerminal` (Impact: 8.7 | O(N^3))
    * *Intent:* /// Initialize our options from the terminal state. /// /// Note that `macos_option_as_alt` cannot b...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 556`, `structural_boundaries: 260`, `args: 20`, `func_start: 20`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 80`, `state_mutation: 571`, `dead_code: 2`, `fragile_debt: 1`
* *Architecture:* `api: 13`, `import: 9`
* *Defense:* `safety: 280`, `doc: 66`, `test: 87`, `sync_locks: 7`, `immutability_locks: 73`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, key.zig, builtin, Terminal.zig, key.zig, config.zig, function_keys.zig, kitty.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/gtk/class/surface.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.588 IQR)
- **Top Global Matches:** file_cluster_8: 12.588, file_cluster_7: 12.816, file_cluster_13: 12.947
- **Magnitude:** 6069.94 | **LOC:** 4041 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 44.4%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (7.7582%), Tech Debt (13.7993%)
**Top Internal Functions/Classes:**
  * `set` (Impact: 1441.6 | O(2^N) | DB: 4)
    * *Intent:* /// Set the clipboard contents.
  * `keyEvent` (Impact: 1063.4 | O(2^N))
    * *Intent:* /// /// We set some state to note we're in a key event (self.in_keyevent) /// because some of the in...
  * `dtDrop` (Impact: 337.7 | O(N^6) | DB: 5)
  * `commandFinished` (Impact: 169.3 | O(N^5))
  * `filterSnapPaths` (Impact: 167.1 | O(N^6) | DB: 9)
    * *Intent:* /// Filter out environment variables that start with forbidden prefixes.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 689`, `structural_boundaries: 243`, `args: 132`, `func_start: 132`, `class_start: 41`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 80`, `dead_code: 3`, `planned_debt: 4`, `fragile_debt: 5`, `duplicate_logic: 2`
* *Architecture:* `api: 187`, `import: 36`
* *Defense:* `safety: 282`, `doc: 198`, `test: 5`, `sync_locks: 1`, `immutability_locks: 518`, `cleanup: 52`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` main.zig, main.zig, surface_child_exited.zig, adw, title_dialog.zig, class.zig, quirks.zig, apprt.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `macos/Sources/Ghostty/Ghostty.App.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.207 IQR)
- **Top Global Matches:** file_cluster_8: 11.207, file_cluster_1: 11.699, file_cluster_7: 11.711
- **Magnitude:** 5277.74 | **LOC:** 2241 | **CtrlFlow:** 73.3% | **Authorship Centralization:** 66.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (29.8327%), Tech Debt (75.5954%)
**Top Internal Functions/Classes:**
  * `promptTitle` (Impact: 394.4 | O(2^N))
  * `progressReport` (Impact: 239.8 | O(2^N))
  * `commandFinished` (Impact: 213.8 | O(N^6))
  * `startSearch` (Impact: 183.5 | O(2^N))
  * `gotoSplit` (Impact: 170.3 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 652`, `structural_boundaries: 238`, `args: 59`, `func_start: 56`, `class_start: 4`
* *Risk/State:* `high_risk_execution: 10`, `state_mutation: 15`, `duplicate_logic: 2`, `orphaned_logic: 41`
* *Architecture:* `api: 4`, `concurrency: 14`, `import: 3`
* *Defense:* `safety: 164`, `doc: 19`, `immutability_locks: 233`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SwiftUI, UserNotifications, GhosttyKit
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/Screen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.258 IQR)
- **Top Global Matches:** file_cluster_8: 14.258, file_cluster_7: 14.494, file_cluster_0: 14.512
- **Magnitude:** 5223.76 | **LOC:** 10353 | **CtrlFlow:** 70.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (18.0978%), Tech Debt (11.0806%)
**Top Internal Functions/Classes:**
  * `clone` (Impact: 520.7 | O(2^N) | DB: 2)
    * *Intent:* /// is only for read-only operations, it is better to not have any /// hyperlink state. Note that al...
  * `resize` (Impact: 512.8 | O(2^N) | DB: 3)
    * *Intent:* /// Resize the screen. The rows or cols can be bigger or smaller. /// /// If this returns an error, ...
  * `selectLine` (Impact: 335.4 | O(N^6) | DB: 11)
    * *Intent:* /// Select the line under the given point. This will select across soft-wrapped /// lines and will o...
  * `testWriteString` (Impact: 219.2 | O(N^6) | DB: 6)
    * *Intent:* /// This is basically a really jank version of Terminal.printString. We /// have to reimplement it h...
  * `promptClickLine` (Impact: 198.8 | O(N^5) | DB: 4)
    * *Intent:* /// Determine the inputs required to move from the cursor to the given /// click location. If the cu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 2278`, `structural_boundaries: 944`, `args: 63`, `func_start: 63`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 45`, `state_mutation: 934`, `dead_code: 24`, `planned_debt: 4`, `fragile_debt: 11`, `duplicate_logic: 2`
* *Architecture:* `io: 6`, `api: 81`, `import: 21`
* *Defense:* `safety: 1795`, `doc: 383`, `test: 202`, `sync_locks: 1`, `immutability_locks: 1245`, `cleanup: 520`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.378
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.009248
  * `Imports (Out-Degree: 6):` PageList.zig, osc.zig, tripwire.zig, point.zig, quirks.zig, size.zig, terminal_options, fastmem.zig...
  * `Imported By (In-Degree: 9):` (Excluded from Brief to save tokens)

### `src/input/Binding.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.823 IQR)
- **Top Global Matches:** file_cluster_8: 13.823, file_cluster_7: 13.94, file_cluster_13: 14.039
- **Magnitude:** 4459.68 | **LOC:** 4848 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 7
- **Risk Profile:** Cognitive Load (13.155%), Tech Debt (57.3516%)
**Top Internal Functions/Classes:**
  * `parseAndPutRecurse` (Impact: 795.1 | O(2^N) | DB: 1)
    * *Intent:* /// Returns the set that was ultimately updated if a binding was /// added. Unbind does not return a...
  * `parse` (Impact: 347.9 | O(N^6) | DB: 3)
    * *Intent:* /// Parse a single trigger. The input is expected to be ONLY the trigger /// (i.e. in the sequence `...
  * `formatEntries` (Impact: 315.3 | O(2^N) | DB: 1)
    * *Intent:* /// Writes the configuration entries for the binding /// that this value is part of. /// /// The val...
  * `formatValue` (Impact: 253.6 | O(2^N))
  * `parse` (Impact: 185.2 | O(N^6))
    * *Intent:* /// Parse an action in the format of "key=value" where key is the /// action name and value is the a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1077`, `structural_boundaries: 325`, `args: 64`, `func_start: 64`, `class_start: 33`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 2`, `state_mutation: 392`, `dead_code: 11`, `planned_debt: 2`, `duplicate_logic: 30`
* *Architecture:* `api: 92`, `import: 12`
* *Defense:* `safety: 665`, `doc: 667`, `test: 88`, `immutability_locks: 427`, `cleanup: 84`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.121
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002035
  * `Imports (Out-Degree: 1):` comparison.zig, quirks.zig, std, build_config.zig, formatter.zig, key_mods.zig, uucode, key.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/datastruct/split_tree.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.802 IQR)
- **Top Global Matches:** file_cluster_8: 13.802, file_cluster_7: 13.958, file_cluster_13: 13.977
- **Magnitude:** 4457.16 | **LOC:** 2368 | **CtrlFlow:** 62.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (39.7247%), Tech Debt (8.9274%)
**Top Internal Functions/Classes:**
  * `SplitTree` (Impact: 3914.7 | O(2^N) | DB: 26)
    * *Intent:* /// view. The Allocator will be the allocator provided to the tree /// operation. /// /// - `fn eql(...
  * `ref` (Impact: 8.0 | O(N^2) | DB: 1)
  * `free` (Impact: 6.3 | O(N^6))
  * `splitTreeLabel` (Impact: 6.2 | O(N^2))
  * `unref` (Impact: 2.7 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 562`, `structural_boundaries: 334`, `args: 50`, `func_start: 46`, `class_start: 14`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 435`, `dead_code: 3`, `planned_debt: 2`, `fragile_debt: 1`
* *Architecture:* `api: 42`, `import: 6`
* *Defense:* `safety: 284`, `doc: 155`, `test: 18`, `immutability_locks: 206`, `cleanup: 114`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, glib, build_config.zig, quirks.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/gtk/class/application.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.613 IQR)
- **Top Global Matches:** file_cluster_8: 12.613, file_cluster_13: 12.84, file_cluster_7: 12.879
- **Magnitude:** 4449.04 | **LOC:** 2957 | **CtrlFlow:** 68.7% | **Authorship Centralization:** 55.6%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 17
- **Risk Profile:** Cognitive Load (10.4028%), Tech Debt (10.1461%)
**Top Internal Functions/Classes:**
  * `new` (Impact: 429.3 | O(2^N) | DB: 8)
    * *Intent:* /// Creates a new Application instance. /// /// This does a lot more work than a typical class insta...
  * `run` (Impact: 345.3 | O(2^N) | DB: 1)
    * *Intent:* /// Run the application. This is a replacement for `gio.Application.run` /// because we want more ti...
  * `performAction` (Impact: 300.4 | O(N^5))
    * *Intent:* /// apprt API to perform an action.
  * `actionNewWindow` (Impact: 240.3 | O(N^6) | DB: 10)
    * *Intent:* /// Handle `app.new-window` and `app.new-window-command` GTK actions
  * `glibLogWriterFunction` (Impact: 192.9 | O(N^4) | DB: 2)
    * *Intent:* /// Function used to funnel GLib/GObject/GTK log messages into Zig's logging /// system rather than ...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 557`, `structural_boundaries: 254`, `args: 108`, `func_start: 108`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 35`, `state_mutation: 103`, `dead_code: 4`, `planned_debt: 5`, `fragile_debt: 3`
* *Architecture:* `io: 6`, `api: 84`, `import: 42`
* *Defense:* `safety: 217`, `doc: 124`, `immutability_locks: 258`, `cleanup: 33`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.368
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007121
  * `Imports (Out-Degree: 6):` main.zig, main.zig, App.zig, close_confirmation_dialog.zig, global_shortcuts.zig, adw, class.zig, quirks.zig...
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/terminal/osc/parsers/osc9.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.704 IQR)
- **Top Global Matches:** file_cluster_8: 13.704, file_cluster_13: 14.056, file_cluster_0: 14.075
- **Magnitude:** 3910.72 | **LOC:** 1142 | **CtrlFlow:** 72.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 62
- **Risk Profile:** Cognitive Load (51.9234%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 3706.2 | O(2^N) | DB: 62)
    * *Intent:* /// Parse OSC 9, which could be an iTerm2 notification or a ConEmu extension.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 300`, `structural_boundaries: 112`, `args: 1`, `func_start: 1`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 186`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 216`, `doc: 1`, `test: 61`, `immutability_locks: 190`, `cleanup: 23`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, osc.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/kitty/graphics_command.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.383 IQR)
- **Top Global Matches:** file_cluster_8: 13.383, file_cluster_7: 13.602, file_cluster_13: 13.638
- **Magnitude:** 3728.38 | **LOC:** 1326 | **CtrlFlow:** 74.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 34
- **Risk Profile:** Cognitive Load (40.4897%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `encode` (Impact: 3139.4 | O(2^N) | DB: 34)
  * `feed` (Impact: 346.4 | O(N^5))
    * *Intent:* /// Feed a single byte to the parser. /// /// The first byte to start parsing should be the byte imm...
  * `init` (Impact: 28.7 | O(2^N) | DB: 2)
    * *Intent:* /// Initialize the parser. The allocator given will be used for both /// temporary data and long-liv...
  * `parseString` (Impact: 13.3 | O(N^2) | DB: 1)
    * *Intent:* /// Parse a complete command string.
  * `deinit` (Impact: 5.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 360`, `structural_boundaries: 126`, `args: 22`, `func_start: 22`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 140`, `dead_code: 1`
* *Architecture:* `api: 33`, `import: 3`
* *Defense:* `safety: 237`, `doc: 45`, `test: 22`, `immutability_locks: 143`, `cleanup: 44`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 3.035
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.004069
  * `Imports (Out-Degree: 0):` std, main.zig, quirks.zig
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/terminal/tmux/output.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.948 IQR)
- **Top Global Matches:** file_cluster_8: 13.948, file_cluster_7: 14.14, file_cluster_13: 14.298
- **Magnitude:** 3581.08 | **LOC:** 591 | **CtrlFlow:** 94.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (19.5816%), Tech Debt (10.2552%)
**Top Internal Functions/Classes:**
  * `format` (Impact: 3481.4 | O(2^N) | DB: 4)
    * *Intent:* /// Format a set of variables into the proper format string for tmux /// that we can handle with `pa...
  * `parseFormatStruct` (Impact: 41.3 | O(N^3) | DB: 2)
    * *Intent:* /// Parse the output from a command with the given format struct /// (returned usually by FormatStru...
  * `comptimeFormat` (Impact: 12.8 | O(N^2) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 320`, `structural_boundaries: 19`, `args: 7`, `func_start: 7`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 27`, `planned_debt: 1`
* *Architecture:* `api: 8`, `import: 1`
* *Defense:* `safety: 284`, `doc: 61`, `test: 47`, `immutability_locks: 31`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 1.008
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.001017
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/terminal/stream.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.44%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.903 IQR)
- **Top Global Matches:** file_cluster_8: 11.903, file_cluster_7: 12.232, file_cluster_13: 12.353
- **Magnitude:** 3463.2 | **LOC:** 3450 | **CtrlFlow:** 83.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (20.3707%), Tech Debt (81.6219%)
**Top Internal Functions/Classes:**
  * `Stream` (Impact: 2222.2 | O(N^6) | DB: 8)
    * *Intent:* /// /// fn(comptime action: Action.Key, value: Action.Value(action)) void /// /// The handler type T...
  * `escDispatch` (Impact: 426.6 | O(N^6))
  * `oscDispatch` (Impact: 47.9 | O(N^6))
  * `configureCharset` (Impact: 41.7 | O(N^5))
  * `vt` (Impact: 21.6 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 683`, `structural_boundaries: 136`, `args: 68`, `func_start: 67`, `class_start: 56`
* *Risk/State:* `safety_bypasses: 25`, `high_risk_execution: 1`, `state_mutation: 134`, `dead_code: 3`, `planned_debt: 9`, `duplicate_logic: 30`
* *Architecture:* `api: 91`, `import: 17`
* *Defense:* `safety: 188`, `doc: 67`, `test: 39`, `immutability_locks: 161`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.942
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002543
  * `Imports (Out-Degree: 8):` main.zig, device_status.zig, UTF8Decoder.zig, quirks.zig, modes.zig, std, Parser.zig, osc.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/terminal/style.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.579 IQR)
- **Top Global Matches:** file_cluster_8: 13.579, file_cluster_13: 13.676, file_cluster_7: 13.75
- **Magnitude:** 3407.72 | **LOC:** 1079 | **CtrlFlow:** 65.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 77
- **Risk Profile:** Cognitive Load (37.957%), Tech Debt (26.2894%)
**Top Internal Functions/Classes:**
  * `formatColor` (Impact: 2539.2 | O(2^N) | DB: 77)
  * `format` (Impact: 217.7 | O(N^6) | DB: 1)
    * *Intent:* /// Formatting to make debug logs easier to read /// by only including non-default attributes.
  * `format` (Impact: 141.6 | O(N^4))
  * `fg` (Impact: 128.2 | O(N^6))
    * *Intent:* /// Returns the fg color for a cell with this style given the palette /// and various configuration ...
  * `format` (Impact: 37.7 | O(N^5))
    * *Intent:* /// Formatting to make debug logs easier to read /// by only including non-default attributes.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 250`, `structural_boundaries: 130`, `args: 20`, `func_start: 20`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 191`, `dead_code: 1`, `duplicate_logic: 5`
* *Architecture:* `api: 25`, `import: 7`
* *Defense:* `safety: 169`, `doc: 72`, `test: 37`, `immutability_locks: 135`, `cleanup: 36`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` quirks.zig, std, size.zig, ref_counted_set.zig, sgr.zig, page.zig, color.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/formatter.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.737 IQR)
- **Top Global Matches:** file_cluster_8: 14.737, file_cluster_13: 14.95, file_cluster_0: 14.981
- **Magnitude:** 3338.28 | **LOC:** 6280 | **CtrlFlow:** 54.7% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (70.5332%), Tech Debt (11.8851%)
**Top Internal Functions/Classes:**
  * `formatWithState` (Impact: 1221.3 | O(N^6) | DB: 22)
  * `format` (Impact: 114.8 | O(N^6) | DB: 4)
  * `writeCodepoint` (Impact: 111.0 | O(N^6))
  * `writeCodepointWithReplacement` (Impact: 109.5 | O(N^5) | DB: 1)
  * `formatStyleOpen` (Impact: 104.1 | O(N^5) | DB: 2)
    * *Intent:* /// Write a string with HTML escaping. Used for escaping href attributes /// and other HTML attribut...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1209`, `structural_boundaries: 1001`, `args: 16`, `func_start: 16`, `class_start: 38`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 1402`, `planned_debt: 2`, `fragile_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `io: 2`, `api: 23`, `import: 18`
* *Defense:* `safety: 962`, `doc: 90`, `test: 105`, `immutability_locks: 669`, `cleanup: 402`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` page.zig, point.zig, PageList.zig, quirks.zig, modes.zig, std, Selection.zig, lib.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `macos/Sources/Features/Terminal/TerminalController.swift` (SWIFT | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_17` (Drift: 12.27 IQR)
- **Top Global Matches:** file_cluster_17: 12.27, file_cluster_0: 12.413, file_cluster_8: 12.418
- **Magnitude:** 3326.12 | **LOC:** 1665 | **CtrlFlow:** 75.2% | **Authorship Centralization:** 85.7%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.6469%), Tech Debt (13.8554%)
**Top Internal Functions/Classes:**
  * `newWindow` (Impact: 3266.8 | O(2^N) | DB: 1)
  * `applyCascade` (Impact: 14.4 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 246`, `structural_boundaries: 81`, `args: 41`, `func_start: 26`, `class_start: 2`
* *Risk/State:* `state_mutation: 20`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `api: 10`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 71`, `doc: 40`, `immutability_locks: 92`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Foundation, Cocoa, Combine, GhosttyKit, SwiftUI
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/cli/args.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.909 IQR)
- **Top Global Matches:** file_cluster_8: 13.909, file_cluster_11: 13.953, file_cluster_13: 14.036
- **Magnitude:** 3251.22 | **LOC:** 1628 | **CtrlFlow:** 68.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (48.8904%), Tech Debt (24.6915%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 966.5 | O(2^N) | DB: 3)
    * *Intent:* /// "DiagnosticList" and any diagnostic messages will be added to that list. /// When diagnostics ar...
  * `parseIntoField` (Impact: 647.3 | O(N^6) | DB: 2)
    * *Intent:* /// Parse a single key/value pair into the destination type T. /// /// This may result in allocation...
  * `next` (Impact: 602.7 | O(2^N) | DB: 22)
  * `parseAutoStruct` (Impact: 224.5 | O(N^5) | DB: 4)
  * `parseTaggedUnion` (Impact: 92.2 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 448`, `structural_boundaries: 203`, `args: 29`, `func_start: 28`, `class_start: 8`
* *Risk/State:* `safety_bypasses: 29`, `state_mutation: 264`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 4`
* *Architecture:* `api: 29`, `import: 5`
* *Defense:* `safety: 256`, `doc: 78`, `test: 36`, `immutability_locks: 214`, `cleanup: 43`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` quirks.zig, std, diagnostics.zig, CommaSplitter.zig, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/osc/parsers/semantic_prompt.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.234 IQR)
- **Top Global Matches:** file_cluster_8: 14.234, file_cluster_7: 14.427, file_cluster_13: 14.432
- **Magnitude:** 3204.64 | **LOC:** 1265 | **CtrlFlow:** 76.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 73
- **Risk Profile:** Cognitive Load (58.2681%), Tech Debt (16.5489%)
**Top Internal Functions/Classes:**
  * `parse` (Impact: 2646.3 | O(2^N) | DB: 73)
    * *Intent:* /// Parse OSC 133, semantic prompts
  * `read` (Impact: 200.1 | O(N^6) | DB: 1)
    * *Intent:* /// Read the option value from the raw options string. /// /// The raw options string is the raw unp...
  * `init` (Impact: 32.6 | O(N^3))
  * `key` (Impact: 24.8 | O(2^N))
  * `init` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 361`, `structural_boundaries: 109`, `args: 9`, `func_start: 9`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 2`, `state_mutation: 222`, `duplicate_logic: 3`
* *Architecture:* `api: 15`, `import: 4`
* *Defense:* `safety: 273`, `doc: 50`, `test: 64`, `immutability_locks: 195`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, string_encoding.zig, osc.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/tmux/viewer.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.791 IQR)
- **Top Global Matches:** file_cluster_8: 12.791, file_cluster_7: 13.003, file_cluster_13: 13.13
- **Magnitude:** 3123.0 | **LOC:** 2284 | **CtrlFlow:** 75.9% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (8.2692%), Tech Debt (96.9328%)
**Top Internal Functions/Classes:**
  * `nextCommand` (Impact: 427.1 | O(2^N) | DB: 5)
  * `receivedPaneState` (Impact: 321.5 | O(N^6) | DB: 2)
  * `initLayout` (Impact: 191.0 | O(2^N) | DB: 3)
  * `syncLayouts` (Impact: 148.7 | O(N^5) | DB: 8)
  * `formatCommand` (Impact: 110.7 | O(N^5))
    * *Intent:* /// Format the command into the command that should be executed /// by tmux. Trailing newlines are a...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 437`, `structural_boundaries: 139`, `args: 67`, `func_start: 65`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 13`, `state_mutation: 134`, `dead_code: 4`, `planned_debt: 3`, `duplicate_logic: 32`
* *Architecture:* `api: 18`, `import: 11`
* *Defense:* `safety: 254`, `doc: 220`, `test: 11`, `immutability_locks: 163`, `cleanup: 53`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` ScreenSet.zig, cursor.zig, Terminal.zig, control.zig, output.zig, std, Screen.zig, main.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/apprt/embedded.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.879 IQR)
- **Top Global Matches:** file_cluster_8: 12.879, file_cluster_7: 13.043, file_cluster_13: 13.103
- **Magnitude:** 3061.54 | **LOC:** 2232 | **CtrlFlow:** 70.4% | **Authorship Centralization:** 50.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (6.7639%), Tech Debt (74.2402%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 412.4 | O(2^N) | DB: 9)
  * `pin` (Impact: 142.0 | O(2^N))
  * `cursorPosCallback` (Impact: 124.3 | O(2^N))
  * `CGSDefaultConnectionForThread` (Impact: 121.5 | O(N^6) | DB: 1)
  * `keyEvent` (Impact: 102.0 | O(2^N))
    * *Intent:* /// See CoreApp.keyEvent.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 405`, `structural_boundaries: 170`, `args: 148`, `func_start: 142`, `class_start: 22`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 69`, `dead_code: 5`, `duplicate_logic: 27`
* *Architecture:* `io: 2`, `api: 208`, `import: 16`
* *Defense:* `safety: 186`, `doc: 185`, `sync_locks: 9`, `immutability_locks: 201`, `cleanup: 37`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 0.785
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` apprt.zig, main.zig, App.zig, quirks.zig, dcimgui, std, builtin, config.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/terminal/stream_terminal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.25%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.745 IQR)
- **Top Global Matches:** file_cluster_8: 14.745, file_cluster_13: 14.872, file_cluster_0: 14.966
- **Magnitude:** 2896.14 | **LOC:** 2072 | **CtrlFlow:** 52.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 155
- **Risk Profile:** Cognitive Load (75.0711%), Tech Debt (15.5836%)
**Top Internal Functions/Classes:**
  * `deviceStatus` (Impact: 2039.5 | O(N^6) | DB: 155)
  * `vtFallible` (Impact: 188.8 | O(N^5))
  * `reportDeviceAttributes` (Impact: 19.0 | O(N^2) | DB: 2)
  * `bell` (Impact: 15.8 | O(2^N))
  * `writePty` (Impact: 10.6 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 418`, `structural_boundaries: 386`, `args: 68`, `func_start: 60`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 529`, `dead_code: 1`, `planned_debt: 1`, `duplicate_logic: 3`
* *Architecture:* `api: 7`, `import: 11`
* *Defense:* `safety: 325`, `doc: 41`, `test: 65`, `immutability_locks: 161`, `cleanup: 170`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 0.918
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.002713
  * `Imports (Out-Degree: 6):` device_status.zig, modes.zig, std, csi.zig, color.zig, color.zig, Terminal.zig, Screen.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `macos/Tests/Splits/SplitTreeTests.swift` (SWIFT) | Magnitude: 639.42 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 519, immutability_locks: 167, test: 146, branch: 110
- `macos/Sources/Helpers/Private/Dock.swift` (SWIFT) | Magnitude: 33.66 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 12, indent_spaces: 12, structural_boundaries: 7, pointers: 4
- `macos/Tests/Ghostty/ConfigTests.swift` (SWIFT) | Magnitude: 223.14 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 183, test: 76, branch: 49, immutability_locks: 42
- `macos/Sources/Features/App Intents/CommandPaletteIntent.swift` (SWIFT) | Magnitude: 46.94 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 25, structural_boundaries: 10, state_mutation: 8, branch: 5
- `macos/Sources/Features/App Intents/KeybindIntent.swift` (SWIFT) | Magnitude: 46.9 | Delta: **0.047 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 24, structural_boundaries: 11, state_mutation: 8, branch: 5

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/stb/stb_image.h` (C) | Magnitude: 7549.2 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 3276, indent_spaces: 2524, pointers: 1126, branch: 894
- `src/cli/action.zig` (ZIG) | Magnitude: 258.36 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 205, branch: 78, encapsulation: 54, globals: 52
- `macos/Sources/Helpers/CodableBridge.swift` (SWIFT) | Magnitude: 59.04 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 14, branch: 12, structural_boundaries: 7, safety: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `snap/local/launcher` (SHELL) | Magnitude: 71.06 | Delta: **0.073 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 25, structural_boundaries: 23, api: 17, indent_spaces: 16

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/terminal/c/cell.zig` (ZIG) | Magnitude: 106.26 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 117, state_mutation: 32, doc: 30, branch: 25
- `src/config.zig` (ZIG) | Magnitude: 58.02 | Delta: **0.001 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 46, immutability_locks: 46, api: 42, import: 14
- `src/font/SharedGrid.zig` (ZIG) | Magnitude: 675.92 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 336, branch: 109, globals: 71, encapsulation: 70
- `macos/Sources/Helpers/TabGroupCloseCoordinator.swift` (SWIFT) | Magnitude: 15.58 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: doc: 23, indent_spaces: 17, state_mutation: 9, structural_boundaries: 4
- `pkg/harfbuzz/main.zig` (ZIG) | Magnitude: 33.58 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: globals: 26, immutability_locks: 26, api: 18, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `macos/Sources/Helpers/Extensions/Optional+Extension.swift` (SWIFT) | Magnitude: 68.38 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 7, branch: 5, structural_boundaries: 3, generics: 2
- `src/unicode/lut.zig` (ZIG) | Magnitude: 491.7 | Delta: **0.025 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 144, branch: 52, safety: 28, immutability_locks: 26
- `src/apprt/gtk/ext.zig` (ZIG) | Magnitude: 93.82 | Delta: **0.042 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 27, immutability_locks: 22, branch: 20, globals: 17
- `src/apprt/gtk/class.zig` (ZIG) | Magnitude: 651.18 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 322, doc: 88, branch: 44, immutability_locks: 43
- `macos/Sources/Helpers/ObjCExceptionCatcher.h` (OBJECTIVE-C) | Magnitude: 18.78 | Delta: **0.078 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 4, indent_spaces: 4, safety_bypasses: 2, pointers: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `src/shell-integration/bash/bash-preexec.sh` (SHELL) | Magnitude: 664.64 | Delta: **0.011 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 141, branch: 99, state_mutation: 80, structural_boundaries: 44
- `src/font/shaper/harfbuzz.zig` (ZIG) | Magnitude: 1792.54 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 1774, state_mutation: 843, branch: 529, structural_boundaries: 456
- `macos/Sources/Features/AppleScript/ScriptWindow.swift` (SWIFT) | Magnitude: 216.84 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 130, branch: 82, doc: 74, structural_boundaries: 54
- `macos/Sources/Features/App Intents/QuickTerminalIntent.swift` (SWIFT) | Magnitude: 43.7 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 19, branch: 10, structural_boundaries: 9, state_mutation: 7
- `macos/Sources/Helpers/Extensions/NSWindow+Extension.swift` (SWIFT) | Magnitude: 13.56 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 15, doc: 12, branch: 7, structural_boundaries: 6

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `macos/Sources/Helpers/NonDraggableHostingView.swift` (SWIFT) | Magnitude: 13.08 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: doc: 8, structural_boundaries: 3, ui_framework: 2, generics: 2
- `macos/Sources/Helpers/HostingWindow.swift` (SWIFT) | Magnitude: 18.22 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: structural_boundaries: 6, indent_spaces: 6, state_mutation: 3, class_start: 2
- `macos/Sources/Ghostty/Surface View/SurfaceScrollView.swift` (SWIFT) | Magnitude: 146.34 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 88, doc: 70, branch: 18, immutability_locks: 17
- `macos/Sources/Features/QuickTerminal/QuickTerminalSpaceBehavior.swift` (SWIFT) | Magnitude: 28.16 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 24, branch: 10, structural_boundaries: 7, ui_framework: 4
- `macos/Sources/Features/Custom App Icon/ColorizedGhosttyIconView.swift` (SWIFT) | Magnitude: 16.22 | Delta: **0.039 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 7, structural_boundaries: 5, ui_framework: 4, import: 2

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `macos/Sources/Features/AppleScript/AppDelegate+AppleScript.swift` (SWIFT) | Magnitude: 104.92 | Delta: **0.093 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 77, indent_spaces: 46, branch: 28, structural_boundaries: 22
- `src/benchmark/GraphemeBreak.zig` (ZIG) | Magnitude: 188.94 | Delta: **0.096 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 89, encapsulation: 40, state_mutation: 37, globals: 37
- `src/benchmark/IsSymbol.zig` (ZIG) | Magnitude: 197.02 | Delta: **0.114 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 88, encapsulation: 39, globals: 35, state_mutation: 33
- `macos/Sources/Features/App Intents/Entities/TerminalEntity.swift` (SWIFT) | Magnitude: 118.08 | Delta: **0.117 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 85, state_mutation: 39, concurrency: 34, structural_boundaries: 27
- `macos/Sources/Features/App Intents/IntentPermission.swift` (SWIFT) | Magnitude: 56.84 | Delta: **0.119 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: doc: 24, indent_spaces: 24, branch: 8, concurrency: 8

### Mixed-Responsibility Refactoring Targets for: file_cluster_7
- `src/terminal/cursor.zig` (ZIG) | Magnitude: 16.28 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 9, doc: 8, branch: 1, class_start: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `pkg/macos/text/frame.zig` (ZIG) | Magnitude: 20.58 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 18, globals: 8, immutability_locks: 8, api: 7
- `src/lib/string.zig` (ZIG) | Magnitude: 9.44 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: branch: 5, immutability_locks: 4, indent_spaces: 3, safety: 2
- `src/main_c.zig` (ZIG) | Magnitude: 191.1 | Delta: **0.0 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 139, branch: 56, immutability_locks: 56, globals: 41
- `macos/Sources/Ghostty/Surface View/SurfaceProgressBar.swift` (SWIFT) | Magnitude: 34.82 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_2`
  * Top Architectural Signatures: indent_spaces: 86, structural_boundaries: 27, branch: 21, state_mutation: 18
- `pkg/macos/foundation.zig` (ZIG) | Magnitude: 37.7 | Delta: **0.003 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: globals: 32, immutability_locks: 32, api: 22, import: 12

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `pkg/freetype/tag.zig` (ZIG) | Magnitude: 15.8 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_0`
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

- `src/config/Config.zig` -> Churn: **75.33%** | Cog Load: 8.4684% | Debt: 73.7552%
- `src/terminal/stream_terminal.zig` -> Churn: **63.75%** | Cog Load: 75.0711% | Debt: 15.5836%
- `src/shell-integration/bash/ghostty.bash` -> Churn: **58.9%** | Cog Load: 87.5892% | Debt: 20.365%
- `src/terminal/c/formatter.zig` -> Churn: **55.29%** | Cog Load: 58.0653% | Debt: 31.9909%
- `macos/Sources/Features/AppleScript/AppDelegate+AppleScript.swift` -> Churn: **53.62%** | Cog Load: 49.9301% | Debt: 74.4868%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/terminal/PageList.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 10401.12
- `src/terminal/Terminal.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 8419.84
- `src/renderer/generic.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 8077.48
- `src/input/Binding.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 4459.68
- `src/terminal/osc/parsers/osc9.zig` -> **Mitchell Hashimoto** (100.0% isolated ownership) | Magnitude: 3910.72

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/terminal/PageList.zig` -> **Severity: 0.001** (Bridge: 0.0 * Flux: 62.3304%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `pkg/opengl/glad.zig` -> **Severity: 0.977** (Embedded: 0.0122 * Error Risk: 80.0%)
- `src/benchmark/Benchmark.zig` -> **Severity: 0.376** (Embedded: 0.0081 * Error Risk: 46.2338%)
- `src/apprt/gtk/class/dialog.zig` -> **Severity: 0.318** (Embedded: 0.0064 * Error Risk: 50.0%)
- `src/font/sprite/draw/box.zig` -> **Severity: 0.271** (Embedded: 0.0041 * Error Risk: 66.5429%)
- `pkg/fontconfig/pattern.zig` -> **Severity: 0.244** (Embedded: 0.0031 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/apprt/gtk.zig` -> **Severity: 2193.5** (Blast Radius: 21.935 * Doc Risk: 100.0%)
- `src/terminal/lib.zig` -> **Severity: 1176.6** (Blast Radius: 11.766 * Doc Risk: 100.0%)
- `src/os/macos.zig` -> **Severity: 1161.671** (Blast Radius: 12.539 * Doc Risk: 92.6446%)
- `pkg/opengl/glad.zig` -> **Severity: 818.282** (Blast Radius: 8.183 * Doc Risk: 99.9978%)
- `src/build_config.zig` -> **Severity: 735.037** (Blast Radius: 7.354 * Doc Risk: 99.9507%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
