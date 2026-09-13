# ARCHITECTURAL_BRIEF: capy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/capy-ui/capy.git` |
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
| Avg Path Length | 2.343 | Hops between files. Lower = Tighter coupling. |
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
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

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
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 45.0 | 53.9 | 100.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 100.0 | 5.8 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 25.8 | 11.8 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 40.1 | 3.8 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 94.5 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 57.6 | 0.4 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 81.5 | 100.0 | 100.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

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

- `Atom` (@ `src/data.zig`) -> Impact: **118.7** | LOC: 592
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `process` (@ `src/backends/win32/backend.zig`) -> Impact: **98.3** | LOC: 222
- `createApp` (@ `android/Sdk.zig`) -> Impact: **86.3** | LOC: 286
  * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
- `Events` (@ `src/backends/win32/backend.zig`) -> Impact: **82.1** | LOC: 312
- `GridLayout` (@ `src/containers.zig`) -> Impact: **81.2** | LOC: 238
  * *Intent:* /// Grid layout based on the CSS Grid algorithm
- `fromIid` (@ `android/src/opensl.zig`) -> Impact: **79.2** | LOC: 56
- `Widgeting` (@ `src/internal.zig`) -> Impact: **65.1** | LOC: 313
  * *Intent:* /// Convenience function for creating widgets
- `add` (@ `android/Sdk.zig`) -> Impact: **61.3** | LOC: 376
- `RowLayout` (@ `src/containers.zig`) -> Impact: **54.3** | LOC: 81
  * *Intent:* /// Arranges items horizontally.
- `ColumnLayout` (@ `src/containers.zig`) -> Impact: **53.9** | LOC: 74
  * *Intent:* /// Arranges items vertically.

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

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/backends/wasm/capy.js` (JAVASCRIPT) -> Cumulative Risk: **766.61**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 608.64 | **LOC:** 635 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.9959%), Documentation (97.8495%)
- **Heaviest Functions:** `pushAnswer` (Impact: 31.6), `addChunk` (Impact: 17.0), `fillImage` (Impact: 14.7)

### 2. `src/backends/wasm/capy-worker.js` (JAVASCRIPT) -> Cumulative Risk: **744.19**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 343.46 | **LOC:** 451 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Concurrency (100.0%), State Flux (100.0%), Spec Match (100.0%)
- **Heaviest Functions:** `clock_time_get` (Impact: 15.2), `fd_write` (Impact: 14.5), `waitForAnswer` (Impact: 9.9)

### 3. `src/backends/gtk/Canvas.zig` (ZIG) -> Cumulative Risk: **554.77**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 125.88 | **LOC:** 240 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (94.2857%), State Flux (88.3099%), Safety Score (83.6563%)
- **Heaviest Functions:** `roundedRectangleEx` (Impact: 16.1), `text` (Impact: 8.0), `gtkCanvasDraw` (Impact: 7.8)

### 4. `src/backends/wasm/Window.zig` (ZIG) -> Cumulative Risk: **542.11**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 34.96 | **LOC:** 65 | **CtrlFlow:** 6.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (96.0834%), Tech Debt (88.0797%)
- **Heaviest Functions:** `setChild` (Impact: 5.6), `show` (Impact: 3.2), `resize` (Impact: 2.1)

### 5. `src/backends/macos/backend.zig` (ZIG) -> Cumulative Risk: **537.18**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 170.02 | **LOC:** 381 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (100.0%), Verification (80.0%)
- **Heaviest Functions:** `Events` (Impact: 9.5), `runStep` (Impact: 8.9), `setChild` (Impact: 5.5)

### 6. `src/backends/android/backend.zig` (ZIG) -> Cumulative Risk: **535.25**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 358.24 | **LOC:** 873 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (98.5401%), Safety Score (80.0%)
- **Heaviest Functions:** `Events` (Impact: 13.6), `runOnUiThread` (Impact: 8.2), `onClick` (Impact: 7.3)

### 7. `src/backends/gtk/backend.zig` (ZIG) -> Cumulative Risk: **535.12**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 50.96 | **LOC:** 97 | **CtrlFlow:** 7.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (82.4063%)
- **Heaviest Functions:** `showNativeMessageDialog` (Impact: 9.3), `init` (Impact: 3.4), `runStep` (Impact: 1.7)

### 8. `src/backends/macos/CapyAppDelegate.zig` (ZIG) -> Cumulative Risk: **524.49**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 57.06 | **LOC:** 117 | **CtrlFlow:** 1.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (80.0%)
- **Heaviest Functions:** `get` (Impact: 8.2), `a` (Impact: 2.4), `a` (Impact: 2.4)

### 9. `src/components/Image.zig` (ZIG) -> Cumulative Risk: **513.45**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 53.86 | **LOC:** 148 | **CtrlFlow:** 7.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (78.8731%)
- **Heaviest Functions:** `draw` (Impact: 13.6), `getPreferredSize` (Impact: 5.5), `show` (Impact: 3.1)

### 10. `src/backends/win32/backend.zig` (ZIG) -> Cumulative Risk: **508.21**
- **Archetype:** `Unclassified` (Distance: N/A IQR)
- **Magnitude:** 718.28 | **LOC:** 1773 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Api Exposure (100.0%), Spec Match (100.0%), Documentation (97.1014%), Verification (80.0%)
- **Heaviest Functions:** `process` (Impact: 98.3), `Events` (Impact: 82.1), `setFullscreen` (Impact: 14.2)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `android/src/android-bind.zig` (ZIG | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 1978.5 | **LOC:** 2624 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AHardwareBuffer_lockAndGetInfo` (Impact: 2.9)
  * `ALooper_addFd` (Impact: 2.7)
  * `__android_log_buf_print` (Impact: 2.5)
  * `AInputQueue_attachLooper` (Impact: 2.5)
  * `AHardwareBuffer_lock` (Impact: 2.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 718.28 | **LOC:** 1773 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.2661%), Tech Debt (17.2621%)
**Top Internal Functions/Classes:**
  * `process` (Impact: 98.3)
  * `Events` (Impact: 82.1)
  * `setFullscreen` (Impact: 14.2)
  * `runStep` (Impact: 11.3)
  * `init` (Impact: 9.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 707.42 | **LOC:** 1349 | **CtrlFlow:** 9.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.3138%), Tech Debt (11.0488%)
**Top Internal Functions/Classes:**
  * `Atom` (Impact: 118.7)
    * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to //...
  * `lerp` (Impact: 31.9)
    * *Intent:* /// Linear interpolation between any two values a and b with factor t. /// Both values must be of th...
  * `ListAtom` (Impact: 26.8)
    * *Intent:* /// A list of atoms, that is itself an atom.
  * `dependOn` (Impact: 18.0)
    * *Intent:* // TODO: constrain "function"'s type based on tuple // TODO: optionally provide the function with an...
  * `animate` (Impact: 16.2)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 608.64 | **LOC:** 635 | **CtrlFlow:** 13.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (91.8827%), Tech Debt (10.9481%)
**Top Internal Functions/Classes:**
  * `pushAnswer` (Impact: 31.6)
  * `addChunk` (Impact: 17.0)
    * *Intent:* /** **/
  * `fillImage` (Impact: 14.7)
  * `update` (Impact: 13.5)
    * *Intent:* // TODO: when we're in blocking mode, avoid updating so often
  * `onmessage` (Impact: 12.3)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 491.76 | **LOC:** 799 | **CtrlFlow:** 15.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (30.047%), Tech Debt (11.4285%)
**Top Internal Functions/Classes:**
  * `Widgeting` (Impact: 65.1)
    * *Intent:* /// Convenience function for creating widgets
  * `Events` (Impact: 40.1)
    * *Intent:* /// Convenience function for creating widgets
  * `iterateFields` (Impact: 24.1)
  * `iterateApplyFields` (Impact: 16.9)
  * `errorHandler` (Impact: 9.6)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 473.5 | **LOC:** 924 | **CtrlFlow:** 19.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.8416%), Tech Debt (25.6082%)
**Top Internal Functions/Classes:**
  * `GridLayout` (Impact: 81.2)
    * *Intent:* /// Grid layout based on the CSS Grid algorithm
  * `RowLayout` (Impact: 54.3)
    * *Intent:* /// Arranges items horizontally.
  * `ColumnLayout` (Impact: 53.9)
    * *Intent:* /// Arranges items vertically.
  * `getChild` (Impact: 16.7)
    * *Intent:* /// Searches recursively for a component named `name` and returns the first one found. /// If no com...
  * `MarginLayout` (Impact: 10.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 416.88 | **LOC:** 1550 | **CtrlFlow:** 5.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9604%), Tech Debt (8.0124%)
**Top Internal Functions/Classes:**
  * `createApp` (Impact: 86.3)
    * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
  * `add` (Impact: 61.3)
  * `validate` (Impact: 27.6)
  * `init` (Impact: 19.4)
    * *Intent:* /// Initializes the android SDK. /// It requires some input on which versions of the tool chains sho...
  * `configureModule` (Impact: 8.8)
    * *Intent:* // Note that this function must be accompanied by `configureStep`
**Contextual Mitigations & Amplifications:**
* *Mitigated Danger:* 11 instances
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Rce:* 2 instances
* *Amplified Cascading Flux:* 5 instances
* *High Risk Execution (weighted view):* 0
* *Memory Alloc (weighted view):* 3
* *Sec Tainted Injection (weighted view):* 2
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 368.08 | **LOC:** 423 | **CtrlFlow:** 3.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.8936%), Tech Debt (10.5097%)
**Top Internal Functions/Classes:**
  * `setWindowLongPtr` (Impact: 6.3)
  * `getWindowLongPtr` (Impact: 5.5)
  * `TabCtrl_InsertItemA` (Impact: 4.3)
  * `TabCtrl_InsertItemW` (Impact: 4.3)
  * `TabCtrl_GetItemA` (Impact: 4.2)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 358.24 | **LOC:** 873 | **CtrlFlow:** 2.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.0788%), Tech Debt (28.4194%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 13.6)
  * `runOnUiThread` (Impact: 8.2)
  * `onClick` (Impact: 7.3)
  * `onChangedText` (Impact: 7.3)
  * `onDraw` (Impact: 6.7)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Local Micro-Species:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 343.46 | **LOC:** 451 | **CtrlFlow:** 7.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (81.61%), Tech Debt (100.0%)
**Top Internal Functions/Classes:**
  * `clock_time_get` (Impact: 15.2)
  * `fd_write` (Impact: 14.5)
  * `waitForAnswer` (Impact: 9.9)
    * *Intent:* /** **/
  * `path_open` (Impact: 6.6)
  * `environ_get` (Impact: 6.2)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 314.18 | **LOC:** 905 | **CtrlFlow:** 8.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.2988%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mainLoop` (Impact: 41.3)
  * `debugMessageCallback` (Impact: 21.2)
  * `insertPoint` (Impact: 17.0)
  * `processMotionEvent` (Impact: 11.9)
  * `renderf32` (Impact: 9.2)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 215.74 | **LOC:** 320 | **CtrlFlow:** 13.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (17.9822%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 53.4)
  * `gtkKeyPress` (Impact: 26.4)
  * `gtkButtonPress` (Impact: 22.3)
  * `gtkMouseMotion` (Impact: 9.7)
  * `gtkMouseScroll` (Impact: 7.3)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 189.68 | **LOC:** 384 | **CtrlFlow:** 9.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.3775%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeNativeActivityGlue` (Impact: 20.8)
    * *Intent:* /// Returns a wrapper implementation for the given App type which implements all /// ANativeActivity...
  * `printSymbolInfoAt` (Impact: 13.6)
  * `ANativeActivity_onCreate` (Impact: 13.2)
    * *Intent:* /// Actual application entry point
  * `invoke` (Impact: 12.8)
  * `panic` (Impact: 10.2)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 176.36 | **LOC:** 497 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (21.3596%), Tech Debt (44.962%)
**Top Internal Functions/Classes:**
  * `fromIid` (Impact: 79.2)
  * `getOutputStream` (Impact: 15.1)
  * `checkResult` (Impact: 5.4)
  * `bufferQueueCallback` (Impact: 5.0)
  * `start` (Impact: 4.8)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 170.02 | **LOC:** 381 | **CtrlFlow:** 4.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1886%), Tech Debt (21.8486%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 9.5)
  * `runStep` (Impact: 8.9)
  * `setChild` (Impact: 5.5)
  * `setCallback` (Impact: 4.8)
  * `getFlippedNSView` (Impact: 4.1)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 160.64 | **LOC:** 107 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (16.2747%)
**Top Internal Functions/Classes:**
  * `jsSetAttribute` (Impact: 2.5)
  * `jsSetStyle` (Impact: 2.5)
  * `setColor` (Impact: 2.5)
  * `rectPath` (Impact: 2.5)
  * `fillText` (Impact: 2.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 145.94 | **LOC:** 233 | **CtrlFlow:** 17.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.9074%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `simulationThread` (Impact: 33.1)
  * `onMouseButton` (Impact: 15.7)
  * `onDraw` (Impact: 13.4)
  * `main` (Impact: 4.7)
  * `onMouseMotion` (Impact: 4.3)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 130.32 | **LOC:** 218 | **CtrlFlow:** 13.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (11.037%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `testFunction` (Impact: 36.5)
  * `refine` (Impact: 18.0)
    * *Intent:* /// Tries to find counter-examples (case where there is no error) in the /// given time and adjust t...
  * `Iterator` (Impact: 8.9)
  * `threwError` (Impact: 7.8)
  * `format` (Impact: 5.0)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 127.18 | **LOC:** 296 | **CtrlFlow:** 10.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (19.3176%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkRequests` (Impact: 16.5)
  * `mouseScroll` (Impact: 10.8)
  * `getTile` (Impact: 7.9)
    * *Intent:* // Implementation Methods
  * `drawTile` (Impact: 7.9)
  * `draw` (Impact: 5.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 125.88 | **LOC:** 240 | **CtrlFlow:** 7.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (12.6062%), Tech Debt (16.5122%)
**Top Internal Functions/Classes:**
  * `roundedRectangleEx` (Impact: 16.1)
    * *Intent:* // The radiuses are in order: top left, top right, bottom left, bottom right
  * `text` (Impact: 8.0)
  * `gtkCanvasDraw` (Impact: 7.8)
  * `getTextSize` (Impact: 5.6)
  * `ellipse` (Impact: 5.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 124.62 | **LOC:** 301 | **CtrlFlow:** 14.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (23.1951%), Tech Debt (89.4457%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 41.8)
  * `runStep` (Impact: 19.9)
    * *Intent:* /// Takes the given CompileStep and options and returns a run step. /// The run step from this funct...
  * `make` (Impact: 4.5)
  * `create` (Impact: 2.7)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 123.84 | **LOC:** 318 | **CtrlFlow:** 4.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.2724%), Tech Debt (16.6986%)
**Top Internal Functions/Classes:**
  * `runStep` (Impact: 8.0)
  * `Events` (Impact: 7.0)
  * `setCallback` (Impact: 4.7)
  * `create` (Impact: 4.3)
  * `create` (Impact: 3.9)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 115.64 | **LOC:** 177 | **CtrlFlow:** 12.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.6374%), Tech Debt (20.6086%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 35.3)
  * `processEvent` (Impact: 33.0)
  * `setCallback` (Impact: 4.9)
  * `setUserData` (Impact: 4.0)
  * `requestDraw` (Impact: 3.1)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 111.72 | **LOC:** 206 | **CtrlFlow:** 10.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (8.4013%), Tech Debt (11.8856%)
**Top Internal Functions/Classes:**
  * `animateAtoms` (Impact: 12.9)
  * `runEventLoop` (Impact: 3.4)
  * `stepEventLoop` (Impact: 3.3)
    * *Intent:* /// Returns false if the last window has been closed. /// Even if the wanted step type is Blocking, ...
  * `init` (Impact: 2.9)
  * `deinit` (Impact: 2.5)
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
- **Global Archetype:** `Unclassified` (Drift: 0.0 IQR)
- **Magnitude:** 109.86 | **LOC:** 214 | **CtrlFlow:** 14.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.1138%), Tech Debt (18.8722%)
**Top Internal Functions/Classes:**
  * `gtkLayout` (Impact: 26.1)
  * `initMenu` (Impact: 9.6)
  * `setFullscreen` (Impact: 6.5)
  * `gtkCloseRequest` (Impact: 5.7)
  * `create` (Impact: 5.0)
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

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
