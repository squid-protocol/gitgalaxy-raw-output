# ARCHITECTURAL_BRIEF: normal_esp32_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/espressif/esp32-doom.git` |
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
| Total Artifacts | 203 |
| Analyzed Artifacts (Scanned) | 186 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 17 |
| Total LOC | 48192 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 91.6% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3339 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.0875 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 1.1% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.1374 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 13 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 169 | 47503 | 90.9% |
| MAKEFILE | 9 | 36 | 4.8% |
| CPP | 4 | 648 | 2.2% |
| PLAINTEXT | 2 | 0 | 1.1% |
| SHELL | 1 | 2 | 0.5% |
| CSV | 1 | 3 | 0.5% |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Cluster 3`
> **Architectural Drift Z-Score:** `2.272`
> **Composition Archetype:** `Hub-Coupled App` (z -0.21; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 41%, Large Core Modules 20%, Data / Markup / Trivial 15%, Compute Cores Files 10%, Interface Declarations Files 8%
> **⚠️ UNIQUE INTERPRETATION:** This repository has a high Z-Score. While it maps closest to this archetype, its internal structure is a highly unique or hybrid interpretation of the pattern.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 184 | 98.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 17*

**Composition by Extension & Reason:**
- `.c`: 1x Excluded (Embedded Hex Payload: 40960 hex tokens in 3418 LOC), 1x Excluded (Embedded Hex Payload: 16384 hex tokens in 1370 LOC), 1x Excluded (Embedded Hex Payload: 8196 hex tokens in 687 LOC)
- `.dat`: 4x Excluded (Unsupported Extension: '.dat')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 298 LOC)
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1501 LOC), 1x Excluded (Machine-Generated Source Code Signature: 120 LOC)
- `.projbuild`: 1x Excluded (Unsupported Extension: '.projbuild')
- `.disabled`: 1x Excluded (Unsupported Extension: '.disabled')
- `.wad`: 1x Excluded (Unsupported Extension: '.wad')
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 99.2 | 27.8 | 3.7 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 99.9 | 43.0 | 24.3 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 24.9 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.4 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 32.4 | 7.5 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 41.4 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 52.6 | 3.0 | 0.0 | 0.0 |
| Spec Alignment (formerly Specification Exposure) | 0.0 | 100.0 | 65.2 | 100.0 | 100.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) | 0.0 | 100.0 | 44.9 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 12928 | 137 | 208 | `components/prboom/p_enemy.c` |
| cleanup | 82 | 22 | 1 | `components/prboom/mmus2mid.c` |
| guards | 2498 | 123 | 30 | `components/prboom/d_deh.c` |
| danger | 356 | 46 | 5 | `components/prboom/r_fps.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 2618 | 158 | 24 | `components/prboom/include/d_deh.h` |
| io | 53 | 9 | 0 | `components/prboom/d_deh.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 2 | 0 | `components/prboom/d_client.c` |
| time | 2 | 1 | 0 | `components/prboom-esp32-compat/i_system.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 146 | 17 | 0 | `components/prboom/m_menu.c` |
| debt | 243 | 50 | 3 | `components/prboom/d_deh.c` |
| mutation | 13921 | 106 | 256 | `components/prboom/g_game.c` |
| dead_code | 775 | 90 | 13 | `components/prboom/p_enemy.c` |
| credential | 0 | 0 | 0 | - |
| threat | 259 | 37 | 3 | `components/prboom/r_drawcolumn.inl` |
| ml_ai | 16 | 7 | 0 | `components/prboom/include/d_englsh.h` |
| ui | 1 | 1 | 0 | `components/prboom/lprintf.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.4806**
- `alloc_cleanup_pairing` (cleanup / (memory + 1)): **0.0**

## 7. ARCHITECTURAL CHOKE POINTS & DEPENDENCIES
### Top I/O Latency Risks
- `components/prboom/d_deh.c` (Hits: 16)
- `components/prboom/m_misc.c` (Hits: 11)
- `components/prboom/g_game.c` (Hits: 8)

### Top 5 Structural Pillars (Highest 'Imported By' / Blast Radius)
These are the most interconnected files relative to the rest of this repository. On a repo with dense internal coupling, that means core load-bearing infrastructure -- changes carry real cascading-break risk. On a repo with a flatter internal architecture, the gap between #1 and #5 may be small, and this list is a weaker signal accordingly; compare the connection counts below before treating it as a verdict.

1. **doomstat.h** (`components/prboom/include/doomstat.h`) — 61 inbound connections
2. **lprintf.h** (`components/prboom/include/lprintf.h`) — 52 inbound connections
3. **r_main.h** (`components/prboom/include/r_main.h`) — 41 inbound connections
4. **config.h** (`components/prboom/include/config.h`) — 35 inbound connections
5. **w_wad.h** (`components/prboom/include/w_wad.h`) — 33 inbound connections

### Top 5 Orchestrators (Highest 'Imports' / Fragility Index)
These files pull in the most external dependencies. They are highly coupled and fragile to API changes.

1. **g_game.c** (`components/prboom/g_game.c`) — 41 outbound dependencies
2. **d_main.c** (`components/prboom/d_main.c`) — 38 outbound dependencies
3. **m_misc.c** (`components/prboom/m_misc.c`) — 29 outbound dependencies
4. **i_system.c** (`components/prboom-esp32-compat/i_system.c`) — 26 outbound dependencies
5. **gl_main.c** (`components/prboom/gl_main.c`) — 26 outbound dependencies

## 8. CORE FUNCTION HITLIST (Heaviest Functions)
> *Note: The 'Impact' metric below represents Structural Magnitude (complexity, arguments, and length), NOT operational risk. These are the load-bearing pillars of the logic.*

- `P_CrossSpecialLine` **(Many-Argument Workhorses)** (@ `components/prboom/p_spec.c`) -> Impact: **658.0** | LOC: 881
  * *Intent:* ///////////////////////////////////////////////////////////////////////// // // P_CrossSpecialLine - Walkover Trigger Dispatcher // // Called every ti...
- `P_UseSpecialLine` **(Many-Argument Workhorses)** (@ `components/prboom/p_switch.c`) -> Impact: **648.0** | LOC: 920
  * *Intent:* // // P_UseSpecialLine // // // Called when a thing uses (pushes) a special line. // Only the front sides of lines are usable. // Dispatches to the ap...
- `M_Responder` **(Compute Cores)** (@ `components/prboom/m_menu.c`) -> Impact: **470.2** | LOC: 1088
  * *Intent:* ///////////////////////////////////////////////////////////////////////////// // // M_Responder // // Examines incoming keystrokes and button pushes a...
- `P_TouchSpecialThing` **(Compute Cores)** (@ `components/prboom/p_inter.c`) -> Impact: **182.2** | LOC: 318
  * *Intent:* // // P_TouchSpecialThing //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `components/prboom/r_segs.c`) -> Impact: **169.7** | LOC: 380
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `HU_Drawer` **(Compute Cores)** (@ `components/prboom/hu_stuff.c`) -> Impact: **157.1** | LOC: 541
  * *Intent:* // // HU_Drawer() // // Draw all the pieces of the heads-up display // // Passed nothing, returns nothing //
- `V_DrawMemPatch` **(Many-Argument Workhorses)** (@ `components/prboom/v_video.c`) -> Impact: **156.9** | LOC: 227
  * *Intent:* // // V_DrawMemPatch // // CPhipps - unifying patch drawing routine, handles all cases and combinations // of stretching, flipping and translating // ...
- `mmus2mid` **(Many-Argument Workhorses)** (@ `components/prboom/mmus2mid.c`) -> Impact: **145.4** | LOC: 224
  * *Intent:* // // mmus2mid() // // Convert a memory buffer contain MUS data to an Allegro MIDI structure // with specified time division and compression. // // Pa...
- `D_DoomMainSetup` **(Compute Cores)** (@ `components/prboom/d_main.c`) -> Impact: **144.6** | LOC: 492
  * *Intent:* // // D_DoomMainSetup // // CPhipps - the old contents of D_DoomMain, but moved out of the main // line of execution so its stack space can be freed
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `components/prboom/p_inter.c`) -> Impact: **138.1** | LOC: 169
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...

*Function archetypes referenced above:*
  * **Compute Cores**: dense algorithmic logic (high decision density per line)
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `components/prboom` | 77 | 43936.3 | 56.67% | 39.83% |
| `components/prboom/include` | 77 | 2829.74 | 2.85% | 4.15% |
| `components/prboom-esp32-compat` | 10 | 915.7 | 37.13% | 58.13% |
| `components/prboom/native` | 7 | 399.02 | 22.54% | 78.72% |
| `components/prboom-wad-tables/include` | 4 | 52.16 | 0.0% | 0.0% |
| `components/prboom-esp32-compat/include` | 3 | 43.76 | 0.0% | 0.0% |
| `main` | 3 | 32.22 | 2.67% | 20.75% |
| `__monolith__` | 3 | 23.74 | 0.0% | 0.0% |
| `components/prboom-wad-tables` | 1 | 10.52 | 0.0% | 0.0% |
| `components/prboom/native/include/rom` | 1 | 10.52 | 0.0% | 0.0% |

## 10. TARGETED STRUCTURAL SURFACE VECTORS (formerly Risk Vectors, Top 5 by Surface)
### Highest Debt Markers (formerly Tech Debt; Fragile/Planned)
- `components/prboom-esp32-compat/i_network.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_sound.c` -> **100.0%** Exposure
- `components/prboom/native/i_network.c` -> **100.0%** Exposure
- `components/prboom/native/i_sound.c` -> **100.0%** Exposure
- `components/prboom/native/i_system.c` -> **100.0%** Exposure
### Highest Mutation Surface (formerly State Flux; Mutation/Volatility)
- `components/prboom-esp32-compat/gamepad.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_main.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_system.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/i_video.c` -> **100.0%** Exposure
- `components/prboom-esp32-compat/psxcontroller.c` -> **100.0%** Exposure
### Highest Design Slop (Dead & Duplicated Logic)
- `components/prboom/p_enemy.c` -> **60** Orphaned Functions | **0** Duplicates
- `components/prboom/p_pspr.c` -> **24** Orphaned Functions | **0** Duplicates
- `components/prboom/p_spec.c` -> **22** Orphaned Functions | **0** Duplicates
- `components/prboom-esp32-compat/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates
- `components/prboom/native/i_sound.c` -> **19** Orphaned Functions | **0** Duplicates

## 10.5 AI THREAT INTELLIGENCE (XGBoost)
*No files met the threshold for malicious structural signatures.*

## 10.6 WEAPONIZABLE SURFACE EXPOSURES (RULE-BASED SAST)
> Secondary Evidence: The following files tripped specific static threat signatures. Use these to explain *why* the XGBoost model flagged the files above.

*No critical vulnerabilities or security lens thresholds breached.*

## 10.7 ECOSYSTEM SECURITY AUDITS
> **AI CONTEXT:** High-level perimeter defense metrics from the X-Ray, Supply Chain Firewall, and API Network Mapper.

### ☢️ X-Ray & 🧱 Supply Chain Firewall
- **Binary Anomalies (X-Ray):** `0` (High entropy, packed payloads, or magic byte mismatches).
- **Blacklisted Dependencies:** `0` explicitly banned packages imported.
- **Unknown Dependencies:** `1117` packages imported that bypass the Zero-Trust whitelist.

## 11. CUMULATIVE RISK HITLIST (Top 10 Highest Risk Files)
> Cumulative Risk is the sum of all individual risk exposures. These files represent the highest multi-dimensional technical debt and architectural fragility.

### 1. `components/prboom/p_enemy.c` (C) -> Cumulative Risk: **683.28**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.03)
- **Magnitude:** 2131.44 | **LOC:** 2602 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (97.4349%)
- **Heaviest Functions:** `A_Chase` (Compute Cores, Impact: 86.8), `A_BossDeath` (Compute Cores, Impact: 80.0), `P_DoNewChaseDir` (Compute Cores, Impact: 68.7)

### 2. `components/prboom/st_lib.c` (C) -> Cumulative Risk: **677.14**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Many-Argument Workhorses Files` (z +1.14)
- **Magnitude:** 197.82 | **LOC:** 375 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.1491%)
- **Heaviest Functions:** `STlib_drawNum` (Many-Argument Workhorses, Impact: 45.7), `STlib_updateMultIcon` (Compute Cores, Impact: 13.6), `STlib_updateBinIcon` (Compute Cores, Impact: 13.6)

### 3. `components/prboom/r_bsp.c` (C) -> Cumulative Risk: **662.08**
- **Archetype:** `file_cluster_4` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.36)
- **Magnitude:** 555.7 | **LOC:** 673 | **CtrlFlow:** 30.6% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.6291%)
- **Heaviest Functions:** `R_FakeFlat` (Many-Argument Workhorses, Impact: 65.7), `R_Subsector` (Compute Cores, Impact: 60.9), `R_AddLine` (Compute Cores, Impact: 29.8)

### 4. `components/prboom/p_tick.c` (C) -> Cumulative Risk: **660.44**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +1.23)
- **Magnitude:** 133.3 | **LOC:** 292 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (99.9642%)
- **Heaviest Functions:** `P_UpdateThinker` (Compute Cores, Impact: 12.7), `P_Ticker` (I/O & Config Routines, Impact: 10.6), `P_NextThinker` (Compute Cores, Impact: 7.3)

### 5. `components/prboom/p_pspr.c` (C) -> Cumulative Risk: **657.81**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.70)
- **Magnitude:** 576.08 | **LOC:** 830 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (96.2728%)
- **Heaviest Functions:** `P_SwitchWeapon` (Compute Cores, Impact: 52.3), `P_WeaponPreferred` (Compute Cores, Impact: 28.4), `A_WeaponReady` (Compute Cores, Impact: 23.0)

### 6. `components/prboom/w_wad.c` (C) -> Cumulative Risk: **653.04**
- **Archetype:** `file_cluster_10` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.05)
- **Magnitude:** 331.98 | **LOC:** 486 | **CtrlFlow:** 21.7% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (98.8402%)
- **Heaviest Functions:** `W_AddFile` (Compute Cores, Impact: 24.0), `W_CoalesceMarkedResource` (Many-Argument Workhorses, Impact: 22.6), `ExtractFileBase` (Compute Cores, Impact: 15.2)

### 7. `components/prboom/p_mobj.c` (C) -> Cumulative Risk: **647.68**
- **Archetype:** `file_cluster_11` (Distance: N/A IQR)
- **Composition Archetype:** `Compute Cores Files` (z +1.61)
- **Magnitude:** 1302.54 | **LOC:** 1533 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.1529%)
- **Heaviest Functions:** `P_XYMovement` (Compute Cores, Impact: 122.5), `P_ZMovement` (Compute Cores, Impact: 116.8), `P_SpawnMapThing` (Compute Cores, Impact: 92.0)

### 8. `components/prboom/r_plane.c` (C) -> Cumulative Risk: **643.91**
- **Archetype:** `file_cluster_5` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.00)
- **Magnitude:** 461.4 | **LOC:** 471 | **CtrlFlow:** 23.1% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.8685%)
- **Heaviest Functions:** `R_MapPlane` (Many-Argument Workhorses, Impact: 32.0), `R_DoDrawPlane` (Compute Cores, Impact: 28.4), `R_MakeSpans` (Many-Argument Workhorses, Impact: 24.5)

### 9. `components/prboom-esp32-compat/i_system.c` (C) -> Cumulative Risk: **643.3**
- **Archetype:** `file_cluster_14` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z -0.10)
- **Magnitude:** 221.86 | **LOC:** 344 | **CtrlFlow:** 13.4% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Tech Debt (98.8258%)
- **Heaviest Functions:** `I_Mmap` (Many-Argument Workhorses, Impact: 17.5), `I_Lseek` (Compute Cores, Impact: 12.5), `I_Munmap` (Defensive Guards, Impact: 9.3)

### 10. `components/prboom/r_data.c` (C) -> Cumulative Risk: **639.9**
- **Archetype:** `file_cluster_8` (Distance: N/A IQR)
- **Composition Archetype:** `Large Core Modules` (z +0.22)
- **Magnitude:** 555.62 | **LOC:** 747 | **CtrlFlow:** 18.5% | **Authorship Centralization:** 0.0%
- **Primary Risk Drivers:** State Flux (100.0%), Spec Match (100.0%), Documentation (100.0%), Safety Score (99.4548%)
- **Heaviest Functions:** `R_InitTranMap` (Compute Cores, Impact: 34.9), `R_InitTextures` (I/O & Config Routines, Impact: 33.6), `R_PrecacheLevel` (I/O & Config Routines, Impact: 21.8)

## 12. SCANNED ARTIFACTS HITLIST (Top 25 Heaviest Files)
> *Note: 'Magnitude' represents the file's total Structural Magnitude and impact within the system. It is independent of its Risk Profile. High magnitude implies high structural importance and centralization.*

### `components/prboom/p_spec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2826.24 | **LOC:** 3354 | **CtrlFlow:** 39.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (43.8325%), Tech Debt (0.0%)
**Top Internal Functions/Classes:**
  * `P_CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 658.0)
    * *Intent:* ///////////////////////////////////////////////////////////////////////// // // P_CrossSpecialLine -...
  * `P_ShootSpecialLine` **(Compute Cores)** (Impact: 136.8)
    * *Intent:* // // P_ShootSpecialLine - Gun trigger special dispatcher // // Called when a thing shoots a special...
  * `P_CanUnlockGenDoor` **(Compute Cores)** (Impact: 100.4)
    * *Intent:* // // P_CanUnlockGenDoor() // // Passed a generalized locked door linedef and a player, returns whet...
  * `P_CheckTag` **(Compute Cores)** (Impact: 78.4)
    * *Intent:* // // P_CheckTag() // // Passed a line, returns true if the tag is non-zero or the line special // a...
  * `P_PlayerInSpecialSector` **(Compute Cores)** (Impact: 56.3)
    * *Intent:* // // P_PlayerInSpecialSector() // // Called every tick frame // that the player origin is in a spec...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 400 instances
* *State Mutation (weighted view):* 1218
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 803`, `structural_boundaries: 359`, `args: 56`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 418`, `dead_code: 8`, `fragile_debt: 3`, `unreferenced_by_name: 22`
* *Architecture:* `api: 36`, `import: 19`
* *Defense:* `safety: 2`, `doc: 18`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` d_deh.h, d_englsh.h, doomstat.h, g_game.h, lprintf.h, m_argv.h, m_bbox.h, m_random.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2812.08 | **LOC:** 5565 | **CtrlFlow:** 17.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.1121%), Tech Debt (12.3501%)
**Top Internal Functions/Classes:**
  * `M_Responder` **(Compute Cores)** (Impact: 470.2)
    * *Intent:* ///////////////////////////////////////////////////////////////////////////// // // M_Responder // /...
  * `M_GetKeyString` **(Compute Cores)** (Impact: 80.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////// // // Dynamic HELP scre...
  * `M_DrawSetting` **(Compute Cores)** (Impact: 59.4)
    * *Intent:* ///////////////////////////// // // phares 4/18/98: // Consolidate Item Setting drawing code // // M...
  * `M_DrawInstructions` **(Compute Cores)** (Impact: 24.8)
    * *Intent:* ///////////////////////////// // // phares 4/18/98: // M_DrawInstructions writes the instruction tex...
  * `M_DrawScreenItems` **(Compute Cores)** (Impact: 17.2)
    * *Intent:* ///////////////////////////// // // M_DrawScreenItems takes the data for each menu item and gives it...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 451 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 622`, `structural_boundaries: 641`, `args: 258`, `func_start: 109`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `state_mutation: 541`, `dead_code: 12`, `fragile_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 180`, `import: 24`
* *Defense:* `safety: 2`, `doc: 61`, `immutability_locks: 31`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 22):` am_map.h, d_deh.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, fcntl.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 2732.06 | **LOC:** 2923 | **CtrlFlow:** 25.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.4497%), Tech Debt (33.3215%)
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Compute Cores)** (Impact: 111.3)
  * `G_ReadDemoHeader` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `G_Ticker` **(Compute Cores)** (Impact: 75.0)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_Responder` **(Compute Cores)** (Impact: 60.7)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_CheckSpot` **(Compute Cores)** (Impact: 48.2)
    * *Intent:* // // G_CheckSpot // Returns false if the player cannot be respawned // at the given mapthing_t spot...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 553 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1794
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 507`, `structural_boundaries: 240`, `args: 65`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 688`, `dead_code: 13`, `fragile_debt: 7`, `unreferenced_by_name: 13`
* *Architecture:* `io: 8`, `api: 37`, `import: 43`
* *Defense:* `safety: 17`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 35):` am_map.h, config.h, d_deh.h, d_main.h, d_net.h, doomstat.h, dstrings.h, f_finale.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 2131.44 | **LOC:** 2602 | **CtrlFlow:** 32.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (94.8709%), Tech Debt (97.4349%)
**Top Internal Functions/Classes:**
  * `A_Chase` **(Compute Cores)** (Impact: 86.8)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_BossDeath` **(Compute Cores)** (Impact: 80.0)
    * *Intent:* // // A_BossDeath // Possibly trigger special effects // if on first boss level //
  * `P_DoNewChaseDir` **(Compute Cores)** (Impact: 68.7)
    * *Intent:* // // P_DoNewChaseDir // // killough 9/8/98: // // Most of P_NewChaseDir(), except for what // deter...
  * `P_IsOnLift` **(Compute Cores)** (Impact: 57.9)
    * *Intent:* /* * P_IsOnLift * * killough 9/9/98: * * Returns true if the object is on a lift. Used for AI, * sin...
  * `P_Move` **(Compute Cores)** (Impact: 48.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 304 instances
* *State Mutation (weighted view):* 970
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 546`, `structural_boundaries: 303`, `args: 99`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 362`, `dead_code: 7`, `fragile_debt: 5`, `unreferenced_by_name: 60`
* *Architecture:* `api: 70`, `import: 15`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` doomstat.h, g_game.h, lprintf.h, m_bbox.h, m_random.h, p_enemy.h, p_inter.h, p_map.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1812.54 | **LOC:** 2336 | **CtrlFlow:** 29.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (78.448%), Tech Debt (44.2087%)
**Top Internal Functions/Classes:**
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* // // P_TryMove // Attempt to move to a new position, // crossing special lines unless MF_TELEPORT i...
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 66.7)
    * *Intent:* // // PIT_CheckThing //
  * `P_HitSlideLine` **(Compute Cores)** (Impact: 40.7)
    * *Intent:* // // P_HitSlideLine // Adjusts the xmove / ymove // so that the next move will slide along the wall...
  * `P_GetMoveFactor` **(Compute Cores)** (Impact: 39.9)
    * *Intent:* /* phares 3/19/98 * P_GetMoveFactor() returns the value by which the x,y * movements are multiplied ...
  * `PIT_CheckLine` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* // // PIT_CheckLine // Adjusts tmfloorz and tmceilingz as lines are contacted //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 995
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 376`, `structural_boundaries: 216`, `args: 43`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 379`, `dead_code: 6`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 36`, `import: 14`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` doomstat.h, lprintf.h, m_bbox.h, m_random.h, p_inter.h, p_map.h, p_maputl.h, p_mobj.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_deh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_17` (Drift: 0.0 IQR)
- **Magnitude:** 1784.44 | **LOC:** 3096 | **CtrlFlow:** 21.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (46.3741%), Tech Debt (14.6163%)
**Top Internal Functions/Classes:**
  * `deh_procMisc` **(Many-Argument Workhorses)** (Impact: 102.0)
    * *Intent:* // ==================================================================== // deh_procMisc // Purpose: ...
  * `deh_procText` **(Many-Argument Workhorses)** (Impact: 76.3)
    * *Intent:* // ==================================================================== // deh_procText // Purpose: ...
  * `deh_procFrame` **(Many-Argument Workhorses)** (Impact: 73.5)
    * *Intent:* // ==================================================================== // deh_procFrame // Purpose:...
  * `deh_procSounds` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* // ==================================================================== // deh_procSounds // Purpose...
  * `ProcessDehFile` **(Many-Argument Workhorses)** (Impact: 66.2)
    * *Intent:* // ==================================================================== // ProcessDehFile // Purpose...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 195 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 588
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 499`, `structural_boundaries: 195`, `args: 67`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 198`, `dead_code: 8`, `fragile_debt: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 16`, `api: 19`, `import: 15`
* *Defense:* `safety: 27`, `immutability_locks: 342`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 13):` ctype.h, d_deh.h, d_think.h, doomdef.h, doomstat.h, doomtype.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1444.94 | **LOC:** 1689 | **CtrlFlow:** 21.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.5209%), Tech Debt (18.2853%)
**Top Internal Functions/Classes:**
  * `P_CreateBlockMap` **(Compute Cores)** (Impact: 79.9)
    * *Intent:* // // Actually construct the blockmap lump from the level data // // This finds the intersection of ...
  * `P_SetupLevel` **(Many-Argument Workhorses)** (Impact: 67.0)
    * *Intent:* // // P_SetupLevel // // killough 5/3/98: reformatted, cleaned up
  * `P_LoadLineDefs` **(Compute Cores)** (Impact: 28.8)
    * *Intent:* // // P_LoadLineDefs // Also counts secret lines for intermissions. // ^^^ // ??? killough ??? // Do...
  * `P_GroupLines` **(I/O & Config Routines)** (Impact: 23.9)
    * *Intent:* // modified to return totallines (needed by P_LoadReject)
  * `P_LoadSideDefs2` **(Compute Cores)** (Impact: 21.4)
    * *Intent:* // killough 4/4/98: delay using texture names until // after linedefs are loaded, to allow overloadi...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 313 instances
* *Memory Alloc (weighted view):* 6
* *State Mutation (weighted view):* 1015
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 220`, `structural_boundaries: 62`, `args: 46`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 389`, `dead_code: 8`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 20`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 40`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 19):` doomstat.h, g_game.h, i_system.h, lprintf.h, m_argv.h, m_bbox.h, math.h, p_enemy.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1406.5 | **LOC:** 1739 | **CtrlFlow:** 29.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.3592%), Tech Debt (25.872%)
**Top Internal Functions/Classes:**
  * `D_DoomMainSetup` **(Compute Cores)** (Impact: 144.6)
    * *Intent:* // // D_DoomMainSetup // // CPhipps - the old contents of D_DoomMain, but moved out of the main // l...
  * `CheckIWAD` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* // // CheckIWAD // // Verify a file is indeed tagged as an IWAD // Scan its lumps for levelnames and...
  * `D_Display` **(Compute Cores)** (Impact: 47.8)
  * `GetFirstMap` **(Compute Cores)** (Impact: 36.4)
    * *Intent:* // // GetFirstMap // // Ty 08/29/98 - determine first available map from the loaded wads and run it ...
  * `IdentifyVersion` **(Compute Cores)** (Impact: 33.3)
    * *Intent:* // supports IWADs with custom names. Also allows the -iwad parameter to // specify which iwad is bei...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 290 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 893
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 334`, `structural_boundaries: 122`, `args: 66`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 313`, `dead_code: 5`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 3`, `api: 16`, `import: 39`
* *Defense:* `safety: 6`, `immutability_locks: 23`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 32):` am_map.h, d_deh.h, d_main.h, d_net.h, direct.h, doomdef.h, doomstat.h, doomtype.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 1314.1 | **LOC:** 1042 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.2887%), Tech Debt (24.974%)
**Top Internal Functions/Classes:**
  * `V_DrawMemPatch` **(Many-Argument Workhorses)** (Impact: 156.9)
    * *Intent:* // // V_DrawMemPatch // // CPhipps - unifying patch drawing routine, handles all cases and combinati...
  * `V_UpdateTrueColorPalette` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* #include "GAMMATBL.h" // // V_UpdateTrueColorPalette //
  * `WRAP_V_DrawLine` **(Compute Cores)** (Impact: 40.2)
    * *Intent:* // // WRAP_V_DrawLine() // // Draw a line in the frame buffer. // Classic Bresenham w/ whatever opti...
  * `FUNC_V_DrawBackground` **(Compute Cores)** (Impact: 37.8)
    * *Intent:* /* * V_DrawBackground tiles a 64x64 patch over the entire screen, providing the * background for the...
  * `FUNC_V_CopyRect` **(Many-Argument Workhorses)** (Impact: 36.7)
    * *Intent:* // // V_CopyRect // // Copies a source rectangle in a screen buffer to a destination // rectangle in...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 254 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 803
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 183`, `structural_boundaries: 90`, `args: 66`, `func_start: 42`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 295`, `unreferenced_by_name: 10`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `immutability_locks: 28`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` GAMMATBL.h, doomdef.h, esp_attr.h, i_video.h, lprintf.h, m_bbox.h, r_draw.h, r_filter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 1302.54 | **LOC:** 1533 | **CtrlFlow:** 36.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5678%), Tech Debt (73.229%)
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 122.5)
    * *Intent:* // // P_XYMovement // // Attempts to move something if it has momentum. //
  * `P_ZMovement` **(Compute Cores)** (Impact: 116.8)
    * *Intent:* // // P_ZMovement // // Attempt vertical movement.
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 92.0)
    * *Intent:* // // P_SpawnMapThing // The fields of the mapthing should // already be in host byte order. //
  * `P_MobjThinker` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* // // P_MobjThinker //
  * `P_SetMobjState` **(Compute Cores)** (Impact: 23.7)
    * *Intent:* #include "st_stuff.h" #include "hu_stuff.h" #include "s_sound.h" #include "info.h" #include "g_game....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 316`, `structural_boundaries: 65`, `args: 23`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 257`, `dead_code: 9`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 16`, `import: 16`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 15):` doomdef.h, doomstat.h, g_game.h, hu_stuff.h, info.h, lprintf.h, m_random.h, p_inter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/hu_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 1259.52 | **LOC:** 1594 | **CtrlFlow:** 25.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.1738%), Tech Debt (12.5899%)
**Top Internal Functions/Classes:**
  * `HU_Drawer` **(Compute Cores)** (Impact: 157.1)
    * *Intent:* // // HU_Drawer() // // Draw all the pieces of the heads-up display // // Passed nothing, returns no...
  * `HU_Responder` **(Compute Cores)** (Impact: 76.5)
    * *Intent:* // // HU_Responder() // // Responds to input events that affect the heads up displays // // Passed t...
  * `HU_Start` **(I/O & Config Routines)** (Impact: 56.8)
    * *Intent:* // // HU_Start(void) // // Create and initialize the heads-up widgets, software machines to // maint...
  * `HU_Ticker` **(Compute Cores)** (Impact: 31.2)
  * `HU_Init` **(Compute Cores)** (Impact: 28.1)
    * *Intent:* // // HU_Init() // // Initialize the heads-up display, text that overwrites the primary display // /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 290`, `structural_boundaries: 93`, `args: 38`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 285`, `dead_code: 9`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` d_deh.h, doomstat.h, dstrings.h, g_game.h, hu_lib.h, hu_stuff.h, r_main.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_genlin.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_7` (Drift: 0.0 IQR)
- **Magnitude:** 1252.96 | **LOC:** 1165 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.8414%), Tech Debt (26.287%)
**Top Internal Functions/Classes:**
  * `EV_DoGenCeiling` **(Compute Cores)** (Impact: 76.3)
    * *Intent:* // // EV_DoGenCeiling() // // Handle generalized ceiling types // // Passed the linedef activating t...
  * `EV_DoGenFloor` **(Compute Cores)** (Impact: 73.1)
    * *Intent:* // ////////////////////////////////////////////////////////// // // EV_DoGenFloor() // // Handle gen...
  * `EV_DoGenDoor` **(Compute Cores)** (Impact: 69.2)
    * *Intent:* // // EV_DoGenDoor() // // Handle generalized door types // // Passed the linedef activating the gen...
  * `EV_DoGenStairs` **(Compute Cores)** (Impact: 60.5)
    * *Intent:* // // EV_DoGenStairs() // // Handle generalized stair building // // Passed the linedef activating t...
  * `EV_DoGenLift` **(Compute Cores)** (Impact: 50.9)
    * *Intent:* // // EV_DoGenLift() // // Handle generalized lift types // // Passed the linedef activating the lif...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 270 instances
* *State Mutation (weighted view):* 834
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 235`, `structural_boundaries: 145`, `args: 9`, `func_start: 7`
* *Risk/State:* `state_mutation: 294`, `dead_code: 11`, `planned_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomstat.h, m_random.h, p_spec.h, p_tick.h, r_main.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1158.72 | **LOC:** 1969 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.1297%), Tech Debt (26.6156%)
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(Compute Cores)** (Impact: 56.8)
    * *Intent:* // ==================================================================== // WI_updateNetgameStats // ...
  * `WI_updateStats` **(Compute Cores)** (Impact: 41.8)
    * *Intent:* // ==================================================================== // WI_updateStats // Purpose...
  * `WI_updateDeathmatchStats` **(I/O & Config Routines)** (Impact: 33.9)
    * *Intent:* // ==================================================================== // WI_updateDeathmatchStats ...
  * `WI_drawOnLnode` **(Compute Cores)** (Impact: 23.2)
    * *Intent:* /* ==================================================================== * WI_drawOnLnode * Purpose: ...
  * `WI_drawNum` **(Many-Argument Workhorses)** (Impact: 22.7)
    * *Intent:* // ==================================================================== // WI_drawNum // Purpose: Dr...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 7 instances
* *Amplified Cascading Flux:* 216 instances
* *Memory Alloc (weighted view):* 10
* *State Mutation (weighted view):* 678
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 276`, `structural_boundaries: 124`, `args: 63`, `func_start: 38`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 246`, `dead_code: 4`, `fragile_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 7`, `immutability_locks: 24`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 11):` doomstat.h, g_game.h, lprintf.h, m_random.h, r_draw.h, r_main.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_5` (Drift: 0.0 IQR)
- **Magnitude:** 1106.92 | **LOC:** 1586 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (93.8429%), Tech Debt (17.1887%)
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 97.5)
    * *Intent:* // // AM_Responder() // // Handle events (user inputs) in automap mode // // Passed an input event, ...
  * `AM_drawWalls` **(Compute Cores)** (Impact: 83.0)
    * *Intent:* // This is LineDef based, not LineSeg based. // // jff 1/5/98 many changes in this routine // backwa...
  * `AM_clipMline` **(Compute Cores)** (Impact: 66.8)
    * *Intent:* // // AM_clipMline() // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algor...
  * `AM_DoorColor` **(Compute Cores)** (Impact: 29.5)
    * *Intent:* // // AM_DoorColor() // // Returns the 'color' or key needed for a door linedef type // // Passed th...
  * `AM_drawThings` **(Compute Cores)** (Impact: 26.1)
    * *Intent:* // // AM_drawThings() // // Draws the things on the automap in double IDDT cheat mode // // Passed c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 285`, `structural_boundaries: 100`, `args: 46`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 244`, `dead_code: 6`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 14):` am_map.h, config.h, d_deh.h, doomstat.h, dstrings.h, g_game.h, lprintf.h, p_maputl.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 1086.48 | **LOC:** 1043 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (66.8231%), Tech Debt (58.3251%)
**Top Internal Functions/Classes:**
  * `T_MovePlane` **(Many-Argument Workhorses)** (Impact: 95.1)
    * *Intent:* // // Move a plane (floor or ceiling) and check for crushing. Called // every tick by all actions th...
  * `EV_DoFloor` **(Many-Argument Workhorses)** (Impact: 76.4)
    * *Intent:* /////////////////////////////////////////////////////////////////////// // // Floor motion linedef h...
  * `EV_BuildStairs` **(Many-Argument Workhorses)** (Impact: 54.1)
  * `T_MoveFloor` **(Compute Cores)** (Impact: 41.7)
    * *Intent:* // // T_MoveFloor() // // Move a floor to it's destination (up or down). // Called once per tick for...
  * `EV_DoDonut` **(Compute Cores)** (Impact: 22.4)
    * *Intent:* // // EV_DoDonut() // // Handle donut function: lower pillar, raise surrounding pool, both to height...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 228 instances
* *State Mutation (weighted view):* 715
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 158`, `structural_boundaries: 86`, `args: 9`, `func_start: 9`
* *Risk/State:* `state_mutation: 259`, `dead_code: 8`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 7):` doomstat.h, p_map.h, p_spec.h, p_tick.h, r_main.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 1066.18 | **LOC:** 1079 | **CtrlFlow:** 26.3% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (75.7744%), Tech Debt (12.0436%)
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 82.5)
    * *Intent:* // // R_DrawSprite //
  * `R_ProjectSprite` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing if it might be visible. //
  * `R_DrawPSprite` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* // // R_DrawPSprite //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 35.1)
    * *Intent:* // a letter for the frame, and a number for the rotation. // // A sprite that is flippable will have...
  * `R_DrawVisSprite` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. // // CPhipps - new wad lum...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 221 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 180`, `structural_boundaries: 48`, `args: 25`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `state_mutation: 244`, `dead_code: 4`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` doomstat.h, lprintf.h, r_bsp.h, r_draw.h, r_fps.h, r_main.h, r_segs.h, r_things.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 997.62 | **LOC:** 914 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (82.5195%), Tech Debt (39.408%)
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Compute Cores)** (Impact: 182.2)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 138.1)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_KillMobj` **(Compute Cores)** (Impact: 71.4)
    * *Intent:* // // KillMobj // // killough 11/98: make static
  * `P_GiveAmmo` **(Many-Argument Workhorses)** (Impact: 59.5)
    * *Intent:* // // GET STUFF // // // P_GiveAmmo // Num is the number of clip loads, // not the individual count ...
  * `P_GiveWeapon` **(Many-Argument Workhorses)** (Impact: 30.2)
    * *Intent:* // // P_GiveWeapon // The weapon name may have a MF_DROPPED flag ored in. //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 158 instances
* *State Mutation (weighted view):* 474
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 239`, `structural_boundaries: 128`, `args: 10`, `func_start: 9`
* *Risk/State:* `state_mutation: 158`, `dead_code: 1`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` am_map.h, d_deh.h, doomstat.h, dstrings.h, lprintf.h, m_random.h, p_enemy.h, p_inter.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_16` (Drift: 0.0 IQR)
- **Magnitude:** 897.52 | **LOC:** 857 | **CtrlFlow:** 24.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (73.0363%), Tech Debt (26.0687%)
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 169.7)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 39.3)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked texture) for walls....
  * `R_ScaleFromGlobalAngle` **(Compute Cores)** (Impact: 6.2)
    * *Intent:* // // R_ScaleFromGlobalAngle // Returns the texture mapping scale // for the current line (horizonta...
  * `R_PointToDist` **(Compute Cores)** (Impact: 4.2)
    * *Intent:* // killough 5/2/98: move from r_main.c, made static, simplified
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 136`, `structural_boundaries: 15`, `args: 8`, `func_start: 5`
* *Risk/State:* `state_mutation: 224`, `dead_code: 10`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` doomstat.h, esp_attr.h, lprintf.h, r_bsp.h, r_draw.h, r_main.h, r_plane.h, r_segs.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_switch.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 855.24 | **LOC:** 1151 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (60.1832%), Tech Debt (10.4905%)
**Top Internal Functions/Classes:**
  * `P_UseSpecialLine` **(Many-Argument Workhorses)** (Impact: 648.0)
    * *Intent:* // // P_UseSpecialLine // // // Called when a thing uses (pushes) a special line. // Only the front ...
  * `P_ChangeSwitchTexture` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // // P_ChangeSwitchTexture() // // Function that changes switch wall texture on activation. // // P...
  * `P_InitSwitchList` **(Compute Cores)** (Impact: 15.2)
    * *Intent:* // when activated, and in the case of buttons, change back after a timeout. // // This routine modif...
  * `P_StartButton` **(Many-Argument Workhorses)** (Impact: 14.8)
    * *Intent:* // // P_StartButton() // // Start a button (retriggerable switch) counting down till it turns off. /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 178`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 47`, `dead_code: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 8):` doomstat.h, g_game.h, lprintf.h, p_spec.h, r_main.h, s_sound.h, sounds.h, w_wad.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 850.26 | **LOC:** 1030 | **CtrlFlow:** 15.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.4182%), Tech Debt (84.1944%)
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` **(Compute Cores)** (Impact: 47.2)
    * *Intent:* // // T_MoveCeiling, (ceiling_t: sector_t * swizzle), - active list // T_VerticalDoor, (vldoor_t: se...
  * `P_UnArchiveSpecials` **(I/O & Config Routines)** (Impact: 26.0)
    * *Intent:* // // P_UnArchiveSpecials //
  * `P_ArchiveThinkers` **(I/O & Config Routines)** (Impact: 19.1)
    * *Intent:* // // P_ArchiveThinkers // // 2/14/98 killough: substantially modified to fix savegame bugs
  * `P_UnArchiveThinkers` **(I/O & Config Routines)** (Impact: 18.4)
  * `P_ArchiveWorld` **(I/O & Config Routines)** (Impact: 11.8)
    * *Intent:* // // P_ArchiveWorld //
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 198 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 655
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 107`, `structural_boundaries: 76`, `args: 20`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 259`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` am_map.h, doomstat.h, lprintf.h, m_random.h, p_enemy.h, p_maputl.h, p_saveg.h, p_spec.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/r_patch.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_11` (Drift: 0.0 IQR)
- **Magnitude:** 838.46 | **LOC:** 788 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.4243%), Tech Debt (24.6237%)
**Top Internal Functions/Classes:**
  * `createTextureCompositePatch` **(Compute Cores)** (Impact: 90.1)
    * *Intent:* //---------------------------------------------------------------------------
  * `createPatch` **(Compute Cores)** (Impact: 53.5)
    * *Intent:* //---------------------------------------------------------------------------
  * `getPatchIsNotTileable` **(Compute Cores)** (Impact: 28.2)
    * *Intent:* //---------------------------------------------------------------------------
  * `R_CacheTextureCompositePatchNum` **(Compute Cores)** (Impact: 11.5)
    * *Intent:* //---------------------------------------------------------------------------
  * `R_CachePatchNum` **(Compute Cores)** (Impact: 11.4)
    * *Intent:* //---------------------------------------------------------------------------
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 5 instances
* *Amplified Cascading Flux:* 168 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 544
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 145`, `structural_boundaries: 50`, `args: 24`, `func_start: 18`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 208`, `dead_code: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 5`, `immutability_locks: 67`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` assert.h, doomstat.h, i_system.h, lprintf.h, p_tick.h, r_bsp.h, r_draw.h, r_main.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/mmus2mid.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Drift: 0.0 IQR)
- **Magnitude:** 653.82 | **LOC:** 870 | **CtrlFlow:** 20.2% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (71.5308%), Tech Debt (13.8451%)
**Top Internal Functions/Classes:**
  * `mmus2mid` **(Many-Argument Workhorses)** (Impact: 145.4)
    * *Intent:* // // mmus2mid() // // Convert a memory buffer contain MUS data to an Allegro MIDI structure // with...
  * `main` **(Many-Argument Workhorses)** (Impact: 34.5)
    * *Intent:* #ifdef STANDALONE /* this code unused by BOOM provided for future portability */ /* it also provides...
  * `MidiToMIDI` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* // // MidiToMIDI() // // Convert an in-memory copy of a MIDI format 0 or 1 file to // an Allegro MID...
  * `MIDIToMidi` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* // // MIDIToMidi() // // This routine converts an Allegro MIDI structure to a midi 1 format file // ...
  * `TWriteVarLen` **(Many-Argument Workhorses)** (Impact: 13.2)
    * *Intent:* // // TWriteVarLen() // // write the ULONG value to tracknum-th track, in midi format, which is // b...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Rce:* 3 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 3
* *Sec Tainted Injection (weighted view):* 3
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 105`, `structural_boundaries: 62`, `args: 37`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 8`, `state_mutation: 138`, `dead_code: 6`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 8`, `import: 13`
* *Defense:* `safety: 7`, `immutability_locks: 4`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 5):` allegro.h, config.h, ctype.h, lprintf.h, m_swap.h, mmus2mid.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 634.96 | **LOC:** 684 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (72.6985%), Tech Debt (30.4758%)
**Top Internal Functions/Classes:**
  * `P_PathTraverse` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* // // P_PathTraverse // Traces a line from x1,y1 to x2,y2, // calling the traverser function for eac...
  * `P_BoxOnLineSide` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
  * `P_BlockLinesIterator` **(Many-Argument Workhorses)** (Impact: 19.4)
    * *Intent:* // If the function returns false, // exit with false without checking anything else. // // // P_Bloc...
  * `P_SetThingPosition` **(Compute Cores)** (Impact: 17.0)
    * *Intent:* // // P_SetThingPosition // Links a thing into both a block and a subsector // based on it's x y. //...
  * `P_BlockThingsIterator` **(Compute Cores)** (Impact: 14.4)
    * *Intent:* // // P_BlockThingsIterator // // killough 5/3/98: reformatted, cleaned up
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 125 instances
* *State Mutation (weighted view):* 382
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 95`, `structural_boundaries: 56`, `args: 18`, `func_start: 17`
* *Risk/State:* `state_mutation: 132`, `dead_code: 2`, `unreferenced_by_name: 6`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` doomstat.h, m_bbox.h, p_map.h, p_maputl.h, p_setup.h, r_main.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_doors.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Drift: 0.0 IQR)
- **Magnitude:** 579.72 | **LOC:** 712 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (68.7844%), Tech Debt (32.5279%)
**Top Internal Functions/Classes:**
  * `T_VerticalDoor` **(Compute Cores)** (Impact: 112.7)
    * *Intent:* // Door action routines, called once per tick // ///////////////////////////////////////////////////...
  * `EV_VerticalDoor` **(Compute Cores)** (Impact: 108.3)
    * *Intent:* // // EV_VerticalDoor // // Handle opening a door manually, no tag value // // Passed the line activ...
  * `EV_DoLockedDoor` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* // // Door linedef handlers // /////////////////////////////////////////////////////////////// // //...
  * `EV_DoDoor` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* // // EV_DoDoor // // Handle opening a tagged door // // Passed the line activating the door and the...
  * `P_SpawnDoorRaiseIn5Mins` **(State Mutators)** (Impact: 3.0)
    * *Intent:* // // P_SpawnDoorRaiseIn5Mins() // // Spawn a door that opens after 5 minutes (called at level init)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 64`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 113`, `dead_code: 3`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 9):` d_deh.h, doomstat.h, dstrings.h, lprintf.h, p_spec.h, p_tick.h, r_main.h, s_sound.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_10` (Drift: 0.0 IQR)
- **Magnitude:** 576.08 | **LOC:** 830 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Risk Profile:** Cognitive Load (74.2226%), Tech Debt (93.8421%)
**Top Internal Functions/Classes:**
  * `P_SwitchWeapon` **(Compute Cores)** (Impact: 52.3)
    * *Intent:* // P_SwitchWeapon checks current ammo levels and gives you the // most preferred weapon with ammo. I...
  * `P_WeaponPreferred` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* // killough 5/2/98: whether consoleplayer prefers weapon w1 over weapon w2.
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `A_Saw` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* // // A_Saw //
  * `P_SetPsprite` **(Many-Argument Workhorses)** (Impact: 15.9)
    * *Intent:* // // P_SetPsprite //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 62`, `args: 37`, `func_start: 32`
* *Risk/State:* `state_mutation: 95`, `dead_code: 2`, `unreferenced_by_name: 24`
* *Architecture:* `api: 27`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.207
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 10):` d_event.h, doomstat.h, m_random.h, p_enemy.h, p_inter.h, p_map.h, p_pspr.h, r_demo.h...
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

- `components/prboom/include/doomdef.h` -> **Severity: 0.187** (Bridge: 0.0083 * Flux: 22.594%)
- `components/prboom/include/d_player.h` -> **Severity: 0.126** (Bridge: 0.0112 * Flux: 11.2984%)
- `components/prboom/include/doomstat.h` -> **Severity: 0.082** (Bridge: 0.0069 * Flux: 11.8705%)
- `components/prboom/include/m_fixed.h` -> **Severity: 0.034** (Bridge: 0.0014 * Flux: 24.8158%)
- `components/prboom/include/protocol.h` -> **Severity: 0.022** (Bridge: 0.0002 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `components/prboom/include/doomstat.h` -> **Severity: 17.343** (Embedded: 0.3283 * Error Risk: 52.8272%)
- `components/prboom/include/doomdef.h` -> **Severity: 12.738** (Embedded: 0.226 * Error Risk: 56.3634%)
- `components/prboom/include/m_fixed.h` -> **Severity: 11.874** (Embedded: 0.203 * Error Risk: 58.4884%)
- `components/prboom/include/d_player.h` -> **Severity: 11.812** (Embedded: 0.2071 * Error Risk: 57.0286%)
- `components/prboom/include/d_event.h` -> **Severity: 9.047** (Embedded: 0.1446 * Error Risk: 62.5811%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `components/prboom/include/m_fixed.h` -> **Severity: 3344.5** (Blast Radius: 33.445 * Doc Risk: 100.0%)
- `components/prboom/r_drawcolumn.inl` -> **Severity: 420.5** (Blast Radius: 4.205 * Doc Risk: 100.0%)
- `components/prboom/include/protocol.h` -> **Severity: 325.5** (Blast Radius: 3.255 * Doc Risk: 100.0%)
- `components/prboom/include/z_bmalloc.h` -> **Severity: 276.9** (Blast Radius: 2.769 * Doc Risk: 100.0%)
- `components/prboom/r_drawflush.inl` -> **Severity: 235.1** (Blast Radius: 2.351 * Doc Risk: 100.0%)

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with massive Cumulative Risk, severe Z-Scores (Architectural Drift), or extreme spikes in individual risk vectors (like State Flux or Cognitive Load). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
