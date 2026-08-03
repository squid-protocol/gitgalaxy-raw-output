# ARCHITECTURAL_BRIEF: capy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/capy` |
| **Timestamp** | `2026-08-03T20:08:27.581616+00:00` |
| **Scan Duration** | `0.81s` |
| **Git Branch** | `master` |
| **Git Commit** | `fd77077e296a969ae258c595e75a0723183b3138` |
| **Git Remote** | `https://github.com/capy-ui/capy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 143 malicious artifacts.

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
| Total Artifacts | 517 |
| Analyzed Artifacts (Scanned) | 150 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 367 |
| Total LOC | 22626 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 29.0% |
| Dominant Lang | ZIG |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6158 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.2721 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 12.7% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.9407 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 12 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| ZIG | 131 | 21184 | 87.3% |
| MARKDOWN | 4 | 0 | 2.7% |
| NIX | 3 | 180 | 2.0% |
| JAVA | 2 | 25 | 1.3% |
| C | 2 | 30 | 1.3% |
| GLSL | 2 | 8 | 1.3% |
| JAVASCRIPT | 2 | 541 | 1.3% |
| PLAINTEXT | 1 | 0 | 0.7% |
| HTML | 1 | 26 | 0.7% |
| MAKEFILE | 1 | 632 | 0.7% |
| XML | 1 | 0 | 0.7% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `4.473`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_13 | 64 | 42.7% |
| file_cluster_8 | 46 | 30.7% |
| file_cluster_2 | 24 | 16.0% |
| file_cluster_11 | 4 | 2.7% |
| file_cluster_16 | 2 | 1.3% |
| file_cluster_17 | 2 | 1.3% |
| file_cluster_4 | 2 | 1.3% |
| file_cluster_6 | 1 | 0.7% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 5 | 3.3% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 367*

**Composition by Extension & Reason:**
- `.zig`: 333x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Monolithic Amalgamation: 72269 LOC exceeds safe regex boundaries)
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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 94.6 | 25.7 | 21.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 80.8 | 36.7 | 26.7 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 30.1 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 35.6 | 2.9 | 80.0 |
| API Exposure | 0.0 | 18.4 | 4.8 | 4.3 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 9.6 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.1 | 3.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 97.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 57.6 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 71.9 | 99.9 | 0.0 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 67.7 | 100.0 | 100.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 100.0 | 12.0 | 19.9 | 20.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 0.7 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.1 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `android/Sdk.zig` (Hits: 28)
- `src/backends/win32/win32.zig` (Hits: 25)
- `src/assets.zig` (Hits: 10)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **internal.zig** (`src/internal.zig`) — 14 inbound connections
2. **js.zig** (`src/backends/wasm/js.zig`) — 13 inbound connections
3. **data.zig** (`src/data.zig`) — 12 inbound connections
4. **AnimationController.zig** (`src/AnimationController.zig`) — 6 inbound connections
5. **c.zig** (`android/src/c.zig`) — 5 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **capy.zig** (`src/capy.zig`) — 34 outbound dependencies
2. **backend.zig** (`src/backends/gtk/backend.zig`) — 22 outbound dependencies
3. **backend.zig** (`src/backends/wasm/backend.zig`) — 17 outbound dependencies
4. **android-support.zig** (`android/src/android-support.zig`) — 11 outbound dependencies
5. **c.zig** (`android/src/c.zig`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `Atom` (@ `src/data.zig`) -> Impact: **1765.6** | LOC: 592
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `init` (@ `src/backends/win32/backend.zig`) -> Impact: **1300.7** | LOC: 1234
- `ListAtom` (@ `src/data.zig`) -> Impact: **642.7** | LOC: 254
  * *Intent:* /// A list of atoms, that is itself an atom.
- `Widgeting` (@ `src/internal.zig`) -> Impact: **638.6** | LOC: 313
  * *Intent:* /// Convenience function for creating widgets
- `timerInvoke` (@ `android/examples/invocationhandler/main.zig`) -> Impact: **614.7** | LOC: 220
- `add` (@ `src/backends/android/backend.zig`) -> Impact: **427.7** | LOC: 240
- `Events` (@ `src/internal.zig`) -> Impact: **417.8** | LOC: 236
  * *Intent:* /// Convenience function for creating widgets
- `mainLoop` (@ `android/examples/egl/main.zig`) -> Impact: **393.2** | LOC: 346
- `GridLayout` (@ `src/containers.zig`) -> Impact: **381.7** | LOC: 238
  * *Intent:* /// Grid layout based on the CSS Grid algorithm
- `fromIid` (@ `android/src/opensl.zig`) -> Impact: **376.9** | LOC: 56

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `mainLoop` (@ `android/examples/egl/main.zig`) -> **O(2^N) [Recursive]**
- `init` (@ `src/backends/win32/backend.zig`) -> **O(2^N) [Recursive]**
- `Atom` (@ `src/data.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `ListAtom` (@ `src/data.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// A list of atoms, that is itself an atom.
- `add` (@ `src/backends/android/backend.zig`) -> **O(2^N) [Recursive]**
- `setText` (@ `src/backends/android/backend.zig`) -> **O(2^N) [Recursive]**
- `getChild` (@ `src/containers.zig`) -> **O(2^N) [Recursive]**
  * *Intent:* /// Searches recursively for a component named `name` and returns the first one found. /// If no component is found, `null` is returned.
- `hasUniqueRepresentation` (@ `src/trait.zig`) -> **O(2^N) [Recursive]**
- `create` (@ `android/Sdk.zig`) -> **O(2^N) [Recursive]**
- `create` (@ `android/Sdk.zig`) -> **O(2^N) [Recursive]**

### Highest Data Gravity (Database Complexity)
- `init` (@ `src/backends/win32/backend.zig`) -> DB Complexity: **46**
- `Atom` (@ `src/data.zig`) -> DB Complexity: **33**
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `mainLoop` (@ `android/examples/egl/main.zig`) -> DB Complexity: **26**
- `init` (@ `android/Sdk.zig`) -> DB Complexity: **22**
  * *Intent:* /// Initializes the android SDK. /// It requires some input on which versions of the tool chains should be used
- `add` (@ `android/Sdk.zig`) -> DB Complexity: **21**
- `createApp` (@ `android/Sdk.zig`) -> DB Complexity: **20**
  * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
- `main` (@ `android/tools/zip_add.zig`) -> DB Complexity: **18**
  * *Intent:* // zip_add file.zip local_path zip_path
- `get` (@ `src/assets.zig`) -> DB Complexity: **18**
- `addChunk` (@ `src/backends/wasm/capy.js`) -> DB Complexity: **18**
- `make` (@ `android/Sdk.zig`) -> DB Complexity: **16**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 25 | 10153.5 | 28.74% | 52.22% |
| `android/src` | 13 | 4321.32 | 27.8% | 28.33% |
| `src/backends/win32` | 6 | 2269.2 | 19.18% | 23.96% |
| `src/backends/wasm` | 16 | 1899.74 | 23.15% | 37.85% |
| `src/components` | 15 | 1895.62 | 22.28% | 36.79% |
| `examples` | 23 | 1890.58 | 36.29% | 0.0% |
| `src/backends/gtk` | 19 | 1595.78 | 19.69% | 29.51% |
| `android` | 5 | 1445.54 | 5.29% | 6.88% |
| `src/backends/android` | 1 | 1336.82 | 31.53% | 71.38% |
| `android/examples/egl` | 1 | 894.02 | 23.01% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/async.zig` -> **100.0%** Exposure
- `src/audio.zig` -> **100.0%** Exposure
- `src/c_api.zig` -> **100.0%** Exposure
- `src/components/Canvas.zig` -> **100.0%** Exposure
- `src/http.zig` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/backends/wasm/capy.js` -> **100.0%** Exposure
- `src/backends/win32/Monitor.zig` -> **97.6199%** Exposure
- `src/listener.zig` -> **97.5873%** Exposure
- `src/fuzz.zig` -> **97.377%** Exposure
- `src/backends/wasm/capy-worker.js` -> **97.3132%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/http.zig` -> **0** Orphaned Functions | **14** Duplicates
- `src/c_api.zig` -> **12** Orphaned Functions | **0** Duplicates
- `src/backends/gles/backend.zig` -> **0** Orphaned Functions | **9** Duplicates
- `src/data.zig` -> **0** Orphaned Functions | **9** Duplicates
- `src/components/Canvas.zig` -> **0** Orphaned Functions | **8** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/window.zig`** -> AI Confidence: **99.43%**
2. **`src/backends/gtk/Window.zig`** -> AI Confidence: **99.39%**
3. **`src/backends/wasm/backend.zig`** -> AI Confidence: **99.39%**
4. **`android/src/android-support.zig`** -> AI Confidence: **99.34%**
5. **`src/internal.zig`** -> AI Confidence: **99.34%**
6. **`src/containers.zig`** -> AI Confidence: **99.33%**
7. **`src/backends/gtk/backend.zig`** -> AI Confidence: **99.31%**
8. **`src/backends/macos/backend.zig`** -> AI Confidence: **99.31%**
9. **`src/components/Image.zig`** -> AI Confidence: **99.31%**
10. **`examples/transition.zig`** -> AI Confidence: **99.29%**
11. **`src/backends/wasm/common.zig`** -> AI Confidence: **99.28%**
12. **`src/dev_tools.zig`** -> AI Confidence: **99.26%**
13. **`android/src/c.zig`** -> AI Confidence: **99.25%**
14. **`src/capy.zig`** -> AI Confidence: **99.25%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `src/backends/wasm/capy.js` -> **100.0%** Exposure
- `android/Sdk.zig` -> **20.0%** Exposure
- `android/examples/egl/main.zig` -> **20.0%** Exposure
- `android/examples/invocationhandler/main.zig` -> **20.0%** Exposure
- `android/examples/textview/main.zig` -> **20.0%** Exposure
### Weaponizable Injection Vectors
- `android/Sdk.zig` -> **99.9961%** Exposure
### Raw Memory Manipulation
- `android/src/android-bind.zig` -> **9.9976%** Exposure
- `src/widget.zig` -> **0.1908%** Exposure
- `android/src/opensl.zig` -> **0.1295%** Exposure
- `src/backends/gtk/common.zig` -> **0.086%** Exposure
- `src/internal.zig` -> **0.0405%** Exposure
### Algorithmic DoS Exposure
- `android/Sdk.zig` -> **100.0%** Exposure
- `android/examples/egl/main.zig` -> **100.0%** Exposure
- `android/examples/invocationhandler/main.zig` -> **100.0%** Exposure
- `android/examples/textview/main.zig` -> **100.0%** Exposure
- `android/src/NativeActivity.zig` -> **100.0%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `412` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/async.zig` (ZIG) -> Cumulative Risk: **755.03**
- **Archetype:** `file_cluster_13` (Distance: 11.638 IQR)
- **Magnitude:** 90.72 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), Spec Match (100.0%), Algorithmic Dos (99.9996%)
- **Heaviest Functions:** `getFreeThread` (Impact: 26.7), `init` (Impact: 14.1), `taskRunner` (Impact: 10.3)

### 2. `src/backends/wasm/capy.js` (JAVASCRIPT) -> Cumulative Risk: **740.33**
- **Archetype:** `file_cluster_4` (Distance: 13.479 IQR)
- **Magnitude:** 285.36 | **LOC:** 635 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Algorithmic Dos (100.0%), Logic Bomb (100.0%)
- **Heaviest Functions:** `addChunk` (Impact: 83.4), `pushAnswer` (Impact: 31.6), `log` (Impact: 11.6)

### 3. `android/src/aaudio.zig` (ZIG) -> Cumulative Risk: **731.21**
- **Archetype:** `file_cluster_13` (Distance: 12.286 IQR)
- **Magnitude:** 174.62 | **LOC:** 176 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9949%), Tech Debt (96.128%)
- **Heaviest Functions:** `getOutputStream` (Impact: 72.2), `errorCallback` (Impact: 18.5), `dataCallback` (Impact: 16.0)

### 4. `android/src/opensl.zig` (ZIG) -> Cumulative Risk: **703.8**
- **Archetype:** `file_cluster_8` (Distance: 12.222 IQR)
- **Magnitude:** 712.96 | **LOC:** 497 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.414%), State Flux (96.557%)
- **Heaviest Functions:** `fromIid` (Impact: 376.9), `getOutputStream` (Impact: 82.7), `start` (Impact: 38.4)

### 5. `src/backends/android/backend.zig` (ZIG) -> Cumulative Risk: **698.91**
- **Archetype:** `file_cluster_11` (Distance: 13.114 IQR)
- **Magnitude:** 1336.82 | **LOC:** 873 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9423%), Concurrency (99.3107%)
- **Heaviest Functions:** `add` (Impact: 427.7), `Events` (Impact: 167.1), `setText` (Impact: 148.3)

### 6. `src/image.zig` (ZIG) -> Cumulative Risk: **690.67**
- **Archetype:** `file_cluster_13` (Distance: 14.007 IQR)
- **Magnitude:** 112.12 | **LOC:** 103 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9347%), State Flux (93.907%)
- **Heaviest Functions:** `readFromStream` (Impact: 18.6), `fromBytes` (Impact: 16.4), `deinit` (Impact: 14.2)

### 7. `android/src/android-support.zig` (ZIG) -> Cumulative Risk: **684.93**
- **Archetype:** `file_cluster_13` (Distance: 13.75 IQR)
- **Magnitude:** 476.16 | **LOC:** 384 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.0594%), Documentation (95.0774%)
- **Heaviest Functions:** `makeNativeActivityGlue` (Impact: 124.2), `printSymbolInfoAt` (Impact: 79.2), `panic` (Impact: 62.2)

### 8. `src/list.zig` (ZIG) -> Cumulative Risk: **665.52**
- **Archetype:** `file_cluster_13` (Distance: 12.661 IQR)
- **Magnitude:** 138.0 | **LOC:** 100 | **CtrlFlow:** 63.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9977%), Tech Debt (99.3307%)
- **Heaviest Functions:** `show` (Impact: 42.1), `columnList` (Impact: 36.3), `modelSizeChanged` (Impact: 13.7)

### 9. `build_capy.zig` (ZIG) -> Cumulative Risk: **657.15**
- **Archetype:** `file_cluster_6` (Distance: 13.694 IQR)
- **Magnitude:** 468.02 | **LOC:** 301 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Concurrency (99.3293%), Verification (80.0%)
- **Heaviest Functions:** `handler` (Impact: 220.8), `runStep` (Impact: 145.4), `create` (Impact: 30.7)

### 10. `src/backends/macos/backend.zig` (ZIG) -> Cumulative Risk: **649.98**
- **Archetype:** `file_cluster_8` (Distance: 10.668 IQR)
- **Magnitude:** 346.92 | **LOC:** 381 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Algorithmic Dos (100.0%), Documentation (99.9993%), Tech Debt (99.6626%)
- **Heaviest Functions:** `Events` (Impact: 69.8), `runStep` (Impact: 22.6), `getFlippedNSView` (Impact: 17.1)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/data.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.459 IQR)
- **Top Global Matches:** file_cluster_11: 13.459, file_cluster_13: 13.489, file_cluster_8: 13.522
- **Magnitude:** 3261.82 | **LOC:** 1349 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 33
- **Risk Profile:** Cognitive Load (41.7584%), Tech Debt (74.749%)
**Top Internal Functions/Classes:**
  * `Atom` (Impact: 1765.6 | O(2^N) | DB: 33)
    * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to //...
  * `ListAtom` (Impact: 642.7 | O(2^N) | DB: 8)
    * *Intent:* /// A list of atoms, that is itself an atom.
  * `lerp` (Impact: 241.9 | O(2^N))
    * *Intent:* /// Linear interpolation between any two values a and b with factor t. /// Both values must be of th...
  * `FormattedAtom` (Impact: 63.1 | O(N^4) | DB: 5)
    * *Intent:* // TODO: reimplement using Atom.derived and its arena allocator
  * `isAnimatableType` (Impact: 42.4 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 167`, `args: 89`, `func_start: 83`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 168`, `dead_code: 3`, `planned_debt: 8`, `duplicate_logic: 9`
* *Architecture:* `api: 78`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 123`, `doc: 77`, `test: 56`, `sync_locks: 62`, `immutability_locks: 157`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 68.771
  * `Choke Point (Betweenness):` 0.003191 | `Ripple Effect (Closeness):` 0.093185
  * `Imports (Out-Degree: 4):` trait.zig, containers.zig, AnimationController.zig, internal.zig, std
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `android/src/android-bind.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.48 IQR)
- **Top Global Matches:** file_cluster_8: 10.48, file_cluster_7: 11.011, file_cluster_1: 11.359
- **Magnitude:** 1724.1 | **LOC:** 2624 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (4.9733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__BIONIC_CAST` (Impact: 4.2 | O(N^1))
  * `__BIONIC_ALIGN` (Impact: 3.6 | O(N^1))
  * `__P` (Impact: 3.6 | O(N^1))
  * `__android_log_assert` (Impact: 3.4 | O(N^1))
  * `AHardwareBuffer_lockAndGetInfo` (Impact: 3.3 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 3`, `args: 435`, `func_start: 182`, `class_start: 68`
* *Risk/State:* None
* *Architecture:* `api: 1624`, `import: 3`
* *Defense:* `immutability_locks: 1866`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.018643
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/containers.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.687 IQR)
- **Top Global Matches:** file_cluster_11: 13.687, file_cluster_13: 13.706, file_cluster_6: 13.815
- **Magnitude:** 1686.16 | **LOC:** 924 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (26.7683%), Tech Debt (24.8305%)
**Top Internal Functions/Classes:**
  * `GridLayout` (Impact: 381.7 | O(N^6) | DB: 16)
    * *Intent:* /// Grid layout based on the CSS Grid algorithm
  * `RowLayout` (Impact: 228.4 | O(N^6) | DB: 4)
    * *Intent:* /// Arranges items horizontally.
  * `ColumnLayout` (Impact: 228.0 | O(N^6) | DB: 4)
    * *Intent:* /// Arranges items vertically.
  * `getChild` (Impact: 198.6 | O(2^N))
    * *Intent:* /// Searches recursively for a component named `name` and returns the first one found. /// If no com...
  * `show` (Impact: 61.5 | O(2^N) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 86`, `args: 42`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 101`, `dead_code: 9`, `planned_debt: 17`, `fragile_debt: 1`
* *Architecture:* `api: 45`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 105`, `doc: 33`, `test: 5`, `immutability_locks: 122`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.07
  * `Choke Point (Betweenness):` 0.006257 | `Ripple Effect (Closeness):` 0.065482
  * `Imports (Out-Degree: 5):` capy.zig, data.zig, widget.zig, AnimationController.zig, internal.zig, std, backend.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `src/backends/win32/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.055 IQR)
- **Top Global Matches:** file_cluster_8: 12.055, file_cluster_13: 12.291, file_cluster_11: 12.323
- **Magnitude:** 1594.26 | **LOC:** 1773 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 46
- **Risk Profile:** Cognitive Load (14.737%), Tech Debt (17.5497%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 1300.7 | O(2^N) | DB: 46)
  * `transWinError` (Impact: 3.6 | O(N^1) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 149`, `args: 101`, `func_start: 99`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 127`, `state_mutation: 117`, `dead_code: 3`, `planned_debt: 27`
* *Architecture:* `io: 10`, `api: 142`, `import: 11`
* *Defense:* `safety: 74`, `doc: 15`, `immutability_locks: 214`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` gdip.zig, shared.zig, builtin, Dropdown.zig, capy.zig, trait.zig, win32.zig, std...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/internal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.232 IQR)
- **Top Global Matches:** file_cluster_11: 15.232, file_cluster_13: 15.356, file_cluster_0: 15.424
- **Magnitude:** 1558.96 | **LOC:** 799 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (42.2434%), Tech Debt (12.317%)
**Top Internal Functions/Classes:**
  * `Widgeting` (Impact: 638.6 | O(N^6) | DB: 6)
    * *Intent:* /// Convenience function for creating widgets
  * `Events` (Impact: 417.8 | O(N^6) | DB: 8)
    * *Intent:* /// Convenience function for creating widgets
  * `iterateFields` (Impact: 131.5 | O(2^N) | DB: 2)
  * `iterateApplyFields` (Impact: 91.0 | O(2^N))
  * `convertTupleToWidgets` (Impact: 35.5 | O(N^4) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 68`, `args: 86`, `func_start: 69`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 37`, `dead_code: 17`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 80`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 98`, `doc: 52`, `immutability_locks: 148`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.595
  * `Choke Point (Betweenness):` 0.004937 | `Ripple Effect (Closeness):` 0.100951
  * `Imports (Out-Degree: 5):` root, builtin, trait.zig, containers.zig, shared.zig, data.zig, widget.zig, AnimationController.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `android/Sdk.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.257 IQR)
- **Top Global Matches:** file_cluster_8: 11.257, file_cluster_7: 11.547, file_cluster_13: 11.743
- **Magnitude:** 1411.3 | **LOC:** 1550 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 22
- **Risk Profile:** Cognitive Load (10.518%), Tech Debt (34.3946%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 360.8 | O(N^5) | DB: 21)
  * `createApp` (Impact: 338.4 | O(N^4) | DB: 20)
    * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
  * `validate` (Impact: 157.6 | O(N^6) | DB: 2)
  * `init` (Impact: 128.3 | O(N^4) | DB: 22)
    * *Intent:* /// Initializes the android SDK. /// It requires some input on which versions of the tool chains sho...
  * `make` (Impact: 44.9 | O(N^4) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 96`, `args: 38`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 37`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 28`, `api: 60`, `import: 4`
* *Defense:* `safety: 105`, `doc: 55`, `immutability_locks: 269`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006711
  * `Imports (Out-Degree: 0):` auto-detect.zig, std, builtin
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/android/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.114 IQR)
- **Top Global Matches:** file_cluster_11: 13.114, file_cluster_6: 13.118, file_cluster_0: 13.181
- **Magnitude:** 1336.82 | **LOC:** 873 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 10
- **Risk Profile:** Cognitive Load (31.5306%), Tech Debt (71.3761%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 427.7 | O(2^N) | DB: 10)
  * `Events` (Impact: 167.1 | O(N^5) | DB: 1)
  * `setText` (Impact: 148.3 | O(2^N) | DB: 2)
  * `getEventUserData` (Impact: 138.6 | O(2^N))
  * `ellipse` (Impact: 106.5 | O(N^6) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 121`, `args: 75`, `func_start: 75`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 91`, `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 6`, `planned_debt: 21`, `duplicate_logic: 2`
* *Architecture:* `io: 3`, `api: 88`, `concurrency: 17`, `import: 6`
* *Defense:* `safety: 109`, `doc: 2`, `sync_locks: 3`, `immutability_locks: 179`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shared.zig, capy.zig, trait.zig, android, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/examples/egl/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.612 IQR)
- **Top Global Matches:** file_cluster_8: 11.612, file_cluster_7: 11.934, file_cluster_13: 11.971
- **Magnitude:** 894.02 | **LOC:** 905 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 26
- **Risk Profile:** Cognitive Load (23.008%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mainLoop` (Impact: 393.2 | O(2^N) | DB: 26)
  * `insertPoint` (Impact: 68.1 | O(N^6) | DB: 4)
  * `debugMessageCallback` (Impact: 55.5 | O(N^3))
  * `processMotionEvent` (Impact: 41.3 | O(N^5) | DB: 3)
  * `processKeyEvent` (Impact: 23.7 | O(N^4) | DB: 5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 66`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 2`, `state_mutation: 108`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 27`, `doc: 11`, `sync_locks: 15`, `immutability_locks: 54`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` android, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/src/opensl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.222 IQR)
- **Top Global Matches:** file_cluster_8: 12.222, file_cluster_13: 12.511, file_cluster_0: 12.622
- **Magnitude:** 712.96 | **LOC:** 497 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (68.5693%), Tech Debt (73.3074%)
**Top Internal Functions/Classes:**
  * `fromIid` (Impact: 376.9 | O(N^3))
  * `getOutputStream` (Impact: 82.7 | O(N^5) | DB: 5)
  * `start` (Impact: 38.4 | O(N^5) | DB: 1)
  * `init` (Impact: 23.4 | O(N^3))
  * `checkResult` (Impact: 21.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 86`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 66`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 39`, `sync_locks: 6`, `immutability_locks: 13`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` c.zig, std, audio.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/examples/invocationhandler/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.436 IQR)
- **Top Global Matches:** file_cluster_8: 12.436, file_cluster_4: 12.452, file_cluster_13: 12.603
- **Magnitude:** 655.56 | **LOC:** 242 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (47.4986%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `timerInvoke` (Impact: 614.7 | O(2^N) | DB: 15)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 18`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 14`, `fragile_debt: 1`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 15`, `import: 2`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 44`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` android, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/capy-worker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.669 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.701 IQR)
- **Top Global Matches:** file_cluster_4: 11.669, file_cluster_8: 11.876, file_cluster_15: 11.954
- **Magnitude:** 480.66 | **LOC:** 451 | **CtrlFlow:** 27.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (68.7698%), Tech Debt (94.2617%)
**Top Internal Functions/Classes:**
  * `clock_time_get` (Impact: 29.1 | O(2^N) | DB: 2)
  * `fd_write` (Impact: 27.9 | O(2^N) | DB: 4)
  * `waitForAnswer` (Impact: 22.2 | O(2^N))
    * *Intent:* /**
  * `path_open` (Impact: 12.9 | O(2^N) | DB: 1)
  * `environ_get` (Impact: 11.4 | O(2^N) | DB: 6)
    * *Intent:* /** **/
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 75`, `args: 68`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 74`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 56`, `import: 1`
* *Defense:* `safety: 2`, `doc: 11`, `test: 1`, `sync_locks: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/src/android-support.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.75 IQR)
- **Top Global Matches:** file_cluster_13: 13.75, file_cluster_0: 13.927, file_cluster_11: 13.934
- **Magnitude:** 476.16 | **LOC:** 384 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (37.5668%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeNativeActivityGlue` (Impact: 124.2 | O(N^6) | DB: 2)
    * *Intent:* /// Returns a wrapper implementation for the given App type which implements all /// ANativeActivity...
  * `printSymbolInfoAt` (Impact: 79.2 | O(N^6) | DB: 4)
  * `panic` (Impact: 62.2 | O(N^3) | DB: 6)
    * *Intent:* // Android Panic implementation
  * `ANativeActivity_onCreate` (Impact: 51.2 | O(N^3) | DB: 6)
    * *Intent:* /// Actual application entry point
  * `write` (Impact: 37.2 | O(N^6))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 27`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 49`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 17`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 39`, `doc: 3`, `immutability_locks: 34`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.478
  * `Choke Point (Betweenness):` 0.000862 | `Ripple Effect (Closeness):` 0.026846
  * `Imports (Out-Degree: 6):` root, builtin, build_options, NativeInvocationHandler.zig, c.zig, NativeActivity.zig, android-bind.zig, audio.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `build_capy.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_6` (Drift: 13.694 IQR)
- **Top Global Matches:** file_cluster_6: 13.694, file_cluster_11: 13.816, file_cluster_13: 13.891
- **Magnitude:** 468.02 | **LOC:** 301 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 15
- **Risk Profile:** Cognitive Load (27.2073%), Tech Debt (78.6909%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 220.8 | O(N^6) | DB: 15)
  * `runStep` (Impact: 145.4 | O(N^6) | DB: 1)
    * *Intent:* /// Takes the given CompileStep and options and returns a run step. /// The run step from this funct...
  * `create` (Impact: 30.7 | O(2^N) | DB: 1)
  * `make` (Impact: 21.8 | O(N^3) | DB: 6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 64`, `structural_boundaries: 20`, `args: 4`, `func_start: 4`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 33`, `dead_code: 7`, `planned_debt: 9`, `orphaned_logic: 1`
* *Architecture:* `io: 4`, `api: 5`, `concurrency: 6`, `import: 4`
* *Defense:* `safety: 22`, `doc: 8`, `immutability_locks: 43`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, builtin, Sdk.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/osm-viewer.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.923 IQR)
- **Top Global Matches:** file_cluster_2: 12.923, file_cluster_17: 13.025, file_cluster_13: 13.132
- **Magnitude:** 458.44 | **LOC:** 296 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 3
- **Risk Profile:** Cognitive Load (26.6722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkRequests` (Impact: 147.9 | O(N^6) | DB: 3)
  * `getTile` (Impact: 44.3 | O(N^4) | DB: 1)
    * *Intent:* // Implementation Methods
  * `init` (Impact: 42.4 | O(2^N) | DB: 1)
  * `show` (Impact: 28.3 | O(N^3))
    * *Intent:* // All components have this method, which is automatically called // when Capy needs to create the n...
  * `mouseScroll` (Impact: 24.9 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 71`, `structural_boundaries: 36`, `args: 18`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 28`, `dead_code: 1`, `planned_debt: 1`, `fragile_debt: 1`, `orphaned_logic: 3`
* *Architecture:* `api: 14`, `import: 2`
* *Defense:* `safety: 41`, `doc: 2`, `immutability_locks: 45`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/src/NativeActivity.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.432 IQR)
- **Top Global Matches:** file_cluster_13: 13.432, file_cluster_8: 13.475, file_cluster_0: 13.503
- **Magnitude:** 440.64 | **LOC:** 209 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (35.0432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AndroidDisplayKeyboard` (Impact: 317.2 | O(2^N) | DB: 2)
  * `AndroidMakeFullscreen` (Impact: 54.2 | O(N^2))
  * `get` (Impact: 13.4 | O(N^2) | DB: 1)
    * *Intent:* /// Get the JNIEnv associated with the current thread.
  * `AndroidGetUnicodeChar` (Impact: 10.6 | O(N^1))
  * `fromJniEnv` (Impact: 8.3 | O(N^2) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 20`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 47`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01534
  * `Imports (Out-Degree: 1):` android-support.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/gtk/common.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.167 IQR)
- **Top Global Matches:** file_cluster_8: 12.167, file_cluster_13: 12.209, file_cluster_7: 12.482
- **Magnitude:** 420.86 | **LOC:** 320 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 8
- **Risk Profile:** Cognitive Load (23.8785%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 324.4 | O(N^5) | DB: 8)
  * `widgetSizeChanged` (Impact: 9.4 | O(N^2))
    * *Intent:* /// Since GTK4 removed the ::size-allocate signal which was used to listen to widget resizes, /// ba...
  * `getEventUserData` (Impact: 7.4 | O(N^3))
  * `getWidthFromPeer` (Impact: 7.2 | O(N^1))
  * `getHeightFromPeer` (Impact: 7.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 36`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 22`
* *Architecture:* `api: 27`, `import: 6`
* *Defense:* `safety: 21`, `doc: 4`, `immutability_locks: 54`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shared.zig, capy.zig, gtk.zig, trait.zig, std, backend.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/trait.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.793 IQR)
- **Top Global Matches:** file_cluster_8: 10.793, file_cluster_16: 10.813, file_cluster_11: 11.069
- **Magnitude:** 405.88 | **LOC:** 109 | **CtrlFlow:** 68.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (85.9182%), Tech Debt (34.5631%)
**Top Internal Functions/Classes:**
  * `hasUniqueRepresentation` (Impact: 193.7 | O(2^N) | DB: 1)
  * `isZigString` (Impact: 85.3 | O(N^5))
  * `isPtrTo` (Impact: 25.4 | O(N^4))
  * `isNumber` (Impact: 16.3 | O(N^3))
  * `isContainer` (Impact: 16.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 48`, `structural_boundaries: 22`, `args: 11`, `func_start: 10`, `class_start: 2`
* *Risk/State:* `state_mutation: 3`, `planned_debt: 1`
* *Architecture:* `api: 16`, `import: 1`
* *Defense:* `safety: 6`, `immutability_locks: 10`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 34.516
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.073993
  * `Imports (Out-Degree: 0):` std
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/fuzz.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.912 IQR)
- **Top Global Matches:** file_cluster_13: 14.912, file_cluster_11: 14.941, file_cluster_0: 14.97
- **Magnitude:** 385.28 | **LOC:** 218 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 12
- **Risk Profile:** Cognitive Load (42.3809%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testFunction` (Impact: 223.4 | O(N^6) | DB: 12)
  * `Iterator` (Impact: 56.8 | O(N^4) | DB: 1)
  * `threwError` (Impact: 35.5 | O(N^3))
  * `callback` (Impact: 10.6 | O(N^3))
  * `forAll` (Impact: 4.2 | O(N^1))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 13`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 38`, `dead_code: 5`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 22`, `doc: 4`, `test: 7`, `immutability_locks: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.913
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.039479
  * `Imports (Out-Degree: 1):` std, trait.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/macos/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.668 IQR)
- **Top Global Matches:** file_cluster_8: 10.668, file_cluster_13: 10.785, file_cluster_4: 11.013
- **Magnitude:** 346.92 | **LOC:** 381 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 1
- **Risk Profile:** Cognitive Load (41.9521%), Tech Debt (99.6626%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 69.8 | O(N^5))
  * `runStep` (Impact: 22.6 | O(N^3))
  * `getFlippedNSView` (Impact: 17.1 | O(N^3))
  * `create` (Impact: 16.4 | O(2^N))
  * `create` (Impact: 16.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 34`, `args: 37`, `func_start: 37`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 16`, `planned_debt: 7`, `duplicate_logic: 5`
* *Architecture:* `api: 62`, `concurrency: 18`, `import: 9`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 67`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` shared.zig, AppKit.zig, Button.zig, CapyAppDelegate.zig, capy.zig, trait.zig, std, Monitor.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/win32/win32.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.044 IQR)
- **Top Global Matches:** file_cluster_8: 10.044, file_cluster_7: 10.406, file_cluster_13: 10.537
- **Magnitude:** 344.04 | **LOC:** 423 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (8.6856%), Tech Debt (13.1596%)
**Top Internal Functions/Classes:**
  * `setWindowLongPtr` (Impact: 15.3 | O(N^2))
  * `getWindowLongPtr` (Impact: 13.3 | O(N^2))
  * `TabCtrl_InsertItemA` (Impact: 9.3 | O(N^2))
  * `TabCtrl_InsertItemW` (Impact: 9.3 | O(N^2))
  * `TabCtrl_GetCurSelA` (Impact: 8.1 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 12`, `args: 64`, `func_start: 59`, `class_start: 13`
* *Risk/State:* `safety_bypasses: 26`, `high_risk_execution: 8`, `dead_code: 1`, `planned_debt: 2`
* *Architecture:* `io: 25`, `api: 236`, `import: 5`
* *Defense:* `safety: 2`, `doc: 5`, `immutability_locks: 194`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 16.702
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.026846
  * `Imports (Out-Degree: 0):` std, zigwin32
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `android/src/jni.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.1%)
- **Global Archetype:** `file_cluster_16` (Drift: 12.943 IQR)
- **Top Global Matches:** file_cluster_16: 12.943, file_cluster_13: 13.04, file_cluster_11: 13.093
- **Magnitude:** 334.12 | **LOC:** 190 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^5) | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (60.9568%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `getClassNameString` (Impact: 236.4 | O(N^4) | DB: 2)
  * `invokeJni` (Impact: 42.6 | O(N^5))
  * `invokeJniNoException` (Impact: 8.4 | O(N^3))
  * `JniReturnType` (Impact: 6.2 | O(N^2))
    * *Intent:* // Underlying implementation
  * `findClass` (Impact: 5.3 | O(N^2))
    * *Intent:* // Convenience functions
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 25`, `args: 24`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `dead_code: 1`
* *Architecture:* `api: 26`, `import: 2`
* *Defense:* `safety: 32`, `doc: 6`, `immutability_locks: 61`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01534
  * `Imports (Out-Degree: 1):` android-support.zig, std
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/gles/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.729 IQR)
- **Top Global Matches:** file_cluster_8: 10.729, file_cluster_13: 10.804, file_cluster_11: 11.037
- **Magnitude:** 310.1 | **LOC:** 318 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (14.2277%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 50.8 | O(N^5))
  * `create` (Impact: 38.4 | O(2^N) | DB: 2)
  * `runStep` (Impact: 35.5 | O(N^4))
  * `compile` (Impact: 28.5 | O(2^N) | DB: 2)
  * `create` (Impact: 14.3 | O(N^3))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 33`, `args: 29`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 7`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 9`
* *Architecture:* `api: 49`, `import: 6`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 41`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` shared.zig, capy.zig, glfw3.h, trait.zig, std
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `examples/balls.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 11.795 IQR)
- **Top Global Matches:** file_cluster_2: 11.795, file_cluster_17: 11.867, file_cluster_8: 11.912
- **Magnitude:** 295.4 | **LOC:** 233 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 6
- **Risk Profile:** Cognitive Load (36.3547%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `simulationThread` (Impact: 138.2 | O(N^6) | DB: 1)
  * `onMouseButton` (Impact: 59.8 | O(N^5))
  * `onDraw` (Impact: 25.5 | O(N^3))
  * `main` (Impact: 22.6 | O(N^3) | DB: 6)
  * `onMouseMotion` (Impact: 9.3 | O(N^2))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 45`, `structural_boundaries: 21`, `args: 6`, `func_start: 5`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 27`, `dead_code: 1`, `orphaned_logic: 1`
* *Architecture:* `api: 3`, `concurrency: 6`, `import: 2`
* *Defense:* `safety: 15`, `immutability_locks: 33`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/capy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.479 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.648 IQR)
- **Top Global Matches:** file_cluster_4: 13.479, file_cluster_8: 13.493, file_cluster_11: 13.731
- **Magnitude:** 285.36 | **LOC:** 635 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 18
- **Risk Profile:** Cognitive Load (63.2771%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `addChunk` (Impact: 83.4 | O(N^3) | DB: 18)
  * `pushAnswer` (Impact: 31.6 | O(N^1))
  * `log` (Impact: 11.6 | O(2^N) | DB: 1)
  * `createChunk` (Impact: 8.1 | O(N^4) | DB: 13)
  * `constructor` (Impact: 5.0 | O(N^1) | DB: 8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 25`, `args: 13`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 127`
* *Architecture:* `api: 3`, `concurrency: 8`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.006711
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/http.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.01%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.167 IQR)
- **Top Global Matches:** file_cluster_13: 12.167, file_cluster_6: 12.285, file_cluster_11: 12.299
- **Magnitude:** 280.62 | **LOC:** 128 | **CtrlFlow:** 64.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 2
- **Risk Profile:** Cognitive Load (21.9726%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `send` (Impact: 70.2 | O(2^N) | DB: 2)
  * `isReady` (Impact: 52.6 | O(N^4))
  * `read` (Impact: 21.0 | O(2^N))
  * `checkError` (Impact: 14.2 | O(N^3))
  * `send` (Impact: 14.0 | O(2^N))
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 33`, `structural_boundaries: 18`, `args: 14`, `func_start: 14`, `class_start: 5`
* *Risk/State:* `state_mutation: 6`, `dead_code: 1`, `planned_debt: 3`, `duplicate_logic: 14`
* *Architecture:* `io: 2`, `api: 24`, `import: 3`
* *Defense:* `safety: 11`, `doc: 4`, `immutability_locks: 21`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 6.55
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.039718
  * `Imports (Out-Degree: 1):` internal.zig, std, backend.zig
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/backends/android/backend.zig` (ZIG) | Magnitude: 1336.82 | Delta: **0.004 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 682, immutability_locks: 179, encapsulation: 159, globals: 156
- `src/containers.zig` (ZIG) | Magnitude: 1686.16 | Delta: **0.019 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 748, branch: 249, encapsulation: 135, globals: 133
- `src/data.zig` (ZIG) | Magnitude: 3261.82 | Delta: **0.03 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1091, branch: 295, encapsulation: 181, globals: 178
- `src/internal.zig` (ZIG) | Magnitude: 1558.96 | Delta: **0.124 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 633, branch: 218, immutability_locks: 148, pointers: 119

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/backends/gtk/Dropdown.zig` (ZIG) | Magnitude: 55.7 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, immutability_locks: 20, encapsulation: 13, globals: 12
- `android/examples/minimal/main.zig` (ZIG) | Magnitude: 20.5 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, doc: 11, immutability_locks: 6, api: 5
- `src/async.zig` (ZIG) | Magnitude: 90.72 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, branch: 14, globals: 13, state_mutation: 12
- `android/tools/zip_add.zig` (ZIG) | Magnitude: 0.09 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, branch: 31, structural_boundaries: 17, globals: 17
- `src/fuzz.zig` (ZIG) | Magnitude: 385.28 | Delta: **0.029 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 172, branch: 58, state_mutation: 38, bitwise_ops: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/dev_tools.zig` (ZIG) | Magnitude: 201.06 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, branch: 46, encapsulation: 33, globals: 29
- `android/src/jni.zig` (ZIG) | Magnitude: 334.12 | Delta: **0.097 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 151, branch: 61, immutability_locks: 61, globals: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/fade.zig` (ZIG) | Magnitude: 49.12 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, ui_framework: 18, branch: 10, encapsulation: 7
- `examples/transition.zig` (ZIG) | Magnitude: 16.86 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, ui_framework: 13, encapsulation: 6, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/totp.zig` (ZIG) | Magnitude: 15.5 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, ui_framework: 10, branch: 3, structural_boundaries: 3
- `examples/7gui/temperature-converter.zig` (ZIG) | Magnitude: 82.52 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, branch: 17, safety: 13, globals: 13
- `src/c_api.zig` (ZIG) | Magnitude: 67.74 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 16, api: 14, structural_boundaries: 12
- `src/testing.zig` (ZIG) | Magnitude: 17.78 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, branch: 4, api: 3, ui_framework: 3
- `examples/balls.zig` (ZIG) | Magnitude: 295.4 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 176, encapsulation: 47, branch: 45, globals: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/backends/wasm/capy.js` (JAVASCRIPT) | Magnitude: 285.36 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 127, indent_tabs: 118, branch: 46, indent_spaces: 31
- `src/backends/wasm/capy-worker.js` (JAVASCRIPT) | Magnitude: 480.66 | Delta: **0.207 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 324, structural_boundaries: 75, state_mutation: 74, func_start: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `build_capy.zig` (ZIG) | Magnitude: 468.02 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 248, branch: 64, immutability_locks: 43, globals: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `android/examples/textview/main.zig` (ZIG) | Magnitude: 154.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 120, encapsulation: 28, globals: 26, immutability_locks: 26
- `c_examples/c_template.c` (C) | Magnitude: 7.08 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 10, api: 3, state_mutation: 2, import: 2
- `src/backends/macos/Monitor.zig` (ZIG) | Magnitude: 24.02 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, api: 8, structural_boundaries: 4, args: 4
- `android/examples/invocationhandler/main.zig` (ZIG) | Magnitude: 655.56 | Delta: **0.016 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 176, branch: 53, encapsulation: 51, globals: 48
- `src/components/Slider.zig` (ZIG) | Magnitude: 115.66 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 74, encapsulation: 17, branch: 16, doc: 16

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `src/containers.zig` -> **Severity: 0.294** (Bridge: 0.0063 * Flux: 47.0085%)
- `src/data.zig` -> **Severity: 0.232** (Bridge: 0.0032 * Flux: 72.7812%)
- `android/src/android-support.zig` -> **Severity: 0.073** (Bridge: 0.0009 * Flux: 85.1175%)
- `src/AnimationController.zig` -> **Severity: 0.052** (Bridge: 0.0006 * Flux: 93.5398%)
- `src/backends/wasm/capy.js` -> **Severity: 0.005** (Bridge: 0.0 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `src/internal.zig` -> **Severity: 5.704** (Embedded: 0.101 * Error Risk: 56.5043%)
- `src/widget.zig` -> **Severity: 5.538** (Embedded: 0.0692 * Error Risk: 80.0%)
- `src/AnimationController.zig` -> **Severity: 4.422** (Embedded: 0.0757 * Error Risk: 58.4091%)
- `src/backends/win32/win32.zig` -> **Severity: 2.049** (Embedded: 0.0268 * Error Risk: 76.3215%)
- `src/backends/gtk/windowbin.zig` -> **Severity: 1.611** (Embedded: 0.0201 * Error Risk: 80.0%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/internal.zig` -> **Severity: 5627.607** (Blast Radius: 57.595 * Doc Risk: 97.71%)
- `src/data.zig` -> **Severity: 5426.5** (Blast Radius: 68.771 * Doc Risk: 78.9068%)
- `src/backends/wasm/js.zig` -> **Severity: 4919.5** (Blast Radius: 49.195 * Doc Risk: 100.0%)
- `src/AnimationController.zig` -> **Severity: 4390.831** (Blast Radius: 43.941 * Doc Risk: 99.9256%)
- `src/trait.zig` -> **Severity: 3451.6** (Blast Radius: 34.516 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
