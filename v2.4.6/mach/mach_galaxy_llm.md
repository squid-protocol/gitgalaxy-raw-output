# ARCHITECTURAL_BRIEF: mach
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/mach` |
| **Timestamp** | `2026-08-03T20:08:40.452392+00:00` |
| **Scan Duration** | `1.28s` |
| **Git Branch** | `main` |
| **Git Commit** | `77e4ea34baad312022ddefbbca0829a2c9557017` |
| **Git Remote** | `https://github.com/hexops/mach.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 127 malicious artifacts.

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
| Total Artifacts | 185 |
| Analyzed Artifacts (Scanned) | 132 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 53 |
| Total LOC | 61865 |
| Volatility Index | 0.015 |
| % Scanned of codebase = | 71.4% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6183 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.176 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 9.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.7011 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 7 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 124 | 61849 | 93.9% |
| MARKDOWN | 3 | 0 | 2.3% |
| PLAINTEXT | 2 | 0 | 1.5% |
| C | 2 | 12 | 1.5% |
| SHELL | 1 | 4 | 0.8% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `5.794`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 89 | 67.4% |
| file_cluster_13 | 21 | 15.9% |
| file_cluster_6 | 6 | 4.5% |
| file_cluster_2 | 6 | 4.5% |
| file_cluster_17 | 1 | 0.8% |
| file_cluster_0 | 1 | 0.8% |
| file_cluster_16 | 1 | 0.8% |
| file_cluster_4 | 1 | 0.8% |
| file_cluster_9 | 1 | 0.8% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.8% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 53*

**Composition by Extension & Reason:**
- `.wgsl`: 31x Unsupported Format (.wgsl), 4x Excluded (Unsupported Extension: '.wgsl')
- `no_extension`: 6x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.md`: 5x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.yml`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.zig`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 7424 LOC)
- `.zon`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.manifest`: 1x Unsupported Format (.manifest)
- `.ttf`: 1x Excluded (Explicitly Denied Extension: '.ttf')

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 56.3 | 17.1 | 13.8 | 5.0 |
| Error & Exception Exposure | 0.0 | 99.5 | 24.1 | 6.5 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 23.9 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 49.7 | 80.0 | 80.0 |
| API Exposure | 0.0 | 19.7 | 5.8 | 4.4 | 5.8 |
| Concurrency Exposure | 0.0 | 100.0 | 3.4 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 96.6 | 10.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 100.0 | 4.9 | 0.0 | 0.0 |
| Specification Exposure | 20.0 | 100.0 | 96.0 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 7.3 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 5.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 73.9 | 99.0 | 100.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 74.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 20.0 | 14.3 | 20.0 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/sysaudio/alsa.zig` (Hits: 25)
- `src/core/linux/Wayland.zig` (Hits: 16)
- `src/core/linux/X11.zig` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **interface.zig** (`src/sysgpu/sysgpu/interface.zig`) — 25 inbound connections
2. **buffer.zig** (`src/sysgpu/sysgpu/buffer.zig`) — 9 inbound connections
3. **backends.zig** (`src/sysaudio/backends.zig`) — 8 inbound connections
4. **texture.zig** (`src/sysgpu/sysgpu/texture.zig`) — 8 inbound connections
5. **shader.zig** (`src/sysgpu/shader.zig`) — 6 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **main.zig** (`src/sysgpu/sysgpu/main.zig`) — 28 outbound dependencies
2. **device.zig** (`src/sysgpu/sysgpu/device.zig`) — 20 outbound dependencies
3. **Wayland.zig** (`src/core/linux/Wayland.zig`) — 14 outbound dependencies
4. **X11.zig** (`src/core/linux/X11.zig`) — 11 outbound dependencies
5. **shader.zig** (`src/sysgpu/shader.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `emitGlobalVar` (@ `src/sysgpu/shader/codegen/hlsl.zig`) -> Impact: **2693.9** | LOC: 894
- `init` (@ `src/sysgpu/d3d12.zig`) -> Impact: **2218.2** | LOC: 963
- `Printer` (@ `src/sysgpu/shader/print_air.zig`) -> Impact: **2195.6** | LOC: 511
- `genCall` (@ `src/sysgpu/shader/AstGen.zig`) -> Impact: **1777.6** | LOC: 552
- `emitFn` (@ `src/sysgpu/shader/codegen/glsl.zig`) -> Impact: **1504.1** | LOC: 568
- `renderClass` (@ `src/sysgpu/tools/gen_spirv_spec.zig`) -> Impact: **1364.5** | LOC: 530
- `gen` (@ `src/sysgpu/shader/codegen/glsl.zig`) -> Impact: **1208.3** | LOC: 275
- `Objects` (@ `src/module.zig`) -> Impact: **1186.1** | LOC: 444
- `attribute` (@ `src/sysgpu/shader/Parser.zig`) -> Impact: **869.0** | LOC: 164
- `resolveConstExpr` (@ `src/sysgpu/shader/Air.zig`) -> Impact: **805.8** | LOC: 111

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `tick` (@ `examples/core-transparent-window/App.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* // TODO(object): window-title // try updateWindowTitle(core);
- `tick` (@ `examples/piano/App.zig`) -> **O(2^N) [Recursive]**
- `tick` (@ `examples/play-opus/App.zig`) -> **O(2^N) [Recursive]**
- `initWindow` (@ `src/core/Darwin.zig`) -> **O(2^N) [Recursive]**
- `initWindow` (@ `src/core/Linux.zig`) -> **O(2^N) [Recursive]**
- `init` (@ `src/gamemode.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Initialize gamemode, logging a possible failure. /// If this fails, no more attempts at loading libgamemode will be made. /// Returns true if game...
- `updatePipelineBuffers` (@ `src/gfx/Text.zig`) -> **O(2^N) [Recursive]**
- `next` (@ `src/gfx/font/native/TextRun.zig`) -> **O(2^N) [Recursive]**
- `Objects` (@ `src/module.zig`) -> **O(2^N) [Recursive]**
- `Modules` (@ `src/module.zig`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `init` (@ `src/sysgpu/d3d12.zig`) -> DB Complexity: **43**
- `initWindow` (@ `src/core/linux/X11.zig`) -> DB Complexity: **38**
  * *Intent:* // Mutable fields only used by main thread // Mutable state fields; read/write by any thread
- `init` (@ `src/sysgpu/opengl.zig`) -> DB Complexity: **38**
- `init` (@ `src/sysaudio/alsa.zig`) -> DB Complexity: **31**
- `tick` (@ `src/core/linux/Wayland.zig`) -> DB Complexity: **28**
- `deviceEventsLoop` (@ `src/sysaudio/alsa.zig`) -> DB Complexity: **28**
- `keyboardHandleKeymap` (@ `src/core/linux/Wayland.zig`) -> DB Complexity: **23**
- `refresh` (@ `src/sysaudio/alsa.zig`) -> DB Complexity: **19**
- `execute` (@ `src/sysgpu/opengl.zig`) -> DB Complexity: **17**
  * *Intent:* // Internal
- `renderClass` (@ `src/sysgpu/tools/gen_spirv_spec.zig`) -> DB Complexity: **17**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/sysgpu` | 10 | 20383.54 | 16.99% | 51.67% |
| `src/sysgpu/shader` | 11 | 19672.18 | 20.41% | 8.3% |
| `src/sysgpu/shader/codegen` | 4 | 13919.42 | 40.04% | 17.97% |
| `src` | 11 | 8934.56 | 18.79% | 46.0% |
| `src/sysaudio` | 11 | 8676.08 | 24.37% | 73.44% |
| `src/sysgpu/sysgpu` | 28 | 3964.3 | 9.65% | 2.24% |
| `src/math` | 6 | 3180.82 | 9.25% | 14.79% |
| `src/core` | 4 | 2450.94 | 14.21% | 14.35% |
| `src/core/linux` | 3 | 2052.52 | 37.38% | 39.06% |
| `src/gfx` | 4 | 1745.36 | 8.64% | 47.39% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/gamemode.zig` -> **100.0%** Exposure
- `src/sysaudio/dummy.zig` -> **100.0%** Exposure
- `src/sysaudio/jack.zig` -> **100.0%** Exposure
- `src/sysaudio/main.zig` -> **100.0%** Exposure
- `src/sysaudio/pipewire/sysaudio.c` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/entrypoint/main.zig` -> **96.6253%** Exposure
- `src/graph.zig` -> **95.3832%** Exposure
- `src/sysaudio/wasapi.zig` -> **94.0366%** Exposure
- `src/time/Frequency.zig` -> **91.2492%** Exposure
- `src/sysaudio/alsa.zig` -> **91.0044%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/sysgpu/metal.zig` -> **35** Orphaned Functions | **60** Duplicates
- `src/sysgpu/opengl.zig` -> **35** Orphaned Functions | **60** Duplicates
- `src/sysgpu/d3d12.zig` -> **20** Orphaned Functions | **61** Duplicates
- `src/sysgpu/vulkan.zig` -> **0** Orphaned Functions | **66** Duplicates
- `src/sysaudio/jack.zig` -> **7** Orphaned Functions | **17** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/main.zig`** -> AI Confidence: **99.48%**
2. **`src/sysgpu/sysgpu/main.zig`** -> AI Confidence: **99.48%**
3. **`src/sysgpu/sysgpu/render_bundle_encoder.zig`** -> AI Confidence: **99.43%**
4. **`src/sysgpu/sysgpu/render_pass_encoder.zig`** -> AI Confidence: **99.43%**
5. **`src/sysgpu/main.zig`** -> AI Confidence: **99.39%**
6. **`src/core/linux/Wayland.zig`** -> AI Confidence: **99.35%**
7. **`src/math/main.zig`** -> AI Confidence: **99.34%**
8. **`src/sysgpu/shader/codegen/spirv.zig`** -> AI Confidence: **99.34%**
9. **`src/sysgpu/shader/test.zig`** -> AI Confidence: **99.34%**
10. **`src/sysgpu/vulkan.zig`** -> AI Confidence: **99.34%**
11. **`src/sysgpu/sysgpu/bind_group.zig`** -> AI Confidence: **99.33%**
12. **`src/math/collision.zig`** -> AI Confidence: **99.32%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `examples/core-transparent-window/App.zig` -> **20.0%** Exposure
- `examples/custom-renderer/App.zig` -> **20.0%** Exposure
- `examples/custom-renderer/Renderer.zig` -> **20.0%** Exposure
- `examples/glyphs/App.zig` -> **20.0%** Exposure
- `examples/hardware-check/App.zig` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `src/core/linux/Wayland.zig` -> **0.0096%** Exposure
### Raw Memory Manipulation
- `src/win32.zig` -> **9.9881%** Exposure
- `src/sysaudio/jack.zig` -> **8.6035%** Exposure
- `src/sysaudio/pipewire.zig` -> **8.3221%** Exposure
- `src/sysaudio/pulseaudio.zig` -> **2.7242%** Exposure
- `src/sysaudio/alsa.zig` -> **0.2964%** Exposure
### Algorithmic DoS Exposure
- `examples/core-custom-entrypoint/App.zig` -> **100.0%** Exposure
- `examples/core-transparent-window/App.zig` -> **100.0%** Exposure
- `examples/core-triangle/App.zig` -> **100.0%** Exposure
- `examples/custom-renderer/App.zig` -> **100.0%** Exposure
- `examples/custom-renderer/Renderer.zig` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `1` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `472` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/sysaudio/alsa.zig` (ZIG) -> Cumulative Risk: **782.34**
- **Archetype:** `file_cluster_8` (Distance: 12.98 IQR)
- **Magnitude:** 1605.18 | **LOC:** 838 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.8732%), Tech Debt (96.0381%)
- **Heaviest Functions:** `refresh` (Impact: 334.6), `init` (Impact: 258.3), `createStream` (Impact: 202.3)

### 2. `src/sysaudio/wasapi.zig` (ZIG) -> Cumulative Risk: **773.23**
- **Archetype:** `file_cluster_8` (Distance: 12.073 IQR)
- **Magnitude:** 2126.72 | **LOC:** 1044 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.6683%), Tech Debt (97.9135%)
- **Heaviest Functions:** `refresh` (Impact: 428.0), `createAudioClient` (Impact: 377.2), `init` (Impact: 270.7)

### 3. `src/gfx/font/native/Font.zig` (ZIG) -> Cumulative Risk: **763.77**
- **Archetype:** `file_cluster_13` (Distance: 11.031 IQR)
- **Magnitude:** 201.88 | **LOC:** 116 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `render` (Impact: 118.4), `shape` (Impact: 30.1), `initBytes` (Impact: 15.3)

### 4. `src/sysgpu/opengl.zig` (ZIG) -> Cumulative Risk: **658.12**
- **Archetype:** `file_cluster_8` (Distance: 13.127 IQR)
- **Magnitude:** 3264.68 | **LOC:** 2635 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9966%), Documentation (99.654%)
- **Heaviest Functions:** `init` (Impact: 396.7), `execute` (Impact: 362.1), `applyState` (Impact: 98.3)

### 5. `src/sysaudio/pipewire.zig` (ZIG) -> Cumulative Risk: **652.13**
- **Archetype:** `file_cluster_13` (Distance: 12.995 IQR)
- **Magnitude:** 515.34 | **LOC:** 529 | **CtrlFlow:** 60.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.9998%), Documentation (99.5636%)
- **Heaviest Functions:** `createPlayer` (Impact: 83.5), `createRecorder` (Impact: 83.5), `init` (Impact: 71.0)

### 6. `src/sysgpu/d3d12.zig` (ZIG) -> Cumulative Risk: **650.1**
- **Archetype:** `file_cluster_8` (Distance: 13.191 IQR)
- **Magnitude:** 6310.54 | **LOC:** 4160 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.5478%), Documentation (99.2969%)
- **Heaviest Functions:** `init` (Impact: 2218.2), `init` (Impact: 345.6), `init` (Impact: 283.5)

### 7. `src/sysgpu/vulkan.zig` (ZIG) -> Cumulative Risk: **635.89**
- **Archetype:** `file_cluster_8` (Distance: 13.156 IQR)
- **Magnitude:** 5096.38 | **LOC:** 3622 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.7274%)
- **Heaviest Functions:** `init` (Impact: 406.2), `init` (Impact: 365.1), `init` (Impact: 310.6)

### 8. `src/sysaudio/jack.zig` (ZIG) -> Cumulative Risk: **631.88**
- **Archetype:** `file_cluster_13` (Distance: 13.091 IQR)
- **Magnitude:** 732.2 | **LOC:** 406 | **CtrlFlow:** 67.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9995%)
- **Heaviest Functions:** `init` (Impact: 136.8), `refresh` (Impact: 106.7), `createPlayer` (Impact: 57.3)

### 9. `src/sysaudio/coreaudio.zig` (ZIG) -> Cumulative Risk: **627.06**
- **Archetype:** `file_cluster_8` (Distance: 11.46 IQR)
- **Magnitude:** 999.96 | **LOC:** 770 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Tech Debt (99.8157%), Documentation (98.962%)
- **Heaviest Functions:** `refresh` (Impact: 258.3), `createRecorder` (Impact: 227.1), `createPlayer` (Impact: 93.3)

### 10. `src/sysgpu/shader/CodeGen.zig` (ZIG) -> Cumulative Risk: **620.37**
- **Archetype:** `file_cluster_6` (Distance: 19.063 IQR)
- **Magnitude:** 208.62 | **LOC:** 237 | **CtrlFlow:** 57.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (99.9994%), Dead Code (99.8507%), Documentation (95.0461%)
- **Heaviest Functions:** `generate` (Impact: 115.2), `spvMessageConsumer` (Impact: 19.5), `glslRemapResources` (Impact: 15.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/sysgpu/shader/AstGen.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.138 IQR)
- **Top Global Matches:** file_cluster_8: 13.138, file_cluster_16: 13.509, file_cluster_7: 13.588
- **Magnitude:** 9554.48 | **LOC:** 4569 | **CtrlFlow:** 74.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 11
- **Risk Profile:** Cognitive Load (28.231%), Tech Debt (9.2223%)
**Top Internal Functions/Classes:**
  * `genCall` (Impact: 1777.6 | O(N^6) | DB: 11)
  * `genFn` (Impact: 566.0 | O(N^6) | DB: 7)
  * `genTextureSampleBuiltin` (Impact: 477.1 | O(N^6) | DB: 2)
  * `genBinary` (Impact: 367.9 | O(N^6) | DB: 3)
  * `genBitcast` (Impact: 278.6 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1542`, `structural_boundaries: 537`, `args: 96`, `func_start: 96`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 65`, `state_mutation: 290`, `planned_debt: 9`, `fragile_debt: 2`
* *Architecture:* `api: 4`, `import: 6`
* *Defense:* `safety: 645`, `doc: 3`, `test: 1`, `immutability_locks: 597`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.305
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.017448
  * `Imports (Out-Degree: 4):` Ast.zig, ErrorList.zig, std, Air.zig, Token.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/d3d12.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.191 IQR)
- **Top Global Matches:** file_cluster_8: 13.191, file_cluster_0: 13.491, file_cluster_13: 13.528
- **Magnitude:** 6310.54 | **LOC:** 4160 | **CtrlFlow:** 66.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 43
- **Risk Profile:** Cognitive Load (20.2948%), Tech Debt (99.5478%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 2218.2 | O(2^N) | DB: 43)
  * `init` (Impact: 345.6 | O(2^N) | DB: 10)
  * `init` (Impact: 283.5 | O(N^6) | DB: 9)
  * `init` (Impact: 184.4 | O(N^6) | DB: 13)
  * `init` (Impact: 135.0 | O(N^6) | DB: 9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 619`, `structural_boundaries: 318`, `args: 171`, `func_start: 171`, `class_start: 47`
* *Risk/State:* `safety_bypasses: 229`, `state_mutation: 414`, `dead_code: 1`, `planned_debt: 29`, `duplicate_logic: 61`, `orphaned_logic: 20`
* *Architecture:* `api: 201`, `import: 9`
* *Defense:* `safety: 307`, `doc: 4`, `immutability_locks: 396`, `cleanup: 126`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 4):` main.zig, gpu_allocator.zig, builtin, conv.zig, utils.zig, limits.zig, shader.zig, c.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/shader/codegen/spirv.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.074 IQR)
- **Top Global Matches:** file_cluster_8: 13.074, file_cluster_16: 13.448, file_cluster_0: 13.515
- **Magnitude:** 5161.46 | **LOC:** 2826 | **CtrlFlow:** 82.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (21.671%), Tech Debt (11.3199%)
**Top Internal Functions/Classes:**
  * `emitFnVars` (Impact: 688.5 | O(2^N) | DB: 2)
  * `emitVarProto` (Impact: 435.5 | O(N^6) | DB: 2)
  * `resolve` (Impact: 359.0 | O(2^N))
  * `emitIf` (Impact: 350.4 | O(2^N))
  * `emitBinaryAir` (Impact: 337.3 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 885`, `structural_boundaries: 186`, `args: 68`, `func_start: 68`, `class_start: 19`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 109`, `dead_code: 2`, `planned_debt: 20`
* *Architecture:* `api: 4`, `import: 5`
* *Defense:* `safety: 579`, `doc: 8`, `immutability_locks: 299`, `cleanup: 32`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, spec.zig, CodeGen.zig, Air.zig, Section.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/vulkan.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.156 IQR)
- **Top Global Matches:** file_cluster_8: 13.156, file_cluster_0: 13.494, file_cluster_13: 13.532
- **Magnitude:** 5096.38 | **LOC:** 3622 | **CtrlFlow:** 73.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (18.4496%), Tech Debt (99.7274%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 406.2 | O(2^N) | DB: 9)
  * `init` (Impact: 365.1 | O(2^N) | DB: 10)
  * `init` (Impact: 310.6 | O(2^N) | DB: 5)
  * `findBestAllocator` (Impact: 238.4 | O(N^6) | DB: 1)
  * `init` (Impact: 233.7 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 587`, `structural_boundaries: 211`, `args: 150`, `func_start: 150`, `class_start: 39`
* *Risk/State:* `safety_bypasses: 162`, `high_risk_execution: 1`, `state_mutation: 286`, `planned_debt: 13`, `duplicate_logic: 66`
* *Architecture:* `api: 203`, `import: 10`
* *Defense:* `safety: 360`, `doc: 1`, `test: 1`, `sync_locks: 6`, `immutability_locks: 400`, `cleanup: 120`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 11.269
  * `Choke Point (Betweenness):` 0.000352 | `Ripple Effect (Closeness):` 0.015267
  * `Imports (Out-Degree: 3):` main.zig, main.zig, builtin, utils.zig, limits.zig, conv.zig, vulkan, shader.zig...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/Parser.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.16%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.189 IQR)
- **Top Global Matches:** file_cluster_8: 13.189, file_cluster_0: 13.624, file_cluster_13: 13.671
- **Magnitude:** 4774.12 | **LOC:** 2055 | **CtrlFlow:** 77.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (34.9524%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `attribute` (Impact: 869.0 | O(2^N) | DB: 2)
  * `typeSpecifierWithoutIdent` (Impact: 451.6 | O(N^6) | DB: 4)
  * `lhsExpression` (Impact: 293.7 | O(2^N))
  * `ifStatement` (Impact: 263.1 | O(2^N))
  * `switchStatement` (Impact: 205.9 | O(N^5))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 893`, `structural_boundaries: 260`, `args: 74`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 18`, `state_mutation: 105`, `dead_code: 3`
* *Architecture:* `api: 3`, `import: 5`
* *Defense:* `safety: 542`, `doc: 1`, `immutability_locks: 175`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.017
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021139
  * `Imports (Out-Degree: 4):` wgsl.zig, Ast.zig, ErrorList.zig, std, Token.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/metal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.051 IQR)
- **Top Global Matches:** file_cluster_8: 13.051, file_cluster_0: 13.328, file_cluster_13: 13.333
- **Magnitude:** 3404.4 | **LOC:** 2236 | **CtrlFlow:** 67.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 9
- **Risk Profile:** Cognitive Load (20.3698%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 494.5 | O(2^N) | DB: 9)
  * `init` (Impact: 181.3 | O(2^N) | DB: 5)
  * `setBindGroup` (Impact: 157.0 | O(N^6))
  * `init` (Impact: 140.5 | O(2^N) | DB: 2)
  * `init` (Impact: 124.5 | O(2^N) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 396`, `structural_boundaries: 191`, `args: 133`, `func_start: 133`, `class_start: 29`
* *Risk/State:* `safety_bypasses: 81`, `state_mutation: 176`, `planned_debt: 22`, `duplicate_logic: 60`, `orphaned_logic: 35`
* *Architecture:* `api: 149`, `concurrency: 2`, `import: 11`
* *Defense:* `safety: 212`, `test: 1`, `immutability_locks: 303`, `cleanup: 74`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` objc, main.zig, conv.zig, utils.zig, limits.zig, shader.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/opengl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.127 IQR)
- **Top Global Matches:** file_cluster_8: 13.127, file_cluster_0: 13.413, file_cluster_13: 13.432
- **Magnitude:** 3264.68 | **LOC:** 2635 | **CtrlFlow:** 62.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (23.8205%), Tech Debt (99.9966%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 396.7 | O(2^N) | DB: 38)
  * `execute` (Impact: 362.1 | O(N^6) | DB: 17)
    * *Intent:* // Internal
  * `applyState` (Impact: 98.3 | O(N^5) | DB: 1)
  * `init` (Impact: 85.9 | O(2^N) | DB: 5)
  * `init` (Impact: 82.6 | O(2^N) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 388`, `structural_boundaries: 237`, `args: 126`, `func_start: 126`, `class_start: 32`
* *Risk/State:* `safety_bypasses: 128`, `high_risk_execution: 1`, `state_mutation: 311`, `planned_debt: 14`, `duplicate_logic: 60`, `orphaned_logic: 35`
* *Architecture:* `api: 143`, `import: 9`
* *Defense:* `safety: 201`, `test: 1`, `immutability_locks: 277`, `cleanup: 92`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 3):` main.zig, builtin, utils.zig, limits.zig, shader.zig, c.zig, proc.zig, conv.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/shader/codegen/hlsl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.58 IQR)
- **Top Global Matches:** file_cluster_8: 13.58, file_cluster_11: 13.98, file_cluster_6: 13.989
- **Magnitude:** 3091.08 | **LOC:** 1190 | **CtrlFlow:** 91.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (56.28%), Tech Debt (20.9718%)
**Top Internal Functions/Classes:**
  * `emitGlobalVar` (Impact: 2693.9 | O(N^6) | DB: 8)
  * `emitStruct` (Impact: 163.0 | O(N^4) | DB: 2)
  * `structMemberLessThan` (Impact: 37.1 | O(N^1))
  * `fnParamLessThan` (Impact: 37.1 | O(N^1))
  * `gen` (Impact: 33.4 | O(N^3) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 564`, `structural_boundaries: 52`, `args: 67`, `func_start: 67`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 34`, `planned_debt: 22`
* *Architecture:* `api: 1`, `import: 3`
* *Defense:* `safety: 447`, `immutability_locks: 73`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CodeGen.zig, Air.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/win32.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.995 IQR)
- **Top Global Matches:** file_cluster_8: 10.995, file_cluster_13: 11.436, file_cluster_7: 11.484
- **Magnitude:** 2952.5 | **LOC:** 4254 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (6.369%), Tech Debt (37.3717%)
**Top Internal Functions/Classes:**
  * `MethodMixin` (Impact: 222.2 | O(2^N))
  * `MethodMixin` (Impact: 181.8 | O(2^N))
  * `MethodMixin` (Impact: 142.1 | O(2^N))
  * `MethodMixin` (Impact: 71.0 | O(2^N))
  * `MethodMixin` (Impact: 71.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 247`, `structural_boundaries: 173`, `args: 404`, `func_start: 181`, `class_start: 158`
* *Risk/State:* `safety_bypasses: 154`, `high_risk_execution: 1`, `state_mutation: 3`, `dead_code: 4`, `planned_debt: 27`, `duplicate_logic: 16`
* *Architecture:* `io: 2`, `api: 1048`, `import: 137`
* *Defense:* `safety: 4`, `immutability_locks: 1625`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` builtin, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/shader/codegen/glsl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.5 IQR)
- **Top Global Matches:** file_cluster_8: 13.5, file_cluster_13: 13.975, file_cluster_6: 13.979
- **Magnitude:** 2934.46 | **LOC:** 904 | **CtrlFlow:** 94.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (30.8801%), Tech Debt (19.6181%)
**Top Internal Functions/Classes:**
  * `emitFn` (Impact: 1504.1 | O(N^5) | DB: 3)
  * `gen` (Impact: 1208.3 | O(N^6) | DB: 4)
  * `emitGlobal` (Impact: 188.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 429`, `structural_boundaries: 27`, `args: 59`, `func_start: 59`
* *Risk/State:* `safety_bypasses: 4`, `state_mutation: 17`, `planned_debt: 15`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 368`, `immutability_locks: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CodeGen.zig, Air.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/shader/codegen/msl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.32%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.499 IQR)
- **Top Global Matches:** file_cluster_8: 13.499, file_cluster_6: 13.911, file_cluster_11: 13.921
- **Magnitude:** 2732.42 | **LOC:** 1221 | **CtrlFlow:** 93.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (51.3417%), Tech Debt (19.9827%)
**Top Internal Functions/Classes:**
  * `emitAssign` (Impact: 632.1 | O(N^4) | DB: 2)
  * `emitDiscard` (Impact: 559.5 | O(N^4) | DB: 2)
  * `emitStageInType` (Impact: 386.1 | O(N^4) | DB: 2)
  * `emitGlobalConst` (Impact: 380.0 | O(N^5) | DB: 3)
  * `gen` (Impact: 250.5 | O(N^6) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 600`, `structural_boundaries: 41`, `args: 71`, `func_start: 71`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 32`, `dead_code: 1`, `planned_debt: 22`
* *Architecture:* `api: 1`, `import: 6`
* *Defense:* `safety: 489`, `immutability_locks: 57`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` CodeGen.zig, Air.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/module.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.11%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.456 IQR)
- **Top Global Matches:** file_cluster_16: 12.456, file_cluster_11: 12.504, file_cluster_12: 12.572
- **Magnitude:** 2387.88 | **LOC:** 1021 | **CtrlFlow:** 69.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (30.7933%), Tech Debt (24.4207%)
**Top Internal Functions/Classes:**
  * `Objects` (Impact: 1186.1 | O(2^N) | DB: 3)
  * `Modules` (Impact: 531.6 | O(2^N) | DB: 6)
  * `validate` (Impact: 419.4 | O(2^N) | DB: 12)
    * *Intent:* /// Validates that the given struct is a Mach module.
  * `ModuleTagEnum` (Impact: 46.9 | O(N^4) | DB: 2)
    * *Intent:* /// Enum describing all mach_tags for a given comptime-known module.
  * `ModuleFunctionName2` (Impact: 20.9 | O(N^3) | DB: 2)
    * *Intent:* /// Enum describing all declarations for a given comptime-known module. // TODO: unify with ModuleFu...
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 190`, `structural_boundaries: 83`, `args: 56`, `func_start: 55`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 38`, `high_risk_execution: 3`, `state_mutation: 70`, `dead_code: 2`, `planned_debt: 22`
* *Architecture:* `api: 66`, `concurrency: 7`, `import: 4`
* *Defense:* `safety: 48`, `doc: 136`, `test: 3`, `sync_locks: 12`, `immutability_locks: 128`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 5.06
  * `Choke Point (Betweenness):` 5.9e-05 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 2):` graph.zig, main.zig, StringTable.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/print_air.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.256 IQR)
- **Top Global Matches:** file_cluster_8: 13.256, file_cluster_16: 13.521, file_cluster_0: 13.788
- **Magnitude:** 2222.76 | **LOC:** 529 | **CtrlFlow:** 98.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (32.6482%), Tech Debt (10.4797%)
**Top Internal Functions/Classes:**
  * `Printer` (Impact: 2195.6 | O(N^6) | DB: 5)
  * `printAir` (Impact: 8.3 | O(N^2) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 311`, `structural_boundaries: 6`, `args: 31`, `func_start: 31`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 7`, `planned_debt: 1`
* *Architecture:* `io: 2`, `api: 2`, `import: 2`
* *Defense:* `safety: 288`, `immutability_locks: 38`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.883
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 1):` Air.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/sysaudio/wasapi.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.073 IQR)
- **Top Global Matches:** file_cluster_8: 12.073, file_cluster_13: 12.419, file_cluster_0: 12.473
- **Magnitude:** 2126.72 | **LOC:** 1044 | **CtrlFlow:** 49.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (40.8254%), Tech Debt (97.9135%)
**Top Internal Functions/Classes:**
  * `refresh` (Impact: 428.0 | O(N^6) | DB: 15)
  * `createAudioClient` (Impact: 377.2 | O(N^4) | DB: 1)
  * `init` (Impact: 270.7 | O(2^N) | DB: 4)
  * `readThread` (Impact: 107.1 | O(N^5) | DB: 5)
  * `writeThread` (Impact: 107.0 | O(N^5) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 302`, `structural_boundaries: 312`, `args: 40`, `func_start: 40`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 150`, `state_mutation: 150`, `planned_debt: 1`, `duplicate_logic: 13`, `orphaned_logic: 6`
* *Architecture:* `io: 8`, `api: 25`, `concurrency: 6`, `import: 5`
* *Defense:* `safety: 41`, `immutability_locks: 69`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` backends.zig, std, util.zig, win32.zig, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysaudio/alsa.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.98 IQR)
- **Top Global Matches:** file_cluster_8: 12.98, file_cluster_13: 13.124, file_cluster_0: 13.205
- **Magnitude:** 1605.18 | **LOC:** 838 | **CtrlFlow:** 62.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 31
- **Risk Profile:** Cognitive Load (47.6176%), Tech Debt (96.0381%)
**Top Internal Functions/Classes:**
  * `refresh` (Impact: 334.6 | O(N^6) | DB: 19)
  * `init` (Impact: 258.3 | O(2^N) | DB: 31)
  * `createStream` (Impact: 202.3 | O(N^4) | DB: 2)
  * `deviceEventsLoop` (Impact: 142.7 | O(N^6) | DB: 28)
  * `volume` (Impact: 53.0 | O(N^5) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 210`, `structural_boundaries: 124`, `args: 86`, `func_start: 31`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 28`, `state_mutation: 138`, `duplicate_logic: 13`, `orphaned_logic: 8`
* *Architecture:* `io: 25`, `api: 30`, `concurrency: 9`, `import: 8`
* *Defense:* `safety: 57`, `immutability_locks: 114`, `cleanup: 15`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` main.zig, builtin, backends.zig, std, util.zig, asoundlib.h, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/sysgpu/interface.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.72%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.414 IQR)
- **Top Global Matches:** file_cluster_8: 10.414, file_cluster_7: 10.982, file_cluster_1: 11.242
- **Magnitude:** 1562.84 | **LOC:** 2696 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^3) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (5.9011%), Tech Debt (8.496%)
**Top Internal Functions/Classes:**
  * `Export` (Impact: 217.5 | O(N^3))
    * *Intent:* /// Exports C ABI function declarations for the given sysgpu.Interface implementation.
  * `Interface` (Impact: 9.5 | O(N^1))
    * *Intent:* /// Verifies that a sysgpu.Interface implementation exposes the expected function declarations.
  * `sysgpuRenderPipelineGetBindGroupLayout` (Impact: 7.1 | O(N^3))
    * *Intent:* // SYSGPU_EXPORT WGPUBindGroupLayout sysgpuRenderPipelineGetBindGroupLayout(WGPURenderPipeline rende...
  * `sysgpuSharedTextureMemoryCreateTexture` (Impact: 7.1 | O(N^3))
    * *Intent:* // SYSGPU_EXPORT WGPUTexture sysgpuSharedTextureMemoryCreateTexture(WGPUSharedTextureMemory sharedTe...
  * `sysgpuSwapChainGetCurrentTexture` (Impact: 7.1 | O(N^3))
    * *Intent:* // SYSGPU_EXPORT WGPUTexture sysgpuSwapChainGetCurrentTexture(WGPUSwapChain swapChain);
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 69`, `structural_boundaries: 274`, `args: 646`, `func_start: 432`
* *Risk/State:* `safety_bypasses: 217`, `planned_debt: 3`
* *Architecture:* `api: 438`, `import: 4`
* *Defense:* `doc: 7`, `test: 1`, `immutability_locks: 372`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 82.638
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.191122
  * `Imports (Out-Degree: 0):` root, main.zig
  * `Imported By (In-Degree: 25):` (Excluded from Brief to save tokens)

### `src/sysgpu/shader/Air.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.337 IQR)
- **Top Global Matches:** file_cluster_8: 10.337, file_cluster_7: 10.867, file_cluster_16: 11.022
- **Magnitude:** 1362.94 | **LOC:** 1045 | **CtrlFlow:** 63.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (9.6135%), Tech Debt (21.758%)
**Top Internal Functions/Classes:**
  * `resolveConstExpr` (Impact: 805.8 | O(2^N) | DB: 2)
  * `findFunction` (Impact: 37.1 | O(N^5))
  * `typeSize` (Impact: 31.8 | O(N^3))
  * `resolveInt` (Impact: 30.9 | O(N^4))
  * `mod` (Impact: 21.1 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 157`, `structural_boundaries: 91`, `args: 36`, `func_start: 36`, `class_start: 74`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 9`, `duplicate_logic: 4`
* *Architecture:* `api: 97`, `import: 5`
* *Defense:* `safety: 41`, `doc: 3`, `immutability_locks: 99`, `cleanup: 14`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 14.737
  * `Choke Point (Betweenness):` 0.00094 | `Ripple Effect (Closeness):` 0.030534
  * `Imports (Out-Degree: 4):` AstGen.zig, wgsl.zig, ErrorList.zig, Ast.zig, std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/sysaudio/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.381 IQR)
- **Top Global Matches:** file_cluster_8: 11.381, file_cluster_13: 11.856, file_cluster_0: 11.927
- **Magnitude:** 1273.02 | **LOC:** 511 | **CtrlFlow:** 73.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (19.1559%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 169.4 | O(2^N))
  * `convertTo` (Impact: 60.3 | O(N^3))
  * `convertFrom` (Impact: 60.3 | O(N^3))
  * `createPlayer` (Impact: 56.4 | O(2^N))
  * `createRecorder` (Impact: 56.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 48`, `args: 38`, `func_start: 35`, `class_start: 23`
* *Risk/State:* `safety_bypasses: 16`, `state_mutation: 3`, `planned_debt: 3`, `duplicate_logic: 19`
* *Architecture:* `api: 72`, `import: 5`
* *Defense:* `safety: 47`, `test: 1`, `immutability_locks: 57`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` conv.zig, builtin, backends.zig, util.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/gfx/Text.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_6` (Drift: 12.584 IQR)
- **Top Global Matches:** file_cluster_6: 12.584, file_cluster_11: 12.8, file_cluster_8: 12.831
- **Magnitude:** 1095.4 | **LOC:** 666 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (8.4236%), Tech Debt (60.7925%)
**Top Internal Functions/Classes:**
  * `updatePipelineBuffers` (Impact: 694.8 | O(2^N) | DB: 15)
  * `rebuildPipeline` (Impact: 209.4 | O(2^N) | DB: 1)
  * `tick` (Impact: 79.8 | O(N^4) | DB: 2)
  * `renderPipeline` (Impact: 29.1 | O(2^N) | DB: 1)
  * `deinit` (Impact: 5.8 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 81`, `structural_boundaries: 33`, `args: 6`, `func_start: 6`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 57`, `dead_code: 7`, `planned_debt: 25`, `fragile_debt: 2`
* *Architecture:* `api: 5`, `import: 2`
* *Defense:* `safety: 37`, `doc: 70`, `immutability_locks: 81`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.947
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.007634
  * `Imports (Out-Degree: 0):` main.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/core/linux/Wayland.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.35%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.272 IQR)
- **Top Global Matches:** file_cluster_8: 11.272, file_cluster_13: 11.496, file_cluster_2: 11.654
- **Magnitude:** 1054.32 | **LOC:** 993 | **CtrlFlow:** 69.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (54.9562%), Tech Debt (47.7381%)
**Top Internal Functions/Classes:**
  * `initWindow` (Impact: 326.6 | O(2^N) | DB: 2)
  * `registryHandleGlobal` (Impact: 181.4 | O(N^4) | DB: 1)
  * `seatHandleCapabilities` (Impact: 62.3 | O(N^4) | DB: 2)
  * `keyboardHandleKeymap` (Impact: 58.1 | O(N^4) | DB: 23)
  * `keyboardHandleKey` (Impact: 41.1 | O(N^5) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 57`, `args: 38`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 62`, `state_mutation: 48`, `planned_debt: 15`, `duplicate_logic: 2`
* *Architecture:* `io: 16`, `api: 22`, `import: 15`
* *Defense:* `safety: 35`, `immutability_locks: 105`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Linux.zig, xkbcommon-compose.h, wayland-relative-pointer-unstable-v1-client-protocol.h, xkbcommon.h, Core.zig, wayland-xdg-decoration-client-protocol.h, wayland-client-protocol.h, wayland-xdg-shell-client-protocol.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/mpsc.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_4` (Drift: 12.683 IQR)
- **Top Global Matches:** file_cluster_4: 12.683, file_cluster_8: 12.705, file_cluster_7: 12.836
- **Magnitude:** 1031.4 | **LOC:** 370 | **CtrlFlow:** 71.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (31.8515%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Pool` (Impact: 475.1 | O(2^N) | DB: 5)
    * *Intent:* /// Lock-free atomic pool of nodes for memory allocation
  * `Queue` (Impact: 441.4 | O(2^N) | DB: 2)
    * *Intent:* /// Multi Producer, Single Consumer lock-free FIFO queue
  * `run` (Impact: 18.5 | O(N^6) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 86`, `structural_boundaries: 35`, `args: 13`, `func_start: 13`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 9`, `state_mutation: 37`
* *Architecture:* `api: 13`, `concurrency: 40`, `import: 1`
* *Defense:* `safety: 39`, `doc: 39`, `test: 6`, `sync_locks: 10`, `immutability_locks: 18`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 11.19
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.017176
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `src/sysaudio/coreaudio.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.46 IQR)
- **Top Global Matches:** file_cluster_8: 11.46, file_cluster_13: 11.73, file_cluster_0: 11.88
- **Magnitude:** 999.96 | **LOC:** 770 | **CtrlFlow:** 62.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (20.8122%), Tech Debt (99.8157%)
**Top Internal Functions/Classes:**
  * `refresh` (Impact: 258.3 | O(N^6) | DB: 8)
  * `createRecorder` (Impact: 227.1 | O(N^4) | DB: 5)
  * `createPlayer` (Impact: 93.3 | O(N^3) | DB: 3)
  * `captureCallback` (Impact: 70.6 | O(N^3) | DB: 1)
  * `init` (Impact: 35.4 | O(2^N) | DB: 4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 91`, `args: 26`, `func_start: 26`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 22`, `high_risk_execution: 1`, `state_mutation: 60`, `dead_code: 1`, `planned_debt: 2`, `duplicate_logic: 13`, `orphaned_logic: 5`
* *Architecture:* `io: 1`, `api: 27`, `import: 9`
* *Defense:* `safety: 37`, `immutability_locks: 49`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` objc, CoreAudio.h, builtin, backends.zig, std, util.zig, AudioUnit.h, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/core/linux/X11.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.558 IQR)
- **Top Global Matches:** file_cluster_8: 11.558, file_cluster_13: 11.75, file_cluster_11: 11.768
- **Magnitude:** 986.64 | **LOC:** 912 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 38
- **Risk Profile:** Cognitive Load (52.1933%), Tech Debt (69.4352%)
**Top Internal Functions/Classes:**
  * `initWindow` (Impact: 487.9 | O(2^N) | DB: 38)
    * *Intent:* // Mutable fields only used by main thread // Mutable state fields; read/write by any thread
  * `processEvent` (Impact: 159.3 | O(N^6) | DB: 3)
    * *Intent:* /// Handle XEvents. Window object can be modified.
  * `createStandardCursor` (Impact: 45.3 | O(N^4))
  * `setDisplayMode` (Impact: 37.4 | O(N^4) | DB: 1)
  * `load` (Impact: 20.6 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 132`, `structural_boundaries: 73`, `args: 24`, `func_start: 19`, `class_start: 9`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 65`, `dead_code: 2`, `planned_debt: 10`, `duplicate_logic: 5`
* *Architecture:* `io: 11`, `api: 24`, `import: 12`
* *Defense:* `safety: 43`, `doc: 1`, `immutability_locks: 193`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` Linux.zig, Xatom.h, Core.zig, builtin, xkbcommon.h, Xcursor.h, Xrandr.h, Xlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysgpu/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.341 IQR)
- **Top Global Matches:** file_cluster_8: 12.341, file_cluster_0: 12.72, file_cluster_13: 12.721
- **Magnitude:** 946.98 | **LOC:** 1381 | **CtrlFlow:** 75.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 4
- **Risk Profile:** Cognitive Load (24.5347%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `createInstance` (Impact: 674.4 | O(N^5) | DB: 4)
  * `init` (Impact: 10.6 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 117`, `structural_boundaries: 39`, `args: 219`, `func_start: 218`
* *Risk/State:* `safety_bypasses: 248`, `high_risk_execution: 77`, `state_mutation: 16`, `dead_code: 1`
* *Architecture:* `api: 223`, `import: 11`
* *Defense:* `safety: 73`, `test: 2`, `immutability_locks: 242`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` main.zig, build-options, test.zig, builtin, utils.zig, shader.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/sysaudio/pulseaudio.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.748 IQR)
- **Top Global Matches:** file_cluster_8: 11.748, file_cluster_13: 12.102, file_cluster_7: 12.244
- **Magnitude:** 926.62 | **LOC:** 823 | **CtrlFlow:** 58.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (16.9302%), Tech Debt (96.4876%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 194.4 | O(2^N) | DB: 1)
  * `createPlayer` (Impact: 76.0 | O(N^4) | DB: 2)
  * `createRecorder` (Impact: 76.0 | O(N^4) | DB: 2)
  * `deviceInfoOp` (Impact: 41.2 | O(N^4) | DB: 1)
  * `refresh` (Impact: 32.1 | O(N^4))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 94`, `args: 86`, `func_start: 39`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `state_mutation: 49`, `duplicate_logic: 13`, `orphaned_logic: 7`
* *Architecture:* `api: 29`, `import: 8`
* *Defense:* `safety: 47`, `immutability_locks: 134`, `cleanup: 16`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 4.173
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` main.zig, builtin, backends.zig, std, util.zig, pulseaudio.h, main.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_0
- `src/math/collision.zig` (ZIG) | Magnitude: 601.5 | Delta: **0.021 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 645, branch: 232, globals: 150, encapsulation: 145

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `examples/sprite/App.zig` (ZIG) | Magnitude: 480.44 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 201, globals: 49, encapsulation: 48, immutability_locks: 38
- `src/sysaudio/backends.zig` (ZIG) | Magnitude: 20.8 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 81, import: 47, branch: 12, globals: 6
- `src/time/Timer.zig` (ZIG) | Magnitude: 30.78 | Delta: **0.037 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: branch: 6, args: 6, func_start: 6, api: 6
- `src/sysaudio/pipewire.zig` (ZIG) | Magnitude: 515.34 | Delta: **0.064 IQR** | Secondary Pull: `file_cluster_0`
  * Top Architectural Signatures: indent_spaces: 416, pointers: 110, branch: 72, immutability_locks: 71
- `src/core/Linux.zig` (ZIG) | Magnitude: 751.36 | Delta: **0.067 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 156, branch: 77, immutability_locks: 48, encapsulation: 41

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/module.zig` (ZIG) | Magnitude: 2387.88 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 811, branch: 190, doc: 136, globals: 130

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/text/App.zig` (ZIG) | Magnitude: 449.52 | Delta: **0.013 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 190, globals: 50, encapsulation: 47, immutability_locks: 46

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/custom-renderer/App.zig` (ZIG) | Magnitude: 270.7 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 131, branch: 32, globals: 31, state_mutation: 29
- `examples/piano/App.zig` (ZIG) | Magnitude: 353.6 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 192, globals: 41, immutability_locks: 38, encapsulation: 38
- `examples/hardware-check/App.zig` (ZIG) | Magnitude: 732.68 | Delta: **0.095 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 281, globals: 61, encapsulation: 59, branch: 56
- `src/testing.zig` (ZIG) | Magnitude: 230.68 | Delta: **0.11 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 129, doc: 57, branch: 36, immutability_locks: 29
- `examples/play-opus/App.zig` (ZIG) | Magnitude: 269.9 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 124, globals: 34, immutability_locks: 31, encapsulation: 28

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/mpsc.zig` (ZIG) | Magnitude: 1031.4 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 294, branch: 86, bitwise_ops: 61, concurrency: 40

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `src/gfx/Sprite.zig` (ZIG) | Magnitude: 510.3 | Delta: **0.015 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 378, encapsulation: 73, globals: 71, bitwise_ops: 70
- `src/gfx/font/main.zig` (ZIG) | Magnitude: 43.28 | Delta: **0.056 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 173, branch: 41, immutability_locks: 27, dead_code: 25
- `src/sysgpu/shader/CodeGen.zig` (ZIG) | Magnitude: 208.62 | Delta: **0.063 IQR** | Secondary Pull: `file_cluster_9`
  * Top Architectural Signatures: indent_spaces: 171, immutability_locks: 38, branch: 33, structural_boundaries: 24
- `examples/core-triangle/App.zig` (ZIG) | Magnitude: 100.86 | Delta: **0.065 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 95, globals: 24, immutability_locks: 22, encapsulation: 21
- `examples/core-custom-entrypoint/App.zig` (ZIG) | Magnitude: 103.1 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 95, globals: 23, immutability_locks: 22, encapsulation: 20

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/core/linux/wayland.c` (C) | Magnitude: 11.56 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: import: 3
- `src/sysgpu/shader/codegen/spirv/Section.zig` (ZIG) | Magnitude: 538.08 | Delta: **0.043 IQR** | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 202, bitwise_ops: 75, branch: 67, safety: 37
- `src/time/main.zig` (ZIG) | Magnitude: 18.16 | Delta: **0.046 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: api: 4, globals: 4, immutability_locks: 4, import: 3
- `src/sysgpu/shader/Ast.zig` (ZIG) | Magnitude: 152.32 | Delta: **0.048 IQR** | Secondary Pull: `file_cluster_7`
  * Top Architectural Signatures: indent_spaces: 582, doc: 301, branch: 43, immutability_locks: 42
- `src/sysgpu/sysgpu/adapter.zig` (ZIG) | Magnitude: 131.96 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 96, immutability_locks: 32, api: 25, globals: 22

### Mixed-Responsibility Refactoring Targets for: file_cluster_9
- `src/sysgpu/shader/test.zig` (ZIG) | Magnitude: 79.42 | Delta: **0.062 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 193, branch: 168, safety: 150, dead_code: 54

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 🔥 The Hotspot Matrix (High Volatility + High Risk)
These files are messy, complex, and modified frequently. They are the primary source of developer friction.

- `src/gfx/font/native/Font.zig` -> Churn: **100.0%** | Cog Load: 54.264% | Debt: 98.0911%
- `src/gfx/font/main.zig` -> Churn: **79.25%** | Cog Load: 21.8129% | Debt: 57.899%

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/sysgpu/vulkan.zig` -> **Shail Patel** (100.0% isolated ownership) | Magnitude: 5096.38
- `src/module.zig` -> **OliveThePuffin** (100.0% isolated ownership) | Magnitude: 2387.88
- `src/gfx/Text.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 1095.4
- `src/Audio.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 517.58
- `examples/glyphs/App.zig` -> **Emi** (100.0% isolated ownership) | Magnitude: 332.14

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/sysgpu/vulkan.zig` -> **Severity: 0.01** (Bridge: 0.0004 * Flux: 27.1987%)
- `src/graph.zig` -> **Severity: 0.006** (Bridge: 0.0001 * Flux: 95.3832%)
- `src/module.zig` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 13.8054%)
- `src/sysgpu/utils.zig` -> **Severity: 0.001** (Bridge: 0.0001 * Flux: 16.8868%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/sysgpu/sysgpu/interface.zig` -> **Severity: 15.024** (Embedded: 0.1911 * Error Risk: 78.6111%)
- `src/sysgpu/sysgpu/buffer.zig` -> **Severity: 5.428** (Embedded: 0.0748 * Error Risk: 72.5532%)
- `src/sysgpu/sysgpu/sampler.zig` -> **Severity: 3.404** (Embedded: 0.0538 * Error Risk: 63.3333%)
- `src/sysgpu/utils.zig` -> **Severity: 1.931** (Embedded: 0.0416 * Error Risk: 46.4557%)
- `src/sysgpu/sysgpu/texture_view.zig` -> **Severity: 1.241** (Embedded: 0.0727 * Error Risk: 17.0538%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/sysgpu/sysgpu/interface.zig` -> **Severity: 8240.661** (Blast Radius: 82.638 * Doc Risk: 99.72%)
- `src/math/vec.zig` -> **Severity: 4333.664** (Blast Radius: 43.611 * Doc Risk: 99.3709%)
- `src/math/quat.zig` -> **Severity: 3575.213** (Blast Radius: 40.698 * Doc Risk: 87.8474%)
- `src/math/mat.zig` -> **Severity: 2839.023** (Blast Radius: 40.698 * Doc Risk: 69.7583%)
- `src/sysaudio/backends.zig` -> **Severity: 2307.046** (Blast Radius: 32.555 * Doc Risk: 70.8661%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
