# ARCHITECTURAL_BRIEF: ChrysaLisp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/vygr/ChrysaLisp.git` |
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
| Total Artifacts | 1054 |
| Analyzed Artifacts (Scanned) | 319 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 735 |
| Total LOC | 24624 |
| Volatility Index | 0.009 |
| % Scanned of codebase = | 30.3% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.7781 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.5683 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.2121 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 4 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 285 | 22947 | 89.3% |
| POWERSHELL | 9 | 259 | 2.8% |
| SHELL | 9 | 288 | 2.8% |
| XML | 6 | 0 | 1.9% |
| BATCH | 5 | 119 | 1.6% |
| MARKDOWN | 3 | 0 | 0.9% |
| MAKEFILE | 1 | 98 | 0.3% |
| C | 1 | 913 | 0.3% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Small Flat Repo` (z +0.25; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 78%, Data / Markup / Trivial 18%, Large Core Modules 2%, Interface Declarations Files 1%, Callbacks & Closures Files 0%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 308 | 96.6% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 11 | 3.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 735*

**Composition by Extension & Reason:**
- `.md`: 199x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3032 LOC)
- `.cpm`: 160x Excluded (Unsupported Extension: '.cpm')
- `.lisp`: 142x Excluded (Unsupported Extension: '.lisp'), 5x Unsupported Format (.lisp), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.vp`: 129x Excluded (Unsupported Extension: '.vp'), 4x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 25x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Saturation: Line 47 exceeds 500 chars), 1x Packed Payload Guard (Impossible Density: 4.61 hits/line)
- `.sdf`: 19x Excluded (Unsupported Extension: '.sdf')
- `.png`: 9x Excluded (Explicitly Denied Extension: '.png')
- `.ctf`: 6x Excluded (Unsupported Extension: '.ctf')
- `.tga`: 4x Excluded (Unsupported Extension: '.tga')
- `no_extension`: 2x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Unsupported Format (.undeterminable)
- `.flm`: 3x Excluded (Unsupported Extension: '.flm')
- `.lst`: 3x Excluded (Unsupported Extension: '.lst')
- `.svg`: 1x Excluded (Static Asset Blob without Intent: 1654 LOC), 1x Excluded (Monolithic Amalgamation: 49421 LOC exceeds safe regex boundaries), 1x Excluded (Embedded Array/Matrix Payload: 5355 commas in 726 LOC)
- `.pcb`: 3x Excluded (Unsupported Extension: '.pcb')
- `.ttf`: 2x Excluded (Explicitly Denied Extension: '.ttf')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 100.0 | 7.7 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 100.0 | 16.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 96.2 | 1.0 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 3.8 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 50.4 | 0.2 | 0.0 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 36.7 | 0.1 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 11.1 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 7.4 | 0.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 4.4 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 1.3 | 0.2 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 100.0 | 9.7 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 3.2 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 4002 | 177 | 32 | `class/lisp/root.inc` |
| cleanup | 69 | 36 | 1 | `src/host/gui_fb.c` |
| guards | 562 | 72 | 4 | `src/host/gui_fb.c` |
| danger | 521 | 37 | 2 | `funcs.sh` |
| concurrency | 25 | 7 | 0 | `service/lock/app.inc` |
| connectivity | 32 | 4 | 0 | `src/host/gui_fb.c` |
| io | 63 | 26 | 0 | `src/host/gui_fb.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 411 | 76 | 3 | `lib/task/pipe.inc` |
| time | 0 | 0 | 0 | - |
| serialization | 1 | 1 | 0 | `Makefile` |
| regex | 6 | 1 | 0 | `Makefile` |
| events | 907 | 51 | 2 | `lib/asm/vp.inc` |
| tests | 2 | 1 | 0 | `funcs.sh` |
| docs | 69 | 3 | 0 | `src/host/sdl_dummy.h` |
| debt | 50 | 11 | 0 | `src/host/gui_fb.c` |
| mutation | 1195 | 66 | 4 | `src/host/gui_fb.c` |
| dead_code | 8 | 4 | 0 | `funcs.ps1` |
| credential | 0 | 0 | 0 | - |
| threat | 215 | 10 | 0 | `src/host/vp64.cpp` |
| ml_ai | 63 | 18 | 0 | `lib/math/mesh.inc` |
| ui | 0 | 0 | 0 | - |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **0.0**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `src/host/gui_fb.c` (Hits: 7)
- `run_cube.sh` (Hits: 6)
- `Makefile` (Hits: 5)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **funcs.ps1** (`funcs.ps1`) — 7 inbound connections
2. **funcs.sh** (`funcs.sh`) — 7 inbound connections
3. **pii.h** (`src/host/pii.h`) — 5 inbound connections
4. **CONTRIBUTIONS.md** (`CONTRIBUTIONS.md`) — 1 inbound connections
5. **stop.ps1** (`stop.ps1`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **LLM.md** (`LLM.md`) — 52 outbound dependencies
2. **gui_fb.c** (`src/host/gui_fb.c`) — 17 outbound dependencies
3. **pii_windows.cpp** (`src/host/pii_windows.cpp`) — 15 outbound dependencies
4. **pii_darwin.cpp** (`src/host/pii_darwin.cpp`) — 14 outbound dependencies
5. **pii_linux.cpp** (`src/host/pii_linux.cpp`) — 13 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `host_gui_blit` **(Many-Argument Workhorses)** (@ `src/host/gui_raw.cpp`) -> Impact: **79.5** | LOC: 151
- `get_event_timeout` **(Compute Cores)** (@ `src/host/gui_fb.c`) -> Impact: **53.0** | LOC: 90
  * *Intent:* /* msec timeout 0 to poll, timeout -1 to block */
- `host_gui_create_texture` **(Many-Argument Workhorses)** (@ `src/host/gui_fb.c`) -> Impact: **49.2** | LOC: 53
  * *Intent:* /* allocate drawable for passed data and return a handle to it */
- `host_gui_create_texture` **(Many-Argument Workhorses)** (@ `src/host/gui_raw.cpp`) -> Impact: **49.1** | LOC: 51
  * *Intent:* //////////////////// // texture functions ////////////////////
- `host_gui_filled_box` **(Compute Cores)** (@ `src/host/gui_raw.cpp`) -> Impact: **33.6** | LOC: 50
- `main` **(Many-Argument Workhorses)** (@ `src/host/main.cpp`) -> Impact: **33.3** | LOC: 77
  * *Intent:* #endif
- `open_framebuffer` **(Compute Cores)** (@ `src/host/gui_fb.c`) -> Impact: **26.9** | LOC: 98
  * *Intent:* /* open linux framebuffer*/
- `pii_mprotect` **(Compute Cores)** (@ `src/host/pii_windows.cpp`) -> Impact: **22.9** | LOC: 18
- `read_mouse` **(Many-Argument Workhorses)** (@ `src/host/gui_fb.c`) -> Impact: **21.8** | LOC: 33
  * *Intent:* * --------+-----+-----+-----+-----+-----+-----+-----+----- * Byte 0 | 0 0 Neg-Y Neg-X 1 Mid Right Left * Byte 1 | X X X X X X X X * Byte 2 | Y Y Y Y Y...
- `host_audio_change_sfx` **(Compute Cores)** (@ `src/host/audio_sdl.cpp`) -> Impact: **20.5** | LOC: 28

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `src/host` | 11 | 2524.42 | 43.25% | 3.83% |
| `__monolith__` | 27 | 938.98 | 31.74% | 3.56% |
| `lib/text` | 11 | 246.96 | 9.37% | 0.0% |
| `lib/asm` | 11 | 212.54 | 7.19% | 0.0% |
| `lib/collections` | 10 | 182.62 | 7.01% | 0.0% |
| `apps/science/pcb` | 7 | 134.94 | 3.46% | 0.0% |
| `apps/system/terminal` | 8 | 126.18 | 3.82% | 0.0% |
| `lib/trans` | 5 | 122.94 | 7.49% | 0.0% |
| `gui/path` | 3 | 111.38 | 21.94% | 0.0% |
| `lib/math` | 5 | 107.0 | 5.34% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `funcs.ps1` -> **96.1917%** Exposure
- `apps/desktop/todo/config.inc` -> **81.7574%** Exposure
- `apps/desktop/todo/widgets.inc` -> **81.7574%** Exposure
- `src/host/main.cpp` -> **20.7969%** Exposure
- `src/host/gui_fb.c` -> **10.7489%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `funcs.ps1` -> **100.0%** Exposure
- `run_cube.ps1` -> **100.0%** Exposure
- `run_mesh.ps1` -> **100.0%** Exposure
- `run_tree.ps1` -> **100.0%** Exposure
- `funcs.sh` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `funcs.ps1` -> **5** Orphaned Functions | **0** Duplicates
- `src/host/main.cpp` -> **1** Orphaned Functions | **0** Duplicates
- `src/host/vp64.cpp` -> **1** Orphaned Functions | **0** Duplicates

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
- **Unknown Dependencies:** `160` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `funcs.ps1` (POWERSHELL) -> Cumulative Risk: **618.32**
- **Archetype:** `file_cluster_12` (Distance: N/A IQR)
- **Composition Archetype:** `Callbacks & Closures Files` (z +0.69)
- **Magnitude:** 209.82 | **LOC:** 112 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9956%), Tech Debt (96.1917%)
- **Heaviest Functions:** `boot_cpu_gui` (Callbacks & Closures, Impact: 19.0), `boot_cpu_tui` (Callbacks & Closures, Impact: 19.0), `add_link` (Callbacks & Closures, Impact: 10.5)

### 2. `src/host/gui_fb.c` (C) -> Cumulative Risk: **588.99**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.14)
- **Magnitude:** 1017.26 | **LOC:** 1064 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.3023%)
- **Heaviest Functions:** `get_event_timeout` (Compute Cores, Impact: 53.0), `host_gui_create_texture` (Many-Argument Workhorses, Impact: 49.2), `open_framebuffer` (Compute Cores, Impact: 26.9)

### 3. `funcs.sh` (SHELL) -> Cumulative Risk: **587.86**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z -0.04)
- **Magnitude:** 142.7 | **LOC:** 153 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.9996%), Verification (80.0%)
- **Heaviest Functions:** `main` (Compute Cores, Impact: 11.6), `boot_cpu_gui` (Compute Cores, Impact: 11.4), `boot_cpu_tui` (Compute Cores, Impact: 11.3)

### 4. `src/host/pii_windows.cpp` (CPP) -> Cumulative Risk: **541.99**
- **Archetype:** `file_cluster_0` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.68)
- **Magnitude:** 274.78 | **LOC:** 400 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.9888%), Safety Score (95.967%)
- **Heaviest Functions:** `pii_mprotect` (Compute Cores, Impact: 22.9), `pii_munmap` (Compute Cores, Impact: 18.8), `pii_dirlist` (Many-Argument Workhorses, Impact: 17.8)

### 5. `src/host/gui_raw.cpp` (CPP) -> Cumulative Risk: **538.73**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.50)
- **Magnitude:** 458.68 | **LOC:** 488 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (98.6318%), Verification (80.0%)
- **Heaviest Functions:** `host_gui_blit` (Many-Argument Workhorses, Impact: 79.5), `host_gui_create_texture` (Many-Argument Workhorses, Impact: 49.1), `host_gui_filled_box` (Compute Cores, Impact: 33.6)

### 6. `src/host/pii_linux.cpp` (CPP) -> Cumulative Risk: **522.77**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.29)
- **Magnitude:** 214.28 | **LOC:** 358 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7596%), Safety Score (94.7676%)
- **Heaviest Functions:** `walk_directory` (Compute Cores, Impact: 19.5), `pii_open` (Compute Cores, Impact: 17.2), `pii_open_shared` (Compute Cores, Impact: 13.0)

### 7. `src/host/pii_darwin.cpp` (CPP) -> Cumulative Risk: **522.48**
- **Archetype:** `file_cluster_15` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.49)
- **Magnitude:** 214.3 | **LOC:** 359 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.7527%), Safety Score (94.7225%)
- **Heaviest Functions:** `walk_directory` (Compute Cores, Impact: 19.5), `pii_open` (Compute Cores, Impact: 17.2), `pii_open_shared` (Compute Cores, Impact: 13.0)

### 8. `src/host/vp64.cpp` (CPP) -> Cumulative Risk: **498.52**
- **Archetype:** `file_cluster_13` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z -0.13)
- **Magnitude:** 151.22 | **LOC:** 490 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (99.995%), Cognitive Load (99.9901%)
- **Heaviest Functions:** `vp64` (Many-Argument Workhorses, Impact: 14.9)

### 9. `src/host/main.cpp` (CPP) -> Cumulative Risk: **463.97**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.17)
- **Magnitude:** 63.98 | **LOC:** 145 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), State Flux (98.9816%), Safety Score (91.8047%)
- **Heaviest Functions:** `main` (Many-Argument Workhorses, Impact: 33.3), `enableRawMode` (Interface Declarations, Impact: 1.4), `enableRawMode` (Interface Declarations, Impact: 1.4)

### 10. `src/host/audio_sdl.cpp` (CPP) -> Cumulative Risk: **355.15**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Interface Declarations Files` (z +1.35)
- **Magnitude:** 54.46 | **LOC:** 140 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Documentation (100.0%), Safety Score (80.1945%), State Flux (56.3374%)
- **Heaviest Functions:** `host_audio_change_sfx` (Compute Cores, Impact: 20.5), `host_audio_add_sfx` (Compute Cores, Impact: 5.1), `host_audio_init` (Interface Declarations, Impact: 3.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/host/gui_fb.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1017.26 | **LOC:** 1064 | **CtrlFlow:** 18.6% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (70.1474%), Tech Debt (10.7489%)
**Top Internal Functions/Classes:**
  * `get_event_timeout` **(Compute Cores)** (Impact: 53.0)
    * *Intent:* /* msec timeout 0 to poll, timeout -1 to block */
  * `host_gui_create_texture` **(Many-Argument Workhorses)** (Impact: 49.2)
    * *Intent:* /* allocate drawable for passed data and return a handle to it */
  * `open_framebuffer` **(Compute Cores)** (Impact: 26.9)
    * *Intent:* /* open linux framebuffer*/
  * `read_mouse` **(Many-Argument Workhorses)** (Impact: 21.8)
    * *Intent:* * --------+-----+-----+-----+-----+-----+-----+-----+----- * Byte 0 | 0 0 Neg-Y Neg-X 1 Mid Right Le...
  * `host_gui_filled_box` **(Compute Cores)** (Impact: 20.1)
    * *Intent:* /* fill rectangle with current color */
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Rce:* 1 instances
* *Amplified Cascading Flux:* 188 instances
* *Memory Alloc (weighted view):* 2
* *Sec Tainted Injection (weighted view):* 1
* *State Mutation (weighted view):* 603
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 117`, `args: 49`, `func_start: 34`, `class_start: 6`
* *Risk/State:* `safety_bypasses: 44`, `high_risk_execution: 4`, `state_mutation: 227`, `dead_code: 1`, `fragile_debt: 2`
* *Architecture:* `io: 7`, `api: 23`, `import: 17`
* *Defense:* `immutability_locks: 26`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` errno.h, fcntl.h, inttypes.h, fb.h, kd.h, keyboard.h, vt.h, poll.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/gui_raw.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 458.68 | **LOC:** 488 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (69.8327%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `host_gui_blit` **(Many-Argument Workhorses)** (Impact: 79.5)
  * `host_gui_create_texture` **(Many-Argument Workhorses)** (Impact: 49.1)
    * *Intent:* //////////////////// // texture functions ////////////////////
  * `host_gui_filled_box` **(Compute Cores)** (Impact: 33.6)
  * `host_gui_flush` **(Compute Cores)** (Impact: 11.3)
  * `host_gui_box` **(Compute Cores)** (Impact: 9.4)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 2 instances
* *Amplified Cascading Flux:* 73 instances
* *Memory Alloc (weighted view):* 1
* *State Mutation (weighted view):* 242
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 63`, `args: 34`, `func_start: 18`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 96`
* *Architecture:* `import: 4`
* *Defense:* `doc: 10`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, iostream, memory, stdint.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_windows.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_0` (Drift: 0.0 IQR)
- **Magnitude:** 274.78 | **LOC:** 400 | **CtrlFlow:** 20.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.0309%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `pii_mprotect` **(Compute Cores)** (Impact: 22.9)
  * `pii_munmap` **(Compute Cores)** (Impact: 18.8)
  * `pii_dirlist` **(Many-Argument Workhorses)** (Impact: 17.8)
  * `walk_directory` **(Compute Cores)** (Impact: 17.8)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 32 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 102
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 79`, `args: 34`, `func_start: 23`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 38`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` conio.h, direct.h, fcntl.h, io.h, iostream, pii.h, random, stdio.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_darwin.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 214.3 | **LOC:** 359 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.0011%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk_directory` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
  * `pii_open_shared` **(Compute Cores)** (Impact: 13.0)
  * `pii_mprotect` **(Compute Cores)** (Impact: 12.7)
  * `pii_mmap` **(Type Conversions)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 76`, `args: 30`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 23`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirent.h, fcntl.h, iostream, OSCacheControl.h, pii.h, random, stdio.h, string.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_linux.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 214.28 | **LOC:** 358 | **CtrlFlow:** 18.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (48.2449%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk_directory` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* */ #define FOLDER_PRE 0 #define FOLDER_POST 1
  * `pii_open` **(Compute Cores)** (Impact: 17.2)
  * `pii_open_shared` **(Compute Cores)** (Impact: 13.0)
  * `pii_mprotect` **(Compute Cores)** (Impact: 12.7)
  * `pii_mmap` **(Type Conversions)** (Impact: 12.7)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 23 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 69
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 76`, `args: 30`, `func_start: 22`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `state_mutation: 23`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirent.h, fcntl.h, iostream, pii.h, random, stdio.h, string.h, mman.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `funcs.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_12` (Drift: 0.0 IQR)
- **Magnitude:** 209.82 | **LOC:** 112 | **CtrlFlow:** 36.5% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (81.1278%), Tech Debt (96.1917%)
**Top Internal Functions/Classes:**
  * `boot_cpu_gui` **(Callbacks & Closures)** (Impact: 19.0)
  * `boot_cpu_tui` **(Callbacks & Closures)** (Impact: 19.0)
  * `add_link` **(Callbacks & Closures)** (Impact: 10.5)
  * `main` **(Callbacks & Closures)** (Impact: 7.6)
  * `zero_pad` **(Callbacks & Closures)** (Impact: 6.0)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 45 instances
* *State Mutation (weighted view):* 142
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `structural_boundaries: 8`, `args: 5`, `func_start: 6`
* *Risk/State:* `high_risk_execution: 6`, `state_mutation: 52`, `unreferenced_by_name: 5`
* *Architecture:* `io: 3`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.946
  * `Choke Point (Betweenness):` 6.8e-05 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 1):` $NHROOT\stop.ps1
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/host/vp64.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_13` (Drift: 0.0 IQR)
- **Magnitude:** 151.22 | **LOC:** 490 | **CtrlFlow:** 40.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (99.9901%), Tech Debt (10.5324%)
**Top Internal Functions/Classes:**
  * `vp64` **(Many-Argument Workhorses)** (Impact: 14.9)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 29 instances
* *State Mutation (weighted view):* 128
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 7`, `args: 3`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `state_mutation: 70`, `unreferenced_by_name: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` atomic, cmath, immintrin.h, intrin.h, iostream, pii.h, types.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `funcs.sh` (SHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 142.7 | **LOC:** 153 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (70.8005%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `main` **(Compute Cores)** (Impact: 11.6)
  * `boot_cpu_gui` **(Compute Cores)** (Impact: 11.4)
  * `boot_cpu_tui` **(Compute Cores)** (Impact: 11.3)
  * `add_link` **(Compute Cores)** (Impact: 9.6)
  * `zero_pad` **(Compute Cores)** (Impact: 6.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 25 instances
* *State Mutation (weighted view):* 77
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 62`, `args: 23`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 84`, `state_mutation: 27`
* *Architecture:* `io: 5`, `api: 5`, `concurrency: 3`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 19.946
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.021739
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `gui/path/lisp.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 82.72 | **LOC:** 194 | **CtrlFlow:** 22.6% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (65.8342%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 21 instances
* *State Mutation (weighted view):* 64
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 1`, `args: 17`
* *Risk/State:* `state_mutation: 22`
* *Architecture:* `io: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_cube.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 75.64 | **LOC:** 37 | **CtrlFlow:** 25.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (65.4753%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 20 instances
* *State Mutation (weighted view):* 60
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`
* *Risk/State:* `state_mutation: 20`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/main.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 63.98 | **LOC:** 145 | **CtrlFlow:** 14.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (49.8837%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `main` **(Many-Argument Workhorses)** (Impact: 33.3)
    * *Intent:* #endif
  * `enableRawMode` **(Interface Declarations)** (Impact: 1.4)
  * `enableRawMode` **(Interface Declarations)** (Impact: 1.4)
  * `disableRawMode` **(Interface Declarations)** (Impact: 1.2)
  * `disableRawMode` **(Interface Declarations)** (Impact: 1.1)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 23
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 22`, `args: 14`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 9`, `unreferenced_by_name: 1`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` fcntl.h, io.h, iostream, pii.h, stdint.h, string.h, stat.h, termios.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/lisp/root.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Drift: 0.0 IQR)
- **Magnitude:** 57.6 | **LOC:** 1430 | **CtrlFlow:** 13.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (8.6582%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 162`, `structural_boundaries: 234`, `args: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 8`
* *Architecture:* `io: 2`
* *Defense:* `safety: 5`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_mesh.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 57.52 | **LOC:** 31 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (61.7748%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 14 instances
* *State Mutation (weighted view):* 42
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`
* *Risk/State:* `state_mutation: 14`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/audio_sdl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_14` (Drift: 0.0 IQR)
- **Magnitude:** 54.46 | **LOC:** 140 | **CtrlFlow:** 17.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (16.0452%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `host_audio_change_sfx` **(Compute Cores)** (Impact: 20.5)
  * `host_audio_add_sfx` **(Compute Cores)** (Impact: 5.1)
  * `host_audio_init` **(Interface Declarations)** (Impact: 3.8)
  * `host_audio_remove_sfx` **(Interface Declarations)** (Impact: 3.4)
  * `host_audio_play_sfx` **(Interface Declarations)** (Impact: 3.3)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 2 instances
* *State Mutation (weighted view):* 9
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 25`, `args: 8`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 5`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h, SDL_mixer.h, SDL_rwops.h, iostream, stdint.h, string, unordered_map
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_tree.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 42.5 | **LOC:** 34 | **CtrlFlow:** 20.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (59.8688%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 9 instances
* *State Mutation (weighted view):* 27
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 5`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/gui_sdl.cpp` (CPP | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 41.14 | **LOC:** 155 | **CtrlFlow:** 2.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (7.5212%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `host_gui_init` **(Compute Cores)** (Impact: 4.3)
  * `host_gui_create_texture` **(Parameter Forwarders)** (Impact: 2.9)
  * `host_gui_set_texture_color` **(Parameter Forwarders)** (Impact: 2.5)
  * `host_gui_set_color` **(Parameter Forwarders)** (Impact: 2.4)
  * `host_gui_blit` **(Parameter Forwarders)** (Impact: 2.2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 3`, `structural_boundaries: 48`, `args: 18`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 4`
* *Architecture:* `import: 1`
* *Defense:* `immutability_locks: 7`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/text/document.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 39.46 | **LOC:** 297 | **CtrlFlow:** 8.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (10.7084%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 5 instances
* *State Mutation (weighted view):* 19
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 22`, `structural_boundaries: 2`, `args: 29`
* *Risk/State:* `state_mutation: 9`
* *Architecture:* None
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/science/pcb/router.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 38.14 | **LOC:** 661 | **CtrlFlow:** 5.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (6.7586%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 3 instances
* *State Mutation (weighted view):* 11
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`, `args: 101`
* *Risk/State:* `high_risk_execution: 5`, `state_mutation: 5`
* *Architecture:* None
* *Defense:* `immutability_locks: 2`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_ring.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 36.38 | **LOC:** 24 | **CtrlFlow:** 21.1% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (57.9324%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 7 instances
* *State Mutation (weighted view):* 21
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 7`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_cube.sh` (SHELL | Tier 0 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_15` (Drift: 0.0 IQR)
- **Magnitude:** 35.96 | **LOC:** 39 | **CtrlFlow:** 21.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (63.6453%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` **(Unclassified)** (Impact: 9.5)
  * `__global_context__` **(Unclassified)** (Impact: 1.8)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 8 instances
* *State Mutation (weighted view):* 24
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 17`, `args: 1`
* *Risk/State:* `safety_bypasses: 41`, `state_mutation: 8`
* *Architecture:* `io: 6`, `import: 1`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` funcs.sh
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/text/buffer.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 34.6 | **LOC:** 1351 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 83`, `args: 376`
* *Risk/State:* None
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/text/regexp.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 34.46 | **LOC:** 343 | **CtrlFlow:** 28.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (17.493%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 4 instances
* *State Mutation (weighted view):* 13
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 91`, `structural_boundaries: 2`, `args: 108`
* *Risk/State:* `state_mutation: 5`
* *Architecture:* None
* *Defense:* `safety: 5`, `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 33.36 | **LOC:** 23 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.9834%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_tui.ps1` (POWERSHELL | Tier 2 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 33.36 | **LOC:** 23 | **CtrlFlow:** 22.2% | **Authorship Centralization:** 100.0%
- **Risk Profile:** Cognitive Load (54.9834%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 6 instances
* *State Mutation (weighted view):* 18
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 4`
* *Risk/State:* `state_mutation: 6`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `lib/trans/x86_64.inc` (CPP | Tier 4 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Drift: 0.0 IQR)
- **Magnitude:** 32.28 | **LOC:** 796 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (9.302%), Tech Debt (0.0%)
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Memory Alloc (weighted view):* 0
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 123`, `args: 167`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* None
* *Defense:* `immutability_locks: 61`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 2.87
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

*No highly conflicted/drifting files detected within the 0.9 IQR threshold.*

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/host/gui_fb.c` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 1017.26
- `src/host/gui_raw.cpp` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 458.68
- `funcs.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 209.82
- `run_cube.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 75.64
- `class/lisp/root.inc` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 57.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `funcs.ps1` -> **Severity: 0.007** (Bridge: 0.0001 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `funcs.ps1` -> **Severity: 2.174** (Embedded: 0.0217 * Error Risk: 99.9956%)
- `funcs.sh` -> **Severity: 2.174** (Embedded: 0.0217 * Error Risk: 99.9996%)
- `stop.ps1` -> **Severity: 1.262** (Embedded: 0.0133 * Error Risk: 95.2574%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `funcs.ps1` -> **Severity: 997.3** (Blast Radius: 19.946 * Doc Risk: 50.0%)
- `funcs.sh` -> **Severity: 997.3** (Blast Radius: 19.946 * Doc Risk: 50.0%)
- `src/host/audio_sdl.cpp` -> **Severity: 287.0** (Blast Radius: 2.87 * Doc Risk: 100.0%)
- `src/host/gui_sdl.cpp` -> **Severity: 287.0** (Blast Radius: 2.87 * Doc Risk: 100.0%)
- `src/host/main.cpp` -> **Severity: 287.0** (Blast Radius: 2.87 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
