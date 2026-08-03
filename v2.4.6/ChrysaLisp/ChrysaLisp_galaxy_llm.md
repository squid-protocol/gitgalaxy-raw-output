# ARCHITECTURAL_BRIEF: ChrysaLisp
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Target Path** | `/srv/storage_16tb/projects/gitgalaxy/data/corpus_assembly/ChrysaLisp` |
| **Timestamp** | `2026-08-03T19:26:19.101273+00:00` |
| **Scan Duration** | `2.27s` |
| **Git Branch** | `master` |
| **Git Commit** | `8d8d528d59b1f58c9f22160088d9e49226f95bd4` |
| **Git Remote** | `https://github.com/vygr/ChrysaLisp.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |

## 0.5 AI THREAT AUDIT STATUS
> **🚨 ML_CONFIRMED_THREAT_DETECTED**
> XGBoost Structural Signatures model identified 244 malicious artifacts.

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
| Total Artifacts | 1054 |
| Analyzed Artifacts (Scanned) | 253 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 801 |
| Total LOC | 13929 |
| Volatility Index | 0.008 |
| % Scanned of codebase = | 24.0% |
| Dominant Lang | CPP |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.6489 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.7215 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 0.0% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 1.75 | Hops between files. Lower = Tighter coupling. |
| Articulation Pts | 3 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| CPP | 219 | 12851 | 86.6% |
| POWERSHELL | 9 | 259 | 3.6% |
| SHELL | 9 | 281 | 3.6% |
| XML | 6 | 0 | 2.4% |
| BATCH | 5 | 119 | 2.0% |
| MARKDOWN | 3 | 0 | 1.2% |
| MAKEFILE | 1 | 98 | 0.4% |
| C | 1 | 321 | 0.4% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `8.441`
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| file_cluster_8 | 240 | 94.9% |
| file_cluster_13 | 4 | 1.6% |
| file_cluster_15 | 2 | 0.8% |
| file_cluster_12 | 1 | 0.4% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 6 | 2.4% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 801*

**Composition by Extension & Reason:**
- `.md`: 199x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Lexical Monotony: High structural repetition detected in 3032 LOC)
- `.cpm`: 159x Excluded (Unsupported Extension: '.cpm'), 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.lisp`: 137x Excluded (Unsupported Extension: '.lisp'), 9x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 5x Unsupported Format (.lisp)
- `.vp`: 126x Excluded (Unsupported Extension: '.vp'), 7x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
- `.inc`: 96x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir)
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

## 6. RISK EXPOSURE ANALYSIS (0-100%)
| Risk Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Cognitive Load Exposure | 0.0 | 100.0 | 23.2 | 7.4 | 5.0 |
| Error & Exception Exposure | 0.0 | 100.0 | 28.7 | 9.4 | 0.0 |
| Tech Debt Exposure | 0.0 | 100.0 | 6.3 | 0.0 | 0.0 |
| Testing Exposure | 0.0 | 80.0 | 4.2 | 2.3 | 2.3 |
| API Exposure | 0.0 | 13.9 | 0.6 | 0.0 | 0.0 |
| Concurrency Exposure | 0.0 | 48.0 | 0.2 | 0.0 | 0.0 |
| State Flux Exposure | 0.0 | 100.0 | 49.0 | 34.5 | 0.0 |
| Commented Logic Exposure | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Specification Exposure | 0.0 | 100.0 | 80.1 | 100.0 | 100.0 |
| Instability Exposure | 0.0 | 1.3 | 0.2 | 0.0 | 0.0 |
| Volatility Exposure | 0.0 | 100.0 | 8.3 | 0.0 | 0.0 |
| Documentation Exposure | 0.0 | 100.0 | 39.2 | 30.9 | 11.9 |
| Algorithmic DoS Exposure | 0.0 | 100.0 | 0.8 | 0.0 | 0.0 |
| Obfuscation & Evasion Surface | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Exploit Generation Surface | 0.0 | 72.7 | 0.6 | 0.0 | 0.0 |
| Weaponizable Injection Vectors | 0.0 | 100.0 | 1.6 | 0.0 | 0.0 |
| Raw Memory Manipulation | 0.0 | 10.0 | 0.2 | 0.0 | 0.0 |
| Hardcoded Payload Artifacts | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `apps/science/pcb/router.inc` (Hits: 53)
- `sys/lisp.inc` (Hits: 15)
- `service/audio/app.inc` (Hits: 11)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **funcs.sh** (`funcs.sh`) — 7 inbound connections
2. **pii.h** (`src/host/pii.h`) — 5 inbound connections
3. **sdl_dummy.h** (`src/host/sdl_dummy.h`) — 1 inbound connections
4. **class.inc** (`class/str/class.inc`) — 1 inbound connections
5. **class.inc** (`sys/mem/class.inc`) — 1 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **gui_fb.c** (`src/host/gui_fb.c`) — 17 outbound dependencies
2. **pii_windows.cpp** (`src/host/pii_windows.cpp`) — 15 outbound dependencies
3. **pii_darwin.cpp** (`src/host/pii_darwin.cpp`) — 14 outbound dependencies
4. **pii_linux.cpp** (`src/host/pii_linux.cpp`) — 13 outbound dependencies
5. **main.cpp** (`src/host/main.cpp`) — 10 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `host_gui_blit` (@ `src/host/gui_raw.cpp`) -> Impact: **79.5** | LOC: 151
- `host_gui_init` (@ `src/host/gui_fb.c`) -> Impact: **71.2** | LOC: 83
- `host_gui_filled_box` (@ `src/host/gui_raw.cpp`) -> Impact: **46.5** | LOC: 50
- `boot_cpu_gui` (@ `funcs.ps1`) -> Impact: **46.0** | LOC: 20
- `boot_cpu_tui` (@ `funcs.ps1`) -> Impact: **46.0** | LOC: 20
- `walk_directory` (@ `src/host/pii_darwin.cpp`) -> Impact: **36.8** | LOC: 44
- `walk_directory` (@ `src/host/pii_linux.cpp`) -> Impact: **36.8** | LOC: 44
- `walk_directory` (@ `src/host/pii_windows.cpp`) -> Impact: **33.4** | LOC: 44
- `main` (@ `src/host/main.cpp`) -> Impact: **33.3** | LOC: 77
  * *Intent:* #endif
- `blit_colorblend` (@ `src/host/gui_fb.c`) -> Impact: **29.8** | LOC: 35
  * *Intent:* /* set global clipping rectangle */

## 8.5 ALGORITHMIC & DATABASE BOTTLENECKS
> Highlights the most computationally expensive and database-heavy functions across the repository.

### Highest Time Complexity (Big-O)
- `walk_directory` (@ `src/host/pii_darwin.cpp`) -> **O(2^N) [Recursive]**
- `walk_directory` (@ `src/host/pii_linux.cpp`) -> **O(2^N) [Recursive]**
- `walk_directory` (@ `src/host/pii_windows.cpp`) -> **O(2^N) [Recursive]**
- `blit_colorblend` (@ `src/host/gui_fb.c`) -> **O(N^6)**
  * *Intent:* /* set global clipping rectangle */
- `blit_colormod` (@ `src/host/gui_fb.c`) -> **O(N^6)**
- `blit_blend` (@ `src/host/gui_fb.c`) -> **O(N^6)**
- `boot_cpu_gui` (@ `funcs.ps1`) -> **O(N^4)**
- `boot_cpu_tui` (@ `funcs.ps1`) -> **O(N^4)**
- `main` (@ `funcs.ps1`) -> **O(N^3)**
- `host_gui_init` (@ `src/host/gui_fb.c`) -> **O(N^3)**

### Highest Data Gravity (Database Complexity)
- `host_gui_blit` (@ `src/host/gui_raw.cpp`) -> DB Complexity: **98**
- `host_gui_init` (@ `src/host/gui_fb.c`) -> DB Complexity: **40**
- `host_gui_filled_box` (@ `src/host/gui_raw.cpp`) -> DB Complexity: **30**
- `pii_dirlist` (@ `src/host/pii_windows.cpp`) -> DB Complexity: **28**
- `blit_colorblend` (@ `src/host/gui_fb.c`) -> DB Complexity: **26**
  * *Intent:* /* set global clipping rectangle */
- `main` (@ `funcs.ps1`) -> DB Complexity: **23**
- `blit_colormod` (@ `src/host/gui_fb.c`) -> DB Complexity: **23**
- `blit_blend` (@ `src/host/gui_fb.c`) -> DB Complexity: **22**
- `walk_directory` (@ `src/host/pii_windows.cpp`) -> DB Complexity: **17**
- `vp64` (@ `src/host/vp64.cpp`) -> DB Complexity: **16**

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Cog Load | Avg Debt |
|---|---|---|---|---|
| `src/host` | 11 | 3060.08 | 52.95% | 10.24% |
| `__monolith__` | 27 | 1369.54 | 56.29% | 36.91% |
| `class/lisp` | 4 | 346.08 | 8.56% | 0.0% |
| `sys/list` | 2 | 244.56 | 26.52% | 0.0% |
| `apps/science/pcb` | 7 | 215.16 | 9.18% | 0.0% |
| `apps/system/terminal` | 8 | 151.12 | 12.41% | 0.0% |
| `gui/path` | 3 | 138.38 | 46.5% | 0.0% |
| `gui/view` | 3 | 119.08 | 26.73% | 0.0% |
| `sys/pii` | 4 | 116.46 | 21.07% | 0.0% |
| `apps/media/whiteboard` | 3 | 97.92 | 10.47% | 0.0% |

## 10. TARGETED RISK VECTORS (Top 5 by Exposure)
### Highest Tech Debt (Fragile/Planned)
- `stop.sh` -> **100.0%** Exposure
- `funcs.sh` -> **99.9999%** Exposure
- `run.sh` -> **99.9996%** Exposure
- `run_star.sh` -> **99.9996%** Exposure
- `run_tui.sh` -> **99.9996%** Exposure
### Highest State Flux (Mutation/Volatility)
- `funcs.ps1` -> **100.0%** Exposure
- `run.ps1` -> **100.0%** Exposure
- `run_cube.ps1` -> **100.0%** Exposure
- `run_mesh.ps1` -> **100.0%** Exposure
- `run_ring.ps1` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `funcs.sh` -> **0** Orphaned Functions | **8** Duplicates
- `funcs.ps1` -> **5** Orphaned Functions | **0** Duplicates
- `src/host/gui_fb.c` -> **5** Orphaned Functions | **0** Duplicates
- `run.sh` -> **1** Orphaned Functions | **0** Duplicates
- `run_cube.sh` -> **1** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
> **CRITICAL THREATS DETECTED.** The following files possess the structural signatures of known vulnerabilities.

1. **`src/host/vp64.cpp`** -> AI Confidence: **99.48%**
2. **`src/host/gui_fb.c`** -> AI Confidence: **99.39%**
3. **`run.ps1`** -> AI Confidence: **99.29%**
4. **`run_cube.ps1`** -> AI Confidence: **99.29%**
5. **`run_mesh.ps1`** -> AI Confidence: **99.29%**
6. **`run_ring.ps1`** -> AI Confidence: **99.29%**
7. **`run_star.ps1`** -> AI Confidence: **99.29%**
8. **`run_tree.ps1`** -> AI Confidence: **99.29%**
9. **`run_tui.ps1`** -> AI Confidence: **99.29%**
10. **`stop.ps1`** -> AI Confidence: **99.29%**
11. **`run.sh`** -> AI Confidence: **99.29%**
12. **`run_cube.sh`** -> AI Confidence: **99.29%**
13. **`run_mesh.sh`** -> AI Confidence: **99.29%**
14. **`run_ring.sh`** -> AI Confidence: **99.29%**
15. **`run_star.sh`** -> AI Confidence: **99.29%**
16. **`run_tree.sh`** -> AI Confidence: **99.29%**
17. **`run_tui.sh`** -> AI Confidence: **99.29%**
18. **`apps/desktop/todo/config.inc`** -> AI Confidence: **99.29%**
19. **`apps/games/chess/config.inc`** -> AI Confidence: **99.29%**
20. **`apps/games/chess/ui.inc`** -> AI Confidence: **99.29%**
21. **`apps/media/whiteboard/ui.inc`** -> AI Confidence: **99.29%**
22. **`apps/science/pcb/router.inc`** -> AI Confidence: **99.29%**
23. **`apps/system/files/ui.inc`** -> AI Confidence: **99.29%**
24. **`apps/system/profile/config.inc`** -> AI Confidence: **99.29%**

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

### Exploit Generation Surface
- `tests/utils.inc` -> **72.6553%** Exposure
- `apps/media/whiteboard/ui.inc` -> **20.0%** Exposure
- `class/lisp/root.inc` -> **20.0%** Exposure
- `src/host/gui_fb.c` -> **20.0%** Exposure
- `apps/tools/edit/debug.inc` -> **16.1744%** Exposure
### Weaponizable Injection Vectors
- `stop.sh` -> **100.0%** Exposure
- `apps/media/whiteboard/ui.inc` -> **100.0%** Exposure
- `tests/utils.inc` -> **100.0%** Exposure
- `apps/tools/edit/debug.inc` -> **99.9855%** Exposure
### Raw Memory Manipulation
- `class/lisp/root.inc` -> **10.0%** Exposure
- `service/gui/actions.inc` -> **10.0%** Exposure
- `usr/Guest/env.inc` -> **9.9996%** Exposure
- `apps/media/whiteboard/ui.inc` -> **9.997%** Exposure
- `apps/tools/edit/debug.inc` -> **2.0946%** Exposure
### Algorithmic DoS Exposure
- `funcs.ps1` -> **100.0%** Exposure
- `src/host/gui_fb.c` -> **100.0%** Exposure
- `src/host/audio_sdl.cpp` -> **4.5654%** Exposure

## 10.7 AUTONOMOUS AI VULNERABILITIES (AGENTIC RCE & PROMPT INJECTION)
> **AI CONTEXT:** Identifies untrusted data flowing into LLM context windows (Prompt Injection) and LLM outputs flowing into dynamic execution (Agentic RCE).

*No autonomous AI vulnerabilities detected.*

## 10.8 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `3` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `108` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `funcs.ps1` (POWERSHELL) -> Cumulative Risk: **788.53**
- **Archetype:** `file_cluster_15` (Distance: 14.023 IQR)
- **Magnitude:** 308.02 | **LOC:** 112 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `boot_cpu_gui` (Impact: 46.0), `boot_cpu_tui` (Impact: 46.0), `add_link` (Impact: 21.5)

### 2. `src/host/gui_fb.c` (C) -> Cumulative Risk: **778.88**
- **Archetype:** `file_cluster_13` (Distance: 14.237 IQR)
- **Magnitude:** 663.92 | **LOC:** 1064 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Algorithmic Dos (100.0%)
- **Heaviest Functions:** `host_gui_init` (Impact: 71.2), `blit_colorblend` (Impact: 29.8), `blit_colormod` (Impact: 29.7)

### 3. `funcs.sh` (SHELL) -> Cumulative Risk: **637.8**
- **Archetype:** `file_cluster_8` (Distance: 12.128 IQR)
- **Magnitude:** 174.36 | **LOC:** 153 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9999%), Safety Score (99.9955%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 19.3), `Anonymous_Block` (Impact: 18.0), `Anonymous_Block` (Impact: 17.9)

### 4. `run_mesh.sh` (SHELL) -> Cumulative Risk: **512.97**
- **Archetype:** `file_cluster_8` (Distance: 10.213 IQR)
- **Magnitude:** 25.4 | **LOC:** 31 | **CtrlFlow:** 93.8% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9447%), Safety Score (99.8811%), Tech Debt (99.8499%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 17.1), `__global_context__` (Impact: 1.8)

### 5. `run_cube.sh` (SHELL) -> Cumulative Risk: **510.05**
- **Archetype:** `file_cluster_8` (Distance: 9.835 IQR)
- **Magnitude:** 31.96 | **LOC:** 39 | **CtrlFlow:** 95.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Safety Score (99.9992%), State Flux (99.4363%), Tech Debt (98.6851%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 23.5), `__global_context__` (Impact: 1.8)

### 6. `run_tree.sh` (SHELL) -> Cumulative Risk: **508.99**
- **Archetype:** `file_cluster_8` (Distance: 11.212 IQR)
- **Magnitude:** 28.46 | **LOC:** 33 | **CtrlFlow:** 92.3% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Tech Debt (99.9313%), Safety Score (99.5977%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 14.2), `__global_context__` (Impact: 1.8)

### 7. `run_star.sh` (SHELL) -> Cumulative Risk: **500.72**
- **Archetype:** `file_cluster_8` (Distance: 10.454 IQR)
- **Magnitude:** 15.7 | **LOC:** 21 | **CtrlFlow:** 85.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), State Flux (99.9999%), Tech Debt (99.9996%), Cognitive Load (94.947%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 7.6), `__global_context__` (Impact: 1.8)

### 8. `run_cube.ps1` (POWERSHELL) -> Cumulative Risk: **497.55**
- **Archetype:** `file_cluster_8` (Distance: 13.505 IQR)
- **Magnitude:** 82.64 | **LOC:** 37 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Safety Score (99.38%), Documentation (88.9452%)

### 9. `apps/media/whiteboard/ui.inc` (CPP) -> Cumulative Risk: **495.85**
- **Archetype:** `file_cluster_8` (Distance: 10.68 IQR)
- **Magnitude:** 64.92 | **LOC:** 323 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Churn (100.0%), Injection Surface (100.0%), State Flux (95.7929%)

### 10. `run_ring.sh` (SHELL) -> Cumulative Risk: **493.17**
- **Archetype:** `file_cluster_8` (Distance: 9.183 IQR)
- **Magnitude:** 15.82 | **LOC:** 22 | **CtrlFlow:** 90.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** Spec Match (100.0%), Tech Debt (99.999%), State Flux (99.5504%), Safety Score (93.5031%)
- **Heaviest Functions:** `Anonymous_Block` (Impact: 10.7), `__global_context__` (Impact: 1.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `src/host/gui_raw.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 14.817 IQR)
- **Local Micro-Species:** `Cluster 1: Documented API Headers & Entity Definitions` (Drift: 5.545 IQR)
- **Top Global Matches:** file_cluster_8: 14.817, file_cluster_13: 14.935, file_cluster_7: 14.945
- **Magnitude:** 764.48 | **LOC:** 488 | **CtrlFlow:** 58.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 98
- **Risk Profile:** Cognitive Load (46.1497%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `host_gui_blit` (Impact: 79.5 | O(N^1) | DB: 98)
  * `host_gui_filled_box` (Impact: 46.5 | O(N^1) | DB: 30)
  * `host_gui_flush` (Impact: 15.4 | O(N^1) | DB: 13)
  * `host_gui_box` (Impact: 12.9 | O(N^1) | DB: 11)
  * `host_gui_init` (Impact: 4.4 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 88`, `structural_boundaries: 63`, `args: 15`, `func_start: 16`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 23`, `state_mutation: 577`
* *Architecture:* `import: 4`
* *Defense:* `doc: 74`, `immutability_locks: 7`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` iostream, stdint.h, memory, SDL.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/gui_fb.c` (C | Tier 1.5 | 🚨 AI THREAT: 99.39%)
- **Global Archetype:** `file_cluster_13` (Drift: 14.237 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 6.088 IQR)
- **Top Global Matches:** file_cluster_13: 14.237, file_cluster_8: 14.457, file_cluster_11: 14.653
- **Magnitude:** 663.92 | **LOC:** 1064 | **CtrlFlow:** 70.6% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^6) | **DB Complexity:** 40
- **Risk Profile:** Cognitive Load (68.408%), Tech Debt (81.3356%)
**Top Internal Functions/Classes:**
  * `host_gui_init` (Impact: 71.2 | O(N^3) | DB: 40)
  * `blit_colorblend` (Impact: 29.8 | O(N^6) | DB: 26)
    * *Intent:* /* set global clipping rectangle */
  * `blit_colormod` (Impact: 29.7 | O(N^6) | DB: 23)
  * `blit_blend` (Impact: 29.6 | O(N^6) | DB: 22)
  * `host_gui_blit` (Impact: 24.9 | O(N^2) | DB: 5)
    * *Intent:* /* allocate drawable for passed data and return a handle to it */
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 60`, `structural_boundaries: 25`, `args: 4`, `func_start: 11`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 376`, `fragile_debt: 2`, `orphaned_logic: 5`
* *Architecture:* `io: 4`, `api: 70`, `import: 17`
* *Defense:* `immutability_locks: 14`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` stdlib.h, ioctl.h, termios.h, errno.h, kd.h, unistd.h, fb.h, inttypes.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_windows.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 13.442 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.419 IQR)
- **Top Global Matches:** file_cluster_13: 13.442, file_cluster_8: 13.444, file_cluster_11: 13.823
- **Magnitude:** 416.18 | **LOC:** 400 | **CtrlFlow:** 45.9% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 28
- **Risk Profile:** Cognitive Load (81.5331%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk_directory` (Impact: 33.4 | O(2^N) | DB: 17)
  * `pii_mprotect` (Impact: 22.9 | O(N^1) | DB: 3)
  * `pii_munmap` (Impact: 18.8 | O(N^1))
  * `pii_dirlist` (Impact: 17.8 | O(N^1) | DB: 28)
  * `pii_open` (Impact: 17.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 67`, `structural_boundaries: 79`, `args: 39`, `func_start: 21`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 244`
* *Architecture:* `import: 15`
* *Defense:* `immutability_locks: 12`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` direct.h, thread, conio.h, fcntl.h, stat.h, time.h, types.h, io.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_darwin.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.971 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.708 IQR)
- **Top Global Matches:** file_cluster_13: 12.971, file_cluster_8: 12.976, file_cluster_11: 13.403
- **Magnitude:** 318.4 | **LOC:** 359 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (79.7918%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk_directory` (Impact: 36.8 | O(2^N) | DB: 8)
  * `pii_open` (Impact: 17.2 | O(N^1) | DB: 3)
  * `pii_open_shared` (Impact: 13.0 | O(N^1) | DB: 5)
  * `pii_mprotect` (Impact: 12.7 | O(N^1))
  * `pii_dirlist` (Impact: 11.1 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 76`, `args: 27`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 168`
* *Architecture:* `import: 14`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirent.h, time.h, unistd.h, thread, fcntl.h, stat.h, types.h, iostream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/pii_linux.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.969 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.727 IQR)
- **Top Global Matches:** file_cluster_8: 12.969, file_cluster_13: 12.981, file_cluster_11: 13.4
- **Magnitude:** 318.38 | **LOC:** 358 | **CtrlFlow:** 42.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(2^N) [Recursive] | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (79.8658%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `walk_directory` (Impact: 36.8 | O(2^N) | DB: 8)
  * `pii_open` (Impact: 17.2 | O(N^1) | DB: 3)
  * `pii_open_shared` (Impact: 13.0 | O(N^1) | DB: 5)
  * `pii_mprotect` (Impact: 12.7 | O(N^1))
  * `pii_dirlist` (Impact: 11.1 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 56`, `structural_boundaries: 76`, `args: 27`, `func_start: 20`, `class_start: 4`
* *Risk/State:* `safety_bypasses: 27`, `high_risk_execution: 4`, `state_mutation: 168`
* *Architecture:* `import: 13`
* *Defense:* `immutability_locks: 12`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` dirent.h, time.h, unistd.h, thread, fcntl.h, stat.h, types.h, iostream...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `funcs.ps1` (POWERSHELL | Tier 2 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_15` (Drift: 14.023 IQR)
- **Top Global Matches:** file_cluster_15: 14.023, file_cluster_11: 14.214, file_cluster_8: 14.324
- **Magnitude:** 308.02 | **LOC:** 112 | **CtrlFlow:** 67.3% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N^4) | **DB Complexity:** 23
- **Risk Profile:** Cognitive Load (85.1953%), Tech Debt (98.2197%)
**Top Internal Functions/Classes:**
  * `boot_cpu_gui` (Impact: 46.0 | O(N^4) | DB: 5)
  * `boot_cpu_tui` (Impact: 46.0 | O(N^4) | DB: 5)
  * `add_link` (Impact: 21.5 | O(N^2) | DB: 4)
  * `main` (Impact: 13.6 | O(N^3) | DB: 23)
  * `zero_pad` (Impact: 7.2 | O(N^1) | DB: 3)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 37`, `structural_boundaries: 18`, `args: 5`, `func_start: 6`
* *Risk/State:* `state_mutation: 142`, `orphaned_logic: 5`
* *Architecture:* `io: 3`, `api: 26`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $NHROOT\stop.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `Makefile` (MAKEFILE | Tier 2 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 8.322 IQR)
- **Top Global Matches:** file_cluster_8: 8.322, file_cluster_17: 8.946, file_cluster_12: 9.124
- **Magnitude:** 296.96 | **LOC:** 120 | **CtrlFlow:** 41.8% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (35.3571%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 23`, `structural_boundaries: 32`, `func_start: 8`
* *Risk/State:* `state_mutation: 3`
* *Architecture:* `io: 5`, `api: 3`, `import: 1`
* *Defense:* `cleanup: 4`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $(OBJ_FILES:.o=.d)
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/vp64.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.48%)
- **Global Archetype:** `file_cluster_12` (Drift: 13.218 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.414 IQR)
- **Top Global Matches:** file_cluster_12: 13.218, file_cluster_8: 13.308, file_cluster_13: 13.666
- **Magnitude:** 289.02 | **LOC:** 490 | **CtrlFlow:** 96.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 16
- **Risk Profile:** Cognitive Load (99.9943%), Tech Debt (10.5324%)
**Top Internal Functions/Classes:**
  * `vp64` (Impact: 6.7 | O(N^1) | DB: 16)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 170`, `structural_boundaries: 7`, `func_start: 1`, `class_start: 2`
* *Risk/State:* `state_mutation: 274`, `orphaned_logic: 1`
* *Architecture:* `import: 7`
* *Defense:* `safety: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` cmath, atomic, intrin.h, types.h, iostream, pii.h, immintrin.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/list/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 99.17%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.824 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.603 IQR)
- **Top Global Matches:** file_cluster_8: 11.824, file_cluster_7: 12.436, file_cluster_1: 12.659
- **Magnitude:** 243.56 | **LOC:** 388 | **CtrlFlow:** 72.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (53.045%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`, `structural_boundaries: 3`
* *Risk/State:* `state_mutation: 222`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/lisp/root.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.96%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.134 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.19 IQR)
- **Top Global Matches:** file_cluster_8: 11.134, file_cluster_7: 11.809, file_cluster_1: 12.032
- **Magnitude:** 239.6 | **LOC:** 1430 | **CtrlFlow:** 41.4% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.235%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 165`, `structural_boundaries: 234`, `args: 7`
* *Risk/State:* `high_risk_execution: 1`, `state_mutation: 200`
* *Architecture:* `io: 2`
* *Defense:* `safety: 5`, `immutability_locks: 47`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `funcs.sh` (SHELL | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.128 IQR)
- **Top Global Matches:** file_cluster_8: 12.128, file_cluster_4: 12.613, file_cluster_12: 12.639
- **Magnitude:** 174.36 | **LOC:** 153 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 13
- **Risk Profile:** Cognitive Load (95.1545%), Tech Debt (99.9999%)
**Top Internal Functions/Classes:**
  * `Anonymous_Block` (Impact: 19.3 | O(N^1) | DB: 4)
  * `Anonymous_Block` (Impact: 18.0 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 17.9 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 11.9 | O(N^1) | DB: 3)
  * `Anonymous_Block` (Impact: 10.7 | O(N^1) | DB: 13)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 55`, `args: 22`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 83`, `state_mutation: 74`, `duplicate_logic: 8`
* *Architecture:* `io: 5`, `api: 1`, `concurrency: 3`
* *Defense:* `test: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 26.239
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.027778
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `src/host/main.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.24%)
- **Global Archetype:** `file_cluster_13` (Drift: 12.488 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.693 IQR)
- **Top Global Matches:** file_cluster_13: 12.488, file_cluster_8: 12.545, file_cluster_7: 13.037
- **Magnitude:** 101.28 | **LOC:** 145 | **CtrlFlow:** 45.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 14
- **Risk Profile:** Cognitive Load (68.4643%), Tech Debt (20.7969%)
**Top Internal Functions/Classes:**
  * `main` (Impact: 33.3 | O(N^1) | DB: 14)
    * *Intent:* #endif
  * `enableRawMode` (Impact: 1.8 | O(N^1) | DB: 5)
  * `disableRawMode` (Impact: 1.6 | O(N^1) | DB: 1)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 18`, `structural_boundaries: 22`, `args: 12`, `func_start: 5`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 11`, `state_mutation: 62`, `orphaned_logic: 1`
* *Architecture:* `import: 10`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 1):` termios.h, unistd.h, stdint.h, fcntl.h, string.h, io.h, iostream, stat.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gui/lisp.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.366 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 5.493 IQR)
- **Top Global Matches:** file_cluster_8: 11.366, file_cluster_7: 12.0, file_cluster_1: 12.226
- **Magnitude:** 91.42 | **LOC:** 254 | **CtrlFlow:** 34.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (48.3038%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 16`, `structural_boundaries: 31`, `args: 26`
* *Risk/State:* `state_mutation: 72`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `src/host/audio_sdl.cpp` (CPP | Tier 2 | 🚨 AI THREAT: 99.23%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.61 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 4.202 IQR)
- **Top Global Matches:** file_cluster_8: 10.61, file_cluster_13: 10.746, file_cluster_7: 11.252
- **Magnitude:** 84.66 | **LOC:** 140 | **CtrlFlow:** 44.4% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N^2) | **DB Complexity:** 5
- **Risk Profile:** Cognitive Load (44.0548%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `host_audio_change_sfx` (Impact: 17.9 | O(N^2) | DB: 1)
  * `host_audio_add_sfx` (Impact: 9.8 | O(N^2) | DB: 5)
  * `host_audio_init` (Impact: 8.6 | O(N^2) | DB: 1)
  * `host_audio_deinit` (Impact: 4.8 | O(N^2) | DB: 1)
  * `hasWavExtension` (Impact: 4.2 | O(N^1) | DB: 2)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 20`, `structural_boundaries: 25`, `args: 6`, `func_start: 8`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 28`
* *Architecture:* `import: 7`
* *Defense:* `immutability_locks: 3`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` SDL_rwops.h, SDL_mixer.h, stdint.h, iostream, unordered_map, SDL.h, string
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gui/path/lisp.inc` (CPP | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.926 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.157 IQR)
- **Top Global Matches:** file_cluster_8: 10.926, file_cluster_7: 11.614, file_cluster_1: 11.799
- **Magnitude:** 83.72 | **LOC:** 194 | **CtrlFlow:** 97.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (66.7949%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 42`, `structural_boundaries: 1`
* *Risk/State:* `state_mutation: 64`
* *Architecture:* `io: 1`, `api: 1`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_cube.ps1` (POWERSHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.505 IQR)
- **Top Global Matches:** file_cluster_8: 13.505, file_cluster_15: 13.616, file_cluster_11: 13.916
- **Magnitude:** 82.64 | **LOC:** 37 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (83.5484%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 8`
* *Risk/State:* `state_mutation: 60`
* *Architecture:* `api: 7`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/lisp/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.064 IQR)
- **Top Global Matches:** file_cluster_8: 13.064, file_cluster_7: 13.649, file_cluster_13: 13.742
- **Magnitude:** 75.2 | **LOC:** 62 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 59`, `args: 227`
* *Risk/State:* `state_mutation: 59`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/num/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.622 IQR)
- **Top Global Matches:** file_cluster_8: 12.622, file_cluster_7: 13.241, file_cluster_13: 13.331
- **Magnitude:** 74.34 | **LOC:** 101 | **CtrlFlow:** 1.5% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (58.8607%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 1`, `structural_boundaries: 66`, `args: 187`
* *Risk/State:* `state_mutation: 58`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `apps/science/pcb/router.inc` (CPP | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.523 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.39 IQR)
- **Top Global Matches:** file_cluster_8: 9.523, file_cluster_7: 10.297, file_cluster_1: 10.403
- **Magnitude:** 74.14 | **LOC:** 661 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (10.3114%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 35`
* *Risk/State:* `state_mutation: 45`
* *Architecture:* `io: 53`, `api: 2`
* *Defense:* `immutability_locks: 2`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `gui/textfield/lisp.inc` (CPP | Tier 4 | 🚨 AI THREAT: 99.06%)
- **Global Archetype:** `file_cluster_8` (Drift: 9.947 IQR)
- **Local Micro-Species:** `Cluster 0: Declarative Interfaces & Inert Headers` (Drift: 3.697 IQR)
- **Top Global Matches:** file_cluster_8: 9.947, file_cluster_7: 10.726, file_cluster_1: 10.834
- **Magnitude:** 72.08 | **LOC:** 219 | **CtrlFlow:** 46.7% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (32.189%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 7`, `structural_boundaries: 8`, `args: 2`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* None
* *Defense:* `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/array/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.85%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.613 IQR)
- **Top Global Matches:** file_cluster_8: 11.613, file_cluster_7: 12.308, file_cluster_13: 12.467
- **Magnitude:** 70.96 | **LOC:** 326 | **CtrlFlow:** 33.3% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (69.801%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 31`, `structural_boundaries: 62`, `args: 248`
* *Risk/State:* `state_mutation: 53`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `sys/pii/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.83%)
- **Global Archetype:** `file_cluster_8` (Drift: 11.645 IQR)
- **Top Global Matches:** file_cluster_8: 11.645, file_cluster_7: 12.332, file_cluster_13: 12.456
- **Magnitude:** 70.96 | **LOC:** 118 | **CtrlFlow:** 13.6% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (63.9093%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 9`, `structural_boundaries: 57`, `args: 132`
* *Risk/State:* `state_mutation: 54`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `class/str/class.inc` (CPP | Tier 4 | 🚨 AI THREAT: 98.84%)
- **Global Archetype:** `file_cluster_8` (Drift: 12.848 IQR)
- **Top Global Matches:** file_cluster_8: 12.848, file_cluster_7: 13.441, file_cluster_13: 13.523
- **Magnitude:** 68.14 | **LOC:** 72 | **CtrlFlow:** 0.0% | **Authorship Centralization:** 0.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (0.0%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `structural_boundaries: 104`, `args: 152`
* *Risk/State:* `state_mutation: 52`
* *Architecture:* None
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Producer (Foundation) | `Dependency Blast Radius (PageRank):` 5.38
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.003968
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `apps/media/whiteboard/ui.inc` (CPP | Tier 4 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 10.68 IQR)
- **Local Micro-Species:** `Cluster 2: Inert Headers & Declarative Structures` (Drift: 4.87 IQR)
- **Top Global Matches:** file_cluster_8: 10.68, file_cluster_7: 11.371, file_cluster_1: 11.395
- **Magnitude:** 64.92 | **LOC:** 323 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (24.5711%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 43`
* *Risk/State:* `high_risk_execution: 2`, `state_mutation: 42`
* *Architecture:* `io: 7`, `api: 2`
* *Defense:* `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` None
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `run_mesh.ps1` (POWERSHELL | Tier 2 | 🚨 AI THREAT: 99.29%)
- **Global Archetype:** `file_cluster_8` (Drift: 13.129 IQR)
- **Top Global Matches:** file_cluster_8: 13.129, file_cluster_15: 13.293, file_cluster_11: 13.603
- **Magnitude:** 62.52 | **LOC:** 31 | **CtrlFlow:** 100.0% | **Authorship Centralization:** 100.0%
- **Algorithmic:** O(N) | **DB Complexity:** 0
- **Risk Profile:** Cognitive Load (84.4527%), Tech Debt (0.0%)
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 6`
* *Risk/State:* `state_mutation: 42`
* *Architecture:* `api: 5`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Isolated/Orphan | `Dependency Blast Radius (PageRank):` 3.775
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 0):` $PSScriptRoot\funcs.ps1
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

## 13. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** Pay close attention to 'Anti-Pattern' files. These files blend in globally (Low Global Drift), but heavily violate the standard conventions of their native programming language (High Local Drift). 'Mixed-Responsibility' files sit perfectly between two global archetypes (Delta <= 0.9 IQR), indicating a violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_12
- `src/host/vp64.cpp` (CPP) | Magnitude: 289.02 | Delta: **0.09 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 274, indent_tabs: 229, macros: 172, branch: 170

### Mixed-Responsibility Refactoring Targets for: file_cluster_13
- `src/host/pii_windows.cpp` (CPP) | Magnitude: 416.18 | Delta: **0.002 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 244, indent_tabs: 228, structural_boundaries: 79, branch: 67
- `src/host/pii_darwin.cpp` (CPP) | Magnitude: 318.4 | Delta: **0.005 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 201, state_mutation: 168, structural_boundaries: 76, pointers: 62
- `src/host/main.cpp` (CPP) | Magnitude: 101.28 | Delta: **0.057 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: indent_tabs: 75, state_mutation: 62, pointers: 24, structural_boundaries: 22
- `src/host/gui_fb.c` (C) | Magnitude: 663.92 | Delta: **0.22 IQR** | Secondary Pull: `file_cluster_8`
  * Top Architectural Signatures: state_mutation: 376, indent_spaces: 250, pointers: 193, api: 70

### Mixed-Responsibility Refactoring Targets for: file_cluster_15
- `stop.ps1` (POWERSHELL) | Magnitude: 18.64 | Delta: **0.157 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: branch: 9, globals: 6, safety_bypasses: 4, state_mutation: 3
- `funcs.ps1` (POWERSHELL) | Magnitude: 308.02 | Delta: **0.191 IQR** | Secondary Pull: `file_cluster_11`
  * Top Architectural Signatures: state_mutation: 142, indent_spaces: 77, branch: 37, closures: 36

### Mixed-Responsibility Refactoring Targets for: file_cluster_8
- `src/host/pii_linux.cpp` (CPP) | Magnitude: 318.38 | Delta: **0.012 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 201, state_mutation: 168, structural_boundaries: 76, pointers: 62
- `run_star.sh` (SHELL) | Magnitude: 15.7 | Delta: **0.085 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_tabs: 9, branch: 6, state_mutation: 6, safety_bypasses: 5
- `run_cube.ps1` (POWERSHELL) | Magnitude: 82.64 | Delta: **0.111 IQR** | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: state_mutation: 60, indent_spaces: 27, branch: 8, api: 7
- `src/host/gui_raw.cpp` (CPP) | Magnitude: 764.48 | Delta: **0.118 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: state_mutation: 577, indent_tabs: 336, pointers: 124, branch: 88
- `src/host/audio_sdl.cpp` (CPP) | Magnitude: 84.66 | Delta: **0.136 IQR** | Secondary Pull: `file_cluster_13`
  * Top Architectural Signatures: indent_spaces: 75, state_mutation: 28, structural_boundaries: 25, branch: 20

## 13.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

### 👤 Key Person Dependencies (High Impact + Siloed Knowledge)
These are massive, load-bearing files written almost entirely by a single developer. They represent severe 'Bus Factor' risk.

- `src/host/gui_raw.cpp` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 764.48
- `src/host/gui_fb.c` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 663.92
- `funcs.ps1` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 308.02
- `Makefile` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 296.96
- `class/lisp/root.inc` -> **Chris Hinsley** (100.0% isolated ownership) | Magnitude: 239.6

## 13.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `funcs.sh` -> **Severity: 2.778** (Embedded: 0.0278 * Error Risk: 99.9955%)
- `class/str/class.inc` -> **Severity: 0.342** (Embedded: 0.004 * Error Risk: 86.1901%)
- `sys/mem/class.inc` -> **Severity: 0.295** (Embedded: 0.004 * Error Risk: 74.2466%)
- `src/host/pii.h` -> **Severity: 0.105** (Embedded: 0.0198 * Error Risk: 5.2797%)
- `src/host/sdl_dummy.h` -> **Severity: 0.033** (Embedded: 0.004 * Error Risk: 8.2906%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `sys/mem/class.inc` -> **Severity: 497.69** (Blast Radius: 5.38 * Doc Risk: 92.5074%)
- `funcs.ps1` -> **Severity: 377.5** (Blast Radius: 3.775 * Doc Risk: 100.0%)
- `class/fixeds/class.inc` -> **Severity: 377.5** (Blast Radius: 3.775 * Doc Risk: 100.0%)
- `class/reals/class.inc` -> **Severity: 377.5** (Blast Radius: 3.775 * Doc Risk: 100.0%)
- `class/sym/class.inc` -> **Severity: 377.5** (Blast Radius: 3.775 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Act as a Principal Staff Engineer. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility). DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective, practical, and direct.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
