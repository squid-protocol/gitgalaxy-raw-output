# ARCHITECTURAL_BRIEF: normal_esp32_doom
> INSTRUCTION: Deterministic Syntactic Analysis. Base architectural insights on Structural Magnitude, Extracted Signatures, and Risk overlays.

## 0. FORENSIC TRACEABILITY
| Metadata | Value |
|---|---|
| **Engine** | `GitGalaxy Scope vlatest (Delta Mode)` |
| **Git Remote** | `https://github.com/espressif/esp32-doom.git` |
| **Zero-Dependency Mode** | `Inactive (Full Precision)` |
| **File Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `92c0b8a801d69bb0` · trained `2026-09-19T12:02:33+00:00` |
| **Repo Archetype Brain** | corpus `master_db_v2.9.0.db` @ `71f3d405a2d8` · trainer `2b0cd20` · engine `unknown` · contract `7f4885b42206d553` · trained `2026-09-19T12:02:41+00:00` |
| **Archetype Brains** | trained against engine v2.9.1 (44ffeb1e, 2026-09-19); last measured at engine 49cba5db on language-crucible@v1.7.0 |
| **Function archetypes** | **VALIDATED**, 98.4% agreement with trained state |
| **File archetypes** | **VALIDATED**, 98.7% agreement with trained state |
| **Composition (file)** | **DEGRADED**, 97.4% agreement with trained state -- engine changes since training relabelled 2.6% of crucible files (agreement 97.4%); composition_file inputs disagree with the function model's labels: never read ['Annotated & Test Methods', 'Stateful Encapsulated Methods'], never emitted ['Annotated Framework Methods', 'Tests & Verification'] -- those units drop out and those input columns are always 0.0 (retrain tracked in #4111) |
| **Composition (repo)** | **INVALID**, labels withheld -- not measurable on one corpus; inherits composition_file's measured state; composition_repo reads the composition_file brain labels by name, but none of its 20 inputs (e.g. 'Static: Literature & Documentation') is a label the composition_file brain emits (e.g. 'Annotated Framework Methods Files') -- every input column is 0.0 (retrain tracked in #4111) |

## 0.5 AI THREAT AUDIT STATUS
> **✅ SECURE_NO_THREATS_DETECTED**
> XGBoost Structural Signatures model found no malicious artifacts.

## 1. EXECUTIVE SUMMARY
- **Scope:** 187 analyzed artifact(s), 48247 LOC.
- **Load-bearing artifact:** `components/prboom/include/doomstat.h` -- 61 in-repo importer(s) depend on it. Changes here propagate furthest.
- **Top orchestrator:** `components/prboom/g_game.c` -- pulls in 41 dependencies, the widest assembly point in the scan.
- **Heaviest artifact:** `components/prboom/p_spec.c` at magnitude 2826.24 (structural weight, not risk).
- **How to read this brief:** section 11 ranks artifacts by structural magnitude with a blast-radius line each; section 7 has the full dependency graph. The surface vectors in section 6 describe what is present in a file, not the probability of a defect -- Appendix A has the equations and the validation record behind that distinction.

## 1.5 SYSTEM ROLE & PHILOSOPHY
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
> *(Section 2, the structural-surface lexicon and its equations, is now **Appendix A** at the end of this brief -- the findings come first.)*

## 3. MACRO STATE
| Metric | Value |
|---|---|
| Total Artifacts | 203 |
| Analyzed Artifacts (Scanned) | 187 |
| Excluded Artifacts (Unparsable data, binaries, unsupported formats) | 16 |
| Total LOC | 48247 |
| Volatility Index | 0.0 |
| % Scanned of codebase = | 92.1% |
| Dominant Lang | C |

## 3.5 MACRO-NETWORK TOPOLOGY (Resilience & Coupling)
| Metric | Value | Interpretation |
|---|---|---|
| Modularity | 0.3194 | High = Clean micro-boundaries. Low = Spaghetti coupling. |
| Assortativity | -0.1648 | Positive = Resilient core. Negative = Fragile single-points-of-failure. |
| Cyclic Density | 29.3% | % of files trapped in dependency loops (Static Friction). |
| Avg Path Length | 2.8202 | Mean import hops from a file to each file it transitively depends on. Higher = Longer dependency chains. |
| Articulation Pts | 9 | Number of single files that, if removed, shatter the network. |

## 4. COMPOSITION
| Lang | Files | LOC | Share |
|---|---|---|---|
| C | 170 | 47558 | 90.9% |
| MAKEFILE | 9 | 36 | 4.8% |
| CPP | 4 | 648 | 2.1% |
| PLAINTEXT | 2 | 0 | 1.1% |
| SHELL | 1 | 2 | 0.5% |
| CSV | 1 | 3 | 0.5% |

## 4.1 SOURCE ENCODINGS
> 2 file(s) had no BOM, were not UTF-8 and matched no declared code page: decoded by a legacy guess (`--source-encoding` declares the real one).
| Encoding | Decode | Files |
|---|---|---|
| utf-8 | utf-8 | 185 |
| cp1252 | cp1252-fallback | 2 |

## 4.5 REPOSITORY ECOSYSTEM BASELINE (GLOBAL ARCHITECTURE)
> **Assigned Ecosystem Baseline:** `Unvalidated`
> **Architectural Drift Z-Score:** `0.0`
> **Composition Archetype:** `Unvalidated` (z +0.00; from the repo's file-archetype mix)
> **File Composition:** Declarative / Non-Code 41%, Large Core Modules (3) 17%, Data / Markup / Trivial 14%, Compute Cores Files 10%, Large Core Modules 5%
> **ℹ️ TYPICAL INTERPRETATION:** This repository falls within standard variance (Z-Score between -1.0 and 2.0), representing a typical implementation of this archetype.

## 4.6 FILE ARCHETYPES & STATIC ASSETS
### Active Execution Logic (ML Clusters)
| Archetype | Count | Repo % |
|---|---|---|
| Unclassified | 185 | 98.9% |

### Inert Structural Mass (Static Categories)
| Category | Count | Repo % |
|---|---|---|
| Static: Literature & Documentation | 2 | 1.1% |

## 5. EXCLUDED ARTIFACTS (Unparsable or Shielded Files)
*Total Excluded Artifacts: 16*

**Composition by Extension & Reason:**
- `.c`: 1x Excluded (Embedded Hex Payload: 40960 hex tokens in 3418 LOC), 1x Excluded (Embedded Hex Payload: 16384 hex tokens in 1370 LOC), 1x Excluded (Embedded Hex Payload: 8196 hex tokens in 687 LOC)
- `.dat`: 4x Excluded (Unsupported Extension: '.dat')
- `no_extension`: 1x Excluded (System Exclusion, Hidden Directory, or Dynamic Ignored Dir), 1x Excluded (Machine-Generated Source Code Signature: 298 LOC)
- `.projbuild`: 1x Excluded (Unsupported Extension: '.projbuild')
- `.h`: 1x Excluded (Machine-Generated Source Code Signature: 1501 LOC)
- `.disabled`: 1x Excluded (Unsupported Extension: '.disabled')
- `.wad`: 1x Excluded (Unsupported Extension: '.wad')
- `.rst`: 1x Excluded (Unsupported Extension: '.rst')

## 6. STRUCTURAL SURFACE PROFILE (formerly Risk Exposure) ANALYSIS (0-100%)
| Structural Surface Vector | Min | Max | Mean | Med | Mode |
|---|---|---|---|---|---|
| Complexity Load (formerly Cognitive Load Exposure) | 0.0 | 97.8 | 26.1 | 0.0 | 0.0 |
| Guard Balance (formerly Error & Exception Exposure) | 0.0 | 89.9 | 34.7 | 0.0 | 0.0 |
| Debt Markers (formerly Tech Debt Exposure) | 0.0 | 100.0 | 22.4 | 0.0 | 0.0 |
| Test Surface (formerly Testing Exposure) | 0.0 | 80.0 | 23.3 | 2.3 | 2.3 |
| Connectivity (formerly API Exposure) | 0.0 | 100.0 | 32.7 | 7.6 | 0.0 |
| Concurrency Surface (formerly Concurrency Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Mutation Surface (formerly State Flux Exposure) | 0.0 | 100.0 | 40.7 | 0.0 | 0.0 |
| Dead Code Surface (formerly Commented Logic Exposure) | 0.0 | 94.3 | 2.2 | 0.0 | 0.0 |
| Historical Stability (predictive layer, promotion pending #2987) (formerly Instability Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Historical Churn (predictive layer, promotion pending #2987) (formerly Volatility Exposure) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |
| Doc Surface (formerly Documentation Exposure) _(coverage)_ | 0.0 | 100.0 | 44.6 | 0.0 | 0.0 |
| Credential Material (formerly Hardcoded Payload Artifacts) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

> `Doc Surface (formerly Documentation Exposure)` is **documentation coverage, not a fragility driver**. It is reported for context beside program length, and is deliberately excluded from the ranked-file drivers in this brief: it measures the share of a file's unit weight a reader cannot recover from documentation, so on a codebase that documents little it sits near ceiling everywhere and describes the repo rather than distinguishing files within it.
> `Spec Alignment (formerly Specification Exposure)` was **not measured** on this scan and is therefore absent above rather than reported as 0 (which would assert full alignment). Enable it with `--spec-alignment` if this codebase uses the corresponding convention.

## 6b. SURFACE FAMILY PROFILE (Tier 1/2/3 -- gitgalaxy#2994)
> Percentile columns elsewhere in this brief that come from the Tier-2 snapshot percentiles are SNAPSHOT-RELATIVE: "87" means this file's value sits at the 87th percentile of THIS repo's files for that surface -- true by construction (Hazen average-rank), not a calibrated 0-100 risk threshold like the section 6 sigmoid scores above. An all-zero surface across the whole repo reads as 0.0 for every file, never a false-median 50.
| Family | Repo Total | Files w/ Signal | P90 File Value | Top File |
|---|---|---|---|---|
| memory | 368 | 46 | 5 | `components/prboom/d_deh.c` |
| cleanup | 81 | 22 | 1 | `components/prboom/mmus2mid.c` |
| guards | 2498 | 123 | 30 | `components/prboom/d_deh.c` |
| danger | 356 | 46 | 5 | `components/prboom/r_fps.c` |
| concurrency | 0 | 0 | 0 | - |
| connectivity | 2652 | 159 | 25 | `components/prboom/include/d_deh.h` |
| io | 52 | 9 | 0 | `components/prboom/d_deh.c` |
| crypto | 0 | 0 | 0 | - |
| ipc | 5 | 2 | 0 | `components/prboom/d_client.c` |
| time | 2 | 1 | 0 | `components/prboom-esp32-compat/i_system.c` |
| serialization | 0 | 0 | 0 | - |
| regex | 0 | 0 | 0 | - |
| events | 0 | 0 | 0 | - |
| tests | 0 | 0 | 0 | - |
| docs | 146 | 17 | 0 | `components/prboom/m_menu.c` |
| debt | 242 | 50 | 3 | `components/prboom/d_deh.c` |
| mutation | 13920 | 106 | 256 | `components/prboom/g_game.c` |
| dead_code | 641 | 79 | 11 | `components/prboom/p_enemy.c` |
| credential | 0 | 0 | 0 | - |
| threat | 2 | 2 | 0 | `components/prboom/hu_stuff.c` |
| ml_ai | 16 | 7 | 0 | `components/prboom/include/d_englsh.h` |
| ui | 1 | 1 | 0 | `components/prboom/lprintf.c` |

**Relations (repo medians):**
- `guard_balance_ratio` (guards / (danger + 1)): **1.3421**
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
3. **lprintf.c** (`components/prboom/lprintf.c`) — 43 inbound connections
4. **r_main.h** (`components/prboom/include/r_main.h`) — 41 inbound connections
5. **config.h** (`components/prboom/include/config.h`) — 35 inbound connections

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
- `M_Responder` **(Many-Argument Workhorses)** (@ `components/prboom/m_menu.c`) -> Impact: **470.2** | LOC: 1088
  * *Intent:* ///////////////////////////////////////////////////////////////////////////// // // M_Responder // // Examines incoming keystrokes and button pushes a...
- `P_TouchSpecialThing` **(Many-Argument Workhorses)** (@ `components/prboom/p_inter.c`) -> Impact: **182.2** | LOC: 318
  * *Intent:* // // P_TouchSpecialThing //
- `R_StoreWallRange` **(Many-Argument Workhorses)** (@ `components/prboom/r_segs.c`) -> Impact: **166.2** | LOC: 380
  * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive). //
- `HU_Drawer` **(I/O & Config Routines)** (@ `components/prboom/hu_stuff.c`) -> Impact: **157.1** | LOC: 541
  * *Intent:* // // HU_Drawer() // // Draw all the pieces of the heads-up display // // Passed nothing, returns nothing //
- `V_DrawMemPatch` **(Many-Argument Workhorses)** (@ `components/prboom/v_video.c`) -> Impact: **156.9** | LOC: 227
  * *Intent:* // // V_DrawMemPatch // // CPhipps - unifying patch drawing routine, handles all cases and combinations // of stretching, flipping and translating // ...
- `mmus2mid` **(Many-Argument Workhorses)** (@ `components/prboom/mmus2mid.c`) -> Impact: **145.4** | LOC: 224
  * *Intent:* // // mmus2mid() // // Convert a memory buffer contain MUS data to an Allegro MIDI structure // with specified time division and compression. // // Pa...
- `D_DoomMainSetup` **(I/O & Config Routines)** (@ `components/prboom/d_main.c`) -> Impact: **142.6** | LOC: 492
  * *Intent:* // // D_DoomMainSetup // // CPhipps - the old contents of D_DoomMain, but moved out of the main // line of execution so its stack space can be freed
- `P_DamageMobj` **(Many-Argument Workhorses)** (@ `components/prboom/p_inter.c`) -> Impact: **138.1** | LOC: 169
  * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the damage // creature or missile, can be NULL (slime, ...

*Function archetypes referenced above:*
  * **I/O & Config Routines**: dominated by I/O and configuration handling
  * **Many-Argument Workhorses**: large, many-parameter procedural function doing heavy lifting

## 9. DIRECTORY GROUPS (Top 10 Heaviest Modules)
| Folder Path | Files | Total Impact | Avg Complexity Load | Avg Debt Markers |
|---|---|---|---|---|
| `components/prboom` | 77 | 43649.1 | 55.72% | 35.98% |
| `components/prboom/include` | 78 | 2873.84 | 0.09% | 3.09% |
| `components/prboom-esp32-compat` | 10 | 898.7 | 36.75% | 56.35% |
| `components/prboom/native` | 7 | 395.12 | 21.58% | 76.85% |
| `components/prboom-wad-tables/include` | 4 | 52.16 | 0.0% | 0.0% |
| `components/prboom-esp32-compat/include` | 3 | 43.76 | 0.0% | 0.0% |
| `main` | 3 | 32.22 | 2.67% | 12.58% |
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
- **Unknown Dependencies:** `1120` packages imported that bypass the Zero-Trust whitelist.

## 11. RANKED ARTIFACTS (Top 25 by Structural Magnitude)
> Ranked by Structural Magnitude: the file's structural weight and centralization within the system. Magnitude is **not** a risk score and is independent of the surface vectors in section 6. Each entry carries a **Blast Radius** line stating what a change to it would reach -- that, not the vector percentages, is the actionable part.

### `components/prboom/p_spec.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 8.359)
- **Top Global Matches:** file_cluster_6: 8.359, file_cluster_8: 9.233, file_cluster_4: 16.348
- **Magnitude:** 2826.24 | **LOC:** 3354 | **CtrlFlow:** 39.2% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **15** in-repo importer(s); it depends on **19**; blast radius 4.365; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (76.4%), Complexity Load (formerly Cognitive Load) (43.8%), Connectivity (formerly Api Exposure) (6.0%)
- **Documentation Coverage:** 93.5065% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CrossSpecialLine` **(Many-Argument Workhorses)** (Impact: 658.0)
    * *Intent:* ///////////////////////////////////////////////////////////////////////// // // P_CrossSpecialLine -...
  * `P_ShootSpecialLine` **(Many-Argument Workhorses)** (Impact: 136.8)
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
* *Structure:* `branch: 801`, `structural_boundaries: 359`, `args: 56`, `func_start: 43`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 418`, `fragile_debt: 3`, `unreferenced_by_name: 22`
* *Architecture:* `api: 36`, `import: 19`
* *Defense:* `safety: 2`, `doc: 18`, `immutability_locks: 8`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 4.365
  * `Choke Point (Betweenness):` 0.025905 | `Ripple Effect (Closeness):` 0.106816
  * `Imports (Out-Degree: 39):` d_deh.h, d_englsh.h, doomstat.h, g_game.h, lprintf.h, m_argv.h, m_bbox.h, m_random.h...
  * `Imported By (In-Degree: 15):` (Excluded from Brief to save tokens)

### `components/prboom/m_menu.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 7.774)
- **Top Global Matches:** file_cluster_4: 7.774, file_cluster_16: 9.069, file_cluster_12: 9.247
- **Magnitude:** 2804.28 | **LOC:** 5565 | **CtrlFlow:** 16.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **24**; blast radius 2.284; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.8%), Guard Balance (formerly Safety Score) (69.8%)
- **Documentation Coverage:** 93.3333% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `M_Responder` **(Many-Argument Workhorses)** (Impact: 470.2)
    * *Intent:* ///////////////////////////////////////////////////////////////////////////// // // M_Responder // /...
  * `M_GetKeyString` **(Compute Cores)** (Impact: 80.1)
    * *Intent:* //////////////////////////////////////////////////////////////////////////// // // Dynamic HELP scre...
  * `M_DrawSetting` **(Compute Cores)** (Impact: 59.4)
    * *Intent:* ///////////////////////////// // // phares 4/18/98: // Consolidate Item Setting drawing code // // M...
  * `M_DrawInstructions` **(I/O & Config Routines)** (Impact: 22.8)
    * *Intent:* ///////////////////////////// // // phares 4/18/98: // M_DrawInstructions writes the instruction tex...
  * `M_DrawScreenItems` **(Stateful Encapsulated Methods)** (Impact: 17.2)
    * *Intent:* ///////////////////////////// // // M_DrawScreenItems takes the data for each menu item and gives it...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 6 instances
* *Amplified Cascading Flux:* 451 instances
* *Memory Alloc (weighted view):* 0
* *State Mutation (weighted view):* 1443
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 595`, `structural_boundaries: 641`, `args: 258`, `func_start: 109`, `class_start: 28`
* *Risk/State:* `safety_bypasses: 29`, `high_risk_execution: 1`, `state_mutation: 541`, `dead_code: 9`, `fragile_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `io: 1`, `api: 180`, `import: 24`
* *Defense:* `safety: 2`, `doc: 61`, `immutability_locks: 31`, `cleanup: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.284
  * `Choke Point (Betweenness):` 0.004053 | `Ripple Effect (Closeness):` 0.10614
  * `Imports (Out-Degree: 33):` am_map.h, d_deh.h, d_main.h, doomdef.h, doomstat.h, dstrings.h, fcntl.h, g_game.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/prboom/g_game.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.46)
- **Top Global Matches:** file_cluster_6: 6.46, file_cluster_8: 10.749, file_cluster_4: 14.1
- **Magnitude:** 2673.96 | **LOC:** 2923 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **41**; blast radius 3.404; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (85.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `G_BuildTiccmd` **(Compute Cores)** (Impact: 111.3)
  * `G_ReadDemoHeader` **(Many-Argument Workhorses)** (Impact: 109.2)
  * `G_Ticker` **(I/O & Config Routines)** (Impact: 75.0)
    * *Intent:* // // G_Ticker // Make ticcmd_ts for the players. //
  * `G_Responder` **(Compute Cores)** (Impact: 60.7)
    * *Intent:* // // G_Responder // Get info needed to make ticcmd_ts for the players. //
  * `G_CheckSpot` **(Many-Argument Workhorses)** (Impact: 48.2)
    * *Intent:* // // G_CheckSpot // Returns false if the player cannot be respawned // at the given mapthing_t spot...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 4 instances
* *Amplified Cascading Flux:* 531 instances
* *Memory Alloc (weighted view):* 4
* *State Mutation (weighted view):* 1750
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 496`, `structural_boundaries: 240`, `args: 65`, `func_start: 47`
* *Risk/State:* `safety_bypasses: 14`, `state_mutation: 688`, `dead_code: 8`, `fragile_debt: 7`, `unreferenced_by_name: 13`
* *Architecture:* `io: 8`, `api: 37`, `import: 43`
* *Defense:* `safety: 17`, `immutability_locks: 32`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 3.404
  * `Choke Point (Betweenness):` 0.060915 | `Ripple Effect (Closeness):` 0.13416
  * `Imports (Out-Degree: 62):` am_map.h, config.h, d_deh.h, d_main.h, d_net.h, doomstat.h, dstrings.h, f_finale.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `components/prboom/p_enemy.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 6.021)
- **Top Global Matches:** file_cluster_6: 6.021, file_cluster_4: 7.038, file_cluster_15: 15.146
- **Magnitude:** 2129.64 | **LOC:** 2602 | **CtrlFlow:** 32.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **15**; blast radius 2.434; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (97.3%), Complexity Load (formerly Cognitive Load) (94.9%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `A_Chase` **(Compute Cores)** (Impact: 86.8)
    * *Intent:* // // A_Chase // Actor has a melee attack, // so it tries to close as fast as possible //
  * `A_BossDeath` **(Compute Cores)** (Impact: 80.0)
    * *Intent:* // // A_BossDeath // Possibly trigger special effects // if on first boss level //
  * `P_DoNewChaseDir` **(Many-Argument Workhorses)** (Impact: 68.7)
    * *Intent:* // // P_DoNewChaseDir // // killough 9/8/98: // // Most of P_NewChaseDir(), except for what // deter...
  * `P_IsOnLift` **(Compute Cores)** (Impact: 57.9)
    * *Intent:* /* * P_IsOnLift * * killough 9/9/98: * * Returns true if the object is on a lift. Used for AI, * sin...
  * `P_Move` **(Many-Argument Workhorses)** (Impact: 48.7)
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 304 instances
* *State Mutation (weighted view):* 970
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 545`, `structural_boundaries: 303`, `args: 99`, `func_start: 88`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 12`, `state_mutation: 362`, `fragile_debt: 5`, `unreferenced_by_name: 60`
* *Architecture:* `api: 70`, `import: 15`
* *Defense:* `immutability_locks: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.434
  * `Choke Point (Betweenness):` 0.001945 | `Ripple Effect (Closeness):` 0.080625
  * `Imports (Out-Degree: 31):` doomstat.h, g_game.h, lprintf.h, m_bbox.h, m_random.h, p_enemy.h, p_inter.h, p_map.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `components/prboom/p_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.742)
- **Top Global Matches:** file_cluster_6: 7.742, file_cluster_8: 8.753, file_cluster_4: 16.061
- **Magnitude:** 1811.14 | **LOC:** 2336 | **CtrlFlow:** 29.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **14**; blast radius 3.612; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.8%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (78.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_TryMove` **(Many-Argument Workhorses)** (Impact: 96.7)
    * *Intent:* // // P_TryMove // Attempt to move to a new position, // crossing special lines unless MF_TELEPORT i...
  * `PIT_CheckThing` **(Compute Cores)** (Impact: 66.7)
    * *Intent:* // // PIT_CheckThing //
  * `P_HitSlideLine` **(Compute Cores)** (Impact: 40.7)
    * *Intent:* // // P_HitSlideLine // Adjusts the xmove / ymove // so that the next move will slide along the wall...
  * `P_GetMoveFactor` **(Many-Argument Workhorses)** (Impact: 39.9)
    * *Intent:* /* phares 3/19/98 * P_GetMoveFactor() returns the value by which the x,y * movements are multiplied ...
  * `PIT_CheckLine` **(Compute Cores)** (Impact: 36.7)
    * *Intent:* // // PIT_CheckLine // Adjusts tmfloorz and tmceilingz as lines are contacted //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 308 instances
* *State Mutation (weighted view):* 995
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 375`, `structural_boundaries: 216`, `args: 43`, `func_start: 39`
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 379`, `dead_code: 1`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 36`, `import: 14`
* *Defense:* `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.612
  * `Choke Point (Betweenness):` 0.008871 | `Ripple Effect (Closeness):` 0.115656
  * `Imports (Out-Degree: 25):` doomstat.h, lprintf.h, m_bbox.h, m_random.h, p_inter.h, p_map.h, p_maputl.h, p_mobj.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `components/prboom/d_deh.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 6.699)
- **Top Global Matches:** file_cluster_3: 6.699, file_cluster_8: 22.027, file_cluster_6: 34.861
- **Magnitude:** 1737.44 | **LOC:** 3096 | **CtrlFlow:** 20.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **15**; blast radius 2.138; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (61.4%), Complexity Load (formerly Cognitive Load) (44.9%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `deh_procMisc` **(Many-Argument Workhorses)** (Impact: 98.0)
    * *Intent:* // ==================================================================== // deh_procMisc // Purpose: ...
  * `deh_procText` **(Many-Argument Workhorses)** (Impact: 74.3)
    * *Intent:* // ==================================================================== // deh_procText // Purpose: ...
  * `deh_procFrame` **(Many-Argument Workhorses)** (Impact: 71.5)
    * *Intent:* // ==================================================================== // deh_procFrame // Purpose:...
  * `deh_procSounds` **(Many-Argument Workhorses)** (Impact: 65.0)
    * *Intent:* // ==================================================================== // deh_procSounds // Purpose...
  * `ProcessDehFile` **(Many-Argument Workhorses)** (Impact: 64.2)
    * *Intent:* // ==================================================================== // ProcessDehFile // Purpose...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 1 instances
* *Amplified Cascading Flux:* 191 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 580
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 479`, `structural_boundaries: 195`, `args: 67`, `func_start: 33`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 7`, `state_mutation: 198`, `dead_code: 4`, `fragile_debt: 6`, `unreferenced_by_name: 2`
* *Architecture:* `io: 16`, `api: 19`, `import: 15`
* *Defense:* `safety: 27`, `immutability_locks: 342`, `cleanup: 3`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.138
  * `Choke Point (Betweenness):` 0.000587 | `Ripple Effect (Closeness):` 0.081408
  * `Imports (Out-Degree: 16):` ctype.h, d_deh.h, d_think.h, doomdef.h, doomstat.h, doomtype.h, dstrings.h, g_game.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/prboom/p_setup.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.609)
- **Top Global Matches:** file_cluster_6: 5.609, file_cluster_4: 9.212, file_cluster_8: 16.056
- **Magnitude:** 1440.54 | **LOC:** 1689 | **CtrlFlow:** 20.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **20**; blast radius 2.185; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.4%)
- **Documentation Coverage:** 89.2857% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_CreateBlockMap` **(I/O & Config Routines)** (Impact: 79.9)
    * *Intent:* // // Actually construct the blockmap lump from the level data // // This finds the intersection of ...
  * `P_SetupLevel` **(Many-Argument Workhorses)** (Impact: 62.6)
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
* *Structure:* `branch: 218`, `structural_boundaries: 62`, `args: 46`, `func_start: 26`, `class_start: 5`
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 389`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 2`
* *Architecture:* `api: 5`, `import: 20`
* *Defense:* `safety: 4`, `doc: 5`, `immutability_locks: 40`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.185
  * `Choke Point (Betweenness):` 0.006398 | `Ripple Effect (Closeness):` 0.09638
  * `Imports (Out-Degree: 39):` doomstat.h, g_game.h, i_system.h, lprintf.h, m_argv.h, m_bbox.h, math.h, p_enemy.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `components/prboom/d_main.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 7.161)
- **Top Global Matches:** file_cluster_8: 7.161, file_cluster_6: 13.587, file_cluster_4: 22.073
- **Magnitude:** 1393.5 | **LOC:** 1739 | **CtrlFlow:** 28.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **38**; blast radius 2.657; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.1%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `D_DoomMainSetup` **(I/O & Config Routines)** (Impact: 142.6)
    * *Intent:* // // D_DoomMainSetup // // CPhipps - the old contents of D_DoomMain, but moved out of the main // l...
  * `CheckIWAD` **(Many-Argument Workhorses)** (Impact: 62.4)
    * *Intent:* // // CheckIWAD // // Verify a file is indeed tagged as an IWAD // Scan its lumps for levelnames and...
  * `D_Display` **(Stateful Encapsulated Methods)** (Impact: 46.8)
  * `GetFirstMap` **(Compute Cores)** (Impact: 36.4)
    * *Intent:* // // GetFirstMap // // Ty 08/29/98 - determine first available map from the loaded wads and run it ...
  * `DoLooseFiles` **(I/O & Config Routines)** (Impact: 32.4)
    * *Intent:* // // Note that more than one -file, etc. entry on the command line won't // work, so we have to go ...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 8 instances
* *Amplified Cascading Flux:* 288 instances
* *Memory Alloc (weighted view):* 9
* *State Mutation (weighted view):* 888
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 325`, `structural_boundaries: 122`, `args: 66`, `func_start: 24`, `class_start: 1`
* *Risk/State:* `safety_bypasses: 21`, `state_mutation: 312`, `dead_code: 5`, `fragile_debt: 5`, `unreferenced_by_name: 3`
* *Architecture:* `io: 2`, `api: 16`, `import: 39`
* *Defense:* `safety: 6`, `immutability_locks: 23`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.657
  * `Choke Point (Betweenness):` 0.028761 | `Ripple Effect (Closeness):` 0.109608
  * `Imports (Out-Degree: 54):` am_map.h, d_deh.h, d_main.h, d_net.h, direct.h, doomdef.h, doomstat.h, doomtype.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `components/prboom/v_video.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.162)
- **Top Global Matches:** file_cluster_4: 5.162, file_cluster_6: 9.595, file_cluster_16: 10.89
- **Magnitude:** 1314.1 | **LOC:** 1042 | **CtrlFlow:** 24.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **14** in-repo importer(s); it depends on **11**; blast radius 3.705; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.3%), Guard Balance (formerly Safety Score) (89.2%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `V_DrawMemPatch` **(Many-Argument Workhorses)** (Impact: 156.9)
    * *Intent:* // // V_DrawMemPatch // // CPhipps - unifying patch drawing routine, handles all cases and combinati...
  * `V_UpdateTrueColorPalette` **(Compute Cores)** (Impact: 51.5)
    * *Intent:* #include "GAMMATBL.h" // // V_UpdateTrueColorPalette //
  * `WRAP_V_DrawLine` **(Stateful Encapsulated Methods)** (Impact: 40.2)
    * *Intent:* // // WRAP_V_DrawLine() // // Draw a line in the frame buffer. // Classic Bresenham w/ whatever opti...
  * `FUNC_V_DrawBackground` **(Many-Argument Workhorses)** (Impact: 37.8)
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
* *Risk/State:* `safety_bypasses: 3`, `state_mutation: 295`, `dead_code: 2`, `unreferenced_by_name: 10`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `immutability_locks: 28`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.705
  * `Choke Point (Betweenness):` 0.015884 | `Ripple Effect (Closeness):` 0.138595
  * `Imports (Out-Degree: 17):` GAMMATBL.h, doomdef.h, esp_attr.h, i_video.h, lprintf.h, m_bbox.h, r_draw.h, r_filter.h...
  * `Imported By (In-Degree: 14):` (Excluded from Brief to save tokens)

### `components/prboom/p_mobj.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 7.961)
- **Top Global Matches:** file_cluster_6: 7.961, file_cluster_8: 9.828, file_cluster_4: 15.906
- **Magnitude:** 1298.34 | **LOC:** 1533 | **CtrlFlow:** 35.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **11** in-repo importer(s); it depends on **16**; blast radius 3.349; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (82.9%), Complexity Load (formerly Cognitive Load) (82.4%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_XYMovement` **(Compute Cores)** (Impact: 119.7)
    * *Intent:* // // P_XYMovement // // Attempts to move something if it has momentum. //
  * `P_ZMovement` **(Compute Cores)** (Impact: 116.8)
    * *Intent:* // // P_ZMovement // // Attempt vertical movement.
  * `P_SpawnMapThing` **(Compute Cores)** (Impact: 90.6)
    * *Intent:* // // P_SpawnMapThing // The fields of the mapthing should // already be in host byte order. //
  * `P_MobjThinker` **(Compute Cores)** (Impact: 36.5)
    * *Intent:* // // P_MobjThinker //
  * `P_SetMobjState` **(Stateful Encapsulated Methods)** (Impact: 23.7)
    * *Intent:* #include "st_stuff.h" #include "hu_stuff.h" #include "s_sound.h" #include "info.h" #include "g_game....
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 225 instances
* *State Mutation (weighted view):* 707
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 313`, `structural_boundaries: 65`, `args: 23`, `func_start: 18`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 257`, `dead_code: 2`, `planned_debt: 2`, `fragile_debt: 8`, `unreferenced_by_name: 7`
* *Architecture:* `api: 16`, `import: 16`
* *Defense:* `safety: 1`, `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.349
  * `Choke Point (Betweenness):` 0.010225 | `Ripple Effect (Closeness):` 0.114863
  * `Imports (Out-Degree: 28):` doomdef.h, doomstat.h, g_game.h, hu_stuff.h, info.h, lprintf.h, m_random.h, p_inter.h...
  * `Imported By (In-Degree: 11):` (Excluded from Brief to save tokens)

### `components/prboom/hu_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 11.859)
- **Top Global Matches:** file_cluster_3: 11.859, file_cluster_8: 30.83, file_cluster_1: 41.039
- **Magnitude:** 1259.52 | **LOC:** 1594 | **CtrlFlow:** 24.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **11**; blast radius 2.345; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (73.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `HU_Drawer` **(I/O & Config Routines)** (Impact: 157.1)
    * *Intent:* // // HU_Drawer() // // Draw all the pieces of the heads-up display // // Passed nothing, returns no...
  * `HU_Responder` **(Stateful Encapsulated Methods)** (Impact: 76.5)
    * *Intent:* // // HU_Responder() // // Responds to input events that affect the heads up displays // // Passed t...
  * `HU_Start` **(I/O & Config Routines)** (Impact: 56.8)
    * *Intent:* // // HU_Start(void) // // Create and initialize the heads-up widgets, software machines to // maint...
  * `HU_Ticker` **(I/O & Config Routines)** (Impact: 31.2)
  * `HU_Init` **(I/O & Config Routines)** (Impact: 28.1)
    * *Intent:* // // HU_Init() // // Initialize the heads-up display, text that overwrites the primary display // /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 278 instances
* *State Mutation (weighted view):* 841
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 288`, `structural_boundaries: 93`, `args: 38`, `func_start: 10`
* *Risk/State:* `safety_bypasses: 37`, `state_mutation: 285`, `unreferenced_by_name: 6`
* *Architecture:* `api: 15`, `import: 11`
* *Defense:* `immutability_locks: 6`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.345
  * `Choke Point (Betweenness):` 0.003239 | `Ripple Effect (Closeness):` 0.104162
  * `Imports (Out-Degree: 14):` d_deh.h, doomstat.h, dstrings.h, g_game.h, hu_lib.h, hu_stuff.h, r_main.h, s_sound.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `components/prboom/p_genlin.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_1` (Centroid distance: 5.413)
- **Top Global Matches:** file_cluster_1: 5.413, file_cluster_3: 48.14, file_cluster_8: 69.978
- **Magnitude:** 1252.96 | **LOC:** 1165 | **CtrlFlow:** 27.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **7**; blast radius 2.096; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.7%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 294`, `planned_debt: 2`, `unreferenced_by_name: 7`
* *Architecture:* `api: 7`, `import: 7`
* *Defense:* `doc: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 12):` doomstat.h, m_random.h, p_spec.h, p_tick.h, r_main.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/wi_stuff.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.663)
- **Top Global Matches:** file_cluster_4: 5.663, file_cluster_6: 8.514, file_cluster_16: 12.708
- **Magnitude:** 1158.72 | **LOC:** 1969 | **CtrlFlow:** 23.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **11**; blast radius 2.34; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.0%), Complexity Load (formerly Cognitive Load) (72.1%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `WI_updateNetgameStats` **(I/O & Config Routines)** (Impact: 56.8)
    * *Intent:* // ==================================================================== // WI_updateNetgameStats // ...
  * `WI_updateStats` **(I/O & Config Routines)** (Impact: 41.8)
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
* *Risk/State:* `safety_bypasses: 6`, `state_mutation: 246`, `dead_code: 2`, `fragile_debt: 4`, `unreferenced_by_name: 5`
* *Architecture:* `api: 36`, `import: 11`
* *Defense:* `safety: 7`, `immutability_locks: 24`, `cleanup: 7`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.34
  * `Choke Point (Betweenness):` 0.00217 | `Ripple Effect (Closeness):` 0.0975
  * `Imports (Out-Degree: 17):` doomstat.h, g_game.h, lprintf.h, m_random.h, r_draw.h, r_main.h, s_sound.h, sounds.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/prboom/am_map.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.981)
- **Top Global Matches:** file_cluster_6: 5.981, file_cluster_4: 9.75, file_cluster_8: 15.69
- **Magnitude:** 1096.52 | **LOC:** 1586 | **CtrlFlow:** 26.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **14**; blast radius 2.395; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (93.6%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (76.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `AM_Responder` **(Compute Cores)** (Impact: 97.5)
    * *Intent:* // // AM_Responder() // // Handle events (user inputs) in automap mode // // Passed an input event, ...
  * `AM_drawWalls` **(I/O & Config Routines)** (Impact: 83.0)
    * *Intent:* // This is LineDef based, not LineSeg based. // // jff 1/5/98 many changes in this routine // backwa...
  * `AM_clipMline` **(Many-Argument Workhorses)** (Impact: 56.4)
    * *Intent:* // // AM_clipMline() // // Automap clipping of lines. // // Based on Cohen-Sutherland clipping algor...
  * `AM_DoorColor` **(Stateful Encapsulated Methods)** (Impact: 29.5)
    * *Intent:* // // AM_DoorColor() // // Returns the 'color' or key needed for a door linedef type // // Passed th...
  * `AM_drawThings` **(I/O & Config Routines)** (Impact: 26.1)
    * *Intent:* // // AM_drawThings() // // Draws the things on the automap in double IDDT cheat mode // // Passed c...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 193 instances
* *State Mutation (weighted view):* 630
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 279`, `structural_boundaries: 100`, `args: 46`, `func_start: 31`, `class_start: 3`
* *Risk/State:* `state_mutation: 244`, `fragile_debt: 2`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 14`
* *Defense:* None
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.395
  * `Choke Point (Betweenness):` 0.002149 | `Ripple Effect (Closeness):` 0.099822
  * `Imports (Out-Degree: 19):` am_map.h, config.h, d_deh.h, doomstat.h, dstrings.h, g_game.h, lprintf.h, p_maputl.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `components/prboom/p_floor.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.397)
- **Top Global Matches:** file_cluster_3: 9.397, file_cluster_8: 15.293, file_cluster_6: 28.102
- **Magnitude:** 1086.48 | **LOC:** 1043 | **CtrlFlow:** 22.1% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **7**; blast radius 2.893; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.5%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (66.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
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
* *Risk/State:* `state_mutation: 259`, `planned_debt: 1`, `fragile_debt: 5`, `unreferenced_by_name: 5`
* *Architecture:* `api: 8`, `import: 7`
* *Defense:* `doc: 4`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.893
  * `Choke Point (Betweenness):` 0.000222 | `Ripple Effect (Closeness):` 0.082206
  * `Imports (Out-Degree: 11):` doomstat.h, p_map.h, p_spec.h, p_tick.h, r_main.h, s_sound.h, sounds.h
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `components/prboom/r_things.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 6.438)
- **Top Global Matches:** file_cluster_8: 6.438, file_cluster_6: 10.732, file_cluster_4: 19.316
- **Magnitude:** 1064.78 | **LOC:** 1079 | **CtrlFlow:** 26.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **10**; blast radius 2.476; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (75.6%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_DrawSprite` **(Compute Cores)** (Impact: 82.5)
    * *Intent:* // // R_DrawSprite //
  * `R_ProjectSprite` **(Many-Argument Workhorses)** (Impact: 72.4)
    * *Intent:* // // R_ProjectSprite // Generates a vissprite for a thing if it might be visible. //
  * `R_DrawPSprite` **(Many-Argument Workhorses)** (Impact: 49.5)
    * *Intent:* // // R_DrawPSprite //
  * `R_InitSpriteDefs` **(Compute Cores)** (Impact: 33.7)
    * *Intent:* // a letter for the frame, and a number for the rotation. // // A sprite that is flippable will have...
  * `R_DrawVisSprite` **(Many-Argument Workhorses)** (Impact: 27.5)
    * *Intent:* // // R_DrawVisSprite // mfloorclip and mceilingclip should also be set. // // CPhipps - new wad lum...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 3 instances
* *Amplified Cascading Flux:* 221 instances
* *Memory Alloc (weighted view):* 2
* *State Mutation (weighted view):* 686
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 178`, `structural_boundaries: 48`, `args: 25`, `func_start: 15`, `class_start: 4`
* *Risk/State:* `state_mutation: 244`, `dead_code: 3`, `unreferenced_by_name: 3`
* *Architecture:* `api: 8`, `import: 10`
* *Defense:* `safety: 5`, `immutability_locks: 13`, `cleanup: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.476
  * `Choke Point (Betweenness):` 0.002634 | `Ripple Effect (Closeness):` 0.09164
  * `Imports (Out-Degree: 19):` doomstat.h, lprintf.h, r_bsp.h, r_draw.h, r_fps.h, r_main.h, r_segs.h, r_things.h...
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `components/prboom/p_inter.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.708)
- **Top Global Matches:** file_cluster_3: 9.708, file_cluster_8: 15.18, file_cluster_6: 27.925
- **Magnitude:** 997.62 | **LOC:** 914 | **CtrlFlow:** 38.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **12**; blast radius 2.677; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Complexity Load (formerly Cognitive Load) (82.5%), Guard Balance (formerly Safety Score) (81.6%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_TouchSpecialThing` **(Many-Argument Workhorses)** (Impact: 182.2)
    * *Intent:* // // P_TouchSpecialThing //
  * `P_DamageMobj` **(Many-Argument Workhorses)** (Impact: 138.1)
    * *Intent:* // // P_DamageMobj // Damages both enemies and players // "inflictor" is the thing that caused the d...
  * `P_KillMobj` **(Many-Argument Workhorses)** (Impact: 71.4)
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
* *Risk/State:* `state_mutation: 158`, `fragile_debt: 4`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 13`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.677
  * `Choke Point (Betweenness):` 0.001591 | `Ripple Effect (Closeness):` 0.091142
  * `Imports (Out-Degree: 20):` am_map.h, d_deh.h, doomstat.h, dstrings.h, lprintf.h, m_random.h, p_enemy.h, p_inter.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

### `components/prboom/r_segs.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_3` (Centroid distance: 9.909)
- **Top Global Matches:** file_cluster_3: 9.909, file_cluster_8: 30.19, file_cluster_1: 40.482
- **Magnitude:** 894.02 | **LOC:** 857 | **CtrlFlow:** 23.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **2** in-repo importer(s); it depends on **11**; blast radius 2.335; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `R_StoreWallRange` **(Many-Argument Workhorses)** (Impact: 166.2)
    * *Intent:* // // R_StoreWallRange // A wall segment will be drawn // between start and stop pixels (inclusive)....
  * `R_RenderMaskedSegRange` **(Many-Argument Workhorses)** (Impact: 42.8)
    * *Intent:* // // R_RenderMaskedSegRange //
  * `R_RenderSegLoop` **(I/O & Config Routines)** (Impact: 39.3)
    * *Intent:* // // R_RenderSegLoop // Draws zero, one, or two textures (and possibly a masked texture) for walls....
  * `R_ScaleFromGlobalAngle` **(Stateful Encapsulated Methods)** (Impact: 6.2)
    * *Intent:* // // R_ScaleFromGlobalAngle // Returns the texture mapping scale // for the current line (horizonta...
  * `R_PointToDist` **(Stateful Encapsulated Methods)** (Impact: 4.2)
    * *Intent:* // killough 5/2/98: move from r_main.c, made static, simplified
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 198 instances
* *State Mutation (weighted view):* 620
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 134`, `structural_boundaries: 15`, `args: 8`, `func_start: 5`
* *Risk/State:* `state_mutation: 224`, `dead_code: 3`, `fragile_debt: 2`, `unreferenced_by_name: 2`
* *Architecture:* `api: 4`, `import: 11`
* *Defense:* `safety: 3`, `immutability_locks: 4`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.335
  * `Choke Point (Betweenness):` 0.000138 | `Ripple Effect (Closeness):` 0.07076
  * `Imports (Out-Degree: 20):` doomstat.h, esp_attr.h, lprintf.h, r_bsp.h, r_draw.h, r_main.h, r_plane.h, r_segs.h...
  * `Imported By (In-Degree: 2):` (Excluded from Brief to save tokens)

### `components/prboom/p_switch.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 9.371)
- **Top Global Matches:** file_cluster_8: 9.371, file_cluster_6: 11.639, file_cluster_4: 19.601
- **Magnitude:** 855.24 | **LOC:** 1151 | **CtrlFlow:** 46.9% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **4** in-repo importer(s); it depends on **8**; blast radius 2.429; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (60.2%), Guard Balance (formerly Safety Score) (59.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_UseSpecialLine` **(Many-Argument Workhorses)** (Impact: 648.0)
    * *Intent:* // // P_UseSpecialLine // // // Called when a thing uses (pushes) a special line. // Only the front ...
  * `P_ChangeSwitchTexture` **(Compute Cores)** (Impact: 25.2)
    * *Intent:* // // P_ChangeSwitchTexture() // // Function that changes switch wall texture on activation. // // P...
  * `P_InitSwitchList` **(I/O & Config Routines)** (Impact: 15.2)
    * *Intent:* // when activated, and in the case of buttons, change back after a timeout. // // This routine modif...
  * `P_StartButton` **(Stateful Encapsulated Methods)** (Impact: 14.8)
    * *Intent:* // // P_StartButton() // // Start a button (retriggerable switch) counting down till it turns off. /...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 44 instances
* *State Mutation (weighted view):* 135
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 329`, `structural_boundaries: 178`, `args: 6`, `func_start: 4`
* *Risk/State:* `state_mutation: 47`, `dead_code: 1`, `unreferenced_by_name: 2`
* *Architecture:* `api: 3`, `import: 8`
* *Defense:* `immutability_locks: 2`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.429
  * `Choke Point (Betweenness):` 0.001473 | `Ripple Effect (Closeness):` 0.092143
  * `Imports (Out-Degree: 21):` doomstat.h, g_game.h, lprintf.h, p_spec.h, r_main.h, s_sound.h, sounds.h, w_wad.h
  * `Imported By (In-Degree: 4):` (Excluded from Brief to save tokens)

### `components/prboom/p_saveg.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 11.389)
- **Top Global Matches:** file_cluster_4: 11.389, file_cluster_6: 11.492, file_cluster_12: 14.569
- **Magnitude:** 850.26 | **LOC:** 1030 | **CtrlFlow:** 15.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **1** in-repo importer(s); it depends on **10**; blast radius 2.143; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (89.8%), Debt Markers (formerly Tech Debt) (82.7%), Test Surface (formerly Verification) (80.0%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_ArchiveSpecials` **(I/O & Config Routines)** (Impact: 47.2)
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
* *Structure:* `branch: 105`, `structural_boundaries: 76`, `args: 20`, `func_start: 16`, `class_start: 2`
* *Risk/State:* `safety_bypasses: 40`, `state_mutation: 259`, `dead_code: 2`, `fragile_debt: 3`, `unreferenced_by_name: 14`
* *Architecture:* `api: 15`, `import: 10`
* *Defense:* `safety: 6`, `immutability_locks: 4`, `cleanup: 1`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.143
  * `Choke Point (Betweenness):` 0.002357 | `Ripple Effect (Closeness):` 0.093687
  * `Imports (Out-Degree: 19):` am_map.h, doomstat.h, lprintf.h, m_random.h, p_enemy.h, p_maputl.h, p_saveg.h, p_spec.h...
  * `Imported By (In-Degree: 1):` (Excluded from Brief to save tokens)

### `components/prboom/r_patch.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_6` (Centroid distance: 5.916)
- **Top Global Matches:** file_cluster_6: 5.916, file_cluster_4: 10.382, file_cluster_8: 15.246
- **Magnitude:** 838.46 | **LOC:** 788 | **CtrlFlow:** 26.7% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **8** in-repo importer(s); it depends on **13**; blast radius 3.056; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (87.9%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `createTextureCompositePatch` **(Many-Argument Workhorses)** (Impact: 90.1)
    * *Intent:* //---------------------------------------------------------------------------
  * `createPatch` **(Many-Argument Workhorses)** (Impact: 53.5)
    * *Intent:* //---------------------------------------------------------------------------
  * `getPatchIsNotTileable` **(Stateful Encapsulated Methods)** (Impact: 28.2)
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
* *Risk/State:* `safety_bypasses: 8`, `state_mutation: 208`, `dead_code: 4`, `unreferenced_by_name: 7`
* *Architecture:* `api: 15`, `import: 13`
* *Defense:* `safety: 5`, `immutability_locks: 67`, `cleanup: 5`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 3.056
  * `Choke Point (Betweenness):` 0.002091 | `Ripple Effect (Closeness):` 0.131016
  * `Imports (Out-Degree: 14):` assert.h, doomstat.h, i_system.h, lprintf.h, p_tick.h, r_bsp.h, r_draw.h, r_main.h...
  * `Imported By (In-Degree: 8):` (Excluded from Brief to save tokens)

### `components/prboom/mmus2mid.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.208)
- **Top Global Matches:** file_cluster_4: 5.208, file_cluster_16: 9.883, file_cluster_6: 10.704
- **Magnitude:** 650.42 | **LOC:** 870 | **CtrlFlow:** 19.8% | **Authorship Centralization:** 0.0%
- **Blast Radius:** nothing in-repo imports it (entrypoint or orphan); it depends on **12**; blast radius 2.096; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (83.2%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (71.2%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `mmus2mid` **(Many-Argument Workhorses)** (Impact: 145.4)
    * *Intent:* // // mmus2mid() // // Convert a memory buffer contain MUS data to an Allegro MIDI structure // with...
  * `main` **(Many-Argument Workhorses)** (Impact: 31.1)
    * *Intent:* #ifdef STANDALONE /* this code unused by BOOM provided for future portability */ /* it also provides...
  * `MidiToMIDI` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* // // MidiToMIDI() // // Convert an in-memory copy of a MIDI format 0 or 1 file to // an Allegro MID...
  * `MIDIToMidi` **(Many-Argument Workhorses)** (Impact: 14.7)
    * *Intent:* // // MIDIToMidi() // // This routine converts an Allegro MIDI structure to a midi 1 format file // ...
  * `TWriteVarLen` **(Stateful Encapsulated Methods)** (Impact: 13.2)
    * *Intent:* // // TWriteVarLen() // // write the ULONG value to tracknum-th track, in midi format, which is // b...
**Contextual Mitigations & Amplifications:**
* *Mitigated Memory Allocs:* 13 instances
* *Amplified Cascading Flux:* 116 instances
* *Memory Alloc (weighted view):* 3
* *State Mutation (weighted view):* 370
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 103`, `structural_boundaries: 62`, `args: 37`, `func_start: 13`, `class_start: 3`
* *Risk/State:* `safety_bypasses: 4`, `high_risk_execution: 8`, `state_mutation: 138`, `dead_code: 1`, `unreferenced_by_name: 3`
* *Architecture:* `io: 6`, `api: 8`, `import: 13`
* *Defense:* `safety: 7`, `immutability_locks: 4`, `cleanup: 12`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.096
  * `Choke Point (Betweenness):` 0.0 | `Ripple Effect (Closeness):` 0.0
  * `Imports (Out-Degree: 6):` allegro.h, config.h, ctype.h, lprintf.h, m_swap.h, mmus2mid.h, stdio.h, stdlib.h...
  * `Imported By (In-Degree: 0):` None (Orphan / Entrypoint)

### `components/prboom/p_maputl.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 6.137)
- **Top Global Matches:** file_cluster_4: 6.137, file_cluster_9: 8.779, file_cluster_16: 9.347
- **Magnitude:** 634.96 | **LOC:** 684 | **CtrlFlow:** 24.5% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **7** in-repo importer(s); it depends on **6**; blast radius 2.855; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Guard Balance (formerly Safety Score) (86.4%), Test Surface (formerly Verification) (80.0%), Complexity Load (formerly Cognitive Load) (72.7%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_PathTraverse` **(Many-Argument Workhorses)** (Impact: 61.4)
    * *Intent:* // // P_PathTraverse // Traces a line from x1,y1 to x2,y2, // calling the traverser function for eac...
  * `P_BoxOnLineSide` **(Compute Cores)** (Impact: 20.3)
    * *Intent:* // // P_BoxOnLineSide // Considers the line to be infinite // Returns side 0 or 1, -1 if box crosses...
  * `P_BlockLinesIterator` **(Compute Cores)** (Impact: 19.4)
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
* *Risk/State:* `state_mutation: 132`, `unreferenced_by_name: 6`
* *Architecture:* `api: 14`, `import: 6`
* *Defense:* `safety: 2`, `immutability_locks: 11`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.855
  * `Choke Point (Betweenness):` 0.000682 | `Ripple Effect (Closeness):` 0.09164
  * `Imports (Out-Degree: 9):` doomstat.h, m_bbox.h, p_map.h, p_maputl.h, p_setup.h, r_main.h
  * `Imported By (In-Degree: 7):` (Excluded from Brief to save tokens)

### `components/prboom/p_doors.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_8` (Centroid distance: 5.516)
- **Top Global Matches:** file_cluster_8: 5.516, file_cluster_6: 17.033, file_cluster_3: 19.388
- **Magnitude:** 579.72 | **LOC:** 712 | **CtrlFlow:** 33.0% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **3** in-repo importer(s); it depends on **9**; blast radius 2.357; role: Pure Consumer (Orchestrator)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (75.9%), Complexity Load (formerly Cognitive Load) (68.8%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `T_VerticalDoor` **(Compute Cores)** (Impact: 112.7)
    * *Intent:* // Door action routines, called once per tick // ///////////////////////////////////////////////////...
  * `EV_VerticalDoor` **(Many-Argument Workhorses)** (Impact: 108.3)
    * *Intent:* // // EV_VerticalDoor // // Handle opening a door manually, no tag value // // Passed the line activ...
  * `EV_DoLockedDoor` **(Many-Argument Workhorses)** (Impact: 32.5)
    * *Intent:* // // Door linedef handlers // /////////////////////////////////////////////////////////////// // //...
  * `EV_DoDoor` **(Many-Argument Workhorses)** (Impact: 28.4)
    * *Intent:* // // EV_DoDoor // // Handle opening a tagged door // // Passed the line activating the door and the...
  * `P_SpawnDoorRaiseIn5Mins` **(Compute Cores)** (Impact: 3.0)
    * *Intent:* // // P_SpawnDoorRaiseIn5Mins() // // Spawn a door that opens after 5 minutes (called at level init)...
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 82 instances
* *State Mutation (weighted view):* 277
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 154`, `structural_boundaries: 64`, `args: 7`, `func_start: 6`
* *Risk/State:* `safety_bypasses: 1`, `state_mutation: 113`, `planned_debt: 2`, `unreferenced_by_name: 4`
* *Architecture:* `api: 6`, `import: 9`
* *Defense:* `doc: 6`
* *Network Topology:*
  * `Ecosystem Role:` Pure Consumer (Orchestrator) | `Dependency Blast Radius (PageRank):` 2.357
  * `Choke Point (Betweenness):` 0.000148 | `Ripple Effect (Closeness):` 0.081015
  * `Imports (Out-Degree: 16):` d_deh.h, doomstat.h, dstrings.h, lprintf.h, p_spec.h, p_tick.h, r_main.h, s_sound.h...
  * `Imported By (In-Degree: 3):` (Excluded from Brief to save tokens)

### `components/prboom/p_pspr.c` (C | Tier 1.5 | AI Safe: 0.0%)
- **Global Archetype:** `file_cluster_4` (Centroid distance: 5.952)
- **Top Global Matches:** file_cluster_4: 5.952, file_cluster_15: 8.558, file_cluster_16: 9.04
- **Magnitude:** 576.08 | **LOC:** 830 | **CtrlFlow:** 26.4% | **Authorship Centralization:** 0.0%
- **Blast Radius:** changing it is visible to **6** in-repo importer(s); it depends on **11**; blast radius 2.655; role: Transceiver (Middle-Tier)
- **Top Surface Vectors:** Mutation Surface (formerly State Flux) (100.0%), Debt Markers (formerly Tech Debt) (93.2%), Test Surface (formerly Verification) (80.0%), Guard Balance (formerly Safety Score) (74.4%)
- **Documentation Coverage:** 100.0% of unit weight undocumented
**Top Internal Functions/Classes:**
  * `P_SwitchWeapon` **(Compute Cores)** (Impact: 52.3)
    * *Intent:* // P_SwitchWeapon checks current ammo levels and gives you the // most preferred weapon with ammo. I...
  * `P_WeaponPreferred` **(Compute Cores)** (Impact: 28.4)
    * *Intent:* // killough 5/2/98: whether consoleplayer prefers weapon w1 over weapon w2.
  * `A_WeaponReady` **(Compute Cores)** (Impact: 23.0)
    * *Intent:* // // A_WeaponReady // The player can fire the weapon // or change to another weapon at this time. /...
  * `A_Saw` **(Compute Cores)** (Impact: 19.5)
    * *Intent:* // // A_Saw //
  * `P_SetPsprite` **(Stateful Encapsulated Methods)** (Impact: 15.9)
    * *Intent:* // // P_SetPsprite //
**Contextual Mitigations & Amplifications:**
* *Amplified Cascading Flux:* 83 instances
* *State Mutation (weighted view):* 261
**Structural Signatures (Net Mitigated Signals):**
* *Structure:* `branch: 124`, `structural_boundaries: 62`, `args: 37`, `func_start: 32`
* *Risk/State:* `state_mutation: 95`, `unreferenced_by_name: 24`
* *Architecture:* `api: 27`, `import: 11`
* *Defense:* `immutability_locks: 1`
* *Network Topology:*
  * `Ecosystem Role:` Transceiver (Middle-Tier) | `Dependency Blast Radius (PageRank):` 2.655
  * `Choke Point (Betweenness):` 0.002313 | `Ripple Effect (Closeness):` 0.101637
  * `Imports (Out-Degree: 20):` d_event.h, doomstat.h, m_random.h, p_enemy.h, p_inter.h, p_map.h, p_pspr.h, r_demo.h...
  * `Imported By (In-Degree: 6):` (Excluded from Brief to save tokens)

## 12. ARCHITECTURAL DRIFT ANOMALIES & ANTI-PATTERNS
> **AI CONTEXT:** 'Mixed-Responsibility' files sit almost equally close to two file archetypes (second-nearest centroid within 2% of the nearest), indicating a possible violation of the Single Responsibility Principle.

### Mixed-Responsibility Refactoring Targets for: file_cluster_11
- `components/prboom-esp32-compat/i_video.c` (C) | Magnitude: 89.38 | Delta: **0.14** (centroid distance) | Secondary Pull: `file_cluster_16`
  * Top Architectural Signatures: indent_spaces: 39, structural_boundaries: 28, args: 24, state_mutation: 23
- `components/prboom-esp32-compat/i_sound.c` (C) | Magnitude: 52.04 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 27, api: 20, args: 19, func_start: 19
- `components/prboom/native/i_sound.c` (C) | Magnitude: 52.04 | Delta: **0.144** (centroid distance) | Secondary Pull: `file_cluster_15`
  * Top Architectural Signatures: structural_boundaries: 27, api: 20, args: 19, func_start: 19

### Mixed-Responsibility Refactoring Targets for: file_cluster_16
- `components/prboom/hu_lib.c` (C) | Magnitude: 520.32 | Delta: **0.028** (centroid distance) | Secondary Pull: `file_cluster_4`
  * Top Architectural Signatures: indent_spaces: 286, pointers: 179, state_mutation: 104, branch: 80

### Mixed-Responsibility Refactoring Targets for: file_cluster_2
- `components/prboom/include/doomstat.h` (C) | Magnitude: 109.78 | Delta: **0.007** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 91, globals: 89, indent_spaces: 32, macros: 9
- `components/prboom-wad-tables/include/GAMMATBL.h` (C) | Magnitude: 13.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 2, immutability_locks: 1
- `components/prboom-wad-tables/include/SINETABL.h` (C) | Magnitude: 13.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 2, immutability_locks: 1
- `components/prboom-wad-tables/include/TANGTABL.h` (C) | Magnitude: 13.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 2, immutability_locks: 1
- `components/prboom-wad-tables/include/TANTOANG.h` (C) | Magnitude: 13.04 | Delta: **0.045** (centroid distance) | Secondary Pull: `file_cluster_17`
  * Top Architectural Signatures: api: 2, immutability_locks: 1

### Mixed-Responsibility Refactoring Targets for: file_cluster_4
- `components/prboom/p_saveg.c` (C) | Magnitude: 850.26 | Delta: **0.103** (centroid distance) | Secondary Pull: `file_cluster_6`
  * Top Architectural Signatures: indent_spaces: 621, pointers: 439, state_mutation: 259, branch: 105

## 12.5 STRATEGIC REFACTORING TARGETS (Volatility & Authorship Centralization)
> **AI CONTEXT:** Use these intersections to recommend pragmatic next steps. Risk is exponentially worse when combined with high churn (frequent edits) or high authorship centralization (single points of failure).

## 12.8 SYSTEMIC NETWORK BOTTLENECKS (N-Dimensional Topology)
> **AI CONTEXT:** These metrics cross-multiply Network Graph Theory against Risk Exposure to identify the exact mechanisms of runtime failure.

### ☣️ Cascading State Flux (Betweenness * State Flux)
These files act as structural bridges between components, but possess highly volatile, mutating state. They cause unpredictable side-effects for all downstream consumers.

- `components/prboom/g_game.c` -> **Severity: 6.091** (Bridge: 0.0609 * Flux: 100.0%)
- `components/prboom/r_main.c` -> **Severity: 4.27** (Bridge: 0.0427 * Flux: 100.0%)
- `components/prboom/d_client.c` -> **Severity: 3.676** (Bridge: 0.0368 * Flux: 100.0%)
- `components/prboom/w_wad.c` -> **Severity: 3.186** (Bridge: 0.0319 * Flux: 100.0%)
- `components/prboom/d_main.c` -> **Severity: 2.876** (Bridge: 0.0288 * Flux: 100.0%)

### 🃏 House of Cards (Closeness * Error Risk)
These files are deeply embedded (1 or 2 hops from the entire codebase) but possess high error exposure. A runtime exception here will cascade instantly across the application.

- `components/prboom/include/doomstat.h` -> **Severity: 16.073** (Embedded: 0.3235 * Error Risk: 49.6855%)
- `components/prboom/w_wad.c` -> **Severity: 13.728** (Embedded: 0.1694 * Error Risk: 81.0391%)
- `components/prboom/include/m_fixed.h` -> **Severity: 12.976** (Embedded: 0.2559 * Error Risk: 50.7142%)
- `components/prboom/include/doomdef.h` -> **Severity: 12.476** (Embedded: 0.2437 * Error Risk: 51.1846%)
- `components/prboom/v_video.c` -> **Severity: 12.36** (Embedded: 0.1386 * Error Risk: 89.1784%)

### 🙈 Opaque Critical Nodes (Dependency Blast Radius * Doc Risk)
These are 'Core Architecture Nodes' that the entire ecosystem relies upon, but they lack human intent, documentation, or ownership metadata. Modifying them is flying blind.

- `components/prboom/include/m_fixed.h` -> **Severity: 4019.5** (Blast Radius: 40.195 * Doc Risk: 100.0%)
- `components/prboom/lprintf.c` -> **Severity: 1071.2** (Blast Radius: 10.712 * Doc Risk: 100.0%)
- `components/prboom/r_draw.c` -> **Severity: 595.2** (Blast Radius: 5.952 * Doc Risk: 100.0%)
- `components/prboom/z_bmalloc.c` -> **Severity: 471.2** (Blast Radius: 4.712 * Doc Risk: 100.0%)
- `components/prboom/w_wad.c` -> **Severity: 457.2** (Blast Radius: 4.572 * Doc Risk: 100.0%)

## 14. PROJECT IDIOM WRAPPERS (Hidden Literal Vocabulary)
> **AI CONTEXT:** Project-local helpers that wrap a literal primitive (print, abort, allocation). Their call sites are NOT in the literal signal counts above -- read a low `debug_prints`/`panics_and_aborts`/`memory_alloc` count together with this list. Full detail in `wrapper_data`.

- **`debug_prints`:** 136 literal sites + 142 sites through wrappers = 278
- **`memory_alloc`:** 155 literal sites + 35 sites through wrappers = 190

- `lprintf` (function, debug_prints, primitive): 142 call sites in 31 files -- `components/prboom/lprintf.c`
- `P_AddActiveCeiling` (function, memory_alloc, primitive): 4 call sites in 3 files -- `components/prboom/p_ceilng.c`
- `P_RemoveActiveCeiling` (function, memory_alloc, primitive): 4 call sites in 1 files -- `components/prboom/p_ceilng.c`
- `FreeTracks` (function, memory_alloc, primitive): 3 call sites in 1 files -- `components/prboom/mmus2mid.c`
- `P_AddActivePlat` (function, memory_alloc, primitive): 3 call sites in 3 files -- `components/prboom/p_plats.c`
- `V_AllocScreen` (function, memory_alloc, primitive): 3 call sites in 2 files -- `components/prboom/v_video.c`
- `V_FreeScreen` (function, memory_alloc, primitive): 3 call sites in 2 files -- `components/prboom/v_video.c`
- `P_RemoveActivePlat` (function, memory_alloc, primitive): 2 call sites in 1 files -- `components/prboom/p_plats.c`
- `V_AllocScreens` (function, memory_alloc, via V_AllocScreen): 2 call sites in 2 files -- `components/prboom/v_video.c`
- `V_FreeScreens` (function, memory_alloc, via V_FreeScreen): 2 call sites in 2 files -- `components/prboom/v_video.c`
- `check_intercept` (function, memory_alloc, primitive): 2 call sites in 1 files -- `components/prboom/p_maputl.c`
- `new_visplane` (function, memory_alloc, primitive): 2 call sites in 1 files -- `components/prboom/r_plane.c`
*(+5 more in `wrapper_data`.)*

## 15. FUNCTION CALL RESOLUTION (Call Graph Confidence)
> **AI CONTEXT:** Each function's callee names, linked to the definition they most plausibly mean. *scoped* = same class/file, an imported file, or a class-qualified call; *unique* = the only definition in the repository; *ambiguous* = several candidates or an untyped receiver (never a graph edge); *external* = defined nowhere here (built-ins, packages). A high scoped/unique share means the resolver made a confident choice, not that the choice was correct; resolution accuracy is measured separately (gitgalaxy#3332). Detail in `fcall_data` / `fcall_rate_data`.

- **Repository:** 3541 call pairs -- scoped 24.9%, unique 39.5%, ambiguous 2.4%, external 33.3%

| Language | Pairs | Scoped | Unique | Ambiguous | External |
|---|---|---|---|---|---|
| c | 3524 | 25.0% | 39.5% | 2.4% | 33.1% |
| cpp | 16 | 0.0% | 31.2% | 6.2% | 62.5% |
| shell | 1 | 0.0% | 0.0% | 0.0% | 100.0% |

## APPENDIX A. STRUCTURAL SURFACE LEXICON (EQUATIONS & CONTEXT)
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

## AI SYSTEM INSTRUCTIONS (OUTPUT FORMAT)
> **CRITICAL TONE DIRECTIVE:** Stay in the Senior Technical Storyteller persona from Section 1. Use grounded, professional software engineering terminology (e.g., coupling, cohesion, technical debt, single responsibility) woven into a cohesive narrative -- not a dry, disconnected bullet-point audit. DO NOT use sci-fi, dramatic, or sensational jargon (e.g., 'Trojan', 'violently violates', 'parasitic', 'chimeric'). Be objective and factual, but write like you're explaining the codebase to a colleague, not filing a verdict.
> **When the user asks for an architectural review, structure your response using these directives:**
> 1. **Information Flow & Purpose (The Executive Summary):** Synthesize the overarching purpose of the codebase. Trace the information flow by analyzing the Top Dependencies ('Imports' and 'Imported By') and the Language Composition. Explain how the system's archetype drives its design, but only mention Z-Score deviations if they are highly abnormal.
> 2. **Notable Structures & Architecture:** Discuss the architecture based on the Dependency Graph. Identify the foundational load-bearers (highest inbound connections) versus the fragile orchestrators (highest outbound imports).
> 3. **Security & Vulnerabilities:** Immediately surface any critical threats flagged in the `AI THREAT INTELLIGENCE (XGBoost)` section. If none exist, briefly confirm the repository is secure from recognized structural threats.
> 4. **Outliers & Extremes:** Focus strictly on statistical anomalies. Highlight files or directory groups with high Structural Magnitude combined with a wide Blast Radius, severe Z-Scores (Architectural Drift), or extreme spikes in individual surface vectors (like Mutation Surface or Complexity Load). Do NOT sum the surface vectors together or treat any total of them as a score -- they are independently scaled meters in different units (#3112). Ignore normal, healthy code.
> 5. **Recommended Next Steps (Refactoring for Stability):** Provide 2-3 highly specific, pragmatic suggestions focused strictly on reducing outliers. Instruct the user on how to refactor high Z-score files, decouple massive central nodes, or mitigate extreme risk exposures to stabilize the system's architecture.
