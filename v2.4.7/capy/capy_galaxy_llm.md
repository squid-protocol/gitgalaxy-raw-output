# ARCHITECTURAL_BRIEF: capy
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_zig/capy` |
| **Timestamp** | `2026-08-07T04:29:13.271695+00:00` |
| **Scan Duration** | `0.69s` |
| **Git Branch** | `master` |
| **Git Commit** | `fd77077e296a969ae258c595e75a0723183b3138` |
| **Git Remote** | `https://github.com/capy-ui/capy.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 143 malicious artifacts.

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
| Cognitive Load Exposure | 0.0 | 94.6 | 25.5 | 21.1 | 5.0 |
| Error & Exception Exposure | 0.0 | 96.0 | 56.9 | 66.8 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 34.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 22.8 | 2.6 | 80.0 |
| API Exposure | 0.0 | 18.4 | 4.9 | 4.5 | 0.0 |
| Concurrency Exposure | 0.0 | 100.0 | 7.9 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 15.7 | 0.0 | 0.0 |
| Commented Logic Exposure | 0.0 | 40.1 | 3.8 | 0.0 | 0.0 |
| Specification Exposure | 6.7 | 100.0 | 97.4 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.6 | 0.0 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 57.6 | 0.4 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 66.4 | 91.7 | 0.0 |
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

- `Atom` (@ `src/data.zig`) -> Impact: **277.6** | LOC: 592
  * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to /// a value. It is used for all component properties...
- `init` (@ `src/backends/win32/backend.zig`) -> Impact: **238.7** | LOC: 1234
- `Widgeting` (@ `src/internal.zig`) -> Impact: **193.7** | LOC: 313
  * *Intent:* /// Convenience function for creating widgets
- `fromIid` (@ `android/src/opensl.zig`) -> Impact: **189.9** | LOC: 56
- `createApp` (@ `android/Sdk.zig`) -> Impact: **144.0** | LOC: 286
  * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
- `add` (@ `android/Sdk.zig`) -> Impact: **132.7** | LOC: 373
- `timerInvoke` (@ `android/examples/invocationhandler/main.zig`) -> Impact: **131.7** | LOC: 220
- `Events` (@ `src/internal.zig`) -> Impact: **127.8** | LOC: 236
  * *Intent:* /// Convenience function for creating widgets
- `GridLayout` (@ `src/containers.zig`) -> Impact: **117.6** | LOC: 238
  * *Intent:* /// Grid layout based on the CSS Grid algorithm
- `Events` (@ `src/backends/gtk/common.zig`) -> Impact: **116.4** | LOC: 248

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src` | 25 | 4743.8 | 28.12% | 61.23% |
| `android/src` | 13 | 3250.92 | 28.08% | 35.94% |
| `src/backends/wasm` | 16 | 1504.14 | 23.56% | 43.92% |
| `src/backends/gtk` | 19 | 1285.68 | 20.43% | 29.51% |
| `examples` | 23 | 1113.68 | 36.29% | 0.0% |
| `src/backends/win32` | 6 | 1094.3 | 17.25% | 23.96% |
| `src/components` | 15 | 1029.82 | 22.28% | 36.79% |
| `src/backends/android` | 1 | 708.62 | 20.03% | 98.88% |
| `android` | 5 | 704.74 | 5.29% | 6.88% |
| `src/backends/macos` | 4 | 425.64 | 29.2% | 60.48% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `src/async.zig` -> **100.0%** Exposure
- `src/audio.zig` -> **100.0%** Exposure
- `src/backends/macos/CapyAppDelegate.zig` -> **100.0%** Exposure
- `src/c_api.zig` -> **100.0%** Exposure
- `src/components/Canvas.zig` -> **100.0%** Exposure
### Highest State Flux (Mutation/Volatility)
- `src/backends/wasm/capy-worker.js` -> **100.0%** Exposure
- `src/backends/wasm/capy.js` -> **100.0%** Exposure
- `src/backends/win32/Monitor.zig` -> **97.6199%** Exposure
- `src/listener.zig` -> **97.5873%** Exposure
- `src/fuzz.zig` -> **97.377%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `src/data.zig` -> **0** Orphaned Functions | **28** Duplicates
- `src/backends/macos/CapyAppDelegate.zig` -> **0** Orphaned Functions | **20** Duplicates
- `src/http.zig` -> **0** Orphaned Functions | **14** Duplicates
- `src/c_api.zig` -> **12** Orphaned Functions | **0** Duplicates
- `src/components/Canvas.zig` -> **0** Orphaned Functions | **10** Duplicates

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

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `2` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `412` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `src/backends/wasm/capy.js` (JAVASCRIPT) -> Cumulative Risk: **652.78**
- **Archetype:** `file_cluster_4` (Distance: 13.387 IQR)
- **Magnitude:** 368.06 | **LOC:** 635 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (97.2598%), Concurrency (96.8094%)
- **Heaviest Functions:** `setTimeout` (Impact: 75.9), `addChunk` (Impact: 43.8), `update` (Impact: 35.4)

### 2. `src/backends/wasm/capy-worker.js` (JAVASCRIPT) -> Cumulative Risk: **647.87**
- **Archetype:** `file_cluster_4` (Distance: 11.665 IQR)
- **Magnitude:** 332.86 | **LOC:** 451 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Concurrency (99.987%), Tech Debt (94.2617%)
- **Heaviest Functions:** `clock_time_get` (Impact: 15.2), `fd_write` (Impact: 14.5), `waitForAnswer` (Impact: 11.8)

### 3. `src/fuzz.zig` (ZIG) -> Cumulative Risk: **602.55**
- **Archetype:** `file_cluster_13` (Distance: 14.885 IQR)
- **Magnitude:** 221.28 | **LOC:** 218 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (97.377%), Tech Debt (96.9302%), Documentation (84.6441%)
- **Heaviest Functions:** `testFunction` (Impact: 50.3), `Iterator` (Impact: 23.8), `threwError` (Impact: 18.2)

### 4. `src/async.zig` (ZIG) -> Cumulative Risk: **599.37**
- **Archetype:** `file_cluster_13` (Distance: 11.638 IQR)
- **Magnitude:** 52.72 | **LOC:** 78 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Tech Debt (100.0%), Spec Match (100.0%), Concurrency (98.3925%), State Flux (92.0228%)
- **Heaviest Functions:** `getFreeThread` (Impact: 11.1), `taskRunner` (Impact: 4.3), `init` (Impact: 3.7)

### 5. `src/backends/macos/backend.zig` (ZIG) -> Cumulative Risk: **577.74**
- **Archetype:** `file_cluster_8` (Distance: 10.698 IQR)
- **Magnitude:** 267.62 | **LOC:** 381 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.8809%), Tech Debt (99.6626%), Concurrency (93.2319%)
- **Heaviest Functions:** `Events` (Impact: 25.8), `runStep` (Impact: 12.2), `getFlippedNSView` (Impact: 9.1)

### 6. `src/listener.zig` (ZIG) -> Cumulative Risk: **568.28**
- **Archetype:** `file_cluster_13` (Distance: 12.792 IQR)
- **Magnitude:** 97.3 | **LOC:** 121 | **CtrlFlow:** 56.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (99.1563%), Tech Debt (97.7023%), State Flux (97.5873%)
- **Heaviest Functions:** `hasEnabledListeners` (Impact: 7.6), `remove` (Impact: 7.4), `listen` (Impact: 7.2)

### 7. `src/components/Navigation.zig` (ZIG) -> Cumulative Risk: **566.44**
- **Archetype:** `file_cluster_13` (Distance: 12.791 IQR)
- **Magnitude:** 117.24 | **LOC:** 134 | **CtrlFlow:** 68.2% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (97.5441%), Verification (80.0%), State Flux (74.8806%)
- **Heaviest Functions:** `navigation` (Impact: 16.6), `getChild` (Impact: 10.8), `navigateTo` (Impact: 10.5)

### 8. `src/assets.zig` (ZIG) -> Cumulative Risk: **557.87**
- **Archetype:** `file_cluster_13` (Distance: 12.384 IQR)
- **Magnitude:** 94.12 | **LOC:** 98 | **CtrlFlow:** 69.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Concurrency (94.9228%), Documentation (91.4997%), Tech Debt (81.9409%)
- **Heaviest Functions:** `get` (Impact: 46.4), `read` (Impact: 10.9), `deinit` (Impact: 4.0)

### 9. `src/components/Tabs.zig` (ZIG) -> Cumulative Risk: **544.52**
- **Archetype:** `file_cluster_13` (Distance: 12.921 IQR)
- **Magnitude:** 95.98 | **LOC:** 111 | **CtrlFlow:** 75.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (98.3499%), State Flux (90.2109%), Verification (80.0%)
- **Heaviest Functions:** `tabs` (Impact: 16.6), `show` (Impact: 11.0), `add` (Impact: 9.4)

### 10. `android/src/aaudio.zig` (ZIG) -> Cumulative Risk: **541.12**
- **Archetype:** `file_cluster_13` (Distance: 12.286 IQR)
- **Magnitude:** 95.82 | **LOC:** 176 | **CtrlFlow:** 66.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (96.128%), Safety Score (80.0%), Verification (80.0%)
- **Heaviest Functions:** `getOutputStream` (Impact: 30.6), `errorCallback` (Impact: 9.5), `dataCallback` (Impact: 8.6)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `android/src/android-bind.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.48 IQR)
- **Top Global Matches:** file_cluster_8: 10.48, file_cluster_7: 11.011, file_cluster_1: 11.359
- **Magnitude:** 1724.1 | **LOC:** 2624 | **CtrlFlow:** 50.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (4.9733%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `__BIONIC_CAST` (Impact: 4.2)
  * `__BIONIC_ALIGN` (Impact: 3.6)
  * `__P` (Impact: 3.6)
  * `__android_log_assert` (Impact: 3.4)
  * `AHardwareBuffer_lockAndGetInfo` (Impact: 3.3)
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

### `src/data.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.05%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.447 IQR)
- **Top Global Matches:** file_cluster_11: 13.447, file_cluster_13: 13.474, file_cluster_8: 13.518
- **Magnitude:** 1234.82 | **LOC:** 1349 | **CtrlFlow:** 63.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (40.4904%), Tech Debt (99.927%)
**Top Internal Functions/Classes:**
  * `Atom` (Impact: 277.6)
    * *Intent:* /// An atom is used to add binding, change listening, thread safety and animation capabilities to //...
  * `ListAtom` (Impact: 102.7)
    * *Intent:* /// A list of atoms, that is itself an atom.
  * `lerp` (Impact: 35.8)
    * *Intent:* /// Linear interpolation between any two values a and b with factor t. /// Both values must be of th...
  * `dependOn` (Impact: 28.0)
    * *Intent:* // TODO: constrain "function"'s type based on tuple // TODO: optionally provide the function with an...
  * `FormattedAtom` (Impact: 27.1)
    * *Intent:* // TODO: reimplement using Atom.derived and its arena allocator
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 295`, `structural_boundaries: 167`, `args: 89`, `func_start: 83`, `class_start: 20`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 168`, `dead_code: 3`, `planned_debt: 8`, `duplicate_logic: 28`
* *Architecture:* `api: 81`, `concurrency: 3`, `import: 8`
* *Defense:* `safety: 123`, `doc: 77`, `test: 56`, `sync_locks: 62`, `immutability_locks: 157`, `cleanup: 40`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 68.771
  * `Choke Point (Betweenness):` 0.003191 | `Ripple Effect (Closeness):` 0.093185
  * `Imports (Out-Degree: 4):` std, AnimationController.zig, trait.zig, containers.zig, internal.zig
  * `Imported By (In-Degree: 12):` (Excluded from Brief to save tokens)

### `src/internal.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_11` (Drift: 15.241 IQR)
- **Top Global Matches:** file_cluster_11: 15.241, file_cluster_13: 15.366, file_cluster_0: 15.431
- **Magnitude:** 948.26 | **LOC:** 799 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (28.7986%), Tech Debt (12.317%)
**Top Internal Functions/Classes:**
  * `Widgeting` (Impact: 193.7)
    * *Intent:* /// Convenience function for creating widgets
  * `Events` (Impact: 127.8)
    * *Intent:* /// Convenience function for creating widgets
  * `iterateFields` (Impact: 27.6)
  * `setupEvents` (Impact: 19.8)
  * `TypeOfProperty` (Impact: 18.6)
    * *Intent:* // Properties
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 218`, `structural_boundaries: 68`, `args: 87`, `func_start: 69`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 37`, `dead_code: 17`, `planned_debt: 5`
* *Architecture:* `io: 1`, `api: 99`, `concurrency: 2`, `import: 15`
* *Defense:* `safety: 98`, `doc: 52`, `immutability_locks: 148`, `cleanup: 18`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 57.595
  * `Choke Point (Betweenness):` 0.004937 | `Ripple Effect (Closeness):` 0.100951
  * `Imports (Out-Degree: 5):` std, shared.zig, data.zig, root, AnimationController.zig, builtin, widget.zig, backend.zig...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `src/backends/android/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.114 IQR)
- **Top Global Matches:** file_cluster_11: 13.114, file_cluster_6: 13.119, file_cluster_0: 13.176
- **Magnitude:** 708.62 | **LOC:** 873 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (20.0251%), Tech Debt (98.8797%)
**Top Internal Functions/Classes:**
  * `add` (Impact: 81.3)
  * `Events` (Impact: 59.1)
  * `callback` (Impact: 54.2)
  * `getEventUserData` (Impact: 48.6)
  * `ellipse` (Impact: 33.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 152`, `structural_boundaries: 121`, `args: 75`, `func_start: 75`, `class_start: 15`
* *Risk/State:* `safety_bypasses: 91`, `high_risk_execution: 1`, `state_mutation: 39`, `dead_code: 6`, `planned_debt: 21`, `duplicate_logic: 9`
* *Architecture:* `io: 3`, `api: 96`, `concurrency: 17`, `import: 6`
* *Defense:* `safety: 109`, `doc: 2`, `sync_locks: 3`, `immutability_locks: 179`, `cleanup: 8`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy.zig, android, trait.zig, shared.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/containers.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.33%)
- **Global Archetype:** `file_cluster_11` (Drift: 13.681 IQR)
- **Top Global Matches:** file_cluster_11: 13.681, file_cluster_13: 13.699, file_cluster_6: 13.808
- **Magnitude:** 683.26 | **LOC:** 924 | **CtrlFlow:** 74.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.7683%), Tech Debt (62.6378%)
**Top Internal Functions/Classes:**
  * `GridLayout` (Impact: 117.6)
    * *Intent:* /// Grid layout based on the CSS Grid algorithm
  * `RowLayout` (Impact: 68.1)
    * *Intent:* /// Arranges items horizontally.
  * `ColumnLayout` (Impact: 67.8)
    * *Intent:* /// Arranges items vertically.
  * `getChild` (Impact: 34.0)
    * *Intent:* /// Searches recursively for a component named `name` and returns the first one found. /// If no com...
  * `MarginLayout` (Impact: 19.6)
    * *Intent:* /// Positions one item according to the given margins.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 249`, `structural_boundaries: 86`, `args: 42`, `func_start: 38`, `class_start: 12`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 101`, `dead_code: 9`, `planned_debt: 17`, `fragile_debt: 1`, `duplicate_logic: 2`
* *Architecture:* `api: 45`, `concurrency: 3`, `import: 16`
* *Defense:* `safety: 105`, `doc: 33`, `test: 5`, `immutability_locks: 122`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 29.07
  * `Choke Point (Betweenness):` 0.006257 | `Ripple Effect (Closeness):` 0.065482
  * `Imports (Out-Degree: 5):` std, data.zig, capy.zig, AnimationController.zig, widget.zig, backend.zig, internal.zig
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `android/Sdk.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.256 IQR)
- **Top Global Matches:** file_cluster_8: 11.256, file_cluster_7: 11.546, file_cluster_13: 11.742
- **Magnitude:** 670.5 | **LOC:** 1550 | **CtrlFlow:** 67.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (10.518%), Tech Debt (34.3946%)
**Top Internal Functions/Classes:**
  * `createApp` (Impact: 144.0)
    * *Intent:* /// Instantiates the full build pipeline to create an APK file. ///
  * `add` (Impact: 132.7)
  * `init` (Impact: 53.4)
    * *Intent:* /// Initializes the android SDK. /// It requires some input on which versions of the tool chains sho...
  * `validate` (Impact: 47.5)
  * `createLibCFile` (Impact: 22.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 196`, `structural_boundaries: 96`, `args: 38`, `func_start: 38`, `class_start: 24`
* *Risk/State:* `safety_bypasses: 43`, `state_mutation: 37`, `dead_code: 4`, `planned_debt: 1`, `duplicate_logic: 6`
* *Architecture:* `io: 28`, `api: 60`, `import: 4`
* *Defense:* `safety: 105`, `doc: 55`, `immutability_locks: 269`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.006711
  * `Imports (Out-Degree: 0):` std, builtin, auto-detect.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/win32/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.055 IQR)
- **Top Global Matches:** file_cluster_8: 12.055, file_cluster_13: 12.291, file_cluster_11: 12.323
- **Magnitude:** 532.26 | **LOC:** 1773 | **CtrlFlow:** 60.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.737%), Tech Debt (17.5497%)
**Top Internal Functions/Classes:**
  * `init` (Impact: 238.7)
  * `transWinError` (Impact: 3.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 225`, `structural_boundaries: 149`, `args: 101`, `func_start: 99`, `class_start: 21`
* *Risk/State:* `safety_bypasses: 127`, `state_mutation: 117`, `dead_code: 3`, `planned_debt: 27`
* *Architecture:* `io: 10`, `api: 142`, `import: 11`
* *Defense:* `safety: 74`, `doc: 15`, `immutability_locks: 214`, `cleanup: 20`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` std, zigwin32, Dropdown.zig, capy.zig, builtin, win32.zig, Monitor.zig, trait.zig...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/examples/egl/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.607 IQR)
- **Top Global Matches:** file_cluster_8: 11.607, file_cluster_7: 11.929, file_cluster_13: 11.967
- **Magnitude:** 385.02 | **LOC:** 905 | **CtrlFlow:** 58.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (22.0981%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `mainLoop` (Impact: 71.0)
  * `debugMessageCallback` (Impact: 28.4)
  * `insertPoint` (Impact: 20.5)
  * `processMotionEvent` (Impact: 17.1)
  * `processKeyEvent` (Impact: 10.7)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 93`, `structural_boundaries: 66`, `args: 25`, `func_start: 25`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 51`, `high_risk_execution: 2`, `state_mutation: 108`, `dead_code: 3`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `api: 15`, `concurrency: 11`, `import: 2`
* *Defense:* `safety: 27`, `doc: 11`, `sync_locks: 15`, `immutability_locks: 54`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, android
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/src/opensl.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.09%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.222 IQR)
- **Top Global Matches:** file_cluster_8: 12.222, file_cluster_13: 12.511, file_cluster_0: 12.622
- **Magnitude:** 381.36 | **LOC:** 497 | **CtrlFlow:** 64.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.5693%), Tech Debt (73.3074%)
**Top Internal Functions/Classes:**
  * `fromIid` (Impact: 189.9)
  * `getOutputStream` (Impact: 30.7)
  * `start` (Impact: 14.1)
  * `init` (Impact: 12.3)
  * `checkResult` (Impact: 11.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 159`, `structural_boundaries: 86`, `args: 13`, `func_start: 13`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 30`, `state_mutation: 66`, `planned_debt: 4`, `duplicate_logic: 2`, `orphaned_logic: 2`
* *Architecture:* `api: 10`, `concurrency: 2`, `import: 4`
* *Defense:* `safety: 39`, `sync_locks: 6`, `immutability_locks: 13`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, c.zig, audio.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/gtk/common.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.221 IQR)
- **Top Global Matches:** file_cluster_8: 12.221, file_cluster_13: 12.243, file_cluster_16: 12.522
- **Magnitude:** 370.66 | **LOC:** 320 | **CtrlFlow:** 64.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (37.945%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 116.4)
  * `gtkKeyPress` (Impact: 43.5)
  * `gtkButtonPress` (Impact: 30.3)
  * `gtkMouseMotion` (Impact: 16.5)
  * `getPreferredSize` (Impact: 8.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 65`, `structural_boundaries: 36`, `args: 24`, `func_start: 24`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 33`, `state_mutation: 22`
* *Architecture:* `api: 39`, `import: 6`
* *Defense:* `safety: 21`, `doc: 4`, `immutability_locks: 54`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy.zig, gtk.zig, backend.zig, trait.zig, shared.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/capy.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_4` (Drift: 13.387 IQR)
- **Local Micro-Species:** `Cluster 2: Procedural Core & Safety Wrappers` (Drift: 4.865 IQR)
- **Top Global Matches:** file_cluster_4: 13.387, file_cluster_8: 13.577, file_cluster_11: 13.771
- **Magnitude:** 368.06 | **LOC:** 635 | **CtrlFlow:** 64.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (64.3061%), Tech Debt (97.2598%)
**Top Internal Functions/Classes:**
  * `setTimeout` (Impact: 75.9)
  * `addChunk` (Impact: 43.8)
  * `update` (Impact: 35.4)
  * `pushAnswer` (Impact: 31.6)
  * `constructor` (Impact: 5.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 25`, `args: 13`, `func_start: 19`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 127`, `duplicate_logic: 4`
* *Architecture:* `api: 7`, `concurrency: 13`
* *Defense:* `safety: 10`, `doc: 7`, `immutability_locks: 15`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.125
  * `Choke Point (Betweenness):` 4.5e-05 | `Ripple Effect (Closeness):` 0.006711
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `src/backends/wasm/capy-worker.js` (JAVASCRIPT | Tier 2 | 🚨 AI THREAT: 98.89%)
- **Global Archetype:** `file_cluster_4` (Drift: 11.665 IQR)
- **Local Micro-Species:** `Cluster 3: Pure View Layer Components (UI)` (Drift: 5.701 IQR)
- **Top Global Matches:** file_cluster_4: 11.665, file_cluster_8: 11.873, file_cluster_15: 11.953
- **Magnitude:** 332.86 | **LOC:** 451 | **CtrlFlow:** 27.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.7698%), Tech Debt (94.2617%)
**Top Internal Functions/Classes:**
  * `clock_time_get` (Impact: 15.2)
  * `fd_write` (Impact: 14.5)
  * `waitForAnswer` (Impact: 11.8)
    * *Intent:* /**
  * `path_open` (Impact: 6.6)
  * `environ_get` (Impact: 6.2)
    * *Intent:* /** **/
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 76`, `args: 68`, `func_start: 73`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 74`, `dead_code: 1`, `planned_debt: 5`, `duplicate_logic: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 2`, `api: 7`, `concurrency: 56`, `import: 1`
* *Defense:* `safety: 2`, `doc: 11`, `test: 1`, `sync_locks: 2`, `immutability_locks: 40`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` extras.js
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/win32/win32.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.044 IQR)
- **Top Global Matches:** file_cluster_8: 10.044, file_cluster_7: 10.406, file_cluster_13: 10.537
- **Magnitude:** 315.54 | **LOC:** 423 | **CtrlFlow:** 65.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (5.8107%), Tech Debt (13.1596%)
**Top Internal Functions/Classes:**
  * `setWindowLongPtr` (Impact: 10.3)
  * `getWindowLongPtr` (Impact: 9.0)
  * `TabCtrl_InsertItemA` (Impact: 6.3)
  * `TabCtrl_InsertItemW` (Impact: 6.3)
  * `TabCtrl_GetCurSelA` (Impact: 5.5)
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
- **Global Archetype:** `file_cluster_16` (Drift: 12.985 IQR)
- **Top Global Matches:** file_cluster_16: 12.985, file_cluster_13: 13.069, file_cluster_11: 13.125
- **Magnitude:** 306.52 | **LOC:** 190 | **CtrlFlow:** 70.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3067%), Tech Debt (98.8877%)
**Top Internal Functions/Classes:**
  * `getClassNameString` (Impact: 98.7)
  * `invokeJni` (Impact: 10.5)
  * `callObjectMethod` (Impact: 10.0)
  * `callIntMethod` (Impact: 10.0)
  * `callFloatMethod` (Impact: 10.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 61`, `structural_boundaries: 25`, `args: 24`, `func_start: 24`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 6`, `dead_code: 1`, `duplicate_logic: 4`
* *Architecture:* `api: 38`, `import: 2`
* *Defense:* `safety: 32`, `doc: 6`, `immutability_locks: 61`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01534
  * `Imports (Out-Degree: 1):` std, android-support.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `android/src/android-support.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.34%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.734 IQR)
- **Top Global Matches:** file_cluster_13: 13.734, file_cluster_0: 13.914, file_cluster_11: 13.919
- **Magnitude:** 294.66 | **LOC:** 384 | **CtrlFlow:** 71.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (59.8827%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `makeNativeActivityGlue` (Impact: 39.2)
    * *Intent:* /// Returns a wrapper implementation for the given App type which implements all /// ANativeActivity...
  * `panic` (Impact: 32.2)
    * *Intent:* // Android Panic implementation
  * `ANativeActivity_onCreate` (Impact: 27.2)
    * *Intent:* /// Actual application entry point
  * `printSymbolInfoAt` (Impact: 24.2)
  * `invoke` (Impact: 16.8)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 66`, `structural_boundaries: 27`, `args: 28`, `func_start: 28`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 49`, `dead_code: 5`
* *Architecture:* `io: 3`, `api: 17`, `concurrency: 7`, `import: 11`
* *Defense:* `safety: 39`, `doc: 3`, `immutability_locks: 34`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 26.478
  * `Choke Point (Betweenness):` 0.000862 | `Ripple Effect (Closeness):` 0.026846
  * `Imports (Out-Degree: 6):` std, root, audio.zig, builtin, c.zig, NativeActivity.zig, NativeInvocationHandler.zig, egl.zig...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `src/backends/macos/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.31%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.698 IQR)
- **Top Global Matches:** file_cluster_8: 10.698, file_cluster_13: 10.807, file_cluster_4: 11.033
- **Magnitude:** 267.62 | **LOC:** 381 | **CtrlFlow:** 54.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (38.9942%), Tech Debt (99.6626%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 25.8)
  * `runStep` (Impact: 12.2)
  * `getFlippedNSView` (Impact: 9.1)
  * `getPreferredSize` (Impact: 8.4)
  * `showNativeMessageDialog` (Impact: 6.5)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 40`, `structural_boundaries: 34`, `args: 37`, `func_start: 37`, `class_start: 7`
* *Risk/State:* `safety_bypasses: 1`, `high_risk_execution: 1`, `state_mutation: 16`, `planned_debt: 7`, `duplicate_logic: 5`
* *Architecture:* `api: 71`, `concurrency: 18`, `import: 9`
* *Defense:* `safety: 9`, `doc: 1`, `immutability_locks: 67`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 2):` std, Button.zig, capy.zig, CapyAppDelegate.zig, Monitor.zig, trait.zig, shared.zig, objc...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `android/examples/invocationhandler/main.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.399 IQR)
- **Top Global Matches:** file_cluster_8: 12.399, file_cluster_4: 12.416, file_cluster_13: 12.567
- **Magnitude:** 252.86 | **LOC:** 242 | **CtrlFlow:** 74.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.651%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `timerInvoke` (Impact: 131.7)
  * `getOnClickListener` (Impact: 24.2)
  * `runOnUiThread` (Impact: 18.1)
    * *Intent:* /// Run the given function on the Android UI thread. This is necessary for manipulating the view hie...
  * `setAppContentViewImpl` (Impact: 15.0)
  * `mainLoop` (Impact: 5.6)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 53`, `structural_boundaries: 18`, `args: 11`, `func_start: 11`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 11`, `high_risk_execution: 2`, `state_mutation: 14`, `fragile_debt: 1`, `orphaned_logic: 1`
* *Architecture:* `io: 3`, `api: 8`, `concurrency: 15`, `import: 2`
* *Defense:* `safety: 42`, `doc: 2`, `immutability_locks: 44`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, android
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/fuzz.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 98.98%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.885 IQR)
- **Top Global Matches:** file_cluster_13: 14.885, file_cluster_11: 14.92, file_cluster_0: 14.942
- **Magnitude:** 221.28 | **LOC:** 218 | **CtrlFlow:** 69.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.3809%), Tech Debt (96.9302%)
**Top Internal Functions/Classes:**
  * `testFunction` (Impact: 50.3)
  * `Iterator` (Impact: 23.8)
  * `threwError` (Impact: 18.2)
  * `refine` (Impact: 17.6)
    * *Intent:* /// Tries to find counter-examples (case where there is no error) in the /// given time and adjust t...
  * `next` (Impact: 12.9)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 58`, `structural_boundaries: 26`, `args: 13`, `func_start: 13`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 38`, `dead_code: 5`, `duplicate_logic: 4`
* *Architecture:* `api: 13`, `import: 4`
* *Defense:* `safety: 22`, `doc: 4`, `test: 7`, `immutability_locks: 22`, `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.913
  * `Choke Point (Betweenness):` 3.4e-05 | `Ripple Effect (Closeness):` 0.039479
  * `Imports (Out-Degree: 1):` std, trait.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `android/src/NativeActivity.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.431 IQR)
- **Top Global Matches:** file_cluster_13: 13.431, file_cluster_8: 13.474, file_cluster_0: 13.503
- **Magnitude:** 213.74 | **LOC:** 209 | **CtrlFlow:** 78.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (35.0432%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `AndroidDisplayKeyboard` (Impact: 83.3)
  * `AndroidMakeFullscreen` (Impact: 36.8)
  * `AndroidRequestAppPermissions` (Impact: 31.3)
  * `AndroidGetUnicodeChar` (Impact: 10.6)
  * `get` (Impact: 9.1)
    * *Intent:* /// Get the JNIEnv associated with the current thread.
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 74`, `structural_boundaries: 20`, `args: 11`, `func_start: 11`
* *Risk/State:* `safety_bypasses: 5`, `state_mutation: 17`, `dead_code: 1`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 50`, `doc: 5`, `immutability_locks: 47`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 7.603
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.01534
  * `Imports (Out-Degree: 1):` std, android-support.zig
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `examples/osm-viewer.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.923 IQR)
- **Top Global Matches:** file_cluster_2: 12.923, file_cluster_17: 13.025, file_cluster_13: 13.132
- **Magnitude:** 213.54 | **LOC:** 296 | **CtrlFlow:** 66.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.6722%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `checkRequests` (Impact: 44.0)
  * `getTile` (Impact: 18.3)
    * *Intent:* // Implementation Methods
  * `show` (Impact: 14.4)
    * *Intent:* // All components have this method, which is automatically called // when Capy needs to create the n...
  * `mouseScroll` (Impact: 12.8)
  * `init` (Impact: 11.2)
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

### `src/backends/gles/backend.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.13%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.753 IQR)
- **Top Global Matches:** file_cluster_8: 10.753, file_cluster_13: 10.82, file_cluster_11: 11.052
- **Magnitude:** 208.0 | **LOC:** 318 | **CtrlFlow:** 58.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (14.2277%), Tech Debt (99.9996%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 18.8)
  * `runStep` (Impact: 14.8)
  * `create` (Impact: 11.3)
  * `compile` (Impact: 7.7)
  * `create` (Impact: 7.4)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 46`, `structural_boundaries: 33`, `args: 29`, `func_start: 29`, `class_start: 10`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 7`, `dead_code: 1`, `planned_debt: 4`, `duplicate_logic: 9`
* *Architecture:* `api: 56`, `import: 6`
* *Defense:* `safety: 15`, `doc: 1`, `immutability_locks: 41`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy.zig, glfw3.h, trait.zig, shared.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `build_capy.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.2%)
- **Global Archetype:** `file_cluster_6` (Drift: 13.694 IQR)
- **Top Global Matches:** file_cluster_6: 13.694, file_cluster_11: 13.816, file_cluster_13: 13.891
- **Magnitude:** 179.02 | **LOC:** 301 | **CtrlFlow:** 76.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (27.2073%), Tech Debt (78.6909%)
**Top Internal Functions/Classes:**
  * `handler` (Impact: 65.8)
  * `runStep` (Impact: 45.8)
    * *Intent:* /// Takes the given CompileStep and options and returns a run step. /// The run step from this funct...
  * `make` (Impact: 11.4)
  * `create` (Impact: 6.7)
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

### `examples/graph.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_2` (Drift: 12.493 IQR)
- **Top Global Matches:** file_cluster_2: 12.493, file_cluster_8: 12.732, file_cluster_17: 12.76
- **Magnitude:** 175.68 | **LOC:** 227 | **CtrlFlow:** 55.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (42.581%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `myDataFunction` (Impact: 19.8)
  * `draw` (Impact: 16.6)
  * `SetEasing` (Impact: 14.0)
    * *Intent:* // This demonstrates how you can use Zig's ability to generate functions at compile-time // in order...
  * `main` (Impact: 10.8)
  * `show` (Impact: 9.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 35`, `args: 21`, `func_start: 18`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 10`, `state_mutation: 41`, `planned_debt: 2`, `duplicate_logic: 2`, `orphaned_logic: 7`
* *Architecture:* `api: 11`, `import: 2`
* *Defense:* `safety: 12`, `immutability_locks: 26`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` std, capy
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/wasm/common.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.28%)
- **Global Archetype:** `file_cluster_13` (Drift: 11.211 IQR)
- **Top Global Matches:** file_cluster_13: 11.211, file_cluster_8: 11.404, file_cluster_11: 11.414
- **Magnitude:** 166.96 | **LOC:** 177 | **CtrlFlow:** 78.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (26.3203%), Tech Debt (31.8756%)
**Top Internal Functions/Classes:**
  * `Events` (Impact: 63.0)
  * `processEvent` (Impact: 38.2)
  * `init` (Impact: 7.2)
  * `setCallback` (Impact: 6.9)
  * `getWidth` (Impact: 4.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 29`, `structural_boundaries: 8`, `args: 13`, `func_start: 12`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 13`, `high_risk_execution: 1`, `state_mutation: 3`, `dead_code: 1`, `planned_debt: 3`
* *Architecture:* `api: 20`, `import: 6`
* *Defense:* `safety: 12`, `doc: 2`, `immutability_locks: 29`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, capy.zig, js.zig, trait.zig, shared.zig, Container.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/backends/win32/Monitor.zig` (ZIG | Tier 2 | 🚨 AI THREAT: 99.03%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.327 IQR)
- **Top Global Matches:** file_cluster_13: 13.327, file_cluster_8: 13.515, file_cluster_0: 13.622
- **Magnitude:** 153.84 | **LOC:** 197 | **CtrlFlow:** 53.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.8374%), Tech Debt (18.5041%)
**Top Internal Functions/Classes:**
  * `getList` (Impact: 25.4)
  * `getDpi` (Impact: 11.1)
  * `getInternalName` (Impact: 9.1)
  * `getNumberOfVideoModes` (Impact: 5.6)
  * `getVideoMode` (Impact: 4.0)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 44`, `structural_boundaries: 39`, `args: 15`, `func_start: 15`
* *Risk/State:* `safety_bypasses: 24`, `state_mutation: 39`, `planned_debt: 1`
* *Architecture:* `api: 23`, `import: 6`
* *Defense:* `safety: 26`, `immutability_locks: 28`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.851
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` std, zigwin32, capy.zig, builtin, win32.zig
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `src/backends/android/backend.zig` (ZIG) | Magnitude: 708.62 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 682, immutability_locks: 179, encapsulation: 159, globals: 156
- `src/containers.zig` (ZIG) | Magnitude: 683.26 | Delta: **0.018 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 748, branch: 249, encapsulation: 135, globals: 133
- `src/data.zig` (ZIG) | Magnitude: 1234.82 | Delta: **0.027 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 1091, branch: 295, encapsulation: 181, globals: 178
- `src/internal.zig` (ZIG) | Magnitude: 948.26 | Delta: **0.125 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 633, branch: 218, immutability_locks: 148, pointers: 119

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/backends/gtk/Dropdown.zig` (ZIG) | Magnitude: 40.1 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 30, immutability_locks: 20, encapsulation: 13, globals: 12
- `android/examples/minimal/main.zig` (ZIG) | Magnitude: 14.9 | Delta: **0.02 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 25, doc: 11, immutability_locks: 6, api: 5
- `src/async.zig` (ZIG) | Magnitude: 52.72 | Delta: **0.022 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 53, branch: 14, globals: 13, state_mutation: 12
- `android/tools/zip_add.zig` (ZIG) | Magnitude: 0.05 | Delta: **0.023 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 59, branch: 31, structural_boundaries: 17, globals: 17
- `src/fuzz.zig` (ZIG) | Magnitude: 221.28 | Delta: **0.035 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 172, branch: 58, state_mutation: 38, bitwise_ops: 32

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `src/dev_tools.zig` (ZIG) | Magnitude: 87.76 | Delta: **0.036 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_spaces: 114, branch: 46, encapsulation: 33, globals: 29
- `android/src/jni.zig` (ZIG) | Magnitude: 306.52 | Delta: **0.084 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 151, branch: 61, immutability_locks: 61, api: 38

### Mixed-Responsibility Refactoring Targets for: file_cluster_17
- `examples/fade.zig` (ZIG) | Magnitude: 25.52 | Delta: **0.107 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 32, ui_framework: 18, branch: 10, encapsulation: 7
- `examples/transition.zig` (ZIG) | Magnitude: 14.86 | Delta: **0.153 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 15, ui_framework: 13, encapsulation: 6, branch: 4

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `examples/totp.zig` (ZIG) | Magnitude: 9.4 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 16, ui_framework: 10, branch: 3, structural_boundaries: 3
- `examples/7gui/temperature-converter.zig` (ZIG) | Magnitude: 49.42 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 47, branch: 17, safety: 13, globals: 13
- `src/c_api.zig` (ZIG) | Magnitude: 57.24 | Delta: **0.049 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 30, branch: 16, api: 14, structural_boundaries: 12
- `src/testing.zig` (ZIG) | Magnitude: 8.38 | Delta: **0.059 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 10, branch: 4, api: 3, ui_framework: 3
- `examples/balls.zig` (ZIG) | Magnitude: 136.0 | Delta: **0.072 IQR** | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: indent_spaces: 176, encapsulation: 47, branch: 45, globals: 44

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `src/backends/wasm/capy.js` (JAVASCRIPT) | Magnitude: 368.06 | Delta: **0.19 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 127, indent_tabs: 118, branch: 46, indent_spaces: 31
- `src/backends/wasm/capy-worker.js` (JAVASCRIPT) | Magnitude: 332.86 | Delta: **0.208 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 324, structural_boundaries: 76, state_mutation: 74, func_start: 73

### Mixed-Responsibility Refactoring Targets for: file_cluster_6
- `build_capy.zig` (ZIG) | Magnitude: 179.02 | Delta: **0.122 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: indent_spaces: 248, branch: 64, immutability_locks: 43, globals: 37

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `android/examples/textview/main.zig` (ZIG) | Magnitude: 85.86 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 120, encapsulation: 28, globals: 26, immutability_locks: 26
- `c_examples/c_template.c` (C) | Magnitude: 7.08 | Delta: **0.009 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 10, api: 3, state_mutation: 2, import: 2
- `src/backends/macos/Monitor.zig` (ZIG) | Magnitude: 22.32 | Delta: **0.014 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 11, api: 8, structural_boundaries: 4, args: 4
- `android/examples/invocationhandler/main.zig` (ZIG) | Magnitude: 252.86 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 176, branch: 53, encapsulation: 51, globals: 48
- `src/components/Slider.zig` (ZIG) | Magnitude: 60.56 | Delta: **0.017 IQR** | Secondary Pull: `file_cluster_13`
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

- `src/AnimationController.zig` -> **Severity: 5.87** (Embedded: 0.0757 * Error Risk: 77.5274%)
- `src/widget.zig` -> **Severity: 5.588** (Embedded: 0.0692 * Error Risk: 80.7231%)
- `src/internal.zig` -> **Severity: 4.935** (Embedded: 0.101 * Error Risk: 48.8846%)
- `src/data.zig` -> **Severity: 4.864** (Embedded: 0.0932 * Error Risk: 52.1971%)
- `src/trait.zig` -> **Severity: 3.948** (Embedded: 0.074 * Error Risk: 53.3502%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `src/internal.zig` -> **Severity: 5538.232** (Blast Radius: 57.595 * Doc Risk: 96.1582%)
- `src/backends/wasm/js.zig` -> **Severity: 4919.5** (Blast Radius: 49.195 * Doc Risk: 100.0%)
- `src/data.zig` -> **Severity: 4178.003** (Blast Radius: 68.771 * Doc Risk: 60.7524%)
- `src/trait.zig` -> **Severity: 3413.346** (Blast Radius: 34.516 * Doc Risk: 98.8917%)
- `src/listener.zig` -> **Severity: 2545.541** (Blast Radius: 25.672 * Doc Risk: 99.1563%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
